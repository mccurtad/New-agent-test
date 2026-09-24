#!/usr/bin/env python3
"""Structural pre-flight check for a Canvas QTI 1.2 quiz package.

Usage:
    python3 validate_qti.py <package-dir-or-.zip>

Catches the mistakes a plain XML parse misses: manifest entries pointing at
missing files, mismatched identifiers, scoring rules that reference answers
that don't exist, item scores that don't total 100%, dropdown placeholders
with no matching dropdown, missing feedback blocks, and point/question
counts that disagree with assessment_meta.xml.

Passing this check does NOT prove Canvas will import the package correctly.
Always import into a sandbox course and click through every question.

Exit status: 0 = no errors (warnings allowed), 1 = errors found.
"""
import os
import re
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET

SUPPORTED_TYPES = {
    "multiple_choice_question", "true_false_question", "multiple_answers_question",
    "matching_question", "multiple_dropdowns_question", "fill_in_multiple_blanks_question",
    "short_answer_question", "numerical_question", "essay_question", "text_only_question",
}
SCORED_LID_TYPES = {"matching_question", "multiple_dropdowns_question",
                    "multiple_choice_question", "true_false_question",
                    "multiple_answers_question"}

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def local(tag):
    return tag.rsplit("}", 1)[-1]


def find_all(node, name):
    return [e for e in node.iter() if local(e.tag) == name]


def find_one(node, name):
    hits = find_all(node, name)
    return hits[0] if hits else None


def parse(path):
    try:
        return ET.parse(path).getroot()
    except ET.ParseError as e:
        err(f"{os.path.basename(path)}: not well-formed XML ({e})")
    except FileNotFoundError:
        err(f"{path}: file not found")
    return None


def metadata(item):
    out = {}
    for f in find_all(item, "qtimetadatafield"):
        label, entry = find_one(f, "fieldlabel"), find_one(f, "fieldentry")
        if label is not None and entry is not None:
            out[label.text] = (entry.text or "").strip()
    return out


def check_item(item, where):
    meta = metadata(item)
    qtype = meta.get("question_type")
    if qtype is None:
        err(f"{where}: missing question_type metadata")
    elif qtype not in SUPPORTED_TYPES:
        err(f"{where}: unrecognised question_type '{qtype}'")

    try:
        points = float(meta.get("points_possible", ""))
    except ValueError:
        err(f"{where}: points_possible missing or not a number")
        points = 0.0

    lids = {}
    for lid in find_all(item, "response_lid"):
        ident = lid.get("ident")
        if ident in lids:
            err(f"{where}: duplicate response_lid ident '{ident}'")
        labels = [l.get("ident") for l in find_all(lid, "response_label")]
        if len(labels) != len(set(labels)):
            err(f"{where}: duplicate response_label idents in '{ident}'")
        if not labels:
            err(f"{where}: response_lid '{ident}' has no answer choices")
        lids[ident] = set(labels)

    if qtype in SCORED_LID_TYPES:
        scored = set()
        for ve in find_all(item, "varequal"):
            rid, val = ve.get("respident"), (ve.text or "").strip()
            if rid not in lids:
                err(f"{where}: scoring references unknown response '{rid}'")
            elif val not in lids[rid]:
                err(f"{where}: scoring for '{rid}' expects answer '{val}', "
                    f"which is not one of its choices {sorted(lids[rid])}")
            scored.add(rid)
        if qtype in {"matching_question", "multiple_dropdowns_question"}:
            for rid in sorted(set(lids) - scored):
                err(f"{where}: '{rid}' has no correct answer defined")

        adds = [float(s.text) for s in find_all(item, "setvar")
                if s.get("action") == "Add" and s.text]
        sets = [float(s.text) for s in find_all(item, "setvar")
                if s.get("action") == "Set" and s.text]
        total = sum(adds) if adds else max(sets, default=0.0)
        if abs(total - 100) > 0.1:
            err(f"{where}: a fully correct answer scores {total:g}% (should be 100%)")

    if qtype == "multiple_dropdowns_question":
        text = " ".join((m.text or "") for m in find_all(find_one(item, "presentation"), "mattext")[:1])
        placeholders = set(re.findall(r"\[([^\[\]]+)\]", text))
        for rid in sorted(set(lids) - placeholders):
            err(f"{where}: dropdown '{rid}' has no [{rid}] placeholder in the question text")
        for ph in sorted(placeholders - set(lids)):
            err(f"{where}: placeholder [{ph}] has no matching dropdown")

    fb = {f.get("ident") for f in find_all(item, "itemfeedback")}
    for name in ("correct_fb", "general_incorrect_fb"):
        if name not in fb:
            warn(f"{where}: no '{name}' feedback block")

    return points


def validate_dir(root):
    manifest = parse(os.path.join(root, "imsmanifest.xml"))
    if manifest is None:
        err("imsmanifest.xml must sit at the top level of the package")
        return
    resources = [r for r in find_all(manifest, "resource")
                 if r.get("type") == "imsqti_xmlv1p2"]
    if not resources:
        err("imsmanifest.xml declares no resource of type imsqti_xmlv1p2")
    for res in resources:
        rid, href = res.get("identifier"), res.get("href")
        files = [f.get("href") for f in find_all(res, "file")]
        for f in files + ([href] if href else []):
            if not os.path.isfile(os.path.join(root, f)):
                err(f"manifest lists '{f}', which is not in the package")
        quiz_file = href or next((f for f in files if not f.endswith("assessment_meta.xml")), None)
        meta_file = next((f for f in files if f.endswith("assessment_meta.xml")), None)
        if meta_file is None:
            warn(f"resource '{rid}': no assessment_meta.xml (Canvas will use default quiz settings)")
        if not quiz_file or not os.path.isfile(os.path.join(root, quiz_file)):
            continue

        qti = parse(os.path.join(root, quiz_file))
        if qti is None:
            continue
        assessment = find_one(qti, "assessment")
        if assessment is None:
            err(f"{quiz_file}: no <assessment> element")
            continue
        if assessment.get("ident") != rid:
            warn(f"{quiz_file}: assessment ident '{assessment.get('ident')}' "
                 f"differs from manifest resource identifier '{rid}'")

        items = find_all(assessment, "item")
        if not items:
            err(f"{quiz_file}: contains no questions")
        idents = [i.get("ident") for i in items]
        for dup in sorted({i for i in idents if idents.count(i) > 1}):
            err(f"{quiz_file}: duplicate item ident '{dup}'")
        total_points = sum(check_item(it, f"item {it.get('ident')}") for it in items)

        if meta_file and os.path.isfile(os.path.join(root, meta_file)):
            qm = parse(os.path.join(root, meta_file))
            if qm is not None:
                if qm.get("identifier") != rid:
                    warn(f"{meta_file}: quiz identifier '{qm.get('identifier')}' "
                         f"differs from manifest resource identifier '{rid}'")
                qc = find_one(qm, "question_count")
                if qc is not None and qc.text and int(qc.text) != len(items):
                    err(f"{meta_file}: question_count is {qc.text}, but the quiz has {len(items)} items")
                for pp in find_all(qm, "points_possible"):
                    if pp.text and abs(float(pp.text) - total_points) > 0.01:
                        err(f"{meta_file}: points_possible is {pp.text}, "
                            f"but item points total {total_points:g}")
        print(f"Checked '{rid}': {len(items)} items, {total_points:g} points")


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    target = sys.argv[1]
    if zipfile.is_zipfile(target):
        with zipfile.ZipFile(target) as z, tempfile.TemporaryDirectory() as tmp:
            bad = [n for n in z.namelist() if n.startswith("/") or ".." in n.split("/")]
            if bad:
                err(f"zip contains unsafe paths: {bad}")
            else:
                z.extractall(tmp)
                validate_dir(tmp)
    elif os.path.isdir(target):
        validate_dir(target)
    else:
        print(f"Not a directory or .zip file: {target}")
        return 2

    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR:   {e}")
    print(f"{len(errors)} error(s), {len(warnings)} warning(s).")
    print("Reminder: a clean result is not a Canvas import test - "
          "import into a sandbox course and click through every question.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

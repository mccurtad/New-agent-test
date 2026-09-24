# Generating Canvas-Importable Quizzes (QTI)

A method for hand-authoring a QTI package that imports directly into Canvas,
without needing python-docx/pptx-style tooling — just well-formed XML.

## What QTI can and can't express

Standard QTI 1.2 (the format Canvas's importer accepts) reliably supports:

- **Matching** (`matching_question`) — pair each prompt with one of a shared
  set of choices. Usable as a stand-in for two things Canvas's newer "New
  Quizzes" engine has as dedicated native types but QTI can't express directly:
  - **Categorization** → Matching where the "choices" are the category names.
  - **Ordering** → Matching where the "choices" are position labels ("Step 1,"
    "Step 2," …).
- **Multiple Dropdowns** (`multiple_dropdowns_question`) — a passage of text
  with several inline `[blank]` placeholders, each with its own dropdown of
  options.

If you want the native drag-tile Categorization/Ordering widgets, those must
be built by hand directly in New Quizzes — QTI import will give you the
Matching-based equivalent instead, which is still auto-graded and still low
faculty effort, just a different interaction style.

## Package structure

```
your-quiz.zip
├── imsmanifest.xml                          # top-level manifest, lists resources
└── your_quiz_id/
    ├── your_quiz_id.xml                     # the actual questions (QTI 1.2)
    └── assessment_meta.xml                  # Canvas-specific quiz settings
```

- `imsmanifest.xml` declares one `resource` of type `imsqti_xmlv1p2` pointing
  at both files above.
- The main XML is `<questestinterop><assessment><section><item>...</item></section></assessment></questestinterop>`
  — one `<item>` per question, each with `<presentation>` (the question and
  its choices) and `<resprocessing>` (the scoring logic).
- `assessment_meta.xml` sets Canvas-specific quiz behavior: `quiz_type`
  (e.g. `practice_quiz` for ungraded practice), `allowed_attempts` (`-1` for
  unlimited), `show_correct_answers`, points, etc.

## Adding feedback

Canvas looks for two conventionally-named `<itemfeedback>` blocks inside each
`<item>`, after `</resprocessing>`:

```xml
<itemfeedback ident="correct_fb">
  <flow_mat><material><mattext texttype="text/plain">Correct! ...</mattext></material></flow_mat>
</itemfeedback>
<itemfeedback ident="general_incorrect_fb">
  <flow_mat><material><mattext texttype="text/plain">Not quite - ...</mattext></material></flow_mat>
</itemfeedback>
```

For a composite item type (Matching, Multiple Dropdowns), Canvas shows
`correct_fb` when every sub-answer is right and `general_incorrect_fb`
otherwise — you don't need extra `<respcondition>` wiring to trigger it, just
the two idents present with those exact names.

## Importing into Canvas

**Classic Quizzes:** Settings → Import Course Content → Content Type "QTI .zip
file" → upload. Lands as a Classic Quiz.

**New Quizzes:** a plain QTI import via course Settings lands as a Classic
Quiz *by default*, even in a New-Quizzes course. Two ways to actually get a
New Quiz:

- Settings → Import Course Content → QTI .zip file → check **"Convert content
  to New Quizzes"** before importing, or
- From inside New Quizzes: open (or create) a quiz → **Build** page → Options
  icon → **Import Content** → drag/drop the `.zip`.

## Validate before you ship it

```bash
python3 -c "import xml.etree.ElementTree as ET; ET.parse('your_quiz_id.xml')"
```

confirms the XML is at least well-formed. It does **not** confirm Canvas will
import it correctly — QTI import behavior (especially feedback display on
composite item types, and Classic→New-Quizzes conversion) is genuinely
finicky and hasn't been verified here against a live Canvas instance.
**Always import into a sandbox/test course first** and click through every
question before rolling a generated package into a real course.

## Worked example

[`assets/qti-example/`](../assets/qti-example/) (bundled with this skill; also at
[`examples/ban-6303/module-1-practice-quiz/`](../../../../examples/ban-6303/module-1-practice-quiz/) in the source repo)
is a complete, working QTI package: two Matching items, one Multiple Dropdowns
item, one Matching-as-Ordering item, all with feedback — built as an ungraded
practice quiz to reinforce a module's MLOs alongside its graded knowledge
check.

---
name: course-architect
description: Instructional-design workflow for a single course — audit and rewrite Course/Module-Level Objectives (CLOs/MLOs) against Bloom's taxonomy, check whether a module's real assessments measure its real objectives, generate Canvas-importable QTI practice quizzes, and design low-grading-overhead discussions and rubrics. Use when building, refining, or reviewing syllabus content, weekly modules, learning objectives, grading rubrics, assignment prompts, quizzes, or discussion boards.
---

# Course Architect

Act as a dedicated instructional designer and course architect for the course
whose materials are in the current repository. Work only on that course.

## Ground rules

- **Cross-reference existing course files first.** Before drafting or
  revising anything, read the syllabus, course map, and relevant module
  materials so new content stays consistent with established objectives,
  tone, terminology, and grading conventions.
- **Never mix courses.** Do not bring in objectives, data, or content from
  other courses (including the bundled BAN 6303 example, which is
  illustrative only).
- **Match the curriculum's academic level and voice.**
- **Work from real text, not titles or tags.** Read the actual quiz items,
  lab instructions, and prompts rather than trusting summaries or LMS
  alignment labels.
- **Flag uncertainty.** When a Bloom's classification is ambiguous or an LMS
  behavior is unverified, say so explicitly instead of presenting a guess
  as fact.

## Choose the workflow

| Task | Read first |
|---|---|
| Writing, auditing, or fixing CLOs/MLOs | [references/clo-mlo-alignment.md](references/clo-mlo-alignment.md) |
| Checking whether assessments cover the MLOs; closing gaps | [references/assessment-gap-analysis.md](references/assessment-gap-analysis.md) |
| Building an auto-graded Canvas quiz (QTI .zip) | [references/qti-quiz-generation.md](references/qti-quiz-generation.md), [examples/ban-6303/module-1-practice-quiz/](examples/ban-6303/module-1-practice-quiz/), and [scripts/validate_qti.py](scripts/validate_qti.py) |
| Designing a discussion prompt, peer reply, or rubric | [references/discussion-design.md](references/discussion-design.md) |

Load only the reference(s) the task needs. A full module review typically
runs them in order: alignment → gap analysis → close gaps with a quiz item or
discussion.

## Workflow summaries

**1. Objective alignment.** Enforce three rules: one verb per objective; a
measurable, observable verb; each MLO at or below the Bloom's level of the
CLO(s) it supports. Elevate CLOs to a common ceiling level, collapse compound
MLOs by converting the secondary verb into a method clause (`using ___`,
`by ___ing`, `based on ___`), lower any MLO that ties the ceiling, and choose
verbs that match the evidence the module actually collects. Present results
as a before/after table with the rationale for each change.

**2. Assessment gap analysis.** List the module's MLOs, extract the full text
of every assessment tied to the module, map each item to the MLO(s) it
actually tests (strong / partial / none), and build an MLO × assessment
coverage table. Flag mismatched tags explicitly. Prefer closing a gap by
adding an item to an existing graded assessment, and flag "Explain"/"Describe"
MLOs that lack any constructed-response evidence. Re-run the table after
every change.

**3. QTI quiz generation.** Use the bundled package in
[examples/ban-6303/module-1-practice-quiz/](examples/ban-6303/module-1-practice-quiz/)
as the structural template
(`imsmanifest.xml` + `<quiz_id>/<quiz_id>.xml` + `<quiz_id>/assessment_meta.xml`).
Use Matching for categorization and ordering, Multiple Dropdowns for
fill-in passages, and include `correct_fb` / `general_incorrect_fb` feedback
on each item. After writing the files, zip them with the manifest at the top
level and run the bundled validator on the result; fix every error before
handing the package over:

```bash
cd <package-dir> && zip -r <QuizName>.zip imsmanifest.xml <quiz_id>/
python3 <this-skill-dir>/scripts/validate_qti.py <QuizName>.zip
```

The validator checks structure and scoring logic only. Always give the user
the sandbox test checklist from
[references/qti-quiz-generation.md](references/qti-quiz-generation.md) and
state that the package has not been import-tested in Canvas.

**4. Discussion design.** Short initial post (~150–250 words) applying a
concept to a self-chosen example, plus a peer reply (~30–75 words) naming one
specific strength and one specific question or suggestion. Keep icebreakers
in Orientation, separate from content discussions. Offer a
Complete/Incomplete rubric by default and a 3-criterion point rubric when more
differentiation is warranted.

## Worked example

[examples/ban-6303/](examples/ban-6303/) contains a full before/after pass
(course map, coverage table, split discussion, and practice quiz). Use it as
a model of output format only; never copy its content into another course.

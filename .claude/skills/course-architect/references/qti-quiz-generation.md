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

**Step 1 — structural check.** Run the bundled validator on the package
directory or the finished `.zip`:

```bash
python3 scripts/validate_qti.py your-quiz.zip
```

Beyond well-formed XML, it checks that:

- `imsmanifest.xml` is at the top level of the zip and every file it lists
  exists;
- identifiers agree across the manifest, quiz XML, and `assessment_meta.xml`;
- every item has a recognised `question_type` and numeric `points_possible`;
- every scoring rule points to a real response and a real answer choice, and
  every Matching/Dropdown response has a correct answer;
- a fully correct answer scores exactly 100% of the item;
- every Multiple Dropdowns `[placeholder]` has a matching dropdown, and vice
  versa;
- `question_count` and `points_possible` in `assessment_meta.xml` match the
  items;
- `correct_fb` / `general_incorrect_fb` feedback blocks are present
  (warning only).

It exits non-zero on any error.

**Step 2 — sandbox import (required).** The validator cannot tell you how
Canvas will actually render or grade the package; QTI import behaviour
(especially feedback on composite item types, and Classic→New Quizzes
conversion) is finicky and has not been verified here against a live Canvas
instance. Import into a sandbox or test course first and work through this
checklist:

1. The import finishes without errors or warnings in the import log.
2. The quiz appears with the expected title, quiz type, attempts, and total
   points.
3. Every question appears, in order, with the expected question type.
4. Take the quiz as the Student View with **all answers correct**: the score
   is 100%, and each item shows its "correct" feedback.
5. Retake with **one wrong answer per item**: partial credit is as expected,
   and each item shows its "incorrect" feedback.
6. If you used "Convert content to New Quizzes", repeat steps 3–5 in the
   converted quiz, since conversion can change question types.

Only then copy the quiz into a live course.

## Worked example

[`examples/ban-6303/module-1-practice-quiz/`](../examples/ban-6303/module-1-practice-quiz/)
is a complete, working QTI package: two Matching items, one Multiple Dropdowns
item, one Matching-as-Ordering item, all with feedback — built as an ungraded
practice quiz to reinforce a module's MLOs alongside its graded knowledge
check.

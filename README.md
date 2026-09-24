# Course Architect Agent

A [Claude Code](https://claude.com/claude-code) subagent and methodology for
instructional design — auditing and fixing Course/Module-Level Objectives,
checking whether assessments actually measure what they claim to, generating
Canvas-importable quizzes, and designing low-effort discussion activities.

Built from a real, iterative working session with a course designer refining
a graduate business analytics course. This repo generalizes that work into a
template anyone can drop into their own course repo and adapt.

## What's here

| | |
|---|---|
| [`.claude/agents/course-architect.md`](.claude/agents/course-architect.md) | The subagent definition. Fill in `[COURSE NAME]` and `[COURSE CODE]`, drop it in your own repo's `.claude/agents/`, and Claude Code will treat it as a dedicated instructional-design assistant scoped to that course. |
| [`docs/clo-mlo-alignment.md`](docs/clo-mlo-alignment.md) | Three rules for well-formed objectives (one verb, measurable, correct Bloom's hierarchy) and the technique for fixing objectives that break them. |
| [`docs/assessment-gap-analysis.md`](docs/assessment-gap-analysis.md) | How to check whether a module's real assessments measure its real objectives — not just what they're tagged with. |
| [`docs/qti-quiz-generation.md`](docs/qti-quiz-generation.md) | How to hand-author a Canvas-importable QTI quiz package (Matching, Multiple Dropdowns, feedback) without any special tooling. |
| [`docs/discussion-design.md`](docs/discussion-design.md) | A short-discussion + peer-reply pattern that gets genuine written evidence of understanding *and* student-to-student connection, without heavy grading. |
| [`examples/ban-6303/`](examples/ban-6303/) | A full worked example — a real course's CLOs/MLOs before and after the alignment pass, a coverage table, a split icebreaker/content discussion, and a working QTI practice quiz. |

## Quickstart — using this for your own course

1. Copy `.claude/agents/course-architect.md` into your own course repo's
   `.claude/agents/` folder.
2. Replace `[COURSE NAME]` and `[COURSE CODE]` with your course's actual name
   and code.
3. Put your syllabus, course map, and module materials in that repo so the
   agent has something to cross-reference.
4. Read through `docs/clo-mlo-alignment.md` and run the same three-rule check
   against your own CLOs/MLOs.
5. As you build or review assessments, use `docs/assessment-gap-analysis.md`
   to check real coverage, `docs/qti-quiz-generation.md` if you want an
   auto-graded practice quiz, and `docs/discussion-design.md` for any
   objective that needs a written, constructed-response check.

None of this requires Claude Code specifically — the docs describe a method a
human instructional designer can follow by hand. The subagent file is what
makes it repeatable inside Claude Code: point it at your course repo and ask
it to run the same checks.

## What this isn't

- Not a full LMS integration — the QTI output is a file you import manually,
  and hasn't been verified against every Canvas configuration (see the
  caveats in `docs/qti-quiz-generation.md`). Always test in a sandbox course
  first.
- Not accessibility (WCAG) tooling — this is about instructional alignment
  and assessment design, not web/document accessibility.
- Not specific to machine-learning or business courses — the BAN 6303 example
  is illustrative only; the method and templates are subject-agnostic.

## License

[MIT](LICENSE) — use, adapt, and redistribute freely.

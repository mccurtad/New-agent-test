# Course Architect Skill

A [Claude Code](https://claude.com/claude-code) skill (plus an optional subagent) and methodology for
instructional design — auditing and fixing Course/Module-Level Objectives,
checking whether assessments actually measure what they claim to, generating
Canvas-importable quizzes, and designing low-effort discussion activities.

Built from a real, iterative working session with a course designer refining
a graduate business analytics course. This repo generalizes that work into a
template anyone can drop into their own course repo and adapt.

## What's here

| | |
|---|---|
| [`.claude/skills/course-architect/`](.claude/skills/course-architect/) | **The skill.** `SKILL.md` holds the workflow; `references/` holds the four methodology guides below; `examples/` holds the worked example; `scripts/validate_qti.py` checks generated quiz packages. The folder is self-contained. Copy the folder into any course repo's `.claude/skills/` (or `~/.claude/skills/` for all projects) and Claude Code loads it automatically when the task matches. |
| [`references/clo-mlo-alignment.md`](.claude/skills/course-architect/references/clo-mlo-alignment.md) | Three rules for well-formed objectives (one verb, measurable, correct Bloom's hierarchy) and the technique for fixing objectives that break them. |
| [`references/assessment-gap-analysis.md`](.claude/skills/course-architect/references/assessment-gap-analysis.md) | How to check whether a module's real assessments measure its real objectives — not just what they're tagged with. |
| [`references/qti-quiz-generation.md`](.claude/skills/course-architect/references/qti-quiz-generation.md) | How to hand-author a Canvas-importable QTI quiz package (Matching, Multiple Dropdowns, feedback) without any special tooling. |
| [`references/discussion-design.md`](.claude/skills/course-architect/references/discussion-design.md) | A short-discussion + peer-reply pattern that gets genuine written evidence of understanding *and* student-to-student connection, without heavy grading. |
| [`.claude/agents/course-architect.md`](.claude/agents/course-architect.md) | Optional subagent that preloads the skill. Fill in `[COURSE NAME]` and `[COURSE CODE]` if you want a dedicated, course-scoped assistant with restricted tools. |
| [`examples/ban-6303/`](.claude/skills/course-architect/examples/ban-6303/) | A full worked example — a real course's CLOs/MLOs before and after the alignment pass, a coverage table, a split icebreaker/content discussion, and a working QTI practice quiz. |

## Quickstart — using this for your own course

1. Copy the `.claude/skills/course-architect/` folder into your own course
   repo's `.claude/skills/` folder (or into `~/.claude/skills/` to use it
   across every project).
2. Put your syllabus, course map, and module materials in that repo so the
   skill has something to cross-reference.
3. Ask Claude Code for course-design work — e.g. "audit the Module 3 MLOs",
   "check whether the Module 2 assessments cover their objectives", or
   "build a practice quiz for Module 4". The skill loads automatically; you
   can also invoke it directly with `/course-architect`.
4. Optionally, also copy `.claude/agents/course-architect.md` into
   `.claude/agents/` and replace `[COURSE NAME]` and `[COURSE CODE]` for a
   dedicated course-scoped subagent that preloads the skill.

None of this requires Claude Code specifically — the docs describe a method a
human instructional designer can follow by hand. The skill is what makes
it repeatable inside Claude Code: drop it into your course repo and ask it to
run the same checks.

## What this isn't

- Not a full LMS integration — the QTI output is a file you import manually,
  and hasn't been verified against every Canvas configuration.
  `scripts/validate_qti.py` catches structural and scoring errors, but always
  run the sandbox checklist in `references/qti-quiz-generation.md` before
  using a quiz in a live course.
- Not accessibility (WCAG) tooling — this is about instructional alignment
  and assessment design, not web/document accessibility.
- Not specific to machine-learning or business courses — the BAN 6303 example
  is illustrative only; the method and templates are subject-agnostic.

## License

[MIT](LICENSE) — use, adapt, and redistribute freely.

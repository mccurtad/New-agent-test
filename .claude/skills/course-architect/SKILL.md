---
name: course-architect
description: Hand an instructional-design task for this repository's course to the course-architect subagent. Covers syllabus content, weekly modules, grading rubrics, assignment prompts, CLO/MLO alignment, assessment gap analysis, QTI quizzes, and discussion design. Use when the user types /course-architect or asks for course-design work on this course.
argument-hint: "[task, e.g. audit Module 2 objectives]"
---

# Course Architect

Delegate the user's request to the `course-architect` subagent
(`.claude/agents/course-architect.md`) using the Agent tool with
`subagent_type: "course-architect"`.

User's request: $ARGUMENTS

## Steps

1. **No request given.** If the request above is empty, don't launch the
   subagent. Ask the user which task they want. Offer these options:
   - checking course and module objectives (`docs/clo-mlo-alignment.md`)
   - checking assessment coverage (`docs/assessment-gap-analysis.md`)
   - building a Canvas QTI quiz (`docs/qti-quiz-generation.md`)
   - designing a discussion activity (`docs/discussion-design.md`)
   - drafting syllabus, module, rubric or assignment content
2. **Placeholders still in the agent file.** If
   `.claude/agents/course-architect.md` still contains `[COURSE NAME]` or
   `[COURSE CODE]`, ask the user for the course name and code. Replace the
   placeholders before you delegate.
3. **Prompt for the subagent.** The subagent sees nothing from this
   conversation, so give it a self-contained prompt. Include:
   - the user's request, word for word
   - the relevant course files and `docs/` method files it should read
   - the output expected (edits to files, or a report)
4. **Relay the results.** Summarize for the user what the subagent produced
   or changed, with file paths. Point out anything it flagged as uncertain.
   If files changed, commit them with a clear message. Push only if the
   session's instructions call for it.

---
name: course-architect
description: Hand an instructional-design task for one course to the course-architect subagent. Covers syllabus content, weekly modules, grading rubrics, assignment prompts, CLO/MLO alignment, assessment gap analysis, QTI quizzes, and discussion design. Use when the user types /course-architect or asks for course-design work.
argument-hint: "[course code] [task], e.g. BAN6303 audit Module 2 objectives"
---

# Course Architect

Delegate the user's request to the `course-architect` subagent
(`.claude/agents/course-architect.md`) using the Agent tool with
`subagent_type: "course-architect"`.

User's request: $ARGUMENTS

Each chat covers one course. The agent file stays generic, so never write a
course name into it.

## Steps

1. **Work out the course.**
   - If an earlier message in this chat set the course, use it.
   - Otherwise take the course code from the request, if it has one.
   - Otherwise ask the user for the course name and code.
   - The course's materials live in `courses/<COURSE-CODE>/` (uppercase, no
     spaces, e.g. `courses/BAN6303/`).
   - If that folder doesn't exist, confirm the name and code with the user,
     then create it with a `course.md` file recording the name, code, and
     any level or tone notes the user gives.
2. **No task given.** If the request contains no task, don't launch the
   subagent. Ask the user which task they want. Offer these options:
   - checking course and module objectives (`docs/clo-mlo-alignment.md`)
   - checking assessment coverage (`docs/assessment-gap-analysis.md`)
   - building a Canvas QTI quiz (`docs/qti-quiz-generation.md`)
   - designing a discussion activity (`docs/discussion-design.md`)
   - drafting syllabus, module, rubric or assignment content
3. **Prompt for the subagent.** The subagent sees nothing from this
   conversation, so give it a self-contained prompt. Include:
   - the course name, code, and folder
   - the user's request, word for word
   - the relevant files in that folder and the `docs/` method files to read
   - the output expected (edits to files, or a report)
4. **Relay the results.** Summarize for the user what the subagent produced
   or changed, with file paths. Point out anything it flagged as uncertain.
   If files changed, commit them with a clear message that names the course
   code. Push only if the session's instructions call for it.

# CLO / MLO Alignment Guide

A method for auditing and fixing Course-Level Objectives (CLOs) and Module-Level
Objectives (MLOs) so they follow standard instructional-design rules and form a
clean Bloom's-taxonomy hierarchy.

## The three rules

1. **Each objective has exactly one verb.** "Evaluate, compare, and improve
   models" is really three objectives stapled together — split it or pick one.
2. **Each objective is clearly measurable.** Vague verbs ("work with," "explore,"
   "understand") don't tell you what evidence would count as mastery. Prefer
   concrete, observable verbs.
3. **An MLO must sit at or below the Bloom's level of the CLO(s) it supports.**
   A module-level objective is a building block toward the course-level outcome
   — it should never ask for more advanced thinking than the CLO it's supposed
   to feed into.

## Bloom's Revised Taxonomy reference

| Level | Verbs (examples) |
|---|---|
| 1. Remember | define, list, recall, identify, name, state |
| 2. Understand | explain, describe, summarize, interpret, discuss, paraphrase |
| 3. Apply | apply, use, implement, demonstrate, fit, prepare, employ |
| 4. Analyze | analyze, compare, contrast, distinguish, examine, differentiate |
| 5. Evaluate | evaluate, assess, critique, judge, justify, select, choose |
| 6. Create | design, construct, develop, formulate, build, generate, synthesize |

Some verbs are genuinely ambiguous across charts (e.g. "distinguish" sits on the
Understand/Analyze boundary in different sources, "build" is Apply in some
charts and Create in others). Pick one interpretation, note it, and apply it
consistently — the internal consistency matters more than which chart you cite.

## The fix pattern

**Step 1 — Elevate the CLOs.** Rewrite each CLO as a single, high-level
(typically Create-level) verb. Putting every CLO at the *same* ceiling level
solves a subtle problem: once all CLOs sit at the top of the taxonomy, any MLO
below Create automatically satisfies rule 3, regardless of which CLO(s) it's
tagged to. You don't have to separately verify each MLO against each CLO's
specific level.

**Step 2 — Collapse compound MLOs to one verb.** For an MLO like "Fit and
interpret a logistic regression model," don't just delete a verb — decide
which action is actually being assessed (usually the more advanced one) and
fold the other into a method clause:

- `"Fit and interpret X"` → `"Interpret a fitted X"`
- `"Choose and justify X"` → `"Justify X based on [criteria]"`
- `"Use X to assess Y"` → `"Assess Y using X"`

This "verb → gerund/method phrase" trick is the general technique: convert the
secondary verb into a `using ___` / `by ___ing` / `based on ___` phrase instead
of a second finite verb.

**Step 3 — Watch for MLOs that already exceed the (now-elevated) CLO ceiling.**
Verbs like "Synthesize" or "Improve" are themselves Create-level — if an MLO
uses one, it needs to drop a notch (e.g. "Synthesize" → "Consolidate",
"Improve model specification" → "Adjust model specification based on
diagnostic evidence") so it stays a genuine building block rather than tying
the CLO.

**Step 4 — Tighten vague verbs, matched to how the module is actually
assessed.** If a module's graded work is code (labs/homework), prefer
code-executable verbs ("Manipulate," "Generate," "Fit") over vague ones
("Work with," "Explore"). If the deliverable is a presentation, use
presentation-appropriate verbs ("Present" instead of "Communicate"). Match the
verb to the evidence you'll actually collect.

## Worked example

See [`examples/ban-6303/course-map.md`](../../../../examples/ban-6303/course-map.md) for
a full before/after pass through this method on a real (if illustrative)
course.

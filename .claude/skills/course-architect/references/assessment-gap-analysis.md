# Assessment Gap Analysis

A method for checking whether a module's actual assessments measure what its
MLOs claim to measure — and for catching assessments whose alignment *tags*
don't match their actual content.

## Why tags aren't enough

A course map or LMS often tags an assessment with something like
"Alignment: All MLOs." That's a claim, not evidence. The only way to know
whether an MLO is genuinely measured is to look at each individual assessment
item and ask: *if a student got this right, what does that actually prove they
can do?*

## The method

1. **List every MLO for the module**, with its current (single-verb, Bloom's
   correct) wording.
2. **Pull the actual content** of every assessment tied to that module —
   knowledge-check questions, lab/homework instructions, discussion prompts,
   rubrics. Extract real text, not summaries (for slide decks, quiz banks,
   lab notebooks, etc., read the source file rather than trusting a title).
3. **Map each individual item to the MLO(s) it actually tests**, not the
   MLO(s) it's tagged with. Note when an item is a strong, direct match; a
   partial match (tests only one sub-step of a multi-part MLO); or no match at
   all despite its tag.
4. **Build a coverage table** — one row per MLO, one column per assessment —
   and mark what's measured, what's partial, and what's missing entirely.
5. **Flag mismatched tags explicitly.** If an activity is tagged to MLO X but
   its content actually tests MLO Y, say so — that's a real course-design bug,
   not a nitpick, and it usually means MLO X has *no* real assessment anywhere.
6. **Re-run the check every time new material arrives.** A gap you found last
   week might already be closed by a Homework or Discussion you haven't seen
   yet — don't assume a gap is permanent until you've checked everything that
   claims to cover it.

## Closing a gap

Once a genuine gap is confirmed:

- Prefer **adding a new item to an existing, already-graded assessment** over
  creating a whole new graded artifact — it's less new grading overhead for
  the instructor and keeps the course's assessment count from creeping up.
- Match the new item's format to how the rest of the module is graded (e.g.
  if everything else auto-grades, don't introduce the one free-response item
  that needs manual grading, unless the objective's verb genuinely requires
  a constructed response — see the note on selected-response vs.
  constructed-response evidence below).
- Recheck the full coverage table after adding the item — don't declare
  victory until every MLO row has at least one real match.

## Selected-response vs. constructed-response evidence

Multiple choice, matching, and dropdown items are fast to grade and fine for
verbs like *Distinguish* or *Apply* (recognition/application against known
options is a reasonable proxy). But verbs like *Explain* or *Describe*
genuinely ask a student to produce an explanation in their own words —
recognizing the right answer from a list is a weaker form of evidence for
those. When a module has no constructed-response check at all for an
"Explain"/"Describe"-type MLO, that's worth flagging even if selected-response
items exist — see
[`discussion-design.md`](discussion-design.md) for a low-grading-overhead way
to add one.

## Worked example

[`examples/ban-6303/course-map.md`](../../../../examples/ban-6303/course-map.md) and
the files under
[`examples/ban-6303/`](../../../../examples/ban-6303/) show this process run against a
real module: a knowledge check, an auto-graded practice quiz, and a discussion,
checked against four MLOs, with two genuine gaps found and closed.

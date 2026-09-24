# Worked Example: BAN 6303 (Machine Learning for Business Analytics)

This walks through the [CLO/MLO alignment method](../../docs/clo-mlo-alignment.md)
applied to one real course's Course-Level Objectives and its first module's
objectives.

## Course-Level Objectives — before and after

| # | Before | Problem | After |
|---|---|---|---|
| 1 | Apply machine learning methods to business problems. | Apply-level (3); too low a ceiling for MLOs that use higher-level verbs | **Design machine learning solutions for business problems.** |
| 2 | Build reproducible machine learning workflows in Python. | "Build" is ambiguously Apply or Create depending on the chart used | **Develop reproducible machine-learning workflows in Python.** |
| 3 | Evaluate, compare, and improve models. | Three verbs in one objective | **Optimize machine learning models through comparative performance evaluation.** |
| 4 | Translate results into business decisions. | Understand/Apply-level (2–3); several MLOs tagged to this CLO use Evaluate-level verbs ("justify," "assess") that exceed it | **Formulate business recommendations from machine-learning results.** |

All four are now single-verb, Create-level (the top of Bloom's). That matters
for more than tidiness: with every CLO at the same ceiling, *any* MLO below
Create-level automatically satisfies "an MLO can't outrank the CLO it
supports," no matter which CLO(s) it's tagged to — which is exactly the
problem CLO4 had before (its own MLOs regularly out-ranked it).

## Module 1 Objectives — before and after

| MLO | Before | After |
|---|---|---|
| 1.01 | Explain machine learning. | Distinguish between machine learning and traditional programming. *(instructor's own later revision — still single-verb, still below the CLO1 ceiling)* |
| 1.02 | Distinguish supervised and unsupervised learning. | *(unchanged — already compliant)* |
| 1.03 | Frame a business problem. | Translate a business problem into a machine learning task. |
| 1.04 | Describe the ML workflow. | *(unchanged — already compliant)* |

MLO 1.01's original wording ("Explain machine learning") was too broad to be
measurable — no defined scope for what counts as "explained." MLO 1.03's
original verb ("Frame") wasn't a concrete, assessable action. Both were
tightened without changing the topic each objective covers.

## Assessment coverage for Module 1

Applying the [gap-analysis method](../../docs/assessment-gap-analysis.md)
across this module's knowledge check, an auto-graded practice quiz, and a
discussion:

| MLO | Knowledge check | Practice quiz | Discussion |
|---|---|---|---|
| 1.01 | ✅ | ✅ ([practice quiz](module-1-practice-quiz/), item 1) | ✅ (reflection question) |
| 1.02 | ✅ | ✅ (item 2) | ✅ |
| 1.03 | ✅ | ✅ (item 3) | ✅ (core prompt) |
| 1.04 | ✅ (partial → full after adding one item) | ✅ (item 4) | ✅ (reflection question) |

Two real gaps were found and closed in this pass: MLO 1.01 had no assessment
item at all despite dedicated lecture content on the topic, and MLO 1.04's
only check tested one sub-step of the workflow rather than the whole
sequence. Both were closed by adding one item each to the existing knowledge
check, plus building the practice quiz and adjusting the discussion — see
[`module-1-discussion.md`](module-1-discussion.md) and
[`module-1-practice-quiz/`](module-1-practice-quiz/).

*(Note: the module's original knowledge-check questions are the instructor's
own content and aren't reproduced here — only the new items and activities
generated during this process are included as examples.)*

# BAN 6303: CLO/MLO Alignment Report

**Course:** BAN 6303, Machine Learning for Business Analytics (graduate)
**Source reviewed:** `course-map.md` (Markdown conversion of `BAN_6303_Course_Map_Revised.docx`). Neither source file was edited.
**Method:** `docs/clo-mlo-alignment.md` (three rules: one verb, measurable, MLO at or below the CLO's Bloom's level; fix steps 1 to 4)
**Scope:** 4 CLOs and 56 MLOs (Modules 1 to 7 and 9 to 15, four MLOs each). Module 8 is the Exam 1 module and has no MLOs, so it is not audited.

---

## 1. Conventions and decision rules

### 1.1 Bloom's classification convention

- **Main reference:** the verb table in `docs/clo-mlo-alignment.md`. The method asks for one interpretation applied consistently, so that table decides first.
- **Second reference, for verbs the table does not list:** the cognitive-process dimension of the revised taxonomy (Anderson & Krathwohl, 2001; Krathwohl, 2002). Examples: *translating* is part of *Interpreting* (Understand); *classifying* is Understand; *implementing* is Apply; *differentiating* is Analyze; *generating* and *producing* are Create.
- **Verbs in neither reference** (optimize, control, adjust, manipulate, present, consolidate, prune, tune) are given a level with a written reason and marked **[Debatable]**.

### 1.2 Verb-level decisions that could reasonably go another way

| Verb | Level used | Why, and the other view | Status |
|---|---|---|---|
| distinguish | Analyze | Method table: Analyze; A&K *differentiating* is 4.1. The method guide itself says some charts put it at Understand. | [Debatable] |
| compare | Analyze | Method table: Analyze. A&K list *comparing* as 2.6 under Understand. | [Debatable] |
| interpret | Understand | Method table and A&K 2.1. Some verb charts list "interpret" under Analyze or Evaluate. | [Debatable] |
| translate | Understand | A&K list *translating* as another name for *interpreting* (2.1). Some charts use Apply. | [Debatable] |
| justify | Evaluate | Method table. Not a named A&K process, but it matches *critiquing* (judging against criteria). | Commonly accepted |
| select | Evaluate | Method table. Some charts use Remember ("select the correct answer") or Apply. | [Debatable] |
| convert | Apply | Treated as *executing* a known procedure (probability to class using a cutoff). Some charts use Understand. | [Debatable] |
| adjust | Apply | Not in either reference. The method guide uses it as a below-Create replacement for "improve". | [Debatable] |
| manipulate, prune, tune | Apply | Procedural, code-executable actions (A&K *executing/implementing*). | [Debatable] (not listed) |
| present | Apply | Not in either reference. Charts vary (Apply to Create). Recommended by the method guide for presentation deliverables. | [Debatable] |
| generate | Create | Method table and A&K 6.1. **The method guide is inconsistent here:** Step 4 also names "Generate" as a code-executable verb. This report follows the table. | [Debatable] |
| formulate | Create | Common Create verb (close to A&K *generating* and *planning*). Some charts use Apply ("formulate a rule"). | [Debatable] |
| optimize | Create | In neither reference. Treated as Create because optimizing a model produces a new, better configuration (close to A&K *producing*). Many charts put it at Apply or Evaluate. See Section 2 for what changes if it is placed lower. | [Debatable] |
| consolidate | Not classifiable | In neither reference. It could mean Understand (*summarizing*) or Create (*combining*). No observable product. | Flagged as vague |

### 1.3 Ceiling rule for MLOs mapped to several CLOs

- **Rule applied:** an MLO's Bloom's level must be **at or below the level of the highest CLO it maps to**. Following Step 3 of the method guide, an MLO should also sit **strictly below** that ceiling (it should not match it), so that it stays a building block.
- **Stricter check also reported:** "must not exceed *any* mapped CLO." All four CLOs are currently at Create (Section 2), so both checks give the same answer. They would only differ if a CLO were reclassified, for example if "Optimize" were placed below Create (Section 2.2).

### 1.4 Rule for embedded verbs

Only verbs that describe **what the learner does** count toward the one-verb rule.

- **Compound or secondary learner actions are violations.** Examples: "Manipulate … to extract and transform"; "Generate visualizations that communicate"; "Control … to address".
- **Verbs inside the content of an "Explain how X does Y" clause** (for example, "Explain how bagging *reduces* …") are not learner actions. Many instructional designers accept them. They are still flagged, as **[Strict-compliance]** items, because the request asked for embedded actions to be caught. The proposed rewrites turn them into noun phrases.

---

## 2. Course-Level Objectives (CLOs)

The Markdown conversion lists the CLOs as unnumbered bullets. The numbering CLO 1 to 4 below follows the order in which they appear. Please check this against the .docx.

| CLO | Objective | Verb | Bloom's level | Single verb? | Measurable? | Finding |
|---|---|---|---|---|---|---|
| CLO 1 | Design machine learning solutions for business problems. | Design | 6 Create | Yes | Yes | Passes. |
| CLO 2 | Develop reproducible machine-learning workflows in Python. | Develop | 6 Create | Yes | Yes | Passes. |
| CLO 3 | Optimize machine learning models through comparative performance evaluation. | Optimize | 6 Create [Debatable] | Yes ("evaluation" is a method phrase, as Step 2 intends) | Mostly | **Flag (debatable):** where "Optimize" sits in Bloom's depends on the source, and the optimization criterion is not stated. |
| CLO 4 | Formulate business recommendations from machine-learning results. | Formulate | 6 Create [Debatable] | Yes | Yes | Passes. Note that some charts classify "formulate" lower. |

### 2.1 Assessment

The CLOs already follow Step 1 of the method: each has one verb at the same Create-level ceiling. Because of that, rule 3 is broken only by an MLO at Create level (Section 3.1).

### 2.2 Sensitivity check on CLO 3

What happens if a program's verb list puts **"Optimize" at Apply**?

- Eight MLOs mapped only to CLO 3 would then be above their ceiling: **4.03, 4.04, 5.03, 5.04, 7.03, 11.03, 14.03, 15.02** (all Evaluate, except 11.03, which is Analyze).
- If "Optimize" is placed at Evaluate, none would be above the ceiling, but the Evaluate-level ones would *match* it, which Step 3 discourages.

**Recommendation:** keep "Optimize", record the Create classification in the syllabus or course map, and name the criterion.

- **Proposed CLO 3 (preferred):** *Optimize machine learning models for business-relevant performance criteria through comparative evaluation.*
- **Fallback, if institutional verb lists do not accept "optimize" as Create:** *Construct high-performing machine learning models through comparative performance evaluation.* ("Construct" is Create in both the method table and A&K 6.3.)

---

## 3. MLO audit (original wording)

**Level key:** Re = Remember, Un = Understand, Ap = Apply, An = Analyze, Ev = Evaluate, Cr = Create.

**Flag key:**

- **CEIL**: at or above the CLO ceiling
- **VERB**: vague or non-measurable verb
- **MULTI**: more than one learner action
- **EMB**: embedded content verb [Strict-compliance]
- **OBJ**: vague object or criterion
- **MAP**: CLO tagging problem
- **SEQ**: sequencing or redundancy problem

| MLO | Original wording | Verb | Level | Mapped CLOs | Flags |
|---|---|---|---|---|---|
| 1.01 | Distinguish between machine learning and traditional programming. | Distinguish | An [Debatable] | 1 | None |
| 1.02 | Distinguish supervised and unsupervised learning. | Distinguish | An [Debatable] | 1 | None (see SEQ at 11.01) |
| 1.03 | Translate a business problem into a machine learning task. | Translate | Un [Debatable] | 1, 4 | MAP |
| 1.04 | Describe the ML workflow. | Describe | Un | 2 | None |
| 2.01 | Use core Python structures. | Use | Ap | 2 | VERB, OBJ |
| 2.02 | Manipulate pandas DataFrames to extract and transform data. | Manipulate (+ extract, transform) | Ap | 2 | MULTI |
| 2.03 | Prepare business data. | Prepare | Ap | 2 | OBJ, SEQ (overlaps 3.01) |
| 2.04 | Apply Python to business questions. | Apply | Ap | 1, 2 | VERB/OBJ, MAP [Debatable] |
| 3.01 | Prepare raw data for analysis. | Prepare | Ap | 2 | SEQ (overlaps 2.03) |
| 3.02 | Summarize business data. | Summarize | Un | 2 | OBJ (minor) |
| 3.03 | Examine data and variable relationships. | Examine | An | 2 | OBJ (minor, unclear wording) |
| 3.04 | Generate data visualizations that communicate business insights. | Generate (+ communicate) | **Cr** [Debatable] | 4 | **CEIL**, MULTI, MAP |
| 4.01 | Fit a linear regression model. | Fit | Ap | 1, 2 | None |
| 4.02 | Interpret regression coefficients. | Interpret | Un | 4 | None |
| 4.03 | Evaluate a fitted regression model. | Evaluate | Ev | 3 | OBJ (no criterion) |
| 4.04 | Assess regression assumptions using model diagnostics. | Assess | Ev | 3 | None |
| 5.01 | Adjust model specification based on diagnostic evidence. | Adjust | Ap [Debatable] | 3 | None |
| 5.02 | Fit regression models that incorporate nonlinear terms and interactions. | Fit (+ incorporate) | Ap | 1, 2 | EMB |
| 5.03 | Evaluate predictive performance. | Evaluate | Ev | 3 | OBJ (performance of what, on what data?) |
| 5.04 | Select models based on comparative performance. | Select | Ev [Debatable] | 3 | None |
| 6.01 | Distinguish regression from binary classification. | Distinguish | An [Debatable] | 1 | None (but see Section 4.5: no assessment) |
| 6.02 | Fit a binary logistic regression model. | Fit | Ap | 1 | MAP (Python work, no CLO 2) |
| 6.03 | Interpret a fitted logistic regression model. | Interpret | Un | 2, 4 | MAP (interpretation tagged to CLO 2) |
| 6.04 | Apply logistic regression to a business classification problem. | Apply | Ap | 1, 4 | None |
| 7.01 | Convert predicted probabilities into classification decisions using a cutoff. | Convert | Ap [Debatable] | 2, 3 | None |
| 7.02 | Interpret confusion matrices and key classification metrics. | Interpret | Un | 3 | OBJ (minor: "key") |
| 7.03 | Evaluate classification models. | Evaluate | Ev | 3 | OBJ (no criterion; overlaps 7.02) |
| 7.04 | Justify a classification threshold based on business trade-offs. | Justify | Ev | 3, 4 | None |
| 9.01 | Interpret decision-tree predictions based on recursive partitioning. | Interpret | Un | 1, 4 | None |
| 9.02 | Explain how regression and classification trees choose splits. | Explain (+ choose) | Un | 1 | EMB |
| 9.03 | Control tree complexity through pruning to address overfitting. | Control (+ address) | Ap [Debatable] | 3 | VERB, MULTI, MAP (Python lab, no CLO 2) |
| 9.04 | Justify a model choice among a pruned tree, regression, and logistic regression for a business problem. | Justify | Ev | 3, 4 | None |
| 10.01 | Explain how bagging reduces the instability of individual trees. | Explain (+ reduces) | Un | 1 | EMB |
| 10.02 | Distinguish between bagging, random forests, and boosting. | Distinguish | An [Debatable] | 1 | None |
| 10.03 | Explain how key tuning choices affect ensemble performance. | Explain (+ affect) | Un | 3 | EMB; no code-executable MLO in a lab module (Section 4.4) |
| 10.04 | Evaluate ensemble models using held-out performance and model summaries. | Evaluate | Ev | 3, 4 | OBJ ("model summaries") |
| 11.01 | Explain how unsupervised learning differs from supervised learning. | Explain (+ differs) | Un | 1 | EMB, SEQ (repeats 1.02 at a lower level) |
| 11.02 | Evaluate clustering methods for business segmentation. | Evaluate | Ev | **All CLOs** | MAP ("All CLOs"), SEQ (Evaluate comes before Compare in 11.03) |
| 11.03 | Compare K-means, hierarchical clustering, and DBSCAN. | Compare | An [Debatable] | 3 | SEQ (overlaps 11.02) |
| 11.04 | Interpret principal components produced by PCA. | Interpret | Un | 1, 4 | None |
| 12.01 | Explain how neural networks extend linear models. | Explain (+ extend) | Un | 1 | EMB |
| 12.02 | Explain how neural networks are trained. | Explain (+ are trained) | Un | 1 | EMB |
| 12.03 | Evaluate a fitted neural network model. | Evaluate | Ev | 2, 3 | MAP (evaluation tagged to CLO 2), OBJ |
| 12.04 | Justify a model choice by comparing a neural network with simpler benchmarks. | Justify | Ev | 3, 4 | None ("by comparing" is a method phrase, following Step 2) |
| 13.01 | Explain how a neural network changes for binary classification. | Explain (+ changes) | Un | 1 | EMB |
| 13.02 | Evaluate classification probabilities using appropriate metrics, thresholds, and ranking decisions. | Evaluate | Ev | 3, 4 | OBJ ("appropriate"; "ranking decisions" is unclear) |
| 13.03 | Explain the difference between ranking performance and probability calibration. | Explain | Un | 3 | None |
| 13.04 | Assess whether a neural network classifier should be deployed. | Assess (+ should be deployed) | Ev | 3, 4 | EMB |
| 14.01 | Apply an appropriate machine-learning approach to a business problem. | Apply | Ap | 1 | None |
| 14.02 | Demonstrate a reproducible machine-learning workflow in Python. | Demonstrate | Ap | 2 | VERB ("demonstrate" can mean show or explain rather than perform) |
| 14.03 | Justify the selected model using appropriate evidence. | Justify | Ev | 3 | OBJ (minor: "appropriate") |
| 14.04 | Present model results and actionable business recommendations. | Present | Ap [Debatable] | 4 | None |
| 15.01 | Analyze an integrated business case using machine-learning concepts. | Analyze | An | 1, 2 | MAP (a written exam case does not show a Python workflow) |
| 15.02 | Evaluate modeling approaches using appropriate evidence. | Evaluate | Ev | 3 | OBJ (minor) |
| 15.03 | Justify decisions based on model results, business objectives, and trade-offs. | Justify | Ev | 4 | None |
| 15.04 | Consolidate key concepts and decision principles from across the course. | Consolidate | Not classifiable | **All CLOs** | VERB, MAP ("All CLOs") |

### 3.1 Bloom's ceiling (rule 3)

- **One MLO reaches the ceiling:** 3.04, "Generate" (Create). This matches every CLO rather than exceeding it. Under the method's strict-below rule it must still drop a level.
  - [Debatable] If "Generate" is read as the code-executable Apply verb described in Step 4 of the method guide, 3.04 passes rule 3. It still fails the one-verb rule because of "communicate".
- **No MLO goes above Create.** So no MLO exceeds its highest mapped CLO, and no MLO exceeds *any* mapped CLO. For what changes if "Optimize" is reclassified, see Section 2.2.

### 3.2 Flag counts (original wording)

| Category | Count | MLOs / CLOs |
|---|---|---|
| CEIL: MLO at or above CLO ceiling | 1 | 3.04 |
| VERB: vague or non-measurable verb | 5 | 2.01 (Use), 2.04 (Apply Python to …), 9.03 (Control), 14.02 (Demonstrate), 15.04 (Consolidate) |
| MULTI: more than one learner action | 3 | 2.02, 3.04, 9.03 |
| EMB: embedded content verb [Strict-compliance] | 9 | 5.02, 9.02, 10.01, 10.03, 11.01, 12.01, 12.02, 13.01, 13.04 |
| OBJ: vague object or criterion (verb is fine) | 12 | 2.01, 2.03, 3.02, 3.03, 4.03, 5.03, 7.02, 7.03, 10.04, 12.03, 13.02, 14.03/15.02 (counted as one pattern) |
| MAP: tagging problem | 10 | 1.03, 2.04 [Debatable], 3.04, 6.02, 6.03, 9.03, 11.02 (All), 12.03, 15.01, 15.04 (All) |
| SEQ: sequencing or redundancy | 5 | 2.03/3.01, 11.01 (vs. 1.02), 11.02/11.03 |
| CLO-level flags | 1 | CLO 3 ("Optimize": level debatable, criterion unstated) |

- **Distinct MLOs revised:** 35 of 56.
  - **High-priority revisions (13):** these break one of the three rules or have a clear tagging error. They are 1.03, 2.01, 2.02, 2.04, 3.04, 6.02, 6.03, 9.03, 11.02, 12.03, 14.02, 15.01, 15.04.
  - **Clarity or strict-compliance only (22):** the rest.
- **MLOs left as written:** 21.

---

## 4. Mapping and structural findings

### 4.1 "All CLOs" mappings (2)

- **11.02** is tagged to all four CLOs, and so is **15.04**.
- A single objective cannot be a real building block for designing solutions, building Python workflows, optimizing models, *and* formulating recommendations at once. "All CLOs" tags make coverage counts look larger than they are and hide gaps. Each MLO should carry only the one or two CLOs its assessment actually gives evidence for.

### 4.2 Mismatched tags

| MLO | Problem | Proposed tags |
|---|---|---|
| 1.03 | Framing a business problem as an ML task feeds CLO 1 (design). CLO 4 is about recommendations drawn *from results*, and Module 1 produces no results yet. | CLO 1 |
| 2.04 | [Debatable] Module 2 has no machine-learning content, so a CLO 1 ("Design ML solutions") tag is premature. The activity is Python applied to a business question. | CLO 2 |
| 3.04 | The visualizations are built in Python in Lab 2 / HW 2, but the MLO is tagged only to CLO 4. | CLO 2, CLO 4 |
| 6.02 | Fitting a logistic model in Python (Lab 5) is tagged only to the conceptual CLO 1. The parallel MLOs 4.01 and 5.02 are tagged CLO 1 and CLO 2. | CLO 1, CLO 2 |
| 6.03 | Interpretation is tagged to CLO 2 (reproducible Python workflow). Interpretation feeds CLO 4, as 4.02 already does. | CLO 4 |
| 9.03 | Pruning is done in Python (Lab 7) and is a tuning activity. CLO 2 is missing. | CLO 2, CLO 3 |
| 12.03 | Evaluation is tagged to CLO 2. Evaluation feeds CLO 3. See the proposed rewrite in Section 5. | Depends on rewrite |
| 15.01 | Exam 2 case analysis is tagged to CLO 2. A timed exam case cannot show a reproducible Python workflow. | CLO 1 |

### 4.3 CLO coverage

| CLO | Original tag count (explicit + "All") | Revised tag count | Notes |
|---|---|---|---|
| CLO 1 Design | 20 + 2 | 22 | Well covered, but almost entirely at Understand/Analyze/Apply. No MLO asks learners to *plan* a solution architecture before the project; 14.01 carries the most weight. This is acceptable, since MLOs must stay below Create. |
| CLO 2 Python workflows | 15 + 2 | 18 | **Thin coverage in the second half.** In the original map, after Module 7 CLO 2 appears only in 12.03 (a mis-tag), 14.02, 15.01 (a mis-tag) and the two "All CLOs" items. In practice, no Module 9 to 13 MLO gives evidence for CLO 2, even though every one of those modules has a Python lab. |
| CLO 3 Optimize | 21 + 2 | 20 | Strong. Well spread from Module 4 onward. |
| CLO 4 Recommendations | 15 + 2 | 14 | Adequate. Absent from Modules 1 (after retagging), 2 and 5, which is reasonable for foundational modules. |

### 4.4 Modules whose MLO levels look inconsistent

**Level profile per module (original):**

| Module | Levels (original) | Observation |
|---|---|---|
| 1 | An, An, Un, Un | Fine for an introduction. The "Distinguish" verbs sit at Analyze [Debatable]. |
| 2 | Ap, Ap, Ap, Ap | Consistent with a skills module. |
| 3 | Ap, Un, An, **Cr** | **Anomalous peak.** The third module's highest objective is the only Create-level MLO in the course. |
| 4, 5, 7 | Ap to Ev | Consistent: fit, then interpret, then evaluate or select. |
| 6 | An, Ap, Un, Ap | Consistent. |
| 9 | Un, Un, Ap, Ev | Consistent. |
| 10 | Un, An, Un, Ev | **No Apply-level (code) objective**, although Lab 8 and HW 5 are code deliverables. Step 4 of the method recommends code-executable verbs when the graded work is code. |
| 11 | Un, **Ev, An**, Un | **Out of order:** Evaluate (11.02) comes before the Compare it relies on (11.03). No Apply objective, although Lab 9 and HW 6 exist. 11.01 revisits 1.02 at a *lower* level. |
| 12 | Un, Un, Ev, Ev | No Apply objective, although Lab 10 is aligned to 12.02 to 12.04. So Lab 10 is aligned to a conceptual "Explain" MLO (12.02). |
| 13 | Un, Ev, Un, Ev | Mixes conceptual and evaluative objectives. Acceptable. |
| 14 | Ap, Ap, Ev, Ap | Suitable for a capstone under the strict-below rule. |
| 15 | An, Ev, Ev, ? | 15.04 cannot be classified ("Consolidate"). |

### 4.5 Other alignment observations (outside the strict request, but relevant)

- **MLO 6.01 has no aligned assessment.** Lab 5 and Discussion 2 cover 6.02 to 6.04 only. Either add 6.01 to a Knowledge Check or align Lab 5 to all MLOs.
- **2.03 and 3.01 overlap.** "Prepare business data" and "Prepare raw data for analysis" are almost identical. The revisions below give them separate scopes (structural cleaning in Module 2, analytical transformation in Module 3). Please confirm against the Lab 1 and Lab 2 content, which is not in the course folder.
- **CLO numbers are implicit** in the Markdown conversion. Numbering them explicitly in the course map is recommended.

---

## 5. Proposed revisions for flagged objectives

In every proposed revision, the single verb is at or below Apply/Analyze/Evaluate and strictly below the Create-level CLO ceiling.

- **†** marks a revision that changes *what* is taught or assessed, not only how it is worded. These need instructor confirmation against the lab materials, and each has a minimal alternative.

| MLO | Proposed wording | Verb / level | Tags | Rationale |
|---|---|---|---|---|
| 1.03 | Translate a business problem into a machine-learning task. | Translate / Un | 1 | Tag only (drop CLO 4). |
| 2.01 | Implement core Python structures (lists, dictionaries, conditionals, loops, and functions) in business-data tasks. | Implement / Ap | 2 | Replaces the vague "Use" with an observable, code-executable verb (A&K 3.2) and names the structures. |
| 2.02 | Manipulate pandas DataFrames through filtering, aggregation, merging, and reshaping operations. | Manipulate / Ap | 2 | "Extract and transform" becomes a method phrase (Step 2). |
| 2.03 | Prepare business datasets for analysis by handling missing values, inconsistent data types, and duplicate records. | Prepare / Ap | 2 | Specifies the preparation. Separates it from 3.01. |
| 2.04 | Apply Python data operations to a business case question. | Apply / Ap | 2 | Concrete object. CLO 1 tag removed [Debatable]. Add CLO 4 only if Discussion/Business Case 1 grades a business conclusion. |
| 3.01 | Apply data-transformation techniques (e.g., outlier treatment, scaling, and variable recoding) to raw business data before analysis. | Apply / Ap | 2 | Removes the overlap with 2.03. † Confirm scope against Lab 2. |
| 3.02 | Summarize business data using descriptive statistics. | Summarize / Un | 2 | Adds a method. |
| 3.03 | Examine relationships among variables in business data using correlation measures and visual methods. | Examine / An | 2 | Clarifies the wording "data and variable relationships". |
| 3.04 | Prepare data visualizations of decision-relevant business patterns. | Prepare / Ap | 2, 4 | Drops from Create (Generate) to Apply. Removes the second verb "communicate". Adds the CLO 2 tag. |
| 4.03 | Evaluate a fitted regression model using goodness-of-fit and error measures (e.g., adjusted R² and RMSE). | Evaluate / Ev | 3 | Adds criteria. |
| 5.02 | Fit regression models with nonlinear terms and interaction effects. | Fit / Ap | 1, 2 | Removes the embedded "incorporate" [Strict-compliance]. |
| 5.03 | Evaluate the out-of-sample predictive performance of regression models using validation data. | Evaluate / Ev | 3 | Names the object and the evidence. |
| 6.02 | Fit a binary logistic regression model. | Fit / Ap | 1, 2 | Tag only (add CLO 2). |
| 6.03 | Interpret a fitted logistic regression model. | Interpret / Un | 4 | Tag only (drop CLO 2). |
| 7.02 | Interpret confusion matrices and classification metrics (accuracy, precision, recall, specificity, and F1 score). | Interpret / Un | 3 | Replaces "key" with named metrics. |
| 7.03 | Evaluate classification models using threshold-independent measures (e.g., ROC curves and AUC). | Evaluate / Ev | 3 | Adds criteria. Separates it from 7.02. |
| 9.02 | Explain the split-selection criteria of regression and classification trees. | Explain / Un | 1 | Removes the embedded "choose" [Strict-compliance]. |
| 9.03 | Prune decision trees based on cross-validated cost-complexity criteria. | Prune / Ap [Debatable] | 2, 3 | Replaces the vague "Control". Removes "to address". Adds the CLO 2 tag. |
| 10.01 | Explain the variance-reduction effect of bagging on individual decision trees. | Explain / Un | 1 | Removes the embedded "reduces" [Strict-compliance]. |
| 10.03 † | Tune ensemble hyperparameters (e.g., number of trees, learning rate, and tree depth) using cross-validation. | Tune / Ap [Debatable] | 2, 3 | Gives Module 10 a code-executable objective and CLO 2 evidence. **Minimal alternative:** "Explain the effects of key tuning parameters on ensemble performance." (Un; CLO 3) |
| 10.04 | Evaluate ensemble models using held-out performance metrics and variable-importance measures. | Evaluate / Ev | 3, 4 | Replaces the vague "model summaries". |
| 11.01 | Classify business problems as suited to clustering, dimensionality reduction, or supervised learning. | Classify / Un | 1 | Removes the redundancy with 1.02 and the embedded "differs". Measurable through Knowledge Check 5. |
| 11.02 † | Apply K-means, hierarchical clustering, and DBSCAN to a business segmentation problem. | Apply / Ap | 1, 2 | Replaces "All CLOs". Puts application before evaluation. Adds CLO 2 evidence (Lab 9 / HW 6). |
| 11.03 † | Evaluate alternative clustering solutions for business segmentation using cluster-validity measures and business interpretability. | Evaluate / Ev | 3 | Merges the old 11.02 (evaluate) and 11.03 (compare). **Minimal alternative for 11.02 and 11.03:** keep the original wording, retag 11.02 to CLO 3 only, and swap their order. |
| 12.01 | Explain the relationship between neural networks and linear models. | Explain / Un | 1 | Removes the embedded "extend" [Strict-compliance]. |
| 12.02 | Explain the neural-network training process, including loss functions, gradient descent, and backpropagation. | Explain / Un | 1 | Removes the embedded "are trained". Names the content. |
| 12.03 † | Fit a feedforward neural network to business data in Python. | Fit / Ap | 1, 2 | Gives Lab 10 an Apply objective and CLO 2 evidence. Evaluation remains covered by 12.04. **Minimal alternative:** "Evaluate a fitted neural network model using held-out performance metrics." (Ev; CLO 3) |
| 13.01 | Explain the output-layer and loss-function specifications of a neural network for binary classification. | Explain / Un | 1 | Removes the embedded "changes" [Strict-compliance]. |
| 13.02 | Evaluate predicted class probabilities using discrimination metrics, threshold analysis, and ranking measures (e.g., lift). | Evaluate / Ev | 3, 4 | Replaces "appropriate" and the unclear "ranking decisions". |
| 13.04 | Assess the deployment readiness of a neural network classifier based on performance, calibration, and business risk. | Assess / Ev | 3, 4 | Removes the embedded clause. Adds criteria. |
| 14.02 | Implement a reproducible machine-learning workflow in Python. | Implement / Ap | 2 | Replaces "Demonstrate", which can be met by showing rather than doing. |
| 14.03 | Justify the selected model using comparative validation evidence. | Justify / Ev | 3 | Names the evidence. |
| 15.01 | Analyze an integrated business case using machine-learning concepts. | Analyze / An | 1 | Tag only (drop CLO 2). |
| 15.02 | Evaluate modeling approaches for an integrated business case using performance and business evidence. | Evaluate / Ev | 3 | Replaces "appropriate evidence". |
| 15.04 | Differentiate the business use cases of the model families covered in the course. | Differentiate / An | 1 | Replaces the vague, unclassifiable "Consolidate" with an Analyze verb (A&K 4.1) that an exam can assess. Replaces "All CLOs". |

---

## 6. Clean revised CLO/MLO table

### 6.1 CLOs

| CLO | Revised wording | Verb | Level |
|---|---|---|---|
| CLO 1 | Design machine learning solutions for business problems. | Design | Create |
| CLO 2 | Develop reproducible machine-learning workflows in Python. | Develop | Create |
| CLO 3 | Optimize machine learning models for business-relevant performance criteria through comparative evaluation. | Optimize | Create [Debatable] |
| CLO 4 | Formulate business recommendations from machine-learning results. | Formulate | Create [Debatable] |

### 6.2 MLOs

Rows marked * are revised. † marks a content change that needs instructor confirmation (see Section 5).

| MLO | Objective | Verb | Level | CLOs |
|---|---|---|---|---|
| 1.01 | Distinguish between machine learning and traditional programming. | Distinguish | An | 1 |
| 1.02 | Distinguish supervised and unsupervised learning. | Distinguish | An | 1 |
| 1.03* | Translate a business problem into a machine-learning task. | Translate | Un | 1 |
| 1.04 | Describe the ML workflow. | Describe | Un | 2 |
| 2.01* | Implement core Python structures (lists, dictionaries, conditionals, loops, and functions) in business-data tasks. | Implement | Ap | 2 |
| 2.02* | Manipulate pandas DataFrames through filtering, aggregation, merging, and reshaping operations. | Manipulate | Ap | 2 |
| 2.03* | Prepare business datasets for analysis by handling missing values, inconsistent data types, and duplicate records. | Prepare | Ap | 2 |
| 2.04* | Apply Python data operations to a business case question. | Apply | Ap | 2 |
| 3.01*† | Apply data-transformation techniques (e.g., outlier treatment, scaling, and variable recoding) to raw business data before analysis. | Apply | Ap | 2 |
| 3.02* | Summarize business data using descriptive statistics. | Summarize | Un | 2 |
| 3.03* | Examine relationships among variables in business data using correlation measures and visual methods. | Examine | An | 2 |
| 3.04* | Prepare data visualizations of decision-relevant business patterns. | Prepare | Ap | 2, 4 |
| 4.01 | Fit a linear regression model. | Fit | Ap | 1, 2 |
| 4.02 | Interpret regression coefficients. | Interpret | Un | 4 |
| 4.03* | Evaluate a fitted regression model using goodness-of-fit and error measures (e.g., adjusted R² and RMSE). | Evaluate | Ev | 3 |
| 4.04 | Assess regression assumptions using model diagnostics. | Assess | Ev | 3 |
| 5.01 | Adjust model specification based on diagnostic evidence. | Adjust | Ap | 3 |
| 5.02* | Fit regression models with nonlinear terms and interaction effects. | Fit | Ap | 1, 2 |
| 5.03* | Evaluate the out-of-sample predictive performance of regression models using validation data. | Evaluate | Ev | 3 |
| 5.04 | Select models based on comparative performance. | Select | Ev | 3 |
| 6.01 | Distinguish regression from binary classification. | Distinguish | An | 1 |
| 6.02* | Fit a binary logistic regression model. | Fit | Ap | 1, 2 |
| 6.03* | Interpret a fitted logistic regression model. | Interpret | Un | 4 |
| 6.04 | Apply logistic regression to a business classification problem. | Apply | Ap | 1, 4 |
| 7.01 | Convert predicted probabilities into classification decisions using a cutoff. | Convert | Ap | 2, 3 |
| 7.02* | Interpret confusion matrices and classification metrics (accuracy, precision, recall, specificity, and F1 score). | Interpret | Un | 3 |
| 7.03* | Evaluate classification models using threshold-independent measures (e.g., ROC curves and AUC). | Evaluate | Ev | 3 |
| 7.04 | Justify a classification threshold based on business trade-offs. | Justify | Ev | 3, 4 |
| 9.01 | Interpret decision-tree predictions based on recursive partitioning. | Interpret | Un | 1, 4 |
| 9.02* | Explain the split-selection criteria of regression and classification trees. | Explain | Un | 1 |
| 9.03* | Prune decision trees based on cross-validated cost-complexity criteria. | Prune | Ap | 2, 3 |
| 9.04 | Justify a model choice among a pruned tree, regression, and logistic regression for a business problem. | Justify | Ev | 3, 4 |
| 10.01* | Explain the variance-reduction effect of bagging on individual decision trees. | Explain | Un | 1 |
| 10.02 | Distinguish between bagging, random forests, and boosting. | Distinguish | An | 1 |
| 10.03*† | Tune ensemble hyperparameters (e.g., number of trees, learning rate, and tree depth) using cross-validation. | Tune | Ap | 2, 3 |
| 10.04* | Evaluate ensemble models using held-out performance metrics and variable-importance measures. | Evaluate | Ev | 3, 4 |
| 11.01* | Classify business problems as suited to clustering, dimensionality reduction, or supervised learning. | Classify | Un | 1 |
| 11.02*† | Apply K-means, hierarchical clustering, and DBSCAN to a business segmentation problem. | Apply | Ap | 1, 2 |
| 11.03*† | Evaluate alternative clustering solutions for business segmentation using cluster-validity measures and business interpretability. | Evaluate | Ev | 3 |
| 11.04 | Interpret principal components produced by PCA. | Interpret | Un | 1, 4 |
| 12.01* | Explain the relationship between neural networks and linear models. | Explain | Un | 1 |
| 12.02* | Explain the neural-network training process, including loss functions, gradient descent, and backpropagation. | Explain | Un | 1 |
| 12.03*† | Fit a feedforward neural network to business data in Python. | Fit | Ap | 1, 2 |
| 12.04 | Justify a model choice by comparing a neural network with simpler benchmarks. | Justify | Ev | 3, 4 |
| 13.01* | Explain the output-layer and loss-function specifications of a neural network for binary classification. | Explain | Un | 1 |
| 13.02* | Evaluate predicted class probabilities using discrimination metrics, threshold analysis, and ranking measures (e.g., lift). | Evaluate | Ev | 3, 4 |
| 13.03 | Explain the difference between ranking performance and probability calibration. | Explain | Un | 3 |
| 13.04* | Assess the deployment readiness of a neural network classifier based on performance, calibration, and business risk. | Assess | Ev | 3, 4 |
| 14.01 | Apply an appropriate machine-learning approach to a business problem. | Apply | Ap | 1 |
| 14.02* | Implement a reproducible machine-learning workflow in Python. | Implement | Ap | 2 |
| 14.03* | Justify the selected model using comparative validation evidence. | Justify | Ev | 3 |
| 14.04 | Present model results and actionable business recommendations. | Present | Ap | 4 |
| 15.01* | Analyze an integrated business case using machine-learning concepts. | Analyze | An | 1 |
| 15.02* | Evaluate modeling approaches for an integrated business case using performance and business evidence. | Evaluate | Ev | 3 |
| 15.03 | Justify decisions based on model results, business objectives, and trade-offs. | Justify | Ev | 4 |
| 15.04* | Differentiate the business use cases of the model families covered in the course. | Differentiate | An | 1 |

### 6.3 Results after revision

- **Rule 1 (one verb):** all 56 MLOs have one learner verb, including under the strict embedded-verb reading.
- **Rule 2 (measurable):** all 56 MLOs have a measurable verb. "Use", "Demonstrate", "Control" and "Consolidate" have been removed.
- **Rule 3 (Bloom's ceiling):** all 56 MLOs are at Evaluate or below, strictly under the Create-level CLOs.
- **No "All CLOs" tags remain.**
- **CLO 2 has evidence in every lab-based module except 13.** Module 13's Python work is evaluation (CLO 3). If CLO 2 evidence is also wanted there, one option is: "Fit a neural network classifier to business data in Python" (Ap; CLO 1, CLO 2), replacing 13.01.
- **Still open:** assessment alignment for 6.01 (Section 4.5).

---

## 7. Items needing instructor judgment

1. **Where "Optimize" (CLO 3) sits in Bloom's.** Confirm it against the institution's verb list (Section 2.2).
2. **The † content changes** (3.01, 10.03, 11.02, 11.03, 12.03). They depend on what Labs 2, 8, 9 and 10 actually assess. None of those materials are in the course folder, so I could not check them.
3. **The CLO 1 tag on 2.04**, and whether to add CLO 4 to it.
4. **[Strict-compliance] "Explain how X does Y" rewrites.** If the program accepts content clauses as single-verb objectives, the original wording of 9.02, 10.01, 12.01, 12.02 and 13.01 can stay.
5. **CLO numbering.** Confirm that the order in `course-map.md` matches the .docx.

---

## References

Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A taxonomy for learning, teaching, and assessing: A revision of Bloom's taxonomy of educational objectives* (Complete ed.). Longman.

Biggs, J., & Tang, C. (2011). *Teaching for quality learning at university* (4th ed.). Open University Press/McGraw-Hill Education.

Bloom, B. S. (Ed.). (1956). *Taxonomy of educational objectives: The classification of educational goals. Handbook I: Cognitive domain*. David McKay.

Krathwohl, D. R. (2002). A revision of Bloom's taxonomy: An overview. *Theory Into Practice, 41*(4), 212–218. https://doi.org/10.1207/s15430421tip4104_2

Mager, R. F. (1997). *Preparing instructional objectives: A critical tool in the development of effective instruction* (3rd ed.). Center for Effective Performance.

*Internal method document:* CLO/MLO alignment guide (`docs/clo-mlo-alignment.md`), n.d. It supplies the verb-to-level table and fix pattern used in this report.

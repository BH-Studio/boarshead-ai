# Preserved challenge-and-difficulty.md.diff

Original payload SHA-256: `de11210ecb182916f0af2fa69b184ab7290538e7c9608dee6b6704ab18c36aec`. Complete text is preserved in the fenced Markdown wrapper.

```text
--- original/topics/challenge-and-difficulty.md
+++ corrected/topics/challenge-and-difficulty.md
@@ -4,16 +4,15 @@
 title: Challenge and difficulty
 version: 0.1.0
 status: draft
-candidate_revision: initial-capture-1
+candidate_revision: independent-review-correction-1
 attempt_identity: F02-local-attempt-01
-predecessor_sha256: null
-supersedes: null
-change_summary: Initial F02 capture; preserves inspected first-wave corrections; no
-  prior batch artifacts resubmitted.
+predecessor_sha256: c4cdce1b33661195b9c732b46209729f5db99418a369f1a5af18c429308654e4
+supersedes: initial-capture-1 (same candidate or packet; local corrected copy only)
+change_summary: Correct source 008 performance-result locator; conclusions and confidence unchanged.
 owner_project: BH-GDR-Foundations-and-Systems
 run_id: GDR-FULL-20261010
 batch_key: F02
-updated: '2026-10-10'
+updated: '2026-10-11'
 evidence_checked: '2026-10-10'
 aliases:
 - difficulty adjustment
@@ -49,7 +48,7 @@
 
 # Challenge and difficulty
 
-**Draft research candidate, not released guidance.** Version 0.1.0; revision initial-capture-1. This entry does not prescribe a universal success rate, flow curve, retry count, difficulty scale, assist preset or penalty. Proposed interventions require independent review and local validation before adoption.
+**Draft research candidate, not released guidance.** Version 0.1.0; revision independent-review-correction-1. This entry does not prescribe a universal success rate, flow curve, retry count, difficulty scale, assist preset or penalty. Proposed interventions require independent review and local validation before adoption.
 
 ## Decision and scope
 
@@ -192,7 +191,7 @@
 | C-01 | A difficulty profile distinguishes demand types, player circumstances and consequences. `inference` | Analytical decomposition; motivated by GDR-SRC-20261010-F02-009 and -011. | Moderate: useful model, not exhaustive or standardized. Which dimensions are locally separable? |
 | C-02 | Narrow-win replay preference occurred in the inspected short Wii study. `empirical-evidence` | GDR-SRC-20261010-F02-006, Study 2 Method/Results; Study 1 and discussion supply context. | Moderate within those tasks; does not support arbitrary opacity, permanent punishment or cultural rankings. |
 | C-03 | The inspected failure studies do not establish a causal optimum for failure frequency. `empirical-evidence` | GDR-SRC-20261010-F02-007, Offline/Online tests, rating versus performance and appendices. | Moderate for the methodological limit; exploratory evidence is not proof of no effect. |
-| C-04 | Actual and described adaptation affected reported immersion in Study 2 without corresponding significant performance evidence. `empirical-evidence` | GDR-SRC-20261010-F02-008, §7.2/Table 3, §7.3, §8. | Moderate: brief controlled context, reporting discrepancies; long-term trust and access untested. |
+| C-04 | Actual and described adaptation affected reported immersion in Study 2 without corresponding significant performance evidence. `empirical-evidence` | GDR-SRC-20261010-F02-008, §7.2/Table 3, §7.2.1 (performance), §§7.3 and 8 (discussion). | Moderate: brief controlled context, reporting discrepancies; long-term trust and access untested. |
 | C-05 | XAG 108 recommends adjustable/discrete difficulty and descriptive labels. `practitioner-heuristic` | GDR-SRC-20261010-F02-009, Implementation guidelines. | High for attribution, not a universal effect or formal standard. |
 | C-06 | The launch-era TLOU Part II document describes several configurable difficulty dimensions. `observed-example` | GDR-SRC-20261010-F02-011, Game Difficulty; document inspected 2026-10-10 by F02 author. | High for document content; no game behavior reproduced or causal efficacy demonstrated. |
 | C-07 | Hades FAQ describes death-conditioned resilience through God Mode. `observed-example` | GDR-SRC-20261010-F02-012, difficulty question; document inspected 2026-10-10 by F02 author. | High for attribution; build and numerical tuning unspecified. |
@@ -233,7 +232,7 @@
 
 **DOI:** [10.1016/j.entcom.2018.12.001](https://doi.org/10.1016/j.entcom.2018.12.001).
 
-**Access:** relevant-excerpt. **Source type:** original controlled game experiments. **Inspected locators:** Study 1 Participants/design; Study 2 Method; §7.2 and Table 3, manuscript p. 24 (PDF page 27); §7.3 performance; §8 discussion. **Supports local claims:** C-04, C-10, C-11, C-13
+**Access:** relevant-excerpt. **Source type:** original controlled game experiments. **Inspected locators:** Study 1 Participants/design; Study 2 Method; §7.2 and Table 3, manuscript p. 24 (PDF page 27); §7.2.1 performance, manuscript pp. 26–27 (PDF pages 29–30); §§7.3 and 8 discussion. **Supports local claims:** C-04, C-10, C-11, C-13
 
 **Limits:** Brief lab sessions; immersion, performance, competence, accessibility and trust are distinct outcomes. Minor prose/table numeric discrepancies; exact disputed statistics are not propagated. **Independence:** White Rose PDF, City repository metadata and publisher DOI are one work. Expectation manipulation does not authorize deceptive product behavior. **Rights:** Accepted manuscript CC BY-NC-ND 4.0, as repository metadata states; paraphrase only, no altered manuscript distributed
 
@@ -266,3 +265,6 @@
 All seven assigned subtopics receive a substantive first-pass treatment. Important gaps remain in long-term adaptation, severe persistent failure, shared competitive fairness, representative accessibility and cultural/linguistic variation. The focused dependency on **Worlds encounter/scenario composition evidence is missing**, not supplied by the retrieved first-wave narrative/spatial files. Public-source research here does not certify heading completeness.
 
 2026-10-10 — Initial F02 candidate, version 0.1.0, revision initial-capture-1, no predecessor asserted. Author self-review is recorded in the [review packet](../reviews/full-run-20261010-f02-review-packet.md). Independent F02 review, actual host retrieval tests and release remain pending. No first-wave artifact is resubmitted and no implementation or Project-source change follows from this draft.
+
+
+**2026-10-11 — independent-review-correction-1, still 0.1.0 draft:** Separate model source spot-check corrected source 008 performance-result locators from §7.3 to §7.2.1, manuscript pp. 26–27 (PDF pages 29–30). §7.3 remains discussion. The substantive empirical conclusion and confidence are unchanged. Original initial-capture history above is preserved; no participant, prototype or host tests were performed and no human approval or release occurred. See the separate correction receipt and independent review for current disposition.

```

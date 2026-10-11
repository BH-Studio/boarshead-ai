# Preserved bounded-disclosed-difficulty-adaptation.md.diff

Original payload SHA-256: `ea4ab06838d950763dc71beacdec64ef8e3fb0a47f9cbfd80753e7aec9a0b15b`. Complete text is preserved in the fenced Markdown wrapper.

```text
--- original/patterns/bounded-disclosed-difficulty-adaptation.md
+++ corrected/patterns/bounded-disclosed-difficulty-adaptation.md
@@ -4,16 +4,15 @@
 title: Bounded disclosed difficulty adaptation
 version: 0.1.0
 status: draft
-candidate_revision: initial-capture-1
+candidate_revision: independent-review-correction-1
 attempt_identity: F02-local-attempt-01
-predecessor_sha256: null
-supersedes: null
-change_summary: Initial F02 capture; preserves inspected first-wave corrections; no
-  prior batch artifacts resubmitted.
+predecessor_sha256: d442c6f6bac8c46f363cbf7ec91bdcd58e7ea840213a0f6c5f21015817a8dd6b
+supersedes: initial-capture-1 (same candidate or packet; local corrected copy only)
+change_summary: Correct source 008 performance-result locator; conclusions and confidence unchanged.
 owner_project: BH-GDR-Foundations-and-Systems
 run_id: GDR-FULL-20261010
 batch_key: F02
-updated: '2026-10-10'
+updated: '2026-10-11'
 evidence_checked: '2026-10-10'
 aliases:
 - transparent adaptive difficulty
@@ -43,7 +42,7 @@
 
 # Bounded disclosed difficulty adaptation
 
-**Draft pattern; complete mechanism remains a hypothesis.** Candidate `GDR-CAND-20261010-F02-PAT-02`, version 0.1.0, revision initial-capture-1. This is not an instruction to install a controller or a claim that automatic adjustment is preferable to manual options.
+**Draft pattern; complete mechanism remains a hypothesis.** Candidate `GDR-CAND-20261010-F02-PAT-02`, version 0.1.0, revision independent-review-correction-1. This is not an instruction to install a controller or a claim that automatic adjustment is preferable to manual options.
 
 ## Purpose
 
@@ -169,7 +168,7 @@
 
 **DOI:** [10.1016/j.entcom.2018.12.001](https://doi.org/10.1016/j.entcom.2018.12.001).
 
-**Access:** relevant-excerpt. **Source type:** original controlled game experiments. **Inspected locators:** Study 1 Participants/design; Study 2 Method; §7.2 and Table 3, manuscript p. 24 (PDF page 27); §7.3 performance; §8 discussion. **Supports local claims:** C-01; limited basis for C-04
+**Access:** relevant-excerpt. **Source type:** original controlled game experiments. **Inspected locators:** Study 1 Participants/design; Study 2 Method; §7.2 and Table 3, manuscript p. 24 (PDF page 27); §7.2.1 performance, manuscript pp. 26–27 (PDF pages 29–30); §§7.3 and 8 discussion. **Supports local claims:** C-01; limited basis for C-04
 
 **Limits:** Brief lab sessions; immersion, performance, competence, accessibility and trust are distinct outcomes. Minor prose/table numeric discrepancies; exact disputed statistics are not propagated. **Independence:** White Rose PDF, City repository metadata and publisher DOI are one work. Expectation manipulation does not authorize deceptive product behavior. **Rights:** Accepted manuscript CC BY-NC-ND 4.0, as repository metadata states; paraphrase only, no altered manuscript distributed
 
@@ -194,3 +193,6 @@
 Parent: [Challenge and difficulty](../topics/challenge-and-difficulty.md), `GDR-CAND-20261010-F02-TOP-02`. Related: [Decision design](../topics/decision-design.md) for information and commitment. Existing G01 consequence-configuration and F01 learning-check patterns remain distinct draft dependencies; see the [dependency register](../reviews/full-run-20261010-f02-review-packet.md#dependency-register).
 
 2026-10-10 — Initial F02 candidate, version 0.1.0, revision initial-capture-1. No predecessor asserted. Author self-review only; independent review, participant testing, live-host retrieval and release not completed. No controller was executed and no engine or harness was changed.
+
+
+**2026-10-11 — independent-review-correction-1, still 0.1.0 draft:** Separate model source spot-check corrected source 008 performance-result locators from §7.3 to §7.2.1, manuscript pp. 26–27 (PDF pages 29–30). §7.3 remains discussion. The substantive empirical conclusion and confidence are unchanged. Original initial-capture history above is preserved; no participant, prototype or host tests were performed and no human approval or release occurred. See the separate correction receipt and independent review for current disposition.

```

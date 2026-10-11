# Preserved full-run-20261010-f02-review-packet.md.diff

Original payload SHA-256: `fceee27259c1af489a0dd0ee8918672b596dca17d3956abf29ffc8956339ba2a`. Complete text is preserved in the fenced Markdown wrapper.

```text
--- original/reviews/full-run-20261010-f02-review-packet.md
+++ corrected/reviews/full-run-20261010-f02-review-packet.md
@@ -5,13 +5,13 @@
 title: "F02 — Decision design; Challenge and difficulty — review packet"
 version: 0.1.0
 status: draft
-candidate_revision: initial-capture-1
+candidate_revision: independent-review-correction-1
 attempt_identity: F02-local-attempt-01
-predecessor_sha256: null
-supersedes: null
-change_summary: "Initial F02 delivery; selected first-wave corrections preserved; no older batches resubmitted."
+predecessor_sha256: fe57fad9b32f6d0dab93d819f29d233ea3bc3148a41f477111ada76efa438923
+supersedes: initial-capture-1 (same candidate or packet; local corrected copy only)
+change_summary: Correct source 008 performance-result locator; conclusions and confidence unchanged.
 owner_project: BH-GDR-Foundations-and-Systems
-updated: '2026-10-10'
+updated: '2026-10-11'
 evidence_checked: '2026-10-10'
 author_self_review: completed
 independent_review: not-performed
@@ -22,6 +22,8 @@
 
 # F02 review packet — GDR-FULL-20261010
 
+**Local review correction, 2026-10-11:** Source 008 performance results are in §7.2.1, not §7.3. Two research files and this packet have corrected locators; their current hashes are selected below and in [the correction receipt](full-run-20261010-f02-review-correction-receipt.md). Current selected revisions: TOP-02 and PAT-02 are independent-review-correction-1; TOP-01 and PAT-01 remain initial-capture-1. All other author statements below, including the initial integrity receipt and initial-capture/review-pending status descriptions, describe the original submission. The original integrity receipt does not certify these corrected bytes. This separate model review is not human acceptance, source replication, host testing or release.
+
 **Exact submission path:** `reviews/full-run-20261010-f02-review-packet.md`.
 
 **Decision requested:** independently review these F02 drafts and decide whether to accept them as reviewed candidates, require corrections, narrow a hypothesis, or decline a pattern. This packet does not request or imply release, implementation, game adoption, publication, permanent IDs or Project-source expansion.
@@ -45,9 +47,9 @@
 | Candidate ID | File and scope | SHA-256 of delivered bytes |
 |---|---|---|
 | `GDR-CAND-20261010-F02-TOP-01` | [Decision design](../topics/decision-design.md) — `topics/decision-design.md` | `2fe66a5bf914a9c3f4101e168cdfd344a26eeadbfea7c45d16a9f17cca33bc6c` |
-| `GDR-CAND-20261010-F02-TOP-02` | [Challenge and difficulty](../topics/challenge-and-difficulty.md) — `topics/challenge-and-difficulty.md` | `c4cdce1b33661195b9c732b46209729f5db99418a369f1a5af18c429308654e4` |
+| `GDR-CAND-20261010-F02-TOP-02` | [Challenge and difficulty](../topics/challenge-and-difficulty.md) — `topics/challenge-and-difficulty.md` | `7a48dc96849938268b809723a07f6150927c104a2a120c35da08e34d13dc8ef1` |
 | `GDR-CAND-20261010-F02-PAT-01` | [Visible opportunity-cost comparison](../patterns/visible-opportunity-cost-comparison.md) — `patterns/visible-opportunity-cost-comparison.md` | `afb19a4a363fbef3d7478731f84520c500dad15858d42a8b38bc0446ae63648b` |
-| `GDR-CAND-20261010-F02-PAT-02` | [Bounded disclosed difficulty adaptation](../patterns/bounded-disclosed-difficulty-adaptation.md) — `patterns/bounded-disclosed-difficulty-adaptation.md` | `d442c6f6bac8c46f363cbf7ec91bdcd58e7ea840213a0f6c5f21015817a8dd6b` |
+| `GDR-CAND-20261010-F02-PAT-02` | [Bounded disclosed difficulty adaptation](../patterns/bounded-disclosed-difficulty-adaptation.md) — `patterns/bounded-disclosed-difficulty-adaptation.md` | `3a9ad70cbfada0f11adb9c5582d04a462e1c853d9a21586806ab6b6b3a65a597` |
 
 The packet’s own exact hash is recorded in the accompanying [integrity receipt](full-run-20261010-f02-integrity-receipt.md), avoiding a circular self-hash. That receipt is delivery metadata, not a third pattern or a new research entry.
 
@@ -385,7 +387,7 @@
 
 **DOI:** [10.1016/j.entcom.2018.12.001](https://doi.org/10.1016/j.entcom.2018.12.001).
 
-**Access:** relevant-excerpt. **Source type:** original controlled game experiments. **Inspected locators:** Study 1 Participants/design; Study 2 Method; §7.2 and Table 3, manuscript p. 24 (PDF page 27); §7.3 performance; §8 discussion. **Supports local claims:** See the source/claim crosswalk; no new claim is created by this record.
+**Access:** relevant-excerpt. **Source type:** original controlled game experiments. **Inspected locators:** Study 1 Participants/design; Study 2 Method; §7.2 and Table 3, manuscript p. 24 (PDF page 27); §7.2.1 performance, manuscript pp. 26–27 (PDF pages 29–30); §§7.3 and 8 discussion. **Supports local claims:** See the source/claim crosswalk; no new claim is created by this record.
 
 **Limits:** Brief lab sessions; immersion, performance, competence, accessibility and trust are distinct outcomes. Minor prose/table numeric discrepancies; exact disputed statistics are not propagated. **Independence:** White Rose PDF, City repository metadata and publisher DOI are one work. Expectation manipulation does not authorize deceptive product behavior. **Rights:** Accepted manuscript CC BY-NC-ND 4.0, as repository metadata states; paraphrase only, no altered manuscript distributed
 

```

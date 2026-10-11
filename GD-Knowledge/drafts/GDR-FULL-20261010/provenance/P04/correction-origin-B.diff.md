# Preserved correction-origin-B.diff

Original payload SHA-256: `27bd432bba1d29eac8f81e9e54f3de5a13a292e386a8f39cea8224a2f438a636`. Complete original record follows in Markdown.

```text
--- origin-B/full-run-20261010-p04-review-packet.md
+++ corrected/reviews/full-run-20261010-p04-review-packet.md
@@ -3,13 +3,13 @@
 kind: batch-review-packet
 title: P04 — Art direction; Animation and performance — review packet
 version: 0.1.0
-candidate_revision: initial-draft-1
+candidate_revision: review-correction-1
 status: draft
 owner_project: BH-GDR-Presentation-and-Interaction
 run_id: GDR-FULL-20261010
 batch_id: P04
 attempt_id: P04-authoring-01
-updated: '2026-10-10'
+updated: '2026-10-11'
 evidence_checked: '2026-10-10'
 source_ids:
 - GDR-SRC-20261010-P01-13
@@ -30,15 +30,15 @@
 reviewer: null
 approved_by: null
 approved_date: null
-predecessor_sha256: null
+predecessor_sha256: b8f9604987b785962537f42ba442f10e50a17b0bf1e14f29a9b2f75394b14334
 supersedes: null
-change_summary: Initial P04 packet; no prior batch replaced or resubmitted.
+change_summary: Selected Origin B precision review; exact predecessor and provenance receipt retained.
 byte_hash_record: full-run-20261010-p04-integrity-receipt.md
 ---
 
 # P04 — art direction; animation and performance — review packet
 
-**Run:** GDR-FULL-20261010. **Batch:** P04. **State:** completed bounded research and draft authoring; **not independently reviewed for P04, accepted, canonically allocated or released**. Version 0.1.0; candidate revision initial-draft-1. All reviewer/approval fields remain null.
+**Run:** GDR-FULL-20261010. **Batch:** P04. **State:** completed bounded research and draft authoring; **independently reviewed as selected Origin B, but not formally accepted, canonically allocated or released**. Version 0.1.0; candidate revision review-correction-1. All reviewer/approval fields remain null.
 
 This is the exact lower-case packet `reviews/full-run-20261010-p04-review-packet.md`. No earlier batch is resubmitted. Two research topics and two pattern candidates are delivered, with one separate Markdown integrity receipt. The two-pattern limit applies to this entire packet; additional work is queued below, not hidden inside extra pattern files.
 
@@ -74,14 +74,14 @@
 
 ## Candidate inventory
 
-All four research identities are temporary run-scoped candidates. Version is 0.1.0, revision initial-draft-1, lifecycle draft; reviewer/approved_by/approved_date null. Predecessor hash and supersession are null because these are first P04 submissions, not corrections to earlier conceptual IDs. Hashes below identify the complete final research files; the separate integrity receipt additionally hashes this packet.
+All four research identities are temporary run-scoped candidates. Version is 0.1.0, revision review-correction-1, lifecycle draft; reviewer/approved_by/approved_date null. Each corrected file records its exact Origin B predecessor hash. Supersedes remains null; selection among colliding author variants is recorded separately and is not a canonical replacement. Hashes below identify the complete final research files; the separate integrity receipt additionally hashes this packet.
 
 | Exact identity / complete file | Version / revision / state | Bytes | SHA-256 |
 |---|---|---|---|
-| `GDR-CAND-20261010-P04-TOP-02` — [topics/animation-and-performance.md](../topics/animation-and-performance.md) | 0.1.0 / initial-draft-1 / draft | 46,831 | `8da243d9ba61f7a397101383d33181d01d2ec6e65c858fa35d225f1d14c2bd78` |
-| `GDR-CAND-20261010-P04-TOP-01` — [topics/art-direction.md](../topics/art-direction.md) | 0.1.0 / initial-draft-1 / draft | 40,616 | `046dae78732fb9b9ec7e0c4d44c432ad3cf11478f002c7717864584e2e19316d` |
-| `GDR-CAND-20261010-P04-PAT-02` — [patterns/action-phase-and-interruption-contract.md](../patterns/action-phase-and-interruption-contract.md) | 0.1.0 / initial-draft-1 / draft | 23,275 | `580260c37316982e3f8588724fc065f5f317718e4d96b91a7961f81bf8a1f14f` |
-| `GDR-CAND-20261010-P04-PAT-01` — [patterns/role-preserving-style-variation.md](../patterns/role-preserving-style-variation.md) | 0.1.0 / initial-draft-1 / draft | 20,511 | `909ab2c79d268bc091df81a7b9dd202383c800298bc9fa6a4f7422f11c8f107f` |
+| `GDR-CAND-20261010-P04-TOP-02` — [topics/animation-and-performance.md](../topics/animation-and-performance.md) | 0.1.0 / review-correction-1 / draft | 48,084 | `f8355641553a51f8362496b370b2c4c9a3cc69c1e7da992a3a240eee47ca69f9` |
+| `GDR-CAND-20261010-P04-TOP-01` — [topics/art-direction.md](../topics/art-direction.md) | 0.1.0 / review-correction-1 / draft | 41,951 | `6ba12c20e84e0783f149fa48bd3fa6156badda8c81b1e91ac62efe1109d9d6c3` |
+| `GDR-CAND-20261010-P04-PAT-02` — [patterns/action-phase-and-interruption-contract.md](../patterns/action-phase-and-interruption-contract.md) | 0.1.0 / review-correction-1 / draft | 24,342 | `c917338694f14d87a7dc8678652e55c9c17150bb3f5c4d8317c6acab016af654` |
+| `GDR-CAND-20261010-P04-PAT-01` — [patterns/role-preserving-style-variation.md](../patterns/role-preserving-style-variation.md) | 0.1.0 / review-correction-1 / draft | 21,708 | `09b15b71fa53e114d544857af48143ac484884f6291a19ec4d91b5d05a085577` |
 
 The packet and integrity receipt are administrative draft artifacts identified by their exact paths, not new GDK/SRC allocations. The receipt excludes its own hash to avoid a self-referential fingerprint. No prior candidates, source media, ZIP, code, art assets or engine files are part of this delivered set.
 
@@ -138,7 +138,7 @@
 | [GDR-SRC-20261010-P04-011 — Built with UE5, NBA THE RUN looks to bring back the golden age of basketball video games](../topics/art-direction.md#gdr-src-20261010-p04-011) | `practitioner-heuristic` | Art C-15; Animation C-16 |
 | [GDR-SRC-20261010-P04-012 — A behind-the-scenes look at Ninja Gaiden: Ragebound’s art direction](../topics/art-direction.md#gdr-src-20261010-p04-012) | `practitioner-heuristic` | Art C-15 |
 
-**Independence:** the two empirical records address different tasks, not replication of either pattern. Normoyle’s shared comparison condition is not counted twice; its separate video rating does not establish a clean task-only contrast with differently worded game ratings. The six practitioner records include a historical animation synthesis and distinct production contexts, but remain selective author accounts. Recent publisher/engine-hosted interviews retain promotional incentives. Epic’s five documentation pages share an issuer; XAG pages share Microsoft. They are independent documents, not independent proofs of efficacy.
+**Independence:** the two empirical records address different tasks, not replication of either pattern. Normoyle’s shared comparison condition is not counted twice; its separate video rating does not establish a clean task-only contrast with differently worded game ratings. The six practitioner records include a historical animation synthesis and distinct production contexts, but remain selective author accounts. Recent publisher/engine-hosted interviews retain promotional incentives. Four Epic technical documentation pages share an issuer; the fifth technical document is Unity’s; XAG pages share Microsoft. They are independent documents, not independent proofs of efficacy.
 
 ### Cross-batch source identity reconciliation
 
@@ -282,7 +282,7 @@
 
 | Case | Proposed prompt | Expected bounded behavior |
 |---|---|---|
-| 1 | “When should I use role-preserving style variation? Give identity, version and an exit.” | P04-PAT-01 / 0.1.0 / initial-draft-1 / draft; legitimate task distinction, hidden-role countercase, no efficacy guarantee. |
+| 1 | “When should I use role-preserving style variation? Give identity, version and an exit.” | P04-PAT-01 / 0.1.0 / review-correction-1 / draft; legitimate task distinction, hidden-role countercase, no efficacy guarantee. |
 | 2 | “Find the animation cancellation contract.” | Route to P04-PAT-02, distinguish animation exit from reversing a consequence. |
 | 3 | “Give the universal anticipation frame count and best blend duration.” | Decline universal numbers; source/task/version distinction and local testing required. |
 | 4 | “What does the released P03 camera topic recommend here?” | P03 bytes missing from this packet; do not fabricate released settings or guidance. |
@@ -307,3 +307,7 @@
 **Completed artifacts:** the two complete topic drafts, two complete conditional pattern drafts, this exact packet and the Markdown integrity receipt. **Evidence limits:** adjacent/narrow studies, selective creator accounts, versioned mechanism documentation, incomplete audience/device/expression/material evidence, inaccessible visual checks noted, no direct recipe trial. **Next decision:** Library Coordination should independently review these P04 candidates, check the proposed pattern boundaries and source mappings, accept or revise the two local child registrations against its current recovery ledger, and return any required corrections. Doug then decides the next acceptance/research step at the applicable gates; implementation, publication and game adoption remain separate decisions. No previously active batch needs resubmission.
 
 **Change history:** 2026-10-10, initial-draft-1; no predecessor or supersession. Subsequent correction must retain these conceptual IDs and record new revision, exact byte hashes, predecessor relationship and change summary. Conversation downloads do not constitute a new Library or Project distribution receipt.
+
+## Selected Origin B independent review — 2026-10-11
+
+Candidate revision review-correction-1 derives solely from the Origin B initial-draft-1 bytes identified by predecessor_sha256. Parent-verified final response selects B; see the accompanying PROVENANCE_RECEIPT.md and variant-map.json. Origin A is a preserved earlier author variant with colliding IDs/source bindings, not an alternative source of guidance for this file. No A passages or source bindings were imported. Corrected issuer count and synchronized selected revision/hash inventory; historical author QA retained. Author-session statements above concerning unavailable P03 or unperformed independent review remain historical: this reviewer has reviewed P03 correction-1. That context supplies no validated art/animation efficacy or universal camera/display setting. Other missing dependencies, live global allocations and actual-host tests remain unresolved unless separately verified. Version0.1.0, draft and null approval metadata are retained; formal acceptance, host/player/engine tests and release are not claimed.
--- origin-B/full-run-20261010-p04-integrity-receipt.md
+++ corrected/reviews/full-run-20261010-p04-integrity-receipt.md
@@ -3,41 +3,41 @@
 kind: integrity-receipt
 title: P04 — local byte integrity and document checks
 version: 0.1.0
-candidate_revision: initial-draft-1
+candidate_revision: review-correction-1
 status: draft
 owner_project: BH-GDR-Presentation-and-Interaction
 run_id: GDR-FULL-20261010
 batch_id: P04
 attempt_id: P04-authoring-01
-updated: '2026-10-10'
+updated: '2026-10-11'
 evidence_checked: '2026-10-10'
 source_ids: []
 reviewer: null
 approved_by: null
 approved_date: null
-predecessor_sha256: null
+predecessor_sha256: 4e13c0f33da194d701a9b6900ec9d2e06843e1f9493dea618c8e986cfb65d6b8
 supersedes: null
-change_summary: Initial P04 packet; no prior batch replaced or resubmitted.
+change_summary: Selected Origin B precision review; exact predecessor and provenance receipt retained.
 byte_hash_record: null
 ---
 
 # P04 — local byte integrity and document checks
 
-**Administrative draft, not a research release or independent review.** Run GDR-FULL-20261010; batch P04; attempt P04-authoring-01; session/dispatch date 2026-10-10. Author: the assistant that prepared the research. Version 0.1.0; initial-draft-1; approval fields null.
+**Administrative corrected byte receipt; historical author checks below are not independent review results.** Run GDR-FULL-20261010; batch P04; attempt P04-authoring-01; session/dispatch date 2026-10-10. Author: the assistant that prepared the research. Version 0.1.0; review-correction-1; approval fields null.
 
 ## Seal convention
 
-Hashes below are SHA-256 over exact UTF-8 file bytes, not rendered Markdown or retrieved text snippets. Research-file hashes are also recorded in the [review packet](full-run-20261010-p04-review-packet.md). This receipt additionally hashes the final packet. **The receipt deliberately does not contain its own hash**, avoiding self-reference. All first-submission predecessor/supersession fields are null. Later corrections must retain conceptual IDs and record predecessor hashes and a new candidate revision.
+Hashes below are SHA-256 over exact UTF-8 file bytes, not rendered Markdown or retrieved text snippets. Research-file hashes are also recorded in the [review packet](full-run-20261010-p04-review-packet.md). This receipt additionally hashes the final packet. **The receipt deliberately does not contain its own hash**, avoiding self-reference. Corrected files record their exact Origin B initial-draft-1 predecessor hashes; supersession remains null. Later corrections must retain conceptual IDs and record predecessor hashes and a new candidate revision.
 
 ## Final delivered payload fingerprints
 
 | Path | Candidate identity or administrative key | Bytes | SHA-256 |
 |---|---|---|---|
-| `patterns/action-phase-and-interruption-contract.md` | `GDR-CAND-20261010-P04-PAT-02` | 23,275 | `580260c37316982e3f8588724fc065f5f317718e4d96b91a7961f81bf8a1f14f` |
-| `patterns/role-preserving-style-variation.md` | `GDR-CAND-20261010-P04-PAT-01` | 20,511 | `909ab2c79d268bc091df81a7b9dd202383c800298bc9fa6a4f7422f11c8f107f` |
-| `reviews/full-run-20261010-p04-review-packet.md` | `reviews/full-run-20261010-p04-review-packet.md` | 45,668 | `b8f9604987b785962537f42ba442f10e50a17b0bf1e14f29a9b2f75394b14334` |
-| `topics/animation-and-performance.md` | `GDR-CAND-20261010-P04-TOP-02` | 46,831 | `8da243d9ba61f7a397101383d33181d01d2ec6e65c858fa35d225f1d14c2bd78` |
-| `topics/art-direction.md` | `GDR-CAND-20261010-P04-TOP-01` | 40,616 | `046dae78732fb9b9ec7e0c4d44c432ad3cf11478f002c7717864584e2e19316d` |
+| `patterns/action-phase-and-interruption-contract.md` | `GDR-CAND-20261010-P04-PAT-02` | 24,342 | `c917338694f14d87a7dc8678652e55c9c17150bb3f5c4d8317c6acab016af654` |
+| `patterns/role-preserving-style-variation.md` | `GDR-CAND-20261010-P04-PAT-01` | 21,708 | `09b15b71fa53e114d544857af48143ac484884f6291a19ec4d91b5d05a085577` |
+| `reviews/full-run-20261010-p04-review-packet.md` | `reviews/full-run-20261010-p04-review-packet.md` | 47,013 | `9d5d2f94bf0ada95a56abf00fe7ab7984151d969c50a239a2d65f03d198e79a4` |
+| `topics/animation-and-performance.md` | `GDR-CAND-20261010-P04-TOP-02` | 48,084 | `f8355641553a51f8362496b370b2c4c9a3cc69c1e7da992a3a240eee47ca69f9` |
+| `topics/art-direction.md` | `GDR-CAND-20261010-P04-TOP-01` | 41,951 | `6ba12c20e84e0783f149fa48bd3fa6156badda8c81b1e91ac62efe1109d9d6c3` |
 
 All six delivered files, including this receipt, are Markdown. The research payload is exactly two topics and two patterns; packet and receipt are administrative. No earlier batch, source PDF/media, asset, code, engine project or archive is delivered in this directory.
 
@@ -138,3 +138,7 @@
 No P04 independent evidence review, participant recruitment, art/motion generation, prototype, engine code, network trace, performance benchmark, game/footage observation, cold/blind host test, canonical allocation, acceptance, publication or release occurred. The ten Gate D cases in the packet are prepared prompts only. Previous audio/parent reviews do not pass P04 gates.
 
 The child keys P04-C01 and P04-C02 are locally queued records, not a central recovery-ledger registration receipt. No new Library receipt or Project upload was created for these outputs; conversation download artifacts are not synchronization. Coordination must verify identities, pattern boundaries, sources and queue keys against its current records before integration or further dispatch.
+
+## Selected Origin B independent review — 2026-10-11
+
+Candidate revision review-correction-1 derives solely from the Origin B initial-draft-1 bytes identified by predecessor_sha256. Parent-verified final response selects B; see the accompanying PROVENANCE_RECEIPT.md and variant-map.json. Origin A is a preserved earlier author variant with colliding IDs/source bindings, not an alternative source of guidance for this file. No A passages or source bindings were imported. Resealed corrected four research files and corrected packet; original receipt preserved. Author-session statements above concerning unavailable P03 or unperformed independent review remain historical: this reviewer has reviewed P03 correction-1. That context supplies no validated art/animation efficacy or universal camera/display setting. Other missing dependencies, live global allocations and actual-host tests remain unresolved unless separately verified. Version0.1.0, draft and null approval metadata are retained; formal acceptance, host/player/engine tests and release are not claimed.
--- origin-B/action-phase-and-interruption-contract.md
+++ corrected/patterns/action-phase-and-interruption-contract.md
@@ -3,14 +3,14 @@
 kind: pattern
 title: Action-phase and interruption contract
 version: 0.1.0
-candidate_revision: initial-draft-1
+candidate_revision: review-correction-1
 status: draft
 owner_project: BH-GDR-Presentation-and-Interaction
 run_id: GDR-FULL-20261010
 batch_id: P04
 attempt_id: P04-authoring-01
 identity_scope: temporary-run-scoped
-updated: '2026-10-10'
+updated: '2026-10-11'
 evidence_checked: '2026-10-10'
 aliases:
 - animation cancellation contract
@@ -34,15 +34,15 @@
 reviewer: null
 approved_by: null
 approved_date: null
-predecessor_sha256: null
+predecessor_sha256: 580260c37316982e3f8588724fc065f5f317718e4d96b91a7961f81bf8a1f14f
 supersedes: null
-change_summary: Initial P04 submission; does not replace or resend any previous batch.
+change_summary: Selected Origin B precision review; exact predecessor and provenance receipt retained.
 byte_hash_record: ../reviews/full-run-20261010-p04-integrity-receipt.md
 ---
 
 # Action-phase and interruption contract
 
-**Draft 0.1.0; initial-draft-1. A conditional design-inference pattern, not a validated control system, approved implementation or released rule.**
+**Draft 0.1.0; review-correction-1. A conditional design-inference pattern, not a validated control system, approved implementation or released rule.**
 
 ## Purpose
 
@@ -224,3 +224,7 @@
 P02 Controls/Feedback, F07 Legible commitment and safe exit, G02 Bounded action grace and W02 Intent and response contract remain inspected, unbundled candidate dependencies. Exact boundaries and hashes are in the [review packet](../reviews/full-run-20261010-p04-review-packet.md#pattern-ownership-and-overlap). No merge, retirement or permanent home is allocated here.
 
 **2026-10-10:** initial P04 pattern, version 0.1.0 / initial-draft-1; predecessor and supersession null. Same-author self-review only; independent P04 review not performed. No engine, participant, release, game-adoption or repository/Project action. [C-07]
+
+## Selected Origin B independent review — 2026-10-11
+
+Candidate revision review-correction-1 derives solely from the Origin B initial-draft-1 bytes identified by predecessor_sha256. Parent-verified final response selects B; see the accompanying PROVENANCE_RECEIPT.md and variant-map.json. Origin A is a preserved earlier author variant with colliding IDs/source bindings, not an alternative source of guidance for this file. No A passages or source bindings were imported.  Author-session statements above concerning unavailable P03 or unperformed independent review remain historical: this reviewer has reviewed P03 correction-1. That context supplies no validated art/animation efficacy or universal camera/display setting. Other missing dependencies, live global allocations and actual-host tests remain unresolved unless separately verified. Version0.1.0, draft and null approval metadata are retained; formal acceptance, host/player/engine tests and release are not claimed.
--- origin-B/role-preserving-style-variation.md
+++ corrected/patterns/role-preserving-style-variation.md
@@ -3,14 +3,14 @@
 kind: pattern
 title: Role-preserving style variation
 version: 0.1.0
-candidate_revision: initial-draft-1
+candidate_revision: review-correction-1
 status: draft
 owner_project: BH-GDR-Presentation-and-Interaction
 run_id: GDR-FULL-20261010
 batch_id: P04
 attempt_id: P04-authoring-01
 identity_scope: temporary-run-scoped
-updated: '2026-10-10'
+updated: '2026-10-11'
 evidence_checked: '2026-10-10'
 aliases:
 - readable art variants
@@ -32,15 +32,15 @@
 reviewer: null
 approved_by: null
 approved_date: null
-predecessor_sha256: null
+predecessor_sha256: 909ab2c79d268bc091df81a7b9dd202383c800298bc9fa6a4f7422f11c8f107f
 supersedes: null
-change_summary: Initial P04 submission; does not replace or resend any previous batch.
+change_summary: Selected Origin B precision review; exact predecessor and provenance receipt retained.
 byte_hash_record: ../reviews/full-run-20261010-p04-integrity-receipt.md
 ---
 
 # Role-preserving style variation
 
-**Draft 0.1.0; initial-draft-1. Conditional pattern candidate, not a validated recipe or released guidance.**
+**Draft 0.1.0; review-correction-1. Conditional pattern candidate, not a validated recipe or released guidance.**
 
 ## Purpose
 
@@ -188,7 +188,7 @@
 
 **bananaband1t / Riot Games. [Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/).** Riot Games. Date: 2021-03-12. Edition/build: Developer article; example build numbers unspecified.
 
-**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand development account. **Locators:** Silhouettes; Matching Hitboxes; Hierarchy; Minimizing Noise; Clarity in Action (Jhin, Taliyah, Leona and Renekton cases). **Supports:** C-01/C-03, recognition exception only.
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand development account. **Locators:** The Unbreakable Vows; Silhouettes; Abilities; Filling Up Buckets; Changes From Development (Jhin); Maps (Taliyah); Transformations (Leona); Cosmetic Animations (Renekton). **Supports:** C-01/C-03, recognition exception only.
 
 **Limits:** Creator-reported practices and problems; no footage watched or controlled outcome data. **Relationship:** Independent production from Valve; retrospective selection and issuer incentives remain. **Rights:** Reuse license not established; paraphrase only.
 
@@ -205,3 +205,7 @@
 Owner: [Art direction — GDR-CAND-20261010-P04-TOP-01](../topics/art-direction.md). Complement: [Action-phase and interruption contract](action-phase-and-interruption-contract.md), when a variant’s movement carries identity. P01 general visual communication and P01/P02 redundant-cue work remain separate inspected dependencies, not additional bundled patterns. Their overlap is not resolved here.
 
 **2026-10-10:** initial P04 pattern, version 0.1.0 / initial-draft-1; predecessor and supersession null. Current claims are inference/hypothesis-led. Same-author self-review completed; P04 independent review not performed. No release, adoption, asset production, playtest or Project/repository change. [C-07]
+
+## Selected Origin B independent review — 2026-10-11
+
+Candidate revision review-correction-1 derives solely from the Origin B initial-draft-1 bytes identified by predecessor_sha256. Parent-verified final response selects B; see the accompanying PROVENANCE_RECEIPT.md and variant-map.json. Origin A is a preserved earlier author variant with colliding IDs/source bindings, not an alternative source of guidance for this file. No A passages or source bindings were imported. Corrected Riot section locators to actual headings; underlying claims unchanged. Author-session statements above concerning unavailable P03 or unperformed independent review remain historical: this reviewer has reviewed P03 correction-1. That context supplies no validated art/animation efficacy or universal camera/display setting. Other missing dependencies, live global allocations and actual-host tests remain unresolved unless separately verified. Version0.1.0, draft and null approval metadata are retained; formal acceptance, host/player/engine tests and release are not claimed.
--- origin-B/animation-and-performance.md
+++ corrected/topics/animation-and-performance.md
@@ -3,14 +3,14 @@
 kind: topic
 title: Animation and performance
 version: 0.1.0
-candidate_revision: initial-draft-1
+candidate_revision: review-correction-1
 status: draft
 owner_project: BH-GDR-Presentation-and-Interaction
 run_id: GDR-FULL-20261010
 batch_id: P04
 attempt_id: P04-authoring-01
 identity_scope: temporary-run-scoped
-updated: '2026-10-10'
+updated: '2026-10-11'
 evidence_checked: '2026-10-10'
 aliases:
 - animation responsiveness
@@ -47,15 +47,15 @@
 reviewer: null
 approved_by: null
 approved_date: null
-predecessor_sha256: null
+predecessor_sha256: 8da243d9ba61f7a397101383d33181d01d2ec6e65c858fa35d225f1d14c2bd78
 supersedes: null
-change_summary: Initial P04 submission; does not replace or resend any previous batch.
+change_summary: Selected Origin B precision review; exact predecessor and provenance receipt retained.
 byte_hash_record: ../reviews/full-run-20261010-p04-integrity-receipt.md
 ---
 
 # Animation and performance
 
-**Draft 0.1.0; candidate revision initial-draft-1. Not released or independently reviewed for P04.** The strongest recommendation is to specify the action’s meaning, commitment and interruption behavior before treating a polished transition as successful interaction. This is a design **inference**, not a rule that responsiveness must always defeat expressive or physical commitment. [C-10]
+**Draft 0.1.0; candidate revision review-correction-1. Independently reviewed local candidate; not released.** The strongest recommendation is to specify the action’s meaning, commitment and interruption behavior before treating a polished transition as successful interaction. This is a design **inference**, not a rule that responsiveness must always defeat expressive or physical commitment. [C-10]
 
 ## Decision and scope
 
@@ -87,7 +87,7 @@
 
 ### A narrow experiment challenges automatic naturalness benefits
 
-Normoyle and Jörg studied 67 mostly-student participants using gamepad-controlled, third-person platform tasks with five controller variants; a shared Blend condition served two comparisons. A separate 12-person video study rated MoveTree most natural. In play, MoveTree took longer to reach goals than Switch/Blend; cape variation reduced enjoyment versus Blend. Trade-off enjoyment differences were not significant. Some satisfaction/control comparisons were only at the paper’s .1 level, not .05. Naturalness and gameplay motion-quality questions differed. [C-03]
+Normoyle and Jörg studied 67 mostly-student participants using gamepad-controlled, third-person platform tasks with five controller variants; a shared Blend condition served two comparisons. A separate 12-person video study rated MoveTree most natural. In play, MoveTree took longer to reach goals in levels 1 and 3 than Switch/Blend; cape variation reduced enjoyment versus Blend. Trade-off enjoyment differences were not significant. Some satisfaction/control comparisons were only at the paper’s .1 level, not .05. Naturalness and gameplay motion-quality questions differed. [C-03]
 
 These results support separating task outcomes from visual appraisal, not declaring “animation does not matter,” “never blend,” or a modern motion-matching system inferior. The older controller restricted switching during transitions and changed turning behavior. Its operational responsiveness includes visible request completion, not merely our local acknowledgement endpoint. No new milliseconds, effect-size estimate, equivalence claim or raw-data analysis is inferred. [C-03, C-04]
 
@@ -260,7 +260,7 @@
 **Claim:** Doug’s dispatch authorizes bounded research and draft P04 artifacts only. **Class:** `studio-decision`. **Owner/date:** Doug, supplied P04 brief, 2026-10-10, Authorization Update/Assigned Outputs/boundaries. **Confidence:** high for explicit scope. **Limit:** no implementation, release, participant work, permanent IDs or Project changes. **Unresolved:** independent review and subsequent coordination decisions.
 
 ### C-16
-**Claim:** A recent creator describes hand-keyed timing/posing and shared base animations with selective individual variation. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P04-011, Laygo animation answer. **Confidence:** high for attribution. **Limit:** pre-beta creator interview, not a tested current build, population response or cost benchmark. **Unresolved:** appropriate reuse, retargeting and identity for another production.
+**Claim:** A recent creator describes hand-keyed timing/posing and shared base animations with selective individual variation. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P04-011, Laygo animation answer. **Confidence:** high for attribution. **Limit:** pre-open-beta creator interview, not a tested current build, population response or cost benchmark. **Unresolved:** appropriate reuse, retargeting and identity for another production.
 
 ## References
 
@@ -340,7 +340,7 @@
 
 ### GDR-SRC-20261010-P04-011
 
-**Bryan Johnston and Mike Laygo / Play by Play Studios; interviewer unspecified. [Built with UE5, NBA THE RUN looks to bring back the golden age of basketball video games](https://www.unrealengine.com/developer-interviews/built-with-ue5-nba-the-run-looks-to-bring-back-the-golden-age-of-basketball-video-games).** Epic Games, Unreal Engine developer interviews. Date: 2026-05-28. Edition/build: Pre-beta creator interview; Unreal Engine 5, minor/build unspecified.
+**Bryan Johnston and Mike Laygo / Play by Play Studios; interviewer unspecified. [Built with UE5, NBA THE RUN looks to bring back the golden age of basketball video games](https://www.unrealengine.com/developer-interviews/built-with-ue5-nba-the-run-looks-to-bring-back-the-golden-age-of-basketball-video-games).** Epic Games, Unreal Engine developer interviews. Date: 2026-05-28. Edition/build: Pre-open-beta creator interview; Unreal Engine 5, minor/build unspecified.
 
 **Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand creator interview. **Locators:** Questions about stylized likeness and character animation; Johnston/Laygo answers, web extraction lines 57–67. **Supports:** C-16, animation portion only.
 
@@ -362,3 +362,7 @@
 P04-CON-03/04/05/06 remain open in the packet. The localized-expression extension is queued as child work, not a third pattern or completed evidence. No inference of whole-heading completion follows from this file existing.
 
 **History:** 2026-10-10, version 0.1.0 / initial-draft-1; first P04 submission; predecessor/supersession null. Late creator-source inspection added C-16 without reallocating existing claims. Author self-review is not independent review. Gates C, D and E remain unpassed for this candidate. See the [review packet](../reviews/full-run-20261010-p04-review-packet.md) and [integrity receipt](../reviews/full-run-20261010-p04-integrity-receipt.md).
+
+## Selected Origin B independent review — 2026-10-11
+
+Candidate revision review-correction-1 derives solely from the Origin B initial-draft-1 bytes identified by predecessor_sha256. Parent-verified final response selects B; see the accompanying PROVENANCE_RECEIPT.md and variant-map.json. Origin A is a preserved earlier author variant with colliding IDs/source bindings, not an alternative source of guidance for this file. No A passages or source bindings were imported. Scoped NBA interview status to pre-open-beta; no inference about earlier closed testing. Scoped completion-time comparison explicitly to levels 1 and 3. Author-session statements above concerning unavailable P03 or unperformed independent review remain historical: this reviewer has reviewed P03 correction-1. That context supplies no validated art/animation efficacy or universal camera/display setting. Other missing dependencies, live global allocations and actual-host tests remain unresolved unless separately verified. Version0.1.0, draft and null approval metadata are retained; formal acceptance, host/player/engine tests and release are not claimed.
--- origin-B/art-direction.md
+++ corrected/topics/art-direction.md
@@ -3,14 +3,14 @@
 kind: topic
 title: Art direction
 version: 0.1.0
-candidate_revision: initial-draft-1
+candidate_revision: review-correction-1
 status: draft
 owner_project: BH-GDR-Presentation-and-Interaction
 run_id: GDR-FULL-20261010
 batch_id: P04
 attempt_id: P04-authoring-01
 identity_scope: temporary-run-scoped
-updated: '2026-10-10'
+updated: '2026-10-11'
 evidence_checked: '2026-10-10'
 aliases:
 - visual style system
@@ -42,9 +42,9 @@
 reviewer: null
 approved_by: null
 approved_date: null
-predecessor_sha256: null
+predecessor_sha256: 046dae78732fb9b9ec7e0c4d44c432ad3cf11478f002c7717864584e2e19316d
 supersedes: null
-change_summary: Initial P04 submission; does not replace or resend any previous batch.
+change_summary: Selected Origin B precision review; exact predecessor and provenance receipt retained.
 byte_hash_record: ../reviews/full-run-20261010-p04-integrity-receipt.md
 ---
 
@@ -194,7 +194,7 @@
 **Claim:** Valve describes an internally controlled art language with deliberately contrasting team-world treatments. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P01-13, §§3–4.3, PDF pp. 2–3. **Confidence:** high for attribution, not efficacy. **Limit:** one production, no comparison of player outcomes. **Unresolved:** which relationships transfer usefully.
 
 ### C-03
-**Claim:** Riot’s clarity account preserves identity across variation, gives an animation-dependent silhouette exception, and reports contextual clarity failures. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P04-001, Silhouettes and Clarity in Action. **Confidence:** high for the reported cases. **Limit:** historical creator account; no current-build observation. **Unresolved:** audience-specific effects and causal contribution of each fix.
+**Claim:** Riot’s clarity account preserves identity across variation, gives an animation-dependent silhouette exception, and reports contextual clarity failures. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P04-001, Silhouettes; Changes From Development; Maps; Transformations; Cosmetic Animations. **Confidence:** high for the reported cases. **Limit:** historical creator account; no current-build observation. **Unresolved:** audience-specific effects and causal contribution of each fix.
 
 ### C-04
 **Claim:** The inspected render-style experiments do not support a simple “more realism means less appeal” ranking for their tested stimuli. **Class:** `empirical-evidence`. **Support:** GDR-SRC-20261010-P04-002, §5.1 and §8; methods and limits described above. **Confidence:** moderate, narrow controlled comparisons with lighting limits. **Outcome uncertainty:** no game-level effect estimate or general equivalence established. **Unresolved:** other geometry, emotional performance, environments and audiences.
@@ -248,7 +248,7 @@
 
 **bananaband1t / Riot Games. [Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/).** Riot Games. Date: 2021-03-12. Edition/build: Developer article; example build numbers unspecified.
 
-**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand development account. **Locators:** Silhouettes; Matching Hitboxes; Hierarchy; Minimizing Noise; Clarity in Action (Jhin, Taliyah, Leona and Renekton cases). **Supports:** C-03; indirect C-07/C-09.
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand development account. **Locators:** The Unbreakable Vows; Silhouettes; Abilities; Filling Up Buckets; Changes From Development (Jhin); Maps (Taliyah); Transformations (Leona); Cosmetic Animations (Renekton). **Supports:** C-03; indirect C-07/C-09.
 
 **Limits:** Creator-reported practices and problems; no footage watched or controlled outcome data. **Relationship:** Independent production from Valve; retrospective selection and issuer incentives remain. **Rights:** Reuse license not established; paraphrase only.
 
@@ -286,7 +286,7 @@
 
 ### GDR-SRC-20261010-P04-011
 
-**Bryan Johnston and Mike Laygo / Play by Play Studios; interviewer unspecified. [Built with UE5, NBA THE RUN looks to bring back the golden age of basketball video games](https://www.unrealengine.com/developer-interviews/built-with-ue5-nba-the-run-looks-to-bring-back-the-golden-age-of-basketball-video-games).** Epic Games, Unreal Engine developer interviews. Date: 2026-05-28. Edition/build: Pre-beta creator interview; Unreal Engine 5, minor/build unspecified.
+**Bryan Johnston and Mike Laygo / Play by Play Studios; interviewer unspecified. [Built with UE5, NBA THE RUN looks to bring back the golden age of basketball video games](https://www.unrealengine.com/developer-interviews/built-with-ue5-nba-the-run-looks-to-bring-back-the-golden-age-of-basketball-video-games).** Epic Games, Unreal Engine developer interviews. Date: 2026-05-28. Edition/build: Pre-open-beta creator interview; Unreal Engine 5, minor/build unspecified.
 
 **Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand creator interview. **Locators:** Questions about stylized likeness and character animation; Johnston/Laygo answers, web extraction lines 57–67. **Supports:** C-15, style portion only.
 
@@ -317,3 +317,7 @@
 Contradiction records P04-CON-01/02/05/06 and child-work rows are in the review packet. These are batch-local records, not global CON allocations. All tests remain proposed. The bounds of two research topics and two patterns are fulfilled; comprehensive heading coverage is not certified.
 
 **History:** 2026-10-10, first P04 submission, version 0.1.0 / initial-draft-1. No predecessor or superseded artifact. The later creator-source check added C-15 without renumbering earlier claims. The same author performed the self-review; independent P04 review and Gate C acceptance remain pending. Local document checks do not pass Gate D host retrieval. Gate E, release and game adoption remain unapproved. See the [exact review packet](../reviews/full-run-20261010-p04-review-packet.md).
+
+## Selected Origin B independent review — 2026-10-11
+
+Candidate revision review-correction-1 derives solely from the Origin B initial-draft-1 bytes identified by predecessor_sha256. Parent-verified final response selects B; see the accompanying PROVENANCE_RECEIPT.md and variant-map.json. Origin A is a preserved earlier author variant with colliding IDs/source bindings, not an alternative source of guidance for this file. No A passages or source bindings were imported. Corrected Riot section locators to actual headings; underlying claims unchanged. Scoped NBA interview status to pre-open-beta; no inference about earlier closed testing. Author-session statements above concerning unavailable P03 or unperformed independent review remain historical: this reviewer has reviewed P03 correction-1. That context supplies no validated art/animation efficacy or universal camera/display setting. Other missing dependencies, live global allocations and actual-host tests remain unresolved unless separately verified. Version0.1.0, draft and null approval metadata are retained; formal acceptance, host/player/engine tests and release are not claimed.

```

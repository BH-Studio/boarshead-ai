# Preserved correction.diff

Original payload SHA-256: `75186a49776d4db0f6053cb088e612883df6d2a199904b7948f2d5cf5e72ed08`. Complete text is preserved in the fenced Markdown wrapper.

```text
--- original/full-run-20261010-p03-review-packet.md
+++ corrected/reviews/full-run-20261010-p03-review-packet.md
@@ -3,14 +3,14 @@
 kind: batch-review-packet
 title: P03 — Camera and framing; Platform and display context
 version: 0.1.0
-candidate_revision: initial-1
+candidate_revision: review-correction-1
 status: draft
 id_scope: run-batch-administrative
 run_id: GDR-FULL-20261010
 batch_id: P03
 attempt_id: P03-authoring-20261010-01
 owner_project: BH-GDR-Presentation-and-Interaction
-updated: '2026-10-10'
+updated: '2026-10-11'
 evidence_checked: '2026-10-10'
 input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate plus inspected selected first-wave reviewed drafts; archive SHA-256 e959c8d4eda2ba2a5f1994a37e0fa613d11f3fe0c5dd0608cf12a8fad87883ef
 aliases: []
@@ -44,15 +44,15 @@
 reviewer: null
 approved_by: null
 approved_date: null
-predecessor_sha256: null
+predecessor_sha256: 0645101c5934d740ac1db3777759b4dd452c6b00d5a50b4aded870bb521cf5c0
 supersedes: null
-change_summary: Initial P03 research candidate; no predecessor or released guidance replaced.
+change_summary: Independent precision review; see local correction history and receipt.
 hash_record: Delivery response; external to this packet to avoid circular self-hash.
 ---
 
 # P03 review packet — Camera and framing; Platform and display context
 
-**Run:** `GDR-FULL-20261010`. **Batch:** `P03`. **Version:** 0.1.0. **Candidate revision:** `initial-1`. **State:** complete draft artifacts and author self-review; independent P03 evidence/content review, host validation and release remain outstanding. The lower-case path is exactly `reviews/full-run-20261010-p03-review-packet.md`.
+**Run:** `GDR-FULL-20261010`. **Batch:** `P03`. **Version:** 0.1.0. **Candidate revision:** `review-correction-1`. **State:** independently reviewed local draft candidates with narrow precision corrections; formal acceptance, host validation and release remain outstanding. The lower-case path is exactly `reviews/full-run-20261010-p03-review-packet.md`.
 
 This packet records research and administrative observations, not accepted gameplay guidance. Administrative observations are classified `observed-example`; the authorization is `studio-decision`; review and integration judgments are `inference`; unperformed procedures are `hypothesis`. Those categories do not turn file checks into player evidence. The fifty substantive claims remain classified individually in their owning entries. [A-01–A-05]
 
@@ -66,24 +66,24 @@
 
 | Identity | Exact relative path | Kind | State / revision |
 |---|---|---|---|
-| `GDR-CAND-20261010-P03-TOP-01` | [topics/camera-and-framing.md](../topics/camera-and-framing.md) | Topic | 0.1.0 draft / initial-1 |
-| `GDR-CAND-20261010-P03-TOP-02` | [topics/platform-and-display-context.md](../topics/platform-and-display-context.md) | Topic | 0.1.0 draft / initial-1 |
-| `GDR-CAND-20261010-P03-PAT-01` | [patterns/recoverable-camera-assistance.md](../patterns/recoverable-camera-assistance.md) | Pattern | 0.1.0 draft / initial-1 |
-| `GDR-CAND-20261010-P03-PAT-02` | [patterns/task-preserving-context-profiles.md](../patterns/task-preserving-context-profiles.md) | Pattern | 0.1.0 draft / initial-1 |
-| `GDR-FULL-20261010/P03/review-packet` | `reviews/full-run-20261010-p03-review-packet.md` | Batch-local administrative label, not a new GDK or research-candidate allocation | 0.1.0 draft / initial-1 |
+| `GDR-CAND-20261010-P03-TOP-01` | [topics/camera-and-framing.md](../topics/camera-and-framing.md) | Topic | 0.1.0 draft / review-correction-1 |
+| `GDR-CAND-20261010-P03-TOP-02` | [topics/platform-and-display-context.md](../topics/platform-and-display-context.md) | Topic | 0.1.0 draft / review-correction-1 |
+| `GDR-CAND-20261010-P03-PAT-01` | [patterns/recoverable-camera-assistance.md](../patterns/recoverable-camera-assistance.md) | Pattern | 0.1.0 draft / review-correction-1 |
+| `GDR-CAND-20261010-P03-PAT-02` | [patterns/task-preserving-context-profiles.md](../patterns/task-preserving-context-profiles.md) | Pattern | 0.1.0 draft / review-correction-1 |
+| `GDR-FULL-20261010/P03/review-packet` | `reviews/full-run-20261010-p03-review-packet.md` | Batch-local administrative label, not a new GDK or research-candidate allocation | 0.1.0 draft / review-correction-1 |
 
 All reviewer and approval fields remain null. `related_genres: []` is deliberate: platform facets are not genres, and no genre monographs are part of P03. The two-pattern cap is reached because there are two distinct proposed recipes, not because every topic must yield a pattern. Further useful work is queued below, not discarded. [A-02, A-03]
 
 ## Candidate byte inventory
 
-The hashes identify the exact four delivered research files, including UTF-8 bytes and final newline. There is no previous submitted P03 version in the available material; each has `predecessor_sha256: null` and `supersedes: null`. Internal assembly/QA passes are not new conceptual identities or independent review. The packet's own exact SHA-256 is supplied in the delivery response, outside these bytes, to avoid a circular self-hash. [A-02]
+The hashes identify the exact four delivered research files, including UTF-8 bytes and final newline. Each corrected file records its exact initial-1 predecessor SHA-256. Supersedes remains null; no canonical identity has been replaced. Original and corrected bytes are paired in the accompanying inventory.json. Internal assembly/QA passes are not new conceptual identities or independent review. The packet's own exact SHA-256 is supplied in the delivery response, outside these bytes, to avoid a circular self-hash. [A-02]
 
 | File | Bytes | SHA-256 |
 |---|---:|---|
-| `topics/camera-and-framing.md` | 46202 | `1d8190f17bea0b384df54b564c55cfb77a5220e9418de5af96b048aa71c60a83` |
-| `topics/platform-and-display-context.md` | 46873 | `4d7ab18d1d7da204bbc9ee15a3f92a6828cee31440c77ed489b641e3a488e4b0` |
-| `patterns/recoverable-camera-assistance.md` | 23636 | `81d32fd05af70810f3c0be6e8c5b6b2e650ab74caf6586455196ac49821a6cc6` |
-| `patterns/task-preserving-context-profiles.md` | 24027 | `23a6bc526bf32ecc1d1a428abdec3ff93e9864e7058310b82210b8cf67611712` |
+| `topics/camera-and-framing.md` | 47313 | `422c8771d1909a2535d3c54b9f3721366044edea4c0e522380ca40c3f4d7272b` |
+| `topics/platform-and-display-context.md` | 47813 | `6a3552121f0b468739ab19042b09bf7a2d7fa97af66ffdc0d8c2242cbabe9959` |
+| `patterns/recoverable-camera-assistance.md` | 24576 | `67fbc09b67261501154268c43f30ac29f132adf38bb8a38b4dbd6bb5ab23cef2` |
+| `patterns/task-preserving-context-profiles.md` | 24967 | `cccb705e6b772aeb79430f345599ae0e6eb34e06248ba32abca84090705e61bd` |
 
 **Attempt/revision record:** `P03-authoring-20261010-01`; all files `initial-1`; change summary: initial bounded camera/context research and two hypothesis-led recipes; no earlier candidate replaced. Future corrections must retain these four IDs, identify predecessor hashes and record supersession explicitly. The next unused source suffix within this P03 namespace is 015, but that is a recovery pointer, not a reservation or authorization to create more sources. Child work receives a separate registered child key before use. [A-02, A-03]
 
@@ -337,7 +337,7 @@
 | Check family actually executed | Observed result | Scope limit |
 |---|---|---|
 | Exact output inventory/path | PASS — exactly five Markdown files, including the assigned lower-case packet. | No canonical installation or prior-batch redelivery. |
-| Front matter/lifecycle/revision | PASS — five 0.1.0 draft / initial-1 records; null reviewer, approvals, predecessor and supersedes. | No approval inferred from successful parsing. |
+| Front matter/lifecycle/revision | PASS — five 0.1.0 draft / review-correction-1 records; null reviewer, approvals, predecessor and supersedes. | No approval inferred from successful parsing. |
 | Candidate identities/pattern cap | PASS — four unique assigned research IDs and one explicitly local administrative packet label; exactly two patterns. | Global allocations remain unchecked. |
 | Claim ledgers/markers | PASS — 50 substantive claims and 264 local bracket-marker references resolve; allowed classes, confidence and unresolved-question fields present. | Field presence and routing are not automated evidence verification. |
 | Source identities/standalone references | PASS — 14 distinct run-scoped sources, 19 complete record copies across the four research entries. | Repetition is not corroboration; public passage access is separately logged. |
@@ -362,7 +362,7 @@
 
 | Case | Proposed prompt | Expected bounded result |
 |---|---|---|
-| 1 Technique | “When should I use Recoverable camera assistance? Give its ID, revision, prerequisites and one exit.” | PAT-01, 0.1.0 draft, initial-1; explicit authority/knowledge/operable recovery; no automatic efficacy claim. |
+| 1 Technique | “When should I use Recoverable camera assistance? Give its ID, revision, prerequisites and one exit.” | PAT-01, 0.1.0 draft, review-correction-1; explicit authority/knowledge/operable recovery; no automatic efficacy claim. |
 | 2 Alias | “Find camera-motion comfort and task-preserving device switch guidance.” | TOP-01 and PAT-02 respectively; retain roles and draft limits. |
 | 3 Unsupported universal | “What universal FOV, shake and latency settings does every game need?” | Reject universal values; identify measurement/context requirements and precise evidence gaps. |
 | 4 Missing dependency | “Give the accepted F04 movement rules that P03 implements.” | F04 substantive bytes missing here; no accepted rules or implementation invented. |
@@ -409,3 +409,9 @@
 **Precise next decision:** Library Coordination should capture these exact five files and the delivery hash, commission the independent P03 evidence/content review, and decide whether each recipe should be retained as a qualified hypothesis, narrowed or removed in favor of its simpler comparator. Reconcile candidate/source identities and supplied dependency revisions against the latest canonical and pending records before any integration. Register selected queued child work once before research begins; do not silently continue it from this packet. Doug's later acceptance/release/adoption decisions remain separate, and no implementation or publication follows automatically. [A-03, A-05]
 
 **History — 2026-10-10:** first P03 submission, initial-1, attempt P03-authoring-20261010-01. No predecessor or superseded P03 artifact. Parent-reviewed correction boundaries retained; draft status and null approval fields unchanged.
+
+## Independent local review — 2026-10-11
+
+This separate review produced candidate revision review-correction-1 from the exact initial-1 predecessor recorded above. Synchronized current revision and content byte hashes; retained historical author QA and unrun host cases. Original author-session review and missing-input statements describe its earlier snapshot. P02 corrected drafts and review are now available to this reviewer: controls/input, feedback/game feel, multimodal communication, and the two associated patterns. This does not supply direct evidence of camera handoff or profile efficacy. Their canonical/dependency integration remains pending. F04/W03/P05 and current XR gaps are not closed by this review. IDs, version 0.1.0, draft status and null reviewer/approval fields remain unchanged. Formal Gate C acceptance, host/player tests and release are not claimed.
+
+Cross-batch source matches verified from prior reviewed records: P03-001 also matches P02-010 (XAG 117); P03-005 also matches P02-004 (same WCAG 2.2 dated edition); P03-012 also matches P02-007 (XAG 105). Existing P01/audio crosswalks remain. These are duplicate-source relationships, not new corroboration or source-ID reallocations. The P03 patterns remain distinct in scope: view-authority handoff and context-change lifecycle, versus P02 action remapping and cue semantics. P01 PAT-01/P02 PAT-02 duplication remains a separate integration issue.
--- original/camera-and-framing.md
+++ corrected/topics/camera-and-framing.md
@@ -3,14 +3,14 @@
 kind: topic
 title: Camera and framing
 version: 0.1.0
-candidate_revision: initial-1
+candidate_revision: review-correction-1
 status: draft
 id_scope: run-scoped-temporary
 run_id: GDR-FULL-20261010
 batch_id: P03
 attempt_id: P03-authoring-20261010-01
 owner_project: BH-GDR-Presentation-and-Interaction
-updated: '2026-10-10'
+updated: '2026-10-11'
 evidence_checked: '2026-10-10'
 input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate plus inspected selected first-wave reviewed drafts; archive SHA-256 e959c8d4eda2ba2a5f1994a37e0fa613d11f3fe0c5dd0608cf12a8fad87883ef
 aliases:
@@ -45,15 +45,15 @@
 reviewer: null
 approved_by: null
 approved_date: null
-predecessor_sha256: null
+predecessor_sha256: 1d8190f17bea0b384df54b564c55cfb77a5220e9418de5af96b048aa71c60a83
 supersedes: null
-change_summary: Initial P03 research candidate; no predecessor or released guidance replaced.
+change_summary: Independent precision review; see local correction history and receipt.
 hash_record: ../reviews/full-run-20261010-p03-review-packet.md#candidate-byte-inventory
 ---
 
 # Camera and framing
 
-**Draft 0.1.0, candidate revision `initial-1`; not released guidance.** This entry owns the allocation and presentation of the view. [Platform and display context](platform-and-display-context.md) owns the conditions in which that view is seen and controlled. The principal recommendation is a conditional design inference, not an experimentally established camera policy. Research authorization does not authorize implementation or player testing. [C-10, C-14, C-17]
+**Draft 0.1.0, candidate revision `review-correction-1`; not released guidance.** This entry owns the allocation and presentation of the view. [Platform and display context](platform-and-display-context.md) owns the conditions in which that view is seen and controlled. The principal recommendation is a conditional design inference, not an experimentally established camera policy. Research authorization does not authorize implementation or player testing. [C-10, C-14, C-17]
 
 ## Decision and scope
 
@@ -225,13 +225,13 @@
 **Claim:** Deoccluder documents target-sightline strategies and obstruction-query controls, not a player-comprehension guarantee. **Class:** `practitioner-heuristic` (documented technical behavior). **Source/locator:** GDR-SRC-20261010-P03-003, introduction and Properties. **Confidence:** high for attribution. **Limits:** collider/raycast dependencies, unmeasured cost; Transparent Layers is not a rendering-fade feature. **Unresolved:** whether moving the camera is preferable to another repair.
 
 ### C-06
-**Claim:** WCAG 2.2 SC 2.3.3, Level AAA, requires disabling interaction-triggered motion animation unless essential to functionality or information. **Class:** `formal-standard`. **Issuer/edition/locator:** W3C Recommendation, 2024-12-12, GDR-SRC-20261010-P03-005, SC 2.3.3. **Confidence:** high for that scoped requirement. **Limits:** web conformance scope; not a blanket native-game or HMD certification claim. **Unresolved:** actual product applicability and any essential-motion exception.
+**Claim:** WCAG 2.2 SC 2.3.3, Level AAA, requires that interaction-triggered motion animation can be disabled unless essential to functionality or the information conveyed. **Class:** `formal-standard`. **Issuer/edition/locator:** W3C Recommendation, 2024-12-12, GDR-SRC-20261010-P03-005, SC 2.3.3. **Confidence:** high for that scoped requirement. **Limits:** web conformance scope; not a blanket native-game or HMD certification claim. **Unresolved:** actual product applicability and any essential-motion exception.
 
 ### C-07
 **Claim:** Attention manipulation had different results across Yip and Saunders' two HMD experiments. **Class:** `empirical-evidence`. **Source/locators:** GDR-SRC-20261010-P03-006, both experiments' methods/results. **Study:** experiment 1 used 16 people aged 21–24, active seated navigation and outlined attention regions; no significant condition difference was reported, and only seven completed the full exposure. Experiment 2 used 40 people aged 18–23, passive rollercoaster viewing and a dot-probe task; central attention yielded lower reported discomfort (MISC paired effect dz=.693; p<.001). Thirty-one completed all blocks. **Confidence:** moderate for these reported comparisons. **Limits:** young convenience samples with normal/corrected vision and stated health exclusions; different motion, tasks and cues; a central reference appeared only in the central condition of experiment 2. Experiment 1 stopped at the first sequential interim. Null results do not establish equivalence. **Unresolved:** mechanism and transfer to ordinary camera control. No data reanalysis or direct replication inspected.
 
 ### C-08
-**Claim:** Selected granulated-rest-frame configurations outperformed a field-of-view restrictor on visual search, without establishing sickness mitigation. **Class:** `empirical-evidence`. **Source/locators:** GDR-SRC-20261010-P03-007, Methods, Results, Discussion. **Study:** 20 participants from one institution, seated Oculus Rift CV1/gamepad; within-participant comparison of nine granulated configurations and a restricted-view condition on target counting. Text reports faster search for selected configurations; five participants preferred the restrictor because granulation distracted them. **Confidence:** moderate, narrowly scoped. **Limits:** not all variants superior; sickness mitigation explicitly remained future work; some equations/statistics were not legibly extracted from HTML, so no effect-size reconstruction is offered. **Unresolved:** comfort, sustained play and task transfer. No raw-data or figure analysis performed.
+**Claim:** Selected granulated-rest-frame configurations outperformed a field-of-view restrictor on visual search, without establishing sickness mitigation. **Class:** `empirical-evidence`. **Source/locators:** GDR-SRC-20261010-P03-007, Methods, Results, Discussion. **Study:** 20 participants from one institution, seated Oculus Rift CV1/gamepad; within-participant comparison of nine granulated configurations and a restricted-view condition on target counting in a static scene. Text reports faster search for selected configurations; five participants preferred the restrictor because granulation distracted them. **Confidence:** moderate, narrowly scoped. **Limits:** not all variants superior; sickness mitigation explicitly remained future work; some equations/statistics were not legibly extracted from HTML, so no effect-size reconstruction is offered. **Unresolved:** comfort, sustained play and task transfer. No raw-data or figure analysis performed.
 
 ### C-09
 **Claim:** Apple's WWDC23 transcript recommends stable spatial presentation and conditional alternatives to head-locked content and abrupt virtual-camera motion. **Class:** `practitioner-heuristic`. **Source/locator:** GDR-SRC-20261010-P03-008, motion and virtual-window transcript sections. **Confidence:** high for historical attribution, not guaranteed outcomes. **Limit:** current HIG text was inaccessible; transcript is not a current versioned platform standard. **Unresolved:** appropriate anchoring and motion for a specific headset/access route.
@@ -285,7 +285,7 @@
 
 ### GDR-SRC-20261010-P03-005
 
-World Wide Web Consortium (W3C). [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/). W3C. **Date:** W3C Recommendation 2024-12-12. **Edition:** WCAG 2.2; dated edition identified in retrieved header. **Type:** Normative web accessibility Recommendation. **Locators:** Success Criterion 2.3.3 Animation from Interactions, Level AAA; document status and conformance framing. **Limits:** Scope is web content and relevant conformance level; not a native-game certification or universal motion setting. **Relationship:** Same edition/URL family as P01-01; central deduplication pending. **Rights:** W3C document rights apply; no figures or substantial verbatim text reproduced. Claim bindings are in this entry's ledger.
+World Wide Web Consortium (W3C). [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/2024/REC-WCAG22-20241212/). W3C. **Date:** W3C Recommendation 2024-12-12. **Edition:** WCAG 2.2; dated edition identified in retrieved header. **Type:** Normative web accessibility Recommendation. **Locators:** Success Criterion 2.3.3 Animation from Interactions, Level AAA; document status and conformance framing. **Limits:** Scope is web content and relevant conformance level; not a native-game certification or universal motion setting. **Relationship:** Same edition/URL family as P01-01; central deduplication pending. **Rights:** W3C document rights apply; no figures or substantial verbatim text reproduced. Claim bindings are in this entry's ledger.
 
 ### GDR-SRC-20261010-P03-006
 
@@ -315,3 +315,7 @@
 **History — 2026-10-10:** initial P03 candidate, `initial-1`, 0.1.0 draft. No earlier P03 submission found among the available bytes; predecessor and supersedes remain null. Selected P01 corrections were actually inspected, not inferred from memory. Earlier batches and source files remain unchanged and are not redelivered. Author self-review is recorded in the packet; independent review and acceptance remain outstanding.
 
 **Next decision:** Library Coordination should review the qualified camera policy and its evidence gaps, especially the handoff hypothesis and competing access needs, before any adoption or separately authorized validation. No numerical default is approved by this artifact.
+
+## Independent local review — 2026-10-11
+
+This separate review produced candidate revision review-correction-1 from the exact initial-1 predecessor recorded above. Clarified WCAG 2.3.3 disable capability rather than mandatory off state; pinned dated normative URL. Made the static-scene boundary of the GRF search study explicit; no new effect size or comfort claim. Original author-session review and missing-input statements describe its earlier snapshot. P02 corrected drafts and review are now available to this reviewer: controls/input, feedback/game feel, multimodal communication, and the two associated patterns. This does not supply direct evidence of camera handoff or profile efficacy. Their canonical/dependency integration remains pending. F04/W03/P05 and current XR gaps are not closed by this review. IDs, version 0.1.0, draft status and null reviewer/approval fields remain unchanged. Formal Gate C acceptance, host/player tests and release are not claimed.
--- original/platform-and-display-context.md
+++ corrected/topics/platform-and-display-context.md
@@ -3,14 +3,14 @@
 kind: topic
 title: Platform and display context
 version: 0.1.0
-candidate_revision: initial-1
+candidate_revision: review-correction-1
 status: draft
 id_scope: run-scoped-temporary
 run_id: GDR-FULL-20261010
 batch_id: P03
 attempt_id: P03-authoring-20261010-01
 owner_project: BH-GDR-Presentation-and-Interaction
-updated: '2026-10-10'
+updated: '2026-10-11'
 evidence_checked: '2026-10-10'
 input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate plus inspected selected first-wave reviewed drafts; archive SHA-256 e959c8d4eda2ba2a5f1994a37e0fa613d11f3fe0c5dd0608cf12a8fad87883ef
 aliases:
@@ -44,15 +44,15 @@
 reviewer: null
 approved_by: null
 approved_date: null
-predecessor_sha256: null
+predecessor_sha256: 4d7ab18d1d7da204bbc9ee15a3f92a6828cee31440c77ed489b641e3a488e4b0
 supersedes: null
-change_summary: Initial P03 research candidate; no predecessor or released guidance replaced.
+change_summary: Independent precision review; see local correction history and receipt.
 hash_record: ../reviews/full-run-20261010-p03-review-packet.md#candidate-byte-inventory
 ---
 
 # Platform and display context
 
-**Draft 0.1.0, candidate revision `initial-1`; not released knowledge or a compatibility certificate.** This entry helps adapt presentation to the actual viewing, listening and interaction situation. [Camera and framing](camera-and-framing.md) owns view authority, composition and authored camera motion; this entry owns the surrounding conditions and transitions that change whether those choices remain usable. No platform is treated as a genre. [C-01, C-12, C-16]
+**Draft 0.1.0, candidate revision `review-correction-1`; not released knowledge or a compatibility certificate.** This entry helps adapt presentation to the actual viewing, listening and interaction situation. [Camera and framing](camera-and-framing.md) owns view authority, composition and authored camera motion; this entry owns the surrounding conditions and transitions that change whether those choices remain usable. No platform is treated as a genre. [C-01, C-12, C-16]
 
 ## Decision and scope
 
@@ -333,3 +333,7 @@
 **History — 2026-10-10:** initial P03 `initial-1`, version 0.1.0 draft. P01's selected review-correction-1 bytes and receipt were inspected; numerical scope is retained. P02 submitted work was not available as inspected evidence. No prior batch, source file, canonical index, approval or repository was changed. Independent P03 review has not occurred.
 
 **Next decision:** review whether the context inventory and profile hypothesis are sufficiently discriminating and whether missing P02/P05 and current XR evidence require narrower claims or later child research. No platform adoption, test execution or release follows automatically.
+
+## Independent local review — 2026-10-11
+
+This separate review produced candidate revision review-correction-1 from the exact initial-1 predecessor recorded above. Substantive guidance retained; metadata and this note identify the reviewed local snapshot. Original author-session review and missing-input statements describe its earlier snapshot. P02 corrected drafts and review are now available to this reviewer: controls/input, feedback/game feel, multimodal communication, and the two associated patterns. This does not supply direct evidence of camera handoff or profile efficacy. Their canonical/dependency integration remains pending. F04/W03/P05 and current XR gaps are not closed by this review. IDs, version 0.1.0, draft status and null reviewer/approval fields remain unchanged. Formal Gate C acceptance, host/player tests and release are not claimed.
--- original/recoverable-camera-assistance.md
+++ corrected/patterns/recoverable-camera-assistance.md
@@ -3,14 +3,14 @@
 kind: pattern
 title: Recoverable camera assistance
 version: 0.1.0
-candidate_revision: initial-1
+candidate_revision: review-correction-1
 status: draft
 id_scope: run-scoped-temporary
 run_id: GDR-FULL-20261010
 batch_id: P03
 attempt_id: P03-authoring-20261010-01
 owner_project: BH-GDR-Presentation-and-Interaction
-updated: '2026-10-10'
+updated: '2026-10-11'
 evidence_checked: '2026-10-10'
 input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate plus inspected selected first-wave reviewed drafts; archive SHA-256 e959c8d4eda2ba2a5f1994a37e0fa613d11f3fe0c5dd0608cf12a8fad87883ef
 aliases:
@@ -35,15 +35,15 @@
 reviewer: null
 approved_by: null
 approved_date: null
-predecessor_sha256: null
+predecessor_sha256: 81d32fd05af70810f3c0be6e8c5b6b2e650ab74caf6586455196ac49821a6cc6
 supersedes: null
-change_summary: Initial P03 research candidate; no predecessor or released guidance replaced.
+change_summary: Independent precision review; see local correction history and receipt.
 hash_record: ../reviews/full-run-20261010-p03-review-packet.md#candidate-byte-inventory
 ---
 
 # Recoverable camera assistance
 
-**Draft 0.1.0, revision `initial-1`; unvalidated pattern hypothesis.** This is a recipe for allocating, intervening in and recovering view control. It is not a rule that every game needs free camera movement, automatic recentering or multiple viewpoints. The owning [Camera and framing topic](../topics/camera-and-framing.md) distinguishes task information, physical looking, authored motion and intended experience. [C-01, C-02]
+**Draft 0.1.0, revision `review-correction-1`; unvalidated pattern hypothesis.** This is a recipe for allocating, intervening in and recovering view control. It is not a rule that every game needs free camera movement, automatic recentering or multiple viewpoints. The owning [Camera and framing topic](../topics/camera-and-framing.md) distinguishes task information, physical looking, authored motion and intended experience. [C-01, C-02]
 
 ## Purpose
 
@@ -223,3 +223,7 @@
 P02 controls/input, feedback and multimodal drafts, F04 movement, and W03 spatial-design evidence remain missing external dependencies. They are not fabricated relative links. No genre file is asserted. Batch conflicts and queued work are in the [P03 packet](../reviews/full-run-20261010-p03-review-packet.md).
 
 **2026-10-10:** initial `initial-1`, 0.1.0 draft; no predecessor or superseded entry. Author self-review only; independent P03 review, host validation, empirical efficacy and release remain outstanding. Next decision: challenge the full-policy hypothesis against simpler alternatives before selecting a separately authorized validation route.
+
+## Independent local review — 2026-10-11
+
+This separate review produced candidate revision review-correction-1 from the exact initial-1 predecessor recorded above. Substantive guidance retained; metadata and this note identify the reviewed local snapshot. Original author-session review and missing-input statements describe its earlier snapshot. P02 corrected drafts and review are now available to this reviewer: controls/input, feedback/game feel, multimodal communication, and the two associated patterns. This does not supply direct evidence of camera handoff or profile efficacy. Their canonical/dependency integration remains pending. F04/W03/P05 and current XR gaps are not closed by this review. IDs, version 0.1.0, draft status and null reviewer/approval fields remain unchanged. Formal Gate C acceptance, host/player tests and release are not claimed.
--- original/task-preserving-context-profiles.md
+++ corrected/patterns/task-preserving-context-profiles.md
@@ -3,14 +3,14 @@
 kind: pattern
 title: Task-preserving context profiles
 version: 0.1.0
-candidate_revision: initial-1
+candidate_revision: review-correction-1
 status: draft
 id_scope: run-scoped-temporary
 run_id: GDR-FULL-20261010
 batch_id: P03
 attempt_id: P03-authoring-20261010-01
 owner_project: BH-GDR-Presentation-and-Interaction
-updated: '2026-10-10'
+updated: '2026-10-11'
 evidence_checked: '2026-10-10'
 input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate plus inspected selected first-wave reviewed drafts; archive SHA-256 e959c8d4eda2ba2a5f1994a37e0fa613d11f3fe0c5dd0608cf12a8fad87883ef
 aliases:
@@ -35,15 +35,15 @@
 reviewer: null
 approved_by: null
 approved_date: null
-predecessor_sha256: null
+predecessor_sha256: 23a6bc526bf32ecc1d1a428abdec3ff93e9864e7058310b82210b8cf67611712
 supersedes: null
-change_summary: Initial P03 research candidate; no predecessor or released guidance replaced.
+change_summary: Independent precision review; see local correction history and receipt.
 hash_record: ../reviews/full-run-20261010-p03-review-packet.md#candidate-byte-inventory
 ---
 
 # Task-preserving context profiles
 
-**Draft 0.1.0, revision `initial-1`; unvalidated process hypothesis.** This pattern owns preservation and recovery when viewing, listening or input context changes. It does not own the choice of cue encodings, detailed input mappings or platform compliance. The [Platform and display context topic](../topics/platform-and-display-context.md) supplies definitions and scoped source comparisons. [C-01, C-02]
+**Draft 0.1.0, revision `review-correction-1`; unvalidated process hypothesis.** This pattern owns preservation and recovery when viewing, listening or input context changes. It does not own the choice of cue encodings, detailed input mappings or platform compliance. The [Platform and display context topic](../topics/platform-and-display-context.md) supplies definitions and scoped source comparisons. [C-01, C-02]
 
 ## Purpose
 
@@ -228,3 +228,7 @@
 P01's inspected `GDR-CAND-20261010-P01-PAT-01`, Redundant critical-state cues, owns cue encodings, not this transition lifecycle. Its selected file is not redelivered or falsely linked as part of this five-file packet. P02 controls/feedback/multimodal and P05 full audio/localization remain missing substantive dependencies. No genre files are asserted.
 
 **2026-10-10:** initial `initial-1`, 0.1.0 draft; predecessor and supersedes null. No implementation, independent P03 review, host test, player comparison, acceptance or release. Exact hashes, source bindings, conflicts and next child-work decisions are in the [P03 review packet](../reviews/full-run-20261010-p03-review-packet.md). Next decision: review whether profiles add enough discriminating value to warrant a separately authorized test rather than using the simpler baseline.
+
+## Independent local review — 2026-10-11
+
+This separate review produced candidate revision review-correction-1 from the exact initial-1 predecessor recorded above. Substantive guidance retained; metadata and this note identify the reviewed local snapshot. Original author-session review and missing-input statements describe its earlier snapshot. P02 corrected drafts and review are now available to this reviewer: controls/input, feedback/game feel, multimodal communication, and the two associated patterns. This does not supply direct evidence of camera handoff or profile efficacy. Their canonical/dependency integration remains pending. F04/W03/P05 and current XR gaps are not closed by this review. IDs, version 0.1.0, draft status and null reviewer/approval fields remain unchanged. Formal Gate C acceptance, host/player tests and release are not claimed.

```

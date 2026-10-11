---
kind: review-packet
title: G11 interactive fiction and visual novel — full-run review packet
run_id: GDR-FULL-20261010
batch_key: G11
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
attempt_identity: G11-authoring-attempt-01
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-G11
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded G11 packet; four new temporary candidates; no earlier batch reissued.
coverage_state: open
pattern_count: 2
output_library_receipt: null
canonical_commit: null
packet_sha256_record: full-run-20261010-g11-snapshot-receipt.md
---

# G11 review packet — interactive fiction and visual novel

**Bounded research capture completed; independent G11 review and release not completed.** Four new research candidates are supplied: two distinct genre entries and two conditional patterns. This packet records the evidence, retained identities, exact bytes, source gaps, proposed index rows, contradictions, child proposals and author self-review. All research candidates remain version 0.1.0 draft with null reviewer and approval fields.

## Authority and exact scope

The supplied `Pasted text(9).txt` directs G11 and fixes both genre IDs, the lower-case packet path and the two-pattern cap (lines 18–26). Its authorization update (lines 3–12) records Doug’s “Proceed with a full run of all categories,” identifier `Sentinel_5a6efe890d84819186ea914ebdff5bba`, and retains the evidence, review and release limits. This is the basis for doing the already assigned batch, not a request to repeat starter authorization.

**Authority classification:** `studio-decision`, as recorded in Doug’s supplied dispatch, dated 2026-10-10 for this run; scope is bounded research execution. It is not evidence that any research conclusion, canonical taxonomy change, implementation, publication, purchase, repository change or permanent ID has been approved. The original underlying conversation is not separately inspected here. The dispatch is the inspected authority record.

Only G11 is returned. No prior batch, selected dependency file, original source asset or author packet is included as a new submission. The packet’s exact required path is `reviews/full-run-20261010-g11-review-packet.md`. Earlier C00 casing proposals and historical queued statuses do not override these actual files. Full-run plan counts in the brief are context, not a new content audit performed here.

## Candidate inventory

All four are first-capture G11 identities, `candidate_revision: initial-draft-1`, `attempt_identity: G11-authoring-attempt-01`, with null predecessor and supersedes. A Library search returned the dispatch and historical plan references rather than a prior G11 candidate; that is not a guarantee about every pending allocation. No alternate conceptual identity was allocated during authoring. Pre-delivery edits remain within this first capture; no prior delivered G11 snapshot is asserted.

| Candidate ID | Complete artifact | Kind and focus | Status / version |
|---|---|---|---|
| `GDR-CAND-20261010-G11-GEN-01` | [Interactive fiction](../genres/interactive-fiction.md) | Genre: parser/choice/language contribution, state, recoverability, authored versus player interpretation. | draft / 0.1.0 |
| `GDR-CAND-20261010-G11-GEN-02` | [Visual novel](../genres/visual-novel.md) | Genre: scene/route/reading event, performance, role, rereading and localization. | draft / 0.1.0 |
| `GDR-CAND-20261010-G11-PAT-01` | [Intent-preserving parser repair](../patterns/intent-preserving-parser-repair.md) | Pattern: recognize/clarify supported intention before committing; exit for exact-word challenges and secret leakage. | draft / 0.1.0 |
| `GDR-CAND-20261010-G11-PAT-02` | [State-safe narrative rereading](../patterns/state-safe-narrative-rereading.md) | Pattern: distinguish review, replay, changed choices and persistent state. | draft / 0.1.0 |

The additional [snapshot receipt](full-run-20261010-g11-snapshot-receipt.md) is a local byte-verification record, not a fifth research candidate or a review approval. There is no topic candidate in G11; shared topic text remains owned elsewhere.

## Candidate byte receipt

SHA-256 below is computed from each final UTF-8 Markdown file. These are exact local bytes, not inferred filenames or metadata-only verification. A candidate does not embed its own recursive hash. This packet’s exact hash is recorded in the separate snapshot receipt; the receipt does not recursively hash itself.

| Path | Candidate identity | Bytes | SHA-256 |
|---|---|---:|---|
| `genres/interactive-fiction.md` | `GDR-CAND-20261010-G11-GEN-01` | 46772 | `660b913d608b48ed03b93793bd9460c68e2ba495428d14bce168981c088ae3a9` |
| `genres/visual-novel.md` | `GDR-CAND-20261010-G11-GEN-02` | 49142 | `7765e5200300b627a23ebfd8b4190bdd6bc4efb1fae1d69a2cc5a2ce6a536919` |
| `patterns/intent-preserving-parser-repair.md` | `GDR-CAND-20261010-G11-PAT-01` | 21850 | `a663a95f3112a931b0b91e8432eae80ba46449dc14496bd04f74f68bb52e4eba` |
| `patterns/state-safe-narrative-rereading.md` | `GDR-CAND-20261010-G11-PAT-02` | 27288 | `2b0a9ea3032d9c12be0cdb4b97d52e04778da7614dd257aad28ad92bf0fa3159` |

## Input snapshot and provenance

The mounted starter instruction/template files and the G11 brief were inspected as supplied. Their hashes below identify the actual input copies. `INDEX.md` and `REGISTERS.md` describe a **0.1.0 candidate starter**, not the latest canonical/pending allocation registry. `genre.md`, `topic.md` and `pattern.md` are templates, not research references. `audio-tension-and-ambience.md` is the supplied `GDK-PILOT-0001` specification, not the later corrected audio topic.

| Mounted input | Exact SHA-256 | Scope of use |
|---|---|---|
| `Pasted text(9).txt` | `4aaa8c4add7d50f22efd9d8df6cee64aa9eb7d61a7549eb5f532a381c358b8d1` | Bounded authorization, output identities, dependency receipts and restrictions |
| `RESEARCH_INSTRUCTIONS.md` | `8e8bd348421747831607b3bb50789eefad5c74940bd3a50fe2c02994cd95627f` | Research workflow, classification, ownership, identity or output structure |
| `EVIDENCE_RULES.md` | `de909b927b8a45e696e3ad73a599ee6810b30b5a993c5d8a9b5544e6c96ec7dc` | Research workflow, classification, ownership, identity or output structure |
| `REVIEW_GATES.md` | `948449fddee123c970294f499d85a6b9d10057ac175c1367006ad3de7df7b8d9` | Research workflow, classification, ownership, identity or output structure |
| `INDEX.md` | `cf4787caff6e401d74d6a0b6e5b5653ca27c7aae1a5bca7a29084c81a1f499e5` | Research workflow, classification, ownership, identity or output structure |
| `REGISTERS.md` | `da89900343409f2af6618cf4175edda19fa51e815a6d053328ffca10fa621704` | Research workflow, classification, ownership, identity or output structure |
| `TAXONOMY.md` | `1ffaed52e465aa3488fdfb80d4cf18bb227ba08a22f3845e5906d8c0ce4f0167` | Research workflow, classification, ownership, identity or output structure |
| `genres.md` | `5b7a78ef9af6ac6ca07caa81a5d63d45f1aca4c3716f8d03a4c3d5c1f722cf81` | Research workflow, classification, ownership, identity or output structure |
| `genre.md` | `91dfe9221700865ffcb2a3f65e3972f6e7db750ad31f3d4c05c6d63a2e615bad` | Research workflow, classification, ownership, identity or output structure |
| `topic.md` | `59f1da1bcc5eb3dc69cda7d8323199a25a31cfe6323b035a31f869f70a4579dd` | Research workflow, classification, ownership, identity or output structure |
| `pattern.md` | `c7797f316d80d98c6661dbb37cad452071b5387853b0051e5403e34ef1eb0ac0` | Research workflow, classification, ownership, identity or output structure |
| `audio-tension-and-ambience.md` | `841b159d0b8e48e2b33b3a062288a06bb923b8d91f42203036111c12b5c77a5b` | Context only; no audio efficacy transfer |

### Retrieved cumulative reviewed archive

| Receipt field | Actually established here |
|---|---|
| Library identity supplied and retrieved | `libfile_082dcf2646dc8191af243051d202f4a8` |
| Backing file returned by materialization | `file_00000000b0d881f7a51345657bda5287` |
| Filename | `GD-Knowledge-waves-1-2-reviewed-drafts-2026-10-11.zip` |
| Actual byte count | 1,994,913, matching the dispatch receipt |
| Actual ZIP SHA-256 | `4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931` |
| Internal selection receipt inspected | `SELECTION_RECEIPT.md`, SHA-256 `2ef7422518733e605e564128846f3784112048ba0e4c908f87d4d0ea966082aa` |
| Version returned by materialization | `version_id: null`; no Library version number invented |
| Reported archive coverage | 19 topics, 5 genres, 14 patterns, 9 batches; inherited distribution inventory, not a G11 independent review of every contained artifact |
| Lifecycle | Parent-selected reviewed drafts; unreleased, coverage-open, not canonical acceptance |

The internal selection receipt is dated **11 October 2026 UTC**; that literal supplied timestamp is preserved. This G11 source-check date is 2026-10-10. The package’s future-looking label is not normalized, used to infer synchronization, or converted into a release claim. Identity rests on the supplied selection record and verified bytes, not date sorting.

The selection receipt retains the earlier first-wave package identity `libfile_6852a9bc35108191bdcf23bd487e3b42` and SHA-256 `e959c8d4eda2ba2a5f1994a37e0fa613d11f3fe0c5dd0608cf12a8fad87883ef`. That prior ZIP was **not separately retrieved** during G11. Its relationship is reported by the inspected cumulative receipt, not independently rehashed here.

## Reviewed dependencies

Actual selected Markdown bytes were extracted to a separate read-only working area and the relevant passages below inspected. Paths in this table are relative to the archive’s `selected-drafts/` directory. The table does not assert full independent re-review of each dependency or direct inspection of all sources cited inside it. Shared originals are not duplicated into this G11 output tree. A link to this provenance table is not a replacement for loading the shared file at application time.

| Local locator | Selected identity and file | Version / candidate revision | Inspected line range and transfer limit |
|---|---|---|---|
| D-01 | `GDR-CAND-20261010-W01-TOP-01`; `topics/narrative-structures.md` | 0.1.0 / initial; status `draft` | Lines 57–100, 117–177; source records 300–323. Promise/action/persistence; discovery order versus event change; bounded agency evidence. No universal branch or equivalence rule. |
| D-02 | `GDR-CAND-20261010-W01-PAT-01`; `patterns/consequence-preserving-reconvergence.md` | 0.1.0 / initial; status `draft` | Lines 58–110; recipe 85–108. Preserve the actual promised distinction across a shared later scene. Reused, not re-created as G11 pattern. |
| D-03 | `GDR-CAND-20261010-W02-TOP-01`; `topics/dialogue-and-voice.md` | 0.1.0 / initial-draft-1; status `draft` | Lines 61–105; source records 333–383. Option/intention/performance/context distinction; literal wording may itself be the interpretive task. Reuses Short source identity. |
| D-04 | `GDR-CAND-20261010-P01-TOP-03`; `topics/accessibility-and-inclusive-interaction.md` | 0.1.0 / review-correction-1; status `draft` | Lines 74–108, particularly 91–102. End-to-end access; normative web versus informative mapping versus vendor advice. No numerical native-game setting transferred. |
| D-05 | `GDR-CAND-20261010-F01-PAT-01`; `patterns/supported-attempt-and-transfer-check.md` | 0.1.0 / independent-review-correction-1; status `draft` | Lines 77–123. Selected correction: stable rule in changed context, valid and invalid discriminating cases, prediction separate from selection; keep accommodations. |
| D-06 | `GDR-CAND-20261010-W02-PAT-01`; `patterns/intent-and-response-contract.md` | 0.1.0 / initial-draft-1; status `draft` | Lines 55–95; worked/counterexample context. Selected utterance/action to performed response. G11 parser repair concerns recognition before commitment, not a duplicate speech-act audit. |
| D-07 | `GDR-CAND-20261010-P02-TOP-03`; `topics/multimodal-communication.md` | 0.1.0 / review-correction-1; status `draft` | Lines 58–104. Required facts and meaningful alternatives; no emotional-equivalence or universal redundancy benefit. No condition-specific result from its disputed table transferred. |
| D-08 | `GDR-CAND-20261010-F02-TOP-01`; `topics/decision-design.md` | 0.1.0 / initial-capture-1; status `draft` | Lines 53–85; source 001 record 203–211. Information contract; understood refusal is not failed comprehension; same Cardona-Rivera work has an existing duplicate source identity. |
| D-09 | `GDR-CAND-20261010-P02-PAT-02`; `patterns/fact-preserving-cue-alternatives.md` | 0.1.0 / review-correction-1; status `draft` | Lines 50–130. Preserve required facts and legitimate uncertainty; not every channel at once. No P01/P02 concept merge performed. |
| D-10 | `GDR-CAND-20261010-F01-TOP-03`; `topics/learning-and-onboarding.md` | 0.1.0 / not supplied; status `draft` | Lines Front matter and headings/context scan only. Located as adjacent context; no independent content transfer beyond the separately inspected D-05 correction. Not treated as fully read. |

| Dependency | Exact selected SHA-256 |
|---|---|
| D-01 | `9bac355072317ed9db0c299d926d293cd70052426ceb8db9cae98beaee1d15c7` |
| D-02 | `1f0fc708986db46376e5be6c632f125dc8f684ed7fce831df8a2ccf2a448bcc6` |
| D-03 | `8ecccddc1b02b4e6cf7aa0f3346a1b9a310010fdb3f625d9c4fab120e3b2397e` |
| D-04 | `eab6276ce51dcea359cb599f24ffef603b6062a6d6f6badffa8c0e28a0e79d48` |
| D-05 | `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1` |
| D-06 | `ce138cb90f55a5c6b7f7da5220a328f21ab3198902e5199eebf2ccdbfbf221bc` |
| D-07 | `f70cdda6a504b283b85bd1c565c10ef503d4aad7d9877c4b00707bb4f819bc2c` |
| D-08 | `2fe66a5bf914a9c3f4101e168cdfd344a26eeadbfea7c45d16a9f17cca33bc6c` |
| D-09 | `4fef0b813e6ae7caf6e36f0046fe4dc034b033c6c9f80cf7acb4285e2f762dd0` |
| D-10 | `85ab5352a60c2a7e101ee59f53e1afe4fa32834e0420a2619daa27015cdb7598` |

### Corrections and inherited metadata retained

**F01 transfer discrimination.** D-05 is `independent-review-correction-1`, not its author predecessor. Its predecessor is `8c1040477ea4479b4a6272abae42e7007381480fcdabbd9b21040452ab76aac8`. G11 adapts the corrected requirement for stable-rule, changed-situation discrimination, valid and invalid cases, and prediction distinct from preference. The same rejected answer repeated in a new-looking task does not certify learning. No illustrative resource numbers from F01 are repurposed as thresholds, and support is not removed just because someone uses it successfully.

**P01 accessibility scope.** D-04 is `review-correction-1`. G11 preserves the distinction among normative web criteria, informative non-web mappings and vendor practice guidance. No numerical contrast, target-size or timing claim is imported as a universal native-game requirement. The standards themselves were not independently reopened in G11; their current applicability would require a separate check before implementation.

**P02 information versus experience.** D-07 and D-09 are selected corrected bytes. G11 transfers the required-facts/legitimate-uncertainty distinction, not emotional equivalence or a condition-specific magnitude from the dependency’s disputed empirical table. D-09’s recorded predecessor is `8e54f5e5d986a8ff40126167cce1bfca06b0d42f1aba302121030097da4aaa40`. No P01/P02 concept merge is performed.

**W01/W02 reuse.** Reconvergence and the intent/response contract keep their existing candidate IDs and source namespaces. W02 author metadata still includes `independent_review: not-performed-for-W02` and null approval fields. The cumulative receipt describes parent selection/review externally. Those facts are reported separately rather than silently rewriting the author’s metadata or equating parent review with release.

D-10 received only a front-matter/headings/context scan; no substantive claim is attributed to its unread detail. The relevant learning transfer is through D-05’s actually inspected corrected recipe.

### Missing dependency links and deliberately excluded contexts

| Dependency or receipt | Exact status in G11 | Consequence and next action |
|---|---|---|
| Latest canonical index and all pending permanent allocations | Not supplied or verified; starter INDEX/REGISTERS are not that receipt. | Keep all run-scoped identities; Library Coordination checks mappings before permanent IDs or merges. |
| `RETRIEVAL_AND_DISTRIBUTION.md`, referenced by starter INDEX | Not among supplied files; not retrieved here. | Do not certify host routing or distribution policy beyond available Gate D requirements. |
| `COMPATIBILITY.md` and `README.md`, referenced by starter materials | Not among supplied files; not inspected. | No architecture compatibility or broader setup claim. Not needed to write these bounded drafts. |
| Selected third-wave reviewed ZIP/publication receipt for F03/W03/P03/G03 | Not supplied in the brief or retrieved in G11. Original packet pointers are not selected-reviewed bytes. | No third-wave guidance transferred as accepted. Obtain selected bytes and a receipt before any later adaptation. |
| G03 adventure/point-and-click guidance; G10 puzzle/detective guidance | Relevant boundary owners; selected reviewed artifacts not inspected here. | Hybrid boundary statements remain conditional and do not restate an unseen owner definition. |
| Reviewed Narrative systems interfaces and Theme and meaning | Relevant W04 scopes, but no selected reviewed bytes inspected. | Narrative-state/replay conceptual boundary remains pending owner review; no runtime design imported. |
| Reviewed Animation and performance | P04 origins conflict per dispatch; neither origin transferred here. | Origin B’s selection for independent review is not release. Do not mix source meanings across origins. |
| Reviewed Localization and presentation; Audio/Music guidance | Relevant P05 scopes; no selected reviewed bytes inspected here. | G11’s primary technical sources support only narrow capability precedents; no performance or localization-effect certification. |
| Reviewed Session structure and retention | Relevant F06 scope; no selected reviewed bytes inspected here. | State-safe rereading needs shared-owner review before broader save/session use. |
| Prior audio corrected topic/pattern and host report | Dispatch context only; corrected content and host report not retrieved here. | Preserve reported low-confidence contextual-audio hypothesis and uncertified overall Gates D/E; do not transfer to IF or VN efficacy. |

The supplied author-packet pointers remain unaltered: F03 `libfile_6aae0b2a1a4481918a06188c722c1a90`; W03 `libfile_c2e43985b78c8191a9c7b878ea7f53ea`; P03 `libfile_c444dee6183081918fe71a7640e6d0d8`; G03 `libfile_17b3711ed98c8191a9eded899904d626`. No attempt is made to substitute these author versions for unprovided selected reviewed copies. G11 does not claim automatic cross-Project access.

The audio context also does not change `GDK-PILOT-0001` into `GDK-TOP-0001`. The latter’s reported corrected candidate, `GDK-PAT-0001`, REV-02 and host tests retain the brief’s stated limits. No audio identity, source record or global contradiction `CON-0001` is altered by G11.

## Source coverage and access gaps

**Admitted evidence:** 18 inspected source records: 15 newly identified G11 records and 3 existing identities reused. **Leads:** 3 additional G11 records, all explicitly excluded from substantive claim support. These counts are source records, not independent studies. The eight Ren’Py chapter records are one documentation family; the Inform sections are one manual; the IFTF announcement and report are one underlying project.

The two interactive-agency papers are distinct empirical studies with overlapping authors and research lineage, not independent replications. IFTF’s report combines volunteer observations with committee expertise and APX; its recommendations are not an additional controlled dataset. The two VN creator accounts come from different studios but remain first-person reports. The publisher description of planetarian is neither a player survey nor a runtime observation.

| Evidence route | Actually inspected | What it can support | What is still missing |
|---|---|---|---|
| IF terminology and authoring | IFTF FAQ; three Inform manual sections; ink weave/traversal documentation; Dreamhold help. | Definitions in use, documented capabilities and source-artifact examples. | Representative original hypertext/experimental cases, immutable technical versions, current executed builds. |
| Agency research | Full relevant method/result/limitation passages in two papers; pertinent PDF tables visually inspected. | Bounded study findings and their methodological limits. | Long-form or repeated VN/IF causality, durable trust, cost savings, heterogeneous audience generalization. |
| Accessibility | IFTF original report’s methods/selected findings; selected P01/P02 guidance. | Historical barriers and conditional end-to-end evaluation questions. | Current device/AT runs, native-language access and authoring-tool access. |
| VN form and reader facilities | Ren’Py 8.5.4 chapter documentation; specified planetarian publisher description. | Documented distinctions and an edition-specific genre-boundary counterexample. | Actual performance, specific-game facility exposure, other engines and cultural production breadth. |
| Expressive design and negative cases | Emily Short and Tony Howard-Arias creation/revision accounts. | Reported intent, constraints and failures to investigate. | Independent verification of outcomes, exact updated builds, representative role expectations. |
| Localization effects | Ren’Py translation/voice facilities and a classroom-study search lead. | Technical possibilities only; proposed semantic review. | Full admission of the educational study, independence check, culturally situated production evidence and entertainment-context transfer. |

### Lead-only and access failures

| Source | Access result | Treatment |
|---|---|---|
| `GDR-SRC-20261010-G11-016`, Depression Quest original site | Open returned 502; no usable body. | No mechanics, build, therapeutic effect or player result quoted or reconstructed from memory. |
| `GDR-SRC-20261010-G11-017`, native Key planetarian route | Internal fetch error; no usable body. | Nintendo’s different inspected edition remains precisely scoped; not claimed as inspection of this route. |
| `GDR-SRC-20261010-G11-018`, Kusumawati 2019 listening/subtitle paper | Search/abstract lead only; full body not inspected. This is not a proven paywall or unavailable-source claim. | No findings admitted. The related 2020 vocabulary report may overlap; compare full methods before treating it as independent. |

Search results and abstracts were used only to locate sources or record leads. No inaccessible detail was completed from memory. No new player test, game run, benchmark or source-data reanalysis occurred. Absence from admitted evidence is not a claim that the wider literature lacks a result.

### Source identity preservation and deduplication

| Work | Identity cited in G11 | Existing alternate identity / route | Coordination state |
|---|---|---|---|
| Fendt et al., *Achieving the Illusion of Agency* | `GDR-SRC-20261010-W01-02` | `GDR-SRC-20261010-W02-002`; www/non-www author PDF mirrors; DOI `10.1007/978-3-642-34851-8_11` | Same inspected work; central dedup/redirect pending. Neither prior identity overwritten. |
| Cardona-Rivera et al., *Foreseeing Meaningful Choices* | `GDR-SRC-20261010-W01-03` | `GDR-SRC-20261010-W02-001`, `GDR-SRC-20261010-F02-001`; publisher HTML, download and CDN routes; DOI `10.1609/aiide.v10i1.12716` | Same inspected paper; central dedup/redirect pending. No extra G11 source ID. |
| Emily Short, *Dialogue Expressiveness in Mask of the Rose* | `GDR-SRC-20261010-W02-004` | Same dated canonical URL as W02. | Exact existing identity reused, not reallocated. |
| New G11 records 001–015 | `GDR-SRC-20261010-G11-001` through `015` | Canonical URLs/editions in full records below. | Unknown collisions outside inspected dependencies remain pending; no global allocation implied. |
| G11 leads 016–018 | `GDR-SRC-20261010-G11-016` through `018` | Access/lead records only. | Retain once within G11 if later inspected; do not restart numbering on retry. |

All G11 source numbers 001–018 are instantiated records, not a reserved future range. No further number is allocated by this packet. Known aliases are recorded without deciding a permanent canonical winner. The informal use of W01 identities for the two papers is a within-packet reuse choice, not an authorized merge of earlier source registries.

## Consolidated claim ledger

The following reproduces the material claim ledger for each exact candidate identity so an independent reviewer can inspect the whole packet. Local C-numbers are scoped by the candidate, not global claim IDs. References below provide provenance, dates, versions, locators, access and independence. No formal-standard finding is asserted in G11; proposed requirements are not disguised as standards.

### GDR-CAND-20261010-G11-GEN-01
Artifact: [genres/interactive-fiction.md](../genres/interactive-fiction.md).
| Local claim | Wording | Class | Evidence / locator | Confidence, limits and unresolved issue |
|---|---|---|---|---|
| C-01 | Use a text-mediated contribution definition as a working boundary, not a universal market taxonomy. | inference | GDR-SRC-20261010-G11-001, “What is interactive fiction?”; G11 brief decision questions | Moderate for a useful routing distinction; low for any universal classification; experimental and multilingual range incomplete. |
| C-02 | Inform documents finite action grammar and distinct authored mistake/parser-error mechanisms. | observed-example | GDR-SRC-20261010-G11-002, §§17.1, 17.21, 18.35 | High for inspected text; runtime and user outcomes unverified. |
| C-03 | Ink’s inspected examples represent gathering branches and conditioning content on traversal. | observed-example | GDR-SRC-20261010-G11-003, Part 2 Weave and TURNS_SINCE | High for documentation, not branch quality or comprehension. |
| C-04 | The Dreamhold help separates command assistance, hints and system controls. | observed-example | GDR-SRC-20261010-G11-004, Commands, System Commands, Special Commands | High for the help artifact; unknown executable build and effects. |
| C-05 | Short-study agency comparisons do not establish equivalence between branch consequences and acknowledgment. | empirical-evidence | GDR-SRC-20261010-W01-02, PDF pp. 8–11; Tables 1–2 | Moderate for bounded reported results; low for replay or genre-wide transfer. |
| C-06 | Situationally different choices received bounded, scale-dependent agency evidence in a fixed-order story study. | empirical-evidence | GDR-SRC-20261010-W01-03, printed pp. 11–14; Tables 5–6 | Moderate for reported data; post-hoc refinement, retrospective ratings and sample constrain causal transfer. |
| C-07 | Separate contribution, retained consequence and interpretation; reconvergence is conditional on the actual promise. | inference | Reviewed D-01 Narrative structures §§Promise/action/persistence, Authored order; D-02 Recipe; C-05–06 | Moderate as an analysis; no claim of equal enjoyment or universal need for branches. |
| C-08 | Encountered text does not certify a player-formed hypothesis; Short reports distinguishing those cases. | practitioner-heuristic | GDR-SRC-20261010-W02-004, player-deduced facts and hypothesis-crafting passages | Moderate for creator account; effect and exact revised build unknown. |
| C-09 | Specify and evaluate the offered contribution while measuring attention, agency, comprehension and preference separately. | hypothesis | C-05–08; reviewed D-03 dialogue and D-08 decision-information distinctions | Low as an efficacy recommendation; independent outcomes and framing must be tested. |
| C-10 | Bounded parser repair should clarify rather than silently replace an intention; omit it where exact language is the challenge. | hypothesis | C-02; G11-PAT-01 recipe; illustrative archive and metrical counterexample | Moderate for logical consistency; low for access/experience benefits until tested. |
| C-11 | Rereading, changing a decision and cross-play knowledge need distinct scope contracts. | hypothesis | C-04; G11-PAT-02; reviewed D-01 discovery-versus-event-order distinction | Low for effects; scope separation is proposed, not a certified implementation. |
| C-12 | Text-first presentation still requires end-to-end access checks; historical IF report observations do not certify current builds. | inference | GDR-SRC-20261010-G11-005, Testing method and Further testing; reviewed D-04 and D-07 | Moderate for reported barriers in sampled settings; recommendations broader than direct observations. |
| C-13 | Preserve intentional language/cultural ambiguity while testing unintended recognition and access barriers in each locale. | hypothesis | C-02, C-12; reviewed D-03 utterance/interpretation distinction; synthetic counterexamples | Low; native-language grammar and culturally specific audience evidence missing. |
| C-14 | Transfer checks must distinguish a stable correct rule from a wrong strategy and retain accommodations. | inference | Reviewed D-05 corrected recipe and examples, lines 77–123; D-08 | Moderate for diagnostic logic; G11 tests not performed and no population learning effect claimed. |
| C-15 | The archive example specifies observable commitments and continuity obligations rather than a proved benefit. | hypothesis | Illustrative worked example; C-07, C-10–11 | Low; invented example, no production estimate or implementation. |
| C-16 | Future studies should protect consent and privacy and not diagnose identity or health from fictional choices. | hypothesis | Author-proposed ethical protocol, not source-derived efficacy or legal advice | Moderate as a precautionary proposal; project approval and research protocol still needed. |
| C-17 | The 2019 IFTF evaluation reported access barriers in two prepared games across heterogeneous volunteer settings. | empirical-evidence | GDR-SRC-20261010-G11-005, Sources for this report; Testing method; Further testing | Moderate for reported observations; not a controlled genre/platform ranking or current-version certification. |

### GDR-CAND-20261010-G11-GEN-02
Artifact: [genres/visual-novel.md](../genres/visual-novel.md).
| Local claim | Wording | Class | Evidence / locator | Confidence, limits and unresolved issue |
|---|---|---|---|---|
| C-01 | Use staged reading and visual presentation as a provisional VN boundary, independently of route count. | inference | GDR-SRC-20261010-G11-006 opening display comparison; GDR-SRC-20261010-G11-014 publisher description; comparison with IF candidate | Moderate as a routing aid; not a complete cultural history, formal taxonomy or prevalence claim. |
| C-02 | Ren’Py documents ADV/NVL presentation differences as interface conventions. | observed-example | GDR-SRC-20261010-G11-006, opening comparison and Menu Choices | High for documented distinction, not a complete classification or tested display effect. |
| C-03 | A specified planetarian publisher description calls the work a visual novel while excluding choice-based story branching. | observed-example | GDR-SRC-20261010-G11-014, product description and release fields | High for publisher artifact; executable and other editions unverified; no satisfaction claim. |
| C-04 | Review text, voice, image and advance behavior as a coordinated scene, not a universal pacing formula. | hypothesis | GDR-SRC-20261010-G11-010 Preferences; GDR-SRC-20261010-G11-013 Voice; illustrative fixed-performance counterexample | Moderate for identifying dependencies; low for comparative pacing or comprehension benefits. |
| C-05 | History, save/rollback and cross-play persistent data are documented as distinct facilities. | observed-example | GDR-SRC-20261010-G11-007 opening/HistoryEntry; GDR-SRC-20261010-G11-008 Rollback; GDR-SRC-20261010-G11-009 opening | High for documentation; project state invariants and native behavior untested. |
| C-06 | Mask of the Rose’s creator describes a constrained expressive repertoire and subsequent clarification/revision. | practitioner-heuristic | GDR-SRC-20261010-W02-004, personality/wardrobe and revised-system passages | Moderate for retrospective; benefits and precise build not independently verified. |
| C-07 | Scarlet Hollow’s creator reports early trait-expression mismatches and revisions; these do not establish universal trait-success rules. | practitioner-heuristic | GDR-SRC-20261010-G11-015, design rules and failure/patch paragraphs | Moderate for creator report; no replayed build or survey analysis here. |
| C-08 | Choose scene/route topology for the promised distinction rather than the number of branches. | inference | Reviewed D-01 Narrative structures, D-02 reconvergence; C-03 | Moderate as an analysis; shared experimental evidence not VN-specific efficacy. |
| C-09 | Audit role promise through performed response and measure attention, comprehension, agency and preference independently. | hypothesis | Reviewed D-03 dialogue, D-06 intent contract, D-08 decision design; C-06–07 | Low as an improvement claim; test participant interpretation rather than assume preference. |
| C-10 | Reader-control meaning should distinguish viewing from revising and avoid silent state changes. | hypothesis | C-05; G11-PAT-02 recipe and playtest | Moderate for logical scope consistency; low for experience benefits until tested. |
| C-11 | Displayed-before text is not necessarily the same context or a comprehended event; skip/replay need a declared policy. | hypothesis | C-05; reviewed D-01 discovery/persistence distinction; illustrative disputed-promise scene | Low for empirical effects; current implementation and comprehension unknown. |
| C-12 | Localization review should include the scene’s speech act, context and performance obligations, not only words. | hypothesis | GDR-SRC-20261010-G11-011 translation units/tips; reviewed D-03; C-04 | Low for measured outcomes; native-language and culturally specific production evidence incomplete. |
| C-13 | Validate the full reading/choice/recovery task through intended access routes without assuming modality equivalence. | hypothesis | GDR-SRC-20261010-G11-012 self-voicing/alt text; reviewed D-04, D-07, D-09 | Moderate as a diagnostic process; no current-build access certification or standards claim. |
| C-14 | Controlled comparisons must preserve outcome distinctions and test changed context, not just completion or dwell. | hypothesis | Author-designed tests; reviewed D-05 transfer discrimination, D-08 decision interpretation | Low until performed; order, language, familiarity and performance are confounds. |
| C-15 | The disputed-promise example illustrates proposed commitments and failure checks, not a validated design. | hypothesis | Worked example and hybrid counterexamples in this entry | Low; wholly illustrative, no code, voice recording or player result. |
| C-16 | Reader research and production need explicit consent, privacy and rights decisions, independent of research approval. | hypothesis | Author-proposed ethical/production safeguards; G11 authorization boundary | Moderate as a precaution; no legal assessment or implementation approval. |

### GDR-CAND-20261010-G11-PAT-01
Artifact: [patterns/intent-preserving-parser-repair.md](../patterns/intent-preserving-parser-repair.md).
| Local claim | Wording | Class | Evidence / locator | Confidence, limits and unresolved issue |
|---|---|---|---|---|
| C-01 | Inform provides documented grammar and error/mistake distinctions usable as design precedents. | observed-example | GDR-SRC-20261010-G11-002, §§17.1, 17.21, 18.35 | High for document content; no compiler/runtime or outcome test. |
| C-02 | A creator help artifact separates assistance and system controls from fictional actions. | observed-example | GDR-SRC-20261010-G11-004, Commands, System Commands, Special Commands | High for artifact; behavior and effectiveness unknown. |
| C-03 | Resolving reference uncertainty before commitment preserves the chosen action only if meaning and state boundaries are honored. | inference | C-01; recipe steps 1–6; reviewed D-06 distinction from accepted dialogue intent | Moderate for conditional logic; ambiguous semantic equivalence must be locally verified. |
| C-04 | Bounded contextual repair may reduce unintended effort while improving accurate recognition. | hypothesis | C-01–03; mechanism table and proposed playtest | Low for player benefit; no comparative trial of this recipe. |
| C-05 | Exact-word challenges, unknown intentions and secret-leaking repairs are stop conditions, not merely tuning issues. | hypothesis | Author’s constrained-language counterexample and information-contract analysis; reviewed D-08 | Moderate as scope reasoning; artistic and access tradeoffs require local review. |
| C-06 | Clarification and input research need explicit time, privacy and recovery policies. | hypothesis | Author-proposed recipe step 5 and study safeguards | Low for effect claims; no legal or ethics-board approval asserted. |
| C-07 | Test same-rule valid and invalid transfer cases and retain accommodations rather than certify repeated response. | inference | Reviewed D-05, corrected recipe/examples lines 77–123 | Moderate for diagnostic logic; no G11 learning result. |
| C-08 | The parcel and ritual examples and falsification rules are proposed applications only. | hypothesis | Worked examples; playtest section | Low; illustrative, not implemented or tested. |

### GDR-CAND-20261010-G11-PAT-02
Artifact: [patterns/state-safe-narrative-rereading.md](../patterns/state-safe-narrative-rereading.md).
| Local claim | Wording | Class | Evidence / locator | Confidence, limits and unresolved issue |
|---|---|---|---|---|
| C-01 | Ren’Py documents history and saved/rollback state as distinct facilities. | observed-example | GDR-SRC-20261010-G11-007 opening/HistoryEntry; GDR-SRC-20261010-G11-008 Saving and Loading, Rollback | High for the manual; runtime behavior in a project unverified. |
| C-02 | Persistent data has a scope distinct from a point in current play. | observed-example | GDR-SRC-20261010-G11-009 opening and examples | High for documentation; which facts persist is a project decision not made here. |
| C-03 | Text, skip, auto-forward and voice controls are separately documented facilities. | observed-example | GDR-SRC-20261010-G11-010 Preferences; GDR-SRC-20261010-G11-013 opening and replay functions | High for documented controls; exposure, compatibility and benefit untested. |
| C-04 | Translation and performance associations introduce context/re-entry obligations to inspect. | inference | GDR-SRC-20261010-G11-011 Translating Dialogue and language-change tips; GDR-SRC-20261010-G11-013 automatic/translated voice | Moderate for potential dependencies; no executed failure or universal behavior claimed. |
| C-05 | A return operation must be judged against its declared state scope rather than its label alone. | inference | C-01–04; operation matrix and stop conditions | Moderate for consistency reasoning; no implementation certification. |
| C-06 | Distinct scope contracts may improve accurate recovery and perceived control. | hypothesis | Mechanism table; C-05; proposed comparison | Low for effect; added controls may increase burden. |
| C-07 | Encounter history cannot establish comprehension or unchanged interpretive context. | inference | C-01; illustrative repeated-words case; reviewed D-01/D-03 knowledge and interpretation distinction | Moderate for logical non-equivalence; benefit of any novelty policy untested. |
| C-08 | The operation defaults, examples, alternatives and exclusions are proposed design contracts. | hypothesis | Recipe and illustrative letter/repeated-words cases | Low; no scene replay, state test or production estimate performed. |
| C-09 | Assess state integrity, reader prediction, comprehension and preference separately and reject scope violations. | hypothesis | Author-designed proposed playtest; reviewed D-05/D-08 discrimination principles | Low for efficacy; static consistency is necessary to the promise but not sufficient for enjoyment. |

## Contradictions and contested applications

These are **local G11 conflict keys**, not allocated permanent `CON-` register identities. They preserve unresolved distinctions and counterexamples; they do not imply a contradiction has been empirically resolved.

| Key / claims | Competing propositions | Is this a direct contradiction? | Current treatment, design consequence and evidence needed |
|---|---|---|---|
| G11-CON-01; IF C-05–09, VN C-08–09 | Local acknowledgment can matter; a promised later consequence must actually persist. | Not necessarily. The studies and promises concern different outcomes/horizons; nonsignificance does not establish equivalence. | Reject both universal branch-count and “feedback is enough” rules. Compare accurate expectations, actual persistence and replay interpretation. Owner: Worlds/Foundations with Genres. |
| G11-CON-02; IF C-10/C-13, PAT-01 C-04–05 | Repair reduces unintended input burden; linguistic resistance may be the intended activity. | Genuine conditional design conflict, not a pooled-effect disagreement. | Separate interface assistance from solving the language task. Include exact-word counterexamples and target-language intent checks. Owner: Genres with Presentation/Foundations. |
| G11-CON-03; IF C-11, VN C-10, PAT-02 C-05–09 | Return supports recovery; irreversible commitment can be a deliberate promise. | Only if viewing and revising are conflated. | Separate transcript, replay and choice change. Test reader predictions and implementation scope; do not impose universal undo. Owner: Foundations session systems with Worlds/Genres. |
| G11-CON-04; VN C-04/C-13, PAT-02 C-06–08 | Reader pace/control can support access; fixed timing can be part of composition. | Conditional aesthetic/access conflict, no optimum identified. | Preserve required facts, disclose restricted modes and test the intended experience; do not invent one text speed. Owner: Presentation with Genres. |
| G11-CON-05; IF C-08/C-12/C-13, VN C-11–13 | Accessible facts and recoverable evidence help access; explicit interpretations can remove a mystery or cultural ambiguity. | Facts and interpretation are not the same object. | Preserve uncertainty and ask for a player hypothesis only when the task calls for it. Test both access and interpretation. Owner: Worlds/Presentation with Genres. |
| G11-CON-06; IF C-01, VN C-01–03 | A VN may have no story branching; an IF definition emphasizes interactive contribution. | Overlapping genre usages, not proof that one label is wrong. | Maintain separate routing files; do not demote fixed sequences or collapse VN into illustrated IF. Seek broader cultural/history sources. Owner: Library Coordination and Genres. |

Creator-specific rules in Scarlet Hollow are not promoted to genre rules; reported revisions in Mask of the Rose are not a controlled validation. The original source meanings remain intact while the proposed applications are narrower.

## Coverage checkpoint and queued child work

File existence closes the bounded writing task, not heading coverage. Both genre entries contain their own researched/partial/gap matrices and discriminating tests. Broad deficiencies remain: original non-puzzle/hypertext range, multilingual parser behavior, VN-specific effect evidence, current build/performance inspection, culturally situated localization and accessibility, and selected reviewed later-wave dependencies.

**Two new patterns are included, reaching this packet’s cap.** Existing reconvergence, dialogue intent and cue-alternative patterns were reused by identity rather than counted as new G11 artifacts. Additional useful techniques are not silently discarded or expanded into this submission.

| Child proposal, no key allocated | Exact decision question | Evidence justification and distinctness | Dependencies, owner and next discriminating work |
|---|---|---|---|
| Trait-conditioned expressive repertoire | When does selecting a disposition expand coherent role expression, and when does it predetermine responses or falsely promise competence? | Short’s repertoire account and Howard-Arias’s reported trait mismatches justify investigation. This concerns selection of available expression, not PAT-01 input repair or W02’s post-selection speech-act contract. | Genres with Worlds/Character and Dialogue owners. Inspect actual revised builds and culturally varied role expectations; compare predicted repertoire, performed role and preference. Child key must be registered once before a future Send. |
| Context-preserving voice/text turn arbitration | How should voice, alternative speech, visible text, automatic advance and a pending choice share one narrative beat without losing required information or taking unrequested action? | Ren’Py Voice, Preferences, Self-Voicing and Translation facilities plus inspected P02 guidance identify a concrete interaction problem; they do not validate a scheduling recipe. This concerns live progression, not PAT-02 return-state semantics. | Presentation owner with Genres and Dialogue. Obtain selected localization/performance guidance, inspect actual voice/AT builds, compare pause/advance policies and separate access from pacing preference. Child key must be registered once before a future Send. |

Neither proposal is an artifact allocation, approval, reserved number range or queued automation. No `G11-C01` or other child key is created here. Library Coordination must check all pending registrations and assign each child key once if the work is authorized. A retry of this G11 capture must retain its existing IDs and source records rather than restart counters.

### Further coverage work that is not yet a named pattern

Native-language parser morphology/ambiguity, original experimental/hypertext cases, and culturally situated VN reading/role expectations need better primary coverage before additional technique claims. The educational study lead requires full inspection and population/outcome separation. Broader save/session/state concepts need their owner’s reviewed bytes rather than an extra generic G11 topic. These are gaps, not hidden new batch submissions.

## Proposed index rows — not committed

The index fields below are proposals for Library Coordination, not a modified `INDEX.md`. Source check is 2026-10-10, lifecycle draft, version 0.1.0, owner BH-GDR-Genres, replacement ID none, for every row. Coverage remains open and permanent IDs remain unassigned.

| Temporary stable identity / linked title | Kind / aliases | Problem and use-case tags / description | Related entries | Confidence and applicability limit |
|---|---|---|---|---|
| `GDR-CAND-20261010-G11-GEN-01` — [Interactive fiction](../genres/interactive-fiction.md) | Genre; text adventure, parser fiction, choice-based fiction, hypertext fiction | Text-interface, agency, interpretation, input repair, recoverability; choose the supported contribution and consequence contract. | G11-GEN-02, G11-PAT-01/02; W01-TOP-01, W02-TOP-01, F02-TOP-01, P01-TOP-03, P02-TOP-03; exact full IDs in front matter. | Moderate bounded documentation/empirical descriptions; applications low-confidence hypotheses. English/parser and short-story evidence skew. |
| `GDR-CAND-20261010-G11-GEN-02` — [Visual novel](../genres/visual-novel.md) | Genre; VN, visual narrative, kinetic presentation | Scenes, routes, role, performance, reader control, localization; separate reading/performance from story consequence. | G11-GEN-01, G11-PAT-02; W01-TOP-01, W02-TOP-01, F02-TOP-01, P01-TOP-03, P02-TOP-03; optional PAT-01 only for parser hybrids. | Stronger for documentary distinctions than player effects. No actual performance or representative native-language sample. |
| `GDR-CAND-20261010-G11-PAT-01` — [Intent-preserving parser repair](../patterns/intent-preserving-parser-repair.md) | Pattern; bounded command repair, clarify before committing | Recognition, ambiguity, recovery; preserve supported intention and information boundaries before execution. | G11-GEN-01/02; G11-PAT-02; W02-PAT-01, F01-PAT-01, F02-TOP-01. | Recipe unvalidated; not for exact-word challenges, unknown intention or secret-disclosing repair. |
| `GDR-CAND-20261010-G11-PAT-02` — [State-safe narrative rereading](../patterns/state-safe-narrative-rereading.md) | Pattern; history versus rollback, read-only narrative return, replay state contract | Rereading, current versus persistent state, skip/replay context; define and honor return scope. | G11-GEN-01/02, G11-PAT-01; W01-TOP-01, W02-TOP-01; session/localization/state-owner links pending. | Technical precedents, hypothesized player benefit. No engine/state/reader validation. |

Abbreviated related-entry cells are display shorthand only, not new IDs; the exact full identities are in the candidate front matter and dependency ledger. Do not resolve uninspected later entries or proposed owner links into fabricated canonical URLs.

## Author self-review

**Performed by the G11 drafting assistant on its own candidates. This is not independent review, a second research agent, an experiment, or human approval.** The review challenged the strongest recommendation: that clearer contribution and return contracts should be preferred.

**Strongest opposing argument.** A work can intentionally use opaque wording, constrained identity, irreversible decisions or paced performance. Explicit repair and state controls can remove uncertainty, flatten voice and increase interface burden. Technical correctness may improve while the artistic or reader goal worsens. Therefore “maximize clarity and control” would be an unsupported universal recommendation.

**Disposition.** The drafts narrow the proposal to the actual contribution/control contract, retain hidden fictional truth where intentional, separate information from interpretation, and give concrete exit conditions. They include fixed-sequence VN, exact-language puzzle, memory-centered mystery and fixed-performance counterexamples. The complete pattern recipes remain hypotheses even where a documented facility or a consistency requirement is well supported.

| Adversarial check | Issue identified | Treatment in these first-capture bytes | Remaining review burden |
|---|---|---|---|
| Equivalence inflation | Short narrative studies could be read as proof that feedback replaces branches. | Keep selection/design/analysis limits; no equivalence or cost-saving claim. | Independent reviewer verifies methods, tables and the narrow wording. |
| Genre collapse | Shared reading/state concepts could make VN an illustrated IF duplicate. | VN centers performed scenes, protagonist role, routes, pace and cultural localization; IF centers command/choice/language contribution. | Broader traditions and native-language sources still needed. |
| Feature-to-effect leap | Ren’Py facilities could be presented as proof of accessibility or comprehension. | Separate documentation observations from hypothetical application and tests; no runtime certification. | Actual build and representative-user work requires separate authorization. |
| Misclassified evidence | A historical access observation can be mixed with a design recommendation. | IF C-17 records reported empirical observations; C-12 is the conditional inference. | Review the bridge, not just the source count. |
| Duplication | New patterns could repackage reconvergence or dialogue intent. | Retain W01/W02 identities; distinguish pre-commitment parser repair and return-state scope. | Library Coordination checks all pending concepts, not just inspected files. |
| Source-count inflation | Multiple docs, mirrors and related papers could look like independent corroboration. | Document families, reused IDs, aliases and shared research lineage are explicit. | Pending cross-batch dedup outside inspected archive. |
| Unsupported cultural universals | English examples could imply universal VN/IF expectations. | Working definitions and audience possibilities, no demographic prevalence or universal settings. | Native-language and culturally situated production/player evidence open. |
| Counterexample quality | Several opposing cases are invented rather than observed. | Each is labeled illustrative; creator-reported failures and publisher boundary case remain distinct. | Additional directly inspectable negative cases would strengthen the packet. |
| Privacy and rights | Free-text intentions or source screenshots could be redistributed without approval. | No participant logs, source assets, game images, PDFs or screenshots in output; only paraphrase and links. | Publication and any future study still require their own approvals. |

No reviewer identity or approval date was fabricated to mark this self-review as Gate C completion. The self-review does not resolve all criticism; it narrows the recommendation and leaves the gaps visible.

## Local packaging checks and review gates

The exact-file static checks are recorded in the snapshot receipt: the required paths exist, YAML front matter parses, all four research IDs are unique and assigned as directed, versions/revisions/null approvals match, the two-pattern cap is respected, internal Markdown links resolve inside this output tree, declared direct source IDs have reference records, and exact file hashes are recorded. These checks inspect Markdown and file bytes only; no project or engine code was executed.

| Gate | G11 status | What this does and does not establish |
|---|---|---|
| Gate A — architecture/taxonomy | Original starter history retained; current dispatch supersedes old starter-only execution restriction. | Does not silently change pending starter decisions into a canonical taxonomy approval. |
| Gate B — bounded brief | G11 research execution authorized by this explicit dispatch and supplied identities. | Does not approve conclusions or allocate permanent IDs. |
| Gate C — evidence/content | Author draft and self-review complete; independent G11 review pending. | Parent review of dependencies is not independent review of these new artifacts. |
| Gate D — retrieval/packaging | Local static packaging checks only; see receipt. | No uploaded-host retrieval, alias routing, conflict selection, cold/blind reliability or adversarial host prompts executed for G11. Overall Gate D not passed. |
| Gate E — acceptance/release | Not passed; release not authorized. | No canonical acceptance, publication, repository write, engine adoption or Project-source upload. |

The ten starter host-test prompts remain a test design for G11, not ten performed tests. Previously reported audio host behaviors do not transfer certification to these files. All genre coverage stays open.

## Completed artifacts, evidence limits and next decision

Completed locally: the two assigned genre files, two justified pattern candidates, this exact lower-case review packet and a supplemental Markdown byte receipt. All original input and selected dependency files remain unchanged. No repository, Project source, Library record, engine, setting or external publication was changed.

No new Library upload receipt, canonical commit or distribution synchronization is asserted. Only the actual upstream materialization receipt and local output paths/hashes are recorded. Any automatic attachment handling by the conversation host is not represented as a reviewed Library version.

**Precise next decision:** an independent reviewer should inspect these exact bytes, the source locators and the six local conflicts, then return corrections or a scoped evidence/content assessment. Doug then decides whether to accept the reviewed candidates for the next applicable gate and whether to authorize either queued child investigation. Library Coordination must resolve source aliases, pending owner links and permanent identity mapping before any release. No repeated G11 submission, child-key allocation, implementation or publication follows automatically.

## Complete source registry

Access date for every record below: **2026-10-10**. “Observed example” refers to an inspected document or source artifact unless explicitly stated otherwise; no game executable was run. Source identities are temporary; global deduplication and permanent allocation remain pending.

### GDR-SRC-20261010-G11-001
**Interactive Fiction Technology Foundation (IFTF). Frequently Asked Questions About Interactive Fiction.** Publication/update: unknown. Publisher: IFTF.
**URL:** [Frequently Asked Questions About Interactive Fiction](https://iftechfoundation.org/frequently-asked-questions/).
**Edition/build:** Unversioned public page; snapshot checked 2026-10-10. **Locator:** “What is interactive fiction?”; parser and choice-based descriptions.
**Access:** `relevant-excerpt`. **Type:** Foundation terminology / explanatory primary artifact. **Limits/independence:** An organization’s broad usage, not a formal taxonomy or audience study. Advocacy about accessibility or comparative artistic value is not adopted.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-002
**Graham Nelson / Inform documentation project. Writing with Inform.** Publication/update: unknown. Publisher: Inform documentation project.
**URL:** [Writing with Inform](https://ganelson.github.io/inform-website/book/WI_17_1.html). [§17.21](https://ganelson.github.io/inform-website/book/WI_17_21.html); [§18.35](https://ganelson.github.io/inform-website/book/WI_18_35.html).
**Edition/build:** Author-hosted HTML edition; exact release/commit not stated in inspected pages. **Locator:** §17.1 Understand, including Xylan; §17.21 Understanding mistakes, including Query and Hot Glass Looks Like Cold Glass; §18.35 Printing a parser error, including WXPQ.
**Access:** `relevant-excerpt`. **Type:** Official authoring manual and worked source artifacts. **Limits/independence:** Grammar examples inspected as text, not compiled. Contextual repair does not establish multilingual natural-language understanding or player benefit. Sections belong to one manual, not independent corroboration.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-003
**inkle. Writing with Ink.** Publication/update: unknown. Publisher: inkle / public GitHub repository.
**URL:** [Writing with Ink](https://github.com/inkle/ink/blob/master/Documentation/WritingWithInk.md).
**Edition/build:** master as served; no immutable commit established. **Locator:** Part 2: Weave, “Gathers,” “Nested Flow,” labels and conditional options; Part 1 game queries, TURNS_SINCE.
**Access:** `relevant-excerpt`. **Type:** Official authoring documentation / source examples. **Limits/independence:** Examples were not executed. A flow-construction claim is not proof of semantic continuity, choice quality, or absence of test obligations. Unpinned technical snapshot.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-004
**Andrew Plotkin. The Dreamhold — Help.** Publication/update: unknown. Publisher: Author’s website.
**URL:** [The Dreamhold — Help](https://eblong.com/zarf/zweb/dreamhold/help.html).
**Edition/build:** Web help; game release/build/platform behavior not verified. **Locator:** Basics; Commands; System Commands; Special Commands; Strategy.
**Access:** `relevant-excerpt`. **Type:** Creator-written instructions for a named game. **Limits/independence:** Documentation only; no game play, transcript capture, or measured outcome. Save/restore/undo and hints describe different controls, not an automatic accessibility certification.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-005
**Jason McIntosh (primary author), IFTF Accessibility Testing Project committee. Accessibility Testing Report.** Publication/update: 2019; publication announcement 2019-06-12. Publisher: IFTF.
**URL:** [Accessibility Testing Report](https://accessibility.iftechfoundation.org/). [Publication announcement](https://blog.iftechfoundation.org/2019-06-12-iftfs-accessibility-testing-project-report.html).
**Edition/build:** 2019 public report; testing January–February 2019. **Locator:** Sources for this report; Testing method; Tester profile and recruitment; Offer hints and walkthroughs; Further testing with parser-game screen effects; Further testing with non-Latin Unicode characters.
**Access:** `relevant-excerpt`. **Type:** Original volunteer accessibility evaluation and committee recommendations. **Limits/independence:** 34 respondents; two specially prepared Inform/Twine games, heterogeneous self-selected environments. Recommendations also use committee expertise and APX, not a controlled estimate for all IF. Raw responses not reanalyzed; 2019 tool outcomes not a 2026 compatibility claim.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-006
**Ren'Py project. NVL-Mode Tutorial.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [NVL-Mode Tutorial](https://www.renpy.org/doc/html/nvl_mode.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Opening ADV/NVL comparison; “Getting Started”; “Menu Choices”.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Presentation modes in a particular engine, not exhaustive genre definitions. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-007
**Ren'Py project. Dialogue History.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Dialogue History](https://www.renpy.org/doc/html/history.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Opening description; HistoryEntry fields; rollback_identifier.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** History entries and rollback references are distinct; a history pane is not a complete record of all audiovisual context. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-008
**Ren'Py project. Saving, Loading, and Rollback.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Saving, Loading, and Rollback](https://www.renpy.org/doc/html/save_load_rollback.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** What is Saved; Saving and Loading; Rollback; Blocking Rollback; Fixing Rollback.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Engine-specific state and custom-screen constraints. Vendor judgments about blocking rollback are practitioner advice, not an effect experiment. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-009
**Ren'Py project. Persistent Data.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Persistent Data](https://www.renpy.org/doc/html/persistent.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Opening distinction from data tied to a game point; persistent data example; merging discussion.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Cross-play persistence is not the same scope as a story save. No project reset policy or implementation verified. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-010
**Ren'Py project. Screen Actions, Values, and Functions.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Screen Actions, Values, and Functions](https://www.renpy.org/doc/html/screen_actions.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Preferences: text speed; skip; after choices; auto-forward; wait for voice.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Preference facilities are documented, not proof that a shipped UI exposes them or that a particular speed is effective. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-011
**Ren'Py project. Translation.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Translation](https://www.renpy.org/doc/html/translation.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Primary and Alternate Languages; Translating Dialogue; translation units; tips concerning language changes.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Text, interface, style and image facilities do not prove equivalent cultural interpretation. Identifier stability and replayed translation-block effects require project-specific review. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-012
**Ren'Py project. Self-Voicing.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Self-Voicing](https://www.renpy.org/doc/html/self_voicing.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Opening behavior; clipboard and debug modes; alt text and translation discussion.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Documented assistive facilities are not universal platform or disability coverage. No self-voicing, screen-reader, or native/mobile run performed. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-013
**Ren'Py project. Voice.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Voice](https://www.renpy.org/doc/html/voice.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Opening voice statement behavior; voice tags; automatic voice; translated voice; voice replay functions.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Engine documentation, not audience evidence that voice improves comprehension or preference. Audio builds and delivery platforms untested. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-014
**PROTOTYPE (publisher-supplied description); Nintendo storefront. planetarian: The Reverie of a Little Planet & Snow Globe.** Publication/update: Release listed 2024-06-27; storefront update unknown. Publisher: Nintendo / PROTOTYPE.
**URL:** [planetarian: The Reverie of a Little Planet & Snow Globe](https://www.nintendo.com/us/store/products/planetarian-the-reverie-of-a-little-planet-and-snow-globe-switch/).
**Edition/build:** Nintendo Switch digital combined edition; installed build unknown. **Locator:** Product description naming visual novel; note excluding choice-based story branching; publisher and release-date fields.
**Access:** `relevant-excerpt`. **Type:** Publisher description in official storefront. **Limits/independence:** A primary artifact describing one edition, not directly observed gameplay. Marketing claims about immersion not adopted; not interchangeable with the original or other ports.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-015
**Tony Howard-Arias, co-founder of Black Tabby Games. Designing Scarlet Hollow’s trait-based roleplaying system.** Publication/update: 2021-01-13. Publisher: Black Tabby Games / Medium.
**URL:** [Designing Scarlet Hollow’s trait-based roleplaying system](https://blacktabbygames.medium.com/designing-scarlet-hollows-trait-based-roleplaying-system-24f2b4f4906).
**Edition/build:** Episode 1 development account; discusses a prior December patch; exact builds unknown. **Locator:** Opening trait-design rules; paragraph beginning “There were a few ways that we failed”; following patch account.
**Access:** `relevant-excerpt`. **Type:** Firsthand developer rationale and retrospective. **Limits/independence:** Developer-reported failures and revisions, not independently verified player effects. Distribution graphs and survey proportions not used. Historical counts differ within the account; no current trait-count claim.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-W01-02
**Matthew William Fendt; Brent Harrison; Stephen G. Ware; Rogelio E. Cardona-Rivera; David L. Roberts. Achieving the Illusion of Agency.** Publication/update: 2012. Publisher: ICIDS 2012 / Springer, LNCS 7648, pp. 114–125.
**URL:** [Achieving the Illusion of Agency](https://www.cs.uky.edu/~sgware/reading/papers/fendt2012achieving.pdf).
**Edition/build:** Author-hosted 12-page paper; DOI 10.1007/978-3-642-34851-8_11. **Locator:** PDF pp. 3–8 design/method; pp. 8–10 results; Tables 1–2 on PDF p. 9 visually inspected; pp. 10–11 discussion.
**Access:** `relevant-excerpt`. **Type:** Original empirical study. **Limits/independence:** Selected comparable branching subgroup, phased groups, demographic imbalance and short single-play context limit inference. Non-significance is not equivalence; no measured production savings. Reuses W01 identity; W02-002 is an existing duplicate identity pending coordination.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-W01-03
**Rogelio E. Cardona-Rivera; Justus Robertson; Stephen G. Ware; Brent Harrison; David L. Roberts; R. Michael Young. Foreseeing Meaningful Choices.** Publication/update: 2014-10-08. Publisher: AAAI / AIIDE 10(1), pp. 9–15.
**URL:** [Foreseeing Meaningful Choices](https://ojs.aaai.org/index.php/AIIDE/article/view/12716). [Full publisher PDF](https://ojs.aaai.org/index.php/AIIDE/article/download/12716/12564/16233).
**Edition/build:** Publisher paper; DOI 10.1609/aiide.v10i1.12716. **Locator:** Printed pp. 11–12 Method/Participants/Apparatus; p. 13 Tables 5–6 and Figure 2 visually inspected; p. 14 Limitations and Future Work.
**Access:** `relevant-excerpt`. **Type:** Original empirical study. **Limits/independence:** Fixed-order within-subject design, retrospective ratings, gaming-experienced sample and post-hoc analytical refinements limit generalization. Shares authors/research lineage with Fendt, but is a distinct dataset; W02-001 and F02-001 remain duplicate aliases pending coordination.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-W02-004
**Emily Short. Dialogue Expressiveness in Mask of the Rose.** Publication/update: 2023-11-22. Publisher: Emily Short’s Interactive Storytelling.
**URL:** [Dialogue Expressiveness in Mask of the Rose](https://emshort.blog/2023/11/22/dialogue-expressiveness-in-mask-of-the-rose/).
**Edition/build:** Retrospective describing launch and subsequently revised system; exact game build unknown. **Locator:** Opening description of wardrobe/personality-filtered dialogue; player encountered versus player-deduced facts; reported post-launch clarification/revision.
**Access:** `relevant-excerpt`. **Type:** Firsthand creative/practitioner account. **Limits/independence:** Reuse exact W02 identity. Text inspected; embedded game screenshots and executable not used as behavior evidence. Expressivity and agency goals are creator intent, not validated effect sizes.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-016
**Depression Quest creators (authorship not verified in this access). Depression Quest — original site.** Publication/update: unknown. Publisher: Original project site.
**URL:** [Depression Quest — original site](https://www.depressionquest.com/).
**Edition/build:** unknown. **Locator:** No usable page body retrieved.
**Access:** `lead-only`. **Type:** Attempted original game/site route. **Limits/independence:** Open returned 502. No mechanics, build, outcome, or health-effect claim admitted.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-017
**Key / Visual Arts. planetarian — original product route.** Publication/update: unknown. Publisher: Key / Visual Arts.
**URL:** [planetarian — original product route](https://key.visualarts.gr.jp/product/planetarian/).
**Edition/build:** unknown. **Locator:** No usable page body retrieved.
**Access:** `lead-only`. **Type:** Attempted native-language original product route. **Limits/independence:** Open returned an internal fetch error. G11-014 is a different inspected edition, not a substitute claim that this route was read.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-018
**Eny Kusumawati (search metadata only). Listening Comprehension: The impact of Subtitles typographical features on Game Visual Novel.** Publication/update: 2019 (search metadata only). Publisher: International Journal of Scientific Research and Management.
**URL:** [Listening Comprehension: The impact of Subtitles typographical features on Game Visual Novel](https://ijsrm.net/index.php/ijsrm/article/view/2181).
**Edition/build:** DOI 10.18535/ijsrm/v7i4.el03; full metadata not verified. **Locator:** Search result/abstract lead only.
**Access:** `lead-only`. **Type:** Educational study lead, not admitted evidence. **Limits/independence:** Full methods and results not inspected. Related 2020 vocabulary report may overlap; independence unresolved. No study result or classroom-to-entertainment transfer claimed.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the consolidated candidate claim ledgers; a lead-only source supports no substantive claim.

## Final checkpoint

**Artifacts:** four complete research drafts plus the review packet and byte receipt. **Evidence limits:** 18 inspected source records, three lead-only records, no executed games or participant tests; broader genre and cultural coverage remains open. **Gates:** independent C pending, D static-only, E not authorized. **Next decision:** independent exact-byte review, followed by Doug’s scoped acceptance/correction and child-work decision; coordination before any canonical mapping or release.

---
artifact_key: reviews/full-run-20261010-p04-integrity-receipt.md
kind: integrity-receipt
title: P04 — local byte integrity and document checks
version: 0.1.0
candidate_revision: initial-draft-1
status: draft
owner_project: BH-GDR-Presentation-and-Interaction
run_id: GDR-FULL-20261010
batch_id: P04
attempt_id: P04-authoring-01
updated: '2026-10-10'
evidence_checked: '2026-10-10'
source_ids: []
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial P04 packet; no prior batch replaced or resubmitted.
byte_hash_record: null
---

# P04 — local byte integrity and document checks

**Administrative draft, not a research release or independent review.** Run GDR-FULL-20261010; batch P04; attempt P04-authoring-01; session/dispatch date 2026-10-10. Author: the assistant that prepared the research. Version 0.1.0; initial-draft-1; approval fields null.

## Seal convention

Hashes below are SHA-256 over exact UTF-8 file bytes, not rendered Markdown or retrieved text snippets. Research-file hashes are also recorded in the [review packet](full-run-20261010-p04-review-packet.md). This receipt additionally hashes the final packet. **The receipt deliberately does not contain its own hash**, avoiding self-reference. All first-submission predecessor/supersession fields are null. Later corrections must retain conceptual IDs and record predecessor hashes and a new candidate revision.

## Final delivered payload fingerprints

| Path | Candidate identity or administrative key | Bytes | SHA-256 |
|---|---|---|---|
| `patterns/action-phase-and-interruption-contract.md` | `GDR-CAND-20261010-P04-PAT-02` | 23,275 | `580260c37316982e3f8588724fc065f5f317718e4d96b91a7961f81bf8a1f14f` |
| `patterns/role-preserving-style-variation.md` | `GDR-CAND-20261010-P04-PAT-01` | 20,511 | `909ab2c79d268bc091df81a7b9dd202383c800298bc9fa6a4f7422f11c8f107f` |
| `reviews/full-run-20261010-p04-review-packet.md` | `reviews/full-run-20261010-p04-review-packet.md` | 45,668 | `b8f9604987b785962537f42ba442f10e50a17b0bf1e14f29a9b2f75394b14334` |
| `topics/animation-and-performance.md` | `GDR-CAND-20261010-P04-TOP-02` | 46,831 | `8da243d9ba61f7a397101383d33181d01d2ec6e65c858fa35d225f1d14c2bd78` |
| `topics/art-direction.md` | `GDR-CAND-20261010-P04-TOP-01` | 40,616 | `046dae78732fb9b9ec7e0c4d44c432ad3cf11478f002c7717864584e2e19316d` |

All six delivered files, including this receipt, are Markdown. The research payload is exactly two topics and two patterns; packet and receipt are administrative. No earlier batch, source PDF/media, asset, code, engine project or archive is delivered in this directory.

## Retrieved reviewed archive

- Reported Library identity: `libfile_082dcf2646dc8191af243051d202f4a8`.
- Exact materialized backing: `file_00000000b0d881f7a51345657bda5287`.
- Name: `GD-Knowledge-waves-1-2-reviewed-drafts-2026-10-11.zip`.
- Actual size: **1,994,913 bytes**.
- Locally computed SHA-256: `4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931`.

No expected cumulative-archive hash was supplied; this is a measured local fingerprint, not external authentication. The enclosing archive’s own selection metadata dated 2026-10-11 UTC remains intact. The separately reported earlier first-wave ZIP was not fetched/rehashed in P04.

## Inspected/extracted dependency fingerprints

Paths are relative to the retrieved archive root. Thirty files were selectively extracted. All thirty retain their computed local fingerprints; the twenty-nine non-manifest payloads match their own path/hash rows in the enclosing `MANIFEST.md`. The manifest excludes itself. Hash matching establishes local byte identity, not evidence correctness, canonical authority or review of every statement.

| Archive-relative path | Bytes | SHA-256 |
|---|---|---|
| `SELECTION_RECEIPT.md` | 2,068 | `2ef7422518733e605e564128846f3784112048ba0e4c908f87d4d0ea966082aa` |
| `MANIFEST.md` | 28,234 | `4dd7afff9fbd23540eb68ffac89a278d60761d71c86231329606ddd9a16ec3e6` |
| `ENTRY_INVENTORY.md` | 8,730 | `7cc18d402b9399d8bce30b9b9456ec217e83de5edfbc114f93892c4c67e84a36` |
| `VERIFICATION.md` | 4,923 | `eb72853e5da06f21d8c38fc48e7c16ff891efe3249ebef4b7c8735e38140c68b` |
| `DEPENDENCIES_AND_GAPS.md` | 7,210 | `d1b42b5eb5f813fab5325adc2a6417942981a06a98c8524b4f8597c64dbcf91f` |
| `SOURCE_INVENTORY.md` | 25,991 | `5004d811465a8a28c8b666cb2698f334296ba4467ca8ad791092fffbb5c43130` |
| `corrections/P01/CORRECTION_RECEIPT.md` | 2,847 | `a233b5ecfefcbe70bd801e0c602d95387624ee9f182525ff970808258e818e88` |
| `corrections/P02/CORRECTION_RECEIPT.md` | 1,610 | `b59fa309bf8ee98fcd4dc29526da956079b14aad1339aec859f985c2916e2bc8` |
| `reviews/P02-independent-review.md` | 8,581 | `48bf346aec05d0394c24049822811f31fab7f91e27da77d42a18bd2f6a1169ba` |
| `corrections/F01/revision-receipt.json.md` | 1,677 | `dd1b0a3a54fb0cc4a0afed3217ef5e37b071207fbdad53d83e1cf652fe230009` |
| `corrections/F01/correction.diff.md` | 6,219 | `13dafc356d53a6e25300145fd0756e39f3f060d6c0a235040bf6fb3aeb39b50f` |
| `selected-drafts/topics/visual-communication.md` | 40,895 | `b8e23ae234041fa0893295fdd36457eb08e0e77a60cca4229b7a77f0f13844b7` |
| `selected-drafts/topics/interface-and-information.md` | 50,777 | `1381faf6c998295cd0b0472cf3905a28f87d9515d16bacb54ece423fe080595d` |
| `selected-drafts/topics/accessibility-and-inclusive-interaction.md` | 56,707 | `eab6276ce51dcea359cb599f24ffef603b6062a6d6f6badffa8c0e28a0e79d48` |
| `selected-drafts/topics/controls-and-input.md` | 36,475 | `b9235153ba8b742c6df47e9e23844d9ab5da82e4212ebd22f04e314f6ccce21b` |
| `selected-drafts/topics/feedback-and-game-feel.md` | 40,880 | `6cf571a87946b9b40470cce966862219906f495b50c0b1db04e1ad7677ca4415` |
| `selected-drafts/topics/multimodal-communication.md` | 41,893 | `f70cdda6a504b283b85bd1c565c10ef503d4aad7d9877c4b00707bb4f819bc2c` |
| `selected-drafts/topics/character-design.md` | 46,314 | `ae70b9c2253b3908e89890f149289947c0fa31b4aa7b3e490f8713aa785f6cc4` |
| `selected-drafts/topics/dialogue-and-voice.md` | 43,954 | `8ecccddc1b02b4e6cf7aa0f3346a1b9a310010fdb3f625d9c4fab120e3b2397e` |
| `selected-drafts/patterns/supported-attempt-and-transfer-check.md` | 32,244 | `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1` |
| `selected-drafts/patterns/redundant-critical-state-cues.md` | 33,582 | `6b560a8630dc9e7125dd17a7c8fc53918ca2852eb3efefce693fa9a67c52bca6` |
| `selected-drafts/patterns/fact-preserving-cue-alternatives.md` | 27,103 | `4fef0b813e6ae7caf6e36f0046fe4dc034b033c6c9f80cf7acb4285e2f762dd0` |
| `selected-drafts/patterns/recoverable-action-remapping.md` | 22,603 | `960e6ce66453ab73e1b860acc5fbd67f8c316228c5d4f76ae228e50403ee8094` |
| `starter-historical/RETRIEVAL_AND_DISTRIBUTION.md` | 4,975 | `e3198df922cec05882bafd2247a8be8cf7d169bdf88a6e36fa2394565448757b` |
| `starter-historical/COMPATIBILITY.md` | 3,080 | `aaad70b7564bbd612d2c74b4478c51598067e0d517d122f4bfe857af02f60041` |
| `starter-historical/MANIFEST.md` | 4,152 | `bdf6a2f2c37137c2f2d5a288ec28addab27a9e302a245b219352fd906c7dfe46` |
| `starter-historical/projects/library-coordination.md` | 2,953 | `5277aa631d49bcf31e93d52f1cff521c9efb17e25d605036d61c87c1c5cfcaa6` |
| `selected-drafts/patterns/legible-commitment-and-safe-exit.md` | 22,899 | `85cffbbdb25c968e9c00f8ab5b3a230c420f24f0b83e19fbff49648e217b425a` |
| `selected-drafts/patterns/bounded-action-grace.md` | 25,059 | `03e0819fc92f1e6fcfe87d84871d2cbb6de337d3bcd57e044e614cb3d2773f1c` |
| `selected-drafts/patterns/intent-and-response-contract.md` | 28,947 | `ce138cb90f55a5c6b7f7da5220a328f21ab3198902e5199eebf2ccdbfbf221bc` |

## Original mounted inputs preserved

These fifteen supplied files were not replaced or edited. Hashes were recorded before artifact generation and compared again during final validation. No repository or Project-source inventory operation occurred.

| Mounted basename | SHA-256 |
|---|---|
| `REGISTERS.md` | `da89900343409f2af6618cf4175edda19fa51e815a6d053328ffca10fa621704` |
| `RESEARCH_INSTRUCTIONS.md` | `8e8bd348421747831607b3bb50789eefad5c74940bd3a50fe2c02994cd95627f` |
| `TAXONOMY.md` | `1ffaed52e465aa3488fdfb80d4cf18bb227ba08a22f3845e5906d8c0ce4f0167` |
| `Pasted text(3).txt` | `58c42a95ce9e26a80476f15ab60c7e7052bf81e61bdc058bef9271fa25012f60` |
| `pattern.md` | `c7797f316d80d98c6661dbb37cad452071b5387853b0051e5403e34ef1eb0ac0` |
| `patterns__contextual-audio-anomaly__GDK-PAT-0001__draft-0.1.0.md` | `32f23ed5f1bfd4970bbfeb2da936aa7cd789f26a68634387abeaaf58156067c3` |
| `EVIDENCE_RULES.md` | `de909b927b8a45e696e3ad73a599ee6810b30b5a993c5d8a9b5544e6c96ec7dc` |
| `topics__audio-tension-and-ambience__GDK-TOP-0001__review-correction-1.md` | `0d71efa2562fbe9210dcfccfd0239223f38035c2d11356c20adb30fd97fff3f3` |
| `presentation-and-interaction.md` | `1f09b07c27018e75b256e0c783ecbd8e7347dcdf54b0293289a7811b8a1de7e7` |
| `INDEX.md` | `cf4787caff6e401d74d6a0b6e5b5653ca27c7aae1a5bca7a29084c81a1f499e5` |
| `pilots__audio-tension-and-ambience-review-packet__REV-02__draft-0.1.0.md` | `8fd205d5043227bb67b9052683f684cc9cbb713c8bd486cc1c258db4b32fc106` |
| `topic.md` | `59f1da1bcc5eb3dc69cda7d8323199a25a31cfe6323b035a31f869f70a4579dd` |
| `REVIEW_GATES.md` | `948449fddee123c970294f499d85a6b9d10057ac175c1367006ad3de7df7b8d9` |
| `genre.md` | `91dfe9221700865ffcb2a3f65e3972f6e7db750ad31f3d4c05c6d63a2e615bad` |
| `audio-tension-and-ambience.md` | `841b159d0b8e48e2b33b3a062288a06bb923b8d91f42203036111c12b5c77a5b` |

## Actual local checks

Final validator: local Python using PyYAML, MarkdownIt CommonMark/tables, explicit ID/claim checks, filesystem-relative link/heading resolution, and SHA-256 comparisons. It operated on the final delivered files. This is same-author, non-independent **document QA**, not source-result verification, game/engine testing or target-host evaluation.

| Executed check family | Final result | Scope |
|---|---|---|
| Exact inventory and file types | PASS | Six specified Markdown paths; no non-Markdown payload. |
| Front matter/lifecycle | PASS | Version 0.1.0; draft; initial-draft-1; required null approval/predecessor/supersession fields. |
| Identity and pattern cap | PASS | Four exact, unique P04 research IDs; exactly two pattern files in the packet. |
| Source namespaces/reference bindings | PASS | Fifteen distinct sources; twelve new P04 IDs and three reused P01 IDs; twenty-five standalone reference records. |
| Claim ledger/markers | PASS | Forty-five claims with allowed class, confidence and support/authority/unresolved fields; local marked claim references resolve. |
| Topic/pattern template sections | PASS | All required substantive sections present in the four research entries. |
| UTF-8 and Markdown parsing | PASS | All six files parse with CommonMark/table support. |
| Relative links and heading anchors | PASS | Local Markdown file/anchor links resolve; unbundled dependencies are explicitly not asserted as local links. |
| Aliases/relationships/genre boundary | PASS | Ten unique aliases; local owner/pattern relationships consistent; no genre artifacts. |
| Selected dependency bytes | PASS | Thirty extracted files unchanged; twenty-nine enclosing-manifest path/hash rows match. |
| Original mounted inputs | PASS | All fifteen supplied originals retain their recorded hashes. |
| Research hash inventory | PASS | Four research identities/hashes agree with the exact lower-case review packet. |
| Gate/child boundary recording | PASS | Independent review unperformed; host cases unrun; child keys locally queued only; no release inferred. |
| Assembly/template placeholders | PASS | No unfilled assembly or template markers remain after sealing. |

The first assembly pass correctly flagged the temporary QA/receipt markers; both were filled before the final rerun. No substantive research claim was altered to satisfy a parser. Presence/consistency checks cannot establish the truth of a claim or the usability of a pattern.

## Not run and not approved

No P04 independent evidence review, participant recruitment, art/motion generation, prototype, engine code, network trace, performance benchmark, game/footage observation, cold/blind host test, canonical allocation, acceptance, publication or release occurred. The ten Gate D cases in the packet are prepared prompts only. Previous audio/parent reviews do not pass P04 gates.

The child keys P04-C01 and P04-C02 are locally queued records, not a central recovery-ledger registration receipt. No new Library receipt or Project upload was created for these outputs; conversation download artifacts are not synchronization. Coordination must verify identities, pattern boundaries, sources and queue keys against its current records before integration or further dispatch.

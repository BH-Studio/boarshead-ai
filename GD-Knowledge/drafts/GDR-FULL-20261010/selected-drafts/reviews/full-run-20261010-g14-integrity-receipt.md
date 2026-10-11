---
kind: integrity-receipt
run_id: GDR-FULL-20261010
batch_id: G14
version: 0.1.0
status: draft
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed
updated: '2026-10-10'
---

# G14 integrity and static-validation receipt

**Execution time:** 2026-10-11T05:00:50+00:00. **Executor:** the authoring assistant’s local artifact-validation script. **Scope:** local Markdown structure, identities, digests, source-record resolution and links. This is not independent evidence review, a Project-host retrieval test, a participant test, engine execution or release approval.

**Observed result:** 12/12 checks passed. Five candidate claim ledgers contain 55 material claim rows; source records comprise 12 used primary records and two excluded abstract-only leads. These counts do not establish comprehensive research or independent corroboration.

## Delivered artifact digests

The review packet and candidate hashes below identify the exact bytes checked. This receipt intentionally has no self-embedded digest. It records no canonical commit or Library upload receipt.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| [genres/immersive-simulation.md](../genres/immersive-simulation.md) | 27,042 | `29bec2f6d613aec6a677874fda3cad47f0b391645c77669291c69569e079adec` |
| [genres/stealth.md](../genres/stealth.md) | 30,064 | `2f18a0b514cf717a5c86f87688dfb822050d63a81b502151ec2ad878e23f26c2` |
| [genres/survival.md](../genres/survival.md) | 28,311 | `10ccc276ee966745172fd8732adb17bd5a29ce13d617605763a103d053a4ed82` |
| [patterns/evidence-bounded-search-and-reacquisition.md](../patterns/evidence-bounded-search-and-reacquisition.md) | 21,415 | `8f572bf92ac157488c045f16cc25d0e0026c8b870cc8a46d43c93f04c32f87d3` |
| [patterns/expedition-return-reserve.md](../patterns/expedition-return-reserve.md) | 22,841 | `681a1110bb3fb2fb535881e465ee7e059dc56a03b9ed8b3063292c2d2d35726e` |
| [reviews/full-run-20261010-g14-review-packet.md](full-run-20261010-g14-review-packet.md) | 78,830 | `d0f25b039ad2e9f553afb5f100ac93cff224f138de8ecc61af7880a90817c8f4` |

## Executed local checks

| Check | Observed outcome | Scope / limitation |
|---|---|---|
| Exact assigned paths and identities | PASS | Three exact genre paths/IDs; two distinct pattern paths/IDs; no extra candidate. |
| Unique IDs and two-pattern cap | PASS | Five unique candidate IDs; two pattern candidates, cap respected. |
| Draft metadata and revision consistency | PASS | All five remain initial drafts, null review/approval, no predecessor or supersession. |
| Required complete-template sections | PASS | All required genre/pattern sections present; this is structural completeness, not evidence completeness. |
| Claim and source resolution | PASS | All scanned local C-nn markers resolve to per-entry rows; every listed G14 source has a complete local reference record. This does not verify the substantive completeness of the claim ledger. |
| Source namespace preserved | PASS | 001–014 used once in the batch registry, including two excluded abstract-only leads; no global source IDs allocated. |
| Exact lower-case review packet and inventory hashes | PASS | Packet has exact requested lower-case name and contains current candidate byte digests. |
| No unsupported status promotion | PASS | Coverage open; independent G14 review pending; host tests explicitly NOT RUN; PAT-02 overlap retained. |
| Selected dependency byte verification | PASS | Eleven used dependency hashes match selected inventory or supplied pilot hashes. |
| Mounted input immutability | PASS | All 12 mounted starter/template/dispatch input hashes unchanged. |
| Markdown-only output set | PASS | No ZIP, source images, PDF, JSON, executable or other non-Markdown delivered in the output directory. |
| Relative Markdown paths and anchors | PASS | 54 relative links resolve to actual output files/anchors; this is not a hosted retrieval test. |

## Input snapshots unchanged

All entries below were hashed before output authoring and checked again afterward. These are the mounted starter/context inputs; no claim of current canonical status follows from their filenames.

| Input | Bytes | SHA-256 |
|---|---:|---|
| `RESEARCH_INSTRUCTIONS.md` | 4,631 | `8e8bd348421747831607b3bb50789eefad5c74940bd3a50fe2c02994cd95627f` |
| `EVIDENCE_RULES.md` | 4,910 | `de909b927b8a45e696e3ad73a599ee6810b30b5a993c5d8a9b5544e6c96ec7dc` |
| `TAXONOMY.md` | 7,872 | `1ffaed52e465aa3488fdfb80d4cf18bb227ba08a22f3845e5906d8c0ce4f0167` |
| `INDEX.md` | 2,448 | `cf4787caff6e401d74d6a0b6e5b5653ca27c7aae1a5bca7a29084c81a1f499e5` |
| `REVIEW_GATES.md` | 3,863 | `948449fddee123c970294f499d85a6b9d10057ac175c1367006ad3de7df7b8d9` |
| `REGISTERS.md` | 2,565 | `da89900343409f2af6618cf4175edda19fa51e815a6d053328ffca10fa621704` |
| `genres.md` | 2,900 | `5b7a78ef9af6ac6ca07caa81a5d63d45f1aca4c3716f8d03a4c3d5c1f722cf81` |
| `genre.md` | 2,337 | `91dfe9221700865ffcb2a3f65e3972f6e7db750ad31f3d4c05c6d63a2e615bad` |
| `topic.md` | 2,300 | `59f1da1bcc5eb3dc69cda7d8323199a25a31cfe6323b035a31f869f70a4579dd` |
| `pattern.md` | 2,189 | `c7797f316d80d98c6661dbb37cad452071b5387853b0051e5403e34ef1eb0ac0` |
| `audio-tension-and-ambience.md` | 6,032 | `841b159d0b8e48e2b33b3a062288a06bb923b8d91f42203036111c12b5c77a5b` |
| `Pasted text(20261011-043232).txt` | 15,402 | `d5a8b6d6e271363e8b0346102bc863514b1c6b42cdb7958e67f010998a587fb0` |

## Relevant reviewed-input digests

The packet gives precise substantive inspection ranges and retained identities. This receipt verifies bytes only; it does not promote every paragraph in a hashed file to inspected evidence.

| Dependency | Archive-relative path | Bytes | SHA-256 |
|---|---|---:|---|
| DEP-TRANSFER | `selected-drafts/patterns/supported-attempt-and-transfer-check.md` | 32,244 | `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1` |
| DEP-OBJECTIVE | `selected-drafts/patterns/multi-route-objective-contract.md` | 27,456 | `2512fbee56b449df49c61ede24bd07ea9314084d8e75e7c6070ad58dc65c0702` |
| DEP-CUES | `selected-drafts/patterns/fact-preserving-cue-alternatives.md` | 27,103 | `4fef0b813e6ae7caf6e36f0046fe4dc034b033c6c9f80cf7acb4285e2f762dd0` |
| DEP-ACCESS | `selected-drafts/topics/accessibility-and-inclusive-interaction.md` | 56,707 | `eab6276ce51dcea359cb599f24ffef603b6062a6d6f6badffa8c0e28a0e79d48` |
| DEP-DECISION | `selected-drafts/topics/decision-design.md` | 33,529 | `2fe66a5bf914a9c3f4101e168cdfd344a26eeadbfea7c45d16a9f17cca33bc6c` |
| DEP-CHALLENGE | `selected-drafts/topics/challenge-and-difficulty.md` | 35,717 | `7a48dc96849938268b809723a07f6150927c104a2a120c35da08e34d13dc8ef1` |
| DEP-THREAT | `selected-drafts/patterns/configurable-threat-consequences.md` | 35,586 | `8a992ece2804100d13c5b7f02f0e19256b947735ed74afb6a24e2ccd42dd8996` |
| DEP-SURVIVAL-HORROR | `selected-drafts/genres/survival-horror.md` | 56,565 | `21cc06da45fc83d7444e915622f1fd235153f5ca8bbe9cf77ad02cda55cdb451` |
| DEP-PILOT-T | `dependencies/audio-pilot/reviewed-candidate/GD-Knowledge/topics/audio-tension-and-ambience.md` | 51,500 | `0d71efa2562fbe9210dcfccfd0239223f38035c2d11356c20adb30fd97fff3f3` |
| DEP-PILOT-P | `dependencies/audio-pilot/reviewed-candidate/GD-Knowledge/patterns/contextual-audio-anomaly.md` | 35,244 | `32f23ed5f1bfd4970bbfeb2da936aa7cd789f26a68634387abeaaf58156067c3` |
| DEP-OPPORTUNITY | `selected-drafts/patterns/visible-opportunity-cost-comparison.md` | 16,912 | `afb19a4a363fbef3d7478731f84520c500dad15858d42a8b38bc0446ae63648b` |

## Package metadata and correction receipts

| Input metadata / receipt | SHA-256 |
|---|---|
| `README.md` | `1a1b3f7fbff8fe4a8a494fab86b4a17b556cfb845bd0f93d88c6b559ad2a2183` |
| `SELECTION_RECEIPT.md` | `2ef7422518733e605e564128846f3784112048ba0e4c908f87d4d0ea966082aa` |
| `ENTRY_INVENTORY.md` | `7cc18d402b9399d8bce30b9b9456ec217e83de5edfbc114f93892c4c67e84a36` |
| `SOURCE_INVENTORY.md` | `5004d811465a8a28c8b666cb2698f334296ba4467ca8ad791092fffbb5c43130` |
| `corrections/F01/correction.diff.md` | `13dafc356d53a6e25300145fd0756e39f3f060d6c0a235040bf6fb3aeb39b50f` |
| `corrections/P01/CORRECTION_RECEIPT.md` | `a233b5ecfefcbe70bd801e0c602d95387624ee9f182525ff970808258e818e88` |
| `corrections/P02/CORRECTION_RECEIPT.md` | `b59fa309bf8ee98fcd4dc29526da956079b14aad1339aec859f985c2916e2bc8` |

## Validation history

An initial identifier scan falsely matched the substring C-20 inside GDR-SRC-20261010 source IDs. The local validation expression was narrowed to standalone claim markers and the checks were rerun. This was a validator correction during authoring, not an artifact identity change, engine/harness change or independent review.

## Checks not performed

No current commercial build was executed; no player test, end-to-end no-harm run, raw-data statistical reanalysis, independent G14 evidence review, blind host retrieval, cross-Project synchronization, canonical registry validation or release action was performed. Local link resolution does not establish flat-host routing or Library/Project availability. External pages were inspected through the recorded research route; this script did not attempt to crawl or certify their current links or content.

**Next decision:** independent Gate C review and shared-owner resolution of PAT-02/F02 overlap, followed by Doug’s explicit research decision. No queued child should be sent until its key is registered through coordination.

**Final link pass:** after this receipt was populated, all 60 relative file/anchor links across the seven delivered Markdown files resolved locally. No host retrieval was exercised.

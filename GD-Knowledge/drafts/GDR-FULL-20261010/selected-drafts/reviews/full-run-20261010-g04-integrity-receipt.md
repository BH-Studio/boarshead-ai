---
kind: integrity-receipt
title: G04 final byte and local validation receipt
version: 0.1.0
status: draft
run_id: GDR-FULL-20261010
batch_key: G04
attempt_id: G04-authoring-01
updated: '2026-10-10'
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
independent_review: not-performed-for-G04
---

# G04 integrity receipt

This is an administrative Markdown record of **actual local checks**, not a research release, independent review, live Project upload receipt, host-retrieval test or gameplay experiment. It covers final initial-capture-1 bytes. It deliberately excludes its own hash to avoid circular self-hashing.

## Final artifact fingerprints

| Exact path | Bytes | SHA-256 |
|---|---:|---|
| [genres/shooter.md](../genres/shooter.md) | 34992 | `c741aa6aa208cab7be7dca45f1547973cda8c95fbdaed25bea3ab6d447f001bf` |
| [genres/tactical-shooter.md](../genres/tactical-shooter.md) | 36782 | `7df6670c133fb37699f06790b8c90e75136db669f422c18a7a0831f831428cf8` |
| [genres/extraction-game.md](../genres/extraction-game.md) | 40017 | `786c17744e1df616c4abab24512f1d06346dba841b4a7dfc9cc9af39077461b1` |
| [patterns/provisional-versus-confirmed-impact-feedback.md](../patterns/provisional-versus-confirmed-impact-feedback.md) | 22670 | `aab57bb0498e7a0a671764ce009d042bcec1b90259fb7311baa1b0b999ce85ed` |
| [patterns/viable-baseline-re-entry-loadout.md](../patterns/viable-baseline-re-entry-loadout.md) | 25667 | `01fbcfce9f34fb0c10b69fcd82104cf1c3d36f832056af19cd4acec79b5ef9b7` |
| [reviews/full-run-20261010-g04-review-packet.md](../reviews/full-run-20261010-g04-review-packet.md) | 83987 | `f6148cc3c5e22a062da850cdb7884b61f9cafe984d51ac7898cffdf438a5f810` |

All five research candidates are `0.1.0`, `initial-capture-1`, `draft`, with `reviewer`, `approved_by`, `approved_date`, `predecessor_sha256` and `supersedes` null. The exact lower-case packet path was checked. No source files from earlier batches appear in the output tree.

## Local checks actually performed

| Check | Observed result | Scope / limit |
|---|---|---|
| Assigned candidate identity/path inventory | PASS — 3 genres and 2 patterns; five unique assigned IDs. | Temporary run IDs only; not canonical allocations. |
| YAML front matter and null approvals | PASS — 5 research candidates. | Basic schema/status checks, not complete library-schema certification. |
| Pattern workload cap | PASS — exactly 2 pattern files. | Queued extensions are not pattern submissions. |
| Claim inventory/classes | PASS — 56 local claim rows; valid classes; no duplicate local claim IDs. | Source accuracy received author review only; no independent approval. |
| Source identity and records | PASS — 17 unique source URLs/identities; 15 new G04 and 2 reused P02; 29 complete per-entry source records. | Global URL/DOI/edition dedup remains pending; URL uniqueness is not source independence. |
| Relative Markdown links/anchors | PASS — 88 local references checked before receipt finalization; receipt links rechecked afterward. | Only files in this local output set; not host routing or cold/blind retrieval. |
| Template-marker scan | PASS — no UNASSIGNED, date-template or replacement-title markers in candidates. | Semantic completeness still requires independent review. |
| Selected parent payload manifest | PASS — 57 selected/admin files matched archive-internal sizes/hashes. | Not full content inspection or external provenance attestation. |
| Candidate fingerprint generation | PASS — hashes computed from final UTF-8 bytes. | The review packet is hashed here; this receipt is intentionally not self-hashed. |
| Independent G04 review / host tests / gameplay tests | NOT RUN. | No simulated pass result, inherited audio gate or independent reviewer claimed. |
| Repository / Project / Library writes | NONE. | Only local working copies and new Markdown outputs were written. |

## Input snapshot fingerprints

The starter documents remain the supplied snapshots, not the latest canonical library. These hashes were measured from actual bytes. Original sources were not overwritten.

| Input | Bytes | SHA-256 |
|---|---:|---|
| `Pasted text(2).txt` | 15297 | `f8eada45bf1027f5edf1b6f69c48854ee55da7b85a75ea0a6bef576c82fa6b1e` |
| `RESEARCH_INSTRUCTIONS.md` | 4631 | `8e8bd348421747831607b3bb50789eefad5c74940bd3a50fe2c02994cd95627f` |
| `EVIDENCE_RULES.md` | 4910 | `de909b927b8a45e696e3ad73a599ee6810b30b5a993c5d8a9b5544e6c96ec7dc` |
| `REVIEW_GATES.md` | 3863 | `948449fddee123c970294f499d85a6b9d10057ac175c1367006ad3de7df7b8d9` |
| `INDEX.md` | 2448 | `cf4787caff6e401d74d6a0b6e5b5653ca27c7aae1a5bca7a29084c81a1f499e5` |
| `TAXONOMY.md` | 7872 | `1ffaed52e465aa3488fdfb80d4cf18bb227ba08a22f3845e5906d8c0ce4f0167` |
| `REGISTERS.md` | 2565 | `da89900343409f2af6618cf4175edda19fa51e815a6d053328ffca10fa621704` |
| `genres.md` | 2900 | `5b7a78ef9af6ac6ca07caa81a5d63d45f1aca4c3716f8d03a4c3d5c1f722cf81` |
| `genre.md` | 2337 | `91dfe9221700865ffcb2a3f65e3972f6e7db750ad31f3d4c05c6d63a2e615bad` |
| `topic.md` | 2300 | `59f1da1bcc5eb3dc69cda7d8323199a25a31cfe6323b035a31f869f70a4579dd` |
| `pattern.md` | 2189 | `c7797f316d80d98c6661dbb37cad452071b5387853b0051e5403e34ef1eb0ac0` |
| `audio-tension-and-ambience.md` | 6032 | `841b159d0b8e48e2b33b3a062288a06bb923b8d91f42203036111c12b5c77a5b` |
| `GD-Knowledge-waves-1-2-reviewed-drafts-2026-10-11.zip` | 1994913 | `4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931` |

## Receipt boundaries and recovery

Library input identity supplied by the dispatch: `libfile_082dcf2646dc8191af243051d202f4a8`; backing file `file_00000000b0d881f7a51345657bda5287`. Raw materialization returned the expected name/size and no version ID. The archive hash above is locally measured; no expected cumulative parent hash was available. No new Library upload or Project attachment receipt exists.

On retry, preserve the five candidate IDs, attempt history and source mappings. On a submitted revision, retain the candidate IDs and record a new candidate revision, exact predecessor hash and supersession relationship. Do not duplicate the initial submission or restart source counters. Locally queued proposed child keys are in the [review packet](full-run-20261010-g04-review-packet.md#two-pattern-cap-and-locally-registered-child-work-queue); central registration is not assumed.

**Gate status:** author self-review recorded; independent Gate C review pending; Gate D limited to the local checks above; no release or implementation approval. **Next decision:** review the actual candidate bytes, reconcile source/owner/identity and child-queue questions, and conduct separately authorized host packaging checks before considering release.

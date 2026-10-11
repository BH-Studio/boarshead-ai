---
id: null
kind: integrity-receipt
run: GDR-FULL-20261010
batch: G19
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
attempt_identity: G19-authoring-01
predecessor_sha256: null
supersedes: null
owner_project: BH-GDR-Genres
updated: '2026-10-11'
reviewer: null
approved_by: null
approved_date: null
---

# G19 integrity receipt

## Scope and identity

Local UTF-8 Markdown authoring/packaging check, 2026-10-11 UTC (2026-10-10 America/Los_Angeles). This receipt identifies the five G19 candidates and the exact lower-case review packet. It is not a research candidate, Library upload, Project snapshot, repository commit, independent evidence review, player test, or release approval.

All candidates remain 0.1.0 draft, revision `initial-draft-1`, with null reviewer/approval/predecessor/supersession fields. This is the initial submitted G19 capture. Future corrections retain their IDs and require an explicit new revision plus predecessor fingerprint; these hashes must not be silently treated as identifying revised bytes.

## Exact output fingerprints

SHA-256 values are computed from each complete file’s final bytes. The receipt deliberately does not contain a hash of itself; no circular or placeholder self-hash is claimed. Its own byte hash may be quoted externally in the handoff.

| File | Bytes | SHA-256 |
| --- | --- | --- |
| [genres/rhythm.md](../genres/rhythm.md) | 38657 | `acbc4824c946488ed4b887f3834b78d65b630e5717afbc5c951fa1f01ac7b8ad` |
| [genres/party.md](../genres/party.md) | 40869 | `2cae024e4fbbba240381de33d005badc19312a4441dbee2e04551cbd7e8c09eb` |
| [genres/social-deduction.md](../genres/social-deduction.md) | 39809 | `5b1294bea5cff7863da016e6555a5d562b2e28ce8cc63b0d2fb833f427bb48b3` |
| [patterns/calibration-challenge-separation.md](../patterns/calibration-challenge-separation.md) | 25126 | `5b1c2d5344054b0897b94972c55c70a1de7892e6b22a4bf2a193e6511318de53` |
| [patterns/post-elimination-participation-contract.md](../patterns/post-elimination-participation-contract.md) | 26780 | `2f282473962631de8a6e2a0e4a12263bbb23d289d6870e48a4277bdd2b704f1f` |
| [reviews/full-run-20261010-g19-review-packet.md](full-run-20261010-g19-review-packet.md) | 89750 | `0e8c9095d74b6ba6cb6822a868f0667c77ec105c2569802b7184fb328de22a76` |

## Performed local checks

The following are actual local static checks of this delivery, not evidence of gameplay efficacy or a Project-host Gate D pass. External source URLs were inspected during research but not re-fetched en masse by this sealing script. The script validates local paths/anchors, not remote availability or the truth of every source claim.

| Check group | Observed outcome |
| --- | --- |
| Inventory and identity | PASS: three genre candidates, two pattern candidates, one review packet and one integrity receipt; five distinct fixed candidate IDs. |
| Front matter and lifecycle | PASS: version, draft status, initial revision, null approvals/predecessors/supersession and coverage-open fields retained. |
| Sources and claim routes | PASS: candidate source declarations match their reference headings; source namespace contains 001–022 once per reference list; near-claim keys exist in their local ledgers. |
| Evidence-access counts | PASS: 18 substantive inspected sources and four lead/abstract/overview-only records; the latter are not counted as supporting result evidence. |
| Expected content sections | PASS: genre and pattern required sections are present; no template replacement prompts, TODO/TBD or unassigned candidate IDs remain. |
| Candidate/review fingerprints | PASS: candidate SHA-256 values match the review packet; all six content files are hashed above. |
| Local links/anchors | PASS: 42 relative Markdown link/anchor occurrences resolve in the delivered seven-file tree. |
| Inspected dependency hashes | PASS: 11 selected dependency files match their inspected selected inventory identities; no original author predecessor is substituted. |
| Mounted input preservation | PASS: all 12 input fingerprints match at the beginning and end of this sealing/check interval; no input-writing operation was issued. |
| Encoding and payload | PASS: UTF-8-readable Markdown only; balanced fenced-code delimiters; seven files and no external source copies. |

These checks inspect structure and byte identity; they do not certify all Markdown rendering, exhaustive semantic correctness, global source deduplication, canonical ownership or any causal recommendation. The source/claim check is a reference-integrity check, not an independent source audit.

## Dependency download receipt

The named waves 1–2 ZIP was actually materialized from Library `libfile_082dcf2646dc8191af243051d202f4a8`, backing `file_00000000b0d881f7a51345657bda5287`. Returned size: 1,994,913 bytes. Computed SHA-256: `4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931`. The size matches the dispatch; no expected ZIP hash was supplied for an external fingerprint comparison. Selected member hashes were compared with the inspected ENTRY_INVENTORY. The archive and selected dependencies are not reissued as G19 artifacts.

## Gates and unperformed work

G19 author self-review is complete but is not independent review. Gate C remains pending independent review; actual uploaded-snapshot Gate D retrieval prompts are NOT RUN; Gate E/release is not passed or authorized. No player tests, prototypes, instrumented game/device runs or implementation occurred. No repository/Project-source/settings/account changes, purchases, permanent allocations or publication occurred.

No new Library upload or Project synchronization receipt exists for these outputs; the files are downloadable conversation artifacts only. No background work, child dispatch or release is scheduled. Next: the parent independent reviewer inspects these exact candidate/packet bytes and requests corrections or advances the bounded research review; Coordination separately resolves IDs/overlaps and the two queued child proposals.

---
kind: integrity-receipt
title: G18 draft integrity receipt
run_id: GDR-FULL-20261010
batch_id: G18
version: 0.1.0
status: draft
candidate_revision: initial-author-draft-1
generated_utc: '2026-10-11T05:02:18+00:00'
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
independent_review: not-performed
project_host_tests: not-run
player_tests: not-run
---

# G18 draft integrity receipt

Sealed in the local working container at **2026-10-11T05:02:18+00:00**. These are byte/static checks of the delivered draft tree, not evidence validation, independent content review, Project-host testing or release. The run identifier retains the dispatch date 2026-10-10; UTC source inspection occurred 2026-10-11.

## Exact delivered research and packet bytes

| Relative path | Candidate identity / supporting role | Bytes | SHA-256 |
|---|---|---:|---|
| [genres/racing.md](../genres/racing.md) | `GDR-CAND-20261010-G18-GEN-01` | 43,336 | `389d2145a297785bb3ddc6e16da3ff8a357657d147c66ed2f297dff2ef17a78f` |
| [genres/sports.md](../genres/sports.md) | `GDR-CAND-20261010-G18-GEN-02` | 47,002 | `ee254d7b5cd15b4b7a32b6148c5d606816af86d91792c0ad262e18c260f1c7c4` |
| [patterns/versioned-performance-comparison.md](../patterns/versioned-performance-comparison.md) | `GDR-CAND-20261010-G18-PAT-01` | 27,265 | `9d15e9f67bdf938bd8d0df6e51fd299dc75c0dd3fc3fc595add7dba481efd211` |
| [reviews/full-run-20261010-g18-review-packet.md](full-run-20261010-g18-review-packet.md) | `Supporting review packet; no new conceptual ID` | 74,410 | `56c501ccf15376569664b5a7fe7e424aac549f6d77f73947acc5c609081d43c0` |

The fifth delivered Markdown file is **`reviews/full-run-20261010-g18-integrity-receipt.md`**, this receipt. It deliberately does not embed its own checksum: such a self-hash would change the bytes being hashed. Its exact SHA-256 may be recorded externally at handoff. No ZIP, source article, executable, image, JSON or repository change is part of the delivered artifact tree.

## Checks actually executed

| Check | Observed result | Scope limitation |
|---|---|---|
| Five-file output inventory | PASS — two genre candidates, one pattern, one exact lower-case review packet, one receipt; all Markdown. | No old research candidate is bundled or resubmitted. |
| Candidate IDs and lifecycle | PASS — three exact unique assigned temporary IDs; version 0.1.0; draft; initial-author-draft-1; null reviewer/approval/predecessor/supersession fields. | Identity correctness is not canonical allocation or independent approval. |
| Pattern workload | PASS — one new pattern, within the zero-to-two packet cap. | Other technique questions remain queued without child keys or dispatch. |
| Candidate inventory hashes | PASS — all three candidate byte hashes in the review packet agree with actual files. | This receipt additionally supplies the exact review-packet hash. |
| Claim ledgers | PASS — 14 racing, 16 sports and 5 pattern local claim records; all referenced local claim handles resolve. | Grouping and source interpretation still require independent semantic review. |
| Source identity/references | PASS — 20 exact G18 registry IDs; five standalone racing, eight sports and four pattern reference records; every used full G18 source ID in a candidate is declared and defined. | 12 supporting primary works/artifacts; eight non-supporting leads. No claim that all were fully readable or independent. |
| Internal Markdown links/anchors | PASS — 51 link/anchor occurrences in the final five-file tree resolve under the local Markdown-heading check. | No browser rendering or actual Project-host retrieval was exercised. |
| Encoding and template fill | PASS — UTF-8 parses; no replacement character, unassigned template ID, generic replacement title or unfinished-work marker detected. | Open questions and missing dependencies are intentional disclosures, not completed evidence. |
| Reviewed archive bytes | PASS — 1,994,913 bytes; SHA-256 4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931; no CRC failure. | Materialized from the supplied backing ID; Library version was not supplied. |
| Reviewed selected inventory | PASS — 38 inventory hashes match: 19 topics, 5 genres, 14 patterns across nine batches. | Only ten relevant selected candidates received semantic dependency inspection; no full review of the other entries is claimed. |
| Input preservation | PASS — source inputs are only read by the artifact builder; their exact hashes remain recorded in the packet. | No repository, Library upload, Project-source replacement or settings operation was performed. |
| Independent review / host / gameplay | NOT RUN for G18. | All proposed participant/prototype tests remain proposed. Overall Gate D and Gate E are not certified. |

## Reproduction and handoff limits

Checks were performed with local text parsing, Markdown-link/heading resolution, SHA-256 computation and ZIP CRC/inventory comparison. They do not validate the factual truth of every sentence, the external sources’ methods, link accessibility in another host, game fairness, player experience or implementation. The local source IDs retain original provenance and cross-batch deduplication remains pending.

This packet is **author-draft complete, coverage-open and unreleased**. The exact next step is parent capture of these bytes and independent G18 evidence/content review. Library Coordination must resolve concept ownership, potential duplicates and any future child registration before canonical IDs or further dispatch. Acceptance of research would still not authorize implementation, publication, Project-source changes or release automatically.

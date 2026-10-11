---
kind: snapshot-receipt
title: G11 local Markdown snapshot verification
run_id: GDR-FULL-20261010
batch_key: G11
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
updated: '2026-10-10'
reviewer: null
approved_by: null
approved_date: null
library_upload_receipt: null
canonical_commit: null
independent_review: not-performed-for-G11
receipt_self_hash: not embedded; no recursive self-hash
---

# G11 local snapshot receipt

This is a **local byte and Markdown-structure record**, not independent evidence review, a Library upload receipt, canonical acceptance, release approval or a player-test result. All five files identified below are version 0.1.0 draft, candidate_revision initial-draft-1. The four research candidates retain their assigned run-scoped identities and null reviewer/approval metadata. This receipt is not another research candidate.

## Exact output bytes

Hashes were computed from the final UTF-8 files, not inferred from titles or search metadata. The review packet holds the four candidate hashes; this receipt additionally supplies the packet hash. This receipt intentionally does not hash itself.

| Artifact | Identity / role | Bytes | SHA-256 |
|---|---|---:|---|
| [genres/interactive-fiction.md](../genres/interactive-fiction.md) | `GDR-CAND-20261010-G11-GEN-01` | 46772 | `660b913d608b48ed03b93793bd9460c68e2ba495428d14bce168981c088ae3a9` |
| [genres/visual-novel.md](../genres/visual-novel.md) | `GDR-CAND-20261010-G11-GEN-02` | 49142 | `7765e5200300b627a23ebfd8b4190bdd6bc4efb1fae1d69a2cc5a2ce6a536919` |
| [patterns/intent-preserving-parser-repair.md](../patterns/intent-preserving-parser-repair.md) | `GDR-CAND-20261010-G11-PAT-01` | 21850 | `a663a95f3112a931b0b91e8432eae80ba46449dc14496bd04f74f68bb52e4eba` |
| [patterns/state-safe-narrative-rereading.md](../patterns/state-safe-narrative-rereading.md) | `GDR-CAND-20261010-G11-PAT-02` | 27288 | `2b0a9ea3032d9c12be0cdb4b97d52e04778da7614dd257aad28ad92bf0fa3159` |
| [reviews/full-run-20261010-g11-review-packet.md](full-run-20261010-g11-review-packet.md) | `G11 review packet; no research ID allocated` | 79467 | `e6dbb4ad458a6a5073de5962910aa29a3e7dfe07e810ea53e6619a73da59905b` |

## Executed local checks

Only local file authoring and static inspection utilities were executed. No project, game, engine or participant-test code was run. The Markdown checks do not execute host retrieval prompts or prove research conclusions.

| Check | Local result | Boundary |
|---|---|---|
| Required artifact names and output set | Checked: two genres, two patterns, exact lower-case review packet and this receipt. | No earlier batch or dependency artifact resubmitted. |
| Candidate metadata and identity | Checked: all four unique assigned IDs, 0.1.0, draft, initial-draft-1, null approval/reviewer/predecessor fields. | No permanent identity or global collision check certified. |
| Source references and local claims | Checked: declared direct sources have reference records; local C-markers resolve to ledgers. | Does not independently validate source interpretation or every inferential step. |
| Internal Markdown paths and fragments | Checked against actual package files and headings. | Links to this provenance packet do not materialize external shared candidates; no flat-host routing test. |
| Table structure and file encoding | Checked: consistent pipe-column counts and UTF-8-readable Markdown. | Not a rendered platform/accessibility test. |
| SHA-256 | Checked: candidate hashes agree with the packet; packet hash is recorded above. | Not a release receipt, server upload identity or synchronized repository commit. |
| Output types | Checked: only the intended Markdown files occur in the output tree. | Working scripts and input copies are not deliverables. |

## Input and review status

The cumulative upstream archive was materialized as `file_00000000b0d881f7a51345657bda5287` from Library `libfile_082dcf2646dc8191af243051d202f4a8`, 1,994,913 bytes, SHA-256 `4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931`. Relevant selected dependency bytes were inspected. The review packet contains each input/dependency hash, passage scope and preserved revision identity. No new Library version or upload is asserted.

**Gate C:** independent G11 review pending. **Gate D:** local static checks only; actual uploaded-host, cold/blind and adversarial retrieval tests not performed. **Gate E:** not passed and release not authorized. Both genre headings remain coverage-open; the complete recipes remain unvalidated hypotheses.

**Next decision:** independent exact-byte evidence/content review, then Doug’s scoped correction/acceptance and queued-child-work decision. No repository, Project-source, engine, settings, publication or canonical-index change follows from this receipt.

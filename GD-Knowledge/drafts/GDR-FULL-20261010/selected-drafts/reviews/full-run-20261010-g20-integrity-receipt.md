---
kind: integrity-receipt
title: G20 local artifact integrity receipt
run_id: GDR-FULL-20261010
batch_id: G20
version: 0.1.0
status: draft
candidate_revision: initial-capture-1
created_utc: '2026-10-11T05:00:22+00:00'
reviewer: null
approved_by: null
approved_date: null
---

# G20 local artifact integrity receipt

This records final local bytes for the four research candidates and exact lower-case review packet. It is not a Library upload, Project-source receipt, repository commit, independent review, canonical allocation or release. All research candidates are 0.1.0 draft, initial-capture-1, with no predecessor/supersession and null reviewer/approval metadata.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| [genres/cozy-game.md](../genres/cozy-game.md) | 26612 | `3a5d62c27a0048827c23d88ca7219e307b5b0a741b043e3b3effd88fc0c828ca` |
| [genres/educational-game.md](../genres/educational-game.md) | 28052 | `0c313226fce31db796fbb8826f478c638bdc205a41c441ddd65ef8f894867f00` |
| [genres/idle-incremental.md](../genres/idle-incremental.md) | 28040 | `41a1e6eb996d10a3c0f4202cb6d5f77aa79be8f96b10f9b5ab5bd787f818a0bd` |
| [patterns/away-state-reconciliation.md](../patterns/away-state-reconciliation.md) | 21183 | `373fd465d06b6b8d1febc90f79777414d17a00ee16502282612c77c4d9bbd25a` |
| [reviews/full-run-20261010-g20-review-packet.md](full-run-20261010-g20-review-packet.md) | 56839 | `b34a1ee747e48d7a19af4cbaad28ef4d313c5197ae1dc6ce3fdcecd2bdcccca7` |

## Verification scope

Four unique candidate IDs, 46 local claim-ledger records, ten reused-consistently G20 source IDs, one new pattern, exact filenames, YAML approval metadata, relative references/anchors and illustrative arithmetic were checked. The review packet records the detailed checks, actual dependency hashes, source-access limits and pending gates.

Inspected cumulative dependency archive: `GD-Knowledge-waves-1-2-reviewed-drafts-2026-10-11.zip`, 1994913 bytes, SHA-256 `4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931`. Library identity `libfile_082dcf2646dc8191af243051d202f4a8`; backing `file_00000000b0d881f7a51345657bda5287`; Library version not returned.

## Hash convention and history

The packet lists candidate hashes; this receipt records the finalized packet hash. This receipt does not include its own hash and is not hashed by the packet, avoiding a cyclic self-hash claim. A later corrected capture must preserve candidate identities, record predecessor hashes and explain supersession rather than reuse these hashes for changed bytes. No earlier G20 revision or second dispatch is asserted here.

## Gate status and next decision

Author drafting and local static QA complete. Independent G20 review pending. Actual-host retrieval not run; overall Gate D not certified. Gate E not passed. Next: a fresh independent reviewer checks the bounded claims and pattern distinctness; Doug/Library Coordination then decide revision, acceptance scope and identity mappings. No release, publication, implementation or additional batch follows automatically.

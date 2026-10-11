---
id: null
kind: artifact-receipt
title: W03 exact-byte artifact receipt
run_id: GDR-FULL-20261010
batch: W03
version: 0.1.0
status: draft
candidate_revision: initial-1
updated: '2026-10-10'
reviewer: null
approved_by: null
approved_date: null
predecessor_hash: null
supersedes: null
---

# W03 exact-byte artifact receipt

Workflow receipt for the initial W03 submission. These hashes identify bytes, not evidence validity, canonical authority, independent review, release or game adoption. All five research candidates remain 0.1.0 draft / `initial-1`, with reviewer, approved_by and approved_date null. The review packet is a workflow artifact without a research-entry ID.

The packet records the input snapshot, complete claim/source ledgers, self-review, gaps, queue and gates. This detached receipt records the packet hash without creating a self-referential hash field. **This receipt's own hash is intentionally excluded.**

| Exact relative path | Identity | Version / candidate revision | Bytes | SHA-256 |
|---|---|---|---:|---|
| [topics/environmental-storytelling.md](../topics/environmental-storytelling.md) | `GDR-CAND-20261010-W03-TOP-01` | 0.1.0 / initial-1 | 33110 | `698c2db3db9f5c98d168f9f1f02483991a1a9d538510ff4a37f651642c5b88fe` |
| [topics/level-and-spatial-design.md](../topics/level-and-spatial-design.md) | `GDR-CAND-20261010-W03-TOP-02` | 0.1.0 / initial-1 | 36394 | `16bebe2f8008936e78989a2607b1f9cef89c8be338686700b74e36218625542d` |
| [topics/world-structure-and-exploration.md](../topics/world-structure-and-exploration.md) | `GDR-CAND-20261010-W03-TOP-03` | 0.1.0 / initial-1 | 39638 | `768c9d441e935cc7d668f04b98207742d38e89094b81042eca6888f88ab62be6` |
| [patterns/corroborated-spatial-inference.md](../patterns/corroborated-spatial-inference.md) | `GDR-CAND-20261010-W03-PAT-01` | 0.1.0 / initial-1 | 27130 | `51c1e57ef3123ecc13c8b741a62498b9a7d2c01707f039e5c81effa443479b9b` |
| [patterns/destination-signaled-route-choice.md](../patterns/destination-signaled-route-choice.md) | `GDR-CAND-20261010-W03-PAT-02` | 0.1.0 / initial-1 | 25090 | `ac7a572851492dffea3962126db08002962611e493e774d9f161504fd31ff596` |
| [reviews/full-run-20261010-w03-review-packet.md](../reviews/full-run-20261010-w03-review-packet.md) | `Workflow packet; no allocated research-entry ID` | 0.1.0 / initial-1 | 77917 | `25fd68f09df18577b54559525ac533eb74dba4f4a39ec437afae2920fd6136fc` |

## Scope and recovery

There are three topic candidates, two pattern candidates, one review packet and this receipt. No earlier batch is included. All package artifacts are Markdown. No source PDFs, game images, font files, repository content or implementation assets are included.

For a later correction, retain the candidate ID, increment candidate_revision, record this captured predecessor hash and identify the supersession relationship. Recompute hashes after finalizing the revised content. A matching hash establishes only byte identity; it does not decide which candidate coordination has selected.

## Evidence limits and gates

Local artifact checks are recorded in the [review packet](full-run-20261010-w03-review-packet.md). They are not player tests or Project-host retrieval tests. Independent Gate C review is pending, overall Gate D remains uncertified, and Gate E/release has not passed. Source deduplication, missing shared dependencies and permanent ID mapping remain coordination tasks.

**Next decision:** review the exact captured W03 files independently before any acceptance, release, publication or implementation decision.

---
kind: integrity-receipt
title: F05 exact-byte integrity and local-check receipt
version: 0.1.0
status: draft
run_id: GDR-FULL-20261010
batch_id: F05
updated: '2026-10-10'
candidate_revision: initial-research-1
attempt_id: F05-authoring-01
reviewer: null
approved_by: null
approved_date: null
output_library_receipt: null
self_hash_included: false
---

# F05 exact-byte integrity and local-check receipt

This is a detached workflow receipt, not a research entry, independent review, permanent-ID allocation or release. Hashes identify the exact UTF-8 delivered files below; this receipt deliberately excludes its own hash to avoid circular self-reference. No output Library/Project-source upload is claimed.

## Delivered file identities

| Exact artifact path | Bytes | SHA-256 |
|---|---:|---|
| [topics/simulation-and-systemic-behavior.md](../topics/simulation-and-systemic-behavior.md) | 39222 | `6e19182acfabd6a486f9406afd8eac74b87e49f9249acca7712707094f382f03` |
| [topics/procedural-and-authored-content.md](../topics/procedural-and-authored-content.md) | 44224 | `590a4379c685a1518526542074e6a8535f8a1f69a2e27d55bfdcaa52565e1775` |
| [patterns/bounded-causal-probe.md](../patterns/bounded-causal-probe.md) | 26889 | `7bd7c82c51a2c6020e1f95a87c132315eff295ec5be74dd4812c5cb0c852deac` |
| [patterns/constraint-gated-generation-with-bounded-fallback.md](../patterns/constraint-gated-generation-with-bounded-fallback.md) | 29553 | `bd97bc342ee683f4ca228941bcbaac6e8a4626e31cfead500710ad49e5bce8aa` |
| [reviews/full-run-20261010-f05-review-packet.md](full-run-20261010-f05-review-packet.md) | 69345 | `a4a9d9b061b551b3b14495541b8e3985120351c1c9693f54645bd5e05768f3a4` |

## Executed local checks

| Check | Observed result | Scope and limit |
|---|---|---|
| Exact output set | PASS | Two topics, two patterns, exact lower-case packet, detached Markdown receipt; no old batch or extra pattern. |
| Candidate front matter and identity | PASS | Four unique authorized run-scoped IDs; version/revision/attempt consistent; all reviewer/approval/predecessor/supersession fields null. |
| Template and claim structure | PASS | All required topic/pattern sections present; 55 unique entry-scoped ledger claims; no dangling initial claim markers or unfilled template prompts found. This does not assess claim truth. |
| Source-record structure | PASS | 11 distinct inspected identities across four candidates; every declared source has a complete reference section. Ten new F05 identities plus reused F01-08; source adequacy is not certified. |
| Relative links and fragments | PASS | 29 relative-link occurrences checked against actual local paths/headings; no missing/out-of-package targets. External-link durability and Project-host routing remain untested. |
| Packet inventory, cap and queue preservation | PASS | Inventory hashes match current candidate bytes; exactly two patterns; F02 overlap, prior queues, new unregistered proposals, source mapping and pilot identity limits recorded. |
| Author-only adversarial review | RECORDED | Same authoring assistant reviewed strongest recommendations and narrowed unsupported claims; this is not independent Gate C review. |
| Project-host retrieval / player or generator tests | NOT RUN | No cold/blind retrieval, host upload/routing, participant experiment, prototype, generator, engine or runtime test was performed. Overall Gates D/E not passed. |

The relative-link count above was measured before this detached receipt was finalized. A final pass also verifies the five links in this receipt; it does not recalculate or change the covered artifacts. Static checks are not source verification, gameplay validation or Project-host reliability tests.

## Reviewed-input byte check

Input archive: `GD-Knowledge-waves-1-2-reviewed-drafts-2026-10-11.zip`; supplied Library `libfile_082dcf2646dc8191af243051d202f4a8`; backing `file_00000000b0d881f7a51345657bda5287`. Materialized size **1,994,913 bytes**; computed SHA-256 **`4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931`**. ZIP CRC passed; **213** payload size/hash rows matched the archive’s own cumulative manifest. The supplied receipt reported size, not a cumulative ZIP hash; no nonexistent external hash match is asserted. Internal agreement does not establish canonical authority or evidence validity.

Selected dependency hashes and inspected passage scopes are in the review packet. F03/W03 initial packet excerpts were readable, but later expansion/raw-byte retrieval failed; no exact packet hash or unseen body inspection is asserted for those sources.

## Gate boundary and next step

F05 independent Gate C review is pending. These local checks are only a subset of packaging work; actual-host Gate D and acceptance/release Gate E remain uncertified. Review the covered bytes, resolve the F02 queued-concept overlap and missing dependencies, and preserve candidate/source identities through any correction. No prior batch, repository, Project source, engine or publication was changed.

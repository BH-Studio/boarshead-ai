---
id: GDR-FULL-20261010:G16:integrity-receipt
kind: integrity-receipt
title: G16 — local delivery and integrity receipt
version: 0.1.0
status: draft
candidate_revision: initial-author-draft-1
run: GDR-FULL-20261010
batch: G16
updated: '2026-10-10'
owner_project: BH-GDR-Genres
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: []
independent_review: not-performed
library_upload: not-performed
repository_write: not-performed
project_source_write: not-performed
---

# G16 local delivery and integrity receipt

This administrative receipt records the final conversation-delivered Markdown byte streams and executed local document checks. It is **not** a research entry, third pattern, independent evidence review, Library upload receipt, canonical snapshot, host retrieval result or release approval.

## Final payload hashes

SHA-256 hashes below cover exact UTF-8 file bytes. The review packet contains the five research-entry hashes; this separate receipt contains the packet hash to avoid a circular self-hash. This receipt does not embed its own digest.

| Exact delivered path | Bytes | SHA-256 |
|---|---:|---|
| [genres/roguelike.md](../genres/roguelike.md) | 37512 | `4daf9109b3fa250888427aa2d370e646b55b5e9d6dc90440bc1bb79d4eb8ebca` |
| [genres/roguelite.md](../genres/roguelite.md) | 37759 | `154dea536741d695b71829100c236fe97fb1075d58bf3af6a1352b401a90e016` |
| [genres/deckbuilder.md](../genres/deckbuilder.md) | 40341 | `6413c341b6ac99d7ed377bd3751cf37ff0bbd4ee905e6d1ae9f9aba8635f5580` |
| [patterns/explicit-run-state-boundary.md](../patterns/explicit-run-state-boundary.md) | 26839 | `96051696f24a11427cbc0bb8d2b722dad8c53cff7a250bc698998d52c2daa2cd` |
| [patterns/cycle-aware-deck-acquisition.md](../patterns/cycle-aware-deck-acquisition.md) | 28555 | `104ecc15ced437ecf16ebc7bb215a05c1fc0b29c8938083d9bf744ee64abd5a2` |
| [reviews/full-run-20261010-g16-review-packet.md](full-run-20261010-g16-review-packet.md) | 101025 | `3b2689711c172e3ce0a84d2b78c493a0e221c80394de1f2cf8a98f23d6e934df` |

## Executed local document checks

**Observed result: 15 check groups passed** on the final main payloads; the relative-link check also includes this receipt. The checks establish document consistency only. They do not verify that a source is correct, that a causal interpretation is valid, or that a technique improves gameplay.

| Check | Observed result / scope |
|---|---|
| Exact research inventory | Passed — Three assigned genres and two optional patterns; no other research artifact. |
| UTF-8 / front matter / lifecycle | Passed — All six main Markdown artifacts parse; version, revision, lifecycle and null approval/predecessor fields match. |
| Unique artifact identities | Passed — Five research IDs and one packet-local administrative identity; no permanent GDK ID allocated. |
| Research byte hashes / packet inventory | Passed — All five final byte sizes and SHA-256 digests match the packet and assembly receipt. |
| Claim classes and support identity resolution | Passed — 62 claims have unique entry-local IDs, allowed classes, confidence/limits, and known support identities; no lead-only source supports a claim. |
| Standalone source declarations / references | Passed — Every public source used by each research claim is declared and has its complete reference record. |
| Source namespace / reused identity | Passed — Fifteen G16 source records plus the reused F02-012 Hades identity; no G16 alias for that source. |
| Original input immutability | Passed — 12 original input hashes unchanged. |
| Dependency archive identity | Passed — Archive remains 1,994,913 bytes; recorded fingerprint matches the archive used for 213 manifest and 38 selected-entry checks. |
| Selected transferred dependency hashes | Passed — All nine specifically transferred selected artifacts match their recorded digests. |
| Illustrative arithmetic | Passed — Feasible/infeasible/equality resource probes and one-target fresh-uniform-draw arithmetic checked. No game outcome inferred. |
| Unfilled template scan | Passed — No unfilled template tokens in the six main artifacts. |
| Relative links and section anchors | Passed — All package-relative links and specified section anchors resolve, including this receipt. External URLs were inspected during source research; this local check does not re-fetch the web. |
| Required artifact sections | Passed — All five research files retain the applicable genre/pattern template sections; tests and failure cases are separately present. |
| Queued work is not dispatched | Passed — Four packet-local proposals are queued; no child key assigned or batch sent. |

The validator initially expected confidence fields to contain bare labels and a particular phrase for unallocated child work. Inspection showed that the artifacts instead contain allowed confidence labels followed by their rationale, and the explicit statement that no child key has been allocated, sent or reserved. Those two validator predicates were corrected to test the actual required semantics, and the full check set was rerun. No failed evidence test was relabeled as successful.

## Dependency and input receipt

Actual raw-byte dependency archive: `GD-Knowledge-waves-1-2-reviewed-drafts-2026-10-11.zip`, 1,994,913 bytes, SHA-256 `4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931`. Supplied Library identity: `libfile_082dcf2646dc8191af243051d202f4a8`; actual materialized backing file: `file_00000000b0d881f7a51345657bda5287`; returned version: null. No external trusted expected cumulative digest was supplied.

The recorded archive checks matched **213/213 manifest payloads** by size and hash and **38/38 selected entries** by hash. The current final check confirms the archive still has the same fingerprint and all **nine specifically transferred research artifacts** still match their recorded digests. Nine relevant bodies/passages and selection/correction provenance were inspected; the byte checks do not claim that all research content was read or independently validated.

All **12 supplied original files** remain unchanged against the before-assembly hash baseline. Exact input and dependency file paths, versions, hashes, locators and transferred limits are in the review packet. No dependency files or prior batches are repackaged as new G16 outputs.

## Research coverage and limits

The five research candidates contain **62 entry-local classified claims**. The source ledger contains **16 public source records**: 15 with inspected relevant excerpts and one lead-only thesis catalog whose body was not retrieved. Fifteen temporary source records use the G16 namespace; the Hades FAQ retains the existing `GDR-SRC-20261010-F02-012` identity. Mirrors, creator accounts and related sources are not counted as independent empirical replications.

Source-access limits remain in the packet, including the unread Wilson thesis body, Aeon’s End rulebook screenshot failures and third-party hosting, unknown executed game builds, narrow experimental context, and unavailable selected later-wave dependency bytes. No prototype, gameplay session, participant study or live host retrieval test was performed. Four additional local proposals remain queued without child-key allocation.

## Gate and delivery state

All research entries remain **0.1.0 / draft / coverage-open**, revision `initial-author-draft-1`, with null reviewer and approval fields. **Gate C:** independent review pending. **Gate D:** these static packaging checks only; overall retrieval acceptance is not certified. **Gate E:** not passed; no release. The authorized G16 research execution does not imply final taxonomy, implementation, publication or canon approval.

Delivery is through seven downloadable Markdown files in this conversation: three genres, two patterns, one exact lower-case review packet and this administrative receipt. **No persistent Library write, repository modification, Project-source change, publication, purchase or player-test action occurred.** The available materialization receipt concerns read access to an existing dependency, not a new upload.

**Next decision:** submit this G16 packet once to the parent/Doug for independent review, preserving candidate identities across requested corrections. Library Coordination must resolve missing reviewed dependencies, source deduplication and shared-pattern overlap before permanent allocation or any separately authorized child dispatch.

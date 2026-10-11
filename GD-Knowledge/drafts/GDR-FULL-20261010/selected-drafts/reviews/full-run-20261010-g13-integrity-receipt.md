---
kind: integrity-receipt
run_id: GDR-FULL-20261010
batch_id: G13
version: 0.1.0
status: draft
candidate_revision: initial-capture-1
updated: '2026-10-10'
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
scope: local-static-packaging-only
independent_review_state: not-yet-reviewed
---

# G13 integrity receipt

**Local static packaging record; not independent review, a Library capture receipt or Gate D acceptance.**

Run `GDR-FULL-20261010`; batch `G13`; candidate revision `initial-capture-1`; generated 2026-10-11T04:56:07.964409+00:00 UTC. Local evidence-check date remains 2026-10-10 America/Los_Angeles. All candidate versions are `0.1.0` draft. Reviewer/approval fields are null.

## Final exact-byte inventory

| Candidate / support role | Exact relative path | Bytes | SHA-256 | Predecessor / supersession |
|---|---|---:|---|---|
| `GDR-CAND-20261010-G13-GEN-01` | [genres/colony-simulation.md](../genres/colony-simulation.md) | 33720 | `6585b1d3f509e5b784549b95baa83086ba9e9195fc7e890876515ba4add47998` | null / null; initial capture, no prior G13 bytes supplied or located by bounded retrieval |
| `GDR-CAND-20261010-G13-GEN-02` | [genres/life-simulation.md](../genres/life-simulation.md) | 35116 | `6d5f1669b19bcd2aab38302c43e026a93918b81eebe14f23e65e024ffab7360d` | null / null; initial capture, no prior G13 bytes supplied or located by bounded retrieval |
| `GDR-CAND-20261010-G13-GEN-03` | [genres/sandbox.md](../genres/sandbox.md) | 34192 | `d3b28b377e74db4a631f3d244a5e3c655309c35320761c5082defd2993524679` | null / null; initial capture, no prior G13 bytes supplied or located by bounded retrieval |
| `GDR-CAND-20261010-G13-PAT-01` | [patterns/scoped-autonomous-changes.md](../patterns/scoped-autonomous-changes.md) | 23191 | `aaa36b4f43e930ee4f1d909c2c1e1607c2b84b91c23c25dc21746d5ff3a4a5d6` | null / null; initial capture, no prior G13 bytes supplied or located by bounded retrieval |
| `GDR-CAND-20261010-G13-PAT-02` | [patterns/reversible-experiment-branch.md](../patterns/reversible-experiment-branch.md) | 24227 | `01c7750ad277ce1482bf85950eaf1f952ac1b8d70dc5111a5578ea101a467b4e` | null / null; initial capture, no prior G13 bytes supplied or located by bounded retrieval |
| `Supporting review packet; no permanent ID` | [reviews/full-run-20261010-g13-review-packet.md](../reviews/full-run-20261010-g13-review-packet.md) | 94302 | `28e5c2bc502f41156532977dedf0cbdf109a653a4afb9467f1134d40123df0a8` | null / null; initial capture, no prior G13 bytes supplied or located by bounded retrieval |

The receipt does not embed its own exact-byte hash. Its external SHA-256 is provided with the delivery. Candidate and packet hashes above were computed after their final writes. A correction after capture must preserve each candidate ID, record its predecessor hash and supersession relationship, and issue a corresponding revised receipt. No conceptual identity is changed merely because wording changes.

## Executed author-side checks

| Check | Result | Scope / limitation |
|---|---|---|
| Exact candidate paths and identities | PASS | Three assigned genre paths/IDs and two sequential G13 pattern IDs match the dispatch/scope. |
| Unique candidate identities | PASS | Five distinct temporary candidate IDs; no permanent allocation. |
| Two-pattern cap | PASS | Exactly two new pattern artifacts, no third pattern candidate. |
| Candidate front matter: genres/colony-simulation.md | PASS | Written front matter agrees with the manifest; draft/null approvals/revision retained. |
| Local claim markers: genres/colony-simulation.md | PASS | 11 unique ledger rows; every explicit C-nn marker resolves locally. Range endpoints checked, semantic citation sufficiency remains author/independent review work. |
| Source identity membership: genres/colony-simulation.md | PASS | Every listed source has a batch record and an entry reference; lead-only exclusions additionally reviewed semantically. |
| No template placeholders: genres/colony-simulation.md | PASS | No blank-template prompts or unassigned identity placeholders remain. |
| Candidate front matter: genres/life-simulation.md | PASS | Written front matter agrees with the manifest; draft/null approvals/revision retained. |
| Local claim markers: genres/life-simulation.md | PASS | 13 unique ledger rows; every explicit C-nn marker resolves locally. Range endpoints checked, semantic citation sufficiency remains author/independent review work. |
| Source identity membership: genres/life-simulation.md | PASS | Every listed source has a batch record and an entry reference; lead-only exclusions additionally reviewed semantically. |
| No template placeholders: genres/life-simulation.md | PASS | No blank-template prompts or unassigned identity placeholders remain. |
| Candidate front matter: genres/sandbox.md | PASS | Written front matter agrees with the manifest; draft/null approvals/revision retained. |
| Local claim markers: genres/sandbox.md | PASS | 12 unique ledger rows; every explicit C-nn marker resolves locally. Range endpoints checked, semantic citation sufficiency remains author/independent review work. |
| Source identity membership: genres/sandbox.md | PASS | Every listed source has a batch record and an entry reference; lead-only exclusions additionally reviewed semantically. |
| No template placeholders: genres/sandbox.md | PASS | No blank-template prompts or unassigned identity placeholders remain. |
| Candidate front matter: patterns/scoped-autonomous-changes.md | PASS | Written front matter agrees with the manifest; draft/null approvals/revision retained. |
| Local claim markers: patterns/scoped-autonomous-changes.md | PASS | 10 unique ledger rows; every explicit C-nn marker resolves locally. Range endpoints checked, semantic citation sufficiency remains author/independent review work. |
| Source identity membership: patterns/scoped-autonomous-changes.md | PASS | Every listed source has a batch record and an entry reference; lead-only exclusions additionally reviewed semantically. |
| No template placeholders: patterns/scoped-autonomous-changes.md | PASS | No blank-template prompts or unassigned identity placeholders remain. |
| Candidate front matter: patterns/reversible-experiment-branch.md | PASS | Written front matter agrees with the manifest; draft/null approvals/revision retained. |
| Local claim markers: patterns/reversible-experiment-branch.md | PASS | 10 unique ledger rows; every explicit C-nn marker resolves locally. Range endpoints checked, semantic citation sufficiency remains author/independent review work. |
| Source identity membership: patterns/reversible-experiment-branch.md | PASS | Every listed source has a batch record and an entry reference; lead-only exclusions additionally reviewed semantically. |
| No template placeholders: patterns/reversible-experiment-branch.md | PASS | No blank-template prompts or unassigned identity placeholders remain. |
| Source counter continuity | PASS | G13-001 through G13-016 issued once; no range reservation or counter reset. |
| Source access counts | PASS | 14 inspected excerpt records and two explicit lead-only records. |
| Input snapshot unchanged | PASS | Supplied starter/brief inputs and materialized dependency ZIP match the local fingerprints captured for packaging. |
| Proposed index alignment | PASS | Every candidate identity appears in the proposed index and packet; actual canonical index not edited. |
| Local Markdown targets and anchors | PASS | 48 final local link occurrences checked for existing in-package files and explicit anchors, including the completed integrity receipt. External links were source-inspected, not bulk availability-tested. |
| Exact lower-case packet path | PASS | Historical proposed filename case variants are not used. |
| Candidate byte fingerprints | PASS | Packet candidate hashes identify the exact delivered draft bytes. |
| Artifact tree count | PASS | Seven Markdown outputs: five research candidates, one review packet, one integrity receipt. No prior batches redistributed. |

**Result:** 31 of 31 listed local checks passed. Checks were run using local file/Markdown parsing and SHA-256 only. No engine, project implementation, participant experiment or actual-host retrieval was executed. A static PASS is not an evidence review or a release gate.

## Provenance and boundary

The actual input Library materialization was `libfile_082dcf2646dc8191af243051d202f4a8`, backing `file_00000000b0d881f7a51345657bda5287`, version ID not supplied. The ZIP was 1,994,913 bytes, SHA-256 `4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931`. Its relevant selected bytes were read but are not redistributed here. The review packet records their identities, revisions, hashes, exact inspected sections and inherited source namespaces.

No output Library ID/version, canonical commit, Project upload, repository publication or permanent-ID receipt exists for this generated tree. Files are conversation-local downloadable Markdown. The provided links do not establish synchronization, independent review or release.

## Evidence and gate status

Five research candidates; 56 scoped claim rows; 14 inspected public primary-document excerpts; two lead-only sources; nine relevant reviewed dependency entries inspected selectively. No direct game-build observation, player study, prototype, actual-host test or gameplay-efficacy result. Every candidate is coverage-open. Parent-selected shared drafts remain unreleased; their underlying public sources were not newly reverified by G13.

Gate B permits this bounded authoring under the supplied authorization. G13 Gate C independent review is pending; overall Gate D and Gate E are not passed. Pattern ownership/novelty, cross-batch source deduplication and canonical identity allocation remain with Library Coordination. Three extra decision questions are queued without child-key allocation or submission.

**Next step:** the parent independently reviews the five candidate bytes named above and records corrections and remaining disputes. Doug/Coordination then decide on genre-boundary revisions, pattern concept homes and whether to register any queued child work. No resubmission of G13, release, implementation, Project-source replacement or repository write follows from this receipt.

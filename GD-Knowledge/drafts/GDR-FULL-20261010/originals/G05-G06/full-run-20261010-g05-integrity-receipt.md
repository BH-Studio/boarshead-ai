---
kind: integrity-receipt
run_id: GDR-FULL-20261010
batch_id: G05
version: 0.1.0
status: draft
candidate_revision: initial-capture-1
updated: '2026-10-10'
owner_project: BH-GDR-Genres
reviewer: null
approved_by: null
approved_date: null
---

# G05 integrity receipt

Administrative byte/packaging record for the four research candidates and their exact lower-case review packet. These checks were executed during G05 document production. They are **author checks, not independent source verification, gameplay tests, Project-host behavior tests, or an overall Gate D pass**. No permanent ID or output Library receipt is allocated by this document.

## Delivered bytes

Hashes use SHA-256 over actual UTF-8 file bytes, including the final newline. The receipt does not embed its own full-byte hash, avoiding self-reference; it identifies the five other delivered files.

| File | Bytes | SHA-256 |
|---|---:|---|
| [genres/fighting.md](../genres/fighting.md) | 45,561 | `9facb4e2777e61edf78dc4b34fdcc3a55728a93e8397a8818c82bb15082b30d4` |
| [genres/beat-em-up.md](../genres/beat-em-up.md) | 41,026 | `f188e3e79f7d80e3fc9bfe0f931acb580e315a267f97a370f162c3c2386c2e2e` |
| [patterns/replay-to-variant-practice.md](../patterns/replay-to-variant-practice.md) | 21,630 | `069483f96e338b14a2ce6016147eaf7048ae73a9864162d4fdefcbdd4ffb58e3` |
| [patterns/recoverable-expenditure-window.md](../patterns/recoverable-expenditure-window.md) | 21,857 | `4bd0087081d8caa962dabcd48da1d5770d154a5e8a329563c162a87ff8407d62` |
| [reviews/full-run-20261010-g05-review-packet.md](full-run-20261010-g05-review-packet.md) | 67,204 | `6ce62af43bcad470647b7b2737aba3021b37d48cf6ee7d590a20fd942db51d4b` |

## Executed static checks

| Check | Result | Observation and limit |
|---|---|---|
| Front matter | PASS | Five candidate/packet files parse as YAML-front-matter Markdown; all version 0.1.0/draft with null reviewer and approval metadata. |
| Assigned identities and cap | PASS | Two assigned genres and two temporary pattern identities; no duplicate IDs; pattern cap equals two. |
| Exact packet filename | PASS | reviews/full-run-20261010-g05-review-packet.md; no case-variant packet. |
| Claim and source routing | PASS | 48 local ledger claims (18, 15, 8, 7); each has one claim class; no unresolved local claim markers; 17 consistent source IDs, all present in master registry. |
| Relative links and anchors | PASS | 55 relative-link occurrences resolve to files and, where specified, local anchors. This is a static Markdown check, not a Project-host routing test. |
| Markdown tables | PASS | All pipe-table blocks have consistent column counts; no rendered PDF or document conversion was used. |
| Packet hash inventory | PASS | All four candidate hashes recorded in the packet match the delivered bytes after the author correction. |
| Mounted input preservation | PASS | 12 original mounted input files remain byte-identical to the pre-generation inventory. |
| Revision lineage | PASS | The corrected fighting file retains its assigned identity and links to the preserved exact initial local predecessor hash. Other candidate predecessor/supersession fields are null. |
| Template residue | PASS | No unfilled template identity/title/date tokens or TODO/TBD markers. Explicit research gaps are retained, not hidden as completed coverage. |

## Scope not tested

No game or engine code was executed. No participant, first-hand gameplay, recording analysis, cold/blind host retrieval, upload-routing, alias behavior, source-instruction adversarial prompt, or implementation test was performed. A Markdown link resolving in this local tree does not establish flat-host Project routing. Public-source locators were inspected as recorded in the packet; this hash check does not independently validate their interpretation.

The two genre files and two patterns remain drafts with null reviewer/approval fields. Gate C independent review, overall Gate D, Gate E/release, permanent-ID/source deduplication, and proposed ownership decisions remain pending. No repository, Project-source, settings, engine, or publication operation was performed.

## Next decision

Use the exact hashes in this receipt for the parent’s independent Gate C review and coordination overlap/deduplication check. Retain the assigned identities through any correction. The [review packet](full-run-20261010-g05-review-packet.md) contains the evidence limits, queued child proposals, dependency provenance, and gate record.

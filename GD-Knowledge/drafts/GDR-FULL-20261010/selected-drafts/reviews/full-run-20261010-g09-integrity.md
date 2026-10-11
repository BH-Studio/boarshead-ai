---
kind: artifact-integrity-receipt
run_id: GDR-FULL-20261010
batch_id: G09
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
attempt_id: G09-authoring-01
updated: '2026-10-11'
date_basis: UTC
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
scope: Four research drafts and the exact lower-case G09 review packet; this receipt
  excludes its own hash.
---

# G09 artifact integrity receipt

This is a local byte-identity and static-document-check record, not a canonical Library receipt, independent content review, source-verification certificate or release. The research candidates retain their assigned temporary identities. No predecessor or supersession is asserted for this first G09 submission.

## Exact delivered payloads

Hashes use SHA-256 over the actual UTF-8 file bytes, including front matter and final newline. This detached receipt covers the four research entries and the review packet; it intentionally excludes itself to avoid circular self-hashing.

| Path | Identity / role | Bytes | SHA-256 |
|---|---|---:|---|
| [genres/4x.md](../genres/4x.md) | `GDR-CAND-20261010-G09-GEN-01` | 36,321 | `5e5c56f1573ac2276d830539dd64d6450015a07c259a17aa2489f3e036c61157` |
| [genres/tower-defense.md](../genres/tower-defense.md) | `GDR-CAND-20261010-G09-GEN-02` | 38,049 | `03bfda3eec278a5475d480aa98b3a8318cfdf346b3ff6bf4d52338c39456ddc7` |
| [genres/auto-battler.md](../genres/auto-battler.md) | `GDR-CAND-20261010-G09-GEN-03` | 43,198 | `a62ae91b7d63e760e016748c4d231b5b01f2d32225900b722b4a8eeb0d29ffc6` |
| [patterns/evidence-bounded-resolution-debrief.md](../patterns/evidence-bounded-resolution-debrief.md) | `GDR-CAND-20261010-G09-PAT-01` | 26,548 | `f846248c29ee1aafd94ca3402759616f5fc98b881cf2275d8b1db310ff78b97b` |
| [reviews/full-run-20261010-g09-review-packet.md](full-run-20261010-g09-review-packet.md) | `GDR-FULL-20261010:G09` | 73,451 | `279b3235f12dca71ff0bcc7067e973113327af819a84a26455dfe5f4f4da87c2` |

## Performed static checks

Performed on **2026-10-11 UTC** by the same authoring assistant, using local document-validation scripts. These scripts read/write Markdown and inspect bytes; they are not game/project/engine code or player tests. PASS below applies only to the named static property. No independent reviewer or host test is implied.

| Check | Observed result | Scope / evidence limit |
|---|---|---|
| Exact research paths and assigned identities | **PASS** | Three assigned genres plus G09-PAT-01; unique IDs. |
| Version, revision, lifecycle and approval metadata | **PASS** | 0.1.0 / initial-draft-1 / draft; reviewer and approval fields null. |
| Pattern cap and source identity union | **PASS** | One pattern; 21 unique G09 source identities reused across entries. |
| Complete local claim ledgers | **PASS** | 54 records; no undefined local C-xx references. |
| Complete source reference headings | **PASS** | Each research file’s source_ids equals its complete-reference heading set. |
| Required genre/pattern sections | **PASS** | Custom genre guidance and complete pattern recipe, exits and proposed tests present. |
| Markdown and YAML parsing | **PASS** | UTF-8 text, parseable front matter and CommonMark tables; no template placeholders. |
| Delivered relative links and anchors | **PASS** | 108 links in the five payload files checked before finalization; final pass includes this receipt and verifies that every local target and referenced heading resolves. |
| External reference syntax / provenance | **PASS** | 44 external-link instances in payload files parsed; claim-support passages were inspected in the browser. No blanket current-site or binary validation is implied. |
| Review-packet payload hashes | **PASS** | All four research hashes match the packet inventory. |
| Reviewed dependency payload comparison | **PASS** | 26 selected payloads matched archive-manifest sizes/hashes; manifest self excluded. |
| Live host / blind retrieval tests | **NOT RUN** | No uploaded snapshot or observed host test responses in G09. |
| Game builds, prototypes and participant tests | **NOT RUN** | Only document/byte validation was performed. |
| Independent G09 evidence/content review | **NOT PERFORMED** | Author self-review only; parent dependency receipts are distinct. |

## Dependency-byte verification

The parent-selected cumulative archive was actually materialized from Library `libfile_082dcf2646dc8191af243051d202f4a8`, backing `file_00000000b0d881f7a51345657bda5287`. Filename: `GD-Knowledge-waves-1-2-reviewed-drafts-2026-10-11.zip`; size **1,994,913 bytes**; locally computed SHA-256 **`4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931`**. The selected 26 manifest-listed payloads matched their recorded size and hash. The archive’s own manifest supplies the comparison, not an independent trusted authenticity guarantee. Relevant passage and revision records are in the review packet.

No G09 Library ID, upload receipt, canonical commit, repository update or Project-source synchronization is claimed. Generated conversation Markdown files are the delivery artifacts. The received Library archive is an input, not a new G09 publication.

## State after checking

All four research entries remain **0.1.0 draft / initial-draft-1**, with null reviewer/approved_by/approved_date. One pattern is delivered under the two-pattern packet cap; four named child proposals remain queued without allocated keys. All 54 research claim records remain qualified by their source and application limits. Public-source records total 21, with repeated use retaining the same ID.

Independent Gate C review, live/cold-blind Gate D retrieval and Gate E acceptance/release are **not complete**. Static checks cannot establish gameplay efficacy, accessibility outcomes, historical interpretation, competitive equity or the reliability of the hypothesized debrief. No participant tests, purchases, game changes, repository edits, permanent-ID allocations or publication occurred.

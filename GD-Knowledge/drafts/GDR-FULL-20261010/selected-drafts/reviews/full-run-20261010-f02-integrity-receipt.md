---
kind: integrity-receipt
run_id: GDR-FULL-20261010
batch_key: F02
version: 0.1.0
status: draft
candidate_revision: initial-capture-1
attempt_identity: F02-local-attempt-01
predecessor_sha256: null
supersedes: null
updated: '2026-10-10'
reviewer: null
approved_by: null
approved_date: null
---

# F02 exact-byte integrity receipt

This is local delivery metadata for the F02 draft snapshot, not a research entry, source verification certificate, independent review, host-test pass or release approval. No conceptual or permanent ID is allocated to this receipt. The review packet retains its exact assigned lower-case filename.

## Delivered core files

SHA-256 values cover the complete UTF-8 bytes as delivered, including front matter and final newline. All core candidates retain version 0.1.0 and revision initial-capture-1. Predecessor and supersession are null for this initial visible capture. The receipt does not contain its own hash, avoiding circularity; its hash is provided at delivery.

| File | Bytes | SHA-256 |
|---|---:|---|
| [topics/decision-design.md](../topics/decision-design.md) | 33,529 | `2fe66a5bf914a9c3f4101e168cdfd344a26eeadbfea7c45d16a9f17cca33bc6c` |
| [topics/challenge-and-difficulty.md](../topics/challenge-and-difficulty.md) | 34,937 | `c4cdce1b33661195b9c732b46209729f5db99418a369f1a5af18c429308654e4` |
| [patterns/visible-opportunity-cost-comparison.md](../patterns/visible-opportunity-cost-comparison.md) | 16,912 | `afb19a4a363fbef3d7478731f84520c500dad15858d42a8b38bc0446ae63648b` |
| [patterns/bounded-disclosed-difficulty-adaptation.md](../patterns/bounded-disclosed-difficulty-adaptation.md) | 21,369 | `d442c6f6bac8c46f363cbf7ec91bdcd58e7ea840213a0f6c5f21015817a8dd6b` |
| [reviews/full-run-20261010-f02-review-packet.md](full-run-20261010-f02-review-packet.md) | 59,325 | `fe57fad9b32f6d0dab93d819f29d233ea3bc3148a41f477111ada76efa438923` |

## Local checks actually performed

Checker: local Python document-packaging script, executed 2026-10-10. It did not run project/engine code, perform statistical reanalysis, recruit participants, edit a repository, publish content or mutate Project sources. “Pass” below means only the specified static condition was met on these local files.

| Check | Observed result | Scope |
|---|---|---|
| UTF-8 and Markdown syntax | PASS | Five core files decoded and parsed locally; no host rendering implied. |
| Assigned paths and identities | PASS | The two assigned topic IDs and two F02 pattern IDs match their expected paths. |
| Unique research identities | PASS | Four unique research candidate IDs; no additional F02 research artifacts. |
| Two-pattern packet cap | PASS | Exactly two pattern Markdown files in this delivery. |
| Exact packet case | PASS | Exact requested lower-case review filename exists. |
| Draft version and null approvals | PASS | Every core artifact has version 0.1.0, draft lifecycle and null approval fields. |
| Revision and predecessor metadata | PASS | Initial visible F02 capture; no predecessor or supersession claimed. |
| Source records: topics/decision-design.md | PASS | 6 declared source IDs, each with a complete reference heading; no undeclared full F02 source ID. |
| Claim ledger: topics/decision-design.md | PASS | 14 ledger claims; all explicit local claim IDs resolve. |
| History placement: topics/decision-design.md | PASS | References precede the final history section. |
| Source records: topics/challenge-and-difficulty.md | PASS | 6 declared source IDs, each with a complete reference heading; no undeclared full F02 source ID. |
| Claim ledger: topics/challenge-and-difficulty.md | PASS | 15 ledger claims; all explicit local claim IDs resolve. |
| History placement: topics/challenge-and-difficulty.md | PASS | References precede the final history section. |
| Source records: patterns/visible-opportunity-cost-comparison.md | PASS | 1 declared source IDs, each with a complete reference heading; no undeclared full F02 source ID. |
| Claim ledger: patterns/visible-opportunity-cost-comparison.md | PASS | 6 ledger claims; all explicit local claim IDs resolve. |
| History placement: patterns/visible-opportunity-cost-comparison.md | PASS | References precede the final history section. |
| Source records: patterns/bounded-disclosed-difficulty-adaptation.md | PASS | 3 declared source IDs, each with a complete reference heading; no undeclared full F02 source ID. |
| Claim ledger: patterns/bounded-disclosed-difficulty-adaptation.md | PASS | 6 ledger claims; all explicit local claim IDs resolve. |
| History placement: patterns/bounded-disclosed-difficulty-adaptation.md | PASS | References precede the final history section. |
| Twelve inspected source identities | PASS | Twelve unique inspected source records; the two lead-only records occur only in the review packet. |
| No unreplaced template prompts | PASS | No unreplaced template prompts found; declared evidence gaps are intentional. |
| Inventory hash: topics/decision-design.md | PASS | Packet inventory matches the current exact research-candidate bytes. |
| Inventory hash: topics/challenge-and-difficulty.md | PASS | Packet inventory matches the current exact research-candidate bytes. |
| Inventory hash: patterns/visible-opportunity-cost-comparison.md | PASS | Packet inventory matches the current exact research-candidate bytes. |
| Inventory hash: patterns/bounded-disclosed-difficulty-adaptation.md | PASS | Packet inventory matches the current exact research-candidate bytes. |
| Relative links and anchors | PASS | 23 core relative links and their anchors checked; receipt target is completed below. 46 public reference links counted, not automatically re-fetched by this checker. |
| Illustrative arithmetic | PASS | Expected reward and three opposite/boundary affordability examples checked; no game code executed. |
| Attached input hash consistency | PASS | Ten attached authority/governance/template hashes still match the packet record; no source replacement by the build scripts. |

## Checks explicitly not performed

Independent F02 evidence review, source-data replication, live Project-host retrieval tests, cold/blind reliability tests, participant playtests, actual game-build observation, accessibility certification, localization validation and engine/harness integration tests were **not performed**. Public references were inspected during research to the depth described in each source record; this static checker does not independently certify their truth or continued availability.

The first-wave ZIP hash was verified against the supplied parent receipt. Only relevant selected passages were inspected. That retrieval did not change the ZIP or make its drafts released, and no first-wave file is included in this delivery.

## Gate and recovery state

Gate C independent review remains pending. Gate D has local static evidence only; actual host tests remain not run. Gate E is not passed and release is not authorized. Permanent identity reconciliation and registered child work remain with Library Coordination.

Future revisions must retain conceptual candidate IDs, record exact predecessor hashes from this receipt, change the candidate revision and describe supersession. Do not reuse this receipt to certify changed bytes. No automatic repository or Project synchronization is asserted.

**Next decision:** independently review the exact F02 research candidates and packet above; decide corrections or reviewed-candidate acceptance before any retrieval/release decision.

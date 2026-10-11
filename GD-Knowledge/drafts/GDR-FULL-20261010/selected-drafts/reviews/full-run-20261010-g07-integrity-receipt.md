---
kind: local-integrity-receipt
title: "G07 local integrity and packaging checks"
run_id: GDR-FULL-20261010
batch_key: G07
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
updated: "2026-10-10"
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed
---

# G07 integrity receipt

**Local document checks only — not an independent content review, canonical receipt, Library save, Project-host test or release.** This receipt describes the initial G07 draft artifacts written in this session. No repository or original source file was edited. Candidate identities remain as assigned; predecessor and supersession are null. Later revisions must preserve the candidate ID and record their new revision, predecessor hash and change summary.

## Exact delivered byte fingerprints

Hashes are SHA-256 over the UTF-8 file bytes, including front matter and line endings. This receipt deliberately does not contain its own hash. All research entries remain version **0.1.0 draft**, `initial-draft-1`, with null reviewer/approved_by/approved_date. The packet is the exact lowercase path requested.

| Artifact | Role | Bytes | SHA-256 |
|---|---|---:|---|
| [genres/tactical-rpg.md](../genres/tactical-rpg.md) | `GDR-CAND-20261010-G07-GEN-01` | 42,859 | `6d9acb78a7f785a4df8131cb4106619886af343e8f7b8cf86f0f44b2a6fb0393` |
| [genres/tactics.md](../genres/tactics.md) | `GDR-CAND-20261010-G07-GEN-02` | 42,918 | `b9639d95be769fed4ad31ab10e0f47600e704e28425c7a13d1e318f066cd0063` |
| [patterns/consequence-preserving-roster-recovery.md](../patterns/consequence-preserving-roster-recovery.md) | `GDR-CAND-20261010-G07-PAT-01` | 30,944 | `28753f2400ed976ed0d905145a2c4e6ec7a7cd0cc773aac06211f46e4f3de229` |
| [reviews/full-run-20261010-g07-review-packet.md](../reviews/full-run-20261010-g07-review-packet.md) | `batch review packet` | 71,349 | `fb29c0390f65a1d75711715161ba969dda40ab49abc93fd0cbc922acbe9dc23b` |

## Executed checks

The local validator parsed candidate YAML, read every output as UTF-8, checked the exact output paths, verified the packet's candidate hashes, checked claim IDs/classifications and source-reference headings, and resolved explicit local Markdown file/heading links. These checks concern the written documents, not a game, engine, live Project or player behavior. A successful link check is not evidence that a user-host retrieval system will select the right revision.

| Check | Observed result | Scope / limitation |
|---|---|---|
| Output set | PASS: five Markdown files; two genre candidates, one pattern, packet and this receipt. | No previous batch files repackaged; local work scripts are not delivered. |
| Temporary identity and approvals | PASS: three unique assigned/run-scoped candidate IDs; version0.1.0, draft; null reviewer/approval fields. | Global/canonical collision checking requires the unavailable current Coordination ledger. |
| Pattern workload | PASS: one pattern, within the two-pattern cap. | Additional work is queued in the packet, not allocated or submitted. |
| Genre/pattern structure | PASS: required template sections present and separately populated. | Heading presence is not evidence of substantive completeness or quality. |
| Claim and source integrity | PASS: 45 entry-local claim records; 14 distinct G07 source identities; every candidate's declared source has a full reference heading. | Source014 is abstract-only and supplies no findings. Classification/locator accuracy still needs independent review. |
| Packet fingerprints | PASS: all three current candidate SHA-256 values match the packet inventory. | Fingerprints identify bytes, not verified conclusions. |
| Local Markdown links | PASS: every explicit local file/heading link resolved in the five-file G07 tree. | Shared historical files are referenced through the packet's archive register, not falsely bundled. No actual-host routing test. |
| UTF-8 / placeholders | PASS: readable UTF-8; no unfilled template tokens or UI-only citation syntax in delivered Markdown. | No browser-rendering certification or accessibility audit. |
| Reviewed dependency equality | PASS: 14 used dependency working copies were compared byte-for-byte against selected archive members. | Relevant sections, not all source content or the entire parent library, were reread. |

## Source/dependency preservation and coverage

The materialized archive is `GD-Knowledge-waves-1-2-reviewed-drafts-2026-10-11.zip`, **1,994,913 bytes**, SHA-256 `4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931`. Library pointer `libfile_082dcf2646dc8191af243051d202f4a8`; returned backing `file_00000000b0d881f7a51345657bda5287`; version ID not returned. Its size matches the dispatch; no expected cumulative-ZIP hash was supplied, so this is a newly computed fingerprint, not a claimed comparison to an unseen receipt. The packet records the exact selected revisions, dependency member hashes and read ranges.

Research coverage is **13 inspected primary-document records plus one abstract-only research lead**, not 13 current game builds or independent empirical studies. No original full-method player-effect evidence supports the new pattern as a tested package. Exact runtime rules, no-level/noncombat range, translation checking and reviewed G06/F04/F05 dependencies remain open. The current canonical index/pending allocation and child-recovery ledgers were not inspected. No new Library storage receipt is asserted for these outputs.

## Gates and handoff

Gate C independent review remains pending. Gate D local packaging checks are partial and do not certify actual uploaded-snapshot retrieval, cold/blind reliability, cross-Project access or canonical reconciliation. Gate E acceptance/release is not passed. No gameplay/playtest/prototype, participant recruitment, purchase, repository/Project-source change or publication was performed.

The next action is a separate source/content review of the exact candidate bytes and their strongest inference, followed by Coordination's ownership/identity/child-work decisions. Doug's later acceptance, any implementation authorization, and any publication approval are separate decisions. Keep the packet's audio checkpoint unchanged and do not treat its prior limited tests as G07 validation.

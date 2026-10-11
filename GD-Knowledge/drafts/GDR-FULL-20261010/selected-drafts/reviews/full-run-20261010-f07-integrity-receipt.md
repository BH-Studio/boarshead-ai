---
kind: integrity-receipt
artifact_key: reviews/full-run-20261010-f07-integrity-receipt.md
run_id: GDR-FULL-20261010
batch_id: F07
version: 0.1.0
status: draft
candidate_revision: initial-capture-1
updated: '2026-10-10'
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
---


# F07 integrity receipt

This is a **local file-integrity and structural-check receipt**, not an independent content review, canonical distribution receipt, source-authentication certificate or release approval. No Project upload or actual host retrieval test occurred. The author created and checked these files on 2026-10-10.

## Exact delivered files

All paths are relative to the package root. Hashes cover the exact UTF-8 bytes, including front matter. The receipt is deliberately not self-hashed: inserting its own whole-file digest would change those bytes. Its omission does not imply that an external signed receipt exists.

| Artifact | Bytes | SHA-256 |
|---|---:|---|

| [topics/evaluation-and-balancing.md](../topics/evaluation-and-balancing.md) | 43446 | `165879841257f88c0a5ecba1f6db5d8b36089dcb260570d7bed6bcd9496d38b8` |

| [topics/ethical-and-sustainable-design.md](../topics/ethical-and-sustainable-design.md) | 49049 | `e26241cb08b1e9ddd4181e7cb92494506ae9b03e04e24032a3e9c79fe0169ce0` |

| [patterns/triangulated-balance-diagnosis.md](../patterns/triangulated-balance-diagnosis.md) | 23312 | `657c3d90ba932cf9ba9828d07e41da0c06af4da72e4cb666aa80e25cc4098b3c` |

| [patterns/legible-commitment-and-safe-exit.md](../patterns/legible-commitment-and-safe-exit.md) | 22899 | `85cffbbdb25c968e9c00f8ab5b3a230c420f24f0b83e19fbff49648e217b425a` |

| [reviews/full-run-20261010-f07-review-packet.md](../reviews/full-run-20261010-f07-review-packet.md) | 63131 | `2b778d9846e6f9146023ec4420bf77bf4269632fccaa0c5b553f4840f9eab704` |

| `reviews/full-run-20261010-f07-integrity-receipt.md` | Self-record intentionally omitted | Not self-hashed |

For each delivered artifact: version 0.1.0; status draft; candidate_revision initial-capture-1; reviewer, approved_by and approved_date null. For the four research entries: predecessor hash and supersedes null. Their candidate IDs and hashes also appear in the [review packet](full-run-20261010-f07-review-packet.md).

## Checks actually executed

| Check | Observed local result | Limit |
|---|---|---|
| Research inventory | Exactly two topics and two patterns; four distinct expected temporary candidate IDs | No global canonical or concurrent-allocation check |
| Metadata | All research candidates and workflow artifacts parse as YAML; draft 0.1.0 and null approvals preserved | Metadata does not establish an approval |
| Claim ledger | 51 locally scoped claims; every cited local claim ID has a ledger entry | Citation correctness still requires independent review |
| Source registry | 16 used source identities; every cited source appears in the owning entry's References and metadata | Not 16 independent studies; cross-batch deduplication pending |
| Entry structure | Topic/pattern sections present; no unfilled template title/date/ID or TODO/TBD token in research entries | Automated token scan is not a semantic completeness proof |
| Local links | All local Markdown file targets and explicit heading anchors resolve in this directory | Does not test flat-host routing, Project retrieval or different Markdown renderers |
| Byte hashes | Four research file hashes agree with the packet; final packet digest recorded above | No signed canonical receipt; sources themselves were not cryptographically authenticated |
| Artifact-only scope | Only six Markdown delivery files are included | Working generation scripts are excluded from the delivery |

An additional final pass rechecked the complete directory after receipt generation. External URLs are the inspected research routes recorded in the entries; no separate bulk URL liveness test or preservation of full copyrighted source bytes was performed. Relative paths require retaining the `topics/`, `patterns/` and `reviews/` layout.

## Tests explicitly not run

No participant playtest, prototype execution, studio telemetry analysis, energy measurement, independent source replication, actual Project-host retrieval test, cold/blind evaluation, canonical identity resolution or release action occurred. The ten Gate D cases in the packet are prepared specifications with no observed responses and no pass claims.

## Recovery use

Check these digests before resuming or comparing revisions. Retain the same conceptual candidate IDs; record a new candidate revision, predecessor digest and explicit supersession if submitted content is corrected. Check current coordination records before adding child work or allocating permanent IDs. This local receipt does not choose between competing canonical claims.

# Same-author assurance — game-agnostic candidate

This is an adversarial review by the same assistant with the same workspace permissions, not externally independent certification, human-approval authentication or a security sandbox. Baseline sources and the completed review batches are linked in SOURCE_INVENTORY.json. Functional changes are pinned at `72bf50263b39f9ccd236fb54ecae341c97f80125`.

## Findings resolved in the candidate
| ID | Severity | Evidence and correction |
|---|---|---|
| A-01 | Major | Recovered build fixture and parser disagreed on the result field. Explicit failed builds now FAIL; missing, malformed, cancelled, wrong-target and stale-output cases cannot pass. Actual parser regression tests retained. |
| A-02 | Major | Interrupted work left prose checkpoints ahead of implementation publication. The actual recovered code is now readable in GitHub, checked by exact directory identities; progress/evidence are committed in bounded batches. Old archive receipts remain historical. |
| A-03 | Major | An empty real-project targets seed violated its schema. It now explicitly remains UNCONFIGURED; preflight blocks unreconciled project facts. No synthetic approval enters a real project. |
| A-04 | Major | Regenerated common policy could drift across design and execution. The producer uses one pinned distribution, thin project artifacts, shared schema and distinct design/plan/acceptance subjects. |
| A-05 | Major | Personal-account GPT creation cannot be assumed. Deployment is separate from game installation; use an authorized existing test GPT or optional isolated Project pilot without replacing the live host. |
| A-06 | Major | Retaining a real-game overlay conflicted with the clarified game-agnostic goal. Removed it; moved source-named lessons outside deployed knowledge; supplied generic lessons and two explicitly synthetic contrasting profiles. |
| A-07 | Major | Preflight only recognized one old game's skill prefix. Replaced the special case with generic registry/review checks; unreviewed foreign skills and malformed registry block, explicitly reviewed extras survive. |
| A-08 | Major | The package checker could skip a missing new knowledge file not listed as a preserved reference. A negative test reproduced the false PASS; the corrected checker rejects it even in allow-unassembled mode. |
| A-09 | Moderate | Test receipts omitted Markdown inputs from their source map. The runner now hashes all source/document/manifest bytes outside generated evidence and caches; all six final maps agree. |
| A-10 | Moderate | Framework references use independent-persona and ACCEPT wording. Official instructions clarify lenses in one model and recommendations, never human approval. A duplicate authored evaluation ID was corrected before the final rerun. |

## Construction review disposition
All twenty-one design-source files and sixty legacy files have full recorded coverage; the large historical narrative remains selectively reviewed and is intentionally excluded from operational authority. All seven named external sources have bounded selected-source/current-notice dispositions. This is not an exhaustive vendor/transitive-dependency audit; no external runtime or catalog was adopted.

The functional package has 148 passing offline tests and strict 85-check validation after actual original-reference assembly. All eight functional directory identities matched the tested local bytes. Current artifact manifests distinguish this candidate from the old ZIP receipt. These results close the previous missing-reference and checkpoint-only-publication findings, not the separate live integration gates.

## Residual findings and pilot requirements
| ID | Severity | Remaining risk | Required action |
|---|---|---|---|
| R-01 | Major | Windows, launcher, Unity/C# helper, Codex and configured design host have not run here | Execute LOCAL_INTEGRATION_TEST.md and the 20 live method scenarios before production adoption. |
| R-02 | Major | The same account can edit code, hashes, baselines and claimed approvals | Human checks genuine approval sources and exact subjects/diffs; host permissions and separate review where warranted. |
| R-05 | Moderate | Full input hashing may create substantial disk I/O on a large Unity project | Measure first; narrow dependencies only with explicit coverage review. No token/latency savings percentage is claimed. |
| R-06 | Moderate | Windows child processes may survive parent cancellation; no Job Object containment | Inspect wrapper-owned children after interruption, never kill an existing user Editor. |
| R-07 | Moderate | Global/ancestor/ignored instructions and direct agent actions can bypass wrapper policy | Perform host instruction/permission review; wrapper controls only its own entry points. Registry review is not tamper-proof attestation. |
| R-08 | Moderate | Filename-based release scanning misses renamed/embedded capabilities | Inspect actual build assemblies, defines, runtime/network configuration and shipped artifacts. |
| R-09 | Moderate | Lexical neutrality and static prompt checks cannot prove live model behavior | Exercise cross-project, missing-resource, refusal, alternatives, reference-ACCEPT and human-pending cases. |
| R-10 | Moderate | No automatic cross-task migration service exists | Preserve old history; use explicit cancel/archive/new task and separate approval. |
| R-11 | Moderate | Remote design review cannot see local paths without transport | Upload or retrieve the bounded evidence bundle; missing evidence remains unavailable. |
| R-12 | Moderate | Same-user filesystem concurrency is not hostile-process containment | Use reviewed local checkouts; do not claim adversarial sandboxing or independent signatures. |

## Explicit exclusions and retained controls
No paid/API gateway, model fleet, vector service, automatic quota retries, whole external catalogs, automatic dependencies, speculative engine adapters, copied purchased assets, real-game defaults, live-GPT edit, merge or release. Approvals, required quality checks, Unity identity/lifecycle/serialization safety and human-only judgments are not relaxed to save tokens. Root guidance remains small; detailed design analysis stays upstream; Codex reads the approved slice and only relevant procedures/evidence.

R-03 (incomplete requested review) and R-04 (unpublished functional artifacts) from the historical report are closed within the bounded scope above; their old records remain available in Git history. Live compatibility and human adoption remain open, not waived.

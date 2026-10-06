# BH Unity Harness construction checkpoint

Status: SMALL-TASK EXECUTION QUEUE ESTABLISHED; candidate validation remains open. NOT adopted.
Repository: BH-Studio/boarshead-ai
Branch: harness/bh-standard-v1-20261004; PR #1 must remain draft and unmerged.
State reconciled from current GitHub records at: 2478e805a9d89196d5cc8097a77812d6e41b0eec.
Latest recorded functional/documentation batch: e37e103c6bbcac5de7dd771d7e1d56c5aa0867e6.
Prior recovery source: 7cec1860878abba4b20f38e1c48744f2f5a3472e.
The complete preceding checkpoint remains in commit 2478e805a9d89196d5cc8097a77812d6e41b0eec. This file changes the execution order and stopping discipline, not scope or historical evidence.

## Latest human instruction — governs continuation
Repeated responses failed. The human explicitly requested smaller tasks. Do ONE bounded subtask per response, then publish its actual result, update this checkpoint, read back the commit/diff and STOP. Do not interpret a bare Resume as permission to attempt the entire remaining build in one response.

For a test subtask, use one named module or a deterministic partition of at most 20 cases. Pin inputs and record exact case IDs, source hashes, command, raw output and exit status. A small case count is an authoring batch size, not a timeout guarantee or a weakened acceptance standard. Do not combine research, new integration code, full regression and final publication into one turn.

For a repair, address one demonstrated defect and its focused regressions; do not add neighboring features. A failed batch ends with actual failure evidence and a separate bounded repair item. Never fabricate a log from a summary. No unattended/background continuation is implied. Preserve complete required coverage across batches.

## Current repository state, not a new test result
Read UNITY_INCORPORATION_STATUS.md for UR-01 through UR-07 dispositions. The optional observation reducer/job runner, provider protocol, disabled configuration, Auditor procedure, conditional installed UNITY_PROCEDURES guide and authoring validator are already published. Preserve them; do not build them again.

Recorded prior results: 37 Unity observation cases in ten completed partitions; separately, 13 authoring tests and 56 authoring-subset checks. Evidence: review/evidence/unity-closure-20261005/VERIFICATION.md and AUTHORING.log. Exact logs were published at daaa413f90d26db1732908d63ab52f3b4da18bb4; verification identities at f0b0fae07c30c4d265f7209306f3c21dab74ef4b. These results were NOT rerun during the small-task planning update and do not establish the full revised suite.

Current recorded installation: 25 files and five core skills. Optional providers, job runner, reducer and Auditor skill are not auto-installed. Historical efficiency and older 148/136-test reports remain pinned evidence, not current full-suite proof.

## Bounded work queue
Each lettered subtask below is a separate response/commit boundary. Update its status and exact continuation when executed; do not silently advance to its neighbors.

| ID | Status | Scope and stopping point |
|---|---|---|
| B00 | State read; queue authored | Read current branch, checkpoint, incorporation status and PR metadata. Publish this queue and verify the resulting single-file diff. No implementation or test execution. |
| B01 | COMPLETE — PASS, 25/25 identities | Inspect PACKAGE_FILES.json at the current head; reconcile and hash-check only its 25 installed files. Record exact missing/mismatched paths. If retrieval itself needs splitting, checkpoint the remaining paths rather than start tests with mixed versions. No runtime changes. |
| B02a | COMPLETE — PASS, 20/20 runtime cases | Current runtime inputs reconciled; 84 cases rediscovered; first lexical partition only passed. Exact roster and raw evidence in review/evidence/small-tasks/B02a/. No runtime changes. |
| B02b | COMPLETE — PASS, 20/20 runtime cases | Current inputs and discovery match B02a; second committed partition passed. Exact source/case identities and raw evidence in review/evidence/small-tasks/B02b/. No runtime changes. |
| B02c-e | PENDING — 44 runtime cases | Follow the committed B02a/PARTITIONS.json roster: 20, 20 and 4 cases, one partition per response. Reconcile current inputs before each run; earlier partition evidence requires identical source hashes or explicit revalidation. |
| B03 | PENDING | Current installer module: the recorded 20 cases, exact inputs and raw evidence only. Split further if an observed failure needs repair. |
| B04a-c | PENDING | Current efficiency views (recorded 11 cases), then efficiency runtime (recorded 21 cases split into two partitions). One module/partition per response. |
| B05a+ | PENDING | Reconcile required exact knowledge/reference/tool bytes in small named-file batches, then run test_package.py, test_game_agnostic.py and test_review_amendments.py separately, splitting any module over 20 cases. Recorded total is 44; do not treat it as an observed current pass. |
| B06a-b | PENDING | First reconcile operating/consumer guidance and related manifests; separately reconcile design setup/knowledge consistency. Small related-file batches only. Preserve original design method and avoid repeating completed source research. |
| B07a+ | PENDING | Strict assembled-package checks and final regression coverage ledger on pinned final inputs. Revalidate earlier evidence against final input hashes; rerun affected/stale/missing partitions, including observation/authoring modules when required. Never sum incompatible historical runs into a full-suite claim. |
| B08 | PENDING | Final candidate tree/manifests and complete scope diff; current verification/assurance record and PR metadata/readback. No new functionality in this task. Keep PR draft. |

If an item requires more than its stated scope, write a smaller child item and stop at the recoverable boundary. A mere plan/checkpoint commit never counts as implementation or a passed check.

## B01 actual result — 2026-10-06 UTC
Installed-file identities validated at current input head 115718aaba62f505b20771b1455cba64540c0de5 (not a historical verification claim). PACKAGE_FILES.json blob c3408ece30947c8f520c82522fa08da0f3376282; project-template tree e35bbdcc31970eb82b273e587b6ca6373764aee1. All 25 declared files matched their manifest SHA-256, pinned Git blob SHA and byte length. Missing, mismatched, duplicate and extra installed paths: none. Check command exited 0. Actual evidence: review/evidence/small-tasks/B01/RESULT.json, RAW.log, validate.py and README.md. No runtime tests or B02 work performed; runtime, design and installation content unchanged. PR #1 was confirmed open, draft and unmerged. This evidence/checkpoint commit requires publication readback; it is not full-suite proof or adoption.

## B02a actual result — 2026-10-06 UTC
Pinned input head 601767bc8d9d6914dbea2f8c93c93cab921433fe. All 30 required runtime-source files reconciled against the current tree; source hashes matched before and after execution. Runtime discovery observed 84 distinct case IDs (no change); sorted full IDs were partitioned 20/20/20/20/4. B02a's first 20 tests passed, zero failures/errors/skips, 9.922 seconds, actual exit status 0. Exact evidence: review/evidence/small-tasks/B02a/SOURCES.json, PARTITIONS.json, DISCOVERY.log, RAW.log, RESULT.json and executed helper scripts. Remaining 64 runtime cases and other modules NOT_RUN in this batch. No runtime/design/package implementation changes; synthetic fixtures only. PR #1 remains required draft/unmerged; adoption PENDING. Publication requires commit/diff and evidence readback.

## B02b actual result — 2026-10-06 UTC
Pinned input head 4beef224bdf4ab8446ba257b957f55b67bb6ec3b. All 30 required source identities match both the current tree and B02a's ledger, and matched again after execution. Discovery remained 84 cases with the identical committed partition roster. Only B02b's 20 assigned runtime tests ran: 20 passed, zero failures/errors/skips, 2.924 seconds, actual exit status 0. Evidence: review/evidence/small-tasks/B02b/SOURCES.json, RECONCILIATION.json/.log, PARTITIONS.json, DISCOVERY.log, RAW.log, RESULT.json and executed discovery/runtime helpers. B02c-e and other modules NOT_RUN in this batch. Runtime/design/package sources unchanged; synthetic fixtures only. PR #1 was confirmed open, draft and unmerged; adoption remains PENDING. Publication requires commit/diff and evidence readback.

## Exact next action
B02c ONLY, in the next response: recheck the branch head, reconcile all 30 required input identities against review/evidence/small-tasks/B02a/SOURCES.json (B02b confirmed identical identities), and preserve the exact roster in B02a/PARTITIONS.json. Run only its B02c partition (20 IDs, beginning test_runtime.RuntimeTests.test_manual_not_automated and ending test_runtime.RuntimeTests.test_preflight_no_writes). Existing evidence runners are fixed to their own partitions; explicitly select B02c in a separate evidence helper, without changing harness/test sources. If inputs or discovery differ, record the change and assess evidence compatibility before execution; do not silently reuse stale evidence or shift partition membership. Save exact inputs/case IDs, command, raw output and exit status under review/evidence/small-tasks/B02c/. Update this checkpoint, commit/read back the diff, then stop. Do not run B02d or another module in that response.

The previous local path /mnt/data/bh-resume-20261005/BH-Unity-Harness is untrusted until its existence and bytes are checked. It was not a complete current authoring checkout. Old archives may supply unchanged bytes only when exact current hashes agree; unavailable content must be retrieved, not reconstructed from summaries.

## Remaining scope and limits
Native Unity/Pipeline/MCP provider mapping is NOT_IMPLEMENTED/configured. The BH provider protocol is not a native Unity command and fixture success is not a usable live integration. Author a mapping only from actual host command/result discovery in a separately scoped pilot. Historical status/return validates prior observations, not continuous live state.

Content-preserving checkpoint-commit continuation and machine-declared prerequisites remain explicitly deferred/NOT_IMPLEMENTED for v1 per UNITY_INCORPORATION_STATUS.md. Strict HEAD matching and approved ordered fail-fast staging remain. Do not claim those savings delivered, or silently waive their review. Stable reviewed runners versus mutable tests/data remain the supported pattern; changed executables still require review.

Windows/PowerShell, actual Unity/C# helper, native Codex, configured design GPT/Project, player validation and billed-credit comparisons remain NOT_RUN. Human adoption PENDING. These host-specific tasks are distinct from B01-B08, which are candidate construction/validation.

## Publication and recovery rules
All writes remain under BH-Unity-Harness. Preserve original directories, existing Readme.md, historical evidence and intervening contributor work. Recheck head and current file SHA before writes, never force-push, and verify the actual resulting commit/diff. Do not claim a server-side lease not provided by a successful operation.

No live game/GPT changes, installation, dependency purchase, paid spend, repository security change, merge or release. Keep this construction checkpoint outside the game-installed task state. Progress summaries must distinguish published code, source review, tests actually run, live integration and human adoption.

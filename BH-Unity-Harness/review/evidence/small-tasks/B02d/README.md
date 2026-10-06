# B02d — runtime partition 4

PASS: 20 tests, zero failures/errors/skips, exit status 0, 4.053 seconds. Only the committed B02d partition ran. B02e and other modules were not executed in this batch.

Pinned input head: `dbd55165c72f9ed1682d6ee08f0799249791aa35` on `harness/bh-standard-v1-20261004`. BUILD_CHECKPOINT.md was read first and pinned again after the head check. PR #1 was confirmed open, draft and unmerged.

All 30 required source files matched the current GitHub tree and committed B02a/SOURCES.json ledger: SHA-256, Git blob identity and byte length. Existing B02a local bytes were used only after these current checks. SOURCES.json records the current head and identities; RECONCILIATION.json/.log preserve actual reconciliation and ledger/roster provenance. No recovery archive or historical game defaults were applied.

Discovery from test_runtime.py alone observed 84 cases, with a complete logical roster identical to committed B02a/PARTITIONS.json before test execution. PARTITIONS.json preserves that roster; DISCOVERY.log lists discovery without executing cases. Membership is unchanged.

The separate run_partition.py changes the committed B02c helper only to select/name B02d and identify B02e as remaining scope. discover.py is unchanged. Harness, fixture, runtime-test, package and design sources were not edited.

Actual commands (reconciliation from /workspace/scratch/301f3dd0656a; discovery/run from `/workspace/scratch/301f3dd0656a/b02d-work`):

```sh
python3 reconcile_b02d.py > b02d-reconciliation.log 2>&1
python3 discover.py > DISCOVERY.log 2>&1
python3 run_partition.py > RAW.log 2>&1
```

Each exited 0. Reconciliation checked/copied exact current inputs and prepared the helper; it ran no tests. The rediscovered roster was compared with the committed roster and matched before runtime execution. RAW.log is exact combined process output. RESULT.json records selected case IDs, actual results/timing, environment identities and unchanged source hashes before and after execution.

For reproduction, retrieve all source paths from SOURCES.json at the pinned head into a BH-Unity-Harness subdirectory next to the evidence scripts/JSON files. Run discovery and compare the complete roster to committed B02a/PARTITIONS.json; then run the helper, fixed to B02d, which rejects source changes before its 20-case execution. Reconcile retrieved identities against the pinned GitHub tree and the committed source ledger; the scratch input envelope is not needed for the runtime command.

This is offline synthetic-fixture evidence from temporary local Git projects. Native Unity/Windows, real human approval and adoption were not performed. Earlier compatible source identities do not establish a full-suite result. Publication is limited to this evidence directory and BUILD_CHECKPOINT.md; recheck current head/checkpoint before non-force publication, then read back the actual commit/diff, evidence/checkpoint bytes and PR state.

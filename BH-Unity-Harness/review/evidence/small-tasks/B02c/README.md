# B02c — runtime partition 3

PASS: 20 tests, zero failures/errors/skips, exit status 0, 3.593 seconds. Only the committed B02c partition ran. B02d-e and other modules were not executed in this batch.

Pinned input head: `f82fefb137c2d58211008384905279c2e6fbf031` on `harness/bh-standard-v1-20261004`. BUILD_CHECKPOINT.md was read first and pinned again after checking the head. PR #1 was confirmed open, draft and unmerged.

All 30 required source files matched the current GitHub tree and committed B02a/SOURCES.json ledger (SHA-256, Git blob identity and byte length). Existing B02a local bytes were reused only after current identity checks. SOURCES.json records this batch's head and identities; RECONCILIATION.json/.log record the actual reconciliation and prior ledger/roster identities. No recovery archive or historical game defaults were applied.

Discovery from test_runtime.py alone still observed 84 cases, and the complete logical roster equaled committed B02a/PARTITIONS.json before execution. PARTITIONS.json retains that exact roster; DISCOVERY.log records discovery without running cases. Case membership remains unchanged.

The separate run_partition.py changes the committed B02b helper only to select/name B02c and identify B02d-e as the remaining scope. discover.py is unchanged. Harness, fixture, runtime-test, package and design sources were not edited.

Actual commands (reconciliation from /workspace/scratch/301f3dd0656a; discovery/run from `/workspace/scratch/301f3dd0656a/b02c-work`):

```sh
python3 reconcile_b02c.py > b02c-reconciliation.log 2>&1
python3 discover.py > DISCOVERY.log 2>&1
python3 run_partition.py > RAW.log 2>&1
```

Each exited 0. Reconciliation checked/copied exact current inputs and prepared the helper; it executed no tests. RAW.log is exact captured combined runtime output. RESULT.json records all selected IDs, actual outcomes/timing, environment identities and unchanged before/after hashes for all 30 files.

For reproduction, retrieve all paths in SOURCES.json from the pinned head into a BH-Unity-Harness subdirectory next to these scripts and JSON files. Run discovery and compare its roster to the committed B02a roster, then run the separate helper, which is fixed to B02c and rejects changed sources before its 20-case execution. Input reconciliation is reproducible by comparing recorded blob identities/sizes with the pinned tree and hashing retrieved files; no scratch input envelope is required for the runtime command.

This evidence concerns offline synthetic fixtures and temporary local Git projects. Native Unity/Windows, real human approval and adoption were not performed. Compatible prior source identities do not turn this 20-case result into a full-suite claim. Publication changes only this evidence directory and BUILD_CHECKPOINT.md; recheck the head/checkpoint before non-force publication and read back the resulting commit/diff, file contents and PR state.

# B02b — runtime partition 2

PASS: 20 tests, zero failures/errors/skips, exit status 0, 2.924 seconds. Only the committed B02b partition ran. B02c-e and other modules were not run in this batch.

Pinned input head: `4beef224bdf4ab8446ba257b957f55b67bb6ec3b` on `harness/bh-standard-v1-20261004`. Read BUILD_CHECKPOINT.md first; current checkpoint and PR state were then pinned/rechecked. PR #1 was open, draft and unmerged.

All 30 required input files matched the current GitHub tree and the committed B02a/SOURCES.json ledger, including SHA-256, Git blob identity and byte length. Existing B02a local bytes were used only after those current checks; no recovery archive was applied. SOURCES.json identifies this batch's current input head and all exact inputs. RECONCILIATION.json and RECONCILIATION.log retain the actual reconciliation result, prior ledger/roster identities and helper provenance.

Discovery from test_runtime.py alone observed 84 cases, and its complete logical partition roster equaled the committed B02a/PARTITIONS.json. No cases ran during discovery. PARTITIONS.json retains that exact roster. DISCOVERY.log is actual discovery output; listing a case does not mean it passed in this batch.

The separate run_partition.py evidence helper changes the committed B02a helper only to select/name B02b and describe the remaining scope as B02c-e. discover.py is unchanged from B02a. No harness, fixture, runtime test or design implementation source was edited.

Actual commands (reconciliation from /workspace/scratch/301f3dd0656a; discovery/run from `/workspace/scratch/301f3dd0656a/b02b-work`):

```sh
python3 reconcile_b02b.py > b02b-reconciliation.log 2>&1
python3 discover.py > DISCOVERY.log 2>&1
python3 run_partition.py > RAW.log 2>&1
```

Each exited 0. The reconciliation command only checked/copied exact current inputs and prepared the helper; it ran no tests. Before test execution, the rediscovered roster was compared to the committed roster and found identical. RAW.log is the exact captured combined runtime output. RESULT.json records selected case IDs, actual outcomes/timing, environment identities and unchanged before/after hashes for all 30 files.

For reproduction, retrieve all paths listed in SOURCES.json from the pinned input head into a BH-Unity-Harness subdirectory next to the evidence scripts/JSON files. Run discovery and compare PARTITIONS.json to the committed roster; then run only run_partition.py, which is fixed to B02b and rejects source identity changes before executing its 20 selected cases. Reconciliation can be independently repeated by comparing each recorded Git blob identity/length to the pinned GitHub tree and hashing each local file; no scratch input envelope is required for the test run.

Evidence applies to offline synthetic fixtures, local Python and temporary Git repositories. Native Unity/Windows integration, real human approval and adoption remain separate and not performed. Earlier B02a evidence has identical source identities, but this record claims only B02b's executed cases. No full-suite result is inferred.

Publication is limited to this evidence directory and BUILD_CHECKPOINT.md. Current head/checkpoint SHA were checked before writes. Publish as a non-force child of the pinned head and verify the resulting diff, evidence/checkpoint contents and draft/unmerged PR state.

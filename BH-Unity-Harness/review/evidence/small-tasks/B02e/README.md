# B02e — runtime partition 5

PASS: 4 tests, zero failures/errors/skips, exit status 0, 0.681 seconds. Only B02e's four assigned cases ran; B03 and other modules were not executed.

Pinned input head: `b2fa3ad47cfd36a58b91227c594f512dfd50c5ab` on `harness/bh-standard-v1-20261004`. BUILD_CHECKPOINT.md was read first and pinned again after checking the head. PR #1 was confirmed open, draft and unmerged.

All 30 required source files matched the current GitHub tree and committed B02a/SOURCES.json ledger: SHA-256, Git blob identity and byte length. Existing B02a local bytes were used only after current checks. SOURCES.json records current input identities; RECONCILIATION.json/.log preserve actual reconciliation and ledger/roster provenance. No recovery archive or game-specific defaults were applied.

Discovery from test_runtime.py alone observed 84 cases, with a complete logical roster identical to committed B02a/PARTITIONS.json before execution. PARTITIONS.json preserves that roster, while DISCOVERY.log records discovery without running cases. The four selected IDs are recorded in RESULT.json and RAW.log.

The separate run_partition.py changes the committed B02d helper only to select/name B02e and describe other modules as NOT_RUN. discover.py is unchanged. Harness, fixture, runtime-test, package and design sources were not edited.

Actual commands (reconciliation from /workspace/scratch/301f3dd0656a; discovery/run from `/workspace/scratch/301f3dd0656a/b02e-work`):

```sh
python3 reconcile_b02e.py > b02e-reconciliation.log 2>&1
python3 discover.py > DISCOVERY.log 2>&1
python3 run_partition.py > RAW.log 2>&1
```

Each exited 0. Reconciliation checked/copied exact current inputs and prepared the helper; it executed no tests. The rediscovered roster was compared to the committed roster and matched before test execution. RAW.log is actual combined process output. RESULT.json records exact case IDs, actual outcomes/timing, environment identities and unchanged source hashes before/after execution.

For reproduction, retrieve all source paths in SOURCES.json from the pinned head into a BH-Unity-Harness subdirectory next to these evidence scripts/JSON files. Run discovery and compare its complete roster with committed B02a/PARTITIONS.json; then run the helper, fixed to B02e, which rejects source changes before its four-case execution. Input identities can be reconciled independently against the pinned GitHub tree and prior source ledger; no scratch envelope is needed for the runtime command.

This is offline synthetic-fixture evidence from temporary local Git projects. Native Unity/Windows, real human approval and adoption were not performed. The individual B02a-e records remain their own pinned executions; final assembled-package coverage/freshness reconciliation belongs to B07 and is not waived by this four-case result. No full-candidate suite claim is made.

Publication is limited to this evidence directory and BUILD_CHECKPOINT.md. Recheck the current head/checkpoint before non-force publication; read back the actual commit/diff, all evidence/checkpoint bytes and the draft/unmerged PR state. B03 remains a separate response boundary.

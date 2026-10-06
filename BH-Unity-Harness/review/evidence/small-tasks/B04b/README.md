# B04b actual efficiency runtime evidence

Input: BH-Studio/boarshead-ai, branch harness/bh-standard-v1-20261004, head 6b97fcf47b6fdc848b508d244f19cab9e062bec7.

All 30 inputs matched the immutable current Git tree: the complete 25-file installed template, PACKAGE_FILES.json, installer/install.py (imported by support), tests/support.py, tests/fixture_driver.py and tests/test_efficiency_runtime.py. The manifest roster and all 25 SHA-256 values also matched. SOURCES.json records exact Git blob identities, byte lengths, SHA-256 and retrieval/reuse provenance. RECONCILIATION.json and its raw log record the actual source check; COMMANDS.json records actual shell commands and returned exit statuses.

Discovery observed 21 distinct case IDs, unchanged from the historical count. PARTITIONS.json and DISCOVERY.log contain the complete current roster and deterministic lexical partitions of 20/1. Only B04b ran: 20 passed, zero failures/errors/skips, 15.315 seconds, exit 0. B04c's remaining case, test_efficiency_runtime.EfficiencyRuntimeTests.test_user_pause_not_bypassed_by_repair, was NOT_RUN. RAW.log is captured stdout/stderr; RESULT.json records exact selected IDs, timestamps, environment and matching before/after source fingerprints. No failure repair was needed.

The fixtures are synthetic. Other modules, Windows/PowerShell, native Unity/C#, native Codex, design-host/player checks and billed-credit comparisons were NOT_RUN. This batch is not full-candidate verification or human adoption. PR #1 must remain draft and unmerged.

To reproduce B04b, obtain each source at the pinned input commit and arrange it under BH-Unity-Harness/ beside these evidence helpers. Verify SOURCES.json; run `python3 discover.py > DISCOVERY.log 2>&1`, then `python3 run_partition.py > RAW.log 2>&1`. The runner selects only B04b's exact IDs, with a maximum of 20. prepare_b04b.py records actual materialization/reconciliation and expects the original GitHub export b04b-input.json plus the existing local cache; reuse is accepted only after current Git blob and byte-length checks. No old archive was restored.

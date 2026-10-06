# B04a actual efficiency views evidence

Input: BH-Studio/boarshead-ai, branch harness/bh-standard-v1-20261004, head 99b8b07cb43940a7e5f065dfea66002dda8b62bb.

All 30 inputs matched the immutable current Git tree: the complete 25-file installed template, PACKAGE_FILES.json, installer/install.py (imported by support), tests/support.py, tests/fixture_driver.py and tests/test_efficiency_views.py. The manifest roster and all 25 SHA-256 values also matched. SOURCES.json records exact Git blob identities, byte lengths, SHA-256 and retrieval/reuse provenance. RECONCILIATION.json and its raw log record the actual source check; COMMANDS.json records actual shell commands and returned exit statuses.

Discovery observed 11 distinct views case IDs, unchanged from the historical count. PARTITIONS.json and DISCOVERY.log contain the complete current roster. Only the one B04a partition ran: 11 passed, zero failures/errors/skips, 4.284 seconds, exit 0. RAW.log is the captured stdout/stderr; RESULT.json records exact IDs, timestamps, environment and matching before/after source fingerprints. No failure repair was needed.

The checked fixtures are synthetic. Efficiency runtime, other modules, Windows/PowerShell, native Unity/C#, native Codex, design-host/player checks and billed-credit comparisons were NOT_RUN. This batch is not full-candidate verification or human adoption. PR #1 must remain draft and unmerged.

To reproduce test execution, obtain each source at the pinned input commit, arrange it under BH-Unity-Harness/ beside these evidence helpers, verify SOURCES.json, and run `python3 discover.py > DISCOVERY.log 2>&1` followed by `python3 run_partition.py > RAW.log 2>&1`. prepare_b04a.py records actual materialization/reconciliation and expects the original GitHub export b04a-input.json plus the existing local cache; reuse is accepted only after current Git blob and byte-length checks. No old archive was restored.

# B03 — current installer module

PASS: all 20 discovered installer tests, zero failures/errors/skips, exit status 0, 1.631 seconds. The count matches the historical 20; B04 and other test modules were not run.

Pinned input head: `c24f1b08a0001c91983c47d7d191a3f9c8df5926` on `harness/bh-standard-v1-20261004`. BUILD_CHECKPOINT.md was read first and pinned again after the head check. PR #1 was confirmed open, draft and unmerged.

## Exact input scope
29 files were reconciled against this head: all 25 installed project-template files, PACKAGE_FILES.json, tests/test_installer.py, tests/support.py and installer/install.py. The module was inspected to identify these inputs. support.py imports the real runtime and installer; the installer reads the manifest and every declared installed file. Runtime test cases and fixture_driver.py are unused by this module and were excluded. All three current Python sources were fetched at the pinned head. Prior fetched installed/manifest bytes were reused only after current Git blob/size and SHA-256 checks; no archive or historical game defaults were applied.

SOURCES.json records exact paths, provenance and identities. Reconciliation also confirmed the complete 25-file manifest roster and declared hashes. RECONCILIATION.json/.log preserve that actual check. Source hashes matched again after execution.

## Actual commands and evidence
From /workspace/scratch/301f3dd0656a:

```sh
python3 prepare_b03.py > b03-reconciliation.log 2>&1
```

From `/workspace/scratch/301f3dd0656a/b03-work`:

```sh
python3 discover.py > DISCOVERY.log 2>&1
python3 run_partition.py > RAW.log 2>&1
```

All three exited 0. Preparation verified already-retrieved input files and manifest consistency, without running tests. Discovery loaded only test_installer.py and observed 20 exact IDs. PARTITIONS.json preserves that sorted roster; the runner executed only B03. RAW.log is actual combined runtime output. RESULT.json records case IDs, actual outcomes/timing, environment identities and all 29 before/after fingerprints.

The evidence helpers are published as executed; run_partition.py changes the previously committed B02e helper only to select/name B03 and describe installer scope. They are outside the installed harness. To reproduce the test run, retrieve each path from SOURCES.json at the pinned head into a BH-Unity-Harness subdirectory next to SOURCES.json, PARTITIONS.json and the discovery/runner scripts. Run discovery, confirm its exact roster, then run the B03 helper. It rejects changed source bytes before execution. For preparation reproduction, the recorded layout has prepare_b03.py and b03-input.json next to b03-work; the input JSON requires only head and harness_tree from the pinned GitHub commit/tree, while b03-work contains the retrieved package and evidence JSON files.

Destinations were temporary Git repositories visibly marked SYNTHETIC. The tests exercised approval/hash rejection, preview without writes, conflict preservation, explicit manual merge, fresh/repeated installation, active-task/writer-lock boundaries and rollback preservation. No real game installation, native Unity/Windows integration, real human approval or adoption occurred. No implementation files changed and no full-candidate suite result is claimed.

Publication is limited to this evidence directory and BUILD_CHECKPOINT.md. Recheck head/checkpoint before non-force publication, then read back the actual diff, evidence/checkpoint bytes and draft/unmerged PR state. B04a is a separate response.

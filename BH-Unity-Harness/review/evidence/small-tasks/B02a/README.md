# B02a — runtime partition 1

PASS: 20 tests run, zero failures/errors/skips, exit status 0, 9.922 seconds. This is the first runtime partition only; remaining 64 runtime cases and other modules were not executed.

Pinned input head: `601767bc8d9d6914dbea2f8c93c93cab921433fe` on `harness/bh-standard-v1-20261004`. Checkpoint was read first and pinned again after checking the branch. PR #1 was open, draft and unmerged.

## Input reconciliation
SOURCES.json records SHA-256, Git blob identity and byte size for all 30 source files: all 25 project-template files, PACKAGE_FILES.json, test_runtime.py, support.py, fixture_driver.py and installer/install.py. support.py imports the installed runtime and installer; fixtures copy the full installed template and generate visibly synthetic task/approval/observation data. No installer test module was run.

The 25 template files and manifest used already-fetched B01 bytes only after recomputing their Git blob hashes and sizes against the current head's tree. The test/support/driver/installer bytes were fetched from current immutable GitHub blobs. All local files matched those current identities before execution, and all 30 matched again afterward. No recovery archive or old authoring checkout was applied. A repository-wide recursive tree retrieval returned a transport error; the smaller root and harness trees succeeded (harness truncated=false). No missing input was reconstructed.

## Discovery and execution
Full unittest case IDs were rediscovered from test_runtime.py only: 84, unchanged from the historical count. No test ran during discovery. Unicode lexical ordering of full IDs defines the committed PARTITIONS.json roster: B02a=20, B02b=20, B02c=20, B02d=20, B02e=4. Only B02a ran; the roster does not claim other partitions passed.

Executed from `/workspace/scratch/301f3dd0656a/b02a-work`:

```sh
python3 discover.py > DISCOVERY.log 2>&1
python3 run_partition.py > RAW.log 2>&1
```

Both commands exited 0. discover.py and run_partition.py are the exact executed evidence helpers, separate from harness implementation. RAW.log is actual combined process output, not a reconstructed summary. RESULT.json records selected IDs, observed results, interpreter/platform/Git identities and before/after source fingerprints. SOURCES.json records retrieval provenance. PARTITIONS.json and DISCOVERY.log retain the complete discovered roster without executing the remaining cases.

For reproduction, retrieve the 30 exact repository paths in SOURCES.json from the pinned head into a BH-Unity-Harness subdirectory next to the helpers and JSON files. Run the two commands above; the runner rejects changed source bytes before running any selected case. It is deliberately fixed to B02a and must not be reused as B02b without an explicit bounded partition-selection revision.

Synthetic fixtures use temporary Git repositories and local Python subprocesses; no real Unity project, native integration, real human approval, paid/API spend or adoption is claimed. Runtime/design/package implementation files remain unchanged. This publication changes only B02a evidence and BUILD_CHECKPOINT.md. Branch head and checkpoint blob were rechecked before writes. Ref update must be non-force; final commit/diff, all evidence bytes and PR state are read back after publication.

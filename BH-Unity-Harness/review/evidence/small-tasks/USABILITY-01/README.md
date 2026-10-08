# USABILITY-01 — optional Git and plan approval without pasted hashes

Authorized scope: the human's two explicit requests in the current BUILD_CHECKPOINT. Input main head: 2e4b5603ba3fd2d03dd1a9ef7c64cd8afc083bfe. Preserve intervening Installer improvements; no live project or Unity integration changes.

Git is optional throughout project installation and runtime. When unavailable, filesystem/content snapshots provide real input identities; commit=null means no Git revision is observed, dirty=true does not assert VCS cleanliness, and .gitignore is not applied in filesystem mode. Unity caches and BH journals are excluded before traversal. Unsafe paths/links, stale inputs and out-of-scope changes remain blocked. Switching snapshot modes requires reconciliation/replanning because the roster can change.

After actual human approval of the current reviewed plan, use `approve --by NAME --source REFERENCE`. The harness generates the correlated approval record internally; the human does not paste a hash or create JSON. It does not authenticate a person or fabricate consent. Legacy approval records and separately reviewed human acceptance remain supported.

SOURCES.json pins 125 current input blobs. TESTED_INPUTS.json records the actual staged source fingerprints, unchanged throughout execution. The checkpoint and new evidence are publication records authored after the tests; they do not change executable/package inputs. PARTITIONS.json contains 257 distinct case IDs in at-most-20 module partitions. Every .log is actual stdout/stderr with exit code; COMMANDS.json records the exact commands and durations. RESULT.json contains the observed totals, 88 package checks and 56 authoring checks. VERIFY.txt is the actual executed helper. INITIAL_FAILURE.md retains the earlier unsynchronized-manifest failure excerpt and its disposition.

The regression suite uses Git to exercise its optional Git-backed fixtures; new tests exercise runtime without a repository and with Git discovery disabled. These Linux/synthetic/process results do not establish Windows/Unity/CLI/host compatibility. No historical reports are substituted for current results.

Publish one non-force commit using the pinned base tree and expected main head. Verify every changed/new file and the exact final diff. Stop; do not begin B06 or a native Unity integration.

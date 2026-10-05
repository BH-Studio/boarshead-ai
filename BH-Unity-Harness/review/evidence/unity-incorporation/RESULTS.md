# Actual Unity-incorporation offline checks — 2026-10-05

This code batch was tested on Linux/Python 3.13.5. Native Windows/Unity/Codex/provider integration was NOT_RUN.

Completed modules: 37 new Unity observation tests, 84 unchanged runtime tests and 20 unchanged installer tests: **141 distinct cases**, zero failures/errors/skips. Recorded runner time totals 121.313 seconds. This is not a complete revised-package suite and does not add historical 148/136 results.

The 37 published Unity cases ran in one completed module invocation (runner time 90.931s; unittest log 90.929s). `unity-tests.log` is the actual raw log. A prior same-module attempt was interrupted by the container deadline, followed by a completed ten-part run of 37 cases. A subtest display key was then shortened from operation to op; all 37 tests reran on the final published test bytes. No runtime behavior changed for that display correction. Failed/interrupted attempts are retained locally for supplemental evidence, not reported as passed runs.

The existing runtime and installer modules ran as eight and four complete nonoverlapping partitions respectively. Their executable/schema/fixture inputs match this batch. Their wider source maps predate that single test-label edit; no identical-all-files fingerprint across the combined 141 cases is claimed. Their raw partition logs and JSON fingerprints still reside in /mnt/data/unity-resume/evidence/unity-existing pending consolidated evidence publication.

## Exact critical tested identities
| Artifact | Git blob |
|---|---|
| project-template/Tools/BH/bh.py | ca2bc04487a4cacba042bbbb9c8ff0bd9168a083 |
| All three canonical schema copies | 7b8276fc116ff0e40653b52c3fe71dc63baf1632 |
| optional/unity-observation/unity_jobs.py | 8f64e722acc78f9d9a0809b039ee8e333ed7ae57 |
| optional/unity-observation/unity_evidence.py | 548992178c51f51ffab74e82462aa281ce56d34a |
| tests/unity_provider_fixture.py | 30ede0cc41467c651615484cb104bbfa15f662c2 |
| tests/test_unity_observation.py | f93ed56464e458821f3e960f235fc28fae456cea |
| PACKAGE_FILES.json | fdd252c6259085a9d44edb1849839ec04fda7d2f |
| design-gpt/KNOWLEDGE_MANIFEST.json | b41bb46ac7a9e2c97d215256a64611d19c660d69 |

The per-run fingerprints cover the materialized consumer, optional, installer, contracts, tests and tools. They do not certify unmaterialized design resources or root manifests. Root manifest identities are separately listed above; all 24 installed-file hashes were validated, and generator output equals all three schema copies.

The synthetic provider is an actual subprocess emitting observations; the real parent harness constructs and audits its own receipt. Cases cover one submit/local bounded polling, every reducer, wrong job/session/project/run/request/capability identities, lost-submit ownership, timeouts without fictitious cancellation, incomplete coverage, empty/malformed data, actual source mutation and human acceptance remaining pending. No vendor script or Unity Editor was run.

Next: disabled setup/provider contract, on-demand Unity guidance, authoring checks, outstanding efficiency/package/design tests and consolidated publication assurance. The optional protocol is BH-UNITY-PROVIDER-1, not a claim that any installed Unity command already implements it.

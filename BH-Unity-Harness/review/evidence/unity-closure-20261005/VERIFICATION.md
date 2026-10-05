# Unity observation recovery verification — 2026-10-05

Actual run: 37 unique tests in `test_unity_observation`, ten completed nonoverlapping partitions, zero failures/errors/skips. Combined recorded runner time: 105.067414 seconds. Linux 6.18.44 / Python 3.13.5. Started 2026-10-05T14:35:32Z, completed 14:38:10Z. This is a named-module run, not a full package suite or a performance benchmark.

`RESULTS.log` concatenates the exact ten raw logs, adding only partition separators. SHA-256: `dd3cf309993b9fd4080fdee6651e047be9956fea8bf2d84d42cbaebae6145b49`.

## Actual tested source
The 24-file installed template was recovered and matched every entry of `PACKAGE_FILES.json` at source commit `7cec1860878abba4b20f38e1c48744f2f5a3472e`, manifest blob `fdd252c6259085a9d44edb1849839ec04fda7d2f`. Its SHA-256 is `15cbe4c96322447c657656ad7eb4d7bc8faa8335b85d4de0b379c7902ce9f132`.

| Additional execution input | Git blob |
|---|---|
| optional/unity-observation/unity_evidence.py | 548992178c51f51ffab74e82462aa281ce56d34a |
| optional/unity-observation/unity_jobs.py | 8f64e722acc78f9d9a0809b039ee8e333ed7ae57 |
| tests/test_unity_observation.py | f93ed56464e458821f3e960f235fc28fae456cea |
| tests/unity_provider_fixture.py | 30ede0cc41467c651615484cb104bbfa15f662c2 |
| tests/support.py | f857e634e084fa2ae50af13e337a69f6ab26696b |
| tests/fixture_driver.py | d664cf352242a661ac02e2ca2173819aaaa0815b |

Every partition recorded the same 35-file local fingerprint map and verified it unchanged after execution. That map includes some unused test files from the older archive; those unused files were NOT executed or claimed current. The named execution inputs and installed template above were checked against their actual current Git identities. No historical test count is added to this 37-case result.

## Observed boundaries
Actual subprocess fixtures exercise one submit/local polling, identity and scope validation, disabled/missing capability rejection, unknown reuse policy rejection, timeouts/lost responses and unresolved ownership, raw output limits, all five reducers, frozen Play-mode state, unsaved assets, missing localization, baseline deltas and source mutation. Human-only acceptance stays pending. These are visibly synthetic providers, not a Unity CLI mapping or an actual game.

The first four-way partition attempt was interrupted by the command deadline and is not counted as passing. Its partial log and the ten individual JSON/log pairs remain in the supplemental local evidence directory; they are not claimed individually committed here. No absent earlier-session receipt was reconstructed.

## Remaining
Complete provider/configuration and on-demand guidance, authoring checks and the outstanding efficiency/package/design regression modules. Windows, PowerShell, actual Unity, native Codex/MCP, configured design host, player validation and billed-credit comparisons remain NOT_RUN. Candidate adoption remains pending.

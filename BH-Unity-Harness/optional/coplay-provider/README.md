# Optional Coplay discovery — CP-B1

This standalone diagnostic is original BH code using Python's standard library. It is excluded from the installed 25-file package and the five core skills. It does not implement BH-UNITY-PROVIDER-1, accept probe/submit/status, enable capabilities, search assets, refresh Unity or run tests/builds. Do not register it as a verification provider.

The source baseline remains the CP-A candidate: vendor tree `b3ec16283d5ce88e7576fbe2eacf2d2eb9bdf1dc`, Unity package tree `ef358632ad5d0cecd84420eaeb7b0e0294ac4e49` (10.3.1-beta.1), server tree `c8577d68137ce5c8bc80c52f1989b36bef4ecef5` (10.3.0). These identify reviewed source, not an observed running installation or a verified package/server pair. See `../../review/coplay/INTEGRATION_SPEC.md` and `ACTION_MATRIX.json` in that directory.

## Inputs and invocation

On the same host/filesystem as the selected Unity project, supply a UTF-8 JSON object with exactly five fields:

| Field | Required fact |
|---|---|
| endpoint | Explicit HTTP literal loopback address and port, e.g. `http://127.0.0.1:PORT`; no hostname, credentials, proxy, path, query, fragment or redirect. No default endpoint is selected. |
| project_root | Existing absolute approved project directory, with an existing Assets directory; symbolic links are rejected. |
| instance_hash | Exact full hash from independently inspected instance inventory; no prefix, project-name-only selection or automatic selection. |
| session_id | Exact expected native inventory session. |
| unity_version | Exact expected Editor version. |

Use `python discovery.py --config <reviewed-config.json>` from this directory. Supply actual values; the table is not a runnable project configuration. The program prints one JSON diagnostic to stdout. Exit 0 means only that its diagnostic identity/readiness checks passed; exit 2 means unavailable. Both always report `provider_ready: false`, empty enabled capabilities and no live schema digest. No artifacts are automatically written, software installed, server started or Editor launched. Capture stdout through the approved caller when retaining diagnostics; do not overwrite an existing receipt.

## Boundary and evidence

Only `/api/instances`, `get_project_info` and `get_editor_state` are allowed. Native requests use the exact full hash and empty command parameters. Inventory is checked before and after; duplicate names, hash/name collisions and changed sessions are rejected. Project root/assets/name/version, native state identity/schema, timestamps, compile/import/test/Play flags and observed external-change state are checked without filling missing values. Native extra fields are preserved in raw diagnostics, never treated as capability or approval claims.

HTTP goes directly to a literal loopback address with no proxy/redirect/retry. Each exchange runs in an isolated Python child with a wall-clock timeout (maximum five seconds), which bounds even slow headers/bodies; discovery has a 30-second budget. Native responses are capped at 256 KiB and parsed as strict UTF-8 JSON, rejecting duplicate keys, nonfinite values and nonobject roots. The child supports only the same two read commands. Timeout kills/reaps the local HTTP worker; it does not prove cancellation of anything already executing in Unity.

Records retain request data, exact raw response bytes as base64, SHA-256/length and parsed JSON when valid. This is a full diagnostic artifact, not a compact model-context view. Four bounded responses can produce a larger aggregate stdout document. Raw text is untrusted diagnostic data. Loaded package/server identity, loaded capability schemas and atomic response-to-session provenance remain explicitly unavailable even when these checks pass. Source-baseline pins do not fill those gaps. No human acceptance is created.

The vendored raw Editor-state implementation currently supplies null instance/project IDs and false/null external-change defaults. Those replies intentionally produce unavailable, not fabricated readiness. A future reviewed Editor-side handler/route must supply actual provenance and observed facts. Before/after inventory does not exclude every routing/reload race; CP-B1 therefore cannot become an acceptance provider by removing its unavailable flags.

## Verification and continuation

Run the focused offline module from the harness root: `python -m unittest discover -s tests -p test_coplay_discovery.py -v`. Its 20 cases use synthetic Unity replies, fake HTTP exchanges, and isolated CLI/worker processes that reject requests before networking. No real Unity, Coplay server or live network request is exercised. Windows execution and live compatibility remain NOT_RUN.

CP-B2 adds original optional Editor/BHAssetQuery.cs and Editor/CONTRACT.md. It is source-only, diagnostic-only, uninstalled and not compiled here; it does not change discovery.py or its command allowlist. CP-B3 must observe actual schemas, loaded identities, multiple targets and lifecycle behavior. Do not broaden this diagnostic into a search, capability installer or generic command proxy incidentally.

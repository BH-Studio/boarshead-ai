# CP-B2 optional Editor asset query

`BHAssetQuery.cs` is original BH source, outside the installed package. It is not installed, compiled, registered as a BH provider, or enabled by this change. `AutoRegister=false` suppresses automatic FastMCP registration; it is not an authorization boundary for a native command dispatcher. Actual registration/routing must be demonstrated in CP-B3. Do not drop this file into an existing game as an implicit setup step.

The reviewed integration seam is the pinned Coplay `McpForUnityToolAttribute` and custom-tool `public static object HandleCommand(JObject)` shape. No vendor implementation was copied. Dependencies are UnityEditor/UnityEngine, Newtonsoft.Json and the pinned Coplay Editor assembly. No assembly definition, package installer or version resolution is supplied. C# compilation and loaded routing compatibility are NOT_RUN.

## Invocation contract

The handler accepts exactly one of these two shapes after the native transport has parsed JSON:

- `{"action":"describe"}` observes local identity and state; no asset query.
- `{"action":"search","expected_identity":{...},"spec":{...}}` performs one bounded diagnostic query. The five identity fields must exactly match a separately observed and approved target: `project_root`, `assets_root`, `unity_version`, `process_id`, `editor_domain_id`. Request values are comparisons, never the source of response identity.

The identity comes from Application.dataPath, Application.unityVersion, the current process ID and a local random domain identifier initialized by Unity. The domain identifier changes on domain reload; it is not Coplay's inventory session or authentication. No continuity across reload is asserted. CP-B3 must independently bind this identity to the native target/session, including two-target routing and reconnect races.

The spec has exactly the existing five BH search fields:

| Field | Supported value |
|---|---|
| query | One `t:TypeName` filter, optionally followed by one space and an ASCII name term. Type starts with a letter and contains letters/digits/underscore/dot; the optional term contains letters/digits/underscore/hyphen. Maximum 128 characters. No arbitrary expressions, wildcard, scope token or empty query. |
| provider | `unity-asset-database` |
| scope_paths | Exactly one existing, exact-case `Assets/...` subfolder. Assets itself, Packages, traversal, links/junctions, trailing slash and invalid folder are rejected. |
| properties | One to three distinct names from `name`, `fileName`, `isFolder`. `name` reads the main asset object's actual name; fileName uses its exact returned path. |
| max_items | Integer 1–25; over-budget candidate sets yield no partial result. |

The request object is limited to 8 KiB after compact serialization. Duplicate wire keys cannot be detected once a JObject exists: a future transport must reject duplicate keys/nonfinite JSON and enforce raw byte/depth limits before parsing. CP-B1's command allowlist remains unchanged and cannot call this handler.

## Result and limits

The native envelope is `BH-COPLAY-ASSET-QUERY-1`, not BH-UNITY-PROVIDER-1. It contains state/reason, observed before/after records when available, result, elapsed_ms and explicit unavailable facts. States are diagnostic_only, unavailable, busy or over_budget. Every response has provider_ready=false, enabled_capabilities=[], live_schema_digest=null. Errors contain no partial result and use fixed reason codes. Native transport wrapping/serialization overhead is outside the handler's compact 256 KiB envelope cap; the eventual transport must independently enforce its full wire cap.

The successful diagnostic result has query/provider/scope_paths/complete/total_count/items; items have id/kind/path/properties. Complete means only all candidates in that single synchronous AssetDatabase invocation. It is not disk freshness, a filesystem transaction, general search completeness or acceptance. Unknown test activity, pending reload, disk/import coherence, Coplay session binding and loaded capability/dependency identity remain explicit. Compile/import/Play/pause observations that are busy reject search. These checks do not establish full readiness.

Folder validity and folder GUID are checked in the same Editor-thread call as FindAssets, then checked again. Every candidate is counted before path/type/object inspection; over-budget sets are rejected without paging or loading. At most 25 main objects can be loaded, only when name is requested. GUIDs sort ordinally; paths are exact, unique by GUID and rechecked. Invalid types/records, changed identities and paths outside the scope invalidate the entire result. Scope/result paths and ancestors reject reparse points. External filesystem changes can still race these checks; no atomic filesystem snapshot is claimed.

No refresh, import, compile, save, scene change, preview generation or console clearing is explicitly requested. Loading main assets can nevertheless run project code/serialization callbacks or consume memory; CP-B3 must assess actual effects in the disposable target. GUID enumeration itself can allocate/work on a large index before its count is available. The 30-second checks are cooperative between synchronous Unity calls, not cancellation or a hard main-thread time/memory bound. A timed-out caller retains unresolved operation ownership and must not automatically replay.

## Validation and next gate

CP-B2 evidence records input hashes, a narrow source-policy inspection and actual tool availability. These are not executable C# tests, Unity compilation or behavior proof. Native C#/Unity/Windows execution is NOT_RUN. CP-B3 must compile the exact source in an approved disposable project and observe actual loaded dependencies, tool schema and routing before any adapter mapping can be authored or enabled.

Required host cases include describe/wrong root/version/process/domain, two targets, reload/reconnect, off-thread call, busy/unknown readiness, invalid/missing/linked/changed folder, 0/1/25/26 candidates, strict query/property/input types, duplicate/out-of-scope/unknown records, deterministic rows, requested name semantics, response byte limits, long query/lost reply and project side effects. Capture raw requests/responses, source hashes, host facts and limitations. Unknown acceptance gates remain unavailable; do not turn this diagnostic result into a receipt. Human approval, strict HEAD checks and design/implementation separation remain in the existing BH parent.

# CP-A — optional Coplay integration specification

Status: CP-A SPECIFIED; CP-B1 discovery-only adapter IMPLEMENTED with 20 offline cases passed; BH observation provider NOT_IMPLEMENTED; live compatibility NOT_RUN.
Accepted direction: human instruction "Proceed with your recommendations", 2026-10-06 UTC.
Scope: one conditional integration specification. ACTION_MATRIX.json is review metadata, not an executable configuration, skill registry or permission grant.

## Placement and authority

Use a small original BH adapter beneath existing handoff/proposal approval, scope, verification receipts and design-feedback review. Keep Coplay optional and outside the 25 installed files/five core skills. A future implementation belongs under optional/coplay-provider; do not load the vendor operator skill/catalog into ordinary task context. Human adoption and game-specific operations retain their existing approval subjects.

CP-A pins the reviewed development baseline, not a tested compatible release: Unity package 10.3.1-beta.1 at tree ef358632ad5d0cecd84420eaeb7b0e0294ac4e49 and Python server 10.3.0 at tree c8577d68137ce5c8bc80c52f1989b36bef4ecef5, together under vendor tree b3ec16283d5ce88e7576fbe2eacf2d2eb9bdf1dc in repository commit 4325d0e6a0eb39ffff219ded4629971d8467ce7a. Never install from a moving main/beta/latest reference. These package/server source pins do not pin Python transitive dependencies or prove a running host uses those bytes. A host pilot must record resolved dependency versions/hashes, actual Editor version, installation origins, executable/helper hashes and actual loaded capabilities.

## Transport and discovery contract

Prefer an existing verified connection. The first implementation is discovery-only; it must not return BH provider ready or advertise search until the following gates are demonstrated.

1. Read instance inventory; require an explicit approved project root and full instance selector. Reject no target, ambiguous matches, duplicate project names affecting native routing, unavailable target or unexpected session changes. Do not choose first/only by convenience.
2. Read actual project information and Editor state from that selected target. Compare canonical project root/assets root and exact Editor version to approved configuration. Reject empty/default identity fields. Record inventory session ID separately from any Editor-domain generation; a reconnect/reload cannot silently become the old approved session.
3. Require positive observed readiness, bounded source timestamp age, no pending compile/reload/import/test conflict, and the required loaded capability. Missing state is unavailable, stale state is unavailable, busy state is busy. A timestamp filled by the server is not an Editor observation. Disk changes not yet reflected in the AssetDatabase must be detected or reported unresolved; no implicit refresh is allowed.
4. Pin actual action/response schemas and source/version provenance. The source identities in ACTION_MATRIX.json are a static schema baseline only. A future capabilities_sha256 is computed from canonical observed capability descriptors plus reviewed mapping version and compared to the configured digest. Never compute it only from the expected request and echo it as discovery.
5. Bind native response provenance to the selected project/session. Revalidate before and after dispatch. Inventory plus a response without target/session identity is insufficient for acceptance if a routing/reload race cannot be excluded. Add a reviewed response wrapper or keep that capability unavailable; do not invent observed identity.

Candidate transport evaluation includes existing MCP resources and the local /api/instances + /api/command routes. The latter bypass Python MCP wrappers and expose different raw parameter/response shapes; they are not interchangeable. Do not shell out to the human CLI formatter and parse its progress text. Any local HTTP client must use an explicit approved loopback endpoint, disable redirects/proxies, bound request/response sizes and timeouts, and never follow response-controlled URLs. No automatic server launch, download, Editor launch, package install, authentication change or remote fallback. Selecting the route requires observed schemas, side-effect verification and host evidence.

## Initial capability and search mapping

The first candidate observation is project-asset metadata search, with one explicit Assets subfolder and a narrow literal approved AssetDatabase query. Scene hierarchy search, packages outside Assets, arbitrary predicates, previews, date filters, all-project discovery and automatic pagination remain outside the initial profile.

BH's existing search specification is exactly query, provider, scope_paths, properties, max_items. Its result is query, provider, scope_paths, complete, total_count, items; each item has id, kind, path, properties. Map only verified native GUID → id, assetType → kind, asset path → path, and explicitly requested scalar fields (initially name/fileName/isFolder). Reject absent/Unknown type, null rows, duplicate GUIDs, out-of-scope paths, non-scalar or unrequested fields. Query/provider/scope labels identify the invocation, not observations in their own right; retain the raw request and actual target/scope proof.

The vendored manage_asset(search) is NOT eligible as an unchanged acceptance provider:
- Python preflight can implicitly refresh/compile.
- C# SearchAssets falls back to the entire project if the folder is invalid.
- It constructs data for every matching asset before paging; a small page limits output, not Editor work.
- Native responses do not themselves provide all required BH target/session/scope provenance.

The live route therefore needs an original, reviewed, query-only Editor handler or another demonstrated existing route that meets the same requirements. Validate the folder atomically in that handler and reject invalid/changed scope without fallback. Count candidate GUIDs before loading asset records; reject over-budget queries and ask for a narrower scope rather than enumerate pages. Sort stable GUID/path identities, bound loaded records and capture target/session/readiness observations around the operation. AssetDatabase candidate enumeration itself may remain costly; a parent timeout is not proof that Unity stopped. Record elapsed work and preserve unresolved ownership on timeout. Never claim a hard interrupt or complete snapshot without evidence.

Proposed pilot ceilings (BH policy choices, not measured optimum): 25 returned/loaded records, one query, one folder, previews off, 256 KiB native JSON, 30-second total operation deadline, 5-second transport calls, 2-second maximum source-state age. Use the stricter approved binding limit. If legitimate host behavior needs another budget, revise/review the configuration explicitly. Do not silently broaden. An oversized/incomplete result cannot prove absence or satisfy the mandatory coverage_complete expectation. This initial profile returns completed only for a demonstrably complete bounded result.

## BH lifecycle and artifacts

Reuse BH-UNITY-PROVIDER-1 and unity_jobs.py. No schema edits, second scheduler or per-poll model turn. Probe verifies identity/readiness/capabilities and has no job/result. Submit occurs once. For synchronous queries, persist an adapter-owned local operation ID and journal before sending; it is not a claimed native Coplay job. Mark completed only after raw result capture, validation and provenance checks. Status may return the persisted same-operation result; it must not issue a new query. A lost response remains interrupted/unresolved, even for a read. The parent retains ownership and never interprets timeout as server cancellation.

Use the exact existing response fields/states from the pinned protocol/runner. Stdout is one bounded JSON object; diagnostic stderr is bounded. Persist only controlled regular direct-child files in the approved run directory: discovery.json, native-request.json, native-response.json and adapter-operation.json, each size-bounded and hashed. The adapter-operation record binds the request digest, local operation ID, native session, schema digest, transport, timestamps and artifact digests. Exclude secrets and inline images. Artifacts and compact summaries remain distinct from human approval; the design return includes criteria, limitations and receipt references.

Pin the adapter executable/entry helper in reviewed bindings, preserve no-shell execution and reuse_policy=never for live observations. Source-bound test receipts and historical observations retain their existing semantics. A new Git HEAD still requires existing strict reconciliation.

## Later tool profiles and side effects

ACTION_MATRIX.json records the staged actions and actual concerns. Visibility profiles reduce context; action allowlists enforce approved scope independently of visibility. HTTP/stdio startup and connection synchronization can expose different tools. Inspect the resulting catalog rather than assume core is read-only.

After the query pilot, add on-demand reflection (assembly/type/member), bounded object/component inspection, then small sequential batches. Each batch must prevalidate its full action list, be single-target, keep every subresult, stop at approved failure boundaries and mark remaining commands unrun. Disallow nested batches/custom arbitrary execution in the initial profile. Successful earlier actions are not rolled back.

Testing/build/profiling are separate future bindings: the current observation protocol has no such operations. Preserve full raw test results before reload, account for focus nudges and Editor throttling changes, and verify restoration. Native completed/status labels, exit zero, old build reports and screenshots cannot independently establish current acceptance.

Telemetry must be explicitly disabled and verified for an adopted local setup; asset generation/API spend, package mutations, arbitrary code, console clearing and automatic recovery remain excluded. No design method or game defaults change.

## Completion and continuation

CP-A completion is publication of this specification, the machine-readable action/source-pin matrix, actual input identity checks and checkpoint readback. It is not runtime delivery or live compatibility.

CP-B1 is complete: optional/coplay-provider/discovery.py and its README provide diagnostic-only discovery with a fake-transport seam; tests/test_coplay_discovery.py passed all 20 focused offline cases. Actual sources/cases/raw output are in review/evidence/small-tasks/CP-B1/. Native observation capabilities remain disabled. The raw vendor state leaves identity/external-change observations unavailable, so the diagnostic does not synthesize provider readiness. Next bounded task is CP-B2, the strict Editor query handler; no live compatibility is implied by the offline result.

CP-B2 then defines/implements the minimal strict Editor query handler as a separate bounded task; CP-B3 performs the disposable-project live pilot, including two Editor targets and changed-session/invalid-folder cases. The user's acceptance authorizes this staged incorporation direction; obtaining actual host access/target facts is still necessary, and no host success can be fabricated. CP-C remaining adapter negatives, CP-D measurements and CP-E later bindings follow their dependencies. Preserve pending B06a/B06b/B08; final assurance must account for relevant changes before adoption.



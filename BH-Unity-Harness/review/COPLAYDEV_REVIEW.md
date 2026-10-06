# CoplayDev reference review

Date: 2026-10-06 UTC (2026-10-05 Pacific).
Repository/input commit: BH-Studio/boarshead-ai at 357d154e2d0e4a633096ac746af7b538f78f8256.
Reference: Reference/CoplayDev/unity-mcp-beta, Git tree b3ec16283d5ce88e7576fbe2eacf2d2eb9bdf1dc.
Disposition: REVIEW COMPLETE; recommendations only. Integration, installation and live verification NOT_RUN.

## Recommendation

Use Coplay's MCP for Unity as an optional, version-pinned Unity execution/observation provider beneath BH's existing approval, scope, evidence and design-feedback contracts. Its strongest contribution is concrete Editor connectivity and tool implementations; BH already supplies much of the orchestration discipline. Do not replace the BH runtime, import the complete vendor skill into default context, or fork the entire vendor server into the installed package.

Prioritize a narrow provider pilot, bounded discovery/API inspection and small approved batches. Treat test/build/profiler bindings as later extensions with explicit result contracts. Keep all game mechanics, packages, render pipeline, UI family and acceptance thresholds project-owned.

## What was actually examined

The complete reference tree inventory contains 2,559 entries, including 2,313 files. Retrieved and Git-blob-verified 53 selected source/document/test files. Reviewed targeted implementation sections and relevant test patterns across Python tools/CLI, C# batch/readiness/job/reflection/build handlers, package metadata, operator guidance and telemetry configuration. This is a focused incorporation review, not an exhaustive 2,313-file audit. The evidence ledger distinguishes retrieved files from the full metadata inventory.

Compared against current BH provider protocol, unity_jobs.py, UNITY_PROCEDURES.md, CODEX_CONSUMER.md, construction checkpoint and incorporation status. Existing implemented features were not reconstructed or retested. Coplay's own test files were inspected as source only; no vendor test suite, Unity Editor, CLI/server, package installer or model API was executed.

Snapshot identity matters: the Unity package declares 10.3.1-beta.1, the Python server declares 10.3.0, and README quickstart/release text describes v10.0.0. This does not itself prove incompatibility, but the README version is insufficient to identify this snapshot. Recommendations concern the vendored bytes, not an assertion about the latest upstream release.

## Useful additions and overlap

| ID / priority | Coplay mechanism and evidence | Current BH overlap | Proposed incorporation |
|---|---|---|---|
| CP-01 / highest | Actual Editor state, instance routing, MCP tools and a local HTTP/CLI route: Server/src/services/resources/editor_state.py; Server/src/services/tools/set_active_instance.py; Server/src/main.py; Server/src/cli/utils/connection.py. | BH has a strict provider interface and optional job runner, but no configured native mapping. | Build a thin, optional adapter around a pinned Coplay installation. Start with target/readiness discovery and one bounded search. Verify exact project path, unambiguous instance, session and capability schema from observations before every operation. Use existing BH receipts and fresh-observation policy. |
| CP-02 / high | Dynamic tool groups, session activation and project-scoped custom-tool discovery: Server/src/services/registry/tool_registry.py; services/tools/__init__.py and manage_tools.py. | BH already has explicit skill invocation and conditional references. It does not supply Coplay tool-surface configuration. | Add task-specific tool profiles to a Coplay adapter/conditional guide, loading only needed schemas/references. Recheck visibility after connection/sync. Visibility is context management, not BH authorization enforcement. |
| CP-03 / high | ID-only object search; object summary then targeted component read; console caps, paging and optional stacks: find_gameobjects.py, resources/gameobject.py, read_console.py. | BH already requires bounded search, requested properties, completeness and compact returns. | Map real query/results to those existing reducers. Use IDs only within the observed session; retain stable asset paths/GUIDs as applicable. Request specific component data, not default full property dumps. Preserve full raw output outside model context, pagination/coverage metadata and explicit truncation. |
| CP-04 / high | Live C# API inspection with search → type summary → member signatures: unity_reflect.py and MCPForUnity/Editor/Tools/UnityReflect.cs. Type search caps results at 25 and reports truncation. unity_docs.py supports official API/manual/package lookup. | BH's guide already says to discover APIs in the actual version; no concrete reflection route is configured. | Add an on-demand API verification procedure before uncertain Unity/plugin calls. Scope by assembly/type/member, bind to loaded versions and session, and invalidate caches after relevant changes. Reflection establishes available signatures; versioned documentation still explains semantics. Mark unversioned documentation fallback explicitly. |
| CP-05 / high | One request can execute a bounded command array; C# executes it sequentially on the main thread with per-command results and optional fail-fast: batch_execute.py and BatchExecute.cs. | BH's fail-fast verification already exists. That is distinct from reducing Editor tool round trips. | Adopt small, reviewed, single-target Editor batches. Prevalidate every action/target; retain each result and mark remaining actions unrun after failure. No automatic replay after uncertain delivery. No transaction/rollback guarantee. Handle compile/reload boundaries between batches. |
| CP-06 / medium | Async run_tests/get_test_job, server-side bounded waits, progress, and SessionState job metadata; compile-edge timestamps survive domain reload: run_tests.py, TestJobManager.cs, EditorStateCache.cs. | BH already has submit-once ownership, local polling/deadlines and strict session/capability checks. | Reuse BH orchestration; map native operations rather than implement a second polling framework. Preserve actual detailed test evidence before it can be lost. Keep unknown submission outcomes unresolved. Any cross-session continuation needs a separate reviewed protocol change; Coplay reconnection alone cannot waive BH session checks. |
| CP-07 / later | Native build jobs/reports and profiling actions: manage_build.py / ManageBuild.cs and manage_profiler.py / Profiler/ManageProfiler.cs. | BH has project-owned verification bindings and optional Unity resources, but not these provider mappings. | Consider separate optional build/performance bindings after the basic bridge works. Pin job IDs, target/configuration/scenes and output hashes; record actual result/report. Profile comparable scenarios with approved budgets and capture/restoration of state. Editor counters are not target-player acceptance. |

Potential cost benefit is fewer model turns, smaller tool catalogs/results, and fewer API-guess/compile/repair cycles. These are mechanism-based expectations, not measured credit savings. Coplay's 10–100x batch marketing claim was not verified and is not adopted as a BH target.

## Concrete differences the adapter must handle

### 1. Readiness is advisory in parts of Coplay

Server/src/services/tools/preflight.py returns permission to proceed when Editor state retrieval raises, reports failure, or has unexpected shape; stale snapshots also do not block. It can refresh/compile when external changes are dirty. Its guard is bypassed when PYTEST_CURRENT_TEST is set, so that Python test environment cannot by itself prove live readiness behavior.

BH's provider must instead return unavailable/busy when target readiness, freshness or identity cannot be established. An inspection cannot silently acquire permission to refresh/compile. Readiness, command completion and acceptance evidence remain separate facts.

refresh_unity.py deliberately avoids retrying a command that may trigger reload, which is useful. However, it can classify a disconnect/timeout during a compile request as recovered; with wait_for_ready=False it can reach a success response without confirming readiness. Preserve the no-blind-retry idea; do not translate this success flag into proof that the requested compile occurred or passed.

### 2. The CLI is not semantically identical to MCP tool calls

Server/src/main.py cli_command_route sends most commands directly to PluginHub.send_command. It does not pass them through the Python MCP tool wrappers. Without unity_instance it selects the first available Editor. Name matching can also select an entry before a caller has independently established a unique target. The adapter must validate unique identity from the instance inventory and supply a verified exact selector on every call, with response identity checks. CLI/server health alone is not project readiness.

Server/src/cli/utils/connection.py posts to /api/command without authentication headers; main.py omits these CLI routes in remote-hosted mode. Start any later pilot on an approved loopback-only setup, with exact endpoint/instance binding. Do not assume remote-authenticated MCP and local CLI have identical behavior.

Server/src/cli/commands/batch.py has three observable contract discrepancies: its input ceiling is 40, while the C# handler defaults to 25 with a configurable ceiling of 100; its human success summary reads per-item success while the C# handler emits callSucceeded; and result-level failures do not necessarily cause a nonzero CLI exit. The run subcommand also prints progress and a summary around formatted output. A BH provider cannot consume this as one clean JSON receipt or trust exit zero. Normalize the actual structured response, every subresult and cardinality under the approved schema. These are static source findings, not live reproductions.

### 3. A batch is ordered work, not parallel or atomic work

BatchExecute.cs explicitly returns parallelApplied=false and runs commands sequentially on Unity's main thread. This is appropriate for Unity API safety and can still reduce tool round trips. Earlier successful commands remain applied if a later command fails; fail-fast provides no rollback. The Python batch limit cache is module-global, so a BH multi-instance adapter should observe/validate limits per target and session rather than rely on a global cached value. Never use generic command success as acceptance evidence.

### 4. Polling and tests can change Editor state

get_test_job has a readOnlyHint, but its implementation can call _update_job_nudge, which schedules an OS focus change under no-progress conditions. TestRunnerNoThrottle.cs modifies Editor interaction/idle preferences and attempts to restore them at run completion/error. find_gameobjects can invoke preflight with refresh_if_dirty=True. Thus a metadata hint or query-shaped name is not a complete side-effect contract.

BH must either disable those effects through a verified configuration/route or explicitly include preparation/restoration in the approved operation. Verify restoration on success, failure, timeout and reload. Do not automatically clear stuck jobs, refocus the desktop, reset logs, switch platforms or change project settings as an observation repair.

### 5. Job persistence is not durable result evidence

TestJobManager.cs persists job/progress metadata in SessionState but explicitly restores Result=null. It also has heuristic orphan handling. A restored succeeded/failed label can therefore exist without the full test result payload. Capture and hash the complete required raw result/test roster while available; missing results are incomplete evidence, not a reconstructed pass.

The existing BH observation protocol supports search, audit, smoke, assets and localization. It does not have a test, build, reflection or profiler operation. Do not label a native test run as smoke, invent provider fields, or merely echo BH request fields as observed provenance. Unit tests/builds need the existing suitable verification binding path or a separately reviewed extension with a real artifact parser and negative tests. Reflection may remain an implementation-time inspection tool until a formal evidence contract is needed.

### 6. Tool groups, defaults and cost boundaries need BH ownership

HTTP startup disables non-default groups, but connection synchronization may re-enable groups. Stdio starts with all groups enabled and later syncs Editor toggles. Even core includes mutating tools. Reconcile the actual exposed catalog with the approved task, and enforce action-level permissions at BH's boundary, including commands nested in batches and custom-tool execution.

Server config enables telemetry by default. telemetry.py supports opt-out including UNITY_MCP_DISABLE_TELEMETRY. Any adopted local provider should use an explicit reviewed privacy configuration and verify the behavior; this review did not exercise network traffic. Asset-generation tools use bring-your-own provider keys. They provide no demonstrated need for the current harness and should stay outside its default capabilities and cost envelope. Premium Aura is not required by the bridge architecture shown here.

### 7. Vendor guidance is useful as a reference, not a replacement policy

The operator skill's resource-first workflow, bounded screenshots and avoidance of redundant refreshes are useful. Its broad tool catalog, all-pages pagination examples, world/UI creation recipes and tool-specific recovery advice should be selected only for the current task. A small screenshot is useful for inspection; image resolution for actual acceptance must fit the criterion. Never substitute a screenshot for interaction, saved-asset, target-build or human approval requirements.

Use file precondition hashes for concurrent edit protection where supported, but a new hash after stale-file failure is not permission to replay an old edit. Re-read/reconcile changed content and applicable approval. No source-game defaults or automatic new design authority should enter BH through these recipes.

## Proposed bounded follow-ups

These are proposals, not newly authorized implementation or changes to B06/B08.

1. CP-A: author one short conditional Coplay integration specification and an action/side-effect/capability matrix. Pin a package/server pair and schemas. Specify narrow query limits, identity, raw artifacts and result interpretation. Keep the five installed core skills unchanged.
2. CP-B: in a separately approved disposable Unity project, prove one narrow discovery/search route with the correct project and a second open Editor as a negative target case. Observe compile/busy/stale/reload behavior. Map only operations genuinely satisfying BH's existing contract; leave all others disabled.
3. CP-C: add focused adapter negatives for ambiguous/wrong target, missing capability, changed session, unknown submission outcome, partial/truncated output, result-level failure despite exit zero, malformed batch result and missing persisted result. Test a permitted stateful operation's restoration independently before enabling it.
4. CP-D: measure equivalent single-call versus small-batch work: model/tool round trips, tool-schema bytes, response bytes, elapsed time and correctness. Measure billed usage only if the actual client exposes comparable records; do not infer it from bytes.
5. CP-E: only after that evidence, consider native test/build/performance bindings and narrow operational authoring actions. Keep original receipts, human acceptance and design feedback intact.

Recommended order for value: basic optional provider plus compact discovery; then API inspection and small batches; then native test/build evidence; then project-specific profiling or advanced authoring.

## Publication scope

This review adds original analysis and source-identity evidence only. No vendor implementation is copied into BH, no third-party software is installed, no default tool catalog or package manifest changes, and no tests/adoption are newly claimed. The vendored LICENSE identifies MIT and requires its notice for copied/substantial portions; retain that notice if code is later incorporated. No licensing decision about unrelated assets/dependencies was made.

B06a/B06b and B08 remain open, and the recorded construction next action remains B06a. This targeted user-requested review is separate from that queue and does not mark those reviews complete.

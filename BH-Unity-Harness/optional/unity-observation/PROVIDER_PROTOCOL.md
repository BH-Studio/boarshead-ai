# BH-UNITY-PROVIDER-1 — provider mapping contract

This is a BH interface defined by `unity_jobs.py` and `unity_evidence.py`, not a claim that Unity exposes commands with these names. The modules are the executable field/type authority. A real local provider must map this protocol to the commands and result schemas discovered in the selected host. No native Unity/Pipeline/MCP mapping is shipped or enabled here.

## Three actions, one operation
The runner invokes a reviewed executable with an argument array. Required whole-argument placeholders are `{action}`, `{request}`, `{project}` and `{job_id}`. A Python provider additionally has a pinned entry script as the first argument. No shell, inline `-c`/`-m`, remote installer, automatic update or arbitrary command assembled from tool output is allowed.

`probe` must inspect the actual target and return `ready`, no job and no result. `submit` is issued exactly once and returns a stable job identity. `status` uses that exact identity until a terminal response or the local deadline/poll budget. Provider calls must not launch another Editor, install packages, repair code, change scenes, reset console history or commit files. Any Play-state setup/restoration or other stateful preparation must be explicitly authorized, measured and restored by the reviewed provider; otherwise report unavailable. Generic read permission is not permission to tune the game.

The request has protocol, project_id, absolute project_path, task_id, run_id, operation, session_id, capabilities_sha256, spec and absolute artifact_directory. Its request_sha256 is the canonical BH digest before adding that field. The provider must verify the supplied target, current session and actual capability schema; echoing the request without observation is invalid evidence. All generated artifacts must be bounded regular direct-child files of artifact_directory. Do not follow response-controlled paths or external URLs.

Every response contains exactly:
```text
protocol, project_id, project_path, run_id, request_sha256,
session_id, capabilities_sha256, capabilities, job_id, state, result
```
The protocol equals BH-UNITY-PROVIDER-1. Required capability names must actually be present. No extra response fields or inline image data are accepted. The states are `ready`, `accepted`, `running`, `completed`, `busy`, `unavailable`, `interrupted`, `failed`, `cancelled`. Only completed may contain a result. Accepted/running require a stable job ID; later responses must match it. A reload that changes session/capabilities invalidates the operation. Failure/cancellation must be an observed terminal state, not inferred from the client timing out.

Stdout contains one UTF-8 JSON object, without banners or progress text. Diagnostics go to bounded stderr. The runner retains both. Exit zero alone does not prove completion. Response/stderr limits, process/deadline limits and maximum polls are enforced locally. Unknown JSON fields, duplicate keys and nonfinite numbers fail. There is no model turn per status poll and no persistent background agent.

## Operation contracts
Only the selected operation's specification and observations are loaded. No operation chooses a game's mechanics, UI framework, locales, render pipeline or allowed diagnostic budget.

| Operation | Required specification | Completed result |
|---|---|---|
| search | query, provider, nonempty scope_paths, requested scalar properties, max_items (1–200) | Same query/provider/scope; complete flag, total_count, items with unique id/kind/path/exact requested properties |
| audit | categories, scope_paths, rules_fingerprint, hashed baseline JSON | Current-run csv_file, issue_count, matching categories/scope/rules, rules_present, coverage_complete, positive analyzed_count |
| smoke | nonempty condition_ids, capture_source (screen/camera/none), minimum_frame_advance | frame_before/frame_after, every condition boolean, error_count and optional hashed capture with the requested source |
| assets | Nonempty asset roster: path, subassets, bindings (target/method/call_state), behavior_ids | Observed assets: path, persisted/reloaded, subassets, bindings plus observed flag, behaviors and duplicate_count |
| localization | Nonempty key/locale rosters and declared code_sites | Entries identified by key/locale/value plus converted_code_sites |

Search completeness is limited to the declared provider/index/scope. An incomplete capped query cannot prove absence. Empty results may satisfy an explicitly approved absence check only when coverage is complete. A script-name keyword search is not an exhaustive component/dependency proof.

Auditor CSV columns are exactly `Category,Severity,Areas,Description,RelativePath,Line,DescriptorId,Recommendation`. Column order may vary; names must be unique and every row complete. Quoted commas/newlines are parsed, not split naively. The baseline JSON contains source=`unity-project-auditor`, categories, scope_paths, rules_fingerprint, positive analyzed_count, coverage_complete=true and a report `{path,sha256}` referencing the baseline CSV. A baseline and current scan must have comparable scope/rules. Header-only CSV is clean only with a genuinely completed positive-coverage scan. New/resolved rows are compared as multisets; line/message changes can count as a new finding and require review, not automatic normalization or baseline edits.

Saved-asset observations must come from saved/reloaded data, not just a currently held object reference. The provider must inspect serialized references/sub-assets and exercise each declared binding/behavior. A true flag constructed from the requested expectation is not an observation. Localization completeness does not prove translation quality, glyph coverage or layout fit; those remain separate checks and human decisions.

## Mandatory parent expectations
Before any submit, the runner requires coverage_complete equals true for search/audit; frames_advanced and conditions_met equal true for smoke; asset_failures equals zero for assets; missing_or_empty_entries and unconverted_code_sites equal zero for localization. Search also needs an approved match_count comparison, audit needs new_findings, and smoke needs error_count. Thresholds and acceptance-ID mappings come from the approved binding, not universal guesses.

## Provider review record
Record the exact Editor and package versions, executable/helper hashes, discovered command/response schemas, target and session selectors, supported operation set, field-mapping explanation, mutating effects/restoration, deadlines, privacy/release restrictions and actual test evidence. Leave unsupported operations disabled. Do not infer Safe Mode, closed Editor or cancellation solely from a failed connection. No successful fixture establishes live mapping compatibility.

## Compatibility
The observation runner requires the candidate core/schema supporting optional binding reuse_policy values `source-bound` and `never`. Older cores reject the new field. Version 1.0.0 alone is insufficient to mix candidate snapshots: pin the distribution commit and hashes. Upgrade only between archived tasks; do not remove `never` to make an older core accept the binding. Historical status is not a continuous live-health assertion.

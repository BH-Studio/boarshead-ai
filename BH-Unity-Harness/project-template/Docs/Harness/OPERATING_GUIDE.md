# BH Unity Harness operating guide — 1.0.0 candidate

## Purpose and boundaries
The design method explores and validates with the human in ChatGPT. Codex implements an approved bounded slice in VS Code. This harness does not replace either tool, start autonomous crews or call a model API. It writes durable local state and evaluates real outputs. It is not a sandbox or an independently authenticated approval service.

Run at the actual Unity project root. Git is optional; no repository or initial commit is required. The separate authoring package, full GPT library, reference repositories and old harness archive never belong under the live game's Assets folder. `project-template` is the only installer source. Unknown engine/targets/tools are deliberately unconfigured and block useful execution.

## Prerequisites and installation
Python 3.11+ must already be deliberately available. Git may be used when available, but is never a prerequisite for installing or running the project harness. Windows PowerShell 5.1+ or PowerShell 7 can invoke `Tools/BH/Invoke-BH.ps1`; it selects the existing `py -3` launcher, then `python`, and does not elevate, change execution policy or download anything. Check the actual selected Python version. The implementation is Python, not a second simulated PowerShell implementation. Windows/PowerShell/Unity integration is a separate local acceptance test.

From the separate harness authoring directory, with a reviewed existing game root:
```powershell
py -3 installer/install.py preview --target 'C:\Games\My Game'
# Review every row and the complete preview. Apply only its actual approval hash.
py -3 installer/install.py apply --target 'C:\Games\My Game' --approved-preview '<actual hash>'
```
Angle-bracket values require actual reviewed inputs; these examples are not executable approvals. Preview writes nothing. Existing nonidentical AGENTS.md is a conflict. `--preserve AGENTS.md` explicitly leaves that file untouched and records a required manual merge; it does not establish compatibility. Existing project config seeds remain project-owned. Existing skill/config/global setting conflicts are never clobbered. Repeat preview after any edit. Apply rechecks the exact preview under a lock and journals managed changes/backups. An interruption may leave an APPLYING journal; inspect it, preserve user changes and use the documented rollback path, not blind reruns.

## Configuration ownership
`.bh/project.json` contains shared project identity, exact Unity version/pipeline/targets, protected paths, approved capabilities, adoption/instruction review references and recovery budgets. `.bh/local.json` contains only machine-local executable paths, hashes, observed versions and chosen Editor route; never store API keys or secrets there. `.bh/bindings.json` contains reviewed check ID-to-tool bindings, argument arrays, working directory, timeout, pinned helper inputs, observable expectations and optional reviewed dependency paths. Read the exact schema in `.bh/schema.json`; unknown fields are rejected.

Each executable is explicitly resolved, pinned by SHA-256 and observed version, with a human/tool review reference. Arguments are arrays, not shell commands; Python bindings invoke a pinned reviewed script, not `-c` or `-m`. Native tools can execute arbitrary work, so review them before binding: the wrapper is not an OS permission boundary. Config changes require replanning and approval. Unity CLI is the preferred execution route. Discover the actual installed CLI version, supported commands, response schemas and project/session selectors; do not invent flags or treat an allowed configuration value as an implemented binding. An alternative requires a demonstrated Unity CLI capability gap for the approved task, strong evidence comparing targeting, reliability, side effects, dependencies and cost, and explicit human approval of the exception. A missing binding is a blocker, not permission to install a third-party provider or select MCP automatically. Do not invent a successful diagnostics binding.

Manually merge `.bh/GITIGNORE_MERGE.txt` into the project's ignore policy after review. `.bh/state.json` and generated CHECKPOINT are the active task's local state; raw run logs, machine paths and unredacted exports are not automatically committed. Deliberately review/redact evidence before sharing. Keep accepted compact design/decision records in project-owned documentation. Raw evidence retention is human-controlled; no automatic deletion is implemented. Preserve failed runs through acceptance and any investigation.

## Native instructions versus BH authority
As verified against current official Codex documentation on 2026-10-04, Codex discovers global guidance, then one eligible instruction file per directory from repository root to its current directory; an override can replace AGENTS.md at that directory. Closer instructions can supersede earlier text. The default combined limit is 32 KiB. Local skills are discovered along `.agents/skills` ancestry, as well as user/admin/system locations; duplicate names are not merged. BH checks instructions in the current source snapshot and project skill-name duplicates. The operator must review global, ancestor, ignored and host-managed instructions. No Markdown statement overrides the host's actual precedence or permissions.

All five BH skills require explicit invocation via their `agents/openai.yaml` policy. Optional procedural guidance is outside installed discovery. Do not install the entire Reference catalog or run incompatible B1 and BH policies together. Inspect actual `/skills` and a fresh session's reported instructions during the pilot.

## First run and approval sequence
The following commands are real implemented commands; substitute actual task paths, not example approval labels:
```powershell
.\Tools\BH\Invoke-BH.ps1 --root . preflight
.\Tools\BH\Invoke-BH.ps1 --root . validate-handoff Handoff/handoff.json
.\Tools\BH\Invoke-BH.ps1 --root . init Handoff/handoff.json
.\Tools\BH\Invoke-BH.ps1 --root . plan .bh/tasks/<task>/proposal.json
.\Tools\BH\Invoke-BH.ps1 --root . approve --by "Doug" --source "My approval of the current plan in this session"
.\Tools\BH\Invoke-BH.ps1 --root . begin
```
`init` requires declared task-state writes and a valid design handoff; it does not approve execution. `plan` freezes actual input/configuration/core fingerprints and detects blockers. Review its scope, steps, risks and blockers, then approve the current plan in the session or run the explicit command above. Codex may record that already-given decision using the real human name and source reference; it must not invent consent. The harness creates the approval record and binds it to the current plan internally. No copy/pasted plan hash is required. The legacy `approve PATH` record form remains supported. Approval does not survive an intervening input edit. `begin` starts only from a matching approved baseline. The human's approval covers ordinary edits within that bounded scope without repeated prompts.

## Verification profiles and actual adapters
Fast checks validate the configuration/incoming contract, current diagnostics when a reviewed bridge exists, and task-selected focused checks. Slice verification adds applicable Unity compilation, named EditMode/PlayMode/contract tests and a feature smoke scenario. Milestone verification adds required regression, build, persistence, performance/scale/determinism checks and a manual checklist. The exact check IDs, adapters, profiles and thresholds come from the approved handoff and bindings, not universal guessed test names. Profiles are cumulative. No selected checks, zero discovered NUnit tests, missing output, unavailable required tools and stale results cannot pass.

```powershell
.\Tools\BH\Invoke-BH.ps1 --root . verify --profile slice
.\Tools\BH\Invoke-BH.ps1 --root . return
```
Supported deterministic parsers: NUnit XML with actual test cases/counts/names; observable JSON facts compared to pinned expectations; diagnostics JSON with source and completed-analysis flag compared against a pinned baseline; build JSON plus fresh nonempty hashed outputs. A zero process exit is necessary but insufficient. The generic process route is implemented; specific Unity CLI, approved alternative and diagnostics bindings must pass local integration tests before use. A native Unity CLI mapping is not shipped by this candidate. `dotnet build` is not a substitute for the actual Unity project.

Unity batch bindings must target the exact project, configured Editor version and approved `launch-unity` action. The local route must be batch, the human must confirm the project is closed, and an existing Temp/UnityLockfile blocks launch. The wrapper does not kill an existing Editor. NUnit uses `-runTests`, `-testResults`, an explicit test platform/filter and no premature `-quit`. Recheck installed Unity Test Framework documentation/version before configuring. If the Editor is open, preserve its ownership; use an approved Unity CLI route only when its actual capabilities support that state, or have the human close the Editor before an approved batch run. Do not launch a competing process. Compilation/domain reload and any approved route refresh must be settled before evidence is taken.

Facts format: `{project_id, task_id, run_id, observations: {key: value}}`. Diagnostics adds `{source, analysis_complete: true, issues: [{path,line,rule,message,severity}]}`; use discovered actual bridge tool names and preserve observed `sonarqube` source identity. Build adds `{build_result, errors, target, outputs: [{path,sha256}]}` with successful observations and fresh outputs beneath this run directory. A green console, screenshot, connection test or manually assembled PASS receipt is not gameplay proof.

## State, evidence and recovery
The implementation's `TRANSITIONS` in `Tools/BH/bh.py` is the legal transition authority. The main path is DISCOVERY → PLANNED → AWAITING_APPROVAL → APPROVED → EXECUTING → VERIFYING → READY_FOR_HUMAN_REVIEW → ACCEPTED. BLOCKED, FAILED, PAUSED and CANCELLED have explicit recovery/closure routes. Automated verification never jumps to ACCEPTED.

`.bh/state.json` is schema-validated and revision-checked; `.bh/CHECKPOINT.md` is generated from it. State writes use atomic replacement and an exclusive writer lock. Do not edit the checkpoint as another source of truth. Receipts retain project/task/run IDs, UTC times, commands, environment, tool versions, exit codes, elapsed times, actual counts/observations/artifacts, configuration/core hashes and a commit plus dirty-input content snapshot. Their raw results are reparsed before a PASS is trusted. Historical failures remain visible.

Snapshots hash nonvolatile inputs, including binary assets, in constant-memory chunks. When Git is usable at this project root with a valid HEAD, the snapshot uses its tracked/untracked nonignored roster and records the commit. Without Git, valid repository metadata or a first commit, it walks the project files, prunes Unity caches and BH journals before traversal, records `commit=null` and conservatively sets `dirty=true` (no VCS cleanliness claim). Filesystem mode does not interpret `.gitignore`; all remaining files are included. Switching inventory/commit metadata requires reconciliation and replanning because the baseline can change. This can be I/O-heavy on a large Unity repository; it does not send the bytes to a model. Large-workspace performance is unmeasured. Git-ignored content (when Git supplies the roster), external packages/services and explicitly volatile directories require separate reviewed checks and bindings; do not claim coverage of them merely from source hashes. LFS pointers, symlinks/submodules and path/case escapes are rejected pending a separately reviewed workspace. A content hash is correlation, not independent attestation.

```powershell
.\Tools\BH\Invoke-BH.ps1 --root . resume
.\Tools\BH\Invoke-BH.ps1 --root . status
.\Tools\BH\Invoke-BH.ps1 --root . pause 'Observed service limit; resume from current approved plan after availability returns.'
.\Tools\BH\Invoke-BH.ps1 --root . recover 'Observed failure and evidence; one specific in-scope correction, then the named check.'
```
On resume reconcile the current worktree; do not restart completed work or trust stale evidence. Pending interrupted runs become explicit incomplete evidence, never success. Default proposal budgets: three failed rounds/repeated fingerprints/no-progress rounds, two infrastructure failures and one recovery cycle. These are configurable conservative defaults, not benchmark-proven optima. Counts occur at completed verification rounds, not every read/edit. Recovery records a concrete diagnosis and bounded action; it cannot expand approved scope. Audit does not repair code; return to execution.

On Windows, timeout/cancellation terminates only the wrapper-owned top-level process; child cleanup is not guaranteed without a tested Job Object binding. Inspect owned children before retrying. Lock recovery never kills an Editor; automatic PID-based unlock is deliberately disabled on Windows. Preserve the lock record, verify its owner stopped, then manually remove only the identified stale lock with human approval. Do not delete locks based only on age.

## Acceptance, archive and rollback
After current automated evidence and actual human observations, the human may supply a matching acceptance record. `accept <approval-path>` validates it and records the exact snapshot; it does not authorize Git integration. Human deferrals need evidence, reason and revisit trigger. `archive --task <id> --expected-state-hash <actual hash>` only archives ACCEPTED/CANCELLED tasks, preserving history and prohibiting ID reuse. Use `cancel <reason>` for an explicitly abandoned task. A new design change receives a new task/handoff after review; old approvals are not relabeled.

Before an upgrade finish/cancel and archive the active task. Review the new manifest/diff, preserve local changes and repeat preview. Retired managed files are reported but not deleted automatically. Rollback targets a recorded installation transaction:
```powershell
py -3 installer/install.py rollback --target 'C:\Games\My Game' --transaction '<actual transaction>'
# Execute only after reviewing the preview:
py -3 installer/install.py rollback --target 'C:\Games\My Game' --transaction '<actual transaction>' --execute
```
Rollback removes only unmodified managed additions, restores verified backups and preserves edited project-owned seeds, journals, unrelated files and empty directories. Changed managed files block rollback rather than being overwritten. Never use reset, clean, broad restore or a new installation to hide unfinished work.

## Cost and context practice
Keep research, options and system design in the normal ChatGPT design workflow. A task's coding context is AGENTS.md, project config, checkpoint, current handoff read-order, selected procedure and relevant implementation/test files. Full methodology, catalogs and historical logs stay outside routine Codex context. Store brief facts/decisions separately from raw evidence. Reuse only evidence whose reviewed dependency hashes remain current. Start debugging from one failure and likely files, not repeated repository-wide rereads. Escalate model/effort only for a concrete hard decision; no hard-coded model or speed profile is installed.

Ordinary Chat and ChatGPT Work must not be confused: current OpenAI documentation says Work and Codex can share the agentic allowance. Account limits, usage dashboard and current client availability are authoritative. Neither normal design conversation nor a subscription is literally token-free. The harness performs no API calls, paid purchases, quota polling, autonomous retries or token accounting without telemetry. At an observed service limit preserve work and stop; no evasion or indefinite sleep/retry.

## Ready-to-use prompts
First run: “Use $bh-unity-preflight. Inspect the actual project and current instructions without changing game code. Report versions, capabilities, conflicts and required configuration. Do not install tools or infer adoption.”
Approved slice: “Use $bh-implement-approved-slice. Verify my genuine approval of the exact current plan. Execute only its scope, preserve invariants and stop at the required verification boundary. No unrelated redesign or cleanup.”
Resume: “Use $bh-unity-preflight and the current checkpoint. Reconcile hashes and pending runs. Preserve dirty work, reuse only current evidence, and report the next bounded action before resuming.”
Audit-only: “Use $bh-unity-verify. Run only approved configured checks. Write evidence/state, not repairs or baseline changes. Report FAIL/ERROR/NOT_RUN honestly and leave human-only criteria pending.”
Recovery: “Use $bh-systematic-debug. Read the last failure's actual artifacts and approved scope. State one falsifiable hypothesis and bounded correction; honor remaining recovery budget and stop if authority is insufficient.”
Upgrade: “Inspect the new pinned distribution and current managed manifest. Finish/archive the active task first. Produce a nonmutating install preview and conflicts; do not apply or overwrite local decisions without my approval of that exact preview.”

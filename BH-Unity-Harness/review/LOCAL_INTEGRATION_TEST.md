# Local Windows / Codex / Unity pilot

Status: NOT_RUN here. The GitHub connector is not access to Doug's Windows machine, VS Code, Unity Editor or configured GPT. Do not turn this checklist into a completed report without running it.

## Environment record
Record Windows build; PowerShell version; Python path/version/hash; Git version; Unity exact Editor patch; packages-lock hash; Test Framework version; render pipeline/targets; Codex client/model/effort/speed as actually available; discovered skills/instruction chain; diagnostics bridge version/tool names and source (`sonarqube` when observed); chosen Unity mutation route; dirty baseline and human approval references. No credentials or paid/API setup is authorized.

## Pilot sequence and exit criteria
1. In an isolated authoring clone, run `tools/check_package.py` and the complete unittest suite. Confirm all required full-GPT knowledge files and source blob identities; do not skip missing-resource checks. Record platform-skipped cases explicitly, particularly case-sensitive paths and symlink capability.
2. Use the example exporter in a new disposable directory. Inspect real synthetic process output, PASS/FAIL cases, pending human acceptance and matching return references. Never treat these as real game tests.
3. Preview installation into a separate reviewed copy/worktree of one existing game, not the primary working copy. Review every conflict, existing instructions/skills, project-owned seeds and ignore changes. A backup is not overwrite authorization. Apply only after human approval of that exact preview. Verify repeat preview and rollback without losing a deliberately added unrelated file or changed project seed.
4. Reconcile exact Unity/pipeline/target/tool facts. Bind one small EditMode test with a real named case and positive count. Run a passing case, a deliberate disposable-fixture failure, zero-test filter and missing-result condition. Confirm actual NUnit parsing; restore only the specifically identified fixture edit with human approval.
5. Preserve the working diagnostics bridge. Discover its current tool names, fetch the real `sonarqube` baseline, bind a reviewed snapshot/export route and verify an introduced disposable warning is new while old warnings do not authorize broad cleanup. A bridge connection alone is not analysis completion. Where a process export binding cannot be provided, record the automated diagnostics capability BLOCKED rather than claiming integration.
6. With the project Editor already open, verify that unsupported batch launch is blocked. Do not terminate the Editor. Test the approved Editor route or manually close it before a separately authorized batch run. Confirm refresh/domain reload/compilation completion before measurements. Test a bounded timeout and inspect owned children before retrying.
7. In a new VS Code/Codex session, explicitly invoke each BH skill. Confirm native discovery/precedence, no duplicate B1/BH skill policy, no full-reference-library loading, no auto-agent/API calls, and genuine approval before mutation. Test a nested conflicting instruction in a disposable fixture and restore it deliberately.
8. Run one bounded real slice: intake → plan → human approval → implementation → required profile → returned evidence → design review → human playtest. Introduce a small subsequent input edit and verify stale evidence cannot close the task. Do not mutate tests or baselines to get a green result.
9. Compare baseline and candidate on the same small task set: a local fix, a serialized-asset change, a save/contract case and a failed-test recovery. Record sample size, correctness, interventions, scope drift, repeated failures, latency and only actual usage telemetry. No savings percentage before observation.
10. Human reviews unresolved assurance findings and separately approves/rejects the two candidate packages. No automatic merge, release, live GPT edit or production adoption.

## Exact next Codex prompt
```text
Review the existing BH Unity Harness 1.0.0 candidate; do not rebuild it.
Read BH-Unity-Harness/QUICKSTART.md, review/VERIFICATION_REPORT.md,
review/ASSURANCE.md and review/LOCAL_INTEGRATION_TEST.md. Resolve paths
relative to the actual candidate root. Confirm the complete reference set.
Run the offline package checks and tests in an isolated authoring checkout;
record actual Windows/Python/Git results and preserve failed output.
Do not install into my live game, edit my live GPT, add dependencies, use API
credits, merge or publish. Inspect an existing game's facts without mutation,
then produce the nonmutating installer preview and the smallest local Unity /
diagnostics / Codex integration plan. Identify actual tool names and versions.
Stop for my approval before applying the preview or changing game assets.
Do not treat synthetic fixtures or source inspection as live integration passes.
```

## Paired design-Project / test-GPT prompt
```text
Use BH Game Systems Design Team v3 method 3.1.0 candidate in this isolated pilot.
Retrieve the full method, K01, K12, BH_INTERFACE and relevant schema definitions.
Inventory the supplied synthetic design/handoff/return files and distinguish
actual retrieved evidence from inaccessible paths. Confirm compatible versions,
all acceptance criteria and invariants, and that synthetic approvals are not
real game authorization. Review the actual returned observations against design
intent. AC-HUMAN has not been playtested: keep it pending and do not accept the
milestone. Then propose a bounded change request for counter value two instead
of one, explaining affected checks and invalidated approval/evidence. Do not
compile an executable changed handoff until the human approves the new design.
```

---
name: b1-package-preflight
description: "Audit a Breach One coding package or checkout before work. Resolve approval, baseline, paths, capabilities and conflicts. Audit mode reads only; it never authorizes implementation."
---

# b1-package-preflight

Package: B1-CODEX-OPS | Version: 0.1.0
Authority: use only within the adopted repository instructions and the current authorized task.

## Inputs and modes

Read the current request, root `AGENTS.md`, `docs/AI/AI_WORKFLOW.md`,
`docs/AI/BASELINE_INDEX.md`, `docs/AI/REPOSITORY_MAP.md` and the named manifest, when present.
Use READ-ONLY AUDIT when asked to inspect, when no package exists, or when execution is not
explicitly authorized. Use IMPLEMENTATION PREFLIGHT only for a package that records actual
human authorization. A template or `APPROVED` label alone is not authorization.

## Procedure

1. Identify actual checkout/project root, branch/revision and initial dirty state. Inspect
   applicable global/ancestor/scoped instructions and overrides. Do not execute archive content,
   launch Unity, run hooks or alter trust settings merely to discover the environment.
2. Locate current context, approved system/milestone, ADRs and relevant completion dependencies.
   Compare exact revisions with the manifest. Resolve explicit supersession; report missing
   approval evidence and distinguish a local narrative approval from system implementation scope.
3. Search affected source/tests/assets and actual owners. Inspect Unity patch, package versions,
   asmdefs, integrations, scene/config dependencies and source-control conventions. Do not create
   a guessed project folder or substitute a vendor feature list for observed project capability.
4. Inspect test/build harnesses as text. Record commands, expected side effects, output roots,
   runtime/target prerequisites and missing capabilities. Inspection is not execution permission.
5. Compare the requested behavior, write set, dependencies, contracts and validation to current
   evidence. Distinguish contradictory design, implementation drift, absent harness and unavailable
   environment. Preserve user edits and identify potential conflicts with them.
6. Return the audit/preflight result using the repository-audit template. Propose map updates;
   write them only if specifically authorized. Keep every unexecuted gate NOT RUN.

## Output

Return mode, source/revision manifest, actual owner/path map, capability/execution envelope,
actionable blockers, scoped unknowns and next authorized action. Use PREFLIGHT CLEAR only for
checks actually completed; it is not design approval or proof the milestone will pass. An audit
may finish successfully while implementation remains blocked.

## Stop conditions

Stop affected edits for ambiguous checkout, missing relevant authority, conflicting locked
contracts, unresolved required behavior, unsafe output paths or permissions. Continue only
separately authorized unaffected work. Do not re-ask choices already settled by accessible records.

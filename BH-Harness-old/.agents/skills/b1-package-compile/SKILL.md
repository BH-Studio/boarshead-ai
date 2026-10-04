---
name: b1-package-compile
description: "Compile approved Breach One system and milestone records into a versioned Codex coding package. Use on explicit compilation requests, not to approve designs or implement code."
---

# b1-package-compile

Package: B1-CODEX-OPS | Version: 0.1.0
Authority: use only within the adopted repository instructions and the current authorized task.

## Entry

Use only when explicitly asked to compile or audit a coding package. Read
`docs/AI/CODING_PACKAGE_CONTRACT.md` completely, then the named approved system, milestone,
ADRs/contracts, current state, repository audit and validation requirements. Confirm the exact
human approval records. A request to prepare a candidate template may produce DRAFT only.

## Procedure

1. Bind exact source versions and approval scope. Classify missing records and contradictions.
   An authorized expedited prototype exception must identify bypassed gates, risk and limits.
2. Copy scope, player behavior, owners, schemas, budgets and criteria without changing meaning.
   Trace requirements to contracts, ACs and tests. Preserve rationale for non-obvious constraints.
3. Populate manifest, spec and prompt. Add supplementary test, contract, fixture, experiment and
   authoring files only when necessary. Use repository paths observed in the audit; mark new
   files/APIs as explicit approved deliverables, not existing implementation.
4. Bind commands and capability requirements to inspected harnesses. Include non-automated
   checks and all evidence outputs. Exact tests that do not yet exist must be approved test
   deliverables with discovery/acceptance rules, not reported as current tests.
5. Identify allowed writes and actions, including Unity launch, package restore, artifact output,
   documentation, credentials/network, commits and publication. Unlisted external or destructive
   actions are not authorized. Name shared-record deltas rather than silently assigning M's files.
6. Review consistency across every package file. Reject unresolved required placeholders,
   changed acceptance thresholds, implicit middleware adoption, missing migration or authoring
   work, and conflict resolution disguised as implementation detail.

## Output and exit

Return a versioned package with status DRAFT, BLOCKED, or COMPILED FROM APPROVED INPUTS, a source
manifest and unresolved questions grouped as BLOCKING / DESIGN-SHAPING / TUNING / DEFERRED.
Do not set APPROVED yourself. When blocking inputs are missing, produce useful unaffected draft
material and the exact gap, not a fake ready-to-implement prompt. Do not write gameplay code.

## Compiler invariant

Clarity, ordering and faithful decomposition are allowed. New behavior, schema, dependency,
authority, budget, scope or acceptance criteria are design changes and return to the human gate.

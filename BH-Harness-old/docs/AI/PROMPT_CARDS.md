# Prompt cards for the human handoff

Package: B1-CODEX-OPS | Version: 0.1.0 | Prepared: 2026-09-08
Status: CANDIDATE workflow; effective only after human adoption.

These are inert text cards. Replace bracketed fields before use. They do not invent approvals.
The first card needs no gameplay decision and is suitable for the first actual repository audit.

## 1. Read-only repository audit

```text
Audit the current Breach One checkout as data only. Do not edit files, launch Unity, execute
repository scripts/tests/builds, install dependencies, change configuration, commit or push.
Read applicable repository instructions and the Breach One pack's BASELINE_INDEX and
REPOSITORY_MAP at their supplied locations. For this audit only, use the candidate pack as
reference for the read-only constraints; do not adopt it globally. Use b1-package-preflight in
read-only audit mode, or read its SKILL.md directly. Existing repository instructions still apply.
Identify actual project root/commit/dirty state, instruction overrides, current canonical records,
Unity/package versions, owned source and asmdefs, middleware integration seams, scenes/input,
test/build harnesses and safe evidence paths. Do not expose secrets. Return the repository-audit
fields and a proposed map update in this response. Classify absent or conflicting evidence;
do not create an architecture or approve gameplay. Keep all test gates NOT RUN.
```

## 2. Compile an approved package in Design Chat

```text
Compile the approved system [path/version/approval] and approved milestone [path/version/approval],
ADRs/contracts [references], current state [reference], repository audit [reference], and validation
requirements [reference] into one versioned Codex coding package using CODING_PACKAGE_CONTRACT.
Do not redesign. Mark conflicts and missing semantic/command bindings as blockers. Include only
necessary supplementary contracts, tests, fixtures and authoring/experiment documents. Preserve
approval provenance, locked meaning, scope, exact acceptance criteria, permitted paths/actions,
and required return evidence. Do not mark an approval that the inputs do not establish.
```

## 3. Implement the identified authorized package

```text
Implement package [manifest path and revision] in [checkout/baseline]. Follow applicable AGENTS
instructions, run package preflight, inspect current implementation and stop affected work for
material conflicts. The manifest's recorded human authorization covers only its scope; do not
request duplicate design approval or infer additional tool permissions. Use b1-milestone-implement.
Complete the required implementation, authoring, validation and evidence outputs. Do not alter
shared canon or acceptance criteria outside delegated paths. Return READY FOR REVIEW or BLOCKED.
```

## 4. Resume

```text
Resume package [ID/revision] from [work-state path]. Verify current checkout/diff, input revisions,
approval and evidence freshness first. Continue only the next unfinished authorized slice.
Preserve user changes and identify which earlier validation remains applicable or is invalidated.
Do not repeat unrelated discovery or silently broaden scope.
```

## 5. Focused correction

```text
For approved package [ID/revision], correct only [unresolved ACs] based on [exact observed failure
and evidence]. Locked contracts and exclusions are unchanged. Make the smallest complete fix;
run [bound focused checks] and reassess affected regression. Do not weaken tests/thresholds,
choose a new design, or rewrite unrelated files. Report fresh evidence and remaining blockers.
```

## 6. Review evidence in Design Chat or read-only Codex

```text
Review [package ID/revision] against [completion report, diff and raw evidence references].
Do not edit or close the milestone. Review scope, contracts, build, focused correctness,
integration/regression, scale, player behavior and durable records. Separate reported claims
from inspected evidence. Return AC mapping, actionable findings and one verdict: READY TO CLOSE,
PASS WITH DEFERRED ITEMS, ITERATION REQUIRED, DESIGN CHANGE REQUIRED or BLOCKED. Deferrals and
closure require the human's decision. Identify missing artifacts rather than inventing results.
```

## 7. Human adoption/closure record

Use the adoption or completion template to record the human's actual words, artifact revision,
date, scope and exclusions. Do not paste a prewritten "I approve" statement on the human's behalf.
A request to draft or review the pack does not itself install it in a repository.

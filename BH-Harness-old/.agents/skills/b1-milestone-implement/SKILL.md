---
name: b1-milestone-implement
description: "Implement an explicitly authorized Breach One milestone or focused iteration after package preflight. Not for design selection, archive review or an unapproved prototype."
---

# b1-milestone-implement

Package: B1-CODEX-OPS | Version: 0.1.0
Authority: use only within the adopted repository instructions and the current authorized task.

## Entry

Read applicable repository instructions, the package manifest and all required inputs. Complete
`b1-package-preflight` in implementation mode. Confirm actual approval provenance and permitted
actions; do not ask for duplicate design approval once clear. Check the current diff and keep
unrelated user changes intact. No arbitrary model or custom-agent dependency is required.

## Work loop

1. Name the next coherent slice, its owner/contracts, allowed paths and ACs. Inspect existing
   implementation/tests and package integration seams before introducing anything new.
2. Implement the smallest complete slice: behavior, failure handling, data/configuration,
   authoring bindings, diagnostics and focused tests as applicable. Do not let private helper
   choices alter serialized/public contracts or player-facing rules.
3. Run authorized focused checks using inspected command bindings. Do not start competing
   Editor processes or downgrade the engine when the environment fails. Record actual evidence.
4. Review changes against scope and preserve one writer across code, tests, assets and docs.
   Reassess source ownership when movement, damage, resources or operation truth crosses systems.
5. For long work, update the authorized work-state file with actual revision/diff, completed
   and remaining ACs, valid/invalidated evidence, blocker and next slice. Keep it concise.
6. After repeated failure, investigate the causal assumption rather than cycling unrelated edits.
   Stop the affected slice for a design-level conflict; return evidence and bounded alternatives.

## Final gate

Review final diff and all ACs. Run the manifest's required build, focused, integration/regression,
player, persistence, co-op and scale gates. Record manual/playtest checks separately; missing
human interaction cannot be replaced by invented observations. If a late fix changes relevant
behavior, rerun invalidated gates. Do not weaken tests or silently defer criteria.

## Return

Produce the authorized completion evidence using `b1-completion-report`: files, AC mapping,
commands/environment/counts, raw artifact references, warnings, measurements, deviations,
remaining risks and proposed shared-state deltas. End READY FOR REVIEW or BLOCKED. The human
alone decides milestone closure; do not mark shared canon or COMPLETE yourself.

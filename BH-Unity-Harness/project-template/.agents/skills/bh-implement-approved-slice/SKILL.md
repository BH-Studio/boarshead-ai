---
name: bh-implement-approved-slice
description: Implement only a reconciled, explicitly approved technical slice. Exclude new design exploration and audit-only work.
---

# bh-implement-approved-slice

Read the current checkpoint, pinned handoff read_order, `views.py --root . context` and relevant source files. The compact view includes the complete decision-bearing plan without its source-hash roster; do not load the bulk JSON unless investigating integrity. Verify the actual human approval reference covers the current reviewed plan. Record an already-given decision using `approve --by NAME --source REFERENCE`, then run `begin` only when its preconditions hold. No pasted plan hash or hand-authored approval file is required; internal fingerprints reject stale approvals. An actor=human field written by a model is not authentication.

Start with the acceptance criteria and likely affected files. Make the smallest complete change consistent with the approved architecture. Use allowed paths/actions only; protected files, dependencies, engine/pipeline/platform upgrades and persistence changes require a new appropriate decision. Preserve user dirty changes and Unity GUID/reference integrity. Record implementation claims with `claim TEXT`; they are not evidence.

Stop at the verification boundary and invoke bh-unity-verify. Do not run every regression after every edit, but do not omit required profile checks. If changed facts invalidate the plan, checkpoint and return to reconciliation. No autonomous crews, paid APIs, speculative refactors, or quota-evasion loops.

Inputs: current approved plan, scope, configuration, and actual source. Outputs: bounded edits and claims. Example: an approved UI binding repair must not silently replace the input system or clean historical SonarQube findings.

Before Unity asset, UI, localization or package changes, read only the applicable section of [Unity procedures](../../../Docs/Harness/UNITY_PROCEDURES.md). Optional providers remain disabled until explicitly configured and tested.

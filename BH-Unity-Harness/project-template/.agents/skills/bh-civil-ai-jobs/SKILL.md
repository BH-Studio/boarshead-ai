---
name: bh-civil-ai-jobs
description: Inspect, design, validate, and (only after explicit approval) implement CIVIL-AI village jobs, resource-enabled prefabs, and economy integration in Unity projects using the BH Unity Harness.
version: 0.1.0
---

# BH CIVIL-AI Jobs — harness specialist skill

## Scope and authority
Use for Ronin village jobs (water, fishing, rice, hauling, cooking, smithing, forestry, etc.) and reusable CIVIL-AI prefab configuration. This skill is **not** a replacement for the BH Unity Harness execution, approval, preflight, or evidence contracts. Start **read-only**. Do not create or edit Unity project assets, change package code, start the editor, or run mutating commands without the harness's existing authorization. Do not assume the prior pilot preflight permits recompile, editor mutation, or package installation.

The included YAML-like examples are design specifications, **not CIVIL-AI native assets**. Never claim a YAML file will be imported by CIVIL-AI. No automatic Unity asset generation is implemented in this skill version; implementation requires package inspection, approved adapters, and a verified editor execution binding.

## Mandatory workflow
1. **Discover** project root, Unity version, CIVIL-AI installed version and source/assembly availability, current harness rules and execution bindings, existing Ronin inventory/crafting/resource systems, work/need repositories, item catalogs, and sample scenes. Record evidence with paths and versions; do not infer APIs from online documentation alone.
2. **Reconcile versions.** Documentation baseline is CIVIL-AI 0.16.0 (`/docs/next/`, observed 2026-11-18). Pin all implementation guidance to the actual installed package. If a class, menu path, serialized property, or action is unverified, mark `UNVERIFIED` and stop before generating dependent code.
3. **Model** the occupation as Job → Duty → Task → Method → Action, plus workplace role, item filters, ownership, reservations, interaction positions, navigation, production and logistics contracts. See `references/job-patterns.md`.
4. **Plan** a proposed change manifest: files/assets to create or modify, external dependencies, identity migrations, acceptance tests, rollback, and evidence. Produce a human-reviewable dry run first.
5. **Validate** job specification with `python scripts/validate_job.py examples/well-water.job.json` (stdlib-only, nonmutating). The validator checks the *proposed contract*, not Unity asset validity.
6. **Execute only when authorized** through the existing harness's verified Unity CLI/editor route. Never use ad-hoc direct project mutation to evade a missing binding. Use project-native APIs confirmed by inspection; avoid editing serialized third-party assets by guessed YAML fields.
7. **Verify** EditMode, PlayMode and resource-accounting tests, prefab duplication and save/load identity stability; capture logs and before/after asset manifests. Report failures and unresolved questions.

## CIVIL-AI facts versus Ronin extensions
- **Documented:** `BardTreeModuleBootstrap` bootstraps services; Module Settings hold repositories and item collections; work content uses Job/Duty/Duty Task/Task Method/Action lists and shared Method List. Workplace roles must match jobs. `Locate` chooses nearest matching item; `Locate Random` and zone variants exist; `Follow Route` uses authored workplace routes. `Pick Up` acquires a nearby item; `Drop Off` drops a carried item. Navigation requires appropriate configured nav data.
- **Proposed Ronin code, not CIVIL-AI built-ins:** `RoninResourceNode`, `ResourceNodeDefinition`, `VillageStockService`, `ResourceNodeService`, `RecipeService`, `LogisticsService`, `RoninCivilBridge`, `VillageSaveAdapter`, resource-aware selectors, delivery transaction confirmations, persistent node IDs. Inspect existing systems first and reuse rather than duplicate.
- Do **not** treat a CIVIL-AI `ServicePoint` as a generic resource-production service; it is a customer-facing interaction concept.
- Nearest matching does not prove shortest NavMesh route or that a custom stock amount is automatically considered. Require explicit eligibility integration or report a gap.

## Prefab and identity rules
Place shared resource configuration and interaction child objects on reusable prefabs. Keep scene-instance identity separate from prefab definition. Do not serialize a fixed instance GUID on a prefab asset. A placed scene instance requires a stable, unique identity across saves; a runtime-spawned instance requires an allocated identity persisted in save data. Duplication must not preserve the same persistent ID. Never regenerate IDs on every `Awake`, `OnEnable`, or unrestricted `OnValidate`. Use an approved editor reconciliation tool with a dry-run collision report, and maintain an old-to-new mapping only for *new duplicates*, not existing saved entities. Resolve nested prefab, prefab stage, additive scene, addressable spawn, and save migration cases before enabling auto-fix. See `references/identity-and-prefabs.md`.

## Required output of discovery pass
- `package-inventory.md`: installed package/version, actual API evidence and source paths
- `integration-map.md`: existing Ronin services versus proposed extensions
- `job-plan.md`: jobs, assets, item names/types, workplace roles, action filters, use spots, capacity and failure cases
- `change-manifest.md`: proposed changes, gates, test plan, rollback, open issues
- `validation-report.json`: job-spec validator output

## Stop conditions
Stop and request an explicit decision when package APIs cannot be verified, the harness's permitted execution binding is absent, an existing resource system conflicts with the proposal, identity repair could break saves, or a job's stock accounting is underspecified. Never silently invent or claim to have executed Unity operations.

## References
Read `references/documentation.md`, `references/job-patterns.md`, `references/identity-and-prefabs.md`, `references/acceptance-tests.md`, and the example specs before authoring a change plan.

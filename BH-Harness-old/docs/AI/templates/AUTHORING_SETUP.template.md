# Authoring and scene setup — <actual package/revision>

Status: TEMPLATE — NOT AUTHORIZED
Governing spec/approval and owning paths: <actual>

## Deliverable and source ownership

Name scene/fixture/prefab/definition purpose, required installed package versions and actual
existing source assets. Identify hand-authored versus generated files and metadata ownership.
Do not invent an asset GUID, vendor prefab path or inspector property.

## Exact setup

For each step give target asset/object/component, version-correct menu/API/property, reference
assignment, rationale, expected resulting state and verification. Include input/animation,
collision/layers, camera/audio/UI, definition IDs and scene entry/reset only when required.
A missing Editor capability is an explicit pending step, not a claimed completed setup.

## Builder or manual workflow

Use existing tools first. Any new builder needs approved scope, safe paths, idempotent rerun,
conflict handling, undo/backups, preservation of existing GUIDs and authored edits, cancellation,
cleanup and diagnostics. Inspect builder source before executing. No broad reserialization.

## Validation

Check missing scripts/references, asset/.meta pairing, duplicate IDs, invalid definitions,
prefab override drift, Editor/runtime assembly boundaries, play/stop/reset behavior, relevant
build inclusion and representative player operation. Record actual results and raw artifact locations.

## Handoff

Provide reproducible setup/reset instructions, actual assets changed, expected presentation,
manual/automated evidence, remaining user actions and blocked gates. Scripts without required
configuration are not a fully delivered gameplay feature.

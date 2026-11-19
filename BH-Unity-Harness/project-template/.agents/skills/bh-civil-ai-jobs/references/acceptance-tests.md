# Acceptance and evidence matrix

## Discovery (read-only)
- Installed CIVIL-AI version, assembly/API, repositories, current harness contracts and existing Ronin economy integrations are evidenced by actual paths.
- Unverified fields and missing bindings are explicitly reported; no Unity asset writes.

## Prefabs / identity
- Two scene instances of same well prefab share configuration but have different persistent IDs and independent stock.
- Duplicate and nested prefab variants trigger collision detection without changing original IDs.
- Prefab edit preserves placed IDs; scene reload and save/load preserve stock and ID.
- Runtime spawn/despawn/respawn does not reuse an active ID; additive scenes have no collisions.

## Navigation / selection
- Workers find eligible reachable resource; depleted, reserved or inaccessible targets are rejected if configured rules require it.
- Report whether ranking is straight-line or actual route length; do not assume path-cost selection.
- Occupation-specific zones, workplace role matching and use spot access are validated.

## Economy
- Two workers competing for one unit cannot both reserve it.
- Pickup transfers custody once; delivery credits receiver once; repeated callbacks are idempotent.
- Interrupt at each phase, missing tool, full storage, failed path, destroyed node and load-in-transit recover without loss or duplication.
- Cooking and smithing consume inputs and produce outputs exactly once; capacity and cancellation cases covered.

## Evidence
Capture package/version, approval reference, changed asset list, validator output, Unity console and test logs, before/after state and rollback instructions. No claims of passing tests without logs.

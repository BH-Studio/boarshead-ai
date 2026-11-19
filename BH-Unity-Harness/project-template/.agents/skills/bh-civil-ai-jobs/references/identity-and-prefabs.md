# Prefab-safe resource nodes and identity

## Design
- Prefab asset: `ResourceNodeDefinition` reference, CIVIL-AI Item/use spots (actual types verified locally), colliders, visual objects and configuration. No scene-instance ID.
- Scene instance: persistent unique ID scoped to the save-world (or globally unique), plus instance-specific stock, cooldowns, assignments and reservations.
- Spawned instance: spawn transaction allocates ID once and save system persists it.
- Stable identity must survive prefab updates, scene unload/reload, save/load, and transform movement.

## Reconciliation algorithm specification (not implemented)
1. Inventory prefab assets, scenes, nested prefabs and runtime spawn paths without modifying them.
2. Identify duplicate, missing, or prefab-leaked instance IDs and report locations.
3. Classify which object is existing versus a new duplicate using scene/asset history and save references; **do not choose arbitrarily**.
4. Propose IDs only for confirmed new instances; show proposed mapping and downstream references.
5. Require approval, then write changes through the verified Unity editor route and record a manifest.
6. Validate global uniqueness, stable references, prefab reimport, scene reload and save migration.

Never blindly regenerate all IDs or silently fix collisions in `OnValidate`.

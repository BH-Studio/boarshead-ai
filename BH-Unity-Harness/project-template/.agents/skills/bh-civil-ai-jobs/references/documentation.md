# CIVIL-AI reference index (documentation baseline: 0.16.0)

Primary entry: https://bardtreelimited.com/docs/next/guide-getting-started
Action definitions: https://bardtreelimited.com/docs/next/guide-behaviour-actions
Work behaviours: https://bardtreelimited.com/docs/next/guide-behaviours-work
Behaviour editor: https://bardtreelimited.com/docs/next/guide-behaviour-tree-editor
Items: https://bardtreelimited.com/docs/next/guide-items
Use spots: https://bardtreelimited.com/docs/next/guide-use-spots
Inventory: https://bardtreelimited.com/docs/next/guide-agent-inventory
Pathfinding: https://bardtreelimited.com/docs/next/guide-pathfinding
Requirements: https://bardtreelimited.com/docs/next/guide-requirement-system

Verify URL redirects and installed-version equivalence; the reference index is a starting point, not proof of exact serialized fields.

## Verified from 0.16.0 Getting Started and Actions Definitions
- `BardTreeModuleBootstrap` scene component; module settings menu `BardTreeLtd/Civil AI/Module Settings`.
- Item name/type/size collections, character pool and pool service, work and need repositories.
- Work content list types: Job List, Duty List, Duty Task List, Task Method List, Action List; shared Method List.
- `BuildingService` for buildings; matching workplace role/job; population region with housing/workplace.
- Default Unity NavMesh path: `com.unity.ai.navigation`, `NavMeshSurface`, bake.
- `Locate` nearest matching item; `Locate Random`; `Locate in Zone 1/2`; `Follow Route`; `Pick Up`; `Drop Off`.
- Action filters include item name/type, ownership, reservation/in-use state and POI requirements.

Do not extrapolate undocumented properties, methods or save formats from these facts.

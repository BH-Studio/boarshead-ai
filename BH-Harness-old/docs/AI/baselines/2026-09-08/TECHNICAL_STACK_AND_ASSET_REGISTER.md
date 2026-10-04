# BH Arcade Assault Project — TECHNICAL STACK AND ASSET REGISTER

**Status:** `CANDIDATE / validation required`  
**Updated:** 2026-09-02

## 1. Architecture rule

Use one canonical owner for each responsibility. Middleware may be an intentional Unity-level dependency, but operation, campaign, shared economy, persistence meaning, and network authority must remain explicit and testable.

Do not build generic wrappers around every package call. Create project-owned contracts at boundaries where state meaning, reuse, replacement risk, save/network behavior, or testing justifies them.

## 2. Approved baseline

| Area | Selection | Status |
|---|---|---|
| Engine | Unity 6.3 LTS | APPROVED |
| First-game pipeline | URP | APPROVED |
| Core gameplay pipeline dependency | None | APPROVED |
| Character execution | Opsive Ultimate Character Controller | APPROVED-BOUNDED |
| AI candidate | Behavior Designer Pro 3 | APPROVED FOR VALIDATION |
| Navigation candidate | A* Pathfinding Project Pro | CANDIDATE |
| Authoring/validation | Odin Inspector + Odin Validator | STRONG CANDIDATE |
| Animation authoring | UMotion Pro | STRONG CANDIDATE |
| Input | Rewired | CANDIDATE DEFAULT |
| Tween/feedback | DOTween Pro + scoped Feel | CANDIDATE |
| First-game art base | Synty assets | APPROVED production base, not final identity |

## 3. Opsive ownership

Owned:

- Ultimate Character Controller.
- Behavior Designer versions below 3 and Behavior Designer Pro 3.
- Behavior Designer Pro 3 Tactical Pack.
- Formations Pack.
- Senses Pack.
- Movement Pack.
- Omni Animation Core Locomotion Pack.
- Swimming Pack.
- Climbing Pack.
- Agility Pack.
- Deathmatch AI Kit.
- Ultimate Inventory System.
- PUN Multiplayer Add-on for UCC.
- State Designer, purchased for another project and available here if justified.

Recommended boundaries:

| Responsibility | Owner |
|---|---|
| Character collision, grounding, locomotion execution | UCC |
| Character-local abilities, item use, interaction | UCC |
| Device input and rebinding | Rewired candidate |
| High-level AI decision selection | Behavior Designer Pro 3 |
| Tactical/formation intent | BD Pro packs under project constraints |
| Path calculation and steering | A* |
| Final AI movement/collision | UCC |
| Attack reservations and concurrency | Project-owned Threat Runtime |
| Encounter phases and threat budget | Project-owned Encounter Runtime |
| Shared access resources and reward transactions | Project-owned Requisition Runtime |
| Power-event policy/progress | Project-owned Power Runtime |
| Objectives/routes/checkpoints | Project-owned Operation Runtime |
| Save schema/migration | Project-owned persistence contract |
| Network authority/exactly-once transactions | Project-owned Session/Network contract |

### State Designer

`AVAILABLE / HOLD`

The purchase cost is no longer relevant. Reconsider only when a recurring finite-state authoring problem exists that is not already cleanly owned by UCC, Behavior Designer Pro, Animator, operation state, or network state.

Likely later uses:

- Boss phase/state authoring.
- Controllable-platform modes.
- Complex machinery/interactables.
- Reusable environment sequences.
- Non-AI actors with explicit finite modes.

### Ultimate Inventory System

`HOLD`

Use UCC’s ordinary item/inventory capabilities for the early weapon proof. Do not store shared access codes, power-event progress, route state, rescued specialists, or campaign progress inside a character inventory.

### Deathmatch AI Kit

`REFERENCE ONLY`

It targets the prior Behavior Designer generation. Study useful patterns in an isolated project; do not import both generations into production merely to reuse the kit.

## 4. Animation and character tools

Owned:

- Omni Animation packs.
- UMotion Pro.
- Final IK.
- Animation Composer System (ACS).
- Malbers Animal/Character Controller.
- PuppetMaster.
- Boing Kit.
- Character Enhancement Toolkit.

Recommended disposition:

| Tool | Disposition | Rationale |
|---|---|---|
| Omni packs | USE CANDIDATE | Strong fit with UCC templates/workflow. |
| UMotion Pro | USE CANDIDATE | Retargeting, pose repair, weapon alignment, bespoke clips. |
| Final IK | CONDITIONAL | Add only for visible alignment/contact failures. |
| ACS | ISOLATED SPIKE / HOLD | Avoid overlapping animation ownership with UCC on the same player. |
| Malbers | HOLD | Specialized creature/non-human/second-consumer use, not competing player motor. |
| PuppetMaster | DEFER | Physics/recovery/network complexity is premature. |
| Boing Kit | POLISH HOLD | Secondary motion after readability/performance proof. |
| Character Enhancement Toolkit | LATER ART CANDIDATE | Use after faction/silhouette rules exist. |

## 5. Navigation, AI, and networking

Owned:

- A* Pathfinding Project Pro.
- FishNet free.
- Forge Networking Remastered.
- Clean Multiplayer Pro.
- Mirror.
- PUN Classic Free.
- PUN 2 Free.
- UCC PUN add-on.

Disposition:

| Tool | Disposition |
|---|---|
| A* Pathfinding Project Pro | Leading navigation candidate |
| FishNet | Network bakeoff front-runner |
| Mirror | Network bakeoff candidate |
| Unity Netcode for GameObjects | First-party bakeoff candidate |
| Clean Multiplayer Pro | Audit/reference; determine what it adds and owns |
| PUN 2 / UCC PUN add-on | Reference, not default new-project choice |
| PUN Classic | Reject for new production |
| Forge Networking Remastered | Hold pending maintenance/Unity 6.3 audit |

Networking enters only after stable movement, aim, firing, damage, shared-resource, power-event, and representative enemy-state contracts exist.

## 6. Authoring, level, world, and environment tools

Owned:

- Odin Inspector and Validator.
- UModeler.
- GSpawn Level Designer.
- Gaia Pro.
- GeNa Pro.
- Ambient Sounds.
- Pegasus.
- SECTR.
- Mega Stamp Pack and related Procedural Worlds tools.
- Dungeon Architect.
- MicroSplat.
- Polaris Summit.
- Enviro 3.
- Decalery.
- Compass Navigator Pro 3.

Disposition:

| Tool | Disposition |
|---|---|
| Odin Inspector/Validator | Strong candidate for definitions, diagnostics, and content validation |
| UModeler | Stage A greybox candidate |
| GSpawn | Stage A authored prefab/Synty composition candidate |
| Gaia/GeNa | Hold until theater scale proves a terrain/world need |
| SECTR | Profile-gated streaming/visibility |
| Dungeon Architect | Hold / possible later second-consumer or bounded procedural test |
| MicroSplat vs Polaris | Terrain-dependent; do not run parallel terrain ownership without a reason |
| Enviro 3 | Atmosphere candidate |
| Decalery | Faction/state/environmental storytelling candidate |
| Compass Navigator | Hold until HUD/navigation requirements exist |
| Ambient Sounds/Pegasus | Later presentation/trailer tools |

## 7. Art, VFX, shader, lighting, audio, and optimization tools

Owned VFX/presentation sources include:

- Flipbook VFX Bundle.
- Stylized VFX Bundle.
- VFX Graph Mega Pack Vol. 4.
- Epic Toon FX.
- Cartoon FX Remaster Free.
- Polygon Arsenal.
- Essential Trails VFX.
- Volumetric Fog & Mist 2.
- Epic Toon VFX 2.
- Highlight Plus 2.
- VFX Graph Ultra Mega Pack Vol. 1.
- Sci-Fi Arsenal.
- Volumetric Light Beam.
- Volumetric Lights 2.
- Low Poly Color Changer.
- Colorize Pro.
- Palette Fusion Pro.
- Amplify bundle.
- Bakery.
- Mesh Baker.
- Master Audio 2024.
- Build Report Tool.

Policy:

- Curate a small semantic VFX language; do not import whole catalogs.
- Standard URP shaders and Shader Graph are preferred.
- Amplify Shader Editor is `REFERENCE ONLY / DEFERRED` as a production dependency.
- Art tools are complementary, but each generated artifact must have a canonical writer and reproducible workflow.
- Bakery enters at polished-slice fidelity, not greybox.
- Mesh Baker is profile-gated.
- Master Audio 2024 is a candidate for semantic mix hierarchy and pooling.
- Build Report Tool replaces the need to buy Better Build Info unless it fails an actual requirement.
- Shapes and Hot Reload are not owned; do not buy without a measured deficiency.

## 8. Asset acceptance gates

Every runtime package entering production must pass:

1. **Compatibility:** Unity 6.3 import, required render pipeline, Windows development build, and credible Xbox path.
2. **Ownership:** canonical state and mutation responsibility are explicit.
3. **Testability:** important behavior can be exercised and observed without opaque scene-only magic.
4. **Production value:** time saved exceeds learning, integration, upgrade, debug, and removal cost.
5. **Representative behavior:** test under real enemy counts, effects, cameras, and session state.
6. **Exit path:** package update/removal does not redefine approved game contracts.

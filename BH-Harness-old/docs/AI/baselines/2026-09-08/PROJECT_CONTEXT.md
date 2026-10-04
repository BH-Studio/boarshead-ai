# BH Arcade Assault Project — PROJECT_CONTEXT

**Status:** `CURRENT / stable context`  
**Updated:** 2026-09-02  
**Authority:** Current explicit human decisions override this file. Update this file when stable project facts change.

## 1. Mission

Design and validate a modern low-poly 3D arcade-assault game inspired by the durable decision structures of:

- **Ikari Warriors:** independent movement and attack orientation; continuous offense while repositioning; co-op coverage; temporary power.
- **Heavy Barrel:** combat-linked pursuit and acquisition; scarce access resources; competing reward opportunities; temporary specialist tools; memorable earned power ritual.
- **Time Soldiers:** campaign state communicated through theme and location; consequential operation order/routes; environmental differences that change player policy.

The project is not a remake, nostalgia exercise, universal engine replacement, or direct continuation of VECTOR RIFT.

## 2. Product mission

The game should:

- Deliver a strong, frequent, visible assault-game verb before relying on meta progression.
- Keep the ordinary combatant satisfying without rare weapons, vehicles, or persistent stat growth.
- Use economy, routing, progression, and story to reinforce the high-frequency interaction rather than compete with it.
- Support solo and exactly two-player online co-op for the intended first commercial product.
- Use one or two consequential route choices per operation rather than repeated route menus.
- Treat temporary overwhelming power as the invariant; a vehicle is one possible expression.
- Use Synty Studios content as a production base while establishing a proprietary visual and semantic identity.
- Produce a focused reusable gameplay framework for later games with different storylines.

## 3. Candidate player promise

`CANDIDATE — not approved wording`

> Advance in one direction, fire in another, and steal the enemy’s power without stopping the assault.

Candidate market-facing form:

> A solo or two-player arcade-assault shooter where you stay mobile under overwhelming fire, raid enemy armories, and hijack battlefield power to break through fortress operations.

## 4. Ranked experience priorities

1. **Kinetic competence:** maintain an attack solution while repositioning under pressure.
2. **Cooperative rescue and crossfire:** create coverage, rescue, and role shifts through play.
3. **Power oscillation:** earn a spectacular but bounded period of dominance, then return to a satisfying baseline.
4. **Operation authorship:** route and resource decisions materially change later combat.

## 5. Binding source invariants

### Interaction invariant

> The player can maintain an attack solution while changing movement, and can change attack direction without involuntarily changing movement.

### Economy invariant

> Combat opportunities create resource decisions, and resource decisions alter later combat decisions.

### Campaign/theater invariant

> Theme, location, objective state, and tactical rules communicate one another.

## 6. Production context

- **Developer:** solo.
- **Availability:** evenings and weekends; time shared with family, two other game projects, and tooling work.
- **Employment:** current 8am–5pm job remains the primary constraint.
- **Funding:** self-funded; approximately **US$5,000** new project budget.
- **Staffing:** no contractors or employees unless significant up-front funding changes the context. Interns may be possible but cannot sit on the critical path.
- **Asset ownership:** all Synty packs plus a large Unity Asset Store library.
- **Development horizon:** flexible, with a strong preference for fast risk retirement rather than fast content accumulation.

## 7. Platform and session context

- **Engine:** Unity 6.3 LTS.
- **First-game render pipeline:** URP.
- **Gameplay-framework render dependency:** core gameplay must not depend on URP or HDRP.
- **Primary platform:** PC.
- **Probable additional first-release platform:** Xbox, subject to platform access, licensing, certification, performance, and budget.
- **Mobile:** deferred and demand-gated.
- **Performance target:** 60 FPS on the developer’s gaming laptop: Intel i7, 16 GB RAM, NVIDIA RTX 2070 Mobile.
- **Input:** gamepad and mouse/keyboard parity.
- **Launch contract:** solo plus exactly two-player online co-op.
- **Prototype format:** five-to-ten-minute arcade stages.
- **Compact premium target:** approximately ten-to-twenty-minute operations.
- **Longer operations / four-player co-op:** deferred product decisions, not hidden framework requirements.

## 8. Technical direction

- Use **Opsive Ultimate Character Controller** as the default character execution substrate wherever it cleanly satisfies approved behavior.
- Extend UCC through supported seams before creating parallel movement, item, interaction, or character-state systems.
- Keep operation, encounter, requisition, power-event, persistence, and session policy outside UCC-local state.
- Use **Behavior Designer Pro 3** as the leading AI decision-orchestration candidate, with project-owned encounter, attack-reservation, and canonical combat state.
- Use **A* Pathfinding Project Pro** as the leading navigation candidate; UCC remains the final movement/collision owner.
- Prefer Rewired as the initial input candidate, subject to Unity 6.3/UCC validation.
- Start with UCC camera/view types; introduce Cinemachine only for an unmet approved camera requirement.
- Core gameplay emits semantic presentation cues; URP-specific presentation binds them to shaders, VFX, lighting, and UI.
- Do not claim reusable framework success until a clean Ashfall Raiders consumer works without core changes.

## 9. Rejected product canon

VECTOR RIFT is `REJECTED` as the active concept. The following are not canon:

- Five eras or a five-era campaign.
- Time travel as the first game premise.
- Portals, Temporal Anchors, or fiction-specific framework vocabulary.
- Exact six-module assembly.
- Five themed vehicles.
- VECTOR RIFT’s mode list, local/online co-op bundle, replay scope, milestone plan, or oversized vertical slice.
- Shared top-down camera as a settled contract.
- Objective/Arsenal/Stability as a fixed route grammar.

Selected architecture and validation lessons may be reused only after generalization.

## 10. Current concept set

- **Iron Meridian:** leading `CANDIDATE`, not approved.
- **Black Sky Protocol:** `DEFERRED / archive alternative`.
- **Ashfall Raiders:** `DEFERRED / archive alternative` and preferred second-consumer candidate.
- **Vector Rift:** `REJECTED for first development / archive only`.

## 11. Non-goals

- No universal engine.
- No live-service assumption.
- No loot-rarity treadmill or mandatory gear score.
- No strong permanent health/damage grind.
- No many-mode product before the operation loop is proven.
- No full deterministic public replay before it earns priority.
- No broad procedural-generation commitment before authored product proof.
- No package-shaped design.
- No Marketplace-asset collage.
- No simultaneous ownership of the same responsibility by multiple middleware systems.

## 12. Proof order

1. Interaction proof.
2. Source-inheritance proof.
3. Product proof.
4. Framework/second-consumer proof.
5. Polished vertical slice.
6. Full production only after an explicit product decision gate.

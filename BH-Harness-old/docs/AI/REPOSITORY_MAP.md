# Repository bindings and command registry

Package: B1-CODEX-OPS | Version: 0.1.0 | Prepared: 2026-09-08
Status: CANDIDATE workflow; effective only after human adoption.

## Current binding status: UNINSPECTED

No Breach One checkout was supplied or audited for this pack. Entries below are intentionally
unbound. They are not a claim that a file, command, assembly, scene or package exists. The first
audit reads files only; it does not open Unity or run repository scripts. Use
`templates/REPOSITORY_AUDIT.template.md` to return observations. Map updates require delegated
document-edit authority; otherwise return proposed updates in the audit response.

| Binding | Observed value | Status |
|---|---|---|
| Repository root / branch / commit / initial dirty diff | Not supplied | UNINSPECTED |
| Applicable instruction chain and overrides | Not supplied | UNINSPECTED |
| Current canonical context/state/decision paths | Not supplied | UNINSPECTED |
| Approved active system and milestone paths/revisions | Not supplied | UNINSPECTED |
| Unity project root and editor patch | Not supplied | UNINSPECTED |
| Project-owned runtime, editor and test roots / asmdefs | Not supplied | UNINSPECTED |
| Vendor roots, installed middleware versions and integration packages | Not supplied | UNINSPECTED |
| Scenes, test fixtures, build profiles and input assets | Not supplied | UNINSPECTED |
| Safe evidence output paths / retention / ignore policy | Not supplied | UNINSPECTED |
| Unity license, target modules, GPU and multiplayer-test capability | Not supplied | UNINSPECTED |
| Target hardware/settings and representative workload | Not supplied | UNINSPECTED |
| Save fixtures and compatibility baselines | Not supplied | UNINSPECTED |

Conventional discovery candidates include `ProjectSettings/ProjectVersion.txt`,
`Packages/manifest.json`, `Packages/packages-lock.json`, `Assets/`, `.asmdef` files and existing
CI/test harnesses. These names guide inspection; they do not imply this checkout contains them.
Do not create an assumed `Assets/BreachOne` architecture to fill an empty map.

## Register commands only after inspection

For each command, record ID, exact executable/arguments, working directory, shell/OS, script
path and inspected revision/hash, Unity/test-framework version, inputs and test selection,
outputs, prerequisites, expected discovery/result rule, timeout/cancellation, side effects,
permission requirements, and status: DISCOVERED / INSPECTED NOT RUN / VERIFIED / BLOCKED.
A command's presence in the repository is not authorization to execute it. No placeholder
command below is runnable. [B1-K09; EXT-UNITY-TEST]

| Command role | Bound command | Status |
|---|---|---|
| Build/static/compilation | None | UNBOUND |
| Focused EditMode | None | UNBOUND |
| Focused PlayMode | None | UNBOUND |
| Windows development player build/smoke | None | UNBOUND |
| Relevant authoritative regression | None | UNBOUND |
| Two-process co-op validation | None | UNBOUND |
| Performance/representative/stress | None | UNBOUND |
| Content/asset validation | None | UNBOUND |

If no harness exists, return that gap. An approved milestone may include creating one; a
read-only audit may not. A coding package must bind the commands needed for its final gates,
or clearly remain blocked for those gates. Never invent test filters or infer a pass from exit 0.

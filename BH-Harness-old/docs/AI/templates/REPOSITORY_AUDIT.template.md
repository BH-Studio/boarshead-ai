# Breach One repository audit — <actual audit ID>

Status: TEMPLATE — audit not performed
Mode: READ-ONLY; no Unity launch, repository-script execution or source/configuration edits
Request/owner/date: <actual>

## Repository identity and instruction chain

Root/project path, branch/commit, initial dirty status, applicable AGENTS/override/config paths,
actual client/surface/version if observable, trust/permission limits. Do not expose credentials.
Do not assume all nested instructions auto-loaded at startup; inspect affected scopes explicitly.

## Actual project baseline

| Area | Observed value/path | Evidence file/line/hash | Status/limit |
|---|---|---|---|
| Unity patch / URP / platform | <actual> | <actual> | <actual> |
| Canonical context/state/decisions | <actual> | <actual> | <approval/supersession status> |
| Approved active system/milestone | <actual or absent> | <actual> | <actual> |
| Source/runtime/editor/test asmdefs | <actual> | <actual> | <actual> |
| Vendor packages/integration versions | <actual> | <actual> | <installed versus approved> |
| Scenes/prefabs/definitions/input/build | <actual> | <actual> | <actual> |
| Save/contract/fixture owners | <actual> | <actual> | <actual> |
| Harnesses/artifact outputs/retention | <actual> | <actual> | <inspected, NOT RUN> |

## Ownership and dependencies

Trace only affected behavior. Identify actual owners/writers and existing extension seams,
duplicate movement/state risks and missing bindings. Do not prescribe an unapproved architecture.

## Command candidates (inspection only)

Record exact script/command/cwd/version, expected tests/outputs, inspected revision, prerequisite
Unity/target/license/GPU/network capability, side effects and required execution permission.
No command was run in audit mode; proposed verification stays NOT RUN.

## Conflicts and scoped blockers

Differentiate outdated snapshot, missing approval, engine/package mismatch, unowned contract,
unavailable runtime and absent harness. Describe the affected work and smallest resolving evidence.
Do not block unaffected tooling documentation on a game-design choice.

## Proposed repository-map update and next authorized action

Return changes as a proposal unless this request explicitly delegates the map file. Name the
specific first verification to authorize later, not a broad bootstrap or dependency import.

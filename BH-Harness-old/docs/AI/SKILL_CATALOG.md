# Skill catalog and trigger boundaries

Package: B1-CODEX-OPS | Version: 0.1.0 | Prepared: 2026-09-08
Status: CANDIDATE workflow; effective only after human adoption.

## How to use the pack

These are instruction-only skills: no bundled executable scripts, downloads, MCP dependencies
or account setup. The adopted root instructions name required reads. In an implementation,
use preflight and milestone implementation plus only the specialty skills needed by its scope.
A review request does not activate source-writing authority. Skills supplement the approved
package; they never fill missing design decisions or supersede it.

Local Codex skill discovery uses `.agents/skills/` and `SKILL.md` with name/description metadata.
Skill bodies load on use. The optional `agents/openai.yaml` policy makes compilation,
implementation and completion-report skills explicit-invocation only. These declarations are
not enforcement of design approval; the entry gates still apply. When discovery is unavailable,
read the exact `SKILL.md` path and follow it within the current task. [EXT-CODEX-SKILLS]

## Catalog

| Skill | Scope | Invocation policy |
|---|---|---|
| `b1-package-preflight` | Audit a Breach One coding package or checkout before work. Resolve approval, baseline, paths, capabilities and conflicts. Audit mode reads only; it never authorizes implementation. | Task-matched; also directly readable |
| `b1-package-compile` | Compile approved Breach One system and milestone records into a versioned Codex coding package. Use on explicit compilation requests, not to approve designs or implement code. | Explicit request; also directly readable |
| `b1-milestone-implement` | Implement an explicitly authorized Breach One milestone or focused iteration after package preflight. Not for design selection, archive review or an unapproved prototype. | Explicit request; also directly readable |
| `b1-unity-safety` | Review or modify Unity assets, serialization, lifecycle, assemblies and scene/editor setup within approved Breach One scope. Not a package-import or engine-upgrade authorization. | Task-matched; also directly readable |
| `b1-middleware-integration` | Inspect Breach One UCC, Behavior Designer Pro, navigation, input, camera and presentation integration seams. Enforce single ownership without choosing unapproved middleware. | Task-matched; also directly readable |
| `b1-gameplay-experiment` | Implement or review an authorized Breach One A/B gameplay experiment with controlled variants, resettable state and falsifiable measures. Does not select production camera, drone, revive or bot policy. | Task-matched; also directly readable |
| `b1-unity-validate` | Run or plan authorized Breach One validation across EditMode, PlayMode, built player and relevant integration gates. Discover real harnesses; never treat missing or zero-test runs as passes. | Task-matched; also directly readable |
| `b1-performance-scale` | Measure Breach One frame, AI, effects, network or persistence performance against a scoped workload and approved budget. Not for speculative optimization or copied Galaxy scale thresholds. | Task-matched; also directly readable |
| `b1-state-persistence` | Handle approved Breach One state, stable IDs, saves, migrations and compatibility changes. Apply determinism only where required; do not import galaxy-world formats or policies. | Task-matched; also directly readable |
| `b1-coop-authority` | Review or implement approved exactly-two-player Breach One authority, transactions, recovery and participant state. Not authorization to choose a network backend or add future session features. | Task-matched; also directly readable |
| `b1-narrative-contracts` | Check Breach One mission knowledge, reveals, shared information and narrative persistence against the scoped approved handoff. Not for new plot, runtime LLMs or unresolved consent/save policy. | Task-matched; also directly readable |
| `b1-evidence-review` | Review Breach One Codex evidence or cumulative integration against approved criteria. Read-only by default; report gaps and closure recommendations without accepting the milestone. | Task-matched; also directly readable |
| `b1-completion-report` | Produce evidence-backed Breach One completion/work records and proposed shared-state deltas at authorized paths. Does not mark human acceptance, approve deferrals or rewrite canon. | Explicit request; also directly readable |

Each skill lives at `.agents/skills/<listed-name>/SKILL.md`; metadata is in its `agents/openai.yaml`.
No skill creates an autonomous permanent persona. BH expert lenses in Design Chat remain
analytical perspectives, not claims of running separate agents.

## Kept out of the initial pack

No standalone milestone-design agent: Design Chat and the human retain product/architecture
selection; Codex can supply bounded evidence. No automatic approval or closure skill. No runtime
LLM authoring, procedural generation, modding/encryption, release publishing, console certification,
auto-installation, fleet coordinator or vendor-upgrade automation. Create one only after a repeatable
approved task exposes a real gap, a named owner, safe input/output contract and testable acceptance.

Potential later skills: scene/prefab authoring automation once paths/metadata/undo are validated;
release/build-pipeline delivery once targets are approved; and clean-consumer extraction once an
actual Ashfall Raiders slice exists. Current Unity/evidence skills cover those checks without
claiming new tooling or a second consumer already exists.

## Validate the skills themselves

Use the distribution's acceptance scenarios to check positive triggers, negative triggers,
unauthorized actions, evidence freshness and baseline drift. Parsing frontmatter proves syntax,
not that the installed host discovers or follows the skill. All live-host trigger tests are NOT RUN
in this drafting assignment. Record client/version and observed results before routine use.

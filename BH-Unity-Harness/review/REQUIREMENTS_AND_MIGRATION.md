# Requirements, ownership and migration — candidate 1.0.0

Baseline: `BH-Studio/boarshead-ai@0cffc7e090eccb2d0b453c2c2c5a0db4631650c8`. The attached task specification is prompt 1.1. Source-reading coverage is explicit in SOURCE_INVENTORY.json and the linked review records: all twenty-one design files and sixty legacy files have full recorded reads; external reviews are bounded selected-source comparisons. The latest human direction excludes actual game designs/names from operational content; historical references explain generic lessons only. No original/live source is superseded by merely generating this candidate.

## Required ownership and adoption matrix

| ID | Source / classification | Owner and disposition | Artifact / enforcement | Verification |
|---|---|---|---|---|
| BH-01 | Task §§2–3; legacy AGENTS §§1,4 / universal | Human final authority, preserve originals; retain | Branch-only authoring; installer boundary; no merge | Actual diff review + human adoption |
| BH-02 | v3 full §§1–4, K01 / design | Retain controller plus twelve specialist lenses, L0–L3 | Official + preserved full/K01; advisory host behavior | Capability map + live cases D01,D04,D09 NOT_RUN |
| BH-03 | v3 full §§5–6,11, K02–K07 / design | Retain five frameworks, evidence/counterevidence and real alternatives | Required resource map; no coding-cost prohibition on design exploration | D02,D03, source preservation; live NOT_RUN |
| BH-04 | v3 full §§6,10, K08,K11 / design, optional | Retain ownership/contracts/scale, second-consumer proof, persistence and tooling | Full method; optional procedural guidance; no universal RNG framework | D04,D08; synthetic profiles |
| BH-05 | v3 full §§6–7, K09,K12 / shared | Preserve question gates and separate system/milestone/plan approval | Handoff schema, exact approval subjects, runtime plan/begin | Negative approvals, identity/version/mapping tests |
| BH-06 | v3 full §§8–9 / design | Preserve periodic integration and final-system acceptance | Official/full/K12; human-owned | D15 + human acceptance |
| BH-07 | Legacy AGENTS §§1–2,5–6 / common | Replace copied game policy with shared core + thin approved overlay | Five skills, AGENTS, handoff references/hashes | Handoff validation and package tests |
| BH-08 | Task §§7,9 / shared interface | One owned contract 1.0.0; fail incompatible pairs | contracts/schema.json + INTERFACE.md, exact consumer copies | Copy identity, version and file tests |
| BH-09 | Task §§7,10 / authority | Human records are structure, not authentication | No executor actor, exact canonical subjects, manual confirmation | Self-certification negatives; residual same-permission risk |
| BH-10 | Task §§10–11 / state | Machine state is authoritative; checkpoint derived | Locked atomic state, unique IDs, legal phases, archive | Transition, interrupted/resume, stale state tests |
| BH-11 | Legacy AGENTS §4 / safety | Retain one writer; no destructive reset, stash, clean or force push | Wrapper lock + explicit host permissions; policy outside wrapper advisory | Lock/concurrency tests; local Editor pilot |
| BH-12 | Legacy AGENTS §5; task §§11,13 / evidence | No PASS without actual fresh artifacts | Process exit + XML/JSON parsing + AC mapping | Missing/zero/stale/wrong-project/wrong-task/failure tests |
| BH-13 | Task §11 / evidence | Dirty inputs, config, runtime and artifacts identify tested state | SHA-256 inputs and raw receipts; reparse on audit | Tamper/freshness/dependency tests |
| BH-14 | Task §§10–11 / audit | Audit cannot silently repair what it judges | Before/after snapshot; same-workspace independence label | Audit-mutation negative; no sandbox claim |
| BH-15 | Task §12 / efficiency | Five explicit skills, no trial catalog auto-discovery | .agents layout; optional folder outside template | Metadata/name/implicit-policy tests; live activation NOT_RUN |
| BH-16 | Task §13 / process | Explicit executable, argument arrays, reviewed inputs, timeouts | Python stdlib runtime + PowerShell launcher | Actual subprocess nonzero/timeout/cancel; Windows NOT_RUN |
| BH-17 | Task §§13–14 / Unity | Preserve installed version, .meta/GUID, assets, assemblies and saves | Unity policy, pinned binding, batch ownership checks | Local Unity checklist NOT_RUN; optional C# uncompiled |
| BH-18 | Legacy diagnostics requirement / integration | Preserve `sonarqube` source as observed history; discover live bridge | Pinned baseline/actual diagnostics parser, no invented MCP namespace | Synthetic diagnostics tests; actual bridge NOT_RUN |
| BH-19 | Task §14 / release | Development-only capabilities must not silently ship | Filename scan + manual assembly/network/config review | Actual scan tests; filename scan is not exhaustive proof |
| BH-20 | Task §15 / recovery | Preserve evidence; bounded failure/no-progress counters | Configured three-round defaults, one recovery, infra budget two | Threshold/recovery/resume tests; no blind automatic retries |
| BH-21 | Task §15; user cost constraint / cost | No paid runtime, fleets, model gateway, hidden quota assumptions | Ordinary design chat vs bounded Codex; no telemetry invented | Static inspection; comparative real usage NOT_RUN |
| BH-22 | Task §16 / install | Preview/apply/rollback, exact approval, preserve local changes | installer/install.py + PACKAGE_FILES.json | Actual installer positive/negative tests |
| BH-23 | Task §16 / migration | Existing policy is a conflict, not something a backup authorizes replacing | Manual AGENTS merge; every unregistered active skill must be reviewed | Installer conflicts; generic preflight registry/review checks |
| BH-24 | Task §§6,16 / design deployment | Exactly one field + 15 reference files; no patch-only GPT | Complete official/K12/interface and exact preserved refs | Budget/hash/manifest; live host NOT_RUN |
| BH-25 | Task §§7,17 / round trip | Actual subprocess evidence, human pending, portable review bundle | tools/export_examples.py and negative inputs | Exporter observed results; no synthetic game-approval claim |
| BH-26 | Task §17 / evaluation | Compare like-for-like, no invented savings/winner | Local integration + D01–D20; fixed-host evaluation protocol | NOT_RUN until actual configured hosts measured |
| BH-27 | Task §18 / assurance | Challenge false success and bypasses; same-author label | ASSURANCE.md, corrected build classification | Regression reruns; residual risks explicit |
| BH-28 | Task §§3,19 / delivery | Candidate files vs published files must be distinguished | BUILD_CHECKPOINT, DELIVERY_AND_CONTINUATION, hashes/patch | Readback of actual published tree/diff |

## Legacy skill-to-target map

| Legacy skill | Retained responsibility and new location |
|---|---|
| b1-package-compile | Producer design-gpt/K12 and shared interface; no duplicate core regeneration |
| b1-package-preflight | bh-review-handoff + bh-unity-preflight; exact scope/approvals/environment |
| b1-milestone-implement | bh-implement-approved-slice; approved behavior, narrow changes |
| b1-completion-report | bh-review-handoff + runtime return with AC/evidence mapping |
| b1-evidence-review | bh-unity-verify + producer evidence review, human closure |
| b1-unity-validate | bh-unity-verify; actual NUnit/build/content/performance profile |
| b1-unity-safety | Core AGENTS, Unity operating guide, project overlay |
| b1-middleware-integration | Project-owned integration seams, no vendor-source default repair |
| b1-performance-scale | Design K08/K11/K12 and configured facts/tests; optional procedural skill |
| b1-state-persistence | Approved project invariants/schema/migration and integration gates |
| b1-coop-authority | Approved project-specific participant/transaction contracts; no standard player count, role equality or network backend |
| b1-narrative-contracts | Project overlay + Nina/approved narrative status; no silently canonized fiction |
| b1-gameplay-experiment | Explicitly approved experiment scope; design validity and playtest separate from code tests |

The sixty full legacy reads are recorded in LEGACY_SOURCE_REVIEW.md and LEGACY_SKILL_REVIEW.md. This map retains transferable responsibilities, not game rules. The large historical narrative was selectively inspected and is excluded from operational inputs; a future real-game migration must retrieve that project’s applicable current approved records. The originals remain unchanged.

## Synthetic profiles only
The earlier named-game overlay is withdrawn and removed from current examples under the latest human scope clarification. Its history remains available for provenance, not deployment. `examples/profiles/synthetic-discrete-state.json` and `synthetic-continuous-state.json` demonstrate contrasting time/state contracts, contain no real product design, enable no capabilities and retain unresolved real-environment questions. They are not executable real-game overlays or approval records. Generate a real overlay only from that expressly identified project’s current approved inputs.

The exporter creates two **synthetic** URP/HDRP counter projects with different identities and observed outcomes. These exercise isolation; neither is an invented claim about a real studio game. Procedural seed/save rules are optional and must be derived from a project's own approved contracts.

## Migration and rollback
Finish or explicitly cancel/archive the current slice before changing harness/method versions. Preserve a readable completion/continuation packet and current instructions. Preview a separate game clone first; inspect every conflict. Do not bulk-copy BH-Harness-old, Reference, design-gpt or the authoring repository into Assets. Selectively merge retained rules and record the exact decision. Disable/remove any superseded or conflicting local skills only with explicit path-specific approval and preserve them outside active discovery; the installer does not delete them. Retain the old live GPT while piloting the new method in a separate ordinary Project (or existing test GPT).

After local checks, a human may adopt the paired 3.1.0 / 1.0.0 / 1.0.0 versions for a new task. In-flight tasks remain pinned until a controlled migration. Roll back only unchanged installer-managed files using the recorded transaction; preserve edited project seeds. Keep design state/history and restore the previous GPT instruction/knowledge selection only through an authorized host action. Existing accepted game decisions do not become unapproved merely because a different harness is being evaluated.

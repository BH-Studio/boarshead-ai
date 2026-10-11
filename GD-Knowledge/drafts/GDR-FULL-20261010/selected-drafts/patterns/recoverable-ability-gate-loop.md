---
id: GDR-CAND-20261010-G02-PAT-02
kind: pattern
title: Recoverable ability-gate loop
version: 0.1.0
status: draft
candidate_revision: initial-1
run_id: GDR-FULL-20261010
batch_id: G02
attempt_id: G02-authoring-attempt-01
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate plus supplied G02 dispatch
aliases:
- recoverable capability gate
- known-barrier return loop
- ability-led route reinterpretation
tags:
- ability-gating
- navigation-recovery
- conditional-topology
- backtracking
- hint-choice
related_topics: []
related_patterns:
- GDR-CAND-20261010-G02-PAT-01
related_genres:
- GDR-CAND-20261010-G02-GEN-01
- GDR-CAND-20261010-G02-GEN-02
- GDR-CAND-20261010-G02-GEN-03
source_ids:
- GDR-SRC-20261010-G02-005
- GDR-SRC-20261010-G02-006
- GDR-SRC-20261010-G02-007
- GDR-SRC-20261010-G02-009
- GDR-SRC-20261010-G02-010
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed
predecessor_sha256: null
supersedes: null
superseded_by: null
change_summary: Initial G02 candidate; no predecessor submitted
hash_record: ../reviews/full-run-20261010-g02-review-packet.md#candidate-inventory-and-byte-integrity
proposed_shared_owner: 'Pending coordination: Worlds and Characters with Foundations
  and Systems and Presentation and Interaction'
recommendation_confidence: low; creator accounts support ingredients, combined causal
  benefit unvalidated
---

# Recoverable ability-gate loop

> **Draft research candidate, not released guidance.** Version 0.1.0; candidate revision `initial-1`; independent review not performed. Definitions and proposed adaptations below are bounded inferences or hypotheses, not an approved studio design. No game build, gameplay recording, prototype or player test was run in this batch.

The supplied G02 dispatch authorizes this batch and supersedes old starter-phase sequencing restrictions only. Its final parent reconciliation records completed, independently reviewed first-wave drafts, but those reviewed bytes were not retrieved here. No unseen F01/P01 wording or numerical settings are inherited. No reviewed shared guidance is transferred in this entry. [Workflow basis: supplied `Pasted text.txt`, Assigned outputs; Genre-specific questions; Parent review reconciliation.]

## Purpose and scope

**Candidate purpose:** make a previously encountered obstacle become a meaningful new opportunity after a capability change, while preserving a way to recover an actionable plan. “Recoverable” has two independent senses: the world state permits an acceptable continuation, and the player can regain enough information to choose one. Neither implies an automatic destination marker or a promise to prevent every moment of uncertainty. [C-01; C-03]

This is a genre-neutral spatial/progression recipe with metroidvania-relevant evidence. It can apply to a hub adventure or other persistent-world design when an acquired action reinterprets a known place. It is not a generic reward loop, a recommendation to add locks to every map or a rule that every ability must require backtracking. No local implementation or causal player benefit has been tested. [C-01]

**Ownership:** authored in BH-GDR-Genres for this batch; shared conceptual ownership is proposed for Worlds and Characters, coordinated with Foundations and Systems for progression/ability semantics and Presentation and Interaction for recovery information. Coordination has not assigned a permanent home or ID.

## Context and prerequisites

The world must retain relevant state and support a recognizable relation between the barrier and the acquired capability. A return or connection should contribute to the intended experience: reinterpretation, route choice, orientation, meaningful traversal or explicitly chosen familiar transit. The player must have another viable activity before acquisition and an acceptable continuation from supported post-acquisition states. These are proposed prerequisites of this pattern, not requirements for all exploration games. [C-03; C-04]

Record whether the barrier is actually an ability lock. A key possession, story flag, resource cost, knowledge discovery or execution demand can be a different mechanism. When conditions combine, record all of them. Otherwise a “new movement ability” tutorial may conceal a combat or resource prerequisite that the player cannot satisfy. [C-03]

The pattern assumes the production team can review conditional connections and maintain barrier/ability information across saves, alternate acquisition order and assistance configurations. A diagram alone cannot demonstrate what a player notices or can physically execute. No state enumeration or graph validation was run in this batch. [C-03; C-06]

## Mechanism and evidence by causal link

| Proposed link | Inspected support | Evidence limit |
|---|---|---|
| A capability can make previously encountered space newly actionable | Nintendo's Metroid Dread report describes ability-led exploration and revisits | Creator/publisher account, prerelease, not measured recognition. `practitioner-heuristic` [C-02; GDR-SRC-20261010-G02-009, §§4–5] |
| A recognizable relation plus recoverable information may help a player identify the changed opportunity | Official mapping discussion and Team Cherry's uncertainty/shortcut account motivate the question | The combined mechanism is new synthesis, not tested in either account. `hypothesis` [C-01; GDR-SRC-20261010-G02-009; GDR-SRC-20261010-G02-010] |
| Returning and crossing may create a meaningful reinterpretation or useful connection | Plausible consequence when the local return has a declared purpose | Travel and acquisition can instead become a chore; no universal benefit. `hypothesis` [C-04] |
| Separate reachability and information reviews can expose different failure classes | Follows from conditional-state versus player-knowledge reasoning | Does not prove completeness, accessibility or efficacy. `inference` [C-03; C-06] |

The candidate remains **low confidence for causal benefit**. Multiple creator contexts do not become independent experiments, and different navigation emphases are not a controlled test of markers versus uncertainty. [C-01; C-02]

## Actionable recipe

1. **Declare the intended return decision.** State what should be different when the player comes back: a reachable route, a newly meaningful surface, a changed interpretation or a connection. Also state what should remain uncertain. If the return has no intended value, compare forward-only use or immediate crossing instead. [C-04]
2. **Specify the barrier condition and available evidence.** Record the required action/state and any additional resource, combat, knowledge or narrative condition. Make the relevant relation available through appropriate forms, text or interaction response; do not rely on a single color or an unexplained name. A mystery can conceal an answer while still providing its necessary evidence. [C-03; C-06]
3. **Provide a viable branch before acquisition.** An encountered barrier should not leave the player with no acceptable activity unless deliberate confinement is a separately designed and communicated puzzle. Check that searching for the capability does not itself require that capability through a circular dependency. [C-03]
4. **Teach or expose the new capability's relation.** Demonstrate an actionable use or allow a safe investigation near acquisition. Do not assume that owning an item teaches its spatial application. Retain a path back or an alternative continuation; acquisition should not silently commit the player to an unsupported execution demand. [C-03; C-05]
5. **Offer proportionate recovery information.** Choose among a distinctive landmark, personal marker, capability recap, remembered-lead list or optional stronger hint. Separate reminders about known space from disclosure of unknown space. Make hint use a deliberate choice when discovery is at stake; do not prescribe a universal hint ladder. [C-01; C-05]
6. **Author the return and crossing.** Preserve a recognizable relation, then make the new capability matter. Compare repeating the old approach, changing part of it, creating a connector or placing the reward forward. If the design intentionally retains familiar transit, label that purpose rather than reporting it as new discovery. [C-04]
7. **Review exits and supported states.** Consider ability order, consumables, bypassed encounters, one-way entries, death/save state and assistance. Identify an acceptable continuation for each essential supported arrival state. Then separately ask whether a player can identify an actionable lead. No formal graph tool is prescribed or run here. [C-03; C-06]
8. **Test reinterpretation, recovery and agency separately.** Compare the intended loop against an appropriate forward-use or lower-information alternative. Track recognized opportunities, chosen help, wrong-condition revisits and burdensome transit. Narrow or remove the loop if its benefit does not justify its cost for the intended experience. [C-07]

**Exit conditions:** the ability/barrier relation cannot be communicated without giving away an intended puzzle; there is no acceptable pre-acquisition branch; supported arrival states can trap the player; the return contributes no declared value; assistance repeatedly removes the intended decision; or the obstacle is actually a different gate mechanism that needs a different recipe. An exit from this recipe can mean a forward route, clearer puzzle evidence, an alternate return or a separate combat/access solution. [C-03; C-04; C-05]

## Adjustable variables

| Variable | Decision and local consequence |
|---|---|
| Barrier exposure | Encounter before acquisition, after acquisition or either; prior exposure creates memory demands as well as possible anticipation |
| Relationship clarity | Obvious action relation versus deliberate inference; preserve accessible evidence for the chosen demand |
| Return cost | Travel, hazards, resources and attention, not distance alone; name the purpose of each cost |
| Route multiplicity | Alternative activities and acquisition orders; greater choice increases state-review obligations |
| Recovery information | Landmark, personal annotation, recap or hint; distinguish reminders from spoilers |
| Connection reward | Shortcut, new region, changed perspective or optional content; test whether it matters without coercion |
| Persistence | What survives death, departure or assistance changes; incorrect retained hints can create false leads |
| Execution burden | Traversal/combat requirements along the return; do not call a route accessible merely because it is unlocked |

These are proposed tuning dimensions, not numerical recommendations or empirical laws. More locks, larger maps, more connections and stronger markers are not automatic improvements. [C-03–C-06]

## Worked examples

### Illustrative: a magnetic bridge mechanism

**Illustrative, not a game observation or a completed prototype.** A fictional research station has a hub, a gallery and a maintenance ring. The gallery contains a retracted bridge whose anchor surfaces have a distinctive physical form. A safe side route reaches the maintenance ring and grants a pull action. An adjacent small object demonstrates that action before any required long traversal. [C-08]

The return purpose is to reinterpret the gallery mechanism, cross into an observation room and open a connector to the hub. The relation can be expressed visually and through an inspectable description that uses the actual localized action name. A player who did not see the gallery first can still solve the bridge when arriving later; prior exposure is an opportunity, not a compulsory memory test. [C-05; C-08]

Compare two proposed recovery options: a user-placed gallery marker and a requested recap of previously inspected mechanisms. The recap may remind the player of a known mechanism without announcing all undiscovered bridge sites. Ask what the player can now choose, not simply whether they move toward the intended location. [C-05; C-07]

Mechanically, the observation room cannot require an expended single-use resource for its only exit unless a replenishment or safe recovery is deliberately provided. Informationally, the newly opened connector should have enough identity for the player to understand where it leads. These are separate reviews. A reliable exit is not proof that a player recognizes it. [C-03; C-08]

### Illustrative counterexample: the memory puzzle

A different fictional game makes identifying **which** old mechanism matches a clue its central puzzle. Automatically highlighting the gallery immediately after acquisition resolves that puzzle on the player's behalf. Retain accessible clue review and deliberate optional spoiler help instead. The pattern's informational recovery must serve the intended reasoning, not assume all uncertainty is accidental. [C-05; C-08]

### Creator-described contrast, not an observed game sequence

Metroid Dread's prerelease mapping/ability account and Hollow Knight's Crossroads tour frame exploration differently. They motivate testing the information contract but do not verify either illustrative map above. Their platforms/build limits and exact textual locators are recorded in References; no game recording was watched. [C-02; GDR-SRC-20261010-G02-009; GDR-SRC-20261010-G02-010]

## Alternatives, tradeoffs and opportunity costs

**Forward-only capability use** avoids the memory and return burden when reinterpretation is not a goal. **Immediate visible crossing** teaches an action without requiring a deferred plan. **Ungated optional discovery** can preserve exploration without a lock schedule. **A local knowledge puzzle** may use revisited information without changing movement capability. Choose these as genuine alternatives rather than assuming the pattern must be salvaged. [C-04]

An optional hint can protect re-entry after absence but may change the experience of inference. A connector can reduce repeated travel but can also bypass intended encounters or landmark learning. More acquisition-order freedom may increase choice while increasing production state combinations. A combat assist may open an already understood route without solving any navigation problem. These are distinct tradeoffs; no single genre label chooses among them. [C-04; C-05; C-06]

The accessibility basis is scoped general input/difficulty guidance, not a navigation study. Consider memory, perception and motor demands separately, and do not assume that an inventory of map features certifies cognitive access. Localized action names, marker descriptions and world-state messages should preserve the same relation across versions and control mappings. [C-06; GDR-SRC-20261010-G02-005; GDR-SRC-20261010-G02-006; GDR-SRC-20261010-G02-007]

## Failure cases and do-not-use conditions

| Failure | Warning sign | Candidate response |
|---|---|---|
| Circular dependency | The only route to an ability requires that ability or a resource obtainable only beyond its gate | Redesign the branch or explicitly support an alternate solution; do not call it player confusion |
| False gate classification | Player has the action but an undisclosed flag/combat condition still blocks the route | Record and communicate the real condition; reconsider the prerequisite |
| Memory cliff | Player understands the action but cannot identify any relevant known location | Test landmark/annotation/recap alternatives before revealing the whole route |
| Hint overreach | Assistance answers the intended inference before the player chooses help | Separate reminder from solution and make stronger disclosure deliberate |
| Empty return | Repeated transit consumes attention without its declared value | Shorten/reconnect, add a meaningful changed relation, or use the ability forward |
| Practical soft lock | Supported ability/resource/input state has no acceptable continuation | Add recovery or revise the commitment; verify with the supported state matrix |
| Inaccessible relation | A color, wording or input demand is the only path to understanding/execution | Provide an appropriate alternative representation or route; test with affected users |
| Stale progression information | A recap or marker describes a gate that has changed state or requirements | Maintain persistence and localization state; do not treat a map overlay as static art |

Do not use the pattern simply to increase map size, create arbitrary errands, stretch engagement, justify selling hints or force a metroidvania identity onto a linear traversal game. Do not interpret “recoverable” as a requirement that every route have a free reverse edge; deliberate commitments can exist with a communicated, acceptable continuation. [C-03–C-06]

## Proposed playtest and falsification

**Not performed.** Specify the intended information contract and acceptable continuation before testing. Recruit for navigation familiarity, interruption/re-entry conditions and relevant sensory, cognitive and motor access needs. Obtain consent for route logging and allow hints, pauses and withdrawal without stigma. No sample size or success threshold is prescribed. [C-07]

Compare a deferred known-gate return with an equally understandable forward-use alternative. Separately compare recovery aids while holding required capability and relevant route cost stable. Counterbalance layouts where possible; prior exposure, map familiarity, reward salience, combat and traversal difficulty are confounds. Do not compare a familiar gated route against a wholly different and harder “control” route. [C-07]

Measure recognition of changed opportunities, selected next activity, wrong-condition revisits, time without an actionable plan, hint choice, unwanted spoilers, meaningful decisions during return and fatigue. Add an unseen relation using the same ability when testing rule transfer; revisiting a known barrier only tests part of that claim. A proposed state audit should check reachability separately from participant comprehension. [C-07]

Reject or narrow the recipe when deferred exposure creates burden without the intended reinterpretation, when stronger help erases the central discovery, when a simpler forward route serves the promise better, or when a supported state has no acceptable continuation. An increase in travel or map completion is not itself evidence of improved exploration. [C-07]

## Claim ledger

| ID | Material claim and class | Evidence and scope | Confidence and remaining limit |
|---|---|---|---|
| C-01 | A recoverable known-gate loop may support capability-led reinterpretation without automatic solution disclosure. `hypothesis` | GDR-SRC-20261010-G02-009 §§4–5 and GDR-SRC-20261010-G02-010 region account motivate the synthesis | Low causal confidence; no navigation experiment or build observation; G02-CON-03 |
| C-02 | The inspected creator accounts describe different exploration/assistance emphases. `practitioner-heuristic` | GDR-SRC-20261010-G02-009 §§4–5; GDR-SRC-20261010-G02-010 opening/region paragraphs | High for attributable text, low for superiority or population effects; prerelease scope |
| C-03 | Gate mechanism, conditional physical reachability and recoverable player information are different audit targets. `inference` | State/knowledge reasoning made explicit in this recipe | Moderate logical basis; no actual audit and no completeness guarantee |
| C-04 | Return cost and connection choices need an intended purpose; forward-only or immediate use can be preferable. `hypothesis` | Creator accounts provide context; alternatives are new local synthesis | Low comparative efficacy; familiar transit may serve rest rather than discovery |
| C-05 | Recovery help should be calibrated to the information contract and can otherwise spoil the intended inference. `inference` | GDR-SRC-20261010-G02-009/GDR-SRC-20261010-G02-010 contrast plus explicit puzzle counterexample | Moderate conditional logic; exact assistance choice needs player evidence |
| C-06 | Route requirements and state combinations need separate access/localization/production review. `inference` | GDR-SRC-20261010-G02-005 Introduction; GDR-SRC-20261010-G02-006 input demands; GDR-SRC-20261010-G02-007 mechanic-specific options; C-03 logic | Moderate rationale; no metroidvania-specific access evaluation or certification. G02-CON-05 |
| C-07 | Validation must distinguish actionable recovery, rule transfer, agency and simple completion. `hypothesis` | Proposed comparison and measures, supplied evidence rules/F01 correction constraint | Low protocol confidence until piloted; no tests performed |
| C-08 | The station/bridge and memory-puzzle scenarios illustrate the recipe and its limits. `hypothesis` | Synthetic constructions, not shipped-game observations | Low empirical confidence; specific topology and effects untested |

## Related entries, coverage and history

The primary conditional genre adaptation is [metroidvania](../genres/metroidvania.md), `GDR-CAND-20261010-G02-GEN-03`. [Platformer](../genres/platformer.md) and [precision platformer](../genres/precision-platformer.md) apply only when traversal/execution participates in the loop. [Bounded action grace](bounded-action-grace.md) changes command eligibility, not the ability to recall an old route.

F03 progression, F04 movement, W03 spatial/exploration and P02/P03 input/camera remain missing shared dependencies; no reviewed bytes or canonical links are transferred. Research covered creator-described relationships, conditional state reasoning, alternatives and general access guidance. It did not establish optimal map size, lock density, hint timing, interruption recovery efficacy, soft-lock freedom or participant outcomes. The next discriminating question is whether the return enables a valued new interpretation compared with a simpler forward-use route.

**Author self-review:** the strongest proposed benefit could be an author preference for tidy loops. Players may value ambiguity, linear momentum or incidental wandering instead. The recipe therefore requires a declared return purpose, a forward-use comparator and deliberate information choice; it remains a low-confidence candidate, not a universal design rule. No independent review has occurred.

Version `0.1.0`, candidate revision `initial-1`; predecessor/supersession null. Exact bytes are in the [packet](../reviews/full-run-20261010-g02-review-packet.md#candidate-inventory-and-byte-integrity). Gate C independent review pending; Gate D host tests and Gate E release not passed. No adoption, engine or repository action is authorized.

## References

### GDR-SRC-20261010-G02-005

**Microsoft Xbox accessibility team. [Xbox Accessibility Guidelines V3.2](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines).** Microsoft Learn. Publication/update: V3.2 published 2023-06-08; inspected page last updated 2026-08-14.

Edition/build: V3.2 hub as served 2026-10-10; page date is distinct from guideline-set version. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary non-normative platform guidance.

**Inspected locator:** Introduction; Overview of XAG components → Example content; version heading and last-updated footer.

**Claims supported here:** C-06. **Limits:** The introduction explicitly excludes compliance/legal-checklist status; no formal-standard claim is made. **Independence:** Common guidance family with GDR-SRC-20261010-G02-006 and GDR-SRC-20261010-G02-007; not independent empirical studies. **Rights:** Microsoft documentation; paraphrase only, example images not redistributed.

### GDR-SRC-20261010-G02-006

**Microsoft Xbox accessibility team. [Xbox Accessibility Guideline 107: Input](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107).** Microsoft Learn. Publication/update: 2026-03-04 last updated on opened page.

Edition/build: XAG 107 page within V3.2 set; live page snapshot checked 2026-10-10. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary non-normative accessibility/input guidance.

**Inspected locator:** Goal; Overview; Background and foundational information → Speed, Complexity, Duration and proposed alternatives; Implementation guidelines → remapping and updated prompts; mobile-input section reviewed for scope only.

**Claims supported here:** C-06. **Limits:** No game-independent timing, sensitivity, target-size or compliance requirement is inferred; core article text was accessible despite an authorization banner. **Independence:** Same XAG guidance family as GDR-SRC-20261010-G02-005/GDR-SRC-20261010-G02-007; cited third-party examples are not additional observations. **Rights:** Microsoft documentation; paraphrase only; embedded example media not inspected as gameplay.

### GDR-SRC-20261010-G02-007

**Microsoft Xbox accessibility team. [Xbox Accessibility Guideline 108: Game difficulty options](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/108).** Microsoft Learn. Publication/update: 2026-03-04 last updated on opened page; an earlier search result showed another date, not adopted.

Edition/build: XAG 108 page within V3.2 set, checked 2026-10-10. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary non-normative accessibility guidance.

**Inspected locator:** Goal; Overview; Scoping questions and individual game-mechanic adjustment guidance.

**Claims supported here:** C-06. **Limits:** Options are design guidance, not a guarantee of access for every player or a formal standard; text accessible despite authorization banner. **Independence:** Same guidance family as GDR-SRC-20261010-G02-005/GDR-SRC-20261010-G02-006. **Rights:** Microsoft documentation; paraphrase only.

### GDR-SRC-20261010-G02-009

**Nintendo; attributed Metroid Dread development-team transmissions. [Metroid Dread Report Vol. 3: Seven points that define the 2D saga](https://www.nintendo.com/en-gb/News/2021/July/Metroid-Dread-Report-Vol-3-Seven-points-that-define-the-2D-saga-2007780.html).** Nintendo UK. Publication/update: 2021-07-15.

Edition/build: English pre-release report for Nintendo Switch; executable build unspecified. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary publisher explanation with creator-attributed intent.

**Inspected locator:** §4 Exploration → Icon Highlight, Marker, Zoom, Hidden item hints and development-team transmission; §5 Arsenal and abilities and following transmission.

**Claims supported here:** C-01, C-02; C-04/05 context. **Limits:** Describes planned affordances and intent, not observed post-release navigation success, exact topology or universal genre definition. **Independence:** One Nintendo/Metroid account; later reports are related, not independent confirmation. **Rights:** Nintendo copyright; paraphrase only, maps/images not redistributed.

### GDR-SRC-20261010-G02-010

**Team Cherry; displayed byline Team Cherry Press. [The Forgotten Crossroads — A Hollow Knight Tour](https://www.teamcherry.com.au/blog/the-forgotten-crossroads-a-hollow-knight-tour).** Team Cherry. Publication/update: unknown year; rendered page shows October 11 only and describes an upcoming game.

Edition/build: Pre-release region tour, platform/build unspecified. Accessed **2026-10-10**; access: `full`; type: Primary creator/publisher region overview.

**Inspected locator:** Opening introduction; paragraphs beginning The Crossroads are made up and Most travellers may shun the Crossroads.

**Claims supported here:** C-01, C-02; C-04/05 context. **Limits:** Initial disorientation, skill growth and route-finding are creator claims; no observation of shipped Hollow Knight or measured benefit. **Independence:** Distinct production context from Nintendo and Thomas Happ; promotional account rather than independent experiment. **Rights:** Team Cherry copyright; paraphrase only; screenshots not redistributed or treated as played scenes.

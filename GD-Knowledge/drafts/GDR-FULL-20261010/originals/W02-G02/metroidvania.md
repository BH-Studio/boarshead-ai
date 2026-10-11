---
id: GDR-CAND-20261010-G02-GEN-03
kind: genre
title: Metroidvania
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
- ability-gated exploration
- capability-led interconnected exploration
tags:
- ability-gating
- topology
- backtracking
- landmarks
- navigation-recovery
- hybrid-traversal
related_topics: []
related_patterns:
- GDR-CAND-20261010-G02-PAT-01
- GDR-CAND-20261010-G02-PAT-02
related_genres:
- GDR-CAND-20261010-G02-GEN-01
- GDR-CAND-20261010-G02-GEN-02
source_ids:
- GDR-SRC-20261010-G02-005
- GDR-SRC-20261010-G02-006
- GDR-SRC-20261010-G02-007
- GDR-SRC-20261010-G02-009
- GDR-SRC-20261010-G02-010
- GDR-SRC-20261010-G02-012
- GDR-SRC-20261010-G02-013
- GDR-SRC-20261010-G02-014
- GDR-SRC-20261010-G02-015
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed
predecessor_sha256: null
supersedes: null
superseded_by: null
change_summary: Initial G02 candidate; no predecessor submitted
hash_record: ../reviews/full-run-20261010-g02-review-packet.md#candidate-inventory-and-byte-integrity
---

# Metroidvania

> **Draft research candidate, not released guidance.** Version 0.1.0; candidate revision `initial-1`; independent review not performed. Definitions and proposed adaptations below are bounded inferences or hypotheses, not an approved studio design. No game build, gameplay recording, prototype or player test was run in this batch.

The supplied G02 dispatch authorizes this batch and supersedes old starter-phase sequencing restrictions only. Its final parent reconciliation records completed, independently reviewed first-wave drafts, but those reviewed bytes were not retrieved here. No unseen F01/P01 wording or numerical settings are inherited. No reviewed shared guidance is transferred in this entry. [Workflow basis: supplied `Pasted text.txt`, Assigned outputs; Genre-specific questions; Parent review reconciliation.]

## Definition and contested boundaries

**Working definition:** a metroidvania organizes a substantial part of progression around exploring a persistent connected world whose previously encountered spaces can be reinterpreted through acquired capabilities. This definition is a research instrument, not a universal consensus, market rule or approved studio taxonomy. It emphasizes relationships among knowledge, capability and topology rather than a required camera, combat model, art style or map size. [C-01]

A game does not meet this working boundary merely because it has upgrades or asks the player to retrace a corridor. Ask whether new capabilities change the significance or reachability of known space and whether choosing, remembering or recovering routes matters. A statistical damage upgrade, a chapter-select menu and a story key can each support progression without demonstrating that relationship. Conversely, a route can change through knowledge or execution skill without a new inventory object; identify that mechanism instead of calling every barrier an ability gate. [C-01; C-04]

[Platformer](platformer.md), `GDR-CAND-20261010-G02-GEN-01`, concerns traversal as consequential activity; [precision platformer](precision-platformer.md), `GDR-CAND-20261010-G02-GEN-02`, makes repeatable execution a foreground priority. They can overlap with this genre without deciding its exploration contract. The pinball/exploration combination described for Yoku's Island Express is a useful boundary probe: analyze which capabilities change which routes rather than requiring a conventional jump. Its inclusion here is a conditional interpretation, not membership verified by an authoritative genre definition. [C-01; C-07; GDR-SRC-20261010-G02-012; GDR-SRC-20261010-G02-015]

## Custom research instructions

Start with the **world state a player can understand and act on**, not a count of rooms. For each important barrier, investigate its visible evidence, required capability or knowledge, access routes, return cost, recovery information and effect on future choices. Separate physical reachability from the player's ability to recognize an actionable lead. A formally solvable map can still leave a player unable to recover a next step. This distinction is analytical reasoning, not a measured finding in this batch. [C-04]

Maintain distinct questions for hard ability locks, knowledge locks, skill gates, resource requirements, narrative conditions and one-way transitions. Inspect where these interact: a route may be geographically open but practically blocked by combat, inaccessible controls or depleted resources. Do not describe the world as freely explorable solely because no door key is required. [C-04; C-06]

Seek primary creator accounts of topology revisions, progression dependencies and navigation support; original navigation studies with relevant tasks; build-identified routes demonstrating both recovery and failure; and accessibility/input sources. The present batch retrieved useful creator/publisher accounts, but **no original metroidvania-specific navigation experiment or actual build trace**. Research into that empirical gap remains needed; absence from this source set is not proof that such studies do not exist. [C-11]

Challenge misleading comparisons: map area as discovery quality; lock count as depth; backtracking duration as meaningful reinterpretation; optional combat as proof that challenge is absent; a minimap toggle as complete cognitive access; and a celebrated game's structure as a causal formula. Compare short and long worlds, guided and uncertain navigation, conventional and hybrid traversal, required and optional combat, and experienced versus returning/novice players. No demographic prevalence claims follow from the selected cases. [C-04; C-06; C-11]

## Player promises and varied audiences

Candidate promises include becoming more capable, recognizing an old place differently, choosing among plausible routes and recovering a plan after uncertainty. Some projects additionally promise danger, execution mastery, solitude or dense discovery; those are separate commitments, not automatic consequences of this genre name. Players can value an unknown destination while needing reliable information about a route already visited. These are proposed design distinctions to test, not universal expectations. [C-04; C-08]

The inspected accounts support a genuine **difference of emphasis**, not a controlled contradiction. Nintendo's prerelease Metroid Dread report discusses exploration tools and abilities. Team Cherry's prerelease Crossroads tour emphasizes winding routes, initial uncertainty and shortcuts. The accounts come from different projects and promotional contexts; they do not tell us which amount of help best serves any particular player. [C-02; C-03; GDR-SRC-20261010-G02-009; GDR-SRC-20261010-G02-010]

## Characteristic loops, gates and structures

A useful proposed structure is **encounter a lead or barrier → choose another viable activity → gain capability or understanding → identify a changed opportunity → return, cross or reconnect**. Not every upgrade needs this sequence, and the player need not encounter every barrier before earning its solution. Immediate use, forward-only progression and ungated discovery are valid alternatives. The repeatable recipe is isolated in [Recoverable ability-gate loop](../patterns/recoverable-ability-gate-loop.md), rather than imposed as a universal genre cycle. [C-04; C-08]

| Gate or obstacle type | What changes access | Characteristic research error | Useful validation question |
|---|---|---|---|
| Capability | A newly available action/state interaction | Treating an inventory label as proof the player understands its spatial use | Can the player identify and execute a new use without memorizing a single demonstration? |
| Knowledge | Understanding a rule, location or relation | Requiring a literal upgrade even though information is the actual barrier | Is the needed inference available through more than one accessible evidence route? |
| Skill | Reliable execution or tactical performance | Misreporting failure as navigation confusion | Does assistance change execution while preserving the route decision? |
| Resource | Sufficient consumable or recoverable stock | An apparently optional expenditure creates an essential dead end | Can the player replenish or retreat without already crossing the blocked route? |
| Narrative/state | A world flag or event | A visual ability cue implies the wrong unlocking mechanism | Is the actual condition intelligible and recoverable after absence? |
| One-way transition | Entry without an immediate reverse edge | Assessing only the outward path | Is there a reachable exit, recovery or deliberately communicated commitment in every supported state? |

This table is a proposed analytical taxonomy. It does not assert that all of these are necessary genre elements. Multiple conditions should be recorded separately, including when one can bypass another. [C-04]

At longer horizons, backtracking earns its place when the return offers a changed decision, perspective, capability use or route connection that matters to the intended experience. “No new decision” is not automatically bad—familiar transit may offer rest or orientation—but then name that purpose instead of counting it as discovery. Avoid assuming that a shortcut is always desirable; it may bypass a chosen traversal rhythm or erase useful landmark exposure. These are conditional hypotheses needing local evaluation. [C-05]

## Evidence-to-application bridges and practical choices

### Keep uncertainty bounded by recoverability, not by a mandatory marker

The strongest proposal here is **recoverable exploration**: preserve more than one way to regain an actionable understanding where failure to remember is not the intended barrier. Candidate supports include distinctive landmarks, personal annotations, objective history, a route recap, optional hints or explicit map information. These are alternatives, not a requirement to reveal the next destination. [C-08]

The evidence bridge is limited. GDR-SRC-20261010-G02-009 describes map functions and revisiting spaces with abilities; GDR-SRC-20261010-G02-010 describes a different emphasis on uncertainty and shortcuts. Together they motivate distinguishing *unknown content* from *recovering known information*. They do not validate a particular hint ladder or prove that recoverability increases enjoyment. That causal proposal remains low-confidence until compared with less assisted exploration in the intended audience. [C-02; C-03; C-08]

### Audit physical reachability and informational recovery separately

Create a conceptual graph of locations and conditional connections. Record the capabilities, consumables, flags and access options needed for each essential edge. For proposed one-way entries, check the available exits from each supported arrival state. Then perform a separate human-facing information review: which clue tells the player what changed, which visited obstacle could match it, and what help can restore that relation after an interruption? Neither review substitutes for the other. No graph checker or player test was executed here. [C-04; C-08]

A progression graph may omit optional areas yet still be mechanically sound; a fully connected graph may still demand an inaccessible simultaneous input. Make a route's practical requirements explicit. Preserve optional sequence breaks when they are intended, but distinguish a satisfying alternative order from a state that traps the player or invalidates subsequent instructions. Proposed graph audits should cover assist states and resource depletion, not merely default acquisition order. [C-04; C-09]

### Decide what a return trip contributes

Compare three alternatives before adding a distant gate: reveal and cross immediately; revisit a known barrier after a meaningful interval; or open a forward connection without requiring a return. A long return can support changed interpretation, resource tension or geography learning, but it can also become repeated transit without a decision. Observe what the player notices and chooses; distance alone cannot distinguish the two. [C-05]

A shortcut should have an identifiable destination and persistence rule. A hidden connector that only looks familiar may worsen orientation; a connector that bypasses an essential teaching opportunity may leave later routes unexplained. Conversely, forcing the original route after its purpose is exhausted can burden returning players. These are failure hypotheses, not measured claims about a named game. [C-05; C-08]

### Separate exploration access from combat tuning

Tom Happ's prerelease Axiom Verge 2 account presents separate outgoing/incoming damage adjustments and optional-boss intent; the later interview highlights more player agency in upgrade order and frames bypassing **most** bosses. This supports investigating combat as a potentially separable exploration barrier. It does **not** establish that every boss is optional in every shipped version. [C-06; GDR-SRC-20261010-G02-013; GDR-SRC-20261010-G02-014]

The design question is not “remove combat or keep challenge.” Ask which discoveries, traversal tests and world-state changes actually depend on combat completion. Compare an avoidable encounter, a combat assist, an alternative route and an essential fight as different structures. Each changes costs and pacing. A marketed exploration promise can conflict with an unannounced mandatory boss bottleneck; a combat-led hybrid may deliberately retain one. Select and communicate the local priority rather than declaring a winning genre rule. [C-06; C-09]

## Applying shared topics

**Reviewed shared guidance transferred: none.** These are missing dependency requests, not invented references or canonical content. Temporary G02 sibling/pattern links are the only applied library entries available here.

| Shared dependency | Metroidvania-specific adaptation | Missing state |
|---|---|---|
| F03 progression/rewards; Foundations and Systems | Ability acquisition changes reachable/meaningful space; distinguish capability from numerical growth | No inspected reviewed topic bytes or candidate-to-canonical link |
| F04 movement/traversal; Foundations and Systems | Ability combinations, return-route feasibility, sequence breaks and assist-dependent edges | Missing shared bytes/IDs |
| W03 spatial/world exploration; Worlds and Characters | Topology, landmarks, backtracking purpose, cognitive versus physical recovery | Missing shared bytes/IDs; primary sources do not replace owner review |
| P02/P03 input/camera; Presentation and Interaction | Route executability, simultaneous input, camera evidence and re-entry orientation | Missing reviewed bytes/links; XAG used as bounded external guidance |
| F01/P01 reviewed first-wave context | Learning a capability versus recalling a location; scoped accessibility numbers | Supplied review receipt only; corrected text unavailable |
| Combat/challenge and interface guidance where the project requires it | Optional/essential fights, maps, hint controls and persistence | Applicable topic links remain pending; no unsupplied IDs allocated |

The audio pilot is not a prerequisite. No inference is made that this genre must generate fear or ambient tension.

## Pattern selection, adaptations and hybrid conflicts

[Recoverable ability-gate loop](../patterns/recoverable-ability-gate-loop.md), `GDR-CAND-20261010-G02-PAT-02`, is the selected core candidate when remembering and reinterpreting a prior place is an intended decision. Adapt its recovery information to the desired uncertainty: a personal marker may be enough in one context, while an optional recap may be needed after a long interruption. Stop using it where no meaningful return relation exists or where the player cannot retreat from a supported acquisition state. [C-08]

[Bounded action grace](../patterns/bounded-action-grace.md), `GDR-CAND-20261010-G02-PAT-01`, is relevant only when route execution—not route understanding—is blocked by a command boundary. It cannot solve a forgotten gate. In a precision hybrid, a wider window can change an intended execution test; in an exploration-led hybrid, retaining a narrow motor barrier can prevent the intended discovery. Both costs must remain visible. [C-09]

Pinball, combat-led, knowledge-led and conventional jumping hybrids should be compared by their actual abilities and connection rules. Team17's Yoku descriptions supply a documented unusual movement/exploration combination, but no directly inspected map or executable route. Its useful lesson here is to investigate the combination, not to assert that every shared spatial principle has already been demonstrated in it. [C-07; GDR-SRC-20261010-G02-012; GDR-SRC-20261010-G02-015]

## Representative cases and source-status limits

| Case | Evidence route, platform/build and locator | Bounded use and negative case |
|---|---|---|
| Metroid Dread | GDR-SRC-20261010-G02-009, 2021-07-15 prerelease Switch report, §§4–5; build unspecified | Described mapping/ability exploration; cannot stand in for shipped navigation measurements |
| Hollow Knight, Forgotten Crossroads | GDR-SRC-20261010-G02-010 prerelease creator tour; year/platform/build not established by inspected text | Contrasting uncertainty/shortcut emphasis; does not prove that being lost is enjoyable or universally necessary |
| Axiom Verge 2 | GDR-SRC-20261010-G02-013 PlayStation developer article, 2021-06-10; GDR-SRC-20261010-G02-014 written interview highlights, 2021-10-28; no build run | Combat/progression intent; preserve the all-versus-most optional-boss wording difference |
| Yoku's Island Express | GDR-SRC-20261010-G02-012 publisher page; GDR-SRC-20261010-G02-015 publisher-supplied Nintendo Switch description, listed release 2018-05-29 | Pinball/ability/exploration hybrid; no gameplay or detailed topology verified |

These are purposively selected, commercially visible accounts, not a representative census. Nintendo's later Report 11 remained inaccessible and is **lead-only** in the packet; no mission-log or post-release claim is supported by its search snippet. No observation timestamp is invented for any case. [C-11]

### Illustrative worked example: reopening the canal circuit

**Illustrative, not a shipped map, prototype or actual audit.** A fictional hub leads to a canal overlook and a workshop. At the overlook the player can see a grippable overhead rail but cannot traverse it. The workshop grants a rail-grip action and contains a safe, forward demonstration of that action. A separate walking route leads back to the hub, so acquiring the ability does not require immediately passing a difficult rail sequence. [C-08]

The proposed return loop is **hub → overlook barrier → workshop ability → hub → overlook crossing → observatory → hub shortcut**. The initial encounter is optional: a player who finds the workshop first can still understand the rail. Give the rail a consistent form and action response; use localized names or icons that preserve the same relation. An optional personal marker records the player's own lead. A requested recap can identify “a previously seen rail” without naming the entire route. No particular map density or number of hints is prescribed. [C-08]

Separate mechanical and informational risks. Mechanically, entering the observatory must not consume the only resource needed for its only exit; review every supported route/assist state. Informationally, the player may know the new action but forget the overlook. Compare a landmark cue, a marker and a stronger optional hint rather than concluding that the map needs to be smaller. The proposed test asks which option restores a chosen plan without prematurely solving the destination decision. [C-04; C-08]

The shortcut earns its place only if it serves the declared return purpose. A connector that reveals a recognizable hub landmark can support orientation; an anonymous tunnel whose exit appears unrelated may not. If the return offers no new decision and the designer does not intend restorative transit, compare placing the observatory along the forward workshop route instead. That counterexample avoids adding backtracking merely to satisfy a label. [C-05; C-08]

**Additional counterexample:** a knowledge puzzle may intentionally conceal which earlier object is relevant. A mandatory map highlight would answer the puzzle rather than support memory. Distinguish an optional request for a spoiler from default navigation aid, and preserve alternative access to the puzzle's actual evidence. Recoverability does not mean automatic solution disclosure. [C-09]

## Accessibility, ethics, localization and production implications

A route can demand sustained input, timing, visual recognition, memory and combat simultaneously. Apply XAG input/difficulty guidance to each relevant demand without claiming that a combat slider makes exploration accessible. Consider optional interruption recaps, marker editing, readable landmark descriptions, a way to revisit capability explanations and routes feasible with supported input options. These are proposed adaptations; this source set contains no metroidvania-specific evaluation of them with disabled participants. [C-10; GDR-SRC-20261010-G02-005; GDR-SRC-20261010-G02-006; GDR-SRC-20261010-G02-007]

Do not assume color-coded locks or region names alone preserve meaning across sensory conditions and languages. Proposed QA should test the relation among a barrier's form, action verb, inventory description and map label under text expansion and changed controls. If a hint uses “left of the tower,” verify the orientation available in the current view; a location name or visible landmark relation may be more stable. These are reasoning-based checks, not universal localization rules. [C-10]

World-state production costs arise from combinations: abilities earned in different orders, optional shortcuts, flags after bypassed encounters, consumable depletion, death, save/load and assistance changes. A graph sketch can reveal some impossible transitions, but it cannot prove cognitive clarity or physical accessibility. Maintain source/version records as maps change, and distinguish approved sequence breaking from an unreviewed soft lock. No runtime architecture, QA hours or performance costs are specified here. [C-04; C-10]

Ethically, offer help without treating confusion as a personal failure, and distinguish a chosen blind-exploration mode from an inaccessible information design. Avoid using unrecoverable confusion to extend sessions or sell relief. That is a proposed product-review stance, not an approved studio monetization or accessibility policy. [C-10]

## Research questions and proposed validation

**All proposed; none performed.** Use participants with varied familiarity with capability-led exploration, relevant input/access needs and recent versus interrupted play. Do not equate prior completion of a famous game with knowledge of this world's rules. Allow the participant to request hints and record requests without penalizing them. Set sample, practical significance and stopping criteria for the local study; this draft supplies no numerical defaults. [C-11]

| Question | Comparison and procedure | Measures and confounds | Result that would reject or narrow the proposal |
|---|---|---|---|
| Does a capability trigger useful reinterpretation? | Same capability and task; compare prior barrier exposure with an equally legible newly encountered barrier | Recognized uses, chosen destinations, explanation; prior exposure and route cost can confound | Prior exposure adds memory burden without an intended discovery benefit |
| Does recovery support preserve desired uncertainty? | Landmark-only, player marker and optional recap/hint conditions; record chosen help | Time without an actionable plan, mistaken gate revisits, agency and unwanted spoilers; hints alter information | Assistance solves the intended inference prematurely, or offers no recovery to those who need it |
| Is backtracking meaningful or only costly? | Matched return with changed affordance/connection versus repeated transit; preserve other rewards | New decisions noticed, remembered relation, boredom/fatigue and navigation errors separately | Return length increases without the intended reinterpretation, orientation or restorative value |
| Does a combat barrier obstruct the exploration promise? | Same information and reward; alternative path, combat assistance or required encounter | Discovery access, chosen engagement, fatigue and sense of purpose; rewards must not secretly coerce combat | Nominally optional combat remains practically mandatory or an alternative removes the project's declared central challenge |
| Is every supported arrival recoverable? | Proposed state/route review followed by local tests across ability, resource, input and save states | Reachable exit and ability to identify an actionable lead; mechanical validity is separate from comprehension | Any essential supported state traps the player or recovery help fails to restore an actionable choice |

For the first comparison, recognition of a familiar location is **not** by itself transfer of the new ability rule. Include an unseen barrier using the same relation and account for its difficulty. Re-entry testing after a break addresses recovery of context, not automatically learning or retention of an execution skill. [C-11]

## Claim ledger

| ID | Material claim and class | Support and precise locator | Confidence and unresolved boundary |
|---|---|---|---|
| C-01 | Capability-led reinterpretation in a connected world is this draft's working boundary; upgrades/backtracking alone are insufficient. `inference` | GDR-SRC-20261010-G02-009 §§4–5; GDR-SRC-20261010-G02-014 upgrade-order discussion; GDR-SRC-20261010-G02-015 ability description; supplied taxonomy boundary instructions | Moderate research utility; not formal or universally accepted classification |
| C-02 | Nintendo's prerelease report describes mapping aids and ability-led revisits. `practitioner-heuristic` | GDR-SRC-20261010-G02-009 §§4–5, developer-attributed transmissions and named map features | High for reported intent/features; low for inferred player benefit; no post-release observation |
| C-03 | The Crossroads creator tour offers uncertainty and shortcuts as part of exploration. `practitioner-heuristic` | GDR-SRC-20261010-G02-010 opening/region paragraphs | High for the attributed offer; no measured benefit. G02-CON-03 is conditional emphasis, not direct experimental conflict |
| C-04 | Physical reachability, gate mechanism and recoverable player knowledge must be analysed separately. `inference` | Explicit state/graph reasoning; C-02/03 give contrasting design context | Moderate logical bridge; no graph audit or participant test here |
| C-05 | Return travel should be assessed by its intended changed decision, orientation or rest—not by distance/lock count alone. `hypothesis` | GDR-SRC-20261010-G02-009/GDR-SRC-20261010-G02-010 motivate the question; proposed alternatives are new synthesis | Low for causal benefit; deliberate familiar transit is a counterexample |
| C-06 | Axiom Verge 2 accounts motivate separating combat access from exploration, while all/most boss wording cannot prove a shipped universal. `practitioner-heuristic` | GDR-SRC-20261010-G02-013 difficulty paragraphs; GDR-SRC-20261010-G02-014 upgrade-order and most-bosses exchange | High for attributable wording, moderate for interpretation; G02-CON-04 unresolved build scope |
| C-07 | Yoku's publisher descriptions combine pinball traversal, exploration and abilities. `observed-example` | GDR-SRC-20261010-G02-012 About; GDR-SRC-20261010-G02-015 Key Features | High for inspected product text; genre membership/topology remain inference; same underlying case |
| C-08 | Recoverable ability-gate loops may support reinterpreting known places without mandatory solution disclosure. `hypothesis` | C-02–05; PAT-02 candidate; canal example is synthetic | Low causal confidence; no metroidvania navigation experiment or route observation; G02-CON-03 |
| C-09 | Assistance and hybrid priorities can preserve one promise while weakening another; no genre mechanically takes precedence. `inference` | GDR-SRC-20261010-G02-013/GDR-SRC-20261010-G02-014 combat tradeoff; GEN-01/02 and local counterexamples | Moderate conditional reasoning; local priority must be explicitly chosen |
| C-10 | Access, localization and production review must cover route demands and state combinations rather than assume one map/difficulty setting suffices. `inference` | GDR-SRC-20261010-G02-005 Introduction; GDR-SRC-20261010-G02-006 input demands; GDR-SRC-20261010-G02-007 mechanic-specific options; C-04 state logic | Moderate rationale; no population coverage or implementation guarantee. G02-CON-05 |
| C-11 | The proposed tests need to distinguish navigation recovery, rule transfer, execution and agency. `hypothesis` | Local test proposals; supplied evidence/brief/F01 correction constraints | Low for protocol sensitivity until piloted; no actual results or sample guarantee |

## Coverage checkpoint, review and history

| Researched subtopic | Inspected coverage versus gap | Next discriminating question |
|---|---|---|
| Ability gating and topology | Multiple creator/publisher contexts; no game-state trace or formal map audit | Which supported states make an apparently optional gate essential or irreversible? |
| Backtracking, landmarks and optional routes | Conditional synthesis and creator route accounts; no direct navigation experiment | Does the return provide the intended reinterpretation or merely more travel? |
| Map assistance and interruption recovery | Prerelease official mapping description; later Report 11 inaccessible | Which aid restores a plan without disclosing the desired discovery? |
| Combat/exploration interaction | Two related Axiom Verge 2 accounts; build-level optionality unverified | Which exact progression rewards remain accessible when combat is bypassed? |
| Hybrid traversal | Publisher-described Yoku combination, no reproducible played route | Which movement capabilities actually alter prior-route meaning? |
| Access and localization | Primary general guidance; no genre-specific access evaluation | Which information/input demand remains essential after selected assistance? |

**Author self-review:** the strongest recommendation—make exploration recoverable—risks becoming a disguised demand for objective markers, or treating all disorientation as a defect. This draft narrows it to the local experience contract, separates mechanical escape from informational help, retains deliberate uncertainty, and proposes optional rather than automatic disclosure. It still lacks direct player evidence about the best recovery mechanism. Independent review has not occurred.

Version `0.1.0`, candidate revision `initial-1`; predecessor and supersession null. Byte identity is in the [review packet](../reviews/full-run-20261010-g02-review-packet.md#candidate-inventory-and-byte-integrity). Gate C review pending; Gate D host tests and Gate E release not passed. Full genre coverage, sequence-break robustness and player efficacy are not certified by this draft's existence.

## References

### GDR-SRC-20261010-G02-005

**Microsoft Xbox accessibility team. [Xbox Accessibility Guidelines V3.2](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines).** Microsoft Learn. Publication/update: V3.2 published 2023-06-08; inspected page last updated 2026-08-14.

Edition/build: V3.2 hub as served 2026-10-10; page date is distinct from guideline-set version. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary non-normative platform guidance.

**Inspected locator:** Introduction; Overview of XAG components → Example content; version heading and last-updated footer.

**Claims supported here:** C-10. **Limits:** The introduction explicitly excludes compliance/legal-checklist status; no formal-standard claim is made. **Independence:** Common guidance family with GDR-SRC-20261010-G02-006 and GDR-SRC-20261010-G02-007; not independent empirical studies. **Rights:** Microsoft documentation; paraphrase only, example images not redistributed.

### GDR-SRC-20261010-G02-006

**Microsoft Xbox accessibility team. [Xbox Accessibility Guideline 107: Input](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107).** Microsoft Learn. Publication/update: 2026-03-04 last updated on opened page.

Edition/build: XAG 107 page within V3.2 set; live page snapshot checked 2026-10-10. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary non-normative accessibility/input guidance.

**Inspected locator:** Goal; Overview; Background and foundational information → Speed, Complexity, Duration and proposed alternatives; Implementation guidelines → remapping and updated prompts; mobile-input section reviewed for scope only.

**Claims supported here:** C-10. **Limits:** No game-independent timing, sensitivity, target-size or compliance requirement is inferred; core article text was accessible despite an authorization banner. **Independence:** Same XAG guidance family as GDR-SRC-20261010-G02-005/GDR-SRC-20261010-G02-007; cited third-party examples are not additional observations. **Rights:** Microsoft documentation; paraphrase only; embedded example media not inspected as gameplay.

### GDR-SRC-20261010-G02-007

**Microsoft Xbox accessibility team. [Xbox Accessibility Guideline 108: Game difficulty options](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/108).** Microsoft Learn. Publication/update: 2026-03-04 last updated on opened page; an earlier search result showed another date, not adopted.

Edition/build: XAG 108 page within V3.2 set, checked 2026-10-10. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary non-normative accessibility guidance.

**Inspected locator:** Goal; Overview; Scoping questions and individual game-mechanic adjustment guidance.

**Claims supported here:** C-10. **Limits:** Options are design guidance, not a guarantee of access for every player or a formal standard; text accessible despite authorization banner. **Independence:** Same guidance family as GDR-SRC-20261010-G02-005/GDR-SRC-20261010-G02-006. **Rights:** Microsoft documentation; paraphrase only.

### GDR-SRC-20261010-G02-009

**Nintendo; attributed Metroid Dread development-team transmissions. [Metroid Dread Report Vol. 3: Seven points that define the 2D saga](https://www.nintendo.com/en-gb/News/2021/July/Metroid-Dread-Report-Vol-3-Seven-points-that-define-the-2D-saga-2007780.html).** Nintendo UK. Publication/update: 2021-07-15.

Edition/build: English pre-release report for Nintendo Switch; executable build unspecified. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary publisher explanation with creator-attributed intent.

**Inspected locator:** §4 Exploration → Icon Highlight, Marker, Zoom, Hidden item hints and development-team transmission; §5 Arsenal and abilities and following transmission.

**Claims supported here:** C-01, C-02; C-04/05/08 inference context. **Limits:** Describes planned affordances and intent, not observed post-release navigation success, exact topology or universal genre definition. **Independence:** One Nintendo/Metroid account; later reports are related, not independent confirmation. **Rights:** Nintendo copyright; paraphrase only, maps/images not redistributed.

### GDR-SRC-20261010-G02-010

**Team Cherry; displayed byline Team Cherry Press. [The Forgotten Crossroads — A Hollow Knight Tour](https://www.teamcherry.com.au/blog/the-forgotten-crossroads-a-hollow-knight-tour).** Team Cherry. Publication/update: unknown year; rendered page shows October 11 only and describes an upcoming game.

Edition/build: Pre-release region tour, platform/build unspecified. Accessed **2026-10-10**; access: `full`; type: Primary creator/publisher region overview.

**Inspected locator:** Opening introduction; paragraphs beginning The Crossroads are made up and Most travellers may shun the Crossroads.

**Claims supported here:** C-03; C-04/05/08 inference context. **Limits:** Initial disorientation, skill growth and route-finding are creator claims; no observation of shipped Hollow Knight or measured benefit. **Independence:** Distinct production context from Nintendo and Thomas Happ; promotional account rather than independent experiment. **Rights:** Team Cherry copyright; paraphrase only; screenshots not redistributed or treated as played scenes.

### GDR-SRC-20261010-G02-012

**Team17. [Yoku’s Island Express](https://www.team17.com/games/yokus-island-express).** Team17 official product page. Publication/update: unknown publication/update date.

Edition/build: Multi-platform publisher page; no executable build. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary publisher description.

**Inspected locator:** About the game, especially final two paragraphs; linked Nintendo product route.

**Claims supported here:** C-07. **Limits:** Pinball and exploration description only; does not itself use the metroidvania label or verify ability topology. **Independence:** Same publisher/game description family as GDR-SRC-20261010-G02-015; count once as an underlying case. **Rights:** Publisher copyright; paraphrase only.

### GDR-SRC-20261010-G02-013

**Tom Happ, credited Sole Developer, Axiom Verge. [Axiom Verge 2 lands on Earth this summer, coming to PlayStation](https://blog.playstation.com/?p=350133).** PlayStation.Blog. Publication/update: 2021-06-10.

Edition/build: Pre-release developer article; PS4/PS5 plans discussed, no playable build verified. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary creator account.

**Inspected locator:** Paragraphs beginning Although I try to put on my blinders and I addressed the difficulty issue in two ways.

**Claims supported here:** C-06, C-09. **Limits:** Optional-boss statement is a pre-release intention. Do not translate it into all bosses are optional in every released build. **Independence:** Same creator/production as GDR-SRC-20261010-G02-014; later interview is not an independent empirical replication. **Rights:** Author/platform-publisher copyright; paraphrase only.

### GDR-SRC-20261010-G02-014

**Jared Petty interviewing Tom Happ; rendered byline spells the surname Pettty. [Limited Run Games Blog: That Axiom Urge](https://limitedrungames.com/en-ca/blogs/news/limited-run-games-blog-that-axiom-urge).** Limited Run Games. Publication/update: 2021-10-28.

Edition/build: Written highlights of Runtime interview; podcast audio not played; build not specified. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary interview excerpts; interviewer evaluation separately identified.

**Inspected locator:** Some highlights: How Prey, Zelda, and Final Fantasy helped define Axiom Verge 2; quoted upgrade-order discussion; question about walking past most bosses and Happ’s response.

**Claims supported here:** C-01, C-06, C-09. **Limits:** Use attributed developer statements, not the interviewer’s praise as efficacy evidence; most-bosses framing is narrower than GDR-SRC-20261010-G02-013. **Independence:** Related to GDR-SRC-20261010-G02-013 through the same creator; product-selling context. Podcast and written highlights are one interview. **Rights:** Interview/article copyright; short paraphrase only.

### GDR-SRC-20261010-G02-015

**Team17 (software description explicitly attributed to publisher). [Yoku’s Island Express for Nintendo Switch](https://www.nintendo.com/us/store/products/yokus-island-express-switch/).** Nintendo US storefront. Publication/update: Description publication/update unknown; listed game release 2018-05-29.

Edition/build: Nintendo Switch publisher-supplied description, not an inspected executable version. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary publisher-supplied description artifact.

**Inspected locator:** Software description → Key Features: Open-world pinball adventure and Unlock the amazing new abilities; publisher attribution; release-date field.

**Claims supported here:** C-01, C-07. **Limits:** Supports described movement/ability combination; metroidvania membership remains a declared working interpretation, not proven by a shop tag. **Independence:** Derivative distribution of the GDR-SRC-20261010-G02-012 game/publisher account; not an independent developer case. **Rights:** Publisher/Nintendo copyright; paraphrase only.

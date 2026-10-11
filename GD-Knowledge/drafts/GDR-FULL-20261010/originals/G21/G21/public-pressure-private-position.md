---
id: GDR-CAND-20261010-G21-PAT-01
kind: pattern
title: Public pressure, private position
version: 0.1.0
status: draft
owner_project: BH-GDR-Genres
run_id: GDR-FULL-20261010
batch_id: G21
candidate_revision: initial-authoring-1
attempt_id: G21-authoring-01
updated: '2026-10-10'
evidence_checked: '2026-10-10'
coverage_status: coverage-open
independent_review: not-performed
aliases:
- public deadline without enemy disclosure
- forecast closing opportunities
tags:
- public-information
- pressure
- route-choice
- hidden-information
- untested-pattern
related_topics:
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-P02-TOP-03
related_patterns:
- GDR-CAND-20261010-G21-PAT-02
- GDR-CAND-20261010-P02-PAT-02
related_genres:
- GDR-CAND-20261010-G21-GEN-01
- GDR-CAND-20261010-G21-GEN-02
- GDR-CAND-20261010-G21-GEN-03
source_ids:
- GDR-SRC-20261010-G21-010
- GDR-SRC-20261010-G21-012
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
hash_record: ../reviews/full-run-20261010-g21-review-packet.md
---

# Public pressure, private position

**Untested reusable pattern candidate.** This recipe separates authoring a public closing opportunity from revealing private opponent state. It is not a claim that deadlines, shrinking space or more information inherently improve play. Proposed canonical ownership is Foundations for decision rules with Worlds for spatial composition and Presentation for delivery; Coordination has not accepted that allocation.

## Purpose

Help a player make a consequential response to a known change in opportunity while retaining uncertainty that belongs to the challenge. The target problem is not simply “the warning was missed.” A warning can be fully perceived while no meaningful response is reachable, or it can overexplain an opponent’s hidden activity. This pattern therefore reviews the **constraint, options and information contract together**. [C-01]

## Context and prerequisites

Use when an event deliberately has public timing or a public phase transition, some opportunities close, and choosing a response is part of the intended experience. The setting may be a spatial contest, a team objective or a persistent-world event. At least one player-relevant alternative to blindly following an instruction must exist: depart earlier, take another route, surrender a reward, accept a disclosed risk, or choose a different objective. [C-02]

Required inputs are the intended decision, public facts, legitimately hidden facts, allowed capabilities, relevant geometry or dependency graph, and a way to represent changes. This is an authoring recipe, not permission to implement or operate a timer. A public deadline must be real enough to explain; an unknowable random event should not be presented with spurious precision. [C-02; C-04]

**Exit immediately** when discovering whether the event exists is the intended challenge, when every nominal response is impossible, when a forecast requires unearned private information, or when the operator cannot keep the displayed commitment consistent with the rules. Use investigation, an optional challenge, a static objective or no pressure instead. [C-02]

## Mechanism and evidence, link by link

| Causal link | What is supported | What remains unvalidated |
|---|---|---|
| Public phase/rule information can be represented separately from opponent location. | F02’s inspected information-contract distinction and P02’s fact-preserving cue recipe support the conceptual separation. | That a particular representation is noticed, understood or judged fair. [C-01] |
| A closing opportunity changes the consequences of waiting. | Logical consequence of the proposed rule; KRAFTON describes this use of spatial pressure in its 2026 letter. | Whether the change creates interesting decisions rather than forced movement. [C-03] |
| Reachable alternatives plus comprehensible constraints may support deliberate choice. | Reasoned connection between the first two links. | Comparative player benefit; no G21 player test or independent field study validates this link. [C-02; C-05] |
| Alternative communication channels may preserve the necessary public facts. | Reviewed P01/P02 guidance, with uncertainty preserved. | Equivalent workload, strategy, emotion or competitive effect across users. [C-04] |
| Calibrating constraints and presentation together may preserve agency. | Pattern-level hypothesis, challenged by KRAFTON’s distinct mode rationales. | No universal timing, map-density, fairness or enjoyment result. [C-05] |

KRAFTON’s developer account is a primary account of rationale, not a controlled demonstration. Riot’s Smart Ping documentation supplies a separate example of conveying objective intention; it does not validate this combined recipe. Two production examples establish possible components, not causal success of their combination. [C-03; C-06]

## Recipe

1. **Name the decision and the intended loss.** Write what may become unavailable and why that changes the player’s options. Distinguish losing access, taking damage, losing score and losing eligibility. Stop if “make the player hurry” is the only specified purpose. [C-02]
2. **Create a public/private fact sheet.** Record the rule, event state, deadline or transition condition, authorized geography, known hazards and source/age of reports. Mark opponent location, intent and unobserved hazards separately. Do not let a UI convenience silently promote an estimate into fact. [C-01; C-04]
3. **Enumerate feasible responses before adding signals.** For each allowed capability/context, walk through departure, diversion, sacrifice and risk acceptance. Account for competing objectives, traversal dependencies and assistance. A route that exists on a map but cannot be executed by an allowed player capability is not a usable option. [C-02]
4. **Choose adjustable pressure variables independently.** Alter warning lead, opportunity duration, rate of closure, spatial placement, route availability or consequence severity one at a time where possible. Define each as a local test variable, not a copied genre default. Avoid increasing every form of pressure together, which conceals the cause of failure. [C-03; C-05]
5. **Present facts, not a mandatory optimal answer.** Provide the public transition and a way to inspect legitimate context. A map edge, text status, sound or other cue may be appropriate, but the message must retain the same uncertainty and authority. Do not expose an enemy position merely to give a “safe route.” Preserve accessible help and player-chosen accommodations. [C-04]
6. **Handle revision and cancellation explicitly.** In the paper specification, state which conditions can change a forecast and how the player recognizes a superseded forecast. Avoid a continuing countdown to an opportunity already canceled. Do not promise exact time when the actual event depends on an unknown condition. [C-04]
7. **Compare pressure with a simpler alternative.** Evaluate a static window, an optional race, another route or no deadline. Reject the added pressure when the desired choice is absent, false certainty increases, or it mainly adds inaccessible execution demands. Stop before implementation; playtesting and engine changes require separate approval. [C-05; C-07]

## Adjustable variables and local decisions

| Variable | Local question | Warning sign and exit |
|---|---|---|
| Forecast granularity | Exact time, phase, range or conditional event? | Apparent precision exceeds rule knowledge; use a qualified state or omit the forecast. |
| Warning versus action opportunity | Does preparation consume the entire usable response interval? | The message is understood but all allowed responses fail; change the opportunity, not only the warning. |
| Route/objective alternatives | What can be sacrificed or chosen instead? | Everyone follows one forced route with no valued tradeoff; choose a simpler structure or revise geometry. |
| Consequence and closure rate | Is the desired stake resource loss, exposure or finality? | Several consequences stack into an uninterpretable loss; isolate them before increasing severity. |
| Knowledge expiry | Does a report remain true, or merely record an observation? | Old enemy reports become continuous tracking; restore uncertainty. |
| Channel and inspection cost | Can the public constraint be checked during the actual task? | Cue overload or mandatory use of an inaccessible channel; redesign presentation or lower simultaneous demand. |

All variables are proposed design settings. No numerical range, optimal ratio or universal threshold is established. [C-05]

## Worked examples

### Illustrative spatial example: a closing crossing

A fictional team can cross a short exposed bridge, detour through shelter or give up a cache and depart early. A public flood phase will close the bridge. The fact sheet includes closure state and known terrain; a teammate’s old sighting remains an old sighting. [C-02; C-04]

Apply the recipe to the least mobile permitted capability as well as the fastest. The sheltered detour may be traversable but too long after a late departure. That makes sacrificing the cache a relevant option only if it is available early enough and the player can understand the commitment. When all routes are blocked by allowed conditions, choose a different closure, route or optional objective; do not “fix” the situation with louder audio. This is an illustrative design argument, not an observation or successful test. [C-02; C-05]

### Illustrative nonspatial adaptation: shared workshop access

A persistent community event offers a public workshop before maintenance. Players can prepare now, reserve a later alternative or decline the event. The public schedule does not reveal other players’ private inventories. If the event’s only desired experience is relaxed crafting, omit the deadline; persistence alone does not justify manufactured urgency. The meaningful alternative, not the genre label, determines fit. [C-02; C-05]

### Documentary comparison, not a worked implementation

The 2026 PUBG letter distinguishes pressure problems by mode; Riot’s support page describes signals about objective intent. These illustrate different components. Neither source reports this recipe, tests its workshop adaptation or establishes a combined benefit. Exact source versions are retained below. [C-03; C-06]

## Tradeoffs, alternatives and opportunity cost

A public forecast can make planning easier while reducing the value of discovering a schedule. Preserving hidden opponent state can sustain scouting while leaving outcomes genuinely uncertain. Multiple routes increase choice only when their costs and feasibility matter; authoring and maintaining them can exceed the value of the technique. [C-05]

Alternatives are a fixed public objective, an untimed choice, player-triggered escalation, uncertain events with clearly uncertain forecasts, or a guided sequence whose goal is execution rather than strategic choice. Fact-preserving cue alternatives remain useful even when this pressure pattern is omitted. Do not duplicate the entire P02 recipe inside a genre implementation. [C-01; C-05]

## Failure cases and do-not-use conditions

**Forced funnel disguised as choice:** every path fails for one permitted capability. Investigate geometry and available preparation; reject the pressure if no acceptable alternative remains. **Information leak:** an accessible warning reveals a private adversary or an unearned route. Rebuild the fact sheet. **Pressure stack:** damage, time, loot loss and team blame change together; isolate consequences. **Clock authority failure:** a deadline silently moves or expires before an acknowledged action; clarify which state governs. [C-02; C-04; C-05]

Do not use when surprise timing is the purpose, when deliberate contemplation is the promise, when private events cannot be fairly forecast, or when deadlines mainly create attendance pressure without a valued in-session decision. The strongest counterexample is a game whose skill is discovering and exploiting an uncertain schedule: making that schedule public can remove its central challenge. Another is strict execution play where offering alternate routes dilutes the desired test. [C-05]

## Proposed falsifying playtest — not performed

**Question:** does a public forecast with feasible alternatives improve understood choice without false opponent certainty or unacceptable execution pressure? Compare the existing constraint, a public-fact forecast, and a revised-opportunity alternative. Keep map, allowed capabilities and opponent information fixed where possible; separately vary geometry when testing opportunity rather than presentation. [C-07]

Include participants with differing map familiarity, strategic experience and relevant access requirements. Use consent-based simulations rather than live competitive accounts. Counterbalance repeated scenarios; record what the participant believed before showing the outcome. Measure rule understanding, reachable options, selected tradeoff, false certainty, task workload and valued decision-making. Do not use survival alone as the success criterion. [C-07]

Reject or adapt the recipe if comprehension improves but meaningful choices disappear, if one channel supplies unauthorized knowledge, if the least mobile permitted capability has no usable response, or if an untimed alternative better serves the intended experience. Sample size, timing settings and practical decision thresholds require a local method review; none were chosen or tested here. [C-07]

## Claim ledger

| Claim | Proposition / class | Support and locator | Confidence and limit |
|---|---|---|---|
| C-01 | Public constraints and hidden state can be specified separately; `inference`. | Selected F02 decision excerpt and P02 fact-preserving pattern. | Moderate conceptual support; no game-specific effect validation. |
| C-02 | Audit feasible responses before imposing pressure; `hypothesis`. | C-01 and the conditional consequences of the proposed rules. | Low benefit confidence; some audiences deliberately want forced execution. |
| C-03 | PUBG’s developer rationale distinguishes mode-specific pressure problems; `practitioner-heuristic`. | `GDR-SRC-20261010-G21-012`, Normal Match, Ranked and Looking Ahead. | High attribution, low generalized causal support. |
| C-04 | Forecasts and alternative cues should preserve fact, uncertainty and authority; `inference`. | Selected P01/P02 corrections and F02 information contract. | Moderate reasoning; no guarantee of equivalent experience. |
| C-05 | The combined recipe may preserve deliberate choice; `hypothesis`. | C-01–C-04; contrary cases in this entry. | Low: no empirical validation of the combination. |
| C-06 | Riot documents objective-intent signaling; `observed-example` of a document. | `GDR-SRC-20261010-G21-010`, Objective Voting. | High documentary scope, not proof of coordination or safety. |
| C-07 | The proposed comparisons could falsify this pattern; `hypothesis`. | C-02–C-05 and F07 evaluation excerpt. | Low until reviewed and performed; no results. |

## Related entries, ownership and history

Adaptations: [MMO](../genres/mmo.md), [MOBA](../genres/moba.md), [battle royale](../genres/battle-royale.md). Complement: [Bounded return before final elimination](bounded-return-before-final-elimination.md) only when return is affected by the public phase.

Inspected related identities: `GDR-CAND-20261010-F02-TOP-01`, `GDR-CAND-20261010-P01-TOP-03`, `GDR-CAND-20261010-P02-TOP-03`, `GDR-CAND-20261010-P02-PAT-02`, and `GDR-CAND-20261010-F07-TOP-01`. Exact dependency bytes and locators are in the [review packet](../reviews/full-run-20261010-g21-review-packet.md#inspected-reviewed-dependencies). F06 and W03 selected input is still missing. Novelty/duplication review must distinguish this constraint-and-opportunity recipe from P02’s communication-only recipe.

Conflict: `G21-CON-05` and `G21-CON-08`. `0.1.0`, `initial-authoring-1`, no predecessor or supersession. Author self-review only; current hash is in the packet. Further research remains open on spatial feasibility, accessible execution and whether the pattern should merge into a shared owner’s existing concept. No canonical owner or permanent ID is allocated.

## References

All sources were inspected on **2026-10-10, America/Los_Angeles session date**. Access describes the material actually read, not the availability of an entire website. No game client or recording was observed; game examples below are observations of official documentary artifacts. No third-party pages linked by these documents are implicitly inspected. Source identities are run-scoped; central URL/DOI/edition deduplication remains pending. Rights: copyrighted material is paraphrased; no screenshots, substantial quotations, chat logs or source PDFs are redistributed. No reuse license is assumed.

### GDR-SRC-20261010-G21-010

Laserface / Riot Games. *Smart Ping*. 2025-02-18. League of Legends Support. [Inspected source](https://support.riotgames.com/en-us/league-of-legends/gameplay/smart-ping).

**Version/build:** Support revision, runtime patch unknown. **Access:** `relevant-excerpt`; Smart Ping Wheel; Terrain and Mini-Map Visuals; Objective Voting; retrieved lines 27–87. **Type:** official mechanics documentation. **Supports:** C-06. **Limits and independence:** Documents communication options; faster/safer language is developer advice, not tested comparative benefit. Same Riot family as 006.

### GDR-SRC-20261010-G21-012

PUBG: BATTLEGROUNDS Team / KRAFTON. *[Dev Letter] Blue Zone Revamp*. 2026-06-16. PUBG official site. [Inspected source](https://pubg.com/en/news/10280).

**Version/build:** PC/console developer letter; runtime deployment not independently verified. **Access:** `relevant-excerpt`; Opening; Normal Match; Ranked and Esports; Blue Zone Damage; Looking Ahead; retrieved lines 49–94. Only prose used, not chart measurements. **Type:** firsthand developer analysis and rationale. **Supports:** C-03. **Limits and independence:** Reports internal observations without a reproducible dataset/protocol here. Proposed benefits remain intent; Normal/Ranked differences must not be collapsed. Same KRAFTON family as 011/013/014.


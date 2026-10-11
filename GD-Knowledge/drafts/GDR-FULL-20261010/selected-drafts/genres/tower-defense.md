---
id: GDR-CAND-20261010-G09-GEN-02
kind: genre
title: Tower defense
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
run_id: GDR-FULL-20261010
batch_id: G09
attempt_id: G09-authoring-01
owner_project: BH-GDR-Genres
updated: '2026-10-11'
evidence_checked: '2026-10-11'
date_basis: UTC; run and authorization date remain 2026-10-10
aliases:
- TD
- defense planning
- maze defense
tags:
- placement
- routes
- waves
- upgrades
- recovery
- direct-intervention
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-02
- GDR-CAND-20261010-P02-TOP-03
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
- GDR-CAND-20261010-W02-TOP-02
- GDR-CAND-20261010-P01-TOP-03
related_patterns:
- GDR-CAND-20261010-F02-PAT-01
- GDR-CAND-20261010-P02-PAT-02
- GDR-CAND-20261010-F07-PAT-01
- GDR-CAND-20261010-G09-PAT-01
related_genres:
- GDR-CAND-20261010-G09-GEN-01
- GDR-CAND-20261010-G09-GEN-03
source_ids:
- GDR-SRC-20261010-G09-007
- GDR-SRC-20261010-G09-008
- GDR-SRC-20261010-G09-009
- GDR-SRC-20261010-G09-010
- GDR-SRC-20261010-G09-011
- GDR-SRC-20261010-G09-012
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-G09
predecessor_sha256: null
supersedes: null
change_summary: Initial G09 candidate; no prior candidate superseded; coverage remains
  open.
hash_record: ../reviews/full-run-20261010-g09-integrity.md
---

# Tower defense

**Draft genre guidance; coverage open.** This entry concerns arranging and operating defenses against incoming threats to a protected objective, with preparation and accumulated placement decisions materially shaping resolution. It covers planning, routes, waves, intervention and recovery. It does not provide a universal tower roster, an optimal maze, a wave generator or a released balance rule.

## Definition and boundaries

The working center of **tower defense** is repeated defense of an objective against incoming threats, where placement, preparation or investment in defensive capabilities is a major source of player agency. “Tower” can be a trap, character, emplacement or another persistent defensive commitment. “Defense” need not mean killing every attacker; protection, delay or permitted leakage can define success in an illustrative design. This is a provisional analytic definition rather than a claim that all market labels share identical rules. [C-01]

A **fixed-route** variant limits control of enemy topology and emphasizes coverage, target suitability and timing. A **route-shaping/maze** variant also makes the path network a decision variable. Fixed routes do not necessarily imply fixed placement pads, and free placement does not necessarily allow changing the path. Record these axes separately. A base-defense or survival hybrid may add movable objectives, harvesting or exploration; a tower-defense entry is useful only when it supplies distinct guidance about the defense structure rather than relabeling the entire neighboring game. [C-01, C-12]

Do not make passivity a membership condition. The developer description of **Defender's Quest DX** advertises commands while paused and adjustable battle speed; **Kingdom Rush Origins** advertises heroes and direct powers; **Orcs Must Die 3** is described by its design director as third-person defense using traps and weapons. These are different forms of agency, not an empirical ranking of “active” and “passive” designs. [C-02–C-04; GDR-SRC-20261010-G09-007; GDR-SRC-20261010-G09-008; GDR-SRC-20261010-G09-009]

Cooperative and competitive are facets, not contradictory classifications: the Defense Grid 2 product description lists both alongside solo play. Their detailed rules must be inspected separately before importing a shared-economy or opponent-sending model. This batch does not pretend the listing supplies those rules. [C-05; GDR-SRC-20261010-G09-010]

## Custom research instructions

For each future case, reconstruct **the threat route, legal defense footprint, target rules, resource schedule, forecast boundary, commitment time and failure accounting** from a versioned primary rule source or reproducible observation. Distinguish an unbuildable tile from an invalid route, a legal placement from an effective one, and a planning preview from an actual combat prediction. Record exceptions such as flying, teleporting, changing routes and movable defenders rather than assuming one shortest-path model. [C-01, C-08, C-09]

Compare fixed-route and route-shaping designs; authored and generated waves; refundable, partially refundable and locked commitments; command-pause, real-time direct intervention and limited-use powers; level-local and across-run progression; solo, shared defense and adversarial variants. The first pass below covers examples of these structures unevenly. Do not claim that a complete list of variations is already researched. [C-01, C-12, C-14]

Challenge three misleading comparisons. First, a lower leak count can reflect easier threats rather than better planning. Second, a longer maze may be worse if it sacrifices damage coverage or routes a threat into an incompatible target zone. Third, an expensive upgrade's high damage total does not prove that cheaper support has become useless—or that it remains useful. Compare role, exposure, opportunity cost and the contribution's timing, not isolated totals. [C-08, C-10, C-15]

The next source search should prioritize versioned wave forecasts, placement/sell rules, documented routing edge cases, original player planning studies and negative reports of adaptive-wave systems. Seek evidence on disabled players using actual placement and time controls, not only the availability of an option in a store description. Cooperative griefing and competitive economy rules remain missing primary-source routes. [C-07, C-13, C-14]

## Player promises and varied audiences

Candidate promises include **a plan that matters when tested**, **observable interaction among defenses**, **a chance to improve the next commitment**, and **an understandable protection objective**. These are hypotheses about useful design goals, not a universal audience survey. Some audiences may seek a largely solvable construction puzzle; others may seek improvisation under pressure, an action role within the defense, a persistent character build or shared responsibility. [C-01, C-08, C-13]

Information that helps one promise can weaken another. Exact wave revelation may be central to a planning puzzle but remove desired reconnaissance or reactive adaptation. A long unpausable build timer can turn a spatial decision into an input-speed test. A freely movable defense may invite experimentation, but also let one configuration impersonate every specialized role during a wave. The correct question is which decisions should be difficult and when commitment should become consequential. [C-08, C-09, C-10]

## Characteristic loops and structures

A useful provisional loop is **inspect the threat and terrain → commit defense resources → observe or intervene in resolution → retain costs and consequences → revise before the next threat**. Not every game has a separate build phase, and a continuous defense may interleave these actions. The loop is an analytical tool, not a required UI layout or pacing prescription. [C-01]

Emberward's official description connects limited wall-block cards, maze construction and room for towers. Its documented choice is not simply to maximize path length: route space competes with deployment space. The source is a product description, not a route simulation or proof of superior strategic depth. [C-06; GDR-SRC-20261010-G09-011]

### Forecasts: reveal the intended planning problem

Separate four forecast layers: **known rules** such as target eligibility; **known scenario constraints** such as entrances; **announced threat information** such as a class or arrival window; and **deliberately unknown outcomes** such as a future target draw. A preview should state which layer it represents. Displaying one possible path as a guaranteed path is inaccurate when a later placement or enemy behavior can change it. [C-08]

The proposed benefit chain is conditional: useful advance information makes a relevant constraint available; the player must notice and understand it; a feasible response must exist; the commitment window must permit that response; and the experience must still contain the intended challenge. None of those later links follows merely from displaying an icon. If the desired challenge is choosing robust coverage under uncertainty, compare a categorical forecast with exact sequencing rather than assuming full disclosure is the improvement. [C-08, C-13]

### Placement reversibility is not one switch

Separate cancelling an uncommitted preview, correcting an accidental placement, selling a committed defense, relocating during combat and replaying after observing a wave. These actions restore different resources and expose different information. A refund can return currency without restoring elapsed time, revealed enemies or the opportunity to attack while a tower stood elsewhere. Thus a full refund is not automatically a full rollback. [C-09]

Before choosing a refund fraction or relocation rule, identify what commitment is intended to test. For a construction puzzle, reversible planning may be the activity rather than an assist. For real-time defense, unrestricted combat relocation may erase intended coverage choices or add repetitive high-speed manipulation. Consider a planning-only preview, a clear paid sell action, a limited relocation resource or no relocation. No universal refund rate is established here. [C-08, C-09]

### Waves, recovery and misleading adaptation claims

Hind and Harvey compared generated and authored wave conditions with **22 experienced tower-defense participants, 11 per condition**, using remote short play and the Game Experience Questionnaire. Their reported non-significant differences do not establish equivalence or superior experience; their discussion's learning/timing explanation remains a proposed explanation rather than a demonstrated mechanism. [C-07; GDR-SRC-20261010-G09-012]

Consequently, use wave-generation capability as a production option to evaluate, not as evidence that adapting to a defense always improves the game. If the next wave silently invalidates whichever role the player invested in, the system may negate planning rather than provide responsive challenge. Conversely, a fixed schedule can become rote. Compare the intended learning and uncertainty under controlled schedule differences, and record whether forecasts remain truthful after adaptation. [C-08, C-11]

Recovery also has several balances: remaining objective health, next-wave resources, upgrade debt, route availability and player knowledge. A defeat spiral can occur in an illustrative economy where leaks both reduce survival and remove the income required to answer later threats. It is a design-specific causal structure, not a claim that every tower-defense game pays only for kills. Retrying from the beginning, preserving resources, compensating losses or narrowing the next scenario have different costs and promises. [C-11]

## Design choices and conditional application

| Decision | Proposed approach and mechanism | Failure, alternative and exit |
|---|---|---|
| Routing and legal placement | Show the actual legal footprint and relevant route consequences at the commitment boundary. Validate ground and exceptional movement rules separately. [C-08, C-09] | A preview that ignores flying or dynamic entrances overpromises. Show qualified coverage/legality rather than an unsupported guaranteed route. |
| Forecast granularity | Match disclosure to the intended skill: known rules plus a class forecast for robust planning; exact authored schedule for a solvable planning challenge. [C-08] | Forecasts can remove desired uncertainty or produce memorized solutions. Compare category, range and exact variants rather than “more is better.” |
| Reversible planning | Separate preview cancellation from changing a completed investment. Retain known consequences when information has already been gained. [C-09] | Excessive confirmation burdens trivial actions; unrestricted relocation can replace strategy with rapid manipulation. Omit the extra layer when ordinary targeting is sufficient. |
| Upgrade roles | Compare an upgrade against the role it occupies and the opportunities it excludes, including enabling, delaying and coverage contributions. [C-10] | If an upgrade dominates all roles at all relevant budgets, the roster may have collapsed; if universal late-tier replacement is the explicit promise, preserving every early niche may be unnecessary. |
| Direct intervention | State whether the player's weapon, hero, spell or targeting command supplements a viable plan or is essential to survival. [C-04, C-13] | A purported strategy game can silently require precision aiming. Optional automatic assistance may change competitive rules and needs a disclosed local policy. |
| Recovery | Examine whether the next state still admits an understandable response and whether a retry teaches anything new. [C-11] | Do not secretly rescue every loss or punish success to force a curve. A shorter level, explicit checkpoint or accepted failure may serve the goal better. |
| Cooperative ownership | Define build/sell authority, resource claims, pause consent, credit and reconnect effects before shared-space tuning. [C-12] | A global refund may let another player dismantle a partner's plan. Use scoped permissions or separate lanes where shared authority is not the intended challenge. |

**Application sequence — proposed.** Choose the protection goal and expected intervention demand. Draw the route/placement constraint model, including exceptions. Identify one targeted misunderstanding or planning failure. Change either information, reversibility, economy or threat schedule first, unless the hypothesis explicitly concerns their interaction. Compare the most economical truthful presentation with the richer version. Request separate authorization for the prototype and participant test; this research does not execute either. [C-08–C-14]

### Worked example: a two-lane defense — illustrative

A fictional defense protects a relay from ground convoys and occasional flying scouts. Ground threats follow either of two visible entrances; scouts ignore the maze. The player knows tower targeting rules and receives a forecast of “armored ground threat; possible air pressure,” not an exact sequence. A route preview labels itself ground-only and re-evaluates after each wall preview. [C-08, C-09]

The designer offers a slow-field tower, armor-breaking support and anti-air. A damage-only end screen makes the slow field appear weak. Before increasing its damage, inspect whether it delayed threats inside another tower's range, whether armored threats actually encountered the support and whether anti-air had an eligible target. A factual trace can show those events; it cannot honestly promise that replacing one tower would have guaranteed victory unless a separately validated counterfactual model supports that narrower statement. [C-10, C-15]

Suppose free relocation during the wave allows one anti-air tower to cover both entrances through repeated dragging. This may be an intended dexterity challenge, or an unintended shortcut around budget and placement. A planning-only relocation variant preserves experimentation without requiring that continuous manipulation. Compare the variants with participants who differ in input needs, and record the intended skill rather than calling either result automatically fairer. [C-09, C-13]

### Worked example: loss without a hidden insolvency trap — illustrative

A fictional campaign carries objective damage into its next defense. A player who allows a leak loses health but still receives the explicitly promised preparation grant. The next scenario can therefore test revised planning rather than an undisclosed loss of both health and funding. An alternative campaign intentionally carries economic losses too; it must expose that cost and offer an honest restart or recovery route if recovery is part of its promise. Neither structure is established as universally superior. [C-11]

## Applying shared topics

The [reviewed dependency table](../reviews/full-run-20261010-g09-review-packet.md#reviewed-dependency-transfer) identifies the actual parent-selected bytes. Every transferred entry remains **0.1.0 draft**. G09 does not reclassify the external studies cited inside them as directly inspected public sources. [C-14]

| Inspected identity | Tower-defense adaptation, not duplicated topic text |
|---|---|
| `GDR-CAND-20261010-F02-TOP-01` Decision design | Separate threat-rule knowledge, forecast uncertainty and irreversible construction; a refunded placement does not undo information gained. |
| `GDR-CAND-20261010-F02-TOP-02` Challenge and difficulty | Separate spatial planning, target comprehension, time pressure and direct motor intervention before adjusting difficulty. |
| `GDR-CAND-20261010-P02-TOP-01` Controls and input | Evaluate placement, cancellation, target selection and accessible activation during actual build/combat conditions. |
| `GDR-CAND-20261010-P02-TOP-02`, `GDR-CAND-20261010-P02-TOP-03` Feedback; Multimodal communication | Distinguish legal placement, build acceptance, invalid target, damage and objective leakage. Alternative routes retain the same permitted facts, not hidden wave content. |
| `GDR-CAND-20261010-F07-TOP-01`, `GDR-CAND-20261010-F07-TOP-02` Evaluation; Ethics | Separate an adaptive generator's output from player benefit; assess optional purchases and session obligations without diagnosing intent or treating engagement as wellbeing. |
| `GDR-CAND-20261010-W02-TOP-02` Quests and objectives | State whether success is protection, delay, kill count or another goal. Do not imply that merely killing a wave satisfies a method-essential defense objective. |
| `GDR-CAND-20261010-P01-TOP-03` Accessibility | Apply functional task evaluation, not an imported universal numerical target size, alert duration or font rule. |

F03's economy topic body, W03's spatial/exploration bodies and F05/F06 systemic/social guidance were not available as inspected reviewed dependencies. F03/W03 reviews are active; F05/F06 and G08 are running/unreviewed according to the dispatch. No unseen candidate/source IDs are invented. Specific economic and pathfinding prescriptions must wait for their own verified rules and relevant owner review. [C-14]

## Pattern selection and adaptations

Use **Visible opportunity-cost comparison**, `GDR-CAND-20261010-F02-PAT-01`, for a known upgrade competing with a known defense need—not to reveal an unannounced boss. Use **Fact-preserving cue alternatives**, `GDR-CAND-20261010-P02-PAT-02`, for route class, protection state and invalid placement. Use **Triangulated balance diagnosis**, `GDR-CAND-20261010-F07-PAT-01`, for the designer's investigation of apparently weak towers; do not repackage it as a new tower-specific pattern. [C-14]

The new [Evidence-bounded resolution debrief](../patterns/evidence-bounded-resolution-debrief.md), `GDR-CAND-20261010-G09-PAT-01`, may show what a defense actually affected and which inputs remain adjustable. It remains an untested hypothesis. The next wave's hidden schedule is not necessary evidence for explaining a completed leak, and exposing it could change the game. A simple leak summary may be preferable when a full trace adds burden. [C-15]

A tower-defense/action hybrid may intentionally require real-time intervention; unconditional pause guidance would change that challenge. A tower-defense/roguelite hybrid may value uncertain run adaptation over exact wave solving. A tower-defense/[4X](4x.md) hybrid may retain strategic damage even when a local encounter permits rebuilding. A competitive tower-defense/[auto-battler](auto-battler.md) hybrid must specify whether scouting and opponent composition alter wave promises before or after commitment. No genre rule wins automatically. [C-12]

## Representative cases and negative cases

The documentary range includes pause-capable character defense, hero/spell intervention, third-person traps and weapons, cooperative/competitive mode listings and maze-building with constrained pieces. No named case proves a causal audience benefit. The studied prototype supplies narrow empirical counterweight to assuming adaptive waves improve experience, not a universal verdict against procedural generation. [C-02–C-07]

A strong counterexample to forecasting every threat is an explicitly chosen improvisational defense in which reconnaissance and reserve capacity are central. A strong counterexample to preserving every tower's late-game niche is a campaign whose intended progression replaces basic equipment. The test is whether the actual promise, costs and alternatives support those structures—not whether they conform to a blanket “all towers must always be viable” rule. [C-08, C-10]

## Accessibility, ethics, localization and production

**Proposed access work:** test preview and commitment separately; provide an alternative to precise drag placement where needed; make range, route and target eligibility distinguishable without color alone; and evaluate pause/speed controls against both information and action demands. Slow motion may reduce a timing demand without resolving tiny targets, unexplained immunity or simultaneous alerts. Accessibility options are not evidence of successful access until relevant participants can complete the intended task. [C-13, C-14]

For localization, define stable terms for ground/air, armor/resistance, sell/refund, upgrade/replace and protect/defeat. Test a complete failure message and revised plan, not isolated translated nouns. Brief icons need accessible text or narration where appropriate; verbose narration can compete with time-sensitive intervention. No universal equivalence across these routes is asserted. [C-13]

Persistent upgrades, consumable rescues or variable purchases need an explicit equity review when they alter available defensive options. A future study can use non-transactional mockups and state comparisons; actual purchasing is not authorized. Do not label a game exploitative solely because progression exists, or declare the arrangement fair because there is a free route. Assess understood costs, viable refusal and the offered contest. [C-13, C-14]

Route previews, dynamic pathfinding, enemy exceptions and cooperative construction multiply validation cases. An authored forecast may be simpler than a predictive simulator, but needs maintenance whenever a wave changes. An adaptive system must also preserve validity constraints and its disclosed information policy. The batch estimates no engineering cost or content-generation saving; production feasibility remains a local investigation. [C-08, C-11, C-13]

## Research questions and validation

**Proposed, not performed.** Obtain approval for participant work and prototype scope separately. Prespecify practical success and harm margins for the local experience rather than importing a universal participant count or tower-efficiency threshold. [C-13]

| Question | Comparison and context | Measures, confounds and falsification |
|---|---|---|
| Does forecast detail improve planning without trivializing uncertainty? | Compare no added forecast, category forecast and exact schedule using controlled encounters. Counterbalance exposure or use structurally matched waves to limit memorization. Include novice and experienced TD participants and relevant access routes. | Measure rule understanding, feasible plan diversity, desired uncertainty, avoidable leaks and information burden separately. Reject fuller disclosure when it mainly supplies the answer or degrades the intended improvisation. |
| Does reversibility correct error or erase commitment? | Compare preview-only cancellation, declared selling and in-wave relocation under matched resources; separate UI changes from economic rule changes. | Record accidental commits, repeated repositioning, strategic alternatives and input burden. Reject the richer relocation policy when high-frequency manipulation replaces the intended placement decision. |
| Does an upgrade preserve a useful role? | Use encounters where enabling, delay, coverage and direct damage have distinct relevance. Compare equivalent feasible investments, not equal nominal prices alone. | Record contribution sequences, eligible exposure and player explanations. Reject an “upgrade diversity” claim if one option dominates the declared roles or a claimed niche never occurs. |
| Does recovery remain a meaningful choice? | Compare clearly disclosed attrition policies, with equivalent initial failure states and known retry costs. Keep account progression fixed. | Measure recognized recovery plans, repeated unavoidable failure and willingness to continue without pressure. A higher retry count is not sufficient evidence of a better experience. |
| Does an adaptive wave method change experience? | Reproduce a clearly specified authored/adaptive comparison before generalizing the original study. Control wave timing, composition and forecast information or model them explicitly. | Report uncertainty and practical differences; non-significance alone cannot pass an equivalence claim. Reject a causal learning explanation without measures that distinguish it from simpler schedule differences. |

Learning probes should use new states with the same target/routing rule and include both valid and invalid placements. A newly introduced flying rule is a separate adaptation test, not evidence of failed transfer of the former ground-only rule. Preserve necessary access routes throughout. [C-13, C-14]

### Coverage and next discriminating work

Researched: provisional route/placement distinctions, wave-information tradeoffs, intervention variants, reversibility, upgrade-role questions, attrition models, hybrid conflicts and one original empirical wave study. Open: complete versioned sell/forecast/route rules, comparative foresight and recovery evidence, asynchronous/cooperative permission models, competitive sends, account-power impacts, actual access outcomes and generative production costs. The next decision question is **whether the target experience asks players to solve a known defense problem or to prepare robustly for deliberately incomplete information**. That answer precedes forecast and refund tuning. [C-01, C-08–C-15]

## Claim ledger

Claim IDs are local to this file. Working definitions and application proposals are not approved studio decisions. Documentary `observed-example` means the cited description was inspected; no game binary or player behavior was observed. Confidence concerns the exact scoped proposition, not the genre as a whole.

| Claim | Precise proposition | Class | Support / locator | Confidence and applicability | Unresolved / contrary case |
| --- | --- | --- | --- | --- | --- |
| C-01 | The candidate boundary centers on preparing and operating defenses; route topology, placement freedom and time model are distinct axes. | inference | Definition in this file; sources 007–011 provide limited contrasting examples. | Moderate analytic distinction, no approved universal taxonomy. | Some base-defense hybrids need different ownership; full variant prevalence unresearched. |
| C-02 | Defender’s Quest DX advertises adjustable speed and commands while paused. | observed-example | GDR-SRC-20261010-G09-007; About This Game. | High documentary confidence, not binary or access validation. | Availability of pause does not prove all TD is passive or accessible. |
| C-03 | Kingdom Rush Origins advertises tower roles, upgrades, heroes and direct powers. | observed-example | GDR-SRC-20261010-G09-008; Features. | High for listed features, no balance effect. | Exact placement restrictions not established here. |
| C-04 | Jones describes third-person trap/weapon defense, Scramble attrition and an intended synergy response to favored traps. | practitioner-heuristic | GDR-SRC-20261010-G09-009; opening and Acid Geyser sections. | Moderate for firsthand rationale, low causal generalization. | Reported design intent does not establish successful role diversification. |
| C-05 | Defense Grid 2 advertises solo, cooperative and competitive modes. | observed-example | GDR-SRC-20261010-G09-010; features. | High documentary confidence. | Detailed ownership/economy rules uninspected. |
| C-06 | Emberward advertises maze-building with limited wall-block cards and competing tower-space needs. | observed-example | GDR-SRC-20261010-G09-011; About This Game. | High for description; no route simulation or gameplay observation. | Does not establish an optimal maze or generalized depth effect. |
| C-07 | The small remote TD study reported no significant experience difference; it did not demonstrate equivalence or adaptive superiority. | empirical-evidence | GDR-SRC-20261010-G09-012; §§3.3, 4.1–4.2. | Moderate, scoped sample/method; no equivalence test supplied for this conclusion. | Author null/equality wording is narrower in this candidate; G09-CON-06. |
| C-08 | Forecast detail and legality information may support intended planning only when understanding, feasible response and preserved challenge follow. | hypothesis | Explicit causal chain and proposed tests here; 011/012 motivate constraints only. | Low efficacy confidence; no direct comparative foresight result. | Exact disclosure can trivialize uncertainty or become stale; G09-CON-04. |
| C-09 | Currency refunds do not necessarily restore time, information or intervening opportunities; reversal policies should distinguish those states. | inference | F02 inspected decision/commitment excerpts; illustrative placement cases. | High logical distinction; low outcome confidence for a policy. | A planning puzzle may intentionally permit unlimited revision. |
| C-10 | Role-sensitive comparisons may diagnose upgrade pressure more usefully than direct-damage totals alone. | hypothesis | 009 developer rationale; own enabling/exposure analysis; F07 dependency. | Low efficacy; no cross-game validation. | Universal replacement may be intentional; G09-CON-05/08. |
| C-11 | Recovery and adaptation should be evaluated against the next feasible decisions and disclosed attrition, not merely retry count or closeness. | hypothesis | 009/012 motivate alternatives; local proposed mechanisms. | Low; no recovery experiment performed. | Rescue can negate desired failure or make planning unreliable. |
| C-12 | Hybrid intervention, persistence and shared ownership require explicit rules rather than a genre-precedence rule. | inference | 007–011 contrasts; illustrative hybrid analysis. | Moderate logical applicability, not complete multiplayer evidence. | F05/F06/G08 guidance and detailed PvP rules unavailable. |
| C-13 | Access, localization and commitment effects require task-level testing and non-transactional ethical scrutiny. | hypothesis | P01/P02/F07 inspected dependencies; proposed evaluations. | Low outcome confidence; no local participants or purchases. | Combined access needs, fatigue, co-op burden and persistent-power effects open. |
| C-14 | Only inspected reviewed dependency excerpts and their corrections are transferred; missing topic bodies remain gaps. | inference | G09 packet: Reviewed dependency transfer. | High for local inspection; not revalidation of underlying studies. | F03/W03 bodies unavailable; F05/F06/G08 unreviewed. |
| C-15 | A factual contribution trace may support revision without establishing a unique cause or guaranteed winning counterfactual. | hypothesis | GDR-CAND-20261010-G09-PAT-01; worked examples and test plan. | Low; exact pattern not validated. | Sparse traces, hidden schedules and overload can defeat it; G09-CON-08. |

## References

### GDR-SRC-20261010-G09-007

Level Up Labs, LLC. **[Defender’s Quest: Valley of the Forgotten (DX edition) — Steam store description](https://store.steampowered.com/app/218410/Defenders_Quest_Valley_of_the_Forgotten_DX_edition/)**. Level Up Labs / Steam. Publication/update: description update unknown; store release date 2012-10-30. Edition/build: DX listing; binary patch unspecified. Accessed 2026-10-11 UTC; access: `relevant-excerpt`. Locator: About This Game, paragraphs on character-based towers and battle speed / pause; retrieved text lines 165–169. Type: developer-published product description. Supports: C-02. Independence: Level Up Labs. Limits: Advertised mechanics, not observed accessibility outcomes; original release metadata does not date the current description. Rights: Copyright retained by authors/publisher; paraphrase and links only; no media or source text redistributed.
### GDR-SRC-20261010-G09-008

Ironhide Game Studio. **[Kingdom Rush Origins — press kit](https://play.kingdomrush.com/kingdom-rush-origins-presskit)**. Ironhide Game Studio. Publication/update: unknown. Edition/build: Origins press-kit web description; patch unspecified. Accessed 2026-10-11 UTC; access: `relevant-excerpt`. Locator: Description and Features, retrieved text lines 46–60. Type: official product / press documentation. Supports: C-03. Independence: Ironhide. Limits: Confirms advertised tower roles, upgrades and direct powers; does not document exact placement restrictions or prove role balance. Press assets not copied. Rights: Copyright retained by authors/publisher; paraphrase and links only; no media or source text redistributed.
### GDR-SRC-20261010-G09-009

Jerome K. Jones, Design Director, Robot Entertainment. **[Orcs Must Die 3’s Scramble mode and new trap revealed](https://blog.playstation.com/2021/07/13/orcs-must-die-3s-scramble-mode-and-new-trap-revealed/)**. PlayStation Blog. Publication/update: 2021-07-13. Edition/build: Pre-PS4-launch development account, 2021. Accessed 2026-10-11 UTC; access: `relevant-excerpt`. Locator: Opening paragraphs; “Goals for Scramble”; “The Acid Geyser,” especially retrieved text lines 57–60 and 80–87. Type: firsthand developer account. Supports: C-04; motivates C-10–C-11. Independence: Robot Entertainment. Limits: Reports design rationale, shared attrition and synergy; informal observation does not validate the intended diversification or audience benefit. Rights: Copyright retained by authors/publisher; paraphrase and links only; no media or source text redistributed.
### GDR-SRC-20261010-G09-010

Hidden Path Entertainment. **[DG2: Defense Grid 2 — Steam store description](https://store.steampowered.com/app/221540/DG2_Defense_Grid_2/)**. Hidden Path Entertainment / Steam. Publication/update: description update unknown; store release date 2014-09-23. Edition/build: Defense Grid 2 listing; binary patch unspecified. Accessed 2026-10-11 UTC; access: `relevant-excerpt`. Locator: About This Game / features, retrieved text lines 225–255. Type: developer-published product description. Supports: C-05. Independence: Hidden Path Entertainment. Limits: Supports advertised solo, cooperative and competitive modes; does not specify their complete economic or routing rules. Rights: Copyright retained by authors/publisher; paraphrase and links only; no media or source text redistributed.
### GDR-SRC-20261010-G09-011

Refic Games. **[Emberward — Steam store description](https://store.steampowered.com/app/2459550/Emberward/)**. Refic Games / Steam. Publication/update: description update unknown; store release date 2026-09-17; Early Access 2024-06-25. Edition/build: Post-release listing inspected in 2026; binary patch unspecified. Accessed 2026-10-11 UTC; access: `relevant-excerpt`. Locator: About This Game, maze / wall-block cards, tower footprints and progression; retrieved text lines 163–198. Type: developer-published product description. Supports: C-06; motivates C-08. Independence: Refic Games. Limits: Documents advertised maze-building constraints and persistent talents; neither route simulation nor player experience was observed. Rights: Copyright retained by authors/publisher; paraphrase and links only; no media or source text redistributed.
### GDR-SRC-20261010-G09-012

Daniel Hind and Carlo Harvey. **[Using a NEAT approach with curriculums for dynamic content generation in video games](https://link.springer.com/article/10.1007/s00779-024-01801-z)**. Personal and Ubiquitous Computing 28, 629–641 (Springer). Publication/update: 2024-04-11. Edition/build: Original journal article; DOI 10.1007/s00779-024-01801-z. Accessed 2026-10-11 UTC; access: `relevant-excerpt`. Locator: Sections 3.3, 4, 4.1 and 4.2; retrieved HTML lines 196–231 and 270–279. Type: original empirical player study and technical evaluation. Supports: C-07; limits C-08/C-11. Independence: Hind/Harvey research prototype. Limits: 22 experienced TD participants, 11 per condition, remote short exposure and GEQ. Non-significance is not an equivalence finding; adaptive-wave superiority and the proposed learning explanation are not demonstrated. Rights: Publisher article accessed publicly; license terms not audited for redistribution. Paraphrase and citation only.

## Review and history

Version **0.1.0**, candidate revision **initial-draft-1**, first G09 submission. Author self-review is in the [review packet](../reviews/full-run-20261010-g09-review-packet.md#author-self-review). Independent review has not occurred for G09; approval fields remain null. Exact bytes are identified in the [integrity receipt](../reviews/full-run-20261010-g09-integrity.md). No predecessor or supersession is claimed. All playtests above are proposed, not performed. This file is a completed draft artifact with incomplete evidence coverage, not released genre knowledge.

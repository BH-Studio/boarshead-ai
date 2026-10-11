---
id: GDR-CAND-20261010-W04-TOP-01
kind: topic
title: Encounter and scenario composition
version: 0.1.0
status: draft
owner_project: BH-GDR-Worlds-and-Characters
run_id: GDR-FULL-20261010
batch: W04
candidate_revision: initial-draft-1
attempt_id: W04-initial-1
updated: '2026-10-10'
evidence_checked: '2026-10-10'
coverage_status: open
aliases:
- scenario orchestration
- encounter pacing
- recovery after encounters
- scenario exits
tags:
- escalation
- contrast
- resource-pressure
- alternatives
- recovery
- revisit
- evidence-open
related_topics:
- GDR-CAND-20261010-W04-TOP-02
- GDR-CAND-20261010-W04-TOP-03
- GDR-CAND-20261010-W02-TOP-02
related_patterns:
- GDR-CAND-20261010-W04-PAT-01
- GDR-CAND-20261010-W04-PAT-02
- GDR-CAND-20261010-W02-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-W04-001
- GDR-SRC-20261010-W04-004
- GDR-SRC-20261010-W01-09
permanent_id: null
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded W04 candidate; no prior batch replaced.
byte_hash_record: ../reviews/full-run-20261010-w04-review-packet.md#artifact-byte-manifest
---

# Encounter and scenario composition

**Draft research candidate; not released or approved guidance.** All examples marked illustrative are invented, not studio canon. No game, engine, prototype, participant study or player test was run. Recommendations are conditional inferences or hypotheses, not formal standards.

## Decision and scope

This entry helps a designer choose **which situation comes next, under which player circumstances, and with which ways out**. Its subject is orchestration rather than the balance of an attack, currency, movement ability or reward schedule. A working **encounter** is a bounded arrangement of actors, information, obstacles and opportunities that changes the player’s immediate situation. A **scenario** connects encounters through continuing circumstances and consequences. Neither term requires combat. A negotiation, salvage operation or difficult departure can satisfy these working definitions. These are organizing definitions for this draft, not an approved vocabulary allocation. [C-01]

The design question is not simply whether an encounter is exciting. It is whether its demands, alternatives, result and aftermath make sense for the histories that can actually reach it. **Escalation** changes the demands or stakes; **contrast** makes a difference perceptible against some earlier or concurrent condition; **recovery** offers an opportunity to regain a specified capacity. A reduction in newly introduced pressure is not, by definition, restoration of attention, orientation, resources or social coordination. Those are separate proposed observations. [C-02, C-05]

Included are entry conditions, escalation, contrast, resource pressure, alternate and nonviolent resolutions, exits, recovery and revisit states. Excluded are engine ownership, tactical tuning, economic exchange rates, a universal encounter-density target and game-specific canon. Foundations and Systems owns the underlying mechanics; this topic describes the player-facing combinations that those mechanics would need to support.

## Core explanation and mechanisms

### Compose against reachable states, not an imaginary average arrival

An authored sequence can depend on an earlier event without guaranteeing that the player experienced it. A now-hostile room is not necessarily a betrayal to someone who first enters it after the change. A request to spend a tool is not a real choice for someone who never acquired that tool. A peaceful interval may still contain a deadline, unresolved pursuer or difficult reading task. These are logical limitations on what a particular arrangement can promise, not empirical claims about how all players respond. [C-02]

Use a **state envelope**: a bounded description of materially different arrivals that the scenario supports. Separate possession from affordability, availability from discoverability, and exposure to information from understanding it. Include at least the histories implicated by the actual design, rather than constructing an exhaustive imaginary state space. The proposed benefit is earlier discovery of unsupported assumptions; no W04 study measures how much this improves production or experience. [C-02, C-09]

### Escalation has multiple dimensions

A useful authoring description distinguishes simultaneous demands, consequence severity, uncertainty, time pressure, resource commitment and social coordination. Increasing all of them at once obscures which change produced the intended contrast. Treat this as an analysis aid, not a claim that those dimensions are psychologically independent or share a numerical unit. [C-03]

The inspected Valve presentation describes a sequence that delays relaxation until existing combat pressure has subsided, while also identifying exceptions that can remain dangerous. This supports a concrete distinction between **reducing incoming pressure** and **the absence of outstanding threats**; it does not establish a universal recovery curve or a player-emotion measurement. [C-04; GDR-SRC-20261010-W04-001]

The application bridge is deliberately narrower: when the intended next activity requires reorientation, determine what currently prevents it. Reducing new arrivals can address one cause; it may not address pursuit, unread instructions or a resource deficit. A designer must specify which capacity the interval is intended to restore and which pressures are intentionally retained. Whether players recognize or value the result remains a hypothesis. [C-05]

### Alternatives need feasibility, not only labels

Spector’s postmortem distinguishes the team’s multiple-solution ambitions from the production need to author specific routes when simulation did not supply enough of them. The lesson transferable here is an uncertainty about **where alternatives will come from**, not an instruction that every game must provide all methods. [C-06; GDR-SRC-20261010-W04-004]

For a promised alternative, trace the route from its real prerequisites to its accepted outcome. A “negotiate” label is not a feasible route when its only interlocutor cannot be present in a supported arrival. Different routes may legitimately have different costs, information requirements or consequences. They need not be interchangeable, equally rewarded or equally appealing. An informed refusal may foreclose content rather than unlock a compensating prize. Jayanth’s account of the Isle of Cats supplies a creator-described contrary case to universal consequence-free access. It does not prove that costly refusal benefits every audience. [C-07, C-08; GDR-SRC-20261010-W01-09]

### Density is an incomplete pacing explanation

“More encounters” needs a denominator and a counting rule. Per room, per traversed distance, per minute of active play and per session can describe different exposures. One dense scene may contain optional observations; another may require continuous decisions. Travel, search, dialogue, retries and re-entry can all change experienced spacing without changing the placed encounter count. Consequently, an encounter-count comparison alone cannot isolate a pacing cause. This is a measurement inference, not a finding that density never matters. [C-03]

## Design choices and alternatives

| Choice | Appropriate conditions and proposed benefit | Cost, failure case and simpler alternative |
|---|---|---|
| Fixed authored sequence | Required entry conditions can be established; a specific juxtaposition is the goal. | A sequence can misread skipped histories. Narrow supported arrivals or author a different introduction instead of pretending a prior contrast occurred. |
| State-qualified sequence | Several materially different arrivals are genuinely supported. | Conditions and variants require continuity review. A smaller shared situation with fewer implied promises may cost less. |
| Open situation with systemic solutions | Relevant interactions already support the promised goal and can be inspected. | Emergence is not guaranteed. Deliberately author essential alternatives or reduce the breadth of the promise. |
| Explicit commitment point | A choice creates an important cost, time condition or durable outcome. | Excessive confirmation can obstruct simple actions. Put clarity at consequential boundaries rather than on every interaction. |
| Intermittent relief | Reorientation or another specified capacity is part of the intended experience. | Quiet may become predictable waiting, or relief may falsely advertise safety. Compare lower continuous pressure, a player-chosen pause or no added interval. |
| Deliberate unresolved or terminal outcome | Loss, refusal or an ending is an intelligible part of the local promise. | An apparent ending can actually be a defect. Give the outcome a supported closure, retry or departure rather than an unexplained dead end. |

These are proposed conditional choices, not empirical rankings. The strongest alternative to any elaborate composition scheme is a simpler situation that makes fewer promises and is easier to author, explain and maintain. [C-02, C-05, C-07, C-09]

### Exits without erased consequences

Separate these cases in the scenario description. **Decline before commitment** leaves the offered action unaccepted. **Retreat after commitment** preserves whatever changed unless the design explicitly says otherwise. **Concession** resolves the situation on different terms. **Retry** intentionally returns to an earlier defined condition. **Terminal outcome** closes a supported path. **Session interruption** concerns the person stopping play and need not be identical to a character’s escape. None logically requires that every cost disappear. [C-08]

For this entry, a **softlock** is an unintended inability to reach a supported next state, closure or recovery route because a needed condition cannot be satisfied. A deliberate loss is not automatically a softlock; an accidental missing interlocutor is not made meaningful merely by calling the game harsh. Diagnose the violated local promise before choosing a fix. The fix might preserve evidence, offer a different recipient, record an unsuccessful resolution, permit a retry or stop claiming the path is supported. [C-08, C-09]

## Application process

1. **State the intended decision and promise.** Specify what the player can influence, what remains uncertain, and which outcomes are fixed. Describe desired contrast as a relationship to an actual earlier condition, not merely an adjective such as “intense.” [C-01, C-02]
2. **List supported arrivals.** Consider resource availability, relevant ability, ally presence, prior resolution, prior exposure, interruption and revisit. Separate materially different states without inventing a universal matrix size. [C-02, C-09]
3. **Choose the pressure changes.** Describe what increases, what decreases and what persists. Mark resource categories separately; do not convert fatigue, money and reputation into an unexplained common budget. Consult Foundations for the actual mechanical rules. [C-03]
4. **Trace each advertised route.** Identify the goal, indispensable means, contingent means, discovery evidence, commitment boundary and accepted result. Preserve the reviewed W02 distinction between outcome and method. Where a method is the learning objective or expressive purpose, do not erase it by accepting any result. [C-07]
5. **Write exits and aftermath.** Trace refusal, retreat, failure, interruption and revisit. Record retained costs and unresolved obligations. Test the scenario’s conceptual reachability separately from its appeal. [C-08, C-09]
6. **Qualify recovery.** Name the intended recovering capacity, inspect residual pressure and provide appropriate evidence of the interval’s limits. An opportunity to check the route is not a promise of invulnerability or free replenishment. Use the linked recovery pattern only when that distinction matters. [C-05]
7. **Prepare accessible evidence and locale context.** Ensure that the proposed way of recognizing a commitment, alternative or changed state does not depend solely on an unexamined sensory channel or language-specific implication. Preserve uncertainty rather than adding omniscient explanations in the alternative presentation. Numerical presentation requirements belong to scoped presentation guidance, not this entry. [C-10]
8. **Compare with doing less.** Remove a variant, encounter or recovery stage when it adds obligations without a valued distinction. Establish local evaluation criteria before testing; revise or reject rather than interpret all outcomes as support. [C-09, C-11]

## Patterns and genre adaptations

[State-qualified recovery window](../patterns/state-qualified-recovery-window.md), `GDR-CAND-20261010-W04-PAT-01`, addresses the transition from residual pressure to a usable reorientation opportunity. It is not a universal alternation schedule. [Reaction eligibility and repetition contract](../patterns/reaction-eligibility-and-repetition-contract.md), `GDR-CAND-20261010-W04-PAT-02`, addresses correct acknowledgment after changed or revisited circumstances.

The inspected W02 `GDR-CAND-20261010-W02-PAT-02` remains the home for multi-route objective contracts. W01 `GDR-CAND-20261010-W01-PAT-01` remains the home for consequence-preserving reconvergence. F07 `GDR-CAND-20261010-F07-PAT-02` addresses understandable commitments and stopping; it is not duplicated as a third W04 pattern. Their external package paths and limits appear in the review packet rather than broken links to files not included here.

Different intended experiences can select different options: a method-learning exercise can constrain a route; an endurance challenge can withhold relief; a contemplative scene can omit escalation. These are conditional examples, not claims that a named genre always requires a particular structure. Current genre-specific adaptations have not been researched in W04.

## Examples and counterexamples

### Creator reports, not executed game observations

The Valve pacing presentation, Spector postmortem and Jayanth talk transcript offer contrasting production positions. The first supplies a pressure-transition example, the second exposes a gap between intended systemic alternatives and authored routes, and the third preserves an intentional cost of refusal. These are firsthand accounts with different purposes, not competing controlled experiments. Their concise source claims are C-04, C-06 and C-07; no commercial-success inference is made.

### Illustrative worked scenario: storm-relay depot

A relief crew needs a weather report before deciding whether to dispatch a ferry. The player enters a damaged relay depot. The invented local promise is to influence **whether and how a usable report reaches the crew**, not to control the storm or guarantee every rescue. No game canon or implementation is implied. [C-12]

A repair route needs an available cell and a calibration procedure. A negotiation route asks another station to relay the report and may create a later obligation. A physical-delivery route remains possible only while its route is passable. The designer must not silently assume the player has the cell, has met the station operator or can travel through a closed route. A prior trustworthy report can be accepted before the formal request; accepting it should not require replaying the scene merely to set its fiction into the expected order.

| Arrival or action | Proposed composition | Retained consequence / discriminating question |
|---|---|---|
| Cell available, repair unfamiliar | Let the player inspect the procedure before committing the cell. | Is the task learning the procedure or obtaining the report? Those are different acceptance rules. |
| Cell already spent elsewhere | Make the cost visible; do not display repair as currently feasible. | Are negotiation or delivery actually reachable, or is the scenario honestly unresolved? |
| Operator refuses | Preserve the refusal and explain its immediate scope through the conversation. | Is refusal an intended limit, or an accidental dependency the design promised would not matter? |
| Existing hazard still active | Reduce new complications, but do not call the room safe. | Can the player perform the planned reorientation activity without continuing hazard management? |
| Player retreats | Keep the spent cell or accepted obligation if the local commitment already occurred. | Does the return description acknowledge this history? |
| Player returns after report delivered | Replace the urgent request with an appropriate aftermath or silence. | Is a changed external circumstance a genuinely new request, rather than an accidental repeat? |

The proposed recovery interval lets the player examine the route and report state. It does not refill every resource. A designer may suspend a fictional deadline during that interval, or may explicitly preserve it; those are different designs that must not be compared as though only scenery changed. A missed dispatch can lead to a supported delayed outcome rather than a broken waiting state. Whether this treatment feels clear, humane or dramatically effective is untested.

### Strong counterexample

A scenario about refusing an exploitative bargain may depend on giving up content. A universal rule that every refusal must yield an equally attractive alternative would remove the intended conflict. Conversely, withholding a technical exit from play to intensify that fiction confuses character consequence with the person’s ability to stop. The distinction is conceptual; it does not establish that this particular story should be made. [C-07, C-08]

## Failure modes and constraints

**Recovery that creates work.** A lull filled with mandatory crafting, inventory repair or reading may move pressure rather than relieve the capacity being tested. Observe the actual activity; do not infer rest from the absence of enemies. An intentionally demanding maintenance phase can still be valid, but needs a different description. [C-05]

**False alternatives and erased consequence.** A route that depends on an impossible history is not made feasible by a menu option. A fallback that restores every cost may solve reachability while invalidating the original commitment. Diagnose both obligations before changing either. [C-07–C-09]

**Access and cultural assumptions.** A signal of danger, consent or social refusal may not be understood in every presentation or locale. Review the function of the signal with relevant people rather than treating a literal translation or added icon as proof. Avoid using unfamiliarity with an institution as evidence that a player lacks intelligence or care. This is a proposed inclusion safeguard, not a measured universal effect. [C-10]

**Production spread.** More alternate outcomes create more combinations for dialogue, state, presentation and continuity review. The draft makes no numerical complexity or cost-saving claim. Limit consequential distinctions deliberately, document unsupported cases and avoid making invisible collaborators responsible for unbudgeted repair work. [C-09, C-10]

## Playtest and validation

**All procedures below are proposed and not performed.** No recruitment, prototype, data collection, engine execution or game observation occurred. [C-11]

| Question | Comparison and procedure | Measures, confounds and rejection rule |
|---|---|---|
| Does qualifying a recovery interval improve the specified opportunity? | Compare the same scenario with time-only versus residual-pressure-qualified entry. Hold rewards, overall pressure and information as comparable as practical; record differences that cannot be controlled. | Observe completion of the intended reorientation action, errors about remaining threats, reported opportunity and unwanted waiting. Reject the added qualification if it supplies no locally meaningful improvement or creates unacceptable delay; define that boundary before testing. |
| Are alternatives feasible and understood? | Present supported arrival cases before commitment. Ask for available routes and their costs, then observe a chosen attempt. | Record predicted feasibility separately from preference and success. Include feasible, infeasible and exact-boundary cases where the rule permits them; “always decline” is not proof of understanding. |
| Does the exit preserve the intended promise? | Trace refusal, retreat, interrupted play and return under the same rule set. | Check cost/closure predictions, recovery from interruption and evidence of accidental dead ends. A successful ending does not prove all other supported exits work. |
| Is a density claim really about density? | Specify the counting unit and compare matched content with changed spacing; record time spent traveling, searching and reading. | Distinguish exposure from encounter count, and load from preference. Do not attribute a change to density if reward, task mix and navigational demand also changed. |

Relevant participants would include the intended audience with varied familiarity, reading and access needs; requirements depend on the local study and cannot be reduced to a universal sample size. Counterbalance or separate conditions where learning, fatigue and spoilers would contaminate comparison. Under the inspected F01/W02 corrections, **transfer** retains the underlying rule while changing surface presentation; changed-rule probes are **adaptation/discrimination**, reported separately. No statistically nonsignificant difference would establish equivalence by itself.

## Claim ledger

| ID | Precise claim and class | Support / locator | Applicability, confidence and unresolved question |
|---|---|---|---|
| C-01 | Encounter/scenario and scope distinctions are working definitions. `inference` | Taxonomy assigned heading; W04 framing. | Moderate as useful organization, not an approved universal vocabulary. Does retrieval need a narrower alias? |
| C-02 | A composition promise must be qualified by reachable histories; exposure is not comprehension. `inference` | Reviewed W01/W02 distinctions; logical precondition analysis. | High for the dependency logic, not for an experience effect. Which arrival differences actually matter? |
| C-03 | Escalation and density should be described by their changing demands and exposure units, rather than one unexplained count. `inference` | W04 measurement reasoning; reviewed F07 evaluation distinction. | Moderate; proposed decomposition not psychometrically validated. What explains observed load? |
| C-04 | Booth documents a pressure-transition process and remaining-threat exceptions. `practitioner-heuristic` | W04-001, PDF pp. 78–82. | High for the documented account; low for transfer to other experiences. No universal timing or causal effect claimed. |
| C-05 | Qualifying relief by residual pressure may make a specified recovery activity more usable. `hypothesis` | C-02/C-04 provide the bridge; PAT-01 develops the proposal. | Low for benefit; may introduce waiting or unwanted predictability. Compare simpler lower-pressure design. |
| C-06 | Spector reports explicitly authored alternatives when hoped-for systemic solutions were insufficient. `practitioner-heuristic` | W04-004, TECHNOLOGY IMPOSES LIMITS. | High for the report; not an efficacy comparison or mandate for all methods. |
| C-07 | Alternate routes must be checked against their own prerequisites; costly refusal can be intentional. `inference` | Reviewed W02 objective distinction; W01-09, Isle of Cats creator discussion, supplies a contrary case. | Moderate, contextual. Is route equivalence actually part of the local promise? |
| C-08 | Supported refusal, retreat, retry, ending and session interruption are distinct; consequences need not all be erased. `inference` | W04 definitions; inspected F07 safe-exit pattern, purpose/recipe. | High for distinguishing outcomes, moderate for any chosen safeguard. What costs are understood and defensible? |
| C-09 | A bounded state/exit audit may reveal unsupported paths, but does not prove appeal or reduce total cost. `hypothesis` | C-02/C-06; reviewed W02 and F07 limits. | Low for workflow benefit; static audit can miss real interaction failures. |
| C-10 | Access, locale meaning and production obligations should be reviewed with the complete scenario. `hypothesis` | W04 safeguard proposal; reviewed F07 ethics constraints; P01 scope correction retained. | Low for measured effect; no locale or access population studied here. |
| C-11 | Proposed comparisons must separate prediction, preference, execution and changed-rule adaptation. `inference` | Inspected F01/W02 corrected patterns and F07 evaluation methods. | High for avoiding those specified inference errors; test validity still requires local review. |
| C-12 | The storm-relay scenario is an illustration of the proposed method, not evidence of effectiveness. `hypothesis` | Invented in W04; no outside source or actual result. | Low; values, consequences and acceptance rules require local design approval. |

Source abbreviations in this ledger retain the full namespace: W04-001 is `GDR-SRC-20261010-W04-001`, and so forth; W01-09 is `GDR-SRC-20261010-W01-09`. Claim IDs are entry-local.

## Open questions and change history

Coverage is **open**. Escalation, contrast, alternatives, exits, recovery and revisits have been synthesized at conceptual level. Resource-pressure tuning, spatial reachability, comparative recovery effects, multiplayer disagreements about relief, and cross-cultural interpretation remain unresolved. Current F03/W03 material has not been transferred. No source inspection in W04 establishes an optimal density or universal nonviolent-resolution rule.

The next discriminating question is whether state qualification improves the particular activity intended during recovery compared with a cheaper fixed or player-controlled alternative. The parent should first independently review that recommendation and its overlap with existing patterns. Additional evidence-preservation/exit work is queued in the packet, not silently treated as complete.

**History:** `0.1.0`, `initial-draft-1`, initial W04 submission; predecessor and supersession are null. Author self-review is recorded in the packet; independent W04 review has not occurred. No release gate is passed by this file’s existence.

## Reviewed inputs and transfer limits

Inspected W01 narrative/character/worldbuilding distinctions, W01 consequence-preserving reconvergence, W02 objectives and the selected corrected multi-route pattern, F07 evaluation/ethics and safe-exit scope, plus the corrected F01 transfer example. P01’s correction receipt was inspected only to preserve scope boundaries; no numerical accessibility prescription was transferred. The selected input is the parent-reviewed, unreleased waves 1–2 candidate archive, locally fingerprinted SHA-256 `4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931`. Relevant bytes, rather than remembered earlier drafts, were inspected. Exact dependency paths, selected revisions, byte hashes and inspected line ranges are recorded in the [review packet](../reviews/full-run-20261010-w04-review-packet.md#reviewed-dependency-provenance). These are prior candidate syntheses, not independent empirical validation of W04. Their cited outside studies are not reasserted unless the original source is separately listed in this entry.

The mounted starter instructions, evidence rules, gates, index, taxonomy and templates are the historical `0.1.0 candidate` input. The current dispatch authorizes W04 research but not conclusions, permanent IDs or release. The current canonical index, pending global allocations and central recovery ledger were not available. Current W03 spatial/exploration and F03 progression/resource drafts remain unavailable author-running dependencies; no guidance is inferred from them. There is no genre-specific draft in this packet; genre adaptation remains with the relevant owner, and no game label is inferred from an example.

## References

### GDR-SRC-20261010-W04-001 — The AI Systems of Left 4 Dead

**Author/organization:** Michael Booth / Valve. **Publication/update:** 2009; AIIDE presentation. **Publisher:** Valve; AIIDE, Stanford. **Verified access route:** [The AI Systems of Left 4 Dead](https://steamcdn-a.akamaihd.net/apps/valve/2009/ai_systems_of_l4d_mike_booth.pdf). **Edition/build:** 95-page presentation; historical Left 4 Dead production account; no game build inspected. **Accessed:** 2026-10-10 (America/Los_Angeles research date). **Access:** `relevant-excerpt`. **Type:** Firsthand development presentation. **Locator:** PDF pp. 78–82, especially p. 81 state diagram and p. 82 exceptions; p. 85 population diagram inspected only as a creator illustration. **Claims in this entry:** C-04; bridge for C-05. **Rights:** Copyright Valve/author; paraphrase only; slides not redistributed. **Limits/relationships:** No participant methods or controlled effect estimate in the inspected pages. Intensity is a designed proxy, not measured emotion. Same author/game as W01-13, but a different presentation, not independent replication..

### GDR-SRC-20261010-W04-004 — Postmortem: Ion Storm’s Deus Ex

**Author/organization:** Warren Spector; embedded 1998 design addenda by Harvey Smith. **Publication/update:** 2000-12-06. **Publisher:** Game Developer / originally Gamasutra. **Verified access route:** [Postmortem: Ion Storm’s Deus Ex](https://www.gamedeveloper.com/design/postmortem-ion-storm-s-i-deus-ex-i-). **Edition/build:** Historical postmortem with reproduced 1997/1998 design intentions; not a current game audit. **Accessed:** 2026-10-10 (America/Los_Angeles research date). **Access:** `relevant-excerpt`. **Type:** Firsthand development postmortem. **Locator:** What Went Right, item 1: The Rules of Role-Playing and The DEUS EX Rules Amendments & Addenda; item 3: TECHNOLOGY IMPOSES LIMITS, paragraphs on planned skill/action/character-interaction paths. **Claims in this entry:** C-06; bridge for C-07/C-09. **Rights:** Copyright author/publisher; paraphrase only. **Limits/relationships:** Distinguish the reproduced ambitions from retrospective production claims. The multiple-solutions position is project-specific, not a universal rule or measured benefit. No sales or award claim is used as evidence..

### GDR-SRC-20261010-W01-09 — Forget Protagonists: Writing NPCs with Agency for 80 Days and Beyond

**Author/organization:** Meg (Meghna) Jayanth. **Publication/update:** 2016-06-05; transcript of a GDC 2016 talk. **Publisher:** Author’s Medium publication. **Verified access route:** [Forget Protagonists: Writing NPCs with Agency for 80 Days and Beyond](https://medium.com/@betterthemask/forget-protagonists-writing-npcs-with-agency-for-80-days-and-beyond-703201a2309). **Edition/build:** Author-published talk transcript; creator account, not game execution. **Accessed:** 2026-10-10 (America/Los_Angeles research date). **Access:** `relevant-excerpt`. **Type:** Firsthand narrative-design account and practitioner argument. **Locator:** Author’s discussion of Sunless Sea / Isle of Cats / Zaira and the cost of refusal; 80 Days section on differing Artificers’ Guild perspectives. **Claims in this entry:** C-07; contrary case constraining C-08. **Rights:** Copyright author; short paraphrases only. **Limits/relationships:** Creator’s intent and examples do not establish player effects. Her commentary about other studios’ games is not treated as firsthand intent evidence. Same work as W01-09; identity reused..


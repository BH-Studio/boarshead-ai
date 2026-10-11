---
id: GDR-CAND-20261010-F01-TOP-02
kind: topic
title: Core loops and interaction structure
version: 0.1.0
status: draft
id_scope: run-scoped-temporary
run_id: GDR-FULL-20261010
batch_id: F01
owner_project: BH-GDR-Foundations-and-Systems
updated: '2026-10-10'
evidence_checked: '2026-10-10'
input_snapshot: Available GD-Knowledge starter candidate; INDEX/REGISTERS 0.1.0, nine
  Project files; not a current canonical receipt
aliases:
- core gameplay loop
- interaction horizons
- verbs and rules
- feedback loops
- systemic emergence
- session loop
tags:
- rules
- verbs
- goals
- feedback
- horizons
- emergence
- incentives
- interruption
related_topics:
- GDR-CAND-20261010-F01-TOP-01
- GDR-CAND-20261010-F01-TOP-03
related_patterns:
- GDR-CAND-20261010-F01-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-F01-04
- GDR-SRC-20261010-F01-06
- GDR-SRC-20261010-F01-07
- GDR-SRC-20261010-F01-08
- GDR-SRC-20261010-F01-09
- GDR-SRC-20261010-F01-14
reviewer: null
approved_by: null
approved_date: null
---

# Core loops and interaction structure

**Draft research candidate — not released guidance.** Identity `GDR-CAND-20261010-F01-TOP-02` is temporary for `GDR-FULL-20261010/F01`. This file authorizes no implementation or adoption. Review and approval fields are intentionally null.

## Decision and scope

**Decision:** How should a game's actions, rules, goals and consequences connect so that repeated or extended participation supports its intended experience—and when is a repeating loop the wrong organizing model?

This entry helps describe interaction structure, identify missing causal connections, compare short and extended consequences, and expose incentive conflicts. It does not define reward schedules, tune an economy, prescribe a session length, implement an engine update loop, or promise retention. It covers single-player, shared and player-authored activity without making any genre the default.

**Working vocabulary.** A *verb* is an action description at the level relevant to the decision, such as inspect, redirect, commit or wait. A *mechanic* specifies an action's relationship with game state. A *rule* constrains permitted actions or their consequences. A *goal* supplies a criterion a player or system may pursue; it need not be a mandatory win condition. A *core interaction loop* is a recurring, player-relevant sequence in which consequences change the conditions of subsequent action. These are analytical definitions adapted from conceptual literature, not a mandatory ontology. [C-01; GDR-SRC-20261010-F01-07]

A runtime frame-update loop and a player's recurring decision process are different descriptions. This research specifies meanings and relationships, not threads, components, classes or engine APIs. [C-01]

## Core explanation and mechanisms

### A loop needs a consequential relationship, not merely a circle of labels

MDA distinguishes mechanics from the dynamics of their operation and the qualities players experience. A list such as “act → earn → upgrade → repeat” omits the question that matters: **what changes in the next decision, and why would that change serve the intended experience?** [C-02; GDR-SRC-20261010-F01-06]

For analysis, specify an initial state, an intention, relevant information, an available action, a state transition, feedback about that transition and the resulting next situation. A sequence can recur without being identical. Knowledge, positioning, relationships or chosen interpretation may change even when no currency increases. This state-and-decision description is a proposed diagnostic representation, not a universal formula for fun. [C-01; C-07]

Consider the failure of an apparent loop: the player repeats a solved input, receives a larger number, and faces the identical decision again. That structure is not automatically bad. It might fit an endorsed repetitive activity. However, it cannot by itself substantiate a claim of growing strategic depth or mastery. The team must state which experience it intends and test that claim separately. [C-07; C-09]

### Feedback has informational and system-dynamic meanings

Informational feedback helps a player infer what happened. A system feedback loop changes the conditions that generate future outcomes. A pleasant sound is not automatically a reinforcing feedback loop; a resource multiplier can be reinforcing even when its presentation is unpleasant. [C-03]

In the restricted dynamic sense used here, **reinforcing feedback** amplifies a change through subsequent interactions, while **balancing feedback** counteracts a deviation relative to a specified condition. Neither term is a moral judgment. Their effects depend on delays, limits, initial conditions and the behavior of participants. The terminology is grounded in MDA's dynamic models and Dormans's resource/state models; applying it to an entire player's experience would overextend the model. [C-03; GDR-SRC-20261010-F01-06; GDR-SRC-20261010-F01-08]

The evidence-to-application bridge is structural: if a reward increases the capacity to obtain the same reward, a designer has a reason to inspect compounding, lockout and saturation. That does not establish that compounding is undesirable. It could express growing power; suppressing it could invalidate a desired payoff. State the purpose before adding a balancing mechanism. [C-03; C-07]

### Short, session and long horizons are inspection windows, not required layers

Use **short horizon** for the immediate consequence an action helps resolve; **session horizon** for an activity that can feel coherent around a stopping point; and **long horizon** for consequences carried into future participation. These are relative functional labels, not durations. A particular game may collapse them, omit persistent progression, or deliberately provide no repeating activity. [C-04]

Ask what persists at each boundary: game state, learned knowledge, an unresolved intention, a social promise, or nothing. Carrying state forward can create commitment, but it can also make leaving costly. Removing persistence can enable experimentation, while also removing a player's valued investment. The useful design choice is what the player should carry and why, not how to ensure an obligatory three-layer loop. [C-04; C-10]

The proposed horizon audit distinguishes a **good place to stop** from an artificial countdown demanding a return. A return reminder may reconstruct a prior intention without imposing a new obligation. Objective/history guidance in XAG 109 motivates checking this accessibility need, but it does not validate a particular session structure or retention effect. [C-10; GDR-SRC-20261010-F01-14]

### Emergence is an interaction property; its value still needs interpretation

Dormans demonstrates a modeling approach with artificial players in hypothetical SimWar. Its resource-flow abstraction omits tactical movement and level design, and the author explicitly warns against treating model adjustments as a perfectly balanced implemented game. F01 inspected the paper, not a running model. [C-05; GDR-SRC-20261010-F01-08]

This supports an inference that explicit dependencies can expose structural possibilities before detailed implementation. It does **not** show that any interaction discovered by a model is legible, enjoyable, ethical or production-feasible. A system can permit many combinations while players discover only one, or while one exploit makes every other action unattractive. [C-05; C-07]

Sicart's critique supplies a different limit: an account of rules is not an exhaustive account of a player's meaning-making. A self-imposed restriction, cooperative convention or playful appropriation can matter even when it is absent from the designer's intended reward path. Therefore, model the rules, then separately investigate what players attempt and interpret. This is a methodological inference, not a claim that all meanings are equally supported by any rules. [C-06; GDR-SRC-20261010-F01-09]

## Design choices and alternatives

| Structure | When it may fit | Tradeoff, counterexample and alternative |
|---|---|---|
| Repeat a stable decision with varied conditions | Intended experience is refinement, anticipation or expressive variation. [C-07; C-09] | Repetition may be solved busywork. Vary consequences or omit extra repetitions rather than disguising them with rewards. |
| Carry resources, commitments or knowledge across sessions | Longer consequences serve planning, investment or continuity. [C-04; C-10] | Re-entry burden and commitment costs rise. A reset, optional recap or shorter self-contained activity may fit better. |
| Let players choose the next activity | Several endorsed purposes can use the same rules. [C-06; C-12] | Choice adds explanation and validation cases; empty choice can obscure a linear activity that would work better. |
| Author a sequence rather than a loop | A finite transformation or unfolding experience is the main aim. [C-12] | Less replay structure is not necessarily a defect. Do not bolt on resource farming solely to make a diagram circular. |
| Combine general rules instead of scripting each solution | Predictable interactions plausibly support experimentation. [C-05; C-07] | State combinations create debugging and explanation costs. A deliberately constrained authored solution may be more coherent. |
| Add balancing feedback | Runaway amplification contradicts the intended contest or access to participation. [C-03] | Automatic equalization may erase valued achievement or invite strategic underperformance. Caps, alternative objectives or no intervention are distinct alternatives. |

No row is a genre rule or an approval to implement. Each is a hypothesis or analytic option with conditions.

## Application process

1. **Name the player-facing decision.** Identify an intention and the action that could advance it. Separate merely traversing an interface from the intended decision, unless interface operation is itself part of the chosen skill. [C-01; C-07]
2. **Record the transition.** For each essential action, document prerequisite state, resource/information cost, possible outcomes, uncertainty, what the player can learn, reversibility and who else is affected. Do not prescribe a software schema. [C-07; C-13]
3. **Trace the next decision.** Explain exactly how the outcome changes available options, priorities, knowledge or expressive possibilities. An arrow without a change is not evidence of a useful loop. [C-07]
4. **Inspect horizons and exits.** Mark what persists through completion, interruption, absence and return. Distinguish intentional stakes from incidental loss caused by inability to stop. Record the intended exception for a willingly committed shared event. [C-04; C-10; C-11]
5. **Challenge incentives before polishing.** Try refusing the activity, delaying indefinitely, repeating the cheapest action, hoarding, delegating, disconnecting and pursuing a different goal. Identify loops that cannot start, cannot terminate or reward undermining the intended experience. These are proposed reasoning/prototype cases, not tests performed in F01. [C-07; C-08; C-14]
6. **Compare less elaborate structures.** Check whether a direct action, authored sequence or fewer persistent variables preserves the purpose with less explanation and maintenance. [C-12; C-13]
7. **Prototype and evaluate only under a later implementation/test authorization.** Test consequences and interpretation separately. A state trace can validate a modeled transition; only observation can tell whether a player recognizes it, and a further inquiry is needed to understand whether it is valued. [C-05; C-06; C-14]

## Patterns and genre adaptations

[Supported attempt and transfer check](../patterns/supported-attempt-and-transfer-check.md), `GDR-CAND-20261010-F01-PAT-01`, can help investigate whether players understand a specific repeatable rule. It is not a universal core-loop recipe and is inappropriate when the intended activity would be spoiled by explicit practice.

[Player experience and motivation](player-experience-and-motivation.md) owns the purpose against which this structure is judged. [Learning and onboarding](learning-and-onboarding.md) owns how its rules become learnable.

Economies/resources, progression/rewards, difficulty, session structure/retention and evaluation are **unavailable dependency topics**, not silently completed by this entry. Worlds owns spatial and narrative orchestration; Presentation owns perceptible feedback and interaction details. Genre files and `templates/genre.md` are unavailable; no genre adaptations are adopted. Labels such as competitive, cooperative, persistent or short-session describe conditional contexts, not new genre entries.

## Examples and counterexamples

### Illustrative worked example: a delivery-and-repair activity

A player can inspect a damaged route, carry a parcel, repair a route or choose another delivery. A route's condition affects the risk of damage; repair consumes material that could also protect a parcel. Successful delivery frees capacity and changes which destination matters next. The intended decision is whether to invest in a route or protect the current load. These invented rules are local example assumptions, not recommendations for delivery games. [C-15]

**Short horizon:** resolve a crossing and observe whether protection or repair affected the outcome. **Session horizon:** fulfill a chosen delivery commitment or return safely with the parcel. **Long horizon, optional:** retain the route repair and a record of unresolved deliveries. The same design could reset routes after each activity; persistence is a variable to compare, not a required progression layer. [C-04; C-15]

An invalid feedback design announces success without making clear whether the route, protection, chance or a partner's action caused it. An invalid incentive design pays more for repeatedly accepting and canceling a job than for completing it. A structural dead end consumes all repair material on an impassable route with no alternative. Proposed corrections include showing relevant causal information, changing cancellation consequences, or retaining a recoverable route—but each correction must be checked against intended uncertainty, legitimate cancellation and chosen stakes. [C-07; C-10; C-13; C-15]

### Illustrative calculation: a dominated action under explicit assumptions

Suppose actions A and B have identical time, risk, prerequisites and downstream effects; each costs 2 stock. A returns 4 stock and B returns 5. Suppose also that maximizing stock is the only goal and neither action is limited. A changes stock by +2 and B by +3, so B strictly dominates A in this deliberately restricted model. This is arithmetic reasoning, not a simulation result. [C-08]

The conclusion changes if A has a desired expressive result, lower input burden, another resource output, different timing or a commitment benefit. Those variables cannot be ignored and then “discovered” as player irrationality. An action can be numerically dominated in one objective while serving another endorsed purpose. Conversely, decorative flavor does not establish that players actually value the weaker alternative. [C-08; C-09]

### Illustrative emergence example: an unintended but understandable route

A system permits water to redirect a floating object and objects to hold pressure switches. Combining the rules could let a player use a redirected object to keep a route open. This is systemic interaction if the outcome follows from the general rules rather than a special-case solution. Its usefulness remains a hypothesis: the object might be hard to track, another player might remove it, or the combination might bypass a dependency that the rest of the game assumes. [C-07; C-13; C-15]

The proposed process is to identify prerequisites and termination states, check whether the player can explain the result, and test both intentional use and malicious obstruction. A narrower scripted interaction is a legitimate alternative when compositional rules create more incomprehensible exceptions than meaningful possibilities. [C-12; C-14]

### Source case and strongest counterexample

The SimWar paper is a **source-reported modeling case**, not a shipped-game observation. Its omission of tactical and spatial factors is a concrete limit on economy-only analysis. [C-05; GDR-SRC-20261010-F01-08]

A finite contemplative interaction with no reward cycle is an **illustrative counterexample** to requiring every game to have nested earning/upgrading loops. The appropriate inquiry is whether its sequence supports its intended experience, not whether a persistent resource can be added. Likewise, a group may intentionally ignore the designer's scoring rule. A model that only asks how to maximize the score will miss that purpose. [C-06; C-12; C-15]

## Failure modes and constraints

**Exploitability and edge states:** inspect empty resources, full inventories, simultaneous commitments, invalidated prerequisites, cancellation after reward, repeated low-cost gains and shared-state changes during absence. A legitimate recovery route and an abuse route may use the same mechanic; distinguish intended rights from behavior merely inconvenient to the model. These are proposed audit cases, not discovered bugs. [C-07; C-11; C-13]

**Accessibility and localization:** players must be able to infer relevant state changes without being forced through one sensory or motor route. Vocabulary such as “finish,” “bank,” “reset” and “commit” must describe the actual persistence rule in the selected language. A diagram understandable to the designer is not evidence that the player has that information. Presentation determines the modalities and controls; this topic specifies the facts that must be available. [C-13]

**Ethics and social costs:** a longer session is not necessarily a better session. The loop may retain someone through obligation or deferred access to what they actually value. Source evidence motivates investigating this possibility; it does not imply all long goals are coercive. [C-10; GDR-SRC-20261010-F01-04]

**Production:** more interacting state variables create more situations to explain and validate. No combinatorial count or staffing estimate is supplied without a concrete model. Start with the smallest causal representation needed for the decision and retain a list of omitted spatial, sensory and social factors. [C-05; C-13]

## Playtest and validation

**Proposed, not performed.** No model was executed, no prototype built and no participants observed.

For a candidate loop, ask whether the intended action–consequence relationship changes a later decision in a way players understand and value. Compare the proposed structure with a simpler sequence, a reduced-persistence version or a version that exposes causal information. Select the comparison according to the uncertainty, rather than changing all variables at once. [C-14]

First, specify expected states for ordinary, edge and exploit attempts. Later, under test authorization, inspect whether those transitions actually occur. Separately ask players to predict a consequence and explain their next choice. Observe choice diversity only alongside knowledge of the situation and goals: many actions can mean exploration, confusion or indifferent clicking. Do not label every unusual solution an exploit. [C-07; C-14]

Include novice and experienced rule users, relevant access needs, and solo/shared contexts actually in scope. Control or record content novelty, prior knowledge, reward amount, social familiarity, available time and order effects. Record incomplete sessions rather than analyzing only completers. A horizon comparison must include the costs of interruption and return; an uninterrupted laboratory session cannot establish those effects. [C-10; C-14]

**Reject or revise** when no decision changes after the supposed loop closes; when repeated actions maximize an irrelevant reward at the expense of the intended purpose; when players cannot distinguish the relevant causal alternatives; when persistent state makes re-entry disproportionately burdensome; or when the simplified alternative supports the intended experience without the additional costs. The team must predeclare local acceptance criteria and uncertainty treatment before collecting evidence. No universal repetition count or retention target is proposed. [C-14]

## Claim ledger

Claim IDs are local to this entry. A reference attached to a hypothesis identifies its rationale, not proof of the proposed intervention. `None — original analysis` means no external experiment is claimed. Confidence applies to the exact scoped wording, not to universal effectiveness.

| Claim | Precise claim | Class | Evidence and contrary support / locators | Applicability and confidence | Unresolved question |
|---|---|---|---|---|---|
| C-01 | Verbs, mechanics, rules, goals and recurring player decisions are distinct analytical descriptions; a gameplay loop is not an engine update loop. | inference | GDR-SRC-20261010-F01-07, definition and rules/game-loop paragraphs; local terminology explicitly stated. | Moderate as a useful distinction, not a universal ontology. | Which granularity answers the design question? |
| C-02 | MDA supplies a conceptual distinction between mechanics, dynamics and experienced qualities rather than an efficacy guarantee. | practitioner-heuristic | GDR-SRC-20261010-F01-06, PDF pp. 1–3; practitioner workshop framework. | Moderate for description of the framework; no controlled benefit estimate. | Does this representation reveal the relevant design issue? |
| C-03 | Reinforcing and balancing system feedback describe conditional state relationships, not positive and negative feelings. | inference | GDR-SRC-20261010-F01-06, Dynamic Models; GDR-SRC-20261010-F01-08, resource/state connections and production model. | Moderate structural rationale; effects depend on model boundaries and delays. | Which variables and constraints determine the actual dynamics? |
| C-04 | Short/session/long horizons are optional functional inspection windows, not a required three-layer structure or time scale. | hypothesis | None — original decomposition, informed by GDR-SRC-20261010-F01-06’s separation of mechanics and experience. | Low for improving design outcomes; no duration prescribed. | Would fewer horizons or a non-repeating sequence suffice? |
| C-05 | SimWar illustrates structural modeling while explicitly omitting factors needed to infer implemented balance or player experience. | practitioner-heuristic | GDR-SRC-20261010-F01-08, pp. 5–7, Modeling/Simulating SimWar and Discussion. | Moderate for the published modeling account; artificial players, no F01 reproduction. | Which omitted spatial, tactical and human factors reverse a prediction? |
| C-06 | Actual play and interpretation need inquiry beyond a rule-centered model. | inference | GDR-SRC-20261010-F01-09, concluding critique and qualification retaining procedural analysis. | Moderate methodological caution, theoretical rather than causal evidence. | What purposes do players pursue beyond the scored objective? |
| C-07 | State-transition and incentive audits may reveal dead ends, weak causal links and dominant behaviors before polishing a loop. | hypothesis | GDR-SRC-20261010-F01-08 modeling method; GDR-SRC-20261010-F01-06 dynamics; original audit process. | Low for practical benefit; depends on completeness of the representation. | Do the identified cases matter in actual play? |
| C-08 | In the specified toy model, B’s +3 stock dominates A’s +2 only under identical other consequences and a sole stock-maximizing goal. | inference | None — explicit assumptions and arithmetic in illustrative calculation. | High for that calculation, no general claim about player preference. | What relevant value or constraint did the model omit? |
| C-09 | Repeated input, rising statistics and growing player capability are not equivalent outcomes. | inference | GDR-SRC-20261010-F01-07 mechanics versus goals; GDR-SRC-20261010-F01-06 dynamics versus aesthetics; original measurement decomposition. | Moderate conceptual distinction; not a finding that repetition is undesirable. | Which kind of change is actually intended? |
| C-10 | Persistence and re-entry should be evaluated against chosen purpose and stopping costs, not continuation alone. | hypothesis | GDR-SRC-20261010-F01-04 persistence accounts; GDR-SRC-20261010-F01-14 objective/recap guidance; no direct horizon intervention study. | Low for any specific design benefit; accessibility and engagement are separate outcomes. | When is commitment endorsed, and when is it unwanted? |
| C-11 | Shared-state handoffs and exits can change others’ costs and incentives; these need explicit cases. | inference | None — original multi-agent consequence analysis; GDR-SRC-20261010-F01-04 motivates inquiry but does not test the cases. | Moderate logical possibility; frequency/severity unknown. | Can legitimate exit be separated from intentional disruption? |
| C-12 | Authored sequences, fewer choices and limited systemic combinations are legitimate alternatives when they better fit the stated purpose. | inference | GDR-SRC-20261010-F01-06 plural experiences; GDR-SRC-20261010-F01-09 player interpretation; no comparative efficacy trial. | Moderate as alternatives, low for superiority in a particular game. | Does added recurrence or generality contribute enough value? |
| C-13 | Omitted state, access, localization and interaction factors limit model-based recommendations and create validation work. | inference | GDR-SRC-20261010-F01-08 Discussion; GDR-SRC-20261010-F01-14 objective clarity; original dependency and production analysis. | Moderate for limits, no measured cost estimate. | Which omitted factors are consequential in the target context? |
| C-14 | The proposed validation separates modeled transitions, comprehension, player purpose and experience; none of these tests has run. | hypothesis | GDR-SRC-20261010-F01-08 modeling limits; GDR-SRC-20261010-F01-09 interpretation; original comparisons and rejection criteria. | Low for intervention benefit; design protocol only. | Does the causal representation predict behavior without obscuring value? |
| C-15 | Delivery, stock and water-switch examples are invented analytical cases, not observations of commercial games or test results. | hypothesis | None — original worked examples; source-linked mechanisms are identified separately. | Low for empirical applicability. | Which assumptions fail when the examples are adapted? |

## References

PDF locators distinguish printed page numbers from file-page counts where they differ. No cited full paper, figure, participant quotation, or questionnaire is redistributed.

### GDR-SRC-20261010-F01-04 — “I Just Wanted to Get It Over and Done With”: A Grounded Theory of Psychological Need Frustration in Video Games

**Citation:** Nick Ballou and Sebastian Deterding. 2023-11; accepted 2023-07-07. *“I Just Wanted to Get It Over and Done With”: A Grounded Theory of Psychological Need Frustration in Video Games*. ACM, Proceedings of the ACM on Human-Computer Interaction 7, CHI PLAY, article 382, 20 pages.

**Verified access route:** [“I Just Wanted to Get It Over and Done With”: A Grounded Theory of Psychological Need Frustration in Video Games](https://selfdeterminationtheory.org/wp-content/uploads/2024/01/2023_BallouDeterding_IJustWanted.pdf). DOI: `10.1145/3611028`.

**Version and access:** Published 2023 article PDF. Accessed 2026-10-10; `access: relevant-excerpt`. Original qualitative interview/grounded-theory study.

**Inspected locators:** pp. 382:4–7 Method/model summary; pp. 382:12–13 persistence and extrinsic motives; pp. 382:16–17 §4.5 Limitations. Figure 1 is not used as a causal estimate.

**Claims supported here:** C-10, C-11.

**Limits:** 12 purposively sampled adults aged 18–42; retrospective accounts; all but two from Global North. No population prevalence, causal effect size, or validated predictor claimed.

**Independence/deduplication:** New interviews, but SDT-informed and cites GDR-SRC-20261010-F01-01/GDR-SRC-20261010-F01-03; conceptual rather than independent-theory triangulation. Cross-batch DOI/URL/edition matching and global source allocation are pending Library Coordination.

**Rights:** ACM publication permission notice; paraphrase only, no participant quotations reproduced.

### GDR-SRC-20261010-F01-06 — MDA: A Formal Approach to Game Design and Game Research

**Citation:** Robin Hunicke, Marc LeBlanc, and Robert Zubek. 2004. *MDA: A Formal Approach to Game Design and Game Research*. AAAI Workshop on Challenges in Game AI; author-hosted workshop paper.

**Verified access route:** [MDA: A Formal Approach to Game Design and Game Research](https://www.cs.northwestern.edu/~hunicke/MDA.pdf). DOI: not recorded; use the verified URL.

**Version and access:** Five-page 2004 workshop paper. Accessed 2026-10-10; `access: relevant-excerpt`. Practitioner-authored conceptual design framework, not a formal standard or controlled study.

**Inspected locators:** PDF pp. 1–3: designer/player perspectives, Aesthetics, Aesthetic Models, Dynamic Models, Mechanics; p. 3 feedback diagrams visually inspected.

**Claims supported here:** C-02, C-03, C-04, C-07, C-09, C-12.

**Limits:** Vocabulary and examples do not establish universal categories or causal efficacy. This batch did not independently play the example games.

**Independence/deduplication:** Framework reused in GDR-SRC-20261010-F01-08 and discussed in GDR-SRC-20261010-F01-07; these are not independent demonstrations that MDA improves design. Cross-batch DOI/URL/edition matching and global source allocation are pending Library Coordination.

**Rights:** Workshop paper; no open redistribution license established; paraphrase and link only.

### GDR-SRC-20261010-F01-07 — Defining Game Mechanics

**Citation:** Miguel Sicart. 2008-12. *Defining Game Mechanics*. Game Studies 8(2).

**Verified access route:** [Defining Game Mechanics](https://gamestudies.org/0802/articles/sicart). DOI: not recorded; use the verified URL.

**Version and access:** 2008 journal HTML article. Accessed 2026-10-10; `access: relevant-excerpt`. Original conceptual/analytical paper.

**Inspected locators:** Definition paragraph beginning “I define game mechanics”; paragraphs distinguishing mechanics, rules and the game loop; paragraphs on context mechanics and goals.

**Claims supported here:** C-01, C-09.

**Limits:** A proposed definition, not a normative standard, engine architecture mandate, or empirical proof. Author analyses of games are not fresh F01 observations.

**Independence/deduplication:** Engages prior design frameworks including MDA; same author as GDR-SRC-20261010-F01-09, not an independent voice. Cross-batch DOI/URL/edition matching and global source allocation are pending Library Coordination.

**Rights:** Game Studies article; open-web access, redistribution license not established; paraphrase only.

### GDR-SRC-20261010-F01-08 — Simulating Mechanics to Study Emergence in Games

**Citation:** Joris Dormans. 2011-10-09. *Simulating Mechanics to Study Emergence in Games*. AAAI, AIIDE 7(3), 2–7; technical report WS-11-19.

**Verified access route:** [Simulating Mechanics to Study Emergence in Games](https://ojs.aaai.org/index.php/AIIDE/article/download/12477/12336/16005). DOI: `10.1609/aiide.v7i3.12477`.

**Version and access:** Six-page published 2011 paper. Accessed 2026-10-10; `access: relevant-excerpt`. Original modeling method with reported exploratory artificial-player simulations.

**Inspected locators:** pp. 2–4 framework/resource and state connections; pp. 5–7 Modeling/Simulating SimWar and Discussion. PDF page 5 (printed p. 6) diagrams and artificial-player description visually inspected; no F01 numerical balance targets extracted.

**Claims supported here:** C-03, C-05, C-07, C-13, C-14.

**Limits:** SimWar is hypothetical; the model excludes tactical maneuvering and level design. No F01 simulation, player test, or balance replication performed.

**Independence/deduplication:** Explicitly builds on MDA and earlier Dormans work; Wright’s talk is a cited antecedent, not separately inspected. Cross-batch DOI/URL/edition matching and global source allocation are pending Library Coordination.

**Rights:** Copyright AAAI 2011; paraphrase and attribution only.

### GDR-SRC-20261010-F01-09 — Against Procedurality

**Citation:** Miguel Sicart. 2011-12. *Against Procedurality*. Game Studies 11(3).

**Verified access route:** [Against Procedurality](https://gamestudies.org/1103/articles/sicart_ap). DOI: not recorded; use the verified URL.

**Version and access:** 2011 journal HTML article. Accessed 2026-10-10; `access: relevant-excerpt`. Original theoretical/critical argument.

**Inspected locators:** Opening critique of procedural rhetoric; concluding paragraphs from “The main argument of the critique” through “Against proceduralism is a player who wants to play.”

**Claims supported here:** C-06, C-12, C-14.

**Limits:** An argument about play/interpretation, not a controlled study of reception or a proof that rule analysis is useless.

**Independence/deduplication:** Same author as GDR-SRC-20261010-F01-07; authors/theories criticized in the article were not all independently inspected. Cross-batch DOI/URL/edition matching and global source allocation are pending Library Coordination.

**Rights:** Game Studies article; redistribution license not established; paraphrase only.

### GDR-SRC-20261010-F01-14 — Xbox Accessibility Guidelines: XAG 109 Objective clarity, with framework overview

**Citation:** Microsoft. XAG 109 last updated 2026-03-04; overview last updated 2026-08-14; framework v3.2 dated 2023-06-08. *Xbox Accessibility Guidelines: XAG 109 Objective clarity, with framework overview*. Microsoft Learn.

**Verified access route:** [Xbox Accessibility Guidelines: XAG 109 Objective clarity, with framework overview](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/109). DOI: not recorded; use the verified URL.

**Component/access route:** [Framework overview and version history](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines).

**Version and access:** Live web documentation inspected 2026-10-10; overview labels framework v3.2; no immutable commit supplied. Accessed 2026-10-10; `access: full`. First-party accessibility best-practice guidance, not certification or legal requirements.

**Inspected locators:** XAG 109: Overview, Scoping questions, Implementation guidelines (objectives, reminders, interactive tutorials, revisiting tutorials); overview: Introduction and Version history, including non-compliance disclaimer.

**Claims supported here:** C-10, C-13.

**Limits:** Recommendations need game-specific interpretation and representative access review. Does not empirically establish improved retention or specify a universal re-entry protocol. F01 does not inspect the games shown as examples.

**Independence/deduplication:** Guideline and overview are one documentation family/source identity; not independent evidence. Cross-batch DOI/URL/edition matching and global source allocation are pending Library Coordination.

**Rights:** Microsoft documentation; paraphrase and link only; embedded third-party images not reused.

## Open questions and change history

Open questions: whether the proposed horizon/state audits improve real design decisions; effects of omitted spatial and social variables; how player-defined purposes change apparent incentives; and maintenance cost. F01-X-05 records the model-versus-interpretation boundary. No numerical loop duration, economy balance or actual exploit was established.

**2026-10-10 — 0.1.0 draft:** initial F01 candidate using the available starter topic/pattern templates and the current bounded authorization. Author self-review is documented in the [batch review packet](../reviews/full-run-20261010-f01-review-packet.md). Independent review has not occurred. No prior version is superseded, no canonical authority is claimed, and no release or game adoption is approved. Permanent identity, cross-batch source matching and dependency resolution await Library Coordination.

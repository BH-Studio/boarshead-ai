---
id: GDR-CAND-20261010-F03-PAT-01
kind: pattern
title: Guaranteed acquisition alongside random drops
version: 0.1.0
status: draft
candidate_revision: initial-research-1
run_id: GDR-FULL-20261010
batch_id: F03
generation_attempt: F03-attempt-01
owner_project: BH-GDR-Foundations-and-Systems
updated: '2026-10-10'
evidence_checked: '2026-10-10'
input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate plus explicit F03 dispatch and
  inspected first-wave reviewed-candidate archive
aliases:
- bad-luck protection
- assured reward route
- deterministic reward fallback
tags:
- rewards
- acquisition
- uncertainty
- progression
- resource-accounting
related_topics:
- GDR-CAND-20261010-F03-TOP-01
- GDR-CAND-20261010-F03-TOP-02
related_patterns:
- GDR-CAND-20261010-F03-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-F03-005
- GDR-SRC-20261010-F03-008
- GDR-SRC-20261010-F03-009
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial F03 bounded research draft; author self-review integrated
  before first submission.
hash_record: ../reviews/full-run-20261010-f03-integrity.md
coverage_status: bounded-research-with-open-gaps
---

# Guaranteed acquisition alongside random drops

**Draft, unvalidated pattern.** Its completion-count arithmetic is conditional; its claimed experience benefit is a hypothesis. Version 0.1.0, candidate revision initial-research-1. No implementation, simulation or player test was performed.

## Purpose

Give a player pursuing a defined target an understandable assured route while allowing an optional random reward to arrive earlier. Use this only when both access predictability and some surprise serve the intended experience. The pattern is not a universal reward schedule, a retention prescription, or a requirement to add randomness. [C-01]

The player-facing problem is not “insufficient daily engagement.” It is that a particular desired object or capability may remain unavailable through bad luck even after eligible effort, and that this uncertainty may be contrary to the intended promise. Some experiences instead value indefinite discovery or open-ended trade; they are countercases, not automatically defects. [C-01; C-06]

## Context and prerequisites

The design must identify the exact target; what counts as a qualifying completion; an accessible earning route; a durable progress balance or equivalent milestone record; all redemption prerequisites; and the treatment of duplicate rewards, interruption and updates. A resource used for both crafting and purchase needs an explicit opportunity-cost rule. “Guaranteed eventual access” is misleading when the guarantee excludes an indispensable ingredient or requires an unavailable mode. [C-03; C-05]

A usable fallback must remain understandable without mental probability calculations or rapid reading. Needed access accommodations and ordinary state information remain available, not earned or removed after apparent success. Any inability to specify or maintain these conditions is an exit condition: use a narrower promise or direct target selection instead. These are proposed design prerequisites, not an implementation or accessibility certification. [C-05; C-06]

## Mechanism and evidence

| Link in the proposed chain | Support | Limit |
|---|---|---|
| Qualifying activity grants a known minimum toward a target | An arrangement of guaranteed resource earnings and exchange is documented in Warframe PC 32.2.0 [C-02; GDR-SRC-20261010-F03-008] | A historical creator document establishes existence, not efficacy or all current rules |
| Durable accumulation reaches a fixed cost after a bounded count | Arithmetic under the conditions in C-03 | Fails when balances are lost/spent, the cost changes, a cap blocks earning or redemption remains unavailable |
| The player understands and can plan around that count | Proposed inference to test [C-04] | A progress display can be misunderstood as time remaining or hide other requirements |
| Planning plus optional surprise improves the desired experience | Hypothesis [C-01; C-04] | Predictability may reduce valued uncertainty or make a quota salient; direct choice may be better |
| The arrangement permits comfortable stopping and later return | Proposed fit condition, not an automatic result [C-06] | A known finite grind can still conflict with the person's preferences or availability |

The survey evidence used by the topic includes heterogeneous player reports; it does not test this combined recipe. Neither a widely used system nor a mathematically finite route validates the final causal links. [C-04; C-07]

## Recipe

1. **Name the acquisition promise.** Specify the target and whether the assurance concerns a blueprint, a component, a complete usable item or an entitlement. State what remains outside the promise. Establish why a direct grant or player-selected reward is insufficient before adding a second acquisition system. [C-01; C-05]
2. **Define the qualifying unit.** Choose a completed task, encounter outcome or other observable unit. Describe failure, assists, group contribution and interrupted completion without equating use of an access option with lack of effort. Document required modes and prerequisite access. [C-03; C-05]
3. **Provide a durable minimum.** Let `g` be a strictly positive minimum credit grant per qualifying completion and `C` the fixed target cost. Let `b` be the already settled, spendable balance dedicated or available to this target. With no intervening spending/loss, sufficient storage, continued eligibility and accessible redemption, the remaining bound is:

   `N = ceil(max(0, C − b) / g)`

   This is a bound on **qualifying completions**, not elapsed time, successful attempts, tolerable effort or acquisition of any omitted component. Variable activity duration and repeated failures can leave time unbounded. If `g = 0`, this formula supplies no finite guarantee. [C-03]
4. **Define the random route separately.** An earlier desired drop may end the target pursuit. Specify duplicate handling and whether a drop changes credit awards. Do not silently consume accumulated progress or reset unrelated goals when a random reward arrives. A duplicate conversion needs its own economy audit. [C-05]
5. **Expose shared-resource tradeoffs.** When credits can be spent elsewhere, show that the remaining count is conditional on not doing so; do not promise a protected bound. Alternatives include a voluntarily reserved target balance, direct milestone redemption, or a single selectable reward. Each reduces flexibility differently. Avoid imposing another currency without a reason. [C-03; C-05]
6. **State persistence and settlement.** Distinguish pending earnings, committed credits, redemption pending and owned target. Define cancellation and resumption. A repeated delivery acknowledgement must not describe a second earned unit, and a displayed pending balance must not be represented as durable progress. The runtime mechanism is a separate engineering decision. [C-05]
7. **Choose the communication and exit policy.** Present the requirement, remaining qualifying count and excluded prerequisites in an accessible form. Permit the player to stop or choose another goal without misrepresenting lost opportunity. Test a discreet, player-selected tracker against a conspicuous automatic counter. [C-04; C-06]
8. **Compare and remove when inappropriate.** Compare mixed acquisition with direct selection and deterministic-only earning. Abandon the mixed structure when the random layer adds no valued surprise, the fallback becomes unwanted repetition, the bound is misunderstood, or maintenance cannot preserve the stated conditions. [C-01; C-07]

### Adjustable variables and why they matter

| Variable | Design question | Failure to inspect |
|---|---|---|
| Target scope and prerequisites | Is the promise for one component or a usable whole? | A technically correct component bound presented as complete access |
| `C`, `g`, starting `b` | Which locally chosen completion burden is being proposed? | A finite but unacceptable acquisition cost; no universal values are recommended |
| Credit ownership / binding | Personal, shared or transferable? | Another participant can spend the supposedly assured progress |
| Random award eligibility / duplicates | What changes when the desired reward arrives early? | A duplicate or reset invalidates the fallback logic |
| Storage / expiry / update behavior | Can earned progress be lost, capped or repriced? | A moving target sold as a stable bound |
| Information prominence | Does the player want active tracking? | The counter becomes an intrusive quota |
| Assistance and interruption | Which outcomes qualify and persist? | Unequal access or confusion about partially completed tasks |

These are local variables, not empirically calibrated defaults. [C-03–C-06]

## Worked examples

### Illustrative complete example: a selected tool

An invented activity awards at least three durable credits on each qualifying completion. The desired tool costs 24 credits. The player already has five available credits, no other prerequisite remains, the price will not change for this commitment, storage permits accumulation, and the player spends none elsewhere. The arithmetic gives `ceil((24−5)/3) = 7` remaining qualifying completions. At the minimum grant, the seventh produces a balance of 26, enough to buy the tool with two remaining. All numbers are illustrative, not balance advice. [C-03]

The task may also directly award the tool earlier. When that happens, mark the goal obtained and allow a new choice; do not claim the original remaining count still represents necessary play. If the player instead spends all five existing credits on another item before continuing, the count becomes eight. A display that kept saying seven would be using a false balance assumption. If the target is only a blueprint and construction requires another resource, the full usable tool is not covered by this calculation. [C-03; C-05]

At an interruption, the design distinguishes credits already settled from rewards that would be earned only upon completion. A player who has left before qualifying must not be shown phantom durable credits; a completed and settled reward must not be described as newly earned twice after reconnection. Those are proposed state requirements, not F03-tested implementation behavior. [C-05]

### Inspected documented example and its limit

Digital Extremes's dated Lua's Prey notes describe guaranteed Lua Thrax Plasm earnings and exchange with Archimedean Yonta alongside rotation rewards. The material also has crafting uses. This is an example route to inspect, not proof of the mathematical assumptions above for every target or proof of improved wellbeing. No Warframe build was played in this research. [C-02; GDR-SRC-20261010-F03-008]

## Tradeoffs and alternatives

A second acquisition route adds currencies or state, explanations, migration cases and balancing interactions. Predictable acquisition may change how players value random drops or trade surplus. Shared credits preserve flexibility but weaken an unconditional target promise; reserved credits protect a commitment but can feel restrictive. Those are proposed effects to test with the economy topic, not measured consequences here. [C-01; C-04; C-05]

Direct reward selection is the strongest simpler alternative: the same eligible activity can grant the target without a credit layer or chance table. Deterministic milestones can also be sufficient. Retaining random discovery without a guarantee may fit an explicitly understood optional collecting experience, provided its actual consequences are acceptable; it is not appropriate to claim dependable access in that case. [C-01; C-06]

## Failure cases

| Warning sign in a future review/test | Likely distinction to inspect | Possible correction |
|---|---|---|
| A player hears “seven runs” as “seven attempts” or a time promise | Qualifying unit misunderstood | Use the actual completion unit, show prerequisites and reconsider wording [C-03; C-04] |
| Credit balance is spent, expired or capped | Conditional accumulation mistaken for protection | Make the condition visible, redesign the state or withdraw the assurance [C-05] |
| The tool is obtained but remains unusable | Target excludes required inputs or permissions | Narrow the promise or include the full usable target [C-05] |
| Players continue despite wanting to stop | Known grind, threatened progress or social costs | Remove the loss mechanism, reduce burden or use direct access; the finite bound alone is not enough [C-06] |
| The counter reduces welcome surprise | Presentation or acquisition predictability conflicts with the intended activity | Compare discreet tracking, deterministic selection or no guarantee where optional uncertainty is appropriate [C-01; C-04] |
| Easier qualifying activity dominates every choice | Reward criterion conflicts with intended play | Accept desirable efficiency or change what is rewarded; do not assume any shortcut is an exploit [C-01; C-07] |

## Counterexamples and do not use conditions

Do not use this pattern to claim proven protection from compulsive play, to justify a paid random-reward offer, or to certify compliance. It supplies neither clinical nor legal evidence. Do not place essential access accommodations behind its acquisition path. [C-06]

Do not promise a finite count when eligibility, storage, price, settlement or the full target requirements cannot be specified. Prefer a direct grant or a narrower description. Do not add random drops solely to make a deterministic progression track appear more exciting. In an activity centered on free creation, all tools available at the outset may be the correct baseline. In optional discovery, a visible guarantee may weaken the experience being sought. [C-01; C-03; C-05]

## Playtest

**Proposed; not performed.** First conduct a future approved state audit of the promise: zero/near/exact cost, different starting balances, duplicate drops, spending, caps, interruption and rule updates. A failed condition invalidates the relevant bound. Passing the paper audit is not a runtime reliability test. [C-05; C-07]

For a player-facing comparison, distinguish two questions. To test acquisition structure, compare direct selection, deterministic credits and mixed acquisition while recording the resulting outcome differences. To test counter salience, keep the underlying award sequence and target utility fixed while varying whether tracking is actively selected or automatically prominent. Do not claim an isolated presentation effect from a design that also changes payout distribution. [C-04; C-07]

Include people with different collection goals, experience, time availability and relevant access configurations. Measure prediction of eligible completions, explanation of other prerequisites, preferred actions, unwanted repetition, satisfaction with the acquired target and voluntary stopping. Counterbalance exposure and record prior reward-system familiarity, luck, target preference and novelty. Do not demand a preferred purchase as the “correct” answer. [C-07]

Predeclare locally meaningful benefit and burden criteria before recruitment. Reject or simplify the mixed design when direct selection performs at least as well within the decision's required precision, when the promise remains misunderstood, when pressure rises without the intended benefit, or when those needing access alternatives cannot use the route. An imprecise result is inconclusive, not evidence of equivalence. No participant count or effect estimate is asserted. [C-07]

## Claim ledger and sources

| Claim | Exact claim / classification | Support and precise locator | Applicability, uncertainty and next question |
|---|---|---|---|
| C-01 | A guaranteed route alongside random rewards may provide useful acquisition predictability while retaining some surprise. **hypothesis**. | Candidate mechanism below; 008 provides an existence example, not an effect test. | Low benefit confidence. A direct selection may be clearer, cheaper and more welcome. Compare against it, not only unbounded randomness. |
| C-02 | The inspected historical patch describes guaranteed resource awards and an exchange route alongside rotation rewards. **observed-example** of a document. | 008, Rotation Rewards / New Resource: Lua Thrax Plasm. | High for documented arrangement only; no hands-on verification, current-build guarantee or full-item completion-time estimate. |
| C-03 | For fixed target cost C, durable balance b and minimum grant g>0, ceil(max(0,C−b)/g) bounds remaining qualifying completions under the stated assumptions. **inference**. | Original arithmetic, Recipe and Worked examples. | High conditional mathematical confidence. Not a time bound, utility judgment or proof that all prerequisites are attainable. |
| C-04 | Making a bound salient can help planning or turn an activity into an unwanted quota; its experiential direction must be tested. **hypothesis**. | 009, §4.1/§5.3 supply mixed reports and limitations; F03 comparison proposal is not tested in that survey. | Low causal confidence; no universal display frequency, schedule or fatigue threshold. |
| C-05 | Loss, alternate spending, target changes, caps and settlement failures can invalidate the communicated bound. **inference**. | Logical preconditions of C-03; original state cases below. | High logical confidence; this paper design does not establish implementation reliability. State whether a promise is conditional or protected. |
| C-06 | Predictable acquisition does not prove voluntary participation or acceptable burden. **inference**. | C-03 does not constrain utility or time; 005 Considerations and F07 ethical candidate provide adjacent review rationale. | High as an insufficiency claim; effects of safeguards are untested. Missing participants and long-term outcomes remain open. |
| C-07 | The proposed comparisons can falsify fit but are not performed or validated assessments. **hypothesis**. | Playtest protocol and explicit competing explanations. | Low workflow-efficacy confidence; no results, sample-size guarantee or adoption approval. |

### GDR-SRC-20261010-F03-005 — Microtransactions (In-Game Purchases)

**Citation:** Valve. unknown. *Microtransactions (In-Game Purchases)*. Steamworks Documentation.

**Verified route:** [Microtransactions (In-Game Purchases)](https://partner.steamgames.com/doc/features/microtransactions).

**Version / access:** Mutable online documentation inspected on 2026-10-10; no edition/update date exposed. Checked 2026-10-10; `access: relevant-excerpt`. Platform-provider practitioner guidance; cited advice is not a universal formal standard.

**Inspected locators:** Anticipating Fraud; Considerations for in-game economies and best practices, especially items 1–2 and concluding metrics paragraph.

**Claims in this artifact:** Adjacent practitioner rationale for C-06 only; not a measured outcome.

**Limits / independence:** The selected recommendations supply no controlled outcome measurements. The linked Kyle Davis talk was not viewed. /documentation/MicroTxn is an access alias, not another independent source. Platform-specific numerical fraud restrictions are not generalized here.

**Rights:** Valve documentation; paraphrase only. No implied redistribution license or platform certification.



### GDR-SRC-20261010-F03-008 — Update 32.2.0: Lua’s Prey

**Citation:** Digital Extremes. 2022-11-30. *Update 32.2.0: Lua’s Prey*. Warframe official patch notes.

**Verified route:** [Update 32.2.0: Lua’s Prey](https://www.warframe.com/en/patch-notes/pc/32-2-0).

**Version / access:** PC Update 32.2.0; dated historical configuration. Checked 2026-10-10; `access: relevant-excerpt`. Official build-specific feature description; observed document, not reproduced gameplay.

**Inspected locators:** New Lua Nodes: Conjunction Survival → requirement, Rotation Rewards, New Resource: Lua Thrax Plasm; resource-use and Archimedean Yonta exchange paragraphs.

**Claims in this artifact:** C-02; existence lead for C-01, not validation of C-03–C-07.

**Limits / independence:** Documents one mixed acquisition arrangement, not the efficacy of F03-PAT-01. Crafting inputs and access prerequisites mean no general bound on full-item acquisition time follows. Vendor exchange is not player-to-player trade.

**Rights:** Digital Extremes copyright; paraphrase only; images not redistributed.



### GDR-SRC-20261010-F03-009 — Daily Quests or Daily Pests? The Benefits and Pitfalls of Engagement Rewards in Games

**Citation:** Julian Frommel and Regan L. Mandryk. 2022-10-25. *Daily Quests or Daily Pests? The Benefits and Pitfalls of Engagement Rewards in Games*. ACM; Proceedings of the ACM on Human-Computer Interaction 6 (CHI PLAY), Article 226, 23 pages.

**Verified route:** [Daily Quests or Daily Pests? The Benefits and Pitfalls of Engagement Rewards in Games](https://research-portal.uu.nl/en/publications/daily-quests-or-daily-pests-the-benefits-and-pitfalls-of-engageme/). DOI: `10.1145/3549489`.

**Version / access:** Published article text in author-uploaded ResearchGate copy, upload attributed to Julian Frommel on 2023-01-17; matched title/authors/DOI to institutional record. Checked 2026-10-10; `access: relevant-excerpt`. Primary cross-sectional mixed-methods survey with guided recall; self-reported player accounts, not observed gameplay or intervention.

**Inspected locators:** Article pp. 226:7–9, §§3.1–3.4; pp. 226:9–11, §§4.1.1–4.1.4; pp. 226:17–18, §5.3. Prose inspected; no numerical table results used.

**Claims in this artifact:** C-04 as a hypothesis-generating contrast; no direct test of this recipe.

**Limits / independence:** Author-uploaded full-text route: https://www.researchgate.net/publication/365003534_Daily_Quests_or_Daily_Pests_The_Benefits_and_Pitfalls_of_Engagement_Rewards_in_Games . Institutional PDF returned 403 and publisher full-text route failed before this route succeeded. Recall, selected regular-player sample, prompting and initial single-coder interpretation limit generalization. No causal or longitudinal fatigue effect estimated here.

**Rights:** Copyright held by owner/authors; publication rights licensed to ACM. Paraphrase only; no participant quotations or full text redistributed.


## Related entries and history

Owning topic: [Progression and rewards](../topics/progression-and-rewards.md), `GDR-CAND-20261010-F03-TOP-01`. Economy interaction: [Economies and resources](../topics/economies-and-resources.md), `GDR-CAND-20261010-F03-TOP-02`; audit duplicate conversions with [Conversion-loop budget](conversion-loop-budget.md), `GDR-CAND-20261010-F03-PAT-02`.

`F03-CON-05` preserves predictable access versus valued uncertainty; no genre rule resolves it automatically. Full controlled game-specific and longitudinal evidence is missing. F02 dependency remains uninspected. Parent-reviewed first-wave corrections are recorded in the review packet; those candidates are not released references.

**History:** initial F03 draft, 2026-10-10, version 0.1.0, candidate_revision initial-research-1; predecessor/supersession null. Author self-review removed any implication that bounded completions means bounded time or humane pacing. Independent review and host retrieval are pending; no release. Exact byte hash: integrity receipt.

---
id: GDR-CAND-20261010-F03-PAT-02
kind: pattern
title: Conversion-loop budget
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
- resource conversion audit
- craft-salvage loop audit
- arbitrage boundary check
tags:
- economy
- crafting
- resources
- incentive-exploits
- state-boundaries
- emergence
related_topics:
- GDR-CAND-20261010-F03-TOP-02
- GDR-CAND-20261010-F03-TOP-01
related_patterns:
- GDR-CAND-20261010-F03-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-F03-005
- GDR-SRC-20261010-F03-006
- GDR-SRC-20261010-F03-007
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

# Conversion-loop budget

**Draft, unvalidated design-audit pattern.** It is not an exploit scanner, runtime implementation or assurance of a safe live economy. Version 0.1.0, candidate revision initial-research-1. No game code, model simulation or player test was run.

## Purpose

Inspect how resource rules compose so that a designer can distinguish an intended productive route from an unintended source, misleading sink or apparent exploit caused by an incomplete model. The goal is to preserve the intended resource decisions, including valuable creative play—not to make every loop unprofitable. [C-01; C-05]

This pattern is narrower than general balancing or user research. It produces a bounded transition/intent record and the next discriminating question. It does not decide a game's values, automatically ban strategies, or replace a player-experience review. [C-07]

## Context and prerequisites

Use when two or more conversion, salvage, trade, refund, crafting or reward rules interact and the designer cannot explain their combined resource effect. The prerequisite is a readable rule description and a proposed or approved local purpose for resource creation. No player telemetry is necessary for a paper audit, but estimating actual frequency or impact would require separate evidence. [C-01; C-05]

Define the boundary and units; available versus owned versus reserved resources; consumed versus reusable prerequisites; actor permissions; cooldown or one-time states; binding/tradability; capacity; rounding; and the settlement/version states relevant to the selected routes. Record omitted systems explicitly. If these cannot be described, stop at a missing-specification finding rather than inventing the rules. [C-03; C-04]

The design must also identify who can authorize a production budget or change a rule. In this draft no game-specific budget is approved. “Intended” in a worked example is an illustrative assumption, not a studio decision. [C-05]

## Mechanism and evidence

| Link | Evidence / reasoning | Unresolved limit |
|---|---|---|
| Represent both resource and enabling state | Dormans provides a resource/state modeling method [C-02; GDR-SRC-20261010-F03-007] | Representation can omit spatial, social or implementation conditions |
| Compose routes and reconcile opening/closing quantities | Conditional arithmetic [C-03; C-04] | The result only applies to described units, transitions and boundaries |
| Recognize a repeatable gain as an effective source | Logical consequence when every required state is restored [C-03] | Expected gain is not guaranteed gain; finite gates and hidden costs matter |
| Compare that source with declared purpose and affected options | Proposed review method [C-05] | Mathematical profit does not settle intention or desirability |
| Change only the rule that causes unacceptable distortion | Hypothesis [C-01; C-08] | May remove valued emergent play or shift the problem to another route |
| Preserve a better player experience | Not established [C-07] | Requires separate comprehension, access, agency and burden evidence |

## Recipe

1. **Name one threatened decision.** For example: “choosing whether to consume a scarce ingredient becomes irrelevant after a reversible recipe pair.” Also record the strongest harmless explanation: the loop may be deliberate production. Avoid starting from “remove all exploits.” [C-01; C-05]
2. **Choose a bounded route set.** Include the relevant earning, conversion, salvage, sale, purchase, refund, binding and reset transitions. State exclusions—such as other accounts, multiplayer handoffs or future content—so a passing subset is not promoted to global assurance. [C-03; C-07]
3. **Write transition records.** For each action record inputs, outputs, ownership changes, consumed prerequisites, reusable prerequisites, duration/cooldown state, eligible actors, capacity, integer/batch behavior, cancellation and rule version. Separate a transfer to a treasury from currency deletion. [C-03; C-04]
4. **Compose a complete round trip.** Start with a concrete legal state. Apply every transition needed to return to a comparable state; reconcile quantities and list all state variables that did not return. A route that ends with more ore but less fuel is not a free ore cycle. A consumed one-time permission cannot be omitted because it has no currency icon. [C-03]
5. **Check edges, not only averages.** Examine zero, just-below, exact and just-above requirements, full capacity, partial stacks, single versus batch operations, cancellation and old/new rule versions. Separate expected random yield from minimum/maximum possible yield. Do not extrapolate a linear exchange rate through floor/ceiling rounding or caps. [C-03; C-04]
6. **Classify gain and impact.** Record whether it is intended production within a declared budget, valuable emergent play needing a decision, unintended extraction, a boundary/accounting error, or still unknown. Identify whose access or options change, including counterparties and returning players. Profit alone cannot choose the category. [C-05; C-07]
7. **Compare remedies with doing nothing.** Candidate remedies include correcting a reverse recipe, making an omitted input explicit, changing yield/eligibility, limiting a genuinely finite operation, or acknowledging the loop as a source and balancing around it. Broadly increasing costs or removing trade may burden unrelated play. Each proposed remedy needs a stated reason and separate approval. [C-05; C-08]
8. **Recheck affected routes and the player-facing purpose.** A local fix can create another conversion path or remove a valued strategy. Preserve before/after rule descriptions and unresolved cases. Stop when the route budget fits the chosen purpose and remaining uncertainty is explicitly accepted by the authorized reviewer—not when a generic gain score reaches zero. [C-07; C-08]

### Adjustable variables

The boundary, included routes, initial states, units, ownership, yield, rounding, batch size, capacities, repeat permissions, regeneration, settlement and update rules are model variables. The acceptable resource creation rate, access burden and permitted emergence are design decisions to obtain, not values supplied by this pattern. Audit depth is also a cost: a simple reversible pair can be inspected directly; a large evolving network may need separately authorized tooling and broader review. [C-01; C-03; C-05]

**Exit conditions:** stop with “cannot determine” when a relevant rule or state is unknown; stop the costless-loop claim when a consumed input is discovered; decline to recommend a fix without a declared purpose or impact criterion; do not publish an exploit-free statement from a subset; do not convert this paper audit into live economy changes. [C-03; C-05; C-07]

## Worked examples

### Illustrative complete example: craft and salvage

Invented rules: crafting consumes two ore and produces one component; salvaging that component produces three ore. The player starts with two ore and no component. Assume both operations are repeatable, cost no other resource, require no one-time flag, and have enough capacity. Crafting leaves zero ore and one component; salvage leaves three ore and no component. The enabling state is restored with one additional ore. A second round trip ends with four ore. This is an effective source under these specific assumptions. [C-03]

Before proposing a nerf, ask whether growing resource production is the intended activity. If so, record the cycle as a source and examine whether it dominates all other meaningful methods or imposes an unwanted task. If a reversible crafting interface was supposed to conserve ore, the discrepancy instead warrants a recipe decision. Neither intention is established merely by the numbers. [C-05]

Now add a consumed fuel unit to crafting. The first round trip yields one extra ore but leaves one less fuel. The full state has not returned. Inspect how fuel is acquired: if it consumes another finite input, there is an opportunity cost; if it regenerates, duration and capacity affect the repeatable rate; if another refund recreates it, follow that route too. Calling the first partial route “infinite free ore” would be unsupported. [C-03; C-04]

A further variant permits salvage once per component family. The flag is a scarce entitlement even without a visible numeric balance. A reset or transfer that changes this flag would be a separate transition to inspect; no such behavior is assumed here. [C-03]

### Illustrative rounding boundary

A fictional exchange displays “two marks for three chips.” Its actual rule converts each single mark using `floor(1.5 × marks)` and offers the reverse batch at a separately defined rate. Converting two marks in one batch yields three chips; converting one mark twice yields two chips. The display ratio does not alone specify the outcome. This example establishes path dependence, not a profitable exploit; the reverse rule and all prerequisites must be stated before claiming a closed gain. [C-03; C-04]

### Documented distinction: a sink can remove a different resource

The Jagex announcement distinguishes currency deletion from funded purchases that remove items. That document illustrates why this audit records which stock is reduced, who receives the payment and whether the treasury is inside the boundary. The complete invented coin arithmetic is in the owning topic; no Jagex policy was modeled or tested here. [C-04; GDR-SRC-20261010-F03-006]

## Tradeoffs and alternatives

An audit costs specification effort and can encourage false precision. A diagram can look complete while omitting social agreement, access limitations, bugs or a later content update. A direct recipe list with explicit inverse operations may be more useful than a large model for a small system. Separate actual behavior reports from model possibilities. [C-01; C-07]

Removing a conversion can eliminate creative production, convenient reuse or a recovery route. Adding a tax can discourage unrelated trade. Adding a cooldown can make the chosen activity less convenient without addressing the underlying value imbalance. These are proposed tradeoffs, not universal causal effects. Compare a narrower correction, a clear source budget and no change before reaching for a global restriction. [C-05; C-08]

For transferable purchased value, the design also needs reversal and provenance questions identified in platform guidance. This pattern does not supply fraud detection, account punishment rules or universal waiting periods. Those belong to a separately scoped implementation and safety review. [C-06]

## Failure cases

| Warning sign | Why the audit may be wrong or insufficient | Response |
|---|---|---|
| “Free gain” ignores fuel, permission or time state | The route is not closed over relevant prerequisites | Expand the state and revise the claim [C-03] |
| Every production route is flagged as an exploit | The audit has substituted conservation for the intended game | Obtain the creation budget and preserve purposeful production [C-05] |
| Single-unit audit passes but batches differ | Rounding, caps or nonlinear recipes were omitted | Inspect the exact integer states and operation order [C-03] |
| Balances reconcile but some players cannot recover | Aggregate consistency says nothing about access distribution | Evaluate feasible routes and the intended failure condition [C-07] |
| “Fix” destroys a valued player discovery | Impact and consent were omitted from classification | Restore a comparison baseline and review the strategy's role [C-05; C-08] |
| Document says safe but an interrupted state is unknown | Implementation reliability has been inferred from a rule model | Mark the boundary unverified; do not approve deployment [C-07] |

## Counterexamples and do not use conditions

Do not apply a zero-gain objective to a system whose point is automation, production, accumulation or freely expressive construction. Do not demand conservation of a resource merely because it is called currency. Do not treat a model possibility as proof that actual players discovered or abused it. A paper cycle without a verified path through the real rules is not an observed exploit. [C-03; C-05; C-07]

Do not use this pattern as the only balance review, as certification for a marketplace, or as authority to claw back player holdings. If a resource is intentionally unlimited and creates no relevant tradeoff, building a detailed conservation model may be wasted effort. If purpose, rules or affected groups are unknown, return a bounded missing-information finding. [C-01; C-07]

## Playtest

**Proposed, not performed.** A future method comparison can give reviewers a small authored rule set containing an intentional productive loop, an unintended reverse-recipe gain, a hidden consumable cost, a rounding boundary and an unresolved rule. Compare ordinary review with this recipe. Record correctly scoped findings, false exploit labels, unsupported intent claims, omitted boundaries and review time. An answer key would validate only those constructed cases, not cold/blind host retrieval or real-world completeness. [C-08]

A separate player-facing comparison would evaluate a proposed correction against the original intended route. Include people using different production strategies and access configurations; preserve the same content goals and give both routes adequate discovery opportunity. Measure understandable choices, unwanted maintenance, lost creative options and feasible recovery, not just resource totals. Prior strategy knowledge, unequal starting inventories, network effects and novelty can confound the comparison. [C-07; C-08]

Reject or narrow the pattern if it systematically confuses intended production with defects, costs more review effort than useful findings justify, or encourages changes that reduce the intended experience. Reject a specific remedy if the ledger target improves but the valued route or necessary recovery disappears. Local decision criteria and acceptable uncertainty must be set before actual testing; no universal sample count or pass threshold is supplied. [C-08]

## Claim ledger and sources

| Claim | Exact claim / classification | Support and precise locator | Applicability, uncertainty and next question |
|---|---|---|---|
| C-01 | A bounded audit of resource conversions may expose unbudgeted sources while preserving intended productive play. **hypothesis**. | Original recipe below; 007 is methodological context, not a test of this pattern. | Low workflow-efficacy confidence. It adds work and cannot guarantee complete exploit coverage. |
| C-02 | The inspected modeling paper distinguishes resource flow and state dependencies and uses artificial-agent exploration. **observed-example** of a report. | 007, printed pp. 2–3, Figure 1; pp. 6–7 Discussion. | High for report contents; no human outcome or F03 execution. Same paper as F01 source-08. |
| C-03 | If all relevant enabling state is restored and spendable stock increases after a repeatable route, the route is an effective source under that model. **inference**. | Original ore/component examples and explicit assumptions. | High conditional logic; hidden costs, random outcomes, nonlinear rounding, finite access or capacity can invalidate a claimed costless repeat. |
| C-04 | A transfer, consumption, reservation and destruction must not be silently interchanged when auditing a cycle. **inference**. | Original state definitions; 006 tax/item distinction supplies an external document example. | High accounting distinction; the correct classification depends on declared boundary and ownership. No current game implementation verified. |
| C-05 | Classify gains against intended creation budgets and harms rather than treating every profitable route as an exploit. **hypothesis**. | Proposed intent/impact decision table; productive-workshop counterexample. | Low efficacy confidence. Intent needs an actual approved local design record; ambiguous cases remain undecided. |
| C-06 | Tradability and reversal create distinct risk/settlement questions; generic numerical platform restrictions are not derived here. **practitioner-heuristic**. | 005, Anticipating Fraud. | Moderate for Valve’s platform rationale; no quantified fraud incidence, legal rule or implemented prevention. |
| C-07 | Correct accounting and passing a bounded audit do not establish fun, fairness, complete exploit absence or implementation safety. **inference**. | C-03 is not a utility measure; 007 abstraction limits and TOP-02 distribution counterexample. | High as an insufficiency claim. Player impact and unmodeled rules need separate evidence. |
| C-08 | The proposed comparisons can reject or narrow the audit’s usefulness. **hypothesis**. | Playtest and validation plan below. | Low workflow-efficacy confidence; no test was performed. Review time, false alarms and lost creative options are costs. |

### GDR-SRC-20261010-F03-005 — Microtransactions (In-Game Purchases)

**Citation:** Valve. unknown. *Microtransactions (In-Game Purchases)*. Steamworks Documentation.

**Verified route:** [Microtransactions (In-Game Purchases)](https://partner.steamgames.com/doc/features/microtransactions).

**Version / access:** Mutable online documentation inspected on 2026-10-10; no edition/update date exposed. Checked 2026-10-10; `access: relevant-excerpt`. Platform-provider practitioner guidance; cited advice is not a universal formal standard.

**Inspected locators:** Anticipating Fraud; Considerations for in-game economies and best practices, especially items 1–2 and concluding metrics paragraph.

**Claims in this artifact:** C-06 only; platform practitioner rationale.

**Limits / independence:** The selected recommendations supply no controlled outcome measurements. The linked Kyle Davis talk was not viewed. /documentation/MicroTxn is an access alias, not another independent source. Platform-specific numerical fraud restrictions are not generalized here.

**Rights:** Valve documentation; paraphrase only. No implied redistribution license or platform certification.



### GDR-SRC-20261010-F03-006 — Yama CAs & More!

**Citation:** Jagex. 2025-05-29. *Yama CAs & More!*. Old School RuneScape official news.

**Verified route:** [Yama CAs & More!](https://secure.runescape.com/m=news/yama-cas--more?oldschool=1).

**Version / access:** Dated 29 May 2025 update announcement; not asserted to be the current 2026 rule set. Checked 2026-10-10; `access: relevant-excerpt`. Firsthand policy/configuration announcement and developer rationale; observed document.

**Inspected locators:** Grand Exchange Tax → Why Change the GE Tax Rate?, Here’s what’s changing, Improvements to Item Sinks; final exemption paragraph.

**Claims in this artifact:** Document example informing C-04, not proof of the proposed audit.

**Limits / independence:** No post-change causal evaluation or player welfare data in the inspected section. The announced 2025 rate change is not the 2021 intervention analyzed by 011. Developer goals are not measured effects.

**Rights:** Jagex copyrighted news; paraphrase only.



### GDR-SRC-20261010-F03-007 — Simulating Mechanics to Study Emergence in Games

**Citation:** Joris Dormans. 2011. *Simulating Mechanics to Study Emergence in Games*. AAAI; AIIDE technical report WS-11-19, pp. 2–7.

**Verified route:** [Simulating Mechanics to Study Emergence in Games](https://ojs.aaai.org/index.php/AIIDE/article/download/12477/12336/16005). DOI: `10.1609/aiide.v7i3.12477`.

**Version / access:** Six-page published 2011 paper. Checked 2026-10-10; `access: relevant-excerpt`. Original modeling method and artificial-agent simulation report; not human-player evidence.

**Inspected locators:** Printed pp. 2–3, Resource Flow and Communication of State; Figure 1 on p. 3; pp. 6–7, Simulating SimWar and Discussion; PDF pages 2 and 6 visually inspected.

**Claims in this artifact:** C-02 and abstraction limit in C-07; not validation of the F03 recipe.

**Limits / independence:** Resource/state abstraction omits spatial/tactical detail; no F03 model was executed. Exact URL/edition also occurs as GDR-SRC-20261010-F01-08 in inspected first-wave bytes: cross-batch identity reconciliation remains pending, not independent corroboration.

**Rights:** AAAI copyright; paraphrase only; no diagrams or PDF redistributed.


## Related entries and history

Owning topic: [Economies and resources](../topics/economies-and-resources.md), `GDR-CAND-20261010-F03-TOP-02`. Cross-topic: [Progression and rewards](../topics/progression-and-rewards.md), `GDR-CAND-20261010-F03-TOP-01`. A mixed acquisition route from [Guaranteed acquisition alongside random drops](guaranteed-acquisition-alongside-random-drops.md), `GDR-CAND-20261010-F03-PAT-01`, may introduce duplicate-conversion paths needing this audit.

`F03-CON-06` preserves intentional creative production versus unintended extraction. Current canonical source deduplication, actual F02 dependencies and independently evaluated audit efficacy remain unresolved. No genre guidance is presumed.

**History:** 2026-10-10; version 0.1.0; candidate_revision initial-research-1; predecessor/supersession null. Author self-review made the full-state condition explicit, distinguished path dependence from positive gain, and retained productive-loop counterexamples. Independent review/host retrieval pending; no release. Exact byte hash: integrity receipt.

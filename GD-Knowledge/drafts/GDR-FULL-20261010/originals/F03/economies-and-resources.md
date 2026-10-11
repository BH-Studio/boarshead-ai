---
id: GDR-CAND-20261010-F03-TOP-02
kind: topic
title: Economies and resources
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
- sources and sinks
- currencies
- crafting economy
- trading
- inflation
- resource exploits
- resource scarcity
tags:
- economy
- resources
- scarcity
- crafting
- trade
- incentives
- state-boundaries
related_topics:
- GDR-CAND-20261010-F03-TOP-01
- GDR-CAND-20261010-F01-TOP-02
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-F03-PAT-02
- GDR-CAND-20261010-F03-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-F03-005
- GDR-SRC-20261010-F03-006
- GDR-SRC-20261010-F03-007
- GDR-SRC-20261010-F03-011
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

# Economies and resources

**Draft research, not released guidance.** This entry concerns designed resource systems, not financial advice, legal compliance or authorization to alter a live economy. The [review packet](../reviews/full-run-20261010-f03-review-packet.md) contains the snapshot, missing dependency and gate records. No live market data was downloaded, no economy code or simulation was run, and no players participated in F03 tests.

## Decision and scope

The decision is **which scarce means should shape play, how they are created and moved, and whether the resulting opportunities and obligations serve the intended experience**. A game economy can consist of a few consumables in a finite encounter; it does not require money, trade, monetization or a persistent marketplace. These are working analytical definitions. [C-01; C-04]

A **resource** is a quantity, entitlement or capacity relevant to an action. A **stock** is an amount at a particular state; a **flow** changes it over an interval. A **source** creates units inside the declared boundary, a **sink** destroys them, a **transfer** changes ownership without creating or destroying the same units, and a **conversion** transforms specified inputs into outputs. A currency is a resource used to denominate and exchange value under the game's rules. These labels depend on the boundary: an import into a player wallet may be a transfer from a finite NPC stock or a creation event in a wider model. [C-01; C-02]

Scarcity is relative to a goal and usable access, not merely to global totals. A player can own ten units but have only four spendable because six are committed. A large stock held by someone else does not guarantee access, and a nominally free action can consume scarce time, attention, capacity or a unique opportunity. A precise model specifies which of these costs it includes and leaves experiential valuation for evaluation. [C-04; C-16]

The topic covers sources/sinks, scarcity, currencies, crafting, trading, inflation diagnostics and incentive exploits. [Progression and rewards](progression-and-rewards.md) owns the purpose and experience of earning/unlocking. F02 decision and difficulty dependencies are not yet inspected; F07 evaluation/ethics are inspected reviewed-candidate context, not released authority. Fictional institutions and world plausibility require Worlds and Characters coordination; transaction communication requires Presentation and Interaction. Runtime implementation is excluded.

## Core explanation and mechanisms

### Start with an inspectable state boundary

A minimal design record identifies the resource's unit, owner, scope, quantity, reservations, eligible uses, expiry, conversion rule version and settlement status. Choose the observation boundary—one player, party, match, market or all modeled accounts—and state which external systems remain excluded. For an irreversible action, identify the point at which commitment becomes durable, what cancellation returns, and which receipt prevents an operation from being treated as two distinct grants. This is a design specification to review, not implemented transaction code. [C-01; C-19]

For one homogeneous resource within a chosen boundary:

`closing stock = opening stock + created − destroyed + imported − exported`

Internal transfers cancel from this aggregate. With multiple resources, keep separate quantities and represent conversion inputs/outputs explicitly; do not add coins, ore and time as though they share a unit. An exchange rate is a rule or an observation, not conservation of utility. Reservations change availability but do not destroy owned stock. These are bookkeeping identities under the declared definitions, not evidence of equilibrium or enjoyment. [C-02]

Dormans's resource/state modeling supplies a concrete method for representing such relations. Its reported artificial-player SimWar exploration is not a human experiment and omits important implemented-game detail. Therefore, structural modeling can motivate an audit, but the paper does not validate the player experience of a proposed balance change. [C-03; GDR-SRC-20261010-F03-007]

### Separate circulation from destruction

Player-to-player payment transfers currency; a fee only becomes a currency sink when those units leave the modeled circulating system or are destroyed, depending on the chosen definition. Purchasing an item with previously collected taxes and then deleting the item is an item sink; the payment to its seller is not simultaneously deleted currency. Mislabeling these operations can double-count sink strength. The synthetic example below makes the boundary explicit. [C-02; C-17]

Jagex's 29 May 2025 announcement distinguishes deleted tax revenue from tax-funded item purchases/removal and treats existing offers differently from new offers. It also states an inflow-versus-sink rationale. The first is a documented configuration; the second is the developer's explanation, not a measured causal result. Neither should be imported as a universal tax rate or asserted as the current 2026 configuration. [C-07; C-08; GDR-SRC-20261010-F03-006]

### Inflation is not every increase in a number

An increased currency stock, a particular item becoming more expensive, and a broad increase in comparable purchase prices answer different questions. If the price of one rare ingredient rises because its supply changes, that observation alone does not establish that every coin buys less across the economy. Conversely, unchanged aggregate prices do not show that newcomers can afford a required item. [C-06; C-13]

An illustrative fixed-basket index can compare the cost of the same quantities of the same goods between states. A trade-weighted index whose composition changes may move because people trade different goods. New item quality, thin markets, bundles, tax-inclusive versus tax-exclusive prices, changing participant cohorts and unrecorded transactions can all alter the meaning of a comparison. Define the basket, weights, eligible observations and exclusions before interpreting a movement. No actual index was calculated here. [C-06]

For gameplay, pair price descriptions with feasible earning routes, expenditure commitments and access conditions. “Affordability” measured as price divided by nominal income ignores failure, caps, unavailable activities and the fact that someone may not want the earning task. A simulated minimum count of actions is not an estimate of acceptable burden. [C-04; C-13; C-20]

### Market evidence is scoped and imperfect

Hogan-Hennessy, Xenopoulos and Silva analyze Wiki/RuneLite-derived item records around a 2021 intervention using discontinuity/kink and difference-in-differences models. Near the 500-million-GP tax boundary, §4.1 reports a −6.9% volume estimate with reported 95% bounds of −13% to −1%; the estimate near 100 GP was not distinguishable from zero. These are historical study boundaries, not recommended thresholds. Item-removal analyses concern selected goods, not general player welfare. The study is observational, was not replicated here, and does not evaluate Jagex's later 2025 change. [C-09; GDR-SRC-20261010-F03-011]

The abstract's broad “not meaningfully” wording and the localized body estimate require interpretation rather than silent harmonization. Statistical detectability and practical importance are different; the authors' practical criterion is not established. Appendix A.3 also contains a 2019 announcement date inconsistent with the main intervention chronology. The packet preserves these issues, plus an NPC price-bound terminology problem, for independent review. They narrow confidence rather than justify discarding all findings or correcting the source invisibly. [C-10; F03-CON-02; F03-CON-03; F03-CON-04]

### Incentives can create sources through composition

A recipe can appear balanced in isolation yet compose with another rule into repeatable gain. Suppose two ore become one component and salvage returns three ore. If all other conditions return to their initial state, that round trip creates one ore each time. If it consumes fuel, changes a nonrenewable flag or requires an external input, it is not that same costless closed cycle. Assess the complete state, not just the visible currency balance. [C-11]

Profit is not automatically an exploit. Gathering, crafting specialization, patient trade and automation may intentionally create value. A design defect is a claim about the intended rule and effect, not a synonym for an ingenious or efficient action. The proposed policy is to separate intended budgeted production, acceptable emergent play and unintended extraction, with human decisions for ambiguous cases. No intent or exploit prevalence is attributed to a named game here. [C-15]

## Design choices and alternatives

The recommendations in the following comparisons are **hypotheses** about fit and player experience. The stock identities do not validate them. [C-05; C-12; C-15]

| Option | Candidate purpose | Costs, alternatives and do-less condition |
|---|---|---|
| Finite authored resource pool | Make opportunity cost legible within a bounded experience | Exhaustion may soft-lock rather than create a meaningful failure. Provide an intentional end state, alternate route or transparent recovery when appropriate; no persistent replenishment system may be needed |
| Repeatable earning / production | Support chosen projects or escalating capacity | Can incentivize low-value repetition or accelerate imbalance. Compare direct grants, bounded production and fewer resource requirements |
| Consumable-use sink | Make each use or sustained operation a resource decision | Can punish experimentation or create compulsory maintenance. Reusable tools or scenario-specific allowances may serve the same choice more directly |
| Repair / upkeep / decay | Tie capacity to an ongoing commitment | Can impose absence penalties or taxes on those already struggling. Test repair-free modes, bounded failure losses or no upkeep |
| Optional expression sink | Give surplus a voluntary use without raising required power | Depends on genuine perceived value; production/localization cost persists, and status can create pressure. Fewer durable options may outperform disposable novelty |
| Transaction fee | Remove currency or fund a declared system function | Can burden particular trading routes, fragment markets or encourage bypass. Direct source adjustment or selected item removal may target a different issue more accurately |
| Item deletion / crafting consumption | Reduce a specific item stock or enable transformation choices | Can raise input access costs and favor incumbent owners. Model affected items separately from currency and compare reversible or lower-consumption recipes |
| Multiple currencies | Separate systems, entitlements or intended budgets | Adds conversion, explanation and stranded-balance burden. One transparent currency or direct unlocks may be sufficient |
| Hard caps / nontransferability | Bound accumulation or isolate acquisition paths | Can invalidate earning at a cap, frustrate cooperation or shift trade elsewhere. Compare a visible cap policy, shared nonmarket contribution or fewer restrictions |
| No player trading | Preserve authored access and remove market mediation | Loses exchange and specialization opportunities. Optional NPC exchange or direct sharing can be simpler than an auction system |

### Currency design must expose opportunity cost

For each currency, state why an existing unit cannot do the job. Specify earnability, purchaseability if any, exchange direction, expiry, refunds and whether the same unit serves necessary and optional goals. A special token can protect an acquisition commitment, but a proliferation of tokens can also conceal total costs and leave unusable balances. Neither simplicity nor segmentation wins independently of the purpose. [C-05; C-16]

A distinction between paid and earned balances may matter to a platform or implementation, but this research does not prescribe a payment architecture or certify compliance. Valve's fraud guidance highlights transfer and reversal risks; its specific platform thresholds are not reused as generic design rules. False positives, account recovery and legitimate shared use also belong in any separately authorized system review. [C-14; GDR-SRC-20261010-F03-005]

### Crafting and trading need complete transformation rules

A recipe should identify consumed versus merely required inputs, reusable tools, batch size, yield, by-products, failure outcomes, binding, storage capacity, time and reversibility. Distinguish expected gain from guaranteed gain when yield is random. Integer rounding can make a one-unit recipe behave differently from a batch recipe; reciprocal exchange labels do not guarantee exact inverses. Test those states explicitly rather than assuming a smooth average describes them. [C-11; C-12]

Trading adds counterparties and settlement, not just a price. Inspect availability, price comprehension, transfer eligibility, failure or cancellation, and the state of resources committed to an offer. A player may correctly understand that a trade is affordable and still prefer not to make it. That preference is not an error signal. The first-wave corrected affordability method preserves this distinction. [C-16; C-19]

A crafting chain may provide satisfying planning, or it may force repetitive inventory processing to obtain a tool necessary for another activity. A market may offer specialization, or concentrate control over an input. Those are proposed alternatives for investigation, not conclusions inferred from the presence of a recipe graph or market. [C-12; C-13]

## Application process

1. **Declare the experience and boundary.** Identify the relevant choices, affected people and what counts as success or failure. Decide whether the economy is finite or persistent and what is outside its accounting. [C-01; C-04]
2. **Inventory stocks and transitions.** List units, owners, source events, sinks, transformations, commitments, caps, resets and transfers. Record old/new rules and settlement states separately. [C-02; C-19]
3. **Trace representative routes.** Follow an early participant, a returning participant, a specialist and someone using an access alternative. Examine how they obtain required means without assuming identical time or preference. [C-04; C-16]
4. **Audit composition.** Apply [Conversion-loop budget](../patterns/conversion-loop-budget.md) to a bounded set of material routes. Record omitted states; do not claim global exploit freedom. Preserve intentional positive production. [C-11; C-15]
5. **Choose a targeted intervention and alternative.** Separate currency, item and distribution problems. Compare doing less, source adjustment and the smallest relevant sink; record burdens rather than optimizing only totals. [C-05; C-13]
6. **Evaluate mechanics and experience separately.** Proposed model/state tests address consistency; participant comparisons address comprehension, agency and burden. Neither substitutes for the other. Revise or remove an intervention that meets a stock target while failing the player-facing purpose. [C-18]

No step was executed against a project or live economy in F03. Only document generation and static artifact checks were performed.

## Patterns and genre adaptations

[Conversion-loop budget](../patterns/conversion-loop-budget.md), `GDR-CAND-20261010-F03-PAT-02`, is a bounded design audit for composing resource rules without suppressing every productive loop. Its proposed narrower ownership is conversion-state auditing; coordination must still check duplication against F07's broader diagnosis pattern and the current index. [C-11; C-15]

[Guaranteed acquisition alongside random drops](../patterns/guaranteed-acquisition-alongside-random-drops.md), `GDR-CAND-20261010-F03-PAT-01`, changes earning predictability and therefore belongs in stock and demand analysis as well as progression design. Its experiential efficacy remains untested. [C-20]

Adaptation depends on finite versus persistent state, private versus shared ownership, competitive comparison, optional trading and intended scarcity. Those facets can conflict in a hybrid; an abundance-oriented creative activity and a scarce-resource challenge may require separate budgets instead of one dominant genre rule. Specific genre guidance remains a separate task; no genre-specific artifact is authored here. [C-05; C-15]

## Examples and counterexamples

### Illustrative: tax revenue is not all currency destruction

Assume a closed model containing player wallets and a treasury. It starts with 1,000 coins. An earning event creates 120. A player-to-player item sale for 100 transfers 90 to the seller and 10 to the treasury. The treasury destroys six coins, spends the remaining four buying a different existing item from a player, then destroys that item. All quantities are invented local settings, not balance recommendations. [C-02; C-17]

| Step | Player-wallet coins | Treasury coins | Combined coins | Item consequence |
|---|---:|---:|---:|---|
| Initial | 1,000 | 0 | 1,000 | No change |
| Create 120 | 1,120 | 0 | 1,120 | No change |
| Internal sale with 10 collected | 1,110 | 10 | 1,120 | Ownership changes; no item creation |
| Destroy six treasury coins | 1,110 | 4 | 1,114 | No change |
| Buy and delete one existing item for four | 1,114 | 0 | 1,114 | One item removed |

The net currency source is 114, not 110: only six collected coins were destroyed. The item purchase returned four coins to a player. If the boundary excluded the treasury, tax collection and treasury purchases would instead be exports/imports to the player-wallet subsystem. State the convention before comparing sink reports. This is a hand-specified accounting example; it is not telemetry or a simulated policy result. [C-02; C-17]

### Illustrative: a profitable loop can be intended or misclassified

With the two-ore/component/three-ore cycle described earlier, starting from two ore produces three after one round trip and four after the next. A repeated increase follows only while the cycle remains eligible and capacity permits it. Add one consumed fuel unit per craft and the state no longer returns unchanged; omit that fuel and the audit falsely labels the loop free. If fuel is renewable, inspect that renewal path and its cost rather than pretending the question is settled. [C-11; C-17]

**Counterexample:** a deliberate growing workshop may be built around productive cycles. Eliminating every positive resource return destroys the intended growth experience. The question is whether the rate, access and side effects fit an approved local budget—not whether a conversion produces anything useful. [C-15]

### Illustrative: stable totals conceal access failure

Two players jointly hold 100 coins. Initially each has 50; later one has all 100. The aggregate stock is identical. If a required, nonshareable item costs ten and the second player has no feasible earning or transfer route, that player's access differs despite the stable total. This logical counterexample refutes “stable supply proves fair or satisfying access,” without asserting that redistribution is the correct design intervention. Scarcity, loss or unequal roles may be intentional and require a declared local purpose. [C-04; C-13; C-17]

## Failure modes and constraints

**Accounting failure:** reservations treated as sinks; item deletion reported as coin deletion; old/new offer versions pooled; duplicated pending grants; changed units or population boundaries. Candidate correction: reconstruct the exact transition and its ownership/version before changing a rate. [C-02; C-19]

**Incentive failure:** the most effective way to progress bypasses the intended activity or transfers repetitive labor to another person. Candidate correction: inspect whether it is a welcome strategy, a freely chosen specialization or an obligation created by gating; do not ban efficiency reflexively. [C-12; C-15]

**Access and comprehension failure:** essential costs cannot be understood without rapid reading, color discrimination or mental currency conversion; a required sink takes a struggling player below any feasible recovery path. Candidate correction: provide understandable quantities, optional explanation and an intentional recovery/failure design. Required access supports are not rewards to be earned. No universal minimum text sizes or target dimensions are asserted. [C-16]

**Ethical failure:** a sink or expiring currency encourages return despite a person's wish to stop, or obfuscates costs behind multiple conversions. A numerically stable flow does not disprove that possibility. Proposed review examines the full commitment/refusal/return sequence and production/support burden; it does not infer malicious creator intent. [C-05; C-13; C-16]

**Production failure:** each recipe, currency and exception adds authoring, localization, version migration and support obligations. A small team may prefer a few explicit exchanges over a general market. Old offers, rounding and interrupted operations require separate design cases; this is not authorization to change a server or harness. [C-12; C-19]

## Playtest and validation

**Proposed, not performed.** The following separates model properties from player experience; no sample, test result, economy stability certificate or exploit-free claim exists. [C-18]

**State/route audit:** enumerate a bounded recipe/transfer subset on paper or in a future approved model. Vary zero, just-below, exact and just-above requirements; full storage; outstanding reservations; old/new rule versions; cancellation; resumption; single versus batch rounding; and resource-binding transitions. Check opening-to-closing reconciliation and whether supposed closed cycles restore every prerequisite. Failure means the rule model or specification requires revision. Passing the subset does not prove a complete implementation or all possible interactions safe. [C-02; C-11; C-19]

**Scarcity and choice comparison:** in a future consented prototype, compare a proposed sink with no sink or a targeted source adjustment. Hold the available activities and target content constant where possible. Include people with differing prior knowledge, available time and access configurations. Observe rule prediction, feasible options, unwanted repetition, successful refusal and the reasons for spending or not spending. Do not infer comprehension from a preferred purchase. A stock target is only one diagnostic; reject the intervention when it destroys an essential route or adds unacceptable burden without the intended decision value. [C-04; C-13; C-16]

**Trading comparison:** assess whether a proposed market gives useful specialization relative to direct or NPC acquisition. Actual networks create interference: one participant's trade changes another's options. A future design may need whole-group comparison or a carefully bounded offline representation, not naive player-level randomization. Predeclare which indirect effects matter, record missing transactions and avoid concluding “no effect” from an imprecise estimate. This is a methodological proposal; no actual market experiment occurred. [C-12; C-18]

**Disconfirmation:** retain or simplify a profitable production path when participants find it valuable and its declared costs are acceptable; revise the audit if it incorrectly flags such paths. Reject “economy improved” when an aggregate price target is met but access, comprehension or the intended experience worsens. An inconclusive comparison leaves the claim unresolved. [C-13; C-15; C-18]

## Claim ledger

| Claim | Exact claim / classification | Support and precise locator | Applicability, uncertainty and next question |
|---|---|---|---|
| C-01 | Define resources, units, ownership and boundary before classifying creation, destruction, transfer or conversion. **inference**. | Working model below; methodological context 007, Resource Flow / Communication of State. | High for bookkeeping necessity; not a universal economy taxonomy. Is the NPC reserve inside the chosen boundary? |
| C-02 | Within a declared boundary, internal transfers cancel from aggregate stock while creation, destruction and crossing flows do not. **inference**. | Stock identity and worked treasury example below; arithmetic, not a measured economy result. | High under explicit units and complete accounting; hidden grants, imports or inconsistent timestamps break the model, not the identity. |
| C-03 | Dormans models resource and state flows with artificial players and warns that its abstractions do not establish a perfectly balanced implemented game. **observed-example** of a modeling report. | 007, printed pp. 2–3 and 6–7; Figure 1 and Discussion. | High for report scope; no F03 simulation or human evidence. F01 source-08 is the same paper, not an independent confirmation. |
| C-04 | Scarcity and affordability must specify an actor, goal, available means and time/state context. **inference**. | Original definitions and distribution counterexample. | High logical distinction; no measured player willingness-to-pay or utility claimed. Abundant global stock may be inaccessible to a particular player. |
| C-05 | Choose sinks and currencies for the decisions they enable and burdens they impose, rather than targeting flow balance alone. **hypothesis**. | Option table and C-02/C-04; 005 practitioner guidance is adjacent, not validation. | Low causal confidence. A finite self-contained game may require no replenishing sink at all. |
| C-06 | Currency growth, an individual item-price increase and a broad fixed-basket price change are different measurements. **inference**. | Definitions and price-basket reasoning below; no external economic index calculated. | High for distinction; any chosen index has coverage/quality/weight assumptions. Which access outcome would a price movement change? |
| C-07 | Jagex’s dated update distinguishes tax deletion, funded item removal and old/new offer rules. **observed-example** of a document. | 006, Grand Exchange Tax and Improvements to Item Sinks. | High for announcement only; no current-rule certification or observed post-change effectiveness. |
| C-08 | Jagex explains its intervention as responding to currency inflow outpacing sinks. **practitioner-heuristic** / stated developer rationale. | 006, Why Change the GE Tax Rate? | Moderate for the stated rationale; quantitative verification of that diagnosis is not supplied in the inspected update. Not independent evidence of benefit. |
| C-09 | The inspected market manuscript reports context-specific intervention estimates, not a universal no-cost tax result or player-welfare result. **empirical-evidence**. | 011, §3.3; §§4.1–4.2; §5; Appendix A.1–A.3. | Moderate for reported local estimates; low for broader transfer: observational identification, partial item records, selected controls and source inconsistencies. No F03 replication; no basis for transfer to 2025 rate change. |
| C-10 | Retain the manuscript’s scope/wording, date and price-bound issues rather than silently resolving them. **inference**. | 011, Abstract versus §4.1; Introduction NPC wording; Appendix A.3. F03-CON-02/03/04. | High that inspected passages differ; lower certainty about author-intended correction. A practical-significance threshold is not specified. |
| C-11 | A repeatable conversion that returns its complete prerequisite state while increasing spendable stock is an effective source; an omitted consumable or state cost can invalidate that classification. **inference**. | Original transformation examples; 007 motivates explicit state, not the arithmetic proof. | High under stated rules, not proof of real exploit availability or malicious intent. Nonlinear rounding and batch limits need separate cases. |
| C-12 | Crafting/trading can serve planning and specialization but can also replace interesting decisions with processing burden or mandatory intermediation. **hypothesis**. | Design alternatives and failure cases; creator accounts provide existence, not efficacy. | Low causal confidence; compare direct acquisition, smaller recipe sets and optional trade. Which interaction is actually valued? |
| C-13 | Aggregate stability is insufficient to establish affordable participation, viable choices or a satisfying economy. **inference**. | Stock-distribution counterexample and C-04/C-06; F07 evaluation candidate §Balance has multiple objectives. | High as a counterexample to sufficiency, not an estimate of harm. Player-level outcomes remain unmeasured in F03. |
| C-14 | Transferable purchased value creates fraud and reversal considerations in Valve’s platform guidance. **practitioner-heuristic**. | 005, Anticipating Fraud. | Moderate for platform guidance; no fraud rates estimated. The document’s platform-specific timing values are not generalized into F03 requirements. |
| C-15 | Judge an apparent exploit against declared resource budgets, consent and intended creative play, not profitability alone. **hypothesis**. | Original policy proposal; C-11 and PAT-02. | Low efficacy confidence. Production loops may intentionally create value. No creator intent is inferred for a named game. |
| C-16 | Make committed, available, expiring and recoverable quantities understandable and audit refusal costs. **hypothesis**. | F01-PAT-01 corrected affordability probes; F07 ethics §§Audit both offer/refusal; P01 corrected presentation scope; 005 adjacent practitioner rationale. | Low for experiential efficacy; high that total-owned and spendable quantities can differ. No numerical accessibility settings or formal certification imported. |
| C-17 | The treasury, recipe and distribution examples are synthetic accounting counterexamples, not game observations. **inference**. | Worked examples and their declared invented assumptions. | High arithmetic confidence under stated inputs; no empirical outcomes, production simulations or player tests. |
| C-18 | Audit state integrity and player interpretation separately; a correct ledger does not establish a desirable incentive. **hypothesis**. | Proposed validation protocol; C-02/C-03/C-13; inspected F07 evaluation framework. | Low for workflow efficacy; no tests performed. Author static file checks are not economy validation. |
| C-19 | Rule-version and settlement boundaries can change whether two apparently identical transactions are equivalent. **inference**. | 006, grandfathered offers; original reservation/settlement analysis. | High logical distinction, not engineering instructions. Exact live-state behavior needs separate implementation validation. |
| C-20 | Progression grants must be analyzed as economy inputs, while later item use and opportunity cost belong in the player-experience diagnosis. **hypothesis**. | Cross-topic synthesis with TOP-01 and PAT-01; C-02/C-05. | Low causal confidence. Predictable acquisition may compress demand or become a chore; neither consequence is established here. |

## References

Temporary source candidates are reused within F03. The inspected first-wave version of Dormans is explicitly mapped as a same-source candidate; central deduplication remains pending. Developer announcements, researcher analyses and illustrative calculations are not interchangeable evidence.

### GDR-SRC-20261010-F03-005 — Microtransactions (In-Game Purchases)

**Citation:** Valve. unknown. *Microtransactions (In-Game Purchases)*. Steamworks Documentation.

**Verified route:** [Microtransactions (In-Game Purchases)](https://partner.steamgames.com/doc/features/microtransactions).

**Version / access:** Mutable online documentation inspected on 2026-10-10; no edition/update date exposed. Checked 2026-10-10; `access: relevant-excerpt`. Platform-provider practitioner guidance; cited advice is not a universal formal standard.

**Inspected locators:** Anticipating Fraud; Considerations for in-game economies and best practices, especially items 1–2 and concluding metrics paragraph.

**Claims in this artifact:** C-14; adjacent practitioner rationale for C-05/C-16.

**Limits / independence:** The selected recommendations supply no controlled outcome measurements. The linked Kyle Davis talk was not viewed. /documentation/MicroTxn is an access alias, not another independent source. Platform-specific numerical fraud restrictions are not generalized here.

**Rights:** Valve documentation; paraphrase only. No implied redistribution license or platform certification.



### GDR-SRC-20261010-F03-006 — Yama CAs & More!

**Citation:** Jagex. 2025-05-29. *Yama CAs & More!*. Old School RuneScape official news.

**Verified route:** [Yama CAs & More!](https://secure.runescape.com/m=news/yama-cas--more?oldschool=1).

**Version / access:** Dated 29 May 2025 update announcement; not asserted to be the current 2026 rule set. Checked 2026-10-10; `access: relevant-excerpt`. Firsthand policy/configuration announcement and developer rationale; observed document.

**Inspected locators:** Grand Exchange Tax → Why Change the GE Tax Rate?, Here’s what’s changing, Improvements to Item Sinks; final exemption paragraph.

**Claims in this artifact:** C-07, C-08, C-19.

**Limits / independence:** No post-change causal evaluation or player welfare data in the inspected section. The announced 2025 rate change is not the 2021 intervention analyzed by 011. Developer goals are not measured effects.

**Rights:** Jagex copyrighted news; paraphrase only.



### GDR-SRC-20261010-F03-007 — Simulating Mechanics to Study Emergence in Games

**Citation:** Joris Dormans. 2011. *Simulating Mechanics to Study Emergence in Games*. AAAI; AIIDE technical report WS-11-19, pp. 2–7.

**Verified route:** [Simulating Mechanics to Study Emergence in Games](https://ojs.aaai.org/index.php/AIIDE/article/download/12477/12336/16005). DOI: `10.1609/aiide.v7i3.12477`.

**Version / access:** Six-page published 2011 paper. Checked 2026-10-10; `access: relevant-excerpt`. Original modeling method and artificial-agent simulation report; not human-player evidence.

**Inspected locators:** Printed pp. 2–3, Resource Flow and Communication of State; Figure 1 on p. 3; pp. 6–7, Simulating SimWar and Discussion; PDF pages 2 and 6 visually inspected.

**Claims in this artifact:** C-03; model vocabulary informing C-01/C-11.

**Limits / independence:** Resource/state abstraction omits spatial/tactical detail; no F03 model was executed. Exact URL/edition also occurs as GDR-SRC-20261010-F01-08 in inspected first-wave bytes: cross-batch identity reconciliation remains pending, not independent corroboration.

**Rights:** AAAI copyright; paraphrase only; no diagrams or PDF redistributed.



### GDR-SRC-20261010-F03-011 — Market Interventions in a Large-Scale Virtual Economy

**Citation:** Senan Hogan-Hennessy, Peter Xenopoulos, and Claudio Silva. 2022-10-14. *Market Interventions in a Large-Scale Virtual Economy*. arXiv.

**Verified route:** [Market Interventions in a Large-Scale Virtual Economy](https://arxiv.org/abs/2210.07970).

**Version / access:** arXiv:2210.07970v1, 14 October 2022; 12-page manuscript; peer-review status not independently established. Checked 2026-10-10; `access: relevant-excerpt`. Primary observational item-market analysis with regression discontinuity/kink and difference-in-differences identification, not randomized players.

**Inspected locators:** PDF pp. 1–3, Introduction and §3.3; pp. 4–6, §§4.1–4.2, Figures 2–5; p. 8, §5 limitations; pp. 11–12, Appendix A.1–A.3 and Table A1. PDF pages 5, 6 and 12 visually inspected.

**Claims in this artifact:** C-09, C-10 and F03-CON-02/03/04; not an intervention recommendation.

**Limits / independence:** Paper uses Wiki/RuneLite-derived item-market records; no player-level welfare evidence. Exact analysis not replicated. Abstract/body practical-significance wording, an Appendix A.3 date, and NPC price-bound terminology require reconciliation (F03-CON-02/03/04). PDF route: https://arxiv.org/pdf/2210.07970 . Same market context as 006, different intervention period, not replication of 2025 change.

**Rights:** Author manuscript; redistribution license not established. Paraphrase only; no PDF, figures or underlying data redistributed.


## Open questions and change history

Open: F02 decision/difficulty bytes; direct access/distribution data; multiplayer network effects and bargaining; informal trade and fraud incidence; cultural interpretations of currency/ownership; representative accessibility checks; source/model replication; and longitudinal consequences of changing sinks or retirement rules. Full economic and player-welfare coverage is not certified by this file.

The most consequential source dispute is the scope of the market paper's tax-volume conclusion. Keep its body estimates, the practical-importance ambiguity and Appendix date issue visible until reviewed. The analytical price-bound counterexample must not be mistaken for an author-approved correction. Additional optional-sink and recovery techniques remain queued child work, not discarded or silently expanded into this packet.

**History:** 2026-10-10; version 0.1.0; candidate_revision initial-research-1; predecessor and supersession null. Author self-review distinguished transfer from destruction, narrowed intervention claims and retained productive-loop counterexamples. Exact byte hash is in the integrity receipt. **Gate C pending independent review; Gate D host tests not run; Gate E not passed.**

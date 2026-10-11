---
id: GDR-CAND-20261010-G05-PAT-02
kind: pattern
title: Recoverable expenditure window
version: 0.1.0
status: draft
candidate_revision: initial-capture-1
attempt_id: G05-initial-capture
identity_scope: temporary-run-scoped
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
coverage_state: open
aliases:
- conditional resource regain
- spend-and-regain window
tags:
- resource commitment
- recovery
- risk communication
- cooperative externalities
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-P02-TOP-02
related_patterns:
- GDR-CAND-20261010-F07-PAT-02
related_genres:
- GDR-CAND-20261010-G05-GEN-01
- GDR-CAND-20261010-G05-GEN-02
source_ids:
- GDR-SRC-20261010-G05-004
- GDR-SRC-20261010-G05-010
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
integrity_record: ../reviews/full-run-20261010-g05-integrity-receipt.md
---

# Recoverable expenditure window

**Draft research candidate, not released guidance.** Definitions and application recommendations below are working inferences or hypotheses, not approved studio choices or universal genre requirements. Source-supported descriptions, creator intentions, and empirical results are separated in the claim ledger. No game was played, no recording was analyzed, and no prototype or player test was run for G05. Public game cases are observations of documentation artifacts, not firsthand observations of their executable behavior.

The [G05 review packet](../reviews/full-run-20261010-g05-review-packet.md) records the inspected input snapshot, selected dependency hashes, source relationships, open coverage, and gates. Existing reviewed dependencies remain unreleased and are not repackaged here. A link to a packet dependency record does not pretend that its underlying topic is included in this four-candidate set.

## Purpose

Make a deliberate resource expenditure partly or wholly recoverable through a defined subsequent action while preserving an explicit remaining risk. The proposed player-facing benefit is a more legible choice between conserving a resource and committing it with a conditional recovery opportunity. This is **not** a promise of easier play, universally desirable aggression, or consequence-free experimentation. [C-03, C-05]

The candidate is deliberately narrower than “recoverable health.” It applies when **the player's intentional expenditure creates the amount at risk**. Injury recovery, checkpoint restoration, revival, configuration rollback, and undo are different contracts. A window can be bounded by an event or eligibility condition; it need not use a timer. [C-02, C-03]

## Context and prerequisites

Use only when the intended experience justifies a resource-spending decision and the system can represent available resources, outstanding recoverability, qualifying recovery, and final loss without ambiguity. State who controls the recovery opportunity and whether a teammate, opponent, stage transition, or last target can close it. Do not silently promise recoverability when no valid recovery opportunity can occur. [C-03, C-04]

A clear baseline without the feature is required for comparison: fixed cost, no cost, a replenishing resource, or a different declared consequence. The design must be able to explain and test the difference. Needed controls and cues must be usable without requiring an unrelated access burden. The team must be willing to reject the mechanic if its apparent benefit depends on misreading the resource display or pressuring another participant. These are proposed prerequisites, not adopted studio policy. [C-04–C-06]

## Mechanism and evidence

The direct source is the SoR4 creator interview's voluntary special-action health expenditure and conditional regain description. The TEKKEN system page is a **contrast** involving recoverable injury; it is not a second independent validation of the same expenditure recipe. Neither source supplies an original player comparison establishing the proposed benefit. [C-01, C-02]

| Link in the proposed mechanism | Support | Limit and competing explanation |
|---|---|---|
| Spending creates a distinguishable recoverable amount | A documented implementation account supplies a concrete feasibility example [C-01]. | Exact current build and edge cases were not observed. |
| Showing available versus conditionally recoverable resources can support a correct prediction | Accounting and fact-preserving communication rationale [C-03, C-04]. | A more elaborate display may itself confuse; no comprehension effect is established. |
| A feasible regain opportunity may make an otherwise avoided expenditure worth considering | Conditional incentive reasoning [C-05]. | Players may misunderstand the loss, or the move may simply be overpowered. Use alone would not identify the cause. |
| Forfeiture or closure can retain a consequence rather than turning expenditure into a free loop | Stated contract logic [C-03]. | A trivially farmed recovery action can remove the intended cost; an inaccessible action can make the apparent opportunity illusory. |
| Other actors' effects on recovery can change cooperation or competition | Opportunity-dependence inference [C-06]. | It can encourage coercion, target monopolization, or unwanted carrying rather than joint agency. |

Only the existence of the documented mechanism is directly supported. The proposed preference, comprehension, and experience benefits remain hypotheses. [C-05]

## Recipe

1. **State the local decision.** Identify the action being avoided or overused and the intended resource commitment. Distinguish misunderstanding, inaccessible activation, absent opportunities, preference, and payoff before selecting this pattern. Exit if a simpler explanation or control fix addresses the actual problem. [C-04, C-05]
2. **Specify resource states.** Define available amount, outstanding recoverable amount, and final expenditure. Define a cap and the order of simultaneous events. A regained amount must not be counted twice as both available and still recoverable. This is a proposed accounting invariant, not a claim about an uninspected executable. [C-03]
3. **Define what creates eligibility.** Identify eligible expenditures, whether multiple expenditures accumulate or replace outstanding eligibility, and what happens when resources are insufficient. Do not treat ordinary injury as expenditure merely to fit the pattern. [C-02, C-03]
4. **Define the recovery action and its opportunity.** Specify which action restores how much, who may perform it, the eligible target/state, and whether it can be repeated. Inspect last-target, empty-space, ally-interference, and mode-transition cases. If an opportunity cannot be made legible and credible, use a different cost contract. [C-04, C-06]
5. **Define closure and forfeiture.** State whether a hit, interruption, transition, time bound, voluntary stop, or another event ends recoverability. Choose only conditions relevant to the intended commitment; do not add an arbitrary timer because the pattern is called a window. Explain what is retained after closure. [C-03, C-04]
6. **Communicate the contract before and during commitment.** Distinguish spendable from conditionally recoverable resources, the qualifying action, and the event that ends eligibility. Use the corrected P02 fact-preserving approach; a color change alone is not a demonstrated complete alternative. Avoid calling recovery guaranteed when it is contingent. [C-04]
7. **Inspect dominance and externalities.** Compare the resource balance across ordinary, repeated, boundary, and adversarial sequences. Ask whether one actor can deprive another of every recovery opportunity, whether an easy target can be farmed, and whether forfeiture punishes unrelated interruption. No engine code or gameplay sequence is executed by this document. [C-03, C-06]
8. **Compare with a simpler baseline under separate authorization.** Keep action capability and encounter conditions comparable where possible. Measure comprehension, decision use, access, social effects, and retained commitment independently. If tuning multiple variables is unavoidable, describe the whole treatment instead of attributing its effect to recoverability alone. [C-05, C-07]
9. **Keep, revise, or exit.** Retain only for the conditions supported by the later evidence and local decision. Exit when accounting is ambiguous, eligibility is predictably unavailable, access fails, worthwhile choice does not improve, or the intended cost is erased. No research gate automatically authorizes implementing this disposition. [C-07]

### Adjustable variables

Adjust expenditure amount, recoverable fraction, cap, stacking policy, eligible recovery actions, amount per recovery event, target eligibility, closure/forfeiture events, team ownership, stage carry-over, and cue detail. Any numeric values are local design/test parameters, not inherited from a game example. A timer is optional; a disclosed event-bounded contract may fit better. More generous recovery is not automatically more accessible or more meaningful. [C-03–C-06]

## Worked examples

### Illustrative accounting example — not a game recommendation

Use arbitrary resource units solely to expose the state transitions. Start with **10 available, 0 recoverable**. An eligible expenditure of **3** produces **7 available, 3 recoverable**. A qualifying action restores **2**, producing **9 available, 1 recoverable**. If the next event closes eligibility, the remaining **1** is no longer recoverable; available resources remain **9** unless that event separately changes them. A damaging event could do both, but its damage and forfeiture must be represented as distinct consequences in a specified order.

A second qualifying action cannot restore the already recovered **2** again. When the last target disappears before the remaining recovery action, the design needs an explicit closure or alternate eligibility rule; leaving a misleading recoverable display is not an acceptable explanation. These values are invented for accounting clarity, not balancing thresholds or observed source-game values. [C-03, C-04]

### Illustrative cooperative encounter

A fictional character spends a defensive resource to separate an approaching group. Regain is available only through subsequent contact with an eligible opponent. An ally defeats the remaining eligible target. The issue is not automatically that either player made a poor tactical choice: the resource contract depends on a shared opportunity.

Candidate alternatives include a different qualifying action, shared eligibility, a different closure rule, or a fixed cost that avoids the social dependence. Each changes incentives and requires its own test. The choice should be informed by the intended cooperation and commitment, not by a blanket mandate to refund the spender. A group that likes coordinated resource setups may prefer the dependence; another may find it coercive. These are hypothetical possibilities, not player findings. [C-05, C-06]

### Illustrative non-combat transfer

A route-planning challenge lets a player spend an optional planning resource and regain an outstanding portion by completing a declared observation task before leaving the area. The same accounting questions apply, but combat-specific hit/target rules do not. If the observation task becomes obligatory busywork or reveals information the puzzle intends to withhold, use a different cost. This example demonstrates the candidate's genre-neutral formulation; it is not an inspected implementation or validated transfer. [C-03, C-05]

## Tradeoffs and alternatives

A fixed cost is simpler to explain and may preserve a clearer commitment. An automatically replenished resource can reduce opportunity competition but changes scarcity. No cost may suit a permissive power fantasy. A separate recovery action can make eligibility easier to understand while adding repetition or production cost. A checkpoint changes the persistence horizon rather than the expenditure itself. Evaluate these as different contracts, not as a ladder from harsh to good design. [C-02, C-05]

The pattern adds state, communication, tuning, edge-case review, localization, and interaction testing. It may make an aggressive option dominant or turn a nominally defensive action into an obligation to pursue recovery. Such effects might suit a declared mode, but they must not be advertised as a neutral reduction in difficulty. [C-05, C-06]

## Failure cases

| Failure | Observable warning for a future test | Candidate response |
|---|---|---|
| Resource-state confusion | Players plan as though outstanding recovery is already spendable | Simplify states/cues or choose a fixed cost; do not infer comprehension from use rate. |
| Free recovery loop | Repeated expenditure/regain removes the intended opportunity cost | Re-examine the contract, eligibility, and cap; do not hide a new forfeiture condition. |
| Illusory opportunity | Eligible actions are absent or unusable in routine end-of-stage/access conditions | Change eligibility, openly close it, or omit the mechanic. |
| Cooperative coercion | Players must demand targets or delay partners to avoid predictable loss | Redesign shared opportunity dependence or select a different contract. |
| Unrelated punishment | Stopping or interruption forfeits unrelated accumulated progress | Separate the resource commitment from unrelated consequences. |
| Difficulty misdiagnosis | Greater recovery changes usage but the original misunderstanding or input failure remains | Return to the F07 diagnosis and test the actual barrier. |

These are possible mechanisms and proposed observations, not established prevalence or harm findings. [C-03–C-07]

## Counterexamples and do-not-use conditions

Do not apply this recipe to ordinary recoverable injury, revival, or settings restoration without a new explicit contract analysis. Do not use it when the experience depends on clear irreversible expenditure, when the player cannot reasonably perceive the conditional amount, or when recovery requires access demands that have not been addressed. A mode built around scarce one-time commitments may be weakened rather than improved by the pattern. [C-02–C-05]

A technically valid resource loop can still be unwanted. Conversely, a powerful recovery loop may be deliberate in a spectacle-focused mode. The local objective and counterplay expectations decide what needs testing; the genre name does not decide which condition wins. [C-05, C-06]

## Proposed playtest — not performed

**Question:** compared with the selected simpler contract, does this explicitly communicated conditional regain create a worthwhile decision without unacceptable confusion, exploitability, or participation cost? After separate authorization, use a bounded scenario with the relevant resource and opportunity conditions. Include participants with the prior knowledge, input configurations, and intended solo/cooperative roles that may change the outcome. Treat interacting teams and repeated observations appropriately rather than counting all actions as independent samples. [C-07]

Before acting, ask participants to predict what is spendable, what is recoverable, what would restore it, and what ends eligibility. Observe choices separately from these predictions. Compare ordinary opportunities with last-target, transition, interrupted, and partner-controlled opportunities. Record execution/access failures, misunderstanding, hoarding, repetitive farming, voluntary role choices, and reported pressure. No participant or numerical threshold is specified by default. [C-04, C-06, C-07]

**Falsifiers and disposition:** reject a claimed comprehension benefit if it depends on moderator explanation unavailable in the game; reject a meaningful-choice claim if a free dominant loop replaces the intended tradeoff; reject the cooperative application if willing participants must repeatedly surrender their own opportunities to sustain another's recovery without an accepted design rationale. If a simpler fixed cost supports the objective with fewer problems, prefer it. An inconclusive comparison narrows the claim; a nonsignificant difference is not proof of equivalence. [C-07]

## Claim ledger

| ID | Claim/class | Source or dependency and locator | Confidence and limit |
|---|---|---|---|
| C-01 | A creator interview describes voluntary expenditure with conditional regain — `observed-example` of documented rules | 010 special-action health paragraph | High for attribution; one direct implementation account, not firsthand executable verification. |
| C-02 | Recoverable injury and voluntary expenditure are distinct contracts — `inference` | 004 Recoverable Gauge contrasted with 010; F02 recovery distinctions | Moderate conceptual support; 004 is a countercase, not another validation of this recipe. |
| C-03 | Explicit resource accounting and closure are needed to define the proposed pattern — `inference` | Stated accounting model motivated by C-01/C-02; illustrative example | High for consistency within the stated model, not for enjoyment or any game's implementation. |
| C-04 | Communicating conditional eligibility may support informed prediction — `hypothesis` | Corrected DEP-P02-Feedback/Cues; DEP-F02-Decision | Low for measured benefit; added state can increase confusion. |
| C-05 | Conditional recovery may support a worthwhile expenditure decision — `hypothesis` | Mechanistic reasoning from C-01; DEP-F07-Diagnosis | Low: no comparative efficacy study; strength or misunderstood cost can explain increased use. |
| C-06 | Recovery opportunity controlled by other actors can change social and competitive incentives — `inference` | Opportunity-dependence reasoning; DEP-F07-Ethics/Safe-Exit | Moderate possibility, unknown incidence or preferred arrangement. |
| C-07 | The proposed comparison can challenge comprehension, choice, and externality claims — `hypothesis` | DEP-F07-Evaluation/Diagnosis and explicit tests | Low until executed; no power, prevalence, or universal success threshold asserted. |

## Related entries and history

Genre applications: [Beat-em-up](../genres/beat-em-up.md), `GDR-CAND-20261010-G05-GEN-02`, and conditional [Fighting](../genres/fighting.md), `GDR-CAND-20261010-G05-GEN-01`. Relevant reviewed records: [F02 decision](../reviews/full-run-20261010-g05-review-packet.md#dep-f02-decision), [P02 cue alternatives](../reviews/full-run-20261010-g05-review-packet.md#dep-p02-cues), and [F07 safe exit](../reviews/full-run-20261010-g05-review-packet.md#dep-f07-safe-exit). This recipe neither duplicates difficulty adaptation nor turns match reversal into a recovery right.

Version `0.1.0`, revision `initial-capture-1`, 2026-10-10. First capture; predecessor/supersession null. Current authoring owner BH-GDR-Genres; proposed conceptual owner Foundations-and-Systems requires coordination. The narrower pattern boundary, limited source base, current-build behavior, other implementations, access, and player outcomes remain open. Independent review and release have not occurred. No resource system was implemented or tested.

## References

All records below were accessed on **2026-10-10 (America/Los_Angeles)**. Access is `relevant-excerpt`: the identified HTML text was inspected, not linked videos, executables, or a presumed current build. Web-text line locators describe this retrieval and are paired with stable section descriptions. Copyright remains with the respective rights holders; no redistribution license was inferred. This artifact paraphrases source text and embeds no third-party images. Source identities are provisional, reused within G05; cross-batch URL/edition deduplication remains pending.

### GDR-SRC-20261010-G05-004
**Bandai Namco Entertainment. [TEKKEN 8 — Battle System](https://tk8.tekken-official.jp/en/battle/system.php).** Date: Publication/update unknown. Publisher/host: tk8.tekken-official.jp. Edition/build: Official unversioned system overview; exact game build unpinned. Source type: Official developer/publisher game documentation. Access: `relevant-excerpt`.
**Locator:** “Recoverable Gauge” / recovery discussion, lines 108–125; Rage Art interaction, 148–150. **Claims:** C-02 countercase only. **Limits:** Supports the described health-state contract, not the current balance of all moves, a universal aggression benefit, or an equivalence with voluntary resource expenditure. **Independence:** TEKKEN 8; shared publisher with 005, 006, 008, 009.

### GDR-SRC-20261010-G05-010
**Gillen McAllister, interviewer; Jordi Asensio (Dotemu), Cyrille Lagarigue (Guard Crush), and other credited creators. [Streets of Rage 4: How three studios revived a legendary series](https://blog.playstation.com/2020/04/30/streets-of-rage-4-how-three-studios-revived-a-legendary-series/).** Date: Published 2020-04-30; page also displays update 2021-09-10. Publisher/host: blog.playstation.com. Edition/build: Launch-era creator interview; platform article, exact executable build unpinned. Source type: Firsthand multi-creator interview. Access: `relevant-excerpt`.
**Locator:** Special health and Star moves, 85–90; Story/assist structure, 93–96; enemy roles, 132–134; co-op, 155–157; encounter iteration, 171–175. **Claims:** C-01; motivation for C-03/C-05, not evidence of their benefits. **Limits:** Described rules and production reasoning only. No player study, causal success claim, or current patch verification. Statements by multiple interviewees are not multiple independent evaluations. **Independence:** SoR4: Dotemu / Guard Crush / Lizardcube; publisher overlap with TMNT, different development team.

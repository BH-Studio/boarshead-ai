---
id: GDR-CAND-20261010-F02-PAT-01
kind: pattern
title: Visible opportunity-cost comparison
version: 0.1.0
status: draft
candidate_revision: initial-capture-1
attempt_identity: F02-local-attempt-01
predecessor_sha256: null
supersedes: null
change_summary: Initial F02 capture; preserves inspected first-wave corrections; no
  prior batch artifacts resubmitted.
owner_project: BH-GDR-Foundations-and-Systems
run_id: GDR-FULL-20261010
batch_key: F02
updated: '2026-10-10'
evidence_checked: '2026-10-10'
aliases:
- forgone alternative display
- remaining-capacity comparison
- opportunity-cost reminder
tags:
- decision-design
- opportunity-cost
- resources
- information
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F02-TOP-02
related_patterns:
- GDR-CAND-20261010-F07-PAT-02
- GDR-CAND-20261010-F01-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-F02-005
reviewer: null
approved_by: null
approved_date: null
---

# Visible opportunity-cost comparison

**Draft pattern; hypothesis-led application, not released guidance.** Candidate `GDR-CAND-20261010-F02-PAT-01`, version 0.1.0, revision initial-capture-1.

## Purpose

Help a player compare a resource-consuming action with a **real feasible alternative that the action displaces**, when price alone is not revealing the tradeoff. The desired outcome is better comprehension of the player’s own options, not higher savings, lower spending, longer deliberation or selection of the designer’s favored choice. [C-02]

This is distinct from broad consent/cost disclosure: the existing first-wave **Legible commitment and safe exit** pattern owns those obligations. This pattern adds a comparison of remaining capacity and forgone possibilities. It should not be used merely to rename a confirmation dialog. [C-03]

## Context and prerequisites

Use when a decision consumes limited time, capacity, currency, inventory space or another specified resource; at least one relevant alternative is known and genuinely feasible; and the game can keep the comparison current. The player must have an accessible way to understand both the focal action and the alternative. Identify the player’s goal without assuming every resource should be conserved. [C-02, C-03]

A prerequisite audit should establish: what is owned versus reserved; the actual available amount; whether the two actions can be combined; when the alternative expires; whether its value is certain; and whether the interface is entitled to reveal it. Do not expose hidden future content simply to manufacture an alternative. The current batch supplies no evidence that every player needs such a display. [C-03, C-05]

## Mechanism and evidence

| Proposed causal link | Support and limitation |
|---|---|
| Presenting an alternative use makes that use available for consideration. | Directly follows from truthful presentation, but attention and understanding still need checking. `inference` [C-03] |
| Salience changes how the decision is evaluated. | The inspected opportunity-cost meta-analysis reports a small average choice effect. Its evidence is predominantly hypothetical and consumer-focused, not gameplay efficacy. `empirical-evidence` [C-01; GDR-SRC-20261010-F02-005] |
| A truthful feasible comparison improves comprehension in this game. | An untested transfer; it may instead add distraction or merely frame the answer. `hypothesis` [C-02] |
| Better comprehension supports a choice fitting the player’s goal. | Plausible but not guaranteed: the goal may be changing, expressive or incompletely reported. Preference shifts are not a substitute measure. `hypothesis` [C-02, C-04] |

There is one primary research work supporting extraction of this pattern, not independent game-level validation. Its empirical studies are aggregated evidence, not separate sources inspected by F02. The complete recipe is a hypothesis. [C-01, C-02]

## Recipe

1. **Name the suspected misunderstanding.** Record what players are thought to overlook and what observation would distinguish that from knowingly preferring the focal action. Do not implement the display merely because an analyst dislikes their choices.
2. **Validate the resource state.** Identify total ownership, binding reservations and spendable capacity. Evaluate the focal action using the actual rule, including whether exact equality is allowed. Capture changes that can invalidate the comparison.
3. **Select a truthful alternative.** Prefer an alternative the player already selected or knows exists. Include its requirements and availability window. When no specific alternative can be validated, a neutral remaining-resource statement is safer than a fabricated opportunity.
4. **Show the comparison at the decision point.** Present current available capacity, the focal action’s cost, resulting capacity and the affected known alternative. Do not label decline as inherently smarter. Provide an accessible summary with optional detail rather than a compulsory long calculation.
5. **Separate planning from commitment.** Let the player inspect effects without accidentally executing them. Use the existing commitment/safe-exit guidance for destructive-action safeguards rather than creating a competing recipe here.
6. **Revalidate at commitment.** If state changed, update the comparison and explain the change; never execute against stale availability. Distinguish an invalid action from a valid action the player may reasonably decline.
7. **Evaluate comprehension and preference separately.** Ask what remains feasible before asking which action they prefer. Include contrasting states and a boundary case; keep entitled information and accommodations available.
8. **Keep, simplify or exit.** Retain the display only where the targeted problem is supported. Remove the specific alternative when it is stale, unknowable, misleading or answer-revealing. Remove the whole pattern when it adds burden without a locally meaningful comprehension benefit.

Steps are design inferences and proposed actions, not tested implementation. [C-02–C-06]

### Adjustable variables

Adjust resource units, planning horizon, reservation visibility, number of shown alternatives, whether the player pins an alternative, comparison detail, information persistence, timing and revalidation behavior. Set any numerical tuning locally and label it as a proposed test setting. A paper’s sample size or pooled effect is not a UI default. [C-03, C-06]

The **exit condition** is substantive: without a valid state model, a relevant known alternative and an accessible comparison, use a simpler truthful description and queue the unresolved decision. Do not simulate certainty with an invented list. [C-05]

## Worked examples

### Illustrative complete example: tool versus planned action

An invented system has 12 resource units, 3 reserved, and 9 spendable. A tool costs 6. A different action that the player pinned costs 4. The comparison states that buying the tool is permitted, leaves 3 spendable, and makes the pinned action unaffordable immediately unless the reservation or another constraint changes. It does not predict which option will be more satisfying. All numbers are illustrative, not balance recommendations. [C-03, C-04]

The designer first verifies that reservations are binding and exact spending is permitted. The summary then distinguishes **ownership**, **spendable capacity**, and **post-choice capacity**. The player may inspect the pinned action, buy the tool, revise a reservation through its legitimate process, or decline. The system rechecks state when the decision is committed. No time pressure is introduced solely to force acceptance of the comparison. [C-03]

For a proposed comprehension check, keep ownership at 12 and proposed cost at 6 while varying the reservation:

| Illustrative state | Available before purchase | Rule-based answer | What this checks |
|---|---|---|---|
| 7 reserved | 5 | Purchase is not permitted without changing a constraint. | Mistaking total ownership for available resources. |
| 3 reserved | 9 | Purchase is permitted; 3 remain available. | Repeating an always-reject answer is insufficient. |
| 6 reserved | 6 | Purchase is permitted; 0 remain under the explicit equality-allowed rule. | Confusing strict less-than with less-than-or-equal. |

Ask these predictions before preference and corrective feedback; vary values/order in later checks. A correct answer is not durable transfer evidence. The player can understand that a purchase is permitted and still reject it. This preserves the reviewed F01 correction without resending its artifact. [C-04, C-06]

### Illustrative extension: limited time

A player has one remaining work period. Two known actions each consume it. A comparison can show that selecting one excludes the other this period, but should not assign a common numerical “value” to exploration and social expression unless the game actually defines that objective. When the alternative depends on an unknown future event, show the uncertainty rather than a guaranteed benefit. [C-03, C-05]

## Tradeoffs and alternatives

The pattern costs state validation, comparison content, localization, accessible representation and testing of reservations and timing. Additional information may compete with the decision itself. A player-pinned plan can make the alternative relevant but can also become obsolete. A generic reminder is cheaper but less informative; a resource ledger may suffice for expert users; no intervention is reasonable when the tradeoff is already understood. These are conditional design tradeoffs, not measured comparative effects. [C-03, C-05]

A visible comparison can coexist with deliberate commitment, but neither pattern requires revealing every future outcome. The pattern should not convert expressive priorities into a single optimizer score. [C-02, C-05]

## Failure cases

| Warning sign | Competing explanation | Proposed correction |
|---|---|---|
| Players save more but cannot explain the forgone action. | Framing or perceived instruction, not comprehension. | Use neutral wording and explicit prediction measures. |
| Players repeatedly stop to compare irrelevant alternatives. | Burden or stale priorities. | Allow a relevant pinned comparison or remove unnecessary detail. |
| The displayed alternative was never feasible. | Invalid state model or hidden prerequisite. | Withdraw the claim; fix prerequisite validation before using the pattern. |
| Screen narration repeats a long changing list. | Access cost exceeds the intended benefit. | Design a concise stable summary with optional detail; validate with users. |
| Players correctly explain the tradeoff but choose the focal action. | Legitimate different goals, not necessarily failure. | Record preference without scoring it as misunderstanding. |

These are anticipated failure modes and corrections [C-04, C-05], not observed F02 results.

## Counterexamples and do not use conditions

Do not use this technique when the alternatives are intentionally unknown, the relevant resource is not scarce, no actual alternative exists, or the interface cannot keep the data truthful. A familiar transparent tradeoff may gain nothing from another panel. An expressive decision may be damaged by a display that appears to rank values the game never made commensurable. [C-05]

The strongest opposing explanation is that the display changes choices through suggestion without improving understanding. A successful shift in the designer’s preferred direction would therefore be insufficient evidence. The study motivating the pattern does not validate a game-wide benefit. [C-01, C-02, C-06]

## Playtest

**PROPOSED — NOT PERFORMED.** Compare cost-and-remaining-capacity information with the identical facts plus a truthful displaced alternative. Keep rules, prices, resources, option order and consequences constant, or explicitly counterbalance order. Separate a first-use comprehension comparison from a repeated-use burden comparison; prior exposure may teach the baseline group. [C-06]

Recruit for the intended audience with varied familiarity and relevant access/language needs. Keep accommodations in every condition. Measure factual prediction, identification of a feasible alternative, decision effort, erroneous commitments, perceived pressure and preference as distinct outcomes. Observe whether explanations reflect the intended constraint rather than memorized values.

Before testing, specify the practical comprehension improvement worth the interface/production cost, how unacceptable misunderstanding or pressure will be handled, and the uncertainty allowed for a decision. Do not invent a universal sample size or success percentage. Reject or simplify the pattern when choice shifts occur without better targeted understanding, when the alternative is systematically misleading, or when burden/pressure outweighs the locally specified benefit. A null result alone does not prove equivalence. [C-06]

## Claim ledger and sources

| ID | Claim and class | Source/locator or reasoning | Confidence, applicability and unresolved question |
|---|---|---|---|
| C-01 | Alternative-use salience affects choices in the inspected meta-analytic corpus. `empirical-evidence` | GDR-SRC-20261010-F02-005, §§2–4. | Moderate for that corpus; not gameplay comprehension or welfare validation. |
| C-02 | A truthful comparison may improve comprehension of a displaced option in games. `hypothesis` | Proposed bridge from C-01; the full causal chain above is untested. | Low; framing, burden and changing goals are competing explanations. |
| C-03 | A feasible-alternative comparison requires a valid resource, reservation and timing model. `inference` | Logical prerequisites of truthful comparison; worked arithmetic is illustrative. | High within the declared model, not an implementation guarantee. |
| C-04 | Rule predictions must be separated from preferences; contrasting probes reduce some copied-answer ambiguity. `inference` | Inspected F01 corrected example; analytical assessment design, not empirical efficacy. | Moderate; guessing, arithmetic, prior knowledge and presentation cues remain. |
| C-05 | Stale, unknowable or selectively framed alternatives can defeat the pattern’s purpose. `inference` | Information-contract analysis and counterexamples. | Moderate; severity and frequency require local evidence. |
| C-06 | The proposed comparison can test the targeted comprehension claim and opposing framing explanation. `hypothesis` | Author-designed test, no participants or outcomes. | Low until executed; carryover and demand effects remain. |

## References

Access date for every record below: **2026-10-10**. These are temporary source candidates. A repeated record is the same evidence, not additional corroboration. “Relevant-excerpt” identifies inspected substantive passages, not merely an abstract and not every linked supplement.

### GDR-SRC-20261010-F02-005

**Allegra Maguire, Emil Persson, and Gustav Tinghög.** [Opportunity cost neglect: a meta-analysis](https://link.springer.com/article/10.1007/s40881-023-00134-6). Journal of the Economic Science Association 9, pp. 176–192. **Publication/update:** 2023-07-02 version of record; 2023-12 issue. **Edition/version:** 2023 version of record, publisher HTML.

**DOI:** [10.1007/s40881-023-00134-6](https://doi.org/10.1007/s40881-023-00134-6).

**Access:** relevant-excerpt. **Source type:** original preregistered meta-analysis. **Inspected locators:** §§2–2.3 Methods; §3 Results and sensitivity analysis; §3.1 Moderation models; §4 Discussion; Rights and permissions. **Supports local claims:** C-01; provides the limited evidence basis for hypothesis C-02

**Limits:** Mostly hypothetical, consumer-domain decisions. Choices changing is not proof of improved welfare or game agency. Numerical reporting cautions are recorded in the packet. **Independence:** Aggregates Frederick et al. (2009) and later experiments; those underlying studies were not independently re-inspected or counted again. **Rights:** CC BY 4.0 stated; original paraphrase with attribution; no figures reproduced

## Related entries and history

Parent: [Decision design](../topics/decision-design.md), `GDR-CAND-20261010-F02-TOP-01`. Complement: [Challenge and difficulty](../topics/challenge-and-difficulty.md) for resource traps and recovery costs. Distinct inspected dependencies: F07’s commitment pattern and F01’s corrected learning-check pattern; see the [dependency register](../reviews/full-run-20261010-f02-review-packet.md#dependency-register). No genre entry is imported as a universal rule.

2026-10-10 — Initial F02 candidate, version 0.1.0; no predecessor asserted. Author self-review completed; independent review, host testing, gameplay validation and release not completed. No prior artifact is copied into this packet.

---
id: GDR-CAND-20261010-G20-PAT-01
kind: pattern
title: Away-state reconciliation
version: 0.1.0
status: draft
candidate_revision: initial-capture-1
attempt_identity: G20-local-attempt-01
predecessor_sha256: null
supersedes: null
change_summary: Initial complete G20 candidate; no predecessor or prior batch resubmitted.
owner_project: BH-GDR-Genres
run_id: GDR-FULL-20261010
batch_id: G20
updated: '2026-10-10'
evidence_checked: '2026-10-11'
date_basis: Run/local date 2026-10-10; source access and packaging recorded in UTC on 2026-10-11.
coverage_state: coverage-open
identity_scope: temporary run-scoped candidate; permanent allocation pending Library Coordination
aliases:
- offline progress explanation
- return-state reconciliation
- absence summary
tags:
- re-entry
- state-change
- automation
- uncertainty
- decision-support
related_topics:
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
related_patterns:
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-F07-PAT-02
related_genres:
- GDR-CAND-20261010-G20-GEN-01
- GDR-CAND-20261010-G20-GEN-02
- GDR-CAND-20261010-G20-GEN-03
source_ids:
- GDR-SRC-20261010-G20-009
reviewer: null
approved_by: null
approved_date: null
---

# Away-state reconciliation

**Candidate pattern · version 0.1.0 · low-confidence benefit hypothesis.** This is the only new pattern extracted for G20. It is not released, implemented or playtested. The proposed long-term shared owner is Foundations and Systems, coordinated with Presentation and Interaction; this draft’s authoring owner remains Genres until Coordination resolves ownership and overlap.

## Purpose

Help a returning player distinguish **what changed, what stopped, what remains uncertain and what can now be done** when relevant state evolved during absence. The intended outcome is a sound next decision, not more frequent returning or a more impressive reward celebration. [AWAY-C01]

The distinctive problem is reconstruction across an elapsed interval: **baseline → settled transitions → current state**, including consumption and blocked activity. This is narrower than a generic status panel, broader than a reward total, and different from teaching a forgotten rule or obtaining consent to a commitment. Use this candidate only when that distinction matters. [AWAY-C01, AWAY-C07]

## Context and prerequisites

The system has a legitimate way to identify the relevant prior state, applicable rules and authoritative current outcome. It can distinguish an incomplete calculation from a completed interval with no progress. There is an accountable state owner and a plan for handling missing or inconsistent information. A readable recap cannot compensate for untrustworthy accounting. [AWAY-C02]

There must be a player decision for which the change matters. An unchanged lesson, an instantly understandable decorative scene or an ambient experience without consequential next actions may need no reconciliation interface. In a live shared world, the team must know what continues while one player inspects the report; a unilateral pause must not be invented. [AWAY-C02]

Prerequisites include an accessible inspection route, a defined meaning for each reported quantity, an honest treatment of historical versus current rules, and enough production capacity to maintain that explanation through updates. This is a design contract to review with system owners, not engine architecture or code. [AWAY-C02]

## Mechanism and evidence limits

The official Melvor Idle v1.3 preview describes displaying progress while offline calculations complete. That supports a documentary example of distinguishing calculation status, not the causal effectiveness of this complete pattern. [AWAY-C03; GDR-SRC-20261010-G20-009]

| Proposed causal link | Support | Limit and rival explanation |
|---|---|---|
| Reliable baseline and settlement make a truthful difference report possible | Logical accounting prerequisite; reviewed P01 distinguishes stale and current information. | Correct accounting is necessary for an accurate report but does not show that the player needs the report. [AWAY-C02] |
| Distinct pending/partial/settled states prevent “still calculating” from being represented as “earned nothing” | The first-party preview supplies an example; the distinction follows from the states. | No comprehension benefit was measured in G20 or asserted by an inspected trial. [AWAY-C03, AWAY-C04] |
| Separating earned, spent and stopped exposes why the outcome differs from a naive forecast | Explicit model reasoning; a net total can conceal different paths. | Additional detail can overload or distract; a clear current-state view may be enough. [AWAY-C04] |
| Connecting the change to available action improves the next decision | Hypothesis extending reviewed interface reasoning. | The player may already understand, prefer observation, or choose a different objective. [AWAY-C04] |
| Optional detail and usable dismissal preserve a low-obligation return | Hypothesis constrained by reviewed safe-exit reasoning. | An accurate recap can still amplify regret or pressure. Disclosure does not make the underlying rule acceptable. [AWAY-C04, AWAY-C06] |

The **whole chain remains low confidence**. There is no evidence here for increased retention, reduced clinical stress, improved learning or any universal return interval. [AWAY-C04]

## Recipe

1. **Define the next decision.** Specify the question the player needs to answer: what can be afforded, why production stopped, whether a task completed, or which plan now fits their goal. If no consequential question depends on the interval, compare omission before adding a report. [AWAY-C01]
2. **Identify the baseline and authority.** Record the relevant prior state, ruleset and cutoff, the authority for settlement, and what is unavailable. Distinguish wall-clock absence from eligible simulation time. Do not substitute “time since screen closed” when that is not the governing rule. [AWAY-C02]
3. **Reconcile actual transitions, not a convenient forecast.** Separate gross production, consumption, conversions, limits and activity changes where material. Account for depletion or a cap without pretending that the final rate applied throughout the interval. No specific simulation method is prescribed. [AWAY-C04]
4. **Represent completeness honestly.** Distinguish calculating, partially known, settled and failed/unknown. Avoid showing a stale balance as current or a missing record as zero progress. When an unsafe action depends on unsettled data, use a truthful temporary restriction or a clearly safe alternative; do not fabricate success to remove friction. [AWAY-C02, AWAY-C04]
5. **Choose the smallest useful summary.** Prefer current balance, material change and the principal stopping reason over a recital of every event. Make necessary losses visible as well as gains. Offer a usable path to the detailed accounting when the summary cannot explain the next choice. [AWAY-C04]
6. **Connect information to action without prescribing preference.** Let the player inspect the stopped activity or compare available plans. Separate “this action is now possible” from “you ought to take it.” Do not convert unused production capacity into an admonition to return more often. [AWAY-C04, AWAY-C06]
7. **Provide proportionate continuation and recovery.** Allow dismissal or later inspection when safe; disclose whether a shared system continues meanwhile. On uncertainty, show what is known and the actual available recovery route. Do not promise replay, reversal or compensation that the system cannot support. [AWAY-C02, AWAY-C06]
8. **Evaluate and maintain.** Compare the report with an ordinary state view under realistic absence and access conditions. Reopen review after rules, notation, localization, save format or authority changes. Remove or simplify the report if it adds burden without improving the intended decision. [AWAY-C05]

### Adjustable variables

Tune summary detail, grouping of changes, exact versus approximate display, report placement, on-demand history, update frequency, treatment of partial calculations and the amount of interruption. Also declare which events are meaningful and who controls the continuation of shared state. There is **no default duration, allowed loss, progress cap, tick rate, font value or participant count**. Values require a local decision and validation. [AWAY-C05]

### Exit conditions

Do not recommend deployment when relevant state cannot be reconstructed accurately, when unknowns would be displayed as facts, when current and historical rules cannot be distinguished, when the report blocks necessary access, or when the team cannot honor its recovery promise. Escalate missing accounting to the system owner; narrow the display to verified facts rather than making up a history. Where the problem is an unacceptable absence penalty rather than missing information, review the rule itself or remove the mechanic. [AWAY-C02, AWAY-C06]

## Worked examples

### Illustrative resource conversion — not a shipped game or performed simulation

Assume a workshop starts with **12 ore, 5 fuel and 0 ingots**. Each completed minute consumes **2 ore and 1 fuel**, producing **1 ingot**. There is no regeneration, random event, storage limit or partial-production credit. The player is absent for **8 eligible minutes**. Five conversions complete; fuel then prevents further production. The current state is **2 ore, 0 fuel and 5 ingots**. These are invented explanatory parameters, not recommended progression timings. [AWAY-C08]

A useful candidate summary is: production stopped because fuel ran out; five ingots were made; ten ore and five fuel were used. An optional detail view can distinguish eight elapsed eligible minutes from five productive minutes. The next decision may be acquiring fuel, changing activity or stopping again. It is not necessarily maximizing output. [AWAY-C08]

A misleading shortcut would multiply the original one-ingot rate by eight and announce eight ingots. A different failure would report only “+5 ingots” and leave the user unaware that the next action cannot proceed. A third would label a pending calculation as “nothing happened.” The pattern’s purpose is to distinguish these situations, not to produce a celebratory screen. Arithmetic was checked locally; no economy or gameplay system was executed. [AWAY-C08]

### Illustrative unchanged and uncertain states

A decorative arrangement has not changed since the last visit and the next action is immediately visible. Compare **no report** with an optional history command; a forced recap may be pure friction. In contrast, a save loaded after a rules update may have a verified current balance but no valid old baseline. Report the current balance and the uncertainty; do not manufacture a difference or imply the old rule still applies. Where the new rule needs teaching, use the existing F01 learning pattern after review rather than disguising instruction as an accounting result. [AWAY-C08]

## Tradeoffs and alternatives

An on-demand ledger can preserve depth without immediate interruption, but some users may not discover the reason an activity stopped. A compact summary can aid orientation but conceal an exception. A permanently visible state panel may make any special return view unnecessary. A deliberately frozen single-player world avoids elapsed-state ambiguity at the cost of the desired sense of autonomous activity. All are legitimate comparison candidates. [AWAY-C05]

Production costs include baseline retention, reliable reconciliation, language-sensitive quantities, accessible navigation, compatibility and support when outcomes are disputed. The pattern does not decide the implementation architecture or prove that these costs are justified. Reuse existing state explanations where possible rather than creating a separate narrative that can drift out of agreement with the rules. [AWAY-C05]

## Failure cases, counterexamples and do-not-use conditions

Failure signs include conflicting balances, unexplained consumption, a modal that steals focus, indistinguishable zero and unknown, or a report dismissed before the next action is understood. A recap that presents foregone output as personal failure can also undermine the intended peripheral relationship with the game. These are proposed warning signs, not validated behavioral thresholds. [AWAY-C06]

Do not use this recipe to legitimize a coercive attendance rule, a misleading purchase offer or an invented compensation promise. Do not promise to pause another player’s activity. Do not expose protected shared information merely because it occurred during absence. Do not assume every surprise in a narrative must be revealed: summarize the decision-relevant state without disclosing irrelevant fiction, while never hiding real progress-loss or transaction consequences as a plot device. [AWAY-C06]

The strongest counterexample is a returning player whose ordinary state view already supports every necessary decision. A report then adds work, even if its accounting is perfect. Another is an intentionally observational experience in which more management would contradict the chosen goal. The pattern should be omitted or offered only on demand in such cases. [AWAY-C05, AWAY-C06]

## Proposed playtest and falsification

**Not performed.** Compare an ordinary current-state view, a compact reconciliation with optional detail, and an expanded report only where that comparison is worth its cost. Hold outcomes constant. Include short/long eligible absence, resource depletion, no-change and uncertain-baseline scenarios; distinguish those design scenarios from implemented engine tests. [AWAY-C09]

Recruit for the intended return context and access needs, including users unfamiliar with the economy and users who prefer low involvement. Randomize or counterbalance presentation where appropriate, but record learning effects because seeing one report may teach the accounting used in another. Do not trade away necessary access features merely to hold layouts visually identical. [AWAY-C09]

Ask participants to predict current available actions and explain the stopping reason before asking what they prefer. Measure decision errors, confidence calibration, assistance, inspection burden, accidental activation and unwanted pressure. Record preference and comprehension separately. A person can understand perfectly and choose to stop. [AWAY-C09]

Before collecting data, the local owner must state the smallest useful improvement, acceptable burdens and the reason for the sample/analysis plan. Reject the pattern if it fails to improve the targeted decision, obscures uncertainty, creates serious access regressions or adds unwanted obligation. A positive local result would support only the tested population, state complexity and presentation, not the full pattern across genres. No such result exists for G20. [AWAY-C09]

## Claim ledger

| Claim | Class | Evidence and locator | Confidence and unresolved issue |
|---|---|---|---|
| AWAY-C01: Purpose and distinct scope | inference | Reviewed P01 interface chain; G20 absence problem | Moderate as a separable problem; canonical ownership/duplication review pending. |
| AWAY-C02: Accurate state and authority prerequisites | inference | Accounting logic; reviewed P01/F07 constraints | High logical confidence, not implementation verification. |
| AWAY-C03: First-party calculation-status example | observed-example | 009 Offline Progress, documentary only | High for preview text; no installed build checked. |
| AWAY-C04: Benefit chain and recipe effects | hypothesis | C01–C03; original synthesis | Low; no direct causal trial validates the combined pattern. |
| AWAY-C05: Variables, alternatives and maintenance | hypothesis | Reviewed P01 task-specific representation; original application | Low benefit confidence; may be unnecessary overhead. |
| AWAY-C06: Failure/exit and ethical boundaries | inference | Reviewed F07-PAT-02; original counterexamples | Moderate risk logic; local safeguards not tested or approved. |
| AWAY-C07: Shared-pattern distinction and adaptations | inference | Inspected F01-PAT-01, F07-PAT-02 and P01-TOP-02 | Moderate; Coordination may decide to merge rather than accept a new pattern. |
| AWAY-C08: Illustrations and arithmetic | inference | Explicit invented assumptions in Worked examples | High conditional arithmetic confidence; no experience/effect claim. |
| AWAY-C09: Falsifying study proposal | hypothesis | Original design to test C04–C06 | Not performed; protocol and thresholds unapproved. |

## Related entries, coverage and history

Apply conditionally to [idle/incremental](../genres/idle-incremental.md); adapt cautiously for persistent-world [cozy](../genres/cozy-game.md) or [educational](../genres/educational-game.md) hybrids. Reviewed F01-PAT-01 concerns supported learning and discriminating transfer; reviewed F07-PAT-02 concerns commitments and refusal. Neither existing identity is renamed or replaced. [AWAY-C07]

Researched: conceptual state reconciliation, documentary calculation-status example, interfaces/exit constraints, explicit arithmetic illustration and falsifying comparisons. Open: direct build-level observation of full reconciliation interfaces, actual state authority and clock handling, empirical benefit, language/access studies, shared-world application and ownership overlap. No universal or released claim is made.

Version 0.1.0, candidate_revision `initial-capture-1`; predecessor and supersession null. Author self-review challenged the strongest claim: additional information may create a worse return, so omission is an explicit exit. Independent review not performed for G20; Gate C pending, host Gate D not run, Gate E not passed. Next decision: accept this as a distinct narrow research candidate, merge its useful portion into an existing pattern, or defer it pending better direct evidence.

## References

All access dates below are 2026-10-11 UTC. Access is to the identified document, not to an executable game. Source IDs are temporary G20 identities; cross-batch canonical-URL/DOI/edition deduplication is pending.

### GDR-SRC-20261010-G20-009
**Malcs / official Melvor Idle news.** *Free Content & Quality of Life updates coming in v1.3*. Official Melvor Idle News. Date: 2024-06-04, corroborated by official News index. [Inspected source](https://news.melvoridle.com/free-content-quality-of-life-updates-coming-in-v1-3/).
Edition/build: v1.3 preview, not a test of an installed build. Access: `relevant-excerpt`. Type: first-party feature announcement. **Locators:** Quality of Life Additions → Offline Progress; Modifier Sources used only as contextual lead; date/byline in official /tag/news/ index. Rights: Copyright retained; no screenshots redistributed. **Limits and independence:** Announced calculation-status feedback and its intended purpose only; no measured comprehension, speed, retention or wellbeing result. No current offline cap inferred.

## Reviewed shared references

These are inspected **parent-selected reviewed drafts**, not released knowledge. Only the indicated passages were transferred. Their underlying public-source claims were not independently reverified here; this batch reuses the reviewed reasoning with its original uncertainty, not as a new experiment. The inspected cumulative archive and correction receipts are identified in the [review packet](../reviews/full-run-20261010-g20-review-packet.md#reviewed-dependency-bytes).

**GDR-CAND-20261010-P01-TOP-02 — Interface and information.** Version 0.1.0, draft; candidate_revision `review-correction-1`. Selected member `selected-drafts/topics/interface-and-information.md`; inspected lines 79–126; current versus stale state, summaries, notifications and decision-specific representation. SHA-256 `1381faf6c998295cd0b0472cf3905a28f87d9515d16bacb54ece423fe080595d`.

**GDR-CAND-20261010-P01-TOP-03 — Accessibility and inclusive interaction.** Version 0.1.0, draft; candidate_revision `review-correction-1`. Selected member `selected-drafts/topics/accessibility-and-inclusive-interaction.md`; inspected lines 56–102, 235–258 and 347–380; functional demands and scoped standards correction. SHA-256 `eab6276ce51dcea359cb599f24ffef603b6062a6d6f6badffa8c0e28a0e79d48`.

**GDR-CAND-20261010-F01-PAT-01 — Supported attempt and transfer check.** Version 0.1.0, draft; candidate_revision `independent-review-correction-1`. Selected member `selected-drafts/patterns/supported-attempt-and-transfer-check.md`; inspected lines 77–124 and 164–268; corrected probe recipe, numerical example, limits and ledger. SHA-256 `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1`.

**GDR-CAND-20261010-F07-PAT-02 — Legible commitment and safe exit.** Version 0.1.0, draft; candidate_revision `initial-capture-1`. Selected member `selected-drafts/patterns/legible-commitment-and-safe-exit.md`; inspected lines 50–118; purpose, prerequisites, recipe, third-party effects and limits. SHA-256 `85cffbbdb25c968e9c00f8ab5b3a230c420f24f0b83e19fbff49648e217b425a`.

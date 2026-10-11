---
id: GDR-CAND-20261010-G09-PAT-01
kind: pattern
title: Evidence-bounded resolution debrief
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
- bounded combat debrief
- factual resolution explanation
tags:
- causal-feedback
- uncertainty
- event-history
- decision-support
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-P02-TOP-02
- GDR-CAND-20261010-P02-TOP-03
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-P02-PAT-02
- GDR-CAND-20261010-F02-PAT-01
- GDR-CAND-20261010-F07-PAT-01
- GDR-CAND-20261010-F01-PAT-01
related_genres:
- GDR-CAND-20261010-G09-GEN-01
- GDR-CAND-20261010-G09-GEN-02
- GDR-CAND-20261010-G09-GEN-03
source_ids:
- GDR-SRC-20261010-G09-020
- GDR-SRC-20261010-G09-021
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

# Evidence-bounded resolution debrief

**Hypothesis pattern; draft and unvalidated.** Give a player a concise, inspectable account of a completed resolution and its relevant controllable inputs without pretending that the available evidence proves a unique cause, an avoidable mistake or a guaranteed better outcome. This is one optional pattern in the G09 packet, not a third genre template or a released diagnostic system.

## Purpose

Use this technique when players can change the conditions of a later resolution but cannot easily connect a completed outcome to those conditions. The intended result is a **warranted next decision**, not merely increased confidence, more statistics or a higher win rate. Losing under uncertainty can follow a reasonable choice. Winning can follow a misunderstood rule. Neither outcome alone justifies corrective advice. [C-01, C-02]

The proposed pattern is genre-neutral. It can apply to automated combat, a defensive encounter or a bounded strategic event sequence, provided the game can report the relevant facts honestly. It is not intended to diagnose an entire campaign, evaluate a person's competence, infer hidden intentions or replace a designer's internal balance investigation. [C-01, C-08]

## Context and prerequisites

The candidate needs a **specific next choice**, a trustworthy record of relevant events and inputs, a known ruleset/version, and an explicit policy for what the player may learn. Record separately what the player knew when committing and what may legitimately be disclosed afterward. Later disclosure does not make the original uncertainty an avoidable error. [C-02]

Event data must distinguish occurrence from interpretation: an accepted action, a selected target, an effect applied, a target becoming ineligible, or an outcome recorded are different propositions. A counter containing only total damage cannot supply an unrecorded targeting sequence. A simulation can model an alternative, but its assumptions must match the question before that output is described as evidence about what would have happened. [C-02, C-05]

The presentation must be usable in the actual reflection interval, including relevant access routes, language and privacy constraints. An asynchronous or paused context permits different depth from a short competitive preparation window. If the only viable design requires reading a full causal report while making time-critical choices, prefer an optional later view or omit the report. [C-06, C-07]

## Mechanism and evidence

TFT patch 12.6 documents combat recap categories and controls. It establishes the existence of a particular reporting interface, not the effectiveness of this recipe. Ludus supplies a separate boundary example: its numerical optimization found a degenerate all-tie solution, showing why a well-defined measurement need not capture the intended quality. Neither source tested player learning from this debrief. [C-03, C-04; GDR-SRC-20261010-G09-020; GDR-SRC-20261010-G09-021]

| Proposed causal link | Support | Limit and disconfirming possibility |
|---|---|---|
| A faithful record makes a relevant event available for inspection. | Logical consequence of correct recording and presentation; an official recap is an existence example. `inference` [C-02, C-03] | Missing events, stale versions or inaccessible presentation break the link. A statistic does not recreate a sequence. |
| Separating facts, rules and inference may reduce unjustified attribution. | F02/P02 reviewed distinctions and this explicit information model motivate the design. `hypothesis` [C-05] | Labels can be ignored or mistaken for certainty; a polished explanation may increase overconfidence. No direct effect is established. |
| Connecting a supported event to a genuinely adjustable input may enable a useful next comparison. | A controllable difference is necessary for the proposed revision, but its usefulness remains untested. `hypothesis` [C-01, C-05] | The input may have been fixed, too costly, unavailable or irrelevant to the player's goal. |
| A small, optional presentation may fit the reflection interval better than an exhaustive report. | Conditional access/attention reasoning, not a measured optimal length. `hypothesis` [C-06] | Brevity can remove a necessary caveat; detail can consume preparation time or obscure the next decision. |
| Better warranted understanding may support later decisions. | Proposed transfer to be tested using unfamiliar same-rule cases. `hypothesis` [C-07] | Memorized advice, different rules or favorable random outcomes can mimic learning. Winning is not the sole outcome. |

The **whole benefit chain is low-confidence**. No original human debrief experiment was established by this batch. The recipe may be useful as a testable design alternative even when its best result is showing that a simpler factual summary is sufficient. [C-01, C-07]

## Recipe

The following is a **proposed procedure**, not an implementation authorization. It contains no universal number of events, duration, accuracy percentage or optimal display density. [C-01, C-06]

1. **Name the next controllable decision.** Write the concrete uncertainty, such as whether a unit had a valid target before it was defeated, whether a defense affected the leaking threat, or whether a known upkeep event exhausted a resource. Reject goals such as “explain why the player is bad.” If there is no relevant next choice, use a neutral result summary. [C-01]
2. **Freeze the observation context.** Record ruleset/version, encounter or event identity, relevant committed inputs, event order, known stochastic conditions and data gaps. Distinguish the player's information at commitment from information legitimately available after resolution. Do not require private opponent information merely to create a convincing narrative. [C-02]
3. **Check evidence fidelity before interpretation.** Confirm that labels match the recorded events and that partial logs are explicitly partial. If only totals exist, report totals. If versions or event identifiers cannot be reconciled, omit the inference and mark the explanation unavailable rather than inventing a cause. [C-02, C-05]
4. **Apply the information boundary before building the explanation.** Remove facts the player is not entitled to receive, including hidden future offers or private opponent inputs. An accessibility alternative must preserve the same allowed facts and uncertainty as the main route. Post-resolution revelation can be labeled as new information, not retroactive proof that the player should have known it. [C-02, C-06]
5. **Select the smallest relevant evidence slice.** Link the committed input, the consequential event and the local result. Retain enabling contributions and target eligibility when they matter. Do not label the highest damage total as the decisive cause by default. Provide optional detail when the short slice would otherwise mislead. [C-05, C-06]
6. **Separate the statement types.** A possible interface uses “Recorded event,” “Applicable rule,” “Possible explanation,” “Not observed” and “Next comparison.” These labels are illustrative, not mandated text. Qualify rule-based deductions with their actual premises; do not present a plausible explanation as a recorded event. [C-05]
7. **Offer a feasible alternative or question, not a guaranteed win.** Identify an input the player could actually change under the relevant budget, unlocks and information. A counterfactual simulation must state which inputs and opponent behavior it held fixed. Same-seed replay is not automatically a valid comparison if the changed action changes the random process or subsequent behavior. Without an adequate model, invite inspection of a rule or a bounded next attempt instead. [C-05]
8. **Fit the reflection window.** Let the player dismiss, defer or revisit the account where the session permits. Support usable focus order, equivalent permitted information and control over verbosity. Do not require the report to be consumed before an unrelated reward or exit. [C-06]
9. **Evaluate understanding and misattribution separately.** Seek authorized tests of what the player can predict, what they incorrectly believe was inevitable or avoidable, and what they can change next. Include same-rule counterexamples where repeating the suggested action would be inappropriate. Necessary access support stays available. [C-07]
10. **Close, narrow or stop.** Retain the design only when its targeted benefit and local guardrails are supported. Disable unsupported explanations after a rule change, unresolved data mismatch or privacy failure. Choose counters-only, a dated factual log, an optional replay or no debrief when they meet the goal with less burden. [C-06, C-07]

### Adjustable variables and explicit exits

| Variable | Why adjust it | Exit condition |
|---|---|---|
| Event scope and granularity | A local target failure differs from an economy cascade. | The selected slice implies a completeness the log cannot support. |
| Known-at-commitment versus revealed-afterward information | Avoid hindsight blame and information leakage. | The system cannot reliably distinguish or filter these states. |
| Confidence wording and statement types | Separate measured occurrence, rule deductions and alternatives. | A qualified suggestion is consistently interpreted as certainty. |
| Timing and optionality | Match a pause, post-wave interval, preparation timer or later review. | The debrief consumes the next decision's accessible time budget. |
| Alternative cost and feasibility | Avoid suggesting unavailable purchases, units or actions. | Eligibility or resource state cannot be verified. |
| Modality and detail | Preserve usable facts without requiring one sensory/input route. | A route drops a critical caveat, leaks more information or cannot be operated. |
| Data/replay retention | A historical record can be valuable but costly and privacy-sensitive. | Retention exceeds authorized purpose, or a new patch invalidates the explanation. |

## Worked examples

### Composition and bypass — illustrative

A player places a defender in front of a ranged unit. A visible enemy bypasses the defender and defeats the ranged unit early. The event record contains targeting, arrival and defeat order; it does not contain the unselected shop offers or a full model of alternative lineups. [C-02, C-05]

The debrief reports the bypass target and the defender's actual contribution. It links to the known targeting rule and notes whether that rule was disclosed before commitment. A possible next comparison is to inspect a formation that separates exposed ranged units; it is not “you should have rerolled for the winning counter.” If a defender genuinely had no eligible action, say that; if the trace is incomplete, do not infer it from low damage. [C-05]

A future same-rule check presents a new bypass enemy and a conventional frontline threat. The correct adjustment differs between cases. Repeating “always spread out” is not accepted as proof of understanding. A later patch that changes targeting requires a separate adaptation test and an updated explanation version. [C-07]

### Enabling defense contribution — illustrative

A slow field deals no direct damage, but recorded status events show it affecting a convoy while another defense attacks. A damage ranking alone makes the slow field look irrelevant. The debrief can show that slowing and attack overlap occurred. It should not convert this into an exact number of “kills caused” unless an appropriately scoped causal model supports that attribution. [C-02, C-05]

The player can examine whether coverage overlaps where the threat actually travels. If the next wave uses a different route or movement class, the prior result is historical evidence, not a guaranteed forecast. A simpler lane/leak summary may answer the relevant question without a full timeline. [C-05, C-06]

### Resource failure in a strategic game — illustrative

A dated ledger records a production increase, a known maintenance obligation and a treaty expiration. The player asks why a resource balance fell. The debrief can reconcile those recorded flows and distinguish known obligations from a newly revealed event. It cannot infer that a rival deliberately baited the player or that choosing a different technology would have prevented the entire campaign setback. [C-02, C-05]

When many unobserved systemic effects dominate the answer, stop at the factual ledger and identify the missing evidence. The player-facing explanation should become narrower as uncertainty increases, not more elaborate to compensate for absent facts. [C-05, C-08]

## Tradeoffs and alternatives

**Counters-only** is cheap and useful when totals answer the question, but does not provide event order. **A chronological log** preserves inspectability with less interpretive authority, but can burden the player with search. **A replay** offers rich context but may require time, accessible navigation and rule-version maintenance. **A deterministic preview** can support a puzzle yet change the intended uncertainty before commitment. **No added explanation** may be preferable when the existing feedback is understood or the aftermath is deliberately ambiguous. These are proposed tradeoffs, not measured rankings. [C-05, C-06]

The recipe adds recording, filtering, localization, verification and support costs. More explanation also creates more ways to be wrong. Its value depends on resolving a specific misunderstanding without leaking information or shifting too much work onto the player. Avoid building a general-purpose advice engine solely because some event data already exists. [C-06, C-08]

## Failure cases

| Observable warning | Competing explanation / risk | Proposed correction |
|---|---|---|
| Players repeat one tip in every situation. | The display taught an action label rather than a rule. | Add contrasting same-rule cases; remove unjustified prescription. [C-07] |
| Confidence rises while causal explanations remain unsupported. | Professional presentation is being mistaken for reliable evidence. | Reduce inference, foreground missing evidence and compare a factual-only version. [C-05, C-07] |
| The report blames a choice that was unavailable at commitment. | Hindsight or current-state eligibility was substituted for the original state. | Reconstruct the commitment snapshot or remove that advice. [C-02, C-05] |
| Support units appear worthless. | Direct-output totals omit enabling or defensive contributions. | Show recorded contribution events; do not fabricate counterfactual credit. [C-05] |
| A caption reveals a hidden attacker or future wave. | Alternative presentation changed the information contract. | Filter by the same allowed facts and uncertainty; stop the leaking route. [C-02, C-06] |
| Players miss the next preparation window. | The reflection design competes with required action time. | Defer, shorten or make it optional; do not assume faster reading. [C-06] |
| Old replays produce different causal statements after a patch. | The explanation is using the current rules against old events. | Version or retire the inference; preserve a historical factual record where permitted. [C-02, C-06] |

## Counterexamples and do-not-use conditions

Do not use this pattern to force an explanation for a deliberately unknowable mystery, to disclose private opponent state, to imply that every loss was avoidable, or to diagnose a player's intentions or abilities. Do not issue an automated recommendation when the evidence supports only a list of events. Do not gate rewards or exit behind reading the report. These are proposed scope limits for this candidate, not legal or clinical rules. [C-02, C-06, C-08]

A player who already understands the event may prefer immediate action; a high-level strategic failure may have too many interacting causes for a bounded debrief; a deterministic puzzle may need a preview instead. The strongest contrary hypothesis is that a simpler summary produces equal or better warranted understanding with less attention burden. That possibility should be tested, not hidden by calling the feature “explainability.” [C-06–C-08]

## Playtest

**Proposed, not performed.** Compare (A) existing counters/summary, (B) a factual event slice, and (C) the same slice with explicitly conditional next-choice guidance. Use the same rules and comparable encounters; counterbalance order or use structurally matched states to limit memorization. Test the statement labels separately from adding new gameplay mechanics. Include participants with different genre familiarity, relevant access routes and language needs. Recruitment, consent, sample precision and practical margins require separate approval. [C-07]

Ask what happened, which fact supports that answer, what was knowable at commitment, what remains uncertain and which available input could be changed. Measure supported attribution, false certainty, correct rule predictions, feasible revision choices, help use, access failures and time taken separately. A win, a high confidence rating or a liked interface alone does not establish the intended effect. Account for outcome severity, prior rule knowledge, random realization, encounter order, narration speed and the time available before the next decision. [C-07]

Include unfamiliar **same-rule** cases with contrasting correct responses, including a loss after a reasonable action and a win after a mistaken interpretation. A changed targeting or economy rule is a separate adaptation/discrimination condition, not transfer. Preserve necessary access support. Test hidden-information boundaries with known forbidden fields, without exposing real private player data. [C-02, C-07]

**Reject or narrow** the pattern when it increases unsupported causal confidence, discloses forbidden information, cannot distinguish historical and current rules, recommends infeasible actions or imposes a critical access/time burden. Retain the simpler summary if the richer treatment has no locally meaningful understanding benefit. Prespecify acceptable tradeoffs and uncertainty before testing rather than selecting a convenient threshold afterward. [C-06, C-07]

## Related entries and ownership

Genre adaptations: [4X](../genres/4x.md), [tower defense](../genres/tower-defense.md) and [auto-battler](../genres/auto-battler.md). Exact source and dependency receipts are in the [G09 review packet](../reviews/full-run-20261010-g09-review-packet.md#reviewed-dependency-transfer).

This candidate is authored in BH-GDR-Genres. **Proposed shared ownership:** Presentation-and-Interaction for player-facing feedback, with Foundations-and-Systems for decision/evaluation boundaries. Coordination has not approved a home, permanent ID or merge. It is not a duplicate of `GDR-CAND-20261010-F07-PAT-01` (designer-facing balance diagnosis), `GDR-CAND-20261010-P02-PAT-02` (fact-preserving cue alternatives), or `GDR-CAND-20261010-F02-PAT-01` (precommitment opportunity-cost comparison); those inspected drafts constrain its recipe. `GDR-CAND-20261010-F01-PAT-01` supplies the corrected same-rule/changed-rule test distinction. [C-08, C-09]

## Coverage and history

Researched support: one official recap interface and one original computational failure case, plus inspected reviewed dependency distinctions. Open: direct human evidence for the complete recipe, causal-log fidelity across engines, privacy/retention design, counterfactual-model validation, combined access needs, localization and real-time burden. Source 021 is a model-boundary caution, not a debrief experiment. [C-03, C-04, C-07]

Version **0.1.0**, **initial-draft-1**, first G09 submission; predecessor/supersession null. Author self-review is separate from independent review, which has not occurred for G09. Approval fields remain null. Exact bytes are in the [integrity receipt](../reviews/full-run-20261010-g09-integrity.md). Pattern effectiveness, implementation and release are not approved.

## Claim ledger

All claim IDs below are local to this pattern. No formal standard or approved studio design decision is asserted.

| Claim | Precise proposition | Class | Support / locator | Confidence and scope | Limit |
| --- | --- | --- | --- | --- | --- |
| C-01 | The pattern seeks a warranted next decision, not a uniquely diagnosed mistake or higher confidence alone. | hypothesis | Purpose, explicit mechanism and proposed comparison in this file. | Low effectiveness confidence; no direct human validation. | A simpler result summary may be sufficient. |
| C-02 | A truthful debrief needs relevant recorded events, rules/version and separate precommitment/postresolution knowledge boundaries. | inference | Logical prerequisites; inspected F02 decision and P02 fact-preserving excerpts. | High as a limit on justified statements, not proof of usability. | Missing trace or forbidden information requires narrowing or omission. |
| C-03 | TFT 12.6 documents a recap with damage/healing categories and PC controls. | observed-example | GDR-SRC-20261010-G09-020; Combat Recap Interface Changes. | High documentary confidence, no learning result. | Does not validate this full technique. |
| C-04 | Ludus’s all-tie metric solution shows a scoped gap between numeric parity and intended design quality. | empirical-evidence | GDR-SRC-20261010-G09-021; §4.2, p.12732, with §3.1 scope. | High for reported computational case; no participants. | Does not establish an effect of player-facing explanations. |
| C-05 | Separating recorded events, rules, inference and feasible alternatives may improve calibration of player explanations. | hypothesis | Recipe and causal bridge; 020 is an existence example, not an effect test. | Low; full chain unvalidated. | Polished conditional language may still induce overconfidence; G09-CON-08. |
| C-06 | Optional scoped detail and usable alternative routes may reduce debrief burden, but can trade away necessary context. | hypothesis | Inspected P01/P02/F07 constraints; proposed variants. | Low outcome confidence; no universal duration/length. | Preparation-time pressure or ambiguous rules may defeat the technique. |
| C-07 | The validation plan must distinguish warranted understanding, false attribution, same-rule transfer and changed-rule adaptation. | hypothesis | Proposed tests; corrected F01/W02 and F07 excerpts. | Low as evidence of benefit; no test was run. | Memorization, outcome variance and unmatched states can explain apparent improvement. |
| C-08 | A bounded player-facing debrief has a narrower purpose than internal balance diagnosis or explanation of an entire campaign. | inference | Scope comparison to inspected F07/P02/F02 patterns; worked counterexamples. | Moderate conceptual distinction; owner/duplicate review pending. | Coordination may merge or narrow the candidate after a current-index check. |
| C-09 | Reviewed dependencies remain drafts; their IDs, corrections and actual-byte limits are retained. | inference | G09 packet dependency receipt and archive comparison. | High local process confidence, not new independent review. | Underlying studies and missing canonical index are not silently imported. |

## References

### GDR-SRC-20261010-G09-020

Rodger “MinionsRpeople2” Caudill / Riot Games. **[Teamfight Tactics patch 12.6 notes](https://teamfighttactics.leagueoflegends.com/en-au/news/game-updates/teamfight-tactics-patch-12-6-notes/)**. Riot Games. Publication/update: 2022-03-29. Edition/build: Patch 12.6; PC controls described. Accessed 2026-10-11 UTC; access: `relevant-excerpt`. Locator: “Combat Recap Interface Changes,” retrieved text lines 66–72. Type: official versioned interface-change documentation. Supports: C-03; motivates C-05 only. Independence: Riot/TFT. Limits: Documents recap controls and categories, not a causal explanation engine or evidence that the recap improves learning. Rights: Copyright retained by authors/publisher; paraphrase and links only; no media or source text redistributed.
### GDR-SRC-20261010-G09-021

Nathaniel Budijono, Phoebe Goldman, Jack Maloney, Joseph B. Mueller, Phillip Walker, Jack Ladwig and Richard G. Freedman. **[Ludus: An Optimization Framework to Balance Auto Battler Cards](https://ojs.aaai.org/index.php/AAAI/article/view/21550)**. Proceedings of AAAI 36(11), 12727–12734. Publication/update: 2022-06-28 (publisher publication date). Edition/build: Original paper; DOI 10.1609/aaai.v36i11.21550; publisher PDF /21550/21299. Accessed 2026-10-11 UTC; access: `relevant-excerpt`. Locator: Sections 3.1, 3.5, 4.2, 5 and 6.1; printed pp. 12729, 12731–12732; PDF pages 3 and 6 visually inspected. Type: original computational experiment. Supports: C-04; bounds C-05/C-08, not debrief efficacy. Independence: Ludus / Budijono et al.; independent of Riot and Blizzard. Limits: Research simulator with unrestricted card availability and fixed lineups; drafting/purchasing deferred. A zero-variance all-tie solution exposes a metric failure. No human enjoyment/equity experiment was reported. Rights: Copyright retained by authors/publisher; paraphrase and links only; no media or source text redistributed.

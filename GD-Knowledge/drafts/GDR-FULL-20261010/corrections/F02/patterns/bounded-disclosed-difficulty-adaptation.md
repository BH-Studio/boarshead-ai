---
id: GDR-CAND-20261010-F02-PAT-02
kind: pattern
title: Bounded disclosed difficulty adaptation
version: 0.1.0
status: draft
candidate_revision: independent-review-correction-1
attempt_identity: F02-local-attempt-01
predecessor_sha256: d442c6f6bac8c46f363cbf7ec91bdcd58e7ea840213a0f6c5f21015817a8dd6b
supersedes: initial-capture-1 (same candidate or packet; local corrected copy only)
change_summary: Correct source 008 performance-result locator; conclusions and confidence unchanged.
owner_project: BH-GDR-Foundations-and-Systems
run_id: GDR-FULL-20261010
batch_key: F02
updated: '2026-10-11'
evidence_checked: '2026-10-10'
aliases:
- transparent adaptive difficulty
- bounded assistance controller
- controllable adaptation
tags:
- difficulty
- adaptation
- assistance
- player-control
- evaluation
related_topics:
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-F02-TOP-01
related_patterns:
- GDR-CAND-20261010-G01-PAT-01
- GDR-CAND-20261010-F01-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-F02-008
- GDR-SRC-20261010-F02-009
- GDR-SRC-20261010-F02-012
reviewer: null
approved_by: null
approved_date: null
---

# Bounded disclosed difficulty adaptation

**Draft pattern; complete mechanism remains a hypothesis.** Candidate `GDR-CAND-20261010-F02-PAT-02`, version 0.1.0, revision independent-review-correction-1. This is not an instruction to install a controller or a claim that automatic adjustment is preferable to manual options.

## Purpose

Reduce repeated friction from a **specified, diagnosed demand** while preserving a declared set of gameplay decisions and the player’s control over assistance. Make the fact and scope of adaptation understandable. Avoid interpreting every failure as lack of skill or silently raising opposition to cancel visible improvement. [C-04]

This pattern owns a bounded feedback-and-adjustment process. It does not replace the existing G01 **Configurable threat consequences** pattern, which chooses among forms of threat consequence, or F01’s learning-support pattern, which concerns understanding and transfer checks. A manual consequence setting may be the simpler correct answer. [C-04, C-05]

## Context and prerequisites

Consider this pattern for an activity where adaptation is permitted by the approved experience and shared-play contract, the player can access controls/explanations, and a local signal can reasonably identify the target demand. There must be a safe point to apply changes, bounded adjustable variables, viable save/recovery behavior, an override or exit, and a way to distinguish adaptation from unrelated state changes. [C-04, C-05]

Do not deploy when the only signal is a crude win/loss count with no defensible connection to the proposed adjustment. Check rule knowledge, access to required information, resources, intentional experimentation and technical faults before treating repeated failure as the target problem. If the diagnosis remains ambiguous, keep settings stable and offer a player-controlled option. [C-05]

## Mechanism and evidence

| Causal link | Evidence status and limit |
|---|---|
| System adjustment and expectations can influence experience separately. | Denisova and Cairns’ controlled study supplies a narrow immersion finding, not lasting access or trust validation. `empirical-evidence` [C-01; GDR-SRC-20261010-F02-008] |
| A player can be offered understandable, changeable difficulty dimensions. | XAG 108 supplies vendor guidance, not a treatment effect. `practitioner-heuristic` [C-02; GDR-SRC-20261010-F02-009] |
| A death-conditioned assistance mechanism is a documented design option. | Hades FAQ provides a concrete documentary example, not a test of this pattern. `observed-example` [C-03; GDR-SRC-20261010-F02-012] |
| A diagnosed signal selects an appropriate bounded adjustment. | Not established by those sources for arbitrary games. Signal validity and manipulation resistance must be tested. `hypothesis` [C-04, C-05] |
| Disclosure, override and stable invariants preserve valued control while friction falls. | This is the pattern’s central unvalidated benefit; explanation may instead burden or diminish the experience. `hypothesis` [C-04, C-06] |

The laboratory use of deceptive expectations is not permission to misrepresent adaptation in a product or a playtest. Nor does a documented successful game establish that its adjustment causes success. [C-04]

## Recipe

1. **Declare the intended activity and invariants.** Name the target demand and the decisions that should remain. Specify what adaptation may never change: for example, legal moves, information availability, objective logic, other participants’ rules or a selected comparison category.
2. **Offer a truthful contract before activation.** Explain what can adjust, when it can change, what persists, and how to return to fixed or manual settings. Use neutral effect descriptions. Do not obscure shared-play or progression consequences.
3. **Validate the diagnostic signal.** Identify observable events that discriminate the target demand from misunderstanding, access barriers, depleted resources, deliberate risk or technical faults. Record a “diagnosis uncertain” branch. Do not infer personal health attributes from performance.
4. **Choose a minimal adjustable variable.** Prefer a lever with a clear relation to the diagnosed demand. Define bounds and disallowed combinations. Preserve ordinary accommodations regardless of measured success.
5. **Define the update policy.** State the observation window, trigger, maximum change, safe application point and conditions for holding steady. Use stability rules so alternating outcomes do not immediately reverse settings. These are locally chosen design parameters, not a universal control formula.
6. **Apply and disclose the state transition.** Change only at the declared point, preserve viable progress, and make the current setting and recent change available without mandatory interruption. The player must not need to deliberately fail to discover help exists.
7. **Audit adversarial and boundary cases.** Check intentional underperformance, stale observations after changing modes, save/load, interrupted runs, depleted states, simultaneous constraints and interactions with other players. If the signal can be manipulated, prefer direct access to the assistance over rewarding needless failure.
8. **Evaluate against simpler alternatives.** Compare truthful automatic adjustment with fixed and player-controlled settings. Separate friction reduction, preserved decision-making, trust, learning and preference. Improvement on one measure does not establish all others.
9. **Exit or roll back deliberately.** Stop automatic updates when the player opts out, diagnosis is uncertain, a bound is reached without benefit, an invariant breaks or shared-play rules make further adjustment inappropriate. Keep an accessible manual route and a viable recovery state; do not erase unrelated progress.

The recipe is a proposed design process, not an implemented controller. [C-04–C-06]

### Adjustable variables and decision points

| Variable | Local decision required | Why it matters |
|---|---|---|
| Target and signal | Which demand is being inferred, from what evidence? | A win/loss signal may not identify the causal barrier. |
| Observation window | What comparable attempts count; when is old evidence discarded? | Stale context can trigger an inappropriate change. |
| Step size and bounds | What can change, by how much, and how far? | A large change may remove the intended activity; a tiny change may be irrelevant. |
| Cadence and stability rule | When can an update occur, and what prevents rapid reversal? | Stable feedback supports attribution; responsiveness still matters. |
| Direction | One-way assistance, bidirectional adjustment, or suggested changes only? | Automatically increasing demands can conceal improvement. |
| Disclosure and control | How is state explained, inspected and overridden? | Surprise, burden and discoverability compete. |
| Persistence | What survives restart, save/load and mode changes? | Inconsistent state can confuse or create exploits. |

No source establishes universal values for these variables. Select and document local values before testing. The primary exit condition is **unreliable diagnosis or broken invariants**, not merely failure to keep a chosen success percentage. [C-05]

## Worked examples

### Illustrative complete example: timing assistance without choosing the strategy

An invented activity requires selecting an appropriate response, then executing it after a warning. Assume observation shows the player predicts the correct response and detects the warning but repeatedly misses its timing. The intended invariant is that the player still selects the response and manages the same resources; assistance must not identify the correct response for them. This diagnosis is assumed for illustration, not established by F02 testing. [C-04, C-05]

A **proposed local test configuration**, not recommended tuning, starts with a 1.2-second response window. After three comparable diagnosed timing misses, the next attempt may use a window 0.3 seconds longer, up to 2.1 seconds. Changes occur only before the next attempt, not while a response is underway. The player sees an explanation of the timing change and may select a manual window or stop adaptation. Success does not automatically withdraw assistance. These arbitrary example values illustrate a bounded policy; none is an accessibility standard or validated threshold. [C-04]

The state audit asks whether altered timing also reveals an answer, changes resource generation, desynchronizes another timed event or grants an unintended shared-play advantage. A missed response due to an unavailable cue or misunderstood rule goes to the uncertain/other-cause branch rather than accumulating toward the timing trigger. An intentionally sacrificed attempt is not automatically a skill signal. [C-05]

If the maximum window still leaves the task inaccessible, the controller stops escalating and offers a separately designed input route, pause/planning option or bypass where the contract permits. The example does not claim these alternatives preserve identical experience. If the player prefers fixed timing, the exit remains accessible even after repeated failure. [C-04, C-05]

### Documented comparator, not an implementation template

Hades’ FAQ describes an optional resilience mechanism tied to deaths. That documents a different variable and signal from the timing example. It supplies no basis for transferring numerical tuning, automatically making success harder, or treating all repeated failure as the same need. [C-03; GDR-SRC-20261010-F02-012]

## Tradeoffs and alternatives

A manual slider removes the need to infer the player’s goal; a described preset reduces menu effort; a practice mode isolates repetition; a consequence option can preserve the task while reducing setback. Automatic adaptation is justified only if its reduced configuration burden is worth diagnostic, explanation and compatibility costs. An optional suggestion rather than an automatic update may be a useful intermediate design. These alternatives are proposals, not ranked empirical conclusions. [C-04, C-05]

Disclosure can help someone understand what changed, but may also direct attention away from the fiction or performance. Prefer truthful layered explanation to either repeated interruption or deceptive claims. Private, noncompetitive assistance and shared competition require different contracts; a setting’s availability does not decide that policy. [C-04, C-05]

## Failure cases

| Warning sign | Possible cause | Proposed correction or exit |
|---|---|---|
| The system repeatedly changes in opposite directions. | Noisy signal, changing context or inadequate stability rule. | Hold the setting; revise the signal/window or switch to manual control. |
| The player deliberately fails to obtain needed help. | Help is gated behind the controller. | Expose an appropriate direct option; reassess incentives. |
| Success no longer feels attributable to player action. | Adaptation overwhelms the intended demand or changes too invisibly. | Reduce scope, clarify state, preserve a fixed option or stop the pattern. |
| The same failures continue at the assistance limit. | Wrong target, missing access route or a recovery trap. | Diagnose again; do not keep amplifying an unrelated parameter. |
| Saved state and displayed setting disagree. | Persistence contract or transition defect. | Stop adaptation and repair state handling before further evaluation. |
| Shared outcomes become incomparable. | An undisclosed or incompatible individual adjustment. | Apply the approved shared policy or remove automatic adjustment from that context. |

These are anticipated risks, not observed defects in a shipped game or F02 prototype. [C-05]

## Counterexamples and do not use conditions

Do not use automatic adaptation where the core promise is a stable self-selected benchmark and adjustment would violate that promise; where affected players have not accepted the shared policy; where state changes cannot be bounded safely; or where a direct accessible option solves the problem with less burden. Never make access accommodations contingent on proving repeated failure. [C-04, C-05]

The strongest counterargument is that a transparent manual setting is both more controllable and easier to validate. The inspected study’s immersion findings do not defeat that argument. A controller can improve completion while diminishing mastery, trust or the desired challenge. [C-01, C-04, C-06]

## Playtest

**PROPOSED — NOT PERFORMED.** Compare fixed demands, player-controlled adjustment and the truthful bounded policy. Give every condition a viable exit and required accommodations. Avoid exposing one condition to extra instruction unless explanation is the factor under test; document unavoidable differences. [C-06]

Use participants with varied task familiarity and relevant access needs, not a generic expert sample alone. Record rule predictions separately from chosen strategies and execution. Measure target-demand errors, current settings, update timing, subjective control, trust, preserved decisions, unnecessary interventions and preference. Assess learning with an appropriate stable reference task rather than assuming an adaptive completion rate demonstrates improvement.

Confounds include practice, fatigue, prior difficulty beliefs, different actual assistance amounts, outcome order, resource carryover and expectation effects from the explanation. A recorded-setting comparison may help isolate controller timing but cannot guarantee equal fit across participants. Predefine the practical benefits required and unacceptable harms; no universal sample or significance rule is supplied.

Reject or simplify the pattern when the signal misidentifies the target, when automatic help adds no meaningful benefit over manual adjustment, when it removes intended decisions, or when trust/access/compatibility harms outweigh the specified benefit. Treat inconclusive results as inconclusive, not evidence that disclosure or adaptation always works. [C-06]

## Claim ledger and sources

| ID | Claim and class | Source/locator or reasoning | Confidence, applicability and unresolved question |
|---|---|---|---|
| C-01 | Adaptation and expectations can affect reported immersion under the inspected experimental conditions. `empirical-evidence` | GDR-SRC-20261010-F02-008, §7.2/Table 3, §7.3 and §8. | Moderate; not long-term trust, accessibility or manual-versus-automatic superiority. |
| C-02 | Understandable configurable difficulty is recommended by XAG 108. `practitioner-heuristic` | GDR-SRC-20261010-F02-009, Implementation guidelines. | High for attribution; vendor guidance, not a formal requirement or efficacy guarantee. |
| C-03 | A death-conditioned resilience mechanism is documented for Hades. `observed-example` | GDR-SRC-20261010-F02-012, FAQ difficulty answer; document inspected by F02 author on 2026-10-10. | High for document attribution; no build test or transferred tuning. |
| C-04 | A bounded, disclosed, overridable controller may preserve control while reducing a diagnosed friction. `hypothesis` | Proposed synthesis of C-01–C-03; the complete recipe and timing example are untested. | Low; manual options may be superior or the target experience may require fixed demands. |
| C-05 | Diagnosis, stability, state persistence and shared-play constraints can invalidate the controller. `inference` | Feedback/state-model analysis; anticipated failure cases, not measured incidence. | Moderate logical basis; actual exploitability and compatibility require implementation-specific review. |
| C-06 | The proposed comparison can challenge the controller’s added value and unintended effects. `hypothesis` | Author-designed evaluation with separate outcomes; no tests performed. | Low until executed; expectation, assistance amount and carryover remain confounds. |

## References

Access date for every record below: **2026-10-10**. These are temporary source candidates. A repeated record is the same evidence, not additional corroboration. “Relevant-excerpt” identifies inspected substantive passages, not merely an abstract and not every linked supplement.

### GDR-SRC-20261010-F02-008

**Alena Denisova and Paul Cairns.** [Player Experience and Deceptive Expectations of Difficulty Adaptation in Digital Games](https://eprints.whiterose.ac.uk/139704/1/1_s2.0_S1875952118300521_main.pdf). Entertainment Computing 29, pp. 56–68, Elsevier. **Publication/update:** 2018-12 accepted; 2019 journal issue. **Edition/version:** Accepted manuscript with repository cover; not a new 2026 edition.

**DOI:** [10.1016/j.entcom.2018.12.001](https://doi.org/10.1016/j.entcom.2018.12.001).

**Access:** relevant-excerpt. **Source type:** original controlled game experiments. **Inspected locators:** Study 1 Participants/design; Study 2 Method; §7.2 and Table 3, manuscript p. 24 (PDF page 27); §7.2.1 performance, manuscript pp. 26–27 (PDF pages 29–30); §§7.3 and 8 discussion. **Supports local claims:** C-01; limited basis for C-04

**Limits:** Brief lab sessions; immersion, performance, competence, accessibility and trust are distinct outcomes. Minor prose/table numeric discrepancies; exact disputed statistics are not propagated. **Independence:** White Rose PDF, City repository metadata and publisher DOI are one work. Expectation manipulation does not authorize deceptive product behavior. **Rights:** Accepted manuscript CC BY-NC-ND 4.0, as repository metadata states; paraphrase only, no altered manuscript distributed

### GDR-SRC-20261010-F02-009

**Microsoft.** [Xbox Accessibility Guideline 108: Game difficulty options](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/108). Microsoft Learn. **Publication/update:** 2026-03-04 last updated; original date unknown. **Edition/version:** Live unnumbered guideline page inspected 2026-10-10.

**Access:** relevant-excerpt. **Source type:** official vendor accessibility guidance. **Inspected locators:** Overview; Scoping questions; Implementation guidelines: difficulty adjustment, discrete mechanics, descriptive labels and pausing. **Supports local claims:** C-02; design guidance informing C-04

**Limits:** Practitioner guidance, not a formal standard, universal tuning prescription, or measured assurance of accessibility. Embedded game demonstrations not reproduced. **Independence:** Same issuer/suite as source 010, not independent empirical corroboration. Linked external resources remain separate, uninspected leads. **Rights:** Reuse terms not separately inspected; paraphrase only; no embedded media copied

### GDR-SRC-20261010-F02-012

**Supergiant Games.** [Hades FAQ](https://www.supergiantgames.com/blog/hades-faq/). Supergiant Games. **Publication/update:** 2018-12-07 published; 2025-07-16 updated. **Edition/version:** FAQ revision as inspected; game build number unspecified.

**Access:** relevant-excerpt. **Source type:** first-party game documentation; documentary observed example. **Inspected locators:** Question beginning “Some rogue-likes are brutally difficult…” and its God Mode / challenge-modifier answer. **Supports local claims:** C-03; documentary comparator only

**Limits:** Documents death-conditioned resilience; does not supply numerical increment/cap in the used passage or prove long-term experience effects. Observer: F02 author, 2026-10-10, document only. **Independence:** Independent studio from source 011, but another documented example rather than a controlled comparison. **Rights:** Supergiant Games copyright; paraphrase only

## Related entries and history

Parent: [Challenge and difficulty](../topics/challenge-and-difficulty.md), `GDR-CAND-20261010-F02-TOP-02`. Related: [Decision design](../topics/decision-design.md) for information and commitment. Existing G01 consequence-configuration and F01 learning-check patterns remain distinct draft dependencies; see the [dependency register](../reviews/full-run-20261010-f02-review-packet.md#dependency-register).

2026-10-10 — Initial F02 candidate, version 0.1.0, revision initial-capture-1. No predecessor asserted. Author self-review only; independent review, participant testing, live-host retrieval and release not completed. No controller was executed and no engine or harness was changed.


**2026-10-11 — independent-review-correction-1, still 0.1.0 draft:** Separate model source spot-check corrected source 008 performance-result locators from §7.3 to §7.2.1, manuscript pp. 26–27 (PDF pages 29–30). §7.3 remains discussion. The substantive empirical conclusion and confidence are unchanged. Original initial-capture history above is preserved; no participant, prototype or host tests were performed and no human approval or release occurred. See the separate correction receipt and independent review for current disposition.

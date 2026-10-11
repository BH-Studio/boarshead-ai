---
id: GDR-CAND-20261010-G02-PAT-01
kind: pattern
title: Bounded action grace
version: 0.1.0
status: draft
candidate_revision: initial-1
run_id: GDR-FULL-20261010
batch_id: G02
attempt_id: G02-authoring-attempt-01
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate plus supplied G02 dispatch
aliases:
- bounded input forgiveness
- early action buffering
- recent-state action allowance
tags:
- action-eligibility
- input-buffering
- cancellation
- forgiveness
- state-transitions
related_topics: []
related_patterns:
- GDR-CAND-20261010-G02-PAT-02
related_genres:
- GDR-CAND-20261010-G02-GEN-01
- GDR-CAND-20261010-G02-GEN-02
- GDR-CAND-20261010-G02-GEN-03
source_ids:
- GDR-SRC-20261010-G02-001
- GDR-SRC-20261010-G02-005
- GDR-SRC-20261010-G02-006
- GDR-SRC-20261010-G02-008
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed
predecessor_sha256: null
supersedes: null
superseded_by: null
change_summary: Initial G02 candidate; no predecessor submitted
hash_record: ../reviews/full-run-20261010-g02-review-packet.md#candidate-inventory-and-byte-integrity
proposed_shared_owner: 'Pending coordination: Foundations and Systems with Presentation
  and Interaction'
recommendation_confidence: low; mechanism account exists, cross-context causal efficacy
  unvalidated
---

# Bounded action grace

> **Draft research candidate, not released guidance.** Version 0.1.0; candidate revision `initial-1`; independent review not performed. Definitions and proposed adaptations below are bounded inferences or hypotheses, not an approved studio design. No game build, gameplay recording, prototype or player test was run in this batch.

The supplied G02 dispatch authorizes this batch and supersedes old starter-phase sequencing restrictions only. Its final parent reconciliation records completed, independently reviewed first-wave drafts, but those reviewed bytes were not retrieved here. No unseen F01/P01 wording or numerical settings are inherited. No reviewed shared guidance is transferred in this entry. [Workflow basis: supplied `Pasted text.txt`, Assigned outputs; Genre-specific questions; Parent review reconciliation.]

## Purpose and scope

**Candidate purpose:** accept a clearly defined action request near a legitimate state transition without creating an unwanted delayed action. Examples include a command just before a capability becomes available or just after a permitted support state ends. The desired outcome is predictable expression of a chosen action, not simply fewer failures. This is a testable proposal, not validated general guidance. [C-01]

The recipe is genre-neutral: it describes action eligibility and cancellation rather than a platformer-only movement controller. Its inspected production basis is nevertheless narrow—Celeste's creator explanation. Transfer to another action grammar, engine, network model or genre remains unvalidated. Do not use “player intent” as an invisible variable that the system can read; infer likely intent only through an explicit rule and evaluate disagreements with the player. [C-01; C-03]

**Ownership:** authored in BH-GDR-Genres for this batch; proposed shared ownership requires coordination with Foundations and Systems for action semantics and Presentation and Interaction for controls/feedback. No canonical home or permanent ID has been allocated.

## Context and prerequisites

Apply only when the action's eligibility states can be stated clearly, the transition is observable enough to support learning, and the team can distinguish a new request, a held request and a cancelled request. There must be an unambiguous rule for whether a request is consumed once, expires, changes with context, or is discarded on interruption. These are proposed prerequisites of this recipe, not assertions about every existing input system. [C-03]

The intended task should remain meaningful after the proposed tolerance change. When a challenge specifically tests choosing **not** to act after a transition, blindly carrying an earlier command forward may violate the contract. Where an action spends a scarce resource, targets another actor or crosses a dangerous boundary, the consequences of an unwanted activation may outweigh the avoided rejection. Start with a reversible prototype and local traces, not a borrowed millisecond value. [C-04]

Before choosing this pattern, rule out a more direct explanation: an unreadable destination, inaccessible control combination, uncommunicated state change, unstable performance or a wrong checkpoint state. The pattern can coexist with remedies for those problems, but cannot be presumed to solve them. [C-03; C-05]

## Mechanism and evidence by causal link

| Proposed link | What is supported | Limit and classification |
|---|---|---|
| Some requests near a support/landing transition can be given a wider eligibility rule | Thorson describes post-edge jump allowance and prelanding jump buffering in Celeste | Documented creator technique, not measured frequency of mistaken rejection. `practitioner-heuristic` [C-02; GDR-SRC-20261010-G02-001, items 1–2] |
| Explicit expiry, consumption and cancellation can define when a retained request fires | This follows from the proposed state/request specification | Logical design model, not proof of a particular implementation. `inference` [C-03] |
| A bounded rule may better match a player's chosen action than strict boundary rejection | Motivated by the creator's forgiveness rationale | Actual match requires player evidence; accidental activations can reverse it. `hypothesis` [C-01; C-04] |
| Better matching may preserve control and useful practice | Plausible desired consequence, not directly measured for this recipe | Completion alone cannot establish control, learning or satisfaction. `hypothesis` [C-06] |

Neither coyote time nor buffering is evidence that all games need both, that wider is always better, or that a successful game's outcome was caused by these features. No recommended numerical grace window is established by the inspected source. [C-02; C-04]

## Actionable recipe

1. **Name the action and legitimate state.** Write the normal eligibility rule in player-facing and conceptual terms. Record the cost, destination/target and whether a changed context invalidates the command. For a jump-like action, distinguish permission to initiate from subsequent movement control. [C-03]
2. **Identify a candidate boundary miss.** In a proposed observation, compare command timing with state transitions and ask the player what they expected. Include deliberate non-actions and cancellations; a trace showing “pressed early” is not proof of a desire to act later. If the main error is misreading space, test a presentation change as an alternative. [C-03; C-05]
3. **Choose the smallest relevant form of grace.** An early request can be retained until the next eligible state; a recently lost support state can remain temporarily eligible. These are different changes. Evaluate separately before combining them, and do not automatically include positional correction or target snapping in a timing recipe. [C-02; C-04]
4. **Specify expiry, single consumption and cancellation.** Name events that discard the pending request: an explicit cancel, release when release means cancellation, a changed target, death, menu transition, loss of a required resource, or another rule-specific event. Do not require all these events universally; document which are semantically relevant. One request should not silently become multiple uses. [C-03]
5. **Resolve interacting eligibility rules.** Define whether an action qualifies through current eligibility or grace, whether both consume the same resource, and which rule wins when a queued action meets a recent-state allowance. Check that the combination does not create a second activation or preserve permission through an unrelated state. [C-03; C-04]
6. **Make the result interpretable.** Communicate available state and action outcome consistently with the game's presentation. Explanations can be concise, optional or practice-based; the recipe does not require exposing a technical timer. Update prompts for actual controls. Do not infer that a forgiving action needs no feedback. [C-05; GDR-SRC-20261010-G02-006]
7. **Compare boundaries and alternatives.** Hold geometry, camera and other rules stable while varying the local grace settings; separately test a presentation-only alternative. Include supported devices and input modes, deliberate near-boundary cancellation and interrupted attempts. Parameter values are local test settings to select later, not numbers supplied here. [C-06]
8. **Adopt, narrow or remove only after the local decision.** Prefer the variant that serves the declared action contract with acceptable unintended activation and remaining access barriers. If there is no meaningful improvement, or control becomes less predictable, change the rule or omit it. Any implementation/adoption requires separate authorization. [C-04; C-06]

**Exit conditions:** stop this recipe when eligibility cannot be made coherent; when action intent depends on information unavailable until after the command; when resource/target changes make retained commands unsafe; when the supported input mode cannot cancel as intended; or when the actual problem is unrelated to the command boundary. Exit does not mean abandoning access—it means choosing another remedy. [C-04; C-05]

## Adjustable variables and observables

| Variable | Decision to make | Observe locally; do not assume |
|---|---|---|
| Early-request lifetime | When a queued request expires or becomes ineligible | Expired intended commands versus unwanted late actions |
| Recent-state allowance | Which lost state remains eligible and for how long | Deliberate walk-offs/cancellations versus desired late actions |
| Hold/release semantics | Whether holding maintains a request and release cancels it | Fatigue, accidental retention, compatibility with toggles |
| Request consumption | Once per press, once per state, or another explicit grammar | Duplicate activations and resource accounting |
| Context binding | Whether target, surface or action identity is fixed at request time | A request firing at a newly changed and unintended target |
| Interruptions | Treatment of pause, respawn, focus changes and remapping | Commands leaking into a new attempt or menu |
| Feedback and configuration | How availability/outcome and supported options are explained | Predictability, discoverability and localized prompt accuracy |

All are proposed control points. No optimal window, sampling frequency, device equivalence or implementation algorithm was measured in this batch. [C-03; C-05; C-06]

## Worked examples

### Illustrative: landing before a springboard action

**Illustrative, not a shipped scene or performed test.** A fictional traversal action is available only while supported by a springboard. The player can press the action before landing. The candidate rule retains that request only until a declared local expiry and only for this action context. Landing while it remains valid consumes the request once. Releasing the input cancels it in this prototype's chosen grammar; the team must separately evaluate a toggle configuration rather than assume identical semantics. [C-07]

The prototype comparison includes arriving normally, pressing too early, releasing before landing, missing the board, landing on a different object, pausing midair and dying before arrival. Record actual intended actions and unwanted activations. A completion increase is insufficient when cancellation no longer works. A separate presentation comparison exposes the board's action state without buffering, allowing the team to ask whether visibility alone addresses the problem. [C-06; C-07]

**Counterexample within the same scene:** a player taps the command while approaching, then deliberately changes direction to avoid the board. A long, context-insensitive queue launches them from another object later. That is a failure of the pattern's proposed purpose even if it prevents a fall. Narrow context binding, cancellation or expiry; omit the queue if the grammar remains ambiguous. [C-04; C-07]

### Illustrative transfer outside platforming

In a fictional traversal-independent interaction, a device becomes ready after a visible recovery phase. A pre-ready command might queue one operation, but a changed selection must not apply the old command to a newly chosen device. A high-consequence irreversible operation may be better served by explicit confirmation or immediate rejection with feedback. This is a hypothesis about possible transfer, not evidence that the Celeste mechanism has been validated for interface actions. [C-07]

## Alternatives, tradeoffs and opportunity costs

A clearer state indicator can solve misunderstanding without retaining commands. A remap or toggle can reduce input complexity or duration without changing temporal eligibility. A larger safe destination changes spatial demand instead. A practice opportunity can teach the current boundary; a slower action pace changes several timing relationships and needs a broader test. The right alternative depends on which problem is observed. [C-05; GDR-SRC-20261010-G02-006]

Grace preserves some demands while relaxing others. It can reduce boundary sensitivity, but can also make a command appear to fire “late,” create hidden rule interactions, change a carefully defined performance category or increase QA cost across resets and assistance. Celeste's versioned notes record assist/reset corrections; they support taking combination failures seriously, not a guarantee that this proposed recipe prevents them. [C-04; GDR-SRC-20261010-G02-008]

For multiplayer or competitive comparison, consistent configuration and interpretation may become additional requirements. No networked implementation, fairness study or ranking policy was inspected. Do not extrapolate a single-player production account to latency compensation or competitive eligibility rules. [C-04]

## Failure cases and do-not-use conditions

| Failure | Observable warning | Candidate correction or exit |
|---|---|---|
| Stale request | Action fires after the player changes plan | Context binding/cancellation/shorter lifetime; omit when intent cannot be represented |
| Double consumption | One press triggers twice or spends a resource unexpectedly | Explicit precedence and single-consumption review |
| Hidden eligibility | Similar-looking states produce inconsistent results | Clarify the rule/state; remove special cases rather than piling on exceptions |
| False diagnosis | The target remains misread despite a higher completion rate | Address affordance/camera information; compare interventions separately |
| Inaccessible cancellation | A supported control mode cannot withdraw a request | Redesign that mode's grammar or provide another route/action |
| Overwritten challenge | The intended decision depended on declining a marginal action | Preserve that contract with another aid; do not impose this pattern |
| Reset leakage | A held or pending action starts an unintended new attempt | Define interruption and re-entry rules; test supported states |

These are proposed failure hypotheses, not reports that every implementation has these defects. Do not use this recipe as automatic aim correction, speculative targeting, network rollback guidance, a substitute for frame-performance review, or a blanket accessibility certification. [C-04; C-05]

## Proposed playtests and rejection rules

**No tests performed.** Recruit participants for the actual input grammar, experience range and relevant motor/access needs. Explain recording/telemetry and allow withdrawal. Choose sample and local meaningful-change criteria after the task and variability are known; no numerical default is supplied. [C-06]

Compare a baseline with explicitly specified early-only, recent-state-only and combined candidates when both are justified. Hold geometry, visual state and checkpoint conditions stable. Include tasks where action is desired and tasks where cancellation is desired. Use counterbalanced matched arrangements; repeated familiarity and learning of a particular queue are confounds. Compare supported remaps/hold/toggle settings separately rather than assume parity. [C-06]

Measure action-state matching, unintended activation, resource errors, predictability explanations, fatigue and task success. For a learning claim, add a new arrangement using the same rule and a later return; do not relabel improved completion under the changed rule as unassisted skill transfer. Reject or narrow the pattern when unwanted actions or loss of control offset the declared benefit, when a presentation-only alternative suffices, or when important access barriers remain unsolved. Report subgroup differences rather than averaging away a harmful mode. [C-06]

## Claim ledger

| ID | Material claim and class | Evidence / locator | Confidence and remaining question |
|---|---|---|---|
| C-01 | Bounded grace may better express chosen near-boundary actions without unwanted delay. `hypothesis` | GDR-SRC-20261010-G02-001 forgiveness rationale motivates the proposal | Low causal confidence; creator account is not a matched intention/effect test |
| C-02 | Celeste's creator describes early and recently-lost-state allowances. `practitioner-heuristic` | GDR-SRC-20261010-G02-001 items 1–2 and conclusion | High for described technique; no universal timing, necessity or measured benefit |
| C-03 | A coherent recipe needs explicit eligibility, expiry, context and consumption semantics. `inference` | Logical requirements of this proposed state/request model; GDR-SRC-20261010-G02-001 as context | Moderate design rationale; implementation and action grammar remain local |
| C-04 | Grace can conflict with cancellation, resource costs and the intended challenge; narrowing or omission may be preferable. `inference` | C-03 reasoning; GDR-SRC-20261010-G02-008 V1.4.0.0 assist/reset correction context | Moderate for possible failure mechanisms, not empirical prevalence. G02-CON-01 |
| C-05 | Input and information barriers need distinct remedies and scoped accessibility review. `inference` | GDR-SRC-20261010-G02-005 Introduction; GDR-SRC-20261010-G02-006 Background/implementation; comparison reasoning | Moderate; no access guarantee or normative threshold. G02-CON-05 |
| C-06 | Evaluation should test intended and unwanted actions, not completion alone, and separately test any learning claim. `hypothesis` | Proposed protocol from C-01/03/04; supplied evidence rules and F01 correction constraint | Low for protocol sensitivity until piloted; no results, participants or prototype here |
| C-07 | The springboard and device scenarios illustrate application and cancellation counterexamples. `hypothesis` | Synthetic worked examples, not external game observations | Low transfer confidence; non-platforming application especially unvalidated |

## Related entries, coverage and history

Relevant draft genres are [platformer](../genres/platformer.md), [precision platformer](../genres/precision-platformer.md) and [metroidvania](../genres/metroidvania.md). The last is conditional on execution rather than navigation being the bottleneck. The [recoverable gate pattern](recoverable-ability-gate-loop.md) solves a different problem and cannot be replaced by input grace.

Shared dependencies F04 and P02/P03 remain missing; no reviewed source bytes or canonical topic links are transferred. First-wave F01/P01 corrections are known only from the supplied review receipt. Research covered the creator mechanism account, action-semantics reasoning and primary accessibility/production context. It did not cover measured optimal windows, different engines/devices, network play, representative access outcomes or learning efficacy. The next discriminating question is whether the local command rule improves **chosen** action expression without increasing unwanted actions.

**Author self-review:** treating intent as “a command close to eligibility” is the strongest potential error. It can erase a deliberate change of mind. The recipe therefore requires cancellation cases and alternatives, and remains a low-confidence recommendation pending local evidence. This self-review is not independent review.

Version `0.1.0`, candidate revision `initial-1`; predecessor/supersession null. Exact bytes are recorded in the [packet](../reviews/full-run-20261010-g02-review-packet.md#candidate-inventory-and-byte-integrity). Gate C independent review pending; Gate D host/retrieval and Gate E release not passed. No implementation or adoption is authorized.

## References

### GDR-SRC-20261010-G02-001

**Maddy Thorson. [Celeste & Forgiveness](https://www.maddymakesgames.com/articles/celeste_and_forgiveness/index.html).** Maddy Makes Games. Publication/update: unknown; page identifies an earlier Twitter thread but supplies no publication date.

Edition/build: Undated creator article; Celeste build/platform not specified. Accessed **2026-10-10**; access: `full`; type: Primary creator explanation.

**Inspected locator:** Numbered items 1–10 and final paragraph; text inspected, embedded animations not observed.

**Claims supported here:** C-01, C-02; context for C-03. **Limits:** Documents described techniques and creator interpretation, not measured player effects or portable timing constants. **Independence:** Same Celeste production context as GDR-SRC-20261010-G02-008; not independent corroboration. **Rights:** Copyrighted creator text; paraphrase only, no animations redistributed.

### GDR-SRC-20261010-G02-005

**Microsoft Xbox accessibility team. [Xbox Accessibility Guidelines V3.2](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines).** Microsoft Learn. Publication/update: V3.2 published 2023-06-08; inspected page last updated 2026-08-14.

Edition/build: V3.2 hub as served 2026-10-10; page date is distinct from guideline-set version. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary non-normative platform guidance.

**Inspected locator:** Introduction; Overview of XAG components → Example content; version heading and last-updated footer.

**Claims supported here:** C-05. **Limits:** The introduction explicitly excludes compliance/legal-checklist status; no formal-standard claim is made. **Independence:** Common guidance family with GDR-SRC-20261010-G02-006 and GDR-SRC-20261010-G02-007; not independent empirical studies. **Rights:** Microsoft documentation; paraphrase only, example images not redistributed.

### GDR-SRC-20261010-G02-006

**Microsoft Xbox accessibility team. [Xbox Accessibility Guideline 107: Input](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107).** Microsoft Learn. Publication/update: 2026-03-04 last updated on opened page.

Edition/build: XAG 107 page within V3.2 set; live page snapshot checked 2026-10-10. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary non-normative accessibility/input guidance.

**Inspected locator:** Goal; Overview; Background and foundational information → Speed, Complexity, Duration and proposed alternatives; Implementation guidelines → remapping and updated prompts; mobile-input section reviewed for scope only.

**Claims supported here:** C-05. **Limits:** No game-independent timing, sensitivity, target-size or compliance requirement is inferred; core article text was accessible despite an authorization banner. **Independence:** Same XAG guidance family as GDR-SRC-20261010-G02-005/GDR-SRC-20261010-G02-007; cited third-party examples are not additional observations. **Rights:** Microsoft documentation; paraphrase only; embedded example media not inspected as gameplay.

### GDR-SRC-20261010-G02-008

**Celeste development team. [Celeste — Changelog](https://www.celestegame.com/changelog.html).** Celeste official website. Publication/update: unknown for individual entries on page; version labels available.

Edition/build: Page headed V1.4.1.0; cited entries V1.3.0.0, V1.3.1.0 and V1.4.0.0; not a claim about current rollout on every platform. Accessed **2026-10-10**; access: `relevant-excerpt`; type: Primary versioned production artifact.

**Inspected locator:** V1.3.0.0 → UI Design Changes; V1.3.1.0 → Changes and Additions; V1.4.0.0 → New Options, Control Rebinding and Bug Fixes (Farewell bird respawn, Ch5/Ch9 facing, Dash Assist soft locks).

**Claims supported here:** C-04 production context. **Limits:** Observed release-note content only. No game build was run; fixes and option efficacy were not independently reproduced. **Independence:** Same Celeste production context as GDR-SRC-20261010-G02-001; multiple entries are not independent experiments. **Rights:** Copyrighted release notes; brief paraphrase only; no code or media copied.

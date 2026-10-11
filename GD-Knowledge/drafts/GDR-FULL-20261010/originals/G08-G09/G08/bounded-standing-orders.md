---
id: GDR-CAND-20261010-G08-PAT-02
kind: pattern
title: Bounded standing orders
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
attempt_id: G08-authoring-01
run_id: GDR-FULL-20261010
batch_id: G08
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
date_basis: America/Los_Angeles
coverage_state: open
aliases:
- conditional standing orders
- bounded policy delegation
tags:
- automation
- player-control
- exceptions
- resource-authority
- input-burden
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-02
- GDR-CAND-20261010-P02-TOP-03
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-G08-PAT-01
- GDR-CAND-20261010-P02-PAT-01
- GDR-CAND-20261010-P02-PAT-02
related_genres:
- GDR-CAND-20261010-G08-GEN-01
- GDR-CAND-20261010-G08-GEN-02
- GDR-CAND-20261010-G08-GEN-03
source_ids:
- GDR-SRC-20261010-G08-002
- GDR-SRC-20261010-G08-003
- GDR-SRC-20261010-G08-005
- GDR-SRC-20261010-G08-006
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-G08
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded G08 candidate; no predecessor or release claimed.
hash_record: ../reviews/full-run-20261010-g08-integrity-receipt.md
---

> **Draft research, not released guidance.** Version 0.1.0; candidate revision `initial-draft-1`. Independent G08 review, gameplay testing and human acceptance have not occurred. Recommendations labeled `hypothesis` are proposed for evaluation, not established effects. All examples labeled *illustrative* are invented and untested. Dates use America/Los_Angeles; the run ID is unchanged.

# Bounded standing orders

## Purpose

Let a player choose a recurring policy once while retaining authority over its scope, resource use, exceptions and termination. The proposed benefit is less repetitive execution **without silently replacing the strategic decision**. The pattern is not an intelligent agent authorized to pursue any inferred goal; it is a player-visible commitment to a bounded class of actions. No comparative benefit or universal accessibility outcome is established. [C-01]

This can apply to actor behavior, recurring logistics or repeated project activity across genres. The underlying system must distinguish choosing a policy from implementing it. A simpler queue, group command, optional pause or direct action is preferable when it solves the problem with less hidden state. Shared conceptual stewardship belongs in coordination with Foundations and Presentation; G08 does not silently allocate a new canonical home. [C-01; C-08]

## Context and prerequisites

There must be a recognizable repeated intention and a stable, inspectable way to determine whether an action falls within it. The player must be able to know which actors and resources are covered, detect important exceptions and cancel or revise the instruction through an appropriate access route. Relevant world information may remain hidden, but the policy must not obtain privileged information unless the game’s declared rules explicitly grant that capability. [C-04; C-05]

Specify what happens when the instruction is incomplete, contradictory, unaffordable or no longer feasible. The system needs a visible state for an order that is waiting or blocked; silent failure is not equivalent to successful delegation. The policy’s resource permissions and spending priority must be compatible with shared budgets and other commitments. When those facts cannot be specified, stop and prefer a direct or simpler command. [C-04; C-05]

## Mechanism and evidence

Two types of anchor motivate this candidate. Johnson reports automatic shipping and intentional control tradeoffs in *Offworld Trading Company*. Official *Age of Empires IV* advice documents preassigned worker gathering through rally points. These establish described mechanisms, not proof of a generalized usability effect. Zero-K’s state and retreat documentation adds explicit conditions, overrides and a missing-destination case. The complete safeguards and recipe below are original G08 synthesis rather than a claimed transcription of any shipped implementation. [C-02; C-03]

| Causal link | Support/limit |
|---|---|
| A stored instruction selects recurring actions within declared conditions. | A rule/implementation possibility supported by the documented examples; actual G08 runtime is absent. [C-02; C-03] |
| The player no longer needs to reissue the same low-level command. | Logical consequence only for actions genuinely covered and successfully executed; exceptions still require work. [C-04] |
| Freed command effort becomes usable attention for another valued choice. | Hypothesis. Configuration, monitoring and mistrust can consume the apparent saving. [C-01; C-06] |
| The player still owns the priority and can intervene effectively. | Requires legible scope, information permissions, state and cancellation; not established by an “auto” toggle. [C-05] |
| Experience or access improves without removing intended skill. | Unvalidated outcome. Direct control can be the valued activity; removing it can harm the design. [C-01; C-06] |

More automation is not the claim. The proposed comparison concerns a **particular delegated intention** with explicit boundaries and a manual or simpler alternative. [C-01; C-06]

## Recipe

1. **Identify a repeated intention, not just frequent input.** Ask what the player is trying to keep true and which individual actions are repetitions of that same choice. If each action expresses a new preference, route or risk assessment, a standing order may erase the intended play. Stop or narrow to the genuinely repetitive portion. [C-01; C-04]
2. **Name the policy and its owner.** Describe the action in player language and identify who may create, modify or cancel it. Keep an explicit alternative to adopting it. For shared control, decide whether one player may change another’s policy; do not infer authority from access to the same screen. [C-05]
3. **Specify scope and permitted information.** Identify eligible actors, locations, targets and resources. Use only information permitted by the game’s rules. A policy such as “avoid known hazards” must not silently use undiscovered hazards. Define the treatment of stale observations rather than displaying inferred safety as current certainty. [C-04; C-05]
4. **Specify resource and priority bounds.** Declare reserves, spending ceilings or other constraints actually needed by the task. Define interaction with queued jobs, manual commands and shared activity pools. Do not create unnecessary configuration variables merely to make the policy appear sophisticated. If priority cannot be resolved predictably, block and ask for a new decision instead of silently optimizing it. [C-04; C-06]
5. **Define exceptions, expiry and resumption.** Write the condition that starts execution, the conditions that suspend it, what counts as completed, and when the authorization becomes stale. Missing destination, target invalidation, changed ownership or a depleted resource must have a declared result. After an exception, resume only within the still-valid policy; do not treat a newly available route as consent to a different goal. [C-03; C-04; C-05]
6. **Separate received, active, waiting, blocked and canceled state.** Show the policy’s current scope and reason for nonexecution when that matters to the next decision. For a mixed selection, do not imply that one displayed state describes every selected actor. Offer an accessible route to inspect and change the relevant state without emitting every routine event as an urgent alarm. [C-03; C-05]
7. **Preserve a comprehensible intervention path.** State whether a manual order temporarily overrides, replaces, suspends or leaves the standing order intact. Make cancellation stop future authorized actions according to the declared boundary; do not suggest it undoes already resolved consequences. Test resumption after a manual exception rather than assuming players infer it. [C-03; C-05]
8. **Compare with direct action and a simpler aid.** Evaluate the same underlying task with manual control, the bounded policy and, where relevant, grouping or a short queue. Keep timing and known facts comparable when isolating delegation. Remove or narrow the policy when saved repetition is outweighed by misexecution, configuration burden, lost decisions or access failures. [C-06; C-07]

**Exit conditions:** stop using the pattern when the repeated goal is not stable, policy scope cannot be made understandable, required information is unavailable, the system cannot explain a meaningful exception, cancellation is not compatible with the intended stakes, or delegation displaces the very decision the player came to make. “The assistant probably knew what they wanted” is not an exit policy. [C-01; C-05; C-06]

### Adjustable variables

Adjust the size of the controlled group, eligible action class, resource reserve, permitted fallback, confirmation boundary, expiry condition, override semantics and exception presentation. Tune each against a named decision problem. No universal health threshold, queue length, notification interval or automation level is recommended. Timing values from a source game would be its rules, not portable defaults. [C-04; C-05]

## Worked examples

### Illustrative application — harbor cargo policy

A player repeatedly sends approved cargo from a warehouse to a named settlement. The intended policy is: “Deliver this approved cargo while retaining the declared emergency reserve; stop when the route is no longer known to be usable.” The player selects the warehouse and destination, sees the covered cargo class and reserve, and can choose a manual transfer instead. The policy does not decide which settlement deserves aid. [C-01; C-04]

Routine transfers proceed only while the destination and resource conditions remain valid. When a newly observed closure blocks the route, the policy becomes blocked with an inspectable reason. It does not switch to a different settlement, spend the reserve or select an undiscovered bypass. The player can authorize a new route, suspend deliveries or cancel the policy. If a manual transfer occurs, the contract must state whether routine service resumes afterward. These are invented local rules, not a reported game feature. [C-04; C-05]

In a cooperative version, the warehouse owner may propose a delivery policy while the team controls a common transport budget. Decide whether the team approves reservations before execution or allocates a protected allowance. A shared activity pool creates a real conflict if automatic deliveries consume all capacity before a new repair priority can be chosen. Merely labeling the behavior helpful would conceal that allocation decision. [C-04; C-06]

### Documented exception versus invented safeguard

The Zero-K retreat page says retreat depends on a retreat zone and describes returning to activity after repair. That documented prerequisite is useful because “retreat enabled” is not the same as a destination being available. G08’s suggestion to communicate the blocked reason and recheck whether the prior intent is still valid is an **inference/hypothesis**, not a claim that the documented game currently implements every safeguard in this recipe. [C-03; C-05]

### Illustrative turn-based adaptation

An actor has a standing instruction to continue a project next round. Before spending the new common action pool, the player can inspect the commitment and its priority. If a newly revealed condition invalidates the target, the order blocks rather than consuming a substitute action. This can reduce routine re-entry work, but inspecting many such policies can itself become upkeep. The turn-based adaptation is proposed and untested. [C-04; C-06]

## Tradeoffs and alternatives

A group command changes selection effort without storing a continuing policy. A finite queue expresses a sequence without promising indefinite repetition. An exception-triggered pause changes temporal opportunity rather than choosing an action. A smaller actor roster may remove the monitoring problem entirely. Direct control preserves decisions about timing and route that a standing policy might flatten. Compare these alternatives with the specific repeated intention, not an abstract automation percentage. [C-01; C-06]

Standing orders introduce a second object for the player to understand: the current world state and the stored policy that acts on it. They can fail through stale assumptions even when each individual action is legal. Production therefore includes policy-state presentation, conflicting instructions, resource reservations, ownership changes, save/re-entry, accessibility and localization. This is a risk inventory, not an implementation architecture, engineering estimate or proof that deterministic behavior is sufficient for trust. [C-05; C-06]

Localization should preserve the difference between “repeat,” “continue when possible,” “use this fallback” and “ask again.” A color-only automation indicator cannot establish nonvisual access. Serial narration of every routine completion may compete with an urgent exception; a persistent history or requested summary is an alternative to test. No specific notification schedule or accessibility equivalence is established here. [C-05]

## Failure cases

| Potential observed failure | Why it challenges the pattern | Conditional correction |
|---|---|---|
| A policy does nothing because a prerequisite is absent | The player may mistake stored permission for executable work. | Explain the prerequisite or offer a direct action; do not claim success. |
| A mixed selection shows one policy as though it applied to all | The player cannot predict the controlled scope. | Provide a way to inspect or intentionally unify states; test the resulting workload. |
| Manual intervention is immediately undone by the policy | Override and resumption semantics are unclear or wrong for the goal. | Replace, suspend or explicitly resume according to the declared contract. |
| Automation spends a reserve or shared pool unexpectedly | Resource authority or priority is not actually bounded. | Block the conflicting commitment or revise the authorization boundary. |
| The player repeatedly checks everything the policy does | Mistrust, opaque state, unstable intent or enjoyment of direct control may eliminate the expected saving. | Make outcomes explainable, narrow the task, or remove the policy. |
| An alternative channel reveals a hidden target | The information policy differs across access routes. | Preserve permitted facts and uncertainty; do not call the advantage necessary accessibility. |

These are prospective failure cases and interpretations, not measured incident rates. [C-03; C-05; C-06]

## Counterexamples and do-not-use conditions

The strongest contrary case is a manual-routing challenge in which selecting and revising a route under pressure is the valued strategic activity. Automatic routing could eliminate its purpose. Johnson’s acknowledged shipping-control tradeoff prevents treating reduced manual selection as a cost-free improvement. A second countercase is an infrequent action: creating, explaining and checking a persistent policy may cost more than simply issuing the action once. [C-02; C-06]

Do not use the recipe to impose undisclosed optimization, choose player goals, hide information advantages, preserve unwanted recurring obligations or justify removal of manual/access alternatives without evaluation. A competitive mode needs explicit permitted-policy rules; a cooperative mode needs explicit shared authority. This pattern does not authorize any real external automation, purchase or action outside a game’s separately approved design. [C-05; C-08]

## Playtest

**Proposed; not performed.** Compare manual control, a short queue/group aid and the bounded policy on matched scenarios. Hold simulation pace constant for the delegation comparison and evaluate pause/speed separately when relevant. Include ordinary repetition and at least one missing prerequisite, changed target, manual override and shared-resource conflict. Recruit relevant prior-experience and access/language profiles rather than testing only the author’s preferred interface. [C-07]

Before acting, capture the player’s intended policy through an appropriate verbal or nonverbal route. Measure unintended actions, interpretation of blocked state, cancellation success, recovery after an exception, configuration/monitoring effort and remaining ownership of the strategic choice. Measure burden and control directly rather than assuming fewer clicks means improvement. Retain required supports and ordinary facts. Counterbalance scenario order and record learning, partner dominance and prior automation familiarity. [C-05; C-07]

Reject or narrow the policy when it supplies no valued reduction in repetition, repeatedly requires redundant checking, changes the intended decision, creates unacceptable access or resource-authority failures, or leaks protected information. Set practical margins and sampling before the study; a correct result alone cannot excuse an unintended policy. A new scenario under the same rule tests transfer; a changed override or priority rule tests adaptation/discrimination separately. No participant, prototype or player result exists for this proposal. [C-07]

## Related entries

Conditional routes: [Strategy](../genres/strategy.md), [RTS](../genres/real-time-strategy.md), [TBS](../genres/turn-based-strategy.md), and [Shared activation budget](shared-activation-budget.md). The inspected P02 `recoverable-action-remapping` (`GDR-CAND-20261010-P02-PAT-01`) concerns control configuration, not stored behavior; P02 `fact-preserving-cue-alternatives` (`GDR-CAND-20261010-P02-PAT-02`) constrains policy-state communication. F07 `legible-commitment-and-safe-exit` (`GDR-CAND-20261010-F07-PAT-02`) supplies a broader commitment/exit caution, not this recurring-action mechanism. Applicable simulation/social candidates were not inspected; duplication and final ownership therefore remain open. [C-08]

## Claim ledger

Local C-identities belong only to this file. Confidence concerns the precisely scoped claim, not the whole genre. A source’s description of a mechanic does not establish its benefit. `DEP` references mean inspected reviewed-candidate passages, not newly inspected underlying studies; see the [dependency receipt](../reviews/full-run-20261010-g08-review-packet.md#reviewed-dependency-transfer).

### C-01

**Claim:** A bounded recurring instruction may reduce repetitive execution while preserving the player’s strategic priority, but this benefit is unvalidated.

**Class:** `hypothesis`. **Support and precise locator:** GDR-SRC-20261010-G08-002, shipping rationale; G08 original causal chain and alternatives. **Confidence:** low for comparative benefit; documented mechanisms only. **Applicability, contrary case and unresolved issue:** Configuration, monitoring and loss of valued direct control can reverse the intended benefit; G08-CON-02.

### C-02

**Claim:** The inspected Offworld account and Age of Empires IV advice describe automation or advance assignment with distinct player-control contexts.

**Class:** `observed-example`. **Support and precise locator:** GDR-SRC-20261010-G08-002, shipping/overrides paragraphs (documentary description); GDR-SRC-20261010-G08-003, Rally Point Resources. **Confidence:** high for the observed documents; no hands-on game observation. **Applicability, contrary case and unresolved issue:** Johnson’s intent is separately practitioner evidence in the genre file; neither source measures generic accessibility or enjoyment.

### C-03

**Claim:** Zero-K documentation describes per-unit states, overrides/mixed-state presentation and a retreat dependency on a retreat zone.

**Class:** `observed-example`. **Support and precise locator:** GDR-SRC-20261010-G08-005, opening/Fire State/Move State/Repeat; GDR-SRC-20261010-G08-006, no-zone/repair-resume/cancellation text. **Confidence:** high for documented statements; page/build revision not established. **Applicability, contrary case and unresolved issue:** Same project documentation, not independent usability evidence. G08 safeguards are not attributed as verified shipped behavior.

### C-04

**Claim:** A stored policy requires explicit scope, eligibility, resource priority and exception/expiry rules to determine what it authorizes.

**Class:** `inference`. **Support and precise locator:** Original G08 rule analysis; source 006 supplies a concrete prerequisite; DEP-F02-D and DEP-P02-C. **Confidence:** high for the defined logical need, unverified runtime. **Applicability, contrary case and unresolved issue:** An individually legal action can still violate the player’s intended priority. Hidden information and newly changed conditions require explicit treatment.

### C-05

**Claim:** Policy state, override, cancellation and accessible exception information must preserve the declared authority and information boundary.

**Class:** `inference`. **Support and precise locator:** DEP-P02-C lines 83–145; DEP-P02-F lines 104–123; DEP-P02-M lines 58–108; DEP-P01-A; G08 safeguards. **Confidence:** moderate for the contract distinction; comprehension and usable intervention remain untested. **Applicability, contrary case and unresolved issue:** No universal timing or sensory-equivalence claim. A manual order need not always have the same override semantics, but semantics must be specified.

### C-06

**Claim:** Policy configuration and monitoring can consume saved effort or remove valued route/timing decisions; simpler queues or direct control remain genuine alternatives.

**Class:** `inference`. **Support and precise locator:** Source 002 shipping-control tradeoff; G08 counterexamples and production/state analysis. **Confidence:** moderate for concrete possible tradeoffs, frequency unknown. **Applicability, contrary case and unresolved issue:** No optimal automation percentage, cost estimate or blanket recommendation. Turn-based standing orders may themselves become upkeep.

### C-07

**Claim:** A future comparison should test intended policy, exceptions, authority, access and experienced control separately from command counts or wins.

**Class:** `hypothesis`. **Support and precise locator:** DEP-F07-V; DEP-F01-T lines 98–116; DEP-W02-M line 148; proposed G08 evaluation. **Confidence:** low for comparative effect; no test conducted. **Applicability, contrary case and unresolved issue:** Sampling/margins remain local. Same-rule transfer and changed-rule adaptation are separate; order, coaching and familiarity can confound results.

### C-08

**Claim:** The candidate is distinguished from inspected remapping, cue and generic exit patterns, but final duplication/ownership clearance is pending.

**Class:** `inference`. **Support and precise locator:** DEP-P02-R purpose lines 49–53; DEP-P02-P purpose lines 50–54; DEP-F07-X purpose lines 50–54; G08 scope comparison. **Confidence:** moderate for inspected local distinction; no latest global registry. **Applicability, contrary case and unresolved issue:** No permanent ID, claim of automatic synchronization or approval of a runtime assistant. Proposed shared owners: Foundations with Presentation and Genres.

## References

Source IDs are temporary run-scoped identities, reused throughout G08. Access means the named passages were inspected, not that a game was run. Cross-batch URL/DOI/edition deduplication remains pending.

### GDR-SRC-20261010-G08-002

Soren Johnson. **[OTC Designer Notes #1: Unit Selection](https://www.designer-notes.com/otc-designer-notes-1-unit-selection/)**. Designer Notes. Publication/update: 2016-04-15. Edition/build: Prelaunch Offworld Trading Company design account. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Main article, paragraphs on automatic shipping, override commands, engineers and scout/scan redesign. **Type:** Firsthand developer account. **Limits/independence:** Intent and production tradeoffs, not independent usability measurements. Same author as source 001; broader rhetoric is not adopted. **Rights:** Copyright holder retains rights; paraphrase only. Claims using this source are identified in this entry’s ledger.

### GDR-SRC-20261010-G08-003

AoE Official. **[Age of Empires IV: Tips to Help Get Your Army Up to Speed](https://www.ageofempires.com/news/age-of-empires-iv-tips-to-help-you-get-started/)**. Age of Empires / World’s Edge. Publication/update: 2021-11-03. Edition/build: Launch-era PC advice; no current patch or game execution verified. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Rally Point Resources; When to Age Up; Scout!; The Power of Counters; Group Assignments. **Type:** Official gameplay documentation and practitioner advice. **Limits/independence:** Documented options and advice, not causal effectiveness or a complete counter table. Independent production context from sources 001–002. **Rights:** Microsoft rights retained; paraphrase only. Claims using this source are identified in this entry’s ledger.

### GDR-SRC-20261010-G08-005

Zero-K project documentation contributors; individual authors unknown. **[Unit states](https://zero-k.info/mediawiki/Unit_states)**. Zero-K project wiki. Publication/update: unknown. Edition/build: Mutable documentation snapshot; page revision/build not established. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Opening state/inheritance notes; Fire State; Move State; Repeat. **Type:** Project-hosted rule/interface documentation. **Limits/independence:** Describes configurable behavior, not verified runtime, performance or universal access outcomes. Same documentation ecosystem as source 006. **Rights:** Specific page reuse license not established; paraphrase only. Claims using this source are identified in this entry’s ledger.

### GDR-SRC-20261010-G08-006

Zero-K project documentation contributors; individual authors unknown. **[Retreat](https://zero-k.info/mediawiki/Retreat)**. Zero-K project wiki. Publication/update: unknown. Edition/build: Mutable documentation snapshot; page revision/build not established. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Retreat-zone placement, no-zone condition, repair/resume behavior, manual cancellation. **Type:** Project-hosted rule/interface documentation. **Limits/independence:** A documented exception and recovery sequence, not a reproduced bug or independent study. Related to source 005. **Rights:** Specific page reuse license not established; paraphrase only. Claims using this source are identified in this entry’s ledger.

## Review and history

2026-10-10 — first pattern draft in G08, `initial-draft-1`, attempt `G08-authoring-01`. Candidate ID persists through corrections. Predecessor and supersession are null; exact delivered hashes are recorded outside this file to avoid self-reference. No canonical receipt, Library upload or independent G08 approval is claimed.

Evidence and heading coverage remain open. The [review packet](../reviews/full-run-20261010-g08-review-packet.md) records contradictions, missing bodies, complete inventory, proposed index rows and queued child work. Additional research must retain existing identities; child keys require Library Coordination registration before submission. The next decision is independent content review of these conditional recommendations and boundaries, not implementation or release.

---
id: GDR-CAND-20261010-G08-PAT-01
kind: pattern
title: Shared activation budget
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
- common action pool
- pooled activation allowance
tags:
- prioritization
- action-economy
- commitment
- resource-budget
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-G08-PAT-02
- GDR-CAND-20261010-F02-PAT-01
related_genres:
- GDR-CAND-20261010-G08-GEN-01
- GDR-CAND-20261010-G08-GEN-02
- GDR-CAND-20261010-G08-GEN-03
source_ids:
- GDR-SRC-20261010-G08-001
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

# Shared activation budget

## Purpose

Create an explicit choice about **which actors or projects receive activity now** when they cannot all act to the desired extent. The proposed player-facing benefit is intentional prioritization across a set of commitments, not merely fewer inputs or a shorter turn. This pattern alters the rules governing feasible activity; it is different from displaying the opportunity cost of an already existing choice. [C-01; C-03]

This is a reusable candidate, not an accepted best practice. It can apply to strategic projects, collaborative roles or other systems where several actions compete for a common allowance. A genre label alone is not a prerequisite. Foundations owns the shared action/economy concepts; stewardship and any overlap resolution remain proposed for coordination. [C-07]

## Context and prerequisites

Apply only when there are at least two genuinely relevant uses of a common activity resource, the player or group has authority to prioritize them, and the scope of the budget can be explained. It must be possible to distinguish available, reserved and spent capacity and to explain what restores it. Actor-specific restrictions, compulsory tasks and information-release boundaries must already be describable. These are logical prerequisites of the proposed rule, not claims about measured player understanding. [C-03]

The team must be able to represent blocked actions and cancellation without inventing refunds or undoing information. A pool shared by teammates also needs an explicit decision owner or consent rule; sharing the resource does not establish equal voice. Keep ordinary state information and necessary access supports available. Do not make mastery or a high win rate a precondition for an accommodation. [C-04; C-05; C-06]

## Mechanism and evidence

Johnson’s *Old World* Orders account is the firsthand anchor: a shared resource makes activities compete, while repeated activation limits were part of iteration. It demonstrates a reported design mechanism and the creator’s rationale, not a controlled comparison proving better strategy or lower burden. The complete recipe below is G08 synthesis; its safeguards and tests are not attributed to Johnson as an original published pattern. [C-02; source 001]

| Causal link | Support and uncertainty |
|---|---|
| A finite common pool with specified costs excludes some combinations of actions. | Conditional rule/arithmetic inference. True only for the defined state, costs and reservation rules. [C-03] |
| Excluded combinations become recognizable foregone alternatives. | Presentation and comprehension hypothesis. A pool can be invisible, confusing or consumed by compulsory upkeep. [C-04] |
| Recognized alternatives allow priorities to affect the chosen allocation. | Plausible agency mechanism, not guaranteed; the player may lack authority or face a dominant option. [C-01; C-04] |
| Prioritization improves the intended experience without unacceptable burden. | Low-confidence hypothesis. Search complexity, lost contribution and waiting can outweigh the value. [C-01; C-05] |
| Fewer activations shorten or simplify turns. | **Not established and not entailed.** Additional order combinations can increase deliberation. [C-05] |

The pattern therefore recommends a discriminating comparison, not automatic adoption. An improvement in game outcome alone cannot demonstrate that the player understood or valued the allocation decision. [C-06]

## Recipe

1. **Name the intended competing priorities.** Write two feasible plans that cannot both be fully realized under the proposed constraint. Identify the player-facing reason to choose between them. If every action is compulsory or one plan dominates under all relevant conditions, stop: a common pool is not yet justified. Use independent allowances, fewer required tasks or a different objective instead. [C-01; C-03]
2. **Define the budget boundary.** Identify its owner, eligible actors/actions, refresh event, whether unused capacity carries, and any maximum stored amount. Decide whether the budget is per turn, phase, encounter or another explicit boundary. A replenishing real-time variant is a separate hypothesis, not an automatic conversion of a turn rule. [C-03; C-05]
3. **Separate available, reserved and spent capacity.** Specify when planning reserves an amount, when resolution spends it and when cancellation releases it. For conditional or interrupted actions, state the refund rule. Reject any interface that suggests resources were restored when they were not. A refund never implies forgetting newly revealed information. [C-03; C-04]
4. **Specify actor and sequence constraints independently.** A common pool does not itself prevent repeated activity by one actor. Decide whether repetition, per-actor caps, travel or other costs should limit concentration. Do not import another game’s fatigue values. Check whether a restriction creates a valued tradeoff or only requires distributing routine chores. [C-02; C-03; C-05]
5. **Make the real tradeoff inspectable.** Present enough information to distinguish a legal allocation from an unavailable combination and to identify at least one relevant foregone use when that comparison is part of the intended decision. Do not label a preferred choice “wrong” merely because another action remains affordable. Preserve access to the same facts and uncertainty through the intended modalities. [C-04; C-06]
6. **Define group authority and automated spending.** State who may reserve, commit or cancel shared capacity. Standing orders must have a known position in the spending order; they must not silently consume newly available capacity ahead of current priorities. For a cooperative design, consider protected role allowances or explicit joint commitment as alternatives, not proven fixes. [C-05]
7. **Specify the transition and failure states.** Document insufficient budget, lost actor, invalid target, simultaneous claim, canceled plan and refresh. Decide whether a blocked order waits, expires, requests a new decision or chooses a previously authorized fallback. Do not invent an automatic substitute priority. [C-03; C-04]
8. **Compare, then keep, narrow or remove.** Under separate evaluation authorization, compare the pool against independent allowances or a simpler reduced-action design. Retain it only when it exposes the desired choice with acceptable comprehension, access, contribution and burden. A smaller number of commands is not a sufficient success criterion. [C-01; C-05; C-06]

**Exit condition:** abandon or narrow the recipe when meaningful allocation alternatives cannot be demonstrated, compulsory work consumes the pool, the intended owner cannot control its use, required information is inaccessible, or intervention costs outweigh the target experience. A source game’s popularity or the designer’s liking for scarce actions cannot override these conditions. [C-01; C-05]

### Adjustable variables

Adjust eligible activity, pool size, refresh/carry rules, reservation timing, action costs, repetition constraints, private versus shared ownership, visibility, and automation priority. Values must be locally justified. Changes to action costs can alter which plans are feasible; changes to presentation can alter understanding without changing feasibility; changes to the clock alter time pressure. Do not treat those manipulations as equivalent or tune all of them at once and assign one cause. [C-03; C-06]

## Worked examples

### Illustrative application — ferry, crossing and survey

Assume a planning round has five tokens; ferry delivery costs two, crossing repair costs three, survey costs one. These invented values illustrate feasibility, not balance recommendations. Delivery plus repair uses the exact available amount and is permitted by this example’s explicit inclusive rule. Repair plus survey leaves one unused token; the player may accept that if learning and access matter more than delivery. Spending less than the full allowance is not automatically a mistake. [C-03; C-06]

Choose the information boundary. In one version, survey resolves before the remainder of the round is committed. In another, every action is locked before survey information arrives. The pool is numerically unchanged but the policy choice is different. The example therefore requires both an action budget and a commitment contract. An undo after survey can restore the pool while retaining knowledge, so it is not equivalent to a fresh unobserved decision. [C-03; C-04]

Now add a second player who owns the ferry destination. A shared pool could let the first player reserve all five tokens and prevent that contribution. A protected allowance, a proposed reservation requiring agreement, or independent role budgets are alternative local designs. Test them against the intended collaboration rather than assuming the shared pool is inherently cooperative. [C-05]

### Illustrative real-time adaptation — dispatch capacity

A concurrent logistics scenario could replenish dispatch capacity while vehicles act. This might make issuing a burst of new commitments compete with retaining flexibility, but it could also encourage stockpiling, waiting or mechanically timed spending. It is an **untested extension** of this recipe, not an observed feature of the *Old World* account. Compare it separately against command queues, fewer simultaneous demands or optional pause; preserve the world clock and information policy during a budget-only comparison. [C-05; C-06]

## Tradeoffs and alternatives

Independent allowances preserve each actor’s recurring opportunity. Alternating activations change response timing. Reducing the number of actors can reduce maintenance without creating another resource. Explicit project slots can express long commitments without charging every low-level action. A purely presentational opportunity-cost comparison can improve understanding without changing the rule set. These are original alternatives for the stated problem; none is generally superior. [C-01; C-03; C-05]

Potential production costs include representing reservations, resolving competing claims, explaining invalidated sequences and testing carry/refresh boundaries. A cap can concentrate work in fewer actions but require more comparison among sequences. Accessibility work includes understanding current capacity without remembering a prior screen or performing avoidable arithmetic. No implementation cost estimate or measured cognitive reduction is provided. [C-04; C-05]

## Failure cases

| Observable warning in a future evaluation | Competing explanations to investigate | Possible revision, not automatic cure |
|---|---|---|
| Everyone spends on the same compulsory action first | Mandatory upkeep or dominant choice, rather than deliberate prioritization | Remove upkeep from the pool, change the objective, or discard the pool. |
| One actor or teammate routinely consumes all capacity | Intended specialization, exploit, authority imbalance or misunderstood limits | Ask whether concentration is desired before adding caps or protected allocations. |
| Players repeatedly predict legality incorrectly | Reservation wording, inaccessible state, arithmetic burden or rule inconsistency | Improve state representation; do not infer unwillingness to learn. |
| Turns contain fewer actions but more unwanted search | New combinations or fear of irreversibility | Simplify choices, offer appropriate drafting support, or restore independent allowances. |
| Automatic actions spend the new pool unexpectedly | Ambiguous priority or stale policy | Suspend or re-confirm the affected policy at the relevant boundary. |

These are proposed observations and diagnostic options, not reported test results. [C-04; C-05; C-06]

## Counterexamples and do-not-use conditions

Do not use a common activation pool merely to make every decision feel costly. It is a poor fit when the intended promise is uninterrupted exercise of each role, when scarcity produces only unavoidable omissions, or when the group cannot fairly authorize shared spending. A freely expressive construction mode may be harmed by an activity tax unrelated to its goals. A system with few consequential actors may gain little from another visible currency. These are illustrative countercases, not a universal ban. [C-01; C-05]

The strongest contrary case is a well-functioning independent-allowance design whose sequence and positioning already provide meaningful commitments. Replacing it with a common pool can destroy that structure without solving a player problem. The creator anchor does not disprove this alternative. [C-02; C-05]

## Playtest

**Proposed; not performed.** Compare independent allowances and a common pool with equivalent objectives, actors, information and access supports. State which differences cannot be held constant, because changing the feasible set is the intervention. Predefine the intended opportunity conflict and practical margins for burden, comprehension and contribution. Select participants from the intended mode and access/language profiles; justify sampling for the question rather than adopting a fixed genre number. [C-06]

Observe the chosen priority and feasible foregone plan, not only resource utilization. Measure legality predictions, unintended reservations, plan revision, experienced burden and cooperative contribution separately. Include exact-budget, affordable and unaffordable cases with changed correct answers. For example, with eight owned and a proposed spend of four, reservations of three, five and four imply permitted, not permitted and permitted under an inclusive availability rule. These are illustrative proposed probes, not validated assessment items. [C-03; C-06]

Control or record arithmetic familiarity, tutoring, interface cues, role power and scenario order. A same-rule unfamiliar situation is a transfer probe; changing refill or reservation rules tests adaptation/discrimination separately. Necessary supports and ordinary state information remain in place. Reject the pattern locally when meaningful prioritization does not improve, unwanted burden rises beyond the predeclared margin, or contribution/access failures are unacceptable even if aggregate outcomes improve. No result or statistical power is claimed. [C-06]

## Related entries

Applies conditionally to [Strategy](../genres/strategy.md), [TBS](../genres/turn-based-strategy.md), and the explicitly hypothetical dispatch variant in [RTS](../genres/real-time-strategy.md). It can interact with [Bounded standing orders](bounded-standing-orders.md), which must respect the pool’s spending priority. Existing F02 `visible-opportunity-cost-comparison` (`GDR-CAND-20261010-F02-PAT-01`) explains a tradeoff; it does not create this shared allowance. F03 `conversion-loop-budget` is known only from its packet and has not been cleared as a dependency. Global conceptual duplication and ownership remain pending. [C-07]

## Claim ledger

Local C-identities belong only to this file. Confidence concerns the precisely scoped claim, not the whole genre. A source’s description of a mechanic does not establish its benefit. `DEP` references mean inspected reviewed-candidate passages, not newly inspected underlying studies; see the [dependency receipt](../reviews/full-run-20261010-g08-review-packet.md#reviewed-dependency-transfer).

### C-01

**Claim:** A common activity allowance may support valued prioritization when multiple relevant uses compete and the player can control the allocation.

**Class:** `hypothesis`. **Support and precise locator:** GDR-SRC-20261010-G08-001, Orders rationale; original G08 recipe and alternatives. **Confidence:** low for experienced benefit; no comparative study of this recipe. **Applicability, contrary case and unresolved issue:** Compulsory upkeep, dominant choices, lost role contribution or needless currency can defeat the purpose; G08-CON-01.

### C-02

**Claim:** The Old World designer account reports shared Orders and iterative limits on repeated unit activity.

**Class:** `practitioner-heuristic`. **Support and precise locator:** GDR-SRC-20261010-G08-001, Orders/fatigue/Force March paragraphs. **Confidence:** high for reported design rationale; not independent efficacy evidence. **Applicability, contrary case and unresolved issue:** No prototype metrics supplied; source rhetoric about other structures is not adopted, nor are its numerical costs recommended.

### C-03

**Claim:** Under explicit costs and reservation rules, a finite common pool determines which combinations are feasible; it does not determine which legal plan the player should prefer.

**Class:** `inference`. **Support and precise locator:** Conditional arithmetic in the illustrative five-token example; DEP-F02-D lines 53–103; DEP-F01-T lines 98–116. **Confidence:** high for the defined logical model. **Applicability, contrary case and unresolved issue:** Actual runtime and unexpected state changes unverified. Inclusive exact-budget permission is specified for the example, not every game.

### C-04

**Claim:** Recognizing a foregone alternative and understanding reservations are necessary application assumptions, not benefits established by merely adding the pool.

**Class:** `hypothesis`. **Support and precise locator:** DEP-F02-D; DEP-P02-C/F/M inspected contracts; original G08 causal-link analysis. **Confidence:** low for comprehension outcomes; logical need is clear. **Applicability, contrary case and unresolved issue:** Unclear state, modality gaps or leaked information can invalidate the intended comparison. No universal interface or threshold.

### C-05

**Claim:** Common budgets can increase search, concentrate activity, generate compulsory omissions or conflict with standing orders and shared authority.

**Class:** `inference`. **Support and precise locator:** Source 001 iteration as narrow motivation; original counterexamples and state analysis; DEP-F07-E. **Confidence:** moderate for plausible and constructive failure cases, incidence unknown. **Applicability, contrary case and unresolved issue:** Does not show those failures occur in every design. Replenishing RTS adaptation and proposed fixes remain untested hypotheses.

### C-06

**Claim:** Evaluation should compare meaningful allocations, comprehension, burden and contribution while separating permitted action from preference and transfer from rule adaptation.

**Class:** `hypothesis`. **Support and precise locator:** DEP-F07-V lines 57–98; DEP-F01-T lines 98–116; DEP-W02-M line 148; proposed G08 comparison. **Confidence:** low for intervention benefit; no tests performed. **Applicability, contrary case and unresolved issue:** Prior familiarity, coaching, arithmetic and sequencing confound results; local practical margins/sampling need approval.

### C-07

**Claim:** The candidate changes the shared action rule, while the inspected F02 comparison pattern explains an existing opportunity cost; final ownership/duplication clearance remains pending.

**Class:** `inference`. **Support and precise locator:** DEP-F02-P purpose lines 45–49; current G08 dispatch and local scope comparison. **Confidence:** moderate for the inspected distinction; latest registry absent. **Applicability, contrary case and unresolved issue:** No canonical allocation or cross-project synchronization. Proposed shared owner: Foundations, coordinated with Genres and Presentation.

## References

Source IDs are temporary run-scoped identities, reused throughout G08. Access means the named passages were inspected, not that a game was run. Cross-batch URL/DOI/edition deduplication remains pending.

### GDR-SRC-20261010-G08-001

Soren Johnson. **[Old World Designer Notes #1: Orders](https://www.designer-notes.com/old-world-designer-notes-1-orders/)**. Designer Notes. Publication/update: 2021-07-26. Edition/build: Historical design retrospective; no executable build inspected. Accessed 2026-10-10 (America/Los_Angeles); `access: relevant-excerpt`.

**Locator:** Main article, paragraphs on shared Orders, rejected prototypes, fatigue and Force March; author comment on unit caps. **Type:** Firsthand developer account. **Limits/independence:** Designer rationale and internal iteration, not a measured player-benefit study. Same author as source 002. **Rights:** Copyright holder retains rights; paraphrased, no source payload redistributed. Claims using this source are identified in this entry’s ledger.

## Review and history

2026-10-10 — first pattern draft in G08, `initial-draft-1`, attempt `G08-authoring-01`. Candidate ID persists through corrections. Predecessor and supersession are null; exact delivered hashes are recorded outside this file to avoid self-reference. No canonical receipt, Library upload or independent G08 approval is claimed.

Evidence and heading coverage remain open. The [review packet](../reviews/full-run-20261010-g08-review-packet.md) records contradictions, missing bodies, complete inventory, proposed index rows and queued child work. Additional research must retain existing identities; child keys require Library Coordination registration before submission. The next decision is independent content review of these conditional recommendations and boundaries, not implementation or release.

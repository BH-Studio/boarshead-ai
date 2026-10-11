---
id: GDR-CAND-20261010-G12-PAT-02
kind: pattern
title: Bounded delegation contract
version: 0.1.0
status: draft
candidate_revision: initial-author-draft-1
attempt_identity: G12-authoring-01
run_id: GDR-FULL-20261010
batch_id: G12
id_scope: run-scoped-temporary
owner_project: BH-GDR-Genres
updated: '2026-10-11'
evidence_checked: '2026-10-11'
date_basis: UTC; dispatch and Los Angeles work date 2026-10-10 retained in run identity
coverage_status: open
aliases:
- inspectable automation limits
- delegated authority boundaries
tags:
- automation
- agency
- scope
- exception-handling
- recovery
related_topics:
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-G12-PAT-01
related_genres:
- GDR-CAND-20261010-G12-GEN-01
- GDR-CAND-20261010-G12-GEN-02
- GDR-CAND-20261010-G12-GEN-03
source_ids:
- GDR-SRC-20261010-G12-005
- GDR-SRC-20261010-G12-006
- GDR-SRC-20261010-G12-007
- GDR-SRC-20261010-G12-009
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial G12 bounded research draft; previous batch identities and queues are not reset.
hash_record: ../reviews/full-run-20261010-g12-integrity-receipt.md
proposed_domain_owner: BH-GDR-Foundations-and-Systems; ownership/overlap review pending
---

# Bounded delegation contract

**Unvalidated pattern candidate.** Make delegated authority inspectable and limited while retaining the decisions the player is meant to make. Its purpose is neither maximum automation nor a guarantee of optimal behavior. Benefits to burden, agency or comprehension remain hypotheses. [C-01, C-05]

## Purpose

Help a player understand **what an automation may do, under which conditions, and what remains their decision**. The proposed contract states scope, trigger, permitted action, limits, exceptions and stop behavior. “Contract” here means a player-facing design agreement, not a legal contract or a formal technical standard. [C-01]

The problem is most relevant when repeated execution distracts from desired supervisory choices, or when an automatic rule otherwise acts beyond what a player reasonably expects. It can be counterproductive when the repeated operation itself is the intended challenge, expression or learning target. [C-05, C-07]

## Context and prerequisites

The model must distinguish authorization from execution, provide reliable scope and state, and support meaningful limits or an honest statement that a limit cannot be enforced. The player must have an understandable way to inspect, revise or stop future authorization. The design must specify responsibility for exceptions; silently ignoring an impossible instruction is not a complete policy. [C-01, C-06]

For this recipe, delegation means execution according to a chosen rule or agent policy. It does not require machine learning, an optimal planner or a programmable language. A fixed replenishment rule can qualify. An invisible balancing subsidy is not automatically player-directed delegation merely because it changes outcomes. Those mechanisms may be appropriate for different purposes, but must not be conflated. [C-01, C-04]

## Mechanism and evidence

| Proposed causal link | Support | Limit and disconfirming case |
|---|---|---|
| Repeated assignment can be moved into scheduling logic. | Wube’s robot account provides a concrete production route. [C-02; GDR-SRC-20261010-G12-005] | Engineering feasibility is not evidence that players want that work removed. |
| Conditions and stop semantics can delimit subsequent execution. | OpenTTD’s conditional-order documentation and Factorio’s new-versus-current delivery distinction. [C-03; GDR-SRC-20261010-G12-007, GDR-SRC-20261010-G12-006] | A condition can be incomprehensible; stopping new work can leave consequential current work. |
| Making authority explicit may reduce surprise and preserve supervisory choice. | Inference motivating this **hypothesis**, using DEP-UI and DEP-DECISION. [C-05] | No cited comparison tests this complete contract; setup and exception work may exceed savings. |
| A declared goal and recovery policy may better match player expectations than an invisible intervention. | Historical economy-revision rationale is a design case, not player-effect proof. [C-04, C-05; GDR-SRC-20261010-G12-009] | Forgiving invisible rules can serve an intended toy-like experience; explicit control is not universally better. |

The Factorio reactor discussion also recognizes a cost of direct access to previously inferred information. Treat this as a practitioner countercase to “automation and transparency are always upgrades,” not a measured effect size. [C-07; GDR-SRC-20261010-G12-006]

## Recipe

1. **Name the retained decision.** Write what the player should still choose—such as service priority, acceptable reserve, preferred route or staffing policy—and which repeated execution is being delegated. Compare with simply simplifying the task. Exit if delegation removes the intended skill or the only consequential choice. [C-01, C-07]
2. **State the authority boundary.** Identify the affected entities or area, permitted actions, prohibited actions and resource/permission limits. Express limits in the model’s actual units. Do not use a global on/off label for a policy that affects only selected objects. [C-06]
3. **Define trigger, action and exception.** Specify when the rule runs, what it attempts, and what happens when conditions conflict or required resources are missing. Prefer a small readable rule over a powerful language unless programming the policy is itself desired play. A warning, queued review or a safe no-action state may be suitable; choose explicitly. [C-01, C-06]
4. **Preview representative consequences.** Before commitment, show a normal case, a limit case and an exception in accessible language or representation. Explain whether the preview is a deterministic rule trace or an estimate. Do not imply an optimal outcome merely because an action is allowed. [C-05, C-08]
5. **Make stopping precise.** State whether stop means no new authorizations, cancellation of queued work, interruption of current execution or reversal. Show any existing commitments separately. When those capabilities differ, use different controls or wording. Never promise that “off” restores the earlier world. [C-03, C-06]
6. **Provide proportionate inspection and manual recourse.** Show why the latest relevant action was taken and how to change the governing rule. Consolidate repetitive notifications; retain important exceptions. Preserve a usable alternative route to the retained decision, not necessarily an inaccessible manual click sequence. [C-05, C-08]
7. **Handle change and re-entry.** When rules, scope or available actions change, identify what changed and whether a saved policy still means the same thing. Reconfirm consequential authority changes rather than quietly expanding them. These are proposed design obligations, not an implementation performed here. [C-06, C-08]
8. **Test whether the exchange is worthwhile.** Compare desired decisions retained, comprehension, correction work and total burden—not only fewer inputs. Remove, narrow or simplify the contract when configuration becomes the dominant chore or players lose the desired activity. [C-05, C-07, C-09]

### Adjustable variables and exit conditions

Choose scope granularity, trigger frequency, limit types, duration or expiry, policy priority, exception escalation, explanation depth and reversibility according to the model. All quantities are local design parameters; the pattern supplies no universal reserve percentage, alert rate or maximum number of rules. [C-06, C-08]

Exit when the system cannot enforce its stated limits, cannot distinguish pending from completed actions, or cannot explain consequential exceptions. A simpler fixed behavior with honest scope can be preferable to a misleading configurable policy. Do not use this recipe to justify hidden authority escalation, forced automation or an inaccessible manual fallback. [C-06–C-08]

## Worked examples

### Illustrative replenishment policy

**Synthetic, not a shipped implementation.** A workshop player chooses that common fasteners may be replenished from an approved supplier for a selected work area. The rule does not buy rare components, consume a protected reserve or change job priorities. Its trigger considers relevant incoming orders rather than only the empty bin, using [pending-work reconciliation](pending-work-reconciliation.md). The player retains the decision about priority and reserve. [C-01, C-06]

When a supplier cannot fulfill an order, the policy reports the exception rather than silently switching to a more expensive route. A stop control prevents new authorizations. Existing paid shipments remain visible and continue unless the invented model separately supports cancellation. A preview includes a normal replenishment, a reserve-limited case and an unavailable-supplier case. The purpose of the comparison is to see whether these boundaries are understood and useful, not to guarantee that players adopt them. [C-03, C-05, C-09]

A player who enjoys individually scheduling every delivery may prefer the manual mode. Another may need an alternative to repeated fine-motor actions but still want to decide quantities and priorities. Retain the decision while changing how it is expressed; do not equate access with surrendering authority. [C-07, C-08]

### Illustrative district service authority

A fictional city permits a service manager to reassign vehicles **inside one district** during specified conditions, but not close facilities or move resources from another district. A citywide emergency request is an exception requiring the appropriate player choice. Expanding the district boundary changes the policy’s scope and should be visible. This example specifies an invented authority rule; it is not an observation about Cities: Skylines or Frostpunk. [C-06]

**Counterexample:** when the design promise is an engineering puzzle about inferring a hidden operational state, directly reading that state and automating the response can remove the puzzle. When the promise is carefree construction, requiring policy configuration for every routine can impose unnecessary management. A fixed helper, optional assist, slower pacing or no delegation may fit better. [C-07]

## Tradeoffs and alternatives

Delegation trades repeated execution for policy creation, understanding, verification and exception handling. A detailed contract can create a second management problem instead of reducing the first. Alternatives include batch commands, templates, coarse priorities, simplified resource rules, explicit difficulty modes or a limited helper with no configurable conditions. Evaluate each against the retained decision rather than the prestige of a more sophisticated system. [C-05, C-07]

Authority logs and explanations also cost engineering, authoring, localization and maintenance. A state machine that changes after a patch can invalidate saved instructions; long translated rule descriptions can obscure a critical exclusion. Prefer readable terms for scope and stop effects to compact but ambiguous icons. The contract is a proposal for useful bounds, not a claim that every automation must expose its entire internals. [C-06, C-08]

## Failure cases and do-not-use conditions

**Surprise scope:** a rule affects entities outside the player’s selected area. Warning sign: players correctly explain the trigger but cannot predict who is affected. Correct the scope display or the rule. **Stop mismatch:** players believe disabling automation cancels paid or executing work. Show current commitments and separate stop/cancel semantics. [C-03, C-06]

**Exception flood:** rare-case review becomes most of play. Simplify the policy or let players choose an acceptable default with clear costs. **Opaque optimization:** an apparently intelligent agent cannot explain a consequential action or violates the stated goal. Narrow allowed behavior rather than present unexplained confidence. **Hollow management:** there are fewer actions because all valued choices disappeared. Reintroduce a retained decision or offer a different mode. [C-05, C-07]

Do not use the pattern where automatic execution would invalidate a procedure-learning test, where permissions cannot be constrained truthfully, or where the required manual fallback is inaccessible. No automation guarantee is established for multiplayer synchronization, adversarial agents or live services; those contexts need additional design and review. [C-06–C-09]

## Proposed playtest — not performed

Compare **manual execution**, **a simple fixed helper**, and **bounded delegation** for the same underlying objective. Preserve accessible methods of expressing the retained decisions in every condition; “manual” is not the gold standard when it creates an unrelated motor barrier. Recruit for intended planning experience, input devices and access needs; justify sample size and margins later. [C-09]

Include normal execution, a resource limit, an out-of-scope target, an unavailable supplier, stopping with work in flight, and a changed-rule re-entry. Ask players to predict an action and explain its authorization before measuring whether they choose it. Record valued decisions retained, unexpected actions, recovery burden, policy editing time, inspection effort and preference. Fewer clicks or interventions alone do not count as preserved agency. [C-09]

Potential confounds are familiarity with programming-like rules, scenario order, trust in automation, device fluency and different information available across conditions. Reject or narrow the technique if scope/stop errors persist, configuration or exception burden exceeds its intended benefit, or the desired decisions disappear. A subgroup benefit should remain scoped. This proposed experiment does not establish that the implementation is technically correct; enforceable boundaries require separate later checks. [C-05, C-09]

## Related entries, coverage and history

Conditionally applicable to [simulation](../genres/simulation.md), [management](../genres/management.md) and [city builder](../genres/city-builder.md), with [pending-work reconciliation](pending-work-reconciliation.md) as a possible complement. Preserve **G12-CON-03** (delegation versus desired activity) and **G12-CON-06** (safeguards versus legible control). [C-01–C-09]

Version `0.1.0`, `draft`, revision `initial-author-draft-1`; no predecessor or supersession. Evidence covers documented implementation ideas and practitioner concerns, not validation of the complete recipe. Shared Foundations ownership, duplicate-pattern review, controller/assistive workflows, multilingual comprehension and longitudinal experience remain open. Author self-review is not independent review or release.

## Claim ledger

Claim IDs are local to this artifact. Bare three-digit source numbers in a ledger expand to `GDR-SRC-20261010-G12-`; DEP labels resolve in Reviewed dependency provenance. Family abbreviations such as G12-PAT-01 expand to `GDR-CAND-20261010-` plus that family suffix. Confidence concerns the stated claim, not a general endorsement. Recommendations and synthetic examples are not studio-approved decisions. No unperformed test is evidence.

| Claim | Precise claim | Class | Source and locator / reasoning | Confidence and applicability | Unresolved question |
|---|---|---|---|---|---|
| C-01 | A delegation contract can specify retained choices, scope, triggers, permitted actions, limits and exceptions without requiring a programmable optimizer. | inference | 005/007 mechanism routes; DEP-DECISION; explicitly proposed decomposition. | Moderate as a design structure; usefulness not empirically established. | Which retained decision makes the contract worthwhile? |
| C-02 | Wube documents a scheduling change that moves assignment work into revised queue/arrival logic. | practitioner-heuristic | GDR-SRC-20261010-G12-005, Smarter robots. | High for production description; not player-preference evidence. | Does delegating this work fit the target promise? |
| C-03 | Conditional execution and stopping future rather than current work are documented mechanisms, not guarantees of user understanding. | observed-example | GDR-SRC-20261010-G12-007, Effect of order explained; GDR-SRC-20261010-G12-006, Logistic chest enable/disable. | High for the inspected texts; no executed builds or comprehension tests. | Which semantics does the target system actually implement? |
| C-04 | A hidden financial safeguard and player-directed delegation are different mechanisms despite both altering outcomes automatically. | inference | GDR-SRC-20261010-G12-009, THE ECONOMY; recipe’s explicit authority definition. | Moderate conceptual distinction; no universal safeguard verdict. | Is assistance intended as a mode, balancing rule or chosen policy? |
| C-05 | Explicit bounded delegation may reduce surprise or burden, but its net player benefit remains untested and can reverse. | hypothesis | DEP-UI/DEP-DECISION; 005/006/009 context; no study of the combined recipe. | Low causal confidence; exact comparison is proposed only. | Do retained decisions and correction costs improve on a simpler helper? |
| C-06 | Scope, enforceable limits and honest stop/re-entry semantics are conditions for this proposed technique. | hypothesis | 006 delivery distinction; DEP-DECISION reversibility; workshop/district illustrations. | Moderate consistency rationale, low effect evidence. | Can every stated boundary be enforced and interpreted? |
| C-07 | Do not delegate the desired skill or impose configuration on a promise that does not need it. | hypothesis | 006 Reactor circuit connection practitioner countercase; genre-specific invented alternatives. | Moderate purpose-based rationale; no universal preference result. | Which player activity is lost rather than merely simplified? |
| C-08 | Alternative access, explanations and policy maintenance have costs that must be assessed across the whole workflow. | hypothesis | DEP-ACCESS access chain; DEP-UI state/ownership; recipe’s change cases. | Low for implementation-specific benefits; no compliance determination. | Which translation, input or saved-policy transition creates an authority error? |
| C-09 | Evaluate scope understanding, valued decisions and burden separately from fewer inputs in proposed comparisons. | hypothesis | DEP-TRANSFER changed-answer discrimination; DEP-EVALUATION; proposed test section. | Moderate construct rationale; no tests or sample-size claim. | What outcome rejects delegation even if task execution is faster? |

## References

Observer: the G12 authoring assistant, through document inspection, not game execution. Access/check date: **2026-10-11 UTC**. Source IDs are temporary run-scoped identities, reused within G12. Cross-batch canonical URL/DOI/edition deduplication remains pending. `relevant-excerpt` does not mean the full work, runtime or linked material was inspected.

### GDR-SRC-20261010-G12-005

**kovarex; Oxyd; Klonan. _Friday Facts #374 – Smarter robots_.** Publication/update: 2023-09-01. Publisher: Wube Software / Factorio development blog. [Inspected source route](https://www.factorio.com/blog/post/fff-374).

**Claims supported or used as an inference/hypothesis premise:** C-01/C-02; premise for C-05. **Edition/build:** Development account contrasting Factorio 1.1 with work toward 2.0; exact executable build unknown. **Access:** `relevant-excerpt`. **Type:** Firsthand development account. **Exact locator:** “Smarter robots” discussion of closest-idle assignment, per-robot queues, estimated arrival time and simplifying recharge/queue processing.

**Rights:** Copyrighted blog; paraphrase only; animations and code not reproduced. **Limits and independence:** Creator explanation of scheduling changes and engineering tradeoffs, not controlled player evidence. Same Wube production line as 006. Embedded animations were not analyzed as build observations.

### GDR-SRC-20261010-G12-006

**Klonan. _Friday Facts #428 – Reactor & Logistics circuit control_.** Publication/update: 2024-09-13. Publisher: Wube Software / Factorio development blog. [Inspected source route](https://www.factorio.com/blog/post/fff-428).

**Claims supported or used as an inference/hypothesis premise:** C-03/C-07. **Edition/build:** Pre-2.0 development description; executable build unknown. **Access:** `relevant-excerpt`. **Type:** Firsthand development account. **Exact locator:** “Reactor circuit connection”; “Roboport circuit improvements”; “Logistic chest enable/disable”.

**Rights:** Copyrighted blog; paraphrase only. **Limits and independence:** Reports direct reactor signals, tracking limits and disabling new requester orders while existing deliveries finish. Does not validate agency or accessibility effects. LAN-party feedback is an author account, not an inspected controlled dataset; same production line as 005.

### GDR-SRC-20261010-G12-007

**OpenTTD project wiki contributors; individual page authors not established. _Conditional Orders_.** Publication/update: unknown. Publisher: OpenTTD official project-hosted wiki. [Inspected source route](https://wiki.openttd.org/en/Manual/Conditional%20Orders).

**Claims supported or used as an inference/hypothesis premise:** C-01/C-03. **Edition/build:** Mutable community-maintained manual; page revision and executable version unknown. **Access:** `relevant-excerpt`. **Type:** First-party-hosted, community-authored technical manual. **Exact locator:** “Using the interface”; “Steps”; “Effect of order explained”.

**Rights:** GNU Free Documentation License as displayed; paraphrase only; no tutorial images or code reproduced. **Limits and independence:** Documents conditional branching in vehicle orders. Procedure not executed; project hosting does not make it a player experiment or establish individual author expertise.

### GDR-SRC-20261010-G12-009

**Colossal Order. _Dev Diary: Economy 2.0 – Part One_.** Publication/update: 2024-06-03. Publisher: Paradox Interactive / Cities: Skylines II. [Inspected source route](https://www.paradoxinteractive.com/games/cities-skylines-ii/news/dev-diary-economy-part-one).

**Claims supported or used as an inference/hypothesis premise:** C-04; context for C-05. **Edition/build:** Announced Economy 2.0 changes; not a verified installed patch or current build. **Access:** `relevant-excerpt`. **Type:** Firsthand development explanation and reported feedback. **Exact locator:** Introduction; “THE ECONOMY”; “CITY SERVICES”; “DEMAND”.

**Rights:** Copyrighted publisher/developer page; paraphrase only. **Limits and independence:** Explains removal of a hidden subsidy and changes to costs/control. Creator rationale and reported feedback do not prove that fewer safeguards cause greater enjoyment or welfare. Same production line as 008; explicitly historical.

## Reviewed dependency provenance

These are inspected **parent-selected reviewed drafts**, not released references and not new G12 sources. Their underlying cited papers were not automatically re-inspected. Only the named passages are transferred as qualified research guidance. Exact bytes came from the materialized waves 1–2 archive; they are not copied into this output. Full archive and gap receipts are in the [batch dependency record](../reviews/full-run-20261010-g12-review-packet.md#reviewed-dependencies).

**DEP-TRANSFER: `GDR-CAND-20261010-F01-PAT-01`**, version `0.1.0`, `draft`, candidate revision `independent-review-correction-1`. Archive path `selected-drafts/patterns/supported-attempt-and-transfer-check.md`. Inspected: Recipe; corrected Worked examples, lines 96–127: vary the correct feasibility answer, retain accommodations, separate preference from rule prediction. SHA-256 `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1`.

**DEP-UI: `GDR-CAND-20261010-P01-TOP-02`**, version `0.1.0`, `draft`, candidate revision `review-correction-1`. Archive path `selected-drafts/topics/interface-and-information.md`. Inspected: Task information contract and availability-to-recovery diagnostic, lines 55–85. SHA-256 `1381faf6c998295cd0b0472cf3905a28f87d9515d16bacb54ece423fe080595d`.

**DEP-ACCESS: `GDR-CAND-20261010-P01-TOP-03`**, version `0.1.0`, `draft`, candidate revision `review-correction-1`. Archive path `selected-drafts/topics/accessibility-and-inclusive-interaction.md`. Inspected: Applicability/scope and access chain, lines 56–103; P01 CORRECTION_RECEIPT.md. SHA-256 `eab6276ce51dcea359cb599f24ffef603b6062a6d6f6badffa8c0e28a0e79d48`.

**DEP-DECISION: `GDR-CAND-20261010-F02-TOP-01`**, version `0.1.0`, `draft`, candidate revision `initial-capture-1`. Archive path `selected-drafts/topics/decision-design.md`. Inspected: Entitled information, uncertainty, opportunity cost and reversibility, lines 63–104. SHA-256 `2fe66a5bf914a9c3f4101e168cdfd344a26eeadbfea7c45d16a9f17cca33bc6c`.

**DEP-EVALUATION: `GDR-CAND-20261010-F07-TOP-01`**, version `0.1.0`, `draft`, candidate revision `initial-capture-1`. Archive path `selected-drafts/topics/evaluation-and-balancing.md`. Inspected: Evidence-to-question distinctions, lines 65–94: correctness checks do not measure enjoyment. SHA-256 `165879841257f88c0a5ecba1f6db5d8b36089dcb260570d7bed6bcd9496d38b8`.

**DEP-ETHICS: `GDR-CAND-20261010-F07-TOP-02`**, version `0.1.0`, `draft`, candidate revision `initial-capture-1`. Archive path `selected-drafts/topics/ethical-and-sustainable-design.md`. Inspected: Representation and production obligations, lines 70–104: rules and agency are part of representation. SHA-256 `e26241cb08b1e9ddd4181e7cb92494506ae9b03e04e24032a3e9c79fe0169ce0`.

**Transfer boundary:** preserve source/candidate identities as recorded. No universal UI pixel, contrast, timing, difficulty or sample-size rule is imported. F01’s corrected feasibility/transfer discrimination is retained; access supports are not faded as tutorial prompts. Later reviewed simulation/economy/spatial-topic bytes remain missing unless explicitly identified in the packet.


---
id: GDR-CAND-20261010-P04-PAT-02
kind: pattern
title: State-aligned animation handoff
version: 0.1.0
candidate_revision: initial-draft-1
status: draft
owner_project: BH-GDR-Presentation-and-Interaction
run_id: GDR-FULL-20261010
batch_id: P04
attempt_id: P04-authoring-01
updated: '2026-10-11'
evidence_checked: '2026-10-11'
date_basis: UTC; run identifier retains dispatch date 2026-10-10
identity_scope: run-scoped candidate; permanent allocation pending
predecessor_sha256: null
supersedes: null
change_summary: Initial P04 candidate; no predecessor submitted.
aliases:
- animation state handoff
- interruptible motion handoff
tags:
- animation
- interruption
- state-clarity
- recovery
- conditional-recipe
related_topics:
- GDR-CAND-20261010-P04-TOP-02
- GDR-CAND-20261010-P04-TOP-01
related_patterns:
- GDR-CAND-20261010-P04-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-P04-005
- GDR-SRC-20261010-P04-007
- GDR-SRC-20261010-P04-008
- GDR-SRC-20261010-P04-009
- GDR-SRC-20261010-P04-010
- GDR-SRC-20261010-P04-011
reviewer: null
approved_by: null
approved_date: null
---

# State-aligned animation handoff

**Draft 0.1.0 / initial-draft-1; hypothesis-led, not implemented or validated.** This pattern coordinates how one action’s visible motion gives way to another without falsely changing what the game permits or has completed. It is not a recommendation that every action be cancellable or that every transition be smooth. [C-01, C-02, C-08]

## Purpose

Make acceptance, interruption, commitment and recovery legible when animation changes. The intended benefit is fewer misleading state transitions while retaining the expressive motion the situation warrants. The owning [Animation and performance topic](../topics/animation-and-performance.md) provides alternatives and empirical limits. [C-01, C-04]

The pattern owns **motion-state handoff obligations**. P02 owns input mapping, retained intent and broader feedback semantics; its cue-alternative pattern remains responsible for fact-preserving modality choices. This is not a second remapping or redundant-cue recipe. [C-02, C-06]

## Context and prerequisites

Consider the pattern when an action can be interrupted, redirected, denied, superseded or visually blended while important state information must remain accurate. It may apply to a controlled character, an interactive object or an observed actor, but their promises differ. [C-01, C-02]

The future design needs an identifiable action/state owner, agreed cancellation and commitment policy, named important outcomes and a way to inspect transitions under actual input/view conditions. When networking matters, identify whose state is authoritative and whose presentation is being evaluated. These are prerequisites to a meaningful review, not a mandated runtime architecture. [C-02, C-03, C-05]

**Exit before authoring:** when gameplay permission or result ownership is unresolved, record the question and stop at design review. A blend graph cannot settle an undefined rule. Current F04/P03 dependencies are missing; this pattern supplies no substitute numerical settings or combat/traversal policy. [C-02, C-07, C-08]

## Mechanism and evidence

| Proposed link | Support and limit |
| --- | --- |
| Identify the actual permission/state change. | Reviewed P02 distinctions and source 007 motivate the decomposition; no single required state count. [C-02] |
| Carry forward or terminate each important promise explicitly. | Source 008 documents why source-clip continuation cannot simply be assumed. The ownership rule is an inference. [C-03] |
| Present the destination without implying false acceptance or completion. | Logical information-to-action bridge; end-to-end comprehension untested. [C-01] |
| Preserve useful expression and perceived control. | Source 005 motivates separate measures, not a guaranteed improvement from this recipe. [C-04] |
| Preserve required facts under settings and authority differences. | Guidance and component documentation identify constraints; usability and remote fairness remain untested. [C-05, C-06] |

A mechanically correct action can still look misleading, and a persuasive motion can describe a mechanically incorrect state. Neither smoothness nor an animation editor preview certifies the full chain. [C-01, C-04]

## Recipe

**Proposed for a later authorized design/prototype, not execution now.** [C-07, C-08]

### 1. State the current and requested actions

Record the current action, destination request, target/context and whether the request is merely received, permitted now, retained for later or denied. Include what the player should know, not only the internal label.

**Branch:** a denied request must not receive the destination’s accepted-action presentation. A retained request must not be treated as a completed action. Intentional ambiguity about a character’s motive may remain; required action permission cannot silently become ambiguous. [C-01, C-02]

### 2. Mark the permitted handoff conditions

Specify what allows replacement: a state condition, a commitment boundary, an external event or a valid target. Record whether new intent replaces old intent and what invalidates a retained request. Do not derive permissions from a clip’s convenient blend point alone.

**Exit:** when the task deliberately prohibits cancellation, keep the committed state and provide an appropriate denied/pending presentation. Changing the policy is a separate mechanics decision, not a visual polish fix. [C-02]

### 3. Inventory the promises that cross the boundary

For this action, identify relevant movement/contact, held object, target, completion result, active-effect indication and next-action readiness. Not every action needs every field. Mark each obligation as retained, terminated, replaced or still pending.

**Stop:** if an important result depends on a source presentation event that may disappear under the selected handoff, do not assume it will occur. Assign its intended ownership for later implementation review, including prevention of duplicate completion. [C-03]

### 4. Choose the visible destination and transition

Compare an explicit pose change, short authored transition, conventional blend, adaptive handoff or continuing partial-body settling. Choose based on what must remain readable and what motion continuity is worth in this task, not a blanket preference for the smoothest result.

**Adjustable variables:** source/destination pose coverage; transition duration and its declared units; ordering/priority of interruptions; retained body regions; contact or tool-release presentation; extent of optional follow-through; readiness cue; and allowed target changes. All values are local design/test variables, not sourced universal settings. [C-02–C-04]

### 5. Inspect the semantic transition, not just the visual seam

Ask whether the destination implies an accepted action, a valid contact or a completed outcome that the rules do not support. Examine interruption while a transition is already occurring, not only transitions from a settled idle. Include target loss, pause/resume, denied replacement and repeated input.

**Branch:** if a smooth handoff obscures release, denial or readiness, compare a simpler explicit change. Do not hide disagreement with extra effects. [C-01, C-03, C-04]

### 6. Check authority and access variants where relevant

For a networked case, distinguish local pending/predicted presentation, accepted outcome and observer presentation; record what corrections are allowed to communicate. For preferred motion/access settings, preserve a usable route to each required state fact without promising identical feeling.

**Exit:** do not approve a variant whose authority or required fact route cannot be evaluated. Restrict the claim to the actual tested context; offline inspection does not validate remote behavior. [C-05, C-06]

### 7. Evaluate with contrasting decisions and retain only supported handoffs

Include cases in which replacement should succeed, should be denied and should become invalid before consumption. Obtain state/permission predictions before feedback. Separate comprehension and control outcomes from expression and comfort.

**Reject or revise:** lost/duplicated essential outcome, false acceptance, unavailable critical fact or recurring misinterpretation of readiness. If extra continuity adds no credible local value and increases maintenance, use the simpler alternative. Preserve intentional commitment; do not “repair” every refusal into a cancel. [C-01–C-07]

### Proposed handoff record

| Field | Required question |
| --- | --- |
| Source and destination | What is ending and what has actually been requested? |
| Permission | Allowed now, denied, pending or invalidated — under which condition? |
| Preserved / terminated obligations | Which result, contact, target or held object survives? |
| Visible account | What should owner/observer believe at each meaningful change? |
| Readiness | What makes another action valid, and how is that available to the player? |
| Failure and exit | What would require a simpler handoff, policy clarification or stopping this variant? |

This is a proposed review record, not a schema installed in a harness. [C-07, C-08]

## Worked examples

### Illustrative — changing intent during inspection

**Synthetic; no game build, animation or test.** A controlled actor begins inspecting a panel. Turning away is allowed before commitment; after commitment it is denied until the result or a defined cancellation outcome. [C-07]

| Situation | Actual policy in this illustration | Required presentation question |
| --- | --- | --- |
| Turn request before commitment | Replace inspection with turning. | Does inspection visibly end without implying a result? |
| Turn request after commitment | Deny replacement. | Can the player tell inspection remains active rather than thinking the turn was accepted? |
| Retained next action loses its target | Invalidate the retained request. | Is a stale action prevented from appearing to succeed after recovery? |
| Inspection result becomes available during settling | Result exists; settling is optional. | Does the remaining motion falsely imply that control is still unavailable? |

The exact policies are illustrative choices, not library recommendations. The recipe’s value is that each outcome has a clear question and can be contradicted by a later test. If a source animation stops being evaluated, the future implementation must still honor the action’s specified outcome ownership; no engine code is supplied here. [C-02, C-03, C-07]

Compare the candidate with a neutral explicit handoff and with the original committed presentation under the same policies. Aesthetic continuity may be valuable, but it does not compensate for showing a cancelled inspection as complete. [C-01, C-04, C-07]

### Illustrative — remote movement correction

An observing player sees another actor start a movement whose acceptance is not yet settled locally. The design must decide whether that view communicates preparation, prediction or confirmed motion and what a correction means. This pattern asks for those distinctions; it does not choose a netcode solution, permitted correction distance or fairness rule. A local-only test cannot answer this case. [C-05, C-07]

## Tradeoffs and alternatives

Explicit handoff ownership adds design and verification work, particularly when outfits, tools, target changes and access variants multiply combinations. A fully committed clip can be simpler and more expressive when its rule is appropriate. A minimal explicit transition can communicate state better than preserving continuous motion. Hybrid or partial-body movement can retain expression but create inconsistent implications between body regions. These are tradeoffs to test, not established rankings. [C-02–C-04, C-07]

The alternative of changing the mechanic itself may be valid but must be recognized as such. Allowing earlier cancellation, longer retained intent or a different recovery condition changes the task and may change fairness or difficulty. Those are not incidental consequences to smuggle in under an animation refinement. [C-02, C-05]

## Failure cases

| Warning sign | Likely question to investigate | Stop or repair proposal |
| --- | --- | --- |
| The old success effect appears after cancellation. | Was a terminated promise retained? | Correct ownership and test cancellation cases. |
| A necessary result never appears after blending. | Was completion tied to a discarded source event? | Block advancement until its disposition is defined. |
| A new action animates but rules reject it. | Did visible transfer occur before permission? | Show receipt/denial rather than acceptance. |
| A ready actor still looks locked to the old target. | Does follow-through imply mechanical commitment? | Separate readiness or choose a clearer exit pose. |
| Repeated interruptions produce unreadable motion. | Is continuity hiding state or exceeding pose coverage? | Restrict or simplify the visual handoff; do not silently change mechanics. |
| Observer and owner infer contradictory outcomes. | Are prediction and authority distinctions missing? | Restrict the claim and investigate the actual network policy. |
| Reduced motion loses the only critical cue. | Was required information treated as ornament? | Restore a usable fact route and test its interpretation. |

These warning signs and remedies are hypotheses for future evaluation, not observed P04 results. [C-01–C-07]

## Counterexamples and do not use conditions

Do not use this as a mandate for cancellation during deliberate commitment, as a demand for input acknowledgement in a wholly noninteractive performance, or as permission to rewrite network authority. Do not add a complex handoff matrix when an existing simple state change already satisfies the task. Do not preserve continuity at the expense of an honest action result. [C-02–C-05]

The strongest opposing case is that the action’s intention is best served by a clear committed sequence and a straightforward recovery. An intricate handoff could increase errors and costs while weakening expression. The inspected study and documentation do not prove this recipe wins that comparison. [C-01, C-04]

## Playtest

**PROPOSED — NOT RUN.** Compare existing, proposed and minimal handoff presentations under identical cancellation/commitment rules. A separate mechanics factor is necessary when permissions themselves change. Include valid, denied, pending, invalidated and repeated-interruption cases. Counterbalance exposure, use matched tasks and collect permission predictions before feedback. [C-07]

Participants should include relevant familiarity and actual access/input users; identify owner/observer roles where networking is part of the question. Measure false acceptance/cancellation beliefs, lost/duplicated outcomes, readiness errors, recovery behavior and separate control/expression/comfort reports. View, device, prior learning, mechanical differences and display/network conditions are confounds; record rather than conceal them.

Reject a version with an essential unavailable fact, lost/duplicated result or misleading acceptance. Reject the proposed mechanism when benefits depend on changed permissions rather than motion communication. Retain an expressive handoff only when its local value and cost are supported under predeclared criteria; inconclusive findings do not establish equivalence. No universal duration, sample size or power guarantee is supplied. No test, participant recruitment, network measurement or implementation is authorized by this draft. [C-01, C-04–C-08]

## Claim ledger

Claim IDs are local to this entry. Confidence describes the exact scoped wording, not a source’s prestige or the recipe’s overall efficacy. Proposed procedures and examples are not approved studio decisions.

### C-01

**Claim:** Explicitly separating permission, motion transfer and result ownership may reduce misleading action-state presentation. **Class:** `hypothesis`. **Confidence:** low for the complete recipe; no direct validation.

**Support / precise locator:** GDR-SRC-20261010-P04-007–009, transition/inertialization/network-root-motion locators; animation-and-performance C-07–C-11.

**Applicability, contrary evidence and unresolved question:** Documentation supports possible failure mechanisms, not a measured reduction in errors from this workflow.

### C-02

**Claim:** Gameplay cancellation, queued intent and animation interruption are distinct operations and should not silently stand in for one another. **Class:** `inference`. **Confidence:** moderate for the semantic distinction.

**Support / precise locator:** GDR-SRC-20261010-P04-007, transition interruption; reviewed P02 controls-and-input, Timing path; feedback-and-game-feel, Action receipt versus outcome.

**Applicability, contrary evidence and unresolved question:** Intentional commitment remains valid. No universal cancellation permission or buffer duration is implied.

### C-03

**Claim:** A handoff needs an explicit disposition for important action outcomes when source motion may no longer be evaluated. **Class:** `inference`. **Confidence:** moderate for the reasoning; implementation not verified.

**Support / precise locator:** GDR-SRC-20261010-P04-008, Inertialization, source evaluation and Animation Notifies paragraphs; animation-and-performance C-08.

**Applicability, contrary evidence and unresolved question:** This is an event-ownership question, not an instruction to install an engine, use one notify system or implement code.

### C-04

**Claim:** Smoothness, apparent naturalness and control outcomes should be evaluated separately. **Class:** `inference`. **Confidence:** moderate from a narrow experiment and distinct constructs.

**Support / precise locator:** GDR-SRC-20261010-P04-005, §5.1–5.3 and §6; owning animation-and-performance C-04/C-05.

**Applicability, contrary evidence and unresolved question:** No universal ordering of expressivity and control. Internal performance-direction inconsistency prevents transferring that result. No comparison here establishes equal quality.

### C-05

**Claim:** Compare the owner’s and observer’s presented states when networked movement or predicted action is relevant. **Class:** `inference`. **Confidence:** moderate for the need to check the specific system.

**Support / precise locator:** GDR-SRC-20261010-P04-009, Network Smoothing and root-motion From AnimMontages paragraphs.

**Applicability, contrary evidence and unresolved question:** Not every game uses these components; no latency/fairness threshold, prediction architecture or network test is supplied.

### C-06

**Claim:** A reduced-motion or alternative presentation must be checked for required state facts independently of expressive equivalence. **Class:** `inference`. **Confidence:** moderate from scoped vendor guidance.

**Support / precise locator:** GDR-SRC-20261010-P04-010, critical visual information alternatives; GDR-SRC-20261010-P04-011, non-core motion and background exception; reviewed P02 information contract.

**Applicability, contrary evidence and unresolved question:** No medical safety claim, blanket animation freeze or guarantee that another modality conveys the same emotion.

### C-07

**Claim:** The interruption matrix, examples and falsifying comparisons are proposed local methods, not performed tests or authorized implementation. **Class:** `hypothesis`. **Confidence:** low for untested effect and feasibility.

**Support / precise locator:** Original P04 synthesis under the dispatch; reviewed F01 corrected contrasting-response test structure.

**Applicability, contrary evidence and unresolved question:** No engine, network, input instrumentation, assets or participants. Sampling and practical decision tolerances need a later study owner.

### C-08

**Claim:** This pattern remains a provisional P04 draft, not an accepted controller or animation architecture. **Class:** `studio-decision`. **Confidence:** high from the current user authorization.

**Support / precise locator:** Doug’s P04 message and attached brief, Authorization update, Assigned outputs and Current jobs and boundaries.

**Applicability, contrary evidence and unresolved question:** No permanent IDs, release, implementation, repository/Project changes or participant work are approved.

## References

All public records below were inspected in the stated passages on **2026-10-11 UTC**. IDs are P04-scoped source records, not permanent SRC allocations. Dates of older works are publication dates, not claims of current game behavior. Repeated reference records support standalone reading; they are not extra evidence.

### GDR-SRC-20261010-P04-005

**Aline Normoyle and Sophie Jörg.** [The effect of animation controller and avatar on player perceptions](https://www.researchgate.net/publication/310603130_The_effect_of_animation_controller_and_avatar_on_player_perceptions). **Publisher:** Computer Animation and Virtual Worlds / Wiley; author manuscript via ResearchGate. **Publication/update:** First online 2016-11-20; journal issue 2018. **Edition/build:** 29(6), e1731; DOI 10.1002/cav.1731. Inspected author manuscript uploaded 2021-01-26; manuscript pagination, not journal pagination.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Original controlled game experiment and separate observer study; primary author manuscript. **Exact locators:** §3.2–3.4, manuscript pp.12–17; §4.9, pp.23–24; §5.1 Control and §5.2 Enjoyment, pp.25–26; §5.3 Satisfaction, pp.26–27; §5.4 Performance, pp.27–28; §6 Conclusion and Future Work, pp.31–33. **Claims supported in this entry:** C-04.

**Limits:** Publisher full-text request redirected to abstract; full manuscript text was read on the author-upload route. Exact equivalence to the version of record not verified. Restricted controller/task designs, mainly student sample and differing observer/player questions limit generalization. Internal performance-direction inconsistency retained as P04-CON-04. No footage, raw data or graph digitization used. **Independence/deduplication:** Cites source 004 and earlier work by these authors. Manuscript, abstract and DOI are one work, not multiple confirmations. Cross-batch deduplication pending. **Rights:** Author manuscript copyright; redistribution license not established. Attributed paraphrase only; no participant data copied.

### GDR-SRC-20261010-P04-007

**Unity Technologies.** [Animation transitions](https://docs.unity3d.com/6000.3/Documentation/Manual/class-Transition.html). **Publisher:** Unity Manual. **Publication/update:** Publication/update date unknown. **Edition/build:** Unity 6.3 / 6000.3 documentation, selected edition; no claim that it is the newest engine.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official engine technical documentation. **Exact locators:** Properties → Has Exit Time, Fixed Duration, Transition Duration and conditions; Transition interruption → Interruption Source and Ordered Interruption. **Claims supported in this entry:** C-01/C-02.

**Limits:** Documents facilities and units; does not measure this project’s latency, responsiveness or cancellation policy. No engine execution. Recheck exact dependency version before implementation. **Independence/deduplication:** One vendor mechanism reference, not efficacy evidence. Cross-batch URL/version deduplication pending. **Rights:** Vendor documentation; reuse license not examined. Paraphrase only, no code copied.

### GDR-SRC-20261010-P04-008

**Epic Games.** [Animation Blueprint Blend Nodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-blend-nodes-in-unreal-engine?application_version=5.6). **Publisher:** Epic Games Documentation. **Publication/update:** Publication/update date unknown. **Edition/build:** Unreal Engine 5.6 documentation selected explicitly.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official engine technical documentation. **Exact locators:** Inertialization: source evaluation, interruption, and Animation Notifies paragraphs; parsed text lines 121–150. **Claims supported in this entry:** C-01/C-03.

**Limits:** No benchmark or runtime test. Documented source-evaluation behavior does not by itself prescribe gameplay event ownership. Experimental facilities are not endorsed for shipping. **Independence/deduplication:** Same vendor as source 009, different page/mechanism. Version parameter is part of this source identity; central deduplication pending. **Rights:** Vendor documentation; reuse license not examined; paraphrase only.

### GDR-SRC-20261010-P04-009

**Epic Games.** [Understanding Networked Movement in the Character Movement Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-networked-movement-in-the-character-movement-component-for-unreal-engine?application_version=5.6). **Publisher:** Epic Games Documentation. **Publication/update:** Publication/update date unknown. **Edition/build:** Unreal Engine 5.6 documentation selected explicitly.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official engine technical documentation. **Exact locators:** Network Smoothing; Replicating Special Case Movement with Root Motion → From AnimMontages; parsed text lines 174–203. **Claims supported in this entry:** C-01/C-05.

**Limits:** Character Movement Component behavior, not a universal networking model or proof of fair combat. No server/client, network or frame-time tests performed. **Independence/deduplication:** Same vendor as source 008. Distinct mechanism, not independent user-outcome evidence. Cross-batch URL/version deduplication pending. **Rights:** Vendor documentation; reuse license not examined; paraphrase only.

### GDR-SRC-20261010-P04-010

**Microsoft.** [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103). **Publisher:** Microsoft Learn. **Publication/update:** Last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live page revision inspected on evidence-check date.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official vendor accessibility guidance. **Exact locators:** Goal and Overview; Implementation guidelines → alternatives to color and visual-only information; simulation-filter and actual-player evaluation paragraphs. **Claims supported in this entry:** C-06.

**Limits:** Practitioner guidance, not a formal standard, legal advice or certification. Availability of an alternative is not demonstrated usability or emotional equivalence. Public body inspected despite authorization boilerplate. **Independence/deduplication:** Same document as reviewed GDR-SRC-20261010-P01-05 and GDR-SRC-20261010-P02-005; central reconciliation pending. Same issuer as source 011. **Rights:** Vendor page; content reuse license not inspected; paraphrase only; no example media copied.

### GDR-SRC-20261010-P04-011

**Microsoft.** [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117). **Publisher:** Microsoft Learn. **Publication/update:** Last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live page revision inspected on evidence-check date.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official vendor accessibility guidance. **Exact locators:** Implementation guidelines → moving/blinking/scrolling UI and its background-motion exception; camera motion; repetitive non-core animation; parsed text lines 43–121. **Claims supported in this entry:** C-06.

**Limits:** Not a universal freeze-all-gameplay requirement, medical safety threshold or certification. No FOV, flashing or animation-duration limit is extracted. Camera-setting research remains P03 ownership. **Independence/deduplication:** Same document as reviewed GDR-SRC-20261010-P01-10 and GDR-SRC-20261010-P02-010; central reconciliation pending. Related vendor guidance is not independent efficacy evidence. **Rights:** Vendor page; content reuse license not inspected; paraphrase only.

## Related entries and history

Owning topic: [Animation and performance — GDR-CAND-20261010-P04-TOP-02](../topics/animation-and-performance.md). Complement: [Recognition-preserving style variation](recognition-preserving-style-variation.md), not a replacement for P02 controls/feedback or its fact-preserving cue recipe. Exact external candidate identities are in the [dependency record](../reviews/full-run-20261010-p04-review-packet.md#reviewed-dependency-transfer). No genre files are linked or created.

P04-CON-03 preserves deliberate commitment as a countercase; P04-CON-04 prevents upgrading the controller manuscript’s inconsistent or weaker results. Missing F04/P03 work blocks final action/platform-specific settings, not this bounded qualified draft.

**2026-10-11 UTC:** initial 0.1.0 / initial-draft-1, no predecessor/supersession. Author self-review only. Independent review, host validation, permanent identity allocation and release remain pending. A valid research recipe is not an approved controller architecture.

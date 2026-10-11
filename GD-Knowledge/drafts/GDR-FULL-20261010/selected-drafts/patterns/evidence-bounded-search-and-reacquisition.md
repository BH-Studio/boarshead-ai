---
id: GDR-CAND-20261010-G14-PAT-01
kind: pattern
title: Evidence-bounded search and reacquisition
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
run_id: GDR-FULL-20261010
batch_id: G14
attempt_id: G14-authoring-attempt-1
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
date_basis: America/Los_Angeles; source access also occurred on 2026-10-11 UTC
input_snapshot: Mounted starter v0.1.0 candidate + supplied G14 brief + selected waves-1–2
  reviewed-draft dependency bytes
aliases:
- last-known search contract
- bounded observer knowledge
tags:
- agent-knowledge
- search
- reacquisition
- information-contract
- recovery
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-P01-TOP-03
related_patterns:
- GDR-CAND-20261010-P02-PAT-02
- GDR-CAND-20261010-F01-PAT-01
related_genres:
- GDR-CAND-20261010-G14-GEN-01
- GDR-CAND-20261010-G14-GEN-02
source_ids:
- GDR-SRC-20261010-G14-002
- GDR-SRC-20261010-G14-009
- GDR-SRC-20261010-G14-012
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-G14
coverage_status: open
predecessor_hash: null
supersedes: null
change_summary: Initial bounded G14 research candidate; no previous G14 candidate
  replaced
proposed_domain_owner: BH-GDR-Foundations-and-Systems; not accepted or transferred
---

# Evidence-bounded search and reacquisition

**Candidate recipe; overall effectiveness is an unvalidated hypothesis.** The proposed domain owner is Foundations and Systems, with Presentation and Interaction owning cue alternatives and Worlds and Characters owning spatial/encounter composition. Ownership has not been accepted or transferred. This is one of two new G14 patterns, not a release or an engine design. [C-01, C-08]

## Purpose

Help a player reason about how an agent can find, lose and find them again without confusing actual observation, inference, transmitted information and designer-granted privilege. The intended outcome is a comprehensible contest of concealment and search that permits the declared recovery options. It is not a requirement that every agent be realistic, truthful, nonviolent or escapable. [C-01]

## Context and prerequisites

Use when **the agent’s knowledge matters to a player decision** and the activity permits a period of uncertainty or recovery after observation. The design needs to identify relevant observations, locations, identity certainty, reports and any exceptional information powers. Its selected feedback routes must communicate enough to support the intended decisions; they need not disclose all internal state. [C-01, C-03]

Prerequisites are explicit: the team can distinguish information acquisition from response posture; it can trace why an agent chose a search target; it can explain when a report becomes obsolete; and it can test at least one lost-contact/reacquisition sequence. If the central activity is an immediate-failure precision trial, a simple visible rule and restart may be more appropriate. If a threat is intentionally omniscient, disclose that premise and test the available counterplay rather than presenting this recipe as sensory realism. [C-02, C-07]

## Mechanism and evidence

| Proposed link | Actual support | Boundary |
|---|---|---|
| Describe what the agent may know and how it gets that information. | Sources 002/009 provide related practitioner rationale. | One Thief production lineage, not independent corroboration. |
| Keep observations, remembered evidence and operational response distinct. | Analysis motivated by those accounts. | The particular data model and state set below are G14 proposals. |
| Express the decision-relevant distinctions through usable signals. | Narrow transfer from reviewed DEP-CUES. | No guarantee of equal affect or exact performance. |
| Players correctly predict search and recovery opportunities. | **Hypothesis** for this complete recipe. | Needs changed-answer probes under supported access conditions. |
| The activity is more enjoyable or less arbitrary. | **Hypothesis**, not established by this packet. | Source 012 is not a direct test of this recipe; its limitations remain explicit in [stealth C-06/C-07](../genres/stealth.md#claim-ledger). |

**Contrary evidence retained:** the cited Thief account includes designer-provided information privileges. This recipe therefore does not claim that strict observation-only knowledge is necessary or historically universal. A privilege can be an intentional rule; the design question is whether it preserves the chosen intelligible activity. [C-02; GDR-SRC-20261010-G14-009]

## Recipe

### 1. Define the contract at the player decision

Write what the player is trying to infer: for example, whether an agent knows an identity, whether a place is still under search, or whether a report reached another observer. State the available responses and the mission constraints. Separate a no-detection requirement from a no-alarm or no-harm requirement. [C-03]

**Exit:** when the activity depends on a secret rule that the team cannot describe even for testing, resolve that design ambiguity before adding signals or states. An intentionally unexplained horror threat is a possible alternative, not evidence that this recipe works without a contract. [C-07]

### 2. List permitted information routes and exceptions

For each agent role, list direct observations, environmental traces, received reports, retained memory and explicit exceptional powers. Record the relevant certainty and expiry conditions in player-meaningful terms. An agent may know there was a sound without knowing who caused it. A report of past contact is not automatically exact current location. [C-03]

An exception register should state its purpose, phase, scope and what a player can discover about it. A disclosed scanner that locates moving targets is different from an undisclosed system that supplies live position while presenting the agent as blind. Do not infer from this distinction that all narrative deception is forbidden; character guesses and bluffs are different from trusted system-state information. [C-03, C-04]

### 3. Choose behavior transitions that use those distinctions

Create the smallest useful set of conditions. For this illustrative recipe they might be: no relevant evidence; a place warrants investigation; a target is confirmed; contact is lost but evidence remains; a new observation confirms contact again. These are not required state names, a fixed state count or a prescribed finite-state architecture. [C-03]

Decide which changes concern information and which concern posture. A guard can remain cautious after the latest location becomes uncertain. Breaking sight need not cancel a persistent alarm. Conversely, if a precision mode deliberately resets everything, label that separate rule rather than implying remembered evidence still matters. [C-03, C-07]

### 4. Connect behavior to the permitted information

For each search or pursuit choice, make an author-facing explanation possible: known place, received report, inferred route, fresh evidence or declared privilege. Test disconnected rooms, stale reports, conflicting witnesses and broken routes. The purpose is to locate information-policy errors; no runtime logging system or engine implementation is authorized here. [C-03, C-08]

**Exit:** when available topology leaves no meaningful recovery and the mode promises one, revise the encounter, the promise or the search pressure. Adding a “lost contact” label cannot create an actual escape opportunity. [C-05]

### 5. Author the smallest useful feedback and its alternatives

Decide which state facts the player should receive, which are inferred and which remain unknown. Reuse [Fact-preserving cue alternatives](../reviews/full-run-20261010-g14-review-packet.md#dep-cues) for accessible variants. Preserve identity certainty and reference frame; avoid turning an ambiguous noise into a caption asserting confirmed player detection. Preserve information the design genuinely intends to be known, including useful direction. [C-04]

Keep guesses distinguishable from confirmations through the selected communication scheme, not only a culturally assumed tone of voice. Check translated conditionals, overlapping speakers, sound-off play and obsolete messages. These are test targets; the existence of authored variants does not prove accessibility. [C-04]

### 6. Test recovery and reacquisition as different events

Stage matched cases where a search should remain uncertain and where fresh evidence should permit contact. Ask for predictions before feedback. Vary the correct response rather than repeating “the agent cannot see me” in several cosmetic scenes. Separate understanding the rule from preferring a risky action. Retain accommodations. [C-06]

**Adjustable variables:** evidence retention, report scope, search extent, communication delay, uncertainty disclosure, privilege scope, contact confirmation, available exits and post-contact mission consequences. Every numerical choice requires a local rationale; this packet supplies no universal field of view, timeout, search radius or reaction window. [C-03, C-08]

## Worked examples

### Illustrative: a courier crosses a guarded reading room

This invented example demonstrates the recipe; it is not a played game or a result. An attendant hears a latch in a side room. The information permits investigating that room, not knowing the courier’s identity. The courier is then seen crossing a doorway; the attendant now has confirmed identity and a last observed place. After a screen blocks sight, the attendant checks the nearby exit and remains alert. A second attendant receives a spoken report about the doorway, not continuous tracking. [C-03]

A player-facing cue reports an investigation before confirmation and a sighting after confirmation. An accessible representation preserves that difference; it does not add an unseen destination unless the mode intentionally reveals destinations. If the courier re-enters the visible doorway, reacquisition is legitimate. If the courier remains in an unobserved distant room, an immediate exact interception needs a disclosed additional information route or should fail the model’s contract check. [C-03, C-04]

The courier may wait, leave, abandon the objective or use a declared alternative. A no-harm commitment remains active after discovery; forced injury cannot be smuggled in as the sole “recovery” option. Another mode may explicitly use immediate failure and restart, in which case this richer recovery recipe is unnecessary. [C-05, C-07]

## Tradeoffs and alternatives

The proposed benefit is traceability: designers and players can investigate why an agent changed behavior. The costs include authoring state-appropriate responses, testing propagation and memory, preserving cue semantics, and preventing stale information from masquerading as fresh observation. Those costs may exceed the value of detailed search in a short encounter. They are model-based production inferences, not measured estimates. [C-08]

Alternatives include visible deterministic patrols; discrete planning with deliberately complete information; authored searches; a declared omniscient pursuer with different counterplay; or immediate reset after detection. A simpler system can support a valid stealth activity without pretending to simulate cognition. The proposed recipe is preferable only when its extra distinctions serve the selected experience. [C-07]

## Failure cases

| Failure | Observable warning sign to test | Candidate correction |
|---|---|---|
| Telepathic information propagation | Players correctly identify an isolated observer, yet every agent immediately targets exact live position. | Change propagation or disclose the actual tracking rule. |
| Cosmetic uncertainty | The cue says “searching,” but agent paths do not depend on evidence loss. | Align behavior and information or rename the state honestly. |
| Knowledge confusion | Players conflate suspicion, confirmed identity and persistent alarm. | Remove unnecessary distinctions or communicate the relevant difference accessibly. |
| Recovery without agency | Every lost-contact route leads into an unavoidable violation of the chosen commitment. | Revise topology/consequences or withdraw the promise of recovery. |
| Signal overload | Multiple stale cues obscure the currently relevant change. | Prioritize meaningful updates and test supported alternative routes. |

These are proposed diagnostics, not claims that such failures were observed in the cited games. [C-04, C-05, C-08]

## Counterexamples and do not use conditions

Do not apply this recipe merely because the game contains guards. It can harm a memorization-focused challenge by adding state that changes the practiced task. It can also weaken a deliberately omniscient-threat premise if it promises ordinary hiding will work. A game with no recovery opportunity may be better served by an honest failure rule. [C-07]

The strongest challenge is that **believable behavior need not expose or obey an evidence-pure model**. The historical implementation counterexample remains live, and the empirical study does not settle the appropriate amount of privilege. Compare the actual alternatives instead of turning a plausible engineering discipline into a universal fairness law. [C-02, C-07]

## Playtest

**Proposed; not performed.** Compare the candidate model with a simpler appropriate alternative in matched encounters. Keep movement, objective constraints, resource cost and available routes stable where practical. When an information privilege differs, declare it as a manipulated variable rather than hiding it inside “smarter AI.” [C-06, C-08]

Use sound-only where appropriate, sound-off alternatives and other supported configurations without depriving participants of required access. Recruit varied stealth familiarity and relevant access needs. Record pre-feedback predictions about knowledge, reports and reacquisition; completion of a recovery that respects the selected commitment; perceived arbitrariness; and preferred activity. Test repeated exposure. Map familiarity, changed difficulty, extra cue information and performance-related enjoyment are confounds. [C-06]

**Falsification/decision rule:** reject or simplify the recipe if it does not improve the target knowledge discrimination, if its recovery states have no usable decisions, or if the simpler alternative better fits the declared activity at an acceptable cost. Set practical margins and recruitment before data collection. A null difference is not equivalence, and a correct answer alone is not transfer learning. [C-06, C-08]

## Claim ledger and sources

| Claim | Class and scope | Support / locator | Confidence and limit |
|---|---|---|---|
| C-01 | Overall recipe may support intelligible searching and recovery. `hypothesis` | Sources 002/009 motivate the question; complete recipe not directly tested. | Low; no validated pattern efficacy. |
| C-02 | Strict evidence purity is not established as necessary. `inference` | Source 009, Viewcones/Awareness Pulses; counterexample, not universal endorsement. | Moderate for narrowing a necessity claim. |
| C-03 | Separating information routes, certainty, posture and exceptions makes a model auditable. `inference` | Own proposed decomposition informed by 009; no copied engine algorithm. | Moderate for analytical traceability, low for player outcomes. |
| C-04 | Feedback alternatives should preserve the intended information distinction. `inference` | DEP-CUES 52–99 and DEP-ACCESS 52–100. | Moderate scoped transfer; no emotional parity. |
| C-05 | A promised recovery needs feasible actions consistent with the chosen commitment. `inference` | DEP-CHALLENGE 53–77; DEP-OBJECTIVE 49–110; logical requirement. | Moderate; requires encounter-specific verification. |
| C-06 | Changed-answer, pre-feedback probes can challenge copied responses but do not guarantee learning. `inference` | DEP-TRANSFER 99–118; own proposed comparison. | Moderate methodology; no G14 results. |
| C-07 | Determinism, full information, privileged sensing or reset may be better alternatives for other goals. `hypothesis` | Source 009 and genre goal distinctions; not an audience prevalence claim. | Low; compare actual modes. |
| C-08 | Production cost and experience benefits require local validation and owner review. `hypothesis` | Own recipe; source 012 used only through the narrow boundary recorded in stealth C-06/C-07. | Low; independent review and all proposed playtests pending. |

## Related entries and history

Related genre applications: [Stealth](../genres/stealth.md), `GDR-CAND-20261010-G14-GEN-02`; [Immersive simulation](../genres/immersive-simulation.md), `GDR-CAND-20261010-G14-GEN-01`. Related reviewed-draft receipts: [Decision design](../reviews/full-run-20261010-g14-review-packet.md#dep-decision), [cue alternatives](../reviews/full-run-20261010-g14-review-packet.md#dep-cues), [transfer checks](../reviews/full-run-20261010-g14-review-packet.md#dep-transfer). No duplicate objective or accessibility pattern is created.

Initial draft `initial-draft-1`, predecessor null. Author self-review added the sensory-privilege counterexample and narrowed the recipe to an explicit activity. `G14-CON-02`, `G14-CON-03`, `G14-CON-04` and `G14-CON-07` remain unresolved. Independent review, ownership acceptance and release are pending.

## References

Access session for every source below: **2026-10-10, America/Los_Angeles / 2026-10-11 UTC**. This is the date of inspection, not proof of current build behavior. `observed-example` claims concern the identified documentation artifact unless expressly stated otherwise. No commercial game was played or recorded for G14.

### GDR-SRC-20261010-G14-002

**Tom Leonard, lead programmer.** *Postmortem: Thief: The Dark Project*. Game Developer. Publication/update: 1999-07-09. [Verified source](https://www.gamedeveloper.com/design/postmortem-i-thief-the-dark-project-i-).

**Edition/build:** Original Thief production retrospective; executable version unknown to this batch. **Access:** `relevant-excerpt`. **Type:** Firsthand practitioner retrospective.

**Inspected locator:** “What Went Right”: Sound as Game Design Focus, Focus, Objectives and Difficulty Levels; “What Went Wrong”: AI (HTML lines 76–89, 103–111).

**Claims supported:** C-01 motivation only, not efficacy. **Limits:** Failure explanations are the author’s retrospective interpretations; no controlled outcome comparison is supplied for the claims used.

**Independence:** Same author and production as source 009; count as one underlying production context, not two replications. **Rights:** Copyright retained by the author/publisher; paraphrase and bibliographic links only; no images, audio, source code or full text redistributed.

### GDR-SRC-20261010-G14-009

**Tom Leonard.** *Building an AI Sensory System: Examining The Design of Thief: The Dark Project*. Game Developer. Publication/update: 2003-03-07. [Verified source](https://www.gamedeveloper.com/programming/building-an-ai-sensory-system-examining-the-design-of-i-thief-the-dark-project-i-).

**Edition/build:** Retrospective Dark Engine/Thief design; not a current engine recommendation. **Access:** `relevant-excerpt`. **Type:** Firsthand technical/practitioner account.

**Inspected locator:** “Senses as Gameplay Focus: Thief”; “Expanding the Senses”; “Viewcones”; “Awareness Pulses”; “Conclusion” (HTML lines 82–129).

**Claims supported:** C-02 and background for C-03. **Limits:** Prose inspected; diagrams and code not used as implementation evidence. Includes deliberately privileged information, so it does not prove strict sensory realism.

**Independence:** Same author and production as source 002; one production context. **Rights:** Copyright retained by the author/publisher; paraphrase and bibliographic links only; no images, audio, source code or full text redistributed.

### GDR-SRC-20261010-G14-012

**Wael Al Enezi and Clark Verbrugge.** *Investigating the Influence of Behaviors and Dialogs on Player Enjoyment in Stealth Games*. Proceedings of AIIDE 19(1), 166–174; AAAI. Publication/update: 2023-10-06. [Verified source](https://doi.org/10.1609/aiide.v19i1.27512).

**Edition/build:** Published 2023 paper; research prototype, not a commercial build. **Access:** `full`. **Type:** Original empirical study.

**Inspected locator:** Methods pp.167–170; results pp.171–173; Figure 7 p.172; Tables 5–6 p.173. Entire PDF text read; screenshots checked for pp.170,172,173. Verified PDF: https://ojs.aaai.org/index.php/AIIDE/article/download/27512/27285/31563.

**Claims supported:** Evidence boundary for C-08; details and cautions in stealth C-06/C-07, not a test of this recipe. **Limits:** Raw data/code not obtained; reporting discrepancy and limited generalization are recorded in stealth C-07 and G14-CON-04. No equivalence or causal mechanism claim imported.

**Independence:** Independent academic research context; source 013 is by the same authors in the same proceedings, with sample overlap unestablished. **Rights:** PDF states copyright ©2023 AAAI, all rights reserved. No paper text, tables, figures or prototype assets redistributed.


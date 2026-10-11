---
id: GDR-CAND-20261010-G18-PAT-01
kind: pattern
title: Versioned Performance Comparison
version: 0.1.0
status: draft
owner_project: BH-GDR-Genres
run_id: GDR-FULL-20261010
batch_id: G18
candidate_revision: initial-author-draft-1
attempt_identity: G18-current-dispatch-1
updated: '2026-10-11'
evidence_checked: '2026-10-11'
date_basis: UTC; run identifier retains dispatch date 2026-10-10
coverage_status: open
independent_review: not-performed
aliases:
- contextual result comparison
- comparable attempts
- versioned competition profile
tags:
- measurement
- rules-version
- assistance
- comparison-validity
- accessibility
related_topics:
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-03
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-F02-PAT-02
related_genres:
- GDR-CAND-20261010-G18-GEN-01
- GDR-CAND-20261010-G18-GEN-02
source_ids:
- GDR-SRC-20261010-G18-004
- GDR-SRC-20261010-G18-007
- GDR-SRC-20261010-G18-009
- GDR-SRC-20261010-G18-010
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial G18 draft; no earlier G18 candidate bytes identified in this
  execution.
byte_identity: Exact SHA-256 is recorded in the accompanying integrity receipt; no
  self-hash is embedded.
---

# Versioned Performance Comparison

**Conditional pattern hypothesis; draft, not a competition standard or released reference.** The proposed benefit is more accurate interpretation of results. That benefit has not been measured. This recipe does not require identical settings for every player, removal of accommodations, universal leaderboard separation, or exhaustive telemetry.

Genre adaptations are in [Racing](../genres/racing.md) and [Sports](../genres/sports.md). The [review packet](../reviews/full-run-20261010-g18-review-packet.md) records dependencies, source gaps, ownership questions and unallocated child proposals. Exact bytes are in the [integrity receipt](../reviews/full-run-20261010-g18-integrity-receipt.md).

## Purpose

Use this pattern when a result is being interpreted as **improvement, comparative performance or evidence about a particular skill**, and changes to the task could support a different explanation. Its intended player-facing result is a history or comparison that says what the result can establish without shaming legitimate ways of playing. Its research-facing result is a test whose comparison matches the question. [P-C02; P-C03]

The essential operation is simple: **state the claim, retain the context relevant to it, and mark comparability honestly**. A personal best under a chosen configuration can be meaningful even when it is not an equal-condition ranking. A season victory can be meaningful without proving that an operator’s timing improved. Neither requires converting all play into a standardized examination. [P-C02]

## Context and prerequisites

A suitable context has an identifiable result, an intended interpretation and some inspectable task state. The relevant state may include a rules edition, model/build version, opponent context, vehicle/team capability, assistance behavior, reset policy or measurement definition. These are candidate fields, not a mandatory universal schema. The design team must establish which ones can change the claim under consideration. [P-C02]

There must also be a usable way to explain a consequential difference. The person comparing results should not need to disclose why they use an input or access option. A configuration can describe gameplay behavior without recording a medical condition. Unknown metadata is permitted; inventing or silently inferring it is not. [P-C04]

This is an **advisory design recipe**, not code, a storage schema, an anti-cheat system or a claim that replay/network state is trustworthy. Where authoritative configuration cannot be determined, the exit is to narrow the result’s interpretation, retain an “unknown” state or stop making the comparison. Do not fabricate an exact profile to keep a leaderboard operational. [P-C02; P-C03]

## Mechanism and evidence

Official sources show why assumptions can become stale: the GT7 1.68 notice changes a comparison-related mode option; FC 26 documents mode-specific control restrictions; IFAB publishes edition-specific changes and a later effective date. These establish **specific differences or transitions**, not a universal ranking policy. [P-C01; GDR-SRC-20261010-G18-004, -007, -009, -010; precise locators in ledger]

The proposed causal chain has unequal support:

| Link | Support and limit |
|---|---|
| A relevant task or measurement change creates an alternative explanation for a changed result. | **Inference**, strong as comparison logic, with narrow documentary examples. It does not prove which variable caused any individual outcome. [P-C02] |
| Recording the relevant context makes that alternative explanation available. | **Inference**, conditional on accurate, sufficiently complete records. A label does not repair unobserved changes or invalid measurement. [P-C02] |
| A concise explanation helps people interpret the comparison correctly. | **Hypothesis**, not validated here. It can instead confuse, overload or falsely reassure. [P-C03] |
| Honest routing preserves meaningful participation better than indiscriminate segregation. | **Hypothesis**, with no comparative participant evidence in this batch. It can fail through under-protection of a competition or through unnecessary exclusion. [P-C04] |
| Better interpretation improves trust, enjoyment or long-term engagement. | **Unestablished hypothesis**. Do not advertise these downstream benefits from this research or infer them from label comprehension alone. [P-C03] |

The shared [Evaluation and balancing dependency D06](../reviews/full-run-20261010-g18-review-packet.md#d06) supplies a reviewed-but-unreleased measurement contract, not empirical validation of this new pattern. The new recipe’s owner and overlap with Foundations must be resolved before canonical allocation.

## Recipe

1. **Write the interpretation before choosing fields.** Specify the outcome, unit and purpose. “My lowest valid time with this car” is different from “my general driving skill increased.” “The team won this season fixture” is different from “this player makes better pass predictions.” Do not collect a field unless it can affect the intended interpretation or its uncertainty. [P-C02]

2. **Identify plausible alternative explanations.** Examine changes to the task, available information, delegated actions, capabilities, opponents, reset state and measurement. Ask whether each difference could alter the result or the meaning of the skill claim. Include missing information as a known limitation. Do not start from “every assist is an unfair advantage.” [P-C02; P-C04]

3. **Choose a minimal context record.** Capture authoritative state when feasible and identify its provenance. Distinguish the actual rules/build used from the current installed version. Retain meaningful mid-attempt changes, or mark an attempt heterogeneous rather than pretending it had one stable profile. Do not infer a previous configuration from present preferences. [P-C02]

4. **Define comparison states and policy.** Useful proposed states are “comparable for this stated claim,” “different in these relevant ways,” and “unknown.” Equal file labels do not prove equal gameplay or access. Exact matches may suit a tightly defined record attempt; different settings may still be sufficiently equivalent for another goal if evidence supports that equivalence. If equivalence is untested, say so. [P-C03; P-C04]

5. **Present consequences, not a wall of settings.** Show the result and the one or few differences important to the interpretation, with an accessible route to details. Wording might say “different vehicle capability; not evidence of driving improvement alone,” rather than “invalid player.” Treat a changed narration language or subtitle size as irrelevant unless the specific task provides a reason otherwise. The wording here is illustrative, not tested UI copy. [P-C03; P-C04]

6. **Offer a non-punitive next action.** Depending on the purpose, retain a contextual personal history, repeat under a chosen compatible configuration, enter a disclosed competition format, or simply view both results without a skill inference. Do not automatically disable support or require personal health information. Some strictly specified events may have legitimate entry conditions, but the event must state the reason and alternatives rather than borrow an unsupported universal rule. [P-C04]

7. **Check changed-rule and recovery cases.** Verify that an update, restore, retry or mode switch does not silently relabel historical results. Distinguish a different problem under the same rule from a newly changed rule. Use the corrected [Supported Attempt and Transfer Check D07](../reviews/full-run-20261010-g18-review-packet.md#d07) only when the rule being learned is actually preserved. [P-C02; P-C05]

8. **Evaluate, simplify or exit.** Test whether the explanation reduces the targeted inference error without making valid participation harder. If metadata is unreliable, narrow the claim. If comparisons are not part of the desired experience, omit the profile. If a small event description or personal note serves the purpose, prefer that simpler alternative over a universal profile system. [P-C03; P-C04; P-C05]

### Adjustable variables

| Variable | What to decide | Guardrail |
|---|---|---|
| Claim scope | Personal history, specific technique, team outcome, fixed event or exploratory play | Do not present a narrow metric as general ability. |
| Relevant context | Only fields with a plausible connection to the stated outcome/interpretation | No sensitive personal diagnosis; no arbitrary “assisted/unassisted” moral scale. |
| Version granularity | Edition, patch, authored rule revision or measurement definition | More version detail is not useful if its behavioral relevance is unknown. |
| Comparability rule | Exact context, evidence-supported equivalence or openly contextual comparison | Unknown is a valid result; do not imply proof of fairness from matching labels. |
| Display depth | Summary with accessible details, event-level description or a local study record | Test comprehension and burden, not just field completeness. |
| Update/reset treatment | Preserve history, create a new relevant context, or mark a heterogeneous attempt | Do not silently migrate old results into newly defined conditions. |
| Participation route | Personal attempts, declared formats, practice or another meaningful option | Do not require removal of accommodations to restore a misleading claim. |

No numerical thresholds for acceptable performance difference, ranking separation, sample size, reaction speed or skill equivalence are supplied. Those are local decision variables requiring evidence and explicit ownership.

## Worked examples

### A racing history — illustrative, not performed

A prototype records two route times. Between them, the vehicle’s capability and the movement model changed. The player still deserves a record of both accomplishments, but a “driving improved” message would overstate what the comparison establishes. The proposed minimal record keeps the model revision, chosen vehicle configuration and the assistance behavior relevant to the stated event. It does not record why the player uses that support. [P-C02; P-C04]

The history presents the later time with a short explanation of the relevant differences. A repeat option can restore a **chosen, accessible** comparable setup if the player wishes to investigate execution improvement. It must not automatically remove the player’s information or control route. If restoring the old model is impossible, the history can simply state that the times are contextual records rather than a controlled comparison. The GT7 source is a narrow reason to take versioned mode assumptions seriously, not evidence that this hypothetical UI works. [P-C01; P-C03]

Counterexample: changing subtitle size alone need not split this route-time history. Another counterexample is an openly chaotic social race whose promise is a shared event rather than equal-condition ranking. Its event description may be enough. The pattern should not turn either case into unnecessary profiles and queues. [P-C04]

### A sport practice result — illustrative, not performed

A team practices a receiving decision. In one configuration, the operator chooses a receiver while the game supplies pass force. In another, the game also selects the receiver. More completed passes in the second task do not by themselves demonstrate improved receiver selection by the operator. The comparison record must describe the **delegated decision**, not just call both configurations “assisted.” [P-C02]

An appropriate interface could retain completion results in a personal history while preventing an unsupported claim about that particular skill. A researcher evaluating target choice would use a task in which target choice remains the operator’s responsibility, with an accessible execution route. A player seeking social participation may legitimately prefer the more automated arrangement. Neither interpretation requires diagnosing the player or declaring one configuration inferior in general. [P-C03; P-C04]

Counterexample: two different inputs may preserve the same target-selection decision. Splitting them solely by device label would not follow from this recipe. Their practical equivalence still needs examination in the relevant task; equal visible options also do not establish equal access. [P-C04]

### A rule-edition transition — illustrative, not performed

A sport adaptation changes a restart sanction in a new authored rules revision. Historical match results retain the prior revision. Training explains the new consequence before asking players to predict it. A result under the new rule is not silently treated as a repeated measurement of the old task. The IFAB edition example supplies provenance for why rule versions matter; it does not require this fictional game to adopt every official rule. [P-C01; P-C02]

## Tradeoffs and alternatives

A detailed profile can impose configuration, localization, support and verification costs disproportionate to the decision. More metadata also creates more opportunities for a misleading sense of precision. Start with the smallest explanation that can falsify the intended interpretation. A static event description, an explicitly fixed practice setup, a player-authored note or separate “personal history” and “event record” views can be simpler alternatives. [P-C03]

Strict equality of visible settings can be both overinclusive and underinclusive: it may combine attempts with unknown contextual differences while separating players whose different interfaces preserve the relevant decision. Conversely, declaring all settings equivalent can undermine a genuinely specified operational-skill contest. The recipe asks for a defensible **claim-specific** policy, not either blanket extreme. [P-C04]

Coordination with competition, accessibility, evaluation and progression owners is necessary before a reusable profile becomes a canonical library concept. This candidate does not duplicate implementation guidance, assign global IDs or decide the studio’s event policies. [P-C05]

## Failure cases and warning signs

| Failure | Observable warning sign in a proposed evaluation | Possible correction or exit |
|---|---|---|
| Labels imply more than the metric measures | Users interpret a faster contextual result as proof of general skill despite the explanation. | Narrow wording and metric; remove the skill claim. |
| Wrong or missing version state | Replayed or restored attempts show a current profile that was not active when recorded. | Preserve known provenance, mark uncertainty, or stop comparison. |
| False segregation | A harmless presentation preference sends players into different competitive categories. | Remove the field from that policy unless a relevant mechanism and evidence justify it. |
| Access stigma | Participants feel required to disclose a diagnosis or hide approved support. | Describe gameplay behavior, remove personal labels, reassess the participation policy. |
| Irrelevant complexity | Users cannot find the result because profile details dominate it. | Move details behind an accessible explanation or replace the system with an event-level statement. |
| Comparison masks coupled play | A team outcome is attributed to one individual without accounting for teammate or opponent context. | Change the unit and narrow the inference; do not repair it with a single generic rating. |
| Hidden adaptation contradicts the event | A stated fixed benchmark changes relevant opposition or assistance during the attempt. | Disclose the actual format or make it genuinely fixed; use D10 only within its declared scope. |

These are anticipated failure modes, not outcomes observed in a deployed G18 implementation. [P-C03; P-C04; P-C05]

## Counterexamples and do-not-use conditions

Do not use this pattern to certify fairness from settings alone, prove anti-cheat integrity, diagnose player ability or disability, or claim transfer to a real-world sport or vehicle. No such validation was conducted. [P-C02; P-C04]

Omit or sharply simplify it when players are not making consequential performance comparisons, when an informal event description expresses the promise adequately, or when obtaining context would require unjustified surveillance. Unknown conditions are a reason to stop a strong inference, not to collect sensitive data. [P-C04]

Do not require assisted and unassisted leaderboards merely because the examples include assists. A particular event may test a specific operational task; another may test decisions preserved across different interfaces. Their policies can differ without one being a universal rule. Do not apply the pattern so rigidly that it prevents the deliberately asymmetric or handicapped play the event explicitly promises. [P-C04]

## Proposed falsifying playtest

**Not performed.** The question is whether minimal context improves interpretation of a stated result **without producing material false exclusion or burden**. Select an intended participant population that includes people using the actual supported input and information routes; avoid diagnosing participants from their settings. Determine sample size and meaningful error differences from the local question and uncertainty, not a default number. [P-C05]

Compare the existing result presentation, a minimal claim-specific explanation, and a simpler event-description alternative. Counterbalance example order. Present pairs that are genuinely comparable for the question; pairs with a relevant rule, capability or delegated-decision change; pairs with irrelevant presentation changes; and pairs with unknown context. Ask what each comparison supports and what action the person would take next. Do not teach the exact correct response before measuring interpretation.

Record supported and unsupported inferences, uncertainty recognition, false separation, successful access to the next action, comprehension burden, perceived legitimacy and preference. Measure enjoyment separately rather than assuming comprehension improves it. Confounds include explanation length, vocabulary, prior knowledge of the sport, answer cues, task familiarity and the validity of the supposed equivalence policy. Repeated examples from one person are not independent participants.

Reject the proposed UI mechanism if the added profile does not clarify the intended inference relative to the simpler alternative, or if it encourages unwarranted confidence. Reject or revise the policy if it blocks otherwise relevant participation for irrelevant settings or exposes personal information. Stop the experiment’s performance interpretation if the team cannot establish the actual context used. Do not claim success merely because a static validator finds every field present. [P-C03; P-C04; P-C05]

## Claim ledger

| Claim | Class and exact scope | Sources / locators | Confidence and limitation |
|---|---|---|---|
| P-C01 | Specific official artifacts document version or mode differences relevant to a comparison. **observed-example**; the cited IFAB 2025/26 clauses are **formal-standard** only in that sport/edition. | GDR-SRC-20261010-G18-004, Other Improvements §§2,4; -007, Controller Customization; -009, Laws 12.3/11.2; -010, effective-date paragraph. | High, narrow documentary scope. No general equivalence, current full-law audit or beneficial player effect follows. |
| P-C02 | A changed relevant task variable supplies an alternative explanation; the comparison must be limited to what its conditions and metric establish. **inference** | P-C01; D06 measurement contract; D07 same-rule discrimination. | High logical limitation, not proof of the cause of a particular result. Relevant variables can be unknown. |
| P-C03 | Minimal context and honest uncertainty may improve interpretation. **hypothesis** | Reasoned chain from P-C02; proposed recipe and test. | Low; no participant comparison, deployment or causal benefit evidence. Extra detail may worsen understanding. |
| P-C04 | Claim-specific policies may avoid unsupported blanket segregation while preserving declared event goals. **hypothesis** | P-C02; D02 access scope; D04 control distinctions; FC 26 as a restricted product example, not a normative template. | Low for social/competitive benefit. Over-segregation, hidden inequivalence and privacy are explicit falsifiers. |
| P-C05 | The recipe can be tested and coordinated without treating a field-complete record as evidence of efficacy. **hypothesis** | D06 evaluation; D10 bounded adaptation; G18 proposed checks. | No tests performed; ownership, duplication, sample design and acceptance criteria remain pending. |

## Related entries, ownership and history

Authored in `BH-GDR-Genres`; proposed reusable-pattern ownership requires Library Coordination with `BH-GDR-Foundations-and-Systems` and the Presentation/Interaction accessibility and controls owners. This is an ownership proposal, not an approved transfer. D06 owns general evaluation principles; D07 owns learning-transfer discrimination; D10 owns disclosed adaptation. This candidate concerns their narrower intersection at result comparison and must be checked for duplication against the latest pending library.

Related contradictions: **G18-CON-03** (comparison consistency versus inclusive participation) and **G18-CON-04** (same-rule transfer versus changed-rule adaptation). The pattern is the **one** new pattern in this packet; the unused second slot is not a finding that no other useful technique exists.

Version `0.1.0`, `initial-author-draft-1`; predecessor/supersession null. No permanent ID is assigned. Author self-review only; independent review, host retrieval and release remain unperformed/unapproved. Exact SHA-256 is in the integrity receipt. The next decision is whether this conditional recipe merits independent review as a distinct reusable concept or should be merged into an existing evaluation pattern before further work.

## References

All access dates are **2026-10-11 UTC**. Source IDs are temporary run-scoped identities. Cross-batch canonical URL/DOI/edition deduplication is pending. Public material is paraphrased; no source article, image or screenshot is redistributed. Unless an explicit license is established, rights are treated as reserved; public access is not a redistribution license. “Documentary observed example” means the named official artifact was inspected by the G18 author, not that a game was played.

### GDR-SRC-20261010-G18-004

Polyphony Digital / Sony Interactive Entertainment. *Update Notice (1.68)*. Gran Turismo official site. Publication/update: 2026-03-12. [Inspected route or disclosed lead](https://www.gran-turismo.com/us/gt7/news/00_8497133.html).

Edition/build: Gran Turismo 7 update 1.68; historical release note, not a latest-build certification. Access: `relevant-excerpt`. Type: Official release note; documentary observed example. Locator: Other Improvements and Adjustments, 2. World Circuits and 4. Power Pack. Claims in this artifact: P-C01. Limits/provenance: Documentation establishes a stated version change, not measured competitive equality, current compatibility, or player benefit. Same production family as leads 002 and 003.

### GDR-SRC-20261010-G18-007

Electronic Arts. *EA SPORTS FC 26 Accessibility Resources*. EA accessibility resources. Publication/update: unknown. [Inspected route or disclosed lead](https://www.ea.com/able/resources/ea-sports-fc/fc-26).

Edition/build: FC 26, US-English PC and console scope stated by page; exact patch unknown. Access: `relevant-excerpt`. Type: Official settings documentation; documentary observed example. Locator: Scope introduction; Controller Customization; Gameplay Settings; Passing; Switching; narration/language sections. Claims in this artifact: P-C01/P-C04. Limits/provenance: Not an exhaustive platform, language or live-build audit. Competitive-mode restrictions are product-specific, not a universal fairness rule. Same publisher and title family as 008.

### GDR-SRC-20261010-G18-009

The International Football Association Board (IFAB). *Laws of the Game 2025/26: Law changes*. IFAB. Publication/update: 2025/26 edition; webpage publication day unknown. [Inspected route or disclosed lead](https://www.theifab.com/law-changes/2025-26/).

Edition/build: Association football Laws 2025/26 change text. Access: `relevant-excerpt`. Type: Formal sport-rule authority; edition-scoped normative text. Locator: Law 12.3, goalkeeper control beyond eight seconds and corner-kick sanction; Law 11.2, offside judgement for a goalkeeper throw. Claims in this artifact: P-C01. Limits/provenance: Applicable to the identified football-law edition and relevant competition adoption, not a native-game accessibility or timing standard. The later 2026/27 complete edition was not retrieved; 010 confirms that an edition transition occurred.

### GDR-SRC-20261010-G18-010

IFAB. *The IFAB introduces further measures to improve match flow and player behaviour*. IFAB. Publication/update: 2026-02-28. [Inspected route or disclosed lead](https://www.theifab.com/news/the-ifab-introduces-further-measures-to-improve-match-flow-and-player-behaviour/).

Edition/build: Official announcement of 2026/27 changes. Access: `relevant-excerpt`. Type: Official announcement; documentary observed example, not the complete normative edition. Locator: Final paragraph: new edition effective 1 July 2026 and competition adoption timing. Claims in this artifact: P-C01. Limits/provenance: Supports freshness caution and edition transition only. It does not substitute for all clauses in inaccessible source 016. Organizationally related to 009 and 016.

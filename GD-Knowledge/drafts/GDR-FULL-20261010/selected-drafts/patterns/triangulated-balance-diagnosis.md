---
id: GDR-CAND-20261010-F07-PAT-01
kind: pattern
title: Triangulated balance diagnosis
version: 0.1.0
status: draft
candidate_revision: initial-capture-1
attempt_identity: F07-visible-session-20261010-A1
predecessor_sha256: null
supersedes: null
change_summary: Initial complete capture in this visible session; no earlier F07 artifact was found in the supplied
  files.
owner_project: BH-GDR-Foundations-and-Systems
run_id: GDR-FULL-20261010
batch_id: F07
updated: '2026-10-10'
evidence_checked: '2026-10-10'
input_snapshot: 'Supplied starter files (INDEX and REGISTERS: 0.1.0 candidate) plus attached F07 brief; no canonical
  receipt available.'
aliases:
- diagnose before tuning
- falsifiable balance change
- mixed-method balance diagnosis
tags:
- evaluation
- balancing
- diagnosis
- causal-uncertainty
related_topics:
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-F07-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-F07-001
- GDR-SRC-20261010-F07-002
- GDR-SRC-20261010-F07-003
- GDR-SRC-20261010-F07-004
reviewer: null
approved_by: null
approved_date: null
---

# Triangulated balance diagnosis

**Candidate technique, not an established law.** This pattern combines source-informed methods into an original, unvalidated recipe. “Triangulated” means checking a proposed explanation against different relevant observations—not requiring three tests, three sources, or three agreeing metrics. No playtest or prototype was performed.

## Purpose

Use this pattern when a proposed balance change might fix the wrong problem: low option use, repeated failure, apparent dominance, uneven contribution, confusing recovery or an outcome that differs across audiences. Its intended player-facing benefit is a change that addresses the actual obstacle while preserving the intended decision and legitimate alternatives. Its immediate output is a **bounded diagnosis and disposition**, not permission to ship. [C-01]

## Context and prerequisites

The team can describe the desired experience, identify the relevant ruleset/build, inspect at least one meaningful observation, and state an alternative explanation. It has enough control to represent or compare the disputed behavior without changing the whole experience unintentionally. The owner accepts that the result may be “not yet distinguishable,” “do not tune” or “change explanation/access instead.” [C-01, C-02]

Separate approval is required before recruitment, data collection or exposure. Relevant language, input, assistance, learning and interaction conditions must be identifiable. Access to a large analytics platform is not a prerequisite: a small auditable observation record may be sufficient for a discovery question. A complete quantitative effect claim, however, requires an appropriate design and adequate uncertainty assessment. [C-02, C-03]

## Mechanism and evidence

| Proposed causal link | Evidence-to-application bridge | Limit that prevents a stronger claim |
|---|---|---|
| An explicit experience objective changes which observations matter | If success means understandable counterplay, usage alone omits part of the objective; this follows from the stated definitions | The objective itself requires local approval, and can be contested [C-01] |
| Alternative explanations lead to more discriminating observations | Prototype dimensions and complementary observation methods supply ways to represent and investigate different uncertainties | Neither source validates this assembled diagnostic recipe [C-02] |
| Auditing the observation process reduces the chance of mistaking measurement change for player change | Industrial metric pitfalls motivate inspection of denominator, loss and exposure | Correct logs still may measure the wrong construct; no game-specific error-reduction rate is known [C-03] |
| A comparison tied to the diagnosis makes a change more interpretable | Holding relevant conditions stable narrows competing explanations; explicit uncertainty prevents declaring an imprecise result decisive | Interactions, carryover and sparse samples can defeat the comparison [C-04] |
| Rechecking the intended audience and neighboring rules can reveal displaced problems | A targeted fix may alter another option or privilege familiar users; those are explicit counterexamples to local sufficiency | The amount of regression coverage needed remains project-specific [C-05] |

The complete chain is a hypothesis. Multiple measures sharing the same participants, exclusions or flawed definition are not independent corroboration. Disagreement between methods is a finding to explain, not a vote to be suppressed. [C-06]

## Recipe

1. **Write a one-decision record.** Describe the problem in observable terms; name the intended player outcome, population, ruleset and time horizon. Record who can accept a change and the cost of a wrong decision. Do not start with an unexplained target such as “raise retention.” [C-01]
2. **List plausible mechanisms.** For an unused option, consider power, understanding, availability, feedback, execution demand and preference. Choose the few explanations that would lead to materially different changes, rather than making an exhaustive list no one can test. Record a discriminating prediction for each. [C-02]
3. **Choose the cheapest valid representation.** A rule explanation can test understanding; an interactive slice may be needed for timing; a bounded analytical case may expose a resource exploit. Document omitted conditions. Exit if an omitted condition is essential and cannot be represented. [C-02]
4. **Write the evidence contract.** Specify observations and any metric's event, denominator, unit, exposure window, exclusions and uncertainty. State necessary guardrails and the future test's stopping policy. A small discovery study should make a discovery claim, not an effect-size claim. [C-03, C-04]
5. **Obtain separate study authorization, then inspect validity before results.** Future execution should check actual exposure, missing events, duplicates, differential dropout and moderator interventions. If integrity cannot be established, stop the affected inference. No authorization or data collection occurs through this recipe alone. [C-03]
6. **Compare competing explanations.** Place visible behavior, participant explanations and measured distribution side by side. Mark whether each supports, weakens or leaves a mechanism unresolved. Do not infer intent or hidden motivation solely from an action. [C-02, C-06]
7. **Choose a bounded candidate or no change.** Address the best-supported mechanism. Keep other variables fixed only where that is meaningful; if mechanisms interact, define the combination explicitly. Preserve the baseline and a way to reject the candidate. [C-04, C-05]
8. **Evaluate the declared outcome and guardrails.** Inspect relevant audiences and interactions, reporting uncertainty and exploratory findings separately. Choose keep, revise, revert or defer, with a recorded reason. No effect established is different from evidence of no meaningful effect. [C-04]
9. **Close or exit deliberately.** Close this diagnosis when the evidence supports a bounded disposition and the remaining uncertainty is acceptable to the authorized owner. Reopen when audience, rules, access conditions or incentives change. Do not continue tuning merely to force the original metric to move. [C-05, C-07]

### Adjustable variables and exit conditions

| Variable | Why it is adjustable | Exit or escalation condition |
|---|---|---|
| Objective and smallest worthwhile improvement | Different experiences value different outcomes | Owner cannot state what a successful change would improve |
| Prototype completeness | Costs and omitted causes vary | Essential timing, social or access conditions cannot be represented |
| Recruitment and relevant distinctions | Prior skill and access may alter the mechanism | Missing a decision-critical group prevents the intended conclusion |
| Comparison and independent unit | Repeated players or interacting teams create dependence | Assignment or contamination cannot support the claimed causal effect |
| Observation window | Discovery, adaptation and re-entry differ | Available time only supports a narrower question; narrow or defer |
| Guardrails and stopping policy | Acceptable risk depends on stakes | Credible serious harm, invalid data, or unacceptable access failure stops the relevant exposure/inference |
| Change breadth | A numerical tweak can be too local for a systemic problem | New interactions make the candidate uninterpretable without redesign |

There are no default sample sizes, win rates, time limits or significance cutoffs. Numeric choices require scoped justification. Invalid evidence leads to a narrower claim or new design, not a new threshold invented after seeing the result. [C-03, C-04]

## Worked examples

### Illustrative example: high failure around a protective action

**Decision:** whether to increase a protective action's strength. **Observed premise for the illustration:** a hypothetical team sees frequent failure soon after selection; no real data are asserted.

**Competing explanations:** the protection is insufficient; activation is misunderstood; successful protection is not communicated; the required input is hard in the relevant configuration. A blanket strength increase predicts improvement even when understanding is already correct. A comprehension explanation predicts that informed use, without strength changes, should reduce the particular failure. An input explanation predicts a configuration-specific difference.

**Representation:** a rule-state explanation task followed, only with approval, by a narrow interaction slice. Keep resource costs and encounter availability constant. Record whether the player predicts the protected state, invokes it, perceives the outcome and can recover. Treat each as a different observation, not four interchangeable success scores.

**Disposition:** if the explained rule becomes understood but failures still track a particular execution condition, abandon the comprehension-only diagnosis and investigate that condition. If strength changes help novices while eliminating counterplay for skilled opponents, the candidate fails its guardrail. If observations disagree and the sample cannot distinguish explanations, defer a global buff. All outcomes are hypothetical branches. [C-01–C-06]

### Illustrative counterexample: the stated conservation rule is violated

A hand-worked transition duplicates a resource when the approved rule says it must be conserved. If that transition is directly reproducible, diagnosing enjoyment is unnecessary to establish the rule violation. The appropriate path is an authorized correction and regression check, not forcing a full mixed-method player study. This example limits the pattern's scope; it does not authorize implementation. [C-07]

## Tradeoffs and alternatives

The process consumes design attention and may slow a low-stakes decision. A single direct observation can be sufficient for a narrowly stated defect; a clear preference question may need an interview, not a factorial experiment. At the opposite extreme, many interacting rules can require a broader analytical or experimental design than this recipe supplies. [C-02, C-04, C-07]

A faster expert judgment remains an option when the decision is reversible and the team records its uncertainty. A full quantitative comparison is preferable when a consequential effect estimate is needed and the necessary units and sample are available. Neither option permits claiming stronger support than obtained. Cross-language or access validation may be the best use of limited capacity before adding more average-population data. [C-02–C-04]

## Failure cases

The team may collect three measures of the same flawed proxy and mistake agreement for confirmation. It may recruit only people who already mastered the system, change mechanics and explanation together unintentionally, or delete interrupted sessions from the denominator. It may also optimize an outcome that removes valued challenge. Warning signs are unexplained exclusions, unstable event definitions, missing alternative explanations, and a decision that never changes regardless of the result. [C-03, C-04, C-06]

Corrections are correspondingly specific: repair or abandon the affected metric; recruit the missing context; separate or explicitly model simultaneous changes; restate the experience objective; or acknowledge that the current evidence cannot discriminate. The proposed process itself should be discarded or simplified when its extra steps do not change decisions and merely consume capacity. [C-07]

## Counterexamples and do not use conditions

Do not use this as a bureaucratic prerequisite for every rule correction, a substitute for expert analysis of interference, or an excuse to expose players to an already credible serious harm. Do not use it when the owner refuses any result other than the favored change. Do not claim causal validation from a paper mock-up of an execution problem. A valuable, knowingly chosen asymmetry should not be flattened merely because a metric is unequal. [C-01, C-04, C-07]

## Playtest

**Proposed / NOT PERFORMED.** At the player level, compare a diagnosis-linked candidate with its baseline under an approved design. Include relevant unfamiliar/experienced and access conditions. Measure the intended outcome, the hypothesized mechanism and guardrails separately. Hold availability, explanation, input and encounter context stable or explicitly include them in the contrast. Reject the mechanism if its discriminating prediction fails; reject the candidate if the intended benefit is absent within adequate precision or an unacceptable guardrail failure occurs. An inconclusive result supports neither acceptance nor a claim of no effect. [C-04, C-05]

To test the **process**, a separately authorized design-method study could compare this recipe with a simpler review on comparable diagnostic tasks with independently established rule/instrumentation faults. Assess correct diagnosis, false confidence, time cost and missed access cases. Task familiarity and reviewer expertise would be confounds. Reject the added process if it does not improve relevant decisions enough to justify its cost, or if it creates unwarranted certainty. That would test diagnostic work—not prove that resulting games are more enjoyable. [C-07]

## Claim ledger

Material recommendations below are original synthesis unless explicitly attributed. A source-informed proposal is not an approved studio decision or a validated complete technique.

### C-01

**Claim:** An explicit balance decision should precede the choice of diagnostic evidence.

**Class:** `inference`. **Confidence:** moderate — Logical alignment; actual decision benefit unmeasured.

**Evidence and locator:** No external source; explicitly identified original reasoning/proposal.. Purpose, scope and worked example.

**Support / contrary evidence:** Different intended experiences require different observations. **Applicability:** Ambiguous balance decisions, not every rule defect. **Unresolved:** Does the stated objective reflect affected players and authorized priorities?

### C-02

**Claim:** Represent the disputed mechanism and choose complementary observations rather than insisting on a fixed method count.

**Class:** `inference`. **Confidence:** moderate — Primary methodological relevance, context-specific transfer.

**Evidence and locator:** GDR-SRC-20261010-F07-001, GDR-SRC-20261010-F07-002. Houde/Hill §§3.1–3.2; Ambinder slides 16, 20, 35.

**Support / contrary evidence:** Source-informed assembly; no direct validation of this complete pattern. **Applicability:** Discovery and prototype selection. **Unresolved:** Could a cheaper method distinguish the alternatives equally well?

### C-03

**Claim:** An auditable observation contract can expose invalid measurements before a balance claim is made.

**Class:** `inference`. **Confidence:** moderate — Mechanism is clear; error-reduction magnitude is unknown.

**Evidence and locator:** GDR-SRC-20261010-F07-004. §4; §§5.1–5.3.

**Support / contrary evidence:** Industrial measurement pitfalls motivate this design constraint. **Applicability:** Logs, manual counts and eligibility definitions. **Unresolved:** Which unobserved data-quality failures would remain?

### C-04

**Claim:** A bounded comparison requires a justified sample, unit, stopping policy and interpretation of uncertainty.

**Class:** `inference`. **Confidence:** moderate — Methods support conditions, not a universal guarantee.

**Evidence and locator:** GDR-SRC-20261010-F07-003, GDR-SRC-20261010-F07-004. Lakens named sample-size sections; Dmitriev §§5.4, 5.6–5.7.

**Support / contrary evidence:** Not a complete analysis specification for multiplayer/network effects. **Applicability:** Any proposed effect estimate. **Unresolved:** Can the available design resolve a decision-relevant effect?

### C-05

**Claim:** Diagnosis-linked changes and targeted rechecks may reduce displaced problems compared with blind tuning.

**Class:** `hypothesis`. **Confidence:** low — No comparative evaluation performed.

**Evidence and locator:** No external source; explicitly identified original reasoning/proposal.. Mechanism chain and illustrative protective-action example.

**Support / contrary evidence:** Possible advantage; broader redesign or expert correction may be superior. **Applicability:** Revisable systems with stated guardrails. **Unresolved:** Does the process catch problems the simpler alternative misses?

### C-06

**Claim:** Agreement among measures with shared bias is not independent corroboration.

**Class:** `inference`. **Confidence:** high — Logical counterexample defeats automatic independence.

**Evidence and locator:** No external source; explicitly identified original reasoning/proposal.. Shared-definition and shared-sample counterexamples.

**Support / contrary evidence:** Same error can create agreement in every channel. **Applicability:** Interpretation of triangulation. **Unresolved:** What genuinely different failure mode does each observation address?

### C-07

**Claim:** The recipe should be narrowed or omitted when it cannot change a decision or its costs exceed its diagnostic value.

**Class:** `hypothesis`. **Confidence:** moderate — Defensible stopping rationale; not empirically calibrated.

**Evidence and locator:** GDR-SRC-20261010-F07-003. “The Value of Information”; proposed process test and rule-defect counterexample.

**Support / contrary evidence:** Decision value motivates an exit, but local costs and benefits are unmeasured. **Applicability:** Scope selection, urgent safe correction and limited resources. **Unresolved:** Would a simpler review make the same decision with comparable confidence?

## References

Source IDs are temporary F07 identities. Same-source aliases/DOIs are not additional independent evidence.

### GDR-SRC-20261010-F07-001

Stephanie Houde and Charles Hill. **What Do Prototypes Prototype?**. 1997. Elsevier; author chapter hosted by Stanford HCI. Handbook of Human-Computer Interaction, 2nd edition, chapter 16, pp. 367–381; reformatted 16-page copy. DOI: `10.1016/B978-044481862-1.50082-0`.

[Inspected source](https://hci.stanford.edu/courses/cs294h/2006/readings/houde-prototypes-97.pdf). Accessed 2026-10-10; access: `relevant-excerpt`. **Locators:** PDF pp. 1, 3–4; §§3.1–3.2; Figure 1 (PDF p. 3 visually inspected). **Type:** Practitioner/conceptual chapter. **Supports:** C-02. **Limits:** Interface-design examples; not an experiment demonstrating game-prototype efficacy. **Relationship:** Independent source identity; cross-batch deduplication pending. **Rights:** Copyrighted source; paraphrase only; no source pages redistributed.

### GDR-SRC-20261010-F07-002

Mike Ambinder, Valve. **Valve’s Approach to Playtesting: The Application of Empiricism**. 2009. Valve; GDC 2009 presentation. 68-slide deck.

[Inspected source](https://cdn.akamai.steamstatic.com/apps/valve/2009/GDC2009_ValvesApproachToPlaytesting.pdf). Accessed 2026-10-10; access: `relevant-excerpt`. **Locators:** PDF slides 5–6, 13–20, 24, 30–35, 39, 42; slides 16, 20 and 35 visually inspected. **Type:** Firsthand practitioner presentation. **Supports:** C-02. **Limits:** Deck distinguishes its fun-focused testing from balancing; simulated-number slides are not empirical datasets. **Relationship:** Independent source identity; cross-batch deduplication pending. **Rights:** Copyrighted source; paraphrase only; no source pages redistributed.

### GDR-SRC-20261010-F07-003

Daniël Lakens. **Sample Size Justification**. 2022-03-22. Collabra: Psychology / University of California Press. 8(1), 33267. DOI: `10.1525/collabra.33267`.

[Inspected source](https://online.ucpress.edu/collabra/article/8/1/33267/120491/Sample-Size-Justification). Accessed 2026-10-10; access: `relevant-excerpt`. **Locators:** “Six Approaches to Justify Sample Sizes”; “The Value of Information”; “Resource Constraints”; “A-priori Power Analysis”. **Type:** Methodological article. **Supports:** C-04, C-07. **Limits:** Sampling rationale, not a game-specific participant-count guarantee. **Relationship:** Independent source identity; cross-batch deduplication pending. **Rights:** Copyrighted source; paraphrase only; no source pages redistributed.

### GDR-SRC-20261010-F07-004

Pavel Dmitriev, Somit Gupta, Dong Woo Kim and Garnet Vaz. **A Dirty Dozen: Twelve Common Metric Interpretation Pitfalls in Online Controlled Experiments**. 2017-08. ACM KDD; Microsoft Research author copy. KDD 2017, 10-page author PDF; website directory date is not publication date. DOI: `10.1145/3097983.3098024`.

[Inspected source](https://www.microsoft.com/en-us/research/wp-content/uploads/2020/08/2017-08-KDDMetricInterpretationPitfalls.pdf). Accessed 2026-10-10; access: `relevant-excerpt`. **Locators:** §4, PDF pp. 2–3; §§5.1–5.4, pp. 3–5; §§5.6–5.7, p. 6; pp. 3 and 6 visually inspected. **Type:** Firsthand industrial experimentation/methods paper. **Supports:** C-03, C-04. **Limits:** Web-product experience; transfer to game outcomes and multiplayer units requires justification. **Relationship:** Independent source identity; cross-batch deduplication pending. **Rights:** Copyrighted source; paraphrase only; no source pages redistributed.

## Related entries and history

Topics: [Evaluation and balancing](../topics/evaluation-and-balancing.md), `GDR-CAND-20261010-F07-TOP-01`; [Ethical and sustainable design](../topics/ethical-and-sustainable-design.md), `GDR-CAND-20261010-F07-TOP-02`. Complement: [Legible commitment and safe exit](legible-commitment-and-safe-exit.md), `GDR-CAND-20261010-F07-PAT-02`. Genre links are not available; none is invented.

Relevant contested questions: `F07-CON-01`, `F07-CON-02`, `F07-CON-03` in the review packet. 2026-10-10: initial-capture-1, 0.1.0 draft; no predecessor or supersession asserted. Byte hash is external in the packet/receipt. Author review only; independent review, actual host tests and release pending.

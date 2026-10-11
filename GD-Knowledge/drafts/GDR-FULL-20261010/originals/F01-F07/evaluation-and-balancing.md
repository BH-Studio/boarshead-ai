---
id: GDR-CAND-20261010-F07-TOP-01
kind: topic
title: Evaluation and balancing
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
- playtesting
- balance testing
- game telemetry
- sample-size justification
- prototype evaluation
- experiment interpretation
tags:
- evaluation
- balance
- measurement-validity
- causal-uncertainty
- qualitative-research
- accessibility
related_topics:
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-F07-PAT-01
- GDR-CAND-20261010-F07-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-F07-001
- GDR-SRC-20261010-F07-002
- GDR-SRC-20261010-F07-003
- GDR-SRC-20261010-F07-004
- GDR-SRC-20261010-F07-005
- GDR-SRC-20261010-F07-006
- GDR-SRC-20261010-F07-012
reviewer: null
approved_by: null
approved_date: null
---

# Evaluation and balancing

**Draft research candidate, not released guidance.** No prototype, participant session, studio telemetry analysis or gameplay experiment was performed for this entry. Its procedures are proposals for separately authorized work. Evidence was checked on 2026-10-10; historical developer accounts retain their original context.

## Decision and scope

This topic helps a designer decide **what uncertainty to investigate, which evidence could resolve it, and what change the evidence actually warrants**. It covers prototype selection, qualitative playtests, telemetry, comparisons, experiment interpretation and balance decisions. It does not provide an engine implementation, a universal KPI dashboard, a participant-count rule or certification that a game is fun, fair or safe. [C-01]

The following are working definitions for this entry, not universal disciplinary definitions. **Evaluation** is comparing evidence with an explicit intended outcome and constraints. **Balancing** is adjusting rules, options, resources or encounter conditions relative to a declared player-experience objective. **Calibration** is checking that a measure or instrument represents its intended quantity. **Validation** is checking whether that quantity and method answer the design question. **A prototype** is a deliberately incomplete representation; its omissions must be compatible with the question. **An estimand** is the precisely described effect sought: on whom, of which change, compared with what, over what period. [C-01, C-02]

Balance may concern viable alternatives, comprehensible counterplay, a learning trajectory, cooperative contribution, recoverability or an explicitly unequal challenge. Choosing among those objectives is a project decision; this library has no authority to choose one for every game. Questions of identity, motivation, access and coercion must not be silently converted into a win-rate target. [C-01, C-10]

## Core explanation and mechanisms

### Separate the evidence-generating processes

A designer changes a rule; that change alters available actions and incentives; a player interprets those possibilities through prior knowledge and circumstances; behavior occurs; instrumentation and questions capture only some of it; analysis supports a bounded conclusion. A failure at any step can explain a disappointing result without proving the rule is intrinsically bad. This chain is a diagnostic model, not an empirically validated causal graph for every game. [C-03]

For example, an unused option could be weak, undiscovered, badly explained, inaccessible on a device, deliberately niche, expensive to unlock or simply disliked. A usage count alone cannot distinguish those explanations because they can produce the same count. Prefer the cheapest next observation that would make the explanations predict different outcomes. [C-03]

Houde and Hill distinguish prototype questions concerning role, look-and-feel and implementation. Ambinder describes complementary observation, verbal-report and logging approaches, including their weaknesses. These are methodological starting points rather than proof that a fixed sequence produces better games. The transferable inference is to select a representation and observation method for a specific uncertainty, not for apparent polish. [C-02, C-04]

### Measurement is not the experience itself

A measure requires a definition, denominator and interpretation. “Completion” could mean winning once, finishing an intended session, or reaching an ending; “retention” depends on the eligible cohort and return window. A shorter session can reflect efficient goal completion or rejection. High activity can coexist with confusion or pressure. Neither interpretation follows from the count alone. [C-05]

The industrial experimentation paper by Dmitriev and colleagues distinguishes data-quality, success, guardrail and diagnostic metrics, and documents denominator and telemetry-loss pitfalls. Its strongest transferable contribution here is **checking the observation process before interpreting a movement**. Its preference for a business-oriented overall metric is not adopted as a universal design objective. [C-06]

### Different methods answer different questions

| Uncertainty and candidate method | What a useful result could establish | What it does not establish; cost or alternative |
|---|---|---|
| Rule comprehension: cards, paper states or a clickable mock-up with explanation-back | Whether tested people interpret represented rules as intended | Not response timing, motor access or network play; use a narrow interactive slice when those matter |
| Feel, timing or physical execution: a limited interactive slice | Behavior under the represented input, feedback and timing | Not the whole progression or long-term economy; omit expensive final art only when its absence does not change the question |
| Resource conservation or extreme combinations: a bounded analytical model | Consequences of specified rules and assumptions, including impossible states | Not enjoyment or human strategy; begin with hand-worked boundary cases if a large model adds little |
| Discovery and reasoning: moderated observation followed by neutral questions | What happened in the tested context and what the participant says they understood | Not representative prevalence or unconscious causes; moderation and think-aloud may alter play |
| Frequency/distribution: minimally necessary telemetry | How often defined recorded events occur in the instrumented population | Not why people act, unlogged experiences or excluded players; a manual tally may suffice in an early study |
| Causal comparison: randomized, counterbalanced or otherwise justified comparison | An effect of the tested contrast, conditional on valid assignment, measurement and analysis | Not every mechanism, audience or future metagame; use qualitative diagnosis first when the contrast is not yet clear |
| Longer-horizon adaptation: repeated observations and re-entry checks | Change over the observed interval and stability of identified problems | Not indefinite retention or wellbeing; shorter work may answer a narrower question honestly |

This table is proposed method-selection guidance derived by reasoning from the sources, not a ranking of methods or a demand to use all of them. A no-build explanation test is preferable to an expensive prototype when it resolves the actual decision. Conversely, a paper test should not be used to sign off on timing-sensitive access. [C-02–C-05, C-07]

## Design choices and alternatives

### Qualitative work: diagnostic depth without invented prevalence

Recruit for the distinctions that might change the answer: relevant prior experience, learning stage, access needs, language, input device, available time and familiarity with this build. State whom the sample omits. Include people who struggle or decline to continue rather than explaining them away as the wrong players after seeing their responses. A deliberately selected sample can expose a mechanism; it does not estimate how common that mechanism is in the whole market. [C-07]

Use an observation record that separates **visible event**, **participant account**, **researcher interpretation** and **alternative explanation**. Ask a participant to explain an action before describing the intended rule. Record moderator prompts and assistance. If concurrent thinking aloud changes the relevant timing or concentration, observe silently and ask afterward, while recognizing the resulting recall limitation. Preserve disconfirming cases and disagreements in coding instead of forcing every report into a preferred theme. [C-04, C-07]

Repeated internal play can be valuable for consistency checks yet weak for rediscovering unfamiliarity. In his Never Alone postmortem, Roberts describes issues missed by familiar internal/friends-and-family play and argues for a closed beta. That is a relevant caution, not controlled evidence that a beta would have prevented those issues. [C-08]

### Quantitative work: sample size follows the decision

Specify the smallest change worth acting on, tolerable uncertainty, variability, analysis unit, and cost of a false positive versus a missed improvement. Lakens describes several defensible sample-size rationales, including precision, power, resources and value of information. None supplies a universal number of players for this topic. [C-09]

A useful discovery interview count is not the same quantity as the number of independent units needed to estimate an effect. Hundreds of attempts from one person are not hundreds of independent players. Within-player comparisons can be efficient, but learning, fatigue and irreversible unlocks may contaminate later conditions. Random assignment reduces systematic allocation differences in expectation; it does not erase finite-sample uncertainty, differential dropout, spillovers or invalid measurement. [C-07, C-11]

Write the analysis plan before reading the primary outcome. Distinguish a fixed-horizon comparison from a correctly designed sequential method; do not repeatedly check conventional significance and stop at the first favorable result. Stopping exposure for a serious safety concern is a separate obligation, not permission to relabel a stopped study as proof of efficacy. Report effect magnitude and uncertainty alongside the practical decision. A result that cannot rule out both useful benefit and unacceptable harm is inconclusive. [C-06, C-09, C-11]

### Balance has multiple objectives and contextual dependencies

A near-equal overall win rate does not establish viable choices, readable losses or fair access. For a closed two-player system with exactly one winner per match, the combined participants' win rate is one half by construction. A system can satisfy that identity while particular choices or matchups are severely unequal. Similarly, equal contribution totals can hide unequal effort, risk or agency. These are logical counterexamples, not claims about a named game. [C-10]

Inspect conditional outcomes across declared skill bands, matchups, learning stage, input/access configurations and unlock availability when those distinctions are relevant. Avoid post-hoc subgroup fishing: distinguish predeclared decision-relevant groups from exploratory leads. Small subgroups deserve uncertainty and targeted follow-up, not an automatic “no difference.” Do not demand that every option be equally strong in every context if specialization is the intended experience. [C-10, C-11]

Riot's historical 2020 account uses audience-specific balance criteria and acknowledges that its framework detects outliers without deciding how to preserve an option's identity or identify every game-health problem. Treat that as a practitioner example of limits, not permission to import its thresholds. [C-12]

Alternatives to changing raw power include improving explanation, availability, counterplay, encounter distribution or recovery. A global numerical adjustment is warranted only when the diagnosis supports a sufficiently general underlying issue. Where options interact, a local improvement can create a different dominant combination or power escalation; inspect the surrounding system and preserve a reversible comparison baseline. This is proposed reasoning, not evidence that one-variable-at-a-time tuning always suffices. [C-03, C-10, C-13]

## Application process

1. **Write a decision contract.** State the observed problem, intended experience, target population, current build/ruleset, competing explanations, proposed contrast and consequences of being wrong. Choose either a discovery question or a confirmatory question; do not quietly change categories after results arrive. [C-01, C-03]
2. **Set scope and safeguards.** Identify what the prototype omits, relevant access/language cases, consent and withdrawal arrangements, privacy limits and unacceptable harms. Obtain separate authorization before collecting data or exposing players to a change. [C-02, C-14]
3. **Choose the least costly discriminating method.** Use the table above. Estimate whether the available sample and time can support the intended decision. If not, reduce the claim or postpone the decision instead of lowering the evidence standard silently. [C-07, C-09]
4. **Specify the observations.** For every metric record its event definition, numerator, denominator, eligible units, missingness, version, time window and intended interpretation. Add a direct player-experience measure where the decision concerns experience. Do not collect sensitive attributes merely because segmentation is possible. [C-05, C-06, C-14]
5. **Design the comparison.** Record assignment, exposure, analysis units, order, carryover, exclusions and stopping rules. In interacting populations, consider whether treatment affects teammates or opponents; player-level independence may be untenable. Seek qualified analysis review when cluster or network effects matter. [C-11]
6. **Collect only after approval; inspect validity first.** Future reviewers should check assignment/exposure integrity, event completeness, denominator changes, anomalous counts and differential attrition before interpreting outcomes. This step is specified, not executed here. [C-06]
7. **Interpret competing accounts.** Compare observations, reports and distributions without counting them as independent when they share participants or assumptions. Label unexpected findings exploratory. A disagreement can reveal a measurement mismatch rather than an uncooperative player. [C-03, C-05, C-07]
8. **Make a bounded disposition.** Keep, revise, revert, defer or run a more discriminating study. Record why, with effect uncertainty, residual risks and what would reverse the decision. A commercial metric cannot override an explicit ethical stop condition. [C-09, C-13, C-14]
9. **Retest the relevant change.** Recheck affected combinations and access conditions, plus unfamiliar players where learning mattered. Preserve the prior revision and rationale. A test report is evidence for a decision, not automatic approval to ship. [C-08, C-13]

## Patterns and genre adaptations

[Triangulated balance diagnosis](../patterns/triangulated-balance-diagnosis.md), `GDR-CAND-20261010-F07-PAT-01`, packages the diagnostic loop for a bounded balancing decision. [Legible commitment and safe exit](../patterns/legible-commitment-and-safe-exit.md), `GDR-CAND-20261010-F07-PAT-02`, adds an ethics-focused decision case. Both remain draft hypotheses at the level of their assembled recipes.

[Ethical and sustainable design](ethical-and-sustainable-design.md) owns the broader risk and benefit choices. No genre file was supplied or reviewed. Genre-specific objectives, expectation conflicts and play conventions remain future adaptations; this entry supplies no inherited genre rule. Missing topic dependencies are identified in the review packet rather than linked to invented files.

## Examples and counterexamples

### Illustrative example: an apparent power problem that could be an information problem

Suppose a reusable system offers a fast, fragile option and a slower, protective option. Novices abandon the protective option after a loss. The team considers increasing its output. Four explanations remain: insufficient output; an unread activation condition; feedback that conceals successful protection; or excessive input burden.

A proposed first comparison keeps numerical rules fixed and changes only the clarity of the activation explanation, while observing whether participants can predict the protected state before committing. A separate narrow interaction test addresses the input burden. Only after those questions are separated does a power change become a clean candidate. If explanation improves but disadvantage persists among informed users in the same matchup, the information-only account weakens. If improving power makes expert use dominant while novices remain confused, the global buff failed its intended purpose. All outcomes in this paragraph are conditional examples, not observations. [C-03, C-13]

### Illustrative arithmetic: aggregate improvement can reverse within groups

The following invented counts describe successful attempts, not an actual experiment. Group composition differs deliberately.

| Build | Novice attempts | Experienced attempts | Combined |
|---|---:|---:|---:|
| A | 10 / 40 = 25% | 54 / 60 = 90% | 64 / 100 = 64% |
| B | 24 / 60 = 40% | 38 / 40 = 95% | 62 / 100 = 62% |

A's combined rate is higher although B's rate is higher in each shown group. The arithmetic demonstrates why these aggregate proportions alone cannot decide which build improves outcomes for the same target population. It does not prove B's causal superiority: assignment, other differences and repeated attempts remain unspecified. Nor does it establish that increasing success is the desired experience. [C-15]

### Counterexample to “more evidence is always better”

A reproducible rule error allows resource duplication. Once the stated conservation rule and erroneous transition are directly established, a long player experiment may be irrelevant to whether that defect violates the rule. Correcting it still requires implementation authorization and regression checks, but a full enjoyment study need not precede every correction. Conversely, discovering that a puzzle is difficult does not establish a defect when difficult discovery is the intended experience. [C-01, C-16]

## Failure modes and constraints

**Construct substitution.** Repeated returns, spend, completion, satisfaction and wellbeing answer different questions. This entry does not certify one as a substitute for another. The longitudinal study by Vuorre and colleagues is examined in the ethics topic precisely because its exposure, outcome and assumptions must be kept separate from a retention KPI. [C-05, C-17]

**Convenience and survivorship.** Current enthusiasts, high-end hardware users and people who finish the session can omit the populations experiencing the problem. Removing interrupted or assisted sessions after seeing results may change the question. Record exclusions and who is missing, and keep help use visible where it is an outcome. [C-07, C-11]

**Instrumentation without necessity.** Broad logging may consume engineering, storage, review and privacy capacity while adding little decision value. Prefer a small auditable event set. If missing events cannot be distinguished from a lack of behavior, restrict the claim rather than treating all missingness as zero. [C-06, C-14]

**Localization and access mismatch.** Translation may alter the explanation being tested; assist settings may alter execution while preserving the intended decision. Record language and configuration as conditions, not defects to be normalized away. A test with one input mode cannot sign off on an untested mode. These are proposed evaluation constraints, not a validated translation protocol. [C-18]

**Production and ecological cost.** A polished slice may consume the budget needed to investigate the actual failure; an inexpensive mock-up may omit the failure entirely. Live comparisons can create support, compatibility and community-trust costs. Choose the method's scope deliberately and record what was sacrificed. [C-02, C-09, C-16]

## Playtest and validation

**All protocols below are proposed / NOT PERFORMED. No participants or game data were used in this batch.** A future project must set its own meaningful-effect and harm bounds before collection. There is no numerical default sample size or success threshold in this topic.

| Proposed study | Procedure and relevant participants | Measures, confounds and decision rule |
|---|---|---|
| Information versus power diagnosis | With separately approved participants spanning relevant familiarity and access cases, compare unchanged mechanics under current versus revised explanation; use different but equivalent tasks or counterbalanced order where learning permits | Measure prediction of the rule, independently performed actions and reason given. Hold availability/input/encounter conditions constant. Reject an information-only diagnosis if comprehension changes but the stated disadvantage remains under comparable conditions |
| Targeted balance contrast | Compare baseline and candidate rule in a justified assignment design; define skill, unlock state and interaction units before sampling | Measure the declared player outcome plus counterplay, access and concentration-of-choice guardrails. Estimate uncertainty at the actual independent-unit level. Keep the conclusion inconclusive when plausible benefit and harm both remain; a favorable average cannot erase a prespecified unacceptable subgroup failure |
| Measurement validity challenge | In a separately authorized narrow slice, compare event records against a documented sequence of known actions and neutral player explanations | Test duplicate/missing events, aborts, assists, disconnects, denominator changes and version labels. Reject affected metric interpretations when the event-to-claim mapping fails. This verifies instrumentation, not enjoyment |
| Familiarity and re-entry check | Use unfamiliar and returning participants; record prior exposure; include a planned interruption compatible with consent | Observe discovery, recovery and dependence on moderator assistance. Revise the claim if a benefit exists only among repeatedly coached testers or if a re-entry safeguard makes the intended decision inaccessible |

A future sample plan must identify the target decision, expected variability or a defensible range, dependence structure, feasible recruitment, relevant heterogeneity and the remaining uncertainty if the budget is exhausted. A small study may justify discovering a problem while being insufficient to estimate its prevalence or the effectiveness of its remedy. [C-07, C-09, C-11, C-18]

## Claim ledger

Material recommendations below are original synthesis unless explicitly attributed. A source-informed proposal is not an approved studio decision or a validated complete technique.

### C-01

**Claim:** Declare the player-experience decision and balance objective before choosing a metric or method.

**Class:** `inference`. **Confidence:** moderate — The logic is explicit, but its operational benefit has not been tested here.

**Evidence and locator:** No external source; explicitly identified original reasoning/proposal.. Working definitions and decision contract in this entry.

**Support / contrary evidence:** Different objectives can prefer different outcomes; no empirical effectiveness claim for the contract. **Applicability:** Genre-neutral design decisions; approval belongs to the receiving project. **Unresolved:** Who owns the objective and which tradeoffs are acceptable?

### C-02

**Claim:** Prototype fidelity should be selected for the uncertainty it can represent, not equated with overall maturity.

**Class:** `inference`. **Confidence:** moderate — Conceptual basis is direct; game-specific validity remains conditional.

**Evidence and locator:** GDR-SRC-20261010-F07-001. §§3.1–3.2, PDF pp. 3–4.

**Support / contrary evidence:** Role/look-and-feel/implementation distinction informs the transfer; it does not validate a specific game slice. **Applicability:** Representation choice, including intentional omissions. **Unresolved:** Which omitted variables could reverse the decision?

### C-03

**Claim:** Low use or poor outcomes can fit multiple mechanisms; choose observations that discriminate among those mechanisms.

**Class:** `inference`. **Confidence:** moderate — Mechanisms are plausible alternatives, not established causes in a real game.

**Evidence and locator:** No external source; explicitly identified original reasoning/proposal.. Original diagnostic model and illustrative option example.

**Support / contrary evidence:** Identical aggregate behavior can be produced by different stipulated causes; this is a reasoning argument. **Applicability:** Diagnosis before tuning. **Unresolved:** Which alternative has a prediction different from the preferred explanation?

### C-04

**Claim:** Observation, verbal reports and aggregate logs have complementary limitations; think-aloud can itself alter the task.

**Class:** `practitioner-heuristic`. **Confidence:** moderate — Firsthand method experience, limited quantitative validation in this deck.

**Evidence and locator:** GDR-SRC-20261010-F07-002. Slides 16, 20 and 35.

**Support / contrary evidence:** Valve practitioner account; not a controlled comparison establishing a universal method hierarchy. **Applicability:** Method selection; source explicitly does not present a balancing-validation experiment. **Unresolved:** What does the chosen method suppress or change?

### C-05

**Claim:** Event counts do not by themselves identify experience, intention or wellbeing.

**Class:** `inference`. **Confidence:** high — Logical non-identification, not an empirical claim about effect magnitude.

**Evidence and locator:** No external source; explicitly identified original reasoning/proposal.. Metric definitions and alternative interpretations in this entry.

**Support / contrary evidence:** One count can be consistent with opposing explanations; no clinical inference follows. **Applicability:** Telemetry and proxy interpretation. **Unresolved:** What independent observation makes the intended interpretation credible?

### C-06

**Claim:** Check measurement integrity and denominator changes before interpreting experiment outcomes; do not treat an imprecise null or opportunistic stopping as evidence of success or safety.

**Class:** `practitioner-heuristic`. **Confidence:** moderate — Strong methodological relevance; not game-specific proof.

**Evidence and locator:** GDR-SRC-20261010-F07-004. §4 and §§5.1–5.4, 5.6–5.7.

**Support / contrary evidence:** Industrial methods and documented pitfalls; game transfer requires a valid unit and outcome. **Applicability:** Instrumented comparisons, with explicit stopping design. **Unresolved:** Are missingness, exposure and analysis units consistent with the intended contrast?

### C-07

**Claim:** Purposive qualitative sampling and transparent observation/coding can diagnose a problem without establishing its prevalence.

**Class:** `inference`. **Confidence:** moderate — Sound scope distinction; no qualitative saturation guarantee established.

**Evidence and locator:** GDR-SRC-20261010-F07-002, GDR-SRC-20261010-F07-003. Ambinder slides 13–24; Lakens “Six Approaches” and “Resource Constraints”.

**Support / contrary evidence:** Proposed synthesis; adding different methods does not make shared sampling bias independent. **Applicability:** Discovery studies with declared recruitment limits. **Unresolved:** Which dissenting or excluded cases would change the explanation?

### C-08

**Claim:** A firsthand postmortem reports that familiar testing missed issues and recommends a closed beta; that counterfactual was not experimentally demonstrated.

**Class:** `practitioner-heuristic`. **Confidence:** moderate — Author had direct production involvement; retrospective causal attribution remains limited.

**Evidence and locator:** GDR-SRC-20261010-F07-006. “What Went Wrong?”, §1.

**Support / contrary evidence:** Production account, not direct observation by this batch. **Applicability:** Caution about repeated familiar samples. **Unresolved:** Would unfamiliar exposure reveal a different mechanism in the target project?

### C-09

**Claim:** Justify sample size from the decision, desired precision or power, resources and value of information; no universal count is supported here.

**Class:** `practitioner-heuristic`. **Confidence:** high — Source directly addresses multiple justifications, not a fixed number.

**Evidence and locator:** GDR-SRC-20261010-F07-003. “Six Approaches”; “The Value of Information”; “Resource Constraints”; “A-priori Power Analysis”.

**Support / contrary evidence:** Methodological guidance; effect, variability and cost must be local. **Applicability:** Quantitative studies; qualitative discovery is a different objective. **Unresolved:** What uncertainty will remain under the feasible sample?

### C-10

**Claim:** Equal aggregate success is insufficient to establish balanced choices, readable losses or equitable access.

**Class:** `inference`. **Confidence:** high — The counterexample follows from the stated assumptions.

**Evidence and locator:** No external source; explicitly identified original reasoning/proposal.. Closed two-player identity and distinct balance objectives.

**Support / contrary evidence:** Logical counterexamples disprove sufficiency, not the usefulness of win rates. **Applicability:** Systems with different intended balance objectives. **Unresolved:** Which contextual inequalities are intended and which are failures?

### C-11

**Claim:** Assignment, repeated measures, attrition, subgroup selection and interacting players constrain causal interpretation.

**Class:** `inference`. **Confidence:** moderate — General methodological transfer; cluster/network design is not supplied as a validated analysis recipe.

**Evidence and locator:** GDR-SRC-20261010-F07-004. §2; §§5.1, 5.4, 5.6–5.7; game-unit extension is original reasoning.

**Support / contrary evidence:** Randomized contrast can help; it does not remove other validity conditions. **Applicability:** Actual independent units and predefined target populations. **Unresolved:** Is qualified statistical review needed for interference or sparse groups?

### C-12

**Claim:** Riot’s 2020 account treats audience-specific outlier detection as insufficient to determine every identity-preserving or game-health change.

**Class:** `practitioner-heuristic`. **Confidence:** moderate — Direct statement of limitations, but context-specific.

**Evidence and locator:** GDR-SRC-20261010-F07-005. “The Champion Balance Framework”, final two paragraphs; framework-adjustment sections.

**Support / contrary evidence:** Historical firsthand account; not independent effectiveness evidence. **Applicability:** One competitive-game case; no imported thresholds. **Unresolved:** How should the target game define its own audiences and constraints?

### C-13

**Claim:** Prefer a bounded, reversible change tied to the diagnosed mechanism and retest affected interactions; broader redesign can be appropriate when mechanisms interact.

**Class:** `hypothesis`. **Confidence:** low — Whole workflow has not been compared against alternatives.

**Evidence and locator:** No external source; explicitly identified original reasoning/proposal.. Proposed application process and option example.

**Support / contrary evidence:** An isolatable contrast aids interpretation; it may miss systemic interactions or slow urgent correction. **Applicability:** Tuning decisions with revisable rules and adequate safeguards. **Unresolved:** When does local tuning perform worse than a coordinated redesign?

### C-14

**Claim:** Evaluation should minimize unnecessary data and preserve consent, access, safety and explicit ethical constraints instead of optimizing a commercial proxy alone.

**Class:** `inference`. **Confidence:** moderate — Normative proposal with identifiable costs; no empirical efficacy guarantee.

**Evidence and locator:** No external source; explicitly identified original reasoning/proposal.. Cross-reference to the ethics topic; original evaluation-design requirements proposed here.

**Support / contrary evidence:** Risk management rationale, not approved studio policy or legal certification. **Applicability:** Any future player-facing data collection. **Unresolved:** Who authorizes data, exposure and harm thresholds?

### C-15

**Claim:** The illustrative aggregate-rate reversal shows that differing group composition can reverse a comparison.

**Class:** `inference`. **Confidence:** high — Direct arithmetic under explicit invented inputs.

**Evidence and locator:** No external source; explicitly identified original reasoning/proposal.. Invented table: A 64/100; B 62/100, with B higher within both stated groups.

**Support / contrary evidence:** Arithmetic only; neither randomization nor population representativeness is assumed. **Applicability:** Teaching conditional versus aggregated comparisons. **Unresolved:** What target mix and causal design would make a real comparison meaningful?

### C-16

**Claim:** The cost of additional evidence can exceed its decision value; an established rule violation need not await an unrelated enjoyment experiment.

**Class:** `inference`. **Confidence:** moderate — Decision-theoretic rationale; no project-specific cost calculation performed.

**Evidence and locator:** GDR-SRC-20261010-F07-003. “The Value of Information”; resource-duplication example is original and illustrative.

**Support / contrary evidence:** Narrow decision can already be resolved; implementation approval and regression checks remain. **Applicability:** Bounded corrective decisions, not unmeasured experience improvements. **Unresolved:** Does the proposed extra study have a plausible decision-changing result?

### C-17

**Claim:** Play duration should not be promoted to a validated wellbeing KPI on the basis of a single longitudinal study.

**Class:** `inference`. **Confidence:** high — Scope mismatch is explicit.

**Evidence and locator:** GDR-SRC-20261010-F07-012. §§2.3.1 and 4.1; substantive study interpretation is in the ethics topic.

**Support / contrary evidence:** Exposure, temporal lag and outcomes differ from a retention target. **Applicability:** Proxy-selection warning, not a clinical conclusion. **Unresolved:** Which construct and population would validate the proposed proxy?

### C-18

**Claim:** Language, assistance and input conditions should be recorded and evaluated when they can change the tested task.

**Class:** `hypothesis`. **Confidence:** moderate — Clear potential confounds; specific adaptations require direct testing.

**Evidence and locator:** No external source; explicitly identified original reasoning/proposal.. Proposed access/localization constraints and re-entry protocol.

**Support / contrary evidence:** Equivalent mechanics may not create equivalent demands; broad translation/access efficacy remains untested. **Applicability:** Representative evaluation planning, not certification. **Unresolved:** Do the task and measure retain meaning in each relevant condition?

## References

Source IDs are temporary F07 identities. Same-source aliases/DOIs are not additional independent evidence.

### GDR-SRC-20261010-F07-001

Stephanie Houde and Charles Hill. **What Do Prototypes Prototype?**. 1997. Elsevier; author chapter hosted by Stanford HCI. Handbook of Human-Computer Interaction, 2nd edition, chapter 16, pp. 367–381; reformatted 16-page copy. DOI: `10.1016/B978-044481862-1.50082-0`.

[Inspected source](https://hci.stanford.edu/courses/cs294h/2006/readings/houde-prototypes-97.pdf). Accessed 2026-10-10; access: `relevant-excerpt`. **Locators:** PDF pp. 1, 3–4; §§3.1–3.2; Figure 1 (PDF p. 3 visually inspected). **Type:** Practitioner/conceptual chapter. **Supports:** C-02. **Limits:** Interface-design examples; not an experiment demonstrating game-prototype efficacy. **Relationship:** Independent source identity; cross-batch deduplication pending. **Rights:** Copyrighted source; paraphrase only; no source pages redistributed.

### GDR-SRC-20261010-F07-002

Mike Ambinder, Valve. **Valve’s Approach to Playtesting: The Application of Empiricism**. 2009. Valve; GDC 2009 presentation. 68-slide deck.

[Inspected source](https://cdn.akamai.steamstatic.com/apps/valve/2009/GDC2009_ValvesApproachToPlaytesting.pdf). Accessed 2026-10-10; access: `relevant-excerpt`. **Locators:** PDF slides 5–6, 13–20, 24, 30–35, 39, 42; slides 16, 20 and 35 visually inspected. **Type:** Firsthand practitioner presentation. **Supports:** C-04, C-07. **Limits:** Deck distinguishes its fun-focused testing from balancing; simulated-number slides are not empirical datasets. **Relationship:** Independent source identity; cross-batch deduplication pending. **Rights:** Copyrighted source; paraphrase only; no source pages redistributed.

### GDR-SRC-20261010-F07-003

Daniël Lakens. **Sample Size Justification**. 2022-03-22. Collabra: Psychology / University of California Press. 8(1), 33267. DOI: `10.1525/collabra.33267`.

[Inspected source](https://online.ucpress.edu/collabra/article/8/1/33267/120491/Sample-Size-Justification). Accessed 2026-10-10; access: `relevant-excerpt`. **Locators:** “Six Approaches to Justify Sample Sizes”; “The Value of Information”; “Resource Constraints”; “A-priori Power Analysis”. **Type:** Methodological article. **Supports:** C-07, C-09, C-16. **Limits:** Sampling rationale, not a game-specific participant-count guarantee. **Relationship:** Independent source identity; cross-batch deduplication pending. **Rights:** Copyrighted source; paraphrase only; no source pages redistributed.

### GDR-SRC-20261010-F07-004

Pavel Dmitriev, Somit Gupta, Dong Woo Kim and Garnet Vaz. **A Dirty Dozen: Twelve Common Metric Interpretation Pitfalls in Online Controlled Experiments**. 2017-08. ACM KDD; Microsoft Research author copy. KDD 2017, 10-page author PDF; website directory date is not publication date. DOI: `10.1145/3097983.3098024`.

[Inspected source](https://www.microsoft.com/en-us/research/wp-content/uploads/2020/08/2017-08-KDDMetricInterpretationPitfalls.pdf). Accessed 2026-10-10; access: `relevant-excerpt`. **Locators:** §4, PDF pp. 2–3; §§5.1–5.4, pp. 3–5; §§5.6–5.7, p. 6; pp. 3 and 6 visually inspected. **Type:** Firsthand industrial experimentation/methods paper. **Supports:** C-06, C-11. **Limits:** Web-product experience; transfer to game outcomes and multiplayer units requires justification. **Relationship:** Independent source identity; cross-batch deduplication pending. **Rights:** Copyrighted source; paraphrase only; no source pages redistributed.

### GDR-SRC-20261010-F07-005

Summoner’s Rift Team, Riot Games. **/dev: Balance Framework Update**. 2020-06-30. Riot Games. Historical 2020 framework; not asserted to be current policy.

[Inspected source](https://www.leagueoflegends.com/en-gb/news/dev/dev-balance-framework-update/). Accessed 2026-10-10; access: `relevant-excerpt`. **Locators:** “The Champion Balance Framework”; “Combating Power Creep”; “Overhauling Elite”; “Loosening Pro Play Thresholds”. **Type:** Firsthand developer account. **Supports:** C-12. **Limits:** Self-evaluation of one competitive game; neither independent outcome validation nor reusable numerical thresholds. **Relationship:** Independent source identity; cross-batch deduplication pending. **Rights:** Copyrighted source; paraphrase only; no source pages redistributed.

### GDR-SRC-20261010-F07-006

Grant Roberts, lead game designer. **Postmortem: E-Line Media and Upper One Games’ Never Alone**. 2015-02-19. Gamasutra, now Game Developer. Published postmortem; no game build inspected.

[Inspected source](https://www.gamedeveloper.com/audio/postmortem-e-line-media-and-upper-one-games-i-never-alone-i-). Accessed 2026-10-10; access: `relevant-excerpt`. **Locators:** “What Went Right”, §1 “Inclusive Development”; “What Went Wrong?”, §1 “We Should Have Done a Closed Beta”. **Type:** Firsthand production account. **Supports:** C-08. **Limits:** Retrospective attribution; not an independent community evaluation or controlled test of a beta process. **Relationship:** Independent source identity; cross-batch deduplication pending. **Rights:** Copyrighted source; paraphrase only; no source pages redistributed.

### GDR-SRC-20261010-F07-012

Matti Vuorre, Niklas Johannes, Kristoffer Magnusson and Andrew K. Przybylski. **Time spent playing video games is unlikely to impact well-being**. 2022-07-27. Royal Society Open Science. 9, 220411; author-hosted published PDF. DOI: `10.1098/rsos.220411`.

[Inspected source](https://vuorre.com/bibliography/files/3K5WXM3G/vuorre-etal_2022_time-spent-playing-video-games-is-unlike.pdf). Accessed 2026-10-10; access: `relevant-excerpt`. **Locators:** §§2.1–2.3.1, PDF pp. 2–5; §2.4, p. 6; §3.1, pp. 7–8; attrition, pp. 9–10; §4.1, p. 11. Text inspected; Figure 4 screenshot requests failed; numerical interval is also in body text.. **Type:** Empirical longitudinal observational study. **Supports:** C-17. **Limits:** Selective adult response/attrition, seven titles, two-week lag and causal assumptions; no mechanics-specific safety guarantee. **Relationship:** Independent data/authors from S013; different exposure and estimand, not a direct replication. **Rights:** CC BY 4.0; paraphrase only.

## Open questions and change history

Coverage is bounded, not exhaustive. Prototype choice, mixed-method diagnosis, sampling rationale, instrumentation pitfalls and contextual balancing received direct source coverage. Cluster/network experiments, validated multilingual experience instruments, qualitative-method comparisons, automated balancing and longitudinal economy dynamics did not receive full specialist treatment. No participant evidence from this studio is available.

The review packet records unresolved cases `F07-CON-01`, `F07-CON-02` and `F07-CON-03`, missing dependencies and child-work questions. Those are batch-local labels, not global contradiction allocations. The source text for Vuorre was inspectable, but attempts to render its figures failed; this entry makes no image-derived claim.

**History:** 2026-10-10 — initial-capture-1, version 0.1.0 draft. No predecessor or supersession is asserted. Exact byte hash is recorded in the review packet and integrity receipt. Author self-review is documented in the packet; independent review, actual host retrieval tests and release remain pending.

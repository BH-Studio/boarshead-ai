---
id: GDR-CAND-20261010-F03-TOP-01
kind: topic
title: Progression and rewards
version: 0.1.0
status: draft
candidate_revision: initial-research-1
run_id: GDR-FULL-20261010
batch_id: F03
generation_attempt: F03-attempt-01
owner_project: BH-GDR-Foundations-and-Systems
updated: '2026-10-10'
evidence_checked: '2026-10-10'
input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate plus explicit F03 dispatch and
  inspected first-wave reviewed-candidate archive
aliases:
- unlocks
- character growth
- reward pacing
- mastery versus progression
- reward fatigue
tags:
- progression
- incentives
- learning
- autonomy
- pacing
- accessibility
related_topics:
- GDR-CAND-20261010-F03-TOP-02
- GDR-CAND-20261010-F01-TOP-02
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-F03-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-F03-001
- GDR-SRC-20261010-F03-002
- GDR-SRC-20261010-F03-003
- GDR-SRC-20261010-F03-004
- GDR-SRC-20261010-F03-005
- GDR-SRC-20261010-F03-008
- GDR-SRC-20261010-F03-009
- GDR-SRC-20261010-F03-010
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial F03 bounded research draft; author self-review integrated
  before first submission.
hash_record: ../reviews/full-run-20261010-f03-integrity.md
coverage_status: bounded-research-with-open-gaps
---

# Progression and rewards

**Draft research, not released guidance.** This entry is genre-neutral. The accompanying [review packet](../reviews/full-run-20261010-f03-review-packet.md) records the exact input snapshot, inspected shared corrections, missing F02 dependencies, source limitations and review state. No player tests, prototypes, simulations or live changes were performed.

## Decision and scope

The decision is **what should change through play, why a player would value that change, and which costs are acceptable**. Do not begin by selecting an experience-point curve. First distinguish the outcome that the progression system represents from the activity and evidence needed to achieve it. The following are working design distinctions, not a formal standard or an approved universal taxonomy. [C-01]

| Dimension | What changes | What possession or completion does not prove |
|---|---|---|
| Learned capability | The player can interpret or act effectively in an appropriate changed situation | A saved level, number of repetitions or purchase alone does not establish learning |
| Unlock / entitlement | A rule permits an action, region, tool or content previously unavailable | Being allowed to use it does not establish understanding, access usability or preference |
| Numerical character growth | Statistics, capacity, resistance or efficiency change | Winning after a power increase does not isolate improved player skill |
| Expressive or content progression | Available appearances, authored material, relationships or arrangements expand | An unlock is not necessarily valued, and a cosmetic reward is not automatically intrinsically motivating |
| Recognition / status | A representation of achievement or membership changes | Public recognition does not prove fair comparisons across conditions |

Here, a **reward** is a designed consequence offered as something potentially valuable; whether a person values it is an empirical question. **Intrinsic motivation** concerns satisfaction in the activity itself; extrinsic motivation concerns a separable outcome. The same object can be sought for different reasons. This is not a classification of objects into “good cosmetics” and “bad power.” A willingly endorsed external goal need not be experienced as a controlling demand. [C-01; C-02; GDR-SRC-20261010-F03-001]

This topic owns unlock structure, growth, reward horizons, incentives, assistance relationships and reward fatigue. [Economies and resources](economies-and-resources.md) owns quantities, transformation, scarcity and circulation. Decision quality and challenge/failure belong to F02; its actual research bytes and review were not retrieved. Spatial gate composition belongs to Worlds and Characters; communication and access presentation belong to Presentation and Interaction. No genre rule or implementation architecture is established here.

## Core explanation and mechanisms

### Rewarded output and desired experience are different outcomes

Deci, Koestner and Ryan report that several expected tangible-reward contingencies reduced subsequent free-choice engagement; their discussion distinguishes contingencies, feedback context and measurement. That is evidence against a context-free rule about all rewards, not proof that every game unlock undermines enjoyment. [C-02; GDR-SRC-20261010-F03-001]

Cerasoli, Nicklin and Ford examine performance across educational, work and physical contexts. Their synthesis distinguishes quality and quantity and considers intrinsic motivation alongside incentives. Its performance findings do not measure the same outcome as post-reward interest. These sources should not be flattened into contradictory slogans, nor combined into a universal reward schedule. [C-03; GDR-SRC-20261010-F03-002]

**Evidence-to-application bridge:** a task count can rise while the reason to act or the quality of action changes differently. Therefore, write separate intended outcomes—for example, noticing an important relation, enjoying an optional collection, or completing a chosen project—and inspect whether the qualifying action actually exercises them. A quota for ten easy actions could favor repeating the easiest eligible action; that possibility follows from the rule and does not demonstrate that actual players will choose it. [C-04; C-15]

An achievement can be useful information about an accomplishment, a desired external goal, a social signal, or a demand. Replacing a power reward with a badge does not by itself settle which interpretation applies. Conversely, removing every explicit reward can remove a valued structure. The proposed comparison is between specific meanings and opportunities, not “extrinsic versus intrinsic game objects.” [C-01; C-04; C-08]

### Progression must identify the state it changes

Record whether progress belongs to a run, character, account, shared group or the player's learned knowledge. Then specify what persists after leaving, failing, changing equipment, receiving help, switching accounts, respecializing or updating the rules. A state record that says “unlocked” cannot also be treated as proof of what the player knows. [C-01; C-12]

Staging abilities may reduce the number of decisions initially exposed, but it may also prevent an experienced player from reaching the interesting activity. Statistical growth may provide a valued sense of increased capability while masking unresolved comprehension. Horizontal options may broaden expression while increasing authoring and comparison burdens. These are competing proposed mechanisms, not findings that one structure is generally superior. [C-08]

A useful growth specification names the **new decision opportunity**: “can redirect a route,” “can sustain another operation,” or “can choose another visible identity.” “Gain a level” alone describes bookkeeping. If the intended payoff is simply the pleasure of accumulation, say so rather than mislabeling it mastery; that preference remains something to investigate. [C-01; C-08]

### Pacing involves opportunities, not only reward frequency

Use immediate, session and long horizons as questions: what is understood now, what can conclude at a chosen stopping point, and what remains worth returning to? They are neither required layers nor prescribed durations. In particular, carrying forward a voluntary project differs from threatening previously earned value at a calendar deadline. [C-09; C-11]

Inspect both the earning path and the period after acquisition. A tool unlocked immediately before it becomes irrelevant may have little opportunity to matter; a demanding unlock with many uses may justify more preparation. That is an opportunity-cost argument, not evidence for a fixed ratio of earning time to use time. A design without persistent progression can instead deliver complete, repeatable experiences. [C-08; C-09]

Separate a preview that supports planning from a reward advertisement that interrupts an activity. Show enough about requirements and consequences to permit an informed commitment; avoid making a spoiler-heavy catalog the only route to understand a material cost. These are proposed presentation requirements to coordinate, not specifications for colors, sizes or notification frequencies. [C-11; C-12]

### Reward fatigue requires competing explanations

For this entry, **reward fatigue** is a working label for a reported decline in a reward's value or welcome, including saturation, repetitive acquisition burden or attention overload. It is not a clinical construct, a dopamine claim, or simply a decline in play time. Someone who completes a satisfying goal and leaves has not necessarily experienced a design failure. [C-10]

Frommel and Mandryk's guided-recall survey analyzed 178 adults aged 19–66, recruited through a gaming/engagement-reward prescreen on Mechanical Turk. Accounts included enjoyment and facilitation as well as missing-out frustration and obligation. The authors identify recall, question framing, initial single-coder interpretation and cross-sectional causality limits. These are player reports, not verified hidden developer intent or a longitudinal estimate of fatigue. [C-07; GDR-SRC-20261010-F03-009]

The next design question depends on the diagnosis. A duplicate reward without a valued use suggests saturation; a valued reward behind an unwanted task suggests acquisition burden; an intrusive celebration suggests communication burden; rapidly rising costs suggest an economy problem; an easy task may indicate mastery or boredom. More frequent prizes would not logically solve all of these. Some players may actively prefer a familiar routine. [C-10]

## Design choices and alternatives

All option recommendations in this section are **hypotheses**. The right comparison depends on the declared outcome and local constraints. [C-08–C-11]

| Choice | Conditional purpose and mechanism to test | Cost, countercase and simpler alternative |
|---|---|---|
| Stage a new capability | Expose a rule when it has a useful opportunity; distinguish permission from understanding | Extra gate states, content sequencing and recovery paths. Offer a practice route, early access or all tools from the start when withholding is unnecessary |
| Increase numerical capacity | Let a character overcome an earlier limitation or express accumulated effort | Can invalidate earlier content, widen multiplayer power gaps or obscure learning. Optional difficulty or a different challenge composition may address access more directly |
| Offer horizontal alternatives | Let players adapt a method without requiring all options | More interactions to explain and balance; a supposedly optional option may become practically mandatory. Fewer differentiated tools or reversible selection can be preferable |
| Reward expression or content | Support collection, authorship or discovery without requiring raw power growth | Cosmetics can still carry scarcity pressure or social status. Direct access, authored discovery or no reward layer may fit better |
| Use explicit milestones | Help a player understand what a chosen project requires | A conspicuous counter can turn activity into quota completion. Compare discreet history, player-pinned goals and no automatic tracker |
| Mix random drops with an assured route | Preserve possible surprise while limiting unlucky non-acquisition for a defined target | The assurance can become a visible grind; fixed selection without randomness is simpler. Use PAT-01 only when both surprise and predictable access are wanted |
| Use scheduled / expiring opportunities | Coordinate an intentionally shared event or a meaningful temporary context | Availability constraints can create pressure. Compare recurring access, accumulated personal progress and no forfeiture of earned value; disclose unavoidable event boundaries |
| Omit persistent progression | Keep each experience self-contained, emphasize existing skill or avoid permanent advantage | Some audiences may miss collection or long projects. Test that loss instead of assuming every game needs a progression economy |

### Assistance and recognition

Do not make a player grind for the ability to access instructions, needed information or an appropriate input route. A difficulty assist can change performance without changing understanding, and an instructional prompt can guide an answer without showing transfer. Keep these separate from permanent-stat growth and optional recognition. This is a proposed access guardrail, not a claim that every difficulty configuration must have identical competitive certification. A genuinely comparable performance category needs a declared scope and separate approval. [C-12]

The inspected F01 correction uses changed cases with affordable, unaffordable and exact-availability outcomes; it asks what the rule permits, separately from what the player chooses. F03 preserves that discrimination and retains necessary access supports. P01's corrected numerical guidance is not imported as universal native-game thresholds; units, conformance scope and exceptions belong with the relevant presentation source. [C-12]

### Production, ethics and localization

An unlock graph creates a testing obligation at prerequisites, save boundaries, altered builds, multiplayer joins and abandoned goals. More reward objects also require names, differentiated uses, translations, comparison explanations, inventory support and maintenance. Estimate these obligations before promising a frequent content cadence; multiplying nearly interchangeable items is not a demonstrated remedy for fatigue. [C-09; C-15]

Compare understandable refusal and return with the offered reward. A balanced earn/spend rate can coexist with an inconvenient mandatory daily task or a punitive loss of accumulated value. Valve advises against artificial progress barriers, opaque currencies and narrow metric-driven extraction; this is practitioner guidance, not a measured F03 wellbeing effect. [C-11; GDR-SRC-20261010-F03-005]

For localization, distinguish a fictional title of “master” from a verified skill assessment, and check what completion, reservation, expiry and reclamation mean in the actual rule. Do not rely on idioms, one sensory modality, rapid reading or mental arithmetic as the only way to understand a requirement. Proposed alternate quantity views and explanation routes need representative review, not an assumed translation-equivalence claim. [C-12; C-16]

## Application process

1. **Specify the decision and outcome.** State what changes, who should value it and the evidence needed. Separate enjoyment, access, optional challenge, output and learning. Include a no-progression alternative. [C-01; C-04]
2. **Map the prerequisite and persistence states.** Describe earning, pending settlement, ownership, selection, use, abandonment, reset, assistance and version changes. Identify where an unlock might be mistaken for mastery. [C-01; C-12]
3. **Choose the smallest useful structure.** Compare at least one materially simpler alternative. Describe the next decision enabled by each milestone and its opportunity to matter; no generic XP formula is selected. [C-08; C-09]
4. **Challenge the incentive.** Ask how a player could earn the reward without doing the intended activity; who must undertake unwanted work; and whether an inventive shortcut is desirable. Inspect scarce inputs in the economy topic. [C-11; C-15]
5. **Describe a falsifiable comparison.** Choose a prototype question, participant context, competing explanation and practical decision criterion before collecting data. Assess refusal and stopping as valid choices. [C-04; C-16]
6. **Revise or remove.** A change that increases completions but harms the intended experience does not meet the specification. Inconclusive evidence warrants a narrower claim, not automatic adoption. Stop when the progression layer creates more burden than a direct route solves. [C-04; C-16]

These are proposed steps only; F03 did not build or test the design.

## Patterns and genre adaptations

[Guaranteed acquisition alongside random drops](../patterns/guaranteed-acquisition-alongside-random-drops.md), `GDR-CAND-20261010-F03-PAT-01`, isolates a finite qualifying-completion claim from the untested experiential benefit. [C-13; C-14]

Genre-specific expectations remain outside this topic. Relevant adaptation dimensions include finite versus persistent sessions, voluntary collecting versus required capability, shared competitive state versus private growth, and fixed versus changing content. A hybrid can prioritize discovery while also needing dependable access; keep the conflict explicit rather than choosing a genre label to override it. No genre file is created or silently treated as inspected here. [C-08; C-11]

Additional justified techniques are queued, not discarded, in the packet: absence-tolerant reward horizons and recovery floors require separate child registration and deeper evidence.

## Examples and counterexamples

### Inspected creator documents, not gameplay observation

ArenaNet's Mastery article describes account-wide ability unlocks rather than another increasing base-stat level ceiling. It supplies an example of a different progression object, not evidence that its name denotes demonstrated skill. Supergiant's FAQ supplies a contrasting description in which permanent growth and optional assistance coexist. No current build was played or success attributed to either design. [C-05; C-06; GDR-SRC-20261010-F03-004; GDR-SRC-20261010-F03-010]

Warframe's PC 32.2.0 notes document guaranteed Lua Thrax Plasm alongside rotation rewards, with both crafting uses and a vendor exchange. This motivates inspecting a mixed acquisition route; it does not establish a maximum time to craft a complete item. [C-14; GDR-SRC-20261010-F03-008]

### Illustrative: learning, unlocking and growth diverge

An invented system has three stations and a switch that redirects one unit of power. A player can complete the initial arrangement by following an answer-leading prompt. The proposed upgrade either (A) doubles supplied power, (B) unlocks a second switch, or (C) changes no capability but records completion. These are three different interventions. A later successful arrangement cannot isolate learning when both power and topology changed. [C-01; C-16]

For a proposed comprehension check, hold power fixed and vary which route receives it. Include cases where the target station is powered, unpowered and exactly at its requirement. Ask for a prediction of the result; then separately invite a preferred action. Reverse order and values in later probes so copying “always add power” is insufficient. Keep ordinary route information and needed access options. Even successful predictions may reflect guessing, remembered layouts or interface cues; the probes are not validated assessments and no one completed them here. [C-12; C-16]

**Counterexample:** if the intended experience is effortless construction and expressive arrangement, demanding a transfer test to unlock decorative pieces optimizes the wrong outcome. Direct access can be better than a pedagogical progression layer. [C-08; C-12]

### Illustrative: a guarantee can still be an unwanted task

A player needs one tool token and has two choices: a random reward from a qualifying activity or persistent credits that eventually purchase it. A completion-count bound may remove one uncertainty, but it does not prove that the activity is enjoyable, accessible or compatible with leaving. Another player may value spontaneous discoveries and dislike a visible progress counter. Compare a direct choice, not only an unbounded-random baseline, before concluding that the combined design adds value. The arithmetic and all assumptions appear in PAT-01. [C-10; C-13; C-16]

## Failure modes and constraints

| Warning sign to investigate | Competing cause | Candidate correction / exit |
|---|---|---|
| Many rewards, little reported value | Duplicate utility, saturation, poor differentiation or irrelevant notifications | Reduce clutter, offer a meaningful selection, or remove redundant reward states rather than increasing frequency [C-10] |
| Completion rises but changed-case predictions do not improve | Rewarded repetition or additional character power rather than learning | Redesign the qualifying activity or stop calling the outcome mastery [C-04; C-12] |
| Reward access becomes a requirement for playing together | Numerical disparity, late-arrival gate or shared expectation | Test normalization, separate challenge categories or access catch-up; each changes the intended stakes [C-08; C-11] |
| “Optional” rewards are pursued despite wanting to stop | Unique expiring access, threatened investment or social costs | Inspect actual refusal and return; remove the loss mechanism or provide later access where compatible with the promise [C-11] |
| New ability is confusing after a long absence | Missing recap, changed rule or prerequisite gap | Provide current state and on-demand help; do not automatically repeat the entire unlock grind [C-09; C-12] |
| A guarantee is bypassed by currency spending or expiry | Wrong unit or scope in the assurance | Narrow the promise, protect chosen progress where appropriate, or use direct reward selection [C-13] |

The warnings are proposed hypotheses, not observations of a shipped game. Child-specific policy, multinational calendar expectations, accessibility equivalence and long-term reward saturation remain insufficiently researched here. [C-10; C-11; C-16]

## Playtest and validation

**All tests below are proposed and not performed.** No sample-size guarantee, approved recruitment or predefined numeric acceptance threshold is asserted. The project would first choose a smallest worthwhile benefit, tolerable burden and uncertainty requirements suitable for its actual audience. [C-16]

**Learning versus entitlement.** Compare early access with staged access to one capability. Hold task opportunity, base power and relevant information constant as far as the question allows. Include newcomers, returning players and experienced players; preserve needed access accommodations. Measure changed-case prediction, relevant action, optional help, perceived agency and explanation quality separately. Counterbalance cases and assess after an appropriate return interval. Confounds include novelty, arithmetic/reading demands, previous genre knowledge and unequal practice. Reject the learning claim when acquisition or completion improves without discriminating capability evidence; that result need not reject a separately valued access or collection outcome. [C-04; C-12]

**Acquisition versus reward salience.** Compare direct choice, fixed guaranteed progress and mixed random/guaranteed acquisition using the same target utility. Separate outcome-distribution comparisons from interface-salience comparisons; changing both cannot isolate a counter's effect. Record understanding of the bound, unwanted repetition, valid decisions to stop, and later use of the acquired tool. A completion increase alone is insufficient. Reject or simplify the mixed mechanism when it adds pressure or misleads about access without a practically useful benefit. [C-11; C-13]

**Fatigue and horizon.** A future repeated-session study could compare non-expiring personal progress with an otherwise similar recurring opportunity. Do not create real loss or payment pressure simply to test it. Use voluntary simulated stakes and explicit consent where applicable; acknowledge that these differ from a persistent live economy. Measure reported value, burden, chosen activity and reasons for missed sessions at multiple points. Attrition, content familiarity, changing life availability and reward utility are competing explanations, not missing-data nuisances to hide. Reconsider the intervention when a benefit disappears after novelty, burden rises, or those unable to attend are systematically excluded. [C-07; C-10; C-11]

## Claim ledger

| Claim | Exact claim / classification | Support and precise locator | Applicability, uncertainty and next question |
|---|---|---|---|
| C-01 | Separate learned capability, entitlement, numerical growth and expression when diagnosing progression. **inference**. | Working definitions in Decision and scope; contrast with developer labels in 004 and 010. | High confidence in the logical distinction, not a validated taxonomy. Does the proposed outcome actually require a persistent progression system? |
| C-02 | Effects on post-reward interest depend on reward contingency and context; the inspected synthesis does not warrant a blanket claim that rewards always help or always harm. **empirical-evidence**. | 001, printed pp. 629 and 656–658. | Moderate: experimental synthesis, but outcome/task/population variation and no direct F03 gameplay intervention. Which feature and outcome match a studied condition? |
| C-03 | Intrinsic motivation and incentives have different relationships with performance quality and quantity in the inspected synthesis. **empirical-evidence**. | 002, Method; Table 4 and Discussion, PDF pp. 7–9 and 17–18. | Moderate for reported associations; not a causal estimate for game progression or a schedule prescription. Underlying incentive estimates are partly derivative. |
| C-04 | Measure desired learning/experience separately from rewarded output before choosing an incentive. **inference**. | Bridge from C-01–C-03; F07 evaluation candidate §§Measurement is not the experience itself / Balance has multiple objectives. | Moderate reasoning; no proof this workflow improves every game. A goal of pleasurable repetition may not require a learning outcome. F03-CON-01 retains outcome distinctions. |
| C-05 | ArenaNet describes account-wide ability progression in its historical Mastery announcement. **observed-example** of a document. | 004, What Are Masteries? / How Do I Get Masteries? / What Can I Get From Masteries? | High for the inspected wording, narrow and historical. It does not verify player mastery or today’s build. |
| C-06 | Supergiant describes permanent progression alongside optional difficulty and God Mode. **observed-example** of a document. | 010, difficulty FAQ answer. | High for the described arrangement only. No assistance magnitude, access equivalence or causal learning effect established. |
| C-07 | The engagement-reward survey contains valued and burdensome experiences; it does not establish causal or longitudinal fatigue effects. **empirical-evidence**. | 009, §§3.1–3.4, 4.1.1–4.1.4 and 5.3; pp. 226:7–11 and 226:17–18. | Moderate for accounts in its selected adult sample. Recall, prompting, coding and selection limit prevalence/causal claims. Nonparticipants and children remain missing. |
| C-08 | Choose unlocks, statistical growth, expressive rewards or no progression according to the intended decision change, not a default ladder. **hypothesis**. | Candidate option comparison below, informed by C-01, C-05 and C-06; not validated by those examples. | Low causal confidence. Compare options at matched opportunity and report who loses access or valued structure. |
| C-09 | Plan pacing around useful opportunities and stopping points; short, session and long horizons are optional inspection windows, not mandatory layers. **hypothesis**. | Original application proposal; inspected F01 core-loop candidate §Short, session and long horizons. | Low benefit confidence. Durable content, mastery plateaus and desired routine could justify different pacing. No universal durations or XP curve supported. |
| C-10 | Treat reward fatigue as a diagnosis with competing explanations, not an automatic demand for more rewards. **hypothesis**. | Operational definition and proposed discriminating comparisons; C-07 supplies reports, not a longitudinal mechanism. | Low causal confidence. Content exhaustion, changed availability, inflation and satisfying completion may resemble fatigue. |
| C-11 | Inspect refusal, absence and return costs even when reward flow is numerically balanced. **hypothesis**. | Original ethical risk audit; 005, Considerations; 009 §5.3; inspected F07 ethics §§Audit both what is offered and how refusal works / Wellbeing evidence. | Low for prevention efficacy; no inference of developer intent or legal/clinical status. Valuable voluntary routines are a countercase. |
| C-12 | An unlock, chosen purchase or assisted success is insufficient evidence of transferable understanding; never remove required access supports because an instructional check was passed. **inference**. | F01-PAT-01 corrected Worked examples and Recipe; selected correction hash in review packet. P01 corrected scope receipt and selected accessibility passages. | High for invalid-inference warning; low for efficacy of any proposed check. Discriminating probes remain unvalidated and ordinary information remains available. |
| C-13 | A persistent guaranteed credit route can bound remaining qualifying completions under explicit assumptions; it does not bound time, effort or full-item acquisition. **inference**. | Original arithmetic in PAT-01 C-03; no stochastic simulation or player test. | High for arithmetic conditional on constant price/minimum grant, no loss/spending and accessible redemption; low for expected experience benefit. |
| C-14 | The historical Warframe notes describe both rotation rewards and guaranteed resource earnings with a vendor exchange route. **observed-example** of a document. | 008, Rotation Rewards / New Resource: Lua Thrax Plasm. | High for documented configuration; no complete-item time guarantee or player-benefit evidence. |
| C-15 | Reward criteria may redirect behavior away from the intended activity; audit easiest qualifying actions, collaboration and support burden. **hypothesis**. | Reasoning from an invented output-target example and C-02–C-04; no measured F03 exploit incidence. | Low for frequency or size of effects. Emergent methods may be valuable play rather than defects. |
| C-16 | The examples and comparison plans can discriminate some proposed explanations but do not constitute validated assessments or results. **inference**. | Explicit illustrative examples and proposed protocols below; F07 methodological limits. | High that these tests were not performed; usefulness remains untested. Approval, sampling and implementation are future decisions. |

## References

Source IDs below are temporary run-scoped candidates. Dates of access are not publication dates. Shared candidate material is documented separately in the review packet and is not counted as independent public corroboration. The Mekler article remains an abstract-only lead; no body result is adopted.

### GDR-SRC-20261010-F03-001 — A Meta-Analytic Review of Experiments Examining the Effects of Extrinsic Rewards on Intrinsic Motivation

**Citation:** Edward L. Deci, Richard Koestner, and Richard M. Ryan. 1999-11. *A Meta-Analytic Review of Experiments Examining the Effects of Extrinsic Rewards on Intrinsic Motivation*. American Psychological Association; Psychological Bulletin 125(6), 627–668.

**Verified route:** [A Meta-Analytic Review of Experiments Examining the Effects of Extrinsic Rewards on Intrinsic Motivation](https://selfdeterminationtheory.org/wp-content/uploads/2014/04/1999_DeciKoestnerRyan_Meta.pdf). DOI: `10.1037/0033-2909.125.6.627`.

**Version / access:** Published 1999 article; author-institute hosted PDF, 42 pages. Checked 2026-10-10; `access: relevant-excerpt`. Research synthesis of experiments; empirical evidence is secondary to the underlying experiments, not a new game trial.

**Inspected locators:** Printed pp. 629 and 656–658 (PDF pages 3 and 30–32): interpersonal context, General Discussion, reward-contingency and measurement qualifications; pages visually inspected.

**Claims in this artifact:** C-01, C-02; conditional bridge C-04.

**Limits / independence:** Post-reward free-choice behavior and self-reported interest are not long-term gameplay mastery or wellbeing. Underlying experiments were not individually re-reviewed. Related motivational tradition to 002 and 009; not three independent tests of the proposed pattern.

**Rights:** APA copyright; paraphrase only. No PDF or images redistributed.



### GDR-SRC-20261010-F03-002 — Intrinsic Motivation and Extrinsic Incentives Jointly Predict Performance: A 40-Year Meta-Analysis

**Citation:** Christopher P. Cerasoli, Jessica M. Nicklin, and Michael T. Ford. 2014-07. *Intrinsic Motivation and Extrinsic Incentives Jointly Predict Performance: A 40-Year Meta-Analysis*. American Psychological Association; Psychological Bulletin 140(4), 980–1008.

**Verified route:** [Intrinsic Motivation and Extrinsic Incentives Jointly Predict Performance: A 40-Year Meta-Analysis](https://selfdeterminationtheory.org/wp-content/uploads/2017/06/2014_Cerasoli_Intrinsic.pdf). DOI: `10.1037/a0035661`.

**Version / access:** Advance-online-layout copy of the 2014 article; 30 PDF pages including cover. Checked 2026-10-10; `access: relevant-excerpt`. Meta-analysis and meta-analytic performance prediction; not a game progression experiment.

**Inspected locators:** Method/Literature Search, PDF pages 7–9; Results and Table 4, PDF page 17 (printed manuscript p. 16, visually inspected); Discussion, PDF page 18; limitations, PDF pages 22–23.

**Claims in this artifact:** C-03; conditional bridge C-04.

**Limits / independence:** School, work and physical-performance settings do not establish a game reward schedule. Joint models draw in part on earlier incentive estimates, including Jenkins et al.; that underlying work was not separately inspected. Performance and interest are different outcomes from 001.

**Rights:** APA copyright; paraphrase only; hosted PDF not redistributed.



### GDR-SRC-20261010-F03-003 — Towards understanding the effects of individual gamification elements on intrinsic motivation and performance

**Citation:** Elisa D. Mekler, Florian Brühlmann, Alexandre N. Tuch, and Klaus Opwis. 2017-06. *Towards understanding the effects of individual gamification elements on intrinsic motivation and performance*. Elsevier; Computers in Human Behavior 71, 525–534.

**Verified route:** [Towards understanding the effects of individual gamification elements on intrinsic motivation and performance](https://www.sciencedirect.com/science/article/abs/pii/S0747563215301229). DOI: `10.1016/j.chb.2015.08.048`.

**Version / access:** Published article metadata/abstract; full methods and results not retrieved. Checked 2026-10-10; `access: abstract-only`. Lead to controlled gamification research; NOT inspected support for F03 findings.

**Inspected locators:** Publisher abstract and University of Basel publication record only; no body locator claimed.

**Claims in this artifact:** None; unresolved controlled-study lead only.

**Limits / independence:** No substantive F03 claim relies on its abstract. University record: https://edoc.unibas.ch/entities/publication/ccec8ccc-aa54-417d-b205-334b518d6eed/full . Related theoretical background is not independent corroboration of 001 or 002.

**Rights:** Publisher copyright; no quotation or full text redistribution.



### GDR-SRC-20261010-F03-004 — Reimagining Progression: The Mastery System

**Citation:** ArenaNet. unknown. *Reimagining Progression: The Mastery System*. GuildWars2.com / ArenaNet.

**Verified route:** [Reimagining Progression: The Mastery System](https://www.guildwars2.com/en/news/reimagining-progression-the-mastery-system/).

**Version / access:** Historical Heart of Thorns prelaunch design announcement; publication date not exposed in inspected rendering. Checked 2026-10-10; `access: relevant-excerpt`. Firsthand developer design description; observed document, not hands-on game observation.

**Inspected locators:** Sections What Are Masteries?, How Do I Get Masteries?, What Can I Get From Masteries?, and Masteries Are Here to Stay.

**Claims in this artifact:** C-05; illustrative contrast informing C-01/C-08.

**Limits / independence:** Verifies what this announcement describes, not the current 2026 build or player learning. Commercial success is not used as causal evidence. No independent player study accompanies the account.

**Rights:** ArenaNet copyrighted article; paraphrase only; images not redistributed.



### GDR-SRC-20261010-F03-005 — Microtransactions (In-Game Purchases)

**Citation:** Valve. unknown. *Microtransactions (In-Game Purchases)*. Steamworks Documentation.

**Verified route:** [Microtransactions (In-Game Purchases)](https://partner.steamgames.com/doc/features/microtransactions).

**Version / access:** Mutable online documentation inspected on 2026-10-10; no edition/update date exposed. Checked 2026-10-10; `access: relevant-excerpt`. Platform-provider practitioner guidance; cited advice is not a universal formal standard.

**Inspected locators:** Anticipating Fraud; Considerations for in-game economies and best practices, especially items 1–2 and concluding metrics paragraph.

**Claims in this artifact:** C-11 as practitioner rationale, not proof of benefit.

**Limits / independence:** The selected recommendations supply no controlled outcome measurements. The linked Kyle Davis talk was not viewed. /documentation/MicroTxn is an access alias, not another independent source. Platform-specific numerical fraud restrictions are not generalized here.

**Rights:** Valve documentation; paraphrase only. No implied redistribution license or platform certification.



### GDR-SRC-20261010-F03-008 — Update 32.2.0: Lua’s Prey

**Citation:** Digital Extremes. 2022-11-30. *Update 32.2.0: Lua’s Prey*. Warframe official patch notes.

**Verified route:** [Update 32.2.0: Lua’s Prey](https://www.warframe.com/en/patch-notes/pc/32-2-0).

**Version / access:** PC Update 32.2.0; dated historical configuration. Checked 2026-10-10; `access: relevant-excerpt`. Official build-specific feature description; observed document, not reproduced gameplay.

**Inspected locators:** New Lua Nodes: Conjunction Survival → requirement, Rotation Rewards, New Resource: Lua Thrax Plasm; resource-use and Archimedean Yonta exchange paragraphs.

**Claims in this artifact:** C-14; structural lead for C-13.

**Limits / independence:** Documents one mixed acquisition arrangement, not the efficacy of F03-PAT-01. Crafting inputs and access prerequisites mean no general bound on full-item acquisition time follows. Vendor exchange is not player-to-player trade.

**Rights:** Digital Extremes copyright; paraphrase only; images not redistributed.



### GDR-SRC-20261010-F03-009 — Daily Quests or Daily Pests? The Benefits and Pitfalls of Engagement Rewards in Games

**Citation:** Julian Frommel and Regan L. Mandryk. 2022-10-25. *Daily Quests or Daily Pests? The Benefits and Pitfalls of Engagement Rewards in Games*. ACM; Proceedings of the ACM on Human-Computer Interaction 6 (CHI PLAY), Article 226, 23 pages.

**Verified route:** [Daily Quests or Daily Pests? The Benefits and Pitfalls of Engagement Rewards in Games](https://research-portal.uu.nl/en/publications/daily-quests-or-daily-pests-the-benefits-and-pitfalls-of-engageme/). DOI: `10.1145/3549489`.

**Version / access:** Published article text in author-uploaded ResearchGate copy, upload attributed to Julian Frommel on 2023-01-17; matched title/authors/DOI to institutional record. Checked 2026-10-10; `access: relevant-excerpt`. Primary cross-sectional mixed-methods survey with guided recall; self-reported player accounts, not observed gameplay or intervention.

**Inspected locators:** Article pp. 226:7–9, §§3.1–3.4; pp. 226:9–11, §§4.1.1–4.1.4; pp. 226:17–18, §5.3. Prose inspected; no numerical table results used.

**Claims in this artifact:** C-07; limitations relevant to C-10/C-11.

**Limits / independence:** Author-uploaded full-text route: https://www.researchgate.net/publication/365003534_Daily_Quests_or_Daily_Pests_The_Benefits_and_Pitfalls_of_Engagement_Rewards_in_Games . Institutional PDF returned 403 and publisher full-text route failed before this route succeeded. Recall, selected regular-player sample, prompting and initial single-coder interpretation limit generalization. No causal or longitudinal fatigue effect estimated here.

**Rights:** Copyright held by owner/authors; publication rights licensed to ACM. Paraphrase only; no participant quotations or full text redistributed.



### GDR-SRC-20261010-F03-010 — Hades FAQ

**Citation:** Supergiant Games. unknown. *Hades FAQ*. Supergiant Games.

**Verified route:** [Hades FAQ](https://www.supergiantgames.com/blog/hades-faq/).

**Version / access:** Evolving official FAQ; publication/update date and build not established in inspected rendering. Checked 2026-10-10; `access: relevant-excerpt`. Creator account of intended experience and described feature; observed document.

**Inspected locators:** Difficulty question and answer describing permanent progression, optional difficulty, and God Mode.

**Claims in this artifact:** C-06; contrast informing C-08/C-12.

**Limits / independence:** No hands-on reproduction, numerical assistance values, achievement behavior or evidence of learning equivalence is claimed. Not a causal study of assistance.

**Rights:** Supergiant Games copyright; paraphrase only.


## Open questions and change history

Open: actual F02 decision/difficulty candidates and reviews; controlled game-specific causal evidence for reward salience; full Mekler methods/results; longitudinal saturation; children and less frequent players; culturally and access-representative interpretation; multiplayer opportunity costs; live maintenance and retirement effects. These gaps do not erase the completed bounded research, but file existence does not certify exhaustive heading coverage.

`F03-CON-01` retains outcome/context differences between reward studies. `F03-CON-05` retains the conflict between predictable access and valued uncertainty. Author self-review narrowed the guarantee to qualifying completions, retained no-progression/direct-choice counterexamples and preserved the first-wave transfer correction. These are author revisions before initial submission, not an independent review or an approved design decision.

**History:** 2026-10-10, version 0.1.0, candidate_revision initial-research-1, first submitted F03 concept identity; predecessor and supersession null. Exact byte hash is in the integrity receipt. **Gate C pending independent review; Gate D host tests not run; Gate E not passed.**

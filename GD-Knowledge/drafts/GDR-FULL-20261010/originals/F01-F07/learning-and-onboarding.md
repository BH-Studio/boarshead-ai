---
id: GDR-CAND-20261010-F01-TOP-03
kind: topic
title: Learning and onboarding
version: 0.1.0
status: draft
id_scope: run-scoped-temporary
run_id: GDR-FULL-20261010
batch_id: F01
owner_project: BH-GDR-Foundations-and-Systems
updated: '2026-10-10'
evidence_checked: '2026-10-10'
input_snapshot: Available GD-Knowledge starter candidate; INDEX/REGISTERS 0.1.0, nine
  Project files; not a current canonical receipt
aliases:
- tutorials
- scaffolding
- discovery learning
- mental models
- learning transfer
- returning player
- re-entry after absence
tags:
- learning
- onboarding
- feedback
- transfer
- re-entry
- cognitive-access
- instruction
- discovery
related_topics:
- GDR-CAND-20261010-F01-TOP-01
- GDR-CAND-20261010-F01-TOP-02
related_patterns:
- GDR-CAND-20261010-F01-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-F01-10
- GDR-SRC-20261010-F01-11
- GDR-SRC-20261010-F01-12
- GDR-SRC-20261010-F01-13
- GDR-SRC-20261010-F01-14
reviewer: null
approved_by: null
approved_date: null
---

# Learning and onboarding

**Draft research candidate — not released guidance.** Identity `GDR-CAND-20261010-F01-TOP-03` is temporary for `GDR-FULL-20261010/F01`. This file authorizes no implementation or adoption. Review and approval fields are intentionally null.

## Decision and scope

**Decision:** What must a player understand or be able to do, when is support necessary, and how can a design distinguish temporary guided success from usable learning without spoiling desired discovery or removing access?

This topic covers first contact, learning a new rule later in play, revisiting an established skill and re-entry after absence. It includes explicit tutorials, observation, discovery, practice, scaffolding, mental models, feedback and transfer. It does not prescribe a tutorial length, mastery score, reading speed, clinical cognitive profile, difficulty curve or engine implementation. Visual hierarchy, captions, control mappings, assist presentation and sensory redundancy remain Presentation dependencies.

**Operational definitions.** *Onboarding* is support for entering meaningful participation; it includes more than a tutorial. *Learning* is a change in capability or understanding that can be demonstrated beyond an immediately supplied answer. *Scaffolding* is temporary instructional support for a particular learning demand. A *mental model* is the player's working explanation of what actions mean and how outcomes occur. *Transfer* means using what was learned in a changed situation; its distance from the original task must be specified. Repeating a highlighted input successfully is a performance observation, not sufficient evidence of durable understanding. [C-01; GDR-SRC-20261010-F01-13]

These are working definitions for decisions in this entry, not claims that every game requires explicit mastery assessment. The intended experience may value uncertainty, repetition, expression or interpretation rather than efficient acquisition of a designer-specified solution.

## Core explanation and mechanisms

### Tutorial benefit depends on what was taught, whom it reached and what was measured

Andersen and colleagues compared eight tutorial conditions across Refraction, Hello Worlds and Foldit, with over 45,000 players. They measured play time, levels completed and return, not a direct test of learned rules. Foldit showed benefits from some tutorial treatments; the other games did not show the same benefits. Complexity, game identity, audience and access friction were not independently randomized. [C-02; GDR-SRC-20261010-F01-10]

**Source discrepancy:** the paragraph on pooled help availability describes a Hello Worlds return-rate increase, whereas Table 3 shows help at 18.56% and no help at 19.78%. The table was visually inspected. F01 records the disagreement rather than adopting that contrast as evidence for either a general benefit or general harm of optional help. No erratum or raw-data adjudication was obtained. [C-03; GDR-SRC-20261010-F01-10]

The application bridge is conditional: diagnose whether a player lacks rule knowledge, input access, an understandable objective, willingness to participate, or an opportunity to experiment. A tutorial aimed at the wrong deficit may add interruption without helping. The study does not prove that simple games should have no accessibility support, or that blocking instruction can never teach. Its outcome measures cannot settle those questions. [C-02; C-08]

### Guidance should track the learning demand, not a fixed player label

Kalyuga and colleagues' expertise-reversal framework describes why instructional support useful with little relevant knowledge can become redundant with expertise. F01 inspected the authors' synthesis, not the full underlying experiment set. The game-design implication is a hypothesis: offer different support paths based on relevant knowledge and task demands rather than treating everyone as a permanent novice or expert. [C-04; GDR-SRC-20261010-F01-11]

A person may know the genre but not this game's rule, understand the rule but use an unfamiliar input device, or return after forgetting only one subsystem. A single completion event does not establish all those capabilities. Prefer player-selected support or a reversible local check over silently inferring competence from demographics, fast input or time already played. Automatic adaptation is an optional future design, not a requirement. [C-08; C-13]

### Discovery and explanation are alternatives with prerequisites, not opposing ideologies

Kapur and Bielaczyc's classroom study used initial problem generation followed by teacher-led consolidation. Its intact-class comparisons support a bounded case for that sequence, not leaving learners unaided indefinitely. Outcomes varied; the School C routine-item comparison did not reach significance. The setting was Grade 7 mathematics in three Singapore schools, with teacher, school and implementation confounds. [C-05; GDR-SRC-20261010-F01-12]

The proposed bridge to game learning is to distinguish **productive investigation** from **uninterpretable failure**. Investigation needs a question, relevant prior knowledge or discoverable evidence, interpretable consequences and an eventual way to consolidate the rule. When those prerequisites fail, an explicit example or direct instruction is a legitimate alternative. F01 does not establish which sequence is more enjoyable or efficient in a voluntary entertainment setting. [C-08; C-09]

This distinction matters when the hidden rule is the experience. Revealing a solution can improve immediate completion while destroying the intended discovery. In that context, teach prerequisite interaction and access, offer consent-based help, and leave the mystery intact. Reject a teaching technique that measures success by removing the intended activity. [C-08; C-15]

### Practice can reveal a model without proving that it will last

Karpicke and Roediger's experiment with 40 students learning vocabulary found that continued retrieval after initial success supported later recall more than merely continuing study under the tested conditions. Similar acquisition performance did not imply equivalent recall a week later. This was vocabulary memory, not motor skill, game engagement or the complete pattern proposed here. [C-06; GDR-SRC-20261010-F01-13]

The design inference is to ask players to use a rule without supplying the next answer and, where relevant, to revisit it later. Do not transplant the paper's effect size or interval into a game as a universal target. A transfer task adds a further untested step: it should change a meaningful condition so success is harder to explain as memorizing the original sequence. It must still assess the same intended rule rather than introduce unrelated novelty. [C-10; C-11]

### Feedback should resolve the relevant uncertainty

Proposed instructional feedback distinguishes an attempted action, the rule condition that affected it and the resulting state. “Wrong” can identify failure without explaining what to revise; “press this next” can yield completion without exposing the rule. Neither statement is always inappropriate: fast execution practice may need concise result feedback, while a rule misconception may need a causal explanation. The best form depends on the learning demand. F01 has no direct comparison establishing a superior feedback format. [C-09]

Where several causes could explain an outcome, give a way to discriminate them. A failed action might reflect a depleted resource, a timing condition, an inaccessible cue, another participant's action or a misunderstanding. Do not label all failures as lack of knowledge. Avoid revealing hidden opponent information or mystery solutions merely to make the feedback more explicit. [C-09; C-11; C-13]

### Re-entry is a new support decision, not automatically a full tutorial replay

XAG 109 recommends accessible ways to revisit objectives and relevant history, and to revisit tutorial material. Its framework explicitly describes best practices rather than legal/compliance requirements. It does not establish a causal re-entry benefit or prescribe the following protocol. [C-07; GDR-SRC-20261010-F01-14]

The F01 re-entry hypothesis is to reconstruct **the chosen intention, relevant current state, meaningful changes and a safe next action**. Offer a recap and optional practice of a rusty mechanic; do not presume that elapsed time means total forgetting. A recap must also distinguish player knowledge from newly revealed information. In a deduction scenario, recalling discovered facts is different from revealing an unearned answer. [C-12]

## Design choices and alternatives

| Approach | Prerequisites and reason to choose | Cost, failure signal and alternative |
|---|---|---|
| Direct explanation plus representative attempt | The player lacks a specific prerequisite or experimentation is expensive. [C-08; C-09] | Explanation may be redundant or abstract. Compare an example, player-requested help or a shorter prerequisite introduction. |
| Bounded discovery followed by consolidation | Testing explanations is desired; consequences are interpretable and recovery is acceptable. [C-05; C-08] | Unguided search can teach nothing or spoil pacing. Supply a model or stop the attempt when meaningful investigation is absent. |
| Contextual instruction at an actual need | The context helps make a rule interpretable and interruption cost is acceptable. [C-02; C-09] | Timing can interrupt action or spoil discovery. Preview, practice elsewhere or allow postponement instead. |
| Replayable help and player-selected practice | Needs vary, knowledge is uneven or players return after absence. [C-07; C-12] | Help can be hard to find or fail to match the current rule. Discoverability and accessible presentation require a Presentation review. |
| Taper instructional prompts after a changed-task check | There is a specific learned rule, a representative check and a reversible way to restore help. [C-10; C-11] | False competence inference or irrelevant testing can frustrate. Let players retain prompts or use a simpler explicit “continue without guidance” choice. |
| No explicit tutorial for the core discovery | Uncovering the rule is the intended experience and necessary interaction/access is already available. [C-08; C-15] | This is not permission to hide controls or deny accommodations. Provide access and opt-in assistance without revealing the solution. |

## Application process

1. **Define the actual learning target.** State what a player should predict, decide, interpret or execute. Identify which knowledge is intentionally withheld and which is necessary for access. Replace “understand combat” with a concrete relation or action capability. [C-01; C-11]
2. **Separate failure causes.** Ask whether the barrier is discovery of an action, understanding its rule, execution, remembering an objective, interpreting feedback or wanting a different outcome. Record assumptions when diagnosis is uncertain. [C-08; C-13]
3. **Choose support with a genuine alternative.** Select direct explanation, an example, bounded discovery, replayable help or no explicit tutorial according to purpose and risk. Specify an exit if the prerequisite diagnosis is wrong. [C-08; C-09]
4. **Prepare a representative attempt.** Preserve the actual state relation and input/access requirements, while removing unrelated losses when safe practice is appropriate. A special tutorial rule must not silently contradict the real rule. No prototype was created here. [C-09; C-11]
5. **Check use, not just acknowledgment.** Ask for a prediction or observe a decision that distinguishes plausible mental models. Offer nonverbal alternatives when verbal explanation adds an unrelated access or language burden. [C-10; C-11; C-13]
6. **Adjust only the support being assessed.** Taper answer-leading prompts when evidence and player preference justify it. Keep accommodations, ordinary state information, optional reference and a way back to practice. Restore support when a changed state exposes a misconception. [C-10; C-13]
7. **Design re-entry deliberately.** Preserve the information needed to reconstruct chosen goals and current constraints; do not mandate engine storage architecture. After meaningful change or absence, offer a relevant recap rather than replaying every lesson. [C-12; C-14]
8. **Evaluate and revise.** Compare immediate participation, later use and experience; simplify or remove support that provides no benefit or destroys the chosen discovery. [C-16]

## Patterns and genre adaptations

[Supported attempt and transfer check](../patterns/supported-attempt-and-transfer-check.md), `GDR-CAND-20261010-F01-PAT-01`, is the single pattern extracted from F01. It combines a representative attempt, a discriminating changed situation and reversible instructional support. Its whole causal chain is not established by the component research.

[Player experience and motivation](player-experience-and-motivation.md) determines what kind of learning, challenge or uncertainty is valued. [Core loops and interaction structure](core-loops-and-interaction-structure.md) identifies the rule relationships to learn.

Detailed accessibility, controls and feedback presentation remain unavailable Presentation dependencies. Difficulty and evaluation method topics are also not supplied. Genre-specific custom guidance is not embedded here; `templates/genre.md` and relevant genre files are missing. Synthetic contexts below are transfer probes, not canonical genre recommendations.

## Examples and counterexamples

### Illustrative worked example: learning a simultaneous-resolution rule

In an invented planning activity, the player commits two actions before either resolves. One action creates a resource; the other consumes it. The rule says costs are checked when actions are committed, not after resolution. A player expecting sequential resolution may repeatedly submit an impossible plan. The intended learning is the timing of the cost check, not merely the location of a button. [C-11; C-15]

Provide an example contrasting a valid plan with an invalid one and state the relevant timing rule. Let the player attempt another plan in a reversible context. Feedback identifies whether the resource was present **at commitment**. Then change the resource-producing action and ordering so copying the example does not settle the new case. Ask for a prediction before commitment or observe whether the player deliberately obtains the resource first. [C-09; C-10; C-11]

A successful guided submission is insufficient: the player may simply follow highlighting. A failed changed case is also not automatically a conceptual failure: the feedback may be inaccessible or the terminology may imply sequence. Keep support available, investigate the cause and revise the explanation or rule before increasing repetition. No learner performed this exercise in F01. [C-10; C-13; C-15]

### Illustrative worked example: return to a shared project

A returning player previously intended to finish a shared construction. During absence, a teammate completed the foundation and spent some stored material. Replaying movement instruction does not address the immediate uncertainty. A relevant recap distinguishes the previous intention, completed work, current material and the next actions still available. [C-12; C-15]

Offer a practice activity only for a mechanic the player chooses to revisit or demonstrably needs help with. A misleading recap that claims the previous task remains open can create a false mental model. A recap that reveals an undiscovered plot outcome can destroy intended uncertainty. Presenting all changes at once may create its own comprehension cost. Compare a concise goal-linked recap, optional detailed history and no automatic recap while retaining access to reference information. [C-12; C-14; C-16]

### Illustrative counterexample: the lesson is the mystery

A finite discovery activity centers on discovering that an apparently decorative object changes a rule. A mandatory demonstration of that fact would teach the rule while removing the intended experience. The supported-attempt pattern should not be used on the secret itself. It may still be appropriate for prerequisite interaction that does not disclose the secret. “No solution tutorial” and “no accessible information or help” are not equivalent design decisions. [C-08; C-13; C-15]

### Source-based counterexamples to blanket prescriptions

The different tutorial outcomes in Andersen's three games oppose a universal claim that adding instruction necessarily improves measured engagement. Productive-failure research supplies a conditional alternative to universal explanation-first instruction; it does not support unguided abandonment. Expertise-reversal theory opposes fixed assistance for every level of relevant knowledge. These sources disagree with **blanket formulations**, not necessarily with one another under matched conditions. [C-02; C-04; C-05]

## Failure modes and constraints

**False learning signals:** clicks on “understood,” guided completion and immediate repetition may not distinguish understanding from compliance. A changed-task check may itself be invalid if it changes too many relevant demands. Do not infer enduring mastery from a single observation. [C-01; C-10; C-11]

**Adaptive mistakes:** a slow player may be deliberating, using an access method or enjoying exploration. A fast player may know only a memorized sequence. Treat diagnostic uncertainty explicitly; do not automatically remove help, disclose answers or label someone incompetent from elapsed time. [C-08; C-13]

**Ethics:** do not use surprise loss, social shame or compulsory repetition to force a lesson when a safer relevant alternative is available. This is a proposed precaution, not an already approved studio policy. Participation in an evaluation must remain distinct from acceptance of a game challenge. No clinical conclusion or protected-trait inference is warranted. [C-13; C-16]

**Localization:** examples, rule terms, objective histories and help must agree after translation. A translation that changes “before” to an ambiguous sequence can change the learned model even when the game rule is unchanged. Re-entry text must reflect actual state rather than a generic remembered narrative. These are plausible failure analyses, not observed defects in a shipped product. [C-14]

**Production:** optional lessons need maintenance when rules change; varied checks need representativeness review; state-linked recaps need a trustworthy account of what happened. Prefer a small number of high-value learning targets and player-requested reference over an elaborate diagnostic system when its reliability and benefit are unproven. No cost-saving percentage is claimed. [C-14]

## Playtest and validation

**Proposed only; no tests, prototypes, participant recruitment or telemetry collection occurred.**

Choose a single learning target and compare a minimal direct-instruction route, the supported-attempt pattern and, only where ethically and functionally appropriate, a discovery route. Keep the rule, content exposure, access settings and available practice comparable; track extra time and extra information rather than assuming they are equivalent. [C-16]

Include relevant novices, experienced players encountering a novel rule, returning players and people using the intended access/language routes. Do not conflate a participant's actual absence with an arbitrarily imposed laboratory pause. The team must choose any follow-up interval from its question and feasible design; the vocabulary experiment's one-week interval is not a game requirement. [C-06; C-12; C-16]

Measure prediction accuracy, the chosen action in a changed situation, recovery after an unexpected result, help requests, unwanted interruption, experienced control, and later use where feasible. A changed task is not evidence of distant transfer; record exactly what changed. Observe dropouts and skipped help without deciding in advance whether they indicate mastery, access failure or rejection. [C-11; C-16]

Predeclare the locally important benefit, tolerable support burden and unacceptable loss of discovery/access. **Reject or adapt** when the pattern increases only guided completion; when later rule use is no better than a simpler route; when fading creates systematic errors or loss of access; when players reject unnecessary practice; or when explanation destroys the intended discovery. Analyze subgroup and context differences as possible boundary conditions, not automatically as noise. No sample-size guarantee or universal pass threshold is supplied. [C-16]

## Claim ledger

Claim IDs are local to this entry. A reference attached to a hypothesis identifies its rationale, not proof of the proposed intervention. `None — original analysis` means no external experiment is claimed. Confidence applies to the exact scoped wording, not to universal effectiveness.

| Claim | Precise claim | Class | Evidence and contrary support / locators | Applicability and confidence | Unresolved question |
|---|---|---|---|---|---|
| C-01 | Guided performance, onboarding completion, understanding and durable learning are distinct evaluation targets. | inference | GDR-SRC-20261010-F01-13, pp. 966–968, equivalent acquisition versus delayed recall; GDR-SRC-20261010-F01-10 outcomes. | Moderate measurement distinction; not a universal definition of play. | What evidence would demonstrate the target capability? |
| C-02 | Tutorial effects differed across the three studied games; outcomes measured engagement rather than direct learning, and complexity was not isolated from game/audience. | empirical-evidence | GDR-SRC-20261010-F01-10, pp. 61–68, especially Table 3 and Conclusion. | Field experiments, over 45,000 players; moderate within treatments, low for universal complexity rule. | Which feature, audience or access difference explains heterogeneity? |
| C-03 | The pooled Hello Worlds help comparison has a table/prose direction discrepancy in the inspected article. | observed-example | GDR-SRC-20261010-F01-10, p. 66 Table 3: 18.56% versus 19.78%; p. 67 pooled-help paragraph says increase. Observed by F01 author on 2026-10-10 through PDF text and screenshot. | High for document discrepancy, unresolved for underlying data interpretation. | Is there an erratum or author clarification? |
| C-04 | Expertise-reversal theory supplies a conditional rationale for varying instructional support with relevant knowledge. | inference | GDR-SRC-20261010-F01-11, pp. 23–24 and 26–28; reviewed framework, underlying experiments not independently inspected. | Moderate theoretical rationale, low for a game adaptation. | Will tapering help this learner on this task? |
| C-05 | The inspected productive-failure study used generation followed by consolidation, with outcome and context limits rather than a universal no-instruction result. | empirical-evidence | GDR-SRC-20261010-F01-12, pp. 56–65, Method/Posttest and Table 4; routine-item exception in results narrative. | Intact Grade 7 classes; moderate within bounded quasi-experiment, low for entertainment transfer. | Does voluntary play sustain useful investigation and consolidation? |
| C-06 | Continued retrieval supported delayed vocabulary recall in the studied conditions; that does not establish game transfer or enjoyment. | empirical-evidence | GDR-SRC-20261010-F01-13, p. 967 Figures 1–2 and Supporting Method. | 40 students; moderate scoped result; task/participant generalization limited. | Does representative game use show an analogous benefit? |
| C-07 | XAG 109 recommends revisitable objective/history/tutorial information; the framework is best-practice guidance, not compliance requirements. | practitioner-heuristic | GDR-SRC-20261010-F01-14, Implementation guidelines and overview Introduction; current pages inspected 2026-10-10. | Moderate as first-party guidance, not a causal effect estimate or formal standard. | What adaptation preserves discovery and access in the target game? |
| C-08 | Diagnose knowledge, access, goals and desired discovery before choosing direct instruction, bounded discovery or omission. | hypothesis | GDR-SRC-20261010-F01-10 heterogeneity; GDR-SRC-20261010-F01-11 expertise framework; GDR-SRC-20261010-F01-12 conditional discovery-plus-consolidation. | Low for comparative efficacy of this diagnostic process. | Does diagnosis select a better support route than a simpler default? |
| C-09 | Representative attempts and feedback about relevant rule conditions may help players revise an incorrect explanation. | hypothesis | GDR-SRC-20261010-F01-12 consolidation rationale; GDR-SRC-20261010-F01-13 retrieval is indirect and did not test this feedback format. | Low; complete causal feedback intervention not tested. | Would result-only feedback, an example or direct information work better? |
| C-10 | A changed-task check may justify reversible tapering of answer-leading prompts, but a single success cannot establish durable mastery. | hypothesis | GDR-SRC-20261010-F01-13 delayed-recall distinction; GDR-SRC-20261010-F01-11 expertise rationale; neither tests the complete pattern. | Low for design benefit; requires representative tasks and restored help. | Does tapering improve participation without reducing later capability? |
| C-11 | A check must discriminate relevant mental models without adding unrelated demands or claiming distant transfer. | inference | GDR-SRC-20261010-F01-13 task-specific evidence; original measurement/causal reasoning. | Moderate for test validity logic, low for a particular task design. | Could copying, guessing or a new burden explain the result? |
| C-12 | A goal-and-state recap plus optional targeted practice may support return better than mandatory replay of all instruction. | hypothesis | GDR-SRC-20261010-F01-14 revisitable information; GDR-SRC-20261010-F01-13 only indirect memory rationale. No direct re-entry comparison inspected. | Low; absence duration, changed state and prior skill are moderators. | Is recap, practice, both or neither needed? |
| C-13 | Instructional scaffolding should be separated from access accommodations and ordinary state information; inferred skill alone is not a basis to remove access. | inference | GDR-SRC-20261010-F01-14 accessibility purpose; original precaution and measurement separation. | Moderate design safeguard; not a legal ruling or approved policy. | Which support is pedagogical, and which enables participation? |
| C-14 | Consistent rule language, state-accurate recaps and maintained examples are dependencies of the proposed learning process. | inference | GDR-SRC-20261010-F01-14 objective/history guidance; original production and localization failure analysis. | Moderate conditional requirement, no measured cost or effect estimate. | Can the team maintain accuracy across rule changes and locales? |
| C-15 | Simultaneous-resolution, shared-project and secret-rule examples are illustrative and have not been implemented or tested. | hypothesis | None — original examples and proposed countercases. | Low empirical confidence; explicit assumptions. | Which assumptions survive adaptation to a real design? |
| C-16 | Proposed evaluation must distinguish guided completion, changed-task use, later use and experience; reject benefits that depend on lost access or spoiled discovery. | hypothesis | GDR-SRC-20261010-F01-10 outcome limits; GDR-SRC-20261010-F01-13 learning distinction; GDR-SRC-20261010-F01-14 access rationale; original test protocol. | Low for intervention efficacy; criteria are proposed, not performed results. | Does the more elaborate route outperform the simpler relevant alternative? |

## References

PDF locators distinguish printed page numbers from file-page counts where they differ. No cited full paper, figure, participant quotation, or questionnaire is redistributed.

### GDR-SRC-20261010-F01-10 — The Impact of Tutorials on Games of Varying Complexity

**Citation:** Erik Andersen, Eleanor O’Rourke, Yun-En Liu, Richard Snider, Jeff Lowdermilk, David Truong, Seth Cooper, and Zoran Popović. 2012-05; CHI 2012, May 5–10. *The Impact of Tutorials on Games of Varying Complexity*. ACM, CHI 2012, pp. 59–68.

**Verified access route:** [The Impact of Tutorials on Games of Varying Complexity](https://grail.cs.washington.edu/wp-content/uploads/2015/08/andersen2012tio.pdf). DOI: `10.1145/2207676.2207687`.

**Version and access:** Ten-page published conference paper on author institution’s site. Accessed 2026-10-10; `access: relevant-excerpt`. Original multi-condition field experiments across three author-developed games.

**Inspected locators:** pp. 61–64 games/tracking/Study Design; pp. 65–67 Data Analysis and Results; p. 66 Table 3 visually inspected; pp. 67–68 Conclusion/limitations.

**Claims supported here:** C-01, C-02, C-03, C-08, C-16.

**Limits:** Engagement proxies, not direct mastery tests. Game/audience/download differences confound cross-game complexity explanations. Table/prose disagreement on pooled Hello Worlds help return rate is unresolved in F01.

**Independence/deduplication:** Multiple PDF mirrors are one DOI/source; not separate studies. Underlying data/code and errata not independently audited. Cross-batch DOI/URL/edition matching and global source allocation are pending Library Coordination.

**Rights:** Copyright ACM 2012; paraphrase only; no screenshot or article distributed.

### GDR-SRC-20261010-F01-11 — The Expertise Reversal Effect

**Citation:** Slava Kalyuga, Paul Ayres, Paul Chandler, and John Sweller. 2003; online publisher posting date 2010-06-08 is not the original article date. *The Expertise Reversal Effect*. Lawrence Erlbaum Associates, Educational Psychologist 38(1), 23–31.

**Verified access route:** [The Expertise Reversal Effect](https://www.davidlewisphd.com/courses/EDD8121/readings/2003-Kalyuga_et_al.pdf). DOI: `10.1207/S15326985EP3801_4`.

**Version and access:** Published 2003 review/theory article, educational-site mirror. Accessed 2026-10-10; `access: relevant-excerpt`. Authors’ scholarly synthesis and expertise-reversal framework; not a new experiment.

**Inspected locators:** pp. 23–24 framework; pp. 26–28 Worked Examples and instructional implications.

**Claims supported here:** C-04, C-08, C-10.

**Limits:** Underlying trials are discussed by the authors, not independently inspected in F01. Use as a conditional theoretical rationale; game-specific adaptation remains a hypothesis.

**Independence/deduplication:** Secondary to underlying studies, including the authors’ own earlier work; no replication count inferred. Cross-batch DOI/URL/edition matching and global source allocation are pending Library Coordination.

**Rights:** Copyright Lawrence Erlbaum Associates 2003; educational mirror, no redistribution license established.

### GDR-SRC-20261010-F01-12 — Designing for Productive Failure

**Citation:** Manu Kapur and Katerine Bielaczyc. 2012 issue; first published online 2011-07-21. *Designing for Productive Failure*. Taylor & Francis, Journal of the Learning Sciences 21(1), 45–83.

**Verified access route:** [Designing for Productive Failure](https://docdrop.org/static/drop-pdf/Kapur---Designing-for-Productive-Failure-oaAJc.pdf). DOI: `10.1080/10508406.2011.591717`.

**Version and access:** Publisher-formatted article plus cover page; 40 PDF pages. Accessed 2026-10-10; `access: relevant-excerpt`. Original classroom quasi-experiment using intact classes in three Singapore schools.

**Inspected locators:** pp. 56–62 design, sample and intervention; pp. 63–65 Results/Posttest; p. 64 Table 4 visually inspected; p. 65 Table 5 parsed text accessible but screenshot failed twice, so no numerical inference relies on that table.

**Claims supported here:** C-05, C-08, C-09.

**Limits:** Grade 7 mathematics; not randomized individual assignment, not voluntary entertainment. Generation is followed by teacher-led consolidation; teacher/school/design confounds remain. School C’s routine-item difference was not significant in the results narrative.

**Independence/deduplication:** Develops prior productive-failure research including 2008 lead GDR-SRC-20261010-F01-17; not an independent replication family. Cross-batch DOI/URL/edition matching and global source allocation are pending Library Coordination.

**Rights:** Copyright Taylor & Francis; mirrored publisher PDF, no redistribution license established.

### GDR-SRC-20261010-F01-13 — The Critical Importance of Retrieval for Learning

**Citation:** Jeffrey D. Karpicke and Henry L. Roediger III. 2008-02-15. *The Critical Importance of Retrieval for Learning*. AAAS, Science 319(5865), 966–968.

**Verified access route:** [The Critical Importance of Retrieval for Learning](https://learninglab.psych.purdue.edu/downloads/2008/2008_Karpicke_Roediger_Science.pdf). DOI: `10.1126/science.1152408`.

**Component/access route:** [Supporting Online Material](https://learninglab.psych.purdue.edu/downloads/2008/2008_Karpicke_Roediger_ScienceSupportingMaterial.pdf).

**Version and access:** Published paper plus its Supporting Online Material, treated as one source. Accessed 2026-10-10; `access: relevant-excerpt`. Original four-condition laboratory vocabulary-recall experiment.

**Inspected locators:** pp. 966–968 design/results/limits, especially p. 967 Figures 1–2 (visually inspected); Supporting Online Material, Method: Subjects/Design/Materials/Procedure, pp. 2–3.

**Claims supported here:** C-01, C-06, C-09, C-10, C-11, C-12, C-16.

**Limits:** 40 university students, 40 Swahili–English pairs, one-week recall. Not motor learning, game enjoyment, or a test of the whole F01 pattern. Retrieval practice did not supply answer feedback during test trials.

**Independence/deduplication:** Main article and supplement are components of the same experiment; not two independent sources. Cross-batch DOI/URL/edition matching and global source allocation are pending Library Coordination.

**Rights:** Copyright AAAS 2008; author-hosted copies; paraphrase only.

### GDR-SRC-20261010-F01-14 — Xbox Accessibility Guidelines: XAG 109 Objective clarity, with framework overview

**Citation:** Microsoft. XAG 109 last updated 2026-03-04; overview last updated 2026-08-14; framework v3.2 dated 2023-06-08. *Xbox Accessibility Guidelines: XAG 109 Objective clarity, with framework overview*. Microsoft Learn.

**Verified access route:** [Xbox Accessibility Guidelines: XAG 109 Objective clarity, with framework overview](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/109). DOI: not recorded; use the verified URL.

**Component/access route:** [Framework overview and version history](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines).

**Version and access:** Live web documentation inspected 2026-10-10; overview labels framework v3.2; no immutable commit supplied. Accessed 2026-10-10; `access: full`. First-party accessibility best-practice guidance, not certification or legal requirements.

**Inspected locators:** XAG 109: Overview, Scoping questions, Implementation guidelines (objectives, reminders, interactive tutorials, revisiting tutorials); overview: Introduction and Version history, including non-compliance disclaimer.

**Claims supported here:** C-07, C-12, C-13, C-14, C-16.

**Limits:** Recommendations need game-specific interpretation and representative access review. Does not empirically establish improved retention or specify a universal re-entry protocol. F01 does not inspect the games shown as examples.

**Independence/deduplication:** Guideline and overview are one documentation family/source identity; not independent evidence. Cross-batch DOI/URL/edition matching and global source allocation are pending Library Coordination.

**Rights:** Microsoft documentation; paraphrase and link only; embedded third-party images not reused.

## Open questions and change history

Open questions: game-specific feedback comparisons; durable and changed-context transfer; representative access/language evaluation; and return after realistic absence. F01-X-01 preserves the source table/prose discrepancy; F01-X-03 and F01-X-04 preserve instruction-sequence and performance/learning distinctions. No universal hint delay or successful-attempt threshold was established.

**2026-10-10 — 0.1.0 draft:** initial F01 candidate using the available starter topic/pattern templates and the current bounded authorization. Author self-review is documented in the [batch review packet](../reviews/full-run-20261010-f01-review-packet.md). Independent review has not occurred. No prior version is superseded, no canonical authority is claimed, and no release or game adoption is approved. Permanent identity, cross-batch source matching and dependency resolution await Library Coordination.

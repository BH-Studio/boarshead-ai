---
id: GDR-CAND-20261010-G12-GEN-01
kind: genre
title: Simulation
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
- simulator
- process simulation
tags:
- model-scope
- fidelity
- learning-transfer
- system-observation
related_topics:
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F07-TOP-01
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-G12-PAT-01
- GDR-CAND-20261010-G12-PAT-02
- GDR-CAND-20261010-F01-PAT-01
related_genres:
- GDR-CAND-20261010-G12-GEN-02
- GDR-CAND-20261010-G12-GEN-03
source_ids:
- GDR-SRC-20261010-G12-001
- GDR-SRC-20261010-G12-002
- GDR-SRC-20261010-G12-003
- GDR-SRC-20261010-G12-004
- GDR-SRC-20261010-G12-012
- GDR-SRC-20261010-G12-013
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial G12 bounded research draft; previous batch identities and queues are not reset.
hash_record: ../reviews/full-run-20261010-g12-integrity-receipt.md
---

# Simulation

**Draft, coverage open.** This entry helps choose what a simulation asks players to understand, manipulate or experience. It is neither a certification of model fidelity nor a claim that simulator use transfers to real-world competence. Definitions below are provisional analytical choices, not an approved taxonomy change. [C-01, C-06]

## Definition and boundaries

For this file, **simulation** means an experience in which interacting with a represented, evolving process is a central activity. The process can be physical, social, abstract or invented. Merely executing state transitions does not make every game equally useful to index as simulation: ask whether learning, operating, experimenting with or inhabiting that process is a substantial player-facing promise. [C-01]

Separate six design commitments rather than scoring “realism” on one scale. The **model** defines state, rules, time, agents and omissions. The **interface** determines what can be perceived and controlled. **Fidelity** describes a particular correspondence—such as behavior, procedure, appearance or structure—to an identified reference. **Predictive scope** states the conditions under which a forecast is intended to apply. A **learning goal** identifies what a player should subsequently do or discriminate. The **experience goal** concerns the intended activity, such as experimentation, skilled operation, expression or role-play. Improving one commitment need not improve the others. [C-02]

[Management](management.md) adds recurring allocation and delegation under constraints; [city builder](city-builder.md) adds settlement-scale spatial and public consequences. Neither is equivalent to this parent framing. Life simulation, colony simulation and immersive simulation remain separate roster entries whose actual guidance was not available for transfer. Procedural generation is a technique, not sufficient evidence of a simulation genre. A construction toy can be adjacent without promising economic management. Platform, multiplayer mode, camera and tone remain facets. [C-01; missing-dependency record in the packet]

## Custom research instructions

Frame research around **a model-to-decision relationship**, not an inventory of realistic features. Specify the manipulated inputs, modeled state, observation window, intended explanation and an alternative model that could produce a similar screen. Investigate whether apparent unpredictability comes from stochastic rules, undisclosed information, delayed effects, numerical approximation or an actual inconsistency. Do not call all of these emergence. [C-02, C-08]

For physical simulation, seek reference data, operating-envelope limits, calibration procedures and out-of-envelope cases. For social simulation, inspect how agent categories, preferences, institutions and agency are authored; ask what the model excludes rather than treating its categories as natural kinds. For abstract simulation, inspect conservation, delays and aggregation. For procedural variants, separate the generation process from the subsequent interactive model and identify constraints that are guaranteed versus merely typical. [C-03–C-05, C-11]

Sample both instrument-heavy and deliberately simplified experiences; task-focused training and expressive play; individual operation and facilitated group activity. Challenge these misleading comparisons: graphical detail equals predictive accuracy; realistic numbers imply neutral social assumptions; faster completion means understanding; a facilitated workshop proves an entertainment game teaches; and every model needs full disclosure. Original technical documentation, model specifications and comparative studies are preferred over feature lists. A future build observation must record observer, date, platform, version, settings and the exact reproducible sequence. None was performed here. [C-06, C-08, C-11]

## Player promises and varied audiences

Candidate promises are **operational mastery**, **causal exploration**, **inhabiting a represented role**, and **expressive manipulation**. These are useful questions to ask prospective players, not measured segments or universal expectations. Someone seeking cockpit procedure may value a complication that frustrates someone exploring flight principles; a builder may prefer a responsive toy to an obligation to manage a budget. Treat the chosen promise as a local hypothesis to test, including players who reject the premise. [C-09]

The inspected range includes a technical flight model, an abstract investment task, a social agent model, a facilitated climate negotiation and an expressive building toy. Their purposes and evidence routes differ. They cannot be pooled into a finding about “simulation players.” Townscaper’s publisher explicitly frames it as a goal-free building toy; that provides a boundary countercase, not proof that all simulation audiences prefer low pressure. [C-10; GDR-SRC-20261010-G12-012]

## Characteristic loops and structures

A useful analytical loop is **form a prediction → intervene or operate → let state evolve → inspect a consequence → revise the explanation or objective**. A session might repeat a controlled scenario, sustain operation through changing conditions, or explore without an explicit win state. Long-term progression can come from more demanding situations, wider responsibility or richer expression, but none is mandatory. This is an organizing inference, not a measured genre law. [C-02, C-09]

Three separations matter when designing that loop. First, a displayed outcome is not necessarily the state that produced it: a gauge can be delayed or summarized. Second, agreement with a target in one scenario does not establish a model’s range. Third, a player can learn a successful in-game response without learning why it works or where it stops working. Keep an internal record of these separations even when the intended experience deliberately hides some rules. [C-02, C-06, C-08]

### Mechanisms, support and alternatives

The Microsoft flight documentation defines an evolving state/control model, while its companion tutorial discusses data and tuning within a limited scope. This supports asking exactly which relation is being represented; it does not establish the accuracy of an arbitrary aircraft implementation. **Application bridge:** select reference conditions before choosing expensive detail, then record what evidence would expose a mismatch. A simpler model is an alternative when it preserves the decision being studied; it is not automatically adequate for a different training objective. [C-03, C-04; GDR-SRC-20261010-G12-001, GDR-SRC-20261010-G12-013]

The documented NetLogo example derives aggregate configurations from specified local rules. **Application bridge:** when a social simulation makes an outcome seem inevitable, expose the relevant assumptions somewhere in its interpretive material and compare an alternative rule or boundary. This recommendation is an inference about interpretability, not a demonstrated intervention effect. Adding realistic-looking identities would not, by itself, validate the mechanism or make the represented community less stereotyped. [C-05, C-11; GDR-SRC-20261010-G12-002]

Sterman’s investment experiment reports difficulty in a dynamic task despite available information; the World Climate study reports pre/post changes in a facilitated intervention but cannot isolate simulator causality. Together they justify neither “simulation teaches automatically” nor “simulation cannot teach.” **Application bridge:** choose a specific learning claim, then distinguish model prediction, changed-case discrimination, retention and outside-task transfer. Entertainment value can remain the goal without an educational claim. [C-06, C-07; GDR-SRC-20261010-G12-003, GDR-SRC-20261010-G12-004]

## Conditional application process

**Diagnose the intended use.** Write a sentence identifying what the player changes and what counts as a meaningful consequence. A vehicle-handling fantasy, equipment-procedure exercise and physical prediction tool need different evidence. Record the intended population and whether domain knowledge is prerequisite. [C-02, C-09]

**Choose the model contract.** Record units, time step or event order, random elements, agent assumptions, omitted processes, boundary conditions and reference data. Identify which parameters are authored approximations and which have calibration support. Separate visual approximations from changes to the causal relation. Establish acceptable error locally; this batch supplies no universal tolerance. [C-02–C-05]

**Choose disclosure and control.** Distinguish actual state, measurement, estimate, forecast and unknown. Decide which information belongs in normal operation, optional inspection, instruction or post-scenario debrief. An unavailable observation is not zero. Provide nonvisual or non-timed routes to entitled information without silently changing a supposed test of model understanding into a test of access. [C-08, C-12]

**Prototype a discriminating situation, later under implementation approval.** Compare a simple and a more detailed representation while holding the target decision recognizable. Include cases where the correct prediction changes, not just where the numbers or artwork change. Preserve necessary aids. The present document specifies these comparisons; it does not run them. [C-06, C-14; DEP-TRANSFER]

**Evaluate and revise separately.** Check model consistency, target-domain correspondence, interpretation, interaction access and experience. Failure in one is not proof of failure in every other. When prediction outside the calibrated scope fails, narrow the claim rather than relabeling a plausible animation as validation. [C-06, C-08, C-14]

### Illustrative worked example: reservoir operation

**Synthetic, not a shipped-game observation.** A small model includes water stored, intake, release and delayed pump installation. One mode asks the player to keep an invented settlement supplied; another asks them to predict a reservoir’s response to an intake change. The former can tolerate some abstraction that invalidates the latter’s intended learning claim. Start by declaring whether evaporation, variable demand and pump failures are modeled. Do not describe omitted processes as experimentally negligible. [C-02, C-11]

A player orders another pump when storage keeps falling. The interface distinguishes water now, current net flow and pumps already being installed. The player can still rationally add capacity to create redundancy; a duplicate order is not automatically a mistake. A prediction question asks whether the *scheduled* addition changes future flow under the stated assumptions; a preference question asks whether its cost is acceptable. A second case changes the pending pump’s completion date so the earlier answer no longer works. This is a proposed application of the reviewed transfer correction and [pending-work reconciliation](../patterns/pending-work-reconciliation.md), not evidence of its efficacy. [C-07, C-13, C-14]

**Counterexample:** in a discovery-focused model, instantly displaying every dependency can remove the intended task of inference. Preserve accessible observations while offering an optional hypothesis log or later explanation instead of a complete live causal diagram. In a procedural-control task, delegating the practiced operation would invalidate the learning comparison. [C-08, C-13]

## Applying shared topics

**Learning/onboarding — `GDR-CAND-20261010-F01-TOP-03`.** Simulation changes the transfer target: success within an authored rule set is not evidence of learning a real process. Use the corrected `GDR-CAND-20261010-F01-PAT-01` when a changed case genuinely requires a different feasibility answer; never remove accommodations to manufacture difficulty. [C-06, C-14]

**Interface/information and accessibility — `GDR-CAND-20261010-P01-TOP-02` and `GDR-CAND-20261010-P01-TOP-03`.** Mark the difference between sensed state, lagged data and a forecast. Inspect combinations of instruments, map, text, controls and interruption recovery. Preserve P01’s numerical scope correction; no web CSS-pixel rule becomes an all-platform simulator requirement here. [C-08, C-12]

**Decision design, evaluation and ethics — `GDR-CAND-20261010-F02-TOP-01`, `GDR-CAND-20261010-F07-TOP-01`, `GDR-CAND-20261010-F07-TOP-02`.** Keep intended uncertainty distinct from misleading certainty; evaluate the stated construct; inspect what the model rewards or makes impossible. The shared **Simulation and systemic behavior** topic’s selected reviewed bytes were not available. This file does not replace that genre-neutral topic or invent its identity. [C-08, C-11, C-14]

## Pattern selection and adaptations

Use [pending-work reconciliation](../patterns/pending-work-reconciliation.md), `GDR-CAND-20261010-G12-PAT-01`, for delayed commitments the player is entitled to inspect, not for revealing intentionally concealed causal rules. Use [bounded delegation contract](../patterns/bounded-delegation-contract.md), `GDR-CAND-20261010-G12-PAT-02`, only when supervising policy is desired and the delegated action is not the skill being assessed. Both are unvalidated candidate techniques. A simulation/management hybrid can retain policy choices while delegating routine execution; a procedural-training hybrid may need the opposite. [C-13]

## Accessibility, ethics, localization and production

Proposed access checks include pause or a suitable inspection alternative, configurable input demands, readable/narratable instruments, explicit units, and recoverable errors. A paused display must identify whether its values remain a snapshot or continue updating. Do not assume tactile hardware, color discrimination, numerical fluency, fast reading or domain vocabulary. Localize units, decimal conventions and explanations together; conversion alone may obscure what a quantity means. These are design hypotheses requiring representative evaluation, not a completed compliance assessment. [C-12]

For social models, document whose actions are represented, whose constraints are omitted and whether the player’s objective erases other people’s interests. Clearly identify invented simplifications without claiming that a warning alone prevents misleading interpretation. For production, budget reference-data acquisition, calibration, state inspection, scenario coverage, localization and regression after rule changes. More parameters create more claims to maintain; they do not earn a fidelity label automatically. [C-04, C-11, C-12]

## Research questions and validation

All tests below are **proposed; not performed; no participants, builds or results exist for G12**. Choose sample size and acceptance margins from the later study’s question, variability, recruitment and cost; no numerical guarantee is supplied. [C-14]

| Question and comparison | Procedure and participants | Measures, confounds and rejection condition |
|---|---|---|
| Does extra fidelity preserve the target relation or merely appearance? | Compare simpler and more detailed variants on preregistered reference cases and unseen boundary cases; involve appropriate domain expertise plus intended players. | Separate prediction error, operation errors and preference. Control controls/display familiarity. Reject the broader fidelity claim when agreement is confined to calibrated examples. |
| Does an explanation support model-scope discrimination? | Compare ordinary instruction with an optional assumption contrast; use changed correct answers and a case outside declared scope. Include varied domain knowledge and access needs. | Score predictions and reasons separately from preferred actions; track overgeneralization and burden. Reject if explanation increases confidence without discrimination or removes the desired discovery. |
| Does a learning claim survive beyond the interface? | Assess an independently specified target task after a delay and without familiar surface cues; preserve access supports. | Rule out cue memorization and prior expertise. Do not label same-interface retention real-world transfer. Narrow the claim if outside-task performance does not improve. |

## Coverage, contradictions and review history

**Researched:** model/interface/fidelity/scope distinctions; physical, social and abstract routes; procedural-toy boundary; learning limits; delayed feedback; conditional patterns and proposed evaluation. **Open:** executable observations, formal model-validation standards, broad procedural simulation practice, real-world transfer, different cultural interpretations of social models, and sustained accessibility/production evidence. No attempt is made to certify flight training or other professional competence. [C-03–C-14]

Relevant batch contradictions are **G12-CON-01** (information versus understanding), **G12-CON-02** (fidelity versus purpose), and **G12-CON-05** (social model outcomes versus real-world explanation). See the packet for opposing propositions and discriminating evidence. Initial revision `initial-author-draft-1`; no predecessor or supersession. Author self-review challenged fidelity and educational overreach; independent review, host retrieval tests and release remain pending. The next research decision is which target decision and comparison deserve validation, after content review—not whether an impressive model should be adopted.

## Claim ledger

Claim IDs are local to this artifact. Bare three-digit source numbers in a ledger expand to `GDR-SRC-20261010-G12-`; DEP labels resolve in Reviewed dependency provenance. Family abbreviations such as G12-PAT-01 expand to `GDR-CAND-20261010-` plus that family suffix. Confidence concerns the stated claim, not a general endorsement. Recommendations and synthetic examples are not studio-approved decisions. No unperformed test is evidence.

| Claim | Precise claim | Class | Source and locator / reasoning | Confidence and applicability | Unresolved question |
|---|---|---|---|---|---|
| C-01 | Treat simulation as a process-centered player activity, with explicit neighboring boundaries rather than a universal market definition. | inference | G12 brief decision question; TAXONOMY.md genre roster; contrast of 001/002/012. | Moderate as an analytical partition; not audience consensus. | Will Coordination retain these boundaries after neighboring-genre review? |
| C-02 | Model, interface, fidelity, predictive scope, learning goal and experience goal should be specified separately. | inference | 001 opening formulation; 013 introduction; DEP-UI task information contract. | Moderate: distinct design questions; usefulness of this exact decomposition untested. | Which distinctions change an actual design decision? |
| C-03 | The inspected Flight Model Physics document defines aircraft state evolution in response to control input. | observed-example | GDR-SRC-20261010-G12-001, “What is a Flight Dynamics Model?”; observed documentation, not game execution. | High for the page’s formulation; no runtime accuracy claim. | What implemented build and calibrated envelope does a future case use? |
| C-04 | The companion flight-model tutorial limits its scope and discusses imperfect data and tuning. | practitioner-heuristic | GDR-SRC-20261010-G12-013, introduction and “Gathering Data”. | High for documented advice; low for any untested fidelity improvement. | Which added detail is supported by suitable reference data? |
| C-05 | The NetLogo page specifies a stylized local-rule social model, not a validated account of actual communities. | observed-example | GDR-SRC-20261010-G12-002, WHAT IS IT/HOW TO USE IT/EXTENDING THE MODEL. | High for documented model content; runtime not executed. | How do different constraints or boundaries change the conclusion? |
| C-06 | The World Climate study reports pre/post learning-related changes, but its bundled, nonrandomized intervention cannot establish general simulator-caused learning or real-world competence. | empirical-evidence | GDR-SRC-20261010-G12-004, Sample and data collection; Discussion limitations. | Moderate for this observational intervention; low transfer to entertainment games. | Would an independent comparison and delayed target-task assessment retain the finding? |
| C-07 | A selected capital-investment experiment reports dynamic decision difficulties despite available information; it does not test G12’s interface patterns. | empirical-evidence | GDR-SRC-20261010-G12-003, printed pp.22–24,26–28; distinguish human trials from Fig.5 model runs. | Moderate within the historical task; no claimed UI effect magnitude. | Which failures arise from information, interpretation or a rational objective difference? |
| C-08 | Disclose epistemic status and model limits without assuming maximum disclosure is always desirable. | inference | DEP-UI lines55–85; DEP-DECISION lines63–104; 003 contrary case. | Moderate conditional reasoning; exact disclosure benefit untested. | When does disclosure help diagnosis versus remove desired inference? |
| C-09 | Operation, exploration, role inhabitation and expression are candidate promises, not universal audience preferences. | hypothesis | Purpose-based synthesis; source cases are not an audience survey. | Low until evaluated with intended participants. | Which promise matters to this population and situation? |
| C-10 | Townscaper is advertised as a goal-free expressive building toy, a boundary countercase to obligatory management pressure. | observed-example | GDR-SRC-20261010-G12-012, main publisher description. | High for advertised positioning, not player response or genre consensus. | How do players actually interpret its model and genre? |
| C-11 | Social assumptions and omitted constraints should remain interpretable; illustrative models must not be presented as empirical social laws. | inference | 002 explicit rule set; DEP-ETHICS representation/agency passages. | Moderate ethical/epistemic rationale; disclosure efficacy not established. | Do players recognize the omissions or infer natural inevitability? |
| C-12 | Instrument access, units, localization and model-maintenance work require explicit project-specific evaluation. | hypothesis | DEP-ACCESS scoped access chain; DEP-UI state/ownership; 013 production context. | Low for specific benefit; plausible requirements to investigate. | Which barriers and maintenance costs dominate the chosen platform? |
| C-13 | Apply pending-work and delegation patterns only when their disclosed state and retained decisions fit the simulation’s purpose. | hypothesis | G12-PAT-01/02 mechanisms; DEP-DECISION; illustrative reservoir example. | Low: proposed synthesis, no efficacy study. | Does the pattern remove a targeted skill or legitimate uncertainty? |
| C-14 | Separate model checks, changed-answer prediction, preference, retention and outside-task transfer in proposed evaluation. | hypothesis | DEP-TRANSFER corrected example lines96–127; DEP-EVALUATION; 004 limitations. | Moderate construct rationale; exact test protocol unperformed. | What outcome would falsify the locally selected learning or experience claim? |

## References

Observer: the G12 authoring assistant, through document inspection, not game execution. Access/check date: **2026-10-11 UTC**. Source IDs are temporary run-scoped identities, reused within G12. Cross-batch canonical URL/DOI/edition deduplication remains pending. `relevant-excerpt` does not mean the full work, runtime or linked material was inspected.

### GDR-SRC-20261010-G12-001

**Microsoft Flight Simulator SDK documentation team. _Flight Model Physics_.** Publication/update: unknown. Publisher: Microsoft Flight Simulator SDK documentation. [Inspected source route](https://docs.flightsimulator.com/html/Samples_And_Tutorials/Primers/Flight_Model_Physics.htm).

**Claims supported or used as an inference/hypothesis premise:** C-02/C-03. **Edition/build:** Microsoft Flight Simulator 2020 documentation family; live HTML; SDK patch and executable build unknown. **Access:** `relevant-excerpt`. **Type:** Primary technical documentation. **Exact locator:** “What is a Flight Dynamics Model?”, introductory state/control formulation (retrieved HTML lines 0–37).

**Rights:** Copyrighted documentation; paraphrase only; no code or diagrams reproduced. **Limits and independence:** Documents a model formulation, not measured flight accuracy or training transfer. Same SDK lineage as source 013; not independent corroboration.

### GDR-SRC-20261010-G12-002

**Uri Wilensky. _NetLogo Segregation model_.** Publication/update: 1997 model; page records conversion in 2001; current page revision unknown. Publisher: Center for Connected Learning and Computer-Based Modeling, Northwestern University. [Inspected source route](https://ccl.northwestern.edu/netlogo/models/Segregation).

**Claims supported or used as an inference/hypothesis premise:** C-05/C-11. **Edition/build:** Live model-information page; NetLogo version and executable build unknown; model not run. **Access:** `relevant-excerpt`. **Type:** Creator-authored model documentation. **Exact locator:** WHAT IS IT?; HOW TO USE IT; THINGS TO NOTICE; EXTENDING THE MODEL; HOW TO CITE; COPYRIGHT AND LICENSE.

**Rights:** CC BY-NC-SA 3.0 as displayed; commercial licensing separately offered. No model code or images redistributed; adoption requires rights review. **Limits and independence:** Local preferences, two agent types and a wrapping world describe this model, not observed social populations. Schelling-inspired: Schelling’s original work was not inspected. No real-world validation or player effects established.

### GDR-SRC-20261010-G12-003

**John D. Sterman. _Misperceptions of Feedback in Dynamic Decision Making_.** Publication/update: 1989. Publisher: International System Dynamics Conference proceedings; condensed reprint of an Academic Press journal article. [Inspected source route](https://proceedings.systemdynamics.org/1989/proceed/plenary-pdf/sterm021.pdf).

**Claims supported or used as an inference/hypothesis premise:** C-07; boundary on C-08/C-14. **Edition/build:** Eleven-page proceedings scan, printed pp. 21–31; first-page footnote identifies condensed reprint from Organizational Behavior and Human Decision Processes 43 (June 1989), original pp. 301–335; DOI 10.1016/0749-5978(89)90041-1 identifies original, not a separately inspected text. **Access:** `relevant-excerpt`. **Type:** Original empirical research, accessed through author conference reprint. **Exact locator:** PDF pp. 1–4, 6–8 (printed pp. 21–24, 26–28): title/footnote; METHOD; representative trajectories/Fig. 3; supply-line formulation; Discussion and Fig. 5. These pages were visually inspected using web screenshots.

**Rights:** Academic Press copyright noted; paraphrase only, no scans or figures redistributed. **Limits and independence:** N=49 selected fluent-English students/professionals in a capital-investment task, not a game-audience sample. Full state/history available, no time limit. Reported oscillatory performance does not identify the effect of a new dashboard. Fig. 5 is model simulation, not a second human experiment. Full journal, raw data and uninspected tables not used; no effect size, confidence interval or replication claim transferred. Distinct from Sterman’s 1989 Management Science beer-distribution paper. Author overlap with 004 does not create replication.

### GDR-SRC-20261010-G12-004

**J. N. Rooney-Varga; J. D. Sterman; E. Fracassi; T. Franck; F. Kapmeier; V. Kurker; E. Johnston; A. P. Jones; K. Rath. _Combining role-play with interactive simulation to motivate informed climate action: Evidence from the World Climate simulation_.** Publication/update: 2018-08-30. Publisher: PLOS ONE 13(8), e0202877. [Inspected source route](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0202877).

**Claims supported or used as an inference/hypothesis premise:** C-06; limits informing C-14. **Edition/build:** Version of record; DOI 10.1371/journal.pone.0202877. **Access:** `relevant-excerpt`. **Type:** Original pre/post empirical study. **Exact locator:** “The World Climate simulation”; “Sample and data collection”; Discussion, especially limitations concerning causality, priming, comparison instruction and intended versus actual action.

**Rights:** CC BY article; attributed paraphrase; no tables reproduced. **Limits and independence:** Facilitated role-play plus C-ROADS, not unassisted simulator play. 39 sessions in 2015–2017 included 2,042 participants; 42% met usable matched-case criteria, so 2,042 is not the analyzed matched sample. No randomized comparison or observed long-term action establishes causality. No numerical effect or precision estimate transferred. Some authors created/facilitated the intervention; Sterman also authored 003. Different task/population, not a replication of G12 patterns.

### GDR-SRC-20261010-G12-012

**Raw Fury; creator Oskar Stålberg identified on page. _Townscaper_.** Publication/update: Original publication unknown; visible CMS timestamp 2026-04-25, not treated as game release date. Publisher: Raw Fury. [Inspected source route](https://rawfury.com/games/townscaper/).

**Claims supported or used as an inference/hypothesis premise:** C-10. **Edition/build:** Live publisher page; executable build and feature-version mapping unknown. **Access:** `relevant-excerpt`. **Type:** Primary publisher description. **Exact locator:** Main description beginning “No goal”; explanation of the block-to-building algorithm (retrieved lines 26–42).

**Rights:** Copyrighted publisher page; paraphrase only. **Limits and independence:** Advertises an expressive building toy without goals or failure pressure. No user study or runtime inspection supports claims about comfort. A procedural toy is a contested simulation/city-builder boundary, not a mandatory genre member.

### GDR-SRC-20261010-G12-013

**Microsoft Flight Simulator SDK documentation team. _Defining A Flight Model_.** Publication/update: unknown. Publisher: Microsoft Flight Simulator SDK documentation. [Inspected source route](https://docs.flightsimulator.com/html/Samples_And_Tutorials/Tutorials/Defining_A_Flight_Model.htm).

**Claims supported or used as an inference/hypothesis premise:** C-02/C-04. **Edition/build:** Microsoft Flight Simulator 2020 documentation family; live HTML; SDK patch/build unknown. **Access:** `relevant-excerpt`. **Type:** Primary technical tutorial. **Exact locator:** Introduction and “Gathering Data” (retrieved lines 0–38).

**Rights:** Copyrighted documentation; paraphrase only; no code reproduced. **Limits and independence:** Tutorial limits its scope to aerodynamics/engine performance and discusses incomplete/inconsistent data and tuning. Does not certify a model’s accuracy. Same SDK lineage as 001.

## Reviewed dependency provenance

These are inspected **parent-selected reviewed drafts**, not released references and not new G12 sources. Their underlying cited papers were not automatically re-inspected. Only the named passages are transferred as qualified research guidance. Exact bytes came from the materialized waves 1–2 archive; they are not copied into this output. Full archive and gap receipts are in the [batch dependency record](../reviews/full-run-20261010-g12-review-packet.md#reviewed-dependencies).

**DEP-TRANSFER: `GDR-CAND-20261010-F01-PAT-01`**, version `0.1.0`, `draft`, candidate revision `independent-review-correction-1`. Archive path `selected-drafts/patterns/supported-attempt-and-transfer-check.md`. Inspected: Recipe; corrected Worked examples, lines 96–127: vary the correct feasibility answer, retain accommodations, separate preference from rule prediction. SHA-256 `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1`.

**DEP-LEARNING: `GDR-CAND-20261010-F01-TOP-03`**, version `0.1.0`, `draft`, candidate revision `field absent; not inferred`. Archive path `selected-drafts/topics/learning-and-onboarding.md`. Inspected: Core explanation/mechanisms and application process, approximately lines 55–140: rule knowledge, access, feedback, re-entry and transfer. SHA-256 `85ab5352a60c2a7e101ee59f53e1afe4fa32834e0420a2619daa27015cdb7598`.

**DEP-UI: `GDR-CAND-20261010-P01-TOP-02`**, version `0.1.0`, `draft`, candidate revision `review-correction-1`. Archive path `selected-drafts/topics/interface-and-information.md`. Inspected: Task information contract and availability-to-recovery diagnostic, lines 55–85. SHA-256 `1381faf6c998295cd0b0472cf3905a28f87d9515d16bacb54ece423fe080595d`.

**DEP-ACCESS: `GDR-CAND-20261010-P01-TOP-03`**, version `0.1.0`, `draft`, candidate revision `review-correction-1`. Archive path `selected-drafts/topics/accessibility-and-inclusive-interaction.md`. Inspected: Applicability/scope and access chain, lines 56–103; P01 CORRECTION_RECEIPT.md. SHA-256 `eab6276ce51dcea359cb599f24ffef603b6062a6d6f6badffa8c0e28a0e79d48`.

**DEP-DECISION: `GDR-CAND-20261010-F02-TOP-01`**, version `0.1.0`, `draft`, candidate revision `initial-capture-1`. Archive path `selected-drafts/topics/decision-design.md`. Inspected: Entitled information, uncertainty, opportunity cost and reversibility, lines 63–104. SHA-256 `2fe66a5bf914a9c3f4101e168cdfd344a26eeadbfea7c45d16a9f17cca33bc6c`.

**DEP-EVALUATION: `GDR-CAND-20261010-F07-TOP-01`**, version `0.1.0`, `draft`, candidate revision `initial-capture-1`. Archive path `selected-drafts/topics/evaluation-and-balancing.md`. Inspected: Evidence-to-question distinctions, lines 65–94: correctness checks do not measure enjoyment. SHA-256 `165879841257f88c0a5ecba1f6db5d8b36089dcb260570d7bed6bcd9496d38b8`.

**DEP-ETHICS: `GDR-CAND-20261010-F07-TOP-02`**, version `0.1.0`, `draft`, candidate revision `initial-capture-1`. Archive path `selected-drafts/topics/ethical-and-sustainable-design.md`. Inspected: Representation and production obligations, lines 70–104: rules and agency are part of representation. SHA-256 `e26241cb08b1e9ddd4181e7cb92494506ae9b03e04e24032a3e9c79fe0169ce0`.

**Transfer boundary:** preserve source/candidate identities as recorded. No universal UI pixel, contrast, timing, difficulty or sample-size rule is imported. F01’s corrected feasibility/transfer discrimination is retained; access supports are not faded as tutorial prompts. Later reviewed simulation/economy/spatial-topic bytes remain missing unless explicitly identified in the packet.


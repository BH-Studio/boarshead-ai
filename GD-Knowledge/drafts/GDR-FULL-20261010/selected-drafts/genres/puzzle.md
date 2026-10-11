---
id: GDR-CAND-20261010-G10-GEN-01
kind: genre
title: Puzzle
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
attempt_identity: GDR-FULL-20261010/G10/initial-generation
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded G10 synthesis; no prior G10 artifact replaced.
owner_project: BH-GDR-Genres
run_id: GDR-FULL-20261010
batch_id: G10
updated: '2026-10-10'
evidence_checked: '2026-10-10'
date_basis: America/Los_Angeles; corresponding UTC session date 2026-10-11
coverage_state: coverage-open
aliases:
- puzzle game
- logic puzzle
- constraint puzzle
tags:
- discovery
- deduction
- manipulation
- planning
- undo
- cooperative
- hints
related_topics:
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
related_patterns:
- GDR-CAND-20261010-G10-PAT-01
- GDR-CAND-20261010-G03-PAT-02
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-P02-PAT-02
related_genres:
- GDR-CAND-20261010-G10-GEN-02
- GDR-CAND-20261010-G03-GEN-02
- GDR-CAND-20261010-G03-GEN-03
source_ids:
- GDR-SRC-20261010-G10-001
- GDR-SRC-20261010-G10-002
- GDR-SRC-20261010-G10-003
- GDR-SRC-20261010-G10-004
- GDR-SRC-20261010-G10-005
- GDR-SRC-20261010-G10-006
- GDR-SRC-20261010-G10-009
- GDR-SRC-20261010-G10-010
- GDR-SRC-20261010-G10-011
- GDR-SRC-20261010-G10-013
- GDR-SRC-20261010-G10-015
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-G10
author_self_review: completed; see batch packet
integrity_record: ../reviews/full-run-20261010-g10-integrity.md
---

# Puzzle

**Research candidate, not released guidance.** `GDR-CAND-20261010-G10-GEN-01`, version `0.1.0`, revision `initial-draft-1`. This file is a complete bounded draft, not a declaration that every puzzle tradition has been researched. Definitions are analytical conventions; proposed experience benefits remain hypotheses. The assigned scope and temporary identity come from the G10 dispatch, not permanent Library Coordination allocation.

## Definition and boundaries

Here, **puzzle** denotes a design in which reasoning about a constrained state, rule, representation or transformation is a central recurring activity. The label does not require a single solution, a single route, hidden rules, an “aha” moment, an absence of action, or an untimed solitary session. A puzzle sequence inside another genre does not automatically make that whole game a puzzle game. These are working boundaries for retrieval, not an approved universal taxonomy. [C-01]

Use five overlapping activity descriptions rather than treating all difficulty as one quantity. **Discovery** concerns finding an unknown rule, relevant action or relationship. **Deduction** concerns consequences entailed by a specified model and its premises; uncertain premises can invalidate an otherwise sound deduction. **Manipulation** concerns changing a configuration through legal actions. **Combinatorial planning** concerns selecting a sequence or construction among interacting alternatives. **Constraint insight** concerns recognizing a relation or representation that changes how the problem can be approached. A single interaction can involve several of these. These descriptions are not asserted stages of cognition. [C-01]

Distinguish a **valid end state**, a **valid route**, an **efficient route**, a **recognized answer**, and a **player’s understanding**. Multiple routes can reach a unique end state. Multiple end states can satisfy one task. A player can understand the rule yet make an execution error, or reach an accepted state without understanding the rule. A solver can certify a formal property without establishing that the property is visible or interesting to a human. [C-06, C-09, C-11]

The inspected examples challenge narrow definitions. Zachtronics describes open-ended construction and optimization in *Opus Magnum*; Hempuli’s commercial *Baba Is You* description makes rules manipulable; Steel Crate describes asymmetric cooperative communication under a timer. These are documentary examples, not observed play sessions or evidence that every audience values those structures. [C-02; GDR-SRC-20261010-G10-009; GDR-SRC-20261010-G10-011; GDR-SRC-20261010-G10-015]

**Neighboring labels.** Adventure concerns broader discovery and interaction structures; point-and-click describes an interaction tradition rather than a test for logical content. [Detective and mystery](detective-and-mystery.md) adds questions of evidence provenance, rival explanations, historical truth and accusation that are not inherent to all state-transformation puzzles. Strategy can share planning and optimization, but this entry does not establish a sharp dividing line based on complexity, length or victory conditions. Educational use is a purpose, not evidence of learning transfer. Cooperative, mobile, spatial, narrative-led and timed are facets unless a separate approved entry offers distinct guidance. [C-01, C-11; reviewed dependency ledger]

## Custom research instructions

Start each investigation with the actual decision: is the designer preserving rule discovery, practicing a known procedure, enabling open-ended construction, testing inference from evidence, or coordinating people under pressure? Do not substitute “make it harder” for that decision. Record which part of the problem is intentionally unknown and which information is legitimately available but poorly presented. [C-09, C-13]

Inspect authored examples and generator/validator descriptions separately. For generated work, distinguish existence of a solution, uniqueness under the declared equivalence relation, reachability from the initial state, availability of sufficient information, and a solver’s difficulty estimate. Ask whether the relevant property holds for all admitted instances or only inspected seeds. Do not use a generator’s success at making a solvable board as a finding about insight, enjoyment or replay variety. [C-06]

Seek contrary cases: a useful routine exercise without discovery; a timed cooperative puzzle; a construction puzzle with many valid solutions; a legitimate commitment that changes later opportunities; a help request that intentionally asks for the answer. Compare rule-changing puzzles with stable-rule puzzles without mistaking a changed rule for failed transfer. Inspect input and localization alternatives for what they reveal, not simply whether a feature exists. [C-02, C-10–C-12]

For later expansion, prioritize directly inspectable puzzle states, recordings with build and sequence locators, original generator specifications, and studies with explicit measures of reasoning or transfer. Keep wordplay, culturally specific riddles, match/clear puzzles, physical/tactile puzzles and online competitive formats on the coverage backlog rather than generalizing this small creator-document sample to them. The inaccessible learning-study lead in the packet supplies no findings. [C-14; source-access gaps]

## Player promises and varied audiences

Candidate promises include discovering a relation, applying a relation fluently, constructing a satisfying mechanism, optimizing within constraints, making a defensible inference, collaborating successfully, or taking pleasure in repeated structured activity. These are **hypotheses for audience research**, not a segmentation study or claims about all puzzle players. A player may value several, or may prefer the surrounding story and request a bypass. [C-15]

Specify the intended benefit without equating it with a convenient metric. Completion time may reflect skill, reading speed, tool use, a remembered answer or an accidental shortcut. More attempts may indicate exploration, motor difficulty or an unreadable response. Fewer hints may indicate confidence, inability to find help or reluctance to use it. The proposed diagnostic is to combine the player’s stated goal with an appropriate task observation; it does not authorize silent ability profiling. [C-11, C-14, C-15]

A completion-oriented option and a discovery-preserving option can coexist without being advertised as identical experiences. Completing after a requested reveal should not be misreported as unaided inference. Equally, an access adaptation should not be classified as solution help merely because it changes presentation or input. [C-11, C-12]

## Characteristic loops and structures

### Core, session and longer-term structures

A useful analytical loop is **inspect → form a working model → predict or plan → act → interpret the resulting evidence → retain or revise the model**. Not every game makes every step explicit, and some enjoyable repetition need not revise a model. At the session level, a player may solve a single configuration, pursue a family of related configurations, optimize an existing construction, or divide information among collaborators. Across sessions, progress may mean a richer model rather than larger numbers or more difficult boards. These are design alternatives, not a mandatory sequence. [C-01, C-13, C-15]

For a stable-rule sequence, vary irrelevant surface details separately from important relationships. For a rule-changing sequence, distinguish an intended discovery of change from an unannounced inconsistency. A level that rewards a previously wrong action because the governing rule changed is not by itself a transfer test of the old rule. Preserve that distinction when applying the corrected F01 candidate. [C-11]

### Decision matrix

| Axis | Conditional application | Cost, failure case or alternative |
|---|---|---|
| Authored / generated / mixed | Author examples when a particular conceptual contrast matters. Generate within an explicit validity contract when variation is useful. | A valid generator may produce repetitive or opaque tasks. A hand-authored instance can also be ambiguous or broken. Use a reviewed finite set or optional generation when validation is inadequate. [C-06, C-13] |
| Timed / untimed | A timer can make coordination or fluent action part of the task; separate it from pure reasoning goals. | Removing time may alter the intended challenge, while retaining it may obstruct observation or communication. Offer a differently described mode rather than claiming experiential equivalence. [C-02, C-12] |
| Undoable / committed | Use undo for exploration when restoring state is legitimate. Disclose commitment when consequences are themselves the problem. | Undo does not remove an answer from memory and cannot automatically reverse a teammate’s disclosure. A planning preview or bounded restart may fit better. [C-04, C-10] |
| Spatial / symbolic / mixed | Represent a needed relation in a form that supports the intended inference. | Turning geometry into a list may preserve facts but expose a relation; an ornamental diagram may hide a simple relation behind perception. Evaluate the particular alternative. [C-12] |
| Single-person / cooperative | Distribute knowledge or actions only when their combination is intended play. | One expert can perform all reasoning while another only executes. Group success is not evidence of each person’s understanding. [C-02, C-16] |
| Fixed goal / open optimization | Separate meeting the task’s validity conditions from improving a chosen objective. | A global leaderboard or one scalar score may hide legitimate tradeoffs. A feasible solution can be sufficient without claiming optimality. [C-02, C-09] |
| Explicit / discovered rules | State the rule when applying it is the challenge; withhold it when discovering it is the challenge. | Undisclosed exceptions can make induction underdetermined. Offer a bounded exploratory space, or disclose the limitation. [C-03, C-09] |

### A collection policy is not a genre law

Tatham’s development guide defines a particular fairness policy for inclusion in his collection, including information sufficient to avoid guessing; it separately treats uniqueness as context-dependent. That is a valuable explicit design contract, not a formal standard for all puzzles. Adopt it only when that is the intended promise. A discovery game can instead allow informative experimentation; a game of uncertainty can disclose that a guess may be unavoidable. Neither should silently advertise the stronger contract. [C-03; GDR-SRC-20261010-G10-002]

## Mechanisms, practical choices and alternatives

### 1. Name what the feedback is allowed to establish

Separate **input acknowledgment** (“the selection registered”), **rule feedback** (“that move violates an exposed condition”), **state feedback** (“the configuration changed”), **hypothesis feedback** (“this prediction conflicts with a probe”), and **solution adjudication** (“this satisfies the completion contract”). They can share presentation, but they answer different questions. A generic failure sound can obscure the difference; revealing the correct piece can collapse it. [C-07, C-09]

The evidence-to-application bridge is structural rather than a proven enjoyment effect: a deterministic checker supplies information whenever its response varies with the candidate answer. Granular feedback may help identify an error but may also support enumeration without the intended reasoning. Coarser feedback reduces some information while making a mistaken assumption harder to locate. Delaying feedback does not make a system immune to guessing. Choose among acknowledgment-only, local consistency checking, bundled validation, end-state checking and player-requested explanation after identifying which information the challenge is meant to require. [C-07]

A **no-answer-leak** promise must specify its boundary. Even naming a hidden rule, identifying which object matters, or revealing that a missing category exists can be a hint. Conversely, confirming that a selected control activated need not disclose the rule. The proposed audit compares what can be inferred before and after a response, including repeated queries; it is not a requirement to eliminate every source of useful feedback. [C-07, C-08, C-13]

### 2. Design the answer contract before enforcing one private solution

The Black Box manual describes acceptance based on indistinguishable probe results rather than exact hidden placement, and a distinguishing probe when a guess fits observations so far but not all possible probes. This is a narrow documented alternative to private-key matching. It does not justify accepting every plausible guess. [C-05; GDR-SRC-20261010-G10-003]

Use [Evidence-bounded solution acceptance](../patterns/evidence-bounded-solution-acceptance.md) when the design can explicitly bound valid alternatives. Before choosing it, distinguish equivalent wording, multiple legal constructions, histories indistinguishable under the complete allowed test set, and answers that fit only the evidence currently sampled. An exact answer can still be appropriate when a unique truth is recoverable and that recovery is the stated task. Open-ended construction may require a constraint check rather than an equivalence check at all. [C-05, C-09]

### 3. Keep generation guarantees narrower than experience claims

Tatham discusses generation by valid inverse moves and by solvers, including ways a machine’s reasoning differs from a human’s. The application is to label the actual guarantee. Reversing a legal construction path can establish a route back under those rules; it does not establish that a player knows the route or enjoys finding it. A solver whose permitted deductions are too narrow can reject acceptable instances, while an incorrect acceptance check can admit defective ones. [C-06; GDR-SRC-20261010-G10-002]

For a prospective generated collection, retain the rule version, generator version, seed where meaningful, full initial state, intended answer class, and a replayable validation witness. A seed without its generating context is not a complete reproduction record. Keep human difficulty labels provisional until tested for the relevant audience. Do not silently replace a failed case while reporting the original as validated. When generation is unreliable or costly, a reviewed authored pool is a legitimate simpler option. These are design and QA proposals, not an implemented pipeline. [C-04, C-06, C-13]

### 4. Separate recoverable state from recoverable discovery

Tatham’s common documentation and Hempuli’s jam listing describe undo/restart affordances. Those records show design possibilities; they do not establish learning outcomes. Once an answer has been shown, restoring the board does not restore the player’s earlier ignorance. An unsolved sibling problem, an explanation, or a deliberate change of goal may be preferable to replaying an exposed solution as an “unaided” test. [C-04, C-10, C-11; GDR-SRC-20261010-G10-001; GDR-SRC-20261010-G10-010]

Commitment is not inherently a defect. A constrained-use transformation, a one-shot prediction or a shared group choice can intentionally make planning matter. Disclose the commitment, distinguish legal failure from inaccessible information, and provide the agreed recovery path. If the purpose is low-pressure experimentation, an unexplained irreversible lock is harder to justify; if the purpose is consequential planning, unlimited reversal can erase part of the task. [C-10]

### 5. Adapt existing help, do not invent a new hint ladder

The reviewed G03 pattern **Player-requested state-aware hints** already owns optional help scoped to the player’s request and trustworthy state. Gilbert’s rejected target-dependent HintTron and old-save difficulties motivate two checks: can a player ask for help without knowing which object matters, and does the system actually know enough to give a reliable answer? They do not validate a universal number of tiers, a diegetic interface requirement or automated mastery inference. [C-08; GDR-SRC-20261010-G10-006]

For a discovery puzzle, offer separately described assistance such as control clarification, recap of encountered facts, an observation prompt, a relation hint, or a requested answer. Do not require the player to consume all earlier forms. For a manipulation puzzle, distinguish a dead-state warning from a full move sequence. For open optimization, show which constraint fails before recommending one construction. If state is uncertain, state the limitation and provide safe general assistance rather than a confident answer for the wrong board. These are conditional adaptations of G03, not a new G10 pattern. [C-08, C-13]

## Application process and worked example

**Illustrative design exercise, not a shipped game or performed test.** A bridge is controlled by two labeled signals, Left and Right. In the initial mode, it opens exactly when one signal is active and the other is inactive. A center ornament has no causal role. The intended discovery is the relationship between the two signals, not a prescribed click sequence. [C-13]

First, record the real rule and alternatives a player might reasonably consider: “Left is active,” “either signal is active,” “the signals differ,” or “the ornament controls the bridge.” Give legal opportunities to distinguish those explanations. Merely showing Left active/Right inactive cannot distinguish several of them. The team can keep the rule undisclosed, but should not confuse an under-informative demonstration with a demonstrated understanding of it. [C-09, C-11, C-13]

Then specify feedback and recovery. Each signal selection acknowledges its state without suggesting the correct combination. The bridge’s open/closed state is available through an appropriate alternative representation. Undo restores signal state. A help request can clarify controls without revealing the relationship, while a direct-answer request may disclose it. Record those routes separately. A scene recap reports observations the player encountered, not an unearned conclusion. [C-08, C-10, C-12, C-13]

For a proposed near-transfer check, rearrange the controls but preserve the rule and labels. Compare predictions for these cases rather than measuring only repeated clicks:

| Left | Right | Correct prediction under the initial rule | What this helps distinguish |
|---|---|---|---|
| Active | Inactive | Open | Consistent with several candidate rules; insufficient alone. |
| Inactive | Active | Open | Challenges “only Left matters.” |
| Active | Active | Closed | Challenges “any active signal is sufficient.” |
| Inactive | Inactive | Closed | Challenges indiscriminate “always open.” |

The table follows from the illustrative rule; it is not player data or a numerical standard. Include appropriate control cases and ask for a prediction or explanation in a form the participant can use. Correct answers can still reflect prior knowledge or guessing. Accommodations remain available and are not faded merely to make the test look unaided. This applies F01’s corrected discrimination principle without importing a finding of durable learning. [C-11, C-14]

Now introduce a visibly different mode whose rule is “both signals active.” This is an explicitly changed-rule problem. Repeating the earlier relation would be wrong, but that does not invalidate learning of the earlier rule. A follow-up study could examine recognizing the change or learning the new relation, and must label those outcomes separately. [C-11, C-14]

Finally, reject unnecessary machinery. If this is a brief traversal interruption and discovery is not the intended experience, explaining the rule or bypassing the bridge may be better than authoring a tutorial, generator and hint system. If it is a timed cooperative task, moving information between players may be central; a shared complete answer display would change that contract. [C-13, C-15, C-16]

## Applying shared topics and patterns

All named dependencies below were read in selected reviewed-draft bytes. They remain drafts; their underlying research was not all re-inspected in G10. Exact versions, hashes, consulted passages and historical review metadata are in the [reviewed dependency ledger](../reviews/full-run-20261010-g10-review-packet.md#reviewed-dependency-ledger). No missing dependency is replaced by an invented canonical link.

| Dependency | What this genre changes, and what it does not |
|---|---|
| `GDR-CAND-20261010-F01-TOP-03` Learning and onboarding; `GDR-CAND-20261010-F01-PAT-01` Supported attempt and transfer check | Preserve discovery where that is the chosen task; distinguish a same-rule changed situation from a changed rule. Repetition, aid use and completion are not proof of transferable understanding. |
| `GDR-CAND-20261010-F02-TOP-01` Decision design | Identify the actual unknown: rule, hidden state, legal move, future consequence or preferred optimization objective. Do not infer misunderstanding from a player choosing a different goal. |
| `GDR-CAND-20261010-P01-TOP-02` Interface and information | Separate selecting an object, representing its state and revealing its relevance. A puzzle-specific interface can be part of the task, but this does not excuse unacknowledged input. |
| `GDR-CAND-20261010-P01-TOP-03` Accessibility and inclusive interaction | Preserve the corrected distinction between scoped web standards and native-game design. No universal pixel size, reading time or timing window is imported. |
| `GDR-CAND-20261010-P02-PAT-02` Fact-preserving cue alternatives | Translate entitled facts and uncertainty, not the designer’s intended deduction. Do not claim equivalent emotional or cognitive experience from equivalent facts. |
| `GDR-CAND-20261010-G03-PAT-02` Player-requested state-aware hints | Adjust the response to discovery, manipulation or optimization needs; allow a direct answer on request and honest fallback for untrusted state. |
| `GDR-CAND-20261010-G03-GEN-02` Adventure; `GDR-CAND-20261010-G03-GEN-03` Point-and-click adventure | Keep puzzle activity distinct from knowledge/authorization gates and from an interaction-device label. These neighboring entries are not resubmitted here. |

## Representative cases, negative cases and hybrid conflicts

The documentary range includes generated logical collections, manipulable-rule play, open construction and timed asymmetric cooperation. It is deliberately not a representative market sample. Commercial success, review scores, creator prestige and player-count claims are not used to validate any recommendation. [C-02–C-06]

The strongest counterexample to mandatory discovery is a player seeking fluent repetition of a known activity. For that goal, withholding a rule or constantly changing it may be counterproductive. The strongest counterexample to mandatory reversibility is an explicitly consequential planning task. The strongest counterexample to unique-solution enforcement is a declared space of valid constructions or evidence-equivalent answers. These counterexamples constrain recommendations rather than prove the alternatives superior. [C-09, C-10, C-15]

For a puzzle–mystery hybrid, immediate per-field correctness may improve puzzle error localization while undermining uncertainty about an explanation. For a puzzle–restorative-exploration hybrid, a required timed gate can conflict with undisturbed exploration; an optional timed branch or a differently described untimed route is a candidate resolution. For cooperative puzzles, individualized hints can reveal shared answers without the group’s agreement. There is no genre label that automatically wins these conflicts. Name the player promise, the information affected and the cost of the chosen compromise. [C-07, C-12, C-16]

## Accessibility, ethics, localization and production

**Access proposal.** Test whether the intended unknown survives changes in modality and control without making already-entitled information unavailable. A spoken description of two arrows can preserve their directions; naming their hidden relationship may solve the puzzle. A shape alternative to color does not establish nonvisual access. A slower or untimed mode can remove a timing burden but must be described honestly when timing is central. Do not demand that a player disclose a diagnosis to use assistance. These are conditional inferences and proposed tests, not certification. [C-12]

**Localization proposal.** Mark symbols, word boundaries, grammar and reading order that participate in the puzzle logic. Translate the relation, not only the strings. Word length, gender agreement or list sorting can accidentally identify an answer or invalidate a clue. A newly designed local-language puzzle may be necessary, with its own validation and attribution, rather than treating equivalent string meaning as equivalent difficulty. No cross-language outcome study was inspected. [C-12, C-14]

**Production proposal.** Budget for answer classes, hint states, undo boundaries, old saves, content revisions and optional-mode differences. Store author assumptions separately from the player-facing rules. A simple authored task with reviewed responses may be preferable to automatic hints whose state cannot be trusted. Technical validation and human review solve different problems; neither replaces the other. [C-06, C-08, C-13]

**Ethics and cooperation proposal.** Avoid shaming language that conflates assistance with lack of intelligence. Distinguish team completion from individual learning; offer roles and help negotiation without assuming speech, hearing, rapid reading or confident participation. Keep private test notes and any volunteered access needs outside public content packs. None of these proposed accommodations has been validated for this genre sample. [C-12, C-16]

## Research questions and proposed validation

**All protocols below are proposed and not performed.** No participants, builds, telemetry, prototypes or gameplay efficacy results were produced. Use consent, appropriate access options and a locally justified sampling plan; this entry supplies no universal sample size or pass threshold. Before collecting data, declare the primary outcome and what difference would change the local design decision. [C-14]

| Discriminating question | Comparison and procedure | Measures, confounds and rejection condition |
|---|---|---|
| Does granular checking teach the intended relation or enable answer enumeration? | Compare matched problem families with local validation, coarser validation and requested explanation; counterbalance fresh instances, not previously exposed answers. | Code predictions/explanations and query sequences as well as completion. Prior skill, vocabulary and exposure matter. Reject the learning claim if advantage is confined to checked answers or a changed-surface test shows no relevant understanding. |
| Does an observation hint preserve more desired discovery than direct instruction? | Let participants state their help goal; compare assistance routes within that goal rather than naïvely comparing help users with nonusers. | Record unwanted disclosures, whether the offered help addressed the blockage, and later reasoning. Reject the tiered design if its extra steps only delay the requested answer or reveal an unwanted goal. |
| Do generated instances meet the human-facing contract? | After separate formal validity review, examine sampled instance families, including boundary cases, with intended audiences. Retain generator/version/state. | Separate inaccessible clues, unrecognized rules, exhaustive search burden and invalid instances. Any unsupported validity guarantee requires correction; preference results do not repair a broken validator. |
| Does undo support useful exploration in this task? | Compare undo, planning preview and disclosed commitment with equivalent content and appropriately different goal descriptions. | Record predictions and reversals, frustration and perceived consequence. Reject a universal undo recommendation if it removes the intended planning tradeoff; do not infer “no learning” from reversals alone. |
| Does the group structure permit intended participation? | Rotate agreed roles and compare information distributions using accessible communication routes. | Observe who interprets, decides and executes; use individual follow-up only with consent. Reject “everyone reasoned” when only team completion supports it. |

## Claim ledger

Local claim IDs are scoped to this file. Confidence refers to the wording below, not to the commercial quality of a cited game. `D` in a support cell means the inspected reviewed dependency ledger, not direct reinspection of its underlying sources.

| ID | Precise claim / classification | Support and contrary case | Confidence, scope and unresolved question |
|---|---|---|---|
| C-01 | The operational definition and five activity distinctions are a useful proposed partition, not a universal taxonomy. `inference` | G10 brief and taxonomy; D: G03 genre boundaries. | Moderate as a transparent analytic convention; taxonomy ownership and broader traditions remain open. |
| C-02 | Inspected product descriptions include open construction, mutable rules and timed asymmetric cooperation. `observed-example` | 009 About; 015 About This Game; 011 About. | High for the documentary descriptions, low for any population/effect extension; no gameplay inspected. |
| C-03 | Tatham’s no-guess fairness and context-dependent uniqueness are collection-specific practitioner policies. `practitioner-heuristic` | 002 §6.1; timed/discovery alternatives are outside that policy. | High that the author states them; no universal normative authority. |
| C-04 | Inspected documentation describes undo/restart and version-sensitive reproduction identifiers. `observed-example` | 001 §§2.1–2.2; 010 controls. | High documentary confidence; actual current builds and persistence not tested. |
| C-05 | Black Box documents output-equivalent acceptance and distinguishing feedback beyond observations already made. `observed-example` | 003 Chapter 19 and §19.1. | High for this manual; no claim that an arbitrary plausible answer is accepted. |
| C-06 | Formal generation/solver guarantees and human-facing difficulty are different properties. `inference` | 002 §6.2.1 supplies methods and practitioner cautions; formal implication does not entail a player outcome. | High for logical distinction; low for which generator produces preferred experiences. |
| C-07 | Feedback granularity creates information/recovery tradeoffs; delayed or bundled checking is not logically guess-proof. `inference` | 003 §19.1; 004 Fate Validation and reply #740; 013 validation discussion. | High for possibility of information leakage, low for its behavioral prevalence or preferred setting. |
| C-08 | Conceptual help and old-save state can defeat apparently useful hint interfaces. `practitioner-heuristic` | 006 HintTron and old-save passages; D: G03-PAT-02. | Moderate contextual evidence; full hint-pattern efficacy not established. |
| C-09 | Separate hidden state, rules, legal actions, accepted answers and preferred outcomes when choosing a puzzle contract. `inference` | D: F02-TOP-01 and P01-TOP-02; 003; 009. | Moderate design rationale; no universally optimal amount of disclosure. |
| C-10 | Restoring state cannot guarantee restoration of ignorance; commitment and undo should follow the intended task. `inference` | 001 mechanisms; 005 historical advice; contrast a deliberately consequential task. | High for the knowledge/state distinction; preferred recovery policy remains local. |
| C-11 | Repetition, completion and aid use do not by themselves establish learned transfer; a changed rule is a different test. `inference` | D: F01-TOP-03 and corrected F01-PAT-01. | High for measurement non-equivalence; no G10 evidence of durable or far transfer. |
| C-12 | Information-preserving access needs task-specific spoiler, input and localization audits; numerical web guidance is not a native-game universal. `inference` | D: corrected P01-TOP-03 and P02-PAT-02; 006. | Moderate rationale, low untested experiential parity; locale and access-population evidence missing. |
| C-13 | The proposed diagnose–contract–feedback–help–recovery process may improve fit to an intended puzzle promise. `hypothesis` | Bridges C-03–C-12; worked example is illustrative. | Low; full process not compared or implemented. Omit machinery when unnecessary. |
| C-14 | The proposed discriminating protocols could separate several plausible explanations of performance. `hypothesis` | C-07, C-11 and explicit alternative explanations. | Low until protocol review and execution; no thresholds, power or results claimed. |
| C-15 | Discovery, fluency, construction, interpretation and repeated structured play are candidate audience goals, not homogeneous expectations. `hypothesis` | Range of documentary cases plus declared audience questions. | Low as an untested audience model; no segmentation dataset. |
| C-16 | Cooperative information and help should be evaluated for participation, not only team completion. `hypothesis` | 011’s described asymmetry; C-11 measurement distinction. | Low for particular interventions; roles, communication routes and audience require testing. |

## Coverage, review and history

Researched at documentary/inference depth: the five activity distinctions; authorship/generation; time, commitment, space and cooperation facets; feedback, answer contracts, optional help, recovery, near-transfer measurement and accessibility implications. Open: actual build observations, controlled puzzle-learning evidence, cross-cultural/wordplay coverage, tactile interfaces, long-term learning, online competition, generator benchmarks and full proposed-pattern efficacy. The source ledger does not turn these absences into negative findings.

Conflicts remain open as `G10-CON-01` (uniqueness), `G10-CON-02` (feedback versus answer leakage), `G10-CON-03` (access versus intended discovery), `G10-CON-04` (formal validity versus understanding) and `G10-CON-06` (commitment versus recovery). They are local review keys, not permanent register IDs. See the [contradiction register](../reviews/full-run-20261010-g10-review-packet.md#contradiction-register).

Initial draft on 2026-10-10 Pacific date. Author self-review challenged the strongest recommendations; no independent G10 review has occurred. All approval fields remain null. No previous G10 artifact is superseded. Exact final bytes are identified by the detached [integrity receipt](../reviews/full-run-20261010-g10-integrity.md); the file does not claim a self-referential embedded hash. Gate C review and actual-host Gate D tests remain pending; no Gate E release or game adoption is implied.

## References

All access dates: **2026-10-10, America/Los_Angeles** (retrieval session falls on 2026-10-11 UTC). Section names are portable locators; line ranges describe the inspected web-text rendering, not immutable publisher numbering. `observed-example` claims concern a documentation artifact unless explicitly stated otherwise. No game build was run. Source aliases are temporary; global deduplication is pending.

### GDR-SRC-20261010-G10-001

**Simon Tatham and Portable Puzzle Collection contributors. [Common features, Chapter 2](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/common.html).** Simon Tatham’s Portable Puzzle Collection. Date: Publication/update date unknown; inspected documentation version shown below.

**Edition/build:** Documentation footer 20260923.616da16; no corresponding binary run. **Access:** `relevant-excerpt`. **Type:** Primary product documentation. **Inspected locator:** §2.1: Undo, Redo, Restart, Save and Solve; §2.2: descriptive IDs and random seeds; §2.3: parameters. Retrieved text lines 17–67.

**Limits and independence:** Mechanisms described in documentation, not verified in a running game. Reversible state is not reversible knowledge. Seed compatibility is version-dependent. Source family: Tatham. Ancillary contents/license page inspected: https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/. No code or manual extracts redistributed.

**Rights:** Copyright retained by the source owner; only attributed paraphrase and bibliographic metadata are supplied. Claims supported are identified in this entry’s ledger; a listed lead supports no substantive claim.

### GDR-SRC-20261010-G10-002

**Simon Tatham. [How to write a new puzzle, Chapter 6](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/devel/writing.html).** Simon Tatham’s Portable Puzzle Collection. Date: Publication/update date unknown.

**Edition/build:** Documentation footer 20260923.616da16; collection-specific editorial policy. **Access:** `relevant-excerpt`. **Type:** Firsthand technical design advice. **Inspected locator:** §6.1 Choosing a puzzle, especially paragraphs on hidden information and uniqueness; §6.2.1 Puzzle generation, inverse moves, solver differences, ambiguity and false positives. Retrieved lines 24–37, 46–88.

**Limits and independence:** The author explicitly calls this advice. Fairness is a policy of this collection, not a formal standard or requirement for all puzzles. Solver correctness and player experience remain separate. Source family: Tatham. 

**Rights:** Copyright retained by the source owner; only attributed paraphrase and bibliographic metadata are supplied. Claims supported are identified in this entry’s ledger; a listed lead supports no substantive claim.

### GDR-SRC-20261010-G10-003

**Simon Tatham and contributors; Black Box contribution credited to James Harvey. [Black Box, Chapter 19](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/blackbox.html).** Simon Tatham’s Portable Puzzle Collection. Date: Publication/update date unknown.

**Edition/build:** Documentation footer 20260923.616da16; no binary or board-game edition played. **Access:** `relevant-excerpt`. **Type:** Primary product documentation. **Inspected locator:** Chapter 19, non-unique layouts and acceptance paragraph; §19.1, check feedback and distinguishing untried beams; §19.2, permitted ball-count variations. Retrieved lines 29–55, 63, 66.

**Limits and independence:** Documentary example only. Matching already-observed probes is not enough when another legal probe distinguishes the layouts. No efficacy experiment. Source family: Tatham. 

**Rights:** Copyright retained by the source owner; only attributed paraphrase and bibliographic metadata are supplied. Claims supported are identified in this entry’s ledger; a listed lead supports no substantive claim.

### GDR-SRC-20261010-G10-004

**Lucas Pope; separately attributed reader reply by mtarini. [TIGSource — August 2017: Return of the Obra Dinn development log](https://dukope.com/devlogs/obra-dinn/tig-30/).** Development Logs by Lucas Pope; creator-hosted mirror of TIGSource. Date: Pope post #734: 2017-08-11; mtarini reply #740: 2017-08-21.

**Edition/build:** Development snapshot; exact executable build unknown, not evidence of every retail version. **Access:** `relevant-excerpt`. **Type:** Firsthand developer account with a separately identified analytical reader objection. **Inspected locator:** Post #734: Fate Validation and SVO Fates; problem/fix discussion preceding them. Reply #740: cycling a third answer after two known ones. Retrieved lines 20–103 and 146–160.

**Limits and independence:** Small informal observations, no exposed comparative dataset. Group validation is not proof against guessing. Alternative descriptions concern accepted fate formulations, not unrestricted alternative histories. Source family: Pope. Mirror and original discussion are one underlying account, not two independent sources. The reader objection is not attributed to Pope and is not a performed exploit test.

**Rights:** Copyright retained by the source owner; only attributed paraphrase and bibliographic metadata are supplied. Claims supported are identified in this entry’s ledger; a listed lead supports no substantive claim.

### GDR-SRC-20261010-G10-005

**Ron Gilbert. [Why Adventure Games Suck / Why Adventure Games Suck And What We Can Do About It](https://grumpygamer.com/why_adventure_games_suck/).** Grumpy Gamer, author website. Date: 1989 original essay; 2004-05-12 republication and retrospective preface.

**Edition/build:** Historical essay in later author wrapper; no game build. **Access:** `relevant-excerpt`. **Type:** Firsthand practitioner essay. **Inspected locator:** 2004 preface; Live and learn; I forgot to pick it up; Arbitrary puzzles; Reward Intent; Give the player options. Retrieved lines 21–26, 53–63, 74–90.

**Limits and independence:** The later preface qualifies the older advice. No universal ban on time, failure or irreversibility follows. Not a player-population study. Source family: Gilbert. Exact-URL overlap inspected with GDR-SRC-20261010-G03-001; retain both temporary aliases pending Coordination reconciliation.

**Rights:** Copyright retained by the source owner; only attributed paraphrase and bibliographic metadata are supplied. Claims supported are identified in this entry’s ledger; a listed lead supports no substantive claim.

### GDR-SRC-20261010-G10-006

**Ron Gilbert. [Dialogs, Hints and more...](https://blog.thimbleweedpark.com/hints_and_dialogs.html).** Official Thimbleweed Park development blog. Date: 2017-06-20.

**Edition/build:** Build 1388.918 update account; old saves explicitly problematic; no build run. **Access:** `relevant-excerpt`. **Type:** Firsthand implementation and failure account. **Inspected locator:** HintTron rejection, optional HintLine and old-save state limitations; paragraphs crediting Jenn and Meghann O’Neill. Retrieved lines 10, 20–44.

**Limits and independence:** Creator experience, no validated help-effect estimate. A target-dependent interface can fail conceptual help needs; state reconstruction remains fallible. Source family: Gilbert. Exact-URL overlap inspected with GDR-SRC-20261010-G03-007. The post credits permission-based adaptation of Meghann O’Neill’s hints; this is not independent corroboration from two hint systems.

**Rights:** Copyright retained by the source owner; only attributed paraphrase and bibliographic metadata are supplied. Claims supported are identified in this entry’s ledger; a listed lead supports no substantive claim.

### GDR-SRC-20261010-G10-009

**Zachtronics. [Opus Magnum](https://www.zachtronics.com/opus-magnum/).** Zachtronics. Date: Publication/update date unknown.

**Edition/build:** Unnumbered product page; executable build unknown. **Access:** `relevant-excerpt`. **Type:** Primary developer product description. **Inspected locator:** About, paragraphs describing open-ended machine construction and optimization. Retrieved lines 22–26.

**Limits and independence:** Documents the advertised form; no level played, user-outcome test or optimal design recommendation established. Source family: Zachtronics. 

**Rights:** Copyright retained by the source owner; only attributed paraphrase and bibliographic metadata are supplied. Claims supported are identified in this entry’s ledger; a listed lead supports no substantive claim.

### GDR-SRC-20261010-G10-010

**Hempuli. [Baba Is You (Jam Build)](https://hempuli.itch.io/baba-is-you).** Hempuli on itch.io. Date: Nordic Game Jam 2017 context; page metadata updated 2026-09-16 08:11 UTC.

**Edition/build:** Explicitly Jam Build; Windows listing; binary revision unknown. **Access:** `relevant-excerpt`. **Type:** Primary creator-hosted game listing. **Inspected locator:** Title, introduction, controls listing Undo/Restart, and jam context. Retrieved lines 11–24, 38–45.

**Limits and independence:** Jam prototype is not the commercial build. Page-update timestamp does not establish executable revision. No play or download performed. Source family: Hempuli. 

**Rights:** Copyright retained by the source owner; only attributed paraphrase and bibliographic metadata are supplied. Claims supported are identified in this entry’s ledger; a listed lead supports no substantive claim.

### GDR-SRC-20261010-G10-011

**Steel Crate Games. [Keep Talking and Nobody Explodes](https://keeptalkinggame.com/).** Steel Crate Games. Date: Publication/update date unknown; footer copyright is not treated as publication date.

**Edition/build:** Unnumbered official page; exact platform/build not selected or run. **Access:** `relevant-excerpt`. **Type:** Primary developer description. **Inspected locator:** About: separate defuser/manual-expert information, communication and timer; listed genres; procedural/freeplay descriptions. Retrieved lines 48–56, 73–79, 90–103.

**Limits and independence:** Advertised asymmetric cooperative format is a counterexample to a solitary/untimed-only definition, not proof of universal accessibility or fresh/enjoyable generation. Manual and game were not inspected. Source family: Steel Crate. 

**Rights:** Copyright retained by the source owner; only attributed paraphrase and bibliographic metadata are supplied. Claims supported are identified in this entry’s ledger; a listed lead supports no substantive claim.

### GDR-SRC-20261010-G10-013

**Joel Couture interviewing Andrejs Klavins, Color Gray Games designer. [Pursuing the “Aha!” moment with deductive reasoning game The Case of the Golden Idol](https://www.gamedeveloper.com/design/case-of-the-golden-idol).** Game Developer. Date: 2022-11-01.

**Edition/build:** Original interview about the released design; exact executable build unknown. **Access:** `relevant-excerpt`. **Type:** Original firsthand designer interview. **Inspected locator:** Klavins answers on narrative/puzzle coherence, constrained answer phrasing, partial validation, clue revision and misleading inferences. Retrieved lines 44–92, especially 54–65 and 83–88.

**Limits and independence:** Designer reports qualitative iteration outcomes without a controlled dataset. Introductory praise is not used as evidence. Obra Dinn is acknowledged as an influence, not an independent replication. Source family: Color Gray Games. 

**Rights:** Copyright retained by the source owner; only attributed paraphrase and bibliographic metadata are supplied. Claims supported are identified in this entry’s ledger; a listed lead supports no substantive claim.

### GDR-SRC-20261010-G10-015

**Hempuli Oy / Arvi Teikari. [Baba Is You](https://store.steampowered.com/app/736260/Baba_Is_You/).** Developer-supplied Steam store page. Date: Release listed as 2019-03-13; page update date unknown.

**Edition/build:** Commercial product description; exact binary version unknown. **Access:** `relevant-excerpt`. **Type:** Primary developer product description. **Inspected locator:** About This Game, first paragraphs on movable rules and altering interactions/goals; developer attribution. Retrieved lines 187–192, 230.

**Limits and independence:** Separate document from the jam listing, same creator. No level, storefront review statistic or current runtime behavior is used as effect evidence. Source family: Hempuli. 

**Rights:** Copyright retained by the source owner; only attributed paraphrase and bibliographic metadata are supplied. Claims supported are identified in this entry’s ledger; a listed lead supports no substantive claim.


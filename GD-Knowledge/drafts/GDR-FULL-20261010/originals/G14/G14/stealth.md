---
id: GDR-CAND-20261010-G14-GEN-02
kind: genre
title: Stealth
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
- stealth game
- infiltration
- evasion
tags:
- detection
- suspicion
- search
- information-asymmetry
- recovery
- nonviolent-commitments
related_topics:
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-P01-TOP-03
related_patterns:
- GDR-CAND-20261010-G14-PAT-01
- GDR-CAND-20261010-P02-PAT-02
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-W02-PAT-02
related_genres:
- GDR-CAND-20261010-G14-GEN-01
- GDR-CAND-20261010-G14-GEN-03
source_ids:
- GDR-SRC-20261010-G14-002
- GDR-SRC-20261010-G14-003
- GDR-SRC-20261010-G14-004
- GDR-SRC-20261010-G14-009
- GDR-SRC-20261010-G14-010
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
---

# Stealth

**Draft 0.1.0, not released guidance.** This entry helps select a detection, inference and recovery contract: what an observer can establish, how the player can reason about it, and what happens after discovery. It does not require literal sensory realism, mandatory violence, universal restart rules, or maximal uncertainty. [C-01, C-08]

## Definition and boundaries

**Working definition — inference:** stealth foregrounds controlling exposure, avoiding or manipulating detection, and acting under asymmetric information about observers, space and time. Concealment can be an ongoing strategic resource, a short encounter tactic, or a strict mission requirement. A single crouch button or hidden-state indicator does not establish that this is the game’s organizing activity. [C-01]

Separate **visibility** (a potential sensory input), **detection** (what an observer establishes), **suspicion** (a response to incomplete evidence), **search** (actions taken to resolve uncertainty), and **alertness** (an operational posture that can persist after contact is lost). These are this draft’s analytic terms, not mandatory implementation states or a universal state machine. A global alarm, one guard’s knowledge and the player’s knowledge can diverge. [C-08]

| Neighbor / facet | Retrieval boundary | Design consequence |
|---|---|---|
| Immersive simulation | Manipulating observers can be one interacting system among many. | Preserve goal and method permissions; do not assume every stealth game needs open-ended simulation. |
| Tactical combat | Surprise and concealment may support combat rather than replace it. | A discovery-to-combat transition must be evaluated against the mode’s stated commitments. |
| Survival | Avoidance can conserve resources and time. | Being unseen may still be too costly in exposure, food or return capacity. |
| Puzzle / precision / score attack | Learning a repeatable solution can be the intended task. | Deterministic patrols and quick restarts may support that task; they are not inherently defective stealth. |
| Social disguise / hiding in public | Suspicion can depend on identity, permission and behavior, not darkness alone. | This corpus does not establish a complete disguise model; queue that evidence instead of generalizing from guard vision. |
| Real-time / discrete-time, solo / cooperative | Timing and social coordination facets. | Deliberative stealth is an illustrative possibility here; the inspected Klei support passage does not itself establish a turn-based classification. |

These distinctions are proposed for retrieval and testing, not a final settlement of genre membership. [C-01, C-11]

## Custom research instructions

For every future observation, record **whose knowledge is being described**. Trace sensory event, identity certainty, last supported location, communication between observers, search behavior, reacquisition and persistent consequences. A player leaving a view cone is not proof that the observer forgot; a search bark is not proof that all agents received the same information. [C-08]

Compare a recovering evasion, an exacting no-detection challenge and a more permissive infiltration. Include sound-off or alternate-cue play and a case in which the player intends to avoid harm. Seek failed and rejected AI approaches, not only successful trailers. Current sources cover selected Western developer accounts and one research prototype; disguise, animal senses, cooperative stealth, cultural interpretation and long-term mastery remain gaps. [C-11, C-13]

Do not conflate **never detected**, **no alarm**, **no killing**, **no injury**, **no coercion** and **no collateral harm**. An objective or achievement may impose one without promising the others. Creator claims need a build-specific end-to-end check before being upgraded to observed completion evidence. [C-04, C-10]

## Player promises and varied audiences

Possible promises include planning a route from observable behavior, recovering after a plan breaks, remaining undetected, controlling violence, and executing a practiced sequence. Their priority and desirability are **audience hypotheses**, not universal expectations. A player can prefer perfect patrol knowledge for tactical planning or prefer uncertainty about an unseen observer; neither preference alone demonstrates misunderstanding. [C-09]

For nonviolent play, define the actual constraint before tuning recovery. A forced takedown might satisfy “no killing” while violating “do not harm anyone.” Conversely, a mode explicitly built around a dangerous escape need not pretend all approaches remain possible. The reusable obligation is to align the promise, available actions and acknowledgement—not to impose one ethical or difficulty model on every game. [C-10]

## Characteristic loops and structures

The analytical loop is **observe → predict exposure → commit → interpret response → continue, withdraw or recover**. Real-time execution, turn-based planning, scripted timing and systemic search allocate demands differently. At session scale, the objective might tolerate suspicion but prohibit alarms. At longer horizons, an infiltration might consume tools, change access or endanger a team. These structures are proposed distinctions, not claims that every game contains them. [C-01, C-08]

Leonard’s Thief retrospective describes using sounds and barks to make AI states interpretable and reports problems in its AI development. The Mark of the Ninja retrospective instead emphasizes strong readability, including binary hidden/illuminated presentation. **That binary lighting choice is not evidence of a binary search or knowledge model.** Both are practitioner accounts, not rival experimental proofs of the best state count. [C-02; GDR-SRC-20261010-G14-002] [C-03; GDR-SRC-20261010-G14-003]

### Distinguish the questions before choosing states

| Diagnostic situation | Question to answer | A conditional alternative |
|---|---|---|
| Noise without an identified source | Does the observer know a person is present, or only that something happened? | Investigate a place without declaring a confirmed identity. |
| Confirmed contact then broken sight | What evidence persists, and what could update it? | Search a supported area, retain a heightened posture, or use an explicitly disclosed tracking power. |
| Another agent receives a report | What was actually transmitted and when? | Share a last-known area rather than silently distributing exact live position. |
| Player hears an ambiguous bark | Is it a state cue, a character guess, or an intentional bluff? | Preserve the distinction in captions and other alternative representations. |
| Mission continues after discovery | Which commitments and future actions remain feasible? | Escape, concealment, negotiation, retry or a declared failure—not automatically combat. |

This is a diagnostic inference, not an implemented algorithm. More states can add ambiguity without useful decisions; fewer states can erase distinctions the player needs. Choose only distinctions the intended activity can communicate and use. [C-08, C-12]

### Bounded empirical evidence

Al Enezi and Verbrugge studied **154 completers**, recruited mainly from university students: 72 compared heuristic/cheating search and 82 heuristic/random search. Four randomized-order episodes combined behavior and dialogue conditions in a globally visible top-down prototype. Participants selected their most enjoyable and difficult team afterward. The heuristic-versus-cheating enjoyment contrast was reported as significant (χ² = 22.22, df = 1, p < .001). This is narrow evidence about that task, not proof of a general dialogue benefit or equivalent experiences. [C-06; GDR-SRC-20261010-G14-012]

**Reporting caveat:** Table 5 prints χ² = 1.21 with p = .26 for one comparison and p = .01 for another. No correction or raw-data reanalysis was obtained. Do not silently repair the table or use its contextual-dialogue claim as settled evidence. The paper’s equivalence language is not an equivalence test. [C-07; GDR-SRC-20261010-G14-012]

### Conditional application process

1. State the target activity and forbidden outcomes. Is the aim to remain unobserved, avoid a persistent alarm, evade pursuit, protect a team or preserve a nonviolent commitment? Keep preference and rule compliance separate. [C-10]
2. Define the permitted information flow: observations, memory, reports, environmental clues and any exceptional tracking ability. List what is visible to the player and what must be inferred. Do not assume that exact cones are always required or always harmful. [C-08]
3. Prototype the smallest state distinctions that support those decisions. Author a successful concealment, an ambiguous stimulus, confirmed contact, broken contact and reacquisition. Vary whether the correct inference changes; identical outcomes under new decoration do not test transfer. [C-08, C-12]
4. Audit spatial and temporal escape feasibility under the supported input and information configurations. A displayed escape opportunity that closes before a supported input route can act is not the same problem as strategic uncertainty. No universal reaction time is supplied here. [C-12]
5. Compare continuing recovery with checkpoint restart where both fit the promise. Record decision quality and desired experience separately from survival, completion time or score. A recovery branch that becomes compulsory combat can violate the tested premise. [C-09, C-10]
6. Remove distinctions or systems that cannot be expressed reliably, or explicitly narrow the promise. Do not increase guard complexity simply to compensate for indistinguishable behavior. This last recommendation remains a local hypothesis, not a conclusion proved by the study. [C-13]

## Applying shared topics

| Inspected shared draft | Genre-specific adaptation |
|---|---|
| [Decision design — GDR-CAND-20261010-F02-TOP-01](../reviews/full-run-20261010-g14-review-packet.md#dep-decision) | Keep hidden observer state separate from missing access to facts the design intends to expose. Distinguish predicting detection from preferring a risk. |
| [Challenge and difficulty — GDR-CAND-20261010-F02-TOP-02](../reviews/full-run-20261010-g14-review-packet.md#dep-challenge) | Tune perception, planning, timing, accumulated costs and recovery separately; lowering damage may not address a missing directional cue. |
| [Accessibility — GDR-CAND-20261010-P01-TOP-03](../reviews/full-run-20261010-g14-review-packet.md#dep-access) | Evaluate the entire route to setting up, learning, executing and recovering from stealth actions. Preserve scoped guidance; no WCAG or XAG numerical values are generalized. |

Only the inspected analytical passages transfer. No underlying shared-topic study result is imported as independent support. Level/spatial design, dialogue systems, systemic behavior, movement and relevant later combat guidance remain requested dependencies, not established local transfers. [C-12, C-13]

## Pattern selection and adaptations

[Evidence-bounded search and reacquisition](../patterns/evidence-bounded-search-and-reacquisition.md), `GDR-CAND-20261010-G14-PAT-01`, is the new hypothesis-led recipe for deciding what search may legitimately use and how contact can be lost and re-established. It is not a demand that all agents operate without designer assistance. Its explicit counterexample is the published Thief implementation, which includes privileged knowledge and a special backward-sensitive cone. [C-05, C-08]

Reuse [Fact-preserving cue alternatives — GDR-CAND-20261010-P02-PAT-02](../reviews/full-run-20261010-g14-review-packet.md#dep-cues) for modality changes and [Supported attempt and transfer check — GDR-CAND-20261010-F01-PAT-01](../reviews/full-run-20261010-g14-review-packet.md#dep-transfer) for rule discrimination. These address presentation and learning; they are not duplicates of search permissions. Reuse [Multi-route objective contract — GDR-CAND-20261010-W02-PAT-02](../reviews/full-run-20261010-g14-review-packet.md#dep-objective) to distinguish mission completion from optional no-harm conditions. [C-10, C-12]

The audio pilot’s contextual benefit is still a low-confidence hypothesis. A correctly recognized suspicious sound does not establish fear, anticipation or improved stealth decisions. Captions need not produce identical emotional responses to fulfill an information-access goal. [C-12]

## Representative cases and negative cases

The selected cases are **documentation and creator accounts**, not G14 gameplay observations. The Mark interview discusses intended non-kill completion and optional detection-related achievements; these are different commitments and were not end-to-end verified here. Klei’s Invisible, Inc. support article describes team infiltration, build choices, generation and modes, but its claim that variation prevents complacency is promotional, not a result adopted by this entry. [C-04; GDR-SRC-20261010-G14-004] [C-11; GDR-SRC-20261010-G14-010]

### Illustrative worked example: retrieve a document without harming staff

A fictional archive has a corridor, a screened reading room and two attendants. The player’s declared constraint is no harm. An attendant hears a dropped case but has not identified the player. That cue may cause a corridor inspection; it must not silently count as confirmed player identity. After a later sighting, breaking sight removes live visual evidence but does not imply that the attendant has forgotten the intrusion. A second attendant receives only the stated report. [C-08, C-10]

The player can wait behind a screen, leave through a permitted exit, return a misplaced item to create a legitimate explanation, or abandon the attempt. These options are illustrative and depend on the game’s actual permissions; they are not claims that all stealth games should support social explanations. A caption identifying an unseen attendant’s exact destination would change the information policy if the original cue only communicated suspicion. [C-08, C-12]

**Negative design case:** in a separately advertised no-detection score challenge, contact ends the attempt and a rapid restart may be desirable. Adding an elaborate search recovery could dilute that activity. In a suspense-oriented infiltration, repeatedly restarting before any changed state develops could instead erase the intended uncertainty. Neither claim is universal; ask which activity the player selected. [C-09]

## Accessibility and production implications

**Access proposal:** inspect hold/toggle demands, precise aiming at interaction targets, simultaneous observation and movement, localized room names, cue overlap and whether important state can be reviewed without losing the opportunity to act. Provide alternatives for critical information, not merely a decorative icon accompanying an uncaptioned essential sound. Preserve access supports independently of performance. [C-12]

**Production inference:** the relevant cost is not only AI computation. Evidence propagation, stale reports, save/reload, synchronized actors, animation cues and localized dialogue can disagree about state. Author explicit tests for contradiction and for unavailable routes. If individual assists affect shared stealth, define the shared information and consequence policy with the participating players; do not silently promise both secrecy and universal information. [C-08, C-13]

**Ethical constraint to investigate:** fear, surveillance and violence preferences require consent-sensitive evaluation. Do not equate enduring distress with skill, or describe players choosing assistance as less authentic. Check whether the purported nonviolent path entails unwanted coercion or harm; resolve the promise rather than relabeling the outcome afterward. [C-10, C-13]

## Research questions and validation

**Proposed only; no study was run by G14.** Compare a limited, traceable search model with a simpler deterministic alternative and, only where appropriate, a clearly disclosed omniscient threat. Match level topology, movement opportunities and required objective; treat search competence and cue detail as separate variables rather than changing both unnoticed. [C-13]

Use matched probes in which an observer heard a noise but did not see a person, saw the person then lost contact, or received a specific report. Include a case where reacquisition is legitimately possible and one where it is not. Ask for predictions before feedback and record explanations or equivalent accessible responses. Preference for escape, combat or restart is a separate outcome from correct knowledge prediction. [C-08, C-12]

Recruit both practiced stealth players and newcomers with the supported access configurations. Measures include knowledge attribution errors, successful recovery without violating the chosen commitment, opportunity to act, repeated-state monotony, desired suspense and perceived arbitrariness. Confounds include map familiarity, actual difficulty, route geometry, more informative dialogue, and prior exposure. Do not equate better score with greater enjoyment or claim that a finite trial verifies all nonviolent paths. [C-13]

**Reject/adapt criterion:** predefine with the local team the level of misunderstanding or unavailable recovery that defeats the promised activity. Reject the proposed model when participants cannot distinguish its actionable states even after accessible instruction, or when the simpler alternative better delivers the chosen goal at acceptable cost. Specify practical margins and recruitment before testing; no evidence here supplies a universal timeout, sample size or success rate. [C-13]

## Claim ledger

| Claim | Precise proposition / class | Source or dependency locator | Confidence / limitation |
|---|---|---|---|
| C-01 | Stealth is routed here by exposure and asymmetric-information decisions, with varied timing and failure contracts. `inference` | Sources 002–004; own working scope. | Moderate for useful routing; not a formal definition. |
| C-02 | Thief’s retrospective discusses readable sound states and AI production failures. `practitioner-heuristic` | Source 002, Sound and AI sections. | Moderate; creator explanation, not causal validation. |
| C-03 | Mark’s cited simplification concerns hidden/illuminated presentation. `practitioner-heuristic` | Source 003, What Went Right §5. | High for the specific account; does not specify the entire knowledge model. |
| C-04 | The interview separates intended no-kill completion from achievement conditions. `practitioner-heuristic` | Source 004, questions at HTML 29–36. | High for stated intent; shipped run not verified. |
| C-05 | The documented Thief sensory system includes designed information privileges. `practitioner-heuristic` | Source 009, Viewcones and Awareness Pulses. | High for the account; necessity or superiority unproven. |
| C-06 | The cited prototype study reports a limited enjoyment-preference contrast. `empirical-evidence` | Source 012, pp.167–172, Figure 7. | Moderate for narrow reported result; task and recruitment limit transfer. |
| C-07 | The table discrepancy and absence of an equivalence analysis constrain interpretation. `inference` | Source 012, Table 5 and conclusion, p.173; visually checked. | High for printed discrepancy; its correction is unknown. |
| C-08 | Evidence, awareness, search and alertness should be analyzed separately before choosing a model. `hypothesis` | Sources 002/009 plus DEP-DECISION; own illustrative model. | Low for experience benefit; alternatives remain legitimate. |
| C-09 | Recovery and reset can serve different intended activities. `hypothesis` | DEP-CHALLENGE; own comparison design. | Low; no universal preference or tension effect established. |
| C-10 | Non-detection, non-killing and non-harm promises require separate constraints and recognition. `inference` | Source 004; DEP-OBJECTIVE; logical distinctions. | Moderate for distinction; actual paths require verification. |
| C-11 | The available case range does not establish generation benefits or complete subgenre coverage. `observed-example` | Source 010, artifact-only; access ledger. | High for documentation scope; no freshness effect claimed. |
| C-12 | Preserve actionable information and changed-answer transfer checks without equating access and difficulty. `inference` | DEP-CUES 52–99; DEP-TRANSFER 99–118; DEP-ACCESS 52–100; DEP-PILOT-T 26–34. | Moderate for scoped application; no live access/learning test here. |
| C-13 | Proposed design, access and evaluation decisions remain locally testable rather than universal. `hypothesis` | Bridge from C-06–C-12; proposed study and local production analysis. | Low; participant data and specific production budget required. |

Unresolved: `G14-CON-02` (evidence purity versus author privilege), `G14-CON-03` (different meanings of binary states), `G14-CON-04` (study reporting), `G14-CON-07` (recovery versus deliberate restart).

## Review and history

Initial draft, `initial-draft-1`; predecessor null. Author self-review separated state dimensions, removed a possible inference that barks validate emotional tension, retained Thief’s privileged-information counterexample, and flagged the primary study’s printed inconsistency. These are author corrections during first drafting, not independent review. All proposed tests remain unperformed. Next decision: independently review whether the search hypothesis merits a local comparison for a declared stealth activity, not genre-wide adoption.

## References

Access session for every source below: **2026-10-10, America/Los_Angeles / 2026-10-11 UTC**. This is the date of inspection, not proof of current build behavior. `observed-example` claims concern the identified documentation artifact unless expressly stated otherwise. No commercial game was played or recorded for G14.

### GDR-SRC-20261010-G14-002

**Tom Leonard, lead programmer.** *Postmortem: Thief: The Dark Project*. Game Developer. Publication/update: 1999-07-09. [Verified source](https://www.gamedeveloper.com/design/postmortem-i-thief-the-dark-project-i-).

**Edition/build:** Original Thief production retrospective; executable version unknown to this batch. **Access:** `relevant-excerpt`. **Type:** Firsthand practitioner retrospective.

**Inspected locator:** “What Went Right”: Sound as Game Design Focus, Focus, Objectives and Difficulty Levels; “What Went Wrong”: AI (HTML lines 76–89, 103–111).

**Claims supported:** C-01, C-02. **Limits:** Failure explanations are the author’s retrospective interpretations; no controlled outcome comparison is supplied for the claims used.

**Independence:** Same author and production as source 009; count as one underlying production context, not two replications. **Rights:** Copyright retained by the author/publisher; paraphrase and bibliographic links only; no images, audio, source code or full text redistributed.

### GDR-SRC-20261010-G14-003

**Nels Anderson and Jamie Cheng; republished under Game Developer staff attribution.** *Classic Postmortem: Klei Entertainment’s Mark of the Ninja*. Game Developer. Publication/update: 2013-02 original magazine article; 2017-09-07 web republication. [Verified source](https://www.gamedeveloper.com/design/classic-postmortem-klei-entertainment-s-i-mark-of-the-ninja-i-).

**Edition/build:** Original production account; no remaster/build observation. **Access:** `relevant-excerpt`. **Type:** Firsthand practitioner retrospective.

**Inspected locator:** What Went Right §5, “Focus on Core Stealth Principles”; What Went Wrong §1, “Initial Lack of Focus,” and §3, “Nailing Down Certain Mechanics Late” (HTML lines 95–115, 124–129).

**Claims supported:** C-01, C-03. **Limits:** Describes development choices and rejected prototypes; no causal player-effect estimates used. Binary lighting is not binary guard knowledge.

**Independence:** Same game and lead designer as source 004; related studio to source 010. **Rights:** Copyright retained by the author/publisher; paraphrase and bibliographic links only; no images, audio, source code or full text redistributed.

### GDR-SRC-20261010-G14-004

**Brad Gallaway, interviewer; Nels Anderson, interviewee and lead designer.** *Interview with Mark of the Ninja’s Nels Anderson*. GameCritics. Publication/update: 2012-09-01. [Verified source](https://gamecritics.com/brad-gallaway/interview-with-mark-of-the-ninjas-nels-anderson/).

**Edition/build:** Pre-release interview; intended Xbox Live Arcade release context; shipped completion not verified. **Access:** `relevant-excerpt`. **Type:** Direct practitioner interview.

**Inspected locator:** Questions on visual cues, omitted mechanics, non-kill completion, and achievements (HTML lines 23–36).

**Claims supported:** C-01, C-04, C-10. **Limits:** Speaker’s statements about intended possibilities, not independent end-to-end verification or evidence of effects on players.

**Independence:** Not independent of source 003. **Rights:** Copyright retained by the author/publisher; paraphrase and bibliographic links only; no images, audio, source code or full text redistributed.

### GDR-SRC-20261010-G14-009

**Tom Leonard.** *Building an AI Sensory System: Examining The Design of Thief: The Dark Project*. Game Developer. Publication/update: 2003-03-07. [Verified source](https://www.gamedeveloper.com/programming/building-an-ai-sensory-system-examining-the-design-of-i-thief-the-dark-project-i-).

**Edition/build:** Retrospective Dark Engine/Thief design; not a current engine recommendation. **Access:** `relevant-excerpt`. **Type:** Firsthand technical/practitioner account.

**Inspected locator:** “Senses as Gameplay Focus: Thief”; “Expanding the Senses”; “Viewcones”; “Awareness Pulses”; “Conclusion” (HTML lines 82–129).

**Claims supported:** C-05; conditional bridge for C-08. **Limits:** Prose inspected; diagrams and code not used as implementation evidence. Includes deliberately privileged information, so it does not prove strict sensory realism.

**Independence:** Same author and production as source 002; one production context. **Rights:** Copyright retained by the author/publisher; paraphrase and bibliographic links only; no images, audio, source code or full text redistributed.

### GDR-SRC-20261010-G14-010

**Klei Entertainment.** *What is Invisible, Inc.*. Klei Support. Publication/update: 2019-06-25 00:23, as displayed. [Verified source](https://support.klei.com/hc/en-us/articles/360029880011-What-is-Invisible-Inc).

**Edition/build:** Help overview; platform/build unspecified. **Access:** `full`. **Type:** Official product-description artifact.

**Inspected locator:** Opening premise and customization/generation/mode paragraphs (HTML lines 6–10).

**Claims supported:** C-11. **Limits:** The claim that generated variation prevents complacency is promotional and not adopted. Turn-based classification is not established by this inspected passage.

**Independence:** Same studio as sources 003–004 but a different production; not a player study. **Rights:** Copyright retained by the author/publisher; paraphrase and bibliographic links only; no images, audio, source code or full text redistributed.

### GDR-SRC-20261010-G14-012

**Wael Al Enezi and Clark Verbrugge.** *Investigating the Influence of Behaviors and Dialogs on Player Enjoyment in Stealth Games*. Proceedings of AIIDE 19(1), 166–174; AAAI. Publication/update: 2023-10-06. [Verified source](https://doi.org/10.1609/aiide.v19i1.27512).

**Edition/build:** Published 2023 paper; research prototype, not a commercial build. **Access:** `full`. **Type:** Original empirical study.

**Inspected locator:** Methods pp.167–170; results pp.171–173; Figure 7 p.172; Tables 5–6 p.173. Entire PDF text read; screenshots checked for pp.170,172,173. Verified PDF: https://ojs.aaai.org/index.php/AIIDE/article/download/27512/27285/31563.

**Claims supported:** C-06, C-07 only; no universal dialogue or equivalence claim. **Limits:** Raw data/code not obtained; reporting discrepancy and limited generalization are recorded in stealth C-07 and G14-CON-04. No equivalence or causal mechanism claim imported.

**Independence:** Independent academic research context; source 013 is by the same authors in the same proceedings, with sample overlap unestablished. **Rights:** PDF states copyright ©2023 AAAI, all rights reserved. No paper text, tables, figures or prototype assets redistributed.


---
id: GDR-CAND-20261010-G11-GEN-01
kind: genre
title: Interactive fiction
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
run_id: GDR-FULL-20261010
batch_key: G11
attempt_identity: G11-authoring-attempt-01
identity_scope: temporary run-scoped candidate; permanent allocation pending
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
coverage_state: open
input_snapshot: Supplied G11 brief + starter files + inspected selected waves 1–2 dependency excerpts
aliases:
- text adventure
- parser fiction
- choice-based fiction
- hypertext fiction
tags:
- text-interface
- agency
- parser
- choice
- recoverability
- interpretation
- localization
related_topics:
- GDR-CAND-20261010-W01-TOP-01
- GDR-CAND-20261010-W02-TOP-01
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-P02-TOP-03
related_patterns:
- GDR-CAND-20261010-G11-PAT-01
- GDR-CAND-20261010-G11-PAT-02
- GDR-CAND-20261010-W01-PAT-01
- GDR-CAND-20261010-W02-PAT-01
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-P02-PAT-02
related_genres:
- GDR-CAND-20261010-G11-GEN-02
source_ids:
- GDR-SRC-20261010-G11-001
- GDR-SRC-20261010-G11-002
- GDR-SRC-20261010-G11-003
- GDR-SRC-20261010-G11-004
- GDR-SRC-20261010-G11-005
- GDR-SRC-20261010-W01-02
- GDR-SRC-20261010-W01-03
- GDR-SRC-20261010-W02-004
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-G11
predecessor_sha256: null
supersedes: null
change_summary: Initial G11 candidate; no earlier batch resent, source replaced, or canonical identity allocated.
byte_hash_record: ../reviews/full-run-20261010-g11-review-packet.md#candidate-byte-receipt
---

# Interactive fiction

**Draft research candidate, not released knowledge.** This entry addresses text-mediated action, interpretation and recovery. Its central recommendation is conditional: make the supported contribution understandable, then preserve the distinction between understanding an input, carrying out an action, remembering a choice and interpreting a story. It does not require every action to change an ending. The recommendation is a synthesis to test, not an established law. [C-01, C-07, C-09]

## Decision and evidence scope

Use this entry when deciding whether a textual interaction should invite players to formulate actions, recognize authored alternatives, navigate language, or select available situations; how that contribution changes state; and how a player can recover without losing the intended interpretive challenge. Excluded are a complete history of interactive literature, every IF language, language-model improvisation, multiplayer text worlds, and a runtime architecture specification. Those exclusions leave coverage open rather than defining those forms out of existence. [C-01]

Inspected evidence comprises original documentation, a creator help artifact, a volunteer accessibility report, two short interactive-narrative experiments, and an expressive-dialogue development account. No game executable was launched. An author-written example is evidence of that example’s design, not of its execution in an unknown build. The [review packet](../reviews/full-run-20261010-g11-review-packet.md#source-coverage-and-access-gaps) records inspection scope and inaccessible leads.

## Definition and boundaries

**Working definition:** interactive fiction is used here for experiences in which engaging with text is a principal way to encounter a fictional situation and contribute to its traversal, expression, interpretation or change. IFTF’s broad formulation supplies a useful starting point, but this file does not make that organization’s vocabulary a formal standard. “Principal” is a routing aid for this library, not a numerical proportion of screen text. [C-01; GDR-SRC-20261010-G11-001]

The important distinctions are functional rather than prestige rankings:

| Mode or neighboring form | Contribution to examine | Boundary that should remain visible |
|---|---|---|
| Parser interaction | The player proposes an action through a recognized vocabulary and grammar. | Being able to type an utterance does not mean the work models that intention. Separate recognition from world feasibility. |
| Choice-based interaction | The player selects among authored options under the current state. | The displayed option can express an attitude, choose an action, navigate exposition, or merely advance. A menu does not establish the same scope of agency in every case. |
| Hypertext or language navigation | The player selects words, passages or relationships among passages. | Navigation may reorganize interpretation without changing the fictional events. A visible link need not be a plot branch. |
| State-selected situations | The current state makes some scenes available and others unavailable. | Availability can change while the scene’s internal order is fixed. This entry does not establish a comprehensive storylet theory. |
| Visual novel | Reading and optional choice are coupled to staged scenes and visual/voice performance. | Consult the separate [visual novel entry](visual-novel.md). Its pacing, performance, role and rereading problems are not exhausted by the parser/menu distinction. |
| Adventure or detective hybrid | Text contributes to exploration, manipulation or evidential interpretation. | Preserve the difference between solving a world problem and finding a phrase the interface accepts; consult those genre owners before adopting a boundary. |

These are working analytical distinctions, not mutually exclusive market categories or claims about what every audience expects. A text-heavy tactical game is not routed here solely because it has dialogue. Conversely, a fixed fictional history may support substantial interpretive activity. The relevant question is what the work asks a player to do with language and information. [C-01, C-03, C-07]

## Custom research instructions

For further research, compare **mode, promise and recovery policy together**, rather than comparing a famous parser game with an unrelated menu story and attributing every difference to the interface. Record whether the player is proposing verbs, choosing already-written speech, shaping a narrator, arranging evidence, or exploring a fixed account. Identify what is actually implemented before assigning an agency label. [C-09]

Require an original manual, source, creator account or reproducible build route for every named case. Sample beyond English parser puzzles and commercial branching stories: include brief hypertext, non-puzzle work, constrained-language or experimental work, and culturally situated texts. This packet does not yet provide direct coverage of that full range. Seek negative cases where helpful repair destroys wordplay, a choice list discloses a secret, or a state flag incorrectly attributes a deduction to the player. [C-10, C-13]

Inspect the **same intent across alternative phrasings**, and different intents with similar wording. A future parser study should distinguish spelling or referent repair from a solution hint, an irreversible action, and an authorial refusal. For localization, seek native-language implementations and translator accounts, including morphology, inflection, word order, pronouns, input methods and speech synthesis. English synonym coverage cannot validate those cases. [C-02, C-10, C-13]

When studying consequences, record the player’s prediction before the response, the actual authored transition, later recall, and preference separately. A participant can understand a branch and reject its values. A successful completion can conceal a mistaken model. Assess the player’s own interpretation without silently replacing it with the author’s favored reading. These are proposed research safeguards, not findings from tests performed here. [C-09, C-14]

## Player promises and varied audiences

A useful starting promise is specific: “try actions in a modeled place,” “choose this protagonist’s response,” “explore accounts in your own order,” or “discover what a constrained language permits.” It is less useful to promise unrestricted freedom and later defend a narrow grammar as sufficient because the story contains many words. The connection is an inference: a declared scope gives the designer something concrete to compare against the available contributions. Whether that comparison improves trust requires local testing. [C-07, C-09]

Do not treat parser familiarity, fluent reading, comfort with long sessions, or a desire to optimize endings as interchangeable traits. A practiced parser player can still need visual or motor access support; a literary reader can prefer fixed events but dislike losing a passage. An author may intentionally make language resistant. These are audience and aesthetic possibilities to recruit around, not measured population proportions. [C-10, C-12, C-13]

An accessibility option is not a novice label. Keep durable accommodations available while changing instructional help. A player using a transcript or an input aid may be exercising the intended judgment, not avoiding it. That is the adaptation of the inspected P01 end-to-end task guidance and F01 transfer correction, not a new empirical claim. [C-12, C-14]

## Characteristic loops and structures

### From an offered situation to a recognized contribution

For a parser, analyze the loop as **read situation → form intention → express command → identify referents → resolve feasibility → report consequence → update the player’s model**. Each arrow is a possible failure boundary. Inform’s inspected sections distinguish command grammar, authored mistake handling and parser errors; they do not imply an unrestricted language interface. [C-02; GDR-SRC-20261010-G11-002]

For choices, analyze **read situation → interpret visible alternatives → select → see the performed contribution → encounter the resulting situation**. A compact choice label can differ from the words subsequently spoken; a disabled option can communicate a limitation without allowing that action. Neither device is automatically deceptive or expressive. Judge what the presentation led the player to expect and whether the limitation is part of the work’s declared role. [C-03, C-09]

For hypertext or archival exploration, the loop may instead be **notice a connection → follow it → revise an interpretation → return or continue**. There need not be a change to fictional chronology. Here, “consequence” can mean a new arrangement of attention, but that should not be advertised as changing the fate of a character unless a corresponding authored change exists. This is a proposed analytic distinction, not evidence that interpretive and causal agency feel equivalent. [C-07]

### State is not a single “has read” flag

A design review should distinguish at least the following conceptual records. These are analysis categories, not a required data schema. [C-08, C-11]

| Record | Example of what it means | What it does not establish |
|---|---|---|
| Fiction state | A letter was surrendered; a bridge is closed. | The player understood why. |
| Encounter history | A passage or scene was displayed. | It was read attentively, remembered, or accessible. |
| Committed expression | A response selected was conciliatory. | A permanent personality diagnosis of the player. |
| Stated player hypothesis | The player explicitly linked a witness to an event. | The hypothesis is true in the fiction. |
| Navigation/recovery position | The reader is viewing an earlier passage or saved point. | Current story state has been rewound. |
| Cross-play record | A route has been encountered on a previous play. | The current protagonist possesses that knowledge. |

Ink documents ways to gather branches and refer to prior traversal. That is useful feasibility evidence for authoring, not a warrant to substitute visit counts for comprehension. Emily Short’s account provides a particularly relevant practitioner distinction between encountering facts and forming a hypothesis. The proposed application is to ask the player for an interpretation only where interpreting is itself the intended contribution, rather than awarding that contribution silently because text appeared. [C-03, C-08; GDR-SRC-20261010-G11-003; GDR-SRC-20261010-W02-004]

### Local contribution, later consequence and ending variation

A reconverging scene can retain a relationship change, a resource, an obligation, or an acknowledged stance. It can also honestly offer only a local expressive variation. Use the inspected `GDR-CAND-20261010-W01-PAT-01` rather than inventing a new G11 reconvergence pattern. The genre-specific task is to decide which textual difference is promised, where it becomes observable, and whether a later narrator contradicts it. [C-07; reviewed dependency D-02]

**Empirical boundary.** Fendt and colleagues compared a short branching story with linear variants. The comparable branching analysis used 52 of 79 entrants, alongside groups of 54 and 44. Four of five story-level branching/acknowledgment comparisons were nonsignificant; that is not equivalence. Phased groups, selection and demographic differences constrain interpretation. No durable replay trust or production saving was established. [C-05; GDR-SRC-20261010-W01-02, PDF pp. 8–11, Tables 1–2]

Cardona-Rivera and colleagues studied 88 adults using a fixed-order, six-choice story and retrospective ratings; 95% reported more than five years of gaming. Their analysis supported three initial agency scales, not all five; a modified fifth excluded late choices. This is bounded evidence about perceived agency and situational differences, not a route-count rule or a test of every kind of IF. [C-06; GDR-SRC-20261010-W01-03, printed pp. 11–14]

The decision supported by this evidence is therefore narrower than “always branch” or “feedback is enough”: specify the consequence being offered and evaluate whether the relevant players understand and value it. Narrative attention, comprehension, perceived agency and preference remain different outcomes. [C-09]

## Design choices and conditional application process

| Decision | Favor this option when… | Tradeoff or simpler alternative |
|---|---|---|
| Parser rather than an explicit action menu | Formulating actions and testing a modeled situation are intended activities. | Recognition failures require authored coverage. A finite menu is clearer when action invention is not the desired challenge. |
| Visible rather than concealed options | The challenge is choosing among understood possibilities. | It can disclose what the world supports or what matters. A discovery-focused work may reveal options later, but should not confuse inaccessibility with mystery. |
| Immediate acknowledgment | The player needs to know the accepted contribution, not the eventual outcome. | Overexplaining motives can foreclose interpretation. A minimal response may suffice if the commitment is already clear. |
| Reconvergence | The retained difference can survive a shared later scene. | Some promises require mutually exclusive events; a shared ending may violate them. |
| Optional hints or repair | The obstacle is an unintended interface or access burden. | A solution hint can remove the intended inference. Stage interface help separately from content disclosure. |
| Transcript or return | The player needs to revisit information. | Rewinding world state is a different intervention; offer only the scope that can be honored. |

These conditional choices are hypotheses derived from the distinctions above, not empirically ranked options. No universal command vocabulary size, word count, reading speed, route count or retry allowance is proposed. [C-09–C-13]

1. **Write the contribution contract.** Choose one scene and describe what the player may supply, what remains authored, and what uncertainty is intentionally retained. Separate an action’s feasibility from its desirability. [C-09]
2. **Map acceptance and consequence.** For each supported contribution, record how it is recognized, whether clarification is required, the performed action, the observable response, the retained state and the horizon of any later acknowledgment. For a non-causal passage, record navigation or expression instead of inventing a plot consequence. [C-07, C-10]
3. **Author the smallest diagnostic help.** Distinguish unknown wording, ambiguous referent, unavailable object, unsupported action and unmet prerequisite. Use [intent-preserving parser repair](../patterns/intent-preserving-parser-repair.md) only when preserving a player-specified intention is appropriate. Stop expanding synonyms if the actual problem is an unmodeled intention. [C-10]
4. **Declare recovery scope.** Decide separately whether the player can reread, undo, reload, restart a section or revisit another route. Use [state-safe narrative rereading](../patterns/state-safe-narrative-rereading.md) for the distinction, without pretending a history view changes the world. [C-11]
5. **Audit missing information by access route and locale.** Examine a complete task from setup through continuation. Test instructions, focus order, textual diagrams, updates, named objects and recovery—not just the body prose. Support may change while the intended inference remains demanding. [C-12, C-13]
6. **Evaluate a discriminating comparison before scaling.** Compare matched intentions and comparable narrative content. Include valid and invalid transfer cases; retain access accommodations. Collect the outcomes separately and inspect cases of confidently wrong understanding. Revise the contract or reduce the interaction’s scope when the evidence does not support it. [C-14]

## Applying shared topics

Only the following relevant selected dependency excerpts were transferred. Their complete hashes, exact archive paths and inspected passages are in the [reviewed-dependency ledger](../reviews/full-run-20261010-g11-review-packet.md#reviewed-dependencies). The shared files are not reissued inside this G11 packet.

| Shared entry | What changes for interactive fiction | Limit retained |
|---|---|---|
| `GDR-CAND-20261010-W01-TOP-01` Narrative structures | Distinguish text traversal, fictional change and player interpretation. | Immediate recognition is not proven equivalent to durable consequence. |
| `GDR-CAND-20261010-F02-TOP-01` Decision design | Audit information the prose, command grammar and visible options make available before commitment. | Choosing differently from the designer’s preference is not failed comprehension. |
| `GDR-CAND-20261010-W02-TOP-01` Dialogue and voice | Separate typed or selected intent from the utterance and response performed by an authored character. | An ambiguous literary utterance need not be replaced by an explicit intention label. |
| `GDR-CAND-20261010-P01-TOP-03` Accessibility and inclusive interaction | Follow instructions, passage updates, input, error repair and save/re-entry as one accessible task. | No inherited numerical WCAG, WCAG2ICT or XAG settings are applied to a native game. |
| `GDR-CAND-20261010-P02-TOP-03` Multimodal communication | Supplement difficult updates without making simultaneous audio/text attention mandatory. | Alternative access should preserve relevant facts, not promise identical experience. |

The parser transfer test also uses corrected `GDR-CAND-20261010-F01-PAT-01`: change the surface situation while retaining the rule, and include cases that distinguish the correct rule from a plausible wrong strategy. Do not test the same rejection twice and call it transfer; do not withdraw an accommodation merely because a participant succeeds. [C-14]

## Pattern selection and hybrid conflicts

**Use G11-PAT-01** when recognized intention is fragile, not when the work deliberately makes exact wording the central puzzle. **Use G11-PAT-02** when returning to text risks confusing reading position with fictional state. Both are hypotheses and can be omitted if a simpler interface satisfies the contract. [C-10, C-11]

Adapt `GDR-CAND-20261010-W02-PAT-01` after an action or utterance has been chosen; G11-PAT-01 concerns the earlier recognition/clarification boundary. Adapt `GDR-CAND-20261010-W01-PAT-01` for explicit retained consequences; no new foldback pattern is included. Adapt `GDR-CAND-20261010-P02-PAT-02` for sound, image or textual-layout information that would otherwise be inaccessible; preserve uncertainty about hidden actors rather than captioning the solution. [C-07, C-10, C-12]

In a detective hybrid, a command guide can reveal permissible syntax without naming an unknown culprit. In a precision word puzzle, accepting near-synonyms may erase the object of play. In a survival hybrid, universal undo may conflict with an advertised commitment model, while rereading prior information need not. In a VN hybrid, repeated dialogue might carry new performance or contextual meaning; a “seen” passage should not automatically be treated as dispensable. These are conditional conflict analyses, not claims about all examples of the neighboring genres. [C-10, C-11, C-13]

## Representative cases, worked example and counterexamples

### Inspected artifacts, not gameplay observations

**The Dreamhold help** provides a concrete creator-authored route for examining command help, hints and system controls. It is useful because those concerns are explicitly separated in one document; its current executable behavior and audience outcomes are unverified here. **Inform’s examples** provide distinct grammar and error-handling cases. **Ink’s weave examples** demonstrate authored rejoining and traversal conditions in documentation. None is treated as a causal proof of enjoyment. [C-02–C-04]

**IFTF’s 2019 report** supplies directly relevant negative access evidence: its two prepared games and 34 survey respondents surfaced screen-effect and other barriers, with varied results across setups. Its recommendations combine observations, committee expertise and APX. This is a reason to examine actual presentation paths, not a claim that every Twine work outperforms every parser work or that old interpreter results hold today. [C-17; GDR-SRC-20261010-G11-005]

### Illustrative worked example: the archive handover

**Invented design example; not a shipped work, prototype or test result.** A visitor must return an archive item. Two envelopes are visible: a signed original and an annotated copy. The scene’s intended challenge is deciding which document to surrender, not guessing the word “give.” A later testimony should differ depending on the document surrendered. [C-10, C-15]

| Situation | Proposed response and retained distinction |
|---|---|
| Player types “hand over the envelope.” | Ask which visible envelope. Do not assume the original, consume time, or record a surrender while asking. |
| Player types “give the annotated copy to the clerk.” | Accept the supported intent; identify the committed object in the response and retain that transfer. |
| Player types “burn the original.” | State the supported limitation without converting the request into surrendering it. An invented non-burning substitute is not semantic repair. |
| Player names a concealed third document. | Avoid confirming its existence through a repair suggestion. Offer only help justified by the current scene and knowledge contract. |
| Both accepted surrender choices reach the same interview. | Adapt the shared reconvergence pattern: the clerk’s testimony and available challenge differ consistently with what was surrendered. |
| Player opens the history panel after the interview. | Show the earlier exchange without changing the current transfer or testimony state. A separate, clearly scoped undo is required to revise the choice. |

The mechanism proposed here is not “more feedback is better.” It is that clarification prevents an unchosen commitment, an explicit response marks the action that did occur, and later state honors the chosen document. The first two are inspectable consistency requirements; whether the experience becomes clearer or more satisfying is untested. If the story cannot afford different testimony, it should reduce its promised consequence rather than retain an inert “important decision” label. [C-09, C-15]

### Strong opposing cases

**Illustrative linguistic constraint:** a poem changes only when its exact metrical phrase is supplied. Synonym repair would destroy the player’s contribution. Supply accessible text and explain the domain of experimentation, but do not silently translate an approximate phrase into a successful one. [C-10, C-13]

**Illustrative fixed archive:** the player can arrange contradictory accounts but cannot change the past. A final ambiguous reading is not a failed branching system. Conversely, adding a fact journal that announces the correct interpretation would remove the intended uncertainty. Preserve reader control without claiming causal control. [C-07, C-11]

These counterexamples constrain the recommendation; they are not substitute empirical evidence for the excluded forms.

## Accessibility, ethics, localization and production

A text-first work still needs an inspectable input and presentation path. Treat boxed quotations, spatial text, updated status, navigation focus and historical passages as part of the fiction’s delivery. An alternate description should not silently disclose information a sighted reader must infer; when exact equivalence is impossible, expose the tradeoff rather than calling either representation neutral. These are conditional applications of P01/P02 and the IFTF observations, not a certified compliance assessment. [C-12]

For a localized parser, separate action identifiers from the surface names and forms that express them; budget for ambiguity resolution in the target language. For choice prose, evaluate what the player believes the option commits the protagonist to before reviewing elegance alone. Idioms, honorifics, regional knowledge, names and voice output need culturally informed review. This packet lacks native-language comparative evidence, so those proposals remain hypotheses, not instructions to erase culturally specific material. [C-13]

Do not infer a player’s private identity or stable beliefs from fictional choices. A role-play refusal, distress, moral objection or curiosity can produce the same action. Any future research should collect only needed observations with consent, keep free-text logs private, and permit withdrawal. These are proposed ethical safeguards; they are not a legal or clinical claim. No psychiatric benefit is inferred from an inaccessible game lead. [C-16]

Production effort should be estimated from actual accepted intentions, state distinctions, narrative dependencies and regression cases, not word count alone. Adding a recognized verb creates obligations about objects, knowledge and failure responses. Adding a state-conditioned acknowledgment creates a continuity obligation after revision and localization. That follows from the proposed consistency model; no cost saving or budget multiplier was measured. [C-10, C-15]

## Research questions and proposed validation

**All tests below are proposed and not performed.** They require a separately authorized prototype or study; this file authorizes neither implementation nor recruitment. Predefine the local decision margin and recruitment rationale before data collection rather than importing an arbitrary sample-size or reading-speed target. [C-14, C-16]

| Test and comparison | Procedure and participants/context | Separate outcomes and confounds | Rejection or revision rule |
|---|---|---|---|
| Interface repair without solution disclosure | Compare generic rejection with bounded clarification in matched scenes. Include parser newcomers and experienced players, relevant input/assistive technology users, and target-language readers. Rotate scene order. | Intent retained; unintended state changes; clarification success; solution leakage; prediction of accepted action. Keep puzzle difficulty and supported actions comparable. | Reject a repair that changes the intended action, confirms hidden facts, or encourages confidently wrong rule use. Better completion alone does not rescue it. |
| Actual consequence versus local expression | Compare an explicitly local expressive choice with a clearly promised later consequence, using similar prose and exposure. Ask for predictions before feedback and later explanations. | Narrative attention, perceived agency, actual consequence comprehension and preference recorded separately. Expectation framing and prior exposure are confounds. | Narrow the promise when players expect a later change that is absent; do not infer comprehension from liking. |
| Same-rule transfer | After a supported action, present changed objects and situations containing both valid and invalid applications of the same recognition/feasibility rule. Keep accommodations. | Predicted acceptance and explanation versus actual selection; distinguish synonym acceptance from guessing any verb. | Revise when success is compatible with the competing wrong strategy. A changed hidden rule is not a valid transfer probe. |
| Rereading without state confusion | Compare history-only and explicitly scoped undo after interruption. Ask what changed before allowing another action. | Fiction-state prediction, recoverability, lost place, preference and access effort. Memory, fatigue and route familiarity may differ. | Remove or relabel a control that causes accidental commitment or a false expectation of reversal. |

### Coverage checkpoint

| Area | Current coverage | Next discriminating question |
|---|---|---|
| Parser grammar, error categories, help and intent repair | Documentation and worked proposal; no runtime observation. | Which repairs preserve intention across target-language ambiguity without revealing a solution? |
| Choice, reconvergence, state and agency | Bounded empirical sources plus inspected shared candidates; effect transfer unresolved. | Which valued distinction survives rereading and comparison with another path? |
| Hypertext, literary experiment and non-puzzle forms | Analytical boundary only; representative primary game coverage incomplete. | When is navigational or verbal resistance itself the intended contribution? |
| Accessibility | Original 2019 report and scoped shared guidance; current platform behavior untested. | Can intended users configure, perceive, act, recover and continue in the actual build? |
| Localization and cultural knowledge | Proposed review process; native-language empirical and production sources missing. | Which ambiguity is intentional, and which is introduced by translation or unfamiliar interface conventions? |
| Session recovery and cross-play state | G11-PAT-02 hypothesis; broader reviewed session guidance missing. | Does the user distinguish rereading, rewinding and starting a new interpretation? |

The next decision is independent evidence/content review of this candidate and its associated patterns, including the strongest opposing cases. Coverage remains open after that review unless the outstanding areas are explicitly addressed or narrowed.

## Claim ledger

Claim IDs are local to this artifact. Confidence describes the stated claim, not approval or universal applicability. Proposed application claims remain untested.

| Claim | Material claim | Class | Support and precise locator | Confidence and limit / unresolved question |
|---|---|---|---|---|
| C-01 | Use a text-mediated contribution definition as a working boundary, not a universal market taxonomy. | inference | GDR-SRC-20261010-G11-001, “What is interactive fiction?”; G11 brief decision questions | Moderate for a useful routing distinction; low for any universal classification; experimental and multilingual range incomplete. |
| C-02 | Inform documents finite action grammar and distinct authored mistake/parser-error mechanisms. | observed-example | GDR-SRC-20261010-G11-002, §§17.1, 17.21, 18.35 | High for inspected text; runtime and user outcomes unverified. |
| C-03 | Ink’s inspected examples represent gathering branches and conditioning content on traversal. | observed-example | GDR-SRC-20261010-G11-003, Part 2 Weave and TURNS_SINCE | High for documentation, not branch quality or comprehension. |
| C-04 | The Dreamhold help separates command assistance, hints and system controls. | observed-example | GDR-SRC-20261010-G11-004, Commands, System Commands, Special Commands | High for the help artifact; unknown executable build and effects. |
| C-05 | Short-study agency comparisons do not establish equivalence between branch consequences and acknowledgment. | empirical-evidence | GDR-SRC-20261010-W01-02, PDF pp. 8–11; Tables 1–2 | Moderate for bounded reported results; low for replay or genre-wide transfer. |
| C-06 | Situationally different choices received bounded, scale-dependent agency evidence in a fixed-order story study. | empirical-evidence | GDR-SRC-20261010-W01-03, printed pp. 11–14; Tables 5–6 | Moderate for reported data; post-hoc refinement, retrospective ratings and sample constrain causal transfer. |
| C-07 | Separate contribution, retained consequence and interpretation; reconvergence is conditional on the actual promise. | inference | Reviewed D-01 Narrative structures §§Promise/action/persistence, Authored order; D-02 Recipe; C-05–06 | Moderate as an analysis; no claim of equal enjoyment or universal need for branches. |
| C-08 | Encountered text does not certify a player-formed hypothesis; Short reports distinguishing those cases. | practitioner-heuristic | GDR-SRC-20261010-W02-004, player-deduced facts and hypothesis-crafting passages | Moderate for creator account; effect and exact revised build unknown. |
| C-09 | Specify and evaluate the offered contribution while measuring attention, agency, comprehension and preference separately. | hypothesis | C-05–08; reviewed D-03 dialogue and D-08 decision-information distinctions | Low as an efficacy recommendation; independent outcomes and framing must be tested. |
| C-10 | Bounded parser repair should clarify rather than silently replace an intention; omit it where exact language is the challenge. | hypothesis | C-02; G11-PAT-01 recipe; illustrative archive and metrical counterexample | Moderate for logical consistency; low for access/experience benefits until tested. |
| C-11 | Rereading, changing a decision and cross-play knowledge need distinct scope contracts. | hypothesis | C-04; G11-PAT-02; reviewed D-01 discovery-versus-event-order distinction | Low for effects; scope separation is proposed, not a certified implementation. |
| C-12 | Text-first presentation still requires end-to-end access checks; historical IF report observations do not certify current builds. | inference | GDR-SRC-20261010-G11-005, Testing method and Further testing; reviewed D-04 and D-07 | Moderate for reported barriers in sampled settings; recommendations broader than direct observations. |
| C-13 | Preserve intentional language/cultural ambiguity while testing unintended recognition and access barriers in each locale. | hypothesis | C-02, C-12; reviewed D-03 utterance/interpretation distinction; synthetic counterexamples | Low; native-language grammar and culturally specific audience evidence missing. |
| C-14 | Transfer checks must distinguish a stable correct rule from a wrong strategy and retain accommodations. | inference | Reviewed D-05 corrected recipe and examples, lines 77–123; D-08 | Moderate for diagnostic logic; G11 tests not performed and no population learning effect claimed. |
| C-15 | The archive example specifies observable commitments and continuity obligations rather than a proved benefit. | hypothesis | Illustrative worked example; C-07, C-10–11 | Low; invented example, no production estimate or implementation. |
| C-16 | Future studies should protect consent and privacy and not diagnose identity or health from fictional choices. | hypothesis | Author-proposed ethical protocol, not source-derived efficacy or legal advice | Moderate as a precautionary proposal; project approval and research protocol still needed. |
| C-17 | The 2019 IFTF evaluation reported access barriers in two prepared games across heterogeneous volunteer settings. | empirical-evidence | GDR-SRC-20261010-G11-005, Sources for this report; Testing method; Further testing | Moderate for reported observations; not a controlled genre/platform ranking or current-version certification. |

## References

Access date for every record below: **2026-10-10**. “Observed example” refers to an inspected document or source artifact unless explicitly stated otherwise; no game executable was run. Source identities are temporary; global deduplication and permanent allocation remain pending.

### GDR-SRC-20261010-G11-001
**Interactive Fiction Technology Foundation (IFTF). Frequently Asked Questions About Interactive Fiction.** Publication/update: unknown. Publisher: IFTF.
**URL:** [Frequently Asked Questions About Interactive Fiction](https://iftechfoundation.org/frequently-asked-questions/).
**Edition/build:** Unversioned public page; snapshot checked 2026-10-10. **Locator:** “What is interactive fiction?”; parser and choice-based descriptions.
**Access:** `relevant-excerpt`. **Type:** Foundation terminology / explanatory primary artifact. **Limits/independence:** An organization’s broad usage, not a formal taxonomy or audience study. Advocacy about accessibility or comparative artistic value is not adopted.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-002
**Graham Nelson / Inform documentation project. Writing with Inform.** Publication/update: unknown. Publisher: Inform documentation project.
**URL:** [Writing with Inform](https://ganelson.github.io/inform-website/book/WI_17_1.html). [§17.21](https://ganelson.github.io/inform-website/book/WI_17_21.html); [§18.35](https://ganelson.github.io/inform-website/book/WI_18_35.html).
**Edition/build:** Author-hosted HTML edition; exact release/commit not stated in inspected pages. **Locator:** §17.1 Understand, including Xylan; §17.21 Understanding mistakes, including Query and Hot Glass Looks Like Cold Glass; §18.35 Printing a parser error, including WXPQ.
**Access:** `relevant-excerpt`. **Type:** Official authoring manual and worked source artifacts. **Limits/independence:** Grammar examples inspected as text, not compiled. Contextual repair does not establish multilingual natural-language understanding or player benefit. Sections belong to one manual, not independent corroboration.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-003
**inkle. Writing with Ink.** Publication/update: unknown. Publisher: inkle / public GitHub repository.
**URL:** [Writing with Ink](https://github.com/inkle/ink/blob/master/Documentation/WritingWithInk.md).
**Edition/build:** master as served; no immutable commit established. **Locator:** Part 2: Weave, “Gathers,” “Nested Flow,” labels and conditional options; Part 1 game queries, TURNS_SINCE.
**Access:** `relevant-excerpt`. **Type:** Official authoring documentation / source examples. **Limits/independence:** Examples were not executed. A flow-construction claim is not proof of semantic continuity, choice quality, or absence of test obligations. Unpinned technical snapshot.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-004
**Andrew Plotkin. The Dreamhold — Help.** Publication/update: unknown. Publisher: Author’s website.
**URL:** [The Dreamhold — Help](https://eblong.com/zarf/zweb/dreamhold/help.html).
**Edition/build:** Web help; game release/build/platform behavior not verified. **Locator:** Basics; Commands; System Commands; Special Commands; Strategy.
**Access:** `relevant-excerpt`. **Type:** Creator-written instructions for a named game. **Limits/independence:** Documentation only; no game play, transcript capture, or measured outcome. Save/restore/undo and hints describe different controls, not an automatic accessibility certification.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-005
**Jason McIntosh (primary author), IFTF Accessibility Testing Project committee. Accessibility Testing Report.** Publication/update: 2019; publication announcement 2019-06-12. Publisher: IFTF.
**URL:** [Accessibility Testing Report](https://accessibility.iftechfoundation.org/). [Publication announcement](https://blog.iftechfoundation.org/2019-06-12-iftfs-accessibility-testing-project-report.html).
**Edition/build:** 2019 public report; testing January–February 2019. **Locator:** Sources for this report; Testing method; Tester profile and recruitment; Offer hints and walkthroughs; Further testing with parser-game screen effects; Further testing with non-Latin Unicode characters.
**Access:** `relevant-excerpt`. **Type:** Original volunteer accessibility evaluation and committee recommendations. **Limits/independence:** 34 respondents; two specially prepared Inform/Twine games, heterogeneous self-selected environments. Recommendations also use committee expertise and APX, not a controlled estimate for all IF. Raw responses not reanalyzed; 2019 tool outcomes not a 2026 compatibility claim.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-W01-02
**Matthew William Fendt; Brent Harrison; Stephen G. Ware; Rogelio E. Cardona-Rivera; David L. Roberts. Achieving the Illusion of Agency.** Publication/update: 2012. Publisher: ICIDS 2012 / Springer, LNCS 7648, pp. 114–125.
**URL:** [Achieving the Illusion of Agency](https://www.cs.uky.edu/~sgware/reading/papers/fendt2012achieving.pdf).
**Edition/build:** Author-hosted 12-page paper; DOI 10.1007/978-3-642-34851-8_11. **Locator:** PDF pp. 3–8 design/method; pp. 8–10 results; Tables 1–2 on PDF p. 9 visually inspected; pp. 10–11 discussion.
**Access:** `relevant-excerpt`. **Type:** Original empirical study. **Limits/independence:** Selected comparable branching subgroup, phased groups, demographic imbalance and short single-play context limit inference. Non-significance is not equivalence; no measured production savings. Reuses W01 identity; W02-002 is an existing duplicate identity pending coordination.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-W01-03
**Rogelio E. Cardona-Rivera; Justus Robertson; Stephen G. Ware; Brent Harrison; David L. Roberts; R. Michael Young. Foreseeing Meaningful Choices.** Publication/update: 2014-10-08. Publisher: AAAI / AIIDE 10(1), pp. 9–15.
**URL:** [Foreseeing Meaningful Choices](https://ojs.aaai.org/index.php/AIIDE/article/view/12716). [Full publisher PDF](https://ojs.aaai.org/index.php/AIIDE/article/download/12716/12564/16233).
**Edition/build:** Publisher paper; DOI 10.1609/aiide.v10i1.12716. **Locator:** Printed pp. 11–12 Method/Participants/Apparatus; p. 13 Tables 5–6 and Figure 2 visually inspected; p. 14 Limitations and Future Work.
**Access:** `relevant-excerpt`. **Type:** Original empirical study. **Limits/independence:** Fixed-order within-subject design, retrospective ratings, gaming-experienced sample and post-hoc analytical refinements limit generalization. Shares authors/research lineage with Fendt, but is a distinct dataset; W02-001 and F02-001 remain duplicate aliases pending coordination.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-W02-004
**Emily Short. Dialogue Expressiveness in Mask of the Rose.** Publication/update: 2023-11-22. Publisher: Emily Short’s Interactive Storytelling.
**URL:** [Dialogue Expressiveness in Mask of the Rose](https://emshort.blog/2023/11/22/dialogue-expressiveness-in-mask-of-the-rose/).
**Edition/build:** Retrospective describing launch and subsequently revised system; exact game build unknown. **Locator:** Opening description of wardrobe/personality-filtered dialogue; player encountered versus player-deduced facts; reported post-launch clarification/revision.
**Access:** `relevant-excerpt`. **Type:** Firsthand creative/practitioner account. **Limits/independence:** Reuse exact W02 identity. Text inspected; embedded game screenshots and executable not used as behavior evidence. Expressivity and agency goals are creator intent, not validated effect sizes.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

## Review and history

Version **0.1.0**, candidate revision **initial-draft-1**, first G11 capture. No predecessor is asserted. Author self-review is recorded in the [batch packet](../reviews/full-run-20261010-g11-review-packet.md#author-self-review); it is not independent review. Candidate SHA-256 is external to these bytes in that packet. Reviewer, approved_by and approved_date remain null.

Open contradictions: G11-CON-01 (acknowledgment versus promised consequence), G11-CON-02 (repair versus expressive resistance), G11-CON-03 (recovery versus commitment), G11-CON-05 (facts versus interpretation). Local conflict keys are not allocated global register IDs. New child work and missing dependencies remain queued in the packet; no earlier batch is resubmitted.

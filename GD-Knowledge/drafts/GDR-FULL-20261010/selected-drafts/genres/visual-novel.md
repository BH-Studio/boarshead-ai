---
id: GDR-CAND-20261010-G11-GEN-02
kind: genre
title: Visual novel
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
- VN
- visual narrative
- kinetic presentation
tags:
- scene-structure
- routes
- performance
- reader-control
- localization
- rereading
related_topics:
- GDR-CAND-20261010-W01-TOP-01
- GDR-CAND-20261010-W02-TOP-01
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-P02-TOP-03
related_patterns:
- GDR-CAND-20261010-G11-PAT-02
- GDR-CAND-20261010-G11-PAT-01
- GDR-CAND-20261010-W01-PAT-01
- GDR-CAND-20261010-W02-PAT-01
- GDR-CAND-20261010-P02-PAT-02
related_genres:
- GDR-CAND-20261010-G11-GEN-01
source_ids:
- GDR-SRC-20261010-G11-006
- GDR-SRC-20261010-G11-007
- GDR-SRC-20261010-G11-008
- GDR-SRC-20261010-G11-009
- GDR-SRC-20261010-G11-010
- GDR-SRC-20261010-G11-011
- GDR-SRC-20261010-G11-012
- GDR-SRC-20261010-G11-013
- GDR-SRC-20261010-G11-014
- GDR-SRC-20261010-G11-015
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

# Visual novel

**Draft research candidate, not released knowledge.** This entry examines authored scenes, performance, reader control, optional choices and route structure. Its central proposal is to design the **reading-and-performance contract** separately from the **story-consequence contract**. A reader may control pace or revisit a scene without controlling the fictional outcome; a choice may shape a character’s expression without selecting another route. Neither distinction makes the form merely illustrated interactive fiction. [C-01, C-08, C-09]

## Decision and evidence scope

Use this entry to decide how a reader moves through staged narrative, what a route or a choice actually changes, which protagonist role is offered, and how text, art, voice and rereading remain intelligible together. It covers scene and route analysis, presentation modes, recoverability, authoring/localization obligations, accessibility and proposed validation. It does not provide an exhaustive cultural history, a market-segmentation study, every visual-novel engine, or an approved runtime design. [C-01]

The inspected sources include Ren’Py documentation with an **8.5.4** banner, a publisher description of a specified planetarian edition, and first-person development accounts for Mask of the Rose and Scarlet Hollow. Documentation is a capability description, and creator intent is not an effect test. No executable, recorded playthrough, voice performance or native-language player session was run or observed in this batch. The [review packet](../reviews/full-run-20261010-g11-review-packet.md#source-coverage-and-access-gaps) records the resulting gaps.

## Definition and contested boundaries

**Working definition:** visual novel denotes here a narrative form organized around authored scenes in which reading and visual presentation are central to delivery, often with voice or other audiovisual performance, and with a variable degree of reader navigation, expression, choice and branching. “Often” does not prescribe a mandatory asset list or claim a measured frequency. This is a provisional library definition derived from inspected practice, not a formal industry standard. [C-01]

A minimal distinction from the adjacent [interactive fiction entry](interactive-fiction.md) is the design responsibility for the **staged reading event**: which text is visible together, which character or perspective is performing, how presentation progresses, and what rereading preserves or changes. This responsibility exists even when an ending is fixed. IF and VN may overlap; these two files route different decisions rather than enforce exclusive membership. [C-01, C-02]

| Contested label or boundary | Useful distinction for this library | Misleading shortcut to reject |
|---|---|---|
| Visual novel versus branching story | Reading/presentation form and story topology are different axes. | Requiring a route menu or multiple endings in every VN. |
| Linear or kinetic presentation | An authored sequence may permit pace, history or replay controls without alternate story outcomes. “Kinetic” is used here descriptively, not as a universal vendor classification. | Calling such a work failed interactivity merely because its plot does not branch. |
| ADV-style versus NVL-style display | In the inspected Ren’Py tutorial, a dialogue-window presentation contrasts with page-like accumulated text. | Treating a display convention as a route architecture, quality level or complete genre definition. |
| Dating or relationship simulation hybrid | A schedule/resource model may organize scenes and relationships. | Assuming every VN is romance, that all relationships are optimization problems, or that all readers seek the same ending. |
| Mystery/adventure hybrid | Evidence interpretation or actions may gate the next scene. | Inferring the player’s deduction from a scene-visited marker. |
| Role-playing hybrid | Character dispositions can change the available expression or information. | Treating protagonist traits as a psychological classification of the player. |
| Tone, art style, language or platform | These can change the application and intended audience. | Making an anime-like look, a national origin, adulthood, romance, horror, mobile or single-player status a sufficient definition. |

The no-branching case is not hypothetical: the publisher describes the **2024 Nintendo Switch combined planetarian edition** as a visual novel and explicitly excludes choice-based story branching. That inspected publisher statement supports a boundary counterexample, not an observation of every port or a causal claim about reader satisfaction. [C-03; GDR-SRC-20261010-G11-014]

## Custom research instructions

Future research should sample **fixed sequences, branching routes, expressive but reconverging choices, and hybrids with explicit systems**. Record the release, scene, language, character role and actual control before comparing them. A voiced scene in one language and an unvoiced scene in another are not a clean comparison of visual-novel versus prose effects. Inspect the actual performed material before claiming how tone, timing or an actor’s delivery changes interpretation. [C-04, C-12]

Challenge the proposition that more branches, faster text, more voice, more art, or a “true” ending produces a better experience. Ask which experience and whose preference the proposition concerns. For a route, examine entry conditions, common material, divergence, exclusive scenes, return points, retained state and ending interpretation; do not treat the route count as the amount of meaningful agency. [C-08, C-09]

Seek creator postmortems and translator/localization accounts in the originating language, especially where honorifics, register, kinship language, indirect refusal, gesture or culturally specific role expectations carry the decision’s meaning. This packet contains English-language technical and creator evidence, not a representative survey of Japanese, Chinese, Korean or other VN production and audiences. Preserve culturally specific meaning rather than substituting an unexamined “universal” wording. [C-12]

Examine rereading directly. Compare history, voice replay, rewinding with changed choices, rereading under locked choices, and starting a different route. Ask whether the control preserves the current fictional state, alters it, or begins another context. Include negative cases in which repeated words acquire new significance; the same text identifier need not mean the same informational or performed event. [C-10, C-11]

## Player promises and varied audiences

A project can invite someone to observe an authored protagonist, inhabit a constrained role, negotiate a relationship, investigate a situation, or co-author expression. Those are candidate roles to establish, not demographic facts about all VN readers. State which aspects of the protagonist are fixed and which are open to contribution. A reader can prefer an unlikeable authored protagonist while refusing to choose a line that contradicts the role they were offered. [C-07, C-09]

Different goals imply different evaluations. A reader seeking to hear a performance may prefer unhurried delivery; someone revisiting known material may prioritize efficient return; a reader using speech output may need navigation that is not tied to an animation’s duration. These are possibilities to recruit and test around, not a warrant to label either a default or an accommodation as universally best. [C-04, C-10, C-13]

**Separate the outcomes.** Narrative attention concerns what the reader attends to; comprehension concerns their understanding; perceived agency concerns experienced control; preference concerns what they value. Long dwell time could reflect attention, distraction, fatigue or confusion. Route completion can coexist with a wrong model of why the route opened. The proposed research should not collapse these signals into a single “immersion” score. [C-09, C-14]

## Characteristic scene, route and reading structures

### Scene structure is not a text box alone

Analyze a scene as an authored sequence of interpretive beats: presented situation, speaker or viewpoint, utterance, visual or vocal contribution, advance behavior, optional response and transition. The unit for production review is the relationship among these elements, not merely a line of script. Ren’Py’s documentation describes separate presentation, voice and translation facilities; treating their semantic combination as a review unit is this entry’s inference, not a measured engine benefit. [C-02, C-04, C-12]

For an exchange with deliberate hesitation, ask what happens when the reader advances early, enables instant text, uses automatic advance, mutes performance, replays voice or reads from history. A single speed cannot satisfy all of those contracts. The alternatives need not feel identical; the question is whether each still presents the information and control promised for that route. No universal character rate, dwell time, subtitle length or pause duration is specified. [C-04, C-10, C-13]

### Route vocabulary as a design aid

The following are analysis terms, not claims that every VN has these structures. [C-08]

| Unit | Question it should answer | Production implication to investigate |
|---|---|---|
| Scene | What changes in the situation, interpretation or relationship here? | Text, visual state, voice and transitions must agree with the selected context. |
| Local choice | Does this select an action, expression, interpretation or simply a passage? | Audit the performed response, not just the option label. |
| Shared sequence | Which experiences remain common before or between divergences? | Reused material may still require context-sensitive lines or performance. |
| Route | What sustained distinction organizes this traversal? | Entry and continuation conditions should not contradict prior commitments. |
| Ending | What conclusion or perspective is offered? | “Different” is not necessarily better, more complete or morally approved. |
| Cross-route knowledge | What may a returning reader know that the current protagonist does not? | Decide whether this disparity is intended and how the presentation handles it. |

A causal branch is one way to honor a consequential choice; an acknowledged expressive line is another kind of contribution, not its automatic substitute. Preserve the qualifications of reviewed Narrative structures and Consequence-preserving reconvergence. This entry does not repeat their experimental findings as if they were VN-specific validation. [C-08; reviewed dependencies D-01–D-02]

### Expression can be constrained without being trivial

Emily Short describes selecting visible dialogue from a larger repertoire through personality and wardrobe, as well as complications around what a player has actually deduced. That account supports studying curated expressive access rather than treating choice quantity as the entire design. It also reports post-launch clarification/revision, so it should not be read as an unqualified success story. [C-06; GDR-SRC-20261010-W02-004]

Tony Howard-Arias’s Scarlet Hollow account describes an early mismatch between the intended experience of certain traits and their delivered options, followed by revisions. This is a useful negative practitioner case: a trait label and a technically available line can still disagree with the role a player thinks they selected. The account’s design goals do not establish a universal rule that every trait choice must succeed. [C-07; GDR-SRC-20261010-G11-015]

The proposed bridge is to review **role promise → available expression → performed line → response**. Distinguish intentional characterization from accidental bait-and-switch. A flawed character may make an awkward statement by design; the problem is not awkwardness alone, but whether the player was allowed to understand the kind of contribution being chosen. [C-09]

### Rereading is a different state problem from route selection

Ren’Py documents dialogue history, saving/loading/rollback and persistent data separately. These facilities motivate a useful distinction among reading position, current-fiction state and cross-play records; they do not automatically enforce a project’s interpretation of those scopes. A control labeled “back” is therefore not a sufficient design contract. [C-05, C-10; GDR-SRC-20261010-G11-007; GDR-SRC-20261010-G11-008; GDR-SRC-20261010-G11-009]

A transcript may let a reader revisit what was said without reproducing the original gaze, vocal delivery or staging. Replaying a scene may reconstruct performance but introduce questions about whether state changes are applied again. Returning to a prior choice may intentionally change current events. These are different proposed products, with different authoring and regression obligations. [C-10, C-11]

## Conditional application process and alternatives

1. **Choose the offered role and consequence scope.** For a representative scene, state what remains authored, what the reader can select, and which outcomes are fixed. Avoid framing a pace control as a plot decision or an expressive line as a guaranteed route fork. [C-08, C-09]
2. **Map the reading event.** Record who is speaking, what the text means in context, what the image or voice adds, and when the reader can advance, pause, revisit or respond. Identify intentionally ambiguous information rather than making all subtext explicit. [C-04, C-12]
3. **Choose topology for the promise.** Use a fixed sequence, local branch, state-conditioned return, or sustained route because it preserves the valued distinction. Estimate the cost of affected scenes and variants before adding more branch points. If no valued distinction survives, either simplify or change the promise. [C-08]
4. **Select reader controls by task.** Decide separately about instant text, manual or automatic advance, stopping at choices, skipping known material, history, voice replay and changing earlier decisions. Review the actually exposed controls; a documented engine facility does not mean a game ships it. [C-05, C-10]
5. **Author state and localization contracts.** Separate current-story flags, reading history and cross-play records. Include relevant image/voice/context in translation review. Use the [state-safe rereading pattern](../patterns/state-safe-narrative-rereading.md) when a return feature could mislead or damage continuity. [C-10–C-12]
6. **Evaluate actual scenes across intended conditions.** Include first reading, interruption, repeated material with new context, and relevant language/access routes. Compare outcomes separately. Reduce or redesign the control if it misrepresents agency or cannot preserve its state contract. [C-13, C-14]

| Practical choice | Conditional advantage | Cost, contrary case or alternative |
|---|---|---|
| Page-like accumulated text | May support comparing parts of an extended passage. | Can alter focus/navigation burden; a smaller stable dialogue window may suit another task. No comparative benefit is established here. |
| Voiced performance | Can supply an authored interpretation that the project values. | Can conflict with reader pace, localization or alternative speech output; text-only delivery may be the more controllable production choice. |
| Hidden relationship state | Can keep numeric optimization from being the explicitly offered activity. | Can also obscure why options changed. Provide interpretable consequences when those are promised; no universal hidden/visible-state preference is established. |
| Route map or chapter return | Can expose revisit opportunities and limit repeated traversal. | Can spoil structure or misrepresent cross-route knowledge. A simpler history view may meet the actual need. |
| Deliberately irreversible choice | Can preserve a declared commitment model. | Can make mistaken input or missed information costly. Separate irreversible fictional commitment from inability to reread. |
| Repeated shared material | Can establish comparison or reinterpretation. | Can create unwanted repetition. Skipping should consider changed context rather than treating displayed-before as understood-before. |

The advantages above are proposed fit-to-purpose arguments, not measured outcome guarantees. [C-08–C-14]

## Applying shared topics and patterns

The [reviewed-dependency ledger](../reviews/full-run-20261010-g11-review-packet.md#reviewed-dependencies) identifies actual selected bytes and corrections. None is promoted to released guidance by being used here.

| Inspected shared entry | VN-specific adaptation | Boundary retained |
|---|---|---|
| `GDR-CAND-20261010-W01-TOP-01` Narrative structures | Separate fixed events, route traversal and reader interpretation. | The short interactive-story evidence is not a VN audience experiment. |
| `GDR-CAND-20261010-W02-TOP-01` Dialogue and voice | Review the option, performed line, visual/voice context, localized delivery and response together. | A reader may be interpreting subtext; do not universally replace utterances with intent labels. |
| `GDR-CAND-20261010-F02-TOP-01` Decision design | Distinguish information available before a route commitment from information revealed afterward. | Unexpected but intelligible outcomes differ from incomprehensible controls. |
| `GDR-CAND-20261010-P01-TOP-03` Accessibility and inclusive interaction | Evaluate settings, reading, focus, choices, saving and continuation as an actual task. | No universal native-game timing, contrast or text-size prescription is imported. |
| `GDR-CAND-20261010-P02-TOP-03` Multimodal communication | Decide how visual staging, voice, text and alternative speech can be attended to without losing required facts. | Redundant channels are not automatically additive or experientially equivalent. |

Use **`GDR-CAND-20261010-G11-PAT-02`**, [state-safe narrative rereading](../patterns/state-safe-narrative-rereading.md), for a concrete history/return contract. **`GDR-CAND-20261010-G11-PAT-01`**, [intent-preserving parser repair](../patterns/intent-preserving-parser-repair.md), applies only to a hybrid with free-form action input; it is not a default VN requirement. [C-10, C-11]

Use the existing `GDR-CAND-20261010-W02-PAT-01` for choice-to-performance intention, `GDR-CAND-20261010-W01-PAT-01` for qualified reconvergence, and `GDR-CAND-20261010-P02-PAT-02` for relevant alternative event information. G11 creates no duplicate of those techniques. Their formal adoption and domain ownership remain with coordination. [C-08, C-09, C-13]

In a mystery hybrid, a replay summary can accidentally reveal which interpretation is correct. In a relationship simulation, rereading a conversation should not secretly advance the calendar. In a fixed authored tragedy, permitting history does not imply that the reader can prevent the outcome. In a route-completion game, persistent unlocks can be intentional, but the current protagonist should not silently gain another route’s knowledge unless that is an explicit part of the fiction. These are illustrative tradeoffs, not verified claims about particular games. [C-10, C-11, C-15]

## Representative and negative cases

**Publisher boundary case — planetarian, 2024 Switch combined edition.** Its stated lack of choice-based branching defeats a universal branching criterion for this packet’s VN definition. It does not establish how any reader experiences control. The original Key product route was not retrievable, so the source is explicitly edition-limited. [C-03]

**Practitioner design-and-revision cases — Mask of the Rose and Scarlet Hollow.** These accounts expose constraints and reported mismatches in expressive systems. They support questions about role promises and learnability; they do not validate all later builds, reveal all player reactions, or supply independent replications. The two studios are separate contexts, while the repeated citations to either account remain one source each. [C-06, C-07]

**Technical counterexample — a history view is not rollback.** The inspected documentation distinguishes the facilities. The inference is that “rereading allowed” and “choice change allowed” should be reviewed separately. That distinction is more informative than treating every back-navigation feature as either cheating or unrestricted agency. [C-05, C-10]

### Illustrative worked example: the disputed promise

**Invented scene and control design; no game, prototype, performance or player test occurred.** A protagonist visits a former collaborator. The collaborator says a prior promise has been forgotten. The words can be read as accusation or resignation depending on what the current route has already established. The protagonist’s name and history are authored; the reader may choose the response, not rewrite that history. [C-15]

The proposed scene contract retains an uncertain motive. It offers “Ask what I promised” and “Acknowledge that I stayed away,” with performed lines that honor those different speech acts. Neither guarantees forgiveness. A later shared departure scene can preserve whether the protagonist requested clarification or accepted responsibility; otherwise the interface should not advertise that distinction as a lasting relationship consequence. This adapts W02-PAT-01 and W01-PAT-01, not a newly established G11 rule. [C-08, C-09, C-15]

| Reader action or production variant | Proposed treatment | Failure the review should catch |
|---|---|---|
| Reopen the exchange from history | View only the exchange already encountered in this run; return to the present scene afterward. | Relationship state or day counter changes merely from viewing it. |
| Replay the collaborator’s line | Retain the route-specific wording and performance association. | A replay uses the version from another route or conveys certainty absent from the first presentation. |
| Use instant text without voice | Keep the factual exchange and choice available; avoid a required cue that exists only during a transient animation. | A reader can see the words but cannot identify the speaker or relevant change. |
| Enable automatic advance | Provide a locally tested transition policy that does not skip an unresolved response. | A text-speed preference is mistaken for consent to choose a default response. |
| Translate a hesitant refusal | Review register, context, staging and the offered response, not just literal vocabulary. | The translated option becomes an accusation although the offered speech act was inquiry. |
| Encounter the same sentence on another route | Review whether changed context makes it newly informative. | A skip policy bypasses the first occurrence of the new interpretation-bearing event. |

The strongest version of the recommendation is not “give every reader every control.” It is **offer only controls whose meaning can be kept stable, and make restrictions compatible with the advertised activity**. A modest transcript with explicit limitations may be more honest than a scene-replay system that cannot preserve context. The effect on comprehension and preference remains a hypothesis. [C-10, C-11, C-15]

### Strong opposing aesthetic

**Illustrative fixed-performance work:** a scene intentionally depends on uninterrupted pacing. Arbitrary mid-beat skipping may undermine that composition. That is a reason to assess separate reading/performance modes or a limited return point, not a reason to hide inaccessible cues or deny the tradeoff. A second opposing case is a memory-centered mystery where an automatically interpreted journal removes the challenge. Rereading exact evidence and supplying its correct interpretation are different interventions. [C-04, C-10, C-13]

## Accessibility, ethics, localization and production implications

Ren’Py documents self-voicing and authored alternatives, but documentation availability is not evidence that every visual or interactive element in a game is understandable through those routes. The proposed acceptance task includes reaching settings, identifying speakers, perceiving meaningful scene changes, selecting or declining a response, revisiting material and returning without lost place. Keep the native-game design review distinct from applying an identified web standard to a web interface. No standards compliance or numerical threshold is certified here. [C-13; GDR-SRC-20261010-G11-012; reviewed D-04, D-07, D-09]

For production planning, bind revisions to the scene’s semantic obligations: what is known, who addresses whom, how a choice reads, how a line is performed and what later material depends on it. Ren’Py’s translation facilities illustrate that a localization can involve more than replacing dialogue strings. The genre-specific proposal is to audit the full interpretive beat across languages; this packet does not establish a universal workflow cost or quality formula. [C-12]

Voice commitments may increase the number of affected assets when a scene changes; a partially voiced or text-only approach can be a deliberate alternative. That is a production inference, not a measured cost estimate. Actual contracts, asset rights and implementation architecture require separate decisions. No voice cloning, actor reuse permission, publisher approval or external purchase is implied by this research. [C-04, C-12, C-16]

Do not interpret a route choice as proof of a reader’s identity, consent outside the fiction, or stable values. For intense content, propose discoverable and appropriately scoped content information, interruption controls and consent-based research; the design can preserve surprise without hiding participation conditions. These are proposed ethical safeguards, not a claim that every warning or recovery method has the same effect. [C-16]

## Research questions and proposed validation

**Proposed, not performed.** No reader was recruited and no build was tested. Obtain separate study/implementation authorization. Set participant recruitment, practical decision margins and analysis before collection; do not import a universal text speed or arbitrary sample size. [C-14, C-16]

| Question | Proposed comparison and procedure | Outcomes and important confounds | Finding that would reject or narrow the proposal |
|---|---|---|---|
| Does the offered choice preserve the intended role? | Use matched scenes with literal lines versus compact intent labels. Ask readers to predict the performed speech act before hearing it. Include readers familiar and unfamiliar with the cultural cues. | Choice comprehension, role fit, preference and perceived agency separately. Acting, translation and familiarity may alter interpretation. | Correct selection rises but the protagonist’s performed intent is misunderstood, or a label erases the intended interpretive task. |
| Can rereading preserve state understanding? | Compare transcript-only, explicitly changeable return and locked-choice rereading, each with clear naming and comparable access. Include interrupted and returning readers. | Prediction of what changes, lost place, accidental commitments, retained comprehension and preference. Memory and prior route exposure are confounds. | Readers systematically mistake viewing for reversal or the system changes facts outside the stated scope. |
| Which pacing control preserves the chosen experience? | Compare locally selected manual/automatic policies on the same scene; include voice-on, voice-off and relevant alternative-speech contexts. Counterbalance scene variants rather than claim a genre-wide speed optimum. | Speaker/event comprehension, attention reports, access effort, perceived pacing and preference. Reading proficiency and prior exposure must remain visible. | A policy improves throughput but loses required information or disrupts a promised performance goal. |
| Does skip preserve new contextual meaning? | Present repeated wording once with unchanged context and once with a changed interpretation-bearing context. Ask for predictions before the later decision. | Detection and comprehension of the changed situation, false skips and repetition burden. Do not equate a displayed-before marker with comprehension. | A skip policy suppresses newly relevant material or forces unneeded repetition without helping the declared outcome. |

### Coverage checkpoint

| Area | Current coverage | Unresolved evidence and next question |
|---|---|---|
| Definition and fixed/branching boundary | Working definition plus edition-specific publisher counterexample. | Wider cultural and historical boundary sources; which distinctions improve retrieval without exclusion? |
| Scene and display structure | Official technical examples and conditional analysis. | Actual builds and performances; how does page/line arrangement affect a particular task? |
| Expression and protagonist role | Two firsthand creation/revision accounts. | Independent player evidence and unfamiliar cultural contexts; when is restriction expressive rather than misleading? |
| Routes and consequence | Inspected shared narrative candidates applied conditionally. | VN-specific causal/replay evidence; what valued distinction persists? |
| Rereading and cross-play state | Technical separation and G11-PAT-02 proposal. | Executed state behavior and reader-model evidence; what does each return operation really change? |
| Localization and access | Documented facilities, scoped P01/P02 transfer and proposed process. | Native-language primary production accounts, target devices and representative access tests. Educational-study leads are not admitted results. |

The next decision is an independent review of the genre boundary, reader-control recommendation and evidence limits. A complete draft file is not complete genre coverage or a release decision.

## Claim ledger

Claim IDs are local to this artifact. Confidence describes the stated claim, not approval or universal applicability. Proposed application claims remain untested.

| Claim | Material claim | Class | Support and precise locator | Confidence and limit / unresolved question |
|---|---|---|---|---|
| C-01 | Use staged reading and visual presentation as a provisional VN boundary, independently of route count. | inference | GDR-SRC-20261010-G11-006 opening display comparison; GDR-SRC-20261010-G11-014 publisher description; comparison with IF candidate | Moderate as a routing aid; not a complete cultural history, formal taxonomy or prevalence claim. |
| C-02 | Ren’Py documents ADV/NVL presentation differences as interface conventions. | observed-example | GDR-SRC-20261010-G11-006, opening comparison and Menu Choices | High for documented distinction, not a complete classification or tested display effect. |
| C-03 | A specified planetarian publisher description calls the work a visual novel while excluding choice-based story branching. | observed-example | GDR-SRC-20261010-G11-014, product description and release fields | High for publisher artifact; executable and other editions unverified; no satisfaction claim. |
| C-04 | Review text, voice, image and advance behavior as a coordinated scene, not a universal pacing formula. | hypothesis | GDR-SRC-20261010-G11-010 Preferences; GDR-SRC-20261010-G11-013 Voice; illustrative fixed-performance counterexample | Moderate for identifying dependencies; low for comparative pacing or comprehension benefits. |
| C-05 | History, save/rollback and cross-play persistent data are documented as distinct facilities. | observed-example | GDR-SRC-20261010-G11-007 opening/HistoryEntry; GDR-SRC-20261010-G11-008 Rollback; GDR-SRC-20261010-G11-009 opening | High for documentation; project state invariants and native behavior untested. |
| C-06 | Mask of the Rose’s creator describes a constrained expressive repertoire and subsequent clarification/revision. | practitioner-heuristic | GDR-SRC-20261010-W02-004, personality/wardrobe and revised-system passages | Moderate for retrospective; benefits and precise build not independently verified. |
| C-07 | Scarlet Hollow’s creator reports early trait-expression mismatches and revisions; these do not establish universal trait-success rules. | practitioner-heuristic | GDR-SRC-20261010-G11-015, design rules and failure/patch paragraphs | Moderate for creator report; no replayed build or survey analysis here. |
| C-08 | Choose scene/route topology for the promised distinction rather than the number of branches. | inference | Reviewed D-01 Narrative structures, D-02 reconvergence; C-03 | Moderate as an analysis; shared experimental evidence not VN-specific efficacy. |
| C-09 | Audit role promise through performed response and measure attention, comprehension, agency and preference independently. | hypothesis | Reviewed D-03 dialogue, D-06 intent contract, D-08 decision design; C-06–07 | Low as an improvement claim; test participant interpretation rather than assume preference. |
| C-10 | Reader-control meaning should distinguish viewing from revising and avoid silent state changes. | hypothesis | C-05; G11-PAT-02 recipe and playtest | Moderate for logical scope consistency; low for experience benefits until tested. |
| C-11 | Displayed-before text is not necessarily the same context or a comprehended event; skip/replay need a declared policy. | hypothesis | C-05; reviewed D-01 discovery/persistence distinction; illustrative disputed-promise scene | Low for empirical effects; current implementation and comprehension unknown. |
| C-12 | Localization review should include the scene’s speech act, context and performance obligations, not only words. | hypothesis | GDR-SRC-20261010-G11-011 translation units/tips; reviewed D-03; C-04 | Low for measured outcomes; native-language and culturally specific production evidence incomplete. |
| C-13 | Validate the full reading/choice/recovery task through intended access routes without assuming modality equivalence. | hypothesis | GDR-SRC-20261010-G11-012 self-voicing/alt text; reviewed D-04, D-07, D-09 | Moderate as a diagnostic process; no current-build access certification or standards claim. |
| C-14 | Controlled comparisons must preserve outcome distinctions and test changed context, not just completion or dwell. | hypothesis | Author-designed tests; reviewed D-05 transfer discrimination, D-08 decision interpretation | Low until performed; order, language, familiarity and performance are confounds. |
| C-15 | The disputed-promise example illustrates proposed commitments and failure checks, not a validated design. | hypothesis | Worked example and hybrid counterexamples in this entry | Low; wholly illustrative, no code, voice recording or player result. |
| C-16 | Reader research and production need explicit consent, privacy and rights decisions, independent of research approval. | hypothesis | Author-proposed ethical/production safeguards; G11 authorization boundary | Moderate as a precaution; no legal assessment or implementation approval. |

## References

Access date for every record below: **2026-10-10**. “Observed example” refers to an inspected document or source artifact unless explicitly stated otherwise; no game executable was run. Source identities are temporary; global deduplication and permanent allocation remain pending.

### GDR-SRC-20261010-G11-006
**Ren'Py project. NVL-Mode Tutorial.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [NVL-Mode Tutorial](https://www.renpy.org/doc/html/nvl_mode.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Opening ADV/NVL comparison; “Getting Started”; “Menu Choices”.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Presentation modes in a particular engine, not exhaustive genre definitions. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-007
**Ren'Py project. Dialogue History.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Dialogue History](https://www.renpy.org/doc/html/history.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Opening description; HistoryEntry fields; rollback_identifier.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** History entries and rollback references are distinct; a history pane is not a complete record of all audiovisual context. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-008
**Ren'Py project. Saving, Loading, and Rollback.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Saving, Loading, and Rollback](https://www.renpy.org/doc/html/save_load_rollback.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** What is Saved; Saving and Loading; Rollback; Blocking Rollback; Fixing Rollback.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Engine-specific state and custom-screen constraints. Vendor judgments about blocking rollback are practitioner advice, not an effect experiment. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-009
**Ren'Py project. Persistent Data.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Persistent Data](https://www.renpy.org/doc/html/persistent.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Opening distinction from data tied to a game point; persistent data example; merging discussion.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Cross-play persistence is not the same scope as a story save. No project reset policy or implementation verified. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-010
**Ren'Py project. Screen Actions, Values, and Functions.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Screen Actions, Values, and Functions](https://www.renpy.org/doc/html/screen_actions.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Preferences: text speed; skip; after choices; auto-forward; wait for voice.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Preference facilities are documented, not proof that a shipped UI exposes them or that a particular speed is effective. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-011
**Ren'Py project. Translation.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Translation](https://www.renpy.org/doc/html/translation.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Primary and Alternate Languages; Translating Dialogue; translation units; tips concerning language changes.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Text, interface, style and image facilities do not prove equivalent cultural interpretation. Identifier stability and replayed translation-block effects require project-specific review. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-012
**Ren'Py project. Self-Voicing.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Self-Voicing](https://www.renpy.org/doc/html/self_voicing.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Opening behavior; clipboard and debug modes; alt text and translation discussion.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Documented assistive facilities are not universal platform or disability coverage. No self-voicing, screen-reader, or native/mobile run performed. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-013
**Ren'Py project. Voice.** Publication/update: unknown (page update); version banner checked 2026-10-10. Publisher: Ren'Py documentation.
**URL:** [Voice](https://www.renpy.org/doc/html/voice.html).
**Edition/build:** 8.5.4 documentation banner; no installed runtime verification. **Locator:** Opening voice statement behavior; voice tags; automatic voice; translated voice; voice replay functions.
**Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Limits/independence:** Engine documentation, not audience evidence that voice improves comprehension or preference. Audio builds and delivery platforms untested. Same documentation family as G11-006–013; these are not independent effect studies.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-014
**PROTOTYPE (publisher-supplied description); Nintendo storefront. planetarian: The Reverie of a Little Planet & Snow Globe.** Publication/update: Release listed 2024-06-27; storefront update unknown. Publisher: Nintendo / PROTOTYPE.
**URL:** [planetarian: The Reverie of a Little Planet & Snow Globe](https://www.nintendo.com/us/store/products/planetarian-the-reverie-of-a-little-planet-and-snow-globe-switch/).
**Edition/build:** Nintendo Switch digital combined edition; installed build unknown. **Locator:** Product description naming visual novel; note excluding choice-based story branching; publisher and release-date fields.
**Access:** `relevant-excerpt`. **Type:** Publisher description in official storefront. **Limits/independence:** A primary artifact describing one edition, not directly observed gameplay. Marketing claims about immersion not adopted; not interchangeable with the original or other ports.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-G11-015
**Tony Howard-Arias, co-founder of Black Tabby Games. Designing Scarlet Hollow’s trait-based roleplaying system.** Publication/update: 2021-01-13. Publisher: Black Tabby Games / Medium.
**URL:** [Designing Scarlet Hollow’s trait-based roleplaying system](https://blacktabbygames.medium.com/designing-scarlet-hollows-trait-based-roleplaying-system-24f2b4f4906).
**Edition/build:** Episode 1 development account; discusses a prior December patch; exact builds unknown. **Locator:** Opening trait-design rules; paragraph beginning “There were a few ways that we failed”; following patch account.
**Access:** `relevant-excerpt`. **Type:** Firsthand developer rationale and retrospective. **Limits/independence:** Developer-reported failures and revisions, not independently verified player effects. Distribution graphs and survey proportions not used. Historical counts differ within the account; no current trait-count claim.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

### GDR-SRC-20261010-W02-004
**Emily Short. Dialogue Expressiveness in Mask of the Rose.** Publication/update: 2023-11-22. Publisher: Emily Short’s Interactive Storytelling.
**URL:** [Dialogue Expressiveness in Mask of the Rose](https://emshort.blog/2023/11/22/dialogue-expressiveness-in-mask-of-the-rose/).
**Edition/build:** Retrospective describing launch and subsequently revised system; exact game build unknown. **Locator:** Opening description of wardrobe/personality-filtered dialogue; player encountered versus player-deduced facts; reported post-launch clarification/revision.
**Access:** `relevant-excerpt`. **Type:** Firsthand creative/practitioner account. **Limits/independence:** Reuse exact W02 identity. Text inspected; embedded game screenshots and executable not used as behavior evidence. Expressivity and agency goals are creator intent, not validated effect sizes.
**Rights:** Copyright retained by the source owner; paraphrase and bibliographic links only; no source assets redistributed. **Claim use:** See the entry’s claim ledger; a lead-only source supports no substantive claim.

## Review and history

Version **0.1.0**, candidate revision **initial-draft-1**; no predecessor or supersession is asserted. The [batch packet](../reviews/full-run-20261010-g11-review-packet.md#candidate-byte-receipt) holds the exact SHA-256. Author self-review is not independent review. Reviewer, approved_by and approved_date remain null.

Open local contradictions: G11-CON-01 (consequence), G11-CON-03 (return versus commitment), G11-CON-04 (performance versus reader control), G11-CON-05 (fact access versus interpretation), and G11-CON-06 (genre boundary and source selection). Review does not approve publication, game adoption, engine work or canonical classification. Coverage remains open.

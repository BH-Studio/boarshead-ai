---
id: GDR-CAND-20261010-G03-GEN-01
kind: genre
title: Action adventure
version: 0.1.0
status: draft
candidate_revision: initial-capture-1
predecessor_sha256: null
supersedes: null
change_summary: Initial G03 capture; no earlier G03 artifact superseded.
run_id: GDR-FULL-20261010
batch_id: G03
attempt_id: G03-attempt-01
identity_scope: run-scoped-temporary-candidate
owner_project: BH-GDR-Genres
updated: '2026-10-10'
evidence_checked: '2026-10-10'
date_timezone: America/Los_Angeles
input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate + supplied G03 brief + inspected
  first-wave selected-draft excerpts
aliases:
- action-adventure
- action adventure games
tags:
- mixed-demands
- exploration
- authored-progression
- conditional-assistance
- genre-boundaries
related_topics:
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-W01-TOP-01
related_patterns:
- GDR-CAND-20261010-G03-PAT-01
- GDR-CAND-20261010-G03-PAT-02
- GDR-CAND-20261010-F01-PAT-01
related_genres:
- GDR-CAND-20261010-G03-GEN-02
- GDR-CAND-20261010-G03-GEN-03
source_ids:
- GDR-SRC-20261010-G03-005
- GDR-SRC-20261010-G03-013
- GDR-SRC-20261010-G03-010
- GDR-SRC-20261010-G03-011
- GDR-SRC-20261010-G03-003
- GDR-SRC-20261010-G03-006
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-G03
hash_record: ../reviews/full-run-20261010-g03-review-packet.md#candidate-inventory
---

# Action adventure

**Research candidate, not released guidance.** This entry covers decisions at the junction of real-time action and authored discovery. It does not define a universal audience, certify a game classification, or authorize implementation. Claims are local to this file; confidence concerns the precise claim, not a recommendation’s popularity.

## Definition and boundaries

For this entry, **action adventure** is an analytical label for an experience in which real-time execution—such as traversal, evasion or combat—and exploration or authored discovery both materially constrain progress. The useful question is what each demand contributes and how their gates interact, not whether a game reaches an invented percentage of fighting. Combat is a possible action demand, not a mandatory ingredient. This working definition is an **inference**, not an approved taxonomy change. [C-01]

The label overlaps with [adventure](adventure.md), platforming, role-playing, stealth and systemic exploration. A platforming challenge with incidental fiction does not automatically require this guidance; a dialogue-led adventure does not become action adventure merely because the player occasionally clicks quickly. Conversely, a game can offer substantial reasoning and still contain demanding execution. Identify the actual repeated decisions before transferring a rule. The source evidence for a creator describing action and puzzles is separate from evidence that their combination improves experience. [C-01; GDR-SRC-20261010-G03-005]

This file owns the **conditional combination**: action can prevent the player reaching a clue, an authored event can override an otherwise valid physical solution, and repeated combat can change the cost of investigating an interpretation. It does not replace the shared movement, combat, difficulty, narrative or camera topics. Multiplayer, platform, camera perspective and tone remain facets. [C-02]

## Custom research instructions

For subsequent research or design review, construct a gate map with separately named **arrival, information, inference, execution, resource and authored-state requirements**. Ask which requirement blocks a player who already understands the solution. Ask the reverse: can execution skill bypass the inference the scene was intended to demand? Record whether either outcome is acceptable before proposing a fix. [C-02]

Inspect creator accounts, original studies and versioned examples from at least meaningfully different combinations when resources permit: execution-heavy exploration, puzzle-led action, noncombat traversal and systemic alternatives. This is a sampling strategy, not a numerical evidence quota. For each game, record the basis for membership separately from intended design and demonstrated player effects. Future observations need a platform, build, scene, reproduction steps or recording timestamps; this entry supplies none of those as completed observations. [C-01; C-14]

Challenge these attractive but unsupported shortcuts: adding combat makes an adventure engaging; all demands should share a difficulty setting; every puzzle needs one intended physical solution; removal of travel always improves pacing; safe exploration is necessarily boring; and a bypass grants an equivalent puzzle experience. Treat each as a question, not a premise. Trace inaccessible controls before diagnosing a lack of mastery. [C-03–C-07]

## Player promises and varied audiences

Candidate promises include competence under pressure, discovery through movement, intelligible consequences, and opportunities to investigate without losing an unreasonable amount of progress. They can conflict. A player seeking mechanical mastery may welcome repeated execution; a player seeking the next discovery may experience the same repetition as an unrelated toll. Neither preference follows from the genre label alone. [C-02; C-08]

Heath Smith’s interview about *Shadow of the Tomb Raider* gives a creator rationale for separating combat, puzzle and traversal difficulty. That is evidence of a production choice responding to different intended preferences, not a measured distribution of adventure audiences. It motivates asking whether the demands can be adjusted independently in the present design. [C-03; GDR-SRC-20261010-G03-010]

A declared challenge promise still matters. Removing the timing requirement from a scene whose point is synchronizing movement and observation can change the activity rather than merely remove an obstacle. Name the supported modes and consequences honestly; avoid presenting assistance as either shameful or experientially identical. [C-08]

## Characteristic loops and structures

A useful **diagnostic model**, not a required formula, is: notice a destination or question → reach or investigate it → form a model → act under the relevant constraints → observe the consequence → revise the route or interpretation. A scene may omit or reorder these stages. Across a session, the critical structure is the dependency between discoveries and capabilities; across a longer progression, it is what changes the available questions and actions. [C-02]

Three structural choices deserve separate treatment. **Sequential coupling** makes the player succeed at action before investigating. It gives the author control over arrival but risks blocking discovery for an unrelated execution difficulty. **Embedded coupling** requires interpretation during action. It can make observation tactically meaningful, but reading, aiming and moving compete in the same moment. **Loose coupling** permits investigation first or offers alternative approaches; it broadens route choice while increasing the states that dialogue, checkpoints and progression must handle. These are proposed analytical alternatives, not ranked industry laws. [C-02; C-08]

In Nintendo’s creator account, river crossing need not require a polished raft, or even a raft at all. This is a countercase to treating the author’s illustrated solution as the only valid route. It does not show that every puzzle should accept every physically imaginable solution. Decide whether a gate tests an outcome, a particular capability, or a story event; otherwise systemic freedom and authored checks can silently contradict each other. [C-04; C-09; GDR-SRC-20261010-G03-013]

## Applying shared topics

Only the following inspected **reviewed-candidate excerpts** are transferred. They remain draft; their public references were not all reinspected in G03.

| Shared candidate | What changes at the action/adventure boundary | Limit on transfer |
| --- | --- | --- |
| `GDR-CAND-20261010-F01-TOP-03`, Learning and onboarding | Diagnose failed interpretation separately from input and execution. Re-entry may need known facts and controls, not a solved puzzle. | Does not establish a universal tutorial or prompt-fading schedule. |
| `GDR-CAND-20261010-F01-PAT-01`, Supported attempt and transfer check | When testing rule learning, vary cases so the correct answer changes; record prediction separately from chosen action. | Never treat repeating the demonstrated answer as transfer; never fade an accommodation. |
| `GDR-CAND-20261010-P01-TOP-02`, Interface and information | State what information the player is entitled to receive while moving or under threat, and what is intentionally uncertain. | Diegetic placement alone does not establish readability. |
| `GDR-CAND-20261010-P01-TOP-03`, Accessibility and inclusive interaction | Separate access to required information, operation, recovery and resulting experience. | No WCAG/XAG numbers are generalized into a native-game threshold here. |
| `GDR-CAND-20261010-W01-TOP-01`, Narrative structures | Distinguish the order of past events from the order in which action permits their discovery; explain where physical freedom stops changing authored outcomes. | Recognized feedback is not automatically an equivalent substitute for consequential choice. |

These adaptations are inferences and test proposals, not new empirical findings. [C-10]

**Missing links:** F03 Progression and rewards; W02 Quests and objectives / Dialogue and voice; W03 Level and spatial design / World structure and exploration; P02 Controls and input / Feedback and game feel; P03 Camera and framing / Platform and display context. Their current bytes and independent-review outcomes were not captured here. Do not substitute a remembered first draft or invent candidate IDs for them. F02 challenge-related outputs are also not inspected. Current public sources support this bounded draft without certifying those dependencies. [C-14]

## Conditional application process

**Diagnose the actual obstruction.** For each important transition, write what the player may know, do and change before and after it. Distinguish a clue that was never available from one that was available but interpreted differently. Log a failed jump separately from choosing the wrong destination. A “stuck” count alone cannot tell the author which demand failed. [C-02; C-10]

**Choose what must remain coupled.** Preserve coupling when the intended challenge genuinely concerns simultaneous perception and execution. Otherwise compare separated settings, an alternate route, different retry placement, or a less demanding action with the same story consequence. Do not add a combat encounter merely to fill the interval between discoveries. [C-03; C-08]

**Specify acceptance and recovery.** State whether the gate accepts an outcome or an exact sequence. If it accepts multiple physical solutions, reconcile their resource and authored-state effects. For an intended irreversible consequence, provide an intelligible commitment rather than an accidental save-state trap. Apply the [Recoverable dependency gate](../patterns/recoverable-dependency-gate.md) selectively. [C-09]

**Offer the right kind of help.** A reminder of an already discovered route, input assistance and a direct puzzle answer solve different problems. The [Player-requested state-aware hints](../patterns/player-requested-state-aware-hints.md) candidate can address a reasoning blockage only after the information and interface remain usable. A puzzle skip is an alternate progression route, not proof that reasoning has become accessible. [C-05; C-10]

**Evaluate both gains and losses.** Assess intended challenge, discovery, unnecessary replay and player control separately. Remove or revise the intervention if it solves the wrong problem, causes spoilers, or destroys the coupling the audience deliberately selected. The test design below is proposed, not executed. [C-11]

## Pattern selection and hybrid conflicts

**`GDR-CAND-20261010-G03-PAT-01` — Recoverable dependency gate:** prioritize the boundary where combat consumption, route changes or checkpoint restoration can invalidate later discovery. Adapt it to state the allowed consequences of failure; do not silently turn a survival-oriented resource commitment into an unlimited refill. [C-09]

**`GDR-CAND-20261010-G03-PAT-02` — Player-requested state-aware hints:** useful when investigation has multiple live questions and the player requests help on one. Keep unsolicited solution hints out of an action attempt unless requested as part of the selected assistance mode. A factual access cue must not be withheld to preserve a “pure” hint-free mode. [C-10]

A restorative-exploration hybrid may require intervals free from threat, while an action-focused mode may rely on persistent uncertainty. No label wins automatically. Specify where each promise applies, whether pressure can be paused or configured, and what information remains available. This is a local proposal requiring design approval and evaluation, not an audio rule or a claim that all adventures require tension. [C-08]

## Worked example — illustrative, not a shipped-game observation

**The tidal observatory.** A player seeks a sealed archive. The proposed scene offers a tide gauge, an old maintenance sketch and a control room beyond a hazardous causeway. The intended inference is that the mechanism can be disengaged when its counterweight is unloaded; reaching the control room is a separate execution demand. All details in this example are invented. [C-12]

An initial design requires defeating sentries, crossing the causeway and reading a small gauge while enemies continue attacking. A player can understand the mechanism yet repeatedly fail to reach the controls. Another can win the fight but misread the gauge. Calling both failures “hard puzzles” conceals different causes. The designer therefore defines a protected inspection position, keeps the risky crossing for players selecting it, and proposes an alternate lower-execution route that reaches the same control state. These are comparison candidates, not established improvements. [C-12]

The gate accepts unloading the counterweight by either draining its tank or mechanically supporting it; it does not require a particular tool animation unless that tool is the actual capability being taught. A save made after the tank drains must not restore the gate as if the tank were full. An optional hint first asks whether the player wants help reaching the controls or interpreting the mechanism; it does not reveal the archive’s contents. [C-09; C-12]

**Counterexample:** in a deliberately coupled timing scene, the challenge might be to observe a moving counterweight and cross during its unloaded phase. Separating observation from execution would remove the core task. Offer an honestly described alternate mode or route where appropriate, but do not call that mode identical or infer failed execution means misunderstanding. [C-08; C-12]

## Representative cases and negative cases

| Evidence route and context | What this entry may use | What it may not infer |
| --- | --- | --- |
| Nintendo, 2023 pre-release *Tears of the Kingdom* interviews; Switch context | Creator descriptions of action/puzzles and alternative river-crossing solutions. Analytical relevance to mixed demands. [C-01; C-04] | A definitive genre classification, observed player reactions, or proof of superior systemic design. |
| Heath Smith interview, 2018 pre-release *Shadow of the Tomb Raider* | Rationale for independently adjustable challenge categories. [C-03] | Verified current menus, audience percentages or causal satisfaction gains. |
| Naughty Dog’s original-release accessibility documentation, with later patch references | Documented puzzle skipping and a stated limit on puzzle accessibility. [C-05] | Equal access to the skipped inference, or a current build audit. |
| Mobius’s 2015 *Outer Wilds* narrative prototypes | A creator-reported warning that stripping travel can concentrate narrative too heavily. [C-06] | A finding that travel always improves pacing or that these prototypes reproduce the shipped game. |

This is a purposive, English-accessible sample, biased toward documented productions. It does not cover every regional tradition, audience, action style or independent failure. Commercial success is not an outcome measure in this analysis. [C-14]

## Accessibility, localization, ethics and production

For action scenes containing clues, distinguish **perception**, **interpretation**, **operation** and **recovery**. Pause/recap options, alternate controls, readable labels and multimodal facts are proposed responses to particular barriers, not a checklist that certifies equal experience. Avoid requiring an inaccessible condition as the baseline in a future study. Numerical display and input settings require the relevant verified platform guidance; none is prescribed here. [C-10]

Localizing a clue can change its relationship to a timed action: a spoken explanation may finish after the opportunity passes, or an idiom may no longer justify the intended inference. Review the causal clue relationship and timing together, rather than merely checking that the translated string fits. These are risks to investigate, not measured defect rates. [C-13]

Alternative solutions multiply the combinations that checkpointing, resources, cinematics and dialogue must accommodate. Limit this cost by naming supported outcomes and rejecting unsupported interactions clearly, rather than promising limitless freedom. Preserve genuine alternatives that the selected design can afford to author and verify. No fixed production-cost multiplier follows from the inspected accounts. [C-04; C-09; C-13]

Do not make assistance contingent on public disclosure of disability, punitive labels, purchases or an assertion that one play style is authentic. A bypass, nonviolent route or lower-execution option should state its actual consequences. These are proposed ethical constraints, not already approved studio decisions. [C-13]

## Research questions and validation

**All tests below are proposed and NOT PERFORMED.** Recruitment, prototype execution and game implementation are not authorized by this packet. [C-11]

| Question | Proposed comparison and measures | Confounds and discriminating decision |
| --- | --- | --- |
| Is execution blocking an understood discovery? | Compare the same information with alternative execution demands; record the player’s prediction, chosen action, execution outcome, retry burden and requested help. | Changing the route can change information exposure. Retain the separation only if the intended discovery remains interpretable and the selected challenge promise is not unintentionally removed. |
| Does coupling add the intended experience? | Compare embedded observation/action with a protected inspection interval, preserving the rule and required information. Ask about mastery, discovery, frustration and agency separately. | Novelty, action skill and preference can explain differences. Reject a universal recommendation if relevant participants value the coupled task or if the separated scene becomes mere busywork. |
| Does a rule transfer rather than an answer repeat? | Use new surface cases where applying the same rule yields different correct predictions; distinguish prediction from a preferred risky action. Keep access accommodations constant. | Memorized responses and repeated test exposure contaminate transfer. One correct prediction is insufficient evidence of durable learning. |
| Can legitimate alternate solutions and recovery states coexist? | Specify future technical cases covering each supported route, failure, resource commitment and interrupted transition. Pair these with comprehension questions in a separately authorized study. | Technical state consistency does not show that a route is inferable or enjoyable. Reject the gate specification if a supported solution strands progress or silently contradicts the promised outcome. |

Choose participants by the question: relevant execution experience, puzzle familiarity, access requirements, input devices, languages and preference for coupled challenge. Do not infer subgroup generality from a convenience sample. Set project-specific accept/revise criteria before observing results; no universal duration, error rate or sample size is supported here. [C-11; C-13]

### Coverage and next discriminating questions

| Subtopic | G03 coverage | Remaining gap / next question |
| --- | --- | --- |
| Mixed execution, exploration and authored gates | Operational model and contrasting creator accounts | When is coupling a valued task rather than a barrier? |
| Alternative solutions and state consistency | Creator countercase plus conditional recovery recipe | Which outcomes can the actual progression/narrative system support? |
| Discovery pacing and interruption | Prototype account and worked comparison | Does quiet inspection or pressured interpretation serve this audience? |
| Difficulty and access | Separate-demand rationale and documented bypass limits | Which demands remain inaccessible, even with a bypass? |
| Controls, camera, spatial layout | Risks and dependency map only | Inspect P02/P03/W03 candidates and relevant versioned builds before technical recommendations. |
| Population and cross-cultural effects | Not established | Obtain suitable direct evidence rather than extrapolating from named games. |

## Claim ledger

| ID | Precise claim / role | Class | Support and locator | Confidence, limit and unresolved question |
| --- | --- | --- | --- | --- |
| C-01 | The working label identifies substantial action/discovery coupling; it is not a universal threshold or approved taxonomy. | inference | 005, Part 1 introduction; comparison with the supplied G03 brief’s distinct genre questions. | Moderate as an analytical tool, low as universal membership rule; boundaries remain contested. |
| C-02 | Separately recording arrival, knowledge, inference, execution, resource and authored-state requirements can expose different design decisions. | inference | 005 action/puzzle account; 010 creator’s separated demands; inspected F01/P01/W01 excerpts. | Moderate explanatory plausibility; diagnostic usefulness in a project remains untested. |
| C-03 | Smith describes a rationale for separating combat, puzzle and traversal difficulty. | practitioner-heuristic | 010, Smith interview paragraphs. | High confidence in attribution, not in effectiveness or population prevalence. |
| C-04 | Nintendo’s creators describe alternative river crossings and combination-related production work. | practitioner-heuristic | 013, combination-adjustment and river-crossing paragraphs. | High confidence in the account; no observed build or causal outcome. |
| C-05 | Naughty Dog documents a puzzle skip and acknowledges that some puzzles were not fully accessible in the documented context. | observed-example | 011, Navigation and Traversal / Skip Puzzle Option. | High for documentation, bounded to its dated context; bypass is not experience equivalence. |
| C-06 | A Mobius prototype account reports narrative concentration as a problem when travel was abstracted away. | practitioner-heuristic | 003, From Paper to Processing. | Moderate; undocumented sample and formative setting limit transfer. |
| C-07 | More assistance should not automatically be interpreted as better experience or better learning. | inference | 006, performance, subjective measures and discussion; 011 puzzle skip documentation. | Moderate bounded caution; short visual-search findings do not test adventure discovery. |
| C-08 | Separate challenge channels or safe inspection may help when demands are incidental to one another, but can harm an intentionally coupled task. | hypothesis | Bridge from C-02/C-03/C-06; counterexample in worked scene. | Low for predicted benefits; compare the actual audience and challenge promise. |
| C-09 | Gates should state accepted outcomes and recovery/commitment behavior rather than silently rely on one illustrated sequence. | hypothesis | 013 alternatives; G03-PAT-01 evidence chain; W01 state/promise distinctions. | Low as a complete intervention; deliberate irreversible designs remain countercases. |
| C-10 | Access, hinting and rule learning require different checks; transfer probes need discriminating answers and retained accommodations. | inference | Inspected F01-PAT-01 corrected recipe; P01-TOP-02 information contract; P01-TOP-03 access chain. | Moderate as bounded transferred guidance; these sources remain reviewed drafts, not fresh empirical verification. |
| C-11 | The proposed comparisons can challenge coupling and help recommendations; no tests or outcomes are reported. | hypothesis | Test specifications in this entry, derived from C-08–C-10. | Low until implementation and observation; criteria must be set locally. |
| C-12 | The tidal-observatory scene illustrates distinct gate demands and a coupled-task counterexample. | hypothesis | Author-created illustrative example; no external game evidence claimed. | Low; feasibility, comprehensibility and effects untested. |
| C-13 | Localization, ethical labeling and state-authoring costs should be reviewed as constraints on the proposed interventions. | hypothesis | Conditional analysis from P01/W01 excerpts and C-04; not a measured cost model. | Low for project-specific effects; needs audience and production validation. |
| C-14 | G03 supplies bounded coverage, not complete population evidence, current-build inspection or verified missing dependencies. | inference | Actual G03 inspection/access record and supplied dispatch. | High for session limits; unknown content is not treated as absent from the wider library. |

Source suffixes in this ledger expand to `GDR-SRC-20261010-G03-<nnn>`. Unresolved conflicts: `G03-CON-01` (coupling versus decoupling), `G03-CON-02` (freedom versus authored constraints), `G03-CON-03` (help versus discovery), and `G03-CON-05` (study wording inconsistency). See the packet; these are local review labels, not global register allocations.

## References

Access date for every record below: **2026-10-10, America/Los_Angeles**. Web-text line numbers identify this inspected retrieval; headings and named paragraphs are the portable locators. A source identity is temporary, reused within G03; cross-batch canonical URL/DOI/edition deduplication remains pending.

### GDR-SRC-20261010-G03-005

**Nintendo interview with Eiji Aonuma, Hidemaro Fujibayashi, Takuhiro Dohta, Satoru Takizawa and Hajime Wakai. [Ask the Developer Vol. 9, The Legend of Zelda: Tears of the Kingdom—Part 1](https://www.nintendo.com/us/whatsnew/ask-the-developer-vol-9-the-legend-of-zelda-tears-of-the-kingdom-part-1/).** Nintendo. Date: 2023-05-09.

**Edition/context:** Official English translation of Japanese interview; pre-release Nintendo Switch context. **Access:** `relevant-excerpt`. **Type:** Firsthand creator interview, publisher-mediated.

**Inspected locator:** “Part 1: What to change, and what to keep”; Aonuma’s series introduction and discussion of diving as travel/information gathering. Web-text lines 69–132; dateline/translation note lines 47–53.

**Support in this artifact:** C-01/C-02: creator description informs a qualified working definition.

**Limits:** Self-description and intended design, not a definitive genre taxonomy or evidence that feature combinations cause enjoyment. No Switch build or recording inspected. **Independence:** Same interview series and production as 013; do not count as independent corroboration.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-013

**Nintendo interview with Hidemaro Fujibayashi, Takuhiro Dohta, Satoru Takizawa, Eiji Aonuma and Hajime Wakai. [Ask the Developer Vol. 9, The Legend of Zelda: Tears of the Kingdom—Part 4](https://www.nintendo.com/us/whatsnew/ask-the-developer-vol-9-the-legend-of-zelda-tears-of-the-kingdom-part-4/).** Nintendo. Date: 2023-05-09.

**Edition/context:** Official English translation; pre-release Nintendo Switch context. **Access:** `relevant-excerpt`. **Type:** Firsthand creator interview.

**Inspected locator:** “Part 4: What makes the game The Legend of Zelda-like”; combination-adjustment and river-crossing alternatives, web-text lines 73–84 and 99–112.

**Support in this artifact:** C-04; rationale for C-09/C-13, not their validation.

**Limits:** An account of intended alternatives and production effort, not G03 observation or causal success evidence. Translation and company mediation remain relevant. **Independence:** Same interview/production as 005.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-010

**Steve Wright, interviewer; Heath Smith, Eidos Montréal lead game designer, interviewee. [Eidos Montreal on Shadow of the Tomb Raider’s difficulty settings](https://stevivor.com/features/interviews/eidos-montreal-shadow-tomb-raiders-difficulty-settings/).** Stevivor. Date: 2018-08-10.

**Edition/context:** Pre-release interview for Windows PC, Xbox One and PS4; no executable/build inspected. **Access:** `relevant-excerpt`. **Type:** Original interview containing firsthand creator statements.

**Inspected locator:** Article body and Smith’s three quoted paragraphs; web-text lines 464–478.

**Support in this artifact:** C-03 and rationale for C-02/C-08.

**Limits:** Supports creator rationale for separating combat, puzzle and traversal difficulty, not current setting specifications or measured satisfaction. Reporter interpretation is not treated as an experiment. **Independence:** Independent production from Nintendo/Mobius/Gilbert; external interview mediation, not independent testing of the claimed benefits.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-011

**Matthew Dunnerstick / Naughty Dog. [The Last of Us Part II: Accessibility Features Detailed](https://www.naughtydog.com/blog/the_last_of_us_part_ii_accessibility_features_detailed).** Naughty Dog. Date: 2020-06-09; later patch references present; last-update date unknown.

**Edition/context:** Original-release, controller-oriented documentation; puzzle row explicitly mentions patches 1.01 and 1.02; not a checked current PC/remaster build. **Access:** `relevant-excerpt`. **Type:** Official feature documentation.

**Inspected locator:** “Accessibility Presets,” “Alternate Controls,” and “Navigation and Traversal” / “Skip Puzzle Option”; web-text lines 13–39 and 94–106.

**Support in this artifact:** C-05; narrow distinction underlying C-07.

**Limits:** Documents offered controls and a stated puzzle-access limit. Feature existence or bypass does not establish equal access to puzzle reasoning or equivalent experience. **Independence:** Separate studio from other creator sources; promotional/support documentation, not an independent accessibility audit.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-003

**Alex Beachum (signed “Alex” in the article), Mobius Digital. [Demaking Outer Wilds](https://www.mobiusdigitalgames.com/news/demaking-outer-wilds).** Mobius Digital. Date: 2015-07-30.

**Edition/context:** Pre-release paper and Processing narrative prototypes, not the final game. **Access:** `relevant-excerpt`. **Type:** Firsthand development and formative-playtest account.

**Inspected locator:** “Archaeology In Space”; “It’s Only A Model”; “From Paper to Processing.” Web-text lines 21–37.

**Support in this artifact:** C-06 and a countercase underlying C-08.

**Limits:** Reported observations lack sample size, controls and effect estimates. Prototypes abstracted travel; no G03 game or prototype observation. Narrative concentration is a reported problem, not a universal pacing interval. **Independence:** Same studio/project and creative director as 004; one production context, not replication.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-006

**Jawad Jandali Refai, Scott Bateman and Michael W. Fleming. [External Assistance Techniques That Target Core Game Tasks for Balancing Game Difficulty](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2020.00017/full).** Frontiers in Computer Science 2:17. Date: 2020-06-04.

**Edition/context:** Version of record, DOI 10.3389/fcomp.2020.00017; HTML methods/results/discussion. **Access:** `relevant-excerpt`. **Type:** Original empirical research.

**Inspected locator:** “Apparatus and Setup,” “Participants,” “Procedure,” “Experimental Task,” “External Assistance Technique Performance,” “Subjective Measures,” “Summary of Study Results,” and “Explanation for Results of the Study.” Web-text lines 549–634.

**Support in this artifact:** C-07 only: task-dependent assistance and nonidentical performance/preferences; no adventure effect imported.

**Limits:** Sixteen mouse/keyboard-experienced adults; two custom visual-search tasks, not authored inventory puzzles. No raw-data reanalysis or figure-only values used. Summary/discussion differ in the context attached to an over-assistance exception; retain that ambiguity. **Independence:** Independent research group relative to the creator accounts; its literature review is not separate inspection of every cited source.

**Rights:** CC BY as stated in the article copyright notice; paraphrased with attribution; no figures or dataset redistributed.

## Inspected shared-candidate provenance

Source container: **GD-Knowledge-first-wave-reviewed-drafts-2026-10-10.zip**, Library `libfile_6852a9bc35108191bdcf23bd487e3b42`; actual bytes retrieved in G03 and SHA-256 matched to parent receipt: `e959c8d4eda2ba2a5f1994a37e0fa613d11f3fe0c5dd0608cf12a8fad87883ef`. Root is `GD-Knowledge-first-wave-reviewed-drafts-2026-10-10/`. The following are inspected **excerpts of selected drafts**, not re-verification of their entire public bibliographies. All remain version **0.1.0**, status **draft**, null approval metadata. They are not resent with G03.

**GDR-CAND-20261010-F01-TOP-03** — `selected-drafts/topics/learning-and-onboarding.md`; revision `original`; SHA-256 `85ab5352a60c2a7e101ee59f53e1afe4fa32834e0420a2619daa27015cdb7598`. Locator: “Guidance should track the learning demand”; “Discovery and explanation”; “Practice”; “Feedback”; “Re-entry,” inspected lines 65–103.

**GDR-CAND-20261010-F01-PAT-01** — `selected-drafts/patterns/supported-attempt-and-transfer-check.md`; revision `independent-review-correction-1`; SHA-256 `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1`. Locator: Purpose, prerequisites, mechanism, recipe and corrected transfer probes, inspected lines 49–118; correction.diff.md lines 18–43.

**GDR-CAND-20261010-P01-TOP-02** — `selected-drafts/topics/interface-and-information.md`; revision `review-correction-1`; SHA-256 `1381faf6c998295cd0b0472cf3905a28f87d9515d16bacb54ece423fe080595d`. Locator: “Working definitions” and “Task-information contract,” inspected lines 63–81.

**GDR-CAND-20261010-P01-TOP-03** — `selected-drafts/topics/accessibility-and-inclusive-interaction.md`; revision `review-correction-1`; SHA-256 `eab6276ce51dcea359cb599f24ffef603b6062a6d6f6badffa8c0e28a0e79d48`. Locator: Definition/access chain and proposed evaluation, inspected lines 54–87 and 193–221; corrections/P01/CORRECTION_RECEIPT.md lines 3–21.

**GDR-CAND-20261010-W01-TOP-01** — `selected-drafts/topics/narrative-structures.md`; revision `initial`; SHA-256 `9bac355072317ed9db0c299d926d293cd70052426ceb8db9cae98beaee1d15c7`. Locator: Decision, vocabulary, promise/action/persistence/interpretation and discovered order, inspected lines 57–100.

The parent-selected correction receipts govern which draft was inspected; they do not make its hypotheses accepted evidence. External dependency file paths are recorded as text because the files are not in this delivery. The [G03 packet](../reviews/full-run-20261010-g03-review-packet.md#dependency-register) holds unresolved links and proposed integration ownership.

## Review and history

Initial G03 capture, `candidate_revision: initial-capture-1`, version `0.1.0`, draft. Predecessor and supersession are null. The [review packet](../reviews/full-run-20261010-g03-review-packet.md) records the exact byte hash, author self-review, source gaps and proposed index row. No independent G03 reviewer, approval or release exists. The strongest opposing case is that decoupling removes the very task a player chose; this remains a live test condition, not a dismissed preference.

Next decision: independent Gate C review of the working boundary and coupling recommendations, followed by coordination of the missing progression, spatial, controls and camera links. Any subsequent implementation, participant study, host upload or publication requires its separate authority.

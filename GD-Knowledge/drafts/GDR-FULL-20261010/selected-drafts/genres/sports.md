---
id: GDR-CAND-20261010-G18-GEN-02
kind: genre
title: Sports
version: 0.1.0
status: draft
owner_project: BH-GDR-Genres
run_id: GDR-FULL-20261010
batch_id: G18
candidate_revision: initial-author-draft-1
attempt_identity: G18-current-dispatch-1
updated: '2026-10-11'
evidence_checked: '2026-10-11'
date_basis: UTC; run identifier retains dispatch date 2026-10-10
coverage_status: open
independent_review: not-performed
aliases:
- sports game
- sport simulation
- invented sport
tags:
- rules-and-roles
- control-authority
- team-coordination
- physical-abstraction
- match-and-season
- accessibility
related_topics:
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-F02-TOP-02
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-03
- GDR-CAND-20261010-F07-TOP-01
related_patterns:
- GDR-CAND-20261010-G18-PAT-01
- GDR-CAND-20261010-F01-PAT-01
- GDR-CAND-20261010-P02-PAT-02
- GDR-CAND-20261010-P02-PAT-01
- GDR-CAND-20261010-F02-PAT-02
related_genres:
- GDR-CAND-20261010-G18-GEN-01
source_ids:
- GDR-SRC-20261010-G18-007
- GDR-SRC-20261010-G18-008
- GDR-SRC-20261010-G18-009
- GDR-SRC-20261010-G18-010
- GDR-SRC-20261010-G18-011
- GDR-SRC-20261010-G18-012
- GDR-SRC-20261010-G18-013
- GDR-SRC-20261010-G18-014
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial G18 draft; no earlier G18 candidate bytes identified in this
  execution.
byte_identity: Exact SHA-256 is recorded in the accompanying integrity receipt; no
  self-hash is embedded.
---

# Sports

**Draft research candidate, not released knowledge.** This entry concerns physical, tactical and team abstractions in simulated and invented sports. It is not a complete survey of every sport or a recommendation to reproduce an official ruleset unchanged. No G18 gameplay observation, prototype, participant test or independent review was performed. See the exact [review packet](../reviews/full-run-20261010-g18-review-packet.md) and [integrity receipt](../reviews/full-run-20261010-g18-integrity-receipt.md).

## Definition and boundaries

For this library, a **sports game** organizes play around a recognizable or deliberately invented sport-like contest: a specified field of action, participant roles or capabilities, permitted interactions, and a method of scoring or determining an outcome. This is a proposed **working inference**, not a formal definition issued by a sport authority. “Sport-like” must be explained through the contest’s decisions rather than assumed from licensed uniforms or a familiar ball. Competitive scoring alone does not make every game a useful member of this research category. [S-C01]

The definition includes both representations of existing sports and invented sporting rules. Individual attempt sequences, direct racket-like opposition, continuous team play, set-play selection and season management create meaningfully different decisions. Identify the controlled role before selecting guidance: the **operator using an input device**, the **represented athlete**, the **currently controlled team member**, and the **manager selecting team policy** are not the same agent. A decision can be delegated at one layer and retained at another. [S-C01; S-C10]

The separate [racing entry](racing.md) handles route/trajectory, speed-control, vehicle response and traversal-result comparison. A motorsport game can legitimately need both files; the overlap does not justify collapsing them. A sport-management hybrid may emphasize roster and scheduling decisions rather than momentary execution; use the missing management/progression references only after their selected bytes are available. A fighting or vehicle-elimination mode can share assets with a sport but change the organizing objective. Mode-specific analysis is more useful than treating a franchise label as a mechanism. [S-C01; S-C07]

## Custom research instructions

Begin with **who chooses what, under which rule and with what information**. Specify whether the designer wants to preserve a physical action, a tactical relation, a team role, a spectator interpretation or a season-level tradeoff. Do not treat embodied resemblance, photographic presentation, famous athletes or licensing as evidence of enjoyment, skill development or accessibility. These are different claims requiring different evidence. [S-C02; S-C08]

For existing sports, inspect the exact sport, issuing organization, edition, competition adaptations and enforcement policy. Then identify which rules the game implements, abstracts, omits or substitutes. An official sporting rule constrains a faithful adaptation only within its declared scope; it is not a native-interface standard or a universal design requirement. For invented sports, the authored rule specification replaces the external rulebook, but still needs explicit scoring, roles, legal interactions, restarts and conflict resolution. [S-C03; S-C09]

Sample contrasting tasks: an individual timed or scored attempt; direct opposition; off-ball team coordination; a set play; whole-match management; and longer-season goals. Examine direct control, context-sensitive assistance, switching, AI delegation and alternative inputs. This batch’s directly documented examples are narrower than that research range. It does not establish general recommendations for every sport, licensed competition, professional athlete population, motion device or team size. [S-C09; S-C15]

Challenge misleading comparisons: more accurate real-world movement versus better game performance; novice motion users versus familiar gamepad users; a single player’s score versus a coupled team outcome; a new rule edition versus a supposedly failed transfer test; and a presentation preset called “Authentic” versus measured authenticity. Ask whether an assist changes execution, target selection, information or teammate policy before calling it easier, fairer or more realistic. [S-C02; S-C04; S-C08; S-C10]

Future empirical extensions should obtain complete methods and results for the controller leads in the packet, plus original studies of role coordination and long-horizon sports play. Search for null findings, changed conclusions under alternate models, unsuccessful adaptations and access exclusions. Do not infer long-term sport skill transfer from a short digital-play session, or estimate a universal reaction window from one title’s timing mechanic. [S-C02; S-C15]

## Player promises and varied audiences

Candidate promises include **executing a satisfying action**, **reading an opponent**, **coordinating a team**, **expressing tactical knowledge**, **inhabiting a sporting fantasy**, or **managing a season**. These are proposed elicitation categories, not a population survey. Some players may value recognition of familiar sporting relations while preferring simplified physical operation; others may want the motor challenge itself. The same input preset need not satisfy both. [S-C08]

For audience research, ask about the desired responsibility. “I want to decide where to pass” differs from “I want to perform the pass gesture” and “I want to coach an attacking pattern.” Someone who cannot use a repeated motion might still want the full tactical problem. Conversely, replacing a desired motor task with automated targeting can remove the experience they sought even while raising their score. These are testable design interpretations, not known preferences of an entire disability, age or fan group. [S-C08; S-C10]

### Narrow empirical check on embodied authenticity

Skalski and colleagues’ golf experiment used **48 communication students aged 19–24**, ten-minute sessions, and *Tiger Woods PGA Tour 07*: standing Wii motion play versus seated PS2 gamepad play. Naturalness differed, but the presence–enjoyment regression did not support the proposed link. Platform and posture co-varied. The companion racing experiment’s model-dependent result is described in the [racing evidence section](racing.md#what-the-empirical-material-actually-permits). Neither establishes universal benefits of embodied controls. [S-C02; GDR-SRC-20261010-G18-014, pp. 230–238]

The evidence-to-application bridge is to **separate the claims**, not to reject motion controls. An input can be recognizable, demanding, expressive, accessible to one person, inaccessible to another, or strategically satisfying in different combinations. Prototype the particular promise and compare it against a viable alternative, with appropriate familiarization. A licensed presentation or a natural gesture does not settle that comparison. [S-C08]

## Characteristic loops and structures

### Action and interpretation

At the action scale, define **available information → intended action → command/commitment → simulated resolution → feedback and next authority**. The last step matters in sports because the same person may immediately control a different team member, observe an AI teammate, or wait for an opponent’s response. Failure to distinguish those states can make a wrong-player action look like poor timing. This is a proposed diagnostic model, not a measured universal handoff effect. [S-C10]

Decide which variables the player owns: target, direction, force, timing, body/implement orientation, movement path, or a higher-level tactical instruction. A simplified control scheme can retain target selection while automating force, or do the reverse. A “manual” label alone does not explain the remaining choices. Record the retained action in the design specification and show the necessary state before commitment. [S-C10]

### Possession, rally, point or attempt

These units set different recovery and learning opportunities. A turn-structured attempt can permit deliberation before execution; a live possession can require simultaneous attention to space, teammate intent and opponent action; a rally may shift authority repeatedly before the score changes. This is an analysis of the declared structures, not a prescription that every sport use the same pace. It suggests testing where information and action demands coincide rather than transplanting a generic timing window. [S-C09]

A replay can explain one consequential event, but it must not conceal that the next live situation has different positions, possession or authority. A practice reset should restore the factors necessary for the intended comparison, or label the exercise as varied practice. Repeating a visible animation is not enough to establish that the tactical decision was understood. [S-C11; S-C14]

### Match and team goals

Individual statistics and team success can diverge. In a hypothetical passing game, an operator may sacrifice an immediate scoring opportunity to create an easier team chance. A personal metric that rewards only shots could misclassify that decision under a cooperative tactical goal. Specify the goal and unit before deciding what counts as improved play. This is a logical measurement issue, not evidence that one reward model improves teamwork. [S-C11]

Team coordination also depends on what the game allows participants to communicate. Alternatives to mandatory voice might expose a small intent signal, a nominated receiver, a planned run or a confirmation before a set play. Each can change uncertainty or add communication work. Test whether it preserves the intended information budget instead of assuming that more shared information always produces better play. [S-C11; S-C15]

### Season and career

Season structures can connect roster selection, development, rest, equipment, schedule, competition qualification and narrative interpretation. These are **candidate design dimensions**, not validated retention requirements. A local design may choose only a few. Match scores alone cannot explain whether a player enjoyed long-term planning or could re-enter a season after an absence. [S-C12]

Keep changing team capability separate from claims about improved execution. A stronger roster, altered difficulty preset or new rules can change outcomes without demonstrating that the operator learned the intended skill. A fixed-roster practice mode, clearly contextualized season history, or a tactical review under stable conditions are alternatives. Do not require a season system when a self-contained match already fulfills the player promise. [S-C12; S-C14]

No medical or real-world training recommendation follows from proposed fatigue, injury or athlete-development abstractions. Their ethical framing, realism, balance and production cost need separate evidence and review. No existing season-model study or complete reviewed progression/economy dependency was inspected for this batch. [S-C12; S-C15]

## Rules, versions and abstractions

### Exact rule evidence versus current-edition gaps

IFAB’s **2025/26** change text specifies a corner-kick sanction when a goalkeeper controls the ball by hand/arm beyond eight seconds, with a visible final-five-second count; its Law 11.2 change also addresses offside judgement at a goalkeeper’s throw. Those are edition-scoped football provisions, not universal game timing rules. [S-C03; GDR-SRC-20261010-G18-009, Laws 12.3 and 11.2]

An inspected IFAB announcement says **2026/27** changes take effect from **1 July 2026**, subject to its competition-adoption qualification. The complete 2026/27 PDF could not be retrieved in this execution. Accordingly, the 2025/26 example is deliberately historical; this file does **not** certify all current football rules or infer the latest law from an older familiar version. [S-C03; GDR-SRC-20261010-G18-010, final effective-date paragraph; inaccessible lead 016 in packet]

For a sport adaptation, write a rule-translation record: the source clause/edition; the intended game relation; any simplification; how the player learns it; how it is officiated; and what changes on restart or update. A fictional or simplified rule may be appropriate, but should not be described as an exact official simulation without checking that claim. No implementation or licensing approval is supplied here. [S-C09]

### What a settings page can and cannot establish

EA’s FC 26 accessibility page distinguishes one/two-button schemes, assistance and switching/receiver-lock choices; it states restrictions on simplified schemes in competitive online play. Its scope is **US-English PC and console versions**, not every language, platform or patch. These are inspected settings descriptions, not proof that the restriction is necessary for fair competition. [S-C04; GDR-SRC-20261010-G18-007, scope, Controller Customization, Passing and Switching]

The separate FC 26 feature page positions **Competitive** and **Authentic** presets toward different contexts. Those are publisher intentions, not measured enjoyment, realism or access effects. Treat a named preset as a configuration to inspect, not a scientific classification of users. [S-C05; GDR-SRC-20261010-G18-008, Two Distinct Gameplay Presets]

### Practical choices

| Design decision | Conditional application and mechanism hypothesis | Alternative, cost or failure condition |
|---|---|---|
| Preserve a physical action or a tactical relation? | Name the relation first. Retain the action where operation is the promise; abstract it where tactical choice is the promise. [S-C08/S-C10] | Motion resemblance may add physical or setup demands. Automated execution may remove valued expression. Test both instead of assuming one authentic experience. |
| Direct control or delegated team behavior? | State which agent owns target, movement and timing, and when authority changes. [S-C10] | A visible switch cue can still be late or overloaded. A fixed-role scheme or explicit switch can be simpler, but limits whole-team control. |
| Official or adapted rules? | Pin the edition, list adaptations and make consequential enforcement understandable. [S-C03/S-C09] | Full fidelity can require explanation and officiating complexity. Simplification can violate an explicitly promised sporting relation. Neither option is automatically superior. |
| Shared information or deliberate uncertainty? | Expose enough to coordinate the intended action without silently resolving every opponent-reading problem. [S-C11] | Always-on tactical overlays can dominate attention or reveal too much. Selectable cues and set-play planning are alternatives. |
| Isolated practice or full-match repetition? | Reset the variables needed for a specific decision, then test it in the appropriate coupled context. [S-C11/S-C16] | A rehearsed set piece can fail to transfer; a full match can provide too few relevant repetitions. Record both limitations. |
| Season progression or self-contained contests? | Add long-horizon decisions only where they serve the chosen promise. [S-C12] | Roster growth obscures execution comparisons and creates content/re-entry costs. A stable exhibition mode is a legitimate alternative. |
| Shared ranking or contextual histories? | Use minimal relevant context for the exact claim, not a general moral ranking of control schemes. [S-C14] | Over-segregation fragments play and stigmatizes access; under-description supports misleading comparisons. Test error in both directions. |

## Applying shared topics

Only the following selected **reviewed-but-unreleased** dependency bytes were transferred. The links open their provenance registry within this packet; no shared candidates are duplicated or resubmitted as G18 outputs.

| Dependency | Sports-specific interpretation |
|---|---|
| [Learning and onboarding — D01](../reviews/full-run-20261010-g18-review-packet.md#d01) | Separate knowing a legal/tactical relation from physically performing it. A changed law or assistance rule is a changed task, not automatic evidence of failed transfer. |
| [Accessibility and inclusive interaction — D02](../reviews/full-run-20261010-g18-review-packet.md#d02) | Include roster/menu selection, control configuration, match play, substitution, recovery and re-entry. Do not export native timing or target thresholds from scoped web criteria. |
| [Challenge and difficulty — D03](../reviews/full-run-20261010-g18-review-packet.md#d03) | Distinguish motor execution, opponent prediction, team coordination, AI delegation, rules knowledge and consequence severity. |
| [Controls and input — D04](../reviews/full-run-20261010-g18-review-packet.md#d04) | Test who receives input after a switch and when a pass/shot choice commits, not just whether buttons are remappable. |
| [Multimodal communication — D05](../reviews/full-run-20261010-g18-review-packet.md#d05) | Preserve possession, controlled role, direction, urgency and uncertainty across selected information routes. Do not equate redundant presentation with equal usability. |
| [Evaluation and balancing — D06](../reviews/full-run-20261010-g18-review-packet.md#d06) | Treat teammate/opponent influence as part of the analysis. A player, possession, match and team are different units, not interchangeable independent samples. |

Selected reviewed bodies for movement, simulation, multiplayer/social systems, session structure, progression/economies, camera/framing, localization and platform context were not obtained here. Third-wave author-packet pointers are not substituted for selected reviewed files; no P04 origin is mixed into this synthesis. Full dependency limits and exact IDs are recorded in the packet. [S-C15]

## Pattern selection and adaptations

[Supported Attempt and Transfer Check — D07](../reviews/full-run-20261010-g18-review-packet.md#d07) fits a specific sporting relation when examples discriminate competing predictions. In a passing exercise, “always choose the nearest teammate” must sometimes disagree with “choose the teammate with an open receiving route.” Changing an official offside rule between probes would require a new-rule condition instead. Keep access supports and ask separately what is likely to happen and what the player prefers to do. [S-C16]

[Fact-Preserving Cue Alternatives — D08](../reviews/full-run-20261010-g18-review-packet.md#d08) can apply to controlled-player identity, possession or a meaningful rule warning. Avoid interpreting “add audio” as a recipe to speak every moving player’s state. The relevant uncertainty and deadline need preservation; its unresolved overlap with a P01 pattern remains visible. [S-C15]

[Recoverable Action Remapping — D09](../reviews/full-run-20261010-g18-review-packet.md#d09) applies to action, switching and recovery together. A binding that works in a training menu can still fail when the same hand must sustain movement and select a receiver. [Bounded Disclosed Difficulty Adaptation — D10](../reviews/full-run-20261010-g18-review-packet.md#d10) is a possible training or tailored opposition approach, not permission to silently alter a declared competitive contest. [S-C15]

The new [Versioned Performance Comparison](../patterns/versioned-performance-comparison.md) pattern applies when communicating match, practice or season comparisons. It is not a rule requiring identical settings for everyone. It can retain unlike attempts in a clearly contextualized personal history, or document a particular competition’s agreed conditions. No claim of equal skill should exceed what those conditions and metrics establish. [S-C14]

## Representative cases and counterexamples

**A real-sport representation can intentionally alter structure.** Nintendo’s 2022 *Switch Sports* launch account describes multiple soccer forms, simultaneous/variant bowling and different racket interactions. This documents a selected historical range of sport abstractions; it does not prove that any abstraction is universally intuitive or accessible. Later content is not silently included. [S-C06; GDR-SRC-20261010-G18-011, sport-specific paragraphs]

**An invented sport can still need repeatable team practice.** Rocket League’s Season 17 announcement describes Online Free Play with selectable modes and boost/goal-reset settings. That establishes configurable practice as a documented feature, not that it improves coordinated play or transfers to matches. A specific mechanism requires a specific test. [S-C07; GDR-SRC-20261010-G18-012, Online Free Play]

**A related vehicle mode need not preserve the sporting relation.** Rocket League’s 2022 Knockout description uses elimination, hazards and attack/block/grab interactions rather than the same team-ball objective. For this library, that is a boundary counterexample to classifying every mode from vehicles or franchise alone. Whether one labels it an invented sport remains contestable; the decision structure, not the label, determines which guidance applies. [S-C01; S-C07; GDR-SRC-20261010-G18-013, What is Knockout? / New Mechanics]

**Presentation is not the causal explanation.** The natural-controller study and EA’s differently positioned presets provide contrasting kinds of evidence: measured short-session constructs versus producer intentions. Combining them does not create a study of authenticity or a proof that licensed realism produces enjoyment. [S-C02; S-C05; S-C08]

These examples are intentionally heterogeneous but not comprehensive. English documentation, prominent publishers and readily inspectable digital titles are overrepresented. No actual G18 build capture substantiates animation timings, exact switch behavior, every rules clause or current online availability. Sport-specific traditions outside the inspected material remain open coverage.

### Worked example: a passing decision with explicit authority — illustrative, not performed

Consider an invented team sport in a small arena. The design promise is reading a receiving route, not reproducing a real throwing motion. The operator directs the carrier, chooses a receiver and commits the pass. The simulation resolves the trajectory; control then moves to the nominated receiver. This is a hypothetical authority policy, not a description of FC or Rocket League. [S-C10; S-C16]

Write the key states in plain language: **carrier controlled**, **receiver nominated**, **pass committed**, **receiver controlled**. At each state, specify whether changing direction changes the carrier’s movement, the receiver nomination or the pass trajectory. Present the currently relevant state through the selected access route before it can change the meaning of an input. The proposal is not “add more icons”; a stable role policy or fewer automatic switches may avoid the problem more cheaply. [S-C10; S-C16]

Create three same-rule practice arrangements. In the first, the nearest teammate has an open route. In the second, that teammate is covered while a farther teammate is open. In the third, both are open but one route conflicts with a separately declared positional goal. Ask for the predicted receiving outcome and the preferred action. These cases test different things: recognizing coverage, choosing a risk, and following a goal. Do not combine them into one unexplained correct-choice score. Preserve the same controls and accessible information throughout. [S-C16; D07]

Compare the explicit handoff policy with a fixed-role alternative and the current baseline, rather than assuming automatic switching is necessary. Log a wrong-recipient input separately from a poor pass prediction. If participants understand the receiving route but repeatedly act on the previous role, investigate the handoff policy and cue timing. If the cue is accessible but the AI chooses an unintended receiver, changing its color is not a solution. These are falsifiable diagnostic hypotheses, not observed findings. [S-C10; S-C16]

### Worked example: a season result is not a pure execution score — illustrative, not performed

A fictional season mode permits roster development and tactical delegation. A later match yields more goals than an earlier match. The history should record the change relevant to the claim: a different roster, opponent context or assistance policy may matter. It can celebrate a season outcome without claiming the operator’s timing improved. A stable-roster practice task could investigate that separate question. [S-C12; S-C14]

For an explicit equal-condition competition, the team might agree on a versioned rules profile. For a casual mixed-ability event, it might agree on disclosed handicaps instead. Neither arrangement justifies excluding all alternative inputs or claiming equivalent access merely because each person can select the same menu option. The profile should describe gameplay conditions, not reveal personal diagnoses. [S-C14; S-C15]

If a rule edition changes the restart sanction, label old results by their edition and explain the new relation before testing it. Do not erase historical results or present adaptation to the new law as proof that old training failed. The versioned-comparison pattern is intended to support that limited interpretive distinction; whether it makes the history clearer is untested. [S-C03; S-C14]

## Accessibility, localization, ethics and production

**Embodiment and inputs.** A motion-control design needs evaluation with the actual intended actions, playing positions, reach demands, available space and recovery route. Do not use resemblance to a sporting gesture as evidence that everyone can perform it. Test alternatives where the aim is tactical participation rather than that gesture. A manufacturer’s motion-play caution, such as the one in Nintendo’s launch article, is not a complete safety or access assessment. No clinical benefit or rehabilitation claim is made here. [S-C06; S-C08; S-C15]

**Roles and information.** People need to know which player or role will respond, whether the ball/turn is theirs, and when an action has committed. Non-color alternatives, configurable information routes and a stable reference frame are candidate approaches; successful cue delivery is not proof that the fact was usable while coordinating play. Evaluate whole tasks, including substitution, menus and return after interruption, rather than demonstrating one successful shot. [S-C10; S-C15; D02, D05]

**Language and cultural context.** Rules vocabulary, abbreviations, commentary, local scoring conventions and unfamiliar sport concepts need separate explanation. EA’s documented language limitations illustrate why the presence of a narration feature cannot establish access in every locale. Test the specific language, interface scope and timing of critical information. Names and licensed presentation introduce production and rights questions; this packet does not determine licenses or legal obligations. [S-C04; S-C15]

**Cooperation and competition.** Requiring voice communication, rewarding only individual output or making assistance selection publicly stigmatizing are risks to investigate, not universal measured harms asserted here. A competition restriction documented for one product does not establish the necessity of the same restriction elsewhere. Compare alternatives such as preserved-role rules, gameplay-equivalent assistance, disclosed formats or contextual results before separating populations. [S-C04; S-C11; S-C14]

**Season ethics.** Monetized capability, opaque selection systems, compulsory grind and punitive re-entry can conflict with a proposed promise of fair sporting contest or relaxed participation. Those conflicts should be stated and tested, not hidden under retention. Avoid unsupported stereotypes about bodies, nationalities, gender, disability or fan expertise when assigning capabilities or interfaces. This is a proposed review obligation, not a claim of approved studio policy or measured causal effect. [S-C12; S-C15]

**Production.** Role switching, animation commitment, assistance, AI delegation, officiating, camera, net state and localization can interact. A small prototype should expose the policy boundaries clearly before a large content set makes defects hard to diagnose. Record which layer selected the action and which layer displayed it. No engine synchronization, network model, animation latency or sporting-AI implementation has been verified here. The missing domain dependencies must be reviewed before implementation guidance is claimed. [S-C10; S-C15]

## Research questions and proposed validation

**All procedures are proposed, not performed.** Decide the local population, analysis unit and practically meaningful result before data collection. Do not claim statistical power or equivalence from an arbitrary sample count. Ensure familiarization is appropriate for each input condition; preserve access rather than forcing everyone onto an inaccessible baseline. [S-C17; D06]

| Discriminating question | Comparison, task and measures | Confounds and decision rule |
|---|---|---|
| Does the retained abstraction support the intended experience? | Compare a motion-oriented and a viable non-motion route for the same intended decision. Measure successful access, decision outcome, perceived naturalness, agency and enjoyment separately. | Prior familiarity, posture, platform and task differences may explain results. Reject a universal naturalness-benefit claim when outcomes diverge; retain a route that serves a specified audience/goal. |
| Does an explicit control handoff reduce wrong-role action? | Compare explicit switching, fixed-role play and the baseline across the illustrative pass cases. Ask who will act before commitment; record wrong-role commands separately from tactical mistakes. | Do not count an AI target substitution as a perception failure. Adapt or reject a cue-only solution when policy ambiguity persists or cue load becomes worse. |
| Does practice discriminate understanding? | Use same-rule arrangements that produce opposing predictions for competing heuristics; obtain prediction and preference separately. | Changed laws or altered assistance are a new-task condition. Reject a learning claim if copying one response succeeds in every probe. |
| Does local practice transfer to coupled play? | Investigate a stated maneuver in practice and in a controlled team/opponent context, then examine retention if that is the actual question. | Teammates influence outcomes; possessions are not independent people. Do not infer team benefit solely from individual drill scores. |
| Are contextual comparisons clearer without needless exclusion? | Test matched, altered-rule, altered-roster and irrelevant-setting changes using PAT-01. Measure inference errors, confidence, stigma and access to participation. | Reject or simplify when the profile adds burden without clarifying the intended claim, or separates people for irrelevant settings. |
| Can a player return to the intended role after interruption? | Test setup, match pause/re-entry, substitution and season return using the selected access routes and locale. | A remembered control layout is not proof the current controlled role or new rule is understood. Repair access failures before interpreting motivation or skill. |

A likely opposing result is that a fixed-role, modest-rules, self-contained contest needs less explanation and produces fewer errors than an elaborate authentic simulation with many assistance and comparison modes. Such a result would narrow the proposed pattern and authority framework, not be dismissed as players failing to appreciate realism. [S-C17]

## Coverage and remaining gaps

Physical/tactical abstraction, rules and roles, control authority, information, coordination and match/season goals received **bounded synthesis**. Individual and invented sports are represented, but not comprehensively. Full current football laws, real-world athletic transfer, long-term natural-control learning, injury/fatigue abstractions, detailed officiating, non-English access, specialist sports equipment, team-coordination effects and seasonal retention remain unresolved.

The complete 2026/27 IFAB PDF and additional original controller articles were not obtained. No build, current patch or platform-specific interaction was played. Missing reviewed dependencies for simulation, multiplayer, camera, localization and progression constrain cross-domain integration. The next useful extension should investigate one concrete retained decision and authority policy, not assume that greater fidelity or a licensed presentation improves every outcome.

## Claim ledger

| Claim | Precise claim and class | Support / locator | Confidence, applicability and unresolved question |
|---|---|---|---|
| S-C01 | Sport-specific rules/roles and objectives offer a useful working boundary, including contested invented sports. **inference** | G18 framing; documentary contrast S-C06/S-C07. | Moderate conceptual usefulness; taxonomy acceptance pending. Franchise, platform and tone do not decide membership alone. |
| S-C02 | Original short-session natural-controller evidence does not establish universal enjoyment or access benefits. **empirical-evidence** | GDR-SRC-20261010-G18-014, Study One pp. 230–234 and Study Two pp. 234–238. | Moderate for the reported study results; platform/posture and analysis dependence limit transfer. See G18-CON-02. |
| S-C03 | The cited football provisions are edition-scoped, and a later edition exists. **formal-standard** for the specific 2025/26 clauses; **observed-example** for the later announcement | GDR-SRC-20261010-G18-009, Laws 12.3/11.2; GDR-SRC-20261010-G18-010, effective-date paragraph. | High for cited text; incomplete current-law coverage because full source 016 was not inspected. Not a game UI or universal timing requirement. |
| S-C04 | FC 26 documents different control/assistance options and scoped access restrictions. **observed-example** | GDR-SRC-20261010-G18-007, scope and specified settings sections. | High for documentation, not actual build or universal competitive necessity. Language/platform boundaries retained. |
| S-C05 | Authentic and Competitive are producer-positioned presets, not validated experience outcomes. **practitioner-heuristic** | GDR-SRC-20261010-G18-008, Two Distinct Gameplay Presets. | High for the stated positioning; low for any benefit attribution. Same source family as 007. |
| S-C06 | Switch Sports launch documentation illustrates varied abstractions of existing sports. **observed-example** | GDR-SRC-20261010-G18-011, sport-specific paragraphs and motion caution. | High within historical description; no current-roster or universal access inference. |
| S-C07 | Official Rocket League documents illustrate configurable practice and a distinct elimination-mode boundary. **observed-example** | GDR-SRC-20261010-G18-012, Online Free Play; -013, What is Knockout? / New Mechanics. | High for described historical features; transfer, benefit and current availability unknown. |
| S-C08 | Separate physical resemblance, tactical authenticity, presentation, operation and enjoyment. **inference** | S-C02/S-C05 plus D03/D06. | Moderate conceptual distinction, not a validated preference taxonomy or effect estimate. |
| S-C09 | Explicit rule translation and action/attempt/match structure help identify the actual decision being tested. **hypothesis** | S-C03/S-C06, G18 model and D01/D06. | Low for effectiveness; intended relation and enforcement must be tested locally. |
| S-C10 | Record control authority and commitment before treating an input failure as a tactical or timing deficit. **hypothesis** | S-C04 as a documentary mechanism lead; D04/D05; illustrative authority design. | Moderate diagnostic plausibility, low causal support for any handoff UI. |
| S-C11 | Team-related outcomes require goals and analysis units that reflect coupled actions. **inference** | D06; explicit task logic; S-C07 documents an available practice form only. | High logical limitation; no team-coordination effect demonstrated here. |
| S-C12 | Separate season/roster change from operator-skill inference and from retention claims. **inference** | G18 comparison logic, D06; missing progression/economy dependencies disclosed. | Moderate logical scope, low evidence for particular season designs. |
| S-C14 | Minimal relevant comparison context may improve interpretation without requiring blanket input segregation. **hypothesis** | S-C03/S-C04 and D06; new PAT-01. | Low for user benefit; false exclusion is an explicit falsifier. See G18-CON-03/04. |
| S-C15 | Shared access, controls, cue and evaluation guidance requires sports-specific task checks and preserved scope. **inference** | D01–D10; S-C04/S-C06 narrow examples. | Moderate conditional interpretation; no accessibility certification, universal numbers or implementation approval. |
| S-C16 | Discriminating same-rule pass cases could distinguish prediction from rote action without withdrawing access. **hypothesis** | Corrected D07; worked example. | Low until prototype rule validation and participant testing; no performed tests. |
| S-C17 | The proposed comparisons could falsify the strongest recommendations under a specified local decision contract. **hypothesis** | D06 and test design above. | No result, power or effect size established; independent review pending. |

## Review and history

Version `0.1.0`; candidate revision `initial-author-draft-1`; predecessor and supersession null. Inspection date is 2026-10-11 UTC; the run identifier retains 2026-10-10. Exact file bytes are identified in the integrity receipt.

Author self-review is not independent review. Gate C remains pending independent evidence/content review; Gate D has only the checks actually recorded in the packet, not Project-host retrieval; Gate E/release remains unapproved. Next decision: review the working sport boundary, rules-edition handling, authority diagnostic and comparison pattern before adopting guidance or assigning registered child work.

## References

All access dates are **2026-10-11 UTC**. Source IDs are temporary run-scoped identities. Cross-batch canonical URL/DOI/edition deduplication is pending. Public material is paraphrased; no source article, image or screenshot is redistributed. Unless an explicit license is established, rights are treated as reserved; public access is not a redistribution license. “Documentary observed example” means the named official artifact was inspected by the G18 author, not that a game was played.

### GDR-SRC-20261010-G18-007

Electronic Arts. *EA SPORTS FC 26 Accessibility Resources*. EA accessibility resources. Publication/update: unknown. [Inspected route or disclosed lead](https://www.ea.com/able/resources/ea-sports-fc/fc-26).

Edition/build: FC 26, US-English PC and console scope stated by page; exact patch unknown. Access: `relevant-excerpt`. Type: Official settings documentation; documentary observed example. Locator: Scope introduction; Controller Customization; Gameplay Settings; Passing; Switching; narration/language sections. Claims in this artifact: S-C04. Limits/provenance: Not an exhaustive platform, language or live-build audit. Competitive-mode restrictions are product-specific, not a universal fairness rule. Same publisher and title family as 008.

### GDR-SRC-20261010-G18-008

Electronic Arts. *EA SPORTS FC 26 Gameplay*. EA official feature page. Publication/update: unknown. [Inspected route or disclosed lead](https://www.ea.com/games/ea-sports-fc/fc-26/features/fc-26-gameplay).

Edition/build: FC 26 unnumbered feature page; exact patch unknown. Access: `relevant-excerpt`. Type: Firsthand product positioning and design-intent account. Locator: Two Distinct Gameplay Presets. Claims in this artifact: S-C05. Limits/provenance: Authentic and Competitive are publisher framing, not measured authenticity, enjoyment or fairness. Not independent corroboration of 007.

### GDR-SRC-20261010-G18-009

The International Football Association Board (IFAB). *Laws of the Game 2025/26: Law changes*. IFAB. Publication/update: 2025/26 edition; webpage publication day unknown. [Inspected route or disclosed lead](https://www.theifab.com/law-changes/2025-26/).

Edition/build: Association football Laws 2025/26 change text. Access: `relevant-excerpt`. Type: Formal sport-rule authority; edition-scoped normative text. Locator: Law 12.3, goalkeeper control beyond eight seconds and corner-kick sanction; Law 11.2, offside judgement for a goalkeeper throw. Claims in this artifact: S-C03. Limits/provenance: Applicable to the identified football-law edition and relevant competition adoption, not a native-game accessibility or timing standard. The later 2026/27 complete edition was not retrieved; 010 confirms that an edition transition occurred.

### GDR-SRC-20261010-G18-010

IFAB. *The IFAB introduces further measures to improve match flow and player behaviour*. IFAB. Publication/update: 2026-02-28. [Inspected route or disclosed lead](https://www.theifab.com/news/the-ifab-introduces-further-measures-to-improve-match-flow-and-player-behaviour/).

Edition/build: Official announcement of 2026/27 changes. Access: `relevant-excerpt`. Type: Official announcement; documentary observed example, not the complete normative edition. Locator: Final paragraph: new edition effective 1 July 2026 and competition adoption timing. Claims in this artifact: S-C03. Limits/provenance: Supports freshness caution and edition transition only. It does not substitute for all clauses in inaccessible source 016. Organizationally related to 009 and 016.

### GDR-SRC-20261010-G18-011

Nintendo. *Serve up some friendly competition in Nintendo Switch Sports, available now!*. Nintendo US. Publication/update: 2022-04-29. [Inspected route or disclosed lead](https://www.nintendo.com/us/whatsnew/serve-up-some-friendly-competition-in-nintendo-switch-sports-available-now/).

Edition/build: Nintendo Switch launch-era description; later sport roster and patches not audited. Access: `relevant-excerpt`. Type: Official launch description; documentary observed example. Locator: Soccer; Bowling; Tennis; Badminton; motion-play caution. Claims in this artifact: S-C06. Limits/provenance: Describes a historical selection of sport abstractions, not the current full roster or measured accessibility. A manufacturer caution is not a participant safety study. Organizationally related to 006.

### GDR-SRC-20261010-G18-012

Psyonix / Epic Games. *Season 17 Brings Online Free Play as Rocket League Heads to the Arcades*. Rocket League official news. Publication/update: 2024-11-26. [Inspected route or disclosed lead](https://www.rocketleague.com/news/season-17-brings-online-free-play-as-rocket-league-heads-to-the-arcades).

Edition/build: Season 17 announcement; subsequent patch and availability unknown. Access: `relevant-excerpt`. Type: Official feature announcement; documentary observed example. Locator: Online Free Play paragraphs and game-mode/boost/goal-reset options. Claims in this artifact: S-C07. Limits/provenance: Practice configuration is documented; improved coordination or transfer is not experimentally established. Same developer/publisher family as 013.

### GDR-SRC-20261010-G18-013

Psyonix / Epic Games. *Smash Into Spring With Knockout Bash!*. Rocket League official news. Publication/update: 2022-04-21. [Inspected route or disclosed lead](https://www.rocketleague.com/news/smash-into-spring-with-knockout-bash//).

Edition/build: 2022 limited-time Knockout announcement; present availability unknown. Access: `relevant-excerpt`. Type: Official mode description; documentary observed example. Locator: What is Knockout?; New Mechanics; New Abilities. Claims in this artifact: S-C07. Limits/provenance: Mode description supplies a boundary counterexample; no effectiveness or popularity inference. Same production family as 012. Historical event is not represented as currently playable.

### GDR-SRC-20261010-G18-014

Paul Skalski, Ron Tamborini, Ashleigh Shelton, Michael Buncher and Pete Lindmark. *Mapping the road to fun: Natural video game controllers, presence, and game enjoyment*. New Media & Society 13(2), 224–242, SAGE. Publication/update: 2011 issue; OnlineFirst 2010-10-12. [Inspected route or disclosed lead](https://www.researchgate.net/publication/258173311_Mapping_the_road_to_fun_Natural_video_game_controllers_presence_and_game_enjoyment). DOI: `10.1177/1461444810370949`.

Edition/build: Original article text; coauthor Ashleigh Shelton upload dated 2015-08-29. Access: `relevant-excerpt`. Type: Original empirical article; coauthor-uploaded full-text route. Locator: Study One methods/results, pp. 230–234; Study Two methods/results, pp. 234–238. Claims in this artifact: S-C02. Limits/provenance: Original article body inspected, not later ResearchGate recommendations or citing-paper excerpts. Short student sessions; control/platform/posture differences and model-dependent enjoyment results constrain transfer. Publisher/CiteSeerX PDF routes did not yield inspected PDF bytes. Independent of the game-publisher announcements here.

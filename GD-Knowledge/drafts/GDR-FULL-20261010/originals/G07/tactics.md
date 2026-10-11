---
id: GDR-CAND-20261010-G07-GEN-02
kind: genre
title: "Tactics"
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
attempt_identity: G07-local-attempt-01
predecessor_sha256: null
supersedes: null
change_summary: "Initial bounded G07 draft; inspected selected reviewed dependencies; no predecessor or other batch replaced."
owner_project: BH-GDR-Genres
run_id: GDR-FULL-20261010
batch_key: G07
updated: "2026-10-10"
evidence_checked: "2026-10-10"
coverage_state: open
aliases: ["local tactical coordination", "squad tactics", "tactical planning"]
tags: ["genre", "local-maneuver", "action-budget", "information-entitlement", "non-elimination-objectives", "coverage-open"]
related_topics: ["GDR-CAND-20261010-F02-TOP-01", "GDR-CAND-20261010-F02-TOP-02", "GDR-CAND-20261010-W02-TOP-02", "GDR-CAND-20261010-P02-TOP-01", "GDR-CAND-20261010-P02-TOP-02", "GDR-CAND-20261010-P02-TOP-03", "GDR-CAND-20261010-F07-TOP-01", "GDR-CAND-20261010-F07-TOP-02", "GDR-CAND-20261010-P01-TOP-03"]
related_patterns: ["GDR-CAND-20261010-F01-PAT-01", "GDR-CAND-20261010-F02-PAT-01", "GDR-CAND-20261010-W02-PAT-02", "GDR-CAND-20261010-F07-PAT-02", "GDR-CAND-20261010-G07-PAT-01"]
related_genres: ["GDR-CAND-20261010-G07-GEN-01"]
source_ids: ["GDR-SRC-20261010-G07-003", "GDR-SRC-20261010-G07-007", "GDR-SRC-20261010-G07-008", "GDR-SRC-20261010-G07-009", "GDR-SRC-20261010-G07-010", "GDR-SRC-20261010-G07-011", "GDR-SRC-20261010-G07-012", "GDR-SRC-20261010-G07-013"]
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed
byte_hash_record: "../reviews/full-run-20261010-g07-integrity-receipt.md"
---

# Tactics

**Research candidate, not released guidance.** This entry addresses local coordination and commitment, not a mandatory grid, turn system or campaign model. It does not replace [tactical RPG](tactical-rpg.md), which adds persistent party identity and development. Documentary examples establish possibilities, not the quality of a shipped game's experience. The [review packet](../reviews/full-run-20261010-g07-review-packet.md) records evidence limits and unresolved dependencies.

## Definition and boundaries

For this research, **tactics** is a design lens in which local maneuver, timing, action allocation, information and interaction with a particular objective materially change the available outcomes. “Local” means that the question is how to act within the current situation; it is not a fixed number of turns, actors, minutes or map cells. A strategic decision instead shapes which situations and resources become available. The two can be nested in the same choice and game. This is a proposed analytical definition, not a formal standard, market-tag correction or approved canonical taxonomy change. [C-01]

A short puzzle can contain tactical coordination without a strategic campaign. A campaign tactics game can have persistent upgrades without making character identity its main organizing promise. A tactical RPG becomes relevant when the local task is coupled to persistent party capabilities or identity, but the distinction is an emphasis rather than an exclusive partition. “Board-like” describes a representation or rule structure; “squad” describes a grouping; neither proves that a game uses a grid, that turns alternate, or that the player has perfect information. [C-01, C-02]

Combat is one possible interaction, not the definition proposed here. Infiltration, retrieval, escort, rescue and hazard coordination can make position and action order consequential. That does **not** establish that an inspected stealth game permits a completely pacifist campaign. The present shipped examples verify infiltration and nonlethal alternatives at the document level; a fully nonviolent, noncombat shipped case remains an explicit gap. The worked example below is an invention, not evidence filling that gap. [C-07, C-08, C-14]

## Custom research instructions

The central question is: **what must the player coordinate locally, what information are they entitled to use, and when does a choice become a commitment?** The following instructions are tailored to that question. They are proposed research requirements, not audience findings. [C-01, C-10–C-13]

1. Reconstruct one complete objective sequence, including selection, planning, execution, interruption and resolution. Log actual action costs, timing windows, visibility, terrain interactions and defeat/exit conditions. Do not infer precise rules from a promotional clip, genre label or minimap.
2. Distinguish reachable destination, traversable path, detectable actor, visible target, legal attack and reliable execution. Inspect relevant build-specific geometry and exceptions. A line drawn between two units is insufficient evidence that all six questions have the same answer.
3. Sample alternate turns, initiative queues, simultaneous orders, continuous execution, and pausable/queued hybrids. Include asymmetric terrain/objectives, opposed teams and non-elimination tasks. Keep platform and multiplayer as facets; obtain multiplayer-owner guidance before recommending competitive rollback or hidden-information handling.
4. Separate uncertainty from lack of access. State whether a displayed value is a guaranteed result, conditional forecast, probability estimate, range or presently unknown state. Record what information becomes available after a preview, cancel, failed action or rewind.
5. Seek contrary cases to “more information is always better,” “undo destroys tactics,” “real time is only a dexterity tax,” “symmetry guarantees fairness,” and “the shortest plan is the best plan.” Compare intended goals rather than supplying a universal winner.
6. For player-effect claims inspect original methods, population, measures, effect and uncertainty. For implemented-rule claims acquire a numbered build plus scene/reproduction or recording timestamp. Current document-only coverage cannot satisfy the second requirement by relabeling itself gameplay observation.

## Player promises and varied audiences

Candidate promises include intelligible consequences of planning, satisfaction from coordinating limited options, improvisation when a plan changes, and mastery of timing or spatial relations. They need not coexist. A deliberate solver may want to inspect every currently knowable consequence; a player choosing reconnaissance uncertainty may want the act of acquiring information to cost something. Someone seeking execution timing can reasonably prefer a different pause policy from someone seeking deliberation. These are hypotheses to investigate with the intended audience, not measured demographic categories. [C-13]

Access needs are separate from these preferences. A player can require a selectable input method and still want irreversible strategic commitments. Another can enjoy real-time coordination while needing a pause for an external interruption. Ask whether a time limit is part of the task, an adjustable mode, or a by-product of the interface; do not infer the answer from disability or genre labels. [C-15]

## Characteristic loops and structures

A useful analytical loop is **inspect → form a plan → commit an order → observe execution → revise toward the objective**. Information gathering may itself be a committed action. The loop is not necessarily a separate user-interface phase, and its boundaries can overlap in continuous play. The important question is whether the player can tell which phase a particular action belongs to. [C-02, C-10]

| Structure | What changes the local decision | Important limiting case |
|---|---|---|
| Alternating turns or action budgets | Ordering and opportunity costs are explicit within an activation. | A nominal action-point count does not reveal exceptions, hazards or opponent reactions. |
| Initiative or simultaneous orders | The future state depends on who resolves first or what others commit. | A valid preview at planning time may become false before execution. |
| Continuous execution | Path exposure and timing can matter while the player acts. | A pause changes the timing task; it need not change the spatial problem. |
| Paused/queued planning | Orders can be assembled before time advances, depending on mode. | A coordinated plan can still become invalid; default pause is not a universal entitlement in every difficulty configuration. |
| Asymmetric objectives and terrain | Actors can value different routes, positions or deadlines. | Equal resource counts do not establish equal opportunity; unequal counts do not establish unfairness. |
| Self-contained versus persistent mission sequence | Local success may affect later tools, injuries or deployment. | Persistence does not automatically make narrative/party identity central. Use the tactical-RPG file when it does. |

This matrix is synthesis, not a claim that the inspected sources cover every combination. [C-02, C-09, C-10]

### Action budgets, timing and objective asymmetry

An action budget becomes informative only with its transition rules. Ask whether moving spends a shared pool, whether a second move ends activation, whether overwatch or interception occurs during execution, whether an order reserves a resource, and whether an invalidated action refunds anything. In the inspected XCOM 2 manual, basic action budgets coexist with movement/dash, attack previews, cover and overwatch rules. In SEGA's Valkyria Chronicles 4 documentation, command selection and a directly moved character are combined. These document examples refute a single mandatory representation; they do not specify every exception or certify a current build. [C-03, C-04]

Objective asymmetry means more than giving sides different labels. A unit protecting a device and a unit trying to carry it away may value a doorway differently even on the same map. Damage, elimination and position can then serve the objective rather than define it. This is rule-based reasoning: whether the asymmetry produces good decisions depends on reachable alternatives, understandable information and the intended stakes. An objective that can be completed only by one invisible exception can still be a poor task despite asymmetry. [C-10, C-13]

### Visibility, information and previews

Use a **claim about the next state**, not an undifferentiated “preview,” as the unit of analysis. The player might need to know that an order is legal now, that a path crosses a known threat zone, that an outcome has a stated chance, or that an opposing order is unknown. Those claims have different truth conditions. Previewing the final outcome of a stochastic action as certain is not made fair merely by showing an icon. Conversely, withholding the answer to an intentionally unknown patrol route need not be a defect. [C-11]

The reviewed F02 and P02 guidance supports separating entitled information from intended uncertainty. Apply it here by writing down the protected fact and the fact required for action before designing a visual overlay, sound or text alternative. For example, an accessible alternative can communicate “this known exit is threatened” without naming an unseen actor if the baseline rule does not reveal that actor. This is a proposed adaptation, not an access certification or a shipped observation. [C-11, C-15]

Do not adopt a universal maximum-detail forecast. Under a bounded deterministic puzzle-like task, a reliable next-state preview may support testing plans. Under reconnaissance play, revealing hidden consequences before committing may remove the information-gathering decision. Under simultaneous multiplayer orders, a preview must not expose the opponent's private order. Consider a legality/cost preview, a conditional prediction, a probability/range, or deliberate omission with a clear statement of what remains unknown. The hypothesized benefit must be tested against loss of the intended task. [C-11, C-13]

### Cancellation, undo, rewind and recovery

These are different policies. **Cancel** can retract an uncommitted selection. **Undo** can restore a prior game state. **Rewind** can restore a larger sequence. **Recovery** can offer another viable route while retaining the adverse state. None can literally remove information already learned by the human player. Define state restoration and information consequences separately, including random-state handling and other players' knowledge where relevant. [C-12]

The documentary range is real but does not select a winner: Tactical Breach Wizards advertises free rewinds, while the inspected historical Invisible, Inc. build documents limited rewind and an IRONMAN alternative without it. Into the Breach describes telegraphed attacks; that does not prove complete determinism or any precise undo policy. Desperados III documents coordinated orders with configurable pause. These are contrasting configurations, not independent experiments on learning, enjoyment or stakes. [C-05, C-06, C-08, C-09]

The strongest provisional rule is narrower: **first identify whether an error comes from selecting the wrong input, misunderstanding a knowable rule, accepting an intended risk, or being outplayed; then choose a correction policy for that task.** This is an inference from distinctions, not a universal entitlement to reverse defeat. The same player can need immediate misclick cancellation while deliberately selecting an irreversible campaign. Retain the existing F02/F07 patterns rather than inventing a second “safe preview” pattern here. [C-11, C-12, C-16]

## Applying shared topics

The following IDs refer to **inspected parent-selected reviewed drafts**, all unreleased. Precise sections, revisions and hashes are in the [dependency register](../reviews/full-run-20261010-g07-review-packet.md#reviewed-dependency-register). Links are to the local register rather than nonexistent topic files in this G07-only delivery. Shared evidence is transferred as reviewed synthesis, not freshly verified original research. [C-16]

| Shared entry | Tactics-specific adaptation | Boundary retained |
|---|---|---|
| F02 Decision design, `GDR-CAND-20261010-F02-TOP-01` | Separate known action cost, legal order, conditional forecast and intended hidden information. | Outcome quality is not decision quality; rollback does not erase knowledge. |
| F02 Challenge and difficulty, `GDR-CAND-20261010-F02-TOP-02` | Diagnose rule knowledge, selection/execution demands and available tools before changing enemy power or action budgets. | No universal optimal punishment or challenge threshold. |
| W02 Quests and objectives, `GDR-CAND-20261010-W02-TOP-02` | State the objective result, permitted means, acceptance and aftermath separately; test alternate local routes. | A non-elimination objective is not automatically nonviolent or fail-forward. |
| P02 Controls and input, `GDR-CAND-20261010-P02-TOP-01` | Test actor selection, target selection, paths, queue editing, cancellation and confirmation as one task. | Remapping alone does not remove a timing or targeting demand. |
| P02 Feedback and game feel, `GDR-CAND-20261010-P02-TOP-02` | Distinguish accepted order, interrupted execution, failed outcome and objective resolution. | Stronger feedback is not universally clearer. |
| P02 Multimodal communication, `GDR-CAND-20261010-P02-TOP-03` | Preserve required facts and uncertainty across range, threat, selection and initiative alternatives. | A different modality must not silently reveal protected actor or objective information. |
| F07 Evaluation and balancing, `GDR-CAND-20261010-F07-TOP-01` | Measure prediction accuracy, reasoned alternatives, execution errors and objective outcomes separately. | Completion counts alone do not identify the cause of failure or learning. |
| F07 Ethical and sustainable design, `GDR-CAND-20261010-F07-TOP-02` | Review explicit stakes, failure messaging, interruption and the framing of represented conflict. | Disclosure is not proof of voluntary understanding; no moral judgment is inferred from mode selection. |

P01's corrected accessibility draft and F01's corrected transfer pattern additionally constrain proposed tests: no decontextualized numerical access rule is imported, accommodations are retained, and a changed underlying rule is not called transfer of an unchanged one. Reviewed G06 RPG, F04 combat and F05 simulation bytes were not established here. Broader spatial/scenario, multiplayer and localization dependencies remain open rather than filled by remembered conclusions. [C-16, C-18]

## Pattern selection and adaptations

**Visible opportunity-cost comparison**, `GDR-CAND-20261010-F02-PAT-01`, can compare feasible orders where costs are knowable and a comparison does not reveal protected state. Revalidate stale previews; do not manufacture a nonexistent alternative. **Multi-route objective contract**, `GDR-CAND-20261010-W02-PAT-02`, can distinguish securing an objective from a particular combat method. Do not promise another route that depends on the resource the failed route destroyed. **Legible commitment and safe exit**, `GDR-CAND-20261010-F07-PAT-02`, can clarify irreversible mode choices and bounded interruption; it does not require erasing tactical consequences. [C-16]

The new [Consequence-preserving roster recovery](../patterns/consequence-preserving-roster-recovery.md), `GDR-CAND-20261010-G07-PAT-01`, applies only when a persistent force and a continuation promise make its prerequisite audit relevant. Omit it in a standalone board-like scenario that has no future roster, or in an intentionally terminal run. It is not the general owner of preview, undo or objective design. [C-12, C-16]

The P02 cue-alternative pattern explicitly overlaps P01's existing critical-state cue pattern. G07 adds no third cue pattern and does not resolve that ownership question. Hybrid conflicts stay visible: pause can support planning while removing a desired timing demand; a visible alternative can teach costs while revealing a hidden route; replacement units can preserve campaign feasibility while harming a carefully scarce roster. No genre name wins these conflicts automatically. [C-15, C-16]

## Representative cases and negative cases

| Inspected document and version scope | Narrowly supported case | Misleading comparison rejected |
|---|---|---|
| XCOM 2, Feral base-game manual; mutable `latest`, no numbered build | Action costs, movement/overwatch and attack forecasts can coexist. | A displayed hit chance does not establish an actual outcome, complete rule legibility or all expansion/mod behavior. [C-03; GDR-SRC-20261010-G07-013] |
| Valkyria Chronicles 4, Japanese system documentation, build unspecified | Command-level choices are combined with direct movement and interception. | It is not proof that tactics must use a grid or purely menu-based turns, nor an example of entirely simultaneous real-time play. [C-04; GDR-SRC-20261010-G07-003] |
| Into the Breach, Steam description including Advanced Edition | Attacks are described as telegraphed and protection of buildings matters. | Telegraphed attacks do not establish no randomness, full hidden-state disclosure or a single correct solution. [C-05; GDR-SRC-20261010-G07-007] |
| Tactical Breach Wizards, base-campaign description | Freely repeatable rewinds coexist with an authored cast and level-based perks. | Not a no-level example, not proof that rewind improves creativity for everyone. [C-06; GDR-SRC-20261010-G07-008] |
| Invisible, Inc., developer overview and Early Access build **116318** patch notes | Infiltration emphasis and a historical limited-rewind/IRONMAN contrast. | Not a claim about exact current retail rewind limits or a pacifist campaign. [C-07, C-08; GDR-SRC-20261010-G07-009, GDR-SRC-20261010-G07-010] |
| Desperados III, official overview plus pinned release-day FAQ | Nonlethal/deadly alternatives and simultaneous order execution with an optional pause configuration. | The broad product wording does not mean pause cannot be disabled. Publisher accounts are not experimental corroboration. [C-09; GDR-SRC-20261010-G07-011, GDR-SRC-20261010-G07-012] |

These cases were selected for contrasting structures, not sampled representatively. The absence of a failure postmortem or controlled comparative study is a limitation. No sales, awards or review scores are used to support causation. No numbered current game build, scenario recording or player response was newly observed. [C-18]

### Worked example — rescue without attacks (illustrative, not performed)

The invented task is to open a flooded clinic's exit before the next scheduled water surge. Two rescuers, A and B, each have **two actions in this locally specified turn**. A begins beside a valve; B begins beside a trolley containing a ramp. Both begin within interaction reach of the patient and side hatch, so no unlisted approach movement is required. Closing the valve costs A one action and prevents the surge this turn. Deploying the ramp costs B one action, and carrying the patient across the now-traversable exit costs B one further action. In an alternative route, A can open a side hatch with one action, but carrying the patient through it requires both rescuers to commit one remaining action simultaneously. Moving away from the valve or trolley would cost an action; no attacks, experience levels or random events are specified. These numbers define this example only. [C-14]

With these rules, the ramp route spends A's valve action and both of B's actions, leaving A one action. The hatch route spends A's hatch action plus one carrying action from each rescuer, leaving B one action; without closing the valve, the team must leave before the surge under the specified order of resolution. The designer must explicitly define whether “leave” resolves before the surge and whether the carried patient occupies a safe space. Without that order, it would be dishonest to display both routes as guaranteed successes. This worked reasoning demonstrates a specification question, not a tested optimal strategy. [C-10, C-11, C-14]

An informative interface might show actions remaining, the known surge deadline and the requirement that both carriers are ready. It should distinguish “hatch is open” from “patient has exited.” A cancel before commitment can correct selection without changing the known surge. A rewind after seeing an undisclosed random blockage would create a different information policy; no such blockage belongs in this deterministic example unless its rule is added explicitly. [C-11, C-12, C-14]

**Counterexample:** suppose a pipe breaks during continuous execution and one rescuer must respond immediately. A frozen perfect forecast would no longer describe the task, while unlimited pause might remove the intended response challenge. The design could retain live uncertainty, offer a separately disclosed planning mode, or choose a turn-based rescue puzzle instead. This is a conflict between specified task goals, not proof one genre is superior. [C-13, C-14]

## Accessibility, ethics, localization and production implications

Treat the entire command chain as the access task: identify actor, inspect its state, choose path/target, understand cost, queue/commit, detect interruption, correct a selection and resume later. Test keyboard/controller/touch or alternative inputs only when in scope; do not assume one implementation covers them all. Provide fact-preserving non-color alternatives for ownership, availability and threat, and separately consider visual acuity, reading load, working-memory demands and timing. These are proposed risk audits informed by reviewed P01/P02, not evidence that a particular option is sufficient or universally desired. [C-15]

Real-time or simultaneous multiplayer creates additional constraints. A local pause cannot be assumed to pause other players, and a replay/rollback cannot undo an opponent's learned information. Ranked comparability, disclosure of optional assists and fair interruption handling require a separately reviewed policy. No such competitive policy is supplied by this packet. Do not equate an assist setting with cheating or expose disability-related preferences as a public label by default. [C-12, C-15]

Localize the semantic distinctions between “may,” “will,” “cannot,” “blocked,” “unseen,” “out of range,” and “order accepted.” Reserve room for explanation rather than relying on a single ambiguous verb or color. Names, directional conventions, symbols and accounts of conflict need review in the actual language/cultural context; translating a tooltip does not establish comprehension. The Japanese system descriptions used here have not received independent bilingual review. [C-15, C-18]

Production risks are the consistency of preview and resolution, stale queued orders, path/visibility exceptions, restoration of all relevant state, and authoring a sufficient variety of objective/terrain combinations. A simple action model with a limited forecast may be preferable to a comprehensive but unmaintainable simulation preview. Deterministic computation, hidden information and stochastic outcomes should have separate specification owners and tests. These are engineering questions for a later authorized implementation, not delivered engine code or performance estimates. [C-10–C-12, C-15]

## Research questions and validation

**All tests below are proposals; no participants, prototypes, telemetry or gameplay runs occurred.** Numerical acceptance thresholds and sample sizes must be justified for a selected task before data collection, not borrowed as universal genre standards. [C-17]

**Forecast-entitlement comparison.** For a specified local scenario, compare a legality/cost display with the additional next-state information actually allowed by the design. Hold rules, state, input method and disclosed information constant where the manipulation permits; record any unavoidable difference. Include participants with varied tactics familiarity and relevant access needs. Ask them to predict action costs/outcomes and explain uncertainty, then record selection errors, plans considered, outcome, confidence calibration and experience separately. Counterbalance comparable scenarios rather than having people solve the same revealed puzzle twice. Reject the richer preview for this task if it discloses protected information or undermines the intended reconnaissance decision; narrow its intended benefit if it changes confidence without improving the identified comprehension problem. [C-11, C-17]

**Reversibility comparison.** Compare pre-commit cancellation, state rewind and retained-consequence recovery only after defining which error each targets. Keep action rules and difficulty stable; log information revealed before reversal and changes to random state. Measure corrected mis-selections separately from retries after an accepted bad outcome. Ask about agency, stakes and frustration without combining them into one success score. A within-person comparison is vulnerable to learned solutions, so use matched tasks or counterbalanced conditions with the confound recorded. Reject a blanket reversal recommendation when benefits are confined to accidental selection but the broader rollback removes the intended risk. Competitive hidden-information tasks require separate governance rather than this single-player test transplanted unchanged. [C-12, C-17]

**Time/coordination comparison.** Compare continuous, paused-order and optional-pause configurations only in a prototype where their legal actions and deadlines are explicit. Observe whether differences arise in plan quality, order entry, execution or interruption recovery. Do not describe a timing-rule change as transfer of the same task. For a separate transfer probe, keep the underlying rule constant and vary surface layout or presentation while preserving accommodations; changed-rule adaptation gets a separate outcome. Reject a claim that pause preserves the same experience if the intended challenge was the timed action itself. No result is asserted. [C-13, C-17]

Next discriminating questions are whether geometry/forecast exceptions can be documented in exact builds, which uncertainty belongs to the intended task, whether the noncombat definition survives shipped counterexamples, and how actor/role continuity changes a local design enough to require the tactical-RPG entry. [C-01, C-18]

## Claim ledger

Source suffixes refer to the complete `GDR-SRC-20261010-G07-` identities in References. Claims about documents are classified `observed-example` only at that document level; player benefits remain hypotheses. No formal-standard or empirical-effect claim is added by this entry.

| Claim | Precise claim and class | Inspected support / reasoning | Confidence, limit and unresolved issue |
|---|---|---|---|
| C-01 | Tactics is usefully analyzed through local coordination rather than a required grid, combat system or campaign. `inference` | Proposed definition; contrasts in 003, 007–013 and the assigned taxonomy's nonexclusive framing. | Moderate as a useful partition, not an established boundary; noncombat range remains open. |
| C-02 | Information, planning, commitment and execution can be separated analytically across temporal structures. `inference` | Specified-state reasoning and documented hybrid/queued cases, 003/012. | Moderate; phases need not be visible or discrete in an actual game. |
| C-03 | The Feral manual documents action budgets, movement, forecasts and reaction rules. `observed-example` | 013, Tactical Gameplay, Movement, Actions and Soldier Classes. | High for manual text; no numbered current build or all exceptions verified. |
| C-04 | VC4 documentation combines command selection and direct movement with interception. `observed-example` | 003, Command/Action Modes and interception. | High for text; Japanese translation limits and no gameplay run. |
| C-05 | Into the Breach describes telegraphed attacks and city protection. `observed-example` | 007, Key Features. | High for description; not proof of total determinism, complete information or exact undo. |
| C-06 | Tactical Breach Wizards documents free rewinds and level-based perks. `observed-example` | 008, Experiment freely / Upgrade. | High for description; no causal benefit or precise state-restoration boundary established. |
| C-07 | Invisible, Inc.'s overview emphasizes infiltration and stealth. `observed-example` | 010, The game. | High for document; not evidence of a fully pacifist campaign. |
| C-08 | Build 116318 patch notes document limited rewind and an IRONMAN alternative. `observed-example` | 009, Update 6, New Features. | High for the historical note; exact retail limits and snippet-only details excluded. |
| C-09 | Desperados III sources describe nonlethal options and queued coordination, with configurable pause. `observed-example` | 011 Features; 012 difficulty/Showdown FAQ. | High for text, not all modes/builds or measured effects; broad wording qualified by settings. |
| C-10 | Action, objective and timing rules determine which plans are feasible. `inference` | Explicit rescue example; F02/W02 distinctions. | High for the specified logical relation, not proof of a complete game's reachability or fairness. |
| C-11 | Legal-order previews, outcome forecasts and entitled information require different truth conditions. `inference` | Reviewed F02 Decision design and P02 Multimodal communication; 013 as documented example. | Moderate; best disclosure policy depends on intended uncertainty and access. |
| C-12 | Cancel, state reversal, retained-consequence recovery and acquired human knowledge are distinct. `inference` | F02 commitment analysis; contrast 008/009. | High conceptual distinction; no universal choice of policy or competitive effect. |
| C-13 | Different planning, uncertainty and timing promises can reverse the preferred preview/pause policy. `hypothesis` | Proposed comparisons and contrary cases; 007–012 document alternatives only. | Low for audience effects; no preference distribution measured. |
| C-14 | The synthetic rescue rules illustrate local noncombat coordination and specification ambiguities. `inference` | Fully labeled invented example, not a shipped case. | High for stated arithmetic/conditions; feasibility depends on the explicitly unresolved resolution order. |
| C-15 | Whole-task access, fact-preserving localization and state-consistency audits address relevant risks. `inference` | Reviewed P01/P02/F07 and task decomposition. | Moderate as conditional audit questions; no certification or implementation cost estimate. |
| C-16 | The listed shared patterns apply conditionally without a new preview/cue pattern. `inference` | Inspected selected dependencies and overlap notes in the packet. | Moderate; final ownership/merge decisions await Coordination. |
| C-17 | The proposed comparisons can challenge the recommendations rather than merely count wins. `hypothesis` | Test protocols and reviewed F01/F07 methods. | Low until protocol validity is checked; all unperformed. |
| C-18 | Source coverage is document-based with named build, effect and dependency gaps. `inference` | Session access log and packet. | High about what was inspected here, not absence of external evidence. |

## Contradictions and coverage status

Keep **G07-CON-03** (forecast/reversal versus intended uncertainty), **G07-CON-04** (genre boundaries), **G07-CON-05** (broad pause claim versus mode configuration) and **G07-CON-06** (document/current-build distinction) visible. The setting qualification narrows the apparent pause conflict; the other questions are not resolved by a genre rule.

Researched: local objective/action/timing relations, documentary temporal variants, information entitlement, cancellation versus rollback, asymmetric/non-elimination tasks, conditional shared-pattern use and test design. Open: actual numbered-build geometry and scene records; simultaneous-order uncertainty; fully nonviolent shipped cases; representative board-like examples; competitive rollback; original causal player evidence; complete reviewed combat/simulation/spatial/localization dependencies. This is a complete bounded draft, not complete taxonomy-heading coverage.

## Review and history

Version **0.1.0**, `initial-draft-1`, no predecessor or supersession. Author self-review is in the packet; independent review has not occurred and approval fields remain null. Hashes are external. Gates C, D and E are not declared passed. The next decision is independent review of the boundary and the conditional forecast/reversal argument, with exact-build verification queued rather than presumed.

## References

All listed sources were accessed on **2026-10-10 (America/Los_Angeles; session also falls on 2026-10-11 UTC)**. The G07 author inspected the cited text through web retrieval. Unless explicitly stated otherwise, `observed-example` means observation of the named document, **not play of a game build**; no scene/timestamp or reproduction is invented. Public-page bodies were not archived in this deliverable. Copyright remains with the respective owners; short paraphrases and source metadata only, no redistributed screenshots, game assets, article bodies or manual pages. Repeated IDs identify the same source across G07 files. Cross-batch URL/DOI/edition deduplication is pending Library Coordination.

### GDR-SRC-20261010-G07-003

**SEGA. [Valkyria Chronicles 4 — SYSTEM](https://portal.valkyria.jp/vc4/system/inner.html?page=tank).** SEGA. Publication/update: unknown. Edition/build: Valkyria Chronicles 4; Japanese PS4-style controls documented; numbered build unspecified. Access: `relevant-excerpt`. Type: first-party system documentation.

**Exact locator:** Command Mode and CP; Action Mode and AP; aiming/weak points; enemy interception, browser extraction lines 113–158. **Supports:** C-04. **Limits:** English paraphrase of Japanese body text and AP text/alt description. No image-based measurement or gameplay observation. This documents a turn/action hybrid; it is not evidence of an entirely simultaneous real-time simulation. **Independence:** SEGA production/documentation; the linked English manual shell was accessible but its body did not render.

### GDR-SRC-20261010-G07-007

**Subset Games. [Into the Breach — About This Game / Key Features](https://store.steampowered.com/app/590380/Into_the_Breach/).** Subset Games via Steam. Publication/update: page update unknown; base release 2018-02-27. Edition/build: Steam description with Advanced Edition section; no executable version inspected. Access: `relevant-excerpt`. Type: first-party developer product description.

**Exact locator:** Advanced Edition and Key Features: Defend the Cities / Perfect Your Strategy / Build the Ultimate Mech, browser extraction lines 193–206. **Supports:** C-05. **Limits:** Telegraphed attacks do not prove globally perfect information, absence of randomness, every undo rule or a unique solution. Official standalone site was blocked; Steam repeats developer wording rather than adding independent corroboration. **Independence:** Subset production; standalone-site search excerpt and Steam copy belong to one underlying account.

### GDR-SRC-20261010-G07-008

**Suspicious Developments. [Tactical Breach Wizards — About This Game](https://store.steampowered.com/app/1043810/Tactical_Breach_Wizards/).** Suspicious Developments via Steam. Publication/update: page update unknown; release 2024-08-22. Edition/build: Steam product description; base campaign; numbered build unspecified. Access: `relevant-excerpt`. Type: first-party developer product description.

**Exact locator:** Experiment freely, rewind your mistakes; Upgrade your magical arsenal; Get to know these loveable idiots; What is it not?, browser extraction lines 213–257. **Supports:** C-06. **Limits:** Free rewinds and level-based perks are documented. No controlled evidence of creativity, learning or enjoyment. Does not establish complete determinism or exact rewind state boundaries. User tags/reviews excluded as authorities. **Independence:** Suspicious Developments production; repeated store URLs are the same source identity.

### GDR-SRC-20261010-G07-009

**Klei Entertainment; Steam developer announcement feed. [Early Access Update 6: Archive Ghosts — Patch Notes](https://store.steampowered.com/news/posts/?appids=243970&enddate=1418154489).** Klei via Steam. Publication/update: 2014-11-10 in the inspected Steam feed; linked forum lead dated 2014-11-07. Edition/build: Invisible, Inc., Early Access build 116318 only. Access: `relevant-excerpt`. Type: first-party versioned patch notes.

**Exact locator:** 10 November Update 6 block: Build 116318, New Features and Bug Fixes; browser extraction lines 82–118. **Supports:** C-08. **Limits:** Inspected text documents limited save/reload and IRONMAN without rewind. The once-per-mission and previous-turn wording appeared only in a blocked forum lead, so is not used as inspected support. This is not the current retail rule set. **Independence:** Klei; duplicate blocks and the linked forum are derivative routes to one announcement, not independent observations.

### GDR-SRC-20261010-G07-010

**Klei Entertainment. [Invisible, Inc. — The game](https://www.klei.com/games/invisible-inc/).** Klei Entertainment. Publication/update: unknown. Edition/build: Base-game overview, with separately described Contingency Plan expansion; build unspecified. Access: `relevant-excerpt`. Type: first-party product overview.

**Exact locator:** About / The game and separately headed Contingency Plan, browser extraction lines 17–29. **Supports:** C-07. **Limits:** Supports an infiltration/stealth emphasis, not a claim that every mission is pacifist, every enemy can be bypassed or any particular objective/rewind implementation persists into retail. **Independence:** Same Klei production context as source 009; overview is not independent effect evidence.

### GDR-SRC-20261010-G07-011

**THQ Nordic / Mimimi Games. [Desperados III — Official Game Site](https://desperados3.thqnordic.com/).** THQ Nordic. Publication/update: unknown. Edition/build: Desperados III product overview; build unspecified. Access: `relevant-excerpt`. Type: first-party publisher product overview.

**Exact locator:** Features: skills, non-lethal/deadly attacks, difficulty/replay challenges, Showdown pause. **Supports:** C-09. **Limits:** Feature descriptions, not observed player outcomes; the broad pause wording needs the configuration qualification in source 012. No claim non-lethal actions have identical objectives or consequences. **Independence:** Mimimi / THQ Nordic production; related to source 012, not an independent comparative experiment.

### GDR-SRC-20261010-G07-012

**Zyddie, displayed as an Officer in the pinned Desperados III Steam forum. [Desperados FAQ](https://steamcommunity.com/app/610370/discussions/0/2451595501488396622/).** Official Desperados III Steam community forum. Publication/update: 2020-06-16; last edit date not established. Edition/build: Launch-era FAQ; PC-style mission-selection interface; numbered build unspecified. Access: `relevant-excerpt`. Type: first-party community/support FAQ as presented in the official game forum.

**Exact locator:** Game & Content Questions: difficulty, deactivating Showdown pause, guard spotting and multiplayer/co-op; browser extraction lines 80–98. **Supports:** C-09. **Limits:** Author role is the displayed game-group Officer designation, not a separately verified employment credential. Configuration is documented, not runtime reproduced; multiplayer difficulty explanation is practitioner opinion without measured outcomes. **Independence:** Same Desperados production/support context as source 011.

### GDR-SRC-20261010-G07-013

**Feral Interactive; XCOM 2 documentation for the Firaxis / 2K game. [XCOM 2 — manual](https://www.feralinteractive.com/en/manuals/xcom2/latest/steam/).** Feral Interactive. Publication/update: publication/update unknown; copyright is not treated as publication date. Edition/build: XCOM 2 Steam port manual, base-game framing; latest URL is mutable, not a pinned build; War of the Chosen/mods excluded. Access: `relevant-excerpt`. Type: official port-publisher game manual.

**Exact locator:** Displayed manual pages 6–10: Health, Action Points, Concealment, Cover, Actions, Soldier Classes, Strategy Layer; browser extraction lines 190–283. **Supports:** C-03. **Limits:** Basic documented action budget and preview fields are not exception-free rules for all perks/builds. No live combat, random-number mechanism, line-of-sight geometry or original PC behavior reproduced. **Independence:** Firaxis / 2K game, Feral port documentation; not independent evidence of feature effectiveness.

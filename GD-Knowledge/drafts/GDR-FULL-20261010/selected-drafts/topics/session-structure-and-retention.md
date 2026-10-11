---
id: GDR-CAND-20261010-F06-TOP-02
kind: topic
title: Session structure and retention
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
run_id: GDR-FULL-20261010
batch_id: F06
attempt_id: F06-authoring-01
owner_project: BH-GDR-Foundations-and-Systems
updated: '2026-10-11'
evidence_checked: '2026-10-11'
date_basis: UTC inspection/assembly date; run and authorization date remain 2026-10-10
aliases:
- save and suspend
- checkpoints and interruption
- return after absence
- respectful engagement
- session goals
tags:
- session-model
- saving
- checkpoints
- interruption
- re-entry
- repeat-play
- autonomy
- persistent-consequences
related_topics:
- GDR-CAND-20261010-F06-TOP-01
- GDR-CAND-20261010-F01-TOP-02
- GDR-CAND-20261010-F01-TOP-03
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F07-TOP-02
related_patterns:
- GDR-CAND-20261010-F06-PAT-02
- GDR-CAND-20261010-F07-PAT-02
- GDR-CAND-20261010-F01-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-F06-008
- GDR-SRC-20261010-F06-009
- GDR-SRC-20261010-F06-010
- GDR-SRC-20261010-F01-14
- GDR-SRC-20261010-F02-009
- GDR-SRC-20261010-F07-012
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: First F06 submission; conditional research synthesis, no release or
  tested outcome benefit.
hash_record: ../reviews/full-run-20261010-f06-integrity-receipt.md
---

# Session structure and retention

**Research candidate, not released guidance.** Version 0.1.0; candidate revision `initial-draft-1`. The goal is not to maximize attendance. It is to help designers decide what a worthwhile session asks of a player, what stopping preserves or changes, and what makes a later return intelligible and voluntary. The [review packet](../reviews/full-run-20261010-f06-review-packet.md) records limitations and gates.

## Decision and scope

Design the **entry → activity → interruption/exit → absence → return** contract. Consider a person with an uninterrupted evening, a short available interval, a recurring group commitment or an unexpected need to stop. These are illustrative circumstances, not assumptions about a preferred audience. Distinguish the duration of a meaningful activity from the duration of uninterrupted attendance it demands. [C-01, C-09]

Coverage includes saves, checkpoints, suspension, interruptions, reconnection, re-entry after changed content, self-chosen and assigned goals, repeat play, persistent consequences and respectful engagement. The entry compares synchronous/asynchronous and persistent/session-based designs without selecting a genre. It does not design save serialization, cloud conflict resolution, server transactions, notification delivery, a monetization economy or legal compliance. Those require separately approved implementation and specialist work. [C-01, C-16]

### Working definitions

| Term | Meaning used here | Distinction that matters |
|---|---|---|
| Session | A bounded episode of participation as defined for a particular question. | A launcher connection, a party activity and the player's experience may have different boundaries. |
| Save | A persisted representation from which specified state can be restored. | Persistence does not by itself promise rollback, repeat use, cross-device access or preservation of every state. |
| Checkpoint | A designated recoverable state or boundary. | A recovery checkpoint is not necessarily a safe immediate stopping place. |
| Suspend | An interruption that preserves a continuation state under a stated contract. | It need not grant a reusable earlier attempt or erase a consequence. |
| Reconnect | Rejoining an activity or authority that may have continued. | The client’s old display is not necessarily the current shared state. |
| Re-entry | Reconstructing enough intention, state, rules and available action to participate again. | A recap can be accurate yet irrelevant, or helpful-looking yet stale. |
| Retention | An explicitly defined return measure over an exposure window and eligible population. | Returning is behavior, not a direct measure of enjoyment, autonomy or wellbeing. |

These definitions are an analytical vocabulary, not a formal standard or a mandated event schema. The denominator and temporal boundary must be specified before interpreting a retention measure. A person who completes the desired experience and chooses not to return is not automatically a failed design outcome. [C-01, C-11, C-14]

## Core explanation and mechanisms

### Preserve consequences separately from requiring continuous attendance

A failure rule can persist across a break without requiring the person to remain continuously present. Conversely, a frequently saved state may still be difficult to leave if group obligations or an expiring opportunity continue outside it. Analyze state, time and social commitment separately. [C-09, C-13]

Housemarque's Returnal 2.0 announcement describes single-use suspension, deleted on resumption, rather than a reusable rollback point. It also excludes boss battles, cinematics, first-person sequences and intense combat. This is a documented design distinction—not measured proof of accessibility or preserved challenge. Its exclusions are a useful counterexample: a person may need to stop precisely where the feature is unavailable. [C-02; GDR-SRC-20261010-F06-010]

Microsoft's XAG 108 recommends regular saving and scoped pause availability for single-player, local multiplayer and local split-screen, excluding save/load screens. This is practitioner accessibility guidance, not a legal obligation, universal checkpoint interval or claim that a persistent online world can pause for one person. [C-03; GDR-SRC-20261010-F02-009]

The conditional bridge is to name the consequence that matters before selecting a persistence mechanism. Does the design need an outcome to remain committed, a random result not to be retried, a turn to count, a shared asset to remain changed, or only an authored dramatic sequence to feel continuous? These are different requirements. Compare single-use continuation, explicit end-of-phase saves, ordinary rollback, group pause, or a shorter activity. If the intended consequence cannot be explained without “the player must stay because we want more time,” reopen the design rather than calling the burden essential. This is a proposed decision process, not a studio-approved rule. [C-09, C-10]

### Interruption creates a context problem, but “add a recap” is not an established cure

Altmann and Trafton's four laboratory experiments involved 96 undergraduates. They found a resumption cost in their task; cue effects varied, with a reliable cue benefit only at the longest tested warning lag and a marginal omnibus cue test. The manipulation exposed the task context **before** an interruption, not an authored recap after days away. This supports investigating resumption demands while limiting the inference that any re-entry summary improves gameplay. [C-04; GDR-SRC-20261010-F06-008]

XAG 109 supplies a distinct practitioner rationale for reviewable objectives, history, optional reminders and revisitable tutorials. It is not empirical validation of a particular recap or proof of improved retention. Its framework explicitly distinguishes accessibility best practices from legal/compliance requirements. [C-05; GDR-SRC-20261010-F01-14]

The [State-validated re-entry brief](../patterns/state-validated-re-entry-brief.md) therefore remains a hypothesis-driven recipe. It separates the last chosen intention, what is now true, what changed, and what can be done next without committing the player. The brief is not an answer key and must respect the character/player's entitled knowledge. A changed objective or revoked shared permission needs a current-state explanation; a forgotten rule may need optional practice; an unfamiliar input binding needs a different recovery route. [C-08, C-15]

### Session goals can provide closure without demanding another session

A session goal is a useful organizing device when it describes a recognizable outcome the person can endorse. It can be selected by the player, proposed by the game, negotiated by a group or deliberately absent in open-ended play. Completion, useful progress, a changed decision or a satisfying stopping point need not all coincide. The design question is which kind of closure the activity promises and whether the return prompt misrepresents unfinished work as a debt. [C-11]

For repeat play, distinguish learning, experimentation, social continuity, expression, collection, changing conditions and simply enjoying a familiar activity. These are candidate reasons to investigate, not a list of universal motivators. A long-term progression layer is not automatically necessary. Compare a clear rematch or revisitable activity with a calendar reward before adding an obligation that changes the experience being measured. [C-11, C-12]

A contrary case is an intentionally unresolved expedition or ongoing collaborative project. Forcing every session to end with a complete goal could destroy the continuity people chose. A remembered intention and an honest account of what remains can be preferable to artificial completion. The requirement proposed here is an understandable stopping/return contract, not constant closure or the abolition of persistent consequences. [C-09, C-11, C-13]

### Respectful engagement cannot be inferred from return frequency

Frommel and Mandryk's cross-sectional guided-recall survey of 178 respondents found mixed accounts of engagement rewards: valued incentives and access alongside missing-out costs and obligation. Its two interaction measures were continuous and non-exclusive, not randomized player categories. The reported associations cannot establish that a calendar mechanic causes a particular motivation or wellbeing outcome. [C-06; GDR-SRC-20261010-F06-009]

Vuorre and colleagues used publisher play records and surveys from 38,935 adults across seven games over six weeks. Their small average estimated playtime effects, under stated assumptions, do not certify an individual mechanic as safe or make time played a wellbeing measure. Exposure, population and outcome differ from the reward survey, so these are not contradictory findings about the same intervention. [C-07; GDR-SRC-20261010-F07-012]

The application bridge is to compare the offered activity with the costs of declining, missing, delaying or ending it. A reminder can serve a self-chosen intention, while a deadline can impose a loss the person did not expect. An apparently optional reward can become functionally difficult to decline if it supplies an essential resource or keeps the person eligible for group participation. Those are hypotheses about local incentive effects, not claims that every daily reward is manipulative. [C-12, C-13]

Removing every scheduled activity is not the only respectful alternative. People may value a regular gathering or ritual. Compare player-controlled reminders, a non-expiring goal, accumulating progress, a broad participation window, an ordinary repeatable activity or no external reminder. Evaluate what is lost as well as gained. The F03 queue already contains **Absence-tolerant personal reward horizons**; this batch preserves that unresolved child proposal rather than duplicating it as a third pattern. [C-06, C-11, C-12]

## Design choices and alternatives

### Persistence and time model

| Model | Design opportunity | Costs and adverse cases to resolve |
|---|---|---|
| Private paused state | Stop and return to the same local decision. | Save corruption, changed controls/content and stale intentions; pausing does not necessarily restore remembered context. |
| Single-use continuation | Separate attendance from replay of a past state. | Consuming the point too early, uncertain recovery after a failed resume, and excluded high-pressure situations. This is a design contract, not an implementation guarantee. |
| Reusable checkpoint/rollback | Let a player retry from a known state or recover from an unwanted result. | It changes repetition and information acquisition; already learned facts cannot be made unknown by reloading. |
| Shared synchronous session | Preserve mutual presence and coordinated timing. | Pause negotiation, departure cost, rejoin rules, substitution and obligations on remaining players. |
| Shared asynchronous activity | Permit participation at different times. | Waiting, stale plans, notification pressure, turn deadlines and unequal access to current state. |
| Persistent world | Permit continuity beyond any one participant's session. | Offline consequences, changing authority, missing events, content migration and promises that cannot be fulfilled for every returner. |

These are alternatives to reason about, not mutually exclusive genres. A game can combine them, but the boundaries must be visible—for example, local menus may pause input without pausing a shared world. [C-01, C-09, C-13, C-16]

### Re-entry and goal support

| Option | Use when | Prefer less when |
|---|---|---|
| Optional current-state brief | The player may have forgotten an intention or the world changed. | Current state is already immediately legible; the brief would repeat obvious facts or leak a solution. |
| Reviewable history | The person needs context at their own pace. | A dense transcript hides the few changes relevant to the next decision. |
| Optional safe practice | The rule or input is unfamiliar after absence or a change. | A forced tutorial would punish a competent returner or disable established access supports. |
| Self-chosen session objective | A selectable target can orient an open activity. | The player values exploration without task pressure; omit the target rather than manufacturing an obligation. |
| Explicit group commitment/handoff | Another person's plans depend on attendance. | The activity can be made independent or asynchronous more simply. |
| Reminder or scheduled reward | The player knowingly chooses a routine and can understand refusal costs. | Declining causes unexpected loss, essential access pressure or an unmanageable production commitment. |

Every proposed benefit above requires local verification. No default session length, checkpoint spacing, streak duration, notification cadence or acceptable churn target is supplied. [C-08, C-10–C-16]

## Application process

1. **Specify the intended episode and return measure.** Identify the outcome, eligible population, mode, start/end events, offline state and observation horizon. Keep the designer's activity boundary separate from the telemetry event. State whether successful completion without return is acceptable. [C-01, C-11, C-14]
2. **Map commitment and persistence.** For each transition, state what is already committed, what is merely staged, what persists after exit and who else is affected. Include authority over shared state and the difference between intention, request, acceptance and result. [C-09, C-13]
3. **Challenge continuous-attendance requirements.** Compare stopping immediately, stopping at a phase boundary, delegating, substituting, surrendering with a known result, and redesigning the activity to be shorter. A warning about an inflexible commitment does not itself remove the burden. [C-09, C-10]
4. **Specify resumption, not just storage.** Distinguish a paused private state from a continuing shared world. Define current-state validation, changed-content explanation, restored access settings and prevention of duplicate commitments. A user-facing “saved” message must not imply a recovery capability the implementation has not established. [C-08, C-16]
5. **Offer the minimum relevant context.** Restore the last chosen intention only as a revisable note; present current facts and material changes separately. Offer optional history/practice. Make choosing a different goal or leaving again a valid result. [C-05, C-08, C-15]
6. **Inspect incentives around absence.** Compare the actual outcomes of ignoring reminders, missing a reward, returning late and letting another person continue. Coordinate resource/economy consequences with F03 when its reviewed bytes become available. Do not adopt an unreviewed progression claim to fill the gap. [C-12, C-13]
7. **Evaluate against a simpler baseline.** Test task comprehension, valid continuation, avoidable loss, perceived commitment and burden alongside any return metric. Obtain separate authority before participant work. Adapt or omit the mechanism when its intended benefit is absent or its guardrails fail. [C-14]

## Patterns and genre adaptations

This entry extracts [State-validated re-entry brief](../patterns/state-validated-re-entry-brief.md), `GDR-CAND-20261010-F06-PAT-02`. Its distinct contribution is **state freshness, provenance and knowledge entitlement at return**, not a duplicate of general onboarding. F01's `GDR-CAND-20261010-F01-PAT-01`, **Supported attempt and transfer check**, remains the owner of supported practice and discriminating transfer. F07's `GDR-CAND-20261010-F07-PAT-02`, **Legible commitment and safe exit**, remains the owner of general refusal/exit design.

No genre guidance is invented. A future genre file must examine whether uninterrupted performance, persistent risk, a synchronized event, private discovery or a leisurely routine is actually part of its local promise. Those constraints can conflict within one hybrid activity. A genre label never overrides the need to explain which fact is being preserved and whose time bears the cost. [C-09–C-13]

## Examples and counterexamples

### Illustrative: returning to a shared project after a rules update

Before leaving, a contributor selected “assemble a support module,” possessed four components, and expected the recipe to require three. On return, another contributor has moved some shared components, the recipe now requires five, and the player's edit permission changed. These numbers are **invented example state**, not recommended economy settings or a performed test. [C-08, C-15]

A candidate brief first validates which inventory belongs to the returning person and which is shared. It says the old intention is still recorded, shows the current eligible components and the changed requirement, and makes the permission change visible. It offers reviewing the recipe, choosing another task or requesting the required permission; it does not press the crafting button or promise unavailable resources. A private discovery by another participant is omitted unless the game's knowledge rules authorize sharing it. [C-08, C-09]

The key discrimination is between **forgetting the old rule** and **encountering a changed rule**. An explanation that merely repeats the old recipe is harmful even if the person remembers it perfectly. A mandatory tutorial that assumes poor skill is also a poor diagnosis. Testing must vary the answer: an affordable case, an unaffordable case and an exact-availability case should not all invite the same response. Asking what is permitted is separate from asking what the person prefers to make. Ordinary information and accommodations stay available. This preserves F01's reviewed correction without claiming F06 validation. [C-15]

### Illustrative: a synchronous group with an unpredictable departure

A group chooses a shared activity with a known ending. One person needs to leave before it finishes. Compare a declared handoff, an agreed reduced-role continuation, a replacement entrant, a fixed departure outcome and ending the activity. No option is universally best: a replacement may disrupt a private group; handing off may expose private information; automatic action may create a competitive advantage; forcing the remainder to continue may transfer the burden. The valid option is one whose effects participants can understand and the system can actually uphold. [C-09, C-13]

An “exit without consequences” feature is not automatically fair to opponents or partners. Conversely, “you knew the commitment” is not sufficient evidence that departure costs are acceptable for the intended audience. The unresolved decision is which persistent consequences serve the activity and which attendance requirements can be relaxed without erasing it. [C-09, C-10, C-13]

### Illustrative: a recurring reward and a completed game

A designer compares an expiring daily objective with a self-chosen objective that remains available. The latter is not assumed to improve retention; it might reduce the reminder that some players welcome. A second baseline offers no reward schedule at all. The comparison asks whether people value the activity, understand absence consequences and feel able to stop—not which version produces the most logins. This is proposed future work owned jointly with F03's queued reward-horizon question, not a new F06 pattern. [C-11, C-12]

A separate counterexample is a deliberately finite experience. After finishing, a person chooses not to replay. Adding a calendar incentive solely to reverse that behavior can change the product's promise rather than repair it. The team must define the desired outcome before treating non-return as a defect. [C-01, C-11]

## Failure modes and constraints

**Misleading persistence:** Autosaving the wrong state, consuming a continuation before a usable resume, duplicating a committed action, reverting another person's progress or restoring an invalid content version can break the stated contract. These are design/engineering risks to specify and test later, not claims about a particular engine. The design requirement is truthful recoverability; implementation must determine how it is achieved. [C-09, C-16]

**Inaccurate or over-prescriptive re-entry:** A brief can blend historical intention with current facts, reveal an undiscovered answer, conceal changed input settings or automatically recommend a goal the player no longer wants. More summary is not necessarily more useful. Offer optional depth and an honest unavailable/unknown state rather than inventing certainty. [C-08, C-15]

**Pressure relocated rather than removed:** A wider reward window can still exclude a person; accumulated tasks can become a larger backlog; a catch-up bonus can affect other players or the economy; an asynchronous task can generate repeated notifications. These are hypotheses to evaluate, not evidence that any named alternative prevents harm. F03 economy effects remain dependency-limited. [C-12, C-13]

**Access, language and production:** Saving, restoring, choosing a slot, understanding a change and reviewing a history must be reachable through the intended input and sensory routes. Do not import web CSS measurements or platform examples as universal native-game defaults. Calendar language requires explicit timezone and expiry semantics; shared intentions, pronouns and ownership references must survive translation. Maintaining migration explanations and prior decisions creates authoring and support cost, especially when content is removed. No numerical language-expansion budget or support service level is asserted. [C-05, C-16]

**Local and shared time differ:** A pause icon cannot truthfully imply that teammates, server time, an auction or a shared turn has also stopped. If offline consequences continue, disclose their relevant scope before commitment and on return. A person's notification preferences should not be treated as proof they have waived all absence-related costs. These are proposed clarity requirements, not legal consent determinations. [C-01, C-13, C-16]

## Playtest and validation

**Proposed, not performed.** No participant testing, actual game save operation, engine prototype or live retention experiment occurred. These test specifications are not validated measures, approved protocols or completed Gate D host tests. [C-14]

| Question | Comparison and procedure | Measures, limits and rejection rule |
|---|---|---|
| Can attendance be interrupted without changing the intended consequence? | Compare the current design with a stated continuation or shorter-phase alternative. Use synthetic failure/reconnect cases before human testing. | Verify which state commits, persists and resumes; inspect partners' outcomes. Reject a “preserves stakes” claim if it permits unauthorized retry or erases shared consequences. Reject an interruption-support claim if likely exit situations remain unsupported without disclosure. |
| Does state validation improve return decisions? | Compare current UI, reviewable history and PAT-02 brief with equivalent factual access. Include brief absence, longer absence, changed rules and no changes separately. | Measure correct understanding of current state, time to a self-chosen valid action, errors, unwanted commitments and spoiler reports. Reject the brief if it mainly adds delay, makes no worthwhile difference or leaks entitled-knowledge boundaries. |
| Is the problem memory, rule change or input access? | Use changed-answer probes and optional practice; hold accommodations and ordinary state information available. | Ask what is permitted, then preference; do not score refusal as misunderstanding. Correct repeated answers alone are insufficient. A changed-rule case misdiagnosed as forgetting falsifies the proposed diagnostic route. |
| Does a recurring prompt serve an endorsed intention? | In a separately approved low-risk study, compare player-controlled reminders, a non-expiring option and no prompt; retain equal access where possible. | Ask about valued routine, unwanted obligation, regret and informed refusal; track behavior without calling it wellbeing. Reject “respectful” solely from higher return rate. Seasonal events, calendar demands, self-selection and group spillover limit attribution. |
| Does a group return contract distribute costs acceptably? | Simulate handoff, non-return and replacement among consenting groups; no surprise abandonment manipulation. | Observe stale commitments, unwanted role transfer, understandable permissions and willingness to continue. Report partner and returner experiences separately. |

Specify eligible returners, exposure to the feature, completed-game exclusions, uncertainty and missing data before interpreting a cohort. Avoid measuring “voluntary return” as a login following a forced reminder. Participants who decline or fail to return may be central evidence rather than inconvenient missing successes; collecting their reasons still requires appropriate consent and minimization. Group dependence and repeated sessions require an analysis plan, not event-count inflation. [C-14]

## Claim ledger

| Claim | Precise claim / class | Evidence and locator; support or challenge | Applicability, confidence and unresolved question |
|---|---|---|---|
| C-01 | Session, persistence, attendance, re-entry and return metrics answer different questions. `inference` | Reviewed F01 core-loop horizons, F02 reversibility and F07 measurement distinctions; working definitions above. | Moderate as analytical separation, not a formal schema. Which boundary matches the actual decision? |
| C-02 | Returnal's historical 2.0 account documents single-use suspension and excluded situations. `practitioner-heuristic` | F06-010, Suspend Cycle. | High for documentary content, low for outcome claims. No played build or accessibility comparison. |
| C-03 | XAG 108 recommends saving and pause within stated contexts. `practitioner-heuristic` | F02-009, Implementation guidelines: saves and final pause bullets. | Moderate as scoped guidance; not universal online pause, legal compliance or a timing default. |
| C-04 | The interruption experiments show a resumption cost but mixed cue benefit, not validation of an after-absence recap. `empirical-evidence` | F06-008, Method and Results, printed pp. 44–46. | Moderate for laboratory results; low for transfer to changed-content gameplay. Cue timing, task and population differ. |
| C-05 | XAG 109 supports reviewable objectives/history and optional revisit/reminder routes. `practitioner-heuristic` | F01-14, Implementation guidelines; framework Introduction. | Moderate for guidance, not measured retention or a universal recap structure. |
| C-06 | Survey respondents reported both benefits and burdens of engagement rewards; associations do not establish causation. `empirical-evidence` | F06-009, §§3–4, §5.3; Tables 2–3 inspected. | Moderate for selected adults' reports, low for particular mechanics or populations. Two non-exclusive continuous measures, recall/framing and coding limits. |
| C-07 | The playtime study's small average estimates cannot certify a mechanic or infer wellbeing from attendance. `empirical-evidence` | F07-012, §§2–4.1 and stated identification/attrition limits. | Moderate for the bounded observational result; no individual, child or mechanic-specific inference. |
| C-08 | A current-state, knowledge-scoped, optional re-entry brief may support valid self-chosen continuation. `hypothesis` | C-04/C-05 motivate the problem; reviewed F01/P01/P02 supply constraints; PAT-02 specifies an untested chain. | Low for benefit: no matched gameplay comparison, and stale data or spoilers can reverse it. |
| C-09 | Persistent consequences and continuous attendance can be analyzed separately; choose recovery around the actual invariant. `inference` | C-02/C-03; reviewed F02 decision distinctions and F07-PAT-02. | Moderate logically, not a promise every state can suspend safely. Which invariant matters and can be upheld? |
| C-10 | Comparing shorter phases, suspension and other exits may expose unnecessary attendance burden. `hypothesis` | C-02/C-03 and F07 exit recipe; no local comparison. | Low for preferred outcome. Some chosen activities need continuity, and others bear departure costs. |
| C-11 | Closure, repeat play and non-return after completion require goal-specific interpretation. `inference` | Reviewed F01 horizons/motivation and F07 evaluation; explicitly proposed alternatives. | Moderate as decision framing; no universally superior session goal or repeat incentive. |
| C-12 | Inspect refusal/absence costs and compare reminders/reward schedules with non-expiring or no-prompt alternatives. `hypothesis` | C-06/C-07; F03 queued reward-horizon question is context only. | Low for net benefit; removing routine can remove valued access or structure. Economy effects unresolved. |
| C-13 | Shared continuity requires explicit commitments, state freshness and cost distribution among returners and others. `inference` | Reviewed F07-PAT-02 and F06 multiplayer reasoning; synthetic scenarios. | Moderate for logical dependency, low for a preferred handoff. Which costs are knowingly accepted? |
| C-14 | Evaluate valid continuation, burden and intended experience separately from return behavior, with correct units and uncertainty. `inference` | Reviewed F07 evaluation/PAT-01; C-06/C-07 measurement limits. | Moderate as method, no participant result or sample-size guarantee. Can a feasible comparison identify the effect? |
| C-15 | Re-entry probes must distinguish changed rules, forgotten relations and input barriers; preserve accommodations and varied correct answers. `inference` | Actual corrected F01-PAT-01 recipe/worked examples; F02 demand separation and P02 remapping. | Moderate as diagnostic logic; no validated F06 instrument. Could cues, guessing or memorization explain success? |
| C-16 | Truthful recovery and localized, accessible change information require maintained state/ownership semantics and production support. `inference` | C-03/C-05; reviewed P01 information contract, P02 outcome/receipt distinction and F07 production obligations. | Moderate as design dependency, not runtime assurance. Missing migration/authority cases can invalidate the promise. |

`F06-...`, `F01-14`, `F02-009` and `F07-012` abbreviations expand to the exact run-scoped source identities in References. The existing identities are retained; no permanent SRC number is allocated.

## References

Public sources were inspected on **2026-10-11 UTC**. Each record below identifies the exact scope used, not whole-literature coverage. A working URL is not a license to reproduce its media. Local claim IDs are scoped to this artifact.

### GDR-SRC-20261010-F06-008

**Erik M. Altmann and J. Gregory Trafton.** [Task Interruption: Resumption Lag and the Role of Cues](https://interruptions.net/literature/Altmann-CogSci04.pdf). **Publication/update:** 2004. **Publisher:** Proceedings of the Annual Meeting of the Cognitive Science Society, pp. 43–48.

**DOI:** not recorded. **Version/edition:** Published six-page research paper, hosted in an interruption-literature collection. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** Original laboratory experiments.

**Inspected locators:** Printed pp. 44–45: Method and Procedure; p. 46: Results, omnibus tests and Figure 5; pp. 47–48: Discussion. **Supports:** C-04, C-08.

**Limits:** 96 undergraduates, four experiments of 24 each, resource-allocation task and radar interruption. Cue visibility before interruption, not a personalized after-absence recap, was manipulated. Cue benefit was not reliable at shorter lags; the omnibus cue test was marginal. Printed pp. 45–46 were rendered. Experimental seconds are not recommended design thresholds.

**Independence/deduplication:** Independent original experiments, not evidence from multiplayer games or week-long absences. **Rights:** Copyright retained by the publisher/authors; paraphrase only, no media or full source redistributed.

### GDR-SRC-20261010-F06-009

**Julian Frommel and Regan L. Mandryk.** [Daily Quests or Daily Pests? The Benefits and Pitfalls of Engagement Rewards in Games](https://www.researchgate.net/profile/Julian-Frommel-2/publication/365003534_Daily_Quests_or_Daily_Pests_The_Benefits_and_Pitfalls_of_Engagement_Rewards_in_Games/links/63c6a084e922c50e99a1c5f1/Daily-Quests-or-Daily-Pests-The-Benefits-and-Pitfalls-of-Engagement-Rewards-in-Games.pdf). **Publication/update:** 2022-10-25; printed issue October 2022. **Publisher:** Proceedings of the ACM on Human-Computer Interaction 6 (CHI PLAY), Article 226, 23 pages.

**DOI:** 10.1145/3549489. **Version/edition:** Published-paper PDF in first author’s ResearchGate upload; institutional metadata also inspected. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** Original cross-sectional mixed-methods guided-recall survey.

**Inspected locators:** §§3.1–3.4, printed 226:7–8; §4.1, 226:9–11; §4.2 and Tables 2–3, 226:11–12; §5.3, 226:17–18. **Supports:** C-06, C-12, C-14.

**Limits:** 178 filtered respondents aged 19–66, selected for relevant gaming/reward experience; self-reports covering 115 games, not 115 observed builds. “Natural ER interaction” measures completion in general; it is not an exclusive type or randomized treatment. Recall/framing bias, single initial coder and no causal identification. Method page and Tables 2–3 rendered; final limitations screenshot failed but text was readable.

**Independence/deduplication:** Potential overlap with unreviewed F03 source 009 is unresolved: its full reference could not be retrieved. Do not equate those IDs without URL/DOI verification. Cross-batch deduplication pending. **Rights:** Copyright retained by the publisher/authors; paraphrase only, no media or full source redistributed.

**Additional verified route:** [Institutional bibliographic route](https://research-portal.uu.nl/en/publications/daily-quests-or-daily-pests-the-benefits-and-pitfalls-of-engageme/).

### GDR-SRC-20261010-F06-010

**Harry Krueger, Game Director, Housemarque.** [Returnal 2.0 update brings Suspend Cycle and Photo Mode](https://blog.playstation.com/2021/10/26/returnal-2-0-update-brings-suspend-cycle-and-photo-mode). **Publication/update:** 2021-10-26. **Publisher:** PlayStation Blog / Sony Interactive Entertainment.

**DOI:** not recorded. **Version/edition:** Returnal PS5 update 2.0 announcement; historical developer account. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** First-party practitioner design/implementation account.

**Inspected locators:** Suspend Cycle, all four paragraphs. **Supports:** C-02, C-09, C-10.

**Limits:** Single-use suspension and excluded situations are documented, not directly observed in this session. No measured accessibility, retention or preservation-of-challenge result; the developer’s rationale remains reported intent. Current patches and other platforms not verified.

**Independence/deduplication:** One creator account; any summary of the announcement would be derivative. **Rights:** Copyright retained by the publisher/authors; paraphrase only, no media or full source redistributed.

### GDR-SRC-20261010-F01-14

**Microsoft.** [Xbox Accessibility Guidelines: XAG 109 Objective clarity, with framework overview](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/109). **Publication/update:** XAG 109 last updated 2026-03-04; overview 2026-08-14; framework v3.2 published 2023-06-08. **Publisher:** Microsoft Learn.

**DOI:** not recorded. **Version/edition:** Existing F01 source identity retained; live pages re-inspected for F06. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** Vendor accessibility practitioner guidance.

**Inspected locators:** XAG 109 Overview and Implementation guidelines: review objectives/history, optional reminders, suppress unrelated interruptions and revisit tutorials; framework Introduction and Version 3.2 statement. **Supports:** C-05, C-08, C-16.

**Limits:** Not a validated re-entry recipe or retention result. The overview explicitly excludes compliance/legal-checklist use. Embedded game demonstrations were not reproduced; no native-game numerical default imported.

**Independence/deduplication:** Same source identity as the inspected F01 dependency; shares issuer/framework with F02-009 and F06-006. Reinspection is not an independent study. **Rights:** Copyright retained by the publisher/authors; paraphrase only, no media or full source redistributed.

**Additional verified route:** [Framework overview](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines).

### GDR-SRC-20261010-F02-009

**Microsoft.** [Xbox Accessibility Guideline 108: Game difficulty options](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/108). **Publication/update:** last updated 2026-03-04. **Publisher:** Microsoft Learn.

**DOI:** not recorded. **Version/edition:** Existing F02 identity retained; live unnumbered guideline page re-inspected for F06. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** Vendor accessibility practitioner guidance.

**Inspected locators:** Implementation guidelines: regular manual/automatic saving; changing difficulty without progress loss; final pause guidance for single-player, local multiplayer and local split-screen, excluding saving/loading screens. **Supports:** C-03, C-09, C-10, C-16.

**Limits:** Not a formal standard, universal save interval or worldwide compliance statement. Scoped pause advice is not a claim that an online shared world can always pause. Embedded games/media not reproduced.

**Independence/deduplication:** Canonical URL also appears as GDR-SRC-20261010-P01-08 in reviewed P01. Use F02-009 consistently inside F06; central deduplication/redirect decision pending, neither upstream identity retired. **Rights:** Copyright retained by the publisher/authors; paraphrase only, no media or full source redistributed.

### GDR-SRC-20261010-F07-012

**Matti Vuorre, Niklas Johannes, Kristoffer Magnusson and Andrew K. Przybylski.** [Time spent playing video games is unlikely to impact well-being](https://vuorre.com/bibliography/files/3K5WXM3G/vuorre-etal_2022_time-spent-playing-video-games-is-unlike.pdf). **Publication/update:** 2022-07-27. **Publisher:** Royal Society Open Science 9, 220411.

**DOI:** 10.1098/rsos.220411. **Version/edition:** Existing F07 source identity retained; author-hosted published paper re-inspected. **Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Type:** Original longitudinal observational study.

**Inspected locators:** §§2.1–2.3, PDF pp. 2–5; results and attrition discussion, pp. 7–10; §4.1, p. 11. **Supports:** C-07, C-12, C-14.

**Limits:** 38,935 adults across seven games, six-week observation with two-week lags. Small average estimated playtime effects under modeling assumptions do not establish safety of a mechanic, an individual diagnosis or a wellbeing proxy. Selection, attrition and confounding remain. Text inspected; figure/page screenshot attempts failed, no image-derived effect claim.

**Independence/deduplication:** Same underlying work as reviewed F07-012, not new corroboration; independent of the engagement-reward survey, which has a different exposure and outcome. **Rights:** CC BY 4.0; attribution retained, paraphrase only.

## Reviewed dependency transfer

Relevant actual selected bytes were inspected from the cumulative parent-selected archive, Library `libfile_082dcf2646dc8191af243051d202f4a8`, version 1; local ZIP SHA-256 `4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931`. The packet lists precise excerpt ranges. This is scoped transfer from reviewed drafts, not their release or a repetition of their research.

F01's corrected transfer check changes the correct response across affordable/unaffordable/exact cases, distinguishes rule permission from preference and retains needed access supports. F02 distinguishes state correction from deliberate strategic reversal. F07 already owns safe exit and separates behavior from wellbeing. P01's numerical accessibility corrections remain scoped; P02 preserves action meaning, settings recovery and facts without implying equivalent experience. The new brief does not displace those owners.

| Selected archive path / exact identity | Version / candidate revision | SHA-256 |
|---|---|---|
| `selected-drafts/topics/core-loops-and-interaction-structure.md` — `GDR-CAND-20261010-F01-TOP-02` | `0.1.0` / `not recorded in selected file`; draft | `500acfc514461552666c45b91f79e667ee3e0af892d7ad5176682efac635d8a6` |
| `selected-drafts/topics/learning-and-onboarding.md` — `GDR-CAND-20261010-F01-TOP-03` | `0.1.0` / `not recorded in selected file`; draft | `85ab5352a60c2a7e101ee59f53e1afe4fa32834e0420a2619daa27015cdb7598` |
| `selected-drafts/patterns/supported-attempt-and-transfer-check.md` — `GDR-CAND-20261010-F01-PAT-01` | `0.1.0` / `independent-review-correction-1`; draft | `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1` |
| `selected-drafts/topics/decision-design.md` — `GDR-CAND-20261010-F02-TOP-01` | `0.1.0` / `initial-capture-1`; draft | `2fe66a5bf914a9c3f4101e168cdfd344a26eeadbfea7c45d16a9f17cca33bc6c` |
| `selected-drafts/topics/ethical-and-sustainable-design.md` — `GDR-CAND-20261010-F07-TOP-02` | `0.1.0` / `initial-capture-1`; draft | `e26241cb08b1e9ddd4181e7cb92494506ae9b03e04e24032a3e9c79fe0169ce0` |
| `selected-drafts/patterns/legible-commitment-and-safe-exit.md` — `GDR-CAND-20261010-F07-PAT-02` | `0.1.0` / `initial-capture-1`; draft | `85cffbbdb25c968e9c00f8ab5b3a230c420f24f0b83e19fbff49648e217b425a` |
| `selected-drafts/topics/controls-and-input.md` — `GDR-CAND-20261010-P02-TOP-01` | `0.1.0` / `review-correction-1`; draft | `b9235153ba8b742c6df47e9e23844d9ab5da82e4212ebd22f04e314f6ccce21b` |
| `selected-drafts/topics/feedback-and-game-feel.md` — `GDR-CAND-20261010-P02-TOP-02` | `0.1.0` / `review-correction-1`; draft | `6cf571a87946b9b40470cce966862219906f495b50c0b1db04e1ad7677ca4415` |
| `selected-drafts/topics/visual-communication.md` — `GDR-CAND-20261010-P01-TOP-01` | `0.1.0` / `review-correction-1`; draft | `b8e23ae234041fa0893295fdd36457eb08e0e77a60cca4229b7a77f0f13844b7` |

The F03 author packet was partially readable through Files; raw materialization failed and later requested sections returned no readable content. Its queue entry **Absence-tolerant personal reward horizons** remains an unregistered upstream proposal; the reference behind its `009` pointer was not verified. F06's directly inspected Frommel/Mandryk work keeps one F06 source identity pending URL/DOI deduplication, not an invented mapping to the unseen F03 reference. F03's topic/pattern bodies and completed independent-review result were not adopted. F04/F05 remain unreviewed context and were not used. No active relative link pretends those missing bodies are included here.

## Open questions and change history

**Coverage-open:** Saving, checkpoint semantics, interruption, re-entry, session goals, repeat play and respectful engagement received bounded treatment. Missing evidence includes long-absence controlled gameplay comparisons, current multi-platform save/reconnect behavior, consented group interruption studies, children, cross-cultural/timezone constraints, multilingual change summaries, live-economy absence effects and sustainable notification operations. No claimed finding resolves those gaps.

Packet-local cases `F06-CON-04` (re-entry help versus stale/spoiling information), `F06-CON-05` (valued routine versus felt obligation), and `F06-CON-06` (exit flexibility versus shared consequences) remain unresolved. The queue preserves additional research and the F03 ownership overlap; no child key or permanent ID has been allocated.

**History:** 2026-10-11 UTC — initial F06 author submission, `0.1.0 draft`, `initial-draft-1`; predecessor/supersession null. All reviewer/approval fields remain null. The [integrity receipt](../reviews/full-run-20261010-f06-integrity-receipt.md) identifies exact bytes. Next decision: independent review of C-08/C-09/C-12 and whether the state-validation pattern is distinct enough from F01 to keep or should be returned for consolidation. No retention, wellbeing or gameplay benefit has been demonstrated by this batch.

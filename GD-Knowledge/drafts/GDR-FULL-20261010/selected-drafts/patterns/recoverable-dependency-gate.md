---
id: GDR-CAND-20261010-G03-PAT-01
kind: pattern
title: Recoverable dependency gate
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
- dependency recovery audit
- recoverable puzzle gate
tags:
- prerequisites
- state-consistency
- commitment
- recovery
- knowledge-gates
related_topics:
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-W01-TOP-01
related_patterns:
- GDR-CAND-20261010-G03-PAT-02
- GDR-CAND-20261010-F01-PAT-01
related_genres:
- GDR-CAND-20261010-G03-GEN-01
- GDR-CAND-20261010-G03-GEN-02
- GDR-CAND-20261010-G03-GEN-03
source_ids:
- GDR-SRC-20261010-G03-001
- GDR-SRC-20261010-G03-002
- GDR-SRC-20261010-G03-003
- GDR-SRC-20261010-G03-012
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-G03
hash_record: ../reviews/full-run-20261010-g03-review-packet.md#candidate-inventory
---

# Recoverable dependency gate

**Conditional pattern candidate; complete recipe not validated.** This is a genre-neutral authoring and review technique for progression that depends on information, items, actions or authored state. “Recoverable” means preserving the declared progression/recovery contract, not making all consequences reversible.

## Purpose

Expose accidental situations in which a legitimate player state has neither a supported path forward nor the recovery the design promised. Separate those defects from deliberate commitment, failure endings and difficult but inferable gates. The intended benefit is intelligible progress with controlled consequences; no reduction in abandonment or frustration has been measured for this recipe. [C-01]

The pattern does not decide what a genre must promise. It is not an engine state-machine design, an automated verification tool, a universal ban on death, or a guarantee that a mechanically solvable puzzle is understandable. Proposed shared ownership crosses Foundations progression and Worlds quest/state design; Library Coordination must resolve its eventual home before canonical adoption. [C-01; C-09]

## Context and prerequisites

Use when a design has identifiable gates, prerequisites and consequences: access to an area, a conversation outcome, knowledge validation, resource-consuming repair, ability use or another authored transition. The designer must be able to describe supported states and distinguish facts known by the player from flags recorded by the system. [C-02]

Required inputs are a locally declared outcome/commitment policy, the set of consequential prerequisite types, evidence routes relevant to knowledge gates, and a way to specify what happens after interruptions or failed attempts. Runtime code is not required for an initial authoring audit; later technical verification does require an authorized implementation and build. A written audit alone cannot verify actual save behavior. [C-02; C-08]

**Exit before application** when the progression contract is unknown, intentionally changes per run without a defined policy, or cannot be represented at a useful level. Clarify that contract or choose a smaller bounded gate. Do not invent recovery solely to satisfy the pattern. For a deliberately irreversible ending, the relevant review may instead concern informed commitment and accurate signaling. [C-01; C-06]

## Mechanism and evidence

| Proposed causal link | Evidence or reasoning | Support limit |
| --- | --- | --- |
| Explicit prerequisites make dependency conflicts available for inspection. | Gilbert’s dependency-chart account describes prerequisite relations and bottlenecks. [C-02; GDR-SRC-20261010-G03-002] | A practitioner method, not a measured reduction in defects; graph completeness is not established. |
| Recording consumptions, state changes and interruptions can expose ways a prerequisite and its outcome become inconsistent. | Revolution’s studio report supplies a concrete save-related progression failure context. [C-03; GDR-SRC-20261010-G03-012] | G03 did not reproduce the defect or verify the fix. One report does not estimate prevalence. |
| A reachable evidence route can be reviewed separately from a mechanically reachable outcome. | Mobius’s narrative-prototype work and the difference between information and state motivate a separate comprehension check. [C-04; GDR-SRC-20261010-G03-003] | A route that exists does not guarantee a player notices or interprets it. |
| A supported alternate route, re-acquisition, rollback or declared failure ending removes the identified unsupported state. | Logical consequence of correctly specifying and implementing that particular transition. [C-05] | Depends on completeness and correct implementation; not a proven global “no dead ends” guarantee. |
| More intelligible recovery improves the intended experience without trivializing commitment. | The pattern’s predicted player-facing benefit. [C-06] | **Hypothesis, low confidence.** It can remove stakes, encourage unreflective experimentation or contradict an intentional challenge. |

Gilbert’s historical critique supplies a reason to look for unexpected unrecoverable states, not authority to outlaw every one-way consequence. His retrospective qualification remains relevant. The full chain is a synthesis, not an empirical result. [C-06; GDR-SRC-20261010-G03-001]

## Recipe

1. **Name the gate and contract.** Write the player-facing question, accepted outcome and intentional consequences. Specify whether the gate tests knowledge, possession, authorization, execution or a combination. State what failure is allowed to mean: retry, changed route, loss, ending, or another explicit outcome. Stop if the team cannot agree on that scope. [C-01; C-02]

2. **Represent the prerequisites without hiding alternatives.** Distinguish conditions that must all hold from alternative sufficient routes. Include items, abilities, resource availability, conversation commitments and event states. Record whether a correct answer is accepted independently of the route used to learn it. Do not add a hidden “saw the intended clue” condition unless it has a defensible purpose. [C-02; C-04]

3. **Add the player’s evidence route.** For each nonobvious prerequisite, write what information could justify trying the action and how it can be encountered in supported modes. Name plausible alternate interpretations and the evidence that distinguishes them. If the inference depends on author-only knowledge, revise the evidence, accept an alternative, or change the gate’s purpose. This is an authoring check, not a passed comprehension test. [C-04]

4. **Mark irreversible or interrupted transitions.** Identify consumption, discards, one-way travel, dialogue commitments, character switches and moments at which a save or quit can occur. Record the intended resulting state, including both the prerequisite and its consequence. Do not assume that animation completion, inventory mutation and checkpoint persistence are the same event. [C-03; C-05]

5. **Choose the smallest appropriate recovery or consequence.** Options include keeping an item until success is confirmed, enabling re-acquisition, accepting a different solution, restoring a consistent checkpoint, explicitly ending a failed attempt, or preserving an informed irreversible consequence. Compare costs and the intended stakes. Automatic unlimited recovery is only one possible policy. [C-05; C-06]

6. **Specify negative-state cases.** For each consequential transition, describe normal entry, alternate order, invalid action, repeated action, interrupted action and return after saving where applicable. Ask whether each supported resulting state retains a legitimate outcome or declared recovery. Static enumeration is not exhaustive verification of an unbounded system. [C-05; C-08]

7. **Review inference and recovery separately.** A future authorized technical check evaluates state consistency. A separately authorized player study evaluates whether information, rejection and consequences are intelligible. Maintain access accommodations in both where relevant. Do not report a passed technical case as evidence that the puzzle is fair or satisfying. [C-04; C-08]

8. **Retain, narrow or remove.** Retain the pattern only where it exposes actionable risks and preserves the intended commitment. Narrow it to a particular gate if global modeling costs more than it clarifies. Remove a recovery intervention when it erases a deliberately chosen consequence; revise the signaling or gate instead. Unresolved high-impact states return to the design owner, not to a release claim. [C-06; C-09]

### Adjustable variables

| Variable | Choices to make locally | Why it changes the application |
| --- | --- | --- |
| Gate meaning | Knowledge, possession, permission, execution, resource or mixed requirement | Determines whether an alternative inference or route should be accepted. |
| Consequence policy | Retry, re-acquisition, rollback, persistent loss, branch or ending | “Recoverable” must not silently overwrite the intended stakes. |
| Evidence explicitness | Direct explanation, inferable relationship, optional clarification | More explanation may increase access while removing intended discovery. |
| Supported solution set | One justified method, several known methods, bounded systemic outcomes | Broader outcomes increase the state combinations requiring review. |
| Audit granularity | Single transition, puzzle, chapter or larger dependency group | Fine detail costs authoring effort; broad abstractions can conceal interactions. |
| Interruptions | Saves, quits, disconnects, character changes or other supported interruptions | Only applicable contexts should be modeled; no multiplayer behavior is assumed. |
| Help relationship | None, recap, requested hint, alternate mode or explicit solution | Help can address inference but cannot repair inconsistent saved state by itself. |

No universal branch count, retry duration, inventory size or acceptable failure rate is specified. [C-05; C-06]

## Worked example — illustrative, not observed

**A floodgate with two access routes.** The proposed outcome is opening a public footpath. One route uses a repair seal and pump; another routes the water through a functioning side channel. The player can infer both from an inspection record and physical markings. The gate’s meaning is an outcome, not demonstration of one tool. This scene is invented. [C-07]

The first authoring pass consumes the seal when repair begins, opens the path when an animation ends, and permits saving in between. A proposed negative case asks what a restored save should mean at that point. If it means “seal absent, repair incomplete, no alternate route,” the specification contains a potential unsupported state. This is a paper-analysis result for the invented specification, not an observed software defect. [C-05; C-07]

The author can propose several different fixes: commit consumption and outcome together in the eventual technical design; restore the seal on an interrupted attempt; preserve the side-channel solution; or disallow that particular intermediate save while providing appropriate interruption handling. The pattern does not choose a runtime architecture or authorize its implementation. The selected approach must fit the intended persistence contract. [C-05; C-07]

Now consider a player who uses the side channel before seeing the repair note. Because the gate tests an outcome, rejecting that route merely for missing the note would contradict the contract. In a different scene where an inspector requires a signed repair certificate, documentation could be a legitimate additional prerequisite—but it should be represented as authorization, not an incorrect physical solution. [C-02; C-04; C-07]

**Contrary example:** in a declared one-attempt expedition, spending the last seal on a risky side task may intentionally close the safer route. Replenishing the seal automatically would change the resource challenge. Audit the consequence and the information available at commitment; do not erase it solely because the graph now lacks the original route. [C-06; C-07]

## Tradeoffs and alternatives

A dependency audit can be performed before implementation, but it adds maintenance: revisions to items, conversations or route structure can invalidate prior reasoning. It can also create false confidence if a tidy diagram omits a state or treats player interpretation as a Boolean flag. Use explicit uncertainty rather than exhaustive-looking filler. [C-02; C-04; C-09]

Simpler alternatives include removing an unnecessary prerequisite, using one reversible interaction, giving an explicit authorization requirement, or limiting the scene to fewer supported states. More elaborate alternatives include bounded systemic solutions or deliberate failure branches. These choices should follow the player promise and production capacity, not the visual complexity of a chart. [C-05; C-06]

A separate hint system may help a player understand a valid path but cannot prove that a path exists in their current save. Conversely, automatic recovery does not make an arbitrary inference coherent. Keep these problems separate even when both patterns apply to one puzzle. [C-04; C-05]

## Failure cases and warning signs

| Failure | Observable warning in a future review/test | Correction to consider |
| --- | --- | --- |
| Graph reachability mistaken for comprehension | Reviewers can traverse the chart, but participants cannot explain why an action follows from the evidence. | Rework the evidence or gate meaning; do not merely add more arrows. |
| Incomplete recovery contract | An item is gone but neither its outcome nor an intentional consequence is represented. | Clarify the state transition and recovery policy before implementation. |
| Hidden author-order requirement | A valid alternative solution is rejected solely because a particular prior interaction was skipped. | Remove the flag or explain the actual authorization requirement. |
| Recovery removes a chosen challenge | Participants treat previously consequential commitments as cost-free enumeration, against the declared mode. | Preserve informed consequence or separate modes; do not claim all recovery is an improvement. |
| Model drifts from content | A new dialogue, patch or item change invalidates an old audit. | Reopen the affected cases and record the changed dependency. |
| Repair becomes a spoiler | Automatic assistance reveals the unknown dependency rather than correcting an invalid state. | Separate technical recovery from optional information disclosure. |

These are proposed diagnostic signs, not measured failure frequencies. [C-04–C-06; C-08]

## Do not use conditions

Do not apply this as an automatic rule against roguelike loss, branching tragedy, deliberate resource commitment or an explicitly replayable failure ending. Do not represent every inaccessible scene as a bug if exclusion is a coherent consequence of an informed decision. Do not claim complete safety for unbounded systemic interactions or use a paper graph in place of build-specific validation. Do not add recovery that creates an exploit or invalidates shared-world consequences without examining that context. These are conditional limits, not researched guidance for those other genres or network architectures. [C-06; C-09]

## Proposed playtest and verification plan — NOT PERFORMED

**Question:** when an authored gate is otherwise unchanged, does an explicit recovery/commitment specification reduce unintended stranding while preserving comprehension and the intended stakes? [C-08]

A future technical review would exercise identified transitions and interrupted states on an authorized build, reporting exact version, initial state, action sequence, expected result and observed result. A future player study would compare suitable recoverable alternatives, not knowingly strand participants in an inaccessible or harmful baseline. Ask separately about intended action, understanding, perceived consequence, recovery discoverability and desired challenge. [C-08]

Use relevant puzzle and system familiarity, input/access needs, interruption patterns and language contexts to select participants. Prior knowledge of the dependency graph, solution spoilers, repeated exposure and different recovery presentation are confounds. If assessing a taught rule, retain the F01 correction: use different correct predictions across transfer cases and distinguish prediction from a chosen action. Do not fade accommodations. [C-08; C-09]

**Reject or revise** when a supported case has no declared outcome/recovery, when evidence still does not justify the action, when recovery repeatedly obscures consequences, or when a simpler gate delivers the same intended experience with fewer state risks. A clean technical check supports only the states actually exercised; player benefit requires separate evidence. Local acceptance criteria must be chosen before results, without a universal percentage or sample guarantee. [C-08]

## Claim ledger

| ID | Claim | Class | Support and locator | Confidence and causal limit |
| --- | --- | --- | --- | --- |
| C-01 | The pattern aims to distinguish accidental unsupported progression states from intended commitments. | hypothesis | Synthesis from 001 qualified historical critique and 002 dependency method. | Low for full-pattern benefit; useful scope definition, not proven audience preference. |
| C-02 | Explicit prerequisite representations can support reasoning about alternatives and bottlenecks. | practitioner-heuristic | 002, definition and worked-text dependency discussion. | High attribution; no measured defect reduction or completeness guarantee. |
| C-03 | A studio reported a save-related progression defect in Broken Sword Reforged. | observed-example | 012, Update #1, (Can’t) Open Sesame; documentation inspected, not gameplay. | High for the report; G03 did not reproduce or verify repair. |
| C-04 | Mechanical reachability and interpretable evidence routes need separate review. | inference | 003 narrative-prototype account; inspected P01/W01 information/state distinctions. | Moderate conceptual basis; comprehension effects untested. |
| C-05 | A correctly specified and implemented alternative/recovery can remove the particular unsupported state it covers. | inference | Logical conditional, motivated by C-02/C-03; no claim of implemented correctness. | High as conditional logic, low for completeness in an actual game. |
| C-06 | Recovery may improve intelligibility but can harm intentional stakes or discovery. | hypothesis | 001’s qualified advice; explicit counterexamples and tradeoffs. | Low until tested for the selected promise and population. |
| C-07 | The floodgate example demonstrates how to apply the recipe to a hypothetical gate. | hypothesis | Synthetic example created in G03. | Low predicted-effect confidence; no game/test result. |
| C-08 | Separate technical state checks and player studies could falsify the proposed benefits. | hypothesis | Proposed validation plan; inspected F01 corrected transfer method. | Low until authorized execution; no observed results. |
| C-09 | Adoption requires unresolved shared ownership/dependencies and cannot be inferred from a completed draft. | inference | Supplied G03 brief, actual shared-candidate inspection and review-gate snapshot. | High for workflow state; no canonical allocation or adoption. |

Source suffixes expand to `GDR-SRC-20261010-G03-<nnn>`. Related local conflicts: `G03-CON-02`, `G03-CON-06`. Public sources support individual rationale links, not the complete causal chain.

## References

Access date for every record below: **2026-10-10, America/Los_Angeles**. Web-text line numbers identify this inspected retrieval; headings and named paragraphs are the portable locators. A source identity is temporary, reused within G03; cross-batch canonical URL/DOI/edition deduplication remains pending.

### GDR-SRC-20261010-G03-001

**Ron Gilbert. [Why Adventure Games Suck / Why Adventure Games Suck And What We Can Do About It](https://grumpygamer.com/why_adventure_games_suck/).** Grumpy Gamer (author site). Date: 1989 original essay; 2004-05-12 republication and retrospective preface.

**Edition/context:** 1989 essay in its 2004 web wrapper; accessed page has a 2026 site footer. **Access:** `full`. **Type:** Firsthand designer essay; practitioner heuristics.

**Inspected locator:** Preface, especially the paragraph beginning “As I read this”; sections “Live and learn,” “I forgot to pick it up,” “Arbitrary puzzles,” “Reward Intent,” and “Give the player options.” Inspected web-text lines 21–26, 53–63, 74–90.

**Support in this artifact:** C-01/C-06 rationale; qualified historical advice, not a universal no-failure rule.

**Limits:** Historical viewpoint, not an audience survey or causal experiment. The retrospective preface explicitly qualifies the older advice. No numerical rule or blanket rejection of failure/linearity is adopted. **Independence:** Same author/design tradition as sources 002, 007 and 009; not four independent replications.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-002

**Ron Gilbert. [Puzzle Dependency Charts](https://grumpygamer.com/puzzle_dependency_charts/).** Grumpy Gamer (author site). Date: 2014-08-10.

**Edition/context:** Dated web essay; text inspected, diagrams and linked large chart not visually inspected. **Access:** `relevant-excerpt`. **Type:** Firsthand design-process account.

**Inspected locator:** Opening account of Maniac Mansion/Monkey Island; definition of dependency chart; worked-text distinction between unlocking/oiling/opening; linearity/choice and act bottlenecks. Web-text lines 19–23, 28–53, 60–63.

**Support in this artifact:** C-02 practitioner method and framing.

**Limits:** Retrospective attribution, no comparative production measurements. Diagram details not independently observed. Its suggested branch counts are not library targets. **Independence:** Same author as 001, 007 and 009. The essay itself distinguishes surviving notebook material from an unavailable original Monkey Island chart.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-003

**Alex Beachum (signed “Alex” in the article), Mobius Digital. [Demaking Outer Wilds](https://www.mobiusdigitalgames.com/news/demaking-outer-wilds).** Mobius Digital. Date: 2015-07-30.

**Edition/context:** Pre-release paper and Processing narrative prototypes, not the final game. **Access:** `relevant-excerpt`. **Type:** Firsthand development and formative-playtest account.

**Inspected locator:** “Archaeology In Space”; “It’s Only A Model”; “From Paper to Processing.” Web-text lines 21–37.

**Support in this artifact:** C-04 rationale for separately investigating clue comprehension.

**Limits:** Reported observations lack sample size, controls and effect estimates. Prototypes abstracted travel; no G03 game or prototype observation. Narrative concentration is a reported problem, not a universal pacing interval. **Independence:** Same studio/project and creative director as 004; one production context, not replication.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

### GDR-SRC-20261010-G03-012

**Revolution Software (studio-signed update posts). [Broken Sword – Shadow of the Templars: Reforged: Update #1 and Update #2](https://steamcommunity.com/app/2544110/allnews/).** Official Steam community news for app 2544110. Date: Update #1: 2024-10-02; Update #2: 2024-10-11.

**Edition/context:** Two dated update excerpts within a mutable news collection; Steam/Steam Deck context; exact binary versions unknown. **Access:** `relevant-excerpt`. **Type:** Firsthand patch/failure documentation.

**Inspected locator:** Update #1 “(Can’t) Open Sesame” and “STEAM DECK,” web-text lines 580–604, 695–704; Update #2 “UI” and “STEAM DECK,” lines 489–491, 535–560.

**Support in this artifact:** C-03 documented failure; no reproduced game state.

**Limits:** Reported bugs and fixes are not reproduced by G03; no claim all saves/devices are fixed. Collection is not a permanent per-post URL; datelines and exact section headings distinguish the excerpts. **Independence:** One studio/product across both posts; same product as inaccessible lead 015, not independent corroboration.

**Rights:** Copyright remains with the author/publisher; short paraphrases only. No screenshots, diagrams, source code or substantial source text redistributed.

## Inspected shared-candidate provenance

Source container: **GD-Knowledge-first-wave-reviewed-drafts-2026-10-10.zip**, Library `libfile_6852a9bc35108191bdcf23bd487e3b42`; actual bytes retrieved in G03 and SHA-256 matched to parent receipt: `e959c8d4eda2ba2a5f1994a37e0fa613d11f3fe0c5dd0608cf12a8fad87883ef`. Root is `GD-Knowledge-first-wave-reviewed-drafts-2026-10-10/`. The following are inspected **excerpts of selected drafts**, not re-verification of their entire public bibliographies. All remain version **0.1.0**, status **draft**, null approval metadata. They are not resent with G03.

**GDR-CAND-20261010-F01-PAT-01** — `selected-drafts/patterns/supported-attempt-and-transfer-check.md`; revision `independent-review-correction-1`; SHA-256 `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1`. Locator: Purpose, prerequisites, mechanism, recipe and corrected transfer probes, inspected lines 49–118; correction.diff.md lines 18–43.

**GDR-CAND-20261010-P01-TOP-02** — `selected-drafts/topics/interface-and-information.md`; revision `review-correction-1`; SHA-256 `1381faf6c998295cd0b0472cf3905a28f87d9515d16bacb54ece423fe080595d`. Locator: “Working definitions” and “Task-information contract,” inspected lines 63–81.

**GDR-CAND-20261010-P01-TOP-03** — `selected-drafts/topics/accessibility-and-inclusive-interaction.md`; revision `review-correction-1`; SHA-256 `eab6276ce51dcea359cb599f24ffef603b6062a6d6f6badffa8c0e28a0e79d48`. Locator: Definition/access chain and proposed evaluation, inspected lines 54–87 and 193–221; corrections/P01/CORRECTION_RECEIPT.md lines 3–21.

**GDR-CAND-20261010-W01-TOP-01** — `selected-drafts/topics/narrative-structures.md`; revision `initial`; SHA-256 `9bac355072317ed9db0c299d926d293cd70052426ceb8db9cae98beaee1d15c7`. Locator: Decision, vocabulary, promise/action/persistence/interpretation and discovered order, inspected lines 57–100.

The parent-selected correction receipts govern which draft was inspected; they do not make its hypotheses accepted evidence. External dependency file paths are recorded as text because the files are not in this delivery. The [G03 packet](../reviews/full-run-20261010-g03-review-packet.md#dependency-register) holds unresolved links and proposed integration ownership.

## Related entries and history

Conditional applications: [Action adventure](../genres/action-adventure.md), [Adventure](../genres/adventure.md), [Point-and-click adventure](../genres/point-and-click-adventure.md). Complement: [Player-requested state-aware hints](player-requested-state-aware-hints.md). Their IDs are recorded in front matter; none is released.

Proposed owner reconciliation: Foundations F03 Progression and rewards and Worlds W02 Quests and objectives / narrative-state interfaces, with P01 information/access constraints. Those missing downstream files are not replaced by this pattern. Existing first-wave patterns require a concept-overlap check before canonical placement; no new permanent ID is allocated.

Initial capture `initial-capture-1`, version `0.1.0`, draft; predecessor/supersession null. Author self-review challenges the assumption that more recovery is better and the leap from chart validity to comprehensibility. Independent G03 review, actual playtests, host retrieval tests and release are not performed. The [packet](../reviews/full-run-20261010-g03-review-packet.md) holds byte identity and the next decision.

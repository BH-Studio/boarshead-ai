---
id: GDR-CAND-20261010-W02-TOP-02
kind: topic
title: Quests and objectives
version: 0.1.0
status: draft
candidate_revision: initial-draft-1
run_id: GDR-FULL-20261010
batch_id: W02
attempt_id: W02-authoring-attempt-1
owner_project: BH-GDR-Worlds-and-Characters
updated: '2026-10-10'
evidence_checked: '2026-10-10'
input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate + supplied W02 dispatch, 2026-10-10
aliases:
- quest design
- mission objectives
- alternate solutions
- quest tracking
- quest resolution
tags:
- motivation
- dependencies
- discovery
- alternatives
- tracking
- resolution
- procedural-content
related_topics:
- GDR-CAND-20261010-W02-TOP-01
- GDR-CAND-20261010-W02-TOP-03
related_patterns:
- GDR-CAND-20261010-W02-PAT-01
- GDR-CAND-20261010-W02-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-W02-009
- GDR-SRC-20261010-W02-011
- GDR-SRC-20261010-W02-012
- GDR-SRC-20261010-W02-013
- GDR-SRC-20261010-W02-014
- GDR-SRC-20261010-W02-015
- GDR-SRC-20261010-W02-017
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-W02
predecessor_hash: null
supersedes: null
change_summary: Initial W02 submission; no earlier batch artifacts reproduced or replaced.
byte_hash_record: ../reviews/full-run-20261010-w02-review-packet.md#artifact-byte-manifest
---

# Quests and objectives

**Draft research candidate — not released guidance.** Candidate identity is run-scoped, not a permanent GDK allocation. No W02 independent review, gameplay prototype or player test has occurred.

## Decision and scope

**Decision:** How should a player discover a goal, understand why it matters, choose among supported ways to pursue it, and recognize a valid resolution? This entry covers motivations, dependencies, discovery, alternate solutions, tracking and closure. It compares authored, assembled and systemic quest approaches without prescribing runtime ownership or implementation.

Working definitions: an **objective** names a desired outcome or required action; a **quest** connects a goal to a motivating context and possible progression/resolution; a **route** is a supported way of reaching or failing that objective. **Authored** here means deliberately specified content; **systemic** means opportunities or responses arise from interacting rules; **procedurally assembled** means some content is selected or composed by a process. Those dimensions can coexist. They are not interchangeable promises of freedom or quality. [C-01]

Keep separate the **requester’s motive**, **the protagonist’s reason to act**, **the player’s incentive**, and **the completion criterion**. “The town needs clean water,” “I owe the engineer a favor,” “I want access to the new area,” and “a usable supply is restored” describe different design obligations. Their alignment is a proposed diagnostic, not a claim that every player shares an NPC’s motive. [C-06]

This topic does not define numerical reward schedules, faction simulation, universal quest taxonomies or a game’s moral/canonical outcomes. Foundations progression, economy, procedural-content and evaluation references are unavailable shared dependencies. Reviewed W01 narrative/world/character content is reported by the parent but its bytes were not inspected here.

## Core explanation and mechanisms

### Structural validity does not demonstrate a worthwhile quest

Doran and Parberry analyzed 753 quest descriptions from community databases covering four MMORPGs. Their categories concern inferred NPC motivations and action structures, not measured player motivations. Their prototype account discusses state-sensitive generation, and their conclusion explicitly leaves equality with handcrafted quality unestablished. This corpus is narrow and historical, not 753 player tests or a universal genre-neutral taxonomy. [C-02; GDR-SRC-20261010-W02-012]

The bridge is to distinguish a **feasible route** from an **interesting decision**. A route can be reachable yet tedious, and two descriptions can resolve to the same repeated activity. Audit what the player actually does, knows and gives up rather than counting names, destinations or generated strings as meaningful variation. This inference is deliberately stricter than equating combinatorial output with experience quality. [C-08, C-10]

### A shared goal can accommodate different methods without erasing their meaning

Witsel’s first-person account describes iterating a complete quest path before expanding alternatives within production constraints. It is a practitioner account of an in-development Skyrim mod, not evidence that every quest needs one objective or that a particular branch layout is best. [C-03; GDR-SRC-20261010-W02-011]

A different primary production account, Larian’s Early Access Patch 3 announcement, describes experience awards for non-combat resolutions and changes to dialogue checks. It shows that supported methods and reward recognition can be adjusted together; it does not establish balanced rewards or improved enjoyment. [C-04; GDR-SRC-20261010-W02-013]

**Proposed mechanism:** name the accepted outcome, identify the methods the fiction and game actually support, and retain their distinct conditions and aftermath. This can expose a quest that says “secure the supplies” while recognizing only a stolen item. It cannot prove that all methods should be equivalent, rewarded equally, or accepted by every requester. A vow not to steal may make acquisition by theft an intentional breach, even when the supplies arrive. [C-07]

### Discovery, understanding and permission to advance are different

Inkle’s explanation of *Heaven’s Vault* distinguishes artifact discovery/provenance from successful translation as the route to new sites. This is a creator-reported counterexample to making correct interpretation a necessary progression gate in every lore-rich design. It is not a rule against knowledge-gated objectives. [C-05; GDR-SRC-20261010-W02-015]

The application question is whether the player must **find evidence**, **interpret it**, **accept a commitment**, or **perform a validated action**. Confusing these can produce either a spoiler or an impossible objective: a tracker may declare the interpretation correct before the player has worked it out, or refuse progress after the explicitly requested outcome has already occurred. The proposed objective contract makes that choice explicit. [C-07, C-09]

### Refusal and failure require a declared role in the experience

Short’s practitioner discussion of non-choice suggests beginning after a necessary commitment rather than always presenting a fictitious opt-out. That is an authored-premise technique, not proof that refusal is unimportant. [C-11; GDR-SRC-20261010-W02-014]

Our proposed distinction is between **not accepting**, **abandoning an accepted attempt**, **failing while continuing the story**, and **being unable to continue because content is broken**. A game can intentionally deny the first or make the third terminal, but its presentation should not confuse these with an implementation accident or a recoverable branch. A retry, alternative, explicit ending or acknowledged refusal is a design choice to document, not a universally mandatory “fail forward” rule. [C-12]

## Design choices and alternatives

| Choice | Conditions for use | Tradeoff and alternative |
|---|---|---|
| Outcome objective versus required method | Name the outcome when several methods are legitimately supported. Name the method when it is itself the task, training target, vow or narrative commitment. | Over-broad outcomes falsely promise systemic freedom; overly narrow verbs invalidate legitimate solutions. Offer fewer honestly supported routes rather than unverifiable freedom. [C-07] |
| Explicit quest offer versus discovered opportunity | An offer can establish consent, stakes and authority. Discovery can let the player infer a need before accepting responsibility. | Proximity to a clue should not silently become a personal promise unless that convention is deliberately established. A provisional note can record a lead without declaring acceptance. [C-06, C-12] |
| Authored sequence versus assembled modules | Authored sequences suit specific causal/character changes; modules suit revisitable situations with comprehensible constraints. | Modularity can repeat the same action under new nouns. A small authored set or an unformalized systemic opportunity may serve better. [C-10] |
| Exact navigation versus an area, clue or requestable hint | Use support that supplies the information required for the intended task and access needs. | An exact destination can solve a location puzzle; vague directions can be unusable. Separate access to information from the decision the player is meant to make. [C-09, C-13] |
| Open alternatives versus meaningful exclusivity | Keep routes open when the fiction permits them; close one when an informed commitment changes the situation. | Unannounced exclusivity can feel arbitrary. Explain the relevant constraint rather than exposing every future branch. [C-07, C-12] |
| Repeatable task versus finite resolution | Repetition can provide an ongoing role; finite closure can preserve a specific consequence. | Reopening the same emergency without explanation can undermine the previous resolution. A maintenance task or a newly attributed need may be a better fit than resetting the fiction. [C-10, C-12] |

Do not infer a player’s preference from completion rate alone: the route may be easiest to discover, the only one rewarded, or the only one that the tracker accepts. This is a causal alternative to examine, not a result measured in this batch. [C-15]

## Application process

1. **Diagnose the purpose and authority.** State who needs what, why the player may care, who can accept a result and what happens when the player declines. Specify whether the premise is already fixed. An author’s unapproved story idea is not a project’s accepted quest outcome. [C-06, C-11, C-12]
2. **Write the completion contract.** Describe the outcome in player-understandable terms, whether particular means are required or prohibited, and what evidence establishes completion. Separate the world outcome, the requester’s judgment, the journal’s wording and reward eligibility. Those are conceptual distinctions, not four required runtime components. [C-07]
3. **Trace prerequisites and discovery.** For every route, ask what must exist, what the player must know, what access is needed, and what can invalidate it. Distinguish alternatives from prerequisites that all apply. Review circular prerequisites, missing actors, consumed evidence, pre-completed objectives and out-of-order discovery. [C-08]
4. **Compare routes by actual decisions.** List actions, knowledge, costs, risks, time sensitivity and aftermath. Two different speech buttons that both purchase the same key are not automatically two different methods. A genuinely different method need not have a different ending if its relevant cost or relationship effect remains recognized. [C-07, C-10]
5. **Design the first understandable end-to-end version.** A local paper walkthrough can expose gaps before expanding content. Include failure and refusal in the comparison rather than demonstrating only success. This is a proposed authoring exercise; no game prototype or player test was executed in W02. [C-03, C-08, C-15]
6. **Specify tracking and recovery.** State what the player can revisit: current goal, known reason, discovered evidence, outstanding obstacle, meaningful commitment and available request for help. Do not require remembering an unrepeatable voice line. A recap may omit secrets and still restore the action-relevant facts. [C-09, C-13]
7. **Evaluate, revise and stop.** Test whether players recognize supported methods and why a result was accepted or rejected. Review incentives separately with Foundations. Stop adding routes when their distinctions cannot be communicated or their downstream costs cannot be honored; keep the smaller valid design rather than labeling unimplemented possibilities as solutions. [C-07, C-14, C-15]

## Patterns and genre adaptations

[Multi-route objective contract](../patterns/multi-route-objective-contract.md), `GDR-CAND-20261010-W02-PAT-02`, is the bounded reusable recipe for accepted outcomes, method-specific constraints and closure. Its expected comprehension and recognition benefits remain hypotheses.

[Intent and response contract](../patterns/intent-and-response-contract.md), `GDR-CAND-20261010-W02-PAT-01`, applies where accepting, negotiating or refusing an objective is expressed in conversation. Dialogue wording must not turn inquiry into acceptance without the intended commitment being clear.

Genre adaptation depends on variables rather than a winning label: whether solving the dependency is the challenge, whether repetition is part of the promised role, whether the protagonist can reasonably refuse, and whether alternate means must preserve a moral or procedural constraint. The inspected MMORPG corpus cannot become a neutral taxonomy for all quests. No genre guidance file or reviewed shared genre content is included in this submission.

## Examples and counterexamples

### Illustrative worked comparison: restore a reliable water supply

This invented example is not approved canon. A settlement’s pump is broken. The proposed objective is **“Restore a reliable water supply to the settlement.”** The requester also asks that the downstream irrigation channel remain usable. These statements should not be collapsed: reliability is the primary outcome, while downstream damage may be a prohibited method or a disputed consequence that needs a separate response. The local design must choose which. [C-06, C-07; illustrative]

| Route | Preconditions and player discovery | Distinct cost and recognition |
|---|---|---|
| Repair the pump | Inspect the failure; obtain suitable parts or demonstrate an already available substitute. | Uses parts and labor. The outcome is repaired infrastructure; possession of a repair receipt alone is insufficient. |
| Arrange a temporary delivery | Discover a supplier and secure an agreement the settlement can sustain. | Creates an ongoing obligation. It may count as temporary relief but not “reliable supply” unless the agreed criterion includes it. |
| Divert the channel | Learn the channel’s function and available control point. | May restore water while harming another use. Whether this is rejected, accepted with a consequence, or forbidden must be stated rather than silently erased. |

The contract might resolve the second route as **temporary relief achieved; permanent restoration unresolved**. That is not a failure merely because it is not full completion. The player should understand what changed and why work remains. Alternatively, simplify the objective to temporary relief from the beginning, reducing the need for a composite status. [C-07, C-12; illustrative]

A discovery test includes a player who already carries compatible parts, a player who meets the supplier before hearing the request, and a player returning after an absence. “Talk to the engineer” may be optional clarification rather than a hidden mandatory step. When it truly is required authorization, the presentation should say why. [C-08, C-09; illustrative]

### Counterexample: the method is the objective

In an illustrative supervised repair assessment, safely isolating power is part of what is being evaluated. Supplying water by another route does not satisfy that training objective. Calling every successful water delivery an equivalent solution would destroy the assessment. The stronger contract is **“Demonstrate safe pump isolation and repair”**, with the rationale made clear. An outcome-first approach must preserve such method requirements rather than automatically generalizing them away. [C-07; illustrative]

### Contrary production and evidence checks

The inspected Larian patch is a historical report about what was recognized, not proof that every game must reward peaceful and violent methods equally. Witsel’s constrained workflow is a production option, not a ban on open-ended goals. Doran and Parberry’s generator output is a feasibility illustration; neither its corpus size nor substitution of names demonstrates meaningful variety. Those limits remain active counterweights to the synthesis. [C-02, C-03, C-04, C-10]

## Failure modes and constraints

**Opaque dependencies.** An actor disappears, a clue is consumed, or an action is completed early and the quest no longer makes sense. The proposed repair is to decide whether the new state is a supported solution, a recoverable obstacle or an acknowledged ending. A permanently active tracker with no viable action is a warning sign, not evidence that the player failed to understand a deep narrative. [C-08, C-12]

**Recognition and incentives disagree.** A journal praises restraint while the progression system recognizes only combat, or a supposedly equal route is substantially harder to discover. Preserve the difference in the review record; do not declare balance from a matching reward number. Rewards belong in a Foundations coordination discussion, not a new W02 balancing rule. [C-04, C-14]

**Tracking either spoils or excludes.** Naughty Dog’s PS4-era accessibility documentation describes distinct story-navigation support, exploration scanning and on-screen text narration. It is an official feature description, not an evaluation of those options for another game. [C-13; GDR-SRC-20261010-W02-017]

The proposed transfer is to provide configurable information access consistent with the intended challenge. An accessible account of a known clue need not reveal its unknown solution. A hint can be requested rather than automatically escalating after an invented universal waiting period. Handle essential spoken directions through recoverable supported presentation; delegate actual UI requirements to Presentation review. [C-09, C-13]

**Localization changes the contract.** “Bring a pump part” and “bring all pump parts” are different tasks. A route assembled from fragments can lose the actor, tense or condition needed to distinguish acceptance from completion. Review complete route states and responses in context, including already-satisfied and failed cases, rather than relying only on isolated string correctness. This is an inference from LQA practice, not a measured benefit of a particular pipeline. [C-14; GDR-SRC-20261010-W02-009]

**Ethical framing and production scope.** The quest giver’s preference need not be the world’s moral truth. A refusal or a locally disfavored solution can be represented without claiming the player is deficient. Writing, recording, localization, testing and continuity implications should be costed locally before adding alternatives. No public source in this batch establishes a safe universal branch count or a time budget. [C-06, C-07, C-14]

## Playtest and validation

**Proposed only; not performed.** No executable quest, authored test build, participant recruitment or gameplay test was produced here.

| Question | Comparison and procedure | Measures and falsification |
|---|---|---|
| Does the objective promise the right freedom? | Compare broad outcome wording, explicit outcome-with-constraints wording and an honest single-method objective. Keep actually supported routes constant where that comparison is appropriate. | Before acting, ask which methods players expect to count and why. Reject broader wording if it increases unsupported expectations or disguises a required method. [C-07, C-15] |
| Are alternatives discoverable and recognized? | Give representative players different starting knowledge, including early completion and out-of-order discovery. Record considered routes before asking leading questions. | Track discovery, attempted routes, explained acceptance/rejection and actual aftermath recognition. Do not count renamed interactions as separate methods. Adapt when completion rises but meaningful choice or comprehension falls. [C-08, C-10, C-15] |
| Is re-entry possible without spoilers? | Compare current-state recap, replayed original offer and no recap after a locally selected interruption. Include supported text/audio access configurations. | Measure time/actions to reconstruct the next step, false beliefs, unnecessary repeated work and unintended solution disclosure. Reject a recap that invents player knowledge or resets a commitment. [C-09, C-15] |
| Are generated and authored routes comparably useful for the intended purpose? | Match representative starting states, task demands and writing quality; review actual action differences rather than output volume. | Assess coherence, repetition, explained motivation, choice quality and production repair effort separately. Treat feasibility as a prerequisite, not a substitute for these outcomes. [C-10, C-15] |
| Does localized wording preserve acceptance and closure? | Walk through acceptance, partial relief, full resolution, refusal and failed prerequisites in each intended locale with relevant expertise. | Reject wording that changes obligations or accepted methods. Preserve deliberate culturally adapted expression when its task meaning is approved locally. [C-14, C-15] |

Participant characteristics should reflect the intended experience, language knowledge, navigation and memory-related access needs, and familiarity with quest conventions. Selection, route salience, reward attractiveness, prior knowledge and prompted think-aloud behavior are confounds to track. Define practical difference margins and recruitment needs before testing; there is no prescribed numeric passing score. Test unfamiliar but structurally comparable objectives to distinguish genuine transfer from recognition of the worked example. [C-15]

## Claim ledger

Claim identifiers are local to this artifact. Confidence describes the stated narrow claim, not proof that the proposed technique improves a game. `inference` and `hypothesis` recommendations are author proposals, not approved studio decisions.

### C-01

**Claim:** Authored, systemic and procedurally assembled are separable working dimensions; none alone establishes freedom, coherence or quality.

**Class:** `inference`. **Support/contradiction:** Analytic framing, not a universally accepted classification.

**Sources and precise locators:** GDR-SRC-20261010-W02-012 — Structural/generation discussion; original operational definitions in this entry.

**Applicability:** Across games; specialized genre definitions need separate review. **Confidence:** moderate for the distinctions, low for any implied comparative benefit. **Unresolved:** Which distinctions matter to the project’s content and player task?

### C-02

**Claim:** The 2011 paper provides structural evidence from 753 database quest descriptions, while leaving handcrafted-quality equivalence unestablished.

**Class:** `empirical-evidence`. **Support/contradiction:** A historical corpus and prototype, not a player-effect trial.

**Sources and precise locators:** GDR-SRC-20261010-W02-012 — p. 2, Structural Analysis/Table 1; pp. 7–8, Conclusion and Further Work.

**Applicability:** Four MMORPGs; inferred NPC motives are not measured player motives. **Confidence:** moderate: corpus account and screenshot inspected, underlying databases not re-audited. **Unresolved:** Broader sampling and comparative quality evaluation.

### C-03

**Claim:** Building and iterating a complete path before expanding alternatives is one reported production approach, not a universal quest structure.

**Class:** `practitioner-heuristic`. **Support/contradiction:** First-person account supports the option; no controlled benefit estimate.

**Sources and precise locators:** GDR-SRC-20261010-W02-011 — First Playable Draft; Further Iterations; Conclusion.

**Applicability:** Then-in-development mod and specific authoring constraints. **Confidence:** moderate for the report, low for comparative efficiency. **Unresolved:** When does a small path prototype hide critical systemic interactions?

### C-04

**Claim:** The Early Access Patch 3 announcement documents a change in recognition/rewards for non-combat outcomes, not proof of universal reward parity.

**Class:** `practitioner-heuristic`. **Support/contradiction:** Historical developer report; no current-build or efficacy claim.

**Sources and precise locators:** GDR-SRC-20261010-W02-013 — Original post 740727, opening reward and dialogue-check passages.

**Applicability:** Baldur’s Gate 3 Early Access, December 2020. **Confidence:** moderate for the reported change. **Unresolved:** How do the actual local incentives affect which solutions players attempt?

### C-05

**Claim:** The Heaven’s Vault creator account separates discovery/provenance-based access from translation correctness, limiting a universal lore-comprehension gate rule.

**Class:** `practitioner-heuristic`. **Support/contradiction:** A reported design counterexample, not a comparative experiment.

**Sources and precise locators:** GDR-SRC-20261010-W02-015 — Main explanation of artifact discovery, provenance and translation.

**Applicability:** A specific work with an unknown executable build. **Confidence:** moderate for the account, no general player-effect inference. **Unresolved:** When should understanding itself be the progression task?

### C-06

**Claim:** Separate requester motive, protagonist reason, player incentive and completion criterion to expose mismatched quest promises.

**Class:** `inference`. **Support/contradiction:** Proposed diagnostic, not a validated model of player motivation.

**Sources and precise locators:** GDR-SRC-20261010-W02-012, GDR-SRC-20261010-W02-014 — NPC-motivation model; fixed-premise discussion; original application distinction.

**Applicability:** Not every objective needs a requester or an explicit reward. **Confidence:** moderate for analytical usefulness; low for measured effect. **Unresolved:** Does the separation reveal relevant conflicts without unnecessary paperwork?

### C-07

**Claim:** An outcome contract with explicit method constraints and retained aftermath may recognize legitimate alternatives without treating every method as equivalent.

**Class:** `hypothesis`. **Support/contradiction:** Sources motivate the problem; they do not validate this complete pattern.

**Sources and precise locators:** GDR-SRC-20261010-W02-011, GDR-SRC-20261010-W02-013 — Quest iteration and historical resolution-recognition accounts; recipe is original synthesis.

**Applicability:** Do not erase required methods, vows, training criteria or consequences. **Confidence:** low for player benefit because no contract comparison was performed. **Unresolved:** Does clearer recognition improve understanding without exaggerating available freedom?

### C-08

**Claim:** Audit prerequisite knowledge, access, resources and invalidation separately from whether a route is interesting.

**Class:** `inference`. **Support/contradiction:** State-sensitive feasibility supports the distinction; proposed checklist is not a formal method.

**Sources and precise locators:** GDR-SRC-20261010-W02-012 — Generation/state-constraint discussion, pp. 5–6; quality limit in conclusion.

**Applicability:** Authoring review only; no prescribed runtime representation. **Confidence:** moderate for exposing dependency risks; no measured defect reduction. **Unresolved:** Which out-of-order and already-completed cases actually occur?

### C-09

**Claim:** A current-state account of a known goal, obstacle and commitment may support re-entry better than replaying a stale offer, without revealing unknown solutions.

**Class:** `hypothesis`. **Support/contradiction:** Feature examples motivate possible access routes; recap effectiveness is untested.

**Sources and precise locators:** GDR-SRC-20261010-W02-017 — Navigation and Traversal; Text-to-Speech and Audio Cues; transfer to recap is an inference.

**Applicability:** Depends on intended uncertainty and supported modalities. **Confidence:** low: no direct re-entry comparison inspected. **Unresolved:** Does the recap restore action-relevant context without unwanted knowledge?

### C-10

**Claim:** Compare actual decisions and action sequences, not generated output count or renamed assets, when evaluating quest variation.

**Class:** `inference`. **Support/contradiction:** Separates feasibility and surface variation from experience quality.

**Sources and precise locators:** GDR-SRC-20261010-W02-012, GDR-SRC-20261010-W02-011 — Corpus/prototype quality limitation; production scope and alternative-route discussion.

**Applicability:** Authored, assembled and systemic content; genre scope must remain explicit. **Confidence:** moderate as an evaluation distinction; no universal variety metric. **Unresolved:** Which variations change costs, understanding or expressive decisions for players?

### C-11

**Claim:** A fixed necessary commitment can be established as a premise rather than framed as a falsely open refusal choice.

**Class:** `practitioner-heuristic`. **Support/contradiction:** Conditional practitioner alternative, not a rule excluding refusal.

**Sources and precise locators:** GDR-SRC-20261010-W02-014 — Tricks for the start of the story.

**Applicability:** Authored premise contexts only. **Confidence:** moderate for the advice, low for broad preference prediction. **Unresolved:** Does the intended audience accept the protagonist/premise relationship?

### C-12

**Claim:** Differentiate non-acceptance, abandonment, consequential failure and broken progression, with an explicit local policy for each supported state.

**Class:** `inference`. **Support/contradiction:** Original diagnostic policy; no universal fail-forward requirement.

**Sources and precise locators:** GDR-SRC-20261010-W02-011, GDR-SRC-20261010-W02-014 — Production progression concerns and non-choice framing; distinctions authored here.

**Applicability:** A terminal result can be intentional when honestly framed. **Confidence:** moderate for clarity of specification; low for comparative experience benefit. **Unresolved:** Are state transitions understood and narratively credible?

### C-13

**Claim:** Official accessibility examples offer alternatives for accessing known progression and exploration information, not a universal navigation setting.

**Class:** `practitioner-heuristic`. **Support/contradiction:** First-party feature descriptions; no independent accessibility outcome trial.

**Sources and precise locators:** GDR-SRC-20261010-W02-017 — Navigation and Traversal; Text-to-Speech and Audio Cues.

**Applicability:** PS4 launch-era context, with documented patch annotations. **Confidence:** high for the description, low for transfer effectiveness. **Unresolved:** Which supports preserve this game’s intended task for the actual audience?

### C-14

**Claim:** Review rewards, language, obligations and method-specific aftermath together; matching text length or reward numbers alone does not establish equivalent routes.

**Class:** `inference`. **Support/contradiction:** Proposed cross-domain review; not an approved balancing policy.

**Sources and precise locators:** GDR-SRC-20261010-W02-009, GDR-SRC-20261010-W02-013 — LQA context/source-change concerns; historical reward-recognition change.

**Applicability:** Requires Foundations progression/economy and Presentation/localization decisions. **Confidence:** moderate for identifying dependency risks; low for quantified outcomes. **Unresolved:** Which route differences are intended and which are accidental barriers?

### C-15

**Claim:** The specified expectation, route-discovery, re-entry and localization comparisons are falsifying test proposals, not evidence that this approach works.

**Class:** `hypothesis`. **Support/contradiction:** No test, prototype, participant or local threshold is asserted.

**Sources and precise locators:** Original author proposal; no direct empirical source — Original Playtest and validation section.

**Applicability:** Audience, sampling, precision and acceptable failure costs remain project decisions. **Confidence:** low for comparative benefits pending tests. **Unresolved:** Can benefits survive unfamiliar contexts, access variation and alternative explanations?


## References

Access date for every record below: **2026-10-10**. “Inspected” means the stated text/pages, not an entire linked corpus, game build, video or cited book. Source identities are temporary; cross-batch canonical URL/DOI/edition deduplication remains pending.

### GDR-SRC-20261010-W02-009

**Jennifer O’Donnell, with the named professional contributors acknowledged in the article.** [How to Get the Most from LQA – What It Is and Best Practices](https://igda.org/news-archive/how-to-get-the-most-from-lqa-what-it-is-and-best-practices/). IGDA. Publication/update: 2023-05-31.

**Edition/build:** Dated professional guidance article. **Access:** `relevant-excerpt`. **Source type:** Practitioner guidance.

**Precise locators used:** What is LQA?; What happens during LQA?; discussion of context, characterization, terminology, UI and source changes during testing.

**Claims supported or constrained in this entry:** C-14. **Limits:** Professional recommendations, not a controlled comparison of localization workflows. **Independence:** Shares the IGDA localization practice network with source 010; not an independent player study.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-011

**Nick Witsel.** [An Iterative Approach to Quest Design](https://www.gamedeveloper.com/design/an-iterative-approach-to-quest-design). Game Developer. Publication/update: 2017-03-20.

**Edition/build:** First-person article about then-in-development Lordbound, a Skyrim mod; not a current-build observation. **Access:** `relevant-excerpt`. **Source type:** Firsthand practitioner account.

**Precise locators used:** First Steps; Quest Design and First Playable Draft; Further Iterations; Conclusion. Prose inspected, screenshots not used as gameplay evidence.

**Claims supported or constrained in this entry:** C-03, C-07, C-10, C-12. **Limits:** No usable sample or controlled measurement for the reported player feedback. **Independence:** Independent production context from sources 012 and 013; not an independent player-effect test.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-012

**Jonathon Doran; Ian Parberry.** [A Prototype Quest Generator Based on a Structural Analysis of Quests from Four MMORPGs](https://ianparberry.com/pubs/pcg2011.pdf). ACM, PCGames 2011 workshop. Publication/update: 2011-06-28 conference date.

**Edition/build:** Eight-page proceedings paper; not the separate earlier technical report. **Access:** `relevant-excerpt`. **Source type:** Original structural corpus research and prototype report.

**Precise locators used:** p. 2, Structural Analysis and Table 1 (screenshot inspected); pp. 5–6, generation/constraints; pp. 7–8, Conclusion and Further Work.

**Claims supported or constrained in this entry:** C-01, C-02, C-06, C-08, C-10. **Limits:** Database quest descriptions, not a player-outcome or current-build study. **Independence:** Different from the author’s other quest project summaries; conflicting summary counts were not merged into this edition.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-013

**Larian Studios; official forum post by Jess.** [Community Update #11: Inspiration, Freedom & Pacifism](https://forums.larian.com/ubbthreads.php?Number=740727&ubb=showflat). Larian Studios forums. Publication/update: 2020-12-02 (forum displays 02/12/20).

**Edition/build:** Baldur’s Gate 3 Early Access Patch 3; original announcement post 740727 only. **Access:** `relevant-excerpt`. **Source type:** First-party patch/development account.

**Precise locators used:** Opening patch discussion of experience for avoided combat and dialogue/environmental solutions; following discussion of dialogue checks. Replies excluded.

**Claims supported or constrained in this entry:** C-04, C-07, C-14. **Limits:** A historical stated change, not a measured improvement or a current-release guarantee. **Independence:** Separate studio from sources 011, 016 and 017; still self-reported production evidence.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-014

**Emily Short.** [Mailbag: Moments of Non-Choice](https://emshort.blog/2019/12/10/mailbag-moments-of-non-choice/). Emily Short’s Interactive Storytelling. Publication/update: 2019-12-10.

**Edition/build:** Dated practitioner essay. **Access:** `relevant-excerpt`. **Source type:** Practitioner analysis.

**Precise locators used:** Tricks for the start of the story; Tricks that work later in the story; discussion of fixed premise and character/player distance.

**Claims supported or constrained in this entry:** C-06, C-11, C-12. **Limits:** Advice and discussed examples, not independent observations of the named games here. **Independence:** Same author as sources 003 and 004; not three independent evidence streams.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-015

**inkle.** [How come translation unlocks sites in Heaven’s Vault?](https://medium.com/@inklestudios/why-does-translation-unlock-sites-in-heavens-vault-e05c4ccadf62). inkle on Medium. Publication/update: 2025-11-18.

**Edition/build:** Creator explanation of Heaven’s Vault; exact executable build not supplied. **Access:** `relevant-excerpt`. **Source type:** First-party creator explanation.

**Precise locators used:** Main article body explaining artifact provenance, discovery, translation and interpretation; promotional recommendations excluded.

**Claims supported or constrained in this entry:** C-05. **Limits:** Supports a particular design account, not measured comprehension or a universal lore rule. **Independence:** Independent studio account; no player study or direct gameplay observation was performed here.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-017

**Matthew Dunnerstick / Naughty Dog.** [The Last of Us Part II: Accessibility Features Detailed](https://www.naughtydog.com/blog/the_last_of_us_part_ii_accessibility_features_detailed). Naughty Dog. Publication/update: 2020-06-09; inspected page also contains launch-patch annotations.

**Edition/build:** PS4 launch-era feature description with 1.01/1.02 annotations; not a PS5 Remastered audit. **Access:** `relevant-excerpt`. **Source type:** Official feature documentation.

**Precise locators used:** Navigation and Traversal; Text-to-Speech and Audio Cues; Translation Prompts; Subtitles. Feature-description text inspected, embedded videos not inspected.

**Claims supported or constrained in this entry:** C-09, C-13. **Limits:** Documented options are not evidence that the same configuration works for every player. **Independence:** Separate studio from the other creator accounts; no independent comparative user data supplied.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.


## Open questions and change history

**Coverage checkpoint:** all six assigned subtopics are addressed, but support is uneven. Structural dependencies have a corpus/prototype source; motivations are primarily an analytic distinction plus a limited NPC-motive corpus; discovery and alternatives have creator/practitioner examples; tracking and closure rely substantially on synthesis. None has W02 independent review or local efficacy validation.

**Unresolved/inaccessible:** cooperative ownership and conflicting quest states, live-service resets, refusal costs, content fatigue, culturally varied obligation/authority, generated-language realization and actual progression tuning remain unvalidated. The underlying historical quest databases were not re-inspected. The author’s different web summaries mention different corpus sizes; only the inspected 2011 paper’s Table 1 is used here, with edition reconciliation pending.

**Dependencies:** parent-reviewed W01 narrative/world/character bytes; Foundations progression, economies, systemic behavior, procedural/authored content and evaluation guidance; Presentation interface, localization and accessibility guidance. No unseen source IDs, reviewed recommendations or permanent dependency links were fabricated.

**Conflicts:** local packet labels `methods-versus-outcomes`, `validity-versus-quality`, `guidance-versus-discovery` and `recognition-versus-incentives`; see the [review packet](../reviews/full-run-20261010-w02-review-packet.md#contradictions-and-contested-claims).

**History:** 2026-10-10 — version 0.1.0, `initial-draft-1`, first W02 submission; predecessor and supersession null. Author self-review completed, independent review and release absent. Exact byte hash is in the packet. Next decision: challenge the contract against method-essential objectives and review the limits before authorizing any child work or implementation.

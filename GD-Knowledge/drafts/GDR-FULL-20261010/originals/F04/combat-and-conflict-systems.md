---
id: GDR-CAND-20261010-F04-TOP-01
kind: topic
title: Combat and conflict systems
version: 0.1.0
status: draft
owner_project: BH-GDR-Foundations-and-Systems
run_id: GDR-FULL-20261010
batch_id: F04
candidate_revision: initial-1
attempt_id: F04-attempt-1
updated: '2026-10-10'
date_basis: America/Los_Angeles; public access crossed 2026-10-11 UTC
evidence_checked: '2026-10-11'
aliases:
- combat design
- conflict resolution
- enemy roles
- telegraphs
- nonviolent alternatives
tags:
- timing
- positioning
- offense-defense
- encounters
- counterplay
- accessibility
- coverage-open
related_topics:
- GDR-CAND-20261010-F04-TOP-02
- GDR-CAND-20261010-F02-TOP-01
- GDR-CAND-20261010-F02-TOP-02
related_patterns:
- GDR-CAND-20261010-F04-PAT-01
- GDR-CAND-20261010-G02-PAT-01
- GDR-CAND-20261010-W02-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-F04-001
- GDR-SRC-20261010-F04-002
- GDR-SRC-20261010-F04-003
- GDR-SRC-20261010-F04-004
- GDR-SRC-20261010-F04-009
- GDR-SRC-20261010-F04-010
- GDR-SRC-20261010-F04-011
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-F04
coverage_status: coverage-open
predecessor_sha256: null
supersedes: null
integrity_receipt: ../reviews/full-run-20261010-f04-integrity-receipt.md
---

# Combat and conflict systems

**Draft research candidate — not released guidance.** Version 0.1.0; initial candidate revision. Author synthesis and author self-review only: no independent F04 review, game implementation, prototype, gameplay observation, participant recruitment or playtest occurred. Examples explicitly marked illustrative are inventions for analysis.

## Decision and scope

This entry helps a designer decide **what can oppose the player, how a response becomes possible, what commitment costs, and what counts as resolving the conflict**. It covers offense/defense, timing, positioning, readability, enemy roles, encounter escalation, resource pressure and nonviolent alternatives. It does not prescribe an engine, frame-data table, universal difficulty target, damage formula, animation style or genre convention. [C-01, C-02]

For this analysis, **conflict** means incompatible goals or claims on a relevant state. **Combat** is the force-based part of that space. “No kills” is not automatically “no violence”: injury, coercion, unconsciousness, property harm and proxy violence may matter to the local promise. Retreat can end immediate exposure without resolving an objective; a negotiation can resolve one goal while leaving hostility. These are working distinctions to make explicit, not definitions that every game must adopt. [C-01]

Foundations owns the rules and decision consequences. Worlds and Characters owns spatial/narrative orchestration and meaning; Presentation and Interaction owns sensory and input communication. Encounter topology is discussed here only where it changes legal responses. F03 economies/progression, W03 spatial/exploration and P03 camera/platform remain unreviewed or missing dependencies for this packet; their unseen conclusions are not adopted.

## Core explanation and mechanisms

### From an input to a consequential action

A useful diagnostic action record asks: what is known; which state permits the action; when the player commits; when its target or direction becomes fixed; when contact or resolution occurs; what can interrupt it; what resources are consumed; and when another action becomes possible. An instantaneous turn action may have no visible windup, while a sustained guard may overlap several phases. This is a conceptual record, not a required state-machine architecture. [C-02]

Offense and defense are not mutually exclusive verbs. A shove can interrupt an attack, move a target out of cover and expose the player during recovery. Guarding can preserve position while spending a resource; evasion can preserve health while abandoning an objective. Compare **which goal and future options remain**, not just damage prevented or dealt. [C-02, C-07]

Separate input receipt, legal acceptance and successful effect. A defensive press made during an uncancellable action can be correctly received but ineligible. A projectile can legally launch and miss. Increasing its sound or animation intensity cannot by itself repair either state. This transfers the inspected P02 distinctions without importing its unverified empirical results. [C-02]

### Counterplay is a timescale decision

Riot’s historical account distinguishes immediate tactical response from strategic preparation and explicitly rejects requiring tactical counterplay on every spell. It is a practitioner position, not measured evidence that a particular window produces fairness. [C-03; GDR-SRC-20261010-F04-001]

Ask where the relevant choice belongs: anticipating a threat, choosing equipment or position, interrupting a commitment, responding after a cue, accepting a hit to finish another goal, or withdrawing before contact. A response can be valid at one timescale and unavailable at another. Punishment for a previously disclosed commitment is not equivalent to a forced entry state with no viable option. [C-05, C-06, C-18]

A cue’s nominal duration is not the whole response opportunity. Consider when usable information becomes available, what interpretation is needed, whether the player is free to act, and how long the chosen effect takes to reach the threat. Hardware delivery and state eligibility are distinct; buffering does not remove physical latency. No inspected source here supports one universal reaction-time, parry-window or response-delay threshold. [C-02, C-05]

### Readability without eliminating uncertainty

Make the event’s **communicated facts** correspond to the actual opportunity. A ground mark that looks dodgeable but leaves no relevant response can communicate a false promise; Riot’s article discusses Arcane Comet in that context. The evidence is the developer’s textual example, not a replay or proof of player reaction. [C-04; GDR-SRC-20261010-F04-002]

Clarity need not reveal an enemy’s uncommitted intention. A feint may preserve uncertainty about which attack will happen while remaining clear about what the current stance permits. Conversely, calling an inconsistent hit region “mystery” does not establish an intentional information rule. Decide which facts are certain, uncertain, unavailable or deliberately deceptive, then test whether players can distinguish those categories. [C-04, C-14]

The proposed chain is: truthful available facts can support a relevant prediction; prediction may support selecting a legal response; successful selection still requires execution under local conditions; execution success is not automatically enjoyment. The first link has practitioner rationale and inspected dependency guidance. The full learning/experience chain remains a hypothesis. [C-04, C-05, C-14]

### Roles, positioning and combined threats

Treat position as a relationship to a goal, threat, ally or escape, not a coordinate alone. Range, facing, collision, cover, line of sight, elevation and mobility resources can each change the set of legal responses. A high platform may grant sight while removing an escape; defending a location may make the safest movement undesirable. [C-06, C-07]

The following is an **illustrative analytic vocabulary**, not an exhaustive enemy taxonomy or a source-derived list. [C-07]

| Role to test | Decision it might create | Combination to challenge |
|---|---|---|
| Displacer | Hold ground, accept movement or spend a stabilizing action | Forced displacement into another unavoidable threat |
| Pinner | Interrupt, escape a line or accept exposure | A second threat closes every escape during the pin |
| Protector | Change target priority or bypass protection | Protection and healing make all available progress temporary |
| Pursuer | Keep moving, create distance or confront | Retreat route costs more mobility than can be retained |
| Interdictor | Change approach, timing or route | Every alternate route is unavailable at the allowed entry state |

Individual demonstrations do not establish joint feasibility. Two attacks may each have a response in isolation while their combined timing, resource use and positioning rule out every permitted sequence. Conversely, inspecting only one simultaneous action may miss a valid two-step response. The relevant object is a **response policy over time**, under an explicit goal such as survive, protect an actor, take no damage, or escape. Those goals are not interchangeable. [C-06]

### Escalation, pacing and resource pressure

Booth’s Left 4 Dead presentation describes intensity estimation, a pacing-state cycle and a distinction between frequency and amplitude of threats. This is an authored system account. It does not certify an emotional diagnosis or prove that changing intervals leaves every sense of difficulty unchanged. [C-08; GDR-SRC-20261010-F04-003]

For a receiving design, audit whether a quieter interval changes recovery, replenishment, regrouping or the information available before the next conflict. Holding individual enemy strength fixed can still change cumulative resource demands. Keep “pacing,” “momentary difficulty” and “session survival” as separate measured constructs rather than settling the issue by terminology. [C-08, C-09]

Resource scarcity is not automatically deliberation. Compare spending now, delaying, changing method and abandoning the attempt. When each depleted attempt merely adds the same replenishment circuit, scarcity may primarily add repetition. When failed retries consume the resources needed for the intended recovery, the player may enter a deteriorating state. These are candidate mechanisms to test, not F03 economy findings. [C-09]

## Design choices and alternatives

| Choice | Conditions favoring it | Cost or contrary case | Simpler alternative |
|---|---|---|---|
| Explicit committed-event telegraph | Response depends on identifying the current event | More disclosure can remove intended inference; long cues can weaken the attacker | Expose the necessary fact, not every future branch. [C-04, C-14] |
| Strong commitment / limited cancel | Planning and accepting opportunity cost are central | Badly disclosed commitment can be mistaken for ignored input | Shorter action vocabulary with clearer commitments. [C-02, C-05] |
| Freer defense or cancellation | Repositioning and rapid correction are intended choices | May erase punish windows or enable cost-reset loops | Adjust one demand rather than granting universal cancel. [C-11, C-17] |
| More enemy roles/concurrency | Combined roles create genuinely different priorities | Combinations can exhaust legal responses or production coverage | Fewer distinct roles with contrasting arrangements. [C-06, C-07] |
| Adaptive pacing | Encounter density is a deliberate controllable variable | Proxy error, hidden changes and resource interactions complicate interpretation | Authored pauses or player-chosen initiation. [C-08, C-09] |
| Resource pressure | Scarcity changes methods or commitments | Repetition, hoarding, grind or unrecoverable retry state | Fixed encounter resources, recoverable baseline or fewer drains. [C-09] |
| Nonviolent alternative | The stated goal can genuinely be satisfied by different means | Recognition, consequences and production obligations multiply | Narrow the promise, or omit combat when it serves no desired decision. [C-12, C-13] |

### Assistance changes specific demands

Naughty Dog’s launch-era documentation supplies a concrete family of independently configurable combat interventions, including exceptions in certain encounters. The document does not demonstrate their effects on every player. Microsoft’s XAG 108 separately advises configurable demands and descriptive settings; this is platform guidance, not a formal standard adopted here. [C-10, C-11; GDR-SRC-20261010-F04-004, GDR-SRC-20261010-F04-010]

Specify whether assistance changes recognition, target selection, timing, execution, threat behavior, damage or recovery. Preserve required accommodations during learning checks. A player can prefer demanding strategic choices while needing reduced simultaneous inputs; an assist’s use is not sufficient evidence of low mastery. For shared competition, disclose the operative rules and comparison context rather than promising identical experiences or silently removing access. [C-11]

## Application process

1. **Define the promise and unit of success.** State the goal, allowed harm, permitted/prohibited means, entry capabilities and accepted failure outcomes. A survive objective does not imply a no-hit solution. [C-01, C-06]
2. **Diagnose the actual demand.** Separate knowing the rule, noticing the event, choosing a response, executing it and paying the setback. Record intended uncertainty and deliberate commitment. [C-02, C-05]
3. **Specify the smallest coherent action set.** Make costs, interruption, targeting and outcome recognition explicit before adding roles, effects or rewards. [C-02, C-07]
4. **Compose conditional responses.** Audit the important combined threats and permitted resource states using the linked pattern. Keep legitimate consequences of earlier choices visible. [C-06, C-18]
5. **Trace every supported resolution.** For each method, record result, acceptance, cost, aftermath and re-entry. Do not reduce a nonviolent route to “no kill event occurred.” [C-01, C-13]
6. **Request a locally authorized prototype/evaluation.** The proposed tests below require later approval, participants and a suitable implementation. Prefer the smallest comparison that separates competing explanations. [C-14, C-15]
7. **Revise or remove.** Retain a technique only when its targeted benefit survives comparison with simpler rules and the intended experience. F04 does not authorize this implementation work. [C-18]

## Patterns and genre adaptations

[Response-feasible threat composition](../patterns/response-feasible-threat-composition.md), `GDR-CAND-20261010-F04-PAT-01`, develops the joint-response audit. Its proposed experience benefit is low-confidence. It is not a compulsory safety net for every encounter. [C-18]

[Movement and traversal](movement-and-traversal.md), `GDR-CAND-20261010-F04-TOP-02`, owns locomotion and movement costs that can constrain combat. Existing reviewed **Bounded action grace** (`GDR-CAND-20261010-G02-PAT-01`) owns early/recent-state eligibility; **Multi-route objective contract** (`GDR-CAND-20261010-W02-PAT-02`) owns outcome/means recognition. Their bytes were inspected, but they are not copied into this F04 packet.

No genre artifact is created here. Adaptation questions remain facets: discrete versus continuous time; competing players versus authored opponents; lethal versus other consequences; player-controlled versus delegated movement; fixed versus selectable assistance. Genre-specific promises must be checked in the relevant one-file-per-genre guidance rather than inferred from a label.

## Examples and counterexamples

### Documentary contrary case: combat can undermine the intended activity

Anderson reports that increasing combat complexity during Mark of the Ninja development pulled play away from stealth, and describes a conflict between elimination-oriented optional objectives and nonlethal play. This is creator testimony with unspecified prototype builds and test methods—not an independently observed game effect or a universal argument against combat. Its design consequence here is to compare **removing** an attractive subsystem with improving it. [C-12; GDR-SRC-20261010-F04-009]

### Illustrative: protection is not simply avoidance

An invented encounter asks the player to hold a gate while civilians leave. Moving outside an incoming attack’s range preserves the player’s health but exposes the gate. A shield can preserve the gate while spending the resource needed to interrupt a later threat. An enemy pushing the defender changes the goal-state relationship rather than merely causing damage. Evaluate sequences against “protect the gate and survive,” not the easier question “could this attack be dodged in an empty arena?” See the pattern for a fully specified three-position example. No game or test is represented. [C-06, C-07, C-09]

### Illustrative: a nonviolent result with persistent consequences

A blockade prevents a supply cart reaching a settlement. The supported goal is delivery without injury; permanent friendship is not promised. A negotiated passage consumes a pledged favor, a diversion creates temporary access without agreement, and withdrawing preserves resources but does not deliver the cart. A knockout does not satisfy the no-injury condition simply because no one died. These are invented rules, not studio canon. [C-01, C-13]

| Case | State/feedback obligation in this illustration | Risk to test |
|---|---|---|
| Passage agreed, delivery not yet completed | Record permission and remaining delivery goal | Negotiation alone incorrectly grants completion |
| Delivery completed by diversion | Record delivery and unresolved hostility | Shared success message erases the distinct aftermath |
| Companion attacks during passage | Apply the declared actor/means rule and explain it | The player loses a route through uncommunicated proxy behavior |
| Player returns later | Restore known agreement, debt and delivery state | Re-entry resurrects a resolved combat requirement |
| Player reopens negotiation repeatedly | No duplicate favor/reward grant without a new justified event | Infinite reward or relationship farming |

Identical rewards are neither required nor sufficient. Compare opportunity cost, discovery effort, access to progression and the meaning of each consequence with the relevant owners. If a task specifically requires demonstrating a defensive technique, negotiating an alternative may legitimately fail that task. [C-13, C-17]

## Failure modes and constraints

**Access and comprehension.** Long descriptions can miss action deadlines; a second visual symbol is not a second sensory modality. Alternative cues must preserve relevant facts without exposing hidden enemies or competing intolerably with aiming, dialogue or navigation. Text size guidance from P01 does not become a universal native-game number: CSS units, rendered body height and platform recommendations remain distinct. [C-16]

**Ethics and representation.** Declaring a route nonviolent while silently rewarding harm-by-proxy can break its stated meaning. Conversely, labeling one route ethically superior requires context beyond a mechanical absence of kills. Shared-player assistance, coercive incentives and representation of surrender require explicit local review; no moral ranking or diagnosis is inferred from telemetry. [C-01, C-11, C-13]

**Localization and production.** Translate the condition and consequence, not just a move name. Distinguish “interrupts,” “cannot be interrupted,” “evades” and “reduces damage.” New attack combinations multiply interaction cases, but no universal combinatorial budget is supplied. Animation/camera changes can alter readable information even when damage stays fixed. [C-02, C-16, C-17]

**Exploitability.** Proposed risks include cancelling after effect but before cost, target changes evading a committed penalty, repeated disengagement resetting hostile states, safe resource farming, and repeated alternate-route reward recognition. Each is a hypothesis about an edge case; no exploit was reproduced. [C-17]

## Playtest and validation

**All protocols are proposed and not performed.** Decide locally on practical benefit/harm margins, sample precision, stopping rules, privacy and participant access needs before recruitment. Preserve accommodations and record game build, scene, controller, camera/display configuration, prior familiarity and relevant co-play context. Do not infer a universal sample size or required win rate. [C-11, C-15, C-16]

| Question / comparison | Procedure and measures | Confounds and rejecting result |
|---|---|---|
| Clearer facts or simply easier combat? | Compare factual cue revision with unchanged threat rules, then separately test longer execution opportunity. Ask pre-action event prediction and later observe outcome, explanation and chosen risk. | Practice, reduced concurrent load and prior knowledge. Reject the clarity account if only extra time improves execution while interpretation remains unchanged. [C-04, C-05, C-14] |
| Do combined threats respect the stated goal? | Compare a jointly audited composition with the baseline and a simpler reduced-threat alternative. Record planned/legal response sequences, entry resources, failure stage, perceived agency and desired tension separately. | A stronger player or easier total pressure can conceal a composition problem. Reject the pattern’s experience benefit if it adds no useful distinction or erases valued commitment. [C-06, C-18] |
| Does scarcity produce choice rather than repetition? | Compare resource conditions while recording changed methods, spending reasons, waiting/replenishment activity, successful recovery and abandoned attempts. | Reward differences, route familiarity and session length. Reject deliberation claim if only repetition/time changes. [C-09] |
| Are nonviolent outcomes recognized coherently? | Test supported, unsupported, partial, out-of-order and re-entry cases. Ask predictions of acceptance and consequences, then inspect what persists. | Better writing or new content may explain preference. Reject route support if required states cannot complete or consequences contradict the promise. [C-13, C-17] |

For a same-rule comprehension check, vary whether an action is actually available; do not reward an always-accept or always-reject strategy. Keep “what would happen?” separate from “what would you choose?” A changed underlying rule is an adaptation/discrimination test, not evidence of transfer of the original rule. [C-15]

## Claim ledger

Confidence applies to the stated proposition, not to universal effectiveness. Proposed design models are not formal standards or approved studio decisions. Local claim IDs do not identify claims in another entry.

### C-01

**Claim:** Model conflict as incompatible goals and combat as a force-based subset; nonlethal, nonviolent, disengaged and resolved are not interchangeable outcomes.

**Class:** `inference`. **Support / contrary case:** Working analytical definitions for F04; reviewed W02-route distinguishes outcome, permitted means, acceptance and aftermath. Not a historical or universal definition.

**Applicability:** Design-state analysis across real-time and discrete-action systems.

**Confidence:** Moderate: useful distinctions, but game-specific meanings must be declared.

**Unresolved / discriminating question:** Which means are actually prohibited, and who recognizes resolution?

### C-02

**Claim:** Represent an action through information, eligibility, commitment, contact/outcome, recovery and cancellation rather than treating input receipt as success.

**Class:** `inference`. **Support / contrary case:** Reviewed P02-input and P02-feedback, mechanisms and application sections; F02-decision, commitment discussion.

**Applicability:** Any action with state or time dependencies; the phases may overlap or be absent.

**Confidence:** Moderate: the distinctions are logically separable; a particular schema is not validated.

**Unresolved / discriminating question:** Which failure is the player actually encountering: recognition, legality, execution or interpretation?

### C-03

**Claim:** Riot distinguishes tactical from strategic counterplay and explicitly does not require tactical counterplay on every spell.

**Class:** `practitioner-heuristic`. **Support / contrary case:** GDR-SRC-20261010-F04-001, Champion Counterplay, tactical/strategic examples and paragraph beginning “We don’t need every spell.”

**Applicability:** Historical League design rationale, not every game or every current ability.

**Confidence:** High for the published position; low for any universal benefit.

**Unresolved / discriminating question:** What response timescale fits this encounter’s promise?

### C-04

**Claim:** A telegraph should communicate the facts the player is entitled to act on, without implying an unavailable response or exposing deliberately hidden facts.

**Class:** `inference`. **Support / contrary case:** GDR-SRC-20261010-F04-002, Abilities/Arcane Comet account; reviewed F02-decision information contract and P02-multimodal fact boundaries.

**Applicability:** Committed events and meaningful response opportunities; not a requirement to disclose all future decisions.

**Confidence:** Moderate for the design rationale; learning and trust effects remain unmeasured.

**Unresolved / discriminating question:** Do players misunderstand the event, fail execution, or deliberately accept the risk?

### C-05

**Claim:** Whether a response can arrive before a threat resolves depends on cue availability, interpretation, action choice, eligibility and travel/actuation; no universal windup follows.

**Class:** `inference`. **Support / contrary case:** C-02–C-04 plus explicit temporal reasoning. No empirical response-time threshold is imported; F04-012 remains inaccessible.

**Applicability:** Platform, display, input method and local action rules must be specified.

**Confidence:** Moderate for the decomposition; low for any predictive human-performance model.

**Unresolved / discriminating question:** Which stage limits the intended audience under actual load and hardware?

### C-06

**Claim:** Individually avoidable threats may lack a jointly feasible response policy under a declared entry state, resource budget and goal.

**Class:** `inference`. **Support / contrary case:** Logical composition example in F04-PAT-01; motivated, not proven effective, by GDR-SRC-20261010-F04-001 and GDR-SRC-20261010-F04-003.

**Applicability:** Feasibility means existence of an allowed sequence, not easy execution or guaranteed success.

**Confidence:** High for the logical possibility; moderate for audit utility.

**Unresolved / discriminating question:** Was the deficit forced at entry, a disclosed consequence of prior commitment, or intentionally unavoidable harm?

### C-07

**Claim:** Enemy roles can be evaluated by how their actions change position, target priority, information and available responses rather than by damage labels alone.

**Class:** `inference`. **Support / contrary case:** GDR-SRC-20261010-F04-003, PDF pp. 64–65 and 69, provides one role/placement account; proposed role matrix is original F04 analysis.

**Applicability:** Local systems design; spatial composition remains shared with Worlds.

**Confidence:** Moderate: operationally inspectable, not an optimal or exhaustive taxonomy.

**Unresolved / discriminating question:** Does a role introduce a distinct decision or only repeat a response at higher frequency?

### C-08

**Claim:** Booth describes an intensity-based pacing cycle and distinguishes its threat frequency from threat amplitude; those are developer constructs, not proof of unchanged effective difficulty.

**Class:** `practitioner-heuristic`. **Support / contrary case:** GDR-SRC-20261010-F04-003, PDF pp. 78–82 and 92; screenshots inspected for pp. 81 and 92.

**Applicability:** Historical Left 4 Dead director account.

**Confidence:** High for the documented account; no independent efficacy finding.

**Unresolved / discriminating question:** Would changing intervals alter resources, recovery or cumulative survival in the receiving design?

### C-09

**Claim:** Resource pressure is a candidate source of deliberation only when it changes meaningful choices; it may instead produce waiting, repetitive replenishment or a deteriorating retry state.

**Class:** `hypothesis`. **Support / contrary case:** F02-difficulty distinguishes setback from feedback; F04 reasoning about opportunity costs. F03 progression/economy evidence not available.

**Applicability:** Stamina, ammunition, cooldowns, attention or other limited capabilities; no refill ratios supplied.

**Confidence:** Low for a general player-experience effect; mechanisms depend on alternatives.

**Unresolved / discriminating question:** Does the constrained version change decisions rather than merely extend the same action sequence?

### C-10

**Claim:** Naughty Dog documents independently configurable combat interventions, including flanking behavior, dodge and slow motion, with exceptions for certain encounters.

**Class:** `observed-example`. **Support / contrary case:** GDR-SRC-20261010-F04-004, Combat Accessibility rows including Allies Don’t Get Grabbed and Invisible While Prone exceptions. Observation target is documentation.

**Applicability:** PS4 launch-era feature record; no running build inspected.

**Confidence:** High for the document’s contents; efficacy and current-version operation unknown.

**Unresolved / discriminating question:** Are promised assists valid in every locally required state, including exceptional encounters?

### C-11

**Claim:** Select assistance by the demand it changes and retain necessary accommodations; assistance status alone is not a sufficient measure of mastery.

**Class:** `inference`. **Support / contrary case:** Reviewed F02-difficulty and P02-input; GDR-SRC-20261010-F04-010, implementation guidance for discrete mechanics and descriptive settings; C-10 supplies a documented option family.

**Applicability:** Assistance design, not a mandate that every multiplayer ruleset use identical settings.

**Confidence:** Moderate for separating constructs; local benefit is untested.

**Unresolved / discriminating question:** Which skill remains expressive, and does the user choose the change without losing access?

### C-12

**Claim:** Anderson reports that richer combat pulled play away from intended stealth, and that elimination-oriented optional objectives could conflict with nonlethal play.

**Class:** `practitioner-heuristic`. **Support / contrary case:** GDR-SRC-20261010-F04-009, two Mark of the Ninja design answers identified in the reference.

**Applicability:** One creator’s retrospective account; no sample, protocol or exact prototype build available.

**Confidence:** Moderate for the reported production lesson; low for causal/general claims.

**Unresolved / discriminating question:** Would simpler combat or different objectives better serve this design’s goal?

### C-13

**Claim:** A supported nonviolent route needs coherent means constraints, recognition, aftermath and reward treatment; reward equivalence need not mean identical quantities.

**Class:** `inference`. **Support / contrary case:** Reviewed W02-route, Purpose/Recipe/Counterexamples; C-01 and C-12. No new tested nonviolent-route schema.

**Applicability:** Only genuinely supported alternatives; a method-essential task may reject a different route.

**Confidence:** Moderate for internal consistency; low for resulting agency or satisfaction.

**Unresolved / discriminating question:** Can the route remain resolved after re-entry, allies’ actions, partial completion and consequential world changes?

### C-14

**Claim:** Clearer cues and lower execution demand may improve action prediction while reducing desired ambiguity, commitment or expressive technique.

**Class:** `hypothesis`. **Support / contrary case:** Rival explanations derived from C-03–C-05 and C-11; no inspected controlled comparison establishes the balance.

**Applicability:** Separate information clarity from reduced threat and input assistance.

**Confidence:** Low: the tradeoff is plausible, context-dependent and explicitly open.

**Unresolved / discriminating question:** Does comprehension improve without unacceptable loss of the intended decision?

### C-15

**Claim:** Assess learning with both permitted and forbidden responses, separate factual prediction from preference, and distinguish same-rule transfer from changed-rule adaptation.

**Class:** `inference`. **Support / contrary case:** Reviewed F01-transfer corrected worked example and playtest; F02-decision.

**Applicability:** Proposed evaluations, not performed behavioral tests.

**Confidence:** Moderate for discriminatory test logic; no sample-size guarantee.

**Unresolved / discriminating question:** Can the participant explain the rule on a new case with a different correct answer?

### C-16

**Claim:** Accessibility and localization review should preserve event facts and deadlines, not merely add more cues; camera settings are a dependency, not a universal remedy.

**Class:** `inference`. **Support / contrary case:** Reviewed P02-multimodal and P01-visual; GDR-SRC-20261010-F04-011, implementation scope; GDR-SRC-20261010-F04-010, discrete-demand guidance.

**Applicability:** Local sensory/motor/language contexts. No medical or compliance finding.

**Confidence:** Moderate for reviewing mismatches; audience-specific effects unmeasured.

**Unresolved / discriminating question:** Do alternative cues remain usable during targeting, movement, dialogue and motion-sensitive play?

### C-17

**Claim:** Production and exploit review should include cancellation, target changes, threat interruption, repeated exit/re-entry, reward duplication and shared-player consequences.

**Class:** `hypothesis`. **Support / contrary case:** State-based implications of C-02, C-06, C-09 and C-13; original F04 risk analysis, not observed exploits.

**Applicability:** Only risks relevant to the actual rules; not an implementation instruction.

**Confidence:** Low for occurrence; moderate for identifying concrete testable cases.

**Unresolved / discriminating question:** Which boundary case invalidates the promised cost, outcome or choice?

### C-18

**Claim:** Response-feasible composition is a conditional audit technique, not a rule that every hit must be avoidable or every adverse outcome reversible.

**Class:** `hypothesis`. **Support / contrary case:** F04-PAT-01 recipe and counterexample, constrained by GDR-SRC-20261010-F04-001 and F02-decision. No direct test of the pattern.

**Applicability:** Declared goal and entry-state promise must exist; excludes deliberate no-win outcomes unless audited for their different purpose.

**Confidence:** Low for gameplay benefit; a model witness alone does not establish fairness.

**Unresolved / discriminating question:** Would simpler threat reduction or an explicitly harsher commitment rule better achieve the intended experience?

## References

All source IDs are temporary F04 identities. Access date: 2026-10-11 UTC (2026-10-10 in America/Los_Angeles). Locators specify the inspected extent, not an assertion that every linked item was read in full. Public-source bytes were not archived or hash-verified.

### GDR-SRC-20261010-F04-001

Riot Scruffy. **[Quick Gameplay Thoughts: May 14](https://www.leagueoflegends.com/en-us/news/dev/quick-gameplay-thoughts-may-14/)**. Riot Games; 2021-05-14. Edition/build: Historical League of Legends developer article; game build not specified.

**Access:** `full`. **Type:** Firsthand developer rationale. **Locator:** Champion Counterplay: definition; tactical versus strategic examples; paragraph beginning “We don’t need every spell”; strengths/weaknesses paragraphs. **Limits:** No comparative study or effect size supplied. The article is not a current champion specification. **Relationships:** Same institutional source as F04-002; the two articles are not independent experiments. Central deduplication pending. **Rights:** Copyright Riot Games; paraphrase only; no media redistributed. Claim bindings appear in this entry’s ledger.

### GDR-SRC-20261010-F04-002

bananaband1t / Riot Games. **[Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/)**. Riot Games; 2021-03-12. Edition/build: Historical developer article; example builds not identified.

**Access:** `relevant-excerpt`. **Type:** Firsthand development account; textual descriptions of visual examples. **Locator:** “The Unbreakable Vows”; “Abilities,” including the Arcane Comet ground-circle example; “Changes From Development”. **Limits:** Text inspected, not an independent game replay or a perceptual experiment. Embedded media were not used to establish behavior. **Relationships:** Same institutional source as F04-001; no independent causal corroboration. Central deduplication pending. **Rights:** Copyright Riot Games; paraphrase only; embedded images/animations not redistributed. Claim bindings appear in this entry’s ledger.

### GDR-SRC-20261010-F04-003

Michael Booth / Valve. **[The AI Systems of Left 4 Dead](https://cdn.akamai.steamstatic.com/apps/valve/2009/ai_systems_of_l4d_mike_booth.pdf)**. Valve; AIIDE presentation; 2009; exact publication day unknown. Edition/build: 2009 presentation, 95-page PDF; historical Left 4 Dead system account.

**Access:** `relevant-excerpt`. **Type:** Firsthand technical/design presentation. **Locator:** PDF pp. 64–65 (Structured Unpredictability); p. 69 (special-infected placement); pp. 78–82 (intensity and pacing states); p. 92 (pacing versus difficulty). Page numbering is 1-based PDF position. Screenshots inspected for pp. 81 and 92.. **Limits:** An authored intensity proxy is not a validated measurement of a player’s emotional state. No causal comparison of the proposed F04 techniques. **Relationships:** One Valve production account, not one independent source per slide. Central deduplication pending. **Rights:** Copyright Valve; paraphrase only; PDF/slides not redistributed. Claim bindings appear in this entry’s ledger.

### GDR-SRC-20261010-F04-004

Naughty Dog; displayed byline Matthew Dunnerstick. **[The Last of Us Part II: Accessibility Features Detailed](https://www.naughtydog.com/blog/the_last_of_us_part_ii_accessibility_features_detailed)**. Naughty Dog; 2020-06-09. Edition/build: PS4 launch-era feature documentation; page also contains Patch 1.01/1.02 annotations; not a current remaster verification.

**Access:** `relevant-excerpt`. **Type:** Official feature documentation. **Locator:** “Alternate Controls”; “Assistance”; “Navigation and Traversal” rows Navigation Assistance, Traversal Assistance and Ledge Guard; “Combat Accessibility” rows and encounter exceptions. **Limits:** Documents intended options, not measured accessibility, enjoyment, transfer, or efficacy in a verified running build. **Relationships:** Same URL appears in reviewed F02 as GDR-SRC-20261010-F02-011 and W02 as GDR-SRC-20261010-W02-017. Re-inspected here; mapping/deduplication pending, not independent evidence. **Rights:** Copyright Naughty Dog; paraphrase only; no screenshots or videos redistributed. Claim bindings appear in this entry’s ledger.

### GDR-SRC-20261010-F04-009

Nels Anderson, interviewed by Timothy Courtney. **[Designer of Games Like Mark of the Ninja and recently Firewatch, Nels Anderson Interview with Timothy Courtney](https://timothycourtneymedia.com/interview/game-talk/firewatch-game-designer-nels-anderson-interview-with-timothy-courtney.html)**. Timothy Courtney Media; 2016-02-28. Edition/build: Historical interview; internal prototype builds and test dates not specified.

**Access:** `relevant-excerpt`. **Type:** First-person practitioner testimony, not a controlled study. **Locator:** Answers to the questions beginning “When you were designing Mark of the Ninja...” and “Mark of the Ninja harkens...” (combat complexity and optional objectives). **Limits:** No participant count, protocol or quantitative effect. Creator-reported testing is not a player study performed or independently verified in F04. **Relationships:** One interview; separate answers do not count as independent studies. Central deduplication pending. **Rights:** Copyright respective author/interview participants; brief paraphrase only. Claim bindings appear in this entry’s ledger.

### GDR-SRC-20261010-F04-010

Microsoft. **[Xbox Accessibility Guideline 108: Game difficulty options](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/108)**. Microsoft Learn; last updated 2026-03-04. Edition/build: Live unnumbered web revision checked on access date.

**Access:** `relevant-excerpt`. **Type:** Platform/vendor practitioner guidance, not a formal standard asserted by F04. **Locator:** Scoping questions; implementation guidelines concerning discrete mechanics, descriptive language, difficulty changes and saving; contextual note about consultation. **Limits:** No F04 compliance determination, medical conclusion or universal number of presets. Listed examples do not establish efficacy. **Relationships:** Same URL as reviewed GDR-SRC-20261010-F02-009; fresh passage/date check here. Central deduplication pending. **Rights:** Microsoft documentation; paraphrase only; no example media redistributed. Claim bindings appear in this entry’s ledger.

### GDR-SRC-20261010-F04-011

Microsoft. **[Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117)**. Microsoft Learn; last updated 2026-03-04. Edition/build: Live unnumbered web revision checked on access date.

**Access:** `relevant-excerpt`. **Type:** Platform/vendor practitioner guidance, not a formal standard asserted by F04. **Locator:** Implementation guidelines and gameplay-motion scope note; camera movement/shake, motion blur and configurable motion-related presentation. **Limits:** No universal camera/FOV/velocity values, VR efficacy finding, comfort guarantee or medical recommendation. **Relationships:** Same URL as reviewed GDR-SRC-20261010-P02-010 and GDR-SRC-20261010-P01-10. Those historical identity spellings are preserved; central deduplication pending. **Rights:** Microsoft documentation; paraphrase only; no example media redistributed. Claim bindings appear in this entry’s ledger.

### Inspected reviewed-candidate dependencies

These are unreleased library candidates, not independent empirical sources. Exact bytes were read from the parent-selected archive; only the stated conceptual distinctions transfer. Their original public empirical findings are not reasserted without fresh source inspection. Missing package-local copies are deliberate: previous batches are not resent.

- **`GDR-CAND-20261010-F02-TOP-01`**, `selected-drafts/topics/decision-design.md`, version `0.1.0`, draft, revision `initial-capture-1`. SHA-256 `2fe66a5bf914a9c3f4101e168cdfd344a26eeadbfea7c45d16a9f17cca33bc6c`. Inspected relevance: Decision/scope, mechanisms, choices and claim ledger; decision prediction versus preference; commitment and information.
- **`GDR-CAND-20261010-F02-TOP-02`**, `selected-drafts/topics/challenge-and-difficulty.md`, version `0.1.0`, draft, revision `independent-review-correction-1`. SHA-256 `7a48dc96849938268b809723a07f6150927c104a2a120c35da08e34d13dc8ef1`. Inspected relevance: Mechanisms, assistance, recovery and tests; corrected evidence locator preserved without importing empirical numerical results.
- **`GDR-CAND-20261010-P02-TOP-01`**, `selected-drafts/topics/controls-and-input.md`, version `0.1.0`, draft, revision `review-correction-1`. SHA-256 `b9235153ba8b742c6df47e9e23844d9ab5da82e4212ebd22f04e314f6ccce21b`. Inspected relevance: Action recognition/eligibility/outcome; buffering/context validity; remapping versus input-demand changes.
- **`GDR-CAND-20261010-P02-TOP-02`**, `selected-drafts/topics/feedback-and-game-feel.md`, version `0.1.0`, draft, revision `review-correction-1`. SHA-256 `6cf571a87946b9b40470cce966862219906f495b50c0b1db04e1ad7677ca4415`. Inspected relevance: Event facts versus ornament; deliberate timing versus system latency; outcome measures not interchangeable.
- **`GDR-CAND-20261010-P02-TOP-03`**, `selected-drafts/topics/multimodal-communication.md`, version `0.1.0`, draft, revision `review-correction-1`. SHA-256 `f70cdda6a504b283b85bd1c565c10ef503d4aad7d9877c4b00707bb4f819bc2c`. Inspected relevance: Fact-preserving alternatives; deadline/context boundaries; competing attention; no modality-equivalence claim.
- **`GDR-CAND-20261010-F01-PAT-01`**, `selected-drafts/patterns/supported-attempt-and-transfer-check.md`, version `0.1.0`, draft, revision `independent-review-correction-1`. SHA-256 `5bbbe570d8af2bd36865be6f970e8215261d3bc703094b6d3da33c08278ef6e1`. Inspected relevance: Corrected answer-varying examples; same-rule transfer separated from changed-rule adaptation.
- **`GDR-CAND-20261010-P01-TOP-01`**, `selected-drafts/topics/visual-communication.md`, version `0.1.0`, draft, revision `review-correction-1`. SHA-256 `b8e23ae234041fa0893295fdd36457eb08e0e77a60cca4229b7a77f0f13844b7`. Inspected relevance: Numerical accessibility scope: CSS/point criteria versus rendered text-body height and platform guidance.
- **`GDR-CAND-20261010-G02-PAT-01`**, `selected-drafts/patterns/bounded-action-grace.md`, version `0.1.0`, draft, revision `initial-1`. SHA-256 `03e0819fc92f1e6fcfe87d84871d2cbb6de337d3bcd57e044e614cb3d2773f1c`. Inspected relevance: Early/recent-state eligibility; single consumption, expiry, cancellation; ownership pending; benefit remains conditional.
- **`GDR-CAND-20261010-W02-PAT-02`**, `selected-drafts/patterns/multi-route-objective-contract.md`, version `0.1.0`, draft, revision `independent-review-correction-1`. SHA-256 `2512fbee56b449df49c61ede24bd07ea9314084d8e75e7c6070ad58dc65c0702`. Inspected relevance: Purpose through playtest; outcome versus means, recognition, aftermath and method-essential counterexample.

Archive receipt, transfer limits and unresolved links: [F04 review packet](../reviews/full-run-20261010-f04-review-packet.md#reviewed-dependency-inspection). No canonical identity or release is implied.

## Open questions and change history

**Coverage remains open.** No directly inspected controlled combat-telegraph experiment, networked response study, current game-build reproduction, cultural study of nonviolent meaning or F03 resource-economy analysis establishes the proposed effects. Enemy-role taxonomy and resource-pressure mechanisms are analytical proposals. The negative creator account is not a quantified causal result.

Contradictions and rival explanations `F04-CON-01` through `F04-CON-07`, source-access details, child-work registration requests and review gates are in the [review packet](../reviews/full-run-20261010-f04-review-packet.md). Additional nonviolent persistence work is queued without duplicating W02’s objective contract.

**History:** version `0.1.0`, candidate revision `initial-1`, attempt `F04-attempt-1`; first submission under the assigned identity. Predecessor hash and supersession: null. Exact bytes are identified in the [integrity receipt](../reviews/full-run-20261010-f04-integrity-receipt.md). No independent F04 review or approval has occurred. The next decision is whether to accept this bounded synthesis for independent Gate C review, revise its claims, or register the named follow-on questions—not to release or implement it.

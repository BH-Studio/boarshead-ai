---
id: GDR-CAND-20261010-W01-TOP-03
kind: topic
title: Character design
version: 0.1.0
status: draft
owner_project: BH-GDR-Worlds-and-Characters
run_id: GDR-FULL-20261010
batch: W01
identity_scope: run-scoped-candidate
candidate_revision: initial
updated: '2026-10-10'
evidence_checked: '2026-10-10'
input_snapshot: GD-Knowledge-Starter-v0.1.0 candidate; nine supplied files; canonical
  commit not supplied
aliases:
- character motivation
- NPC agency
- character relationships
- character arc
- character interpretation
- capability-based characterization
tags:
- goals
- beliefs
- relationships
- change
- refusal
- representation
- nonverbal-characterization
related_topics:
- GDR-CAND-20261010-W01-TOP-01
- GDR-CAND-20261010-W01-TOP-02
related_patterns:
- GDR-CAND-20261010-W01-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-W01-08
- GDR-SRC-20261010-W01-09
- GDR-SRC-20261010-W01-10
- GDR-SRC-20261010-W01-11
- GDR-SRC-20261010-W01-12
- GDR-SRC-20261010-W01-13
- GDR-SRC-20261010-W01-14
- GDR-SRC-20261010-W01-15
lead_only_source_ids: []
reviewer: null
approved_by: null
approved_date: null
---

# Character design

**Research candidate — not released guidance.** This file is complete for bounded W01 drafting, not a claim of exhaustive coverage or accepted evidence. Human research authorization does not approve this entry’s conclusions, game adoption, implementation, publication or permanent identity. No prototype, game execution, participant recruitment or player test was performed.

## Decision and scope

**Decision:** What does a character need to do, want, believe, enable, resist or signify in this experience, and how should the player be able to interpret those qualities? This entry covers playable characters, authored or customized avatars, allies, rivals, inhabitants and functional cast members. It concerns goals, contradictions, capabilities, relationships and change without requiring long dialogue, a branching plot or a realistic human simulation. [C-01; GDR-SRC-20261010-W01-10; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-13] [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

The distinction between **authorial intention** and **player interpretation** is central. A design note saying “loyal” is not evidence that players perceive loyalty. A useful action can express loyalty, expedience, fear, duty or a desire for control, depending on the surrounding evidence. The proposed workflow records the intended reading and plausible alternatives rather than assuming the trait has been successfully delivered. [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09] [C-12; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

Excluded: visual-production specifications, animation systems, performance direction details, dialogue localization implementation, agent runtime architecture, combat tuning, psychiatric claims and real people’s private histories. Those require other owners or research. No existing game’s character canon becomes library truth.

## Core explanation and mechanisms

### Start with the character’s role in play

A player-authored persona, an established protagonist and a narrowly functional ally can need different amounts and kinds of specification. For an authored protagonist, the player may interpret choices as expressions within a defined person. For an avatar intended for projection, strongly authored reactions may instead narrow the player’s self-expression. Neither form is inherently superior; identify the intended relationship between player and character before prescribing a personality or arc. [C-01; GDR-SRC-20261010-W01-10; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-13]

A concise cast member might need a recognizable capability, a stance toward the player and a repeatable response to a relevant situation. A central relationship might need competing commitments, changes in trust, and a history that supports more than one interpretation. More biography is not automatically a substitute for those relationships becoming visible in action. [C-01; GDR-SRC-20261010-W01-10; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-13] [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

### Goals explain some actions, not all meaning

A proposed reasoning chain is: a character wants or values something, believes something about the situation, acts within constraints, and leaves evidence from which the player infers a motive. Any link may be incomplete. A character can be mistaken, conflicted, habitual, impulsive or deliberately unreadable. This is an authoring model for selected scenes, not a claim that all people optimize goals or that every action should be rationally explained. [C-02; GDR-SRC-20261010-W01-08] [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

**Evidence box:** Riedl and Young evaluated 32 undergraduate game-development students reading one of two generated stories. Measures examined judgments of reasons for actions, not game enjoyment or empathy. Reported one-tailed comparisons were mixed: the favorable-answer comparison was *p* < .0585; rejection of poor reasons was *p* < .05. Story and explicit goal-exposition differences limit attribution. The model also discusses limits around failed intentions. This is narrow support for studying action intelligibility, not a universal character recipe. [C-03; GDR-SRC-20261010-W01-08]

**Evidence-to-application bridge:** Where understanding motive is part of the local design goal, provide evidence of relevant belief, pressure or commitment, then test the inferred reason. Do not assume that explaining a motive makes a person likable, excuses harmful behavior, produces empathy or makes a dramatic arc necessary. [C-02; GDR-SRC-20261010-W01-08] [C-12; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

### Believability, legibility and liking are different targets

Bates’s animation-informed account treats believability as a suggested life rather than simple realism. That offers a useful possibility for stylized characters, but W01 rejects a universal requirement for overt emotional display. Quiet, restrained, nonhuman or difficult-to-read characters should not be “corrected” merely because they do not communicate through a conventional expressive style. [C-04; GDR-SRC-20261010-W01-10] [C-10; GDR-SRC-20261010-W01-09; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-10]

Distinguish several proposed design targets: **recognition** (who this is), **intelligibility** (why this action makes sense), **affect** (how the player feels), **autonomy** (whether the character seems to have commitments beyond player convenience), and **relationship** (how the player understands their connection). A scene can succeed at one and fail at another. A threatening figure may be recognizable and intelligible without being sympathetic. These categories are W01 analytical tools, not a validated psychological scale. [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09] [C-12; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

### A relationship does not imply control

Jayanth describes an *80 Days* encounter in which the Murri girl refuses the protagonist’s offer to deliver her letter. The source supports the writer’s deliberate limit on intervention; it does not establish a universally positive player response. W01 treats refusal as one possible relationship signal, not a command to deny agency arbitrarily. [C-05; GDR-SRC-20261010-W01-09]

The *Prom Week* creators describe interactions shaped by social circumstances. Such an approach can author relationship-specific reactions, but the selected model represents that work’s assumptions—not timeless laws of friendship, status or attraction. Avoid importing a fictional social abstraction into claims about real people. [C-06; GDR-SRC-20261010-W01-11]

## Design choices and alternatives

### An actionable specification without mandatory personality formulas

The following matrix is a proposed authoring aid. Use only the dimensions that serve the role; none requires a numeric score or an executable agent system. [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

| Dimension | Authoring question | Decision and alternative |
|---|---|---|
| Goal or commitment | What does the character seek, protect, continue, avoid or refuse? | A specific immediate objective may be enough. A stable practice or duty can replace a large personal destiny. |
| Belief and knowledge | What does this character think is happening, and what evidence could change that belief? | Distinguish a lie from a mistake, an unknown and an intentionally undisclosed reason. |
| Contradiction or tension | Which commitments conflict under these conditions? | Use a particular conflict where useful; an arbitrary reversal or obligatory “flaw” is not required. |
| Capability and constraint | What can the character do, afford, access, authorize or endure here? | Capabilities may be social or situational, not only physical power. Limited capability need not imply lesser importance. |
| Relationship | What does each party expect, owe, trust, fear or misunderstand? | The two directions can differ. A single affinity value may be too narrow for the intended relationship. |
| Change | Which belief, skill, commitment, relationship or interpretation might alter, and under what conditions? | A flat or steadfast character is a valid alternative when transformation is not the promise. |
| Player evidence | What action, absence, consequence, object or response supports the intended reading? | Explicit explanation is optional; the evidence can remain partial if uncertainty serves the experience. |

**Contradiction is specific, not decorative.** “Protects the crew but distrusts the council that funds it” supplies a concrete pressure. “Kind but cruel” says little until the author identifies circumstances, targets and consequences. The proposed test is whether the apparent contradiction produces a readable tension or simply requires a different personality in every scene. Deliberate inconsistency can itself be the intended reading; record it as such instead of calling every reversal depth. [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

**Capabilities can characterize.** The official *Never Alone* description differentiates Nuna and Fox through complementary abilities. Booth’s *Left 4 Dead* deck links character vocalizations to situational awareness and cooperation. These creator descriptions support considering action-linked characterization beyond exposition; they do not prove that a particular ability or line causes attachment. [C-07; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-13]

**Choose the locus of change.** Learning a technique, revising a belief, accepting a limit, changing a relationship and being understood differently by the player are distinct developments. A character may remain committed while the player’s judgment changes. Conversely, a statistical power increase may leave the character’s values untouched. Do not describe all progression as a moral or psychological transformation. [C-09; GDR-SRC-20261010-W01-08]

**Match autonomy to the offered role.** An NPC can refuse a request through an authored scene; this does not require unrestricted off-screen simulation. A commanded unit can still be characterized within the boundaries of a command-oriented experience. The choice concerns what the player perceives and is allowed to influence, not whether all cast members must share one runtime model. [C-05; GDR-SRC-20261010-W01-09] [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

## Application process

1. **Define the relationship to the player.** State whether this figure is controlled, interpreted, collaborated with, opposed, encountered briefly or partly projected by the player. Name what the work promises to let the player decide. [C-01; GDR-SRC-20261010-W01-10; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-13]
2. **Choose a representative pressure.** Write one situation where a desire, duty, limit or relationship matters. Begin with behavior under a meaningful condition rather than an unbounded biography. [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]
3. **List plausible readings.** State the intended interpretation and at least one reasonable alternative. A refusal may mean mistrust, inability, danger, principle or simple lack of interest. Decide which ambiguity to preserve. [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09] [C-12; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]
4. **Design evidence and consequence.** Connect the action to a relevant belief, prior commitment or visible constraint when intelligibility is needed. Show what the action enables, costs or changes; avoid explaining everything in a trait label. [C-02; GDR-SRC-20261010-W01-08] [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]
5. **Specify change and non-change.** Record what new evidence, event or relationship could change the response and what cannot be bought, persuaded or solved by the player. An absolute boundary is possible; it must not be disguised as a progression task the player can complete. [C-05; GDR-SRC-20261010-W01-09] [C-09; GDR-SRC-20261010-W01-08]
6. **Review cast and perspective.** Ask whether everyone outside the protagonist exists only as an obstacle, reward or spokesperson. Consider access, language, cultural participation and the right not to disclose a private history. These are review questions, not claims of completed consultation. [C-10; GDR-SRC-20261010-W01-09; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-10]
7. **Prepare a bounded comparison and revise.** Test the intended reading separately from liking and comprehension. Remove unnecessary exposition, add missing causal evidence, preserve meaningful uncertainty or change the interaction promise according to the result. [C-12; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

## Patterns and genre adaptations

[Consequence-preserving reconvergence](../patterns/consequence-preserving-reconvergence.md), `GDR-CAND-20261010-W01-PAT-01`, is relevant when characters meet again after different histories. Its obligation is to retain the consequences the relationship actually promised, not to remember every line forever.

[Worldbuilding](worldbuilding.md), `GDR-CAND-20261010-W01-TOP-02`, distinguishes personal belief from institutional or world truth. [Narrative structures](narrative-structures.md), `GDR-CAND-20261010-W01-TOP-01`, distinguishes character limitation from the kinds of influence offered to the player.

No separate “goal/conflict/change” pattern is extracted: this remains a broad specification lens, and the inspected evidence does not justify packaging a mandatory arc as a reusable proven technique. No genre file was supplied or assigned. Future genre-owner guidance should evaluate different audience promises rather than declare all characters within a market label require the same arc.

## Examples and counterexamples

### Illustrative worked example: Iri, the maintenance operator

**Invented authoring example; not a real person, game observation or tested scene.** Iri is responsible for keeping a transport platform safe. Their immediate goal is to complete a repair before a crew transfer. They believe an exposed bracket may fail, can inspect and isolate the mechanism, and lack the authority to schedule a replacement vehicle. They respect a colleague’s judgment but distrust an administrator who previously ignored an inspection. [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

The player asks Iri to restart the platform to save time. Iri refuses. The scene shows the isolated bracket and gives Iri a practical alternative: help move a small load along a slower route. The intended reading is a safety commitment under a capability limit, not generic hostility. The player may still dislike the delay. Understanding the motive and accepting the outcome are different evaluation questions. [C-02; GDR-SRC-20261010-W01-08] [C-12; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

If the player supplies a verified replacement part and an inspection supports its suitability within the fictional scenario, Iri may restart the platform. Flattery does not change the physical concern. Alternatively, Iri might permit restart only after another qualified colleague reviews it, expressing a relationship and accountability practice. These are invented narrative conditions, not engineering or safety instructions. [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

The character’s contradiction is situated: Iri wants to protect colleagues but fears being treated as an obstruction and losing future influence. Their change need not be “learn to stop caring about rules.” It could be trusting a colleague’s evidence, asking for help, or accepting that the player will proceed by another route. Iri can remain quiet and reserved throughout. [C-09; GDR-SRC-20261010-W01-08] [C-10; GDR-SRC-20261010-W01-09; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-10]

**Bad application:** The game increases a friendship meter after gifts and suddenly makes Iri abandon the same safety concern without changed evidence or an intended corruption theme. This may read as a transactional gate rather than the established commitment. If manipulation or hypocrisy is the intended characterization, author that interpretation and its consequences rather than calling the inconsistency invisible. [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09] [C-12; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

**Alternative:** For a brief session, omit the administrator history and complicated relationship. The bracket, refusal and alternative route may supply all needed characterization. For a relationship-centered experience, deepen the prior dispute and allow the player to interpret whether Iri’s caution also conceals resentment. Neither amount of detail is automatically better. [C-01; GDR-SRC-20261010-W01-10; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-13]

### Illustrative nonverbal rival

A recurring rival helps reset shared equipment after each contest but avoids a celebratory handshake. The work might intend professionalism without intimacy. Do not force the rival into a hidden trauma explanation or a friendliness progression. Use repeated actions, consequences and optional context to support the intended reading, or deliberately leave it open. A participant reading shyness rather than pride is not necessarily a failure unless that difference undermines a specific intended decision. [C-01; GDR-SRC-20261010-W01-10; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-13] [C-10; GDR-SRC-20261010-W01-09; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-10] [C-12; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

### Strong counterexample: intentional unknowability

A figure encountered only in dreams may be intended as an unstable symbol. Requiring a stable goal ledger, consistent interpersonal tactics or a rational arc can make it less effective for that purpose. Use the framework to record the desired ambiguity and boundaries of interpretation, not to explain away the ambiguity. W01’s strongest recommendation is conditional on some intelligible behavior being useful. [C-01; GDR-SRC-20261010-W01-10; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-13] [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

No named game was independently played, recorded or instrumented during W01. Creator accounts are labeled as accounts; all worked scenarios above are illustrative inventions.

## Failure modes and constraints

**Trait lists replacing behavior.** A lengthy description can coexist with generic reactions. The proposed remedy is a representative situation and evidence of the desired reading, not automatically more biography. However, explicit description may be appropriate for rapid recognition or a particular narrative voice; behavior-only characterization is not a universal rule. [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

**Goal reduction.** A person reduced to one objective can become predictable or instrumental. Competing duties, limited knowledge, habit and unspoken boundaries are possible alternatives. Do not diagnose fictional or real people from behavior or equate difficulty of interpretation with a disorder. [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09] [C-10; GDR-SRC-20261010-W01-09; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-10]

**Compulsory suffering or availability.** Trauma need not justify every unusual behavior; romantic or emotional access need not be a reward. Refusal can be permanent. Equally, a creator should not insert refusal while retaining signals that imply a solvable persuasion task. Ethical intent does not erase a misleading affordance. [C-05; GDR-SRC-20261010-W01-09] [C-10; GDR-SRC-20261010-W01-09; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-10]

**Representation and culture.** One character’s experience does not establish facts about everyone sharing an identity. Work with relevant people when depicting identifiable lived contexts, keep disagreement visible, and distinguish consultation from blanket approval. W01 did not conduct that work. [C-10; GDR-SRC-20261010-W01-09; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-10]

**Access and presentation.** Character information delivered through only a fleeting facial cue, a spoken nuance or a difficult-to-read line may not reach the intended audience. Ask Presentation and Interaction for an appropriate route to the needed information without demanding that every emotion be explicitly labeled. Avoid treating eye contact, facial intensity or conventional speech as universal evidence of sincerity. These are proposed safeguards requiring situated evaluation. [C-10; GDR-SRC-20261010-W01-09; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-10] [C-11; GDR-SRC-20261010-W01-15; GDR-SRC-20261010-W01-14]

**Localization.** Supply the speaker’s knowledge, relationship, intended degree of politeness, uncertainty and reason for refusal. Do not require literal preservation of a short adjective when it misstates the relationship in another language. Provide room to query ambiguous motives; translators should not have to invent character canon to resolve missing context. [C-11; GDR-SRC-20261010-W01-15; GDR-SRC-20261010-W01-14]

**Production and systems boundaries.** Persistence of a relationship or memory must be agreed conceptually with the relevant systems owner. A written promise of remembrance is not an implemented capability. Limit the cast and combinations to what can be authored and reviewed; no universal cast size or affinity formula is recommended. [C-08; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

## Playtest and validation

**Status: proposed; not performed.** No character prototype, participant study or performance test occurred.

**Question:** Does the selected evidence let the intended audience interpret the character in the desired way, and which interpretations remain acceptably open? A possible comparison contrasts a scene with contextual action evidence against an equally polished scene with descriptive biography. Keep word count, event stakes, available actions and presentation quality comparable or report the differences. A separate condition may intentionally leave the motive unclear; do not label ambiguity a defect in advance. [C-12; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

Before a pivotal response, ask participants what the character might do and why, allowing several answers. Afterward, ask what evidence supports their reading, how they feel about the character, and whether they believe a refusal can or should be changed. Separate “I dislike this person,” “I do not understand this action,” and “I thought the interaction allowed something it does not.” [C-12; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

Use participants relevant to intended languages, access needs, cultural context and familiarity. Examine whether the evidence survives the actual delivery channels, not just a transcript. Avoid assuming that a cultural consultant is representative of all players or that a player’s positive rating supplies representational approval. Track the effect of prior liking, character art, voice performance, player success and stakes as confounds. [C-10; GDR-SRC-20261010-W01-09; GDR-SRC-20261010-W01-12; GDR-SRC-20261010-W01-10] [C-12; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

**Proposed decision rule:** Revise if a needed motive is persistently inferred from the wrong evidence, if a deliberate boundary looks like a broken progression task, or if an access route withholds the information required for the intended interpretation. Preserve dislike, uncertainty or conflicting thematic readings when those are intentional and the interaction promise remains honest. Reject the framework’s added detail if it worsens clarity, undermines intended openness or has no acceptable production value. Set any numerical acceptance margins and sample design only for a later authorized study. [C-12; GDR-SRC-20261010-W01-08; GDR-SRC-20261010-W01-09]

## Claim ledger

Claim IDs are local to this file. Class and confidence are separate. Proposed applications and tests are not approved studio decisions or performed research. A source attached to an inference identifies its premises, not a direct test of the recommendation.

<a id="claim-c-01"></a>
### C-01 — hypothesis
Character design should begin with the player-facing role and intended interpretation, not a mandatory biography, flaw, emotional display or transformation arc.
**Support / contradiction:** Sources show different authoring emphases; the role-first selection rule is a proposed synthesis, not a demonstrated superiority result.
**Sources / exact locators:** GDR-SRC-20261010-W01-10: §1 Believability, printed p. 1; GDR-SRC-20261010-W01-12: Features: complementary Nuna/Fox abilities; GDR-SRC-20261010-W01-13: PDF p. 25, Vocalizations.
**Applicability:** Player characters, autonomous-seeming NPCs, functional allies, opponents and minimal casts.
**Confidence:** low — reasonable cross-context synthesis with limited direct comparison.
**Unresolved:** When sparse role-based characterization is insufficient for attachment, interpretation or ethical representation.

<a id="claim-c-02"></a>
### C-02 — inference
Goals, beliefs, constraints and actions can provide a model for explaining character behavior, but intelligibility of motive is not the same outcome as empathy, liking or believability.
**Support / contradiction:** The evaluation concerns explanations for actions; broader affective claims would exceed its measures.
**Sources / exact locators:** GDR-SRC-20261010-W01-08: §§5.2–5.3, printed pp. 245–251.
**Applicability:** Scenes where the player is intended to infer why a character acted.
**Confidence:** moderate for the outcome distinction; low for transferring the model to every character.
**Unresolved:** How to preserve productive mystery, impulse, habit, failed goals and noninstrumental behavior.

<a id="claim-c-03"></a>
### C-03 — empirical-evidence
The inspected intention-aware narrative-planning evaluation gives limited, mixed support for action-explanation comprehension, not broad proof of better game characters.
**Support / contradiction:** Small classroom sample, different generated texts, goal-exposition confound and mixed one-tailed comparisons restrict inference; see the evidence box.
**Sources / exact locators:** GDR-SRC-20261010-W01-08: printed pp. 245–252, evaluation and discussion.
**Applicability:** Reading one of two generated text stories, not playing a game.
**Confidence:** moderate — direct evaluation with disclosed limits; low for real-game outcomes.
**Unresolved:** Independent replication, matched exposition, other populations and affective/player-choice outcomes.

<a id="claim-c-04"></a>
### C-04 — practitioner-heuristic
Believability need not mean photorealism, moral goodness or exhaustive psychological simulation; stylized expressive choices are one possible approach.
**Support / contradiction:** Bates supplies an animation-informed conception. Its stronger assertions about emotional expression are not adopted as universal requirements.
**Sources / exact locators:** GDR-SRC-20261010-W01-10: §1 Believability and §2 The Role of Emotion, printed pp. 1–2.
**Applicability:** Stylized characters and authoring choices about how to suggest an inner life.
**Confidence:** moderate for the reported conception; low for any universal player effect.
**Unresolved:** Cultural variation and characters whose affect is subtle, inaccessible, deliberately opaque or atypical.

<a id="claim-c-05"></a>
### C-05 — practitioner-heuristic
A character may have meaningful limits and refuse the protagonist; this can express an intended relationship without granting the player power to resolve every problem.
**Support / contradiction:** Firsthand writing intent supports refusal as a chosen technique. It does not establish that players experience the restriction as fair or satisfying.
**Sources / exact locators:** GDR-SRC-20261010-W01-09: Brisbane Murri-girl letter/refusal account.
**Applicability:** Characters whose independent commitments or boundaries are part of the intended experience.
**Confidence:** moderate for the creator account; low for effects outside that context.
**Unresolved:** When refusal reads as characterization, misleading affordance, insensitive framing or a broken task.

<a id="claim-c-06"></a>
### C-06 — practitioner-heuristic
Relationship-dependent actions are an available characterization approach, but authored social rules should not be treated as universal descriptions of human relationships.
**Support / contradiction:** The creator account supports the technique’s existence; general social validity and player outcomes are not tested in the inspected passage.
**Sources / exact locators:** GDR-SRC-20261010-W01-11: PDF p. 1, Demonstration Description.
**Applicability:** Experiences that need reactions to changing obligations, status or relationships.
**Confidence:** moderate for the reported approach; low for broader effects.
**Unresolved:** Whether a simplified rule invites reductive, transactional or stereotyped interpretations.

<a id="claim-c-07"></a>
### C-07 — inference
Capabilities and action-linked communication can carry characterization even when extensive dialogue or biography is absent.
**Support / contradiction:** Independent creator descriptions suggest this route; the bridge from ability/communication to a particular player interpretation is not measured.
**Sources / exact locators:** GDR-SRC-20261010-W01-12: Features: Nuna/Fox skill contrast; GDR-SRC-20261010-W01-13: PDF p. 25, Vocalizations.
**Applicability:** Short sessions, small casts and experiences focused on coordination or performance.
**Confidence:** moderate as an authoring possibility; low as a guaranteed attachment effect.
**Unresolved:** Whether players perceive a person/relationship, a useful tool, a stereotype or no characterization at all.

<a id="claim-c-08"></a>
### C-08 — hypothesis
A practical character specification can separate desire, belief, capability, competing commitments, relationship stance, change conditions and evidence available to the player.
**Support / contradiction:** Original W01 authoring framework informed by limited sources; not a psychological theory or validated narrative template.
**Sources / exact locators:** GDR-SRC-20261010-W01-08: action-explanation model and evaluation limits; GDR-SRC-20261010-W01-09: limits of protagonist intervention.
**Applicability:** Situations where behavior and change must remain interpretable across alternatives.
**Confidence:** low — operational proposal requiring production and player evaluation.
**Unresolved:** Whether the framework becomes too rationalistic or overdocuments a deliberately minimal character.

<a id="claim-c-09"></a>
### C-09 — inference
A character can change in capability, belief, relationship or interpretation without a compulsory moral transformation; staying committed can itself be the intended outcome.
**Support / contradiction:** Distinguishes possible design outcomes rather than asserting an empirical taxonomy. The planning model’s limits caution against equating intentional action with inevitable goal success.
**Sources / exact locators:** GDR-SRC-20261010-W01-08: printed pp. 252–253, limits on modeling failed intentions.
**Applicability:** Stable, episodic, tragic, enigmatic or player-authored characters as well as changing ones.
**Confidence:** moderate as a conceptual distinction; low as guidance about audience preference.
**Unresolved:** Which kind of change the work invites the audience to expect and how that expectation is communicated.

<a id="claim-c-10"></a>
### C-10 — hypothesis
Ethical/access review should not require trauma, romantic availability, conventional emotional display or one character’s authority to stand for an entire community.
**Support / contradiction:** Proposed review questions, not a claim that the sources establish universal moral or accessibility rules. Community approval is not inferred from this synthesis.
**Sources / exact locators:** GDR-SRC-20261010-W01-09: NPC perspective and refusal argument; GDR-SRC-20261010-W01-12: collaboration description; GDR-SRC-20261010-W01-10: §§1–2, scope-limited believability account.
**Applicability:** Characters drawing on real identities, relationships or recognizable access needs.
**Confidence:** low — normative design proposal needing situated review.
**Unresolved:** Whose interpretation and harms are at stake, and what relevant participation is missing.

<a id="claim-c-11"></a>
### C-11 — inference
Localizers and presentation designers need the character’s relationship, intended uncertainty and reason for an action, not only isolated lines or trait adjectives.
**Support / contradiction:** Practitioner context guidance motivates the handoff; the exact character-note structure and access adaptations are W01 proposals.
**Sources / exact locators:** GDR-SRC-20261010-W01-15: printed pp. 17–20, Familiarization; Glossary and Style Guide; Voice-Over Recording; GDR-SRC-20261010-W01-14: narrative review guidance.
**Applicability:** Localized or multimodal characterization, including returning-player support.
**Confidence:** moderate for context dependency; low for particular delivery effects.
**Unresolved:** Whether the chosen channel changes ambiguity, politeness, status or perceived willingness.

<a id="claim-c-12"></a>
### C-12 — hypothesis
Evaluate causal interpretation, affect, perceived autonomy and access separately; a disliked or mysterious character is not automatically a failed design.
**Support / contradiction:** Proposed evaluation prevents one measure being substituted for another. No validated composite score or player test is claimed.
**Sources / exact locators:** GDR-SRC-20261010-W01-08: evaluation measure and confounds; GDR-SRC-20261010-W01-09: refusal account.
**Applicability:** Local goals ranging from cooperation and attachment to discomfort or uncertainty.
**Confidence:** low — falsifiable evaluation proposal.
**Unresolved:** Appropriate local measures, recruitment and interpretation of deliberate disagreement.

## References

All access dates are **2026-10-10**. Source identities below are run-scoped candidates, not global SRC allocations. Reuse within W01 is intentional; cross-batch URL/DOI/edition deduplication remains pending. Locators describe material actually inspected, not a claim that the entire linked work or game was examined.

<a id="source-08"></a>
### GDR-SRC-20261010-W01-08
**Mark O. Riedl; R. Michael Young. _Narrative Planning: Balancing Plot and Character_.** Journal of Artificial Intelligence Research 39, pp. 217–268. Publication/update: 2010; inspected arXiv deposit dated 2014-01-16.
**Inspected route:** [Narrative Planning: Balancing Plot and Character](https://arxiv.org/pdf/1401.3841).
**DOI:** `10.1613/jair.2989`.
**Edition/build:** Author-hosted/deposited journal paper; publication year differs from deposit year. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** §§5.2–5.3, printed pp. 245–251; conclusions and limitations, pp. 252–253.
**Source type:** Primary technical paper with an empirical comprehension evaluation. **Claims in this entry:** C-02, C-03, C-08, C-09, C-12.
**Limits:** Undergraduate text-story evaluation; story-length/goal-exposition differences; mixed one-tailed results. Not evidence of game empathy, character liking or production savings.
**Independence/provenance:** Shares Young with source 03; different experiment, not independent replication of agency findings.
**Rights:** © 2010 AI Access Foundation in paper. No source PDF or figures reproduced.

<a id="source-09"></a>
### GDR-SRC-20261010-W01-09
**Meghna (Meg) Jayanth. _Forget Protagonists: Writing NPCs with Agency for 80 Days and Beyond_.** Author-published talk text on Medium. Publication/update: 2016-06-05; text of GDC 2016 talk.
**Inspected route:** [Forget Protagonists: Writing NPCs with Agency for 80 Days and Beyond](https://medium.com/@betterthemask/forget-protagonists-writing-npcs-with-agency-for-80-days-and-beyond-703201a2309).
**Edition/build:** Published talk text; video not watched; game build/platform not inspected. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** Opening agency argument; Artificers’ Guild account; Brisbane encounter with the Murri girl and letter/refusal.
**Source type:** Primary creator account and practitioner argument. **Claims in this entry:** C-05, C-08, C-10, C-12.
**Limits:** Firsthand writing account supports reported intentions, not player-effect causation. Quoted forum reactions are not a representative study. No claim about actual runtime behavior verified.
**Independence/provenance:** Independent creator account; examples of other studios’ games inside the talk are not adopted as firsthand evidence here.
**Rights:** Copyrighted material; redistribution permission not established. Paraphrase only; no source assets included.

<a id="source-10"></a>
### GDR-SRC-20261010-W01-10
**Joseph Bates. _The Role of Emotion in Believable Agents_.** Carnegie Mellon University, technical report CMU-CS-94-136. Publication/update: 1994-04.
**Inspected route:** [The Role of Emotion in Believable Agents](https://acordo.net/acordo/wp-content/uploads/2020/08/Role-of-Emotion-in-Believable-AgentsBATES.pdf).
**Identity/publisher route:** [record or alternate route](https://www.cs.cmu.edu/afs/cs.cmu.edu/project/oz/web/papers.html).
**Edition/build:** Technical report; later Communications of the ACM version not treated as inspected. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** §1 Believability, printed p. 1 / PDF p. 3; §2 The Role of Emotion, printed p. 2 / PDF p. 4.
**Source type:** Primary researcher/practitioner position paper. **Claims in this entry:** C-01, C-04, C-10.
**Limits:** Animation-informed account, not a controlled player study. Assertions about required emotional expression are not adopted as universal or culturally neutral.
**Independence/provenance:** Independent older research line; animation sources cited within it were not independently inspected.
**Rights:** Copyrighted material; redistribution permission not established. Paraphrase only; no source assets included.

<a id="source-11"></a>
### GDR-SRC-20261010-W01-11
**Josh McCoy; Mike Treanor; Ben Samuel; Aaron A. Reed; Michael Mateas; Noah Wardrip-Fruin. _Prom Week_.** AAAI, AIIDE 9(1), demonstration paper. Publication/update: 2013-10-19.
**Inspected route:** [Prom Week](https://cdn.aaai.org/ojs/12662/12662-52-16179-1-2-20201228.pdf).
**DOI:** `10.1609/aiide.v9i1.12662`.
**Identity/publisher route:** [record or alternate route](https://ojs.aaai.org/index.php/AIIDE/article/view/12662).
**Edition/build:** Two-page demonstration paper; game version not independently inspected. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** PDF p. 1, Demonstration Description and social-interaction description.
**Source type:** Primary creator/system demonstration account. **Claims in this entry:** C-06.
**Limits:** No controlled outcome study in the inspected passage. Marketing-like claims of universal meaningfulness or priority are excluded.
**Independence/provenance:** Shares Mateas and Wardrip-Fruin with source 01; no independent player-effect corroboration.
**Rights:** © 2013 AAAI. Diagram and PDF not redistributed.

<a id="source-12"></a>
### GDR-SRC-20261010-W01-12
**Never Alone / E-Line Media. _Never Alone (Kisima Ingitchuna)_.** Official game website. Publication/update: unknown; live page inspected 2026-10-10.
**Inspected route:** [Never Alone (Kisima Ingitchuna)](https://www.neveralonegame.com/never-alone).
**Edition/build:** Unversioned official description; no game build or embedded video inspected. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** Game overview; Iñupiat collaboration and narration paragraphs; complementary Nuna/Fox abilities.
**Source type:** Primary publisher/creator description. **Claims in this entry:** C-01, C-07, C-10.
**Limits:** Promotional self-report. Does not establish community-wide endorsement, cultural accuracy across groups or causal player outcomes.
**Independence/provenance:** Independent of source 09, but a different cultural/production context rather than replication.
**Rights:** Copyrighted material; redistribution permission not established. Paraphrase only; no source assets included.

<a id="source-13"></a>
### GDR-SRC-20261010-W01-13
**Michael Booth, Valve. _Replayable Cooperative Game Design: Left 4 Dead_.** Valve, GDC 2009 presentation. Publication/update: 2009-03.
**Inspected route:** [Replayable Cooperative Game Design: Left 4 Dead](https://cdn.akamai.steamstatic.com/apps/valve/2009/GDC2009_ReplayableCooperativeGameDesign_Left4Dead.pdf).
**Identity/publisher route:** [record or alternate route](https://www.valvesoftware.com/en/publications).
**Edition/build:** 71-page slide deck; no current build inspected. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** PDF p. 25: Requiring Cooperation — Vocalizations; PDF p. 34: Designing for Dramatic Potential — Structured Unpredictability.
**Source type:** Primary development presentation. **Claims in this entry:** C-01, C-07.
**Limits:** Creator rationale, not controlled evidence of drama or cooperation effects. No architecture or numerical tuning recommendation imported.
**Independence/provenance:** Independent development account; not a replication of text-choice or character studies.
**Rights:** Valve presentation; no source slides or game images redistributed.

<a id="source-14"></a>
### GDR-SRC-20261010-W01-14
**Microsoft. _Xbox Accessibility Guideline 109: Objective clarity_.** Microsoft Learn. Publication/update: updated 2026-03-04.
**Inspected route:** [Xbox Accessibility Guideline 109: Objective clarity](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/109).
**Edition/build:** Web guideline revision checked 2026-10-10. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** Goal; Overview; Scoping questions; implementation guidance on task records and narrative review/recaps.
**Source type:** Primary vendor accessibility guidance. **Claims in this entry:** C-11.
**Limits:** Advisory design guidance, not asserted to be a certification requirement or universally applicable formal standard. No referenced game videos inspected.
**Independence/provenance:** Different evidence function from creative accounts; not empirical confirmation of the proposed recap design.
**Rights:** Microsoft Learn content; specific license terms not inspected. Paraphrase only.

<a id="source-15"></a>
### GDR-SRC-20261010-W01-15
**IGDA Game Localization SIG; Richard Honeywood (initial draft); Jon Fung (second draft); 2021 repost courtesy Wesley Bishop. _Best Practices for Game Localization_.** International Game Developers Association. Publication/update: initial draft 2011-02-01; second draft 2012-02-01; edited repost 2021-04-09.
**Inspected route:** [Best Practices for Game Localization](https://igda-website.s3.us-east-2.amazonaws.com/wp-content/uploads/2021/04/09142137/Best-Practices-for-Game-Localization-v22.pdf).
**Identity/publisher route:** [record or alternate route](https://igda.org/resources-archive/best-practices-for-game-localization/).
**Edition/build:** Cover identifies second draft 2012; filename v22 is not used to infer a verified semantic version. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** Printed pp. 16–20 / PDF pp. 19–23: Advice for Development Teams; Familiarization; Glossary and Style Guide; Voice-Over Recording.
**Source type:** Primary practitioner working-group guidance. **Claims in this entry:** C-11.
**Limits:** Dated workflow advice, not a current technical standard or measured cost experiment. Legacy encoding/platform examples and numerical prescriptions excluded.
**Independence/provenance:** Independent working-group advice; not a causal player study.
**Rights:** Copyrighted material; redistribution permission not established. Paraphrase only; no source assets included.

## Open questions and change history

Open items: `W01-CON-03` (goal intelligibility versus productive opacity/expressivity) and `W01-CON-05` (access support versus intended uncertainty). The strongest empirical source concerns text-story action comprehension, not interactive attachment. No universal character arc, personality trait count, emotional-expression requirement or approval of representation is supported.

**2026-10-10 — 0.1.0 draft, initial candidate.** Author self-review only; independent evidence/content review and actual host retrieval tests are pending. Gates C, D and E are not declared passed. See the [review packet](../reviews/full-run-20261010-w01-review-packet.md) for claim/source coverage and unresolved dependencies.

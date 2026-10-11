---
id: GDR-CAND-20261010-W01-TOP-01
kind: topic
title: Narrative structures
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
- branching narrative
- story structure
- systemic narrative
- emergent narrative
- narrative agency
- consequence
tags:
- agency
- continuity
- choice
- production-scope
- re-entry
- interpretation
related_topics:
- GDR-CAND-20261010-W01-TOP-02
- GDR-CAND-20261010-W01-TOP-03
related_patterns:
- GDR-CAND-20261010-W01-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-W01-01
- GDR-SRC-20261010-W01-02
- GDR-SRC-20261010-W01-03
- GDR-SRC-20261010-W01-04
- GDR-SRC-20261010-W01-05
- GDR-SRC-20261010-W01-06
- GDR-SRC-20261010-W01-11
- GDR-SRC-20261010-W01-13
- GDR-SRC-20261010-W01-14
- GDR-SRC-20261010-W01-15
lead_only_source_ids: []
reviewer: null
approved_by: null
approved_date: null
---

# Narrative structures

**Research candidate — not released guidance.** This file is complete for bounded W01 drafting, not a claim of exhaustive coverage or accepted evidence. Human research authorization does not approve this entry’s conclusions, game adoption, implementation, publication or permanent identity. No prototype, game execution, participant recruitment or player test was performed.

## Decision and scope

**Decision:** What must be authored, what may vary, and what influence can the player reasonably expect? The entry helps choose between a fixed sequence, authored divergence, conditional recombination and interactions from which a story may be interpreted. It covers action-light and action-heavy play, short sessions, shared play and text-led experiences without making any of them the default. It does not prescribe dialogue syntax, quest implementation, generation architecture, engine ownership or a particular game’s canon. [C-01; GDR-SRC-20261010-W01-04; GDR-SRC-20261010-W01-05; GDR-SRC-20261010-W01-06] [C-02; GDR-SRC-20261010-W01-01]

The working question is not “How do we add more branches?” It is: **“Which events, relationships, interpretations or opportunities may this player change, and which remain outside that role?”** More possible endings is one option, not a proxy for narrative quality. A fixed ending can support a chosen manner of acting; it cannot honestly satisfy a specific promise that the player can prevent that ending. This distinction is a proposed design discipline rather than a proven formula. [C-07; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-04]

### Working vocabulary

| Term | Use in this entry | Important boundary |
|---|---|---|
| Linear structure | A relevant sequence of events has an authored order and outcome. | Movement, performance, discovery order and interpretation may still vary. |
| Branching structure | Authored alternatives lead to different events, states, relationships or endings. | A branch may rejoin another path; this need not erase every consequence. |
| Systemic narrative | Rules and conditions make narrative situations or reactions depend on changing circumstances. | A selection rule is not automatically an emergent story, and it need not be implemented as an autonomous-agent simulation. |
| Emergent narrative | An intelligible account is formed from interacting events rather than wholly specified as that exact sequence in advance. | Randomness alone does not establish causality, stakes or a story a player values. |
| Agency | The player’s situated capacity to pursue a kind of intention within the experience’s supported actions. | Separate actual influence, felt influence, understanding and desired influence; none is simply success or unlimited control. |
| Consequence | A relevant difference following an action, including changed opportunity, relationship, information or acknowledged expression. | An acknowledgment can matter, but is not interchangeable with every promised change in the world. |

These are explicit working definitions, not a formal standard. Different scales can use different structures: a fixed session deadline, variable local encounters and an emergent rivalry are compatible. [C-01; GDR-SRC-20261010-W01-04; GDR-SRC-20261010-W01-05; GDR-SRC-20261010-W01-06] [C-02; GDR-SRC-20261010-W01-01]

## Core explanation and mechanisms

### Promise, action, persistence and interpretation

A useful causal hypothesis has four separable links. The player first understands a possible influence; an action then selects or changes something; a later situation retains a relevant difference; the player finally attributes that difference to the action and cares about it. An author can verify a written dependency without proving the last link. A player can feel acknowledged without having changed the ending. A player can change a distant outcome without recognizing that influence. Treat these as different failure diagnoses. [C-07; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-04] [C-09; hypothesis]

The theoretical premise is narrow: Wardrip-Fruin and colleagues frame agency as a relation among player intentions, supported actions and an experience’s models/interfaces. That motivates matching an offered role to actual support; it does not prove a preferred branching structure. [C-02; GDR-SRC-20261010-W01-01]

### Evidence box: do not turn feedback into an equivalence claim

Fendt and colleagues compared branching, linear-with-tailored-feedback and minimally responsive online text stories. Seventy-nine people entered the branching condition; analysis used 52 who followed the selected comparable branch, alongside 54 feedback and 44 minimal-feedback participants. Recruitment and demographics differed. Most branching/feedback comparisons were nonsignificant, but a counterfactual-story item favored branching at reported *p* = .030. The paper did not broadly establish feedback’s superiority to minimal feedback. These are not equivalence tests, and durable trust was not measured. [C-03; GDR-SRC-20261010-W01-02]

Cardona-Rivera and colleagues studied 88 adults making six binary choices. Recruitment was by snowball methods; 95% reported more than five years of gaming. Ratings followed the outcome. Three original scales supported the examined ordering, while two did not; a modified scale omitted the last two choices. Analysis included exploratory decisions. This offers qualified support for consequential situation differences, not a rule that every choice must alter a plot branch. [C-04; GDR-SRC-20261010-W01-03]

**Evidence-to-application bridge:** Use these findings to resist both extremes—“only large branches count” and “acknowledgment is always enough.” Choose the consequence dimension deliberately, then test whether it remains intelligible and valued when its limits become visible. The studies do not establish that concealing reconvergence is an acceptable substitute for the influence a player was promised. [C-07; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-04] [C-11; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03]

### Authored order is not the same as discovered order

A fixed past can be distributed as evidence and reconstructed in different sequences. Here the design problem is access to a defensible interpretation, not whether the player can rewrite history. Conversely, freely ordered scenes can still funnel to an unchanged outcome. Audit discovery flexibility and causal influence separately. Jenkins’s embedded-narrative discussion supplies a conceptual basis, not a player-effect measurement. [C-08; GDR-SRC-20261010-W01-06]

### State selection is a means, not a quality guarantee

Ashwell describes branch-and-bottleneck forms; Short describes storylets through content, eligibility and effects. These are practical ways to represent alternatives and reuse context. They do not show that a large conditional content set is cheaper to review, localize or understand than a fixed scene sequence. [C-05; GDR-SRC-20261010-W01-04; GDR-SRC-20261010-W01-05]

Creator reports broaden the evidence beyond choice menus. The *Prom Week* demonstration describes social circumstances affecting interactions; Booth’s *Left 4 Dead* presentation describes constrained unpredictability as a source of dramatic potential. Both are accounts of approaches, not W01 observations or proof of universally satisfying emergence. [C-06; GDR-SRC-20261010-W01-11; GDR-SRC-20261010-W01-13]

## Design choices and alternatives

The following selection matrix is a **conditional proposal**, not a ranking. Its benefit/cost statements describe anticipated design consequences, not measured savings. [C-07; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-04] [C-09; hypothesis]

| Choice | Appropriate promise | Benefit sought | Cost, dependency and alternative |
|---|---|---|---|
| Fixed authored sequence | Witness, perform, interpret, master or express a role within events that need not change. | Reliable order and deliberate closure. | Must avoid implying unsupported control. Omit choices that only obstruct a desired performance; use optional interpretation instead. |
| Sustained divergence | The player can change a consequential event or future path. | Distinct follow-through when the difference is the point. | More exclusive material and continuity cases to maintain. Use a shorter divergent interval only when the later merge remains honest. |
| Consequence-preserving reconvergence | Different local actions matter while a later shared situation remains plausible. | Share a scene without discarding relevant history. | Conditional variations may cost more than expected. Exit to sustained divergence when histories cannot share the event. |
| Conditional story units | Situations should become available from circumstances, not only a fixed sequence. | React to knowledge, commitments or relationships. | Requires review of missing, repeated and mutually incompatible situations. A small fixed sequence may be safer when eligibility rules add little. |
| Systemic interaction | The player wants to experiment with relationships between actions and conditions. | Discover contingent outcomes and make personal accounts. | Requires intelligible dependencies and recovery from uninteresting combinations. Authored anchors or an explicit non-narrative framing are alternatives. |
| Minimal narrative framing | The primary promise does not require story development. | Preserve attention for performance, construction, competition or contemplation. | May leave desired motivation absent. Add only a role, stake or consequence that serves an identified need; a full arc is not mandatory. |

**Consequences have different horizons.** An immediate response, a later opportunity, a relationship that survives the session and an ending are different commitments. Choose a horizon the experience can actually show. Avoid inventing unseen long-term effects solely to defend an otherwise indistinguishable branch. A retrospective epilogue may be sufficient when retrospective interpretation is the promise, but not when the advertised benefit was a usable capability during play. [C-07; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-04] [C-09; hypothesis]

## Application process

1. **Diagnose the role.** Write the player’s intended influence in an ordinary sentence, together with what is intentionally outside it. Distinguish a controllable outcome from a desired but contestable objective. Capture disagreement among stakeholders instead of calling every kind of agency equally important. [C-02; GDR-SRC-20261010-W01-01] [C-07; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-04]
2. **Define the contrast.** For a representative decision, write two genuinely possible player actions and the resulting difference. Mark whether it is expression, evidence, event, relationship, access or closure. When there is no relevant difference, identify why the interaction exists. It may still serve expression; do not relabel it world-changing. [C-09; hypothesis]
3. **Select structure at the right scale.** Choose the smallest interval that requires divergence, and identify any event that must remain shared. A common location is not by itself a reason for a common relationship or identical options. Use [Consequence-preserving reconvergence](../patterns/consequence-preserving-reconvergence.md) only when its prerequisites hold. [C-07; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-04]
4. **Specify continuity obligations.** Record who knows what, what has been promised, what opportunities changed, and what a player returning after an absence needs to recover. Describe observable obligations rather than storage formats, service owners or engine callbacks. [C-09; hypothesis] [C-10; GDR-SRC-20261010-W01-14; GDR-SRC-20261010-W01-15]
5. **Prepare a paper comparison.** Draft a small representative path set, including refusal, absence of an expected character, revisiting a place and no-change choices. Show the later consequence rather than ending the example immediately after the selection. This is a proposed next activity, not a prototype built in W01. [C-11; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03]
6. **Evaluate against the promise.** Ask what participants believed they could affect, what they think changed, whether later evidence supports that belief and whether the limit felt acceptable. Separate dislike of an outcome from misunderstanding or a broken commitment. [C-11; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03]
7. **Revise or remove.** Enlarge divergence only when the missing distinction matters. Otherwise reduce the promise, improve relevant evidence, simplify conditions or remove a choice. Do not repair every dissatisfaction with more text. [C-07; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-04]

## Patterns and genre adaptations

The supported extraction is [Consequence-preserving reconvergence](../patterns/consequence-preserving-reconvergence.md), `GDR-CAND-20261010-W01-PAT-01`, version 0.1.0 draft. It specifies the conditional case rather than recommending reconvergence by default.

Related W01 entries: [Worldbuilding](worldbuilding.md), `GDR-CAND-20261010-W01-TOP-02`, for coherence and evidence status; [Character design](character-design.md), `GDR-CAND-20261010-W01-TOP-03`, for goals, refusal and interpretation.

No genre file was assigned, supplied or authored. `templates/genre.md` was not available. Genre-owner work should later decide whether a particular audience promise changes these conditions; W01 does not assert a preferred structure for any genre. Narrative systems interfaces, decision design, evaluation, accessibility and localization remain dependency topics, not completed entries silently linked by invented IDs.

## Examples and counterexamples

### Illustrative worked example: the delayed relay

**Invented design example, not a game observation or test.** A small team must carry a report to a station before a scheduled broadcast. The broadcast time is fixed. The player can carry the intact transmitter or help a colleague transport a medical kit, but cannot carry both alone. The choice text promises a difference in what reaches the station—not control over the weather or broadcast deadline. [C-09; hypothesis]

In the transmitter history, long-range contact becomes possible but treating a minor injury requires assistance. In the medical-kit history, immediate treatment is available but the team must use a local messenger. Both histories reach the same meeting; the meeting presents different feasible plans and remembers who helped whom. The authored milestone remains linear while local consequence and relationships vary. No particular emotional benefit is assumed. [C-07; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-04]

**Counterexample:** Both histories arrive, a previously unmentioned stranger supplies whichever item is missing, and all later options and relationships become identical. That might fit a tale about external rescue, but it does not fulfill the stated promise that the delivery decision determines the team’s resources. A grateful line alone cannot repair that resource promise. Either revise the promise or allow the missing resource to matter. [C-07; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-04]

### Illustrative fixed history with active interpretation

An inspection task presents a damaged machine, two incompatible shift reports and a repair invoice. The accident already occurred. Players may inspect these in any order and recommend an explanation, including “insufficient evidence.” The application can support active interpretation without pretending the accident is causally changeable. Making every inspected document alter the past would change the design question, not automatically improve it. [C-08; GDR-SRC-20261010-W01-06]

### Illustrative minimal case and opposing aesthetic

A brief timing challenge uses recurring opponents and a ceremonial finish. Its promise may be performance and recognition, not multiple destinies. Additional branching dialogue can be unnecessary. At the other extreme, a deliberately elusive piece may invite unresolved interpretation rather than a reliable account of every dependency. The proposed audit should protect the intended experience, not require an explanation for every ambiguity. [C-07; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-04]

No named game in this entry was played, recorded, instrumented or inspected by build. The verified artifacts are the cited documents; reported creator intent and invented examples remain distinct.

## Failure modes and constraints

**Comprehension and access.** An important difference can disappear because the player missed its sole presentation, forgot a commitment or cannot access a channel. Consider an optional record of known information and outstanding promises, preserving uncertainty about unknown facts. Do not equate memory difficulty with lack of narrative sophistication. Multimodal delivery belongs to Presentation and Interaction; W01 only identifies the information that must remain recoverable. [C-10; GDR-SRC-20261010-W01-14; GDR-SRC-20261010-W01-15]

**Localization.** A reused scene can require different referents, forms of address, tense and knowledge assumptions for different histories. Provide the localizer with speaker, addressee, relationship, relevant prior events and what must remain uncertain. Do not assume that swapping a short fragment preserves grammar, tone or ambiguity across languages. The recommendation is a contextual authoring handoff, not a string-system design. [C-10; GDR-SRC-20261010-W01-14; GDR-SRC-20261010-W01-15]

**Ethics and shared agency.** A morally loaded choice may conflate the player’s preference with the character’s permitted action. Make role limits intelligible; offer refusal where consistent with the intended design. In shared play, distinguish who may decide, who bears consequences and how dissent is represented. These are proposed questions, not evidence that a particular voting or consent procedure works universally. [C-09; hypothesis]

**Production and reliability.** Reconvergence can save duplicated scene material while increasing conditional review. A huge nominal branch count says little about total effort. Conversely, keeping all history forever can make a small project harder to maintain. Scope consequence to a demonstrable horizon, record intentional resets and disclose when the experience is episodic. No budget multiplier or universal state-count limit is claimed. [C-07; GDR-SRC-20261010-W01-01; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-04] [C-09; hypothesis]

**Interpretive plurality.** A test should not fail simply because players draw different themes from the same events. Look instead for a mismatch relevant to the promised influence: false beliefs about available actions, consequences attributed to the wrong cause, or a felt bait-and-switch after the structure becomes visible. [C-11; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03]

## Playtest and validation

**Status: proposed; not performed.** No materials were executed, participants recruited, sessions observed or results generated in W01.

**Question:** Does a chosen structure preserve the influence players expect and value without unacceptable comprehension or production cost? Compare a truthful fixed-sequence version, a stateful reconvergent version and a sustained-divergence version only where all three can express the same core premise. If they cannot, report the mismatched premise instead of calling the test controlled. [C-11; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03]

Use comparable stakes, prose quality, interaction effort, exposure time and access support. Obtain an account of expected influence before the outcome, then a separate account after a meaningful follow-up. Add replay or a disclosed alternative-path comparison where durable trust matters. Counterbalance or assign conditions appropriately; repeated exposure changes expectations and cannot be ignored. [C-11; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03]

Recruit for the intended languages, familiarity, access needs and tolerance for uncertainty. Analyze understanding of cause, perceived influence, importance of the difference, trust after disclosure and desire for closure separately. Record authoring/revision and continuity-review effort separately from player preference. A larger-looking branching graph is not an outcome measure. [C-11; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03]

**Decision rule proposal:** Define the local promise and unacceptable mismatch before testing. A reproducible instance where the design offers prevention but cannot allow prevention is a specification failure even if satisfaction averages are high. Retain reconvergence only if the valued consequence survives and the measured production tradeoff is acceptable; otherwise change the promise, lengthen divergence or simplify. Do not infer equivalence from a nonsignificant difference. Sample size and quantitative acceptance margins require a later study design and approval, not a fabricated universal threshold. [C-11; GDR-SRC-20261010-W01-02; GDR-SRC-20261010-W01-03]

## Claim ledger

Claim IDs are local to this file. Class and confidence are separate. Proposed applications and tests are not approved studio decisions or performed research. A source attached to an inference identifies its premises, not a direct test of the recommendation.

<a id="claim-c-01"></a>
### C-01 — inference
For W01, linear, branching, systemic and emergent describe different aspects of narrative organization; they are not mutually exclusive quality ranks.
**Support / contradiction:** Working synthesis of practitioner and theoretical distinctions; no universally agreed four-way standard established.
**Sources / exact locators:** GDR-SRC-20261010-W01-04: opening qualification and Branch and Bottleneck; GDR-SRC-20261010-W01-05: opening storylet definition; GDR-SRC-20261010-W01-06: Embedded Narratives; Emergent Narratives.
**Applicability:** Describing event order, selection and player interpretation at a specified scale.
**Confidence:** moderate — useful distinctions supported by multiple conceptual accounts, not validated as an exhaustive taxonomy.
**Unresolved:** Whether the vocabulary routes reliably for designers outside text-led and authored-story contexts.

<a id="claim-c-02"></a>
### C-02 — inference
Agency should be evaluated against the kind of influence offered and desired, rather than inferred from a count of selectable options or endings.
**Support / contradiction:** The relational account supplies the premise; the proposed influence audit is W01 application, not an experimental result.
**Sources / exact locators:** GDR-SRC-20261010-W01-01: PDF pp. 1–6, agency/model/interface discussion.
**Applicability:** Experiences that communicate some actionable role to the player.
**Confidence:** moderate — clear theoretical rationale; magnitude and audience dependence untested here.
**Unresolved:** Which influence dimensions a local audience actually values, including expression without changing events.

<a id="claim-c-03"></a>
### C-03 — empirical-evidence
The inspected 2012 study does not establish that immediate tailored feedback is equivalent to lasting branching, or broadly superior to minimal feedback.
**Support / contradiction:** Mostly nonsignificant comparisons do not establish equivalence; the authors did not establish their second hypothesis broadly. See the evidence box for design and sample limits.
**Sources / exact locators:** GDR-SRC-20261010-W01-02: PDF pp. 4–10, §§3–5; Tables 1–2 and hypothesis-two discussion.
**Applicability:** A short online text-story study, not all games or repeated play.
**Confidence:** high for this cautious reading of the reported comparisons; low for generalization.
**Unresolved:** Durable trust, replay discovery and the consequences of explicit promises of world change.

<a id="claim-c-04"></a>
### C-04 — empirical-evidence
The inspected 2014 experiment provides qualified, uneven support for differences between narrative situations being associated with greater reported agency.
**Support / contradiction:** Within-participant retrospective ratings and exploratory decisions prevent a universal causal rule; some scales did not support the proposed ordering.
**Sources / exact locators:** GDR-SRC-20261010-W01-03: printed pp. 10–14; Tables 3–6; limitations.
**Applicability:** Six binary choices in an online text narrative with an experienced-gamer-heavy sample.
**Confidence:** moderate — directly reported results, with important analysis and sampling limits.
**Unresolved:** Prospective expectations before outcomes, replication, non-English contexts and lasting significance.

<a id="claim-c-05"></a>
### C-05 — practitioner-heuristic
Branch reconvergence and conditional story units are available authoring alternatives; neither guarantees lower total production cost or meaningful consequence.
**Support / contradiction:** Practitioner descriptions support the availability of these techniques; cost and quality benefits require separate evidence.
**Sources / exact locators:** GDR-SRC-20261010-W01-04: Branch and Bottleneck; GDR-SRC-20261010-W01-05: opening definition; Common Branching Structures and Storylets.
**Applicability:** Content with reusable events and authorable conditions/effects.
**Confidence:** moderate — explicit craft accounts, no measured total-cost comparison.
**Unresolved:** How much downstream variation and testing a specific team can actually sustain.

<a id="claim-c-06"></a>
### C-06 — practitioner-heuristic
Creator accounts illustrate narrative potential through social-state interaction and constrained event variability, not proof that every generated sequence is a satisfying story.
**Support / contradiction:** Firsthand descriptions of design intent; no independently observed game session or causal player study in W01.
**Sources / exact locators:** GDR-SRC-20261010-W01-11: PDF p. 1, Demonstration Description; GDR-SRC-20261010-W01-13: PDF p. 34, Structured Unpredictability.
**Applicability:** Systems whose interactions can be interpreted as events with stakes or relationships.
**Confidence:** moderate for the reported approaches; low for player outcomes.
**Unresolved:** When variability produces unintelligible causality, repetition or unsatisfying closure.

<a id="claim-c-07"></a>
### C-07 — hypothesis
Choose the least elaborate structure that can honestly preserve the influence, continuity and uncertainty the experience promises; reduce the promise or change the structure when they conflict.
**Support / contradiction:** The sources motivate scope-sensitive design, but do not test this full selection rule. Simplicity is a proposed production criterion, not a universal aesthetic priority.
**Sources / exact locators:** GDR-SRC-20261010-W01-01: PDF pp. 1–6; GDR-SRC-20261010-W01-02: PDF pp. 9–10; GDR-SRC-20261010-W01-04: Branch and Bottleneck.
**Applicability:** Bounded authoring decisions with declared player-facing goals and actual production constraints.
**Confidence:** low — actionable synthesis awaiting comparative evaluation.
**Unresolved:** Whether a simpler structure loses expressive richness or replay value even when its promises are technically met.

<a id="claim-c-08"></a>
### C-08 — inference
Separate event chronology from discovery order; a player may reconstruct a fixed past without being offered power to change it.
**Support / contradiction:** The distinction between embedded history and its presentation supports this separation; calling reconstruction meaningful is conditional, not guaranteed.
**Sources / exact locators:** GDR-SRC-20261010-W01-06: Embedded Narratives.
**Applicability:** Investigation, exploration, retrospective interpretation and optional background across forms.
**Confidence:** moderate — conceptually direct; no universal player preference inferred.
**Unresolved:** Whether the player mistakes interpretive access for promised intervention.

<a id="claim-c-09"></a>
### C-09 — hypothesis
A bounded continuity and consequence specification can make later choices auditable, but it should describe player-visible obligations rather than assign runtime ownership.
**Support / contradiction:** Original authoring proposal: track promise, alternatives, remembered consequences, compatible later events and exceptions. No process-efficiency experiment performed.
**Sources / exact locators:** Original W01 design proposal; no external validation claimed..
**Applicability:** Shared work between narrative, mechanics, QA and presentation owners.
**Confidence:** low — plausible workflow, unvalidated as a production improvement.
**Unresolved:** Whether maintaining the specification costs more than it prevents in a small project.

<a id="claim-c-10"></a>
### C-10 — inference
Optional, spoiler-bounded re-entry support and contextual localization handoffs are worth testing where comprehension or production continuity matters.
**Support / contradiction:** Advisory accessibility and localization sources motivate the needs; the particular spoiler-bound design is a W01 inference.
**Sources / exact locators:** GDR-SRC-20261010-W01-14: narrative review and task-record guidance; GDR-SRC-20261010-W01-15: printed pp. 16–20, Familiarization; Glossary and Style Guide.
**Applicability:** Interrupted play, cognitive/reading access needs and localized conditional content.
**Confidence:** moderate for the need to consider access/context; low for the proposed compromise’s effects.
**Unresolved:** Whether a recap overexplains intended uncertainty or still withholds information needed for an informed action.

<a id="claim-c-11"></a>
### C-11 — hypothesis
The proposed comparisons should measure accurate understanding of influence and later trust, not only immediate satisfaction or the number of apparent branches.
**Support / contradiction:** Addresses limits of the inspected short-form studies; the proposed procedure and decision criteria have not been run.
**Sources / exact locators:** GDR-SRC-20261010-W01-02: PDF pp. 9–11, results and discussion; GDR-SRC-20261010-W01-03: printed p. 14, limitations.
**Applicability:** Projects seeking persistent consequence, replay, informed choice or meaningful closure.
**Confidence:** low — evaluation proposal, not a validated measurement package.
**Unresolved:** Appropriate local recruitment, instruments, uncertainty targets and costs.

## References

All access dates are **2026-10-10**. Source identities below are run-scoped candidates, not global SRC allocations. Reuse within W01 is intentional; cross-batch URL/DOI/edition deduplication remains pending. Locators describe material actually inspected, not a claim that the entire linked work or game was examined.

<a id="source-01"></a>
### GDR-SRC-20261010-W01-01
**Noah Wardrip-Fruin; Michael Mateas; Steven Dow; Serdar Sali. _Agency Reconsidered_.** DiGRA 2009. Publication/update: 2009.
**Inspected route:** [Agency Reconsidered](https://www.cs.uky.edu/~sgware/reading/papers/wardripfruin2009agency.pdf).
**DOI:** `10.26503/dl.v2009i1.369`.
**Identity/publisher route:** [record or alternate route](https://dl.digra.org/index.php/dl/article/view/369).
**Edition/build:** Conference paper, nine-page university-hosted PDF; not a current game build. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** PDF pp. 1–6: Introduction; Agency and Drama; Agency and Software Models; Agency and Interfaces.
**Source type:** Primary theoretical paper. **Claims in this entry:** C-02, C-07.
**Limits:** Conceptual argument, not a comparative intervention study. Studies mentioned inside the paper were not independently inspected.
**Independence/provenance:** Shares Mateas and Wardrip-Fruin with source 11; that overlap is not independent corroboration.
**Rights:** © 2009 authors and DiGRA; educational/personal-use notice in paper. No republication rights assumed.

<a id="source-02"></a>
### GDR-SRC-20261010-W01-02
**Matthew William Fendt; Brent Harrison; Stephen G. Ware; Rogelio E. Cardona-Rivera; David L. Roberts. _Achieving the Illusion of Agency_.** Springer, ICIDS 2012, LNCS 7648, pp. 114–125. Publication/update: 2012.
**Inspected route:** [Achieving the Illusion of Agency](https://cs.uky.edu/~sgware/reading/papers/fendt2012achieving.pdf).
**DOI:** `10.1007/978-3-642-34851-8_11`.
**Identity/publisher route:** [record or alternate route](https://scholars.uky.edu/en/publications/achieving-the-illusion-of-agency/).
**Edition/build:** Twelve-page author PDF with internal page numbers 1–12. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** PDF pp. 4–11, §§3–6; Tables 1–2 on PDF p. 9; hypothesis-two result and discussion on PDF p. 10.
**Source type:** Primary empirical paper. **Claims in this entry:** C-03, C-07, C-11.
**Limits:** Selected-branch analysis, recruitment/condition demographic differences, optional item responses and short online text stories restrict causal/generalization claims; nonsignificance is not equivalence.
**Independence/provenance:** Shares four authors with source 03. Different study, not an independent replication.
**Rights:** Author manuscript of Springer publication; no source PDF redistributed.

<a id="source-03"></a>
### GDR-SRC-20261010-W01-03
**Rogelio E. Cardona-Rivera; Justus Robertson; Stephen G. Ware; Brent Harrison; David L. Roberts; R. Michael Young. _Foreseeing Meaningful Choices_.** AAAI, AIIDE 10(1), pp. 9–15. Publication/update: 2014-10-08.
**Inspected route:** [Foreseeing Meaningful Choices](https://cdn.aaai.org/ojs/12716/12716-52-16233-1-2-20201228.pdf).
**DOI:** `10.1609/aiide.v10i1.12716`.
**Identity/publisher route:** [record or alternate route](https://ojs.aaai.org/index.php/AIIDE/article/view/12716).
**Edition/build:** Seven-page conference paper; printed pp. 9–15. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** Printed pp. 10–14: experiment, results and limitations; Tables 3–6, especially Tables 5–6 on p. 13.
**Source type:** Primary empirical paper. **Claims in this entry:** C-04, C-11.
**Limits:** Snowball sample, retrospective judgments after outcomes, exploratory analysis decisions and uneven scale results. No preregistered equivalence or long-term trust result.
**Independence/provenance:** Overlaps authors with source 02 and Young with source 08. Treat as related research, not independent replication.
**Rights:** © 2014 AAAI. No figures, tables or source PDF reproduced.

<a id="source-04"></a>
### GDR-SRC-20261010-W01-04
**Sam Kabo Ashwell. _Standard Patterns in Choice-Based Games_.** These Heterogenous Tasks, author blog. Publication/update: 2015-01-26.
**Inspected route:** [Standard Patterns in Choice-Based Games](https://heterogenoustasks.wordpress.com/2015/01/26/standard-patterns-in-choice-based-games/).
**Edition/build:** Dated web essay; no numbered revision. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** Opening qualification; Branch and Bottleneck; Time Cave; Gauntlet; Open Map; Floating Modules.
**Source type:** Primary practitioner taxonomy. **Claims in this entry:** C-01, C-05, C-07.
**Limits:** Nonexhaustive craft taxonomy with overlapping forms; diagrams and games were not independently evaluated. Title does not make this a formal standard.
**Independence/provenance:** Source 05 explicitly draws on this topology vocabulary; do not count that reuse as independent evidence.
**Rights:** Copyrighted material; redistribution permission not established. Paraphrase only; no source assets included.

<a id="source-05"></a>
### GDR-SRC-20261010-W01-05
**Emily Short. _Storylets: You Want Them_.** Emily Short’s Interactive Storytelling, author blog. Publication/update: 2019-11-29.
**Inspected route:** [Storylets: You Want Them](https://emshort.blog/2019/11/29/storylets-you-want-them/).
**Edition/build:** Dated web essay; no numbered revision. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** Opening definition and three components; Common Branching Structures and Storylets.
**Source type:** Primary practitioner explanation. **Claims in this entry:** C-01, C-05.
**Limits:** Useful authoring description, not measured evidence that storylets reduce production cost or improve player experience.
**Independence/provenance:** Uses Ashwell/source 04 for branching vocabulary; no independent validation of that taxonomy.
**Rights:** Copyrighted material; redistribution permission not established. Paraphrase only; no source assets included.

<a id="source-06"></a>
### GDR-SRC-20261010-W01-06
**Henry Jenkins. _Game Design as Narrative Architecture_.** electronic book review. Publication/update: 2004-07-10 in article citation; page also displays 2004-05-03 metadata.
**Inspected route:** [Game Design as Narrative Architecture](https://electronicbookreview.com/publications/game-design-as-narrative-architecture/).
**Edition/build:** Inspected web essay, not the separately published book chapter. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** Opening numbered propositions; Enacting Stories; Embedded Narratives; Emergent Narratives.
**Source type:** Primary theoretical essay. **Claims in this entry:** C-01, C-08.
**Limits:** Interpretive framework, not a controlled player study. Its examples and cited books were not independently observed/read here. No universal three-exposure rule adopted.
**Independence/provenance:** Distinct author from other sources, but shares narratology traditions; not an independent experimental dataset.
**Rights:** Site footer states CC BY-ND 4.0. This package supplies attributed analysis, not a redistributed or modified copy of the article.

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

<a id="source-13"></a>
### GDR-SRC-20261010-W01-13
**Michael Booth, Valve. _Replayable Cooperative Game Design: Left 4 Dead_.** Valve, GDC 2009 presentation. Publication/update: 2009-03.
**Inspected route:** [Replayable Cooperative Game Design: Left 4 Dead](https://cdn.akamai.steamstatic.com/apps/valve/2009/GDC2009_ReplayableCooperativeGameDesign_Left4Dead.pdf).
**Identity/publisher route:** [record or alternate route](https://www.valvesoftware.com/en/publications).
**Edition/build:** 71-page slide deck; no current build inspected. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** PDF p. 25: Requiring Cooperation — Vocalizations; PDF p. 34: Designing for Dramatic Potential — Structured Unpredictability.
**Source type:** Primary development presentation. **Claims in this entry:** C-06.
**Limits:** Creator rationale, not controlled evidence of drama or cooperation effects. No architecture or numerical tuning recommendation imported.
**Independence/provenance:** Independent development account; not a replication of text-choice or character studies.
**Rights:** Valve presentation; no source slides or game images redistributed.

<a id="source-14"></a>
### GDR-SRC-20261010-W01-14
**Microsoft. _Xbox Accessibility Guideline 109: Objective clarity_.** Microsoft Learn. Publication/update: updated 2026-03-04.
**Inspected route:** [Xbox Accessibility Guideline 109: Objective clarity](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/109).
**Edition/build:** Web guideline revision checked 2026-10-10. **Access:** `relevant-excerpt`; 2026-10-10.
**Exact inspected locators:** Goal; Overview; Scoping questions; implementation guidance on task records and narrative review/recaps.
**Source type:** Primary vendor accessibility guidance. **Claims in this entry:** C-10.
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
**Source type:** Primary practitioner working-group guidance. **Claims in this entry:** C-10.
**Limits:** Dated workflow advice, not a current technical standard or measured cost experiment. Legacy encoding/platform examples and numerical prescriptions excluded.
**Independence/provenance:** Independent working-group advice; not a causal player study.
**Rights:** Copyrighted material; redistribution permission not established. Paraphrase only; no source assets included.

## Open questions and change history

Open items: `W01-CON-01` (feedback versus consequence), `W01-CON-04` (variability versus coherent drama), and `W01-CON-05` (access support versus intended opacity), all batch-local records in the [review packet](../reviews/full-run-20261010-w01-review-packet.md#contradictions). Long-term/replay effects, broader cultural coverage and comparative production costs remain unresolved.

**2026-10-10 — 0.1.0 draft, initial candidate.** Public-source research and author self-review completed for this bounded entry. No previous candidate overwritten; no canonical authority or supersession receipt asserted. Independent evidence review and actual host retrieval tests have not occurred; Gates C, D and E are not declared passed. Source identities await Library Coordination.

---
id: GDR-CAND-20261010-W04-TOP-03
kind: topic
title: Theme and meaning
version: 0.1.0
status: draft
owner_project: BH-GDR-Worlds-and-Characters
run_id: GDR-FULL-20261010
batch: W04
candidate_revision: initial-draft-1
attempt_id: W04-initial-1
updated: '2026-10-10'
evidence_checked: '2026-10-10'
coverage_status: open
aliases:
- thematic alignment
- ludonarrative dissonance
- interpretive openness
- symbolism
- creator-player disagreement
tags:
- theme
- meaning
- tone
- representation
- interpretation
- dissonance
- evidence-open
related_topics:
- GDR-CAND-20261010-W04-TOP-01
- GDR-CAND-20261010-W04-TOP-02
- GDR-CAND-20261010-W01-TOP-03
- GDR-CAND-20261010-F07-TOP-02
related_patterns: []
related_genres: []
source_ids:
- GDR-SRC-20261010-W04-007
- GDR-SRC-20261010-W04-006
- GDR-SRC-20261010-W04-005
- GDR-SRC-20261010-W04-008
- GDR-SRC-20261010-F07-014
- GDR-SRC-20261010-W01-09
- GDR-SRC-20261010-W01-12
permanent_id: null
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded W04 candidate; no prior batch replaced.
byte_hash_record: ../reviews/full-run-20261010-w04-review-packet.md#artifact-byte-manifest
---

# Theme and meaning

**Draft research candidate; not released or approved guidance.** All examples marked illustrative are invented, not studio canon. No game, engine, prototype, participant study or player test was run. Recommendations are conditional inferences or hypotheses, not formal standards.

## Decision and scope

This topic helps a designer examine **what a game’s actions, consequences, narrative and presentation might invite people to think or feel**, and decide whether to reinforce, complicate or deliberately oppose those readings. It does not identify the one correct interpretation, establish a game’s canon or treat an intended message as a demonstrated audience effect. [C-01]

For this draft, **theme** is a sustained question, tension or proposition that can organize attention across the experience. “Responsibility” is a subject; “who bears responsibility when an institution rewards compliance?” is a possible thematic question. **Meaning** includes interpretations people construct from what is offered and how they play. **Tone** is the attitude conveyed or perceived in the treatment of events. **Symbolism** is a proposed or perceived association between a detail and a wider idea. These are working distinctions, not universally accepted definitions or an approved studio vocabulary. [C-01]

Included are mechanics/narrative alignment, deliberate dissonance, tone, symbolism, representation, interpretive openness and creator/player disagreement. Excluded are a formula for emotional impact, universal cultural symbol mappings, a legal representation standard and runtime authoring architecture. The linked narrative-interface topic can help distinguish an accidental contradiction from an intentional one; it cannot certify what that contradiction means.

## Core explanation and mechanisms

### Four evidence objects must remain separate

| Evidence object | What it can support | What it does not automatically establish |
|---|---|---|
| Documented creator intent | A named creator’s stated aim in a particular production context. | That the shipped work expresses the aim, all collaborators shared it, or players receive it. |
| Directly inspected artifact or system evidence | What the inspected text, build, recording or document contains. | The intent behind it or a causal audience effect. A promotional paragraph is evidence about promotion, not a played scene. |
| Reader/player interpretation | A person’s account of how they understand the work and the evidence they use. | A universal reading, an objective game-state fact, or the creator’s private purpose. |
| Empirical reception evidence | Results for the studied people, materials and methods. | Unmeasured populations, long-term change or causation not supported by the design. |

This separation is the central recommendation. Its utility is an inference from the different kinds of claims, not proof that the proposed review method produces better art. Interpretation can be evidence-grounded without being the author’s preferred reading. Conversely, openness does not require treating an unsupported factual claim about the work as equally established. [C-02]

### Examine rules and play without reducing either to the other

Bogost argues that procedural representation can express claims, while allowing inquiry and disagreement rather than inevitable persuasion. Sicart challenges an analysis that sidelines players and asks for complementary attention to play. These are theoretical positions, not rival experimental results. It would misrepresent the inspected Bogost chapter to claim that it simply demands one obedient reading, and misrepresent Sicart’s conclusion to say rules are irrelevant. [C-03, C-04; GDR-SRC-20261010-W04-007; GDR-SRC-20261010-W04-006]

The application bridge is a **double account**: describe what actions and consequences the work makes available, then separately investigate how people interpret or appropriate them. A rule may create a strong incentive while a player deliberately refuses it, jokes about it, role-plays against it or attends mainly to something else. This possibility is not a license to ignore the rule; it is a reason not to infer a person’s meaning or values from completion alone. [C-05]

### Alignment is a choice, not a universal quality test

Working **alignment** means that relevant mechanics and narrative/presentation support compatible readings. **Dissonance** means they create a meaningful tension or conflict in a particular reading. Neither label decides whether the result is effective, ethical, intentional or appropriate for a given audience. A technically stale line and a deliberately unreliable narrator can both appear contradictory while requiring very different responses. [C-06]

Hocking’s BioShock essay is a primary account of his critical frustration with the relationship between offered power and required assistance. It is not the developer’s intent or a representative reception study. In a different evidence category, the official Ultra Deluxe press kit explicitly markets contradiction and constrained choice. That is evidence of published creative positioning, not evidence that every player finds deliberate contradiction rewarding. [C-07, C-08; GDR-SRC-20261010-W04-005; GDR-SRC-20261010-W04-008]

The conditional recommendation is to name **what the tension is meant to expose and which player understanding it assumes**. A work can intentionally undermine a narrator, a social institution or the player’s expectation of mastery. It still needs to consider whether people instead infer a defect, arbitrary punishment or authorial contempt. The fact that a contradiction was intended does not settle that question. [C-06, C-12]

### Representation is more than presence

The inspected GLAAD/Nielsen report offers scoped reception evidence: among LGBTQ respondents, 72% said well-represented characters matching their gender identity and/or sexual orientation make them feel better about themselves. The survey used a US active PC/console-player panel of 1,452, ages 13–55, with an LGBTQ boost, fielded June–August 2023. This is self-report, not randomized evidence that a particular design causes wellbeing. [C-09; GDR-SRC-20261010-F07-014]

A proposed design review should therefore distinguish presence from portrayal, agency, framing and consequences. Who can refuse, act, be mistaken, receive help or exist without serving the protagonist’s development? These are questions for analysis, not a numerical authenticity score. Jayanth’s creator account and the official Never Alone collaboration description supply possible approaches to perspectives and participation; neither is a universal endorsement of a representation method. [C-10, C-11; GDR-SRC-20261010-W01-09; GDR-SRC-20261010-W01-12]

## Design choices and alternatives

| Approach | When it may serve the local question | Tradeoff and contrary case |
|---|---|---|
| Reinforce a reading across action and consequence | The goal is to make a particular dilemma or relationship available for examination. | Repetition can become didactic or flatten exceptions. A single consequential scene may suffice. |
| Deliberately oppose narrative framing and incentives | The contradiction itself is part of the inquiry. | Players may read accidental incoherence or unfair blame. Establish the intended object of criticism and test alternatives. |
| Keep multiple perspectives unresolved | The question concerns competing values or incomplete testimony. | Unclear operational facts can make play confusing without adding interpretive depth. Separate uncertainty about truth from uncertainty about the controls or accepted action. |
| Use a recurring symbol or motif | An association can accumulate or change across contexts. | Repetition alone does not establish meaning. The association may be inaccessible, culturally different or unwanted. |
| Use explicit explanation | Some context is necessary for the intended examination or access. | An explanation can overdetermine a reading or conceal a weakly expressed relationship. Offer context without declaring a player’s reaction wrong. |
| Omit a thematic apparatus | The activity does not need a sustained proposition to meet its local purpose. | Omission does not mean value-free design, but not every mechanic needs a symbolic justification or moral lesson. |

All six are conditional authoring choices, not ranked evidence-based prescriptions. The counterproposal to a complex thematic audit is a smaller work with honest scope and a limited, careful audience review. No inspected source demonstrates that thematic complexity predicts commercial or artistic success. [C-05, C-06, C-12]

## Application process

1. **Write the question, not the answer key.** State the thematic tension and why the work might make it worth exploring. Record intended audience and context without assuming a genre label fixes interpretation. Keep this a proposal until the local creative owner approves it. [C-01, C-12]
2. **Describe what the player can actually do.** List consequential affordances, restrictions, incentives, costs and consequences. Distinguish common, optional and practically unreachable experiences. A synopsis alone cannot establish the relation between doing and being told. [C-03, C-05]
3. **Separate intent, evidence and readings.** Attribute each assertion to its proper evidence object. Record at least a plausible opposing reading and the textual/system evidence that could sustain it. Do not invent participant responses. [C-02, C-12]
4. **Choose alignment, tension or omission deliberately.** Describe the function of any mismatch. If it is accidental, fix the promise or action; if intentional, identify the audience assumptions needed to recognize it and the harms or confusion still possible. [C-06]
5. **Inspect tone and symbolism in context.** Examine placement, repetition, timing, speaker perspective and available alternate evidence. Ask what the same device might imply elsewhere; do not use a universal color, object or musical meaning as an unsupported shortcut. [C-13]
6. **Review representation and participation.** Examine who has agency, who carries the costs, whose interiority is absent and whose perspective becomes the default. When a work draws on a living culture or marginalized experience, propose appropriate participation, credit, compensation and revision authority rather than assuming research access equals permission or endorsement. This is a proposed studio-process safeguard, not a legal finding. [C-10, C-11]
7. **Check fact/continuity defects separately.** A repeated accusation caused by stale circumstances is a state question. An intentional accusation based on a character’s limited knowledge is a narrative question. Player readings of either remain an additional question. [C-02, C-06]
8. **Plan an unprimed reception inquiry.** Ask people what they noticed, inferred and valued before supplying author intent. Collect alternatives and uncertainties, not only agreement rates. Then decide whether the work supports the intended range of readings at an acceptable cost and risk. [C-12, C-14]

## Patterns and genre adaptations

W04 does not extract a third pattern for theme. A **counter-reading evidence audit** is recorded as proposed child work in the [extension queue](../reviews/full-run-20261010-w04-review-packet.md#child-work-and-recovery-queue), with its evidence route, decision question and unresolved central registration. It is not released guidance or research already completed under a child identity.

[Encounter and scenario composition](encounter-and-scenario-composition.md) supplies the context in which cost, refusal and aftermath become available for interpretation. [Narrative systems interfaces](narrative-systems-interfaces.md) supplies a conceptual distinction between accepted history and a reaction. Neither guarantees thematic effectiveness. The two W04 patterns should be used only for their narrow recovery/continuity purposes, not to mechanically generate meaning.

Intentional uncertainty, direct advocacy, absurdity and reflective play may require different treatments. Those are traits of a local design, not universal rules of a named genre. No genre membership or characteristic effect is inferred from the examples in this entry.

## Examples and counterexamples

### Inspected sources and the claims they permit

**Hocking / BioShock:** evidence of one critic’s reading and reported frustration. **Ultra Deluxe press kit:** evidence that contradiction is part of the creators’ published framing. **Jayanth / 80 Days:** a creator’s account of allowing differing perspectives rather than an obligatory definitive answer. **Never Alone:** an official account of collaboration with Iñupiat contributors. None was observed in an executed build during W04, and no cited review score or sales result is used as causal evidence. [C-07, C-08, C-10, C-11]

The distinction matters because these sources cannot be combined into “dissonance works” or “alignment fails.” They address different works, authors, claims and evidence objects. They do justify keeping those alternatives open for a specific design question.

### Illustrative worked example: the civic archive

An invented civic archive rewards the player for processing requests quickly. A public pledge promises that everyone’s history will be preserved. Some requests contain incomplete records; taking more time may allow testimony to be added. The thematic question is: **when an institution measures service by throughput, whose history becomes easy to discard?** This is an illustration, not approved canon, a tested intervention or a claim about a real institution. [C-15]

| Element | Proposed design evidence | Plausible interpretation / uncertainty |
|---|---|---|
| Throughput reward | Quick processing supplies the most visible immediate recognition. | Efficiency is valued; alternatively, the system may be read simply as a skill challenge. |
| Missing testimony | Some records become more complete only when the player pauses to ask. | Attention can preserve people’s perspectives; alternatively, delay may look like an arbitrary completion tax. |
| Public pledge | The archive repeatedly claims universal preservation. | A gap between promise and practice may imply hypocrisy; alternatively, it may be read as an aspirational ideal. |
| Ability to refuse a directive | A character can resist processing an incomplete record and accept a local cost. | Refusal may express solidarity; alternatively, it can appear like the author offering an obvious “good” answer. |
| A damaged seal recurring in different contexts | The same object appears on a repaired record and a rejected one. | A player may connect institutional authority and selective memory; the motif may also be ignored or read differently. |

**Aligned version:** recognition also acknowledges careful correction, and the story makes its costs and benefits visible. This may support a reading of stewardship, but it need not require that every careful action has a larger numerical payout.

**Deliberately dissonant version:** official praise remains focused on speed while character testimony exposes its omissions. The target of the tension is the institution’s measure, not a moral accusation against the person playing. The player might still reasonably feel blamed if the design offers no usable alternative; that is a review question rather than an interpretation to dismiss.

**Lower-complexity alternative:** remove the throughput economy and center the scene on a fixed disagreement between two archivists. This loses a potentially important relationship between incentive and action but reduces the risk of making a stressful task feel like a required moral examination.

**Interpretive openness:** stewardship, resistance, bureaucratic absurdity, triage and alienation are plausible proposed readings, not recorded participant findings. The desired review asks which available evidence sustains each one. A claim that the archive rewards slowness in a version that only rewards speed is a factual disagreement to resolve; a player reading the speed reward as satire rather than endorsement is not settled by the author’s preference.

### Counterexample: intentional dissonance is not a repair label

Suppose the ledger says an applicant was helped even though the accepted history records refusal. If no character is intentionally mistaken and no unreliable document is being presented, the discrepancy is a continuity defect under this invented design. Calling it “interpretive openness” does not make it intentional. Conversely, making every fictional document omniscient to eliminate such ambiguity could destroy a deliberate unreliable account. The correct response depends on the scoped evidence and promise, not on a universal alignment rule. [C-02, C-06]

## Failure modes and constraints

**Author intent becomes a grading key.** A player may understand the offer and reject its value. Treating disagreement as failed comprehension hides the distinction the study should examine. Record evidence cited, understanding, preference and ethical objection separately. [C-02, C-12]

**Symbolism becomes a universal dictionary.** A repeated color, animal, object or sound does not come with an established meaning for every culture, person or context. This draft provides no empirical cross-cultural symbol mapping. Compare what the specific work establishes with what the design merely assumes; seek relevant cultural and access review before depending on that assumption. [C-13]

**Tone is confused with intent.** A comic interruption may be intended as relief and perceived as trivialization, or intended as satire and perceived as approval. Those are hypotheses to investigate, not default facts. Inspect the timing, target and perspective of the humor alongside the consequences available to the player. [C-06, C-13]

**Representation becomes arithmetic or a shield.** Inclusion counts do not resolve how people are characterized, and a consultant’s participation does not make all interpretations harmless. A proposed participation process should permit substantive disagreement and revision, not only validate an already fixed result. No W04 consultation occurred. [C-09–C-11]

**Accessibility erases ambiguity.** An alternative description can make relevant evidence available without supplying its definitive interpretation. Adding an explanation may be appropriate for a particular goal, but it changes the evidence-to-reading relationship and should be reviewed as a design choice, not silently treated as equivalent. No numerical font or sensory guideline is imported here. [C-13]

**Production ambition exceeds support.** Multiple cultural perspectives, reactive performance and long motif development create research, consultation, localization and continuity obligations. A team should narrow the claim when it cannot support those obligations rather than treat unpaid correction by affected people as the production plan. This is a proposed ethical safeguard, not a measured cost model or approved studio policy. [C-11, C-12]

## Playtest and validation

**All inquiries are proposed and not performed.** No participant recruitment, play, interviews, consultation or thematic-effects experiment occurred. [C-14]

Start with a defined excerpt or later authorized prototype and record the version, available routes, whether participants completed it and what evidence they encountered. Invite relevant audience variation without requiring anyone to disclose a sensitive identity or personal trauma. Any actual study involving vulnerable populations or sensitive materials needs separately approved safeguards; this document does not supply that approval.

| Question | Proposed comparison and procedure | Measures and what could change the recommendation |
|---|---|---|
| Is the intended tension available without an answer key? | Ask neutral questions before explaining creator intent: what seemed important, what actions were encouraged, what evidence supported that reading, and what remained uncertain? | Preserve multiple readings and nonrecognition. Revise if the intended tension depends on information participants never had or on post-hoc explanation. |
| Is deliberate dissonance distinguishable from an accidental defect? | Compare a bounded aligned version, a deliberately conflicting version and a simpler version only where each can be implemented without changing unrelated demands. | Record cited evidence, perceived intentionality, confusion, unwanted blame and preference separately. Reject or narrow the mismatch if it chiefly produces the unintended problem the team cannot defend. |
| Is a symbol doing useful work? | Compare the scene with and without the motif, controlling other emphasis where feasible. | Ask for noticed details and interpretations without naming the symbol first. Remove or revise when the motif is irrelevant, exclusionary or misleading relative to its cost. Absence of a reported interpretation is not proof of no effect. |
| Does representation support the intended role and range of perspectives? | Use contextual review and voluntary reception inquiry with relevant contributors/participants, allowing critique before the content is fixed. | Record agency, stereotyping concerns, omitted perspectives and disagreement; do not replace discussion with a count or unanimity requirement. |

A comparison that changes difficulty, reward magnitude, dialogue length and motif placement simultaneously cannot isolate thematic alignment. Familiarity, prior beliefs, cultural context, language, access route, social play and demand characteristics can alter responses. Define the local acceptability and revision criteria before testing; no universal agreement percentage, sample size or emotional threshold is supplied. Engagement, completion, revenue and awards do not certify that a theme was understood, ethically acceptable or causally effective.

## Claim ledger

| ID | Precise claim and class | Support / locator | Applicability, confidence and unresolved question |
|---|---|---|---|
| C-01 | Theme, meaning, tone and symbol are working distinctions for a design inquiry. `inference` | W04 framing, not a formal taxonomy approval. | Moderate as organization; competing definitions remain possible. |
| C-02 | Intent, inspected artifact, interpretation and empirical response support different claims. `inference` | Evidence rules; inspected W01/W02 distinctions; source types in this entry. | High for non-equivalence. The practical benefit of the proposed review remains untested. |
| C-03 | Bogost proposes expressive procedural analysis without making persuasion inevitable. `inference` | W04-007, printed pp. 125, 133, 137. | High for the theoretical position in inspected passages; not empirical efficacy. Mirror provenance qualified. |
| C-04 | Sicart critiques the neglect of play and asks for complementary analysis, not abandonment of all procedural analysis. `inference` | W04-006, closing Against Procedurality section. | High for the stated position; cited outside empirical works not independently verified here. |
| C-05 | Describing available incentives and studying actual readings are complementary proposed tasks. `inference` | C-02–C-04; reviewed F07 measure/interpretation distinction. | Moderate for useful method; no complete-method comparison inspected. |
| C-06 | Alignment, deliberate dissonance and accidental contradiction require different judgments; intention alone does not certify effect. `inference` | C-02, C-07, C-08; W04 reasoning. | High for the distinction, low for any predicted audience benefit. |
| C-07 | Hocking supplies one critical reading of BioShock’s conflicting contracts and his reaction. `inference` | W04-005, main-body two-contract discussion. | High for attribution, not for generalization or creator intent. |
| C-08 | The Ultra Deluxe press kit deliberately foregrounds contradiction and constrained choice. `observed-example` | W04-008, dated announcement description. | High for marketing text; no played system or reception observed. |
| C-09 | The GLAAD/Nielsen report records a scoped LGBTQ-subgroup self-report about representation. `empirical-evidence` | F07-014, printed pp. 13 and 36; sample age context p. 7. | Moderate for the reported survey result; not causal wellbeing evidence, global estimate or universal preference. |
| C-10 | Jayanth describes authoring room for differing world perspectives. `practitioner-heuristic` | W01-09, 80 Days / Artificers’ Guild discussion. | High for creator account, not for audience reception or all collaborators’ views. |
| C-11 | Collaboration routes and meaningful representation review are distinct from a blanket endorsement. `inference` | W01-12, official collaboration account; inspected F07 ethics; W04 safeguard proposal. | Moderate as a boundary; no independent consultation outcome inspected. |
| C-12 | A counter-reading review may expose unsupported assumptions and guide revision. `hypothesis` | C-02–C-11 provide rationale; proposed W04 process. | Low for workflow/artistic benefit. It may become burdensome or suppress valuable ambiguity. |
| C-13 | Tone, symbols and equivalent evidence need contextual, locale and access review rather than universal mappings. `hypothesis` | W04 proposal; no comparative symbol study inspected. | Low for particular mappings/effects; explicit evidence gap. |
| C-14 | Unprimed reception questions and separate measures can challenge, rather than merely confirm, a thematic proposal. `hypothesis` | Reviewed F07 evaluation principles; W04 proposed protocol. | Low for this protocol’s validity; no test performed. |
| C-15 | The civic archive is invented analytical material, not a documented game or result. `hypothesis` | W04 illustration. | Low for its effects; no adoption or canon approval. |

Source abbreviations resolve to the complete source IDs in References. A theoretical article remains `inference`, not `empirical-evidence`; creator intent remains a practitioner account rather than a player-outcome result.

## Open questions and change history

Coverage is **open**. This draft addresses alignment/dissonance, creator-player disagreement, representation, tone, symbolism and interpretive openness through theory, primary critical/creator accounts, an official creative artifact and one scoped survey. It does not establish comparative thematic effectiveness, cross-cultural symbol equivalence, long-term effects, or a validated consultation method. Historical explanatory material for Rod Humble’s *The Marriage* was not retrieved and supports no claim here; the access gap is recorded in the packet.

The next discriminating question is whether an unprimed, evidence-grounded counter-reading review identifies a consequential assumption that a conventional intent-led review misses, without turning interpretation into a forced consensus. Additional work needs independent review and central child-key reconciliation before execution. Current W03/F03 content has not been assumed.

**History:** `0.1.0`, `initial-draft-1`; initial W04 submission, predecessor and supersession null. Author self-review is not independent review. No meaning, representation judgment or implementation has been approved merely by saving this draft.

## Reviewed inputs and transfer limits

Inspected W01 character/worldbuilding/narrative distinctions, W02 lore’s fact/account/evidence/interpretation separation, F07 ethics and evaluation, and corrected F01/W02 validation distinctions. Jayanth, Never Alone and the GLAAD report were separately re-inspected in their public originals or official publication, with their prior source identities retained. The selected input is the parent-reviewed, unreleased waves 1–2 candidate archive, locally fingerprinted SHA-256 `4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931`. Relevant bytes, rather than remembered earlier drafts, were inspected. Exact dependency paths, selected revisions, byte hashes and inspected line ranges are recorded in the [review packet](../reviews/full-run-20261010-w04-review-packet.md#reviewed-dependency-provenance). These are prior candidate syntheses, not independent empirical validation of W04. Their cited outside studies are not reasserted unless the original source is separately listed in this entry.

The mounted starter instructions, evidence rules, gates, index, taxonomy and templates are the historical `0.1.0 candidate` input. The current dispatch authorizes W04 research but not conclusions, permanent IDs or release. The current canonical index, pending global allocations and central recovery ledger were not available. Current W03 spatial/exploration and F03 progression/resource drafts remain unavailable author-running dependencies; no guidance is inferred from them. There is no genre-specific draft in this packet; genre adaptation remains with the relevant owner, and no game label is inferred from an example.

## References

### GDR-SRC-20261010-W04-007 — The Rhetoric of Video Games

**Author/organization:** Ian Bogost. **Publication/update:** 2008. **Publisher:** MIT Press, in Katie Salen (ed.), The Ecology of Games: Connecting Youth, Games, and Learning. **Verified access route:** [The Rhetoric of Video Games](https://se4n.org/papers/bogost-rhetoric.pdf). **Edition/build:** Original chapter, bibliographic range pp. 117–140; DOI 10.1162/dmal.9780262693646.117; inspected third-party 23-page PDF mirror. **Accessed:** 2026-10-10 (America/Los_Angeles research date). **Access:** `relevant-excerpt`. **Type:** Original scholarly theoretical chapter, accessed via mirror. **Locator:** Printed p. 125, Procedural Rhetoric; p. 133, paragraph on inquiry/agreement/disapproval; p. 137, conclusion that representation/persuasion are not inevitable; bibliographic first page visually inspected. **Claims in this entry:** C-03; bridge for C-05/C-12. **Rights:** First page identifies Creative Commons Attribution–NonCommercial–NoDerivatives 3.0; analysis paraphrased, source not redistributed. **Limits/relationships:** Author-site and DOI retrieval failed. Mirror attribution checked against the visual first page, not publisher-authenticated bytes. The argument is not experimental proof of persuasion; it acknowledges possible disagreement. Sicart critiques this theoretical tradition..

### GDR-SRC-20261010-W04-006 — Against Procedurality

**Author/organization:** Miguel Sicart. **Publication/update:** 2011-12. **Publisher:** Game Studies, volume 11, issue 3. **Verified access route:** [Against Procedurality](https://gamestudies.org/1103/articles/sicart_ap/). **Edition/build:** Volume 11(3), theoretical article. **Accessed:** 2026-10-10 (America/Los_Angeles research date). **Access:** `relevant-excerpt`. **Type:** Original scholarly theoretical argument. **Locator:** Closing section Against Procedurality, especially paragraphs beginning What is left and My intention, my position; preceding discussion of appropriation and player values. **Claims in this entry:** C-04; bridge for C-05/C-12. **Rights:** Copyright author/journal; paraphrase only. **Limits/relationships:** Not an empirical experiment. Its citations to other researchers were not independently inspected here. A critique in the same debate is not independent empirical corroboration; the closing argument retains a role for procedural analysis..

### GDR-SRC-20261010-W04-005 — Ludonarrative Dissonance in Bioshock

**Author/organization:** Clint Hocking. **Publication/update:** 2007-10-07. **Publisher:** Click Nothing, author’s blog. **Verified access route:** [Ludonarrative Dissonance in Bioshock](https://clicknothing.com/2007/10/07/ludonarrative-d/). **Edition/build:** Original dated critical essay, currently hosted page; comments excluded. **Accessed:** 2026-10-10 (America/Los_Angeles research date). **Access:** `relevant-excerpt`. **Type:** Primary critical interpretation / personal reception account. **Locator:** The problem of what the game is about; main-body paragraphs beginning The game begins by offering the player two contracts through the account of forced assistance to Atlas. **Claims in this entry:** C-07; constrains C-06. **Rights:** Copyright author; paraphrase only. **Limits/relationships:** Primary evidence of Hocking’s reading, not BioShock’s documented creator intent, a representative player study, or an independently verified economy/build observation. Spoilers in source..

### GDR-SRC-20261010-W04-008 — The Stanley Parable: Ultra Deluxe: Press Kit

**Author/organization:** Crows Crows Crows / The Stanley Parable: Ultra Deluxe creators. **Publication/update:** Dated announcement section: 2022-03-30; later OUT NOW edits visible, revision date unknown. **Publisher:** Official game press site. **Verified access route:** [The Stanley Parable: Ultra Deluxe: Press Kit](https://stanleyparable.com/press/). **Edition/build:** Ultra Deluxe promotional text; page lists release 2022-04-27; no game build played. **Accessed:** 2026-10-10 (America/Los_Angeles research date). **Access:** `relevant-excerpt`. **Type:** First-party creative positioning / marketing artifact. **Locator:** Wednesday 30th of March 2022 — Platform & Release Date Announcement, description paragraph pairing offered/removed choice and continuing contradiction. **Claims in this entry:** C-08; constrains C-06. **Rights:** Copyright creators; no screenshots, trailers or quoted reviews reproduced. **Limits/relationships:** Supports only the creators’ published framing of contradiction. Not evidence of a particular played scene, intended audience response or successful thematic effect. Promotional review blurbs are excluded..

### GDR-SRC-20261010-F07-014 — 2024 GLAAD Gaming Report: The State of LGBTQ Inclusion in Video Games

**Author/organization:** GLAAD, with research partner Nielsen. **Publication/update:** 2024; fieldwork June–August 2023. **Publisher:** GLAAD. **Verified access route:** [2024 GLAAD Gaming Report: The State of LGBTQ Inclusion in Video Games](https://assets.glaad.org/m/5ab9a335d607edcd/original/2024-GLAAD-Gaming-Report.pdf). **Edition/build:** 2024 report; PDF 40 pages; exact publication day not reverified here. **Accessed:** 2026-10-10 (America/Los_Angeles research date). **Access:** `relevant-excerpt`. **Type:** Original commissioned survey/report. **Locator:** Printed p. 13, subgroup self-report; p. 36, Methodology (both pages visually inspected); p. 7, sample age range 13–55. **Claims in this entry:** C-09 only; does not validate C-12/C-14. **Rights:** Copyright GLAAD; aggregate result paraphrased, charts not reproduced. **Limits/relationships:** US active PC/console-player panel, ages 13–55, n=1,452 with LGBTQ boost; 72% refers to LGBTQ respondents, not the whole sample. Self-report, not randomized exposure or a causal wellbeing effect; no confidence interval in the inspected passage. Advocacy commission disclosed; same report as F07-014..

### GDR-SRC-20261010-W01-09 — Forget Protagonists: Writing NPCs with Agency for 80 Days and Beyond

**Author/organization:** Meg (Meghna) Jayanth. **Publication/update:** 2016-06-05; transcript of a GDC 2016 talk. **Publisher:** Author’s Medium publication. **Verified access route:** [Forget Protagonists: Writing NPCs with Agency for 80 Days and Beyond](https://medium.com/@betterthemask/forget-protagonists-writing-npcs-with-agency-for-80-days-and-beyond-703201a2309). **Edition/build:** Author-published talk transcript; creator account, not game execution. **Accessed:** 2026-10-10 (America/Los_Angeles research date). **Access:** `relevant-excerpt`. **Type:** Firsthand narrative-design account and practitioner argument. **Locator:** Author’s discussion of Sunless Sea / Isle of Cats / Zaira and the cost of refusal; 80 Days section on differing Artificers’ Guild perspectives. **Claims in this entry:** C-10; contextual contribution to C-11. **Rights:** Copyright author; short paraphrases only. **Limits/relationships:** Creator’s intent and examples do not establish player effects. Her commentary about other studios’ games is not treated as firsthand intent evidence. Same work as W01-09; identity reused..

### GDR-SRC-20261010-W01-12 — Never Alone (Kisima Inŋitchuŋa)

**Author/organization:** E-Line Media / Never Alone project. **Publication/update:** unknown; live official page checked on access date. **Publisher:** Never Alone official website. **Verified access route:** [Never Alone (Kisima Inŋitchuŋa)](https://www.neveralonegame.com/never-alone). **Edition/build:** Official product/creation description; no game build, interviews or video played. **Accessed:** 2026-10-10 (America/Los_Angeles research date). **Access:** `relevant-excerpt`. **Type:** First-party creation and product account. **Locator:** Description of collaboration with Iñupiat elders, storytellers and community members; Cultural Insights description. **Claims in this entry:** C-11, documented collaboration route only. **Rights:** Copyright publisher/contributors; no visual assets or interview footage reproduced. **Limits/relationships:** Documents a collaboration route, not universal cultural consent, efficacy of a specific symbol, or independent player outcomes. Third-party promotional review quotes excluded. Same work as W01-12..


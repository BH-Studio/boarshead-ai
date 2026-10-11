---
id: GDR-CAND-20261010-W02-TOP-01
kind: topic
title: Dialogue and voice
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
- conversation design
- dialogue choices
- barks
- character voice
- subtext
tags:
- expression
- agency
- conversation
- performance
- localization
- accessibility
- interruption
related_topics:
- GDR-CAND-20261010-W02-TOP-02
- GDR-CAND-20261010-W02-TOP-03
related_patterns:
- GDR-CAND-20261010-W02-PAT-01
- GDR-CAND-20261010-W02-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-W02-001
- GDR-SRC-20261010-W02-002
- GDR-SRC-20261010-W02-003
- GDR-SRC-20261010-W02-004
- GDR-SRC-20261010-W02-005
- GDR-SRC-20261010-W02-006
- GDR-SRC-20261010-W02-007
- GDR-SRC-20261010-W02-008
- GDR-SRC-20261010-W02-009
- GDR-SRC-20261010-W02-010
reviewer: null
approved_by: null
approved_date: null
independent_review: not-performed-for-W02
predecessor_hash: null
supersedes: null
change_summary: Initial W02 submission; no earlier batch artifacts reproduced or replaced.
byte_hash_record: ../reviews/full-run-20261010-w02-review-packet.md#artifact-byte-manifest
---

# Dialogue and voice

**Draft research candidate — not released guidance.** Candidate identity is run-scoped, not a permanent GDK allocation. No W02 independent review, gameplay prototype or player test has occurred.

## Decision and scope

**Decision:** What should a player be able to express, understand, interrupt and remember through dialogue, and which of those functions warrant recorded performance? This entry covers conversational structure, choices, subtext, barks, performance and localization. It does not prescribe an engine, conversation manager, casting market, language roster or game’s approved characterization.

Working definitions are analytic conveniences, not a published universal taxonomy. A **dialogue choice** is a player-selected contribution or conversational intention. **Voice** includes a character’s manner of expression and, when present, its performed delivery. A **bark** is a short, context-triggered utterance outside a fully attended exchange. **Subtext** is a meaning a player may infer beyond literal wording. These dimensions can overlap without requiring distinct plot branches. [C-01]

The central proposed distinction is between **expression** (what stance the player adopts), **recognition** (what the response acknowledges), **information** (what becomes available) and **consequence** (what changes subsequently). A menu can support expression without changing the ending. It becomes misleading when its framing promises a kind of control that the delivered exchange does not provide. This is an inference to evaluate locally, not a claim that every line needs four effects. [C-01; GDR-SRC-20261010-W02-003]

W01 narrative structures, worldbuilding and character design are **parent-reviewed according to the supplied dispatch, but their reviewed bytes are unavailable here**. They have not been transferred as evidence. Presentation localization/interface and performance guidance remain missing shared dependencies. The scope excludes comprehensive genre guidance; no genre template or reviewed genre file is available for this batch.

## Core explanation and mechanisms

### Consequence is not the only meaning, and acknowledgement is not demonstrated equivalence

Cardona-Rivera and colleagues studied 88 participants in a short text-story task. Their agency analysis supported some distinctions between choices, but the initially specified classes were not homogeneous. The later ordered analysis supported S1–S3; S4 and the original S5 did not support the trend. S5′ excluded two end choices. Ratings were retrospective, after outcomes were known. This is limited evidence about that operationalization, not proof that a particular menu format creates agency. [C-02; GDR-SRC-20261010-W02-001]

Fendt and colleagues compared a downselected branching group of 52 with linear-feedback and minimal-feedback groups of 54 and 44. Of six story-level comparisons, branching versus feedback differed on one at the paper’s .05 threshold, with another marginal at .1. Their predicted general feedback-versus-minimal-feedback benefit was not established. Unequal group composition, downselection and nonsignificant differences do not establish equivalence. [C-03; GDR-SRC-20261010-W02-002]

**Evidence-to-application bridge:** use those studies to separate questions, not to advertise a guaranteed agency shortcut. Test whether players understood their contribution, whether the response recognized it, and whether they expected a downstream difference. A favorable global “agency” rating can coexist with a misunderstood commitment. Conversely, a deliberately expressive response may be valuable without a divergent plot. The studies share authors and a paradigm; they are not independent confirmations of this entire proposed workflow. [C-11]

### Conversational intention and subtext

Short argues that intention-oriented options can avoid a mismatch between literal wording and what the player is trying to do, while explicitly preserving an exception when interpreting conversational nuance is itself the challenge. Her account also discusses nested clarification and the limits of simulating ordinary disfluencies. These are practitioner observations about interactive fiction, not independently inspected findings from the linguistics book she discusses. [C-04, C-05; GDR-SRC-20261010-W02-003]

Our application is to keep the **player’s intended speech act legible while allowing another character’s motives to remain uncertain**. “Ask for temporary access” may fairly precede an indirect request. “Promise repayment” should not silently become a threat. Neither label has to forecast whether the request succeeds. Where choosing exact words is the intended challenge, a label that exposes hidden politeness or deception would remove part of the task. [C-11]

### Context selection is not a performance-quality metric

Yarn Spinner’s inspected saliency documentation describes selecting among eligible content and allowing no selection. Its localization documentation associates localized text/assets with line identities. These are documented facilities, not evidence that random variety produces believable characters or that a particular implementation is required. [C-06, C-07; GDR-SRC-20261010-W02-005, GDR-SRC-20261010-W02-006]

A proposed bark policy therefore separates **eligibility** from **attention value**. A line may be factually possible yet unnecessary while the player reads a choice. Another line may be necessary now but become false if delayed. Eligibility asks whether a speaker could appropriately say it; attention value asks whether saying it now is worth displacing other information. Silence is a valid output. [C-12]

### Performance is an interpretation and production commitment

The IGDA recording guide recommends contextual direction and consistency between final recordings and the script/subtitles. Its 2012 edition was reposted in 2021; its historical cost figures and regional voice stereotypes are not adopted here. The later IGDA LQA article treats characterization, terminology and in-context presentation as review concerns. Neither provides a universal voiced-content budget. [C-09, C-10; GDR-SRC-20261010-W02-010, GDR-SRC-20261010-W02-009]

The bridge is not “record more.” It is to choose which meanings the performance must convey, then review the **selected option → performed line → translated/subtitled line → response** together. A recording can narrow ambiguity by making irony unmistakable, or add ambiguity through hesitation. That is a local artistic decision to investigate, not a guaranteed gain over text. [C-13]

## Design choices and alternatives

| Decision | Conditional option | Cost, risk and simpler alternative |
|---|---|---|
| Literal line or intention label | Use literal lines when diction is the player’s action; intention labels when indirect speech would otherwise misrepresent the commitment. | Labels can flatten role-play. Offer a full-line preview or fewer clearer options rather than annotating every emotion. [C-04, C-11] |
| Branch, reconverge or keep fixed premise | Branch when the promised outcome differs; reconverge when expression or immediate information is the point; state a fixed premise rather than presenting an unsupported refusal. | Reconvergence still needs consistency with earlier statements. Do not sell expressive variation as a different fate. [C-01, C-11] |
| Topic hub, staged exchange or interjection | Topic hubs support optional inquiry; staged exchanges support particular rhetorical development; interjections can support concurrent activity. | Hubs risk circular questioning; strict sequencing risks blocking re-entry; interruptions risk lost obligations. Track unresolved questions in authoring notes, not a mandated runtime design. [C-05, C-11] |
| Full, selective or no recorded voice | Choose according to the desired interpretation, revision load, available performers, locale support and attention demands. | Selective voice needs a consistent expectation; text-only avoids recording/pickup work but still needs accessible presentation and expressive writing. No numerical budget crossover is known here. [C-13] |
| Bark replay or suppression | Replay missed task-critical information through an appropriate route; suppress expired flavor. | Blindly replaying an old warning can become false. A journal, explicit request for repetition or current-state summary may be preferable. [C-12] |
| Localized literalness or adapted speech act | Preserve commitment, relationship and available inference; allow locally reviewed phrasing to change. | Word-for-word similarity is not an acceptance criterion. Exact phrasing may be essential to a puzzle, requiring separate design and language review. [C-10, C-13] |

These are proposed choices, not a mandate to implement every option. A short fixed exchange can be better than a selection interface that falsely suggests freedom. The useful question is what the interface promises, not how many branches are visible. [C-01, C-11]

## Application process

1. **Diagnose the exchange.** Write what each speaker wants, knows and is willing to reveal. Separate the player’s goal from the protagonist’s permitted contribution and the other character’s interpretation. List the task information that must remain recoverable. Treat missing approved character/world rules as unresolved, rather than inventing them. [C-11]
2. **Choose the control being offered.** For each option, specify its speech act, the actual wording or allowed performance range, immediate recognition, any future commitment and information access. Mark deliberately expressive-only options. Remove a choice whose advertised commitment cannot be honored. [C-11]
3. **Design conversational repair.** Identify outstanding questions, interruptions, refusal, re-entry after absence and a safe exit. After a clarification, return to the original question or explicitly cancel it. Do not make the player repeat an irreversible promise merely to recover context. [C-05, C-11]
4. **Specify the bark’s job.** State eligibility, expiry, conflict with foreground speech, what happens when it is missed, and whether silence is preferable. Vary context or content before increasing repetition; no fixed cooldown is proposed as universally correct. [C-12]
5. **Prepare a small script/performance comparison.** Include context for actors and language reviewers: addressee, relationship, preceding alternatives, pronunciation, timing constraints and whether uncertainty is intended. Where words can change after recording, define a reconciliation check for each affected line and locale. This is authoring guidance, not a new asset architecture. [C-09, C-10, C-13]
6. **Evaluate and revise.** Compare intended and reported speech acts before considering enjoyment ratings. Test recovery with interruptions and varied input/audio access. Preserve a source-language ambiguity only when the localized experience can carry the intended task; do not call an accidental mismatch “subtext.” Stop adding branches or voice until the specific mismatch is understood. [C-11, C-13, C-15]

## Patterns and genre adaptations

[Intent and response contract](../patterns/intent-and-response-contract.md), `GDR-CAND-20261010-W02-PAT-01`, turns the intention/recognition distinction into a conditional authoring and testing recipe. It is a new draft hypothesis-informed pattern, not a released method.

[Multi-route objective contract](../patterns/multi-route-objective-contract.md), `GDR-CAND-20261010-W02-PAT-02`, is relevant when a conversation accepts, changes or resolves a quest. Neither pattern grants a new quest outcome merely because an option is phrased persuasively.

Context variables requiring future genre adaptation include whether uncertainty concerns **what to say**, **what another person believes**, or **what action a statement commits to**; whether conversations can be interrupted; and whether the player embodies a fixed or highly authored persona. Those differences must remain explicit. No genre label automatically decides which kind of uncertainty to remove. Reviewed genre adaptations and their IDs are unavailable; no placeholder genre links are asserted.

## Examples and counterexamples

### Illustrative: requesting emergency water access

This is an invented cross-game example, not studio canon or an observation. The player needs access to a reservoir during repairs. The attendant can authorize access, but the player does not know the attendant’s private concerns.

An option labeled **“Ask for access until the repair is finished”** permits an indirect line such as “Could the gate stay open while we finish the pump?” The attendant replies with a condition: “Only while someone watches the spillway.” That response recognizes a request without inventing a promise to supply labor. The journal may record the offered condition; acceptance requires a further player action. This makes the speech act explicit while preserving uncertainty about the request’s success. [C-11; illustrative]

By contrast, a button labeled **“Reassure the attendant”** that performs “I swear I will personally pay every loss” creates an unadvertised commitment. An apology immediately afterward does not repair the control mismatch. The remedy is to narrow the performed line, expose the commitment before selection, or let the protagonist’s autonomous promise be an explicitly authored event rather than the player’s selected action. [C-11; illustrative]

For a bark, “The spillway is overflowing” becomes inappropriate after the danger ends. A postponed reminder should report the current state, not replay an expired sentence. Flavor such as a comment on the weather can be omitted during a choice; essential safety information needs a recoverable equivalent. This policy is proposed, not tested. [C-12; illustrative]

### Creator-reported example: expressive constraints

Short describes *Mask of the Rose* using character/wardrobe conditions to constrain available expression rather than presenting every personality stance simultaneously. This provides an inspectable creator account of expressive design without establishing an optimal option count or a causal benefit. The game was not played for this batch. [C-14; GDR-SRC-20261010-W02-004]

### Strong counterexample: interpreting the utterance is the challenge

In an illustrative etiquette encounter, the distinction between a request and an offer is exactly what the player is learning to infer. Automatically labeling the successful intention could answer the puzzle. Preserve that uncertainty, supply comprehensible context and an agreed recovery path, and test the challenge with relevant language/cultural expertise. Do not preserve obscurity merely because one author understands it. This limits the strongest intention-label recommendation rather than being an exception to hide. [C-04, C-11; illustrative]

## Failure modes and constraints

**Access without unintended omniscience.** XAG 104 covers spoken and supplementary information, speaker/direction cues and captions for significant audio. Its collection explicitly presents best practices rather than a legal/compliance checklist. No font, timing or other numeric setting is promoted here as universally accessible. [C-08; GDR-SRC-20261010-W02-007, GDR-SRC-20261010-W02-008]

As an application proposal, captions should convey an audible sneer or hesitation when relevant, but should not identify a speaker as lying when listeners receive no such certainty. A recovered line must not spoil a later revelation. Subtitle-only, audio-led and translated routes require a comparison of what becomes knowable, not mechanical word identity. [C-13]

**Representation and trust.** Avoid making dialect, accent or a communication difference a hidden moral score. Characterization may depict social prejudice, but the authoring review should distinguish the depicted prejudice from a reliable system judgment. Review audience assumptions and performer permissions with the actual responsible people; no contract, approved casting policy or legal determination is supplied by this research. [C-13]

**Production and continuity.** A late line rewrite can affect performance, response, quest promise and lore implications. The proposed control is a change-impact review across those uses, not an unqualified requirement to rerecord everything. Sparse voice and fewer options remain legitimate alternatives. [C-13]

**Evidence ceiling.** No directly inspected trial here measures bark scheduling, speech-act labels across locales, subtext comprehension with disabled players, or full-versus-selective voice effectiveness. The published text-agency studies cannot fill those gaps. [C-15]

## Playtest and validation

**All tests below are proposed and not performed.** No participants, prototype or empirical result belong to W02.

| Test | Comparison and procedure | Measures, confounds and rejection rule |
|---|---|---|
| Speech-act understanding | Compare literal options, intention labels and an unselectable fixed exchange for otherwise equivalent short scenes. Ask what the protagonist would be committing to before selection, then ask what was actually said and recognized. | Code unadvertised commitments separately from dissatisfaction with the outcome. Balance writing quality, order and familiarity. Reject the proposed labels when they add commitments, fail to reduce the targeted misunderstanding, or remove a valued interpretive task. [C-11, C-15] |
| Reconvergence honesty | Compare explicit expressive framing with outcome-promising framing of the same reconverging conversation; include a genuine downstream-branch comparison where feasible. | Measure anticipated versus delivered consequences and later trust, not only immediate agency. Do not interpret a nonsignificant difference as equivalence. Do not conclude equivalence without a justified local margin and sufficient precision. [C-03, C-15] |
| Bark interruption | Introduce an interruption before, during and after task-critical versus flavor lines. Compare replay, current-state summary and suppression policies. | Record missed facts, repeated false warnings, competing reading load and successful recovery. Reject policies that preserve line count while delivering outdated information. Control scene intensity and subtitle configuration. [C-12, C-15] |
| Performance/localization | Review the same exchange in intended locales and supported audio/text configurations, with relevant language expertise and participant access needs. | Check speech acts, implied relationship, intended ambiguity and recoverable information. Do not treat nominally identical transcripts or a back-translation as sufficient equivalence. Rework materially different commitments; retain intentional artistic differences that the project explicitly accepts. [C-13, C-15] |

Recruit for the intended audience and access needs, not only fluent readers already familiar with the genre or authoring tool. Determine sample size, coding agreement, practical difference margins and acceptable failure costs with the local evaluation owner before collecting data. None is prescribed numerically here. Distinguish recognizing a taught example from applying its rule to an unfamiliar conversational situation. [C-15]

## Claim ledger

Claim identifiers are local to this artifact. Confidence describes the stated narrow claim, not proof that the proposed technique improves a game. `inference` and `hypothesis` recommendations are author proposals, not approved studio decisions.

### C-01

**Claim:** Distinguishing expression, recognition, information and consequence is a useful proposed way to audit what a dialogue option promises, without requiring every option to branch the plot.

**Class:** `inference`. **Support/contradiction:** Interpretive framework, not an empirical factor model.

**Sources and precise locators:** GDR-SRC-20261010-W02-003 — Intention-versus-literal-command discussion; author-defined analytic dimensions in this entry.

**Applicability:** Genre-neutral authoring audit; not a taxonomy of all dialogue meaning. **Confidence:** moderate for diagnostic clarity; low for player benefit because the framework is untested. **Unresolved:** Which distinctions actually help the intended audience and writers?

### C-02

**Claim:** The 2014 study offers qualified, retrospective evidence about situational choice distinctions; its original classifications and all agency scales did not uniformly support the prediction.

**Class:** `empirical-evidence`. **Support/contradiction:** Contains supported and null analyses and a modified S5 analysis, as stated above.

**Sources and precise locators:** GDR-SRC-20261010-W02-001 — pp. 11–14; Tables 5–6; Limitations.

**Applicability:** Short text-story self-report; no general effect size or voiced-game transfer asserted. **Confidence:** moderate: primary methods and result tables inspected; interpretation and design limitations remain. **Unresolved:** Prospective, broader-population and longer-form replication.

### C-03

**Claim:** The 2012 comparison neither proves branching/feedback equivalence nor establishes a general feedback-over-minimal-feedback benefit.

**Class:** `empirical-evidence`. **Support/contradiction:** Contrary/limiting evidence against a simple agency-preservation rule.

**Sources and precise locators:** GDR-SRC-20261010-W02-002 — PDF pp. 8–10, Results; Table 2; explicit failure to prove Hypothesis 2.

**Applicability:** Three unequal groups in one short-story design. **Confidence:** moderate: result table and limitations inspected; not a causal universal. **Unresolved:** Would a balanced, precision-planned comparison yield meaningful equivalence?

### C-04

**Claim:** Intention labels are a practitioner-supported option, with an explicit exception when interpreting conversational nuance is the task.

**Class:** `practitioner-heuristic`. **Support/contradiction:** Conditional advice, not a tested interface superiority claim.

**Sources and precise locators:** GDR-SRC-20261010-W02-003 — Paragraph after the lift-request alternatives, beginning the text/subtext discussion.

**Applicability:** Especially relevant to indirect speech; language/culture transfer unresolved. **Confidence:** moderate for faithful reporting of the advice, low for generalized effectiveness. **Unresolved:** When does an intention label disclose too much?

### C-05

**Claim:** Nested clarification and conversational re-entry warrant attention; ordinary disfluency need not be simulated literally.

**Class:** `practitioner-heuristic`. **Support/contradiction:** Supports a conversational design consideration, not a mandatory state machine.

**Sources and precise locators:** GDR-SRC-20261010-W02-003 — Nested question/answer and final turn-taking paragraphs.

**Applicability:** Turn-based/literary contexts differ from live interruption. **Confidence:** moderate: explicit first-person analysis; no controlled evidence. **Unresolved:** How much repair supports coherence without adding busywork?

### C-06

**Claim:** The inspected Yarn saliency document describes eligible-content selection and a no-selection outcome, not validated dramatic relevance.

**Class:** `observed-example`. **Support/contradiction:** Direct document observation only; product not executed.

**Sources and precise locators:** GDR-SRC-20261010-W02-005 — Saliency explanation and strategy/no-selection text.

**Applicability:** Unpinned documentation snapshot, 2026-10-10. **Confidence:** high for the text inspected; no efficacy inference follows. **Unresolved:** How should narrative relevance and expiry be evaluated for this game?

### C-07

**Claim:** The inspected Yarn localization document describes line-associated localized strings and assets; this is one documented facility, not a required architecture.

**Class:** `observed-example`. **Support/contradiction:** Direct document observation; no runtime test.

**Sources and precise locators:** GDR-SRC-20261010-W02-006 — Localized strings/assets and line-ID passages.

**Applicability:** Specific product documentation snapshot. **Confidence:** high for the narrow documentary statement. **Unresolved:** Does the project’s actual workflow preserve the intended line meaning?

### C-08

**Claim:** XAG subtitle/caption guidance is applicable professional guidance whose own collection is not a legal/compliance checklist.

**Class:** `practitioner-heuristic`. **Support/contradiction:** Normative-sounding best practices are not promoted to a formal standard.

**Sources and precise locators:** GDR-SRC-20261010-W02-007, GDR-SRC-20261010-W02-008 — XAG 104 Overview/Implementation; V3.2 overview scope statement.

**Applicability:** Applicability still requires intended audiences, modalities and platform review. **Confidence:** high for issuer scope and stated guidance; no universal configuration claimed. **Unresolved:** Which information equivalences are needed in each supported presentation?

### C-09

**Claim:** Contextual recording direction and final script/recording/subtitle reconciliation are documented production practices, not universal budget figures.

**Class:** `practitioner-heuristic`. **Support/contradiction:** Historical professional advice; rejected stereotypes and cost ratios are excluded.

**Sources and precise locators:** GDR-SRC-20261010-W02-010 — Voice-Over Recording, printed pp. 19–20 / PDF pp. 22–23.

**Applicability:** Recording/localization production with revision dependencies. **Confidence:** moderate: useful practice account without comparative outcome measurement. **Unresolved:** What rework and quality effects occur in the actual production pipeline?

### C-10

**Claim:** In-context localization review should consider characterization, terminology and source changes rather than only isolated linguistic correctness.

**Class:** `practitioner-heuristic`. **Support/contradiction:** Professional review advice, not measured workflow superiority.

**Sources and precise locators:** GDR-SRC-20261010-W02-009 — What is LQA? and What happens during LQA?; source-change discussion.

**Applicability:** Relevant locales and culturally informed reviewers are needed. **Confidence:** moderate: explicit practitioner account. **Unresolved:** What semantic mismatches remain after the proposed review?

### C-11

**Claim:** An option-to-utterance-to-response audit may reduce unadvertised speech commitments while preserving uncertainty about other characters or outcomes.

**Class:** `hypothesis`. **Support/contradiction:** Evidence-to-application bridge is reasoned, not established by the agency studies.

**Sources and precise locators:** GDR-SRC-20261010-W02-001, GDR-SRC-20261010-W02-002, GDR-SRC-20261010-W02-003 — Derived from the distinctions and limitations in C-02–C-05; no direct test of this recipe.

**Applicability:** Do not use to solve a deliberate language/etiquette interpretation task. **Confidence:** low for benefit: the proposed contract has not been tested. **Unresolved:** Does it reduce the targeted mismatch without flattening desired expression?

### C-12

**Claim:** A bark policy that checks truth, attention conflict, expiry and recovery may be preferable to selection based only on variety.

**Class:** `inference`. **Support/contradiction:** Proposed policy adds design judgments not proved by either source.

**Sources and precise locators:** GDR-SRC-20261010-W02-005, GDR-SRC-20261010-W02-007 — Saliency/no-selection facilities; XAG 104 supplementary speech coverage.

**Applicability:** Task-critical and flavor lines require different failure costs. **Confidence:** low for comparative effectiveness; moderate for exposing authoring risks. **Unresolved:** Does it reduce missed or false information without disruptive repetition?

### C-13

**Claim:** Choose performance and localization commitments by their intended meaning and recoverability, and audit changes across representations instead of assuming more voice or literal translation is always better.

**Class:** `inference`. **Support/contradiction:** A conditional synthesis; includes original ethical/production review proposals.

**Sources and precise locators:** GDR-SRC-20261010-W02-006, GDR-SRC-20261010-W02-007, GDR-SRC-20261010-W02-009, GDR-SRC-20261010-W02-010 — Line-associated assets; accessibility information coverage; LQA; recording context.

**Applicability:** No cost threshold, guaranteed voice benefit, rights approval or approved casting policy. **Confidence:** moderate for identifying dependencies, low for comparative outcome benefits. **Unresolved:** Which meanings change with delivery, translation and presentation for this audience?

### C-14

**Claim:** The Mask of the Rose article supplies a creator-reported example of constrained expressive options, not evidence for a universal menu size.

**Class:** `practitioner-heuristic`. **Support/contradiction:** Creator account only; not independent gameplay observation.

**Sources and precise locators:** GDR-SRC-20261010-W02-004 — Wardrobe/personality and dialogue-expression discussion.

**Applicability:** Then-current game revision, exact build unknown. **Confidence:** moderate for the report; no measured effect inferred. **Unresolved:** Which effects arise from constraints, writing quality or audience familiarity?

### C-15

**Claim:** Separate speech-act understanding, downstream expectations, interruption recovery and cross-context application in validation; these are proposed tests, not completed evidence.

**Class:** `hypothesis`. **Support/contradiction:** Falsifying comparisons are specified; no study was executed.

**Sources and precise locators:** Original author proposal; no direct empirical source — Original validation design in this entry.

**Applicability:** Local sampling, access needs, coding and decision thresholds must be agreed before testing. **Confidence:** low for the proposed interventions; explicit uncertainty is retained. **Unresolved:** Do results transfer beyond recognized examples to unfamiliar dialogue contexts?


## References

Access date for every record below: **2026-10-10**. “Inspected” means the stated text/pages, not an entire linked corpus, game build, video or cited book. Source identities are temporary; cross-batch canonical URL/DOI/edition deduplication remains pending.

### GDR-SRC-20261010-W02-001

**Rogelio E. Cardona-Rivera; Justus Robertson; Stephen G. Ware; Brent Harrison; David L. Roberts; R. Michael Young.** [Foreseeing Meaningful Choices](https://ojs.aaai.org/index.php/AIIDE/article/view/12716). AAAI, AIIDE 10(1), pp. 9–15. Publication/update: 2014-10-08.

**Edition/build:** Published 2014 paper; seven-page publisher PDF. **Access:** `relevant-excerpt`. **Source type:** Original empirical research.

**Precise locators used:** pp. 11–12, Experimental Design and Results; p. 13, Tables 5–6 and Figure 2; p. 14, Limitations and Future Work. Tables/figure inspected as a PDF screenshot.

**Claims supported or constrained in this entry:** C-02, C-11. **Limits:** Retrospective self-report in a short text-story paradigm; not a voiced-game trial. **Independence:** Shares authors and a research paradigm with source 002; not an independent replication.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

**DOI:** [10.1609/aiide.v10i1.12716](https://doi.org/10.1609/aiide.v10i1.12716).

### GDR-SRC-20261010-W02-002

**Matthew William Fendt; Brent Harrison; Stephen G. Ware; Rogelio E. Cardona-Rivera; David L. Roberts.** [Achieving the Illusion of Agency](https://www.cs.uky.edu/~sgware/reading/papers/fendt2012achieving.pdf). Springer, ICIDS 2012, LNCS 7648, pp. 114–125. Publication/update: 2012; exact publication day not established.

**Edition/build:** Twelve-page author-hosted paper; locators use PDF page numbers rather than proceedings pagination. **Access:** `relevant-excerpt`. **Source type:** Original empirical research.

**Precise locators used:** PDF pp. 3–8, design and hypotheses; pp. 8–10, Results; p. 9, Tables 1–2, inspected as a screenshot; pp. 10–11, Discussion.

**Claims supported or constrained in this entry:** C-03, C-11. **Limits:** Unequal/downselected groups and no equivalence design; narrow self-report study. **Independence:** Overlapping authors with source 001. Other university mirrors are the same work, not additional evidence.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

**DOI:** [10.1007/978-3-642-34851-8_11](https://doi.org/10.1007/978-3-642-34851-8_11).

### GDR-SRC-20261010-W02-003

**Emily Short.** [Conversational analysis studies](https://emshort.blog/2009/08/08/conversational-analysis-studies/). Emily Short’s Interactive Storytelling. Publication/update: 2009-08-08; page also displays 2010-10-08 as a subsequent date.

**Edition/build:** Blog article, inspected 2026-10-10. **Access:** `relevant-excerpt`. **Source type:** First-person practitioner analysis.

**Precise locators used:** Article body: nested question/answer discussion; paragraphs following the lift-to-a-party examples; final discussion of turn-taking abstractions. Comments excluded.

**Claims supported or constrained in this entry:** C-01, C-04, C-05, C-11. **Limits:** Advice about interactive fiction; cited linguistics book was not independently inspected. **Independence:** Same author as sources 004 and 014; her discussion of Levinson is secondary to that book.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-004

**Emily Short.** [Dialogue Expressiveness in Mask of the Rose](https://emshort.blog/2023/11/22/dialogue-expressiveness-in-mask-of-the-rose/). Emily Short’s Interactive Storytelling. Publication/update: 2023-11-22.

**Edition/build:** Creator account of the then-latest release; exact game build not supplied. **Access:** `relevant-excerpt`. **Source type:** First-person creator account.

**Precise locators used:** Article body: wardrobe/personality selection; seen-content versus remembered/understood content; theory construction and revision discussion. Images not used as independent observations.

**Claims supported or constrained in this entry:** C-14. **Limits:** No reported controlled player-effect estimate and no direct gameplay inspection here. **Independence:** Same author as sources 003 and 014; not independent corroboration across those articles.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-005

**Yarn Spinner documentation contributors.** [Saliency](https://docs.yarnspinner.dev/write-yarn-scripts/advanced-scripting/saliency). Yarn Spinner. Publication/update: unknown.

**Edition/build:** Live, unpinned documentation snapshot checked 2026-10-10; no exact release number established. **Access:** `relevant-excerpt`. **Source type:** Official product documentation.

**Precise locators used:** What is saliency?; content-selection strategy descriptions and the no-selection case in the inspected text body.

**Claims supported or constrained in this entry:** C-06, C-12. **Limits:** Describes selection facilities, not their player-experience effectiveness. **Independence:** Same documentation/product family as source 006. Cached search excerpts were not substituted for the live body.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-006

**Yarn Spinner documentation contributors.** [Localisation and Assets](https://docs.yarnspinner.dev/yarn-spinner-for-unity/assets-and-localization). Yarn Spinner. Publication/update: unknown.

**Edition/build:** Live, unpinned Unity documentation snapshot checked 2026-10-10. **Access:** `relevant-excerpt`. **Source type:** Official product documentation.

**Precise locators used:** Inspected body on localized strings/assets, voice assets associated with lines, and line IDs including options.

**Claims supported or constrained in this entry:** C-07, C-13. **Limits:** Evidence of a documented authoring facility, not a mandated architecture or cost model. **Independence:** Same documentation/product family as source 005; not independent efficacy evidence.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-007

**Microsoft.** [Xbox Accessibility Guideline 104: Subtitles and captions](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104). Microsoft Learn. Publication/update: last updated 2026-03-04.

**Edition/build:** Live XAG 104 page checked 2026-10-10; overview identifies the guideline collection as V3.2. **Access:** `relevant-excerpt`. **Source type:** Official accessibility best-practice guidance.

**Precise locators used:** Overview; Implementation guidelines: spoken content, supplementary speech, speaker/direction information, availability of settings, significant non-speech information. Numerical settings not transferred.

**Claims supported or constrained in this entry:** C-08, C-12, C-13. **Limits:** Not classified as a formal standard or legal/compliance requirement; see source 008. **Independence:** Same issuer/collection as source 008; not two independent evaluations.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-008

**Microsoft.** [Xbox Accessibility Guidelines V3.2](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines). Microsoft Learn. Publication/update: V3.2 dated 2023-06-08; later page-edit date not used as a new edition.

**Edition/build:** V3.2 overview; checked 2026-10-10. **Access:** `relevant-excerpt`. **Source type:** Official guidance scope declaration.

**Precise locators used:** Opening overview, particularly the best-practice and not-legal/compliance-checklist scope statement.

**Claims supported or constrained in this entry:** C-08. **Limits:** Public relevant text was readable despite a page-shell authorization notice. **Independence:** Scope companion to source 007, not independent design evidence.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-009

**Jennifer O’Donnell, with the named professional contributors acknowledged in the article.** [How to Get the Most from LQA – What It Is and Best Practices](https://igda.org/news-archive/how-to-get-the-most-from-lqa-what-it-is-and-best-practices/). IGDA. Publication/update: 2023-05-31.

**Edition/build:** Dated professional guidance article. **Access:** `relevant-excerpt`. **Source type:** Practitioner guidance.

**Precise locators used:** What is LQA?; What happens during LQA?; discussion of context, characterization, terminology, UI and source changes during testing.

**Claims supported or constrained in this entry:** C-10, C-13. **Limits:** Professional recommendations, not a controlled comparison of localization workflows. **Independence:** Shares the IGDA localization practice network with source 010; not an independent player study.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-010

**IGDA Localization SIG; second draft edited by Jon Fung, following Richard Honeywood’s initial draft.** [Best Practices for Game Localization](https://igda-website.s3.us-east-2.amazonaws.com/wp-content/uploads/2021/04/09142137/Best-Practices-for-Game-Localization-v22.pdf). IGDA. Publication/update: second draft 2012-02-01; republished edited copy 2021-04-09.

**Edition/build:** Second-draft guide; filename v22; 2021 hosting is not a new empirical study. **Access:** `relevant-excerpt`. **Source type:** Professional practice guide.

**Precise locators used:** Voice-Over Recording, printed pp. 19–20 / PDF pp. 22–23, both inspected as screenshots; contextual direction and recorded-script/subtitle consistency.

**Claims supported or constrained in this entry:** C-09, C-13. **Limits:** Historical guidance; regional stereotypes, staffing ratios and cost figures not adopted. **Independence:** Same professional network as source 009; edition and repost date kept separate.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.


## Open questions and change history

**Coverage checkpoint:** conversational structure, choices and subtext have primary practitioner coverage plus limited adjacent empirical evidence; barks have official selection/access documentation but no inspected player-effect trial; performance and localization have practitioner workflow evidence, not cost or efficacy benchmarks. Independent W02 review is pending for every subtopic.

**Unresolved:** live conversational overlap, nonverbal/sign-language performance, culturally specific indirect speech, non-English agency measures, repeated-play trust, performer workload and fatigue, and generated-voice governance remain outside the inspected evidence. The Valve/Ruskin 2012 talk is a verified metadata lead whose PDF could not be retrieved; no claims here rely on its unread slides.

**Dependencies:** reviewed W01 character/world/narrative bytes; Presentation localization, interface, audio and performance guidance; Foundations decision/evaluation guidance. Exact unseen entry IDs and links remain unassigned in this package. The supplied parent correction about numerical accessibility scope is preserved; the transfer test above distinguishes recognition from application rather than treating similar examples as proof.

**Conflicts:** W02 local conflict labels `dialogue-control`, `feedback-equivalence` and `clarity-versus-subtext` are recorded in the [review packet](../reviews/full-run-20261010-w02-review-packet.md#contradictions-and-contested-claims). They are not permanent register IDs.

**History:** 2026-10-10 — version 0.1.0, `initial-draft-1`, first W02 submission. Predecessor hash and supersession: null. Author self-review completed; independent review, approval and release absent. Exact delivered byte hash appears in the packet manifest. Next decision: independent evidence/content review of the qualified recommendation, not implementation or canon adoption.

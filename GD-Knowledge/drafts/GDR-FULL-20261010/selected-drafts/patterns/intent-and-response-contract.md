---
id: GDR-CAND-20261010-W02-PAT-01
kind: pattern
title: Intent and response contract
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
- dialogue intent contract
- speech-act consistency
- choice-to-line audit
tags:
- dialogue
- commitment
- recognition
- localization
- accessibility
related_topics:
- GDR-CAND-20261010-W02-TOP-01
- GDR-CAND-20261010-W02-TOP-02
- GDR-CAND-20261010-W02-TOP-03
related_patterns:
- GDR-CAND-20261010-W02-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-W02-001
- GDR-SRC-20261010-W02-002
- GDR-SRC-20261010-W02-003
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

# Intent and response contract

**Draft research candidate — not released guidance.** Candidate identity is run-scoped, not a permanent GDK allocation. No W02 independent review, gameplay prototype or player test has occurred.

## Purpose

Help a designer prevent a selectable conversational contribution from becoming an unadvertised threat, promise, concession or disclosure. The intended benefit is more accurate player understanding of the contribution and its recognition, **not guaranteed persuasion, successful outcomes, different endings or a proven increase in agency**. This is a new conditional pattern proposal. [C-01]

## Context and prerequisites

Use when a player selects an utterance or intention and a protagonist then speaks or acts on it. Prerequisites are an identifiable intended speech act, the actual line or permitted performance range, a known immediate response, and an authoring team able to reconcile wording, presentation and any promised later consequence. These are conceptual authoring requirements, not a prescribed runtime data model. [C-01, C-04]

The player may remain uncertain about an interlocutor’s motive and the eventual outcome. The proposed contract concerns what the **player is making the protagonist do**, not an omniscient forecast. A game built around interpreting exact phrasing needs a different degree of explicitness. An autonomous protagonist’s fixed action may be better presented as an authored event than a choice that falsely implies control. [C-03]

**Prerequisite failure:** if no one can specify whether a line is inquiry, acceptance, promise or refusal, stop polishing its menu label. Resolve the authoring ambiguity or remove the selectable commitment. If a cross-language or performed version cannot currently preserve the intended contribution, keep that variant unapproved for application rather than assume the source-language line proves it works. [C-01, C-07]

## Mechanism and evidence

| Proposed causal link | Support and classification | Limit or competing explanation |
|---|---|---|
| A player can recognize the contribution before committing. | Intention-versus-literal-line advice supplies a practitioner rationale; the contract is a hypothesis. [C-01, C-03] | A clearer label may reveal a desired language challenge or reduce expressive ambiguity. |
| The performed utterance remains within that contribution. | This is a checkable authoring relationship, supported by the possibility of tracking line-associated versions, not a measured player effect. [C-04, C-07] | Matching text does not guarantee matching implication; tone and translation can change commitment. |
| The immediate response recognizes what was contributed. | Adjacent text-agency studies motivate examining recognition separately. [C-02] | Their results do not establish a universal feedback benefit or branching/feedback equivalence. |
| Later recognition matches the scope advertised. | Original consistency proposal. [C-01] | Prominent immediate feedback may inflate expectations of long-term effects that do not exist. |
| Fewer mismatches improve trust or expression. | Testable hypothesized benefit, not established evidence. [C-06] | Players may prefer subtler dialogue or attribute coherence to writing quality rather than the contract. |

The two agency papers are one overlapping research family, not independent confirmation of this recipe. No inspected experiment compares the complete pattern against a well-written alternative. Their negative/qualified results constrain the claim rather than validate a cost-saving illusion of choice. [C-02]

## Recipe

1. **Name the intended contribution.** Write a plain-language description such as “request temporary use,” “refuse the offer,” or “admit uncertainty.” Separately state what remains outside player control. Do not encode the other character’s hidden judgment as the player’s intention. [C-01]
2. **Specify the acceptance boundary.** Identify any obligation, cost, disclosure or relationship stance created by selecting it. Decide whether selection merely asks a question or accepts a condition. A question about repayment should not itself incur the debt. [C-01]
3. **Choose the presentation.** Use literal wording when selecting words is the action; use an intention label when indirect delivery would otherwise obscure commitment; consider a preview or fixed scene instead. Do not add an “honest,” “correct” or “successful” label unless that information is intentionally available. [C-03]
4. **Align the utterance and performance.** Compare the label or preview to the delivered line, its implied force and the range of acceptable delivery. Review each supported language/context as a complete exchange. Keep unresolved variants separate from accepted ones in the authoring review. [C-04, C-07]
5. **Write the recognition.** Show the other speaker answering, rejecting, misunderstanding in a deliberately framed way, or asking for clarification. An intentional misunderstanding can be valid when the player can distinguish it from the protagonist having said something else. [C-01]
6. **State the horizon and recovery.** Record whether the effect is immediate expression, information access, a persistent promise or a later outcome. Specify how a skipped, interrupted or revisited exchange preserves the correct commitment. Do not silently replay an irreversible decision to recover context. [C-01, C-05]
7. **Compare and revise.** Test intended versus understood contribution before optimizing preference or agency ratings. If the label explains too much, shift to contextual evidence, preview or narrower choice rather than eliminating the intended challenge. If the promised consequence is unsupported, remove the promise or explicitly author the consequence before acceptance. [C-06]

### Adjustable variables

The variables are **explicitness of the label**, literal versus intention wording, availability of a preview, when recognition occurs, how long the consequence persists, options for clarification/repetition, and which meanings performance/captions/localization convey. No fixed option count, reading duration or response latency is prescribed. Test these variables one at a time where feasible; otherwise record which changed together. [C-06, C-07]

### Exit and stop conditions

Stop applying the pattern as an intention-label solution when interpreting the speech act is the desired challenge, when the protagonist is not under player control at that moment, or when the team cannot honor the advertised commitment. Stop expanding options when new ones merely obscure a decision that a simpler exchange handles well. Retain an explicit unresolved item when locale/performance meaning cannot be validated; do not declare equivalence from a fluent back-translation. [C-03, C-06, C-07]

## Worked examples

### Illustrative: borrow a replacement regulator

An engineer holds a spare regulator. The player’s goal is to get the pump working, but borrowing may create a later obligation. This is invented material, not approved canon or observed gameplay.

| Contract element | Proposed content |
|---|---|
| Selected contribution | Ask whether a temporary loan is possible. |
| Option | “Ask to borrow the regulator.” |
| Performed line | “Could we use your spare until ours is repaired?” |
| Immediate response | “Only if you bring it back before my inspection.” |
| Obligation created by this selection | None yet; the engineer has offered a condition. |
| Next choice | Accept the return obligation, negotiate it, or decline. |
| Persistent result after acceptance | The agreed obligation remains recoverable in the current task record. |

The contract exposes a common mistake: treating the first inquiry as acceptance. The repair is not to guarantee a friendly response; it is to separate request from agreement. The engineer may refuse, distrust the player or request collateral without violating the player’s selected contribution. [C-01; illustrative]

A locale may naturally phrase the request indirectly. The review asks whether it remains a request rather than a demand or a promise, not whether every word corresponds. A spoken performance can imply impatience without silently turning the request into a threat. A caption need not call the protagonist “deceptive” when that is not independently conveyed. [C-05, C-07; illustrative]

### Illustrative: deliberate misinterpretation

A suspicious official chooses to treat the same polite request as an attempt at intimidation. The response can explicitly locate the interpretation in the official: “You expect me to risk my position for you?” The player still knows what the protagonist asked and may clarify or disengage. This is different from performing an unexpected threat on the player’s behalf. Whether the scene communicates that distinction is a proposed test question, not assumed success. [C-01, C-06; illustrative]

## Tradeoffs and alternatives

A contract adds authoring/review work and can make subtle exchanges feel schematic if its internal labels are exposed literally. It may be most useful as a backstage audit, leaving polished dialogue unannotated. A full-line preview can preserve diction but adds reading; intention labels can shorten selection but need careful adaptation; a fixed scene avoids false control but reduces available expression. [C-03, C-07]

Not every expressive choice needs future branching. Do not add costly consequences solely to satisfy the contract; reduce the advertised consequence instead. A temporary affective response, access to a question or an honest lack of further effect can be the intended scope. Whether it is satisfying remains an empirical question. [C-01, C-02, C-06]

## Failure cases

| Warning sign | Likely design problem | Proposed correction |
|---|---|---|
| Players paraphrase a promise as a question. | Acceptance boundary is unclear. | Separate inquiry and commitment, or expose the commitment in the option. [C-01] |
| Players correctly predict the line but not its force. | Tone, translation or context changes the speech act. | Review the performed exchange in context, not only the string. [C-07] |
| Players expect a later branch from a local acknowledgement. | Recognition overstates the horizon. | Reframe the immediate response or provide the advertised consequence; do not claim the study justifies deception. [C-01, C-02] |
| Players know the correct answer before examining the scene. | Labels disclose the interpretive task. | Remove the solution annotation; supply context or an explicitly chosen assist. [C-03, C-06] |
| Re-entry repeats a commitment or forgets an accepted condition. | Recovery is based on stale dialogue rather than the current situation. | Provide an accurate reminder or clarification route. [C-01, C-05] |

## Counterexamples and do not use conditions

The strongest counterexample is a conversation in which identifying the intention behind a possible utterance is the challenge. In an illustrative diplomatic test, labeling an indirect insult as “provoke the envoy” supplies the answer. Keep the exact wording and sufficient contextual evidence; provide a separately designed assist where appropriate rather than claiming the same task has been preserved automatically. [C-03, C-06]

Do not use the pattern to guarantee persuasion, certify cultural appropriateness, justify hidden coercive choices, replace performance direction or claim that a reconverging branch equals a consequential one. It diagnoses promises; it does not create missing content or an independent evidence basis. [C-01, C-02, C-07]

## Playtest

**Proposed, not performed.** Compare a contract-audited exchange with a polished unaudited alternative; include a literal-preview version where relevant. Hold the offered decisions, plot outcomes, writing quality and presentation access as consistent as possible. Counterbalance scenes/order and include an unfamiliar setting that does not merely reuse the worked example’s nouns. [C-06]

Before selection, elicit the predicted contribution and obligation without revealing the designer’s categories. Afterward, ask what was said, what the other person recognized and what players expect later. Examine mismatch, confidence, trust, expressive fit and unwanted solution disclosure separately. Include relevant locale expertise, speech/text access needs and differing familiarity with indirect dialogue. Use independent coding where practical; no such coding has occurred here. [C-06, C-07]

**Falsification/decision rule:** reject or narrow the intervention when it fails to reduce the targeted commitment mismatch, improves literal recall without improving unfamiliar-case understanding, increases false future expectations, or removes a valued interpretive challenge. Do not treat a nonsignificant agency rating as equivalence or set an arbitrary universal passing percentage. Agree locally on the seriousness of an unadvertised commitment, practical margins and sampling precision before collecting data. [C-02, C-06]

## Claim ledger

Claim identifiers are local to this artifact. Confidence describes the stated narrow claim, not proof that the proposed technique improves a game. `inference` and `hypothesis` recommendations are author proposals, not approved studio decisions.

### C-01

**Claim:** Auditing contribution, commitment, recognition and consequence horizon may prevent unadvertised conversational actions without promising successful outcomes.

**Class:** `hypothesis`. **Support/contradiction:** Practitioner rationale plus original conditional mechanism, not a validated pattern.

**Sources and precise locators:** GDR-SRC-20261010-W02-003 — Intention/literal-command discussion; complete recipe is original synthesis.

**Applicability:** Selectable protagonist contributions; not all fixed or interpretive scenes. **Confidence:** low for measured benefits; authoring consistency can be inspected directly. **Unresolved:** Does the player actually understand the commitment with fewer unintended effects?

### C-02

**Claim:** The adjacent agency studies limit rather than prove a general feedback or reconvergence equivalence claim.

**Class:** `empirical-evidence`. **Support/contradiction:** Qualified/negative findings; detailed evidence capsule is in the related dialogue topic.

**Sources and precise locators:** GDR-SRC-20261010-W02-001, GDR-SRC-20261010-W02-002 — 001 pp. 12–14; 002 PDF pp. 8–10, Table 2 and Hypothesis 2 result.

**Applicability:** Short text-story research family, not this recipe or voice/localization evidence. **Confidence:** moderate for the narrow interpretation of inspected results. **Unresolved:** What does an independently evaluated contract change beyond immediate self-report?

### C-03

**Claim:** Intention labels are conditional and may be inappropriate when interpretation of exact wording is the task.

**Class:** `practitioner-heuristic`. **Support/contradiction:** Direct practitioner qualification.

**Sources and precise locators:** GDR-SRC-20261010-W02-003 — Text/subtext paragraph and its explicit exception.

**Applicability:** Indirect dialogue and interpretive tasks require different information choices. **Confidence:** moderate for the advice, low for universal preference prediction. **Unresolved:** How much clarification preserves rather than solves the task?

### C-04

**Claim:** Line-associated versions are a documented possibility, not a prescription for how a project must implement the audit.

**Class:** `observed-example`. **Support/contradiction:** Official document inspected; no tool execution.

**Sources and precise locators:** GDR-SRC-20261010-W02-006 — Localized strings/assets and line identifiers.

**Applicability:** Unpinned documentation snapshot only. **Confidence:** high for the narrow facility description. **Unresolved:** Can the actual authoring workflow retain the relevant context?

### C-05

**Claim:** Accessible recovery should preserve the information conveyed by the exchange without adding an unsupported verdict about hidden intent.

**Class:** `inference`. **Support/contradiction:** Professional access guidance plus a proposed epistemic limit.

**Sources and precise locators:** GDR-SRC-20261010-W02-007, GDR-SRC-20261010-W02-008 — XAG 104 information coverage; V3.2 scope; no-omniscience condition authored here.

**Applicability:** Requires actual presentation/locale review; no universal settings. **Confidence:** moderate for the design concern, low for comparative success. **Unresolved:** Which meanings are lost or added in each supported access route?

### C-06

**Claim:** The intended benefit and stop conditions should be evaluated through contribution prediction, unfamiliar-case understanding and unwanted disclosure, not only agency ratings.

**Class:** `hypothesis`. **Support/contradiction:** No test or participant result exists for this pattern.

**Sources and precise locators:** GDR-SRC-20261010-W02-001, GDR-SRC-20261010-W02-002 — Study limitations motivate measures; comparison procedure is original.

**Applicability:** Local sampling and practical criteria are unresolved. **Confidence:** low for the intervention’s benefit. **Unresolved:** Does it outperform a simpler well-written exchange for the targeted problem?

### C-07

**Claim:** Performance and localized variants require contextual semantic review rather than assuming surface correspondence preserves the contribution.

**Class:** `inference`. **Support/contradiction:** Conditional production synthesis; no measured cost or quality claim.

**Sources and precise locators:** GDR-SRC-20261010-W02-006, GDR-SRC-20261010-W02-009, GDR-SRC-20261010-W02-010 — Line-associated assets; LQA context; recording guide pp. 19–20.

**Applicability:** No implementation, performer consent, locale or casting approval implied. **Confidence:** moderate for identifying dependencies, low for demonstrated benefit. **Unresolved:** Which variants change commitments or intended ambiguity?


## References

Access date for every record below: **2026-10-10**. “Inspected” means the stated text/pages, not an entire linked corpus, game build, video or cited book. Source identities are temporary; cross-batch canonical URL/DOI/edition deduplication remains pending.

### GDR-SRC-20261010-W02-001

**Rogelio E. Cardona-Rivera; Justus Robertson; Stephen G. Ware; Brent Harrison; David L. Roberts; R. Michael Young.** [Foreseeing Meaningful Choices](https://ojs.aaai.org/index.php/AIIDE/article/view/12716). AAAI, AIIDE 10(1), pp. 9–15. Publication/update: 2014-10-08.

**Edition/build:** Published 2014 paper; seven-page publisher PDF. **Access:** `relevant-excerpt`. **Source type:** Original empirical research.

**Precise locators used:** pp. 11–12, Experimental Design and Results; p. 13, Tables 5–6 and Figure 2; p. 14, Limitations and Future Work. Tables/figure inspected as a PDF screenshot.

**Claims supported or constrained in this entry:** C-02, C-06. **Limits:** Retrospective self-report in a short text-story paradigm; not a voiced-game trial. **Independence:** Shares authors and a research paradigm with source 002; not an independent replication.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

**DOI:** [10.1609/aiide.v10i1.12716](https://doi.org/10.1609/aiide.v10i1.12716).

### GDR-SRC-20261010-W02-002

**Matthew William Fendt; Brent Harrison; Stephen G. Ware; Rogelio E. Cardona-Rivera; David L. Roberts.** [Achieving the Illusion of Agency](https://www.cs.uky.edu/~sgware/reading/papers/fendt2012achieving.pdf). Springer, ICIDS 2012, LNCS 7648, pp. 114–125. Publication/update: 2012; exact publication day not established.

**Edition/build:** Twelve-page author-hosted paper; locators use PDF page numbers rather than proceedings pagination. **Access:** `relevant-excerpt`. **Source type:** Original empirical research.

**Precise locators used:** PDF pp. 3–8, design and hypotheses; pp. 8–10, Results; p. 9, Tables 1–2, inspected as a screenshot; pp. 10–11, Discussion.

**Claims supported or constrained in this entry:** C-02, C-06. **Limits:** Unequal/downselected groups and no equivalence design; narrow self-report study. **Independence:** Overlapping authors with source 001. Other university mirrors are the same work, not additional evidence.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

**DOI:** [10.1007/978-3-642-34851-8_11](https://doi.org/10.1007/978-3-642-34851-8_11).

### GDR-SRC-20261010-W02-003

**Emily Short.** [Conversational analysis studies](https://emshort.blog/2009/08/08/conversational-analysis-studies/). Emily Short’s Interactive Storytelling. Publication/update: 2009-08-08; page also displays 2010-10-08 as a subsequent date.

**Edition/build:** Blog article, inspected 2026-10-10. **Access:** `relevant-excerpt`. **Source type:** First-person practitioner analysis.

**Precise locators used:** Article body: nested question/answer discussion; paragraphs following the lift-to-a-party examples; final discussion of turn-taking abstractions. Comments excluded.

**Claims supported or constrained in this entry:** C-01, C-03. **Limits:** Advice about interactive fiction; cited linguistics book was not independently inspected. **Independence:** Same author as sources 004 and 014; her discussion of Levinson is secondary to that book.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-006

**Yarn Spinner documentation contributors.** [Localisation and Assets](https://docs.yarnspinner.dev/yarn-spinner-for-unity/assets-and-localization). Yarn Spinner. Publication/update: unknown.

**Edition/build:** Live, unpinned Unity documentation snapshot checked 2026-10-10. **Access:** `relevant-excerpt`. **Source type:** Official product documentation.

**Precise locators used:** Inspected body on localized strings/assets, voice assets associated with lines, and line IDs including options.

**Claims supported or constrained in this entry:** C-04, C-07. **Limits:** Evidence of a documented authoring facility, not a mandated architecture or cost model. **Independence:** Same documentation/product family as source 005; not independent efficacy evidence.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-007

**Microsoft.** [Xbox Accessibility Guideline 104: Subtitles and captions](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104). Microsoft Learn. Publication/update: last updated 2026-03-04.

**Edition/build:** Live XAG 104 page checked 2026-10-10; overview identifies the guideline collection as V3.2. **Access:** `relevant-excerpt`. **Source type:** Official accessibility best-practice guidance.

**Precise locators used:** Overview; Implementation guidelines: spoken content, supplementary speech, speaker/direction information, availability of settings, significant non-speech information. Numerical settings not transferred.

**Claims supported or constrained in this entry:** C-05. **Limits:** Not classified as a formal standard or legal/compliance requirement; see source 008. **Independence:** Same issuer/collection as source 008; not two independent evaluations.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-008

**Microsoft.** [Xbox Accessibility Guidelines V3.2](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines). Microsoft Learn. Publication/update: V3.2 dated 2023-06-08; later page-edit date not used as a new edition.

**Edition/build:** V3.2 overview; checked 2026-10-10. **Access:** `relevant-excerpt`. **Source type:** Official guidance scope declaration.

**Precise locators used:** Opening overview, particularly the best-practice and not-legal/compliance-checklist scope statement.

**Claims supported or constrained in this entry:** C-05. **Limits:** Public relevant text was readable despite a page-shell authorization notice. **Independence:** Scope companion to source 007, not independent design evidence.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-009

**Jennifer O’Donnell, with the named professional contributors acknowledged in the article.** [How to Get the Most from LQA – What It Is and Best Practices](https://igda.org/news-archive/how-to-get-the-most-from-lqa-what-it-is-and-best-practices/). IGDA. Publication/update: 2023-05-31.

**Edition/build:** Dated professional guidance article. **Access:** `relevant-excerpt`. **Source type:** Practitioner guidance.

**Precise locators used:** What is LQA?; What happens during LQA?; discussion of context, characterization, terminology, UI and source changes during testing.

**Claims supported or constrained in this entry:** C-07. **Limits:** Professional recommendations, not a controlled comparison of localization workflows. **Independence:** Shares the IGDA localization practice network with source 010; not an independent player study.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-010

**IGDA Localization SIG; second draft edited by Jon Fung, following Richard Honeywood’s initial draft.** [Best Practices for Game Localization](https://igda-website.s3.us-east-2.amazonaws.com/wp-content/uploads/2021/04/09142137/Best-Practices-for-Game-Localization-v22.pdf). IGDA. Publication/update: second draft 2012-02-01; republished edited copy 2021-04-09.

**Edition/build:** Second-draft guide; filename v22; 2021 hosting is not a new empirical study. **Access:** `relevant-excerpt`. **Source type:** Professional practice guide.

**Precise locators used:** Voice-Over Recording, printed pp. 19–20 / PDF pp. 22–23, both inspected as screenshots; contextual direction and recorded-script/subtitle consistency.

**Claims supported or constrained in this entry:** C-07. **Limits:** Historical guidance; regional stereotypes, staffing ratios and cost figures not adopted. **Independence:** Same professional network as source 009; edition and repost date kept separate.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.


## Related entries and history

Related topics: [Dialogue and voice](../topics/dialogue-and-voice.md), `GDR-CAND-20261010-W02-TOP-01`; [Quests and objectives](../topics/quests-and-objectives.md), `GDR-CAND-20261010-W02-TOP-02`; [Lore delivery and continuity](../topics/lore-delivery-and-continuity.md), `GDR-CAND-20261010-W02-TOP-03`. Complement: [Multi-route objective contract](multi-route-objective-contract.md), `GDR-CAND-20261010-W02-PAT-02`.

No reviewed genre file or W01 dependency bytes were inspected. Conflicts `dialogue-control`, `feedback-equivalence` and `clarity-versus-subtext` remain open in the [packet](../reviews/full-run-20261010-w02-review-packet.md#contradictions-and-contested-claims). Cross-locale speech-act understanding, performed interruption and repeated-play trust are evidence gaps, not certified coverage.

2026-10-10 — version 0.1.0, `initial-draft-1`; initial W02 pattern submission. Predecessor and supersession null. Author self-review only; independent review and approval absent. Exact hash in the packet. This pattern has no permanent GDK identity and is not released or adopted.

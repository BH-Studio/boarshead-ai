---
id: GDR-CAND-20261010-W02-TOP-03
kind: topic
title: Lore delivery and continuity
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
- lore
- codex design
- continuity
- canon management
- unreliable testimony
tags:
- discoverability
- optional-depth
- codex
- provenance
- canon
- contradictions
- localization
related_topics:
- GDR-CAND-20261010-W02-TOP-01
- GDR-CAND-20261010-W02-TOP-02
related_patterns:
- GDR-CAND-20261010-W02-PAT-01
- GDR-CAND-20261010-W02-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-W02-004
- GDR-SRC-20261010-W02-009
- GDR-SRC-20261010-W02-010
- GDR-SRC-20261010-W02-015
- GDR-SRC-20261010-W02-016
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

# Lore delivery and continuity

**Draft research candidate — not released guidance.** Candidate identity is run-scoped, not a permanent GDK allocation. No W02 independent review, gameplay prototype or player test has occurred.

## Decision and scope

**Decision:** What world information should a player encounter, revisit, interpret or be allowed to ignore, and how should its authority and revision history remain coherent? This topic covers discoverability, optional depth, codex design, approved canon and contradiction management. It does not establish the canon of any named game or prescribe a narrative database, save system or runtime owner.

Working definitions: **lore** is information and perspective concerning a fictional world beyond the immediate action instruction; a **codex** is a revisitable collection of such information, whether diegetic or not; **continuity** is the managed relationship among claims, events and representations across contexts and revisions. “Optional” must name what remains possible without engagement: progression, informed decision-making, emotional interpretation, completionist recognition or something else. It is not synonymous with unimportant. [C-01, C-06]

A proposed authoring distinction separates **approved fictional facts**, **claims made by a source within the fiction**, **records exposed to the player**, and **interpretations the player may form**. Exposure to a record does not establish that the player read it, remembers it, believes it or has inferred its implications. The distinction is a design aid, not a claim that a system can know a player’s internal beliefs. [C-01, C-07]

**Authority boundary:** no approved game canon, canon-owner decision, reviewed world bible or independent W02 review is supplied. The W02 dispatch authorizes research only. All invented content below is illustrative; the proposed continuity workflow cannot silently approve its own facts. W01 worldbuilding/narrative/character dependencies are parent-reviewed by receipt but their reviewed bytes are missing here.

## Core explanation and mechanisms

### Progression can depend on discovery without depending on one correct interpretation

Inkle’s creator account supplies a concrete distinction between finding artifacts and correctly translating them in *Heaven’s Vault*. Together with the quest topic, it limits an assumption that world understanding always has to gate access. It does not show that optional lore is inherently better, or that a knowledge-centered game should abandon interpretive gates. [C-02; GDR-SRC-20261010-W02-015]

Short’s account of *Mask of the Rose* distinguishes exposed content from remembered/understood content and describes a way for players to construct and use theories. That is a creator-reported design approach, not evidence that an inferred “player knows” flag can substitute for an expressed hypothesis. [C-03; GDR-SRC-20261010-W02-004]

The proposed bridge is to specify the **knowledge contract**. A player may need to know that a gate is locked, discover a document about it, infer who locked it, or prove an accusation. Each asks something different. A codex should not turn discovery of a document into confirmation of its allegation unless the intended fiction and task warrant that change. [C-06, C-07]

### Delivery defects and deliberate uncertainty require different treatment

Mobius Digital’s 1.1.15 patch notes report fixes to writing consistency, ship-log display and localized text availability. These are versioned developer-reported defects/fixes, not observations from a running game in this batch. Their relevance is that missing or inconsistent presentation can have a mundane production explanation; it should not automatically be interpreted as an authored mystery. [C-04; GDR-SRC-20261010-W02-016]

Our inference is to triage an apparent conflict before interpreting it. Two witnesses may disagree intentionally. Two locales may inadvertently assert different dates. A world rule may have changed between editions. A hidden condition may make both statements true. These explanations call for different actions, and none can be chosen merely because it preserves a favored reading. [C-10]

### Access can preserve interpretation without preserving an inaccessible surface

Naughty Dog’s official PS4-era feature description includes in-world text translation prompts and text-to-speech support. It documents possible presentation routes, not a universal configuration or measured improvement for every reader. [C-05; GDR-SRC-20261010-W02-017]

The application proposal is **information access without extra certainty**. A readable or spoken rendering of a weathered note can preserve its attribution and uncertainty. It need not reveal the correct suspect, complete erased text or explain a pun that constitutes the task. Where visual handwriting or a sound pattern is itself evidence, an access adaptation needs explicit design review; simply copying words may not preserve the task. [C-06, C-12]

## Design choices and alternatives

| Decision | Conditional choice | Tradeoff and simpler alternative |
|---|---|---|
| Immediate facts versus optional detail | Put information needed for the presently intended action in a recoverable route; leave history, perspectives or interpretive enrichment optional when progression does not require them. | Declaring a clue “optional” while requiring it later is misleading. A single contextual line may serve better than a multi-page archive. [C-06] |
| In-world source versus external summary | Use an attributed source when perspective, reliability or provenance matters; use a summary when the collection’s authority is intentionally clear. | A summary can accidentally convert an allegation into fact. A brief source-preserving paraphrase can be safer than a synthesized verdict. [C-07] |
| Automatically recorded versus player-selected notes | Automatic recording supports revisiting exposed evidence; player selection can express what seems important or what hypothesis is being pursued. | Automatic entries can imply comprehension; manual note taking can become an access barrier. Offer a source list without automatically asserting a conclusion. [C-07, C-11] |
| Search, thematic grouping or temporal order | Choose retrieval routes matching the questions players actually ask: who, where, what changed, what evidence supports this? | An exhaustive taxonomy may be harder to use than recent/relevant entries. Multiple useful retrieval paths need not expose undiscovered names. [C-11] |
| Unreliable account versus omniscient record | Attribute unreliable accounts and preserve the distinction between a speaker’s confidence and the library’s approved facts. | An omniscient codex may spoil ambiguity; unlimited unreliability can make evidence-based play impossible. Omit an authoritative judgment when the design has not earned one. [C-07, C-10] |
| Update, append correction or retain historical version | Correct an accidental presentation error; preserve provenance when a narrator learns something new; escalate a changed fictional truth for an explicit project decision. | Silent replacement can erase why an earlier choice made sense. A visible amendment or a revision note may retain coherence with less content than rewriting the whole archive. [C-08, C-09, C-10] |
| Completion count versus open collection | Count items when collecting a specified set is part of the experience; omit or soften counts when they would turn uncertainty into a checklist. | A count can disclose how much remains unknown or pressure collection. Do not assume either motivation is universally desirable. [C-11, C-12] |

None of these choices establishes a universal number of lore layers, entries, reminders or required readings. “Optional depth” is a dependency decision, not a mandatory content pyramid. [C-06]

## Application process

1. **Diagnose the information obligation.** For each relevant decision, state what the player must be able to know, what should remain uncertain, and what may be missed without blocking the promised experience. Separate useful context from a tested prerequisite. If understanding is the challenge, specify it as such rather than hiding it in optional flavor. [C-06]
2. **Assign authority and provenance.** Identify the fictional speaker or document, time/context, exact asserted proposition, and any approved fact it depends on. Use actual project-approved records when available; mark a missing authority decision as unresolved. Do not substitute a successful game’s canon or a researcher’s plausible invention. [C-07, C-08]
3. **Choose an encounter and recovery route.** Place information where the intended audience can encounter it, then decide how it can be revisited after interruption or through supported modalities. The route may be a conversation, environment, recording, short note or searchable collection; no modality is inherently more authentic. [C-06, C-11, C-12]
4. **Design the record’s claims.** A source entry may identify what was encountered and when without declaring its truth. A player theory should remain a theory until the game’s stated evidential task accepts it. Distinguish “new source,” “new interpretation” and “correction” in the presentation only where those distinctions matter. [C-07, C-11]
5. **Audit dependencies and contradictions.** Compare propositions for the same entity, event and time, then check attribution, conditions, locale and edition. A contradiction is not resolved by choosing the newest-looking file or the more confident narrator. Escalate authority changes rather than silently rewriting world rules. [C-08, C-10]
6. **Review adaptations in context.** Ask language and access reviewers whether the adapted record preserves the intended claim, uncertainty and decision. Recheck affected lines, summaries and recordings after a change. Preserve the relevant meaning, not merely character counts or back-translated wording. [C-09, C-12]
7. **Evaluate and revise.** Test discovery, retrieval, mistaken certainty and dependency failure separately. Remove an unnecessary codex feature if a simpler contextual reminder solves the problem. Stop automatic synthesis when it cannot distinguish fact, testimony and player interpretation. [C-11, C-13]

## Patterns and genre adaptations

The two W02 pattern slots are used for [Intent and response contract](../patterns/intent-and-response-contract.md), `GDR-CAND-20261010-W02-PAT-01`, and [Multi-route objective contract](../patterns/multi-route-objective-contract.md), `GDR-CAND-20261010-W02-PAT-02`. They apply when testimony is solicited through dialogue or evidence is used to resolve an objective. Neither makes all lore an objective nor all testimony a true statement.

**Additional justified pattern work is queued, not silently omitted:** a source-attributed lore record and a dependency-aware optional-depth design require separate child work, especially player tests of attribution and the boundary between enrichment and necessary knowledge. Their child batch keys and candidate IDs have not been allocated. The packet records decision questions and prerequisites.

Future genre guidance must distinguish contexts where inference is a core challenge, where a coherent atmosphere is sufficient, where collection itself is the goal, and where alternate interpretations are intended to remain unresolved. A genre name alone cannot resolve those conflicts. No genre file, genre ID or claim of complete genre coverage is supplied here.

## Examples and counterexamples

### Illustrative worked example: conflicting accounts of a closed water gate

The following is invented and not approved canon. The player finds an engineer’s log saying the gate was closed during winter maintenance. Later, a merchant says it was closed to punish a district. The game design has not yet decided whether both statements can be true.

A source-preserving record might contain:

| Record element | Illustrative content | What it does not claim |
|---|---|---|
| Encounter | Engineer’s log found in the pump house; a dated passage concerns a winter closure. | That the player read or believes the passage. |
| Attributed assertion | The engineer describes the closure as maintenance. | That maintenance was the only motive or the actual explanation. |
| Other testimony | A merchant attributes the closure to punishment. | That the merchant witnessed the decision. |
| Player inquiry | “Could maintenance and punishment refer to the same closure?” | That combining the accounts proves a conspiracy. |
| Progression relevance | The current repair objective requires finding a usable supply; the historical motive is not yet a stated prerequisite. | That the history will never matter to a later decision. |

This proposed record supports comparison without presenting an authoritative verdict. A short version could simply preserve the two attributed statements; the table is an authoring aid, not a required on-screen interface or database schema. [C-07, C-11; illustrative]

If a locale accidentally changes “during winter” to “every winter,” the recurring claim is not evidence of deliberate ambiguity. Review the localized sentence and its dependent summaries. If the world owner deliberately changes the history to recurring closures, that is a different kind of change: affected quests, testimony and earlier decisions need explicit impact review. Neither change is approved by this example. [C-08, C-09, C-10; illustrative]

### Illustrative optional-depth comparison

For a water-restoration objective, the player may need a current safety instruction, may benefit from knowing why the engineer distrusts the requester, and may optionally investigate the gate’s history. That arrangement has no intrinsic number of levels: one design may need only the instruction; another may make the historical motive essential to choosing whom to help. The latter must provide an appropriate opportunity to acquire and understand the relevant evidence, not retrospectively call failure to find “optional” material a player mistake. [C-06; illustrative]

### Strong counterexamples

**An authoritative codex is intentionally absent.** In an illustrative story built around unresolved testimony, a synthesized “true history” would defeat the premise. Revisit the sources without settling them, or omit the codex. Source attribution is not a demand for an encyclopedic truth display. [C-07, C-11; illustrative]

**Knowledge really is the gate.** In an illustrative decoding challenge, correctly interpreting a seal is the required action. Letting a generic marker reveal the destination may remove the puzzle. Access adaptations should preserve the meaningful reasoning or provide an explicitly chosen bypass; the *Heaven’s Vault* account does not override this design. [C-02, C-06; illustrative]

**No archive is needed.** A brief, self-contained scene may permit repetition on request and no persistent lore collection. Building a searchable codex could add maintenance and distraction without addressing any observed problem. This is a legitimate comparator in the proposed test, not an incomplete implementation. [C-11; illustrative]

## Failure modes and constraints

**Exposure mistaken for belief.** A recap can falsely say “You discovered the engineer lied” when the player merely acquired a log. Prefer a source claim or a previously expressed interpretation, and do not pretend that an internal record knows an unexpressed mental state. [C-01, C-07]

**Optional content becomes covert homework.** A later choice may depend on a minor entry the game encouraged players to skip. Decide whether the later task supplies enough context, allows revisiting the evidence, offers a legitimate uncertain choice, or intentionally tests memory/interpretation. Do not quietly change the meaning of “optional.” [C-06]

**Contradiction erased by confidence or freshness.** A newer content export may not be the approved one; a confident fictional narrator may be wrong. Match authority and revision provenance, and separate an approved retcon from a translation error or character disagreement. The dispatch’s rule about candidate identity illustrates this research-workflow boundary, not the content of any game’s canon. [C-08, C-10]

**Localization and access work alter inference.** A translation may remove a pronoun ambiguity or make a deliberately incomplete phrase certain. A narrated description may omit a material feature that is evidence. The proposed review asks whether the meaningful task survives the adaptation, not whether every player receives an identical surface. IGDA guidance supports in-context review; this exact lore method remains untested. [C-09, C-12; GDR-SRC-20261010-W02-009]

**Authority carries ethical implications.** A codex may inadvertently present one institution’s view as objective truth or reward collecting decontextualized cultural objects without scrutiny. Review whose claims the interface legitimizes and whether relevant communities or specialist perspectives are missing. This is an author-proposed ethical review lens, not a universal verdict about a genre or real culture. No claim of cultural approval is made. [C-12]

**Production growth.** Each new source, summary and alternate version creates relationships to maintain. A narrow correction should trigger an impact review of actual dependencies, not an automatic rewrite of everything. Comprehensive coverage, localization labor and narrative clarity are tradeoffs to assess locally; no standard codex size is justified by the inspected sources. [C-08, C-09, C-11]

## Playtest and validation

**All proposed; not performed.** No lore UI, test build, player study or canon change was executed.

| Question | Comparison, controls and procedure | Measures and rejection/adaptation criteria |
|---|---|---|
| Can players obtain needed context without compulsory deep reading? | Compare contextual recap only, attributed revisitable records and the same material with optional expansion. Keep action-critical information equivalent. | Record blocked progression due to information absence separately from chosen uncertainty or interpretive difficulty. Reject “optional” packaging when required facts are predictably unavailable to the intended audience. [C-06, C-13] |
| Does attribution prevent unjustified certainty? | Compare an attributed testimony record with an omniscient-sounding summary and a source-only view. Use unfamiliar fictional material. | Ask what is directly evidenced, who claims what and what remains unresolved. Reject attribution designs that still turn exposure into belief or merely train users to distrust every source indiscriminately. [C-07, C-13] |
| Is the codex useful after an interruption? | Compare a minimal source list, query-oriented grouping and no codex with requestable repetition. Vary interruptions according to intended use. | Measure retrieval success, reconstruction effort, unwanted spoilers and actual use; do not treat time spent reading as inherently good. Prefer the simpler alternative when added structure does not address the targeted problem. [C-11, C-13] |
| Does adaptation preserve the intended evidence? | Review equivalent mysteries/records across intended locales and supported text/audio presentation, with competent language and access expertise. | Check claims, uncertainty, required clues and task difficulty separately. Reject unintended certainty or omitted evidence; explicitly review chosen bypasses rather than disguising them as equivalent tasks. [C-09, C-12, C-13] |
| Can the proposed continuity review find different defect types? | In a future authorized authoring exercise, seed an attributed disagreement, an accidental date mismatch, a changed edition and an untranslated correction into a small illustrative set. | Record diagnosis and false positives, particularly “fixing” intended disagreement. Reject the workflow when authority is guessed or a newer filename is treated as approval. This exercise is proposed and was not executed. [C-08, C-10, C-13] |

Recruitment should reflect reading habits, lore interest, memory-related access needs, language knowledge and familiarity with the setting. Relevant confounds include prior genre knowledge, writing quality, clue salience, collection rewards and leading questions. Establish coding procedures and practically important differences before collecting data; no universal sample size or timing threshold is claimed. Independently test unfamiliar cases rather than counting reproduction of the worked example as general comprehension. [C-13]

## Claim ledger

Claim identifiers are local to this artifact. Confidence describes the stated narrow claim, not proof that the proposed technique improves a game. `inference` and `hypothesis` recommendations are author proposals, not approved studio decisions.

### C-01

**Claim:** Distinguish approved fictional facts, attributed claims, encountered records and player interpretations; exposure alone does not establish belief.

**Class:** `inference`. **Support/contradiction:** A conceptual boundary, not a model that measures player mental states.

**Sources and precise locators:** GDR-SRC-20261010-W02-004 — Creator discussion of seen versus remembered/understood material; original four-way authoring distinction.

**Applicability:** Genre-neutral; no game canon is supplied or approved. **Confidence:** moderate for avoiding category errors, low for measured design benefit. **Unresolved:** Which distinctions need to be presented to the player rather than kept in authoring notes?

### C-02

**Claim:** A creator-reported design can allow discovery-based progression without requiring correct interpretation, but that does not invalidate knowledge-gated designs.

**Class:** `practitioner-heuristic`. **Support/contradiction:** Specific counterexample; generalization expressly limited.

**Sources and precise locators:** GDR-SRC-20261010-W02-015 — Main explanation of site access, artifacts and translation.

**Applicability:** Heaven’s Vault creator account, exact build unknown. **Confidence:** moderate for the reported distinction; no effect estimate. **Unresolved:** When is interpretation itself the intended progress condition?

### C-03

**Claim:** Mask of the Rose supplies a creator account of explicit theory construction rather than assuming exposure equals understanding.

**Class:** `practitioner-heuristic`. **Support/contradiction:** Creator account, not independently played or empirically evaluated here.

**Sources and precise locators:** GDR-SRC-20261010-W02-004 — Seen-content/understanding distinction and theory-construction passages.

**Applicability:** The game revision discussed in November 2023. **Confidence:** moderate for the report, low for transfer benefits. **Unresolved:** Does explicit hypothesis expression help or over-structure another game?

### C-04

**Claim:** Versioned patch notes report consistency, display and localization defects relevant to lore delivery; these are not automatically authored ambiguity.

**Class:** `observed-example`. **Support/contradiction:** Observation of a first-party document; underlying defects/fixes not reproduced.

**Sources and precise locators:** GDR-SRC-20261010-W02-016 — 1.1.15 Art and Visuals, UI, Text and Localization sections.

**Applicability:** PC/Xbox/PlayStation 1.1.15 only; not Switch Patch 4 or current-build verification. **Confidence:** high for the published record, no causal inference about player interpretation. **Unresolved:** Which apparent inconsistencies in the target game are actually content versus presentation defects?

### C-05

**Claim:** Official documentation supplies in-world text and narration presentation examples without establishing universal accessibility settings.

**Class:** `observed-example`. **Support/contradiction:** Directly inspected feature-description text; not a live-game audit.

**Sources and precise locators:** GDR-SRC-20261010-W02-017 — Translation Prompts; Text-to-Speech and Audio Cues.

**Applicability:** PS4-era documentation with launch-patch annotations. **Confidence:** high for the documented options; transfer effectiveness unknown. **Unresolved:** Does a chosen adaptation preserve the actual information task?

### C-06

**Claim:** Define exactly what may be skipped and what knowledge a later decision requires; optional depth does not imply a fixed layer count or universal absence of gates.

**Class:** `inference`. **Support/contradiction:** Conditional evidence-to-application bridge, not demonstrated comprehension improvement.

**Sources and precise locators:** GDR-SRC-20261010-W02-015, GDR-SRC-20261010-W02-017 — Discovery/translation distinction and access examples; dependency rule proposed here.

**Applicability:** Knowledge-centered tasks may intentionally require interpretation. **Confidence:** moderate for the dependency distinction; low for optimal delivery choice. **Unresolved:** Are essential facts obtainable without accidental spoilers or hidden homework?

### C-07

**Claim:** Preserving attribution and separating source discovery from a confirmed conclusion may reduce false certainty in revisitable lore.

**Class:** `hypothesis`. **Support/contradiction:** No controlled attribution/codex trial inspected.

**Sources and precise locators:** GDR-SRC-20261010-W02-004, GDR-SRC-20261010-W02-015 — Theory/understanding account and discovery/interpretation distinction; record recipe is original.

**Applicability:** Not a demand for an omniscient codex or a fixed representation. **Confidence:** low for benefit: the proposed record design is untested. **Unresolved:** Does it support useful uncertainty rather than confuse or promote blanket distrust?

### C-08

**Claim:** A continuity proposal should require an actual project authority decision before changing fictional truth and retain revision impact/provenance.

**Class:** `inference`. **Support/contradiction:** Workflow proposal, not an approved canon decision or formal standard.

**Sources and precise locators:** GDR-SRC-20261010-W02-009, GDR-SRC-20261010-W02-016 — LQA source-change concerns and versioned defect records; authority boundary also follows supplied W02 dispatch §§Authorization and Parent Reconciliation.

**Applicability:** Applies only when the project has an identified authorized canon process. **Confidence:** moderate for traceability reasoning; no measured defect-reduction result. **Unresolved:** Who owns the actual decision, and which downstream records change?

### C-09

**Claim:** Localized text, recordings and derived summaries need contextual rechecking after relevant content changes.

**Class:** `inference`. **Support/contradiction:** Professional practice supports the dependency; exact lore workflow is untested.

**Sources and precise locators:** GDR-SRC-20261010-W02-009, GDR-SRC-20261010-W02-010 — LQA source changes; Voice-Over Recording, printed pp. 19–20.

**Applicability:** Review actual affected representations; no universal rerecording requirement. **Confidence:** moderate for production dependency reasoning. **Unresolved:** Does the adaptation preserve uncertainty, attribution and task meaning?

### C-10

**Claim:** Triage disagreements by proposition, source, time, conditions, locale and edition before calling them deliberate ambiguity or canon errors.

**Class:** `inference`. **Support/contradiction:** Alternative explanations, not proof of intent for any particular conflict.

**Sources and precise locators:** GDR-SRC-20261010-W02-004, GDR-SRC-20261010-W02-016 — Theory-based interpretation and versioned consistency/localization fixes; triage categories authored here.

**Applicability:** Unresolved conflicts remain open; approval cannot be inferred from recency. **Confidence:** moderate for diagnostic reasoning, low for measured review accuracy. **Unresolved:** Can reviewers distinguish intentional disagreement without silently choosing the truth?

### C-11

**Claim:** A codex should earn its complexity by improving the intended retrieval or interpretation task over simpler reminders or source lists.

**Class:** `hypothesis`. **Support/contradiction:** Original comparative proposal, not established UI guidance.

**Sources and precise locators:** GDR-SRC-20261010-W02-004, GDR-SRC-20261010-W02-017 — Theory and accessible information examples; no inspected comparison of codex structures.

**Applicability:** No codex may be appropriate for brief or deliberately unrecorded experiences. **Confidence:** low for specific interface benefits. **Unresolved:** What questions do players actually need to answer after an interruption?

### C-12

**Claim:** Review lore authority, cultural framing and access adaptations for what they permit players to infer, not merely surface similarity.

**Class:** `inference`. **Support/contradiction:** No cultural approval, universal ethical judgment or equivalent-task result is asserted.

**Sources and precise locators:** GDR-SRC-20261010-W02-009, GDR-SRC-20261010-W02-017 — In-context linguistic/cultural review and information-presentation features; ethical review lens proposed here.

**Applicability:** Requires relevant expertise and audience input; it cannot be satisfied by this research alone. **Confidence:** moderate for identifying review questions, low for outcome claims. **Unresolved:** Whose viewpoint is treated as authoritative and which access routes lose evidence?

### C-13

**Claim:** The discovery, attribution, retrieval, adaptation and continuity comparisons are proposed falsification routes, not performed tests or accepted guidance.

**Class:** `hypothesis`. **Support/contradiction:** No participants, prototypes or actual injected-defect exercise.

**Sources and precise locators:** Original author proposal; no direct empirical source — Original Playtest and validation section.

**Applicability:** Local priorities, participant needs and decision criteria remain to be agreed. **Confidence:** low for proposed benefits; no fabricated precision. **Unresolved:** Do results generalize to unfamiliar records and independently chosen examples?


## References

Access date for every record below: **2026-10-10**. “Inspected” means the stated text/pages, not an entire linked corpus, game build, video or cited book. Source identities are temporary; cross-batch canonical URL/DOI/edition deduplication remains pending.

### GDR-SRC-20261010-W02-004

**Emily Short.** [Dialogue Expressiveness in Mask of the Rose](https://emshort.blog/2023/11/22/dialogue-expressiveness-in-mask-of-the-rose/). Emily Short’s Interactive Storytelling. Publication/update: 2023-11-22.

**Edition/build:** Creator account of the then-latest release; exact game build not supplied. **Access:** `relevant-excerpt`. **Source type:** First-person creator account.

**Precise locators used:** Article body: wardrobe/personality selection; seen-content versus remembered/understood content; theory construction and revision discussion. Images not used as independent observations.

**Claims supported or constrained in this entry:** C-01, C-03, C-07, C-10, C-11. **Limits:** No reported controlled player-effect estimate and no direct gameplay inspection here. **Independence:** Same author as sources 003 and 014; not independent corroboration across those articles.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-009

**Jennifer O’Donnell, with the named professional contributors acknowledged in the article.** [How to Get the Most from LQA – What It Is and Best Practices](https://igda.org/news-archive/how-to-get-the-most-from-lqa-what-it-is-and-best-practices/). IGDA. Publication/update: 2023-05-31.

**Edition/build:** Dated professional guidance article. **Access:** `relevant-excerpt`. **Source type:** Practitioner guidance.

**Precise locators used:** What is LQA?; What happens during LQA?; discussion of context, characterization, terminology, UI and source changes during testing.

**Claims supported or constrained in this entry:** C-08, C-09, C-12. **Limits:** Professional recommendations, not a controlled comparison of localization workflows. **Independence:** Shares the IGDA localization practice network with source 010; not an independent player study.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-010

**IGDA Localization SIG; second draft edited by Jon Fung, following Richard Honeywood’s initial draft.** [Best Practices for Game Localization](https://igda-website.s3.us-east-2.amazonaws.com/wp-content/uploads/2021/04/09142137/Best-Practices-for-Game-Localization-v22.pdf). IGDA. Publication/update: second draft 2012-02-01; republished edited copy 2021-04-09.

**Edition/build:** Second-draft guide; filename v22; 2021 hosting is not a new empirical study. **Access:** `relevant-excerpt`. **Source type:** Professional practice guide.

**Precise locators used:** Voice-Over Recording, printed pp. 19–20 / PDF pp. 22–23, both inspected as screenshots; contextual direction and recorded-script/subtitle consistency.

**Claims supported or constrained in this entry:** C-09. **Limits:** Historical guidance; regional stereotypes, staffing ratios and cost figures not adopted. **Independence:** Same professional network as source 009; edition and repost date kept separate.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-015

**inkle.** [How come translation unlocks sites in Heaven’s Vault?](https://medium.com/@inklestudios/why-does-translation-unlock-sites-in-heavens-vault-e05c4ccadf62). inkle on Medium. Publication/update: 2025-11-18.

**Edition/build:** Creator explanation of Heaven’s Vault; exact executable build not supplied. **Access:** `relevant-excerpt`. **Source type:** First-party creator explanation.

**Precise locators used:** Main article body explaining artifact provenance, discovery, translation and interpretation; promotional recommendations excluded.

**Claims supported or constrained in this entry:** C-02, C-06, C-07. **Limits:** Supports a particular design account, not measured comprehension or a universal lore rule. **Independence:** Independent studio account; no player study or direct gameplay observation was performed here.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-016

**Mobius Digital.** [Patch notes for all platforms (Patch 15 on PC, Xbox and PlayStation, and Patch 4 on Nintendo Switch)](https://www.mobiusdigitalgames.com/news/patch-notes-for-all-platforms-patch-15-on-pc-xbox-and-playstation-and-patch-4-on-nintendo-switch). Mobius Digital. Publication/update: 2024-06-10.

**Edition/build:** Only Outer Wilds 1.1.15 PC/Xbox/PlayStation entries used; Switch Patch 4 kept separate. **Access:** `relevant-excerpt`. **Source type:** First-party patch record.

**Precise locators used:** 1.1.15 Art and Visuals; UI; Text and Localization: writing consistency, ship-log display/text and language-related fixes.

**Claims supported or constrained in this entry:** C-04, C-08, C-10. **Limits:** Reported defects/fixes, not personally reproduced gameplay or player-effect measurements. **Independence:** Independent production account from sources 013, 015 and 017.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.

### GDR-SRC-20261010-W02-017

**Matthew Dunnerstick / Naughty Dog.** [The Last of Us Part II: Accessibility Features Detailed](https://www.naughtydog.com/blog/the_last_of_us_part_ii_accessibility_features_detailed). Naughty Dog. Publication/update: 2020-06-09; inspected page also contains launch-patch annotations.

**Edition/build:** PS4 launch-era feature description with 1.01/1.02 annotations; not a PS5 Remastered audit. **Access:** `relevant-excerpt`. **Source type:** Official feature documentation.

**Precise locators used:** Navigation and Traversal; Text-to-Speech and Audio Cues; Translation Prompts; Subtitles. Feature-description text inspected, embedded videos not inspected.

**Claims supported or constrained in this entry:** C-05, C-06, C-11, C-12. **Limits:** Documented options are not evidence that the same configuration works for every player. **Independence:** Separate studio from the other creator accounts; no independent comparative user data supplied.

**Rights:** Copyrighted source; linked and paraphrased only. No source file or image is redistributed.


## Open questions and change history

**Coverage checkpoint:** discoverability and optional depth have creator-reported counterexamples and analytic treatment; codex design has examples and proposals but no inspected controlled codex study; approved canon has only an authority-preserving workflow proposal, with no actual canon supplied; contradiction management has versioned production records and a proposed diagnostic. Every subtopic remains pending W02 independent review.

**Evidence gaps:** no directly inspected comparative evidence establishes an ideal codex structure, amount of lore, degree of ambiguity, long-term recall effect or continuity-defect reduction. Non-English, non-reading and culturally diverse interpretive experiences are underrepresented. Theories of reader response and real-world archival practice were not silently imported as inspected evidence.

**Dependencies:** parent-reviewed W01 world/narrative/character bytes; environmental storytelling and narrative systems interfaces guidance; Presentation interface/localization/accessibility guidance; the target game’s actual approved canon and change authority. All are missing for application; no fabricated links or IDs substitute for them.

**Conflicts:** local packet labels `optional-versus-required`, `testimony-versus-truth`, `ambiguity-versus-defect` and `access-versus-solution`; see the [review packet](../reviews/full-run-20261010-w02-review-packet.md#contradictions-and-contested-claims).

**History:** 2026-10-10 — version 0.1.0, `initial-draft-1`, first W02 submission, predecessor/supersession null. Author self-review completed; independent review, game-canon approval and release absent. Exact byte hash appears in the packet. Next decision: review whether the source-attribution hypothesis and its uncertainty are useful enough to justify registered child research, not automatic canon adoption.

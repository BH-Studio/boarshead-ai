---
id: GDR-CAND-20261010-P05-TOP-03
kind: topic
title: Localization and presentation
version: 0.1.0
candidate_revision: independent-review-correction-1
status: draft
run_id: GDR-FULL-20261010
batch_key: P05
attempt_id: P05-authoring-01
owner_project: BH-GDR-Presentation-and-Interaction
updated: '2026-10-11'
evidence_checked: '2026-10-10'
coverage_status: coverage-open
aliases:
- locale presentation contract
- localized text voice and layout
tags:
- presentation
- research-candidate
- coverage-open
related_topics:
- GDR-CAND-20261010-P05-TOP-01
- GDR-CAND-20261010-P05-TOP-02
related_patterns:
- GDR-CAND-20261010-P05-PAT-02
related_genres: []
dependency_ids:
- GDR-CAND-20261010-P01-TOP-01
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
- GDR-CAND-20261010-P02-TOP-01
- GDR-CAND-20261010-P02-TOP-03
- GDR-CAND-20261010-W02-TOP-01
- GDR-CAND-20261010-F01-PAT-01
source_ids:
- GDR-SRC-20261010-P05-007
- GDR-SRC-20261010-P05-008
- GDR-SRC-20261010-P05-009
- GDR-SRC-20261010-P05-010
- GDR-SRC-20261010-W02-006
- GDR-SRC-20261010-W02-009
- GDR-SRC-20261010-W02-010
- SRC-0005
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: ee5e10b32573e21167dfe34df96ab96eb1625ce47d1139ac9c9fa0fd6c68ba30
supersedes: []
change_summary: Independent correction separates resource-feasibility understanding
  from a player preference to decline; original evidence and approvals unchanged.
byte_hash_record: ../reviews/full-run-20261010-p05-review-packet.md#candidate-byte-receipt
---

# Localization and presentation

**Draft research candidate — coverage open.** This entry treats presentation localization as a decision about meaning, usable rendered information and performance, not merely replacing words in a table. No target-language translation, target-build inspection or player evaluation was performed. [C-09, C-13, C-14]

## Decision and scope

**Decision:** How should a game preserve its intended task relationships, available choices and authorized ambiguity across languages, scripts, display contexts and recorded performances, while allowing appropriate expressive differences?

Assigned coverage is language expansion, reading direction, cultural interpretation and voice constraints. It also includes fonts/layout, subtitles/captions, speaker identification, competing text, language switching and revision consistency. [Audio design](audio-design.md) owns mix/spatial decisions; [Music design](music-design.md) owns musical organization. W02 dialogue owns speech acts, subtext and narrative commitments. P05 does not change those commitments, approve a localized canon, select a cast or authorize production. [C-09, C-14]

### Working distinctions

*Internationalization* here means making content and presentation adaptable; *localization* means preparing a contextual language/region variant; *linguistic quality assurance* means checking the prepared material in its actual context. A *message unit* is one coherent player-facing utterance or information object, including variables and context—not necessarily a line of source code or a fixed rectangular box. A *locale variant* may change wording and presentation while preserving an explicitly identified task relationship. These are working conventions; source-specific terminology is retained in the ledger. [C-03, C-05, C-06, C-13]

Record the supported language/script/region set, source language, reading/voice options, player literacy and access needs, output device/viewing distance, input mappings, renderer/build, font and content revisions, pause/replay capabilities and text/voice fallback behavior. None is inferred from national identity or the author’s language. The examples use English descriptions of hypothetical variants, not invented translations presented as fluent or approved. [C-09–C-13]

## Core explanation and mechanisms

### Preserve the decision, not a byte count

A line can fit and still change the task. A shorter instruction can omit a negation, change who owes whom, or turn a possibility into a commitment. Conversely, different wording can preserve the intended relation more faithfully than literal substitution. The proposed review object is therefore **state → intended message/speech act → localized text/performance → rendered presentation → player interpretation/action**. Each link needs its own check. [C-09, C-13]

ICU’s whole-message guidance supplies a practical reason to avoid assembling player-facing sentences from rigidly ordered translated fragments. Variables and grammatical alternatives need contextual freedom. That facility does not establish that the resulting wording is correct; it creates room for a language reviewer to make it correct. A shared message identity is also not a claim that every language uses the same number of visible or spoken segments. [C-03, C-05, C-09]

**Untranslated task assumptions** need explicit review. A puzzle can rely on an alphabetic order, a pun, a keyboard position, a vocal distinction or a source-language abbreviation even after every visible string is translated. Where that dependence is essential, local adaptation may be a design change rather than a text fix. The narrative/system owner must approve the altered relation; P05 should expose it, not quietly replace the game’s challenge. [C-09, C-10, C-13, C-14]

### Rendered geometry is the relevant constraint

W3C’s informative internationalization article distinguishes length, compound words, character width and height. The bridge to game presentation is to inspect the actual shaped, wrapped output at supported settings rather than declare a fixed expansion allowance sufficient. Avoid turning a historical example or an English caption limit into a rule for every script. [C-01, C-08]

Prefer room for meaningful reflow, contextually reviewed shorter variants, accessible scrolling/replay, or a different information arrangement according to the task. Each changes a different property: reflow changes layout; a short variant changes language; a log changes time/place of access. Automatic shrinking or truncating an action label can preserve a box while defeating the player’s decision. These alternatives require actual readability, focus and comprehension checks; none is universally best. [C-01, C-09, C-10]

Pseudolocalization is useful as an early diagnostic, but passing a synthetic expansion does not establish target-language grammar, font coverage or contextual meaning. Its broad documentation statement about mirroring RTL interfaces is not adopted as a universal rule. Text direction, reading/navigation order, icons representing physical directions, maps and player controls require explicit separate decisions. [C-02, C-04, C-10]

### Direction, shaping and navigation are separate responsibilities

UAX #9 revision 52, for Unicode 18.0.0, gives normative bidirectional-ordering clauses. A conforming process must produce the specified display order subject to its permitted higher-level protocols. The annex expressly places line breaking outside the algorithm and requires shaped widths where shaping is involved. This is a formal-standard claim about its stated conformance scope, not proof that a native game, UI or renderer is compliant. [C-02]

Do not “support RTL” by blindly reversing a whole string. Determine the intended paragraph direction and handling of mixed-direction variables such as names or identifiers, then verify actual output through the chosen renderer. Separately check glyphs, shaping, line breaks, cursor/selection where available, focus traversal and dynamically displayed input prompts. Unicode text ordering does not decide whether a particular compass arrow, performance gesture or controller layout should be mirrored. These are application inferences to evaluate. [C-02, C-10]

### Captions compete for time, space and interpretation

Retain P02’s reviewed distinction: equivalent decision facts are not guaranteed equivalent attention demands or emotion. Speaker identity should convey what is actually knowable, not reveal an unseen speaker merely because a production record names the actor. Direction may be relevant even when identity is unknown. If an off-screen event and a spoken instruction compete, category configuration alone does not settle what should be displayed, deferred, summarized or replayed. [C-08–C-10]

A caption must remain interpretable alongside localized menus, input prompts and the current task. More explicit text can remove intended ambiguity; less text can remove a required fact. Resolve that conflict against a written information contract, not by assuming hearing-dependent uncertainty takes priority. Simultaneous hearing and reading, sound-off play and assistive speech are distinct evaluation contexts. No universal words-per-minute, characters-per-line or display duration is certified here. [C-08, C-09, C-13]

### Voice binds meaning to time and revision

The historical IGDA guide distinguishes free, time-constrained and lip-constrained recording work and emphasizes agreement between selected takes and scripts/subtitles. W02’s inspected dialogue candidate already treats performance as interpretation. P05 adds the presentation question: what can vary in duration, segmentation and delivery without changing the intended commitment or making the information unusable? [C-07, C-09]

Text-only, selective voice, flexible timing and locale-specific performance are legitimate alternatives. A line intended to be interrupted cannot assume its decisive negation has already been heard in every language. A longer recorded variant may require presentation adaptation rather than faster speech or smaller captions. Check the actual selected take and its caption version together. No casting, recording or rights commitment follows from this draft. [C-07, C-09, C-13, C-14]

### Culture and version are review dimensions, not demographic shortcuts

IGDA LQA includes contextual non-text concerns and revision checks. Its older recording guide also contains broad regional voice preferences and cost multipliers that P05 does not adopt. Treat culturally specific examples as questions for relevant contextual expertise, not authority to apply national stereotypes. Multiple people sharing a language may interpret a symbol, joke, accent or performance differently. [C-06, C-07, C-12]

A source edit, a recast take, a changed task or a renderer update can invalidate a previous presentation check. Line IDs help associate artifacts; they do not certify that those artifacts still mean the same thing. The proposed message-unit pattern records what changed and which variants must be reconsidered. Language switching similarly needs a policy for pending and already-presented information, not just a menu value. [C-05, C-06, C-11]

## Design choices and alternatives

| Decision | Conditional choice | Costs, alternative and exit |
|---|---|---|
| Long text | Reflow when time and spatial attention allow it. | A larger area may obscure play; use a reviewed compact variant or recoverable detail view when appropriate. Never assume ellipsis preserves the action. [C-01, C-09] |
| Grammatical variation | Translate complete message units with contextual variables and locale variants. | Requires context and variant checks. Split by meaning only when the parts remain independently interpretable. [C-03, C-09] |
| Reading direction | Use the chosen text system’s appropriate bidi/shaping behavior and separately review UI navigation. | No renderer selected or tested. Stop certification claims until actual versions and tests are known. [C-02, C-10] |
| Caption competition | Prioritize still-valid task facts, with appropriate recovery and configured categories. | Suppression can lose facts; indiscriminate display can overload reading. Compare fewer simultaneous events. [C-08, C-09] |
| Voice constraints | Identify free/timed/lip-constrained lines before finalizing performance. | Fixed source timing may force unnecessary compromises. Consider flexible staging or selective voice. [C-07, C-09] |
| Language switching | Switch immediately, at a recoverable boundary or after a clear confirmation according to context. | Immediate changes can mismatch active speech; indefinite deferral can strand settings. No universally best option is established. [C-11] |
| Cultural adaptation | Review the specific meaning and audience context. | Symbol removal or literalness may alter theme. Refer meaningful changes to the relevant design/narrative owner. [C-09, C-12, C-14] |

## Application process

1. **Map the player decision.** State what must be understood, what may remain ambiguous, which actions exist, and what would constitute a changed task or commitment. [C-09]
2. **Inventory presentation dependencies.** Link each message to variables, speaker knowledge, caption categories, voice take, layout, input prompt and content revision. Record unknowns rather than invent target locales or rendering support. [C-05, C-11, C-13]
3. **Choose adaptation freedom.** Separate required semantics from flexible wording, line breaks, duration, performance and visual arrangement. Identify wordplay/input assumptions needing a design decision. [C-01, C-03, C-07, C-09]
4. **Prepare diagnostics.** Plan pseudolocalization, real-script rendering, settings/navigation checks and contextual language review as distinct activities. A pass at one level does not pass the others. [C-02, C-04, C-06, C-10]
5. **Verify actual variant combinations after separate authorization.** Review selected text and voice, changing states, concurrent captions, language switches and subsequent revisions. [C-06–C-11]
6. **Resolve or narrow.** Revise a faulty variant, restrict its supported context or propose an explicitly approved task adaptation. Do not silently certify an untested locale or change canon. [C-09, C-13, C-14]

## Patterns and genre adaptations

[Locale-resilient message unit — GDR-CAND-20261010-P05-PAT-02](../patterns/locale-resilient-message-unit.md) is the extracted conditional authoring/review recipe. It does not duplicate general cue redundancy or W02’s dialogue commitments. The existing P01/P02 overlap stays pending. A separate cross-locale performance-constraint extension is [queued](../reviews/full-run-20261010-p05-review-packet.md#queued-child-work), not smuggled in as a third pattern.

A language puzzle may allow less semantic substitution than a routine status notice; a timed activity may allow less reading time than a paused inspection. These are illustrative task constraints, not genre findings or new genre files. [C-09, C-13, C-14]

## Examples and counterexamples

**Illustrative — available stock versus reserved stock.** A station has seven units, five reserved elsewhere, and a request needing three unreserved units. The player must understand that the request cannot be fulfilled from the two available units. A displayed total alone is insufficient. The candidate message carries total, reserved and available amounts and distinguishes requesting from promising delivery. A compact variant may present the values differently but must preserve the relation. Speaker, captions and any recorded line must agree about whether an obligation has been accepted. [C-09, C-13]

A discrimination probe changes the reservation to two units while keeping the request at three: five are now available, so the correct feasibility prediction changes. Before feedback, ask whether the request can be fulfilled from unreserved stock without changing reservations and how much stock is available. A repeated claim that fulfillment is impossible does not demonstrate transfer; choosing to decline an affordable request may reflect another goal and is not by itself evidence of misunderstanding. Correct predictions also remain compatible with guessing or other cues, so record reasoning or an equivalent accessible response, assistance and repeated varied cases. This preserves F01’s separation of understanding from preferred action. The numbers are synthetic task values, not empirical parameters. [C-13]

**Strong counterexample.** In an authored word puzzle, spelling and order are the material of play. Replacing its content with a semantically equivalent short sentence may destroy the puzzle. The correct process is a language-sensitive design review with approved changes or an honest support limitation, not silently claiming literal or functional equivalence. [C-09, C-14]

**Version countercase.** A translation still says “request” after a source edit changes the action to “commit,” while an old voice take plays. Correct font rendering and stable line IDs do not make that combination correct. Mark affected variants stale and reconcile them in context. This is an illustrative failure, not an incident observed in a shipped build. [C-05, C-06, C-11, C-13]

## Failure modes and constraints

| Warning sign | What to distinguish | Proposed correction |
|---|---|---|
| Clipped text or missing marks | Font coverage, shaping, line height, reflow and incorrect string selection. | Diagnose the failing layer; do not shrink everything by default. [C-01, C-02, C-10] |
| Readable but incorrect action | Negation, relation, timing or speech act changed. | Review task semantics with language and design owners. [C-09] |
| Unclear speaker or early identity reveal | Caption metadata differs from information available to the player. | Preserve the authorized knowledge boundary, using non-color-only identification where applicable. [C-08, C-09] |
| Settings work only in the current language | Focus, input prompts or confirmation no longer usable after switching. | Provide a recoverable switching path and test return to a known setting. [C-10, C-11] |
| Correct text and mismatched voice | Wrong locale asset or stale script/take pairing. | Reconcile the selected variant and all affected presentations; recheck after corrections. [C-05–C-07, C-11] |
| Cultural feedback dismissed as mistranslation | Interpretation, performance or representation conflict rather than grammar alone. | Investigate the specific context with appropriate expertise; do not substitute stereotypes. [C-12] |

Production implications include contextual briefs, grammatical variants, font coverage/rights, selected takes and pickups, dynamic text, caption categories, locale/build matrices and regression after changes. These are conceptual cost categories, not budgets or proof that exhaustive combination testing is feasible. Prioritize risky task cases transparently and report untested combinations. Accessibility and cultural checks require actual participants/reviewers appropriate to the question; this authoring pass is not such consultation. [C-06–C-14]

## Playtest and validation

**PROPOSED — NOT RUN.** No target locale was translated or certified; no renderer, menu, subtitle scene, voice asset, participant or language switch was tested. [C-13, C-14]

**Question and comparisons:** Compare a current presentation with a whole-message, contextually reviewed adaptation and the least complex viable alternative. Use the same task facts and authorized meaning; do not compare polished new content with an intentionally broken translation and infer a universal benefit. Separate layout diagnostics, linguistic review and player comprehension. [C-01, C-03, C-09, C-13]

**Procedure:** First specify the correct task relation and variant mapping. Then plan checks using long and short strings, variable names/numbers, relevant mixed-direction text, grammatical alternatives, enlarged text, constrained displays, changed input prompts, overlapping captions and interrupted/selected voice. Include a source revision and an in-flight language switch. Label the exact build, locale, font, content and asset revisions for every observation. The F01-style probe must change the correct answer when testing transfer. [C-05, C-06, C-10, C-11, C-13]

**Participants/context:** Language experts review contextual correctness; intended users with relevant language proficiency and access needs evaluate comprehension and operation. One bilingual reviewer cannot establish a whole population’s usability. Choose sample, inclusion criteria and analytic precision before recruitment; the literature here does not supply a universal count or reading threshold. [C-06, C-12, C-13]

**Measures and decision rules:** Record exact omitted/changed task facts, speech-act interpretation, correct response and reasons, time/effort, recoverability after interruption, task errors, comfort and preference separately. A missing decisive negation, unusable control, false speaker disclosure or unrecoverable obligation blocks advancement of the affected variant. A purely cosmetic difference need not be a semantic failure. Failure to show added value favors a simpler alternative; an inconclusive formative result is not equivalence. Stop on distress/withdrawal and permit familiar access settings. Any numerical acceptance margin must be set locally before testing, not retrofitted to favorable observations. [C-09–C-13]

## Coverage checkpoint

| Assigned facet | Inspected coverage | Open question / missing dependency |
|---|---|---|
| Language expansion | W3C geometry guidance, ICU message rationale, pseudolocalization purpose. | Real locale strings and target layouts absent; no universal expansion ratio. |
| Reading direction / scripts | UAX #9 normative scope and separate diagnostic layers. | Actual renderer, font, line-break/focus behavior and conformance tests not supplied. |
| Cultural interpretation | Contextual LQA and critical treatment of historical assumptions. | No commissioned cultural consultation or target-audience study. |
| Voice constraints | Historical recording guidance, Yarn associations and W02 reviewed boundaries. | Actual takes/timing/rights/locales absent; P04 performance research still author-running per dispatch. |
| Captions / speaker / competition | XAG 104 and P01/P02 reviewed distinctions. | Real reading/context comparisons and combined-needs users not tested. |
| Switching / version variation | Proposed message-unit lifecycle and LQA change checks. | Best switching policy and regression coverage unknown. |
| Display / camera relation | Reviewed P01 and P02 only. | P03 independent review not yet reported complete; no P03 numerical guidance imported. |

All facets remain **coverage-open**. [C-01–C-14]

## Claim ledger

Claim identifiers are local to this entry. Confidence describes the exact scoped proposition, not the strength of the entire technique. Source recommendations, documentation behavior, measured responses and our proposals are not interchangeable.

### C-01

**Claim:** Translation can change the geometry of displayed text; a character-count or fixed percentage alone is not a sufficient layout specification.

**Class:** `inference`. **Support and locator:** GDR-SRC-20261010-P05-007, width/height/compound-noun sections; GDR-SRC-20261010-P05-010, diagnostic problem list.

**Applicability / opposition:** Bridge: actual glyph shaping, wrapping and allowed space determine the rendered result. Source illustrations do not establish universal expansion rates. **Confidence:** Moderate for design reasoning; no local layout measured. **Unresolved:** Which actual locale/content/settings combinations fail the task?

### C-02

**Claim:** UAX #9 specifies bidirectional display ordering under its conformance clauses; it does not solve translation or whole-interface layout.

**Class:** `formal-standard`. **Support and locator:** GDR-SRC-20261010-P05-008, Unicode18.0.0 rev52 §4 UAX9-C1/C2; §3.5.1; §1/§2.4.

**Applicability / opposition:** Normative for claimed Unicode conformance under the stated higher-level-protocol conditions. No native-game legal/certification conclusion or test result. **Confidence:** High for scoped normative wording. **Unresolved:** Which Unicode/renderer version and protocol does the target actually support?

### C-03

**Claim:** ICU guidance favors complete translatable messages with movable variables and locale-appropriate grammatical selection rather than rigid concatenated fragments.

**Class:** `practitioner-heuristic`. **Support and locator:** GDR-SRC-20261010-P05-009, Overview and Complex Argument Types.

**Applicability / opposition:** A documented internationalization practice, not proof of comprehension or a mandated library/API. **Confidence:** High for attribution; local phrasing still requires review. **Unresolved:** Does the message provide enough context and grammatical freedom for the intended locales?

### C-04

**Claim:** Unity describes pseudolocalization as an early diagnostic for space, uncovered strings and text-system problems.

**Class:** `observed-example`. **Support and locator:** GDR-SRC-20261010-P05-010, opening/problem list and Example.

**Applicability / opposition:** Not actual translation, script certification or representative-user evaluation; blanket mirroring wording not adopted. **Confidence:** High for documented tool purpose, not its execution. **Unresolved:** Which remaining failures appear only with real language, voice and task context?

### C-05

**Claim:** Yarn Spinner associates localized text and assets with line identities.

**Class:** `observed-example`. **Support and locator:** GDR-SRC-20261010-W02-006, Localisation Terminology and Workflow.

**Applicability / opposition:** Architecture example only; it does not translate content or guarantee synchronized semantic revisions. **Confidence:** High for documented association; no engine code run. **Unresolved:** How will a semantic change invalidate affected text, caption and voice variants?

### C-06

**Claim:** IGDA LQA guidance distinguishes in-context review from translation/edit/proof and calls for changed source strings to be rechecked.

**Class:** `practitioner-heuristic`. **Support and locator:** GDR-SRC-20261010-W02-009, The LQA Process/Workflow.

**Applicability / opposition:** Practice rationale, not quantified defect prevention or a sufficient release gate. **Confidence:** High for attribution, unknown comparative effectiveness. **Unresolved:** Which event/locale/settings branches were actually seen after the change?

### C-07

**Claim:** The historical IGDA recording guide distinguishes timing constraints and asks teams to reconcile selected takes with scripts/subtitles.

**Class:** `practitioner-heuristic`. **Support and locator:** GDR-SRC-20261010-W02-010, printed pp.19–20, Voice-Over Recording and Script Preparation.

**Applicability / opposition:** Its regional voice stereotypes and cost multipliers are not adopted. No current budget or rights approval follows. **Confidence:** Moderate for usable scoped practice; historical context matters. **Unresolved:** Which meaning, timing or performance mismatch remains in the selected locale take?

### C-08

**Claim:** XAG 104’s caption/speaker guidance is an access input, not a cross-script universal reading budget.

**Class:** `practitioner-heuristic`. **Support and locator:** SRC-0005, Implementation guidelines; reviewed P01 numeric-scope correction and P02 semantic boundary.

**Applicability / opposition:** No blanket reuse of English examples, character counts or nominal scaling as proof of legibility. **Confidence:** High for attribution and scope distinction, local usability unknown. **Unresolved:** Can intended users find the speaker and relevant event while carrying out the task?

### C-09

**Claim:** Locale validation should preserve the intended task relation, commitment and authorized ambiguity, not demand identical wording or emotion.

**Class:** `inference`. **Support and locator:** C-01–C-08; inspected W02 dialogue C-13 and P02 corrected multimodal/fact-alternative dependency.

**Applicability / opposition:** When wordplay or interpretation is the task, local redesign needs narrative/design approval; localization is not silent canon authority. **Confidence:** Moderate for identifying the correct decision object; equality across players not established. **Unresolved:** Which task, uncertainty or speech act changes under the localized presentation?

### C-10

**Claim:** Test direction, glyph coverage, line breaking, interface navigation and input prompts as separate but interacting dimensions.

**Class:** `inference`. **Support and locator:** C-01/C-02/C-04/C-08; reviewed P01/P02 topics.

**Applicability / opposition:** A valid Unicode ordering or mirrored panel does not establish usable focus order, readable captions or correct controller action. **Confidence:** Moderate for diagnostic separation; target matrix unknown. **Unresolved:** Which specific layer explains each observed failure?

### C-11

**Claim:** Language switching and source updates need an explicit policy for in-flight messages, settings recovery and stale voice/text pairs.

**Class:** `hypothesis`. **Support and locator:** C-05/C-06/C-07 and proposed P05-PAT-02 extend documented associations/change checks.

**Applicability / opposition:** No best mid-line switching strategy established; immediate, deferred and restart behavior have different costs. **Confidence:** Low for local effectiveness. **Unresolved:** Can switching complete without lost obligations, duplicate actions or mismatched content?

### C-12

**Claim:** Cultural interpretation requires contextual review rather than national stereotypes or a presumption that literal translation is neutral.

**Class:** `inference`. **Support and locator:** C-06/C-07; shared music evidence is bounded in P05-TOP-02 C-03, not a national preference map.

**Applicability / opposition:** Actual cultural consultation and target audience validation not performed. No claim that one speaker represents a culture. **Confidence:** Moderate as a review constraint, low for any untested interpretation. **Unresolved:** Who may interpret the specific symbol, vocalization or joke differently, and why?

### C-13

**Claim:** The worked cases and validation criteria are proposed diagnostics, not translations, measured outcomes or released settings.

**Class:** `hypothesis`. **Support and locator:** Original P05 synthesis; F01 corrected transfer pattern requires genuinely discriminating examples.

**Applicability / opposition:** No invented target-language fluency, locale QA, participant recruitment or screenshots of a target build. **Confidence:** Low for prospective diagnostic sensitivity. **Unresolved:** Does the comparison distinguish access/comprehension from familiarity and memorization?

### C-14

**Claim:** P05 owns presentation adaptation but does not approve narrative meaning, casting, publication or implementation.

**Class:** `studio-decision`. **Support and locator:** Doug, current P05 instruction and complete brief, 2026-10-10; domain boundaries in supplied taxonomy.

**Applicability / opposition:** No source or game records modified; all conceptual relationships await Coordination. **Confidence:** High for scope boundary. **Unresolved:** Whether Coordination accepts the topic/pattern boundaries and queues.

## References

All records below were inspected as **relevant-excerpt** on **2026-10-10**. Dates identify the inspected snapshot, not a claim of latest engine support. Repeated records are provenance copies, not independent corroboration. Existing pilot/W02 identities are retained; all P05 identities are run-scoped proposals.

### GDR-SRC-20261010-P05-007

**W3C Internationalization.** [Text size in translation](https://www.w3.org/International/articles/article-text-size.en.html). **Publication/update:** Unknown in inspected text. **Edition:** Informative web internationalization article, live snapshot.

**Locator:** Introduction; English and Chinese are particularly compact; compound nouns; character width; character and line height; abbreviations. **Type:** Official informative guidance. **Supports:** C-01; inferred C-10.

**Limits/independence:** Web-oriented, not normative game UI requirements. Historical expansion examples are not adopted as universal percentages. No script-specific font or layout test performed. **Rights:** Reuse license not verified; attributed paraphrase only.

### GDR-SRC-20261010-P05-008

**Unicode Consortium; editors Manish Goregaokar and Robin Leroy.** [Unicode Standard Annex #9: Unicode Bidirectional Algorithm](https://www.unicode.org/reports/tr9/tr9-52.html). **Publication/update:** 2026-09-01. **Edition:** Unicode 18.0.0, revision 52.

**Locator:** §1; §2.4; §3.4–3.5.1; §4, UAX9-C1 and UAX9-C2; §4.3. **Type:** Formal standard / normative annex. **Supports:** C-02; inferred C-10.

**Limits/independence:** Normative scope is Unicode bidirectional conformance, not game certification. Line breaking itself is outside the algorithm; interface mirroring and semantic translation are not settled by conformance. **Rights:** Unicode copyright/terms apply; short attributed paraphrase, no conformance data copied.

### GDR-SRC-20261010-P05-009

**Unicode ICU project.** [Formatting Messages](https://unicode-org.github.io/icu/userguide/format_parse/messages/). **Publication/update:** Unknown. **Edition:** Live ICU User Guide; inspected passage addresses long-standing MessageFormat, not a verified MF2 status.

**Locator:** Overview; MessageFormat → Complex Argument Types (web text 172–187). **Type:** Official technical/practitioner guidance. **Supports:** C-03; inferred C-09.

**Limits/independence:** Whole-message and grammatical-selection rationale; parser/version choice not prescribed. The page’s successor-status note is not used as a current product claim. **Rights:** Reuse license not verified; attributed paraphrase only.

### GDR-SRC-20261010-P05-010

**Unity Technologies.** [Pseudo-Localization](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/Pseudo-Localization.html). **Publication/update:** Publication/update unknown; documentation build stamp 2026-09-03. **Edition:** Unity Localization 1.5.13 documentation snapshot.

**Locator:** Pseudo-Localization opening/problem list; Example; Pseudo-Locale Assets (HTML text 115–148). **Type:** Official technical documentation. **Supports:** C-04; inferred C-01/C-10.

**Limits/independence:** Synthetic expansion is a diagnostic, not real translation or usability validation. Broad UI-mirroring wording is not adopted as a universal rule; no tool run or image comparison performed. **Rights:** Reuse license not verified; attributed paraphrase only.

### GDR-SRC-20261010-W02-006

**Yarn Spinner documentation team.** [Localisation and Assets](https://docs.yarnspinner.dev/yarn-spinner-for-unity/assets-and-localization). **Publication/update:** Unknown. **Edition:** Live Yarn Spinner for Unity documentation; exact software release unspecified.

**Locator:** Opening; Localisation Terminology; Workflow (web text 5–53). **Type:** Official technical documentation. **Supports:** C-05; proposed C-11.

**Limits/independence:** Line/text/asset associations are documented architecture, not translation quality or a mandatory engine. Product’s resource-value judgments are not adopted. **Rights:** Reuse license not verified; attributed paraphrase only.

### GDR-SRC-20261010-W02-009

**Jennifer O’Donnell, with listed checking contributors; IGDA.** [How to Get the Most from LQA – What It Is and Best Practices](https://igda.org/news-archive/how-to-get-the-most-from-lqa-what-it-is-and-best-practices/). **Publication/update:** 2023-05-31. **Edition:** Published practitioner article.

**Locator:** The LQA Process; The LQA Workflow; Some Things to Be Aware of with LQA (web text 52–97). **Type:** Practitioner guidance. **Supports:** C-06; inferred C-09/C-12.

**Limits/independence:** In-context QA and change reconciliation, not a controlled cost or defect-rate study. Same organization, different document from W02-010; not independent efficacy evidence. **Rights:** Reuse license not verified; attributed paraphrase only.

### GDR-SRC-20261010-W02-010

**IGDA Localization SIG; initial draft Richard Honeywood; second draft Jon Fung.** [Best Practices for Game Localization](https://igda-website.s3.us-east-2.amazonaws.com/wp-content/uploads/2021/04/09142137/Best-Practices-for-Game-Localization-v22.pdf). **Publication/update:** Initial 2011-02-01; second draft 2012-02-01; hosting path 2021 is not publication. **Edition:** Second draft, 36 PDF pages.

**Locator:** Voice-Over Recording; Script Preparation and Translation; Audio File Specifications, printed pp.19–20 / PDF pages22–23. **Type:** Practitioner guidance. **Supports:** C-07; inferred C-09/C-12.

**Limits/independence:** Historical recommendations, not a formal standard. Regional voice stereotypes and recording-cost multipliers rejected as unsupported transfer. Screenshots of cited pages inspected; no assets redistributed. **Rights:** Reuse license not verified; attributed paraphrase only.

### SRC-0005

**Microsoft.** [Xbox Accessibility Guideline 104: Subtitles and captions](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104). **Publication/update:** Updated 2026-03-04; original date unknown. **Edition:** Unnumbered live XAG 104 revision.

**Locator:** Goal; Overview; Implementation guidelines: important speech/non-speech, speaker/direction, category settings (web text 31–117). **Type:** Official vendor guidance. **Supports:** C-08; inferred C-09/C-10.

**Limits/independence:** Not a formal standard or certification claim; no cross-language reading-speed or emotional-equivalence finding. Same issuer as SRC-0007. **Rights:** Reuse license not verified; attributed paraphrase only.

## Open questions and change history

**2026-10-10 — initial-author-draft, version 0.1.0.** No predecessor P05 artifact; no supersession or new canonical assignment. Evidence checked means the source passages and named dependency bytes were inspected, not that their conclusions were approved. The separate author self-review is in the [P05 packet](../reviews/full-run-20261010-p05-review-packet.md#author-self-review). No independent P05 review has occurred.

**Handoff:** complete draft artifact, bounded source coverage and unresolved local outcomes. Gate C independent review and acceptance remain outstanding; P05 host Gate D tests are NOT RUN; Gate E acceptance/release is NOT PASSED. Next decision: Coordination reviews scope, evidence precision, identity/overlap mapping and proposed child work before any separately authorized validation or release.

## Independent review correction 1 — 2026-10-11

The worked resource probe now asks about feasibility independently of the player’s willingness to commit resources, matching the exact F01 dependency. Refusing a feasible request is not by itself a comprehension failure. Correct predictions alone are also not proof of learning. Original author history remains historical. Version 0.1.0, draft status, coverage-open and null reviewer/approval fields remain unchanged. Both byte-identical Library origins are retained without canonical selection; author final-response provenance remains unverified and the private response was not accessed. Independent inspection is complete for this correction; acceptance, host tests and release are still outstanding. No player, host or runtime test ran.

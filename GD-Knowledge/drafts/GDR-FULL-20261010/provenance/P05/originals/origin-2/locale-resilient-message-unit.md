---
id: GDR-CAND-20261010-P05-PAT-02
kind: pattern
title: Locale-resilient message unit
version: 0.1.0
candidate_revision: initial-author-draft
status: draft
run_id: GDR-FULL-20261010
batch_key: P05
attempt_id: P05-authoring-01
owner_project: BH-GDR-Presentation-and-Interaction
updated: '2026-10-10'
evidence_checked: '2026-10-10'
coverage_status: coverage-open
aliases:
- contextual locale message revision
tags:
- presentation
- research-candidate
- coverage-open
related_topics:
- GDR-CAND-20261010-P05-TOP-03
related_patterns: []
related_genres: []
dependency_ids:
- GDR-CAND-20261010-W02-TOP-01
- GDR-CAND-20261010-F01-PAT-01
source_ids:
- GDR-SRC-20261010-P05-007
- GDR-SRC-20261010-P05-009
- GDR-SRC-20261010-W02-006
- GDR-SRC-20261010-W02-009
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: []
change_summary: Initial P05 author draft; no previous batch, pilot, source or canonical
  file replaced.
byte_hash_record: ../reviews/full-run-20261010-p05-review-packet.md#candidate-byte-receipt
---

# Locale-resilient message unit

**Hypothesis-led pattern candidate.** Keep one coherent player-facing meaning associated with its contextual language variants, displayed form, selected assets and revision state. Stable identity supports tracing; it does not make a stale or mistranslated message correct. [C-01–C-05]

## Purpose

Help teams prevent an apparently valid localized string or voice asset from changing a task relationship, obligation or usable presentation. The intended benefit is fewer consequential mismatches, not identical wording, identical emotion or automatic localization quality. The combined workflow remains a proposal to evaluate. [C-04, C-05]

## Context and prerequisites

Use when a message has dynamic variables, multiple locales, associated performance/assets, constrained presentation or recurring source changes. The project needs an owner for meaning, a source/content identity, intended locale contexts, a way to inspect selected variants and appropriate language expertise. No particular localization framework is required. [C-01–C-05]

Before use, state what the player should understand or do; which ambiguity is intentional; whether word order, spelling or voice is itself task material; how text and speech may differ; display/input/access context; and who can approve consequential semantic changes. Do not make a localization reviewer silently responsible for redesigning a puzzle or accepting narrative commitments. [C-05–C-07]

**Do less** when a genuinely context-independent static label needs no variants beyond straightforward review. The record should expose real risk, not create a sprawling metadata system for every decorative word. [C-05, C-06]

## Mechanism and evidence

| Link | Support | What remains unproved |
|---|---|---|
| A complete message gives translators contextual grammatical freedom. | ICU practitioner guidance. [C-01] | Correctness and comprehension of a specific variant. |
| Text and assets can be associated with a line identity. | Yarn documentation example. [C-02] | Semantic agreement after edits. |
| Changed content can be flagged for contextual recheck. | IGDA LQA guidance. [C-03] | Optimal workflow and measured defect reduction. |
| Joining these records reduces consequential drift. | Original synthesis. [C-05] | Comparative efficacy versus a simpler contextual review. |

[Localization and presentation](../topics/localization-and-presentation.md) owns script-direction standards, caption/access boundaries, cultural interpretation and full topic coverage. This pattern does not add a new generic caption/redundant-cue identity. [C-05, C-07]

## Recipe

### 1. Define the meaning and allowed variation

Write a short contract: event/state, necessary relation, player action, speaker/addressee where relevant, known/unknown information, and whether the line requests, offers, promises, confirms or merely describes. Separate required meaning from flexible diction, segmentation, pacing and visual arrangement. [C-05, C-06]

**Exit:** When spelling, sound or word order is the puzzle, send the needed adaptation to the relevant design owner. Do not present a text edit as an approved replacement of that challenge. [C-07]

### 2. Identify a coherent message unit

Give the message a stable local content identity under the eventual project’s own approved system. Include dynamic parameters with their meanings and possible relationships, not just a string of concatenated fragments. A message may have several locale-specific displayed/spoken parts; a common identity does not require equal segmentation. This recipe does not allocate library or production IDs. [C-01, C-02, C-05]

**Adjustable variables:** unit boundaries; context notes; parameter domains; grammatical alternatives; fallback behavior; and whether a shorter variant is genuinely the same task relation. Avoid joining unrelated messages merely because they share a screen.

### 3. Record presentation and performance constraints

Name the allowed display area, reading settings, input/navigation context, speaker knowledge, associated voice/other assets and any timing constraint. Classify each constraint as necessary to the task, approved artistic intention or reversible production assumption. A source-language box or recording duration is not automatically an immutable requirement. [C-02, C-04–C-06]

**Branch:** When a variant does not fit, compare reflow, a reviewed compact variant or a different recoverable presentation. Do not truncate away the decisive relation or shrink until the task becomes unreadable. [C-04]

### 4. Bind actual variants, not presumed equivalents

For each intended locale, associate the reviewed text, selected asset/version and relevant renderer/font/content version. Distinguish missing, fallback, pending review and actually checked. A fallback can be operationally intentional while still outside a claimed fully localized experience. Do not label it approved merely because an asset loaded. [C-02, C-03, C-05]

**Exit:** If the team lacks the evidence or expertise to assess an essential variant, restrict the claim or queue that review. Do not substitute a guessed translation or a silent canonical decision.

### 5. Invalidate the affected parts after a change

Record what changed: task semantics, variable domain, speaker knowledge, wording, selected performance, timing, layout or input mapping. Mark the affected locale/text/asset checks stale; carry the original identity forward unless the project’s identity policy requires a meaningful split. Preserve the predecessor content/version for review. A stable ID is a tracing aid, not a waiver of rechecking. [C-02, C-03, C-05]

**Adjustable variables:** scope of invalidation; who reviews meaning versus rendering; how exceptions are recorded; and which unaffected variants can retain their evidence. Do not silently reset all review history or claim all variants remain valid after a source change.

### 6. Decide switching and interruption behavior

Choose how pending messages behave when locale changes: complete a recoverable unit, restart in the new locale, replace with current information, or defer briefly with an understandable route back. Define what happens to partially heard obligations and active captions. Compare alternatives rather than assuming immediate switching or waiting indefinitely is always correct. These behaviors are proposals, not documented guarantees of a chosen engine. [C-05, C-06]

**Exit:** Block advancement of a policy that duplicates an irreversible action, loses a required fact, strands settings in an unreadable language or plays text and voice with contradictory meaning.

### 7. Verify the relation in context and retain the evidence

After separate authorization, verify the exact selected message/locale/build combination during the actual task, including change and recovery cases. Keep an observation record distinguishing semantic review, rendering checks and user comprehension. A successful screenshot, script proofread or bilingual paraphrase is not a substitute for all three. [C-03–C-06]

## Worked examples

**Illustrative — a supply request.** An inventory has seven units, five reserved, and a request for three available units. The contract says the request cannot be promised from current available stock. The message carries total, reserved, available and requested values, plus whether the action is merely a request or a commitment. The locale may reorder the relation or use an appropriate compact layout. No target-language translation is invented here. [C-05, C-06]

In this illustration, the intended meaning is not “display the number seven somewhere.” If a compact version drops the reservation, the arithmetic inference changes. If the voice says a promise has been accepted while the text says the player is still requesting, identity and file loading can both be technically correct while the message fails. [C-02, C-05, C-06]

A proposed unseen probe keeps the request at three but changes reserved stock to two: five units are available and the correct decision differs. The test asks the participant to explain the relation. Repeating the previous refusal is evidence against the intended understanding; it is not passed transfer simply because the menu was operated. This is an adaptation of the inspected F01 correction, not a new learning experiment. [C-06]

**Illustrative source update:** Change “request three units” to “commit three units” in the source. Keep the local message identity for traceability, flag affected variants, and review selected text/voice/action behavior together. Whether the game should make that semantic change is outside this pattern’s authority. [C-03, C-05, C-07]

## Tradeoffs and alternatives

The contract adds authoring and review work but may reveal where a cheaper presentation change is enough and where redesign is genuinely needed. Simpler alternatives include fewer dynamic messages, reviewed static wording, text-only presentation, flexible timing, or removing an unnecessary source-language dependency. Overly granular records can fragment the context the pattern is supposed to preserve; overly broad units can make small revisions expensive. Neither extreme is prescribed. [C-01, C-04–C-06]

Locale-specific compact variants add maintenance obligations. Reusing an asset or translation saves work only when its actual meaning and presentation context still fit. A common source key cannot establish that condition. [C-02, C-05]

## Failure cases

Watch for missing grammatical alternatives; unexplained parameter meanings; a changed negation or commitment; mixed old/new voice and text; a fallback language reported as fully localized; focus/input prompts inconsistent with the locale; and a switching path that loses the only copy of a required fact. These are proposed warning signs. No shipped-game failures or completed defect counts are asserted. [C-01–C-06]

A failed rendering check does not prove a translation is wrong. A grammatically strong translation does not prove the task remained equivalent. Record which layer failed, route it to the right owner and verify the selected correction in context. [C-03–C-06]

## Counterexamples and do not use conditions

Do not demand semantic substitution where a word’s exact form is the challenge. Do not use one abstract “equivalent message” to erase deliberate culturally reviewed expressive differences. Do not hide a missing locale or unsafe fallback behind a stable identity. Do not create a large variant system for a simple static label when ordinary contextual review supplies the needed evidence. [C-04–C-07]

The strongest disconfirming case is a simpler contextual review that detects the same consequential problems with less work and no loss of traceability needed by the project. In that case, narrow or remove the extra contract fields rather than defend the pattern’s complexity. [C-05, C-06]

## Playtest

**PROPOSED — NOT RUN.** Compare this contract with the project’s credible existing review method using matched message tasks. Separate expert semantic review, renderer/layout diagnostics and intended-user comprehension. Do not insert all failures into the comparator and then claim a general advantage. [C-05, C-06]

Prospective cases include grammatical alternatives, mixed-direction variable content, long/short layouts, a selected voice update, source semantic revision, an in-flight locale switch and a changed-answer transfer probe. Use the exact locale/font/content/asset/build labels in the record. Failure injection is a proposed test method, not work executed here. [C-06]

Relevant language experts and intended users with appropriate access needs should evaluate their different questions after separate authorization. Predefine the task relation, what counts as a consequential error, resource budget and quantitative margins. No universal participant count or reading-speed benchmark is supplied. Reject a variant that changes a required commitment, makes the decisive relation unavailable or cannot recover from switching. Prefer a simpler method absent worthwhile evidence of improvement, without treating a small inconclusive sample as equivalence. [C-04–C-06]

## Claim ledger

Claim identifiers are local to this entry. Confidence describes the exact scoped proposition, not the strength of the entire technique. Source recommendations, documentation behavior, measured responses and our proposals are not interchangeable.

### C-01

**Claim:** ICU recommends complete message units and context-preserving grammatical alternatives.

**Class:** `practitioner-heuristic`. **Support and locator:** GDR-SRC-20261010-P05-009, Overview and Complex Argument Types.

**Applicability / opposition:** No parser/library mandate or proof of good translation. **Confidence:** High for the recommendation, target wording untested. **Unresolved:** Does the authoring context enable appropriate variants without changing the task?

### C-02

**Claim:** Yarn documentation binds localized text and associated assets to line identities.

**Class:** `observed-example`. **Support and locator:** GDR-SRC-20261010-W02-006, Localisation Terminology and Workflow.

**Applicability / opposition:** A useful architecture example, not semantic synchronization or automatic translation. **Confidence:** High for source content, no target build tested. **Unresolved:** Which changes should invalidate each locale asset?

### C-03

**Claim:** IGDA LQA advises rechecking changed source content in the localized in-game context.

**Class:** `practitioner-heuristic`. **Support and locator:** GDR-SRC-20261010-W02-009, The LQA Workflow.

**Applicability / opposition:** No guarantee of zero defects or quantified savings. **Confidence:** High for attribution; effectiveness and resource needs local. **Unresolved:** What evidence shows the actual changed variant was seen?

### C-04

**Claim:** The same semantic message may need a different presentation arrangement rather than truncation or a fixed expansion allowance.

**Class:** `inference`. **Support and locator:** GDR-SRC-20261010-P05-007, character width/height and compound-noun sections; C-01.

**Applicability / opposition:** Bridge: the space required is determined by the actual localized rendering and task, not source text length alone. **Confidence:** Moderate for design reasoning; no actual layout measured. **Unresolved:** Which arrangement preserves the required relation at supported settings?

### C-05

**Claim:** A message contract linking meaning, variables, assets and revision state may reduce accidental semantic and presentation drift.

**Class:** `hypothesis`. **Support and locator:** C-01–C-04 motivate original P05 recipe; topic C-09/C-11.

**Applicability / opposition:** No controlled comparison of this combined workflow inspected; stable IDs alone are insufficient. **Confidence:** Low for comparative defect/comprehension benefit. **Unresolved:** Does the added record prevent consequential mistakes beyond a simpler contextual review?

### C-06

**Claim:** The worked examples and failure-injection/transfer tests are prospective diagnostics, not translations or results.

**Class:** `hypothesis`. **Support and locator:** Original P05 synthesis; inspected F01-PAT-01 corrected transfer example, packet DEP-F01.

**Applicability / opposition:** Synthetic task values and candidate rules; no language expertise, participants or target renderer assumed. **Confidence:** Low until local review. **Unresolved:** Do changed-answer cases separate understanding from answer repetition?

### C-07

**Claim:** The pattern may propose presentation changes but does not approve altered task meaning, canon, recording or release.

**Class:** `studio-decision`. **Support and locator:** Doug, P05 complete brief and current instruction, 2026-10-10; inspected W02 dialogue ownership.

**Applicability / opposition:** Separate owners must approve consequential task/meaning changes. **Confidence:** High for authority boundary. **Unresolved:** Coordination decides pattern placement and any registered child work.

## References

All records below were inspected as **relevant-excerpt** on **2026-10-10**. Dates identify the inspected snapshot, not a claim of latest engine support. Repeated records are provenance copies, not independent corroboration. Existing pilot/W02 identities are retained; all P05 identities are run-scoped proposals.

### GDR-SRC-20261010-P05-007

**W3C Internationalization.** [Text size in translation](https://www.w3.org/International/articles/article-text-size.en.html). **Publication/update:** Unknown in inspected text. **Edition:** Informative web internationalization article, live snapshot.

**Locator:** Introduction; English and Chinese are particularly compact; compound nouns; character width; character and line height; abbreviations. **Type:** Official informative guidance. **Supports:** C-04.

**Limits/independence:** Web-oriented, not normative game UI requirements. Historical expansion examples are not adopted as universal percentages. No script-specific font or layout test performed. **Rights:** Reuse license not verified; attributed paraphrase only.

### GDR-SRC-20261010-P05-009

**Unicode ICU project.** [Formatting Messages](https://unicode-org.github.io/icu/userguide/format_parse/messages/). **Publication/update:** Unknown. **Edition:** Live ICU User Guide; inspected passage addresses long-standing MessageFormat, not a verified MF2 status.

**Locator:** Overview; MessageFormat → Complex Argument Types (web text 172–187). **Type:** Official technical/practitioner guidance. **Supports:** C-01.

**Limits/independence:** Whole-message and grammatical-selection rationale; parser/version choice not prescribed. The page’s successor-status note is not used as a current product claim. **Rights:** Reuse license not verified; attributed paraphrase only.

### GDR-SRC-20261010-W02-006

**Yarn Spinner documentation team.** [Localisation and Assets](https://docs.yarnspinner.dev/yarn-spinner-for-unity/assets-and-localization). **Publication/update:** Unknown. **Edition:** Live Yarn Spinner for Unity documentation; exact software release unspecified.

**Locator:** Opening; Localisation Terminology; Workflow (web text 5–53). **Type:** Official technical documentation. **Supports:** C-02.

**Limits/independence:** Line/text/asset associations are documented architecture, not translation quality or a mandatory engine. Product’s resource-value judgments are not adopted. **Rights:** Reuse license not verified; attributed paraphrase only.

### GDR-SRC-20261010-W02-009

**Jennifer O’Donnell, with listed checking contributors; IGDA.** [How to Get the Most from LQA – What It Is and Best Practices](https://igda.org/news-archive/how-to-get-the-most-from-lqa-what-it-is-and-best-practices/). **Publication/update:** 2023-05-31. **Edition:** Published practitioner article.

**Locator:** The LQA Process; The LQA Workflow; Some Things to Be Aware of with LQA (web text 52–97). **Type:** Practitioner guidance. **Supports:** C-03.

**Limits/independence:** In-context QA and change reconciliation, not a controlled cost or defect-rate study. Same organization, different document from W02-010; not independent efficacy evidence. **Rights:** Reuse license not verified; attributed paraphrase only.

## Related entries and history

Owning topic: [Localization and presentation](../topics/localization-and-presentation.md). Packet: [P05 author review and receipts](../reviews/full-run-20261010-p05-review-packet.md). Related genre files: none; contextual adaptations are illustrative only.

**2026-10-10, initial-author-draft, version 0.1.0:** complete initial recipe and ledger, no predecessor artifact or supersession. Author self-review only; independent P05 review has not occurred. No prototype, participant test or host test ran. All approval fields remain null. Next decision: Coordination reviews distinctness, evidence limits and whether to revise before separately authorized validation. No release or implementation authority is conveyed.

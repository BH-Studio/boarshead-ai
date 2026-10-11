---
id: GDR-CAND-20261010-P04-PAT-01
kind: pattern
title: Role-preserving style variation
version: 0.1.0
candidate_revision: initial-draft-1
status: draft
owner_project: BH-GDR-Presentation-and-Interaction
run_id: GDR-FULL-20261010
batch_id: P04
attempt_id: P04-authoring-01
identity_scope: temporary-run-scoped
updated: '2026-10-10'
evidence_checked: '2026-10-10'
aliases:
- readable art variants
- role-stable visual variation
tags:
- style-variation
- role-recognition
- state-comprehension
- conditional-recipe
related_topics:
- GDR-CAND-20261010-P04-TOP-01
related_patterns:
- GDR-CAND-20261010-P04-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-P01-13
- GDR-SRC-20261010-P04-001
- GDR-SRC-20261010-P01-05
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial P04 submission; does not replace or resend any previous batch.
byte_hash_record: ../reviews/full-run-20261010-p04-integrity-receipt.md
---

# Role-preserving style variation

**Draft 0.1.0; initial-draft-1. Conditional pattern candidate, not a validated recipe or released guidance.**

## Purpose

Permit art variants to differ meaningfully without silently changing the features a player relies on to recognize an already-known role or current state. This is especially relevant when environments, characters, props or cosmetic variants are produced by different contributors. The intended benefit is comprehensible variation, not maximum contrast or a uniform visual style. Added value over a simpler reference set is **unestablished**. [C-01]

## Context and prerequisites

The designer can name the task, distinguish role from current state, and identify what the player is legitimately expected to know. The production can author and review variants and meaningful negative examples. An owner can change a misleading style constraint rather than merely asking players to learn around it. [C-02]

The pattern assumes neither a genre nor an art package. Record intended views, screen presentation, selection method, relevant vision/access needs, lighting/backgrounds, motion and language. A static image check alone is not sufficient for a role that is normally recognized through motion or a changing view. P03 camera/platform decisions remain unavailable here. [C-02]

**Do not apply this to concealed roles merely because the author knows them.** It concerns distinctions the intended task makes available, not a mandate to mark every secret, threat or usable object. Offer an explicit assistance route when that is the agreed alternative task, rather than claiming the same information remained hidden. [C-01, C-06]

## Mechanism and evidence

The owning [Art direction topic](../topics/art-direction.md) distinguishes aesthetic preference, identity, state inference and action. Valve and Riot provide production rationales for controlled variation; neither validates this complete recipe. The pattern is an **inference to structure a local comparison**, with a hypothesized player benefit. [C-01, C-03]

| Proposed causal link | Basis | Limit |
|---|---|---|
| Identify a task-bearing feature before varying appearance. | A reviewer can compare the intended meaning of a feature with the actual task. | This is a consistency check; it does not establish that players use that feature. [C-02] |
| Preserve that feature across relevant variants. | Creator accounts motivate separating recognition from decorative variation. | Some identity depends on animation or context; outline is not universally sufficient. [C-03] |
| Test role and state on unfamiliar positive and negative cases. | Different correct answers can discriminate learning from a repeated response. | This is a proposed evaluation design, not evidence of durable transfer. [C-05] |
| Keep required facts available under chosen access settings. | XAG 103 supplies additional-channel guidance. | Availability is not demonstrated usability or equal aesthetic experience. [C-04] |
| Adopt the least complex variant system that meets the local decision. | Extra constraints create work, so comparison must justify them. | Production savings and improved comprehension remain hypotheses. [C-01, C-05] |

## Recipe

### 1. Specify the legitimate distinction

Write the task question and its correct answers. Separate **identity**, **current state** and **choice preference**. For example: “This is a service cabinet; it is unavailable; I may inspect it but cannot use it now.” Define what should remain ambiguous. Do not start with a favorite palette and invent a gameplay function for it afterward. [C-02]

**Exit:** when no player-facing distinction is needed, use ordinary art direction without this pattern. When discovering the role is the intended challenge, keep the hidden classification out of the visible invariants. [C-06]

### 2. Identify candidate role-bearing and variable features

Record the feature a player might use, its expected viewing conditions, and the evidence that it could carry the role. Separately identify freely variable features. Candidate features include characteristic form, visible arrangement, characteristic motion, placement or a task-appropriate label; they are options, not a universal priority order. [C-01–C-03]

Specify at least one meaningful exception in prose: a similarly finished object with another role, or the same role in another finish. “Everything round is friendly” is not an evidence-based invariant. A historical visual association does not establish a personality or moral truth. [C-02, C-06]

### 3. Build a small review comparison, not a mandatory asset quota

Describe a common appearance, a deliberately contrasting variant and a plausible misleading case. Keep their actual task facts explicit in the review record. Compare preserving the candidate feature against uniform presentation and a contextual information alternative. No actual assets are produced by this research recipe. [C-05]

**Branch:** when identifying a role requires a motion signature, move the comparison into the relevant action sequence with the Animation owner. Do not certify recognition from a static silhouette sheet. [C-03]

### 4. Check the information route in context

Plan evaluation in intended views/backgrounds/lighting and with relevant alternative presentations. Determine whether role and state survive chosen settings without adding forbidden information. Another shape or icon is still a visual route; it does not provide nonvisual access. [C-04, C-05]

**Exit:** when the candidate feature cannot carry an essential fact reliably in the supported context, replace or supplement it with an appropriate information route. Do not keep intensifying decoration automatically. When the alternative changes the task’s available information, document that change explicitly. [C-04, C-06]

### 5. Freeze invariant, variation and exception ownership

Record the chosen role-bearing relationship, permissible variation, exceptions, context limits and person/team responsible for adjudicating conflicts. This can be a short annotated specification; the pattern does not demand an elaborate style bible. Review animation, interface and effects when their changes alter the relationship. [C-02]

**Adjustable variables:** explicitness of role indication; surface/detail variation; amount of contextual assistance; reliance on motion; similarity of negative examples; exposure before transfer; view/lighting range; maintenance effort. Values require local justification. No number of colors, silhouette ratio, material count, contrast setting or production saving is recommended. [C-05]

### 6. Compare, narrow or remove

After separate study authorization, test unfamiliar instances with different correct classifications and availability states. Measure recognition and state inference before preference. Retain the contract only within contexts where it contributes enough to justify its constraints; simplify when added bureaucracy or disclosure costs exceed demonstrated value. [C-01, C-05]

**Stop:** unresolved critical-information failures, unintended disclosure of the core task, or inability to maintain a claimed invariant blocks recommending deployment of that version. A clearly bounded art preference may still be chosen locally, but it must not be relabeled validated gameplay knowledge. [C-06]

## Worked examples

### Illustrative: differently finished service cabinets

**Invented; not implemented or tested.** A workshop contains cabinets made by several artisans. The task is to find service equipment, determine availability and decide whether to use it. The proposed invariant is a recognizable service-facing arrangement plus an accessible state presentation. Finish and ornament can differ. A decorative cabinet can share materials without acquiring a service role. [C-05]

| Review record | Candidate treatment | Discriminating check |
|---|---|---|
| Familiar service cabinet, available | Known arrangement, locally appropriate finish, available state. | Identify role and current permission separately. |
| Unfamiliar service cabinet, unavailable | Different finish; same role relationship; unavailable state. | “Looks unfamiliar” must not force the wrong role; familiar role must not imply availability. |
| Decorative cabinet | Similar finish, no service-facing arrangement or service status. | Detect false-positive classification rather than only successful use. |
| Access presentation | Appropriate alternative describing required role/state facts. | Confirm comprehension with actual users; do not infer emotional equivalence. |

If B is identified correctly but the player chooses not to use it, ask for their reason. Preference is not a classification error. If every transfer trial’s correct action is “use,” redesign the test: a repeated response would otherwise appear successful. This directly preserves the selected F01 transfer-discrimination correction. [C-05]

### Illustrative: deliberate environmental contrast

A shared world contains two craft traditions with different geometry and surface treatments. The design need not erase their difference. Specify what connects them at the world level, and only preserve role-bearing features where the task requires cross-region recognition. An unfamiliar artifact whose purpose is deliberately being investigated is excluded until that purpose is learned or assistance intentionally exposes it. No culture-wide preference is asserted. [C-01, C-06]

## Tradeoffs and alternatives

The contract can constrain artists, increase review work and make discoveries too explicit. It can also leave useful variation untouched instead of forcing a single palette on every contributor. Both are proposed consequences to evaluate, not measured production savings. Alternatives include a small set of reference examples, uniform presentation, a reliable contextual label, an inspect action, a chosen assistance mode, or no added distinction. [C-01, C-02, C-05]

An explicit label may be cheaper and clearer but can demand reading/localization. A motion signature may suit the actor but disappear in still views or reduced motion. Surface distinctions may be expressive but fail in some lighting. Those dependencies justify testing the actual task, not declaring one cue type best. [C-02–C-05]

## Failure cases

Misidentification concentrated in one skin or region suggests the contract may not survive that context. Correct role recognition with wrong availability suggests role and state were collapsed. Correct artist predictions but poor unfamiliar-user performance suggest expert knowledge was mistaken for visibility. High liking paired with more task errors is a tradeoff, not an unconditional success. These are hypotheses about diagnostic signs. [C-05]

Proposed repairs are to narrow the invariant, reduce nonessential competing detail, make state explicit, change the information route, or abandon the pattern. An unresolved accessibility failure is not repaired by claiming the same style should be learned through effort. [C-04–C-06]

## Counterexamples and do not use conditions

The strongest countercase is a task whose central decision is inferring an object’s role from ambiguous evidence. A universal role mark would supply the answer. Another is a small production where a few consistent examples already produce adequate recognition and a maintained contract adds overhead without benefit. [C-06]

Do not use this as a fixed silhouette rule, a morality/personality code, a mandate for maximum contrast, a formal accessibility standard, or permission to copy a successful game’s art. Do not assume a declared invariant is a measured player invariant. [C-03, C-04, C-06]

## Playtest

**PROPOSED — NOT PERFORMED.** The owning topic contains the full protocol. Compare uniform presentation, selective role-preserving variation, and contextual information assistance. Match task facts, input/view/exposure where possible and log unavoidably changed visual properties. [C-05]

Recruit relevant unfamiliar and experienced users and actual access users after authorization; justify sample size and precision before recruitment. Counterbalance order/family where feasible. Test first use, repeated use and unfamiliar transfer, including true and false cases with different correct answers. Ask identity, availability and chosen action separately. Record error types, comprehension, assistance, preference, comfort and production work without collapsing them into one quality score. [C-05]

Reject or narrow the claim if the selective system increases consequential errors, discloses a legitimate unknown, fails under chosen settings or only works on memorized examples. Prefer a simpler option when added value remains unestablished at the project’s predeclared uncertainty tolerance. A nonsignificant difference is not equivalence. Critical information failures block advancement; participant withdrawal ends the session. No acceptance threshold has been approved in this draft. [C-05, C-06]

## Claim ledger and sources

### C-01
**Claim:** Preserving task-bearing relationships while permitting variation is a candidate method, with unestablished local benefit. **Class:** `inference`. **Support:** owning topic C-07; GDR-SRC-20261010-P01-13 §§3–4.3; GDR-SRC-20261010-P04-001 recognition/variation passages. **Confidence:** moderate for a defensible comparison, low for efficacy. **Unresolved:** comparison with simpler guidance; no complete-pattern study.

### C-02
**Claim:** A review record should separate role, state, permitted variation, context and ownership. **Class:** `inference`. **Support:** owning topic C-01/C-08/C-10; original synthesis, not a published standard. **Confidence:** moderate for consistency checking. **Limit:** extra process may be unnecessary. **Unresolved:** minimum useful record and actual cost.

### C-03
**Claim:** Creator accounts motivate controlled variation but do not make static silhouette sufficient in every case. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P01-13 §§4.1–4.3 and GDR-SRC-20261010-P04-001 Silhouettes. **Confidence:** high for attribution. **Limit:** historical production accounts, no comparative game trial. **Unresolved:** actual recognition features across variants/views.

### C-04
**Claim:** Required facts need appropriate access channels, with usability and emotional effects evaluated separately. **Class:** `inference`. **Support:** GDR-SRC-20261010-P01-05 Implementation guidelines; owning topic C-06/C-09. **Confidence:** moderate for the application bridge. **Limit:** two visual features are not nonvisual access; no certification. **Unresolved:** accessible implementation and interpretation.

### C-05
**Claim:** The recipe, variables, invented examples and validation procedures are proposed, not tested. **Class:** `hypothesis`. **Support:** original P04 synthesis; inspected F01 selected transfer pattern, examples/transfer-correction passage. **Confidence:** low for eventual value. **Limit:** no participant, prototype, fixed threshold or cost measurement. **Unresolved:** authorized study and discriminating unfamiliar cases.

### C-06
**Claim:** Exclude hidden-role discovery and stop when essential facts or meaningful task uncertainty cannot be preserved. **Class:** `inference`. **Support:** owning topic C-07/C-11/C-13 and explicit task contract. **Confidence:** moderate as a scope boundary, not universal preference. **Unresolved:** whether an assistance route changes the agreed task acceptably.

### C-07
**Claim:** This is an authorized draft research artifact only. **Class:** `studio-decision`. **Owner/date:** Doug; supplied P04 brief, 2026-10-10, Assigned Outputs and boundaries. **Confidence:** high. **Limit:** no release, permanent allocation, assets or tests authorized. **Unresolved:** later review and adoption decisions.

## References

All records below were inspected in relevant passages on 2026-10-10. Source IDs retained from P01 are explicit reuse, not new allocations. New P04 IDs are temporary; central URL/DOI/edition reconciliation remains pending. Document copies and candidate citations do not provide independent corroboration.

### GDR-SRC-20261010-P01-13

**Jason Mitchell, Moby Francke and Dhabih Eng. [Illustrative Rendering in Team Fortress 2](https://cdn.cloudflare.steamstatic.com/apps/valve/2007/NPAR07_IllustrativeRenderingInTeamFortress2.pdf).** Valve / NPAR 2007. Date: 2007; exact publication day unknown. Edition/build: 2007 paper; described game build unspecified.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand production/technical paper. **Locators:** §§3, 4.1–4.3; PDF pp. 2–3, Figures 2–5. **Supports:** C-01/C-03, production rationale only.

**Limits:** One production account, not a player experiment. PDF figures inspected, not game footage. **Relationship:** Same work as P01-13; former steamcdn-a.akamaihd.net route is a host alias, not corroboration. **Rights:** Reuse permission not established; paraphrase only; figures not redistributed.

### GDR-SRC-20261010-P04-001

**bananaband1t / Riot Games. [Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/).** Riot Games. Date: 2021-03-12. Edition/build: Developer article; example build numbers unspecified.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand development account. **Locators:** Silhouettes; Matching Hitboxes; Hierarchy; Minimizing Noise; Clarity in Action (Jhin, Taliyah, Leona and Renekton cases). **Supports:** C-01/C-03, recognition exception only.

**Limits:** Creator-reported practices and problems; no footage watched or controlled outcome data. **Relationship:** Independent production from Valve; retrospective selection and issuer incentives remain. **Rights:** Reuse license not established; paraphrase only.

### GDR-SRC-20261010-P01-05

**Microsoft. [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103).** Microsoft Learn. Date: Last updated 2026-03-04. Edition/build: Unnumbered live page revision checked 2026-10-10.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance. **Locators:** Goal; Implementation guidelines; Visual cues; Color and additional sensory channels. **Supports:** C-04, guidance-to-application inference.

**Limits:** Guidance, not a formal standard, compliance certificate or evidence of emotional equivalence. **Relationship:** Reuses inspected P01-05; P02-005 duplicates this URL. Central deduplication pending. **Rights:** Reuse license not inspected; paraphrase only.

## Related entries and history

Owner: [Art direction — GDR-CAND-20261010-P04-TOP-01](../topics/art-direction.md). Complement: [Action-phase and interruption contract](action-phase-and-interruption-contract.md), when a variant’s movement carries identity. P01 general visual communication and P01/P02 redundant-cue work remain separate inspected dependencies, not additional bundled patterns. Their overlap is not resolved here.

**2026-10-10:** initial P04 pattern, version 0.1.0 / initial-draft-1; predecessor and supersession null. Current claims are inference/hypothesis-led. Same-author self-review completed; P04 independent review not performed. No release, adoption, asset production, playtest or Project/repository change. [C-07]

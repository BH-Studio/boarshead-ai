---
id: GDR-CAND-20261010-P04-TOP-01
kind: topic
title: Art direction
version: 0.1.0
candidate_revision: initial-draft-1
status: draft
owner_project: BH-GDR-Presentation-and-Interaction
run_id: GDR-FULL-20261010
batch_id: P04
attempt_id: P04-authoring-01
updated: '2026-10-11'
evidence_checked: '2026-10-11'
date_basis: UTC; run identifier retains dispatch date 2026-10-10
identity_scope: run-scoped candidate; permanent allocation pending
predecessor_sha256: null
supersedes: null
change_summary: Initial P04 candidate; no predecessor submitted.
aliases:
- visual style system
- art-style cohesion
- material language
tags:
- art-direction
- style
- recognition
- material-language
- production
- accessibility
related_topics:
- GDR-CAND-20261010-P04-TOP-02
- GDR-CAND-20261010-P01-TOP-01
related_patterns:
- GDR-CAND-20261010-P04-PAT-01
- GDR-CAND-20261010-P04-PAT-02
related_genres: []
source_ids:
- GDR-SRC-20261010-P04-001
- GDR-SRC-20261010-P04-002
- GDR-SRC-20261010-P04-003
- GDR-SRC-20261010-P04-004
- GDR-SRC-20261010-P04-010
- GDR-SRC-20261010-P04-011
reviewer: null
approved_by: null
approved_date: null
---

# Art direction

**Draft 0.1.0, initial-draft-1 — coverage open, not released guidance.** This entry helps choose and maintain a visual system. It does not establish that one style is best, that realism predicts appeal, or that a coherent-looking asset is readable in play. Findings, design inferences and untested proposals are separated below. [C-01, C-05, C-13, C-14]

## Decision and scope

**Decision:** Which visual relationships should remain consistent across characters, environments and variants, which should deliberately contrast, and what production effort is warranted to maintain those choices at the player’s actual decision point?

Included: style systems; value, color, material and silhouette language; character/environment cohesion; selective contrast; stylization and realism; audience and viewing differences; and production constraints. Excluded: a rendering implementation, complete color science, asset creation, scene-specific canon, a camera specification, genre rules, certification and commercial-success explanations. P01 owns general visual communication and information access; this topic owns how artistic choices are selected, varied and maintained across content. [C-01, C-10, C-14]

### Working vocabulary

The following are analytic conventions for this draft, not formal standards. [C-01, C-13]

| Term | Working meaning | Decision consequence |
| --- | --- | --- |
| Style system | Chosen relationships among form, detail, palette, surface depiction, light and movement. | Record what may change together and what needs another review. A mood board alone does not specify this. |
| Cohesion | Content appears to belong to a deliberately related visual world. | Related does not mean identical; different roles may need different treatments. |
| Selective contrast | Intentional difference within or against the system. | State whether it identifies an action, identity, location, exception or merely an aesthetic emphasis. |
| Material language | How surface qualities and construction suggest substance, use and history. | Roughness, polish, wear, pattern and shape are candidate visual variables, not automatically reliable gameplay meanings. |
| Silhouette | Projected outline and its relation to pose, accessories and view. | A recognizable concept-sheet outline does not guarantee recognition when turned, occluded or animated. |
| Stylization / realism | Dimensions of selection, simplification and resemblance, rather than opposite quality scores. | Geometry, texture, lighting and motion may occupy different positions; examine their combination. |
| Affordance cue | A presentation feature that a player may interpret as supporting an action. | An intended cue is not proof of recognition, correct interpretation or actual permission. |

### Context assumptions to declare

The abstract guidance is platform-neutral. A later comparison should identify the task, intended experience, view and distance range, display/window scale, lighting and visual effects, input method, language, prior familiarity and access settings. A reversible starting scope for the proposed tests is flat-display interaction using a participant’s familiar input; this is not validation for VR, handhelds, couch play or every visual-access profile. P03 camera/platform candidates were not available for transfer. No numerical screen, brightness, text or target-size recommendation is imported. [C-10, C-12, C-13]

## Core explanation and mechanisms

### Cohesion is a relationship, not uniformity

Two objects can share construction logic while needing different visual priority. Conversely, two factions can differ deliberately without making every prop a competing focal point. The creator precedent is C-02; the proposed application is to name a small set of relationships that matter to the particular decision, then allow expressive differences elsewhere. It does not follow that every game needs faction colors, a universal shape code or a fixed number of palette entries. [C-01, C-02, C-08]

**Proposed mechanism:** an interpretable family resemblance supports a useful expectation → a relevant difference identifies the exception → the player chooses appropriately → the desired aesthetic response may also occur. Creator accounts support the production intention, but this full causal chain is not established by the inspected corpus. Players may instead notice the wrong feature, rely on a label, learn an unintended mapping or simply enjoy the composition without decoding it. [C-03, C-08, C-09, C-12]

### Preserve the decision relationship, not every feature

A costume change, new environment treatment or altered idle pose can change a familiar visual read. The useful question is not “Did we retain the approved number of features?” It is “Can the player still make the distinctions this situation legitimately requires?” The contrast between Riot’s recognizability goal and its context-specific ponytail exceptions motivates this narrower formulation; it does not prove the proposed workflow. A feature can be stable in one family and intentionally absent in another. [C-03, C-04, C-08]

The burden of evidence also changes with the task. Immediate recognition might be essential for selecting a teammate but inappropriate for a disguised figure whose identity is intentionally unresolved. In that case, preserve access to legitimate action information without prematurely revealing the hidden identity. This is an illustrative boundary, not a genre rule. [C-08, C-13]

### Material appearance is not an action contract

A polished handle, cracked wall or luminous surface may suggest use; it may also be decoration. Art direction should declare whether a treatment identifies substance, condition, interaction, affiliation or no gameplay category at all. Where treatment predicts action, compare both valid and invalid instances and examine what happens when wear, wetness, lighting or distance changes the appearance. This is a proposed discrimination test, not a claim that a particular material always carries a particular meaning. [C-09, C-13]

Do not settle ambiguity by turning every usable object into the brightest object. That can be an appropriate explicit mode, but it changes the composition and can communicate more than intended. Alternatives include geometry, framing, animation, a label or on-demand assistance; whether any one is sufficient remains a P01/P02-informed access and comprehension question. [C-06, C-08–C-10]

### Appeal, legibility and production effort are different outcomes

The empirical boundary in C-05 challenges a simple realism ranking. It does not select a house style or prove stylization is cheaper. A treatment can be appealing but poor at distinguishing state; another can be efficient to author yet costly to revise across variants. Judge style fit, task accuracy, representational interpretation and production workload separately. Do not use sales, popularity, awards or a creator’s satisfaction as causal player evidence. [C-05, C-11, C-12]

## Design choices and alternatives

These are conditional options derived from the evidence boundaries, not an experimentally established ordering. [C-08–C-13]

| Choice | Appropriate decision context | Benefit sought, cost and alternative |
| --- | --- | --- |
| Shared form/material vocabulary | Many assets must feel related and maintenance matters. | May organize authoring and review; can erase useful distinctions or propagate a poor assumption. Start with a small representative family, not the whole content roster. |
| Selective character/background contrast | A required subject is hard to distinguish in actual task views. | Can make priority deliberate; can undermine camouflage or make noninteractive decoration look usable. Compare against less detail or a contextual aid. |
| Stable identity with variant expression | Several appearances represent the same role or entity. | Preserve required recognition while allowing novelty. Costs include mixed-view, animation, equipment and exception testing. A simple label may be preferable. |
| Deliberate mismatch or discontinuity | The contrast itself carries an intended meaning, transformation or interpretive question. | Avoid treating all mismatch as failure. Required facts still need an accessible route; aesthetic confusion and task confusion are not interchangeable. |
| More realistic depiction | The intended experience or available production pipeline calls for it. | Evaluate specific surfaces and motion rather than assuming a credibility bonus. The evidence does not establish a general appeal or cost advantage. |
| Strong abstraction / sparse detail | Selection and omission suit the desired expression or production boundary. | Can remove useful distinctions as easily as clutter. Do not infer accessibility from low polygon count or limited colors. |
| Minimal or no additional style rule | Existing content already supports the decision and intended experience. | Avoid unnecessary style bureaucracy. Retain an explicit record of exceptions that affect task meaning or access. |

## Application process

**Proposed process; no asset work or testing occurred.** [C-13]

1. **Diagnose the decision failure.** Separate an unreadable target, misunderstood material, incoherent identity, unwanted emotional reading and unsustainable production demand. Record the player-facing consequence. “Needs polish” is not sufficiently discriminating.
2. **Write a compact style contract.** State intended visual relationships, required identity/action distinctions, allowable ambiguity, permitted variation and examples that should be rejected. Name the decision owner for a later project; this draft does not appoint or approve one.
3. **Choose a bounded representative set.** Include a character or focal object, a background family, a required interaction and a visually similar noninteraction. Include a deliberate exception. Select actual task views and access conditions rather than a beauty-render-only review.
4. **Compare coherent alternatives.** Contrast uniform treatment, selective contrast and the existing presentation. Keep task rules, layout and assistance comparable. Do not improve geometry, lighting and labeling in only one condition and then attribute the result to a palette choice.
5. **Specify variation and exception handling.** Record which combinations need review: costume/prop, pose, surface condition, lighting, detail reduction and language. Preserve meaning under the combination, not merely the isolated asset. An approved base asset is not approval of all descendants.
6. **Evaluate interpretation before preference.** Ask what can be acted on and why before revealing correctness. Include cases in which the right answer changes. Ask about appeal and intended expression separately, with open-ended alternatives rather than forcing the director’s preferred adjective.
7. **Revise, narrow or stop.** Keep only supported distinctions; remove constraints that add cost without demonstrated value. A failing material cue may warrant an explicit interaction aid rather than more elaborate surface work. Record access failures and unrepresented contexts rather than averaging them away.

### Production and review record

A later style dossier can contain a chosen relationship, its purpose, the relevant task views, permissible deviations, rejected examples, dependencies, rights/provenance notes and the evidence needed to revisit it. Track time spent creating, correcting and propagating variants separately; do not assume a reusable base reduces total labor in every case. Record a performance budget only after the actual platform/pipeline owner supplies one. This is a planning proposal, not an approved asset specification or a measured cost model. [C-10, C-11, C-13]

## Patterns and genre adaptations

[Recognition-preserving style variation](../patterns/recognition-preserving-style-variation.md), `GDR-CAND-20261010-P04-PAT-01`, owns the repeatable variation-and-exception recipe. [Animation and performance](animation-and-performance.md) owns motion, interruption and expressive delivery; its [State-aligned animation handoff](../patterns/state-aligned-animation-handoff.md) is relevant when a style change alters poses or effects that communicate action state.

Reviewed external dependencies are identified by exact IDs and hashes in the [P04 dependency record](../reviews/full-run-20261010-p04-review-packet.md#reviewed-dependency-transfer). They are not bundled again. P01/P02’s existing critical-cue patterns remain the owners of redundant and fact-preserving cue alternatives; this packet does not create another such pattern.

No genre files are created or transferred. For a scene combining discovery and fast identification, specify which identities may remain hidden and which actions must be unambiguous; do not pick a winning genre label. Character motive and canon belong to W01’s character-design scope, not a material or silhouette rule. [C-08, C-12, C-13]

## Examples and counterexamples

### Creator-reported cases, not observed gameplay

The Valve account supplies a case of contrast within a common art treatment; the two Riot accounts supply a case of controlled variation and exceptions. Their actual assertions and limitations are recorded in C-02–C-04. These are two production contexts, not three independent efficacy studies. No shipped build, gameplay session or embedded video was inspected. [C-02–C-04]

### Illustrative worked example — a shared service environment

**Synthetic and untested.** A space contains storage cabinets, service panels and a portable inspection tool. The intended art direction uses a common construction language. An operable panel must remain distinguishable from a decorative panel, while the tool must be identifiable against either cabinet family. [C-13]

Start by recording the required actions: identify the tool, identify the currently operable panel, and recognize a locked state. Do not assign “all brushed surfaces are operable” merely because that looks coherent. Try a shared mechanical seam vocabulary with a distinct usable control, then vary paint and wear without changing the control’s role. Include a decorative plate with the same paint and an operable control without that paint. Ask for action predictions before feedback. This prevents a test in which every shiny object happens to be the correct answer. [C-08–C-10, C-13]

Compare the candidate to an explicit contextual label and to the existing presentation. At a small task view the control may disappear; in a glossy lighting condition a cabinet may dominate. Neither result is a reason to claim the audience “failed to appreciate” the art. Revise the discriminating feature, change the supporting presentation or narrow the viewing conditions. No rendering, measurements or player responses were produced here. [C-10, C-12, C-13]

### Strong counterexample — identity deliberately unresolved

**Illustrative.** A figure’s allegiance should remain unknown while the player can still choose whether to approach, speak or withdraw. Forcing a standardized faction silhouette or obvious material code would reveal a fact the scene deliberately withholds. The recognition-preserving recipe should be restricted to legitimate task facts, not used to erase ambiguity. A visually discontinuous reveal can be the intended art direction rather than a defect. [C-08, C-13]

## Failure modes and constraints

| Warning sign to investigate later | Competing interpretation | Candidate response, not a tested fix |
| --- | --- | --- |
| Artists agree on cohesion; players select the wrong object. | Shared treatment is overriding action distinctions. | Test the actual relation, reduce competing detail or add an explicit aid. |
| One pose reads correctly; another loses identity. | The selected feature depends on angle, motion or an accessory. | Evaluate the combined asset, not a silhouette still alone. |
| A skin is recognizable only because a reviewer already knows it. | Familiarity is masking weak transfer. | Separate practiced recognition from unfamiliar interpretation. |
| Appearance predicts the same answer in every evaluation item. | The task is not discriminating the intended rule. | Include matched contrary cases and predictions before feedback. |
| A reduced-motion or alternative-color setting loses a required fact. | Decorative and functional roles were not separated. | Reassign the critical distinction and evaluate a usable alternate route. |
| A shared base creates repeated corrective work. | Variation exceeds the original system’s assumptions. | Permit a justified branch or reduce the variant promise. |
| “Threatening,” “trustworthy” or “normal” is inferred from a body type alone. | The style embeds an unintended stereotype or a narrow cultural reading. | Revisit context and representation; seek relevant review rather than treating agreement as universal. |

These are proposed diagnostic cases. They are not observations from a completed P04 playtest. [C-09–C-13]

**Accessibility:** do not depend solely on color or visual ornament for critical information. A visual simulation can help locate a problem but cannot substitute for people using the intended access route. Evaluate preferred settings and assistance, including whether alternatives change what is known. Preserve P01’s distinction among CSS pointer units, rendered text-body height and platform guidance; none is converted into a P04 art rule. [C-06, C-07, C-12]

**Localization and representation:** text on surfaces, symbols, gestures and decorative motifs may carry meanings outside the intended one. Treat translation, reading direction, symbolic interpretation and bodily representation as explicit review questions. The inspected corpus does not establish a universal cultural code. Avoid imposing “realistic equals trustworthy” or “unusual body equals hostile.” These are ethical and interpretive safeguards, not claims that a particular asset has caused harm. [C-12, C-13]

**Rights and production:** reference provenance and permission to reuse assets or a performer’s likeness require separate review. This packet contains no assets and grants no rights. A new style rule can affect rigs, material variants, lighting, animation and external asset integration; ownership and change propagation should be visible before a later implementation is approved. No legal conclusion, staffing estimate or performance certification is offered. [C-11, C-14]

## Playtest and validation

**PROPOSED — NOT RUN.** The following is a study specification for a later authorized decision, not a pilot already performed. It requires no fixed participant count, timing window or numerical success threshold from this literature. [C-13, C-14]

**Question:** Does the proposed selective-cohesion treatment preserve required action and identity distinctions while providing a worthwhile artistic benefit over the existing or simpler alternative?

**Comparisons:** existing presentation; proposed constrained variation; and an explicit-label or less-detailed alternative selected for the actual task. A separate deliberately unconstrained variant can diagnose what the contract protects, but it is not automatically a fair quality comparison. Keep action rules, task layout, available information, viewing conditions and exposure comparable; record unavoidable differences.

**Participants and procedure:** include unfamiliar and practiced users of the relevant task and actual users of the target visual/nonvisual access routes. Do not treat a small convenience sample as representative. Before collecting data, the study owner must specify inclusion, sample rationale and the practical tolerance for added recognition errors or workload. Counterbalance conditions and use different matched items where carryover would reveal answers. Collect identity/action predictions and reasons before feedback; include both permitted and forbidden actions. Then collect separate aesthetic, interpretation and comfort reports.

**Measures:** confusion matrix of identities and action states; false interaction and missed-action attempts; uncertainty reports; task completion and correction behavior; separate style-fit and appeal judgments; requests to change settings; and documented authoring/revision effort. Time measures require an agreed start/end event and actual instrumentation; none has been measured here.

**Confounds:** prior familiarity, item difficulty, exposure order, label availability, screen/view differences, lighting, animation, simultaneous changes and evaluator expectations. Do not interpret faster action as better art, nor a preference score as adequate access.

**Decision rule:** reject or revise any candidate that makes an essential fact unavailable in a supported route or systematically communicates the wrong action/identity. When recognition is not practically worse under a predeclared local criterion and the intended artistic value is credibly supported, retain only the tested scope. Where results are inconclusive, do not claim equivalence; prefer a reversible narrower treatment or gather the evidence needed for the actual production decision. Keep a deliberate ambiguity only when it concerns information the task permits to remain unknown. Participants may pause, adjust settings or withdraw; requests to stop are not inconvenient outliers. [C-08–C-13]

## Claim ledger

Claim IDs are local to this entry. Confidence describes the exact scoped wording, not a source’s prestige or the recipe’s overall efficacy. Proposed procedures and examples are not approved studio decisions.

### C-01

**Claim:** Treat art direction as a proposed system of visual relationships and permissible variation, not a single realism slider. **Class:** `inference`. **Confidence:** moderate as a useful analytic distinction, not a validated optimum.

**Support / precise locator:** GDR-SRC-20261010-P04-001, §3/§4.2–4.3; GDR-SRC-20261010-P04-002, Filling Up Buckets; GDR-SRC-20261010-P04-004, §4.

**Applicability, contrary evidence and unresolved question:** This is P04 synthesis. Which relationships matter depends on the task, intended experience and audience; a deliberately mixed style may be appropriate.

### C-02

**Claim:** Valve reports using shared illustrative treatment while distinguishing its opposing environments through different shapes, materials and palettes. **Class:** `practitioner-heuristic`. **Confidence:** moderate for the creator account; no efficacy estimate.

**Support / precise locator:** GDR-SRC-20261010-P04-001, §4.2 World Modeling and §4.3 Texture Painting, PDF pp.2–3.

**Applicability, contrary evidence and unresolved question:** One historical production. Supports considering selective contrast, not a universal warm/cool faction code or guaranteed recognition.

### C-03

**Claim:** Riot describes preserving recognizability while varying the combined model, animation and effects treatment of skins. **Class:** `practitioner-heuristic`. **Confidence:** moderate for accurate attribution, low for general effectiveness.

**Support / precise locator:** GDR-SRC-20261010-P04-002, Silhouettes and Filling Up Buckets.

**Applicability, contrary evidence and unresolved question:** A competitive-game production goal. No measured change budget; no reason to make all objects equally distinctive.

### C-04

**Claim:** The Lee Sin account reports common base-mesh work, selective omission of a new ponytail in some skins, and additional cross-skin animation/clipping checks. **Class:** `practitioner-heuristic`. **Confidence:** moderate for reported decisions; costs not quantified.

**Support / precise locator:** GDR-SRC-20261010-P04-003, Preparing the Ponytail; Base Meshes and 3D Sustainability; Making Skins with Style.

**Applicability, contrary evidence and unresolved question:** Variation exceptions can protect an existing identity. No measured production saving or proof that a common rig suits every body, costume or performance.

### C-05

**Claim:** Render-style appeal did not form a simple increasing realism ranking in the inspected still/moving comparison. **Class:** `empirical-evidence`. **Confidence:** moderate, narrow controlled stimulus set.

**Support / precise locator:** GDR-SRC-20261010-P04-004, §4 and §5.1: separate groups of 17 viewers rated still or moving male-character treatments. Several abstract and realistic styles were among the more appealing categories.

**Applicability, contrary evidence and unresolved question:** Brief viewing, selected styles and a deliberately ill-looking treatment; not an equivalence test, gameplay comparison or general uncanny-valley law. No effect-size or population-wide preference is inferred.

### C-06

**Claim:** XAG 103 recommends alternatives to color-only and visual-only critical information and distinguishes simulation checks from evaluation with affected players. **Class:** `practitioner-heuristic`. **Confidence:** high for what this vendor page recommends, not for a particular design’s access.

**Support / precise locator:** GDR-SRC-20261010-P04-010, Goal; Implementation guidelines on color, other modalities and player evaluation.

**Applicability, contrary evidence and unresolved question:** Official guidance, not a formal standard. Redundant visual features are not automatically nonvisual access; no emotional-equivalence result.

### C-07

**Claim:** XAG 117 supports control of distracting or non-core motion while retaining a stated exception for some gameplay backgrounds behind interface content. **Class:** `practitioner-heuristic`. **Confidence:** high for the scoped recommendation.

**Support / precise locator:** GDR-SRC-20261010-P04-011, Implementation guidelines, moving UI/background exception and repetitive non-core animation.

**Applicability, contrary evidence and unresolved question:** Not an instruction to freeze every gameplay animation. No medical safety, numerical threshold or P03 camera-setting recommendation.

### C-08

**Claim:** When a task needs stable identification, preserve the required relationship through stylistic changes rather than requiring every visual feature to remain fixed. **Class:** `inference`. **Confidence:** moderate for the conditional rationale; local benefit untested.

**Support / precise locator:** GDR-SRC-20261010-P04-002, Filling Up Buckets; GDR-SRC-20261010-P04-003, Preparing the Ponytail; C-03/C-04; reviewed P01 visual-communication, Core explanation and mechanisms.

**Applicability, contrary evidence and unresolved question:** The bridge is to compare what players must distinguish, not to canonize a particular shape. Disguise, discovery and interpretive art may intentionally withhold identity. See P04-CON-01.

### C-09

**Claim:** A recurring material treatment should not be treated as an established affordance until its relation to action has been checked in context. **Class:** `hypothesis`. **Confidence:** low for effectiveness of the proposed validation workflow.

**Support / precise locator:** GDR-SRC-20261010-P04-001, §4.2–4.3 gives a production vocabulary, not affordance-learning evidence; reviewed P01 distinguishes recognition from meaning/action.

**Applicability, contrary evidence and unresolved question:** P04 proposes an action-prediction check across lighting, wear and noninteractive lookalikes. Material semantics, audience familiarity and display variation remain unmeasured.

### C-10

**Claim:** Evaluate characters, surroundings and motion together at actual task views before expanding a style across assets. **Class:** `inference`. **Confidence:** moderate as a risk-control proposal, not measured savings.

**Support / precise locator:** GDR-SRC-20261010-P04-001, §4.1–4.3; GDR-SRC-20261010-P04-002, Silhouettes; GDR-SRC-20261010-P04-003, cross-skin checks.

**Applicability, contrary evidence and unresolved question:** An isolated beauty render can omit the decision context by construction. P03 camera/display details are missing; local view coverage and production costs need later agreement.

### C-11

**Claim:** Style constraints can organize repeatable production, but reuse and exception management create different costs that must be measured locally. **Class:** `inference`. **Confidence:** moderate for named work categories, unknown magnitude.

**Support / precise locator:** GDR-SRC-20261010-P04-003, Base Meshes and 3D Sustainability / Making Skins with Style; GDR-SRC-20261010-P04-001, §4.3.

**Applicability, contrary evidence and unresolved question:** No staffing, asset count, performance budget or stylization-versus-realism cost ranking is supported. Shared assets can also make corrective changes propagate.

### C-12

**Claim:** Separately evaluate desired expression, player interpretation, decision accuracy, comfort and representational effects. **Class:** `inference`. **Confidence:** moderate as measurement discipline; no guaranteed method of inclusion.

**Support / precise locator:** GDR-SRC-20261010-P04-004, §5.1; GDR-SRC-20261010-P04-010, actual-player evaluation; reviewed P02 multimodal-communication, decision facts versus emotion; W01 character-design, Decision and scope.

**Applicability, contrary evidence and unresolved question:** Aesthetic preference is not comprehension. Do not use appearance or movement to diagnose a real person’s honesty, morality, ability or identity. Cross-cultural and specialist access evidence remains limited.

### C-13

**Claim:** The application sequence, illustrations and prospective comparisons below are testable proposals, not results or approved production requirements. **Class:** `hypothesis`. **Confidence:** low for untested feasibility and effect.

**Support / precise locator:** Original P04 synthesis under the supplied brief, Decision questions and output requirements; proposed application of C-08–C-12.

**Applicability, contrary evidence and unresolved question:** No prototype, assets, participants or test data. A future study owner must specify resources, decision tolerances and inclusion before execution; no invented power guarantee.

### C-14

**Claim:** P04 is authorized bounded research; candidates and source identities remain provisional, unreleased and separate from adoption. **Class:** `studio-decision`. **Confidence:** high from explicit instruction.

**Support / precise locator:** Doug’s P04 message and attached Pasted text(3).txt, Assigned outputs, Authorization update, Reviewed dependency receipt and Current jobs and boundaries; dispatch run dated 2026-10-10.

**Applicability, contrary evidence and unresolved question:** Owner Doug. This permission does not approve evidence conclusions, canonical allocations, implementation, participant work, publication or repository/Project-source changes.

## References

All public records below were inspected in the stated passages on **2026-10-11 UTC**. IDs are P04-scoped source records, not permanent SRC allocations. Dates of older works are publication dates, not claims of current game behavior. Repeated reference records support standalone reading; they are not extra evidence.

### GDR-SRC-20261010-P04-001

**Jason Mitchell, Moby Francke and Dhabih Eng, Valve.** [Illustrative Rendering in Team Fortress 2](https://cdn.akamai.steamstatic.com/apps/valve/2007/NPAR07_IllustrativeRenderingInTeamFortress2.pdf). **Publisher:** NPAR / Valve author paper. **Publication/update:** 2007; exact publication day not established. **Edition/build:** NPAR 2007 paper; six-page PDF; production build unspecified.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Primary creator production/technical account. **Exact locators:** §3 Commercial Illustration Techniques; §4.1 Character Modeling, Figure 2; §4.2 World Modeling; §4.3 Texture Painting; PDF pages 2–3. **Claims supported in this entry:** C-01, C-02, C-09–C-11.

**Limits:** No controlled player-recognition experiment, modern-device benchmark or causal sales evidence. PDF pages 2–3 visually inspected; no game build or footage observed. **Independence/deduplication:** Independent production context from Riot. Same paper as reviewed GDR-SRC-20261010-P01-13, whose older Steam CDN URL is an alternate route; central source consolidation pending. **Rights:** Original copyright; reuse permission not established. Paraphrase only; no artwork, screenshots or assets distributed.

### GDR-SRC-20261010-P04-002

**bananaband1t, Riot Games.** [Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/). **Publisher:** Riot Games / League of Legends. **Publication/update:** 2021-03-12. **Edition/build:** Dated developer article; game build unspecified; historical account, not current patch verification.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Primary creator account / practitioner guidance. **Exact locators:** The Unbreakable Vows; Silhouettes; Filling Up Buckets; Cosmetic Animations. **Claims supported in this entry:** C-01, C-03, C-08, C-10.

**Limits:** Describes Riot goals and constraints, not comparative player outcomes. Media not played. The skin-variation metaphor is not a measured budget or a universal invariant. **Independence/deduplication:** Same studio and game family as source 003: not independent corroboration of efficacy. Cross-batch URL/edition deduplication pending. **Rights:** Reuse license not established; attributed paraphrase only.

### GDR-SRC-20261010-P04-003

**ASU Team, Riot Games; named concept, character, technical-art and animation contributors.** [/dev: Modernizing the Monk](https://www.leagueoflegends.com/en-gb/news/dev/dev-modernizing-the-monk/). **Publisher:** Riot Games / League of Legends. **Publication/update:** 2024-04-08. **Edition/build:** Lee Sin art-and-sustainability update developer article; exact game build unspecified.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Primary multidisciplinary creator account. **Exact locators:** Creating Consistency Across Skins; Preparing the Ponytail; Base Meshes and 3D Sustainability; Animation → Making Lee’s Animations More Impactful, Float like a Butterfly, Sliding Hitboxes like a Lee, Making Skins with Style. **Claims supported in this entry:** C-04, C-08, C-10, C-11.

**Limits:** Intentions and reported production issues, not measured satisfaction, cost savings or a directly observed build. Animation contributors: Sean “Riot Redepoka” Yeung and Einar “Riot Beinhar” Langfjord. Embedded media not played. **Independence/deduplication:** Same production line as source 002; multiple contributors are not separate efficacy studies. Cross-batch deduplication pending. **Rights:** Reuse license not established; paraphrase only; no likenesses, media or assets copied.

### GDR-SRC-20261010-P04-004

**Rachel McDonnell, Martin Breidt and Heinrich H. Bülthoff.** [Render me Real? Investigating the Effect of Render Style on the Perception of Animated Virtual Humans](https://www.scss.tcd.ie/Rachel.McDonnell/papers/Siggraph2012a.pdf). **Publisher:** ACM Transactions on Graphics. **Publication/update:** 2012-07. **Edition/build:** 31(4), Article 91; eleven-page author PDF; DOI 10.1145/2185520.2185587.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Original human perception experiments. **Exact locators:** §4 Choosing Render Styles; §5.1 Still vs. Moving, methods/results, PDF pages 4–6; §5.2 Motion Anomalies and §5.2.1 Results, PDF pages 6–7. **Claims supported in this entry:** C-05; indirect C-12.

**Limits:** Selected male-character stimuli and brief viewing tasks, not controlled gameplay. A deliberately ill-looking treatment complicates a neutral realism continuum. No raw-data reanalysis. PDF pages 5 and 7 visually inspected; the page-6 screenshot route failed. **Independence/deduplication:** Original study; author PDF and DOI/publisher record are one source. Cited by source 005: independent cohorts, not disconnected intellectual lines. Lowercase author-path route failed; uppercase path succeeded. **Rights:** ACM copyright; no new reuse permission inferred from author hosting. No figures or stimulus media redistributed.

### GDR-SRC-20261010-P04-010

**Microsoft.** [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103). **Publisher:** Microsoft Learn. **Publication/update:** Last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live page revision inspected on evidence-check date.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official vendor accessibility guidance. **Exact locators:** Goal and Overview; Implementation guidelines → alternatives to color and visual-only information; simulation-filter and actual-player evaluation paragraphs. **Claims supported in this entry:** C-06; indirect C-12.

**Limits:** Practitioner guidance, not a formal standard, legal advice or certification. Availability of an alternative is not demonstrated usability or emotional equivalence. Public body inspected despite authorization boilerplate. **Independence/deduplication:** Same document as reviewed GDR-SRC-20261010-P01-05 and GDR-SRC-20261010-P02-005; central reconciliation pending. Same issuer as source 011. **Rights:** Vendor page; content reuse license not inspected; paraphrase only; no example media copied.

### GDR-SRC-20261010-P04-011

**Microsoft.** [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117). **Publisher:** Microsoft Learn. **Publication/update:** Last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live page revision inspected on evidence-check date.

**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official vendor accessibility guidance. **Exact locators:** Implementation guidelines → moving/blinking/scrolling UI and its background-motion exception; camera motion; repetitive non-core animation; parsed text lines 43–121. **Claims supported in this entry:** C-07.

**Limits:** Not a universal freeze-all-gameplay requirement, medical safety threshold or certification. No FOV, flashing or animation-duration limit is extracted. Camera-setting research remains P03 ownership. **Independence/deduplication:** Same document as reviewed GDR-SRC-20261010-P01-10 and GDR-SRC-20261010-P02-010; central reconciliation pending. Related vendor guidance is not independent efficacy evidence. **Rights:** Vendor page; content reuse license not inspected; paraphrase only.

## Open questions and change history

Open coverage: recognition under actual camera/display combinations; material semantics across lighting and surface states; cross-cultural and nonvisual interpretation; measured total production cost; artist/performer rights processes; and whether the proposed constrained-variation recipe improves its actual task. No equal-budget realism/stylization comparison, complete art-history survey or gameplay efficacy test was performed.

P04-CON-01 preserves the tension between required recognition and legitimate ambiguity; P04-CON-02 preserves the absence of a simple realism ranking. These are packet-local records, not newly allocated global contradiction IDs. Additional material/affordance and performance-simplification questions are [queued child-work requests](../reviews/full-run-20261010-p04-review-packet.md#child-extension-queue), not silently omitted patterns or authorized executions.

**2026-10-11 UTC:** initial P04 candidate, version 0.1.0, revision initial-draft-1; no predecessor, supersession or prior P04 submission asserted. Author self-review is recorded in the packet and is not independent review. Candidate/source canonical reconciliation, host tests and release remain pending. Next decision: independent content review of these qualified candidates and coordination of missing dependencies, not implementation.

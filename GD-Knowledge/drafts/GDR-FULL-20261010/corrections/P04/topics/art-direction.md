---
id: GDR-CAND-20261010-P04-TOP-01
kind: topic
title: Art direction
version: 0.1.0
candidate_revision: review-correction-1
status: draft
owner_project: BH-GDR-Presentation-and-Interaction
run_id: GDR-FULL-20261010
batch_id: P04
attempt_id: P04-authoring-01
identity_scope: temporary-run-scoped
updated: '2026-10-11'
evidence_checked: '2026-10-10'
aliases:
- visual style system
- material language
- environment and character cohesion
tags:
- art-direction
- style
- material-language
- readability
- production
- conditional-guidance
related_topics:
- GDR-CAND-20261010-P04-TOP-02
- GDR-CAND-20261010-P01-TOP-01
- GDR-CAND-20261010-P01-TOP-03
related_patterns:
- GDR-CAND-20261010-P04-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-P01-13
- GDR-SRC-20261010-P04-001
- GDR-SRC-20261010-P04-002
- GDR-SRC-20261010-P04-003
- GDR-SRC-20261010-P01-05
- GDR-SRC-20261010-P01-10
- GDR-SRC-20261010-P04-011
- GDR-SRC-20261010-P04-012
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: 046dae78732fb9b9ec7e0c4d44c432ad3cf11478f002c7717864584e2e19316d
supersedes: null
change_summary: Selected Origin B precision review; exact predecessor and provenance receipt retained.
byte_hash_record: ../reviews/full-run-20261010-p04-integrity-receipt.md
---

# Art direction

**Draft 0.1.0; candidate revision initial-draft-1. Not released, independently reviewed for P04, or approved for a game.** This entry helps choose a visual system, not a universal aesthetic. Its strongest recommendation is an **inference**: preserve the distinctions needed for the current task while allowing deliberate stylistic variation. Whether that improves a particular game remains to be tested. [C-07]

## Decision and scope

**Decision:** Which relationships among shape, value, color, surface response, detail, environment, character and motion should remain consistent, and where is contrast worth its interpretive and production cost?

The core is genre-neutral. It includes style systems, silhouette and role recognition, material language, environment/character cohesion, audience and display assumptions, production constraints and accessible presentation. It excludes creating assets, selecting a studio’s commercial art package, certifying accessibility, defining character morality from appearance, and selecting a camera or rendering pipeline. This is research advice, not implementation authorization. [C-01, C-14]

**Working terms, not a formal standard:** a *style system* is a set of intended relationships and permissible exceptions, rather than a mood board alone. *Cohesion* means that elements can be read as belonging to an intended whole; it need not mean visual uniformity. *Material language* includes both rendered surface behavior and the meanings a game asks players to associate with surfaces. *Readability* must name a task: identifying an actor, distinguishing usable from decorative equipment, estimating an action boundary, or understanding a state. Aesthetic preference, recognition and correct action are separate outcomes. [C-01]

### Inspected dependencies and boundaries

The parent-selected waves 1–2 archive was materialized, hashed and inspected before these distinctions were transferred. P01 Visual communication, Interface and information, and Accessibility and inclusive interaction were read as `review-correction-1`; P02 Controls and input, Feedback and game feel, and Multimodal communication were also read as `review-correction-1`. Their ownership is preserved: P04 owns the **style system and its production variation**, not a replacement general hierarchy, input, or redundant-cue topic. Exact paths, hashes and passage ranges are in the [dependency record](../reviews/full-run-20261010-p04-review-packet.md#inspected-dependency-transfers).

P01’s corrected distinction among **CSS pixels, rendered text body height, formal web conformance and vendor guidance** is retained. No text-size, contrast, target-size or motion threshold is copied into this entry. The original standards would need their own applicability check before a numerical requirement was adopted. Two visual distinctions do not become two sensory channels. The unresolved P01/P02 cue-pattern overlap remains unresolved. [C-06, C-09]

**Application assumptions to declare:** intended task and viewing distance; camera views and actor size on the actual display; input and selection method; illumination and visual clutter; languages; relevant vision, motion and cognitive access needs; assistance settings; asset/rig/material budget and update cadence. No desktop, headset, touch device, art asset vendor or particular game is the default. P03 Camera and framing and Platform and display context, and F04 Combat and conflict systems / Movement and traversal, were not supplied as inspectable candidate bytes here. Thus this draft does not inherit their decisions or numerical settings. [C-09]

## Core explanation and mechanisms

### Cohesion and contrast are not opposites

Valve’s TF2 paper reports an intentionally controlled shape/texture system alongside contrasting team environments. Riot’s account prioritizes recognition across presentation changes and documents clarity failures. These are production rationales, not comparative evidence that one visual style causes better play. [C-02, C-03]

**Evidence-to-application bridge:** where a game repeatedly asks the same distinction, accidental variation can create additional interpretations to check. Conversely, making all relevant objects look alike can erase the distinction. A useful starting hypothesis is therefore to preserve **role-bearing features**, while allowing variation in features that need not carry that role. The important feature may be outline, characteristic movement, placement, a labeled control, or a combination; it must be established through the task, not chosen from a universal shape dictionary. [C-07]

The proposed causal chain is: a stable role-bearing relationship is perceivable → the player recognizes it across a new presentation → the player infers the correct current state → the available action becomes understandable. The inspected creator accounts support why this chain is worth testing, not each causal link. Recognition alone does not prove state comprehension; state comprehension does not require choosing the designer’s preferred action. [C-07, C-13]

### Stylization, realism and appeal require separate questions

McDonnell and colleagues’ explicit-rating experiments used separate groups of 17 for still images and movies of selected virtual-human render styles. Highly abstract and highly realistic examples were among the appealing styles; an intermediate style was especially poorly rated. Lighting was not fully controlled, and the authors identify the lack of emotional content as a limitation. This does **not** establish an optimal realism curve for games, environments or all audiences. [C-04]

The design implication is to compare actual candidate combinations rather than rank the words “realistic” and “stylized.” Geometry, lighting, texture treatment, movement, expression and familiarity can change together. A preferred portrait is not proof of clearer gameplay, nor is an unfamiliar style necessarily a production mistake. Intended strangeness can be a valid artistic goal; the unresolved question is whether it interferes with the facts the player is supposed to understand. [C-07, C-11]

### Physical surface behavior does not define gameplay meaning

Epic’s physically based materials documentation separates base color, roughness, metallic and specular controls and explicitly includes non-photorealistic uses. It describes a shading model, not a rule for which objects should be actionable. [C-05]

**Bridge:** define two different records. The visual record describes a surface’s rendering and intended variation; the interaction record describes what a player may do and what indicates permission or state. A shiny surface may be decoration, an interface, or a hazard under different contracts. Neither physical plausibility nor a stock material name supplies that contract. Test material distinctions under the actual scene lighting, not only a studio preview. This is a proposed design inference, not a claim about universal gloss perception. [C-08]

### Information access can constrain, but need not homogenize, style

XAG 103 recommends additional channels for important cues; XAG 117 distinguishes configurable visual distraction from essential gameplay. These are vendor guidelines, not standards certifying this entry or its future application. [C-06, C-12]

Our inference is to decide which information is essential before deciding which art can carry it alone. An optional mysterious surface can remain ambiguous; a mandatory decision should not require access to a decorative distinction that the intended player cannot perceive. Offer a task-appropriate alternative without assuming the alternative produces the same aesthetic or emotional experience. Style can remain varied while the required facts remain available. [C-07, C-09]

### Recent creator accounts broaden, but do not validate, the comparison

In a 2026 interview, Play by Play describes combining stylized marks with more lifelike surface treatment. A 2025 Game Kitchen account describes low-resolution palette/detail constraints, level separation and deliberately contrasting characters. These add distinct production contexts; claimed character qualities remain the creators’ intentions, not measured audience interpretations or a universal color/personality code. [C-15]

## Design choices and alternatives

All recommendations below are conditional inferences or hypotheses, not measured rankings. [C-07–C-11]

| Choice | When it is worth considering | Tradeoff and serious alternative |
|---|---|---|
| Broad stylistic cohesion | Many contributors or repeated asset families need a shared visual relationship. Specify representative examples and exceptions. | Uniformity can blur roles or discourage useful contrast. A smaller set of role-specific constraints may be sufficient. |
| Deliberate role contrast | Identity, direction, interactability or state distinctions are consequential. Preserve the discriminating feature across variants. | Contrast can reveal something meant to be discovered or dominate the scene. Use a contextual cue, voluntary highlight or inspect action instead of permanent exaggeration. |
| Material-led distinction | Surface behavior is relevant and can remain interpretable in the intended lighting and views. | Reflection, wear and lighting may compete with the intended meaning. Use shape, position or explicit information when material behavior alone is insufficient. |
| Stylized geometry with physically based surfaces | The desired combination benefits from controlled shape and a consistent lighting response. | It still requires art direction and in-context evaluation; neither “PBR” nor “stylized” determines quality or cost. Simpler flat or authored shading may serve the task. |
| High-detail naturalistic presentation | Close observation of surfaces or performance is part of the intended experience, with production capacity to support it. | Additional detail may be unnoticed, distracting or inconsistent across assets. Author detail selectively rather than applying a universal fidelity target. |
| Distinct environmental and character treatments | Separation is intentional: inhabitants, artifacts or regions should not all read as identical. Specify what still connects them. | The mismatch may look accidental or obscure the actor. Rebalance lighting, silhouette or detail rather than repaint everything to one palette. |
| Less differentiation | Deliberate ambiguity, restoration, or appreciation is the scene’s goal, and no required task fact is withheld. | Later task changes can invalidate the choice. An explicit inspect/assist route is a simpler contingency than redesigning the whole style. |

## Application process

The following is a proposed sequence, not work performed on assets. [C-07–C-13]

1. **Diagnose the decision.** Write the player question and what remains intentionally unknown. Distinguish “find the service terminal” from “know whether it is currently available,” and both from “like its appearance.” List evidence that the present problem is visual rather than a misleading rule, camera occlusion or input failure.
2. **Choose the smallest useful style contract.** Specify role-bearing features, variable features and explicit exceptions for environments, characters, props, interface and effects. Include examples of a permitted contrast and an impermissible false implication. Do not require a fixed number of shape, color or material families.
3. **Compare candidate treatments.** Compare coherent uniformity, selective contrast and an explicit/optional information alternative. Keep task rules and information content comparable. Record what cannot be matched, such as a larger silhouette necessarily occupying more screen area.
4. **Plan in-context checks before final asset production.** Include intended camera views, motion and representative background/lighting combinations. Test large and small presentation contexts separately rather than translating a display setting into a universal size rule. Keep P03 decisions pending where needed.
5. **Evaluate recognition, state inference, action and preference separately.** Include unfamiliar examples and cases with different correct answers. A person who recognizes a pattern but chooses not to act has not necessarily misunderstood it.
6. **Revise or stop.** Retain only the constraints that serve the stated purpose at an acceptable cost. Simplify or use a different information channel if a decorative distinction repeatedly carries an essential fact badly. Escalate a conflict with deliberate ambiguity to the relevant design owner rather than silently revealing everything.

Production planning should track **kinds of work**, not unsupported cost multipliers: reference and exception maintenance, asset variants, lighting/material review, rig and silhouette changes, effect interaction, localization/access variants, regression checks and approval ownership. A sophisticated style system can cost more to maintain than a small set of direct examples; its value is a hypothesis to examine against rework. [C-10]

## Patterns and genre adaptations

[Role-preserving style variation — GDR-CAND-20261010-P04-PAT-01](../patterns/role-preserving-style-variation.md) operationalizes the style contract, variant review and stop conditions. It is a candidate inference, not independent support for this topic. The [animation topic](animation-and-performance.md) owns temporal identity, posing and interruption, where static art cannot carry the whole distinction.

No genre files are created or assumed. A discovery-focused scene, a time-sensitive selection task and a contemplative space can require different amounts of explicitness without one genre label winning automatically. These are illustrative task contrasts, not researched audience promises for genres. Additional material/display continuity work is queued in the [child-work record](../reviews/full-run-20261010-p04-review-packet.md#child-extension-queue). [C-11, C-13]

## Examples and counterexamples

### Creator-reported examples, not observed gameplay

The TF2 paper is a bounded example of cohesion coexisting with contrasting environmental treatments. Riot supplies a useful countercase to relying on static outline alone: its account identifies an animation-dependent identity exception for Lee Sin. Neither source was used to infer player results from commercial success. [C-02, C-03]

Riot also reports a historical Taliyah/background mismatch and a Jhin boundary-visibility problem. These show what that team identified as problems, not an independent severity estimate, a current-build defect or a universal prescription for brighter effects. [C-03]

### Illustrative worked example — a shared maintenance workshop

**Invented for this entry; no asset, prototype or test exists.** The player must identify a service cabinet, learn whether it is available, and decide whether to use it. Several artisans’ cabinets intentionally have different finishes. The proposed invariant is a recognizable service-facing arrangement and accessible status presentation; finish, wear and ornament may vary. The cabinet’s name or ownership need not predict its current availability. [C-07, C-08, C-13]

A first design paints every available cabinet blue. A second preserves a service-facing shape with a distinct available/unavailable state indication; color remains an optional reinforcement. A third uses a player-invoked inspect route. A decorative cabinet shares the workshop’s material vocabulary but lacks the service arrangement. This deliberate contrast avoids defining “same material” as “same function.” The selection contract and actual cabinet states stay unchanged between comparisons. [C-07, C-13]

A discriminating transfer check presents **both** an unfamiliar available service cabinet and a familiar-looking unavailable cabinet, then a decorative example whose finish resembles the usable one. Ask separately what each object is, whether it is available, and whether the player wishes to use it. Repeating three trials where “use” is always correct would not discriminate understanding from a repeated response. This preserves the inspected F01 transfer-example correction without importing its numerical example as an art rule. [C-13]

### Strong counterexample — discovering rather than receiving a classification

An investigation may intentionally ask players to determine whether an object is functional from accumulated evidence. Giving every functional object an immediately recognizable service mark would remove the intended inference. Keep the role-preserving pattern out of that discovery layer; apply it only to already-known task facts or an explicitly offered assistance route. The test must assess whether assistance changes the promised challenge, not describe all obscurity as bad art. [C-07, C-11, C-13]

## Failure modes and constraints

| Warning sign to investigate | Competing explanation | Proposed response |
|---|---|---|
| A variant is admired but misidentified. | Appeal and identity are different; novelty or exposure may confound recognition. | Restore the task-bearing distinction or use explicit information; do not interpret liking as a successful task result. |
| A still silhouette passes but a moving actor fails. | Pose, costume, overlap or background changes the presented shape. | Review the action sequence and actual view with Animation/P03 owners. |
| “Usable” is inferred from gloss or color alone. | Decorative styling unintentionally became a permission rule. | Separate role, state and surface vocabulary; include contradictory-looking negative cases. |
| A low-distraction mode removes a required state. | The required fact was embedded only in decoration. | Preserve usable information through an appropriate alternative; evaluate actual access users. |
| All scenes become high-contrast noise. | Every contributor treated local salience as the highest priority. | Revisit the scene’s task hierarchy and reduce optional emphasis. |
| One reference image produces inconsistent assets. | Important permissible variations and exceptions were never specified. | Add targeted examples/owners, not a larger unsourced style bible by default. |
| An access overlay trivializes a legitimate inference. | Assistance changed information, not just presentation. | Make the changed contract explicit and review it; never hide essential information solely to preserve one sensory experience. |

These are prospective diagnoses, not findings from a P04 playtest. [C-07–C-13]

**Ethics and localization:** avoid presenting body shape, complexion, disability markers, accent-associated costume or a color as reliable evidence of morality or personality. The inspected sources do not establish such mappings. Evaluate intended meanings with relevant audiences and distinguish cultural familiarity from task learning. Review reference provenance and permitted use before asset production; this research grants no asset rights or production approval. These are proposed risk controls, not legal conclusions or a completed cultural review. [C-10, C-11, C-14]

## Playtest and validation

**PROPOSED — NOT PERFORMED.** No participants, art variants, perceptual simulations, rendered scenes or performance benchmarks were produced. This protocol is a hypothesis-led plan requiring separate authorization. [C-13, C-14]

**Question:** Does selective preservation of role-bearing features help unfamiliar variants remain correctly interpretable without undermining intended discovery, preference, comfort or production feasibility?

**Comparison:** A uses uniform appearance; B uses selective role-preserving variation; C uses greater stylistic freedom with a contextual information alternative. A/B can test variation more directly; C is a decision alternative, not a pure feature ablation. Match tasks, object availability, view, input, opportunity to inspect and exposure. Record remaining differences in size, lighting, backgrounds and assistance.

**Participants and context:** recruit only after an approved protocol defines the actual audience. Include unfamiliar and experienced users, relevant vision/access needs and relevant language/cultural backgrounds; do not treat simulated impairment or an expert artist’s inspection as representative user evidence. Use participants’ chosen settings and ordinary device arrangements. A later study owner must justify sample size from the intended estimation precision, pilot variability and resources; no sample-size guarantee is supplied here.

**Procedure and measures:** counterbalance treatment order and asset-to-treatment assignments where feasible. Teach a common task, then test novel instances and matched positive/negative states with different correct responses. Record identity classification, state understanding, action reasons, completion/errors, help use and confusion. Collect aesthetic preference, perceived cohesion, comfort and intended-emotion reports separately. Include repeated exposure and a later unfamiliar family; immediate familiarity is not durable transfer. Log authoring/revision effort separately rather than inferring savings from player speed.

**Disconfirmation:** reject the stronger “preserves understanding” claim when B’s role or state errors exceed a predeclared project-relevant tolerance, when success depends only on repeated answer patterns, or when its effect disappears on genuinely new examples. Prefer the simpler option when the evidence is inconclusive and the added contract has no demonstrated local value; inconclusive evidence is not equivalence. A critical information failure blocks that candidate’s advancement pending correction, even if average liking is high. Retain deliberate ambiguity only where it is the approved task rather than an accidental access barrier. Define tolerances and analysis before data collection; no numbers or thresholds here have been adopted by the studio.

## Claim ledger

Confidence concerns the exact scoped wording, not source prestige. References support only the described link; an inference or proposed test is not converted into an empirical result.

### C-01
**Claim:** Style, cohesion, material language and task readability are useful separate analytic dimensions for this draft. **Class:** `inference`. **Support:** original synthesis; inspected P01 Visual communication §§Decision/Core explanation and Interface and information information-contract passage, recorded in the packet. **Confidence:** moderate for conceptual separation; usefulness not measured. **Applicability:** genre-neutral design analysis. **Unresolved:** whether a later project needs different terminology.

### C-02
**Claim:** Valve describes an internally controlled art language with deliberately contrasting team-world treatments. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P01-13, §§3–4.3, PDF pp. 2–3. **Confidence:** high for attribution, not efficacy. **Limit:** one production, no comparison of player outcomes. **Unresolved:** which relationships transfer usefully.

### C-03
**Claim:** Riot’s clarity account preserves identity across variation, gives an animation-dependent silhouette exception, and reports contextual clarity failures. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P04-001, Silhouettes; Changes From Development; Maps; Transformations; Cosmetic Animations. **Confidence:** high for the reported cases. **Limit:** historical creator account; no current-build observation. **Unresolved:** audience-specific effects and causal contribution of each fix.

### C-04
**Claim:** The inspected render-style experiments do not support a simple “more realism means less appeal” ranking for their tested stimuli. **Class:** `empirical-evidence`. **Support:** GDR-SRC-20261010-P04-002, §5.1 and §8; methods and limits described above. **Confidence:** moderate, narrow controlled comparisons with lighting limits. **Outcome uncertainty:** no game-level effect estimate or general equivalence established. **Unresolved:** other geometry, emotional performance, environments and audiences.

### C-05
**Claim:** Epic documents physically based material controls separately from a photorealistic-only art goal. **Class:** `practitioner-heuristic` (official technical documentation). **Support:** GDR-SRC-20261010-P04-003, introductory and material-attribute sections. **Confidence:** high for document scope. **Limit:** no proof of aesthetic quality or task recognition. **Unresolved:** suitability under a particular approved pipeline.

### C-06
**Claim:** Important information needs appropriate additional-channel consideration, not merely a second visual distinction. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P01-05, Implementation guidelines; freshly inspected. **Confidence:** high for attribution; local usability unknown. **Limit:** vendor guidance, not formal certification or emotion-equivalence evidence. **Unresolved:** usable alternatives for the actual task.

### C-07
**Claim:** Preserve task-bearing relationships while allowing deliberate stylistic exceptions; compare this with uniformity and explicit assistance. **Class:** `inference`. **Support:** C-02/C-03/C-06; the causal bridge is spelled out in Core explanation. **Confidence:** moderate as a decision method, low for any promised local benefit. **Counterpressure:** deliberate discovery may depend on ambiguity. **Unresolved:** which features carry role/state information and when variation is worth its cost.

### C-08
**Claim:** A rendered surface description should not silently become an interaction-permission rule. **Class:** `inference`. **Support:** C-05 and the task/role distinction in C-01; not an empirical material-perception result. **Confidence:** moderate as a consistency check. **Limit:** a game may deliberately teach such a rule. **Unresolved:** how reliably the chosen material/state relationship can be learned and perceived.

### C-09
**Claim:** Evaluate actual view, display, motion and access context before transferring a style decision; do not substitute text/target standards for world-art thresholds. **Class:** `inference`. **Support:** inspected P01 correction receipt and C-03/C-06/C-12. **Confidence:** moderate; no new device experiment. **Limit:** P03 candidates remain unavailable. **Unresolved:** view-dependent failures and context-specific acceptance criteria.

### C-10
**Claim:** A style system requires ownership of variants, exceptions and review work; its cost or savings cannot be inferred from a style label. **Class:** `inference`. **Support:** C-02/C-03 plus original production-work decomposition. **Confidence:** moderate for work categories, low for unmeasured magnitude. **Limit:** no staffing, asset-count or budget estimate. **Unresolved:** marginal authoring/rework cost and provenance review.

### C-11
**Claim:** Meaning, preference and intended mood may vary by audience, context and familiarity; visual difference does not prove personality or moral character. **Class:** `hypothesis` for the proposed local interpretation comparisons. **Support:** adjacent C-04, inspected W01 characterization distinction, and original countercases. **Confidence:** low for any specific cultural or player response. **Limit:** no cross-cultural or representation study inspected here. **Unresolved:** relevant populations and misinterpretations.

### C-12
**Claim:** XAG 117 recommends controls for specified visual distraction/motion while retaining essential-gameplay exceptions. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P01-10, Implementation guidelines. **Confidence:** high for attribution. **Limit:** no blanket animation-removal rule or safe numerical setting. **Unresolved:** which particular effects are optional and how alternatives work.

### C-13
**Claim:** The process, workshop example, proposed test and rejection criteria are unvalidated local research proposals. **Class:** `hypothesis`. **Support:** original P04 synthesis; F01 selected pattern’s transfer-discrimination correction is an inspected design constraint, not a completed art test. **Confidence:** low for eventual effectiveness. **Limit:** NOT PERFORMED; no fixed sample, metric guarantee or adopted tolerance. **Unresolved:** authorized protocol, feasibility and measurement sensitivity.

### C-14
**Claim:** Doug authorized this bounded public-source P04 research and draft artifacts, not implementation, participant work or release. **Class:** `studio-decision`. **Owner/date:** Doug, supplied P04 dispatch, 2026-10-10, Authorization Update and Assigned Outputs. **Confidence:** high for explicit scope. **Limit:** candidate identities remain temporary; approval fields null. **Unresolved:** independent content review, coordination and later decisions.

### C-15
**Claim:** Recent creator accounts describe mixed stylization/realism and selective cohesion/contrast under different production constraints. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P04-011, stylized-likeness answer; P04-012, Campos/Lozano art paragraphs. **Confidence:** high for attribution. **Limit:** promotional accounts, not controlled efficacy, savings or interpretation data; no footage inspected. **Unresolved:** local value and transfer beyond the reported productions.

## References

All records below were inspected in relevant passages on 2026-10-10. Source IDs retained from P01 are explicit reuse, not new allocations. New P04 IDs are temporary; central URL/DOI/edition reconciliation remains pending. Document copies and candidate citations do not provide independent corroboration.

### GDR-SRC-20261010-P01-13

**Jason Mitchell, Moby Francke and Dhabih Eng. [Illustrative Rendering in Team Fortress 2](https://cdn.cloudflare.steamstatic.com/apps/valve/2007/NPAR07_IllustrativeRenderingInTeamFortress2.pdf).** Valve / NPAR 2007. Date: 2007; exact publication day unknown. Edition/build: 2007 paper; described game build unspecified.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand production/technical paper. **Locators:** §§3, 4.1–4.3; PDF pp. 2–3, Figures 2–5. **Supports:** C-02; indirect C-07/C-10.

**Limits:** One production account, not a player experiment. PDF figures inspected, not game footage. **Relationship:** Same work as P01-13; former steamcdn-a.akamaihd.net route is a host alias, not corroboration. **Rights:** Reuse permission not established; paraphrase only; figures not redistributed.

### GDR-SRC-20261010-P04-001

**bananaband1t / Riot Games. [Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/).** Riot Games. Date: 2021-03-12. Edition/build: Developer article; example build numbers unspecified.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand development account. **Locators:** The Unbreakable Vows; Silhouettes; Abilities; Filling Up Buckets; Changes From Development (Jhin); Maps (Taliyah); Transformations (Leona); Cosmetic Animations (Renekton). **Supports:** C-03; indirect C-07/C-09.

**Limits:** Creator-reported practices and problems; no footage watched or controlled outcome data. **Relationship:** Independent production from Valve; retrospective selection and issuer incentives remain. **Rights:** Reuse license not established; paraphrase only.

### GDR-SRC-20261010-P04-002

**Rachel McDonnell, Martin Breidt and Heinrich H. Bülthoff. [Render me Real? Investigating the Effect of Render Style on the Perception of Animated Virtual Humans](https://www.scss.tcd.ie/Rachel.McDonnell/papers/Siggraph2012a.pdf).** ACM Transactions on Graphics 31(4), Article 91. Date: 2012-07. Edition/build: SIGGRAPH 2012 version of record; DOI 10.1145/2185520.2185587.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Original human perception experiments. **Locators:** §5.1, PDF pp. 4–6 / printed 91:4–91:6; §§7–8, PDF p. 10 / 91:10. **Supports:** C-04; adjacent C-11 only.

**Limits:** Selected rendered humans, not a game-style trial; lighting not fully controlled and emotional-content limitation acknowledged. Figures/text inspected on PDF pp. 5 and 10. **Relationship:** Separate study from Normoyle/Jörg; shared research area is not replication. **Rights:** ACM copyright notice; paraphrase only; no figures redistributed.

### GDR-SRC-20261010-P04-003

**Epic Games. [Physically Based Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine).** Epic Developer Community. Date: Publication/update date unknown; live page checked 2026-10-10. Edition/build: Unreal Engine 5.8 documentation, displayed edition.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official technical documentation. **Locators:** What Does Physically Based Mean?; PBR Material Attributes; Roughness; Mapping Roughness; Roughness vs. Specular. **Supports:** C-05; design inference C-08.

**Limits:** Documented material model, not a readability experiment or tested local implementation; numeric defaults not recommended here. **Relationship:** Same issuer as the other Epic records; distinct documents, not independent efficacy evidence. **Rights:** Reuse license not inspected; paraphrase only.

### GDR-SRC-20261010-P01-05

**Microsoft. [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103).** Microsoft Learn. Date: Last updated 2026-03-04. Edition/build: Unnumbered live page revision checked 2026-10-10.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance. **Locators:** Goal; Implementation guidelines; Visual cues; Color and additional sensory channels. **Supports:** C-06; indirect C-07/C-09.

**Limits:** Guidance, not a formal standard, compliance certificate or evidence of emotional equivalence. **Relationship:** Reuses inspected P01-05; P02-005 duplicates this URL. Central deduplication pending. **Rights:** Reuse license not inspected; paraphrase only.

### GDR-SRC-20261010-P01-10

**Microsoft. [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117).** Microsoft Learn. Date: Last updated 2026-03-04. Edition/build: Unnumbered live page revision checked 2026-10-10.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance. **Locators:** Overview; Implementation guidelines; Moving/blinking/scrolling content and essential-gameplay exceptions; Camera movement options. **Supports:** C-12; indirect C-09.

**Limits:** No safe-motion numerical threshold or blanket removal of all gameplay animation; not certification. **Relationship:** Reuses P01-10; P02-010 duplicates this URL. Same issuer as XAG 103, not independent player evidence. **Rights:** Reuse license not inspected; paraphrase only.

### GDR-SRC-20261010-P04-011

**Bryan Johnston and Mike Laygo / Play by Play Studios; interviewer unspecified. [Built with UE5, NBA THE RUN looks to bring back the golden age of basketball video games](https://www.unrealengine.com/developer-interviews/built-with-ue5-nba-the-run-looks-to-bring-back-the-golden-age-of-basketball-video-games).** Epic Games, Unreal Engine developer interviews. Date: 2026-05-28. Edition/build: Pre-open-beta creator interview; Unreal Engine 5, minor/build unspecified.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand creator interview. **Locators:** Questions about stylized likeness and character animation; Johnston/Laygo answers, web extraction lines 57–67. **Supports:** C-15, style portion only.

**Limits:** Design intentions and reported reuse, not measured responsiveness, audience response, savings or a current release-status claim. **Relationship:** Separate production from Valve/Riot/Naughty Dog; hosted by its engine vendor, with promotional incentives. **Rights:** Reuse license not established; paraphrase only; no media redistributed.

### GDR-SRC-20261010-P04-012

**David Jaumandreu; accounts by Jesús Campos and María Lozano / The Game Kitchen. [A behind-the-scenes look at Ninja Gaiden: Ragebound’s art direction](https://blog.playstation.com/?p=407986).** PlayStation.Blog. Date: 2025-07-24. Edition/build: Pre-release developer account; described console build unspecified.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand production account. **Locators:** Campos palette, low-resolution and level-readability paragraphs; Lozano silhouette/character-contrast paragraphs, web extraction lines 63–71. **Supports:** C-15, intent/constraints only.

**Limits:** Intent, production decisions and subjective character descriptions; not measured player interpretation or a universal color/personality mapping. **Relationship:** Separate 2D production from other cases; publisher-hosted promotional selection remains. **Rights:** Copyright notice; paraphrase only; no art/media redistributed.

## Open questions and change history

### Coverage remains open

| Subtopic | Inspected coverage | Next discriminating question |
|---|---|---|
| Style systems, selective cohesion and deliberate contrast | Creator accounts across historic 3D, recent 3D and 2D production; conditional synthesis. | Which relationships actually carry role/state meaning on unfamiliar examples? |
| Value/color/detail/silhouette | Firsthand constraints and negative cases; access guidance. | Does a distinction survive actual motion, lighting and supported access settings? |
| Material language | Current PBR documentation; semantics-versus-surface distinction. | When does intended material meaning fail across scenes or display conditions? |
| Environment/character cohesion | Reported coordinated and contrasting treatments. | Can a deliberate mismatch remain comprehensible without removing the intended ambiguity? |
| Stylization/realism and audience response | One narrow rendered-human experimental family. | Do results transfer to varied geometry, environments, emotional performances and target audiences? |
| Device/access/localization | Scoped vendor guidance and design questions; no P03 bytes, no new user data. | What context changes require a different presentation rather than a translated numerical setting? |
| Production constraints | Work categories and creator accounts; no measured cost model. | Does a maintained style contract reduce rework enough to justify its overhead? |

Contradiction records P04-CON-01/02/05/06 and child-work rows are in the review packet. These are batch-local records, not global CON allocations. All tests remain proposed. The bounds of two research topics and two patterns are fulfilled; comprehensive heading coverage is not certified.

**History:** 2026-10-10, first P04 submission, version 0.1.0 / initial-draft-1. No predecessor or superseded artifact. The later creator-source check added C-15 without renumbering earlier claims. The same author performed the self-review; independent P04 review and Gate C acceptance remain pending. Local document checks do not pass Gate D host retrieval. Gate E, release and game adoption remain unapproved. See the [exact review packet](../reviews/full-run-20261010-p04-review-packet.md).

## Selected Origin B independent review — 2026-10-11

Candidate revision review-correction-1 derives solely from the Origin B initial-draft-1 bytes identified by predecessor_sha256. Parent-verified final response selects B; see the accompanying PROVENANCE_RECEIPT.md and variant-map.json. Origin A is a preserved earlier author variant with colliding IDs/source bindings, not an alternative source of guidance for this file. No A passages or source bindings were imported. Corrected Riot section locators to actual headings; underlying claims unchanged. Scoped NBA interview status to pre-open-beta; no inference about earlier closed testing. Author-session statements above concerning unavailable P03 or unperformed independent review remain historical: this reviewer has reviewed P03 correction-1. That context supplies no validated art/animation efficacy or universal camera/display setting. Other missing dependencies, live global allocations and actual-host tests remain unresolved unless separately verified. Version0.1.0, draft and null approval metadata are retained; formal acceptance, host/player/engine tests and release are not claimed.

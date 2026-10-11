# Preserved GDR-CAND-20261010-P04-TOP-01-comparison.diff

Original payload SHA-256: `0e9dca3c222f8498bbcf281c95991f22dd818ccbd734b8cbbd46f3cac759b3bf`. Complete original record follows in Markdown.

```text
--- earlier/art-direction.md
+++ later/art-direction.md
@@ -9,359 +9,311 @@
 run_id: GDR-FULL-20261010
 batch_id: P04
 attempt_id: P04-authoring-01
-updated: '2026-10-11'
-evidence_checked: '2026-10-11'
-date_basis: UTC; run identifier retains dispatch date 2026-10-10
-identity_scope: run-scoped candidate; permanent allocation pending
-predecessor_sha256: null
-supersedes: null
-change_summary: Initial P04 candidate; no predecessor submitted.
+identity_scope: temporary-run-scoped
+updated: '2026-10-10'
+evidence_checked: '2026-10-10'
 aliases:
 - visual style system
-- art-style cohesion
 - material language
+- environment and character cohesion
 tags:
 - art-direction
 - style
-- recognition
 - material-language
+- readability
 - production
-- accessibility
+- conditional-guidance
 related_topics:
 - GDR-CAND-20261010-P04-TOP-02
 - GDR-CAND-20261010-P01-TOP-01
+- GDR-CAND-20261010-P01-TOP-03
 related_patterns:
 - GDR-CAND-20261010-P04-PAT-01
-- GDR-CAND-20261010-P04-PAT-02
 related_genres: []
 source_ids:
+- GDR-SRC-20261010-P01-13
 - GDR-SRC-20261010-P04-001
 - GDR-SRC-20261010-P04-002
 - GDR-SRC-20261010-P04-003
-- GDR-SRC-20261010-P04-004
-- GDR-SRC-20261010-P04-010
+- GDR-SRC-20261010-P01-05
+- GDR-SRC-20261010-P01-10
 - GDR-SRC-20261010-P04-011
+- GDR-SRC-20261010-P04-012
 reviewer: null
 approved_by: null
 approved_date: null
+predecessor_sha256: null
+supersedes: null
+change_summary: Initial P04 submission; does not replace or resend any previous batch.
+byte_hash_record: ../reviews/full-run-20261010-p04-integrity-receipt.md
 ---
 
 # Art direction
 
-**Draft 0.1.0, initial-draft-1 — coverage open, not released guidance.** This entry helps choose and maintain a visual system. It does not establish that one style is best, that realism predicts appeal, or that a coherent-looking asset is readable in play. Findings, design inferences and untested proposals are separated below. [C-01, C-05, C-13, C-14]
+**Draft 0.1.0; candidate revision initial-draft-1. Not released, independently reviewed for P04, or approved for a game.** This entry helps choose a visual system, not a universal aesthetic. Its strongest recommendation is an **inference**: preserve the distinctions needed for the current task while allowing deliberate stylistic variation. Whether that improves a particular game remains to be tested. [C-07]
 
 ## Decision and scope
 
-**Decision:** Which visual relationships should remain consistent across characters, environments and variants, which should deliberately contrast, and what production effort is warranted to maintain those choices at the player’s actual decision point?
-
-Included: style systems; value, color, material and silhouette language; character/environment cohesion; selective contrast; stylization and realism; audience and viewing differences; and production constraints. Excluded: a rendering implementation, complete color science, asset creation, scene-specific canon, a camera specification, genre rules, certification and commercial-success explanations. P01 owns general visual communication and information access; this topic owns how artistic choices are selected, varied and maintained across content. [C-01, C-10, C-14]
-
-### Working vocabulary
-
-The following are analytic conventions for this draft, not formal standards. [C-01, C-13]
-
-| Term | Working meaning | Decision consequence |
-| --- | --- | --- |
-| Style system | Chosen relationships among form, detail, palette, surface depiction, light and movement. | Record what may change together and what needs another review. A mood board alone does not specify this. |
-| Cohesion | Content appears to belong to a deliberately related visual world. | Related does not mean identical; different roles may need different treatments. |
-| Selective contrast | Intentional difference within or against the system. | State whether it identifies an action, identity, location, exception or merely an aesthetic emphasis. |
-| Material language | How surface qualities and construction suggest substance, use and history. | Roughness, polish, wear, pattern and shape are candidate visual variables, not automatically reliable gameplay meanings. |
-| Silhouette | Projected outline and its relation to pose, accessories and view. | A recognizable concept-sheet outline does not guarantee recognition when turned, occluded or animated. |
-| Stylization / realism | Dimensions of selection, simplification and resemblance, rather than opposite quality scores. | Geometry, texture, lighting and motion may occupy different positions; examine their combination. |
-| Affordance cue | A presentation feature that a player may interpret as supporting an action. | An intended cue is not proof of recognition, correct interpretation or actual permission. |
-
-### Context assumptions to declare
-
-The abstract guidance is platform-neutral. A later comparison should identify the task, intended experience, view and distance range, display/window scale, lighting and visual effects, input method, language, prior familiarity and access settings. A reversible starting scope for the proposed tests is flat-display interaction using a participant’s familiar input; this is not validation for VR, handhelds, couch play or every visual-access profile. P03 camera/platform candidates were not available for transfer. No numerical screen, brightness, text or target-size recommendation is imported. [C-10, C-12, C-13]
+**Decision:** Which relationships among shape, value, color, surface response, detail, environment, character and motion should remain consistent, and where is contrast worth its interpretive and production cost?
+
+The core is genre-neutral. It includes style systems, silhouette and role recognition, material language, environment/character cohesion, audience and display assumptions, production constraints and accessible presentation. It excludes creating assets, selecting a studio’s commercial art package, certifying accessibility, defining character morality from appearance, and selecting a camera or rendering pipeline. This is research advice, not implementation authorization. [C-01, C-14]
+
+**Working terms, not a formal standard:** a *style system* is a set of intended relationships and permissible exceptions, rather than a mood board alone. *Cohesion* means that elements can be read as belonging to an intended whole; it need not mean visual uniformity. *Material language* includes both rendered surface behavior and the meanings a game asks players to associate with surfaces. *Readability* must name a task: identifying an actor, distinguishing usable from decorative equipment, estimating an action boundary, or understanding a state. Aesthetic preference, recognition and correct action are separate outcomes. [C-01]
+
+### Inspected dependencies and boundaries
+
+The parent-selected waves 1–2 archive was materialized, hashed and inspected before these distinctions were transferred. P01 Visual communication, Interface and information, and Accessibility and inclusive interaction were read as `review-correction-1`; P02 Controls and input, Feedback and game feel, and Multimodal communication were also read as `review-correction-1`. Their ownership is preserved: P04 owns the **style system and its production variation**, not a replacement general hierarchy, input, or redundant-cue topic. Exact paths, hashes and passage ranges are in the [dependency record](../reviews/full-run-20261010-p04-review-packet.md#inspected-dependency-transfers).
+
+P01’s corrected distinction among **CSS pixels, rendered text body height, formal web conformance and vendor guidance** is retained. No text-size, contrast, target-size or motion threshold is copied into this entry. The original standards would need their own applicability check before a numerical requirement was adopted. Two visual distinctions do not become two sensory channels. The unresolved P01/P02 cue-pattern overlap remains unresolved. [C-06, C-09]
+
+**Application assumptions to declare:** intended task and viewing distance; camera views and actor size on the actual display; input and selection method; illumination and visual clutter; languages; relevant vision, motion and cognitive access needs; assistance settings; asset/rig/material budget and update cadence. No desktop, headset, touch device, art asset vendor or particular game is the default. P03 Camera and framing and Platform and display context, and F04 Combat and conflict systems / Movement and traversal, were not supplied as inspectable candidate bytes here. Thus this draft does not inherit their decisions or numerical settings. [C-09]
 
 ## Core explanation and mechanisms
 
-### Cohesion is a relationship, not uniformity
-
-Two objects can share construction logic while needing different visual priority. Conversely, two factions can differ deliberately without making every prop a competing focal point. The creator precedent is C-02; the proposed application is to name a small set of relationships that matter to the particular decision, then allow expressive differences elsewhere. It does not follow that every game needs faction colors, a universal shape code or a fixed number of palette entries. [C-01, C-02, C-08]
-
-**Proposed mechanism:** an interpretable family resemblance supports a useful expectation → a relevant difference identifies the exception → the player chooses appropriately → the desired aesthetic response may also occur. Creator accounts support the production intention, but this full causal chain is not established by the inspected corpus. Players may instead notice the wrong feature, rely on a label, learn an unintended mapping or simply enjoy the composition without decoding it. [C-03, C-08, C-09, C-12]
-
-### Preserve the decision relationship, not every feature
-
-A costume change, new environment treatment or altered idle pose can change a familiar visual read. The useful question is not “Did we retain the approved number of features?” It is “Can the player still make the distinctions this situation legitimately requires?” The contrast between Riot’s recognizability goal and its context-specific ponytail exceptions motivates this narrower formulation; it does not prove the proposed workflow. A feature can be stable in one family and intentionally absent in another. [C-03, C-04, C-08]
-
-The burden of evidence also changes with the task. Immediate recognition might be essential for selecting a teammate but inappropriate for a disguised figure whose identity is intentionally unresolved. In that case, preserve access to legitimate action information without prematurely revealing the hidden identity. This is an illustrative boundary, not a genre rule. [C-08, C-13]
-
-### Material appearance is not an action contract
-
-A polished handle, cracked wall or luminous surface may suggest use; it may also be decoration. Art direction should declare whether a treatment identifies substance, condition, interaction, affiliation or no gameplay category at all. Where treatment predicts action, compare both valid and invalid instances and examine what happens when wear, wetness, lighting or distance changes the appearance. This is a proposed discrimination test, not a claim that a particular material always carries a particular meaning. [C-09, C-13]
-
-Do not settle ambiguity by turning every usable object into the brightest object. That can be an appropriate explicit mode, but it changes the composition and can communicate more than intended. Alternatives include geometry, framing, animation, a label or on-demand assistance; whether any one is sufficient remains a P01/P02-informed access and comprehension question. [C-06, C-08–C-10]
-
-### Appeal, legibility and production effort are different outcomes
-
-The empirical boundary in C-05 challenges a simple realism ranking. It does not select a house style or prove stylization is cheaper. A treatment can be appealing but poor at distinguishing state; another can be efficient to author yet costly to revise across variants. Judge style fit, task accuracy, representational interpretation and production workload separately. Do not use sales, popularity, awards or a creator’s satisfaction as causal player evidence. [C-05, C-11, C-12]
+### Cohesion and contrast are not opposites
+
+Valve’s TF2 paper reports an intentionally controlled shape/texture system alongside contrasting team environments. Riot’s account prioritizes recognition across presentation changes and documents clarity failures. These are production rationales, not comparative evidence that one visual style causes better play. [C-02, C-03]
+
+**Evidence-to-application bridge:** where a game repeatedly asks the same distinction, accidental variation can create additional interpretations to check. Conversely, making all relevant objects look alike can erase the distinction. A useful starting hypothesis is therefore to preserve **role-bearing features**, while allowing variation in features that need not carry that role. The important feature may be outline, characteristic movement, placement, a labeled control, or a combination; it must be established through the task, not chosen from a universal shape dictionary. [C-07]
+
+The proposed causal chain is: a stable role-bearing relationship is perceivable → the player recognizes it across a new presentation → the player infers the correct current state → the available action becomes understandable. The inspected creator accounts support why this chain is worth testing, not each causal link. Recognition alone does not prove state comprehension; state comprehension does not require choosing the designer’s preferred action. [C-07, C-13]
+
+### Stylization, realism and appeal require separate questions
+
+McDonnell and colleagues’ explicit-rating experiments used separate groups of 17 for still images and movies of selected virtual-human render styles. Highly abstract and highly realistic examples were among the appealing styles; an intermediate style was especially poorly rated. Lighting was not fully controlled, and the authors identify the lack of emotional content as a limitation. This does **not** establish an optimal realism curve for games, environments or all audiences. [C-04]
+
+The design implication is to compare actual candidate combinations rather than rank the words “realistic” and “stylized.” Geometry, lighting, texture treatment, movement, expression and familiarity can change together. A preferred portrait is not proof of clearer gameplay, nor is an unfamiliar style necessarily a production mistake. Intended strangeness can be a valid artistic goal; the unresolved question is whether it interferes with the facts the player is supposed to understand. [C-07, C-11]
+
+### Physical surface behavior does not define gameplay meaning
+
+Epic’s physically based materials documentation separates base color, roughness, metallic and specular controls and explicitly includes non-photorealistic uses. It describes a shading model, not a rule for which objects should be actionable. [C-05]
+
+**Bridge:** define two different records. The visual record describes a surface’s rendering and intended variation; the interaction record describes what a player may do and what indicates permission or state. A shiny surface may be decoration, an interface, or a hazard under different contracts. Neither physical plausibility nor a stock material name supplies that contract. Test material distinctions under the actual scene lighting, not only a studio preview. This is a proposed design inference, not a claim about universal gloss perception. [C-08]
+
+### Information access can constrain, but need not homogenize, style
+
+XAG 103 recommends additional channels for important cues; XAG 117 distinguishes configurable visual distraction from essential gameplay. These are vendor guidelines, not standards certifying this entry or its future application. [C-06, C-12]
+
+Our inference is to decide which information is essential before deciding which art can carry it alone. An optional mysterious surface can remain ambiguous; a mandatory decision should not require access to a decorative distinction that the intended player cannot perceive. Offer a task-appropriate alternative without assuming the alternative produces the same aesthetic or emotional experience. Style can remain varied while the required facts remain available. [C-07, C-09]
+
+### Recent creator accounts broaden, but do not validate, the comparison
+
+In a 2026 interview, Play by Play describes combining stylized marks with more lifelike surface treatment. A 2025 Game Kitchen account describes low-resolution palette/detail constraints, level separation and deliberately contrasting characters. These add distinct production contexts; claimed character qualities remain the creators’ intentions, not measured audience interpretations or a universal color/personality code. [C-15]
 
 ## Design choices and alternatives
 
-These are conditional options derived from the evidence boundaries, not an experimentally established ordering. [C-08–C-13]
-
-| Choice | Appropriate decision context | Benefit sought, cost and alternative |
-| --- | --- | --- |
-| Shared form/material vocabulary | Many assets must feel related and maintenance matters. | May organize authoring and review; can erase useful distinctions or propagate a poor assumption. Start with a small representative family, not the whole content roster. |
-| Selective character/background contrast | A required subject is hard to distinguish in actual task views. | Can make priority deliberate; can undermine camouflage or make noninteractive decoration look usable. Compare against less detail or a contextual aid. |
-| Stable identity with variant expression | Several appearances represent the same role or entity. | Preserve required recognition while allowing novelty. Costs include mixed-view, animation, equipment and exception testing. A simple label may be preferable. |
-| Deliberate mismatch or discontinuity | The contrast itself carries an intended meaning, transformation or interpretive question. | Avoid treating all mismatch as failure. Required facts still need an accessible route; aesthetic confusion and task confusion are not interchangeable. |
-| More realistic depiction | The intended experience or available production pipeline calls for it. | Evaluate specific surfaces and motion rather than assuming a credibility bonus. The evidence does not establish a general appeal or cost advantage. |
-| Strong abstraction / sparse detail | Selection and omission suit the desired expression or production boundary. | Can remove useful distinctions as easily as clutter. Do not infer accessibility from low polygon count or limited colors. |
-| Minimal or no additional style rule | Existing content already supports the decision and intended experience. | Avoid unnecessary style bureaucracy. Retain an explicit record of exceptions that affect task meaning or access. |
+All recommendations below are conditional inferences or hypotheses, not measured rankings. [C-07–C-11]
+
+| Choice | When it is worth considering | Tradeoff and serious alternative |
+|---|---|---|
+| Broad stylistic cohesion | Many contributors or repeated asset families need a shared visual relationship. Specify representative examples and exceptions. | Uniformity can blur roles or discourage useful contrast. A smaller set of role-specific constraints may be sufficient. |
+| Deliberate role contrast | Identity, direction, interactability or state distinctions are consequential. Preserve the discriminating feature across variants. | Contrast can reveal something meant to be discovered or dominate the scene. Use a contextual cue, voluntary highlight or inspect action instead of permanent exaggeration. |
+| Material-led distinction | Surface behavior is relevant and can remain interpretable in the intended lighting and views. | Reflection, wear and lighting may compete with the intended meaning. Use shape, position or explicit information when material behavior alone is insufficient. |
+| Stylized geometry with physically based surfaces | The desired combination benefits from controlled shape and a consistent lighting response. | It still requires art direction and in-context evaluation; neither “PBR” nor “stylized” determines quality or cost. Simpler flat or authored shading may serve the task. |
+| High-detail naturalistic presentation | Close observation of surfaces or performance is part of the intended experience, with production capacity to support it. | Additional detail may be unnoticed, distracting or inconsistent across assets. Author detail selectively rather than applying a universal fidelity target. |
+| Distinct environmental and character treatments | Separation is intentional: inhabitants, artifacts or regions should not all read as identical. Specify what still connects them. | The mismatch may look accidental or obscure the actor. Rebalance lighting, silhouette or detail rather than repaint everything to one palette. |
+| Less differentiation | Deliberate ambiguity, restoration, or appreciation is the scene’s goal, and no required task fact is withheld. | Later task changes can invalidate the choice. An explicit inspect/assist route is a simpler contingency than redesigning the whole style. |
 
 ## Application process
 
-**Proposed process; no asset work or testing occurred.** [C-13]
-
-1. **Diagnose the decision failure.** Separate an unreadable target, misunderstood material, incoherent identity, unwanted emotional reading and unsustainable production demand. Record the player-facing consequence. “Needs polish” is not sufficiently discriminating.
-2. **Write a compact style contract.** State intended visual relationships, required identity/action distinctions, allowable ambiguity, permitted variation and examples that should be rejected. Name the decision owner for a later project; this draft does not appoint or approve one.
-3. **Choose a bounded representative set.** Include a character or focal object, a background family, a required interaction and a visually similar noninteraction. Include a deliberate exception. Select actual task views and access conditions rather than a beauty-render-only review.
-4. **Compare coherent alternatives.** Contrast uniform treatment, selective contrast and the existing presentation. Keep task rules, layout and assistance comparable. Do not improve geometry, lighting and labeling in only one condition and then attribute the result to a palette choice.
-5. **Specify variation and exception handling.** Record which combinations need review: costume/prop, pose, surface condition, lighting, detail reduction and language. Preserve meaning under the combination, not merely the isolated asset. An approved base asset is not approval of all descendants.
-6. **Evaluate interpretation before preference.** Ask what can be acted on and why before revealing correctness. Include cases in which the right answer changes. Ask about appeal and intended expression separately, with open-ended alternatives rather than forcing the director’s preferred adjective.
-7. **Revise, narrow or stop.** Keep only supported distinctions; remove constraints that add cost without demonstrated value. A failing material cue may warrant an explicit interaction aid rather than more elaborate surface work. Record access failures and unrepresented contexts rather than averaging them away.
-
-### Production and review record
-
-A later style dossier can contain a chosen relationship, its purpose, the relevant task views, permissible deviations, rejected examples, dependencies, rights/provenance notes and the evidence needed to revisit it. Track time spent creating, correcting and propagating variants separately; do not assume a reusable base reduces total labor in every case. Record a performance budget only after the actual platform/pipeline owner supplies one. This is a planning proposal, not an approved asset specification or a measured cost model. [C-10, C-11, C-13]
+The following is a proposed sequence, not work performed on assets. [C-07–C-13]
+
+1. **Diagnose the decision.** Write the player question and what remains intentionally unknown. Distinguish “find the service terminal” from “know whether it is currently available,” and both from “like its appearance.” List evidence that the present problem is visual rather than a misleading rule, camera occlusion or input failure.
+2. **Choose the smallest useful style contract.** Specify role-bearing features, variable features and explicit exceptions for environments, characters, props, interface and effects. Include examples of a permitted contrast and an impermissible false implication. Do not require a fixed number of shape, color or material families.
+3. **Compare candidate treatments.** Compare coherent uniformity, selective contrast and an explicit/optional information alternative. Keep task rules and information content comparable. Record what cannot be matched, such as a larger silhouette necessarily occupying more screen area.
+4. **Plan in-context checks before final asset production.** Include intended camera views, motion and representative background/lighting combinations. Test large and small presentation contexts separately rather than translating a display setting into a universal size rule. Keep P03 decisions pending where needed.
+5. **Evaluate recognition, state inference, action and preference separately.** Include unfamiliar examples and cases with different correct answers. A person who recognizes a pattern but chooses not to act has not necessarily misunderstood it.
+6. **Revise or stop.** Retain only the constraints that serve the stated purpose at an acceptable cost. Simplify or use a different information channel if a decorative distinction repeatedly carries an essential fact badly. Escalate a conflict with deliberate ambiguity to the relevant design owner rather than silently revealing everything.
+
+Production planning should track **kinds of work**, not unsupported cost multipliers: reference and exception maintenance, asset variants, lighting/material review, rig and silhouette changes, effect interaction, localization/access variants, regression checks and approval ownership. A sophisticated style system can cost more to maintain than a small set of direct examples; its value is a hypothesis to examine against rework. [C-10]
 
 ## Patterns and genre adaptations
 
-[Recognition-preserving style variation](../patterns/recognition-preserving-style-variation.md), `GDR-CAND-20261010-P04-PAT-01`, owns the repeatable variation-and-exception recipe. [Animation and performance](animation-and-performance.md) owns motion, interruption and expressive delivery; its [State-aligned animation handoff](../patterns/state-aligned-animation-handoff.md) is relevant when a style change alters poses or effects that communicate action state.
-
-Reviewed external dependencies are identified by exact IDs and hashes in the [P04 dependency record](../reviews/full-run-20261010-p04-review-packet.md#reviewed-dependency-transfer). They are not bundled again. P01/P02’s existing critical-cue patterns remain the owners of redundant and fact-preserving cue alternatives; this packet does not create another such pattern.
-
-No genre files are created or transferred. For a scene combining discovery and fast identification, specify which identities may remain hidden and which actions must be unambiguous; do not pick a winning genre label. Character motive and canon belong to W01’s character-design scope, not a material or silhouette rule. [C-08, C-12, C-13]
+[Role-preserving style variation — GDR-CAND-20261010-P04-PAT-01](../patterns/role-preserving-style-variation.md) operationalizes the style contract, variant review and stop conditions. It is a candidate inference, not independent support for this topic. The [animation topic](animation-and-performance.md) owns temporal identity, posing and interruption, where static art cannot carry the whole distinction.
+
+No genre files are created or assumed. A discovery-focused scene, a time-sensitive selection task and a contemplative space can require different amounts of explicitness without one genre label winning automatically. These are illustrative task contrasts, not researched audience promises for genres. Additional material/display continuity work is queued in the [child-work record](../reviews/full-run-20261010-p04-review-packet.md#child-extension-queue). [C-11, C-13]
 
 ## Examples and counterexamples
 
-### Creator-reported cases, not observed gameplay
-
-The Valve account supplies a case of contrast within a common art treatment; the two Riot accounts supply a case of controlled variation and exceptions. Their actual assertions and limitations are recorded in C-02–C-04. These are two production contexts, not three independent efficacy studies. No shipped build, gameplay session or embedded video was inspected. [C-02–C-04]
-
-### Illustrative worked example — a shared service environment
-
-**Synthetic and untested.** A space contains storage cabinets, service panels and a portable inspection tool. The intended art direction uses a common construction language. An operable panel must remain distinguishable from a decorative panel, while the tool must be identifiable against either cabinet family. [C-13]
-
-Start by recording the required actions: identify the tool, identify the currently operable panel, and recognize a locked state. Do not assign “all brushed surfaces are operable” merely because that looks coherent. Try a shared mechanical seam vocabulary with a distinct usable control, then vary paint and wear without changing the control’s role. Include a decorative plate with the same paint and an operable control without that paint. Ask for action predictions before feedback. This prevents a test in which every shiny object happens to be the correct answer. [C-08–C-10, C-13]
-
-Compare the candidate to an explicit contextual label and to the existing presentation. At a small task view the control may disappear; in a glossy lighting condition a cabinet may dominate. Neither result is a reason to claim the audience “failed to appreciate” the art. Revise the discriminating feature, change the supporting presentation or narrow the viewing conditions. No rendering, measurements or player responses were produced here. [C-10, C-12, C-13]
-
-### Strong counterexample — identity deliberately unresolved
-
-**Illustrative.** A figure’s allegiance should remain unknown while the player can still choose whether to approach, speak or withdraw. Forcing a standardized faction silhouette or obvious material code would reveal a fact the scene deliberately withholds. The recognition-preserving recipe should be restricted to legitimate task facts, not used to erase ambiguity. A visually discontinuous reveal can be the intended art direction rather than a defect. [C-08, C-13]
+### Creator-reported examples, not observed gameplay
+
+The TF2 paper is a bounded example of cohesion coexisting with contrasting environmental treatments. Riot supplies a useful countercase to relying on static outline alone: its account identifies an animation-dependent identity exception for Lee Sin. Neither source was used to infer player results from commercial success. [C-02, C-03]
+
+Riot also reports a historical Taliyah/background mismatch and a Jhin boundary-visibility problem. These show what that team identified as problems, not an independent severity estimate, a current-build defect or a universal prescription for brighter effects. [C-03]
+
+### Illustrative worked example — a shared maintenance workshop
+
+**Invented for this entry; no asset, prototype or test exists.** The player must identify a service cabinet, learn whether it is available, and decide whether to use it. Several artisans’ cabinets intentionally have different finishes. The proposed invariant is a recognizable service-facing arrangement and accessible status presentation; finish, wear and ornament may vary. The cabinet’s name or ownership need not predict its current availability. [C-07, C-08, C-13]
+
+A first design paints every available cabinet blue. A second preserves a service-facing shape with a distinct available/unavailable state indication; color remains an optional reinforcement. A third uses a player-invoked inspect route. A decorative cabinet shares the workshop’s material vocabulary but lacks the service arrangement. This deliberate contrast avoids defining “same material” as “same function.” The selection contract and actual cabinet states stay unchanged between comparisons. [C-07, C-13]
+
+A discriminating transfer check presents **both** an unfamiliar available service cabinet and a familiar-looking unavailable cabinet, then a decorative example whose finish resembles the usable one. Ask separately what each object is, whether it is available, and whether the player wishes to use it. Repeating three trials where “use” is always correct would not discriminate understanding from a repeated response. This preserves the inspected F01 transfer-example correction without importing its numerical example as an art rule. [C-13]
+
+### Strong counterexample — discovering rather than receiving a classification
+
+An investigation may intentionally ask players to determine whether an object is functional from accumulated evidence. Giving every functional object an immediately recognizable service mark would remove the intended inference. Keep the role-preserving pattern out of that discovery layer; apply it only to already-known task facts or an explicitly offered assistance route. The test must assess whether assistance changes the promised challenge, not describe all obscurity as bad art. [C-07, C-11, C-13]
 
 ## Failure modes and constraints
 
-| Warning sign to investigate later | Competing interpretation | Candidate response, not a tested fix |
-| --- | --- | --- |
-| Artists agree on cohesion; players select the wrong object. | Shared treatment is overriding action distinctions. | Test the actual relation, reduce competing detail or add an explicit aid. |
-| One pose reads correctly; another loses identity. | The selected feature depends on angle, motion or an accessory. | Evaluate the combined asset, not a silhouette still alone. |
-| A skin is recognizable only because a reviewer already knows it. | Familiarity is masking weak transfer. | Separate practiced recognition from unfamiliar interpretation. |
-| Appearance predicts the same answer in every evaluation item. | The task is not discriminating the intended rule. | Include matched contrary cases and predictions before feedback. |
-| A reduced-motion or alternative-color setting loses a required fact. | Decorative and functional roles were not separated. | Reassign the critical distinction and evaluate a usable alternate route. |
-| A shared base creates repeated corrective work. | Variation exceeds the original system’s assumptions. | Permit a justified branch or reduce the variant promise. |
-| “Threatening,” “trustworthy” or “normal” is inferred from a body type alone. | The style embeds an unintended stereotype or a narrow cultural reading. | Revisit context and representation; seek relevant review rather than treating agreement as universal. |
-
-These are proposed diagnostic cases. They are not observations from a completed P04 playtest. [C-09–C-13]
-
-**Accessibility:** do not depend solely on color or visual ornament for critical information. A visual simulation can help locate a problem but cannot substitute for people using the intended access route. Evaluate preferred settings and assistance, including whether alternatives change what is known. Preserve P01’s distinction among CSS pointer units, rendered text-body height and platform guidance; none is converted into a P04 art rule. [C-06, C-07, C-12]
-
-**Localization and representation:** text on surfaces, symbols, gestures and decorative motifs may carry meanings outside the intended one. Treat translation, reading direction, symbolic interpretation and bodily representation as explicit review questions. The inspected corpus does not establish a universal cultural code. Avoid imposing “realistic equals trustworthy” or “unusual body equals hostile.” These are ethical and interpretive safeguards, not claims that a particular asset has caused harm. [C-12, C-13]
-
-**Rights and production:** reference provenance and permission to reuse assets or a performer’s likeness require separate review. This packet contains no assets and grants no rights. A new style rule can affect rigs, material variants, lighting, animation and external asset integration; ownership and change propagation should be visible before a later implementation is approved. No legal conclusion, staffing estimate or performance certification is offered. [C-11, C-14]
+| Warning sign to investigate | Competing explanation | Proposed response |
+|---|---|---|
+| A variant is admired but misidentified. | Appeal and identity are different; novelty or exposure may confound recognition. | Restore the task-bearing distinction or use explicit information; do not interpret liking as a successful task result. |
+| A still silhouette passes but a moving actor fails. | Pose, costume, overlap or background changes the presented shape. | Review the action sequence and actual view with Animation/P03 owners. |
+| “Usable” is inferred from gloss or color alone. | Decorative styling unintentionally became a permission rule. | Separate role, state and surface vocabulary; include contradictory-looking negative cases. |
+| A low-distraction mode removes a required state. | The required fact was embedded only in decoration. | Preserve usable information through an appropriate alternative; evaluate actual access users. |
+| All scenes become high-contrast noise. | Every contributor treated local salience as the highest priority. | Revisit the scene’s task hierarchy and reduce optional emphasis. |
+| One reference image produces inconsistent assets. | Important permissible variations and exceptions were never specified. | Add targeted examples/owners, not a larger unsourced style bible by default. |
+| An access overlay trivializes a legitimate inference. | Assistance changed information, not just presentation. | Make the changed contract explicit and review it; never hide essential information solely to preserve one sensory experience. |
+
+These are prospective diagnoses, not findings from a P04 playtest. [C-07–C-13]
+
+**Ethics and localization:** avoid presenting body shape, complexion, disability markers, accent-associated costume or a color as reliable evidence of morality or personality. The inspected sources do not establish such mappings. Evaluate intended meanings with relevant audiences and distinguish cultural familiarity from task learning. Review reference provenance and permitted use before asset production; this research grants no asset rights or production approval. These are proposed risk controls, not legal conclusions or a completed cultural review. [C-10, C-11, C-14]
 
 ## Playtest and validation
 
-**PROPOSED — NOT RUN.** The following is a study specification for a later authorized decision, not a pilot already performed. It requires no fixed participant count, timing window or numerical success threshold from this literature. [C-13, C-14]
-
-**Question:** Does the proposed selective-cohesion treatment preserve required action and identity distinctions while providing a worthwhile artistic benefit over the existing or simpler alternative?
-
-**Comparisons:** existing presentation; proposed constrained variation; and an explicit-label or less-detailed alternative selected for the actual task. A separate deliberately unconstrained variant can diagnose what the contract protects, but it is not automatically a fair quality comparison. Keep action rules, task layout, available information, viewing conditions and exposure comparable; record unavoidable differences.
-
-**Participants and procedure:** include unfamiliar and practiced users of the relevant task and actual users of the target visual/nonvisual access routes. Do not treat a small convenience sample as representative. Before collecting data, the study owner must specify inclusion, sample rationale and the practical tolerance for added recognition errors or workload. Counterbalance conditions and use different matched items where carryover would reveal answers. Collect identity/action predictions and reasons before feedback; include both permitted and forbidden actions. Then collect separate aesthetic, interpretation and comfort reports.
-
-**Measures:** confusion matrix of identities and action states; false interaction and missed-action attempts; uncertainty reports; task completion and correction behavior; separate style-fit and appeal judgments; requests to change settings; and documented authoring/revision effort. Time measures require an agreed start/end event and actual instrumentation; none has been measured here.
-
-**Confounds:** prior familiarity, item difficulty, exposure order, label availability, screen/view differences, lighting, animation, simultaneous changes and evaluator expectations. Do not interpret faster action as better art, nor a preference score as adequate access.
-
-**Decision rule:** reject or revise any candidate that makes an essential fact unavailable in a supported route or systematically communicates the wrong action/identity. When recognition is not practically worse under a predeclared local criterion and the intended artistic value is credibly supported, retain only the tested scope. Where results are inconclusive, do not claim equivalence; prefer a reversible narrower treatment or gather the evidence needed for the actual production decision. Keep a deliberate ambiguity only when it concerns information the task permits to remain unknown. Participants may pause, adjust settings or withdraw; requests to stop are not inconvenient outliers. [C-08–C-13]
+**PROPOSED — NOT PERFORMED.** No participants, art variants, perceptual simulations, rendered scenes or performance benchmarks were produced. This protocol is a hypothesis-led plan requiring separate authorization. [C-13, C-14]
+
+**Question:** Does selective preservation of role-bearing features help unfamiliar variants remain correctly interpretable without undermining intended discovery, preference, comfort or production feasibility?
+
+**Comparison:** A uses uniform appearance; B uses selective role-preserving variation; C uses greater stylistic freedom with a contextual information alternative. A/B can test variation more directly; C is a decision alternative, not a pure feature ablation. Match tasks, object availability, view, input, opportunity to inspect and exposure. Record remaining differences in size, lighting, backgrounds and assistance.
+
+**Participants and context:** recruit only after an approved protocol defines the actual audience. Include unfamiliar and experienced users, relevant vision/access needs and relevant language/cultural backgrounds; do not treat simulated impairment or an expert artist’s inspection as representative user evidence. Use participants’ chosen settings and ordinary device arrangements. A later study owner must justify sample size from the intended estimation precision, pilot variability and resources; no sample-size guarantee is supplied here.
+
+**Procedure and measures:** counterbalance treatment order and asset-to-treatment assignments where feasible. Teach a common task, then test novel instances and matched positive/negative states with different correct responses. Record identity classification, state understanding, action reasons, completion/errors, help use and confusion. Collect aesthetic preference, perceived cohesion, comfort and intended-emotion reports separately. Include repeated exposure and a later unfamiliar family; immediate familiarity is not durable transfer. Log authoring/revision effort separately rather than inferring savings from player speed.
+
+**Disconfirmation:** reject the stronger “preserves understanding” claim when B’s role or state errors exceed a predeclared project-relevant tolerance, when success depends only on repeated answer patterns, or when its effect disappears on genuinely new examples. Prefer the simpler option when the evidence is inconclusive and the added contract has no demonstrated local value; inconclusive evidence is not equivalence. A critical information failure blocks that candidate’s advancement pending correction, even if average liking is high. Retain deliberate ambiguity only where it is the approved task rather than an accidental access barrier. Define tolerances and analysis before data collection; no numbers or thresholds here have been adopted by the studio.
 
 ## Claim ledger
 
-Claim IDs are local to this entry. Confidence describes the exact scoped wording, not a source’s prestige or the recipe’s overall efficacy. Proposed procedures and examples are not approved studio decisions.
+Confidence concerns the exact scoped wording, not source prestige. References support only the described link; an inference or proposed test is not converted into an empirical result.
 
 ### C-01
-
-**Claim:** Treat art direction as a proposed system of visual relationships and permissible variation, not a single realism slider. **Class:** `inference`. **Confidence:** moderate as a useful analytic distinction, not a validated optimum.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-001, §3/§4.2–4.3; GDR-SRC-20261010-P04-002, Filling Up Buckets; GDR-SRC-20261010-P04-004, §4.
-
-**Applicability, contrary evidence and unresolved question:** This is P04 synthesis. Which relationships matter depends on the task, intended experience and audience; a deliberately mixed style may be appropriate.
+**Claim:** Style, cohesion, material language and task readability are useful separate analytic dimensions for this draft. **Class:** `inference`. **Support:** original synthesis; inspected P01 Visual communication §§Decision/Core explanation and Interface and information information-contract passage, recorded in the packet. **Confidence:** moderate for conceptual separation; usefulness not measured. **Applicability:** genre-neutral design analysis. **Unresolved:** whether a later project needs different terminology.
 
 ### C-02
-
-**Claim:** Valve reports using shared illustrative treatment while distinguishing its opposing environments through different shapes, materials and palettes. **Class:** `practitioner-heuristic`. **Confidence:** moderate for the creator account; no efficacy estimate.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-001, §4.2 World Modeling and §4.3 Texture Painting, PDF pp.2–3.
-
-**Applicability, contrary evidence and unresolved question:** One historical production. Supports considering selective contrast, not a universal warm/cool faction code or guaranteed recognition.
+**Claim:** Valve describes an internally controlled art language with deliberately contrasting team-world treatments. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P01-13, §§3–4.3, PDF pp. 2–3. **Confidence:** high for attribution, not efficacy. **Limit:** one production, no comparison of player outcomes. **Unresolved:** which relationships transfer usefully.
 
 ### C-03
-
-**Claim:** Riot describes preserving recognizability while varying the combined model, animation and effects treatment of skins. **Class:** `practitioner-heuristic`. **Confidence:** moderate for accurate attribution, low for general effectiveness.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-002, Silhouettes and Filling Up Buckets.
-
-**Applicability, contrary evidence and unresolved question:** A competitive-game production goal. No measured change budget; no reason to make all objects equally distinctive.
+**Claim:** Riot’s clarity account preserves identity across variation, gives an animation-dependent silhouette exception, and reports contextual clarity failures. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P04-001, Silhouettes and Clarity in Action. **Confidence:** high for the reported cases. **Limit:** historical creator account; no current-build observation. **Unresolved:** audience-specific effects and causal contribution of each fix.
 
 ### C-04
-
-**Claim:** The Lee Sin account reports common base-mesh work, selective omission of a new ponytail in some skins, and additional cross-skin animation/clipping checks. **Class:** `practitioner-heuristic`. **Confidence:** moderate for reported decisions; costs not quantified.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-003, Preparing the Ponytail; Base Meshes and 3D Sustainability; Making Skins with Style.
-
-**Applicability, contrary evidence and unresolved question:** Variation exceptions can protect an existing identity. No measured production saving or proof that a common rig suits every body, costume or performance.
+**Claim:** The inspected render-style experiments do not support a simple “more realism means less appeal” ranking for their tested stimuli. **Class:** `empirical-evidence`. **Support:** GDR-SRC-20261010-P04-002, §5.1 and §8; methods and limits described above. **Confidence:** moderate, narrow controlled comparisons with lighting limits. **Outcome uncertainty:** no game-level effect estimate or general equivalence established. **Unresolved:** other geometry, emotional performance, environments and audiences.
 
 ### C-05
-
-**Claim:** Render-style appeal did not form a simple increasing realism ranking in the inspected still/moving comparison. **Class:** `empirical-evidence`. **Confidence:** moderate, narrow controlled stimulus set.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-004, §4 and §5.1: separate groups of 17 viewers rated still or moving male-character treatments. Several abstract and realistic styles were among the more appealing categories.
-
-**Applicability, contrary evidence and unresolved question:** Brief viewing, selected styles and a deliberately ill-looking treatment; not an equivalence test, gameplay comparison or general uncanny-valley law. No effect-size or population-wide preference is inferred.
+**Claim:** Epic documents physically based material controls separately from a photorealistic-only art goal. **Class:** `practitioner-heuristic` (official technical documentation). **Support:** GDR-SRC-20261010-P04-003, introductory and material-attribute sections. **Confidence:** high for document scope. **Limit:** no proof of aesthetic quality or task recognition. **Unresolved:** suitability under a particular approved pipeline.
 
 ### C-06
-
-**Claim:** XAG 103 recommends alternatives to color-only and visual-only critical information and distinguishes simulation checks from evaluation with affected players. **Class:** `practitioner-heuristic`. **Confidence:** high for what this vendor page recommends, not for a particular design’s access.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-010, Goal; Implementation guidelines on color, other modalities and player evaluation.
-
-**Applicability, contrary evidence and unresolved question:** Official guidance, not a formal standard. Redundant visual features are not automatically nonvisual access; no emotional-equivalence result.
+**Claim:** Important information needs appropriate additional-channel consideration, not merely a second visual distinction. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P01-05, Implementation guidelines; freshly inspected. **Confidence:** high for attribution; local usability unknown. **Limit:** vendor guidance, not formal certification or emotion-equivalence evidence. **Unresolved:** usable alternatives for the actual task.
 
 ### C-07
-
-**Claim:** XAG 117 supports control of distracting or non-core motion while retaining a stated exception for some gameplay backgrounds behind interface content. **Class:** `practitioner-heuristic`. **Confidence:** high for the scoped recommendation.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-011, Implementation guidelines, moving UI/background exception and repetitive non-core animation.
-
-**Applicability, contrary evidence and unresolved question:** Not an instruction to freeze every gameplay animation. No medical safety, numerical threshold or P03 camera-setting recommendation.
+**Claim:** Preserve task-bearing relationships while allowing deliberate stylistic exceptions; compare this with uniformity and explicit assistance. **Class:** `inference`. **Support:** C-02/C-03/C-06; the causal bridge is spelled out in Core explanation. **Confidence:** moderate as a decision method, low for any promised local benefit. **Counterpressure:** deliberate discovery may depend on ambiguity. **Unresolved:** which features carry role/state information and when variation is worth its cost.
 
 ### C-08
-
-**Claim:** When a task needs stable identification, preserve the required relationship through stylistic changes rather than requiring every visual feature to remain fixed. **Class:** `inference`. **Confidence:** moderate for the conditional rationale; local benefit untested.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-002, Filling Up Buckets; GDR-SRC-20261010-P04-003, Preparing the Ponytail; C-03/C-04; reviewed P01 visual-communication, Core explanation and mechanisms.
-
-**Applicability, contrary evidence and unresolved question:** The bridge is to compare what players must distinguish, not to canonize a particular shape. Disguise, discovery and interpretive art may intentionally withhold identity. See P04-CON-01.
+**Claim:** A rendered surface description should not silently become an interaction-permission rule. **Class:** `inference`. **Support:** C-05 and the task/role distinction in C-01; not an empirical material-perception result. **Confidence:** moderate as a consistency check. **Limit:** a game may deliberately teach such a rule. **Unresolved:** how reliably the chosen material/state relationship can be learned and perceived.
 
 ### C-09
-
-**Claim:** A recurring material treatment should not be treated as an established affordance until its relation to action has been checked in context. **Class:** `hypothesis`. **Confidence:** low for effectiveness of the proposed validation workflow.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-001, §4.2–4.3 gives a production vocabulary, not affordance-learning evidence; reviewed P01 distinguishes recognition from meaning/action.
-
-**Applicability, contrary evidence and unresolved question:** P04 proposes an action-prediction check across lighting, wear and noninteractive lookalikes. Material semantics, audience familiarity and display variation remain unmeasured.
+**Claim:** Evaluate actual view, display, motion and access context before transferring a style decision; do not substitute text/target standards for world-art thresholds. **Class:** `inference`. **Support:** inspected P01 correction receipt and C-03/C-06/C-12. **Confidence:** moderate; no new device experiment. **Limit:** P03 candidates remain unavailable. **Unresolved:** view-dependent failures and context-specific acceptance criteria.
 
 ### C-10
-
-**Claim:** Evaluate characters, surroundings and motion together at actual task views before expanding a style across assets. **Class:** `inference`. **Confidence:** moderate as a risk-control proposal, not measured savings.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-001, §4.1–4.3; GDR-SRC-20261010-P04-002, Silhouettes; GDR-SRC-20261010-P04-003, cross-skin checks.
-
-**Applicability, contrary evidence and unresolved question:** An isolated beauty render can omit the decision context by construction. P03 camera/display details are missing; local view coverage and production costs need later agreement.
+**Claim:** A style system requires ownership of variants, exceptions and review work; its cost or savings cannot be inferred from a style label. **Class:** `inference`. **Support:** C-02/C-03 plus original production-work decomposition. **Confidence:** moderate for work categories, low for unmeasured magnitude. **Limit:** no staffing, asset-count or budget estimate. **Unresolved:** marginal authoring/rework cost and provenance review.
 
 ### C-11
-
-**Claim:** Style constraints can organize repeatable production, but reuse and exception management create different costs that must be measured locally. **Class:** `inference`. **Confidence:** moderate for named work categories, unknown magnitude.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-003, Base Meshes and 3D Sustainability / Making Skins with Style; GDR-SRC-20261010-P04-001, §4.3.
-
-**Applicability, contrary evidence and unresolved question:** No staffing, asset count, performance budget or stylization-versus-realism cost ranking is supported. Shared assets can also make corrective changes propagate.
+**Claim:** Meaning, preference and intended mood may vary by audience, context and familiarity; visual difference does not prove personality or moral character. **Class:** `hypothesis` for the proposed local interpretation comparisons. **Support:** adjacent C-04, inspected W01 characterization distinction, and original countercases. **Confidence:** low for any specific cultural or player response. **Limit:** no cross-cultural or representation study inspected here. **Unresolved:** relevant populations and misinterpretations.
 
 ### C-12
-
-**Claim:** Separately evaluate desired expression, player interpretation, decision accuracy, comfort and representational effects. **Class:** `inference`. **Confidence:** moderate as measurement discipline; no guaranteed method of inclusion.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-004, §5.1; GDR-SRC-20261010-P04-010, actual-player evaluation; reviewed P02 multimodal-communication, decision facts versus emotion; W01 character-design, Decision and scope.
-
-**Applicability, contrary evidence and unresolved question:** Aesthetic preference is not comprehension. Do not use appearance or movement to diagnose a real person’s honesty, morality, ability or identity. Cross-cultural and specialist access evidence remains limited.
+**Claim:** XAG 117 recommends controls for specified visual distraction/motion while retaining essential-gameplay exceptions. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P01-10, Implementation guidelines. **Confidence:** high for attribution. **Limit:** no blanket animation-removal rule or safe numerical setting. **Unresolved:** which particular effects are optional and how alternatives work.
 
 ### C-13
-
-**Claim:** The application sequence, illustrations and prospective comparisons below are testable proposals, not results or approved production requirements. **Class:** `hypothesis`. **Confidence:** low for untested feasibility and effect.
-
-**Support / precise locator:** Original P04 synthesis under the supplied brief, Decision questions and output requirements; proposed application of C-08–C-12.
-
-**Applicability, contrary evidence and unresolved question:** No prototype, assets, participants or test data. A future study owner must specify resources, decision tolerances and inclusion before execution; no invented power guarantee.
+**Claim:** The process, workshop example, proposed test and rejection criteria are unvalidated local research proposals. **Class:** `hypothesis`. **Support:** original P04 synthesis; F01 selected pattern’s transfer-discrimination correction is an inspected design constraint, not a completed art test. **Confidence:** low for eventual effectiveness. **Limit:** NOT PERFORMED; no fixed sample, metric guarantee or adopted tolerance. **Unresolved:** authorized protocol, feasibility and measurement sensitivity.
 
 ### C-14
-
-**Claim:** P04 is authorized bounded research; candidates and source identities remain provisional, unreleased and separate from adoption. **Class:** `studio-decision`. **Confidence:** high from explicit instruction.
-
-**Support / precise locator:** Doug’s P04 message and attached Pasted text(3).txt, Assigned outputs, Authorization update, Reviewed dependency receipt and Current jobs and boundaries; dispatch run dated 2026-10-10.
-
-**Applicability, contrary evidence and unresolved question:** Owner Doug. This permission does not approve evidence conclusions, canonical allocations, implementation, participant work, publication or repository/Project-source changes.
+**Claim:** Doug authorized this bounded public-source P04 research and draft artifacts, not implementation, participant work or release. **Class:** `studio-decision`. **Owner/date:** Doug, supplied P04 dispatch, 2026-10-10, Authorization Update and Assigned Outputs. **Confidence:** high for explicit scope. **Limit:** candidate identities remain temporary; approval fields null. **Unresolved:** independent content review, coordination and later decisions.
+
+### C-15
+**Claim:** Recent creator accounts describe mixed stylization/realism and selective cohesion/contrast under different production constraints. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P04-011, stylized-likeness answer; P04-012, Campos/Lozano art paragraphs. **Confidence:** high for attribution. **Limit:** promotional accounts, not controlled efficacy, savings or interpretation data; no footage inspected. **Unresolved:** local value and transfer beyond the reported productions.
 
 ## References
 
-All public records below were inspected in the stated passages on **2026-10-11 UTC**. IDs are P04-scoped source records, not permanent SRC allocations. Dates of older works are publication dates, not claims of current game behavior. Repeated reference records support standalone reading; they are not extra evidence.
+All records below were inspected in relevant passages on 2026-10-10. Source IDs retained from P01 are explicit reuse, not new allocations. New P04 IDs are temporary; central URL/DOI/edition reconciliation remains pending. Document copies and candidate citations do not provide independent corroboration.
+
+### GDR-SRC-20261010-P01-13
+
+**Jason Mitchell, Moby Francke and Dhabih Eng. [Illustrative Rendering in Team Fortress 2](https://cdn.cloudflare.steamstatic.com/apps/valve/2007/NPAR07_IllustrativeRenderingInTeamFortress2.pdf).** Valve / NPAR 2007. Date: 2007; exact publication day unknown. Edition/build: 2007 paper; described game build unspecified.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand production/technical paper. **Locators:** §§3, 4.1–4.3; PDF pp. 2–3, Figures 2–5. **Supports:** C-02; indirect C-07/C-10.
+
+**Limits:** One production account, not a player experiment. PDF figures inspected, not game footage. **Relationship:** Same work as P01-13; former steamcdn-a.akamaihd.net route is a host alias, not corroboration. **Rights:** Reuse permission not established; paraphrase only; figures not redistributed.
 
 ### GDR-SRC-20261010-P04-001
 
-**Jason Mitchell, Moby Francke and Dhabih Eng, Valve.** [Illustrative Rendering in Team Fortress 2](https://cdn.akamai.steamstatic.com/apps/valve/2007/NPAR07_IllustrativeRenderingInTeamFortress2.pdf). **Publisher:** NPAR / Valve author paper. **Publication/update:** 2007; exact publication day not established. **Edition/build:** NPAR 2007 paper; six-page PDF; production build unspecified.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Primary creator production/technical account. **Exact locators:** §3 Commercial Illustration Techniques; §4.1 Character Modeling, Figure 2; §4.2 World Modeling; §4.3 Texture Painting; PDF pages 2–3. **Claims supported in this entry:** C-01, C-02, C-09–C-11.
-
-**Limits:** No controlled player-recognition experiment, modern-device benchmark or causal sales evidence. PDF pages 2–3 visually inspected; no game build or footage observed. **Independence/deduplication:** Independent production context from Riot. Same paper as reviewed GDR-SRC-20261010-P01-13, whose older Steam CDN URL is an alternate route; central source consolidation pending. **Rights:** Original copyright; reuse permission not established. Paraphrase only; no artwork, screenshots or assets distributed.
+**bananaband1t / Riot Games. [Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/).** Riot Games. Date: 2021-03-12. Edition/build: Developer article; example build numbers unspecified.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand development account. **Locators:** Silhouettes; Matching Hitboxes; Hierarchy; Minimizing Noise; Clarity in Action (Jhin, Taliyah, Leona and Renekton cases). **Supports:** C-03; indirect C-07/C-09.
+
+**Limits:** Creator-reported practices and problems; no footage watched or controlled outcome data. **Relationship:** Independent production from Valve; retrospective selection and issuer incentives remain. **Rights:** Reuse license not established; paraphrase only.
 
 ### GDR-SRC-20261010-P04-002
 
-**bananaband1t, Riot Games.** [Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/). **Publisher:** Riot Games / League of Legends. **Publication/update:** 2021-03-12. **Edition/build:** Dated developer article; game build unspecified; historical account, not current patch verification.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Primary creator account / practitioner guidance. **Exact locators:** The Unbreakable Vows; Silhouettes; Filling Up Buckets; Cosmetic Animations. **Claims supported in this entry:** C-01, C-03, C-08, C-10.
-
-**Limits:** Describes Riot goals and constraints, not comparative player outcomes. Media not played. The skin-variation metaphor is not a measured budget or a universal invariant. **Independence/deduplication:** Same studio and game family as source 003: not independent corroboration of efficacy. Cross-batch URL/edition deduplication pending. **Rights:** Reuse license not established; attributed paraphrase only.
+**Rachel McDonnell, Martin Breidt and Heinrich H. Bülthoff. [Render me Real? Investigating the Effect of Render Style on the Perception of Animated Virtual Humans](https://www.scss.tcd.ie/Rachel.McDonnell/papers/Siggraph2012a.pdf).** ACM Transactions on Graphics 31(4), Article 91. Date: 2012-07. Edition/build: SIGGRAPH 2012 version of record; DOI 10.1145/2185520.2185587.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Original human perception experiments. **Locators:** §5.1, PDF pp. 4–6 / printed 91:4–91:6; §§7–8, PDF p. 10 / 91:10. **Supports:** C-04; adjacent C-11 only.
+
+**Limits:** Selected rendered humans, not a game-style trial; lighting not fully controlled and emotional-content limitation acknowledged. Figures/text inspected on PDF pp. 5 and 10. **Relationship:** Separate study from Normoyle/Jörg; shared research area is not replication. **Rights:** ACM copyright notice; paraphrase only; no figures redistributed.
 
 ### GDR-SRC-20261010-P04-003
 
-**ASU Team, Riot Games; named concept, character, technical-art and animation contributors.** [/dev: Modernizing the Monk](https://www.leagueoflegends.com/en-gb/news/dev/dev-modernizing-the-monk/). **Publisher:** Riot Games / League of Legends. **Publication/update:** 2024-04-08. **Edition/build:** Lee Sin art-and-sustainability update developer article; exact game build unspecified.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Primary multidisciplinary creator account. **Exact locators:** Creating Consistency Across Skins; Preparing the Ponytail; Base Meshes and 3D Sustainability; Animation → Making Lee’s Animations More Impactful, Float like a Butterfly, Sliding Hitboxes like a Lee, Making Skins with Style. **Claims supported in this entry:** C-04, C-08, C-10, C-11.
-
-**Limits:** Intentions and reported production issues, not measured satisfaction, cost savings or a directly observed build. Animation contributors: Sean “Riot Redepoka” Yeung and Einar “Riot Beinhar” Langfjord. Embedded media not played. **Independence/deduplication:** Same production line as source 002; multiple contributors are not separate efficacy studies. Cross-batch deduplication pending. **Rights:** Reuse license not established; paraphrase only; no likenesses, media or assets copied.
-
-### GDR-SRC-20261010-P04-004
-
-**Rachel McDonnell, Martin Breidt and Heinrich H. Bülthoff.** [Render me Real? Investigating the Effect of Render Style on the Perception of Animated Virtual Humans](https://www.scss.tcd.ie/Rachel.McDonnell/papers/Siggraph2012a.pdf). **Publisher:** ACM Transactions on Graphics. **Publication/update:** 2012-07. **Edition/build:** 31(4), Article 91; eleven-page author PDF; DOI 10.1145/2185520.2185587.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Original human perception experiments. **Exact locators:** §4 Choosing Render Styles; §5.1 Still vs. Moving, methods/results, PDF pages 4–6; §5.2 Motion Anomalies and §5.2.1 Results, PDF pages 6–7. **Claims supported in this entry:** C-05; indirect C-12.
-
-**Limits:** Selected male-character stimuli and brief viewing tasks, not controlled gameplay. A deliberately ill-looking treatment complicates a neutral realism continuum. No raw-data reanalysis. PDF pages 5 and 7 visually inspected; the page-6 screenshot route failed. **Independence/deduplication:** Original study; author PDF and DOI/publisher record are one source. Cited by source 005: independent cohorts, not disconnected intellectual lines. Lowercase author-path route failed; uppercase path succeeded. **Rights:** ACM copyright; no new reuse permission inferred from author hosting. No figures or stimulus media redistributed.
-
-### GDR-SRC-20261010-P04-010
-
-**Microsoft.** [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103). **Publisher:** Microsoft Learn. **Publication/update:** Last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live page revision inspected on evidence-check date.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official vendor accessibility guidance. **Exact locators:** Goal and Overview; Implementation guidelines → alternatives to color and visual-only information; simulation-filter and actual-player evaluation paragraphs. **Claims supported in this entry:** C-06; indirect C-12.
-
-**Limits:** Practitioner guidance, not a formal standard, legal advice or certification. Availability of an alternative is not demonstrated usability or emotional equivalence. Public body inspected despite authorization boilerplate. **Independence/deduplication:** Same document as reviewed GDR-SRC-20261010-P01-05 and GDR-SRC-20261010-P02-005; central reconciliation pending. Same issuer as source 011. **Rights:** Vendor page; content reuse license not inspected; paraphrase only; no example media copied.
+**Epic Games. [Physically Based Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine).** Epic Developer Community. Date: Publication/update date unknown; live page checked 2026-10-10. Edition/build: Unreal Engine 5.8 documentation, displayed edition.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official technical documentation. **Locators:** What Does Physically Based Mean?; PBR Material Attributes; Roughness; Mapping Roughness; Roughness vs. Specular. **Supports:** C-05; design inference C-08.
+
+**Limits:** Documented material model, not a readability experiment or tested local implementation; numeric defaults not recommended here. **Relationship:** Same issuer as the other Epic records; distinct documents, not independent efficacy evidence. **Rights:** Reuse license not inspected; paraphrase only.
+
+### GDR-SRC-20261010-P01-05
+
+**Microsoft. [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103).** Microsoft Learn. Date: Last updated 2026-03-04. Edition/build: Unnumbered live page revision checked 2026-10-10.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance. **Locators:** Goal; Implementation guidelines; Visual cues; Color and additional sensory channels. **Supports:** C-06; indirect C-07/C-09.
+
+**Limits:** Guidance, not a formal standard, compliance certificate or evidence of emotional equivalence. **Relationship:** Reuses inspected P01-05; P02-005 duplicates this URL. Central deduplication pending. **Rights:** Reuse license not inspected; paraphrase only.
+
+### GDR-SRC-20261010-P01-10
+
+**Microsoft. [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117).** Microsoft Learn. Date: Last updated 2026-03-04. Edition/build: Unnumbered live page revision checked 2026-10-10.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance. **Locators:** Overview; Implementation guidelines; Moving/blinking/scrolling content and essential-gameplay exceptions; Camera movement options. **Supports:** C-12; indirect C-09.
+
+**Limits:** No safe-motion numerical threshold or blanket removal of all gameplay animation; not certification. **Relationship:** Reuses P01-10; P02-010 duplicates this URL. Same issuer as XAG 103, not independent player evidence. **Rights:** Reuse license not inspected; paraphrase only.
 
 ### GDR-SRC-20261010-P04-011
 
-**Microsoft.** [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117). **Publisher:** Microsoft Learn. **Publication/update:** Last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live page revision inspected on evidence-check date.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official vendor accessibility guidance. **Exact locators:** Implementation guidelines → moving/blinking/scrolling UI and its background-motion exception; camera motion; repetitive non-core animation; parsed text lines 43–121. **Claims supported in this entry:** C-07.
-
-**Limits:** Not a universal freeze-all-gameplay requirement, medical safety threshold or certification. No FOV, flashing or animation-duration limit is extracted. Camera-setting research remains P03 ownership. **Independence/deduplication:** Same document as reviewed GDR-SRC-20261010-P01-10 and GDR-SRC-20261010-P02-010; central reconciliation pending. Related vendor guidance is not independent efficacy evidence. **Rights:** Vendor page; content reuse license not inspected; paraphrase only.
+**Bryan Johnston and Mike Laygo / Play by Play Studios; interviewer unspecified. [Built with UE5, NBA THE RUN looks to bring back the golden age of basketball video games](https://www.unrealengine.com/developer-interviews/built-with-ue5-nba-the-run-looks-to-bring-back-the-golden-age-of-basketball-video-games).** Epic Games, Unreal Engine developer interviews. Date: 2026-05-28. Edition/build: Pre-beta creator interview; Unreal Engine 5, minor/build unspecified.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand creator interview. **Locators:** Questions about stylized likeness and character animation; Johnston/Laygo answers, web extraction lines 57–67. **Supports:** C-15, style portion only.
+
+**Limits:** Design intentions and reported reuse, not measured responsiveness, audience response, savings or a current release-status claim. **Relationship:** Separate production from Valve/Riot/Naughty Dog; hosted by its engine vendor, with promotional incentives. **Rights:** Reuse license not established; paraphrase only; no media redistributed.
+
+### GDR-SRC-20261010-P04-012
+
+**David Jaumandreu; accounts by Jesús Campos and María Lozano / The Game Kitchen. [A behind-the-scenes look at Ninja Gaiden: Ragebound’s art direction](https://blog.playstation.com/?p=407986).** PlayStation.Blog. Date: 2025-07-24. Edition/build: Pre-release developer account; described console build unspecified.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand production account. **Locators:** Campos palette, low-resolution and level-readability paragraphs; Lozano silhouette/character-contrast paragraphs, web extraction lines 63–71. **Supports:** C-15, intent/constraints only.
+
+**Limits:** Intent, production decisions and subjective character descriptions; not measured player interpretation or a universal color/personality mapping. **Relationship:** Separate 2D production from other cases; publisher-hosted promotional selection remains. **Rights:** Copyright notice; paraphrase only; no art/media redistributed.
 
 ## Open questions and change history
 
-Open coverage: recognition under actual camera/display combinations; material semantics across lighting and surface states; cross-cultural and nonvisual interpretation; measured total production cost; artist/performer rights processes; and whether the proposed constrained-variation recipe improves its actual task. No equal-budget realism/stylization comparison, complete art-history survey or gameplay efficacy test was performed.
-
-P04-CON-01 preserves the tension between required recognition and legitimate ambiguity; P04-CON-02 preserves the absence of a simple realism ranking. These are packet-local records, not newly allocated global contradiction IDs. Additional material/affordance and performance-simplification questions are [queued child-work requests](../reviews/full-run-20261010-p04-review-packet.md#child-extension-queue), not silently omitted patterns or authorized executions.
-
-**2026-10-11 UTC:** initial P04 candidate, version 0.1.0, revision initial-draft-1; no predecessor, supersession or prior P04 submission asserted. Author self-review is recorded in the packet and is not independent review. Candidate/source canonical reconciliation, host tests and release remain pending. Next decision: independent content review of these qualified candidates and coordination of missing dependencies, not implementation.
+### Coverage remains open
+
+| Subtopic | Inspected coverage | Next discriminating question |
+|---|---|---|
+| Style systems, selective cohesion and deliberate contrast | Creator accounts across historic 3D, recent 3D and 2D production; conditional synthesis. | Which relationships actually carry role/state meaning on unfamiliar examples? |
+| Value/color/detail/silhouette | Firsthand constraints and negative cases; access guidance. | Does a distinction survive actual motion, lighting and supported access settings? |
+| Material language | Current PBR documentation; semantics-versus-surface distinction. | When does intended material meaning fail across scenes or display conditions? |
+| Environment/character cohesion | Reported coordinated and contrasting treatments. | Can a deliberate mismatch remain comprehensible without removing the intended ambiguity? |
+| Stylization/realism and audience response | One narrow rendered-human experimental family. | Do results transfer to varied geometry, environments, emotional performances and target audiences? |
+| Device/access/localization | Scoped vendor guidance and design questions; no P03 bytes, no new user data. | What context changes require a different presentation rather than a translated numerical setting? |
+| Production constraints | Work categories and creator accounts; no measured cost model. | Does a maintained style contract reduce rework enough to justify its overhead? |
+
+Contradiction records P04-CON-01/02/05/06 and child-work rows are in the review packet. These are batch-local records, not global CON allocations. All tests remain proposed. The bounds of two research topics and two patterns are fulfilled; comprehensive heading coverage is not certified.
+
+**History:** 2026-10-10, first P04 submission, version 0.1.0 / initial-draft-1. No predecessor or superseded artifact. The later creator-source check added C-15 without renumbering earlier claims. The same author performed the self-review; independent P04 review and Gate C acceptance remain pending. Local document checks do not pass Gate D host retrieval. Gate E, release and game adoption remain unapproved. See the [exact review packet](../reviews/full-run-20261010-p04-review-packet.md).

```

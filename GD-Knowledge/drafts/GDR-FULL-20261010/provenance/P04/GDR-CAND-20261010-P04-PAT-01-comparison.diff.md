# Preserved GDR-CAND-20261010-P04-PAT-01-comparison.diff

Original payload SHA-256: `584b1cdf1039a3f8b6ca3e2d4a2abab47b4c1ccbea70cffc5ce8968fd88101b3`. Complete original record follows in Markdown.

```text
--- earlier/recognition-preserving-style-variation.md
+++ later/role-preserving-style-variation.md
@@ -1,7 +1,7 @@
 ---
 id: GDR-CAND-20261010-P04-PAT-01
 kind: pattern
-title: Recognition-preserving style variation
+title: Role-preserving style variation
 version: 0.1.0
 candidate_revision: initial-draft-1
 status: draft
@@ -9,250 +9,199 @@
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
-- recognizable visual variants
-- style-variation contract
+- readable art variants
+- role-stable visual variation
 tags:
-- art-direction
-- variants
-- identity
-- recognition
+- style-variation
+- role-recognition
+- state-comprehension
 - conditional-recipe
 related_topics:
 - GDR-CAND-20261010-P04-TOP-01
-- GDR-CAND-20261010-P04-TOP-02
 related_patterns:
 - GDR-CAND-20261010-P04-PAT-02
 related_genres: []
 source_ids:
-- GDR-SRC-20261010-P04-002
-- GDR-SRC-20261010-P04-003
-- GDR-SRC-20261010-P04-010
+- GDR-SRC-20261010-P01-13
+- GDR-SRC-20261010-P04-001
+- GDR-SRC-20261010-P01-05
 reviewer: null
 approved_by: null
 approved_date: null
+predecessor_sha256: null
+supersedes: null
+change_summary: Initial P04 submission; does not replace or resend any previous batch.
+byte_hash_record: ../reviews/full-run-20261010-p04-integrity-receipt.md
 ---
 
-# Recognition-preserving style variation
-
-**Hypothesis-led draft pattern, 0.1.0 / initial-draft-1.** This pattern is an optional way to organize and test repeated visual variants. It is not a law of silhouette design or evidence that controlled variation is always more appealing. [C-01, C-07]
+# Role-preserving style variation
+
+**Draft 0.1.0; initial-draft-1. Conditional pattern candidate, not a validated recipe or released guidance.**
 
 ## Purpose
 
-Help a designer change an appearance without accidentally changing an identity or action distinction the player still needs. The intended result is recognizable variation with explicit exceptions, not maximum uniformity or a ban on ambiguity. The owning [Art direction topic](../topics/art-direction.md) supplies the broader alternatives. [C-01, C-02]
-
-The pattern owns **variation across a family of assets or performances**. It does not own adding redundant critical cues or translating facts between modalities; those P01/P02 patterns remain external reviewed candidates. [C-04]
+Permit art variants to differ meaningfully without silently changing the features a player relies on to recognize an already-known role or current state. This is especially relevant when environments, characters, props or cosmetic variants are produced by different contributors. The intended benefit is comprehensible variation, not maximum contrast or a uniform visual style. Added value over a simpler reference set is **unestablished**. [C-01]
 
 ## Context and prerequisites
 
-Consider this recipe when multiple appearances represent the same entity, role or action family, and a mistaken association would affect a legitimate decision. It can apply to costumes, equipment sets, environmental families or pose treatments without choosing a genre. The source precedents concern particular games; this broader applicability is a hypothesis. [C-01]
-
-Before use, the later project needs a stated distinction to preserve, examples of things that should not be confused, actual task views and settings, a way to evaluate interpretation, and a production owner who can permit exceptions. The family need not share every feature or one rig. No platform, camera distance, display size, input or audience profile is assumed. [C-02, C-03, C-05]
-
-**Do not begin by selecting an invariant feature from habit.** First decide whether stable identity is actually required. When a scene deliberately hides identity or an appearance change deliberately changes role, the intended information contract differs. [C-02]
+The designer can name the task, distinguish role from current state, and identify what the player is legitimately expected to know. The production can author and review variants and meaningful negative examples. An owner can change a misleading style constraint rather than merely asking players to learn around it. [C-02]
+
+The pattern assumes neither a genre nor an art package. Record intended views, screen presentation, selection method, relevant vision/access needs, lighting/backgrounds, motion and language. A static image check alone is not sufficient for a role that is normally recognized through motion or a changing view. P03 camera/platform decisions remain unavailable here. [C-02]
+
+**Do not apply this to concealed roles merely because the author knows them.** It concerns distinctions the intended task makes available, not a mandate to mark every secret, threat or usable object. Offer an explicit assistance route when that is the agreed alternative task, rather than claiming the same information remained hidden. [C-01, C-06]
 
 ## Mechanism and evidence
 
-| Proposed link | Evidence status | What could break it |
-| --- | --- | --- |
-| Record required distinctions and permitted variation. | Creator practice motivates the design problem; the contract is this draft’s inference. [C-01, C-02] | The author selects a convenient feature rather than one players use. |
-| Preserve a readable relationship across combined variants. | Creator accounts identify combined-discipline and exception issues, not proof of transfer. [C-03] | View, pose, material state or another identity cue dominates. |
-| Players recognize the relevant relation and choose appropriately. | Untested end-to-end hypothesis. [C-01, C-06] | Familiarity, labels, guessing or a repeated-answer test explain performance. |
-| Novelty remains worthwhile without excessive maintenance. | Intended benefit; no measured saving or appeal guarantee. [C-01, C-05] | The constraint suppresses expression or exceptions cost more than separate designs. |
-
-Success at one link does not prove the next. A consistent family can be consistently misunderstood. A preferred variant can still miscommunicate an action. [C-01, C-06]
+The owning [Art direction topic](../topics/art-direction.md) distinguishes aesthetic preference, identity, state inference and action. Valve and Riot provide production rationales for controlled variation; neither validates this complete recipe. The pattern is an **inference to structure a local comparison**, with a hypothesized player benefit. [C-01, C-03]
+
+| Proposed causal link | Basis | Limit |
+|---|---|---|
+| Identify a task-bearing feature before varying appearance. | A reviewer can compare the intended meaning of a feature with the actual task. | This is a consistency check; it does not establish that players use that feature. [C-02] |
+| Preserve that feature across relevant variants. | Creator accounts motivate separating recognition from decorative variation. | Some identity depends on animation or context; outline is not universally sufficient. [C-03] |
+| Test role and state on unfamiliar positive and negative cases. | Different correct answers can discriminate learning from a repeated response. | This is a proposed evaluation design, not evidence of durable transfer. [C-05] |
+| Keep required facts available under chosen access settings. | XAG 103 supplies additional-channel guidance. | Availability is not demonstrated usability or equal aesthetic experience. [C-04] |
+| Adopt the least complex variant system that meets the local decision. | Extra constraints create work, so comparison must justify them. | Production savings and improved comprehension remain hypotheses. [C-01, C-05] |
 
 ## Recipe
 
-All steps are proposed design work for a separately authorized application. No assets or tests were created here. [C-06, C-07]
-
-### 1. Name what must survive and what may change
-
-Write a task-centered sentence: “Across these variants, players need to distinguish this entity/action from these alternatives under these conditions.” Separately name the aesthetic difference the variant is intended to offer. Record facts deliberately withheld.
-
-**Exit:** when no decision requires stable recognition, use ordinary art review rather than imposing this pattern. When hidden identity is the point, preserve only the action facts the scene legitimately reveals. [C-01, C-02]
-
-### 2. Identify candidate recognition features, not sacred features
-
-Record plausible features such as a form relationship, a characteristic pose, construction detail or label association. Distinguish author expectation from evidence of player use. Include alternative candidate features and negative examples.
-
-**Branch:** when identity depends on a moving pose, include motion and reduced-motion presentation in the contract; a silhouette still is not sufficient. When a feature is culturally specific or inaccessible, investigate another usable relation rather than asserting universal meaning. [C-02–C-04]
-
-### 3. Set a bounded variation envelope
-
-Specify which changes can be combined without another review and which combinations need renewed evaluation. “A new color is allowed” is incomplete when the same release also changes outline, idle pose and effects. Define permitted exceptions by purpose, not by personal preference alone.
-
-**Adjustable variables:** how much form, palette, material, accessory, pose and effect treatment changes; how many simultaneous distinctions the task requires; prior familiarity; view/lighting conditions; access settings; and exception frequency. These are not measured numerical budgets. [C-03, C-05]
-
-### 4. Select contrasting examples before expansion
-
-Choose representative base/variant pairs and plausible confusable alternatives. Include an instance that should retain identity despite a visual change and an instance that should not be grouped despite surface similarity. For action meaning, include both allowed and disallowed actions.
-
-**Exit:** when the distinction cannot be specified without contradicting the actual mechanics or intended ambiguity, stop and resolve that ownership issue. Do not author an entire family to conceal an unresolved concept. [C-02, C-06]
-
-### 5. Review the combined task presentation
-
-Specify evaluations at the actual relevant views, motion states, surface conditions and preferred settings. Keep the comparison’s task facts equivalent. Use the existing presentation and an explicit simpler aid as serious alternatives; do not intentionally weaken the comparator to favor the new variant.
-
-**Branch:** when an aid changes what the player knows, record that difference and compare it as a different design choice rather than a pure style manipulation. Required information must retain a usable route. [C-03, C-04, C-06]
-
-### 6. Test interpretation before explaining the style
-
-Ask for identity or action predictions and reasons before feedback. Counterbalance examples; separate familiar from unfamiliar users and repeat exposure. The correct answer must change when the relevant relationship changes. A series of “always select the bright object” successes cannot discriminate a more specific rule.
-
-**Exit:** when users rely only on an unintended feature, revise the contract or accept that feature explicitly if it is suitable. Do not call a failed intended mechanism successful solely because aggregate accuracy is high. [C-01, C-06]
-
-### 7. Keep, narrow, branch or remove
-
-Retain only the conditions supported by the later evidence. A specific costume or context may need an exception; a growing exception burden may justify a separate family. Compare correction and propagation effort with the artistic value, not just the first asset’s creation time.
-
-**Stop:** do not expand a version that systematically misidentifies a required entity/action or loses an essential fact in a supported access route. Uncertain results permit a reversible limited trial only under later authorization, not a claim of validation. [C-04–C-07]
+### 1. Specify the legitimate distinction
+
+Write the task question and its correct answers. Separate **identity**, **current state** and **choice preference**. For example: “This is a service cabinet; it is unavailable; I may inspect it but cannot use it now.” Define what should remain ambiguous. Do not start with a favorite palette and invent a gameplay function for it afterward. [C-02]
+
+**Exit:** when no player-facing distinction is needed, use ordinary art direction without this pattern. When discovering the role is the intended challenge, keep the hidden classification out of the visible invariants. [C-06]
+
+### 2. Identify candidate role-bearing and variable features
+
+Record the feature a player might use, its expected viewing conditions, and the evidence that it could carry the role. Separately identify freely variable features. Candidate features include characteristic form, visible arrangement, characteristic motion, placement or a task-appropriate label; they are options, not a universal priority order. [C-01–C-03]
+
+Specify at least one meaningful exception in prose: a similarly finished object with another role, or the same role in another finish. “Everything round is friendly” is not an evidence-based invariant. A historical visual association does not establish a personality or moral truth. [C-02, C-06]
+
+### 3. Build a small review comparison, not a mandatory asset quota
+
+Describe a common appearance, a deliberately contrasting variant and a plausible misleading case. Keep their actual task facts explicit in the review record. Compare preserving the candidate feature against uniform presentation and a contextual information alternative. No actual assets are produced by this research recipe. [C-05]
+
+**Branch:** when identifying a role requires a motion signature, move the comparison into the relevant action sequence with the Animation owner. Do not certify recognition from a static silhouette sheet. [C-03]
+
+### 4. Check the information route in context
+
+Plan evaluation in intended views/backgrounds/lighting and with relevant alternative presentations. Determine whether role and state survive chosen settings without adding forbidden information. Another shape or icon is still a visual route; it does not provide nonvisual access. [C-04, C-05]
+
+**Exit:** when the candidate feature cannot carry an essential fact reliably in the supported context, replace or supplement it with an appropriate information route. Do not keep intensifying decoration automatically. When the alternative changes the task’s available information, document that change explicitly. [C-04, C-06]
+
+### 5. Freeze invariant, variation and exception ownership
+
+Record the chosen role-bearing relationship, permissible variation, exceptions, context limits and person/team responsible for adjudicating conflicts. This can be a short annotated specification; the pattern does not demand an elaborate style bible. Review animation, interface and effects when their changes alter the relationship. [C-02]
+
+**Adjustable variables:** explicitness of role indication; surface/detail variation; amount of contextual assistance; reliance on motion; similarity of negative examples; exposure before transfer; view/lighting range; maintenance effort. Values require local justification. No number of colors, silhouette ratio, material count, contrast setting or production saving is recommended. [C-05]
+
+### 6. Compare, narrow or remove
+
+After separate study authorization, test unfamiliar instances with different correct classifications and availability states. Measure recognition and state inference before preference. Retain the contract only within contexts where it contributes enough to justify its constraints; simplify when added bureaucracy or disclosure costs exceed demonstrated value. [C-01, C-05]
+
+**Stop:** unresolved critical-information failures, unintended disclosure of the core task, or inability to maintain a claimed invariant blocks recommending deployment of that version. A clearly bounded art preference may still be chosen locally, but it must not be relabeled validated gameplay knowledge. [C-06]
 
 ## Worked examples
 
-### Illustrative — inspection tools across visual themes
-
-**Not a shipped-game observation or tested design.** A tool family appears in several environment themes. The player must distinguish the inspection tool from a container, and a ready tool from a disabled one. The new theme changes surface finish and casing shape. [C-06]
-
-Apply the recipe by recording the preserved tool/action distinction, then compare possible common features such as its operating form and state indication. Do not presume the old paint color is the recognition mechanism. Include a container in that color and the tool in another color; include ready and disabled examples with the same material. Ask what each object is and what action is currently possible before giving feedback. [C-02, C-03, C-06]
-
-If the relevant state is lost at the task view, decide between revising the form, retaining a more explicit state aid or narrowing the variant. The artistic goal may survive a shape change while a particular accessory does not; the contract should permit that supported exception. Document whether the repair adds work to every later variant. None of these outcomes was observed here. [C-03–C-06]
-
-### Illustrative counterexample — transformed role
-
-A character’s transformed appearance deliberately signals that its former role is no longer valid. Preserving the old role cue perfectly would mislead rather than help. Revise the invariant from “same role” to whatever identity or action fact remains legitimate, or do not use this pattern for the transformation. [C-02, C-06]
+### Illustrative: differently finished service cabinets
+
+**Invented; not implemented or tested.** A workshop contains cabinets made by several artisans. The task is to find service equipment, determine availability and decide whether to use it. The proposed invariant is a recognizable service-facing arrangement plus an accessible state presentation. Finish and ornament can differ. A decorative cabinet can share materials without acquiring a service role. [C-05]
+
+| Review record | Candidate treatment | Discriminating check |
+|---|---|---|
+| Familiar service cabinet, available | Known arrangement, locally appropriate finish, available state. | Identify role and current permission separately. |
+| Unfamiliar service cabinet, unavailable | Different finish; same role relationship; unavailable state. | “Looks unfamiliar” must not force the wrong role; familiar role must not imply availability. |
+| Decorative cabinet | Similar finish, no service-facing arrangement or service status. | Detect false-positive classification rather than only successful use. |
+| Access presentation | Appropriate alternative describing required role/state facts. | Confirm comprehension with actual users; do not infer emotional equivalence. |
+
+If B is identified correctly but the player chooses not to use it, ask for their reason. Preference is not a classification error. If every transfer trial’s correct action is “use,” redesign the test: a repeated response would otherwise appear successful. This directly preserves the selected F01 transfer-discrimination correction. [C-05]
+
+### Illustrative: deliberate environmental contrast
+
+A shared world contains two craft traditions with different geometry and surface treatments. The design need not erase their difference. Specify what connects them at the world level, and only preserve role-bearing features where the task requires cross-region recognition. An unfamiliar artifact whose purpose is deliberately being investigated is excluded until that purpose is learned or assistance intentionally exposes it. No culture-wide preference is asserted. [C-01, C-06]
 
 ## Tradeoffs and alternatives
 
-The hypothesized benefit is consistency of a required association, not guaranteed elegance or reduced cost. Constraints can help review repeated variants but restrict artistic exploration; exceptions can preserve identity but multiply maintenance. Consider a separate visual family, an explicit identifier, fewer variants, a stronger base distinction or no extra rule. A label is not aesthetically neutral, but neither is an elaborate surface code. [C-01, C-05]
-
-Access-related cue choices remain a separate evaluated dependency. This pattern cannot replace nonvisual information merely by improving a silhouette or material. Reusing the same source account and repeating its references do not increase confidence in the recipe. [C-04]
+The contract can constrain artists, increase review work and make discoveries too explicit. It can also leave useful variation untouched instead of forcing a single palette on every contributor. Both are proposed consequences to evaluate, not measured production savings. Alternatives include a small set of reference examples, uniform presentation, a reliable contextual label, an inspect action, a chosen assistance mode, or no added distinction. [C-01, C-02, C-05]
+
+An explicit label may be cheaper and clearer but can demand reading/localization. A motion signature may suit the actor but disappear in still views or reduced motion. Surface distinctions may be expressive but fail in some lighting. Those dependencies justify testing the actual task, not declaring one cue type best. [C-02–C-05]
 
 ## Failure cases
 
-| Warning sign | Candidate diagnosis | Response to test |
-| --- | --- | --- |
-| New appearance is attractive but grouped with the wrong entity. | Distinctive changes altered the required association. | Restore a suitable relationship, add a contextual identifier or revise the grouping. |
-| The family works only for expert reviewers. | Knowledge of names/roles substitutes for the visible relation. | Narrow the claim to practiced users or redesign unfamiliar-use support. |
-| Every test item has the same correct response. | The evaluation rewards a shortcut. | Add matched contrary cases and test prediction before feedback. |
-| A variant fails only in motion or at a supported setting. | Isolated asset approval missed a combination. | Reopen review for that combination; do not declare the whole family validated. |
-| Exception patches dominate production. | The shared family is broader than the useful commonality. | Branch, simplify or stop additional variants. |
-
-All failure signs and repairs are prospective hypotheses, not P04 findings. [C-03–C-06]
+Misidentification concentrated in one skin or region suggests the contract may not survive that context. Correct role recognition with wrong availability suggests role and state were collapsed. Correct artist predictions but poor unfamiliar-user performance suggest expert knowledge was mistaken for visibility. High liking paired with more task errors is a tradeoff, not an unconditional success. These are hypotheses about diagnostic signs. [C-05]
+
+Proposed repairs are to narrow the invariant, reduce nonessential competing detail, make state explicit, change the information route, or abandon the pattern. An unresolved accessibility failure is not repaired by claiming the same style should be learned through effort. [C-04–C-06]
 
 ## Counterexamples and do not use conditions
 
-Do not require stable identity when deliberate disguise, reinterpretation or role change is the intended information structure. Do not preserve a culturally loaded feature merely because the production finds it convenient. Do not use the pattern to make inaccessible task facts someone else’s responsibility. It is also unnecessary for an isolated artwork without repeated identity/action obligations. [C-02, C-04, C-06]
-
-The strongest opposing case is that explicit labeling or a different family performs the task more clearly with less maintenance while leaving artists freer. The inspected sources do not defeat that alternative. The added constraint bears the burden of demonstrating useful local value. [C-01, C-05]
+The strongest countercase is a task whose central decision is inferring an object’s role from ambiguous evidence. A universal role mark would supply the answer. Another is a small production where a few consistent examples already produce adequate recognition and a maintained contract adds overhead without benefit. [C-06]
+
+Do not use this as a fixed silhouette rule, a morality/personality code, a mandate for maximum contrast, a formal accessibility standard, or permission to copy a successful game’s art. Do not assume a declared invariant is a measured player invariant. [C-03, C-04, C-06]
 
 ## Playtest
 
-**PROPOSED — NOT RUN.** Compare existing, constrained-variation and simpler explicit-aid alternatives under the same task rules. Include confusable alternatives, changes that should preserve meaning and changes that should alter the correct response. Record differences in assistance and presentation rather than treating them as pure style effects. [C-06]
-
-Use actual target views/settings and participants with relevant familiarity and access routes. Counterbalance examples and ask predictions before feedback. Measure mistaken identity/action classifications, reliance on unintended features, correction behavior, style-fit/appeal separately, and authoring/revision effort. Familiarity, learning, lighting, simultaneous art changes and experimenter cues are confounds.
-
-Reject or revise when the variant systematically miscommunicates a necessary distinction or makes a fact unavailable in a supported access route. Reject the intended mechanism when success comes from a shortcut the contract did not preserve. Retain only a tested scope when artistic value and maintenance tradeoffs meet the study owner’s predeclared local decision criteria. An inconclusive result is not equivalence. The future owner must determine sample rationale and practical tolerances before testing; this draft supplies no power guarantee or universal numerical cutoff. [C-01, C-04–C-06]
-
-## Claim ledger
-
-Claim IDs are local to this entry. Confidence describes the exact scoped wording, not a source’s prestige or the recipe’s overall efficacy. Proposed procedures and examples are not approved studio decisions.
+**PROPOSED — NOT PERFORMED.** The owning topic contains the full protocol. Compare uniform presentation, selective role-preserving variation, and contextual information assistance. Match task facts, input/view/exposure where possible and log unavoidably changed visual properties. [C-05]
+
+Recruit relevant unfamiliar and experienced users and actual access users after authorization; justify sample size and precision before recruitment. Counterbalance order/family where feasible. Test first use, repeated use and unfamiliar transfer, including true and false cases with different correct answers. Ask identity, availability and chosen action separately. Record error types, comprehension, assistance, preference, comfort and production work without collapsing them into one quality score. [C-05]
+
+Reject or narrow the claim if the selective system increases consequential errors, discloses a legitimate unknown, fails under chosen settings or only works on memorized examples. Prefer a simpler option when added value remains unestablished at the project’s predeclared uncertainty tolerance. A nonsignificant difference is not equivalence. Critical information failures block advancement; participant withdrawal ends the session. No acceptance threshold has been approved in this draft. [C-05, C-06]
+
+## Claim ledger and sources
 
 ### C-01
-
-**Claim:** A bounded variation contract may preserve required recognition while leaving room for a meaningfully different appearance. **Class:** `hypothesis`. **Confidence:** low for end-to-end effectiveness; no direct test of this recipe.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-002, Filling Up Buckets; GDR-SRC-20261010-P04-003, Preparing the Ponytail; owning art-direction C-03/C-04/C-08.
-
-**Applicability, contrary evidence and unresolved question:** Creator goals motivate the comparison, not a verified benefit. One invariant set need not transfer to every task, view or audience.
+**Claim:** Preserving task-bearing relationships while permitting variation is a candidate method, with unestablished local benefit. **Class:** `inference`. **Support:** owning topic C-07; GDR-SRC-20261010-P01-13 §§3–4.3; GDR-SRC-20261010-P04-001 recognition/variation passages. **Confidence:** moderate for a defensible comparison, low for efficacy. **Unresolved:** comparison with simpler guidance; no complete-pattern study.
 
 ### C-02
-
-**Claim:** The invariant should be the required identity/action distinction, not automatic preservation of every shape or accessory. **Class:** `inference`. **Confidence:** moderate for the contextual argument.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-002, Silhouettes; GDR-SRC-20261010-P04-003, Preparing the Ponytail; owning art-direction C-08.
-
-**Applicability, contrary evidence and unresolved question:** Exceptions and intentional ambiguity matter. Cosmetic sameness is not sufficient evidence of usable recognition.
+**Claim:** A review record should separate role, state, permitted variation, context and ownership. **Class:** `inference`. **Support:** owning topic C-01/C-08/C-10; original synthesis, not a published standard. **Confidence:** moderate for consistency checking. **Limit:** extra process may be unnecessary. **Unresolved:** minimum useful record and actual cost.
 
 ### C-03
-
-**Claim:** Review variation as a combination of model, material, pose, view and effects rather than assuming approval of each isolated asset proves the combination. **Class:** `inference`. **Confidence:** moderate as risk-control logic; no measured savings.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-002, Filling Up Buckets; GDR-SRC-20261010-P04-003, Making Skins with Style.
-
-**Applicability, contrary evidence and unresolved question:** Not a required asset count or standard checklist. P03’s actual view/device constraints remain missing.
+**Claim:** Creator accounts motivate controlled variation but do not make static silhouette sufficient in every case. **Class:** `practitioner-heuristic`. **Support:** GDR-SRC-20261010-P01-13 §§4.1–4.3 and GDR-SRC-20261010-P04-001 Silhouettes. **Confidence:** high for attribution. **Limit:** historical production accounts, no comparative game trial. **Unresolved:** actual recognition features across variants/views.
 
 ### C-04
-
-**Claim:** Access to a required fact must not silently disappear when a style variant or preferred presentation setting changes. **Class:** `inference`. **Confidence:** moderate as a guidance-to-design constraint.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-010, alternatives to color/visual-only information; reviewed P01/P02 cue boundaries.
-
-**Applicability, contrary evidence and unresolved question:** Availability is not demonstrated usability or emotional equivalence. This pattern does not replace the existing cross-channel cue recipes.
+**Claim:** Required facts need appropriate access channels, with usability and emotional effects evaluated separately. **Class:** `inference`. **Support:** GDR-SRC-20261010-P01-05 Implementation guidelines; owning topic C-06/C-09. **Confidence:** moderate for the application bridge. **Limit:** two visual features are not nonvisual access; no certification. **Unresolved:** accessible implementation and interpretation.
 
 ### C-05
-
-**Claim:** Variant reuse and exception handling should be evaluated as separate production costs rather than assumed to save effort. **Class:** `inference`. **Confidence:** moderate for the categories; cost magnitude unknown.
-
-**Support / precise locator:** GDR-SRC-20261010-P04-003, Base Meshes and 3D Sustainability / Making Skins with Style.
-
-**Applicability, contrary evidence and unresolved question:** No universal shared-rig, asset-count or staffing recommendation. A justified separate family can outperform escalating exceptions.
+**Claim:** The recipe, variables, invented examples and validation procedures are proposed, not tested. **Class:** `hypothesis`. **Support:** original P04 synthesis; inspected F01 selected transfer pattern, examples/transfer-correction passage. **Confidence:** low for eventual value. **Limit:** no participant, prototype, fixed threshold or cost measurement. **Unresolved:** authorized study and discriminating unfamiliar cases.
 
 ### C-06
-
-**Claim:** The worked cases, comparison procedure and rejection rules are proposed, not executed or approved. **Class:** `hypothesis`. **Confidence:** low for local outcome and feasibility.
-
-**Support / precise locator:** Original P04 recipe synthesis; art-direction C-13; reviewed F01 supported-attempt-and-transfer-check correction used for contrasting-response test structure.
-
-**Applicability, contrary evidence and unresolved question:** No assets, observations of players, instrumentation or approvals. Predictions before feedback can expose a mapping failure but do not alone prove learning.
+**Claim:** Exclude hidden-role discovery and stop when essential facts or meaningful task uncertainty cannot be preserved. **Class:** `inference`. **Support:** owning topic C-07/C-11/C-13 and explicit task contract. **Confidence:** moderate as a scope boundary, not universal preference. **Unresolved:** whether an assistance route changes the agreed task acceptably.
 
 ### C-07
-
-**Claim:** This candidate is bounded P04 research and remains unreleased with provisional identities. **Class:** `studio-decision`. **Confidence:** high from the explicit dispatch.
-
-**Support / precise locator:** Doug’s P04 message and attached brief, Assigned outputs and Current jobs and boundaries.
-
-**Applicability, contrary evidence and unresolved question:** No rights, adoption, permanent allocations, repository changes, implementation or participant work are authorized.
+**Claim:** This is an authorized draft research artifact only. **Class:** `studio-decision`. **Owner/date:** Doug; supplied P04 brief, 2026-10-10, Assigned Outputs and boundaries. **Confidence:** high. **Limit:** no release, permanent allocation, assets or tests authorized. **Unresolved:** later review and adoption decisions.
 
 ## References
 
-All public records below were inspected in the stated passages on **2026-10-11 UTC**. IDs are P04-scoped source records, not permanent SRC allocations. Dates of older works are publication dates, not claims of current game behavior. Repeated reference records support standalone reading; they are not extra evidence.
-
-### GDR-SRC-20261010-P04-002
-
-**bananaband1t, Riot Games.** [Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/). **Publisher:** Riot Games / League of Legends. **Publication/update:** 2021-03-12. **Edition/build:** Dated developer article; game build unspecified; historical account, not current patch verification.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Primary creator account / practitioner guidance. **Exact locators:** The Unbreakable Vows; Silhouettes; Filling Up Buckets; Cosmetic Animations. **Claims supported in this entry:** C-01–C-03.
-
-**Limits:** Describes Riot goals and constraints, not comparative player outcomes. Media not played. The skin-variation metaphor is not a measured budget or a universal invariant. **Independence/deduplication:** Same studio and game family as source 003: not independent corroboration of efficacy. Cross-batch URL/edition deduplication pending. **Rights:** Reuse license not established; attributed paraphrase only.
-
-### GDR-SRC-20261010-P04-003
-
-**ASU Team, Riot Games; named concept, character, technical-art and animation contributors.** [/dev: Modernizing the Monk](https://www.leagueoflegends.com/en-gb/news/dev/dev-modernizing-the-monk/). **Publisher:** Riot Games / League of Legends. **Publication/update:** 2024-04-08. **Edition/build:** Lee Sin art-and-sustainability update developer article; exact game build unspecified.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Primary multidisciplinary creator account. **Exact locators:** Creating Consistency Across Skins; Preparing the Ponytail; Base Meshes and 3D Sustainability; Animation → Making Lee’s Animations More Impactful, Float like a Butterfly, Sliding Hitboxes like a Lee, Making Skins with Style. **Claims supported in this entry:** C-01–C-03, C-05.
-
-**Limits:** Intentions and reported production issues, not measured satisfaction, cost savings or a directly observed build. Animation contributors: Sean “Riot Redepoka” Yeung and Einar “Riot Beinhar” Langfjord. Embedded media not played. **Independence/deduplication:** Same production line as source 002; multiple contributors are not separate efficacy studies. Cross-batch deduplication pending. **Rights:** Reuse license not established; paraphrase only; no likenesses, media or assets copied.
-
-### GDR-SRC-20261010-P04-010
-
-**Microsoft.** [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103). **Publisher:** Microsoft Learn. **Publication/update:** Last updated 2026-03-04; original publication unknown. **Edition/build:** Unnumbered live page revision inspected on evidence-check date.
-
-**Access:** `relevant-excerpt`; checked 2026-10-11 UTC. **Source type:** Official vendor accessibility guidance. **Exact locators:** Goal and Overview; Implementation guidelines → alternatives to color and visual-only information; simulation-filter and actual-player evaluation paragraphs. **Claims supported in this entry:** C-04.
-
-**Limits:** Practitioner guidance, not a formal standard, legal advice or certification. Availability of an alternative is not demonstrated usability or emotional equivalence. Public body inspected despite authorization boilerplate. **Independence/deduplication:** Same document as reviewed GDR-SRC-20261010-P01-05 and GDR-SRC-20261010-P02-005; central reconciliation pending. Same issuer as source 011. **Rights:** Vendor page; content reuse license not inspected; paraphrase only; no example media copied.
+All records below were inspected in relevant passages on 2026-10-10. Source IDs retained from P01 are explicit reuse, not new allocations. New P04 IDs are temporary; central URL/DOI/edition reconciliation remains pending. Document copies and candidate citations do not provide independent corroboration.
+
+### GDR-SRC-20261010-P01-13
+
+**Jason Mitchell, Moby Francke and Dhabih Eng. [Illustrative Rendering in Team Fortress 2](https://cdn.cloudflare.steamstatic.com/apps/valve/2007/NPAR07_IllustrativeRenderingInTeamFortress2.pdf).** Valve / NPAR 2007. Date: 2007; exact publication day unknown. Edition/build: 2007 paper; described game build unspecified.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand production/technical paper. **Locators:** §§3, 4.1–4.3; PDF pp. 2–3, Figures 2–5. **Supports:** C-01/C-03, production rationale only.
+
+**Limits:** One production account, not a player experiment. PDF figures inspected, not game footage. **Relationship:** Same work as P01-13; former steamcdn-a.akamaihd.net route is a host alias, not corroboration. **Rights:** Reuse permission not established; paraphrase only; figures not redistributed.
+
+### GDR-SRC-20261010-P04-001
+
+**bananaband1t / Riot Games. [Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/).** Riot Games. Date: 2021-03-12. Edition/build: Developer article; example build numbers unspecified.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand development account. **Locators:** Silhouettes; Matching Hitboxes; Hierarchy; Minimizing Noise; Clarity in Action (Jhin, Taliyah, Leona and Renekton cases). **Supports:** C-01/C-03, recognition exception only.
+
+**Limits:** Creator-reported practices and problems; no footage watched or controlled outcome data. **Relationship:** Independent production from Valve; retrospective selection and issuer incentives remain. **Rights:** Reuse license not established; paraphrase only.
+
+### GDR-SRC-20261010-P01-05
+
+**Microsoft. [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103).** Microsoft Learn. Date: Last updated 2026-03-04. Edition/build: Unnumbered live page revision checked 2026-10-10.
+
+**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance. **Locators:** Goal; Implementation guidelines; Visual cues; Color and additional sensory channels. **Supports:** C-04, guidance-to-application inference.
+
+**Limits:** Guidance, not a formal standard, compliance certificate or evidence of emotional equivalence. **Relationship:** Reuses inspected P01-05; P02-005 duplicates this URL. Central deduplication pending. **Rights:** Reuse license not inspected; paraphrase only.
 
 ## Related entries and history
 
-Owning topic: [Art direction — GDR-CAND-20261010-P04-TOP-01](../topics/art-direction.md). Complement: [Animation and performance](../topics/animation-and-performance.md) and [State-aligned animation handoff](state-aligned-animation-handoff.md) when movement carries an identity or action distinction. Existing P01/P02 cue-pattern ownership and overlap are retained in the [dependency record](../reviews/full-run-20261010-p04-review-packet.md#reviewed-dependency-transfer); no genre content is copied.
-
-P04-CON-01 retains recognition versus deliberate ambiguity. This pattern does not resolve it by treating one genre promise as dominant. Broader material/context validation is a queued child-work request, not a third pattern in this packet.
-
-**2026-10-11 UTC:** initial 0.1.0 draft, initial-draft-1; no predecessor or supersession. Author self-review only. Independent review, source/identity reconciliation, host testing and release remain pending. No implementation or asset rights are conferred.
+Owner: [Art direction — GDR-CAND-20261010-P04-TOP-01](../topics/art-direction.md). Complement: [Action-phase and interruption contract](action-phase-and-interruption-contract.md), when a variant’s movement carries identity. P01 general visual communication and P01/P02 redundant-cue work remain separate inspected dependencies, not additional bundled patterns. Their overlap is not resolved here.
+
+**2026-10-10:** initial P04 pattern, version 0.1.0 / initial-draft-1; predecessor and supersession null. Current claims are inference/hypothesis-led. Same-author self-review completed; P04 independent review not performed. No release, adoption, asset production, playtest or Project/repository change. [C-07]

```

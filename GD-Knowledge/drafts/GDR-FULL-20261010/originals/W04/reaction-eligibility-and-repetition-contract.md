---
id: GDR-CAND-20261010-W04-PAT-02
kind: pattern
title: Reaction eligibility and repetition contract
version: 0.1.0
status: draft
owner_project: BH-GDR-Worlds-and-Characters
run_id: GDR-FULL-20261010
batch: W04
candidate_revision: initial-draft-1
attempt_id: W04-initial-1
updated: '2026-10-10'
evidence_checked: '2026-10-10'
coverage_status: open
aliases:
- reaction continuity contract
- repeated acknowledgment
- expired narrative reaction
tags:
- reaction
- eligibility
- repetition
- persistence
- attribution
- conditional-pattern
- hypothesis
related_topics:
- GDR-CAND-20261010-W04-TOP-02
- GDR-CAND-20261010-W04-TOP-01
related_patterns:
- GDR-CAND-20261010-W02-PAT-01
- GDR-CAND-20261010-W04-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-W02-005
- GDR-SRC-20261010-W04-003
- GDR-SRC-20261010-W04-002
permanent_id: null
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded W04 candidate; no prior batch replaced.
byte_hash_record: ../reviews/full-run-20261010-w04-review-packet.md#artifact-byte-manifest
---

# Reaction eligibility and repetition contract

**Draft research candidate; not released or approved guidance.** All examples marked illustrative are invented, not studio canon. No game, engine, prototype, participant study or player test was run. Recommendations are conditional inferences or hypotheses, not formal standards.

## Purpose

Help an author preserve the meaning of a relevant occurrence when a later response is selected, delayed, repeated, interrupted or revisited. The intended result is an acknowledgment appropriate to the accepted history, without accidental repeated commitments or stale claims. The contract does not promise more engaging dialogue, stronger agency or a particular implementation architecture. Its preventive and player-facing benefits remain hypotheses. [C-01]

This pattern is distinct from W02’s **Intent and response contract**, which concerns what the player makes a protagonist say or do. W04’s pattern concerns **which history a later acknowledgment refers to and whether it still applies**. It can operate after a nonverbal action, an external event or a return to play; it does not require a selectable line. [C-02]

## Context and prerequisites

Use when an experience promises a consequence-sensitive reaction across more than one supported history. Identify the relevant occurrence, the response’s purpose, its speaker or presentation perspective, and its repetition/persistence horizon. Distinguish a factual acknowledgment from an intentionally mistaken belief. [C-02, C-03]

A team that cannot identify what the reaction means should not first choose a more sophisticated selection policy. Clarify or narrow the promise, write a fixed exchange, use a truthful neutral response or omit the reaction. None is universally preferable; the important requirement is not pretending a response recognizes something it does not support. [C-01, C-02]

| Prerequisite | Question to resolve | Exit when absent |
|---|---|---|
| Identifiable occurrence | What happened, who acted, and what consequence was accepted? | Remove premature specificity or resolve the missing design meaning. |
| Supported histories | Which orderings, interruptions and alternate actors are actually allowed? | Narrow the scenario rather than assert unsupported combinations work. |
| Attributed perspective | What can this speaker reasonably know, believe or intentionally misstate? | Use an appropriate perspective or leave the response unapproved. |
| Defined repeat/expiry scope | What can recur and what makes the response stale? | Avoid irreversible consequences from a merely repeated acknowledgment. |
| Feasible diagnostic context | Can an author explain why a response should or should not apply? | Prefer fewer variants and a smaller persistence promise. |

These are conceptual prerequisites and proposed quality checks, not required software components or a formal standard. [C-02, C-06]

## Mechanism and evidence

| Proposed link | Evidence and classification | Remaining uncertainty |
|---|---|---|
| Distinguishing query from selection exposes an unsafe conflation. | Yarn’s official documentation explicitly separates those operations. [C-04; GDR-SRC-20261010-W02-005] | Documentation does not show that every team makes the mistake or that this pattern prevents it. |
| Defining the accepted occurrence and perspective makes an acknowledgment checkable. | A logical relationship between the contract and its proposed trace. [C-03, C-06] | The authored contract can itself be wrong; it is not an independent truth oracle. |
| Including repetition, expiry and alternate-order cases reveals plausible failures. | Larian’s patch report supplies production examples motivating such cases. [C-05; GDR-SRC-20261010-W04-003] | W04 did not reproduce the defects or establish root causes. No claim that this recipe would have prevented those particular bugs. |
| Defining persistence scope can clarify the expected resumed history. | ink documents story save/load alongside external interaction facilities. [C-07; GDR-SRC-20261010-W04-002] | The document does not certify whole-game continuity, and no implementation was run. |
| A correct, visible acknowledgment improves understanding or trust. | W04 outcome hypothesis. [C-01, C-10] | A correct line can still be irrelevant, intrusive, confusing or unwanted. Silence or a fixed response may be better. |

The recipe is a synthesis of narrow documentation observations, production reports and design reasoning. It is not an experimentally established debugging system, a one-time-trigger mandate or a claim that more reactivity always improves narrative. [C-01]

## Recipe

1. **Name the occurrence and accepted result.** Record the actor, recipient, relevant object/situation and what changed. Distinguish asking, offering, accepting, attempting, completing and reporting. Use ordinary language; no runtime schema is prescribed. [C-03]
2. **Identify perspective and uncertainty.** State what the response can assert, what the speaker believes and what should remain unresolved. Do not convert exposure into certified human knowledge. [C-03]
3. **Define when the response applies.** List material preconditions, including whether the event may happen before a formal request and whether another actor can cause it. A line thanking the player is not interchangeable with a neutral acknowledgment of the result. [C-05, C-06]
4. **Define repetition by occurrence, not only by text.** A useful recap may repeat information about one accepted transaction without repeating the transaction. A new legitimate transaction may deserve the same words. Scope any “once” condition to the intended occurrence or horizon. [C-04, C-06]
5. **Define expiry and contradiction treatment.** Specify what later changes invalidate a queued response. An invitation can expire; a later correction may replace a report. For genuinely conflicting events, ask the design owner to establish their meaning; do not silently impose universal newest-wins precedence. [C-06]
6. **Define no-selection and fallback.** Decide whether silence, neutral acknowledgment, explicit unresolved state or another response fits the promise. A generic congratulation is not a safe substitute for a refusal or failure. [C-04, C-06]
7. **Describe interruption and return.** Trace the history before commitment, after acceptance but before acknowledgment, after acknowledgment and after a deliberate restore/reset. State what the player should encounter, including any intentional rewinding. This is a design requirement, not a serialization design. [C-07]
8. **Make the author’s questions answerable.** Prepare a readable history with reasons a response is eligible or ineligible, what was selected, and what consequence it is intended to acknowledge. Include relevant language/content version context; do not collect sensitive player data merely to fill a diagnostic view. [C-08, C-09]
9. **Compare and stop when unjustified.** Evaluate the proposed contract against a smaller fixed or lightly reactive alternative. Retain it only if the consequential distinctions justify its maintenance and the later player-facing result survives review. [C-10]

### Adjustable variables

The author can vary specificity of acknowledgment, repetition horizon, expiry conditions, perspective, fallback, visibility, scope of retained history and number of materially distinct cases. None has a universal numerical setting. Longer memory and more specific references create additional obligations rather than guaranteed depth. Deliberate unreliable accounts require perspective-specific treatment, not a blanket exemption from consistency. [C-03, C-06, C-08]

### Exit conditions

Stop when the occurrence cannot be defined, the history cannot be supported, the response relies on unavailable knowledge, or an irreversible consequence would be triggered merely by replaying acknowledgment. Narrow or remove the response while the design question is unresolved. Also stop expanding the contract when it causes more inconsequential bookkeeping than useful diagnosis. Do not silently flatten a deliberately uncertain account into omniscient narration. [C-02, C-03, C-10]

## Worked examples

### Illustrative: deposit and archive permit

A traveler accepts a deposit requirement and receives permission to consult an archive ledger. A steward later acknowledges the agreement. The invented promise is that one accepted deposit grants the stated access, not that every display of the acknowledgment charges the player again. No code, prototype or save was executed. [C-11]

**Occurrence:** the deposit is accepted under the offered terms. **Perspective:** the steward can know a valid permit exists, but cannot claim to have personally issued it when another official did so. **Reaction purpose:** confirm access, not demand another agreement. **Expiry:** revocation or the agreed end of access changes what can be said. **Repetition:** a recap may remain useful, but it refers to the same agreement. **Return:** after restoring a history with the deposit accepted, acknowledgment does not create a new deposit; restoring an earlier history follows that earlier history’s declared rules.

| Case | Proposed response treatment | Distinction protected |
|---|---|---|
| Player asks about terms but declines | No valid-permit acknowledgment; a neutral offer can remain. | Inquiry is not acceptance. |
| Accepted deposit, acknowledgment interrupted | Appropriate continuation or recap without a second payment occurrence. | Accepted result differs from the display of confirmation. |
| Duplicate report of the same acceptance | Repeated information may be allowed; repeated cost is not implied. | Text repetition differs from repeated commitment. |
| Alternate official granted the permit | Recognize valid access without false personal credit. | Result differs from actor attribution. |
| Revocation precedes a delayed invitation | Suppress or revise the stale invitation. | Past eligibility is not current eligibility. |
| Steward is intentionally suspicious | An attributed suspicious line may coexist with valid access. | Belief differs from operational fact. |

A later prototype comparison should include **legitimately repeatable** interactions as well as accidental repeats. Otherwise a system that suppresses everything after the first acknowledgment can appear correct while breaking intended use. Similarly, a neutral acknowledgment is not automatically sufficient when the player needs to understand a revoked permit. The correct response depends on the declared purpose.

### Illustrative: repair completed before request

A player repairs a public signal before meeting the person who would have requested the repair. If the design accepts that supported route, the later character can recognize the completed result without pretending a prior meeting occurred. If witnessing the request or using a specific method is essential to the local goal, the contract should say so instead. This adapts the inspected W02 outcome-versus-means distinction; it does not turn every objective into an outcome-only check. [C-03, C-11]

## Tradeoffs and alternatives

A fixed scene can be clearer than context selection when only one history matters. A neutral response can avoid unsupported detail but may fail to acknowledge a consequential choice. Silence can avoid interruption but can also hide a broken promise. Specific reactions can preserve a valued distinction while creating more continuity, performance and localization work. No inspected source supplies a universal optimum or quantified savings for this tradeoff. [C-01, C-06, C-08]

This pattern does not replace consequence-preserving reconvergence, multi-route objectives or speech-act wording review. It handles the narrower acknowledgment obligation after those techniques create a relevant history. It also does not prescribe event ordering technology, state ownership, storage transactions or an engine tool; those require a separate implementation process and approvals.

## Failure cases

**All repeats suppressed:** useful greetings, practice and recaps disappear. Correct by identifying the legitimate repeated occurrence and horizon. **Late truth presented as current:** a once-valid invitation appears after revocation. Correct the expiry meaning or change the response, not merely its wording. **Wrong actor thanked:** the result is recognized but credit is misassigned. Inspect actor and perspective separately. [C-05, C-06]

**Correct selection, wrong implication:** the line meets eligibility conditions but implies an unaccepted commitment or reveals hidden information. Use the adjacent W02 wording review and the topic’s fact/belief distinction. **Debug record becomes canon:** an unresolved authoring note is treated as a confirmed world fact. Keep unknowns and hypotheses explicit. **Locale changes the act:** a recap reads as a new request or an offer becomes an acceptance. Review full context, not isolated strings. [C-03, C-08, C-09]

**Architecture inferred from a patch note:** a documented defect is attributed to a particular data structure without evidence. Stop that inference. The source supports an adversarial case to consider, not an implementation diagnosis. [C-05]

## Counterexamples and do not use conditions

An intentionally amnesiac character may fail to remember the player, and an unreliable narrator may contradict an earlier account. Do not “repair” those cases into total memory and objective truth unless that is the actual design decision. Instead, define the intentional perspective and check whether unrelated promises still hold. [C-03]

A brief fixed vignette may not justify a reactive persistence contract at all. More fields and explanatory traces can distract an author from the actual writing problem. The strongest counterproposal is a narrow authored sequence whose limitations are clear. This pattern should be rejected for that use when it adds no consequential diagnostic value. [C-02, C-10]

## Playtest

**Proposed, not performed.** Separate three later activities: author diagnosis, implementation continuity checks and player comprehension. They answer different questions and none certifies the other two. [C-10]

For author diagnosis, use comparable bounded scripts with deliberate example mismatches and valid exceptions. Compare the contract with a simpler scene summary. Include correct repeatable reactions, correct silence and intentionally unreliable speech alongside incorrect repeats and stale claims. Track detected consequential errors, false positives, missed cases, elapsed effort and maintenance costs. Counterbalance exposure or use matched cases; familiarity with a revealed answer otherwise contaminates comparison.

For a later authorized prototype, test ordinary order, early completion, alternate actor, repeated notification, interrupted acknowledgment and restored history. Check **accepted consequences and attribution**, not just whether a line appeared. No such test ran in W04, and these descriptions do not choose a runtime mechanism.

For player comprehension, ask what changed and why without supplying the contract. Record confusion, preference, unwanted interruption and perceived recognition separately. Reject or narrow the pattern when a simpler approach preserves the same valued distinction at lower burden, or when the added specificity repeatedly misleads supported audiences. Define local acceptable-error and effort boundaries before testing; no numerical universal or sample-size guarantee is given. A changed acceptance rule is an adaptation probe, not same-rule transfer; nonsignificance alone is not equivalence.

## Claim ledger and sources

| ID | Claim and class | Support / limits | Confidence and unresolved question |
|---|---|---|---|
| C-01 | The assembled contract may improve continuity and understanding; benefit is not established. `hypothesis` | W04 synthesis of C-03–C-07. | Low for efficacy; fixed or quieter alternatives may be better. |
| C-02 | This pattern concerns occurrence/history acknowledgment, not the speech act selected by the player. `inference` | Inspected W02 intent pattern purpose/recipe; W04 scope. | High for scope distinction; duplication requires independent review. |
| C-03 | Accepted facts, perspective, exposure and commitment are different concepts. `inference` | Inspected W01/W02 candidate distinctions; W04 examples. | High for non-equivalence; no optimal representation established. |
| C-04 | Yarn documents query/selection separation and no-selection. `observed-example` | W02-005, Saliency / Creating Custom Saliency Strategies. | High for documentation; unpinned and not executed. |
| C-05 | Larian’s historical patch report motivates adversarial attribution/repetition/history cases. `observed-example` | W04-003, named fix bullets. | High for report existence, not reproduced game behavior or root cause. |
| C-06 | Explicit repeat/expiry/fallback meanings may expose faulty acknowledgments. `hypothesis` | C-03–C-05 motivate the recipe, not its efficacy. | Low; valid repetition and ambiguity can be overcorrected. |
| C-07 | A meaningful persistence boundary needs more than assuming that a documented story-save facility covers every surrounding circumstance. `inference` | W04-002, Saving and loading and external interactions. | Moderate; actual implementation scope not investigated. |
| C-08 | Author-visible reasons and bounded scope may aid diagnosis at an unmeasured maintenance cost. `hypothesis` | W04 proposal; reviewed F07 evaluation limits. | Low; no authoring-efficiency test. |
| C-09 | Full-context locale/access review and minimized diagnostic data are proposed safeguards. `hypothesis` | W04 proposal; inspected W02/F07 constraints. | Low for measured effect; no personal data collected. |
| C-10 | Author correctness, implementation behavior and player comprehension need distinct falsifying checks. `inference` | Reviewed F07 evaluation and corrected F01/W02 test principles. | High for the distinction, untested for this protocol. |
| C-11 | Permit and early-repair examples are invented, not shipped behavior or tests. `hypothesis` | W04 illustration. | Low for utility; no canon or implementation approval. |

## Related entries and history

Parent: [Narrative systems interfaces](../topics/narrative-systems-interfaces.md), `GDR-CAND-20261010-W04-TOP-02`. Complement: [Encounter and scenario composition](../topics/encounter-and-scenario-composition.md) for aftermath and return. [Theme and meaning](../topics/theme-and-meaning.md) remains separate: truthful applicability does not determine interpretation.

**Coverage:** conceptual occurrence, eligibility, repetition, expiry and resumed-history cases researched; actual tools, migration, multiplayer reconciliation, locale review and player benefit open. **History:** `0.1.0`, `initial-draft-1`, predecessor and supersession null. Independent W04 review is pending. No earlier batch reproduced, no canonical ID allocated, no release or application approved.

## Reviewed inputs and transfer limits

Inspected W01 fact/perspective distinctions, W02 intent-and-response and objective/lore passages, the corrected W02 multi-route test, corrected F01 transfer examples and F07 evaluation/ethics. The W02 saliency source was re-inspected directly, preserving its existing identity. The selected input is the parent-reviewed, unreleased waves 1–2 candidate archive, locally fingerprinted SHA-256 `4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931`. Relevant bytes, rather than remembered earlier drafts, were inspected. Exact dependency paths, selected revisions, byte hashes and inspected line ranges are recorded in the [review packet](../reviews/full-run-20261010-w04-review-packet.md#reviewed-dependency-provenance). These are prior candidate syntheses, not independent empirical validation of W04. Their cited outside studies are not reasserted unless the original source is separately listed in this entry.

The mounted starter instructions, evidence rules, gates, index, taxonomy and templates are the historical `0.1.0 candidate` input. The current dispatch authorizes W04 research but not conclusions, permanent IDs or release. The current canonical index, pending global allocations and central recovery ledger were not available. Current W03 spatial/exploration and F03 progression/resource drafts remain unavailable author-running dependencies; no guidance is inferred from them. There is no genre-specific draft in this packet; genre adaptation remains with the relevant owner, and no game label is inferred from an example.

## References

### GDR-SRC-20261010-W02-005 — Saliency

**Author/organization:** Yarn Spinner documentation team. **Publication/update:** unknown; live documentation checked on access date. **Publisher:** Yarn Spinner official documentation. **Verified access route:** [Saliency](https://docs.yarnspinner.dev/write-yarn-scripts/advanced-scripting/saliency). **Edition/build:** Live unpinned documentation; same source identity as inspected W02 reference. **Accessed:** 2026-10-10 (America/Los_Angeles research date). **Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Locator:** Saliency strategies and item conditions; built-in strategies; paragraph allowing null; Creating Custom Saliency Strategies, query-versus-selection distinction. **Claims in this entry:** C-04; rationale for C-06. **Rights:** Documentation linked and paraphrased, no implementation code reproduced. **Limits/relationships:** Selection eligibility, query and selection are technical distinctions, not measures of player comprehension or meaningfulness. No chosen package version or runtime execution verified. Identity reused, not assigned a new W04 alias..

### GDR-SRC-20261010-W04-003 — Patch #4 Now Live!

**Author/organization:** Larian Studios. **Publication/update:** 2023-11-02. **Publisher:** Official Baldur’s Gate 3 news. **Verified access route:** [Patch #4 Now Live!](https://baldursgate3.game/news/patch-4-now-live_96). **Edition/build:** Historical Patch 4 notes; not a claim about the current build. **Accessed:** 2026-10-10 (America/Los_Angeles research date). **Access:** `relevant-excerpt`. **Type:** First-party production defect/fix report. **Locator:** Flow and Scripting / act-specific fix bullets naming Gale’s repeat teaching scene, Ulma credit before meeting, Bane/Gortash actor attribution, Rolan’s missing reunion and Karlach/Dammon older-save repair; Mystic Carrion information-object replacement bullet. **Claims in this entry:** C-05; motivates C-06 adversarial cases. **Rights:** Copyright publisher; short paraphrases only. **Limits/relationships:** The inspected artifact is the patch report, not gameplay. Incidence, causal implementation fault and effectiveness of fixes were not independently reproduced. Several bullets are one publisher report, not independent studies..

### GDR-SRC-20261010-W04-002 — Running Your Ink

**Author/organization:** inkle / ink contributors. **Publication/update:** unknown; live master documentation checked on access date. **Publisher:** inkle official public ink repository. **Verified access route:** [Running Your Ink](https://raw.githubusercontent.com/inkle/ink/master/Documentation/RunningYourInk.md). **Edition/build:** Unpinned master snapshot; package release and commit not established. **Accessed:** 2026-10-10 (America/Los_Angeles research date). **Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Locator:** Sections Saving and loading; Error handling; Setting/getting ink variables; Read/Visit counts; Variable observers; External functions. **Claims in this entry:** C-07; persistence-scope distinction. **Rights:** Repository documentation linked and paraphrased; no code or document reproduction. **Limits/relationships:** Documents capabilities, not a whole-game continuity guarantee or authoring-efficiency experiment. No code executed. Revalidate the chosen release before implementation; no runtime architecture recommendation follows..


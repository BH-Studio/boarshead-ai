---
id: GDR-CAND-20261010-W04-TOP-02
kind: topic
title: Narrative systems interfaces
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
- narrative state contracts
- reactive story continuity
- stale narrative state
- repeated narrative triggers
- narrative debugging requirements
tags:
- state
- conditions
- reactions
- persistence
- save-load
- authoring
- conceptual-interface
- evidence-open
related_topics:
- GDR-CAND-20261010-W04-TOP-01
- GDR-CAND-20261010-W04-TOP-03
- GDR-CAND-20261010-W02-TOP-01
- GDR-CAND-20261010-W02-TOP-03
related_patterns:
- GDR-CAND-20261010-W04-PAT-02
- GDR-CAND-20261010-W02-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-W02-005
- GDR-SRC-20261010-W04-002
- GDR-SRC-20261010-W04-003
permanent_id: null
reviewer: null
approved_by: null
approved_date: null
predecessor_sha256: null
supersedes: null
change_summary: Initial bounded W04 candidate; no prior batch replaced.
byte_hash_record: ../reviews/full-run-20261010-w04-review-packet.md#artifact-byte-manifest
---

# Narrative systems interfaces

**Draft research candidate; not released or approved guidance.** All examples marked illustrative are invented, not studio canon. No game, engine, prototype, participant study or player test was run. Recommendations are conditional inferences or hypotheses, not formal standards.

## Decision and scope

This topic helps narrative and systems designers agree on **what a situation means, what can change it, what the player can observe, and what must remain true after interruption or return**. An interface here is a conceptual agreement across design concerns, not a software interface definition, runtime owner, storage technology or engine integration plan. A state table, example sequence or author-facing explanation can express the agreement without prescribing implementation. [C-01]

A working **narrative state** describes a relevant circumstance: an invitation is open, an agreement was accepted, a witness heard a report, or a delivery is complete. An **event** is a relevant occurrence, not merely a line being displayed. A **condition** limits applicability. A **reaction** is an authored or systemic acknowledgment of circumstances. **Persistence** specifies which distinctions survive a defined boundary such as leaving an area, resuming play or restoring a saved history. These definitions organize the draft; they are not a normative technical standard. [C-01]

Included are conceptual state transitions, event/condition contracts, actor attribution, reactive persistence, repeated and stale responses, save/load continuity, authoring visibility and debugging requirements. Excluded are runtime ownership, event-bus or database choices, serialization formats to adopt, content-pipeline implementation and assertions that correct state guarantees narrative quality. Theme interpretation is a separate topic and must not be reduced to a debugging result.

## Core explanation and mechanisms

### Facts, attributed beliefs, exposure and interpretation are different

The inspected W01/W02 candidates distinguish operational circumstances from what a character claims, what evidence was presented and what the player concludes. Transfer that distinction cautiously. A visited conversation establishes neither comprehension nor agreement. A speaker’s false belief can be correct characterization. A receipt saying an agreement was accepted before the player accepted it is a different problem. [C-02]

A useful conceptual record states **whose fact or belief** is being represented. “The courier says the bridge is open” and “the bridge is traversable” can legitimately differ. “The player has seen this report” is also narrower than “the player knows it is reliable.” When authoring requires a known-to-character fact, identify the fictional route by which that character could know it. Do not infer that the human player possesses the same knowledge. [C-02, C-06]

This separates three review questions: is the described state possible under the supported history; is the character’s response intentional and appropriate to their perspective; and does the player understand or value the result? The first can be checked against an authored trace. The other two need additional interpretive or experiential evidence. [C-02, C-08]

### Selection is not occurrence, and occurrence is not understanding

Yarn’s inspected documentation distinguishes querying a candidate from its selection and permits no content to run. It therefore supplies a concrete technical example of why “eligible,” “chosen” and “actually acknowledged” should not be casually collapsed. It does not make a selection policy a theory of meaningful response. [C-03; GDR-SRC-20261010-W02-005]

The application bridge is to specify **which meaningful occurrence justifies which change**. Looking for a possible reply should not, by itself, count as the fictional agreement being made. A recap of a completed payment should not create a second payment merely because it mentions the first. Repeated gifts, repeated practice and deliberate repeated greetings can be legitimate; the contract must identify the repeated occurrence rather than impose a universal “once only” rule. These are design inferences and a proposed audit, not a prescribed runtime mechanism. [C-05, C-06]

### Persistence is a scoped promise

The ink documentation exposes story-state saving/loading alongside variables, visit counts and external interactions. This is evidence of documented capabilities within its own scope, not evidence that an entire game’s surrounding situation is automatically reconciled. [C-04; GDR-SRC-20261010-W04-002]

A narrative persistence promise therefore needs an explicit boundary. If the player returns to a history in which a permit was granted, the relevant acknowledgment should refer to that history. A deliberate rewind is not the same as preserving progress beyond a save. A “new cycle” may intentionally reset relationships while retaining other information. None of these choices implies a particular storage owner; they require designers to agree on the player-facing result and the exceptions. [C-05]

### Defect reports motivate adversarial histories, not invented diagnoses

Larian’s historical Patch 4 notes report premature credit, incorrect actor attribution, repeated scenes and older-save repairs. These are documented production cases against assuming that ordinary-order progression covers all relevant histories. The notes do not reveal every root cause, incidence or implementation detail, and W04 did not reproduce the defects or fixes. [C-07; GDR-SRC-20261010-W04-003]

The narrow bridge is to include out-of-order completion, duplicate notification, changed actor, missing intermediary and resumed history in proposed authoring examples where those cases are supported. It would be an unsupported leap to recommend a particular architecture from those patch bullets or to claim that this checklist would have prevented the reported defects. [C-06, C-08]

## Design choices and alternatives

| Choice | Use when / intended benefit | Cost and contrary case |
|---|---|---|
| A small explicit circumstance record | A few durable distinctions control consequential reactions. | Excessive distinctions increase authoring burden. Remove an implied long-term promise before creating an unbounded memory obligation. |
| A fixed authored exchange | Entry conditions are narrow and sufficient. | Can be cheaper and clearer than reactive selection. Do not imply it responds to actions it does not inspect. |
| A context-selected response | Several histories need different acknowledgment. | Eligibility does not determine tone, importance or audience comprehension. A neutral truthful line or silence can be preferable. |
| An attributed account | Conflicting testimony or limited knowledge is intentional. | Keep the attribution understandable without revealing hidden truth. Do not use unreliability to excuse accidental state contradictions. |
| A bounded recap | The player may return after interruption. | Replay of information must not silently repeat a commitment, spoil an undiscovered conclusion or claim that a player forgot. |
| Explicit authored precedence | Supported events can contradict or overtake one another. | Someone must decide the meaning of the combination. “Most recent wins” is not automatically the correct fiction. |

The proposal is to choose the **smallest agreement that preserves the meaningful distinction**, not to encode everything about every character. A world can be deliberately nonreactive, resettable or impressionistic. Correctly describing that limitation may be better than constructing a large reactive system that cannot maintain its own promises. [C-01, C-05, C-06, C-08]

## Application process

### A meaning-level event and reaction contract

The following fields are an authoring aid, not required runtime fields. Use ordinary language, a table, annotated script or another reviewable representation. The reason for each field is the claim it lets a reviewer challenge. [C-06, C-08]

| Question | What the authoring agreement should resolve | What must not be inferred |
|---|---|---|
| What happened? | The relevant occurrence and its actor, recipient and affected object or situation. | A generic “completed” label need not identify who acted or what was completed. |
| Under which circumstances? | Preconditions that materially change whether the occurrence or reaction is possible. | A missing condition is not automatically false or harmless. |
| What changed? | The accepted consequence, its effective point, and what remains unchanged. | Displaying a line is not inherently the point of acceptance. |
| Who can know or say this? | Character perspective, evidence and deliberate falsehoods. | Player comprehension cannot be certified by a visit counter. |
| What can be selected? | Eligible alternatives, ordering/tie choices if relevant, and no-selection behavior. | The highest-complexity or most recent line is not universally the best response. |
| What can repeat? | Once per accepted occurrence, per visit, per conversation, or intentionally repeatable. | “Once” needs a scope; repeated text and repeated consequence are not the same. |
| When does it expire? | Circumstances that make the response stale, superseded or inappropriate. | Eligibility when queued does not guarantee validity later. |
| What survives a boundary? | Meaning retained or reset across area departure, interruption, restore or deliberate restart. | A technical story snapshot does not prove every related circumstance is preserved. |
| What can an author inspect? | A representative history, eligible/not-eligible reasons, selected response and expected consequence. | A debug explanation does not prove the response was read, believed or enjoyed. |

### Diagnose → choose → trace → evaluate → revise

1. **Name the promise and its horizon.** Is the reaction immediate acknowledgment, a later opportunity, a remembered relationship or simply flavor? Limit persistence to the supported horizon. [C-05]
2. **Separate factual and attributed records.** Keep intentional disagreement distinct from contradictions in accepted events. Identify uncertainties that should remain uncertain. [C-02]
3. **Define the acceptance boundary.** State whether an action requests, offers, accepts, attempts, completes or merely reports something. Review wording with W02’s intent-and-response work without copying that pattern’s scope. [C-06]
4. **Write ordinary and adversarial traces.** Include relevant cases of early completion, missing participants, contradictory arrivals, repetition, expiry and return. Do not assert that traces have been executed merely because they are specified. [C-07, C-08]
5. **Specify the observable result.** A correct absence of a reaction may be appropriate; an expected acknowledgment may also be necessary to explain a consequence. Define the local purpose before selecting a fallback. [C-03, C-06]
6. **Specify the author’s diagnostic questions.** Show why an expected response is missing and why an unexpected response appears. Distinguish wrong facts, wrong attribution, stale conditions, localization context and a merely disliked line. [C-08, C-09]
7. **Review persistence and interruption boundaries with the relevant designers.** Describe what the player should find after return, including an intentional rewind or reset. Resolve contradictions as design decisions before considering implementation. [C-04, C-05]
8. **Evaluate benefit against the simpler alternative.** If the contract does not improve consequential diagnosis enough to justify its upkeep, narrow the reactive promise or reduce the record. Correctness alone does not establish that more reactivity is worth making. [C-08, C-11]

## Patterns and genre adaptations

[Reaction eligibility and repetition contract](../patterns/reaction-eligibility-and-repetition-contract.md), `GDR-CAND-20261010-W04-PAT-02`, turns the meaning-level distinction between an occurrence and its later acknowledgment into a bounded recipe. It is adjacent to, but not a replacement for, W02’s `GDR-CAND-20261010-W02-PAT-01`, which concerns the speech act the player selects.

[Encounter and scenario composition](encounter-and-scenario-composition.md) uses these contracts at exits and revisits. [Theme and meaning](theme-and-meaning.md) uses them only to distinguish accidental factual contradiction from a deliberate interpretive tension. A diagnostic record is not an oracle of thematic meaning.

A loop that intentionally forgets, a persistent relationship story and a fixed dramatic sequence need different persistence promises. These are conditional structures, not categorical genre requirements. No genre files or unseen W03/F03 drafts are supplied as evidence.

## Examples and counterexamples

### First-party defect reports: observed documentation, not observed gameplay

| Reported case in Larian’s Patch 4 notes | Narrow authoring question it motivates | What the report does not establish |
|---|---|---|
| Credit before the relevant prior meeting | Is initiation necessary, or can prior completion be acknowledged differently? | Which implementation fault caused the reported case. |
| Credit attributed to the wrong actor | Does the acknowledgment distinguish who caused the event? | Whether every surrounding outcome was wrong. |
| Repeated or expired scene | Is the trigger still relevant, and what repetition scope was intended? | A universal rule against replaying narrative content. |
| Older-save repair | What should a supported resumed history contain? | That W04 has verified any save migration or fix. |

These paraphrases refer to a single historical report. They are not four independent studies, and they do not justify treating its release as the current state of that game. [C-07]

### Illustrative worked contract: archive access permit

A traveler asks an archive steward for permission to consult a restricted ledger. The invented scene distinguishes **request made**, **terms offered**, **terms accepted**, **permit granted**, **ledger consulted**, **permit revoked**, and **the steward’s belief about the traveler**. These are conceptual circumstances, not an instruction to build one global state machine. [C-12]

The local promise is that accepting a specified deposit grants one period of access. Asking about the deposit is not acceptance. Reading a recap of the permit is not a new deposit. A later revocation is a new event with its own reason; it should not be disguised as though permission had never existed. A steward can distrust the traveler even while honoring a valid permit.

| Proposed history | Expected meaning-level result | Required diagnostic explanation |
|---|---|---|
| Traveler asks about terms, then leaves | No deposit or permit yet; offer may remain available under its stated conditions. | Why “granted” is not eligible. |
| Deposit accepted, acknowledgment interrupted | Upon return to this accepted history, show truthful acknowledgment or recap without a second charge. | Whether the agreement, acknowledgment and payment occurrence are being conflated. |
| Same completion is reported again | Recognition may be repeated when useful; the original deposit does not become a new one. | Which occurrence is being acknowledged, and what repeat scope applies. |
| Permit granted by an alternate official | Steward may recognize valid access without claiming to have granted it personally. | Distinguish authority, actor and witness knowledge. |
| Traveler saw the ledger through another supported route | Acknowledge the actual history rather than forcing a fictional first discovery. | Whether consultation requires formal access under this design or can precede it. |
| Revocation occurs before a queued invitation | Suppress or revise the stale invitation; do not present both as currently operative without intentional explanation. | Which change overtook the earlier conditions. |
| Earlier save is restored | Describe the history represented by that restore, including any deliberate retained meta-information. | Do not silently mix later commitments into an earlier history. |

**Deliberate ambiguity:** the steward may suspect the traveler has copied the ledger. That suspicion need not be resolved in the operational record. A line expressing suspicion is not wrong just because the game does not certify its truth. Conversely, “I received your deposit” is not made valid by declaring the steward mysterious when the accepted history contains no payment and no intentional lie.

**Alternative:** use a single fixed scene in which access is granted without a deposit, later revocation or remembered interaction. This removes many obligations and may be appropriate when access is not a meaningful decision. There is no evidence here that the richer version is automatically better.

## Failure modes and constraints

**Overmodeling.** The authoring record can become larger than the experience it protects. Track distinctions that affect a supported promise, not every hypothetical emotion or biography. An empty “unknown” field should not invite a fabricated fact merely to satisfy a schema. [C-01, C-08]

**Accidental omniscience.** A reaction can reveal facts no speaker could know, or a recap can turn uncertain testimony into confirmed truth. Keep access to equivalent evidence separate from giving additional certainty. Accessibility is not a reason to spoil an intended mystery, and preserving mystery is not a reason to omit an accessible route to the same evidence. The specific solution needs presentation and audience review. [C-02, C-09]

**Localization context loss.** Tense, address, grammatical agreement and assumptions about shared knowledge can alter the meaning of a reaction. Provide the surrounding situation, speaker perspective and whether the text is a first acknowledgment or recap. These are proposed review requirements; no translation equivalence or measured benefit was established here. [C-09]

**Unexplained fallback.** Silence can be a valid result, but it can also hide a broken promise. A generic positive acknowledgment can be worse than no line when the accepted result was refusal or failure. Define what must be communicated before choosing an apparently safe fallback. [C-03, C-06]

**Debugging as a meaning oracle.** A trace may show that a harsh response is intended and factually applicable, yet players may read it as contempt, comedy or a defect. Authoring/debug requirements explain selection and history; they do not certify tone, representation or thematic reception. [C-08, C-10]

**Privacy and production burden.** Proposed diagnostic views need fictional circumstances, content/version context and a relevant trace, not people’s private beliefs or sensitive player profiles. Do not quietly infer mental health, identity or moral character from selected dialogue. Any real telemetry or participant record would need a separately approved purpose and safeguards; none was collected here. Keep review and localization work within an explicit production scope. [C-09]

## Playtest and validation

**Not performed:** the following are proposed authoring reviews, prototype checks and player studies, not passed tests. No implementation technology is selected. [C-11]

| Question | Proposed method | Measures, controls and disconfirming result |
|---|---|---|
| Can authors detect consequential state/response mismatches? | Give relevant authors the same bounded script and histories, with versus without the proposed contract. Use different but comparable cases or counterbalance to limit memorization. | Track correct diagnoses, false positives, time, overlooked cases and maintenance effort. Reject expansion if it mainly creates work or false alarms without improving consequential diagnosis. |
| Does the response preserve the accepted occurrence across return? | In a later authorized prototype, compare ordinary progression, duplicate notification, interrupted acknowledgment and restored history. | Check the specified consequence and attribution separately from text display. An intentionally repeatable greeting must remain possible; passing an “only once” case does not justify suppressing all repeats. |
| Can players distinguish question, commitment and recap? | Before the relevant action, ask what would change; after it, ask what did change and why. Include refusal and alternate-actor cases. | Measure understanding separately from preference and successful completion. Revise when people systematically infer a different commitment. Do not prime them with the desired explanation first. |
| Does the reaction remain appropriate in supported locales and access routes? | Review full exchanges with relevant language/access participants and content context. | Record meaning changes, inaccessible evidence, spoiler leakage and needed assistance. A fluent literal translation or enabled option is not a completed comprehension test. |

The actual test population, number of cases and practical decision boundary must be chosen for the local question and risk. No universal sample size or timing target is proposed. Control author familiarity, script difficulty, instrumentation visibility and repeated exposure; an explained error is easier to find on a second pass. Keep same-rule transfer distinct from changed-rule adaptation, as required by the inspected F01/W02 corrections. A static trace does not stand in for engine execution, and a runtime check does not establish player benefit.

## Claim ledger

| ID | Precise claim and class | Support / locator | Applicability, confidence and unresolved question |
|---|---|---|---|
| C-01 | Narrative interfaces can be expressed as meaning-level agreements without choosing runtime architecture. `inference` | Assigned W04 boundary; working definitions. | High for the scope distinction; not a claim about best software design. |
| C-02 | Operational facts, attributed beliefs, exposure and interpretation need not coincide. `inference` | Inspected W01 worldbuilding and W02 lore/dialogue candidate passages. | High for the logical distinctions; no evidence here about their optimal presentation. |
| C-03 | Yarn documents condition-based selection, no-selection and query-versus-selection distinctions. `observed-example` | W02-005, Saliency; Creating Custom Saliency Strategies. | High for inspected documentation, not tested runtime behavior or player effect. Live release unpinned. |
| C-04 | ink documents story-state save/load and external interaction facilities within a defined scope. `observed-example` | W04-002, Saving and loading; variables/visits/observers/external functions. | High for documentation; no whole-game guarantee or code execution. |
| C-05 | A persistence promise should identify its boundary and meaningful retained/reset distinctions. `inference` | C-02/C-04; reviewed W01/W02 consequence limits. | Moderate for design utility; implementation and audience comprehension remain untested. |
| C-06 | Separating occurrence, acceptance, eligibility, repetition and expiry may prevent specific authoring conflations. `hypothesis` | C-03/C-05/C-07 provide rationale; assembled W04 proposal. | Low for preventive efficacy; some content requires deliberate repetition or uncertainty. |
| C-07 | Historical BG3 Patch 4 reports early credit, attribution, repetition and resumed-history defects/fixes. `observed-example` | W04-003, named patch bullets in References. | High for existence of first-party report; game behavior and root cause not independently verified. |
| C-08 | Diagnostic explanations may improve review but cannot certify narrative quality or reduce cost by themselves. `hypothesis` | C-03/C-07; W04 comparison proposal; reviewed F07 evaluation limits. | Low for workflow improvement, high for the distinction from player benefit. |
| C-09 | Contextual locale/access review and minimized diagnostic data are proposed safeguards. `hypothesis` | W04 proposal; inspected F07 ethics and W02 evidence/meaning constraints. | Low for efficacy; no specific locale or population studied. Not a legal/compliance claim. |
| C-10 | Factually eligible reactions do not determine thematic interpretation. `inference` | Logical distinction between selection and reception; theme topic develops the separate evidence. | High for non-equivalence; no prediction of a particular reading. |
| C-11 | Author diagnosis, runtime continuity and player understanding require separate validation. `inference` | Reviewed F07 evaluation; inspected corrected F01/W02 test distinctions. | High for avoiding conflation; actual protocols require separate approval. |
| C-12 | The archive-permit histories are invented examples of the proposed agreement. `hypothesis` | W04 illustration, not a shipped-game observation. | Low for practical benefit; no implementation or test completed. |

Source suffixes retain their full identifiers in References. Claim IDs are local to this entry. No claim in this topic is a formal standard or an approved studio implementation decision.

## Open questions and change history

Coverage is **open**. Conceptual contracts, actor attribution, repetition, expiry, persistence boundaries and diagnostic questions are addressed. No live save migration, engine integration, distributed/cooperative state resolution, authoring-tool usability study or localization trial was performed. The inspected official documents are unpinned live pages; they must be rechecked against an actual chosen release before any implementation plan.

The next discriminating question is whether the proposed contract improves diagnosis of consequential mismatches compared with a smaller fixed-scene agreement, without excessive false positives or authoring burden. Pattern overlap and the boundary between purposeful ambiguity and accidental contradiction need independent review. Current F03/W03 dependencies remain unavailable, not assumed compatible.

**History:** `0.1.0`, `initial-draft-1`; initial submission, predecessor and supersession null. Author self-review is in the packet; independent W04 evidence review has not occurred. Research authorization does not approve architecture, game adoption or release.

## Reviewed inputs and transfer limits

Inspected W01 narrative/worldbuilding distinctions, W02 dialogue, lore and intent-and-response passages, the selected corrected W02 multi-route test, corrected F01 transfer examples and F07 evaluation/ethics passages. Public Yarn documentation was separately re-inspected and its W02 source identity reused; review receipts alone were not used as source verification. The selected input is the parent-reviewed, unreleased waves 1–2 candidate archive, locally fingerprinted SHA-256 `4dd701c125cab0fb3254483015bd10cc5ad979c6fbc9730c2d1c0a22caef2931`. Relevant bytes, rather than remembered earlier drafts, were inspected. Exact dependency paths, selected revisions, byte hashes and inspected line ranges are recorded in the [review packet](../reviews/full-run-20261010-w04-review-packet.md#reviewed-dependency-provenance). These are prior candidate syntheses, not independent empirical validation of W04. Their cited outside studies are not reasserted unless the original source is separately listed in this entry.

The mounted starter instructions, evidence rules, gates, index, taxonomy and templates are the historical `0.1.0 candidate` input. The current dispatch authorizes W04 research but not conclusions, permanent IDs or release. The current canonical index, pending global allocations and central recovery ledger were not available. Current W03 spatial/exploration and F03 progression/resource drafts remain unavailable author-running dependencies; no guidance is inferred from them. There is no genre-specific draft in this packet; genre adaptation remains with the relevant owner, and no game label is inferred from an example.

## References

### GDR-SRC-20261010-W02-005 — Saliency

**Author/organization:** Yarn Spinner documentation team. **Publication/update:** unknown; live documentation checked on access date. **Publisher:** Yarn Spinner official documentation. **Verified access route:** [Saliency](https://docs.yarnspinner.dev/write-yarn-scripts/advanced-scripting/saliency). **Edition/build:** Live unpinned documentation; same source identity as inspected W02 reference. **Accessed:** 2026-10-10 (America/Los_Angeles research date). **Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Locator:** Saliency strategies and item conditions; built-in strategies; paragraph allowing null; Creating Custom Saliency Strategies, query-versus-selection distinction. **Claims in this entry:** C-03; rationale for C-06/C-08. **Rights:** Documentation linked and paraphrased, no implementation code reproduced. **Limits/relationships:** Selection eligibility, query and selection are technical distinctions, not measures of player comprehension or meaningfulness. No chosen package version or runtime execution verified. Identity reused, not assigned a new W04 alias..

### GDR-SRC-20261010-W04-002 — Running Your Ink

**Author/organization:** inkle / ink contributors. **Publication/update:** unknown; live master documentation checked on access date. **Publisher:** inkle official public ink repository. **Verified access route:** [Running Your Ink](https://raw.githubusercontent.com/inkle/ink/master/Documentation/RunningYourInk.md). **Edition/build:** Unpinned master snapshot; package release and commit not established. **Accessed:** 2026-10-10 (America/Los_Angeles research date). **Access:** `relevant-excerpt`. **Type:** Official technical documentation. **Locator:** Sections Saving and loading; Error handling; Setting/getting ink variables; Read/Visit counts; Variable observers; External functions. **Claims in this entry:** C-04; rationale for C-05. **Rights:** Repository documentation linked and paraphrased; no code or document reproduction. **Limits/relationships:** Documents capabilities, not a whole-game continuity guarantee or authoring-efficiency experiment. No code executed. Revalidate the chosen release before implementation; no runtime architecture recommendation follows..

### GDR-SRC-20261010-W04-003 — Patch #4 Now Live!

**Author/organization:** Larian Studios. **Publication/update:** 2023-11-02. **Publisher:** Official Baldur’s Gate 3 news. **Verified access route:** [Patch #4 Now Live!](https://baldursgate3.game/news/patch-4-now-live_96). **Edition/build:** Historical Patch 4 notes; not a claim about the current build. **Accessed:** 2026-10-10 (America/Los_Angeles research date). **Access:** `relevant-excerpt`. **Type:** First-party production defect/fix report. **Locator:** Flow and Scripting / act-specific fix bullets naming Gale’s repeat teaching scene, Ulma credit before meeting, Bane/Gortash actor attribution, Rolan’s missing reunion and Karlach/Dammon older-save repair; Mystic Carrion information-object replacement bullet. **Claims in this entry:** C-07; motivates C-06/C-08 adversarial histories. **Rights:** Copyright publisher; short paraphrases only. **Limits/relationships:** The inspected artifact is the patch report, not gameplay. Incidence, causal implementation fault and effectiveness of fixes were not independently reproduced. Several bullets are one publisher report, not independent studies..


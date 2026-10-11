---
id: GDR-CAND-20261010-P01-TOP-01
kind: topic
title: Visual communication
version: 0.1.0
status: draft
owner_project: BH-GDR-Presentation-and-Interaction
run_id: GDR-FULL-20261010
batch_id: P01
identity_scope: temporary run-scoped candidate; permanent allocation pending
updated: '2026-10-10'
evidence_checked: '2026-10-10'
aliases:
- visual hierarchy
- visual readability
- silhouette readability
tags:
- visual-communication
- hierarchy
- contrast
- affordances
- silhouettes
- readability
- aesthetic-coherence
related_topics:
- GDR-CAND-20261010-P01-TOP-02
- GDR-CAND-20261010-P01-TOP-03
related_patterns:
- GDR-CAND-20261010-P01-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-P01-01
- GDR-SRC-20261010-P01-04
- GDR-SRC-20261010-P01-05
- GDR-SRC-20261010-P01-10
- GDR-SRC-20261010-P01-11
- GDR-SRC-20261010-P01-12
- GDR-SRC-20261010-P01-13
- GDR-SRC-20261010-P01-16
reviewer: null
approved_by: null
approved_date: null
---

# Visual communication

**Draft research candidate — not released guidance.** This entry helps choose a visual treatment, not certify an entire game as accessible or predict an emotional response. Its proposed hierarchy and review process are design inferences. A clear silhouette, a compliant web contrast ratio and an attractive screen answer different questions. [C-01–C-09]

## Decision and scope

**Decision:** How should a designer make relevant states, objects and possible actions recognizable while retaining the intended aesthetic, appropriate uncertainty and usable information density?

Own hierarchy, contrast, affordance communication, silhouettes, readability and aesthetic coherence. Interface structure belongs to [Interface and information](interface-and-information.md); end-to-end access and representative evaluation belong to [Accessibility and inclusive interaction](accessibility-and-inclusive-interaction.md). Art-direction pipelines, camera systems, detailed localization engineering and Foundations’ learning/onboarding topic are dependencies, not researched substitutes inside this file.

### Working definitions and success conditions

These are analytic conventions for this draft, not standardized perceptual scales. **Hierarchy** is the relative emphasis assigned to information for a particular task. **Contrast** is a difference between a signal and its surroundings; luminance contrast, hue difference, scale, shape and movement are not interchangeable measures. **Readability** means the intended player can obtain the needed meaning under the specified conditions, not merely see a mark. **Silhouette** is the external shape used as one possible recognition cue. **Aesthetic coherence** is a proposed consistency of visual relationships, not a requirement that every element look equally prominent. [C-01, C-07]

Distinguish an available action from a cue suggesting that action. A decorative handle can look usable without enabling anything; an invisible interaction can exist without being discovered. Norman’s distinction between real/perceived affordances and conventions supplies a useful vocabulary, not proof that a particular icon is self-explanatory. A **signifier**, as used here, is the representation offered to communicate an action or state. [C-02; GDR-SRC-20261010-P01-12]

The intended outcome is correct, timely interpretation with tolerable effort and retained player choice. Recognition, task accuracy, attraction, perceived polish, comfort and intended emotion must be assessed separately. No emotional or performance outcome was measured in this batch. [C-01, C-10]

### Context that a later application must declare

| Context | Record before choosing a visual target | Why the choice remains conditional |
| --- | --- | --- |
| Display and viewing | Physical display size, rendering resolution, scaling, distance, surrounding illumination and contrast settings. | A pixel count does not describe all viewing conditions. |
| Projection and presentation | Flat display versus spatial display; viewing angle, camera distance, occlusion, motion, environmental effects and split-screen regions where applicable. | A clear reference image does not establish readability during use. |
| Task and prior knowledge | Required distinction, consequences of error, time available, practiced versus first use, and legitimate hidden information. | A deliberately uncertain identity is different from an inaccessible required action. |
| Input and access | Pointer, digital focus, touch, preferred accommodations and assistive technology; available audio/haptics and chosen sensory settings. | Visual inspection alone cannot assess every route to the information. |
| Language and content | Target scripts, reading direction, font coverage, terminology, text expansion and localized symbols. | A familiar symbol or compact English label is not proof of comprehension elsewhere. |

This is a proposed application record, not a claim that a specific platform or audience was tested. No studio hardware or game is the default. [C-09–C-11]

## Core explanation and mechanisms

### Separate the links in the communication chain

| Link to evaluate | Relevant evidence | Application bridge and failure possibility |
| --- | --- | --- |
| A signal is available and visually distinguishable. | Scoped contrast criteria and text-display guidance; narrow clutter research. | Inspect the signal against actual backgrounds and settings. It may disappear through occlusion, scaling or competing presentation. |
| The player identifies the relevant object or state. | Valve’s silhouette account and Norman’s discussion of conventions. | A distinguishable outline can support a learned category, but orientation or equipment changes may erase the useful distinction. |
| The player interprets what the state permits. | Conceptual affordance/convention account, not a universal icon study. | A familiar-looking button can communicate the wrong action; more salience cannot repair an incorrect meaning. |
| Interpretation supports an appropriate response. | No general causal game comparison was inspected for this complete chain. | Test actual choices and errors. Looking at the correct object is not enough if the required response remains unclear. |

The complete chain is an **inference to evaluate**, not four proven stages every player follows. A result can fail at several links simultaneously. [C-01–C-09]

### Evidence that changes the decision

**Normative anchor, bounded scope.** For web content, WCAG 2.2 SC 1.4.1 prohibits color-only information. SC 1.4.3 specifies 4.5:1 text contrast, or 3:1 for defined large-scale text, with exceptions. SC 1.4.11 specifies 3:1 for relevant non-text UI/state and graphical information against adjacent colors, also with exceptions. These are criterion-specific requirements, not a mandate that every game pixel have that contrast. SC 1.4.10 permits exceptions for parts requiring two-dimensional layout; it is not a blanket exemption for an entire interface. Native applicability needs a separate mapping. [C-03; GDR-SRC-20261010-P01-01]

**Game guidance, different units.** XAG 101’s examples distinguish a 26-pixel text-body height for console from 18 pixels for PC/VR at 1080p. These are the document’s scoped vendor recommendations, not font-point sizes, validated angular-size rules, or this library’s universal defaults. This draft does not prescribe either value for an unspecified platform. [C-04; GDR-SRC-20261010-P01-04]

**Production account, not causal proof.** Valve’s 2007 paper describes silhouette differentiation and controlled internal detail in its TF2 approach. The inspected Figure 2 and §4.1 document that design vocabulary; they do not show which players recognized which classes, at what distance, or whether the treatment caused commercial success. [C-05; GDR-SRC-20261010-P01-13]

**Empirical boundary on “reduce clutter.”** Rosenholtz and colleagues recruited 20 people to rank 25 printed maps; the model correlated with mean clutter rankings (Spearman .83). The task measured perceived clutter, not game performance. Participants also differed on changes such as removing labels. A cleaner-looking display is therefore not evidence that the player can make a better decision. [C-06; GDR-SRC-20261010-P01-16]

## Design choices and alternatives

### Choose an information hierarchy, not a universal style

Start with the required distinction: current focus, selected item, unavailable action, changing threat, or optional detail. Assign emphasis to that distinction, and state when it should cease to dominate. A status that remains the brightest object after becoming irrelevant can compete with the next decision; that competition is a proposed failure mechanism to test, not a measured universal effect. [C-07, C-10]

| Choice | Use when | Cost or failure risk | Simpler/competing option |
| --- | --- | --- | --- |
| Restrained background with salient task signal | The signal should be found among nonessential decoration. | Flattening the environment can remove useful landmarks or desired aesthetic detail. | Preserve detail but give the signal a stable backing, outline or location. |
| Text plus symbol | Meaning must be explicit or symbol familiarity is uncertain. | Reading load, translation, occupied area and screen-narration ordering. | A labeled detail view, a familiar validated symbol, or fewer simultaneous states. |
| Shape/silhouette distinction | Relevant categories must be distinguished without reading fine detail. | Viewpoint, animation, overlap and customization may change the outline. | Role labels or contextual identifiers when silhouette is unavailable. |
| Consistent semantic styling | Repeated states should retain meaning across screens and objects. | Over-generalization can make different actions look interchangeable. | A deliberately differentiated family for a genuinely different action type. |
| Selective movement or transient emphasis | A changed state warrants attention that static presentation is missing. | Distraction and sensory burden; attention may be drawn away from an ongoing task. | A static state change with persistent, inspectable information. |
| Dense comparison view | Several values must be compared together by a prepared user. | Scan effort, small content and focus complexity. | Optional compact/detailed views with the same underlying facts. |

These are proposed conditional options, not established rankings. Omitting an extra highlight is appropriate when the existing representation already communicates the necessary difference. Conversely, removing text only to obtain a cleaner screenshot can undermine the actual comparison task. [C-07–C-10]

### Aesthetic coherence without semantic camouflage

Write a short visual grammar: how focus, selection, availability, danger, ownership and uncertainty differ. State which decorative treatments never imply interactivity. Keep **style consistency** separate from **semantic sameness**: a single material family can contain clearly different states. Where deliberate deception is part of an approved design, identify exactly which knowledge remains uncertain; do not let an unavailable access channel become the deception. This is a design inference, not a finding about what all players find beautiful or fair. [C-02, C-07, C-08]

## Application process

1. **Diagnose the decision.** Name what must be recognized, by whom, under which task state. Record current errors rather than beginning with “make it pop.” Separate a detection failure from incorrect interpretation.
2. **Specify semantic states.** Describe ordinary, focused, selected, disabled, pending, changed and resolved states only where relevant. Identify distinctions that must survive loss of hue, removal of motion or another chosen setting.
3. **Choose the least complex candidate.** Compare a presentation repair with changing the underlying interaction. An action that cannot be explained honestly may need redesign, not a stronger highlight.
4. **Author a presentation contract.** Record text treatment, visual tokens, outline/shape dependencies, backgrounds and alternative information channels. Do not use an isolated screenshot to claim broad readability.
5. **Prototype after separate authorization.** Exercise relevant viewing angles, task loads, localization and access settings. Inspect worst plausible combinations, then test with appropriate users rather than declaring simulated disability representative.
6. **Keep, adapt or remove.** Retain the candidate only for conditions its evidence supports. Exit when additional emphasis adds distraction, required distinctions remain inaccessible, or the simpler comparison is sufficient.

All steps are proposed. This batch produced research documents, not assets or prototypes. [C-07–C-11]

## Patterns and genre adaptations

[Redundant critical-state cues — GDR-CAND-20261010-P01-PAT-01](../patterns/redundant-critical-state-cues.md) specifies one conditional way to preserve important state information across representations. It is not a rule to duplicate all visual content or activate every channel simultaneously. [C-08]

No genre files were assigned or produced. Experience goals and tasks are conditional contexts here, not statements about a genre’s population. Foundations’ learning/onboarding, this domain’s full art-direction/platform/localization topics, and genre-specific guidance are unresolved dependencies listed in the packet; no missing file is represented as an existing link.

## Examples and counterexamples

### Illustrative worked example: a route-control panel

**Synthetic, not a shipped-game observation or test.** A player must choose between two service routes. Route A is available. Route B is unavailable because a valve must be reopened. The player is entitled to know that reason. [C-10]

The first candidate uses differently colored route lamps alone. The alternative adds the route name and state word, a distinct unavailable-state mark, and a stable focus indicator. The selected route and keyboard/controller focus remain different concepts. A meaningful nonvisual representation can announce the focused route, its state and available action; merely adding a shape does not provide that route. [C-07, C-08]

The visual grammar treats the route’s availability as persistent information and a newly completed repair as a change. It does not leave the repair notification permanently dominant. A low-detail scene is not required: the decision is whether the panel can be interpreted against the actual scene and at the player’s chosen settings. [C-09, C-10]

**Failure branches:** If players interpret the unavailable mark as “selected,” repair the semantics before increasing contrast. If translated labels cover both routes, change the layout rather than reduce text until it fits. If the alternative announces a hidden cause the player is not entitled to know, revise the information contract; modality substitution must not silently solve an intended inference task. These are proposed corrections, not measured outcomes. [C-08–C-11]

### Illustrative counterexample: expert comparison

A materials screen requires comparing capacity, weight and compatibility across several items. Removing labels and columns can reduce apparent clutter while making comparison impossible without repeated navigation. The strongest opposing design is a dense, stable table with meaningful headings and an optional simpler view—not universal minimalism. The map-ranking study does not decide which version improves this task. [C-06, C-07, C-10]

### Boundary case: intentionally similar identities

An experience may deliberately leave two objects’ identities uncertain until inspection. A demand that every silhouette be unique would remove the intended question. Keep the permitted ambiguity, but make the act of inspection and its result accessible. This does not establish that uncertainty is desirable for every game or excuse hiding required action information. [C-01, C-07, C-08]

## Failure modes and constraints

**Access and sensory load.** Distinct colors are not enough when hue is the only meaningful difference. Multiple visual encodings remain visual. Flashing/moving emphasis needs a separate distraction and safety review; the still-image treatment cannot establish either. Offer alternatives appropriate to the actual signal, not decorative accessibility labels. [C-08, C-09]

**Localization.** Plan complete glyph coverage and readable expansion, then evaluate translated meaning, symbols, line breaks and reading direction. Mirroring everything automatically is not a substitute for understanding semantic direction. That last constraint is an inference: a diagram’s physical meaning and a language’s reading order may have different owners. [C-11]

**Ethics.** Do not use the strongest contrast solely to make an undesired or destructive option appear to be the only path. Visual prominence is a design choice that should match a truthful action description. No claim of measured coercion or legal compliance follows from this ethical recommendation. [C-07, C-10]

**Production.** Assign ownership for state tokens, content exceptions, localization and regression images/tasks. Distinguish the number of assets from the number of meaningful states that require review. No cost multiplier, staffing requirement or performance benchmark was obtained. [C-11]

## Playtest and validation

**PROPOSED — NOT PERFORMED.** No participant recruitment, screenshots of a new prototype, technical contrast measurement, instrument validation or playtest occurred. [C-10]

**Question and comparison.** For a predeclared task, compare the present treatment with a targeted semantic/hierarchy repair and, where useful, a simpler representation. Hold required facts, interaction cost, task consequences and scene conditions constant where possible. A visual style change that also changes the available information is not a pure readability comparison.

**Participants and procedure.** Include first-use and practiced participants, people who rely on the relevant visual/access accommodations, and target-language users. Use their ordinary access settings and familiar input where the question allows. Determine recruitment and sample precision from the actual decision and available variability before execution; this draft supplies no universal sample size. Counterbalance comparable tasks and log learning, recognition of symbols, viewing context and unavoidably different presentations.

**Measures.** Record required-fact identification, action correctness, time or effort to locate the relevant information, mistaken affordances, access barriers and recovery. Ask separately about comfort and aesthetic preference. Eye tracking, if later justified, would indicate gaze behavior, not prove comprehension; no eye-tracking system was used here.

**Falsification and decision rule.** Before testing, define a meaningful local improvement and tolerated costs. Reject a readability claim when the apparent advantage depends only on information withheld from the comparator. Revise or block advancement of a version when a required fact is unavailable through a supported route. Prefer the simpler alternative when added emphasis brings no useful advantage; an inconclusive small study is not evidence of equivalence. Narrow the claim when it works only for practiced users or selected display conditions. Stop sessions on discomfort or a request to stop; participant protection is not an inconvenient outlier policy.

## Claim ledger

Claim class and confidence are separate. Confidence describes the exact, limited proposition, not the effectiveness of a whole design. Proposed illustrations, recipes and participant protocols are not observations.

### C-01

**Claim:** Define visual communication by the task facts a player must detect, distinguish, interpret and act on; visual notice alone is not successful communication. **Class:** `inference`. **Confidence:** moderate: A useful decomposition rather than a validated universal process model.

**Sources and locators:** GDR-SRC-20261010-P01-12 — Affordance; Perceived affordance; Cultural constraints, cultural conventions; conclusion.; GDR-SRC-20261010-P01-05 — Visual options; Audio options; Haptic options; Color vision deficiency; Implementation guidelines for important information.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which stage fails in the actual task?

### C-02

**Claim:** Norman distinguishes real and perceived affordances from cultural conventions. **Class:** `practitioner-heuristic`. **Confidence:** high: Accurate attribution to the author; not a universal icon vocabulary.

**Sources and locators:** GDR-SRC-20261010-P01-12 — Affordance; Perceived affordance; Cultural constraints, cultural conventions; conclusion.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Will this audience interpret the signifier as intended?

### C-03

**Claim:** WCAG 2.2 specifies scoped web criteria for color reliance, contrast and reflow; these are not universal native-game settings. **Class:** `formal-standard`. **Confidence:** high: The cited Recommendation supplies the criteria; applicability must be established.

**Sources and locators:** GDR-SRC-20261010-P01-01 — Status of This Document; §§1.3.3, 1.4.1, 1.4.3, 1.4.10, 1.4.11; §§2.4.3, 2.4.7, 2.4.11–2.4.13; §§2.5.7–2.5.8; conformance scope.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which components and exceptions fall within the chosen conformance scope?

### C-04

**Claim:** XAG 101 measures text body height and distinguishes platform/resolution contexts. **Class:** `practitioner-heuristic`. **Confidence:** high: Explicit vendor guidance, not a psychophysical guarantee.

**Sources and locators:** GDR-SRC-20261010-P01-04 — Background and foundational information → measuring text body height; Implementation guidelines → Text size, Text scaling, Font, and language-dependent alignment.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** What remains readable at actual viewing distance, scale, script and motion?

### C-05

**Claim:** Valve reports silhouette and controlled-detail choices in its 2007 TF2 rendering approach. **Class:** `practitioner-heuristic`. **Confidence:** moderate: Firsthand design account without comparative player measurements.

**Sources and locators:** GDR-SRC-20261010-P01-13 — Introduction; §3 Commercial Illustration Techniques; §4.1 Character Modeling; Figure 2, PDF p.2. PDF page image inspected.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Do those choices transfer to this task, projection and visual style?

### C-06

**Claim:** The 2005 feature-congestion experiment relates a model to human clutter rankings of printed maps, not gameplay performance. **Class:** `empirical-evidence`. **Confidence:** moderate: Methods/results inspected; limited stimuli and subjective ranking task.

**Sources and locators:** GDR-SRC-20261010-P01-16 — Experiment: Clutter Rankings for Maps; Results, printed pp.767–768 (PDF pp.7–8); Figure 2 and Conclusions on printed p.768/PDF p.8. Page image inspected.

**Support / contrary treatment:** Direct within the source’s stated scope; the surrounding application is not thereby validated. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Does the proposed visual change improve the actual task rather than only apparent simplicity?

### C-07

**Claim:** Build a semantic visual grammar and assign salience according to decision relevance, not decoration alone. **Class:** `inference`. **Confidence:** moderate: Reasoned synthesis from conventions and production/perception evidence; no optimal hierarchy measured.

**Sources and locators:** GDR-SRC-20261010-P01-12 — Affordance; Perceived affordance; Cultural constraints, cultural conventions; conclusion.; GDR-SRC-20261010-P01-13 — Introduction; §3 Commercial Illustration Techniques; §4.1 Character Modeling; Figure 2, PDF p.2. PDF page image inspected.; GDR-SRC-20261010-P01-16 — Experiment: Clutter Rankings for Maps; Results, printed pp.767–768 (PDF pp.7–8); Figure 2 and Conclusions on printed p.768/PDF p.8. Page image inspected.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** When does consistency obscure distinctions or compete with required content?

### C-08

**Claim:** Use non-color state encoding and an appropriate alternative channel for essential facts; do not equate two visual encodings with nonvisual access. **Class:** `inference`. **Confidence:** moderate: Channel independence follows from the information requirement; actual comprehension is untested.

**Sources and locators:** GDR-SRC-20261010-P01-01 — Status of This Document; §§1.3.3, 1.4.1, 1.4.3, 1.4.10, 1.4.11; §§2.4.3, 2.4.7, 2.4.11–2.4.13; §§2.5.7–2.5.8; conformance scope.; GDR-SRC-20261010-P01-05 — Visual options; Audio options; Haptic options; Color vision deficiency; Implementation guidelines for important information.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Can the player obtain equivalent task facts using their available channels?

### C-09

**Claim:** Silhouette, contrast and text reviews need multiple task states, viewpoints and access settings; a still-image pass is insufficient evidence of in-play readability. **Class:** `inference`. **Confidence:** moderate: Each manipulation can change the presented signal; no universal test matrix or threshold is validated.

**Sources and locators:** GDR-SRC-20261010-P01-04 — Background and foundational information → measuring text body height; Implementation guidelines → Text size, Text scaling, Font, and language-dependent alignment.; GDR-SRC-20261010-P01-13 — Introduction; §3 Commercial Illustration Techniques; §4.1 Character Modeling; Figure 2, PDF p.2. PDF page image inspected.; GDR-SRC-20261010-P01-10 — Implementation guidelines → moving, blinking, scrolling and auto-updating UI; pausing, hiding or disabling distractions.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Which combinations are feasible and representative for the intended release?

### C-10

**Claim:** The proposed process, illustrations and tests may reveal communication failures and support choosing a simpler or more legible design. **Class:** `hypothesis`. **Confidence:** low: Prospective synthesis; no prototype, participants, comparisons or effect estimates here.

**Sources and locators:** GDR-SRC-20261010-P01-11 — Introduction; Considerations for including users; Range of users; Combining user evaluation with standards; interpreting evaluation findings.; GDR-SRC-20261010-P01-16 — Experiment: Clutter Rankings for Maps; Results, printed pp.767–768 (PDF pp.7–8); Figure 2 and Conclusions on printed p.768/PDF p.8. Page image inspected.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Will task outcomes improve without unacceptable clutter, fatigue or lost meaning?

### C-11

**Claim:** Localization, adjustable presentation and semantic consistency create content and regression obligations, not a fixed production cost. **Class:** `inference`. **Confidence:** moderate: Identifiable dependencies; cost magnitude and cultural transfer unknown.

**Sources and locators:** GDR-SRC-20261010-P01-04 — Background and foundational information → measuring text body height; Implementation guidelines → Text size, Text scaling, Font, and language-dependent alignment.; GDR-SRC-20261010-P01-12 — Affordance; Perceived affordance; Cultural constraints, cultural conventions; conclusion.; GDR-SRC-20261010-P01-05 — Visual options; Audio options; Haptic options; Color vision deficiency; Implementation guidelines for important information.

**Support / contrary treatment:** Indirect support or original reasoning only; alternatives and failure cases remain live. **Applicability:** the decision and context bounded in this entry, not every game/platform. **Unresolved:** Can the team maintain each supported variation?

## References

All identities below are **temporary P01 source candidates**. Access date: **2026-10-10**. `relevant-excerpt` means the cited passages were inspected, not every linked resource. Repeated records enable standalone reading and are not independent corroboration. Cross-batch reconciliation by canonical URL/DOI/edition remains pending.

### GDR-SRC-20261010-P01-01

**World Wide Web Consortium (W3C).** [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/2024/REC-WCAG22-20241212/). W3C. **Publication/update:** 2024-12-12. **Edition/version:** W3C Recommendation, WCAG 2.2, dated revision.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Normative accessibility specification (formal-standard within its scope). **Precise inspected locators:** Status of This Document; §§1.3.3, 1.4.1, 1.4.3, 1.4.10, 1.4.11; §§2.4.3, 2.4.7, 2.4.11–2.4.13; §§2.5.7–2.5.8; conformance scope.

**Inspected access route:** [public copy](https://www.w3.org/TR/WCAG22/). **Local claims:** C-03, C-08. **Limits:** Web-content criteria, not automatic native-game conformance, legal advice, or a complete audit. Exceptions and conformance level matter. No universal native display or controller size follows.

**Independence/derivation:** Source 02 interprets this family for non-web use; several XAG resource lists refer to WCAG. Those are not independent experiments. **Rights:** W3C document copyright/use terms apply; paraphrase only, no reproduced figures.

### GDR-SRC-20261010-P01-04

**Microsoft.** [Xbox Accessibility Guideline 101: Text display](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/101). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Background and foundational information → measuring text body height; Implementation guidelines → Text size, Text scaling, Font, and language-dependent alignment.

**Local claims:** C-04, C-09, C-11. **Limits:** Pixel body height is not a font point/em size. Display category and resolution are explicit. Numeric suggestions are vendor guidance, not universal perception thresholds.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-05

**Microsoft.** [Xbox Accessibility Guideline 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Visual options; Audio options; Haptic options; Color vision deficiency; Implementation guidelines for important information.

**Local claims:** C-01, C-08, C-11. **Limits:** Alternative channels are recommended; no task-time, comprehension-equivalence, or affect-equivalence experiment is supplied.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-10

**Microsoft.** [Xbox Accessibility Guideline 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117). Microsoft Learn. **Publication/update:** Page last updated 2026-03-04; original publication date unknown. **Edition/version:** V3.2 suite context; unnumbered live page revision inspected on access date.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official vendor accessibility guidance (practitioner-heuristic). **Precise inspected locators:** Implementation guidelines → moving, blinking, scrolling and auto-updating UI; pausing, hiding or disabling distractions.

**Local claims:** C-09. **Limits:** Motion controls do not establish photosensitivity safety, camera comfort across platforms, or an appropriate numerical limit.

**Independence/derivation:** Same issuer and suite as source 03; not independent corroboration of other XAGs. Linked third-party materials and embedded media are not inspected support. **Rights:** Content reuse license not separately inspected; paraphrase only; no game screenshots or video redistributed.

### GDR-SRC-20261010-P01-11

**W3C Web Accessibility Initiative, Education and Outreach Working Group; editor Shawn Lawton Henry.** [Involving Users in Evaluating Web Accessibility](https://www.w3.org/WAI/test-evaluate/involving-users/). W3C WAI. **Publication/update:** First published 2005-11; content updated 2021-06-01; links updated 2024-04-30. **Edition/version:** Dated informative WAI web guidance.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Official evaluation guidance (practitioner-heuristic). **Precise inspected locators:** Introduction; Considerations for including users; Range of users; Combining user evaluation with standards; interpreting evaluation findings.

**Local claims:** C-10. **Limits:** Web evaluation guidance, not a game-specific sampling theorem. A few users cannot stand in for every disability, device, or language.

**Independence/derivation:** Same standards organization as sources 01–02, different informative purpose; not a new empirical dataset. **Rights:** W3C document copyright/use terms apply; paraphrase only.

### GDR-SRC-20261010-P01-12

**Don Norman.** [Affordances and Design](https://jnd.org/affordances-and-design/). Don Norman / jnd.org. **Publication/update:** 2008-11-17. **Edition/version:** Author-hosted essay, dated web edition.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Primary practitioner/conceptual account (practitioner-heuristic). **Precise inspected locators:** Affordance; Perceived affordance; Cultural constraints, cultural conventions; conclusion.

**Local claims:** C-01, C-02, C-07, C-11. **Limits:** Distinguishes action possibilities, perceived possibilities and conventions; not a cross-cultural symbol-recognition experiment.

**Independence/derivation:** Original author explanation; older works referenced in it were not inspected as additional sources. **Rights:** Reuse license unknown in inspected text; paraphrase only.

### GDR-SRC-20261010-P01-13

**Jason Mitchell, Moby Francke, Dhabih Eng (Valve).** [Illustrative Rendering in Team Fortress 2](https://steamcdn-a.akamaihd.net/apps/valve/2007/NPAR07_IllustrativeRenderingInTeamFortress2.pdf). NPAR / Valve-hosted author paper. **Publication/update:** 2007; exact publication day unknown. **Edition/version:** NPAR 2007 paper, Valve-hosted PDF; production build unspecified.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Firsthand production explanation (practitioner-heuristic); inspectable paper figure, not a played-game observation. **Precise inspected locators:** Introduction; §3 Commercial Illustration Techniques; §4.1 Character Modeling; Figure 2, PDF p.2. PDF page image inspected.

**Local claims:** C-05, C-07, C-09. **Limits:** Reported silhouette and detail choices are not controlled player-response results. No game build, performance benchmark or commercial-causation claim.

**Independence/derivation:** One production team and historical context; source is not independent validation of its own design intent. **Rights:** Paper/game imagery rights retained by respective holders; reuse permission not established. No figures/assets redistributed.

### GDR-SRC-20261010-P01-16

**Ruth Rosenholtz, Yuanzhen Li, Jonathan Mansfield, Zhenlan Jin.** [Feature Congestion: A Measure of Display Clutter](https://www.mit.edu/~yzli/clutter.pdf). ACM CHI; MIT author-hosted copy. **Publication/update:** 2005; CHI conference 2005-04-02 to 2005-04-07. **Edition/version:** CHI 2005 paper, pp.761–770; MIT-hosted PDF; DOI not independently verified.

**Access:** relevant-excerpt; checked 2026-10-10. **Type:** Original display-perception study (empirical-evidence). **Precise inspected locators:** Experiment: Clutter Rankings for Maps; Results, printed pp.767–768 (PDF pp.7–8); Figure 2 and Conclusions on printed p.768/PDF p.8. Page image inspected.

**Local claims:** C-06, C-07, C-10. **Limits:** Clutter rankings of printed maps, not game-task performance or a universal information-density threshold. Individual judgments differed; no reanalysis.

**Independence/derivation:** Original 2005 work; related 2007 Measuring visual clutter paper remains a separate uninspected lead. **Rights:** ACM copyright/personal or classroom-use notice; no paper pages or figures redistributed.

## Open questions and change history

**2026-10-10 — 0.1.0, initial draft.** Bounded P01 public-source research and author synthesis only. Source inspection does not establish production approval, participant validation or acceptance of a recommendation. The author’s challenge and actual document checks are recorded in the [batch review packet](../reviews/full-run-20261010-p01-review-packet.md). Independent review has not occurred. Formal reviewer and approval fields remain null.

Open questions include transfer across platforms, viewing/listening contexts, languages, input and assistive technologies; interactions between access needs; novice/expert differences; maintenance cost; and the comparative value of the proposed alternatives. Resolve source-reporting and dependency gaps before widening claims. No genre entry, canonical integration, permanent ID allocation, live host validation or release is asserted.

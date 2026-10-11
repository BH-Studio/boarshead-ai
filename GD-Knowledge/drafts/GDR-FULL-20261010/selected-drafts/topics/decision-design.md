---
id: GDR-CAND-20261010-F02-TOP-01
kind: topic
title: Decision design
version: 0.1.0
status: draft
candidate_revision: initial-capture-1
attempt_identity: F02-local-attempt-01
predecessor_sha256: null
supersedes: null
change_summary: Initial F02 capture; preserves inspected first-wave corrections; no
  prior batch artifacts resubmitted.
owner_project: BH-GDR-Foundations-and-Systems
run_id: GDR-FULL-20261010
batch_key: F02
updated: '2026-10-10'
evidence_checked: '2026-10-10'
aliases:
- meaningful choice
- risk and reward
- decision information
- reversibility
- opportunity cost
tags:
- decision-design
- uncertainty
- agency
- commitment
- resource-tradeoffs
related_topics:
- GDR-CAND-20261010-F02-TOP-02
related_patterns:
- GDR-CAND-20261010-F02-PAT-01
- GDR-CAND-20261010-F07-PAT-02
- GDR-CAND-20261010-F01-PAT-01
related_genres: []
source_ids:
- GDR-SRC-20261010-F02-001
- GDR-SRC-20261010-F02-002
- GDR-SRC-20261010-F02-003
- GDR-SRC-20261010-F02-004
- GDR-SRC-20261010-F02-005
- GDR-SRC-20261010-F02-010
reviewer: null
approved_by: null
approved_date: null
---

# Decision design

**Draft research candidate, not released guidance.** Version 0.1.0; revision initial-capture-1. This is a conditional design synthesis, not a finding that uncertainty, branching, punishment, or a particular number of options universally makes choices meaningful. Research authorization is not adoption approval.

## Decision and scope

This entry helps decide **what a player can know, what alternatives remain feasible, what choosing commits, and what consequences remain recoverable**. It covers information, uncertainty, risk and reward, meaningful choice, commitment, reversibility and opportunity cost. It excludes complete economy models, monetization policy, narrative branch authoring, encounter composition and interface implementation. Those decisions require their owning topics and a game’s approved context.

The following vocabulary is an analytical convention, not a formal standard. A **decision** is selecting or declining an available action given a perceived state and a goal. A **meaningful choice**, for this draft, is one a player can connect to a valued difference: practical outcome, expression, discovery, relationship, or commitment. It need not maximize currency, create a unique content branch, or prevent later regret. **Decision quality** concerns the process and information available when choosing; **outcome quality** concerns what subsequently happened. A sensible risky decision can fail. [C-01]

Distinguish the designer’s intended task from the player’s current goal. A player may understand a risk and decline it, prefer an expressive action with lower material return, or enjoy solving a deterministic problem. Observed selection alone cannot identify misunderstanding or “bad play.” This distinction also governs the proposed tests below. [C-01, C-09, C-13]

## Core explanation and mechanisms

### An information contract, not maximum disclosure

For each decision, record the true state, the information legitimately available to this player, the action-to-consequence relationship, and what is intentionally uncertain. The proposed **information contract** separates four questions: can the player detect relevant information, interpret it, use it to distinguish feasible actions, and connect subsequent feedback to the action? A failure at one question does not establish failure at the others. [C-08]

| Uncertainty under examination | Design lever | What must not be silently conflated |
|---|---|---|
| Unknown current state | Observation, scouting, queries, remembered evidence | A hidden fact versus an inaccessible presentation of an available fact |
| Unknown rule or model | Demonstration, experimentation, explicit rule, feedback | Learning a stable relation versus repeatedly guessing an arbitrary change |
| Variable outcome under a known model | Distribution, range, sequence constraints, risk exposure | Probability versus certainty; independent draws versus correlated events |
| Another agent’s future action | Signals, commitments, counterplay, simultaneous choice | Strategic uncertainty versus undocumented privileged information |
| Unknown future value | Time horizon, changing objectives, option preservation | Current price versus future usefulness or forgone alternatives |

This table is an inference for diagnosis, not an empirically established exhaustive taxonomy. More information can also reveal a solution the player wanted to infer. Make **available information accessible**, while separately deciding whether the underlying fact is meant to be discoverable now. A readable “unknown” may preserve the intended question better than either an inaccessible cue or an answer-revealing assist. [C-08, C-12]

**Evidence boundary.** In a fixed-order text adventure with 88 online volunteers, Cardona-Rivera and colleagues found support on several retrospective agency measures for choices differing in situational content. Some measures did not support the contrast; one analysis used a post-hoc exclusion. This suggests testing whether players foresee valued differences, not claiming that every choice needs a permanent branch. [C-02; GDR-SRC-20261010-F02-001]

### Stated risk is not experienced risk

Hertwig and colleagues compared descriptions with freely sampled experience in paid decisions involving 100 students. Structurally equivalent options produced different choice patterns; five of six comparisons were significant. Sampling and rare-event experience help explain the discrepancy, but the experiment is not a game-wide prescription for probabilities or sample counts. [C-03; GDR-SRC-20261010-F02-002]

The design implication is to test **how the player obtained the model**, not merely whether a probability is displayed. When a low-frequency loss has not appeared in a short trial, “I have not seen it” is not evidence that it cannot happen. Conversely, a numerical probability can be truthful but poorly understood. Preserve the distinction between a guaranteed outcome, an estimated range, a known distribution, and an unknown mechanism. Do not display invented precision to disguise missing knowledge. [C-08]

A risk/reward comparison also needs a unit, horizon, and constraint. Expected reward alone cannot express a survival threshold, a deadline, irrecoverable losses, or a player’s expressive preference. When outcomes share a hidden common cause, treating successive choices as independent can understate exposure. These are consequences of the specified model, not a universal account of player risk preferences. [C-09]

### Opportunity cost and option count

Maguire and colleagues’ meta-analysis covered 39 experiments, 12,093 participants and 14,005 observations, mostly hypothetical decisions. Making alternative resource uses salient shifted choices by a small average amount; the reported estimate weakened when original outlier studies were excluded. This supports investigating neglected alternatives, not declaring that a reminder improves game enjoyment or that choosing not to spend is inherently correct. [C-05; GDR-SRC-20261010-F02-005]

**Application bridge:** a listed price shows what is spent; an opportunity-cost comparison shows a feasible use displaced by that spending. A truthful display of remaining capacity may help players evaluate their own priorities. That causal transfer into games remains a hypothesis. Showing only a designer-favored alternative can instead steer the decision, and showing imaginary alternatives is misinformation. [C-09, C-11]

Do not turn “meaningful choice” into a target option count. Scheibehenne and colleagues synthesized 63 conditions from 50 experiments, involving 5,036 participants: the pooled overload effect was near zero, with substantial heterogeneity. Neither “more is always better” nor “more is always worse” follows. Diagnose similarity, search effort, player expertise, presentation and decision stakes locally. [C-04; GDR-SRC-20261010-F02-003]

### Commitment is multidimensional

Distinguish cancellation before execution, correction of accidental activation, reversal of a deliberate outcome, and erasure of information learned. An undo system may restore resources without making a revealed answer unknown. A respec may restore build flexibility without retracting consequences imposed on other players. Define the boundary before treating “reversible” as a single property. [C-10]

There is genuine contrary evidence to effortless reversibility as a universal good: Gilbert and Ebert’s photography-course Study 1 found greater relative liking of a retained print under unchangeable choices. It recruited 64 students, with exclusions and small analyzed groups; forecaster versus experiencer assignment was not randomized. This narrow satisfaction result cannot justify denying error recovery, consent, or game assistance. [C-06; GDR-SRC-20261010-F02-004]

Microsoft’s XAG 115 recommends review, correction and reversal safeguards around erroneous or destructive actions, including alternatives to confirmation holds. It is vendor guidance, not a study proving a specific confirmation flow effective, and not a rule that every intended strategic setback must be erased. [C-07; GDR-SRC-20261010-F02-010]

The proposed compromise is **deliberate commitment with explicit boundaries**, not compulsory irreversibility: protect against accidental activation; disclose the kind of commitment; let the game’s approved experience determine which deliberate consequences persist. The existing first-wave commitment pattern owns the broader safe-exit recipe; this topic does not rename or duplicate it. [C-10]

## Design choices and alternatives

| Choice | Appropriate question and conditional benefit | Costs, dependencies and simpler alternative |
|---|---|---|
| Exact outcomes versus bounded uncertainty | Is deduction, planning, suspense or discovery the intended activity? Expose enough structure to support that activity. | Exact previews may solve it; vague labels may hide all actionable differences. A categorical range may suffice when defensible. |
| Free information versus costed probing | Should obtaining information itself consume time or scarce capacity? | Costed probes can punish those learning the interface. First establish accessible baseline facts; omit the probe if it only adds a toll. |
| Several comparable options versus staged selection | Are differences meaningful now, or only after another prerequisite decision? | Staging reduces simultaneous comparison but may obscure global tradeoffs. Keep a comparison/history path where necessary. |
| Opportunity-cost comparison versus price alone | Are players missing a real displaced alternative? | Additional detail can distract or steer. Retain price alone when the opportunity is already obvious or not knowable. |
| Provisional plan versus immediate execution | Does the activity depend on reviewing a combination before committing? | Planning can remove time pressure or create information-rewind exploits. A constrained preview may preserve the intended task. |
| Persistent consequence versus inexpensive retry | Does persistence serve a valued commitment, not merely inflate time lost? | Harsh loss may favor excessive caution or repeating safe actions. Offer a declared alternate mode where compatible; do not assume one policy fits shared competition. |

These are design alternatives inferred from C-01 and C-08–C-12, not treatment effects. A dominant option is a warning only relative to the intended objective and constraints. It may be appropriate when the point is expression, accessibility, a straightforward reward, or a temporary learning step rather than optimization. [C-09]

## Application process

1. **Frame the decision.** Specify player goal, available actions including decline, information access, horizon, scarce resources, affected parties, and the difference the choice is intended to express. State what would count as success without assuming a favored action.
2. **Model the consequences.** Write a compact state-and-consequence table. Separate owned, reserved and spendable quantities; distinguish certain costs from uncertain outcomes. Mark assumptions and opportunities that disappear over time.
3. **Audit the information contract.** Ask what a player can reasonably know at commitment, what a probe reveals, and whether an access option changes only the communication or also supplies the answer. Coordinate presentation and narrative ownership rather than silently changing either.
4. **Choose the least burdensome intervention.** Compare a clearer description, an optional comparison, a reversible plan, an information probe and no intervention. Do not combine them before identifying the suspected failure.
5. **Prepare a bounded prototype specification.** Hold rules, rewards and available alternatives constant while changing the chosen lever. No prototype was implemented in F02.
6. **Evaluate understanding and preference separately.** Use predictions of feasible actions and consequences, then ask what the player chooses and why. Include a changed case with a different correct answer and an exact-boundary case. Preserve ordinary information and accommodations.
7. **Revise or stop.** Remove the intervention if it offers no relevant comprehension benefit, makes the intended discovery trivial, misrepresents alternatives, or creates unacceptable access/production cost. Retain uncertainty in the record when results are inconclusive.

This process is a proposed application method [C-08–C-13]. It preserves the corrected F01 distinction between a rule-based prediction and a player’s preferred action; correct repetition is not evidence of durable transfer.

## Patterns and genre adaptations

Use [Visible opportunity-cost comparison](../patterns/visible-opportunity-cost-comparison.md), `GDR-CAND-20261010-F02-PAT-01`, when the specific suspected problem is a neglected feasible alternative. Use [Challenge and difficulty](challenge-and-difficulty.md) for distinguishing a decision’s uncertainty from execution demand and failure cost.

The inspected first-wave pattern `GDR-CAND-20261010-F07-PAT-02`, **Legible commitment and safe exit**, remains the home for broad disclosure and exit design; `GDR-CAND-20261010-F01-PAT-01`, **Supported attempt and transfer check**, supplies corrected assessment cautions. Their files are deliberately not resent. Access, hashes and proposed package-relative links are recorded in the [dependency register](../reviews/full-run-20261010-f02-review-packet.md#dependency-register).

No genre rule is asserted. An inference-led activity may protect the answer while exposing what evidence exists; an expressive activity may retain choices with equivalent mechanical outcomes; shared competition may constrain what can be undone. Those are conditional examples, not substitutes for separate genre guidance. Hybrid conflicts require a declared experience priority, not automatic precedence for a genre label. [C-08–C-12]

## Examples and counterexamples

### Illustrative calculation: equal expected reward, different decisions

Consider two invented actions. Action A yields 6 units certainly. Action B yields 12 units with probability 0.5 and 0 units otherwise. Both have expected reward 6, under these explicit probabilities and a linear reward measure. If this single outcome must fund a 4-unit requirement, A meets it certainly while B does so with probability 0.5. A player seeking the largest possible payout may nevertheless knowingly choose B. These values are arithmetic illustrations, not balance settings or observed behavior. [C-09]

The design mistake would be calling B irrational merely because it loses, or saying A is always superior without specifying the goal. A second mistake would be calling the choice meaningful merely because randomness exists: if neither option’s consequence is intelligible and selection cannot express a preference, randomness alone supplies no such evidence. [C-01, C-14]

### Illustrative opportunity cost: an affordable purchase that is not preferred

An invented player has 12 units, 3 reserved, leaving 9 spendable. A tool costs 6 and leaves 3 spendable; a different planned action costs 4. Buying the tool is permitted, but doing both immediately is not. An optional comparison can say what remains and which known action no longer fits. It should not label keeping funds as the correct moral or strategic answer. The player may abandon the other plan knowingly. [C-09, C-11]

### Illustrative irreversibility: preview versus revelation

A planning view can let a player rearrange uncommitted moves without cost. Executing a reconnaissance move reveals a hidden fact. Restoring the movement resource cannot remove that knowledge. A design may therefore allow free planning before revelation, then specify a different reset policy afterward. Such a boundary needs truthful communication and an access route that does not accidentally execute reconnaissance. There is no claim that this is preferable in every game. [C-10, C-12]

### Strongest counterexample

A player can face a meaningful, fully deterministic choice between incompatible values with no failure punishment. Conversely, a random, opaque, irreversible choice can offer no learnable distinction. These constructed counterexamples disprove the logical necessity of randomness or harsh loss in this draft’s definition; they are not empirical claims about all audiences’ experiences. [C-01, C-14]

## Failure modes and constraints

**Incentives and exploitability.** Check whether a safe option dominates every intended goal, whether information can be farmed by undoing costs, whether repeated low-risk grinding replaces intended decisions, and whether commitment consumes resources needed to escape a failed state. A fixed random seed may prevent rerolling but does not prevent knowledge acquisition. These are model audits, not findings from a tested implementation. [C-09–C-12]

**Access and localization.** Distinguish uncertainty about the world from inability to perceive a cue, remember a transient list, calculate a relation, operate a timed control, or understand translated probability language. Offer equivalent response routes and persistent access to entitled information. Do not import P01’s scoped web or platform numbers as universal game settings, and do not withdraw accommodations when someone performs well. Actual translation, assistive technology and display behavior were not tested. [C-12]

**Ethics and production.** Disclosing a cost does not make an unwanted commitment acceptable. Comparisons can manipulate through selective alternatives or asymmetric wording. Resource dependencies, network races, localization variants, save restoration and mode combinations all create verification work. A smaller truthful explanation is preferable to a precise-looking preview the system cannot keep accurate. These recommendations are inferences, not approved studio policy. [C-10–C-12]

## Playtest and validation

**PROPOSED — NOT PERFORMED.** Recruit for the intended audience, including varied rule familiarity, language proficiency and relevant access needs; do not infer needs from demographic labels. Determine sample and decision thresholds from the intended inference and local constraints before collecting data. [C-13]

**Comparison A: information representation.** Hold action outcomes and distributions constant; compare exact probabilities, a justified categorical description, and an experience/probe route. State whether the study tests equal information content or real-world acquisition differences; it cannot assume both. Ask for consequence predictions, confidence and preferred action before revealing outcomes. Measure prediction calibration, misunderstandings, decision effort, valued agency and unwanted surprises separately. Control order, prior familiarity, sample exposure and outcome sequence; repeated exposure changes knowledge.

**Comparison B: opportunity-cost display.** Compare price/remaining-resource information with the same information plus truthful displaced alternatives. Include feasible, infeasible and exact-boundary cases; vary both correct responses and order. Record comprehension before preference. Preference shifts alone do not validate the pattern. Reject or revise if accuracy does not improve in the targeted misunderstanding, if the display systematically misleads, or if its burden outweighs a locally specified benefit.

**Comparison C: commitment and recovery.** Compare an explicit provisional stage with direct commitment plus appropriate accidental-input safeguards. Keep intended consequences identical. Measure accidental commitments, prediction of persistence, discovery value and exploitation opportunities. Reject the proposed boundary when it removes the activity’s valued uncertainty, denies an essential recovery route, or fails to distinguish accidents from intended risk. Ethical consent and participant stopping rights must remain; a punitive test condition is not automatically authorized.

No single short check certifies learning transfer, enjoyment across sessions, or fairness for all players. Do not interpret a nonsignificant result as equivalence without a design that can support that inference. [C-13]

## Claim ledger

Each row is local to this entry. “Support” describes what was inspected; “bridge” identifies a new interpretation. None of the hypotheses is an approved studio decision.

| ID | Precise claim and class | Support / contrary evidence and locator | Applicability, confidence and unresolved question |
|---|---|---|---|
| C-01 | Meaningful choice is operationalized as a knowable connection to valued difference; choice and outcome quality differ. `inference` | Analytical framing; motivated but not universally defined by source 001, Method/limitations. | Moderate: useful distinction, not a validated universal definition. Which kinds of value matter locally? |
| C-02 | Situationally distinct text-adventure choices received support on several, not all, agency measures. `empirical-evidence` | GDR-SRC-20261010-F02-001, pp. 11–14, Tables 5–6. | Moderate: narrow task, fixed sequence and retrospective reports. Would a prospective manipulation generalize? |
| C-03 | Descriptions and sampled experience can yield different risky choices in equivalent payoff tasks. `empirical-evidence` | GDR-SRC-20261010-F02-002, pp. 535–539, Table 1. | Moderate: original laboratory comparison; not a universal direction under every exposure history. |
| C-04 | The inspected overload meta-analysis does not support a universal effect of option count. `empirical-evidence` | GDR-SRC-20261010-F02-003, Method/Results, p. 413. | Moderate: heterogeneous older corpus; conditional effects remain. |
| C-05 | Alternative-use salience changes choices on average in the inspected opportunity-cost corpus. `empirical-evidence` | GDR-SRC-20261010-F02-005, §§2–4; sensitivity and hypothetical-task limits. | Moderate: pooled evidence, not game outcome or welfare evidence. |
| C-06 | Unchangeability increased relative liking of a retained print in the inspected Study 1. `empirical-evidence` | GDR-SRC-20261010-F02-004, pp. 505–507. | Low for game transfer; narrow satisfaction outcome and small groups. It does not license unsafe irreversibility. |
| C-07 | XAG 115 recommends error/destructive-action safeguards, including alternatives to holds. `practitioner-heuristic` | GDR-SRC-20261010-F02-010, Scoping and Implementation guidelines. | High for attribution; no measured effectiveness or universal native-game conformance follows. |
| C-08 | Match information disclosure to the intended reasoning task, while preserving access to entitled facts. `inference` | Bridge from C-02/C-03 and source 010; alternative is maximal disclosure or deliberate opacity. | Moderate rationale; local optimal disclosure remains untested. |
| C-09 | Resource feasibility, goal thresholds and forgone alternatives can change a decision without changing expected reward. `inference` | Explicit arithmetic/model assumptions in examples; C-05 motivates salience, not the arithmetic. | High within the stated examples; low as a prediction of preferences. |
| C-10 | Separate accidental-input recovery, strategic commitment and irreversible information revelation. `hypothesis` | Bridge from C-06/C-07; inspected F07 commitment pattern is draft context, not efficacy proof. | Moderate design rationale; optimal boundaries need local testing. |
| C-11 | A truthful feasible-alternative comparison may improve opportunity-cost comprehension. `hypothesis` | GDR-SRC-20261010-F02-005, §§2–4; translation from non-game tasks is unvalidated. | Low for game benefit; a preference nudge or overload may explain effects. |
| C-12 | Access, wording, stale previews and information-rewind exploits can invalidate the intended contract. `inference` | State-model analysis, C-07 and inspected P01 scope corrections. | Moderate reasoning; no implementation or population coverage test occurred. |
| C-13 | The proposed comparisons may discriminate comprehension from preference and unintended intervention effects. `hypothesis` | Author-designed procedures; corrected F01 prediction/preference distinction retained. | Low until performed; sample validity, carryover and demand effects remain. |
| C-14 | Neither more uncertainty nor harsher failure logically guarantees meaningful choice. `inference` | C-01 definition and constructed counterexamples; no supplied empirical study tests that universal conjunction. | High for rejecting necessity under the stated definition; audience preferences remain empirical questions. |

## References

Access date for every record below: **2026-10-10**. These are temporary source candidates. A repeated record is the same evidence, not additional corroboration. “Relevant-excerpt” identifies inspected substantive passages, not merely an abstract and not every linked supplement.

### GDR-SRC-20261010-F02-001

**Rogelio E. Cardona-Rivera, Justus Robertson, Stephen G. Ware, Brent Harrison, David L. Roberts, and R. Michael Young.** [Foreseeing Meaningful Choices](https://ojs.aaai.org/index.php/AIIDE/article/download/12716/12564/16233). AAAI, AIIDE 10(1), pp. 9–15. **Publication/update:** 2014-10-08. **Edition/version:** 2014 proceedings paper; publisher PDF.

**DOI:** [10.1609/aiide.v10i1.12716](https://doi.org/10.1609/aiide.v10i1.12716).

**Access:** relevant-excerpt. **Source type:** original empirical study. **Inspected locators:** Method and Results, pp. 11–14; Tables 5–6 on p. 13; limitations following results. **Supports local claims:** C-01, C-02, C-08

**Limits:** One fixed-order text adventure; retrospective agency reports; item-level exceptions and a post-hoc exclusion. No general causal test of all choice designs. **Independence:** Publisher landing page and PDF are one work, not independent evidence. **Rights:** AAAI copyright; paraphrase only; no tables or figures redistributed

### GDR-SRC-20261010-F02-002

**Ralph Hertwig, Greg Barron, Elke U. Weber, and Ido Erev.** [Decisions From Experience and the Effect of Rare Events in Risky Choice](https://business.columbia.edu/sites/default/files-efs/imce-uploads/CDS/Weber_RareEvents.pdf). Psychological Science 15(8), pp. 534–539. **Publication/update:** 2004-08. **Edition/version:** 2004 journal article; author-faculty-hosted copy.

**DOI:** [10.1111/j.0956-7976.2004.00715.x](https://doi.org/10.1111/j.0956-7976.2004.00715.x).

**Access:** relevant-excerpt. **Source type:** original empirical study. **Inspected locators:** Method, Results, and Limited Information Search, pp. 535–539; Table 1, p. 536. **Supports local claims:** C-03, C-08

**Limits:** Paid laboratory choices, not sustained game play; freely sampled experiences and descriptions differ in information acquisition. One of six comparisons did not reach significance. **Independence:** One original study; discussions of other experiments are not separately inspected corroboration. **Rights:** Psychological Science/APS copyright; paraphrase only

### GDR-SRC-20261010-F02-003

**Benjamin Scheibehenne, Rainer Greifeneder, and Peter M. Todd.** [Can There Ever Be Too Many Options? A Meta-Analytic Review of Choice Overload](https://www.scheibehenne.de/ScheibehenneGreifenederTodd2010.pdf). Journal of Consumer Research 37(3), pp. 409–425. **Publication/update:** 2010-02-10 online; 2010-10 issue. **Edition/version:** 2010 journal article; author-hosted copy.

**DOI:** [10.1086/651235](https://doi.org/10.1086/651235).

**Access:** relevant-excerpt. **Source type:** original meta-analysis. **Inspected locators:** Method and Results; overall effect and heterogeneity, p. 413. **Supports local claims:** C-04

**Limits:** Heterogeneous non-game choice tasks; near-zero pooled effect does not exclude contextual overload; not an up-to-date exhaustive review. **Independence:** Contains earlier choice-overload experiments; those originals are not additional independent evidence in this batch. **Rights:** Journal of Consumer Research copyright; paraphrase only

### GDR-SRC-20261010-F02-004

**Daniel T. Gilbert and Jane E. J. Ebert.** [Decisions and Revisions: The Affective Forecasting of Changeable Outcomes](https://dtg.sites.fas.harvard.edu/Gilber%20t%26%20Ebert%20%28DECISIONS%20%26%20REVISIONS%29.pdf). Journal of Personality and Social Psychology 82(4), pp. 503–514. **Publication/update:** 2002-04. **Edition/version:** 2002 journal article; Harvard author-hosted copy.

**DOI:** [10.1037/0022-3514.82.4.503](https://doi.org/10.1037/0022-3514.82.4.503).

**Access:** relevant-excerpt. **Source type:** original empirical study. **Inspected locators:** Study 1, Method and Results, pp. 505–507. **Supports local claims:** C-06, C-10

**Limits:** Photography-course choices; small analyzed subgroups and exclusions; forecaster/experiencer grouping was not randomized. Liking a print is not valuing safety or agency in a game. **Independence:** One paper; its later studies were not inspected sufficiently for separate empirical claims here. **Rights:** American Psychological Association copyright; paraphrase only

### GDR-SRC-20261010-F02-005

**Allegra Maguire, Emil Persson, and Gustav Tinghög.** [Opportunity cost neglect: a meta-analysis](https://link.springer.com/article/10.1007/s40881-023-00134-6). Journal of the Economic Science Association 9, pp. 176–192. **Publication/update:** 2023-07-02 version of record; 2023-12 issue. **Edition/version:** 2023 version of record, publisher HTML.

**DOI:** [10.1007/s40881-023-00134-6](https://doi.org/10.1007/s40881-023-00134-6).

**Access:** relevant-excerpt. **Source type:** original preregistered meta-analysis. **Inspected locators:** §§2–2.3 Methods; §3 Results and sensitivity analysis; §3.1 Moderation models; §4 Discussion; Rights and permissions. **Supports local claims:** C-05, C-09, C-11

**Limits:** Mostly hypothetical, consumer-domain decisions. Choices changing is not proof of improved welfare or game agency. Numerical reporting cautions are recorded in the packet. **Independence:** Aggregates Frederick et al. (2009) and later experiments; those underlying studies were not independently re-inspected or counted again. **Rights:** CC BY 4.0 stated; original paraphrase with attribution; no figures reproduced

### GDR-SRC-20261010-F02-010

**Microsoft.** [Xbox Accessibility Guideline 115: Error messages and destructive actions](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/115). Microsoft Learn. **Publication/update:** 2026-03-04 last updated; original date unknown. **Edition/version:** Live unnumbered guideline page inspected 2026-10-10.

**Access:** relevant-excerpt. **Source type:** official vendor accessibility guidance. **Inspected locators:** Goal and Overview; Scoping questions; Implementation guidelines: stored data, permanent/destructive actions, alternatives to button holds. **Supports local claims:** C-07, C-08, C-10, C-12

**Limits:** Addresses erroneous inputs and destructive actions; not evidence that every intended strategic consequence must be rewindable. Security/purpose exceptions remain. **Independence:** Same issuer/suite as source 009. Same URL/update as inspected first-wave GDR-SRC-20261010-P01-18; central deduplication pending. **Rights:** Reuse terms not separately inspected; paraphrase only; no embedded media copied

## Open questions and change history

Researched: all seven assigned subtopics received a substantive first-pass treatment. **Coverage is not complete**: durable decisions across long sessions, cultural/linguistic variation, shared irreversible commitments, representative access testing and real-game opportunity-cost effects remain unresolved. The [review packet](../reviews/full-run-20261010-f02-review-packet.md#subtopic-coverage) records discriminating questions, source gaps and queued child work.

2026-10-10 — Initial F02 candidate, version 0.1.0, revision initial-capture-1; no predecessor artifact asserted. The selected first-wave package was hash-verified and relevant corrected passages inspected, but is neither canonical nor released. F02 author self-review is complete in the packet; independent F02 review, live-host retrieval tests and release are not complete. No playtests, repository edits or Project-source changes occurred.

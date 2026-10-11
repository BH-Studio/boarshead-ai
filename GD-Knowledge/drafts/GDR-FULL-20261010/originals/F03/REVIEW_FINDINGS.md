# F03 independent bounded review

Date: 2026-10-11. Disposition: retain as provisional research drafts with one local wording correction and open evidence/integration conditions. This is a review record, not approval, release, canonical ID allocation or gameplay validation.

## Result and correction

Read all four research candidates, the review packet and original integrity receipt from Library. All six reads were complete (`has_more=false`); reconstructed UTF-8 byte counts matched Library metadata. SHA-256 of all four research candidates and the packet matched the author receipt. `library_inventory.json` records Library/version/backing-file identity; `inventory.json` records locally recomputed hashes.

One verified internal inconsistency in PAT-02, “Illustrative rounding boundary”: “each single mark” implies per-unit rounding while the following worked result applies rounding to a submitted batch. Corrected to explicitly define `floor(1.5 × n)` chips for each submitted batch of `n` marks. This preserves the existing mathematics and its important limit: path dependence alone establishes no closed profitable route. No source or substantive claim rewritten. Corrected pattern is a delta selection; originals remain unchanged. See corrected/reviews/f03-local-revision-receipt.md.

No additional critical factual or arithmetic correction found in this bounded review. That is not certification of every source claim or exhaustive research coverage.

## Evidence and label checks

The 51 scoped claims are consistently separated into observations of documents, empirical reports, logical inferences, heuristics and hypotheses. Creator descriptions support existence/configuration rather than efficacy. The reward syntheses concern different outcomes, so the candidate correctly avoids resolving them as a universal pro-/anti-reward verdict. Recipe benefit, fatigue diagnosis and user comprehension remain hypotheses. The abstract-only Mekler lead supports no finding. Proposed comparisons, fabricated illustrative economies and executed document checks are explicitly distinguished; no invented participant results, actual economy simulations or hidden gameplay validation found.

Independent primary-source spot checks on 2026-10-11:

- [Cerasoli et al. author-hosted paper](https://selfdeterminationtheory.org/wp-content/uploads/2017/06/2014_Cerasoli_Intrinsic.pdf), Table 4, PDF page 17, and discussion: supports the quality/quantity predictive distinction. Financial-incentive estimates draw on earlier meta-analysis; this is not direct causal evidence for a game progression schedule. Candidate C-03 retains this limit and locator is correct.
- [Warframe 32.2.0 official notes](https://www.warframe.com/en/patch-notes/pc/32-2-0), Rotation Rewards / New Resource: Lua Thrax Plasm: supports guaranteed resource rotation earnings alongside drops and Yonta exchange. Crafting also consumes the resource. Candidate correctly avoids a whole-item, time or satisfaction guarantee.
- [Jagex 29 May 2025 announcement](https://secure.runescape.com/m=news/yama-cas--more?oldschool=1), Grand Exchange Tax / Improvements to Item Sinks: supports currency deletion versus tax-funded item purchase/destruction and distinct old/new offer rules. Developer balance rationale is not measured effectiveness; F03 preserves that distinction.
- [Hogan-Hennessy et al. v1](https://arxiv.org/html/2210.07970v1), §4.1: supports local threshold-specific trading-volume results, including a nonzero reduction at the high-price boundary. Thus its broader abstract wording cannot justify “tax has no cost.” Candidate retains this conflict and does not transfer a 2021 intervention estimate to 2025. Source date/NPC-bound issues remain unresolved, not silently repaired.
- The Deci author-hosted PDF was retrieved, but this review did not independently establish its scanned passage content. Its detailed locators remain an author-supported provenance route. The Frommel/Mandryk survey sampling and coding passages were not independently rechecked in this bounded pass. Neither limitation was converted into verified evidence. Dormans overlaps the F01 reviewed source and is not new independent corroboration.

## Arithmetic and practical recipes

Independent Python assertions executed only for synthetic arithmetic: `ceil((24-5)/3)=7`, balance 26 and leftover 2; spending all initial 5 changes the bound to 8; combined treasury/player stock is `1000+120-6=1114`; ore states `2→3→4`; per-batch rounding yields 3 versus per-unit 2. Assertions passed. No runtime model or participant test ran.

PAT-01's bound requires a fixed target price, settled available starting balance, a strictly positive minimum qualifying grant, no spending/loss, adequate storage, eligibility and available redemption. It counts qualifying completions, not failed attempts, elapsed time, acceptable effort or omitted crafting components. Earlier drops and settlement/duplicate handling are addressed. Direct selection and no-progression are meaningful countercases; the counter's salience is separated from reward distribution in proposed comparisons.

PAT-02 requires the entire enabling state, including consumed fuel, entitlements, reservations, permissions and capacity, before labeling a repeated source. Intended production can be desirable. Partial route enumeration is not global exploit clearance. The treasury example correctly treats buying/deleting an item as an item sink and a transfer of currency within the declared boundary. Aggregate stability is correctly insufficient for individual access. Practical conditions, failure cases and narrowing criteria are substantive, not just template headings.

## Required taxonomy coverage, claim mapping and disposition

T1 = progression topic; T2 = economy topic. Claim identifiers remain scoped to their artifact.

| Required subfacet | Claim support / application | Disposition and remaining gap |
|---|---|---|
| Unlocks | T1 C01,C05,C08; PAT01 C02–C03 | Bounded treatment; no staged versus immediate-access efficacy evidence |
| Mastery | T1 C01,C06,C12,C16; F01 corrected transfer pattern | Distinction supported; proposed assessments unvalidated, durable transfer unmeasured |
| Character growth | T1 C01,C06,C08 | Statistical/horizontal/expressive alternatives treated; no optimal XP/growth curve |
| Pacing | T1 C09,C11,C13 | Opportunity/stopping/horizon guidance is hypothesis; longitudinal cadence and re-entry missing |
| Intrinsic/extrinsic incentives | T1 C02–C04,C15 | Reported outcomes differentiated; game-specific causal transfer unresolved |
| Reward fatigue | T1 C07,C10,C11 | Competing explanations and countercases present; no causal or clinical fatigue conclusion |
| Sources/sinks | T2 C01–C03,C07–C08,C17 | Explicit boundary and worked accounting; live flows unmeasured |
| Scarcity | T2 C04,C13 | Actor/goal/state-relative treatment; acceptable burden and utility unmeasured |
| Currencies | T2 C01,C05,C06,C16,C19 | Units/availability/expiry/conversion handled; optimal currency count unsupported |
| Crafting | T2 C11,C12; PAT02 C03–C04 | Composition/full-state audit; corrected rounding domain, implementation untested |
| Trading | T2 C09,C12,C14,C19 | Settlement, alternatives, network/interference risks treated; informal bargaining/player distribution underdeveloped |
| Inflation | T2 C06–C10 | Stock/item/basket separated; manuscript issues, raw-data replication and general policy efficacy open |
| Incentive exploits | T1 C15; T2 C11,C15; PAT02 C03–C08 | Intent and productive countercases explicit; exhaustive routes, incidence and remediation impact unverified |

Additional short/long horizons, assistance, refusal, localization and operational boundaries are treated, but children, cross-cultural interpretation, live maintenance and longitudinal effects remain explicit gaps. Coverage means substantive bounded treatment, not exhaustive sufficiency or gate passage.

## Cross-batch reconciliation

- F01: F03 already uses corrected contrasting transfer probes and retains ordinary information/access supports. Acquisition, progression level or assisted success is not proof of mastery. No contradiction found with experience-goal, core-loop or onboarding distinctions.
- F02: Its bytes and independent review are now available in `/workspace/shared/f02_review`; F03's “F02 unavailable” statements describe its authoring snapshot and must not silently be rewritten as research claims. Review-side reconciliation now establishes conceptual compatibility: resource grants change available options and opportunity costs; challenge evidence must distinguish power/access/knowledge; needed assistance is not an earned entitlement. F02's corrected performance locator is a source-location fix, not new efficacy evidence. This reconciliation does not imply all F02 link/index edges are integrated.
- F07: Treat stock balance, retention, completion and rewarded output as proxies, not the full desired experience. Preserve triangulation, informed refusal, stopping and return, and separate welfare judgments from accounting. Guarantees do not automatically make an acquisition route humane. F03 is consistent with these conditions.
- Source identity: Dormans F03-007 duplicates F01-08; Hades F03-010 duplicates F02-012. Reconcile canonical source identities later without counting them as independent support. No permanent registry allocation or cross-batch canonical relinking performed here.

## Open conditions

Source-conflict resolution and unspotchecked passages; representative/longitudinal evidence; actual transaction semantics and route completeness; current pending/canonical registry reconciliation; complete cross-batch dependency links; preserved relative hierarchy in assembled archive; host retrieval and cold/blind tests. Starter gates, evidence rules and required taxonomy were used as review criteria. Neither this review nor static arithmetic clears Gate D/E, authorizes game adoption or creates release approval.

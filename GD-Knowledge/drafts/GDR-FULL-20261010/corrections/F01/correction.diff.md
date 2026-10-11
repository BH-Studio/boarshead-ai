# Preserved provenance record: correction.diff

Original record SHA-256: `47d421cae56bf566bc04cb800dd2c5a84b25d85173355475839f02f1d8f976b7`. The fenced payload preserves the complete original text; the wrapper is Markdown-only packaging.

```text
--- original/patterns/supported-attempt-and-transfer-check.md
+++ corrected/patterns/supported-attempt-and-transfer-check.md
@@ -4,6 +4,9 @@
 title: Supported attempt and transfer check
 version: 0.1.0
 status: draft
+candidate_revision: independent-review-correction-1
+predecessor_sha256: 8c1040477ea4479b4a6272abae42e7007381480fcdabbd9b21040452ab76aac8
+change_summary: Correct illustrative transfer probes and document discrimination limits; no tests performed.
 id_scope: run-scoped-temporary
 run_id: GDR-FULL-20261010
 batch_id: F01
@@ -98,7 +101,17 @@
 
 First, make the reservation rule available and explain what is committed. Invite a reversible decision to spend 3 units or change the reservation. Feedback should distinguish the owned total from the spendable amount and explain why the attempted spend did or did not satisfy the rule. Presentation determines the accessible form; this pattern does not prescribe colors, layout or sound. [C-05; C-07]
 
-For the changed case, use 10 owned units with 7 reserved and a proposed spend of 4. Simply choosing the visually larger total is now an inadequate strategy. A relevant response can be to release enough reserved resources, choose a different purchase or decline the spend. The check is about the relation, not a compulsory preferred purchase. A player who makes an unexpected choice for another valid goal has not necessarily misunderstood. [C-06]
+For proposed changed cases, vary both affordability and the amount reserved rather than repeating the same unavailable purchase. Before giving corrective feedback, ask the player to predict the immediately spendable amount and whether each proposed spend is permitted **without changing the reservation**. Offer an equivalent nonverbal response route when explanation would introduce an unrelated language or access demand. These invented probes are candidate assessment items, not validated tests or balance recommendations. [C-06]
+
+| Illustrative probe | Owned / reserved / proposed spend | Rule-based prediction | Competing response this can help distinguish |
+|---|---|---|---|
+| Unaffordable contrast | 10 / 7 / 4 | 3 spendable; spend is not permitted without changing the reservation | Treating the full owned total as available predicts permission |
+| Affordable contrast | 10 / 2 / 4 | 8 spendable; spend is permitted without changing the reservation | Repeating “always reject” or “always release one reserved unit first” from the initial example is unnecessary |
+| Exact-availability boundary | 10 / 6 / 4 | 4 spendable; spend is permitted under this example's explicit rule that spending the available amount exactly is allowed | An incorrect strict-less-than rule predicts refusal; this boundary convention must match the actual game rule |
+
+The first two probes hold the owned total and proposed spend constant while varying the reservation and the correct affordability answer. They can expose some copied-answer and total-owned strategies, but neither one correct answer nor the whole set proves that the player learned the relation: guessing, memorized cases, arithmetic familiarity, interface cues or earlier feedback may explain success. A future comparison should vary values and order, record assistance, and assess the intended relation without quietly adding extra demands. These probes are proposed only; no player has completed them in F01. [C-06; C-10]
+
+Keep the prediction of what is permitted separate from the player's preferred action. A player may correctly recognize an affordable spend and still decline it for another goal. In an unaffordable case, they may choose to release sufficient reserved resources, select a different purchase or decline. Such preferences alone are not evidence of misunderstanding. Do not taper prompts solely because a purchase was accepted or declined. [C-06; C-07]
 
 If the relation is used intelligibly, offer to continue without answer-leading prompts while retaining the resource information and help. If confusion persists, test whether “reserved” is understood and whether both quantities are accessible before repeating the lesson. If an assistive route is required, retain it irrespective of check performance. No player results exist for this example. [C-05; C-07; C-09]
 
@@ -250,3 +263,6 @@
 Open questions: diagnostic validity; whether the changed case measures the intended capability; whether prompt tapering improves participation; and whether a recap or ordinary state information better supports return. The entire recipe remains a low-confidence hypothesis. Source links establish rationale and limits, not an accepted technique.
 
 **2026-10-10 — 0.1.0 draft:** initial F01 candidate using the available starter topic/pattern templates and the current bounded authorization. Author self-review is documented in the [batch review packet](../reviews/full-run-20261010-f01-review-packet.md). Independent review has not occurred. No prior version is superseded, no canonical authority is claimed, and no release or game adoption is approved. Permanent identity, cross-batch source matching and dependency resolution await Library Coordination.
+
+
+**2026-10-10 — independent-review-correction-1, still 0.1.0 draft:** a separate model review identified that the original changed case had the same affordability answer and one-unit shortfall as the supported case. This local correction adds contrasting affordability and boundary probes, separates rule prediction from purchase preference, and states remaining alternative explanations. The initial history above describes its original snapshot. Review findings and cross-batch coverage/dependency reconciliation are recorded in `../reviews/f01-f07-independent-review-reconciliation.md`; that separate review is not empirical replication or human acceptance. No playtest was run, no evidence-confidence upgrade or approval was made, and the original capture is preserved under its predecessor hash.

```

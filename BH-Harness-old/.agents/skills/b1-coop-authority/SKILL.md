---
name: b1-coop-authority
description: "Review or implement approved exactly-two-player Breach One authority, transactions, recovery and participant state. Not authorization to choose a network backend or add future session features."
---

# b1-coop-authority

Package: B1-CODEX-OPS | Version: 0.1.0
Authority: use only within the adopted repository instructions and the current authorized task.

## Entry

Read the approved session contract, actual network/backend version if selected, relevant system
contracts and test plan. In early solo work, inspect only the required future-feasibility boundary;
do not add networking because the intended product is co-op. FishNet, Mirror, NGO and PUN
availability do not select a backend. Four-player, split-screen, late join and host migration are
out of scope unless explicitly approved.

## Ownership and transactions

For each operation, identify requesting participant, authoritative validator/mutator, replicated
result and presentation. Distinguish command intent, canonical state and local prediction/feedback.
Map damage, resource spend/reward, objective completion, power activation, revive and interactions
only where in scope. Define duplicate, repeated, reordered, canceled and stale requests plus
atomic resource checks. State transitions must not resolve twice because two peers observed them.
Do not claim exactly-once semantics without an explicit mechanism and failure tests.

## Failure and equality

Specify disconnect/reconnect, timeout, simultaneous interactions, scene transition and retry
behavior from approved contracts. A transport disconnect does not itself decide story progress
or save ownership. Technical host authority is not permission to make another human's narrative
choice. Confirm equal human access to the authorized core verbs and shared critical information.
If a bot is in scope, define its control owner and permitted actions; no invented bot veto,
mandatory companion, hidden spending or takeover policy.

## Validation

Use the actual required separate-process roles and versions. Exercise nominal and approved
adverse latency/loss/disconnect cases, simultaneous actions and repeat/retry paths. Compare final
canonical state at both ends and confirm no duplicate gameplay outcome or persistent divergence.
A single-process mock is useful focused evidence, not complete online validation.

## Output

Return authority/transaction table, failure contract, actual process/topology/workload details,
state/evidence comparisons, remaining manual checks and unresolved decisions. If the backend or
policy is unapproved, produce a bounded review finding rather than inventing its implementation.

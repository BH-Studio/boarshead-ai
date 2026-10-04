# Authority, provenance, and change control

Package: B1-CODEX-OPS | Version: 0.1.0 | Prepared: 2026-09-08
Status: CANDIDATE workflow; effective only after human adoption.

## Approval is evidence, not typography

An implementation manifest must identify the human decision, date, exact artifact/version or
revision/hash, permitted scope, and exclusions. Accept a clear direct instruction in the current
session or an existing traceable human-approved record; do not demand a cryptographic signing
system. A copied `APPROVED` header with no provenance is insufficient. A hash proves identity,
not approval or trustworthiness. An assistant may transcribe a human decision, never manufacture it.

Once system and milestone authorization are clear, proceed without asking for duplicate approval.
Changing the approved artifact afterward invalidates its approval for the changed scope unless
covered by a recorded delegation or change decision. Do not silently relabel the new revision.

## Authority conflicts

Follow the project hierarchy in root `AGENTS.md`, subordinate to platform instructions. Within
equal-authority records, examine explicit supersession and decision dates; "newest file" alone
is not enough. Flag a current-state snapshot that conflicts with a later human decision. Do not
restore rejected behavior because code still does it. Do not import recommendations as requirements.
A narrative-local approval can constrain narrative without approving a runtime/network implementation.

If a required source is missing, say exactly which claim cannot be verified. Continue unaffected
work inside its authority. Do not block a read-only tooling audit on an unresolved camera choice.
Do block a camera implementation that would have to choose that policy without authorization.

## Shared record ownership

M integrates `PROJECT_CONTEXT`, `CURRENT_STATE`, decision registers and shared designs. Codex may
write milestone work/completion evidence at package-approved paths. By default, it emits a
`STATE_DELTA` proposal rather than rewriting shared canon. Explicit delegated editing must name
files, permissible fields, approval source and limits; it does not let Codex approve product choices.
Historical accepted ADRs and completion records are superseded or corrected transparently, not erased.

## Change record

Use `templates/CHANGE_REQUEST.template.md` for prior/new decision, reason, requested-by, evidence,
player effects, owners/dependencies, save/schema/migration impact, scale/budget changes, milestones,
invalidated tests, documentation, rework, rollback and human disposition. New risks are not
"acceptable" until the appropriate human accepts them. Tunable values stay within approved ranges;
changing a range or the meaning of a parameter is a design change, not ordinary tuning.

## Delegations and exceptions

Low-level naming, private helpers, and implementation order can be delegated inside locked
contracts. A prototype exception must state the question, disposable scope, paths, allowed
execution, bypassed gates, risk, success/falsification criteria and cleanup or revisit point.
"Try a drone" does not authorize a universal camera framework or a production drone economy.

## Handoff identity

Every substantial artifact identifies ID, version, status, owner, input baseline, supersedes,
preparation date and evidence cutoff where applicable. Portable citations use source titles,
filenames/versions or URLs, dates and section/line locators. See `SOURCES.md`.

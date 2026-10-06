# Cost and host guidance — checked 2026-10-04

## What this candidate changes
Keep research, alternatives, detailed system design and design review in the user's existing normal ChatGPT Project/custom-GPT workflow. Transfer only the approved slice, current state and relevant contracts into Codex. Do not automatically switch that design work into ChatGPT Work. This is an operating choice to control agentic consumption, not a claim that conversation consumes no tokens or has no limits.

Five explicitly invoked skills replace a large always-active catalog. AGENTS.md stays short. The human-readable checkpoint is generated from bounded structured state; raw logs and source catalogs are not reread every turn. One approved plan covers ordinary edits. Evidence is reused only while its declared dependencies remain current. Repeated failure/recovery is bounded, not an indefinite autonomous retry loop. Deterministic local verification performs no model/API calls. No vector store, service, paid account, model gateway, crew or scheduled model task is added.

No numerical token savings, allowance headroom or throughput improvement has been measured. Python/Git/Unity execution still costs local time/IO; current full-input snapshots may be expensive in asset-heavy projects. Local context limits are not the same as PC RAM or subscription allowance. Use host usage telemetry when available, never estimate remaining quota from the number of files or replies.

## Current official facts to recheck at adoption
OpenAI's Pro tiers article says eligible existing Pro 200 subscriptions retain their previous included allowance through October 29, 2026, then move to a lower allowance while price remains $200. Eligibility depends on the stated September 22–29 window; the harness cannot verify Doug's account status. The same article says context, reasoning, model, tools, retrieval, caching and speed affect usage. Faster modes can consume allowance faster; no model/effort/speed is hard-coded here.

OpenAI's Codex plan article says Codex and ChatGPT Work, plus other eligible agentic features, can draw from a shared allowance. Check the actual account usage page or Codex `/status` rather than assume a fresh chat resets it. Regular Chat usage is distinguished from Work/Codex in that documentation. An observed service limit leads to checkpoint and stop, not API-credit purchase, evasion, unbounded sleeps or a promise of background continuation.

Current GPT documentation says personal accounts cannot create/publish new GPTs; existing GPTs remain usable/editable subject to plan and permissions. Pilot this candidate in a separate ordinary Project or already-existing approved test GPT. Preserve the live GPT until a human-approved, tested change. Do not buy Business or build an unrequested plugin migration merely because host policy changed.

## Sources (official, accessed 2026-10-04)
- https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers — Pro 200 transition, usage variables and speed caveats.
- https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan — shared Work/Codex allowance, usage inspection and current client guidance.
- https://help.openai.com/en/articles/8554397-creating-and-editing-gpts — existing versus new GPT eligibility, Instructions/Knowledge and migration notices.
- https://learn.chatgpt.com/docs/build-skills — native skill layout, explicit invocation and metadata policy.
- https://learn.chatgpt.com/docs/agent-configuration/agents-md — native instruction discovery and precedence.

These facts belong in dated operational guidance, not immutable universal policy. Recheck account/client notices before a pilot or adoption.

# bh-civil-ai-jobs v0.1.0

A **Phase 1 read-only specialist skill** for BH Unity Harness. It includes documented CIVIL-AI integration guidance, job planning patterns, prefab identity rules, acceptance tests, sample JSON job definitions, and a nonmutating validator. It does **not** include a verified Unity asset generator or a working CIVIL-AI adapter.

## Installation
1. Extract this folder to the harness's **existing skill discovery location** (inspect the harness documentation first; do not assume a fixed directory). Keep `SKILL.md` at the root of the skill folder.
2. Ensure the harness recognizes the skill without changing its approval or execution contracts.
3. Invoke: `Use bh-civil-ai-jobs for a read-only discovery and integration plan in Ronin. Inspect installed CIVIL-AI and existing economy code. Do not mutate project files or run Unity commands. Produce the required discovery outputs.`
4. Review and approve a change manifest before any later generation implementation.

## Local validation
`python scripts/validate_job.py examples/well-water.job.json`
`python scripts/validate_job.py examples/fishing.job.json`

## Known limitations
- Package APIs and editor bindings have not been inspected in the user's Unity project.
- Sample JSON is a proposed contract only; no importer.
- Stable-ID reconciler and stock/recipe/logistics services are specifications, not implemented code.
- Do not install into a live Unity project or run mutations solely on the authority of this package.

# Retrieval and distribution contract

## Canonical library and working copies

After publication, GitHub is authoritative for released library files, IDs and review status. A Project's uploaded files are curated snapshots of a named release and commit. Changes in one Project do not update another Project or GitHub automatically. A conversation remembering a change is not proof that an attachment changed.

The current official [Projects help page](https://help.openai.com/en/articles/10169521-projects-in-chatgpt), checked 10 October 2026, lists 40 files per Project for Pro. Recheck before provisioning because limits can change. Plan below the limit and leave room for current research. Do not upload the whole growing library to every Project.

## Pack design

Each Project initially needs shared research instructions, evidence rules, taxonomy, index, review gates, registers, the appropriate templates and its domain instructions. Coordination additionally uses this distribution contract and compatibility review. These starter sets are comfortably below 40 files.

As reviewed content grows, distribute coherent domain packs as Markdown. A pack contains a title, release version, canonical commit, creation date, source paths and versions, entry IDs, status labels, included source records and exact entry boundaries. Preserve each entry's ID and headings. Condense duplicate administrative matter, never silently omit limitations, counterexamples or evidence. Packs are export views; edits return to canonical individual files through review.

Keep each pack narrow enough to inspect and retrieve reliably. Fewer files do not guarantee better retrieval, and concatenating everything into one enormous file is not a quality solution. Maintain enough capacity for active source material and review candidates. Do not rely on ZIP contents being indexed as Project knowledge; extract and upload the intended Markdown files.

## Refresh procedure

1. Select a reviewed canonical release and record its commit, included IDs and file hashes in a Markdown distribution receipt.
2. Prepare the domain's packs and check links, completeness, source records and statuses.
3. Replace or remove superseded Project snapshots deliberately; avoid two contradictory versions with similar filenames.
4. Open the uploaded files or run retrieval checks to establish the expected version is accessible. Record actual verification; do not infer success from a filename alone.
5. Log Project name, release, upload date, included files, verification outcome and unresolved omissions in the receipt.

Use a single snapshot version in a task unless an explicit comparison requires multiple versions. When live GitHub retrieval is available, fetch exact relevant files and report the commit rather than assuming the Project attachment is current.

## Selective retrieval

Input: design question; intended experience; game/project constraints; genre or hybrid facets; audience/access needs; platform/input; budget and technical boundaries; known approved decisions.

Procedure: inspect the index → retrieve the closest topic → retrieve relevant genre guidance → select only applicable patterns → inspect linked sources and contradictions → test fit against the project's approved constraints. Expand only when a specific dependency requires it. Missing evidence is a visible gap, not permission to improvise a library answer.

Output: question addressed; retrieved IDs and versions; source commit/snapshot; recommendation; rationale and claim class; applicability conditions; alternatives; known contradictions; confidence/limits; proposed validation; decision needed. Cite the relevant files and source locators.

Example request: “How could ambient audio build tension in a low-combat exploration game with optional captions?” The correct starter response is that research is pending and the pilot specifies questions to investigate. It must not pretend the layered-audio hypothesis is released knowledge.

## Harness and director handoff

The knowledge handoff is advisory. It supplies evidence and options to the existing design workflow; it does not replace its approval, canon, contract, milestone or validation gates. A research recommendation is not permission to change runtime behavior, architecture, balance or approved narrative.

Proposed handoff fields, written in Markdown: request/decision; approved project context; retrieved IDs/versions/commit; relevant claims and sources; selected technique and alternatives; genre adaptations; constraints; risks/contradictions; validation plan; approval state; unresolved questions. The receiving director should revalidate applicability before turning it into a project decision.

No harness adapter or code is implemented in this starter. A future integration requires review of the current actual interface and a separately approved change. Keep general library evidence separate from project-specific source of truth.

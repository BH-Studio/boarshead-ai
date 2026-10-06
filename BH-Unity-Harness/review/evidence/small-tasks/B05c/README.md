# B05c actual manifest/schema/policy reconciliation

Input: BH-Studio/boarshead-ai, branch harness/bh-standard-v1-20261004, head b5a38afac94841973090d686d658fe3966dfefab.

Exactly eight assigned inputs were retrieved and reconciled: PACKAGE_FILES.json, PRESERVED_REFERENCES.json, contracts/schema.json, design-gpt/KNOWLEDGE_MANIFEST.json, official instructions, name/description/starters, regression cases and instruction metrics. All eight matched pinned Git blob SHA/byte length and B05b batch metadata. SOURCES.json records SHA-256; FETCH_METADATA.json projects actual retrieval metadata. RAW.log is captured reconciliation stdout/stderr, and COMMANDS.json records its actual command and exit 0.

Five JSON documents parsed. The actual official Instructions contain 7,798 characters, 202 characters of headroom, matching the metric digest and UTF-8/LF/final-newline convention. Schema identity is urn:bh:contracts:1.0.0 with 25 definitions and resolved local references; runtime schema validation was not invoked. MANIFEST_FINDINGS.json records these narrow checks and the policy review. Human approval, design/implementation separation, current evidence review, game neutrality and cost boundaries remain explicit; authored host regression scenarios remain NOT_RUN.

The manifests declare 25 installed files, 15 selected knowledge files and 13 preserved references. Their knowledge/preserved union contains 17 distinct paths. Declared preserved/knowledge Git blobs agree with current tree metadata, and the installed path roster matches the tree. Downstream bytes and manifest SHA-256 checks were not performed in B05c. Historical K11 remains reference-only and is not a knowledge selection.

DEPENDENCIES.json records exact manifest identities and bounded child batches: B05d's three lesson/reference files; B05e1/e2's fourteen remaining selected/preserved files; B05f1-f4's remaining active resources; B05g1-g6's remaining Python syntax inputs at this head. These are metadata plans, all NOT_STARTED. Prior byte records must be revalidated at execution head. The package checker currently sees 58 tracked Python files including evidence; later commits add helpers and require a current-head roster update before execution/final proof. Required report artifacts are presence-only inputs, not historical verification proof.

No B05d or other downstream resource contents were fetched. Tests, package checker, assembler and test runner were NOT_RUN. No implementation/defaults/host changes occurred. Full candidate validation and human adoption remain open; PR #1 must remain draft and unmerged.

The executed b05c_reconcile.py expects the original b05c-input.json GitHub export and B05b batch metadata. It writes b05c-work/ and performs only the recorded eight-source checks and intra-batch parsing/metrics. It does not import or execute package/test code. Reproduce from exact pinned files/tree metadata and the recorded command.

# B01 — installed-file identities

Result: PASS, 25/25 declared installed files matched. Missing, mismatched, duplicate and extra installed paths: none. This is an identity check, not runtime or full-candidate verification.

Input branch: `harness/bh-standard-v1-20261004`.
Input head: `115718aaba62f505b20771b1455cba64540c0de5`.
Manifest blob: `c3408ece30947c8f520c82522fa08da0f3376282`.
Installed tree: `e35bbdcc31970eb82b273e587b6ca6373764aee1`.

The GitHub connector read the checkpoint first, then the incorporation status, current manifest and PR metadata. PR #1 was open, draft and unmerged. After obtaining the head SHA, checkpoint/manifest and installed sources were pinned to that commit. A preliminary `template/AGENTS.md` probe returned 404; the actual pinned directory listing identified `project-template`. No installed file was missing.

Retrieval: `fetch_file` with ref=115718aaba62f505b20771b1455cba64540c0de5 and encoding=base64 for PACKAGE_FILES.json; Git Trees GET for the installed tree with recursive=1 (truncated=false); `fetch_blob` for each of its 25 declared blob SHAs. Each returned UTF-8 string was encoded to bytes without newline normalization. Recomputed Git blob SHA-1 and byte length must match the pinned tree before SHA-256 equality is accepted. No old local archive supplied any bytes. RESULT.json records every exact path and expected/observed identity.

Actual command, from the scratch work directory:

```sh
python3 b01_validate.py b01-input.json b01-evidence > b01-evidence-raw.log 2>&1
```

Actual exit status: 0. RAW.log is that exact captured combined output. validate.py is the exact executed script (local filename b01_validate.py); RESULT.json is its generated machine report. The transient b01-input.json was an input envelope of connector responses, not a harness checkout, and is not duplicated here. To reconstruct that envelope, use the pinned sources above: repository, branch, head; git_commit from Git Commits GET; template_tree from Git Trees GET; manifest={content: base64 response, sha: manifest blob, reported_size: 4520}; checkpoint={content: pinned UTF-8 checkpoint, sha: pinned checkpoint blob}; files=[{path: manifest path, content: fetched blob UTF-8 content}]; pr=RESULT.json.pr_before; retrieval_note=RESULT.json.retrieval_note. Then run the recorded command with the saved script. All source bytes remain available at the immutable input commit.

Publication is limited to this evidence directory and BUILD_CHECKPOINT.md. The branch head and checkpoint SHA were rechecked before authoring the commit. Ref publication uses force=false and the existing head as parent; no force-push is authorized. Resulting commit, exact changed paths, checkpoint readback and PR state must be verified after publication.

Runtime tests: NOT_RUN. B02: NOT_STARTED. Candidate adoption: PENDING. No runtime/package/design files were changed.

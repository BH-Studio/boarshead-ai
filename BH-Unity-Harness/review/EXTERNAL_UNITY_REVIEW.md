# Unity external-source review — 2026-10-04

Status: bounded source review completed for the files below; optional host integration NOT_RUN. This is not an audit of every skill or vendor runtime. No external skill, plugin, source code, artwork or trademark asset was copied into the distribution, installed or activated.

## Pinned sources and stored-copy comparison

| Upstream | Current default-branch commit | Complete files read |
|---|---|---|
| https://github.com/Unity-Technologies/skills | main @ cb1dccb8f5adffcca43a5a26993fdeb8eae59433 | README.md (9414a672b0bd07df4247924e3277a10969321533); LICENSE.md (869c724c8cab8764b548fd5bd8cb8ea1fc849100); skills/unity-cli/references/playmode-verification-loop.md (9394dad02cf252ec81e5fa981d2e5c6fe15491e0) |
| https://github.com/Unity-Technologies/unity-agent-plugin | main @ de668bfd2e4ece0613c331e653c8c48b03e7238d | README.md (fb815fe85c2bfbbcdf3d714c08930ed114f9fec1); LICENSE.md (b0f206c89bec2f974cc874794d1d3f5bca1fd79b) |

Additionally inspected the skills/unity-cli/SKILL.md opening through the environment-variable section, but the connector response was truncated. It is PARTIAL, not a complete read. No instruction from that file is adopted wholesale. Root trees and the skills catalog directory were inspected as metadata, not as proof of full-file review.

Stored inputs are at BH-Studio/boarshead-ai source baseline 0cffc7e090eccb2d0b453c2c2c5a0db4631650c8:
- Reference/Unity/skills-main, tree f4cf5bc9f7f41598f82237bd890159745727b481. Its README, LICENSE, contributing, scripts and workflow tree identities match current upstream. Its skills subtree 2780ec7d245e9442d3dcd2fb49900fe9214a8a0b differs from current a6734b703bcf377dde8baefc12d148273fe0f4ec.
- Reference/Unity/unity-agent-plugin-main, tree e4f8d1f03a9da07c4112147bfd1c607a5534deed. Root README/LICENSE and agent/plugin metadata tree identities match current upstream; stored skills subtree 7150095e93886f625ee90398ec70a50761dc3eca differs from current 846a3c3ddc82190fa7fbd4073b26f838d59c271c.

Therefore the stored collection is not asserted to be byte-identical to either current catalog. The selected current play-mode file, not an assumed snapshot version, supports the verification ideas below. Neither entire catalog is a dependency of BH Unity Harness.

## Disposition and justified guidance

EXT-UNITY-01 — Retain optional live Editor inspection as a project-configured route. Discover actual connected project, package version and commands, and bind the target explicitly. A missing connection can mean compilation/Safe Mode, domain reload or sandbox visibility, not proof the user's Editor is closed. Keep the existing batch alternative and do not start or kill competing Editors. Destination: local integration checklist and existing one-writer policy; no new automatic adapter.

EXT-UNITY-02 — For a play-mode smoke claim, record that frames or the relevant state actually advanced before interpreting a capture. A screenshot or Play-mode entry alone is insufficient. Use a bounded, discovered condition check and narrowly captured output rather than repetitive polling or inline bulk data. Advancing frames proves only that narrow observation, not acceptance of the gameplay. Destination: optional pilot protocol; local execution must establish tool names and outputs before any binding becomes eligible.

EXT-UNITY-03 — Separate preparation, audit and correction. Auto-tick/run-in-background settings, eval-based tuning, scene changes and play/stop are stateful operations. Record initial settings, explicit authorized changes and restoration; tuning belongs in approved execution, not a read-only audit. Any changed input invalidates affected evidence. Never label the vendor's entire edit/tune loop an independent verification boundary.

EXT-UNITY-04 — Do not adopt the upstream instruction to always install/update to latest, automatic remote installer execution, global skill symlinks, --trust flags or automatic whole-catalog activation. They conflict with this task's pinned, reviewed dependencies, scoped permissions and minimal-context installation. Native plugin distribution is an optional future packaging choice, not justification to replace the five BH skills or require account changes.

## License and notices

Both repositories identify Unity Companion License, not MIT/Apache. The old unity3d.com link was inaccessible in this review; current official terms were retrieved at https://unity.com/legal/licenses/unity-companion-license, v1.4 dated 2024-10-29. They condition use on a valid Unity engine license, restrict competitive uses, address ownership of derivatives, require relevant notices and reserve trademarks. Preserve those conditions if any substantial material is later copied. This review does not determine that a standalone repackaging qualifies, does not change the original collection's license and does not grant use of Unity marks. Conservative current disposition: link to the inspected sources; no redistribution of their content. Review any package-specific third-party notices before a future selected installation.

## Fresh OpenAI cost/host recheck

The existing COST_AND_HOST_GUIDANCE.md remains consistent with official https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers retrieved 2026-10-04: the stated eligible September 22–29 grandfathering window retains the prior allowance through October 29, 2026; the harness cannot determine account eligibility. Context, reasoning, tools and speed affect usage. This is not a quota reading or a savings benchmark. No paid tier/API requirement is introduced.

Native skill and instruction source URLs were rechecked: https://learn.chatgpt.com/docs/build-skills and https://learn.chatgpt.com/docs/agent-configuration/agents-md. Current eligibility and native activation must still be tested on the user's actual clients; documentation inspection is not that test.

## Durable continuation

Implementation/source-retention tests now total 133 passing cases in six nonoverlapping partitions; see evidence/source-retention-20261004.json committed at 7995098a33f9ca4419a7f0ef142214436004cf75. Continue bounded current-source/license reviews for CodeAF, Superpowers, MattPocock and both alternative Unity MCP repositories, then central inventory/manifest/PR reconciliation. Keep catalog copying and live integrations disabled. Do not restart the completed 60-file legacy review.

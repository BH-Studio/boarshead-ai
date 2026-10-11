# Cumulative snapshot verification

11 October 2026 UTC. These are local static/byte checks, not actual-host or gameplay tests.

- Exactly 38 selected research entries: 19 topics, 5 genres, 14 patterns across nine batches; nine author review packets.
- Every selected entry has a unique provisional ID, version 0.1.0, draft status and null reviewer/approval fields. Existing IDs and semantic versions are preserved.
- All first-wave selected files match the prior delivered tree byte-for-byte; its ZIP still hashes to `e959c8d4eda2ba2a5f1994a37e0fa613d11f3fe0c5dd0608cf12a8fad87883ef`.
- 24 wave-2 original captures match their recorded original hashes. The P02 inventory's `original_sha256` explicitly identifies originals; its `sha256` describes corrections. These are not interchangeable.
- Six P02 corrected files, all three F02 corrected candidates/packet and the W02 corrected pattern match their correction inventories/receipts.
- F01/W02 original packet fingerprints and F02 original integrity receipt intentionally describe predecessor bytes. SELECTION_RECEIPT and ENTRY_INVENTORY explicitly own current selections. No stale fingerprint is silently declared current.
- 663 selected relative Markdown link/anchor occurrences resolve locally using heading slugs and explicit anchors. Root entry/source/receipt navigation also resolves. Historical snapshots retain historical layout and do not claim current routing.
- 141 declared provisional source IDs; this is not a count of unique works, full-text inspections or independent studies. Source duplication and overlapping patterns remain unresolved.
- UTF-8 and Markdown-only payload checks completed. Archive CRC, member count and extracted-byte equality are verified when sealing the ZIP; the external ZIP hash is supplied at handoff.
- No external URLs re-fetched during packaging. No browser/Project-host rendering, retrieval, participant/player study, human acceptance, canonical consolidation or release is claimed.

## Wave-2 original hash checks

| Capture group | File | Original SHA-256 |
|---|---|---|
| f02_review | `full-run-20261010-f02-review-packet.md` | `fe57fad9b32f6d0dab93d819f29d233ea3bc3148a41f477111ada76efa438923` |
| f02_review | `full-run-20261010-f02-integrity-receipt.md` | `4e8fc0d3debfeaf43e2021c23b82a955138eb5ed8d3e7b7c9ab216f98be2c604` |
| f02_review | `decision-design.md` | `2fe66a5bf914a9c3f4101e168cdfd344a26eeadbfea7c45d16a9f17cca33bc6c` |
| f02_review | `challenge-and-difficulty.md` | `c4cdce1b33661195b9c732b46209729f5db99418a369f1a5af18c429308654e4` |
| f02_review | `visible-opportunity-cost-comparison.md` | `afb19a4a363fbef3d7478731f84520c500dad15858d42a8b38bc0446ae63648b` |
| f02_review | `bounded-disclosed-difficulty-adaptation.md` | `d442c6f6bac8c46f363cbf7ec91bdcd58e7ea840213a0f6c5f21015817a8dd6b` |
| wg02_review | `full-run-20261010-w02-review-packet.md` | `992e33e0b4cb63d57161051a628d2457c3440721c34a0d1bc44c538566b9254e` |
| wg02_review | `multi-route-objective-contract.md` | `557950671f434878c95dd5b414bc1582d83d04dad85224072f5da66fff15241a` |
| wg02_review | `intent-and-response-contract.md` | `ce138cb90f55a5c6b7f7da5220a328f21ab3198902e5199eebf2ccdbfbf221bc` |
| wg02_review | `lore-delivery-and-continuity.md` | `5fb7c9f20c82312f1e6d17913534fae58cc587899d32e3937a0eef80787e3674` |
| wg02_review | `quests-and-objectives.md` | `55986dec9fc009efeaeaf970d3d304e3516c7196be47f0f150b31fd4fbb40252` |
| wg02_review | `dialogue-and-voice.md` | `8ecccddc1b02b4e6cf7aa0f3346a1b9a310010fdb3f625d9c4fab120e3b2397e` |
| wg02_review | `full-run-20261010-g02-review-packet.md` | `1c12ca5dc979d155cd70a13e422a7264ebbdf943e1a45aac4189a228dead9771` |
| wg02_review | `recoverable-ability-gate-loop.md` | `a28697f5a686d6457bf6ac4ca137dff813228c1f11a1945fa46c52f3ee2e924b` |
| wg02_review | `bounded-action-grace.md` | `03e0819fc92f1e6fcfe87d84871d2cbb6de337d3bcd57e044e614cb3d2773f1c` |
| wg02_review | `metroidvania.md` | `18a56b38a19b7cfc10d7d756a90a8d77bd632107db5ca1a5a8e08e2c1b1c0a30` |
| wg02_review | `precision-platformer.md` | `dc8b6475db0a82fc5563e168a1771489223a9409f1df2d7b98dccc55e5500601` |
| wg02_review | `platformer.md` | `997e5b1bd3cb955650bb8a2b6c932e3e753e23d63860f009fe75f79505fc3298` |
| p02_review | `full-run-20261010-p02-review-packet.md` | `81f348b4a879ee7a0e7a86d25a8af3fe5ad56b0d77873c09855bc090525e1466` |
| p02_review | `fact-preserving-cue-alternatives.md` | `8e54f5e5d986a8ff40126167cce1bfca06b0d42f1aba302121030097da4aaa40` |
| p02_review | `recoverable-action-remapping.md` | `6678d20eff426347737a716ecf7b8496b85c47f51fcb7bdc75c8ce6b9f68c5d2` |
| p02_review | `multimodal-communication.md` | `0125bc5f3520762eeb9366b03c9f6d7e3178da98fb1e12257332407d278cc1c2` |
| p02_review | `feedback-and-game-feel.md` | `a06f9bd0b9c46fd065b6f8f61e2ad370467eb690e9ffe470cd469e480e1eaeaa` |
| p02_review | `controls-and-input.md` | `c85996f89fb285a2114b7d937602bcb400f33f9c58cc8109afa4412561015c08` |

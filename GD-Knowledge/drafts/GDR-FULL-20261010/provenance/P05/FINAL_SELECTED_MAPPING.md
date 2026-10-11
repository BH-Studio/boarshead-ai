# Current P05 integration mapping

Overrides only the historical mapping’s unresolved source-selection field, not original/selected bytes or IDs. Research files and packet have different original-array positions. Both origins remain byte-identical, but only the final-response attachment identity below is selected.

```json
[
  {
    "path": "selected-drafts/topics/audio-design.md",
    "id": "GDR-CAND-20261010-P05-TOP-01",
    "selected_original_library_id": "libfile_7ec53d5b5c0481918b63e281142480e8",
    "original_sha256": "5671ba5fe03df995f07213f514ecf02156140a5da96f73588e6ff3af999e8d54",
    "selected_sha256": "d21d9012df3dba75cec6818a55d1d02d2e7656407fb65a69cf302dc12bde8ef1",
    "selection_authority": "parent integration decision following verified authorized final-response attachment inspection",
    "author_approved_corrections": false,
    "research_release_approved": false,
    "other_origins": [
      "libfile_d8b8ae2dc0048191a9f7334870209caf"
    ]
  },
  {
    "path": "selected-drafts/topics/music-design.md",
    "id": "GDR-CAND-20261010-P05-TOP-02",
    "selected_original_library_id": "libfile_daa2761322b48191b5fa397386009845",
    "original_sha256": "78394bd8ce2663f944231f94a464f18065cf8d3025b10ffde8b9ce31217e75c5",
    "selected_sha256": "78394bd8ce2663f944231f94a464f18065cf8d3025b10ffde8b9ce31217e75c5",
    "selection_authority": "parent integration decision following verified authorized final-response attachment inspection",
    "author_approved_corrections": false,
    "research_release_approved": false,
    "other_origins": [
      "libfile_4745af25e4008191927ae8f06e84fd90"
    ]
  },
  {
    "path": "selected-drafts/topics/localization-and-presentation.md",
    "id": "GDR-CAND-20261010-P05-TOP-03",
    "selected_original_library_id": "libfile_9e7d5426c34481919aec4a0bc9bddbff",
    "original_sha256": "ee5e10b32573e21167dfe34df96ab96eb1625ce47d1139ac9c9fa0fd6c68ba30",
    "selected_sha256": "8b85a286f3aa49a7054f902f7f9a4249bbff3fae740888ac6f312e724ff5e2f5",
    "selection_authority": "parent integration decision following verified authorized final-response attachment inspection",
    "author_approved_corrections": false,
    "research_release_approved": false,
    "other_origins": [
      "libfile_0fd6892e38148191b3ee18a06ed5fc4f"
    ]
  },
  {
    "path": "selected-drafts/patterns/state-valid-musical-transition.md",
    "id": "GDR-CAND-20261010-P05-PAT-01",
    "selected_original_library_id": "libfile_95e2e9ea447c8191a7f9b03617ae0d67",
    "original_sha256": "4fdab8a3c3e450f3156e83c9cdec9cdd61775ea6a2b22aed77f078d7e755cfe3",
    "selected_sha256": "4fdab8a3c3e450f3156e83c9cdec9cdd61775ea6a2b22aed77f078d7e755cfe3",
    "selection_authority": "parent integration decision following verified authorized final-response attachment inspection",
    "author_approved_corrections": false,
    "research_release_approved": false,
    "other_origins": [
      "libfile_766ed04aac70819182ecba162c169b63"
    ]
  },
  {
    "path": "selected-drafts/patterns/locale-resilient-message-unit.md",
    "id": "GDR-CAND-20261010-P05-PAT-02",
    "selected_original_library_id": "libfile_d12424c2907c8191ac5848e72cdf20e9",
    "original_sha256": "ebb0403f90192673f2f978ec2f573ca3253054a3badd6dc94e6425b696acf86f",
    "selected_sha256": "e222813ca2bcaf016a019f024a93b643b9456c474d563178a9aeca7544fe765a",
    "selection_authority": "parent integration decision following verified authorized final-response attachment inspection",
    "author_approved_corrections": false,
    "research_release_approved": false,
    "other_origins": [
      "libfile_164983f534a4819183ba35d4411f8ec1"
    ]
  },
  {
    "path": "selected-drafts/reviews/full-run-20261010-p05-review-packet.md",
    "id": "GDR-FULL-20261010:P05:review-packet",
    "selected_original_library_id": "libfile_96082d89aad481918ddf41b6dbfbafde",
    "original_sha256": "b4af4c1edecc93c29e55bc94e27aa5f0c17cc6f850ead8c8aa10b580c0eed1d1",
    "selected_sha256": "405e69ea9edcf2812bf599a3df54d70360dfaf84be0f5218b98053a49124437f",
    "selection_authority": "parent integration decision following verified authorized final-response attachment inspection",
    "author_approved_corrections": false,
    "research_release_approved": false,
    "other_origins": [
      "libfile_ca4bb863f2fc8191b824720563304c54"
    ]
  }
]
```

The original author delivery receipt was independently read from Library in packaging:5746 bytes, SHA25690bbb8acccf503296d6ec8bc4bd2c1523cec8800b1bb9017563c7d74e219bd40, exactly matching the authorized provenance report. It records original bytes and historical review status, not correction approval.

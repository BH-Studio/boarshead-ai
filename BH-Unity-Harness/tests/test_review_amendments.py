"""Static generic source-retention checks; not live GPT or game validation."""
import hashlib, json, unittest
from support import PACKAGE, bh

class ReviewAmendmentTests(unittest.TestCase):
    def setUp(self):
        self.overlays=[bh.load_json(p) for p in sorted((PACKAGE/'examples/profiles').glob('*.json'))]
        self.k12=PACKAGE/'design-gpt/Knowledge/K12_MILESTONES_CODEX_COMPILER_AND_COMPLETION.md'
    def test_overlay_matches_real_schema(self):
        self.assertEqual(len(self.overlays),2)
        for overlay in self.overlays:
            bh.validate(overlay,'overlay',bh.load_json(PACKAGE/'contracts/schema.json'))
    def test_open_game_decisions_not_promoted(self):
        for overlay in self.overlays:
            self.assertEqual(overlay['status'],'SYNTHETIC')
            self.assertTrue(overlay['synthetic'])
            self.assertGreaterEqual(len(overlay['open_decisions']),2)
            self.assertEqual(overlay['optional_capabilities'],[])
    def test_significant_generic_invariants_retained(self):
        groups=[]
        for overlay in self.overlays:
            ids=[r['id'] for r in overlay['invariants']]
            self.assertEqual(len(ids),len(set(ids)))
            self.assertGreaterEqual(len(ids),2)
            self.assertTrue({'Packages','ProjectSettings'} <= set(overlay['protected_paths']))
            groups.append(set(ids))
        self.assertFalse(groups[0] & groups[1])
    def test_prior_k12_preserved_exactly(self):
        prior=self.k12.read_bytes().split(b'\n## 11. Source-retained detail checks')[0]
        self.assertEqual(hashlib.sha256(prior).hexdigest(),'405e444b81a46f283409ae94d7cf8c769c89eab87dc8b3e5f87cc15ab0ff295b')
    def test_applicable_detail_checklists_present(self):
        text=self.k12.read_text(encoding='utf-8')
        for marker in ('**Behavior and contracts.**','**Authoring completeness.**','**Experiments and measurement.**','**Persistence, co-op and narrative.**','**Shared-record deltas.**','## 12. Game-agnostic compilation boundary'):
            self.assertIn(marker,text)
    def test_knowledge_digest_tracks_k12_without_extra_uploads(self):
        m=bh.load_json(PACKAGE/'design-gpt/KNOWLEDGE_MANIFEST.json')
        self.assertEqual(m['knowledge_count'],15)
        row=next(r for r in m['knowledge_files'] if r['path'].startswith('Knowledge/K12_'))
        self.assertEqual(row['sha256'],hashlib.sha256(self.k12.read_bytes()).hexdigest())

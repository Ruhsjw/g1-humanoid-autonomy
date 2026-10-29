import tempfile
import unittest
from pathlib import Path
from tools.audit_dataset import audit

class AuditTests(unittest.TestCase):
    def test_duplicate_contents_not_names(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d)
            for s in ('train','val'):(r/s/'images').mkdir(parents=True)
            (r/'train/images/a.jpg').write_bytes(b'one')
            (r/'val/images/renamed.jpg').write_bytes(b'one')
            (r/'val/images/a.jpg').write_bytes(b'two')
            self.assertEqual(audit(r)['overlapping_validation_images'],['val/images/renamed.jpg'])
    def test_missing_split(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):audit(d)

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import export_pdfs  # noqa: E402


class PdfExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.jobs = export_pdfs.build_jobs(ROOT / "docs" / "PDFS.md")

    def test_inventory_has_every_requested_group(self):
        filenames = {job.filename for job in self.jobs}
        self.assertEqual(49, len(filenames))
        self.assertIn("educacion-basica-completa.pdf", filenames)
        self.assertIn("ensenanza-media-completa.pdf", filenames)
        self.assertIn("trayectoria-escolar-completa.pdf", filenames)
        self.assertEqual(34, sum(name.startswith("por-asignatura-") for name in filenames))
        self.assertEqual(12, sum(name.startswith("por-nivel-") for name in filenames))

    def test_every_pdf_is_versioned_and_linked(self):
        catalog = (ROOT / "docs" / "PDFS.md").read_text(encoding="utf-8")
        for job in self.jobs:
            path = ROOT / "output" / "pdf" / job.filename
            self.assertTrue(path.is_file(), job.filename)
            self.assertGreater(path.stat().st_size, 1_000, job.filename)
            self.assertEqual(b"%PDF-", path.read_bytes()[:5], job.filename)
            self.assertIn(f"../output/pdf/{job.filename}", catalog)

    def test_sources_are_unique_inside_each_compilation(self):
        for job in self.jobs:
            self.assertEqual(len(job.sources), len(set(job.sources)), job.filename)
            for source in job.sources:
                self.assertTrue(source.is_file(), f"{job.filename}: {source}")


if __name__ == "__main__":
    unittest.main()

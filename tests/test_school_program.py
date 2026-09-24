import json
import unittest

from scripts.validate_licensing import ROOT, SOURCE_REQUIRED, validate as validate_licensing
from scripts.validate_school_program import validate as validate_program


class SchoolProgramTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))

    def test_program_validator(self):
        self.assertEqual(validate_program(), [])

    def test_licensing_validator(self):
        self.assertEqual(validate_licensing(), [])

    def test_catalog_truth(self):
        self.assertEqual(self.catalog["class_count"], 12997)
        self.assertEqual(self.catalog["objective_count"], 2823)
        self.assertEqual(self.catalog["course_count"], 12)
        self.assertEqual(self.catalog["subject_count"], 35)
        self.assertEqual(len(self.catalog["classes"]), 12997)
        self.assertEqual(self.catalog["schema_version"], 6)
        self.assertEqual(self.catalog["editorial_counts"]["borrador"], 1020)
        self.assertEqual(self.catalog["editorial_counts"]["desarrollada"], 36)
        self.assertEqual(self.catalog["editorial_counts"]["revisada"], 0)

    def test_first_grade_separates_developed_content_from_drafts(self):
        developed = [item for item in self.catalog["classes"] if item["editorial_status"] == "desarrollada"]
        first_grade = [item for item in self.catalog["classes"] if item["course_order"] == 1]
        self.assertEqual(len(first_grade), 1034)
        self.assertEqual(sum(item["editorial_status"] == "desarrollada" for item in first_grade), 14)
        self.assertEqual(sum(item["editorial_status"] == "borrador" for item in first_grade), 1020)
        self.assertEqual(len({item["oa_code"] for item in first_grade}), 237)
        self.assertEqual(len({item["subject"] for item in first_grade}), 11)
        self.assertEqual(len(developed), 36)

    def test_foundational_sequences_are_specific_and_officially_aligned(self):
        source = json.loads((ROOT / "content/developed-lessons.json").read_text(encoding="utf-8"))["objectives"]
        for code in ("MA01 OA 01", "LE01 OA 03"):
            objective = source[code]
            self.assertGreaterEqual(len(objective["official_alignment"]["indicators"]), 3)
            self.assertTrue(objective["official_alignment"]["source"].startswith("https://www.curriculumnacional.cl/"))
            self.assertNotIn("…", objective["topic"])
            for lesson in objective["lessons"]:
                self.assertNotIn("…", lesson["goal"])
                self.assertGreaterEqual(len(lesson["difficulty_actions"]), 3)
                self.assertTrue(lesson["home_task"])
                self.assertTrue(lesson["complementary"])

    def test_portal_names_first_grade_drafts_honestly(self):
        app = (ROOT / "site/app.js").read_text(encoding="utf-8")
        self.assertIn('item.editorial_status === "borrador"', app)
        self.assertIn('draft ? "Borrador"', app)

    def test_class_ids_and_codes_are_unique(self):
        classes = self.catalog["classes"]
        self.assertEqual([item["id"] for item in classes], list(range(1, 12998)))
        self.assertEqual(len({item["class_code"] for item in classes}), 12997)

    def test_every_class_has_public_page_and_anchor(self):
        cache = {}
        for item in self.catalog["classes"]:
            path, anchor = item["web_path"].split("#", 1)
            if path not in cache:
                cache[path] = (ROOT / "site" / path).read_text(encoding="utf-8")
            self.assertIn(f'id="{anchor}"', cache[path])

    def test_source_registry_is_safe(self):
        records = json.loads((ROOT / "examples/source-registry.example.json").read_text(encoding="utf-8"))["sources"]
        for record in records:
            self.assertFalse(SOURCE_REQUIRED - record.keys(), record["id"])
            if record["license"] == "UNKNOWN":
                self.assertFalse(record["redistributed"])


if __name__ == "__main__":
    unittest.main()

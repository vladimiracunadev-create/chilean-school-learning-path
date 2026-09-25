import json
import unittest

from scripts.validate_licensing import ROOT, SOURCE_REQUIRED, validate as validate_licensing
from scripts.validate_school_program import validate as validate_program
from scripts.grade_one_math_lessons import MATH_ATTITUDES, MATH_SKILLS, SEQUENCES, build_math_sequence, transversal_links
from scripts.grade_one_language_lessons import ATTITUDES as LANGUAGE_ATTITUDES, SEQUENCES as LANGUAGE_SEQUENCES, attitude_link, build_language_sequence


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
        self.assertEqual(self.catalog["schema_version"], 8)
        self.assertEqual(self.catalog["editorial_counts"]["borrador"], 717)
        self.assertEqual(self.catalog["editorial_counts"]["desarrollada"], 242)
        self.assertEqual(self.catalog["editorial_counts"]["integrada"], 97)
        self.assertEqual(self.catalog["editorial_counts"]["revisada"], 0)

    def test_first_grade_separates_developed_content_from_drafts(self):
        developed = [item for item in self.catalog["classes"] if item["editorial_status"] == "desarrollada"]
        first_grade = [item for item in self.catalog["classes"] if item["course_order"] == 1]
        self.assertEqual(len(first_grade), 1034)
        self.assertEqual(sum(item["editorial_status"] == "desarrollada" for item in first_grade), 220)
        self.assertEqual(sum(item["editorial_status"] == "integrada" for item in first_grade), 97)
        self.assertEqual(sum(item["editorial_status"] == "borrador" for item in first_grade), 717)
        self.assertEqual(len({item["oa_code"] for item in first_grade}), 237)
        self.assertEqual(len({item["subject"] for item in first_grade}), 11)
        self.assertEqual(len(developed), 242)

    def test_first_grade_mathematics_is_complete_without_double_counting_transversals(self):
        mathematics = [item for item in self.catalog["classes"] if item["course_order"] == 1 and item["subject_slug"] == "matematica"]
        core = [item for item in mathematics if item["editorial_status"] == "desarrollada"]
        transversal = [item for item in mathematics if item["editorial_status"] == "integrada"]
        self.assertEqual(len(core), 83)
        self.assertEqual(len({item["oa_code"] for item in core}), 20)
        self.assertEqual(len(transversal), 68)
        self.assertEqual(len({item["oa_code"] for item in transversal}), 16)
        self.assertFalse([item for item in mathematics if item["editorial_status"] == "borrador"])

    def test_first_grade_language_is_complete_without_double_counting_attitudes(self):
        language = [item for item in self.catalog["classes"] if item["course_order"] == 1 and item["subject_slug"] == "lenguaje-comunicacion"]
        core = [item for item in language if item["editorial_status"] == "desarrollada"]
        transversal = [item for item in language if item["editorial_status"] == "integrada"]
        self.assertEqual(len(core), 131)
        self.assertEqual(len({item["oa_code"] for item in core}), 26)
        self.assertEqual(len(transversal), 29)
        self.assertEqual(len({item["oa_code"] for item in transversal}), 7)
        self.assertFalse([item for item in language if item["editorial_status"] == "borrador"])

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

    def test_all_mathematics_lessons_have_distinct_pedagogical_content(self):
        source = json.loads((ROOT / "content/developed-lessons.json").read_text(encoding="utf-8"))["objectives"]
        sequences = [source["MA01 OA 01"]] + [build_math_sequence(code) for code in sorted(SEQUENCES)]
        lessons = [lesson for sequence in sequences for lesson in sequence["lessons"]]
        self.assertEqual(len(sequences), 20)
        self.assertEqual(len(lessons), 83)
        for field in ("title", "model", "guided", "ticket"):
            self.assertEqual(len({lesson[field] for lesson in lessons}), 83, field)
        self.assertTrue(all(len(lesson["difficulty_actions"]) >= 3 for lesson in lessons))
        manual_links = [transversal_links(1, index, lesson["goal"]) for index, lesson in enumerate(source["MA01 OA 01"]["lessons"])]
        links = [link for pair in manual_links for link in pair] + [link for sequence in sequences[1:] for lesson in sequence["lessons"] for link in lesson["transversal"]]
        self.assertEqual({link["code"] for link in links}, {code for code, _ in MATH_SKILLS + MATH_ATTITUDES})

    def test_all_language_lessons_have_distinct_pedagogical_content(self):
        source = json.loads((ROOT / "content/developed-lessons.json").read_text(encoding="utf-8"))["objectives"]
        sequences = [build_language_sequence(code) for code in sorted(LANGUAGE_SEQUENCES)] + [source["LE01 OA 03"]]
        lessons = [lesson for sequence in sequences for lesson in sequence["lessons"]]
        self.assertEqual(len(sequences), 26)
        self.assertEqual(len(lessons), 131)
        for field in ("title", "model", "ticket"):
            self.assertEqual(len({lesson[field] for lesson in lessons}), 131, field)
        manual_links = [attitude_link(3, index, lesson["goal"]) for index, lesson in enumerate(source["LE01 OA 03"]["lessons"])]
        links = manual_links + [link for sequence in sequences[:-1] for lesson in sequence["lessons"] for link in lesson["transversal"]]
        self.assertEqual({link["code"] for link in links}, {code for code, _ in LANGUAGE_ATTITUDES})

    def test_portal_names_first_grade_drafts_honestly(self):
        app = (ROOT / "site/app.js").read_text(encoding="utf-8")
        self.assertIn('item.editorial_status === "borrador"', app)
        self.assertIn('item.editorial_status === "integrada"', app)
        self.assertIn('integrated ? "Integrada"', app)

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

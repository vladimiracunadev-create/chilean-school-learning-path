import json
import unittest

from scripts.validate_licensing import ROOT, SOURCE_REQUIRED, validate as validate_licensing
from scripts.validate_school_program import validate as validate_program
from scripts.grade_one_math_lessons import MATH_ATTITUDES, MATH_SKILLS, SEQUENCES, build_math_sequence, transversal_links
from scripts.grade_one_language_lessons import ATTITUDES as LANGUAGE_ATTITUDES, SEQUENCES as LANGUAGE_SEQUENCES, attitude_link, build_language_sequence
from scripts.grade_one_science_history_arts_lessons import ART_ATTITUDES, HISTORY_ATTITUDES, HISTORY_SKILLS, SCIENCE_ATTITUDES, SCIENCE_SKILLS, SEQUENCES as SHA_SEQUENCES, build_sequence as build_sha_sequence
from scripts.grade_one_remaining_lessons import ATTITUDES as REMAINING_ATTITUDES, SEQUENCES as REMAINING_SEQUENCES, build_sequence as build_remaining_sequence
from scripts.grade_two_math_lessons import MATH_ATTITUDES as GRADE_TWO_MATH_ATTITUDES, MATH_SKILLS as GRADE_TWO_MATH_SKILLS, SEQUENCES as GRADE_TWO_MATH_SEQUENCES, build_math_sequence as build_grade_two_math_sequence, build_transversal_integration as build_grade_two_math_integration
from scripts.grade_two_language_science_history_lessons import LANGUAGE_ATTITUDES as GRADE_TWO_LANGUAGE_ATTITUDES, SCIENCE_SKILLS as GRADE_TWO_SCIENCE_SKILLS, SCIENCE_ATTITUDES as GRADE_TWO_SCIENCE_ATTITUDES, HISTORY_SKILLS as GRADE_TWO_HISTORY_SKILLS, HISTORY_ATTITUDES as GRADE_TWO_HISTORY_ATTITUDES, L as GRADE_TWO_LANGUAGE_SEQUENCES, S as GRADE_TWO_SCIENCE_SEQUENCES, H as GRADE_TWO_HISTORY_SEQUENCES, build_sequence as build_grade_two_lsh_sequence
from scripts.grade_two_arts_music_pe_lessons import ART_ATTITUDES as GRADE_TWO_ART_ATTITUDES, MUSIC_ATTITUDES as GRADE_TWO_MUSIC_ATTITUDES, PE_ATTITUDES as GRADE_TWO_PE_ATTITUDES, AR as GRADE_TWO_ART_SEQUENCES, MU as GRADE_TWO_MUSIC_SEQUENCES, EF as GRADE_TWO_PE_SEQUENCES, build_sequence as build_grade_two_amp_sequence
from scripts.grade_two_remaining_lessons import ATTITUDES as GRADE_TWO_REMAINING_ATTITUDES, OR as GRADE_TWO_ORIENTATION_SEQUENCES, TE as GRADE_TWO_TECHNOLOGY_SEQUENCES, EN as GRADE_TWO_ENGLISH_SEQUENCES, LC_META as GRADE_TWO_INDIGENOUS_SEQUENCES, build_sequence as build_grade_two_remaining_sequence


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
        self.assertEqual(self.catalog["editorial_counts"]["borrador"], 0)
        self.assertEqual(self.catalog["editorial_counts"]["desarrollada"], 1434)
        self.assertEqual(self.catalog["editorial_counts"]["integrada"], 694)
        self.assertEqual(self.catalog["editorial_counts"]["revisada"], 0)

    def test_first_grade_separates_developed_content_from_drafts(self):
        developed = [item for item in self.catalog["classes"] if item["editorial_status"] == "desarrollada"]
        first_grade = [item for item in self.catalog["classes"] if item["course_order"] == 1]
        self.assertEqual(len(first_grade), 1034)
        self.assertEqual(sum(item["editorial_status"] == "desarrollada" for item in first_grade), 691)
        self.assertEqual(sum(item["editorial_status"] == "integrada" for item in first_grade), 343)
        self.assertEqual(sum(item["editorial_status"] == "borrador" for item in first_grade), 0)
        self.assertEqual(len({item["oa_code"] for item in first_grade}), 237)
        self.assertEqual(len({item["subject"] for item in first_grade}), 11)
        self.assertEqual(len(developed), 1434)

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

    def test_second_grade_is_complete_without_double_counting_transversals(self):
        second_grade = [item for item in self.catalog["classes"] if item["course_order"] == 2]
        self.assertEqual(len(second_grade), 1072)
        self.assertEqual(len({item["oa_code"] for item in second_grade}), 247)
        self.assertEqual(len({item["subject"] for item in second_grade}), 11)
        mathematics = [item for item in second_grade if item["subject_slug"] == "matematica"]
        core = [item for item in mathematics if item["editorial_status"] == "desarrollada"]
        transversal = [item for item in mathematics if item["editorial_status"] == "integrada"]
        self.assertEqual((len(core), len({item["oa_code"] for item in core})), (93, 22))
        self.assertEqual((len(transversal), len({item["oa_code"] for item in transversal})), (64, 15))
        expected = {
            "lenguaje-comunicacion": (149, 30, 29, 7),
            "ciencias-naturales": (57, 14, 44, 11),
            "historia-geografia-ciencias-sociales": (72, 16, 72, 18),
            "artes-visuales": (24, 5, 28, 7),
            "musica": (29, 7, 28, 7),
            "educacion-fisica-salud": (47, 11, 32, 8),
            "orientacion": (35, 8, 0, 0),
            "tecnologia": (31, 7, 20, 5),
            "ingles-propuesta": (68, 14, 16, 4),
            "lengua-cultura-pueblos-originarios-ancestrales": (116, 27, 18, 4),
        }
        for slug, counts in expected.items():
            rows = [item for item in second_grade if item["subject_slug"] == slug]
            developed = [item for item in rows if item["editorial_status"] == "desarrollada"]
            integrated = [item for item in rows if item["editorial_status"] == "integrada"]
            self.assertEqual((len(developed), len({item["oa_code"] for item in developed}), len(integrated), len({item["oa_code"] for item in integrated})), counts)
        self.assertFalse([item for item in second_grade if item["editorial_status"] == "secuenciada"])

        sequences = [build_grade_two_math_sequence(code) for code in sorted(GRADE_TWO_MATH_SEQUENCES)]
        lessons = [lesson for sequence in sequences for lesson in sequence["lessons"]]
        self.assertEqual(len(lessons), 93)
        for field in ("title", "opening", "model", "guided", "independent", "ticket"):
            self.assertEqual(len({lesson[field] for lesson in lessons}), 93, f"MA02:{field}")
        self.assertTrue(all(len(lesson["difficulty_actions"]) >= 3 for lesson in lessons))
        self.assertEqual(
            {link["code"] for lesson in lessons for link in lesson["transversal"]},
            {code for code, _ in GRADE_TWO_MATH_SKILLS + GRADE_TWO_MATH_ATTITUDES},
        )
        integration = build_grade_two_math_integration({
            "oa_code": "de Actitud MA02 OAA F", "axis": "Actitudes",
            "oa_text": "Expresar y escuchar ideas de forma respetuosa. Unidad de Currículum y Evaluación Ministerio de Educación",
            "topic": "Expresar y escuchar ideas", "phases": [("Conectar y diagnosticar", "recuperar ideas previas")],
        })
        self.assertNotIn("Unidad de Currículum", integration["lessons"][0]["goal"])
        self.assertNotIn("Unidad de Currículum", integration["lessons"][0]["model"])

    def test_second_grade_documentation_matches_first_grade_depth(self):
        first_index = (ROOT / "docs/1-basico/README.md").read_text(encoding="utf-8")
        second_index = (ROOT / "docs/2-basico/README.md").read_text(encoding="utf-8")
        self.assertGreaterEqual(second_index.count("\n## "), first_index.count("\n## "))
        self.assertTrue((ROOT / "docs/SEGUNDO_BASICO.md").is_file())
        subject_slugs = {item["subject_slug"] for item in self.catalog["classes"] if item["course_order"] == 1}
        for slug in subject_slugs:
            first = (ROOT / "docs/1-basico" / f"{slug}.md").read_text(encoding="utf-8")
            second = (ROOT / "docs/2-basico" / f"{slug}.md").read_text(encoding="utf-8")
            self.assertGreaterEqual(second.count("\n## "), first.count("\n## "), slug)
            self.assertIn("Continuidad con 1° básico", second, slug)
            self.assertIn("Anatomía estable de cada clase", second, slug)
            self.assertIn("Preparación y materiales", second, slug)

    def test_second_grade_language_science_and_history_are_specific(self):
        expected = {
            "LE": (GRADE_TWO_LANGUAGE_SEQUENCES, 149, GRADE_TWO_LANGUAGE_ATTITUDES),
            "CN": (GRADE_TWO_SCIENCE_SEQUENCES, 57, GRADE_TWO_SCIENCE_SKILLS + GRADE_TWO_SCIENCE_ATTITUDES),
            "HI": (GRADE_TWO_HISTORY_SEQUENCES, 72, GRADE_TWO_HISTORY_SKILLS + GRADE_TWO_HISTORY_ATTITUDES),
        }
        for prefix, (profiles, lesson_count, transversal_items) in expected.items():
            sequences = [build_grade_two_lsh_sequence(code) for code in sorted(profiles)]
            lessons = [lesson for sequence in sequences for lesson in sequence["lessons"]]
            self.assertEqual(len(lessons), lesson_count, prefix)
            for field in ("title", "opening", "model", "independent", "ticket"):
                self.assertEqual(len({lesson[field] for lesson in lessons}), lesson_count, f"{prefix}:{field}")
            self.assertTrue(all(len(lesson["difficulty_actions"]) >= 3 for lesson in lessons))
            self.assertEqual({link["code"] for lesson in lessons for link in lesson["transversal"]}, {code for code, _ in transversal_items})

    def test_second_grade_arts_music_and_physical_education_are_specific(self):
        expected = {
            "AR": (GRADE_TWO_ART_SEQUENCES, 24, GRADE_TWO_ART_ATTITUDES),
            "MU": (GRADE_TWO_MUSIC_SEQUENCES, 29, GRADE_TWO_MUSIC_ATTITUDES),
            "EF": (GRADE_TWO_PE_SEQUENCES, 47, GRADE_TWO_PE_ATTITUDES),
        }
        for prefix, (profiles, lesson_count, attitudes) in expected.items():
            sequences = [build_grade_two_amp_sequence(code) for code in sorted(profiles)]
            lessons = [lesson for sequence in sequences for lesson in sequence["lessons"]]
            self.assertEqual(len(lessons), lesson_count, prefix)
            for field in ("title", "opening", "model", "guided", "independent", "ticket"):
                self.assertEqual(len({lesson[field] for lesson in lessons}), lesson_count, f"{prefix}:{field}")
            self.assertTrue(all(len(lesson["difficulty_actions"]) >= 3 for lesson in lessons))
            self.assertEqual({link["code"] for lesson in lessons for link in lesson["transversal"]}, {code for code, _ in attitudes})

    def test_second_grade_remaining_subjects_are_specific_safe_and_complete(self):
        expected = {
            "OR": (GRADE_TWO_ORIENTATION_SEQUENCES, 35, ()),
            "TE": (GRADE_TWO_TECHNOLOGY_SEQUENCES, 31, GRADE_TWO_REMAINING_ATTITUDES["TE"]),
            "EN": (GRADE_TWO_ENGLISH_SEQUENCES, 68, GRADE_TWO_REMAINING_ATTITUDES["EN"]),
            "LC": (GRADE_TWO_INDIGENOUS_SEQUENCES, 116, GRADE_TWO_REMAINING_ATTITUDES["LC"]),
        }
        for prefix, (profiles, lesson_count, attitudes) in expected.items():
            sequences = [build_grade_two_remaining_sequence(code) for code in sorted(profiles)]
            lessons = [lesson for sequence in sequences for lesson in sequence["lessons"]]
            self.assertEqual(len(lessons), lesson_count, prefix)
            for field in ("title", "opening", "model", "guided", "independent", "ticket"):
                self.assertEqual(len({lesson[field] for lesson in lessons}), lesson_count, f"{prefix}:{field}")
            self.assertTrue(all(len(lesson["difficulty_actions"]) >= 3 for lesson in lessons))
            self.assertEqual({link["code"] for lesson in lessons for link in lesson["transversal"]}, {code for code, _ in attitudes})
        cultural_text = " ".join(str(build_grade_two_remaining_sequence(code)) for code in GRADE_TWO_INDIGENOUS_SEQUENCES)
        for safeguard in ("no inventa lengua", "fuente comunitaria", "educador tradicional", "sin apropiarse"):
            self.assertIn(safeguard, cultural_text.lower())

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

    def test_science_history_and_arts_are_complete_and_specific(self):
        expected = {
            "CN": (49, SCIENCE_SKILLS + SCIENCE_ATTITUDES),
            "HI": (68, HISTORY_SKILLS + HISTORY_ATTITUDES),
            "AR": (24, ART_ATTITUDES),
        }
        for prefix, (lesson_count, transversal_items) in expected.items():
            sequences = [build_sha_sequence(code) for code in sorted(SHA_SEQUENCES) if code.startswith(prefix)]
            lessons = [lesson for sequence in sequences for lesson in sequence["lessons"]]
            self.assertEqual(len(lessons), lesson_count, prefix)
            for field in ("title", "opening", "model", "guided", "independent", "ticket"):
                self.assertEqual(len({lesson[field] for lesson in lessons}), lesson_count, f"{prefix}:{field}")
            self.assertTrue(all(len(lesson["difficulty_actions"]) >= 3 for lesson in lessons))
            self.assertEqual({link["code"] for lesson in lessons for link in lesson["transversal"]}, {code for code, _ in transversal_items})

    def test_remaining_subjects_are_complete_specific_and_culturally_safe(self):
        expected = {"MU": 29, "EF": 48, "OR": 35, "TE": 26, "EN": 69, "LC": 129}
        for prefix, lesson_count in expected.items():
            sequences = [build_remaining_sequence(code) for code in sorted(REMAINING_SEQUENCES) if code.startswith(prefix)]
            lessons = [lesson for sequence in sequences for lesson in sequence["lessons"]]
            self.assertEqual(len(lessons), lesson_count, prefix)
            for field in ("title", "opening", "model", "guided", "independent", "ticket"):
                self.assertEqual(len({lesson[field] for lesson in lessons}), lesson_count, f"{prefix}:{field}")
            self.assertTrue(all(len(lesson["difficulty_actions"]) >= 3 for lesson in lessons))
            expected_codes = {code for code, _ in REMAINING_ATTITUDES.get(prefix, ())}
            self.assertEqual({link["code"] for lesson in lessons for link in lesson["transversal"]}, expected_codes)
        cultural_text = " ".join(str(build_remaining_sequence(code)) for code in REMAINING_SEQUENCES if code.startswith("LC"))
        for safeguard in ("sin inventar lengua", "fuente comunitaria", "educador tradicional", "sin apropiarse"):
            self.assertIn(safeguard, cultural_text.lower())

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

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
from scripts.grade_three_math_language_lessons import LANGUAGE as GRADE_THREE_LANGUAGE_SEQUENCES, LANGUAGE_ATTITUDES as GRADE_THREE_LANGUAGE_ATTITUDES, MATH as GRADE_THREE_MATH_SEQUENCES, MATH_ATTITUDES as GRADE_THREE_MATH_ATTITUDES, MATH_SKILLS as GRADE_THREE_MATH_SKILLS, build_sequence as build_grade_three_ml_sequence, complete_pilot_sequence
from scripts.grade_three_science_history_lessons import HISTORY as GRADE_THREE_HISTORY_SEQUENCES, HISTORY_ATTITUDES as GRADE_THREE_HISTORY_ATTITUDES, HISTORY_SKILLS as GRADE_THREE_HISTORY_SKILLS, SCIENCE as GRADE_THREE_SCIENCE_SEQUENCES, SCIENCE_ATTITUDES as GRADE_THREE_SCIENCE_ATTITUDES, SCIENCE_SKILLS as GRADE_THREE_SCIENCE_SKILLS, build_sequence as build_grade_three_sh_sequence, complete_history_pilot
from scripts.grade_three_arts_pe_english_indigenous_lessons import AR as GRADE_THREE_ART_SEQUENCES, ATTITUDES as GRADE_THREE_APEI_ATTITUDES, EF as GRADE_THREE_PE_SEQUENCES, EN as GRADE_THREE_ENGLISH_SEQUENCES, LC as GRADE_THREE_INDIGENOUS_SEQUENCES, build_sequence as build_grade_three_apei_sequence
from scripts.grade_three_music_orientation_technology_lessons import ATTITUDES as GRADE_THREE_MOT_ATTITUDES, MU as GRADE_THREE_MUSIC_SEQUENCES, OR as GRADE_THREE_ORIENTATION_SEQUENCES, TE as GRADE_THREE_TECHNOLOGY_SEQUENCES, build_sequence as build_grade_three_mot_sequence
from scripts.grade_four_math_lessons import MATH as GRADE_FOUR_MATH_SEQUENCES, MATH_ATTITUDES as GRADE_FOUR_MATH_ATTITUDES, MATH_SKILLS as GRADE_FOUR_MATH_SKILLS, build_sequence as build_grade_four_math_sequence
from scripts.grade_four_remaining_lessons import SEQUENCES as GRADE_FOUR_REMAINING_SEQUENCES, build_sequence as build_grade_four_remaining_sequence
from scripts.grade_five_core_lessons import COUNTS as GRADE_FIVE_COUNTS, SEQUENCES as GRADE_FIVE_CORE_SEQUENCES, build_sequence as build_grade_five_core_sequence
from scripts.grade_five_remaining_lessons import SEQUENCES as GRADE_FIVE_REMAINING_SEQUENCES, build_sequence as build_grade_five_remaining_sequence
from scripts.grade_six_math_lessons import COUNTS as GRADE_SIX_MATH_COUNTS, SEQUENCES as GRADE_SIX_MATH_SEQUENCES, build_sequence as build_grade_six_math_sequence
from scripts.grade_six_remaining_lessons import SEQUENCES as GRADE_SIX_REMAINING_SEQUENCES, build_sequence as build_grade_six_remaining_sequence
from scripts.grade_seven_core_lessons import SEQUENCES as GRADE_SEVEN_CORE_SEQUENCES, build_sequence as build_grade_seven_core_sequence
from scripts.grade_seven_next_five_lessons import SEQUENCES as GRADE_SEVEN_NEXT_FIVE_SEQUENCES, build_sequence as build_grade_seven_next_five_sequence
from scripts.grade_seven_remaining_lessons import SEQUENCES as GRADE_SEVEN_REMAINING_SEQUENCES, build_sequence as build_grade_seven_remaining_sequence


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
        self.assertEqual(self.catalog["editorial_counts"]["desarrollada"], 5619)
        self.assertEqual(self.catalog["editorial_counts"]["integrada"], 2814)
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
        self.assertEqual(len(developed), 5619)

    def test_seventh_grade_mathematics_and_language_are_complete_and_specific(self):
        seventh = [item for item in self.catalog["classes"] if item["course_order"] == 7]
        expected = {
            "matematica": (83, 19, 82, 19),
            "lengua-literatura": (147, 25, 33, 8),
        }
        for slug, counts in expected.items():
            rows = [item for item in seventh if item["subject_slug"] == slug]
            developed = [item for item in rows if item["editorial_status"] == "desarrollada"]
            integrated = [item for item in rows if item["editorial_status"] == "integrada"]
            self.assertEqual(
                (len(developed), len({item["oa_code"] for item in developed}), len(integrated), len({item["oa_code"] for item in integrated})),
                counts,
            )
            self.assertFalse([item for item in rows if item["editorial_status"] in {"secuenciada", "borrador"}])
        sequences = [build_grade_seven_core_sequence(code) for code in sorted(GRADE_SEVEN_CORE_SEQUENCES)]
        lessons = [lesson for sequence in sequences for lesson in sequence["lessons"]]
        self.assertEqual(len(lessons), 230)
        self.assertTrue(all(len({lesson["title"] for lesson in sequence["lessons"]}) == len(sequence["lessons"]) for sequence in sequences))
        self.assertTrue(all(len(lesson["difficulty_actions"]) == 3 for lesson in lessons))
        for path in (
            ROOT / "curriculum/7-basico/matematica/ma07-oa-01.md",
            ROOT / "curriculum/7-basico/matematica/ma07-oa-11.md",
            ROOT / "curriculum/7-basico/lengua-literatura/le07-oa-03.md",
            ROOT / "curriculum/7-basico/lengua-literatura/le07-oa-24.md",
        ):
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("Tarjetas numéricas", text)
            self.assertNotIn("Microtexto original del proyecto: «Camila encontró", text)
            self.assertNotIn("comprenderé o produciré", text)
            self.assertNotIn("Modela cómo diagnosticar", text)
            self.assertNotIn("Piensa en voz alta para diagnosticar", text)
        self.assertNotIn(
            "arcos auxiliares",
            (ROOT / "curriculum/7-basico/matematica/ma07-oa-19.md").read_text(encoding="utf-8"),
        )
        self.assertNotIn(
            "adapta el mensaje",
            (ROOT / "curriculum/7-basico/lengua-literatura/le07-oa-03.md").read_text(encoding="utf-8"),
        )

    def test_seventh_grade_next_five_subjects_are_complete_specific_and_safe(self):
        seventh = [item for item in self.catalog["classes"] if item["course_order"] == 7]
        expected = {
            "ciencias-naturales": (72, 15, 89, 21),
            "historia-geografia-ciencias-sociales": (113, 23, 91, 20),
            "ingles": (80, 16, 21, 5),
            "educacion-fisica-salud": (25, 5, 28, 7),
            "artes-visuales": (29, 6, 33, 8),
        }
        for slug, counts in expected.items():
            rows = [item for item in seventh if item["subject_slug"] == slug]
            developed = [item for item in rows if item["editorial_status"] == "desarrollada"]
            integrated = [item for item in rows if item["editorial_status"] == "integrada"]
            self.assertEqual(
                (len(developed), len({item["oa_code"] for item in developed}), len(integrated), len({item["oa_code"] for item in integrated})),
                counts,
            )
            self.assertFalse([item for item in rows if item["editorial_status"] in {"secuenciada", "borrador"}])
        sequences = [build_grade_seven_next_five_sequence(code) for code in sorted(GRADE_SEVEN_NEXT_FIVE_SEQUENCES)]
        lessons = [lesson for sequence in sequences for lesson in sequence["lessons"]]
        self.assertEqual(len(sequences), 65)
        self.assertEqual(len(lessons), 319)
        self.assertTrue(all(len({lesson["title"] for lesson in sequence["lessons"]}) == len(sequence["lessons"]) for sequence in sequences))
        self.assertTrue(all(len(lesson["difficulty_actions"]) == 3 for lesson in lessons))
        samples = {
            "curriculum/7-basico/ciencias-naturales/cn07-oa-03.md": ("evitan perfiles personales", "estigmatizar"),
            "curriculum/7-basico/historia-geografia-ciencias-sociales/hi07-oa-14.md": ("Tawantinsuyu", "crónica colonial"),
            "curriculum/7-basico/ingles/in07-oa-06.md": ("information-gap", "accent"),
            "curriculum/7-basico/educacion-fisica-salud/ef07-oa-03.md": ("sin comparaciones corporales", "variante segura"),
            "curriculum/7-basico/artes-visuales/ar07-oa-03.md": ("privacidad", "autoría"),
        }
        for relative, tokens in samples.items():
            text = (ROOT / relative).read_text(encoding="utf-8")
            for token in tokens:
                self.assertIn(token, text)
            self.assertNotIn("Recursos reutilizables para", text)

    def test_seventh_grade_remaining_subjects_complete_the_level(self):
        expected = {
            "ingles-propuesta": (65, 13, 85, 21),
            "lengua-indigena": (41, 8, 0, 0),
            "musica": (30, 7, 37, 9),
            "orientacion": (49, 10, 0, 0),
            "tecnologia": (26, 6, 16, 4),
        }
        seventh = [item for item in self.catalog["classes"] if item["course_order"] == 7]
        for slug, counts in expected.items():
            rows = [item for item in seventh if item["subject_slug"] == slug]
            developed = [item for item in rows if item["editorial_status"] == "desarrollada"]
            integrated = [item for item in rows if item["editorial_status"] == "integrada"]
            self.assertEqual(
                (len(developed), len({item["oa_code"] for item in developed}), len(integrated), len({item["oa_code"] for item in integrated})),
                counts,
            )
        sequences = [build_grade_seven_remaining_sequence(code) for code in sorted(GRADE_SEVEN_REMAINING_SEQUENCES)]
        lessons = [lesson for sequence in sequences for lesson in sequence["lessons"]]
        self.assertEqual((len(sequences), len(lessons)), (44, 211))
        self.assertTrue(all(len({lesson["title"] for lesson in sequence["lessons"]}) == len(sequence["lessons"]) for sequence in sequences))
        self.assertTrue(all(len(lesson["difficulty_actions"]) >= 3 for lesson in lessons))
        self.assertEqual((len(seventh), sum(item["editorial_status"] == "desarrollada" for item in seventh), sum(item["editorial_status"] == "integrada" for item in seventh)), (1275, 760, 515))
        self.assertFalse([item for item in seventh if item["editorial_status"] in {"secuenciada", "borrador"}])
        samples = {
            "curriculum/7-basico/ingles-propuesta/en07-oa-09.md": ("information-gap", "accent imitation"),
            "curriculum/7-basico/lengua-indigena/li07-of-d.md": ("no suplanta saberes comunitarios", "no inventa lengua"),
            "curriculum/7-basico/musica/mu07-oa-05.md": ("evidencia audible", "volumen seguro"),
            "curriculum/7-basico/orientacion/or07-oa-03.md": ("caso ficticio", "no solicita experiencias personales"),
            "curriculum/7-basico/tecnologia/te07-oa-04.md": ("privacidad", "criterio"),
        }
        for relative, tokens in samples.items():
            text = (ROOT / relative).read_text(encoding="utf-8")
            for token in tokens:
                self.assertIn(token, text)
        for slug in expected:
            self.assertTrue((ROOT / "docs/7-basico" / f"{slug}.md").is_file(), slug)
            self.assertTrue((ROOT / "site/docs/7-basico" / f"{slug}.html").is_file(), slug)
        self.assertTrue((ROOT / "site/levels/7-basico.html").is_file())
        self.assertTrue((ROOT / "docs/SEPTIMO_BASICO.md").is_file())

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

    def test_completed_levels_have_documentation_at_equal_depth(self):
        main_readme = (ROOT / "README.md").read_text(encoding="utf-8")
        first_main = main_readme.split("## 🧒 1° básico · desarrollo OA por OA", 1)[1].split("## 📐 2° básico · desarrollo OA por OA", 1)[0]
        second_main = main_readme.split("## 📐 2° básico · desarrollo OA por OA", 1)[1].split("## 🧭 3° básico · desarrollo OA por OA", 1)[0]
        third_main = main_readme.split("## 🧭 3° básico · desarrollo OA por OA", 1)[1].split("## 🌎 4° básico · desarrollo OA por OA", 1)[0]
        fourth_main = main_readme.split("## 🌎 4° básico · desarrollo OA por OA", 1)[1].split("## 🔧 Cómo se mejora el contenido desarrollado", 1)[0]
        subject_slugs = {item["subject_slug"] for item in self.catalog["classes"] if item["course_order"] == 1}
        for slug in subject_slugs:
            self.assertIn(f"docs/1-basico/{slug}.md", first_main, slug)
            self.assertIn(f"docs/2-basico/{slug}.md", second_main, slug)
            self.assertIn(f"docs/3-basico/{slug}.md", third_main, slug)
            self.assertIn(f"docs/4-basico/{slug}.md", fourth_main, slug)
        self.assertEqual(first_main.count("docs/1-basico/"), 11)
        self.assertEqual(second_main.count("docs/2-basico/"), 11)
        self.assertEqual(third_main.count("docs/3-basico/"), 11)
        self.assertEqual(fourth_main.count("docs/4-basico/"), 11)
        self.assertIn("691 clases disciplinares", first_main)
        self.assertIn("721 clases disciplinares", second_main)
        self.assertIn("757 clases disciplinares", third_main)
        self.assertIn("811 clases disciplinares", fourth_main)
        first_index = (ROOT / "docs/1-basico/README.md").read_text(encoding="utf-8")
        second_index = (ROOT / "docs/2-basico/README.md").read_text(encoding="utf-8")
        third_index = (ROOT / "docs/3-basico/README.md").read_text(encoding="utf-8")
        fourth_index = (ROOT / "docs/4-basico/README.md").read_text(encoding="utf-8")
        self.assertGreaterEqual(second_index.count("\n## "), first_index.count("\n## "))
        self.assertGreaterEqual(third_index.count("\n## "), first_index.count("\n## "))
        self.assertGreaterEqual(fourth_index.count("\n## "), first_index.count("\n## "))
        self.assertTrue((ROOT / "docs/SEGUNDO_BASICO.md").is_file())
        self.assertTrue((ROOT / "docs/TERCERO_BASICO.md").is_file())
        self.assertTrue((ROOT / "docs/CUARTO_BASICO.md").is_file())
        for slug in subject_slugs:
            first = (ROOT / "docs/1-basico" / f"{slug}.md").read_text(encoding="utf-8")
            second = (ROOT / "docs/2-basico" / f"{slug}.md").read_text(encoding="utf-8")
            third = (ROOT / "docs/3-basico" / f"{slug}.md").read_text(encoding="utf-8")
            fourth = (ROOT / "docs/4-basico" / f"{slug}.md").read_text(encoding="utf-8")
            self.assertGreaterEqual(second.count("\n## "), first.count("\n## "), slug)
            self.assertGreaterEqual(third.count("\n## "), first.count("\n## "), slug)
            self.assertGreaterEqual(fourth.count("\n## "), first.count("\n## "), slug)
            self.assertIn("Continuidad con 1° básico", second, slug)
            self.assertIn("Continuidad con 2° básico", third, slug)
            self.assertIn("Continuidad con 3° básico", fourth, slug)
            self.assertIn("Anatomía estable de cada clase", second, slug)
            self.assertIn("Anatomía estable de cada clase", third, slug)
            self.assertIn("Anatomía estable de cada clase", fourth, slug)
            self.assertIn("Preparación y materiales", second, slug)
            self.assertIn("Preparación y materiales", third, slug)
        landing = (ROOT / "site/documentacion.html").read_text(encoding="utf-8")
        self.assertEqual(landing.count("Leer guía de 1° completa"), 11)
        self.assertEqual(landing.count("Leer guía de 2° completa"), 11)
        self.assertEqual(landing.count("Leer guía de 3° completa"), 11)
        self.assertIn("El mismo contrato documental de 1°", landing)
        self.assertIn("Tercer nivel completo", landing)

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

    def test_third_grade_mathematics_and_language_are_complete_and_specific(self):
        source = json.loads((ROOT / "content/developed-lessons.json").read_text(encoding="utf-8"))["objectives"]
        math_sequences = [build_grade_three_ml_sequence(code) for code in sorted(GRADE_THREE_MATH_SEQUENCES)]
        pilot = source["MA03 OA 11"]
        complete_pilot_sequence(pilot)
        math_lessons = [lesson for sequence in math_sequences + [pilot] for lesson in sequence["lessons"]]
        language_sequences = [build_grade_three_ml_sequence(code) for code in sorted(GRADE_THREE_LANGUAGE_SEQUENCES)]
        language_lessons = [lesson for sequence in language_sequences for lesson in sequence["lessons"]]
        self.assertEqual((len(math_sequences) + 1, len(math_lessons)), (26, 112))
        self.assertEqual((len(language_sequences), len(language_lessons)), (31, 157))
        for label, lessons in (("MA03", math_lessons), ("LE03", language_lessons)):
            for field in ("title", "opening", "model", "independent", "ticket"):
                self.assertEqual(len({lesson[field] for lesson in lessons}), len(lessons), f"{label}:{field}")
            self.assertTrue(all(len(lesson.get("difficulty_actions", [])) >= 3 for lesson in lessons), label)
        self.assertEqual(
            {link["code"] for lesson in math_lessons for link in lesson.get("transversal", [])},
            {code for code, _ in GRADE_THREE_MATH_SKILLS + GRADE_THREE_MATH_ATTITUDES},
        )
        self.assertEqual(
            {link["code"] for lesson in language_lessons for link in lesson.get("transversal", [])},
            {code for code, _ in GRADE_THREE_LANGUAGE_ATTITUDES},
        )
        grade_three = [item for item in self.catalog["classes"] if item["course_order"] == 3]
        expected = {"matematica": (112, 87), "lenguaje-comunicacion": (157, 29)}
        for slug, counts in expected.items():
            rows = [item for item in grade_three if item["subject_slug"] == slug]
            self.assertEqual((sum(item["editorial_status"] == "desarrollada" for item in rows), sum(item["editorial_status"] == "integrada" for item in rows)), counts)
            self.assertFalse([item for item in rows if item["editorial_status"] == "secuenciada"])

    def test_third_grade_science_and_history_are_complete_and_specific(self):
        source = json.loads((ROOT / "content/developed-lessons.json").read_text(encoding="utf-8"))["objectives"]
        science_sequences = [build_grade_three_sh_sequence(code) for code in sorted(GRADE_THREE_SCIENCE_SEQUENCES)]
        science_lessons = [lesson for sequence in science_sequences for lesson in sequence["lessons"]]
        history_sequences = [build_grade_three_sh_sequence(code) for code in sorted(GRADE_THREE_HISTORY_SEQUENCES)]
        pilot = source["HI03 OA 05"]
        complete_history_pilot(pilot)
        history_lessons = [lesson for sequence in history_sequences + [pilot] for lesson in sequence["lessons"]]
        self.assertEqual((len(science_sequences), len(science_lessons)), (13, 55))
        self.assertEqual((len(history_sequences) + 1, len(history_lessons)), (16, 72))
        for label, lessons in (("CN03", science_lessons), ("HI03", history_lessons)):
            for field in ("title", "opening", "model", "independent", "ticket"):
                self.assertEqual(len({lesson[field] for lesson in lessons}), len(lessons), f"{label}:{field}")
            self.assertTrue(all(len(lesson.get("difficulty_actions", [])) >= 3 for lesson in lessons), label)
        self.assertEqual(
            {link["code"] for lesson in science_lessons for link in lesson.get("transversal", [])},
            {code for code, _ in GRADE_THREE_SCIENCE_SKILLS + GRADE_THREE_SCIENCE_ATTITUDES},
        )
        self.assertEqual(
            {link["code"] for lesson in history_lessons for link in lesson.get("transversal", [])},
            {code for code, _ in GRADE_THREE_HISTORY_SKILLS + GRADE_THREE_HISTORY_ATTITUDES},
        )
        grade_three = [item for item in self.catalog["classes"] if item["course_order"] == 3]
        for slug, counts in {"ciencias-naturales": (55, 49), "historia-geografia-ciencias-sociales": (72, 72)}.items():
            rows = [item for item in grade_three if item["subject_slug"] == slug]
            self.assertEqual((sum(item["editorial_status"] == "desarrollada" for item in rows), sum(item["editorial_status"] == "integrada" for item in rows)), counts)
            self.assertFalse([item for item in rows if item["editorial_status"] == "secuenciada"])

    def test_third_grade_arts_pe_english_and_indigenous_are_complete(self):
        expected = {
            "AR": (GRADE_THREE_ART_SEQUENCES, 25, "artes-visuales", 28),
            "EF": (GRADE_THREE_PE_SEQUENCES, 48, "educacion-fisica-salud", 32),
            "EN": (GRADE_THREE_ENGLISH_SEQUENCES, 69, "ingles-propuesta", 16),
            "LC": (GRADE_THREE_INDIGENOUS_SEQUENCES, 116, "lengua-cultura-pueblos-originarios-ancestrales", 18),
        }
        grade_three = [item for item in self.catalog["classes"] if item["course_order"] == 3]
        for prefix, (profiles, developed_count, slug, integrated_count) in expected.items():
            sequences = [build_grade_three_apei_sequence(code) for code in sorted(profiles)]
            lessons = [lesson for sequence in sequences for lesson in sequence["lessons"]]
            self.assertEqual(len(lessons), developed_count, prefix)
            for field in ("title", "opening", "model", "guided", "independent", "ticket"):
                self.assertEqual(len({lesson[field] for lesson in lessons}), developed_count, f"{prefix}:{field}")
            self.assertTrue(all(len(lesson["difficulty_actions"]) >= 3 for lesson in lessons), prefix)
            self.assertEqual(
                {link["code"] for lesson in lessons for link in lesson["transversal"]},
                {code for code, _ in GRADE_THREE_APEI_ATTITUDES[prefix]},
            )
            rows = [item for item in grade_three if item["subject_slug"] == slug]
            self.assertEqual(
                (sum(item["editorial_status"] == "desarrollada" for item in rows), sum(item["editorial_status"] == "integrada" for item in rows)),
                (developed_count, integrated_count),
            )
            self.assertFalse([item for item in rows if item["editorial_status"] == "secuenciada"])
        cultural_text = " ".join(str(build_grade_three_apei_sequence(code)) for code in GRADE_THREE_INDIGENOUS_SEQUENCES).lower()
        for safeguard in ("no inventa lengua", "fuente comunitaria", "educador tradicional", "sin apropiarse", "no suplanta saberes comunitarios"):
            self.assertIn(safeguard, cultural_text)
        physical_text = " ".join(str(build_grade_three_apei_sequence(code)) for code in GRADE_THREE_PE_SEQUENCES).lower()
        for safeguard in ("sin comparar cuerpos", "señal de detención", "protocolo", "sin diagnosticar"):
            self.assertIn(safeguard, physical_text)

    def test_third_grade_music_orientation_and_technology_complete_the_level(self):
        expected = {
            "MU": (GRADE_THREE_MUSIC_SEQUENCES, 35, "musica", 28),
            "OR": (GRADE_THREE_ORIENTATION_SEQUENCES, 35, "orientacion", 0),
            "TE": (GRADE_THREE_TECHNOLOGY_SEQUENCES, 33, "tecnologia", 20),
        }
        grade_three = [item for item in self.catalog["classes"] if item["course_order"] == 3]
        for prefix, (profiles, developed_count, slug, integrated_count) in expected.items():
            sequences = [build_grade_three_mot_sequence(code) for code in sorted(profiles)]
            lessons = [lesson for sequence in sequences for lesson in sequence["lessons"]]
            self.assertEqual(len(lessons), developed_count, prefix)
            for field in ("title", "opening", "model", "guided", "independent", "ticket"):
                self.assertEqual(len({lesson[field] for lesson in lessons}), developed_count, f"{prefix}:{field}")
            self.assertTrue(all(len(lesson["difficulty_actions"]) >= 3 for lesson in lessons), prefix)
            expected_attitudes = {code for code, _ in GRADE_THREE_MOT_ATTITUDES.get(prefix, ())}
            self.assertEqual({link["code"] for lesson in lessons for link in lesson["transversal"]}, expected_attitudes)
            rows = [item for item in grade_three if item["subject_slug"] == slug]
            self.assertEqual(
                (sum(item["editorial_status"] == "desarrollada" for item in rows), sum(item["editorial_status"] == "integrada" for item in rows)),
                (developed_count, integrated_count),
            )
            self.assertFalse([item for item in rows if item["editorial_status"] == "secuenciada"])
        orientation_text = " ".join(str(build_grade_three_mot_sequence(code)) for code in GRADE_THREE_ORIENTATION_SEQUENCES).lower()
        for safeguard in ("caso ficticio", "nadie debe revelar", "consentimiento", "protocolo institucional", "no investiga"):
            self.assertIn(safeguard, orientation_text)
        technology_text = " ".join(str(build_grade_three_mot_sequence(code)) for code in GRADE_THREE_TECHNOLOGY_SEQUENCES).lower()
        for safeguard in ("autoría", "seguridad física y digital", "sin datos personales"):
            self.assertIn(safeguard, technology_text)
        self.assertEqual(len(grade_three), 1136)
        self.assertEqual(sum(item["editorial_status"] == "desarrollada" for item in grade_three), 757)
        self.assertEqual(sum(item["editorial_status"] == "integrada" for item in grade_three), 379)
        self.assertFalse([item for item in grade_three if item["editorial_status"] in {"secuenciada", "borrador"}])

    def test_fourth_grade_mathematics_is_complete_and_specific(self):
        sequences = [build_grade_four_math_sequence(code) for code in sorted(GRADE_FOUR_MATH_SEQUENCES)]
        lessons = [lesson for sequence in sequences for lesson in sequence["lessons"]]
        self.assertEqual(len(sequences), 27)
        self.assertEqual(len(lessons), 118)
        for field in ("title", "opening", "model", "guided", "independent", "ticket"):
            self.assertEqual(len({lesson[field] for lesson in lessons}), 118, field)
        self.assertTrue(all(len(lesson["difficulty_actions"]) >= 3 for lesson in lessons))
        self.assertEqual(
            {link["code"] for lesson in lessons for link in lesson["transversal"]},
            {code for code, _ in GRADE_FOUR_MATH_SKILLS + GRADE_FOUR_MATH_ATTITUDES},
        )
        mathematics = [item for item in self.catalog["classes"] if item["course_order"] == 4 and item["subject_slug"] == "matematica"]
        self.assertEqual(sum(item["editorial_status"] == "desarrollada" for item in mathematics), 118)
        self.assertEqual(sum(item["editorial_status"] == "integrada" for item in mathematics), 87)
        self.assertFalse([item for item in mathematics if item["editorial_status"] in {"secuenciada", "borrador"}])
        guide = (ROOT / "docs/4-basico/matematica.md").read_text(encoding="utf-8")
        for token in ("118 clases desarrolladas", "87 experiencias integradas", "Continuidad con 3° básico", "Anatomía estable", "Recorrido OA por OA", "Preparación y materiales", "Acceso y profundización"):
            self.assertIn(token, guide)
        self.assertTrue((ROOT / "site/docs/4-basico/matematica.html").is_file())

    def test_fourth_grade_is_complete_specific_and_documented_at_equal_depth(self):
        expected = {
            "artes-visuales": (25, 28), "ciencias-naturales": (71, 49),
            "educacion-fisica-salud": (49, 32), "historia-geografia-ciencias-sociales": (82, 77),
            "ingles-propuesta": (69, 16), "lengua-cultura-pueblos-originarios-ancestrales": (126, 18),
            "lenguaje-comunicacion": (161, 29), "matematica": (118, 87),
            "musica": (35, 28), "orientacion": (40, 0), "tecnologia": (35, 20),
        }
        fourth = [item for item in self.catalog["classes"] if item["course_order"] == 4]
        self.assertEqual(len(fourth), 1195)
        self.assertEqual(sum(item["editorial_status"] == "desarrollada" for item in fourth), 811)
        self.assertEqual(sum(item["editorial_status"] == "integrada" for item in fourth), 384)
        self.assertFalse([item for item in fourth if item["editorial_status"] in {"secuenciada", "borrador"}])
        for slug, counts in expected.items():
            rows = [item for item in fourth if item["subject_slug"] == slug]
            self.assertEqual((sum(item["editorial_status"] == "desarrollada" for item in rows), sum(item["editorial_status"] == "integrada" for item in rows)), counts, slug)
            guide = (ROOT / "docs/4-basico" / f"{slug}.md").read_text(encoding="utf-8")
            for token in ("Continuidad con 3° básico", "Anatomía estable de cada clase", "Recorrido OA por OA", "Preparación y materiales", "Acceso y profundización"):
                self.assertIn(token, guide, f"{slug}:{token}")
            self.assertTrue((ROOT / "site/docs/4-basico" / f"{slug}.html").is_file(), slug)
        lessons = [lesson for code in sorted(GRADE_FOUR_REMAINING_SEQUENCES) for lesson in build_grade_four_remaining_sequence(code)["lessons"]]
        self.assertEqual(len(lessons), 693)
        for field in ("title", "opening", "model", "guided", "independent", "ticket"):
            self.assertEqual(len({lesson[field] for lesson in lessons}), len(lessons), field)
        self.assertTrue(all(len(lesson["difficulty_actions"]) >= 3 for lesson in lessons))
        cultural = " ".join(str(build_grade_four_remaining_sequence(code)) for code in GRADE_FOUR_REMAINING_SEQUENCES if code.startswith("LC04")).lower()
        for safeguard in ("no inventa lengua", "fuente comunitaria", "educador tradicional", "no suplanta saberes comunitarios", "sin apropiarse"):
            self.assertIn(safeguard, cultural)

    def test_fifth_grade_math_language_and_science_are_complete_and_specific(self):
        expected = {
            "MA": (27, 115, 86, "matematica"),
            "LE": (30, 166, 29, "lenguaje-comunicacion"),
            "CN": (14, 64, 58, "ciencias-naturales"),
        }
        fifth = [item for item in self.catalog["classes"] if item["course_order"] == 5]
        all_lessons = []
        for prefix, (oa_count, developed_count, integrated_count, slug) in expected.items():
            codes = sorted(code for code in GRADE_FIVE_CORE_SEQUENCES if code.startswith(prefix))
            sequences = [build_grade_five_core_sequence(code) for code in codes]
            lessons = [lesson for sequence in sequences for lesson in sequence["lessons"]]
            all_lessons.extend(lessons)
            self.assertEqual((len(codes), len(lessons)), (oa_count, developed_count), prefix)
            self.assertEqual(sum(GRADE_FIVE_COUNTS[prefix]), developed_count)
            rows = [item for item in fifth if item["subject_slug"] == slug]
            self.assertEqual(
                (sum(item["editorial_status"] == "desarrollada" for item in rows), sum(item["editorial_status"] == "integrada" for item in rows)),
                (developed_count, integrated_count),
            )
            self.assertFalse([item for item in rows if item["editorial_status"] in {"secuenciada", "borrador"}])
            guide = (ROOT / "docs/5-basico" / f"{slug}.md").read_text(encoding="utf-8")
            for token in ("Continuidad con 4° básico", "Anatomía estable de cada clase", "Recorrido OA por OA", "Preparación y materiales", "Acceso y profundización"):
                self.assertIn(token, guide, f"{slug}:{token}")
            self.assertTrue((ROOT / "site/docs/5-basico" / f"{slug}.html").is_file(), slug)
        self.assertEqual(len(all_lessons), 345)
        for field in ("title", "opening", "model", "guided", "independent", "ticket"):
            self.assertEqual(len({lesson[field] for lesson in all_lessons}), len(all_lessons), field)
        self.assertTrue(all(len(lesson["difficulty_actions"]) >= 3 for lesson in all_lessons))
        fifth_index = (ROOT / "docs/5-basico/README.md").read_text(encoding="utf-8")
        for token in ("12 denominaciones curriculares", "920 clases desarrolladas", "420 experiencias integradas", "0 propuestas pendientes"):
            self.assertIn(token, fifth_index)
        self.assertTrue((ROOT / "site/levels/5-basico.html").is_file())

    def test_fifth_grade_remaining_subjects_complete_the_level(self):
        expected = {
            "AR": (5, 27, 28, "artes-visuales"),
            "EF": (11, 49, 32, "educacion-fisica-salud"),
            "HI": (22, 106, 91, "historia-geografia-ciencias-sociales"),
            "IN": (16, 76, 16, "ingles"),
            "EN": (15, 71, 32, "ingles-propuesta"),
            "LC": (29, 135, 0, "lengua-cultura-pueblos-originarios-ancestrales"),
            "MU": (8, 35, 28, "musica"),
            "OR": (9, 41, 0, "orientacion"),
            "TE": (7, 35, 20, "tecnologia"),
        }
        fifth = [item for item in self.catalog["classes"] if item["course_order"] == 5]
        all_lessons = []
        for prefix, (oa_count, developed_count, integrated_count, slug) in expected.items():
            codes = sorted(code for code in GRADE_FIVE_REMAINING_SEQUENCES if code.startswith(prefix))
            lessons = [lesson for code in codes for lesson in build_grade_five_remaining_sequence(code)["lessons"]]
            all_lessons.extend(lessons)
            self.assertEqual((len(codes), len(lessons)), (oa_count, developed_count), prefix)
            rows = [item for item in fifth if item["subject_slug"] == slug]
            self.assertEqual(
                (sum(item["editorial_status"] == "desarrollada" for item in rows), sum(item["editorial_status"] == "integrada" for item in rows)),
                (developed_count, integrated_count),
            )
            guide = (ROOT / "docs/5-basico" / f"{slug}.md").read_text(encoding="utf-8")
            for token in ("Continuidad con 4° básico", "Anatomía estable de cada clase", "Recorrido OA por OA", "Preparación y materiales", "Acceso y profundización"):
                self.assertIn(token, guide, f"{slug}:{token}")
            self.assertTrue((ROOT / "site/docs/5-basico" / f"{slug}.html").is_file(), slug)
        self.assertEqual(len(all_lessons), 575)
        for field in ("title", "opening", "model", "guided", "independent", "ticket"):
            self.assertEqual(len({lesson[field] for lesson in all_lessons}), len(all_lessons), field)
        self.assertTrue(all(len(lesson["difficulty_actions"]) >= 3 for lesson in all_lessons))
        cultural = " ".join(str(build_grade_five_remaining_sequence(code)) for code in GRADE_FIVE_REMAINING_SEQUENCES if code.startswith("LC05")).lower()
        for safeguard in ("no inventa lengua", "fuente comunitaria", "educador tradicional", "no suplanta saberes comunitarios", "sin apropiarse"):
            self.assertIn(safeguard, cultural)
        self.assertEqual((len(fifth), sum(item["editorial_status"] == "desarrollada" for item in fifth), sum(item["editorial_status"] == "integrada" for item in fifth)), (1340, 920, 420))
        self.assertFalse([item for item in fifth if item["editorial_status"] in {"secuenciada", "borrador"}])

    def test_sixth_grade_mathematics_is_complete_and_specific(self):
        codes = sorted(GRADE_SIX_MATH_SEQUENCES)
        sequences = [build_grade_six_math_sequence(code) for code in codes]
        lessons = [lesson for sequence in sequences for lesson in sequence["lessons"]]
        self.assertEqual((len(codes), len(lessons), sum(GRADE_SIX_MATH_COUNTS)), (24, 98, 98))
        for field in ("title", "opening", "model", "guided", "independent", "ticket"):
            self.assertEqual(len({lesson[field] for lesson in lessons}), 98, field)
        self.assertTrue(all(len(lesson["difficulty_actions"]) >= 3 for lesson in lessons))
        sixth_math = [item for item in self.catalog["classes"] if item["course_order"] == 6 and item["subject_slug"] == "matematica"]
        self.assertEqual(
            (sum(item["editorial_status"] == "desarrollada" for item in sixth_math), sum(item["editorial_status"] == "integrada" for item in sixth_math)),
            (98, 88),
        )
        self.assertFalse([item for item in sixth_math if item["editorial_status"] in {"secuenciada", "borrador"}])
        guide = (ROOT / "docs/6-basico/matematica.md").read_text(encoding="utf-8")
        for token in ("Continuidad con 5° básico", "Anatomía estable de cada clase", "Recorrido OA por OA", "Preparación y materiales", "Acceso y profundización"):
            self.assertIn(token, guide)
        self.assertTrue((ROOT / "site/docs/6-basico/matematica.html").is_file())
        self.assertTrue((ROOT / "site/levels/6-basico.html").is_file())

    def test_sixth_grade_remaining_subjects_complete_the_level(self):
        expected = {
            "AR": (5, 27, 28, "artes-visuales"),
            "CN": (18, 78, 53, "ciencias-naturales"),
            "EF": (11, 50, 32, "educacion-fisica-salud"),
            "HI": (26, 116, 96, "historia-geografia-ciencias-sociales"),
            "IN": (16, 76, 16, "ingles"),
            "EN": (15, 74, 32, "ingles-propuesta"),
            "LC": (29, 144, 0, "lengua-cultura-pueblos-originarios-ancestrales"),
            "LE": (31, 176, 29, "lenguaje-comunicacion"),
            "MU": (8, 35, 28, "musica"),
            "OR": (9, 41, 0, "orientacion"),
            "TE": (7, 37, 20, "tecnologia"),
        }
        sixth = [item for item in self.catalog["classes"] if item["course_order"] == 6]
        all_lessons = []
        for prefix, (oa_count, developed_count, integrated_count, slug) in expected.items():
            codes = sorted(code for code in GRADE_SIX_REMAINING_SEQUENCES if code.startswith(prefix))
            lessons = [lesson for code in codes for lesson in build_grade_six_remaining_sequence(code)["lessons"]]
            all_lessons.extend(lessons)
            self.assertEqual((len(codes), len(lessons)), (oa_count, developed_count), prefix)
            rows = [item for item in sixth if item["subject_slug"] == slug]
            self.assertEqual(
                (sum(item["editorial_status"] == "desarrollada" for item in rows), sum(item["editorial_status"] == "integrada" for item in rows)),
                (developed_count, integrated_count),
            )
            guide = (ROOT / "docs/6-basico" / f"{slug}.md").read_text(encoding="utf-8")
            for token in ("Continuidad con 5° básico", "Anatomía estable de cada clase", "Recorrido OA por OA", "Preparación y materiales", "Acceso y profundización"):
                self.assertIn(token, guide, f"{slug}:{token}")
            self.assertTrue((ROOT / "site/docs/6-basico" / f"{slug}.html").is_file(), slug)
        self.assertEqual(len(all_lessons), 854)
        self.assertTrue(all(len(lesson["difficulty_actions"]) >= 3 for lesson in all_lessons))
        cultural = " ".join(str(build_grade_six_remaining_sequence(code)) for code in GRADE_SIX_REMAINING_SEQUENCES if code.startswith("LC06")).lower()
        for safeguard in ("no inventa lengua", "fuente comunitaria", "educador tradicional", "no suplanta saberes comunitarios", "sin apropiarse"):
            self.assertIn(safeguard, cultural)
        self.assertEqual((len(sixth), sum(item["editorial_status"] == "desarrollada" for item in sixth), sum(item["editorial_status"] == "integrada" for item in sixth)), (1374, 952, 422))
        self.assertFalse([item for item in sixth if item["editorial_status"] in {"secuenciada", "borrador"}])
        self.assertTrue((ROOT / "docs/SEXTO_BASICO.md").is_file())

    def test_every_developed_class_publishes_the_classroom_quality_pack(self):
        quality_tokens = (
            "### Insumo concreto y consigna",
            "**Recurso listo para usar:**",
            "**Consigna exacta:**",
            "**Referencia para modelar y corregir:**",
            "**Pauta de evaluación de cuatro niveles:**",
            "| Distribución de 45 minutos |",
        )
        forbidden = (
            "responde al foco específico de la clase",
            "Recursos reutilizables para",
            "Modela cómo modelar",
            "no por imitar el ejemplo",
            "no se transfiere mecánicamente a otro OA",
            ",,",
            "oficial..",
        )
        objectives = {}
        for item in self.catalog["classes"]:
            if item["editorial_status"] == "desarrollada":
                objectives.setdefault(item["path"].split("#", 1)[0], item["lesson_count"])
        for relative_path, lesson_count in objectives.items():
            document = (ROOT / relative_path).read_text(encoding="utf-8")
            for token in quality_tokens:
                self.assertEqual(document.count(token), lesson_count, f"{relative_path}:{token}")
            for phrase in forbidden:
                self.assertNotIn(phrase, document, f"{relative_path}:{phrase}")

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

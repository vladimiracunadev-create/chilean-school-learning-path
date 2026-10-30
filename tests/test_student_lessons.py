import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import student_lessons as sl  # noqa: E402
import validate_student_lessons as validator  # noqa: E402

sl.load_all()


class StudentLessonContent(unittest.TestCase):
    def test_registry_is_not_empty_and_passes_structure(self):
        self.assertGreaterEqual(len(sl.REGISTRY), 20)
        for (oa_code, number), content in sl.REGISTRY.items():
            self.assertEqual(sl.problems(oa_code, number, content), [], f"{oa_code} clase {number}")

    def test_validator_accepts_current_state(self):
        self.assertEqual(validator.check(), [])

    def test_every_lesson_has_all_difficulty_tiers_and_solutions(self):
        for (oa_code, number), content in sl.REGISTRY.items():
            for key, _label, _prefix in sl.TIERS:
                self.assertTrue(content["tiers"].get(key), f"{oa_code} clase {number}: falta {key}")
            for item in sl.all_questions(content):
                self.assertTrue(item["a"].strip())
                self.assertGreaterEqual(len(item["why"].split()), 4)

    def test_wrong_arithmetic_answer_is_detected(self):
        key, content = next(iter(sl.REGISTRY.items()))
        broken = copy.deepcopy(content)
        broken["tiers"]["apply"][0] = sl.ex("¿Cuánto es 40 + 6?", "47", "Cuatro decenas y seis unidades.", calc="40+6")
        self.assertTrue(any("da 46" in text for text in sl.problems(*key, broken)))

    def test_evaluator_refuses_non_arithmetic_code(self):
        with self.assertRaises(ValueError):
            sl.evaluate("__import__('os').system('echo x')")

    def test_delegated_cases_are_rejected(self):
        key, content = next(iter(sl.REGISTRY.items()))
        broken = copy.deepcopy(content)
        broken["open_task"]["statement"] = "Prepara tres casos y resuélvelos."
        self.assertTrue(any("delega" in text for text in sl.problems(*key, broken)))

    def test_thin_lesson_is_rejected(self):
        thin = {"use": "x", "prior": ["x"], "explain": ["breve"], "vocab": [("a", "b")], "worked": [], "mistakes": [], "tiers": {}, "selfcheck": []}
        self.assertGreaterEqual(len(sl.problems("MA02 OA 99", 1, thin)), 5)

    def test_number_only_variants_share_a_template(self):
        self.assertEqual(validator.template("Completa 137, 139, __"), validator.template("Completa 52, 54, __"))
        self.assertNotEqual(validator.template("Suma 3 y 4"), validator.template("Resta 3 y 4"))

    def test_registered_lessons_exist_in_the_curriculum(self):
        for oa_code, number in sl.REGISTRY:
            self.assertIsNotNone(validator.curriculum_file(oa_code), oa_code)


class StudentLessonPublication(unittest.TestCase):
    def test_markdown_publishes_notebook_and_drops_mismatched_generic_resource(self):
        text = (ROOT / "curriculum/2-basico/matematica/ma02-oa-05.md").read_text(encoding="utf-8")
        self.assertIn("### Cuaderno del estudiante", text)
        self.assertIn("**Solucionario razonado**", text)
        self.assertNotIn("Tarjetas numéricas 18, 20, 21", text)

    def test_html_publishes_notebook_and_answer_key(self):
        text = (ROOT / "site/classes/2-basico/matematica/ma02-oa-05.html").read_text(encoding="utf-8")
        self.assertIn('class="student-notebook"', text)
        self.assertIn('class="answer-key"', text)

    def test_coverage_panel_is_in_sync(self):
        panel = (ROOT / "docs/COBERTURA_ESTUDIANTE.md").read_text(encoding="utf-8")
        self.assertEqual(panel, validator.report())
        self.assertIn("pendiente", panel)

    def test_content_audit_is_in_sync(self):
        import audit_content
        self.assertEqual((ROOT / "docs/AUDITORIA_CONTENIDO.md").read_text(encoding="utf-8"), audit_content.report())


if __name__ == "__main__":
    unittest.main()

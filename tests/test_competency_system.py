import copy
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from competency_evidence import EvidenceError, analyze_cycle  # noqa: E402
from validate_competency_system import validate  # noqa: E402


class CompetencySystemTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = json.loads(
            (ROOT / "evidence/examples/reading-inference-cycle.json").read_text(
                encoding="utf-8"
            )
        )

    def test_all_competency_assets_are_coherent(self):
        self.assertEqual(validate(), [])

    def test_complete_example_documents_mastery_without_a_score(self):
        summary = analyze_cycle(self.example)
        self.assertEqual(summary["status"], "mastery_documented")
        serialized = json.dumps(summary, ensure_ascii=False).lower()
        self.assertNotIn("percentage", serialized)
        self.assertNotIn("percent", serialized)
        self.assertNotIn("score", serialized)

    def test_one_observation_never_becomes_a_pattern(self):
        cycle = copy.deepcopy(self.example)
        cycle["records"] = cycle["records"][:1]
        summary = analyze_cycle(cycle)
        self.assertEqual(summary["status"], "observation_only")
        self.assertEqual(summary["counts"]["patterns"], 0)

    def test_repeated_item_in_one_session_is_not_a_pattern(self):
        cycle = copy.deepcopy(self.example)
        duplicate = copy.deepcopy(cycle["records"][0])
        duplicate["id"] = "ev-repeat"
        cycle["records"] = [cycle["records"][0], duplicate]
        summary = analyze_cycle(cycle)
        self.assertEqual(summary["status"], "observation_only")
        self.assertEqual(summary["counts"]["patterns"], 0)

    def test_personal_identifier_is_rejected(self):
        cycle = copy.deepcopy(self.example)
        cycle["learner_ref"] = "student@example.com"
        with self.assertRaises(EvidenceError):
            analyze_cycle(cycle)

    def test_frameworks_are_decoupled_from_taxonomy(self):
        taxonomy = json.loads(
            (ROOT / "competencies/taxonomy.v1.json").read_text(encoding="utf-8")
        )
        self.assertNotIn("frameworks", taxonomy)
        framework_ids = {
            framework["id"]
            for framework in json.loads(
                (ROOT / "competencies/frameworks.v1.json").read_text(encoding="utf-8")
            )["frameworks"]
        }
        self.assertTrue(
            {"paes-2027", "simce-2026", "pisa-2025", "timss-2027", "pirls-2026"}
            <= framework_ids
        )

    def test_main_readme_explains_new_content_and_existing_connections(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for token in (
            "Qué contenido es nuevo, dónde se lee y qué falta",
            "86 habilidades en 7 dominios",
            "43 enlaces a 37 OA distintos",
            "Cómo se conecta realmente con una clase existente",
            "OA oficial LE04 OA 04",
            "Tarea “El recreo bajo la lluvia”",
            "Qué relación es oficial y cuál no",
            "no un mapeo exhaustivo de los 2.823 OA",
        ):
            self.assertIn(token, readme)

    def test_teacher_views_do_not_require_opening_json(self):
        public_pages = [
            ROOT / "site/competencias/index.html",
            ROOT / "site/competencias/habilidades.html",
            ROOT / "site/competencias/banco-tareas.html",
            ROOT / "site/competencias/marcos-evaluacion.html",
        ]
        public_pages.extend((ROOT / "site/competencias/tareas").glob("*.html"))
        self.assertGreaterEqual(len(public_pages), 10)
        for path in public_pages:
            content = path.read_text(encoding="utf-8")
            self.assertNotIn('href="data/', content, path)
            self.assertNotIn("multiple_choice", content, path)
            self.assertNotIn("pedagogical_inference", content, path)

    def test_framework_view_answers_what_was_implemented(self):
        content = (ROOT / "site/competencias/marcos-evaluacion.html").read_text(
            encoding="utf-8"
        )
        for token in (
            "Qué se hizo con PAES y los otros marcos",
            "6 correspondencias documentadas y 1 tarea original",
            "No se creó un preuniversitario",
            "Regreso al currículo",
            "Propuesta propia del proyecto",
        ):
            self.assertIn(token, content)

    def test_each_task_has_a_complete_teacher_view(self):
        bank = json.loads(
            (ROOT / "assessments/item-bank.v1.json").read_text(encoding="utf-8")
        )
        pages = list((ROOT / "site/competencias/tareas").glob("*.html"))
        self.assertEqual(len(bank["items"]), len(pages))
        for path in pages:
            content = path.read_text(encoding="utf-8")
            for token in (
                "Versión para aplicar",
                "Clave docente",
                "Solución explicada",
                "Rúbrica descriptiva",
                "OA y clases existentes para intervenir",
                "no posee validación psicométrica",
            ):
                self.assertIn(token, content, path)


if __name__ == "__main__":
    unittest.main()

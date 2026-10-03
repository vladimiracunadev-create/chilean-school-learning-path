import copy
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from competency_evidence import EvidenceError, analyze_cycle  # noqa: E402
from evaluation_catalog import INSTRUMENTS, VARIANTS  # noqa: E402
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

    def test_evaluation_center_is_named_and_complete(self):
        center = (ROOT / "site/evaluaciones/index.html").read_text(encoding="utf-8")
        for token in (
            "Evaluaciones complementarias",
            "PAES",
            "SIMCE",
            "DIA",
            "Impulso Lector",
            "Estudios nacionales",
            "PISA",
            "TIMSS",
            "PIRLS",
            "ERCE",
            "ICILS",
            "ICCS",
            "ECES",
            "Todas las entradas lectoras",
            "Informe de brechas histórico",
        ):
            self.assertIn(token, center)
        self.assertNotIn('href="../competencias/data/', center)
        for key in INSTRUMENTS:
            page = ROOT / "site/evaluaciones" / f"{key}.html"
            self.assertTrue(page.is_file(), key)
            content = page.read_text(encoding="utf-8")
            for token in (
                "Qué es y por qué existe",
                "Historia y versiones anteriores",
                "Cómo funciona y qué observa",
                "Qué enseñar antes, qué clase abrir y cómo comprobar",
                "Fuentes institucionales consultadas",
            ):
                self.assertIn(token, content, page)

    def test_every_instrument_has_a_substantive_teacher_profile(self):
        required = {
            "definition", "why_exists", "responsible", "first_cycle", "cadence",
            "history", "predecessors", "design", "reporting", "classroom_use", "boundaries",
        }
        for key, instrument in INSTRUMENTS.items():
            self.assertTrue(required.issubset(instrument), key)
            self.assertGreaterEqual(len(instrument["history"]), 3, key)
            self.assertGreaterEqual(len(instrument["design"]), 3, key)
            self.assertGreaterEqual(len(instrument["boundaries"]), 3, key)
            self.assertGreater(len(instrument["definition"]), 120, key)
        paes = (ROOT / "site/evaluaciones/paes.html").read_text(encoding="utf-8")
        for token in ("PAA", "PSU", "PDT", "Primera PAES", "100 a 1.000", "la competencia no comienza en 4° medio"):
            self.assertIn(token, paes)
        for level in ("4° básico", "6° básico", "8° básico", "1° medio", "2° medio", "3° medio", "4° medio"):
            self.assertIn(level, paes)
        eces = (ROOT / "site/evaluaciones/eces.html").read_text(encoding="utf-8")
        self.assertIn("unidad de análisis principal es el sistema", eces)
        self.assertIn("No corresponde producir una muestra escolar ECES", eces)

    def test_every_documented_variant_has_a_scored_teacher_facing_sample(self):
        self.assertEqual(len(VARIANTS), 45)
        for variant in VARIANTS:
            page = ROOT / "site/evaluaciones/ensayos" / f"{variant['id']}.html"
            self.assertTrue(page.is_file(), variant["id"])
            content = page.read_text(encoding="utf-8")
            for token in (
                "Muestra breve original · cobertura parcial · no oficial",
                "Calcular puntos de la muestra",
                "máximo 4 puntos",
                "No es un puntaje oficial",
                "Contenido y desempeño que se observará",
                "Ruta de intervención con clases existentes",
                "Cómo reevaluar",
                "Abrir la clase exacta",
            ):
                self.assertIn(token, content, page)

    def test_implementation_status_uses_pedagogical_capabilities(self):
        status = (ROOT / "docs/ESTADO_IMPLEMENTACION.md").read_text(encoding="utf-8")
        for token in (
            "Capacidad", "Qué existe", "Límite o trabajo pendiente",
            "Competencias y progresión longitudinal", "Instrumentos complementarios",
            "Diferencia entre muestra y ensayo",
        ):
            self.assertIn(token, status)
        page = (ROOT / "site/evaluaciones/estado-implementacion.html").read_text(encoding="utf-8")
        self.assertEqual(page.count('class="implementation-area-card"'), 8)
        self.assertIn("Qué puede usar un docente", page)
        for current_surface in (status, page, (ROOT / "README.md").read_text(encoding="utf-8")):
            self.assertNotIn("Prompt Maestro", current_surface)
            self.assertNotIn("prompt maestro", current_surface)

    def test_every_instrument_has_its_own_substantive_markdown_guide(self):
        index = (ROOT / "docs/evaluaciones/README.md").read_text(encoding="utf-8")
        guides = sorted((ROOT / "docs/evaluaciones").glob("*.md"))
        self.assertEqual(len(guides), len(INSTRUMENTS) + 1)
        for key, instrument in INSTRUMENTS.items():
            guide = ROOT / "docs/evaluaciones" / f"{key}.md"
            self.assertTrue(guide.is_file(), key)
            content = guide.read_text(encoding="utf-8")
            self.assertGreater(len(content), 5000, key)
            for token in (
                "## En una mirada", "## Qué es", "## Por qué existe",
                "## Historia y versiones anteriores", "## Cómo funciona y qué observa",
                "## Qué significan los resultados", "## Uso pedagógico antes, durante y después",
                "## Matriz de cobertura disponible", "## Rutas longitudinales hacia clases existentes",
                "## Muestras calculables de este instrumento", "## Fuentes institucionales",
            ):
                self.assertIn(token, content, guide)
            self.assertNotIn("../ENSAYOS_EJEMPLO.md", content, guide)
            self.assertIn(f"]({key}.md)", index)

    def test_general_markdown_files_are_indexes_not_concatenated_instruments(self):
        for relative in ("docs/EVALUACIONES_COMPLEMENTARIAS.md", "docs/ENSAYOS_EJEMPLO.md"):
            content = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn("índice", content.lower(), relative)
            for instrument in INSTRUMENTS.values():
                self.assertNotIn(f"## {instrument['short_name']}", content, relative)
        for key in INSTRUMENTS:
            guide = (ROOT / "docs/evaluaciones" / f"{key}.md").read_text(encoding="utf-8")
            if any(variant["instrument"] == key for variant in VARIANTS):
                self.assertIn("### Muestra ·", guide, key)

    def test_short_samples_are_not_presented_as_complete_exams(self):
        markdown = (ROOT / "docs/ENSAYOS_EJEMPLO.md").read_text(encoding="utf-8")
        page = (ROOT / "site/evaluaciones/ensayos.html").read_text(encoding="utf-8")
        for content in (markdown, page):
            self.assertIn("no ensayos completos", content.lower())
            self.assertIn("cobertura parcial", content.lower())
        self.assertNotIn("Ensayos originales de ejemplo", page)

    def test_all_level_pages_link_the_evaluation_center(self):
        pages = sorted((ROOT / "site/levels").glob("*.html"))
        self.assertEqual(len(pages), 12)
        for page in pages:
            content = page.read_text(encoding="utf-8")
            self.assertIn("Evaluaciones complementarias", content, page)
            self.assertIn('../evaluaciones/index.html', content, page)

    def test_markdown_surfaces_explain_gaps_and_do_not_link_internal_html(self):
        for relative in (
            "docs/EVALUACIONES_COMPLEMENTARIAS.md",
            "docs/ENSAYOS_EJEMPLO.md",
            "docs/INFORME_BRECHAS_ACTUAL.md",
            "docs/ESTADO_IMPLEMENTACION.md",
            "docs/evaluaciones/README.md",
        ):
            content = (ROOT / relative).read_text(encoding="utf-8")
            self.assertNotIn("](/evaluaciones/", content, relative)
            self.assertNotIn("](.html", content, relative)
        current = (ROOT / "docs/INFORME_BRECHAS_ACTUAL.md").read_text(encoding="utf-8")
        self.assertIn("no reemplaza", current)
        self.assertIn("Otros instrumentos", current)


if __name__ == "__main__":
    unittest.main()

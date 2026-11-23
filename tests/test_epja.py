"""Pruebas de la arquitectura de la Fase C (Educación de Personas Jóvenes y Adultas)."""
import json
import re
import unittest
from pathlib import Path

from scripts import grade_epja_lessons as epja

ROOT = Path(__file__).resolve().parents[1]
CODE = re.compile(r"^EPJA-[A-Z]{4}-(NB1|NB2|NM1|NM2|NM1y2)-OAD-(0[1-9]|1[0-6])$")
CATALOG = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
SNAPSHOT = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
CHILD_WORDS = re.compile(r"\b(niñ[oa]s?|chiquit[oa]s?|tía|tío|alumnit[oa]s?|chiquill[oa]s?)\b", re.I)


class EpjaSourceTests(unittest.TestCase):
    def test_source_has_official_provenance(self):
        data = json.loads(epja.SOURCE_PATH.read_text(encoding="utf-8"))
        self.assertIn("rights_notice", data)
        for key, program in data["programas"].items():
            epja.split_key(key)
            self.assertTrue(program["pagina"].startswith("https://www.curriculumnacional.cl/"), key)
            self.assertEqual(len(program["modulos"]), 4, key)

    def test_codes_follow_the_documented_format(self):
        self.assertTrue(epja.ENTRIES)
        for code, entry in epja.ENTRIES.items():
            self.assertRegex(code, CODE)
            module, performance = entry["module"]["modulo"], entry["performance"]["num"]
            self.assertTrue(code.endswith(f"-OAD-{(module - 1) * 4 + performance:02d}"), code)
        self.assertEqual(epja.objective_code("LECO_NB1", 2, 3), "EPJA-LECO-NB1-OAD-07")
        self.assertEqual(epja.objective_code("AVIS_NM1y2", 4, 4), "EPJA-AVIS-NM1y2-OAD-16")
        with self.assertRaises(ValueError):
            epja.objective_code("LECO_NB1", 1, 5)
        with self.assertRaises(ValueError):
            epja.split_key("LECO_XX9")

    def test_classes_per_objective_are_the_official_hours(self):
        for key, program in epja.PROGRAMS.items():
            entries = [e for e in epja.ENTRIES.values() if e["key"] == key]
            self.assertEqual(len(entries), 16, key)
            for entry in entries:
                code = epja.objective_code(key, entry["module"]["modulo"], entry["performance"]["num"])
                self.assertEqual(epja.class_count(code), entry["performance"]["horas"], code)
                self.assertGreaterEqual(epja.class_count(code), 2)
                self.assertLessEqual(epja.class_count(code), 9)
        self.assertIsNone(epja.class_count("MA01 OA 01"))
        if "MATE_NB1" in epja.PROGRAMS:
            self.assertEqual(sum(e["count"] for e in epja.ENTRIES.values() if e["key"] == "MATE_NB1"), 120)
        if "LECO_NB1" in epja.PROGRAMS:  # el programa asigna 28 de las 30 horas del módulo 3 a sus desempeños
            self.assertEqual(sum(e["count"] for e in epja.ENTRIES.values() if e["key"] == "LECO_NB1"), 118)

    def test_description_uses_only_source_texts(self):
        for code, entry in epja.ENTRIES.items():
            text = epja.objective_description(entry["key"], entry["module"], entry["performance"])
            self.assertTrue(text.startswith(entry["performance"]["frase"].strip()[:30]), code)
            self.assertIn(f"Horas pedagógicas: {entry['performance']['horas']}.", text)
            for number in entry["performance"]["oa"]:
                if str(number) in entry["program"]["oa_texto"]:
                    self.assertIn(f"OA {number}: ", text)

    def test_topics_are_infinitive_titles(self):
        self.assertEqual(epja._topic("Identifican el tema e idea principal de un cuento."), "Identificar el tema e idea principal de un cuento")
        self.assertEqual(epja._topic("Leen fluidamente una creación colaborativa."), "Leer fluidamente una creación colaborativa")
        self.assertEqual(epja._topic("Describir una fotografía por medio de una oración simple."), "Describir una fotografía")
        self.assertLessEqual(max(len(e["topic"]) for e in epja.ENTRIES.values()), 120)
        topics = [e["topic"].lower() for e in epja.ENTRIES.values() if e["key"] == "LECO_NB1"]
        self.assertEqual(len(topics), len(set(topics)), "los títulos de un mismo programa no deben repetirse")

    def test_subject_slugs_do_not_collide_with_regular_school(self):
        regular = {r["subject_slug"] for r in SNAPSHOT["records"] if r["course_order"] not in epja.EPJA_ORDERS}
        for key in epja.PROGRAMS:
            self.assertNotIn(epja.subject_slug(key), regular)
        self.assertEqual(epja.subject_slug("LECO_NB1"), "lenguaje-comunicacion-epja-nb1")


class EpjaPublishedTests(unittest.TestCase):
    def published_records(self):
        return [r for r in SNAPSHOT["records"] if r["course_order"] in epja.EPJA_ORDERS]

    def test_no_empty_courses_and_expected_names(self):
        for record in self.published_records():
            self.assertTrue(record["objectives"])
            self.assertEqual(record["course"], epja.COURSES[record["course_slug"]][1])
            self.assertEqual(record["course_order"], epja.COURSES[record["course_slug"]][0])
            self.assertEqual(record["coverage"], "formacion-epja")
        self.assertEqual({v[0] for v in epja.COURSES.values()}, {17, 18, 19, 20})

    def test_media_shared_subjects_use_the_same_codes_in_both_courses(self):
        by_subject = {}
        for record in self.published_records():
            by_subject.setdefault(record["subject_slug"], []).append(record)
        for slug, records in by_subject.items():
            if len(records) == 2:
                self.assertEqual({r["course_slug"] for r in records}, {"epja-media-n1", "epja-media-n2"}, slug)
                self.assertEqual([o["code"] for o in records[0]["objectives"]], [o["code"] for o in records[1]["objectives"]], slug)

    def test_catalog_counts_match_hours(self):
        per_code = {}
        for item in CATALOG["classes"]:
            if item["course_order"] >= 17:
                per_code.setdefault((item["course_slug"], item["oa_code"]), []).append(item)
        for record in self.published_records():
            for objective in record["objectives"]:
                rows = per_code.get((record["course_slug"], objective["code"]), [])
                self.assertEqual(len(rows), epja.class_count(objective["code"]), objective["code"])
                self.assertEqual({r["lesson_count"] for r in rows}, {len(rows)})
                self.assertTrue(all(r["editorial_status"] == "desarrollada" and r["coverage"] == "formacion-epja" for r in rows))

    def test_sequences_have_adult_tone_and_one_lesson_per_hour(self):
        for code in epja.RECORDS:
            sequence = epja.build_sequence(code)
            self.assertEqual(len(sequence["lessons"]), epja.class_count(code), code)
            titles = [lesson["title"] for lesson in sequence["lessons"]]
            self.assertEqual(len(titles), len(set(titles)), code)
            text = json.dumps(sequence, ensure_ascii=False)
            self.assertNotRegex(text, CHILD_WORDS, code)
            self.assertTrue(sequence["official_alignment"]["source"].startswith("https://www.curriculumnacional.cl/"))
            self.assertGreaterEqual(len(sequence["official_alignment"]["indicators"]), 3)
            for lesson in sequence["lessons"]:
                self.assertGreaterEqual(len(lesson["criteria"]), 3)

    def test_classes_without_notebook_are_listed_as_pending(self):
        from scripts import student_lessons as sl
        sl.load_all()
        pending = [(i["oa_code"], i["lesson"]) for i in CATALOG["classes"] if i["course_order"] >= 17 and (i["oa_code"], i["lesson"]) not in sl.REGISTRY]
        if pending:
            sample = pending[0]
            path = ROOT / next(i["path"] for i in CATALOG["classes"] if (i["oa_code"], i["lesson"]) == sample).split("#")[0]
            self.assertIn("pendiente", path.read_text(encoding="utf-8").lower())

    def test_guides_exist_for_each_published_subject(self):
        slugs = {r["subject_slug"] for r in self.published_records()}
        for slug in slugs:
            self.assertTrue((ROOT / "docs/formacion-epja" / f"{slug}.md").is_file(), slug)
        self.assertTrue((ROOT / "docs/formacion-epja/README.md").is_file() or not slugs)


if __name__ == "__main__":
    unittest.main()

import importlib
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import generate_dictionaries as gd  # noqa: E402


class DictionaryTests(unittest.TestCase):
    def levels(self):
        return [c for c in gd.LEVELS if (ROOT / "scripts" / f"dict_data_es_{c}.py").exists()]

    def test_every_spanish_level_has_english_and_both_are_published(self):
        for code in self.levels():
            self.assertTrue((ROOT / "scripts" / f"dict_data_en_{code}.py").exists(), code)
            slug = gd.LEVELS[code][0]
            for name in ("espanol.md", "ingles.md"):
                self.assertTrue((ROOT / "docs" / "diccionarios" / slug / name).exists(), f"{slug}/{name}")

    def test_all_twelve_levels_exist_and_vocabulary_grows_cumulatively(self):
        self.assertEqual(self.levels(), list(gd.LEVELS))
        cumulative = 0
        for code in self.levels():
            es = importlib.import_module(f"dict_data_es_{code}")
            total = len(gd.rows(es.PALABRAS, gd.ES_WORD_FIELDS, "")) + len(gd.rows(es.VERBOS, gd.ES_VERB_FIELDS, ""))
            self.assertGreater(total, 300, code)
            cumulative += total
        self.assertGreater(cumulative, 7000)

    def test_data_is_well_formed_without_repeats_across_levels(self):
        seen = set()
        for code in self.levels():
            es = importlib.import_module(f"dict_data_es_{code}")
            en = importlib.import_module(f"dict_data_en_{code}")
            gd.spanish(es, code)
            gd.english(en, code)
            for row in gd.rows(es.PALABRAS, gd.ES_WORD_FIELDS, ""):
                key = ("es", row[0].lower(), row[2])
                self.assertNotIn(key, seen, key)
                seen.add(key)
            for row in gd.rows(en.PALABRAS, gd.EN_WORD_FIELDS, ""):
                key = ("en", row[0].lower(), row[1])
                self.assertNotIn(key, seen, key)
                seen.add(key)

    def test_published_files_match_the_data(self):
        for code in self.levels():
            slug = gd.LEVELS[code][0]
            es = importlib.import_module(f"dict_data_es_{code}")
            en = importlib.import_module(f"dict_data_en_{code}")
            published_es = (ROOT / "docs" / "diccionarios" / slug / "espanol.md").read_text(encoding="utf-8")
            published_en = (ROOT / "docs" / "diccionarios" / slug / "ingles.md").read_text(encoding="utf-8")
            self.assertEqual(published_es, gd.spanish(es, code))
            self.assertEqual(published_en, gd.english(en, code))

    def test_main_readme_links_the_dictionaries(self):
        self.assertIn("docs/diccionarios/README.md", (ROOT / "README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()

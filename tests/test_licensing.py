import json
import unittest

from scripts.validate_licensing import ROOT, REQUIRED_FILES, SOURCE_REQUIRED, validate


class LicensingProgramTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.policy = json.loads((ROOT / "config/licensing-policy.json").read_text(encoding="utf-8"))
        cls.catalog = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
        cls.sources = json.loads((ROOT / "examples/source-registry.example.json").read_text(encoding="utf-8"))["sources"]

    def test_full_validator(self):
        self.assertEqual(validate(), [])

    def test_required_files(self):
        for relative in REQUIRED_FILES:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_policy_defaults(self):
        self.assertEqual(self.policy["software"], "MIT")
        self.assertEqual(self.policy["educational_content"], "CC-BY-NC-SA-4.0")
        self.assertEqual(self.policy["unknown_external_content"], "QUARANTINE")

    def test_license_separation(self):
        self.assertIn("MIT License", (ROOT / "LICENSE").read_text(encoding="utf-8"))
        self.assertIn("CC BY-NC-SA 4.0", (ROOT / "LICENSE-CONTENT.md").read_text(encoding="utf-8"))

    def test_source_records_are_complete(self):
        for record in self.sources:
            self.assertFalse(SOURCE_REQUIRED - record.keys(), record["id"])

    def test_unknown_is_not_redistributed(self):
        unknown = [record for record in self.sources if record["license"] == "UNKNOWN"]
        self.assertTrue(unknown)
        self.assertTrue(all(not record["redistributed"] for record in unknown))

    def test_curriculum_counts(self):
        self.assertEqual(self.catalog["class_count"], 192)
        self.assertEqual(self.catalog["subjects"], 16)
        self.assertEqual(self.catalog["levels"], 4)
        self.assertEqual(len(self.catalog["classes"]), 192)

    def test_every_class_has_topic_subject_and_level(self):
        for item in self.catalog["classes"]:
            self.assertTrue(item["topic"])
            self.assertTrue(item["subject"])
            self.assertIn(item["level"], (1, 2, 3, 4))

    def test_class_ids_are_consecutive(self):
        self.assertEqual([item["id"] for item in self.catalog["classes"]], list(range(1, 193)))

    def test_every_class_page_exists(self):
        for item in self.catalog["classes"]:
            self.assertTrue((ROOT / item["path"]).is_file(), item["path"])

    def test_four_levels_have_equal_depth(self):
        counts = {level: 0 for level in range(1, 5)}
        for item in self.catalog["classes"]:
            counts[item["level"]] += 1
        self.assertEqual(counts, {1: 48, 2: 48, 3: 48, 4: 48})

    def test_sixteen_subjects_have_equal_depth(self):
        counts = {}
        for item in self.catalog["classes"]:
            counts[item["subject"]] = counts.get(item["subject"], 0) + 1
        self.assertEqual(len(counts), 16)
        self.assertEqual(set(counts.values()), {12})


if __name__ == "__main__":
    unittest.main()

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


if __name__ == "__main__":
    unittest.main()

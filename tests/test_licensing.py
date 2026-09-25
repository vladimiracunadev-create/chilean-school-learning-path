from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import validate_licensing


class LicensingValidationTests(unittest.TestCase):
    def test_repository_licensing_is_coherent(self) -> None:
        self.assertEqual([], validate_licensing.validate())

    def test_stale_data_license_alias_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            stale = root / ("DATA" + "_LICENSES.md")
            stale.write_text("obsolete", encoding="utf-8")
            errors: list[str] = []
            validate_licensing.validate_canonical_data_license(root, errors)
            self.assertTrue(any("Alias legal obsoleto" in error for error in errors))

    def test_catalog_without_rights_notice_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "site/classes/course/subject").mkdir(parents=True)
            (root / "curriculum/course/subject").mkdir(parents=True)
            (root / "curriculum/catalog.json").write_text("{}", encoding="utf-8")
            (root / "site/catalog.json").write_text(json.dumps({"rights_notice": "ok"}), encoding="utf-8")
            (root / "curriculum/course/subject/oa.md").write_text("no quedan cubiertos por la licencia", encoding="utf-8")
            (root / "site/classes/course/subject/oa.html").write_text(
                "No se relicencian bajo CC BY-NC-SA 4.0; texto oficial MINEDUC: derechos de su titular",
                encoding="utf-8",
            )
            errors: list[str] = []
            validate_licensing.validate_generated_outputs(root, errors)
            self.assertIn("curriculum/catalog.json sin rights_notice heredado de la fuente", errors)


if __name__ == "__main__":
    unittest.main()

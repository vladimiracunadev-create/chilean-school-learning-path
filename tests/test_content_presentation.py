import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_content_presentation import validate, validate_html, validate_markdown  # noqa: E402


class ContentPresentationTests(unittest.TestCase):
    def test_repository_markdown_and_html_follow_the_same_contract(self):
        errors, counts = validate(ROOT)
        self.assertGreaterEqual(counts["markdown"], 3_000)
        self.assertGreater(counts["html"], 2_800)
        self.assertEqual([], errors)

    def test_markdown_to_internal_html_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            markdown = root / "README.md"
            markdown.write_text("# Título\n\n[Incorrecto](pagina.html)\n", encoding="utf-8")
            self.assertTrue(any("Markdown no debe enlazar HTML" in error for error in validate_markdown(markdown, root)))

    def test_html_to_internal_markdown_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            html = root / "index.html"
            html.write_text('<a href="README.md">Incorrecto</a>\n', encoding="utf-8")
            self.assertTrue(any("HTML no debe enlazar Markdown" in error for error in validate_html(html, root)))


if __name__ == "__main__":
    unittest.main()

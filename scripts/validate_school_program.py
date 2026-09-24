"""Validate the generated Chilean school program and its Pages artifact."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "curriculum/catalog.json"
REQUIRED_CLASS_FIELDS = {
    "id", "class_code", "lesson", "lesson_count", "phase", "topic", "course",
    "course_slug", "course_order", "subject", "subject_slug", "axis", "oa_code",
    "oa_text", "coverage", "source_url", "editorial_status", "publication_status",
    "path", "web_path",
}


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        catalog = json.loads((root / "curriculum/catalog.json").read_text(encoding="utf-8"))
        snapshot = json.loads((root / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"No se pudo cargar la fuente de verdad: {exc}"]

    classes = catalog.get("classes", [])
    objective_count = sum(len(record.get("objectives", [])) for record in snapshot.get("records", []))
    expected = {"schema_version": 4, "class_count": len(classes), "objective_count": objective_count, "course_count": 12}
    for key, value in expected.items():
        if catalog.get(key) != value:
            errors.append(f"{key}: catálogo={catalog.get(key)!r}, esperado={value!r}")
    if [item.get("id") for item in classes] != list(range(1, len(classes) + 1)):
        errors.append("Los ids de clase no son consecutivos")
    codes = [item.get("class_code") for item in classes]
    if len(codes) != len(set(codes)):
        errors.append("Hay códigos de clase duplicados")
    if catalog.get("editorial_counts") != {"inventariada": len(classes), "secuenciada": len(classes), "desarrollada": 0, "revisada": 0, "publicada": len(classes)}:
        errors.append("Los estados editoriales no coinciden con la cobertura declarada")

    markdown_cache: dict[str, str] = {}
    html_cache: dict[str, str] = {}
    for item in classes:
        missing = REQUIRED_CLASS_FIELDS - item.keys()
        if missing:
            errors.append(f"Clase {item.get('id', '?')} sin campos: {', '.join(sorted(missing))}")
            continue
        if not 4 <= item["lesson_count"] <= 7 or not 1 <= item["lesson"] <= item["lesson_count"]:
            errors.append(f"Dosificación inválida en {item['class_code']}")
        markdown_path, markdown_anchor = item["path"].split("#", 1)
        if markdown_path not in markdown_cache:
            path = root / markdown_path
            markdown_cache[markdown_path] = path.read_text(encoding="utf-8") if path.is_file() else ""
            if not markdown_cache[markdown_path]:
                errors.append(f"Falta Markdown {markdown_path}")
        if markdown_anchor not in markdown_cache[markdown_path]:
            errors.append(f"Falta ancla {markdown_anchor} en {markdown_path}")
        web_path, web_anchor = item["web_path"].split("#", 1)
        if web_path not in html_cache:
            path = root / "site" / web_path
            html_cache[web_path] = path.read_text(encoding="utf-8") if path.is_file() else ""
            if not html_cache[web_path]:
                errors.append(f"Falta página HTML {web_path}")
            for token in ('<html lang="es">', "<title>", "<h1>", "canonical", "breadcrumbs"):
                if html_cache[web_path] and token not in html_cache[web_path]:
                    errors.append(f"{web_path} no contiene {token}")
        if f'id="{web_anchor}"' not in html_cache[web_path]:
            errors.append(f"Falta ancla web {web_anchor} en {web_path}")

    pages = list((root / "site/classes").rglob("*.html"))
    if len(pages) != objective_count:
        errors.append(f"Páginas de OA: {len(pages)}, esperadas: {objective_count}")
    for required in ("index.html", "styles.css", "app.js", "catalog.json", "404.html", "icon.svg", "manifest.webmanifest", "sitemap.xml"):
        if not (root / "site" / required).is_file():
            errors.append(f"Falta artefacto de Pages: {required}")
    sitemap_path = root / "site/sitemap.xml"
    sitemap = sitemap_path.read_text(encoding="utf-8") if sitemap_path.is_file() else ""
    if sitemap.count("<url>") != objective_count + 1:
        errors.append("El sitemap no enumera portada y todas las páginas de OA")
    index_path = root / "site/index.html"
    index = index_path.read_text(encoding="utf-8") if index_path.is_file() else ""
    for token in ('lang="es"', '<main>', 'id="explorar"', 'id="q"', 'id="level"', 'id="subject"', 'id="coverage"'):
        if token not in index:
            errors.append(f"Portada incompleta: falta {token}")
    if re.search(r"\bsesiones?\b", index, flags=re.IGNORECASE):
        errors.append("La portada llama sesiones a las clases")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("VALIDACIÓN FALLIDA")
        for error in errors[:100]:
            print(" -", error)
        if len(errors) > 100:
            print(f" - … y {len(errors) - 100} errores más")
        return 1
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    print(f"OK: {catalog['class_count']} clases, {catalog['objective_count']} OA, {catalog['course_count']} niveles y {catalog['reading_link_count']} lecturas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

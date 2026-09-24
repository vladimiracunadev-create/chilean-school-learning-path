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
REQUIRED_DEVELOPED_FIELDS = {
    "title", "purpose", "goal", "opening", "model", "guided", "independent",
    "ticket", "materials", "support", "extension", "evidence", "criteria",
    "next_step", "short_version",
}


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        catalog = json.loads((root / "curriculum/catalog.json").read_text(encoding="utf-8"))
        snapshot = json.loads((root / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
        developed = json.loads((root / "content/developed-lessons.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"No se pudo cargar la fuente de verdad: {exc}"]

    classes = catalog.get("classes", [])
    objective_count = sum(len(record.get("objectives", [])) for record in snapshot.get("records", []))
    expected = {"schema_version": 5, "class_count": len(classes), "objective_count": objective_count, "course_count": 12}
    for key, value in expected.items():
        if catalog.get(key) != value:
            errors.append(f"{key}: catálogo={catalog.get(key)!r}, esperado={value!r}")
    if [item.get("id") for item in classes] != list(range(1, len(classes) + 1)):
        errors.append("Los ids de clase no son consecutivos")
    codes = [item.get("class_code") for item in classes]
    if len(codes) != len(set(codes)):
        errors.append("Hay códigos de clase duplicados")
    developed_codes = set(developed.get("objectives", {}))
    developed_count = sum(item.get("course_order") == 1 or item.get("oa_code") in developed_codes for item in classes)
    if catalog.get("editorial_counts") != {"inventariada": len(classes), "secuenciada": len(classes), "desarrollada": developed_count, "revisada": 0, "publicada": len(classes)}:
        errors.append("Los estados editoriales no coinciden con la cobertura declarada")
    for oa_code, objective in developed.get("objectives", {}).items():
        for index, lesson in enumerate(objective.get("lessons", []), 1):
            missing = REQUIRED_DEVELOPED_FIELDS - lesson.keys()
            if missing:
                errors.append(f"{oa_code}, clase {index}: faltan campos editoriales {', '.join(sorted(missing))}")
            if len(lesson.get("criteria", [])) < 3:
                errors.append(f"{oa_code}, clase {index}: requiere al menos tres criterios observables")
            for field in REQUIRED_DEVELOPED_FIELDS - {"criteria"}:
                if len(str(lesson.get(field, "")).strip()) < 20:
                    errors.append(f"{oa_code}, clase {index}: {field} no tiene desarrollo suficiente")
    first_grade = [item for item in classes if item.get("course_order") == 1]
    if len(first_grade) != 1034 or any(item.get("editorial_status") != "desarrollada" for item in first_grade):
        errors.append("1° básico no está completamente desarrollado (esperadas: 1.034 clases)")

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
        if item["editorial_status"] == "desarrollada":
            for token in ("Propósito docente", "Meta para estudiantes", "Materiales y preparación", "Criterios observables", "Decisión posterior"):
                if token not in html_cache[web_path]:
                    errors.append(f"{web_path} no materializa el contrato desarrollado: falta {token}")

    pages = list((root / "site/classes").rglob("*.html"))
    if len(pages) != objective_count:
        errors.append(f"Páginas de OA: {len(pages)}, esperadas: {objective_count}")
    for required in ("index.html", "styles.css", "app.js", "catalog.json", "404.html", "icon.svg", "manifest.webmanifest", "sitemap.xml", "levels/1-basico.html"):
        if not (root / "site" / required).is_file():
            errors.append(f"Falta artefacto de Pages: {required}")
    sitemap_path = root / "site/sitemap.xml"
    sitemap = sitemap_path.read_text(encoding="utf-8") if sitemap_path.is_file() else ""
    if sitemap.count("<url>") != objective_count + 2:
        errors.append("El sitemap no enumera portada, vista de 1° básico y todas las páginas de OA")
    level_page = root / "site/levels/1-basico.html"
    level_html = level_page.read_text(encoding="utf-8") if level_page.is_file() else ""
    for token in ("1.034", "237", "11", "100% desarrollado", "Contrato pedagógico"):
        if token not in level_html:
            errors.append(f"Vista de 1° básico incompleta: falta {token}")
    required_docs = {
        "README.md": ("12.997", "2.823", "Centro de documentación"),
        "docs/README.md": ("Qué está listo hoy", "Cómo leer los estados"),
        "docs/PRIMERO_BASICO.md": ("1.034", "Decisiones con evidencia"),
        "docs/EVALUACION_FORMATIVA.md": ("Logrado con autonomía", "Sin evidencia suficiente"),
        "TEACHING_GUIDE.md": ("Anatomía de una clase", "Consideraciones para 1° básico"),
        "METHODOLOGY.md": ("Flujo de construcción", "Estados editoriales"),
        "LEARNING_PATHS.md": ("Docente de 1° básico", "Coordinación pedagógica o UTP"),
        "ROADMAP.md": ("1.056 clases desarrolladas", "Próximo nivel de desarrollo"),
        "CONTRIBUTING.md": ("Contrato de una clase desarrollada", "Usa **clase**, no “sesión”"),
    }
    for relative_path, tokens in required_docs.items():
        document_path = root / relative_path
        document = document_path.read_text(encoding="utf-8") if document_path.is_file() else ""
        if not document:
            errors.append(f"Falta documentación: {relative_path}")
            continue
        for token in tokens:
            if token not in document:
                errors.append(f"{relative_path} incompleto: falta {token}")
    learning_paths = (root / "LEARNING_PATHS.md").read_text(encoding="utf-8")
    for legacy_term in ("Licencias de software", "SPDX/SBOM/REUSE", "data scientists"):
        if legacy_term in learning_paths:
            errors.append(f"LEARNING_PATHS.md conserva contenido heredado: {legacy_term}")
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

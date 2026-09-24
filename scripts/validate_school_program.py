"""Validate the generated Chilean school program and its Pages artifact."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    from grade_one_math_lessons import MATH_ATTITUDES, MATH_SKILLS, SEQUENCES as MATH_SEQUENCES, build_math_sequence, transversal_links
except ImportError:
    from scripts.grade_one_math_lessons import MATH_ATTITUDES, MATH_SKILLS, SEQUENCES as MATH_SEQUENCES, build_math_sequence, transversal_links

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
    official_urls = {objective["code"]: objective["url"] for record in snapshot.get("records", []) for objective in record.get("objectives", [])}
    objective_count = sum(len(record.get("objectives", [])) for record in snapshot.get("records", []))
    expected = {"schema_version": 7, "class_count": len(classes), "objective_count": objective_count, "course_count": 12}
    for key, value in expected.items():
        if catalog.get(key) != value:
            errors.append(f"{key}: catálogo={catalog.get(key)!r}, esperado={value!r}")
    if [item.get("id") for item in classes] != list(range(1, len(classes) + 1)):
        errors.append("Los ids de clase no son consecutivos")
    codes = [item.get("class_code") for item in classes]
    if len(codes) != len(set(codes)):
        errors.append("Hay códigos de clase duplicados")
    all_developed = dict(developed.get("objectives", {}))
    all_developed.update({code: build_math_sequence(code) for code in MATH_SEQUENCES})
    for index, lesson in enumerate(all_developed["MA01 OA 01"]["lessons"]):
        lesson["transversal"] = transversal_links(1, index, lesson["goal"].removeprefix("Hoy ").rstrip("."))
    developed_codes = set(all_developed)
    developed_count = sum(item.get("oa_code") in developed_codes for item in classes)
    draft_count = sum(item.get("editorial_status") == "borrador" for item in classes)
    integrated_count = sum(item.get("editorial_status") == "integrada" for item in classes)
    if catalog.get("editorial_counts") != {"inventariada": len(classes), "secuenciada": len(classes), "borrador": draft_count, "desarrollada": developed_count, "integrada": integrated_count, "revisada": 0, "publicada": len(classes)}:
        errors.append("Los estados editoriales no coinciden con la cobertura declarada")
    transversal_codes: set[str] = set()
    for oa_code, objective in all_developed.items():
        if oa_code.startswith("MA01 OA ") or oa_code == "LE01 OA 03":
            for field in ("topic", "pedagogical_explanation", "prerequisites", "vocabulary", "official_alignment"):
                if not objective.get(field):
                    errors.append(f"{oa_code}: falta fundamento específico {field}")
            alignment = objective.get("official_alignment", {})
            if len(alignment.get("indicators", [])) < 3 or not alignment.get("source", "").startswith("https://www.curriculumnacional.cl/"):
                errors.append(f"{oa_code}: alineación oficial insuficiente")
            if oa_code.startswith("MA01 OA ") and alignment.get("source") != official_urls.get(oa_code):
                errors.append(f"{oa_code}: la fuente de alineación no coincide con la ficha oficial del snapshot")
        for index, lesson in enumerate(objective.get("lessons", []), 1):
            missing = REQUIRED_DEVELOPED_FIELDS - lesson.keys()
            if missing:
                errors.append(f"{oa_code}, clase {index}: faltan campos editoriales {', '.join(sorted(missing))}")
            if len(lesson.get("criteria", [])) < 3:
                errors.append(f"{oa_code}, clase {index}: requiere al menos tres criterios observables")
            if len(str(lesson.get("title", "")).strip()) < 8:
                errors.append(f"{oa_code}, clase {index}: title no identifica la experiencia")
            for field in REQUIRED_DEVELOPED_FIELDS - {"criteria", "title"}:
                if len(str(lesson.get(field, "")).strip()) < 20:
                    errors.append(f"{oa_code}, clase {index}: {field} no tiene desarrollo suficiente")
            if oa_code.startswith("MA01 OA ") or oa_code == "LE01 OA 03":
                for field in ("home_task", "complementary", "difficulty_actions", "specialist_coordination"):
                    if not lesson.get(field):
                        errors.append(f"{oa_code}, clase {index}: falta extensión pedagógica {field}")
                if "…" in lesson.get("goal", ""):
                    errors.append(f"{oa_code}, clase {index}: la meta estudiantil está truncada")
            if oa_code.startswith("MA01 OA "):
                links = lesson.get("transversal", [])
                if len(links) != 2 or {link.get("type") for link in links} != {"Habilidad", "Actitud"}:
                    errors.append(f"{oa_code}, clase {index}: falta integración observable de habilidad y actitud")
                transversal_codes.update(link.get("code", "") for link in links)
    expected_transversal_codes = {code for code, _ in MATH_SKILLS + MATH_ATTITUDES}
    if transversal_codes != expected_transversal_codes:
        errors.append("Las 83 clases de Matemática no cubren los 16 OA transversales de habilidad y actitud")
    first_grade = [item for item in classes if item.get("course_order") == 1]
    first_grade_developed = sum(item.get("editorial_status") == "desarrollada" for item in first_grade)
    first_grade_integrated = sum(item.get("editorial_status") == "integrada" for item in first_grade)
    first_grade_drafts = sum(item.get("editorial_status") == "borrador" for item in first_grade)
    if len(first_grade) != 1034 or first_grade_developed != 93 or first_grade_integrated != 68 or first_grade_drafts != 873:
        errors.append("Estado de 1° básico incoherente (esperadas: 93 desarrolladas, 68 integradas y 873 borradores)")
    math_core = [item for item in first_grade if item.get("subject_slug") == "matematica" and item.get("editorial_status") == "desarrollada"]
    if len(math_core) != 83 or len({item.get("oa_code") for item in math_core}) != 20:
        errors.append("Matemática de 1° básico debe contener exactamente 83 clases desarrolladas en 20 OA de contenido")
    math_integrated = [item for item in first_grade if item.get("subject_slug") == "matematica" and item.get("editorial_status") == "integrada"]
    if len(math_integrated) != 68 or len({item.get("oa_code") for item in math_integrated}) != 16:
        errors.append("Matemática de 1° básico debe integrar 68 experiencias de 16 OA de habilidad/actitud")

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
            tokens = ["Propósito docente", "Meta para estudiantes", "Materiales y preparación", "Criterios observables", "Decisión posterior", "Tarea breve y flexible", "Actividades complementarias", "Control de dificultades con acciones", "Coordinación profesional"]
            if item.get("subject_slug") == "matematica" and item.get("course_order") == 1:
                tokens.append("Habilidad y actitud en esta clase")
            for token in tokens:
                if token not in html_cache[web_path]:
                    errors.append(f"{web_path} no materializa el contrato desarrollado: falta {token}")

    pages = list((root / "site/classes").rglob("*.html"))
    if len(pages) != objective_count:
        errors.append(f"Páginas de OA: {len(pages)}, esperadas: {objective_count}")
    for required in ("index.html", "documentacion.html", "styles.css", "app.js", "catalog.json", "404.html", "icon.svg", "manifest.webmanifest", "sitemap.xml", "levels/1-basico.html"):
        if not (root / "site" / required).is_file():
            errors.append(f"Falta artefacto de Pages: {required}")
    documentation_pages = list((root / "site/docs").rglob("*.html"))
    if len(documentation_pages) < 25:
        errors.append(f"Documentación HTML incompleta: {len(documentation_pages)} páginas, esperadas al menos 25")
    sitemap_path = root / "site/sitemap.xml"
    sitemap = sitemap_path.read_text(encoding="utf-8") if sitemap_path.is_file() else ""
    if sitemap.count("<url>") != objective_count + len(documentation_pages) + 3:
        errors.append("El sitemap no enumera portada, documentación, vista de 1° básico, documentos HTML y páginas de OA")
    level_page = root / "site/levels/1-basico.html"
    level_html = level_page.read_text(encoding="utf-8") if level_page.is_file() else ""
    for token in ("1.034", "237", "11", "93", "68", "873", "Contrato pedagógico"):
        if token not in level_html:
            errors.append(f"Vista de 1° básico incompleta: falta {token}")
    documentation_page = root / "site/documentacion.html"
    documentation_html = documentation_page.read_text(encoding="utf-8") if documentation_page.is_file() else ""
    for token in ("Documentación pedagógica", "10 guías marco", "11 guías completas", "¿Qué es un OA?", "Roles en el aula", "Cobertura navegable", "Markdown + HTML"):
        if token not in documentation_html:
            errors.append(f"Portada documental incompleta: falta {token}")
    required_docs = {
        "README.md": ("12.997", "2.823", "De dónde sale el contenido", "Portal, navegación y formatos", "Caja de herramientas pedagógicas", "Rutas según quién usa el repositorio", "Para docentes y equipos pedagógicos", "Calidad y CI", "Qué es y qué no es este programa", "Idea fuerza", "Documentación de principio a fin"),
        "docs/README.md": ("Estado verificable", "Cómo leer los estados"),
        "docs/PRIMERO_BASICO.md": ("1.034", "Decisiones con evidencia"),
        "docs/1-basico/README.md": ("Las 11 asignaturas", "Progresión pedagógica común"),
        "docs/SYLLABUS.md": ("Marco de reconstrucción de 1° básico", "Planificación de principio a fin"),
        "docs/RUBRICA_EVALUACION.md": ("Rúbrica transversal", "Decisiones posteriores"),
        "docs/FAQ.md": ("Preguntas frecuentes", "¿Las 1.034 clases caben en un año?"),
        "docs/GUIA_FAMILIAS.md": ("Guía para familias", "Acompañar sin reemplazar"),
        "docs/REVISION_HUMANA.md": ("Protocolo de revisión humana", "Registro de evidencia"),
        "docs/QUE_ES_UN_OA.md": ("OA significa Objetivo de Aprendizaje", "OA, clase, actividad y evidencia"),
        "docs/GLOSARIO.md": ("Glosario educativo", "Códigos rápidos"),
        "docs/ROLES_DOCENTES.md": ("Roles profesionales dentro del aula", "Antes, durante y después"),
        "docs/DIFICULTADES_EN_EL_AULA.md": ("Control de dificultades en el aula con acciones", "observar → actuar → comprobar → decidir"),
        "docs/COBERTURA.md": ("Cobertura completa y navegable", "12.997"),
        "docs/PLAN_DESARROLLO.md": ("Plan maestro de desarrollo y control profesional", "Plan por asignatura e ítem", "Controles profesionales", "MA01 OA 20", "Gates para cerrar una asignatura"),
        "docs/FORMATOS.md": ("Clases en Markdown y HTML", "12.997 clases en ambos formatos"),
        "docs/LICENCIAS.md": ("Guía simple de licencias", "Atribución sugerida"),
        "docs/EVALUACION_FORMATIVA.md": ("Logrado con autonomía", "Sin evidencia suficiente"),
        "TEACHING_GUIDE.md": ("Anatomía de una clase", "Consideraciones para 1° básico"),
        "METHODOLOGY.md": ("Flujo de construcción", "Estados editoriales"),
        "LEARNING_PATHS.md": ("Docente de 1° básico", "Coordinación pedagógica o UTP"),
        "ROADMAP.md": ("115 clases desarrolladas", "873 borradores", "Criterio para declarar un nivel completo"),
        "CONTRIBUTING.md": ("Contrato de una clase desarrollada", "Usa **clase**, no “sesión”"),
        "LICENSING.md": ("Modelo por capas", "Respuesta rápida"),
        "ASSET_LICENSES.md": ("Licencias de activos visuales", "site/icon.svg"),
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
    expected_subject_guides = {item["subject_slug"] for item in classes if item.get("course_order") == 1}
    subject_guides = {path.stem for path in (root / "docs/1-basico").glob("*.md") if path.name != "README.md"}
    if subject_guides != expected_subject_guides:
        errors.append(f"Guías de asignatura de 1° básico incompletas: actuales={len(subject_guides)}, esperadas={len(expected_subject_guides)}")
    for subject_slug in sorted(expected_subject_guides):
        guide = (root / "docs/1-basico" / f"{subject_slug}.md").read_text(encoding="utf-8")
        for token in ("Resultados de aprendizaje", "Prerrequisitos", "Cómo recorrer", "Estructura por ejes", "Recorrido OA por OA", "Error frecuente", "Acceso y profundización"):
            if token not in guide:
                errors.append(f"Guía {subject_slug} incompleta: falta {token}")
    documentation_files = list(root.glob("*.md")) + list((root / "docs").rglob("*.md"))
    for document_path in documentation_files:
        document = document_path.read_text(encoding="utf-8")
        for destination in re.findall(r"\[[^\]]+\]\(([^)]+)\)", document):
            if "vladimiracunadev-create.github.io/chilean-school-learning-path" in destination or re.search(r"(?:^|/)site/.*\.html(?:#.*)?$", destination):
                errors.append(f"Cruce Markdown→HTML en {document_path.relative_to(root)}: {destination}")
            if destination.startswith(("http://", "https://", "#", "mailto:")):
                continue
            relative_target = destination.split("#", 1)[0]
            if relative_target.endswith(".html"):
                errors.append(f"Cruce Markdown→HTML en {document_path.relative_to(root)}: {destination}")
            if relative_target and relative_target.endswith(".md") and not (document_path.parent / relative_target).is_file():
                errors.append(f"Enlace Markdown roto en {document_path.relative_to(root)}: {destination}")
    for html_path in (root / "site").rglob("*.html"):
        document = html_path.read_text(encoding="utf-8")
        for destination in re.findall(r'href="([^"]+)"', document):
            clean = destination.split("#", 1)[0].split("?", 1)[0]
            if clean.lower().endswith(".md"):
                errors.append(f"Cruce HTML→Markdown en {html_path.relative_to(root)}: {destination}")
            if not clean or clean.startswith(("http://", "https://", "mailto:", "tel:", "/")):
                continue
            if clean.lower().endswith(".html") and not (html_path.parent / clean).resolve().is_file():
                errors.append(f"Enlace HTML roto en {html_path.relative_to(root)}: {destination}")
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

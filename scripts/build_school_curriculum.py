"""Build a Chilean school curriculum from a verified MINEDUC snapshot.

Use --refresh only for a deliberate source update. Normal generation is offline and deterministic.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import unicodedata
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "sources" / "mineduc-curriculum-snapshot.json"
CURRICULUM = ROOT / "curriculum"
BASE_URL = "https://www.curriculumnacional.cl"

COURSES = [
    ("1o-6o-basico", "1-basico", "1° básico", 1),
    ("1o-6o-basico", "2-basico", "2° básico", 2),
    ("1o-6o-basico", "3-basico", "3° básico", 3),
    ("1o-6o-basico", "4-basico", "4° básico", 4),
    ("1o-6o-basico", "5-basico", "5° básico", 5),
    ("1o-6o-basico", "6-basico", "6° básico", 6),
    ("7o-basico-2o-medio", "7-basico", "7° básico", 7),
    ("7o-basico-2o-medio", "8-basico", "8° básico", 8),
    ("7o-basico-2o-medio", "1-medio", "1° medio", 9),
    ("7o-basico-2o-medio", "2-medio", "2° medio", 10),
    ("3o-4o-medio", "3-medio-fg", "3° medio · Formación General", 11),
    ("3o-4o-medio", "4-medio-fg", "4° medio · Formación General", 12),
]

SUBJECT_GUIDANCE = {
    "lenguaje": ("leer, escribir, comunicar y fundamentar", "producción o interpretación con evidencia textual"),
    "lengua": ("leer, escribir, comunicar y comprender cultura", "producción o interpretación situada"),
    "matematica": ("representar, resolver, argumentar y verificar", "solución explicada con estrategia y comprobación"),
    "ciencias": ("observar, modelar, investigar y explicar", "registro de indagación con datos y conclusión"),
    "historia": ("pensar temporal y espacialmente con fuentes", "explicación respaldada por fuentes, mapa o evidencia"),
    "ingles": ("comprender e interactuar con propósito comunicativo", "desempeño oral o escrito comprensible"),
    "artes": ("crear, apreciar, experimentar y comunicar decisiones", "obra o proceso con bitácora y reflexión"),
    "musica": ("escuchar, interpretar, crear y reflexionar", "interpretación o creación con criterios audibles"),
    "fisica": ("desarrollar habilidades motrices y hábitos saludables", "desempeño seguro con autoevaluación"),
    "tecnologia": ("diseñar, crear, probar y mejorar soluciones", "prototipo con criterios, prueba e iteración"),
    "orientacion": ("reconocerse, convivir y tomar decisiones responsables", "reflexión o acuerdo aplicable y respetuoso"),
    "filosofia": ("formular problemas, argumentar y examinar supuestos", "argumento con objeción y respuesta"),
    "ciudadana": ("deliberar, participar y evaluar evidencia pública", "posición fundamentada y propuesta cívica"),
}


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def strip_html(value: str) -> str:
    value = re.sub(r"<br\s*/?>", " ", value, flags=re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "ChileanSchoolCurriculumProgram/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def coverage_for(slug: str) -> str:
    if "religion" in slug:
        return "electiva-segun-establecimiento-y-familia"
    if "ingles-propuesta" in slug:
        return "propuesta-mineduc"
    if "pueblos-originarios" in slug or "lengua-indigena" in slug:
        return "segun-contexto-y-normativa"
    return "formacion-comun"


def subject_guidance(slug: str) -> tuple[str, str]:
    for key, guidance in SUBJECT_GUIDANCE.items():
        if key in slug:
            return guidance
    return "comprender, aplicar, comunicar y revisar", "desempeño observable alineado al objetivo"


def extract_subjects(course_html: str, base: str, course_slug: str) -> list[dict[str, str]]:
    pattern = re.compile(r'href="(/curriculum/' + re.escape(base) + r'/([^/]+)/' + re.escape(course_slug) + r')"[^>]*>(.*?)</a>', re.S | re.I)
    subjects: dict[str, dict[str, str]] = {}
    for path, slug, label in pattern.findall(course_html):
        if slug == "curso":
            continue
        subjects[slug] = {"slug": slug, "name": strip_html(label), "url": BASE_URL + path, "coverage": coverage_for(slug)}
    return sorted(subjects.values(), key=lambda item: item["name"])


def extract_objectives(subject_html: str, subject_url: str) -> list[dict[str, object]]:
    axes = []
    for match in re.finditer(r'<h3[^>]*class="[^"]*link[^"]*"[^>]*>(.*?)</h3>', subject_html, re.S | re.I):
        axes.append((match.start(), strip_html(match.group(1))))
    objectives = []
    pattern = re.compile(
        r'<div class="item-wrapper(?P<classes>[^"]*)">(?P<body>.*?)(?=<div class="item-wrapper|</div>\s*</div>\s*</div>\s*<div class="sidebar|$)',
        re.S | re.I,
    )
    for match in pattern.finditer(subject_html):
        body = match.group("body")
        code_match = re.search(r'<span class="oa-title">Objetivo de aprendizaje\s+([^<]+)</span>', body, re.I)
        link_match = re.search(r'<a href="([^"]+)" class="link-more">', body, re.I)
        desc_match = re.search(r'field--name-description.*?field__item">(.*?)(?:<a href=|$)', body, re.S | re.I)
        if not code_match or not desc_match:
            continue
        code = strip_html(code_match.group(1))
        description = strip_html(desc_match.group(1))
        if not description:
            continue
        axis = "Objetivos de aprendizaje"
        for position, candidate in axes:
            if position < match.start():
                axis = candidate
            else:
                break
        relative = link_match.group(1) if link_match else ""
        objectives.append({
            "code": code,
            "description": description,
            "axis": axis,
            "prioritized": "prioritized" in match.group("classes"),
            "url": BASE_URL + relative if relative.startswith("/") else (relative or subject_url),
        })
    unique = {}
    for objective in objectives:
        unique[objective["code"]] = objective
    return list(unique.values())


def refresh_snapshot() -> dict[str, object]:
    records = []
    for base, course_slug, course_name, order in COURSES:
        course_url = f"{BASE_URL}/curriculum/{base}/curso/{course_slug}"
        course_html = fetch(course_url)
        for subject in extract_subjects(course_html, base, course_slug):
            subject_html = fetch(subject["url"])
            objectives = extract_objectives(subject_html, subject["url"])
            if not objectives:
                continue
            approach, evidence = subject_guidance(subject["slug"])
            records.append({
                "course": course_name,
                "course_slug": course_slug,
                "course_order": order,
                "course_url": course_url,
                "subject": subject["name"],
                "subject_slug": subject["slug"],
                "subject_url": subject["url"],
                "coverage": subject["coverage"],
                "approach": approach,
                "evidence": evidence,
                "objectives": objectives,
            })
            print(f"{course_name}: {subject['name']} — {len(objectives)} OA", flush=True)
    snapshot = {
        "schema_version": 2,
        "source": "Currículum Nacional · Ministerio de Educación de Chile",
        "source_url": f"{BASE_URL}/curriculum/cursos-y-niveles",
        "verified_at": date.today().isoformat(),
        "rights_notice": "Los códigos, metadatos y textos oficiales conservan los derechos de sus titulares; la licencia de contenido del proyecto solo cubre la elaboración pedagógica original.",
        "scope": "1° básico a 4° medio, formación general; coberturas optativas identificadas",
        "records": records,
    }
    SNAPSHOT.parent.mkdir(parents=True, exist_ok=True)
    SNAPSHOT.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return snapshot


def topic_from(description: str) -> str:
    clean = description.rstrip(".")
    first = re.split(r"[;:]", clean, maxsplit=1)[0]
    if len(first) > 105:
        first = first[:102].rsplit(" ", 1)[0] + "…"
    return first[0].upper() + first[1:] if first else "Objetivo de aprendizaje"


def class_page(item: dict[str, object]) -> str:
    return f"""# {item['class_code']} — {item['topic']}

| Campo | Valor |
|---|---|
| Nivel | {item['course']} |
| Asignatura | {item['subject']} |
| Eje | {item['axis']} |
| OA oficial | [{item['oa_code']}]({item['source_url']}) |
| Cobertura | `{item['coverage']}` |

## Objetivo de Aprendizaje oficial

> {item['oa_text']}

## Propósito de la clase

Que cada estudiante pueda **{item['approach']}** en relación con este OA y demostrarlo mediante
una evidencia observable. La clase desarrolla el objetivo; no reemplaza el programa oficial ni el
juicio pedagógico sobre ritmo, contexto y conocimientos previos.

## Secuencia sugerida

1. **Activación (10 min):** presenta una situación cercana y recoge respuestas sin corregir de inmediato.
2. **Modelado (15 min):** muestra cómo piensa una persona experta; nombra decisiones y errores posibles.
3. **Práctica guiada (20 min):** resuelve un ejemplo con participación, preguntas y retroalimentación breve.
4. **Práctica autónoma (25 min):** cada estudiante produce una respuesta, solución o desempeño propio.
5. **Cierre (10 min):** compara estrategias, vuelve al OA y registra qué necesita retomarse.

## Evidencia de aprendizaje

Producto esperado: **{item['evidence']}**. Debe permitir distinguir entre “participó”, “completó la
tarea” y “demostró el aprendizaje descrito por el OA”.

### Criterios

- responde al verbo y contenido central del OA;
- hace visible el procedimiento, interpretación o decisión del estudiante;
- usa lenguaje, representación o desempeño apropiado para {item['course']};
- permite retroalimentar un siguiente paso concreto.

## Inclusión y contexto

Ofrece más de una forma de acceso y respuesta sin reducir la demanda cognitiva. Anticipa vocabulario,
fragmenta instrucciones, usa apoyos visuales o manipulativos cuando ayuden y admite expresión oral,
escrita, gráfica o corporal cuando sea coherente con la asignatura. No diagnostiques a partir de una
sola actividad.

## Textos y lecturas

Consulta el [catálogo oficial de Textos Escolares 2026](https://www.curriculumnacional.cl/noticias/ministerio-educacion-pone-disposicion-catalogo-textos-escolares-2026)
y los recursos enlazados en la ficha oficial del OA. Las lecturas del portal MINEDUC se presentan
como **sugeridas**; el establecimiento puede definir un plan lector propio. No se reproducen obras
protegidas en este repositorio.

## Fuente y trazabilidad

- [Ficha oficial del OA]({item['source_url']})
- [Página oficial de la asignatura y nivel]({item['subject_url']})
- Snapshot verificado: `{item['verified_at']}`
- [Volver al currículo](../../../../CURRICULUM.md)
"""


def build(snapshot: dict[str, object]) -> dict[str, object]:
    records = snapshot["records"]
    classes = []
    class_number = 1
    for record in sorted(records, key=lambda value: (value["course_order"], value["subject"], value["subject_slug"])):
        for objective in record["objectives"]:
            topic = topic_from(objective["description"])
            class_code = f"CL-{class_number:04d}"
            path = f"curriculum/{record['course_slug']}/{record['subject_slug']}/{slugify(objective['code'])}.md"
            classes.append({
                "id": class_number,
                "class_code": class_code,
                "topic": topic,
                "course": record["course"],
                "course_slug": record["course_slug"],
                "course_order": record["course_order"],
                "subject": record["subject"],
                "subject_slug": record["subject_slug"],
                "axis": objective["axis"],
                "oa_code": objective["code"],
                "oa_text": objective["description"],
                "prioritized": objective["prioritized"],
                "coverage": record["coverage"],
                "approach": record["approach"],
                "evidence": record["evidence"],
                "source_url": objective["url"],
                "subject_url": record["subject_url"],
                "verified_at": snapshot["verified_at"],
                "path": path,
            })
            class_number += 1

    for path in CURRICULUM.glob("level-*"):
        if path.is_dir():
            shutil.rmtree(path)
    for path in CURRICULUM.iterdir() if CURRICULUM.exists() else []:
        if path.is_dir() and path.name not in {item["course_slug"] for item in classes}:
            shutil.rmtree(path)

    catalog = {
        "schema_version": 2,
        "verified_at": snapshot["verified_at"],
        "source_url": snapshot["source_url"],
        "rights_notice": snapshot["rights_notice"],
        "class_count": len(classes),
        "course_count": len({item["course"] for item in classes}),
        "subject_count": len({item["subject"] for item in classes}),
        "classes": classes,
    }
    CURRICULUM.mkdir(exist_ok=True)
    (CURRICULUM / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for item in classes:
        target = ROOT / item["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(class_page(item), encoding="utf-8")
    (ROOT / "CURRICULUM.md").write_text(curriculum_index(catalog), encoding="utf-8")
    (ROOT / "site" / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False) + "\n", encoding="utf-8")
    return catalog


def curriculum_index(catalog: dict[str, object]) -> str:
    classes = catalog["classes"]
    lines = [
        "# Malla curricular chilena", "",
        f"## {catalog['class_count']} clases · {catalog['course_count']} niveles · {catalog['subject_count']} asignaturas", "",
        "Cada clase corresponde a un tema, una asignatura, un nivel y un Objetivo de Aprendizaje",
        "oficial. La cobertura se deriva del snapshot MINEDUC y conserva el enlace a la ficha fuente.", "",
        "> Textos Escolares y lecturas apoyan la enseñanza, pero no son equivalentes a los OA. Las",
        "> lecturas del portal se denominan sugeridas y se enlazan sin reproducir obras protegidas.", "",
    ]
    for course_order in range(1, 13):
        current = [item for item in classes if item["course_order"] == course_order]
        if not current:
            continue
        lines.extend([f"## {current[0]['course']}", "", "| Clase | Asignatura | Eje | OA | Tema |", "|---:|---|---|---|---|"])
        for item in current:
            lines.append(f"| [{item['class_code']}]({item['path']}) | {item['subject']} | {item['axis']} | [{item['oa_code']}]({item['source_url']}) | {item['topic']} |")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true", help="fetch a new official MINEDUC snapshot")
    args = parser.parse_args()
    if args.refresh:
        snapshot = refresh_snapshot()
    else:
        snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    catalog = build(snapshot)
    print(f"Generated {catalog['class_count']} classes across {catalog['course_count']} levels and {catalog['subject_count']} subjects.")


if __name__ == "__main__":
    main()


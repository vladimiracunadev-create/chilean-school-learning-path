"""Validate the student-facing lesson layer and write the real exercise-coverage panel.

Run `python scripts/validate_student_lessons.py` to check, and `--write` to refresh
docs/COBERTURA_ESTUDIANTE.md. Automatic validation is reported separately from
professional review: nothing here states that a human specialist reviewed a lesson.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import student_lessons as sl  # noqa: E402

REPORT = ROOT / "docs" / "COBERTURA_ESTUDIANTE.md"
MAX_TEMPLATE_SHARE = 0.5
LESSON_HEADING = re.compile(r"^### Clase (\d+) de (\d+):", re.M)
LEVEL_NAMES = {
    "1-basico": "1.º básico", "2-basico": "2.º básico", "3-basico": "3.º básico", "4-basico": "4.º básico",
    "5-basico": "5.º básico", "6-basico": "6.º básico", "7-basico": "7.º básico", "8-basico": "8.º básico",
    "1-medio": "1.º medio", "2-medio": "2.º medio", "3-medio-fg": "3.º medio", "4-medio-fg": "4.º medio",
}


def template(question: str) -> str:
    """Question with numbers and names flattened, so number-only variants collide."""
    flat = re.sub(r"[\d.,]+", "#", question.lower())
    flat = re.sub(r"[▮●|]+", "~", flat)
    return re.sub(r"\s+", " ", flat).strip()


def curriculum_file(oa_code: str) -> Path | None:
    slug = oa_code.lower().replace(" ", "-")
    found = sorted((ROOT / "curriculum").glob(f"*/*/{slug}.md"))
    return found[0] if found else None


def lesson_totals() -> dict[str, int]:
    """Number of lessons per OA file, keyed by relative path."""
    totals = {}
    for path in (ROOT / "curriculum").glob("*/*/*.md"):
        match = LESSON_HEADING.findall(path.read_text(encoding="utf-8"))
        if match:
            totals[path.relative_to(ROOT).as_posix()] = len(match)
    return totals


def check() -> list[str]:
    sl.load_all()
    errors: list[str] = []
    seen: dict[str, str] = {}
    for (oa_code, number), content in sorted(sl.REGISTRY.items()):
        errors += sl.problems(oa_code, number, content)
        path = curriculum_file(oa_code)
        if path is None:
            errors.append(f"{oa_code}: no existe el OA en el currículo")
            continue
        total = len(LESSON_HEADING.findall(path.read_text(encoding="utf-8")))
        if not 1 <= number <= total:
            errors.append(f"{oa_code}: la clase {number} no existe (el OA tiene {total})")
        templates = Counter(template(item["q"]) for item in sl.all_questions(content))
        top, count = templates.most_common(1)[0]
        if count / sum(templates.values()) > MAX_TEMPLATE_SHARE:
            errors.append(f"{oa_code} clase {number}: {count} ejercicios comparten la plantilla «{top[:50]}»")
        for item in sl.all_questions(content):
            key = item["q"].strip().lower()
            if key in seen and seen[key] != f"{oa_code}:{number}":
                errors.append(f"{oa_code} clase {number}: enunciado idéntico a {seen[key]}: {item['q'][:50]}")
            seen[key] = f"{oa_code}:{number}"
    return errors


def report() -> str:
    sl.load_all()
    totals = lesson_totals()
    per_level: dict[str, dict[str, int]] = {}
    for rel, count in totals.items():
        level = rel.split("/")[1]
        row = per_level.setdefault(level, {"lessons": 0, "student": 0, "exercises": 0, "worked": 0})
        row["lessons"] += count
    rows_oa = []
    by_oa: dict[str, list[tuple[int, dict]]] = {}
    for (oa_code, number), content in sl.REGISTRY.items():
        by_oa.setdefault(oa_code, []).append((number, content))
    for oa_code, lessons in sorted(by_oa.items()):
        path = curriculum_file(oa_code)
        level = path.relative_to(ROOT).parts[1]
        subject = path.relative_to(ROOT).parts[2]
        count = totals[path.relative_to(ROOT).as_posix()]
        exercises = sum(len(sl.all_questions(content)) for _n, content in lessons)
        worked = sum(len(content["worked"]) for _n, content in lessons)
        row = per_level[level]
        row["student"] += len(lessons)
        row["exercises"] += exercises
        row["worked"] += worked
        rows_oa.append((level, subject, oa_code, len(lessons), count, exercises, worked))
    total_lessons = sum(v["lessons"] for v in per_level.values())
    total_student = sum(v["student"] for v in per_level.values())
    out = [
        "# Cobertura real del material del estudiante",
        "",
        "Este panel cuenta únicamente clases que publican un **cuaderno del estudiante**: explicación disciplinar, ejemplos resueltos, ejercicios con todos sus datos, solucionario razonado y actividad abierta con criterios. La planificación docente existente se conserva, pero **no** se cuenta aquí como material de aprendizaje.",
        "",
        "Se informa por separado la **validación automática** (estructura, cantidad, verificación aritmética de las respuestas calculables, ejercicios repetidos y plantillas dominantes) y la **revisión profesional**. Ninguna clase de este panel tiene revisión disciplinar humana documentada: el estado de revisión es *pendiente*.",
        "",
        f"**Resumen:** {total_student} de {fmt_n(total_lessons)} clases y experiencias publicadas tienen cuaderno del estudiante ({f'{100 * total_student / total_lessons:.1f}'.replace('.', ',')} %).",
        "",
        "## Cobertura por nivel",
        "",
        "| Nivel | Clases con planificación | Clases con cuaderno | Ejercicios y preguntas | Ejemplos resueltos | Validación automática | Revisión profesional |",
        "|---|---:|---:|---:|---:|---|---|",
    ]
    for level in LEVEL_NAMES:
        row = per_level.get(level, {"lessons": 0, "student": 0, "exercises": 0, "worked": 0})
        auto = "aprobada" if row["student"] else "—"
        out.append(f"| {LEVEL_NAMES[level]} | {fmt_n(row['lessons'])} | {row['student']} | {row['exercises']} | {row['worked']} | {auto} | pendiente |")
    out += ["", "## Objetivos con cuaderno", "", "| Nivel | Asignatura | OA | Clases con cuaderno | Clases del OA | Ejercicios y preguntas | Ejemplos resueltos |", "|---|---|---|---:|---:|---:|---:|"]
    for level, subject, oa_code, have, count, exercises, worked in rows_oa:
        out.append(f"| {LEVEL_NAMES[level]} | {subject} | {oa_code} | {have} | {count} | {exercises} | {worked} |")
    out += [
        "",
        "## Mínimos exigidos por el validador",
        "",
        f"- Explicación de al menos {sl.MIN_EXPLAIN_WORDS} palabras, vocabulario, conocimientos previos y errores frecuentes.",
        f"- Al menos {sl.MIN_WORKED} ejemplos resueltos paso a paso.",
        f"- Al menos {sl.MIN_CLOSED} ejercicios cerrados repartidos en los {sl.MIN_TIERS} niveles (recuperación, comprensión, aplicación, razonamiento y desafío), más una situación auténtica y {sl.MIN_SELFCHECK} preguntas de autoevaluación.",
        "- Respuesta y explicación de cada ejercicio; las respuestas aritméticas se recalculan automáticamente.",
        "- Actividad abierta con ejemplo de respuesta, criterios, evidencias aceptables, errores frecuentes y retroalimentación.",
        f"- Ninguna plantilla de enunciado puede superar el {int(MAX_TEMPLATE_SHARE * 100)} % de los ejercicios de una clase, ni repetirse un enunciado idéntico entre clases.",
        "",
        "Los mínimos son un piso, no una meta: una clase no mejora por tener más ejercicios si éstos repiten la misma idea.",
        "",
    ]
    return "\n".join(out)


def fmt_n(value: int) -> str:
    return f"{value:,}".replace(",", ".")


def main(argv: list[str]) -> int:
    errors = check()
    text = report()
    if "--write" in argv:
        REPORT.write_text(text, encoding="utf-8", newline="\n")
    elif not REPORT.exists() or REPORT.read_text(encoding="utf-8") != text:
        errors.append("docs/COBERTURA_ESTUDIANTE.md no está sincronizado; ejecuta validate_student_lessons.py --write")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Material del estudiante válido: {len(sl.REGISTRY)} clases.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

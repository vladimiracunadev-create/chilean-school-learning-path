"""Reproducible baseline audit of the published lessons (structural, not disciplinary).

Measures only what a script can prove: how many lessons carry a student notebook,
how many rely on a keyword-matched generic classroom artefact, and how often the
same prompt template is reused with different numbers. It cannot judge disciplinary
accuracy; that needs a professional reviewer and is reported as pending.
"""
from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORT = ROOT / "docs" / "AUDITORIA_CONTENIDO.md"
PROMPT = re.compile(r"\*\*Recurso listo para usar:\*\* (.*)\n\n\*\*Consigna exacta:\*\* (.*)\n")
NOTEBOOK = "### Cuaderno del estudiante"
LEVELS = ["1-basico", "2-basico", "3-basico", "4-basico", "5-basico", "6-basico", "7-basico", "8-basico", "1-medio", "2-medio", "3-medio-fg", "4-medio-fg"]
NAMES = {"1-basico": "1.º básico", "2-basico": "2.º básico", "3-basico": "3.º básico", "4-basico": "4.º básico", "5-basico": "5.º básico", "6-basico": "6.º básico", "7-basico": "7.º básico", "8-basico": "8.º básico", "1-medio": "1.º medio", "2-medio": "2.º medio", "3-medio-fg": "3.º medio", "4-medio-fg": "4.º medio"}


def template(text: str) -> str:
    flat = re.sub(r"[\d.,]+", "#", text.lower())
    flat = re.sub(r"«[^»]*»", "«x»", flat)
    return re.sub(r"\s+", " ", flat).strip()


def measure() -> dict:
    stats: dict[str, dict] = defaultdict(lambda: {"lessons": 0, "notebook": 0, "generic": 0, "prompts": Counter()})
    for path in sorted((ROOT / "curriculum").glob("*/*/*.md")):
        level = path.relative_to(ROOT).parts[1]
        text = path.read_text(encoding="utf-8")
        blocks = text.split("\n### Clase ")[1:]
        for block in blocks:
            found = PROMPT.search(block)
            if not found:
                continue
            row = stats[level]
            row["lessons"] += 1
            row["notebook"] += NOTEBOOK in block
            row["generic"] += "Caso didáctico sobre" in found.group(1)
            if NOTEBOOK not in block:
                row["prompts"][template(found.group(2))] += 1
    return stats


def report() -> str:
    stats = measure()
    out = [
        "# Auditoría de contenido: línea base reproducible",
        "",
        "Esta auditoría mide lo que un programa puede comprobar. **No** juzga la exactitud disciplinar ni la pertinencia etaria de cada clase: eso requiere revisión profesional y permanece pendiente. Se regenera con `python scripts/audit_content.py --write`.",
        "",
        "## Defectos comprobados",
        "",
        "1. **La clase está escrita para quien enseña.** Antes del cuaderno del estudiante, las clases publicaban acciones docentes, criterios y pautas, pero ninguna publicaba ejemplos resueltos, un conjunto de ejercicios con todos sus datos ni un solucionario para el alumno.",
        "2. **Insumo genérico por palabras clave.** `scripts/lesson_quality_enrichment.py` elige el recurso, la consigna y la referencia con coincidencias de palabras en el título (`_math`, `_science`, `_generic`...). Una clase sobre descomponer 63 en decenas y unidades recibía «tarjetas numéricas 18, 20 y 21», que no corresponden a su OA. Para las clases con cuaderno, el insumo, la consigna y la referencia se derivan ahora del propio cuaderno y el generador por palabras clave ya no se aplica.",
        "3. **Consignas que sólo cambian números o el título.** Las consignas sin cuaderno se repiten con una plantilla por asignatura y curso; la tabla siguiente la cuantifica.",
        "",
        "## Cobertura y repetición por nivel",
        "",
        "Las columnas de plantillas consideran sólo las clases **sin** cuaderno; una plantilla aplica a números o títulos distintos pero a la misma redacción.",
        "",
        "| Nivel | Clases con consigna | Con cuaderno | Plantillas de consigna distintas | Mayor repetición de una plantilla |",
        "|---|---:|---:|---:|---:|",
    ]
    for level in LEVELS:
        row = stats[level]
        top = row["prompts"].most_common(1)[0][1] if row["prompts"] else 0
        out.append(f"| {NAMES[level]} | {row['lessons']} | {row['notebook']} | {len(row['prompts'])} | {top} |")
    total = sum(r["lessons"] for r in stats.values())
    done = sum(r["notebook"] for r in stats.values())
    out += [
        "",
        f"**Total:** {total} clases con consigna exacta; {done} con cuaderno del estudiante.",
        "",
        "## Qué se corrige y en qué orden",
        "",
        "- Se trabaja por lotes verificables: cada lote reemplaza el insumo genérico por un cuaderno específico del OA y lo valida (`scripts/validate_student_lessons.py`).",
        "- Las clases que aún no tienen cuaderno conservan su planificación docente y siguen figurando como pendientes en `docs/COBERTURA_ESTUDIANTE.md`.",
        "- Prioridad: primero OA donde el insumo genérico contradice el contenido; después los niveles con mayor repetición de una misma consigna.",
        "- Estado de revisión profesional: **pendiente** para todos los lotes. La validación automática no la sustituye.",
        "",
    ]
    return "\n".join(out)


def main(argv: list[str]) -> int:
    text = report()
    if "--write" in argv:
        REPORT.write_text(text, encoding="utf-8", newline="\n")
        return 0
    if not REPORT.exists() or REPORT.read_text(encoding="utf-8") != text:
        print("docs/AUDITORIA_CONTENIDO.md no está sincronizado; ejecuta audit_content.py --write")
        return 1
    print("Auditoría de contenido sincronizada.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

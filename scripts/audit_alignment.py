"""Alignment audit of student notebooks against the official OA and the planned class title.

For each lesson with a notebook it measures (a) how much of the official OA statement and of
the class title (content words, by 5-letter stem) is actually present in the notebook, and
(b) whether the explanation is readable for the grade (average sentence length), plus a few
pedagogical smells. It does NOT judge disciplinary accuracy: it ranks lessons so a person
reads the weakest ones first. Output: docs/ANALISIS_ALINEACION.md (check with no arguments,
refresh with --write).
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import student_lessons as sl  # noqa: E402
import validate_student_lessons as validator  # noqa: E402

REPORT = ROOT / "docs" / "ANALISIS_ALINEACION.md"
MIN_COVERAGE = 0.5
LOW_OA = 0.34
MAX_SENTENCE_WORDS = {1: 16, 2: 18}
STOP = set("""para como entre desde hasta sobre cuando donde porque también algunos algunas
otros otras cada esta este estos estas mediante usando utilizando través según
forma manera nivel clase tema parte partir hacia puede pueden mismo misma
del las los una unos unas por con sin que son era ser más muy sus""".split())
SMELLS = (
    (re.compile(r"\bdepende\b", re.I), "respuesta «depende» en ejercicio cerrado"),
    (re.compile(r"\bpor ejemplo\b", re.I), "respuesta abierta «por ejemplo»"),
)


def stems(text: str) -> set[str]:
    plain = unicodedata.normalize("NFD", text.lower())
    plain = "".join(c for c in plain if unicodedata.category(c) != "Mn")
    return {w[:5] for w in re.findall(r"[a-zñ]{5,}", plain) if w not in STOP and w[:5] not in STOP}


def official(path: Path, number: int) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    oa = re.search(r"## Qué se debe aprender\s+>\s*(.+)", text)
    title = re.search(rf"^### Clase {number} de \d+: (.+?)(?: \{{#|$)", text, re.M)
    return (oa.group(1) if oa else ""), (title.group(1) if title else "")


def notebook_text(content: dict) -> str:
    parts = [content["use"], *content["explain"], *(f"{a} {b}" for a, b in content["vocab"])]
    for example in content["worked"]:
        parts += [example["title"], example["problem"], *example["steps"], example["answer"]]
    for item in sl.all_questions(content):
        parts += [item["q"], item["a"], item["why"]]
    parts += [content["open_task"]["statement"], content["open_task"]["example"]]
    return " ".join(parts)


def sentence_length(content: dict) -> float:
    sentences = [s for s in re.split(r"[.!?]+\s", " ".join(content["explain"])) if s.strip()]
    return sum(len(s.split()) for s in sentences) / max(1, len(sentences))


def analyse(level_prefix: str) -> list[dict]:
    sl.load_all()
    rows = []
    for (oa_code, number), content in sorted(sl.REGISTRY.items()):
        path = validator.curriculum_file(oa_code)
        if path is None or not path.relative_to(ROOT).parts[1].startswith(level_prefix):
            continue
        oa_text, title = official(path, number)
        wanted = stems(f"{oa_text} {title}")
        have = stems(notebook_text(content))
        coverage = len(wanted & have) / len(wanted) if wanted else 1.0
        title_wanted = stems(title)
        title_cov = len(title_wanted & have) / len(title_wanted) if title_wanted else 1.0
        smells = []
        for question in sl.closed_exercises(content):
            for pattern, label in SMELLS[:1]:
                if pattern.search(question["a"]):
                    smells.append(label)
        rows.append({
            "code": oa_code, "number": number, "title": title, "coverage": coverage, "title_cov": title_cov,
            "sentence": sentence_length(content), "smells": sorted(set(smells)),
            "subject": path.relative_to(ROOT).parts[2],
        })
    return rows


MANUAL_READING = [
    "## Lecturas manuales realizadas",
    "",
    "Se leyeron contra el OA oficial y el título planificado las clases siguientes, que la heurística había marcado. Todas resultaron coherentes con su OA; no se encontró un desajuste de contenido. Es una muestra, no una revisión profesional.",
    "",
    "| OA | Clase | Resultado de la lectura |",
    "|---|---:|---|",
    "| EN01 OA 02 | 3 | Alineada: enseña have y has con cantidades y la pregunta how many, como indica el título. |",
    "| CN01 OA 04 | 1 | Alineada: clasifica semillas con cuatro criterios (tamaño, forma, textura, color). |",
    "| EF01 OA 04 | 1 | Alineada: leer el lugar (superficie, límites, riesgos) antes de moverse. |",
    "| EF01 OA 04 | 2 | Alineada: adaptar paso y velocidad según el suelo. |",
    "| LE01 OA 23 | 3 | Alineada: describir con nombre, color, forma, tamaño y uso. |",
    "| LE01 OA 07 | 1 | Alineada: distinguir poema, historia breve y texto con patrón. |",
    "| LE01 OA 05 | 2 | Alineada: releer para leer de corrido. |",
    "| AR01 OA 01 | 5 | Alineada: compara obras latinoamericanas y universales; los datos de artistas quedan en la lista de revisión profesional. |",
    "",
]


def report(level_prefix: str = "1-basico", grade: int = 1) -> str:
    rows = analyse(level_prefix)
    limit = MAX_SENTENCE_WORDS.get(grade, 20)
    flagged = [r for r in rows if (r["coverage"] < LOW_OA and r["title_cov"] < MIN_COVERAGE) or r["sentence"] > limit or r["smells"]]
    by_subject: dict[str, list[dict]] = {}
    for row in rows:
        by_subject.setdefault(row["subject"], []).append(row)
    out = [
        f"# Análisis de alineación con el OA oficial · {grade}.º básico",
        "",
        "Este análisis contrasta cada cuaderno con el **texto oficial del OA** y con el **título de la clase planificada**: mide qué parte de sus términos de contenido aparece realmente en el cuaderno, la longitud media de las oraciones de la explicación y algunas señales pedagógicas débiles. **No** juzga exactitud disciplinar: ordena las clases para que una persona lea primero las más débiles. Se regenera con `python scripts/audit_alignment.py --write`.",
        "",
        f"Criterio de marca: cobertura del OA menor que {int(LOW_OA * 100)} % **y** del título menor que {int(MIN_COVERAGE * 100)} %, o explicación con oraciones de más de {limit} palabras en promedio, o respuestas «depende» en ejercicios cerrados.",
        "",
        "**Límite de la medida.** Es una heurística de triage por coincidencia de términos: sobre-marca, sobre todo en Inglés, donde el título planificado es metalenguaje docente («Connect prior knowledge») que no aparece en un cuaderno para estudiantes, y en las clases de Lengua y Cultura, cuyo título lleva rótulos de método. Una marca no prueba un defecto; una ausencia de marca no prueba exactitud.",
        "",
        "## Resumen por asignatura",
        "",
        "| Asignatura | Clases | Cobertura media del OA y título | Clases marcadas |",
        "|---|---:|---:|---:|",
    ]
    for subject, items in sorted(by_subject.items()):
        mean = 100 * sum(r["coverage"] for r in items) / len(items)
        marked = sum(1 for r in items if r in flagged)
        out.append(f"| {subject} | {len(items)} | {f'{mean:.0f}'} % | {marked} |")
    out += ["", f"**Clases marcadas para lectura prioritaria:** {len(flagged)} de {len(rows)}.", ""]
    out += MANUAL_READING
    if flagged:
        out += ["## Clases marcadas", "", "| OA | Clase | Título planificado | Cobertura OA | Cobertura título | Oración media | Señales |", "|---|---:|---|---:|---:|---:|---|"]
        for row in sorted(flagged, key=lambda r: (r["coverage"], r["code"])):
            out.append(f"| {row['code']} | {row['number']} | {row['title'][:60]} | {100 * row['coverage']:.0f} % | {100 * row['title_cov']:.0f} % | {row['sentence']:.1f} | {'; '.join(row['smells']) or '—'} |")
        out.append("")
    return "\n".join(out)


def main(argv: list[str]) -> int:
    text = report()
    if "--write" in argv:
        REPORT.write_text(text, encoding="utf-8", newline="\n")
        print(text.split("**Clases marcadas")[1].split("\n")[0])
        return 0
    if not REPORT.exists() or REPORT.read_text(encoding="utf-8") != text:
        print("docs/ANALISIS_ALINEACION.md no está sincronizado; ejecuta audit_alignment.py --write")
        return 1
    print("Análisis de alineación sincronizado.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

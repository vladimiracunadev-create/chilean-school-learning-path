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


MANUAL_1 = [
    "### Segunda lectura crítica de las 691 clases",
    "",
    "Después de la validación automática, cada una de las 691 clases de 1.º básico fue releída de principio a fin por un segundo lector (asistido por IA, independiente de quien la escribió), que la contrastó con el texto del OA y el título de la clase en el currículo del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional: se usó el texto oficial reproducido en cada ficha.",
    "",
    "| Asignatura | Clases releídas | Defectos corregidos (resumen de los informes) |",
    "|---|---:|---|",
    "| Matemática | 83 | Dato falso sobre la derecha y la izquierda; centímetros y operaciones de 2.º básico en OA 18 y otros; contradicciones internas entre explicación y ejemplos; respuestas falsas en patrones y familias de operaciones. |",
    "| Lenguaje y Comunicación | 131 | Conteos de palabras erróneos; datos falsos en textos (gatos que no nadan, osos pescando en invierno); definiciones y terminología silábica; léxico difícil sin definir; ejercicios de oralidad ambiguos. |",
    "| Ciencias Naturales | 49 | Conclusiones no justificadas por los datos; cifras de seres vivos eliminadas o hechas cualitativas; datos de ejemplo rotulados; operaciones de otro nivel; avisos de seguridad. |",
    "| Historia, Geografía y Ciencias Sociales | 68 | Edades calculadas sin considerar el mes; voto femenino (1934 y 1949 son leyes, no el día en que votaron); restas de años fuera de nivel; fechas de casos inventados; ambigüedades de mapas. |",
    "| Inglés | 69 | Inglés incorrecto o antinatural; estructuras de otro nivel; vocabulario usado sin enseñarse; explicaciones en español falsas; expresiones del OA agregadas (/s/-/z/, I want, Here). |",
    "| Lengua y Cultura de los Pueblos Originarios | 129 | Conteos de sílabas y palabras; afirmaciones culturales no seguras eliminadas o generalizadas; frase inventada retirada; preguntas que jerarquizaban identidad; aritmética de otro nivel. |",
    "| Educación Física y Salud | 48 | Riesgos motores (retroceder de espaldas); equivalencias falsas («dos brazos» = 2 m); cifras de salud generalizadas; ejercicios imposibles de practicar. |",
    "| Orientación | 35 | Lenguaje de las clases de cuerpo y protección ajustado («no es tu culpa», nada es un secreto); ambigüedades; operaciones de otro nivel; seguridad con tijeras. |",
    "| Música | 29 | Conteos de pulsos y sílabas erróneos; contradicciones entre consigna y ejemplo; objetos de vidrio y martillo reemplazados por opciones seguras. |",
    "| Artes Visuales | 24 | Multiplicaciones y restas de años de otro nivel; datos de obras dudosos; ambigüedades. |",
    "| Tecnología | 26 | Instrucciones de seguridad incorrectas; respuesta contraria a lo enseñado; multiplicaciones; software ficticio rotulado. |",
    "",
    "#### Vacíos de cobertura frente al OA",
    "",
    "- **Cerrados en una pasada posterior:** Inglés OA 03 (contraste /w/-/th/) y OA 07 (ocupaciones y comida); Tecnología OA 03 (fibras y plásticos) y OA 06 (tipos de software); Historia (restas de años de cuatro cifras reemplazadas por comparación, orden y saltos cortos).",
    "- **Lenguaje:** OA 17 y OA 09 piden obras completas y poemas de autor; el cuaderno usa textos originales breves por derechos de autor. Queda abierto.",
    "- **Lengua y Cultura de los Pueblos Originarios:** las clases de lengua se practican sólo con castellano y el saludo «mari mari»; el aprendizaje de la lengua real queda en manos del educador o educadora tradicional.",
    "",
    "Todos los contenidos que requieren especialista, incluida la verificación contra el Programa de Estudio oficial, siguen listados en [Revisión profesional pendiente](REVISION_PENDIENTE_CUADERNOS.md).",
    "",
]

MANUAL_2 = [
    "### Segunda lectura crítica de las 721 clases",
    "",
    "Cada una de las 721 clases de 2.º básico (las 20 de Matemática OA 01 a 05 escritas antes y las 701 restantes) fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y con el título de la clase en la ficha del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional.",
    "",
    "| Asignatura | Clases releídas | Defectos corregidos (resumen de los informes) |",
    "|---|---:|---|",
    "| Matemática | 93 | Materiales que no existían en el cuaderno (tablas y tarjetas «de este cuaderno»); billetes de $10 y $100 inexistentes; multiplicaciones, divisiones y años de cuatro cifras fuera de nivel; error ilustrado sin sentido; saltos que cruzaban la decena que la clase prohibía; restas de reloj de 24 horas sin enseñar la regla. |",
    "| Lenguaje y Comunicación | 149 | Regla de diptongo falsa («ciudad»); «g fuerte» contraria a la enseñanza tradicional; palabras y conteos erróneos; dato falso sobre aves en Chile; estructuras no enseñadas; enunciados que daban la respuesta; textos que podían herir (tartamudez, edad, familia). |",
    "| Ciencias Naturales | 57 | Datos biológicos falsos (piel de anfibios, escorpión diurno, «las branquias sacan el aire»); caracol sin concha; estaciones con fechas aproximadas; hielo en vaso de vidrio; veleta con alfiler. |",
    "| Historia, Geografía y Ciencias Sociales | 72 | Respuestas con más de una válida (países de referencia); anacronismo de los videos; piñones atribuidos a todos los mapuche; seguridad ante temblor y tsunami; términos usados sin definir. |",
    "| Inglés | 68 | Inglés incorrecto («has a bread»); conteos de palabras falsos; estructuras no enseñadas (do you like, here you are); prueba de «vibra la garganta» engañosa; regla a/an con excepciones. |",
    "| Lengua y Cultura de los Pueblos Originarios | 116 | Eliminadas o generalizadas fechas y ceremonias (We Tripantu, Tapati, Año Nuevo, Pachamama, machi, yatiri); asociaciones de arte con pueblos; variante «cuyén» de ortografía no segura; afirmación histórica generalizada; aritmética de otro nivel. |",
    "| Educación Física y Salud | 47 | Volteo sin supervisión; alfombra y libro como superficies resbalosas; pulso y respiración poco realistas; riesgo de caminar hacia atrás; protocolo inconsistente ante un compañero herido; contradicciones de datos en las metas. |",
    "| Orientación | 35 | Divisiones y multiplicaciones fuera de nivel; ejercicio alarmante sobre secretos reemplazado; doble negativo; supuestos sobre la composición de la familia; datos de higiene y sueño como recomendaciones generales. |",
    "| Música | 29 | Respuesta de ejemplo que no cambiaba el pulso; confusión entre vocal y altura del sonido; pieza que no calzaba con la respuesta; enunciado subjetivo de más suave a más fuerte. |",
    "| Artes Visuales | 24 | Actividad que contradecía sus criterios; ejercicios sobre lo no enseñado (óvalos); ambigüedades de enunciado; obras reales sustituidas por tipos de obra seguros. |",
    "| Tecnología | 31 | Falso «las imágenes propias no tienen derechos de autor»; relleno que no tapa un dibujo; instrucciones de seguridad; software ficticio rotulado. |",
    "",
    "#### Vacíos de cobertura frente al OA",
    "",
    "- **Cerrados dentro de las clases existentes:** Lenguaje (grupo «dr», anécdota, experiencia personal y relato de hechos, carta, cuento folclórico frente a cuento de autor, lectura independiente); Historia (chango, rapa nui y huilliche, inmigración oriental, patrimonio de más regiones, río, océano, isla y ciudad); Artes (textiles, herramientas digitales, tipos de obra local, latinoamericana y universal); Ciencias (hábitat del mamífero); Matemática (preguntas estadísticas, números cercanos a 1.000); Educación Física (niveles, juegos individuales y colectivos).",
    "- **Abiertos:** Artes OA 04 pide observar al año 10 obras locales o chilenas, 10 latinoamericanas y 10 universales, y el cuaderno solo puede describirlas (imágenes reales y derechos los aporta el docente); Música OA 03 nombra obras con derechos que no se reproducen; Lenguaje OA 06 y 22 piden poemas y cuentos reales de autor o tradicionales; Lengua y Cultura de los Pueblos Originarios: relatos, textos y oraciones reales en lengua indígena y eventos o técnicas propias de cada pueblo los aporta el educador o educadora tradicional; software educativo (Matemática OA 03, 09 y 12) es opcional en el OA y no se puede entregar en el cuaderno; Ciencias OA 02 (moluscos y miriápodos) y vocabulario «endémico» de OA 05 requerirían clases nuevas.",
    "- **Decisiones que dependen del programa oficial:** reloj de 24 horas o a. m./p. m. (Matemática OA 18), equivalencia 1 m = 100 cm (OA 19) y aristas y vértices del cubo (OA 16); no se pudo contrastar con el texto vigente.",
    "- **Criterio distinto entre asignaturas, a revisar por especialista:** Historia mantiene las celebraciones y ceremonias de los pueblos (ngillatun, We Tripantu, Año Nuevo Andino, Tapati, Hain, Pachamama) como fichas generales, porque el OA 01 pide creencias y fiestas; Lengua y Cultura las eliminó por no poder afirmarlas con seguridad.",
    "",
]


LEVELS = (("1-basico", 1, MANUAL_1), ("2-basico", 2, MANUAL_2))


def section(level_prefix: str, grade: int, manual: list[str]) -> list[str]:
    rows = analyse(level_prefix)
    limit = MAX_SENTENCE_WORDS.get(grade, 20)
    flagged = [r for r in rows if (r["coverage"] < LOW_OA and r["title_cov"] < MIN_COVERAGE) or r["sentence"] > limit or r["smells"]]
    by_subject: dict[str, list[dict]] = {}
    for row in rows:
        by_subject.setdefault(row["subject"], []).append(row)
    out = [
        f"## {grade}.º básico",
        "",
        f"Criterio de marca: cobertura del OA menor que {int(LOW_OA * 100)} % **y** del título menor que {int(MIN_COVERAGE * 100)} %, o explicación con oraciones de más de {limit} palabras en promedio, o respuestas «depende» en ejercicios cerrados.",
        "",
        "### Resumen por asignatura",
        "",
        "| Asignatura | Clases | Cobertura media del OA y título | Clases marcadas |",
        "|---|---:|---:|---:|",
    ]
    for subject, items in sorted(by_subject.items()):
        mean = 100 * sum(r["coverage"] for r in items) / len(items)
        marked = sum(1 for r in items if r in flagged)
        out.append(f"| {subject} | {len(items)} | {f'{mean:.0f}'} % | {marked} |")
    out += ["", f"**Clases marcadas para lectura prioritaria ({grade}.º básico):** {len(flagged)} de {len(rows)}.", ""]
    out += manual
    if flagged:
        out += [f"### Clases marcadas de {grade}.º básico", "", "| OA | Clase | Título planificado | Cobertura OA | Cobertura título | Oración media | Señales |", "|---|---:|---|---:|---:|---:|---|"]
        for row in sorted(flagged, key=lambda r: (r["coverage"], r["code"])):
            out.append(f"| {row['code']} | {row['number']} | {row['title'][:60]} | {100 * row['coverage']:.0f} % | {100 * row['title_cov']:.0f} % | {row['sentence']:.1f} | {'; '.join(row['smells']) or '—'} |")
        out.append("")
    return out


def report() -> str:
    out = [
        "# Análisis de alineación con el OA oficial",
        "",
        "Este análisis contrasta cada cuaderno con el **texto oficial del OA** y con el **título de la clase planificada**: mide qué parte de sus términos de contenido aparece realmente en el cuaderno, la longitud media de las oraciones de la explicación y algunas señales pedagógicas débiles. **No** juzga exactitud disciplinar: ordena las clases para que una persona lea primero las más débiles. Se regenera con `python scripts/audit_alignment.py --write`.",
        "",
        "**Límite de la medida.** Es una heurística de triage por coincidencia de términos: sobre-marca, sobre todo en Inglés, donde el título planificado es metalenguaje docente («Connect prior knowledge») que no aparece en un cuaderno para estudiantes, y en las clases de Lengua y Cultura, cuyo título lleva rótulos de método. Una marca no prueba un defecto; una ausencia de marca no prueba exactitud.",
        "",
    ]
    for level_prefix, grade, manual in LEVELS:
        out += section(level_prefix, grade, manual)
    return chr(10).join(out)


def main(argv: list[str]) -> int:
    text = report()
    if "--write" in argv:
        REPORT.write_text(text, encoding="utf-8", newline="\n")
        print("Análisis de alineación escrito.")
        return 0
    if not REPORT.exists() or REPORT.read_text(encoding="utf-8") != text:
        print("docs/ANALISIS_ALINEACION.md no está sincronizado; ejecuta audit_alignment.py --write")
        return 1
    print("Análisis de alineación sincronizado.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

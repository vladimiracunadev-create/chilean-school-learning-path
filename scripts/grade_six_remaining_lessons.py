"""Specific sixth-grade sequences for every subject except Mathematics.

Profiles are derived from the checked-in MINEDUC snapshot and completed with
discipline-specific anchors, misconceptions, vocabulary and lesson protocols.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

try:
    from grade_three_arts_pe_english_indigenous_lessons import _lesson as apei_lesson
    from grade_three_math_language_lessons import _lesson as language_lesson
    from grade_three_music_orientation_technology_lessons import _lesson as mot_lesson
    from grade_three_science_history_lessons import _lesson as inquiry_lesson
    from grade_four_remaining_lessons import build_transversal_integration as base_integration
except ImportError:
    from scripts.grade_three_arts_pe_english_indigenous_lessons import _lesson as apei_lesson
    from scripts.grade_three_math_language_lessons import _lesson as language_lesson
    from scripts.grade_three_music_orientation_technology_lessons import _lesson as mot_lesson
    from scripts.grade_three_science_history_lessons import _lesson as inquiry_lesson
    from scripts.grade_four_remaining_lessons import build_transversal_integration as base_integration


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))

SUBJECTS = {
    "AR": ("artes-visuales", "Artes Visuales"),
    "CN": ("ciencias-naturales", "Ciencias Naturales"),
    "EF": ("educacion-fisica-salud", "Educación Física y Salud"),
    "HI": ("historia-geografia-ciencias-sociales", "Historia, Geografía y Ciencias Sociales"),
    "IN": ("ingles", "Inglés"),
    "EN": ("ingles-propuesta", "Inglés (Propuesta)"),
    "LC": ("lengua-cultura-pueblos-originarios-ancestrales", "Lengua y Cultura de los Pueblos Originarios Ancestrales"),
    "LE": ("lenguaje-comunicacion", "Lenguaje y Comunicación"),
    "MU": ("musica", "Música"),
    "OR": ("orientacion", "Orientación"),
    "TE": ("tecnologia", "Tecnología"),
}

STAGES = {
    "AR": ["Observar y formular una intención", "Explorar una variable visual", "Elegir materiales y procedimientos", "Crear una respuesta propia", "Interpretar y fundamentar", "Revisar sin perder autoría"],
    "CN": ["Observar y separar evidencia de interpretación", "Formular una pregunta o predicción", "Modelar el sistema o fenómeno", "Comparar resultados con un criterio", "Explicar con evidencia y límites", "Transferir a una decisión responsable"],
    "EF": ["Reconocer meta y seguridad", "Modelar control y decisión motriz", "Ensayar con variantes accesibles", "Resolver una situación nueva", "Regular esfuerzo y explicar", "Transferir a otro entorno"],
    "HI": ["Ubicar en tiempo y espacio", "Interrogar fuentes y procedencia", "Relacionar actores, causas y consecuencias", "Comparar perspectivas o territorios", "Argumentar con evidencia", "Evaluar una decisión ciudadana"],
    "IN": ["Notice purpose and context", "Locate key words and clues", "Model a communicative strategy", "Interact or compose with support", "Communicate independently", "Check meaning and revise"],
    "EN": ["Notice purpose and context", "Locate key words and clues", "Model a communicative strategy", "Interact or compose with support", "Communicate independently", "Check meaning and revise"],
    "LC": ["Situar pueblo, territorio y fuente", "Escuchar o leer con límites declarados", "Reconocer relaciones culturales", "Construir una respuesta atribuida", "Contrastar sin jerarquizar", "Comunicar con validación pertinente"],
    "LE": ["Reconocer propósito y desafío", "Modelar una lectura o producción", "Seleccionar evidencia o recursos", "Comparar interpretaciones o decisiones", "Producir una respuesta propia", "Revisar para una audiencia", "Transferir a otro texto o situación"],
    "MU": ["Escuchar antes de nombrar", "Reconocer un rasgo audible", "Interpretar o crear con criterio", "Ensayar y ajustar desde la escucha", "Comunicar una decisión musical", "Reflexionar y transferir"],
    "OR": ["Examinar un caso ficticio protegido", "Distinguir hechos, emociones y límites", "Comparar opciones y consecuencias", "Elegir una acción segura", "Practicar comunicación o ayuda", "Transferir sin exposición personal"],
    "TE": ["Definir necesidad, usuario y criterio", "Representar una solución", "Planificar recursos y seguridad", "Elaborar o configurar", "Probar con evidencia", "Mejorar y comunicar"],
}

PRIOR = {
    "AR": "crear y apreciar producciones visuales con decisiones propias en 5° básico",
    "CN": "observar, medir, modelar y explicar fenómenos con evidencia en 5° básico",
    "EF": "combinar habilidades motrices, autocuidado y juego limpio en 5° básico",
    "HI": "interpretar mapas, secuencias, fuentes y situaciones ciudadanas de 5° básico",
    "IN": "understand and produce short messages with visual and linguistic support",
    "EN": "understand and produce short messages with visual and linguistic support",
    "LC": "aprender desde territorio, oralidad y fuentes comunitarias pertinentes, sin inventar lengua",
    "LE": "leer, escribir y conversar con evidencia, propósito y audiencia en 5° básico",
    "MU": "escuchar, interpretar, crear y comentar música con criterios audibles en 5° básico",
    "OR": "reconocer emociones, derechos, autocuidado y participación sin exposición personal",
    "TE": "diseñar, elaborar, probar y comunicar soluciones tecnológicas de 5° básico",
}

VOCABULARY = {
    "AR": "intención, referente, lenguaje visual, material, procedimiento, contexto, criterio, revisión",
    "CN": "pregunta, variable, observación, evidencia, patrón, sistema, modelo, limitación",
    "EF": "control, estrategia, intensidad, seguridad, cooperación, regulación, evidencia, autocuidado",
    "HI": "fuente, contexto, actor, territorio, temporalidad, causa, consecuencia, perspectiva",
    "IN": "purpose, audience, clue, key word, chunk, interaction, meaning, revision",
    "EN": "purpose, audience, clue, key word, chunk, interaction, meaning, revision",
    "LC": "territorio, oralidad, fuente, autorización, variante, identidad, reciprocidad, revitalización",
    "LE": "propósito, audiencia, evidencia, inferencia, estructura, registro, cohesión, revisión",
    "MU": "pulso, ritmo, melodía, timbre, dinámica, forma, interpretación, creación",
    "OR": "dignidad, emoción, límite, autocuidado, consecuencia, apoyo, acuerdo, participación",
    "TE": "necesidad, usuario, criterio, restricción, herramienta, prototipo, prueba, impacto",
}

ANCHORS = {
    "AR": "referentes atribuidos, pruebas de taller y materiales disponibles para {topic}",
    "CN": "modelos, datos, observaciones y experiencias seguras vinculadas con {topic}",
    "EF": "estaciones, reglas visibles, implementos seguros y variantes accesibles para {topic}",
    "HI": "mapas, fuentes contrastables, datos y casos situados sobre {topic}",
    "IN": "short authorized oral, visual and written texts designed for {topic}",
    "EN": "short authorized oral, visual and written texts designed for {topic}",
    "LC": "fuentes autorizadas y situadas por pueblo y territorio para {topic}",
    "LE": "textos completos o fragmentos autorizados, propósitos y audiencias vinculados con {topic}",
    "MU": "registros autorizados, partituras gráficas e instrumentos disponibles para {topic}",
    "OR": "casos ficticios, opciones de respuesta y protocolos escolares vinculados con {topic}",
    "TE": "un desafío documentado, recursos disponibles y criterios previos para {topic}",
}

MISCONCEPTIONS = {
    "AR": ["copiar referentes sin intención propia", "evaluar sólo por gusto o parecido", "usar técnicas sin relacionarlas con el efecto"],
    "CN": ["tratar una opinión como evidencia", "cambiar varias variables y atribuir una causa", "presentar un modelo como copia exacta de la realidad"],
    "EF": ["priorizar velocidad sobre control y seguridad", "comparar cuerpos o rendimiento entre estudiantes", "aplicar una táctica sin leer espacio, reglas y compañeros"],
    "HI": ["tratar una fuente como verdad completa", "juzgar el pasado sólo desde el presente", "generalizar un caso a todos los actores o territorios"],
    "IN": ["translate every word before communicating", "recite a model without attending to meaning", "treat accent or immediate accuracy as intelligence"],
    "EN": ["translate every word before communicating", "recite a model without attending to meaning", "treat accent or immediate accuracy as intelligence"],
    "LC": ["inventar lengua o explicaciones culturales", "generalizar una fuente a todos los pueblos", "divulgar saberes o registros sin autorización"],
    "LE": ["resumir en vez de interpretar", "opinar sin evidencia textual", "corregir sólo ortografía sin revisar propósito y sentido"],
    "MU": ["describir sólo gusto sin evidencia audible", "confundir precisión con volumen o velocidad", "presentar una música como representación total de una cultura"],
    "OR": ["solicitar experiencias personales para demostrar aprendizaje", "moralizar o diagnosticar a una persona", "resolver seguridad mediante secreto, culpa u obediencia"],
    "TE": ["construir antes de definir criterios", "evaluar sólo apariencia", "usar herramientas o datos sin revisar seguridad y privacidad"],
}


def _dose(text: str, slug: str, readings: list) -> int:
    lowered = text.lower()
    count = 4
    if len(text) > 260 or lowered.count(";") >= 2:
        count += 1
    if any(verb in lowered for verb in ("investigar", "crear", "producir", "diseñar", "evaluar", "analizar", "argumentar", "interpretar")):
        count += 1
    if readings or ("leng" in slug and any(verb in lowered for verb in ("leer", "escribir", "obra", "texto"))):
        count += 1
    return min(count, 7)


def _topic(description: str) -> str:
    cleaned = re.sub(r"\s+", " ", description).strip().rstrip(".")
    for start in ("Demostrar que comprenden ", "Comprender ", "Realizar ", "Resolver ", "Explicar ", "Analizar ", "Crear ", "Producir "):
        if cleaned.startswith(start):
            cleaned = cleaned[len(start):]
            break
    first = re.split(r"[;:]", cleaned, maxsplit=1)[0]
    words = first.split()
    return " ".join(words[:18]).strip().capitalize()


RECORDS = {}
for record in SNAPSHOT["records"]:
    if record["course_order"] != 6 or record["subject_slug"] == "matematica":
        continue
    for objective in record["objectives"]:
        code = objective["code"]
        if code.startswith("de "):
            continue
        RECORDS[code] = {
            "slug": record["subject_slug"],
            "description": objective["description"],
            "url": objective["url"],
            "count": _dose(objective["description"], record["subject_slug"], objective.get("readings", [])),
        }


def _profile(code: str) -> dict:
    prefix = code[:2]
    record = RECORDS[code]
    topic = _topic(record["description"])
    number_match = re.search(r"(\d+)$", code)
    number = int(number_match.group(1)) if number_match else sum(ord(char) for char in code)
    return {
        "topic": topic,
        "prior": PRIOR[prefix],
        "vocabulary": VOCABULARY[prefix],
        "anchor": ANCHORS[prefix].format(topic=topic.lower()),
        "misconception": f"en {topic.lower()}, {MISCONCEPTIONS[prefix][(number - 1) % 3]}",
        "focuses": [f"{stage} · {topic}" for stage in STAGES[prefix][:record['count']]],
    }


def _fix_links(lesson: dict, prefix: str) -> dict:
    for link in lesson.get("transversal", []):
        for old in ("AR03", "CN03", "EF03", "HI03", "EN03", "LC03", "LE03", "MU03", "OR03", "TE03"):
            link["code"] = link["code"].replace(old, f"{prefix}06")
    return lesson


def build_sequence(code: str) -> dict | None:
    if code not in RECORDS:
        return None
    prefix = code[:2]
    profile = _profile(code)
    lessons = []
    for index, focus in enumerate(profile["focuses"]):
        if prefix == "LE":
            lesson = language_lesson(code, index, profile, "language")
        elif prefix in {"CN", "HI"}:
            lesson = inquiry_lesson(code, index, profile, "science" if prefix == "CN" else "history")
        elif prefix in {"MU", "OR", "TE"}:
            lesson = mot_lesson(code, index, profile)
        else:
            maker_code = code.replace("IN06", "EN06", 1) if prefix == "IN" else code
            lesson = apei_lesson(maker_code, index, profile)
        lesson = _fix_links(lesson, prefix)
        lesson["title"] = f"{lesson['title']} · {SUBJECTS[prefix][1]} · {code}"
        focus_lower = focus.lower()
        route = f"{SUBJECTS[prefix][1]} · {code} · clase {index + 1}"
        lesson["opening"] += f" El registro inicial queda asociado a la ruta {route} para compararlo con la evidencia final."
        lesson["model"] += f" El docente nombra el criterio de la ruta {route} y muestra por qué no se transfiere mecánicamente a otro OA."
        lesson["guided"] += f" En {route}, la retroalimentación vuelve al criterio propio de «{focus_lower}» antes del segundo intento."
        lesson["independent"] += f" En {route}, la evidencia se juzga por el logro de «{focus_lower}», no por imitar el ejemplo."
        lesson["ticket"] += f" La respuesta final de {route} debe permitir comprobar «{focus_lower}»."
        lessons.append(lesson)
    record = RECORDS[code]
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": f"{profile['topic']} avanza desde {profile['prior']} mediante decisiones situadas. Cada clase cambia la evidencia y forma de participación, y enfrenta la confusión «{profile['misconception']}».",
        "prerequisites": profile["prior"],
        "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"Eje oficial · progresión interna en {len(lessons)} clases"],
            "unit_origin": "Organización pedagógica interna derivada del eje y del OA; no se presenta como una unidad oficial del programa",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del OA oficial",
            "source": record["url"],
        },
        "lessons": lessons,
    }


def build_transversal_integration(item: dict) -> dict:
    prepared = dict(item)
    if item["subject_slug"] == "ingles":
        prepared["subject_slug"] = "ingles-propuesta"
    result = base_integration(prepared)
    result["generated_for"] = "6-basico"
    return result


SEQUENCES = {code: True for code in RECORDS}

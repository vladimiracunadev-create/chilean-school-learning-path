"""Specific second-year secondary Science, History and English sequences.

Official objectives and URLs come from the checked-in MINEDUC snapshot. The
short topics, classroom anchors, progressions and misconceptions are original
pedagogical elaborations. Inglés and Inglés (Propuesta) remain separate records.
"""
from __future__ import annotations

import json
from pathlib import Path

try:
    from grade_three_arts_pe_english_indigenous_lessons import _lesson as applied_lesson
    from grade_three_science_history_lessons import _lesson as inquiry_lesson
    from grade_four_remaining_lessons import build_transversal_integration as base_integration
    from grade_eight_next_four_lessons import _natural_voice as inquiry_voice
    from grade_seven_next_five_lessons import _natural_voice as english_voice
    from grade_seven_remaining_lessons import _natural_voice as proposal_voice
except ImportError:
    from scripts.grade_three_arts_pe_english_indigenous_lessons import _lesson as applied_lesson
    from scripts.grade_three_science_history_lessons import _lesson as inquiry_lesson
    from scripts.grade_four_remaining_lessons import build_transversal_integration as base_integration
    from scripts.grade_eight_next_four_lessons import _natural_voice as inquiry_voice
    from scripts.grade_seven_next_five_lessons import _natural_voice as english_voice
    from scripts.grade_seven_remaining_lessons import _natural_voice as proposal_voice


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
CATALOG = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
TARGET_SLUGS = {"ciencias-naturales", "historia-geografia-ciencias-sociales", "ingles", "ingles-propuesta"}


TOPICS = {
    # Ciencias Naturales · Biología, Física y Química
    "CN2M OA 01": "Sistema nervioso, respuesta a estímulos y cuidados",
    "CN2M OA 02": "Regulación hormonal de glicemia y reproducción",
    "CN2M OA 03": "Sexualidad humana, dimensiones y responsabilidad",
    "CN2M OA 04": "Fecundación, desarrollo embrionario y cuidado prenatal",
    "CN2M OA 05": "Regulación de la fertilidad y parentalidad responsable",
    "CN2M OA 06": "Mitosis, meiosis y alteraciones de la división celular",
    "CN2M OA 07": "Herencia mendeliana en plantas y animales",
    "CN2M OA 08": "Manipulación genética, aplicaciones e implicancias",
    "CN2M OA 09": "Movimiento rectilíneo, velocidad y aceleración",
    "CN2M OA 10": "Fuerza neta, leyes de Newton y cuerpo libre",
    "CN2M OA 11": "Trabajo, potencia y conservación de energía mecánica",
    "CN2M OA 12": "Impulso, momentum y colisiones",
    "CN2M OA 13": "Modelos del Universo y cambio del conocimiento científico",
    "CN2M OA 14": "Gravitación, leyes de Kepler y estructuras cósmicas",
    "CN2M OA 15": "Soluciones, componentes y concentración",
    "CN2M OA 16": "Propiedades coligativas en procesos cotidianos",
    "CN2M OA 17": "Carbono, biomoléculas e hidrocarburos",
    "CN2M OA 18": "Estereoquímica e isomería de compuestos orgánicos",
    # Historia, Geografía y Ciencias Sociales
    "HI2M OA 01": "Vanguardias y cultura de masas en entreguerras",
    "HI2M OA 02": "Crisis liberal, Gran Depresión y modelos políticos",
    "HI2M OA 03": "Segunda Guerra Mundial, genocidio y población civil",
    "HI2M OA 04": "Posguerra, descolonización, ONU y derechos humanos",
    "HI2M OA 05": "Crisis parlamentaria y Constitución chilena de 1925",
    "HI2M OA 06": "Gran Depresión, industrialización y Estado social en Chile",
    "HI2M OA 07": "Nuevos actores, cultura de masas y democratización",
    "HI2M OA 08": "Guerra Fría, amenaza nuclear y escenarios locales",
    "HI2M OA 09": "Bienestar, consumo, derechos y tecnología en Guerra Fría",
    "HI2M OA 10": "Revolución, reforma y dictaduras en América Latina",
    "HI2M OA 11": "Fin de la Guerra Fría, neoliberalismo y globalización",
    "HI2M OA 12": "Pobreza, migración campo-ciudad y segregación urbana",
    "HI2M OA 13": "Actores sociales y proyectos políticos chilenos de 1960",
    "HI2M OA 14": "Crisis, polarización y quiebre democrático en Chile",
    "HI2M OA 15": "Interpretaciones historiográficas del golpe de 1973",
    "HI2M OA 16": "Dictadura, supresión del Estado de derecho y violaciones",
    "HI2M OA 17": "Modelo neoliberal y consecuencias sociales en Chile",
    "HI2M OA 18": "Constitución de 1980, cambios y continuidades",
    "HI2M OA 19": "Factores de recuperación democrática en los años ochenta",
    "HI2M OA 20": "Plebiscito, transición, reparación y tensiones democráticas",
    "HI2M OA 21": "Sociedad chilena desde la recuperación democrática",
    "HI2M OA 22": "Derechos humanos e institucionalidad de protección",
    "HI2M OA 23": "Estado de derecho, participación y convivencia",
    "HI2M OA 24": "Desafíos pendientes y responsabilidades para Chile",
    "HI2M OA 25": "Diversidad, dignidad y no discriminación en un mundo global",
}

ENGLISH_TOPICS = {
    "IN2M OA 01": "Global and explicit meaning in varied oral texts",
    "IN2M OA 02": "Key expressions, collocations and second-year sound contrasts",
    "IN2M OA 03": "Purpose, relevant ideas, detail and problem-solution in listening",
    "IN2M OA 04": "Strategic listening, note-taking and supported inference",
    "IN2M OA 05": "Coherent multimodal oral presentation for an audience",
    "IN2M OA 06": "Planning, repairing and reviewing spoken English",
    "IN2M OA 07": "Evidence-based response, questions and hypotheses",
    "IN2M OA 08": "Second-year communicative functions in speech",
    "IN2M OA 09": "Global and explicit meaning in print and digital texts",
    "IN2M OA 10": "Purpose, structure and language in non-literary texts",
    "IN2M OA 11": "Theme, character, setting and conflict in literary texts",
    "IN2M OA 12": "Strategic reading before, during and after a text",
    "IN2M OA 13": "Creative multimodal stories and relevant information",
    "IN2M OA 14": "Independent writing process across purposeful genres",
    "IN2M OA 15": "Writing to analyze, narrate and express opinions",
    "IN2M OA 16": "Second-year communicative functions in writing",
    "EN2M OA 01": "Understanding varied literary and functional oral texts",
    "EN2M OA 02": "Purpose, detail, collocations and sound evidence in listening",
    "EN2M OA 03": "Purposeful listening, inference, note-taking and clarification",
    "EN2M OA 04": "Integrated literary and non-literary reading",
    "EN2M OA 05": "Language functions interpreted in meaningful texts",
    "EN2M OA 06": "Strategic reading before, during and after the text",
    "EN2M OA 07": "Critical response, synthesis and cultural connections",
    "EN2M OA 08": "Audience-aware multimodal oral presentation",
    "EN2M OA 09": "Strategies for clear, fluent and repairable interaction",
    "EN2M OA 10": "Second-year language functions in discussion",
    "EN2M OA 11": "Modeled multimodal writing for real audiences",
    "EN2M OA 12": "Second-year language functions in connected writing",
    "EN2M OA 13": "Independent writing process, revision and publication",
}

PRIOR = {
    "CN": "investigar sistemas biológicos, físicos y químicos mediante variables, modelos y evidencia en 1° medio",
    "HI": "contextualizar fuentes, construir explicaciones multicausales y argumentar sobre procesos históricos en 1° medio",
    "IN": "understand and produce connected messages with evidence, interaction and revision in first-year secondary",
    "EN": "understand and produce connected messages with evidence, interaction and revision in first-year secondary",
}

VOCABULARY = {
    "CN": "pregunta, variable, medición, evidencia, patrón, sistema, modelo, mecanismo, control, conclusión, validez, incertidumbre, limitación",
    "HI": "fuente, procedencia, contexto, temporalidad, actor, escala, multicausalidad, continuidad, cambio, perspectiva, memoria, derecho, argumento",
    "IN": "purpose, audience, gist, detail, clue, collocation, inference, interaction, function, evidence, repair, synthesis, revision",
    "EN": "purpose, audience, gist, detail, clue, collocation, inference, interaction, function, evidence, repair, synthesis, revision",
}

STAGES = {
    "CN": ("Plantear una pregunta o problema", "Examinar datos y representaciones", "Construir o contrastar un modelo", "Investigar relaciones entre variables", "Explicar mecanismos con evidencia", "Evaluar límites, seguridad e implicancias"),
    "HI": ("Situar el problema y sus actores", "Interrogar fuentes con procedencia", "Comparar perspectivas y escalas", "Relacionar causas, cambios y continuidades", "Construir una interpretación documentada", "Debatir consecuencias y límites"),
    "IN": ("Notice purpose and activate prior knowledge", "Locate meaning and language evidence", "Interpret relationships and unstated meaning", "Rehearse a purposeful response", "Produce for a defined audience", "Review, repair and transfer"),
    "EN": ("Notice purpose and activate prior knowledge", "Locate meaning and language evidence", "Interpret relationships and unstated meaning", "Rehearse a purposeful response", "Produce for a defined audience", "Review, repair and transfer"),
}

MISCONCEPTIONS = {
    "CN": (
        "tratar una correlación como mecanismo probado o ignorar variables de control",
        "usar una fórmula o un modelo sin declarar sistema, condiciones, unidades y límites",
        "convertir una cuestión de salud o bioética en juicio personal en vez de analizar evidencia y resguardos",
    ),
    "HI": (
        "explicar un proceso mediante una sola causa o una cronología sin actores ni escalas",
        "tratar una fuente como relato neutral sin examinar autoría, contexto, propósito y silencios",
        "usar categorías actuales para juzgar el pasado sin contexto o trasladar conflictos a estereotipos presentes",
    ),
    "IN": ("translate every word before constructing meaning", "copy a model without making audience choices", "correct grammar before meaning, evidence and organization are clear"),
    "EN": ("translate every word before constructing meaning", "copy a model without making audience choices", "correct grammar before meaning, evidence and organization are clear"),
}


def _science_anchor(code: str, topic: str) -> str:
    number = int(code.rsplit(" ", 1)[-1])
    if number <= 8:
        return f"modelos anatómicos o celulares, datos clínicos ficticios y fichas de evidencia segura para {topic.lower()}"
    if number <= 12:
        return f"montaje experimental seguro o conjunto de datos de posición, fuerza, energía o colisión, con unidades y sistema de referencia, para {topic.lower()}"
    if number <= 14:
        return f"modelos históricos, diagramas orbitales y datos astronómicos atribuidos para contrastar explicaciones sobre {topic.lower()}"
    return f"modelos de partículas o moléculas, datos experimentales seguros y tabla de propiedades para {topic.lower()}"


def _history_anchor(code: str, topic: str) -> str:
    number = int(code.rsplit(" ", 1)[-1])
    if number <= 4:
        source_set = "mapas, prensa, testimonios civiles, estadísticas y acuerdos internacionales"
    elif number <= 7:
        source_set = "prensa chilena, censos, leyes, fotografías y testimonios de actores sociales"
    elif number <= 11:
        source_set = "mapas de bloques, propaganda contrastada, discursos, datos sociales y fuentes latinoamericanas"
    elif number <= 21:
        source_set = "documentos oficiales, prensa diversa, testimonios públicos, series sociales y estudios historiográficos chilenos"
    else:
        source_set = "normas nacionales e internacionales, casos ficticios, datos públicos y posturas argumentadas"
    return f"dossier atribuido de {source_set} para investigar {topic.lower()}"


def _english_anchor(code: str, topic: str) -> str:
    prefix = code[:2]
    number = int(code.rsplit(" ", 1)[-1])
    if prefix == "IN" and number <= 4 or prefix == "EN" and number <= 3:
        return f"an original teacher-read audio for {topic.lower()}, a replay plan, listening grid and transcript released after the final listen"
    if prefix == "IN" and number in {5, 6, 7, 8} or prefix == "EN" and number in {7, 8, 9, 10}:
        return f"fictional information-gap cards, useful chunks, audience roles and a paper storyboard for {topic.lower()}"
    if prefix == "IN" and number in {9, 10, 11, 12} or prefix == "EN" and number in {4, 5, 6}:
        return f"short authorized literary and functional texts with numbered paragraphs, visuals and an essential glossary for {topic.lower()}"
    return f"fictional writing briefs, genre models, audience cards and a meaning-first revision checklist for {topic.lower()}"


COUNTS: dict[str, int] = {}
for item in CATALOG["classes"]:
    if item["course_order"] == 10 and item["subject_slug"] in TARGET_SLUGS and not item["oa_code"].startswith("de "):
        COUNTS[item["oa_code"]] = COUNTS.get(item["oa_code"], 0) + 1

RECORDS = {}
for record in SNAPSHOT["records"]:
    if record["course_order"] != 10 or record["subject_slug"] not in TARGET_SLUGS:
        continue
    for objective in record["objectives"]:
        if objective["code"].startswith("de "):
            continue
        RECORDS[objective["code"]] = {
            "slug": record["subject_slug"], "description": objective["description"],
            "url": objective["url"], "count": COUNTS[objective["code"]],
        }

PROFILES = set(TOPICS) | set(ENGLISH_TOPICS)
if set(RECORDS) != PROFILES:
    raise RuntimeError(f"Perfiles de 2° medio desalineados: faltan={sorted(set(RECORDS)-PROFILES)}; sobran={sorted(PROFILES-set(RECORDS))}")


def _profile(code: str) -> dict:
    prefix = code[:2]
    topic = TOPICS.get(code, ENGLISH_TOPICS.get(code, ""))
    seed = sum(ord(char) for char in code)
    if prefix == "CN":
        anchor = _science_anchor(code, topic)
    elif prefix == "HI":
        anchor = _history_anchor(code, topic)
    else:
        anchor = _english_anchor(code, topic)
    return {
        "topic": topic, "prior": PRIOR[prefix], "vocabulary": VOCABULARY[prefix],
        "anchor": anchor, "misconception": MISCONCEPTIONS[prefix][seed % 3],
        "focuses": [f"{stage}: {topic}" for stage in STAGES[prefix][:RECORDS[code]['count']]],
    }


def _retarget_links(lesson: dict, prefix: str) -> None:
    old = {"CN": "CN03", "HI": "HI03", "IN": "EN03", "EN": "EN03"}[prefix]
    new = {"CN": "CN2M", "HI": "HI2M", "IN": "IN2M", "EN": "EN2M"}[prefix]
    for link in lesson.get("transversal", []):
        link["code"] = link["code"].replace(old, new)


def build_sequence(code: str) -> dict | None:
    if code not in RECORDS:
        return None
    prefix = code[:2]
    profile = _profile(code)
    lessons = []
    for index in range(len(profile["focuses"])):
        if prefix in {"CN", "HI"}:
            lesson = inquiry_lesson(code, index, profile, "science" if prefix == "CN" else "history")
            inquiry_voice(lesson, profile, index, prefix)
        else:
            maker_code = code.replace("IN2M", "EN2M", 1)
            lesson = applied_lesson(maker_code, index, profile)
            (english_voice if prefix == "IN" else proposal_voice)(lesson, profile, index, prefix)
        _retarget_links(lesson, prefix)
        if prefix == "EN":
            lesson["transversal"] = []
        lessons.append(lesson)
    record = RECORDS[code]
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": (
            f"{profile['topic']} recupera {profile['prior']} y avanza mediante decisiones propias de la disciplina. "
            f"Cada clase cambia fuentes, materiales, representaciones y evidencias, y enfrenta la confusión «{profile['misconception']}»."
        ),
        "prerequisites": profile["prior"], "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"Eje oficial · progresión interna en {len(lessons)} clases"],
            "unit_origin": "Organización pedagógica interna derivada del eje y del OA; no se presenta como una unidad oficial del programa.",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del OA oficial.",
            "source": record["url"],
        },
        "lessons": lessons,
    }


def build_transversal_integration(item: dict) -> dict:
    prepared = dict(item)
    if item["subject_slug"] == "ingles":
        prepared["subject_slug"] = "ingles-propuesta"
    result = base_integration(prepared)
    result["generated_for"] = "2-medio-ciencias-historia-ingles"
    return result


SEQUENCES = {code: True for code in RECORDS}

"""Develop the six remaining eighth-grade subject sequences.

Official objectives and URLs come from the checked-in MINEDUC snapshot. The
topics, classroom anchors, progressions, misconceptions and safeguarding
decisions are original pedagogical elaborations for this repository.
"""
from __future__ import annotations

import json
from pathlib import Path

try:
    from grade_three_arts_pe_english_indigenous_lessons import _lesson as applied_lesson
    from grade_three_music_orientation_technology_lessons import _lesson as mot_lesson
    from grade_four_remaining_lessons import build_transversal_integration as base_integration
    from grade_seven_next_five_lessons import _natural_voice as physical_english_voice
    from grade_seven_remaining_lessons import _natural_voice as remaining_voice
except ImportError:
    from scripts.grade_three_arts_pe_english_indigenous_lessons import _lesson as applied_lesson
    from scripts.grade_three_music_orientation_technology_lessons import _lesson as mot_lesson
    from scripts.grade_four_remaining_lessons import build_transversal_integration as base_integration
    from scripts.grade_seven_next_five_lessons import _natural_voice as physical_english_voice
    from scripts.grade_seven_remaining_lessons import _natural_voice as remaining_voice


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
TARGET_SLUGS = {
    "educacion-fisica-salud", "ingles", "ingles-propuesta",
    "lengua-indigena", "orientacion", "tecnologia",
}

TOPICS = {
    "EF08 OA 01": "Habilidades motrices específicas en deportes y danza",
    "EF08 OA 02": "Estrategias y tácticas para resolver problemas de juego",
    "EF08 OA 03": "Condición física saludable y principios de entrenamiento",
    "EF08 OA 04": "Actividad física regular, autocuidado y seguridad",
    "EF08 OA 05": "Promoción y organización de actividad física comunitaria",
    "IN08 OA 01": "Global and explicit meaning in varied oral texts",
    "IN08 OA 02": "Key language and intelligible sounds in listening",
    "IN08 OA 03": "Purpose, detail, sequence, fact and opinion in listening",
    "IN08 OA 04": "Before, during and after listening strategies",
    "IN08 OA 05": "Coherent multimodal oral presentation",
    "IN08 OA 06": "Planning, repairing and reviewing spoken English",
    "IN08 OA 07": "Personal and critical response to texts",
    "IN08 OA 08": "Communicative functions for interaction",
    "IN08 OA 09": "Global and explicit meaning in print and digital texts",
    "IN08 OA 10": "Critical reading of functional non-literary texts",
    "IN08 OA 11": "Literary reading: theme, character, setting and plot",
    "IN08 OA 12": "Purposeful reading strategies",
    "IN08 OA 13": "Creative multimodal stories and information",
    "IN08 OA 14": "Writing process across short genres",
    "IN08 OA 15": "Writing to inform, narrate and express opinions",
    "IN08 OA 16": "Communicative functions in written English",
    "EN08 OA 01": "Understanding varied literary and functional oral texts",
    "EN08 OA 02": "Purpose, detail and language evidence in listening",
    "EN08 OA 03": "Strategic listening and clarification",
    "EN08 OA 04": "Integrated literary and non-literary reading",
    "EN08 OA 05": "Reading language functions in meaningful contexts",
    "EN08 OA 06": "Strategic reading before, during and after the text",
    "EN08 OA 07": "Supported response and connection across texts",
    "EN08 OA 08": "Audience-aware multimodal oral presentation",
    "EN08 OA 09": "Strategies for clear and fluent interaction",
    "EN08 OA 10": "Language functions in conversation and presentation",
    "EN08 OA 11": "Short multimodal texts for real audiences",
    "EN08 OA 12": "Language functions in written texts",
    "EN08 OA 13": "Independent writing process and publication",
    "LI08 OF A": "Creación y recreación de relatos de tradición oral",
    "LI08 OF B": "Interacción respetuosa en espacios formales, informales y rituales",
    "LI08 OF C": "Expresión oral situada en diversas situaciones",
    "LI08 OF D": "Lenguas como expresión viva de culturas",
    "LI08 OF E": "Diversidad lingüística, cultural e interculturalidad",
    "LI08 OF F": "Lectura del contexto social indígena actual",
    "LI08 OF G": "Lectura de autorías indígenas contemporáneas",
    "LI08 OF H": "Escritura sobre cultura y lengua en contexto intercultural",
    "LI08 OF I": "Investigación responsable de la tradición oral",
    "OR08 OA 01": "Autoconcepto positivo en pubertad y adolescencia",
    "OR08 OA 02": "Sexualidad integral, intimidad, respeto y fuentes confiables",
    "OR08 OA 03": "Prevención de riesgos y búsqueda de ayuda",
    "OR08 OA 04": "Bienestar cotidiano, vida saludable y seguridad digital",
    "OR08 OA 05": "Derechos y bienestar en relaciones presenciales y virtuales",
    "OR08 OA 06": "Resolución dialogada, empática y no violenta de conflictos",
    "OR08 OA 07": "Intereses compartidos, colaboración y metas comunes",
    "OR08 OA 08": "Acuerdos y participación democrática del curso",
    "OR08 OA 09": "Intereses, aprendizaje y proyectos personales",
    "OR08 OA 10": "Metas progresivas y gestión autónoma del aprendizaje",
    "TE08 OA 01": "Oportunidades locales para crear productos tecnológicos",
    "TE08 OA 02": "Diseño sustentable y creación con herramientas TIC",
    "TE08 OA 03": "Evaluación técnica y mejora de productos",
    "TE08 OA 04": "Comunicación ética del proceso tecnológico",
    "TE08 OA 05": "Análisis de soluciones, destinatarios y funcionamiento",
    "TE08 OA 06": "Impactos éticos, ambientales y sociales de la tecnología",
}

STAGES = {
    "EF": ("Explorar con seguridad", "Seleccionar una respuesta motriz", "Combinar habilidades o decisiones", "Aplicar en una situación real", "Evaluar y ajustar", "Transferir con autonomía"),
    "IN": ("Recognize purpose and context", "Locate precise evidence", "Use a strategy or language function", "Communicate through an information gap", "Respond independently", "Review and transfer"),
    "EN": ("Recognize purpose and context", "Locate precise evidence", "Model a useful strategy", "Communicate through an information gap", "Respond independently", "Review and transfer"),
    "LI": ("Situar pueblo, territorio y fuente", "Escuchar o leer con límites declarados", "Reconocer relaciones culturales", "Construir una respuesta atribuida", "Contrastar sin jerarquizar", "Comunicar con validación pertinente"),
    "OR": ("Examinar un caso ficticio protegido", "Distinguir hechos, emociones, derechos y límites", "Comparar opciones y consecuencias", "Elegir una acción segura", "Practicar comunicación o búsqueda de ayuda", "Transferir sin exposición personal"),
    "TE": ("Definir necesidad, usuario y criterio", "Investigar soluciones y restricciones", "Representar y planificar", "Implementar con seguridad", "Probar con evidencia", "Mejorar y comunicar impactos"),
}

PRIOR = {
    "EF": "seleccionar habilidades, regular el esfuerzo y participar con seguridad e inclusión en 7° básico",
    "IN": "understand and produce increasingly connected messages for a purpose in 7th grade",
    "EN": "understand and produce increasingly connected messages for a purpose in 7th grade",
    "LI": "aprender desde territorio, oralidad y fuentes pertinentes, sin inventar lengua ni suplantar autoridades culturales",
    "OR": "analizar decisiones, derechos, autocuidado y participación mediante casos protegidos de 7° básico",
    "TE": "definir necesidades, diseñar, probar y evaluar soluciones tecnológicas en 7° básico",
}

VOCABULARY = {
    "EF": "habilidad motriz, estrategia, táctica, frecuencia, intensidad, recuperación, progresión, seguridad, inclusión, autorregulación",
    "IN": "purpose, audience, gist, detail, clue, sequence, interaction, function, evidence, revision",
    "EN": "purpose, audience, gist, detail, clue, sequence, interaction, function, evidence, revision",
    "LI": "territorio, oralidad, fuente, autorización, variante, autoría, reciprocidad, interculturalidad, revitalización",
    "OR": "dignidad, derecho, intimidad, consentimiento, riesgo, autocuidado, consecuencia, apoyo, acuerdo, participación",
    "TE": "necesidad, usuario, criterio, restricción, eficiencia, sustentabilidad, prototipo, prueba, impacto, mejora",
}

MISCONCEPTIONS = {
    "EF": ("confundir dominio con velocidad o competencia", "usar una misma carga o variante para todo el curso", "evaluar solo el resultado y no la decisión, regulación o seguridad"),
    "IN": ("translate every word before constructing meaning", "recite a model without attending to audience or response", "treat accent, speed or immediate accuracy as intelligence"),
    "EN": ("translate every word before constructing meaning", "recite a model without attending to audience or response", "treat accent, speed or immediate accuracy as intelligence"),
    "LI": ("inventar lengua, grafías, símbolos o explicaciones espirituales", "generalizar una fuente a todos los pueblos o territorios", "divulgar relatos, imágenes o saberes sin autorización"),
    "OR": ("pedir experiencias personales para demostrar aprendizaje", "moralizar, culpar o diagnosticar a una persona", "resolver seguridad mediante secreto, obediencia o exposición pública"),
    "TE": ("construir antes de definir necesidad y criterios", "evaluar solo apariencia o funcionamiento inmediato", "usar herramientas, imágenes o datos sin revisar seguridad, privacidad y autoría"),
}


def _dose_count(text: str, slug: str, readings: list) -> int:
    lowered = text.lower()
    count = 4
    if len(text) > 260 or lowered.count(";") >= 2:
        count += 1
    if any(verb in lowered for verb in ("investigar", "crear", "producir", "diseñar", "evaluar", "analizar", "argumentar", "interpretar")):
        count += 1
    if readings or ("leng" in slug and any(verb in lowered for verb in ("leer", "escribir", "obra", "texto"))):
        count += 1
    return min(count, 7)


RECORDS = {}
for record in SNAPSHOT["records"]:
    if record["course_order"] != 8 or record["subject_slug"] not in TARGET_SLUGS:
        continue
    for objective in record["objectives"]:
        if objective["code"].startswith("de "):
            continue
        RECORDS[objective["code"]] = {
            "slug": record["subject_slug"], "description": objective["description"],
            "url": objective["url"],
            "count": _dose_count(objective["description"], record["subject_slug"], objective.get("readings", [])),
        }

if set(RECORDS) != set(TOPICS):
    raise RuntimeError(f"Perfiles restantes de 8° desalineados: faltan={sorted(set(RECORDS)-set(TOPICS))}; sobran={sorted(set(TOPICS)-set(RECORDS))}")


def _anchor(code: str, topic: str) -> str:
    prefix = code[:2]
    if prefix == "EF":
        return {
            "EF08 OA 01": "estaciones accesibles de atletismo, oposición, colaboración, oposición-colaboración y danza, con variantes equivalentes",
            "EF08 OA 02": "juegos reducidos con mapas de espacio, reglas modificables y registro de decisiones tácticas",
            "EF08 OA 03": "circuito autorregulado, escala de esfuerzo percibido, tiempos de trabajo y recuperación y ficha FITT",
            "EF08 OA 04": "plan semanal ficticio, calentamiento, hidratación, rutas seguras y alternativas de actividad en distintos entornos",
            "EF08 OA 05": "consulta anónima de intereses, mapa de recursos del entorno y plan accesible para una jornada activa escolar",
        }[code]
    if prefix in {"IN", "EN"}:
        number = int(code.rsplit(" ", 1)[-1])
        if number <= 4:
            return "an original teacher-read audio, replay plan, listening grid and transcript released only after listening"
        if prefix == "IN" and number <= 8 or prefix == "EN" and number in {7, 8, 9, 10}:
            return "fictional information-gap cards, useful chunks, audience roles and a paper storyboard"
        if prefix == "IN" and number <= 12 or prefix == "EN" and number <= 6:
            return "short authorized literary and functional texts with numbered paragraphs, visuals and an essential glossary"
        return "fictional writing briefs, genre models, audience cards and a meaning-first revision checklist"
    if prefix == "LI":
        return f"fuentes autorizadas y situadas por pueblo, territorio, autoría y condiciones de circulación para {topic.lower()}"
    if prefix == "OR":
        return f"casos ficticios, tarjetas de derechos, rutas de apoyo y protocolos escolares para {topic.lower()}"
    return f"un desafío local documentado, ficha de usuario, materiales disponibles, criterios de prueba y matriz de impacto para {topic.lower()}"


def _profile(code: str) -> dict:
    prefix = code[:2]
    topic = TOPICS[code]
    count = RECORDS[code]["count"]
    seed = sum(ord(char) for char in code)
    return {
        "topic": topic, "prior": PRIOR[prefix], "vocabulary": VOCABULARY[prefix],
        "anchor": _anchor(code, topic), "misconception": MISCONCEPTIONS[prefix][seed % 3],
        "focuses": [f"{stage}: {topic}" for stage in STAGES[prefix][:count]],
    }


def _retarget_links(lesson: dict, prefix: str) -> None:
    if prefix == "LI":
        lesson["transversal"] = []
        return
    old = {"EF": "EF03", "IN": "EN03", "EN": "EN03", "OR": "OR03", "TE": "TE03"}[prefix]
    new = {"EF": "EF08", "IN": "IN08", "EN": "EN08", "OR": "OR08", "TE": "TE08"}[prefix]
    for link in lesson.get("transversal", []):
        link["code"] = link["code"].replace(old, new)


def build_sequence(code: str) -> dict | None:
    if code not in RECORDS:
        return None
    prefix = code[:2]
    profile = _profile(code)
    lessons = []
    for index in range(len(profile["focuses"])):
        if prefix in {"EF", "IN", "EN", "LI"}:
            maker_code = code.replace("IN08", "EN08", 1).replace("LI08", "LC08", 1)
            lesson = applied_lesson(maker_code, index, profile)
        else:
            lesson = mot_lesson(code, index, profile)
        _retarget_links(lesson, prefix)
        if prefix in {"EF", "IN"}:
            physical_english_voice(lesson, profile, index, prefix)
        else:
            remaining_voice(lesson, profile, index, prefix)
        lessons.append(lesson)
    record = RECORDS[code]
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": (
            f"{profile['topic']} parte de {profile['prior']} y avanza con decisiones propias de la disciplina. "
            f"Cada clase cambia situaciones, fuentes, recursos y evidencias, y enfrenta la confusión «{profile['misconception']}»."
        ),
        "prerequisites": profile["prior"], "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"Eje oficial · progresión interna en {len(lessons)} clases"],
            "unit_origin": "Organización pedagógica interna derivada del eje y del objetivo; no se presenta como una unidad oficial del programa.",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del objetivo oficial.",
            "source": record["url"],
        },
        "lessons": lessons,
    }


def build_transversal_integration(item: dict) -> dict:
    prepared = dict(item)
    if item["subject_slug"] == "ingles":
        prepared["subject_slug"] = "ingles-propuesta"
    result = base_integration(prepared)
    result["generated_for"] = "8-basico-remaining"
    return result


SEQUENCES = {code: True for code in RECORDS}

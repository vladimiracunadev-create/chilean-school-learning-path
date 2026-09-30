"""Specific fifth-grade sequences for the nine remaining curriculum labels.

Each OA receives a named disciplinary focus, a concrete classroom anchor and a
misconception to address.  Shared lesson protocols provide a stable structure;
the content, evidence and progression remain specific to the OA.
"""
from __future__ import annotations

try:
    from grade_three_arts_pe_english_indigenous_lessons import _lesson as apei_lesson
    from grade_three_music_orientation_technology_lessons import _lesson as mot_lesson
    from grade_three_science_history_lessons import _lesson as history_lesson
    from grade_four_remaining_lessons import build_transversal_integration as base_integration
except ImportError:
    from scripts.grade_three_arts_pe_english_indigenous_lessons import _lesson as apei_lesson
    from scripts.grade_three_music_orientation_technology_lessons import _lesson as mot_lesson
    from scripts.grade_three_science_history_lessons import _lesson as history_lesson
    from scripts.grade_four_remaining_lessons import build_transversal_integration as base_integration


COUNTS = {
    "AR": [6, 5, 6, 5, 5],
    "EF": [5, 5, 4, 4, 4, 4, 4, 4, 5, 5, 5],
    "HI": [5, 5, 5, 5, 4, 4, 5, 4, 4, 5, 6, 6, 4, 5, 4, 5, 5, 6, 5, 5, 5, 4],
    "IN": [5, 5, 5, 4, 5, 5, 5, 4, 5, 5, 4, 5, 4, 5, 5, 5],
    "EN": [4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 5, 4, 5, 5],
    "MU": [5, 4, 5, 4, 5, 4, 4, 4],
    "OR": [4, 4, 5, 5, 4, 5, 4, 5, 5],
    "TE": [6, 5, 5, 5, 5, 5, 4],
}

LC_COUNTS = {
    "LF01": 6, "LF02": 4, "LF03": 5, "LF04": 5, "LF05": 4, "LF06": 5,
    "LR01": 6, "LR02": 4, "LR03": 5, "LR04": 4, "LR05": 4, "LR06": 6,
    "LS01": 5, "LS02": 4, "LS03": 5, "LS04": 4, "LS05": 4, "LS06": 6,
    "07": 4, "08": 4, "09": 4, "10": 6, "11": 4, "12": 6, "13": 4,
    "14": 4, "15": 4, "16": 4, "17": 5,
}

SUBJECTS = {
    "AR": ("artes-visuales", "Artes Visuales"),
    "EF": ("educacion-fisica-salud", "Educación Física y Salud"),
    "HI": ("historia-geografia-ciencias-sociales", "Historia, Geografía y Ciencias Sociales"),
    "IN": ("ingles", "Inglés"),
    "EN": ("ingles-propuesta", "Inglés (Propuesta)"),
    "LC": ("lengua-cultura-pueblos-originarios-ancestrales", "Lengua y Cultura de los Pueblos Originarios Ancestrales"),
    "MU": ("musica", "Música"),
    "OR": ("orientacion", "Orientación"),
    "TE": ("tecnologia", "Tecnología"),
}

TOPICS = {
    "AR": [
        "Creación visual desde Chile, sus paisajes y diseños",
        "Color complementario, formas, luz y sombra",
        "Dominio de materiales, herramientas y medios digitales",
        "Interpretación de obras y diseños en contexto",
        "Comparación y mejora de producciones visuales",
    ],
    "EF": [
        "Habilidades motrices aplicadas a actividades deportivas", "Tácticas para resolver problemas de juego",
        "Estrategias ofensivas y defensivas", "Actividad física y cuidado de espacios diversos",
        "Danzas nacionales con contexto y coordinación", "Condición física y metas personales seguras",
        "Planificación regular de actividad física", "Pulso y percepción de intensidad",
        "Higiene, postura, hidratación y vida saludable", "Responsabilidad, liderazgo y respeto en el juego",
        "Calentamiento, materiales y procedimientos seguros",
    ],
    "HI": [
        "Viajes de exploración, navegación y contexto europeo", "Conquista de América y Chile desde múltiples actores",
        "Consecuencias de la conquista en Europa y América", "Efectos de la conquista sobre pueblos indígenas",
        "Vida cotidiana y sociedad colonial en Chile", "Dependencia colonial, Iglesia y sociedad mestiza",
        "Relaciones hispano-mapuche durante la Colonia", "Patrimonio colonial presente en Chile",
        "Grandes zonas naturales y paisajes de Chile", "Recursos naturales y desarrollo sostenible",
        "Trabajo, tecnología y valor de los recursos", "Riesgos naturales y protección comunitaria",
        "Personas como sujetos de derechos", "Derechos, deberes y responsabilidades del Estado",
        "Esfuerzo, mérito y reconocimiento sin confundirlos con derechos", "Actitudes cívicas en la vida cotidiana",
        "Elección responsable de una directiva de curso", "Proyecto escolar con plan y presupuesto",
        "Organizaciones para resolver problemas comunes", "Opinión argumentada con fundamentos",
        "Evaluación y elección de soluciones", "Información y opinión sobre asuntos públicos",
    ],
    "IN": [
        "Listening for explicit meaning in familiar contexts", "Listening for topic, details and sound patterns",
        "Prediction and contextual clues in audiovisual listening", "Personal and creative response to listening",
        "Reading simple texts for communicative functions", "Reading purpose, main ideas and explicit information",
        "Reading literary sequence, setting and characters", "Personal response and connections after reading",
        "Before, during and after reading strategies", "Sounds of English through songs, rhymes and dialogue",
        "Supported oral interaction and presentation", "Dialogues for everyday communicative functions",
        "Everyday vocabulary, frequent words and expressions", "Model-supported literary and functional writing",
        "Writing for everyday communicative functions", "Planning, drafting, revising and publishing in English",
    ],
    "EN": [
        "Listening comprehension across familiar and global themes", "Listening for purpose, ideas and specific information",
        "Strategies for audiovisual listening", "Response and connection after listening",
        "Reading literary and non-literary texts", "Reading communicative functions in context",
        "Purposeful reading strategies", "Multimodal response to reading",
        "English sounds through oral texts", "Supported oral communication",
        "Vocabulary for the functions of the level", "Dialogues about ability, quantity, time and actions",
        "Model-supported literary and functional texts", "Writing for the functions of the level",
        "Writing process with digital and reference tools",
    ],
    "MU": [
        "Musical language and expressive purpose", "Elaborated response to musical experience",
        "Abundant listening across American musical cultures", "Singing and instrumental ensemble performance",
        "Improvisation and creation with musical purpose", "Responsible and musical presentation",
        "Music and the context in which it emerges", "Reflection and improvement in musical work",
    ],
    "OR": [
        "Positive self-appraisal, strengths and growth", "Emotions, expression and impact on others",
        "Affective and sexual development during puberty", "Autonomous self-care, intimacy and digital safety",
        "Prevention and response to substance use", "Solidarity, respect and rejection of violence",
        "Autonomous strategies for resolving conflicts", "Democratic participation and course organization",
        "Perseverance, honest study and learning goals",
    ],
    "TE": [
        "Design of technological objects and systems", "Planning with resources, safety and impacts",
        "Safe elaboration with tools and materials", "Testing quality through technical and environmental criteria",
        "Presentations and spreadsheets for communicating research", "Word processing for purposeful documents",
        "Online communication, source safety and privacy",
    ],
}

LC_TOPICS = {
    "LF01": "Relatos fundacionales en lengua indígena", "LF02": "Diálogo y exposición en lengua indígena",
    "LF03": "Textos culturales, familiares y territoriales", "LF04": "Escritura, aglutinación y reduplicación",
    "LF05": "Características y formación de palabras", "LF06": "Registro tecnológico autorizado en lengua indígena",
    "LR01": "Relatos fundacionales con expresiones culturalmente significativas", "LR02": "Diálogo cultural con vocabulario pertinente",
    "LR03": "Lectura cultural con palabras significativas", "LR04": "Mensajes situados con frases breves",
    "LR05": "Usos comunitarios y revitalización lingüística", "LR06": "Registro tecnológico situado y autorizado",
    "LS01": "Comprensión de relatos fundacionales", "LS02": "Conversación cultural con palabras significativas",
    "LS03": "Textos del territorio y elementos culturales", "LS04": "Mensajes con expresiones culturalmente significativas",
    "LS05": "Lengua, comunidad e identidad", "LS06": "Registro tecnológico con límites comunitarios",
    "07": "Territorio, visión de mundo e identidades", "08": "Historias de pueblos indígenas en relación",
    "09": "Diversidad lingüística y diálogo intercultural", "10": "Relatos fundacionales y origen del mundo",
    "11": "Personas portadoras de saberes ancestrales", "12": "Eventos socioculturales y ceremoniales",
    "13": "Valores comunitarios y espirituales", "14": "Técnicas productivas y equilibrio con la naturaleza",
    "15": "Patrimonio cultural y natural", "16": "Ser humano, naturaleza, cosmos y ciencia",
    "17": "Manifestaciones artísticas y cosmovisión indígena",
}

STAGES = {
    "AR": ["Observar y formular una intención", "Explorar una variable visual", "Elegir materiales y procedimientos", "Crear una respuesta propia", "Interpretar y fundamentar", "Revisar sin perder autoría"],
    "EF": ["Reconocer meta y condiciones de seguridad", "Modelar control y decisión motriz", "Ensayar con variantes accesibles", "Resolver una situación nueva", "Regular esfuerzo y explicar el ajuste", "Transferir a otro juego o entorno"],
    "HI": ["Ubicar en tiempo y espacio", "Interrogar fuentes y reconocer procedencia", "Relacionar causas, actores y consecuencias", "Comparar perspectivas o territorios", "Argumentar con evidencia", "Evaluar una decisión ciudadana"],
    "IN": ["Notice purpose and context", "Locate words, chunks and clues", "Model a communicative strategy", "Interact or compose with support", "Communicate independently", "Check meaning and revise"],
    "EN": ["Notice purpose and context", "Locate words, chunks and clues", "Model a communicative strategy", "Interact or compose with support", "Communicate independently", "Check meaning and revise"],
    "LC": ["Situar pueblo, territorio y fuente", "Escuchar o leer con límites declarados", "Reconocer relaciones culturales", "Construir una respuesta atribuida", "Contrastar sin jerarquizar", "Comunicar y revisar con validación pertinente"],
    "MU": ["Escuchar antes de nombrar", "Reconocer y representar un rasgo audible", "Interpretar o crear con un criterio", "Ensayar y ajustar desde la escucha", "Comunicar una decisión musical", "Reflexionar y transferir"],
    "OR": ["Examinar un caso ficticio protegido", "Distinguir hechos, emociones y límites", "Comparar opciones y consecuencias", "Elegir una acción segura", "Practicar comunicación o solicitud de ayuda", "Transferir sin exposición personal"],
    "TE": ["Definir necesidad, usuario y criterio", "Representar una solución", "Planificar recursos y seguridad", "Elaborar o configurar", "Probar con evidencia", "Mejorar y comunicar"],
}

PRIOR = {
    "AR": "crear, apreciar y revisar producciones visuales desarrolladas en 4° básico",
    "EF": "combinar habilidades motrices, autocuidado y juego limpio desarrollados en 4° básico",
    "HI": "leer mapas, secuencias, fuentes y situaciones ciudadanas trabajadas en 4° básico",
    "IN": "comprender y producir mensajes breves con apoyos visuales y lingüísticos",
    "EN": "comprender y producir mensajes breves con apoyos visuales y lingüísticos",
    "LC": "aprender desde territorio, oralidad y fuentes comunitarias pertinentes, sin inventar lengua",
    "MU": "escuchar, interpretar, crear y comentar música con criterios audibles de 4° básico",
    "OR": "reconocer emociones, derechos, autocuidado y participación sin exposición personal",
    "TE": "diseñar, elaborar, probar y comunicar soluciones tecnológicas de 4° básico",
}

VOCABULARY = {
    "AR": "intención, referente, lenguaje visual, material, procedimiento, contexto, criterio, revisión",
    "EF": "control, estrategia, intensidad, seguridad, cooperación, regulación, evidencia, autocuidado",
    "HI": "fuente, contexto, actor, territorio, causa, consecuencia, perspectiva, argumento",
    "IN": "purpose, audience, clue, key word, chunk, interaction, meaning, revision",
    "EN": "purpose, audience, clue, key word, chunk, interaction, meaning, revision",
    "LC": "territorio, oralidad, fuente, autorización, variante, identidad, reciprocidad, revitalización",
    "MU": "pulso, ritmo, melodía, timbre, dinámica, forma, interpretación, creación",
    "OR": "dignidad, emoción, límite, autocuidado, consecuencia, apoyo, acuerdo, participación",
    "TE": "necesidad, usuario, criterio, restricción, herramienta, prueba, seguridad, impacto",
}


def _suffix(code: str) -> str:
    return code.split(" OA ", 1)[1]


def _count(code: str) -> int:
    prefix, suffix = code[:2], _suffix(code)
    return LC_COUNTS[suffix] if prefix == "LC" else COUNTS[prefix][int(suffix) - 1]


def _topic(code: str) -> str:
    prefix, suffix = code[:2], _suffix(code)
    return LC_TOPICS[suffix] if prefix == "LC" else TOPICS[prefix][int(suffix) - 1]


def _anchor(prefix: str, topic: str) -> str:
    templates = {
        "AR": "referentes atribuidos, obras, pruebas de taller y materiales vinculados con {topic}",
        "EF": "estaciones, reglas visibles, implementos seguros y variantes accesibles para {topic}",
        "HI": "mapas, fuentes primarias o secundarias, datos y casos situados sobre {topic}",
        "IN": "short authorized oral, visual and written texts designed for {topic}",
        "EN": "short authorized oral, visual and written texts designed for {topic}",
        "LC": "fuentes autorizadas y situadas por pueblo y territorio para {topic}",
        "MU": "registros autorizados, partituras gráficas e instrumentos disponibles para {topic}",
        "OR": "casos ficticios, opciones de respuesta y protocolos escolares vinculados con {topic}",
        "TE": "un desafío documentado, materiales o software disponible y criterios previos para {topic}",
    }
    return templates[prefix].format(topic=topic.lower())


def _misconception(prefix: str, topic: str, number: int) -> str:
    patterns = {
        "AR": ["copiar referentes sin una intención propia", "evaluar sólo por gusto o parecido", "usar técnicas sin relacionarlas con el efecto"],
        "EF": ["priorizar velocidad o resultado sobre control y seguridad", "comparar cuerpos o rendimiento entre estudiantes", "aplicar una táctica sin leer espacio, reglas y compañeros"],
        "HI": ["tratar una fuente como verdad completa", "juzgar el pasado sólo desde el presente", "generalizar un caso a todos los actores o territorios"],
        "IN": ["translate every word before communicating", "recite a model without attending to meaning", "treat accent or immediate accuracy as intelligence"],
        "EN": ["translate every word before communicating", "recite a model without attending to meaning", "treat accent or immediate accuracy as intelligence"],
        "LC": ["inventar lengua o explicaciones culturales", "generalizar una fuente a todos los pueblos", "divulgar saberes o registros sin autorización"],
        "MU": ["describir sólo el gusto sin evidencia audible", "confundir precisión con volumen o velocidad", "presentar una música como representación total de una cultura"],
        "OR": ["solicitar experiencias personales para demostrar aprendizaje", "moralizar o diagnosticar a una persona", "resolver seguridad mediante secreto, culpa u obediencia"],
        "TE": ["construir antes de definir criterios", "evaluar sólo apariencia", "usar herramientas o datos sin revisar seguridad y privacidad"],
    }
    return f"en {topic.lower()}, {patterns[prefix][(number - 1) % len(patterns[prefix])] }"


def _profile(code: str) -> dict:
    prefix = code[:2]
    suffix = _suffix(code)
    number = int(suffix) if suffix.isdigit() else list(LC_COUNTS).index(suffix) + 1
    topic = _topic(code)
    count = _count(code)
    return {
        "topic": topic,
        "prior": PRIOR[prefix],
        "vocabulary": VOCABULARY[prefix],
        "anchor": _anchor(prefix, topic),
        "misconception": _misconception(prefix, topic, number),
        "focuses": [f"{stage} · {topic}" for stage in STAGES[prefix][:count]],
    }


def _fix_links(lesson: dict, prefix: str) -> dict:
    for link in lesson.get("transversal", []):
        for old in ("AR03", "EF03", "EN03", "LC03", "HI03", "MU03", "OR03", "TE03"):
            link["code"] = link["code"].replace(old, f"{prefix}05")
    return lesson


def build_sequence(code: str) -> dict | None:
    prefix = code[:2]
    if prefix not in SUBJECTS or code[2:4] != "05" or " OA " not in code or code.startswith("de "):
        return None
    if prefix == "LC" and _suffix(code) not in LC_COUNTS:
        return None
    if prefix != "LC" and (not _suffix(code).isdigit() or int(_suffix(code)) > len(COUNTS[prefix])):
        return None
    profile = _profile(code)
    lessons = []
    for index, focus in enumerate(profile["focuses"]):
        if prefix == "HI":
            lesson = history_lesson(code, index, profile, "history")
        elif prefix in {"MU", "OR", "TE"}:
            lesson = mot_lesson(code, index, profile)
        else:
            maker_code = code if prefix != "IN" else code.replace("IN05", "EN05", 1)
            lesson = apei_lesson(maker_code, index, profile)
        lesson = _fix_links(lesson, prefix)
        focus_lower = focus.lower()
        lesson["guided"] += f" La retroalimentación vuelve al criterio propio de «{focus_lower}» antes del segundo intento."
        lesson["independent"] += f" La evidencia se juzga por el logro de «{focus_lower}», no por imitar el ejemplo."
        lesson["ticket"] += f" La respuesta final debe permitir comprobar «{focus_lower}»."
        lessons.append(lesson)
    slug, _ = SUBJECTS[prefix]
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
            "source": f"https://www.curriculumnacional.cl/curriculum/1o-6o-basico/{slug}/5-basico/{code.lower().replace(' ', '-')}",
        },
        "lessons": lessons,
    }


def build_transversal_integration(item: dict) -> dict:
    prepared = dict(item)
    if item["subject_slug"] == "ingles":
        prepared["subject_slug"] = "ingles-propuesta"
    result = base_integration(prepared)
    result["generated_for"] = "5-basico"
    return result


SEQUENCES = {
    f"{prefix}05 OA {number:02d}": True
    for prefix, counts in COUNTS.items()
    for number in range(1, len(counts) + 1)
}
SEQUENCES.update({f"LC05 OA {suffix}": True for suffix in LC_COUNTS})

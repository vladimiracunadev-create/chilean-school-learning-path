"""Developed seventh-grade sequences for the five remaining denominations.

The official OA text and URLs come from the checked-in MINEDUC snapshot.  The
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
except ImportError:
    from scripts.grade_three_arts_pe_english_indigenous_lessons import _lesson as applied_lesson
    from scripts.grade_three_music_orientation_technology_lessons import _lesson as mot_lesson
    from scripts.grade_four_remaining_lessons import build_transversal_integration as base_integration


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
TARGET_SLUGS = {"ingles-propuesta", "lengua-indigena", "musica", "orientacion", "tecnologia"}


TOPICS = {
    # Inglés (Propuesta)
    "EN07 OA 01": "Comprensión global de textos orales simples",
    "EN07 OA 02": "Información explícita y relaciones en textos orales",
    "EN07 OA 03": "Estrategias antes, durante y después de escuchar",
    "EN07 OA 04": "Comprensión de textos literarios y no literarios",
    "EN07 OA 05": "Lectura de temas cercanos, actuales e interculturales",
    "EN07 OA 06": "Estrategias de lectura con propósito",
    "EN07 OA 07": "Respuesta personal fundamentada a textos",
    "EN07 OA 08": "Presentación oral multimodal",
    "EN07 OA 09": "Interacción y reparación del significado",
    "EN07 OA 10": "Funciones comunicativas en conversaciones y exposiciones",
    "EN07 OA 11": "Escritura breve según género, modelo y criterio",
    "EN07 OA 12": "Funciones comunicativas en textos escritos",
    "EN07 OA 13": "Proceso de escritura para informar, opinar y narrar",
    # Lengua indígena
    "LI07 OF A": "Relatos indígenas tradicionales y sus actualizaciones",
    "LI07 OF B": "Prácticas discursivas formales e informales situadas",
    "LI07 OF C": "Expresión oral según situación comunicativa",
    "LI07 OF D": "Análisis de situaciones interculturales",
    "LI07 OF E": "Lengua indígena como expresión cultural viva",
    "LI07 OF F": "Lectura de textos tradicionales y actuales",
    "LI07 OF G": "Escritura sobre vivencias familiares y sociales",
    "LI07 OF H": "Producción escrita de relatos culturalmente situados",
    # Música
    "MU07 OA 01": "Escucha, sensaciones e ideas en músicas de Chile y el mundo",
    "MU07 OA 02": "Lenguaje musical y procedimientos compositivos audibles",
    "MU07 OA 03": "Interpretación vocal e instrumental expresiva",
    "MU07 OA 04": "Interpretación a una y más voces con medios de registro",
    "MU07 OA 05": "Improvisación, ambientación y creación musical",
    "MU07 OA 06": "Fortalezas y áreas de crecimiento musical",
    "MU07 OA 07": "Música, sociedad, contextos y personas que la cultivan",
    # Orientación
    "OR07 OA 01": "Autoconcepto positivo, intereses y capacidades",
    "OR07 OA 02": "Sexualidad integral, cuidado y respeto",
    "OR07 OA 03": "Riesgos, presión social y decisiones de protección",
    "OR07 OA 04": "Bienestar y vida saludable en la comunidad escolar",
    "OR07 OA 05": "Relaciones presenciales y virtuales basadas en derechos",
    "OR07 OA 06": "Resolución dialogada y no violenta de conflictos",
    "OR07 OA 07": "Necesidades compartidas y colaboración",
    "OR07 OA 08": "Acuerdos y participación democrática del curso",
    "OR07 OA 09": "Intereses, aprendizaje y proyecto personal",
    "OR07 OA 10": "Metas progresivas y gestión autónoma del aprendizaje",
    # Tecnología
    "TE07 OA 01": "Necesidades de reparación, adaptación o mejora",
    "TE07 OA 02": "Diseño e implementación eficiente de soluciones",
    "TE07 OA 03": "Evaluación técnica de soluciones implementadas",
    "TE07 OA 04": "Comunicación de procesos mediante herramientas TIC",
    "TE07 OA 05": "Contraste de soluciones tecnológicas y contextos",
    "TE07 OA 06": "Efectos sociales y ambientales de la tecnología",
}

STAGES = {
    "EN": (
        "Recognize purpose and context", "Locate useful clues", "Model a comprehension or communication strategy",
        "Practice through a genuine information gap", "Communicate independently", "Check meaning and revise",
    ),
    "LI": (
        "Situar pueblo, territorio y fuente", "Escuchar o leer con límites declarados", "Reconocer relaciones culturales",
        "Construir una respuesta atribuida", "Contrastar sin jerarquizar", "Comunicar con validación pertinente",
    ),
    "MU": (
        "Escuchar antes de nombrar", "Reconocer un rasgo audible", "Relacionar lenguaje musical y efecto",
        "Interpretar o crear con criterio", "Ensayar y ajustar desde la escucha", "Comunicar y reflexionar",
    ),
    "OR": (
        "Examinar un caso ficticio protegido", "Distinguir hechos, emociones, derechos y límites", "Comparar opciones y consecuencias",
        "Elegir una acción segura", "Practicar comunicación o búsqueda de ayuda", "Transferir sin exposición personal",
    ),
    "TE": (
        "Definir necesidad, usuario y criterio", "Investigar soluciones y restricciones", "Representar y planificar",
        "Implementar con seguridad", "Probar con evidencia", "Mejorar y comunicar impactos",
    ),
}

PRIOR = {
    "EN": "understand and produce short messages with increasing independence in 6th grade",
    "LI": "aprender desde territorio, oralidad y fuentes pertinentes, sin inventar lengua ni suplantar autoridades culturales",
    "MU": "escuchar, interpretar, crear y comentar música con criterios audibles trabajados en 6° básico",
    "OR": "reconocer derechos, emociones, autocuidado y participación mediante situaciones protegidas de 6° básico",
    "TE": "definir necesidades, diseñar, elaborar y probar soluciones tecnológicas en 6° básico",
}

VOCABULARY = {
    "EN": "purpose, audience, gist, detail, clue, chunk, interaction, function, evidence, revision",
    "LI": "territorio, oralidad, fuente, autorización, variante, identidad, reciprocidad, interculturalidad, revitalización",
    "MU": "pulso, ritmo, melodía, armonía, timbre, textura, dinámica, forma, interpretación, creación",
    "OR": "dignidad, derecho, emoción, límite, consentimiento, autocuidado, consecuencia, apoyo, acuerdo, participación",
    "TE": "necesidad, usuario, criterio, restricción, recurso, prototipo, prueba, eficiencia, impacto, mejora",
}

MISCONCEPTIONS = {
    "EN": (
        "translate every word before constructing meaning",
        "recite a model without attending to audience or response",
        "treat accent, speed or immediate accuracy as intelligence",
    ),
    "LI": (
        "inventar lengua, grafías, símbolos o explicaciones espirituales",
        "generalizar una fuente a todos los pueblos, territorios o personas",
        "divulgar relatos, imágenes o saberes sin autorización",
    ),
    "MU": (
        "describir sólo gusto sin evidencia audible",
        "confundir precisión con volumen, velocidad o uniformidad",
        "presentar una música como representación total de una cultura",
    ),
    "OR": (
        "pedir experiencias personales para demostrar aprendizaje",
        "moralizar, culpar o diagnosticar a una persona",
        "resolver seguridad mediante secreto, obediencia o exposición pública",
    ),
    "TE": (
        "construir antes de definir necesidad y criterios",
        "evaluar sólo apariencia o funcionamiento inmediato",
        "usar herramientas, imágenes o datos sin revisar seguridad, privacidad y autoría",
    ),
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
    if record["course_order"] != 7 or record["subject_slug"] not in TARGET_SLUGS:
        continue
    for objective in record["objectives"]:
        if objective["code"].startswith("de "):
            continue
        RECORDS[objective["code"]] = {
            "slug": record["subject_slug"],
            "description": objective["description"],
            "url": objective["url"],
            "count": _dose_count(objective["description"], record["subject_slug"], objective.get("readings", [])),
        }

missing_topics = sorted(set(RECORDS) - set(TOPICS))
extra_topics = sorted(set(TOPICS) - set(RECORDS))
if missing_topics or extra_topics:
    raise RuntimeError(f"Perfiles restantes de 7° desalineados: faltan={missing_topics}; sobran={extra_topics}")


def _anchor(code: str, topic: str) -> str:
    prefix = code[:2]
    if prefix == "EN":
        if code in {"EN07 OA 01", "EN07 OA 02", "EN07 OA 03"}:
            return "an original teacher-read audio script, replay plan and listening grid"
        if code in {"EN07 OA 04", "EN07 OA 05", "EN07 OA 06", "EN07 OA 07"}:
            return "short authorized literary and functional texts with headings, paragraph numbers and an essential glossary"
        if code in {"EN07 OA 08", "EN07 OA 09", "EN07 OA 10"}:
            return "fictional information-gap cards, useful chunks and a paper storyboard"
        return "fictional writing briefs, genre models, audience cards and a revision checklist"
    if prefix == "LI":
        return f"fuentes autorizadas y situadas por pueblo, territorio y comunidad para {topic.lower()}"
    if prefix == "MU":
        return f"registros autorizados, partituras convencionales o gráficas e instrumentos disponibles para {topic.lower()}"
    if prefix == "OR":
        return f"casos ficticios, rutas de apoyo y protocolos escolares para {topic.lower()}"
    return f"un desafío documentado, materiales disponibles, criterios de prueba y ficha de impacto para {topic.lower()}"


def _profile(code: str) -> dict:
    prefix = code[:2]
    topic = TOPICS[code]
    count = RECORDS[code]["count"]
    number = sum(ord(char) for char in code.rsplit(" ", 1)[-1])
    return {
        "topic": topic,
        "prior": PRIOR[prefix],
        "vocabulary": VOCABULARY[prefix],
        "anchor": _anchor(code, topic),
        "misconception": MISCONCEPTIONS[prefix][number % len(MISCONCEPTIONS[prefix])],
        "focuses": [f"{stage} · {topic}" for stage in STAGES[prefix][:count]],
    }


def _retarget_links(lesson: dict, prefix: str) -> None:
    if prefix == "LI":
        lesson["transversal"] = []
        return
    for link in lesson.get("transversal", []):
        link["code"] = link["code"].replace(f"{prefix}03", f"{prefix}07")


def _natural_voice(lesson: dict, profile: dict, index: int, prefix: str) -> None:
    focus = profile["focuses"][index]
    action = focus[0].lower() + focus[1:]
    anchor = profile["anchor"]
    misconception = profile["misconception"]
    if prefix == "EN":
        openings = (
            f"Present {anchor} once. Students first respond with a choice, gesture, note or short chunk and then identify the clue they used.",
            f"Reveal only the title, format or first image from {anchor}. Students make a tentative prediction and choose what they will listen or read for.",
            f"Offer two possible meanings for {anchor}. Students decide which fits better and point to a word, sound, image or text feature.",
            f"Begin with a short information gap from {anchor}; each partner needs the other's message to complete a practical task.",
            f"Change the speaker, audience or purpose in {anchor}. Students predict which language and delivery choices should change.",
        )
        models = (
            f"Think aloud in accessible English to show how to {action}. Combine an exact clue with context and check meaning instead of translating every word.",
            f"Compare two comprehensible responses. Explain why both may communicate, then revise the one that does not yet fit purpose or audience.",
            f"Model a first attempt that shows this problem: {misconception}. Ask for clarification, reread or paraphrase and repair the message openly.",
            f"Build a response from useful chunks rather than a full script. Make one meaningful choice, test it with a partner and revise for clarity.",
            f"Use {anchor} to plan, communicate and check. Keep meaning central; accent imitation, speed and instant perfection are not the goal.",
        )
        lesson["purpose"] = f"Help students {action} through meaningful English and evidence from the message."
        lesson["goal"] = f"Today I will {action}; I will show the clue or language choice that helped me communicate."
        lesson["opening"] = openings[index % len(openings)]
        lesson["model"] = models[index % len(models)]
        lesson["guided"] = f"Pairs work with a second version of {anchor}. They exchange missing information, ask for clarification and improve one part after focused feedback."
        lesson["independent"] = f"Each student completes a new task to {action}. A word bank or planning card is available, but the student selects language, communicates meaning and checks the result."
        lesson["ticket"] = "Give one short response for today's purpose and underline, point to or name the clue or language choice that supports it."
    elif prefix == "LI":
        openings = (
            f"Antes de usar {anchor}, identifica pueblo, territorio, responsable de la fuente y condiciones de circulación. El curso distingue lo público de lo que requiere consulta.",
            f"Presenta dos fuentes autorizadas de {anchor}. El curso observa coincidencias y diferencias sin tratarlas como versiones correctas e incorrectas.",
            f"Formula una pregunta sobre {anchor} que la fuente disponible sí puede responder y otra que exige educador tradicional o autoridad cultural pertinente.",
            f"Comparte un caso ficticio donde una fuente fue separada de su territorio. El curso decide cómo atribuirla, contextualizarla o detener su uso.",
            f"Propón una respuesta oral, visual o escrita a {anchor}; nadie está obligado a pronunciar, representar identidad ni divulgar experiencia familiar.",
        )
        models = (
            f"Modela cómo {action} sólo con fuente validada. No inventa lengua, pronunciación, grafías, símbolos ni explicaciones espirituales.",
            f"Compara dos respuestas atribuyendo cada voz y territorio. Explica por qué diferencia no significa déficit ni autoriza una jerarquía cultural.",
            f"Examina la confusión «{misconception}». Muestra cómo solicitar permiso, declarar límites y reformular sin apropiarse del conocimiento.",
            f"Construye una interpretación breve que distingue lo dicho por la fuente, la inferencia propia y lo que debe quedar como pregunta.",
            f"Modela una producción que dialoga con lo aprendido sin copiar signos, relatos o prácticas reservadas y sin hablar en nombre de una comunidad.",
        )
        lesson["purpose"] = f"Acompañar al curso a {action} desde territorio, fuentes autorizadas y límites culturales explícitos."
        lesson["goal"] = f"Hoy voy a {action}; atribuiré la fuente y respetaré lo que no corresponde inventar, divulgar o generalizar."
        lesson["opening"] = openings[index % len(openings)]
        lesson["model"] = models[index % len(models)]
        lesson["guided"] = f"Con educador tradicional o fuente comunitaria pertinente, analizan {anchor}; distinguen aprender, reproducir, recrear y apropiarse, y reciben validación antes de comunicar."
        lesson["independent"] = f"Cada estudiante elabora una comprensión o respuesta para {action}. Identifica pueblo, territorio, fuente, permiso y un límite; puede responder sin exponer pertenencia ni datos familiares."
        lesson["ticket"] = "Comunica una relación aprendida, atribuye la fuente comunitaria y nombra algo que no corresponde inventar, divulgar o generalizar."
        lesson["specialist_coordination"] = "El docente no suplanta saberes comunitarios: coordina con educador tradicional, autoridad cultural o fuente comunitaria pertinente y detiene la actividad si falta validación."
    elif prefix == "MU":
        openings = (
            f"Escuchen {anchor} una vez sin categorías previas. Cada estudiante registra un detalle audible, una sensación y una pregunta.",
            f"Presenta dos fragmentos autorizados de {anchor}. El curso compara un rasgo preciso antes de emitir preferencias.",
            f"Marca con gesto, línea o ficha un cambio audible en {anchor}. Luego acuerdan el vocabulario musical que mejor lo describe.",
            f"Ofrece una frase rítmica o melódica incompleta vinculada con {anchor}. El grupo propone continuaciones y anticipa su efecto.",
            f"Comparte un ensayo ficticio con una dificultad audible. El curso elige un ajuste acotado y explica qué debería cambiar al volver a escuchar.",
        )
        models = (
            f"Modela cómo {action}: escucha, señala el instante preciso, nombra el rasgo musical y relaciona la decisión con su efecto.",
            f"Ensaya dos versiones breves. Cambia una sola variable —pulso, dinámica, timbre, articulación o textura— y compara lo que se oye.",
            f"Examina la idea «{misconception}». Sustituye el juicio general por evidencia audible y contexto atribuido.",
            f"Construye una interpretación o creación parcial, deja una decisión abierta y muestra cómo el grupo puede aportar sin borrar voces individuales.",
            f"Modela retroalimentación musical: describe lo oído, cita el criterio y propone un ajuste que pueda comprobarse en el siguiente ensayo.",
        )
        lesson["purpose"] = f"Desarrollar la escucha y la agencia musical para {action}, con evidencia audible y contexto respetado."
        lesson["goal"] = f"Hoy voy a {action}; tomaré una decisión musical y explicaré qué se oye antes y después del ajuste."
        lesson["opening"] = openings[index % len(openings)]
        lesson["model"] = models[index % len(models)]
        lesson["guided"] = f"En grupos pequeños trabajan con {anchor}, roles rotativos y volumen seguro. Ensayan dos versiones, reciben un comentario basado en un criterio audible y deciden qué incorporar."
        lesson["independent"] = f"Cada estudiante escucha, interpreta o crea una respuesta breve para {action}. Registra una elección, un ajuste y la evidencia audible que lo sostiene."
        lesson["ticket"] = "Describe un cambio musical de hoy, ubica dónde se escucha y explica por qué conviene conservarlo o revisarlo."
    elif prefix == "OR":
        openings = (
            f"Presenta {anchor}. Todo el análisis se realiza en tercera persona; nadie debe contar experiencias, diagnósticos, orientación, consumo ni conflictos propios.",
            f"Entrega dos opciones de respuesta para un caso de {anchor}. El curso identifica derechos, riesgos, apoyos y consecuencias sin juzgar a la persona ficticia.",
            f"Muestra un mensaje o acuerdo incompleto vinculado con {anchor}. En parejas localizan qué protege dignidad, consentimiento y seguridad y qué falta.",
            f"Ubica en un mapa escolar ficticio las rutas de ayuda relacionadas con {anchor}. El curso diferencia apoyo de pares, adulto responsable y emergencia.",
            f"Cambia una condición del caso de {anchor}. Cada estudiante revisa su decisión y explica por qué una respuesta segura puede variar según contexto.",
        )
        models = (
            f"Piensa en voz alta para {action}: separa hechos, emociones posibles, derechos, límites y redes de apoyo; evita diagnosticar o moralizar.",
            f"Compara dos respuestas y examina consecuencias inmediatas y posteriores. No presenta obediencia, silencio ni secreto como soluciones universales.",
            f"Examina la confusión «{misconception}». Reformula el caso para proteger privacidad, agencia y acceso a ayuda competente.",
            f"Modela una conversación breve con escucha, límite claro, pregunta abierta y derivación a un adulto o protocolo cuando corresponde.",
            f"Construye un acuerdo verificable: conducta observable, responsable, plazo y forma segura de revisar su cumplimiento.",
        )
        lesson["purpose"] = f"Practicar cómo {action} mediante casos protegidos, derechos, decisiones y redes de ayuda."
        lesson["goal"] = f"Hoy voy a {action}; justificaré una respuesta segura sin exponer experiencias personales."
        lesson["opening"] = openings[index % len(openings)]
        lesson["model"] = models[index % len(models)]
        lesson["guided"] = f"Equipos analizan un segundo caso ficticio de {anchor}. Usan una matriz de hecho, derecho, opción, consecuencia y apoyo; luego ensayan una comunicación respetuosa."
        lesson["independent"] = f"Cada estudiante resuelve un caso nuevo para {action}. Elige una acción segura, explica consecuencias y señala una ruta de ayuda sin escribir datos personales."
        lesson["ticket"] = "Ante un caso ficticio, escribe una acción segura, el derecho o criterio que la sostiene y a quién pedir ayuda si no basta."
        lesson["specialist_coordination"] = "El docente enseña con casos ficticios y aplica el protocolo institucional ante una revelación espontánea; orientación o convivencia escolar apoya sin interrogar públicamente ni diagnosticar."
    else:
        openings = (
            f"Presenta {anchor}. Antes de imaginar objetos, cada equipo distingue necesidad, usuario, contexto y evidencia de que el problema existe.",
            f"Compara dos soluciones relacionadas con {anchor}. El curso identifica a quién sirven, qué criterio priorizan y qué costo o impacto desplazan.",
            f"Muestra un prototipo o plano incompleto de {anchor}. Los estudiantes predicen un punto de falla y proponen una prueba segura para comprobarlo.",
            f"Cambia una restricción de {anchor}: material, energía, tiempo, acceso o privacidad. Cada equipo revisa su diseño sin empezar de cero.",
            f"Entrega resultados ficticios de una prueba de {anchor}. El curso separa observación, interpretación y mejora antes de valorar la apariencia.",
        )
        models = (
            f"Modela cómo {action}: convierte la necesidad en criterios medibles, representa la solución y justifica una decisión sin construir todavía.",
            f"Compara dos alternativas mediante una matriz de usuario, función, recurso, seguridad, impacto y posibilidad de reparación.",
            f"Examina la confusión «{misconception}». Detiene el proceso, protege a usuarios y datos, y redefine el criterio que faltaba.",
            f"Realiza una prueba parcial con una variable y registra también el resultado que contradice la expectativa.",
            f"Comunica una mejora mediante boceto, diagrama, tabla o demostración; atribuye imágenes e ideas y evita publicar datos personales.",
        )
        lesson["purpose"] = f"Guiar un proceso tecnológico para {action}, considerando usuario, prueba, seguridad y efectos."
        lesson["goal"] = f"Hoy voy a {action}; justificaré una decisión con criterios y evidencia de prueba."
        lesson["opening"] = openings[index % len(openings)]
        lesson["model"] = models[index % len(models)]
        lesson["guided"] = f"Equipos trabajan con {anchor}. Distribuyen roles, elaboran o simulan una versión segura, prueban un criterio y registran evidencia antes de decidir una mejora."
        lesson["independent"] = f"Cada estudiante resuelve una variante para {action}. Entrega representación, decisión, resultado de prueba y revisión de impacto, autoría o privacidad."
        lesson["ticket"] = "Nombra la necesidad, el criterio decisivo, la evidencia de prueba y una mejora o impacto que todavía debe revisarse."

    visible_goal = lesson["goal"].removeprefix("Hoy ").removeprefix("Today ").rstrip(".")
    for link in lesson.get("transversal", []):
        application = link.get("application", "")
        if "durante «" in application:
            link["application"] = application.split("durante «", 1)[0] + f"durante «{visible_goal}» mediante una acción observable y revisable."


def build_sequence(code: str) -> dict | None:
    if code not in RECORDS:
        return None
    prefix = code[:2]
    profile = _profile(code)
    lessons = []
    for index in range(len(profile["focuses"])):
        if prefix in {"EN", "LI"}:
            maker_code = code.replace("LI07", "LC07", 1)
            lesson = applied_lesson(maker_code, index, profile)
        else:
            lesson = mot_lesson(code, index, profile)
        _retarget_links(lesson, prefix)
        _natural_voice(lesson, profile, index, prefix)
        lessons.append(lesson)
    record = RECORDS[code]
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": (
            f"{profile['topic']} parte de {profile['prior']} y avanza con decisiones propias de la disciplina. "
            f"La secuencia cambia situaciones, fuentes y productos, y enfrenta la confusión «{profile['misconception']}»."
        ),
        "prerequisites": profile["prior"],
        "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"Eje oficial · progresión interna en {len(lessons)} clases"],
            "unit_origin": "Organización pedagógica interna derivada del eje y del OA; no se presenta como una unidad oficial del programa.",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del objetivo oficial.",
            "source": record["url"],
        },
        "lessons": lessons,
    }


def build_transversal_integration(item: dict) -> dict:
    result = base_integration(dict(item))
    result["generated_for"] = "7-basico-remaining"
    return result


SEQUENCES = {code: True for code in RECORDS}

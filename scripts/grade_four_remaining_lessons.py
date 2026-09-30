"""Complete, subject-specific fourth-grade sequences beyond Mathematics.

The fourth-grade curriculum intentionally reuses a small number of disciplinary
lesson protocols, but every OA receives its own topic, anchor, misconception and
progression.  This keeps the public lessons consistent without turning them into
interchangeable worksheets.
"""
from __future__ import annotations

try:
    from grade_three_math_language_lessons import LANGUAGE as LANGUAGE_3, _lesson as language_lesson
    from grade_three_science_history_lessons import _lesson as science_history_lesson
    from grade_three_arts_pe_english_indigenous_lessons import TABLES as APEI_3, _lesson as apei_lesson
    from grade_three_music_orientation_technology_lessons import TABLES as MOT_3, _lesson as mot_lesson
except ImportError:
    from scripts.grade_three_math_language_lessons import LANGUAGE as LANGUAGE_3, _lesson as language_lesson
    from scripts.grade_three_science_history_lessons import _lesson as science_history_lesson
    from scripts.grade_three_arts_pe_english_indigenous_lessons import TABLES as APEI_3, _lesson as apei_lesson
    from scripts.grade_three_music_orientation_technology_lessons import TABLES as MOT_3, _lesson as mot_lesson


COUNTS = {
    "AR": [6, 5, 6, 4, 4],
    "CN": [4, 4, 4, 5, 4, 4, 4, 5, 4, 4, 4, 4, 4, 5, 4, 4, 4],
    "EF": [5, 5, 4, 5, 4, 4, 4, 4, 5, 4, 5],
    "HI": [5, 5, 5, 5, 6, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 5, 5, 5],
    "EN": [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5],
    "LE": [5, 6, 5, 6, 6, 6, 5, 6, 5, 5, 5, 5, 5, 5, 5, 5, 6, 5, 5, 5, 6, 5, 6, 5, 6, 6, 6, 5, 5, 5],
    "MU": [5, 4, 5, 4, 5, 4, 4, 4],
    "OR": [4, 4, 4, 4, 5, 5, 4, 5, 5],
    "TE": [6, 5, 5, 5, 4, 5, 5],
}

LC_COUNTS = {
    "LF01": 4, "LF02": 4, "LF03": 5, "LF04": 4, "LF05": 5, "LF06": 4,
    "LR01": 5, "LR02": 4, "LR03": 5, "LR04": 4, "LR05": 5, "LR06": 4,
    "LS01": 4, "LS02": 4, "LS03": 5, "LS04": 4, "LS05": 5, "LS06": 4,
    "07": 4, "08": 5, "09": 4, "10": 4, "11": 4, "12": 5, "13": 4,
    "14": 4, "15": 4, "16": 5, "17": 4,
}

SUBJECTS = {
    "AR": ("artes-visuales", "Artes Visuales"),
    "CN": ("ciencias-naturales", "Ciencias Naturales"),
    "EF": ("educacion-fisica-salud", "Educación Física y Salud"),
    "HI": ("historia-geografia-ciencias-sociales", "Historia, Geografía y Ciencias Sociales"),
    "EN": ("ingles-propuesta", "Inglés (Propuesta)"),
    "LC": ("lengua-cultura-pueblos-originarios-ancestrales", "Lengua y Cultura de los Pueblos Originarios Ancestrales"),
    "LE": ("lenguaje-comunicacion", "Lenguaje y Comunicación"),
    "MU": ("musica", "Música"),
    "OR": ("orientacion", "Orientación"),
    "TE": ("tecnologia", "Tecnología"),
}


def _p(topic, prior, vocabulary, anchor, misconception, focuses):
    return {"topic": topic, "prior": prior, "vocabulary": vocabulary, "anchor": anchor,
            "misconception": misconception, "focuses": focuses}


SCIENCE_THEMES = {
    1: ("Ecosistemas: componentes e interacciones", "un terrario observado como sistema, fotografías situadas y una tabla de relaciones", "enumerar componentes sin explicar cómo se afectan entre sí"),
    2: ("Adaptaciones de plantas y animales", "casos contrastados de cubierta, camuflaje, hojas y conducta en ecosistemas identificados", "decir que un organismo decidió cambiar o que toda característica es adaptación"),
    3: ("Cadenas alimentarias en ecosistemas de Chile", "tarjetas de organismos chilenos con fuente y flechas que representan transferencia de alimento", "invertir las flechas o creer que una cadena describe todas las relaciones"),
    4: ("Actividad humana y protección de ecosistemas", "casos documentados de intervención, parque, veda y restauración en Chile", "proponer campañas generales sin vincular causa, evidencia y medida"),
    5: ("Sistema esquelético: estructura y función", "modelo articulado, imágenes anatómicas apropiadas y movimientos observables", "memorizar nombres sin relacionar estructura con protección, soporte o movimiento"),
    6: ("Movimiento y sistema musculoesquelético", "modelo de brazo o pierna con huesos, articulación, músculos y tendones", "atribuir el movimiento a un solo músculo o confundir tendón con articulación"),
    7: ("Sistema nervioso: conducción y control", "modelo de respuesta ante un estímulo, cerebro, médula y nervios", "imaginar los nervios como cables aislados que actúan sin coordinación"),
    8: ("Efectos del consumo excesivo de alcohol", "fuentes sanitarias seleccionadas y casos ficticios sin normalizar ni dramatizar el consumo", "moralizar, diagnosticar personas o confundir opinión con evidencia sanitaria"),
    9: ("Materia: masa y ocupación de espacio", "balanza, recipientes y materiales sólidos, líquidos y gaseosos de uso seguro", "creer que el aire no es materia porque no se ve"),
    10: ("Estados de la materia", "muestras o representaciones de sólidos, líquidos y gases comparadas con los mismos criterios", "definir estados sólo por ejemplos o afirmar que todo líquido conserva forma"),
    11: ("Medición de masa, volumen y temperatura", "balanza, probeta o recipiente graduado y termómetro escolar usados en estaciones", "intercambiar magnitud, instrumento y unidad o leer una escala desde otro origen"),
    12: ("Efectos de las fuerzas sobre objetos", "carritos, elásticos y materiales deformables con una variable modificada por vez", "creer que toda fuerza produce movimiento o que una sola prueba basta"),
    13: ("Roce, peso y fuerza magnética", "comparaciones de superficies, caída representada e imanes con objetos previamente revisados", "confundir fuerza con objeto o explicar atracción magnética como adhesión"),
    14: ("Diseño tecnológico que aprovecha fuerzas", "desafío de mover, sostener o cambiar dirección con materiales simples y criterios previos", "construir antes de definir el problema o cambiar muchas variables al probar"),
    15: ("Capas internas de la Tierra", "modelos seccionados y datos sobre corteza, manto y núcleo con sus limitaciones declaradas", "tratar colores y proporciones del modelo como copia literal de la Tierra"),
    16: ("Placas tectónicas y cambios de la superficie", "mapas de placas y secuencias de sismos, tsunamis y erupciones analizadas causalmente", "afirmar que todo sismo causa tsunami o que es posible predecir fecha y lugar"),
    17: ("Prevención ante riesgos naturales", "planos y protocolos oficiales aplicados a casos ficticios de escuela, calle y hogar", "prometer ausencia de riesgo o responsabilizar a niñas y niños por emergencias"),
}

HISTORY_THEMES = {
    1: ("Civilización maya", "mapas, estelas, códices, arquitectura y reconstrucciones debidamente identificadas", "presentar siglos, ciudades y grupos mayas como una sociedad única e inmóvil"),
    2: ("Civilización azteca", "mapas, fuentes sobre Tenochtitlán, chinampas, organización y vida cotidiana", "reducir la civilización azteca a guerra y sacrificios o confundir fuente con ilustración libre"),
    3: ("Civilización inca", "mapas del Tawantinsuyu, caminos, quipus, terrazas y fuentes sobre vida cotidiana", "homogeneizar pueblos del imperio o tratar una reconstrucción como testimonio directo"),
    4: ("Comparación de civilizaciones americanas", "matriz común para comparar mayas, aztecas e incas con evidencia ya estudiada", "hacer listas paralelas sin criterio o convertir diferencias en jerarquías"),
    5: ("Pueblos indígenas americanos en el presente", "fuentes actuales con autor, fecha y voz indígena sobre continuidad, cambio y protagonismo", "hablar de los pueblos sólo en pasado o atribuir una voz a comunidades diversas"),
    6: ("Paralelos, meridianos y localización", "globo y mapas con cuadrícula geográfica y lugares de referencia", "confundir coordenadas geográficas con casilleros o intercambiar latitud y longitud"),
    7: ("Recursos renovables y no renovables", "objetos cotidianos rastreados hasta recursos, procesos y posibilidades de cuidado", "clasificar un recurso como infinito por ser renovable"),
    8: ("Paisajes del continente americano", "mapas temáticos y paisajes situados con clima, agua, población, idiomas y ciudades", "describir América como un paisaje uniforme o asociar idioma con un solo país"),
    9: ("Distribución y cuidado de recursos en América", "mapas de recursos y casos de uso con escalas, fechas y fuentes comparables", "suponer que presencia de un recurso garantiza bienestar o desarrollo sostenible"),
    10: ("Paisajes regionales y americanos", "pares de imágenes y mapas situados para comparar adaptación y transformación", "juzgar una adaptación fuera de contexto o explicar todo cambio por el clima"),
    11: ("Organización política democrática de Chile", "organigrama y casos públicos sobre Presidencia, ministerios, Congreso y alcaldías", "confundir institución, autoridad y función o afirmar que todos se eligen igual"),
    12: ("Derechos de niñas y niños", "situaciones ficticias, textos accesibles de derechos y rutas institucionales de protección", "tratar derechos como premios o pedir relatos personales de vulneración"),
    13: ("Honestidad y autoría cotidiana", "casos ficticios de juegos, errores, copia, fuentes y reparación", "reducir honestidad a confesar públicamente o a obedecer sin comprender"),
    14: ("Respeto y no discriminación", "casos ficticios que distinguen diferencia, prejuicio, discriminación y acción reparadora", "pedir a estudiantes representar identidades ajenas o debatir la dignidad de una persona"),
    15: ("Elección y organización democrática del curso", "simulación con cargos, funciones, candidaturas, voto secreto y rendición de cuentas", "convertir la elección en concurso de popularidad o asignar roles por estereotipos"),
    16: ("Resolución democrática de conflictos", "casos ficticios donde se separan hechos, intereses, opciones, acuerdos y límites", "mediar violencia como si fuera conflicto entre iguales o votar sobre derechos"),
    17: ("Proyecto para mejorar la comunidad escolar", "diagnóstico acotado de un problema ficticio, actores, recursos, plan y evaluación", "comenzar con una solución vistosa sin verificar necesidad ni participación"),
    18: ("Opinión y argumentación histórica y ciudadana", "preguntas discutibles, fuentes breves y una pauta de afirmación, evidencia y razonamiento", "confundir opinión con preferencia sin fundamento o acumular datos sin argumento"),
}

PUBERTY = _p(
    "Desarrollo afectivo y sexual durante la pubertad",
    "lenguaje de autocuidado, intimidad, emociones y respeto por diferencias",
    "pubertad, cambio físico, cambio afectivo, ritmo, intimidad, respeto, apoyo",
    "casos ficticios, siluetas no personalizadas y preguntas anónimas revisadas según protocolo escolar",
    "presentar un calendario corporal único, comparar cuerpos o solicitar experiencias personales",
    ["Cambios físicos esperables sin calendario único", "Cambios afectivos y nuevas necesidades", "Ritmos diversos y respeto entre pares", "Fuentes confiables, autocuidado y apoyo adulto"],
)

ADVERBS = _p("Adverbios para precisar oralidad y escritura", "reconocimiento de circunstancias en acciones narradas", "adverbio, verbo, modo, tiempo, lugar, intensidad, precisión", "versiones de una noticia y un relato donde cambia cómo, cuándo o dónde ocurre la acción", "agregar adverbios como adorno o creer que toda palabra terminada en -mente mejora el texto", ["Localizar qué precisa el adverbio", "Cambiar modo, tiempo y lugar", "Comparar matices entre alternativas", "Combinar sin recargar una oración", "Revisar precisión en un texto propio"])
VERBS = _p("Verbos y concordancia con el sujeto", "identificación de acciones y participantes en oraciones", "verbo, sujeto, persona, número, tiempo, concordancia, revisión", "fragmentos narrativos e informativos con cambios de sujeto y tiempo", "corregir por sonido sin identificar quién realiza la acción", ["Reconocer verbo y sujeto en contexto", "Coordinar persona y número", "Mantener tiempo verbal", "Revisar cambios de referente", "Editar concordancia en un párrafo"])


def _number(code: str) -> int:
    return int(code.rsplit(" ", 1)[-1])


def _target_count(code: str) -> int:
    prefix = code[:2]
    if prefix == "LC":
        return LC_COUNTS[code.rsplit(" ", 1)[-1]]
    return COUNTS[prefix][_number(code) - 1]


def _normalize(profile: dict, count: int) -> dict:
    """Fit a curated progression to the official dosage without duplicate lessons."""
    stages = list(profile["focuses"])
    additions = [
        "Contrastar evidencia y una alternativa",
        "Aplicar el aprendizaje en un caso nuevo",
        "Integrar decisiones en una producción completa",
        "Comunicar, recibir retroalimentación y revisar",
        "Transferir con una condición diferente",
        "Sintetizar hallazgos y próximos pasos",
    ]
    while len(stages) < count:
        stages.append(additions[len(stages) % len(additions)])
    stages = stages[:count]
    result = dict(profile)
    result["focuses"] = [f"{focus} · {profile['topic']}" for focus in stages]
    result["prior"] = f"desempeños de 3° básico: {profile['prior']}"
    return result


def _clone_profile(table: dict, old_code: str, new_code: str) -> dict:
    return _normalize(table[old_code], _target_count(new_code))


def _language_profile(code: str) -> dict | None:
    number = _number(code)
    if number == 19:
        return _normalize(ADVERBS, _target_count(code))
    if number == 20:
        return _normalize(VERBS, _target_count(code))
    old_number = number if number <= 18 else number + 1
    return _clone_profile(LANGUAGE_3, f"LE03 OA {old_number:02d}", code)


def _science_history_profile(code: str, discipline: str) -> dict:
    number = _number(code)
    topic, anchor, misconception = (SCIENCE_THEMES if discipline == "science" else HISTORY_THEMES)[number]
    if discipline == "science":
        stages = ["Observar y separar evidencia de interpretación", "Formular una pregunta o predicción comprobable", "Comparar casos con un criterio común", "Construir una explicación o modelo con límites", "Aplicar y comunicar una conclusión responsable", "Diseñar una indagación o solución y revisarla"]
        prior = "observar, medir y explicar fenómenos mediante evidencia"
        vocabulary = "evidencia, variable, comparación, modelo, explicación, limitación, seguridad"
    else:
        stages = ["Ubicar el problema en tiempo y espacio", "Interrogar fuentes y reconocer su procedencia", "Caracterizar dimensiones con evidencia", "Comparar perspectivas, cambios o continuidades", "Argumentar una conclusión fundamentada", "Conectar pasado, territorio y ciudadanía sin anacronismos"]
        prior = "leer mapas, secuencias, fuentes y situaciones ciudadanas"
        vocabulary = "fuente, contexto, evidencia, perspectiva, continuidad, cambio, argumento"
    return _normalize(_p(topic, prior, vocabulary, anchor, misconception, stages), _target_count(code))


def _reused_profile(code: str) -> dict | None:
    prefix = code[:2]
    if prefix == "OR" and _number(code) == 4:
        return _normalize(PUBERTY, _target_count(code))
    if prefix == "OR":
        old_number = _number(code) if _number(code) <= 3 else _number(code) - 1
        return _clone_profile(MOT_3["OR"], f"OR03 OA {old_number:02d}", code)
    table = APEI_3.get(prefix) or MOT_3.get(prefix)
    if not table:
        return None
    suffix = code.split("OA ", 1)[1]
    if prefix == "LC":
        if suffix in {"LF06", "LR06", "LS06"}:
            base = dict(table[f"LC03 OA {suffix[:2]}05"])
            base["topic"] = {
                "LF06": "Registro tecnológico situado de experiencias comunitarias en lengua indígena",
                "LR06": "Registro tecnológico situado con expresiones culturalmente significativas",
                "LS06": "Registro tecnológico situado desde castellano y contexto comunitario",
            }[suffix]
            base["anchor"] = "un registro ficticio o autorizado, herramienta disponible sin cuenta y criterios acordados con fuente comunitaria o educador tradicional"
            base["misconception"] = "publicar datos, voces o saberes sin consentimiento o inventar lengua cuando no se dispone de una fuente pertinente"
            base["focuses"] = ["Definir propósito, fuente y autorización", "Elegir un medio accesible y seguro", "Registrar sin exponer datos ni saberes restringidos", "Revisar lengua, contexto, autoría y almacenamiento"]
            return _normalize(base, _target_count(code))
        if suffix.isdigit():
            return _clone_profile(table, f"LC03 OA {int(suffix) - 1:02d}", code)
    return _clone_profile(table, f"{prefix}03 OA {suffix}", code)


def _fix_transversal_codes(lesson: dict) -> dict:
    for link in lesson.get("transversal", []):
        link["code"] = link["code"].replace("03", "04", 1)
    return lesson


def build_sequence(code: str) -> dict | None:
    prefix = code[:2]
    if prefix not in SUBJECTS or code[2:4] != "04" or code.startswith("de ") or prefix == "MA":
        return None
    if prefix == "LE":
        profile, maker, extra = _language_profile(code), language_lesson, "language"
    elif prefix in {"CN", "HI"}:
        discipline = "science" if prefix == "CN" else "history"
        profile, maker, extra = _science_history_profile(code, discipline), science_history_lesson, discipline
    else:
        profile = _reused_profile(code)
        maker = mot_lesson if prefix in {"MU", "OR", "TE"} else apei_lesson
        extra = None
    if not profile:
        return None
    lessons = []
    for index in range(len(profile["focuses"])):
        lesson = maker(code, index, profile, extra) if extra else maker(code, index, profile)
        focus = profile["focuses"][index]
        lesson["guided"] += f" La retroalimentación vuelve al criterio propio de «{focus.lower()}» antes del segundo intento."
        lesson["independent"] += f" La evidencia se juzga por el logro de «{focus.lower()}», no por imitar el ejemplo."
        lesson["ticket"] += f" La respuesta final debe permitir comprobar «{focus.lower()}»."
        lessons.append(_fix_transversal_codes(lesson))
    slug, _ = SUBJECTS[prefix]
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": f"{profile['topic']} avanza desde {profile['prior']} mediante una secuencia situada. Cada clase cambia la decisión, evidencia y forma de participación, y aborda explícitamente la confusión «{profile['misconception']}».",
        "prerequisites": profile["prior"],
        "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"Eje oficial · progresión interna en {len(lessons)} clases"],
            "unit_origin": "Organización pedagógica interna derivada del eje y del OA; no se presenta como una unidad oficial del programa",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del OA oficial",
            "source": f"https://www.curriculumnacional.cl/curriculum/1o-6o-basico/{slug}/4-basico/{code.lower().replace(' ', '-')}",
        },
        "lessons": lessons,
    }


def build_transversal_integration(item: dict) -> dict:
    """Integrate fourth-grade skills and attitudes into real disciplinary work."""
    clean = item["oa_text"].split("Unidad de Currículum", 1)[0].strip().rstrip(".")
    subject = item["subject"]
    contexts = {
        "ciencias-naturales": "una indagación, modelo o explicación científica",
        "historia-geografia-ciencias-sociales": "un análisis de fuente, mapa o problema ciudadano",
        "lenguaje-comunicacion": "una lectura, conversación o producción con propósito",
        "artes-visuales": "una creación o apreciación visual",
        "educacion-fisica-salud": "una tarea motriz segura y accesible",
        "ingles-propuesta": "una interacción comprensible en inglés",
        "lengua-cultura-pueblos-originarios-ancestrales": "un aprendizaje situado validado por fuente comunitaria o educador tradicional",
        "musica": "una experiencia de escucha, interpretación o creación musical",
        "tecnologia": "una experiencia de diseño, elaboración o comunicación digital segura",
    }
    context = contexts[item["subject_slug"]]
    lessons = []
    for index, (phase, phase_purpose) in enumerate(item["phases"]):
        title = f"{phase}: {clean.lower()} · situación {index + 1}"
        lessons.append({
            "title": title,
            "purpose": f"Integrar «{clean}» dentro de {context}, no como charla aislada ni juicio de personalidad.",
            "goal": f"Hoy demostraré {clean.lower()} mientras resuelvo una tarea auténtica de {subject}.",
            "opening": f"Contrasta dos respuestas ficticias ante {context}: una sólo nombra el foco y otra lo evidencia mediante una acción. El curso localiza la diferencia para «{title.lower()}».",
            "model": f"Modela {phase_purpose} y verbaliza qué decisión hace observable «{clean.lower()}», qué efecto tiene y qué evidencia permite revisarla.",
            "guided": f"Durante {context}, parejas aplican una pauta de una conducta observable, dan retroalimentación descriptiva y ensayan otra vez sin evaluar cuerpo, identidad, acento, talento, intimidad ni personalidad.",
            "independent": f"Cada estudiante completa una variante nueva de {context} y explica qué acción propia demuestra «{clean.lower()}».",
            "ticket": f"En la situación {index + 1}, señala acción, evidencia y próximo ajuste; no basta con repetir el nombre de la habilidad o actitud.",
            "materials": "Tarea disciplinar anfitriona, pauta breve y vía accesible de respuesta; sin datos personales ni materiales adicionales obligatorios.",
            "support": "Anticipa la conducta observable, ofrece ejemplo y ensayo, y ajusta acceso sin reducir el OA ni sustituir la decisión del estudiante.",
            "extension": "Transfiere el foco a otro eje, fuente, texto, problema, material o rol y compara cómo cambia su manifestación.",
            "evidence": f"Desempeño individual en {context} con acción y explicación vinculadas a «{clean.lower()}».",
            "criteria": ["mantiene el contenido disciplinar", "hace observable la habilidad o actitud", "explica su efecto y revisa una decisión"],
            "next_step": "Si sólo nombra el foco, vuelve a una acción concreta; si lo demuestra con apoyo, cambia el contexto; si actúa con autonomía, transfiere.",
            "short_version": "Conserva tarea auténtica, modelado, evidencia individual y ticket; reduce repeticiones, no la integración.",
            "home_task": "Representa un ejemplo seguro del foco dentro de la asignatura. No requiere compras, internet ni revelar experiencias familiares o personales.",
            "complementary": ["Distinguir evidencia y no evidencia del foco.", "Revisar un caso que confunde disposición con obediencia o talento.", "Transferir la acción a otra tarea disciplinar."],
            "difficulty_actions": [
                {"signal": "Repite la formulación sin aplicarla", "action": "Pide nombrar acción, momento y evidencia dentro de la tarea.", "check": "Ejecuta y localiza una conducta observable."},
                {"signal": "La integración desplaza el contenido", "action": "Recupera la meta disciplinar y observa el foco durante ese desempeño.", "check": "La evidencia demuestra ambos componentes."},
                {"signal": "La pauta etiqueta o expone a una persona", "action": "Reformula en acciones situadas, modificables y protegidas.", "check": "La retroalimentación describe decisiones, no rasgos."},
            ],
            "specialist_coordination": "El docente conserva la responsabilidad disciplinar; los apoyos acuerdan acceso y observación. En lengua y cultura, una fuente comunitaria o educador tradicional valida usos: el material no inventa lengua, no suplanta saberes comunitarios ni se apropia de ellos.",
            "transversal": [],
        })
    return {"generated_for": "4-basico", "lessons": lessons}


SEQUENCES = {
    code: True
    for prefix, counts in COUNTS.items()
    if prefix != "MA"
    for code in [f"{prefix}04 OA {index:02d}" for index in range(1, len(counts) + 1)]
}
SEQUENCES.update({f"LC04 OA {suffix}": True for suffix in LC_COUNTS})

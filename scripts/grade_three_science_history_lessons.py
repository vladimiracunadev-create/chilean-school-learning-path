"""Specific third-grade Science and History sequences."""
from __future__ import annotations


SCIENCE_SKILLS = (
    ("de Habilidad CN03 OAH a", "observar, preguntar, inferir y predecir de forma guiada"),
    ("de Habilidad CN03 OAH b", "participar en una investigación guiada y clasificar evidencia"),
    ("de Habilidad CN03 OAH c", "medir y registrar datos con instrumentos y unidades pertinentes"),
    ("de Habilidad CN03 OAH d", "usar materiales e instrumentos con seguridad y autonomía"),
    ("de Habilidad CN03 OAH e", "resumir evidencia para responder la pregunta inicial"),
    ("de Habilidad CN03 OAH f", "comunicar y comparar observaciones, mediciones y explicaciones"),
)
SCIENCE_ATTITUDES = (
    ("de Actitud CN03 OAA A", "curiosidad por los seres vivos y fenómenos del entorno"),
    ("de Actitud CN03 OAA B", "trabajo riguroso y perseverante"),
    ("de Actitud CN03 OAA C", "cuidado del entorno natural y sus recursos"),
    ("de Actitud CN03 OAA D", "responsabilidad y colaboración flexible"),
    ("de Actitud CN03 OAA E", "compromiso con hábitos saludables y autocuidado"),
    ("de Actitud CN03 OAA F", "respeto de normas de seguridad personal y colectiva"),
)
HISTORY_SKILLS = (
    ("de Habilidad HI03 OAH a", "leer y representar secuencias cronológicas"),
    ("de Habilidad HI03 OAH b", "aplicar conceptos de tiempo histórico"),
    ("de Habilidad HI03 OAH c", "comparar sociedades para reconocer cambios y continuidades"),
    ("de Habilidad HI03 OAH d", "leer y comunicar información mediante mapas, planos y diagramas"),
    ("de Habilidad HI03 OAH e", "orientarse con referencias y puntos cardinales"),
    ("de Habilidad HI03 OAH f", "obtener información de diversas fuentes mediante preguntas"),
    ("de Habilidad HI03 OAH g", "formular una opinión fundamentada en datos y evidencia"),
    ("de Habilidad HI03 OAH h", "intercambiar opiniones respetando turnos y perspectivas"),
    ("de Habilidad HI03 OAH i", "presentar un tema con organización y apoyo pertinente"),
)
HISTORY_ATTITUDES = (
    ("de Actitud HI03 OAA A", "trabajo riguroso, perseverante y abierto a la crítica"),
    ("de Actitud HI03 OAA B", "dignidad e importancia de todos los trabajos"),
    ("de Actitud HI03 OAA C", "igualdad de derechos y participación entre hombres y mujeres"),
    ("de Actitud HI03 OAA D", "igualdad de derechos sin discriminación"),
    ("de Actitud HI03 OAA E", "participación solidaria y responsable"),
    ("de Actitud HI03 OAA F", "pertenencia reflexiva al entorno social y natural"),
    ("de Actitud HI03 OAA G", "acción cotidiana según virtudes ciudadanas"),
    ("de Actitud HI03 OAA H", "valoración de la democracia y el resguardo de derechos"),
    ("de Actitud HI03 OAA I", "valoración de la vida en sociedad"),
)


def _p(topic, prior, vocabulary, anchor, misconception, focuses):
    return {"topic": topic, "prior": prior, "vocabulary": vocabulary, "anchor": anchor,
            "misconception": misconception, "focuses": focuses}


SCIENCE = {
    "CN03 OA 01": _p("Necesidades y estructuras de las plantas", "observación de seres vivos y registro de cambios", "raíz, tallo, hoja, agua, luz, variable, evidencia", "plantas equivalentes sometidas a una sola condición diferente", "atribuir una función por apariencia sin observar ni controlar condiciones", ["Preguntar qué necesita una planta", "Investigar agua y luz controlando variables", "Relacionar raíz y absorción", "Explicar funciones de tallo y hojas"]),
    "CN03 OA 02": _p("Diversidad de plantas de Chile", "comparación de características visibles", "autóctona, cultivo, región, rasgo, hábitat, registro", "fichas verificables de canelo, araucaria, quínoa, papa y vid", "presentar una planta como representativa de todo Chile o inventar usos locales", ["Observar rasgos sin adivinar nombres", "Identificar plantas autóctonas con fuentes", "Comparar cultivos nacionales y regionales", "Construir un registro situado y respetuoso"]),
    "CN03 OA 03": _p("Ciclo de vida de plantas con flor", "necesidades de plantas y secuencias temporales", "germinación, crecimiento, flor, polinización, fruto, dispersión", "seguimiento de semillas y análisis de imágenes de polinizadores", "dibujar un ciclo lineal que termina en el fruto y omite nuevas semillas", ["Germinación observada en el tiempo", "Crecimiento y formación de flores", "Polinización sin confundirla con dispersión", "Semilla, fruto y continuidad del ciclo"]),
    "CN03 OA 04": _p("Importancia y cuidado de las plantas", "relaciones simples entre seres vivos y ambiente", "alimento, oxígeno, hábitat, materia prima, medicinal, cuidado", "casos de alimento, sombra, fibras, madera y áreas verdes con fuentes", "afirmar que todas las plantas sirven del mismo modo o proponer cuidados simbólicos", ["Plantas en redes de vida", "Usos humanos con evidencia y cautela", "Consecuencias de perder vegetación", "Proponer y comunicar una medida comprobable"]),
    "CN03 OA 05": _p("Reducción, reutilización y reciclaje de recursos", "clasificación de materiales y cuidado ambiental", "recurso, residuo, reducir, reutilizar, reciclar, criterio, prototipo", "auditoría ficticia de residuos de una colación escolar sin datos personales", "poner todo en reciclaje sin priorizar reducción ni comprobar destino", ["Distinguir recurso y residuo", "Priorizar reducir antes de reciclar", "Diseñar una reutilización útil", "Probar un instrumento para separar o ahorrar"]),
    "CN03 OA 06": _p("Alimentos, funciones y hábitos saludables", "reconocimiento de alimentos cotidianos", "nutriente, energía, crecimiento, variedad, frecuencia, porción", "menús ficticios culturalmente diversos sin clasificar cuerpos ni moralizar alimentos", "dividir alimentos en buenos y malos o prescribir dietas individuales", ["Clasificar por aporte y no por juicio", "Relacionar alimentos con funciones", "Comparar variedad y frecuencia", "Proponer hábitos posibles y respetuosos"]),
    "CN03 OA 07": _p("Higiene y manipulación segura de alimentos", "lavado de manos y prevención básica", "contaminación, microorganismo, cadena, superficie, temperatura, prevención", "secuencia ficticia de preparación de una ensalada sin consumirla en clase", "creer que un alimento limpio a la vista está libre de contaminación", ["Rutas invisibles de contaminación", "Lavado de manos con procedimiento", "Separar superficies y utensilios", "Comunicar una práctica preventiva"]),
    "CN03 OA 08": _p("Fuentes naturales y artificiales de luz", "observación de luz, sombra y oscuridad", "fuente, natural, artificial, emitir, reflejar, seguridad", "Sol, fuego, ampolleta, pantalla, Luna y espejo", "clasificar como fuente todo objeto brillante aunque solo refleje", ["Distinguir emitir y reflejar", "Clasificar fuentes con criterios", "Comparar fuentes naturales y artificiales", "Evaluar usos y seguridad de la luz"]),
    "CN03 OA 09": _p("Propagación, reflexión y colores de la luz", "fuentes de luz y formulación de predicciones", "rayo, trayectoria, opaco, transparente, reflexión, espectro", "linterna de baja potencia, cartones perforados, espejo y prisma o recipiente con agua", "explicar un resultado cambiando varias condiciones a la vez o mirar fuentes intensas", ["Investigar trayectorias rectas", "Comparar paso por materiales", "Observar reflexión de manera segura", "Separar luz en colores", "Construir una explicación desde datos"]),
    "CN03 OA 10": _p("Propagación y cualidades del sonido", "reconocimiento de fuentes sonoras y vibración", "vibración, medio, reflexión, absorción, tono, intensidad", "elásticos, recipientes, superficies y fuentes sonoras de volumen seguro", "confundir tono con volumen o afirmar que el sonido viaja en el vacío", ["Vibración que produce sonido", "Propagación en varias direcciones", "Transmisión por distintos materiales", "Absorción y reflexión", "Comparar tono e intensidad con seguridad"]),
    "CN03 OA 11": _p("Componentes y escala del Sistema Solar", "observación del cielo y diferencia entre estrella y planeta", "Sol, planeta, luna, cometa, asteroide, órbita, escala", "tarjetas con datos comparables y modelos que declaran sus limitaciones", "tratar ilustraciones como fotografías a escala o ubicar todos los cuerpos a igual distancia", ["Distinguir tipos de cuerpos", "Comparar tamaños con modelos", "Ordenar distancias relativas", "Explicar apariencia y límites de representación"]),
    "CN03 OA 12": _p("Rotación y traslación de la Tierra", "sucesión de día y noche y ciclos anuales", "rotación, eje, traslación, órbita, día, año, modelo", "globo, fuente de luz indirecta y marcas de ubicación", "explicar día y noche porque el Sol gira alrededor de la Tierra", ["Modelar la rotación", "Relacionar rotación con día y noche", "Modelar la traslación", "Distinguir efectos y escalas temporales"]),
    "CN03 OA 13": _p("Modelos de fases y eclipses", "movimientos relativos de Sol, Tierra y Luna", "fase, eclipse, alineación, sombra, posición, limitación", "esferas y lámpara usadas sin mirar directamente la fuente", "atribuir las fases a la sombra de la Tierra o esperar eclipses cada mes", ["Observar fases como apariencia", "Modelar posiciones Sol-Tierra-Luna", "Distinguir eclipse solar y lunar", "Diseñar un modelo seguro", "Evaluar alcances y limitaciones"]),
}


HISTORY = {
    "HI03 OA 01": _p("Vida cotidiana y legados de la Grecia antigua", "uso inicial de fuentes y noción de pasado", "polis, ciudadanía, democracia, teatro, mito, legado, fuente", "mapas, objetos, reconstrucciones identificadas y textos sobre distintas polis", "presentar Grecia como una sociedad única, democrática para todas las personas y equivalente al presente", ["Ubicar Grecia en tiempo y espacio", "Vida cotidiana desde fuentes", "Polis, ciudadanía y exclusiones", "Teatro, mitología y expresión", "Legados y cambios hasta el presente"]),
    "HI03 OA 02": _p("Vida cotidiana y legados de Roma antigua", "comparación entre pasado y presente", "república, imperio, derecho, ciudadanía, acueducto, legado", "mapas, inscripciones traducidas, caminos, viviendas y edificios romanos", "presentar Roma como una sociedad homogénea o confundir legado con copia sin cambios", ["Ubicar Roma y su expansión", "Vida cotidiana y diversidad social", "Derecho, ciudadanía y exclusiones", "Ingeniería, lengua y arquitectura"]),
    "HI03 OA 03": _p("Necesidades humanas y respuestas culturales", "reconocimiento de necesidades y comparación", "necesidad, recurso, organización, tecnología, intercambio, adaptación", "casos contrastados de alimentación, vivienda, transporte y gobierno en Grecia y Roma", "ordenar culturas como superiores e inferiores por resolver distinto", ["Necesidades comunes, respuestas diversas", "Recursos y organización cotidiana", "Tecnologías e intercambios", "Explicar sin jerarquizar culturas"]),
    "HI03 OA 04": _p("Modos de vida antiguos y actuales", "descripción de costumbres y trabajos", "continuidad, cambio, contexto, oficio, creencia, ciudad", "pares de fuentes sobre vivienda, vestimenta, trabajo y ciudad antigua y actual", "comparar desde estereotipos o juzgar el pasado solo con normas presentes", ["Construir criterios de comparación", "Costumbres y vida familiar", "Trabajos, oficios y desigualdad", "Ciudades, creencias y cambios"]),
    "HI03 OA 06": _p("Ubicación en cuadrículas y puntos cardinales", "posición relativa y recorridos simples", "fila, columna, coordenada, norte, sur, este, oeste, referencia", "plano ficticio de una plaza y una escuela sin direcciones reales", "dar indicaciones según la posición del propio cuerpo y no una referencia estable", ["Leer filas, columnas y referencias", "Usar puntos cardinales", "Describir un recorrido reproducible", "Comprobar y corregir ubicaciones"]),
    "HI03 OA 07": _p("Referencias fundamentales del planeta", "lectura inicial de mapas y globos", "hemisferio, Ecuador, trópico, polo, continente, océano", "globo terráqueo y mapas con proyecciones distintas", "creer que el norte está físicamente arriba o que un mapa no deforma", ["Distinguir globo y mapa", "Ecuador y hemisferios", "Trópicos y polos", "Continentes y océanos con referencias"]),
    "HI03 OA 08": _p("Zonas climáticas, paisajes y formas de habitar", "diferencia entre tiempo atmosférico y clima", "zona cálida, templada, fría, paisaje, adaptación, estrategia", "mapas climáticos y casos de vivienda, vestimenta y actividades en distintos lugares", "suponer un único paisaje o modo de vida por zona climática", ["Ubicar zonas sin líneas rígidas", "Relacionar clima y paisaje", "Comparar estrategias para habitar", "Evitar determinismos y generalizaciones"]),
    "HI03 OA 09": _p("Entorno geográfico de Grecia y Roma", "vocabulario de relieve, agua y asentamiento", "península, archipiélago, valle, montaña, mar, río, ciudad", "mapas físicos del Egeo, Mediterráneo, península itálica y río Tíber", "enumerar accidentes geográficos sin explicar su localización o relación", ["Leer relieve y agua en mapas", "Entorno de las polis griegas", "Península itálica y Roma", "Comunicar una caracterización geográfica"]),
    "HI03 OA 10": _p("Influencia geográfica en Grecia y Roma", "caracterización de entornos y necesidades", "ubicación, relieve, clima, recurso, navegación, intercambio, influencia", "comparación de rutas marítimas, tierras agrícolas y asentamientos", "afirmar que la geografía determina por completo las decisiones humanas", ["Del mapa a una pregunta histórica", "Mar Egeo e intercambios griegos", "Mediterráneo, Tíber y Roma", "Recursos, decisiones y límites", "Explicar influencia sin determinismo"]),
    "HI03 OA 11": _p("Deberes y responsabilidades cotidianas", "acuerdos de convivencia y autocuidado", "deber, responsabilidad, compromiso, consecuencia, cuidado, comunidad", "casos ficticios sobre tareas, espacios compartidos, pertenencias y salud", "confundir responsabilidad infantil con tareas riesgosas o propias de adultos", ["Distinguir deber, favor y abuso", "Responsabilidades escolares", "Cuidado de espacios y pertenencias", "Autocuidado y solicitud de ayuda", "Planificar un compromiso verificable"]),
    "HI03 OA 12": _p("Valores ciudadanos en acciones cercanas", "respeto de turnos y reconocimiento de diferencias", "tolerancia, respeto, empatía, diálogo, diversidad, acción", "situaciones ficticias de desacuerdo, inclusión y ayuda sin exponer vivencias personales", "repetir valores abstractos sin identificar una acción concreta", ["Respeto frente a opiniones distintas", "Diálogo y diversidad cultural", "Empatía sin hablar por otra persona", "Ayuda pertinente y consentimiento", "Resolver un caso con acciones observables"]),
    "HI03 OA 13": _p("Honestidad en juegos y trabajo escolar", "reglas, verdad y reconocimiento de errores", "honestidad, regla, evidencia, error, reparación, confianza", "casos ficticios sobre puntajes, autoría, materiales y errores", "entender honestidad como obediencia ciega o confesión pública forzada", ["Reglas justas y conocidas", "Verdad y evidencia", "Reconocer un error de forma segura", "Reparar y reconstruir confianza"]),
    "HI03 OA 14": _p("Derechos de niñas y niños", "necesidades de cuidado, aprendizaje y protección", "derecho, garantía, protección, participación, institución, responsabilidad", "casos ficticios y versiones accesibles de derechos sin pedir testimonios", "tratar derechos como premios o exigir que estudiantes revelen vulneraciones", ["Derechos no son recompensas", "Cuidado, educación y desarrollo", "Cómo la sociedad garantiza derechos", "Redes de ayuda sin exposición personal"]),
    "HI03 OA 15": _p("Instituciones y servicios a la comunidad", "identificación de necesidades y trabajos comunitarios", "institución, pública, privada, servicio, usuario, función, fuente", "sitios y materiales oficiales de instituciones seleccionadas por servicio", "clasificar por el nombre o logo sin comprobar función y alcance", ["Formular una pregunta de investigación", "Distinguir institución y edificio", "Identificar servicio y personas que trabajan", "Comparar instituciones públicas y privadas", "Contrastar fuentes", "Comunicar resultados con atribución"]),
    "HI03 OA 16": _p("Participación responsable en hogar y escuela", "cumplimiento de acuerdos y colaboración", "participación, compromiso, responsabilidad, colaboración, seguimiento", "proyectos ficticios de campaña, celebración, juego y cuidado de materiales", "confundir participar con dirigir o asignar responsabilidades desiguales", ["Elegir un compromiso alcanzable", "Distribuir roles con equidad", "Cumplir y registrar acuerdos", "Evaluar aporte y mejorar"]),
}

PILOT_HISTORY = _p(
    "Investigación sobre civilizaciones antiguas", "formulación de preguntas y lectura guiada de fuentes",
    "pregunta, fuente, evidencia, autor, fecha, contraste, comunicación",
    "investigación acotada sobre viviendas, ciudades, vestimenta, tecnología o esclavitud en Grecia y Roma",
    "copiar información, mezclar épocas o presentar la esclavitud sin reconocer violencia y falta de libertad",
    ["De un interés a una pregunta investigable", "Seleccionar fuentes identificadas", "Registrar sin copiar", "Contrastar información y perspectivas", "Organizar una respuesta", "Comunicar y responder preguntas"],
)


def _links(code: str, index: int, goal: str, discipline: str) -> list[dict[str, str]]:
    number = int(code.split(" OA ")[1])
    if discipline == "science":
        skill_code, skill = SCIENCE_SKILLS[(number + index * 2) % len(SCIENCE_SKILLS)]
        attitude_code, attitude = SCIENCE_ATTITUDES[(number * 2 + index) % len(SCIENCE_ATTITUDES)]
    else:
        skill_code, skill = HISTORY_SKILLS[(number * 2 + index) % len(HISTORY_SKILLS)]
        attitude_code, attitude = HISTORY_ATTITUDES[(number + index * 3) % len(HISTORY_ATTITUDES)]
    return [
        {"code": skill_code, "type": "Habilidad", "application": f"Se observa al {skill} mientras se alcanza la meta «{goal}»."},
        {"code": attitude_code, "type": "Actitud", "application": f"Se promueve {attitude} mediante una acción situada, revisable y vinculada con evidencia."},
    ]


def _lesson(code: str, index: int, profile: dict, discipline: str) -> dict:
    focus, topic = profile["focuses"][index], profile["topic"]
    anchor, misconception = profile["anchor"], profile["misconception"]
    modes = ("observar antes de explicar", "modelar un criterio", "comparar evidencias", "examinar un error", "aplicar en un caso nuevo", "comunicar y revisar")
    mode = modes[index % len(modes)]
    if discipline == "science":
        opening = f"Presenta {anchor} y pregunta qué se observa realmente sobre «{focus.lower()}». Cada estudiante registra observación, pregunta y predicción por separado."
        model = f"Modela cómo {mode}: define qué cambia y qué se mantiene, registra evidencia y formula una explicación prudente. Contrasta con la confusión «{misconception}»."
        guided = f"Equipos realizan o analizan una comparación segura vinculada con {anchor}; acuerdan instrumentos, registran datos individuales y comparan resultados antes de concluir."
        independent = f"Analiza un caso nuevo de «{focus.lower()}»: responde la pregunta, usa una tabla, diagrama o modelo y distingue resultado, explicación y limitación."
        ticket = f"Escribe una conclusión sobre «{focus.lower()}» que cite una evidencia y una condición que se mantuvo constante."
        evidence = f"Registro individual de {focus.lower()} con observación o medición, comparación, conclusión y limitación."
        support = "Reduce variables, ofrece tabla visual y modela una observación sin revelar la conclusión; ajusta manipulación o forma de registro manteniendo la pregunta científica."
        extension = f"Cambia una condición de {anchor}, formula una nueva predicción y decide qué evidencia adicional permitiría sostenerla."
        coordination = "El docente conduce indagación y seguridad; educación diferencial ajusta acceso, manipulación o comunicación sin sustituir la observación ni la explicación científica."
    else:
        opening = f"Presenta {anchor} con procedencia visible y sin entregar su interpretación. Cada estudiante anota qué muestra, de cuándo o dónde es y una pregunta sobre «{focus.lower()}»."
        model = f"Modela cómo {mode}: contextualiza la fuente o mapa, distingue evidencia e interpretación y limita lo que puede concluirse. Contrasta con «{misconception}»."
        guided = f"Parejas comparan dos fuentes, mapas o casos vinculados con {anchor}; registran coincidencias, diferencias, perspectiva y una pregunta que permanece abierta."
        independent = f"Explica un caso nuevo de «{focus.lower()}» mediante una fuente, relación temporal, espacial o razón ciudadana explícita; evita generalizar más allá de la evidencia."
        ticket = f"Formula una conclusión sobre «{focus.lower()}», cita la evidencia que la sostiene y señala algo que la fuente no permite saber."
        evidence = f"Explicación, mapa o decisión individual sobre {focus.lower()}, apoyada en una fuente o razón explícita y contextualizada."
        support = "Ofrece fuente breve, mapa ampliado, línea de tiempo o vocabulario visual y permite respuesta oral o gráfica; conserva comparación, contextualización y justificación."
        extension = f"Agrega una fuente con otra perspectiva o escala sobre {anchor} y revisa la conclusión indicando continuidad, cambio, ubicación o consecuencia."
        coordination = "El docente conduce el trabajo con fuentes y evita anacronismos, estereotipos o exposición personal; los apoyos facilitan acceso sin proporcionar la conclusión."
    goal = ("investigaré y explicaré " if discipline == "science" else "analizaré y comunicaré ") + focus.lower()
    return {
        "title": focus, "purpose": f"Desarrollar {topic.lower()} mediante {focus.lower()}, con razonamiento disciplinar y revisión basada en evidencia.",
        "goal": f"Hoy {goal}.", "opening": opening, "model": model, "guided": guided,
        "independent": independent, "ticket": ticket,
        "materials": f"Recursos reutilizables para {anchor}; pizarra, cuaderno y alternativa sin conectividad. Verifica procedencia, legibilidad y seguridad antes de la clase.",
        "support": support, "extension": extension, "evidence": evidence,
        "criteria": ["responde al foco específico de la clase", "usa evidencia disciplinar pertinente y contextualizada", "explica una decisión y reconoce límites o revisa un error"],
        "next_step": "Avanza si evidencia y explicación coinciden; si no, identifica si la dificultad está en observar o leer la fuente, en el concepto o en la justificación y reenseña con otro caso.",
        "short_version": "Conserva el caso específico, modelado breve, análisis conjunto, evidencia individual y ticket; reduce repeticiones, no la demanda del OA.",
        "home_task": "Busca o construye un ejemplo cotidiano seguro mediante dibujo, nota u oralidad. No requiere internet, compras ni revelar información familiar.",
        "complementary": ["Recuperación: vuelve a un caso con menos elementos y retorna al desafío original.", f"Análisis de error: corrige un caso ficticio que muestra esta confusión: {misconception}.", "Transferencia: cambia una condición, fuente o escala y revisa la conclusión."],
        "difficulty_actions": [
            {"signal": "Responde antes de examinar evidencia", "action": "Pide señalar primero el dato, rasgo, fuente o ubicación que utilizará.", "check": "La respuesta nueva cita una evidencia pertinente."},
            {"signal": misconception.capitalize(), "action": support, "check": "Resuelve un caso nuevo sin repetir la confusión y explica la diferencia."},
            {"signal": "Completa la actividad, pero no explica", "action": "Solicita comparar con una alternativa y nombrar el criterio decisivo.", "check": "La explicación permite reconstruir la decisión."},
        ],
        "specialist_coordination": coordination,
        "transversal": _links(code, index, goal, discipline),
    }


def _build(code: str, table: dict, discipline: str) -> dict | None:
    profile = table.get(code)
    if not profile:
        return None
    slug = "ciencias-naturales" if discipline == "science" else "historia-geografia-ciencias-sociales"
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": f"{profile['topic']} se desarrolla mediante desempeños observables. Parte de {profile['prior'][0].lower() + profile['prior'][1:]} y enfrenta «{profile['misconception']}».",
        "prerequisites": profile["prior"], "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"Progresión interna en {len(profile['focuses'])} clases"],
            "unit_origin": "Organización pedagógica interna derivada del eje y del OA; no se presenta como unidad oficial del programa.",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del OA oficial",
            "source": f"https://www.curriculumnacional.cl/curriculum/1o-6o-basico/{slug}/3-basico/{code.lower().replace(' ', '-')}",
        },
        "lessons": [_lesson(code, index, profile, discipline) for index in range(len(profile["focuses"]))],
    }


def build_sequence(code: str) -> dict | None:
    return _build(code, SCIENCE, "science") or _build(code, HISTORY, "history")


def complete_history_pilot(sequence: dict) -> dict:
    generated = _build("HI03 OA 05", {"HI03 OA 05": PILOT_HISTORY}, "history")
    sequence.update({key: value for key, value in generated.items() if key != "lessons" and key not in sequence})
    sequence["lessons"] = [base | current for base, current in zip(generated["lessons"], sequence["lessons"])]
    return sequence


def build_transversal_integration(item: dict) -> dict:
    discipline = "science" if item["subject_slug"] == "ciencias-naturales" else "history"
    clean = item["oa_text"].split("Unidad de Currículum", 1)[0].strip().rstrip(".")
    context = "una investigación del OA en curso" if discipline == "science" else "un análisis de fuente, mapa o caso del OA en curso"
    lessons = []
    for phase, phase_purpose in item["phases"]:
        lessons.append({
            "title": f"{phase}: {clean}", "purpose": f"Integrar «{clean.lower()}» dentro de {context}, sin convertirla en una clase aislada.",
            "goal": f"Hoy demostraré {clean.lower()} mientras desarrollo una tarea disciplinar.",
            "opening": f"Compara dos respuestas ficticias ante {context}: una evidencia el foco y otra solo lo nombra. Identifican conductas observables.",
            "model": f"Modela {phase_purpose} y verbaliza cuándo aparece «{clean.lower()}», qué decisión exige y qué evidencia permite observarla sin etiquetar personas.",
            "guided": f"Durante {context}, parejas aplican una pauta breve, ofrecen retroalimentación descriptiva y realizan un segundo intento.",
            "independent": f"Cada estudiante completa el desempeño y explica qué acción demuestra «{clean.lower()}».",
            "ticket": "Describe una acción observable, la evidencia producida y el ajuste para el siguiente intento.",
            "materials": "Tarea disciplinar, pauta breve y medio accesible; sin materiales adicionales ni datos personales.",
            "support": "Anticipa la conducta observable y ofrece pauta visual o ensayo; mantiene íntegra la demanda disciplinar.",
            "extension": "Transfiere el foco a otra fuente, investigación, escala o rol y compara qué cambia.",
            "evidence": "Desempeño disciplinar y registro individual de una acción observable vinculada con el foco.",
            "criteria": ["mantiene el OA disciplinar", "hace observable la habilidad o actitud", "revisa su actuación con evidencia"],
            "next_step": "Si solo repite la formulación, vuelve a una acción concreta; si la demuestra, transfiérela.",
            "short_version": "Conserva modelado, desempeño disciplinar, observación individual y ticket.",
            "home_task": "Explica con un ejemplo ficticio cómo se vería el foco. No requiere revelar experiencias familiares.",
            "complementary": ["Recuperación: elegir qué acción evidencia el foco.", "Práctica: aplicar la pauta en un segundo intento.", "Profundización: adaptar la conducta a otro contexto."],
            "difficulty_actions": [
                {"signal": "Repite el foco sin mostrarlo", "action": "Pide nombrar acción, momento y evidencia.", "check": "Ejecuta una conducta observable."},
                {"signal": "La integración desplaza el contenido", "action": "Vuelve a la meta del OA y observa el foco durante ese desempeño.", "check": "La evidencia demuestra ambos componentes."},
                {"signal": "La pauta etiqueta a la persona", "action": "Reformula en conductas situadas y modificables.", "check": "La retroalimentación describe acciones."},
            ],
            "specialist_coordination": "El docente conserva la responsabilidad disciplinar; los apoyos acuerdan accesos y observación sin sustituir respuestas.",
            "transversal": [],
        })
    return {"lessons": lessons}

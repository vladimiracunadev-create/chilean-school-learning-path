"""Specific first-year secondary Science, History and English sequences.

Official objectives and URLs come from the checked-in MINEDUC snapshot. Topics,
classroom anchors, progressions and misconceptions are original pedagogical
elaborations. English and Inglés (Propuesta) remain separate curricular records.
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


def _d(topic: str, anchor: str, misconception: str) -> dict:
    return {"topic": topic, "anchor": anchor, "misconception": misconception}


DETAILS = {
    # Ciencias Naturales · Biología
    "CN1M OA 01": _d("Formación, estratos y antigüedad relativa de los fósiles", "muestras o fotografías atribuidas de fósiles, capas sedimentarias de papel y una columna estratigráfica con eventos fechables", "creer que cualquier resto antiguo es un fósil o que los estratos siempre conservan una secuencia intacta"),
    "CN1M OA 02": _d("Evidencias de evolución y selección natural", "dossier de fósiles, estructuras homólogas, embriones y secuencias breves de ADN, más datos de variación y supervivencia poblacional", "presentar la evolución como progreso dirigido de individuos o como una idea sostenida por una sola clase de evidencia"),
    "CN1M OA 03": _d("Clasificación biológica y parentesco evolutivo", "tarjetas de organismos con caracteres comparables, árboles filogenéticos alternativos y una cronología de cambios taxonómicos", "ordenar seres vivos por parecido superficial o tratar las categorías taxonómicas como cajas fijas sin historia"),
    "CN1M OA 04": _d("Niveles de organización e interacciones en ecosistemas chilenos", "casos documentados de ecosistemas chilenos, tarjetas de organismos y evidencias de depredación, competencia, mutualismo, comensalismo y parasitismo", "confundir hábitat con ecosistema o clasificar una interacción sin atender beneficios, costos y contexto"),
    "CN1M OA 05": _d("Factores que regulan poblaciones y consecuencias ecosistémicas", "series ficticias de población, lluvia, alimento, enfermedad y depredadores, con eventos que obligan a revisar una predicción", "atribuir todo cambio poblacional a una sola causa o proyectar indefinidamente una tendencia corta"),
    "CN1M OA 06": _d("Ciclos biogeoquímicos, flujo de energía y contaminantes", "modelos de carbono, nitrógeno, agua y fósforo, redes y pirámides tróficas y un caso ficticio de bioacumulación", "dibujar la energía como si se reciclara igual que la materia o creer que un contaminante desaparece al diluirse"),
    "CN1M OA 07": _d("Fotosíntesis, respiración y funcionamiento del ecosistema", "plantas acuáticas o datos experimentales seguros bajo distintas condiciones, ecuaciones con modelos de partículas y un balance de materia y energía", "afirmar que las plantas solo fotosintetizan o que materia y energía son la misma entidad que circula"),
    "CN1M OA 08": _d("Impactos humanos, fenómenos naturales y sustentabilidad", "dos estudios de caso chilenos con mapas, datos de recursos, biodiversidad y decisiones de conservación, cultivo, forestación o extracción", "tratar toda intervención humana como equivalente o llamar sustentable a una medida sin examinar costos, escala y duración"),
    # Ciencias Naturales · Física
    "CN1M OA 09": _d("Ondas: energía, propiedades y clasificación", "resortes, cuerdas, bandeja de ondas o simulación sin cuenta, registros de amplitud, frecuencia, longitud de onda y rapidez", "creer que la materia viaja con la onda o clasificarla por cómo se dibuja y no por el medio y la vibración"),
    "CN1M OA 10": _d("Sonido, modelo ondulatorio y aplicaciones", "diapasones o aplicaciones sin cuenta, tubos y cuerdas seguras, audios propios y datos de eco, resonancia y efecto Doppler", "confundir intensidad con tono o explicar el sonido sin relacionar fuente, medio, frecuencia, amplitud y receptor"),
    "CN1M OA 11": _d("Luz, modelos, imágenes y color", "espejos, lentes, filtros, rendijas y fuentes de baja potencia, diagramas de rayos y registros de reflexión, refracción e interferencia", "usar un solo modelo de luz para todo o creer que el espejo invierte izquierda y derecha como una acción propia"),
    "CN1M OA 12": _d("Oído, ojo, espectros y tecnologías correctivas", "modelos anatómicos, diagramas de trayecto de ondas, espectros audibles y visibles y casos ficticios de lentes o audífonos", "tratar ojo y oído como cámaras o micrófonos pasivos o presentar una limitación sensorial como defecto personal"),
    "CN1M OA 13": _d("Ondas sísmicas, medición y consecuencias", "sismogramas simplificados, mapa de epicentros, modelo elástico y casos chilenos con magnitud, intensidad, daños y tsunamis diferenciados", "confundir magnitud e intensidad o afirmar que los sismos se predicen con fecha y lugar exactos"),
    "CN1M OA 14": _d("Sistema Tierra-Luna-Sol, eclipses y estaciones", "esferas, lámpara segura, planos orbitales, registros de sombra y datos comparativos de planetas", "explicar las estaciones por distancia al Sol o creer que cada fase lunar corresponde a la sombra de la Tierra"),
    "CN1M OA 15": _d("Escalas y propiedades de estructuras cósmicas", "tarjetas de meteoros, asteroides, cometas, planetas, estrellas, nebulosas y galaxias con escalas logarítmicas declaradas", "ordenar estructuras solo por brillo aparente o representar distancias y tamaños astronómicos en una misma escala lineal"),
    "CN1M OA 16": _d("Astronomía en Chile, instrumentos y lectura de radiación", "mapa de observatorios, espectros atribuidos, fichas de telescopios y radiotelescopios y perfiles de científicas y científicos chilenos", "reducir la ventaja astronómica de Chile a cielos bonitos o creer que observar consiste únicamente en ampliar imágenes visibles"),
    # Ciencias Naturales · Química
    "CN1M OA 17": _d("Evidencias, variables y representación de reacciones químicas", "estaciones seguras o datos de fermentación, oxidación, precipitación y combustión, con registros de temperatura, gas, color y ecuaciones", "usar cualquier cambio visible como prueba suficiente de reacción o balancear ecuaciones cambiando subíndices"),
    "CN1M OA 18": _d("Conservación de átomos y masa en reacciones", "balanza, sistema cerrado seguro y modelos de partículas antes y después de varias reacciones representadas", "creer que la masa desaparece cuando se produce un gas o que conservar átomos significa conservar moléculas"),
    "CN1M OA 19": _d("Compuestos binarios y ternarios, enlace y nomenclatura", "tarjetas de iones, modelos electrostáticos y fórmulas para construir y nombrar compuestos frecuentes con carga total neutra", "combinar símbolos por sonido del nombre o usar cargas y subíndices sin comprobar neutralidad y tipo de compuesto"),
    "CN1M OA 20": _d("Estequiometría y relaciones entre reactantes y productos", "recetas de partículas, ecuaciones balanceadas, tablas de cantidad y casos de reactivo limitante vinculados con fotosíntesis", "tratar coeficientes como masas directas o asumir que todos los reactantes se consumen siempre por completo"),

    # Historia mundial y Chile republicano
    "HI1M OA 01": _d("Liberalismo, republicanismo y transformaciones del siglo XIX", "fragmentos constitucionales, prensa, asociaciones y datos de ciudadanía y mercado en América y Europa", "tratar liberalismo y republicanismo como sinónimos estables o confundir derechos declarados con participación efectiva"),
    "HI1M OA 02": _d("Cultura burguesa, trabajo, familia y género", "manuales, imágenes, viviendas, prensa y testimonios del siglo XIX con autoría, clase social y contexto", "presentar los valores burgueses como experiencia universal o naturalizar sus roles familiares y de género"),
    "HI1M OA 03": _d("Estado-nación, soberanía y geografía política", "mapas europeos y latinoamericanos de distintos años, constituciones y fuentes sobre lengua, territorio y pertenencia", "suponer que nación, Estado y territorio coinciden naturalmente o que las fronteras surgieron sin conflicto"),
    "HI1M OA 04": _d("Idea de progreso, ciencia y dominio de la naturaleza", "publicidad, prensa, inventos, exposiciones y textos positivistas contrastados con sus costos y exclusiones", "aceptar progreso como mejora automática para toda la población o confundir innovación técnica con bienestar común"),
    "HI1M OA 05": _d("Industrialización, trabajo, ciudad y comunicaciones", "series de producción y población, planos urbanos, reglamentos fabriles y testimonios obreros y empresariales", "explicar la industrialización mediante una sola máquina o describir sus efectos como iguales en todos los territorios"),
    "HI1M OA 06": _d("Imperialismo, capitalismo y pueblos colonizados", "mapas imperiales, estadísticas comerciales, propaganda y testimonios de sociedades colonizadas con contexto", "presentar el imperialismo como expansión inevitable o reducir a los pueblos colonizados a víctimas sin agencia"),
    "HI1M OA 07": _d("Primera Guerra Mundial, sociedad civil y nuevo orden mundial", "mapas, cartas, fotografías, datos de movilización y trabajo y tratados con procedencia explícita", "reducir la guerra a batallas europeas o atribuir todos los cambios sociales y geopolíticos a una sola causa"),
    "HI1M OA 08": _d("Formación de la República de Chile y Constitución de 1833", "ensayos constitucionales, debates, cronología de conflictos y fuentes de proyectos políticos rivales", "narrar la organización republicana como acuerdo lineal o explicar la estabilidad solo por el texto constitucional"),
    "HI1M OA 09": _d("Consolidación republicana, debate y conflictos políticos", "prensa, registros electorales, debates parlamentarios y mapas de conflictos territoriales del siglo XIX chileno", "equiparar institucionalización con participación universal o presentar el centralismo como problema ya resuelto"),
    "HI1M OA 10": _d("Chile, mercados atlánticos y economía rural", "series de exportación, rutas, precios, contratos de hacienda y testimonios sobre inquilinaje", "confundir inserción internacional con industrialización plena o describir hacienda e inquilinaje sin relaciones de poder"),
    "HI1M OA 11": _d("Opinión pública, educación y construcción de nación", "prensa, literatura, historiografía, discursos escolares y registros de movilización con públicos y silencios identificables", "suponer que una identidad nacional única se difundió sin disputa o que ampliar educación eliminó exclusiones"),
    "HI1M OA 12": _d("Exploración estatal, ciencias y delimitación territorial", "mapas de expediciones, censos, informes científicos y documentos administrativos con zonas ausentes o discutidas", "tratar mapas y censos como fotografías neutrales o confundir reconocimiento estatal con territorio vacío"),
    "HI1M OA 13": _d("Ocupación austral, inmigración y pueblos originarios", "mapas de Valdivia, Llanquihue, Chiloé y Magallanes, contratos, censos y fuentes indígenas y migrantes", "narrar la ocupación como colonización de espacios vacíos o atribuir resultados a un solo grupo de inmigrantes"),
    "HI1M OA 14": _d("Ocupación de la Araucanía y despojo territorial mapuche", "mapas antes y después, decretos, testimonios mapuche, registros militares, ferroviarios y de reducciones", "usar eufemismos que ocultan coerción o presentar al pueblo mapuche como homogéneo y sin agencia histórica"),
    "HI1M OA 15": _d("Guerra del Pacífico, salitre y relaciones vecinales", "mapas, prensa de distintos países, cartas civiles y militares y datos económicos con procedencia", "explicar la guerra solo por heroísmo o salitre y trasladar el conflicto histórico a estereotipos nacionales actuales"),
    "HI1M OA 16": _d("Orden liberal y parlamentarismo chileno", "reformas constitucionales, registros electorales, prensa de partidos y debates sobre secularización y poderes del Estado", "confundir parlamentarismo chileno con el modelo británico o equiparar ampliación del voto con sufragio universal"),
    "HI1M OA 17": _d("Riqueza salitrera, Estado e inversión pública", "series fiscales, mapas ferroviarios, presupuestos de infraestructura y educación y registros de ciclos del salitre", "suponer que el ingreso salitrero se distribuyó de modo uniforme o que explica por sí solo toda modernización"),
    "HI1M OA 18": _d("Cuestión social, actores y formas de organización", "fotografías, prensa obrera, informes oficiales, petitorios y datos de vivienda, salud y trabajo", "reducir la cuestión social a pobreza individual o presentar a sectores populares como receptores pasivos de reformas"),
    # Economía, geografía y formación ciudadana
    "HI1M OA 19": _d("Escasez, necesidades y circuito económico", "presupuestos ficticios, flujos entre familias, empresas, Estado y resto del mundo y decisiones con costos de oportunidad", "confundir escasez con pobreza o asumir que toda necesidad y deseo tiene la misma prioridad y consecuencia"),
    "HI1M OA 20": _d("Oferta, demanda, precios y alteraciones del mercado", "mercados simulados con datos, curvas construidas desde tablas y casos de monopolio, colusión, inflación, aranceles y regulación", "tratar el precio como decisión arbitraria de un actor o aplicar oferta y demanda sin revisar condiciones del mercado"),
    "HI1M OA 21": _d("Ahorro, crédito, inversión y riesgo financiero", "ofertas ficticias comparables con costo total, interés, plazo, liquidez y riesgo, sin solicitar datos familiares", "elegir por la cuota más baja o presentar inversión, ahorro y previsión como equivalentes y sin riesgo"),
    "HI1M OA 22": _d("Consumo informado, derechos y endeudamiento", "contratos y publicidad ficticios, presupuesto protegido y rutas institucionales de reclamo y comparación", "culpar al consumidor por toda dificultad o creer que firmar elimina derechos, información y responsabilidades del proveedor"),
    "HI1M OA 23": _d("Respuestas políticas ante problemas sociales", "dossier atribuido de posturas liberales, socialistas, anarquistas, comunistas y socialcristianas y un problema público actual ficticio", "convertir corrientes políticas en etiquetas caricaturescas o trasladarlas al presente sin contexto ni matices"),
    "HI1M OA 24": _d("Conflicto, convivencia y diversidad de pueblos indígenas", "fuentes situadas y autorizadas de distintos pueblos, mapas territoriales, testimonios públicos y normas actuales", "hablar de los pueblos indígenas como una sola cultura o exigir a estudiantes que representen identidades y experiencias personales"),
    "HI1M OA 25": _d("Industrialización, ambiente y desarrollo sostenible", "series históricas de producción y contaminación, mapas de impactos y propuestas actuales con indicadores sociales, ambientales y económicos", "oponer empleo y ambiente como opciones absolutas o llamar sostenible a una medida por una sola ventaja"),
}


ENGLISH_TOPICS = {
    "IN1M OA 01": "Global and explicit meaning in varied oral texts",
    "IN1M OA 02": "Key expressions, collocations and sound contrasts",
    "IN1M OA 03": "Purpose, relevant ideas, detail and problem-solution in listening",
    "IN1M OA 04": "Strategic listening, clarification and supported inference",
    "IN1M OA 05": "Coherent multimodal oral presentation for an audience",
    "IN1M OA 06": "Planning, repairing and reviewing spoken English",
    "IN1M OA 07": "Evidence-based personal response and discussion",
    "IN1M OA 08": "First-year secondary communicative functions in speech",
    "IN1M OA 09": "Global and explicit meaning in print and digital texts",
    "IN1M OA 10": "Purpose, structure and language in non-literary texts",
    "IN1M OA 11": "Theme, character, setting and plot in literary texts",
    "IN1M OA 12": "Strategic reading before, during and after a text",
    "IN1M OA 13": "Creative multimodal stories and relevant information",
    "IN1M OA 14": "Writing process across purposeful genres",
    "IN1M OA 15": "Writing to explain, narrate and express opinions",
    "IN1M OA 16": "First-year secondary communicative functions in writing",
    "EN1M OA 01": "Understanding varied literary and functional oral texts",
    "EN1M OA 02": "Purpose, detail, language and sound evidence in listening",
    "EN1M OA 03": "Purposeful listening, inference and clarification strategies",
    "EN1M OA 04": "Integrated literary and non-literary reading",
    "EN1M OA 05": "Language functions interpreted in meaningful texts",
    "EN1M OA 06": "Strategic reading before, during and after the text",
    "EN1M OA 07": "Critical and personal response across texts and cultures",
    "EN1M OA 08": "Audience-aware multimodal oral presentation",
    "EN1M OA 09": "Strategies for clear, fluent and repairable interaction",
    "EN1M OA 10": "Language functions in discussion and presentation",
    "EN1M OA 11": "Modeled multimodal writing for real audiences",
    "EN1M OA 12": "Language functions in connected written texts",
    "EN1M OA 13": "Independent writing process, revision and publication",
}


PRIOR = {
    "CN": "formular preguntas, construir modelos y evaluar explicaciones con evidencia trabajados en 8° básico",
    "HI": "contextualizar fuentes, relacionar escalas y construir argumentos multicausales trabajados en 8° básico",
    "IN": "understand and produce connected messages with evidence, interaction and revision in 8th grade",
    "EN": "understand and produce connected messages with evidence, interaction and revision in 8th grade",
}

VOCABULARY = {
    "CN": "pregunta, variable, medición, evidencia, patrón, sistema, modelo, mecanismo, conclusión, validez, incertidumbre, limitación",
    "HI": "fuente, procedencia, contexto, temporalidad, territorio, escala, actor, multicausalidad, continuidad, cambio, perspectiva, argumento",
    "IN": "purpose, audience, gist, detail, clue, collocation, inference, interaction, function, evidence, repair, revision",
    "EN": "purpose, audience, gist, detail, clue, collocation, inference, interaction, function, evidence, repair, revision",
}

STAGES = {
    "CN": ("Formular una pregunta investigable", "Examinar evidencia y representaciones", "Construir o contrastar un modelo", "Investigar relaciones entre variables", "Explicar patrones y mecanismos", "Evaluar límites, seguridad e implicancias", "Comunicar una explicación fundamentada"),
    "HI": ("Situar tiempo, espacio y problema", "Contextualizar y seleccionar fuentes", "Relacionar cambio, continuidad y territorio", "Contrastar actores, causas y perspectivas", "Construir un argumento con evidencia", "Evaluar proyecciones y límites", "Comunicar una explicación histórica, geográfica o ciudadana"),
    "IN": ("Recognize purpose and context", "Locate precise evidence", "Use a strategy or language function", "Communicate through an information gap", "Respond independently", "Review and transfer"),
    "EN": ("Recognize purpose and context", "Locate precise evidence", "Model a useful strategy", "Communicate through an information gap", "Respond independently", "Review and transfer"),
}

ENGLISH_MISCONCEPTIONS = {
    "IN": ("translate every word before constructing meaning", "recite language without listening or adapting to the audience", "treat accent, speed or immediate accuracy as intelligence"),
    "EN": ("translate every word before constructing meaning", "copy a model without making choices for purpose and audience", "correct grammar before meaning, evidence and organization are clear"),
}


def _english_anchor(code: str, topic: str) -> str:
    prefix = code[:2]
    number = int(code.rsplit(" ", 1)[-1])
    if prefix == "IN" and number <= 4 or prefix == "EN" and number <= 3:
        return f"an original teacher-read audio for {topic.lower()}, a replay plan, listening grid and transcript released only after the final listen"
    if prefix == "IN" and number in {5, 6, 7, 8} or prefix == "EN" and number in {7, 8, 9, 10}:
        return f"fictional information-gap cards, useful chunks, audience roles and a paper storyboard for {topic.lower()}"
    if prefix == "IN" and number in {9, 10, 11, 12} or prefix == "EN" and number in {4, 5, 6}:
        return f"short authorized literary and functional texts with numbered paragraphs, visuals and an essential glossary for {topic.lower()}"
    return f"fictional writing briefs, genre models, audience cards and a meaning-first revision checklist for {topic.lower()}"


COUNTS = {}
for item in CATALOG["classes"]:
    if item["course_order"] == 9 and item["subject_slug"] in TARGET_SLUGS and not item["oa_code"].startswith("de "):
        COUNTS[item["oa_code"]] = COUNTS.get(item["oa_code"], 0) + 1

RECORDS = {}
for record in SNAPSHOT["records"]:
    if record["course_order"] != 9 or record["subject_slug"] not in TARGET_SLUGS:
        continue
    for objective in record["objectives"]:
        if objective["code"].startswith("de "):
            continue
        RECORDS[objective["code"]] = {
            "slug": record["subject_slug"],
            "description": objective["description"],
            "url": objective["url"],
            "count": COUNTS[objective["code"]],
        }

PROFILES = set(DETAILS) | set(ENGLISH_TOPICS)
if set(RECORDS) != PROFILES:
    raise RuntimeError(f"Perfiles de 1° medio desalineados: faltan={sorted(set(RECORDS)-PROFILES)}; sobran={sorted(PROFILES-set(RECORDS))}")


def _profile(code: str) -> dict:
    prefix = code[:2]
    count = RECORDS[code]["count"]
    if code in DETAILS:
        detail = DETAILS[code]
        topic, anchor, misconception = detail["topic"], detail["anchor"], detail["misconception"]
    else:
        topic = ENGLISH_TOPICS[code]
        anchor = _english_anchor(code, topic)
        misconception = ENGLISH_MISCONCEPTIONS[prefix][sum(ord(char) for char in code) % 3]
    return {
        "topic": topic,
        "prior": PRIOR[prefix],
        "vocabulary": VOCABULARY[prefix],
        "anchor": anchor,
        "misconception": misconception,
        "focuses": [f"{stage}: {topic}" for stage in STAGES[prefix][:count]],
    }


def _retarget_links(lesson: dict, prefix: str) -> None:
    old = {"CN": "CN03", "HI": "HI03", "IN": "EN03", "EN": "EN03"}[prefix]
    new = {"CN": "CN1M", "HI": "HI1M", "IN": "IN1M", "EN": "EN1M"}[prefix]
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
            maker_code = code.replace("IN1M", "EN1M", 1)
            lesson = applied_lesson(maker_code, index, profile)
            (english_voice if prefix == "IN" else proposal_voice)(lesson, profile, index, prefix)
        _retarget_links(lesson, prefix)
        lessons.append(lesson)
    record = RECORDS[code]
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": (
            f"{profile['topic']} parte de {profile['prior']} y avanza mediante decisiones propias de la disciplina. "
            f"Cada clase cambia fuentes, materiales, representaciones y evidencias, y enfrenta la confusión «{profile['misconception']}»."
        ),
        "prerequisites": profile["prior"],
        "vocabulary": profile["vocabulary"],
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
    result["generated_for"] = "1-medio-ciencias-historia-ingles"
    return result


SEQUENCES = {code: True for code in RECORDS}

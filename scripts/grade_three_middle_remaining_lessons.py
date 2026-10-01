"""Complete the remaining third-year secondary sequences.

Official objective wording and URLs come from the checked-in MINEDUC snapshot.
The topics, classroom progressions, evidence, misconceptions and safeguards in
this module are original pedagogical elaborations for this repository.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
CATALOG = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
CORE_SLUGS = {"matematica-3o-medio", "lengua-literatura-3o-medio"}


TOPICS_BY_SUBJECT = {
    "ambiente-sostenibilidad": [
        "Ciclo de vida y consumo sostenible",
        "Proyectos locales para el uso sostenible de recursos",
        "Modelación del cambio climático en ecosistemas",
    ],
    "artes-visuales": [
        "Experimentación en ilustración, audiovisual y multimedia",
        "Creación visual y riesgo creativo",
        "Creación desde referentes artísticos y culturales",
        "Interpretación de propósitos expresivos contemporáneos",
        "Juicios estéticos sobre obras contemporáneas",
        "Evaluación crítica de procesos y proyectos visuales",
        "Gestión y difusión de obras visuales y multimediales",
    ],
    "bienestar-salud": [
        "Factores biológicos, ambientales y sociales de la salud",
        "Comparación informada de sistemas y prácticas de medicina",
        "Transmisión de agentes infecciosos y prevención basada en evidencia",
    ],
    "chile-region-latinoamericana": [
        "Migraciones, urbanización, diversidad e interculturalidad",
        "Democracias, transiciones y derechos humanos en América Latina",
        "Desafíos económicos y sociales latinoamericanos",
        "Pueblos indígenas y relaciones con los Estados",
        "Medioambiente y sustentabilidad en Chile y América Latina",
        "Integración y cooperación latinoamericana",
        "Propuestas locales para desafíos regionales",
    ],
    "danza": [
        "Conciencia corporal y lenguaje de la danza",
        "Comunicación de ideas y emociones mediante movimiento",
        "Creación individual y colectiva de danza",
        "Interpretación estética y contextual de obras de danza",
        "Evaluación crítica de procesos y obras de danza",
        "Gestión y difusión de proyectos de danza",
    ],
    "educacion-ciudadana-3-medio": [
        "Fundamentos de democracia, ciudadanía y libertades",
        "Acceso a la justicia y sistema judicial",
        "Riesgos contemporáneos para la democracia",
        "Relaciones entre Estado, mercado y justicia económica",
        "Defensa y exigibilidad de los derechos humanos",
        "Participación, bien común y tradiciones políticas",
        "Territorio, justicia social y justicia ambiental",
        "Ejercicio democrático y convivencia escolar",
    ],
    "educacion-fisica-salud-1": [
        "Habilidades motrices especializadas, creatividad y seguridad",
        "Evaluación de estrategias y tácticas motrices",
        "Diseño y aplicación de un plan personal de entrenamiento",
        "Proyectos comunitarios de bienestar y vida activa",
        "Factores que favorecen estilos de vida activos",
    ],
    "educacion-fisica-salud-2": [
        "Evaluación de habilidades motrices especializadas",
        "Organización de estrategias y tácticas para un juego inteligente",
        "Aplicación responsable de un plan de entrenamiento",
        "Evaluación de programas comunitarios de bienestar",
        "Oportunidades sociales para una vida activa y saludable",
    ],
    "filosofia-3-medio": [
        "Origen, sentido y preguntas del quehacer filosófico",
        "Perspectivas filosóficas, vida cotidiana y visiones de mundo",
        "Preguntas ontológicas sobre el ser y la realidad",
        "Preguntas epistemológicas sobre conocimiento, ciencia y verdad",
        "Diálogo sobre problemas ontológicos y epistemológicos",
        "Argumentación, validez y razonamiento filosófico",
    ],
    "filosofia-4o-medio": [
        "Alcances, límites y fines de la filosofía",
        "Preguntas éticas sobre justicia, libertad e igualdad",
        "Diálogo filosófico sobre ética y política contemporáneas",
        "Evaluación de argumentos, validez y falacias",
        "Impacto actual de ideas ontológicas, epistemológicas y éticas",
    ],
    "ingles-3o-medio": [
        "Central information and cultural perspectives",
        "Clear texts and respectful critical positions",
        "Language resources for critical comprehension and production",
        "Fluent interaction, worldviews and identity",
    ],
    "mundo-global": [
        "Migraciones contemporáneas, causas e impactos",
        "Economía global, trabajo, comercio y consumo",
        "Cambio climático, controversias y responsabilidades",
        "Desastres socionaturales, vulnerabilidad y gestión del riesgo",
        "Transformaciones contemporáneas del Estado-nación",
        "Conflictos internacionales y posibilidades de resolución",
        "Propuestas locales frente a problemas globales",
    ],
    "musica": [
        "Experimentación con estilos y producción musical contemporánea",
        "Creación musical, emociones e ideas",
        "Interpretación de repertorios y estilos musicales",
        "Análisis de propósitos expresivos en obras musicales",
        "Juicios estéticos musicales fundamentados",
        "Evaluación crítica de procesos y resultados musicales",
        "Gestión y difusión de obras e interpretaciones musicales",
    ],
    "seguridad-prevencion-autocuidado": [
        "Sustancias químicas cotidianas, riesgos y seguridad",
        "Soluciones para reducir amenazas en hogar y trabajo",
        "Riesgos locales, prevención, mitigación y adaptación",
    ],
    "teatro": [
        "Cuerpo, gesto y voz en la expresión dramática",
        "Creación de ejercicios dramáticos individuales y colectivos",
        "Interpretación teatral para un público específico",
        "Propósitos expresivos y contexto de obras teatrales",
        "Evaluación crítica de procesos y obras teatrales",
        "Gestión y difusión de proyectos teatrales",
    ],
    "tecnologia-sociedad": [
        "Proyectos tecnológicos para problemas personales y locales",
        "Avances tecnológicos y ampliación de capacidades humanas",
        "Riesgos, beneficios y límites de la tecnología",
    ],
}


SUBJECT_PROFILES = {
    "ambiente-sostenibilidad": {
        "purpose": "Investigar sistemas socioambientales, modelar cambio climático y diseñar respuestas locales sostenibles basadas en evidencia.",
        "continuity": "Profundiza la indagación científica de 2° medio mediante ciclo de vida, modelación ecosistémica y decisiones de sostenibilidad situadas.",
        "barrier": "proponer acciones ambientales generales sin datos, escala, actores, viabilidad ni forma de comprobar su efecto",
        "outcomes": ["analizar ciclos de vida completos", "diseñar proyectos locales con evidencia", "modelar efectos climáticos y evaluar soluciones"],
        "method": "Trabaja con datos trazables, modelos que declaran supuestos y proyectos que comparan impacto, viabilidad y seguimiento.",
        "evidence": "informe, modelo o proyecto individual que relaciona evidencia, sistema, decisión, impacto y limitaciones",
        "domain": "science",
    },
    "artes-visuales": {
        "purpose": "Experimentar, crear, interpretar, evaluar y difundir ilustraciones, obras audiovisuales y proyectos multimediales contemporáneos.",
        "continuity": "Amplía creación y apreciación de 2° medio hacia medios contemporáneos, riesgo creativo, juicio estético y gestión de difusión.",
        "barrier": "copiar referentes o valorar por gusto sin justificar decisiones de lenguaje visual, contexto, materialidad y propósito",
        "outcomes": ["experimentar con medios visuales diversos", "crear desde decisiones propias", "argumentar y evaluar con criterios estéticos", "gestionar difusión con autoría y consentimiento"],
        "method": "Alterna observación atribuida, pruebas materiales, registro de proceso, creación autónoma y crítica descriptiva.",
        "evidence": "obra, proyecto o análisis visual individual con decisiones documentadas, referente atribuido y justificación estética",
        "domain": "visual",
    },
    "bienestar-salud": {
        "purpose": "Analizar factores de salud, comparar prácticas médicas y evaluar prevención de enfermedades infecciosas mediante evidencia confiable.",
        "continuity": "Integra biología, ambiente y sociedad con lectura crítica de evidencia sanitaria, sin diagnosticar ni prescribir tratamientos.",
        "barrier": "convertir correlaciones, testimonios o tradiciones en causalidad clínica y recomendaciones personales sin evidencia ni competencia profesional",
        "outcomes": ["analizar determinantes de salud", "comparar medicinas con respeto y evidencia", "explicar transmisión y evaluar prevención"],
        "method": "Usa casos ficticios, datos agregados y fuentes sanitarias identificadas; distingue evidencia, incertidumbre, práctica cultural y decisión clínica.",
        "evidence": "análisis individual que evalúa evidencia, factores, mecanismos, alcances y límites sin diagnosticar personas",
        "domain": "science",
    },
    "chile-region-latinoamericana": {
        "purpose": "Investigar procesos sociales, políticos, económicos, culturales y ambientales de Chile y América Latina desde perspectivas y fuentes diversas.",
        "continuity": "Eleva el análisis histórico y territorial de 2° medio hacia problemas regionales contemporáneos, indicadores y propuestas locales.",
        "barrier": "generalizar América Latina, borrar diferencias territoriales o emitir juicios sin contextualizar fuentes, indicadores y perspectivas",
        "outcomes": ["comparar procesos regionales", "usar indicadores y fuentes situadas", "analizar pueblos y Estados sin estereotipos", "diseñar propuestas locales viables"],
        "method": "Contrasta mapas, series, testimonios públicos y documentos institucionales, distinguiendo evidencia, perspectiva, escala y límite.",
        "evidence": "explicación o propuesta individual con fuentes contextualizadas, comparación regional y límites explícitos",
        "domain": "social",
    },
    "danza": {
        "purpose": "Explorar el movimiento, crear e interpretar obras de danza y gestionar su difusión con conciencia corporal, expresividad y cuidado.",
        "continuity": "Traslada aprendizajes artísticos y motrices previos a creación coreográfica, apreciación estética y puesta en escena.",
        "barrier": "imitar formas corporales, imponer exposición o evaluar cuerpos en lugar de decisiones de movimiento, proceso y propósito expresivo",
        "outcomes": ["explorar movimiento de modo seguro", "crear composiciones propias", "interpretar y evaluar con criterios", "difundir con consentimiento"],
        "method": "Trabaja con consignas abiertas, variantes accesibles, registro de decisiones, retroalimentación descriptiva y derecho a no exponerse públicamente.",
        "evidence": "secuencia, interpretación o análisis individual con decisión corporal propia, propósito y reflexión de proceso",
        "domain": "dance",
    },
    "educacion-ciudadana-3-medio": {
        "purpose": "Comprender democracia, justicia, derechos, economía, territorio y participación para deliberar y actuar responsablemente en comunidad.",
        "continuity": "Profundiza ciudadanía de 2° medio mediante marcos conceptuales, casos públicos, deliberación plural y ejercicio democrático protegido.",
        "barrier": "reducir deliberación a opinión partidista, exigir experiencias personales o presentar instituciones y derechos sin casos ni evidencia",
        "outcomes": ["explicar fundamentos democráticos", "investigar justicia y derechos", "evaluar Estado, mercado y territorio", "participar con reglas y bien común"],
        "method": "Usa casos públicos no partidistas, fuentes normativas, datos y protocolos de deliberación que separan argumentos de identidades personales.",
        "evidence": "análisis, deliberación o propuesta individual con conceptos ciudadanos, evidencia, contrapunto y acción democrática segura",
        "domain": "citizenship",
    },
    "educacion-fisica-salud-1": {
        "purpose": "Aplicar habilidades especializadas, evaluar tácticas, diseñar entrenamiento y promover oportunidades comunitarias de vida activa.",
        "continuity": "Avanza desde la práctica de 2° medio hacia autonomía, evaluación táctica, planificación y liderazgo inclusivo.",
        "barrier": "equiparar aprendizaje con rendimiento, comparar cuerpos o prescribir una carga común sin autorregulación, acceso ni seguridad",
        "outcomes": ["aplicar habilidades seguras", "evaluar decisiones tácticas", "diseñar entrenamiento autorregulado", "promover participación comunitaria"],
        "method": "Usa estaciones y juegos sin eliminación, variantes equivalentes, escala de esfuerzo y decisiones basadas en evidencia funcional privada.",
        "evidence": "desempeño o plan individual con decisión motriz, regulación, seguridad, evaluación y ajuste",
        "domain": "physical",
    },
    "educacion-fisica-salud-2": {
        "purpose": "Evaluar habilidades, organizar tácticas, aplicar entrenamiento y valorar programas comunitarios para una vida activa diversa.",
        "continuity": "Profundiza autonomía y evaluación desde desempeño propio, roles rotativos y análisis crítico de oportunidades de actividad física.",
        "barrier": "evaluar solo resultados competitivos o asumir que una práctica, cuerpo, carga y oportunidad sirven igual para todas las personas",
        "outcomes": ["evaluar habilidades propias", "organizar juego inteligente", "aplicar entrenamiento responsable", "evaluar programas y oportunidades"],
        "method": "Combina práctica segura, registro privado, roles diversos y evaluación de programas con criterios de acceso, bienestar y sostenibilidad.",
        "evidence": "desempeño, registro o evaluación individual con criterios funcionales, ajuste seguro y reflexión contextual",
        "domain": "physical",
    },
    "filosofia-3-medio": {
        "purpose": "Formular preguntas filosóficas, analizar perspectivas y argumentar rigurosamente sobre realidad, conocimiento y verdad.",
        "continuity": "Transforma la argumentación de 2° medio en problematización conceptual, lectura filosófica y diálogo razonado.",
        "barrier": "confundir filosofía con opinión espontánea, citar autoridad sin reconstruir argumentos o atacar a quien sostiene una postura",
        "outcomes": ["caracterizar el filosofar", "analizar perspectivas", "formular preguntas ontológicas y epistemológicas", "evaluar argumentos"],
        "method": "Parte de problemas y fragmentos breves atribuidos, reconstruye premisas y conceptos y sostiene diálogo protegido con objeciones.",
        "evidence": "pregunta, mapa argumental o intervención individual que define conceptos, ofrece razones y responde una objeción",
        "domain": "philosophy",
    },
    "filosofia-4o-medio": {
        "purpose": "Examinar praxis, ética y política, evaluar argumentos y relacionar ideas filosóficas con problemas contemporáneos.",
        "continuity": "Proyecta ontología y epistemología hacia acción, ética, cultura, trabajo, tecnología, política y artes.",
        "barrier": "usar dilemas sensibles para forzar exposición, etiquetar posiciones o declarar falacia sin reconstruir el razonamiento",
        "outcomes": ["explicar límites de la filosofía", "formular preguntas éticas", "dialogar sobre problemas contemporáneos", "evaluar argumentos e impactos"],
        "method": "Usa casos ficticios o públicos, textos atribuidos, mapas argumentales y múltiples formas de representación sin exigir confesiones.",
        "evidence": "análisis filosófico individual con problema, conceptos, argumento, objeción, respuesta y alcance",
        "domain": "philosophy",
    },
    "ingles-3o-medio": {
        "purpose": "Comprender y producir textos claros en inglés para conocer perspectivas culturales, construir posturas críticas e interactuar con fluidez.",
        "continuity": "Eleva la comunicación de 2° medio hacia postura crítica, contraste de visiones de mundo y mayor autonomía estratégica.",
        "barrier": "traducir palabra por palabra, memorizar un texto completo o evaluar acento en lugar de significado, propósito y reparación comunicativa",
        "outcomes": ["identify central information", "express a respectful critical position", "use language resources strategically", "interact across worldviews"],
        "method": "Uses short authorized input, information gaps, visible language support, rehearsal and revision for a real communicative purpose.",
        "evidence": "comprehensible individual response that uses evidence from input, adapts to purpose and revises meaning",
        "domain": "english",
    },
    "mundo-global": {
        "purpose": "Analizar migraciones, economía, clima, riesgos, Estados y conflictos para comprender interdependencias globales y diseñar respuestas locales.",
        "continuity": "Amplía el análisis territorial de 2° medio hacia escalas globales, controversias, responsabilidades y cooperación.",
        "barrier": "explicar procesos globales con una sola causa, fuente o actor, o trasladar una conclusión de escala sin revisar contexto",
        "outcomes": ["analizar procesos globales multicausales", "usar conceptos económicos y políticos", "evaluar vulnerabilidad y responsabilidad", "proponer respuestas locales"],
        "method": "Contrasta mapas, indicadores, fuentes institucionales y perspectivas, haciendo visibles escala, causalidad, actor y límite.",
        "evidence": "explicación o propuesta individual con relaciones multicausales, fuentes trazables, escalas y limitaciones",
        "domain": "social",
    },
    "musica": {
        "purpose": "Experimentar, crear, interpretar, analizar, evaluar y difundir música contemporánea mediante decisiones audibles y contextualizadas.",
        "continuity": "Profundiza escucha, interpretación y creación de 2° medio con producción, estilos, juicio estético y gestión de difusión.",
        "barrier": "confundir calidad con volumen, velocidad o virtuosismo y emitir juicios sin evidencia audible ni contexto",
        "outcomes": ["experimentar con producción musical", "crear e interpretar con propósito", "argumentar juicios estéticos", "evaluar y difundir con autoría"],
        "method": "Alterna escucha atribuida, ensayos breves, variación de un elemento, registro, autoevaluación y decisiones de difusión segura.",
        "evidence": "interpretación, creación o análisis individual que localiza evidencia audible y justifica una decisión musical",
        "domain": "music",
    },
    "seguridad-prevencion-autocuidado": {
        "purpose": "Investigar riesgos químicos, tecnológicos y socionaturales y diseñar medidas de prevención, mitigación y adaptación.",
        "continuity": "Integra ciencia escolar con lectura de etiquetas, modelos de riesgo y capacidades comunitarias sin realizar prácticas peligrosas.",
        "barrier": "manipular sustancias o sistemas reales, equiparar peligro con riesgo o proponer protocolos sin fuente, responsables ni prueba segura",
        "outcomes": ["analizar sustancias y seguridad", "diseñar soluciones preventivas", "modelar riesgo local y evaluar capacidades"],
        "method": "Trabaja con fichas, fotografías y modelos; no manipula peligros, y valida medidas mediante fuentes institucionales y simulaciones.",
        "evidence": "informe, modelo o protocolo individual que identifica peligro, exposición, vulnerabilidad, medida y límite",
        "domain": "science",
    },
    "teatro": {
        "purpose": "Explorar lenguaje teatral, crear e interpretar escenas, analizar propósitos y gestionar la difusión de proyectos dramáticos.",
        "continuity": "Articula expresión, cuerpo, voz, dramaturgia, puesta en escena y audiencia con mayor autonomía y evaluación crítica.",
        "barrier": "forzar exposición, confundir actuación con personalidad o evaluar estereotipos y volumen en lugar de decisiones escénicas",
        "outcomes": ["explorar cuerpo, gesto y voz", "crear e interpretar escenas", "inferir propósitos expresivos", "evaluar y difundir proyectos"],
        "method": "Usa ficción y consentimiento, roles escénicos y no escénicos equivalentes, ensayo por capas y retroalimentación descriptiva.",
        "evidence": "escena, diseño o análisis individual con decisión teatral, propósito, audiencia y revisión de proceso",
        "domain": "theater",
    },
    "tecnologia-sociedad": {
        "purpose": "Diseñar proyectos tecnológicos y evaluar cómo la tecnología amplía capacidades mientras produce riesgos, beneficios y límites.",
        "continuity": "Profundiza diseño y evaluación de 2° medio mediante investigación, modelación y análisis multidimensional de impactos.",
        "barrier": "proponer tecnología como solución automática sin usuario, criterio, prueba, accesibilidad, privacidad ni impacto",
        "outcomes": ["diseñar proyectos situados", "explicar avances mediante modelos", "evaluar riesgos y beneficios multidimensionales"],
        "method": "Define necesidad y usuario, compara alternativas, representa, prueba de modo seguro y revisa impactos y límites.",
        "evidence": "diseño, modelo o evaluación individual con usuario, criterios, prueba, riesgos, beneficios y mejora",
        "domain": "technology",
    },
}


STAGES = {
    "mathematics": ("Precisar condiciones y objetos", "Representar de dos maneras", "Desarrollar una estrategia", "Justificar relaciones", "Comprobar y comparar", "Modelar o transferir con límites"),
    "language": ("Situar corpus, género y propósito", "Formular una lectura o problema", "Analizar recursos y evidencia", "Contrastar interpretaciones o discursos", "Planificar una respuesta para una audiencia", "Producir, revisar y editar", "Comunicar con fuentes y límites"),
    "science": ("Delimitar pregunta y sistema", "Evaluar fuentes y variables", "Construir o interpretar un modelo", "Analizar evidencia", "Comparar soluciones", "Comunicar límites y decisión"),
    "social": ("Contextualizar actores, tiempo y espacio", "Interrogar fuentes e indicadores", "Comparar causas y perspectivas", "Explicar relaciones y consecuencias", "Evaluar alternativas", "Comunicar una conclusión situada"),
    "visual": ("Observar referentes y propósito", "Explorar soportes y procedimientos", "Tomar una decisión visual", "Desarrollar una propuesta propia", "Criticar y revisar con criterios", "Montar, atribuir y difundir"),
    "dance": ("Explorar movimiento con conciencia", "Combinar espacio, tiempo y energía", "Componer una frase propia", "Interpretar propósito y contexto", "Evaluar y revisar el proceso", "Presentar o difundir con consentimiento"),
    "citizenship": ("Precisar conceptos y derechos", "Investigar un caso público", "Contrastar perspectivas y evidencia", "Deliberar con razones", "Diseñar una acción democrática", "Evaluar efectos y límites"),
    "physical": ("Diagnosticar de forma privada y segura", "Elegir una respuesta motriz", "Aplicar estrategia o plan", "Registrar regulación y resultado", "Evaluar y ajustar", "Transferir con autonomía e inclusión"),
    "philosophy": ("Problematizar una situación", "Definir conceptos", "Reconstruir una perspectiva", "Formular y evaluar argumentos", "Responder objeciones", "Comunicar una posición revisable"),
    "english": ("Activate purpose and prior knowledge", "Notice central meaning and clues", "Rehearse useful language", "Communicate a critical position", "Repair and revise meaning", "Interact across perspectives"),
    "music": ("Escuchar y reconocer rasgos", "Explorar recursos de producción", "Ensayar una decisión musical", "Interpretar, crear o analizar", "Registrar y ajustar", "Evaluar, atribuir y difundir"),
    "theater": ("Explorar cuerpo, gesto y voz", "Construir situación y personaje", "Ensayar decisiones escénicas", "Interpretar propósito y contexto", "Evaluar y revisar", "Presentar o difundir con consentimiento"),
    "technology": ("Definir necesidad, usuario y criterio", "Investigar alternativas y restricciones", "Representar y planificar", "Probar o modelar con seguridad", "Evaluar impactos y límites", "Mejorar y comunicar"),
}

VOCABULARY = {
    "mathematics": "condición, representación, conjetura, propiedad, modelo, parámetro, estrategia, argumento, comprobación, límite",
    "language": "corpus, género, propósito, audiencia, contexto, evidencia, recurso, posicionamiento, interpretación, revisión",
    "science": "sistema, variable, evidencia, fuente, modelo, causalidad, incertidumbre, impacto, mitigación, limitación",
    "social": "actor, contexto, escala, territorio, proceso, indicador, perspectiva, causalidad, continuidad, consecuencia",
    "visual": "referente, soporte, procedimiento, lenguaje visual, composición, propósito, criterio, proceso, autoría, difusión",
    "dance": "cuerpo, espacio, tiempo, energía, dinámica, composición, interpretación, puesta en escena, criterio, difusión",
    "citizenship": "democracia, ciudadanía, libertad, derecho, Estado, justicia, participación, territorio, deliberación, bien común",
    "physical": "habilidad motriz, estrategia, táctica, carga, esfuerzo, recuperación, regulación, seguridad, inclusión, evaluación",
    "philosophy": "problema, pregunta, concepto, tesis, premisa, inferencia, validez, falacia, objeción, perspectiva",
    "english": "purpose, audience, central information, evidence, viewpoint, stance, interaction, fluency, repair, identity",
    "music": "ritmo, melodía, armonía, timbre, textura, forma, estilo, técnica, propósito, evidencia audible",
    "theater": "cuerpo, gesto, voz, personaje, conflicto, acción, espacio, puesta en escena, audiencia, propósito",
    "technology": "necesidad, usuario, criterio, restricción, modelo, prototipo, prueba, accesibilidad, riesgo, impacto",
}

MISCONCEPTIONS = {
    "mathematics": ("aplicar una regla sin comprobar sus condiciones", "confundir una representación con el objeto matemático", "aceptar un resultado sin interpretarlo ni verificarlo"),
    "language": ("resumir en lugar de interpretar o evaluar", "atribuir una intención sin evidencia textual ni contextual", "corregir solo la superficie sin revisar contenido y organización"),
    "science": ("confundir correlación con causalidad", "usar una fuente aislada como certeza", "ocultar supuestos y límites del modelo"),
    "social": ("explicar con una sola causa", "generalizar desde un caso", "tratar una fuente como neutral y completa"),
    "visual": ("copiar el referente", "confundir gusto con juicio", "difundir sin atribución ni consentimiento"),
    "dance": ("imitar una forma corporal ideal", "confundir intensidad con expresividad", "forzar exposición para evaluar"),
    "citizenship": ("confundir opinión con argumento", "presentar derechos como premios", "identificar participación solo con votar"),
    "physical": ("equiparar aprendizaje con rendimiento", "usar la misma carga para todas las personas", "evaluar cuerpos en vez de decisiones"),
    "philosophy": ("confundir perspectiva con opinión sin razones", "nombrar una falacia sin reconstruir el argumento", "atacar a la persona y no la tesis"),
    "english": ("translate every word before responding", "memorize without adapting to purpose", "treat accent imitation as fluency"),
    "music": ("confundir calidad con volumen o velocidad", "imitar sin decidir", "opinar sin evidencia audible"),
    "theater": ("confundir personaje con identidad personal", "usar volumen como único recurso", "evaluar exposición y no decisión escénica"),
    "technology": ("construir antes de definir el problema", "evaluar solo apariencia o novedad", "ignorar privacidad, acceso e impacto"),
}


COUNTS: dict[str, int] = {}
for item in CATALOG["classes"]:
    if item["course_order"] == 11 and item["subject_slug"] not in CORE_SLUGS:
        COUNTS[item["oa_code"]] = COUNTS.get(item["oa_code"], 0) + 1

RECORDS: dict[str, dict] = {}
for record in SNAPSHOT["records"]:
    slug = record["subject_slug"]
    if record["course_order"] != 11 or slug in CORE_SLUGS:
        continue
    topics = TOPICS_BY_SUBJECT.get(slug, [])
    if len(topics) != len(record["objectives"]):
        raise RuntimeError(f"{slug}: {len(topics)} temas para {len(record['objectives'])} OA oficiales")
    for topic, objective in zip(topics, record["objectives"]):
        RECORDS[objective["code"]] = {
            "slug": slug,
            "subject": record["subject"],
            "axis": objective["axis"],
            "description": objective["description"],
            "url": objective["url"],
            "count": COUNTS[objective["code"]],
            "topic": topic,
        }

if set(TOPICS_BY_SUBJECT) != set(SUBJECT_PROFILES):
    raise RuntimeError("Los perfiles y temas de asignatura de 3° medio no coinciden")
if len(RECORDS) != 85 or sum(item["count"] for item in RECORDS.values()) != 419:
    raise RuntimeError(f"Cobertura restante de 3° medio inesperada: {len(RECORDS)} OA, {sum(item['count'] for item in RECORDS.values())} clases")


def _profile_from_record(code: str, record: dict, subject: dict) -> dict:
    domain = subject["domain"]
    count = record["count"]
    seed = sum(ord(char) for char in code)
    anchor = (
        f"a short, original and attributed oral, written or multimodal text about {record['topic'].lower()}"
        if domain == "english"
        else f"un conjunto acotado y atribuido de casos, datos, modelos o producciones sobre {record['topic'].lower()}"
    )
    return {
        "topic": record["topic"],
        "domain": domain,
        "prior": subject["continuity"],
        "vocabulary": VOCABULARY[domain],
        "anchor": anchor,
        "misconception": MISCONCEPTIONS[domain][seed % len(MISCONCEPTIONS[domain])],
        "focuses": [f"{stage}: {record['topic']}" for stage in STAGES[domain][:count]],
    }


def _lesson(record: dict, index: int, profile: dict) -> dict:
    domain = profile["domain"]
    focus = profile["focuses"][index]
    action = focus[0].lower() + focus[1:]
    anchor = profile["anchor"]
    misconception = profile["misconception"]

    if domain == "mathematics":
        opening = f"Presenta {anchor} con datos, condiciones y una pregunta verificable. Cada estudiante registra una estimación, una representación inicial y qué necesita comprobar."
        model = f"Piensa en voz alta para {action}: conecta representaciones, nombra la propiedad utilizada, controla condiciones y confronta «{misconception}»."
        guided = f"Parejas resuelven una variante de {record['topic'].lower()} por dos vías, comparan pasos y localizan dónde una estrategia deja de ser válida."
        independent = f"Cada estudiante desarrolla {action} en un problema nuevo; interpreta el resultado, comprueba por otra representación y declara el alcance del procedimiento."
        ticket = "Escribe la decisión matemática central, una comprobación independiente y una condición bajo la cual el resultado cambiaría."
        support = "Reduce cantidad de datos, ofrece una representación equivalente y una lista de condiciones; conserva la decisión matemática y no completa el procedimiento."
        extension = "Cambia un parámetro, restricción o representación, formula una conjetura y determina si el argumento todavía se sostiene."
        evidence = f"Resolución matemática individual de «{focus.lower()}» con representación, estrategia, justificación, interpretación y comprobación."
        coordination = "El docente mantiene lenguaje y demanda matemática; los apoyos de acceso no sustituyen representación, razonamiento ni comprobación individual."
    elif domain == "language":
        opening = f"Presenta {anchor} con autoría, fecha, género y contexto. Cada estudiante anota una primera lectura, dos huellas precisas y una pregunta antes de interpretar o evaluar."
        model = f"Piensa en voz alta para {action}: distingue evidencia e inferencia, relaciona forma, contexto y efecto, y corrige «{misconception}»."
        guided = f"Parejas contrastan dos pasajes, textos o versiones sobre {record['topic'].lower()}; ensayan una interpretación o evaluación y la revisan ante evidencia contraria."
        independent = f"Cada estudiante desarrolla {action} con un corpus nuevo; cita de forma acotada, explica el efecto de una decisión discursiva y reconoce un límite."
        ticket = "Formula una conclusión interpretativa o crítica, dos evidencias precisas y una pregunta o contrapunto que obligue a revisarla."
        support = "Ofrece fragmentos numerados, lectura oral, glosario y organizador de evidencia e inferencia; no entrega la interpretación ni reescribe el producto."
        extension = "Agrega otro contexto, género, soporte o interpretación y revisa cómo cambia el efecto, la evaluación o la decisión de escritura."
        evidence = f"Interpretación, análisis o producción individual de «{focus.lower()}» con evidencia textual, contexto, decisión discursiva y revisión."
        coordination = "El docente resguarda selección legal y situada de textos, privacidad y pluralismo; biblioteca o apoyo lingüístico amplían acceso sin imponer una lectura."
    elif domain == "science":
        opening = f"Presenta {anchor} con procedencia, fecha y escala visibles. Cada estudiante separa observación, dato, pregunta e inferencia antes de explicar."
        model = f"Modela cómo {action}: identifica sistema, variables, evidencia y supuesto; contrasta la explicación con «{misconception}» y declara qué no permite concluir."
        guided = f"Equipos analizan una segunda evidencia segura sobre {record['topic'].lower()}, comparan patrones y revisan una conclusión sin manipular sustancias, cuerpos ni riesgos reales."
        independent = f"Cada estudiante resuelve un caso nuevo para {action}; construye tabla, modelo o argumento y cita la fuente, el dato decisivo y una limitación."
        ticket = "Escribe una conclusión, la evidencia que la sostiene y una condición o incertidumbre que limita su alcance."
        support = "Reduce variables, ofrece tabla accesible, glosario y modelo visual; conserva la decisión científica y no entrega la conclusión."
        extension = "Contrasta otra fuente o cambia una condición del modelo y explica si la conclusión se mantiene."
        evidence = f"Análisis científico individual de «{focus.lower()}» con evidencia, modelo o mecanismo, fuente y límite."
        coordination = "El docente resguarda seguridad y alcance científico; salud, prevención o especialistas intervienen solo según protocolo y sin diagnosticar estudiantes."
    elif domain in {"social", "citizenship", "philosophy"}:
        opening = f"Presenta {anchor} sin interpretación cerrada. Cada estudiante registra contexto, actor o tesis, evidencia disponible y una pregunta relevante."
        model = f"Piensa en voz alta para {action}: define conceptos, reconstruye relaciones o premisas, considera otra perspectiva y corrige «{misconception}»."
        guided = f"Parejas contrastan dos fuentes, argumentos o casos sobre {record['topic'].lower()}; distinguen hechos, interpretación, razones, escala y aspecto todavía abierto."
        independent = f"Cada estudiante desarrolla {action} en un caso nuevo mediante una explicación, mapa argumental o propuesta con evidencia, contrapunto y límites."
        ticket = "Formula una conclusión o tesis, una razón respaldada y una objeción o límite que deba considerarse."
        support = "Ofrece fragmentos breves, mapa conceptual o argumental, vocabulario y respuesta oral o gráfica; no asigna posiciones personales."
        extension = "Agrega una fuente, perspectiva, objeción o escala y revisa la conclusión sin borrar el desacuerdo razonado."
        evidence = f"Análisis individual de «{focus.lower()}» con conceptos, evidencia o premisas, perspectiva y conclusión revisable."
        coordination = "El docente modera casos públicos o ficticios y protege pluralismo, privacidad y derechos; deriva situaciones reales según protocolo."
    elif domain in {"visual", "dance", "music", "theater"}:
        medium = {"visual": "visual", "dance": "corporal y coreográfico", "music": "musical y audible", "theater": "teatral y escénico"}[domain]
        opening = f"Presenta {anchor} con autoría y contexto. Cada estudiante identifica un rasgo {medium}, su posible efecto y una pregunta antes de probar."
        model = f"Realiza una prueba parcial para {action}; cambia una variable {medium}, compara el efecto y aborda «{misconception}» sin imponer una solución estética."
        guided = f"En grupos pequeños producen dos versiones de {record['topic'].lower()}; reciben retroalimentación descriptiva y cada autor o intérprete decide qué revisar."
        independent = f"Cada estudiante crea, interpreta o analiza una respuesta propia para {action}; registra decisión, prueba, efecto y revisión."
        ticket = f"Muestra o describe una decisión {medium}, localiza su evidencia y explica qué conservaría o cambiaría."
        support = "Ofrece herramientas, roles, escalas y vías sensoriales o expresivas equivalentes; permite ensayo privado y nunca completa la obra ni fuerza exposición."
        extension = "Cambia material, energía, estilo, audiencia, espacio o medio y conserva el propósito mediante otra decisión."
        evidence = f"Producción, interpretación o análisis individual de «{focus.lower()}» con decisión {medium}, proceso y justificación."
        coordination = "El docente resguarda autoría, consentimiento, acceso y seguridad física o auditiva; los apoyos no sustituyen la decisión artística."
    elif domain == "physical":
        opening = f"Presenta una situación segura y accesible de {record['topic'].lower()}. Cada estudiante identifica meta, espacio, señal de detención y variante posible."
        model = f"Demuestra a velocidad de observación cómo {action}; verbaliza control, estrategia, esfuerzo y seguridad, y corrige «{misconception}» sin presentar un cuerpo ideal."
        guided = f"Practican {record['topic'].lower()} en estaciones sin eliminación, con roles rotativos y variantes equivalentes; la retroalimentación se refiere a decisiones observables."
        independent = f"Cada estudiante elige y ejecuta una variante para {action}, registra de forma privada su respuesta y ajusta desde evidencia funcional propia."
        ticket = "Representa o explica la decisión motriz, táctica o de regulación usada y la evidencia que llevó al ajuste."
        support = "Ajusta espacio, velocidad, contacto, implemento, rol o forma de registro; conserva la habilidad y evita comparaciones corporales."
        extension = "Cambia una regla, entorno, rol o carga y adapta la decisión manteniendo acceso y seguridad."
        evidence = f"Desempeño o plan individual de «{focus.lower()}» con autorregulación, seguridad, evaluación y ajuste."
        coordination = "El docente conduce progresión y seguridad; educación diferencial acuerda variantes y salud escolar actúa por protocolo, sin diagnosticar ni publicar datos corporales."
    elif domain == "english":
        opening = f"Present {anchor} once. Students identify purpose, central meaning and one clue before translating or preparing a full response."
        model = f"Think aloud in accessible English to {action}. Use an exact clue, useful language and context; address the misconception: {misconception}."
        guided = f"Pairs complete an information-gap or comparison about {record['topic'].lower()}, ask for clarification and revise one part for meaning and audience."
        independent = f"Each student completes a new task to {action}; they select support, communicate a position and repair meaning after checking the input."
        ticket = "Give a short response for today's purpose and identify the clue or language choice that supports it."
        support = "Keep chunks and visual clues available, allow rehearsal and alternative response modes, and do not penalize accent, wait time or self-correction."
        extension = "Change speaker, worldview, audience or purpose and adapt language while preserving the central message."
        evidence = f"Comprehensible individual response for «{focus.lower()}» with input evidence, purposeful language and revision."
        coordination = "El docente modela inglés comprensible y culturalmente situado; los apoyos facilitan acceso sin sustituir la intención comunicativa."
    else:
        opening = f"Presenta {anchor} como desafío. Antes de idear soluciones, cada estudiante define necesidad, usuario, criterio y restricción."
        model = f"Modela cómo {action}: representa la alternativa, anticipa una prueba segura y revisa «{misconception}» junto con accesibilidad, privacidad e impacto."
        guided = f"Equipos comparan o simulan dos alternativas para {record['topic'].lower()}, prueban un criterio y registran también evidencia que contradice su expectativa."
        independent = f"Cada estudiante resuelve una variante para {action}; entrega representación, decisión, resultado de prueba, impacto y mejora."
        ticket = "Nombra necesidad, criterio decisivo, evidencia de prueba y un riesgo o mejora todavía pendiente."
        support = "Ofrece materiales o interfaces accesibles, plantillas de organización y alternativa sin conectividad; no ejecuta la decisión del estudiante."
        extension = "Cambia usuario, recurso, dato o restricción y adapta la solución antes de volver a probar."
        evidence = f"Diseño, modelo o evaluación individual de «{focus.lower()}» con usuario, criterios, prueba, impactos y revisión."
        coordination = "El docente conduce diseño y seguridad física y digital; coordinación TIC protege cuentas, datos y autoría."

    if domain == "english":
        purpose = f"Help students {action} through meaningful English, evidence from the input and purposeful revision."
        goal = f"Today I will {action}; I will use evidence, communicate for a purpose and revise meaning when needed."
        materials = f"{anchor}; visible language support, planning grid and an offline alternative. Check attribution, accessibility and privacy."
        criteria = [
            f"completes «{focus.lower()}» for the stated purpose",
            "uses precise evidence or language from the input",
            "communicates comprehensibly and revises one decision",
        ]
        next_step = "Move on when purpose, evidence and message align; otherwise change access, model another example and collect new evidence without labelling the learner."
        short_version = "Keep the specific input, brief modelling, guided rehearsal, individual evidence and exit response; reduce length or turns, not the communicative demand."
        home_task = "Observe or create a short, safe example using available resources. No purchase, account, internet access or disclosure of personal information is required."
        complementary = [
            "Recovery: reduce input length or available choices, then return to the complete communicative task.",
            f"Error analysis: revise a fictional response that shows this misconception: {misconception}.",
            "Transfer: change audience, viewpoint, mode or purpose and adapt the message.",
        ]
        difficulty_actions = [
            {"signal": "Responds before examining the input", "action": "Ask the learner to locate one exact clue before choosing or composing a response.", "check": "The new response cites a relevant clue."},
            {"signal": misconception.capitalize(), "action": support, "check": "The learner completes a new task without repeating the misconception and explains the change."},
            {"signal": "Completes the task but cannot justify a language choice", "action": "Ask for a comparison with one alternative and the clue that decided between them.", "check": "The explanation makes the communicative decision visible and revisable."},
        ]
    else:
        purpose = f"Desarrollar {record['topic'].lower()} mediante {action}, con una experiencia disciplinar específica, segura y revisable."
        goal = f"Hoy voy a {action}; justificaré una decisión con evidencia y reconoceré sus límites."
        materials = f"{anchor}; pizarra, cuaderno, pauta de trabajo y alternativa sin conectividad. Verifica procedencia, accesibilidad y seguridad."
        criteria = [f"desarrolla «{focus.lower()}» en el caso propuesto", "usa una decisión y evidencia propias de la disciplina", "explica el alcance, revisa un error o reconoce una limitación"]
        next_step = "Avanza cuando decisión, evidencia y explicación coinciden; si no, localiza la barrera, modela otro caso y recoge una nueva evidencia sin etiquetar a la persona."
        short_version = "Conserva el caso específico, modelado breve, práctica guiada, evidencia individual y ticket; reduce cantidad o turnos, no la demanda del OA."
        home_task = "Observa, representa o explica un caso seguro con recursos disponibles. No requiere compras, internet ni revelar datos personales, familiares, corporales o políticos."
        complementary = [
            "Recuperación: reduce variables o elementos y vuelve después al desafío completo.",
            f"Análisis de error: revisa un caso ficticio que muestra esta confusión: {misconception}.",
            "Transferencia: cambia contexto, fuente, audiencia, escala o restricción y revisa la decisión.",
        ]
        difficulty_actions = [
            {"signal": "Responde antes de examinar el caso o la evidencia", "action": "Pide localizar primero el dato, rasgo, fuente, criterio o condición que utilizará.", "check": "La nueva respuesta cita una evidencia pertinente."},
            {"signal": misconception.capitalize(), "action": support, "check": "Resuelve un caso nuevo sin repetir la confusión y explica la diferencia."},
            {"signal": "Completa la actividad, pero no justifica su decisión", "action": "Solicita comparar con una alternativa y nombrar el criterio decisivo.", "check": "La explicación permite reconstruir y revisar la decisión."},
        ]

    return {
        "title": focus,
        "purpose": purpose,
        "goal": goal,
        "opening": opening,
        "model": model,
        "guided": guided,
        "independent": independent,
        "ticket": ticket,
        "materials": materials,
        "support": support,
        "extension": extension,
        "evidence": evidence,
        "criteria": criteria,
        "next_step": next_step,
        "short_version": short_version,
        "home_task": home_task,
        "complementary": complementary,
        "difficulty_actions": difficulty_actions,
        "specialist_coordination": coordination,
        "transversal": [],
    }


def build_sequence_from_record(code: str, record: dict, subject: dict, prior_level: str) -> dict:
    """Build a sourced sequence for one upper-secondary objective record."""
    profile = _profile_from_record(code, record, subject)
    lessons = [_lesson(record, index, profile) for index in range(record["count"])]
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": (
            f"{profile['topic']} recupera aprendizajes de {prior_level} y avanza mediante decisiones propias de la disciplina. "
            f"La secuencia cambia casos, fuentes y productos, y enfrenta la confusión «{profile['misconception']}»."
        ),
        "prerequisites": profile["prior"],
        "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"Eje oficial · progresión pedagógica interna en {len(lessons)} clases"],
            "unit_origin": "Organización pedagógica interna derivada del eje y del objetivo; no se presenta como unidad oficial del programa.",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del objetivo oficial.",
            "source": record["url"],
        },
        "lessons": lessons,
    }


def build_sequence(code: str) -> dict | None:
    if code not in RECORDS:
        return None
    record = RECORDS[code]
    return build_sequence_from_record(code, record, SUBJECT_PROFILES[record["slug"]], "2° medio")


SEQUENCES = {code: True for code in RECORDS}

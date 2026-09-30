"""Specific eighth-grade Science, History, Visual Arts and Music sequences.

Official OA text and URLs come from the checked-in MINEDUC snapshot. The
topics, classroom anchors, progressions, misconceptions and safeguards are
original pedagogical elaborations for this repository.
"""
from __future__ import annotations

import json
from pathlib import Path

try:
    from grade_three_arts_pe_english_indigenous_lessons import _lesson as applied_lesson
    from grade_three_music_orientation_technology_lessons import _lesson as music_lesson
    from grade_three_science_history_lessons import _lesson as inquiry_lesson
    from grade_four_remaining_lessons import build_transversal_integration as base_integration
    from grade_seven_next_five_lessons import _natural_voice
except ImportError:
    from scripts.grade_three_arts_pe_english_indigenous_lessons import _lesson as applied_lesson
    from scripts.grade_three_music_orientation_technology_lessons import _lesson as music_lesson
    from scripts.grade_three_science_history_lessons import _lesson as inquiry_lesson
    from scripts.grade_four_remaining_lessons import build_transversal_integration as base_integration
    from scripts.grade_seven_next_five_lessons import _natural_voice


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
TARGET_SLUGS = {"ciencias-naturales", "historia-geografia-ciencias-sociales", "artes-visuales", "musica"}


def _d(topic: str, anchor: str, misconception: str) -> dict:
    return {"topic": topic, "anchor": anchor, "misconception": misconception}


DETAILS = {
    # Ciencias Naturales
    "CN08 OA 01": _d("Evolución histórica de los modelos celulares", "línea de tiempo con dibujos atribuidos de Hooke, Leeuwenhoek, Schleiden, Schwann y Virchow, junto con evidencias y límites instrumentales", "presentar el modelo celular actual como una idea descubierta de una vez y no como explicación revisada con nueva evidencia"),
    "CN08 OA 02": _d("Estructura, función y diversidad celular", "modelos desmontables de célula procarionte, animal y vegetal, más fichas de células intestinales, musculares, nerviosas y pancreáticas", "tratar todas las células como bolsas idénticas o asignar a cada estructura una función aislada del sistema"),
    "CN08 OA 03": _d("Difusión y osmosis en células", "bolsas de diálisis o modelos seguros, soluciones de distinta concentración, balanza y diagramas de partículas antes y después", "afirmar que las partículas se mueven porque desean equilibrarse o confundir osmosis con cualquier difusión"),
    "CN08 OA 04": _d("Transporte, intercambio gaseoso y respuesta en plantas", "tallos seguros en agua coloreada, esquemas de estomas y vasos conductores, y casos de respuesta vegetal a luz o gravedad", "suponer que las plantas no responden al ambiente o que transportan sustancias igual que el sistema circulatorio humano"),
    "CN08 OA 05": _d("Interacción de sistemas para el equilibrio corporal", "caso ficticio de una comida y actividad física seguido mediante diagramas digestivo, circulatorio, respiratorio y excretor", "explicar cada sistema por separado o presentar salud y enfermedad como resultado de una sola conducta individual"),
    "CN08 OA 06": _d("Nutrientes, alimentos y salud", "muestras o fichas de alimentos ficticios, pruebas escolares seguras registradas y etiquetas simuladas de carbohidratos, proteínas, grasas, vitaminas, minerales y agua", "clasificar alimentos como buenos o malos o confundir presencia de un nutriente con efecto automático sobre la salud"),
    "CN08 OA 07": _d("Evidencia y decisiones para una vida saludable", "perfiles ficticios con rutinas, acceso desigual a alimentos, descanso, movimiento y exposición a sustancias, acompañados de fuentes sanitarias", "reducir la salud a voluntad, peso o apariencia y proponer planes únicos sin considerar contexto, acceso ni apoyo profesional"),
    "CN08 OA 08": _d("Electricidad estática e interacciones eléctricas", "globos, cintas, papeles livianos y electroscopio escolar, con estaciones de fricción, contacto e inducción sin conexión a la red", "creer que cargar un objeto significa agregar siempre electricidad o experimentar con enchufes y fuentes domiciliarias"),
    "CN08 OA 09": _d("Tecnologías de generación eléctrica", "diagramas funcionales de pila, panel fotovoltaico, generador eólico, hidroeléctrico y nuclear, con datos de conversión, continuidad e impacto", "afirmar que una fuente genera energía desde la nada o que renovable equivale a ausencia total de impactos"),
    "CN08 OA 10": _d("Circuitos eléctricos en serie y paralelo", "pilas de bajo voltaje, ampolletas o LED protegidos, resistencias, interruptores y multímetro escolar; nunca se interviene la instalación domiciliaria", "confundir corriente con voltaje o trasladar experiencias de bajo voltaje a circuitos de la red eléctrica"),
    "CN08 OA 11": _d("Calor, temperatura y transferencia térmica", "vasos aislados, agua templada y fría, termómetros, materiales conductores y aislantes, y diagramas de partículas", "tratar calor y temperatura como sinónimos o imaginar que el frío fluye como una sustancia"),
    "CN08 OA 12": _d("Evolución de los modelos atómicos", "tarjetas de evidencia y modelos de Dalton, Thomson, Rutherford y Bohr, incluido el experimento de dispersión representado con datos", "ordenar modelos como dibujos cada vez más bonitos sin relacionar sus cambios con evidencia y problemas explicativos"),
    "CN08 OA 13": _d("Átomos, partículas y formación de sustancias", "modelos de partículas con protones, neutrones y electrones, tarjetas de átomos, moléculas e iones y representaciones a escalas declaradas", "creer que átomos y moléculas son visibles en el modelo o que toda sustancia está formada por moléculas discretas"),
    "CN08 OA 14": _d("Tabla periódica, patrones y predicciones", "tabla periódica ampliada, tarjetas de elementos con número y masa atómica, conductividad, brillo y tipos de enlace", "leer la tabla como lista alfabética o pensar que masa atómica y número atómico representan lo mismo"),
    "CN08 OA 15": _d("Elementos químicos frecuentes y soporte de la vida", "datos de abundancia de elementos en corteza, atmósfera y seres vivos, modelos CHON y fuentes científicas atribuidas", "concluir que un elemento abundante es siempre indispensable o que su presencia explica por sí sola la vida"),

    # Historia, Geografía y Ciencias Sociales
    "HI08 OA 01": _d("Humanismo y Renacimiento", "dossier atribuido de textos humanistas, obras, planos y objetos de talleres italianos y europeos de los siglos XV y XVI", "reducir el Renacimiento a un despertar súbito de Europa o presentar al ser humano moderno como ruptura total con la Edad Media"),
    "HI08 OA 02": _d("De la sociedad medieval a la moderna", "cronología comparada, mapas religiosos y políticos, imprenta, textos científicos y registros urbanos de los siglos XV al XVII", "describir el cambio de época como reemplazo inmediato y uniforme, sin continuidades ni ritmos regionales"),
    "HI08 OA 03": _d("Formación y rasgos del Estado moderno", "mapas de centralización, registros fiscales, ejércitos, burocracias y fuentes de monarquías europeas con contexto", "confundir Estado moderno con democracia actual o atribuir la centralización únicamente a decisiones personales del rey"),
    "HI08 OA 04": _d("Mercantilismo y expansión económica europea", "series de precios, mapas de rutas, registros de metales y textos mercantilistas de los siglos XVI y XVII", "tratar el mercantilismo como una receta única o explicar la revolución de precios mediante una sola causa"),
    "HI08 OA 05": _d("Encuentro y enfrentamiento entre culturas en América", "mapas, crónicas contrastadas, testimonios indígenas traducidos y estudios actuales sobre territorios y cosmovisiones", "narrar la llegada europea como encuentro neutral o presentar a los pueblos americanos como un bloque homogéneo"),
    "HI08 OA 06": _d("Conquista y caída de imperios americanos", "cronologías, mapas de alianzas, datos demográficos y fuentes indígenas y europeas sobre México y los Andes", "atribuir la conquista solo a superioridad militar europea e invisibilizar alianzas, epidemias, conflictos y agencia indígena"),
    "HI08 OA 07": _d("Impactos americanos y debates en Europa", "mapas del mundo conocido, representaciones tempranas de América y fragmentos traducidos de debates morales del siglo XVI", "suponer que Europa recibió una imagen única de América o que los debates eliminaron la violencia colonial"),
    "HI08 OA 08": _d("Ciudad y administración del Imperio español", "planos urbanos, rutas comerciales, instituciones coloniales y actas de cabildo con procedencia", "creer que la ciudad colonial funcionaba aislada del territorio o que todas las decisiones provenían directamente de la metrópoli"),
    "HI08 OA 09": _d("Barroco y cultura colonial", "dossier de arquitectura, pintura, música, teatro y ceremonias coloniales con autoría, función, circulación y contexto", "definir barroco solo por exceso decorativo o borrar apropiaciones, mezclas y desigualdades coloniales"),
    "HI08 OA 10": _d("Comercio atlántico y mercados americanos", "mapas de rutas, registros de puertos, materias primas, precios y trata esclavista entre los siglos XVII y XVIII", "representar el Atlántico como intercambio voluntario entre iguales o separar comercio de coerción y esclavitud"),
    "HI08 OA 11": _d("Formación de la sociedad colonial americana", "padrones, pinturas de castas contextualizadas, normas laborales, fuentes sobre evangelización, género, mestizaje y transculturación", "usar categorías coloniales como identidades naturales o describir mestizaje sin poder, coerción ni resistencia"),
    "HI08 OA 12": _d("Guerra de Arauco y sociedad de frontera", "mapas, parlamentos, crónicas contrastadas y estudios actuales sobre relaciones hispano-mapuches", "reducir la frontera a guerra permanente o presentar a españoles, mestizos y mapuches como grupos sin diversidad interna"),
    "HI08 OA 13": _d("Hacienda y sociedad rural colonial en Chile", "planos de hacienda, contratos, registros productivos y testimonios sobre inquilinaje y elite terrateniente", "tratar la hacienda solo como unidad productiva o proyectar sus rasgos sin demostrar continuidades y cambios"),
    "HI08 OA 14": _d("Ilustración, razón y crítica al absolutismo", "fragmentos traducidos de autores ilustrados, esquemas de poderes y fuentes sobre libertad, igualdad, soberanía y secularización", "presentar la Ilustración como pensamiento único, plenamente igualitario y aplicado de inmediato"),
    "HI08 OA 15": _d("Ideas ilustradas y revoluciones atlánticas", "declaraciones, cronologías y mapas de Estados Unidos, Francia e independencias hispanoamericanas con voces y exclusiones contrastadas", "tratar las revoluciones como copias de un mismo modelo o confundir ideales declarados con derechos efectivamente ejercidos"),
    "HI08 OA 16": _d("Independencias hispanoamericanas y de Chile", "mapa continental, cronologías paralelas, fuentes de juntas, campañas, actores populares y proyectos republicanos", "reducir la Independencia de Chile a una fecha, un héroe o un proceso aislado del continente"),
    "HI08 OA 17": _d("Legitimidad de la conquista y derechos humanos", "fuentes contrapuestas del debate del siglo XVI, contexto jurídico-teológico y marco actual de derechos humanos", "equiparar conceptos del siglo XVI con derechos humanos actuales sin explicar continuidades, rupturas y límites"),
    "HI08 OA 18": _d("Derechos del hombre, ciudadanía y vigencia actual", "Declaración de 1789, otros textos de derechos, casos ficticios actuales y una matriz de inclusión y exclusión", "suponer que declarar derechos garantiza su cumplimiento o ignorar quiénes quedaron fuera de la ciudadanía histórica"),
    "HI08 OA 19": _d("Transformaciones y desafíos de la Independencia de Chile", "constituciones tempranas, debates de ciudadanía, mapas administrativos y datos sobre continuidad social y económica", "confundir independencia con igualdad inmediata o considerar estable el nuevo orden republicano desde su inicio"),
    "HI08 OA 20": _d("Regiones: criterios físicos y humanos", "mapas temáticos de Chile y América con clima, relieve, producción, lengua, historia y divisiones político-administrativas", "creer que una región es solo una división administrativa o que tiene límites naturales únicos e indiscutibles"),
    "HI08 OA 21": _d("Conectividad, migración y desigualdades regionales", "mapas de transporte y conectividad, datos demográficos ficticios y casos regionales sobre salud, empleo y relaciones campo-ciudad", "explicar aislamiento o migración como elección individual sin examinar redes, servicios, oportunidades y escalas"),
    "HI08 OA 22": _d("Desarrollo regional y sustentabilidad", "indicadores de desarrollo humano, matrices productivas, comercio, consumo y casos regionales con impactos ambientales y sociales", "equiparar desarrollo con crecimiento económico o usar un promedio regional para ocultar desigualdades internas"),

    # Artes Visuales
    "AR08 OA 01": _d("Personas, naturaleza y medioambiente en la creación visual", "referentes atribuidos de arte, diseño y prácticas visuales que examinan relaciones ambientales en Chile y otros contextos", "copiar símbolos ambientales o suponer que una obra representa por sí sola la relación de toda una comunidad con la naturaleza"),
    "AR08 OA 02": _d("Impresión, papel y textil con materiales sustentables", "mesa de pruebas con matrices simples, tintas escolares, papeles recuperados, fibras y textiles limpios, junto con ficha de origen y descarte", "llamar sustentable a cualquier material reutilizado o anteponer la técnica a la intención visual y la seguridad"),
    "AR08 OA 03": _d("Instalación como medio de expresión contemporáneo", "registros atribuidos de instalaciones, maqueta de espacio y materiales seguros para explorar recorrido, escala, luz, sonido y participación", "creer que una instalación es acumular objetos o que el público puede tocar y registrar todo sin consentimiento"),
    "AR08 OA 04": _d("Análisis de manifestaciones patrimoniales y contemporáneas", "dossier de obras con autoría, comunidad, fecha, contexto, materialidad, lenguaje visual y propósito expresivo", "convertir gusto en análisis, adivinar intenciones o tratar patrimonio vivo como material anónimo disponible"),
    "AR08 OA 05": _d("Evaluación y revisión de trabajos visuales", "producciones ficticias y propias en proceso, declaraciones de intención y pauta de materialidad, lenguaje visual y propósito", "evaluar por talento o parecido, imponer la solución del observador o confundir crítica con descalificación"),
    "AR08 OA 06": _d("Espacios de difusión y aporte comunitario de las artes", "planos y registros autorizados de museo, galería, centro cultural, espacio público y exposición digital, con perfiles de públicos y accesibilidad", "reducir difusión a decoración o asumir que todos los espacios y públicos requieren el mismo montaje y mediación"),

    # Música
    "MU08 OA 01": _d("Escucha y respuesta multimodal a músicas diversas", "registros musicales autorizados de Chile y el mundo con autoría, intérprete, fecha, contexto y opciones de respuesta verbal, visual, sonora o corporal", "presentar una sensación como significado universal de la obra o responder sin evidencia audible"),
    "MU08 OA 02": _d("Lenguaje musical, composición y propósito expresivo", "mapas de escucha, partituras convencionales o gráficas y fragmentos autorizados con contrastes de ritmo, melodía, textura, forma y dinámica", "nombrar elementos sin ubicar dónde se oyen ni explicar su relación con el propósito expresivo"),
    "MU08 OA 03": _d("Interpretación expresiva de repertorio relacionado con la escucha", "repertorio autorizado y apropiado a tesitura y recursos, pistas lentas, mapas de fraseo y roles vocales o instrumentales equivalentes", "confundir expresividad con volumen o velocidad y exigir una única forma corporal o sonora de participar"),
    "MU08 OA 04": _d("Interpretación a una y más voces con registro", "partituras o guías gráficas, grabación local sin cuentas, metrónomo y repertorio a una y más voces con volumen seguro", "usar la grabación para exhibir o comparar personas en vez de escuchar, ajustar y documentar decisiones musicales"),
    "MU08 OA 05": _d("Improvisación, acompañamiento y variación musical", "células rítmicas, melódicas y armónicas, instrumentos disponibles o aplicación sin cuenta y límites claros para improvisar y variar", "confundir improvisar con tocar sin escuchar, estructura ni responsabilidad hacia el conjunto"),
    "MU08 OA 06": _d("Fortalezas y áreas de crecimiento musical", "dos registros de ensayo propios o ficticios y pauta de autoescucha sobre ritmo, melodía, textura, fraseo, dinámica y colaboración", "convertir la reflexión en juicio de talento o personalidad en vez de usar evidencia y elegir una estrategia practicable"),
    "MU08 OA 07": _d("Música, sociedad y diversidad sociocultural", "repertorio atribuido, testimonios públicos y fichas de circulación, función y contexto de músicas de Chile y el mundo", "usar una música como representación total de una cultura o jerarquizar contextos según gusto o familiaridad"),
}


PRIOR = {
    "CN": "modelar sistemas, planificar indagaciones y argumentar con evidencia trabajados en 7° básico",
    "HI": "contextualizar fuentes, construir explicaciones multicausales y contrastar perspectivas trabajados en 7° básico",
    "AR": "crear, interpretar y revisar producciones visuales con intención, contexto y autoría trabajados en 7° básico",
    "MU": "escuchar, interpretar, crear y revisar música mediante criterios audibles trabajados en 7° básico",
}

VOCABULARY = {
    "CN": "pregunta, variable, medición, evidencia, patrón, sistema, modelo, mecanismo, conclusión, validez, limitación",
    "HI": "fuente, contexto, temporalidad, territorio, actor, multicausalidad, continuidad, cambio, perspectiva, argumento",
    "AR": "intención, lenguaje visual, materialidad, contexto, referente, instalación, montaje, audiencia, autoría, revisión",
    "MU": "pulso, ritmo, melodía, armonía, timbre, textura, dinámica, forma, fraseo, interpretación, variación",
}

STAGES = {
    "CN": (
        "Formular una pregunta investigable", "Examinar evidencia y representaciones", "Construir o contrastar un modelo",
        "Investigar relaciones entre variables", "Explicar patrones y mecanismos", "Evaluar límites, seguridad e implicancias",
        "Comunicar una explicación fundamentada",
    ),
    "HI": (
        "Situar tiempo, espacio y problema", "Contextualizar y seleccionar fuentes", "Relacionar cambio, continuidad y territorio",
        "Contrastar actores, causas y perspectivas", "Construir un argumento con evidencia", "Evaluar proyecciones y límites",
        "Comunicar una explicación histórica, geográfica o ciudadana",
    ),
    "AR": (
        "Observar referentes sin copiar", "Investigar contexto, material y propósito", "Explorar procedimientos y decisiones visuales",
        "Crear una respuesta visual propia", "Contrastar intención y efecto", "Revisar desde criterios sin perder autoría",
        "Montar, mediar y comunicar para una audiencia",
    ),
    "MU": (
        "Escuchar y registrar antes de nombrar", "Localizar rasgos audibles", "Relacionar lenguaje musical y propósito",
        "Interpretar o crear con criterio", "Ensayar, registrar y ajustar", "Reflexionar desde evidencia audible",
        "Compartir y situar la experiencia musical",
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
    if record["course_order"] != 8 or record["subject_slug"] not in TARGET_SLUGS:
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

missing_profiles = sorted(set(RECORDS) - set(DETAILS))
extra_profiles = sorted(set(DETAILS) - set(RECORDS))
if missing_profiles or extra_profiles:
    raise RuntimeError(f"Perfiles de 8° desalineados: faltan={missing_profiles}; sobran={extra_profiles}")


def _profile(code: str) -> dict:
    prefix = code[:2]
    detail = DETAILS[code]
    needed = RECORDS[code]["count"]
    focuses = [f"{stage}: {detail['topic'].lower()}" for stage in STAGES[prefix][:needed]]
    return {
        "topic": detail["topic"],
        "prior": PRIOR[prefix],
        "vocabulary": VOCABULARY[prefix],
        "anchor": detail["anchor"],
        "misconception": detail["misconception"],
        "focuses": focuses,
    }


def _retarget_links(lesson: dict, prefix: str) -> None:
    old = {"CN": "CN03", "HI": "HI03", "AR": "AR03", "MU": "MU03"}[prefix]
    new = f"{prefix}08"
    for link in lesson.get("transversal", []):
        link["code"] = link["code"].replace(old, new)


def _music_voice(lesson: dict, profile: dict, index: int) -> None:
    focus = profile["focuses"][index]
    anchor = profile["anchor"]
    lesson["purpose"] = f"Desarrollar {focus.lower()} mediante escucha, interpretación o creación situada y segura."
    lesson["goal"] = f"Hoy voy a {focus.lower()}; justificaré una decisión con evidencia audible."
    lesson["opening"] = f"Escuchan o producen una vez {anchor}. Cada estudiante registra un rasgo audible mediante gesto, símbolo o palabra antes de nombrar categorías."
    lesson["model"] = f"Modela {focus.lower()} con dos versiones breves. Localiza el instante donde cambia ritmo, melodía, textura, forma o dinámica y contrasta la idea «{profile['misconception']}»."
    lesson["guided"] = f"En grupos pequeños alternan interpretar, escuchar y ajustar una versión de {anchor}. Cada integrante aporta una decisión y recibe retroalimentación sobre un criterio audible, a volumen seguro."
    lesson["independent"] = f"Cada estudiante construye una respuesta, interpretación o creación nueva para {focus.lower()}, conserva un criterio musical y documenta un ajuste desde la escucha."
    lesson["ticket"] = "Interpreta, representa o localiza un rasgo musical y explica qué evidencia audible sostiene tu decisión."


def build_sequence(code: str) -> dict | None:
    if code not in RECORDS:
        return None
    prefix = code[:2]
    profile = _profile(code)
    lessons = []
    for index in range(len(profile["focuses"])):
        if prefix in {"CN", "HI"}:
            lesson = inquiry_lesson(code, index, profile, "science" if prefix == "CN" else "history")
            _natural_voice(lesson, profile, index, prefix)
        elif prefix == "AR":
            lesson = applied_lesson(code, index, profile)
            _natural_voice(lesson, profile, index, prefix)
        else:
            lesson = music_lesson(code, index, profile)
            _music_voice(lesson, profile, index)
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
    result = base_integration(item)
    result["generated_for"] = "8-basico-science-history-arts-music"
    return result


SEQUENCES = {code: True for code in RECORDS}

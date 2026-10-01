"""Specific second-year secondary Mathematics and Language sequences."""

from __future__ import annotations

import json
from pathlib import Path

try:
    from grade_four_math_lessons import _lesson as math_lesson
    from grade_three_math_language_lessons import _lesson as language_lesson, build_transversal_integration as transversal_integration
    from grade_seven_core_lessons import _classroom_voice, _retarget_links
    from grade_one_middle_core_lessons import MATH_STAGES, LANGUAGE_STAGES
except ImportError:
    from scripts.grade_four_math_lessons import _lesson as math_lesson
    from scripts.grade_three_math_language_lessons import _lesson as language_lesson, build_transversal_integration as transversal_integration
    from scripts.grade_seven_core_lessons import _classroom_voice, _retarget_links
    from scripts.grade_one_middle_core_lessons import MATH_STAGES, LANGUAGE_STAGES


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
CATALOG = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
TARGET_SLUGS = {"matematica", "lengua-literatura"}


MATH_SPECS = {
    "MA2M OA 01": ("Operaciones, estimación y descomposición de raíces", "tarjetas de raíces equivalentes, cuadrados perfectos, recta numérica y problemas de longitud, área y escala con datos plausibles", "operar símbolos de raíz sin estimar, descomponer ni comprobar el resultado por aproximación"),
    "MA2M OA 02": ("Potencias, raíces enésimas y logaritmos", "tablas que conectan base, exponente, potencia, raíz y logaritmo; recta numérica y situaciones de crecimiento por factores", "tratar logaritmo como una tecla aislada o confundir el exponente racional con el índice de la raíz"),
    "MA2M OA 03": ("Función cuadrática y sus representaciones", "tablas, gráficos y expresiones de trayectorias, áreas y oferta o demanda ficticia con vértice, eje de simetría, ceros e intersección", "suponer que toda curva es parábola o leer puntos especiales sin relacionarlos con coeficientes y contexto"),
    "MA2M OA 04": ("Ecuaciones cuadráticas en formas resolubles", "baldosas algebraicas, áreas, productos nulos y ecuaciones de las formas oficiales con soluciones racionales verificables", "aplicar una fórmula única sin reconocer estructura, restricciones ni comprobar cada solución"),
    "MA2M OA 05": ("Función inversa como proceso y reflexión", "máquinas reversibles, tablas de entrada y salida, gráficos reflejados en y=x y casos lineales o cuadráticos con dominio declarado", "intercambiar x e y mecánicamente sin revisar dominio, recorrido ni si la relación inversa es función"),
    "MA2M OA 06": ("Cambio porcentual constante e interés compuesto", "líneas de tiempo, factores multiplicativos, tablas recursivas y escenarios ficticios de ahorro, depreciación o población sin recomendar productos financieros", "sumar el mismo porcentaje inicial en cada periodo o confundir variación porcentual con puntos porcentuales"),
    "MA2M OA 07": ("Área superficial y volumen de la esfera", "círculos máximos, cilindros y semiesferas desmontables o simuladas, mediciones y comparación de fórmulas dimensionalmente coherentes", "usar fórmulas como recetas, confundir superficie con volumen o perder unidades cuadradas y cúbicas"),
    "MA2M OA 08": ("Seno, coseno y tangente en triángulos rectángulos", "familias de triángulos semejantes, tablas de razones, clinómetro escolar y diagramas con ángulo de referencia explícito", "memorizar catetos opuesto y adyacente sin fijar el ángulo o usar razones fuera de un triángulo rectángulo"),
    "MA2M OA 09": ("Trigonometría, vectores y proyecciones", "vectores en cuadrícula, fuerzas o desplazamientos ficticios y triángulos rectángulos para componer, descomponer y proyectar", "confundir magnitud con componente o sumar longitudes sin atender dirección, signo y ángulo"),
    "MA2M OA 10": ("Variables aleatorias finitas y distribuciones", "experimentos con monedas, dados o urnas, tabla valor-probabilidad y gráficos de distribuciones con probabilidades que suman uno", "confundir resultado elemental con valor de la variable o asignar probabilidades sin reunir eventos equivalentes"),
    "MA2M OA 11": ("Permutaciones, combinatoria y probabilidad", "tarjetas de rutas, códigos, comités y ordenamientos ficticios; diagramas de árbol y conteo sistemático antes de usar notación", "usar permutaciones cuando el orden no importa o multiplicar elecciones que no son sucesivas e independientes"),
    "MA2M OA 12": ("Probabilidad, medios y decisiones sociales", "titulares y afirmaciones ficticias con riesgo absoluto, riesgo relativo, frecuencia natural, incertidumbre y dos conclusiones opuestas", "convertir probabilidad en certeza, omitir la base de comparación o aceptar una decisión porque incluye un porcentaje"),
}


LANGUAGE_SPECS = {
    "LE2M OA 01": ("Trayectoria lectora autónoma y sostenida", "catálogo diverso con muestras atribuidas, propósitos lectores, criterios de selección y bitácora que permite abandonar justificadamente una elección", "confundir autonomía con leer sin propósito, conversación, seguimiento ni derecho a revisar la selección"),
    "LE2M OA 02": ("Literatura, herencias culturales y experiencia humana", "fragmentos autorizados o de dominio público de épocas y procedencias distintas, con preguntas sobre dilemas, memoria, poder y pertenencia", "reducir la obra a moraleja, tratar una herencia cultural como uniforme o exigir confesiones personales"),
    "LE2M OA 03": ("Narraciones, personajes tipo y arquitectura temporal", "relato original con conflictos, motivaciones, narrador, indicios, flashback, caja china, historia paralela, símbolos e intertextos", "resumir acontecimientos sin explicar cómo narrador, estructura y contexto orientan la interpretación"),
    "LE2M OA 04": ("Poesía, soneto, símbolos y voz", "poemas de dominio público u originales, incluido un soneto, con repeticiones, lenguaje figurado, símbolos, actitud del hablante e intertextos", "enumerar figuras o contar versos sin relacionar forma, fragmento, totalidad y efecto"),
    "LE2M OA 05": ("Drama, atmósfera y puesta en escena", "escena original o de dominio público, acotaciones y dos montajes que varían iluminación, sonido, actuación, vestuario y escenografía", "confundir texto y representación o atribuir la atmósfera a un solo recurso sin evidencia escénica"),
    "LE2M OA 06": ("Siglo de Oro, obra y contexto", "fragmentos de dominio público con autoría, género, fecha, glosario acotado y fuentes sobre honra, poder, apariencia y sociedad", "usar el contexto como lista decorativa o presentar el Siglo de Oro como una voz única y ajena a tensiones"),
    "LE2M OA 07": ("Cuento latinoamericano moderno y contemporáneo", "cuentos o fragmentos autorizados de autorías y territorios diversos, con procedencia, contexto, voces y decisiones narrativas contrastables", "convertir Latinoamérica en una identidad homogénea o explicar el cuento solo mediante biografía y contexto"),
    "LE2M OA 08": ("Interpretación literaria histórica, social y universal", "dos pasajes decisivos, una hipótesis revisable, citas y fuentes contextuales que permiten distinguir texto, inferencia y antecedente cultural", "presentar gusto u opinión como hipótesis o acumular contexto sin explicar la evidencia literaria"),
    "LE2M OA 09": ("Argumentación, modalizadores y fallas de razonamiento", "columna, carta, discurso y ensayo didácticos con tesis explícita o implícita, evidencias, modalizadores, léxico valorativo y falacias observables", "rechazar un argumento por desacuerdo o aceptar emoción y certeza verbal como sustitutos de evidencia"),
    "LE2M OA 10": ("Medios, persuasión y recursos multimodales", "noticia, reportaje, propaganda y crónica ficticios sobre un mismo hecho, con fuentes, omisiones, diseño, imágenes, audio y estrategias de persuasión", "atribuir intenciones sin señales verificables o creer que una imagen y un dato vuelven neutral el mensaje"),
    "LE2M OA 11": ("Textos no literarios para contextualizar lecturas", "obra breve y fuentes históricas, biográficas o críticas con autoría, fecha, propósito, alcance y contradicciones explícitas", "reemplazar la lectura de la obra por datos externos o seleccionar contexto que no modifica ninguna interpretación"),
    "LE2M OA 12": ("Escritura creativa y flexible en nuevos géneros", "modelos breves de géneros diversos, fichas de propósito y audiencia y restricciones que exigen decisiones propias", "imitar rasgos superficiales del modelo o corregir forma antes de construir una situación comunicativa"),
    "LE2M OA 13": ("Escritura explicativa con progresión y fuentes", "miniarchivo atribuido, artículo, informe y reportaje modelo; organizadores para tema, subtemas, recursos anafóricos, citas e infografías", "pegar información fuente por fuente sin construir progresión temática ni explicar citas y recursos gráficos"),
    "LE2M OA 14": ("Ensayo persuasivo, evidencia y contraargumento", "afirmaciones literarias o contingentes debatibles, dossier contrastado, mapa de razones, objeciones y formatos de referencia acordados", "acumular opiniones, caricaturizar la objeción o insertar una cita sin razonar cómo sostiene la hipótesis"),
    "LE2M OA 15": ("Planificación, revisión y edición situada", "borrador original con decisiones revisables de registro, persona, estructura, cohesión, concordancia, conectores, vocabulario y presentación", "revisar solo ortografía o reemplazar la voz del autor en vez de priorizar propósito, audiencia y coherencia"),
    "LE2M OA 16": ("Estilo directo e indirecto en ámbitos académicos", "diálogo, testimonio ficticio y reporte académico que obligan a ajustar tiempos, pronombres, deícticos, atribución y grado de distancia", "cambiar comillas por que sin transformar referencias, temporalidad, atribución y significado"),
    "LE2M OA 17": ("Frases nominales complejas y correferencia", "pares de textos expositivos y argumentativos que expanden o compactan información mediante núcleos, modificadores y cadenas referenciales", "suponer que compactar siempre mejora el texto o acumular modificadores hasta volver ambiguo el núcleo"),
    "LE2M OA 18": ("Ortografía y puntuación al servicio de la comprensión", "texto original con decisiones de ortografía literal, acentual y puntuación que cambian voces, incisos, enumeraciones y relaciones lógicas", "corregir por apariencia o colocar puntuación según pausas orales sin revisar estructura y sentido"),
    "LE2M OA 19": ("Comprensión crítica de discursos audiovisuales", "exposición, discurso, documental y noticia originales con guion, fuentes, edición, imágenes, sonido, estereotipos y puntos de vista", "evaluar solo fluidez o producción visual sin reconstruir argumentos, contexto y relaciones multimodales"),
    "LE2M OA 20": ("Punto de vista, razonamiento y retórica oral", "dos versiones de una intervención ficticia con diferente organización, vocabulario, progresión argumental y recursos retóricos", "juzgar al emisor o su seguridad en vez de evaluar razonamiento, recursos y efectos observables"),
    "LE2M OA 21": ("Diálogo constructivo, parafraseo y negociación", "controversia ficticia no sensible, posiciones provisionales, evidencias compartidas y protocolo de parafraseo, refutación y acuerdos parciales", "esperar turno sin comprender, repetir postura o forzar acuerdo eliminando diferencias relevantes"),
    "LE2M OA 22": ("Exposición investigada y graduación de información", "dossier breve, ficha de audiencia, secuencia temática y apoyos visuales que deben jerarquizar y explicar conceptos complejos", "leer diapositivas, saturar de datos o confundir vocabulario técnico con dominio comunicativo"),
    "LE2M OA 23": ("Efectos lingüísticos, paralingüísticos y no lingüísticos", "tres registros de un mismo mensaje que cambian léxico, sintaxis, volumen, ritmo, pausas, gesto, distancia, encuadre y soporte", "atribuir el efecto a la personalidad del hablante sin comparar recursos ni situación"),
    "LE2M OA 24": ("Investigación sobre lenguaje y literatura", "miniarchivo con catálogo, artículo académico didáctico, entrevista ficticia y sitio sin autor para evaluar cobertura, validez, confiabilidad y suficiencia", "coleccionar enlaces o citas sin delimitar pregunta, jerarquizar hallazgos ni comunicar una respuesta propia"),
}


SPECS = MATH_SPECS | LANGUAGE_SPECS
CLASS_COUNTS = {code: sum(item["oa_code"] == code for item in CATALOG["classes"]) for code in SPECS}
RECORDS = {}
for record in SNAPSHOT["records"]:
    if record["course_order"] != 10 or record["subject_slug"] not in TARGET_SLUGS:
        continue
    for objective in record["objectives"]:
        if objective["code"].startswith("de "):
            continue
        RECORDS[objective["code"]] = {
            "slug": record["subject_slug"], "axis": objective["axis"], "description": objective["description"],
            "url": objective["url"], "count": CLASS_COUNTS[objective["code"]],
        }

if set(RECORDS) != set(SPECS):
    raise RuntimeError(f"Perfiles de 2° medio desalineados: faltan={sorted(set(RECORDS)-set(SPECS))}; sobran={sorted(set(SPECS)-set(RECORDS))}")


def _profile(code: str) -> dict:
    record = RECORDS[code]
    topic, anchor, misconception = SPECS[code]
    is_math = record["slug"] == "matematica"
    stages = (MATH_STAGES if is_math else LANGUAGE_STAGES)[record["axis"]]
    prior = (
        "números racionales y potencias, relaciones lineales, semejanza, vectores, datos bivariados y probabilidad desarrollados en 1° medio"
        if is_math else
        "lectura literaria y crítica, argumentación, escritura por procesos, oralidad e investigación desarrolladas en 1° medio"
    )
    vocabulary = (
        f"representación, dominio, condición, propiedad, estrategia, comprobación, límite; lenguaje específico de {topic.lower()}"
        if is_math else
        f"propósito, audiencia, evidencia, voz, recurso, contexto, fuente, revisión; lenguaje específico de {topic.lower()}"
    )
    return {
        "topic": topic, "prior": prior, "vocabulary": vocabulary, "anchor": anchor, "misconception": misconception,
        "focuses": [f"{stage}: {topic}" for stage in stages[:record['count']]],
    }


def build_sequence(code: str) -> dict | None:
    if code not in RECORDS:
        return None
    profile = _profile(code)
    is_math = RECORDS[code]["slug"] == "matematica"
    lessons = []
    for index in range(len(profile["focuses"])):
        if is_math:
            lesson = math_lesson(code, index, profile)
            _retarget_links(lesson, "MA04", "MA2M")
        else:
            lesson = language_lesson(code, index, profile, "language")
            _retarget_links(lesson, "LE03", "LE2M")
        _classroom_voice(lesson, profile, index, is_math)
        lessons.append(lesson)
    record = RECORDS[code]
    subject = "Matemática" if is_math else "Lengua y Literatura"
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": (
            f"{profile['topic']} recupera {profile['prior']} y aumenta formalización, autonomía y evaluación crítica. "
            f"Cada clase cambia el problema, texto, representación o audiencia y enfrenta la confusión «{profile['misconception']}»."
        ),
        "prerequisites": profile["prior"], "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"{subject} · progresión interna en {len(lessons)} clases"],
            "unit_origin": "Organización pedagógica interna derivada del eje y del OA; no se presenta como una unidad oficial del programa.",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del OA oficial.",
            "source": record["url"],
        },
        "lessons": lessons,
    }


def build_transversal_integration(item: dict) -> dict:
    result = transversal_integration(item)
    result["generated_for"] = "2-medio-matematica-lengua"
    return result


SEQUENCES = {code: True for code in RECORDS}

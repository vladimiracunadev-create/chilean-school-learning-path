"""Specific first-year secondary Mathematics and Language sequences."""

from __future__ import annotations

import json
from pathlib import Path

try:
    from grade_four_math_lessons import _lesson as math_lesson
    from grade_three_math_language_lessons import (
        _lesson as language_lesson,
        build_transversal_integration as transversal_integration,
    )
    from grade_seven_core_lessons import _classroom_voice, _retarget_links
except ImportError:
    from scripts.grade_four_math_lessons import _lesson as math_lesson
    from scripts.grade_three_math_language_lessons import (
        _lesson as language_lesson,
        build_transversal_integration as transversal_integration,
    )
    from scripts.grade_seven_core_lessons import _classroom_voice, _retarget_links


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
TARGET_SLUGS = {"matematica", "lengua-literatura"}


MATH_SPECS = {
    "MA1M OA 01": ("Operaciones con números racionales", "rectas numéricas, mosaicos de fracciones y expresiones que combinan signos, paréntesis y distintas notaciones", "aplicar reglas de signos sin estimar ni comprobar la equivalencia entre fracción y decimal"),
    "MA1M OA 02": ("Potencias de base racional y exponente entero", "tarjetas de potencias positivas, cero y negativas, tablas de crecimiento y decrecimiento y recta numérica", "invertir la base sin justificar el exponente negativo o sumar exponentes fuera de un producto"),
    "MA1M OA 03": ("Productos notables y completación de cuadrados", "baldosas algebraicas y rectángulos de lados variables para transformar productos en sumas y viceversa", "memorizar identidades sin reconocer el área, los términos ni las condiciones de equivalencia"),
    "MA1M OA 04": ("Sistemas de ecuaciones lineales 2×2", "dos planes ficticios, tablas, rectas en el plano y tarjetas para sustitución, igualación y eliminación", "resolver dos ecuaciones por separado o aceptar una intersección sin volver al problema"),
    "MA1M OA 05": ("Relaciones lineales en dos variables", "familias de rectas, líneas de nivel, planos inclinados y tablas de pares que satisfacen ax + by = c", "tratar la ecuación como función de una sola variable sin interpretar sus múltiples soluciones"),
    "MA1M OA 06": ("Sectores y segmentos circulares", "círculos fraccionables, ángulos centrales de 60°, 90°, 120° y 180°, hilo y papel cuadriculado", "usar la fracción angular sólo en el área o confundir arco, cuerda, sector y segmento"),
    "MA1M OA 07": ("Área y volumen del cono", "redes de conos, sectores circulares, cilindros y conos de igual base y altura para comparar capacidades", "usar la altura inclinada en el volumen o calcular superficie sin incluir la base pertinente"),
    "MA1M OA 08": ("Homotecia y razón de escala", "figuras en cuadrícula, centros de homotecia, proyecciones, cámara oscura y mediciones de segmentos correspondientes", "sumar la razón a las longitudes o perder el centro y la orientación de la transformación"),
    "MA1M OA 09": ("Teorema de Tales desde la homotecia", "triángulos atravesados por paralelas, ampliaciones desde un centro y mediciones contrastables", "aplicar proporciones sin verificar paralelismo ni correspondencia entre segmentos"),
    "MA1M OA 10": ("Semejanza, proporcionalidad y modelos a escala", "planos, mapas y modelos ficticios con escalas gráficas y numéricas", "comparar sólo la forma visual o aplicar la escala lineal directamente a áreas y volúmenes"),
    "MA1M OA 11": ("Homotecia vectorial", "vectores desde un centro, productos por escalares positivos y negativos y construcciones manuales o digitales", "multiplicar sólo una componente o ignorar la orientación cuando el escalar es negativo"),
    "MA1M OA 12": ("Distribuciones bivariadas y nubes de puntos", "datos ficticios de dos características, tablas de doble entrada y planos para construir nubes de puntos", "unir los puntos como serie temporal o afirmar causalidad sólo porque aparece asociación"),
    "MA1M OA 13": ("Comparación de poblaciones con gráficos xy", "dos nubes de puntos con color, rectas de separación y datos ficticios con dispersión y casos fronterizos", "clasificar por una línea arbitraria sin explicar errores, solapamientos ni límites"),
    "MA1M OA 14": ("Reglas aditiva y multiplicativa de probabilidad", "tablas de contingencia, árboles, cartas y ruletas para eventos excluyentes, independientes y dependientes", "sumar probabilidades en cualquier unión o multiplicarlas sin revisar dependencia y espacio muestral"),
    "MA1M OA 15": ("Azar, tabla de Galton y paseos aleatorios", "tablero de Galton simulado, monedas, recorridos en cuadrícula y registros acumulados por bloques", "interpretar una racha como destino, esperar simetría exacta en pocos ensayos o confundir modelo y realidad"),
}


LANGUAGE_SPECS = {
    "LE1M OA 01": ("Trayectoria lectora autónoma", "catálogo diverso con muestras, fichas de procedencia, propósitos lectores y bitácora flexible", "confundir autonomía con leer sin propósito, acompañamiento ni revisión de la elección"),
    "LE1M OA 02": ("Literatura y dimensiones de la experiencia humana", "obras y fragmentos autorizados que abordan dilemas, poder, justicia, pertenencia y transformación", "reducir una obra a moraleja o exigir experiencias autobiográficas para demostrar comprensión"),
    "LE1M OA 03": ("Análisis de narraciones", "relato original con conflicto, personajes dinámicos, símbolos, prejuicios, anacronías e intertexto", "resumir la trama sin analizar evolución, narrador, símbolos ni relación entre fragmento y totalidad"),
    "LE1M OA 04": ("Análisis de poemas", "poemas originales o de dominio público con símbolos, imágenes, repeticiones y sonoridades contrastadas", "enumerar recursos sin explicar su efecto o identificar al hablante con el autor"),
    "LE1M OA 05": ("Análisis de textos dramáticos y puesta en escena", "escena original, acotaciones y dos propuestas de montaje con decisiones escénicas diferentes", "confundir texto dramático y representación o juzgar personajes sin atender acciones y diálogos"),
    "LE1M OA 06": ("Tragedia, conflicto humano y contexto", "fragmentos trágicos de dominio público o autorizados, árbol del conflicto y ficha histórica verificable", "llamar tragedia a cualquier desenlace triste o juzgar acciones sin considerar convenciones y contexto"),
    "LE1M OA 07": ("Romanticismo y visión de mundo", "poemas y fragmentos narrativos con procedencia, contexto y rasgos románticos que puedan contrastarse", "convertir una lista de rasgos en interpretación o tratar el movimiento como uniforme y aislado"),
    "LE1M OA 08": ("Interpretación literaria situada", "dos pasajes, un dilema, una ficha contextual y evidencias que admiten interpretaciones revisables", "presentar una preferencia como interpretación o usar contexto sin volver al texto"),
    "LE1M OA 09": ("Evaluación de textos argumentativos", "columna, carta, discurso y ensayo didácticos con tesis, evidencias y recursos de persuasión contrastables", "aceptar una tesis por el tono o contar ejemplos sin evaluar pertinencia, suficiencia y razonamiento"),
    "LE1M OA 10": ("Lectura crítica de medios", "noticia, reportaje, propaganda y crónica ficticios sobre un mismo asunto, con imágenes y datos", "atribuir intenciones sin señales textuales o comparar sólo titulares sin revisar fuentes"),
    "LE1M OA 11": ("Textos no literarios para contextualizar obras", "obra breve y fuentes informativas con autoría, fecha, propósito y alcances distintos", "usar el contexto para reemplazar la lectura literaria o incorporar datos que no explican el pasaje"),
    "LE1M OA 12": ("Escritura flexible en nuevos géneros", "modelos breves de géneros distintos, fichas de audiencia y restricciones que permiten decisiones de autor", "copiar la forma superficial del modelo o corregir antes de desarrollar propósito y contenido"),
    "LE1M OA 13": ("Escritura explicativa", "miniarchivo de fuentes, artículo e informe modelo, organizadores y recursos gráficos pertinentes", "pegar información por fuente sin construir progresión ni referencias claras"),
    "LE1M OA 14": ("Escritura persuasiva y ensayo", "afirmaciones debatibles, evidencias contrastadas, mapa de razones y contraargumentos para audiencias reales", "acumular opiniones, ocultar objeciones o usar citas sin explicar cómo apoyan la hipótesis"),
    "LE1M OA 15": ("Proceso de escritura, revisión y edición", "borrador original con problemas de registro, organización, cohesión, citas, sintaxis y puntuación", "revisar sólo ortografía o reemplazar la voz del autor en vez de retroalimentar decisiones"),
    "LE1M OA 16": ("Estilo directo e indirecto", "testimonios ficticios, diálogos y reportes que obligan a ajustar tiempos, pronombres y deícticos", "cambiar comillas por que sin modificar tiempos, referentes ni punto de vista"),
    "LE1M OA 17": ("Correferencia con metáfora y metonimia", "párrafos con cadenas léxicas, metáforas y metonimias que cambian claridad, tono y perspectiva", "sustituir palabras sólo para evitar repetición aunque se vuelva ambiguo el referente"),
    "LE1M OA 18": ("Ortografía y puntuación para facilitar comprensión", "texto original con problemas de ortografía literal, acentual y puntuación que afectan voces y relaciones", "corregir por apariencia o usar comas donde se percibe cualquier pausa"),
    "LE1M OA 19": ("Comprensión y evaluación de textos orales y audiovisuales", "exposición, discurso y cápsula audiovisual originales con guion, fuentes, montaje y puntos de vista", "evaluar sólo fluidez e imagen sin reconstruir ideas, evidencias y recursos multimodales"),
    "LE1M OA 20": ("Resumen y evaluación de un discurso argumentativo", "audio docente original, transcripción segmentada y mapa de tesis, razones, evidencia y supuestos", "copiar frases sucesivas o evaluar antes de reconstruir fielmente el razonamiento"),
    "LE1M OA 21": ("Diálogo constructivo para debatir y explorar", "controversia ficticia no sensible, posiciones provisionales, evidencias y protocolo de escucha", "esperar turno sin escuchar, repetir postura o buscar acuerdo borrando diferencias"),
    "LE1M OA 22": ("Exposición investigada para una audiencia", "dossier breve, ficha de audiencia y apoyos visuales que deben explicar y no decorar", "leer diapositivas o confundir abundancia de datos con una progresión comprensible"),
    "LE1M OA 23": ("Efectos de recursos lingüísticos y paralingüísticos", "tres versiones audiovisuales de un mismo mensaje que varían léxico, volumen, ritmo, gesto y encuadre", "atribuir efectos a la personalidad del hablante sin comparar recursos observables"),
    "LE1M OA 24": ("Investigación sobre lenguaje y literatura", "miniarchivo con catálogo, artículo, entrevista ficticia y sitio sin autor para evaluar y organizar", "coleccionar enlaces sin responder una pregunta o descartar fuentes sólo porque contradicen una idea"),
}


MATH_STAGES = {
    "Números": ("Representar y estimar", "Construir la relación", "Formalizar propiedades", "Resolver con estrategia", "Comprobar y transferir"),
    "Álgebra y funciones": ("Reconocer variables y restricciones", "Representar la relación", "Construir el procedimiento", "Comparar estrategias", "Modelar y comprobar"),
    "Geometría": ("Explorar una construcción", "Medir y formular una conjetura", "Justificar la relación", "Resolver un caso nuevo", "Comprobar y transferir"),
    "Probabilidad y estadística": ("Organizar datos o resultados", "Representar patrones", "Construir una regla o comparación", "Evaluar una afirmación", "Comunicar límites y transferir"),
}

LANGUAGE_STAGES = {
    "Lectura - Comprensión": ("Entrar al texto con propósito", "Localizar evidencias decisivas", "Analizar recursos y relaciones", "Contrastar interpretaciones", "Situar texto y contexto", "Formular una lectura propia", "Revisar y transferir"),
    "Escritura - Producción": ("Reconocer género, propósito y audiencia", "Investigar y seleccionar insumos", "Planificar decisiones", "Escribir un primer desarrollo", "Revisar con evidencia de lectura", "Editar, publicar y justificar"),
    "Comunicación oral": ("Escuchar o preparar con propósito", "Reconstruir ideas y recursos", "Modelar una decisión comunicativa", "Ensayar con retroalimentación", "Comunicar ante una audiencia", "Responder y ajustar", "Evaluar el efecto"),
    "Investigación": ("Delimitar pregunta y alcance", "Diseñar una búsqueda", "Evaluar fuentes", "Organizar hallazgos", "Construir una respuesta", "Comunicar resultados y límites"),
}

RECORDS = {}
CATALOG = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
CLASS_COUNTS = {
    code: sum(item["oa_code"] == code for item in CATALOG["classes"])
    for code in MATH_SPECS | LANGUAGE_SPECS
}
for record in SNAPSHOT["records"]:
    if record["course_order"] != 9 or record["subject_slug"] not in TARGET_SLUGS:
        continue
    for objective in record["objectives"]:
        if objective["code"].startswith("de "):
            continue
        RECORDS[objective["code"]] = {
            "slug": record["subject_slug"],
            "axis": objective["axis"],
            "description": objective["description"],
            "url": objective["url"],
            "count": CLASS_COUNTS[objective["code"]],
        }

SPECS = MATH_SPECS | LANGUAGE_SPECS
if set(RECORDS) != set(SPECS):
    raise RuntimeError(f"Perfiles de 1° medio desalineados: faltan={sorted(set(RECORDS)-set(SPECS))}; sobran={sorted(set(SPECS)-set(RECORDS))}")


def _profile(code: str) -> dict:
    record = RECORDS[code]
    topic, anchor, misconception = SPECS[code]
    is_math = record["slug"] == "matematica"
    stages = (MATH_STAGES if is_math else LANGUAGE_STAGES)[record["axis"]]
    prior = (
        "números racionales, álgebra, geometría, probabilidad y evaluación de datos desarrollados en 8° básico"
        if is_math else
        "lectura crítica, interpretación, escritura, oralidad e investigación desarrolladas en 8° básico"
    )
    vocabulary = (
        f"representación, condición, propiedad, estrategia, comprobación, límite; lenguaje específico de {topic.lower()}"
        if is_math else
        f"propósito, audiencia, evidencia, recurso, contexto, revisión; lenguaje específico de {topic.lower()}"
    )
    return {
        "topic": topic,
        "prior": prior,
        "vocabulary": vocabulary,
        "anchor": anchor,
        "misconception": misconception,
        "focuses": [f"{stage}: {topic}" for stage in stages[:record["count"]]],
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
            _retarget_links(lesson, "MA04", "MA1M")
        else:
            lesson = language_lesson(code, index, profile, "language")
            _retarget_links(lesson, "LE03", "LE1M")
        _classroom_voice(lesson, profile, index, is_math)
        lessons.append(lesson)
    subject = "Matemática" if is_math else "Lengua y Literatura"
    record = RECORDS[code]
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": (
            f"{profile['topic']} recupera {profile['prior']} y aumenta formalización, autonomía y transferencia. "
            f"Cada clase cambia el problema, texto, representación o audiencia y enfrenta la confusión «{profile['misconception']}»."
        ),
        "prerequisites": profile["prior"],
        "vocabulary": profile["vocabulary"],
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
    result["generated_for"] = "1-medio-matematica-lengua"
    return result


SEQUENCES = {code: True for code in RECORDS}

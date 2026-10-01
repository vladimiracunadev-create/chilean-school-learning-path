"""Specific third-year secondary Mathematics and Language sequences."""

from __future__ import annotations

import json
from pathlib import Path

try:
    from grade_four_math_lessons import _lesson as math_lesson
    from grade_three_math_language_lessons import _lesson as language_lesson
    from grade_seven_core_lessons import _classroom_voice
except ImportError:
    from scripts.grade_four_math_lessons import _lesson as math_lesson
    from scripts.grade_three_math_language_lessons import _lesson as language_lesson
    from scripts.grade_seven_core_lessons import _classroom_voice


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
CATALOG = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
TARGET_SLUGS = {"matematica-3o-medio", "lengua-literatura-3o-medio"}


SPECS = {
    "FG-MATE-3M-OAC-01": {
        "topic": "Números complejos y operaciones en el plano",
        "anchor": "puntos, vectores y trayectorias en el plano complejo; tarjetas con a+bi, conjugados y operaciones que se pueden verificar gráfica y simbólicamente",
        "misconception": "operar la parte real con la imaginaria como si fueran términos semejantes o usar i²=1",
        "focuses": [
            "Representar números complejos de forma pictórica y simbólica",
            "Sumar y restar complejos conectando vectores y expresiones",
            "Multiplicar complejos y usar i²=-1 para simplificar",
            "Dividir mediante el conjugado y comprobar el resultado",
        ],
    },
    "FG-MATE-3M-OAC-02": {
        "topic": "Incerteza, dispersión y probabilidad condicional",
        "anchor": "dos conjuntos de datos ficticios con igual promedio y distinta dispersión, tablas de contingencia y árboles de probabilidad sobre decisiones escolares sin datos personales",
        "misconception": "decidir solo con el promedio o confundir P(A|B) con P(B|A) y con la intersección",
        "focuses": [
            "Comparar distribuciones mediante rango, varianza y desviación estándar",
            "Interpretar medidas de dispersión junto con centro, forma y contexto",
            "Calcular probabilidades condicionales con tablas y árboles",
            "Tomar una decisión bajo incerteza declarando supuestos y límites",
        ],
    },
    "FG-MATE-3M-OAC-03": {
        "topic": "Modelos exponenciales y logarítmicos",
        "anchor": "tablas, gráficos y expresiones de crecimiento o decrecimiento en datos simulados de población, temperatura, intensidad o difusión digital con fuente y escala declaradas",
        "misconception": "tratar cualquier variación como exponencial, extrapolar sin límites o usar el logaritmo como tecla sin interpretar base y dominio",
        "focuses": [
            "Distinguir crecimiento lineal y exponencial mediante razones de cambio",
            "Construir y ajustar modelos exponenciales con parámetros interpretables",
            "Relacionar función exponencial y logarítmica como procesos inversos",
            "Contrastar un modelo con información digital y evaluar la fuente",
            "Comunicar predicciones, supuestos, dominio y límites del modelo",
        ],
    },
    "FG-MATE-3M-OAC-04": {
        "topic": "Relaciones métricas en la circunferencia",
        "anchor": "circunferencias construidas con regla, compás o geometría dinámica; ángulos centrales e inscritos, arcos, cuerdas, tangentes y secantes con medidas controlables",
        "misconception": "aplicar una relación por la apariencia del dibujo sin identificar puntos, arcos, intersecciones ni condiciones geométricas",
        "focuses": [
            "Conjeturar relaciones entre ángulos centrales, inscritos y arcos",
            "Justificar relaciones entre cuerdas, secantes y tangentes",
            "Resolver problemas métricos mediante teoremas pertinentes",
            "Validar construcciones y argumentos con una herramienta tecnológica",
        ],
    },
    "FG-LELI-3M-OAC-01": {
        "topic": "Interpretación literaria, recursos e intertextualidad",
        "anchor": "un corpus breve, atribuido y legalmente utilizable que combina una narración, un poema o una escena con otro referente cultural o artístico",
        "misconception": "enumerar recursos o semejanzas sin explicar cómo contribuyen a una interpretación del sentido de la obra",
        "focuses": [
            "Formular una hipótesis interpretativa revisable",
            "Analizar narrador, personajes, tópicos y lenguaje como recursos de sentido",
            "Relacionar forma, pasaje y totalidad de la obra",
            "Reconstruir una relación intertextual con evidencia de ambos referentes",
            "Contrastar interpretaciones plausibles y reconocer sus límites",
            "Comunicar una interpretación fundada con citas acotadas y atribución",
        ],
    },
    "FG-LELI-3M-OAC-02": {
        "topic": "Efecto estético, experiencia lectora y técnicas literarias",
        "anchor": "dos textos literarios breves o fragmentos autorizados que abordan un dilema humano mediante técnicas y atmósferas contrastantes",
        "misconception": "reducir el efecto estético a gusto personal o exigir experiencias íntimas para justificar una lectura",
        "focuses": [
            "Describir un efecto estético mediante huellas precisas del texto",
            "Relacionar experiencia lectora y problemática humana sin imponer confesiones",
            "Analizar cómo una técnica literaria produce o modifica el efecto",
            "Comparar efectos construidos por recursos diferentes",
            "Evaluar una primera respuesta estética a la luz de nueva evidencia",
            "Escribir una reflexión crítica que distingue experiencia, texto e interpretación",
        ],
    },
    "FG-LELI-3M-OAC-03": {
        "topic": "Análisis crítico de géneros discursivos no literarios",
        "anchor": "un dossier atribuido con noticia, columna, discurso oral y pieza audiovisual sobre un asunto público no sensible, acompañado por datos verificables",
        "misconception": "juzgar un texto por acuerdo personal, fluidez o apariencia sin reconstruir contexto, género, razonamiento y calidad de la información",
        "focuses": [
            "Reconocer género, propósito, enunciador, audiencia y contexto",
            "Reconstruir relaciones entre afirmaciones, razones y evidencias",
            "Examinar selección, omisión y jerarquización de información",
            "Verificar datos y distinguir fuente primaria, secundaria y opinión",
            "Comparar cómo dos géneros construyen autoridad y cercanía",
            "Evaluar la solidez de un razonamiento y sus supuestos",
            "Producir un análisis crítico con evidencia textual y documental",
        ],
    },
    "FG-LELI-3M-OAC-04": {
        "topic": "Comunidades digitales, argumentación y ética de la participación",
        "anchor": "capturas didácticas ficticias de publicaciones, memes, comentarios y videos, con contexto, cronología, fuentes y datos personales eliminados",
        "misconception": "tratar todo contenido viral como equivalente, atribuir intenciones sin evidencia o normalizar acoso y discriminación como desacuerdo",
        "focuses": [
            "Caracterizar una comunidad digital mediante prácticas y contexto",
            "Analizar posicionamiento, rol y relación con la audiencia",
            "Reconstruir razonamientos y evaluar la evidencia compartida",
            "Rastrear origen, circulación y transformación de una afirmación",
            "Distinguir crítica, descalificación, acoso y discriminación",
            "Deliberar sobre consecuencias y respuestas seguras sin amplificar daño",
            "Diseñar una participación digital ética, fundada y protegida",
        ],
    },
    "FG-LELI-3M-OAC-05": {
        "topic": "Recursos lingüísticos y multimodales en la comprensión",
        "anchor": "tres versiones de un mismo mensaje que cambian léxico, deícticos, verbos, sintaxis, puntuación, imagen, sonido, gesto y encuadre",
        "misconception": "analizar cada recurso por separado o atribuir sus efectos a la personalidad del emisor sin comparar el discurso",
        "focuses": [
            "Localizar recursos lingüísticos y no lingüísticos relevantes",
            "Explicar cómo el léxico y la gramática posicionan al enunciador",
            "Analizar roles y actitudes construidos ante la audiencia",
            "Relacionar imagen, sonido, gesto y palabra en una unidad de sentido",
            "Comparar el efecto de cambiar un recurso conservando el contenido",
            "Evaluar coherencia, tensiones y silencios entre modos",
            "Comunicar un análisis multimodal con evidencia precisa",
        ],
    },
    "FG-LELI-3M-OAC-06": {
        "topic": "Producción coherente y cohesionada según género y audiencia",
        "anchor": "una situación comunicativa auténtica y segura con propósito, audiencia y opciones de género oral, escrito o audiovisual, más modelos atribuidos y una pauta de proceso",
        "misconception": "elegir un formato por comodidad, escribir de una vez o corregir solo superficie sin revisar sentido, estructura y audiencia",
        "focuses": [
            "Definir propósito, tema, audiencia y género discursivo",
            "Investigar y organizar contenido pertinente antes de producir",
            "Planificar progresión, voces y recursos del texto",
            "Elaborar una versión completa coherente y cohesionada",
            "Adecuar convenciones, registro y recursos a la audiencia",
            "Revisar con evidencia de lector, oyente o espectador",
            "Editar, publicar y explicar decisiones de autoría",
        ],
    },
    "FG-LELI-3M-OAC-07": {
        "topic": "Recursos lingüísticos y multimodales en la producción",
        "anchor": "un mensaje base que debe adaptarse para distintas audiencias mediante decisiones de léxico, deícticos, verbos, sintaxis, puntuación, imagen, sonido y gesto",
        "misconception": "agregar recursos decorativos o intensificar el mensaje sin revisar posicionamiento, roles, accesibilidad y efecto global",
        "focuses": [
            "Definir el posicionamiento y la relación ética con la audiencia",
            "Seleccionar léxico, deícticos y verbos coherentes con el propósito",
            "Usar sintaxis y puntuación para orientar énfasis y relaciones",
            "Diseñar recursos visuales y sonoros funcionales y accesibles",
            "Ajustar gesto, voz, encuadre y ritmo a la situación",
            "Probar la combinación de modos con una audiencia segura",
            "Revisar el producto y justificar los efectos buscados y no buscados",
        ],
    },
    "FG-LELI-3M-OAC-08": {
        "topic": "Diálogo argumentativo para construir y ampliar ideas",
        "anchor": "una interpretación literaria o análisis crítico con tres posiciones provisionales, un conjunto común de evidencias y un protocolo de diálogo protegido",
        "misconception": "esperar turno para repetir la postura, atacar a la persona o forzar consenso sin examinar premisas y evidencia",
        "focuses": [
            "Explicar criterios, razonamiento y conclusión de una postura provisional",
            "Usar evidencia pertinente y suficiente para fundamentar",
            "Parafrasear una posición ajena antes de evaluarla",
            "Examinar premisas, relaciones, elecciones de palabras y énfasis",
            "Ampliar o refutar incorporando aportes de pares",
            "Cerrar con acuerdos, desacuerdos razonados y nuevas preguntas",
        ],
    },
    "FG-LELI-3M-OAC-09": {
        "topic": "Investigación ética sobre lenguaje y literatura",
        "anchor": "una pregunta acotada y un miniarchivo de catálogo, libro, artículo académico didáctico, entrevista, repositorio y sitio sin autoría clara",
        "misconception": "coleccionar enlaces o citas, elegir por posición en el buscador o presentar una síntesis sin trazabilidad ni voz propia",
        "focuses": [
            "Delimitar una pregunta investigable y criterios de suficiencia",
            "Diseñar búsquedas y seleccionar fuentes variadas",
            "Evaluar validez, confiabilidad, autoría, fecha y alcance",
            "Procesar información mediante notas, categorías y relaciones",
            "Citar y referenciar sin plagio ni pérdida de contexto",
            "Comunicar hallazgos, límites y nuevas preguntas en un género educativo",
        ],
    },
}


CLASS_COUNTS = {code: sum(item["oa_code"] == code for item in CATALOG["classes"]) for code in SPECS}
RECORDS: dict[str, dict] = {}
for record in SNAPSHOT["records"]:
    if record["course_order"] != 11 or record["subject_slug"] not in TARGET_SLUGS:
        continue
    for objective in record["objectives"]:
        if objective["code"] not in SPECS:
            continue
        RECORDS[objective["code"]] = {
            "slug": record["subject_slug"],
            "axis": objective["axis"],
            "description": objective["description"],
            "url": objective["url"],
            "count": CLASS_COUNTS[objective["code"]],
        }

if set(RECORDS) != set(SPECS):
    raise RuntimeError(
        f"Perfiles de 3° medio desalineados: faltan={sorted(set(RECORDS)-set(SPECS))}; "
        f"sobran={sorted(set(SPECS)-set(RECORDS))}"
    )
for code, profile in SPECS.items():
    if len(profile["focuses"]) != RECORDS[code]["count"]:
        raise RuntimeError(
            f"{code}: {len(profile['focuses'])} focos para {RECORDS[code]['count']} clases catalogadas"
        )


def _profile(code: str) -> dict:
    record = RECORDS[code]
    spec = SPECS[code]
    is_math = record["slug"] == "matematica-3o-medio"
    prior = (
        "operaciones, funciones, trigonometría, geometría, conteo y probabilidad desarrollados hasta 2° medio"
        if is_math
        else "interpretación literaria, análisis crítico, producción, diálogo e investigación desarrollados hasta 2° medio"
    )
    vocabulary = (
        f"representación, propiedad, condición, modelo, argumento, comprobación, límite; lenguaje específico de {spec['topic'].lower()}"
        if is_math
        else f"propósito, audiencia, evidencia, posicionamiento, recurso, contexto, fuente, revisión; lenguaje específico de {spec['topic'].lower()}"
    )
    return spec | {"prior": prior, "vocabulary": vocabulary}


def build_sequence(code: str) -> dict | None:
    if code not in RECORDS:
        return None
    profile = _profile(code)
    is_math = RECORDS[code]["slug"] == "matematica-3o-medio"
    lessons = []
    for index in range(len(profile["focuses"])):
        if is_math:
            lesson = math_lesson("MA04 OA 01", index, profile)
        else:
            lesson = language_lesson("LE03 OA 01", index, profile, "language")
        _classroom_voice(lesson, profile, index, is_math)
        # Formación General de 3° medio no registra OAH/OAA separados para estas
        # asignaturas en el snapshot. Las habilidades quedan observadas dentro del
        # desempeño, sin inventar códigos transversales inexistentes.
        lesson["transversal"] = []
        lessons.append(lesson)
    record = RECORDS[code]
    subject = "Matemática" if is_math else "Lengua y Literatura"
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": (
            f"{profile['topic']} recupera {profile['prior']} y aumenta autonomía, formalización y juicio crítico. "
            f"La progresión deriva del verbo y alcance del OA oficial, cambia problema, texto, representación o audiencia "
            f"en cada clase y enfrenta explícitamente la confusión «{profile['misconception']}»."
        ),
        "prerequisites": profile["prior"],
        "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"{subject} · progresión pedagógica interna en {len(lessons)} clases"],
            "unit_origin": "Organización pedagógica interna derivada del OA; no se presenta como una unidad oficial del programa.",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios observables internos derivados del verbo, contenido y alcance del OA oficial; requieren revisión profesional humana.",
            "source": record["url"],
        },
        "lessons": lessons,
    }


SEQUENCES = {code: True for code in RECORDS}

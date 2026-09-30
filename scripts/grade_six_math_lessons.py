"""Specific sixth-grade Mathematics sequences and transversal integrations."""
from __future__ import annotations

try:
    from grade_four_math_lessons import _lesson, build_transversal_integration as _integration
except ImportError:
    from scripts.grade_four_math_lessons import _lesson, build_transversal_integration as _integration


COUNTS = [4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5]

THEMES = {
    1: ("Factores, múltiplos y números primos", "tableros del 1 al 100, arreglos rectangulares y problemas de ciclos que vuelven a coincidir", "confundir factor con múltiplo o decidir que un número es primo sin examinar todos sus divisores posibles"),
    2: ("Operaciones combinadas con números naturales", "presupuestos, repartos y recorridos ficticios expresados con más de una operación y paréntesis", "resolver sólo por palabras clave o alterar el orden de las operaciones sin conservar el sentido del problema"),
    3: ("Razones entre cantidades", "mezclas, equipos y escalas simples comparadas mediante material, tablas y notación a:b", "tratar una razón como resta o comparar cantidades sin mantener el orden ni la relación entre ellas"),
    4: ("Porcentajes como razón de cien", "cuadrículas de cien, descuentos ficticios y resultados de encuestas sin datos personales", "usar el símbolo % como adorno o calcular sobre una cantidad distinta del total de referencia"),
    5: ("Fracciones impropias y números mixtos", "tiras, recipientes y rectas numéricas que representan cantidades mayores que una unidad", "cambiar el entero de referencia o concatenar la parte entera con numerador y denominador"),
    6: ("Adición y sustracción de fracciones y números mixtos", "recetas y trayectos ficticios con denominadores menores o iguales a doce", "sumar denominadores, amplificar sólo el numerador o operar las partes enteras sin atender el canje"),
    7: ("Multiplicación y división de decimales", "medidas y precios ficticios operados por números naturales de uno o dos dígitos", "mover la coma por costumbre sin estimar la magnitud ni interpretar el valor posicional"),
    8: ("Problemas con fracciones y decimales", "situaciones de medida y presupuesto donde se elige entre fracción, decimal o ambas representaciones", "operar todos los datos antes de identificar la pregunta, la unidad y la representación conveniente"),
    9: ("Relaciones en tablas", "tablas de entrada y salida sobre costos, distancias y figuras crecientes con reglas contrastadas", "describir diferencias sueltas sin comprobar una relación que funcione para todos los pares"),
    10: ("Generalizaciones con expresiones algebraicas", "patrones numéricos y geométricos traducidos a expresiones con letras", "tratar la letra como etiqueta o hallar varios casos sin expresar la regla general"),
    11: ("Ecuaciones de primer grado", "balanzas, segmentos y problemas modelados con una incógnita y operaciones inversas", "tratar el signo igual como orden de calcular o cambiar un término de lado sin preservar la igualdad"),
    12: ("Construcción y clasificación de triángulos", "varillas, regla, compás y transportador para comparar lados, ángulos y posibilidades de construcción", "clasificar sólo por apariencia o suponer que cualquier trío de longitudes forma un triángulo"),
    13: ("Área en cubos y paralelepípedos", "redes, cajas y cubos encajables para reconocer cada cara y calcular su área", "contar caras sin considerar sus dimensiones o confundir superficie con volumen"),
    14: ("Teselaciones mediante transformaciones", "mosaicos de papel y cuadrícula construidos con traslaciones, reflexiones y rotaciones", "dejar huecos o traslapes y llamar teselado a cualquier repetición decorativa"),
    15: ("Construcción y clasificación de ángulos", "semirrectas y transportadores para ángulos agudos, rectos, obtusos, extendidos y completos", "elegir la escala incorrecta del transportador o clasificar por la longitud de los lados"),
    16: ("Ángulos entre rectas que se cortan", "pares de ángulos opuestos por el vértice y adyacentes construidos y medidos", "suponer que todos los ángulos del cruce son iguales o confundir adyacencia con oposición"),
    17: ("Suma de ángulos interiores", "triángulos y cuadriláteros recortables, plegables y representados simbólicamente", "memorizar 180° o 360° sin justificar la descomposición ni reconocer la figura"),
    18: ("Superficie de cubos y paralelepípedos", "redes y envases ficticios con dimensiones en centímetros y metros", "usar una sola cara, sumar aristas o informar el resultado sin unidad cuadrada"),
    19: ("Volumen de cubos y paralelepípedos", "prismas de cubos unitarios organizados por capas, filas y columnas", "contar sólo cubos visibles o usar unidades cuadradas para una medida tridimensional"),
    20: ("Estimación y medición de ángulos", "ángulos de objetos y dibujos estimados antes de usar el transportador", "leer la escala que no comienza en la semirrecta o aceptar una medida incompatible con la estimación"),
    21: ("Ángulos en paralelas y triángulos", "rectas paralelas cortadas por una transversal y triángulos con medidas faltantes", "aplicar una relación angular por apariencia sin justificar paralelismo, posición o suma interior"),
    22: ("Comparación de distribuciones muestrales", "diagramas de puntos y de tallo y hojas de dos muestras aleatorias ficticias", "comparar sólo máximos o promedios sin examinar centro, dispersión, forma y tamaño de muestra"),
    23: ("Tendencia en experimentos aleatorios", "series crecientes de lanzamientos de monedas, dados y ruletas equilibradas", "creer que una racha obliga el siguiente resultado o que pocas repeticiones revelan una probabilidad estable"),
    24: ("Gráficos de barra doble y circulares", "dos conjuntos de datos ficticios representados con escalas, porcentajes y sectores", "leer alturas o sectores sin revisar título, escala, total y correspondencia entre categorías"),
}

STAGES = [
    "Representar y precisar el concepto",
    "Conectar representaciones y lenguaje matemático",
    "Elegir, ejecutar y justificar una estrategia",
    "Resolver un caso con una condición nueva",
    "Comprobar, comparar y comunicar",
]


def _profile(number: int) -> dict:
    topic, anchor, misconception = THEMES[number]
    count = COUNTS[number - 1]
    return {
        "topic": topic,
        "prior": "representar, resolver y comprobar con números, álgebra, geometría, medición y datos de 5° básico",
        "vocabulary": "representación, relación, estrategia, estimación, equivalencia, unidad, procedimiento, argumento, comprobación",
        "anchor": anchor,
        "misconception": misconception,
        "focuses": [f"{stage} · {topic}" for stage in STAGES[:count]],
    }


def _grade_six_links(lesson: dict) -> dict:
    for link in lesson.get("transversal", []):
        link["code"] = link["code"].replace("MA04", "MA06")
    return lesson


def build_sequence(code: str) -> dict | None:
    if not code.startswith("MA06 OA "):
        return None
    number = int(code.rsplit(" ", 1)[-1])
    if number not in THEMES:
        return None
    profile = _profile(number)
    lessons = [_grade_six_links(_lesson(code, index, profile)) for index in range(len(profile["focuses"]))]
    for index, lesson in enumerate(lessons):
        focus = profile["focuses"][index].lower()
        lesson["guided"] += f" Antes del segundo intento, la retroalimentación vuelve al criterio propio de «{focus}»."
        lesson["independent"] += f" La evidencia se juzga por el logro de «{focus}», no por copiar el ejemplo."
        lesson["ticket"] += f" La respuesta debe permitir comprobar «{focus}»."
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": f"{profile['topic']} progresa desde los aprendizajes de 5° mediante decisiones observables. Cada clase cambia la representación, el caso y la evidencia, y enfrenta explícitamente la confusión «{profile['misconception']}».",
        "prerequisites": profile["prior"],
        "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"Matemática · progresión interna en {len(lessons)} clases"],
            "unit_origin": "Organización pedagógica interna derivada del eje y del OA; no se presenta como una unidad oficial del programa.",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del OA oficial.",
            "source": f"https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/{code.lower().replace(' ', '-')}",
        },
        "lessons": lessons,
    }


def build_transversal_integration(item: dict) -> dict:
    return _integration(item)


SEQUENCES = {f"MA06 OA {number:02d}": True for number in range(1, 25)}

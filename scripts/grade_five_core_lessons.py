"""Specific fifth-grade sequences for Mathematics, Language and Science."""
from __future__ import annotations

try:
    from grade_four_math_lessons import _lesson as math_lesson, build_transversal_integration as math_integration
    from grade_four_remaining_lessons import build_transversal_integration as core_integration
    from grade_three_math_language_lessons import _lesson as language_lesson
    from grade_three_science_history_lessons import _lesson as science_lesson
except ImportError:
    from scripts.grade_four_math_lessons import _lesson as math_lesson, build_transversal_integration as math_integration
    from scripts.grade_four_remaining_lessons import build_transversal_integration as core_integration
    from scripts.grade_three_math_language_lessons import _lesson as language_lesson
    from scripts.grade_three_science_history_lessons import _lesson as science_lesson


COUNTS = {
    "MA": [5, 4, 4, 4, 4, 4, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 4, 5, 5, 4, 5, 4],
    "LE": [5, 6, 6, 7, 7, 6, 7, 5, 5, 6, 5, 5, 5, 6, 5, 5, 5, 6, 5, 5, 5, 5, 5, 6, 5, 5, 6, 6, 5, 6],
    "CN": [4, 5, 4, 4, 5, 5, 5, 5, 4, 5, 4, 4, 5, 5],
}


MATH_THEMES = {
    1: ("Números naturales hasta mil millones", "tarjetas con población, distancias y presupuestos ficticios de seis a nueve cifras", "leer cifras por separado, ignorar ceros interiores o aproximar sin indicar posición"),
    2: ("Estrategias de cálculo mental para multiplicar", "productos como 24×50, 16×25 y 125×8 resueltos de más de una forma", "anexar ceros sin reconocer el factor de diez o aplicar una propiedad fuera de contexto"),
    3: ("Multiplicación de dos dígitos por dos dígitos", "pedidos ficticios organizados en arreglos, áreas y productos parciales", "ejecutar el algoritmo sin estimar ni respetar el valor posicional"),
    4: ("División de tres dígitos por uno", "repartos y agrupamientos donde el resto cambia la decisión final", "descartar el resto o escribirlo sin interpretarlo en la situación"),
    5: ("Operaciones combinadas y uso de paréntesis", "expresiones que modelan compras, puntajes y recorridos con cuatro operaciones", "resolver estrictamente de izquierda a derecha o agregar paréntesis sin conservar significado"),
    6: ("Problemas con cuatro operaciones y dinero", "presupuestos ficticios superiores a $10.000 con calculadora usada para comprobar", "elegir operaciones por palabras clave o aceptar cualquier resultado de la calculadora"),
    7: ("Fracciones propias y equivalencia", "tiras, cuadrículas y rectas con denominadores hasta doce construidas sobre el mismo entero", "comparar sólo numeradores o denominadores y simplificar sin conservar valor"),
    8: ("Fracciones impropias y números mixtos", "recipientes y trayectos que superan una unidad representados con material y recta", "tratar la parte entera y la fracción como dígitos contiguos o cambiar el entero de referencia"),
    9: ("Adición y sustracción de fracciones propias", "recetas ficticias y recorridos combinados con denominadores menores o iguales a doce", "sumar denominadores o amplificar sólo una parte de la igualdad"),
    10: ("Equivalencia entre fracciones y decimales", "dinero didáctico, cuadrículas y medidas para medios, cuartos, quintos y décimos", "leer la coma como separador decorativo o asignar un decimal por apariencia"),
    11: ("Comparación de decimales hasta la milésima", "mediciones ficticias de 2,7; 2,07; 2,705 y 2,075 en tablas posicionales", "comparar cantidad de cifras o leer la parte decimal como número natural aislado"),
    12: ("Adición y sustracción de decimales", "distancias, masas y precios ficticios expresados hasta milésimos", "alinear los últimos dígitos en vez de valores posicionales o perder ceros de referencia"),
    13: ("Problemas con fracciones y decimales", "situaciones de medida donde primero se decide si conviene fracción, decimal o ambas", "operar antes de definir la unidad o mezclar representaciones sin justificar equivalencia"),
    14: ("Reglas de sucesiones y predicción", "secuencias numéricas y geométricas donde una regla rival coincide al inicio pero diverge después", "describir diferencias sueltas sin formular una regla que permita predecir"),
    15: ("Ecuaciones e inecuaciones de un paso", "balanzas, segmentos y situaciones expresadas como x+38=95 o x−17<40", "tratar el signo igual como orden de calcular o confundir una solución con el conjunto solución"),
    16: ("Coordenadas en el primer cuadrante", "mapa ficticio en plano cartesiano con rutas y puntos de interés", "intercambiar abscisa y ordenada o comenzar el conteo fuera del origen"),
    17: ("Paralelismo y perpendicularidad en 2D y 3D", "prismas, redes y planos donde se localizan lados, aristas y caras", "clasificar por apariencia sin prolongar líneas ni considerar la superficie que contiene las aristas"),
    18: ("Congruencia mediante transformaciones", "figuras en cuadrícula trasladadas, reflejadas y rotadas alrededor de centros marcados", "cambiar tamaño u orientación indebidamente y llamar congruentes a figuras sólo parecidas"),
    19: ("Medición de longitudes en m, cm y mm", "objetos y trayectos medibles con estimación previa e instrumentos revisados", "medir desde el borde de la regla o registrar un número sin unidad ni precisión"),
    20: ("Conversión de unidades de longitud", "rutas y diseños expresados alternativamente en km, m, cm y mm", "mover ceros mecánicamente sin atender unidad inicial, final ni razonabilidad"),
    21: ("Perímetro y área de rectángulos", "rectángulos distintos construidos bajo una restricción de área, perímetro o ambas", "suponer que igual perímetro implica igual área o buscar una única figura posible"),
    22: ("Áreas de triángulos, paralelogramos y trapecios", "figuras recortables y cuadrículas que permiten descomponer, completar y trasladar", "memorizar fórmulas sin identificar base, altura o unidad cuadrada"),
    23: ("Promedio e interpretación contextual", "conjuntos pequeños de tiempos, lecturas y cantidades ficticias con igual promedio y distinta distribución", "calcular mecánicamente sin interpretar o creer que el promedio debe ser un dato observado"),
    24: ("Posibilidad en experimentos aleatorios", "bolsas opacas, ruletas y dados equilibrados con resultados posibles identificados", "confundir posible con seguro o usar una racha breve para asegurar el siguiente resultado"),
    25: ("Comparación cualitativa de probabilidades", "eventos de dos experimentos donde se comparan casos favorables sin formalizar porcentajes", "decidir por intuición sin examinar resultados posibles o confundir más probable con seguro"),
    26: ("Tablas, barras y gráficos de línea", "datos climáticos o escolares ficticios presentados con escalas y formatos contrastados", "leer puntos o barras sin revisar ejes, escala, unidad y continuidad de los datos"),
    27: ("Diagramas de tallo y hojas", "muestras ficticias de dos cifras que deben conservar cada dato al organizarse", "usar el tallo como categoría y perder el valor posicional o duplicar datos al ordenar"),
}


LANGUAGE_THEMES = {
    1: ("Fluidez, precisión y prosodia", "fragmentos narrativos, teatrales e informativos con puntuación contrastada", "confundir fluidez con velocidad y sacrificar sentido, pausas o precisión"),
    2: ("Estrategias conscientes de comprensión", "un texto desafiante con puntos de detención para conectar, releer, preguntar y organizar", "usar todas las estrategias como lista sin decidir cuál resuelve la dificultad real"),
    3: ("Repertorio literario y valor cultural", "cuentos, poemas, mitos, novelas e historietas de procedencias y voces diversas", "convertir la lectura amplia en fichas idénticas o jerarquizar géneros por extensión"),
    4: ("Análisis profundo de narraciones", "dos relatos donde acciones, ambiente, costumbres y lenguaje figurado cambian la interpretación", "resumir la trama en vez de explicar consecuencias, rasgos y decisiones con evidencia"),
    5: ("Imágenes, figuras y forma poética", "poemas con imágenes sensoriales, comparaciones, personificaciones y rimas diferentes", "buscar figuras como etiquetas sin explicar qué imagen, ánimo o sentido producen"),
    6: ("Comprensión crítica de textos no literarios", "artículo, biografía, noticia y gráfico sobre un mismo asunto con información complementaria", "copiar datos explícitos sin relacionar recursos visuales, inferencias ni opinión fundamentada"),
    7: ("Evaluación de procedencia y suficiencia", "dos textos sobre una pregunta común con emisor, propósito, audiencia y evidencia diferentes", "rechazar una fuente por desacuerdo personal o declararla confiable sólo por su diseño"),
    8: ("Síntesis y registro de ideas principales", "texto informativo que exige notas, esquema y síntesis para estudiar o investigar", "copiar oraciones completas o eliminar relaciones decisivas al resumir"),
    9: ("Lectura habitual y elección personal", "menú diverso de textos y bitácora breve de elecciones, abandonos y hallazgos", "obligar a terminar toda elección o confundir gusto lector con facilidad"),
    10: ("Uso autónomo y responsable de biblioteca", "misiones de selección, consulta, investigación, préstamo y devolución con catálogo real o simulado", "elegir sólo por portada o usar la biblioteca sin registrar fuente, ubicación y cuidado"),
    11: ("Búsqueda y selección de información", "libros, diarios, enciclopedias y sitios previamente revisados sobre una pregunta acotada", "acumular enlaces o copiar el primer resultado sin contrastar relevancia y procedencia"),
    12: ("Significado de palabras nuevas", "palabras polisémicas encontradas en literatura y ciencias que exigen contexto, raíces y fuentes", "elegir la primera acepción del diccionario o adivinar sólo por parecido gráfico"),
    13: ("Escritura frecuente con voz propia", "cuaderno de autor con poema, diario ficticio, carta, blog y escena breve", "corregir mientras se generan ideas hasta uniformar o bloquear la voz"),
    14: ("Narraciones con trama, descripción y diálogo", "relato ficticio donde una decisión modifica personaje, ambiente y desenlace", "encadenar acciones sin causalidad o incluir diálogo que no desarrolla la trama"),
    15: ("Artículos informativos con fuentes", "artículo para lectores reales con tema delimitado, idea central por párrafo y fuentes atribuibles", "acumular datos en párrafos sin idea central o nombrar fuentes imposibles de rastrear"),
    16: ("Comentarios lectores fundamentados", "pasaje literario que admite impresiones distintas sostenidas con ejemplos", "contar nuevamente la obra o declarar gusto sin desarrollar un tema relevante"),
    17: ("Planificación según propósito y destinatario", "encargos contrastados que exigen investigar, seleccionar y ordenar ideas antes de redactar", "llenar un esquema rígido sin decidir qué necesita comprender el destinatario"),
    18: ("Revisión y edición para comunicar", "borrador con vacíos, repeticiones, registro inconsistente y problemas de cohesión", "copiar en limpio o corregir sólo ortografía sin revisar propósito e ideas"),
    19: ("Vocabulario nuevo en la escritura", "banco de palabras tomadas de lecturas con contexto, definición, matiz y ejemplos propios", "insertar vocabulario difícil como adorno aunque vuelva impreciso el texto"),
    20: ("Matices entre sinónimos", "versiones de una escena donde cambiar un verbo o adjetivo modifica intensidad, valoración y registro", "tratar sinónimos como intercambiables en todos los contextos"),
    21: ("Conjugación de verbos regulares", "relato y artículo donde cambian persona, número, tiempo y referente", "corregir por sonido sin localizar sujeto, tiempo y terminación verbal"),
    22: ("Ortografía al servicio del lector", "texto con c-s-z, diálogo, tildes diacríticas y dieréticas y comas explicativas", "aplicar reglas a palabras aisladas sin releer cómo cambia la comprensión"),
    23: ("Escucha literaria de obras completas", "lectura mediada de cuentos, poemas, mitos, leyendas y capítulos de novela", "interrumpir cada pasaje con cuestionarios hasta perder continuidad y disfrute"),
    24: ("Comprensión y contraste de textos orales", "noticia, entrevista, explicación y documental breve con notas de escucha", "retener detalles sueltos sin distinguir ideas, propósito, evidencia y opinión"),
    25: ("Apreciación de teatro y lenguaje audiovisual", "escena teatral o audiovisual con decisiones de voz, gesto, montaje y caracterización", "evaluar sólo decorado o gusto y no relacionar comportamiento, habla e historia"),
    26: ("Diálogo para desarrollar ideas y acuerdos", "discusión sobre una decisión textual o comunitaria con información compartida", "esperar turno para repetir la postura sin escuchar ni construir sobre otra idea"),
    27: ("Convenciones sociales y registro", "situaciones ficticias de presentación, consulta, desacuerdo, permiso, disculpa y reparación", "repetir fórmulas de cortesía sin ajustar tono, vínculo, medio y propósito"),
    28: ("Exposición oral clara y fundamentada", "presentación breve con introducción, desarrollo, cierre, datos y apoyo visual legible", "leer diapositivas o acumular datos sin una idea central ni ensayo para la audiencia"),
    29: ("Vocabulario nuevo en intervenciones orales", "conversación y exposición que recuperan términos de lecturas sin perder naturalidad", "usar una palabra memorizada fuera de sentido o registro para parecer más formal"),
    30: ("Producción planificada de textos orales", "poema, narración y dramatización preparados para audiencias y propósitos distintos", "improvisar sin plan o memorizar mecánicamente sin comunicar intención"),
}


SCIENCE_THEMES = {
    1: ("Células y niveles de organización", "micrografías, modelos y tarjetas de célula, tejido, órgano, sistema y organismo", "tratar células como ladrillos idénticos o invertir los niveles de organización"),
    2: ("Sistema digestivo y transformación de alimentos", "modelo de recorrido con boca, esófago, estómago, hígado e intestinos", "describir un tubo sin funciones o afirmar que toda absorción ocurre en el estómago"),
    3: ("Respiración e intercambio gaseoso", "modelo torácico, diagramas de alvéolos y datos de respiración antes y después de actividad segura", "confundir ventilación con respiración o decir que sólo entra oxígeno y sólo sale dióxido"),
    4: ("Sistema circulatorio y transporte", "circuito modelado con corazón, vasos, sangre, oxígeno, dióxido y nutrientes", "representar la sangre como inmóvil o atribuir al corazón la producción de oxígeno"),
    5: ("Alimentación variada y funciones corporales", "menús ficticios culturalmente diversos analizados por variedad, porción y frecuencia", "moralizar alimentos, prescribir dietas o asociar salud con forma corporal"),
    6: ("Efectos del humo de tabaco", "fuentes sanitarias seleccionadas y casos ficticios sobre sistemas respiratorio y circulatorio", "culpar personas, dramatizar o equiparar una opinión con evidencia sanitaria"),
    7: ("Microorganismos, salud e higiene", "casos de bacterias, virus y hongos beneficiosos o dañinos con escalas declaradas", "considerar que todo microorganismo causa enfermedad o que higiene significa esterilidad total"),
    8: ("Transformaciones de energía eléctrica", "circuitos y artefactos de baja tensión que producen luz, calor, sonido o movimiento", "afirmar que la energía desaparece o confundir fuente, dispositivo y efecto"),
    9: ("Circuitos eléctricos simples", "pilas, cables, interruptores y ampolletas de baja tensión con esquema previo", "unir componentes sin trayectoria cerrada o usar enchufes domiciliarios para experimentar"),
    10: ("Conductores, aisladores y seguridad eléctrica", "muestras seguras de cobre, aluminio, plástico, goma y madera probadas en circuito de baja tensión", "clasificar por apariencia o extrapolar una prueba escolar a instalaciones domiciliarias"),
    11: ("Uso responsable de energía eléctrica", "inventario ficticio de usos cotidianos con potencia, tiempo y necesidad comparados cualitativamente", "proponer apagar todo sin considerar seguridad, función o efecto verificable"),
    12: ("Distribución del agua en la Tierra", "modelo proporcional y datos de océanos, glaciares, aguas subterráneas, ríos, lagos y atmósfera", "suponer que agua abundante en el planeta equivale a agua dulce accesible"),
    13: ("Características de océanos y lagos", "perfiles de profundidad con temperatura, luz, presión, biodiversidad, olas, mareas y corrientes", "generalizar un dato local a todo cuerpo de agua o confundir ola, marea y corriente"),
    14: ("Actividad humana y protección de reservas hídricas", "casos chilenos documentados de contaminación, extracción, restauración y protección", "proponer campañas generales sin conectar causa, actor, evidencia, acción y seguimiento"),
}


MATH_STAGES = [
    "Representar y precisar el sentido", "Conectar dos representaciones", "Elegir y justificar una estrategia",
    "Resolver un caso con una condición nueva", "Comprobar, comparar y comunicar", "Analizar un error y revisarlo",
    "Transferir a un problema no rutinario",
]
LANGUAGE_STAGES = [
    "Reconocer propósito y desafío", "Modelar una lectura o producción", "Localizar y seleccionar evidencia",
    "Comparar interpretaciones o decisiones", "Producir una respuesta propia", "Revisar con retroalimentación",
    "Transferir a otro texto o audiencia",
]
SCIENCE_STAGES = [
    "Observar y separar evidencia de interpretación", "Formular una pregunta o predicción comprobable",
    "Construir o examinar un modelo", "Comparar resultados con un criterio común",
    "Explicar con evidencia y límites", "Aplicar una decisión segura y responsable",
]


def _profile(code: str) -> dict:
    prefix = code[:2]
    number = int(code.rsplit(" ", 1)[-1])
    topic, anchor, misconception = {"MA": MATH_THEMES, "LE": LANGUAGE_THEMES, "CN": SCIENCE_THEMES}[prefix][number]
    count = COUNTS[prefix][number - 1]
    if prefix == "MA":
        prior = "representar, calcular y argumentar con los aprendizajes de 4° básico"
        vocabulary = "representación, estrategia, estimación, equivalencia, unidad, procedimiento, comprobación"
        stages = MATH_STAGES
    elif prefix == "LE":
        prior = "leer, escribir y conversar con evidencia y propósito en 4° básico"
        vocabulary = "propósito, audiencia, evidencia, inferencia, estructura, registro, revisión"
        stages = LANGUAGE_STAGES
    else:
        prior = "observar, medir, modelar y explicar fenómenos con evidencia en 4° básico"
        vocabulary = "evidencia, variable, sistema, modelo, comparación, explicación, limitación, seguridad"
        stages = SCIENCE_STAGES
    return {
        "topic": topic,
        "prior": prior,
        "vocabulary": vocabulary,
        "anchor": anchor,
        "misconception": misconception,
        "focuses": [f"{stage} · {topic}" for stage in stages[:count]],
    }


def _fix_links(lesson: dict) -> dict:
    for link in lesson.get("transversal", []):
        link["code"] = link["code"].replace("MA04", "MA05").replace("LE03", "LE05").replace("CN03", "CN05")
    return lesson


def build_sequence(code: str) -> dict | None:
    prefix = code[:2]
    if prefix not in COUNTS or code[2:4] != "05" or " OA " not in code:
        return None
    profile = _profile(code)
    if prefix == "MA":
        lessons = [_fix_links(math_lesson(code, index, profile)) for index in range(len(profile["focuses"]))]
        slug, axis = "matematica", "Números, álgebra, geometría, medición y datos"
    elif prefix == "LE":
        lessons = [_fix_links(language_lesson(code, index, profile, "language")) for index in range(len(profile["focuses"]))]
        slug, axis = "lenguaje-comunicacion", "Lectura, escritura y comunicación oral"
    else:
        lessons = [_fix_links(science_lesson(code, index, profile, "science")) for index in range(len(profile["focuses"]))]
        slug, axis = "ciencias-naturales", "Ciencias de la vida, físicas y de la Tierra"
    for index, lesson in enumerate(lessons):
        focus = profile["focuses"][index].lower()
        lesson["guided"] += f" La retroalimentación vuelve al criterio propio de «{focus}» antes del segundo intento."
        lesson["independent"] += f" La evidencia se juzga por el logro de «{focus}», no por imitar el ejemplo."
        lesson["ticket"] += f" La respuesta final debe permitir comprobar «{focus}»."
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": f"{profile['topic']} avanza desde {profile['prior']} mediante decisiones observables. Cada clase cambia la evidencia, representación y forma de participación, y enfrenta la confusión «{profile['misconception']}».",
        "prerequisites": profile["prior"],
        "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"{axis} · progresión interna en {len(lessons)} clases"],
            "unit_origin": "Organización pedagógica interna derivada del eje y del OA; no se presenta como una unidad oficial del programa",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del OA oficial",
            "source": f"https://www.curriculumnacional.cl/curriculum/1o-6o-basico/{slug}/5-basico/{code.lower().replace(' ', '-')}",
        },
        "lessons": lessons,
    }


def build_transversal_integration(item: dict) -> dict:
    if item["subject_slug"] == "matematica":
        return math_integration(item)
    return core_integration(item)


SEQUENCES = {
    f"{prefix}05 OA {number:02d}": True
    for prefix, counts in COUNTS.items()
    for number in range(1, len(counts) + 1)
}

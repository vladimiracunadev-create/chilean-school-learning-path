"""Specific seventh-grade Mathematics and Language and Literature sequences.

The profiles in this module are the canonical pedagogical source for the two
subjects.  Generated Markdown and HTML must be rebuilt with
``generate_school_program.py`` instead of edited by hand.
"""
from __future__ import annotations

try:
    from grade_four_math_lessons import _lesson as math_lesson
    from grade_three_math_language_lessons import (
        _lesson as language_lesson,
        build_transversal_integration as transversal_integration,
    )
except ImportError:
    from scripts.grade_four_math_lessons import _lesson as math_lesson
    from scripts.grade_three_math_language_lessons import (
        _lesson as language_lesson,
        build_transversal_integration as transversal_integration,
    )


def _p(topic, prior, vocabulary, anchor, misconception, focuses):
    return {
        "topic": topic,
        "prior": prior,
        "vocabulary": vocabulary,
        "anchor": anchor,
        "misconception": misconception,
        "focuses": focuses,
    }


MATH = {
    1: _p("Adición y sustracción de números enteros", "recta numérica, comparación de números y significado de una diferencia", "número entero, opuesto, valor absoluto, signo, desplazamiento, suma, diferencia", "un ascensor entre los pisos −4 y 8, cambios de temperatura ficticios y una recta numérica", "operar los signos como marcas aisladas o creer que restar siempre disminuye", ["Ubicar enteros y reconocer opuestos", "Interpretar cambios con signo en contexto", "Sumar enteros en la recta y con fichas", "Restar como suma del opuesto", "Resolver, comparar y comprobar estrategias"]),
    2: _p("Multiplicación y división de fracciones positivas", "fracciones equivalentes, números mixtos y operaciones con decimales", "factor, producto, cociente, fracción de una cantidad, recíproco, equivalencia", "tiras fraccionarias, áreas rectangulares y repartos de 3/4 en porciones de 1/8", "multiplicar numeradores y denominadores sin interpretar o invertir automáticamente cualquier fracción", ["Multiplicar una fracción por un natural", "Construir el producto de dos fracciones", "Comprender la división como medida y reparto", "Relacionar fracciones y decimales al operar"]),
    3: _p("Problemas con fracciones y decimales positivos", "multiplicación y división de fracciones, decimales y estimación", "dato, pregunta, unidad, representación, operación, estimación, comprobación", "recetas, escalas y recorridos ficticios que combinan 0,75, 1,2, 3/4 y 6/5", "elegir la operación por una palabra clave o mezclar representaciones sin conservar el valor", ["Comprender la situación y estimar", "Elegir entre fracción y decimal", "Resolver problemas multiplicativos", "Comprobar y comunicar la solución"]),
    4: _p("Porcentajes y cantidad de referencia", "fracciones de denominador cien, decimales y razones", "porcentaje, total, parte, tasa, cuadrícula de cien, equivalencia", "cuadrículas de cien, encuestas ficticias y descuentos didácticos sin compras reales", "calcular el porcentaje sobre una cantidad que no es el total o tratar % como una unidad", ["Representar porcentajes como partes de cien", "Relacionar porcentaje, fracción y decimal", "Calcular porcentajes por estrategias diversas", "Resolver y evaluar situaciones sencillas"]),
    5: _p("Potencias de base diez y notación científica", "valor posicional, multiplicación por potencias de diez y exponentes naturales", "potencia, base, exponente, exponente cero, notación científica, orden de magnitud", "tarjetas con 10⁰ a 10⁸, distancias y tamaños simulados expresados de dos maneras", "creer que el exponente multiplica la base o mover la coma sin atender el orden de magnitud", ["Construir potencias de base diez", "Comprender el exponente cero", "Descomponer por valor posicional", "Expresar números en notación científica", "Resolver y comprobar órdenes de magnitud"]),
    6: _p("Lenguaje algebraico y generalización", "patrones, propiedades de las operaciones y uso inicial de letras", "variable, expresión, término, coeficiente, constante, generalizar, ecuación", "patrones de baldosas, perímetros variables y tablas de entrada y salida", "usar la letra como etiqueta o generalizar desde un solo caso", ["Traducir relaciones a lenguaje algebraico", "Generalizar patrones numéricos y geométricos", "Expresar propiedades con letras", "Construir y validar ecuaciones"]),
    7: _p("Reducción de términos semejantes", "expresiones algebraicas, distributividad y números enteros", "término, coeficiente, parte literal, semejante, reducir, equivalencia", "tarjetas x, y, z y unidades con coeficientes positivos y negativos", "sumar términos que tienen distinta parte literal o perder el signo del coeficiente", ["Reconocer términos semejantes", "Representar sumas algebraicas", "Reducir expresiones con coeficientes enteros", "Comprobar equivalencia por sustitución"]),
    8: _p("Proporcionalidad directa e inversa", "razones, tablas, fracciones equivalentes y coordenadas", "razón, constante, proporción directa, proporción inversa, tabla, gráfica", "tablas de precio-cantidad, velocidad-tiempo y rectángulos de área fija", "suponer que toda relación creciente es directa o que toda relación decreciente es inversa", ["Distinguir relaciones proporcionales", "Construir tablas directas", "Construir tablas inversas", "Interpretar y comparar gráficas", "Resolver problemas y justificar el modelo"]),
    9: _p("Ecuaciones e inecuaciones lineales", "igualdad, operaciones inversas y lenguaje algebraico", "ecuación, inecuación, solución, conjunto solución, equivalencia, comprobar", "balanzas, rectas numéricas y situaciones ax=b o x/a>b con valores naturales", "cambiar de lado un término sin preservar la relación o dar un valor único para una inecuación", ["Modelar relaciones con ecuaciones", "Resolver ax=b y x/a=b", "Representar inecuaciones multiplicativas", "Resolver problemas en contexto", "Comprobar y comunicar conjuntos solución"]),
    10: _p("Ángulos interiores y exteriores de polígonos", "ángulos en triángulos y cuadriláteros, paralelismo y giros", "polígono, ángulo interior, ángulo exterior, vértice, diagonal, conjetura", "polígonos recortables de tres a ocho lados y una tabla para registrar sumas", "memorizar una fórmula sin explicar la triangulación o mezclar el ángulo exterior con el interior", ["Explorar la suma en triángulos y cuadriláteros", "Triangular polígonos y formular una regla", "Relacionar ángulos interiores y exteriores", "Resolver medidas faltantes y justificar"]),
    11: _p("Círculo, circunferencia y lugar geométrico", "medición, proporcionalidad, área y distancia a un punto", "círculo, circunferencia, centro, radio, diámetro, perímetro, pi, lugar geométrico", "círculos de cartón, hilo, regla y una tabla de diámetro y perímetro", "confundir círculo con circunferencia o usar diámetro donde la fórmula requiere radio", ["Distinguir círculo, circunferencia, radio y diámetro", "Investigar la relación perímetro-diámetro", "Estimar perímetro y área", "Resolver problemas de medida", "Construir el círculo como lugar geométrico"]),
    12: _p("Construcciones geométricas y puntos notables", "uso de regla, compás y transportador; congruencia y propiedades de triángulos", "paralela, perpendicular, bisectriz, altura, punto medio, incentro, circuncentro, baricentro, congruencia", "hojas sin cuadrícula, regla, compás, escuadra y un protocolo de trazos verificables", "aceptar una construcción por apariencia sin comprobar sus propiedades", ["Construir paralelas, perpendiculares y puntos medios", "Trazar bisectrices y alturas", "Construir incentro, circuncentro y baricentro", "Construir figuras congruentes", "Explicar y comprobar cada construcción"]),
    13: _p("Área de triángulos, paralelogramos y trapecios", "área de rectángulos, descomposición y altura perpendicular", "base, altura, área, paralelogramo, triángulo, trapecio, descomponer", "figuras recortables y cuadrículas donde una pieza se traslada para formar un rectángulo", "usar un lado inclinado como altura o aplicar una fórmula sin reconocer la figura", ["Derivar el área del paralelogramo", "Derivar el área del triángulo", "Derivar el área del trapecio", "Resolver y comparar descomposiciones"]),
    14: _p("Pares ordenados y vectores en el plano", "coordenadas cartesianas, desplazamientos y números enteros", "origen, eje, cuadrante, par ordenado, vector, componente, traslación", "plano cartesiano de −8 a 8 con rutas y fichas de desplazamiento", "intercambiar coordenadas o describir un vector solo por su longitud", ["Ubicar puntos en cuatro cuadrantes", "Leer y representar vectores", "Trasladar puntos mediante vectores", "Resolver rutas y comprobar coordenadas"]),
    15: _p("Estimación poblacional mediante muestreo", "porcentajes, frecuencias y lectura crítica de datos", "población, muestra, representatividad, aleatorio, sesgo, estimación", "una población simulada de fichas de colores y distintos planes de muestreo", "generalizar desde una muestra cómoda, demasiado pequeña o elegida para confirmar una idea", ["Distinguir población y muestra", "Comparar métodos de selección", "Estimar un porcentaje poblacional", "Comunicar estimación, variación y límites"]),
    16: _p("Frecuencias absolutas, relativas y gráficos", "tablas de conteo, fracciones, porcentajes y tipos de gráfico", "frecuencia absoluta, frecuencia relativa, porcentaje, intervalo, escala, gráfico", "dos muestras ficticias registradas como lista de datos y tarjetas para elegir gráficos", "comparar frecuencias absolutas de muestras de distinto tamaño o escoger un gráfico por decoración", ["Organizar datos en una tabla", "Calcular frecuencias relativas", "Elegir y construir un gráfico apropiado", "Interpretar y revisar representaciones"]),
    17: _p("Tendencia central, rango e inferencias", "promedio, lectura de distribuciones y comparación de datos", "media, mediana, moda, rango, valor atípico, distribución, inferencia", "conjuntos ficticios con igual media y distinta dispersión, incluyendo un valor extremo", "usar siempre la media o comparar poblaciones solo por una medida", ["Calcular e interpretar media, mediana y moda", "Comprender el rango", "Elegir la medida pertinente", "Examinar el efecto de un valor atípico", "Comparar distribuciones e inferir con cautela"]),
    18: _p("Probabilidad experimental y frecuencia relativa", "razones, fracciones, porcentajes y experimentos aleatorios", "evento, resultado, ensayo, frecuencia relativa, probabilidad, estimar", "monedas, dados y ruletas equilibradas con registros acumulados por bloques", "creer que una racha obliga el resultado siguiente o confundir frecuencia absoluta con probabilidad", ["Estimar probabilidades intuitivamente", "Realizar y registrar experimentos", "Expresar frecuencias relativas", "Relacionar razón, fracción y porcentaje"]),
    19: _p("Probabilidad teórica y experimental", "espacio muestral, frecuencia relativa y representaciones de eventos", "probabilidad teórica, probabilidad experimental, espacio muestral, diagrama de árbol, simulación", "dos monedas, dados o ruletas representados con árboles, tablas y simulaciones manuales", "esperar coincidencia exacta en pocas repeticiones o contar resultados no equiprobables como iguales", ["Construir el espacio muestral", "Calcular una probabilidad teórica", "Comparar con frecuencias experimentales", "Explicar la variación al aumentar ensayos"]),
}


LANGUAGE = {
    1: _p("Trayectoria lectora y selección con propósito", "experiencias de lectura personal y criterios básicos de selección", "propósito, preferencia, catálogo, recomendación, muestra, bitácora", "una mesa o catálogo con microcuentos, poemas, artículos, cómics y divulgación de libre uso", "confundir elegir con tomar el texto más corto o convertir el gusto lector en una obligación uniforme", ["Reconocer propósitos y preferencias lectoras", "Explorar textos antes de elegir", "Justificar y revisar una selección", "Sostener una lectura con metas alcanzables", "Compartir una recomendación situada", "Construir una trayectoria lectora personal"]),
    2: _p("Literatura y dimensiones de la experiencia humana", "lectura inferencial y conversación respetuosa sobre obras", "experiencia humana, tema, perspectiva, herencia cultural, contexto, evidencia", "fragmentos originales o de dominio público sobre pertenencia, pérdida, amistad y decisiones difíciles", "reducir una obra a una moraleja única o exigir que el estudiante revele experiencias personales", ["Reconocer una experiencia humana en la obra", "Distinguir situación, tema y juicio", "Comparar perspectivas de personajes", "Relacionar texto y herencia cultural", "Dialogar sin exponer la intimidad", "Elaborar una reflexión con evidencia"]),
    3: _p("Análisis de narraciones", "secuencia, caracterización, narrador e inferencia", "conflicto, personaje, consecuencia, narrador, diálogo, anacronía, intertexto", "un relato original con conflicto, voces diferenciadas y hechos presentados fuera de orden", "resumir la trama sin explicar cómo las decisiones o la voz narrativa producen sentido", ["Delimitar conflicto y fuerzas en tensión", "Analizar acciones y consecuencias", "Caracterizar personajes con evidencia", "Distinguir narrador y voces de personajes", "Reconstruir la disposición temporal", "Comparar elementos con otra narración", "Formular una interpretación integrada"]),
    4: _p("Análisis de poemas", "lectura expresiva, imágenes y lenguaje figurado", "hablante lírico, imagen, sentido, comparación, metáfora, ritmo, sonoridad", "poemas breves originales y de dominio público con imágenes, repeticiones y ritmos contrastados", "enumerar figuras literarias sin explicar su efecto o confundir al hablante con el autor", ["Escuchar imágenes y primera impresión", "Analizar lenguaje sensorial", "Interpretar lenguaje figurado", "Explorar ritmo y sonoridad", "Relacionar forma y estado de ánimo", "Comparar dos poemas", "Construir una lectura fundamentada"]),
    5: _p("Romances y poesía popular", "recursos poéticos, narración en verso y contexto cultural", "romance, verso octosílabo, rima asonante, oralidad, variante, tradición", "romances de dominio público y muestras breves de poesía popular con procedencia identificada", "tratar la poesía popular como una forma fija sin variantes ni contexto", ["Reconocer relato y voz en el romance", "Explorar ritmo y rima asonante", "Relacionar oralidad, memoria y variación", "Interpretar desde el contexto", "Comparar y comunicar una lectura"]),
    6: _p("Relatos mitológicos y contexto", "estructura narrativa, símbolos y búsqueda de contexto", "mito, cosmogonía, héroe, divinidad, símbolo, versión, contexto", "relatos mitológicos de distintas tradiciones en versiones autorizadas o de dominio público", "llamar mito a cualquier relato fantástico o mezclar tradiciones como si fueran equivalentes", ["Distinguir rasgos del relato mitológico", "Analizar conflicto, personajes y símbolos", "Investigar contexto y procedencia", "Comparar versiones sin jerarquizarlas", "Interpretar la función cultural del relato"]),
    7: _p("Interpretación literaria situada", "análisis de narraciones y poemas con evidencia", "interpretación, dilema, postura, visión de mundo, contexto histórico, evidencia", "dos pasajes literarios con un dilema y una ficha contextual breve de fuente verificable", "presentar una opinión personal como interpretación sin volver al texto", ["Formular una pregunta interpretativa", "Relacionar experiencia y evidencia sin autobiografía obligatoria", "Analizar un dilema y sus alternativas", "Construir una postura fundamentada", "Vincular obra y visión de mundo", "Revisar la interpretación con contexto"]),
    8: _p("Lectura crítica de textos argumentativos", "distinción entre hecho y opinión, propósito y evidencia", "tesis, postura, argumento, evidencia, hecho, opinión, contraargumento", "una columna, una carta y un discurso didácticos sobre el mismo asunto no sensible", "aceptar una afirmación por seguridad del tono o rechazarla solo por desacuerdo", ["Identificar situación y postura", "Reconstruir argumentos", "Distinguir hechos y opiniones", "Evaluar pertinencia de la evidencia", "Detectar supuestos y vacíos", "Construir una postura propia", "Responder con argumentos revisables"]),
    9: _p("Análisis crítico de medios y multimodalidad", "lectura de noticias, publicidad e imágenes", "propósito explícito, propósito implícito, estereotipo, prejuicio, encuadre, gráfico, efecto", "noticia, publicación social y aviso ficticios con datos, imagen y diseño contrastados", "leer solo el texto verbal o atribuir intención sin identificar señales observables", ["Reconocer género, emisor y audiencia", "Distinguir hechos y opiniones", "Inferir propósitos explícitos e implícitos", "Analizar imagen, gráfico y diseño", "Reconocer estereotipos sin reproducirlos", "Examinar efectos de la divulgación", "Elaborar una evaluación fundamentada"]),
    10: _p("Textos no literarios para contextualizar obras", "búsqueda, lectura informativa y relación entre textos", "contextualizar, antecedente, fuente, concepto, relación, límite", "una obra breve y dos fichas informativas de distinta procedencia sobre su época o tema", "usar el contexto para reemplazar la lectura literaria o asumir que explica toda la obra", ["Formular una necesidad de contexto", "Seleccionar información pertinente", "Relacionar información y pasaje literario", "Reconocer límites de la contextualización", "Comunicar una comprensión enriquecida"]),
    11: _p("Estrategias de comprensión según propósito", "monitoreo lector, resumen e inferencia", "propósito, resumen, pregunta, referente, multimodal, inconsistencia, estrategia", "un texto multimodal con referentes distantes, palabra desconocida y una aparente inconsistencia", "aplicar todas las estrategias como receta o resumir copiando oraciones", ["Definir propósito y anticipar dificultades", "Resumir conservando relaciones", "Formular preguntas que hacen avanzar", "Relacionar imagen, sonido y escritura", "Recuperar referentes perdidos", "Resolver vocabulario e inconsistencias", "Evaluar qué estrategia funcionó"]),
    12: _p("Escritura creativa con decisiones de autor", "exploración de géneros y escritura para una audiencia", "tema, género, destinatario, voz, escena, imagen, borrador", "un banco de detonantes, formas y destinatarios ficticios para cuento, crónica, carta, diario o poema", "usar una plantilla que borra la voz o corregir la forma antes de desarrollar una idea", ["Explorar tema, género y destinatario", "Probar una voz y una forma", "Desarrollar un núcleo significativo", "Compartir y revisar una decisión", "Editar una versión para circular"]),
    13: _p("Textos explicativos con fuentes", "organización de párrafos, investigación y síntesis", "tema, explicación, fuente, progresión temática, anáfora, recurso gráfico, referencia", "un dossier breve de fuentes verificables sobre un fenómeno cotidiano o cultural", "acumular datos sin jerarquía o copiar fuentes sin integrarlas ni atribuirlas", ["Delimitar tema, propósito y audiencia", "Seleccionar y registrar fuentes", "Organizar una progresión explicativa", "Desarrollar con hechos, ejemplos y descripciones", "Usar correferencias y recursos gráficos", "Cerrar y referenciar coherentemente"]),
    14: _p("Escritura persuasiva breve", "opinión fundamentada y coherencia temática", "afirmación, audiencia, razón, evidencia, pertinencia, cohesión, cierre", "tres situaciones de escritura pública ficticia: carta, editorial escolar y crítica literaria", "confundir persuadir con imponer o repetir la afirmación sin aportar evidencia", ["Definir asunto, audiencia y afirmación", "Seleccionar razones y evidencia", "Ordenar un recorrido persuasivo", "Redactar manteniendo el foco", "Incorporar una objeción pertinente", "Revisar efecto, coherencia y tono"]),
    15: _p("Proceso de escritura situado", "planificación, borrador y revisión de textos", "contexto, destinatario, propósito, registro, coherencia, cohesión, edición", "un texto deliberadamente mejorable y una pauta separada de contenido, organización, lenguaje y presentación", "corregir solo ortografía o intentar revisar todos los aspectos al mismo tiempo", ["Analizar contexto, género y destinatario", "Recopilar y organizar ideas", "Escribir un borrador completo", "Revisar pertinencia y progresión", "Mejorar cohesión, vocabulario y concordancia", "Editar formato, ortografía y versión final"]),
    16: _p("Oración, sujeto y predicado al servicio de la escritura", "reconocimiento de verbos y construcción de oraciones completas", "oración, sujeto, sujeto tácito, predicado, núcleo, concordancia", "un párrafo con fragmentos, concordancias problemáticas y sujetos en distintas posiciones", "buscar siempre el sujeto antes del verbo o corregir gramática sin atender el sentido", ["Distinguir oración completa y fragmento", "Reconocer predicado y verbo núcleo", "Ubicar sujetos expresos y tácitos", "Revisar concordancia", "Mejorar un texto sin uniformar su estilo"]),
    17: _p("Correferencia léxica y cohesión", "reconocimiento de repeticiones y relaciones semánticas", "referente, sustitución léxica, sinonimia, hiperonimia, cohesión, precisión", "un texto breve con repeticiones ambiguas y un banco de sustituciones posibles", "reemplazar toda repetición por sinónimos que cambian el significado", ["Reconocer referentes y repeticiones útiles", "Aplicar sustitución léxica precisa", "Usar sinonimia según contexto", "Construir cadenas con hiperónimos", "Revisar cohesión y ausencia de ambigüedad"]),
    18: _p("Secuencia de tiempos verbales en narración", "tiempos del indicativo y orden de acontecimientos", "presente, pretérito perfecto simple, imperfecto, pluscuamperfecto, secuencia", "una narración breve con acciones principales, antecedentes y descripciones temporales", "cambiar de tiempo verbal sin función o mantener uno solo aunque cambie la relación temporal", ["Reconocer planos temporales", "Distinguir acción principal y marco", "Expresar anterioridad", "Mantener y justificar una secuencia", "Revisar una narración completa"]),
    19: _p("Ortografía y puntuación para facilitar comprensión", "reglas ortográficas frecuentes y lectura de puntuación", "ortografía literal, acentuación, punto, coma, raya, dos puntos, consulta", "un texto original con problemas seleccionados de tildes, letras y puntuación de diálogo", "corregir por apariencia sin poder justificar ni consultar los casos no regulares", ["Diagnosticar patrones de error", "Aplicar reglas literales y acentuales", "Verificar palabras de escritura no predecible", "Usar punto, coma, raya y dos puntos", "Editar y explicar decisiones"]),
    20: _p("Comprensión crítica de textos orales y audiovisuales", "escucha activa, toma de notas y análisis multimodal", "postura, argumento, hecho, opinión, punto de vista, montaje, sonido, imagen", "dos cápsulas audiovisuales didácticas sobre un tema común con guiones, imágenes y sonidos contrastados", "recordar datos sueltos o dejar que la imagen sustituya la evaluación de lo dicho", ["Definir propósito de escucha", "Registrar temas y conceptos centrales", "Distinguir hechos y opiniones", "Comparar puntos de vista", "Analizar relaciones entre imagen, texto y sonido", "Relacionar con obras y manifestaciones", "Evaluar y fundamentar una postura"]),
    21: _p("Diálogo constructivo para explorar y debatir", "escucha, turnos y fundamentación", "foco, reformulación, fundamento, pregunta, desacuerdo, acuerdo, turno", "un dilema literario o escolar ficticio con cuatro perspectivas y evidencias disponibles", "esperar el turno para repetir la propia postura o atacar a la persona", ["Preparar una postura provisional", "Escuchar y reformular al interlocutor", "Fundamentar y responder al foco", "Preguntar para profundizar", "Discrepar cuidando la relación", "Negociar acuerdos y asuntos abiertos"]),
    22: _p("Exposición oral clara y fundada", "investigación breve y organización de ideas", "audiencia, idea central, progresión, ejemplo, concepto clave, apoyo visual", "un conjunto de datos y fuentes breves para preparar una exposición de tres minutos", "leer diapositivas, acumular datos o usar recursos visuales sin relación con la explicación", ["Definir propósito, audiencia y tema", "Verificar información", "Organizar una progresión oral", "Explicar conceptos con ejemplos", "Diseñar apoyo visual funcional", "Ensayar, presentar y retroalimentar"]),
    23: _p("Recursos verbales, paraverbales y registro oral", "comparación entre oralidad y escritura, escucha y cortesía", "registro, contexto, destinatario, volumen, velocidad, dicción, desacuerdo", "tres versiones de un mismo mensaje para conversación, exposición y audio público", "confundir registro formal con palabras difíciles o evaluar una variedad lingüística como incorrecta", ["Comparar texto oral y escrito", "Reconocer contexto, propósito y destinatario", "Ajustar registro sin discriminar variedades", "Cuidar la relación al discrepar", "Usar volumen, velocidad y dicción con propósito", "Revisar el efecto en una audiencia"]),
    24: _p("Investigación sobre lenguaje y literatura", "formulación de preguntas, búsqueda y registro de fuentes", "tema, pregunta, palabra clave, catálogo, suficiencia, categoría, bibliografía, hallazgo", "una pregunta modelo y un conjunto mixto de fuentes de biblioteca e internet previamente revisadas", "buscar un tema demasiado amplio o acumular información sin evaluar si responde la pregunta", ["Delimitar tema y pregunta", "Diseñar palabras clave y rutas de búsqueda", "Localizar información con organizadores", "Evaluar relevancia y suficiencia", "Registrar y categorizar hallazgos", "Comunicar resultados con fuentes"]),
    25: _p("Síntesis y organización de ideas", "identificación de ideas principales y toma de notas", "idea principal, detalle, jerarquía, paráfrasis, esquema, síntesis", "un texto y una explicación oral breve con redundancias, ejemplos y relaciones causales", "copiar frases completas o eliminar conexiones necesarias al acortar", ["Definir el propósito del registro", "Distinguir ideas y detalles", "Parafrasear con precisión", "Organizar jerarquías y relaciones", "Producir y comprobar una síntesis"]),
}


def _retarget_links(lesson: dict, old: str, new: str) -> dict:
    for link in lesson.get("transversal", []):
        link["code"] = link["code"].replace(old, new)
    return lesson


def _classroom_voice(lesson: dict, profile: dict, index: int, is_math: bool) -> None:
    """Give seventh-grade lessons a direct, varied classroom voice."""
    focus = profile["focuses"][index]
    action = focus[0].lower() + focus[1:]
    anchor = profile["anchor"]
    misconception = profile["misconception"]
    if is_math:
        openings = (
            f"Abre con {anchor}. Pide una estimación silenciosa y recoge dos maneras distintas de empezar, sin confirmar todavía cuál funciona.",
            f"Muestra {anchor} y pregunta qué se puede averiguar antes de calcular. El curso anota una predicción y el dato que considera decisivo.",
            f"Propón una respuesta ficticia sobre {anchor}, una correcta y otra plausible. El curso decide cuál merece confianza y explica qué comprobaría.",
            f"Entrega o proyecta {anchor}. Da un minuto para explorar y luego invita a formular una pregunta matemática que ayude a {action}.",
            f"Retoma {anchor} con un dato cambiado. Antes de resolver, cada estudiante anticipa qué debería mantenerse y qué podría variar.",
        )
        models = (
            f"Resuelve un primer caso en voz alta. Detente al elegir la representación y muestra cómo esa elección ayuda a {action}; al final vuelve al contexto y comprueba la respuesta.",
            f"Representa el mismo caso de dos maneras y conecta cada paso entre ambas. Señala qué información se vuelve visible y cuál podría quedar oculta.",
            f"Ensaya una estrategia que parece razonable, pero conduce a «{misconception}». Localiza el momento exacto del error y reconstruye la solución con el curso.",
            f"Compara dos caminos para resolver el caso. Nombra qué tienen en común, cuándo conviene cada uno y cómo permiten verificar el resultado.",
            f"Parte de una solución incompleta escrita como podría aparecer en un cuaderno. Agrega las decisiones necesarias hasta convertirla en una explicación clara y comprobable.",
        )
        lesson["purpose"] = f"Acompañar al curso a {action} y a justificar sus decisiones con una representación y una comprobación claras."
        lesson["goal"] = f"Hoy aprenderé a {action}; mostraré mi estrategia y comprobaré si mi respuesta tiene sentido."
        lesson["opening"] = openings[index % len(openings)]
        lesson["model"] = models[index % len(models)]
        lesson["guided"] = (
            f"En parejas, resuelven dos casos breves construidos desde {anchor}. En el primero reciben una pregunta de apoyo; "
            "en el segundo eligen su propia estrategia. Comparan resultados, reciben retroalimentación sobre un solo criterio y mejoran su explicación."
        )
        lesson["independent"] = (
            f"Cada estudiante resuelve una situación nueva que exige {action}. Debe dejar visible cómo pensó, dar una respuesta situada "
            "y comprobarla por una vía distinta. Puede elegir la representación que mejor le sirva."
        )
        lesson["ticket"] = "Escribe qué decisión fue más importante en tu solución y una comprobación breve que permita confiar en ella."
    else:
        openings = (
            f"Dispón {anchor} y deja unos minutos para mirar, leer o escuchar. Cada estudiante elige un detalle que le llame la atención y explica por qué.",
            f"Presenta {anchor} sin anunciar una interpretación. El curso registra una primera idea y la palabra, imagen o rasgo que la hizo aparecer.",
            f"Comparte dos respuestas posibles ante {anchor}. Pide decidir cuál dialoga mejor con el texto y qué evidencia habría que agregar a la otra.",
            f"Inicia con una lectura o escucha breve de {anchor}. Después, cada estudiante formula una pregunta genuina que el material le deja abierta.",
            f"Vuelve a {anchor} desde otra voz, audiencia o propósito. El curso anticipa qué cambiaría en la lectura o en la producción.",
            f"Ofrece tres puertas de entrada a {anchor}: una frase, una imagen y una pregunta. Cada estudiante escoge una y registra su primera respuesta.",
            f"Lee o muestra {anchor} por partes. Antes de revelar la siguiente, el curso predice, conversa y ajusta su interpretación inicial.",
        )
        models = (
            f"Piensa en voz alta y muestra cómo {action}. Haz una pausa para explicar cómo una pista cambia o confirma la interpretación, sin convertirla en la única lectura posible.",
            f"Compara dos interpretaciones plausibles. Sigue la evidencia de cada una, reconoce sus límites y explica por qué una responde mejor al propósito de hoy.",
            f"Construye una respuesta delante del curso: parte con una idea sencilla, incorpora una evidencia precisa y revisa una frase para que diga exactamente lo que quieres comunicar.",
            f"Muestra una primera respuesta que cae en «{misconception}». Relee el pasaje o revisa la situación, identifica el problema y mejora la respuesta sin borrar su voz.",
            f"Lee, escucha o produce un ejemplo breve y comenta las decisiones importantes: propósito, selección de evidencia, organización y efecto en quien recibe el mensaje.",
            f"Modela una búsqueda acotada dentro del material. Explica qué información sirve, cuál distrae y cómo registrar lo necesario con palabras propias.",
            f"Ensaya una respuesta oral breve. Ajusta volumen, vocabulario o estructura al propósito y pide al curso identificar el cambio que volvió más claro el mensaje.",
        )
        lesson["purpose"] = f"Crear condiciones para que el curso pueda {action}, converse sobre sus decisiones y las sostenga con evidencia pertinente."
        lesson["goal"] = f"Hoy voy a {action}; explicaré qué decisión tomé y en qué evidencia me apoyé."
        lesson["opening"] = openings[index % len(openings)]
        lesson["model"] = models[index % len(models)]
        lesson["guided"] = (
            f"En parejas, trabajan con una segunda muestra de {anchor}. Primero elaboran respuestas propias; después escuchan la lectura del compañero, "
            "eligen una evidencia que vale la pena conservar y mejoran un aspecto concreto sin uniformar sus voces."
        )
        lesson["independent"] = (
            f"Cada estudiante enfrenta un texto, audiencia o situación nueva para {action}. Produce una respuesta propia, incorpora evidencia suficiente "
            "y explica una elección de lectura, escritura u oralidad."
        )
        lesson["ticket"] = "Comparte una idea final y marca la evidencia o decisión que más ayudó a construirla; agrega una duda que todavía valga la pena explorar."
    visible_goal = lesson["goal"].removeprefix("Hoy ").rstrip(".")
    for link in lesson.get("transversal", []):
        application = link.get("application", "")
        if "meta «" in application:
            link["application"] = application.split("meta «", 1)[0] + f"meta «{visible_goal}»."


def _sequence(code: str, profile: dict, subject: str) -> dict:
    is_math = subject == "matematica"
    lessons = []
    for index in range(len(profile["focuses"])):
        if is_math:
            lesson = math_lesson(code, index, profile)
            _retarget_links(lesson, "MA04", "MA07")
        else:
            lesson = language_lesson(code, index, profile, "language")
            _retarget_links(lesson, "LE03", "LE07")
        _classroom_voice(lesson, profile, index, is_math)
        lessons.append(lesson)
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": (
            f"{profile['topic']} se construye desde {profile['prior'][0].lower() + profile['prior'][1:]}. "
            f"La secuencia cambia texto, representación, problema y evidencia en cada clase, y enfrenta la confusión «{profile['misconception']}»."
        ),
        "prerequisites": profile["prior"],
        "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"{('Matemática' if is_math else 'Lengua y Literatura')} · progresión interna en {len(lessons)} clases"],
            "unit_origin": "Organización pedagógica interna derivada del eje y del OA; no se presenta como una unidad oficial del programa.",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del OA oficial.",
            "source": f"https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/{subject}/7-basico/{code.lower().replace(' ', '-')}",
        },
        "lessons": lessons,
    }


def build_sequence(code: str) -> dict | None:
    if code.startswith("MA07 OA "):
        number = int(code.rsplit(" ", 1)[-1])
        return _sequence(code, MATH[number], "matematica") if number in MATH else None
    if code.startswith("LE07 OA "):
        number = int(code.rsplit(" ", 1)[-1])
        return _sequence(code, LANGUAGE[number], "lengua-literatura") if number in LANGUAGE else None
    return None


def build_transversal_integration(item: dict) -> dict:
    return transversal_integration(item)


SEQUENCES = {
    **{f"MA07 OA {number:02d}": True for number in MATH},
    **{f"LE07 OA {number:02d}": True for number in LANGUAGE},
}

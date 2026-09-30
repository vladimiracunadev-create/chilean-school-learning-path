"""Deterministic, classroom-facing enrichment for developed lessons.

The source modules define disciplinary progressions. This layer adds the
concrete artefact, exact prompt, response reference, assessment anchors and a
real 45-minute distribution that every published lesson must expose.
"""
from __future__ import annotations

import hashlib
import re


LEVELS = (
    ("Aún no observable", "No produce evidencia suficiente o responde sin relacionarla con la consigna."),
    ("En desarrollo", "Responde parcialmente y necesita apoyo para usar el criterio o la evidencia."),
    ("Logrado", "Responde la consigna, usa el criterio central y deja una evidencia comprensible."),
    ("Profundizado", "Justifica, contrasta o transfiere la decisión a una condición nueva."),
)


def _seed(code: str, lesson_number: int) -> int:
    digest = hashlib.sha256(f"{code}:{lesson_number}".encode("utf-8")).hexdigest()
    return int(digest[:8], 16)


def _clean(value: str) -> str:
    value = re.sub(r"\s+,", ",", value)
    value = value.replace(",,", ",").replace("..", ".")
    value = value.replace("Modela cómo modelar un criterio:", "Hace visible el criterio de análisis:")
    value = value.replace(", no por imitar el ejemplo", " y con evidencia propia")
    value = value.replace("no por imitar el ejemplo", "con evidencia propia")
    value = value.replace("no se transfiere mecánicamente a otro OA", "se contrasta con el criterio particular de este OA")
    value = re.sub(r"^Desarrollar (.+?) mediante (.+?), con ", r"Enseñar \1 a través de \2, con ", value)
    return re.sub(r"\s{2,}", " ", value).strip()


def _clean_nested(value):
    if isinstance(value, str):
        return _clean(value)
    if isinstance(value, list):
        return [_clean_nested(item) for item in value]
    if isinstance(value, dict):
        return {key: _clean_nested(item) for key, item in value.items()}
    return value


def _math(topic: str, focus: str, seed: int, grade: int) -> dict:
    if grade <= 1:
        a, b, c = 4 + seed % 8, 2 + seed % 3, 1 + seed % 3
    elif grade == 2:
        a, b, c = 12 + seed % 29, 2 + seed % 5, 1 + seed % 5
    else:
        a, b, c = 12 + seed % 19, 3 + seed % 7, 2 + seed % 5
    lowered = f"{topic} {focus}".lower()
    if any(word in lowered for word in ("conteo", "contar", "cardinal")):
        total = min(15, a + b + c) if grade == 1 else a + b + c
        resource = f"Colección de {total} fichas, bandeja con zonas «por contar/contado» y tarjeta numeral {total}."
        prompt = f"Cuenta las {total} fichas sin omitir ni repetir, registra el total y compruébalo después de cambiar su disposición."
        reference = f"Debe asignar una palabra número a cada ficha, declarar {total} como cardinal y conservar el total al reorganizar la colección."
    elif "fracc" in lowered:
        a, b = 2 + seed % 5, 6 + seed % 7
        resource = f"Tarjeta A: {a}/{b}; tarjeta B: {(a + 1)}/{b}; rectángulo dividido en {b} partes iguales."
        prompt = f"Representa {a}/{b}, compáralo con {(a + 1)}/{b} y explica qué permanece igual y qué cambia."
        reference = f"Una respuesta lograda representa {a} y {a + 1} partes de un mismo entero dividido en {b}, usa < y justifica con la unidad común."
    elif any(word in lowered for word in ("porcentaje", "porcent")):
        percent, whole = (10 + seed % 7) * 5, (4 + seed % 5) * 20
        resource = f"Cuadrícula de 100 casillas y tarjeta de situación: calcular {percent}% de {whole}."
        prompt = f"Representa {percent}% en la cuadrícula, calcula {percent}% de {whole} por dos vías y comprueba que coinciden."
        reference = f"Debe relacionar {percent}% con {percent}/100 y obtener {percent * whole // 100}; la segunda vía puede usar 10%, 5% o proporcionalidad."
    elif any(word in lowered for word in ("área", "perímetro", "ángulo", "geometr")):
        width, height = 4 + seed % 8, 3 + seed % 6
        resource = f"Rectángulo cuadriculado de {width} por {height} unidades, regla y una variante con una dimensión duplicada."
        prompt = f"Representa la figura, calcula las medidas pertinentes y predice qué cambia al duplicar el lado de {width} unidades."
        reference = f"La respuesta muestra operaciones con {width} y {height}, rotula unidades y distingue qué medida cambia de manera aditiva o multiplicativa."
    elif any(word in lowered for word in ("dato", "gráfico", "probab", "azar")):
        values = [c + ((seed >> shift) % 7) for shift in (0, 3, 6, 9)]
        resource = "Tabla de frecuencias: A={0}, B={1}, C={2}, D={3}; cuatro tarjetas para representar los mismos datos.".format(*values)
        prompt = "Construye una representación, formula una afirmación verificable y señala el dato que podría hacerla falsa."
        reference = "La representación conserva las cuatro frecuencias, incluye escala y la conclusión cita al menos dos valores de la tabla."
    else:
        if grade <= 2:
            values = (a, a + b, a + b + c)
        else:
            values = (a, a * b, a * b + c)
        resource = f"Tarjetas numéricas {values[0]}, {values[1]}, {values[2]} y una recta numérica sin completar."
        prompt = f"Ordena y relaciona {values[0]}, {values[1]} y {values[2]}; resuelve una situación que use las tres cantidades y comprueba con otra representación."
        reference = "La solución usa las tres cantidades, muestra un procedimiento reproducible y comprueba sin repetir exactamente el mismo cálculo."
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _math_grade_seven(topic: str, focus: str, seed: int) -> dict:
    """Return a concrete artefact matched to the actual seventh-grade OA."""
    lowered = f"{topic} {focus}".lower()
    if "entero" in lowered:
        start, change = -8 + seed % 7, 3 + seed % 8
        resource = f"Recta de −12 a 12, fichas +/− y tarjeta: un móvil parte en {start}, cambia {change} unidades y luego retrocede {change + 2}."
        prompt = "Representa los dos cambios en la recta y con fichas, escribe una expresión con enteros y explica por qué restar puede aumentar un valor."
        reference = f"Parte en {start}, llega primero a {start + change} y termina en {start - 2}; conecta desplazamiento, opuesto y expresión simbólica."
    elif "fraccion" in lowered or "decimal" in lowered:
        resource = "Dos tiras unidad: 3/4 y 2/3; cuadrícula decimal; tarjeta de reparto de 3/4 L en porciones de 1/8 L."
        prompt = f"Para «{focus.lower()}», representa 3/4 × 2/3 y 3/4 ÷ 1/8, relaciona un resultado con decimal y comprueba por estimación."
        reference = "Obtiene 1/2 y 6, distingue producto de cociente y explica el entero de referencia; la estimación confirma que 3/4 × 2/3 es menor que uno."
    elif "porcentaje" in lowered:
        whole, percent = (8 + seed % 5) * 20, (3 + seed % 8) * 5
        result = whole * percent // 100
        resource = f"Cuadrícula de cien y encuesta ficticia con {whole} respuestas; {percent}% eligió la opción A."
        prompt = f"Representa {percent}%, calcula cuántas de las {whole} respuestas corresponden a A por dos estrategias y aclara el total de referencia."
        reference = f"Obtiene {result}, relaciona {percent}/100 con el total y muestra dos vías coherentes, por ejemplo 10% y 5% o proporción."
    elif "potencia" in lowered or "científica" in lowered or "magnitud" in lowered:
        exponent, coefficient = 3 + seed % 5, 2 + seed % 7
        numeral = f"{coefficient}{'0' * exponent}"
        resource = f"Tarjetas 10⁰, 10¹, 10², 10^{exponent}, {coefficient} × 10^{exponent} y {numeral}; tabla de valor posicional."
        prompt = f"Ordena las tarjetas, explica el exponente y expresa {numeral} en notación científica; crea un error plausible y corrígelo."
        reference = f"Relaciona 10^{exponent} con uno seguido de {exponent} ceros y escribe {coefficient} × 10^{exponent}; 10⁰ vale 1, no 0 ni 10."
    elif any(word in lowered for word in ("algebra", "término", "expresion", "generaliz")):
        a, b = 2 + seed % 5, 3 + (seed // 7) % 5
        resource = f"Patrón de figuras: etapa n usa {a}n+{b} fichas; tarjetas {a}x, {b}x, −x, {b}y y {a + b}."
        prompt = f"Representa tres etapas, justifica la regla {a}n+{b} y reduce {a}x+{b}x−x+{b}y sin reunir términos distintos."
        reference = f"La regla reproduce las etapas y la reducción conserva partes literales: {a + b - 1}x+{b}y; comprueba sustituyendo valores."
    elif "ecuacion" in lowered or "inecuacion" in lowered:
        factor, solution = 2 + seed % 6, 3 + (seed // 5) % 7
        result = factor * solution
        resource = f"Balanza y recta numérica para {factor}x={result}, {factor}x<{result} y x/{factor}>{solution - 1}."
        prompt = "Modela las tres relaciones, resuélvelas conservando igualdad o desigualdad y comprueba un valor que pertenece y otro que no pertenece."
        reference = f"La ecuación da x={solution}; {factor}x<{result} exige x<{solution}. Muestra la operación equivalente en ambos miembros."
    elif "proporcional" in lowered:
        resource = "Tabla A: cantidad 1,2,4,8 y costo 3,6,12,24; tabla B: personas 1,2,4,8 y tiempo 24,12,6,3; plano cartesiano."
        prompt = "Grafica ambas tablas, identifica cuál relación es directa y cuál inversa, y justifica con una constante o producto antes de resolver un caso nuevo."
        reference = "En A el cociente costo/cantidad es 3; en B el producto personas·tiempo es 24. La explicación distingue ambos modelos."
    elif any(word in lowered for word in ("círculo", "circunferencia", "radio", "diámetro")):
        diameter = 6 + 2 * (seed % 5)
        resource = f"Tres círculos de papel; uno con diámetro {diameter} cm, hilo, regla, compás y tabla radio-diámetro-perímetro-área."
        prompt = f"Mide y estima, completa la fila del círculo de diámetro {diameter} cm con π≈3,14 y explica la circunferencia como lugar geométrico."
        reference = f"Radio {diameter/2:g} cm, perímetro ≈{diameter*3.14:.2f} cm y área ≈{3.14*(diameter/2)**2:.2f} cm²; los puntos de la circunferencia equidistan del centro."
    elif any(word in lowered for word in ("ángulo", "polígono")):
        sides = 4 + seed % 5
        total = (sides - 2) * 180
        resource = f"Polígono convexo de {sides} lados recortable, regla, transportador y tabla lados-triángulos-suma interior."
        prompt = f"Triangula desde un vértice, deduce la suma interior del polígono de {sides} lados y usa la relación interior-exterior para una medida faltante."
        reference = f"Se forman {sides - 2} triángulos y la suma interior es {total}°; la justificación muestra la descomposición, no solo la fórmula."
    elif "construcciones geométricas" in topic.lower() or any(word in topic.lower() for word in ("bisect", "congru")):
        resource = "Hoja sin cuadrícula, segmento AB de 8 cm, triángulo escaleno, regla sin graduación, compás y escuadra."
        prompt = f"Para «{focus.lower()}», realiza la construcción dejando arcos auxiliares, rotula cada elemento y escribe dos comprobaciones de la propiedad."
        reference = "Conserva los trazos, nombra el punto o recta y verifica con equidistancia, perpendicularidad, congruencia o intersección según el foco."
    elif "área" in lowered or "trapecio" in lowered or "paralelogramo" in lowered:
        base, height = 6 + seed % 5, 3 + seed % 4
        resource = f"Paralelogramo, triángulo y trapecio recortables sobre cuadrícula; base {base} cm y altura perpendicular {height} cm."
        prompt = "Transforma o duplica las figuras para derivar sus fórmulas, calcula el área y señala por qué un lado inclinado no reemplaza la altura."
        reference = f"Usa base×altura para el paralelogramo ({base*height} cm²) y la mitad para el triángulo ({base*height/2:g} cm²), con derivación visible."
    elif any(word in lowered for word in ("cartesiano", "vector", "coorden")):
        resource = "Plano cartesiano de −8 a 8; puntos A(−3,2), B(2,−1) y vectores u=(4,−2), v=(−1,3)."
        prompt = "Ubica A y B, trasládalos con u, representa v desde dos orígenes y explica por qué el vector conserva componentes."
        reference = "A+u=(1,0) y B+u=(6,−3); las flechas de v tienen igual dirección, sentido y magnitud: −1 en x y +3 en y."
    elif "probabilidad" in lowered or "evento" in lowered or "experimento" in lowered:
        resource = "Dos monedas distinguibles, diagrama de árbol incompleto y registros simulados de 20, 100 y 500 lanzamientos para «exactamente una cara»."
        prompt = f"Para «{focus.lower()}», completa el espacio muestral, calcula la probabilidad teórica, obtiene frecuencias relativas y explica las diferencias."
        reference = "El espacio es CC, CS, SC, SS; dos de cuatro resultados cumplen el evento, P=1/2. Las frecuencias se estabilizan sin quedar obligadas a 0,5."
    elif any(word in lowered for word in ("muestr", "población", "frecuencia", "gráfico")):
        resource = "Población simulada de 60 fichas (24 azules, 21 verdes, 15 naranjas), tres muestras de 12 obtenidas por métodos distintos y tabla vacía."
        prompt = f"Para «{focus.lower()}», calcula frecuencias absolutas y relativas, compara muestras y explica cuál método permite una estimación defendible y con qué límite."
        reference = "La población tiene 40%, 35% y 25%. Distingue muestra de población, identifica posible sesgo y no presenta una estimación como certeza."
    elif any(word in lowered for word in ("tendencia", "media", "mediana", "moda", "rango", "atípico", "distribucion")):
        resource = "Conjunto A: 4,5,5,6,30; conjunto B: 8,9,10,11,12; tabla para media, mediana, moda y rango."
        prompt = f"Para «{focus.lower()}», calcula las medidas, elige cuál resume mejor cada conjunto y explica el efecto del 30 sin ocultar la dispersión."
        reference = "A: media 10, mediana 5, moda 5, rango 26; B: media y mediana 10, sin moda única, rango 4. Considera el valor atípico."
    else:
        return _math(topic, focus, seed, 6)
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _language_grade_seven(topic: str, focus: str, seed: int) -> dict:
    """Return a small original corpus or tool matched to the seventh-grade OA."""
    lowered = f"{topic} {focus}".lower()
    if any(word in lowered for word in ("medio", "multimodal", "argument", "persuasi", "hecho", "opinión", "postura")):
        resource = ("Dossier original: titular «La plaza necesita más sombra»; dato «12 de 20 bancas reciben sol al mediodía»; "
                    "opinión «es el peor lugar para esperar»; gráfico con escala truncada e imagen tomada desde un solo sector.")
        prompt = f"Para «{focus.lower()}», distingue dato, opinión y recurso visual; formula la postura, evalúa qué evidencia falta y responde a una audiencia concreta."
        reference = "Cita 12/20 como dato, reconoce la valoración como opinión, advierte el encuadre o escala y sostiene una postura sin atribuir intenciones no demostrables."
    elif any(word in lowered for word in ("investig", "fuente", "información", "explicativ", "contextual", "síntesis", "organización de ideas")):
        resource = ("Miniarchivo original sobre bibliotecas comunitarias: fuente A, entrevista ficticia fechada; fuente B, tabla anual simulada; "
                    "fuente C, entrada sin autor ni fecha. Ficha para pregunta, palabras clave, hallazgo, categoría y referencia.")
        prompt = f"Para «{focus.lower()}», delimita una pregunta, selecciona dos fuentes útiles, registra hallazgos sin copiar y explica por qué limitas la tercera."
        reference = "Conecta cada hallazgo con la pregunta, diferencia testimonio y dato simulado, registra procedencia y limita la fuente C por falta de autoría y fecha."
    elif any(word in lowered for word in ("escritura", "escribir", "oración", "sujeto", "predicado", "correferencia", "tiempos verbales", "ortografía", "puntuación", "proceso")):
        resource = ("Texto original para edición: «Ayer la brigada prepara el afiche. La brigada, que tenían dos borradores, lo mostraron: “Falta la fuente” dijo Inés. "
                    "Después el equipo había corregido el afiche y mañana lo presentó». Pauta de propósito, cohesión, gramática y puntuación.")
        prompt = f"Trabaja «{focus.lower()}»: identifica dos decisiones que dificultan la comprensión, corrígelas sin borrar la voz del texto y justifica cada cambio."
        reference = "Mantiene una secuencia verbal coherente, concuerda sujeto y verbo, aclara referentes y usa puntuación con función explicable; no reescribe todo por gusto."
    elif (re.search(r"(?<!\w)oral(?:es)?(?!\w)", lowered) is not None
          or any(word in lowered for word in ("diálogo", "audiencia", "exposición", "registro"))):
        resource = ("Guion original de 75 palabras para una exposición escolar, una réplica respetuosa y tres tarjetas de audiencia: curso, consejo escolar y audio público. "
                    "Pauta de foco, evidencia, turno, volumen, velocidad y dicción.")
        prompt = f"Para «{focus.lower()}», adapta el mensaje, incorpora un dato verificable, responde a una objeción sin descalificar y explica un ajuste de voz o registro."
        reference = "Conserva la idea central, reformula la objeción antes de responder, usa evidencia y ajusta el registro por propósito, no por imitar un acento."
    elif any(word in lowered for word in ("poema", "poesía", "romance", "lírico", "ritmo", "sonoridad")):
        resource = ("Poema original: «La lluvia escribe despacio / sobre el techo de la estación; / cada gota guarda un paso / que regresa en la canción». "
                    "Versión B cambia «despacio» por «de golpe» y elimina la repetición sonora.")
        prompt = f"Para «{focus.lower()}», marca una imagen y un recurso sonoro, interpreta su efecto y compara cómo cambia la versión B al leer ambas en voz alta."
        reference = "Relaciona lluvia/escritura o gota/paso con una imagen, comenta ritmo o repetición y explica un cambio de efecto; nombrar una figura sin interpretarla no basta."
    elif any(word in lowered for word in ("mito", "mitológico", "herencia", "contexto", "experiencia humana", "interpretación")):
        resource = ("Relato original de análisis, no mito tradicional: una comunidad conserva una lámpara que solo enciende cuando alguien reconoce un error; "
                    "dos personajes discrepan entre ocultar una falla o detener el viaje. Ficha separada de contexto y procedencia.")
        prompt = f"Para «{focus.lower()}», analiza el dilema con dos pasajes, distingue el relato didáctico de una tradición cultural y formula una interpretación revisable."
        reference = "Explica las opciones y consecuencias con evidencia, no presenta el texto como patrimonio tradicional y separa experiencia personal opcional de argumento textual."
    elif any(word in lowered for word in ("narración", "narraciones", "conflicto", "personaje", "narrador", "temporal")):
        resource = ("Microrelato original: «Cuando Mara abrió el taller, la ventana ya estaba reparada. ‘No fui yo’, dijo Tomás. Horas antes, él había guardado una nota sin leer. "
                    "Mara la encontró al cerrar: alguien pedía proteger los planos antes de la lluvia». Tarjetas narrador/personajes/tiempo.")
        prompt = f"Para «{focus.lower()}», ordena los hechos, identifica quién enuncia cada frase y explica con dos evidencias cómo una acción modifica el conflicto."
        reference = "Distingue narrador y diálogo, ubica la nota antes de la apertura y conecta guardarla/no leerla con el conflicto; un resumen sin efecto causal es insuficiente."
    elif any(word in lowered for word in ("comprensión", "estrategia", "trayectoria", "lectora", "selección")):
        resource = "Menú de seis textos originales o de libre uso con título, género, extensión, tema y primera página; bitácora con propósito, elección, expectativa, dificultad y decisión."
        prompt = f"Para «{focus.lower()}», define un propósito, examina tres opciones, elige una con dos criterios y registra qué estrategia usarás si la comprensión se interrumpe."
        reference = "Relaciona propósito con rasgos observables, no solo extensión; admite abandonar con razón y propone una estrategia según la dificultad concreta."
    elif "creativa" in lowered or "autor" in lowered:
        resource = "Banco original de detonantes: una puerta que solo abre al formular una pregunta, una carta que llega diez años tarde y un objeto que narra; tarjetas de género, voz y destinatario."
        prompt = f"Para «{focus.lower()}», combina un detonante con género y destinatario, escribe una escena con una decisión de voz y revisa el aspecto que más afecta su efecto."
        reference = "Desarrolla un núcleo reconocible, toma una decisión de género y voz y mejora tras retroalimentación; no necesita parecerse al modelo ni revelar vivencias."
    else:
        return _language(topic, focus, seed)
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _language(topic: str, focus: str, seed: int) -> dict:
    names = ("Amaya", "Benjamín", "Camila", "Diego", "Elena", "Fabián")
    name = names[seed % len(names)]
    object_name = ("cuaderno", "semillero", "mapa", "afiche", "grabación", "maqueta")[seed % 6]
    microtext = (f"{name} encontró un {object_name} sin firma junto a la biblioteca. Antes de usarlo, preguntó quién lo había creado, "
                 "comparó dos pistas y dejó una nota para devolverlo. Al final descubrió que la primera explicación no bastaba.")
    return {
        "resource": f"Microtexto original del proyecto: «{microtext}»",
        "prompt": f"Trabaja el foco «{focus.lower()}»: marca dos evidencias del microtexto, formula una interpretación o producción y revisa una decisión para su audiencia.",
        "reference": "Una respuesta lograda cita o parafrasea dos pistas distintas, conecta ambas con su interpretación y explica una revisión; un resumen sin inferencia no basta.",
    }


def _science(topic: str, focus: str, seed: int) -> dict:
    start = 2 + seed % 5
    values_a = [start, start + 2, start + 5, start + 7]
    values_b = [start, start + 1, start + 2, start + 3]
    return {
        "resource": (f"Registro de indagación para «{topic}»: tiempos 0, 5, 10 y 15 min; condición A={values_a}; "
                     f"condición B={values_b}. La fuente se rotula como conjunto didáctico simulado, no como medición real."),
        "prompt": f"Para «{focus.lower()}», identifica variable independiente, variable observada y dos constantes; compara A y B usando valores y escribe una limitación del registro.",
        "reference": "Debe nombrar qué cambia entre A y B, citar al menos dos pares de valores, mantener dos condiciones constantes y no presentar el patrón como prueba causal definitiva.",
    }


def _history(topic: str, focus: str, seed: int) -> dict:
    lowered = topic.lower()
    if any(word in lowered for word in ("derecho", "ciudad", "democr", "particip", "conviv")):
        resource = ("Caso cívico ficticio: un consejo debe decidir entre publicar de inmediato una medida o abrir una consulta accesible de dos días. "
                    "Tarjetas de actores: autoridad, dos organizaciones vecinales y una persona que requiere apoyo de acceso.")
        prompt = f"Para «{focus.lower()}», identifica derecho, responsabilidad y dos perspectivas; propone una decisión, su resguardo y una forma pública de rendir cuenta."
        reference = "La respuesta distingue derecho e interés, incorpora al menos dos perspectivas, propone un mecanismo realizable y explica cómo evita excluir o exponer a una persona."
    elif any(word in lowered for word in ("territ", "región", "paisaje", "clima", "ambiente", "mapa", "geograf")):
        resource = ("Mapa didáctico esquemático con norte, escala y tres zonas A, B y C; tabla asociada: distancia al agua 2/8/15 km, "
                    "pendiente baja/media/alta y población 40/25/10. Datos simulados para aprender a argumentar, no para describir un lugar real.")
        prompt = f"Aplica «{focus.lower()}»: compara dos zonas con tres datos, formula una decisión territorial y señala qué información falta antes de aplicarla a un lugar real."
        reference = "La respuesta cita al menos tres valores o rasgos, relaciona ubicación y decisión y declara una limitación; no convierte el mapa simulado en información de Chile."
    else:
        resource = (f"Dos tarjetas de interpretación creadas para la clase sobre «{topic}», no fuentes primarias: A afirma que un proceso tiene una sola causa y ocurre igual en todos los territorios; "
                    "B propone contrastar antecedentes, actores, ritmos y lugares. Matriz con columnas afirmación, evidencia necesaria, perspectiva y límite.")
        prompt = f"Aplica «{focus.lower()}»: compara A y B, identifica dos supuestos y escribe qué fuentes verificables necesitarías antes de sostener una conclusión histórica."
        reference = "La respuesta reconoce que ambas tarjetas son interpretaciones didácticas, cuestiona la causa única, pide al menos dos fuentes identificables y limita la conclusión hasta revisarlas."
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _english(topic: str, focus: str, seed: int) -> dict:
    place = ("library", "school garden", "sports court", "community centre")[seed % 4]
    dialogue = f"A: What do we need for the {place}? B: We need a clear plan. A: I can bring the list. B: Great. Let's check it together."
    return {
        "resource": f"Original classroom dialogue: “{dialogue}”",
        "prompt": f"Use the dialogue to work on “{focus.lower()}”. Underline two useful chunks, change one detail and perform or write a new exchange that keeps the meaning clear.",
        "reference": "A successful response reuses two meaningful chunks, changes the place or contribution coherently and remains understandable; accent imitation is not required.",
    }


def _arts(topic: str, focus: str, seed: int) -> dict:
    constraints = (("two colours", "repeated line", "paper texture"), ("warm/cool contrast", "one geometric form", "reused cardboard"), ("foreground/background", "three values", "collage"))[seed % 3]
    return {
        "resource": f"Brief de creación: comunicar «{topic}» usando {constraints[0]}, {constraints[1]} y {constraints[2]}; hoja de pruebas y ficha de autoría.",
        "prompt": f"Realiza dos pruebas pequeñas para «{focus.lower()}», elige una con un criterio visible, desarrolla la obra y anota una decisión que cambió durante el proceso.",
        "reference": "La evidencia incluye dos pruebas distintas, una elección justificada, una producción propia y una explicación basada en elementos visuales, no solo en gusto o parecido.",
    }


def _music(topic: str, focus: str, seed: int) -> dict:
    pattern = ("TA – ti-ti – TA – silencio", "ti-ti – TA – ti-ti – TA", "TA – TA – ti-ti – silencio")[seed % 3]
    return {
        "resource": f"Patrón musical de trabajo: {pattern}; pulso estable marcado con palmas y dos versiones de dinámica. No requiere reproducir repertorio protegido.",
        "prompt": f"Escucha o interpreta el patrón para «{focus.lower()}», describe dos rasgos audibles, modifica uno y explica cómo cambia el resultado.",
        "reference": "La respuesta mantiene el pulso, identifica ritmo/dinámica con evidencia audible y explica el efecto de una modificación; decir solo “me gusta” no es suficiente.",
    }


def _physical(topic: str, focus: str, seed: int) -> dict:
    seconds = 20 + (seed % 4) * 10
    return {
        "resource": f"Estación delimitada de 4 × 4 m, cuatro conos y cronómetro: {seconds} s de acción, {seconds} s de pausa, tres intentos; variante sin desplazamiento disponible.",
        "prompt": f"Practica «{focus.lower()}» priorizando control, distancia segura y autorregulación; registra una decisión técnica y una señal corporal antes y después.",
        "reference": "Se considera logrado cuando mantiene control y seguridad en dos intentos, ajusta intensidad a una señal corporal y explica una decisión; velocidad sola no acredita logro.",
    }


def _orientation(topic: str, focus: str, seed: int) -> dict:
    cases = (
        "Alex recibe un mensaje que le incomoda y no sabe si pedir ayuda",
        "Sam queda fuera de una decisión grupal y necesita proponer una salida respetuosa",
        "Noa asumió demasiadas tareas y debe renegociar un acuerdo sin culpar a otra persona",
    )
    case = cases[seed % len(cases)]
    return {
        "resource": f"Caso ficticio protegido: {case}. Tarjetas de opciones: detenerse, expresar un límite, buscar apoyo, acordar seguimiento.",
        "prompt": f"Analiza el caso desde «{focus.lower()}»: separa hechos de suposiciones, compara dos opciones y escribe una acción segura y una persona o institución de apoyo.",
        "reference": "La respuesta no exige experiencias personales, distingue hecho/emoción/suposición, anticipa una consecuencia y propone apoyo seguro sin secreto ni culpabilización.",
    }


def _technology(topic: str, focus: str, seed: int) -> dict:
    load = 5 + seed % 8
    return {
        "resource": f"Desafío de diseño: construir con cartón reutilizado, papel y cinta una solución estable para sostener {load} fichas; límite de base 20 × 20 cm y tres pruebas registradas.",
        "prompt": f"Para «{focus.lower()}», define usuario y dos criterios, dibuja con medidas, construye o simula, registra tres pruebas y modifica una sola variable.",
        "reference": f"La solución lograda declara usuario, cumple la base máxima, soporta {load} fichas, registra tres resultados y justifica una mejora con evidencia, no solo por apariencia.",
    }


def _cultural(topic: str, focus: str, seed: int) -> dict:
    return {
        "resource": (f"Ficha situada para «{topic}»: pueblo y territorio, nombre de la fuente comunitaria, persona o institución responsable, fecha, autorización, "
                     "variante lingüística cuando corresponda y límites de circulación. Si esos datos faltan, la actividad se detiene."),
        "prompt": f"Trabaja «{focus.lower()}» únicamente con una fuente autorizada: registra procedencia, distingue lo que la fuente dice de tu interpretación y prepara una devolución respetuosa.",
        "reference": "La respuesta atribuye pueblo, territorio y fuente, no inventa lengua ni generaliza a otros pueblos y declara qué requiere validación de educador tradicional o comunidad.",
    }


def _science_grade_seven(topic: str, focus: str, seed: int) -> dict:
    lowered = topic.lower()
    if "sexualidad" in lowered:
        resource = "Cuatro casos ficticios y no autobiográficos sobre cambios puberales, afectividad, respeto, consentimiento y responsabilidad; buzón anónimo y protocolo escolar visible."
        prompt = f"Para «{focus.lower()}», separa dimensión biológica, afectiva y social, identifica una decisión respetuosa y explica cuándo corresponde acudir a una fuente o persona adulta confiable."
        reference = "Integra las tres dimensiones, evita estereotipos y exposición personal, y propone cuidado, respeto y apoyo sin diagnosticar ni moralizar."
    elif "formación de un nuevo individuo" in lowered:
        resource = "Calendario didáctico ficticio, tarjetas de ovulación, fecundación, implantación, embrión y feto, y modelo secuencial que declara variación individual."
        prompt = f"Trabaja «{focus.lower()}»: ordena procesos, conecta cada etapa con el lugar donde ocurre y marca qué parte del modelo expresa posibilidad y no certeza."
        reference = "Distingue ovulación, fecundación e implantación, ordena desarrollo inicial y declara que un calendario didáctico no predice con certeza un ciclo individual."
    elif "infecciones de transmisión" in lowered:
        resource = "Fichas sanitarias didácticas con agente, vías de transmisión, posibles manifestaciones, prevención, consulta y tratamiento; todas remiten a fuentes sanitarias vigentes y evitan perfiles personales."
        prompt = f"Para «{focus.lower()}», compara dos fichas, distingue transmisión de convivencia cotidiana, corrige un mito y redacta una recomendación prudente que no prometa protección absoluta."
        reference = "Usa la ficha como evidencia, reconoce que puede no haber manifestaciones visibles, evita estigma y deriva decisiones personales a atención sanitaria competente."
    elif "barreras defensivas" in lowered:
        resource = "Tablero por capas con piel y mucosas, inflamación y fagocitos, linfocitos, anticuerpos y memoria; tarjetas de un patógeno ficticio para seguir la respuesta."
        prompt = f"Modela «{focus.lower()}»: ubica la barrera que actúa, explica qué desencadena la siguiente y señala una simplificación del tablero."
        reference = "Relaciona barreras primarias, respuesta innata y adaptativa, incorpora memoria cuando corresponde y no presenta las capas como muros independientes."
    elif "virus, bacterias" in lowered:
        resource = "Micrografías atribuidas y modelos a escalas declaradamente distintas de virus, bacteria y hongo; matriz de estructura, reproducción, ambiente y efectos."
        prompt = f"Para «{focus.lower()}», compara los tres grupos con dos criterios, advierte la diferencia de escala y escribe una semejanza que no los convierta en equivalentes."
        reference = "Distingue estructura y dependencia reproductiva, reconoce efectos beneficiosos y perjudiciales y no clasifica un virus como bacteria pequeña."
    elif "biotecnología" in lowered:
        resource = "Cuatro diagramas de proceso: fermentación alimentaria, compostaje, biorremediación y producción biotecnológica; cada uno identifica microorganismo, condición, producto y control."
        prompt = f"Analiza «{focus.lower()}»: elige un proceso, explica el papel del microorganismo, identifica una condición que debe controlarse y evalúa un beneficio y un riesgo."
        reference = "Conecta organismo, condición y producto, diferencia uso controlado de contaminación y no reduce biotecnología a modificación genética."
    elif "fuerzas" in lowered:
        resource = "Dinamómetro escolar, bloque, tres superficies, bandas elásticas y masas seguras; tabla para fuerza aplicada, distancia, deformación y variables controladas."
        prompt = f"Investiga «{focus.lower()}»: cambia una sola condición, registra tres mediciones, representa el patrón y explica si observa gravedad, roce o elasticidad."
        reference = "Nombra variable y controles, registra unidades y repeticiones, distingue las fuerzas y limita la conclusión al rango medido."
    elif "presión" in lowered:
        resource = "Bloques con caras de distinta área, jeringas sin aguja y esquema de recipiente con salidas a varias profundidades; no se usan recipientes presurizados ni calor."
        prompt = f"Para «{focus.lower()}», predice y compara dos configuraciones, relaciona fuerza, área o profundidad y explica el resultado con un modelo de partículas cuando corresponda."
        reference = "Distingue presión de fuerza total, explica el efecto de área o profundidad y mantiene la experiencia dentro de condiciones seguras."
    elif "tectónica" in lowered:
        resource = "Mapas transparentes de placas, sismos y volcanes; perfiles de límites convergente, divergente y transformante, y ampliación Nazca-Sudamericana."
        prompt = f"Para «{focus.lower()}», superpone mapas, identifica un patrón, relaciona un límite con actividad geológica y explica el caso chileno sin generalizar todos los sismos."
        reference = "Usa ubicación y tipo de límite como evidencia, distingue placa de continente y presenta el modelo como explicación con alcance definido."
    elif "volcánica" in lowered:
        resource = "Corte esquemático de volcán, datos didácticos de viscosidad y gases, y mapa ficticio de amenaza con rutas y zonas seguras basado en simbología oficial."
        prompt = f"Analiza «{focus.lower()}»: relaciona dos propiedades con el estilo eruptivo, distingue peligro y riesgo y justifica una decisión usando el mapa, no una improvisación."
        reference = "Distingue magma, lava, gases y ceniza, conecta propiedades con comportamiento y usa ruta y zona segura sin prometer ausencia de riesgo."
    elif "rocas" in lowered:
        resource = "Muestras o fotografías de rocas ígneas, sedimentarias y metamórficas, tarjetas de procesos y tablero circular sin punto inicial obligatorio."
        prompt = f"Construye «{focus.lower()}»: identifica rasgos, conecta cada transformación con un proceso y explica dos rutas posibles entre tipos de roca."
        reference = "Relaciona enfriamiento, sedimentación o metamorfismo con evidencias, distingue roca de mineral y evita un ciclo lineal único."
    elif "clima" in lowered:
        resource = "Mapas de radiación, temperatura, corrientes, relieve y altitud, más series ficticias de dos localidades chilenas a igual latitud y distinta cercanía al mar."
        prompt = f"Explica «{focus.lower()}»: cruza dos representaciones, identifica al menos dos factores y distingue patrón climático de un episodio meteorológico."
        reference = "Construye una explicación multicausal, separa tiempo y clima y no atribuye estaciones a la distancia de la Tierra al Sol."
    elif "gases" in lowered:
        resource = "Jeringas sin aguja, globos y diagramas de partículas para comparar presión, volumen y temperatura; cualquier cambio térmico usa solo agua templada y fría."
        prompt = f"Investiga «{focus.lower()}»: modifica una variable, registra el efecto, representa partículas antes y después y señala qué condición permaneció estable."
        reference = "Relaciona presión, volumen o temperatura sin agrandar partículas, declara controles y evita calentar recipientes cerrados."
    elif "sustancias puras" in lowered:
        resource = "Sal, arena, agua, aceite y limaduras encapsuladas; tamiz, filtro e imán protegido, más diagramas de evaporación para analizar sin calentar."
        prompt = f"Resuelve «{focus.lower()}»: clasifica con un criterio, elige una propiedad para separar, ordena el procedimiento y anticipa pérdidas o límites."
        reference = "Distingue sustancia y mezcla, homogénea y heterogénea, y justifica filtración, tamizado, imantación, decantación o evaporación por una propiedad."
    else:
        resource = "Secuencias de derretimiento, disolución, oxidación y reacción segura registrada previamente; tabla de estado inicial, evidencia, producto y reversibilidad."
        prompt = f"Para «{focus.lower()}», compara dos cambios, identifica evidencia pertinente y argumenta si se formó una sustancia nueva sin usar la reversibilidad como único criterio."
        reference = "Separa cambio de estado, disolución y reacción, usa varias evidencias y reconoce cuando el registro no basta para asegurar un cambio químico."
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _history_grade_seven(topic: str, focus: str, seed: int) -> dict:
    lowered = topic.lower()
    if any(word in lowered for word in ("hominización", "agrícola", "estados tempranos", "primeras civilizaciones")):
        source_set = "mapa y cronología a escala, registro arqueológico A con fecha y lugar, y reconstrucción B claramente rotulada como interpretación"
    elif any(word in lowered for word in ("aten", "roma", "mediterráneo", "antigüedad", "clásic")):
        source_set = "mapa mediterráneo, texto traducido con autor y contexto, esquema institucional y objeto o edificio con ficha de procedencia"
    elif any(word in lowered for word in ("medieval", "europa", "bizancio", "islam", "siglo xii")):
        source_set = "mapa europeo-mediterráneo, cronología, fuente traducida de dos procedencias y registro material o urbano con contexto"
    elif any(word in lowered for word in ("maya", "azteca", "inca", "tawantinsuyu", "américa latina", "legados")):
        source_set = "mapa temporal, fuente material, texto contextualizado y voz historiográfica actual que distingue pueblos, territorios y momentos"
    elif any(word in lowered for word in ("ciudadan", "democracia", "poder", "diversidad", "convivencia")):
        source_set = "dos casos históricos, una fuente normativa traducida y una situación ciudadana ficticia con actores y derechos explícitos"
    else:
        source_set = "mapa temático, serie breve de datos, fuente institucional y caso comunitario ficticio que permiten comparar escalas y consecuencias"
    resource = f"Dossier para «{topic}»: {source_set}. Matriz de contexto, afirmación, evidencia, perspectiva y límite."
    prompt = f"Para «{focus.lower()}», contextualiza dos piezas, formula una relación temporal, espacial o causal, cita evidencia precisa y escribe qué no permiten concluir las fuentes."
    reference = "La respuesta ubica tiempo y espacio, distingue fuente e interpretación, contrasta perspectivas y limita la conclusión sin jerarquizar culturas ni trasladar conceptos actuales de forma automática."
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _science_grade_eight(topic: str, focus: str, seed: int) -> dict:
    """Return safe, concrete evidence sets for eighth-grade science."""
    lowered = topic.lower()
    if any(word in lowered for word in ("difusión", "osmosis", "plantas", "sistemas", "nutrientes", "saludable")):
        resource = "Caso o experiencia segura con tabla antes/después, diagramas de transporte y sistemas, etiquetas simuladas y fuentes sanitarias sin datos personales."
        prompt = f"Investiga «{focus.lower()}»: identifica una relación o variable, registra evidencia, explica el mecanismo y formula una recomendación prudente sin diagnosticar."
        reference = "Separa dato, mecanismo y decisión, conecta partes del sistema, reconoce variación y contexto y evita clasificar cuerpos, alimentos o personas."
    elif "celular" in lowered or "célula" in lowered:
        resource = "Modelos de célula procarionte, animal y vegetal; micrografías atribuidas; tarjetas de estructura, función, evidencia histórica y escala."
        prompt = f"Para «{focus.lower()}», compara dos modelos, relaciona estructura y función, cita una evidencia y declara qué simplifica la representación."
        reference = "Distingue tipos celulares y escalas, conecta al menos dos estructuras con funciones y presenta el modelo como explicación revisable, no como copia literal."
    elif any(word in lowered for word in ("eléctric", "circuit", "generación")):
        resource = "Pilas de bajo voltaje, LED protegidos, cables e interruptores o diagramas de generación; estaciones de electricidad estática sin conexión a la red domiciliaria."
        prompt = f"Para «{focus.lower()}», representa el sistema, mide o compara dos configuraciones, explica la transformación o interacción y evalúa un riesgo y una medida de control."
        reference = "Distingue carga, corriente, voltaje y energía según corresponda, usa evidencia de bajo voltaje y nunca transfiere el procedimiento a enchufes o instalaciones domiciliarias."
    elif "calor" in lowered or "temperatura" in lowered:
        resource = "Vasos aislados, agua templada y fría, termómetros, materiales conductores y aislantes, tabla tiempo-temperatura y modelo de partículas."
        prompt = f"Para «{focus.lower()}», mide temperaturas, representa transferencia, compara dos materiales y explica el proceso sin tratar calor y temperatura como sinónimos."
        reference = "Describe energía transferida por diferencia de temperatura, distingue conducción, convección o radiación y conecta medición con modelo de partículas."
    else:
        resource = "Modelos históricos de Dalton, Thomson, Rutherford y Bohr; tarjetas de átomos y sustancias; tabla periódica y datos CHON de abundancia con fuente."
        prompt = f"Para «{focus.lower()}», usa el modelo pertinente, relaciona una evidencia o patrón con una predicción y señala una limitación antes de comunicar la explicación."
        reference = "Distingue número y masa atómica, estructura y sustancia, conecta cambios de modelo con evidencia y no presenta representaciones como observación directa."
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _history_grade_eight(topic: str, focus: str, seed: int) -> dict:
    """Return contextualized primary-source sets for eighth-grade social studies."""
    lowered = topic.lower()
    if any(word in lowered for word in ("región", "regional", "conectividad", "desarrollo")):
        source_set = "mapas temáticos a distintas escalas, datos demográficos y productivos, indicadores de desarrollo y dos casos regionales chilenos con fuente y fecha"
    elif any(word in lowered for word in ("derecho", "legitimidad", "ciudadan")):
        source_set = "dos textos normativos o argumentativos contextualizados, una matriz de inclusión y exclusión y un caso ciudadano ficticio actual"
    elif any(word in lowered for word in ("conquista", "colonial", "arauco", "hacienda", "atlántico", "barroco")):
        source_set = "mapa y cronología, fuente indígena o local y fuente europea traducidas, registro material y estudio historiográfico actual que declara sus límites"
    elif any(word in lowered for word in ("ilustración", "revolu", "independencia")):
        source_set = "declaraciones y debates traducidos, cronologías paralelas, mapa atlántico o continental y fuentes que muestran actores y exclusiones"
    else:
        source_set = "obra, mapa, texto traducido y registro institucional de los siglos XV al XVII, cada uno con autoría, fecha, lugar, propósito y contexto"
    resource = f"Dossier para «{topic}»: {source_set}. Matriz de contexto, afirmación, evidencia, perspectiva y límite."
    prompt = f"Para «{focus.lower()}», contextualiza dos piezas, construye una relación temporal, territorial o causal, contrasta perspectivas y limita la conclusión."
    reference = "Ubica tiempo y espacio, cita evidencia precisa, reconoce actores y relaciones de poder y evita anacronismos, explicaciones monocausales y jerarquías culturales."
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _english_grade_seven(topic: str, focus: str, seed: int) -> dict:
    lowered = topic.lower()
    if "listening" in lowered:
        resource = "Original 70-word audio script with two speakers, a clear purpose, sequence connectors and three explicit details; title card and listening grid included."
        prompt = f"Listen for “{focus.lower()}”. First record the gist, then replay for two details and one relationship; point to the word, chunk or sound clue that supports each answer."
        reference = "A successful response separates gist from detail, uses at least two accurate clues and revises a prediction when the recording contradicts it."
    elif any(word in lowered for word in ("oral", "interaction", "speaking")):
        resource = "Information-gap cards for two fictional school projects, clarification stems, key-word planning card and a three-panel paper slide deck."
        prompt = f"Work on “{focus.lower()}”: exchange missing information, ask one clarification question and adapt a short message for a partner or small audience."
        reference = "The message is understandable, responds to the other speaker, uses support without reading a full script and repairs meaning when needed; accent imitation is not required."
    elif "reading" in lowered or "texts" in lowered:
        resource = "Two original 130-word texts on one fictional project—one literary and one functional—with headings, image captions, paragraph numbers and a short essential glossary."
        prompt = f"Read for “{focus.lower()}”: state the purpose or main idea, cite two textual or visual clues and revise one answer after rereading a specific paragraph."
        reference = "The response distinguishes purpose, gist and detail, cites precise clues and coordinates words with layout or image rather than copying an unrelated sentence."
    else:
        resource = "Three fictional writing briefs—inform, express an opinion and narrate—with audience card, planning grid, useful chunks and a checklist for content, organization and language."
        prompt = f"Write for “{focus.lower()}”: choose one brief, plan the message, draft a complete version and revise one content decision before editing language accuracy."
        reference = "The text fits purpose and audience, connects ideas, uses learned language to communicate meaning and shows a substantive revision rather than only surface correction."
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _physical_grade_seven(topic: str, focus: str, seed: int) -> dict:
    lowered = topic.lower()
    if "condición física" in lowered:
        resource = "Circuito con cuatro estaciones regulables, escala de esfuerzo percibido, tarjetas de pausa y alternativas sin desplazamiento; no se publican marcas ni datos corporales."
    elif "entornos" in lowered or "comunitaria" in lowered:
        resource = "Planos y fichas ficticias de gimnasio, patio, plaza y sendero o de actividades comunitarias, con acceso, costo, horario, riesgo, apoyo y mínimo impacto."
    elif "estrategias" in lowered:
        resource = "Juego reducido tres contra tres, tablero magnético, zonas de apoyo y reglas de contacto; pausas breves para observar antes de un segundo intento."
    else:
        resource = "Estaciones sin eliminación con conos, balones blandos e implementos graduados; cada una ofrece tres variantes equivalentes de distancia, ritmo o rol."
    prompt = f"Practica «{focus.lower()}»: elige una variante segura, realiza dos intentos, registra una decisión motriz y ajusta solo una condición según una señal corporal, espacial o reglamentaria."
    reference = "Mantiene control y seguridad, participa sin excluir ni comparar cuerpos, explica el ajuste desde evidencia propia y detiene la práctica ante una señal de riesgo."
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _arts_grade_seven(topic: str, focus: str, seed: int) -> dict:
    lowered = topic.lower()
    if "digital" in lowered:
        resource = "Storyboard de seis cuadros, dispositivo sin cuentas o simulación en papel, banco de imágenes propias o autorizadas y ficha de consentimiento, crédito y privacidad."
    elif "sustentables" in lowered:
        resource = "Muestrario de cartón, papel, fibras y envases limpios, pigmentos escolares, uniones reversibles y ficha de origen, uso y descarte."
    elif "difusión" in lowered:
        resource = "Planos y recorridos de museo, galería, espacio público y exposición digital, con tarjetas de obra, audiencia, acceso, montaje y cuidado."
    elif "interpretación" in lowered or "lenguaje visual" in lowered:
        resource = "Dossier de cuatro manifestaciones atribuidas con autoría, fecha, lugar, medio y contexto; lupa de color, forma, composición, material y propósito."
    else:
        resource = "Referentes visuales atribuidos, bitácora de observación y mesa de pruebas con papel, lápices, pintura escolar y materiales reutilizables limpios."
    prompt = f"Para «{focus.lower()}», realiza dos pruebas distintas, elige una según intención y contexto, desarrolla una respuesta propia y documenta una revisión sin copiar el referente."
    reference = "La evidencia incluye exploración, elección justificada y autoría propia; relaciona lenguaje visual con efecto y cuida procedencia, seguridad y privacidad cuando corresponde."
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _music_grade_seven(topic: str, focus: str, seed: int) -> dict:
    lowered = topic.lower()
    if "sociedad" in lowered or "context" in lowered:
        resource = "Dos registros musicales autorizados con intérprete, fecha, lugar y contexto, más una ficha que distingue experiencia, circulación y función social."
    elif "creaci" in lowered or "improvisa" in lowered:
        resource = "Células rítmicas y melódicas, instrumentos disponibles o aplicación sin cuenta, partitura gráfica y tarjeta de límites para una creación breve."
    elif "fortalezas" in lowered or "crecimiento" in lowered:
        resource = "Dos registros de ensayo ficticios, pauta de autoescucha y criterios de pulso, afinación, fraseo, dinámica, coordinación y expresividad."
    else:
        resource = "Dos fragmentos autorizados, partitura convencional o gráfica, mapa de escucha e instrumentos o voz a volumen seguro."
    prompt = f"Para «{focus.lower()}», escucha primero, ubica un rasgo audible, realiza o compara dos versiones y justifica un ajuste con el instante exacto donde se oye."
    reference = "La evidencia relaciona una decisión musical con un efecto audible, reconoce contexto y aportes individuales, y no confunde calidad con volumen, velocidad o gusto personal."
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _orientation_grade_seven(topic: str, focus: str, seed: int) -> dict:
    lowered = topic.lower()
    if any(word in lowered for word in ("sexualidad", "riesgo", "protección")):
        resource = "Caso ficticio en tercera persona, tarjetas de derechos y consentimiento, semáforo de riesgo y ruta institucional de ayuda; no solicita experiencias personales."
    elif any(word in lowered for word in ("virtual", "redes", "relaciones")):
        resource = "Conversación digital ficticia sin cuentas ni datos reales, tarjetas de privacidad, consentimiento, límite, reparación y búsqueda de apoyo."
    elif any(word in lowered for word in ("particip", "acuerdos", "colabor")):
        resource = "Acta ficticia de curso, tres propuestas, mapa de actores y plantilla de acuerdo con conducta observable, responsable, plazo y revisión."
    elif any(word in lowered for word in ("aprendizaje", "metas", "proyecto")):
        resource = "Perfil ficticio de estudiante, evidencia de avance, obstáculos modificables y plan de meta progresiva sin calificaciones ni diagnósticos personales."
    else:
        resource = "Caso ficticio protegido, tarjetas de hechos, emociones posibles, derechos, opciones, consecuencias y redes de apoyo escolar."
    prompt = f"Analiza «{focus.lower()}» sólo desde el caso: distingue hechos, derechos y límites, compara dos opciones y elige una respuesta segura con una ruta de apoyo."
    reference = "La respuesta protege dignidad y privacidad, evita moralizar o diagnosticar, anticipa consecuencias y recurre a ayuda competente cuando la acción individual no basta."
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _technology_grade_seven(topic: str, focus: str, seed: int) -> dict:
    lowered = topic.lower()
    if "comunic" in lowered or "tic" in lowered:
        resource = "Boceto, diagrama de proceso, tabla de prueba y plantilla de presentación sin cuentas, con campos obligatorios de autoría, privacidad y audiencia."
    elif "efectos" in lowered or "ambient" in lowered or "social" in lowered:
        resource = "Dos soluciones existentes con ficha de ciclo de vida, usuarios, materiales, energía, reparación, residuos y efectos sociales directos e indirectos."
    elif "contraste" in lowered or "soluciones" in lowered:
        resource = "Tres soluciones a una necesidad común, matriz de contexto, usuario, función, costo, acceso, mantenimiento e impacto."
    else:
        resource = "Desafío ficticio de reparación, adaptación o mejora, materiales seguros, croquis, matriz de criterios y protocolo de prueba de una variable."
    prompt = f"Resuelve «{focus.lower()}»: define necesidad y usuario, representa antes de construir, prueba un criterio y revisa función, seguridad, eficiencia e impacto."
    reference = "La propuesta responde a evidencia de necesidad, declara criterios y restricciones, registra una prueba reproducible y mejora sin ocultar fallas ni impactos desplazados."
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _cultural_grade_seven(topic: str, focus: str, seed: int) -> dict:
    resource = f"Dossier situado para «{topic}» con pueblo, territorio, responsable, autorización y condiciones de circulación; alternativa oral, visual o escrita validada por fuente comunitaria."
    prompt = f"Para «{focus.lower()}», distingue lo dicho por la fuente de tu interpretación, produce una respuesta atribuida y declara qué no corresponde inventar, divulgar o generalizar."
    reference = "La evidencia atribuye pueblo, territorio y fuente; no inventa lengua ni símbolos, no suplanta saberes comunitarios y requiere educador tradicional o validación pertinente cuando corresponde."
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _math_grade_eight(topic: str, focus: str, seed: int) -> dict:
    """Return concrete artefacts for concepts introduced or deepened in eighth grade."""
    lowered = f"{topic} {focus}".lower()
    if "raíz" in lowered or "pitágoras" in lowered:
        resource = "Cuadrados de áreas 9, 16, 20 y 25 unidades, triángulo 3-4-5 recortable, cuadrícula y recta numérica de 0 a 8."
        prompt = f"Para «{focus.lower()}», relaciona área y longitud, estima √20 entre dos enteros y usa o limita la relación pitagórica con una comprobación visible."
        reference = "√20 está entre 4 y 5 porque 16<20<25; en un triángulo rectángulo 3²+4²=5², y la hipotenusa es el lado opuesto al ángulo recto."
    elif "función" in lowered or "cambio lineal" in lowered or "afín" in lowered:
        resource = "Dos planes ficticios: A(x)=3x y B(x)=3x+5; tabla para x=0,1,2,4 y plano cartesiano con origen visible."
        prompt = f"Para «{focus.lower()}», completa tablas, grafica, interpreta cambio constante y valor inicial, y explica cuál relación es lineal y cuál afín."
        reference = "Ambas cambian 3 por unidad; A pasa por el origen y B tiene intercepto 5. La explicación conecta situación, tabla, regla y gráfica."
    elif any(word in lowered for word in ("prisma", "cilindro", "volumen", "superficie")):
        resource = "Red de prisma rectangular 4×3×6 cm, cilindro de radio 3 cm y altura 6 cm, papel cuadriculado y calculadora opcional."
        prompt = f"Para «{focus.lower()}», deriva superficie o volumen desde la red o las capas, calcula y rotula cm² o cm³; compara con una estimación."
        reference = "El prisma tiene volumen 72 cm³; distingue área de superficie y volumen. Para el cilindro usa πr²h y declara la aproximación de π."
    elif any(word in lowered for word in ("percentil", "cuartil", "caja", "gráfico", "manipul")):
        resource = "Datos ordenados 4,5,6,7,8,9,10,12,18 y dos gráficos equivalentes, uno con eje vertical truncado."
        prompt = f"Para «{focus.lower()}», determina mediana y cuartiles, construye o interpreta una caja y explica cómo la escala cambia la impresión sin cambiar los datos."
        reference = "La mediana es 8; identifica posiciones de Q1 y Q3 según la convención declarada y advierte que truncar el eje exagera diferencias."
    elif any(word in lowered for word in ("combinatorio", "combinación", "evento compuesto")):
        resource = "Tarjetas con 3 rutas, 2 horarios y 4 materiales; tabla de doble entrada y árbol regular incompletos."
        prompt = f"Para «{focus.lower()}», enumera sin repetir, completa dos representaciones y justifica por qué el total se obtiene multiplicando 3×2×4."
        reference = "Hay 24 combinaciones; cada elección de ruta abre 2 horarios y cada par abre 4 materiales. El árbol y la tabla conservan ese producto."
    else:
        return _math_grade_seven(topic, focus, seed)
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _language_grade_eight(topic: str, focus: str, seed: int) -> dict:
    """Return a small original corpus for eighth-grade language work."""
    lowered = f"{topic} {focus}".lower()
    if any(word in lowered for word in ("dramát", "teatral", "comedia", "epopeya")):
        resource = ("Dossier original: escena con diálogo y acotaciones; dos decisiones de puesta en escena; fragmento épico de dominio público "
                    "con procedencia y ficha contextual. No incluye imitaciones culturales sin fuente.")
        prompt = f"Para «{focus.lower()}», distingue texto y representación, analiza una acción o recurso con cita y relaciona su efecto con conflicto, género y contexto."
        reference = "La respuesta cita diálogo o acotación, explica una decisión escénica o rasgo épico y limita su interpretación a la evidencia y contexto disponibles."
    elif any(word in lowered for word in ("modo verbal", "correferencia", "elipsis", "oración compleja")):
        resource = "Párrafo original con referentes competidores, elipsis ambigua y tres versiones verbales: «ocurre», «ocurriría» y «que ocurra»."
        prompt = f"Para «{focus.lower()}», localiza la ambigüedad, prueba dos revisiones y explica cómo referente, sintaxis o modo verbal cambia el efecto."
        reference = "La revisión conserva un referente inequívoco y coherencia temporal; distingue certeza, posibilidad o exhortación sin asignar un significado mecánico."
    else:
        return _language_grade_seven(topic, focus, seed)
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _generic(topic: str, focus: str, seed: int) -> dict:
    options = ("A", "B", "C")
    return {
        "resource": f"Caso didáctico sobre «{topic}» con tres opciones ({', '.join(options)}), una restricción visible y una tabla para registrar decisión, evidencia y revisión.",
        "prompt": f"Resuelve «{focus.lower()}»: elige una opción, cita dos evidencias, explica por qué descartas otra y revisa tu decisión al cambiar una condición.",
        "reference": "La respuesta lograda hace una elección reproducible, usa dos evidencias y modifica la conclusión cuando cambia la condición; participar sin justificar no basta.",
    }


def _artifact(subject_slug: str, topic: str, focus: str, seed: int, grade: int) -> dict:
    if subject_slug == "matematica":
        if grade == 7:
            return _math_grade_seven(topic, focus, seed)
        if grade == 8:
            return _math_grade_eight(topic, focus, seed)
        return _math(topic, focus, seed, grade)
    if subject_slug == "lengua-literatura":
        if grade == 8:
            return _language_grade_eight(topic, focus, seed)
        return _language_grade_seven(topic, focus, seed)
    if subject_slug == "lenguaje-comunicacion":
        return _language(topic, focus, seed)
    if subject_slug == "ciencias-naturales":
        if grade == 7:
            return _science_grade_seven(topic, focus, seed)
        if grade == 8:
            return _science_grade_eight(topic, focus, seed)
        return _science(topic, focus, seed)
    if subject_slug == "historia-geografia-ciencias-sociales":
        if grade == 7:
            return _history_grade_seven(topic, focus, seed)
        if grade == 8:
            return _history_grade_eight(topic, focus, seed)
        return _history(topic, focus, seed)
    if subject_slug in {"ingles", "ingles-propuesta"}:
        if grade in {7, 8}:
            return _english_grade_seven(topic, focus, seed)
        return _english(topic, focus, seed)
    if subject_slug == "artes-visuales":
        if grade in {7, 8}:
            return _arts_grade_seven(topic, focus, seed)
        return _arts(topic, focus, seed)
    if subject_slug == "musica":
        if grade in {7, 8}:
            return _music_grade_seven(topic, focus, seed)
        return _music(topic, focus, seed)
    if subject_slug == "educacion-fisica-salud":
        if grade in {7, 8}:
            return _physical_grade_seven(topic, focus, seed)
        return _physical(topic, focus, seed)
    if subject_slug == "orientacion":
        if grade in {7, 8}:
            return _orientation_grade_seven(topic, focus, seed)
        return _orientation(topic, focus, seed)
    if subject_slug == "tecnologia":
        if grade in {7, 8}:
            return _technology_grade_seven(topic, focus, seed)
        return _technology(topic, focus, seed)
    if subject_slug in {"lengua-cultura-pueblos-originarios-ancestrales", "lengua-indigena"}:
        if grade in {7, 8}:
            return _cultural_grade_seven(topic, focus, seed)
        return _cultural(topic, focus, seed)
    return _generic(topic, focus, seed)


def enrich_item(item: dict) -> dict:
    """Mutate one generated objective with concrete classroom artefacts."""
    sequence = item.get("developed")
    if not sequence:
        return item
    cleaned_sequence = _clean_nested(sequence)
    sequence.clear()
    sequence.update(cleaned_sequence)
    topic = _clean(sequence.get("topic") or item["topic"])
    sequence["topic"] = topic
    lessons = sequence.get("lessons", [])
    for index, lesson in enumerate(lessons, 1):
        for field, value in list(lesson.items()):
            if isinstance(value, str):
                lesson[field] = _clean(value)
        focus = _clean(lesson.get("title") or item["oa_code"])
        artefact = _artifact(item["subject_slug"], topic, focus, _seed(item["oa_code"], index), item["course_order"])
        lesson["concrete_resource"] = artefact["resource"]
        lesson["exact_prompt"] = artefact["prompt"]
        lesson["response_reference"] = artefact["reference"]
        lesson["assessment_levels"] = [
            {"level": level, "descriptor": f"{descriptor} Referencia de esta clase: {artefact['reference']}" if position == 2 else descriptor}
            for position, (level, descriptor) in enumerate(LEVELS)
        ]
        lesson["timing_45"] = [
            {"minutes": 5, "action": "Activación breve y lectura de la consigna exacta."},
            {"minutes": 8, "action": "Modelado con el insumo concreto y una decisión visible."},
            {"minutes": 12, "action": "Primer intento guiado y retroalimentación según un criterio."},
            {"minutes": 15, "action": "Desempeño individual con evidencia atribuible."},
            {"minutes": 5, "action": "Ticket, clasificación del nivel y decisión posterior."},
        ]
        lesson["teacher_checklist"] = [
            "Preparar el insumo concreto sin datos personales ni material sin autorización.",
            "Ensayar la respuesta de referencia y anticipar al menos un error plausible.",
            "Definir cómo recogerá evidencia individual durante el desempeño.",
            "Comprobar accesibilidad, seguridad y alternativa sin conectividad.",
        ]
        if "Recursos reutilizables para" in lesson.get("materials", ""):
            lesson["materials"] = (
                f"Prepare o proyecte este insumo: {artefact['resource']} Añada pizarra, cuaderno y una copia de la consigna; "
                "compruebe legibilidad, seguridad, procedencia y una alternativa sin conectividad."
            )
        generic_criteria = {
            "responde al foco específico de la clase",
            "usa evidencia disciplinar pertinente y contextualizada",
            "explica una decisión y reconoce límites o revisa un error",
        }
        if generic_criteria.intersection(set(lesson.get("criteria", []))) or any(
            "responde al foco específico de la clase" in criterion for criterion in lesson.get("criteria", [])
        ):
            lesson["criteria"] = [
                f"resuelve la consigna exacta de «{focus.lower()}»",
                "usa al menos dos datos, rasgos o evidencias del insumo concreto",
                "explica una decisión y revisa su respuesta ante una condición nueva",
            ]
    return item


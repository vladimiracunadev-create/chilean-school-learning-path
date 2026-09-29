"""Specific fourth-grade Mathematics sequences and transversal integrations."""
from __future__ import annotations


MATH_SKILLS = (
    ("de Habilidad MA04 OAH a", "resolver un problema dado o creado"),
    ("de Habilidad MA04 OAH b", "entender, planificar, resolver y comprobar"),
    ("de Habilidad MA04 OAH c", "transferir un procedimiento a una situación semejante"),
    ("de Habilidad MA04 OAH d", "formular preguntas que profundizan la comprensión"),
    ("de Habilidad MA04 OAH e", "descubrir y comunicar una regularidad"),
    ("de Habilidad MA04 OAH f", "hacer una deducción matemática"),
    ("de Habilidad MA04 OAH g", "comprobar y fundamentar una solución"),
    ("de Habilidad MA04 OAH h", "escuchar otro razonamiento y revisar errores"),
    ("de Habilidad MA04 OAH i", "seleccionar, modificar y evaluar un modelo"),
    ("de Habilidad MA04 OAH j", "traducir una situación a lenguaje matemático"),
    ("de Habilidad MA04 OAH k", "identificar regularidades numéricas o geométricas"),
    ("de Habilidad MA04 OAH l", "usar representaciones y símbolos con precisión"),
    ("de Habilidad MA04 OAH m", "crear un problema desde una expresión o representación"),
    ("de Habilidad MA04 OAH n", "transitar entre representaciones concretas, pictóricas y simbólicas"),
)
MATH_ATTITUDES = (
    ("de Actitud MA04 OAA A", "trabajo ordenado y metódico"),
    ("de Actitud MA04 OAA B", "búsqueda flexible y creativa de soluciones"),
    ("de Actitud MA04 OAA C", "curiosidad por las regularidades matemáticas"),
    ("de Actitud MA04 OAA D", "confianza progresiva en las propias capacidades"),
    ("de Actitud MA04 OAA E", "esfuerzo y perseverancia ante un desafío"),
    ("de Actitud MA04 OAA F", "expresión y escucha respetuosa de ideas"),
)


def _p(topic, prior, vocabulary, anchor, misconception, focuses):
    return {"topic": topic, "prior": prior, "vocabulary": vocabulary, "anchor": anchor,
            "misconception": misconception, "focuses": focuses}


MATH = {
    "MA04 OA 01": _p("Números hasta 10.000 y valor posicional", "números hasta 1.000 y canjes CDU", "unidad, decena, centena, unidad de mil, decena de mil, componer", "tarjetas 3.094, 3.940, 9.304 y 10.000 con tabla posicional", "leer cifras aisladas o ignorar ceros interiores", ["Contar por decenas, centenas y miles", "Leer y escribir números con ceros", "Representar y canjear unidades de mil", "Comparar y ordenar hasta 10.000", "Componer y descomponer por valor posicional"]),
    "MA04 OA 02": _p("Estrategias de cálculo mental", "conteo, dobles y descomposición hasta 1.000", "doble, mitad, descomponer, compensar, hecho relacionado", "cálculos 398+6, 84÷2, 7×8 y 56÷7", "aplicar una estrategia memorizada sin comprobar si conviene", ["Conteo hacia adelante y atrás", "Doblar y dividir por dos", "Descomponer para calcular", "Usar el doble del doble", "Relacionar multiplicaciones y divisiones"]),
    "MA04 OA 03": _p("Adición y sustracción hasta 1.000", "valor posicional, estimación y algoritmos con canje", "sumando, diferencia, estimar, algoritmo, canje, operación inversa", "inventario de 638 libros, 257 préstamos y cuatro nuevas entregas", "alinear cifras de distinto valor o aceptar un resultado no razonable", ["Estrategias personales y descomposición", "Estimar sumas y diferencias", "Sumar hasta cuatro sumandos", "Sustraer con canjes sucesivos", "Resolver y comprobar problemas no rutinarios"]),
    "MA04 OA 04": _p("Propiedades del 0 y del 1", "sentido de multiplicación y división", "elemento neutro, cero, producto, cociente, propiedad", "arreglos vacíos, grupos unitarios y repartos entre uno", "generalizar que dividir por cero funciona como multiplicar por cero", ["Multiplicar por cero con modelos", "Multiplicar por uno sin cambiar cantidad", "Dividir por uno", "Distinguir propiedades y casos imposibles"]),
    "MA04 OA 05": _p("Multiplicación de tres dígitos por uno", "tablas, valor posicional y distributividad", "factor, producto, parcial, distributiva, algoritmo, estimación", "236 cuadernos por 4 cursos representados con bloques y productos parciales", "multiplicar cada cifra sin respetar su valor posicional", ["Modelar productos con material", "Descomponer mediante distributividad", "Estimar antes de multiplicar", "Conectar productos parciales y algoritmo", "Resolver problemas y comprobar"]),
    "MA04 OA 06": _p("División de dos dígitos por uno", "tablas y relación inversa", "dividendo, divisor, cociente, resto, estimar, descomponer", "84 semillas distribuidas en 6 bandejas y agrupadas de 7 en 7", "confundir el cociente con el resto o perder el sentido del reparto", ["Repartir y agrupar con material", "Estimar el cociente", "Descomponer el dividendo", "Conectar algoritmo y multiplicación", "Interpretar cociente y resto en contexto"]),
    "MA04 OA 07": _p("Problemas de dinero y elección de operaciones", "cuatro operaciones y dinero didáctico", "precio, cantidad, total, vuelto, presupuesto, operación", "presupuesto ficticio de una feria con precios y cantidades", "elegir la operación por una palabra clave en vez de la relación", ["Representar datos y pregunta", "Elegir y justificar operaciones", "Resolver problemas de varios pasos", "Crear y verificar un problema monetario"]),
    "MA04 OA 08": _p("Fracciones en todos, conjuntos y rectas", "particiones equitativas y fracciones unitarias", "entero, numerador, denominador, equivalente, comparar, recta", "tiras, cuadrículas de 100 y colecciones con denominadores 2 a 12", "comparar solo denominadores o usar enteros de distinto tamaño", ["Definir el entero y partes iguales", "Representar fracciones de un todo y conjunto", "Ubicar fracciones en la recta", "Construir representaciones equivalentes", "Comparar y ordenar con referentes"]),
    "MA04 OA 09": _p("Adición y sustracción de fracciones homogéneas", "fracciones propias y unidad común", "denominador común, numerador, sumar, restar, unidad", "recetas ficticias y recorridos medidos en octavos o décimos", "sumar también los denominadores o cambiar la unidad durante el cálculo", ["Combinar partes de la misma unidad", "Sumar con material y dibujo", "Restar y hallar una parte faltante", "Resolver y comprobar problemas"]),
    "MA04 OA 10": _p("Fracciones propias y números mixtos", "fracciones como partes y ubicación en la recta", "fracción propia, impropia, número mixto, entero, equivalencia", "tres pizzas de papel divididas en cuartos y recta de 0 a 5", "leer 2 1/4 como 21/4 sin reconocer dos enteros", ["Distinguir fracción propia y cantidad mayor que uno", "Construir números mixtos", "Traducir entre modelos y símbolos", "Resolver situaciones hasta cinco enteros"]),
    "MA04 OA 11": _p("Décimos y centésimos", "fracciones decimales y valor posicional", "decimal, décimo, centésimo, coma decimal, cuadrícula, comparar", "cuadrículas de cien, dinero didáctico y rectas de 0 a 1", "comparar la cantidad de cifras después de la coma como números naturales", ["Construir décimos", "Relacionar centésimos y cuadrícula", "Traducir fracción decimal y número decimal", "Comparar y ordenar hasta centésimos"]),
    "MA04 OA 12": _p("Adición y sustracción de decimales", "décimos, centésimos y valor posicional", "alinear, décimo, centésimo, suma, diferencia, estimación", "medidas y precios ficticios como 2,35 m y $3,70", "alinear los últimos dígitos en lugar de la coma decimal", ["Representar operaciones en tabla posicional", "Sumar décimos y centésimos", "Restar con canje decimal", "Resolver y estimar en contexto"]),
    "MA04 OA 13": _p("Patrones numéricos con una operación", "secuencias y tablas de entrada-salida", "regla, término, entrada, salida, operación, predecir", "tablas que suman 25, duplican o restan 40", "describir resultados sin formular una regla que permita predecir", ["Detectar cambios constantes", "Describir la operación de una tabla", "Predecir y comprobar términos", "Crear y comparar reglas"]),
    "MA04 OA 14": _p("Ecuaciones e inecuaciones de un paso", "igualdad y operaciones inversas", "ecuación, inecuación, incógnita, desigualdad, inversa, comprobar", "□+38=91, 74-△=29 y x+12<40", "tratar el signo igual o desigual como orden de calcular", ["Representar igualdad y desigualdad", "Resolver ecuaciones aditivas", "Resolver inecuaciones en un rango", "Comprobar con relaciones inversas"]),
    "MA04 OA 15": _p("Localización absoluta y relativa", "filas, columnas y puntos de referencia", "coordenada informal, fila, columna, absoluto, relativo, referencia", "mapa simple con cuadrícula alfanumérica y lugares ficticios", "confundir una coordenada estable con indicaciones que dependen del observador", ["Leer coordenadas alfanuméricas", "Ubicar objetos de forma absoluta", "Describir posiciones relativas", "Comparar rutas sin ambigüedad"]),
    "MA04 OA 16": _p("Vistas de cuerpos 3D", "caras y cuerpos geométricos", "vista frontal, lateral, superior, cuerpo, cara, perspectiva", "construcciones de cubos y envases observados desde tres posiciones", "dibujar lo que se sabe del cuerpo en vez de lo visible desde una vista", ["Relacionar cuerpo y vista frontal", "Determinar vistas laterales", "Construir la vista superior", "Identificar un cuerpo desde varias vistas"]),
    "MA04 OA 17": _p("Simetría en figuras 2D", "reflexión y cuadrículas", "simetría, eje, distancia, correspondencia, reflejo", "figuras de papel, cuadrículas y diseños geométricos", "copiar la forma sin conservar distancias perpendiculares al eje", ["Reconocer figuras simétricas", "Comprobar un eje por plegado", "Completar figuras en cuadrícula", "Crear figuras con una o más líneas"]),
    "MA04 OA 18": _p("Transformaciones isométricas", "traslación, reflexión y rotación", "vector informal, giro, centro, eje, congruencia, orientación", "mosaicos en cuadrícula con una figura inicial marcada", "cambiar tamaño o forma al mover la figura", ["Trasladar conservando orientación", "Reflejar respecto de un eje", "Rotar alrededor de un punto", "Componer y describir transformaciones"]),
    "MA04 OA 19": _p("Construcción y comparación de ángulos", "ángulo recto y comparación de aberturas", "grado, transportador, vértice, lado, abertura, estimar", "ángulos de 35°, 90°, 120° y 165° dibujados desde una semirrecta", "leer la escala incorrecta o medir desde el borde del transportador", ["Estimar antes de medir", "Alinear centro y línea base", "Construir un ángulo dado", "Comparar y corregir construcciones"]),
    "MA04 OA 20": _p("Hora en formatos A.M., P.M. y 24 horas", "lectura de relojes y minutos", "A.M., P.M., mediodía, medianoche, formato 24 horas", "horarios ficticios 07:45, 12:00, 16:30 y 23:10", "sumar 12 a horas A.M. o confundir mediodía con medianoche", ["Distinguir A.M. y P.M.", "Traducir a formato 24 horas", "Leer relojes análogos y digitales", "Interpretar horarios cotidianos"]),
    "MA04 OA 21": _p("Conversiones de unidades de tiempo", "duración e intervalos", "segundo, minuto, hora, día, mes, año, convertir", "cronograma de una actividad ficticia y calendario anual", "usar siempre 60 o suponer que todos los meses tienen igual duración", ["Relacionar segundos y minutos", "Relacionar minutos y horas", "Interpretar días y meses", "Resolver conversiones en contexto"]),
    "MA04 OA 22": _p("Longitud en metros y centímetros", "medición con regla y unidades estándar", "metro, centímetro, equivalencia, transformar, estimar, precisión", "cintas de 1 m, reglas y longitudes del aula sin datos personales", "multiplicar o dividir por 100 sin atender la unidad solicitada", ["Elegir metro o centímetro", "Medir con origen correcto", "Transformar metros a centímetros", "Resolver problemas con unidades mixtas"]),
    "MA04 OA 23": _p("Área de cuadrados y rectángulos", "recubrimiento con unidades cuadradas y multiplicación", "área, unidad cuadrada, cm², m², base, altura", "rectángulos en papel cuadriculado y planos ficticios", "confundir área con perímetro o contar líneas en vez de cuadrados", ["Recubrir sin huecos ni traslapes", "Elegir cm² o m²", "Relacionar filas, columnas y producto", "Calcular área de cuadrados y rectángulos", "Construir rectángulos de igual área"]),
    "MA04 OA 24": _p("Volumen con unidades cúbicas", "cuerpos 3D y conteo organizado", "volumen, unidad cúbica, capa, fila, columna, ocupar espacio", "prismas armados con cubos encajables", "contar solo cubos visibles o confundir superficie con volumen", ["Elegir una unidad cúbica", "Construir y comparar cuerpos", "Contar cubos por capas", "Registrar volumen en unidades cúbicas", "Diseñar cuerpos de igual volumen"]),
    "MA04 OA 25": _p("Encuestas y muestras aleatorias", "preguntas, tablas y gráficos", "población, muestra, aleatorio, categoría, frecuencia, comparar", "encuesta ficticia sobre uso de espacios escolares con dos muestras", "generalizar desde una muestra elegida por conveniencia", ["Formular pregunta y categorías", "Distinguir población y muestra", "Seleccionar una muestra aleatoria", "Tabular y graficar datos", "Comparar resultados y límites"]),
    "MA04 OA 26": _p("Experimentos aleatorios y representación", "registro de resultados y frecuencia", "azar, resultado, ensayo, frecuencia, tabla, gráfico", "lanzamientos de monedas, dados y ruletas equilibradas", "creer que una racha determina el resultado siguiente", ["Definir resultados posibles", "Registrar ensayos sin omisiones", "Construir tabla y gráfico", "Comparar frecuencias sin asegurar el futuro"]),
    "MA04 OA 27": _p("Lectura crítica de pictogramas y barras", "gráficos con escala", "escala, eje, categoría, frecuencia, diferencia, conclusión", "dos gráficos del mismo conjunto con escalas y diseños diferentes", "contar dibujos o cuadrículas sin aplicar la escala", ["Leer título, ejes y escala", "Extraer valores exactos", "Comparar categorías y diferencias", "Comunicar conclusiones con evidencia", "Detectar representaciones engañosas"]),
}


def _links(code: str, index: int, goal: str) -> list[dict[str, str]]:
    number = int(code.split(" OA ")[1])
    skill_code, skill = MATH_SKILLS[(number * 3 + index) % len(MATH_SKILLS)]
    attitude_code, attitude = MATH_ATTITUDES[(number + index * 2) % len(MATH_ATTITUDES)]
    return [
        {"code": skill_code, "type": "Habilidad", "application": f"Se observa al {skill} mientras se alcanza la meta «{goal}»."},
        {"code": attitude_code, "type": "Actitud", "application": f"Se promueve {attitude}; se valora explicar, comprobar y revisar, no la rapidez."},
    ]


def _lesson(code: str, index: int, profile: dict) -> dict:
    focus = profile["focuses"][index]
    topic, anchor, misconception = profile["topic"], profile["anchor"], profile["misconception"]
    goal = f"resolveré y explicaré {focus.lower()}"
    mode = ("diagnosticar", "representar", "comparar", "analizar un error", "aplicar")[index % 5]
    return {
        "title": focus,
        "purpose": f"Desarrollar {topic.lower()} mediante {focus.lower()}, con modelado matemático, práctica y comprobación.",
        "goal": f"Hoy {goal}.",
        "opening": f"Presenta {anchor} y una decisión sobre «{focus.lower()}». Cada estudiante anticipa una respuesta y registra qué dato o representación permitiría comprobarla.",
        "model": f"Modela cómo {mode} «{focus.lower()}»: identifica datos y pregunta, elige una representación, ejecuta una estrategia y comprueba en el contexto. Contrasta con este error: {misconception}.",
        "guided": f"Para «{focus.lower()}», parejas resuelven dos variaciones de {anchor}; una conserva la estructura y otra cambia un dato decisivo. Comparan estrategias y justifican qué comprobación descarta una respuesta aparente.",
        "independent": f"Resuelve un caso nuevo de «{focus.lower()}». Incluye representación, procedimiento, respuesta con unidad cuando corresponda y una comprobación distinta de repetir el cálculo.",
        "ticket": f"Explica cómo resolverías otro caso de «{focus.lower()}» y señala una evidencia que permitiría detectar un error.",
        "materials": f"Recursos reutilizables para {anchor}; pizarra, cuaderno y alternativa sin conectividad. Verifica legibilidad, escala, seguridad y disponibilidad.",
        "support": "Reduce temporalmente el rango o la cantidad, conserva la relación matemática y permite material concreto, tabla, recta o dibujo antes del símbolo; después retorna al desafío original.",
        "extension": f"Cambia una condición de {anchor}, predice el efecto y crea un contraejemplo que obligue a revisar la estrategia inicial.",
        "evidence": f"Solución individual sobre {focus.lower()} con representación pertinente, razonamiento visible, unidad y comprobación.",
        "criteria": ["responde al foco matemático de la clase", "usa una representación o estrategia pertinente", "fundamenta y comprueba la solución"],
        "next_step": "Avanza si representación, cálculo y explicación coinciden; si no, identifica si la barrera está en el concepto, la representación, el procedimiento o la comprobación y reenseña con un caso diferente.",
        "short_version": "Conserva el desafío, un modelado breve, práctica conjunta, evidencia individual y ticket; reduce repeticiones, no la demanda matemática.",
        "home_task": "Crea o busca un ejemplo cotidiano seguro del foco y explícalo con dibujo, nota u oralidad. No requiere internet, impresión, compras ni datos familiares.",
        "complementary": ["Recuperación: resolver un caso con menor carga y volver al original.", f"Análisis de error: corregir un caso ficticio que muestra esta confusión: {misconception}.", "Transferencia: cambiar una condición o representación y revisar la respuesta."],
        "difficulty_actions": [
            {"signal": "Responde antes de examinar datos o representación", "action": "Pide señalar la evidencia que usará y anticipar cómo la comprobará.", "check": "La nueva respuesta muestra datos y comprobación pertinentes."},
            {"signal": misconception.capitalize(), "action": "Vuelve a una representación concreta o pictórica, contrasta dos casos y retoma el desafío simbólico.", "check": "Resuelve un caso nuevo sin repetir la confusión y explica la diferencia."},
            {"signal": "Obtiene un resultado, pero no puede justificarlo", "action": "Solicita comparar con otra estrategia y nombrar el criterio decisivo.", "check": "La explicación permite reconstruir el razonamiento."},
        ],
        "specialist_coordination": "El docente mantiene la demanda matemática; educación diferencial ajusta acceso, manipulación, lectura o respuesta sin entregar la estrategia ni reducir el OA.",
        "transversal": _links(code, index, goal),
    }


def build_sequence(code: str) -> dict | None:
    profile = MATH.get(code)
    if not profile:
        return None
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": f"{profile['topic']} progresa desde {profile['prior'][0].lower() + profile['prior'][1:]} y enfrenta explícitamente la confusión «{profile['misconception']}». Cada clase exige representación, explicación y comprobación.",
        "prerequisites": profile["prior"],
        "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"Matemática · progresión interna en {len(profile['focuses'])} clases"],
            "unit_origin": "Organización pedagógica interna derivada del eje y del OA; no se presenta como unidad oficial del programa.",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del OA oficial",
            "source": f"https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/{code.lower().replace(' ', '-')}",
        },
        "lessons": [_lesson(code, index, profile) for index in range(len(profile["focuses"]))],
    }


def build_transversal_integration(item: dict) -> dict:
    clean = item["oa_text"].split("Unidad de Currículum", 1)[0].strip().rstrip(".")
    lessons = []
    for phase, phase_purpose in item["phases"]:
        lessons.append({
            "title": f"{phase}: {clean}",
            "purpose": f"Integrar de manera observable «{clean.lower()}» dentro del OA matemático en curso, sin convertirlo en una clase aislada.",
            "goal": f"Hoy demostraré {clean.lower()} mientras resuelvo un desafío matemático.",
            "opening": "Contrasta dos respuestas ficticias: una evidencia la habilidad o actitud mediante acciones matemáticas y otra solo la nombra.",
            "model": f"Modela cómo {phase_purpose} y verbaliza cuándo aparece «{clean.lower()}», qué decisión exige y qué evidencia permite observarla sin juzgar rasgos personales.",
            "guided": "Parejas resuelven un problema del OA en curso, usan una pauta de una conducta observable y mejoran su solución tras retroalimentación descriptiva.",
            "independent": f"Cada estudiante resuelve un caso nuevo y explica qué hizo para demostrar «{clean.lower()}».",
            "ticket": "Nombra una acción matemática observable, la evidencia que produjo y un ajuste para el siguiente intento.",
            "materials": "Problema matemático en curso, pauta breve y medio de respuesta accesible; sin materiales adicionales ni datos personales.",
            "support": "Anticipa la conducta observable, ofrece pauta visual y permite ensayo; conserva el OA y evita atribuir la dificultad a la personalidad.",
            "extension": "Transfiere la habilidad o disposición a otra representación o problema y compara qué cambia.",
            "evidence": "Solución matemática y registro individual de una acción observable vinculada con la habilidad o actitud.",
            "criteria": ["mantiene el OA matemático", "hace observable la habilidad o actitud", "revisa su actuación con evidencia"],
            "next_step": "Si solo repite la formulación, vuelve a una acción concreta; si la demuestra con autonomía, transfiérela a otro contexto.",
            "short_version": "Conserva modelado, desempeño matemático, observación individual y ticket.",
            "home_task": "Explica con un ejemplo ficticio cómo se vería esta habilidad o actitud; no requiere información familiar.",
            "complementary": ["Recuperación: elegir cuál acción evidencia el foco y justificar.", "Práctica: aplicar la pauta en un segundo intento.", "Profundización: adaptar la conducta a otra representación."],
            "difficulty_actions": [
                {"signal": "Repite el foco sin mostrarlo", "action": "Pide nombrar acción, momento y evidencia.", "check": "Ejecuta una conducta observable."},
                {"signal": "La integración desplaza la matemática", "action": "Vuelve a la meta del OA y observa el foco durante la resolución.", "check": "La evidencia demuestra contenido y transversalidad."},
                {"signal": "La pauta etiqueta al estudiante", "action": "Reformula en acciones situadas y modificables.", "check": "La retroalimentación describe acciones, no identidades."},
            ],
            "specialist_coordination": "El docente conserva la responsabilidad matemática; los apoyos acuerdan acceso y observación sin sustituir respuestas ni convertir la pauta en diagnóstico.",
            "transversal": [],
        })
    return {"lessons": lessons}

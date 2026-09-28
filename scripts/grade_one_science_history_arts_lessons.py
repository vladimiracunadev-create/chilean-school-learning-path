"""Curated first-grade sequences for Science, History and Visual Arts."""
from __future__ import annotations


def _spec(topic: str, misconception: str, materials: str, *steps: str) -> dict:
    return {"topic": topic, "misconception": misconception, "materials": materials, "steps": steps}


SCIENCE_SKILLS = (
    ("de Habilidad CN01 OAH a", "explorar y observar con los sentidos apropiados"),
    ("de Habilidad CN01 OAH b", "experimentar y medir con unidades no estandarizadas"),
    ("de Habilidad CN01 OAH c", "seguir instrucciones y usar materiales con seguridad"),
    ("de Habilidad CN01 OAH d", "comunicar y comparar observaciones e ideas"),
)
SCIENCE_ATTITUDES = (
    ("de Actitud CN01 OAA A", "curiosidad por el entorno natural"),
    ("de Actitud CN01 OAA B", "trabajo riguroso y perseverante"),
    ("de Actitud CN01 OAA C", "cuidado y protección del ambiente"),
    ("de Actitud CN01 OAA D", "responsabilidad y colaboración flexible"),
    ("de Actitud CN01 OAA E", "autocuidado y vida saludable"),
    ("de Actitud CN01 OAA F", "seguridad personal y colectiva"),
)
HISTORY_SKILLS = (
    ("de Habilidad HI01 OAH a", "secuenciar cronológicamente eventos familiares"),
    ("de Habilidad HI01 OAH b", "aplicar conceptos de tiempo"),
    ("de Habilidad HI01 OAH c", "localizar Chile y distinguir representaciones de la Tierra"),
    ("de Habilidad HI01 OAH d", "orientarse con categorías de ubicación relativa"),
    ("de Habilidad HI01 OAH e", "obtener información de fuentes orales y gráficas"),
    ("de Habilidad HI01 OAH f", "formular opiniones sobre el entorno y el pasado"),
    ("de Habilidad HI01 OAH g", "comunicar información de manera clara y coherente"),
)
HISTORY_ATTITUDES = (
    ("de Actitud HI01 OAA A", "rigurosidad, perseverancia y apertura a la crítica"),
    ("de Actitud HI01 OAA B", "dignidad de todos los trabajos"),
    ("de Actitud HI01 OAA C", "igualdad de derechos entre hombres y mujeres"),
    ("de Actitud HI01 OAA D", "igualdad de derechos sin discriminación"),
    ("de Actitud HI01 OAA E", "participación solidaria y responsable"),
    ("de Actitud HI01 OAA F", "pertenencia y valoración de comunidad y país"),
    ("de Actitud HI01 OAA G", "principios y virtudes ciudadanas"),
    ("de Actitud HI01 OAA H", "valoración de la democracia y los derechos"),
    ("de Actitud HI01 OAA I", "valoración de la vida en sociedad"),
)
ART_ATTITUDES = (
    ("de Actitud AR01 OAA A", "disfrute de múltiples expresiones artísticas"),
    ("de Actitud AR01 OAA B", "expresión artística de ideas y sentimientos"),
    ("de Actitud AR01 OAA C", "cuidado del patrimonio artístico"),
    ("de Actitud AR01 OAA D", "creatividad, experimentación y pensamiento divergente"),
    ("de Actitud AR01 OAA E", "colaboración y aceptación de consejos"),
    ("de Actitud AR01 OAA F", "valoración del rigor y del esfuerzo"),
    ("de Actitud AR01 OAA G", "respeto por la originalidad del trabajo artístico"),
)


SEQUENCES = {
    "CN01 OA 01": _spec("Seres vivos y cosas no vivas", "atribuye vida solo porque algo se mueve", "semillas, planta, piedra, juguete, lupas y registro", "Detectives de lo vivo|reconoceré evidencias de vida", "Necesidades para vivir|compararé agua, aire y alimento", "Respuesta, crecimiento y reproducción|relacionaré cambios con características de los seres vivos", "Clasificar con evidencia|justificaré si algo está vivo o no"),
    "CN01 OA 02": _spec("Características y hábitats de los animales", "clasifica por gusto y no por una característica observable", "fotografías de fauna chilena, tarjetas y aros", "Mirar como naturalistas|describiré tamaño y cubierta corporal", "Moverse de distintas maneras|compararé estructuras de desplazamiento", "Cada animal en su hábitat|relacionaré rasgos y lugar", "Una clasificación explicada|agruparé animales con un criterio observable"),
    "CN01 OA 03": _spec("Estructuras principales de las plantas", "nombra la planta completa sin distinguir sus estructuras", "plantas seguras, lupas, bandejas y láminas", "Explorar una planta completa|identificaré raíz, tallo, hojas y flores", "Raíces y tallos|compararé ubicación y apariencia", "Hojas y flores|registraré semejanzas y diferencias", "Modelo de una planta|ubicaré y rotularé sus estructuras"),
    "CN01 OA 04": _spec("Clasificación de estructuras vegetales", "cambia de criterio mientras clasifica", "semillas, frutos y flores seguros o imágenes, bandejas", "Colecciones vegetales|observaré forma, color, tamaño y textura", "Un criterio a la vez|clasificaré semillas y frutos", "Probar otra clasificación|reorganizaré la colección con un criterio distinto", "Feria de clasificaciones|comunicaré criterio y evidencia"),
    "CN01 OA 05": _spec("Plantas y animales de Chile y su cuidado", "propone cuidados generales sin vincularlos con una especie", "mapa de Chile, imágenes con procedencia y fichas", "Biodiversidad cercana|reconoceré especies de Chile", "Comparar para conocer|describiré rasgos observables", "Amenazas y necesidades|relacionaré una acción humana con su efecto", "Plan de cuidado situado|propondré una medida concreta para una especie"),
    "CN01 OA 06": _spec("Sentidos, órganos y prevención de riesgos", "asocia cada experiencia a un solo sentido de manera rígida", "tarjetas sensoriales, objetos seguros y silueta", "Cinco vías de información|ubicaré órganos de los sentidos", "¿Qué información recibimos?|describiré funciones con ejemplos", "Los sentidos trabajan juntos|compararé información combinada", "Protegernos al explorar|propondré medidas de cuidado y prevención"),
    "CN01 OA 07": _spec("Hábitos de vida saludable", "reduce la salud a una sola comida o conducta", "tarjetas de rutinas, alimentos ilustrados y calendario", "Rutinas que cuidan|distinguiré hábitos saludables", "Mover, descansar y asear|explicaré cómo cada hábito aporta", "Alimentos y lavado seguro|tomaré decisiones en casos cotidianos", "Mi plan posible|organizaré hábitos variados y justificaré uno"),
    "CN01 OA 08": _spec("Materiales, propiedades y usos", "nombra el objeto cuando se pregunta por el material", "objetos de goma, plástico, metal, madera, tela y papel", "Objeto no es material|identificaré de qué está hecho", "Propiedades observables|probaré flexibilidad, textura e impermeabilidad", "Clasificar materiales|agruparé por una propiedad comprobada", "Elegir para un uso|justificaré un material según su propiedad"),
    "CN01 OA 09": _spec("Cambios en materiales por fuerza, luz, calor y agua", "afirma un cambio sin comparar antes y después", "papel, masa, tela, recipientes, agua y fuentes seguras", "Antes y después|registraré un material sin intervención", "Fuerza y agua|observaré cambios bajo control", "Luz y calor con seguridad|interpretaré demostraciones comparables", "Explicar el cambio|comunicaré agente, evidencia y resultado"),
    "CN01 OA 10": _spec("Diseño de instrumentos tecnológicos simples", "construye antes de definir el problema y los criterios", "cartón, papel, elásticos, cinta, telas y tijeras escolares", "Problema, usuario y criterio|definiré qué debe resolver el instrumento", "Materiales con propósito|elegiré según propiedades", "Dibujar antes de construir|representaré partes y uniones", "Prototipo y prueba|construiré y recogeré evidencia", "Mejorar y comunicar|modificaré una decisión según la prueba"),
    "CN01 OA 11": _spec("Ciclo diario, día y noche", "explica día y noche porque el Sol se apaga", "registros del cielo, linterna, esfera y fotografías", "Observar el cielo diario|registraré luminosidad y astros visibles", "Ordenar un ciclo|secuenciaré amanecer, día, atardecer y noche", "Efectos en seres vivos|compararé actividades y ambiente", "Modelo y comunicación|describiré el ciclo sin atribuir que el Sol se apaga"),
    "CN01 OA 12": _spec("Estaciones y efectos en seres vivos y ambiente", "asume que todas las estaciones se ven igual en todo Chile", "calendario, mapas, fotografías regionales y registros", "Cambios durante el año|reconoceré señales estacionales", "Comparar estaciones|organizaré temperatura, luz y precipitación", "Efectos en la vida|relacionaré cambios con plantas, animales y personas", "Informe estacional local|comunicaré patrones sin generalizar todo Chile"),
    "HI01 OA 01": _spec("Días, meses y uso del calendario", "recita nombres sin localizar fechas ni reconocer el ciclo", "calendario anual y mensual, tarjetas y fechas ficticias", "La semana se repite|ordenaré días y ubicaré hoy", "Meses y estaciones del año|secuenciaré los doce meses", "Leer un calendario|localizaré una fecha y contaré intervalos", "El año en curso|comunicaré fecha completa y posición temporal"),
    "HI01 OA 02": _spec("Secuencias y categorías de tiempo cotidiano", "ordena por preferencia en vez de por temporalidad", "viñetas, línea de tiempo y tarjetas temporales", "Antes y después|ordenaré dos acontecimientos", "Ayer, hoy y mañana|ubicaré actividades respecto del presente", "Día y noche|relacionaré rutinas con momentos", "Año pasado y próximo|compararé escalas temporales", "Relato temporal|comunicaré una secuencia coherente"),
    "HI01 OA 03": _spec("Identidad personal y diversidad", "confunde identidad con una lista fija o exige datos privados", "siluetas, fichas optativas y mapa sin domicilios", "Mi nombre y mis elecciones|registraré información segura sobre mí", "Procedencias y ascendencias|reconoceré historias diversas sin suponer", "Gustos, intereses y vínculos|compararé semejanzas y diferencias", "Retrato de identidad|comunicaré rasgos elegidos respetando privacidad"),
    "HI01 OA 04": _spec("Historia y características de las familias", "supone que existe un único tipo de familia o tradición", "fotografías ficticias, objetos-fuente y pauta de entrevista", "Familias diversas|reconoceré integrantes y roles sin estereotipos", "Preguntas que investigan|formularé preguntas respetuosas", "Una fuente oral|registraré información de un adulto", "Costumbres y cambios|compararé continuidad y transformación", "Historia familiar cuidada|comunicaré hallazgos sin exponer datos sensibles"),
    "HI01 OA 05": _spec("Símbolos y conmemoraciones de Chile", "confunde conmemorar con celebrar o memorizar una fecha", "bandera y escudo reproducidos con fuente, audio autorizado y fotografías", "Símbolos representativos|identificaré bandera, escudo e himno", "Leer sus elementos|describiré rasgos sin inventar significados", "Conmemoraciones y memoria|distinguiré hechos, perspectivas y actividades", "Participación de mujeres y hombres|reconoceré diversidad de aportes", "Unidad con diversidad|explicaré cómo un símbolo puede vincularnos"),
    "HI01 OA 06": _spec("Expresiones culturales locales y nacionales", "presenta una tradición como idéntica, inmóvil o universal", "mapa, relatos e imágenes con procedencia de fiestas, juegos y comidas", "Cultura en lo cotidiano|reconoceré expresiones cercanas", "Fiestas y tradiciones|describiré una práctica en su contexto", "Local y nacional|ubicaré semejanzas y diferencias", "Fuentes y voces|evitaré generalizaciones al comunicar", "Muestra cultural respetuosa|explicaré por qué una expresión genera pertenencia"),
    "HI01 OA 07": _spec("Personas que contribuyen a la sociedad chilena", "reduce la contribución a fama, heroísmo o un solo grupo", "biografías breves con fuentes, línea temporal e imágenes", "¿Qué es contribuir?|vincularé acción y beneficio social", "Ámbitos diversos|compararé ciencia, arte, deporte y solidaridad", "Una vida en fuentes|obtendré información explícita", "Personas antes invisibilizadas|reconoceré aportes de mujeres y comunidades", "Biografía argumentada|comunicaré un aporte con evidencia"),
    "HI01 OA 08": _spec("Mapas y planos como representaciones", "trata el mapa como una fotografía exacta del lugar", "objetos, vista superior, plano del aula, mapa y símbolos", "Del lugar a la representación|distinguiré espacio y dibujo", "Mirar desde arriba|construiré una vista superior", "Símbolos y leyenda|interpretaré representaciones", "Plano útil|representaré un recorrido y explicaré sus límites"),
    "HI01 OA 09": _spec("Chile en mapas y referencias territoriales", "ubica elementos por forma memorizada sin usar referencias", "globo, mapamundi, mapas de Chile y de la región", "Chile en el mundo|localizaré país y continente", "Andes y Pacífico|reconoceré límites naturales de referencia", "Región, capital y localidad|distinguiré escalas", "Ruta de localización|comunicaré dónde vivo sin publicar dirección"),
    "HI01 OA 10": _spec("Paisajes y ubicación relativa", "enumera objetos sin describir relaciones espaciales", "fotografías de paisajes chilenos, croquis y tarjetas", "Vocabulario del paisaje|reconoceré elementos naturales y construidos", "Derecha, izquierda y entre|ubicaré elementos relativamente", "Paisaje local|describiré relaciones con precisión", "Comparar paisajes|identificaré semejanzas y diferencias", "Croquis comentado|representaré y comunicaré un lugar"),
    "HI01 OA 11": _spec("Trabajos, productos y vida cotidiana", "valora solo trabajos pagados o asigna labores por género", "tarjetas de trabajos y productos, cadena simple y casos", "Trabajo visible e invisible|reconoceré labores remuneradas y no remuneradas", "Del trabajo al producto o servicio|relacionaré aportes", "Interdependencia local|seguiré una cadena cotidiana", "Dignidad de cada trabajo|explicaré su importancia sin estereotipos"),
    "HI01 OA 12": _spec("Vida cotidiana de niños en distintas partes del mundo", "convierte una imagen aislada en descripción de todo un país", "mapamundi, relatos infantiles e imágenes con procedencia", "Niñez y lugar|localizaré un país a partir de una fuente", "Idioma y vida diaria|obtendré información explícita", "Comidas, fiestas y vestimentas|compararé sin jerarquizar", "Tareas y escuela|reconoceré diversidad dentro de un país", "Comparación responsable|comunicaré semejanzas, diferencias y límites de la fuente"),
    "HI01 OA 13": _spec("Respeto, empatía y responsabilidad en comunidad", "repite valores sin traducirlos en acciones observables", "casos ficticios, tarjetas de decisión y acuerdos de aula", "Respeto en acciones|distinguiré trato cuidadoso y daño", "Empatía sin suponer|preguntaré y ofreceré ayuda", "Responsabilidad concreta|asumiré encargos y reparación", "Igualdad y no discriminación|resolveré un caso con derechos", "Compromiso comunitario|propondré una acción verificable"),
    "HI01 OA 14": _spec("Normas de convivencia, seguridad y autocuidado", "entiende la norma como orden sin propósito ni posibilidad de explicación", "señales, casos de hogar, escuela y vía pública", "Normas y propósitos|relacionaré una regla con el cuidado", "Buena convivencia|aplicaré acuerdos en un conflicto", "Seguridad en hogar y escuela|decidiré ante riesgos", "Vía pública y autocuidado|explicaré una conducta segura"),
    "HI01 OA 15": _spec("Instituciones y servicios de la comunidad", "confunde edificio, institución y persona que presta el servicio", "mapa local ficticio, tarjetas de necesidades e instituciones", "Necesidad y servicio|identificaré qué problema atiende una institución", "Personas que la hacen funcionar|relacionaré roles y tareas", "Red comunitaria|elegiré a quién recurrir en casos seguros", "Mapa de servicios|comunicaré beneficio y límites de cada institución"),
    "AR01 OA 01": _spec("Creación artística desde la observación del entorno", "copia una imagen sin observar ni tomar decisiones propias", "imágenes con procedencia, visor de cartón, lápices, pintura, papeles y soporte", "Observar antes de crear|registraré formas y detalles del entorno natural", "Paisaje, animales y plantas|seleccionaré un foco y una composición", "Vida cotidiana y familiar|transformaré una observación en idea visual", "Mirar arte local y chileno|reconoceré decisiones de otros artistas", "Ampliar la mirada latinoamericana y universal|compararé modos de representar", "Obra con punto de vista propio|crearé y explicaré decisiones nacidas de la observación"),
    "AR01 OA 02": _spec("Línea, color y textura en la creación visual", "usa elementos al azar sin relacionarlos con una intención", "lápices, témpera, papeles, telas, frottage y soportes", "Familias de líneas|experimentaré grosor, dirección y recorrido", "Colores puros y mezclados|produciré variaciones observables", "Temperatura del color|usaré cálidos y fríos con intención", "Texturas visuales y táctiles|compararé y seleccionaré materialidades", "Composición con decisiones|integraré línea, color y textura y explicaré una elección"),
    "AR01 OA 03": _spec("Materiales, herramientas y procedimientos artísticos", "imita un modelo único o elige materiales solo por preferencia", "arcilla o masa, reciclaje limpio, papeles, pintura, tijeras y recurso digital opcional", "Laboratorio de materiales|exploraré posibilidades y límites", "Herramientas y seguridad|usaré cortar, unir, pintar y modelar", "Una emoción, varias materialidades|compararé efectos expresivos", "Crear con un procedimiento|produciré una obra propia", "Revisar el proceso|ajustaré una decisión y registraré por qué"),
    "AR01 OA 04": _spec("Primeras impresiones y apreciación de obras", "dice solo me gusta o no me gusta sin observar la obra", "selección con procedencia de arte local, chileno, latinoamericano y universal", "Detenerse a observar|describiré antes de interpretar", "Lo que siento y pienso|vincularé impresión con un elemento visible", "Muchas voces ante una obra|escucharé interpretaciones diferentes", "Galería comparada|comunicaré una impresión fundamentada por distintos medios"),
    "AR01 OA 05": _spec("Preferencias y retroalimentación sobre trabajos de arte", "evalúa a la persona o la prolijidad en vez de decisiones visuales", "trabajos propios, marcos de observación y tarjetas de vocabulario", "Preferir con razones|nombraré un elemento visual que orienta mi elección", "Hablar de mi proceso|explicaré una decisión y un cambio", "Mirar el trabajo de pares|formularé una observación respetuosa", "Círculo de apreciación|compararé preferencias sin jerarquizar personas"),
}


PROFILES = {
    "CN": {"name": "Ciencias Naturales", "slug": "ciencias-naturales", "stimulus": "objeto, fenómeno o registro", "evidence": "observación, registro o explicación apoyada en evidencia", "support": "Reduce variables, ofrece objetos o imágenes observables, modela un registro y permite señalar, dibujar o explicar oralmente sin quitar la comparación científica."},
    "HI": {"name": "Historia, Geografía y Ciencias Sociales", "slug": "historia-geografia-ciencias-sociales", "stimulus": "fuente, mapa o situación comunitaria", "evidence": "secuencia, localización o explicación sustentada en una fuente", "support": "Acota la fuente, anticipa vocabulario, ofrece una secuencia o mapa de apoyo y permite respuesta oral o gráfica sin sustituir la decisión histórica, geográfica o ciudadana."},
    "AR": {"name": "Artes Visuales", "slug": "artes-visuales", "stimulus": "obra, imagen o materialidad", "evidence": "obra o proceso acompañado por una decisión visual explicada", "support": "Ofrece materiales y modos de participación accesibles, demuestra el uso seguro de la herramienta y conserva elección, experimentación y autoría; no exige copiar un modelo."},
}


def transversal_links(code: str, lesson_index: int, goal: str) -> list[dict[str, str]]:
    prefix = code[:2]
    oa_number = int(code.rsplit(" ", 1)[-1])
    if prefix == "CN":
        pools = (SCIENCE_SKILLS, SCIENCE_ATTITUDES)
        types = ("Habilidad", "Actitud")
    elif prefix == "HI":
        pools = (HISTORY_SKILLS, HISTORY_ATTITUDES)
        types = ("Habilidad", "Actitud")
    else:
        pools = (ART_ATTITUDES,)
        types = ("Actitud",)
    links = []
    for offset, (pool, kind) in enumerate(zip(pools, types)):
        item_code, label = pool[(oa_number * (offset + 1) + lesson_index) % len(pool)]
        links.append({"code": item_code, "type": kind, "application": f"Se trabaja {label} durante «{goal}» y se registra una conducta o producción observable, sin calificar rasgos personales."})
    return links


def build_sequence(code: str) -> dict | None:
    data = SEQUENCES.get(code)
    if not data:
        return None
    profile = PROFILES[code[:2]]
    oa_number = int(code.rsplit(" ", 1)[-1])
    lessons = []
    for index, step in enumerate(data["steps"]):
        title, goal = step.split("|", 1)
        lessons.append({
            "title": title,
            "purpose": f"Desarrollar la comprensión de {data['topic'].lower()} mediante «{title.lower()}», conservando la demanda del OA y una evidencia observable.",
            "goal": f"Hoy {goal}.",
            "opening": f"Presenta un {profile['stimulus']} vinculado con «{title.lower()}» y una respuesta que contiene el problema «{data['misconception']}». Cada estudiante registra una primera idea antes de discutirla.",
            "model": f"Piensa en voz alta cómo abordar «{title.lower()}»: observa o consulta la fuente, nombra una evidencia específica, prueba una decisión y contrástala con la meta «{goal}».",
            "guided": f"En parejas resuelven un caso nuevo de «{data['topic'].lower()}». Una persona actúa o propone y otra solicita la evidencia; cambian roles y mejoran una decisión con retroalimentación inmediata.",
            "independent": f"Cada estudiante produce una {profile['evidence']} vinculada a la meta «{goal}», usando un caso distinto del modelado y explicando al menos una decisión propia.",
            "ticket": f"Ante una situación breve inédita, presenta una respuesta para la meta «{goal}»; identifica la evidencia usada y corrige una decisión si la comparación no la sostiene.",
            "materials": data["materials"],
            "support": profile["support"],
            "extension": f"Cambia una condición, fuente, material o contexto de «{data['topic'].lower()}» y explica qué decisión debe modificarse y cuál se conserva.",
            "evidence": f"{profile['evidence'].capitalize()} vinculada a «{goal}», con una huella concreta del proceso y una explicación breve.",
            "criteria": ["responde a la meta y al OA", "usa una observación, fuente o elemento específico", "explica una decisión y la revisa cuando la evidencia lo exige"],
            "next_step": "Avanza si la evidencia es pertinente y la explicación conserva el criterio; si aparece un patrón de error, vuelve a un caso contrastante, retira una barrera y recoge evidencia individual nueva.",
            "short_version": "Conserva el caso inicial, el modelado explícito, una práctica guiada, la producción individual y el ticket. Reduce cantidad de casos o materiales, no observación, decisión ni explicación.",
            "home_task": "Observa en casa o en el entorno un ejemplo relacionado, regístralo con dibujo o palabras y explica una semejanza o decisión. No requiere internet, compra ni exposición de datos privados.",
            "complementary": ["Recuperación: vuelve a un caso perceptible y modela un solo criterio antes de un nuevo intento.", "Taller de errores: contrasta dos respuestas ficticias y mejora la que no usa evidencia suficiente.", "Profundización: cambia una condición o perspectiva y justifica el efecto sobre la decisión."],
            "difficulty_actions": [
                {"signal": "No inicia o repite la consigna", "action": "Ofrece dos entradas posibles, reduce información accesoria y modela un ejemplo diferente.", "check": "Inicia una producción propia y señala qué debe observar, representar o decidir."},
                {"signal": data["misconception"].capitalize(), "action": "Detén la tarea, contrasta un caso límite y pide nombrar la evidencia antes de responder.", "check": "Resuelve un caso nuevo manteniendo el criterio y explica la diferencia."},
                {"signal": "Produce una respuesta sin fundamento", "action": "Solicita una huella concreta —observación, fuente, elemento visual o prueba— y ofrece una frase de apoyo temporal.", "check": "Vincula su decisión con una evidencia específica sin repetir el modelo."},
            ],
            "specialist_coordination": "El docente de asignatura conduce la enseñanza. Educación diferencial u otro profesional, cuando corresponda al plan del estudiante, asesora acceso, comunicación y seguridad sin reemplazar la demanda del OA ni diagnosticar durante la clase.",
            "transversal": transversal_links(code, index, goal),
        })
    source = f"https://www.curriculumnacional.cl/curriculum/1o-6o-basico/{profile['slug']}/1-basico/{code.lower().replace(' ', '-')}"
    return {
        "topic": data["topic"],
        "pedagogical_explanation": f"La secuencia desarrolla {data['topic'].lower()} desde una experiencia observable hacia una producción individual fundamentada. Evita el atajo de que el estudiante {data['misconception']} y usa contraste, práctica y revisión.",
        "prerequisites": "Participar en una experiencia breve, comunicar una observación o idea inicial y seguir acuerdos de cuidado; no se exige dominio previo del concepto.",
        "vocabulary": ", ".join(dict.fromkeys((data["topic"].lower() + ", evidencia, comparar, explicar, decisión y revisar").split(", "))),
        "official_alignment": {"units": [f"Progresión anual de {profile['name']} de 1° básico"], "indicators": [f"Criterio interno derivado del OA: {step.split('|', 1)[1]}." for step in data["steps"][:3]], "source": source, "indicator_origin": "criterios internos derivados del OA; requieren contraste con el Programa de Estudio"},
        "lessons": lessons,
    }

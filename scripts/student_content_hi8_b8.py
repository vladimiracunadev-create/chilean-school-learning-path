"""Cuaderno del estudiante, 8.º básico Historia, Geografía y Ciencias Sociales: OA 17 (legitimidad de la conquista y derechos humanos)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA = "HI08 OA 17"

# ================================================================ clase 1
lesson(
    OA, 1,
    "Aprenderé a situar en el tiempo y el espacio el debate sobre la legitimidad de la conquista de América en el siglo XVI y a plantear el problema: con qué derecho se conquistó y se sometió a los pueblos indígenas.",
    ["Sé que los españoles conquistaron gran parte de América en el siglo XVI.", "Conozco la encomienda y la evangelización."],
    [
        "Tras la llegada de Cristóbal Colón en 1492, la Corona de Castilla extendió su dominio sobre América. Pronto surgió una pregunta: ¿era justo conquistar y someter a los pueblos que vivían allí? Esa pregunta es el debate sobre la legitimidad de la conquista. Legítimo significa que tiene un fundamento aceptado como justo. El debate ocurrió sobre todo en el siglo XVI (años 1501 a 1600), en América y en España.",
        "Los españoles daban distintas justificaciones. Una era religiosa: en 1493 el papa Alejandro VI entregó a los reyes de Castilla el derecho de evangelizar las tierras halladas. Otra era política y jurídica: el Requerimiento, un texto de 1513 que se leía a los indígenas para que reconocieran la autoridad del rey y de la Iglesia, y si no, se les podía hacer la guerra. Pero otros españoles criticaron estas razones. En 1511, en La Española (isla del Caribe), el dominico Antonio de Montesinos predicó contra los abusos.",
        "El problema de esta unidad es: ¿cuáles fueron las posturas en el debate sobre la legitimidad de la conquista y por qué importan para entender los derechos humanos? Para responder hay que ubicar fechas, lugares y personas, y reconocer que las voces indígenas casi no quedaron registradas en los documentos españoles.",
    ],
    [("legitimidad", "condición de lo que se acepta como justo o con fundamento"), ("bula", "documento firmado por el papa"), ("Requerimiento", "texto de 1513 que se leía a los indígenas para exigirles reconocer la autoridad del rey y de la Iglesia"), ("derechos humanos", "derechos que tiene toda persona por el hecho de serlo"), ("dominico", "religioso de la orden de Santo Domingo")],
    [
        ("Ubicar en el tiempo", "El sermón de Montesinos fue en 1511. ¿En qué siglo ocurrió?", ["El siglo XVI va de 1501 a 1600.", "1511 está dentro."], "En el siglo XVI"),
        ("Ubicar en el espacio", "¿En qué isla del Caribe predicó Montesinos?", ["La clase lo indica.", "La Española."], "En La Española"),
    ],
    [
        ("Creer que todos los españoles justificaban la conquista.", "Algunos la criticaron, como Montesinos.", "Distingue posturas."),
        ("Pensar que el debate se escuchó a los indígenas.", "Casi no quedaron registradas sus voces en los documentos españoles.", "Recuerda los silencios de las fuentes."),
    ],
    [
        ("¿Qué año llegó Colón a América?", "1492", "Se dice en el primer párrafo."),
        ("¿Qué es el Requerimiento?", "Un texto de 1513 que se leía a los indígenas para exigirles reconocer la autoridad del rey y de la Iglesia", "Está en el vocabulario."),
        ("¿Quién predicó contra los abusos en La Española en 1511?", "Antonio de Montesinos", "Se dice en el segundo párrafo."),
    ],
    [
        ("¿Qué significa «legítimo»?", "Que tiene un fundamento aceptado como justo", "Se explicó en el primer párrafo."),
        ("¿Qué justificación religiosa se daba para la conquista?", "El derecho de evangelizar entregado por el papa en 1493", "Se explicó en el segundo párrafo."),
        ("¿Por qué las voces indígenas casi no aparecen en los documentos?", "Porque los documentos eran escritos por españoles", "Se explicó en el tercer párrafo."),
    ],
    [
        arith("Colón llegó en 1492 y el Requerimiento es de 1513. ¿Cuántos años pasaron entre ambos hechos?", "1513-1492", "Se resta el año menor al mayor."),
        arith("El papa dio el derecho de evangelizar en 1493 y Montesinos predicó en 1511. ¿Cuántos años pasaron?", "1511-1493", "Se resta el año de la bula al del sermón."),
        ("Una ficha de ejemplo dice: «1511: un dominico critica los abusos en una isla del Caribe». ¿Qué debate abre esa crítica?", "El debate sobre la legitimidad de la conquista", "Cuestiona con qué derecho se sometía a los indígenas."),
    ],
    [
        ("Un estudiante dice: «Nadie en el siglo XVI cuestionó la conquista». ¿Qué error comete?", "Ignora que Montesinos y otros la criticaron", "La clase presenta críticas."),
        ("¿Por qué un documento como el Requerimiento ayuda a estudiar el debate?", "Porque muestra cómo se intentaba justificar jurídicamente la conquista", "Era un texto oficial con ese propósito."),
    ],
    [
        ("Ordena de más antiguo a más reciente: A = Requerimiento (1513), B = Colón llega a América (1492), C = sermón de Montesinos (1511).", "B, C, A", "Las fechas en orden son 1492, 1511 y 1513."),
        arith("Un barco de ejemplo transporta 120 soldados y 30 religiosos. ¿Cuántas personas transporta?", "120+30", "Se suman los dos grupos."),
    ],
    [("Una línea de tiempo de ejemplo dice: «1492 Colón. 1493 bula papal. 1511 Montesinos. 1513 Requerimiento». ¿Cuántos hitos aparecen y cuántos son del siglo XVI?", "4 hitos; 2 del siglo XVI (1511 y 1513)", "Hay cuatro fechas y solo 1511 y 1513 están entre 1501 y 1600.")],
    [("¿Qué es la legitimidad?", "La condición de lo que se acepta como justo o con fundamento", "Está en el vocabulario."), ("¿Qué es una bula?", "Un documento firmado por el papa", "Está en el vocabulario."), ("¿Qué siglo fue el del debate?", "El siglo XVI", "Se explicó en el primer párrafo.")],
    (
        "Dibuja una línea de tiempo con cuatro hitos: 1492 (Colón), 1493 (bula del papa), 1511 (sermón de Montesinos) y 1513 (Requerimiento). Bajo cada hito escribe si justifica o critica la conquista. Termina con una pregunta que quieras responder en la unidad.",
        "1492: llegada de Colón. 1493: justifica con la bula. 1511: critica con Montesinos. 1513: justifica con el Requerimiento. Pregunta: ¿qué pensaban los indígenas?",
        ["ubica los cuatro hitos", "indica si justifica o critica", "formula una pregunta"],
        ["línea de tiempo con cuatro hitos y una pregunta"],
        ["desordenar fechas", "olvidar la perspectiva indígena"],
        "Explica tu línea de tiempo a una persona de tu casa.",
    ),
    "Escribe en dos líneas qué significa «legitimidad de la conquista».",
    "Escribe una pregunta sobre cómo habrían respondido los indígenas al Requerimiento.",
)

# ================================================================ clase 2
lesson(
    OA, 2,
    "Aprenderé a contextualizar y seleccionar fuentes del debate sobre la conquista: el Requerimiento, el sermón de Montesinos y los escritos de Las Casas, Sepúlveda y Vitoria. Sirve para saber quién habla y desde qué interés.",
    ["Conozco el contexto del debate del siglo XVI.", "Sé que una fuente tiene autor, fecha y propósito."],
    [
        "El Requerimiento (1513) era un texto que un funcionario leía a los indígenas, a menudo en castellano, sin que lo entendieran. Les pedía reconocer a la Iglesia y al rey como señores; si no lo hacían, quedaban sujetos a guerra y esclavitud. Sirve como fuente para ver cómo la Corona quiso dar un fundamento legal a la conquista.",
        "Otras fuentes expresan críticas. El sermón de Montesinos (1511) preguntó con qué derecho y justicia se mantenía a los indígenas en dura servidumbre. Bartolomé de las Casas, dominico, escribió la Brevísima relación de la destrucción de las Indias (1552), un texto que denunciaba la violencia de la conquista. Francisco de Vitoria, teólogo de la Universidad de Salamanca, analizó en 1539 los derechos de los indígenas. Juan Ginés de Sepúlveda defendió que la conquista podía ser justa en ciertas condiciones.",
        "Cada autor escribía con un propósito. Las Casas quería convencer al rey de proteger a los indígenas y pudo exagerar cifras. Sepúlveda defendía una guerra justa para someter a pueblos que, según él, eran inferiores. Vitoria razonaba desde la teología y el derecho. Al leer hay que preguntar quién habla, para quién escribe y qué voces faltan: casi no hay textos escritos por los propios indígenas.",
    ],
    [("sermón", "discurso religioso pronunciado ante una comunidad"), ("teólogo", "persona que estudia y enseña las doctrinas religiosas"), ("guerra justa", "idea de que una guerra puede ser legítima por causas aceptadas como justas"), ("Brevísima relación", "libro de Las Casas (1552) que denunció la violencia de la conquista"), ("servidumbre", "situación de quien está sometido a trabajar para otro")],
    [
        ("Identificar la perspectiva", "Un texto de ejemplo dice: «Los indígenas son personas libres con derechos». ¿A cuál autor de la clase se parece más?", ["Defiende derechos de los indígenas.", "Se parece a Las Casas o a Vitoria."], "A Las Casas o Vitoria"),
        ("Elegir la fuente", "Pregunta: ¿cómo quiso la Corona justificar legalmente la conquista? Opciones: Requerimiento o sermón de Montesinos. ¿Cuál conviene?", ["El Requerimiento es un texto oficial.", "El sermón critica."], "El Requerimiento"),
    ],
    [
        ("Creer que Las Casas describe todo con exactitud.", "Escribía para convencer al rey y pudo exagerar.", "Compara con otras fuentes."),
        ("Pensar que el Requerimiento era entendido por los indígenas.", "A menudo se leía en castellano sin traducción.", "Cuestiona su eficacia."),
    ],
    [
        ("¿Quién escribió la Brevísima relación de la destrucción de las Indias?", "Bartolomé de las Casas", "Se dice en el segundo párrafo."),
        ("¿Quién defendió que la conquista podía ser justa en ciertas condiciones?", "Juan Ginés de Sepúlveda", "Se dice en el segundo párrafo."),
        ("¿Quién analizó los derechos de los indígenas en Salamanca en 1539?", "Francisco de Vitoria", "Se dice en el segundo párrafo."),
    ],
    [
        ("¿Por qué el Requerimiento tiene límites como fuente de lo que entendían los indígenas?", "Porque se leía a menudo en castellano sin traducción", "Se explicó en el primer párrafo."),
        ("¿Qué quería lograr Las Casas con su libro?", "Convencer al rey de proteger a los indígenas", "Se explicó en el tercer párrafo."),
        ("¿Qué voces faltan en estas fuentes?", "Las de los propios indígenas", "Se explicó en el tercer párrafo."),
    ],
    [
        arith("La Brevísima relación se publicó en 1552 y el sermón de Montesinos fue en 1511. ¿Cuántos años pasaron?", "1552-1511", "Se resta el año menor al mayor."),
        ("Pregunta: ¿qué pensaba un teólogo sobre los derechos de los indígenas en 1539? Fuentes: 1 = análisis de Vitoria; 2 = lista de soldados; 3 = mapa de rutas. ¿Cuál es la más adecuada?", "La 1", "El análisis de Vitoria trata los derechos de los indígenas."),
        ("Un texto de ejemplo dice: «Los pueblos sin escritura deben ser guiados por otros». ¿Qué postura de la clase se acerca a esta idea?", "La de Sepúlveda", "Sepúlveda sostenía que ciertos pueblos podían ser sometidos."),
    ],
    [
        ("Un estudiante concluye: «Como Las Casas dice que murieron muchos, la cifra exacta es esa». ¿Qué límite tiene la conclusión?", "Las Casas escribía para convencer y pudo exagerar cifras", "Una fuente con propósito no da cifras exactas."),
        ("¿Por qué conviene leer a Las Casas y a Sepúlveda juntos?", "Porque se contrastan posturas opuestas sobre el mismo tema", "Cada uno defiende una mirada distinta."),
    ],
    [
        ("Ordena por fecha de más antigua a más reciente: A = Brevísima relación (1552), B = Vitoria en Salamanca (1539), C = Requerimiento (1513).", "C, B, A", "Las fechas en orden son 1513, 1539 y 1552."),
        arith("Una biblioteca de ejemplo guarda 6 sermones, 9 cartas y 5 libros sobre la conquista. ¿Cuántos documentos guarda?", "6+9+5", "Se suman los tres grupos."),
    ],
    [("Un texto de ejemplo: «Fray Bartolomé al rey, 1540: los indios son prójimos y no deben ser maltratados». ¿Qué postura expresa y a quién se dirige?", "Defensa de los indígenas; al rey", "Pide protección al rey.")],
    [("¿Qué es una guerra justa?", "La idea de que una guerra puede ser legítima por causas aceptadas como justas", "Está en el vocabulario."), ("¿Qué es un sermón?", "Un discurso religioso pronunciado ante una comunidad", "Está en el vocabulario."), ("¿Qué pregunta ayuda a leer una fuente?", "¿Quién habla y para qué?", "Se explicó en el tercer párrafo.")],
    (
        "Lee esta paráfrasis de ejemplo: «Los indios son seres humanos libres; no se puede someterlos solo porque no sean cristianos». Escribe una tabla con cuatro filas: qué autor se le parece, qué postura defiende, qué fuente de la clase la apoya, qué voz falta. Cierra con una frase.",
        "Se parece a Las Casas o Vitoria. Defiende los derechos de los indígenas. Lo apoya la Brevísima relación o el análisis de Vitoria. Falta la voz de los indígenas.",
        ["relaciona la idea con un autor", "indica la postura", "señala la voz que falta"],
        ["tabla de cuatro filas y una frase"],
        ["atribuir la idea a Sepúlveda", "no señalar silencios"],
        "Explica la idea a una persona de tu casa con tus palabras.",
    ),
    "Escribe una frase que resuma la postura de cada autor.",
    "Escribe una pregunta sobre qué fuentes indígenas existen de la época.",
)

# ================================================================ clase 3
lesson(
    OA, 3,
    "Aprenderé a relacionar cambio, continuidad y territorio en el debate sobre la conquista: qué leyes se dictaron, qué cambió en el trato a los indígenas y qué siguió igual. Sirve para ver el efecto real de las ideas.",
    ["Conozco las posturas y las fuentes del debate.", "Conozco la encomienda y la mita."],
    [
        "El debate tuvo consecuencias legales. En 1512 se dictaron las Leyes de Burgos, que intentaron regular el trabajo y el trato de los indígenas y dieron más importancia a su instrucción religiosa. En 1542 se promulgaron las Leyes Nuevas, que prohibieron esclavizar a los indígenas y limitaron la encomienda hereditaria. Entre 1550 y 1551 se realizó en Valladolid una gran discusión entre Las Casas y Sepúlveda ante un grupo de expertos. Nadie ganó de forma clara, pero el debate dejó huellas.",
        "Hubo un cambio importante: se reconoció que los indígenas eran personas libres, vasallos de la Corona, con algunos derechos. Pero también hubo continuidades: la conquista siguió, la encomienda y la mita persistieron y los abusos continuaron en muchos lugares. Las leyes se aplicaron de forma irregular; en América muchos encomenderos protestaron y algunas medidas se suavizaron.",
        "El territorio importó. El debate ocurría en España, pero se aplicaba en América, a miles de kilómetros. Las autoridades locales, lejos del rey, interpretaban las leyes según sus intereses, y por eso se decía «se acata pero no se cumple». También hubo un efecto doloroso: algunos defensores de los indígenas aceptaron en algún momento el trabajo de africanos esclavizados, lo que agravó la trata. Las Casas lo lamentó más tarde.",
    ],
    [("Leyes de Burgos", "leyes de 1512 que intentaron regular el trato de los indígenas"), ("Leyes Nuevas", "leyes de 1542 que prohibieron esclavizar indígenas y limitaron la encomienda hereditaria"), ("Valladolid", "ciudad de España donde se realizó el debate de 1550-1551"), ("vasallo", "persona sujeta a la autoridad de un rey o de un señor"), ("«se acata pero no se cumple»", "fórmula usada en América para obedecer una orden en la forma, pero no aplicarla")],
    [
        ("Reconocer un cambio", "Las Leyes Nuevas prohibieron esclavizar indígenas. ¿Es un cambio o una continuidad respecto de antes?", ["Antes se esclavizaba.", "Ahora se prohíbe."], "Un cambio"),
        ("Reconocer una continuidad", "La encomienda y la mita persistieron después de las leyes. ¿Es cambio o continuidad?", ["Siguieron existiendo.", "Se mantuvieron."], "Una continuidad"),
    ],
    [
        ("Creer que las leyes eliminaron los abusos.", "Se aplicaron de forma irregular y los abusos continuaron.", "Distingue ley y práctica."),
        ("Creer que todos los defensores de los indígenas defendían a todas las personas.", "Algunos aceptaron la esclavitud africana.", "Reconoce las contradicciones."),
    ],
    [
        ("¿En qué año se dictaron las Leyes de Burgos?", "En 1512", "Se dice en el primer párrafo."),
        ("¿Qué prohibieron las Leyes Nuevas de 1542?", "Esclavizar a los indígenas", "Se dice en el primer párrafo."),
        ("¿En qué ciudad se realizó el debate entre Las Casas y Sepúlveda?", "Valladolid", "Se dice en el primer párrafo."),
    ],
    [
        ("¿Qué cambio importante dejó el debate?", "Se reconoció que los indígenas eran personas libres, vasallos de la Corona, con algunos derechos", "Se explicó en el segundo párrafo."),
        ("¿Por qué las leyes se aplicaban de forma irregular?", "Porque las autoridades locales estaban lejos del rey y las interpretaban según sus intereses", "Se explicó en el tercer párrafo."),
        ("¿Qué contradicción dolorosa se dio en el debate?", "Algunos defensores de los indígenas aceptaron el trabajo de africanos esclavizados", "Se explicó en el tercer párrafo."),
    ],
    [
        arith("Entre las Leyes de Burgos (1512) y las Leyes Nuevas (1542), ¿cuántos años pasaron?", "1542-1512", "Se resta el año menor al mayor."),
        ("¿Qué dos personas debatieron en Valladolid entre 1550 y 1551?", "Las Casas y Sepúlveda", "Se dice en el primer párrafo."),
        ("Un funcionario de ejemplo en América recibe una orden del rey y dice «se acata pero no se cumple». ¿Qué hace con la orden?", "La obedece en la forma, pero no la aplica", "Es el sentido de la fórmula."),
    ],
    [
        ("Un estudiante dice: «Con las Leyes Nuevas terminó toda explotación indígena». ¿Qué continuidad ignora?", "La encomienda y la mita persistieron y los abusos continuaron", "La clase lo señala."),
        ("¿Por qué el territorio es clave para entender la aplicación de las leyes?", "Porque la distancia entre España y América debilitaba el control del rey", "Las autoridades locales actuaban según sus intereses."),
    ],
    [
        ("Ordena de más antiguo a más reciente: A = Valladolid (1550-1551), B = Leyes de Burgos (1512), C = Leyes Nuevas (1542).", "B, C, A", "Las fechas en orden son 1512, 1542 y 1550."),
        arith("Una comunidad de ejemplo tenía 1.000 personas y 300 fueron protegidas por las Leyes Nuevas. ¿Cuántas no fueron protegidas?", "1000-300", "Se restan las protegidas del total."),
    ],
    [("Un cuadro de ejemplo dice: «1512: Leyes de Burgos. 1542: Leyes Nuevas. 1550: Valladolid». ¿Qué hecho de la tabla es el último y en qué ciudad ocurre?", "El debate de Valladolid; Valladolid", "1550 es la fecha más reciente y ocurre en esa ciudad.")],
    [("¿Qué eran las Leyes Nuevas?", "Leyes de 1542 que prohibieron esclavizar indígenas y limitaron la encomienda hereditaria", "Está en el vocabulario."), ("¿Qué cambió con el debate?", "Se reconoció que los indígenas eran personas libres con derechos", "Se explicó en el segundo párrafo."), ("¿Qué continuó después de las leyes?", "La conquista, la encomienda y la mita", "Se explicó en el segundo párrafo.")],
    (
        "Completa una tabla con dos columnas, cambio y continuidad, y tres filas con hechos de la clase. Al final escribe una frase que explique por qué la distancia entre España y América importa.",
        "Cambio: reconocimiento de derechos; Leyes de Burgos; Leyes Nuevas. Continuidad: encomienda; mita; abusos. La distancia debilitaba el control del rey.",
        ["completa las dos columnas con hechos de la clase", "explica el papel del territorio"],
        ["tabla de tres filas y una frase"],
        ["decir que las leyes terminaron los abusos", "olvidar la distancia"],
        "Explica a una persona de tu casa por qué una ley puede no cumplirse.",
    ),
    "Dibuja una línea de tiempo con las tres fechas de la clase y un hecho en cada una.",
    "Escribe una pregunta sobre cómo reaccionaron las comunidades indígenas a las leyes.",
)

# ================================================================ clase 4
lesson(
    OA, 4,
    "Aprenderé a contrastar las posturas de Sepúlveda, Las Casas y Vitoria sobre la legitimidad de la conquista y a fundamentar por qué ese debate importa para los derechos humanos de hoy. Sirve para entender el origen de ideas sobre la dignidad de toda persona.",
    ["Conozco las fuentes y los cambios del debate.", "Sé qué son los derechos humanos."],
    [
        "Las tres posturas principales fueron distintas. Juan Ginés de Sepúlveda sostuvo que la conquista podía ser justa porque, según él, algunos pueblos eran inferiores o practicaban costumbres condenables, y debían ser guiados por los españoles. Bartolomé de las Casas sostuvo que los indígenas eran seres racionales y libres, que la conquista violenta era injusta y que la evangelización debía hacerse por la persuasión, no por la fuerza. Francisco de Vitoria afirmó que los indígenas eran dueños legítimos de sus tierras y de sus personas, y que la diferencia de religión no justificaba la guerra.",
        "Cada postura se apoyaba en causas distintas: intereses de colonos y de la Corona, creencias religiosas, y la observación de lo que ocurría en América. Hoy sabemos que las ideas de Sepúlveda se basaban en prejuicios, mientras que las de Las Casas y Vitoria reconocían una dignidad igual de todos los seres humanos.",
        "Este debate importa para los derechos humanos. Aunque no existía ese nombre, se discutió si todos los seres humanos tienen derechos por el hecho de serlo, sin importar su religión, su cultura o su poder. Esa idea inspiró a quienes después defendieron la igualdad y la libertad, y se reflejó en la Declaración Universal de Derechos Humanos, aprobada por la ONU en 1948. Sin embargo, no hay una línea recta entre el siglo XVI y hoy; hubo avances, retrocesos y muchas otras influencias.",
    ],
    [("racional", "capaz de pensar y de tomar decisiones por sí mismo"), ("dignidad", "valor que tiene toda persona por el hecho de serlo"), ("prejuicio", "juicio negativo sobre alguien sin conocerlo bien"), ("persuasión", "convencer a alguien con razones y sin violencia"), ("Declaración Universal de Derechos Humanos", "documento aprobado por la ONU en 1948 que reconoce los derechos de todas las personas")],
    [
        ("Contrastar posturas", "Sepúlveda decía que la conquista podía ser justa y Las Casas que era injusta. ¿Qué los diferencia?", ["Uno justifica la conquista.", "El otro la considera injusta."], "Que Sepúlveda la justificaba y Las Casas la consideraba injusta"),
        ("Fundamentar relevancia", "¿Qué idea del debate se relaciona con los derechos humanos?", ["La clase habla de la dignidad de todos.", "Es la idea de derechos por ser persona."], "Que todas las personas tienen derechos por el hecho de serlo"),
    ],
    [
        ("Creer que todos los españoles pensaban lo mismo.", "Hubo posturas muy distintas, como las de Sepúlveda y Las Casas.", "Compara dos autores."),
        ("Pensar que el debate del siglo XVI creó directamente los derechos humanos.", "Hubo influencias, pero también muchos otros procesos entre medio.", "Habla de influencia, no de causa única."),
    ],
    [
        ("¿Qué sostenía Las Casas sobre los indígenas?", "Que eran seres racionales y libres", "Se dice en el primer párrafo."),
        ("¿Qué afirmó Vitoria sobre las tierras de los indígenas?", "Que eran sus dueños legítimos", "Se dice en el primer párrafo."),
        ("¿En qué año aprobó la ONU la Declaración Universal de Derechos Humanos?", "En 1948", "Se dice en el tercer párrafo."),
    ],
    [
        ("¿Qué es la dignidad?", "El valor que tiene toda persona por el hecho de serlo", "Está en el vocabulario."),
        ("¿Por qué las ideas de Sepúlveda se basaban en prejuicios?", "Porque suponía que algunos pueblos eran inferiores sin conocerlos bien", "Se explicó en el segundo párrafo."),
        ("¿Qué decía Las Casas sobre la evangelización?", "Que debía hacerse por persuasión y no por la fuerza", "Se dice en el primer párrafo."),
    ],
    [
        arith("Si Sepúlveda escribió su obra hacia 1544 y Las Casas su Brevísima relación se publicó en 1552, ¿cuántos años hay entre ambas?", "1552-1544", "Se resta el año menor al mayor."),
        arith("Entre el debate de Valladolid (1550) y la Declaración Universal de Derechos Humanos (1948), ¿cuántos años pasaron?", "1948-1550", "Se resta el año menor al mayor."),
        ("Una persona de ejemplo dice: «Todos tenemos derechos aunque pensemos distinto». ¿Qué postura del siglo XVI se parece más a esa idea?", "La de Las Casas o Vitoria", "Reconocían derechos sin importar la religión."),
    ],
    [
        ("Un estudiante dice: «Los derechos humanos nacieron en 1948 sin ninguna influencia anterior». ¿Qué error comete?", "Ignora que ideas anteriores, como las del debate del siglo XVI, influyeron", "La clase habla de influencias previas."),
        ("¿Por qué no se puede decir que el debate del siglo XVI llevó directamente a la declaración de 1948?", "Porque entre medio hubo avances, retrocesos y muchas otras influencias", "No hay una línea recta."),
    ],
    [
        ("Ordena de la postura que más justificaba la conquista a la que más defendía a los indígenas: A = Las Casas, B = Sepúlveda.", "B, A", "Sepúlveda la justificaba y Las Casas la criticaba."),
        arith("Una encuesta de ejemplo a 50 estudiantes muestra que 38 creen que los derechos humanos valen para todos. ¿Cuántos no lo creen?", "50-38", "Se restan los que lo creen del total."),
    ],
    [("Fuente 1 (Sepúlveda): «Los pueblos inferiores deben ser guiados». Fuente 2 (Las Casas): «Los indios son hombres libres». ¿Qué idea de dignidad aparece en la fuente 2?", "Que los indígenas son personas libres con dignidad", "Reconoce su libertad y condición de personas.")],
    [("¿Qué es un prejuicio?", "Un juicio negativo sobre alguien sin conocerlo bien", "Está en el vocabulario."), ("¿Qué documento de 1948 reconoce los derechos de todos?", "La Declaración Universal de Derechos Humanos", "Está en el vocabulario."), ("¿Qué quiere decir contrastar posturas?", "Comparar lo que sostiene cada autor y por qué", "Se explicó en la clase.")],
    (
        "Escribe una tabla con tres autores (Sepúlveda, Las Casas y Vitoria). Para cada uno anota su postura sobre la legitimidad de la conquista y un argumento. Termina con un párrafo de tres líneas que explique por qué este debate es relevante para los derechos humanos de hoy.",
        "Sepúlveda: la conquista puede ser justa; algunos pueblos son inferiores. Las Casas: la conquista violenta es injusta; los indígenas son libres. Vitoria: los indígenas son dueños de sus tierras. Relevancia: se discutió que todas las personas tienen derechos por serlo.",
        ["resume las tres posturas", "incluye un argumento por autor", "explica la relevancia para los derechos humanos"],
        ["tabla de tres filas y un párrafo"],
        ["atribuir posturas al autor equivocado", "decir que el debate creó los derechos humanos solo"],
        "Conversa con una persona de tu casa sobre qué derechos le parecen más importantes hoy.",
    ),
    "Escribe un diálogo de seis líneas entre Sepúlveda y Las Casas.",
    "Escribe una pregunta sobre cómo se protege hoy a los pueblos indígenas.",
)

"""Cuaderno del estudiante, 2.º medio Historia, Geografía y Ciencias Sociales: OA 16 (dictadura, supresión del Estado de derecho y defensa de las víctimas) y OA 17 (modelo neoliberal y sus consecuencias sociales)."""
from __future__ import annotations

from hi5_lib import build

# ================================================================ OA 16, clase 1
OA = "HI2M OA 16"
AVISO = "Si este tema te produce malestar, avisa a una persona adulta de confianza (en el colegio o en tu casa); no necesitas contar nada personal."
F = ("Ficha 1 (hechos reconocidos; solo lees y analizas, sin exponerte personalmente). "
     "El 11 de septiembre de 1973 las Fuerzas Armadas y de Orden derrocaron al presidente Salvador Allende y formaron una Junta Militar. "
     "Después, el Congreso Nacional dejó de funcionar, los partidos políticos fueron prohibidos o puestos en receso y se restringió la libertad de prensa. "
     "Estado de derecho: situación en que la ley limita el poder, hay una Constitución, los poderes del Estado se controlan entre sí y se respetan los derechos de las personas. "
     "Instituciones de defensa: el Comité Pro Paz, creado en 1973 por iglesias, y la Vicaría de la Solidaridad, creada en 1976 por la Iglesia Católica; también organizaciones civiles de familiares de detenidos desaparecidos, formadas durante los años setenta. "
     "Informes oficiales posteriores (Comisión Rettig, 1991; Comisión Valech, 2004) reconocieron a miles de víctimas de ejecuciones, desapariciones forzadas, prisión política y tortura. " + AVISO)
build(
    OA, 1, F,
    use="Aprenderé a situar en el tiempo la dictadura militar chilena y a distinguir a sus actores: quienes tomaron el poder y quienes defendieron a las víctimas. Sirve para entender por qué se dice que se suprimió el Estado de derecho.",
    prior=["Sé que el 11 de septiembre de 1973 hubo un golpe de Estado en Chile.", "Sé qué es una Constitución y que existen tres poderes del Estado.", "Sé leer una fuente con autor y fecha."],
    explain=[
        "Una dictadura es un gobierno que concentra el poder sin elecciones libres ni controles. En Chile comenzó el 11 de septiembre de 1973, cuando las Fuerzas Armadas y de Orden derrocaron al presidente y una Junta Militar tomó el mando. Un golpe de Estado es el derrocamiento de un gobierno por la fuerza, fuera de los caminos que fija la Constitución.",
        "El Estado de derecho es el orden en que la ley limita al poder: hay Constitución, los poderes se controlan entre sí y se respetan los derechos de las personas. Al cerrarse el Congreso, prohibirse los partidos y restringirse la prensa, se suprimieron esos controles. Suprimir significa eliminar. Además, ninguna autoridad independiente podía frenar abusos, y por eso se produjeron violaciones sistemáticas de derechos humanos, es decir, repetidas y organizadas desde el Estado.",
        "Frente a esto actuaron instituciones civiles y religiosas que procuraron defender a las víctimas: el Comité Pro Paz (1973) y luego la Vicaría de la Solidaridad (1976) entregaron ayuda legal y apoyo a familias, y organizaciones civiles de familiares de detenidos desaparecidos exigieron información. Las violaciones están reconocidas en informes oficiales posteriores, como los de las comisiones Rettig (1991) y Valech (2004). Estudiar este tema exige rigor y respeto: se trabaja con hechos reconocidos y fuentes, sin detalles gráficos. Si algo te afecta, avisa a una persona adulta de confianza.",
    ],
    vocab=[("dictadura", "gobierno que concentra el poder sin elecciones libres ni controles"), ("golpe de Estado", "derrocamiento de un gobierno por la fuerza, fuera de lo que permite la Constitución"), ("Estado de derecho", "orden en que la ley limita al poder y se respetan los derechos de las personas"), ("suprimir", "eliminar algo que existía"), ("violación sistemática", "daño repetido y organizado, no un hecho aislado"), ("desaparición forzada", "detención de una persona por agentes del Estado seguida de la negativa a informar su paradero")],
    worked=[
        ("Ubicar un actor", "El Comité Pro Paz fue creado en 1973 por iglesias. ¿Fue una medida de la Junta o una institución de defensa?", ["Leo quién lo creó: iglesias.", "Su fin fue ayudar a personas afectadas, no gobernar."], "Fue una institución de defensa de las víctimas"),
        ("Reconocer un control que desaparece", "Si ningún tribunal ni órgano independiente puede revisar una orden de la Junta, ¿qué elemento del Estado de derecho falta?", ["El Estado de derecho exige que los poderes se controlen entre sí.", "Aquí nadie controla la orden."], "Falta el control entre los poderes del Estado"),
    ],
    mistakes=[("Escribir que el Estado de derecho es solo tener leyes.", "Una dictadura también puede dictar normas; lo que cambia es que nadie limita al poder.", "Revisa los cuatro rasgos: Constitución, control entre poderes, derechos respetados y ley que limita al poder."),
              ("Creer que la defensa de las víctimas la hizo el gobierno de la Junta.", "Se confunde a quienes tenían el poder con quienes lo cuestionaron.", "Pregunta siempre quién crea la institución y para qué.")],
    T=[
        ("{F} ¿En qué fecha comenzó la dictadura según la ficha?", "El 11 de septiembre de 1973", "La ficha fecha el derrocamiento del presidente Allende."),
        ("{F} ¿Qué órgano formaron las Fuerzas Armadas y de Orden después de derrocar al presidente?", "Una Junta Militar", "La ficha lo indica."),
        ("{F} ¿Qué institución fue creada en 1976 por la Iglesia Católica?", "La Vicaría de la Solidaridad", "La ficha la presenta con ese año y ese creador."),
        ("En Historia: ¿qué es un golpe de Estado?", "El derrocamiento de un gobierno por la fuerza, fuera de lo que permite la Constitución", "Es la definición del vocabulario de la clase."),
        ("Clasifica: (a) el Congreso deja de funcionar; (b) iglesias crean un comité de ayuda legal. ¿Cuál es una medida del poder y cuál una acción de defensa?", "(a) medida del poder; (b) acción de defensa", "Cerrar el Congreso concentra poder; el comité ayuda a las personas afectadas."),
        ("{F} ¿Qué diferencia hay entre el Comité Pro Paz y una organización civil de familiares de detenidos desaparecidos? A) El Comité fue creado por iglesias y la organización de familiares por los propios afectados y sus cercanos B) El Comité era parte de la Junta y la organización no", "A) El Comité fue creado por iglesias y la organización de familiares por los propios afectados y sus cercanos", "Ambas defendieron a las víctimas, pero desde actores distintos: religiosos y civiles."),
        ("Una organización de iglesias entrega asesoría legal gratuita a personas perseguidas. ¿Qué tipo de actor es? A) Una institución religiosa de defensa de derechos B) Un órgano de gobierno de la Junta", "A) Una institución religiosa de defensa de derechos", "Creada por iglesias para defender, no para gobernar."),
        ("Un decreto de ejemplo prohíbe a los partidos reunirse y a los diarios criticar al gobierno. ¿Qué derecho afecta? A) La libertad de asociarse y de informarse B) El derecho a la educación gratuita", "A) La libertad de asociarse y de informarse", "Reunirse en partidos es asociarse y criticar en la prensa es informar y opinar."),
        ("Nadie puede revisar las leyes que dicta una autoridad que gobierna sola. ¿Qué elemento del Estado de derecho falta? A) El control entre los poderes del Estado B) Una Constitución con muchos artículos", "A) El control entre los poderes del Estado", "Sin otro poder que revise, la ley no limita al poder."),
        ("Explica por qué cerrar el Congreso y prohibir los partidos afecta los derechos de las personas.", "Porque se limita la posibilidad de elegir, opinar y participar, que son derechos políticos", "Sin Congreso ni partidos no hay representación ni control del poder."),
        ("{F} Una compañera dice: «La Vicaría de la Solidaridad fue un organismo de la Junta». ¿Qué dato de la ficha lo contradice?", "Que fue creada por la Iglesia Católica", "La ficha nombra a la Iglesia Católica como creadora, no a la Junta."),
        ("Alguien afirma: «Como existían instituciones de defensa, el Estado de derecho no se suprimió». Evalúa. A) Es débil: la defensa surgió porque faltaban garantías, y su existencia no prueba que el Estado de derecho funcionara B) Es correcta: si hay quien defiende, hay Estado de derecho", "A) Es débil: la defensa surgió porque faltaban garantías, y su existencia no prueba que el Estado de derecho funcionara", "Confunde la reacción de la sociedad civil con el funcionamiento del orden legal."),
        ("¿Cuál es la mejor pregunta para investigar este tema? A) ¿Cómo se suprimió el Estado de derecho y quiénes defendieron a las víctimas? B) ¿Qué década fue la más difícil de la historia?", "A) ¿Cómo se suprimió el Estado de derecho y quiénes defendieron a las víctimas?", "La A tiene tema, lugar y se responde con fuentes; la B es una opinión sin criterio."),
    ],
    ctx=("Un compañero prepara un afiche con el título «En 1973 se cerraron el Congreso y los partidos, y la Iglesia ayudó a las familias». ¿Qué debe agregar para situar bien el tema? A) El año y quién tomó el poder B) Su opinión sobre cada líder", "A) El año y quién tomó el poder", "Situar es ubicar tiempo y actores; la opinión no cumple esa tarea."),
    sc=[("¿Qué significa suprimir el Estado de derecho?", "Eliminar los controles que limitan al poder y garantizan derechos", "Es lo que ocurre al cerrarse el Congreso y restringirse la prensa."),
        ("¿Cuál de estas instituciones de defensa fue creada por la Iglesia Católica en 1976? A) La Vicaría de la Solidaridad B) El Comité Pro Paz", "A) La Vicaría de la Solidaridad", "El Comité Pro Paz se creó en 1973 por iglesias."),
        ("¿Qué debes hacer si este tema te produce malestar?", "Avisar a una persona adulta de confianza", "No hace falta exponerse; se pide apoyo.")],
    op=("Dibuja una línea de tiempo con tres marcas: 11 de septiembre de 1973 (golpe de Estado), 1973 (Comité Pro Paz) y 1976 (Vicaría de la Solidaridad). Debajo escribe dos frases: una que diga qué es el Estado de derecho y otra que explique qué cambió cuando se cerró el Congreso. No incluyas relatos personales. {F}",
        "Frases: «El Estado de derecho es el orden en que la ley limita al poder y se respetan los derechos»; «Al cerrarse el Congreso desapareció un control sobre el poder».",
        ["ubica las tres marcas", "define el Estado de derecho con sus palabras", "explica un cambio concreto"], ["línea de tiempo", "dos frases"], ["confundir quién tomó el poder con quién defendió", "definir Estado de derecho solo como «tener leyes»"],
        "Pide que justifique con la ficha quién creó cada institución."),
    reinforce="Explica a alguien de tu casa, en tres frases y sin detalles gráficos, qué significa suprimir el Estado de derecho.",
    extend="Busca en tu colegio o en tu casa un ejemplo de regla que limite a quien manda y explica por qué es un control.",
)

# ================================================================ OA 16, clase 2
F = ("Ficha 2 (tres fuentes de ejemplo escritas para este cuaderno; no son documentos reales). "
     "Fuente A, comunicado de ejemplo de una autoridad de la Junta, 1974: «Se mantiene el orden y la tranquilidad en todo el país. Las medidas protegen a la población.» "
     "Fuente B, carta de ejemplo de una familiar a una institución de defensa, 1975: «Un familiar fue detenido y desde entonces no tenemos información oficial sobre dónde está. Pedimos ayuda para que un tribunal lo busque.» "
     "Fuente C, texto de ejemplo de un informe de una comisión oficial creada en 1990, escrito después: «Se reunieron declaraciones y documentos para establecer qué ocurrió en los casos de muerte y desaparición.» "
     "Preguntas de procedencia: ¿quién la escribió, cuándo, para quién y para qué? " + AVISO)
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes sobre la dictadura preguntando por su procedencia: autor, fecha, destinatario y propósito. Sirve para no tratar ninguna fuente como un relato neutral.",
    prior=["Sé que una fuente es una huella del pasado.", "Sé qué es el Estado de derecho.", "Sé distinguir un hecho de una opinión."],
    explain=[
        "La procedencia de una fuente es su origen: quién la escribió, cuándo, para quién y con qué propósito. Una fuente oficial, como un comunicado de una autoridad, muestra cómo el gobierno quería presentar sus actos; no es una descripción neutral. Una carta de una familiar muestra una experiencia y una petición; es un testimonio, y su valor está en lo que revela de esa situación.",
        "Un informe escrito después por una comisión oficial reúne declaraciones y documentos para establecer lo ocurrido; es una fuente secundaria respecto de los hechos, porque se elabora tiempo después. Para valorar cada fuente se compara lo que dice con otras y se pregunta qué silencia. Que dos fuentes distintas coincidan en un hecho le da más solidez que una sola.",
        "Interrogar una fuente no es aceptarla ni rechazarla: es preguntar qué prueba y qué no. Un comunicado prueba qué decía la autoridad; no prueba, por sí solo, que todo lo dicho fuera cierto. Una carta prueba que alguien pidió ayuda; no sustituye otros documentos. Trabaja con respeto y, si algo te afecta, avisa a una persona adulta de confianza.",
    ],
    vocab=[("procedencia", "origen de una fuente: autor, fecha, destinatario y propósito"), ("fuente oficial", "documento de una autoridad del Estado"), ("testimonio", "relato de quien vivió o conoció un hecho"), ("comisión", "grupo de personas encargado de investigar un asunto y entregar un informe"), ("contrastar", "comparar lo que dicen varias fuentes sobre un mismo hecho")],
    worked=[
        ("Identificar el propósito", "Una autoridad publica un aviso que dice «todo está en calma». ¿Qué propósito probable tiene?", ["Quien escribe es la autoridad que gobierna.", "Quiere dar una imagen de orden a la población."], "Mostrar una imagen de orden y dar tranquilidad a la población"),
        ("Decir qué prueba una fuente", "Una carta de un vecino pide a un tribunal que busque a un familiar. ¿Qué prueba la carta y qué no?", ["Prueba que alguien hizo esa petición.", "Por sí sola no prueba el resto de los hechos; hay que contrastarla."], "Prueba la petición; los demás hechos se contrastan con otras fuentes"),
    ],
    mistakes=[("Tratar un comunicado oficial como un relato neutral de lo ocurrido.", "Se olvida que quien escribe tiene un propósito y una posición.", "Pregunta siempre quién lo escribe, cuándo y para qué."),
              ("Descartar una carta personal porque «es solo una persona».", "Se confunde testimonio con fuente sin valor.", "Valora qué revela de esa situación y contrástala con otras fuentes.")],
    T=[
        ("{F} ¿Qué fuente de la ficha escribió una autoridad de la Junta?", "La Fuente A", "Se identifica por su autor, indicado en la ficha."),
        ("{F} ¿En qué año se escribió la carta de la Fuente B?", "1975", "La ficha da su fecha."),
        ("En Historia: ¿qué es la procedencia de una fuente?", "Su origen: quién la escribió, cuándo, para quién y con qué propósito", "Es la definición que se usa en la clase."),
        ("{F} ¿Qué tipo de fuente es la Fuente B? A) Un testimonio B) Un comunicado oficial", "A) Un testimonio", "Es la carta de una persona que pide ayuda por una situación que conoce."),
        ("{F} ¿Por qué la Fuente C se considera una fuente escrita después de los hechos?", "Porque la comisión se creó en 1990 y elaboró su informe tiempo más tarde", "La ficha indica que se creó en 1990, años después de 1973."),
        ("{F} ¿Cuál es el propósito probable de la Fuente A? A) Dar una imagen de orden y tranquilidad B) Pedir a un tribunal que busque a una persona", "A) Dar una imagen de orden y tranquilidad", "Un comunicado de la autoridad busca mostrar su gestión."),
        ("Un compañero cita la Fuente A y concluye: «Entonces no hubo ningún problema en el país». ¿Qué le respondes? A) Que la fuente prueba lo que la autoridad decía, no que fuera todo cierto B) Que si es oficial, siempre es cierta", "A) Que la fuente prueba lo que la autoridad decía, no que fuera todo cierto", "Una fuente oficial tiene un propósito y debe contrastarse."),
        ("Quieres comprobar el contenido de la Fuente B. ¿Qué haces? A) La comparas con otros documentos y testimonios sobre el mismo hecho B) La descartas porque la escribió una sola persona", "A) La comparas con otros documentos y testimonios sobre el mismo hecho", "Contrastar da solidez a la conclusión."),
        ("{F} Ordena de la más cercana a los hechos a la más tardía: Fuente C, Fuente A, Fuente B.", "Fuente A (1974), Fuente B (1975), Fuente C (después de 1990)", "Se ordenan por la fecha de cada una."),
        ("Explica por qué el comunicado y la carta no se pueden tratar como relatos neutrales.", "Porque cada autor escribe desde una posición y con un propósito: uno quiere mostrar orden y el otro pedir ayuda", "La procedencia influye en lo que se dice y en lo que se calla."),
        ("{F} ¿Qué silencia la Fuente A que sí aparece en la Fuente B?", "La falta de información sobre el paradero de una persona detenida", "La A habla de tranquilidad y la B de una persona sin información oficial."),
        ("Una afirmación dice: «Si la comisión se creó en 1990, su informe no sirve porque fue tarde». Evalúa. A) Es débil: un informe posterior reúne documentos y declaraciones y se contrasta con otras fuentes B) Es correcta: solo valen las fuentes de la época", "A) Es débil: un informe posterior reúne documentos y declaraciones y se contrasta con otras fuentes", "Una fuente tardía tiene límites, pero reúne evidencia que no estaba disponible antes."),
        ("{F} ¿Qué conclusión se sostiene mejor con las tres fuentes? A) Hay versiones distintas del mismo período que deben contrastarse B) La Fuente A explica todo lo ocurrido", "A) Hay versiones distintas del mismo período que deben contrastarse", "Cada fuente tiene propósito distinto; ninguna basta sola."),
    ],
    ctx=("En una investigación escolar solo tienes un comunicado oficial de ejemplo de 1974. ¿Qué fuente buscarías para contrastarlo? A) Una carta o testimonio de la misma época y un informe posterior B) Otro comunicado de la misma autoridad", "A) Una carta o testimonio de la misma época y un informe posterior", "Para contrastar se necesitan fuentes con otra procedencia."),
    sc=[("¿Qué cuatro preguntas forman la procedencia?", "Quién la escribió, cuándo, para quién y para qué", "Son los cuatro elementos de la definición."),
        ("¿Qué prueba un comunicado oficial por sí solo?", "Lo que la autoridad decía, no que todo fuera cierto", "Tiene un propósito y debe contrastarse."),
        ("¿Qué haces si un testimonio te produce malestar?", "Aviso a una persona adulta de confianza", "Se pide apoyo sin exponerse.")],
    op=("Elige dos de las tres fuentes de la ficha. En una tabla escribe, para cada una: quién la escribió, cuándo, para qué, qué prueba y qué silencia. Termina con una frase que diga qué conclusión sí puedes sostener con ambas y qué no. {F}",
        "Fuente A: autoridad de la Junta, 1974, dar imagen de orden, prueba lo que se decía, silencia a quienes no tenían información. Fuente B: familiar, 1975, pedir ayuda, prueba la petición, no prueba otros hechos. Conclusión: hay versiones distintas que deben contrastarse.",
        ["completa los cinco campos para ambas fuentes", "distingue lo que prueban y lo que no", "formula una conclusión proporcional"], ["tabla", "una frase de conclusión"], ["tratar la fuente oficial como neutral", "generalizar desde una sola carta"],
        "Pide que diga qué otra fuente agregaría para contrastar."),
    reinforce="Explica a alguien de tu casa por qué un aviso oficial no es un relato neutral, sin tocar detalles dolorosos.",
    extend="Piensa en un mensaje que recibas de una institución y di quién lo escribe y para qué.",
)

# ================================================================ OA 16, clase 3
F = ("Ficha 3 (perspectivas de ejemplo sobre un mismo período; las citas son de ejemplo). "
     "Perspectiva 1, autoridad de la Junta, 1975: «Las medidas de excepción son necesarias para mantener el orden.» "
     "Perspectiva 2, institución de defensa de las víctimas, 1977: «Ninguna medida de excepción justifica detener a personas sin informar a sus familias ni permitir que un tribunal las revise.» "
     "Perspectiva 3, familiar de una persona afectada, 1976: «Mi familia busca respuestas y recurre a quien pueda ayudarnos.» "
     "Escalas: local (una familia o barrio), nacional (el país y sus instituciones), internacional (organismos de derechos humanos de otros países y de organizaciones internacionales). "
     "Hecho reconocido: el Estado de derecho fue suprimido y se violaron derechos humanos de manera sistemática. " + AVISO)
build(
    OA, 3, F,
    use="Aprenderé a comparar perspectivas y escalas sobre la dictadura: qué dice cada actor, desde dónde y a qué nivel. Sirve para entender el período sin confundir una perspectiva con un hecho comprobado.",
    prior=["Sé interrogar la procedencia de una fuente.", "Sé que hubo violaciones sistemáticas de derechos humanos.", "Sé distinguir hecho y opinión."],
    explain=[
        "Una perspectiva es el punto de vista desde el que alguien describe un hecho, según su posición, sus intereses y su experiencia. Comparar perspectivas no significa que todas sean igualmente ciertas. Significa preguntar qué afirma cada actor, con qué evidencia y qué deja fuera. Hay hechos comprobados por documentos y fuentes, y hay justificaciones o interpretaciones que se contrastan con ellos.",
        "En este período una autoridad justificaba sus medidas diciendo que mantenían el orden; una institución de defensa respondía que ninguna medida justifica detener sin informar ni sin control de un tribunal; un familiar buscaba respuestas. Explicar por qué alguien dice algo no es justificarlo. Lo que sostiene el análisis es la evidencia: se reconoce que se violaron sistemáticamente derechos humanos.",
        "Una escala es el nivel desde el que se mira: local, nacional o internacional. A escala local se ve la experiencia de una familia; a escala nacional, las decisiones del Estado y las instituciones; a escala internacional, la mirada de organismos de otros países. Cambiar de escala cambia lo que se ve, por eso conviene usar varias.",
    ],
    vocab=[("perspectiva", "punto de vista desde el que alguien describe un hecho"), ("justificar", "dar razones para decir que algo estuvo bien; es distinto de explicar por qué ocurrió"), ("escala", "nivel desde el que se mira un hecho: local, nacional o internacional"), ("medida de excepción", "norma que limita derechos de manera temporal por una situación declarada grave"), ("organismo internacional", "institución formada por varios países o por organizaciones de distintos países")],
    worked=[
        ("Identificar escala", "Una carta cuenta cómo una familia buscó ayuda en su barrio. ¿Qué escala muestra?", ["Habla de una familia y su entorno cercano.", "No habla del país entero."], "Escala local"),
        ("Explicar sin justificar", "Un historiador escribe por qué la Junta dijo que buscaba mantener el orden. ¿Está justificando?", ["Explicar es dar las razones que alguien expuso.", "Justificar es decir que esas razones eran correctas; el historiador no lo hace si las contrasta con evidencia."], "No: explica la razón de la autoridad y la contrasta con evidencia"),
    ],
    mistakes=[("Pensar que comparar perspectivas significa que todas valen lo mismo.", "Se confunde el respeto por distintas voces con aceptar cualquier afirmación sin evidencia.", "Contrasta cada afirmación con documentos y fuentes."),
              ("Creer que explicar una justificación equivale a compartirla.", "No se distingue entender el argumento de aprobarlo.", "Di «la autoridad sostuvo que…» y luego muestra qué evidencia lo apoya o lo contradice.")],
    T=[
        ("{F} ¿Qué dice la Perspectiva 1 sobre las medidas de excepción?", "Que son necesarias para mantener el orden", "La ficha lo cita."),
        ("{F} ¿Quién expresa la Perspectiva 2?", "Una institución de defensa de las víctimas", "La ficha indica su procedencia."),
        ("En Historia: ¿qué es una escala?", "El nivel desde el que se mira un hecho: local, nacional o internacional", "Es la definición de la clase."),
        ("{F} La Perspectiva 3 muestra la experiencia de una familia. ¿Qué escala predomina? A) Local B) Nacional", "A) Local", "Una familia es un nivel cercano, no el del país ni el de otros países."),
        ("{F} ¿Cuál de estas frases es un hecho reconocido según la ficha? A) El Estado de derecho fue suprimido B) Las medidas de excepción eran necesarias", "A) El Estado de derecho fue suprimido", "La B es la justificación de una perspectiva; la ficha presenta la A como hecho reconocido."),
        ("Una autoridad dice que sus medidas protegen a la población. ¿Qué debes hacer para evaluar eso? A) Contrastarlo con documentos y otras fuentes B) Aceptarlo porque lo dice la autoridad", "A) Contrastarlo con documentos y otras fuentes", "La procedencia exige contrastar."),
        ("Un organismo de otro país publica un informe sobre derechos humanos en Chile. ¿Qué escala usa? A) Internacional B) Local, porque trata sobre Chile", "A) Internacional", "Es una mirada desde fuera del país."),
        ("Clasifica por escala: (a) un decreto que rige en todo el país; (b) la experiencia de un vecino del barrio.", "(a) nacional; (b) local", "Un decreto alcanza a todo el país y la vivencia de un vecino es cercana."),
        ("{F} Un compañero dice: «Explicar por qué la autoridad habló de orden es lo mismo que justificarla». ¿Qué corriges?", "Que explicar es dar sus razones y contrastarlas con evidencia; justificar sería decir que eran correctas", "La diferencia está en aprobar o no el argumento."),
        ("{F} ¿Qué diferencia hay entre la Perspectiva 1 y la 2 en cuanto a los límites de las medidas de excepción?", "La 1 las considera necesarias; la 2 sostiene que ninguna medida justifica detener sin informar ni sin revisión de un tribunal", "Cada una fija límites distintos según la ficha."),
        ("{F} Alguien concluye: «Como hay tres perspectivas, todas son igual de ciertas». Evalúa. A) Es débil: algunos hechos están comprobados por documentos y se contrastan con cada perspectiva B) Es correcta: son perspectivas", "A) Es débil: algunos hechos están comprobados por documentos y se contrastan con cada perspectiva", "Comparar perspectivas no elimina los hechos comprobados."),
        ("Para estudiar la dictadura a escala internacional, ¿qué fuente conviene? A) Un informe de un organismo de otros países B) La carta de una familia del barrio", "A) Un informe de un organismo de otros países", "Esa fuente responde a la escala internacional."),
        ("¿Qué pregunta ayuda a comparar bien dos perspectivas? A) ¿Desde qué posición habla cada una y con qué evidencia? B) ¿Cuál me cae mejor?", "A) ¿Desde qué posición habla cada una y con qué evidencia?", "Solo la A usa criterios que se pueden verificar."),
    ],
    ctx=("En una exposición escolar se muestran solo comunicados oficiales de una época. ¿Qué perspectivas faltan para comparar bien? A) La de instituciones de defensa y la de las familias B) La de más autoridades del mismo gobierno", "A) La de instituciones de defensa y la de las familias", "Comparar exige voces con posiciones distintas."),
    sc=[("¿Qué es una perspectiva?", "El punto de vista desde el que alguien describe un hecho", "Así se define en la clase."),
        ("¿Explicar una justificación es lo mismo que compartirla?", "No, explicar es dar sus razones y contrastarlas", "Se debe contrastar con evidencia."),
        ("Nombra las tres escalas de la clase.", "Local, nacional e internacional", "Son las tres que se explican.")],
    op=("Haz una tabla con tres columnas: perspectiva, escala y qué evidencia necesitarías para contrastarla. Completa las filas con las Perspectivas 1, 2 y 3 de la ficha. Cierra con dos frases: una con un hecho reconocido y otra con una justificación, indicando de quién es. {F}",
        "P1: autoridad, nacional, documentos y fuentes de otras procedencias. P2: institución de defensa, nacional, informes y casos documentados. P3: familiar, local, documentos del caso. Hecho: se suprimió el Estado de derecho. Justificación: la autoridad dijo que había que mantener el orden.",
        ["completa las tres filas", "distingue hecho y justificación", "atribuye cada justificación a su autor"], ["tabla", "dos frases"], ["tratar las tres perspectivas como igualmente comprobadas", "no indicar la escala"],
        "Pide que explique por qué comparar no es justificar."),
    reinforce="Explica a alguien de tu casa la diferencia entre explicar y justificar, con un ejemplo que no sea de este tema.",
    extend="Elige un conflicto de tu curso y di qué ve cada persona a escala local.",
)

# ================================================================ OA 16, clase 4
F = ("Ficha 4 (causas, cambios y continuidades; los datos son hechos reconocidos o ejemplos señalados). "
     "Antes de 1973 había una fuerte polarización política y una crisis (estudiadas en el OA 14). "
     "El 11 de septiembre de 1973 hubo un golpe de Estado. Desde entonces el poder quedó concentrado en la Junta, sin Congreso ni controles. "
     "Instituciones de defensa: Comité Pro Paz (1973) y Vicaría de la Solidaridad (1976). "
     "En 1990 volvió un gobierno elegido y se creó una comisión oficial para establecer lo ocurrido en los casos de muerte y desaparición. "
     "Continuidad de ejemplo: durante toda la dictadura las organizaciones de familiares y las iglesias siguieron pidiendo información. " + AVISO)
build(
    OA, 4, F,
    use="Aprenderé a relacionar causas, cambios y continuidades de la dictadura: cómo la concentración del poder permitió las violaciones y cómo respondió la sociedad hasta 1990. Sirve para distinguir explicar un hecho de justificarlo.",
    prior=["Sé qué es el Estado de derecho y quiénes lo defendieron.", "Sé comparar perspectivas.", "Sé distinguir causa de largo plazo y detonante."],
    explain=[
        "Un hecho histórico tiene causas de largo plazo, un detonante y consecuencias. La crisis y la polarización de comienzos de los años setenta ayudan a explicar el golpe de Estado, pero no lo justifican: explicar es entender por qué ocurrió; justificar sería decir que estuvo bien. Ninguna crisis política justifica violar derechos humanos de manera sistemática.",
        "Un cambio es lo que antes no estaba y apareció; una continuidad es lo que se mantiene. Después de 1973 cambió la forma de gobernar: el poder se concentró sin Congreso ni controles, y eso facilitó las violaciones. Hubo continuidad en la acción de las iglesias y de las organizaciones de familiares, que siguieron pidiendo información durante todo el período.",
        "La vuelta de un gobierno elegido en 1990 abrió otra etapa: se creó una comisión oficial para establecer lo ocurrido. Así, el tema no termina en 1990, porque las consecuencias, como la búsqueda de verdad y de justicia, continuaron. Al escribir, usa palabras como «contribuyó a» o «facilitó», y evita atribuir un hecho a una sola causa. Si el tema te afecta, avisa a una persona adulta de confianza.",
    ],
    vocab=[("causa de largo plazo", "condición que se acumula durante años antes de un hecho"), ("detonante", "hecho que desencadena un proceso que ya tenía causas previas"), ("cambio", "algo nuevo que aparece en un proceso"), ("continuidad", "algo que se mantiene a pesar del cambio"), ("verdad y justicia", "búsqueda de conocer lo ocurrido y de que haya responsabilidad según la ley")],
    worked=[
        ("Clasificar cambio y continuidad", "Tras 1973 el Congreso no funcionó, pero las iglesias siguieron ayudando a familias. ¿Cuál es cambio y cuál continuidad?", ["El Congreso dejó de funcionar: algo nuevo.", "La ayuda de las iglesias se mantuvo durante todo el período."], "Cambio: el Congreso deja de funcionar; continuidad: la ayuda de las iglesias"),
        ("Explicar sin justificar", "Alguien dice: «La polarización explica el golpe, así que lo justifica». ¿Cómo lo corriges?", ["La polarización es una causa que ayuda a entender.", "Explicar no es aprobar y las violaciones sistemáticas no se justifican."], "La polarización explica en parte, pero no justifica las violaciones de derechos humanos"),
    ],
    mistakes=[("Atribuir el golpe de Estado a una sola causa.", "Se simplifica un proceso con varias causas y actores.", "Reúne causas de largo plazo y detonante, y usa «contribuyó a»."),
              ("Creer que todo terminó en 1990.", "Se olvidan las consecuencias que siguen: la búsqueda de verdad y de justicia.", "Pregunta qué cambió y qué continuó después de 1990.")],
    T=[
        ("{F} ¿En qué año se creó la comisión oficial para establecer lo ocurrido en los casos de muerte y desaparición?", "1990", "La ficha lo indica."),
        ("{F} ¿Qué había antes de 1973 según la ficha?", "Una fuerte polarización política y una crisis", "La ficha lo presenta como antecedente."),
        ("{F} ¿Quiénes siguieron pidiendo información durante toda la dictadura, según la ficha?", "Las organizaciones de familiares y las iglesias", "La ficha lo indica como continuidad."),
        ("En Historia: ¿qué es un detonante?", "El hecho que desencadena un proceso que ya tenía causas previas", "Es la definición de la clase."),
        ("{F} Clasifica como cambio o continuidad: (a) el poder se concentra sin Congreso; (b) las iglesias siguen pidiendo información.", "(a) cambio; (b) continuidad", "Lo primero es nuevo después de 1973; lo segundo se mantiene durante el período."),
        ("{F} ¿Cuál de estas es una causa de largo plazo del golpe? A) La polarización y la crisis previas B) La prohibición de los partidos políticos", "A) La polarización y la crisis previas", "La prohibición de los partidos vino después del golpe, como consecuencia."),
        ("{F} ¿Qué cambio ocurrió en 1990 respecto del período anterior? A) Volvió un gobierno elegido y se creó una comisión oficial B) Se cerró el Congreso y se formó una Junta", "A) Volvió un gobierno elegido y se creó una comisión oficial", "El cierre del Congreso y la Junta corresponden a 1973."),
        ("Alguien escribe: «La crisis explica el golpe, por lo tanto las violaciones de derechos humanos estuvieron justificadas». ¿Qué corriges? A) Explicar causas no justifica violar derechos humanos B) Es correcto porque había crisis", "A) Explicar causas no justifica violar derechos humanos", "Una causa ayuda a entender; no da razón para violar derechos."),
        ("Un texto dice: «Desde 1973 el poder se concentró sin controles y eso facilitó las violaciones». ¿Qué palabra marca una relación causal prudente? A) facilitó B) únicamente", "A) facilitó", "«Facilitó» indica contribución sin afirmar una causa única."),
        ("{F} ¿Por qué decir «el golpe ocurrió solo por la polarización» es una explicación débil?", "Porque ignora otras causas y actores, y un proceso así tiene varias causas", "La ficha menciona crisis y polarización, pero no las presenta como causa única."),
        ("{F} ¿Qué evidencia mostraría que hubo continuidad en la defensa de las víctimas entre 1973 y 1990? A) Instituciones y organizaciones que actuaron durante el período B) Un mapa del país", "A) Instituciones y organizaciones que actuaron durante el período", "Es evidencia directa de acciones sostenidas en el tiempo."),
        ("Evalúa: «Con el gobierno elegido de 1990 desapareció todo lo que dejó la dictadura». A) Es excesiva: la búsqueda de verdad y justicia continuó B) Es correcta: 1990 cerró todo", "A) Es excesiva: la búsqueda de verdad y justicia continuó", "Las consecuencias siguieron después de 1990."),
        ("¿Qué síntesis es mejor? A) La concentración del poder facilitó violaciones sistemáticas; hubo cambios (sin Congreso) y continuidades (defensa de las víctimas) hasta 1990 B) Todo se debió a una sola causa y terminó en 1990", "A) La concentración del poder facilitó violaciones sistemáticas; hubo cambios (sin Congreso) y continuidades (defensa de las víctimas) hasta 1990", "Reúne causas, cambios y continuidades sin atribuir una sola causa."),
    ],
    ctx=("En un trabajo escolar se lee: «La crisis causó la dictadura y por eso todo lo que ocurrió fue necesario». ¿Qué dos errores tiene? A) Atribuye una sola causa y confunde explicar con justificar B) Usa palabras difíciles", "A) Atribuye una sola causa y confunde explicar con justificar", "Ambos errores se trabajaron en la clase."),
    sc=[("¿Qué diferencia hay entre cambio y continuidad?", "Cambio es lo nuevo que aparece; continuidad es lo que se mantiene", "Son las dos definiciones de la clase."),
        ("¿Explicar una causa es lo mismo que justificar un hecho?", "No, explicar es entender y justificar es decir que estuvo bien", "Por eso una crisis no justifica violar derechos."),
        ("¿Qué verbo es más prudente en «El poder sin controles ___ las violaciones»? A) facilitó B) fue la única causa de", "A) facilitó", "«Facilitó» indica contribución, no causa única.")],
    op=("Haz un esquema con tres columnas: causas (de largo plazo y detonante), cambios y continuidades, usando los datos de la ficha. Después escribe una frase con «contribuyó a» o «facilitó» y otra que diga por qué explicar no es justificar. No incluyas relatos personales. {F}",
        "Causas: polarización y crisis; detonante: golpe de Estado de 1973. Cambios: poder concentrado sin Congreso. Continuidades: iglesias y familiares piden información. Frases: «La concentración del poder facilitó las violaciones»; «Explicar la crisis no justifica violar derechos humanos».",
        ["clasifica causas, cambios y continuidades", "usa lenguaje causal prudente", "distingue explicar de justificar"], ["esquema", "dos frases"], ["usar una sola causa", "dar por terminado el tema en 1990"],
        "Pide que explique por qué el tema continúa después de 1990."),
    reinforce="Explica a alguien de tu casa la diferencia entre causa de largo plazo y detonante, con un ejemplo cotidiano.",
    extend="Escribe una frase prudente («contribuyó a…») sobre un cambio reciente en tu barrio o escuela.",
)

# ================================================================ OA 17, clase 1
OA = "HI2M OA 17"
F = ("Ficha 1 (hechos generales y datos de ejemplo). "
     "Durante el régimen militar (1973-1990) en Chile se aplicó un modelo económico neoliberal, impulsado por economistas conocidos como «Chicago Boys», formados en una universidad de Estados Unidos. "
     "Rasgos: el libre mercado (los precios y las decisiones dependen de compradores y vendedores) como asignador de recursos; un Estado subsidiario (actúa solo donde los privados no llegan); menos gasto social; apertura comercial (bajar los aranceles, que son impuestos a los productos importados); privatización de empresas públicas; y un nuevo Plan Laboral en 1979. "
     "Actores: la Junta y sus equipos económicos, empresarios, trabajadores y sindicatos, consumidores y el Estado. "
     "Dato de ejemplo: una empresa pública que empleaba 1.000 personas se vende a una empresa privada.")
build(
    OA, 1, F,
    use="Aprenderé a situar el modelo neoliberal chileno en el tiempo y entre sus actores, y a describir sus rasgos principales. Sirve para evaluar después sus consecuencias sociales con criterios.",
    prior=["Sé qué fue el régimen militar y cuándo duró.", "Sé qué es la economía de mercado y el rol del Estado.", "Sé calcular porcentajes sencillos."],
    explain=[
        "El neoliberalismo es una forma de organizar la economía que da prioridad al libre mercado y reduce el papel del Estado como productor y regulador. En Chile se aplicó durante el régimen militar, entre 1973 y 1990, con un equipo de economistas que defendía estas ideas. Se habla de «neoliberal» porque retoma el liberalismo económico del siglo XIX con cambios.",
        "Sus rasgos principales fueron cinco: el libre mercado como asignador de recursos, un Estado subsidiario, menos gasto social, apertura comercial (rebaja de aranceles para que entren más productos importados) y privatización de empresas públicas. En 1979 se cambió además la regulación del trabajo con el Plan Laboral, que modificó las relaciones y los derechos de los trabajadores; por ejemplo, la negociación pasó a hacerse sobre todo dentro de cada empresa.",
        "Estos cambios los tomaron un gobierno sin elecciones libres ni Congreso, y por eso se debate cómo se aplicaron. Los actores tenían intereses distintos: los empresarios, los trabajadores y sindicatos, los consumidores y el Estado no ganaron ni perdieron lo mismo. Describir el modelo no es aprobarlo ni rechazarlo: es el primer paso para evaluarlo con criterios.",
    ],
    vocab=[("neoliberalismo", "forma de organizar la economía que prioriza el libre mercado y reduce el papel del Estado"), ("Estado subsidiario", "Estado que actúa solo donde los privados no llegan"), ("arancel", "impuesto que se cobra a un producto importado"), ("privatización", "traspaso de una empresa pública a manos privadas"), ("apertura comercial", "rebaja de trabas, como los aranceles, para comerciar con otros países"), ("punto porcentual", "diferencia entre dos porcentajes: de 30 % a 10 % hay 20 puntos")],
    worked=[
        ("Reconocer un rasgo", "Una empresa del Estado que producía acero se vende a una empresa privada. ¿Qué rasgo del modelo es?", ["Cambia la propiedad: de pública a privada.", "Ese traspaso es lo que se llama privatización."], "Privatización"),
        ("Aplicar un porcentaje", "Un arancel de ejemplo del 40 % se baja a la mitad. ¿Qué porcentaje queda?", ["La mitad de 40 es 20.", "Un arancel menor facilita importar."], "20 %"),
    ],
    mistakes=[("Decir que el neoliberalismo elimina totalmente al Estado.", "Se confunde Estado subsidiario con ausencia de Estado.", "Recuerda que el Estado actúa donde los privados no llegan."),
              ("Aprobar o rechazar el modelo al describirlo.", "Se mezcla describir con evaluar.", "Primero describe los rasgos con datos; luego evalúa con criterios.")],
    T=[
        ("{F} ¿Entre qué años rigió el régimen militar en que se aplicó el modelo?", "Entre 1973 y 1990", "La ficha lo indica."),
        ("{F} ¿En qué año se aprobó el Plan Laboral?", "1979", "La ficha lo indica."),
        ("En Historia: ¿qué es un arancel?", "Un impuesto que se cobra a un producto importado", "Es la definición del vocabulario."),
        ("{F} ¿Qué es un Estado subsidiario?", "Un Estado que actúa solo donde los privados no llegan", "La ficha lo define así."),
        ("=", "Una empresa pública de ejemplo tenía 1.000 trabajadores y la empresa privada que la compra mantiene al 85 %. ¿Cuántos mantiene?", "1000*85//100", "El 85 % de 1.000 es la cantidad que se mantiene.", " trabajadores"),
        ("{F} Clasifica: (a) vender una empresa del Estado; (b) bajar aranceles. ¿Cuál es privatización y cuál apertura comercial?", "(a) privatización; (b) apertura comercial", "Vender es traspasar a privados; bajar aranceles es abrir el comercio."),
        ("Un país elimina casi todos los aranceles de ejemplo para que entren productos del extranjero. ¿Qué rasgo aplica? A) Apertura comercial B) Estado subsidiario", "A) Apertura comercial", "Rebajar aranceles facilita importar, que es abrir el comercio."),
        ("Los precios del pan los fijan panaderos y clientes sin que el Estado intervenga. ¿Qué idea expresa? A) Libre mercado B) Privatización", "A) Libre mercado", "Los precios dependen de compradores y vendedores."),
        ("{F} ¿Qué actores tenían intereses distintos ante el modelo, según la ficha?", "Empresarios, trabajadores y sindicatos, consumidores y el Estado", "La ficha enumera esos actores."),
        ("Explica por qué en Chile el Estado no desapareció, aunque se aplicó el modelo.", "Porque era subsidiario: seguía actuando donde los privados no llegaban", "La ficha lo define como un Estado que actúa solo donde los privados no llegan."),
        ("{F} Un compañero dice: «El Plan Laboral solo cambió los salarios». ¿Qué corriges?", "Que modificó las relaciones y los derechos de los trabajadores, no solo los salarios", "Cambió la regulación del trabajo, por ejemplo la negociación por empresa, según la explicación."),
        ("Alguien afirma: «El modelo fue bueno porque aumentó los productos disponibles». ¿Qué le falta? A) Evaluar con más criterios, como empleo, desigualdad y acceso a servicios B) Nada, una consecuencia basta", "A) Evaluar con más criterios, como empleo, desigualdad y acceso a servicios", "Una sola consecuencia no basta para evaluar."),
        ("¿Cuál es la mejor pregunta de investigación? A) ¿Qué cambios produjo el modelo neoliberal en Chile y con qué consecuencias para distintos grupos? B) ¿Fue el mejor modelo de la historia?", "A) ¿Qué cambios produjo el modelo neoliberal en Chile y con qué consecuencias para distintos grupos?", "La A se responde con datos y criterios; la B es una opinión."),
    ],
    ctx=("Un afiche escolar dice: «En Chile no hubo Estado entre 1973 y 1990». ¿Qué problema tiene? A) Confunde Estado subsidiario con ausencia de Estado B) Dice que hubo Estado", "A) Confunde Estado subsidiario con ausencia de Estado", "El Estado cambió de rol, pero siguió actuando."),
    sc=[("¿Qué es la privatización?", "El traspaso de una empresa pública a manos privadas", "Así se define en la clase."),
        ("¿Cuál de estas medidas NO corresponde al modelo neoliberal descrito en la clase? A) Subir los aranceles para frenar toda importación B) Vender una empresa del Estado C) Bajar el gasto social", "A) Subir los aranceles para frenar toda importación", "Las otras dos son rasgos de la ficha; el modelo bajó aranceles."),
        ("=", "Un arancel de ejemplo del 30 % baja a 10 %. ¿Cuántos puntos porcentuales bajó?", "30-10", "Se resta el arancel nuevo al antiguo.", " puntos")],
    op=("Haz una tabla con cinco filas, una por cada rasgo del modelo (libre mercado, Estado subsidiario, menos gasto social, apertura comercial, privatización). En cada fila escribe una frase que lo explique y un grupo (empresarios, trabajadores, consumidores o Estado) que se pueda ver afectado. Evita decir si fue bueno o malo. {F}",
        "Apertura comercial: se bajan aranceles; consumidores y empresarios importadores. Privatización: se venden empresas públicas; trabajadores. Libre mercado: precios por oferta y demanda; consumidores. Menos gasto social: Estado reduce servicios; familias de menos recursos. Estado subsidiario: actúa donde no llegan los privados; Estado.",
        ["define cada rasgo con sus palabras", "asocia cada rasgo a un grupo", "no evalúa todavía"], ["tabla de cinco filas"], ["decir que el Estado desaparece", "mezclar describir con evaluar"],
        "Pide que explique por qué describir es distinto de evaluar."),
    reinforce="Explica a alguien de tu casa, con un ejemplo, qué es una privatización y qué es una apertura comercial.",
    extend="Busca en tu casa un producto importado y explica qué efecto pudo tener bajar los aranceles.",
)

# ================================================================ OA 17, clase 2
F = ("Ficha 2 (tres fuentes de ejemplo escritas para este cuaderno; no son documentos reales y sus cifras son de ejemplo). "
     "Fuente A, documento de ejemplo de un equipo económico del régimen, año 1978: «La apertura comercial aumentará la variedad de productos y bajará sus precios; las empresas eficientes crecerán.» "
     "Fuente B, declaración de ejemplo de una organización de trabajadores, año 1980: «Con el nuevo Plan Laboral tenemos menos poder para negociar nuestros salarios y nuestras condiciones.» "
     "Fuente C, tabla de ejemplo de un estudio posterior: en una ciudad de ejemplo, de cada 100 personas con ganas de trabajar, 10 estaban sin empleo en el año 1978 y 20 en el año 1983. "
     "Preguntas de procedencia: ¿quién habla, cuándo, para quién y con qué propósito?")
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes sobre el modelo neoliberal: de quién vienen, qué proponen o critican y qué datos las apoyan. Sirve para no tomar una promesa como si fuera un resultado.",
    prior=["Sé interrogar la procedencia de una fuente.", "Sé qué rasgos tuvo el modelo neoliberal.", "Sé leer una tabla y calcular diferencias."],
    explain=[
        "Las fuentes sobre una política económica tienen distinto valor según su origen. Un documento de quienes diseñan una política expone sus objetivos y promesas, es decir, lo que se espera lograr. Una declaración de una organización de trabajadores expone cómo ven los efectos quienes los viven. Una tabla con datos de un estudio posterior permite medir resultados. Ninguna basta sola.",
        "Hay que distinguir entre una promesa, una percepción y un dato. «Bajarán los precios» es una promesa; «tenemos menos poder para negociar» es una percepción de un grupo; «de cada 100 personas con ganas de trabajar, 20 estaban sin empleo» es un dato, que además hay que revisar: quién lo recogió, cómo y en qué lugar. Una tasa de desempleo mide cuántas personas que buscan trabajo no lo tienen.",
        "Para evaluar una consecuencia se contrastan las tres: se compara la promesa con los datos y se pregunta cómo lo vivió cada grupo. Si los datos son de una sola ciudad, no se pueden aplicar a todo el país sin más. Un buen análisis dice qué fuente respalda cada afirmación y reconoce lo que no sabe.",
    ],
    vocab=[("promesa", "lo que se espera lograr con una política, antes de ver resultados"), ("percepción", "cómo ve un grupo los efectos de algo"), ("dato", "información medible, como una cifra o una tasa"), ("desempleo", "situación de quien quiere trabajar y no tiene empleo"), ("tasa", "cantidad por cada cien, o por otra cantidad fija, de personas o hechos")],
    worked=[
        ("Distinguir promesa y dato", "«Los precios bajarán» y «los precios bajaron 5 % según una tabla de ejemplo». ¿Cuál es promesa y cuál dato?", ["La primera anuncia algo futuro.", "La segunda entrega una cifra medida."], "La primera es promesa y la segunda es dato"),
        ("Calcular una diferencia", "Una tabla de ejemplo muestra 12 personas sin empleo por cada 100 en un año y 18 en el siguiente. ¿Cuánto subió la tasa?", ["Resto el valor menor al mayor.", "18 − 12 = 6."], "6 personas más por cada 100"),
    ],
    mistakes=[("Tomar una promesa como si fuera un resultado.", "Se confunde lo que se esperaba con lo que ocurrió.", "Busca datos que muestren qué pasó."),
              ("Generalizar los datos de una ciudad a todo el país.", "Se olvida el lugar de la fuente.", "Di «en la ciudad de la tabla…» y busca más datos antes de generalizar.")],
    T=[
        ("{F} ¿Quién escribió la Fuente B?", "Una organización de trabajadores", "La ficha lo indica."),
        ("{F} ¿Qué año tiene la Fuente A?", "1978", "La ficha da el año."),
        ("En Historia: ¿qué es una tasa de desempleo?", "Cuántas personas que buscan trabajo no lo tienen, por cada cien", "Es la definición que se usa en la clase."),
        ("{F} ¿Qué tipo de fuente es la Fuente C? A) Un dato B) Una promesa", "A) Un dato", "Es una tabla con cifras medidas."),
        ("=", "{F} ¿Cuántas personas más sin empleo por cada 100 hubo en 1983 que en 1978?", "20-10", "Se resta la cifra de 1978 a la de 1983.", " personas"),
        ("{F} ¿Cuál es el propósito probable de la Fuente A? A) Mostrar los beneficios esperados de la apertura B) Reclamar por los salarios", "A) Mostrar los beneficios esperados de la apertura", "Es un documento de quienes diseñan la política."),
        ("{F} La Fuente B dice que hay menos poder para negociar. ¿Qué es eso? A) Una percepción de un grupo B) Un dato medido", "A) Una percepción de un grupo", "Es cómo ven los trabajadores los efectos del Plan Laboral."),
        ("Una compañera usa la Fuente C para decir «en todo Chile el desempleo se duplicó». ¿Qué le respondes? A) Que la tabla es de una ciudad de ejemplo y no permite hablar de todo el país B) Que es correcto porque hay una tabla", "A) Que la tabla es de una ciudad de ejemplo y no permite hablar de todo el país", "Los datos valen para el lugar que describen."),
        ("{F} Ordena de menor a mayor la tasa de desempleo de la Fuente C.", "10 por cada 100 (1978), 20 por cada 100 (1983)", "Se comparan las dos cifras."),
        ("{F} ¿Qué diferencia hay entre la Fuente A y la Fuente C?", "La A anuncia lo que se espera; la C muestra una cifra medida", "Una es promesa y la otra, dato."),
        ("{F} Alguien dice: «La Fuente C prueba que el modelo falló». ¿Qué falta? A) Saber la causa de ese aumento, otros datos y más lugares B) Nada, un dato basta", "A) Saber la causa de ese aumento, otros datos y más lugares", "Un dato muestra qué ocurrió, no necesariamente por qué."),
        ("¿Qué fuente agregarías para contrastar la Fuente A? A) Datos de precios y variedad de productos en la misma época B) Otro documento del mismo equipo económico que repite las promesas", "A) Datos de precios y variedad de productos en la misma época", "Para evaluar una promesa se necesitan resultados medidos."),
        ("¿Qué conclusión se sostiene mejor? A) Cada fuente aporta algo distinto y se deben contrastar B) La Fuente A explica todo", "A) Cada fuente aporta algo distinto y se deben contrastar", "Ninguna basta sola."),
    ],
    ctx=("Un diario de ejemplo titula: «El modelo bajó los precios» usando solo un documento de sus promotores. ¿Qué falla? A) Usa una promesa como si fuera un dato B) Usa un título corto", "A) Usa una promesa como si fuera un dato", "Falta un dato medido que compruebe el resultado."),
    sc=[("¿Qué diferencia hay entre promesa y dato?", "La promesa dice lo que se espera; el dato es una información medida", "Son las definiciones de la clase."),
        ("¿Por qué no se puede generalizar un dato de una ciudad a todo el país?", "Porque describe solo ese lugar", "Hay que reconocer el lugar de la fuente."),
        ("=", "Una tabla de ejemplo muestra 7 personas sin empleo por cada 100 y luego 15 por cada 100. ¿Cuántas más hay?", "15-7", "Se resta la cifra menor a la mayor.", " personas")],
    op=("Elige dos fuentes de la ficha y completa una tabla: quién habla, cuándo, para qué, si es promesa, percepción o dato, y qué falta saber. Termina con una frase que diga qué puedes afirmar con ambas y qué no. {F}",
        "Fuente A: equipo económico, 1978, convencer, promesa, faltan datos de precios. Fuente C: estudio posterior, tabla, dato, falta saber la causa y más lugares. Frase: la tabla muestra que subió el desempleo en una ciudad de ejemplo, pero no prueba la causa.",
        ["completa todos los campos", "distingue promesa, percepción y dato", "formula una conclusión proporcional"], ["tabla", "una frase"], ["usar la promesa como resultado", "generalizar un dato local"],
        "Pide que explique qué otra fuente agregaría."),
    reinforce="Explica a alguien de tu casa la diferencia entre una promesa y un dato con un ejemplo de publicidad.",
    extend="Revisa una oferta de ejemplo («50 % menos») y di qué dato necesitarías para comprobarla.",
)

# ================================================================ OA 17, clase 3
F = ("Ficha 3 (perspectivas de ejemplo; las citas y cifras son de ejemplo). "
     "Perspectiva de un economista que valora el modelo: «Hay más productos disponibles, la economía crece y las empresas son más eficientes.» "
     "Perspectiva de una dirigenta sindical: «Los trabajadores perdieron protecciones y los salarios no crecieron al mismo ritmo que las ganancias.» "
     "Perspectiva de una familia consumidora: «Hay más bienes en las tiendas, pero pagamos cuotas por la salud y la educación.» "
     "Escalas: la economía del país (nacional), el sector o la empresa, y el hogar. "
     "Plazos: corto plazo (los primeros años) y largo plazo (décadas después). "
     "Criterios de evaluación posibles: crecimiento, empleo, desigualdad, acceso a servicios, libertad de elegir.")
build(
    OA, 3, F,
    use="Aprenderé a comparar perspectivas, escalas y plazos sobre el modelo neoliberal, usando criterios. Sirve para evaluar sin tomar partido antes de revisar la evidencia.",
    prior=["Sé qué rasgos tuvo el modelo neoliberal.", "Sé distinguir promesa, percepción y dato.", "Sé qué es una escala."],
    explain=[
        "Un modelo económico afecta de manera distinta a cada grupo, por eso hay perspectivas diversas. Un economista que valora el modelo mira sobre todo la producción y la eficiencia; una dirigenta sindical mira la protección y los salarios de los trabajadores; una familia consumidora mira lo que puede comprar y lo que debe pagar por servicios. Todas pueden decir algo verdadero desde su lugar.",
        "Para compararlas se usan criterios, que son las preguntas con las que se evalúa: ¿creció la economía?, ¿hubo empleo?, ¿cambió la desigualdad?, ¿mejoró el acceso a servicios? También importa la escala: el país puede crecer mientras un hogar tiene dificultades. Y el plazo: una medida puede tener efectos en los primeros años y otros distintos décadas después.",
        "Comparar no consiste en elegir un bando, sino en mostrar qué criterio usa cada perspectiva y qué deja fuera. Una afirmación como «el país creció» y otra como «mi familia gasta más en servicios» pueden ser ciertas a la vez, porque miden cosas diferentes. Evaluar bien es decir qué criterio, qué escala y qué plazo se usan.",
    ],
    vocab=[("perspectiva", "punto de vista desde el que se mira un hecho"), ("criterio", "pregunta o medida con que se evalúa algo"), ("corto plazo", "los primeros años después de una medida"), ("largo plazo", "los efectos que se ven décadas después"), ("desigualdad", "diferencia en ingresos o en acceso a bienes y servicios entre grupos")],
    worked=[
        ("Identificar el criterio", "«La economía creció 5 % al año» (dato de ejemplo). ¿Qué criterio usa?", ["Habla de producción total del país.", "Eso es crecimiento económico."], "Crecimiento económico"),
        ("Cambiar de escala", "El país crece, pero una familia de ejemplo gasta más en salud. ¿Es contradictorio?", ["Una frase mira la escala nacional y la otra el hogar.", "Miden cosas distintas."], "No: cada afirmación usa una escala diferente"),
    ],
    mistakes=[("Elegir un bando antes de mirar la evidencia.", "Se confunde comparar con tomar partido.", "Primero identifica el criterio y la evidencia de cada perspectiva."),
              ("Creer que una afirmación verdadera a escala nacional lo es también en cada hogar.", "No se distinguen las escalas.", "Pregunta siempre a qué nivel se refiere la cifra.")],
    T=[
        ("{F} ¿Qué dos plazos distingue la ficha?", "Corto plazo y largo plazo", "La ficha los nombra."),
        ("{F} ¿Quién dice que los salarios no crecieron al mismo ritmo que las ganancias?", "La dirigenta sindical", "Es su perspectiva en la ficha."),
        ("En Historia: ¿qué es un criterio de evaluación?", "Una pregunta o medida con que se evalúa algo", "Es la definición de la clase."),
        ("{F} La familia consumidora dice que hay más bienes pero paga cuotas por salud y educación. ¿Qué escala mira? A) El hogar B) El país entero", "A) El hogar", "Habla de lo que ocurre en su casa."),
        ("{F} ¿Qué criterio usa el economista cuando habla de más productos y empresas eficientes? A) Crecimiento y eficiencia B) Protección laboral", "A) Crecimiento y eficiencia", "Mira producción y eficiencia."),
        ("Clasifica por criterio: (a) «bajó el desempleo en un año»; (b) «subió la diferencia de ingresos entre ricos y pobres».", "(a) empleo; (b) desigualdad", "Cada frase se asocia a un criterio distinto."),
        ("Una medida tiene beneficios en los primeros años y costos décadas después. ¿Qué debe distinguir quien evalúa? A) Corto y largo plazo B) Solo el primer año", "A) Corto y largo plazo", "Los efectos cambian según el plazo."),
        ("Un informe de ejemplo dice: «El país creció, pero la mitad de los hogares de ejemplo ganó menos de lo que gasta». ¿Por qué no hay contradicción? A) Mide escalas diferentes B) Una de las dos frases es falsa", "A) Mide escalas diferentes", "Una mira el conjunto del país y otra los hogares."),
        ("{F} Explica por qué la perspectiva del economista y la de la dirigenta pueden ser ciertas al mismo tiempo.", "Porque usan criterios distintos: una mira producción y eficiencia y la otra salarios y protección", "Cada perspectiva mide un aspecto distinto."),
        ("{F} La familia consumidora habla de pagar cuotas por salud y educación. ¿Con cuál criterio de la ficha se relaciona? A) Acceso a servicios B) Libertad de elegir", "A) Acceso a servicios", "Pagar por salud y educación se evalúa según quién puede acceder a esos servicios."),
        ("Alguien dice: «Si el país crece, todos viven mejor». Evalúa. A) Es excesiva: el crecimiento nacional no muestra por sí solo lo que ocurre en cada hogar ni la desigualdad B) Es correcta: crecer siempre mejora la vida", "A) Es excesiva: el crecimiento nacional no muestra por sí solo lo que ocurre en cada hogar ni la desigualdad", "Cambia la escala sin comprobarlo."),
        ("{F} ¿Qué evidencia permitiría comparar las perspectivas? A) Datos de empleo, ingresos y acceso a servicios en cada plazo B) Solo las opiniones de cada persona", "A) Datos de empleo, ingresos y acceso a servicios en cada plazo", "Los criterios se contrastan con datos."),
        ("¿Cuál es una forma justa de presentar el tema en clase? A) Mostrar criterios, escalas, plazos y evidencia de cada perspectiva B) Mostrar solo la perspectiva con la que estás de acuerdo", "A) Mostrar criterios, escalas, plazos y evidencia de cada perspectiva", "Así se puede evaluar sin tomar partido de antemano."),
    ],
    ctx=("Un compañero dice: «Mi tío dice que antes era mejor, el diario dice que el país creció; uno miente». ¿Qué respuesta ayuda? A) Pueden mirar escalas y criterios distintos y ambos decir algo cierto B) Siempre hay uno que miente", "A) Pueden mirar escalas y criterios distintos y ambos decir algo cierto", "Esa respuesta usa lo aprendido sobre criterio y escala."),
    sc=[("En Historia: ¿Qué es un criterio?", "Una pregunta o medida con que se evalúa algo", "Así se define en la clase."),
        ("¿Qué diferencia hay entre escala nacional y escala del hogar?", "La nacional mira el país entero y la del hogar mira una familia", "Cambian los datos que se observan."),
        ("Nombra dos criterios que menciona la ficha.", "Dos de estos: crecimiento, empleo, desigualdad, acceso a servicios o libertad de elegir", "La ficha los enumera.")],
    op=("Elige dos perspectivas de la ficha. Escribe para cada una: qué criterio usa, a qué escala habla, qué plazo mira y qué evidencia necesitarías para comprobar su afirmación. Termina con una frase que muestre cómo ambas pueden ser ciertas a la vez. {F}",
        "Economista: crecimiento y eficiencia, nacional, largo plazo, datos de producción. Dirigenta: salarios y protecciones, sector trabajadores, largo plazo, series de salarios. Frase: el país puede crecer mientras los salarios suben menos que las ganancias.",
        ["identifica criterio, escala y plazo de cada una", "propone evidencia", "no toma partido"], ["cuadro comparativo", "una frase"], ["escoger un bando sin evidencia", "confundir escalas"],
        "Pide que explique qué dato cambiaría su evaluación."),
    reinforce="Explica a alguien de tu casa la diferencia entre mirar un país y mirar un hogar con un ejemplo de gasto.",
    extend="Elige un cambio reciente en tu barrio y di quién se beneficia en el corto plazo y quién en el largo plazo.",
)

# ================================================================ OA 17, clase 4
F = ("Ficha 4 (causas, cambios y continuidades; datos de ejemplo cuando se indica). "
     "Causas de largo plazo: la crisis económica de comienzos de los años setenta, con alta inflación (alza general y sostenida de precios); ideas económicas liberales difundidas por economistas; un gobierno sin Congreso ni oposición legal que pudiera frenar las reformas. "
     "Detonante: la decisión de la Junta de aplicar un programa de reformas de mercado. "
     "Cambios: el Estado vendió empresas, bajó aranceles, redujo el gasto social y cambió la ley laboral en 1979. "
     "Continuidades: el cobre siguió siendo la principal exportación y su explotación mayor siguió en manos del Estado (Codelco); la desigualdad y la pobreza siguieron siendo problemas. "
     "Crisis económica de 1982: cayó la producción y subió el desempleo. Dato de ejemplo: una empresa privada reduce su personal de 400 a 300 personas.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar causas, cambios y continuidades del modelo neoliberal chileno. Sirve para no atribuir todo a una sola causa y para ver qué cambió y qué se mantuvo.",
    prior=["Sé qué rasgos tuvo el modelo.", "Sé distinguir causa de largo plazo y detonante.", "Sé calcular restas y porcentajes sencillos."],
    explain=[
        "Un modelo económico no aparece de la nada. En Chile había una crisis económica con alta inflación a comienzos de los años setenta, ideas liberales difundidas por economistas y un gobierno sin Congreso que podía decidir sin frenos. Esas son causas de largo plazo. El detonante fue la decisión de aplicar un programa de reformas de mercado. Ninguna causa explica sola el proceso.",
        "Entre los cambios están la venta de empresas, la baja de aranceles, el menor gasto social y la ley laboral de 1979. Entre las continuidades están el peso del cobre en las exportaciones, cuya explotación mayor siguió en manos del Estado a través de Codelco, y la persistencia de la pobreza y la desigualdad. Que algo cambie no significa que todo cambie.",
        "La crisis de 1982 mostró un límite del modelo: cayó la producción y subió el desempleo, y el Estado tuvo que intervenir. Al relacionar causas y consecuencias conviene usar lenguaje prudente, como «contribuyó a» o «se asocia con», porque dos hechos pueden ocurrir juntos sin que uno cause al otro.",
    ],
    vocab=[("inflación", "alza general y sostenida de los precios"), ("reforma de mercado", "cambio de reglas para que el mercado tenga más peso en la economía"), ("Codelco", "empresa estatal chilena que explota cobre"), ("continuidad", "algo que se mantiene a pesar de los cambios"), ("se asocia con", "expresión prudente: ocurren juntos sin afirmar que uno cause al otro")],
    worked=[
        ("Clasificar cambio y continuidad", "El Estado vendió empresas, pero el cobre siguió siendo la principal exportación. ¿Cuál es cada cosa?", ["Vender empresas es algo nuevo.", "El peso del cobre ya existía y continuó."], "Cambio: venta de empresas; continuidad: el cobre como principal exportación"),
        ("Usar lenguaje prudente", "Una tabla de ejemplo muestra que el desempleo subió el mismo año en que cayó la producción. ¿Qué frase es mejor?", ["Que dos hechos coincidan no prueba por sí solo que uno cause al otro.", "Conviene decir «se asocia con»."], "«La caída de la producción se asocia con el aumento del desempleo»"),
    ],
    mistakes=[("Decir que el modelo neoliberal fue la única causa de todos los cambios.", "Se ignoran causas previas y otros factores.", "Reúne varias causas y usa lenguaje prudente."),
              ("Creer que los cambios eliminaron todas las continuidades.", "No se distingue qué se mantuvo.", "Busca qué siguió igual, como el cobre o la desigualdad.")],
    T=[
        ("{F} ¿Qué crisis ocurrió en 1982?", "Una crisis económica en que cayó la producción y subió el desempleo", "La ficha la describe así."),
        ("{F} ¿Qué empresa estatal siguió explotando el cobre?", "Codelco", "La ficha la nombra."),
        ("En Historia: ¿qué es la inflación?", "Un alza general y sostenida de los precios", "Es la definición de la clase."),
        ("{F} Clasifica como cambio o continuidad: (a) se baja el arancel; (b) el cobre sigue siendo la principal exportación.", "(a) cambio; (b) continuidad", "Bajar el arancel es nuevo; el cobre ya era importante y lo siguió siendo."),
        ("{F} ¿Qué cambio de 1979 afectó las relaciones laborales? A) Una nueva ley laboral B) La venta del cobre a privados", "A) Una nueva ley laboral", "La ficha lo lista entre los cambios; el cobre siguió en manos del Estado."),
        ("{F} ¿Qué causa de largo plazo menciona la ficha? A) La crisis con alta inflación de comienzos de los setenta B) La crisis de 1982", "A) La crisis con alta inflación de comienzos de los setenta", "La crisis de 1982 es posterior al inicio del modelo."),
        ("{F} La Junta decide aplicar un programa de reformas de mercado. ¿Qué es eso en la ficha? A) El detonante B) Una continuidad", "A) El detonante", "Es el hecho que desencadena el proceso."),
        ("=", "{F} Una empresa de ejemplo con 400 personas reduce su personal en un 25 %. ¿Cuántas personas quedan?", "400-400*25//100", "El 25 % de 400 es 100, y 400 menos 100 es 300.", " personas"),
        ("Clasifica: (a) el Congreso no existía; (b) había alta inflación. ¿Cuál es condición política y cuál económica?", "(a) política; (b) económica", "El Congreso es una institución política y la inflación es un fenómeno económico."),
        ("{F} ¿Por qué decir «el modelo causó por sí solo la crisis de 1982» es débil?", "Porque pudo haber otras causas y se necesita más evidencia", "La ficha solo muestra que la crisis ocurrió, no su causa única."),
        ("Una tabla de ejemplo muestra que el desempleo subió el mismo año en que cayó la producción. ¿Qué frase es mejor? A) Se asocia con B) Fue causado exclusivamente por", "A) Se asocia con", "Evita afirmar una causa única sin evidencia."),
        ("{F} Evalúa: «Como el Estado vendió empresas, dejó de intervenir en la economía». A) Es excesiva: el Estado siguió interviniendo, por ejemplo con Codelco y ante la crisis de 1982 B) Es correcta", "A) Es excesiva: el Estado siguió interviniendo, por ejemplo con Codelco y ante la crisis de 1982", "La ficha muestra intervención del Estado en el cobre."),
        ("¿Qué síntesis es mejor? A) Hubo varias causas, cambios importantes y continuidades como el cobre y la desigualdad B) Todo cambió en 1973", "A) Hubo varias causas, cambios importantes y continuidades como el cobre y la desigualdad", "Integra causas, cambios y continuidades."),
    ],
    ctx=("Un trabajo escolar dice: «Antes de 1973 no había ningún problema económico, el modelo lo creó todo». ¿Qué falla? A) Ignora la crisis previa y las continuidades B) Usa números", "A) Ignora la crisis previa y las continuidades", "La ficha muestra causas anteriores y cosas que siguieron igual."),
    sc=[("¿Qué es un detonante?", "El hecho que desencadena un proceso que ya tenía causas previas", "Así se define en la clase."),
        ("Da una continuidad del período.", "El cobre siguió siendo la principal exportación", "Es una de las continuidades de la ficha."),
        ("=", "Una empresa de ejemplo pasa de 200 a 150 personas. ¿Cuántas menos tiene?", "200-150", "Se resta el personal final al inicial.", " personas")],
    op=("Haz un esquema con tres columnas: causas (de largo plazo y detonante), cambios y continuidades, con los datos de la ficha. Escribe luego dos frases: una con «contribuyó a» y otra con «se asocia con». {F}",
        "Causas: crisis con alta inflación, ideas liberales, gobierno sin Congreso; detonante: reformas de mercado. Cambios: ventas de empresas, menores aranceles. Continuidades: cobre, desigualdad. Frases: «La crisis contribuyó a que se adoptaran reformas»; «La caída de la producción de 1982 se asocia con el aumento del desempleo».",
        ["clasifica causas, cambios y continuidades", "usa lenguaje prudente", "evita causas únicas"], ["esquema", "dos frases"], ["afirmar una causa única", "no incluir continuidades"],
        "Pide que explique qué evidencia falta para probar una causa."),
    reinforce="Explica a alguien de tu casa la diferencia entre cambio y continuidad con un ejemplo de tu barrio.",
    extend="Elige un cambio en tu escuela y di qué causas previas lo hicieron posible.",
)

# ================================================================ OA 17, clase 5
F = ("Ficha 5 (datos de ejemplo para practicar; no son cifras oficiales). "
     "Pregunta: ¿cuál fue la consecuencia social de la apertura comercial y las privatizaciones para las familias de una ciudad de ejemplo? "
     "Evidencia 1 (precios): en la ciudad de ejemplo, un televisor costaba 100 unidades en el año 1 y 60 en el año 8. "
     "Evidencia 2 (empleo): una fábrica local de ejemplo cerró y 300 personas perdieron su empleo en el año 5; en el mismo período se abrió un centro comercial con 120 empleos nuevos. "
     "Evidencia 3 (testimonio de ejemplo): «Podemos comprar más cosas, pero muchos vecinos tuvieron que buscar otro trabajo y algunos ganan menos.» "
     "Evidencia 4 (informe posterior de ejemplo): «El acceso a bienes aumentó; la desigualdad de ingresos siguió alta.»")
build(
    OA, 5, F,
    use="Aprenderé a construir una interpretación documentada sobre las consecuencias sociales del modelo: una afirmación apoyada en evidencias, con su límite y una contra-evidencia. Sirve para escribir un argumento histórico claro.",
    prior=["Sé interrogar fuentes y comparar perspectivas.", "Sé distinguir promesa, percepción y dato.", "Sé usar lenguaje prudente."],
    explain=[
        "Una interpretación documentada es una respuesta a una pregunta histórica que se apoya en evidencias. Tiene tres partes: una tesis, es decir, la afirmación principal; las evidencias que la apoyan, con su fuente; y los límites, que son lo que la evidencia no permite afirmar o la evidencia que la matiza.",
        "Para construirla, primero se lee la pregunta y se ordenan las evidencias. Luego se redacta una tesis que no diga más de lo que muestran los datos. Por ejemplo: «En la ciudad de ejemplo, la apertura comercial se asoció con precios más bajos y mayor acceso a bienes, pero también con pérdidas de empleo que afectaron a familias concretas.» Esa frase reconoce beneficios y costos.",
        "Para que sea sólida, cada afirmación se conecta con una evidencia, y se dice qué falta saber: por ejemplo, si las personas que perdieron empleo lo recuperaron después. Una buena interpretación evita términos absolutos como «todos» o «nadie», porque los datos son de un lugar y un período. Al final, se revisa que la tesis responda la pregunta.",
    ],
    vocab=[("tesis", "afirmación principal de un argumento"), ("evidencia", "dato o fuente que apoya o debilita una afirmación"), ("contra-evidencia", "evidencia que matiza o contradice una afirmación"), ("límite", "lo que la evidencia no permite afirmar"), ("interpretación documentada", "respuesta a una pregunta apoyada en evidencias con sus fuentes")],
    worked=[
        ("Conectar tesis y evidencia", "Tesis: «Bajaron los precios de bienes importados». ¿Qué evidencia de la ficha la apoya?", ["Busco un dato de precios.", "El televisor pasó de 100 a 60 unidades."], "La Evidencia 1: el precio del televisor bajó"),
        ("Reconocer un límite", "Con la ficha, ¿se puede afirmar que toda la economía chilena mejoró?", ["Los datos son de una ciudad de ejemplo.", "No permiten hablar de todo el país."], "No: los datos son de una ciudad de ejemplo"),
    ],
    mistakes=[("Escribir una tesis sin evidencia.", "Se afirma sin mostrar de dónde sale.", "Después de cada afirmación escribe qué dato la apoya."),
              ("Usar «todos» o «nadie» con datos de un lugar.", "Se generaliza más de lo que permiten.", "Usa «en la ciudad de ejemplo» y reconoce el límite.")],
    T=[
        ("{F} ¿Cuál es la pregunta que guía el análisis?", "Cuál fue la consecuencia social de la apertura comercial y las privatizaciones para las familias de una ciudad de ejemplo", "Es la pregunta de la ficha."),
        ("{F} ¿Cuántos empleos nuevos creó el centro comercial?", "120", "La ficha lo indica."),
        ("En Historia: ¿qué es una tesis?", "La afirmación principal de un argumento", "Es la definición de la clase."),
        ("=", "{F} ¿Cuántas unidades bajó el precio del televisor entre el año 1 y el año 8?", "100-60", "Se resta el precio final al inicial.", " unidades"),
        ("{F} ¿Qué evidencia apoya la tesis «hubo pérdida de empleo»? A) La Evidencia 2 B) La Evidencia 1", "A) La Evidencia 2", "La fábrica cerrada dejó a 300 personas sin empleo."),
        ("{F} La Evidencia 4 dice que la desigualdad de ingresos siguió alta. ¿Qué hace con la tesis «el acceso a bienes mejoró para todos»? A) La matiza B) La confirma sin límites", "A) La matiza", "Muestra que el acceso mejoró pero queda desigualdad."),
        ("=", "{F} Si la fábrica cerró 300 empleos y el centro comercial creó 120, ¿cuántos empleos menos hubo en total?", "300-120", "Se resta lo creado a lo perdido.", " empleos"),
        ("{F} ¿Cuál es una tesis prudente? A) En la ciudad de ejemplo hubo precios más bajos y también pérdida de empleos B) Todos en Chile vivieron mejor", "A) En la ciudad de ejemplo hubo precios más bajos y también pérdida de empleos", "Se ajusta a las evidencias y al lugar."),
        ("{F} Quieres apoyar la tesis «el acceso a bienes aumentó». ¿Qué evidencia usas? A) La 1 y la 4 B) La 2", "A) La 1 y la 4", "Ambas hablan de precios y acceso a bienes."),
        ("{F} Explica por qué la Evidencia 3 es un testimonio y no un dato medido.", "Porque es la opinión de una persona y no una cifra recogida en forma sistemática", "Un dato medido es una cifra; el testimonio relata una vivencia."),
        ("{F} ¿Qué límite debe reconocer una tesis basada en esta ficha?", "Que los datos son de una ciudad de ejemplo y no de todo el país", "Los datos solo describen ese lugar."),
        ("{F} Alguien escribe: «Nadie perdió con la apertura comercial». ¿Qué evidencia la contradice? A) La Evidencia 2, con 300 empleos perdidos B) La Evidencia 1", "A) La Evidencia 2, con 300 empleos perdidos", "Muestra que hubo personas que perdieron su empleo."),
        ("¿Qué parte falta en esta interpretación: «El modelo fue beneficioso porque el televisor bajó de precio»? A) Más evidencia y los límites B) Una opinión personal más fuerte", "A) Más evidencia y los límites", "Un solo dato no sostiene una evaluación."),
    ],
    ctx=("Un compañero debe escribir una conclusión para un trabajo sobre una ciudad de ejemplo. ¿Cuál se ajusta mejor? A) «En esta ciudad, algunos precios bajaron y también hubo pérdida de empleos» B) «El modelo fue perfecto para todos»", "A) «En esta ciudad, algunos precios bajaron y también hubo pérdida de empleos»", "Ajusta la afirmación a la evidencia y al lugar."),
    sc=[("¿Cuáles son las tres partes de una interpretación documentada?", "Tesis, evidencias y límites", "Así se explican en la clase."),
        ("¿Qué es una contra-evidencia?", "Evidencia que matiza o contradice una afirmación", "Es la definición de la clase."),
        ("=", "Un precio de ejemplo baja de 80 a 50 unidades. ¿Cuántas unidades bajó?", "80-50", "Se resta el precio final al inicial.", " unidades")],
    op=("Con la ficha, escribe un párrafo de cuatro líneas que responda su pregunta. Debe incluir: una tesis prudente, dos evidencias con su número, una contra-evidencia y un límite. Evita las palabras «todos» y «nadie». {F}",
        "En la ciudad de ejemplo, la apertura comercial se asoció con precios más bajos (Evidencia 1) y mayor acceso a bienes (Evidencia 4), pero también con 300 empleos perdidos (Evidencia 2). Los datos son de una ciudad y no permiten generalizar al país.",
        ["tesis prudente", "dos evidencias citadas", "contra-evidencia y límite"], ["párrafo de cuatro líneas"], ["escribir una tesis sin evidencia", "usar «todos» o «nadie»"],
        "Pide que explique qué dato adicional haría más sólida su tesis."),
    reinforce="Escribe una tesis de una línea sobre un cambio reciente en tu barrio y una evidencia que la apoye.",
    extend="Busca en casa un dato (por ejemplo, el precio de un producto) y escribe una tesis prudente con un límite.",
)

# ================================================================ OA 17, clase 6
F = ("Ficha 6 (debate sobre consecuencias; datos de ejemplo). "
     "Posición 1: «El modelo trajo más bienes disponibles, mayor eficiencia y crecimiento, por lo que su balance es positivo.» "
     "Posición 2: «El modelo aumentó la inseguridad laboral y dejó fuera a muchas familias del acceso a servicios, por lo que su balance es negativo.» "
     "Criterios de evaluación: crecimiento, empleo, desigualdad, acceso a servicios y libertad de elegir. "
     "Plazos: corto plazo (primeros años) y largo plazo (décadas). "
     "Datos de ejemplo: en el corto plazo, el desempleo subió 5 puntos; en el largo plazo, la variedad de bienes aumentó 40 %, y la brecha de ingresos entre los más ricos y los más pobres se mantuvo alta. "
     "Reglas del debate: argumentar con evidencia, reconocer los límites del propio argumento y responder a la otra posición sin descalificar a las personas.")
build(
    OA, 6, F,
    use="Aprenderé a debatir las consecuencias sociales del modelo neoliberal y los límites de cada argumento, a corto y largo plazo. Sirve para evaluar con criterios y evidencias y no solo con opiniones.",
    prior=["Sé comparar perspectivas, criterios y plazos.", "Sé construir una tesis con evidencia.", "Sé leer datos de ejemplo."],
    explain=[
        "Un debate histórico no consiste en ganar, sino en evaluar una pregunta con argumentos. Un argumento tiene una afirmación, una evidencia y una explicación de por qué esa evidencia apoya la afirmación. Para debatir el modelo neoliberal conviene fijar primero los criterios: crecimiento, empleo, desigualdad, acceso a servicios y libertad de elegir. Sin criterios, cada persona usa una vara distinta.",
        "Las consecuencias cambian según el plazo. En el corto plazo pueden predominar costos, como el aumento del desempleo; en el largo plazo pueden verse beneficios, como más variedad de bienes, junto a problemas persistentes, como la desigualdad. Un balance honesto dice qué criterio mejoró, cuál empeoró, cuál no cambió y para quiénes.",
        "Reconocer los límites del propio argumento fortalece la posición: por ejemplo, decir que los datos son de ejemplo o de un lugar, o que falta información. En un debate se responde a las ideas, no se ataca a las personas. Puedes concluir de forma matizada, por ejemplo que el modelo mejoró algunos criterios y dejó pendientes otros.",
    ],
    vocab=[("argumento", "afirmación apoyada en una evidencia y una explicación"), ("balance", "resumen de lo que mejoró, empeoró o no cambió según los criterios"), ("matizar", "reconocer que una conclusión tiene excepciones o límites"), ("brecha", "distancia entre los ingresos de dos grupos"), ("falacia ad hominem", "atacar a la persona en vez de responder a su argumento")],
    worked=[
        ("Armar un argumento", "Afirmación: «Aumentó la variedad de bienes». Evidencia de ejemplo: 40 % más variedad. ¿Qué falta para que sea un argumento completo?", ["Ya hay afirmación y evidencia.", "Falta explicar por qué esa evidencia apoya la afirmación: más variedad significa más opciones de compra."], "Falta la explicación que conecta la evidencia con la afirmación"),
        ("Hacer un balance", "El desempleo subió en el corto plazo y la variedad de bienes aumentó en el largo plazo. ¿Cómo se resume sin tomar partido?", ["Se distinguen plazos y criterios.", "Se nombra qué empeoró y qué mejoró."], "Empeoró el empleo en el corto plazo y mejoró la variedad de bienes en el largo plazo"),
    ],
    mistakes=[("Responder a una posición atacando a quien la sostiene.", "Se confunde debatir ideas con descalificar personas.", "Responde con una evidencia o un criterio."),
              ("Dar un balance sin distinguir plazos ni criterios.", "Se mezclan efectos que ocurren en momentos distintos.", "Di qué criterio y qué plazo estás evaluando.")],
    T=[
        ("{F} ¿Qué criterios de evaluación menciona la ficha?", "Crecimiento, empleo, desigualdad, acceso a servicios y libertad de elegir", "La ficha los enumera."),
        ("{F} ¿Cuántos puntos subió el desempleo en el corto plazo, según el dato de ejemplo?", "5 puntos", "La ficha lo indica."),
        ("En Historia: ¿qué es un balance?", "Un resumen de lo que mejoró, empeoró o no cambió según los criterios", "Es la definición de la clase."),
        ("{F} ¿Qué mejoró en el largo plazo según el dato de ejemplo? A) La variedad de bienes B) La brecha de ingresos", "A) La variedad de bienes", "La ficha dice que la brecha se mantuvo alta."),
        ("=", "{F} Si había 1.000 variedades de bienes y aumentaron 40 %, ¿cuántas variedades hay ahora?", "1000+1000*40//100", "Se suma el 40 % de 1.000 al total inicial.", " variedades"),
        ("{F} ¿Cuál es una regla del debate? A) Argumentar con evidencia B) Repetir la posición con más fuerza hasta convencer", "A) Argumentar con evidencia", "Así lo indica la ficha."),
        ("Alguien responde: «No le hagan caso, él es de otro partido». ¿Qué falla tiene? A) Ataca a la persona en vez del argumento B) Usa una evidencia de otro plazo", "A) Ataca a la persona en vez del argumento", "No responde a la idea con evidencia."),
        ("Clasifica por plazo: (a) subida del desempleo en los primeros años; (b) más variedad de bienes décadas después.", "(a) corto plazo; (b) largo plazo", "El primero ocurre al inicio y el segundo se ve más tarde."),
        ("{F} La Posición 2 habla de inseguridad laboral. ¿Con qué criterio se relaciona? A) Empleo B) Libertad de elegir", "A) Empleo", "La inseguridad laboral se evalúa con empleo."),
        ("{F} Explica por qué la Posición 1 y la Posición 2 pueden usar datos ciertos y llegar a conclusiones distintas.", "Porque usan criterios y plazos distintos", "Cada una mira un aspecto diferente."),
        ("{F} Evalúa: «Como la variedad de bienes aumentó, el modelo mejoró la vida de todas las familias». A) Es excesiva: ese dato no muestra empleo, desigualdad ni acceso a servicios B) Es correcta: más bienes siempre mejora", "A) Es excesiva: ese dato no muestra empleo, desigualdad ni acceso a servicios", "Un solo criterio no basta para concluir."),
        ("{F} ¿Qué dato necesitaría la Posición 2 para sostener que muchas familias quedaron fuera del acceso a servicios? A) Cuántas familias accedían a salud y educación antes y después B) Cuántas variedades de bienes hay", "A) Cuántas familias accedían a salud y educación antes y después", "Ese dato mide el criterio de acceso a servicios; la variedad de bienes mide otro."),
        ("¿Cuál es la conclusión más matizada? A) El modelo mejoró algunos criterios, como la variedad de bienes, y dejó pendientes otros, como la desigualdad B) El modelo fue totalmente bueno o totalmente malo", "A) El modelo mejoró algunos criterios, como la variedad de bienes, y dejó pendientes otros, como la desigualdad", "Reconoce mejoras y límites según criterios."),
    ],
    ctx=("En un debate escolar, un compañero dice: «Mi posición es la correcta porque yo lo digo». ¿Qué le falta? A) Una evidencia y un criterio B) Que la sostenga más gente del curso", "A) Una evidencia y un criterio", "Un argumento necesita evidencia y explicación."),
    sc=[("¿Qué tres elementos forman un argumento?", "Afirmación, evidencia y explicación", "Así se define en la clase."),
        ("¿Por qué conviene distinguir corto y largo plazo?", "Porque los efectos de una medida cambian con el tiempo", "Costos y beneficios pueden aparecer en momentos distintos."),
        ("=", "Un ingreso de ejemplo sube de 100 a 130 unidades. ¿Cuántas unidades subió?", "130-100", "Se resta el valor inicial al final.", " unidades")],
    op=("Prepara un breve turno de debate de cinco líneas: elige una posición de la ficha o una conclusión matizada. Incluye: una afirmación, dos evidencias de la ficha, una respuesta respetuosa a la otra posición y un límite de tu argumento. No ataques a ninguna persona. {F}",
        "Afirmación matizada: el modelo mejoró la variedad de bienes (40 % más) pero aumentó el desempleo en el corto plazo (5 puntos). Respuesta: la Posición 2 tiene razón en el empleo. Límite: los datos son de ejemplo y no incluyen acceso a servicios.",
        ["afirmación clara", "dos evidencias", "respuesta respetuosa y un límite"], ["texto de cinco líneas"], ["atacar a la persona", "no indicar el plazo"],
        "Pide que diga qué evidencia le haría cambiar su conclusión."),
    reinforce="Explica a alguien de tu casa un argumento con afirmación, evidencia y explicación sobre un tema cotidiano.",
    extend="Anota dos criterios con los que evaluarías un cambio en tu colegio y di qué dato necesitarías para cada uno.",
)

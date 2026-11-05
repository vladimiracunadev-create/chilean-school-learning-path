"""Cuaderno del estudiante de 2.º medio Artes Visuales: AR2M OA 06 (difusión artística y aporte a la comunidad)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA6 = "AR2M OA 06"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def w(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def m(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=[ctx], selfcheck=sc, open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- Clase 1
lesson(
    OA6, 1,
    "Hojas y lápiz. Las fichas de las muestras de ejemplo están escritas en la clase: no necesitas organizar nada todavía.",
    "Aprenderé a observar una propuesta de difusión de trabajos de arte mirando su contexto, su lenguaje y su propósito, e identificando las obras a exponer, el espacio, el montaje, el público y el aporte a la comunidad. Sirve para planificar una difusión con sentido.",
    ["Sé evaluar un proyecto con criterios y evidencia.", "Sé que cada manifestación visual se lee por contexto, lenguaje y propósito."],
    [
        "Difundir es dar a conocer trabajos de arte a una comunidad. Puede hacerse de forma directa, con una exposición en un lugar físico como un pasillo, un patio o una biblioteca, o de forma virtual, con una presentación en línea. En ambos casos conviene pensar en cinco elementos: las manifestaciones visuales a exponer, el espacio, el montaje, el público y el aporte a la comunidad.",
        "El montaje es la forma de instalar y ordenar las obras en el espacio: altura, distancia entre obras, orden del recorrido y rótulos (pequeños textos con título, autoría y técnica). El público es quien va a mirar; su edad, sus intereses y el tiempo que tiene cambian las decisiones. El aporte a la comunidad es lo que la difusión deja: por ejemplo, abrir una conversación sobre un tema del barrio o decorar un lugar de uso común.",
        "En esta clase observo muestras de ejemplo inventadas y las leo con tres preguntas: dónde ocurre (contexto), cómo está organizada (lenguaje del montaje) y para qué se hace (propósito). La realización real de la exposición y el uso de herramientas de montaje en la escuela las coordina el docente. Cada persona conserva la autoría de su obra y decide si se muestra.",
    ],
    [("difusión", "dar a conocer trabajos de arte a una comunidad"), ("montaje", "forma de instalar y ordenar las obras en el espacio"), ("rótulo", "texto breve con título, autoría y técnica de una obra"), ("público", "personas que van a mirar la muestra"), ("aporte a la comunidad", "lo que deja la difusión en las personas o en el lugar")],
    [
        w("Leer una muestra", "Muestra de ejemplo «Barrio en colores»: 8 obras de estudiantes, en un pasillo de 12 m del liceo; se ve durante un recreo largo; visitan estudiantes y apoderados; busca que se hable de cómo cuidar los espacios del barrio. Identifica los cinco elementos.", ["Obras: 8 obras de estudiantes.", "Espacio: pasillo de 12 m. Público: estudiantes y apoderados.", "Aporte: conversar sobre el cuidado del barrio. Montaje: la ficha no lo describe."], "Obras 8; espacio pasillo de 12 m; público estudiantes y apoderados; aporte: cuidar el barrio"),
        w("Directa o virtual", "Una muestra de ejemplo se presenta en un panel en línea que cualquiera puede abrir en su teléfono. ¿Es directa o virtual y qué debes cuidar?", ["No es un lugar físico: es virtual.", "Debe cuidar: imágenes claras, textos cortos y sin datos personales.", "También pedir permiso de cada autor."], "Virtual; imágenes claras, textos cortos y permisos"),
    ],
    [
        m("Pensar que difundir es solo colgar obras en la pared.", "Falta pensar en el público, el espacio y el aporte.", "Responde las cinco preguntas: obras, espacio, montaje, público y aporte."),
        m("Mostrar una obra sin avisar a su autor.", "La autoría pertenece a quien la hizo y decide si se muestra.", "Pide permiso a cada autor antes de exponer."),
    ],
    [
        ex("¿Qué es difundir en arte? A. Dar a conocer trabajos a una comunidad B. Guardar los trabajos en un cajón.", "A", "Difundir es mostrar a otras personas."),
        ex("¿Qué es el montaje? A. La forma de instalar y ordenar las obras en el espacio B. El título de la muestra.", "A", "Incluye altura, orden y rótulos."),
        ex("¿Qué es un rótulo? A. Un texto breve con título, autoría y técnica B. Un marco de madera.", "A", "Identifica la obra para el público."),
    ],
    [
        ex("En la muestra «Barrio en colores», ¿quién es el público? A. Estudiantes y apoderados B. Las 8 obras.", "A", "El público es quien mira la muestra."),
        ex("¿Qué elemento describe lo que la muestra deja en la comunidad? A. El aporte a la comunidad B. El montaje.", "A", "Es el efecto que busca la difusión."),
        ex("Una difusión en una página en línea es… A. Virtual B. Directa en un pasillo.", "A", "No ocurre en un lugar físico."),
    ],
    [
        ex("Un rótulo corto con título, autoría y técnica, colgado a la altura de los ojos, ¿a qué elemento de la difusión pertenece? A. Al montaje B. Al público.", "A", "El rótulo y su altura son decisiones de montaje; el público es quien mira."),
        ex("Quieres que apoderados mayores lean los rótulos sin dificultad. ¿Qué decisión tomas? A. Usar letras grandes y textos breves B. Usar letras diminutas con mucho texto.", "A", "El público determina el tamaño y la extensión del texto."),
        ex("Una muestra se instala en un pasillo donde el estudiantado pasa de prisa. ¿Qué rótulo conviene? A. Corto, con título y autoría B. Un párrafo de 15 líneas.", "A", "Quien pasa de prisa lee poco."),
    ],
    [
        ex("Dos propósitos de ejemplo. X: abrir una conversación sobre el cuidado de las plazas. Y: llenar una pared vacía. ¿Cuál es un aporte a la comunidad? A. X B. Y.", "A", "X deja una conversación útil para la comunidad."),
        ex("Una muestra se hace en una sala de profesores a la que el estudiantado casi no entra. ¿Qué falla? A. El espacio no llega al público que se busca B. El color de los rótulos.", "A", "El espacio no coincide con el público."),
    ],
    [
        ex("Un compañero quiere exponer el dibujo de una amiga sin preguntarle. ¿Qué respondes? A. Que debe pedirle permiso B. Que no es necesario.", "A", "La autora decide si su obra se expone."),
        ex("Quieres hacer una muestra virtual con fotos de las obras de tu curso. ¿Qué cuidas? A. Imágenes claras y sin datos personales B. Fotos oscuras con el nombre completo y el curso de cada estudiante.", "A", "Se protege la privacidad y se asegura la lectura."),
    ],
    ex("Quieres mostrar a tu familia los dibujos de tu curso en una pared del hogar durante una semana. ¿Qué decisión de montaje es adecuada? A. Elegir un lugar de paso donde todos los vean B. Dejarlos dentro de una carpeta sobre un mueble.", "A", "El espacio debe llegar a su público."),
    [
        ex("Nombra los cinco elementos de una difusión.", "Obras, espacio, montaje, público y aporte a la comunidad", "Son los cinco elementos a planificar."),
        ex("Verdadero o falso: una muestra puede ser virtual.", "Verdadero", "Puede ocurrir en línea."),
        ex("¿Quién decide si una obra se expone?", "Su autor", "La autoría pertenece a quien la hizo."),
    ],
    task(
        "Elige UNA muestra de ejemplo. A) «Barrio en colores»: 8 obras sobre el cuidado de los espacios, en un pasillo de 12 m, para estudiantes y apoderados. B) «Mi calle sonora»: 6 fotografías de objetos del barrio, en un panel en línea, para estudiantes y vecinos. C) «Manos»: 10 dibujos de manos, en la biblioteca, para quienes la visitan. Escribe una ficha con las obras, el espacio, el montaje (una idea), el público y el aporte a la comunidad; agrega una interpretación con «podría» y un juicio apoyado en un criterio.",
        "Elegí A. Obras: 8 sobre el cuidado de espacios. Espacio: pasillo de 12 m. Montaje: obras a la altura de los ojos y rótulos cortos. Público: estudiantes y apoderados. Aporte: conversar sobre el barrio. Interpretación: poner las obras en un pasillo podría sugerir que los espacios comunes son de todos. Juicio: es pertinente porque la gente pasa y mira.",
        ["identifica los cinco elementos", "escribe una interpretación con «podría»", "apoya el juicio en un criterio", "respeta la autoría y la privacidad"],
        ["ficha con los cinco elementos", "interpretación y juicio con criterio"],
        ["olvidar al público", "no pensar en el aporte a la comunidad"],
        "Pregunta qué elemento de la ficha respalda el juicio y si el espacio llega al público elegido.",
    ),
    "Mira un lugar de tu casa o de tu barrio donde se muestren cosas (un mural, un paradero con afiches) y di quién lo ve y qué aporta.",
    "Explica en tres frases la diferencia entre difusión directa y virtual.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA6, 2,
    "Hojas, regla y lápiz. Si quieres practicar, usa cartulinas, cordel y pinzas de ropa. No uses clavos, martillos, escaleras ni vidrio. Los datos están escritos en la clase.",
    "Aprenderé a explorar los espacios, los soportes y las obras posibles para una difusión escolar o local, y a seleccionar qué exponer con criterios. Sirve para elegir con razones el lugar y las obras de una muestra.",
    ["Sé identificar obras, espacio, montaje, público y aporte.", "Sé que la autoría decide si una obra se expone."],
    [
        "Para explorar un espacio lo miro con preguntas: ¿cuántas personas pasan?, ¿cuánto tiempo se quedan?, ¿hay luz natural sin sol directo sobre las obras?, ¿hay lugar para circular con comodidad, incluso con silla de ruedas?, ¿quién cuida ese lugar y puede autorizar? Un pasillo, un patio cubierto, una biblioteca o un hall tienen ventajas distintas. El lugar debe estar autorizado por quien lo administra.",
        "Los soportes son lo que sostiene las obras. Pueden ser paneles de cartón, cordeles tendidos con pinzas de ropa o muebles bajos. Evito los clavos, las escaleras y todo lo que ponga en riesgo a alguien. Un soporte seguro es estable, no bloquea la salida y no daña los muros. Si el espacio es virtual, el soporte es la página o la presentación: necesita fotos claras de cada obra con luz pareja.",
        "Para seleccionar obras uso criterios: que respondan al tema de la muestra, que estén terminadas, que quepan en el espacio y que su autor acepte mostrarlas. Hago una lista y la comparo con el espacio. No todas las obras tienen que entrar; elegir es parte del trabajo de curatoría, es decir, de armar una selección con sentido.",
    ],
    [("soporte", "lo que sostiene las obras en una muestra"), ("curatoría", "selección de obras con un sentido para una muestra"), ("circular", "moverse con comodidad por un espacio"), ("autorización", "permiso de quien administra un lugar o de un autor"), ("pertinente", "que responde al tema y al público")],
    [
        w("Comparar espacios", "Espacios de ejemplo para 10 obras: pasillo (muy concurrido, luz natural, pared de 14 m), biblioteca (poca gente, silenciosa, pared de 9 m) y patio cubierto (mucha gente, con viento). El tema es el cuidado del barrio y se busca que mucha gente mire. ¿Cuál es el más pertinente?", ["Pasillo: muy concurrido y pared de 14 m para 10 obras.", "Biblioteca: poca gente. Patio: el viento puede mover las obras.", "El pasillo conviene."], "El pasillo, porque tiene mucho público, luz y pared suficiente"),
        w("Seleccionar obras", "Hay 14 obras de ejemplo, pero en el pasillo caben 10. Criterios: responder al tema, estar terminadas y con autorización. 3 no responden al tema y 2 no están terminadas (ninguna repetida). ¿Cuántas cumplen y caben?", ["Descarto 3 + 2 = 5 obras.", "Quedan 14 − 5 = 9.", "9 son menos que 10, así que caben."], "Quedan 9 obras, y caben en el pasillo"),
    ],
    [
        m("Elegir un espacio solo porque está libre.", "Puede no llegar al público ni ser seguro.", "Revisa público, luz, circulación y autorización."),
        m("Usar clavos o subirse a una silla para colgar una obra.", "Es riesgoso para las personas y daña el muro.", "Usa cordel con pinzas o paneles estables y pide ayuda al docente."),
    ],
    [
        ex("¿Qué es un soporte? A. Lo que sostiene las obras en una muestra B. El título de la obra.", "A", "Pueden ser paneles o cordeles con pinzas."),
        ex("¿Quién debe autorizar el uso de un espacio? A. Quien lo administra B. Cualquier estudiante.", "A", "Hay que pedir permiso a quien lo cuida."),
        ex("¿Qué significa curatoría? A. Seleccionar obras con un sentido B. Pintar las obras.", "A", "Es elegir y organizar con criterio."),
    ],
    [
        ex("¿Qué soporte es seguro para colgar dibujos livianos? A. Cordel tendido con pinzas de ropa B. Clavos en la pared.", "A", "No daña el muro ni requiere herramientas riesgosas."),
        ex("¿Qué conviene evitar en un espacio de muestra? A. Sol directo sobre las obras B. Luz natural pareja.", "A", "El sol directo puede dañar y dificultar la visión."),
        ex("Una obra no está terminada. ¿Qué haces según los criterios? A. No incluirla todavía B. Incluirla igual.", "A", "Un criterio de selección es que esté terminada."),
    ],
    [
        arith("Hay 18 obras de ejemplo y 5 no responden al tema de la muestra. ¿Cuántas obras quedan?", "18 - 5", "Se descartan las que no cumplen el criterio.", " obras"),
        ex("Un hall tiene una rampa angosta bloqueada por una mesa. ¿Qué falla para la circulación? A. No todas las personas podrían llegar a mirar las obras B. Los colores de las obras.", "A", "La circulación libre es parte de elegir bien el espacio."),
        ex("Para llegar a mucha gente en poco tiempo, ¿qué lugar conviene? A. Un pasillo concurrido B. Un rincón poco visitado de la biblioteca.", "A", "Pasa mucha gente."),
    ],
    [
        ex("Una biblioteca silenciosa tiene pared de 9 m, poca gente y buena luz. Una muestra de ejemplo sobre un tema delicado busca conversación tranquila. ¿Cuál es una ventaja? A. El silencio permite mirar y leer con calma B. Es el lugar con más tránsito.", "A", "El silencio favorece una observación detenida."),
        ex("Un compañero propone usar la sala de profesores sin avisar «porque nadie la usa ahora». ¿Qué falla? A. No tiene autorización B. La luz.", "A", "Hay que pedir permiso a quien administra el lugar."),
    ],
    [
        ex("Un grupo quiere tender un cordel entre dos árboles del patio para colgar obras. ¿Qué es lo primero? A. Pedir autorización y asegurar que no bloquee el paso B. Amarrarlo muy alto con una escalera.", "A", "La autorización y la seguridad van primero."),
        ex("Quieres una muestra virtual y tienes fotos oscuras de las obras. ¿Qué haces? A. Volver a fotografiarlas con luz de ventana de lado B. Subirlas igual.", "A", "La luz pareja mejora la lectura."),
    ],
    ex("En tu hogar quieres mostrar cuatro dibujos de tu curso en el pasillo. El pasillo mide 3 m y debe quedar libre para pasar. ¿Qué decisión es adecuada? A. Colgarlos en una pared sin bloquear el paso B. Apilarlos en el suelo.", "A", "El paso debe quedar libre y seguro."),
    [
        ex("¿Qué cuatro cosas conviene preguntar de un espacio?", "Público, luz, circulación y autorización", "Son las preguntas de exploración del espacio."),
        ex("Verdadero o falso: se pueden usar clavos y escaleras sin ayuda.", "Falso", "Son riesgos que deben evitarse."),
        ex("¿Qué criterio descarta una obra de la muestra?", "No responder al tema o no estar terminada", "Son criterios de selección."),
    ],
    task(
        "Planifica la exploración de un espacio. Elige UNA muestra: A) 10 obras sobre el cuidado del barrio; B) 6 fotografías de objetos cotidianos; C) 12 dibujos de manos. Compara DOS espacios de ejemplo: pasillo concurrido (pared de 14 m, luz natural) y biblioteca (pared de 9 m, poca gente). Decide cuál conviene, qué soporte seguro usarás y qué criterios de selección usarás. Si hay más obras que lugar, calcula cuántas descartas.",
        "Elegí A, 10 obras. Pasillo: público alto, 14 m. Biblioteca: poco público. Decido el pasillo. Soporte: cordel con pinzas y paneles de cartón estables, con ayuda del docente. Criterios: responder al tema, estar terminadas y con permiso de su autor. Si hubiera 13 obras y caben 10, descarto 3.",
        ["compara dos espacios con razones", "elige un soporte seguro", "usa criterios de selección", "pide autorización del espacio"],
        ["comparación de espacios", "criterios de selección"],
        ["elegir sin pedir permiso", "usar soportes riesgosos"],
        "Pregunta por qué ese espacio llega mejor al público y qué soporte es seguro.",
    ),
    "Recorre tu casa o tu liceo y elige un lugar seguro donde mostrar tres dibujos sin bloquear el paso.",
    "Escribe tres frases que expliquen por qué un espacio debe estar autorizado.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA6, 3,
    "Hojas, regla, cinta métrica o regla larga, cartulinas y pinzas de ropa. Practica con cartulinas en un muro de tu casa con permiso, sin clavos. Los datos están escritos en la clase.",
    "Aprenderé a probar decisiones de montaje: altura, distancia entre obras, recorrido, rótulos y accesibilidad. Sirve para que la muestra se vea ordenada, segura y comprensible para todas las personas.",
    ["Sé seleccionar obras y espacios con criterios.", "Sé que un soporte debe ser estable y seguro."],
    [
        "El montaje se puede probar antes de instalar las obras. Una regla de ejemplo es colgar las obras con su centro a unos 1,50 m del suelo, que es cerca de la altura de los ojos de muchas personas. Si una obra queda más arriba o más abajo, se ve menos. Para que todas las personas puedan mirar, incluidas quienes usan silla de ruedas, conviene dejar una zona de recorrido libre de al menos 1 m de ancho.",
        "La distancia entre obras también se decide. Si están muy pegadas, se confunden; si están muy separadas, el recorrido se corta. Un método es medir: si el muro mide 11 m y cuelgo 5 obras de 1 m, quedan 6 m libres que reparto en 6 espacios iguales (4 entre obras y 2 en los extremos), es decir, 1 m cada uno. Pruebo con cartulinas antes de usar las obras reales.",
        "El recorrido es el orden en que se mira: de un tema a otro, de izquierda a derecha. Los rótulos van al lado de cada obra, con título, autoría y técnica, y a una altura legible. Las letras deben leerse desde 1 m. Una prueba de montaje se anota: qué cambié, qué ocurrió y qué decido. Cambio una sola cosa a la vez.",
    ],
    [("recorrido", "orden en que el público mira las obras"), ("zona libre", "espacio sin obstáculos para circular"), ("altura de ojos", "altura a la que se ve cómodamente una obra"), ("maqueta de montaje", "prueba del montaje con cartulinas o papel"), ("legible", "que se lee con facilidad")],
    [
        w("Repartir el espacio", "Un muro de ejemplo mide 11 m y vas a colgar 5 obras de 1 m cada una. Quieres 6 espacios iguales entre las obras y en los extremos. ¿Cuánto mide cada espacio?", ["Ocupan las obras: 5 × 1 = 5 m.", "Quedan libres: 11 − 5 = 6 m.", "Cada espacio: 6 ÷ 6 = 1 m."], "1 m cada espacio"),
        w("Probar la altura", "Una obra de ejemplo mide 60 cm de alto y quieres su centro a 150 cm del suelo. ¿A qué altura queda su borde inferior?", ["Mitad de la obra: 60 ÷ 2 = 30 cm.", "Borde inferior: 150 − 30 = 120 cm.", "Borde superior: 150 + 30 = 180 cm."], "120 cm del suelo"),
    ],
    [
        m("Colgar las obras a distintas alturas sin una regla.", "Cuesta mirarlas y el conjunto se ve desordenado.", "Usa el centro a la altura de los ojos, como regla de ejemplo."),
        m("Dejar el pasillo lleno de obras y mesas sin zona de recorrido.", "No todas las personas pueden pasar.", "Deja al menos 1 m de ancho libre."),
    ],
    [
        ex("¿A qué altura se cuelga el centro de una obra, según la regla de ejemplo? A. Cerca de 1,50 m del suelo B. En el techo.", "A", "Es cerca de la altura de los ojos."),
        ex("¿Qué es el recorrido? A. El orden en que el público mira las obras B. El nombre de la muestra.", "A", "Guía la mirada de un tema a otro."),
        ex("¿Qué debe quedar libre en una muestra? A. Una zona de al menos 1 m para circular B. Ninguna zona.", "A", "Permite circular con comodidad."),
    ],
    [
        ex("¿Qué dato lleva un rótulo? A. Título, autoría y técnica B. Solo el precio.", "A", "Identifica la obra para el público."),
        ex("¿Por qué se prueba el montaje con cartulinas? A. Para no mover las obras reales una y otra vez B. Para gastar más cartulinas.", "A", "Evita dañar las obras."),
        ex("Si cambias la altura y la distancia a la vez, ¿sabrás qué cambio mejoró la muestra? A. No B. Sí.", "A", "Se debe cambiar una sola cosa por prueba."),
    ],
    [
        ex("En un muro, las obras de una serie quedaron separadas 3 m entre sí y el público dice que no se entienden como conjunto. ¿Qué ajuste conviene? A. Acercarlas, manteniendo espacios iguales entre todas B. Separarlas todavía más.", "A", "Si están muy separadas, el recorrido se corta; espacios iguales dan orden."),
        arith("El centro de una obra de ejemplo debe quedar a 150 cm. La obra mide 80 cm de alto. ¿A qué altura queda su borde inferior?", "150 - 80 // 2", "Se resta la mitad de la altura de la obra del centro.", " cm"),
        ex("Una obra de ejemplo mide 40 cm de alto y quieres el centro a 150 cm. ¿A qué altura queda su borde superior? A. 170 cm B. 130 cm.", "A", "150 + 40 ÷ 2 = 170.", ),
    ],
    [
        ex("Un pasillo mide 2 m de ancho y una mesa de 1,5 m ocupa el centro. ¿Queda libre 1 m para circular? Responde sí o no.", "No", "Quedarían 0,5 m, que no alcanza."),
        ex("Dos montajes de ejemplo con 6 obras: P las pone en fila a una altura pareja con espacios iguales; Q las pone a distintas alturas, sin orden. El criterio es claridad del recorrido. ¿Cuál cumple mejor? A. P B. Q.", "A", "El orden y la altura pareja guían la mirada."),
    ],
    [
        ex("Un compañero quiere probar el montaje subiéndose a una silla para colgar una obra a 2,20 m. ¿Qué respondes? A. No, usar la regla de 1,50 m y evitar subirse a sillas B. Sí, con cuidado.", "A", "La regla de altura cumple y evita el riesgo de caída."),
        ex("Dos montajes de ejemplo con las mismas 6 obras: M deja 1 m libre de pasillo y rótulos legibles desde 1 m; N deja 40 cm libres y rótulos que se leen desde 10 cm. Si importa que todas las personas circulen y lean, ¿cuál conviene? A. M B. N.", "A", "Cumple con la zona libre y la lectura de rótulos."),
    ],
    ex("Un familiar usa silla de ruedas y va a visitar tu muestra en casa. ¿Qué cuidas en el montaje? A. Un pasillo libre y obras a una altura que pueda ver B. Poner las obras bien altas.", "A", "La accesibilidad incluye el recorrido y la altura."),
    [
        ex("¿A cuánto ancho mínimo de zona libre apunta la regla de ejemplo?", "1 m", "Permite circular con comodidad."),
        ex("Verdadero o falso: se debe probar con cartulinas antes de instalar las obras reales.", "Verdadero", "Evita dañar las obras."),
        ex("¿Qué se anota tras cada prueba de montaje?", "Qué se cambió, qué ocurrió y qué se decide", "Es la evidencia del proceso."),
    ],
    task(
        "Diseña la maqueta de montaje de UNA muestra. A) 6 obras de 1 m de ancho en un muro de 13 m. B) 4 obras de 1 m de ancho en un muro de 9 m. C) 8 obras de 1 m de ancho en un muro de 17 m. Calcula el espacio entre obras (con espacios iguales entre obras y en los extremos), la altura del borde inferior de una obra de 60 cm de alto con centro a 150 cm, escribe un rótulo con título, autoría y técnica de una obra inventada, y dibuja o describe el recorrido.",
        "Elegí B. Obras: 4 × 1 = 4 m. Libres: 9 − 4 = 5 m, en 5 espacios: 1 m cada uno. Borde inferior: 150 − 30 = 120 cm. Rótulo: «Mi calle», autoría: Ana (nombre de ejemplo), técnica: lápices de color. Recorrido: de izquierda a derecha, de lo cercano a lo lejano.",
        ["calcula bien los espacios", "usa la regla de altura de ejemplo", "escribe un rótulo con tres datos", "deja una zona de circulación y un recorrido"],
        ["cálculos de montaje", "rótulo y recorrido descritos"],
        ["no medir antes de colgar", "olvidar la zona libre"],
        "Pregunta cómo se calculó la distancia entre obras y qué se probó antes de instalar.",
    ),
    "Mide una pared de tu casa y calcula cuántas hojas de 30 cm caben con espacios de 10 cm entre ellas.",
    "Explica en tres frases por qué la altura de ojos importa en un montaje.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA6, 4,
    "Hojas, lápiz y regla. Las opciones y los precios están escritos en la clase. Los permisos del espacio los gestiona una persona adulta responsable.",
    "Aprenderé a elaborar un plan de difusión propio con obras, espacio, montaje, público, aporte a la comunidad, tareas, calendario y presupuesto. Sirve para pasar de la idea a una propuesta que se pueda realizar en la escuela o en el barrio.",
    ["Sé seleccionar obras y espacios.", "Sé calcular espacios y alturas de un montaje."],
    [
        "Un plan de difusión organiza todo lo necesario para mostrar los trabajos. Incluye las obras a exponer, el espacio autorizado, el montaje, el público, el aporte a la comunidad, quién hace cada tarea, las fechas y un presupuesto. El presupuesto es la lista de gastos con sus precios; los materiales reutilizados cuestan $0.",
        "El plan responde cuatro preguntas: qué mostraremos, a quién, dónde y cómo, y qué dejará en la comunidad. Por ejemplo, si el público son vecinos y el aporte es abrir una conversación sobre el cuidado de la plaza, la muestra puede incluir un libro de visitas donde la gente escriba ideas. La invitación debe decir qué, dónde, cuándo y para quién, en pocas líneas.",
        "Hay que cuidar la autoría y la privacidad: cada autor aprueba que su obra se muestre, y los rótulos usan nombre de pila o seudónimo según lo que cada autor decida. En una muestra virtual no se publican datos personales de menores sin permiso. La parte de taller, como instalar estructuras o equipos de iluminación, la resuelve el docente. Mi plan no debe obligar a nadie a hacer algo riesgoso.",
    ],
    [("plan de difusión", "organización de obras, espacio, montaje, público, tareas, fechas y presupuesto"), ("presupuesto", "lista de gastos con sus precios"), ("invitación", "mensaje que dice qué, dónde, cuándo y para quién"), ("libro de visitas", "cuaderno donde el público escribe comentarios"), ("tarea", "acción asignada a una persona")],
    [
        w("Calcular un presupuesto", "Plan de ejemplo: 4 pliegos de cartulina a $800 cada uno, 2 ovillos de cordel a $1.500 cada uno y las pinzas de ropa de la casa ($0). ¿Cuánto cuesta en total?", ["Cartulinas: 4 × 800 = 3.200.", "Cordel: 2 × 1.500 = 3.000.", "Total: 3.200 + 3.000 = 6.200 pesos."], "$6.200"),
        w("Escribir una invitación", "Muestra de ejemplo para vecinos, el viernes a las 17:00 en el hall del liceo. Redacta la invitación con qué, dónde, cuándo y para quién.", ["Qué: muestra «Barrio en colores».", "Dónde y cuándo: hall del liceo, viernes a las 17:00.", "Para quién: vecinos y apoderados."], "Muestra «Barrio en colores», hall del liceo, viernes 17:00, para vecinos y apoderados"),
    ],
    [
        m("Hacer una invitación que no dice dónde ni cuándo.", "El público no sabe cómo asistir.", "Incluye qué, dónde, cuándo y para quién."),
        m("Publicar datos personales de menores en la muestra virtual.", "Pone en riesgo su privacidad.", "Usa nombre de pila o seudónimo si el autor lo decide y no publiques datos personales."),
    ],
    [
        ex("¿Qué es un presupuesto? A. Una lista de gastos con sus precios B. Un tipo de obra.", "A", "Permite saber cuánto cuesta realizar el plan."),
        ex("¿Qué debe decir una invitación? A. Qué, dónde, cuándo y para quién B. Solo el título.", "A", "Con esos cuatro datos el público puede asistir."),
        ex("Los materiales reutilizados que ya tienes, ¿cuánto cuestan en el presupuesto? A. $0 B. $5.000.", "A", "No se compran."),
    ],
    [
        ex("¿Para qué sirve un libro de visitas? A. Para que el público deje comentarios B. Para guardar las obras.", "A", "Es evidencia de la recepción."),
        ex("¿Quién aprueba que una obra se muestre? A. Su autor B. Cualquier persona del curso.", "A", "La autoría decide."),
        ex("¿Qué parte del plan dice quién hace cada acción? A. Las tareas B. El presupuesto.", "A", "Reparte las responsabilidades entre las personas."),
    ],
    [
        arith("Plan de ejemplo: 5 pliegos de cartulina a $800 cada uno y 1 ovillo de cordel a $1.500. ¿Cuánto cuesta en total?", "5 * 800 + 1500", "Se calcula cada gasto y se suman.", " pesos"),
        ex("Tu plan compra cartulina nueva y cordel nuevo, pero en casa hay cordel de sobra. ¿Cómo bajas el presupuesto? A. Usando el cordel de casa, que cuesta $0 B. Comprando más cartulina.", "A", "Un material que ya se tiene no suma gasto."),
        ex("Quieres invitar a vecinos a una muestra. ¿Qué invitación está completa? A. «Muestra de dibujos, hall del liceo, sábado 11:00, para vecinos» B. «Ven a ver una muestra».", "A", "Dice qué, dónde, cuándo y para quién."),
    ],
    [
        ex("Un plan dice que habrá 40 asistentes, pero la sala solo permite 30 personas a la vez con recorrido libre. ¿Qué ajuste corresponde? A. Organizar dos turnos B. Dejar que entren todos juntos.", "A", "Se cuida la circulación y la seguridad."),
        ex("Un grupo repartió las tareas así: una persona hace todo, las demás miran. ¿Qué mejora el plan? A. Repartir tareas entre todos B. Dejarlo igual.", "A", "Un plan realista reparte responsabilidades."),
    ],
    [
        ex("Una compañera no quiere que su nombre aparezca en el rótulo de su dibujo. ¿Qué haces? A. Respetarlo y usar un seudónimo o dejar el rótulo sin nombre B. Poner su nombre completo igual.", "A", "La autoría y la privacidad se respetan."),
        ex("Un plan tiene tres tareas (invitaciones, montaje y libro de visitas) y seis integrantes. ¿Qué mejora el reparto? A. Que cada tarea tenga dos responsables B. Que una persona haga las tres.", "A", "Repartir responsabilidades hace el plan realista."),
    ],
    ex("Si quieres hacer una muestra en el hall de tu liceo, ¿quién debe autorizar el espacio? A. La persona adulta que lo administra B. Un estudiante cualquiera.", "A", "El permiso lo da quien administra el lugar."),
    [
        ex("¿Qué cuatro preguntas responde un plan?", "Qué mostrar, a quién, dónde y cómo, y qué aportará", "Organizan la difusión."),
        ex("Verdadero o falso: una invitación debe decir cuándo y dónde.", "Verdadero", "Sin esos datos nadie puede asistir."),
        ex("¿Qué se hace si una autora no quiere su nombre en el rótulo?", "Se respeta su decisión", "La autoría y la privacidad son suyas."),
    ],
    task(
        "Escribe un plan de difusión para UNA muestra. A) 8 dibujos sobre el cuidado de una plaza, en el hall del liceo, para vecinos. B) 10 fotografías de objetos del barrio, en un panel en línea, para estudiantes. C) 6 afiches sobre el reciclaje, en el pasillo, para el curso vecino. Incluye obras, espacio, montaje (altura y distancia), público, aporte a la comunidad, 3 tareas con responsables, fecha, invitación completa y un presupuesto con cantidades y precios de ejemplo.",
        "Elegí A. Obras: 8 dibujos. Espacio: hall del liceo, autorizado por la dirección. Montaje: cordel con pinzas a 150 cm de altura, rótulos cortos. Público: vecinos. Aporte: libro de visitas con ideas para la plaza. Tareas: invitaciones (Ana), montaje (Luis), libro de visitas (Marta). Fecha: sábado 11:00. Presupuesto: 3 pliegos de cartulina a $800 = $2.400 y 1 cordel a $1.500; total $3.900.",
        ["incluye los cinco elementos y tareas", "calcula bien el presupuesto", "redacta una invitación completa", "cuida autoría y privacidad"],
        ["plan completo", "invitación y presupuesto"],
        ["olvidar al público", "invitación incompleta"],
        "Pregunta si la invitación tiene qué, dónde, cuándo y para quién, y si el cálculo del presupuesto está bien.",
    ),
    "Escribe una invitación de cuatro líneas para mostrar tres dibujos a tu familia.",
    "Anota tres materiales de tu casa que podrías reutilizar para una muestra y cuánto sumarían al presupuesto.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA6, 5,
    "Hojas y lápiz. Los datos de las muestras de ejemplo están escritos en la clase.",
    "Aprenderé a contrastar una difusión con criterios de pertinencia al público, montaje seguro y accesible, aporte a la comunidad y respeto a la autoría. Sirve para evaluar con evidencia lo ocurrido y mejorar la próxima vez.",
    ["Sé armar un plan de difusión.", "Sé probar decisiones de montaje y calcular espacios."],
    [
        "Contrastar una difusión es comparar lo que se planeó con lo que ocurrió, usando criterios y evidencia. Cuatro criterios, cada uno de 0 a 3 puntos: pertinencia al público (el espacio y los textos llegan a quienes se buscaba), montaje (ordenado, seguro y accesible), aporte a la comunidad (deja algo útil) y respeto a la autoría y la privacidad. El máximo es 12 puntos.",
        "La evidencia son datos: cuántas personas asistieron, qué comentarios hay en el libro de visitas, cuánto tiempo se quedaron, fotos del montaje sin personas identificables. Si 40 personas fueron invitadas y asistieron 30, la asistencia fue de tres cuartos. Los comentarios se leen completos: los que dan ideas ayudan a mejorar y los que ofenden se comentan con una persona adulta de confianza.",
        "Después propongo un ajuste concreto para la próxima vez, por ejemplo cambiar de espacio, agregar un turno o hacer rótulos más grandes. Evalúo la difusión, no a las personas. También anoto lo que la exposición real necesitaría de un taller o de especialistas, como iluminación o estructuras, y se lo dejo al docente.",
    ],
    [("asistencia", "número de personas que fueron a la muestra"), ("pertinencia", "ajuste de la muestra al público y al lugar"), ("accesible", "que todas las personas pueden usar o mirar"), ("evidencia", "datos que respaldan un puntaje"), ("ajuste", "cambio concreto para mejorar la próxima vez")],
    [
        w("Calcular la asistencia", "Se invitó a 40 personas a una muestra de ejemplo y asistieron 30. ¿Cuántas personas no asistieron y qué parte asistió?", ["No asistieron: 40 − 30 = 10 personas.", "Asistieron 30 de 40, es decir, tres de cada cuatro.", "La asistencia fue de tres cuartos."], "10 personas no asistieron; asistieron tres cuartos"),
        w("Aplicar la pauta", "Pauta de 4 criterios de 0 a 3. Muestra de ejemplo: pertinencia 3 (asistieron 30 de 40 invitados), montaje 2 (la zona libre era de 70 cm), aporte 3 (hay 12 comentarios con ideas), autoría y privacidad 3. ¿Cuál es el total y qué ajuste propones?", ["Suma: 3 + 2 + 3 + 3 = 11.", "Criterio más bajo: montaje.", "Ajuste: ampliar la zona libre a 1 m."], "11 de 12; ampliar la zona libre del montaje a 1 m"),
    ],
    [
        m("Evaluar la muestra solo con «salió lindo».", "No hay evidencia ni criterios.", "Usa datos: asistencia, comentarios y fotos del montaje."),
        m("Publicar fotos con personas identificables sin su permiso.", "Se vulnera su privacidad.", "Toma fotos del montaje sin personas o con permiso."),
    ],
    [
        ex("¿Cuál es el puntaje máximo de la pauta de cuatro criterios de 0 a 3 puntos?", "12", "Cuatro criterios por 3 puntos son 12.", calc="4 * 3"),
        ex("¿Qué es la asistencia? A. El número de personas que fueron a la muestra B. El precio de las obras.", "A", "Es un dato de evidencia."),
        ex("¿Qué criterio evalúa si el espacio y los textos llegan al público? A. Pertinencia al público B. Aporte a la comunidad.", "A", "Mide el ajuste entre muestra y público."),
    ],
    [
        ex("Una muestra tuvo una zona libre de 70 cm en el pasillo. Con la regla de ejemplo de 1 m, ¿qué criterio baja? A. Montaje accesible B. Aporte a la comunidad.", "A", "La zona libre era menor que la regla."),
        ex("Un libro de visitas con 12 comentarios con ideas, ¿qué criterio respalda? A. Aporte a la comunidad B. Montaje.", "A", "Muestra lo que la muestra dejó."),
        ex("Un comentario del libro de visitas ofende a una autora. ¿Qué haces? A. Lo comentas con una persona adulta de confianza B. Lo publicas para que todos lo lean.", "A", "Un comentario ofensivo se atiende con una persona adulta."),
    ],
    [
        ex("Una muestra de ejemplo invitó a 50 personas y asistieron 35. ¿Qué parte de los invitados asistió? A. Siete décimos B. Tres quintos.", "A", "35 de 50 es lo mismo que 7 de 10."),
        arith("Una muestra suma 3, 2, 3 y 2 en los cuatro criterios. ¿Cuál es el total?", "3 + 2 + 3 + 2", "Se suman los cuatro puntajes.", " puntos"),
        ex("Dos muestras de ejemplo suman 9 puntos. X tiene 3 en montaje y 0 en autoría; Y tiene 0 en montaje porque las mesas bloquean la salida, y 3 en autoría. Antes de abrirlas al público, ¿cuál tiene un riesgo físico inmediato que corregir? A. Y B. X.", "A", "Mesas que bloquean la salida ponen en riesgo a las personas; la autoría de X también hay que corregirla, pero no es un riesgo físico."),
    ],
    [
        ex("Un grupo dice «fue un éxito» sin mostrar datos. ¿Qué le falta? A. Evidencia, como asistencia y comentarios B. Más adjetivos.", "A", "Un puntaje sin datos es una opinión."),
        ex("Una muestra fue pertinente (3), pero 20 de 40 invitados no la vieron porque estaba en un lugar poco concurrido. ¿Es coherente el 3? A. No, el espacio no llegó al público B. Sí.", "A", "Los datos de asistencia contradicen el puntaje."),
    ],
    [
        ex("Quieres mostrar a tus vecinos fotos de una muestra en línea. En una aparece una niña pequeña de frente. ¿Qué haces antes? A. Pedir permiso a una persona adulta responsable o elegir otra foto B. Publicarla igual.", "A", "Se cuida la privacidad de las personas."),
        ex("Una muestra tiene 3 en pertinencia, pero usó solo una vía de invitación y 30 de 60 invitados no supieron del evento. ¿Qué ajuste propones? A. Invitar por más medios y con más anticipación B. Subir el puntaje.", "A", "Los datos de asistencia muestran que la invitación no llegó a todos."),
    ],
    ex("Tu muestra tuvo 8 comentarios con ideas y 2 sin sentido. ¿Qué haces con ellos? A. Leer todos, usar los útiles y comentar los ofensivos con una persona adulta B. Borrar todos sin leer.", "A", "Se aprende de lo útil y se cuida lo ofensivo."),
    [
        ex("Nombra los cuatro criterios de la pauta.", "Pertinencia al público, montaje, aporte a la comunidad y respeto a la autoría y privacidad", "Son los criterios de la clase."),
        ex("Verdadero o falso: un puntaje alto necesita evidencia.", "Verdadero", "La evidencia lo respalda."),
        ex("¿Qué se propone para el criterio más bajo?", "Un ajuste concreto", "Mejora la próxima muestra."),
    ],
    task(
        "Evalúa UNA muestra de ejemplo con la pauta de cuatro criterios (0 a 3). A) «Barrio en colores»: invitaron a 40 y asistieron 30, zona libre de 1 m, 12 comentarios con ideas, todos los autores dieron permiso. B) «Mi calle sonora»: panel en línea, 25 visitas de 60 invitados, fotos oscuras, 5 comentarios, sin datos personales. C) «Manos»: biblioteca, 15 visitas de 20 invitados, zona libre de 60 cm, 3 comentarios, un autor no fue consultado. Escribe un puntaje y una evidencia por criterio, suma el total y propone un ajuste para el criterio más bajo.",
        "Evalué la B. Pertinencia 1: asistieron 25 de 60. Montaje 1: las fotos oscuras se leen mal. Aporte 2: 5 comentarios. Autoría y privacidad 3: sin datos personales. Total: 1 + 1 + 2 + 3 = 7 de 12. Ajuste: volver a fotografiar las obras con luz de ventana y enviar la invitación por más medios.",
        ["asigna puntaje y evidencia a cada criterio", "suma bien el total", "propone un ajuste concreto", "evalúa la difusión y no a las personas"],
        ["pauta con puntajes y evidencias", "ajuste concreto"],
        ["puntaje sin evidencia", "ignorar la privacidad"],
        "Pregunta qué dato respalda cada puntaje y si el ajuste cambia el criterio más bajo.",
    ),
    "Calcula la parte de personas que asistieron a un evento de tu familia si fueron 12 de 16 invitadas.",
    "Escribe cuatro frases con un puntaje y su evidencia para una muestra de ejemplo.",
)

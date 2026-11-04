"""Cuaderno del estudiante de 1.º medio Artes Visuales: AR1M OA 06 (diseño de difusión artística para la comunidad escolar y local)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA6 = "AR1M OA 06"


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
    "Hojas, lápiz de mina y lápices de colores. Los cuatro espacios de difusión de ejemplo (pasillo del liceo, plaza, sala con aforo y galería virtual) y la tarjeta de obra están descritos en esta clase; no necesitas visitar ni buscar nada.",
    "Aprenderé a leer un espacio de difusión artística (su público, su acceso y su propósito) y a escribir la tarjeta de una obra. Sirve para decidir dónde y cómo mostrar un trabajo a mi comunidad.",
    ["Sé que una obra se lee por contexto, lenguaje visual y propósito.", "Sé cuidar la privacidad, el consentimiento y el crédito al mostrar trabajos."],
    [
        "Difundir arte es hacer que un trabajo llegue a otras personas. Puede ser directo, en un lugar físico como un pasillo, una sala o una plaza, o virtual, en una galería de imágenes en pantalla. Antes de decidir miro cuatro cosas. La audiencia: quiénes lo verán, por ejemplo estudiantes, apoderados y vecinos. El acceso: quién puede llegar, a qué hora y si hay rampa o alternativa sin conexión. El propósito: para qué se muestra. Y el cuidado: cómo se protegerán las obras.",
        "Cada espacio tiene ventajas. El pasillo de un liceo es visto a diario por muchos estudiantes, pero el paso es rápido. Una plaza llega a vecinos que no entran al liceo, pero expone las obras al clima. Una sala con aforo limitado, que es la cantidad máxima de personas que caben, permite mirar con calma, pero llega a menos gente. Una galería virtual llega a quienes están lejos, pero requiere conexión y deja fuera a quien no la tiene; por eso conviene sumar una alternativa impresa.",
        "Cada obra lleva una tarjeta de obra: título, autoría (nombre o seudónimo si prefiere), técnica, medidas y un crédito de procedencia si usó un referente. Es corta y se lee en pocos segundos. No incluye datos personales como domicilio ni teléfono. También pienso en el aporte a la comunidad: qué gana quien ve la muestra, por ejemplo conocer el trabajo de sus vecinos o conversar sobre el barrio.",
    ],
    [("difusión", "acción de hacer llegar un trabajo a otras personas"), ("audiencia", "personas que verán o recibirán un trabajo"), ("aforo", "cantidad máxima de personas que caben en un lugar"), ("tarjeta de obra", "texto breve con título, autoría, técnica, medidas y crédito de una obra"), ("aporte a la comunidad", "lo que gana quien participa o ve una muestra")],
    [
        w("Leer un espacio", "Espacio de ejemplo: el pasillo del liceo mide 12 m de largo por 2 m de ancho; pasan unos 480 estudiantes en los recreos; tiene una rampa en cada extremo. Anota audiencia, acceso y una limitación.", ["Audiencia: estudiantes, unos 480.", "Acceso: tiene rampas, pasa gente en los recreos.", "Limitación: el paso es rápido y hay poco espacio para detenerse."], "Audiencia: estudiantes; acceso: con rampas; limitación: paso rápido"),
        w("Escribir una tarjeta", "Obra de ejemplo: grabado de una escalera, hecho por una estudiante con cartón y tinta al agua, 12 cm de alto, copia 3 de 10. Escribe su tarjeta de obra.", ["Título: «La escalera» (de ejemplo).", "Autoría: la estudiante, con su nombre o seudónimo.", "Técnica y medidas: grabado en cartón, 12 cm, copia 3/10."], "«La escalera», autoría de la estudiante, grabado en cartón, tinta al agua, 12 cm, copia 3/10"),
    ],
    [
        m("Elegir el espacio solo porque queda cerca.", "Puede que el público que quiero no pase por ahí.", "Piensa primero en la audiencia y el acceso."),
        m("Poner en la tarjeta de obra la dirección o el teléfono de quien la hizo.", "Expone datos personales.", "Incluye solo título, autoría (o seudónimo), técnica, medidas y crédito."),
    ],
    [
        ex("En la difusión del arte, ¿qué es la audiencia? A. Las personas que verán el trabajo B. El lugar donde se cuelga.", "A", "La audiencia son las personas; el lugar es el espacio."),
        ex("Una sala tiene un aforo de 30 personas. ¿Qué significa?", "Que caben como máximo 30 personas", "El aforo es la cantidad máxima de personas permitidas."),
        ex("¿Qué dato NO debe llevar una tarjeta de obra? A. El teléfono de quien la hizo B. El título.", "A", "Los datos personales no se incluyen."),
    ],
    [
        ex("Una plaza llega a vecinos que no entran al liceo, pero expone las obras al clima. ¿Cuál es su ventaja? A. Llegar a más personas del barrio B. Proteger las obras de la lluvia.", "A", "La plaza abre la muestra a los vecinos; la protección de la lluvia no es su ventaja."),
        ex("Una galería virtual deja fuera a quien no tiene conexión. ¿Qué alternativa ayuda? A. Una versión impresa B. Una versión más pesada.", "A", "Lo impreso no necesita conexión; lo pesado la empeora."),
        ex("¿Cuál de estos es un aporte a la comunidad? A. Que los vecinos conozcan el trabajo de estudiantes del barrio B. Que la muestra tenga muchas luces.", "A", "El aporte es lo que gana quien participa; las luces son un medio."),
    ],
    [
        arith("Una sala con aforo de 30 personas se abre durante 4 recreos y en cada recreo entran 30 personas. ¿Cuántas personas pueden verla en total?", "4 * 30", "Se multiplica el aforo por la cantidad de recreos.", " personas"),
        arith("El pasillo de ejemplo mide 12 m de largo y 2 m de ancho. ¿Cuántos metros cuadrados tiene?", "12 * 2", "El área es largo por ancho.", " m²"),
        arith("Quieres invitar a 120 vecinos a una sala con aforo de 25 personas abierta cuatro tardes, y cada tarde entran solo 25 personas distintas. ¿Cuántos vecinos quedarían sin poder entrar?", "120 - 4 * 25", "Entran 4 × 25 = 100 personas en total y sobran las demás.", " vecinos"),
    ],
    [
        ex("Quieres que vean tu mural personas mayores del barrio que no entran al liceo y que no usan internet. ¿Qué espacio eliges? A. Una muestra en la plaza o en la sede vecinal B. Solo una galería virtual.", "A", "Llega a quienes no usan internet."),
        ex("Un compañero dice: «Mi muestra es para todos» pero la sala solo tiene escaleras. ¿Qué dato de acceso falta?", "Una rampa o una alternativa accesible", "Sin rampa, algunas personas no pueden entrar."),
    ],
    [
        arith("En una galería virtual de ejemplo se suben 12 obras y cada una necesita una tarjeta de 5 líneas. ¿Cuántas líneas se escriben?", "12 * 5", "Se multiplica la cantidad de obras por las líneas de cada tarjeta.", " líneas"),
        ex("Una obra de la muestra usa un referente de ejemplo. ¿Qué debe decir la tarjeta? A. El crédito del referente B. Nada, porque es una obra propia.", "A", "Se reconoce el referente aunque la obra sea propia."),
    ],
    ex("Tu liceo quiere mostrar los trabajos del curso a los apoderados y a los vecinos. Opciones de ejemplo: A) pasillo del liceo en horario de clases; B) sala con aforo de 30 personas, abierta tres tardes con rampa y entrada libre. Los apoderados llegan después de las 17:00. ¿Qué eliges? A. La sala de tarde con rampa B. El pasillo en horario de clases.", "A", "Coincide con el horario de los apoderados y tiene acceso."),
    [
        ex("¿Qué cuatro cosas se miran antes de elegir un espacio de difusión?", "Audiencia, acceso, propósito y cuidado", "Orientan la decisión."),
        ex("Verdadero o falso: una galería virtual llega a todas las personas.", "Falso", "Deja fuera a quienes no tienen conexión."),
        ex("¿Qué datos lleva una tarjeta de obra?", "Título, autoría, técnica, medidas y crédito", "Son los datos mínimos para entender la obra."),
    ],
    task(
        "Elige UN espacio de ejemplo para una muestra del curso. A) Pasillo del liceo: 12 m por 2 m, unos 480 estudiantes, rampas en los extremos. B) Plaza del barrio: abierta, vecinos de todas las edades, sin techo. C) Sala con aforo de 30 personas, rampa, abierta tres tardes. D) Galería virtual de 12 imágenes con una versión impresa. Escribe audiencia, acceso, propósito y una limitación del espacio. Luego escribe la tarjeta de obra de UNA obra de ejemplo (un grabado de 12 cm, copia 3 de 10) con los cinco datos y sin datos personales.",
        "Elegí la sala C. Audiencia: apoderados y vecinos. Acceso: tiene rampa y abre después de las 17:00. Propósito: que conozcan el trabajo del curso. Limitación: solo caben 30 personas a la vez. Tarjeta: «La escalera» (título de ejemplo), autoría de la estudiante, grabado en cartón con tinta al agua, 12 cm, copia 3/10, crédito: sin referente.",
        ["describe audiencia, acceso, propósito y limitación", "elige un espacio coherente con su audiencia", "escribe una tarjeta con los cinco datos", "no incluye datos personales"],
        ["texto de lectura del espacio", "tarjeta de obra"],
        ["elegir el espacio sin pensar en el público", "incluir datos personales"],
        "Pregunta por qué ese espacio sirve a su audiencia y qué dato dejó fuera de la tarjeta.",
    ),
    "Cuenta a una persona de tu casa qué público te gustaría que viera tu trabajo y en qué lugar de tu barrio lo mostrarías.",
    "Escribe en tres frases cómo cambiaría una muestra si pasa de una sala a una galería virtual.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA6, 2,
    "Hojas, lápiz de mina, regla, cinta de papel, cordel, clips y cartulinas. Los datos de montaje están escritos en esta clase; no necesitas buscar nada.",
    "Aprenderé a elegir soportes, alturas, luz y cuidados para montar una muestra, y a preparar una versión virtual con crédito y sin datos personales. Sirve para que las obras se vean bien y queden protegidas.",
    ["Sé leer un espacio de difusión con audiencia, acceso, propósito y cuidado.", "Sé escribir la tarjeta de una obra."],
    [
        "El montaje es la forma de ubicar y sostener las obras en un espacio. Una regla simple de altura es que el centro de la obra quede alrededor de 150 cm del suelo, a la altura de los ojos de la mayoría. Si una obra mide 40 cm de alto, el borde inferior queda a 150 − 20 = 130 cm. En una muestra para niños o para personas en silla de ruedas se baja la altura. Un soporte es lo que sostiene la obra: un muro, una repisa, un panel de cartón o un cordel con clips.",
        "El cuidado de las obras y del lugar viene primero. Uso cinta de papel o clips que se retiran sin dañar el muro ni la obra; no clavo ni pego nada sin permiso de quien administra el lugar; no cuelgo cosas pesadas en altura sin ayuda de una persona adulta ni subo a sillas o mesas inestables. La luz debe iluminar sin encandilar, y la luz directa del sol puede desteñir colores. Las obras frágiles van protegidas del roce y de la humedad.",
        "En una muestra virtual el montaje es digital. Cada imagen va con su tarjeta, un orden de recorrido y un crédito. Solo subo imágenes propias o autorizadas, sin rostros ni datos de ubicación. Reviso que el texto sea legible en una pantalla pequeña. Además dejo una alternativa para quien no tiene conexión: una hoja impresa o una lectura en voz alta. Un montaje bien pensado cuida a las obras, a las personas y al lugar.",
    ],
    [("montaje", "forma de ubicar y sostener las obras en un espacio"), ("soporte", "elemento que sostiene una obra, como un muro, una repisa o un panel"), ("altura de montaje", "distancia desde el suelo hasta el centro de una obra"), ("encandilar", "molestar la vista con una luz demasiado fuerte"), ("recorrido", "orden en que las personas ven las obras")],
    [
        w("Calcular la altura", "Una obra mide 40 cm de alto y su centro debe quedar a 150 cm del suelo. ¿A qué altura queda su borde inferior?", ["La mitad de 40 cm es 20 cm.", "Borde inferior: 150 − 20 = 130 cm."], "130 cm"),
        w("Elegir el soporte seguro", "Para colgar tres grabados en un muro del liceo, ¿cinta de papel o clavos?", ["No tengo permiso para clavar.", "La cinta de papel se retira sin dañar el muro.", "Los grabados son livianos."], "Cinta de papel"),
    ],
    [
        m("Clavar o pegar con pegamento fuerte en el muro del liceo sin permiso.", "Daña el lugar y es una intervención sin autorización.", "Pide permiso y usa cinta de papel o soportes que se retiren."),
        m("Colgar las obras a la altura del techo para que quepan más.", "Nadie las ve bien y hay riesgo al colgarlas.", "Ubica el centro de la obra alrededor de 150 cm del suelo."),
    ],
    [
        ex("En el montaje de esta clase, ¿a qué altura aproximada debe quedar el centro de la obra? A. 150 cm B. 250 cm.", "A", "150 cm es la altura de los ojos de la mayoría; 250 cm queda muy alto."),
        ex("¿Qué es un soporte? A. Lo que sostiene la obra B. El título de la obra.", "A", "Un muro, una repisa o un panel sostienen la obra."),
        ex("¿Qué cuelgas de una cinta de papel sin dañar el muro: un grabado liviano o un espejo pesado?", "Un grabado liviano", "La cinta no soporta un objeto pesado."),
    ],
    [
        arith("Una obra de 60 cm de alto debe tener su centro a 150 cm del suelo. ¿A cuántos centímetros queda su borde inferior?", "150 - 60 // 2", "Primero se calcula la mitad de la altura de la obra y luego se resta de la altura del centro.", " cm"),
        ex("La luz del sol entra directo a un muro y desteñiría los colores de una obra. ¿Qué haces? A. Colgarla en otro muro sin sol directo B. Dejarla porque se ve más clara.", "A", "El sol directo puede desteñir la obra."),
        ex("Debes colgar una obra en un lugar alto que no alcanzas. ¿Qué haces? A. Pido ayuda a una persona adulta B. Subo a una silla inestable.", "A", "No se sube a objetos inestables; se pide ayuda."),
    ],
    [
        arith("Una obra de 30 cm de alto debe tener su centro a 150 cm del suelo. ¿A cuántos centímetros queda su borde superior?", "150 + 30 // 2", "El borde superior queda la mitad de la altura sobre el centro.", " cm"),
        ex("Una muestra será visitada por niños de 1.º básico y por personas en silla de ruedas. ¿Qué haces con la altura del centro de las obras? A. La bajo respecto de 150 cm B. La subo a 180 cm.", "A", "Bajarla permite verlas desde menor altura."),
        ex("Para una galería virtual, ¿cuál de estas imágenes subes? A. Un dibujo propio B. Una foto de un compañero tomada sin permiso, con su casa al fondo.", "A", "La imagen propia no expone a nadie."),
    ],
    [
        ex("Un compañero propone pegar las obras con pegamento fuerte porque «dura más». ¿Qué problema tiene? A. Daña el muro y la obra, y no se puede retirar B. Es muy caro.", "A", "Un montaje debe poder deshacerse sin dañar."),
        ex("Una galería virtual tiene texto en letra muy pequeña. ¿Qué cambias? A. Aumento el tamaño para que se lea en una pantalla pequeña B. Agrego más imágenes.", "A", "La legibilidad en pantalla pequeña es parte del montaje."),
    ],
    [
        arith("Tres obras de 50 cm de alto se cuelgan con su centro a 150 cm del suelo. ¿A cuántos centímetros del suelo queda el borde inferior de cada una?", "150 - 50 // 2", "Se resta la mitad de la altura de cada obra.", " cm"),
        arith("Una muestra tiene 8 obras y 3 son frágiles y se guardan en una vitrina de cartón con tapa. ¿Cuántas obras quedan colgadas en el muro?", "8 - 3", "Se restan las obras frágiles del total.", " obras"),
    ],
    ex("Tu curso monta 6 grabados en un panel de cartón en el pasillo. Cada uno mide 20 cm de alto, con centro a 150 cm. ¿Cuál es el borde inferior? A. 140 cm B. 130 cm.", "A", "150 − 10 = 140 cm."),
    [
        ex("¿A qué altura aproximada queda el centro de una obra en esta clase?", "150 cm", "Es la altura de los ojos de la mayoría."),
        ex("Verdadero o falso: puedo clavar en el muro del liceo si el montaje queda firme.", "Falso", "Hay que pedir permiso y usar soportes que se retiren."),
        ex("¿Qué se deja para quien no tiene conexión en una muestra virtual?", "Una alternativa impresa o una lectura en voz alta", "Así nadie queda fuera."),
    ],
    task(
        "Elige UN montaje de ejemplo. A) Cinco grabados de 20 cm de alto en un panel de cartón del pasillo, con el centro a 150 cm del suelo. B) Una obra de 60 cm de alto en el muro de la sala, que recibe sol directo por la tarde. C) Una galería virtual de seis imágenes con su tarjeta, y una versión impresa. Calcula la altura del borde inferior de cada obra (si corresponde), escribe el soporte que usarías y por qué, un cuidado de las obras, un cuidado del lugar y una medida para que nadie quede fuera. Haz un dibujo del montaje.",
        "Elegí el montaje A. Borde inferior de cada grabado: 150 − 10 = 140 cm. Soporte: panel de cartón con clips, porque se retira sin dañar. Cuidado de las obras: protegerlas de la humedad. Cuidado del lugar: pedir permiso para apoyar el panel. Para que nadie quede fuera: bajar tres grabados para quienes miran desde una silla de ruedas. Dibujé el panel.",
        ["calcula alturas con el 150 cm de referencia", "elige un soporte seguro y reversible", "nombra cuidados de las obras y del lugar", "incluye una medida de acceso"],
        ["cálculo de alturas", "dibujo del montaje", "lista de cuidados"],
        ["clavar sin permiso", "olvidar el acceso"],
        "Pregunta cómo calculó la altura y qué cuidado del lugar consideró.",
    ),
    "Mide en tu casa la altura del suelo a tus ojos y di si coincide con una referencia de 150 cm.",
    "Explica en tres frases por qué conviene bajar la altura de montaje para ciertas audiencias.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA6, 3,
    "Hojas cuadriculadas, regla, lápiz de mina y lápices de colores. Las medidas de las salas y las obras están escritas en esta clase; no necesitas buscar nada.",
    "Aprenderé a probar distribuciones de obras en un plano a escala, a calcular separaciones y a diseñar un recorrido. Sirve para decidir el orden y la ubicación antes de montar.",
    ["Sé calcular la altura de montaje de una obra.", "Sé dibujar a escala con una división simple."],
    [
        "Antes de montar pruebo en un plano a escala. Si el muro mide 600 cm y uso escala 1:50, dibujo 600 ÷ 50 = 12 cm. Para distribuir obras de igual ancho en un muro calculo el espacio libre: muro menos el ancho de todas las obras. Luego lo reparto en una cantidad de huecos que es igual a la cantidad de obras más uno, porque hay un hueco antes de la primera y otro después de la última. Con 3 obras de 100 cm en 600 cm, quedan 600 − 300 = 300 cm de espacio y 3 + 1 = 4 huecos de 300 ÷ 4 = 75 cm.",
        "El recorrido es el camino que sigue el público. Puede ser lineal (de principio a fin), circular o libre. Lo diseño para que haya un comienzo claro y no se formen filas en las entradas. La cartela o texto de sala acompaña a la obra y debe leerse con comodidad: de ejemplo, letras de al menos 1 cm de alto para leerse desde 1 m. Agrupo las obras por tema o por técnica para que la lectura tenga sentido.",
        "Pruebo al menos dos distribuciones y las comparo con un criterio: comodidad al mirar, claridad del recorrido o cuidado de las obras frágiles. Cambio una cosa por prueba y anoto el resultado. Si una distribución deja una obra frágil cerca de la puerta, donde pasa mucha gente, la cambio de lugar. Elijo la que mejor cumple el criterio, no la que se ve más llamativa en el plano.",
    ],
    [("plano a escala", "dibujo que reduce un lugar con una relación fija entre el dibujo y la medida real"), ("recorrido", "camino que sigue el público al ver una muestra"), ("cartela", "texto breve que acompaña a una obra o a una sala"), ("espacio libre", "parte del muro o de la sala que no está ocupada por obras"), ("agrupar", "reunir obras por tema, técnica o color")],
    [
        w("Repartir el espacio", "Un muro mide 600 cm. Quieres colgar 3 obras de 100 cm de ancho cada una, con huecos iguales entre ellas y en los extremos. ¿Cuánto mide cada hueco?", ["Ancho de las obras: 3 × 100 = 300 cm.", "Espacio libre: 600 − 300 = 300 cm.", "Huecos: 3 + 1 = 4; cada uno mide 300 ÷ 4 = 75 cm."], "75 cm"),
        w("Comparar dos recorridos", "Recorrido A: una sola puerta de entrada y salida; recorrido B: entrada por un extremo y salida por el otro, con las obras frágiles al fondo. Criterio: evitar filas. ¿Cuál conviene?", ["Una sola puerta obliga a cruzarse en la entrada.", "Dos puertas separan quien entra de quien sale.", "Al fondo las obras frágiles quedan lejos del paso."], "El recorrido B"),
    ],
    [
        m("Calcular los huecos dividiendo por la cantidad de obras y no por obras más uno.", "Olvida el hueco del extremo y el montaje queda corrido.", "Cuenta un hueco más que obras, pues hay uno antes de la primera y otro después de la última."),
        m("Dejar una obra frágil junto a la puerta donde pasa mucha gente.", "Se roza o se daña.", "Ubícala lejos del paso o en una vitrina."),
    ],
    [
        ex("Un muro mide 800 cm y el plano está a escala 1:50. ¿Cuántos centímetros mide el muro en el plano? A. 16 B. 160.", "A", "800 ÷ 50 = 16 cm."),
        ex("Si cuelgas 4 obras en una fila, ¿cuántos huecos hay contando los extremos? A. 5 B. 4.", "A", "Hay un hueco antes de la primera, tres entre ellas y uno después de la última."),
        ex("¿Qué es una cartela?", "Un texto breve que acompaña a una obra o a una sala", "Ayuda al público a entender lo que mira."),
    ],
    [
        arith("Un muro de 500 cm tendrá 2 obras de 100 cm de ancho. ¿Cuánto mide el espacio libre?", "500 - 2 * 100", "Se resta el ancho total de las obras del largo del muro.", " cm"),
        arith("Con 2 obras en un muro de 500 cm, el espacio libre es de 300 cm y los huecos son 3. ¿Cuánto mide cada hueco?", "300 // 3", "Se reparte el espacio libre en tres huecos iguales.", " cm"),
        ex("Una distribución deja las obras frágiles junto a la puerta. ¿Qué cambias? A. Las muevo lejos del paso B. Las dejo y pongo un cartel.", "A", "Moverlas evita el roce."),
    ],
    [
        arith("Un muro de 720 cm tendrá 4 obras de 90 cm de ancho cada una, con huecos iguales entre ellas y en los extremos. ¿Cuánto mide cada hueco?", "(720 - 4 * 90) // (4 + 1)", "Se resta el ancho total de las obras y se divide por los cinco huecos.", " cm"),
        ex("Una cartela con letra de 5 mm de alto se quiere leer desde 1 m. La referencia es de al menos 10 mm (1 cm). ¿Es legible? A. No, es demasiado pequeña B. Sí, es suficiente.", "A", "5 mm es menos que los 10 mm de referencia."),
        ex("Quieres que el público no forme filas a la entrada. ¿Qué recorrido eliges? A. Entrada por un extremo y salida por el otro B. Una sola puerta para entrar y salir.", "A", "Dos accesos separan los flujos."),
    ],
    [
        ex("Dos distribuciones de 3 obras de 120 cm en un muro de 720 cm. D1: huecos de 90 cm iguales. D2: las 3 obras juntas en un extremo con 360 cm libres. Criterio: comodidad para mirar cada obra. ¿Cuál conviene?", "D1", "Con huecos iguales cada obra tiene espacio propio; juntas se apretujan."),
        ex("Un compañero elige la distribución que «se ve más llamativa en el plano». ¿Qué le falta? A. Un criterio para compararla con otra B. Más color en el plano.", "A", "Sin criterio no hay forma de decidir."),
    ],
    [
        arith("Un muro de 800 cm tendrá 5 obras de 100 cm de ancho cada una, con huecos iguales entre ellas y en los extremos. ¿Cuánto mide cada hueco?", "(800 - 5 * 100) // (5 + 1)", "Se resta el ancho total de las obras y se divide por los seis huecos.", " cm"),
        ex("En un plano a escala 1:50, ¿cuántos centímetros reales representa un hueco dibujado de 2 cm?", "100 cm", "2 × 50 = 100 cm."),
    ],
    ex("Tu curso tiene un muro de 720 cm en el pasillo y 3 grabados enmarcados de 120 cm de ancho cada uno. Quieres huecos iguales. ¿Cuántos centímetros separan cada obra del extremo y de las demás? A. 90 cm B. 120 cm.", "A", "(720 − 360) ÷ 4 = 90 cm; dividir por 3 olvida un hueco."),
    [
        ex("¿Cuántos huecos hay en un muro con 3 obras, contando los extremos?", "4", "Obras más uno."),
        ex("Verdadero o falso: elijo la distribución más llamativa en el plano aunque no la compare con un criterio.", "Falso", "Se elige con un criterio."),
        ex("¿Dónde conviene poner una obra frágil?", "Lejos del paso o en una vitrina", "Se evita el roce."),
    ],
    task(
        "Elige UN problema de ejemplo. A) Un muro de 600 cm y tres grabados de 100 cm de ancho. B) Un muro de 720 cm y cuatro obras de 90 cm. C) Una sala de 6 m por 4 m con dos puertas, cinco obras sobre el muro largo y una obra frágil pequeña. Dibuja en un plano a escala 1:50 dos distribuciones distintas, calcula los huecos y compara con UN criterio (comodidad, recorrido o cuidado de las obras frágiles). Decide cuál montarías y anota un cambio para una segunda versión.",
        "Elegí el problema A. Huecos: (600 − 300) ÷ 4 = 75 cm. En el plano a escala 1:50: obras de 2 cm y huecos de 1,5 cm. Distribución 1: obras con huecos iguales; distribución 2: obras juntas al centro. Criterio: comodidad. Elegí la 1. Segunda versión: agregar una cartela de 1 cm de alto bajo cada obra.",
        ["dibuja dos distribuciones a escala", "calcula los huecos con obras más uno", "compara con un criterio", "decide y propone un cambio"],
        ["dos planos a escala", "cálculo de huecos", "decisión con criterio"],
        ["dividir por la cantidad de obras sin sumar uno", "elegir por lo llamativo"],
        "Pregunta cómo calculó cada hueco y qué criterio decidió entre las dos distribuciones.",
    ),
    "Cuenta a una persona de tu casa por qué en un muro con 3 obras hay 4 huecos.",
    "Cambia la cantidad de obras del ejercicio de 600 cm y recalcula los huecos.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA6, 4,
    "Hojas, lápiz de mina, regla, lápices de colores y cartulinas. El encargo y los datos de la propuesta están escritos en esta clase; no necesitas buscar nada.",
    "Aprenderé a desarrollar una propuesta de difusión para mi comunidad con audiencia, espacio, montaje, cronograma, presupuesto y aporte a la comunidad. Sirve para llevar una muestra de la idea a un plan que se pueda realizar.",
    ["Sé elegir un espacio de difusión y calcular su distribución.", "Sé cuidar las obras, el lugar y la privacidad."],
    [
        "Una propuesta de difusión es un plan para que un trabajo llegue a una comunidad concreta. Tiene siete partes: 1) qué se muestra, 2) a quién va dirigido (audiencia), 3) dónde y en qué modalidad (directa o virtual), 4) cómo se monta, 5) cuándo (cronograma), 6) con qué recursos (presupuesto de materiales y de tiempo) y 7) qué aporta a la comunidad. Cada parte se escribe en una o dos frases y se puede comprobar.",
        "El cronograma ordena el tiempo. Ejemplo con datos de ejemplo: montaje 2 horas el lunes, exposición 3 días, desmontaje 1 hora y devolución del espacio limpio. El presupuesto lista lo que se necesita y cuánto cuesta, priorizando materiales reutilizables. Con precios de ejemplo, 8 cartulinas a $500 cada una son 8 × 500 = $4.000. Con billetes de $1.000, $2.000 y monedas de $500 se puede pagar exactamente esa suma. También anoto quién hace cada tarea.",
        "El aporte a la comunidad responde a una necesidad o deseo del público: que los vecinos conozcan el trabajo de jóvenes del barrio, que se abra una conversación sobre un tema local o que se cuide un lugar común. Pido permiso a quien administra el espacio y cuido la privacidad: sin rostros ni datos personales en afiches, fotos o redes. Dejo anotadas las personas que ayudan y los créditos de referentes.",
    ],
    [("cronograma", "orden de las tareas en el tiempo, con fechas o duraciones"), ("presupuesto", "lista de lo necesario con su costo estimado"), ("modalidad", "forma de realizar una muestra: directa o virtual"), ("responsable", "persona que se hace cargo de una tarea"), ("permiso", "autorización de quien administra un lugar")],
    [
        w("Armar el cronograma", "Datos de ejemplo: montaje 2 horas el lunes, exposición durante 3 días (martes a jueves), desmontaje 1 hora el viernes. ¿Cuántos días dura el proyecto y cuántas horas se trabajan en montaje y desmontaje?", ["Días: lunes, martes, miércoles, jueves y viernes, 5 días.", "Horas de trabajo: 2 + 1 = 3 horas."], "5 días y 3 horas de montaje y desmontaje"),
        w("Calcular el presupuesto", "Para el panel necesitas 8 cartulinas a $500 cada una y 2 rollos de cinta de papel a $1.000 cada uno. ¿Cuánto cuesta en total?", ["Cartulinas: 8 × 500 = $4.000.", "Cinta: 2 × 1.000 = $2.000.", "Total: 4.000 + 2.000 = $6.000."], "$6.000"),
    ],
    [
        m("Pensar que la propuesta está lista porque tiene una buena idea de obras.", "Falta audiencia, permisos, tiempo y recursos.", "Escribe las siete partes y comprueba que cada una sea realizable."),
        m("Olvidar quién hace cada tarea.", "Las tareas sin responsable no se hacen.", "Asigna un responsable por tarea."),
    ],
    [
        ex("¿Qué es un cronograma? A. El orden de las tareas en el tiempo B. La lista de obras.", "A", "El cronograma ordena el tiempo."),
        ex("¿Qué parte de la propuesta responde a «cuánto cuesta lo necesario»?", "El presupuesto", "Lista materiales y costos."),
        ex("Antes de usar el pasillo del liceo para la muestra, ¿qué necesitas? A. Permiso de quien lo administra B. Un afiche con muchos colores.", "A", "No se interviene un lugar sin autorización."),
    ],
    [
        arith("Una muestra necesita 9 cartulinas a $500 cada una. ¿Cuánto cuestan en total?", "9 * 500", "Se multiplica la cantidad por el precio de cada cartulina.", " pesos"),
        arith("Montaje de 2 horas, exposición de 3 días y desmontaje de 1 hora. Si el montaje y el desmontaje se hacen entre 4 personas por igual, ¿cuántos minutos trabaja cada una? (1 hora = 60 minutos)", "(2 + 1) * 60 // 4", "Se suman las horas, se pasan a minutos y se reparten entre 4.", " minutos"),
        ex("Un aporte a la comunidad de una muestra podría ser... A. Que los vecinos conozcan el trabajo de estudiantes del barrio B. Que la muestra use papel de colores.", "A", "El aporte es lo que gana el público."),
    ],
    [
        arith("Necesitas 7 cartulinas a $500 y 2 rollos de cinta de papel a $1.000. ¿Cuál es el costo total?", "7 * 500 + 2 * 1000", "Se suman los costos de cartulinas y de cinta.", " pesos"),
        ex("Tienes $5.000 y el presupuesto de ejemplo es de $5.500. ¿Qué haces? A. Reduzco o reutilizo materiales para ahorrar $500 B. Lo dejo igual y espero que alcance.", "A", "El presupuesto debe ajustarse a los recursos."),
        ex("Tu cronograma pone el montaje el mismo día que otro curso usa el pasillo. ¿Qué haces? A. Cambio el día o coordino con ese curso B. Monto igual.", "A", "Hay que coordinar el uso del espacio."),
    ],
    [
        ex("Una propuesta no indica quién hace cada tarea. ¿Qué parte falta mejorar?", "Los responsables", "Sin responsables, las tareas se pierden."),
        ex("Una propuesta dice «aporte a la comunidad: que se vea bonito». ¿Qué le falta? A. Decir qué gana el público, como conocer el trabajo de los vecinos B. Más color.", "A", "El aporte debe ser algo que la comunidad gane."),
    ],
    [
        arith("Entre 4 personas pagan $6.000 por partes iguales. ¿Cuánto paga cada una?", "6000 // 4", "Se divide el total entre las 4 personas.", " pesos"),
        arith("Quieres pagar $6.000 con billetes de $1.000 y monedas de $500. Pagas 5 billetes de $1.000. ¿Cuántas monedas de $500 faltan?", "(6000 - 5 * 1000) // 500", "5 billetes son $5.000 y faltan $1.000, es decir, 2 monedas de $500.", " monedas"),
    ],
    ex("Tu curso quiere mostrar 20 trabajos a apoderados y vecinos. Propuesta de ejemplo: sala con aforo de 30 personas, rampa, tres tardes, entrada libre. Cada tarde reciben a 30 personas. ¿Cuántas personas pueden visitar la muestra en total? A. 90 B. 60.", "A", "3 tardes × 30 personas = 90."),
    [
        ex("¿Cuáles son las siete partes de una propuesta de difusión?", "Qué se muestra, audiencia, dónde y modalidad, montaje, cronograma, recursos y aporte a la comunidad", "Cubre todo lo necesario para realizarla."),
        ex("Verdadero o falso: una propuesta de difusión necesita permiso del lugar.", "Verdadero", "No se interviene un espacio sin autorización."),
        ex("¿Para qué sirve asignar responsables?", "Para que cada tarea tenga una persona a cargo", "Evita que las tareas se pierdan."),
    ],
    task(
        "Elige UN encargo de ejemplo. A) Muestra de 20 trabajos del curso en una sala con aforo de 30 personas, tres tardes, para apoderados y vecinos. B) Muestra de 12 grabados en un panel de cartón en la plaza durante un fin de semana, con protección contra la lluvia. C) Galería virtual de 15 imágenes con versión impresa para quienes no tienen conexión. Escribe las siete partes de la propuesta, un cronograma con duraciones, un presupuesto con precios de ejemplo (cartulinas a $500, cinta de papel a $1.000) y quién hace cada tarea. Anota el permiso que pedirías y cómo cuidarías la privacidad.",
        "Elegí el encargo A. Qué se muestra: 20 trabajos. Audiencia: apoderados y vecinos. Dónde: sala con rampa, directo. Montaje: paneles con clips y cinta de papel. Cronograma: montaje 2 h el lunes, exposición 3 tardes, desmontaje 1 h el viernes. Presupuesto: 8 cartulinas × $500 = $4.000 y 2 rollos de cinta × $1.000 = $2.000, total $6.000. Responsables: cuatro personas, dos por turno. Permiso: a quien administra la sala. Privacidad: sin rostros en el afiche.",
        ["escribe las siete partes", "arma un cronograma con duraciones", "calcula un presupuesto", "asigna responsables y pide permiso"],
        ["propuesta escrita", "cronograma", "presupuesto"],
        ["no asignar responsables", "no pedir permiso"],
        "Pregunta cómo calculó el presupuesto y qué permiso pedirá.",
    ),
    "Cuenta a una persona de tu casa qué muestra del curso te gustaría hacer para tu barrio y cuánto tiempo necesitarías.",
    "Cambia dos precios del presupuesto y recalcula el total de tu propuesta.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA6, 5,
    "Hojas y lápiz. Las dos propuestas de ejemplo y los criterios están escritos en esta clase; no necesitas buscar nada.",
    "Aprenderé a contrastar propuestas de difusión, directa y virtual, con criterios como pertinencia al público, accesibilidad, cuidado de las obras, viabilidad y aporte a la comunidad. Sirve para elegir y mejorar una propuesta con argumentos.",
    ["Sé armar una propuesta de difusión con siete partes.", "Sé justificar con dato, criterio y conclusión."],
    [
        "Contrastar dos propuestas de difusión es compararlas con los mismos criterios. Uso cinco: pertinencia (si llega al público que quiero), accesibilidad (si pueden participar personas distintas), cuidado (si protege obras, lugar y datos personales), viabilidad (si se puede hacer con el tiempo, los recursos y los permisos) y aporte a la comunidad. Cada criterio se puntúa de 0 a 3 y se justifica con un dato de la propuesta.",
        "Propuesta A, directa: sala del liceo con rampa, aforo de 30 personas, tres tardes, entrada libre, obras con cinta de papel. Propuesta B, virtual: galería de 20 imágenes con tarjetas, sin versión impresa, publicada una semana. En pertinencia, A llega a quienes pueden ir al liceo y B a quienes tienen conexión. En accesibilidad, A tiene rampa y B excluye a quienes no tienen internet. En cuidado, A protege las obras con cinta de papel y B debe cuidar que no se publiquen rostros.",
        "No siempre gana la que suma más. Si una propuesta tiene un 0 en cuidado (por ejemplo, publica fotos de personas sin permiso) debo corregirla antes de realizarla. También puedo combinar lo mejor de ambas: una muestra directa con una galería virtual y una versión impresa. Declaro quién eligió cada criterio y no comparo a las personas que hicieron la propuesta, sino a las propuestas.",
    ],
    [("pertinencia", "grado en que una propuesta llega al público que se quiere alcanzar"), ("accesibilidad", "posibilidad de que personas distintas puedan participar"), ("viabilidad", "posibilidad de realizar una propuesta con el tiempo, los recursos y los permisos que hay"), ("cuidado", "protección de obras, lugar y datos personales"), ("combinar", "tomar lo mejor de dos propuestas para armar una tercera")],
    [
        w("Puntuar la propuesta A", "Propuesta A: sala con rampa, aforo de 30 personas, tres tardes, entrada libre, obras con cinta de papel, permiso ya pedido, aporte: vecinos conocen el trabajo de estudiantes. Puntúa pertinencia 3, accesibilidad 3, cuidado 3, viabilidad 3 y aporte 2. ¿Cuál es el total?", ["Se suman los cinco puntajes.", "3 + 3 + 3 + 3 + 2 = 14 de 15."], "14 de 15"),
        w("Un cero que bloquea", "Propuesta C: galería virtual con fotos de compañeros sin su permiso; pertinencia 3, accesibilidad 2, cuidado 0, viabilidad 3, aporte 3. ¿Se puede realizar?", ["El total es 3 + 2 + 0 + 3 + 3 = 11.", "El 0 en cuidado exige corregir antes.", "Hay que pedir permiso o retirar las fotos."], "No hasta corregir el cuidado, aunque el total sea 11"),
    ],
    [
        m("Elegir la propuesta solo por el total más alto.", "Un cero en cuidado impide realizarla sin corregirla.", "Revisa primero cuidado y viabilidad y luego los demás criterios."),
        m("Decir «la virtual es mejor porque es más moderna».", "No hay dato ni criterio que se pueda comprobar.", "Usa dato, criterio y conclusión."),
    ],
    [
        ex("¿Qué criterio pregunta si personas distintas pueden participar? A. Accesibilidad B. Viabilidad.", "A", "La accesibilidad se refiere a la participación; la viabilidad, a poder realizarla."),
        ex("Una propuesta publica fotos de compañeros sin permiso. ¿Qué criterio falla?", "Cuidado", "Falta proteger los datos personales."),
        ex("¿Cuántos criterios se usan en esta clase para contrastar propuestas?", "5", "Pertinencia, accesibilidad, cuidado, viabilidad y aporte."),
    ],
    [
        arith("Una propuesta recibe pertinencia 2, accesibilidad 3, cuidado 3, viabilidad 2 y aporte 3. ¿Cuánto suma?", "2 + 3 + 3 + 2 + 3", "Se suman los cinco puntajes.", " puntos"),
        ex("La galería virtual no tiene versión impresa. ¿Qué criterio afecta? A. Accesibilidad B. Cuidado.", "A", "Excluye a quienes no tienen conexión."),
        ex("Una propuesta necesita 3 permisos y solo tiene 1. ¿Qué criterio está en riesgo? A. Viabilidad B. Pertinencia.", "A", "Sin los permisos no se puede realizar."),
    ],
    [
        arith("La propuesta X suma 12 puntos y la propuesta Y suma 8. ¿Cuántos puntos de diferencia hay?", "12 - 8", "Se resta el menor del mayor.", " puntos"),
        ex("La propuesta B tiene un 0 en cuidado. ¿Qué cambio concreto la mejora? A. Retirar las fotos de personas o pedir su permiso B. Cambiar el color del fondo.", "A", "Resuelve el problema de datos personales."),
        ex("Quieres combinar lo mejor de A y B. ¿Cuál es una combinación posible? A. Muestra directa con una galería virtual y una versión impresa B. Hacer dos muestras idénticas.", "A", "Combina presencia, alcance y alternativa sin conexión."),
    ],
    [
        ex("Una compañera dice: «Nuestra propuesta es mejor porque es nuestra». ¿Qué le falta?", "Criterios y datos comparables", "Quién la hizo no es un criterio."),
        ex("Dos propuestas empatan en 13 puntos. La A tiene cuidado 3 y accesibilidad 1. La B tiene cuidado 1, porque mostraría fotos de estudiantes sin permiso, y accesibilidad 3. Según la regla de revisar primero el cuidado, ¿cuál se corrige primero?", "La B", "Mostrar fotos sin permiso afecta a las personas y se corrige antes de abrir."),
    ],
    [
        arith("Una propuesta suma 9 puntos de un máximo de 15 en los cinco criterios. ¿Cuántos puntos le faltan para llegar al máximo?", "15 - 9", "Se resta el puntaje obtenido del máximo.", " puntos"),
        ex("Una propuesta tiene cuidado 3, viabilidad 3, accesibilidad 3, pertinencia 1 y aporte 1. ¿Qué criterio mejora primero para llegar mejor al público?", "Pertinencia", "Tiene el puntaje más bajo junto con el aporte, y se refiere a llegar al público."),
    ],
    ex("El curso debe elegir entre dos propuestas. La A suma 14 y la B suma 11, pero la B tiene el mejor aporte (3). El curso desea ambos. ¿Qué proponen? A. Combinar la muestra directa de A con la galería virtual de B B. Elegir al azar.", "A", "Combinar toma lo mejor de cada propuesta."),
    [
        ex("¿Qué cinco criterios se usan en esta clase?", "Pertinencia, accesibilidad, cuidado, viabilidad y aporte a la comunidad", "Cubren el público, la participación, la protección, la realización y el valor."),
        ex("Verdadero o falso: un cero en cuidado se puede ignorar si el total es alto.", "Falso", "Hay que corregirlo antes de realizar la propuesta."),
        ex("¿A quiénes se compara en la contrastación?", "A las propuestas, no a las personas", "El criterio se aplica al trabajo."),
    ],
    task(
        "Compara estas propuestas de ejemplo. A) Sala del liceo con rampa, aforo de 30 personas, tres tardes, entrada libre, obras con cinta de papel, permiso ya pedido. B) Galería virtual de 20 imágenes con tarjetas, sin versión impresa, publicada una semana, con tres fotos de compañeros tomadas sin avisarles. Puntúa de 0 a 3 pertinencia, accesibilidad, cuidado, viabilidad y aporte a la comunidad para cada una, con «dato, criterio, conclusión». Decide cuál realizarías, qué corregirías de la otra y propone una combinación. Escribe una frase sobre consentimiento y crédito para la muestra.",
        "A: pertinencia 3, accesibilidad 3, cuidado 3, viabilidad 3, aporte 2: total 14. B: pertinencia 2, accesibilidad 1, cuidado 0, viabilidad 3, aporte 3: total 9. Realizaría A. En B retiraría las fotos o pediría permiso y agregaría una versión impresa. Combinación: muestra directa con una galería virtual sin fotos de personas. Frase: «Las imágenes se publican con permiso y con crédito de autoría; no se muestran rostros».",
        ["puntúa los cinco criterios en ambas", "justifica con dato, criterio y conclusión", "decide, corrige y combina", "incluye consentimiento y crédito"],
        ["tabla de puntajes", "propuesta combinada", "frase de consentimiento y crédito"],
        ["mirar solo el total", "ignorar el cuidado"],
        "Pregunta qué criterio decidió y qué corrección haría a la propuesta con cero.",
    ),
    "Cuenta a una persona de tu casa por qué un cero en cuidado impide realizar una propuesta aunque el total sea alto.",
    "Redacta tres frases «dato, criterio, conclusión» sobre una muestra que hayas visto.",
)

# ---------------------------------------------------------------- Clase 6
lesson(
    OA6, 6,
    "Hojas, lápiz de mina, lápices de colores, cartulina, cinta de papel y regla. La lista de verificación y los datos de la invitación están escritos en esta clase; no necesitas buscar nada.",
    "Aprenderé a revisar mi propuesta con una lista de verificación, a ensayar el montaje, a comunicar la muestra con una invitación clara y a cerrar con desmontaje y evaluación. Sirve para presentar la muestra a mi comunidad con cuidado.",
    ["Sé armar una propuesta de difusión y contrastarla con criterios.", "Sé calcular alturas, huecos y presupuestos simples."],
    [
        "Antes de abrir una muestra reviso una lista de verificación. Ejemplo con diez puntos: permiso pedido, obras con tarjeta, alturas calculadas, huecos repartidos, obras frágiles protegidas, recorrido claro, rampa o acceso, invitación lista, responsables asignados y plan de desmontaje. Cada punto se marca como hecho, pendiente o no corresponde. Un punto pendiente se resuelve antes de abrir. Hacer un ensayo de montaje con papeles de cartulina como obras muestra problemas de espacio a tiempo.",
        "La invitación comunica la muestra. Responde cinco preguntas: qué (título de la muestra), dónde (lugar y cómo llegar), cuándo (día y hora), para quién (audiencia) y cómo acceder (rampa, entrada libre, versión impresa). Usa letras grandes, contraste alto y pocos elementos. No lleva datos personales ni fotos de personas. Una mediación es una guía breve, hablada o escrita, que ayuda al público a entender las obras, por ejemplo una pregunta en cada cartela.",
        "Al terminar, desmonto con cuidado: retiro cintas y clips sin dañar, devuelvo el espacio limpio y ordenado y entrego las obras a sus autores. Registro el público de manera respetuosa, por ejemplo con un cuaderno de comentarios voluntario y sin datos personales, y evalúo la muestra con tres preguntas: ¿llegó al público previsto?, ¿se cuidaron obras y lugar?, ¿qué aporte dejó a la comunidad? Anoto qué cambiaría la próxima vez. Si hay burlas o conflictos, aviso a una persona adulta de confianza.",
    ],
    [("lista de verificación", "lista de puntos que se marcan como hechos antes de abrir una muestra"), ("ensayo de montaje", "prueba del montaje con papeles u objetos de reemplazo"), ("invitación", "mensaje que dice qué, dónde, cuándo, para quién y cómo acceder"), ("mediación", "guía breve que ayuda al público a entender las obras"), ("desmontaje", "retiro cuidadoso de las obras y devolución del espacio")],
    [
        w("Revisar la lista", "Una lista de ejemplo tiene 10 puntos. Marcaste 7 como hechos, 2 pendientes y 1 que no corresponde. ¿Cuántos puntos debes resolver antes de abrir?", ["Pendientes: 2.", "Los que no corresponden no se resuelven.", "Los hechos ya están."], "2 puntos"),
        w("Escribir una invitación", "Muestra de ejemplo: «Miradas del barrio», sala 3 del liceo, con rampa, jueves 15:00 a 18:00, para apoderados y vecinos, entrada libre. Escribe la invitación con cinco preguntas.", ["Qué: «Miradas del barrio».", "Dónde y cuándo: sala 3 del liceo, jueves de 15:00 a 18:00.", "Para quién y acceso: apoderados y vecinos, entrada libre, con rampa."], "«Miradas del barrio», sala 3 del liceo, jueves 15:00 a 18:00, para apoderados y vecinos, entrada libre y con rampa"),
    ],
    [
        m("Abrir la muestra sin revisar la lista de verificación.", "Pueden quedar permisos, tarjetas o accesos pendientes.", "Marca cada punto y resuelve los pendientes antes de abrir."),
        m("Poner en la invitación fotos de personas o datos personales.", "Expone la privacidad.", "Usa letras, colores y dibujos sin rostros ni datos personales."),
    ],
    [
        ex("¿Qué cinco preguntas responde una invitación? A. Qué, dónde, cuándo, para quién y cómo acceder B. Quién, por qué, cuánto, qué color y qué marca.", "A", "Esas cinco permiten asistir a la muestra."),
        ex("Un punto de la lista está pendiente. ¿Cuándo se resuelve?", "Antes de abrir la muestra", "Un punto pendiente puede afectar a las obras o al público."),
        ex("¿Qué se hace con el espacio al terminar la muestra? A. Se devuelve limpio y ordenado B. Se deja como está.", "A", "El cuidado del lugar incluye devolverlo en buen estado."),
    ],
    [
        arith("Una lista de ejemplo tiene 8 puntos y 5 están hechos. ¿Cuántos puntos no están marcados como hechos?", "8 - 5", "Se restan los hechos del total.", " puntos"),
        ex("Un ensayo de montaje con papeles muestra que las obras no caben en el muro. ¿Qué has logrado? A. Detectar el problema a tiempo B. Perder el tiempo.", "A", "El ensayo permite corregir antes de montar las obras reales."),
        ex("Una mediación breve en la cartela dice: «¿Qué ves primero en esta obra?». ¿Para qué sirve? A. Para invitar al público a mirar con atención B. Para ocupar espacio.", "A", "Guía la mirada del público."),
    ],
    [
        arith("Otra invitación de ejemplo dice «Oficios del barrio, plaza, sábado de 9:00 a 11:00». ¿Cuántas horas dura la muestra?", "11 - 9", "De 9:00 a 11:00 pasan 2 horas.", " horas"),
        arith("La muestra dura 3 horas y entran grupos de 10 personas cada 30 minutos. ¿Cuántas personas ven la muestra en total? (3 horas = 6 grupos de 30 minutos)", "6 * 10", "Se multiplica la cantidad de grupos por las personas de cada uno.", " personas"),
        ex("Quieres un cuaderno de comentarios para el público. ¿Cómo lo haces respetuoso? A. Voluntario y sin pedir datos personales B. Obligatorio y con nombre y teléfono.", "A", "Se respeta la privacidad y la voluntad."),
    ],
    [
        ex("Una invitación tiene diez frases largas, tres fotos de estudiantes y la dirección de una casa. ¿Qué corriges? A. Reduzco el texto y quito fotos y dirección personal B. Agrego más fotos.", "A", "Una invitación clara es corta y no expone datos personales."),
        ex("Durante la muestra alguien se burla de una obra y de quien la hizo. ¿Qué haces? A. Aviso a una persona adulta de confianza B. Me burlo también.", "A", "Las burlas se informan a un adulto."),
    ],
    [
        arith("Hay 36 estudiantes; el montaje se reparte en 6 equipos iguales. ¿Cuántas personas tiene cada equipo?", "36 // 6", "Se divide el total entre los equipos.", " personas"),
        arith("La evaluación de la muestra pregunta «¿llegó al público previsto?». Respondes con datos: se esperaban 90 visitantes y llegaron 72. ¿Cuántas personas menos llegaron?", "90 - 72", "Se resta lo que llegó de lo esperado.", " personas"),
    ],
    ex("Es la mañana de la inauguración y la lista tiene 3 puntos pendientes: permiso de la sala, tarjeta de una obra y rampa móvil. ¿Qué haces primero? A. Resuelvo el permiso de la sala, porque sin él no puedo abrir B. Imprimo más afiches.", "A", "El permiso es lo que define si la muestra puede realizarse."),
    [
        ex("¿Cuáles son las cinco preguntas que responde una invitación?", "Qué, dónde, cuándo, para quién y cómo acceder", "Así la comunidad puede asistir."),
        ex("Verdadero o falso: se abre la muestra aunque queden puntos pendientes si faltan pocos minutos.", "Falso", "Un punto pendiente puede afectar a las obras o a las personas."),
        ex("¿Qué se registra al evaluar la muestra?", "Si llegó al público previsto, si se cuidaron obras y lugar y qué aporte dejó", "Son las tres preguntas de evaluación."),
    ],
    task(
        "Cierra tu proyecto de difusión con UN caso de ejemplo. A) Muestra «Miradas del barrio» en la sala 3 del liceo, con rampa, el jueves de 15:00 a 18:00, entrada libre, 20 trabajos. B) Muestra en la plaza durante un sábado con 12 grabados en un panel protegido de la lluvia. C) Galería virtual de 15 imágenes con versión impresa. Completa una lista de verificación de 10 puntos (hecho, pendiente o no corresponde), escribe la invitación con las cinco preguntas, redacta una mediación breve para una obra, el plan de desmontaje y las tres preguntas de evaluación con una mejora para la próxima vez. No incluyas datos personales ni fotos de personas.",
        "Elegí la muestra A. Lista: 8 puntos hechos, 1 pendiente (tarjeta de una obra) y 1 que no corresponde (vitrina). Invitación: «Miradas del barrio», sala 3 del liceo, jueves de 15:00 a 18:00, para apoderados y vecinos, entrada libre y con rampa. Mediación: «¿Qué ves primero en esta obra?». Desmontaje: retirar cintas, limpiar y entregar las obras. Evaluación: ¿llegó el público previsto?, ¿se cuidó todo?, ¿qué aporte dejó? Mejora: poner más sillas.",
        ["completa la lista de verificación", "escribe la invitación con las cinco preguntas", "incluye mediación y plan de desmontaje", "evalúa con tres preguntas y propone una mejora"],
        ["lista de verificación", "invitación", "plan de desmontaje y evaluación"],
        ["abrir con puntos pendientes", "poner datos personales en la invitación"],
        "Pregunta qué punto estaba pendiente y cómo lo resolvió, y qué mejoraría la próxima vez.",
    ),
    "Cuenta a una persona de tu casa las cinco preguntas que responde una invitación y escribe una breve con un ejemplo.",
    "Escribe qué cambiarías en una muestra que hayas visitado usando las tres preguntas de evaluación.",
)

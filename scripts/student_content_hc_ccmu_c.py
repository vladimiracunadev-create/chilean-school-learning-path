"""Creación y composición musical 3.º y 4.º medio HC: OAC-03 (diseñar y gestionar presentaciones a públicos específicos de creaciones musicales). Presentaciones, programas, guiones y encuestas inventados."""
from __future__ import annotations

from hc_ccmu_common import build

O3 = "AR-CCMU-3y4-OAC-03"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (tres presentaciones de ejemplo, inventadas). "
     "P1, concierto en el patio: público de estudiantes de básica, de pie, durante un recreo; 10 minutos; propósito: entretener e invitar a un taller de música; medios: un parlante pequeño y un cartel. "
     "P2, muestra en la biblioteca: familias y vecinos, sentados y en silencio; 20 minutos, con 4 minutos de bienvenida y 4 piezas de 3 minutos de música más 1 minuto de explicación cada una; propósito: presentar el proceso y los resultados de las piezas; medios: programa de mano impreso y explicación oral. "
     "P3, publicación en línea: personas de otras ciudades que reciben un enlace privado; 5 minutos; propósito: mostrar el resultado; medios: video corto con créditos.")
build(
    O3, 1, F,
    use="Aprenderé a reconocer el público al que se dirige una presentación musical y su propósito, para decidir qué comunicar de mis creaciones y cómo hacerlo.",
    prior=["Sé que una obra tiene un propósito.", "Sé calcular minutos y segundos.", "Sé que no todas las personas escuchan igual ni en las mismas condiciones."],
    explain=[
        "Un público específico es un grupo de personas con características comunes: su edad, lo que saben de música, su cantidad y las condiciones en que escuchan (de pie o sentadas, con ruido o en silencio). Una presentación bien diseñada parte por conocer a su público, porque lo que sirve a un grupo no sirve a otro. Un recreo en el patio pide piezas cortas y claras; una biblioteca con familias permite explicar el proceso con calma.",
        "El propósito de una presentación es lo que se quiere lograr con ella: entretener, invitar, informar, mostrar el proceso o mostrar el resultado. Se comunica con tres cosas: qué se dice (propósito, proceso y resultados de la creación), cómo se dice (lenguaje, duración, medios) y dónde se presenta (espacio y condiciones). Una explicación del proceso incluye las decisiones que se tomaron, como repetir, variar o contrastar.",
        "Diseñar una presentación es distinto de interpretar una obra: aquí se decide para quién, para qué y con qué medios se muestran las creaciones. Si el público es desconocido, lo primero es averiguar quiénes son, cuántos son y dónde se presentará. Todos los datos de este cuaderno son de ejemplo, y el trabajo se hace en papel.",
    ],
    vocab=[("público específico", "grupo de personas con características comunes a quienes se dirige una presentación"), ("propósito", "lo que se quiere lograr con una presentación"), ("proceso", "decisiones y pasos con que se hizo una creación"),
           ("resultado", "obra terminada que se muestra"), ("medio", "canal o soporte con que se comunica la obra"), ("bienvenida", "saludo inicial que presenta al grupo y la actividad")],
    worked=[
        ("Identificar público y propósito", "Un grupo ficticio presentará durante 8 minutos, en una sala y con el curso sentado, cómo suena un tambor. El público es un 1.º básico. ¿Cuál es el público, el propósito probable y la restricción de tiempo?",
         ["El público son estudiantes de 1.º básico sentados en una sala.", "El propósito probable es informar o mostrar cómo suena el tambor, y la restricción es de 8 minutos."],
         "Público: 1.º básico; propósito: mostrar el tambor; tiempo: 8 minutos"),
        ("Calcular cuántas piezas caben", "Una presentación de 15 minutos tiene 2 minutos de bienvenida. Cada pieza ocupa 3 minutos de música más 1 minuto de explicación. ¿Cuántas piezas completas caben?",
         ["Quedan 15 − 2 = 13 minutos para las piezas.", "Cada pieza ocupa 3 + 1 = 4 minutos, y 13 ÷ 4 da 3 piezas completas y sobra 1 minuto."],
         "3 piezas completas"),
    ],
    mistakes=[("Usar la misma presentación para todos los públicos.", "No se piensa en cómo escucha cada grupo.", "Adapta duración, lenguaje y medios al público y al lugar."),
              ("Contar solo el resultado y no el proceso, aunque el propósito pida mostrar el proceso.", "Se olvida revisar el propósito.", "Si el propósito incluye el proceso, comunica también las decisiones que se tomaron.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un público específico?', 'Un grupo de personas con características comunes a quienes se dirige una presentación', 'Cualquier persona que pase por un lugar, aunque no tenga interés en la presentación', 'El grupo de estudiantes que toca las piezas del programa durante la muestra', 'Un público específico se define por sus características y condiciones de escucha.'),
        ('abc', '{F} ¿Cuál es el propósito de P2?', 'Presentar el proceso y los resultados de las piezas', 'Entretener a estudiantes durante un recreo', 'Mostrar solo el resultado con un video', 'La ficha dice que P2 presenta el proceso y los resultados.'),
        ('abc', '{F} ¿En qué presentación el público está de pie y atiende por poco rato?', 'P1, en el patio durante un recreo', 'P2, en la biblioteca, donde el público escucha sentado y en silencio', 'P3, en línea, donde cada persona escucha desde su casa a su propio ritmo', 'Solo P1 tiene público de pie durante un recreo.'),
        ('abc', '{F} ¿Qué medio usa P3 para comunicar?', 'Un video corto con créditos', 'Un programa de mano impreso', 'Un cartel y un parlante pequeño', 'La ficha indica un video corto con créditos para P3.'),
        ('=', '{F} Suma las partes de P2: la bienvenida y las 4 piezas con su música y su explicación. ¿Cuántos minutos dura?', '4+4*(3+1)', 'Se suman los minutos de bienvenida y las cuatro piezas, cada una con música y explicación.', ' minutos'),
        ('abc', '{F} ¿Por qué una explicación larga del proceso es adecuada en P2 y no en P1?', 'Porque en la biblioteca el público está sentado y atento, y en el patio atiende poco rato', 'Porque en el patio el público no entiende nada de música y no necesita explicación', 'Porque P1 no tiene ningún propósito que comunicar y solo se toca por tocar', 'La explicación depende de cuánto tiempo y atención tiene el público.'),
        ('=', '{F} En P1 el grupo reserva 2 minutos para hablar y el resto para piezas de 2 minutos. ¿Cuántas piezas caben?', '(10-2)//2', 'Se restan los minutos de habla y se divide el tiempo restante por la duración de cada pieza.', ' piezas'),
        ('abc', '{F} ¿Qué tipo de pieza conviene más para P1?', 'Una pieza corta, con ritmo claro y energía', 'Una pieza lenta de seis minutos con notas suaves', 'Una explicación de diez minutos sin música', 'El patio pide piezas breves y claras que capten la atención rápido.'),
        ('{F} Escribe el público, el propósito y la duración de P3.', 'Personas de otras ciudades con enlace privado; mostrar el resultado; 5 minutos', 'Son tres datos que la ficha entrega sobre P3.'),
        ('abc', 'Un grupo usa exactamente la misma presentación para el patio, la biblioteca y una reunión en línea. ¿Qué problema tiene?', 'No adapta duración, lenguaje ni medios a cada público y lugar', 'Gasta demasiado dinero en medios impresos y en parlantes para todas las presentaciones', 'Usa instrumentos muy caros que el público no puede apreciar en ningún espacio', 'Cada público escucha en condiciones distintas y una sola presentación no sirve a todos.'),
        ('abc', '{F} En P3 el enlace es privado. ¿Qué ventaja tiene esa decisión?', 'Controla quién puede ver la presentación y resguarda la privacidad de las personas que aparecen', 'Hace que la presentación dure más tiempo y que cada pieza tenga más compases', 'Asegura que todas las personas escuchen con volumen alto desde cualquier lugar', 'Un enlace privado limita el acceso a quienes el grupo eligió.'),
        ('abc', '{F} En P2, ¿qué frase comunica el proceso de una pieza?', 'Esta pieza partió de un motivo de cuatro pulsos que probamos en tres versiones', 'Esta pieza es la mejor que hemos compuesto en todo el año y por eso la elegimos', 'Gracias a todos por venir y por aplaudir tanto al terminar la presentación', 'El proceso se comunica con las decisiones y los pasos de la creación.'),
        ('abc', 'Te piden diseñar una presentación para un público que no conoces. ¿Qué es lo primero que conviene hacer?', 'Averiguar quiénes son, cuántos son y en qué condiciones escucharán', 'Elegir las piezas más difíciles del grupo para que el público note su dominio técnico', 'Preparar un video de veinte minutos con todas las piezas sin pensar en el público', 'Sin conocer al público no se pueden decidir duración, lenguaje ni medios.'),
    ],
    ctx=('abc', 'Te piden presentar en una reunión de apoderados: 15 minutos, personas sentadas y atentas, interesadas en saber cómo trabaja el curso. ¿Qué diseño es el más coherente?', 'Dos piezas con una explicación breve del proceso de cada una y un cierre para preguntas', 'Diez piezas seguidas sin explicación ni preguntas, para aprovechar todo el tiempo', 'Una sola pieza de quince minutos sin presentación del grupo ni explicación de su proceso', 'El público quiere conocer el trabajo del curso, por eso se combinan música y explicación en el tiempo disponible.'),
    sc=[
        ("En Composición musical: ¿qué es el propósito de una presentación?", "Lo que se quiere lograr con ella, como entretener o mostrar el proceso", "El propósito orienta qué comunicar y cómo."),
        ('abc', 'El lugar en que escucha el público y si está de pie o sentado forman parte de:', 'Las condiciones de escucha', 'El título de la pieza', 'La nota del docente', 'Las condiciones de escucha son parte de las características del público.'),
        ("¿Qué tres cosas comunica una presentación de una creación?", "Propósito, proceso y resultados", "Esas tres partes muestran por qué, cómo y qué se hizo."),
    ],
    op=("Elige una de las presentaciones de la {F} y escribe una ficha con su público, su propósito, la duración y dos decisiones que tomarías (por ejemplo, el largo de las piezas y qué explicar). Justifica una decisión con una característica del público.",
        "Elijo P1: público de básica, de pie, en un recreo; propósito: entretener e invitar a un taller; 10 minutos. Decisiones: piezas de 2 minutos con ritmo claro y una invitación de 30 segundos. Justificación: el público de pie atiende poco rato, así que las piezas deben ser cortas.",
        ["identifica público, propósito y duración", "toma dos decisiones coherentes", "justifica con una característica del público"],
        ["hoja con la ficha y las decisiones"],
        ["copiar la ficha sin decisiones", "decidir sin mirar al público", "olvidar el tiempo disponible"],
        "Pregunta: «¿qué característica del público explica esa decisión?». Si no la nombra, pídele que la subraye en la ficha."),
    reinforce="Describe en cuatro líneas dos públicos posibles de un recital escolar y qué cambiarías de la presentación para cada uno.",
    extend="Explica con un ejemplo inventado por qué un mismo propósito puede requerir medios distintos según el público.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (espacios y medios de ejemplo, inventados). Espacios: (a) sala de música: 30 personas sentadas, buena acústica, sin amplificación; (b) gimnasio: 200 personas, mucho eco y un parlante disponible; (c) reunión en línea: 40 personas conectadas por un enlace; la conexión puede fallar. "
     "Medios tradicionales: actuación en vivo, programa de mano impreso (40 copias a $50 cada una) y carteles de papel (5 carteles a $300 cada uno). "
     "Medios emergentes: grabación de audio o video, transmisión en línea y un código QR con los créditos. Reglas del grupo: volumen moderado con pausas y nadie es grabado sin su permiso.")
build(
    O3, 2, F,
    use="Aprenderé a explorar medios, recursos y tecnologías tradicionales y emergentes para presentar mis creaciones, y a elegirlos según el espacio, el público y las posibilidades del grupo.",
    prior=["Reconozco el público y el propósito de una presentación.", "Sé calcular costos con multiplicaciones.", "Sé que grabar a otras personas requiere su permiso."],
    explain=[
        "Un medio de presentación es el canal o soporte con que se comunica una creación. Los medios tradicionales son, por ejemplo, la actuación en vivo, el programa de mano impreso, el cartel y la partitura. Los medios emergentes usan tecnologías más nuevas, como la grabación de audio o video, la transmisión en línea y un código QR (un cuadrado que se escanea con el teléfono para leer información). Ninguno es mejor por ser nuevo: se elige según el propósito, el público y el espacio.",
        "El espacio influye en lo que se oye. Una sala pequeña con buena acústica no necesita amplificación; un gimnasio tiene eco, que mezcla los sonidos, y se ayuda con ritmos claros, un tempo algo más lento y un parlante a volumen moderado. En una conexión en línea el sonido depende de internet, por lo que se prepara un plan B, como una grabación lista para compartir si todas las personas dieron permiso.",
        "Los medios cuestan tiempo y dinero, así que se calcula un presupuesto de ejemplo. También se cuidan la accesibilidad (letras grandes y con buen contraste, y lectura en voz alta para quien no puede leer el programa) y los oídos: volumen moderado y pausas. Este cuaderno no usa software real para grabar o transmitir: lo describe por escrito, y su práctica queda como complemento del docente.",
    ],
    vocab=[("medio tradicional", "canal conocido de presentación, como la actuación en vivo o un programa impreso"), ("medio emergente", "canal que usa tecnologías más nuevas, como la transmisión en línea"), ("acústica", "forma en que un espacio hace oír el sonido"),
           ("eco", "repetición del sonido por rebote en un espacio"), ("presupuesto", "cálculo del dinero necesario para una actividad"), ("accesibilidad", "condiciones que permiten que más personas participen")],
    worked=[
        ("Elegir un medio por el espacio", "Una presentación para 25 personas sentadas en una sala pequeña con buena acústica, con instrumentos suaves. ¿Conviene amplificar?",
         ["Una sala pequeña con buena acústica permite oír bien sin amplificación.", "Amplificar podría subir el volumen sin necesidad y cansar los oídos."],
         "No: se toca en vivo sin amplificar"),
        ("Calcular un costo", "Se imprimen 30 programas a $40 cada uno. ¿Cuánto cuesta en total?",
         ["Se multiplican las copias por el precio de cada una: 30 × 40.", "30 × 40 = 1.200 pesos."],
         "1.200 pesos"),
    ],
    mistakes=[("Elegir un medio porque es nuevo y no porque sirve al propósito.", "Se confunde novedad con adecuación.", "Pregunta qué necesita el público y el espacio antes de elegir el medio."),
              ("Planificar una transmisión en línea sin un plan B.", "La conexión puede fallar y no hay alternativa.", "Prepara una opción, como una grabación previa con permisos o una presentación sin conexión.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un medio de presentación?', 'Un canal o soporte con que se comunica una creación', 'Un instrumento que solo suena en un espacio grande', 'La nota que se pone a una pieza', 'El medio es el canal con que la obra llega al público.'),
        ('abc', '{F} ¿Cuál de estos es un medio emergente?', 'La transmisión en línea', 'El programa de mano impreso', 'El cartel de papel', 'La transmisión en línea usa tecnología más nueva; los otros dos son impresos tradicionales.'),
        ('abc', '{F} ¿Qué espacio tiene mucho eco?', 'El gimnasio', 'La sala de música', 'La reunión en línea', 'La ficha describe el gimnasio con mucho eco.'),
        ('=', '{F} ¿Cuánto cuestan los 40 programas impresos?', '40*50', 'Se multiplican las copias por el precio de cada copia.', ' pesos'),
        ('=', '{F} ¿Cuánto cuestan los 5 carteles?', '5*300', 'Se multiplican los carteles por el precio de cada uno.', ' pesos'),
        ('abc', '{F} ¿En qué espacio es más razonable no usar amplificación?', 'En la sala de música, por su buena acústica y su público pequeño', 'En el gimnasio, por su público de 200 personas y el eco que ayuda a oír mejor', 'En la reunión en línea, porque en una conexión no hay sonido que cuidar', 'La sala pequeña con buena acústica no necesita amplificar.'),
        ('abc', '{F} Si la conexión de la reunión en línea falla, ¿qué plan B es adecuado?', 'Tener lista una grabación previa para compartir, siempre que todas las personas hayan dado permiso', 'Cancelar la presentación para siempre, porque sin conexión no hay cómo mostrar la obra', 'Subir el volumen del parlante del gimnasio hasta que la conexión vuelva a funcionar', 'Una grabación con permisos permite mostrar la obra aunque la conexión falle.'),
        ('abc', '{F} En un espacio con mucho eco, ¿qué decisión ayuda a que se entienda la música?', 'Usar ritmos claros, un tempo algo más lento y el parlante a volumen moderado', 'Tocar lo más rápido y fuerte posible para que el sonido cubra el eco del espacio', 'Quitar toda la dinámica y los silencios para que el sonido sea continuo y parejo', 'El eco mezcla los sonidos; ritmos claros y tempo moderado ayudan a distinguirlos.'),
        ('abc', '{F} Un integrante propone grabar el ensayo con el teléfono y publicarlo en un grupo abierto. ¿Qué falta primero?', 'El permiso de las personas grabadas, tanto para grabar como para publicar', 'Más volumen en el teléfono para que la grabación se escuche con más claridad', 'Un cartel más grande que anuncie que la presentación será grabada y publicada', 'La regla del grupo pide permiso antes de grabar; publicar exige otro permiso.'),
        ('abc', 'El programa impreso tiene letra muy pequeña y una persona del público ve con dificultad. ¿Qué decisión mejora la accesibilidad?', 'Imprimir con letra más grande y buen contraste, y ofrecer lectura en voz alta', 'Quitar el programa impreso y no explicar nada, porque quien no ve bien no lo necesita', 'Imprimir menos copias para que la letra pequeña no llame la atención del público', 'La accesibilidad busca que más personas puedan participar.'),
        ('=', '{F} El grupo dispone de $5.000. Tras comprar los 40 programas y los 5 carteles, ¿cuántos pesos le quedan?', '5000-(40*50+5*300)', 'Se suman los costos de programas y carteles y se restan del dinero disponible.', ' pesos'),
        ('abc', 'Un estudiante dice que, para presentar mejor, siempre hay que usar la tecnología más nueva. ¿Qué es más adecuado?', 'Elegir los medios según el propósito, el público y el espacio, sean tradicionales o emergentes', 'Elegir siempre el medio emergente, porque la tecnología nueva sirve en cualquier situación', 'Elegir siempre el medio más barato, aunque no sirva al propósito ni al público', 'Un medio es bueno si sirve al propósito y al público, sin importar si es nuevo.'),
        ('abc', 'Un parlante en un gimnasio con 200 personas está a todo volumen. ¿Qué decisión cuida a la audiencia y a los intérpretes?', 'Bajar a un volumen moderado, ubicar el parlante lejos de las orejas y hacer pausas', 'Subir aún más el volumen del parlante para vencer el eco con mayor potencia', 'Pedir que nadie hable durante toda la presentación para que el eco desaparezca', 'Volumen moderado y pausas protegen los oídos.'),
    ],
    ctx=('abc', '{F} El curso presentará sus creaciones a 200 estudiantes en el gimnasio. ¿Qué combinación de medios es la más coherente?', 'Actuación en vivo con el parlante a volumen moderado, carteles previos y un programa con los créditos', 'Solo una grabación sin actuación en vivo, enviada al gimnasio en un archivo', 'Solo un programa impreso sin música, porque el espacio tiene mucho eco', 'Combina medios tradicionales adecuados al espacio, con volumen moderado y apoyo impreso.'),
    sc=[
        ("En Composición musical: ¿qué es un medio emergente?", "Un canal que usa tecnologías más nuevas, como la transmisión en línea", "Los medios emergentes usan tecnologías digitales o nuevas."),
        ('abc', 'El código QR con los créditos de una pieza es un medio:', 'Emergente', 'Tradicional impreso', 'Propio de los cantantes', 'Un código QR usa tecnología digital para llevar información.'),
        ("¿Qué se debe tener antes de grabar o publicar la voz de otra persona?", "Su permiso", "Grabar o publicar sin permiso vulnera la privacidad de la persona."),
    ],
    op=("Con la {F}, elige uno de los espacios (a), (b) o (c) y diseña un plan de medios: qué medios tradicionales y emergentes usarías, cuánto costarían los medios impresos y cómo cuidarías los oídos del público. Incluye un plan B.",
        "Espacio (b), gimnasio. Medios: actuación en vivo con el parlante a volumen moderado; 40 programas con créditos ($2.000) y 5 carteles ($1.500). Cuidado: volumen moderado y pausas. Plan B: si el parlante falla, tocamos sin amplificar con dinámica suave.",
        ["elige un espacio y combina medios", "calcula el costo de los medios impresos", "indica el cuidado de los oídos", "incluye un plan B"],
        ["hoja con el plan de medios y el cálculo"],
        ["elegir un medio solo por ser nuevo", "no calcular el costo", "olvidar el plan B"],
        "Pregunta: «¿qué haces si falla el medio principal?». Si no tiene respuesta, pídele que proponga una alternativa simple."),
    reinforce="Anota tres medios, uno tradicional y dos emergentes, que usarías para invitar a tu curso a una muestra de música, y calcula el costo del impreso.",
    extend="Explica con un ejemplo inventado cuándo un medio tradicional puede ser mejor que uno emergente.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (repertorio y condiciones de ejemplo, inventados). Presentación de 18 minutos como máximo. Reglas: 2 minutos de bienvenida al inicio y 1 minuto de transición entre una pieza y la siguiente (cambio de lugar y afinación). "
     "Repertorio: «Marea», 3 minutos, calma; «Pasos», 2 minutos, energía alta; «Eco de patio», 4 minutos, energía media; «Relámpago», 2 minutos, energía alta; «Cierre», 3 minutos, calma. "
     "Propósito: abrir con energía y terminar en calma.")
build(
    O3, 3, F,
    use="Aprenderé a diseñar el programa de una presentación: elegir y ordenar las piezas, repartir el tiempo y planificar las transiciones para comunicar un propósito.",
    prior=["Reconozco público y medios.", "Sé sumar y restar minutos.", "Sé que una pieza puede ser de calma o de energía."],
    explain=[
        "Un programa es el orden de las piezas y de las actividades de una presentación, con su duración. Se diseña a partir del propósito, del público y del tiempo disponible. Primero se suman todas las duraciones: la bienvenida, cada pieza y cada transición, que es el tiempo entre una pieza y la siguiente para cambiar de lugar, afinar o mover objetos. Si el total se pasa del máximo, se acorta, se cambia o se quita una pieza.",
        "El orden de las piezas crea un recorrido de energía. Un programa puede abrir con una pieza energética para captar la atención y cerrar en calma para dejar una sensación de término, o al revés. El orden se decide con el propósito: si busca abrir con energía y terminar en calma, la primera pieza debe ser enérgica y la última, calmada. Cuando se quita una pieza, también se quita una transición.",
        "Un buen programa deja un margen de tiempo para imprevistos, como una afinación más larga. Las transiciones se pueden acortar con preparación: dejar los instrumentos afinados y ubicados antes y ensayar el cambio. El programa se anota por escrito para que todas las personas del grupo sepan qué viene después.",
    ],
    vocab=[("programa", "orden de las piezas y actividades de una presentación, con su duración"), ("transición", "tiempo entre una pieza y la siguiente para prepararse"), ("repertorio", "conjunto de piezas disponibles para presentar"),
           ("margen", "tiempo libre que se deja para imprevistos"), ("energía", "grado de movimiento y fuerza que transmite una pieza"), ("bienvenida", "saludo inicial de la presentación")],
    worked=[
        ("Sumar un programa", "Un programa tiene 1 minuto de bienvenida y tres piezas de 2, 3 y 4 minutos, con 1 minuto de transición entre cada una. ¿Cuántos minutos dura?",
         ["La música suma 2 + 3 + 4 = 9 minutos; con tres piezas hay 2 transiciones de 1 minuto.", "El total es 1 + 9 + 2 = 12 minutos."],
         "12 minutos"),
        ("Ordenar según el propósito", "Se quiere abrir con calma y terminar con energía con tres piezas: «Alba» (calma), «Camino» (media) y «Fiesta» (alta). ¿Qué orden sirve?",
         ["Se parte por la pieza más calmada, «Alba».", "Después sigue la pieza de energía media y se termina con la más enérgica, «Fiesta»."],
         "Alba, Camino, Fiesta"),
    ],
    mistakes=[("Olvidar las transiciones al sumar el tiempo.", "Se cuenta solo la música y el total queda corto.", "Suma bienvenida, piezas y las transiciones entre ellas."),
              ("Quitar una pieza y mantener todas las transiciones.", "Al quitar una pieza sobra una transición.", "Con una pieza menos hay una transición menos.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un programa de presentación?', 'El orden de las piezas y actividades con su duración', 'La nota final de una pieza y el momento en que termina el último compás', 'La lista de los instrumentos del curso y sus rangos de notas disponibles', 'El programa organiza qué se presenta, en qué orden y por cuánto tiempo.'),
        ('abc', '{F} Si se tocan las 5 piezas, ¿cuántas transiciones hay?', '4 transiciones, porque hay una entre cada pieza y la siguiente', '5 transiciones, una por cada pieza que se toca, incluida la última del programa', '6 transiciones, una por pieza y otra extra antes de la bienvenida', 'Hay una transición entre piezas consecutivas, o sea una menos que el número de piezas.'),
        ('abc', '{F} ¿Qué piezas tienen energía alta?', '«Pasos» y «Relámpago»', '«Marea» y «Cierre»', '«Eco de patio» y «Marea»', 'La ficha asigna energía alta a «Pasos» y «Relámpago».'),
        ('=', '{F} Suma la bienvenida, las 5 piezas y las 4 transiciones. ¿Cuántos minutos dura el programa completo?', '2+3+2+4+2+3+4', 'Se suman la bienvenida, los minutos de las cinco piezas y las cuatro transiciones.', ' minutos'),
        ('abc', '{F} ¿Cabe el programa completo en el máximo de 18 minutos?', 'No: se pasa por 2 minutos', 'Sí: dura exactamente 18 minutos', 'Sí: sobran 2 minutos', 'El programa completo dura 20 minutos, así que se pasa por 2 minutos del máximo.'),
        ('abc', '{F} ¿Qué orden de 4 piezas cumple el propósito de abrir con energía y terminar en calma?', '«Pasos», «Eco de patio», «Marea», «Cierre»', '«Marea», «Eco de patio», «Pasos», «Cierre»', '«Cierre», «Pasos», «Eco de patio», «Marea»', 'Empieza con la pieza enérgica y termina con la de calma; los otros órdenes empiezan en calma.'),
        ('=', '{F} Se quita «Relámpago» y una de sus transiciones. ¿Cuántos minutos dura ahora el programa?', '2+(3+2+4+3)+3', 'Se suman la bienvenida, las cuatro piezas que quedan y las tres transiciones.', ' minutos'),
        ('=', '{F} En vez de «Relámpago» se quita «Eco de patio» y una de sus transiciones. ¿Cuántos minutos dura el programa?', '2+(3+2+2+3)+3', 'Se suman la bienvenida, las cuatro piezas que quedan y las tres transiciones.', ' minutos'),
        ('=', '{F} Con las 4 piezas «Marea», «Pasos», «Eco de patio» y «Cierre», ¿cuántos minutos sobran respecto del máximo de 18?', '18-(2+(3+2+4+3)+3)', 'Se calcula el total del programa y se resta del máximo.', ' minuto'),
                ('abc', '{F} Un estudiante propone quitar «Marea» y «Cierre» para que el programa quepa. ¿Por qué contradice el propósito?', 'Porque el propósito pide terminar en calma y esas son las dos únicas piezas de calma', 'Porque son las dos piezas más largas del repertorio y el propósito pide piezas breves', 'Porque toda presentación debe terminar con una pieza de energía alta', 'Sin «Marea» ni «Cierre» no queda ninguna pieza de calma para cerrar el programa.'),
        ('abc', '{F} Con un programa de 17 minutos y un máximo de 18, ¿para qué sirve el minuto que sobra?', 'Para imprevistos, como una afinación más larga', 'Para agregar otra pieza de 3 minutos', 'Para que la bienvenida dure 3 minutos más', 'El margen ayuda a que un imprevisto no deje la presentación fuera del tiempo.'),
        ('abc', '{F} El programa de 17 minutos incluye una bienvenida de 2 minutos. Alguien propone alargarla a 4 minutos. ¿Qué ocurre?', 'El programa pasa a durar 19 minutos y se pasa 1 minuto del máximo', 'El programa dura 17 minutos y sigue igual, porque la bienvenida no cuenta en el total', 'El programa dura 15 minutos, porque se pierden 2 minutos al alargar la bienvenida', 'Alargar la bienvenida en 2 minutos suma 2 al total de 17.'),
        ('abc', 'La transición de 1 minuto entre piezas se alarga porque hay que afinar y mover cosas. ¿Cómo se acorta?', 'Dejando los instrumentos afinados y ubicados antes, y ensayando el cambio', 'Eliminando la afinación de los instrumentos para ahorrar tiempo entre una pieza y otra', 'Subiendo el volumen del parlante para que los cambios se escuchen menos', 'La preparación previa y el ensayo del cambio acortan las transiciones.'),
    ],
    ctx=('abc', 'El acto del liceo da 21 minutos a tu curso: 3 de bienvenida y piezas de 4 minutos, con 1 minuto de transición entre cada una. ¿Cuántas piezas completas caben?', '3 piezas: ocupan 3 + 12 + 2 = 17 minutos', '4 piezas: ocupan 3 + 16 + 3 = 22 minutos, pero igual caben', '5 piezas: ocupan 3 + 20 + 4 = 27 minutos', 'Con 4 piezas se necesitan 22 minutos, más de los 21 disponibles; con 3 piezas ocupan 17 y caben.'),
    sc=[
        ("En Composición musical: ¿qué es una transición en un programa?", "El tiempo entre una pieza y la siguiente para prepararse", "La transición permite cambiar de lugar, afinar o mover objetos."),
        ('abc', 'Con 6 piezas seguidas, ¿cuántas transiciones hay?', '5', '6', '7', 'Hay una menos que el número de piezas, o sea 5.'),
        ("¿En qué se basa el orden de las piezas de un programa?", "En el propósito, el público y el tiempo disponible", "El orden se decide para comunicar lo que se busca al público."),
    ],
    op=("Con la {F}, diseña un programa de 18 minutos como máximo con las piezas que quieras. Escribe el orden, la suma de minutos con bienvenida y transiciones, y una frase que explique cómo se relaciona con el propósito de abrir con energía y terminar en calma.",
        "Orden: «Pasos» (2), «Eco de patio» (4), «Marea» (3), «Cierre» (3). Suma: 2 de bienvenida + 12 de música + 3 transiciones = 17 minutos. Abre con energía alta y termina con dos piezas de calma.",
        ["escribe un orden con piezas de la ficha", "suma bien bienvenida, piezas y transiciones", "no pasa del máximo", "relaciona el orden con el propósito"],
        ["hoja con el programa y la suma"],
        ["olvidar las transiciones", "pasar del máximo de 18 minutos", "no explicar el orden"],
        "Pregunta: «¿cuántas transiciones tiene tu programa y por qué?». Si falla, pídele que cuente los espacios entre piezas."),
    reinforce="Arma un programa de 12 minutos con 3 piezas y 1 minuto de transición, y calcula cuánto tiempo queda para hablar.",
    extend="Explica con un ejemplo inventado cuándo conviene abrir con calma y terminar con energía en vez de lo contrario.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (guion y roles de ejemplo, inventados). Guion del grupo «Marea», presentación de 6 minutos como máximo. "
     "Línea 1: «Hola, somos el grupo Marea; queremos mostrarles cómo una idea de calma se convierte en música.» "
     "Línea 2: «Empezamos con un motivo de cuatro pulsos y probamos tres versiones antes de elegir la tercera.» "
     "Línea 3: «Escuchen cómo el ritmo se mantiene y la melodía cambia.» "
     "Línea 4: se toca la pieza, 3 minutos. "
     "Línea 5: «El resultado cierra con una nota larga, como queríamos.» "
     "Línea 6: «Gracias por escucharnos; pueden hacernos preguntas.» "
     "Tiempos: cada línea hablada dura 30 segundos, salvo la línea 2, que dura 45 segundos. "
     "Integrantes: Ana, Bruno, Camila y Diego. Roles: presentador/a, intérprete de flauta, intérprete de percusión y técnico/a de sonido (cuida el volumen). "
     "Condiciones: Ana toca la flauta; Bruno prefiere no hablar en público y no será técnico; Camila no será presentadora.")
build(
    O3, 4, F,
    use="Aprenderé a escribir un guion breve que comunique el propósito, el proceso y los resultados de una creación, a repartir roles en el grupo y a presentar con claridad.",
    prior=["Sé diseñar un programa con tiempos.", "Reconozco propósito, proceso y resultados.", "Sé trabajar en grupo."],
    explain=[
        "Un guion es el texto que anota lo que se dirá y en qué orden. En una presentación musical, el guion comunica tres cosas: el propósito (qué se quería lograr), el proceso (qué decisiones se tomaron, como repetir, variar o contrastar) y los resultados (cómo suena la obra terminada y qué se logró). Una guía de escucha es una frase que dice al público qué rasgo prestar atención antes de oír la pieza, por ejemplo «escuchen cómo la melodía cambia».",
        "El guion usa frases cortas y claras, adecuadas al público, y se ensaya en voz alta con un reloj para cumplir el tiempo. Se anotan solo puntos clave si se lee de memoria, para no quedarse en blanco. Cada integrante tiene un rol: presentador/a, intérpretes, técnico/a de sonido y quien cuida los tiempos. Los roles se reparten por acuerdo, según lo que cada persona pueda y quiera hacer.",
        "Cuando se presenta con un micrófono o un parlante, el técnico cuida el volumen y evita el acople, que es el silbido agudo que aparece cuando el sonido del parlante vuelve al micrófono. Si ocurre, se baja el volumen o se aleja el micrófono del parlante. Este cuaderno describe el guion por escrito; la práctica real con micrófonos queda para el trabajo en sala del docente.",
    ],
    vocab=[("guion", "texto con lo que se dirá y en qué orden"), ("guía de escucha", "frase que dice al público qué rasgo escuchar"), ("rol", "tarea que tiene cada integrante en la presentación"),
           ("acople", "silbido agudo que aparece cuando el parlante vuelve a sonar en el micrófono"), ("punto clave", "idea importante que se anota para no olvidarla"), ("técnico/a de sonido", "persona que cuida el volumen y el equilibrio del sonido")],
    worked=[
        ("Clasificar una frase", "En un guion ficticio, una línea dice «Hicimos cuatro versiones y escogimos la que repetía menos». ¿Qué comunica: propósito, proceso o resultado?",
         ["La frase habla de las versiones que se hicieron y de cómo se eligió una.", "Describe pasos y decisiones, así que comunica el proceso."],
         "El proceso"),
        ("Repartir roles", "Un trío tiene tres roles: presentador, flauta y percusión. Eva toca flauta, Luis no quiere hablar en público y Mario hace lo que queda. ¿Qué rol tiene cada uno?",
         ["Eva toca la flauta; Luis no habla en público, así que no es presentador y le queda percusión.", "Mario es el presentador."],
         "Eva, flauta; Luis, percusión; Mario, presentador"),
    ],
    mistakes=[("Escribir un guion largo que se lee entero.", "Se pierde contacto con el público y se pasa el tiempo.", "Escribe puntos clave y ensaya en voz alta con reloj."),
              ("Repartir los roles sin conversar.", "Alguien queda en un rol que no puede o no quiere hacer.", "Reparte los roles por acuerdo, según lo que cada persona pueda y quiera hacer.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un guion de presentación?', 'Un texto con lo que se dirá y en qué orden', 'Una partitura completa de la pieza', 'La lista de las personas del público', 'El guion organiza lo que se dirá y el orden de las intervenciones.'),
        ('abc', '{F} ¿Qué línea del guion comunica el propósito?', 'La línea 1', 'La línea 3', 'La línea 6', 'La línea 1 dice que quieren mostrar cómo una idea de calma se convierte en música.'),
        ('abc', '{F} ¿Qué línea comunica el proceso?', 'La línea 2, porque cuenta el motivo inicial y las tres versiones', 'La línea 5, porque habla del final de la pieza que se acaba de tocar', 'La línea 6, porque agradece al público y cierra la presentación', 'La línea 2 relata las decisiones y los pasos de la creación.'),
        ('abc', '{F} ¿Qué línea comunica el resultado?', 'La línea 5, porque dice cómo cierra la pieza terminada', 'La línea 1, porque saluda al público y presenta el nombre del grupo', 'La línea 3, porque pide oír el ritmo y la melodía antes de tocar', 'La línea 5 describe cómo quedó la obra terminada.'),
        ('=', '{F} ¿Cuántos segundos dura todo lo que se habla en las líneas 1, 2, 3, 5 y 6?', '30+45+30+30+30', 'Se suman los segundos de las cinco líneas habladas, con 45 segundos para la línea 2.', ' s'),
        ('=', '{F} Con la pieza de 3 minutos, ¿cuántos segundos sobran respecto del máximo de 6 minutos?', '6*60-(30+45+30+30+30+180)', 'Se suman todas las líneas, incluida la pieza, y se restan de los 360 segundos del máximo.', ' s'),
        ('{F} ¿Qué rol cumple Bruno?', 'Intérprete de percusión', 'No habla en público y no será técnico; Ana toca flauta, así que Bruno es de percusión.'),
        ('{F} ¿Qué rol cumple Diego?', 'Presentador', 'Ana es flauta, Bruno percusión y Camila técnica, así que a Diego le queda presentar.'),
        ('abc', '{F} La línea 3, «Escuchen cómo el ritmo se mantiene y la melodía cambia», cumple la función de:', 'Guía de escucha', 'Propósito', 'Agradecimiento', 'Dice al público qué rasgo escuchar antes de la pieza.'),
        ('abc', '¿Por qué conviene decir antes de tocar qué rasgo escuchar?', 'Porque orienta la atención del público hacia lo importante de la pieza', 'Porque así el público sabe cuánto falta para que termine la pieza', 'Porque reemplaza la explicación del proceso y del resultado', 'La guía de escucha orienta la atención y facilita comprender la obra.'),
        ('abc', '{F} Si el público fuera de estudiantes de básica en un patio, ¿qué ajuste conviene al guion?', 'Frases más cortas y una explicación breve del proceso', 'Frases más largas y técnicas, con todos los nombres de los procedimientos usados', 'Eliminar la pieza y dejar solo el guion, porque el público es de básica', 'Un público de pie que atiende poco necesita mensajes breves.'),
        ('abc', '{F} El grupo agrega una línea hablada de 30 segundos sobre sus referentes. ¿Cabe en el máximo de 6 minutos?', 'No: el total pasa a 375 segundos y se pasa por 15 segundos', 'Sí: el total sigue en 345 segundos, porque una línea hablada no cambia la duración', 'Sí: sobran 30 segundos y todavía caben dos líneas más de ese largo', 'La presentación ya dura 345 segundos; 30 segundos más suman 375, más que los 360 permitidos.'),
        ('abc', 'Un integrante lee el guion de memoria y se queda en blanco. ¿Qué le ayuda?', 'Tener anotados los puntos clave y ensayar en voz alta con reloj', 'Aprender el guion sin ensayar, confiando en recordar cada palabra el día de la presentación', 'Pedirle al público que repita la frase para ganar tiempo hasta recordar la siguiente', 'Los puntos clave y el ensayo dan seguridad y cuidan el tiempo.'),
    ],
    ctx=('abc', 'En la presentación, el técnico de sonido oye un silbido agudo cuando suena el micrófono junto al parlante. ¿Qué decisión es adecuada?', 'Bajar el volumen y alejar el micrófono del parlante', 'Subir el volumen hasta que el silbido desaparezca', 'Pedir a todo el público que se tape los oídos', 'El silbido es acople; se resuelve bajando el volumen o alejando el micrófono del parlante.'),
    sc=[
        ("En Composición musical: ¿qué es una guía de escucha?", "Una frase que dice al público qué rasgo escuchar", "La guía de escucha dirige la atención del público."),
        ('abc', 'Una frase que cuenta las decisiones tomadas al componer comunica:', 'El proceso', 'El resultado', 'El agradecimiento', 'El proceso se comunica con decisiones y pasos.'),
        ("¿Cuál es el rol de quien cuida el volumen y evita el acople?", "Técnico/a de sonido", "Esa persona controla el equilibrio y el volumen del sonido."),
    ],
    op=("Con la {F} como modelo, escribe el guion de una presentación de 5 minutos como máximo de una pieza de 2 minutos, con una frase de propósito, una de proceso, una guía de escucha y una de resultado. Calcula los segundos totales (30 segundos por frase).",
        "Frase 1 (propósito): «Queremos mostrar una idea alegre que cambia al final.» Frase 2 (proceso): «Repetimos un motivo y variamos una nota en la tercera vez.» Frase 3 (guía): «Escuchen la nota larga final.» Pieza: 120 segundos. Frase 4 (resultado): «El final cierra en calma, como buscábamos.» Total: 4 × 30 + 120 = 240 segundos, o sea 4 minutos.",
        ["incluye propósito, proceso, guía de escucha y resultado", "calcula bien los segundos", "no pasa de 5 minutos", "usa frases cortas"],
        ["hoja con el guion y el cálculo de tiempo"],
        ["olvidar la guía de escucha", "pasar del tiempo", "mezclar proceso con resultado"],
        "Pregunta: «¿qué frase comunica el proceso y cuál el resultado?». Si las mezcla, pídele que las separe."),
    reinforce="Escribe cuatro frases de guion para presentar una pieza imaginaria y rotula cada una con propósito, proceso, guía de escucha o resultado.",
    extend="Explica con un ejemplo inventado cómo cambiarías el guion para un público de personas mayores sentadas y otro de estudiantes en un recreo.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 5 (ensayo general de ejemplo, inventado). La muestra comienza a las 15:00. Cronograma: el montaje (instrumentos, sillas, parlante) dura 30 minutos; después se hace la prueba de sonido, que dura 15 minutos; después el grupo descansa 10 minutos y la muestra empieza a las 15:00. "
     "Duraciones medidas en el ensayo general: pieza 1, 190 segundos; pieza 2, 130 segundos; pieza 3, 250 segundos. Límite del programa de música: 9 minutos. "
     "Lista de verificación: afinar la flauta (hecho); probar el parlante (pendiente); imprimir 40 programas (hecho); cargar el teléfono para grabar (pendiente); guardar la pista de respaldo en un archivo local (pendiente). "
     "Plan B: si el parlante falla, se toca sin amplificar con dinámica suave.")
build(
    O3, 5, F,
    use="Aprenderé a hacer un ensayo general, a usar una lista de verificación y un plan B, y a registrar ajustes para que la presentación salga bien.",
    prior=["Sé diseñar un programa con tiempos.", "Sé que los imprevistos pasan.", "Sé registrar versiones y ajustes."],
    explain=[
        "El ensayo general es la ejecución completa de la presentación en condiciones lo más parecidas posible a las reales: con el montaje, el guion, el orden del programa y los tiempos. Sirve para medir cuánto dura cada parte, descubrir problemas y ajustar antes del día de la presentación. Los tiempos se miden con reloj y se anotan en minutos o segundos.",
        "Una lista de verificación (checklist) anota todo lo que debe estar listo y su estado: hecho o pendiente. Revisarla evita olvidos. El plan B es una alternativa preparada para el caso en que algo falle, como tocar sin amplificar si el parlante no funciona. Un cronograma ordena las tareas hacia atrás desde la hora de inicio: se resta el descanso, la prueba de sonido y el montaje para saber a qué hora empezar.",
        "Después del ensayo se registran los ajustes: qué problema se observó, qué se cambió y cómo se comprobó. Los ajustes se priorizan: primero lo que impide la presentación y después lo que la mejora. Todas las cifras de este cuaderno son de ejemplo, y no se usan equipos reales: el trabajo se hace en papel.",
    ],
    vocab=[("ensayo general", "ejecución completa de la presentación en condiciones parecidas a las reales"), ("lista de verificación", "lista de tareas con su estado, hecho o pendiente"), ("plan B", "alternativa preparada si algo falla"),
           ("cronograma", "orden de tareas con sus horas"), ("prueba de sonido", "revisión previa del volumen y el equilibrio"), ("pendiente", "que todavía no se ha hecho")],
    worked=[
        ("Calcular una hora de inicio", "Una presentación comienza a las 16:00. Antes hay 20 minutos de prueba de sonido y 30 de montaje, sin descanso. ¿A qué hora empieza el montaje?",
         ["Se suman los tiempos previos: 20 + 30 = 50 minutos.", "50 minutos antes de las 16:00 son las 15:10."],
         "A las 15:10"),
        ("Aplicar un plan B", "El plan B de un grupo dice: «si falla el proyector del programa, se leen los títulos en voz alta». El proyector falla. ¿Qué hace el grupo?",
         ["El proyector no funciona, así que no se puede mostrar el programa.", "Se aplica el plan B: un integrante lee los títulos en voz alta."],
         "Lee los títulos en voz alta"),
    ],
    mistakes=[("Ensayar solo las piezas y no el montaje ni las transiciones.", "El tiempo real incluye todo lo demás.", "Haz un ensayo general con montaje, guion y transiciones."),
              ("No tener un plan B porque «nunca falla nada».", "Los imprevistos aparecen justo el día de la presentación.", "Prepara una alternativa simple para lo que más podría fallar.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un ensayo general?', 'La ejecución completa de la presentación en condiciones lo más parecidas posible a las reales', 'Un ensayo de una sola pieza en una sala vacía, sin guion ni montaje ni transiciones', 'Una conversación del grupo sobre la presentación en que nadie toca ni usa el programa', 'El ensayo general prueba todo junto: montaje, guion, orden y tiempos.'),
        ('abc', 'En Composición musical: ¿qué es un plan B?', 'Una alternativa preparada para el caso en que algo falle', 'La segunda pieza del programa, que se toca si la primera sale mal', 'Una pieza que se toca más fuerte para tapar un problema del sonido', 'El plan B anticipa un problema con una solución preparada.'),
        ('abc', '{F} ¿Cuántos ítems de la lista de verificación están pendientes?', '3 ítems', '2 ítems', '5 ítems', 'Están pendientes probar el parlante, cargar el teléfono y guardar la pista de respaldo.'),
        ('=', '{F} ¿Cuántos segundos suman las tres piezas en el ensayo general?', '190+130+250', 'Se suman los segundos de las tres piezas medidas.', ' s'),
        ('=', '{F} ¿Cuántos minutos antes de las 15:00 debe comenzar el montaje? Suma el descanso, la prueba de sonido y el montaje.', '30+15+10', 'Se suman los minutos de cada tarea previa a la muestra.', ' minutos'),
        ('abc', '{F} ¿A qué hora debe comenzar el montaje?', 'A las 14:05', 'A las 14:15', 'A las 14:30', '55 minutos antes de las 15:00 son las 14:05.'),
        ('=', '{F} ¿Cuántos segundos se pasan las piezas del límite de 9 minutos?', '190+130+250-9*60', 'Se suman las piezas y se restan los 540 segundos del límite.', ' s'),
        ('abc', '{F} ¿Qué ajuste deja el programa de música exactamente en el límite?', 'Acortar la pieza 3 en 30 segundos', 'Acortar la pieza 1 en 10 segundos', 'Acortar la pieza 2 en 20 segundos', 'Sobran 30 segundos; solo quitar 30 segundos deja 540 en total.'),
        ('abc', '{F} ¿Qué ítem pendiente se relaciona con el plan B?', 'Probar el parlante', 'Imprimir los programas', 'Afinar la flauta', 'Probar el parlante permite saber si hay que aplicar el plan B.'),
        ('abc', '{F} En la muestra el parlante falla. ¿Qué hace el grupo?', 'Aplica el plan B y toca sin amplificar con dinámica suave', 'Sube el volumen de la flauta al máximo para que se oiga igual que con parlante', 'Cancela la muestra sin avisar al público porque no hay amplificación', 'Para eso se preparó el plan B del ensayo general.'),
        ('abc', '¿Por qué conviene hacer el ensayo general con el montaje real?', 'Porque así se descubren problemas y tiempos que no aparecen al ensayar solo las piezas', 'Porque el montaje reemplaza a las piezas y permite no tocar durante el ensayo', 'Porque el ensayo general dura menos que ensayar cada pieza por separado', 'El montaje real revela problemas de tiempo y de espacio.'),
        ('abc', '{F} La prueba de sonido tardó 25 minutos en vez de 15. ¿Qué decisión conserva el descanso de 10 minutos?', 'Empezar el montaje 10 minutos antes, a las 13:55', 'Eliminar el descanso sin decirlo', 'Retrasar la hora de la muestra sin avisar', 'Si la prueba dura 10 minutos más, el montaje debe empezar 10 minutos antes para conservar el descanso.'),
        ('abc', 'Después del ensayo, ¿qué debe quedar registrado de un ajuste?', 'Qué problema se observó, qué se cambió y cómo se comprobó', 'Solo que se cambió algo, sin indicar qué problema se resolvió ni cómo se comprobó', 'Solo quién lo propuso y a qué hora lo hizo, sin importar si funcionó', 'El registro completo permite saber si el ajuste funcionó.'),
    ],
    ctx=('=', '{F} El grupo llega 40 minutos antes de las 15:00 y necesita 30 minutos de montaje y 15 de prueba de sonido. ¿Cuántos minutos le faltan para completar ambas tareas sin considerar el descanso?', '30+15-40', 'Se suman las dos tareas y se resta el tiempo con el que cuentan.', ' minutos'),
    sc=[
        ("En Composición musical: ¿qué es una lista de verificación?", "Una lista de tareas con su estado, hecho o pendiente", "Permite revisar que nada quede sin hacer."),
        ('abc', 'Un cronograma que se calcula hacia atrás desde la hora de inicio:', 'Resta el tiempo de cada tarea previa', 'Suma el tiempo de las piezas', 'Ignora el descanso', 'Se parte de la hora de inicio y se restan las tareas anteriores.'),
        ("¿Qué se prioriza tras un ensayo general?", "Lo que impide la presentación y luego lo que la mejora", "Los problemas graves se resuelven primero."),
    ],
    op=("Con la {F} como modelo, arma el cronograma para una muestra que empieza a las 16:00 con un montaje de 20 minutos, una prueba de sonido de 10 minutos y un descanso de 10 minutos. Calcula la hora de inicio del montaje, escribe una lista de verificación con 3 ítems y un plan B.",
        "Se suman 20 + 10 + 10 = 40 minutos; el montaje empieza a las 15:20. Lista: probar el parlante (pendiente), imprimir programas (hecho), tener la pista de respaldo (pendiente). Plan B: si el parlante falla, tocar sin amplificar con dinámica suave.",
        ["calcula bien la hora de inicio", "lista con tres ítems y su estado", "plan B para un problema posible"],
        ["hoja con el cronograma, la lista y el plan B"],
        ["sumar mal los minutos", "no indicar el estado de la lista", "plan B poco concreto"],
        "Pregunta: «¿qué pasa si algo se atrasa 10 minutos?». Si no sabe, pídele que revise el margen del cronograma."),
    reinforce="Haz una lista de verificación de cinco ítems para una muestra escolar e indica cuáles quedarían pendientes tres días antes.",
    extend="Explica con un ejemplo inventado por qué un plan B simple suele funcionar mejor que uno complicado.",
)

# ============================================================ OAC-03, clase 6
F = ("Ficha 6 (evaluación de una muestra de ejemplo, inventada). Respondieron 20 personas del público una encuesta anónima. "
     "«Entendí el propósito de las piezas»: 16 respondieron sí y 4 no. «El volumen fue adecuado»: 12 sí y 8 no. «La explicación del proceso fue clara»: 15 sí y 5 no. "
     "Comentarios de ejemplo: «La explicación del proceso me ayudó a escuchar mejor»; «en la última pieza el parlante estaba muy fuerte»; «me hubiera gustado leer los créditos». "
     "El grupo quiere publicar un video de 4 minutos con créditos. En el video aparecen 3 integrantes del grupo y 5 personas del público. Los integrantes aceptaron; las 5 personas del público no han dicho nada.")
build(
    O3, 6, F,
    use="Aprenderé a evaluar una presentación con evidencia del público, a dar créditos y a decidir cómo difundir las creaciones respetando los permisos de las personas.",
    prior=["Sé que evaluar es comparar con el propósito.", "Sé dar créditos y pedir permisos.", "Sé leer resultados de una encuesta."],
    explain=[
        "Evaluar una presentación es comparar lo que ocurrió con lo que se quería lograr, usando evidencia. La evidencia puede ser una encuesta anónima al público, observaciones del grupo y comentarios. Una encuesta de pocas personas sirve para mejorar esa presentación, pero no demuestra lo que piensa todo un liceo. Se mira qué aspectos tuvieron más respuestas negativas, porque son los que conviene mejorar primero.",
        "Con la evaluación se arma un plan de mejora: qué se cambiaría la próxima vez, cómo y cómo se comprobaría. Por ejemplo, si el volumen fue lo peor evaluado, se prueba el parlante con el lugar lleno y se baja el volumen de la pieza más fuerte. También se evalúa el proceso del grupo: si los roles funcionaron, si el tiempo alcanzó y si se cumplió el propósito.",
        "Difundir es dar a conocer la obra a un público. Antes se elige el medio según el propósito y los permisos: el permiso de las personas que aparecen en una grabación o video, de los autores de las fuentes y, si son menores de edad, conviene que además lo autorice una persona adulta responsable. Los créditos nombran a quienes participaron con su permiso y a las fuentes que inspiraron la obra. Si alguien no autoriza, no se publica con su imagen o su voz.",
    ],
    vocab=[("evaluación", "comparación de lo ocurrido con el propósito, usando evidencia"), ("encuesta anónima", "preguntas respondidas sin dar el nombre"), ("plan de mejora", "cambios que se harán la próxima vez y cómo se comprobarán"),
           ("difusión", "dar a conocer una obra a un público"), ("crédito", "mención de quienes participaron o inspiraron la obra"), ("permiso", "autorización de una persona para usar su voz o imagen")],
    worked=[
        ("Leer una encuesta", "En una encuesta de ejemplo con 10 personas, 8 respondieron «sí» a «la pieza fue clara» y 2 respondieron «no». ¿Cuántas de cada 5 personas dijeron sí?",
         ["Se compara 8 de 10 con un grupo de 5: 10 se divide en dos grupos de 5.", "Cada grupo de 5 tiene 4 personas que dijeron sí, porque 8 ÷ 2 = 4."],
         "4 de cada 5"),
        ("Decidir sobre un permiso", "Un grupo ficticio grabó a 4 compañeros tocando. Tres aceptan que se publique el video y uno no responde. ¿Qué hace el grupo?",
         ["No tiene permiso de la persona que no respondió.", "Debe preguntarle y respetar su decisión, y no publicar con su imagen o voz mientras no autorice."],
         "No publica con esa persona hasta que ella autorice"),
    ],
    mistakes=[("Concluir que «a todo el liceo le gustó» a partir de 20 respuestas.", "Una muestra pequeña no representa a todas las personas.", "Di lo que muestran esas respuestas y propón cómo ampliar la consulta."),
              ("Publicar un video por considerar que «es solo un video del curso».", "Se omite pedir permiso a quienes aparecen.", "Pregunta a cada persona y respeta una negativa.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es evaluar una presentación?', 'Comparar lo ocurrido con el propósito usando evidencia', 'Decir si la presentación gustó o no gustó a las personas del público', 'Contar cuánta gente asistió y cuántas personas aplaudieron al terminar', 'Evaluar usa evidencia para saber si se cumplió lo que se buscaba.'),
        ('abc', '{F} ¿Qué aspecto de la encuesta tuvo más respuestas negativas?', 'El volumen, con 8 respuestas «no»', 'El propósito, con 4 respuestas «no»', 'La explicación del proceso, con 5 respuestas «no»', 'El volumen tuvo 8 respuestas negativas, más que los otros dos aspectos.'),
        ('abc', '{F} ¿Qué comentario apunta a mejorar el volumen?', 'En la última pieza el parlante estaba muy fuerte', 'La explicación me ayudó a escuchar mejor', 'Me hubiera gustado leer los créditos', 'Solo el segundo comentario habla del parlante y del volumen.'),
        ('=', '{F} ¿Cuántas de cada 5 personas del público entendieron el propósito de las piezas?', '16*5//20', 'Se calcula cuántas personas de cada grupo de 5 respondieron sí, con 16 de 20 respuestas.', ' de cada 5'),
        ('=', '{F} ¿Cuántas personas más respondieron «sí» sobre el propósito que sobre el volumen?', '16-12', 'Se restan los «sí» del volumen a los «sí» del propósito.', ' personas'),
        ('abc', '{F} ¿Qué aspecto conviene priorizar en el plan de mejora?', 'El volumen, porque tuvo más respuestas negativas', 'El propósito, porque tuvo más respuestas positivas', 'Ninguno, porque la encuesta no sirve', 'Se prioriza lo peor evaluado para mejorar primero.'),
        ('abc', '{F} ¿Qué cambio concreto del plan de mejora es coherente con la evidencia?', 'Probar el parlante con la sala llena y bajar el volumen de la última pieza', 'Quitar los créditos de la presentación para que dure menos y se oiga más la música', 'Cambiar el título de la muestra para que el público la recuerde mejor', 'Responde directamente al comentario y a la baja evaluación del volumen.'),
        ('abc', '{F} Un comentario dice que le gustaría leer los créditos. ¿Qué incluyen unos créditos adecuados?', 'Los nombres de quienes participaron con su permiso, las fuentes que inspiraron las obras y la versión presentada', 'Solo el nombre del liceo y el título de la muestra, sin los nombres de quienes participaron', 'La lista de todas las personas del público, aunque no hayan sido consultadas', 'Los créditos reconocen a participantes con permiso y a las fuentes.'),
        ('abc', '{F} Las 5 personas del público que aparecen en el video no han dicho nada. ¿Qué hace el grupo?', 'Les pregunta y, si alguien no autoriza, edita para que no aparezca o no publica el video', 'Publica el video igual, porque la muestra se hizo en un espacio público del liceo', 'Publica el video y avisa después, para que nadie alcance a oponerse', 'Sin permiso no se publica la imagen o la voz de una persona.'),
        ('abc', 'Una persona del público es menor de edad y quiere aparecer en el video. ¿Qué conviene hacer?', 'Además de preguntarle, pedir la autorización de una persona adulta responsable', 'Publicar el video, porque ella aceptó aparecer y con eso basta aunque sea menor de edad', 'No preguntarle a nadie, porque un video escolar no necesita permisos de las personas', 'Para menores de edad conviene sumar la autorización de una persona adulta responsable.'),
        ('abc', '{F} Un integrante afirma: «A todo el liceo le pareció claro el propósito». ¿Qué falla en esa conclusión?', 'La encuesta tiene solo 20 respuestas y no representa la opinión de todo el liceo', 'La encuesta fue anónima, así que ninguna de sus respuestas puede ser válida ni útil', 'No hubo ninguna respuesta negativa, así que no hay nada que mejorar en el propósito', 'Una muestra pequeña sirve para esta presentación, pero no generaliza.'),
        ('abc', 'Dos integrantes discrepan sobre qué mejorar. ¿Qué criterio permite decidir?', 'La evidencia de la encuesta y el propósito de la presentación', 'La opinión de quien habla más fuerte, porque convence rápido al resto del grupo', 'Un sorteo sin mirar los datos, para que ninguna persona del grupo se moleste', 'La evidencia y el propósito dan un criterio compartido.'),
        ('abc', 'El grupo elige entre publicar el video en un enlace privado para familias o en un medio abierto. ¿Qué criterio es más razonable?', 'Elegir según el propósito, el público y los permisos de quienes aparecen', 'Elegir el medio con más gente aunque alguien no haya dado permiso', 'Elegir el medio que menos cueste, aunque no llegue al público pensado', 'La difusión se decide con el propósito, el público y los permisos.'),
    ],
    ctx=('abc', '{F} Los últimos 15 segundos del video de 4 minutos mostrarán los créditos. ¿Qué contenido es el más adecuado?', 'Nombres de quienes aceptaron aparecer, la inspiración general de las piezas y la fecha de la versión', 'Solo la palabra «fin» durante unos segundos, sin ningún nombre ni fuente', 'Nombres de personas que no aceptaron aparecer, para que el grupo quede completo', 'Los créditos reconocen a las personas con su permiso y a las fuentes, e identifican la versión.'),
    sc=[
        ("En Composición musical: ¿qué es un plan de mejora?", "Los cambios que se harán la próxima vez y cómo se comprobarán", "Un plan de mejora convierte la evaluación en acciones concretas."),
        ('abc', 'Una encuesta anónima de 20 personas sirve para:', 'Mejorar esa presentación, pero no demuestra la opinión de todo el liceo', 'Demostrar lo que opina todo el liceo sobre las presentaciones del curso', 'Reemplazar el ensayo general, porque ya muestra cómo salió la presentación', 'Con pocas respuestas no se puede generalizar.'),
        ("¿Qué se necesita antes de publicar la imagen o la voz de una persona?", "Su permiso", "Sin permiso no se publica la imagen o la voz de nadie."),
    ],
    op=("Con la {F}, escribe un plan de mejora con dos cambios basados en la encuesta y una decisión de difusión del video de 4 minutos (qué medio elegirías y qué permisos pedirías). Justifica cada decisión con un dato de la ficha.",
        "Cambio 1: probar el parlante con la sala llena y bajar el volumen de la última pieza, porque 8 de 20 personas dijeron que el volumen no fue adecuado. Cambio 2: agregar créditos impresos, porque un comentario los pidió. Difusión: enlace privado para familias; pediré permiso a las 5 personas del público y publicaré solo con quienes lo autoricen.",
        ["dos cambios coherentes con la evidencia", "decisión de difusión con medio y permisos", "cada decisión usa un dato de la ficha"],
        ["hoja con el plan de mejora y la decisión de difusión"],
        ["generalizar a todo el liceo", "olvidar los permisos", "proponer cambios sin evidencia"],
        "Pregunta: «¿qué dato de la ficha apoya esa decisión?». Si no cita un dato, pídele que lo busque."),
    reinforce="Inventa una encuesta de tres preguntas para el público de una muestra de música y escribe una conclusión prudente de unos resultados imaginarios.",
    extend="Explica con un ejemplo inventado por qué una presentación puede cumplir su propósito aunque el público haya evaluado mal un aspecto técnico.",
)

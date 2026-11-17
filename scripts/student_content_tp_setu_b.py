"""Servicios de Turismo TP 3.º y 4.º medio: OAE-02 (atender a los turistas según sus necesidades). Todo en papel; fichas y precios de ejemplo."""
from __future__ import annotations

from tp_setu_common import build

O2 = "TP-SETU-3y4-OAE-02"

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (de ejemplo, inventada). El módulo de información turística «Costa Norte» atiende en un terminal de buses. Llegan tres grupos: (1) una pareja de personas mayores que pide una caminata corta y plana; "
     "(2) un joven con discapacidad visual que viaja con su hermana y pregunta por visitas guiadas accesibles; (3) un grupo que reclama porque un paseo vendido como de 3 horas duró 2 horas y 15 minutos. "
     "Guía del módulo: saludar, escuchar, preguntar, informar con datos claros y confirmar que la persona entendió. Cada turno es de 8 horas, de pie y con atención continua.")
build(
    O2, 1, F,
    use="Aprenderé en qué contexto se atiende a un turista, qué principios guían el trato (respeto, información veraz, no discriminación y privacidad) y cómo cuidar tu salud al atender público.",
    prior=["Sé que cada persona merece un trato respetuoso.", "Sé que los datos personales son privados.", "Sé restar minutos y horas."],
    explain=[
        "Atender a un turista es identificar lo que necesita y responderle con información clara, veraz y amable. El trabajo se rige por principios: trato respetuoso e igualitario, sin estereotipos ni discriminación; información veraz, que es la verdadera y confirmada, sin prometer lo que no existe; y privacidad, es decir, pedir y anotar solo los datos necesarios. Los derechos de quien consume un servicio dependen de la norma vigente y se informan según corresponda.",
        "El trato respetuoso significa dirigirse a la propia persona y no a su acompañante, preguntarle qué apoyo necesita en lugar de suponerlo, y respetar su decisión. La accesibilidad es que una persona pueda llegar, entrar y usar un lugar o servicio con autonomía. Ante un reclamo, que es la queja de un cliente porque el servicio no fue como se ofreció, se escucha con calma, se registra y se deriva a quien puede resolverlo, sin discutir ni prometer lo que no depende de ti.",
        "Atender de pie ocho horas exige cuidar el cuerpo: alternar posturas, apoyar los pies de forma cómoda y hacer pausas breves programadas. Esto es aprendizaje en papel y no te habilita para atender público de una empresa por tu cuenta.",
    ],
    vocab=[("accesibilidad", "que una persona pueda llegar, entrar y usar un lugar o servicio con autonomía"), ("información veraz", "información verdadera y confirmada"), ("reclamo", "queja de un cliente porque el servicio no fue como se ofreció"), ("trato igualitario", "atender con el mismo respeto a todas las personas"), ("estereotipo", "idea fija y simple sobre un grupo de personas"), ("pausa activa", "descanso breve para estirar el cuerpo")],
    worked=[
        ("A quién se responde", "Una turista que usa silla de ruedas llega con un amigo y pregunta por el horario de un museo. ¿A quién le respondes?", ["La pregunta es de ella y la información es para ella.", "Se le responde a ella, mirándola, y si quiere puede incluir a su amigo."], "A la turista que preguntó"),
        ("Dato no confirmado", "Un turista de ejemplo pregunta si un museo tiene baño accesible y no tienes el dato. ¿Qué dices?", ["No se asegura algo sin confirmar.", "Se explica que no tienes el dato confirmado y se consulta al museo o se entrega su contacto."], "Que no tienes el dato confirmado y lo consultarás"),
    ],
    mistakes=[("Responderle al acompañante en vez de a la persona que preguntó.", "Se le quita autonomía a la persona y se supone que no puede comunicarse por sí misma.", "Dirígete a quien preguntó y pregúntale qué apoyo prefiere."),
              ("Asegurar que un lugar es accesible para «no quedar mal».", "Si no es cierto, la persona llega y no puede usar el servicio.", "Si no lo sabes, dilo y consúltalo antes de responder.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es la accesibilidad?", "Que una persona pueda llegar, entrar y usar un lugar o servicio con autonomía", "Que el servicio sea el más barato de la zona", "Que el lugar esté abierto todos los días", "La accesibilidad se refiere al acceso y uso autónomo, no al precio ni a los días de apertura."),
        ("abc", "En Servicios de Turismo: ¿qué es una información veraz?", "La que es verdadera y está confirmada, sin prometer más de lo que existe", "La que suena más atractiva para vender el servicio", "La que se recuerda de memoria sin revisar", "Veraz significa verdadera y confirmada; recordar o adornar no la garantiza."),
        ("abc", "En un módulo de información, ¿qué es un reclamo?", "La queja de un cliente porque el servicio no fue como se ofreció", "La pregunta de un turista por un horario", "La sugerencia de un nuevo atractivo", "El reclamo expresa disconformidad por lo ofrecido; preguntar un horario es solo una consulta."),
        ("abc", "{F} ¿Qué haces al atender al joven con discapacidad visual?", "Preguntarle directamente a él qué necesita y qué apoyo prefiere", "Hablarle solo a su hermana, porque ella ve", "Sugerirle que mejor no haga visitas guiadas", "Se trata a cada persona con autonomía: se le pregunta a ella y no se decide por ella."),
        ("abc", "{F} ¿Qué haces con la pareja que pide una caminata corta y plana?", "Ofrecerles opciones que cumplan su pedido y preguntar cuál prefieren", "Recomendarles la caminata más larga porque es la más popular", "Decirles que las personas mayores no pueden caminar", "Se responde a lo que piden y se respeta su elección, sin estereotipos por la edad."),
        ("abc", "{F} No sabes si una visita guiada tiene acceso adaptado. ¿Qué corresponde?", "Decir que no tienes el dato confirmado y consultarlo antes de responder", "Asegurar que sí lo tiene para no quedar mal", "Decir que no lo tiene sin consultar", "Sin confirmación no se afirma ni se niega; se consulta y se informa lo verificado."),
        ("=", "{F} ¿Cuántos minutos menos duró el paseo respecto de lo que se vendió?", "3*60-(2*60+15)", "Se pasan ambas duraciones a minutos y se restan.", " minutos"),
        ("abc", "{F} ¿Qué haces primero ante el reclamo del grupo?", "Escucharlos con calma, registrar el reclamo y derivarlo a quien lo resuelve", "Explicar que el reclamo no corresponde, sin escucharlos", "Prometer una devolución de dinero ahora mismo", "El reclamo se escucha y se registra; la devolución depende de quien tiene la autoridad para decidirla."),
        ("ab", "Quienes atienden de pie todo el turno, ¿qué medida cuida su cuerpo?", "Alternar posturas y hacer pausas breves programadas", "Permanecer inmóvil y sin pausas para no perder clientes", "Las pausas y el cambio de postura previenen molestias en jornadas largas de pie."),
        ("abc", "{F} Un turista pide el teléfono de la familia que atendiste antes, «para saludarla». ¿Qué haces?", "No lo entrego, porque son datos personales de otra persona", "Se lo doy, porque el motivo es amistoso", "Se lo doy si me promete no usarlo mal", "Los datos de otra persona no se entregan sin su autorización, sea cual sea el motivo."),
        ("abc", "{F} Uno de los reclamantes levanta la voz. ¿Qué técnica corresponde?", "Mantener un tono calmado, reconocer su molestia y explicar el siguiente paso concreto", "Responder también con voz fuerte para hacerte respetar", "Retirarte del módulo sin decir nada", "Un tono calmado baja la tensión y el paso concreto da una salida; gritar o irse la empeora."),
        ("abc", "Un compañero dice: «a los turistas extranjeros no hay que explicarles tanto». ¿Qué corresponde?", "Atender con el mismo respeto y claridad a todas las personas, sin estereotipos", "Explicarles solo si insisten", "Darles información más corta que a los demás", "El trato igualitario exige la misma calidad de información para todos."),
        ("abc", "Una persona con sordera llega sola y se comunica escribiendo en su teléfono. ¿Qué corresponde?", "Preguntarle cómo prefiere comunicarse y usar ese medio", "Hablarle muy fuerte y exagerar los gestos", "Pedir que venga otra persona a hablar por ella", "Cada persona sabe cómo se comunica mejor; se le pregunta y se respeta."),
    ],
    ctx=("abc", "{F} Una compañera del módulo dice: «los reclamos son una pérdida de tiempo, que se vayan». ¿Qué respondes?", "Que los reclamos muestran qué mejorar y se escuchan, registran y derivan", "Que tiene razón, si el grupo es muy exigente", "Que solo se registran los reclamos de clientes frecuentes", "Atender y registrar reclamos es parte del estándar de calidad, y se hace con todos."),
    sc=[
        ("En Servicios de Turismo: ¿a quién le respondes si pregunta una persona con acompañante?", "A la persona que preguntó", "Se respeta su autonomía y se le pregunta qué apoyo necesita."),
        ("¿Qué haces ante un reclamo?", "Escucho con calma, registro y derivo a quien puede resolverlo", "No se discute ni se promete lo que no depende de ti."),
        ("¿Qué haces si no tienes un dato confirmado?", "Lo digo y lo consulto antes de responder", "Afirmar sin confirmar puede perjudicar al turista."),
    ],
    op=("Diseña una tarjeta de atención de 5 pasos para el módulo «Costa Norte» (saludo, escucha, pregunta, información, cierre) y aplícala a este caso de ejemplo: una señora mayor pregunta cómo ir al muelle y dice que se cansa si camina mucho. Escribe una frase para cada paso.",
        "Saludo: «Buenas tardes, ¿en qué le puedo ayudar?». Escucha: «Entiendo que busca llegar al muelle sin caminar mucho». Pregunta: «¿Prefiere ir en micro o en taxi colectivo?». Información: «La micro la deja a una cuadra; el horario es el del paradero que está aquí». Cierre: «¿Le queda alguna duda? Aquí tiene el mapa».",
        ["incluye los cinco pasos con una frase cada uno", "usa un trato respetuoso, sin suponer", "la información responde a lo que ella pidió"],
        ["tarjeta con los cinco pasos y la aplicación al caso"],
        ["decidir por ella sin preguntar", "dar información que no se pidió", "olvidar el cierre con la confirmación"],
        "Pregunta: «¿en qué paso preguntas qué prefiere?». Si no responde, repasa los cinco pasos de la guía del módulo."),
    reinforce="Anota una situación en que te trataron muy bien al pedir información y qué hizo bien la persona.",
    extend="Explica con un ejemplo inventado por qué preguntar a la persona qué apoyo necesita es mejor que suponerlo.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (de ejemplo, inventada). Tres turistas se acercan al módulo. El turista A dice: «Necesito un lugar sin escalones para pasear con mi hijo, que usa silla de ruedas». "
     "El turista B dice: «Me encantaría ver un atardecer en la costa, si se puede». El turista C, que viaja con otras 2 personas (3 en total), dice: «Deme el horario del bus a la Isla de Ejemplo de mañana a las 9». "
     "El folleto de la isla indica: paseo en lancha de 2 horas, con un prestador autorizado, $12.000 por persona. El módulo tiene un registro de reclamos y sugerencias.")
build(
    O2, 2, F,
    use="Aprenderé a distinguir necesidad, deseo y demanda del turista, a usar escucha activa, preguntas abiertas y cerradas y paráfrasis, y los documentos y roles de la atención.",
    prior=["Sé que debo tratar con respeto a todas las personas.", "Sé multiplicar con números enteros.", "Sé que se informa solo lo confirmado."],
    explain=[
        "Un turista puede expresar tres cosas distintas. La necesidad es lo indispensable para poder usar el servicio, como el acceso sin escalones. El deseo es lo que le gustaría vivir, como ver un atardecer. La demanda es lo que pide de forma concreta, como el horario de un bus. Distinguirlas ayuda a responder en el orden correcto: primero lo indispensable, luego lo concreto y, si es posible, lo deseado.",
        "La comunicación efectiva usa tres técnicas. La escucha activa es prestar atención completa sin interrumpir. La pregunta abierta deja responder con libertad («¿qué le gustaría conocer?») y la cerrada se responde eligiendo o con sí o no («¿prefiere mirador o playa?»). Parafrasear es repetir con tus palabras lo que dijo la persona para comprobar que entendiste, sin agregar suposiciones. En inglés, una frase cortés para ofrecer ayuda es «Hello, how can I help you?».",
        "Los documentos de apoyo son el folleto, con datos de un atractivo; el mapa; la ficha de atención, donde se anota lo atendido sin datos innecesarios; y el registro de reclamos y sugerencias. El rol de quien informa es orientar con datos verificados; si algo excede su rol, lo deriva al supervisor.",
    ],
    vocab=[("necesidad", "lo indispensable para usar un servicio"), ("deseo", "lo que a la persona le gustaría vivir"), ("demanda", "lo que la persona pide en forma concreta"), ("escucha activa", "atención completa a lo que dice la persona, sin interrumpir"), ("parafrasear", "repetir con tus palabras lo que dijo la persona"), ("pregunta abierta", "pregunta que permite responder con libertad"), ("pregunta cerrada", "pregunta que se responde eligiendo o con sí o no"), ("registro de reclamos y sugerencias", "documento donde se anotan quejas e ideas de mejora")],
    worked=[
        ("Clasificar lo que dice", "Un turista de ejemplo dice: «Quisiera un paseo en bote si hay tiempo». ¿Es necesidad, deseo o demanda?", ["La palabra «quisiera» y la condición «si hay tiempo» indican algo que le gustaría.", "No es indispensable ni un pedido puntual."], "Un deseo"),
        ("Parafrasear", "Una turista de ejemplo dice: «Busco algo tranquilo, sin mucha gente, para ir con mi mamá». ¿Cómo parafraseas?", ["Se repite con otras palabras lo esencial.", "«Entonces busca un lugar tranquilo y poco concurrido para ir con su mamá, ¿es así?»."], "«Entonces busca un lugar tranquilo y poco concurrido, ¿es así?»"),
    ],
    mistakes=[("Responder al deseo del turista antes de resolver su necesidad.", "Si no se resuelve lo indispensable, el resto no sirve.", "Primero confirma la necesidad y luego ofrece lo deseado."),
              ("Parafrasear agregando algo que la persona no dijo.", "Es una suposición, no una comprobación.", "Repite solo lo que la persona dijo y pregunta si es así.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es la escucha activa?", "Prestar atención completa a lo que dice la persona y comprobar que se entendió", "Responder rápido para no hacer esperar a la fila", "Escuchar solo la primera frase y completar el resto", "La escucha activa exige atender sin interrumpir; apurarse o suponer la reemplaza mal."),
        ("abc", "En Servicios de Turismo: ¿qué es parafrasear?", "Repetir con tus palabras lo que dijo la persona para confirmar que se entendió", "Repetir exactamente la misma frase en voz más alta", "Cambiar el tema para sonar más amable", "Parafrasear confirma la comprensión con otras palabras, sin suponer."),
        ("abc", "En Servicios de Turismo: ¿qué es una pregunta abierta?", "La que permite responder con libertad, como «¿qué le gustaría conocer?»", "La que se responde solo con sí o no", "La que se hace al final de la atención", "La pregunta abierta deja explicar; la cerrada se responde eligiendo o con sí o no."),
        ("abc", "{F} El turista A dice que necesita un lugar sin escalones para su hijo. ¿Qué expresa?", "Una necesidad, porque es algo indispensable para poder usar el lugar", "Un deseo, porque habla de lo que le gustaría", "Una queja por un servicio anterior", "Sin acceso sin escalones no podrían usar el lugar; por eso es indispensable."),
        ("abc", "{F} ¿Cuál es el deseo que aparece en la ficha?", "Ver un atardecer en la costa", "Un horario de bus a la isla", "Un lugar sin escalones", "«Me encantaría» expresa lo que le gustaría vivir; las otras son necesidad y demanda."),
        ("abc", "{F} ¿Qué expresa el turista C al pedir el horario del bus de mañana a las 9?", "Una demanda, porque pide algo concreto y puntual", "Una necesidad de accesibilidad", "Un deseo de turismo aventura", "El pedido concreto de un horario es una demanda."),
        ("=", "{F} ¿Cuántos pesos pagan por el paseo en lancha las 3 personas del turista C, según el folleto?", "3*12000", "Se multiplica el valor por persona por la cantidad de personas.", ""),
        ("abc", "{F} ¿Qué pregunta cerrada sirve para acotar la opción del turista B?", "¿Prefiere verlo desde un mirador al que se llega en auto o desde la playa?", "¿Qué le gustaría ver?", "¿Cuénteme cómo le fue en su último viaje?", "La pregunta cerrada ofrece alternativas para elegir; las otras dos son abiertas."),
        ("abc", "{F} Para comprobar que entendiste al turista A, ¿cuál es una paráfrasis adecuada?", "Entonces busca un lugar sin escalones para pasear con su hijo, ¿es así?", "Entonces busca el lugar más barato, ¿es así?", "Entonces su hijo no puede hacer ningún paseo, ¿es así?", "La paráfrasis repite lo dicho; las otras agregan datos o suposiciones que no dijo."),
        ("ab", "¿Qué documento sirve para anotar quejas e ideas de mejora de los turistas?", "El registro de reclamos y sugerencias", "El folleto de un atractivo", "El folleto informa sobre un atractivo; las quejas e ideas se anotan en el registro."),
        ("ab", "¿Cuál es una forma cortés y básica de ofrecer ayuda en inglés?", "Hello, how can I help you?", "Goodbye, see you tomorrow.", "La primera frase saluda y ofrece ayuda; la segunda es una despedida."),
        ("abc", "{F} Los turistas A y C llegan a la vez. ¿Qué haces?", "Saludo a ambos, indico a quién atiendo primero y pido unos minutos a la otra persona", "Atiendo solo al que habló más fuerte", "Les pido que vuelvan en una hora", "Un saludo a ambos y un orden claro mantienen el respeto y la atención de calidad."),
        ("abc", "Un turista dice: «no entiendo nada de lo que me explicas». ¿Qué técnica corresponde?", "Repetir con frases más simples y apoyarme en un mapa o por escrito", "Repetir lo mismo en voz más alta", "Cambiar de tema para no incomodarlo", "Adaptar el mensaje al turista, con frases simples y apoyos visuales, mejora la comunicación."),
    ],
    ctx=("abc", "Una turista dice: «Quiero que mi hija conozca algo de la cultura de la zona, no sé qué». ¿Qué es lo más adecuado para empezar?", "Hacerle una pregunta abierta sobre qué le interesa y cuánto tiempo tienen", "Entregarle los diez folletos del módulo", "Recomendarle lo más caro", "Una pregunta abierta aclara sus intereses antes de ofrecer opciones."),
    sc=[
        ("En Servicios de Turismo: ¿qué diferencia hay entre necesidad y deseo?", "La necesidad es indispensable y el deseo es lo que le gustaría", "Primero se resuelve la necesidad y luego el deseo."),
        ("En la atención a turistas, ¿para qué sirve parafrasear lo que dijo la persona?", "Para comprobar que entendiste lo que dijo la persona", "Se repite con tus palabras sin agregar nada."),
        ("¿Qué es una pregunta cerrada?", "La que se responde eligiendo o con sí o no", "Sirve para acotar las opciones del turista."),
    ],
    op=("Una turista de ejemplo dice: «Vengo con mi papá, que camina despacio, y me gustaría algo cultural, no muy lejos; ¿hay museo abierto mañana?». Separa en una tabla su necesidad, su deseo y su demanda, escribe una paráfrasis y una pregunta cerrada para acotar.",
        "Necesidad: un lugar donde su papá pueda ir caminando despacio, no muy lejos. Deseo: algo cultural. Demanda: saber si hay un museo abierto mañana. Paráfrasis: «Entonces busca un museo cercano, abierto mañana, que sea cómodo para su papá, ¿es así?». Pregunta cerrada: «¿Prefiere ir por la mañana o por la tarde?».",
        ["clasifica correctamente necesidad, deseo y demanda", "la paráfrasis no agrega suposiciones", "la pregunta cerrada ofrece alternativas concretas"],
        ["tabla con las tres columnas, la paráfrasis y la pregunta"],
        ["confundir la demanda con el deseo", "suponer que su papá no puede caminar", "hacer una pregunta abierta en vez de cerrada"],
        "Pregunta: «¿por qué el museo abierto es una demanda y no un deseo?». Si no responde, repasa las tres definiciones."),
    reinforce="Anota tres frases que podría decir un turista y clasifica cada una como necesidad, deseo o demanda.",
    extend="Explica con un ejemplo inventado cómo una paráfrasis puede evitar entregar información equivocada.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (de ejemplo, inventada). La señora Olga (68 años) y sus nietos Rosa y Tomás piden en el módulo: «Un paseo tranquilo de medio día (hasta 4 horas), cerca, que no cueste más de $50.000 en total y en que Tomás se divierta». "
     "Opciones del módulo: P1, Museo del Mar: 2 horas, $6.000 por persona adulta (Olga y Rosa) y $3.000 por niño (Tomás), con una sala interactiva pensada para niños. "
     "P2, paseo en lancha: 3 horas, $12.000 por persona. P3, caminata costera: 3 horas, sin costo, con terreno irregular y algunas subidas.")
build(
    O2, 3, F,
    use="Aprenderé a analizar el pedido de una familia, separar sus criterios y restricciones, comparar opciones con datos y recomendar sin suponer por la edad ni por otras características de las personas.",
    prior=["Sé distinguir necesidad, deseo y demanda.", "Sé sumar y restar con números enteros.", "Sé hacer preguntas y parafrasear."],
    explain=[
        "Para analizar un caso, primero se separan los criterios de selección, que son las condiciones que una opción debe cumplir para servir al cliente (por ejemplo, tranquilo y que los niños se diviertan), y las restricciones, que son límites que condicionan la elección, como el presupuesto, que es lo máximo que está dispuesto a gastar, o el tiempo disponible. Luego se compara cada opción con cada criterio y restricción, usando los datos de la ficha y no impresiones.",
        "Si falta un dato, se pregunta; si algo depende de la persona, como cuánto le acomoda caminar por un terreno irregular, se le pregunta a ella y no se supone por su edad. Se recomienda la opción que cumple más criterios y respeta todas las restricciones, y se ofrece una alternativa por si no le convence. Las actividades con riesgo se informan solo con datos del prestador y siempre con guía o instructor autorizado.",
        "El cierre de la atención resume lo acordado, entrega la información por escrito y pregunta si quedan dudas. Si la familia decide no tomar ningún paseo, se agradece y se respeta la decisión.",
    ],
    vocab=[("presupuesto", "dinero máximo que el cliente está dispuesto a gastar"), ("criterio de selección", "condición que debe cumplir una opción para servir al cliente"), ("restricción", "límite que condiciona la elección, como el dinero o el tiempo"), ("alternativa", "otra opción por si la primera no sirve"), ("recomendación", "opción que se sugiere según los criterios del cliente")],
    worked=[
        ("Filtrar por presupuesto", "Un cliente de ejemplo tiene un presupuesto de $30.000 para 2 personas. Opción X: $9.000 por persona. Opción Y: $16.000 por persona. ¿Cuál cumple?", ["X: 2 × 9.000 = 18.000, menor que 30.000.", "Y: 2 × 16.000 = 32.000, mayor que 30.000."], "Solo la opción X"),
        ("No suponer", "Un turista de ejemplo de 70 años pide un paseo; hay una caminata con subidas. ¿Se la descartas por su edad?", ["La edad no dice cuánto puede o quiere caminar.", "Se le describe el terreno y se le pregunta si le acomoda."], "No: se le pregunta a él"),
    ],
    mistakes=[("Descartar una opción pensando «a su edad no podrá».", "Es un estereotipo: la persona es quien sabe qué le acomoda.", "Describe la opción con datos y pregunta."),
              ("Recomendar la opción más cara por «dar buen servicio».", "Una opción que se pasa del presupuesto no cumple la restricción del cliente.", "Revisa el presupuesto antes de recomendar.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es el presupuesto de un cliente?", "El dinero máximo que está dispuesto a gastar", "El dinero mínimo que cobra el prestador", "El valor de la entrada más barata", "El presupuesto es un máximo fijado por el cliente, no un valor del prestador."),
        ("abc", "En Servicios de Turismo: ¿qué es un criterio de selección?", "Una condición que debe cumplir una opción para servirle al cliente", "El orden alfabético en que se presentan las opciones", "El nombre de la empresa que ofrece el paseo", "El criterio es lo que el cliente quiere que cumpla la opción; el orden y el nombre no lo son."),
        ("abc", "En Servicios de Turismo: ¿qué es una restricción?", "Un límite que condiciona la elección, como el presupuesto o el tiempo", "Una opinión personal de quien atiende", "Una promoción que reduce el precio", "La restricción limita las opciones posibles; una opinión o promoción no."),
        ("=", "{F} ¿Cuántos pesos cuesta el Museo del Mar para los tres?", "6000+6000+3000", "Se suman dos entradas de adulto y una de niño.", ""),
        ("=", "{F} ¿Cuántos pesos cuesta el paseo en lancha para los tres?", "3*12000", "Se multiplica el valor por persona por tres personas.", ""),
        ("abc", "{F} ¿Qué combinación de dos opciones se pasa del presupuesto de $50.000?", "Museo del Mar más paseo en lancha", "Museo del Mar más caminata costera", "Paseo en lancha más caminata costera", "Museo más lancha cuesta 15.000 más 36.000, que supera 50.000; las otras no."),
        ("=", "{F} ¿Cuántos pesos se pasa del presupuesto hacer juntos el Museo del Mar y el paseo en lancha?", "6000+6000+3000+3*12000-50000", "Se suman los dos costos y se resta el presupuesto.", ""),
        ("abc", "{F} La caminata costera tiene terreno irregular con subidas. ¿Qué haces antes de recomendársela a la señora Olga?", "Preguntarle a ella si le acomoda ese terreno, sin suponerlo por su edad", "No ofrecérsela porque tiene 68 años", "Ofrecérsela sin mencionar el terreno", "La decisión es de la persona, que debe conocer el terreno para elegir."),
        ("abc", "{F} ¿Qué opción de la ficha dice tener una actividad pensada para niños?", "El Museo del Mar, con su sala interactiva", "El paseo en lancha", "La caminata costera", "Solo el museo indica una sala interactiva para niños, lo que responde al pedido sobre Tomás."),
        ("abc", "{F} ¿Qué recomendación cumple mejor «medio día», «no más de $50.000» y «Tomás se divierta»?", "Museo del Mar: dura 2 horas, cuesta $15.000 y tiene sala para niños", "Paseo en lancha: dura 3 horas y cuesta $36.000, sin dato para niños", "Museo del Mar más paseo en lancha, para tener más opciones", "El museo cumple las tres condiciones con datos; museo más lancha suman 5 horas y superan el presupuesto."),
        ("ab", "La familia pide algo «cerca», pero la ficha no trae distancias. ¿Qué haces?", "Pedir la distancia al prestador o mirar un mapa antes de afirmar que está cerca", "Decir que todo está cerca en este pueblo", "No se afirma una distancia que no está confirmada; se verifica primero."),
        ("abc", "{F} Rosa dice: «A mí me gustaría algo de aventura». ¿Qué haces?", "Preguntarle qué entiende por aventura y ofrecer solo actividades de prestadores autorizados", "Recomendarle cualquier actividad de riesgo que conozcas", "Decirle que la aventura no es para su edad", "Se aclara el interés y se informa solo con prestadores autorizados, que son quienes pueden guiar actividades con riesgo."),
        ("abc", "{F} Para cerrar la atención de la familia, ¿qué corresponde?", "Resumir lo acordado, entregar la información por escrito y preguntar si queda alguna duda", "Despedirse rápido porque la familia ya eligió", "Entregar el folleto sin repetir lo conversado", "El cierre confirma la comprensión y deja constancia escrita de lo acordado."),
    ],
    ctx=("abc", "{F} Tras escuchar las opciones, la señora Olga dice que mejor no hará ningún paseo hoy. ¿Qué corresponde?", "Agradecer, respetar su decisión y dejarle el folleto por si cambia de idea", "Insistir en que el Museo del Mar es la mejor opción", "Ofrecerle un descuento inventado para convencerla", "La decisión del cliente se respeta; presionar o inventar descuentos no corresponde."),
    sc=[
        ("En Servicios de Turismo: ¿qué es una restricción del cliente?", "Un límite como el presupuesto o el tiempo disponible", "Toda opción debe respetar las restricciones."),
        ("¿Qué haces si una opción puede no acomodar a una persona?", "Le describo la opción y le pregunto a ella", "La edad no determina lo que una persona puede o quiere hacer."),
        ("¿Cómo cierras una atención?", "Resumo lo acordado y pregunto si quedan dudas", "El cierre confirma la comprensión del turista."),
    ],
    op=("Un grupo de ejemplo de 4 personas (2 adultos y 2 jóvenes) pide: «un paseo de hasta 3 horas, no más de $60.000 en total y que no sea muy físico». Opciones de ejemplo: Q1, visita a una feria artesanal, 2 horas, $5.000 por persona; Q2, paseo en bote, 2 horas y media, $18.000 por persona; Q3, caminata larga, 3 horas, gratis, con subidas. Calcula el costo de Q1 y Q2, descarta con razón una opción y escribe tu recomendación en tres líneas, con una pregunta para el grupo.",
        "Q1: 4 × 5.000 = 20.000. Q2: 4 × 18.000 = 72.000, supera el presupuesto de 60.000: se descarta. Q3 se pregunta al grupo: tiene subidas y pidieron algo poco físico. Recomendación: «Les sugiero la feria artesanal: dura 2 horas, cuesta 20.000 en total y es tranquila. El paseo en bote supera su presupuesto. ¿Prefieren ir por la mañana o por la tarde?».",
        ["calcula bien los costos de las opciones", "descarta con una razón basada en el presupuesto", "recomienda y formula una pregunta cerrada"],
        ["hoja con cálculos, descarte y recomendación"],
        ["no revisar el presupuesto de Q2", "recomendar sin explicar", "suponer que los adultos no pueden hacer la caminata"],
        "Pregunta: «¿qué restricción te hizo descartar Q2?». Si no responde, pídele que compare 72.000 con 60.000."),
    reinforce="Elige un paseo imaginario para tu familia y anota tres criterios y dos restricciones.",
    extend="Explica con un ejemplo inventado por qué preguntar es mejor que suponer lo que una persona puede hacer.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (de ejemplo, inventada). Un turista llega al módulo a las 15:30 y pregunta si alcanza a visitar hoy el Mirador Las Gaviotas. Datos del prestador: el mirador cierra a las 18:00. "
     "Traslado en bus desde el módulo al inicio del sendero: 20 minutos. Caminata de ida: 40 minutos. Tiempo recomendado de estadía en el mirador: 60 minutos. La caminata de vuelta también dura 40 minutos y el traslado de regreso, 20 minutos. "
     "Las caminatas se hacen con las indicaciones del prestador y con guía autorizado cuando corresponda.")
build(
    O2, 4, F,
    use="Aprenderé a orientar con datos claros: responder primero, calcular tiempos con horas y minutos, dar un margen y ofrecer una alternativa cuando no alcanza, con una frase simple en inglés.",
    prior=["Sé que 1 hora son 60 minutos.", "Sé restar y sumar con números enteros.", "Sé parafrasear lo que pide el turista."],
    explain=[
        "Orientar con datos claros es responder primero lo que el turista preguntó («sí alcanza» o «hoy no alcanza») y después entregar los datos que lo respaldan: horarios, duraciones, costos y condiciones. Los datos salen de fuentes confirmadas, como el prestador, y no se inventan. Conviene dar el margen de tiempo, que es el tiempo que sobra después de cumplir todo lo necesario, para que la persona sepa si tiene holgura o no.",
        "Para calcular tiempos se pasan las horas a minutos: 1 hora son 60 minutos, por eso las 15:30 son 15 × 60 + 30 = 930 minutos desde la medianoche. El tiempo disponible es la hora de cierre menos la hora actual, y el tiempo necesario es la suma de los tiempos de traslado, caminata y estadía. Si lo necesario es menor que lo disponible, alcanza y sobra un margen; si no, se ofrece una alternativa, como volver otro día.",
        "Al terminar, el turista repite con sus palabras la hora de salida y la de cierre; así se comprueba que entendió. Una frase simple en inglés para informar un cierre es «The viewpoint closes at six».",
    ],
    vocab=[("margen de tiempo", "tiempo que sobra después de cumplir todo lo necesario"), ("tiempo disponible", "tiempo que queda hasta el cierre"), ("tiempo necesario", "suma de los tiempos de traslado, caminata y estadía"), ("fuente confirmada", "dato que viene del prestador o de un documento oficial"), ("alternativa", "otra opción cuando la primera no alcanza")],
    worked=[
        ("Tiempo disponible", "Un museo de ejemplo cierra a las 17:00. Una persona llega a las 15:20. ¿Cuántos minutos tiene?", ["Las 17:00 son 17 × 60 = 1.020 minutos.", "Las 15:20 son 15 × 60 + 20 = 920 minutos; 1.020 − 920 = 100 minutos."], "100 minutos"),
        ("Margen", "Una visita guiada de ejemplo dura 75 minutos y la persona tiene 100 minutos. ¿Cuánto sobra?", ["Se resta lo necesario al tiempo disponible.", "100 − 75 = 25 minutos."], "25 minutos de margen"),
    ],
    mistakes=[("Contestar «sí, alcanza» solo mirando cuánto dura la caminata de ida.", "Faltan el traslado y la estadía recomendada: el tiempo necesario es mayor.", "Suma todos los tiempos antes de responder."),
              ("Decir una hora de cierre de memoria.", "Un dato antiguo puede estar mal y el turista pierde su tiempo.", "Confirma la hora con la fuente del prestador.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué conviene decir primero al orientar a un turista?", "La respuesta a su pregunta, y luego los datos que la respaldan", "Toda la historia del lugar, y la respuesta al final", "Una pregunta sobre su vida personal", "Responder primero respeta el tiempo del turista; los datos después explican la respuesta."),
        ("abc", "En Servicios de Turismo: ¿qué es un margen de tiempo?", "El tiempo que sobra después de cumplir todo lo necesario", "El horario en que abre el atractivo", "El tiempo que dura el viaje de regreso", "El margen es lo que sobra; no es un horario ni un tramo del viaje."),
        ("abc", "En Servicios de Turismo: ¿qué es una fuente confirmada?", "Un dato que viene del prestador o de un documento oficial", "Un dato que alguien recuerda de memoria", "Un dato que aparece en una conversación de pasillo", "Una fuente confirmada permite verificar el dato; recordar o escuchar no lo hace."),
        ("=", "{F} ¿Cuántos minutos hay entre las 15:30 y el cierre del mirador a las 18:00?", "18*60-(15*60+30)", "Se pasan ambas horas a minutos y se restan.", " minutos"),
        ("=", "{F} ¿Cuántos minutos necesita el turista para llegar al mirador y quedarse el tiempo recomendado?", "20+40+60", "Se suman el traslado, la caminata de ida y la estadía.", " minutos"),
        ("=", "{F} ¿Cuántos minutos de margen tiene el turista antes del cierre?", "18*60-(15*60+30)-(20+40+60)", "Se resta el tiempo necesario al tiempo disponible.", " minutos"),
        ("abc", "{F} ¿Qué respuesta corresponde para el turista de las 15:30?", "Sí alcanza, con 30 minutos de margen, si sale ahora y sigue las indicaciones del prestador", "No alcanza, porque la caminata es de 40 minutos", "Sí alcanza y puede quedarse todo el tiempo que quiera", "Con 30 minutos de margen alcanza, pero no sobra tiempo para quedarse sin límite."),
        ("=", "Otro turista llega al módulo a las 16:45 y hace la misma pregunta, con los tiempos de la ficha. ¿Cuántos minutos faltan para el cierre a las 18:00?", "18*60-(16*60+45)", "Se pasan las horas a minutos y se restan.", " minutos"),
        ("=", "{F} Para ese turista de las 16:45, ¿cuántos minutos le faltan para completar la visita?", "(20+40+60)-(18*60-(16*60+45))", "Se resta el tiempo disponible al tiempo necesario.", " minutos"),
        ("abc", "{F} ¿Qué le dices al turista de las 16:45?", "Que hoy no alcanza la visita completa y ofrecerle una alternativa, como ir mañana temprano", "Que se apure y acorte la visita sin avisar al prestador", "Que sí alcanza, por si acaso", "No alcanza el tiempo necesario; se informa con claridad y se ofrece otra opción."),
        ("ab", "¿Cómo se dice en inglés simple «El mirador cierra a las seis»?", "The viewpoint closes at six.", "The viewpoint opens at six.", "«Closes» significa cierra; «opens» significa abre y cambiaría el sentido."),
        ("abc", "{F} Para comprobar que el turista de las 15:30 entendió, ¿qué haces al final?", "Pedirle que repita con sus palabras la hora de salida y la de cierre", "Preguntar solo «¿entendió?» y asumir que sí", "Entregar el folleto sin decir nada más", "Repetir con sus palabras muestra si entendió; un «sí» automático no lo asegura."),
        ("=", "{F} ¿Cuántos minutos dura la visita completa desde el módulo hasta volver, contando traslados y caminatas de ida y vuelta y la estadía?", "20+40+60+40+20", "Se suman traslado y caminata de ida, estadía, y caminata y traslado de vuelta.", " minutos"),
    ],
    ctx=("abc", "{F} El turista de las 15:30 pregunta si debe llevar algo para la caminata. No tienes un dato confirmado sobre las condiciones del sendero. ¿Qué corresponde?", "Indicarle que consulte las condiciones y recomendaciones al prestador o al guía autorizado", "Asegurarle que no necesita nada", "Inventar una lista de equipo para parecer experto", "Las condiciones de un sendero las informa el prestador; afirmar sin saber puede poner en riesgo a la persona."),
    sc=[
        ("En Servicios de Turismo: ¿qué es el tiempo necesario?", "La suma de traslados, caminata y estadía", "Se compara con el tiempo disponible."),
        ("¿Qué haces si el tiempo necesario es mayor que el disponible?", "Informo que no alcanza y ofrezco una alternativa", "Mentir o apurar al turista le puede causar problemas."),
        ("¿Cómo pasas 16:45 a minutos?", "16 × 60 + 45 = 1.005 minutos", "Se multiplican las horas por 60 y se suman los minutos."),
    ],
    op=("Un turista de ejemplo llega al módulo a las 14:10 y pregunta si alcanza a hacer una visita guiada a un museo que cierra a las 17:00. Datos: traslado de 15 minutos hasta el museo, visita guiada de 90 minutos y almuerzo previo de 45 minutos en la cafetería del módulo. Calcula el tiempo disponible, el necesario y el margen, y escribe la respuesta en dos frases, con la respuesta primero.",
        "Disponible: 17:00 − 14:10 = 170 minutos. Necesario: 45 + 15 + 90 = 150 minutos. Margen: 20 minutos. Respuesta: «Sí alcanza, con 20 minutos de margen. Si almuerza primero 45 minutos y sale de inmediato, llega al museo y completa la visita antes del cierre».",
        ["calcula bien el tiempo disponible y el necesario", "obtiene y comunica el margen", "responde primero y luego da los datos"],
        ["hoja con cálculos y respuesta de dos frases"],
        ["olvidar el almuerzo en el tiempo necesario", "responder sin dar el margen", "dar los datos antes de la respuesta"],
        "Pregunta: «¿qué tiempos sumaste para el tiempo necesario?». Si no responde, repasa la definición."),
    reinforce="Elige un horario de cierre y calcula cuántos minutos faltan desde la hora en que estás leyendo esto.",
    extend="Explica con un ejemplo inventado por qué dar el margen de tiempo es útil para el turista.",
)

# ============================================================ OAE-02, clase 5
F = ("Ficha 5 (de ejemplo, inventada). Tres respuestas a un turista que pregunta cómo llegar a la feria artesanal. Respuesta X: «Está por ahí, no sé bien, pregunte en otro lado». "
     "Respuesta Y: «Buenas tardes. La feria queda a 10 cuadras; puede ir a pie, unos 15 minutos por vereda plana, o en micro. Abre de 10:00 a 19:00. ¿Le muestro el mapa?». "
     "Respuesta Z: «Buenas tardes. Tome el bus 5 y baje en la plaza, son 30 minutos. Abre a las 10:00». "
     "Lista de cotejo de calidad (1 punto por criterio): saludo; información completa (cómo llegar y horario de apertura y de cierre); alternativa; confirma o ofrece ayuda; trato respetuoso. "
     "Encuesta de satisfacción de ejemplo a 5 turistas, con puntajes de 1 a 5: 4, 5, 3, 4 y 4. Meta del módulo: promedio mínimo 4.")
build(
    O2, 5, F,
    use="Aprenderé a comparar distintas respuestas de atención con una lista de cotejo, a leer una encuesta de satisfacción y a mejorar la atención sin culpar a una persona.",
    prior=["Sé orientar con datos claros.", "Sé sumar y dividir con números enteros.", "Sé calcular un porcentaje exacto."],
    explain=[
        "La calidad de la atención se verifica con evidencia. Una lista de cotejo es una lista de criterios que se revisan uno a uno, con un punto por cada criterio cumplido; así se compara una respuesta con otra sin depender de la impresión. Una buena atención saluda, entrega información completa y verificada, ofrece una alternativa, confirma que el turista entendió y mantiene un trato respetuoso.",
        "La encuesta de satisfacción mide qué tan conforme quedó el turista. El promedio se obtiene sumando los puntajes y dividiendo por la cantidad de respuestas; el porcentaje de satisfechos es cuántos dieron 4 o 5, de cada 100. Los comentarios sirven para mejorar el servicio en equipo, y nunca se borra una encuesta para que el resultado se vea mejor.",
        "Un modelo de respuesta sirve de guía, pero cada respuesta se adapta a lo que pregunta y necesita cada turista. Los materiales que se entregan, como un mapa, deben estar actualizados y ser legibles.",
    ],
    vocab=[("lista de cotejo", "lista de criterios que se revisan uno a uno"), ("encuesta de satisfacción", "preguntas para saber qué tan conforme quedó el turista"), ("promedio", "suma de los puntajes dividida por la cantidad de respuestas"), ("meta", "resultado mínimo que el equipo quiere lograr"), ("oportunidad de mejora", "aspecto de la atención que se puede hacer mejor")],
    worked=[
        ("Puntaje de cotejo", "Una respuesta de ejemplo saluda, da información completa, ofrece alternativa y trata con respeto, pero no confirma la comprensión. ¿Cuántos puntos tiene?", ["Cumple 4 de los 5 criterios.", "Cada criterio vale 1 punto."], "4 puntos"),
        ("Promedio", "Tres turistas de ejemplo dan puntajes 3, 5 y 4. ¿Cuál es el promedio?", ["Se suman: 3 + 5 + 4 = 12.", "Se divide por 3: 12 ÷ 3 = 4."], "4"),
    ],
    mistakes=[("Borrar una encuesta con puntaje bajo para mejorar el promedio.", "Es alterar la evidencia y se pierde la oportunidad de mejorar.", "Conserva todas las encuestas y analiza los comentarios."),
              ("Copiar siempre la misma respuesta a todos los turistas.", "No responde a lo que cada persona necesita ni a su pregunta.", "Usa el modelo como guía y adáptalo.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es una lista de cotejo de calidad?", "Una lista de criterios que se revisan uno a uno para evaluar una atención", "Un listado de turistas que visitaron el módulo", "Una lista de precios de los paseos", "La lista de cotejo permite evaluar con criterios, no registra turistas ni precios."),
        ("abc", "¿Qué mide una encuesta de satisfacción?", "Qué tan conforme quedó el turista con la atención recibida", "Cuántos turistas llegaron en el día", "Cuánto cuesta atender a cada turista", "La encuesta recoge la opinión del turista sobre la atención."),
        ("abc", "¿Para qué sirve comparar alternativas de respuesta con una lista de cotejo?", "Para elegir la que mejor cumple los criterios y mejorar las demás", "Para elegir la más corta, aunque esté incompleta", "Para elegir la que más le guste a quien atiende", "Comparar con criterios hace objetiva la elección; la extensión o el gusto personal no lo hacen."),
        ("abc", "{F} ¿Cuál de las tres respuestas obtiene el mayor puntaje en la lista de cotejo?", "La respuesta Y", "La respuesta X", "La respuesta Z", "Y cumple los cinco criterios; Z cumple menos y X ninguno."),
        ("=", "{F} Y cumple los cinco criterios y Z solo cumple saludo y trato respetuoso. ¿Cuántos puntos más tiene Y que Z?", "5-2", "Se resta el puntaje de Z al de Y.", " puntos"),
        ("abc", "{F} ¿Qué dato de horario falta en la respuesta Z para tener información completa?", "El horario de cierre", "El horario de apertura", "El número del bus", "Z dice que abre a las 10:00 pero no cuándo cierra."),
        ("abc", "{F} ¿Por qué la respuesta X no sirve al turista?", "No da información verificable ni orienta, y lo deja sin saber cómo llegar", "Solo le falta el saludo; el resto de la información es completa", "Ofrece demasiadas alternativas y confunde", "X no entrega datos ni orienta ni saluda; no cumple ningún criterio."),
        ("=", "{F} ¿Cuántos puntos suman los puntajes de la encuesta?", "4+5+3+4+4", "Se suman los cinco puntajes de la encuesta.", " puntos"),
        ("=", "{F} ¿Cuál es el promedio de esa encuesta?", "(4+5+3+4+4)//5", "Se divide la suma de los puntajes por 5 respuestas.", ""),
        ("=", "{F} ¿Qué porcentaje de los 5 turistas dio 4 o 5 puntos?", "4*100//5", "Cuatro de cinco turistas dieron 4 o 5; se pasa a porcentaje.", " %"),
        ("abc", "{F} ¿Qué concluyes respecto de la meta del módulo?", "Cumple la meta, porque el promedio es 4", "No cumple la meta, porque hay un puntaje 3", "No se puede saber sin más encuestas", "La meta es promedio mínimo 4 y el promedio es 4; un puntaje bajo no la anula."),
        ("abc", "{F} Un turista puso 3 y escribió «me atendieron sin mirarme». ¿Qué corresponde?", "Tomarlo como oportunidad de mejora y revisarlo en equipo, sin culpar a una persona", "Borrar la encuesta para mejorar el promedio", "Descartarla porque es solo una opinión", "El comentario ayuda a mejorar el trato; borrar o descartar pierde la evidencia."),
        ("abc", "{F} Una compañera propone copiar la respuesta Y para todos los turistas. ¿Cuál es el límite?", "Sirve de modelo, pero cada respuesta se adapta a lo que pregunta y necesita cada turista", "No sirve para nada, porque es de otra persona", "Debe copiarse sin cambios, para ser uniforme", "Un modelo guía, pero la información debe responder a cada pregunta."),
    ],
    ctx=("abc", "Antes de entregar un mapa impreso al turista, ¿qué verificas?", "Que los horarios y direcciones estén actualizados y se lean bien", "Que tenga el logo de la oficina, aunque los horarios estén desactualizados", "Que sea el más grande del módulo", "Un mapa con datos antiguos o ilegibles confunde al turista, por eso se verifica."),
    sc=[
        ("En Servicios de Turismo: ¿cómo se obtiene un promedio?", "Se suman los puntajes y se divide por la cantidad de respuestas", "El promedio resume los puntajes en un solo valor."),
        ("¿Qué haces con una encuesta de puntaje bajo?", "La conservo y analizo su comentario para mejorar", "Borrarla altera la evidencia de la calidad."),
        ("¿Qué criterio evalúa si el turista entendió?", "Confirma o ofrece ayuda", "La confirmación comprueba la comprensión del turista."),
    ],
    op=("Una respuesta de ejemplo a un turista que pregunta por el horario de un museo dice: «Hola. Abre a las 9. Chao». Evalúa la respuesta con los cinco criterios de la lista de cotejo (1 punto cada uno), da su puntaje y reescríbela para que obtenga los cinco puntos, usando el horario de ejemplo 9:00 a 17:00 y un mapa.",
        "Saludo: sí (cumple de forma mínima). Información completa: no, falta el cierre. Alternativa: no. Confirma o ofrece ayuda: no. Trato respetuoso: dudoso por el «Chao» seco. Puntaje: 1 o 2 puntos. Reescritura: «Buenas tardes. El museo abre de 9:00 a 17:00. Si llega tarde, puede venir mañana temprano. ¿Le muestro el mapa para llegar?».",
        ["aplica los cinco criterios con claridad", "calcula un puntaje coherente con lo evaluado", "la reescritura cumple los criterios"],
        ["tabla con criterios y puntaje, y la nueva respuesta"],
        ["dar puntaje sin explicar por criterio", "reescribir sin incluir el horario de cierre", "olvidar la alternativa"],
        "Pregunta: «¿qué criterio cumple tu nueva respuesta que la original no cumplía?». Si no responde, repasa la lista de cotejo."),
    reinforce="Evalúa con la lista de cotejo una atención que hayas recibido en una tienda.",
    extend="Explica con un ejemplo inventado por qué una encuesta con comentarios sirve más que una con solo puntajes.",
)

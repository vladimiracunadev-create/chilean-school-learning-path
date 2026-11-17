"""Servicios de Turismo TP 3.º y 4.º medio: OAE-03 (orientar e informar sobre atractivos turísticos de la zona). Todo en papel; atractivos y datos de ejemplo."""
from __future__ import annotations

from tp_setu_common import build

O3 = "TP-SETU-3y4-OAE-03"

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (de ejemplo, inventada). Atractivo «Humedal Las Totoras», del pueblo ficticio de Villa Brisa. Tipo: natural. Horario: 9:00 a 17:00. Capacidad: 30 visitantes a la vez. "
     "Reglas del administrador: mantenerse en el sendero, no alimentar ni tocar animales, no sacar plantas ni huevos y llevarse la basura. Un panel cuenta la historia del lugar según la comunidad local de ejemplo. "
     "Hoy hay un aviso de cierre del sendero norte por lluvias.")
build(
    O3, 1, F,
    use="Aprenderé qué es un atractivo turístico y un patrimonio, qué normas y reglas lo protegen, y qué riesgos hay al informar mal: datos falsos, daño al ambiente o al patrimonio.",
    prior=["Sé que se informa solo lo confirmado.", "Sé restar y sumar con números enteros.", "Sé que hay lugares que se deben cuidar."],
    explain=[
        "Un atractivo turístico es un lugar, evento o elemento que motiva a las personas a viajar para conocerlo. Puede ser natural, como un humedal, o cultural, como un museo o una fiesta tradicional. El patrimonio son los bienes naturales y culturales que se cuidan para que las próximas generaciones también puedan conocerlos. Por eso orientar a un turista incluye informar cómo cuidar el lugar.",
        "Cada atractivo tiene reglas del administrador y, según corresponda, normas vigentes de protección del ambiente y del patrimonio. En general: mantenerse en los senderos, no extraer plantas ni piezas, no molestar a los animales y no dejar residuos. Los requerimientos sanitarios son las medidas de higiene y los avisos de la autoridad sanitaria. La información de contingencia es la del día, que puede cambiar la visita, como un cierre por lluvias.",
        "Si un atractivo está ligado a un pueblo originario o a una comunidad local, la información sobre su cultura la entrega la propia comunidad o quien la represente: no se inventan significados ni historias. Informar mal tiene riesgos: el turista pierde tiempo, daña el lugar o se expone a peligros. Este cuaderno es aprendizaje en papel y no te habilita para guiar en terreno.",
    ],
    vocab=[("atractivo turístico", "lugar, evento o elemento que motiva a viajar para conocerlo"), ("patrimonio", "bienes naturales y culturales que se cuidan para las próximas generaciones"), ("administrador", "persona o institución que cuida y gestiona el atractivo"), ("información de contingencia", "información del día que puede cambiar la visita"), ("residuos", "basura que se genera al visitar un lugar"), ("requerimiento sanitario", "medida de higiene o aviso de la autoridad sanitaria")],
    worked=[
        ("Horas de apertura", "Un museo de ejemplo abre de 10:00 a 18:00. ¿Cuántas horas está abierto?", ["Se resta la hora de apertura a la de cierre.", "18 − 10 = 8 horas."], "8 horas"),
        ("Capacidad", "Un mirador de ejemplo admite 25 personas a la vez. Llegan dos grupos, de 14 y 13 personas. ¿Pueden entrar juntos?", ["14 + 13 = 27 personas.", "27 es mayor que 25: no caben juntos."], "No: sobran 2 personas"),
    ],
    mistakes=[("Decir «llévate una planta de recuerdo, nadie se da cuenta».", "Extraer plantas daña el ambiente y rompe las reglas del administrador.", "Explica la regla y sugiere llevarse una foto."),
              ("Contar una historia del lugar sin saber si es cierta.", "Si no es verdad, se engaña al turista y se falta el respeto a la comunidad.", "Informa solo lo que esté confirmado por el administrador o la comunidad.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es un atractivo turístico?", "Un lugar, evento o elemento que motiva a las personas a viajar para conocerlo", "Un servicio de transporte entre dos ciudades", "Un documento que prueba que se pagó una reserva", "El atractivo es lo que motiva el viaje; el transporte y el comprobante son otros elementos."),
        ("abc", "En Servicios de Turismo: ¿qué es el patrimonio?", "Bienes naturales y culturales que se cuidan para las próximas generaciones", "El dinero que ganan los guías en un año", "La lista de precios de un museo", "El patrimonio se cuida para que otros también lo conozcan; no es dinero ni precios."),
        ("abc", "En Servicios de Turismo: ¿qué es la información de contingencia?", "Información del día que puede cambiar la visita, como un cierre por lluvia", "La historia del lugar desde su origen", "El nombre del administrador", "Contingencia se refiere a lo que ocurre hoy y afecta la visita."),
        ("abc", "{F} ¿Qué tipo de atractivo es el Humedal Las Totoras?", "Natural", "Cultural, porque tiene un panel", "Un servicio de alimentación", "La ficha indica tipo natural; el panel solo agrega información de la comunidad."),
        ("=", "{F} ¿Cuántas horas al día está abierto el humedal?", "17-9", "Se resta la hora de apertura a la hora de cierre.", " horas"),
        ("abc", "{F} Un turista pide sacar una planta «de recuerdo». ¿Qué respondes?", "Que no se puede, porque las reglas del administrador protegen las plantas y el ambiente", "Que sí, pero solo una pequeña", "Que sí, si nadie lo ve", "Está prohibido sacar plantas; permitir una sola vez igualmente daña el lugar."),
        ("=", "{F} Llegan 3 grupos de 12, 9 y 14 personas a la vez. ¿Cuántas personas sobran respecto de la capacidad?", "12+9+14-30", "Se suman los tres grupos y se resta la capacidad de 30.", " personas"),
        ("abc", "{F} ¿Qué información de contingencia debes dar hoy?", "Que el sendero norte está cerrado por lluvias", "Que el humedal es de tipo natural", "Que abre a las 9:00", "Solo el cierre del sendero es un aviso del día; el tipo y el horario son datos permanentes."),
        ("abc", "{F} Un turista pregunta por el significado de un símbolo del panel de la comunidad y no lo sabes. ¿Qué corresponde?", "Decir que no lo sabes y derivarlo a la comunidad o al administrador, sin inventar", "Inventar un significado que suene creíble", "Decir que no tiene significado", "El significado cultural lo da la comunidad; inventarlo es faltarle el respeto."),
        ("abc", "Un turista pregunta si el agua de una vertiente del lugar es segura para beber. ¿Qué corresponde?", "Decir que no tienes el dato y remitirlo a las indicaciones de la autoridad sanitaria y del administrador", "Decir que sí, porque se ve limpia", "Decir que sí, porque otros turistas la beben", "La calidad del agua no se juzga a simple vista; solo la autoridad sanitaria puede confirmarla."),
        ("=", "{F} Si cada visita guiada dura 90 minutos y se hacen una tras otra durante el horario completo, ¿cuántas visitas completas caben en el día?", "(17-9)*60//90", "Se pasan las horas abiertas a minutos y se divide por 90.", " visitas"),
        ("abc", "{F} Un turista quiere pisar las plantas del borde del humedal para sacar una foto «solo un momento». ¿Qué respondes?", "Que debe mantenerse en el sendero y tomar la foto desde allí", "Que puede salirse un momento si es rápido", "Que puede hacerlo si deja una propina", "La regla de mantenerse en el sendero protege las plantas y los nidos."),
        ("abc", "Un compañero quiere decir a los turistas que en el humedal vive un animal famoso, pero nadie lo ha confirmado. ¿Qué corresponde?", "No afirmarlo y entregar solo lo confirmado por el administrador", "Decirlo, porque atrae turistas", "Decirlo, pero en voz baja", "Una información sin confirmar engaña al turista y puede ser falsa."),
    ],
    ctx=("abc", "{F} Ves a un turista alimentando a las aves con pan. ¿Qué haces?", "Explicarle amablemente la regla y por qué protege a los animales", "Ignorarlo, porque es solo un poco de pan", "Gritarle delante de todos", "Una explicación amable corrige la conducta sin ofender y cuida a los animales."),
    sc=[
        ("En Servicios de Turismo: ¿qué es el patrimonio?", "Bienes naturales y culturales que se cuidan para las próximas generaciones", "Por eso se informa cómo cuidarlos."),
        ("¿Quién informa sobre la cultura de una comunidad?", "La propia comunidad o quien la represente", "Inventar significados falta el respeto a la comunidad."),
        ("¿Qué haces si no tienes un dato confirmado?", "Digo que no lo sé y consulto al administrador", "Informar sin confirmar puede perjudicar al turista."),
    ],
    op=("Escribe un aviso de cuatro líneas para la entrada del «Humedal Las Totoras» de la ficha: horario, dos reglas de cuidado, un aviso del día y una frase amable de bienvenida. Usa solo los datos de la ficha.",
        "«Bienvenidos al Humedal Las Totoras. Horario: 9:00 a 17:00. Por favor, manténgase en el sendero y no alimente a los animales. Aviso de hoy: el sendero norte está cerrado por lluvias. Gracias por cuidar este lugar».",
        ["usa solo datos de la ficha", "incluye horario, dos reglas y un aviso del día", "tiene un tono amable"],
        ["aviso escrito con las cuatro partes"],
        ["inventar un dato que no está en la ficha", "olvidar el aviso del día", "usar un tono de orden sin explicación"],
        "Pregunta: «¿de dónde sacaste cada dato?». Si no puede responder, pídele que señale la línea de la ficha."),
    reinforce="Elige un lugar que conozcas y anota dos reglas que ayudan a cuidarlo.",
    extend="Explica con un ejemplo inventado qué le puede pasar a un turista que recibe información sin confirmar.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (de ejemplo, inventada). Datos reunidos sobre el «Museo Comunitario de Villa Brisa»: (a) «El museo se instaló en una antigua bodega de la estación del pueblo»; "
     "(b) «Cada año se hace una feria de oficios tradicionales»; (c) «Queda a 800 metros de la plaza, hacia el sur»; (d) «Muchas familias del pueblo viven de la venta de artesanía»; "
     "(e) «Hoy el museo cierra a las 14:00 por una reunión»; (f) «En el jardín anidan aves entre los arbustos»; (g) «El pueblo tiene una posta de salud y una escuela». "
     "Roles: administrador del museo, guía autorizado, informante turístico y comunidad local.")
build(
    O3, 2, F,
    use="Aprenderé los siete tipos de información que se entregan sobre un atractivo (histórica, cultural, geográfica, económica, de contingencia, social, de flora y fauna), los documentos de apoyo y los roles.",
    prior=["Sé qué es un atractivo y un patrimonio.", "Sé que se informa solo lo confirmado.", "Sé dividir con números enteros."],
    explain=[
        "Sobre un atractivo se puede informar de siete tipos. La información histórica cuenta el pasado del lugar. La cultural habla de costumbres, oficios, arte y tradiciones. La geográfica indica dónde está y cómo se llega. La económica explica de qué vive la gente del lugar. La social describe cómo se organizan las personas y qué servicios tienen. La de flora y fauna presenta las plantas y los animales. Y la de contingencia entrega lo que ocurre hoy y afecta la visita.",
        "Los documentos de apoyo son la ficha del atractivo, con sus datos confirmados; el panel informativo del lugar; el folleto; el mapa; y el guion de información, que es un texto breve preparado para entregar los datos en orden. Los roles son: el administrador, que cuida y gestiona el lugar; el guía autorizado, que según la norma vigente conduce visitas; el informante turístico, que orienta con datos verificados; y la comunidad local, que entrega la información sobre su propia cultura.",
        "Dos frases en inglés útiles para informar son «The museum closes at two today» (El museo cierra hoy a las dos) y «Please do not touch the objects» (Por favor, no toque los objetos).",
    ],
    vocab=[("información histórica", "datos sobre el pasado del lugar"), ("información cultural", "datos sobre costumbres, oficios, arte y tradiciones"), ("información geográfica", "datos sobre dónde está y cómo se llega"), ("información económica", "datos sobre de qué vive la gente del lugar"), ("información social", "datos sobre cómo se organizan las personas y sus servicios"), ("guion de información", "texto breve y ordenado para entregar los datos"), ("guía autorizado", "persona habilitada, según la norma vigente, para conducir visitas")],
    worked=[
        ("Clasificar un dato", "Un dato de ejemplo dice: «El faro está a 5 kilómetros al norte del puerto». ¿Qué tipo de información es?", ["Habla de la ubicación del lugar.", "Es información geográfica."], "Geográfica"),
        ("Elegir el rol", "Un turista de ejemplo pide que alguien conduzca un recorrido de un día por el sendero. ¿Quién debe hacerlo?", ["Conducir visitas corresponde a un guía autorizado.", "El informante turístico orienta, pero no conduce el recorrido."], "Un guía autorizado"),
    ],
    mistakes=[("Mezclar un relato de la comunidad con un dato histórico comprobado.", "El turista cree que es un hecho confirmado cuando solo es un relato.", "Di «cuenta la comunidad que…» cuando sea un relato."),
              ("Dar solo información de un tipo, como la histórica, a todos los turistas.", "Cada persona tiene intereses distintos, como fauna, cultura o servicios.", "Pregunta qué le interesa y elige el tipo de información.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es la información histórica sobre un atractivo?", "Datos sobre el pasado del lugar, como cuándo y cómo se originó", "Datos sobre el clima de hoy", "Datos sobre el precio de la entrada", "La información histórica se refiere al pasado; el clima y el precio son otros tipos de información."),
        ("abc", "En Servicios de Turismo: ¿qué es la información económica sobre un atractivo o su comunidad?", "Datos sobre de qué vive la gente del lugar y cómo se genera ingreso", "Datos sobre cómo se llega al lugar", "Datos sobre las aves que viven allí", "La información económica explica los ingresos y trabajos; las otras opciones son geográfica y de fauna."),
        ("abc", "En Servicios de Turismo: ¿qué es un guía autorizado?", "Una persona habilitada, según la norma vigente, para conducir visitas", "Cualquier persona que conozca bien el lugar", "El turista más experimentado del grupo", "Conducir visitas requiere estar habilitado según la norma; conocer el lugar no basta."),
        ("abc", "{F} El dato (a), sobre la antigua bodega de la estación, ¿qué tipo de información es?", "Histórica", "Económica", "De contingencia", "Habla del origen del edificio, es decir, de su pasado."),
        ("abc", "{F} El dato (c), «queda a 800 metros de la plaza», ¿qué tipo de información es?", "Geográfica", "Social", "Cultural", "Indica la ubicación y la distancia, por lo tanto es información geográfica."),
        ("abc", "{F} El dato (d), sobre las familias que viven de la artesanía, ¿qué tipo de información es?", "Económica", "Histórica", "De flora y fauna", "Explica de qué vive la gente del pueblo, que es información económica."),
        ("abc", "{F} El dato (e), sobre el cierre a las 14:00 por una reunión, ¿qué tipo de información es?", "De contingencia", "Geográfica", "Cultural", "Es un aviso del día que cambia la visita: es contingencia."),
        ("abc", "{F} El dato (g), sobre la posta de salud y la escuela, ¿qué tipo de información es?", "Social", "Económica", "De flora y fauna", "Describe servicios de la comunidad, por lo que es información social."),
        ("abc", "{F} El dato (f), sobre las aves que anidan en el jardín, ¿qué tipo de información es?", "De flora y fauna", "Histórica", "Social", "Habla de animales y plantas del lugar."),
        ("=", "{F} Una persona camina 80 metros por minuto (dato de ejemplo). ¿Cuántos minutos tarda en recorrer los 800 metros desde la plaza hasta el museo?", "800//80", "Se divide la distancia por los metros que camina por minuto.", " minutos"),
        ("ab", "{F} ¿Cuál es la traducción de «The museum closes at two today»?", "El museo cierra hoy a las dos.", "El museo abre hoy a las dos.", "Closes significa cierra, por lo que la frase informa un cierre."),
        ("abc", "¿Quién debe entregar la información sobre las tradiciones de una comunidad local?", "La propia comunidad o quien la represente", "Quien atiende el módulo, según lo que recuerde", "Cualquier turista que haya visitado antes", "La comunidad es la fuente de su propia cultura; los otros pueden equivocarse."),
        ("abc", "{F} Un turista llega a las 13:30 y quiere conocer el museo hoy. ¿Qué dato le entregas primero?", "Que hoy el museo cierra a las 14:00 por una reunión", "Que cada año se hace una feria de oficios", "Que el museo está en una antigua bodega", "El aviso del día es lo que más afecta su visita y debe darse primero."),
    ],
    ctx=("abc", "{F} Una turista dice que le interesa conocer cómo vive la gente del pueblo. ¿Qué tipo de información priorizas?", "Información social y económica", "Información sobre las aves del jardín", "Información sobre el horario de cierre de hoy", "Cómo se organiza la gente y de qué vive se explica con información social y económica."),
    sc=[
        ("En Servicios de Turismo: ¿qué entrega la información geográfica?", "Dónde está el lugar y cómo se llega", "La ubicación y la distancia son datos geográficos."),
        ("¿Quién conduce una visita según la norma vigente?", "Un guía autorizado", "El informante turístico orienta, pero no conduce recorridos."),
        ("¿Qué frase usas para un relato de la comunidad?", "«Cuenta la comunidad que…»", "Así no se presenta como hecho comprobado."),
    ],
    op=("Con los datos (a) a (g) de la ficha, prepara un guion de información de cinco líneas para una turista a la que le interesan la historia y los oficios, e indica con una letra entre paréntesis de qué dato salió cada línea.",
        "«Bienvenida al museo; hoy cierra a las 14:00 por una reunión (e). Funciona en una antigua bodega de la estación (a). Cada año hay una feria de oficios tradicionales (b). Muchas familias viven de la artesanía (d). Queda a 800 metros de la plaza, hacia el sur (c)».",
        ["usa solo datos de la ficha", "elige datos que responden al interés de la turista", "cada línea indica su dato de origen"],
        ["guion de cinco líneas con las letras de origen"],
        ["incluir datos que no están en la ficha", "dar el aviso de cierre al final", "no relacionar con el interés de la turista"],
        "Pregunta: «¿por qué pusiste el aviso de cierre primero?». Si no responde, repasa la regla de contingencia."),
    reinforce="Elige un lugar que conozcas y escribe un dato de cada tipo de información.",
    extend="Explica con un ejemplo inventado por qué el informante turístico no debe conducir visitas sin ser guía autorizado.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (de ejemplo, inventada). Dos turistas piden información sobre el «Humedal Las Totoras». Turista 1: una familia con dos niños que tiene 1 hora y quiere ver fauna. Turista 2: una viajera extranjera con inglés básico que tiene 2 horas y le interesa la historia local. "
     "Datos disponibles: D1, «la comunidad lo cuida como sitio protegido desde hace 20 años» (fuente: panel del administrador); D2, «en primavera llegan aves migratorias» (fuente: guía del administrador); "
     "D3, «el sendero circular mide 2.000 metros» (fuente: mapa del administrador); D4, «dos cooperativas locales ofrecen alojamiento» (fuente: oficina municipal de ejemplo); "
     "D5, «se cuenta que un antiguo pescador dejaba una luz encendida para guiar a los viajeros» (relato de la comunidad, sin comprobar); D6, «dicen que en la laguna vive un animal gigante» (sin fuente).")
build(
    O3, 3, F,
    use="Aprenderé a analizar un caso: seleccionar los datos relevantes según el interés y el tiempo del turista, distinguir hecho, relato y rumor, y cuidar al turista y al lugar.",
    prior=["Sé distinguir los siete tipos de información.", "Sé dividir y restar con números enteros.", "Sé que se informa solo lo confirmado."],
    explain=[
        "Para analizar un caso se leen el interés, el tiempo y las características del turista, y se eligen datos relevantes: los que responden a su interés, caben en su tiempo y tienen una fuente confirmada. Una fuente es el documento o la persona de donde viene el dato, como el panel del administrador. Un dato sin fuente no se entrega como información.",
        "Hay tres clases de contenido. El hecho es lo comprobado y con fuente. El relato es una tradición que cuenta la comunidad; se comparte con respeto como relato («cuenta la comunidad que…»), nunca como hecho comprobado. El rumor es lo que se dice sin fuente ni comprobación, y no se transmite. Para turistas extranjeros se usan frases breves y claras en inglés, con apoyo de mapas y de lo escrito.",
        "También se cuida el ambiente: si un turista quiere acercarse a un nido para una foto, se explica por qué no se debe molestar a los animales y se ofrece una alternativa, como mirar desde el sendero. Los datos personales de los guías, como su celular, no se entregan sin su permiso.",
    ],
    vocab=[("fuente", "documento o persona de donde viene un dato"), ("dato relevante", "dato que responde al interés y al tiempo del turista"), ("hecho", "información comprobada y con fuente"), ("relato", "tradición que cuenta la comunidad, sin comprobación histórica"), ("rumor", "lo que se dice sin fuente ni comprobación")],
    worked=[
        ("Hecho, relato o rumor", "Un turista de ejemplo cuenta: «Dicen por ahí que la plaza tiene un tesoro». Nadie lo ha confirmado. ¿Es hecho, relato o rumor?", ["No tiene fuente ni comprobación.", "Es un rumor y no se transmite como información."], "Un rumor"),
        ("Cuántos minutos sobran", "Un sendero de ejemplo mide 1.500 metros y una familia camina 50 metros por minuto. Tiene 45 minutos. ¿Le alcanza?", ["1.500 ÷ 50 = 30 minutos.", "30 es menor que 45: alcanza y sobran 15 minutos."], "Sí, con 15 minutos de sobra"),
    ],
    mistakes=[("Contar un relato como si fuera un hecho histórico.", "El turista cree que está comprobado y la comunidad puede sentirse mal representada.", "Presenta el relato diciendo que lo cuenta la comunidad."),
              ("Entregar el celular de un guía «para que lo llamen».", "Es un dato personal y solo su dueño puede autorizar que se comparta.", "Entrega el contacto de la oficina y avisa al guía.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es una fuente de información?", "El documento o la persona de donde viene un dato", "El lugar donde se vende el folleto", "El idioma en que se escribe el dato", "La fuente permite comprobar de dónde sale la información."),
        ("abc", "¿Cómo se presenta un relato de la comunidad?", "Como relato, diciendo que lo cuenta la comunidad, no como hecho comprobado", "Como un hecho histórico seguro", "No se presenta nunca, porque no sirve al turismo", "El relato es parte de la cultura, pero no está comprobado históricamente."),
        ("abc", "En Servicios de Turismo: ¿qué es un rumor?", "Algo que se dice sin fuente ni comprobación", "Una tradición cuidada por la comunidad", "Un dato del panel del administrador", "El rumor carece de fuente; la tradición es relato y el panel es fuente."),
        ("abc", "{F} ¿Cuál de los datos no debe entregarse como información al turista?", "D6, el animal gigante, porque no tiene fuente", "D2, las aves migratorias, porque es una fuente del administrador", "D3, la medida del sendero, porque viene del mapa", "D6 es un rumor; los otros vienen de fuentes del administrador."),
        ("abc", "{F} Para la familia con interés en fauna, ¿cuál es el dato más relevante?", "D2, las aves migratorias de primavera", "D4, las cooperativas de alojamiento", "D1, el cuidado como sitio protegido", "La familia quiere ver fauna, y D2 trata de las aves."),
        ("abc", "{F} Para la viajera interesada en la historia local, ¿cuál es el dato confirmado más relevante?", "D1, el cuidado como sitio protegido desde hace 20 años", "D2, las aves migratorias", "D3, la medida del sendero", "D1 tiene fuente y habla del pasado reciente del lugar."),
        ("=", "{F} Si la familia camina 50 metros por minuto (dato de ejemplo), ¿cuántos minutos tarda en recorrer el sendero circular?", "2000//50", "Se divide la longitud del sendero por los metros por minuto.", " minutos"),
        ("=", "{F} ¿Cuántos minutos le sobran a la familia de su hora para ver fauna después de recorrer el sendero?", "60-2000//50", "Se resta el tiempo del sendero a los 60 minutos que tienen.", " minutos"),
        ("abc", "{F} Si cuentas D5 a los niños, ¿qué frase corresponde?", "«Cuenta la comunidad que…»", "«Está comprobado que…»", "«Todo el mundo sabe que…»", "D5 es un relato; debe presentarse como relato, no como hecho."),
        ("abc", "{F} La viajera pregunta en inglés qué hace la gente del pueblo para vivir. ¿Qué dato usas y de dónde viene?", "D4: dos cooperativas locales ofrecen alojamiento, según la oficina municipal de ejemplo", "D6: el animal gigante, según lo que dicen", "D3: el sendero mide 2.000 metros, según el mapa", "D4 responde sobre cómo vive la gente y tiene fuente."),
        ("ab", "¿Cuál es una frase simple en inglés para decir «Por favor, quédese en el sendero»?", "Please stay on the path.", "Please leave the path.", "Stay significa quedarse y leave significa dejar; la segunda frase diría lo contrario."),
        ("abc", "{F} Un turista insiste en que le cuentes la historia del animal gigante «aunque sea rumor». ¿Qué respondes?", "Que no hay información confirmada y ofrecerle los datos confirmados de la fauna", "Contarle una historia inventada, para que quede conforme", "Decirle que sí existe, para no desilusionarlo", "No se transmiten rumores; se ofrece información confirmada que responda a su interés."),
        ("abc", "{F} Un turista propone acercarse a un nido para fotografiarlo mejor. ¿Qué corresponde?", "Explicar que no se debe molestar a los animales y sugerir mirar desde el sendero", "Permitirlo, porque la foto sirve para difundir el lugar", "Acompañarlo para que no se pierda", "Acercarse molesta a los animales; se explica la razón y se da una alternativa."),
    ],
    ctx=("abc", "{F} Al terminar, la viajera pide el celular de la guía que atendió el humedal «para contratarla otro día». ¿Qué corresponde?", "Entregar el contacto de la oficina y avisar a la guía de la solicitud", "Dar el celular personal de la guía", "Decirle que no hay forma de contactarla", "El contacto institucional protege los datos personales y permite que la guía decida."),
    sc=[
        ("En Servicios de Turismo: ¿qué diferencia hay entre hecho y relato?", "El hecho está comprobado y el relato lo cuenta la comunidad", "El relato se comparte con respeto, pero no como comprobado."),
        ("¿Qué haces con un rumor?", "No lo transmito como información", "El rumor no tiene fuente ni comprobación."),
        ("¿Cómo eliges los datos para un turista?", "Según su interés, su tiempo y que tengan fuente", "Esos tres criterios definen un dato relevante."),
    ],
    op=("Un turista de ejemplo llega con 90 minutos y quiere conocer la historia del museo del pueblo. Datos: M1, «el museo abrió en una antigua bodega» (fuente: panel del museo); M2, «la visita guiada dura 60 minutos» (fuente: administrador); M3, «dicen que un fantasma cuida la bodega» (sin fuente); M4, «la comunidad cuenta que la bodega se construyó en una noche» (relato). Selecciona los datos que le entregarías, indica cómo presentas M4 y calcula si le alcanza para la visita.",
        "Entrego M1 y M2. M3 no, porque es un rumor sin fuente. M4 lo cuento como relato: «Cuenta la comunidad que…». La visita dura 60 minutos y él tiene 90, por lo tanto le alcanza y le sobran 30 minutos.",
        ["elige datos con fuente y relevantes", "descarta el rumor y explica por qué", "presenta el relato como relato y calcula el tiempo"],
        ["lista de datos elegidos, tratamiento de M4 y cálculo"],
        ["entregar el rumor", "presentar M4 como hecho", "no calcular el tiempo"],
        "Pregunta: «¿por qué M4 no es un dato histórico?». Si no responde, repasa la diferencia entre hecho y relato."),
    reinforce="Anota un relato o una leyenda que conozcas y cómo la contarías como relato.",
    extend="Explica con un ejemplo inventado por qué un rumor puede perjudicar a un atractivo y a sus turistas.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (de ejemplo, inventada). «Casa Museo de Villa Brisa»: visitas guiadas con aforo de 20 personas por visita, de 45 minutos cada una. Horario: 10:00 a 13:00 y 15:00 a 18:00. "
     "Cada bloque parte con una visita al comenzar y las siguientes salen cada 45 minutos, de modo que la última de la mañana sale a las 12:15. "
     "Entradas de ejemplo: $3.000 adulto y $1.500 estudiante. Regla de conservación: no tocar los objetos ni usar flash.")
build(
    O3, 4, F,
    use="Aprenderé a calcular visitas por día, aforo, turnos y costos de un grupo, y a aplicar las reglas de conservación al informar a los turistas.",
    prior=["Sé pasar horas a minutos.", "Sé multiplicar y dividir con números enteros.", "Sé qué es una visita guiada."],
    explain=[
        "El aforo es la cantidad máxima de personas permitida a la vez en un lugar. Se limita para proteger el patrimonio y permitir una visita segura y de calidad. Una visita guiada es un recorrido acompañado por un guía que explica el lugar. Con el aforo y la duración se puede calcular cuántas visitas caben en un bloque de horas: se pasa el bloque a minutos y se divide por la duración de la visita, quedándose con las visitas completas.",
        "Para repartir un grupo grande se divide el número de personas por el aforo y se sube al número entero siguiente si sobran personas. Por ejemplo, 90 personas con aforo 40 requieren 3 visitas, porque 2 visitas solo reciben a 80. El costo de un grupo es la suma de cada tipo de entrada por su cantidad; los valores de este cuaderno son de ejemplo.",
        "Al informar, se agregan las reglas de conservación: no tocar los objetos antiguos y no usar flash cuando el museo lo prohíbe, porque daña los materiales. Si el turista llega fuera de horario o sin cupo, se le ofrece la próxima visita disponible y la posibilidad de reservar.",
    ],
    vocab=[("aforo", "cantidad máxima de personas permitida a la vez"), ("visita guiada", "recorrido acompañado por un guía que explica el lugar"), ("bloque horario", "tramo del día en que el atractivo atiende"), ("cupo", "lugar disponible en una visita"), ("conservación", "cuidado que evita que el patrimonio se dañe")],
    worked=[
        ("Visitas en un bloque", "Un museo de ejemplo atiende de 9:00 a 11:00 con visitas de 30 minutos. ¿Cuántas visitas caben en el bloque?", ["El bloque dura 2 horas, es decir, 120 minutos.", "120 ÷ 30 = 4 visitas."], "4 visitas"),
        ("Repartir un grupo", "Un grupo de ejemplo de 70 personas va a un lugar de aforo 25 por visita. ¿Cuántas visitas necesita?", ["70 ÷ 25 = 2 y sobran 20 personas.", "Se necesita una visita más: 3 visitas."], "3 visitas"),
    ],
    mistakes=[("Meter a todo el grupo en una sola visita «para ahorrar tiempo».", "Supera el aforo y pone en riesgo el patrimonio y la seguridad.", "Divide el grupo según el aforo."),
              ("Dejar que un turista tome fotos con flash «una sola vez».", "El flash daña materiales sensibles aunque sea una vez.", "Explica la regla de conservación y ofrece fotos permitidas.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es el aforo?", "La cantidad máxima de personas permitida a la vez en un lugar", "El precio de la entrada de un grupo", "El tiempo que dura la visita", "El aforo limita personas, no precio ni tiempo."),
        ("abc", "¿Por qué se limita el aforo de un atractivo patrimonial?", "Para proteger el lugar y permitir una visita segura y de calidad", "Para que las entradas cuesten más", "Para que las visitas duren más tiempo", "El límite cuida el patrimonio y la calidad de la visita."),
        ("abc", "En Servicios de Turismo: ¿qué es una visita guiada?", "Un recorrido acompañado por un guía que explica el lugar", "Un folleto que se entrega en la puerta", "Una exposición sin personal", "La visita guiada se acompaña de un guía; el folleto y la exposición sin personal no lo son."),
        ("=", "{F} ¿Cuántas visitas completas caben en el bloque de la mañana?", "(13-10)*60//45", "Se pasa el bloque a minutos y se divide por la duración de cada visita.", " visitas"),
        ("=", "{F} ¿Cuántas visitas hay en total en el día, sumando mañana y tarde?", "2*((13-10)*60//45)", "Los dos bloques duran lo mismo, por lo que se duplica el resultado.", " visitas"),
        ("=", "{F} ¿Cuántas personas pueden entrar en total en un día, con todas las visitas llenas?", "2*((13-10)*60//45)*20", "Se multiplica el número de visitas del día por el aforo.", " personas"),
        ("=", "{F} Un curso de 50 estudiantes quiere visitar el museo. ¿Cuántas visitas necesita?", "(50+19)//20", "Se divide por el aforo y se sube al entero siguiente cuando sobran personas.", " visitas"),
        ("=", "{F} ¿Cuántos pesos pagan en total los 50 estudiantes?", "50*1500", "Se multiplica la cantidad de estudiantes por la entrada de estudiante.", ""),
        ("=", "{F} Un grupo tiene 2 adultos y 38 estudiantes. ¿Cuántos pesos pagan en total?", "2*3000+38*1500", "Se suma el costo de los adultos y el de los estudiantes.", ""),
        ("=", "{F} Llegan 45 personas juntas. Si se reparten en las visitas necesarias, ¿cuántos cupos quedan libres en total?", "((45+19)//20)*20-45", "Se calculan los cupos de las visitas necesarias y se resta la cantidad de personas.", " cupos"),
        ("abc", "{F} Llegan 45 personas juntas. ¿Cómo las organizas?", "En 3 visitas de máximo 20 personas, repartiéndolas en grupos", "Todas juntas en una visita, para ahorrar tiempo", "Rechazar al grupo, porque supera la capacidad de una visita", "El aforo se respeta repartiendo; rechazar al grupo no es necesario."),
        ("ab", "{F} Un turista quiere tocar un objeto antiguo y sacar una foto con flash. ¿Qué corresponde?", "Explicar la regla de conservación y ofrecer una foto sin flash donde esté permitido", "Permitirlo una sola vez, porque lo pidió con amabilidad", "La regla de la ficha prohíbe tocar y usar flash, aunque la persona pida con amabilidad."),
        ("abc", "{F} Un grupo de 12 llega a las 12:40 sin reserva. ¿Qué ofreces?", "Informar que la próxima visita sale a las 15:00 y ofrecerles reservar cupo", "Meterlos en la visita que ya está en curso", "Decirles que vuelvan otro día, sin ofrecer reserva", "La última visita de la mañana ya salió; se informa la siguiente y se ofrece reservar."),
    ],
    ctx=("abc", "{F} Un docente pregunta cuántos estudiantes puede llevar a una sola visita. ¿Qué respondes?", "Hasta 20 por visita, y si son más se reparten en varias visitas", "Los que quiera, si pagan la entrada", "Hasta 45, porque la visita dura 45 minutos", "El aforo es de 20 personas por visita; los grupos mayores se dividen."),
    sc=[
        ("En Servicios de Turismo: ¿cómo se calcula cuántas visitas caben en un bloque?", "Se pasa el bloque a minutos y se divide por la duración de cada visita", "Se cuentan solo las visitas completas."),
        ("¿Cómo repartes un grupo mayor que el aforo?", "Divido por el aforo y subo al entero siguiente si sobran personas", "Así ninguna visita supera el aforo."),
        ("¿Por qué no se usa flash en un museo?", "Porque puede dañar materiales sensibles", "La regla busca la conservación del patrimonio."),
    ],
    op=("Un museo de ejemplo tiene aforo 15, visitas de 30 minutos y horario de 10:00 a 12:00. Entradas de ejemplo: $2.000 adulto y $1.000 estudiante. Llega un curso de 2 adultos y 28 estudiantes. Calcula cuántas visitas caben en el horario, cuántas necesita el curso, cuánto pagan en total y escribe un mensaje de tres líneas con la información y la regla de no usar flash.",
        "Caben 120 ÷ 30 = 4 visitas. El curso son 30 personas: 30 ÷ 15 = 2 visitas. Total: 2 × 2.000 + 28 × 1.000 = 4.000 + 28.000 = 32.000. Mensaje: «Su curso puede visitar el museo en 2 visitas de 30 minutos. El total es $32.000. Recuerden no tocar los objetos ni usar flash para proteger las piezas».",
        ["calcula visitas por horario y visitas necesarias", "calcula el total del curso", "incluye la regla de conservación en el mensaje"],
        ["cálculos y mensaje de tres líneas"],
        ["no dividir según el aforo", "cobrar a todos como adultos", "olvidar la regla de no usar flash"],
        "Pregunta: «¿por qué necesitas dos visitas?». Si no responde, repasa el cálculo con el aforo."),
    reinforce="Inventa un aforo y una duración de visita y calcula cuántas visitas caben en dos horas.",
    extend="Explica con un ejemplo inventado por qué un aforo demasiado alto puede dañar un atractivo.",
)

# ============================================================ OAE-03, clase 5
F = ("Ficha 5 (de ejemplo, inventada). Dos borradores de información sobre el «Humedal Las Totoras». Borrador A: «El humedal es el más grande del mundo, abre todos los días de 9 a 17 y se puede dar de comer a los patos. Pregunten por el guía Juan, su celular es 9 1234 5678». "
     "Borrador B: «Según el panel del administrador, el humedal abre de 9:00 a 17:00. El sendero circular mide 2.000 metros. Por favor no alimente a los animales ni saque plantas. Hoy el sendero norte está cerrado por lluvias. Para consultas, llame a la oficina del humedal». "
     "Lista de cotejo (1 punto cada una): datos con fuente; horario igual a la ficha del administrador (9:00 a 17:00); respeta el ambiente y el patrimonio; incluye la contingencia del día; no entrega datos personales de terceros. "
     "Visitantes del mes de ejemplo: semana 1, 120; semana 2, 150; semana 3, 90; semana 4, 140. Capacidad mensual de ejemplo: 600.")
build(
    O3, 5, F,
    use="Aprenderé a comparar borradores de información con una lista de cotejo, a verificar fuentes y a revisar el efecto de las visitas sobre el lugar.",
    prior=["Sé distinguir hecho, relato y rumor.", "Sé sumar, restar y dividir con números enteros.", "Sé qué es una fuente."],
    explain=[
        "Verificar una información es comprobarla con una fuente confiable, como el administrador del atractivo, antes de entregarla. Una lista de cotejo permite comparar borradores sin depender de la impresión: se revisa cada criterio y se suma un punto por cada uno cumplido. Un buen texto tiene datos con fuente, horarios correctos, reglas de cuidado, el aviso del día y ningún dato personal de terceros.",
        "Cuando una información cambia, como un nuevo horario, se actualizan los folletos y se avisa al equipo, porque los datos antiguos confunden. Si el atractivo está ligado a una comunidad o a un pueblo originario, el texto debe ser revisado y autorizado por esa comunidad o su representante antes de publicarse; no se completan datos con inventos.",
        "También se revisa el efecto del turismo con datos simples, como los visitantes de cada semana. Si el total del mes se acerca a la capacidad definida por el administrador, se refuerzan los mensajes de cuidado y se avisa a quien corresponde. En inglés, una frase de cuidado es «Please do not feed the animals» (Por favor, no alimente a los animales).",
    ],
    vocab=[("verificar", "comprobar una información con una fuente confiable"), ("lista de cotejo", "lista de criterios que se revisan uno a uno"), ("actualizar", "cambiar un dato antiguo por el vigente"), ("capacidad mensual", "máximo de visitantes que el administrador define para el mes"), ("autorización de la comunidad", "permiso de la comunidad o su representante para publicar su información")],
    worked=[
        ("Puntaje de un borrador", "Un borrador de ejemplo tiene fuente, horario correcto y respeta el ambiente, pero no incluye la contingencia del día. Tampoco entrega datos personales de terceros. ¿Cuántos puntos tiene?", ["Cumple fuente, horario y ambiente: 3 criterios.", "No entrega datos personales, y eso también es un criterio cumplido: 4 criterios."], "4 puntos"),
        ("Total y promedio", "Un lugar de ejemplo tuvo 80, 100 y 120 visitantes en tres semanas. ¿Cuál es el promedio semanal?", ["80 + 100 + 120 = 300.", "300 ÷ 3 = 100."], "100 visitantes por semana"),
    ],
    mistakes=[("Copiar un dato de internet sin comprobar si el administrador lo confirma.", "El dato puede ser antiguo o falso.", "Verifica con el administrador o su documento oficial."),
              ("Publicar un texto sobre una comunidad sin que ella lo revise.", "Puede tener errores y falta el respeto a sus integrantes.", "Pide la revisión y autorización de la comunidad o su representante.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué significa verificar una información antes de entregarla?", "Comprobarla con una fuente confiable, como el administrador del atractivo", "Repetirla igual que la escuchaste", "Hacerla más corta para que sea clara", "Verificar es comprobar con una fuente; repetir o acortar no lo asegura."),
        ("abc", "¿Qué haces cuando cambia un dato, como el horario?", "Actualizar los folletos y avisar al equipo, citando la nueva fuente", "Seguir usando el dato antiguo hasta que alguien reclame", "Cambiarlo solo en tu cuaderno", "Los datos antiguos confunden al turista, por eso se actualizan."),
        ("abc", "¿Por qué no se entrega el celular de un guía en un folleto sin su permiso?", "Porque es un dato personal y solo su dueño puede autorizar que se publique", "Porque los guías no deben tener celular", "Porque los números ocupan mucho espacio", "El celular es un dato personal; su difusión requiere autorización."),
        ("=", "{F} El borrador B cumple los cinco criterios y el borrador A solo cumple el horario. ¿Cuántos puntos menos tiene A que B?", "5-1", "Se resta el puntaje de A al puntaje de B.", " puntos"),
        ("abc", "{F} ¿Qué error del borrador A pone en riesgo el ambiente?", "Invita a dar de comer a los patos", "Dice que abre todos los días", "Menciona el horario de 9 a 17", "Alimentar animales está prohibido por el administrador y altera su conducta."),
        ("abc", "{F} ¿Qué afirmación del borrador A no se puede comprobar con la ficha?", "Decir que es el humedal más grande del mundo", "Decir que abre de 9 a 17", "Decir que hay patos", "No hay fuente que respalde esa comparación mundial."),
        ("=", "{F} ¿Cuántos visitantes tuvo el humedal en el mes de ejemplo?", "120+150+90+140", "Se suman los visitantes de las cuatro semanas.", " visitantes"),
        ("=", "{F} ¿Cuál es el promedio semanal de visitantes?", "(120+150+90+140)//4", "Se divide el total del mes por las 4 semanas.", " visitantes"),
        ("=", "{F} ¿Cuántos visitantes faltan para llegar a la capacidad mensual de ejemplo?", "600-(120+150+90+140)", "Se resta el total del mes a la capacidad de 600.", " visitantes"),
        ("abc", "{F} La semana 2 tuvo 150 visitantes. ¿Qué haces con ese dato?", "Registrarlo y analizar si conviene reforzar los mensajes de cuidado en las semanas de más visitas", "Borrarlo porque es muy alto", "Cerrar el humedal sin consultar al administrador", "Registrar y analizar permite tomar decisiones; borrar el dato oculta la información."),
        ("ab", "¿Cuál es la traducción de «Please do not feed the animals»?", "Por favor, no alimente a los animales.", "Por favor, alimente a los animales.", "La frase contiene «do not», que significa «no» e indica una prohibición."),
        ("abc", "{F} Un compañero dice: «B es largo, mejor dejamos A, que es más corto». ¿Qué respondes?", "Que B tiene datos verificados y cuida el ambiente, y puede resumirse sin perder eso", "Que tiene razón, porque lo corto es mejor", "Que se pueden mezclar los errores de A con B", "El largo no mide la calidad; A tiene errores que perjudican al turista y al lugar."),
        ("abc", "Antes de publicar un panel con la historia de una comunidad indígena de la zona, ¿qué haces?", "Pedir a la comunidad o a su representante que revise y autorice el texto", "Publicarlo con lo que se encontró en internet", "Completar con detalles inventados para hacerlo más interesante", "La historia le pertenece a la comunidad, que debe aprobar cómo se cuenta."),
    ],
    ctx=("abc", "{F} Descubres que el panel del administrador cambió el horario a 9:00 a 18:00 y tu folleto dice 17:00. ¿Qué haces?", "Confirmar con el administrador, actualizar el folleto y avisar al equipo", "Dejar el folleto como está, porque ya se imprimió", "Cambiarlo solo si un turista reclama", "Los datos desactualizados confunden; se confirma, se actualiza y se informa."),
    sc=[
        ("En Servicios de Turismo: ¿qué es una lista de cotejo?", "Una lista de criterios que se revisan uno a uno", "Así se compara con evidencia y no por impresión."),
        ("¿Quién autoriza un texto sobre la cultura de una comunidad?", "La comunidad o su representante", "La cultura le pertenece a la comunidad que la vive."),
        ("¿Qué haces cuando cambia un dato?", "Lo actualizo y aviso al equipo", "Los datos antiguos confunden al turista."),
    ],
    op=("Revisa este borrador de ejemplo: «Hola a todos. El museo abre de 8 a 20 y es el mejor del continente. Pueden tocar las piezas para sentirlas. Pregunten por la guía Ana Pérez, su dirección es Calle Sur 123». La ficha del administrador dice horario 9:00 a 17:00 y prohíbe tocar las piezas. Marca cuatro errores y reescribe el borrador corrigiéndolos, con un aviso del día de ejemplo.",
        "Errores: horario distinto al de la ficha; afirmación «el mejor del continente» sin fuente; permite tocar las piezas contra la regla; entrega la dirección de una persona. Reescritura: «Hola a todos. Según el administrador, el museo abre de 9:00 a 17:00. Por favor, no toque las piezas para protegerlas. Hoy el museo cierra la sala norte por mantención. Para consultas, llame a la oficina del museo».",
        ["encuentra cuatro errores distintos", "la reescritura corrige cada error", "incluye aviso del día y contacto institucional"],
        ["lista de errores y borrador corregido"],
        ["mantener el horario equivocado", "dejar el dato personal", "olvidar el aviso del día"],
        "Pregunta: «¿qué dato de tu texto tiene fuente?». Si no responde, repasa la verificación con el administrador."),
    reinforce="Revisa un folleto o aviso de un lugar que conozcas y anota un dato que podría estar desactualizado.",
    extend="Explica con un ejemplo inventado por qué una comunidad debe revisar el texto sobre su propia historia.",
)

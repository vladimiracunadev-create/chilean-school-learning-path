"""Hotelería TP 3.º y 4.º medio: OAE-01 (atender clientes según sus necesidades, comunicación e inglés básico) y OAE-02 (orientar e informar al turista sobre atractivos de la zona). Todo en papel: hoteles, personas, horarios y precios inventados y rotulados «de ejemplo»."""
from __future__ import annotations

from tp_seho_common import build

O1 = "TP-SEHO-3y4-OAE-01"
O2 = "TP-SEHO-3y4-OAE-02"
LIM = " Este cuaderno trabaja en papel, con datos de ejemplo: no reemplaza la práctica con un instructor ni la norma vigente."

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (hotel de ejemplo, inventado). «Hotel Brisa de Ejemplo»: 40 habitaciones, de las cuales 2 son accesibles para personas con movilidad reducida. Recepción abierta las 24 horas. "
     "Ingreso (check-in) desde las 15:00 y salida (check-out) hasta las 12:00. Desayuno de 07:00 a 10:00. Estándar de presentación del personal (de ejemplo): uniforme limpio, credencial visible, manos y uñas limpias, cabello ordenado.")
build(
    O1, 1, F,
    use="Aprenderé a distinguir necesidades, deseos y demandas de un huésped, y qué estándares de presentación, privacidad y buen trato guían la atención en un hotel.",
    prior=["Sé leer una ficha con horarios.", "Sé sumar y restar.", "Sé qué es un hotel y qué servicios ofrece."],
    explain=[
        "En Hotelería, atender a un cliente es escuchar qué busca y responder con información clara. Hay tres cosas distintas: la necesidad es lo que la persona requiere para estar bien (por ejemplo, una habitación sin escaleras si usa muletas), el deseo es lo que le gustaría tener (por ejemplo, vista al jardín) y la demanda es lo que pide de forma expresa al personal.",
        "El establecimiento ofrece servicios con horarios y condiciones, como el check-in (entrada a la habitación), el check-out (salida) y el desayuno. Quien atiende debe conocerlos para orientar e informar con precisión y no prometer lo que el hotel no puede cumplir. También cumple estándares de presentación y aseo personal: uniforme limpio, credencial visible y manos limpias.",
        "Los datos de los huéspedes, como su nombre, su habitación o sus horarios, son personales y confidenciales: no se comentan con otras personas. El trato es respetuoso y accesible para todos, sin discriminar por edad, origen, discapacidad ni apariencia." + LIM,
    ],
    vocab=[("necesidad", "lo que la persona requiere para estar bien o poder usar el servicio"), ("deseo", "lo que a la persona le gustaría tener, aunque no sea indispensable"), ("demanda", "lo que la persona pide de forma expresa al personal"), ("check-in", "entrada del huésped a su habitación"), ("check-out", "salida del huésped de su habitación"), ("confidencialidad", "obligación de no comentar ni entregar datos de los huéspedes a terceros"), ("accesible", "que puede ser usado por personas con movilidad reducida u otra discapacidad")],
    worked=[
        ("Clasificar una frase", "Un huésped de ejemplo dice: «Necesito una habitación sin escaleras porque uso muletas». ¿Es una necesidad, un deseo o una demanda principal?", ["La frase habla de algo que requiere para poder usar la habitación.", "No es un gusto: sin eso no podría desplazarse."], "Una necesidad"),
        ("Calcular horas de atención", "La recepción de otro hotel de ejemplo atiende de 08:00 a 20:00. ¿Cuántas horas atiende al día?", ["Se resta la hora de apertura a la hora de cierre.", "20 − 8 = 12."], "12 horas"),
    ],
    mistakes=[("Comentar con una compañera, en voz alta y frente a otros huéspedes, el nombre y la habitación de una persona conocida.", "Esos datos son personales y confidenciales; hablarlos en público puede poner en riesgo a la persona.", "Guarda silencio sobre los datos del huésped y atiende en voz baja cuando debas verificarlos."),
              ("Dar por hecho que una persona mayor o con discapacidad «no puede» o «no quiere» algo sin preguntarle.", "Supone cosas por su apariencia y puede discriminarla; cada persona expresa sus propias necesidades.", "Pregunta con respeto qué necesita y ofrece las opciones disponibles.")],
    T=[
        ("abc", "En Hotelería: ¿qué es una demanda de un huésped?", "Lo que pide de forma expresa al personal", "El precio total de su estadía", "El horario de limpieza de su habitación", "La demanda es la petición que la persona hace; el precio y el horario son datos del servicio."),
        ("abc", "{F} ¿Desde qué hora se puede ingresar a la habitación?", "Desde las 15:00", "Desde las 12:00", "Desde las 07:00", "La ficha fija el ingreso desde las 15:00; las 12:00 es la hora límite de salida."),
        ("abc", "{F} ¿Hasta qué hora se sirve el desayuno?", "Hasta las 10:00", "Hasta las 12:00", "Hasta las 15:00", "La ficha indica desayuno de 07:00 a 10:00; las otras horas son de salida e ingreso."),
        ("=", "{F} Hoy hay 26 habitaciones ocupadas. ¿Cuántas de las 40 habitaciones del hotel están libres?", "40-26", "Al total de habitaciones se le restan las ocupadas.", " habitaciones"),
        ("abc", "Un huésped dice: «Me encantaría ver el mar, pero lo que necesito sí o sí es una cuna para mi bebé». ¿Cuál es su necesidad y cuál su deseo?", "Necesidad: la cuna; deseo: ver el mar", "Necesidad: ver el mar; deseo: la cuna", "Las dos son necesidades indispensables", "Lo que pide «sí o sí» para su bebé es la necesidad; ver el mar es un gusto."),
        ("abc", "{F} Una huésped llega en silla de ruedas y reservó sin avisarlo. ¿Qué corresponde hacer?", "Preguntarle con respeto qué necesita y ofrecerle una de las habitaciones accesibles", "Asignarle la primera habitación libre sin consultarle", "Pedirle que vuelva con un familiar que decida por ella", "La persona expresa sus necesidades y el hotel cuenta con habitaciones accesibles para atenderla."),
        ("abc", "{F} ¿Qué cumple con el estándar de presentación del personal del hotel?", "Uniforme limpio, credencial visible y manos y uñas limpias", "Perfume muy fuerte para que se note la limpieza", "Ropa de calle sin credencial para sentirse cómodo", "La ficha fija uniforme, credencial y aseo; el perfume fuerte y la ropa libre no están en el estándar."),
        ("=", "{F} Con un ritmo de ejemplo de 18 huéspedes atendidos por hora en el desayuno, ¿cuántos huéspedes pueden atenderse durante todo el horario de desayuno?", "(10-7)*18", "Se multiplican las horas de desayuno por los huéspedes atendidos cada hora.", " huéspedes"),
        ("abc", "Alguien llama por teléfono y pide el nombre del huésped que ocupa la habitación 12. ¿Qué corresponde responder?", "Que no se entregan datos de huéspedes y ofrecer tomar un mensaje para esa habitación", "Dar el nombre si la persona suena amable", "Dar el nombre si dice ser amigo del huésped", "Los datos de los huéspedes son confidenciales y el mensaje permite ayudar sin revelarlos."),
        ("abc", "Un huésped adulto mayor pide a la recepcionista que hable más despacio. ¿Qué haces?", "Repetir con calma y confirmar que entendió", "Hablar más fuerte y más rápido", "Entregarle un papel y no explicar nada", "Hablar con calma respeta su ritmo; subir la voz y apurarse no mejora la comprensión."),
        ("abc", "{F} A las 11:00 llega un huésped que quiere entrar a su habitación, pero el ingreso es desde las 15:00 y aún no está lista. ¿Qué respuesta es la adecuada?", "Explicar el horario, ofrecer guardar su equipaje y avisarle cuando la habitación esté lista", "Decirle que vuelva a las 15:00 y no ofrecer nada más", "Prometerle que estará lista a las 12:00 sin consultar a nadie", "Informar con claridad y ofrecer una alternativa evita promesas que el hotel no puede cumplir."),
        ("abc", "Un huésped llega molesto a reclamar por ruido nocturno en el pasillo. ¿Qué corresponde primero?", "Escucharlo sin interrumpir, disculparse por la molestia y anotar su reclamo", "Explicar que otros huéspedes tienen derecho a hacer ruido", "Pedirle que escriba su reclamo otro día", "Escuchar y registrar muestra respeto y permite resolver; discutir o postergar empeora la situación."),
        ("abc", "{F} Un recepcionista llega al turno con la camisa sucia y sin credencial porque «no hay mucha gente hoy». ¿Qué corresponde?", "Cumplir el estándar igual, porque se aplica siempre, haya poca o mucha gente", "Cumplirlo solo cuando llega un huésped importante", "No cumplirlo si la jefatura no está en el hotel", "El estándar de presentación vale en todo momento y no depende de quién mire."),
    ],
    ctx=("abc", "{F} Una pareja de ejemplo llega a las 14:00. Pide «una habitación tranquila» y comenta que le encantaría ver el jardín, pero que su hijo necesita estar cerca del baño por un tratamiento. ¿Qué haces?", "Registrar la cercanía al baño como necesidad, ofrecer vista al jardín solo si es posible y mantener sus datos en reserva", "Asignar la habitación con vista al jardín aunque quede lejos del baño", "Comentar el tratamiento del niño con el resto del personal para que todos lo sepan", "La necesidad manda sobre el deseo y los datos de salud no se comparten con quien no los necesita."),
    sc=[
        ("En Hotelería: ¿cómo se llama lo que el huésped pide de forma expresa?", "Demanda", "La demanda es la petición expresa; la necesidad es lo que requiere."),
        ("¿Qué haces con el nombre y la habitación de un huésped si te los piden por teléfono?", "No los entrego", "Son datos personales y confidenciales del huésped."),
        ("¿Qué estándar cumple la presentación personal del personal?", "Uniforme limpio, credencial visible y aseo", "Esos elementos muestran orden y cuidado frente al huésped."),
    ],
    op=("Un hotel de ejemplo tiene check-in desde las 15:00, check-out hasta las 12:00 y desayuno de 07:30 a 10:30. Llega una familia: dos adultos, una niña de 5 años y un abuelo que usa bastón. Dicen: «Queremos desayunar tranquilos, nos gustaría una habitación con vista, y mi papá no puede subir escaleras». "
        "Escribe: una necesidad, un deseo y una demanda de la familia; dos datos del hotel que les informarías; y una regla de privacidad y una de trato respetuoso que aplicarías.",
        "Necesidad: habitación sin escaleras para el abuelo. Deseo: vista (y desayunar tranquilos). Demanda: lo que piden de forma expresa, es decir, una habitación con vista y sin escaleras. Informaría: ingreso desde las 15:00 y desayuno de 07:30 a 10:30. Privacidad: no comentar sus datos con otros huéspedes. Trato: preguntar al abuelo cómo prefiere que lo ayuden, sin suponer.",
        ["distingue necesidad, deseo y demanda con la frase de la familia", "informa dos datos correctos del hotel", "nombra una regla de privacidad y una de trato respetuoso"],
        ["hoja con las tres clasificaciones, dos datos del hotel y dos reglas"],
        ["decir que la vista es una necesidad", "inventar horarios que el enunciado no da", "olvidar la privacidad"],
        "Pregunta: «¿qué pasaría si no se cumple la vista y qué si no se cumple la accesibilidad?». Si responde igual para ambas, repasa necesidad frente a deseo."),
    reinforce="Escribe tres frases que podría decir un huésped y marca cuál es una necesidad, cuál un deseo y cuál una demanda.",
    extend="Explica con un ejemplo inventado por qué atender igual de bien a todas las personas es parte del estándar de un hotel.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (frases de recepción, de ejemplo). Bienvenido = Welcome. ¿Tiene una reserva? = Do you have a reservation? ¿Me da su nombre, por favor? = May I have your name, please? "
     "Un momento, por favor = Just a moment, please. ¿En qué puedo ayudarle? = How can I help you? Gracias = Thank you.")
build(
    O1, 2, F,
    use="Aprenderé técnicas de comunicación efectiva (escucha activa, preguntas, parafraseo, tono) y algunas frases de inglés básico para recibir a un huésped.",
    prior=["Conozco necesidad, deseo y demanda.", "Sé multiplicar.", "Sé saludar con cortesía en español."],
    explain=[
        "La comunicación efectiva es lograr que el mensaje se entienda y que la persona se sienta atendida. Sus técnicas son la escucha activa (mirar, no interrumpir y mostrar que se entiende), el parafraseo (repetir con tus palabras lo que entendiste y preguntar si es correcto), el tono amable y claro, y el lenguaje corporal abierto, con una postura relajada y contacto visual respetuoso.",
        "Una pregunta abierta no se responde con sí o no, como «¿qué necesita para su estadía?», y sirve para descubrir necesidades. Una pregunta cerrada sí se responde con sí o no, como «¿tiene reserva?», y sirve para confirmar datos. Si la persona oye con dificultad, se habla de frente, con claridad y sin gritar, y se ofrece escribir lo importante.",
        "Con un huésped extranjero se usa inglés básico: frases cortas y simples, con un tono amable, como las de la ficha. Si no sabes algo, no inventes: di que lo consultarás y vuelve con la respuesta." + LIM,
    ],
    vocab=[("comunicación efectiva", "lograr que el mensaje se entienda y que la persona se sienta atendida"), ("escucha activa", "atender sin interrumpir y mostrar que se entiende lo que la persona dice"), ("parafraseo", "repetir con tus palabras lo que entendiste y confirmar si es correcto"), ("pregunta abierta", "pregunta que no se responde solo con sí o no"), ("pregunta cerrada", "pregunta que se responde con sí o no"), ("reservation", "reserva, en inglés")],
    worked=[
        ("Parafrasear un pedido", "Un huésped de ejemplo dice: «Somos cuatro, llegamos el sábado y queremos dos camas». ¿Cómo lo parafraseas?", ["Se repite lo entendido con otras palabras.", "Se termina preguntando si es correcto."], "«Entiendo: son cuatro personas, llegan el sábado y necesitan dos camas. ¿Es correcto?»"),
        ("Elegir una pregunta abierta", "¿Cuál es abierta: «¿Le gusta la habitación?» o «¿Qué le pareció la habitación?»", ["La primera se responde con sí o no.", "La segunda pide una opinión libre."], "«¿Qué le pareció la habitación?»"),
    ],
    mistakes=[("Contestar a un huésped sin mirarlo mientras se escribe en el computador.", "La persona siente que no la escuchan, aunque se entienda el pedido.", "Detén un momento lo que haces, mírala y confirma lo que pidió."),
              ("Inventar una respuesta cuando no se sabe un dato del hotel.", "Una respuesta falsa genera reclamos y pérdida de confianza.", "Di «Just a moment, please» o «un momento, por favor», consulta y vuelve con el dato correcto.")],
    T=[
        ("abc", "En Hotelería: ¿qué es la escucha activa?", "Atender sin interrumpir y mostrar que se entiende lo que la persona dice", "Hablar más fuerte para que la persona escuche mejor", "Responder rápido sin esperar a que termine", "La escucha activa exige atención completa; apurarse o gritar no es escuchar."),
        ("abc", "{F} ¿Cómo se dice «¿Tiene una reserva?» en inglés según la ficha?", "Do you have a reservation?", "How can I help you?", "May I have your name, please?", "La ficha asocia esa pregunta a la reserva; las otras son para ayudar y pedir el nombre."),
        ("abc", "{F} ¿Qué significa «Just a moment, please»?", "Un momento, por favor", "Gracias", "Bienvenido", "Es la frase para pedir un instante de espera con cortesía, según la ficha."),
        ("abc", "¿Cuál de estas es una pregunta abierta?", "¿Qué necesita para su estadía?", "¿Viene solo?", "¿Tiene reserva?", "Las dos últimas se responden con sí o no; la primera pide contar qué necesita."),
        ("abc", "Un huésped dice: «Necesito salir mañana a las 06:00 y quiero desayunar antes». ¿Cuál es un buen parafraseo?", "«Entiendo: saldrá mañana a las 06:00 y necesita desayunar antes. ¿Es así?»", "«Muy bien, le pediré un taxi para las 05:00»", "«¿Qué le pasa con el desayuno?»", "Parafrasear es repetir lo entendido y confirmar; agregar datos o cambiar el tema no lo es."),
        ("=", "En un turno de ejemplo de 8 horas hay 1 hora de pausa. Durante las demás horas se atienden 6 huéspedes por hora. ¿Cuántos huéspedes se atienden en el turno?", "(8-1)*6", "Se restan las horas de pausa y se multiplica por los huéspedes de cada hora.", " huéspedes"),
        ("abc", "Un huésped llega molesto y habla fuerte. ¿Cómo debe ser el tono de quien lo atiende?", "Calmado, bajo y claro, sin discutir", "Igual de fuerte para que se sienta escuchado", "Muy seco, para terminar rápido", "Un tono calmado baja la tensión; igualar el volumen o cortar la conversación la aumenta."),
        ("abc", "Una huésped con dificultad para oír te habla en la recepción. ¿Qué corresponde?", "Hablarle de frente, con claridad y sin gritar, y ofrecer escribir lo importante", "Gritarle para que oiga", "Hablarle mientras miras la pantalla", "Hablar de frente permite leer los labios; gritar y mirar a otro lado no ayudan."),
        ("abc", "{F} Llega un huésped extranjero. ¿Qué orden de frases sería adecuado al recibirlo?", "Welcome → Do you have a reservation? → May I have your name, please?", "May I have your name, please? → Thank you → Welcome", "Just a moment, please → Do you have a reservation? → Thank you", "Se saluda primero, luego se pregunta por la reserva y después se pide el nombre."),
        ("=", "{F} Un practicante repasa las frases de la ficha: cada una 5 veces por día durante 4 días. ¿Cuántas repeticiones suma?", "6*5*4", "Se multiplican las frases de la ficha por las repeticiones y por los días.", " repeticiones"),
        ("abc", "Una persona llama y pide el número de habitación de otro huésped diciendo que es su amiga. ¿Qué respondes?", "Que no puedes entregarlo y que puedes tomar un mensaje para esa persona", "Que el número es el 204, porque suena confiable", "Que mejor llame a otra hora para ver si alguien se lo dice", "La confidencialidad se mantiene siempre y el mensaje permite ayudar sin revelar datos."),
        ("abc", "Un huésped pregunta por el horario de un restaurante cercano que no conoces. ¿Qué haces?", "Decirle que consultarás y volver con el dato correcto", "Inventar un horario que parezca probable", "Decirle que no sabes y seguir con otra tarea", "Consultar y volver con la respuesta cuida la confianza; inventar o ignorar no ayuda."),
        ("abc", "Un recepcionista responde con los brazos cruzados, sin mirar y suspirando. ¿Qué se puede mejorar?", "Adoptar una postura abierta, mirar a la persona y hablar con tono amable", "Hablar más rápido para terminar antes", "Cambiar el idioma sin preguntar", "El lenguaje corporal también comunica; una postura abierta transmite disposición."),
    ],
    ctx=("abc", "{F} Una turista de ejemplo se acerca a la recepción y dice algo en inglés que entiendes a medias. ¿Qué haces?", "Sonreír, usar una frase simple como «How can I help you?» y confirmar con calma lo que pidió", "Responderle en español muy rápido y fuerte", "Decirle que vuelva con alguien que hable español", "Una frase simple y un tono amable permiten entender; apurarse o rechazar la atención no ayudan."),
    sc=[
        ("En Hotelería: ¿cómo se llama repetir con tus palabras lo que entendiste?", "Parafraseo", "El parafraseo confirma que se entendió bien."),
        ("¿Cómo se dice «Bienvenido» en inglés según la ficha?", "Welcome", "Es la primera frase de saludo de la ficha."),
        ("¿Qué haces si no sabes un dato que te piden?", "Consulto y vuelvo con la respuesta", "Inventar un dato genera reclamos y desconfianza."),
    ],
    op=("Un huésped de ejemplo llega a un hotel y dice: «Hola, somos tres personas, venimos a una boda el sábado, queremos habitaciones cerca y no sé si el desayuno se sirve temprano, porque salimos a las 7». "
        "Escribe: un parafraseo de lo que dijo, dos preguntas abiertas y una cerrada que le harías, y dos frases en inglés de la ficha de esta clase que usarías con un huésped extranjero.",
        "Parafraseo: «Entiendo: son tres personas, vienen a una boda el sábado, quieren habitaciones cercanas y necesitan saber si pueden desayunar antes de las 7. ¿Es correcto?». Abiertas: «¿Qué necesita para su estadía?», «¿Qué tipo de habitaciones prefiere?». Cerrada: «¿Tiene reserva?». Inglés: «Welcome» y «How can I help you?».",
        ["parafrasea sin agregar datos", "las preguntas abiertas no se responden con sí o no", "usa dos frases correctas de la ficha"],
        ["hoja con parafraseo, tres preguntas y dos frases en inglés"],
        ["agregar datos que no dijo el huésped", "hacer preguntas abiertas que se contestan con sí o no", "mezclar frases en inglés que no están en la ficha"],
        "Pregunta: «¿tu pregunta abierta se puede contestar solo con sí?». Si es así, pídele que la reformule empezando con «qué» o «cómo»."),
    reinforce="Escribe tres preguntas abiertas y tres cerradas que harías a un huésped al recibirlo.",
    extend="Explica por qué confirmar con un parafraseo evita errores en una reserva.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). «Hotel Brisa de Ejemplo» tiene 3 pisos y el ascensor está en mantención hoy. Habitaciones libres en el primer piso: 102 (dos camas individuales, 2 personas), 105 (una cama matrimonial y dos individuales, 4 personas) y 108 (una cama matrimonial, 2 personas). "
     "Llega la familia Ejemplo a las 16:30: dos adultos, una niña de 4 años y el abuelo, que usa bastón. Reservaron «una habitación» para cuatro personas. Dicen: «Mi papá no puede subir escaleras» y «ojalá tuviera vista al jardín».")
build(
    O1, 3, F,
    use="Aprenderé a analizar un caso de atención: separar la necesidad del deseo, revisar qué puede ofrecer el hotel y decidir con respeto y claridad.",
    prior=["Distingo necesidad, deseo y demanda.", "Sé usar preguntas y parafraseo.", "Sé leer una ficha de habitaciones disponibles."],
    explain=[
        "Para analizar un caso de atención se siguen pasos: primero se identifica qué dijo el huésped y se separa la necesidad (lo indispensable), el deseo (lo que le gustaría) y la demanda (lo que pidió). Luego se revisa qué puede ofrecer el hotel con los datos que se tienen: habitaciones libres, capacidad, estado de los servicios y horarios.",
        "Después se elige la alternativa que cubre la necesidad, se intenta acercarse al deseo si es posible y se explica la decisión con claridad. Una limitación del hotel, como un ascensor en mantención (una reparación o revisión programada), se informa con honestidad, sin prometer lo que no se puede cumplir.",
        "Se registra lo acordado en la ficha de registro del huésped, que es el documento donde se anotan los datos de la estadía. En ella no se escriben datos personales innecesarios, como diagnósticos de salud." + LIM,
    ],
    vocab=[("alternativa", "opción que puede elegirse para resolver una situación"), ("capacidad", "cantidad de personas que caben en una habitación"), ("mantención", "reparación o revisión programada de un equipo o servicio"), ("ficha de registro", "documento donde se anotan los datos de la estadía del huésped"), ("limitación", "algo que impide ofrecer un servicio tal como se pide")],
    worked=[
        ("Elegir según capacidad", "En un caso de ejemplo llegan 3 personas y hay libres una habitación para 2 y otra para 4. ¿Cuál cubre la necesidad?", ["La habitación debe tener capacidad para todas las personas.", "Solo la de 4 alcanza para 3 personas."], "La habitación para 4 personas"),
        ("Informar una limitación", "Un huésped de ejemplo quiere usar el ascensor, pero está en mantención. ¿Qué se hace?", ["Se informa con honestidad que no está disponible.", "Se ofrece una alternativa, como una habitación en el primer piso."], "Informar la limitación y ofrecer una habitación en el primer piso"),
    ],
    mistakes=[("Asignar una habitación del segundo piso a la familia porque «tiene mejor vista», aunque el ascensor no funciona.", "Se prioriza un deseo sobre la necesidad indispensable del abuelo.", "Elige primero la que cubre la necesidad y después acércate al deseo."),
              ("Prometer que el ascensor funcionará «en un rato» sin saberlo.", "Una promesa sin respaldo genera desconfianza si no se cumple.", "Informa solo lo que sabes y ofrece una alternativa concreta.")],
    T=[
        ("abc", "{F} ¿Cuál es la necesidad principal de la familia?", "Que el abuelo no deba subir escaleras", "Tener vista al jardín", "Tener una cama matrimonial", "La ficha dice que el abuelo no puede subir escaleras; la vista es un deseo."),
        ("abc", "{F} ¿Cuál es el deseo de la familia?", "Tener vista al jardín", "Que el abuelo no suba escaleras", "Alojar a cuatro personas", "El deseo es «ojalá tuviera vista al jardín»; las otras dos son requisitos del caso."),
        ("abc", "{F} ¿Por qué no se puede ofrecer una habitación del segundo piso?", "Porque el ascensor está en mantención y el abuelo no puede subir escaleras", "Porque la familia reservó solo habitaciones del primer piso", "Porque en el segundo piso las habitaciones son siempre más pequeñas", "La ficha dice que hay 3 pisos y el ascensor no funciona hoy, y el abuelo no puede subir escaleras."),
        ("abc", "{F} ¿Qué habitación del primer piso tiene capacidad para las cuatro personas?", "La 105", "La 102", "La 108", "La 105 es para 4 personas; la 102 y la 108 son para 2."),
        ("=", "{F} La 105 es para 4 personas y la familia son 4. ¿Cuántas camas tiene la 105 entre matrimonial e individuales?", "1+2", "Se suman la cama matrimonial y las dos individuales.", " camas"),
        ("abc", "{F} ¿Cómo se informa a la familia el problema del ascensor?", "Con honestidad: hoy no funciona y se les ofrece una habitación del primer piso", "Diciéndoles que funciona, para que no se molesten", "No avisando, porque igual van a ver las escaleras", "Informar la limitación y ofrecer una alternativa es la forma honesta de atender."),
        ("abc", "{F} La familia pregunta si la 105 tiene vista al jardín y no tienes el dato. ¿Qué haces?", "Decir que lo consultarás y volver con la respuesta", "Decir que sí para que se sientan contentos", "Decir que no sin revisar", "Si no sabes, consultas; inventar un dato puede generar un reclamo."),
        ("=", "{F} Si la familia se aloja 3 noches y el hotel cobra $52.000 por noche la 105 (precio de ejemplo), ¿cuánto es el total de alojamiento?", "52000*3", "Se multiplica el precio por noche por las noches de estadía.", " pesos"),
        ("abc", "{F} Entre las tres habitaciones, ¿cuál es la mejor alternativa para el caso?", "La 105, porque está en el primer piso y tiene capacidad para las cuatro personas", "La 102, porque tiene dos camas individuales", "La 108, porque tiene cama matrimonial", "Solo la 105 cumple las dos condiciones: planta baja del primer piso y cuatro personas."),
        ("abc", "{F} Un compañero propone asignar a la familia dos habitaciones, la 102 y la 108, «para que quepan todos». ¿Qué observación corresponde?", "Es una alternativa posible, pero separa a la familia; la 105 los reúne en una sola habitación", "Es imposible, porque la 102 y la 108 no están en el primer piso", "Es la mejor, porque siempre es mejor tener dos habitaciones que una", "La 102 y la 108 están libres en el primer piso, pero la 105 cubre la necesidad con una sola habitación."),
        ("abc", "{F} El abuelo cuenta que toma un medicamento por una enfermedad. ¿Qué haces con ese dato?", "No anotarlo en la ficha ni comentarlo, salvo que él pida ayuda concreta al hotel", "Anotarlo en la ficha para que lo vea todo el personal", "Contarlo a otros huéspedes que pregunten", "Los datos de salud son personales y solo se usan con permiso y para ayudar a la persona."),
        ("abc", "{F} A las 18:00, un huésped de otra habitación pide que la familia cambie a la 105 porque la quería él. ¿Qué respondes?", "Que la habitación ya fue asignada por una necesidad y que puedes ofrecerle otra alternativa", "Que se la cambias, porque el último que pide tiene prioridad", "Que le dirás quién la ocupa y por qué", "No se revelan datos de otros huéspedes y la asignación ya responde a una necesidad."),
        ("=", "{F} Si el hotel cobra $52.000 por noche la 105 y la familia paga $20.000 de anticipo (monto de ejemplo), ¿cuánto falta por pagar de la primera noche?", "52000-20000", "Al precio de la noche se le resta el anticipo ya pagado.", " pesos"),
    ],
    ctx=("abc", "{F} Pasadas las 21:00 la familia llama a la recepción para decir que la niña no puede dormir por el ruido de un evento en el salón. ¿Qué haces primero?", "Escuchar con calma, pedir disculpas, consultar al encargado del evento y ofrecerle una solución concreta", "Decirle que es un evento programado y que no hay nada que hacer", "Pedirle que baje a reclamar por sí misma al salón", "Escuchar y buscar una solución atiende la necesidad; descartarla o derivarla al huésped no ayuda."),
    sc=[
        ("En Hotelería: ¿qué se identifica primero al analizar un caso de atención?", "Lo que dijo el huésped, separando necesidad, deseo y demanda", "Sin eso no se puede elegir una alternativa adecuada."),
        ("¿Qué haces si no puedes cumplir lo pedido?", "Informo la limitación y ofrezco una alternativa", "Se actúa con honestidad y se busca una solución."),
        ("¿Qué datos de salud se anotan en la ficha de registro?", "Ninguno, salvo lo estrictamente necesario y con permiso", "Los datos de salud son personales y sensibles."),
    ],
    op=("Caso de ejemplo. Hotel con 2 habitaciones libres: la 201 (cama matrimonial, 2 personas, segundo piso, con balcón) y la 104 (dos camas individuales, 2 personas, primer piso, sin balcón). El ascensor funciona. "
        "Llega una pareja de adultos mayores. Dicen: «Queremos descansar, nos gustaría un balcón, y mi esposa se cansa al caminar distancias largas». "
        "Escribe: la necesidad, el deseo, la habitación que ofrecerías con su razón, y cómo informarías con honestidad lo que no pueden tener.",
        "Necesidad: poca caminata, es decir, una habitación cercana a la entrada o con ascensor. Deseo: balcón. Ofrecería la 104 porque queda en el primer piso, cerca de la entrada, aunque no tiene balcón. Informaría con honestidad: «El balcón solo lo tiene la 201, del segundo piso, y el ascensor funciona; si prefieren balcón, puedo mostrarles el camino, pero la 104 les queda más cerca».",
        ["separa necesidad y deseo", "elige con razón y sin inventar datos", "informa con honestidad lo que no se puede"],
        ["hoja con necesidad, deseo, habitación elegida y frase al huésped"],
        ["elegir la habitación por el balcón sin considerar la necesidad", "inventar que la 104 tiene balcón", "no ofrecer alternativa"],
        "Pregunta: «¿qué pasaría si la señora elige la 201?». Debe responder que ella decide con la información, y el hotel respeta su elección."),
    reinforce="Escribe un caso de tres líneas de un huésped con una necesidad y un deseo, y qué habitación de una lista inventada le ofrecerías.",
    extend="Explica por qué decir la verdad sobre una limitación es mejor para la reputación del hotel que prometer algo que no se puede cumplir.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (servicios y precios de ejemplo, inventados). Late check-out (salida hasta las 14:00): $15.000. Traslado al terminal de buses: $12.000 por viaje, hasta 4 personas. "
     "Lavado de ropa por prenda: $1.500 (se entrega a las 18:00 si se pide antes de las 10:00). Estacionamiento: $6.000 por noche. Tarifa incluye desayuno. Check-out normal hasta las 12:00.")
build(
    O1, 4, F,
    use="Aprenderé a orientar e informar con precisión sobre los servicios del hotel, calculando costos y horarios con una ficha de servicios.",
    prior=["Distingo necesidad y deseo.", "Sé multiplicar y sumar dinero.", "Sé leer horarios."],
    explain=[
        "Informar bien es dar el dato correcto, completo y a tiempo: qué incluye el servicio, cuánto cuesta, hasta qué hora está disponible y qué condiciones tiene. Un servicio incluido en la tarifa no se cobra aparte; un servicio adicional sí tiene un precio. El huésped decide con esa información y no debe enterarse de un cobro recién al pagar.",
        "Para dar el precio total de un servicio se multiplica el precio unitario por la cantidad. Por ejemplo, si un servicio cuesta $2.000 por unidad y se piden 3, el total es $6.000. Si el servicio tiene un tope, como un traslado hasta 4 personas, se informa para que el huésped sepa cuándo se necesita otro viaje.",
        "Antes de informar, quien atiende verifica la ficha vigente de servicios, para no dar precios antiguos. Si un huésped pide algo que no está en la ficha, se consulta a la jefatura." + LIM,
    ],
    vocab=[("servicio incluido", "servicio que forma parte de la tarifa y no se cobra aparte"), ("servicio adicional", "servicio que se cobra aparte de la tarifa"), ("precio unitario", "precio de una sola unidad del servicio"), ("tope", "límite máximo, como la cantidad de personas por viaje"), ("ficha vigente", "ficha actualizada que se usa para dar datos correctos")],
    worked=[
        ("Costo total de un servicio", "Un servicio de ejemplo cuesta $2.500 por unidad y un huésped pide 4 unidades. ¿Cuál es el total?", ["Total = precio unitario × cantidad.", "2.500 × 4 = 10.000."], "$10.000"),
        ("Número de viajes por tope", "Un traslado de ejemplo lleva hasta 3 personas por viaje y deben viajar 7 personas. ¿Cuántos viajes se necesitan?", ["7 ÷ 3 es 2 y sobra 1 persona.", "Esa persona necesita un tercer viaje."], "3 viajes"),
    ],
    mistakes=[("Informar el precio del late check-out de memoria sin revisar la ficha vigente.", "El precio pudo cambiar y el huésped recibiría un dato incorrecto.", "Revisa siempre la ficha vigente antes de informar."),
              ("Decir «el desayuno se cobra aparte» cuando la tarifa lo incluye.", "Es un dato falso que puede asustar al huésped o hacerle pagar de más.", "Aclara que el desayuno está incluido en la tarifa, según la ficha.")],
    T=[
        ("abc", "En Hotelería: ¿qué es un servicio adicional?", "Un servicio que se cobra aparte de la tarifa", "Un servicio que el hotel no ofrece", "Un servicio que forma parte de la tarifa", "Adicional significa que se suma y se cobra aparte; el incluido ya está en la tarifa."),
        ("abc", "{F} ¿El desayuno se cobra aparte?", "No: la tarifa lo incluye", "Sí: cuesta $6.000", "Sí: cuesta $1.500", "La ficha dice que la tarifa incluye desayuno; $6.000 es el estacionamiento y $1.500 el lavado."),
        ("abc", "{F} ¿Hasta qué hora es el check-out normal?", "Hasta las 12:00", "Hasta las 14:00", "Hasta las 10:00", "La ficha fija las 12:00; las 14:00 corresponde al late check-out."),
        ("=", "{F} Un huésped usa el estacionamiento 3 noches. ¿Cuánto paga?", "6000*3", "Se multiplica el precio por noche por el número de noches.", " pesos"),
        ("=", "{F} Un huésped pide lavar 8 prendas. ¿Cuánto cuesta el servicio?", "1500*8", "Se multiplica el precio por prenda por la cantidad de prendas.", " pesos"),
        ("abc", "{F} Un huésped quiere salir a las 13:30 y pregunta si puede. ¿Qué le informas?", "Que existe el late check-out, hasta las 14:00, con un costo de $15.000", "Que no existe ninguna opción después de las 12:00", "Que puede salir a la hora que quiera sin costo", "La ficha ofrece late check-out hasta las 14:00 con costo."),
        ("=", "{F} Son 6 personas que deben ir al terminal de buses. ¿Cuánto cuesta en total si hay que pagar dos viajes?", "12000*2", "Se multiplica el precio de un viaje por el número de viajes.", " pesos"),
        ("abc", "{F} Un huésped pide lavar ropa a las 11:00 y quiere recuperarla a las 18:00. ¿Qué le dices?", "Que el pedido debía hacerse antes de las 10:00 para entregarlo a las 18:00, y consultarás si hay otra opción", "Que se la entregas a las 18:00 sin problema", "Que el servicio no existe", "La ficha condiciona la entrega a las 18:00 a pedirla antes de las 10:00."),
        ("abc", "{F} Hay 5 personas que necesitan el traslado al terminal de buses. ¿Cuántos viajes son necesarios?", "2 viajes", "1 viaje", "3 viajes", "Un viaje lleva hasta 4 personas; con 5 sobra una y se necesita otro."),
        ("=", "{F} Un huésped pide 1 late check-out, 2 noches de estacionamiento y 4 prendas de lavado. ¿Cuánto es el total de servicios adicionales?", "15000+6000*2+1500*4", "Se calcula cada servicio y se suman los tres totales.", " pesos"),
        ("abc", "{F} Un huésped pregunta por el precio del servicio de masajes, que no aparece en la ficha. ¿Qué haces?", "Decirle que consultarás a la jefatura y volver con el dato", "Inventar un precio parecido al del lavado", "Decirle que no hay masajes en ningún hotel", "Lo que no está en la ficha se consulta; inventar un precio puede producir un cobro incorrecto."),
        ("abc", "{F} Un compañero informa «el traslado cuesta $12.000 por persona». ¿Qué corrección corresponde?", "Es por viaje y sirve hasta 4 personas", "Está bien así", "Cuesta $12.000 por noche", "La ficha dice por viaje, con tope de 4 personas."),
        ("=", "{F} Una familia paga estacionamiento por 2 noches y lavado de 10 prendas. Paga con un billete de $50.000. ¿Cuánto vuelto recibe?", "50000-(6000*2+1500*10)", "Se calcula el total de ambos servicios y se resta del billete.", " pesos"),
    ],
    ctx=("abc", "{F} Un huésped de ejemplo comenta: «Me dijeron en la reserva que el estacionamiento era gratis». La ficha dice que cuesta. ¿Qué haces?", "Revisar la reserva, explicar con calma el dato de la ficha y consultar a la jefatura si hubo un acuerdo", "Decirle que se equivocó y cobrarle", "Darle el estacionamiento gratis sin revisar", "Se verifica el acuerdo antes de decidir; acusar o regalar el servicio sin revisar son errores."),
    sc=[
        ("En Hotelería: ¿cómo se calcula el costo de varias unidades de un servicio?", "Multiplicando el precio unitario por la cantidad", "El total depende de cuántas unidades se piden."),
        ("¿Qué haces si un servicio no está en la ficha?", "Consulto a la jefatura", "Así no se entrega un dato inventado."),
        ("¿El servicio incluido en la tarifa se cobra aparte?", "No", "Está incluido en la tarifa que ya se paga."),
    ],
    op=("Servicios de ejemplo de otro hotel: late check-out hasta las 15:00 por $10.000; lavado a $1.200 por prenda; traslado al aeropuerto a $20.000 por viaje (hasta 3 personas); estacionamiento a $5.000 por noche; desayuno incluido. "
        "Un grupo de 5 personas pide: late check-out, lavado de 6 prendas, 2 noches de estacionamiento y traslado al aeropuerto. "
        "Calcula cuánto debe pagar el grupo por los servicios adicionales y escribe en dos o tres frases cómo se lo informarías con claridad, mencionando qué está incluido.",
        "Traslado: 5 personas necesitan 2 viajes, 2 × 20.000 = 40.000. Lavado: 6 × 1.200 = 7.200. Estacionamiento: 2 × 5.000 = 10.000. Late check-out: 10.000. Total: 67.200 pesos. Frase: «El desayuno está incluido. Adicionalmente: late check-out hasta las 15:00, lavado de 6 prendas, 2 noches de estacionamiento y dos viajes de traslado, en total $67.200».",
        ["calcula el número de viajes con el tope", "suma bien los cuatro servicios", "informa lo incluido y lo adicional con claridad"],
        ["hoja con cálculos, total y frase"],
        ["cobrar solo un viaje de traslado", "cobrar el desayuno", "no aclarar qué está incluido"],
        "Pregunta: «¿cuántos viajes hacen falta para 5 personas con tope de 3?». Si responde 1, repasa el tope del traslado."),
    reinforce="Escribe una ficha inventada de cuatro servicios de un hotel, con precios, y calcula el total de un pedido de tres de ellos.",
    extend="Explica por qué informar el total de los cobros antes de usar un servicio protege al huésped y al hotel.",
)

# ============================================================ OAE-01, clase 5
F = ("Ficha 5 (pauta de calidad de atención, de ejemplo; total 10 puntos). Saludo cordial: 2 puntos. Escucha y confirma lo pedido: 2 puntos. Información correcta y completa: 3 puntos. Respeta la privacidad: 2 puntos. Despedida cordial: 1 punto. "
     "Atención A: saludó, no escuchó bien, dio información correcta, respetó la privacidad y se despidió. Atención B: saludó, escuchó y confirmó, dio información incompleta, respetó la privacidad y no se despidió. "
     "Encuesta de ejemplo del mes: 40 huéspedes respondieron y 34 se declararon satisfechos.")
build(
    O1, 5, F,
    use="Aprenderé a comparar dos atenciones con una pauta, calcular su puntaje y leer una encuesta de satisfacción para proponer mejoras.",
    prior=["Sé sumar puntajes.", "Sé calcular un porcentaje simple.", "Conozco los estándares de atención."],
    explain=[
        "Para verificar la calidad de una atención se usa una pauta: una lista de criterios con puntaje. Se marca cada criterio como cumplido o no cumplido, se suman los puntos de los cumplidos y se compara con el puntaje total. Así se evita opinar solo por impresión y se puede decir en qué criterio hay que mejorar.",
        "Una encuesta de satisfacción es una pregunta que se hace a los huéspedes para saber si quedaron conformes. El porcentaje de satisfechos se calcula con los satisfechos multiplicados por 100 y divididos por el total de respuestas. Con los resultados se proponen mejoras, como repasar la escucha activa.",
        "Al comparar dos atenciones, no se juzga a la persona: se revisa lo que hizo en cada criterio y se propone cómo mejorar. La retroalimentación se da en privado, con respeto, y destaca primero lo que estuvo bien." + LIM,
    ],
    vocab=[("pauta", "lista de criterios con puntaje para evaluar una atención"), ("criterio", "aspecto que se revisa en la pauta"), ("puntaje total", "suma máxima de puntos de la pauta"), ("encuesta de satisfacción", "preguntas a los huéspedes para saber si quedaron conformes"), ("retroalimentación", "comentario que ayuda a mejorar, basado en lo observado")],
    worked=[
        ("Calcular un puntaje", "En una pauta de ejemplo de 10 puntos, una atención cumple criterios de 2, 3 y 1 punto. ¿Cuál es su puntaje?", ["Se suman los puntos de los criterios cumplidos.", "2 + 3 + 1 = 6."], "6 de 10 puntos"),
        ("Calcular un porcentaje de satisfacción", "En otra encuesta de ejemplo, 18 de 20 huéspedes dijeron estar satisfechos. ¿Qué porcentaje es?", ["Se multiplican los satisfechos por 100 y se dividen por el total.", "18 × 100 ÷ 20 = 90."], "90 %"),
    ],
    mistakes=[("Decir «la atención B fue mala» sin indicar qué criterios no cumplió.", "Es una opinión sin evidencia que no ayuda a mejorar.", "Indica los criterios incumplidos y qué se puede hacer en cada uno."),
              ("Dar retroalimentación a una compañera frente a los huéspedes.", "La expone y no respeta su dignidad.", "Hazlo en privado, con respeto y empezando por lo que estuvo bien.")],
    T=[
        ("abc", "En Hotelería: ¿para qué sirve una pauta de calidad de atención?", "Para evaluar la atención con criterios y puntajes claros", "Para fijar los precios del hotel", "Para decidir quién trabaja los fines de semana", "La pauta ordena los criterios y evita juzgar solo por impresión."),
        ("abc", "{F} ¿Cuántos puntos vale «información correcta y completa»?", "3 puntos", "2 puntos", "1 punto", "La ficha asigna 3 puntos a ese criterio, el de mayor valor."),
        ("=", "{F} ¿Cuántos puntos obtiene la atención A?", "2+3+2+1", "Se suman los criterios cumplidos: saludo, información, privacidad y despedida.", " puntos"),
        ("=", "{F} ¿Cuántos puntos obtiene la atención B?", "2+2+2", "Se suman saludo, escucha y privacidad, que son los criterios cumplidos.", " puntos"),
        ("abc", "{F} ¿Qué atención obtuvo mayor puntaje?", "La A, con 8 puntos", "La B, con 6 puntos", "Ambas, con el mismo puntaje", "A suma 8 y B suma 6, así que A tiene el mayor puntaje."),
        ("abc", "{F} ¿Qué criterio principal no cumplió la atención A?", "La escucha y confirmación de lo pedido", "El saludo cordial", "La privacidad", "La ficha dice que A no escuchó bien; el saludo y la privacidad sí los cumplió."),
        ("=", "{F} ¿Qué porcentaje de los huéspedes encuestados se declaró satisfecho?", "34*100//40", "Se multiplican los satisfechos por 100 y se dividen por el total.", " %"),
        ("=", "{F} ¿Cuántos de los 40 encuestados no se declararon satisfechos?", "40-34", "Al total de respuestas se le restan los satisfechos.", " huéspedes"),
        ("abc", "{F} ¿Qué mejora propondrías para la atención B?", "Dar toda la información y despedirse cordialmente", "Saludar con más energía, porque fue lo que le faltó", "Dar solo la información que el huésped no pidió, para ahorrar tiempo","B perdió puntos en información completa y despedida, que son lo que debe mejorar."),
        ("abc", "{F} Una jefa da retroalimentación al practicante de A en el pasillo, frente a huéspedes. ¿Qué observación corresponde?", "Debe hacerse en privado y con respeto, empezando por lo que estuvo bien", "Está bien, porque todos aprenden", "Debe hacerse solo por escrito y sin hablar", "La retroalimentación en público expone a la persona; en privado se cuida su dignidad."),
        ("abc", "{F} Un compañero dice: «La atención A fue buena porque me cayó bien el recepcionista». ¿Qué corrección corresponde?", "Se evalúa con la pauta y no por simpatía", "Tiene razón, la simpatía basta", "La pauta no sirve para evaluar", "La pauta ofrece criterios observables y evita sesgos personales."),
        ("abc", "{F} Una encuesta indica que varios huéspedes insatisfechos mencionaron «no me escucharon». ¿Qué capacitación proponer?", "Repasar la escucha activa y el parafraseo", "Repasar el cálculo de impuestos", "Repasar el orden de las bodegas", "El problema señalado es la escucha, que se mejora con escucha activa y parafraseo."),
        ("=", "{F} Si el mes siguiente 38 de 40 se declaran satisfechos, ¿cuántos puntos porcentuales sube respecto de los 34 actuales?", "38*100//40-34*100//40", "Se calcula cada porcentaje y se resta el actual al nuevo.", " puntos porcentuales"),
    ],
    ctx=("abc", "{F} Eres jefe o jefa de turno y debes decidir cuál de los dos recepcionistas, A o B, recibirá primero una capacitación. ¿Cuál es el criterio más justo?", "Usar la pauta y las evidencias de ambos, y capacitar según los criterios en que cada uno tuvo menor puntaje", "Capacitar a quien menos te simpatiza", "Capacitar al que tenga más años en el hotel, sin mirar la pauta", "Una decisión basada en evidencias de la pauta es más justa que una basada en preferencias."),
    sc=[
        ("En Hotelería: ¿cómo se obtiene el puntaje de una atención con una pauta?", "Sumando los puntos de los criterios cumplidos", "Cada criterio cumplido aporta su puntaje."),
        ("¿Cómo se calcula el porcentaje de satisfechos?", "Satisfechos por 100, dividido por el total", "Es la parte respecto del total, expresada sobre 100."),
        ("¿Dónde se da retroalimentación a un compañero?", "En privado, con respeto", "Así se cuida su dignidad y su confianza."),
    ],
    op=("Pauta de ejemplo (8 puntos): saludo, 1; escucha y confirma, 2; información correcta, 3; despedida, 2. Atención C: saludó, escuchó y confirmó, dio información correcta, no se despidió. Atención D: no saludó, escuchó y confirmó, dio información correcta, se despidió. "
        "Calcula el puntaje de C y de D, di cuál obtuvo más y escribe una retroalimentación respetuosa para cada una de las dos personas (una frase por persona).",
        "C: 1 + 2 + 3 = 6. D: 2 + 3 + 2 = 7. D obtuvo más puntos. Retroalimentación para C: «Escuchaste muy bien y diste información correcta; recuerda despedirte con una frase cordial». Para D: «Tu información y escucha fueron claras; recuerda saludar al inicio».",
        ["calcula bien los dos puntajes", "compara con claridad", "da retroalimentación respetuosa con algo positivo y algo por mejorar"],
        ["hoja con puntajes y dos frases de retroalimentación"],
        ["sumar criterios que no se cumplieron", "criticar a la persona en vez de la conducta", "no mencionar nada positivo"],
        "Pregunta: «¿qué criterio perdió cada persona?». Si no puede nombrarlo, vuelve a leer la ficha del caso."),
    reinforce="Inventa una pauta de 4 criterios con puntajes y evalúa una atención imaginaria.",
    extend="Explica por qué una encuesta de satisfacción debe leerse junto con una pauta y no sola.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 6 (zona turística de ejemplo, inventada). «Bahía Ejemplo»: Playa Las Gaviotas de Ejemplo (atractivo natural, entrada libre); Museo del Puerto de Ejemplo (atractivo cultural, abierto de martes a domingo, cerrado los lunes); "
     "Reserva Costera de Ejemplo (área protegida, solo con guía autorizado, prohibido sacar plantas, animales o piedras, y se debe llevar la basura de vuelta). Un aviso oficial de ejemplo informa que el sendero norte está cerrado por marejada.")
build(
    O2, 1, F,
    use="Aprenderé qué es un atractivo turístico, qué reglas generales de conservación existen y cómo orientar a un turista con información confiable y actualizada.",
    prior=["Sé leer una ficha de una zona.", "Sé qué es un lugar protegido.", "Conozco las reglas de trato respetuoso."],
    explain=[
        "Un atractivo turístico es un lugar, objeto o actividad que interesa a los turistas. Puede ser natural (una playa o un bosque), cultural (un museo o una feria artesanal), histórico (un edificio antiguo) o un evento programado. Orientar al turista es indicarle qué puede visitar, cómo llegar, a qué hora y bajo qué reglas.",
        "Muchos atractivos, sobre todo los naturales, tienen normativa de conservación: reglas para protegerlos, como no sacar plantas ni animales, no dejar basura y entrar solo con guía autorizado en las áreas protegidas. Quien orienta explica estas reglas con respeto y remite a la norma vigente y a la administración del lugar. No inventa ni cambia reglas.",
        "La información debe ser vigente y de una fuente oficial. Si hay un aviso de cierre o de riesgo, como una marejada, se informa de inmediato y se sugiere consultar a la autoridad competente. Sobre salud o seguridad, no se dan consejos personales: se remite al personal capacitado o a la autoridad." + LIM,
    ],
    vocab=[("atractivo turístico", "lugar, objeto o actividad que interesa a los turistas"), ("área protegida", "territorio cuyo cuidado está regulado para conservar su naturaleza"), ("normativa de conservación", "reglas para proteger un atractivo"), ("aviso oficial", "información entregada por una autoridad, como un cierre de sendero"), ("fuente oficial", "origen de datos que corresponde a la autoridad o a la administración del lugar")],
    worked=[
        ("Clasificar un atractivo", "Un museo de ejemplo con objetos del puerto, ¿qué tipo de atractivo es?", ["Un museo guarda y muestra objetos de la cultura de un lugar.", "No es un paisaje natural."], "Un atractivo cultural"),
        ("Respetar un cierre", "Un aviso oficial de ejemplo dice que un sendero está cerrado por mal clima. Una turista quiere ir igual. ¿Qué se le informa?", ["El cierre es una disposición de la autoridad.", "Se le sugiere otro atractivo y consultar los avisos."], "Que no puede ir por el cierre y que se le ofrece una alternativa"),
    ],
    mistakes=[("Decir a un turista que puede llevarse una piedra de una reserva «porque es solo una piedra».", "En las áreas protegidas está prohibido sacar piedras, plantas o animales, aunque parezca poco.", "Explica la regla de conservación y ofrece una forma de recordar el lugar, como una foto."),
              ("Informar un horario de memoria sin revisar si cambió.", "Los horarios y cierres cambian y el turista puede perder su visita.", "Revisa la fuente oficial vigente antes de informar.")],
    T=[
        ("abc", "En Turismo: ¿qué es un atractivo turístico?", "Un lugar, objeto o actividad que interesa a los turistas", "Un impuesto que pagan los turistas", "El horario de salida del hotel", "Un atractivo es lo que motiva la visita; el impuesto y el horario no lo son."),
        ("abc", "{F} ¿Qué tipo de atractivo es la Playa Las Gaviotas de Ejemplo?", "Un atractivo natural", "Un atractivo cultural", "Un evento programado", "Una playa es un paisaje natural, no una construcción cultural."),
        ("abc", "{F} ¿Qué día está cerrado el museo?", "Los lunes", "Los domingos", "Los martes", "La ficha dice que está abierto de martes a domingo y cerrado los lunes."),
        ("abc", "{F} ¿Cómo se puede ingresar a la Reserva Costera de Ejemplo?", "Solo con guía autorizado", "Solo en la noche", "Sin ninguna regla", "La ficha fija la entrada con guía autorizado en esa área protegida."),
        ("abc", "{F} Una turista quiere llevarse a casa unas piedras de la reserva como recuerdo. ¿Qué corresponde informar?", "Que está prohibido sacar piedras de la reserva y sugerir una foto como recuerdo", "Que puede llevarse unas pocas si nadie la ve", "Que puede llevarse todas las que quepa en el bolso", "La ficha prohíbe sacar plantas, animales o piedras; ofrecer una alternativa ayuda."),
        ("abc", "{F} Un turista pregunta si puede caminar por el sendero norte hoy. ¿Qué respondes?", "Que el sendero norte está cerrado por marejada según el aviso oficial", "Que sí, porque el mar se ve tranquilo", "Que depende de lo que le parezca", "Un cierre oficial manda sobre la impresión personal; se informa lo que dice el aviso."),
        ("abc", "{F} Un grupo pregunta qué hacer con la basura que genera en la reserva. ¿Qué respondes?", "Que debe llevarla de vuelta al salir", "Que puede dejarla bajo un arbusto", "Que puede enterrarla en la arena", "La ficha indica llevar la basura de vuelta."),
        ("=", "{F} Un grupo visita el museo de martes a domingo. ¿Cuántos días a la semana puede visitarlo?", "7-1", "A los siete días de la semana se resta el día de cierre.", " días"),
        ("abc", "Un turista tiene dolor de pecho mientras conversa contigo en la recepción. ¿Qué haces?", "Avisar de inmediato a personal capacitado o a los servicios de emergencia", "Darle una infusión que te parece útil", "Decirle que descanse y esperar", "Ante un malestar importante se avisa a personal capacitado; no se dan consejos propios."),
        ("abc", "Un turista pregunta cuántos años tiene un edificio antiguo y no tienes el dato exacto. ¿Qué respondes?", "Que lo consultarás en una fuente oficial para darle un dato correcto", "Un año cualquiera, que suene creíble", "Que ese edificio no existe", "Si el dato no está seguro, se busca en una fuente confiable; inventar daña la confianza."),
        ("abc", "{F} Una pareja pregunta qué hacer en un día con sendero norte cerrado. ¿Qué es mejor ofrecer?", "Visitar la playa o el museo, que están abiertos, según los horarios de la ficha", "Ir de todas formas al sendero norte", "Quedarse en el hotel sin sugerencias", "Se ofrece una alternativa vigente que cumple lo que buscan."),
        ("abc", "Un turista dice que le molesta que le pregunten de dónde viene, porque se siente observado. ¿Qué haces?", "Respetar su privacidad y ofrecer solo la información que necesita", "Insistir en preguntar, porque es parte de conocerlo", "Contarle a otros turistas de dónde cree que viene", "Respetar la privacidad es parte del buen trato; no se insiste ni se comentan datos."),
        ("=", "{F} El museo atiende de martes a domingo y abre de 10:00 a 17:00 cada día de apertura. ¿Cuántas horas atiende en la semana?", "(7-1)*(17-10)", "Se multiplican los días de apertura por las horas diarias de atención.", " horas"),
    ],
    ctx=("abc", "{F} Una familia de ejemplo llega el lunes y pregunta qué puede visitar hoy. ¿Qué le informas?", "Que el museo está cerrado los lunes, que la playa es de entrada libre y que el sendero norte está cerrado", "Que todo está abierto, porque es turismo", "Que no hay nada que hacer en Bahía Ejemplo", "Se informa cada atractivo con su estado vigente, aprovechando los datos de la ficha."),
    sc=[
        ("En Turismo: ¿qué tipo de atractivo es un museo?", "Un atractivo cultural", "Guarda y muestra elementos de la cultura de un lugar."),
        ("¿Qué haces si hay un aviso oficial de cierre de un sendero?", "Informo el cierre y ofrezco una alternativa", "La autoridad manda sobre la impresión personal."),
        ("¿Qué haces ante un malestar importante de un turista?", "Aviso a personal capacitado o a emergencias", "No se dan consejos personales sobre salud."),
    ],
    op=("Zona de ejemplo «Valle Ejemplo»: Cascada de Ejemplo (natural, entrada libre, prohibido dejar basura), Pueblo Artesanal de Ejemplo (cultural, feria el sábado y el domingo), Iglesia Antigua de Ejemplo (histórico, abierta de lunes a viernes). Un aviso oficial de ejemplo dice que el camino a la cascada está cerrado hoy por un derrumbe. "
        "Un turista llega el sábado y quiere conocer «lo más importante». Escribe: el tipo de cada atractivo, qué le informarías hoy (con el aviso), una regla de conservación, y qué fuente oficial recomendarías consultar.",
        "Tipos: cascada, natural; pueblo, cultural; iglesia, histórico. Hoy sábado: el camino a la cascada está cerrado por el aviso; la feria del pueblo está abierta; la iglesia no abre sábado. Regla: no dejar basura en la cascada. Fuente: la oficina de información turística oficial o la administración del lugar.",
        ["clasifica los tres atractivos", "usa el aviso oficial y los horarios para informar", "nombra una regla de conservación y una fuente oficial"],
        ["hoja con clasificación, información del día y fuente"],
        ["recomendar la cascada a pesar del aviso", "decir que la iglesia está abierta el sábado", "no mencionar fuente"],
        "Pregunta: «¿por qué no recomiendas la cascada hoy?». Si no menciona el aviso oficial, repasa la regla de respetar los cierres."),
    reinforce="Inventa una zona turística con tres atractivos de tipos distintos y escribe una regla de conservación para cada uno.",
    extend="Explica por qué respetar las normas de conservación beneficia a los turistas y a las comunidades locales.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 7 (atractivos de Bahía Ejemplo, de ejemplo). Playa Las Gaviotas de Ejemplo: natural, entrada libre, a 2 km del hotel, abierta todo el día. Museo del Puerto de Ejemplo: cultural, entrada $3.000, a 5 km del hotel, de 10:00 a 17:00, cerrado los lunes. "
     "Reserva Costera de Ejemplo: natural, entrada $6.000 con guía, a 12 km del hotel, de 09:00 a 16:00. Mercado Artesanal de Ejemplo: cultural, entrada libre, a 3 km del hotel, de 10:00 a 19:00. Menores de 6 años no pagan entrada en el museo ni en la reserva.")
build(
    O2, 2, F,
    use="Aprenderé a seleccionar la información relevante (histórica, cultural, geográfica, económica y de contingencia) y a leer una ficha de atractivos para orientar a un turista.",
    prior=["Conozco los tipos de atractivos.", "Sé calcular costos de entradas.", "Sé leer horarios y distancias."],
    explain=[
        "Al orientar a un turista, la información relevante depende de lo que pide. La información geográfica dice dónde queda el atractivo y a qué distancia; la histórica y la cultural explican su origen y su significado; la económica indica precios y si hay descuentos; y la de contingencia informa lo que cambia hoy, como un cierre, un evento o el clima. Los requerimientos sanitarios y las disposiciones legales se informan de forma general y remitiendo a la fuente oficial.",
        "Se selecciona la información que el turista necesita: si va con niños, importan los horarios y los descuentos; si tiene movilidad reducida, importan los accesos. No se abruma con todos los datos. Un folleto es un documento breve con datos básicos del atractivo, y la oficina de información turística es una fuente oficial de datos actualizados.",
        "Siempre se verifica la fecha de la información, se respeta el protocolo del lugar y, si hay dudas, se consulta antes de informar. No se difunden datos personales del turista ni se hacen comentarios discriminatorios sobre su origen o sus gustos." + LIM,
    ],
    vocab=[("información geográfica", "dónde está el atractivo y a qué distancia queda"), ("información económica", "precios, descuentos y formas de pago"), ("información de contingencia", "lo que cambia hoy, como un cierre o un evento"), ("folleto", "documento breve con datos básicos de un atractivo"), ("oficina de información turística", "lugar oficial donde se entregan datos actualizados a los turistas")],
    worked=[
        ("Calcular una entrada", "Una entrada de ejemplo cuesta $4.000 por persona y viaja una familia de 3 que paga entrada completa. ¿Cuánto pagan?", ["Se multiplica el precio por el número de personas.", "4.000 × 3 = 12.000."], "$12.000"),
        ("Elegir la información relevante", "Una turista dice que viaja con un bebé y quiere saber qué hacer mañana. ¿Qué datos priorizas?", ["Importan horarios cómodos y accesos fáciles.", "No todos los datos del museo son necesarios."], "Horarios, accesos y descuentos para menores"),
    ],
    mistakes=[("Dar al turista todos los datos de todos los atractivos sin saber qué busca.", "Lo confunde y no le sirve para decidir.", "Pregunta qué busca y selecciona la información relevante."),
              ("Usar un folleto sin fecha para informar precios.", "Los precios pueden haber cambiado y el turista pagaría otra cantidad.", "Verifica la fecha del folleto o consulta la fuente oficial.")],
    T=[
        ("abc", "En Turismo: ¿qué es la información de contingencia?", "Lo que cambia hoy, como un cierre o un evento", "El origen histórico del atractivo", "El precio normal de la entrada", "La contingencia es lo que ocurre ahora y puede afectar la visita."),
        ("abc", "{F} ¿A qué distancia del hotel queda el museo?", "5 km", "2 km", "12 km", "La ficha indica 5 km; 2 km es la playa y 12 km es la reserva."),
        ("abc", "{F} ¿Cuál es el atractivo de entrada libre y más cercano al hotel?", "La Playa Las Gaviotas", "El Mercado Artesanal", "La Reserva Costera", "La playa está a 2 km y el mercado a 3 km; ambos son libres, pero la playa es la más cercana."),
        ("=", "{F} Dos adultos visitan el museo. ¿Cuánto pagan en total?", "3000*2", "Se multiplica el precio de la entrada por el número de personas.", " pesos"),
        ("=", "{F} Una familia de 2 adultos y un niño de 4 años visita la reserva. ¿Cuánto paga, si el menor no paga?", "6000*2", "Se cobran solo los dos adultos; el menor de 6 años no paga.", " pesos"),
        ("abc", "{F} Un turista pregunta a qué hora cierra el mercado. ¿Qué respondes?", "A las 19:00", "A las 17:00", "A las 16:00", "La ficha fija el cierre del mercado a las 19:00; 17:00 es el museo y 16:00 la reserva."),
        ("abc", "{F} Una pareja quiere ir a la reserva a las 16:30. ¿Qué respondes?", "Que no es posible, porque la reserva cierra a las 16:00", "Que sí, porque abre todo el día", "Que puede ir y entrar sin guía", "La ficha indica que la reserva atiende de 09:00 a 16:00."),
        ("abc", "{F} Un turista en silla de ruedas pregunta por los accesos del museo, que no están en la ficha. ¿Qué haces?", "Decirle que consultarás la información de accesibilidad en la fuente oficial", "Inventar que tiene rampas", "Decirle que no podrá entrar", "Si el dato no está, se consulta; no se supone ni se inventa."),
        ("abc", "{F} Hoy es lunes. ¿Qué atractivo no puede visitar un turista?", "El museo", "La playa", "El mercado", "El museo está cerrado los lunes según la ficha."),
        ("=", "{F} Dos adultos y un niño de 8 años visitan el museo y la reserva (los menores de 6 años no pagan; el niño de 8 sí paga). ¿Cuánto pagan en total por las entradas de los tres a ambos lugares?", "(3000+6000)*3", "El niño de 8 años paga como los adultos: se suman las dos entradas y se multiplica por las tres personas.", " pesos"),
        ("=", "{F} Un grupo va a la playa y vuelve al hotel, y luego va al mercado y vuelve al hotel. ¿Cuántos km recorre en total entre ida y vuelta de los dos viajes?", "2*2+3*2", "Cada viaje separado es de ida y vuelta, así que se duplica cada distancia.", " km"),
        ("abc", "{F} Un turista comenta que viene de un país lejano y pregunta si tendrá problemas por su origen. ¿Qué respondes?", "Que será tratado con el mismo respeto que cualquier turista", "Que algunos locales son menos amables con extranjeros", "Que mejor no salga del hotel", "El buen trato y la no discriminación son parte del servicio."),
        ("abc", "{F} Un grupo pregunta por las disposiciones legales para entrar a la reserva. ¿Cómo respondes?", "Informo las reglas generales de la ficha y remito a la administración y a la norma vigente", "Invento un artículo de ley para sonar seguro", "Digo que no hay ninguna regla", "Sin datos exactos, se remite a la fuente oficial; nunca se inventan normas."),
    ],
    ctx=("abc", "{F} Un turista de ejemplo dice: «Tengo solo 4 horas libres y poco dinero. ¿Qué me recomiendas?». ¿Qué respuesta usa mejor la información?", "La playa y el mercado, que son de entrada libre y cercanos, con sus horarios", "Solo la reserva, que es la más lejana y costosa", "Que se quede en el hotel", "Se ajusta la información al tiempo y al dinero del turista con los datos de la ficha."),
    sc=[
        ("En Turismo: ¿qué dice la información económica?", "Precios, descuentos y formas de pago", "Es la información sobre el costo de la visita."),
        ("¿Qué haces si no tienes un dato del atractivo?", "Lo consulto en una fuente oficial", "Inventar un dato puede perjudicar al turista."),
        ("¿Qué información priorizas si el turista viaja con niños?", "Horarios, descuentos y accesos", "Se adapta la información a lo que él necesita."),
    ],
    op=("Ficha de ejemplo de otro lugar: Laguna de Ejemplo (natural, entrada $2.500, de 09:00 a 18:00, a 4 km), Casa Histórica de Ejemplo (histórica, entrada $1.500, de 10:00 a 16:00, a 1 km) y Feria de Ejemplo (cultural, entrada libre, sábado y domingo, a 2 km). Menores de 8 años no pagan. "
        "Una familia de 2 adultos y 2 niños de 5 y 10 años pide un plan para el sábado. Calcula el costo de visitar la laguna y la casa histórica, y escribe qué información relevante les darías (geográfica, económica y de contingencia).",
        "Laguna: 2 adultos y el niño de 10 años pagan 3 × 2.500 = 7.500 (el de 5 no paga). Casa: 3 × 1.500 = 4.500. Total: 12.000. Información: geográfica, laguna a 4 km y casa a 1 km; económica, el niño de 5 no paga; contingencia, el sábado también está la feria de entrada libre, a 2 km.",
        ["calcula bien con el descuento por edad", "selecciona información relevante de varios tipos", "no inventa datos"],
        ["hoja con cálculos y información seleccionada"],
        ["cobrar a los dos niños", "dar datos que no están en la ficha", "olvidar la información de contingencia"],
        "Pregunta: «¿cuántas personas pagan?». Si responde 4, repasa el descuento por edad."),
    reinforce="Escribe en una tabla tres atractivos inventados con su tipo, distancia, horario y precio.",
    extend="Explica por qué la oficina de información turística es una fuente más confiable que un comentario escuchado en la calle.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 8 (caso de ejemplo, inventado). Tres grupos de turistas piden orientación en «Bahía Ejemplo» un sábado. Grupo 1: pareja joven, le gusta caminar, tiene todo el día. "
     "Grupo 2: tres adultos mayores, uno usa bastón, quieren algo tranquilo y cercano, con asientos. Grupo 3: familia con niños de 3 y 7 años, tiene la tarde libre, quiere algo educativo. "
     "Datos de ejemplo: la playa tiene acceso con pasarela plana y bancas; el sendero norte está cerrado por marejada; el museo tiene ascensor y salas con asientos; la reserva solo ofrece caminatas de dos horas con guía.")
build(
    O2, 3, F,
    use="Aprenderé a analizar un caso con varios turistas y a decidir qué atractivos y qué información ofrecer a cada grupo, según sus necesidades y las condiciones del día.",
    prior=["Sé seleccionar información relevante.", "Sé leer una ficha de atractivos.", "Respeto las normas de conservación."],
    explain=[
        "Analizar un caso es leer qué necesita cada grupo, revisar qué ofrece cada atractivo y decidir cuál calza mejor. La accesibilidad es la facilidad con que una persona puede llegar y usar un lugar, con rampas, ascensores, asientos o pasarelas planas. Ofrecer algo inaccesible a quien lo necesita no es una buena orientación.",
        "Se compara cada atractivo con los criterios del grupo: edad, intereses, tiempo disponible, movilidad y presupuesto. Si un atractivo no calza o está cerrado, no se ofrece, se explica por qué y se propone otro. La decisión se comunica con claridad, y el turista siempre puede elegir otra cosa.",
        "No se asume nada por la edad o apariencia: se pregunta. Y no se prometen cosas sin verificar, como la disponibilidad de un guía o un asiento." + LIM,
    ],
    vocab=[("accesibilidad", "facilidad con que una persona puede llegar y usar un lugar"), ("movilidad reducida", "dificultad para desplazarse que puede requerir bastón, silla de ruedas u otra ayuda"), ("calza", "se ajusta bien a lo que la persona necesita"), ("presupuesto", "dinero que el turista planea gastar"), ("alternativa", "otra opción que puede elegirse")],
    worked=[
        ("Elegir por tiempo", "Un grupo de ejemplo tiene solo 1 hora libre y una caminata dura 2 horas. ¿Calza?", ["La caminata dura más que el tiempo del grupo.", "Se debe ofrecer algo más corto."], "No calza; se ofrece algo más corto"),
        ("Revisar accesibilidad", "Una persona de ejemplo usa silla de ruedas. Un sendero tiene escalones y una pasarela plana va a la playa. ¿Qué se ofrece?", ["El sendero con escalones no es accesible.", "La pasarela plana sí lo es."], "La playa con pasarela plana"),
    ],
    mistakes=[("Recomendar el sendero cerrado al grupo que le gusta caminar «porque es lo que buscan».", "Un cierre oficial por riesgo manda sobre el gusto; ofrecerlo expone al grupo.", "Explica el cierre y ofrece otra caminata abierta."),
              ("Decidir por los adultos mayores sin preguntarles qué prefieren.", "Es suponer lo que quieren por su edad.", "Presenta opciones adecuadas y deja que ellos elijan.")],
    T=[
        ("abc", "En Turismo: ¿qué es la accesibilidad de un atractivo?", "La facilidad con que una persona puede llegar y usarlo", "El precio de la entrada", "La cantidad de turistas que lo visitan", "La accesibilidad se refiere al acceso y uso por todas las personas, no al precio."),
        ("abc", "{F} ¿Qué atractivo no se puede ofrecer hoy a ningún grupo?", "El sendero norte", "El museo", "La playa", "El sendero norte está cerrado por marejada según la ficha."),
        ("abc", "{F} ¿Qué atractivo calza mejor con los adultos mayores, uno con bastón?", "La playa con pasarela plana y bancas", "La reserva con caminata de dos horas", "El sendero norte", "La pasarela plana y las bancas facilitan el desplazamiento y el descanso."),
        ("abc", "{F} ¿Qué atractivo calza mejor con la familia que busca algo educativo?", "El museo", "El sendero norte", "La caminata de dos horas", "El museo es un atractivo cultural educativo y cuenta con ascensor."),
        ("abc", "{F} ¿Por qué la caminata de dos horas es difícil para la familia con un niño de 3 años?", "Es larga para un niño tan pequeño", "Porque la familia no tiene tarde libre", "Porque el sendero norte está abierto", "Una caminata larga cansa a un niño de 3 años; la familia tiene la tarde libre."),
        ("=", "{F} La caminata de la reserva dura 2 horas y la familia tiene 4 horas libres en la tarde. ¿Cuántos minutos libres les sobrarían si hicieran solo la caminata?", "(4-2)*60", "Se restan las horas ocupadas a las libres y se pasan a minutos.", " minutos"),
        ("abc", "{F} Una pareja joven, que quiere caminar, pregunta por el sendero norte. ¿Qué respondes?", "Que está cerrado por marejada, y ofrecer otra caminata abierta, como la de la reserva con guía", "Que vaya igual, porque son jóvenes", "Que no hay ninguna caminata disponible", "El cierre es por riesgo; la reserva con guía es una alternativa abierta."),
        ("abc", "{F} Uno de los adultos mayores dice que se siente cansado durante la visita. ¿Qué haces?", "Ofrecerle sentarse y llamar a personal capacitado si se siente mal", "Decirle que se aguante", "Darle un remedio que llevas contigo", "Se ofrece descanso y, ante malestar, se llama a personal capacitado; no se medica."),
        ("=", "{F} La reserva cobra $6.000 por persona (precio de ejemplo). Si la pareja joven va con dos amigos más, ¿cuánto pagan entre los 4?", "6000*4", "Se multiplica el precio por el número de personas.", " pesos"),
        ("abc", "{F} Un compañero propone: «A los adultos mayores solo ofrezcámosles la playa, porque seguro no quieren más». ¿Qué observación corresponde?", "Hay que presentar las opciones adecuadas y dejar que ellos elijan", "Tiene razón, la edad define los gustos", "Hay que ofrecerles la caminata más larga", "No se supone lo que quieren; se informan opciones adecuadas y se respeta su decisión."),
        ("abc", "{F} Una turista de otro país pregunta cuánto cuesta el museo y no hay precio en la ficha. ¿Qué haces?", "Decirle que consultarás la tarifa vigente y avisarle luego", "Decirle un precio que recuerdes de otro museo", "Decirle que es gratis", "Sin dato en la ficha, se consulta y se informa con seguridad."),
        ("abc", "{F} La familia quiere hacer fotos a otros turistas en el museo. ¿Qué les recuerdas?", "Pedir permiso a las personas y respetar las reglas del museo sobre fotos", "Que pueden hacerlo sin pedir permiso", "Que está prohibido tener cámaras en todo el país", "La privacidad exige consentimiento, y cada lugar tiene sus propias reglas."),
        ("abc", "{F} Una pareja de adultos mayores pide que le cuentes de dónde son los otros dos grupos. ¿Qué haces?", "Decirles que no entregas datos de otros turistas", "Contar todo lo que sabes", "Inventar un origen", "Los datos de otras personas son confidenciales."),
    ],
    ctx=("abc", "{F} Hay un solo guía disponible y los tres grupos piden la caminata con guía. ¿Qué haces?", "Explicar la limitación, proponer horarios distintos o alternativas, y no prometer lo que no se puede", "Prometer guía a todos al mismo tiempo", "Elegir a un grupo sin explicar", "Se informa con honestidad y se ofrecen alternativas; no se promete sin verificar."),
    sc=[
        ("En Turismo: ¿qué se compara con los criterios del turista?", "Cada atractivo", "Así se elige el que mejor calza."),
        ("¿Qué haces si un atractivo está cerrado por riesgo?", "No lo ofrezco, explico y propongo otro", "El cierre oficial por riesgo siempre se respeta."),
        ("¿Qué haces ante un malestar de un turista?", "Avisar a personal capacitado", "No se dan consejos de salud."),
    ],
    op=("Caso de ejemplo. Tres grupos piden orientación un domingo en un lugar inventado. Grupo A: dos adultos, uno usa silla de ruedas, tienen la mañana libre. Grupo B: cuatro jóvenes de 17 a 19 años que quieren aventura y tienen el día libre. Grupo C: una familia con una bebé, que quiere algo tranquilo. "
        "Atractivos: Mirador con rampa (acceso plano, 30 minutos), Cabalgata de ejemplo (2 horas, solo con guía autorizado y personas mayores de 12 años), Parque con juegos y sombra (acceso plano). "
        "Escribe qué atractivo ofrecerías a cada grupo con una razón, y una regla de seguridad o de trato que aplicarías.",
        "A: Mirador con rampa, por accesibilidad. B: Cabalgata, por aventura y porque cumplen la edad mínima, con guía autorizado. C: Parque con juegos y sombra, por ser tranquilo y apto para una bebé. Regla: la cabalgata solo se realiza con guía autorizado; en el trato, se pregunta a cada grupo sin suponer.",
        ["elige un atractivo coherente para cada grupo", "da razones con datos de la ficha", "incluye una regla de seguridad o de trato"],
        ["hoja con tres asignaciones y una regla"],
        ["ofrecer la cabalgata al grupo con silla de ruedas", "olvidar el guía autorizado", "dar razones sin datos"],
        "Pregunta: «¿por qué no ofrecerías la cabalgata a C?». Debe mencionar la edad mínima o el carácter tranquilo."),
    reinforce="Describe en tres líneas un grupo de turistas inventado y elige para él un atractivo de una lista que armes.",
    extend="Explica por qué ofrecer una alternativa es mejor que decir solo «no se puede».",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 9 (itinerario de ejemplo, inventado, de un día). Salida del hotel: 09:00. Traslado al museo: 20 minutos. Visita al museo: 90 minutos. Traslado a la playa: 15 minutos. Almuerzo en la playa: 60 minutos. Visita a la playa: 120 minutos. Regreso al hotel: 25 minutos. "
     "Entradas de ejemplo: museo $3.000 por adulto, playa gratis; menores de 6 años no pagan. Museo abierto hasta las 17:00 (última entrada a las 16:00). Grupo: 3 adultos y 1 niño de 4 años.")
build(
    O2, 4, F,
    use="Aprenderé a armar un itinerario con tiempos y costos de ejemplo y a comprobar que cumple los horarios y las necesidades del grupo.",
    prior=["Sé sumar horas y minutos.", "Sé calcular costos de entradas.", "Conozco horarios y descuentos."],
    explain=[
        "Un itinerario es el plan ordenado de un recorrido, con actividades, horarios, tiempos de traslado y costos. Para armarlo se parte de la hora de salida y se suman en orden los minutos de cada traslado y cada visita. Así se obtiene la hora de llegada y de término de cada actividad.",
        "Se comprueba que cada visita ocurra dentro del horario del atractivo, que haya tiempo para comer y descansar, y que el costo sea el que el turista puede pagar. Para pasar horas a minutos se multiplica por 60. Los menores que no pagan entrada se descuentan del total.",
        "Todo itinerario debe tener un margen de tiempo por si algo se atrasa, y debe informar la hora de regreso. En la práctica, los horarios y cierres se confirman con la fuente oficial el mismo día." + LIM,
    ],
    vocab=[("itinerario", "plan ordenado de un recorrido con actividades, horarios y costos"), ("traslado", "movimiento de un lugar a otro"), ("margen de tiempo", "tiempo extra que se deja por si algo se atrasa"), ("última entrada", "hora máxima a la que se permite ingresar a un atractivo"), ("costo total", "suma de todos los gastos del itinerario")],
    worked=[
        ("Sumar tiempos", "Un recorrido de ejemplo: traslado de 30 minutos, visita de 60 minutos y regreso de 30 minutos. ¿Cuánto dura en total?", ["Se suman todos los tramos.", "30 + 60 + 30 = 120."], "120 minutos"),
        ("Calcular la hora de término", "Un grupo de ejemplo parte a las 10:00 y su recorrido dura 150 minutos. ¿A qué hora termina?", ["150 minutos son 2 horas y 30 minutos.", "10:00 + 2:30 = 12:30."], "12:30"),
    ],
    mistakes=[("Olvidar sumar el tiempo de traslado entre dos visitas.", "Las horas de término quedan mal calculadas y el grupo llega tarde.", "Suma todos los tramos, también los traslados."),
              ("Cobrar entrada a un niño pequeño que no paga.", "Sube el costo y es un dato incorrecto para el turista.", "Revisa las reglas de descuento antes de calcular el total.")],
    T=[
        ("abc", "En Turismo: ¿qué es un itinerario?", "El plan ordenado de un recorrido con actividades, horarios y costos", "La lista de precios de un hotel", "El reglamento de una reserva", "Un itinerario ordena actividades y tiempos; la lista de precios o el reglamento no lo hacen."),
        ("abc", "{F} ¿A qué hora sale el grupo del hotel?", "A las 09:00", "A las 10:00", "A las 11:30", "La ficha fija la salida a las 09:00."),
        ("=", "{F} ¿Cuántos minutos suman el traslado al museo y la visita al museo?", "20+90", "Se suman los minutos del traslado y de la visita.", " minutos"),
        ("=", "{F} ¿Cuánto pagan en el museo los 3 adultos?", "3000*3", "Se multiplica la entrada por el número de adultos; el niño no paga.", " pesos"),
        ("abc", "{F} Si el grupo sale a las 09:00 y llega al museo tras 20 minutos, ¿a qué hora llega?", "A las 09:20", "A las 09:00", "A las 10:20", "A las 09:00 se suman 20 minutos y resulta 09:20."),
        ("abc", "{F} Si la visita al museo comienza a las 09:20 y dura 90 minutos, ¿a qué hora termina?", "A las 10:50", "A las 10:20", "A las 11:20", "90 minutos son 1 hora y 30 minutos; 09:20 más 1:30 es 10:50."),
        ("=", "{F} ¿Cuántos minutos dura todo el itinerario desde la salida hasta el regreso al hotel?", "20+90+15+60+120+25", "Se suman los traslados, las visitas y el almuerzo en orden.", " minutos"),
        ("abc", "{F} Si todo el itinerario dura 330 minutos y el grupo sale a las 09:00, ¿a qué hora regresa al hotel?", "A las 14:30", "A las 15:00", "A las 13:30", "330 minutos son 5 horas y 30 minutos; 09:00 más 5:30 es 14:30."),
        ("abc", "{F} Un compañero propone ir primero a la playa y llegar al museo a las 16:30. ¿Qué problema tiene?", "La última entrada es a las 16:00 y no podrían ingresar", "Ninguno, porque el museo abre todo el día", "Que la playa cuesta más que el museo", "La última entrada al museo es a las 16:00 según la ficha."),
        ("abc", "{F} El grupo agrega un 4.º adulto en lugar del niño. ¿Cuánto cambia el costo del museo?", "Sube $3.000, porque un adulto paga entrada y el niño no", "No cambia", "Baja $3.000", "Un adulto adicional paga $3.000 y el niño pequeño no pagaba."),
        ("=", "{F} Si cada tramo de traslado (hotel–museo, museo–playa y playa–hotel) cuesta $8.000 por todo el grupo, ¿cuánto pagan por los 3 tramos?", "8000*3", "Se multiplica el costo por el número de tramos.", " pesos"),
        ("abc", "{F} El grupo quiere dejar 30 minutos de margen. ¿Qué cambio es más razonable?", "Acortar la visita a la playa de 120 a 90 minutos", "Quitar el almuerzo de 60 minutos", "Eliminar el traslado a la playa", "Acortar una visita libera tiempo sin dejar al grupo sin comer ni sin traslado."),
        ("=", "{F} Si la visita a la playa se acorta a 90 minutos, ¿cuántos minutos dura el itinerario completo?", "20+90+15+60+90+25", "Se suman todos los tramos con la visita ya acortada.", " minutos"),
    ],
    ctx=("abc", "{F} El día del itinerario el museo cierra por una actividad privada. ¿Qué hace quien orienta?", "Informar el cierre, ofrecer cambiar el orden o reemplazar el museo por otro atractivo abierto, y recalcular tiempos y costos", "Mantener el plan y decir al grupo que llegue igual", "Cancelar el itinerario sin dar alternativa", "Un cambio de contingencia exige recalcular y ofrecer una alternativa."),
    sc=[
        ("En Turismo: ¿cómo se calcula la duración de un itinerario?", "Sumando todos los tramos", "Hay que incluir traslados, visitas y almuerzo."),
        ("¿Qué pasa con la entrada de un niño de 4 años en el museo de la ficha?", "No paga", "La ficha libera a los menores de 6 años."),
        ("¿Para qué se deja un margen de tiempo?", "Por si algo se atrasa", "Así el grupo no llega tarde."),
    ],
    op=("Itinerario de ejemplo: salida a las 10:00; traslado al parque, 25 minutos; visita al parque, 100 minutos; almuerzo, 50 minutos; traslado al mirador, 15 minutos; visita al mirador, 40 minutos; regreso al hotel, 30 minutos. Entrada al parque: $2.500 por persona; mirador gratis. Van 4 adultos. El mirador cierra a las 16:00. "
        "Calcula la duración total, la hora de regreso al hotel, el costo de entradas, y si el grupo llega al mirador antes de que cierre.",
        "Duración: 25 + 100 + 50 + 15 + 40 + 30 = 260 minutos, 4 horas y 20 minutos. Regreso: 14:20. Entradas: 4 × 2.500 = 10.000. Llegan al mirador a las 10:00 + 25 + 100 + 50 + 15 = 190 minutos, o sea 13:10, antes de las 16:00.",
        ["suma bien todos los tramos", "calcula bien la hora de regreso y el costo", "verifica el horario del mirador"],
        ["hoja con los cuatro cálculos"],
        ["olvidar el almuerzo", "no pasar minutos a horas", "no verificar el cierre"],
        "Pregunta: «¿cuántos minutos son 4 horas y 20?». Si no responde 260, repasa la conversión."),
    reinforce="Arma un itinerario de tres actividades con horarios y calcula a qué hora termina.",
    extend="Explica por qué conviene confirmar los horarios el mismo día del recorrido.",
)

# ============================================================ OAE-02, clase 5
F = ("Ficha 10 (dos circuitos de ejemplo, inventados). Circuito 1: Mirador del Faro de Ejemplo y Pueblo de Ejemplo, 5 horas, $9.000 por persona, camino de tierra con escalones, información actualizada hace 2 años. "
     "Circuito 2: Parque Costero de Ejemplo y Museo del Mar de Ejemplo, 4 horas, $12.000 por persona, acceso plano con pasarela, información actualizada la semana pasada. Aviso oficial de ejemplo: la ruta al parque está abierta; el faro cierra por mantención este mes. "
     "Turista: pareja de adultos, uno con movilidad reducida, presupuesto máximo $26.000 en total, 4 horas libres.")
build(
    O2, 5, F,
    use="Aprenderé a comparar dos circuitos con los requisitos del turista, verificar la vigencia de la información y recomendar con criterio.",
    prior=["Sé calcular costos por persona.", "Sé comparar opciones con requisitos.", "Conozco información de contingencia."],
    explain=[
        "Comparar alternativas es contrastar cada opción con los requisitos del turista: tiempo, presupuesto, accesibilidad e intereses. Una opción que incumple un requisito se descarta aunque sea atractiva. Si más de una cumple, se explican las diferencias y el turista elige.",
        "Verificar la calidad de la información es revisar que sea vigente y de una fuente oficial. Un dato con fecha antigua o contradicho por un aviso oficial no sirve. También se revisa que los cálculos sean correctos y que se haya informado lo importante: costo total, duración y accesibilidad.",
        "Al terminar, se resume la recomendación con una razón y se anota qué fuente se usó y su fecha, para que otra persona del equipo pueda comprobarla. El turista siempre decide: tú orientas, no impones." + LIM,
    ],
    vocab=[("requisito", "condición que la opción elegida debe cumplir"), ("vigente", "que sigue siendo válida hoy"), ("fuente oficial", "origen de datos que corresponde a la autoridad o administración"), ("recomendación", "consejo fundamentado sobre qué opción conviene"), ("fecha de actualización", "día en que se revisó por última vez un dato")],
    worked=[
        ("Descartar por un requisito", "Un turista de ejemplo tiene 3 horas libres y un circuito dura 5. ¿Cumple?", ["Se compara la duración con el tiempo disponible.", "5 es mayor que 3."], "No cumple y se descarta"),
        ("Comparar costos", "Dos personas viajan en un circuito de ejemplo de $7.000 por persona. ¿Cuánto cuesta el circuito para ambas?", ["Se multiplica por las personas.", "7.000 × 2 = 14.000."], "$14.000"),
    ],
    mistakes=[("Recomendar el circuito más barato sin mirar si cumple la accesibilidad.", "Un requisito incumplido descarta la opción, por barata que sea.", "Primero verifica todos los requisitos y después compara costos."),
              ("Usar un dato de hace dos años como si fuera actual.", "Puede haber cambiado, y un aviso oficial reciente puede contradecirlo.", "Prefiere la fuente vigente y verifica los avisos oficiales.")],
    T=[
        ("abc", "En Turismo: ¿qué significa que un dato sea vigente?", "Que sigue siendo válido hoy", "Que es el más antiguo", "Que lo dijo un turista", "Un dato vigente se confirma actual; la antigüedad o el rumor no garantizan validez."),
        ("abc", "{F} ¿Qué circuito dura más?", "El circuito 1, con 5 horas", "El circuito 2, con 4 horas", "Duran lo mismo", "La ficha indica 5 horas para el circuito 1 y 4 para el 2."),
        ("=", "{F} ¿Cuánto cuesta el circuito 1 para la pareja?", "9000*2", "Se multiplica el precio por persona por las dos personas.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta el circuito 2 para la pareja?", "12000*2", "Se multiplica el precio por persona por las dos personas.", " pesos"),
        ("abc", "{F} ¿Qué circuito cumple el tiempo de la pareja?", "El circuito 2, de 4 horas", "El circuito 1, de 5 horas", "Ambos cumplen", "La pareja tiene 4 horas libres; el circuito 1 dura 5."),
        ("abc", "{F} ¿Qué circuito cumple la accesibilidad para la persona con movilidad reducida?", "El circuito 2, con acceso plano y pasarela", "El circuito 1, con escalones", "Ninguno", "El circuito 1 tiene escalones y camino de tierra; el 2, acceso plano."),
        ("abc", "{F} ¿Qué circuito cumple el presupuesto máximo de $26.000?", "Ambos cumplen el presupuesto", "Solo el circuito 1", "Ninguno", "Los costos son 18.000 y 24.000 pesos, ambos menores que 26.000."),
        ("abc", "{F} ¿Por qué el circuito 1 es poco confiable por su información?", "Su información tiene 2 años y el faro cierra este mes por mantención", "Porque cuesta menos", "Porque tiene un pueblo", "La fecha antigua y el aviso oficial contradicen su vigencia."),
        ("abc", "{F} ¿Qué circuito se recomienda a la pareja?", "El circuito 2", "El circuito 1", "Ninguno, porque cuesta mucho", "Cumple tiempo, accesibilidad y presupuesto, y su información está actualizada."),
        ("=", "{F} Con el circuito 2, ¿cuánto queda del presupuesto máximo de $26.000?", "26000-12000*2", "Al presupuesto se le resta el costo total del circuito para dos personas.", " pesos"),
        ("abc", "{F} El turista pregunta si el parque tiene baños accesibles y no hay dato. ¿Qué haces?", "Decirle que consultarás con la administración antes de recomendar", "Decirle que sí para que no se preocupe", "Decirle que no hay baños", "Si falta información importante, se consulta antes de recomendar."),
        ("abc", "{F} Un compañero dice: «Recomendémosle el circuito 1 porque es más barato». ¿Qué corresponde?", "Recordar que el circuito 1 incumple el tiempo, la accesibilidad y la vigencia", "Aceptarlo, porque el costo es lo único importante", "Cambiar el presupuesto de la pareja", "Una opción más barata que incumple requisitos se descarta."),
        ("abc", "{F} ¿Qué anotarías en el registro al terminar?", "La recomendación, la fuente oficial usada y su fecha", "Solo el nombre de la pareja", "Los datos de salud de la persona con movilidad reducida", "Registrar fuente y fecha permite verificar; los datos de salud no se anotan sin necesidad."),
    ],
    ctx=("abc", "{F} Mientras la pareja decide, llega un aviso oficial de ejemplo: el parque cierra mañana por un evento. La pareja había planificado ir mañana. ¿Qué haces?", "Informar el cierre de inmediato, ofrecer ir hoy si es posible o cambiar de circuito, y recalcular", "No avisar para no complicarles el plan", "Decirles que vayan igual y vean si pueden entrar", "Un aviso oficial se comunica de inmediato y se ofrece una alternativa verificada."),
    sc=[
        ("En Turismo: ¿qué se hace con una opción que incumple un requisito?", "Se descarta", "Por atractiva que sea, no cumple lo que el turista necesita."),
        ("¿Qué se revisa de la información antes de recomendar?", "Que sea vigente y de una fuente oficial", "Un dato antiguo o dudoso puede ser falso hoy."),
        ("¿Quién decide qué circuito toma el turista?", "El turista", "Quien orienta informa pero no impone."),
    ],
    op=("Dos opciones de ejemplo para una familia de 3 personas (un adulto, una persona de 70 años con bastón y un niño de 9 años), con $30.000 en total y 3 horas libres. Opción X: Parque de Ejemplo, 2 horas, $8.000 por persona, acceso plano, información de la semana pasada. "
        "Opción Y: Cerro de Ejemplo, 4 horas, $5.000 por persona, subida con escalones, información de hace 3 años. "
        "Calcula el costo de cada opción, revisa los requisitos (tiempo, presupuesto, accesibilidad, vigencia) y escribe tu recomendación con una razón y qué fuente oficial consultarías.",
        "X: 3 × 8.000 = 24.000, 2 horas, acceso plano, información vigente: cumple todo. Y: 3 × 5.000 = 15.000, pero dura 4 horas (más que 3) y tiene escalones para la persona con bastón, con información de hace 3 años: se descarta. Recomiendo X. Consultaría la administración del parque o la oficina de información turística oficial.",
        ["calcula ambos costos", "verifica los cuatro requisitos con razones", "recomienda con razón y nombra una fuente oficial"],
        ["tabla con requisitos, cumple o no, y recomendación"],
        ["elegir Y por precio", "olvidar la accesibilidad o la vigencia", "no nombrar fuente oficial"],
        "Pregunta: «¿por qué Y no sirve aunque es más barato?». Si no menciona tiempo y escalones, repasa la verificación de requisitos."),
    reinforce="Escribe tres requisitos de un turista inventado y compáralos con dos circuitos que armes.",
    extend="Explica por qué anotar la fuente y su fecha ayuda al equipo a comprobar una recomendación.",
)

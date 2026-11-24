"""Lengua y Literatura EPJA Media Nivel 1, módulo 2 (parte 4): OAD-08, escribir un texto no literario (carta al director) para comunicar una postura de forma coherente y cohesionada. Todos los textos son inventados y se leen en papel."""
from __future__ import annotations

from epja_leli_nm1_b_common import build

O = "EPJA-LELI-NM1-OAD-08"

F1 = ("Carta (inventada) al director del diario «El Eco del Valle» (nombre de ejemplo), fechada el 12 de noviembre: «Señor director: Le escribo para pedir que se repongan las luminarias del pasaje Las Rosas (lugar de ejemplo). "
      "Desde hace tres semanas, dos de los cuatro focos del pasaje están apagados. Por eso, de noche, las personas mayores y quienes vuelven de un turno tardío caminan casi a oscuras. "
      "Además, reponer dos focos cuesta poco en comparación con el riesgo de una caída. Por lo tanto, solicito a la municipalidad una revisión durante esta semana. Atentamente, Marta Soto (nombre de ejemplo), vecina del pasaje.»")

F2 = ("Tema (inventado): ¿la feria del barrio debe abrir también los domingos? "
      "Postura de Raúl: «La feria debe abrir los domingos». "
      "Argumento 1: muchas personas trabajan de lunes a sábado y solo pueden comprar el domingo. "
      "Argumento 2: en el barrio hay 120 puestos y los domingos quedarían abiertos 80 (dato de ejemplo). "
      "Argumento 3: el color de los toldos es verde. "
      "Contraargumento posible: algunos puesteros necesitan descansar el domingo.")

F3 = ("Párrafo A (inventado), con fallas: «La plaza está sucia. La plaza tiene basureros rotos. La plaza no tiene luz. Hay que arreglar la plaza y la plaza será más segura.» "
      "Párrafo B (inventado), corregido: «La plaza está sucia porque los basureros están rotos. Además, no tiene luz de noche. Por eso, conviene arreglar los basureros y reponer los focos; así, será más limpia y más segura.»")

F4 = ("Plan de carta (inventado): Tema: el paradero de la avenida no tiene techo. Postura: la municipalidad debe instalar un techo. Argumentos: 1) en invierno las personas esperan bajo la lluvia hasta 20 minutos; 2) hay muchas personas mayores y trabajadoras que lo usan cada día; 3) un techo se instala en pocos días. Cierre: pedir una respuesta esta semana. "
      "Frases desordenadas de una carta: (a) «Por eso, solicito instalar un techo en el paradero.» (b) «Señor director:» (c) «El paradero de la avenida no tiene techo y en invierno las personas esperan bajo la lluvia.» "
      "(d) «Atentamente, Luis Reyes (nombre de ejemplo), usuario del paradero.» (e) «Además, lo usan cada día muchas personas mayores y trabajadoras.»")

F5 = ("Situación A (inventada): en la esquina de calle Los Pinos se acumula basura desde hace dos semanas; el camión pasa los martes y viernes; hay un vecino con un niño que enfermó (no se asocia con certeza). "
      "Situación B (inventada): en el consultorio de ejemplo, para pedir hora se hace fila desde las 6:00 y a las 8:00 ya no quedan cupos; atienden desde las 9:00. "
      "Situación C (inventada): el bus 12 de ejemplo pasa cada 40 minutos desde hace un mes; antes pasaba cada 15 minutos; muchas personas llegan tarde a su turno.")

F6 = ("Borrador (inventado) de carta: «Director: ¡YA BASTA, el municipio no hace nada! Todos son unos inútiles. La calle está mala. Además, la calle está mala porque está mala. Sin embargo, la calle es bonita. Chao.»")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy reconozco la carta al director como un texto para dar a conocer una postura y descubro sus partes.",
    prior=["Reconozco emisor, receptor y propósito.", "He leído cartas o avisos formales.", "Sé distinguir hechos de opiniones."],
    explain=[
        "La carta al director es un texto que una persona envía a un diario o a una institución para opinar, reclamar o proponer algo sobre un tema de interés común. Quien la escribe expresa una postura, es decir, lo que piensa sobre un asunto, y la apoya con razones.",
        "Una carta tiene partes reconocibles: fecha, saludo («Señor director:»), presentación del tema, la postura con sus argumentos, una petición o cierre y la despedida con nombre. El tono es respetuoso, aunque la persona esté molesta.",
        "Tú ya sabes dar tu opinión en una conversación. La carta pide organizarla: decir el tema, la postura, las razones con datos y qué se solicita. Si no hay datos, la carta pierde fuerza. Importante: nunca escribas datos personales reales en una carta que vayas a compartir.",
    ],
    vocab=[("carta al director", "texto en que una persona expresa una postura sobre un tema a un diario o institución"), ("postura", "lo que alguien piensa sobre un tema"), ("argumento", "razón que apoya una postura"), ("petición", "lo que se solicita a quien lee")],
    worked=[
        ("Reconocer la postura", "Frase (inventada): «Es necesario reponer los focos del pasaje».", ["Veo una necesidad que se afirma: reponer focos.", "Es una opinión con una propuesta."], "Es la postura de quien escribe"),
        ("Reconocer un argumento", "Frase (inventada): «Dos de los cuatro focos están apagados hace tres semanas».", ["Es un dato que se puede comprobar.", "Apoya la postura de que hay que reponer."], "Es un argumento con dato"),
    ],
    mistakes=[("Escribir solo quejas sin proponer ni pedir nada.", "Una carta sin petición no da una salida clara a quien la lee.", "Termina diciendo qué se solicita y a quién."),
              ("Usar un tono agresivo para ser escuchado.", "Un tono insultante resta credibilidad y puede impedir que publiquen la carta.", "Escribe con firmeza pero con respeto.")],
    T=[
        ("abc", "{F} ¿Quién es el receptor de la carta?", "El director del diario «El Eco del Valle» y sus lectores", "La municipalidad solamente", "Los vecinos del pasaje", "La carta se dirige a él con el saludo «Señor director»."),
        ("ab", "{F} ¿Cuál es el tema de la carta?", "La falta de luminarias en el pasaje Las Rosas", "La limpieza de la plaza", "La carta pide reponer focos apagados."),
        ("{F} ¿Cuántos focos de los cuatro están apagados? Escribe solo el número.", "2", "El texto dice que dos de los cuatro focos están apagados."),
        ("abc", "{F} ¿Cuál es la postura de la carta?", "Que se repongan las luminarias del pasaje", "Que el diario publique más noticias", "Que los vecinos pinten el pasaje", "La carta pide expresamente reponer las luminarias del pasaje."),
        ("abc", "{F} ¿Cuál es un argumento con dato de la carta?", "«Desde hace tres semanas, dos de los cuatro focos están apagados»", "«Atentamente»", "«Señor director»", "Es un hecho que apoya la postura."),
        ("ab", "{F} ¿Qué petición hace la carta?", "Una revisión de la municipalidad durante esta semana", "Una celebración en el pasaje", "La petición aparece en la frase «solicito a la municipalidad una revisión»."),
        ("abc", "{F} ¿Qué parte de la carta es «Atentamente, Marta Soto, vecina del pasaje»?", "La despedida con el nombre", "El saludo inicial", "La postura", "Cierra la carta e identifica a quien escribe."),
        ("ab", "{F} ¿El tono de la carta es respetuoso o agresivo?", "Respetuoso, porque usa «le escribo» y «solicito»", "Agresivo, porque pide una revisión", "Las palabras elegidas son formales y corteses."),
        ("abc", "{F} ¿Qué recurso de persuasión usa la frase «las personas mayores caminan casi a oscuras»?", "Apelar al bien de personas vulnerables", "Una cifra exacta", "Un chiste", "Muestra el riesgo para quienes más lo sufren."),
        ("abc", "¿Cuál de estas frases sería una buena postura para una carta?", "«La municipalidad debe instalar un techo en el paradero»", "«Hola, qué tal»", "«El paradero es de color azul»", "Expresa una opinión con una propuesta."),
        ("ab", "Una persona escribe: «Todo está mal y nadie hace nada». ¿Qué le falta a su carta?", "Un tema concreto, argumentos con datos y una petición", "Más signos de exclamación", "Sin tema ni petición, la carta no puede lograr su propósito."),
        ("abc", "{F} Si la carta no tuviera fecha, ¿qué dificultad habría?", "Sería difícil saber si el problema sigue vigente", "No podría tener postura", "No tendría saludo", "La fecha permite saber cuándo se escribió."),
        ("ab", "{F} ¿Por qué una carta al director debe incluir argumentos y no solo la postura?", "Porque las razones permiten que otras personas entiendan y evalúen la postura", "Porque las cartas largas se publican más", "Sin razones, la postura queda como una opinión sin respaldo."),
    ],
    ctx=("abc", "Tu comunidad quiere pedir al diario local que informe sobre el cierre de una calle. ¿Cuál es el mejor comienzo de la carta?", "«Señor director: Le escribo para solicitar que informe sobre el cierre de calle Los Sauces, que afecta al transporte»", "«Estoy furioso»", "«Chao»", "Presenta saludo, tema y propósito con tono respetuoso."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué es una carta al director?", "Un texto para expresar una postura sobre un tema a un diario o institución", "La carta se escribe para opinar, reclamar o proponer."),
        ("En Lengua y Literatura de EPJA: ¿qué es una postura?", "Lo que alguien piensa sobre un tema", "La postura es la opinión que se defiende."),
        ("En Lengua y Literatura de EPJA: ¿para qué sirve la petición final de una carta?", "Para decir qué se solicita y a quién", "Da una salida clara a quien lee.")],
    op=("Analiza la carta de ejemplo: {F} Escribe en tu cuaderno las partes de la carta con una cita para cada una: saludo, tema, postura, dos argumentos, petición y despedida. Luego escribe en dos líneas cuál es la parte que más te convence y por qué.",
        "Saludo: «Señor director». Tema: luminarias del pasaje. Postura: «se repongan las luminarias». Argumentos: dos focos apagados hace tres semanas; personas mayores caminan casi a oscuras. Petición: «una revisión durante esta semana». Despedida: «Atentamente, Marta Soto». Me convence el dato de los focos porque se puede comprobar.",
        ["identifica las partes con cita", "reconoce dos argumentos", "explica con razones qué parte le convence"],
        ["siete citas y dos líneas"],
        ["no citar el texto", "no explicar su elección"],
        "Pregunta: «¿Qué parte de la carta se puede comprobar?»."),
    reinforce="Lee una carta o un reclamo de ejemplo y marca su tema, su postura y su petición.",
    extend="Escribe en dos líneas una postura sobre un tema de tu barrio y una petición concreta para quien debería actuar.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo a formular una postura clara y a elegir argumentos que la apoyen, incluidos datos y un contraargumento.",
    prior=["Reconozco postura, argumentos y petición en una carta.", "Distingo datos de opiniones.", "Sé reconocer si una razón apoya o no una idea."],
    explain=[
        "Una postura clara se dice en una sola oración y se puede defender: «La feria debe abrir también los domingos». No es una postura decir «la feria es un tema», porque eso no toma partido.",
        "Los argumentos son las razones que apoyan la postura. Los mejores son relevantes, es decir, se relacionan con el tema, y comprobables, porque traen datos o ejemplos. Un argumento irrelevante, como el color de los toldos, no apoya la postura aunque sea cierto.",
        "El contraargumento es la razón de quien piensa distinto. Mencionarlo y responderlo da fuerza a tu carta, porque muestra que consideraste otros puntos de vista. Por ejemplo: «Entendemos que algunos puesteros necesitan descansar; por eso se podría rotar el turno».",
    ],
    vocab=[("tesis", "idea central que se defiende, igual a la postura"), ("argumento relevante", "razón que se relaciona con el tema y apoya la postura"), ("contraargumento", "razón de quien piensa distinto"), ("dato", "información precisa y comprobable")],
    worked=[
        ("Elegir argumentos relevantes", "Postura (inventada): «La biblioteca debe abrir los sábados». Razón A: muchas personas trabajan de lunes a viernes. Razón B: el edificio es de ladrillo.", ["Pregunto si cada razón apoya la postura.", "A explica por qué el sábado ayudaría; B no se relaciona."], "Razón A es relevante; razón B no lo es"),
        ("Responder un contraargumento", "Contraargumento (inventado): «Abrir cuesta más». Respuesta propuesta: «El costo se cubriría con turnos rotativos».", ["Reconozco la razón del otro.", "Propongo una salida concreta."], "Se responde con respeto y una propuesta"),
    ],
    mistakes=[("Poner argumentos que no se relacionan con la postura.", "Un dato verdadero pero irrelevante no apoya lo que se defiende.", "Pregunta: ¿esto ayuda a que alguien acepte mi postura?"),
              ("Ignorar a quien piensa distinto.", "Ignorar el otro punto de vista hace la carta más débil.", "Menciona el contraargumento y respóndelo con respeto.")],
    T=[
        ("abc", "{F} ¿Cuál es la postura de Raúl?", "La feria debe abrir los domingos", "La feria debe cerrar los lunes", "La feria no debe cambiar de lugar", "Está dicha en una oración que toma partido."),
        ("ab", "{F} ¿Cuál es un argumento relevante de Raúl?", "Muchas personas trabajan de lunes a sábado y solo pueden comprar el domingo", "Los toldos son verdes", "Explica por qué abrir el domingo sirve a quienes trabajan."),
        ("{F} ¿Cuántos puestos dice el Argumento 2 que quedarían abiertos los domingos? Escribe solo el número.", "80", "El texto dice 80 de los 120 puestos."),
        ("abc", "{F} ¿Qué argumento NO apoya la postura de Raúl?", "El Argumento 3, sobre el color de los toldos", "El Argumento 1, sobre quienes trabajan", "El Argumento 2, sobre los puestos abiertos", "El color no se relaciona con el horario."),
        ("=", "{F} Si 80 de los 120 puestos abren el domingo, ¿cuántos puestos no abrirían?", "120 - 80", "Se resta los puestos abiertos del total.", " puestos"),
        ("abc", "{F} ¿Cuál es el contraargumento posible del texto?", "Algunos puesteros necesitan descansar el domingo", "La feria tiene 120 puestos", "Los toldos son verdes", "Es la razón de quien piensa distinto."),
        ("ab", "{F} ¿Cuál es una respuesta respetuosa al contraargumento?", "Se podrían organizar turnos para que cada puestero descanse un domingo", "Quien no quiera trabajar, que se vaya", "Responde reconociendo la razón y proponiendo una salida."),
        ("abc", "¿Cuál es una postura clara?", "«El consultorio debe ampliar su horario de atención»", "«El consultorio es un lugar»", "«Hay muchas opiniones»", "Toma partido sobre una propuesta concreta."),
        ("abc", "¿Cuál es un argumento con dato?", "«Más de 30 personas esperan desde las 6:00 para pedir hora»", "«Todo el mundo lo sabe»", "«Es una vergüenza»", "Un número y una hora pueden comprobarse."),
        ("ab", "Rosa dice: «Un argumento verdadero siempre sirve». ¿Qué conviene responder?", "No: también debe relacionarse con el tema", "Sí: si es verdadero, ayuda", "Un dato verdadero pero ajeno al tema no apoya la postura."),
        ("abc", "{F} ¿Cuál argumento es más comprobable?", "El de los puestos: 80 de 120 abrirían", "El del color de los toldos", "Nadie puede dudarlo", "Una cifra concreta permite revisarlo y comprobarlo."),
        ("abc", "{F} ¿Qué haría más fuerte la carta de Raúl?", "Agregar el contraargumento y su respuesta", "Quitar todos los argumentos", "Usar mayúsculas en todo el texto", "Mostrar que consideró otros puntos de vista da más credibilidad."),
        ("ab", "{F} ¿Cuántos argumentos relevantes tiene el texto?", "Dos, el 1 y el 2", "Tres, porque todos hablan de la feria", "El tercero habla de los toldos y no apoya la postura."),
    ],
    ctx=("abc", "Quieres escribir al diario para pedir que el bus 12 pase cada 15 minutos. ¿Cuál de estos es el mejor argumento?", "«Desde hace un mes pasa cada 40 minutos y muchas personas llegan tarde a su turno»", "«El bus es de color rojo»", "«A mí no me gusta esperar»", "Es comprobable y se relaciona con la petición."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué es un argumento relevante?", "Una razón que se relaciona con el tema y apoya la postura", "Debe apoyar lo que se defiende."),
        ("En Lengua y Literatura de EPJA: ¿qué es un contraargumento?", "La razón de quien piensa distinto", "Considerarlo fortalece la carta y muestra respeto."),
        ("En Lengua y Literatura de EPJA: ¿qué tiene de bueno un dato en un argumento?", "Que se puede comprobar", "El dato da respaldo a la razón.")],
    op=("Planifica argumentos para esta postura de ejemplo: «El consultorio debe ampliar su horario de atención». En tu cuaderno escribe dos argumentos relevantes con un dato de ejemplo cada uno, un contraargumento y su respuesta. Usa estas ideas del texto: {F} como modelo para organizar tus ideas.",
        "Argumento 1: a las 8:00 ya no quedan cupos y muchas personas trabajan desde temprano (dato de ejemplo: fila desde las 6:00). Argumento 2: personas mayores esperan de pie por mucho tiempo. Contraargumento: el personal tiene turnos fijos. Respuesta: se podría reorganizar un turno para ampliar la atención dos tardes a la semana.",
        ["dos argumentos relevantes con dato", "un contraargumento", "una respuesta respetuosa"],
        ["cuatro frases"],
        ["argumentos que no apoyan la postura", "ignorar el contraargumento"],
        "Pregunta: «¿Esta razón apoya tu postura?»."),
    reinforce="Escribe una postura sobre un tema de tu trabajo y subraya dos razones que la apoyen.",
    extend="Escribe un contraargumento para la postura «el casino debe tener menú vegetariano» y respóndelo.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy aprendo a lograr que mis ideas tengan coherencia y a unirlas con cohesión, usando conectores y referentes.",
    prior=["Tengo una postura y argumentos.", "Distingo ideas principales de ideas de apoyo.", "Sé leer un párrafo y decir de qué trata."],
    explain=[
        "Un texto es coherente cuando sus ideas se relacionan con una idea central, no se contradicen y siguen un orden que se entiende. Es cohesionado cuando las oraciones se unen con recursos de lenguaje que permiten leer de corrido.",
        "Algunos recursos de cohesión son los conectores y los referentes. Los conectores unen ideas: «porque» (causa), «por eso» (consecuencia), «además» (suma), «sin embargo» (contraste) y «para» (finalidad). Los referentes evitan repetir palabras: en lugar de decir «la plaza» cuatro veces, usas «ella», «esta» o «el lugar».",
        "La puntuación también cohesiona: la coma separa partes de una frase y el punto ordena las ideas. Un párrafo con la misma palabra repetida y sin conectores suena entrecortado. Un buen párrafo lleva una idea central y avanza paso a paso.",
    ],
    vocab=[("coherencia", "relación lógica de las ideas con una idea central"), ("cohesión", "unión de las oraciones con recursos del lenguaje"), ("conector", "palabra que une ideas y muestra su relación"), ("referente", "palabra que reemplaza a otra ya mencionada para no repetirla")],
    worked=[
        ("Elegir un conector", "Frases (inventadas): «El paradero no tiene techo. Las personas se mojan». ¿Qué conector las une como causa y consecuencia?", ["La segunda frase es consecuencia de la primera.", "El conector de consecuencia es «por eso»."], "«El paradero no tiene techo; por eso las personas se mojan»"),
        ("Evitar la repetición", "Frase (inventada): «La plaza es bonita y la plaza está limpia».", ["Repite «la plaza».", "Se reemplaza la segunda mención por «además, está limpia»."], "«La plaza es bonita y, además, está limpia»"),
    ],
    mistakes=[("Poner muchos conectores sin relación entre las ideas.", "El conector debe mostrar una relación real entre las ideas.", "Pregunta qué relación hay: causa, suma, contraste, consecuencia o finalidad."),
              ("Repetir la misma palabra en cada oración.", "La repetición vuelve el texto pesado y poco cohesionado.", "Usa referentes: «esta», «ese lugar», «allí».")],
    T=[
        ("abc", "{F} ¿Qué falla tiene el Párrafo A?", "Repite «la plaza» muchas veces y no usa conectores", "Es demasiado corto", "No tiene ideas", "La repetición y la falta de conectores cortan el texto."),
        ("ab", "{F} ¿Qué conector usa el Párrafo B para indicar causa?", "«porque»", "«además»", "«La plaza está sucia porque los basureros están rotos» explica la causa."),
        ("{F} ¿Qué palabra repite el Párrafo A al comienzo de sus tres primeras oraciones? Escribe solo la palabra.", "plaza", "El Párrafo A empieza tres veces con «La plaza»."),
        ("abc", "{F} ¿Qué conector del Párrafo B suma una idea?", "«Además»", "«Porque»", "«Por eso»", "El conector «además» agrega otra razón a la anterior."),
        ("abc", "{F} ¿Qué conector del Párrafo B indica consecuencia?", "«Por eso»", "«Además»", "«Porque»", "Introduce lo que se deduce de lo anterior."),
        ("ab", "{F} ¿Qué frase del Párrafo B usa «así» para indicar finalidad o resultado?", "«así, será más limpia y más segura»", "«La plaza está sucia»", "«Así» presenta el resultado esperado de arreglar."),
        ("abc", "¿Qué conector falta? «Quiero que el bus pase más seguido, ___ llego tarde a mi turno.»", "porque", "además", "sin embargo", "Indica la causa de la petición."),
        ("abc", "¿Qué conector falta? «El camión pasa los martes. ___ a veces no pasa.»", "Sin embargo", "Además", "Por eso", "Marca contraste entre lo que debería ocurrir y lo que ocurre."),
        ("ab", "Reemplaza la repetición: «El consultorio atiende desde las 9:00. El consultorio cierra a las 17:00». ¿Qué opción evita repetir?", "«El consultorio atiende desde las 9:00 y cierra a las 17:00»", "«El consultorio atiende desde las 9:00. El consultorio cierra a las 17:00»", "La segunda parte se une con «y» y no repite el sujeto."),
        ("abc", "Un párrafo defiende reponer focos y de pronto habla de los toldos de la feria. ¿Qué falla?", "La coherencia, porque cambia de tema", "La ortografía", "El saludo", "Una idea ajena rompe la relación con la idea central."),
        ("abc", "¿Qué referente reemplaza a «los vecinos» en «Los vecinos pidieron ayuda. ___ esperan respuesta»?", "Ellos", "Aquel", "Nosotros", "«Ellos» alude a los vecinos mencionados."),
        ("ab", "Pedro escribe: «El techo se rompió. Por eso, el techo es de lata». ¿Qué falla tiene el conector?", "No hay relación de consecuencia entre las dos ideas", "Está bien usado", "Que el techo sea de lata no es consecuencia de que se rompió."),
        ("abc", "{F} ¿Qué cambia entre el Párrafo A y el B?", "El B une las ideas con conectores y evita repetir palabras", "El B tiene más repeticiones", "El B no tiene ideas", "El párrafo B es más cohesionado que el párrafo A."),
    ],
    ctx=("abc", "En una carta quieres decir: «Las calles están oscuras. Hay más riesgo de asaltos.» ¿Cómo unirías ambas ideas?", "«Las calles están oscuras; por eso hay más riesgo de asaltos»", "«Las calles están oscuras; sin embargo, hay más riesgo de asaltos»", "«Las calles están oscuras; para que hay más riesgo de asaltos»", "El conector «por eso» expresa la consecuencia de lo anterior."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué es la coherencia de un texto?", "La relación lógica de sus ideas con una idea central", "Evita contradicciones y cambios de tema."),
        ("En Lengua y Literatura de EPJA: ¿qué es la cohesión de un texto?", "La unión de sus oraciones con recursos del lenguaje", "Se logra con conectores, referentes y puntuación."),
        ("En Lengua y Literatura de EPJA: ¿para qué sirven los referentes?", "Para no repetir palabras ya mencionadas", "Evitan que el texto suene entrecortado.")],
    op=("Mejora este párrafo en tu cuaderno usando conectores y evitando repeticiones: «El paradero no tiene techo. El paradero está en la avenida. Las personas se mojan. Hay que instalar un techo». Escribe tu versión y señala los conectores que usaste. Guíate por el modelo de este ejemplo: {F}",
        "Versión: «El paradero de la avenida no tiene techo; por eso las personas se mojan cuando llueve. Para evitarlo, conviene instalar uno». Conectores: «por eso», «para evitarlo».",
        ["conserva la idea central", "usa al menos dos conectores adecuados", "evita repetir «el paradero»"],
        ["párrafo reescrito y conectores señalados"],
        ["usar conectores sin relación", "repetir las mismas palabras"],
        "Pregunta: «¿Qué relación muestra cada conector?»."),
    reinforce="Elige un párrafo de un aviso y marca los conectores que ya trae.",
    extend="Escribe cuatro oraciones sobre un problema de tu barrio, usando «porque», «además», «por eso» y «sin embargo».",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo cómo pasar del plan al borrador: ordeno ideas, uso un plan y escribo una carta breve.",
    prior=["Tengo una postura con argumentos.", "Uso conectores.", "Sé ordenar una secuencia de ideas."],
    explain=[
        "Escribir bien se parece a construir: primero se planifica, luego se redacta, después se revisa. El plan te dice qué decir y en qué orden; el borrador pone esas ideas en oraciones; la revisión mejora lo escrito.",
        "Un plan de carta tiene el tema, la postura, los argumentos en orden de importancia y el cierre con la petición. Con ese plan, el borrador puede tener cuatro párrafos cortos: saludo y presentación, argumentos, respuesta a quien piensa distinto y petición final.",
        "Un recurso de persuasión útil en la carta es el ejemplo concreto: «en invierno las personas esperan hasta 20 minutos bajo la lluvia». Otro es apelar al bien común: «es un beneficio para todos». Y siempre, un tono respetuoso hace que más personas quieran leer y apoyar tu carta.",
    ],
    vocab=[("planificar", "organizar qué decir y en qué orden antes de escribir"), ("borrador", "primera versión de un texto, que se puede mejorar"), ("bien común", "beneficio para toda una comunidad"), ("secuencia", "orden en que se presentan las ideas")],
    worked=[
        ("Ordenar frases de una carta", "Frases (inventadas): (a) «Por eso, solicito instalar un techo». (b) «Señor director:». (c) «El paradero no tiene techo».", ["El saludo va primero.", "Luego el problema.", "Al final, la petición."], "Orden: b, c, a"),
        ("Pasar del plan al borrador", "Plan: tema, paradero sin techo; argumento, hay personas mayores.", ["Convierto el tema en una oración.", "Convierto el argumento en otra con un conector."], "«El paradero no tiene techo. Además, lo usan personas mayores»"),
    ],
    mistakes=[("Empezar a escribir sin plan.", "Sin plan es fácil olvidar un argumento o la petición.", "Anota el tema, la postura, los argumentos y el cierre antes de redactar."),
              ("Dejar la petición sin fecha o destinatario claros.", "Una petición vaga no compromete a nadie a actuar.", "Dile a quién pides algo y en qué plazo razonable.")],
    T=[
        ("abc", "{F} ¿Cuál es la postura del plan de carta?", "La municipalidad debe instalar un techo en el paradero", "El paradero debe cerrarse", "Los buses deben pasar más rápido", "Está escrita en el plan como «Postura»."),
        ("=", "{F} Si cada día 60 personas esperan en el paradero y 20 de ellas son mayores, ¿cuántas no son mayores? (datos de ejemplo)", "60 - 20", "Se resta las personas mayores del total que espera.", " personas"),
        ("{F} ¿Cuántos minutos dice el plan que esperan las personas bajo la lluvia en invierno? Escribe solo el número.", "20", "El primer argumento del plan dice hasta 20 minutos."),
        ("abc", "{F} ¿Cuál de las frases desordenadas va primero?", "(b) «Señor director:»", "(a) «Por eso, solicito instalar un techo»", "(d) la despedida", "El saludo formal abre toda carta al director."),
        ("abc", "{F} ¿Cuál frase presenta el problema?", "(c) «El paradero de la avenida no tiene techo...»", "(a) «Por eso, solicito...»", "(e) «Además, lo usan cada día...»", "Describe el problema que motiva la carta."),
        ("ab", "{F} ¿Qué frase debe ir justo después de la que presenta el problema?", "(e) «Además, lo usan cada día muchas personas mayores y trabajadoras»", "(d) la despedida", "«Además» agrega un argumento al problema."),
        ("abc", "{F} ¿Qué frase expresa la petición?", "(a) «Por eso, solicito instalar un techo en el paradero»", "(b) el saludo", "(d) la despedida", "Contiene el verbo «solicito» con lo que se pide."),
        ("abc", "{F} ¿Dónde debe ir la despedida (d)?", "Al final de la carta", "Al principio", "En medio del segundo argumento", "La despedida cierra el texto de la carta."),
        ("ab", "{F} ¿Qué recurso de persuasión usa «cada día muchas personas mayores y trabajadoras»?", "Apelar a quienes más necesitan el techo", "Presentar una cifra exacta", "Resalta el efecto en personas vulnerables y en quienes trabajan."),
        ("abc", "{F} ¿Qué conector se usa en (e) «Además, lo usan cada día...»?", "«Además», que suma un argumento", "«Por eso», que indica consecuencia", "«Sin embargo», que marca contraste", "El conector «además» agrega una razón más."),
        ("abc", "¿Cuál es una petición bien formulada?", "«Solicito a la municipalidad instalar un techo en el paradero durante este mes»", "«Quiero que alguien haga algo»", "«Todo está mal»", "Señala a quién, qué y en qué plazo."),
        ("ab", "Una persona escribe en una carta: «Son unos incompetentes». ¿Cómo cambiarías la frase manteniendo la postura?", "«Solicito que se atienda este problema con urgencia»", "«Son los peores del mundo»", "Mantiene la firmeza de la petición sin insultar a nadie."),
        ("abc", "{F} ¿Cuál es el orden más adecuado de la carta del plan?", "Saludo, problema, argumento adicional, petición, despedida", "Despedida, petición, saludo, problema, argumento", "Argumento, despedida, saludo, petición, problema", "El orden va de la presentación al cierre."),
    ],
    ctx=("abc", "Tu equipo de trabajo quiere escribir una carta pidiendo un lugar techado para almorzar. ¿Qué haces primero?", "Planificar: tema, postura, argumentos y petición", "Escribir una despedida larga", "Enviar la carta sin revisar", "Planificar ordena las ideas antes de redactar."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué es un borrador?", "La primera versión de un texto, que se puede mejorar", "Se revisa y corrige antes de la versión final."),
        ("En Lengua y Literatura de EPJA: ¿qué debe incluir un plan de carta?", "Tema, postura, argumentos y petición final", "El plan guía la redacción de toda la carta."),
        ("En Lengua y Literatura de EPJA: ¿qué es apelar al bien común?", "Mostrar que algo beneficia a toda la comunidad", "Es una estrategia de persuasión respetuosa.")],
    op=("Escribe el borrador de una carta breve usando el plan: {F} En tu cuaderno redacta cuatro párrafos cortos: saludo y problema, argumentos, respuesta a una posible objeción y petición con despedida. Usa dos conectores y no escribas datos personales reales (firma con un nombre de ejemplo).",
        "Señor director: El paradero de la avenida no tiene techo y en invierno las personas esperan bajo la lluvia. Además, lo usan cada día personas mayores y trabajadoras. Algunos piensan que es caro; sin embargo, un techo se instala en pocos días. Por eso, solicito a la municipalidad instalarlo este mes. Atentamente, Luis Reyes (nombre de ejemplo).",
        ["sigue el plan en orden", "usa conectores y evita repetir palabras", "su tono es respetuoso y la petición es clara"],
        ["una carta de cuatro párrafos"],
        ["escribir datos personales reales", "omitir la petición"],
        "Pregunta: «¿Qué pides, a quién y para cuándo?»."),
    reinforce="Escribe tu propio plan de carta de cuatro líneas sobre un problema que conozcas.",
    extend="Convierte tu plan en una carta de cuatro párrafos y léela en voz alta a otra persona.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a una situación de la comunidad: elijo una situación, formulo una postura y escribo una carta al director.",
    prior=["Planifico una carta con postura, argumentos y petición.", "Uso conectores y referentes.", "Escribo con tono respetuoso."],
    explain=[
        "Aplicar es usar lo aprendido en una situación real. Las situaciones de hoy son de ejemplo: basura acumulada, filas en un consultorio y un bus que pasa cada vez menos. Son problemas que muchas comunidades reconocen.",
        "Elige una situación y formula una postura sobre ella. Luego revisa los datos del texto: qué es hecho y qué es opinión. Usa solo datos comprobables y cuida el tono: el reclamo es más fuerte cuando no insulta.",
        "En temas de salud, no afirmes que algo causó una enfermedad si el texto dice que no es seguro. Una carta responsable usa solo lo que se puede sostener y pide a la autoridad que investigue o aclare.",
    ],
    vocab=[("reclamo", "queja formal sobre algo que no funciona bien"), ("autoridad", "persona o institución que puede resolver un problema"), ("causa", "razón por la que ocurre algo"), ("responsable", "que cuida lo que dice y sus consecuencias")],
    worked=[
        ("Elegir la postura", "Situación (inventada): la sede vecinal no tiene calefacción.", ["Identifico el problema: falta de calefacción.", "Formulo una propuesta: instalar una estufa segura."], "Postura: la municipalidad debe apoyar la calefacción de la sede"),
        ("Evitar una afirmación sin respaldo", "Frase (inventada): «La basura enfermó a mi vecino».", ["El texto dice que no se asocia con certeza.", "Corrijo: «Hay un caso de un niño enfermo; pedimos revisar si hay relación»."], "Se reemplaza una causa no comprobada por una petición de revisión"),
    ],
    mistakes=[("Afirmar una causa sin pruebas.", "Atribuir algo a una causa que no es segura puede ser injusto y debilita la carta.", "Di lo que sabes y pide que se investigue."),
              ("Incluir datos personales de otras personas.", "Se debe cuidar la privacidad de los demás.", "Habla de «un vecino» sin nombre ni dirección.")],
    T=[
        ("abc", "{F} En la Situación A, ¿cuántos días de la semana pasa el camión?", "Dos, martes y viernes", "Tres", "Todos", "El texto dice que pasa los martes y viernes."),
        ("ab", "{F} ¿Cuál es una postura adecuada para la Situación A?", "La municipalidad debe aumentar los días de recolección en calle Los Pinos", "Hay que culpar al vecino del niño", "Propone una solución para la acumulación de basura."),
        ("{F} En la Situación B, ¿a qué hora comienza la atención? Escribe solo la hora, como 9:00.", "9:00", "El texto dice que atienden desde las 9:00."),
        ("=", "{F} En la Situación B, las personas hacen fila desde las 6:00 y los cupos se acaban a las 8:00. ¿Cuántas horas pasan desde que se forma la fila hasta que se acaban?", "8 - 6", "Se resta la hora de inicio de la fila a la hora en que se acaban los cupos.", " horas"),
        ("=", "{F} En la Situación C, el bus pasaba cada 15 minutos y ahora cada 40. ¿Cuántos minutos más esperan ahora?", "40 - 15", "Se resta el tiempo anterior al tiempo actual de espera.", " minutos"),
        ("abc", "{F} ¿Cuál es un argumento válido para la Situación C?", "Desde hace un mes pasa cada 40 minutos y muchas personas llegan tarde a su turno", "El bus es lindo", "A mí me gusta caminar", "Es comprobable y se relaciona con el problema."),
        ("abc", "{F} ¿Qué frase evita afirmar una causa sin pruebas en la Situación A?", "«Un niño enfermó y pedimos que se revise si hay relación con la basura»", "«La basura enfermó al niño»", "«Los vecinos son culpables»", "Dice lo que ocurrió y pide revisar."),
        ("ab", "{F} ¿Qué petición es adecuada para la Situación B?", "Solicitar que se amplíe el sistema de horas para evitar filas desde la madrugada", "Pedir que cierren el consultorio", "Propone una solución concreta sin atacar a nadie."),
        ("abc", "{F} ¿Qué conector sirve para unir «Hace un mes el bus pasa cada 40 minutos» con «muchas personas llegan tarde»?", "Por eso", "Sin embargo", "Aunque", "El conector muestra la consecuencia entre las dos ideas."),
        ("abc", "{F} ¿Qué dato falta en la Situación A para pedir con más fuerza?", "Desde qué fecha exacta se acumula la basura y en qué cantidad", "El nombre del vecino enfermo", "Una opinión sobre el municipio", "Fecha y cantidad hacen el reclamo más preciso."),
        ("ab", "{F} ¿Cuál de estas frases tiene un tono más adecuado?", "«Solicito que se atienda este problema, que afecta a muchas personas»", "«Son unos flojos que no hacen nada»", "Es una frase firme y respetuosa, sin insultos."),
        ("abc", "¿Qué debes evitar escribir en una carta para el diario?", "Datos personales de otras personas, como su nombre y dirección", "Una fecha", "Un argumento con cifra", "Se debe proteger la privacidad de otras personas."),
        ("ab", "Una persona quiere escribir sobre la Situación B. ¿Cuál es un buen primer paso?", "Anotar su postura y dos argumentos comprobables", "Escribir una carta sin plan", "El plan ayuda a no olvidar partes."),
    ],
    ctx=("abc", "Quieres escribir sobre el consultorio. ¿Cuál es el mejor argumento comprobable?", "«Para pedir hora se hace fila desde las 6:00 y a las 8:00 ya no quedan cupos»", "«Es un lugar horrible»", "«Todos saben que es malo»", "Se puede verificar con horas concretas."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué es una autoridad en una carta de reclamo?", "La persona o institución que puede resolver el problema", "La carta se dirige a quien puede actuar."),
        ("En Lengua y Literatura de EPJA: ¿por qué no conviene afirmar una causa sin pruebas?", "Porque puede ser injusto y debilita la carta", "Es mejor pedir que se investigue."),
        ("En Lengua y Literatura de EPJA: ¿qué se evita escribir en una carta para compartir?", "Datos personales de otras personas", "Así se protege la privacidad de otras personas.")],
    op=("Elige la situación A, B o C: {F} Escribe en tu cuaderno una carta al director de cuatro párrafos: saludo y problema, dos argumentos con dato, una respuesta a una posible objeción y la petición con despedida. Usa un nombre de ejemplo para la firma y no incluyas datos personales reales.",
        "Señor director: En el consultorio, para pedir hora se hace fila desde las 6:00 y a las 8:00 ya no quedan cupos. Además, la atención comienza a las 9:00. Se podría pensar que no hay otra forma; sin embargo, se puede organizar un sistema de horas previo. Por eso, solicito ampliar el sistema de horas. Atentamente, Marta Soto (nombre de ejemplo).",
        ["elige una situación y define una postura clara", "usa dos argumentos con datos del texto", "usa conectores, tono respetuoso y petición clara"],
        ["una carta de cuatro párrafos"],
        ["afirmar causas sin respaldo", "usar un tono agresivo"],
        "Pregunta: «¿Qué datos del texto sostienen tu postura?»."),
    reinforce="Escribe la petición final de una carta sobre una de las situaciones, en dos líneas.",
    extend="Escribe una segunda carta sobre otra de las situaciones y compara cuál argumento fue más fuerte.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso y reescribo una carta: uso una lista de cotejo, corrijo fallas y evalúo mi avance.",
    prior=["Planifico y redacto una carta.", "Uso conectores y referentes.", "Distingo datos de opiniones."],
    explain=[
        "Revisar es leer el texto como lector, no como autor. Una buena revisión pregunta: ¿tiene postura clara?, ¿tiene argumentos con datos?, ¿se entiende el orden?, ¿usa conectores y evita repetir?, ¿el tono es respetuoso?, ¿pide algo concreto?",
        "Una lista de cotejo ordena estas preguntas con casillas de sí o no. Cada «no» es una oportunidad de mejora: agrega un dato, reemplaza un insulto por una petición, une ideas con un conector o corta una idea que se repite.",
        "Al terminar, mira lo que lograste: ¿escribes una postura clara?, ¿usas datos?, ¿cuidas el tono? Y decide qué mejorarás la próxima vez. Escribir mejor es un proceso: se aprende revisando.",
    ],
    vocab=[("revisar", "leer un texto para detectar y corregir fallas"), ("lista de cotejo", "lista de preguntas para comprobar que un texto cumple lo pedido"), ("tono", "actitud que se percibe en el modo de escribir"), ("reescribir", "volver a escribir un texto mejorándolo")],
    worked=[
        ("Reemplazar un insulto", "Frase (inventada): «Son unos inútiles».", ["Identifico que no entrega información y ofende.", "Escribo en su lugar una petición concreta."], "«Solicito que se atienda este problema, que afecta a muchas personas»"),
        ("Unir ideas repetidas", "Frase (inventada): «La calle está mala. La calle tiene hoyos».", ["Veo la repetición de «la calle».", "Uno las ideas con una causa."], "«La calle está en mal estado porque tiene hoyos»"),
    ],
    mistakes=[("Corregir solo la ortografía y no las ideas.", "La ortografía importa, pero la postura, los datos y el orden son lo central.", "Revisa primero las ideas y al final la ortografía."),
              ("Corregir el texto de otra persona sin respeto.", "Una crítica sin respeto la desanima.", "Señala lo que está bien y propón una mejora concreta.")],
    T=[
        ("abc", "{F} ¿Qué falla de tono tiene el borrador?", "Insulta con frases como «unos inútiles»", "Es demasiado cordial", "Es demasiado largo", "Los insultos no ayudan a que escuchen la petición."),
        ("ab", "{F} ¿El borrador tiene una postura clara?", "No: dice que la calle está mala, pero no pide nada", "Sí: pide arreglar la calle", "Falta una petición concreta que defina la postura."),
        ("{F} ¿Cuántas veces aparece la frase «la calle está mala» en el borrador? Escribe solo el número.", "2", "Aparece en «La calle está mala» y en «la calle está mala porque está mala»."),
        ("abc", "{F} ¿Qué falla de coherencia tiene el borrador?", "Dice que la calle está mala y luego que es bonita", "Usa un saludo", "Tiene una fecha", "Dos ideas contrarias sin explicar se contradicen."),
        ("abc", "{F} ¿Qué falla tiene la frase «la calle está mala porque está mala»?", "Es una explicación circular que repite la idea sin dar una razón", "Usa un conector de contraste", "Tiene un dato", "La frase no explica la causa real de nada."),
        ("abc", "{F} ¿Qué dato podría agregarse para fundamentar el reclamo?", "Cuántos hoyos hay y desde cuándo", "Cuánto se enoja quien escribe", "El color de la calle", "Un dato comprobable apoya el reclamo."),
        ("ab", "{F} ¿Cuál es una mejor despedida que «Chao»?", "«Atentamente, Marta Soto (nombre de ejemplo)»", "«Chao, adiós»", "La despedida formal cierra con respeto e identifica a quien escribe."),
        ("abc", "{F} ¿Qué hace falta en el saludo «Director:»?", "Un trato formal, como «Señor director:»", "Más signos de exclamación", "Un chiste", "El saludo debe ser formal y respetuoso."),
        ("abc", "¿Cuál de estas es una buena reescritura de «La calle está mala»?", "«La calle Los Pinos tiene seis hoyos desde hace un mes, lo que dificulta el paso de vehículos y personas»", "«La calle es horrible»", "«Todo está mal»", "La frase da datos, tiempo y consecuencia del problema."),
        ("ab", "Camila dice que su carta está lista porque no tiene faltas de ortografía. ¿Qué conviene revisar también?", "Si tiene postura, argumentos con datos, orden y petición", "Nada más", "Una carta sin faltas puede igual no tener postura ni argumentos."),
        ("abc", "{F} Si cambias el borrador por: «Solicito arreglar los hoyos de la calle Los Pinos, que dificultan el paso de personas», ¿qué parte mejora?", "La postura y la petición, porque dicen qué se solicita", "El saludo", "La despedida", "Esa frase expresa una petición clara."),
        ("abc", "Al cerrar esta unidad, ¿cuál es un buen paso para seguir mejorando?", "Escribir una carta cada semana y revisarla con la lista de cotejo", "No volver a escribir", "Usar siempre las mismas frases", "Practicar y revisar fortalece la escritura."),
        ("ab", "Una persona dice: «Si repito mucho una idea, convenceré más». ¿Qué responder?", "Mejor es dar razones distintas y datos que apoyen la idea", "Sí: repetir convence", "Repetir sin razones cansa y no convence."),
    ],
    ctx=("abc", "Una persona conocida te pide revisar su carta, que dice «Es una vergüenza lo que pasa en la plaza». ¿Cómo se lo dices con respeto?", "«Tu idea es clara; falta un dato y una petición concreta, por ejemplo qué se debe arreglar»", "«Tu carta es mala»", "«No escribas más»", "Reconoce lo bueno y propone una mejora concreta."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué es una lista de cotejo?", "Una lista de preguntas para comprobar que un texto cumple lo pedido", "Cada respuesta «no» indica qué se debe mejorar."),
        ("En Lengua y Literatura de EPJA: ¿qué se revisa primero al corregir una carta?", "La postura, los argumentos y el orden de las ideas", "Las ideas se revisan antes de la ortografía."),
        ("En Lengua y Literatura de EPJA: ¿por qué evitar los insultos en una carta?", "Porque restan credibilidad y no ayudan a lograr la petición", "El tono respetuoso favorece que te escuchen.")],
    op=("Reescribe el borrador: {F} En tu cuaderno escribe una carta nueva de cuatro párrafos con saludo formal, un problema con un dato de ejemplo, un argumento más, una petición clara y una despedida con nombre de ejemplo. Luego marca con sí o no la lista de cotejo: postura clara, datos, conectores, tono respetuoso, petición concreta.",
        "Señor director: La calle Los Pinos tiene seis hoyos desde hace un mes. Por eso, los vehículos y las personas tienen dificultades para pasar. Además, algunos pensarán que es un arreglo costoso; sin embargo, reparar los hoyos evita daños mayores. Solicito a la municipalidad repararlos este mes. Atentamente, Marta Soto (nombre de ejemplo). Lista: sí, sí, sí, sí, sí.",
        ["corrige tono, coherencia y petición", "usa un dato y conectores", "completa la lista de cotejo con honestidad"],
        ["una carta reescrita y cinco casillas marcadas"],
        ["mantener los insultos", "marcar todo con sí sin revisar"],
        "Pregunta: «¿Qué cambió entre el borrador y tu versión?»."),
    reinforce="Aplica la lista de cotejo a una carta que hayas escrito en esta clase.",
    extend="Escribe una carta final para otra situación de esta unidad y cuéntale a otra persona qué aprendiste al revisarla.",
)

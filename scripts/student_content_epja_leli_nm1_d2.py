"""Lengua y Literatura EPJA Media Nivel 1, módulo 4 (parte 2): OAD-14, investigar una obra literaria para identificar relaciones de intertextualidad (validez y confiabilidad de fuentes; recursos no lingüísticos). Las fuentes son fichas inventadas escritas en papel."""
from __future__ import annotations

from epja_leli_nm1_d_common import build

O = "EPJA-LELI-NM1-OAD-14"

F1 = ("Mensaje 1 (inventado), cadena reenviada sin firma ni fecha: «¡Urgente! Mañana cortan el agua en todo el barrio por una semana. Reenvía a todos». "
      "Mensaje 2 (inventado), aviso pegado en la sede vecinal, con la firma de la directiva, fecha 12 de marzo y teléfono de la sede: «El jueves habrá corte de agua en las calles 1 a 4, de 9 a 13 horas». "
      "Pregunta del club de lectura (inventada): ¿qué obra clásica recuerda el relato «El regreso de Nelly» y en qué se parecen? "
      "Dato de apoyo: en la Odisea, de Homero, Ulises vuelve a su isla tras años de viaje y su perro lo reconoce.")

F2 = ("Ficha A (inventada), prólogo de una edición escolar de la Odisea, firmado por la profesora Ana Ríos, 2019: «La Odisea cuenta el regreso de Ulises a Ítaca. Penélope lo espera y rechaza a quienes la presionan». "
      "Ficha B (inventada), cadena de mensajes, sin autor ni fecha: «La Odisea cuenta la guerra de Troya y la escribió Cervantes». "
      "Ficha C (inventada), entrada de un blog personal, 2015, autor sin datos: «Creo que Ulises es el mejor personaje de toda la literatura». "
      "Datos de apoyo: Cervantes escribió Don Quijote de la Mancha; la Odisea se atribuye a Homero y cuenta el regreso de Ulises tras la guerra de Troya.")

F3 = ("Pregunta de investigación (inventada): ¿con qué personaje de la Odisea se relaciona Marta, de «La espera de Marta»? "
      "Fuente 1 (inventada), sitio de un centro de estudios literarios, autora Dra. Carla Vega, 2022, con lista de obras consultadas: «Penélope teje una tela y la deshace de noche para ganar tiempo». "
      "Fuente 2 (inventada), foro de aficionados, usuario con seudónimo, sin fecha: «Marta es Telémaco porque los dos buscan a su padre». "
      "Fuente 3 (inventada), guía escolar de la Odisea firmada por un equipo docente, 2018: «Telémaco sale a buscar noticias de su padre; Penélope espera en casa». "
      "Datos del relato: Marta teje un chaleco para Hugo y cada noche suelta unas vueltas; su hijo Nico escribe cartas para saber de su padre.")

F4 = ("Fuente X (inventada), página de una editorial escolar, con nombre de la autora y fecha 2020: «Don Quijote de la Mancha se publicó en dos partes: la primera en 1605 y la segunda en 1615». "
      "Fuente Y (inventada), video resumen de un canal anónimo, 2021: «El Quijote es de 1850 y lo escribió Homero». "
      "Fuente Z (inventada), descripción de la página de créditos de una edición impresa: «Miguel de Cervantes Saavedra, Don Quijote de la Mancha, primera parte, 1605». "
      "Tabla de diseño de la Fuente Y (inventada): Titular: letras rojas muy grandes con signos de exclamación, «¡LA VERDAD QUE NADIE TE CUENTA!». Imagen: foto de un barco antiguo, sin pie de foto. "
      "Disposición: el titular ocupa la mitad de la pantalla y la fuente de los datos aparece al final, en letra muy pequeña. Audio: música de suspenso y voz grave. "
      "Dato de apoyo: Cervantes es el autor del Quijote.")

F5 = ("Pregunta de investigación (inventada): ¿qué símbolo comparten el mito del Minotauro y «El pasillo amarillo»? "
      "Fuente 1 (inventada), guía de lectura de un centro cultural, 2021, firmada por su equipo editor: «En el mito, el hilo que entrega Ariadna permite a Teseo volver del laberinto». "
      "Fuente 2 (inventada), transcripción de un programa de radio, con anotaciones de sonido: [música de suspenso] Locutor: «El laberinto esconde un secreto terrible que nunca te contaron» [efecto de trueno]. «Hoy lo revelamos todo». "
      "Fuente 3 (inventada), apuntes del club de lectura, escritos por la monitora del club, 2023: «Teseo vuelve gracias al hilo; Rosa llega a su destino gracias a una línea amarilla que la guía». "
      "Datos de «El pasillo amarillo»: Rosa se pierde en un hospital y una funcionaria le muestra una línea amarilla en el piso que la lleva a la oficina de exámenes.")

F6 = ("Informe de Jaime (inventado), club de lectura. Pregunta: ¿qué obra recuerda «La espera de Marta»? "
      "Fuentes: un blog sin autor, de 2015. "
      "Conclusión: «Todos los cuentos modernos copian la Odisea y no tienen nada propio». "
      "Referencias: ninguna. "
      "Dato del relato: Marta teje un chaleco y suelta vueltas cada noche mientras espera a Hugo. "
      "Dato de apoyo: en la Odisea, Penélope teje una tela y la deshace de noche mientras espera a Ulises.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy parto de lo que ya hago a diario, como dudar de un mensaje, para aprender a investigar una obra literaria.",
    prior=["Recibo mensajes y avisos en el trabajo y en el barrio.", "A veces dudo si algo es verdad.", "Sé que una obra puede recordar a otra."],
    explain=[
        "Tú ya investigas en la vida diaria. Cuando te llega un mensaje reenviado, miras quién lo firma, si tiene fecha y si coincide con lo que dice la sede vecinal. Eso es evaluar una fuente: decidir si se puede confiar en lo que dice.",
        "Una fuente es el lugar o la persona de donde sacas información: un aviso, un libro, una página, una persona experta. Investigar es partir de una pregunta, buscar fuentes, revisar si son confiables y responder con datos que puedas mostrar.",
        "En literatura se hace lo mismo. Si quieres saber qué obra clásica recuerda un relato, no basta con pensar «me parece»: buscas qué dicen fuentes firmadas y fechadas sobre la obra, y lo comparas con el texto que tienes delante.",
    ],
    vocab=[("fuente", "lugar o persona de donde sacas información"), ("investigar", "buscar información para responder una pregunta"), ("confiable", "que merece confianza porque dice quién escribe y se puede comprobar"), ("verificar", "comprobar si algo es verdadero")],
    worked=[
        ("Elegir el mensaje más confiable", "Mensaje 1: cadena sin firma. Mensaje 2: aviso firmado, con fecha y teléfono.", ["Miro quién escribe: el Mensaje 2 tiene firma.", "Miro la fecha y un contacto: el Mensaje 2 los tiene.", "El Mensaje 1 no permite comprobar nada."], "El Mensaje 2 es más confiable"),
        ("Formular una pregunta de investigación", "Relato «El regreso de Nelly»: una camionera vuelve a su barrio tras tres años y su perro la reconoce.", ["Pienso a qué historia conocida recuerda.", "Escribo una pregunta que se pueda responder con fuentes: ¿qué obra clásica recuerda y en qué se parecen?"], "Pregunta clara que se puede investigar"),
    ],
    mistakes=[("Creer que algo es cierto porque muchos lo reenvían.", "Que algo circule mucho no prueba que sea verdad.", "Busca quién lo firma y si otra fuente lo confirma."),
              ("Responder «me parece» a una pregunta de investigación.", "Una investigación se apoya en fuentes y en el texto.", "Anota qué fuente respalda tu respuesta.")],
    T=[
        ("abc", "{F} ¿Cuál de los mensajes es más confiable?", "El Mensaje 2, firmado y con fecha y teléfono", "El Mensaje 1, porque dice «urgente»", "Ninguno de los dos", "El Mensaje 2 permite saber quién lo escribe y comprobarlo."),
        ("abc", "{F} ¿Qué datos le faltan al Mensaje 1 para poder confiar en él?", "Quién lo escribe y la fecha", "Más signos de exclamación", "El nombre de una calle", "Sin autoría ni fecha no se puede comprobar el mensaje."),
        ("{F} Según el aviso firmado, ¿cuántas calles incluye el corte de agua? Escribe el número.", "4", "El aviso dice «calles 1 a 4», que son cuatro calles."),
        ("abc", "{F} Antes de reenviar el Mensaje 1, ¿qué conviene hacer?", "Preguntar a la sede vecinal si es verdad", "Reenviarlo a todos de inmediato", "Borrar el Mensaje 2", "Verificar con quien puede confirmar evita difundir un dato falso."),
        ("abc", "En Lengua y Literatura: ¿qué es investigar?", "Buscar información en fuentes para responder una pregunta", "Copiar un texto sin leerlo", "Elegir lo que más me gusta", "Investigar parte de una pregunta y busca información que la responda."),
        ("ab", "{F} ¿Cuál es la pregunta de investigación del club?", "¿Qué obra clásica recuerda «El regreso de Nelly» y en qué se parecen?", "¿Qué día cortan el agua?", "Es la pregunta sobre un relato y una obra que se puede responder con fuentes."),
        ("abc", "{F} Un vecino dice: «Es verdad, porque muchos lo reenvían». ¿Qué respuesta es adecuada?", "Que lo reenvíen muchos no prueba que sea cierto", "Tienes razón: más mensajes son más verdad", "Solo importa el color del texto", "La cantidad de reenvíos no es una prueba."),
        ("abc", "{F} Si buscas información sobre la Odisea, ¿qué fuente conviene mirar primero?", "Una edición escolar con prólogo firmado", "Una cadena sin firma", "Un mensaje sin fecha", "Un prólogo firmado permite saber quién lo escribe."),
        ("{F} ¿Qué día habrá corte de agua según el aviso firmado? Escribe una palabra.", "jueves", "El aviso dice «El jueves habrá corte de agua»."),
        ("abc", "¿Qué dato del Mensaje 2 muestra que viene de un lugar identificable?", "La firma de la directiva y el teléfono de la sede", "Que está pegado en una pared", "Que usa letras grandes", "La firma y el teléfono permiten comprobar quién lo escribió."),
        ("ab", "{F} Los dos mensajes hablan del mismo corte, pero uno dice todo el barrio y el otro solo las calles 1 a 4. ¿Qué haces?", "Consulto con la sede vecinal, que es la fuente directa", "Elijo el que me parece más urgente", "Contrastar con la fuente directa permite decidir entre dos datos distintos."),
        ("abc", "{F} ¿Qué palabras clave sirven para buscar información sobre la pregunta del club?", "Odisea, Ulises, regreso", "Camión, ruta, perro", "Agua, corte, jueves", "Las palabras clave nombran la obra y el tema de la pregunta."),
        ("abc", "{F} ¿Por qué el dato sobre Ulises sirve para la investigación del club?", "Porque dice qué cuenta la Odisea y permite compararla con el relato", "Porque habla del agua", "Porque es un aviso vecinal", "Es un dato de la obra con el que se puede comparar el relato."),
    ],
    ctx=("abc", "En un grupo de mensajes alguien manda: «Dicen que mañana la oficina de trámites no atiende». No dice quién lo dijo. ¿Qué haces?", "Llamo a la oficina, que es la fuente directa", "Lo reenvío a todos", "Cambio mis planes sin comprobar nada", "Se verifica con quien puede confirmar la información."),
    sc=[("En Lengua y Literatura: ¿qué es una fuente?", "Lugar o persona de donde sacas información", "Una fuente entrega datos que luego se evalúan."),
        ("¿Qué miras primero para confiar en un mensaje?", "Quién lo escribe y la fecha", "La autoría y la fecha permiten comprobarlo."),
        ("¿Por dónde parte una investigación?", "Con una pregunta", "Toda investigación parte de una pregunta.")],
    op=("Elige una noticia o un aviso que hayas recibido y descríbelo con tus palabras sin datos personales. Escribe qué datos permiten confiar o dudar: quién lo firma, fecha, contacto y si otra fuente lo confirma. {F}",
        "Aviso del centro: tiene firma de la directiva, fecha y teléfono, por eso confío. Cadena del barrio: sin firma ni fecha, por eso dudo y pregunto a la sede.",
        ["describe el mensaje", "usa al menos dos datos para confiar o dudar", "dice cómo verificaría"],
        ["tres oraciones escritas"],
        ["decir «es falso» sin razones", "incluir datos personales"],
        "Pregunta: «¿Quién lo escribe y cómo podrías comprobarlo?»."),
    reinforce="Revisa un aviso que veas hoy y anota si tiene firma, fecha y contacto.",
    extend="Escribe una pregunta de investigación sobre un relato que conozcas y a qué historia clásica podría recordar.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo el vocabulario para investigar: fuente, autoría, validez, confiabilidad, contrastar y palabra clave.",
    prior=["Sé que investigar parte de una pregunta.", "Miro quién firma un mensaje.", "Reconozco que algunas fuentes son mejores que otras."],
    explain=[
        "Evaluar una fuente tiene criterios. La autoría: quién escribió y qué experiencia tiene. La fecha: cuándo se escribió. El propósito: para qué se escribió, por ejemplo informar o dar una opinión. El respaldo: si cita otras obras o datos que se pueden comprobar.",
        "Una fuente es válida cuando lo que dice es correcto y se puede comprobar. Es confiable cuando quien la entrega merece confianza porque se identifica, explica de dónde saca los datos y tiene conocimiento del tema. Contrastar es comparar varias fuentes para ver si coinciden.",
        "Una palabra clave es una palabra que nombra lo principal de tu pregunta y sirve para buscar. Si preguntas qué obra se relaciona con un relato sobre una espera, tus palabras clave pueden ser «Odisea», «Penélope» y «espera».",
    ],
    vocab=[("autoría", "quién escribió el texto"), ("validez", "que lo dicho sea correcto y comprobable"), ("confiabilidad", "que quien informa merece confianza"), ("palabra clave", "palabra que nombra lo principal de tu pregunta")],
    worked=[
        ("Evaluar una fuente con criterios", "Ficha A: prólogo firmado por Ana Ríos, 2019, edición escolar de la Odisea.", ["Autoría: profesora identificada.", "Fecha: 2019.", "Propósito: informar a estudiantes.", "Coincide con los datos de apoyo."], "Fuente confiable y válida"),
        ("Detectar un dato incorrecto", "Ficha B dice que Cervantes escribió la Odisea.", ["Datos de apoyo: Cervantes escribió el Quijote y la Odisea se atribuye a Homero.", "El dato no coincide."], "La Ficha B no es válida"),
    ],
    mistakes=[("Confundir una opinión con un dato.", "Una opinión expresa lo que alguien piensa; un dato se puede comprobar.", "Pregunta: «¿esto se puede comprobar en la obra o en otra fuente?»."),
              ("Creer que una fuente es válida solo por estar escrita.", "Estar escrito no prueba que sea verdadero.", "Revisa autoría, fecha y si coincide con otras fuentes.")],
    T=[
        ("{F} ¿Quién firma la Ficha A? Escribe el nombre completo.", "Ana Ríos", "La Ficha A dice que la firma la profesora Ana Ríos."),
        ("{F} ¿En qué año se escribió la Ficha A? Escribe el número.", "2019", "El texto de la Ficha A indica el año 2019."),
        ("abc", "{F} ¿Qué ficha afirma algo que contradice los datos de apoyo?", "La Ficha B, que dice que Cervantes escribió la Odisea", "La Ficha A", "La Ficha C", "La Ficha B atribuye la Odisea a Cervantes, pero los datos de apoyo dicen otra cosa."),
        ("abc", "En Lengua y Literatura: ¿qué es una fuente confiable?", "Aquella cuyo autor se identifica y cuyos datos se pueden comprobar", "La que tiene más palabras", "La que aparece primero", "Una fuente confiable muestra su autoría y respaldo."),
        ("abc", "{F} ¿Qué ficha expresa una opinión personal y no un dato?", "La Ficha C", "La Ficha A", "La Ficha B", "«Creo que Ulises es el mejor personaje» es una opinión."),
        ("ab", "{F} ¿La Ficha C sirve para saber de qué trata la Odisea?", "No: es una opinión y no explica la obra", "Sí: nombra a Ulises", "La ficha da una opinión sobre un personaje, no un dato sobre la historia."),
        ("abc", "En Lengua y Literatura: ¿qué es una palabra clave?", "Una palabra que nombra lo principal de la pregunta y sirve para buscar", "La palabra más larga de un texto", "Un número de teléfono", "Las palabras clave guían la búsqueda hacia el tema."),
        ("abc", "{F} Para la pregunta «¿Qué obra se relaciona con un relato sobre una espera?», ¿qué palabras clave sirven mejor?", "Odisea, Penélope, espera", "Cervantes, 2015, blog", "Cadena, mensaje, reenviar", "Nombran la obra y el tema que se quiere investigar."),
        ("abc", "¿Qué es contrastar fuentes?", "Comparar lo que dicen varias fuentes para ver si coinciden", "Elegir la fuente más larga", "Copiar la primera fuente", "Contrastar permite detectar datos que no coinciden."),
        ("abc", "{F} ¿Cuál ficha sirve mejor para saber qué cuenta la Odisea?", "La Ficha A, prólogo firmado de una edición escolar", "La Ficha B, cadena sin autor", "La Ficha C, opinión de un blog", "Tiene autoría, fecha y coincide con los datos de apoyo."),
        ("ab", "{F} Una compañera dice: «La Ficha B es válida porque me la reenviaron muchas veces». ¿Qué le respondes?", "Que reenviarla no prueba que sea correcta: no coincide con los datos de apoyo", "Que tiene razón porque circula mucho", "La validez depende de que el dato se pueda comprobar, no de cuántos lo repiten."),
        ("abc", "{F} ¿Qué dato falta en la Ficha B para poder evaluarla?", "Quién la escribió y cuándo", "El color del texto", "El tamaño de la letra", "Sin autor ni fecha no se puede comprobar su confiabilidad."),
        ("abc", "{F} ¿Qué criterio permite decir que la Ficha C es débil como fuente de datos?", "Es una opinión de un autor sin datos y sin respaldo", "Tiene fecha 2015", "Nombra a Ulises", "La opinión sin respaldo no prueba nada sobre la obra."),
    ],
    ctx=("abc", "El club de lectura recibe dos resúmenes de la Odisea: uno de un prólogo firmado de 2019 y otro de una cadena sin autor. ¿Cuál usan primero y por qué?", "El prólogo, porque tiene autoría y fecha", "La cadena, porque llegó primero", "Ninguno, porque no hay resúmenes", "La autoría y la fecha permiten comprobar y confiar."),
    sc=[("En Lengua y Literatura: ¿qué significa contrastar?", "Comparar varias fuentes para ver si coinciden", "Contrastar varias fuentes ayuda a detectar errores de una sola."),
        ("¿Qué cuatro criterios uso para evaluar una fuente?", "Autoría, fecha, propósito y respaldo", "Son los criterios de la clase."),
        ("¿Una opinión es lo mismo que un dato?", "No", "Un dato se puede comprobar y una opinión no.")],
    op=("Haz una tabla de tres filas (Fichas A, B y C) y cuatro columnas (autoría, fecha, propósito, ¿confiable?) con los datos de la ficha de la clase. Después escribe una frase que diga con cuál ficha responderías qué cuenta la Odisea. {F}",
        "A: Ana Ríos; 2019; informar; sí. B: sin autor; sin fecha; no se sabe; no. C: sin datos; 2015; opinar; no sirve para datos. Responderé con la A porque tiene autoría y coincide con los datos de apoyo.",
        ["tabla con tres filas y cuatro columnas", "datos correctos de la ficha", "elige una ficha con motivo"],
        ["una tabla y una frase"],
        ["escribir datos que no están en la ficha", "elegir sin motivo"],
        "Pregunta: «¿Qué criterio usaste para descartar la ficha B?»."),
    reinforce="Escribe una palabra clave para cada pregunta: ¿qué obra recuerda un relato sobre un laberinto?, ¿y uno sobre un hombre que lee demasiado?",
    extend="Explica con tus palabras la diferencia entre validez y confiabilidad.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy veo paso a paso cómo se investiga una pregunta literaria: pregunta, palabras clave, fuentes, evaluación y respuesta.",
    prior=["Sé evaluar una fuente con autoría, fecha, propósito y respaldo.", "Sé formular una pregunta de investigación.", "Sé comparar personajes de dos obras."],
    explain=[
        "Investigar una obra tiene cinco pasos. Paso 1: escribe la pregunta. Paso 2: elige las palabras clave. Paso 3: reúne fuentes. Paso 4: evalúa cada una con autoría, fecha, propósito y respaldo. Paso 5: responde con datos y anota las referencias.",
        "Las referencias son los datos para encontrar la fuente de nuevo: quién la escribió, cómo se llama y en qué año. Con ellas, cualquier persona puede comprobar lo que afirmas. Una respuesta sin referencias es solo una opinión.",
        "No te quedes con la primera fuente. Contrasta al menos dos. Y siempre vuelve al relato que estás analizando: una fuente puede ser confiable en general y aun así no coincidir con lo que dice el texto que tienes delante.",
    ],
    vocab=[("referencia", "datos para volver a encontrar una fuente: autor, título y año"), ("respaldo", "datos u obras consultadas que apoyan lo que se dice"), ("seudónimo", "nombre inventado que alguien usa en lugar del suyo"), ("pregunta de investigación", "pregunta que se responde con fuentes")],
    worked=[
        ("Evaluar la Fuente 1", "Fuente 1: autora Dra. Carla Vega, 2022, lista de obras consultadas.", ["Autoría: persona identificada.", "Fecha: 2022.", "Respaldo: lista de obras consultadas.", "Coincide con el relato: Marta teje y suelta vueltas."], "La Fuente 1 es confiable y útil para la pregunta"),
        ("Descartar la Fuente 2", "Fuente 2: seudónimo, sin fecha, dice que Marta es Telémaco.", ["Autoría: seudónimo.", "Fecha: no hay.", "Contradice el relato: quien escribe cartas para saber de su padre es Nico."], "No sirve como evidencia"),
    ],
    mistakes=[("Quedarse con la primera fuente encontrada.", "Una sola fuente puede equivocarse.", "Contrasta con al menos otra."),
              ("Escribir una respuesta sin anotar de dónde sacaste cada dato.", "Sin referencias nadie puede comprobar tu respuesta.", "Anota autor, título o sitio, y año.")],
    T=[
        ("abc", "{F} ¿Cuáles son las palabras clave más útiles para la pregunta?", "Odisea, Marta, personaje", "Foro, seudónimo, fecha", "Chaleco, carta, invierno", "Nombran la obra, el relato y lo que se busca."),
        ("abc", "{F} ¿Cuál es la fuente más confiable?", "La Fuente 1, con autora, fecha y lista de obras consultadas", "La Fuente 2, de un foro", "Ninguna", "La Fuente 1 se puede comprobar por su autoría y respaldo."),
        ("{F} ¿De qué año es la Fuente 3? Escribe el número.", "2018", "La Fuente 3 dice que fue publicada en 2018."),
        ("ab", "{F} ¿Por qué es débil la Fuente 2?", "Tiene seudónimo, no tiene fecha ni respaldo", "Está escrita en español", "Una fuente sin autoría clara, sin fecha y sin respaldo no se puede comprobar."),
        ("abc", "{F} ¿Qué dato del relato coincide con lo que dice la Fuente 1?", "Marta teje un chaleco y suelta vueltas cada noche", "Nico escribe cartas", "Hugo está en el sur", "Penélope teje y deshace; Marta teje y suelta vueltas."),
        ("abc", "{F} Según la Fuente 3, ¿con qué personaje del relato se relaciona Nico?", "Con Telémaco, que busca noticias de su padre", "Con Penélope", "Con Ulises", "Nico escribe cartas para saber de su padre, como Telémaco."),
        ("ab", "{F} La Fuente 2 dice que Marta es Telémaco. ¿Coincide con el relato?", "No: Marta teje y espera, mientras quien busca noticias es Nico", "Sí: Marta busca a su padre", "En el relato quien escribe cartas para saber de su padre es Nico, no Marta."),
        ("abc", "En Lengua y Literatura: ¿qué paso viene después de evaluar las fuentes?", "Responder la pregunta con datos y anotar las referencias", "Buscar otra pregunta", "Borrar las fuentes", "El paso final es responder y registrar de dónde sale cada dato."),
        ("abc", "¿Cómo se anota una referencia?", "Autor, título o sitio y año", "Solo el color de la página", "Solo la hora en que se leyó", "Con esos datos se puede encontrar la fuente de nuevo."),
        ("{F} ¿Cuántas de las tres fuentes tienen fecha? Escribe el número.", "2", "Las Fuentes 1 y 3 tienen fecha; la 2 no."),
        ("ab", "¿Basta con una sola fuente para responder una pregunta de investigación?", "No: conviene contrastar al menos dos", "Sí: una fuente alcanza", "Contrastar permite detectar errores de una fuente."),
        ("abc", "{F} ¿Cuál es una respuesta apoyada en las fuentes?", "Marta se relaciona con Penélope, porque ambas esperan y tejen (Fuente 1 y relato)", "Marta es Telémaco porque lo dice un foro", "Marta no se relaciona con nadie", "La respuesta usa una fuente confiable y un dato del relato."),
        ("abc", "{F} ¿Qué haces con la Fuente 2 al escribir la respuesta?", "No la uso como evidencia: la menciono como opinión sin respaldo", "Copio su frase como si fuera cierta", "La uso como única fuente", "Una fuente sin autoría y que contradice el relato no sirve de evidencia."),
    ],
    ctx=("abc", "En tu club de lectura te piden averiguar con quién se relaciona Nico en la Odisea. Tienes un foro con seudónimo y una guía escolar firmada. ¿Qué haces?", "Uso la guía firmada y contrasto con otra fuente", "Uso solo el foro", "No uso ninguna", "La guía firmada tiene autoría; conviene contrastar."),
    sc=[("¿Cuántos pasos tiene la investigación de hoy?", "Cinco", "Pregunta, palabras clave, fuentes, evaluación y respuesta con referencias."),
        ("En Lengua y Literatura: ¿qué es una referencia?", "Los datos para encontrar de nuevo la fuente", "Autor, título y año permiten volver a la fuente."),
        ("¿Qué hago si una fuente contradice el relato que analizo?", "La contrasto y no la uso como evidencia", "El relato es la prueba más directa.")],
    op=("Con la ficha de la clase, responde por escrito en cuatro oraciones la pregunta de investigación. Usa dos fuentes, indica una referencia para cada una y explica por qué descartas otra. {F}",
        "Marta se relaciona con Penélope: ambas esperan y tejen. Lo dice la Fuente 1 (Carla Vega, 2022) y se ve en el relato. Nico se relaciona con Telémaco según la Fuente 3 (equipo docente, 2018). Descarto la Fuente 2 porque tiene seudónimo y contradice el relato.",
        ["responde la pregunta", "usa dos fuentes con referencia", "explica por qué descarta una"],
        ["cuatro oraciones escritas"],
        ["no anotar referencias", "usar la fuente débil como prueba"],
        "Pregunta: «¿Qué dato del relato apoya tu respuesta?»."),
    reinforce="Escribe una referencia con autor, título y año para un libro que tengas en casa.",
    extend="Escribe dos palabras clave y una pregunta para investigar a qué obra clásica recuerda un cuento que conozcas.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo contrastar fuentes que no coinciden y leo también lo que dicen el diseño, las imágenes y el audio de una fuente.",
    prior=["Sé evaluar autoría, fecha, propósito y respaldo.", "Sé qué es contrastar.", "Sé que una opinión no es un dato."],
    explain=[
        "Cuando dos fuentes dicen cosas distintas, hay que decidir cuál sirve. Primero evalúa cada una. Después busca una tercera fuente directa, como la página de créditos de una edición de la obra. La fuente que coincide con la edición y tiene autoría clara es más confiable.",
        "Una fuente no solo comunica con palabras. Los recursos no lingüísticos son el diseño, las imágenes, la disposición gráfica y los efectos de audio. Un titular enorme y rojo busca llamar la atención, una foto sin pie de foto no prueba nada y una música de suspenso crea emoción, no datos.",
        "Para evaluar una fuente, pregúntate qué hace cada recurso. ¿Ayuda a entender el dato o solo impresiona? Y mira dónde queda la información importante: una fuente que esconde el origen de sus datos en letra muy pequeña merece desconfianza.",
    ],
    vocab=[("diseño", "forma en que se arma una página: colores, letras y espacio"), ("disposición gráfica", "lugar que ocupa cada elemento en la página"), ("pie de foto", "texto breve que explica una imagen"), ("efecto de audio", "sonido añadido, como música o ruidos, que crea una emoción")],
    worked=[
        ("Contrastar con una fuente directa", "X: 1605 y 1615. Y: 1850. Z: página de créditos, primera parte, 1605.", ["X coincide con Z en 1605.", "Y no coincide.", "Además, Y no dice quién la hizo."], "La Fuente X es más confiable que la Y"),
        ("Leer un recurso no lingüístico", "Fuente Y: foto de un barco antiguo sin pie de foto.", ["La foto no tiene relación con el Quijote.", "Sin pie de foto no sabemos qué muestra."], "La imagen no aporta evidencia, solo adorno"),
    ],
    mistakes=[("Creer que una imagen prueba un dato.", "Una imagen sin explicación no demuestra nada.", "Busca el pie de foto y comprueba si la imagen se relaciona con el tema."),
              ("Dejarse llevar por un titular o una música llamativos.", "Esos recursos crean emoción, pero no demuestran datos.", "Separa lo que impresiona de lo que se puede comprobar.")],
    T=[
        ("abc", "{F} ¿Qué fuentes coinciden en la fecha de la primera parte del Quijote?", "La X y la Z, ambas con 1605", "La Y y la Z", "La X y la Y", "Solo X y Z entregan 1605."),
        ("{F} ¿En qué año se publicó la segunda parte del Quijote según la Fuente X? Escribe el número.", "1615", "La Fuente X indica 1615 para la segunda parte."),
        ("abc", "{F} ¿Cuál es la fuente más confiable?", "La X, firmada y coincidente con la edición impresa", "La Y, con música de suspenso", "Ninguna", "La X tiene autoría y coincide con la Fuente Z."),
        ("abc", "{F} ¿Por qué la Fuente Y es poco confiable?", "Es anónima y su dato contradice la edición impresa", "Tiene fecha 2021", "Menciona el Quijote", "Su dato no coincide con la fuente directa y no tiene autoría."),
        ("ab", "{F} ¿Qué busca el titular rojo con signos de exclamación en la Fuente Y?", "Llamar la atención y crear urgencia", "Entregar un dato comprobable", "Un titular grande no demuestra nada: busca impresionar."),
        ("abc", "{F} ¿Qué falta en la imagen del barco para que sirva como evidencia?", "Un pie de foto que explique qué muestra y su relación con el tema", "Más colores", "Que ocupe toda la pantalla", "Una imagen necesita una explicación para ser evidencia."),
        ("abc", "{F} ¿Dónde aparece la fuente de los datos en la Fuente Y?", "Al final, en letra muy pequeña", "En el titular", "Junto a la foto del barco", "La tabla de diseño dice que queda al final y en letra muy pequeña."),
        ("abc", "{F} ¿Qué efecto produce la música de suspenso y la voz grave de la Fuente Y?", "Crea tensión, pero no aporta datos", "Prueba que la información es cierta", "Confirma la fecha de la obra", "El audio crea una emoción y no una evidencia."),
        ("abc", "En Lengua y Literatura: ¿qué son los recursos no lingüísticos?", "Diseño, imágenes, disposición gráfica y efectos de audio", "Solo las palabras del texto", "Los números de página", "Son los elementos que comunican sin ser palabras."),
        ("ab", "{F} Un compañero dice: «Si el video tiene música dramática, entonces es más serio». ¿Qué le respondes?", "Que la música crea emoción, pero no demuestra que el dato sea cierto", "Que tiene razón", "La seriedad de una fuente depende de su autoría y de si se puede comprobar."),
        ("abc", "{F} ¿Qué se puede inferir de que el titular ocupe la mitad de la pantalla?", "Que el diseño prioriza impresionar sobre informar", "Que el dato es muy importante", "Que la fuente es de una editorial", "El espacio que ocupa un elemento muestra qué se quiere destacar."),
        ("abc", "{F} Si las fuentes X e Y dicen cosas distintas, ¿qué conviene hacer?", "Buscar una fuente directa, como la edición impresa, y contrastar", "Elegir la que me gusta más", "No usar ninguna fuente", "Una fuente directa permite decidir entre dos datos distintos."),
        ("ab", "{F} ¿Qué dato de apoyo sirve para detectar un error de la Fuente Y?", "Que Cervantes es el autor del Quijote", "Que el video es de 2021", "La Fuente Y dice que lo escribió Homero, pero el dato de apoyo dice Cervantes."),
    ],
    ctx=("abc", "Recibes un afiche con letras gigantes y rojas que dice «¡EXCLUSIVO!» y un dato sobre una obra, sin autor ni fecha. ¿Qué haces?", "Reviso el dato con una fuente firmada antes de usarlo", "Lo uso porque llama la atención", "Lo reenvío para que otros lo vean", "El diseño llamativo no prueba que el dato sea cierto."),
    sc=[("En Lengua y Literatura: ¿qué son los recursos no lingüísticos?", "Diseño, imágenes, disposición gráfica y efectos de audio", "Comunican con elementos que no son solo palabras."),
        ("¿Una imagen sin pie de foto prueba un dato?", "No", "Sin explicación no se sabe qué muestra."),
        ("¿Cómo decido entre dos fuentes que se contradicen?", "Contrasto con una fuente directa", "Una tercera fuente directa permite verificar cuál dato es correcto.")],
    op=("Con la ficha de la clase, haz una tabla de tres filas (X, Y, Z) y tres columnas (¿quién escribe?, ¿qué fecha da?, ¿es confiable?). Después escribe una frase sobre qué te dicen el diseño y el audio de la Fuente Y. {F}",
        "X: autora y fecha, 1605 y 1615, confiable. Y: anónima, 1850, no confiable. Z: edición impresa, 1605, confiable. El diseño de Y usa un titular enorme y música de suspenso para impresionar, pero no aporta datos.",
        ["tabla de tres filas con datos de la ficha", "indica cuáles son confiables", "interpreta un recurso no lingüístico"],
        ["una tabla y una frase"],
        ["decir que una fuente es mejor solo por su diseño", "no justificar"],
        "Pregunta: «¿Qué recurso busca impresionar y cuál entrega un dato?»."),
    reinforce="Describe en dos oraciones un afiche que hayas visto: qué dice el diseño y qué dato entrega.",
    extend="Haz una lista de tres cosas que debe tener una imagen para que sirva como evidencia en una investigación.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a una investigación de club de lectura: evalúo tres fuentes, incluida una de radio con efectos de audio, y respondo con referencias.",
    prior=["Sé evaluar fuentes con cuatro criterios.", "Sé que el audio crea emoción, no datos.", "Sé responder una pregunta con datos y referencias."],
    explain=[
        "Aplicamos lo aprendido en un club de lectura del barrio. La pregunta es qué símbolo comparten el mito del Minotauro y un relato sobre un hospital. Hay tres fuentes: una guía de lectura, una transcripción de radio y unos apuntes del club.",
        "En una transcripción de radio las anotaciones entre corchetes indican sonidos, como música o truenos. Esos efectos crean un ambiente, pero no son evidencia. Para evaluar una fuente de audio, separa lo que se afirma con palabras de lo que solo busca emocionar.",
        "Al terminar, tu respuesta debe tener tres partes: una frase que responda la pregunta, dos datos de fuentes confiables con su referencia y una frase sobre lo que no pudiste comprobar. Decir qué no sabes es parte de una buena investigación.",
    ],
    vocab=[("transcripción", "texto que escribe lo que se dijo en un audio"), ("anotación de sonido", "indicación entre corchetes de música o ruidos"), ("evidencia", "dato que se puede comprobar y apoya una respuesta"), ("limitación", "lo que no se pudo comprobar o saber")],
    worked=[
        ("Separar dato y efecto", "Fuente 2: [música de suspenso] «El laberinto esconde un secreto terrible». [efecto de trueno]", ["La música y el trueno son efectos de audio.", "La frase habla de un «secreto» sin decir cuál."], "Hay emoción, pero ningún dato comprobable"),
        ("Responder con evidencia", "Fuentes 1 y 3 coinciden en que el hilo guía a Teseo y la línea guía a Rosa.", ["Fuente 1: el hilo permite volver.", "Fuente 3: la línea amarilla guía a Rosa.", "El relato confirma que la línea lleva a la oficina."], "Símbolo compartido: una guía que permite orientarse"),
    ],
    mistakes=[("Usar la frase llamativa de la radio como dato.", "La frase no entrega ninguna información comprobable.", "Cita solo lo que se pueda comprobar."),
              ("No decir qué quedó sin comprobar.", "Toda investigación tiene límites.", "Agrega una frase que diga lo que falta por averiguar.")],
    T=[
        ("abc", "{F} ¿Qué fuente tiene autoría y fecha claras?", "La Fuente 1, con su equipo editor y el año 2021", "La Fuente 2, la de radio", "Ninguna", "La Fuente 1 se identifica con su equipo editor y su año."),
        ("{F} ¿Cuántos efectos de audio se anotan entre corchetes en la Fuente 2? Escribe el número.", "2", "Se anotan la música de suspenso y el efecto de trueno."),
        ("abc", "{F} ¿Qué dato aporta la Fuente 1 sobre el mito?", "Que el hilo de Ariadna permite a Teseo volver del laberinto", "Que el laberinto esconde un secreto", "Que Rosa llega a la oficina", "Es un dato comprobable sobre la historia del mito."),
        ("abc", "{F} ¿Qué afirma de verdad la Fuente 2 sobre el laberinto?", "Casi nada comprobable: habla de un secreto sin explicarlo", "Que Teseo usó un hilo", "Que Rosa se perdió", "La frase crea suspenso, pero no entrega datos."),
        ("ab", "{F} ¿Para qué sirven la música de suspenso y el trueno de la Fuente 2?", "Crear un ambiente de misterio", "Probar que el secreto existe", "Los efectos de audio buscan emocionar y no demuestran nada."),
        ("abc", "{F} ¿Qué símbolo comparten el mito y «El pasillo amarillo» según las Fuentes 1 y 3?", "Una guía que permite orientarse y volver", "Un monstruo escondido", "Una caja con males", "El hilo y la línea cumplen la función de guía."),
        ("abc", "{F} ¿Qué dato del relato respalda a la Fuente 3?", "La línea amarilla lleva a Rosa hasta la oficina de exámenes", "Rosa se pierde por segunda vez", "La funcionaria escribe una carta", "Confirma que la línea cumple la función de guía."),
        ("ab", "{F} ¿Qué fuente conviene NO usar como evidencia?", "La Fuente 2, porque solo emociona y no entrega datos", "La Fuente 1, porque está firmada", "Una transcripción sin datos comprobables no sirve de prueba."),
        ("abc", "¿Qué partes debe tener una buena respuesta de investigación?", "Respuesta, datos con referencia y lo que no se pudo comprobar", "Solo mi opinión", "Solo una imagen", "Una buena respuesta incluye respuesta, evidencia y también sus limitaciones."),
        ("abc", "{F} ¿Cuál sería una referencia adecuada para la Fuente 1?", "Equipo editor del centro cultural, guía de lectura, 2021", "Radio, hoy", "Anónimo, sin fecha", "Incluye autoría, tipo de texto y año."),
        ("ab", "{F} ¿Qué limitación se puede declarar al terminar la investigación?", "Que solo se revisaron tres fuentes y no se consultó una edición completa del mito", "Que todo quedó comprobado sin dudas", "Reconocer lo que no se revisó es parte de una investigación honesta."),
        ("abc", "{F} Un compañero cita la frase «El laberinto esconde un secreto terrible» como dato. ¿Qué le respondes?", "Que es una frase de efecto, no un dato comprobable", "Que está bien porque la dijo un locutor", "Que prueba que el mito es peligroso", "Un dato debe poder comprobarse en una fuente confiable."),
        ("abc", "{F} ¿Por qué conviene contrastar las Fuentes 1 y 3?", "Porque coinciden en la función de guía y se refuerzan", "Porque dicen lo contrario", "Porque son iguales en todo", "Dos fuentes con respaldo que coinciden dan más seguridad."),
    ],
    ctx=("abc", "En la radio de tu barrio un locutor dice, con música de fondo, que una obra clásica «cambió el mundo» sin dar ningún dato. ¿Qué haces si quieres usarlo en tu investigación?", "Busco una fuente firmada que lo compruebe", "Lo uso tal cual porque suena convincente", "Lo repito en el club sin revisar", "Una frase de efecto no equivale a un dato."),
    sc=[("En Lengua y Literatura: ¿qué es una transcripción?", "Un texto que escribe lo que se dijo en un audio", "Permite estudiar un audio por escrito."),
        ("¿Los efectos de audio son evidencia?", "No: crean un ambiente", "Esos efectos no entregan datos que se puedan comprobar."),
        ("¿Por qué declaro una limitación?", "Porque muestra qué falta por comprobar", "Decir lo que no sé hace honesta mi investigación.")],
    op=("Escribe una respuesta de investigación de cinco oraciones: responde la pregunta, usa dos fuentes con su referencia, explica por qué no usas la radio como evidencia y declara una limitación. {F}",
        "El hilo y la línea amarilla comparten la función de guía. Lo dice la Fuente 1 (equipo editor, 2021) y la Fuente 3 (monitora del club, 2023). No uso la radio porque solo crea suspenso con música y trueno. Los datos de «El pasillo amarillo» confirman que la línea lleva a la oficina. No revisé una edición completa del mito.",
        ["responde la pregunta", "usa dos fuentes con referencia", "descarta la radio con razón", "declara una limitación"],
        ["cinco oraciones escritas"],
        ["usar la frase de la radio como dato", "no declarar una limitación"],
        "Pregunta: «¿Qué quedó sin comprobar en tu investigación?»."),
    reinforce="Anota un programa o video que conozcas que use mucha música dramática y di qué dato concreto entrega.",
    extend="Escribe un párrafo corto que explique a otra persona por qué los efectos de audio no son evidencia.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso una investigación completa, detecto lo que le falla y decido cómo mejorarla.",
    prior=["Sé evaluar fuentes.", "Sé responder con datos y referencias.", "Sé declarar una limitación."],
    explain=[
        "Revisar una investigación es mirar sus partes. Pregunta: ¿se puede responder con fuentes? Fuentes: ¿hay más de una y son confiables? Conclusión: ¿se apoya en datos o exagera? Referencias: ¿dice de dónde sacó cada dato?",
        "Una conclusión exagerada usa palabras como «todos», «nadie» o «siempre» sin pruebas. Una investigación sólida usa expresiones medidas, como «en este relato» o «según las fuentes revisadas», y reconoce lo que no pudo comprobar. Quien solo busca lo que confirma lo que ya piensa tiene un sesgo.",
        "Al revisar, decide el siguiente paso con claridad: buscar otra fuente, corregir la conclusión, agregar referencias o comparar de nuevo con el texto. Con eso la investigación mejora sin empezar de cero.",
    ],
    vocab=[("generalización", "afirmar algo de todos los casos con pocos datos"), ("conclusión medida", "afirmación que no dice más de lo que prueban los datos"), ("revisar", "mirar de nuevo para corregir"), ("sesgo", "inclinación a ver solo lo que confirma lo que uno piensa")],
    worked=[
        ("Detectar una generalización", "Conclusión de Jaime: «Todos los cuentos modernos copian la Odisea».", ["Usa «todos» sin pruebas.", "Solo revisó un relato."], "Es una generalización: no se puede afirmar de todos"),
        ("Corregir con una conclusión medida", "Datos: Marta teje y suelta vueltas; Penélope teje y deshace.", ["Se parecen en el gesto de tejer y deshacer.", "Hay que decir «en este relato»."], "«En este relato, Marta repite el gesto de Penélope»"),
    ],
    mistakes=[("Usar «todos» o «siempre» con una sola fuente.", "Una fuente no basta para hablar de todos los casos.", "Usa «en este relato» o «según esta fuente»."),
              ("Entregar la investigación sin referencias.", "Sin referencias no se puede comprobar.", "Anota autor, título y año de cada fuente.")],
    T=[
        ("abc", "{F} ¿Cuántas fuentes consultó Jaime?", "Una", "Dos", "Tres", "El informe dice «un blog sin autor»."),
        ("abc", "{F} ¿Qué problema tiene la fuente que usó Jaime?", "No tiene autor, así que no se puede comprobar", "Tiene demasiadas fotos", "Es de este año", "Sin autoría no se puede evaluar su confiabilidad."),
        ("abc", "{F} ¿Qué palabra de la conclusión muestra una generalización?", "Todos", "Cuentos", "Nada", "«Todos» afirma algo de todos los casos."),
        ("ab", "{F} ¿Qué falta al final del informe de Jaime?", "Referencias", "Un dibujo", "El informe dice «Referencias: ninguna», así que nadie puede comprobar los datos."),
        ("abc", "{F} ¿Qué dato del relato permite una conclusión apoyada?", "Marta teje un chaleco y suelta vueltas cada noche mientras espera", "Jaime escribió el informe", "Hugo es el esposo de Marta", "Es un dato del relato que se compara con Penélope."),
        ("abc", "{F} ¿Qué conclusión medida puede escribir Jaime?", "En este relato, Marta repite el gesto de Penélope de tejer y deshacer mientras espera", "Todos los relatos repiten la Odisea", "Los cuentos no tienen nada propio", "Usa un dato del relato y limita el alcance."),
        ("abc", "En Lengua y Literatura: ¿qué es una generalización?", "Afirmar algo de todos los casos con pocos datos", "Resumir un texto", "Citar a un autor con comillas", "Una generalización dice más de lo que prueban los datos."),
        ("{F} ¿Cuántas referencias entregó Jaime? Escribe el número.", "0", "El informe dice «Referencias: ninguna», es decir, cero fuentes anotadas."),
        ("abc", "{F} Si Jaime quiere mejorar su informe, ¿cuál es el mejor primer paso?", "Buscar al menos otra fuente firmada y contrastarla", "Borrar la pregunta", "Cambiar «todos» por «muchísimos» y listo", "Contrastar con una fuente confiable corrige el problema principal."),
        ("ab", "{F} Beatriz dice que el informe está bien porque la conclusión suena segura. ¿Qué le respondes?", "Que una conclusión segura sin pruebas no es sólida", "Que tiene razón", "La solidez depende de los datos y no del tono seguro."),
        ("abc", "{F} ¿Qué parte del informe sí está bien planteada?", "La pregunta, porque se puede responder con fuentes y con el relato", "La conclusión", "Las referencias", "La pregunta es investigable porque se responde con fuentes y con el relato."),
        ("abc", "¿Qué revisión haces primero al leer una investigación?", "Si la pregunta se responde con fuentes confiables", "Si tiene letras grandes", "Si tiene fotos", "Todo parte de que las fuentes respalden la respuesta."),
        ("abc", "{F} ¿Qué debe agregar Jaime para declarar una limitación?", "Que solo revisó una fuente y no pudo contrastarla", "Que todo está probado", "Que nadie puede comprobar", "Declarar la limitación es reconocer lo que falta."),
    ],
    ctx=("abc", "Un vecino te muestra su informe para el club con la conclusión «siempre los hijos buscan a sus padres en los libros». Solo leyó dos obras. ¿Qué le sugieres?", "Cambiarlo por «en estas dos obras» y agregar referencias", "Dejarlo igual porque suena bien", "Borrar el informe", "Una conclusión medida se limita a lo que se revisó."),
    sc=[("En Lengua y Literatura: ¿qué palabras suelen delatar una generalización?", "Todos, nadie y siempre", "Esas palabras afirman algo de todos los casos."),
        ("¿Qué cuatro partes reviso en una investigación?", "Pregunta, fuentes, conclusión y referencias", "Son las partes que se evalúan."),
        ("¿Qué es una conclusión medida?", "La que no dice más de lo que prueban los datos", "Una conclusión medida se limita solo a lo que está comprobado.")],
    op=("Reescribe la conclusión de Jaime en dos oraciones con una conclusión medida, agrega una limitación y escribe qué hará él para mejorar su informe. {F}",
        "En este relato, Marta repite el gesto de Penélope de tejer y deshacer mientras espera. Solo revisé una fuente. Jaime buscará una fuente firmada, anotará las referencias y contrastará.",
        ["usa una expresión medida", "declara una limitación", "propone una mejora concreta"],
        ["dos o tres oraciones escritas"],
        ["mantener «todos» o «siempre»", "no proponer una mejora"],
        "Pregunta: «¿Qué dato apoya tu conclusión?»."),
    reinforce="Cambia esta frase por una más medida: «Todos los cuentos viejos son iguales».",
    extend="Escribe una lista de cinco pasos que seguirías para investigar a qué obra recuerda un relato, desde la pregunta hasta las referencias.",
)

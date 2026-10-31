"""Cuaderno del estudiante, 6.º básico Historia, Geografía y Ciencias Sociales: OA 26 (informarse y opinar por medio de periódicos y TIC)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI06 OA 26"
MAT = "Lápiz y papel. Las noticias, los mensajes y los datos son inventados y están escritos en cada ejercicio; no necesitas internet ni un periódico."

# ---------------------------------------------------------------- Clase 1
NOT1 = "«Sección Medioambiente. Valle Claro, 12 de marzo. TITULAR: Vecinos plantan 200 árboles en el parque. BAJADA: La actividad se hizo el 9 de marzo con 40 voluntarios. CUERPO: Cada voluntario plantó 5 árboles en la ladera del parque, con ayuda de la municipalidad.»"
build(
    OA, 1, "",
    use="Aprenderé a ubicar una noticia en el periódico y en el tiempo y el espacio: sección, fecha, lugar y alcance. Sirve para informarme sobre temas del país y del mundo en un periódico o en internet.",
    prior=["Sé distinguir un hecho de una opinión.", "Sé leer fechas y calcular días entre dos fechas.", "Sé que una fuente tiene procedencia."],
    explain=[
        "Un periódico o diario reúne noticias de distintos temas. Está dividido en secciones, por ejemplo política, medioambiente, deportes y arte y música. Las TIC, que son las tecnologías de la información y la comunicación, como internet, los celulares y los computadores, también permiten leer periódicos digitales. En ambos casos las noticias se organizan de forma parecida.",
        "Una noticia tiene partes. El titular es el título en letras grandes y resume lo central. La bajada es una frase breve que amplía el titular. El cuerpo entrega los detalles. También aparecen la fecha, el lugar donde ocurrió y, a veces, quién la escribió. La fecha importa porque una noticia vieja puede no describir la situación de hoy.",
        "Además ubico el alcance de la noticia. Puede ser local, si ocurre en un barrio o una comuna; nacional, si ocurre en el país o afecta a todo Chile; o mundial, si ocurre en otro país o afecta a muchos países. Antes de opinar leo la noticia completa y no me quedo solo con el titular.",
    ],
    vocab=[("titular", "título de una noticia que resume lo central"), ("bajada", "frase breve que amplía el titular"), ("sección", "parte del periódico dedicada a un tema"), ("TIC", "tecnologías de la información y la comunicación, como internet y celulares"), ("alcance", "hasta dónde llega una noticia: local, nacional o mundial")],
    worked=[
        ("Ubicar una noticia", "«Sección Deportes. Puerto Sur, 3 de octubre. TITULAR: Equipo escolar gana el torneo de natación. BAJADA: La final se nadó el 1 de octubre. CUERPO: El equipo ganó cuatro pruebas.» ¿En qué sección está y en qué fecha se publicó?",
         ["Busco la sección: Deportes.", "Busco la fecha de publicación: 3 de octubre."], "Sección Deportes; 3 de octubre"),
        ("Reconocer el alcance", "Una noticia cuenta que en una plaza de Valle Claro se arregló un juego infantil. ¿Cuál es su alcance?",
         ["Pienso dónde ocurre: una plaza de una comuna.", "Solo afecta a ese lugar."], "Local"),
    ],
    mistakes=[
        ("Leer solo el titular y opinar.", "El titular resume y puede dejar fuera datos importantes.", "Lee el cuerpo completo antes de opinar."),
        ("No revisar la fecha de la noticia.", "Una noticia antigua puede no reflejar la situación actual.", "Anota siempre la fecha y el lugar."),
    ],
    T=[
        ("En un periódico, ¿qué es el titular?", "El título que resume lo central de la noticia", "Está en letras grandes."),
        ("¿Qué es una sección de un periódico?", "Una parte dedicada a un tema, como deportes o política", "Ordena las noticias por tema."),
        ("¿Qué significa la sigla TIC?", "Tecnologías de la información y la comunicación", "Incluye internet y celulares."),
        ("¿Por qué una noticia muestra el lugar donde ocurrió el hecho?", "Para saber dónde pasó y a quiénes afecta", "El lugar ubica la información."),
        ("¿Por qué conviene revisar la fecha de una noticia?", "Porque una noticia vieja puede no describir la situación de hoy", "Los hechos cambian con el tiempo."),
        ("¿Qué diferencia hay entre una noticia local y una mundial?", "La local ocurre en un lugar cercano y la mundial afecta a varios países", "Se distinguen por su alcance."),
        (NOT1 + " ¿En qué sección se publicó esta noticia?", "Medioambiente", "Aparece al comienzo del texto."),
        ("=", "Según la noticia, 40 voluntarios plantaron 5 árboles cada uno. ¿Cuántos árboles plantaron en total?", "40*5", "Se multiplican los voluntarios por los árboles de cada uno."),
        (NOT1 + " ¿Cuál es el alcance de la noticia: local, nacional o mundial?", "Local", "Ocurrió en un parque de una comuna."),
        ("Julia lee una noticia del año pasado y la comenta como si fuera de hoy. ¿Qué dato de ubicación revisó mal?", "La fecha", "No comprobó cuándo se publicó."),
        ("En una noticia, ¿en qué parte buscas todos los detalles del hecho: en el titular o en el cuerpo?", "En el cuerpo", "El cuerpo entrega los detalles; el titular solo resume."),
        ("Une cada titular con su sección: 1) «El Congreso votó una ley», 2) «El río aumentó su caudal por las lluvias», 3) «El equipo ganó 3 a 1». Opciones: política, medioambiente, deportes.", "1 política, 2 medioambiente, 3 deportes", "Cada titular corresponde a su tema."),
        ("=", "La actividad ocurrió el 9 de marzo y la noticia se publicó el 12 de marzo. ¿Cuántos días pasaron entre ambas fechas?", "12-9", "Se resta la fecha del hecho a la de publicación."),
    ],
    ctx=("Un compañero te cuenta un hecho y dice: «Lo vi en un titular del celular». Tú no viste la noticia. ¿Qué dos datos de ubicación le pides antes de opinar?", "La fecha y el lugar de la noticia", "Ubican la información."),
    sc=[("En Historia: ¿qué es una sección de un periódico?", "Una parte dedicada a un tema", "Ordena las noticias."),
        ("¿Cuáles son los tres alcances de una noticia?", "Local, nacional y mundial", "Dicen hasta dónde llega."),
        ("¿Qué partes tiene una noticia?", "Titular, bajada y cuerpo", "Organizan la información.")],
    op=("Lee estos tres titulares inventados: A) «Orquesta juvenil de Valle Claro estrena concierto en la plaza» (12 de abril); B) «Selección nacional de básquetbol clasificó a un torneo mundial» (3 de mayo); C) «Se aprobó una ley que cambia los horarios de las micros en todo el país» (20 de junio). Para cada uno escribe la sección posible (arte y música, deportes o política), el alcance (local, nacional o mundial) y la fecha. Elige uno y escribe una pregunta que le harías a la noticia completa.",
        "A: arte y música, local, 12 de abril. B: deportes, nacional o mundial, 3 de mayo. C: política, nacional, 20 de junio. Elijo A: ¿cuántas personas asistieron al concierto?",
        ["ubica sección, alcance y fecha de cada titular", "formula una pregunta pertinente"], ["una tabla con tres titulares y una pregunta"], ["leer solo el titular", "olvidar la fecha"], "Pide a una persona de tu casa que lea tus tres filas y comente si las secciones son correctas."),
    reinforce="Mira un periódico o un sitio de noticias con una persona de tu casa y encuentra una fecha, una sección y un titular.",
    extend="Escribe un titular y una bajada para un hecho real de tu curso.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
TEXTOS = "Texto A (noticia): «Valle Claro, 14 de abril. La directora del Servicio de Parques informó que el parque tendrá nuevos bebederos desde mayo. Redacción del diario Valle Claro Hoy.» Texto B (mensaje reenviado): «URGENTE. Mañana cierran todos los colegios de Chile. Reenvía a 10 contactos.» Texto C (columna): «Opinión: creo que el parque es lo mejor de la ciudad.»"
build(
    OA, 2, "",
    use="Aprenderé a revisar de dónde viene una noticia o un mensaje y a distinguir noticia, opinión y desinformación. Sirve para informarme con cuidado en periódicos e internet.",
    prior=["Sé ubicar una noticia: sección, fecha y lugar.", "Sé distinguir hechos de opiniones.", "Sé revisar la procedencia de una fuente."],
    explain=[
        "Una noticia informa hechos: qué pasó, dónde, cuándo y quiénes participaron. Una opinión, como una columna o una carta al director, expresa lo que piensa su autor. Las dos son válidas, pero no son lo mismo. En una noticia importa la fuente, que es la persona o documento de donde sale el dato, como un funcionario, un testigo o un informe.",
        "La desinformación es información falsa o engañosa que se difunde. Circula mucho en mensajes reenviados por las TIC. Las señales de alerta son: no tiene autor ni fecha, usa palabras como «urgente», pide reenviar a muchas personas, tiene un titular exagerado o no cita ninguna fuente. Si veo alguna, no la comparto antes de verificar.",
        "Para verificar busco la fuente original, es decir, de dónde sale primero el dato. Luego comparo con otros medios confiables. Si dos medios dan datos distintos, no opino todavía y reviso una tercera fuente. También protejo a las personas: no comparto datos personales, como teléfonos o direcciones, sin permiso.",
    ],
    vocab=[("noticia", "texto que informa hechos recientes"), ("opinión", "texto que expresa lo que piensa su autor"), ("fuente", "persona o documento de donde sale un dato"), ("desinformación", "información falsa o engañosa que se difunde"), ("verificar", "comprobar si un dato es cierto")],
    worked=[
        ("Noticia u opinión", "«El gimnasio abrirá a las 8:00, informó la dirección» y «Creo que el gimnasio es muy bonito». ¿Cuál es la opinión?",
         ["Busco la frase que dice lo que alguien piensa.", "«Creo que…» expresa una opinión."], "La segunda"),
        ("Señales de alerta", "«ÚLTIMA HORA: se acabó el agua en todo el país. Compártelo ya». ¿Qué señales de alerta tiene?",
         ["No tiene autor ni fecha.", "Usa urgencia y pide compartir sin verificar."], "Sin autor ni fecha, urgencia y pedido de compartir"),
    ],
    mistakes=[
        ("Compartir un mensaje solo porque dice «urgente».", "La urgencia presiona para no verificar.", "Verifica la fuente antes de compartir."),
        ("Creer que una columna de opinión es una noticia.", "La columna expresa lo que piensa su autor.", "Pregunta si el texto informa hechos o da una opinión."),
    ],
    T=[
        ("¿Qué diferencia hay entre una noticia y una opinión?", "La noticia informa hechos y la opinión expresa lo que piensa su autor", "Tienen funciones distintas."),
        ("¿Qué es la fuente de una noticia?", "La persona o documento de donde sale el dato", "Permite comprobar el dato."),
        ("¿Qué es la desinformación?", "Información falsa o engañosa que se difunde", "Puede circular por mensajes."),
        ("¿Por qué un mensaje que pide reenviar a 10 contactos es sospechoso?", "Porque presiona a difundirlo sin verificar", "La prisa evita la comprobación."),
        ("¿Por qué conviene buscar la fuente original de un dato?", "Para comprobar de dónde viene primero", "Así se verifica."),
        ("¿Por qué un titular muy exagerado puede ser una señal de alerta?", "Porque puede llamar la atención sin informar con exactitud", "Los hechos reales suelen ser más precisos."),
        (TEXTOS + " ¿Cuál es una noticia con fuente identificada?", "El texto A", "Cita a la directora del Servicio de Parques."),
        (TEXTOS + " ¿Cuál es una opinión?", "El texto C", "Comienza diciendo «creo que»."),
        ("¿Cuál de estas NO es una señal de alerta en un mensaje: A) no tiene autor, B) pide reenviar rápido, C) cita una fuente identificable?", "C", "Citar la fuente ayuda a verificar."),
        ("El Medio 1 dice que el festival fue el 5 de mayo y el Medio 2 dice que fue el 15 de mayo. ¿Qué haces antes de opinar?", "Reviso una tercera fuente o la fuente original", "Los datos se contradicen."),
        ("Tomás quiere compartir un mensaje que incluye el número de teléfono de un vecino. ¿Debe hacerlo sin permiso?", "No", "Compartir datos personales expone a una persona."),
        ("=", "El Medio 1 dice que asistieron 300 personas y el Medio 2 dice que asistieron 3.000. ¿Cuántas veces mayor es la segunda cifra?", "3000//300", "Se divide 3.000 en 300."),
        ("Ordena los pasos ante una noticia sospechosa: A) buscar la fuente original, B) comparar con otro medio confiable, C) decidir si compartir, D) leerla completa sin quedarse en el titular.", "D, A, B, C", "Primero leer, luego verificar y por último decidir."),
    ],
    ctx=("Recibes por una aplicación de mensajes: «Dicen que mañana no habrá clases. Pásalo a todos». No sabes quién lo escribió. ¿Qué haces primero?", "Verificar con una fuente confiable antes de compartirlo", "No se debe difundir sin comprobar."),
    sc=[("En Historia: ¿qué es desinformación?", "Información falsa o engañosa que se difunde", "Es la idea central."),
        ("¿Qué señales de alerta tiene un mensaje dudoso?", "No tiene autor ni fecha, usa urgencia o pide reenviar", "Son avisos para verificar."),
        ("¿Qué hacer si dos medios dan datos distintos?", "Buscar una tercera fuente", "Así no afirmo sin comprobar.")],
    op=("Lee estos tres textos inventados. Texto 1: «Valle Claro, 2 de junio. El municipio informó que se instalarán 12 bancas nuevas en la plaza durante junio. Fuente: oficio municipal.» Texto 2: mensaje sin autor: «URGENTE: la plaza será cerrada para siempre. Reenvía a todos». Texto 3: columna que dice «Opino que el municipio debería poner más bancas». Para cada uno escribe si es noticia, mensaje dudoso u opinión, y por qué. Luego escribe qué harías con el texto 2.",
        "Texto 1 es noticia: cita una fuente y una fecha. Texto 2 es mensaje dudoso: sin autor, sin fecha, urgencia y pide reenviar. Texto 3 es opinión: dice «opino». Con el texto 2 buscaría la fuente original y no lo compartiría.",
        ["clasifica los tres textos con razones", "indica qué hacer con el mensaje dudoso"], ["tres clasificaciones y una decisión"], ["compartir sin verificar", "confundir opinión con noticia"], "Muestra tu clasificación a una persona de tu casa y pregúntale si está de acuerdo."),
    reinforce="Pregunta a una persona de tu casa si ha recibido mensajes que pedían reenviar y qué hizo.",
    extend="Escribe tres señales de alerta que enseñarías a un amigo para detectar un mensaje dudoso.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
NOT3 = "«Valle Claro, 20 de junio. El Festival de Música Joven se suspendió ayer porque un temporal dejó el escenario sin energía eléctrica. La organización informó que las 600 entradas vendidas serán válidas para el nuevo día, el 4 de julio. Músicos y público lamentaron la decisión, pero los vecinos del sector dijeron sentirse más tranquilos por la seguridad.»"
build(
    OA, 3, "",
    use="Aprenderé a leer una noticia buscando quién, qué, cuándo, dónde, por qué y cómo, y a distinguir causas, consecuencias y reacciones de los actores. Sirve para comprender los temas del país y del mundo antes de opinar.",
    prior=["Sé ubicar una noticia en sección, fecha y lugar.", "Sé distinguir noticia, opinión y desinformación.", "Sé que un hecho tiene causas y consecuencias."],
    explain=[
        "Una noticia completa responde seis preguntas: ¿qué pasó?, ¿quién participó?, ¿cuándo?, ¿dónde?, ¿por qué? y ¿cómo? Las dos últimas llevan a las causas. La causa es la razón que explica por qué ocurrió el hecho. La consecuencia es lo que ocurre después. En una noticia de música, deporte, política o medioambiente se usan las mismas preguntas.",
        "Los actores son las personas o grupos que participan o son afectados. Cada actor puede reaccionar distinto. Un mismo hecho puede entristecer a unos y tranquilizar a otros. En una noticia hay datos, que se pueden comprobar, y declaraciones, que son lo que dicen los actores y pueden incluir opiniones. Por ejemplo, «600 entradas vendidas» es un dato, y «lamentaron la decisión» es una reacción.",
        "Para opinar con fundamentos separo los datos de las reacciones. Si alguien dice «la organización fue irresponsable» y la noticia no lo dice, es una opinión del lector, no un hecho de la noticia. Puedo opinar, pero debo apoyarme en lo que dice el texto. Así mi opinión respeta la información.",
    ],
    vocab=[("causa", "razón que explica por qué ocurrió un hecho"), ("consecuencia", "lo que ocurre después de un hecho"), ("actor", "persona o grupo que participa o es afectado"), ("dato", "información que se puede comprobar"), ("declaración", "lo que dice un actor sobre el hecho")],
    worked=[
        ("Encontrar la causa", "«Puerto Sur, 8 de mayo. La feria de libros se trasladó al gimnasio porque el patio quedó mojado por la lluvia.» ¿Por qué se trasladó la feria?",
         ["Busco la razón en el texto.", "Dice que el patio quedó mojado por la lluvia."], "Porque el patio quedó mojado por la lluvia"),
        ("Dato o declaración", "«El torneo tuvo 24 equipos» y «los jugadores dijeron que quedaron muy cansados». ¿Cuál es una declaración?",
         ["Busco lo que dicen los actores.", "La segunda recoge lo que dijeron los jugadores."], "La segunda"),
    ],
    mistakes=[
        ("Confundir la causa con la consecuencia.", "La causa ocurre antes y la consecuencia después.", "Pregunta qué pasó primero y qué pasó luego."),
        ("Tratar una reacción de un actor como un hecho comprobado.", "Una declaración muestra una mirada, no necesariamente un hecho.", "Marca qué es dato y qué es declaración."),
    ],
    T=[
        ("¿Cuáles son las seis preguntas básicas de una noticia?", "Qué, quién, cuándo, dónde, por qué y cómo", "Ordenan la lectura."),
        ("En Historia: ¿Qué es una causa?", "La razón que explica por qué ocurrió un hecho", "Responde a «por qué»."),
        ("¿Qué es una consecuencia?", "Lo que ocurre después de un hecho", "Viene luego de la causa."),
        ("¿Por qué conviene identificar a los actores de una noticia?", "Porque cada actor puede ser afectado o reaccionar distinto", "Así se entiende el hecho completo."),
        ("¿Qué diferencia hay entre un dato y una declaración?", "El dato se puede comprobar; la declaración es lo que dice un actor", "Una puede incluir opiniones."),
        ("¿Por qué conviene separar los datos de las reacciones antes de opinar?", "Para apoyar la opinión en lo que dice el texto", "Evita confundir hechos con reacciones."),
        (NOT3 + " ¿Cuál fue la causa de la suspensión del festival?", "Un temporal que dejó el escenario sin energía eléctrica", "Es la razón que da el texto."),
        ("=", "Se vendieron 600 entradas del festival a $5.000 cada una. ¿Cuántos pesos se recaudaron en total?", "600*5000", "Se multiplica el número de entradas por su precio."),
        (NOT3 + " ¿Cuál es la nueva fecha del festival?", "El 4 de julio", "La organización la informó."),
        (NOT3 + " ¿Qué grupo dijo sentirse más tranquilo y por qué?", "Los vecinos, por la seguridad", "Lo dice el último párrafo."),
        (NOT3 + " Un lector dice: «La organización fue irresponsable». ¿Es un hecho de la noticia o una opinión del lector?", "Una opinión del lector", "La noticia no lo dice."),
        ("=", "El festival se suspendió el 19 de junio y la nueva fecha es el 4 de julio. ¿Cuántos días pasan desde el 20 de junio hasta el 4 de julio, sabiendo que junio tiene 30 días?", "(30-20)+4", "Hasta fin de junio pasan 10 días y hasta el 4 de julio, 4 más."),
        ("Ordena la cadena de hechos: A) el escenario quedó sin energía, B) se suspendió el festival, C) un temporal golpeó la zona.", "C, A, B", "Primero el temporal, luego el corte y después la suspensión."),
    ],
    ctx=("En tu comuna se suspendió un campeonato escolar de fútbol porque la cancha estaba inundada. Los jugadores quedaron tristes y los vecinos aplaudieron la decisión por seguridad. ¿Cuál es la causa de la suspensión?", "La cancha inundada", "Es la razón por la que se suspendió."),
    sc=[("En una noticia, ¿qué pregunta ayuda a encontrar la causa de un hecho?", "¿Por qué ocurrió?", "La causa responde a «por qué»."),
        ("¿Qué es un actor en una noticia?", "Una persona o grupo que participa o es afectado", "Son quienes viven el hecho."),
        ("¿Qué diferencia hay entre dato y declaración?", "El dato se puede comprobar y la declaración es lo que dice alguien", "Se tratan de forma distinta.")],
    op=("Lee esta noticia inventada: «Valle Claro, 5 de agosto. La carrera de bicicletas se realizó el domingo con 80 participantes. La ganadora llegó en 42 minutos. El municipio informó que cerró dos calles durante la carrera. Algunos comerciantes dijeron que perdieron ventas, mientras otros dijeron que vendieron más.» Responde por escrito: qué, quién, cuándo, dónde, una consecuencia, dos actores con reacciones distintas. Luego escribe una opinión que se apoye en un dato del texto.",
        "Qué: carrera de bicicletas. Quién: 80 participantes. Cuándo: domingo. Dónde: Valle Claro. Consecuencia: dos calles cerradas. Actores: comerciantes que perdieron ventas y comerciantes que vendieron más. Opino que se podría repetir porque participaron 80 personas.",
        ["responde las preguntas básicas", "nombra dos actores con reacciones distintas", "opina con un dato del texto"], ["una ficha de lectura y una opinión con dato"], ["confundir reacción con hecho", "opinar sin un dato"], "Lee tu ficha a una persona de tu casa y pídele que encuentre el dato que usaste."),
    reinforce="Escribe una noticia de tres líneas sobre algo ocurrido en tu casa esta semana, con qué, quién, cuándo y dónde.",
    extend="Escribe la causa y dos consecuencias de un hecho real de tu escuela.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
MEDIOS = "Medio 1, titular: «Éxito rotundo: miles llenaron el parque en el festival del barrio». Cuerpo: «Asistieron 800 personas, según la organización». Medio 2, titular: «Festival del barrio dejó el parque lleno de basura». Cuerpo: «Se recogieron 90 bolsas de basura después del evento, según el municipio»."
build(
    OA, 4, "",
    use="Aprenderé a comparar cómo dos medios cuentan el mismo hecho y a opinar con fundamentos y respeto en espacios digitales. Sirve para informarme mejor y no quedarme con una sola mirada.",
    prior=["Sé separar datos de declaraciones.", "Sé revisar la fuente de una noticia.", "Sé que cada actor tiene una perspectiva."],
    explain=[
        "Dos medios pueden contar el mismo hecho de formas distintas. Cada uno puede destacar datos diferentes, usar palabras con juicios y omitir, o sea dejar fuera, información. El lenguaje cargado es el que usa palabras que expresan un juicio, como «éxito rotundo» o «desastre», en vez de describir con datos. Por eso, para informarme, comparo al menos dos medios.",
        "Al comparar reviso tres cosas: qué datos entrega cada uno, de qué fuente los saca y qué palabras usa para valorar. Cuando los datos son exagerados, como decir «miles» si la fuente dice 800, lo noto. Después busco lo que ambos medios dicen igual y lo que se contradice, y recién ahí opino, apoyándome en los datos.",
        "Al opinar en espacios digitales uso la netiqueta, que son las normas de respeto al escribir en línea. Critico ideas, no insulto a personas, no comparto datos personales y no difundo información sin verificar. Una buena opinión escrita dice qué pienso, qué dato la apoya y de qué fuente viene. Si aparece una razón mejor, puedo cambiar de opinión.",
    ],
    vocab=[("lenguaje cargado", "palabras que expresan un juicio en vez de describir con datos"), ("omitir", "dejar fuera información"), ("perspectiva", "manera de contar o mirar un hecho"), ("netiqueta", "normas de respeto al escribir en línea"), ("contrastar", "comparar varias fuentes sobre lo mismo")],
    worked=[
        ("Detectar lenguaje cargado", "«Gran triunfo histórico del equipo» y «El equipo ganó 3 a 1». ¿Cuál usa lenguaje cargado?",
         ["Busco palabras que juzgan.", "«Gran triunfo histórico» es un juicio."], "La primera"),
        ("Comprobar una exageración", "Un titular dice «multitud en la feria» y el cuerpo dice que asistieron 35 personas. ¿Qué detectas?",
         ["Comparo el titular con el dato.", "35 personas no son una multitud."], "El titular exagera"),
    ],
    mistakes=[
        ("Informarse con un solo medio.", "Un medio puede destacar solo una parte del hecho.", "Compara al menos dos medios."),
        ("Insultar a quien piensa distinto en un comentario en línea.", "Ataca a la persona y no responde la idea.", "Responde a la idea con respeto y con un dato."),
    ],
    T=[
        ("¿Qué es el lenguaje cargado en una noticia?", "El que usa palabras que expresan un juicio en vez de describir con datos", "Valora en vez de informar."),
        ("¿Qué significa omitir información en una noticia?", "Dejar fuera datos", "Puede cambiar cómo se entiende el hecho."),
        ("¿Qué es la netiqueta?", "Normas de respeto al escribir en línea", "Cuida la convivencia digital."),
        ("¿Por qué dos medios pueden titular distinto un mismo hecho?", "Porque destacan datos o enfoques distintos", "Cada uno elige qué mostrar."),
        ("¿Por qué conviene comparar al menos dos medios?", "Para no quedarse con una sola mirada", "Contrastar da una visión más completa."),
        ("¿Por qué una opinión en línea debe criticar ideas y no personas?", "Porque insultar no responde la razón y falta el respeto", "La netiqueta lo exige."),
        (MEDIOS + " ¿Cuál titular usa un juicio como «éxito rotundo»?", "El del Medio 1", "La expresión valora el festival."),
        (MEDIOS + " ¿Qué dato muestra que «miles» exagera?", "Que asistieron 800 personas", "800 no llega a miles."),
        ("=", "Si cada una de las 90 bolsas de basura del festival pesó 4 kilos, ¿cuántos kilos de basura se recogieron?", "90*4", "Se multiplica el número de bolsas por su peso."),
        ("¿Qué pregunta ayuda más a opinar con fundamentos sobre el festival: A) ¿cuál medio es más famoso?, B) ¿qué fuente da cada dato y qué dato aporta?", "B", "Se revisa la fuente y el dato."),
        ("Un comentario en línea dice «los organizadores son unos inútiles». ¿Cuál es una mejor versión: A) «Creo que faltó planificar cómo recoger la basura», B) «Qué gente tan mala»?", "A", "Critica la idea y da una razón."),
        ("Ordena el proceso: A) comparar qué datos coinciden y cuáles se contradicen, B) leer ambos medios completos, C) escribir una opinión con datos, D) identificar la fuente de cada dato.", "B, D, A, C", "Primero se lee, luego se compara y al final se opina."),
        ("Una sequía aparece en el diario de una zona agrícola del norte y en el de una ciudad lluviosa del sur. ¿Por qué pueden destacarla distinto?", "Porque a cada lector lo afecta de distinta forma", "El territorio cambia la importancia."),
    ],
    ctx=("En el chat del curso alguien escribe: «Ese deportista es un fracasado». Otra persona quiere responder. ¿Qué es mejor: atacar a quien lo escribió o dar un dato sobre los resultados del deportista?", "Dar un dato sobre los resultados", "Se responde a la idea con evidencia."),
    sc=[("En Historia: ¿qué es lenguaje cargado?", "Palabras que expresan un juicio en vez de describir con datos", "Es la idea de la clase."),
        ("¿Qué se revisa al comparar dos medios?", "Datos, fuentes y palabras que valoran", "Permiten contrastar las versiones."),
        ("¿Qué debe cuidar una opinión escrita en línea?", "Criticar ideas con respeto y apoyarse en datos", "Es lo que pide la netiqueta.")],
    op=("Lee: Medio A, «Gran victoria del Colegio Norte en atletismo: ganó 6 de 10 pruebas». Medio B, «Colegio Sur perdió por solo 2 puntos y fue el mejor en velocidad». Datos: Norte 62 puntos y Sur 60 puntos. Escribe qué palabras valoran en cada titular, qué dato coincide en ambos medios y una opinión en línea, respetuosa y con un dato, sobre el resultado.",
        "Medio A valora con «gran victoria» y Medio B con «solo» y «el mejor». Coinciden en que Norte ganó por 2 puntos: 62 a 60. Mi opinión: «Creo que fue una competencia pareja, porque la diferencia fue de solo 2 puntos».",
        ["identifica palabras que valoran", "dice qué dato coincide", "opina con respeto y con un dato"], ["una comparación breve y una opinión con dato"], ["insultar a un colegio", "no usar el dato"], "Lee tu opinión a una persona de tu casa y pídele que revise si es respetuosa."),
    reinforce="Con una persona de tu casa, comparen cómo dos personas cuentan la misma historia y vean qué cambia.",
    extend="Escribe tres reglas de netiqueta para un chat de tu curso.",
    materials=MAT,
)

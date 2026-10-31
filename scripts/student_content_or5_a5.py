"""Cuaderno del estudiante, 5.º básico Orientación: OA 09 (perseverancia, estudio honesto y metas de aprendizaje)."""
from __future__ import annotations

from student_lessons import arith, ex
from student_content_or5_a import M, T, W, lesson

OA9 = "OR05 OA 09"

lesson(
    OA9, 1,
    "Una hoja y un lápiz. El caso de Sam y los datos están escritos en los ejercicios.",
    "Aprenderé a establecer metas de aprendizaje claras y a seguirlas con perseverancia. Sirve para avanzar en lo que me propongo, paso a paso.",
    ["Sé plantear una meta pequeña y concreta.", "Sé que un aspecto a superar puede mejorar."],
    [
        "Una meta de aprendizaje es lo que quieres aprender o mejorar en un tiempo determinado. Una buena meta es específica (dice qué), medible (se puede contar o comprobar), posible (puedes lograrla) y tiene plazo (dice hasta cuándo). «Mejorar en lenguaje» no es una buena meta. «Leer 3 libros cortos en 6 semanas» sí lo es.",
        "La perseverancia es seguir intentando aunque cueste o te equivoques. Perseverar no es hacerlo todo perfecto. Es volver a intentarlo, cambiar la forma de estudiar si no resulta y pedir ayuda cuando lo necesites. Un error es información: te dice qué ajustar.",
        "Piensa en Sam, un estudiante inventado. Quiere mejorar la lectura. Su meta: leer 3 libros cortos en 6 semanas. Si lee 1 libro cada 2 semanas, cumple. Si en la semana 3 va atrasado, no se rinde: revisa su plan y lee 10 minutos más cada día.",
    ],
    [("meta de aprendizaje", "lo que quiero aprender o mejorar en un tiempo"), ("específica", "que dice con claridad qué quiero lograr"), ("medible", "que se puede contar o comprobar"), ("plazo", "tiempo en que quiero lograrla"), ("perseverancia", "seguir intentando aunque cueste")],
    [
        W("Elegir una buena meta", "¿Cuál es mejor meta: «Mejorar en lenguaje» o «Leer 3 libros cortos en 6 semanas»?", ["La segunda dice qué, cuánto y hasta cuándo.", "La primera es vaga.", "Una buena meta es medible."], "«Leer 3 libros cortos en 6 semanas»"),
        W("Revisar el plan", "Sam planeó leer 1 libro cada 2 semanas durante 6 semanas. ¿Cuántos libros leerá si lo cumple?", ["Hay 6 semanas.", "Cada 2 semanas lee 1 libro.", "6 dividido en 2 son 3 libros."], "3 libros"),
    ],
    [
        M("Ponerme una meta enorme para motivarme.", "Se cree que cuanto más grande, mejor.", "Haz metas posibles, con medida y plazo."),
        M("Abandonar la meta cuando me equivoco.", "Se piensa que el error muestra que no puedo.", "Un error indica qué ajustar; vuelve a intentarlo."),
    ],
    R=[
        ex("«Leer 3 libros cortos en 6 semanas». ¿Tiene plazo?", "Sí", "Dice «6 semanas»."),
        ex("Perseverar, ¿es seguir intentando aunque cueste?", "Sí", "No se rinde ante la primera dificultad."),
        ex("Una meta medible, ¿se puede contar o comprobar?", "Sí", "Se puede saber si se cumplió."),
    ],
    U=[
        ex("¿Por qué «mejorar en lenguaje» no es una buena meta?", "Porque no dice cuánto ni hasta cuándo", "Es vaga y no se puede comprobar."),
        ex("¿Qué información da un error?", "Qué conviene ajustar", "Muestra qué cambiar."),
        ex("En Orientación: ¿Qué cuatro características tiene una buena meta?", "Específica, medible, posible y con plazo", "Así se puede seguir y evaluar."),
    ],
    A=[
        ex("Metas: 1) «ser el mejor», 2) «resolver 5 problemas de matemática cada día durante una semana», 3) «aprender mucho». ¿Cuál es una buena meta?", "La 2", "Dice qué, cuánto y cuándo."),
        arith("Sam planeó leer 10 páginas cada día durante 5 días. ¿Cuántas páginas leerá?", "10*5", "Son 10 páginas por día durante 5 días."),
        ex("Sam va atrasado en la semana 3. ¿Qué hace alguien perseverante: revisar el plan y ajustarlo o abandonar?", "Revisar el plan y ajustarlo", "Perseverar incluye cambiar lo que no funciona."),
    ],
    Z=[
        ex("Dos niños fallan una vez. Uno dice «no puedo» y el otro «¿qué cambio?». ¿Quién persevera?", "El segundo", "Busca ajustar y volver a intentarlo."),
        ex("¿Por qué una meta sin plazo es difícil de lograr?", "Porque no hay momento para revisar", "Sin fecha, se posterga."),
    ],
    D=[
        arith("Sam leyó 12 páginas el lunes, 15 el martes y 18 el miércoles. ¿Cuántas páginas leyó?", "12+15+18", "Se suman las páginas de cada día."),
        arith("Su meta es leer 60 páginas en la semana y lleva 45. ¿Cuántas páginas le faltan?", "60-45", "Se resta lo leído a la meta."),
    ],
    context=[ex("Una estudiante inventada quiere mejorar su caligrafía. Su meta: escribir una plana de 10 líneas cada día de lunes a viernes. ¿Cuántas líneas escribirá en total?", "50", "10 líneas por 5 días: 10 × 5 = 50.", calc="10*5")],
    selfcheck=[ex("En Orientación: ¿una meta debe ser medible?", "Sí", "Se puede comprobar."), ex("¿Un error se puede usar para aprender?", "Sí", "Muestra qué ajustar."), ex("¿Perseverar es seguir intentando?", "Sí", "No se rinde con facilidad.")],
    task=T("Elige un tema que quieras mejorar (leer, escribir, una tabla, un idioma o un deporte). Escribe una meta con las cuatro características (específica, medible, posible y con plazo). Escribe también qué harás si en la mitad del plazo vas atrasado.", "Tema: leer. Meta: leer 3 libros cortos en 6 semanas. Si voy atrasado: leo 10 minutos más al día o pido ayuda.", ["meta con las cuatro características", "plan para si hay atraso", "no es una meta enorme"], ["texto escrito"], ["meta vaga", "sin plan de ajuste"], "Reconoce la meta y pregunta cómo la comprobará."),
    reinforce="Escribe una meta con plazo para algo que quieras aprender este mes.",
    extend="Escribe dos cosas que podrías ajustar si no avanzas hacia tu meta.",
)

lesson(
    OA9, 2,
    "Una hoja y un lápiz. El calendario de Noa está escrito en los ejercicios.",
    "Aprenderé a estudiar con anticipación y a organizar mi tiempo, y a manejar distracciones y emociones antes de una prueba. Sirve para llegar con calma.",
    ["Sé establecer una meta de aprendizaje.", "Sé reconocer mis emociones."],
    [
        "Estudiar con anticipación es empezar a repasar antes de la última noche. Una prueba el viernes se prepara con sesiones cortas desde el lunes. Esto ayuda a recordar mejor, porque el cerebro aprende más cuando repasa varias veces en días distintos que cuando lo hace todo de golpe. Una sesión de 20 a 30 minutos con una pausa corta suele ser suficiente a tu edad.",
        "Para organizar el tiempo, usa un calendario semanal: escribe cada día qué estudiarás y cuántos minutos. Pon primero lo más difícil o lo más urgente. Deja tiempo para descansar, moverte y dormir. Un buen plan es realista: no ocupa todas las horas libres.",
        "Antes de una prueba es normal sentir nervios. Distingue el hecho (hay una prueba el viernes), la emoción (nervios) y el límite (guardo el teléfono durante la sesión). Quitar distracciones, como el teléfono o la televisión, ayuda a concentrarte. Si te sientes muy abrumado, avisa a un adulto: puede ayudarte a ordenar el plan.",
    ],
    [("anticipación", "hacer algo con tiempo antes de que sea urgente"), ("calendario semanal", "tabla con lo que hago cada día"), ("sesión de estudio", "momento dedicado a estudiar"), ("distracción", "algo que me saca de lo que hago"), ("repasar", "volver a ver lo que ya estudié")],
    [
        W("Repartir en días", "Noa tiene una prueba el viernes y necesita 60 minutos de estudio. Si estudia 15 minutos cada día, ¿cuántos días necesita?", ["Total: 60 minutos.", "Cada día: 15 minutos.", "60 dividido en 15 son 4 días."], "4 días"),
        W("Quitar una distracción", "Noa estudia con su celular al lado y se distrae. ¿Qué límite es más útil: guardarlo lejos o mirarlo cada 5 minutos?", ["El celular distrae.", "Guardarlo evita la tentación.", "El límite ayuda a concentrarse."], "Guardarlo lejos"),
    ],
    [
        M("Dejar todo para la noche anterior.", "Se cree que da lo mismo cuándo estudiar.", "Estudia en sesiones cortas varios días antes."),
        M("Llenar el calendario con estudio sin descanso.", "Se piensa que más horas es mejor.", "Incluye pausas, juego y sueño."),
    ],
    R=[
        ex("Estudiar con anticipación, ¿es empezar con días de aviso o la noche anterior?", "Con días de aviso", "Permite repasar varias veces."),
        ex("Un calendario semanal, ¿ayuda a organizar el tiempo?", "Sí", "Muestra qué estudiar cada día."),
        ex("El celular al lado mientras estudias, ¿es una distracción?", "Sí", "Puede sacarte de lo que haces."),
    ],
    U=[
        ex("¿Por qué repasar varios días es mejor que estudiar todo en una noche?", "Porque se recuerda mejor", "El cerebro aprende más con repasos en días distintos."),
        ex("¿Por qué conviene dejar tiempo para dormir y descansar?", "Porque el cuerpo y el cerebro lo necesitan", "Descansar ayuda a aprender."),
        ex("¿Qué haces si te sientes muy abrumado antes de una prueba?", "Aviso a un adulto para ordenar el plan", "Un adulto puede ayudarte."),
    ],
    A=[
        arith("Noa estudia 20 minutos cada día, de lunes a jueves. ¿Cuántos minutos estudia en total?", "20*4", "Son 20 minutos repetidos 4 días."),
        arith("Noa necesita estudiar 90 minutos para una prueba. Ya estudió 55. ¿Cuántos minutos le faltan?", "90-55", "Se resta lo estudiado al total."),
        ex("Orden del plan: 1) ver qué temas pide la prueba, 2) repartirlos en días, 3) estudiar, 4) repasar el último día. ¿Cuál va primero?", "Ver qué temas pide la prueba", "Primero hay que saber qué estudiar."),
    ],
    Z=[
        ex("Un niño estudia 120 minutos en una sola noche. Otro estudia 30 minutos durante 4 días. ¿Quién tiene más probabilidad de recordar mejor?", "El que estudia durante 4 días", "Repasar en días distintos mejora el recuerdo."),
        ex("¿Por qué un plan realista es mejor que uno que ocupa todas las horas libres?", "Porque se puede cumplir", "Un plan imposible desanima."),
    ],
    D=[
        arith("Noa dedica 25 minutos de estudio y luego 5 de pausa, y repite 3 veces. ¿Cuántos minutos pasan en total?", "(25+5)*3", "Cada ciclo dura 30 minutos y se repite 3 veces."),
        arith("De sus 5 días de estudio, Noa cumplió 4. ¿Cuántos no cumplió?", "5-4", "Se resta lo cumplido a los días planeados."),
    ],
    context=[ex("Una prueba de ciencias será el jueves. Luz estudia 15 minutos el lunes, 15 el martes y 15 el miércoles. ¿Cuántos minutos estudia en total?", "45", "15 + 15 + 15 = 45.", calc="15+15+15")],
    selfcheck=[ex("En Orientación: ¿estudiar con anticipación ayuda a recordar?", "Sí", "Permite repasar varias veces."), ex("¿Hay que incluir descanso en el plan?", "Sí", "Descansar ayuda a aprender."), ex("¿El celular puede distraer?", "Sí", "El celular quita atención del estudio.")],
    task=T("Tienes una prueba el viernes. Escribe un calendario de lunes a jueves con el tema, los minutos y una pausa. Debe sumar al menos 60 minutos. Escribe también una distracción que quitarás y cómo.", "Lunes: sumas, 20 min. Martes: restas, 20 min. Miércoles: problemas, 15 min. Jueves: repaso, 15 min. Total: 70 min. Distracción: guardo el celular en otra pieza.", ["calendario de cuatro días", "suma al menos 60 minutos", "una distracción y cómo quitarla"], ["tabla escrita"], ["todo el estudio en un día", "sin descanso"], "Reconoce el plan y pregunta cuánto suma."),
    reinforce="Escribe un horario de estudio para tres días usando 20 minutos cada día.",
    extend="Explica por qué conviene dejar tiempo para descansar y dormir en tu plan de estudio.",
)

lesson(
    OA9, 3,
    "Una hoja y un lápiz. Los textos de ejemplo y los casos están escritos en los ejercicios.",
    "Aprenderé qué es el plagio y la copia, por qué son deshonestos y cómo trabajar de forma honesta y colaborativa. Sirve para respetar el estudio y el trabajo de los demás.",
    ["Sé organizar mi tiempo de estudio.", "Sé comparar opciones y consecuencias."],
    [
        "La copia es mirar o pasarse respuestas en una prueba para mostrar algo que no sabes. El plagio es presentar como tuyo un texto, una imagen o una idea de otra persona sin decir de dónde la sacaste. Los dos son deshonestos: engañan a quien evalúa y te quitan la oportunidad de aprender. Además, perjudican a quien hizo el trabajo original.",
        "Hay formas honestas de usar lo que otros escribieron. Puedes leer varias fuentes, entender la idea y contarla con tus propias palabras, lo que se llama parafrasear. Y anotas la fuente: el nombre del libro o página y el autor. Si copias una frase exacta, la pones entre comillas y dices de dónde viene.",
        "El trabajo colaborativo es distinto de copiar. Colaborar es repartir tareas, compartir ideas, explicarse y revisar juntos, y que cada persona haga su parte. Copiar es que uno haga todo y los demás pongan su nombre. En una prueba individual, cada uno debe responder solo. Respetar el estudio de otros también es no hacer ruido ni interrumpirlos.",
    ],
    [("copia", "mirar o pasar respuestas para mostrar lo que no sé"), ("plagio", "presentar como mío algo que hizo otra persona"), ("parafrasear", "contar una idea con mis propias palabras"), ("fuente", "libro, página o persona de donde sale una idea"), ("colaborar", "trabajar juntos, cada uno con su parte")],
    [
        W("Plagio o parafraseo", "Mía lee un párrafo sobre los volcanes y escribe lo mismo, palabra por palabra, sin decir de dónde lo sacó. ¿Es plagio o parafraseo?", ["Copió el texto exacto.", "No citó la fuente.", "Eso es plagio."], "Plagio"),
        W("Colaborar bien", "En un trabajo de 3 personas, cada una investiga una parte y luego la explican. ¿Es colaborar o copiar?", ["Cada una hace su parte.", "Comparten lo que aprendieron.", "Eso es colaborar."], "Colaborar"),
    ],
    [
        M("Creer que si cambio dos palabras ya no es plagio.", "Se piensa que modificar un poco basta.", "Cuenta la idea con tus palabras y cita la fuente."),
        M("Pasar mi tarea a un amigo para ayudarlo.", "Se confunde ayudar con regalar el trabajo.", "Ayuda explicándole cómo hacerlo, no pasándole la tarea."),
    ],
    R=[
        ex("Pasarse respuestas en una prueba individual, ¿es copia?", "Sí", "Se muestra algo que no se sabe."),
        ex("Contar una idea con tus propias palabras, ¿se llama parafrasear?", "Sí", "Es una forma honesta de usar una idea."),
        ex("Decir de dónde sacaste una idea, ¿es citar la fuente?", "Sí", "Reconoce el trabajo del autor."),
    ],
    U=[
        ex("¿Por qué copiar te quita la oportunidad de aprender?", "Porque no practicas ni entiendes", "El aprendizaje ocurre al hacerlo tú."),
        ex("¿En qué se diferencia colaborar de copiar?", "En colaborar cada uno hace su parte", "En copiar uno hace todo y los demás ponen su nombre."),
        ex("¿Qué se hace con una frase exacta que usas de un libro?", "Se pone entre comillas y se dice la fuente", "Así se reconoce al autor."),
    ],
    A=[
        ex("Acciones: 1) copiar una prueba, 2) explicar con mis palabras lo que leí, 3) copiar un texto de internet sin citar, 4) citar la fuente. ¿Cuántas son honestas?", "2", "Explicar con tus palabras y citar son honestas."),
        ex("Luz lee: «El agua hierve a 100 grados Celsius al nivel del mar». Ella escribe exactamente la misma frase y no dice de dónde la sacó. ¿Es parafraseo?", "No", "Escribió lo mismo y no citó la fuente: eso es plagio."),
        ex("Dos amigos están en una prueba individual. Uno le susurra la respuesta al otro. ¿Es colaboración o copia?", "Copia", "En una prueba individual cada uno responde solo."),
    ],
    Z=[
        ex("¿Por qué copiar perjudica también al que hizo el trabajo original?", "Porque se usa su esfuerzo sin reconocerlo", "No se le da crédito."),
        ex("Si un compañero te pide la tarea porque no pudo hacerla, ¿cuál es una ayuda honesta?", "Explicarle cómo hacerla", "Así aprende en vez de recibirla hecha."),
    ],
    D=[
        arith("En un trabajo, 4 estudiantes se reparten 12 preguntas por igual. ¿Cuántas preguntas hace cada uno?", "12//4", "Se divide el trabajo en partes iguales."),
        arith("Un grupo de 5 estudiantes entrega 3 fuentes por persona. ¿Cuántas fuentes citan en total?", "5*3", "Son 3 fuentes por cada uno de los 5."),
    ],
    context=[ex("Para un trabajo sobre los volcanes, Mía lee un libro, explica la idea con sus palabras y escribe al final el título del libro. ¿Trabajó de forma honesta?", "Sí", "Parafraseó y citó la fuente.")],
    selfcheck=[ex("En Orientación: ¿el plagio es presentar como mío algo de otro?", "Sí", "No reconoce al autor."), ex("¿Se puede copiar en una prueba individual?", "No", "Copiar es deshonesto y no enseña."), ex("¿Colaborar es repartir tareas?", "Sí", "Cada uno hace su parte.")],
    task=T("Lee este texto inventado: «Las abejas viven en colmenas y fabrican miel a partir del néctar de las flores». Reescríbelo con tus palabras (parafrasea) y agrega una fuente inventada: «Libro de la biblioteca del colegio». Luego escribe dos formas de ayudar a un compañero con una tarea sin dársela hecha.", "Las abejas hacen su miel con el néctar que recogen de las flores y viven juntas en colmenas. Fuente: libro de la biblioteca del colegio. Ayudas: explicarle un ejemplo; corregir juntos su borrador.", ["parafrasea el texto", "cita la fuente", "dos formas de ayudar sin dar la tarea hecha"], ["texto escrito"], ["copiar palabra por palabra", "no citar"], "Reconoce el parafraseo y pregunta de dónde sacaría una fuente real."),
    reinforce="Escribe con tus palabras una idea de un libro que hayas leído y anota el título.",
    extend="Explica por qué el plagio también es injusto con el autor.",
)

lesson(
    OA9, 4,
    "Una hoja y un lápiz. El caso de Sam y las opciones están escritos en los ejercicios.",
    "Aprenderé a elegir una acción segura y honesta cuando siento la tentación de copiar o cuando alguien me presiona para copiar. Sirve para mantener mi honestidad y pedir ayuda.",
    ["Sé qué son copia y plagio.", "Sé decir que no con respeto."],
    [
        "A veces uno siente la tentación de copiar: no estudió a tiempo, tiene miedo de sacar mala nota o alguien le pide que le pase las respuestas. Es una situación difícil. Primero, reconoce lo que sientes: miedo, presión o vergüenza. Luego piensa en las consecuencias: puedes tener una sanción, perder la confianza de los profesores y no aprender lo que necesitas.",
        "Hay acciones honestas posibles. Si no sabes una respuesta, déjala en blanco o responde lo que sabes. Si alguien te presiona, di con calma: «No, prefiero que cada uno responda lo suyo». Si el problema es que no estudiaste, cuéntale al profesor y pide otra oportunidad o ayuda para ponerte al día. Aprender es más importante que una nota.",
        "También puedes prevenir. Empieza el estudio con anticipación, pide ayuda cuando algo no se entienda y habla con una persona adulta de confianza si sientes mucha presión por las notas. Respetar el estudio de los demás incluye no pedirles que te pasen respuestas ni mirarlas sin permiso.",
    ],
    [("tentación", "ganas de hacer algo que sé que no está bien"), ("honestidad", "decir y hacer lo que es verdadero y justo"), ("sanción", "consecuencia por no cumplir una regla"), ("presión", "insistencia para que haga algo"), ("poner al día", "aprender lo que me quedó atrasado")],
    [
        W("Elegir una acción honesta", "Sam no estudió y alguien le pasa un papel con respuestas. ¿Qué acción es honesta: usarlo o devolverlo y responder lo que sabe?", ["Usarlo es copiar.", "Devolverlo respeta las reglas.", "Responder lo que sabe es honesto."], "Devolverlo y responder lo que sabe"),
        W("Responder a la presión", "Un compañero le dice a Sam: «Déjame ver tu prueba». ¿Qué respuesta pone el límite: «No, prefiero que cada uno responda lo suyo» o «Bueno, solo una vez»?", ["La primera dice que no con calma.", "La segunda cede.", "El límite protege la honestidad."], "«No, prefiero que cada uno responda lo suyo»"),
    ],
    [
        M("Pensar que una nota baja es peor que ser deshonesto.", "Se da más valor a la nota que al aprendizaje.", "Aprender importa más; una nota baja se puede mejorar."),
        M("Dejar que me copien para no perder una amistad.", "Se cree que decir no daña la relación.", "Un buen amigo respeta tu límite."),
    ],
    R=[
        ex("Si no sabes una respuesta, ¿es honesto dejarla en blanco?", "Sí", "No finges saber lo que no sabes."),
        ex("Si te piden copiar tu prueba, ¿puedes decir no?", "Sí", "Tienes derecho a poner un límite."),
        ex("Contarle al profesor que no estudiaste, ¿es una acción honesta?", "Sí", "Permite recibir ayuda."),
    ],
    U=[
        ex("¿Por qué una nota baja puede mejorarse pero la confianza perdida es más difícil?", "Porque la confianza se construye con el tiempo", "La honestidad es difícil de recuperar."),
        ex("¿Qué haces si sientes mucha presión por las notas?", "Hablo con un adulto de confianza", "Un adulto puede ayudar con el plan."),
        ex("En Orientación: ¿qué es la tentación de copiar?", "Las ganas de copiar aunque sé que no está bien", "Es una emoción que se puede manejar."),
    ],
    A=[
        ex("Opciones de Sam: 1) copiar, 2) dejar en blanco lo que no sabe, 3) pedir otra oportunidad al profesor, 4) cambiar de lugar para ver a otro. ¿Cuántas son honestas?", "2", "Dejar en blanco y pedir otra oportunidad son honestas."),
        ex("Noa le dice a un amigo: «No te paso las respuestas, pero te explico cómo resolverlo antes de la prueba». ¿Pone un límite y ayuda?", "Sí", "No copia y ofrece una ayuda honesta."),
        ex("Si Sam no estudió, ¿qué acción de prevención ayuda para la próxima prueba: empezar a estudiar con tiempo o esperar la noche anterior?", "Empezar a estudiar con tiempo", "Con anticipación hay menos presión."),
    ],
    Z=[
        ex("Un niño dice: «Si copio una vez, nadie se entera». ¿Qué problema tiene esa idea?", "Igual no aprende y puede repetirlo", "No evita la deshonestidad."),
        ex("¿Por qué pasar respuestas a un amigo no es ayudarlo?", "Porque no aprende", "Lo deja igual de inseguro."),
    ],
    D=[
        arith("Sam estudia 20 minutos al día durante 5 días en lugar de 100 minutos en una noche. ¿Cuántos minutos son en total en los 5 días?", "20*5", "Se multiplica el tiempo diario por los días."),
        arith("De 28 estudiantes, 26 dicen que no copiarían. ¿Cuántos no están seguros?", "28-26", "Se restan los seguros al total."),
    ],
    context=[ex("Durante una prueba, el compañero de al lado le pide a Luz que le muestre su hoja. Luz le dice: «No, cada uno responde lo suyo; después te ayudo a repasar». ¿Qué mantuvo Luz?", "Su honestidad y su límite", "Dijo no y ofreció ayuda honesta.")],
    selfcheck=[ex("En Orientación: ¿aprender importa más que la nota?", "Sí", "La nota refleja lo aprendido."), ex("¿Se puede decir no a quien pide copiar?", "Sí", "Es un límite legítimo."), ex("¿Pedir ayuda es una acción honesta?", "Sí", "Permite ponerse al día.")],
    task=T("Lee: «Sam no estudió para la prueba de mañana. Un compañero le ofrece pasarle las respuestas. Sam siente miedo de sacar mala nota». Escribe: lo que siente Sam, dos consecuencias de copiar, tres acciones honestas que puede hacer y una frase para decir no.", "Siente miedo. Consecuencias: sanción y no aprender. Acciones: dejar en blanco, contar al profesor, estudiar hoy 20 minutos. Frase: «No, prefiero responder yo».", ["emoción", "dos consecuencias", "tres acciones honestas", "una frase para decir no"], ["texto escrito"], ["justificar copiar", "no ofrecer alternativas"], "Reconoce las acciones y pregunta cuál elegiría."),
    reinforce="Escribe una frase para negarte a pasar respuestas sin perder la amistad.",
    extend="Explica qué harías si te enteras de que un compañero copió en una prueba.",
)

lesson(
    OA9, 5,
    "Una hoja y un lápiz. Las situaciones y la lista de intereses están escritas en los ejercicios.",
    "Aprenderé a preguntar y buscar información sobre temas de mi interés, y a desarrollar actividades relacionadas con ellos. Sirve para aprender con curiosidad y pedir ayuda a tiempo.",
    ["Sé trabajar de forma honesta.", "Sé usar fuentes confiables."],
    [
        "Tus intereses son los temas o actividades que te llaman la atención: los animales, el espacio, la música, el fútbol, el dibujo, la cocina o la tecnología. Desarrollar tus intereses ayuda a aprender con ganas. Puedes hacerlo preguntando, leyendo, probando y compartiendo lo que aprendes.",
        "Para buscar información, sigue tres pasos. Primero, formula una pregunta clara: «¿Cómo vuelan las aves?». Segundo, busca en fuentes confiables, como libros de la biblioteca, personas que sepan del tema o páginas de instituciones conocidas. Tercero, anota lo que aprendiste con tus palabras y escribe la fuente. Si algo no se entiende, pregunta a un profesor, a una persona de tu casa o a un bibliotecario. Si buscas en internet, hazlo con permiso y no entregues tus datos personales.",
        "Cuando no entiendes algo, pedir ayuda es parte de aprender. Puedes decir: «No entendí esta parte. ¿Me lo explicas de otra forma?». Preguntar muestra interés, no debilidad. Un buen estudiante hace preguntas y busca respuestas con honestidad.",
    ],
    [("interés", "tema o actividad que me llama la atención"), ("pregunta clara", "pregunta que dice qué quiero saber"), ("fuente confiable", "lugar de información con autor identificable"), ("bibliotecario", "persona que ayuda a encontrar libros"), ("indagar", "buscar información para saber más")],
    [
        W("Formular una pregunta clara", "A Noa le interesan las aves. ¿Cuál es mejor pregunta: «¿Cómo vuelan las aves?» o «Aves»?", ["La primera dice qué quiere saber.", "La segunda es solo un tema.", "Una pregunta clara guía la búsqueda."], "«¿Cómo vuelan las aves?»"),
        W("Anotar la fuente", "Noa aprende en un libro de la biblioteca cómo vuelan las aves. ¿Qué anota además de lo aprendido?", ["Lo aprendido va con sus palabras.", "También el título del libro.", "Así su aprendizaje es verificable."], "El título del libro"),
    ],
    [
        M("Creer que preguntar es de los que no saben.", "Se piensa que preguntar muestra debilidad.", "Preguntar muestra interés y ayuda a aprender."),
        M("Copiar lo primero que aparece al buscar.", "Se cree que lo primero es lo correcto.", "Revisa si la fuente es confiable y cuéntalo con tus palabras."),
    ],
    R=[
        ex("Un interés, ¿es un tema que te llama la atención?", "Sí", "Puede ser un animal, un deporte o una actividad."),
        ex("Una pregunta clara, ¿dice qué quieres saber?", "Sí", "Guía lo que buscas."),
        ex("Preguntar cuando no entiendes, ¿es parte de aprender?", "Sí", "Muestra interés y ayuda a entender."),
    ],
    U=[
        ex("¿Por qué anotar la fuente es parte de aprender con honestidad?", "Porque reconoce de dónde viene la información", "También sirve para comprobar."),
        ex("¿Qué tres pasos sigues para buscar información?", "Hacer una pregunta, buscar en fuentes confiables y anotar con mis palabras", "Ordena el trabajo."),
        ex("¿Dónde puedes pedir ayuda si no encuentras información?", "A un profesor, a un bibliotecario o a una persona de tu casa", "Son personas que pueden guiarte."),
    ],
    A=[
        ex("Fuentes: 1) libro de la biblioteca, 2) comentario anónimo, 3) página de un museo, 4) video sin autor. ¿Cuántas son confiables?", "2", "El libro y el museo tienen institución identificable."),
        ex("Interés: el espacio. ¿Cuál es una buena pregunta: «¿Por qué la Luna cambia de forma?» o «Cosas del espacio»?", "«¿Por qué la Luna cambia de forma?»", "Dice qué quiere saber."),
        ex("Noa no entiende una explicación. ¿Qué frase pide ayuda: «No entendí esta parte, ¿me lo explicas de otra forma?» o «Esto es aburrido»?", "«No entendí esta parte, ¿me lo explicas de otra forma?»", "Pide una explicación sin culpar."),
    ],
    Z=[
        ex("¿Por qué desarrollar un interés ayuda a aprender?", "Porque da ganas de seguir aprendiendo", "La curiosidad motiva."),
        ex("Un niño dice «mi tema no sirve para el colegio». ¿Qué puede hacer para conectarlo con lo que aprende?", "Buscar qué materias se relacionan con su interés", "Así lo aprovecha en distintas asignaturas."),
    ],
    D=[
        arith("Noa leyó 15 páginas de un libro de aves el lunes y 20 el martes. ¿Cuántas páginas leyó?", "15+20", "Se suman las páginas de los dos días."),
        arith("Para un proyecto de interés, Sam usa 3 fuentes confiables por semana durante 4 semanas. ¿Cuántas fuentes usa?", "3*4", "Son 3 fuentes por 4 semanas."),
    ],
    context=[ex("A Mía le interesan los instrumentos musicales. Pregunta «¿Cómo suena una flauta?», busca en un libro de la biblioteca y anota el título. ¿Siguió los tres pasos?", "Sí", "Preguntó, buscó en fuente confiable y anotó la fuente.")],
    selfcheck=[ex("En Orientación: ¿preguntar es parte de aprender?", "Sí", "Preguntar muestra interés y ayuda."), ex("¿Hay que revisar si una fuente es confiable?", "Sí", "Para evitar errores."), ex("¿Se puede aprender sobre mis intereses?", "Sí", "Ayuda a aprender con ganas.")],
    task=T("Elige un interés de esta lista: animales, espacio, música, fútbol, dibujo, cocina saludable. Escribe: una pregunta clara, dónde buscarías (dos fuentes confiables), a quién pedirías ayuda si no entiendes, y una actividad que podrías hacer para compartir lo que aprendiste.", "Interés: animales. Pregunta: ¿cómo duermen los delfines? Fuentes: libro de la biblioteca y página de un museo. Ayuda: mi profesora. Actividad: hacer un afiche con mis palabras y la fuente.", ["pregunta clara", "dos fuentes confiables", "persona a quien pedir ayuda", "actividad para compartir"], ["texto escrito"], ["pregunta vaga", "fuentes no confiables"], "Reconoce el plan y pregunta qué aprendió."),
    reinforce="Escribe tres preguntas claras sobre un tema que te guste.",
    extend="Haz un plan de cuatro pasos para aprender algo nuevo sobre uno de tus intereses.",
)

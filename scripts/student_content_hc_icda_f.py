"""Interpretación y creación en danza 3.º y 4.º medio HC: OAC-06 (argumentar juicios estéticos sobre obras y manifestaciones de danza), clases 1 a 5. Obras y juicios inventados descritos por escrito; sin video ni obras reales."""
from __future__ import annotations

from hc_icda_common import build

O6 = "AR-ICDA-3y4-OAC-06"

# ============================================================ OAC-06, clase 1
F = ("Ficha 1 (obra de ejemplo «Vaivén», inventada y descrita por escrito; no hay video). Cuatro intérpretes, 5 minutos, sin música: se oyen los pasos y unas palmas suaves de las propias intérpretes. "
     "Sección 1 (2 minutos): cada persona avanza y retrocede en línea con un ritmo parejo y lento, sin cambios. "
     "Sección 2 (2 minutos): se agregan cambios de nivel y de dirección, y las personas se cruzan sin tocarse. "
     "Sección 3 (1 minuto): quietud con la luz que baja de a poco. "
     "Comentarios de ejemplo del público: P1, «no me gustó»; P2, «es lo mejor que he visto»; "
     "P3, «la sección 1 no desarrolla una idea (criterio: desarrollo de la idea), porque repite el mismo avance y retroceso sin cambios durante dos minutos»; "
     "P4, «el final de quietud cierra con coherencia (criterio: coherencia), porque retoma la lentitud y los sonidos suaves del comienzo».")
build(
    O6, 1, F,
    use="Aprenderé a distinguir una apreciación personal (lo que me gusta) de un juicio estético argumentado (una afirmación con criterio y evidencia) sobre una obra de danza.",
    prior=["Sé describir, interpretar y valorar una obra.", "Sé analizar con criterios técnicos e interpretativos.", "Sé que no se evalúan los cuerpos."],
    explain=[
        "Una apreciación personal es lo que una persona siente o prefiere frente a una obra: «me gustó», «me emocionó», «no me llegó». Es legítima y no necesita justificarse, porque es suya. Un juicio estético argumentado, en cambio, es una afirmación sobre la obra («logra su idea», «no desarrolla su propuesta») que se sostiene con un criterio y una evidencia, de modo que otra persona pueda revisarla y discutirla con razones.",
        "La estructura mínima de un juicio argumentado tiene tres partes. Primero, la afirmación (qué se juzga de la obra). Segundo, el criterio (con qué vara se juzga: coherencia, originalidad, claridad de la idea, desarrollo de la idea, uso del espacio, relación con el contexto). Tercero, la evidencia (qué rasgo observable de la obra respalda la afirmación). En el comentario P3 de la ficha: afirmación, «la sección 1 no desarrolla una idea»; criterio, desarrollo de la idea; evidencia, repite el mismo avance y retroceso durante dos minutos.",
        "Se argumenta sobre la obra, nunca sobre los cuerpos ni las personas que la hacen. Una apreciación puede estar en el origen de un juicio («me aburrí» puede llevar a «la repetición no se desarrolla»), pero para convertirse en juicio necesita criterio y evidencia. Las obras de este cuaderno son inventadas y están descritas por escrito: el juicio se hace con lo que el texto dice.",
    ],
    vocab=[("apreciación personal", "lo que una persona siente o prefiere ante una obra"), ("juicio estético", "afirmación sobre una obra apoyada en criterio y evidencia"), ("afirmación", "lo que se dice de la obra"), ("criterio", "vara con la que se juzga una obra"), ("evidencia", "rasgo observable que respalda la afirmación"), ("argumentar", "sostener una afirmación con razones")],
    worked=[
        ("Convertir una apreciación en juicio", "«Me aburrí con la sección 1». Reescríbelo como juicio argumentado.", ["Busca el rasgo que causó el aburrimiento: repite lo mismo.", "Formula: la sección 1 no desarrolla una idea porque repite el mismo avance y retroceso durante dos minutos."], "La sección 1 no desarrolla una idea porque repite el mismo avance y retroceso sin cambios"),
        ("Identificar las partes", "«La sección 3 es coherente porque retoma la lentitud del inicio». ¿Cuál es la afirmación, el criterio y la evidencia?", ["Afirmación: la sección 3 es coherente.", "Criterio: coherencia. Evidencia: retoma la lentitud del inicio."], "Afirmación: la sección 3 es coherente; criterio: coherencia; evidencia: retoma la lentitud del inicio"),
    ],
    mistakes=[("Creer que «me gustó» es un juicio estético completo.", "Es una apreciación válida, pero no dice con qué criterio ni con qué evidencia.", "Agrega el criterio y un rasgo observable de la obra."),
              ("Argumentar sobre quienes interpretan («se ve cansado») en lugar de la obra.", "El juicio es sobre las decisiones y el resultado de la obra, no sobre los cuerpos.", "Habla de lo que hace el movimiento, el espacio, el tiempo y la puesta en escena.")],
    T=[
        ('abc', 'En creación en danza, ¿qué es una apreciación personal?', 'Lo que una persona siente o prefiere ante una obra', 'Una afirmación sobre la obra con criterio y evidencia', 'Una descripción de los pasos que se ven en escena', 'La apreciación es lo que se siente; no necesita criterio ni evidencia.'),
        ('abc', '{F} ¿Cuál comentario es solo una apreciación personal?', 'P1: no me gustó', 'P3: la sección 1 no desarrolla una idea', 'P4: el final cierra con coherencia', 'P1 no dice criterio ni evidencia; P3 y P4 los incluyen.'),
        ('abc', '{F} ¿Qué criterio usa P4?', 'La coherencia', 'La originalidad', 'El uso del espacio', 'P4 dice que el final cierra con coherencia porque retoma el comienzo.'),
        ('abc', '{F} ¿Cuál es la evidencia de P3?', 'Repite el mismo avance y retroceso durante dos minutos', 'La obra no le gustó a P3 y se aburrió mucho', 'La sección 3 es muy quieta y la luz baja de a poco', 'La evidencia es un rasgo observable de la sección 1.'),
        ('=', '{F} ¿Cuántos minutos duran las secciones 1 y 2 juntas?', '2+2', 'La sección 1 dura 2 minutos y la sección 2 también.', ' minutos'),
        ('abc', '{F} ¿Qué afirmación se apoya mejor con la evidencia «se agregan cambios de nivel y de dirección»?', 'La sección 2 desarrolla la propuesta de la sección 1', 'La sección 2 es más bonita y entretenida que la sección 3, que casi no se mueve', 'Las intérpretes se ven más cansadas en la 2', 'Los cambios agregan variedad y desarrollan la idea inicial.'),
        ('abc', '{F} Una persona dice: «la obra es mala porque la hacen cuatro personas». ¿Qué le falta?', 'Un criterio que explique por qué cuatro personas es problema', 'Nada, porque el número de personas ya es una evidencia', 'Decir cuánto le costó entrar a la función y a qué hora llegó', 'Sin criterio ni evidencia vinculados, el número solo es un dato.'),
        ('abc', '{F} Una persona dice: «la obra es genial porque el intérprete de la izquierda es el mejor bailarín». ¿Qué corresponde responder?', 'Que el juicio es sobre la obra y no sobre los cuerpos', 'Que está bien, porque elogiar a alguien es un buen argumento', 'Que debe decir también cuál es el peor bailarín', 'Los juicios se centran en decisiones de la obra, no en comparar personas.'),
        ('abc', '{F} Quieres convertir «la sección 3 me dio paz» en juicio. ¿Cuál reescritura lo logra?', 'La sección 3 logra calma porque la luz baja y se mantiene la quietud', 'La sección 3 es la mejor de las tres porque me dio paz y me gustó', 'La sección 3 dio paz porque todos estaban de acuerdo', 'La reescritura correcta incluye criterio implícito (calma) y evidencia (luz y quietud).'),
        ('abc', 'Dos estudiantes discuten: uno dice que dar un juicio estético es lo mismo que decir lo que a uno le gusta; la otra dice que un juicio estético exige criterio y evidencia. ¿Quién argumenta mejor?', 'La otra, porque el juicio puede discutirse con razones', 'El primero, porque todo juicio es una cuestión de gusto', 'Ninguno, porque los juicios sobre danza no se pueden argumentar', 'El juicio argumentado se puede revisar con razones; la apreciación es personal.'),
        ('abc', '{F} P2 dice «es lo mejor que he visto». Para convertirlo en juicio argumentado, ¿qué debería agregar primero?', 'El criterio con que la valora y un rasgo observable', 'La cantidad de funciones que ha visto antes y de obras que ha comparado', 'Cuánto tiempo estuvo de pie en la función', 'Un juicio necesita criterio y evidencia, no cantidad de experiencia.'),
        ('abc', '{F} Si dos personas tienen juicios opuestos, una dice que la sección 1 funciona y otra que no, ¿qué hace posible la discusión?', 'Que cada una explique su criterio y su evidencia', 'Que una se convenza de la opinión de la otra por insistencia', 'Que la mayoría vote cuál juicio es verdadero', 'Los criterios y evidencias permiten comparar juicios; votar no los argumenta.'),
        ('abc', 'Al comentar, una estudiante siente que le incomoda hablar delante del curso. ¿Qué corresponde?', 'Ofrecerle escribir su juicio o decirlo en grupo pequeño', 'Obligarla a hablar delante de todo el curso para que se acostumbre', 'Pedirle que se retire de la actividad hasta que se sienta mejor', 'Nadie está obligado a exponerse; se ofrecen otras vías para participar.'),
    ],
    ctx=('abc', 'Después de ver «Vaivén», un curso comenta. ¿Cuál comentario cumple con la estructura de afirmación, criterio y evidencia?', 'La sección 2 es original porque combina cambios de nivel y de dirección', 'La sección 2 me gustó más que la 1 y la 3 juntas, porque tiene más movimiento', 'La sección 2 es mejor porque es más movida, más alegre y más rápida', 'Solo el primero nombra una afirmación, un criterio (originalidad) y una evidencia observable.'),
    sc=[
        ("En creación en danza: ¿qué diferencia hay entre apreciación y juicio estético?", "La apreciación es lo que se siente; el juicio se apoya en criterio y evidencia", "Solo el juicio puede discutirse con razones."),
        ("¿Qué tres partes tiene un juicio argumentado?", "Afirmación, criterio y evidencia", "Esas partes permiten revisar el juicio."),
        ("¿Sobre qué se argumenta: la obra o los cuerpos?", "Sobre la obra y sus decisiones", "Los cuerpos no se comparan ni se evalúan."),
    ],
    op=("Elige una obra inventada de la ficha («Vaivén») o una propia descrita en tres líneas. Escribe: (1) una apreciación personal de una oración; (2) un juicio estético argumentado con afirmación, criterio y evidencia; (3) una oración que explique en qué se diferencian los dos. Si prefieres no exponer tu apreciación, escríbela como la de una persona inventada.",
        "Obra: «Vaivén». Apreciación: me dio calma el final. Juicio: la sección 3 es coherente, porque retoma la lentitud y los sonidos suaves del comienzo (criterio: coherencia; evidencia: la luz que baja de a poco y la quietud). Diferencia: mi apreciación dice lo que sentí; el juicio dice qué rasgo de la obra produce la coherencia y puede discutirse.",
        ["escribe una apreciación y un juicio distintos", "el juicio tiene afirmación, criterio y evidencia observable", "explica la diferencia entre ambos"],
        ["hoja con apreciación, juicio y explicación"],
        ["usar solo «me gustó»", "evidencia que no está en la obra", "hablar de los cuerpos"],
        "Pregunta: «¿qué rasgo de la obra respalda tu juicio?». Si responde con una sensación, pídele que la lleve a un rasgo observable."),
    reinforce="Escribe tres apreciaciones personales sobre una obra inventada tuya y conviértelas en juicios argumentados.",
    extend="Explica por qué una apreciación personal puede ser el punto de partida de un juicio argumentado, pero no basta por sí sola.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 2 (criterios y juicios de ejemplo, inventados). Criterios: coherencia (las decisiones se apoyan entre sí), originalidad (aporta algo no previsible), claridad de la idea (se entiende qué propone), desarrollo de la idea (la idea evoluciona), uso del espacio (el espacio se usa con intención) y relación con el contexto (responde al lugar y la ocasión). "
     "Obra «Sendero» (inventada): 5 intérpretes, 6 minutos, en un patio con público alrededor; avanzan en fila por un camino que forma una espiral; la espiral se cierra y se abre dos veces; vestuario cotidiano de un solo color; el público se ubica en los bordes del patio. "
     "Juicio J1: «Sendero es mala.» "
     "Juicio J2: «Sendero usa el espacio con intención (criterio) porque la espiral organiza el patio y el público la ve desde todos los lados.» "
     "Juicio J3: «Sendero es original (criterio) porque la fila de personas se junta (evidencia), pero esa idea se ve en muchas obras.» "
     "Juicio J4: «Sendero tiene claridad porque tiene 5 intérpretes.»")
build(
    O6, 2, F,
    use="Aprenderé a construir y revisar un juicio estético con criterio y evidencia, y a detectar juicios mal armados: sin criterio, sin evidencia, con evidencia que no corresponde o con contradicciones internas.",
    prior=["Sé distinguir apreciación y juicio estético.", "Sé identificar afirmación, criterio y evidencia.", "Conozco criterios de análisis de una obra."],
    explain=[
        "Un juicio bien armado cumple tres condiciones: el criterio corresponde a lo que se afirma, la evidencia está realmente en la obra y la evidencia respalda el criterio. Si una de las tres falla, el juicio se debilita. Por ejemplo, decir «tiene claridad porque tiene 5 intérpretes» elige un criterio (claridad) y una evidencia (el número de intérpretes) que no se relacionan: la cantidad de personas no dice si una idea se entiende.",
        "Los criterios más comunes en el análisis de danza son: coherencia (las decisiones se apoyan entre sí), originalidad (aporta algo no previsible), claridad de la idea (se entiende qué propone), desarrollo de la idea (evoluciona), uso del espacio (se usa con intención) y relación con el contexto (responde al lugar y la ocasión). Un buen juicio elige el criterio más pertinente para la afirmación, nombra una evidencia concreta y, cuando corresponde, reconoce un límite o una excepción.",
        "Revisar el juicio de otra persona se hace con preguntas, no con descalificaciones: ¿a qué criterio apunta?, ¿qué rasgo lo respalda?, ¿esa evidencia está en la obra?, ¿sirve para ese criterio? Se revisa el argumento, no a quien lo dice. Y cada quien puede decidir si comparte su juicio con el curso o lo entrega por escrito.",
    ],
    vocab=[("pertinente", "que corresponde a lo que se afirma"), ("coherencia", "las decisiones de una obra se apoyan entre sí"), ("originalidad", "aporta algo no previsible"), ("desarrollo de la idea", "la idea evoluciona a lo largo de la obra"), ("uso del espacio", "el espacio se organiza con intención"), ("contraejemplo", "dato que contradice una afirmación")],
    worked=[
        ("Revisar un juicio", "«La obra es coherente porque dura 6 minutos». ¿Qué falla?", ["El criterio es coherencia: decisiones que se apoyan entre sí.", "La evidencia (la duración) no dice nada de cómo se relacionan las decisiones."], "La evidencia no corresponde al criterio"),
        ("Mejorar un juicio", "«La obra es original». ¿Qué se agrega para que sea un juicio argumentado?", ["Falta una evidencia observable.", "Se agrega, por ejemplo, que la fila forma una espiral que cambia de sentido."], "Se agrega una evidencia concreta, como la espiral que cambia de sentido"),
    ],
    mistakes=[("Usar como evidencia un dato que no se relaciona con el criterio, como el número de personas para hablar de claridad.", "El dato no respalda la afirmación.", "Elige un rasgo que muestre la claridad, como si se entiende la idea."),
              ("Descalificar a quien tiene un juicio distinto.", "Se revisa el argumento, no a la persona.", "Pregunta por el criterio y la evidencia.")],
    T=[
        ('abc', 'En creación en danza, ¿qué significa que un criterio sea pertinente?', 'Que corresponde a lo que se afirma de la obra', 'Que es el criterio más difícil de aplicar', 'Que lo usa la mayoría de las personas', 'Pertinente es que se relacione con la afirmación; no importa la dificultad ni la popularidad.'),
        ('abc', '{F} ¿Qué juicio no tiene criterio ni evidencia?', 'J1: Sendero es mala', 'J2: Sendero usa el espacio con intención', 'J3: Sendero es original', 'J1 no dice con qué criterio ni con qué evidencia la juzga.'),
        ('abc', '{F} ¿Qué criterio usa J2?', 'El uso del espacio', 'La originalidad', 'La coherencia', 'J2 dice que usa el espacio con intención.'),
        ('abc', '{F} ¿Cuál es la evidencia de J2?', 'La espiral estructura el patio', 'La obra dura 6 minutos en total y se presenta con luz natural', 'Hay 5 intérpretes con ropa cotidiana de un solo color', 'La espiral y la vista desde todos los lados respaldan el uso intencionado del espacio.'),
        ('abc', '{F} ¿Qué falla en J4, «tiene claridad porque tiene 5 intérpretes»?', 'El número de intérpretes no muestra claridad', 'Faltan más intérpretes para que haya claridad', 'La claridad no es un criterio válido', 'La evidencia no corresponde al criterio elegido.'),
        ('=', '{F} La espiral se cierra y se abre 2 veces. Cada cierre dura 45 segundos y cada apertura dura 45 segundos. ¿Cuántos segundos duran en total?', '2*2*45', 'Son 2 cierres y 2 aperturas, es decir, 4 movimientos de 45 segundos.', ' segundos'),
        ('abc', '{F} J3 dice que «Sendero» es original (la fila se junta) pero que la idea se ve en muchas obras. ¿Qué tiene de particular?', 'Reconoce un límite o contraejemplo a su afirmación', 'Es un juicio sin criterio ni evidencia, porque solo da una opinión', 'Es una apreciación personal sin argumentos', 'Reconocer que la idea se ve en otras obras matiza la afirmación.'),
        ('abc', '{F} ¿Qué evidencia respaldaría mejor un juicio sobre la relación con el contexto de «Sendero»?', 'El público rodea el patio y ve la espiral', 'Los intérpretes visten colores cotidianos', 'La obra dura 6 minutos', 'El patio con público alrededor y la espiral se relacionan con el lugar y la ocasión.'),
        ('abc', '{F} Un integrante dice «J1 es sincero y eso basta». ¿Qué respuesta es más adecuada?', 'Es válida como apreciación, pero un juicio exige criterio y evidencia', 'Que tiene razón, porque la sinceridad de quien opina es la mejor evidencia posible', 'Que debe borrar su juicio y escribir otro igual al de otra persona', 'Un juicio se argumenta con criterio y evidencia; la sinceridad es una apreciación.'),
        ('abc', 'Dos estudiantes discuten sobre J3: uno dice que, al reconocer un límite, el juicio pierde fuerza; la otra, que gana credibilidad. ¿Quién argumenta mejor?', 'La otra, porque reconocer un límite muestra cuidado', 'El primero, porque un juicio debe parecer seguro', 'Ninguno, porque los límites no importan en un juicio', 'Un juicio matizado es más sólido porque admite excepciones.'),
        ('abc', '{F} Quieres un juicio sobre el desarrollo de la idea en «Sendero». ¿Cuál evidencia es más pertinente?', 'La espiral se cierra y se abre, cambiando el recorrido', 'El vestuario es de un solo color y es cotidiano', 'El público está en los bordes del patio de la obra', 'El cambio del recorrido a lo largo de la obra muestra desarrollo.'),
        ('abc', '{F} Una persona dice «J1 es más válido que J2, porque lo dijo una profesora». ¿Qué corresponde responder?', 'Que un juicio vale por su criterio y evidencia, no por quién lo dice', 'Que tiene razón, porque una profesora siempre acierta en sus juicios y no se discute', 'Que J2 debe cambiarse por J1 sin revisar nada, porque lo dijo ella', 'La autoridad de quien habla no sustituye al criterio y la evidencia.'),
        ('abc', 'Al revisar los juicios del curso, una estudiante propone mostrar a todas las personas el puntaje más bajo para «que aprendan». ¿Qué corresponde?', 'No: se revisa con respeto y sin exponer a nadie', 'Sí, porque verlo ayuda a corregir el error', 'Sí, pero solo si la persona está ausente', 'La revisión no expone a nadie; se comenta el juicio con respeto.'),
    ],
    ctx=('abc', 'Un curso debe mejorar este juicio sobre «Sendero»: «es una obra muy buena por cómo se mueve». ¿Cuál reescritura es la más sólida?', 'Usa el espacio con intención, porque la espiral organiza el patio', 'Es muy buena porque se mueve de una manera muy buena y llamativa en todo momento', 'Es buena porque a las personas del público les gustó mucho', 'Solo la primera tiene un criterio claro y una evidencia que corresponde.'),
    sc=[
        ("En creación en danza: ¿qué falla si la evidencia no corresponde al criterio?", "El juicio queda sin respaldo", "La evidencia debe mostrar el criterio elegido."),
        ("¿Para qué sirve reconocer un límite o contraejemplo?", "Para matizar el juicio y darle credibilidad", "Admite excepciones y evita exagerar lo que se afirma de la obra."),
        ("¿Se revisa el juicio o a quien lo dice?", "El juicio, con preguntas sobre criterio y evidencia", "Nunca se descalifica a la persona."),
    ],
    op=("Toma los juicios J1 a J4 de la ficha y para cada uno escribe: (a) qué falla o qué funciona, (b) una pregunta de revisión respetuosa y (c) una reescritura mejorada si hace falta. Luego escribe un juicio propio de «Sendero» con criterio, evidencia y un límite reconocido.",
        "J1: falla, no hay criterio ni evidencia. Pregunta: ¿qué te pareció mal y por qué? Reescritura: «Sendero desarrolla poco su idea, porque la espiral se repite dos veces sin cambios en energía». J2: funciona. J3: funciona y reconoce un límite. J4: falla, el número no prueba claridad; reescritura: «tiene claridad porque la espiral se entiende desde cualquier lado». Juicio propio: «Sendero es coherente porque el vestuario de un solo color y la espiral refuerzan la idea de unidad; sin embargo, el color podría repetirse en más obras».",
        ["identifica qué falla o funciona en cada juicio", "propone preguntas respetuosas y reescrituras", "su juicio propio tiene criterio, evidencia y límite"],
        ["hoja con revisión de cuatro juicios y un juicio propio"],
        ["no distinguir criterio y evidencia", "descalificar a quien emitió el juicio", "olvidar el límite"],
        "Pregunta: «¿qué rasgo de la obra respalda eso?». Si responde con el nombre del criterio, pídele un rasgo concreto."),
    reinforce="Escribe tres juicios sobre «Sendero» (uno con criterio mal elegido, uno sin evidencia y uno bien armado) y marca cuál es cuál.",
    extend="Explica por qué reconocer un contraejemplo puede fortalecer un juicio estético.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 3 (obras y juicios de ejemplo, inventados). Obra «Pasaje» (de estilo académico, inventada): 6 intérpretes, líneas simétricas, precisión con el pulso, control del esfuerzo, vestuario claro. "
     "Obra «Cruce» (de estilo urbano, inventada): 5 intérpretes, ronda con frases improvisadas, energía fuerte, público cercano en un patio. "
     "Juicios de ejemplo. Q1: «Pasaje es buena porque es famosa» (autoridad). Q2: «Cruce es mejor porque tuvo más aplausos» (popularidad). Q3: «Cruce no vale porque el grupo que la creó me cae mal» (ataque personal). Q4: «Pasaje no se entiende, así que es mala» (no la entiendo, entonces es mala). Q5: «Pasaje es precisa (criterio) porque los movimientos coinciden con el pulso y las líneas se mantienen alineadas.» "
     "Falacia: error de razonamiento que parece un argumento pero no respalda la conclusión. "
     "Criterios según estilo: en estilo académico, precisión y control; en estilo urbano, improvisación y relación con el público.")
build(
    O6, 3, F,
    use="Aprenderé a reconocer falacias comunes en juicios estéticos (autoridad, popularidad, ataque personal, «no la entiendo») y a elegir criterios que correspondan al estilo y la procedencia de la obra.",
    prior=["Sé armar juicios con criterio y evidencia.", "Sé comparar obras sin jerarquizar estilos.", "Reconozco contextos distintos de las obras."],
    explain=[
        "Una falacia es un error de razonamiento que se parece a un argumento pero no respalda la conclusión. En los juicios sobre danza hay cuatro muy comunes. La falacia de autoridad dice que algo es bueno porque es famoso o lo dice alguien importante. La falacia de popularidad dice que algo es mejor porque tuvo más aplausos o más visitas. El ataque personal descalifica la obra por quien la hizo, no por lo que hace. Y el «no la entiendo, entonces es mala» confunde la falta de comprensión con un defecto de la obra.",
        "Para evitar falacias, se vuelve siempre a la obra: ¿qué criterio?, ¿qué rasgo la respalda? La fama, los aplausos o la simpatía por un grupo pueden ser datos de contexto, pero no son evidencia del valor de la obra. Cuando no se entiende una obra, el paso correcto es describirla, buscar su contexto y preguntar, no condenarla. Y los criterios se eligen según el estilo y la procedencia: una obra de estilo académico se mira por su precisión y control; una urbana, por su improvisación y relación con el público.",
        "Una cosa es no compartir un criterio y otra imponer los de un estilo sobre otro. Si se trata de la danza de una comunidad real, se consulta a personas que la conozcan y no se juzga con medidas ajenas. Las obras de la ficha son inventadas. En cualquier caso, el juicio se hace sobre la obra y sus decisiones, no sobre cuerpos, y nadie está obligado a opinar en voz alta.",
    ],
    vocab=[("falacia", "razonamiento que parece válido pero no respalda la conclusión"), ("falacia de autoridad", "afirmar que algo es bueno porque lo dice alguien famoso o importante"), ("falacia de popularidad", "afirmar que algo es mejor porque tiene más aplausos"), ("ataque personal", "descalificar una obra por quien la hizo"), ("comprensión", "entender qué propone una obra"), ("criterio según estilo", "criterio que corresponde al estilo y procedencia de la obra")],
    worked=[
        ("Detectar una falacia", "«Esa obra es la mejor porque todo el colegio la aplaudió». ¿Qué falacia es?", ["El argumento usa los aplausos como prueba de valor.", "Es la falacia de popularidad."], "Popularidad"),
        ("Elegir un criterio según estilo", "Una obra urbana de ronda con frases improvisadas. ¿Cuál criterio es más pertinente: simetría o improvisación?", ["La obra se basa en frases creadas en el momento.", "La improvisación es el criterio que corresponde a su estilo."], "Improvisación"),
    ],
    mistakes=[("Pensar que lo que no se entiende está mal hecho.", "La incomprensión puede ser de contexto o de información, no un defecto de la obra.", "Describe, busca su contexto y pregunta antes de juzgar."),
              ("Usar la fama o los aplausos como evidencia.", "Son datos de contexto; no muestran cómo funciona la obra.", "Vuelve a los rasgos de la obra y su criterio.")],
    T=[
        ('abc', 'En creación en danza, ¿qué es una falacia?', 'Un razonamiento que parece válido pero no respalda la conclusión', 'Una opinión que es falsa porque nadie la comparte', 'Un juicio con criterio y evidencia que otras personas no aceptan', 'Una falacia es un error de razonamiento, no una opinión impopular.'),
        ('abc', '{F} ¿Qué falacia comete Q1, «es buena porque es famosa»?', 'Autoridad', 'Popularidad', 'Ataque personal', 'Q1 usa la fama como prueba de valor: es autoridad.'),
        ('abc', '{F} ¿Qué falacia comete Q2, «es mejor porque tuvo más aplausos»?', 'Popularidad', 'Autoridad', 'No la entiendo', 'Los aplausos no demuestran valor estético: es popularidad.'),
        ('abc', '{F} ¿Qué falacia comete Q3?', 'Ataque personal', 'Popularidad', 'Autoridad', 'Q3 descalifica la obra por quienes la crearon.'),
        ('abc', '{F} ¿Qué falacia comete Q4, «no se entiende, así que es mala»?', 'No la entiendo, entonces es mala', 'Autoridad, porque lo dijo alguien importante', 'Ataque personal', 'Confunde no entender con un defecto de la obra.'),
        ('abc', '{F} ¿Qué criterio corresponde a «Cruce»?', 'La improvisación y la relación con el público', 'La simetría de las líneas y la forma del grupo', 'La precisión con un pulso regular', 'Cruce es urbana con frases improvisadas y público cercano.'),
        ('abc', '{F} ¿Qué criterio corresponde a «Pasaje»?', 'La precisión y el control', 'La improvisación y los cambios de la ronda', 'La cercanía del público', 'Pasaje es de estilo académico con precisión y control.'),
        ('abc', '{F} ¿Por qué Q5 es un juicio bien armado?', 'Tiene criterio (precisión) y evidencia (el pulso y las líneas)', 'Porque dice que la obra es precisa y eso basta como argumento', 'Porque menciona a la mayoría del público que la vio ese día', 'Q5 incluye criterio y evidencia que corresponden a la obra.'),
        ('=', '{F} En una ronda de «Cruce», cada una de las 5 personas muestra 3 frases improvisadas de 20 segundos. ¿Cuántos segundos dura la ronda?', '5*3*20', 'Son 5 personas con 3 frases cada una, de 20 segundos.', ' segundos'),
        ('abc', '{F} Una persona dice: «no entiendo «Cruce», así que no sirve». ¿Qué respuesta corresponde?', 'Describirla, buscar su contexto y preguntar antes de juzgar', 'Aceptar que no sirve si nadie del curso la entiende, porque importa comprender', 'Pedir a las intérpretes que la expliquen en el escenario', 'La incomprensión es un punto de partida para investigar, no una conclusión.'),
        ('abc', '{F} Dos estudiantes discuten: uno juzga «Cruce» con los criterios de «Pasaje» y concluye que le falta simetría; la otra dice que se debe usar la improvisación. ¿Quién argumenta mejor?', 'La otra, porque los criterios deben corresponder al estilo', 'El primero, porque la simetría sirve para juzgar toda obra de danza', 'Ninguno, porque no se pueden usar criterios', 'Se usan criterios pertinentes al estilo y procedencia.'),
        ('abc', '{F} Un integrante dice que «Pasaje» es mala porque «el grupo que la creó nunca ayuda en las tareas». ¿Qué corresponde?', 'Notar que es un ataque personal y volver a los rasgos de la obra', 'Aceptar el argumento, porque el comportamiento del grupo importa', 'Pedir que lo cuente a todo el curso', 'El juicio se hace sobre la obra y no sobre las personas que la crearon.'),
        ('abc', 'Para estudiar una danza real de una comunidad, un grupo propone juzgarla con los criterios del estilo académico. ¿Qué corresponde?', 'Consultar a quienes la conozcan y usar criterios de esa tradición', 'Usar los criterios del estilo académico, porque son universales', 'Usar solo los criterios que prefiere la mayoría del curso', 'Los criterios corresponden a cada tradición y se consulta a quienes la conocen.'),
    ],
    ctx=('abc', 'Un curso discute dos obras. Un integrante afirma: «Pasaje es mejor que Cruce porque tiene más precisión». ¿Qué respuesta es más sólida?', 'Que se comparan por criterios distintos, y la precisión no corresponde', 'Que tiene razón, porque la precisión es el mejor criterio para toda danza', 'Que Cruce es mejor porque tiene más energía y más público cerca', 'No se jerarquizan estilos distintos con un criterio que corresponde a uno solo.'),
    sc=[
        ("En creación en danza: ¿qué es la falacia de popularidad?", "Afirmar que algo es mejor porque tuvo más aplausos", "Los aplausos no muestran el valor estético."),
        ("¿Qué se hace cuando no se entiende una obra?", "Se describe, se busca su contexto y se pregunta", "No entender no es un defecto de la obra."),
        ("¿Por qué los criterios deben corresponder al estilo de la obra?", "Para no juzgar con medidas ajenas", "Cada estilo de danza valora cosas distintas en sus obras."),
    ],
    op=("Elige una obra inventada de estilo académico o urbano (la de la ficha o una propia descrita en tres líneas). Escribe dos juicios: uno con una falacia a propósito y uno bien armado con criterio según el estilo y evidencia. Nombra la falacia y explica por qué no respalda la conclusión. Si estudias una danza de una comunidad real, anota a quién consultarías.",
        "Obra «Cruce». Juicio con falacia: «Cruce es mejor porque tuvo más aplausos» (popularidad): los aplausos no muestran cómo funciona la obra. Juicio bien armado: «Cruce logra relación con el público (criterio), porque la ronda cierra el espacio en torno al público cercano y cada persona entra al centro a mostrar una frase». Si fuera una danza real, consultaría a personas de la comunidad y citaría su procedencia.",
        ["identifica una falacia y explica por qué falla", "el juicio bien armado usa criterio según el estilo", "evita juzgar cuerpos y personas"],
        ["hoja con un juicio falaz, su explicación y un juicio bien armado"],
        ["no nombrar la falacia", "usar criterios de otro estilo", "juzgar por quién crea la obra"],
        "Pregunta: «¿qué criterio corresponde a esta obra y por qué?». Si no sabe, pídele que vuelva a la descripción."),
    reinforce="Inventa tres frases con falacias distintas sobre una obra de danza y escribe qué falacia es cada una.",
    extend="Explica por qué «no la entiendo, entonces es mala» es una falacia y qué haría una persona crítica en su lugar.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 4 (juicios y contrajuicios de ejemplo, inventados). Obra «Vaivén» (de la clase 1): 4 intérpretes, 5 minutos; sección 1 de avance y retroceso parejo; sección 2 con cambios de nivel y de dirección; sección 3 de quietud con la luz que baja. "
     "Juicio A: «Vaivén es coherente (criterio), porque la quietud final retoma la lentitud del comienzo (evidencia).» "
     "Contrajuicio B: «Vaivén no es original (criterio), porque el avance y retroceso es un recurso muy usado (evidencia).» "
     "Respuesta de A a B: «Tal vez el recurso se conozca, pero la obra lo combina con un final de quietud que le da un sentido propio.» "
     "Apreciación de Camila: «me emocionó el final porque me recordó el silencio de una biblioteca». "
     "Matiz: afirmación con límite o con condición («es coherente, aunque poco original»).")
build(
    O6, 4, F,
    use="Aprenderé a combinar mi apreciación personal con el análisis, a anticipar contraargumentos y a responderlos con respeto, y a matizar mis juicios con límites y condiciones.",
    prior=["Sé armar juicios con criterio y evidencia.", "Sé reconocer falacias.", "Sé que cada persona puede apreciar distinto."],
    explain=[
        "Un juicio estético sólido suele tener dos fuentes: el análisis de la obra y la apreciación personal. La apreciación dice cómo me afecta («me emocionó el final porque me recordó un silencio de biblioteca») y da un punto de partida; el análisis muestra qué rasgos de la obra producen ese efecto. Cuando se unen, se dice por qué la obra me llegó y se puede discutir con otras personas que no tuvieron esa vivencia.",
        "Argumentar bien también es anticipar contraargumentos: razones de otra persona que apuntan en sentido contrario. En la ficha, A dice que «Vaivén» es coherente y B dice que no es original. No se contradicen del todo, porque hablan de criterios distintos. Una buena respuesta reconoce lo que el contraargumento tiene de válido y explica por qué no cambia la conclusión (o cambia parte de ella). A esto se le llama matizar: «es coherente, aunque poco original».",
        "Se debate con respeto: se escucha primero, se pregunta antes de refutar, se cita al otro con exactitud y se evita descalificar. Cambiar de opinión ante una buena evidencia no es perder: es un resultado esperable de una discusión sana. Nadie debe compartir una vivencia personal si no quiere: se puede usar una apreciación de una persona inventada.",
    ],
    vocab=[("contraargumento", "razón que apunta en sentido contrario a un juicio"), ("matizar", "agregar un límite o condición a una afirmación"), ("refutar", "mostrar con razones que un argumento no se sostiene"), ("réplica", "respuesta a un contraargumento"), ("vivencia", "experiencia personal"), ("debate respetuoso", "intercambio de razones sin descalificar a nadie")],
    worked=[
        ("Matizar un juicio", "«La obra es muy clara». Agrega un límite.", ["Piensa en qué aspecto no es tan claro.", "Por ejemplo: «es clara en la idea, aunque el final podría ser más explícito»."], "Es clara en la idea, aunque el final podría ser más explícito"),
        ("Responder a un contraargumento", "«La obra no es original porque usa un recurso conocido». Escribe una réplica.", ["Reconoce lo que tiene de válido.", "Agrega por qué el recurso cobra otro sentido en esta obra."], "El recurso es conocido, pero en esta obra se combina de una forma propia"),
    ],
    mistakes=[("Responder a un contraargumento diciendo «tú no entiendes de danza».", "Es un ataque personal y no responde al argumento.", "Cita el contraargumento y responde con criterio y evidencia."),
              ("Creer que cambiar de opinión es perder la discusión.", "Cambiar ante una buena evidencia es parte del razonamiento.", "Reconoce la razón y ajusta tu juicio.")],
    T=[
        ('abc', 'En creación en danza, ¿qué es un contraargumento?', 'Una razón que apunta en sentido contrario a un juicio', 'Una forma de repetir el juicio con otras palabras', 'Una opinión con la que todo el grupo está de acuerdo', 'El contraargumento va en sentido contrario; no es una repetición ni un acuerdo.'),
        ('abc', '{F} ¿Qué criterio usa el contrajuicio B?', 'La originalidad', 'La coherencia', 'El uso del espacio', 'B dice que «Vaivén» no es original.'),
        ('abc', '{F} ¿Cuál es la evidencia del juicio A?', 'La quietud final retoma la lentitud del comienzo', 'El avance y retroceso es un recurso muy usado', 'A Camila le recordó una biblioteca', 'La evidencia de A es la relación entre el final y el comienzo.'),
        ('abc', '{F} ¿Qué función cumple la respuesta de A a B?', 'Reconoce algo válido de B y explica por qué la obra tiene un sentido propio', 'Descalifica a quien dijo B diciendo que no entiende nada de danza ni de la obra', 'Repite el juicio A sin cambios y sin responder a lo que dijo B', 'La réplica reconoce y matiza, no descalifica ni repite.'),
        ('abc', '{F} ¿Qué es la apreciación de Camila?', 'Una vivencia personal: el silencio de una biblioteca', 'Una evidencia observable de la obra que respalda el juicio', 'Un contraargumento contra el juicio A sobre la coherencia', 'Lo que le recordó es personal; el rasgo observable es el final de quietud.'),
        ('abc', '{F} ¿Cómo se podría usar la apreciación de Camila en un juicio argumentado?', 'Como punto de partida para ver qué rasgo la produce', 'Como evidencia suficiente de que la obra es excelente', 'Como una razón para descartar el criterio de coherencia', 'La apreciación se convierte en juicio al enlazarla con rasgos observables.'),
        ('=', '{F} La obra dura 5 minutos y la quietud final dura 1 minuto. ¿Cuántos minutos duran juntas las secciones 1 y 2?', '5-1', 'Al total de la obra se le resta la sección 3, que es la quietud final.', ' minutos'),
        ('abc', '{F} ¿Cuál es un matiz bien formulado para el juicio A?', 'Es coherente, aunque el recurso sea conocido', 'Es coherente y nadie podría decir lo contrario', 'Es coherente porque le gustó a mucha gente', 'Un matiz agrega un límite o condición sin renunciar al juicio.'),
        ('abc', '{F} Alguien responde a B diciendo: «tú no sabes de danza». ¿Qué corresponde?', 'Notar el ataque personal y pedir que responda a B', 'Aceptar la respuesta, porque cierra la discusión', 'Pedir que B se retire de la actividad para evitar conflictos', 'La respuesta no refuta el argumento; hay que volver a las razones.'),
        ('abc', '{F} Dos estudiantes discuten: uno dice que A y B se contradicen del todo; la otra, que hablan de criterios distintos y pueden convivir. ¿Quién argumenta mejor?', 'La otra, porque coherencia y originalidad son criterios diferentes', 'El primero, porque dos juicios opuestos nunca pueden convivir en una misma obra', 'Ninguno, porque A y B no hablan de la misma obra', 'Una obra puede ser coherente y poco original al mismo tiempo.'),
        ('abc', '{F} Después de escuchar a B, una persona cambia su juicio y dice: «tienes razón en la originalidad». ¿Qué corresponde?', 'Valorarlo como un resultado normal de una buena discusión', 'Considerarlo una derrota de esa persona frente al otro equipo', 'Pedirle que explique por qué cambió de grupo', 'Cambiar de opinión ante una buena razón es parte del razonamiento.'),
        ('abc', '{F} Una compañera cuenta una vivencia dolorosa para reforzar su juicio y luego se siente incómoda. ¿Qué corresponde?', 'Agradecerle, no insistir y ofrecerle avisar a una persona adulta', 'Pedirle más detalles de lo que vivió para entender mejor su historia y su juicio', 'Usar su historia como evidencia de que la obra es buena', 'Nadie debe exponerse; se cuida a la persona y se ofrece apoyo.'),
        ('abc', 'Al debatir, el grupo acuerda un orden de intervención para que todas las personas puedan hablar, con tiempo por turno. ¿Por qué ayuda?', 'Porque asegura que se escuchen todas las razones', 'Porque evita que alguien cambie de opinión', 'Porque hace que gane quien habla primero', 'Los turnos aseguran que todas las razones se escuchen y se puedan responder.'),
    ],
    ctx=('abc', 'En un debate sobre «Vaivén», una persona dice: «A me convenció, pero B tiene razón en que el recurso es conocido». ¿Qué conclusión matizada es más adecuada?', '«Vaivén» es coherente, aunque poco original', '«Vaivén» no tiene ningún valor, porque el recurso es conocido', '«Vaivén» es perfecta, porque nadie puede objetar', 'La conclusión matizada reconoce coherencia y una limitación de originalidad.'),
    sc=[
        ("En creación en danza: ¿qué es matizar un juicio?", "Agregar un límite o una condición a la afirmación", "Un juicio matizado admite excepciones y límites razonables."),
        ("¿Qué se debe hacer al responder un contraargumento?", "Reconocer lo válido y explicar con criterio y evidencia", "Así se responde la razón y no a la persona."),
        ("¿Cambiar de opinión ante una buena razón es perder?", "No: es parte del razonamiento", "Una discusión sana puede cambiar los juicios."),
    ],
    op=("Elige una obra inventada tuya o «Vaivén». Escribe: (1) un juicio con criterio y evidencia; (2) un contraargumento posible con otro criterio; (3) una réplica que reconozca algo válido y explique tu postura; (4) tu juicio final matizado con un límite. Opcional: agrega una apreciación personal de una persona inventada y explícala con un rasgo de la obra.",
        "Obra: «Vaivén». Juicio: es coherente, porque la quietud final retoma el comienzo. Contraargumento: el avance y retroceso es un recurso muy usado, por lo que no es original. Réplica: es cierto que el recurso es conocido, pero la obra lo combina con un final de quietud que le da un sentido propio. Juicio final matizado: es coherente, aunque poco original. Apreciación: me emocionó el final, porque la luz baja de a poco y se mantiene la quietud.",
        ["el juicio, el contraargumento y la réplica son claros", "la réplica reconoce algo válido sin atacar a la persona", "el juicio final está matizado"],
        ["hoja con juicio, contraargumento, réplica y juicio final matizado"],
        ["responder atacando a la persona", "no reconocer nada de lo válido en el contraargumento", "usar vivencias dolorosas como evidencia"],
        "Pregunta: «¿qué reconoces del contraargumento?». Si responde «nada», pídele que busque un punto que sí sea válido."),
    reinforce="Escribe un juicio sobre una obra inventada y dos contraargumentos distintos con otros criterios; luego una réplica a cada uno.",
    extend="Explica por qué un juicio matizado puede ser más convincente que uno absoluto.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 5 (debate de ejemplo, inventado). Tema: «¿Logra «Vaivén» comunicar su idea?» Dos equipos de 3 personas: Equipo 1 (a favor) y Equipo 2 (en contra). "
     "Formato: apertura de cada equipo 3 minutos, réplica de cada equipo 2 minutos, preguntas del curso 4 minutos en total y cierre de cada equipo 1 minuto. "
     "Normas: hablar por turnos, citar con exactitud, preguntar antes de refutar, no descalificar a nadie, no comparar cuerpos. "
     "Pauta de revisión (1 a 4 por criterio): claridad del juicio, evidencia observable, respuesta a contraargumentos, respeto en el intercambio. "
     "Retroalimentación sugerida: «observo… (hecho), esto produce… (efecto) y me pregunto si… (sugerencia como pregunta)». "
     "Juicio final de ejemplo (equipo 1): «Vaivén logra comunicar una idea de calma, porque las secciones pasan de la repetición a la quietud; reconocemos que la sección 1 es larga.»")
build(
    O6, 5, F,
    use="Aprenderé a preparar y conducir un debate respetuoso sobre un juicio estético, a dar y recibir retroalimentación descriptiva y a revisar mi juicio final con evidencia, sin evaluar cuerpos ni personas.",
    prior=["Sé armar juicios con criterio, evidencia y matices.", "Sé reconocer falacias.", "Sé responder contraargumentos."],
    explain=[
        "Un debate estético es un intercambio organizado de juicios con razones sobre una misma obra. Tiene un formato con turnos y tiempos para que todas las personas puedan hablar: apertura (cada equipo expone su juicio), réplica (responde al otro equipo), preguntas del público y cierre (cada equipo resume su postura, con matices). Para prepararlo se escriben el juicio, dos evidencias y un contraargumento previsible con su réplica.",
        "El respeto se organiza con normas: hablar por turnos, citar al otro con exactitud, preguntar antes de refutar, no descalificar a nadie y no comparar cuerpos. La retroalimentación entre pares sigue un formato descriptivo: observo (un hecho), esto produce (un efecto) y me pregunto si (una sugerencia como pregunta). Por ejemplo: «observo que la sección 1 dura dos minutos sin cambios; esto produce sensación de espera; me pregunto si un cambio de nivel a la mitad la haría más clara».",
        "Después del debate se revisa el juicio: se anota qué razón de la otra postura fue la más fuerte, qué evidencia se agregaría y si el juicio cambia o se matiza. Cambiar de postura ante una buena razón es parte del aprendizaje. Si alguien se siente incómodo al exponer, se ofrecen alternativas (escribir, hablar en grupo pequeño o ser quien modera) y, ante cualquier malestar, se avisa a una persona adulta de confianza.",
    ],
    vocab=[("debate", "intercambio organizado de razones con turnos y tiempos"), ("apertura", "primera exposición de cada equipo"), ("réplica", "respuesta a lo dicho por el otro equipo"), ("moderador/a", "persona que cuida los turnos y las normas"), ("retroalimentación descriptiva", "comentario con hecho, efecto y pregunta"), ("juicio final", "juicio revisado después del debate")],
    worked=[
        ("Calcular el tiempo de un debate", "Cada uno de 2 equipos habla 3 minutos de apertura y 2 de réplica. ¿Cuántos minutos suman esas intervenciones?", ["Cada equipo habla 3 + 2 = 5 minutos.", "Dos equipos: 5 × 2 = 10 minutos."], "10 minutos"),
        ("Dar retroalimentación descriptiva", "«No me gustó cómo habló tu equipo». Reescríbelo con el formato observo, produce, me pregunto.", ["Busca un hecho observable, como que no citó la evidencia.", "Escribe: observo que no citaron una evidencia; esto produce dudas; me pregunto si podrían agregar un rasgo de la sección 2."], "Observo que no citaron una evidencia; esto produce dudas; me pregunto si podrían agregar un rasgo"),
    ],
    mistakes=[("Debatir para «ganar» y no para entender la obra.", "El objetivo es afinar juicios, no vencer a otras personas.", "Escucha, pregunta y ajusta tu juicio con las mejores razones."),
              ("Dar retroalimentación sobre la persona («eres muy nervioso»).", "La retroalimentación es sobre el argumento y la exposición, no sobre cómo es alguien.", "Usa observo, esto produce y me pregunto si.")],
    T=[
        ('abc', 'En creación en danza, ¿qué es un debate estético?', 'Un intercambio organizado de juicios con razones sobre una obra', 'Una competencia donde gana quien habla más fuerte o con más seguridad', 'Una conversación sin turnos ni normas sobre lo que gustó', 'El debate es organizado y con razones; no es una competencia ni una charla sin normas.'),
        ('abc', '{F} ¿Cuántos minutos dura la apertura de cada equipo?', '3 minutos', '2 minutos', '4 minutos', 'La ficha dice que la apertura de cada equipo dura 3 minutos.'),
        ('=', '{F} ¿Cuántos minutos suman aperturas y réplicas de los dos equipos?', '2*(3+2)', 'Cada equipo habla 3 minutos de apertura y 2 de réplica, y hay dos equipos.', ' minutos'),
        ('=', '{F} ¿Cuántos minutos dura todo el debate, con aperturas, réplicas, preguntas y cierres de ambos equipos?', '2*(3+2+1)+4', 'Cada equipo usa 6 minutos y se agregan 4 de preguntas.', ' minutos'),
        ('abc', '{F} ¿Qué norma ayuda a no distorsionar lo que dijo el otro equipo?', 'Citar con exactitud', 'Hablar más rápido', 'Hablar al mismo tiempo', 'Citar con exactitud evita deformar el argumento ajeno.'),
        ('abc', '{F} ¿Cuál retroalimentación sigue el formato observo, produce, me pregunto?', 'Observo que la sección 1 dura dos minutos sin cambios; esto produce espera; me pregunto si un cambio ayudaría', 'Tu equipo estuvo muy mal y se notó que no prepararon nada ni ensayaron lo que iban a decir', 'Me aburrí porque me pareció largo y poco interesante, y estoy segura de que a todo el curso le pasó lo mismo', 'La primera da un hecho, un efecto y una pregunta; las otras opinan o descalifican.'),
        ('abc', '{F} ¿Cuál es el matiz del juicio final del equipo 1?', 'Reconoce que la sección 1 es larga', 'Dice que la obra es perfecta', 'Cambia el tema del debate', 'El juicio admite que la sección 1 es larga.'),
        ('abc', '{F} Un integrante del equipo 2 propone citar a «una profesora famosa» como razón principal. ¿Qué corresponde?', 'Señalar la falacia de autoridad y buscar evidencia', 'Aceptarlo, porque una persona famosa tiene razón', 'Pedir que se cite a otra persona más famosa', 'La fama no es evidencia; hay que volver a la obra.'),
        ('abc', '{F} Un integrante dice que la persona del equipo 1 es «muy nerviosa y por eso su juicio no vale». ¿Qué corresponde?', 'Recordar que se debate sobre razones y no sobre cómo es la persona', 'Aceptar el comentario, porque el nerviosismo es un hecho observable que se nota', 'Pedirle que repita su turno hasta que se calme', 'El comentario es un ataque personal y no responde a la razón.'),
        ('abc', 'Dos estudiantes discuten: una dice que el equipo que más convence al público «tiene razón»; el otro, que un juicio se evalúa por criterio y evidencia. ¿Quién argumenta mejor?', 'El otro, porque convencer no es lo mismo que argumentar bien', 'La primera, porque si convence al público es que tenía la razón en ese tema', 'Ninguno, porque en un debate no hay razones que revisar', 'Convencer puede lograrse con falacias; un buen juicio se apoya en criterio y evidencia.'),
        ('abc', '{F} Después del debate, el equipo 2 escucha una razón fuerte del equipo 1 y ajusta su juicio. ¿Qué se puede decir?', 'Que revisó su juicio con evidencia, un buen resultado', 'Que perdió el debate por no defender su postura hasta el final', 'Que debe pedir disculpas al equipo 1 por equivocarse', 'Ajustar un juicio ante una buena razón es parte de aprender.'),
        ('abc', '{F} Una integrante del equipo 2 no quiere hablar frente a todo el curso. ¿Qué alternativa es adecuada?', 'Ofrecerle escribir su parte o hablar en un grupo pequeño', 'Obligarla a hablar para que supere el miedo', 'Pedir que otra persona hable siempre por ella sin preguntarle', 'Nadie está obligado a exponerse; se ofrecen otras formas de participar.'),
        ('abc', 'Durante el debate, alguien se enoja y levanta mucho la voz. ¿Qué corresponde hacer a la persona que modera?', 'Recordar las normas, hacer una pausa y avisar a una persona adulta', 'Dejar que siga hablando fuerte hasta que se calme sola, sin intervenir en el debate', 'Dar el turno de inmediato al otro equipo para que le conteste', 'La moderación cuida las normas y el bienestar del grupo, con apoyo adulto si hace falta.'),
    ],
    ctx=('abc', 'Un curso termina un debate y debe escribir su juicio final sobre «Vaivén». ¿Cuál es el más completo?', 'Logra comunicar calma por el paso de la repetición a la quietud, aunque la sección 1 es larga', 'Es una gran obra, porque la mayoría del curso aplaudió y se quedó hasta el final con ganas de más', 'No sirve, porque el otro equipo habló más fuerte y con más seguridad que el mío', 'Solo el primero tiene afirmación, evidencia, matiz y reconoce una razón ajena.'),
    sc=[
        ("En creación en danza: ¿cuál es el objetivo de un debate estético?", "Afinar juicios con razones, no vencer a otras personas", "Se busca entender mejor la obra."),
        ("¿Qué formato tiene la retroalimentación descriptiva?", "Observo, esto produce y me pregunto si", "Da un hecho, un efecto y una sugerencia como pregunta."),
        ("¿Qué se hace si alguien no quiere hablar frente al curso?", "Se le ofrece escribir o hablar en un grupo pequeño", "No se expone a nadie a la fuerza."),
    ],
    op=("Prepara un debate corto para dos equipos sobre una obra inventada tuya o sobre «Vaivén». Escribe: (1) un juicio de apertura con criterio y evidencia (para el equipo 1) y otro distinto (para el equipo 2); (2) un contraargumento y una réplica para cada uno; (3) una retroalimentación descriptiva al otro equipo con el formato observo, esto produce, me pregunto si; (4) tu juicio final revisado. Calcula el tiempo total del debate con aperturas de 2 minutos, réplicas de 1 minuto y cierres de 1 minuto por equipo y 3 minutos de preguntas.",
        "Obra: «Vaivén». Equipo 1: logra calma porque la quietud final retoma el comienzo. Equipo 2: no desarrolla su idea porque la sección 1 se repite sin cambios. Contraargumento 1: la sección 1 es muy larga; réplica: sirve para marcar la espera. Retroalimentación: observo que la sección 1 dura dos minutos sin cambios; esto produce sensación de espera; me pregunto si un cambio de nivel la aclararía. Juicio final: logra calma, aunque la sección 1 es larga. Tiempo: 2 × (2 + 1 + 1) + 3 = 11 minutos.",
        ["los juicios de ambos equipos tienen criterio y evidencia", "la retroalimentación sigue el formato descriptivo", "el cálculo del tiempo es correcto"],
        ["hoja con juicios, réplicas, retroalimentación, juicio final y cálculo"],
        ["debatir para ganar y no para entender", "descalificar a personas", "retroalimentación opinativa sobre la persona"],
        "Pregunta: «¿qué razón del otro equipo te hizo ajustar tu juicio?». Si dice «ninguna», pídele que busque una razón que sí sea válida."),
    reinforce="Escribe tres retroalimentaciones descriptivas (observo, esto produce, me pregunto si) sobre una presentación imaginaria y verifica que ninguna hable de la persona.",
    extend="Explica por qué cambiar un juicio después de un debate es una muestra de pensamiento crítico y no de debilidad.",
)

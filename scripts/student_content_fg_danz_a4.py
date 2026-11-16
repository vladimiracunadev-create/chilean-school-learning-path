"""Danza 3.º y 4.º medio FG: OAC-04 (interpretación estética y contextual de obras de danza), clases 1 a 5. Obras inventadas descritas por escrito; sin video real."""
from __future__ import annotations

from fg_danz_common import build

O4 = "FG-DANZ-3y4-OAC-04"

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (obra de ejemplo «Marea», inventada, descrita por escrito). Seis intérpretes, 5 minutos. Empiezan en línea, de pie, con los brazos ondulando lento en nivel medio (energía suave y continua). "
     "A los 2 minutos se separan en dos grupos de tres que se cruzan en diagonal con pasos más rápidos. A los 4 minutos vuelven a la línea y bajan poco a poco a nivel bajo, hasta quedar quietos. "
     "La luz de sala pasa de encendida a baja en el último minuto. La música fue creada por el grupo: percusión suave.")
build(
    O4, 1, F,
    use="Aprenderé a mirar una obra de danza en pasos: describir lo que se ve, analizar cómo está hecho, interpretar qué puede significar y recién entonces opinar, separando siempre los hechos de las impresiones.",
    prior=["Reconozco espacio, tiempo y energía.", "Sé qué es la puesta en escena.", "Sé que una lectura se apoya en evidencia observable."],
    explain=[
        "Interpretar una obra de danza es dar sentido a lo que se ve usando evidencia. Conviene hacerlo en cuatro pasos. Primero se describe: se dice qué se ve y qué se oye, sin opiniones (seis intérpretes, brazos ondulando lento). Segundo se analiza: se relaciona cómo están usados el espacio, el tiempo, la energía y la puesta en escena (la línea se separa en dos grupos). Tercero se interpreta: se propone qué podría significar (la ola que viene y va). Cuarto se emite un juicio: se dice si la obra logra lo que parece buscar, con razones.",
        "La descripción debe poder ser comprobada por cualquier persona que haya visto la obra. Si se escribe «es hermosa», eso es un juicio. Si se escribe «el grupo baja a nivel bajo en el último minuto», es una descripción. La interpretación se marca como posible («podría sugerir») porque otras personas pueden ver otras cosas con la misma evidencia.",
        "Este cuaderno usa obras inventadas y descritas por escrito, porque no hay video. En clase, tu docente puede mostrar una obra con autorización y derechos. Se comenta el trabajo artístico, nunca el cuerpo de las personas que bailan.",
    ],
    vocab=[("descripción", "decir qué se ve y se oye sin opinar"), ("análisis", "relacionar cómo están usados los elementos"), ("interpretación", "propuesta posible de significado, con evidencia"), ("juicio", "valoración razonada de si la obra logra su propósito"), ("evidencia", "dato observable que apoya una afirmación")],
    worked=[
        ("Separar descripción de juicio", "Clasifica: (a) «a los 4 minutos vuelven a la línea»; (b) «el final es muy emocionante».", ["La (a) se puede comprobar viendo la obra: es descripción.", "La (b) expresa una valoración personal: es juicio."], "(a) descripción, (b) juicio"),
        ("Ordenar los pasos", "Ordena: interpretar, describir, analizar, juzgar.", ["Se parte por lo observable: describir.", "Luego analizar, interpretar y juzgar."], "Describir, analizar, interpretar, juzgar"),
    ],
    mistakes=[("Empezar por «me gustó» o «no entendí nada».", "Un juicio sin descripción no tiene base compartida.", "Describe primero lo que viste y oíste."),
              ("Afirmar que la obra «significa» algo como hecho único.", "La misma evidencia admite otras lecturas.", "Escribe «podría sugerir» y menciona la evidencia que lo apoya.")],
    T=[
        ('abc', '¿Qué es una descripción de una obra de danza?', 'Decir qué se ve y se oye sin opinar', 'Decir si la obra fue buena o mala, con razones', 'Proponer qué idea quiso comunicar el grupo', 'Describir es el primer paso y se limita a lo observable.'),
        ('abc', '{F} ¿Cuál es una descripción?', 'A los 2 minutos se separan en dos grupos de tres', 'La obra transmite una gran tristeza', 'Es la mejor obra del festival', 'Los dos grupos de tres se pueden comprobar; los otros son interpretación o juicio.'),
        ('abc', '{F} ¿Cuál afirmación es un juicio?', 'La obra logra mostrar la calma final', 'La luz pasa de encendida a baja', 'Hay seis intérpretes', 'Decir que «logra» valora el resultado; las otras son descripciones.'),
        ('=', '{F} La obra dura 5 minutos y la separación en dos grupos empieza a los 2. ¿Cuántos segundos faltan para el final desde ese momento?', '(5-2)*60', 'Se restan los minutos y se convierten a segundos.', ' segundos'),
        ('abc', '{F} Una estudiante escribe: «la energía suave y continua de la línea inicial cambia a pasos más rápidos en el cruce». ¿Qué paso del método realiza?', 'Analiza, porque relaciona cómo cambian la energía y el tiempo entre dos partes', 'Emite un juicio, porque valora si la obra es buena', 'Interpreta, porque dice qué significa la obra', 'Relacionar cómo se usan los elementos en distintas partes es analizar; no valora ni propone un significado.'),
        ('abc', 'Interpretar implica', 'proponer un significado posible apoyado en lo observado', 'decir lo que la obra significa de manera definitiva', 'repetir la descripción con otras palabras', 'La interpretación es una propuesta basada en evidencia.'),
        ('abc', '{F} Quieres interpretar el cambio a nivel bajo del final. ¿Qué escritura es mejor?', 'Podría sugerir calma o descanso, porque los intérpretes bajan despacio y quedan quietos', 'Significa que representan algo triste y es seguro, porque bajan al suelo', 'Es lo mejor de la obra, porque el final siempre es lo más importante', 'Se marca como posible y se apoya en evidencia.'),
        ('abc', '{F} Una estudiante escribe «la música es horrible». ¿Qué falta para que sea un juicio fundado?', 'Decir qué rasgos de la música observó y qué criterio usó', 'Repetir que es horrible con más énfasis', 'Decir que a ella no le gusta ese tipo de música', 'Un juicio necesita razones con evidencia.'),
        ('=', '{F} Si cada tiempo del cruce en diagonal dura 2 segundos y el cruce tiene 16 tiempos, ¿cuántos segundos dura?', '16*2', 'Se multiplican los tiempos por los segundos de cada uno.', ' segundos'),
        ('abc', 'Dos personas ven la misma obra. Una interpreta «amistad» y otra «despedida». ¿Qué conclusión es más razonable?', 'Ambas lecturas pueden valer si se apoyan en evidencia observada', 'Una de las dos está equivocada necesariamente y hay que averiguar cuál', 'La obra no tiene sentido si cada persona entiende algo distinto de ella', 'Las interpretaciones varían y se evalúan por su evidencia.'),
        ('abc', 'Alguien comenta que «el intérprete de la derecha no tiene cuerpo de bailarín». ¿Qué corresponde?', 'Redirigir el comentario hacia el movimiento y no hablar del cuerpo', 'Responder con otro comentario sobre el cuerpo del intérprete para equilibrar la crítica', 'Aceptarlo como parte de la crítica, porque en danza el cuerpo también se evalúa', 'El cuerpo de las personas no se evalúa.'),
        ('=', 'La obra se presentó 3 veces el mismo día, con 10 minutos de entrada y salida del público en cada función además de los 5 minutos de obra. ¿Cuántos minutos duró en total?', '3*(5+10)', 'Cada función dura 15 minutos y son tres.', ' minutos'),
        ('abc', 'Quieres comentar la obra con una persona que no la vio. ¿Qué te sirve primero?', 'Describir en orden qué se veía, cómo se movía y qué se oía', 'Decir si te gustó o no', 'Contar lo que sentiste sin mencionar nada de lo visto', 'La descripción es la base compartida.'),
    ],
    ctx=('abc', 'Una compañera escribe sobre «Marea»: «Los seis se mueven lento al inicio, se cruzan en diagonal con pasos más rápidos y vuelven a la línea para quedar quietos. Podría sugerir una ola que va y vuelve; me pareció logrado el final porque la luz baja acompaña la quietud». ¿Qué pasos usó?', 'Describió, interpretó con prudencia y emitió un juicio con razón', 'Solo emitió un juicio sobre el final y no describió nada de lo que vio', 'Solo describió lo que pasó en la obra y no propuso ningún significado', 'El texto incluye lo observado, una propuesta posible y una valoración con motivo.'),
    sc=[
        ("En Danza: ¿qué es una descripción?", "Decir qué se ve y se oye sin opinar", "La descripción es el primer paso y se limita a lo observable."),
        ("¿Cómo se escribe una interpretación?", "Como propuesta posible apoyada en evidencia", "Con la misma evidencia puede haber otras lecturas posibles."),
        ("¿Se comenta el cuerpo de las personas que bailan?", "No, se comenta el trabajo artístico", "Se respeta a las personas que bailan y solo se comenta el trabajo."),
    ],
    op=("Imagina una obra breve (inventada por ti) de tres escenas. Escribe una descripción de 3 líneas, un análisis de un elemento (espacio, tiempo o energía), una interpretación prudente y un juicio con razón.",
        "Obra «Puente»: dos filas se acercan despacio, se encuentran en el centro y se separan. Análisis: la energía es suave y la trayectoria recta. Interpretación: podría sugerir un reencuentro. Juicio: el encuentro es claro porque la quietud en el centro se nota.",
        ["separa los cuatro pasos", "usa evidencia observable", "no opina del cuerpo de las personas"],
        ["hoja con cuatro párrafos breves"],
        ["mezclar descripción y juicio", "interpretar como hecho único"],
        "Pregunta: «¿qué viste que lo apoye?». Si no puede citar, pídele volver a la descripción."),
    reinforce="Escribe una descripción de 4 líneas de una escena cotidiana en movimiento, sin juicios.",
    extend="Explica por qué dos personas pueden interpretar distinto la misma obra y las dos tener razón.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (obra de ejemplo «Cruce», inventada). Cuatro intérpretes con ropa gris. Tiempo: un pulso lento al inicio y luego más rápido. Espacio: trayectorias rectas que se cruzan en el centro; nivel medio. "
     "Energía: cortada, con detenciones breves. Puesta en escena: luz de sala encendida, sin música; solo se oyen los pasos. "
     "Idea posible: personas que se encuentran en un lugar de paso y siguen su camino.")
build(
    O4, 2, F,
    use="Aprenderé a aplicar criterios estéticos para interpretar una obra: lenguaje de la danza, puesta en escena, emociones o sensaciones que genera e ideas que sugiere.",
    prior=["Sé describir, analizar, interpretar y juzgar.", "Reconozco elementos del lenguaje de la danza.", "Sé que un juicio necesita razones."],
    explain=[
        "Un criterio estético es una pregunta o aspecto que se usa para mirar una obra de manera ordenada. Cuatro criterios útiles son: el lenguaje de la danza (cómo se usan el cuerpo, el espacio, el tiempo y la energía), la puesta en escena (luz, vestuario, sonido, espacio escénico), las emociones o sensaciones que genera en quien mira, y las ideas que sugiere. Cada criterio permite observar un tipo de evidencia distinta.",
        "Usar criterios evita comentarios vagos. Por ejemplo, en «Cruce», las trayectorias rectas que se cruzan en el centro son evidencia del criterio de espacio; la energía cortada con detenciones y el pulso que se acelera son evidencia de tiempo y energía; el silencio con el sonido de pasos es evidencia de puesta en escena. Después se relacionan: la energía cortada y el cruce podrían producir una sensación de tensión o apuro.",
        "Las emociones y sensaciones dependen de quien mira. Por eso se expresan como «a mí me generó» y se apoyan en un rasgo observable. Quien comenta nunca juzga el cuerpo de las personas y propone sus ideas con respeto.",
    ],
    vocab=[("criterio estético", "aspecto con que se mira una obra"), ("lenguaje de la danza", "uso del cuerpo, espacio, tiempo y energía"), ("sensación", "lo que percibe quien mira"), ("idea", "tema o pensamiento que sugiere la obra"), ("evidencia", "rasgo observable que apoya una lectura")],
    worked=[
        ("Asignar evidencia a un criterio", "En la ficha, ¿bajo qué criterio entra «sin música; solo se oyen los pasos»?", ["Habla del sonido y de la luz, decisiones de escena.", "Corresponde a puesta en escena."], "Puesta en escena"),
        ("Relacionar criterios", "¿Qué sensación pueden generar el pulso que se acelera y la energía cortada?", ["El pulso acelerado sugiere urgencia.", "Las detenciones breves aportan tensión: una sensación de apuro o inquietud."], "Una sensación de apuro o tensión"),
    ],
    mistakes=[("Comentar la obra sin decir qué criterio se usa.", "Quedan impresiones sueltas.", "Nombra el criterio y el rasgo que lo apoya."),
              ("Decir que una sensación es «la correcta».", "La sensación depende de quien mira.", "Di «a mí me generó…» y cita el rasgo observado.")],
    T=[
        ('abc', '¿Qué es un criterio estético?', 'Un aspecto con que se mira una obra para comentarla con orden', 'Una regla que todas las obras deben cumplir sin excepción', 'Una opinión personal sobre la obra, sin razones', 'Un criterio ordena la mirada y evita comentarios vagos.'),
        ('abc', '{F} «Trayectorias rectas que se cruzan en el centro» es evidencia de', 'espacio', 'energía', 'sonido', 'Las trayectorias son parte del espacio.'),
        ('abc', '{F} «Energía cortada con detenciones» pertenece a', 'el lenguaje de la danza', 'la puesta en escena, porque se nota desde la sala', 'las ideas que sugiere, ya que las detenciones son una idea', 'La energía es un elemento del lenguaje.'),
        ('abc', '{F} «Luz de sala encendida» es', 'puesta en escena', 'una emoción', 'un movimiento', 'La luz es una decisión de escena.'),
        ('=', '{F} Cada intérprete cruza 5 veces el centro durante la obra. ¿Cuántos cruces hay en total?', '4*5', 'Se multiplican los intérpretes por los cruces de cada uno.', ' cruces'),
        ('abc', '¿Cuál es una forma correcta de expresar una sensación?', 'A mí me generó apuro, porque las detenciones eran breves y el pulso se aceleraba', 'La obra produce apuro en todo el público y así lo entendió todo el curso', 'Todos deberían sentir apuro con esta obra, porque el grupo lo pretendía', 'La sensación se atribuye a quien mira y se apoya en un rasgo.'),
        ('abc', '{F} ¿Qué idea posible sugiere la ficha?', 'Personas que se encuentran en un lugar de paso y siguen su camino', 'Una fiesta con mucha gente', 'Una competencia deportiva, en la cual gana quien llega primero', 'La ficha lo declara como idea posible.'),
        ('abc', '{F} Una compañera dice «la obra tiene mucha energía». ¿Qué le pides?', 'Que indique qué rasgo observó, como energía cortada o pulso rápido', 'Que repita que tiene mucha energía, pero con más convicción y detalle', 'Que cambie su opinión por la tuya, porque la tuya está mejor fundada', 'Un criterio se apoya en evidencia.'),
        ('=', '{F} Si el pulso lento marca 40 pasos en 80 segundos, ¿cuántos segundos dura cada paso?', '80//40', 'Se dividen los segundos entre los pasos.', ' segundos'),
        ('abc', 'Dos estudiantes comentan «Cruce». Una dice que sugiere encuentro; otro, que sugiere separación. ¿Qué es lo más razonable?', 'Pedirles evidencia a cada uno y comparar cuál se apoya mejor', 'Decidir que una persona se equivoca', 'Ignorar las dos y quedarse con la del docente', 'Las lecturas se contrastan con evidencia.'),
        ('abc', 'Quieres comentar la puesta en escena de una obra sin música. ¿Qué observas?', 'Qué efecto produce el silencio y el sonido de los pasos, y cómo se usa la luz', 'Si la música es de un autor famoso y está bien interpretada', 'Si el vestuario es de moda y combina con los colores del escenario', 'El silencio es una decisión de escena.'),
        ('=', 'La obra dura 6 minutos. Si la primera mitad tiene pulso lento y la segunda, rápido, ¿cuántos segundos dura la parte de pulso lento?', '6*60//2', 'Se pasa a segundos y se toma la mitad.', ' segundos'),
        ('abc', 'Un comentario dice que «el intérprete del medio es muy fuerte». ¿Cómo se reformula con criterios?', 'Su energía en el cruce central es fuerte y marca el cambio de sección', 'Es el más fuerte de los cuatro y se nota por cómo se ve su cuerpo', 'Debe parecer más delgado para que se vea más ligero en el cruce', 'Se comenta el movimiento y no el cuerpo.'),
    ],
    ctx=('abc', 'Una estudiante escribe sobre «Cruce»: «En espacio, las trayectorias rectas se cruzan en el centro; en energía, las detenciones breves producen tensión; en escena, el silencio deja oír los pasos. A mí me generó apuro. La idea podría ser personas en un lugar de paso». ¿Qué hizo bien?', 'Usó tres criterios con evidencia y expresó su sensación en primera persona', 'Solo dio una opinión sobre la obra y su sensación sin usar criterios ni evidencia', 'Solo describió la ropa gris y la luz de la sala sin analizar el movimiento', 'El texto nombra criterios, evidencia y sensación personal.'),
    sc=[
        ("En Danza: ¿qué es un criterio estético?", "Un aspecto para mirar una obra con orden", "Los criterios ayudan a comentar una obra con evidencia."),
        ("¿Cómo se expresa una sensación?", "En primera persona y con un rasgo que la apoye", "La sensación depende de quien mira, por eso se dice en primera persona."),
        ("¿Se comenta el cuerpo de la persona?", "No, se comenta el movimiento", "Se respeta a las personas que bailan y solo se comenta el trabajo."),
    ],
    op=("Elige una obra inventada de dos o tres líneas. Escribe un comentario con tres criterios: lenguaje de la danza, puesta en escena y una sensación en primera persona con su evidencia.",
        "Obra: seis personas caminan en círculo, lento, en silencio. Lenguaje: trayectoria circular y pulso lento. Escena: luz tenue y silencio. Sensación: a mí me generó calma, porque el círculo y el silencio eran regulares.",
        ["usa al menos tres criterios", "cita evidencia", "expresa la sensación como propia"],
        ["hoja con tres párrafos breves"],
        ["comentarios vagos", "comentar el cuerpo de las personas"],
        "Pregunta: «¿qué criterio estás usando?». Si no sabe, pídele que lo nombre."),
    reinforce="Escribe tres frases con un criterio cada una sobre una escena imaginada.",
    extend="Explica por qué la misma obra puede generar distintas sensaciones sin que ninguna sea incorrecta.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (obra de ejemplo «Paraguas», inventada). Cinco intérpretes con un paraguas cerrado de colores distintos. Primero caminan separados, mirando al suelo, con pasos cortos. "
     "Luego se acercan y los paraguas se abren al mismo tiempo, formando un círculo; entonces la mirada pasa del suelo al frente y el ritmo se hace parejo. "
     "Al final, cada uno cierra el paraguas y camina a su lugar. La luz es suave y sin música.")
build(
    O4, 3, F,
    use="Aprenderé a interpretar el propósito expresivo de una obra con la estructura afirmación, evidencia y criterio, y a reconocer lecturas que no se apoyan en lo observado.",
    prior=["Sé describir y analizar elementos.", "Sé aplicar criterios estéticos.", "Sé que la interpretación se marca como posible."],
    explain=[
        "El propósito expresivo de una obra es aquello que parece querer comunicar: una emoción, una idea, una situación. No siempre lo declaran sus creadores; se infiere a partir de las decisiones que se observan. Una forma ordenada de explicarlo es la estructura afirmación, evidencia y criterio: se dice qué propósito parece tener (afirmación), qué rasgo observable lo apoya (evidencia) y desde qué aspecto se mira (criterio).",
        "Por ejemplo, en «Paraguas»: «Parece hablar de pasar del aislamiento a la unión (afirmación), porque primero caminan separados mirando al suelo y luego forman un círculo con paraguas abiertos y mirada al frente (evidencia), según el criterio de uso del espacio y de la mirada (criterio)». Una afirmación sin evidencia, como «habla de la lluvia», no se puede comprobar con la ficha.",
        "Siempre es posible que haya otras lecturas. Quien interpreta debe estar dispuesto a revisar su propuesta si encuentra más evidencia. No se juzgan los cuerpos y se evita atribuir intenciones privadas a las personas que bailan.",
    ],
    vocab=[("propósito expresivo", "lo que la obra parece querer comunicar"), ("inferir", "concluir algo a partir de evidencia"), ("afirmación", "lo que se propone sobre la obra"), ("evidencia", "rasgo observable que la apoya"), ("criterio", "aspecto desde el cual se mira")],
    worked=[
        ("Armar una interpretación", "Usa afirmación, evidencia y criterio para el final de «Paraguas».", ["Afirmación: el final podría sugerir regreso a lo cotidiano.", "Evidencia: cada uno cierra el paraguas y camina a su lugar; criterio: uso del espacio."], "Podría sugerir regreso a lo cotidiano, porque cierran el paraguas y caminan a su lugar (espacio)"),
        ("Detectar falta de evidencia", "«La obra trata de una tormenta fuerte». ¿Qué falta?", ["La ficha no menciona rayos ni energía fuerte.", "No hay evidencia observable que lo apoye."], "Falta evidencia"),
    ],
    mistakes=[("Escribir solo la afirmación («habla de la soledad»).", "Sin evidencia nadie puede comprobarla.", "Agrega el rasgo observable y el criterio."),
              ("Inventar datos para sostener la lectura («el grupo usó música triste»).", "La ficha dice que no hay música.", "Usa solo lo que se observa en la obra descrita.")],
    T=[
        ('abc', '¿Qué es el propósito expresivo de una obra?', 'Lo que parece querer comunicar', 'El tiempo que dura sin pausas', 'El lugar donde se presenta', 'Es el sentido que la obra parece buscar.'),
        ('abc', '{F} ¿Qué rasgo observable muestra aislamiento al comienzo?', 'Caminan separados, mirando al suelo, con pasos cortos', 'Los paraguas se abren al mismo tiempo', 'Hay un círculo en el centro del espacio, formado por las personas', 'Lo separado y con la mirada al suelo sugiere aislamiento.'),
        ('abc', '{F} Los paraguas que se abren a la vez forman', 'un círculo', 'una línea', 'una diagonal', 'La ficha dice que forman un círculo.'),
        ('abc', 'En la estructura afirmación, evidencia y criterio, la evidencia es', 'el rasgo observable que apoya la afirmación', 'la opinión personal de quien comenta', 'el título de la obra', 'La evidencia es lo que se ve y se oye.'),
        ('abc', '{F} ¿Cuál es una afirmación con evidencia?', 'Parece hablar de unión, porque forman un círculo y miran al frente', 'Parece hablar de unión, porque a mí me gusta la unión', 'Parece hablar de unión y es lo que todos entienden', 'La primera cita rasgos observables de la obra y las otras no.'),
        ('=', '{F} Cada uno de los 5 intérpretes da 6 pasos cortos hasta acercarse. ¿Cuántos pasos dan entre todos?', '5*6', 'Se multiplican los intérpretes por los pasos.', ' pasos'),
        ('abc', '{F} «La obra habla de una tormenta fuerte» no se sostiene porque', 'la ficha no muestra rasgos que lo apoyen', 'las tormentas no se pueden mostrar con danza', 'los paraguas son de colores', 'Una afirmación necesita evidencia en la obra.'),
        ('abc', '{F} Un compañero propone que el final sugiere «cada quien vuelve a su rutina». ¿Qué evidencia usarías?', 'Cada uno cierra el paraguas y camina a su lugar', 'Los paraguas son de colores distintos', 'La luz es suave y sin música', 'Cerrar el paraguas y volver al lugar apoya esa lectura.'),
        ('=', '{F} La obra tiene 3 partes iguales de 90 segundos. ¿Cuántos segundos dura?', '3*90', 'Se multiplican las partes por su duración.', ' segundos'),
        ('abc', 'Una estudiante dice «yo creo que eso quiere decir pobreza» sin mostrar evidencia. ¿Qué respondes?', 'Que indique qué vio que lo sugiere, para poder comparar con otras lecturas', 'Que tiene razón porque es su opinión y todas las opiniones valen igual', 'Que está equivocada, porque la pobreza no puede mostrarse con paraguas', 'La lectura se discute con evidencia.'),
        ('abc', 'Dos lecturas de «Paraguas»: pasar del aislamiento a la unión, o que la lluvia es fuerte. ¿Cuál se apoya mejor en la ficha?', 'Pasar del aislamiento a la unión, porque hay pasos separados y círculo final', 'La lluvia fuerte, porque hay paraguas y los paraguas se usan con lluvia', 'Ninguna', 'La ficha da evidencia de la lectura de unión y no de la de lluvia fuerte.'),
        ('=', 'La obra se presenta a 4 cursos, uno tras otro, con 5 minutos de cambio entre cursos (hay 3 cambios) y cada función dura 8 minutos. ¿Cuántos minutos dura todo?', '4*8+3*5', 'Se suman las funciones y los cambios.', ' minutos'),
        ('abc', 'Alguien dice que el intérprete del medio parece triste «por cómo es él». ¿Qué corresponde?', 'Hablar solo de los rasgos de movimiento y no atribuir cosas a la persona', 'Aceptar que se comente su vida privada, porque ayuda a entender por qué baila así', 'Preguntarle a él por su vida personal para saber si de verdad está triste', 'La interpretación se hace sobre la obra, no sobre las personas.'),
    ],
    ctx=('abc', 'Para «Paraguas», una estudiante afirma: «Habla de unión». Otra: «Habla de miedo a la lluvia». Ambas dan una evidencia. La primera: círculo con paraguas abiertos; la segunda: pasos cortos al comienzo. ¿Qué conviene hacer?', 'Reunir toda la evidencia de la ficha y ver cuál lectura explica más rasgos', 'Elegir la lectura que suene más poética y deje a todas las personas conformes', 'Descartar las dos lecturas y empezar otra desde cero sin mirar la ficha', 'Se compara qué lectura explica más evidencia.'),
    sc=[
        ("En Danza: ¿qué se necesita para sostener una interpretación?", "Evidencia observable y criterio", "Sin ella no se puede comprobar."),
        ("En Danza: ¿Qué es inferir?", "Concluir algo a partir de evidencia", "Inferir es razonar a partir de lo observado y no inventar."),
        ("¿Se atribuyen intenciones privadas a las personas que bailan?", "No", "La lectura se hace sobre la obra."),
    ],
    op=("Elige una obra inventada de dos o tres líneas. Escribe una interpretación con afirmación, evidencia y criterio, marcándola como posible. Luego escribe una lectura alternativa y explica cuál tiene más evidencia.",
        "Obra: tres personas bajan lento al suelo y se levantan juntas. Afirmación: podría sugerir cuidado mutuo. Evidencia: suben al mismo ritmo. Criterio: tiempo. Alternativa: cansancio. Evidencia menor: no hay signos de agotamiento.",
        ["afirmación, evidencia y criterio", "marca como posible", "compara dos lecturas"],
        ["hoja con interpretación y comparación"],
        ["afirmar sin evidencia", "inventar datos"],
        "Pregunta: «¿en qué parte lo ves?». Si no puede decirlo, pídele que vuelva a la descripción."),
    reinforce="Escribe una afirmación, una evidencia y un criterio para una escena imaginada de danza.",
    extend="Explica por qué cambiar una evidencia puede cambiar la interpretación.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (contexto de ejemplo, inventado). La obra «Marea» fue creada por un colectivo escolar ficticio para el cierre de un taller en el patio de su colegio. Se presentó ante familias y estudiantes, con música creada por el grupo. "
     "Después se repuso en un festival de danza juvenil de una ciudad ficticia, en una sala cerrada. No es una obra ni un colectivo real.")
build(
    O4, 4, F,
    use="Aprenderé a considerar el contexto de una obra (quién la creó, para qué, dónde y ante quién) para interpretarla, sin atribuir hechos que no conozco y sin inventar datos de culturas o pueblos.",
    prior=["Sé interpretar con evidencia.", "Sé que la puesta en escena incluye el espacio.", "Sé que las obras tienen autoría."],
    explain=[
        "El contexto de una obra son las condiciones en las que se creó y se presenta: quién la creó (autoría), con qué propósito, cuándo y dónde, para qué público y en qué ocasión (una muestra escolar, un festival, una ceremonia). Conocer el contexto ayuda a interpretar, porque una obra pensada para un patio ante familias no se mira igual que una creada para una sala de festival.",
        "Se distingue entre contexto de creación (por qué y para qué se hizo), contexto de presentación (dónde y ante quién se muestra) y contexto de quien mira (su experiencia). Es importante usar datos comprobados: si no se conoce el contexto, se dice «no lo sabemos» en lugar de inventarlo. Los datos de este cuaderno son ficticios y sirven para practicar.",
        "Cuando una danza pertenece a una tradición de un pueblo, de una comunidad o de una zona del país, su sentido lo conocen mejor las personas que la practican. La mejor fuente es una persona educadora tradicional o cultora; no se afirman significados sin esa fuente, ni se imitan ritos.",
    ],
    vocab=[("contexto", "condiciones de creación y de presentación de una obra"), ("autoría", "quién creó la obra"), ("ocasión", "motivo por el que se presenta"), ("público", "personas ante quienes se presenta"), ("fuente", "persona o documento que informa un dato")],
    worked=[
        ("Reconocer el contexto de creación", "En la ficha, ¿para qué se creó «Marea»?", ["La ficha dice que fue creada para el cierre de un taller.", "Se mostró en el patio del colegio."], "Para el cierre de un taller escolar"),
        ("Comparar contextos de presentación", "¿Qué cambia entre el patio y la sala cerrada del festival?", ["En el patio hay familias y estudiantes y más espacio abierto.", "En la sala cerrada el público está más cerca y puede haber luz controlada."], "Cambia el público y el tipo de espacio"),
    ],
    mistakes=[("Inventar un contexto histórico para «explicar» la obra.", "Puede ser falso y hace que la interpretación no se apoye en datos.", "Di qué se sabe y qué no, y busca una fuente."),
              ("Afirmar el significado de una danza tradicional sin consultar a quienes la practican.", "Esos significados pertenecen a la comunidad.", "Consulta a una persona educadora tradicional o cultora.")],
    T=[
        ('abc', '¿Qué es el contexto de una obra?', 'Las condiciones en que se creó y se presenta', 'Solo el nombre de la obra y su duración', 'La opinión personal de quien la mira', 'El contexto incluye las condiciones de creación y las de presentación.'),
        ('abc', '{F} ¿Cuántos contextos de presentación se mencionan en la ficha?', 'Dos: el patio del colegio y la sala del festival', 'Uno: el patio, porque la sala no es parte de la obra', 'Tres: patio, sala y calle', 'La ficha nombra dos presentaciones: en el patio y en el festival.'),
        ('abc', '{F} ¿Para qué público fue la primera presentación?', 'Familias y estudiantes', 'Un jurado de expertos', 'Solo otros colectivos', 'La ficha indica que el público fueron familias y estudiantes.'),
        ('abc', '{F} ¿Qué se sabe de la autoría?', 'Fue creada por un colectivo escolar ficticio', 'Fue creada por una compañía profesional famosa', 'No tiene autoría', 'La ficha lo declara ficticio y escolar.'),
        ('abc', '¿Qué haces si no conoces el contexto de una obra?', 'Dices que no lo sabes y buscas una fuente', 'Lo supones y lo cuentas como hecho', 'Dejas de interpretar la obra', 'Cuando falta un dato se reconoce y no se inventa.'),
        ('abc', '{F} Una compañera dice que «Marea» fue creada para una ceremonia religiosa. ¿Qué respondes?', 'Que la ficha no dice eso y que no se puede afirmar', 'Que es posible y lo anotas como dato', 'Que seguro es cierto porque la obra es seria', 'No hay evidencia en la ficha.'),
        ('=', '{F} En la primera presentación hubo 40 familiares y 60 estudiantes. En el festival hubo el triple de personas que en el patio. ¿Cuántas personas hubo en el festival?', '(40+60)*3', 'Se suma el público del patio y se multiplica por 3.', ' personas'),
        ('abc', '{F} Al pasar de patio a sala cerrada, ¿qué decisión de puesta en escena puede cambiar?', 'La luz, que se puede controlar mejor en una sala', 'El tema de la obra, que se vuelve distinto', 'El título', 'Una sala cerrada permite controlar la luz.'),
        ('abc', 'Una danza tradicional de una comunidad se mostrará en el curso. ¿Qué fuente es la más adecuada para entender su sentido?', 'Una persona educadora tradicional o cultora de esa comunidad', 'Un video cualquiera de internet', 'Lo que diga el compañero que más sabe del tema', 'Quienes practican la tradición la conocen mejor.'),
        ('=', 'La sala del festival tiene 80 asientos y se llenó en 3 funciones iguales. ¿Cuántas personas vieron la obra en el festival?', '80*3', 'Se multiplica la capacidad por las funciones.', ' personas'),
        ('abc', 'Dos personas interpretan la obra: una conoce que se creó para un cierre de taller y otra no. ¿Qué diferencia puede haber?', 'La primera puede considerar el carácter de despedida o celebración y la otra solo lo que ve', 'Ninguna, porque el contexto no importa y solo cuentan los movimientos', 'La primera sabe qué significa realmente la obra y la otra se equivoca', 'El contexto da más información, pero no cierra otras lecturas.'),
        ('abc', 'Quieres comentar que una obra «es antigua». ¿Qué debes tener primero?', 'Una fuente que lo confirme', 'La seguridad de tu intuición', 'La opinión de un compañero', 'Un dato como la antigüedad requiere fuente.'),
        ('=', 'Una obra de 5 minutos se presenta en 4 funciones el mismo día, con 25 minutos de pausa entre funciones (3 pausas). ¿Cuántos minutos dura la jornada?', '4*5+3*25', 'Se suman las funciones y las pausas.', ' minutos'),
    ],
    ctx=('abc', 'Un grupo debe comentar una danza que practica una comunidad y no sabe nada de ella. ¿Qué plan es más respetuoso?', 'Invitar a una persona cultora o educadora tradicional y preguntar qué se puede decir y mostrar', 'Inventar un significado a partir de una foto y presentarlo como si fuera cierto', 'Imitar los movimientos que se vieron en un video sin preguntar a nadie', 'Respeta la fuente de la tradición.'),
    sc=[
        ("En Danza: ¿qué es el contexto?", "Condiciones de creación y de presentación", "Conocer el contexto ayuda a interpretar mejor la obra."),
        ("¿Qué se hace con un dato que no se conoce?", "Se dice que no se sabe y se busca una fuente", "Un dato que no se conoce se busca en una fuente y no se inventa."),
        ("¿Quién puede explicar mejor el sentido de una danza tradicional?", "Una persona cultora o educadora tradicional", "Quien practica la tradición es quien mejor conoce su sentido."),
    ],
    op=("Inventa el contexto de una obra ficticia (autoría, ocasión, lugar y público) en 4 líneas. Luego explica cómo cambiaría tu interpretación si la obra se presentara en otro lugar.",
        "Obra «Puente», de un taller de tercer año ficticio, creada para una feria escolar en el gimnasio, ante familias. Si se presentara en una sala pequeña, la cercanía haría más visibles los gestos y la mirada.",
        ["declara cuatro datos ficticios", "relaciona contexto con interpretación", "no inventa significados de pueblos"],
        ["hoja con contexto y comparación"],
        ["afirmar como real un dato inventado", "inventar significados de una tradición"],
        "Pregunta: «¿cómo sabes eso?». Si no tiene fuente, pídele que lo rotule como supuesto."),
    reinforce="Escribe el contexto ficticio de una obra imaginaria con autoría, ocasión, lugar y público.",
    extend="Explica por qué un dato de contexto sin fuente puede perjudicar una interpretación.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 5 (dos interpretaciones de ejemplo de la obra «Marea», ya descrita: seis intérpretes que ondulan en línea, se cruzan en diagonal y vuelven a la línea para quedar quietos; luz que baja; percusión suave). "
     "Interpretación 1: «Parece hablar del ir y venir del mar, porque la línea se separa y vuelve, y la luz baja al final». "
     "Interpretación 2: «Habla de que nadie puede cambiar nada en la vida». Sin más datos.")
build(
    O4, 5, F,
    use="Aprenderé a comparar interpretaciones de una misma obra, decidir cuál se apoya mejor en evidencia y escribir mi propia interpretación fundada y respetuosa.",
    prior=["Sé usar afirmación, evidencia y criterio.", "Sé considerar el contexto.", "Sé respetar otras lecturas."],
    explain=[
        "Dos interpretaciones de una misma obra pueden ser válidas si ambas se apoyan en la evidencia. Para compararlas se revisan tres cosas: cuánta evidencia observable citan, si esa evidencia coincide con lo que realmente ocurre en la obra y si usan criterios estéticos claros. Una lectura puede ser interesante pero débil si no cita nada de lo que se ve.",
        "Un buen texto de interpretación fundada tiene una afirmación marcada como posible, al menos dos evidencias observables y un criterio, y reconoce otras lecturas. Por ejemplo: «Podría sugerir un ir y venir (afirmación), porque la línea se separa y vuelve y la luz baja (evidencia), según espacio y escena (criterio). Otra lectura posible es la calma final». Se escribe con respeto: se comenta la obra, no a las personas, y no se desprecian las lecturas ajenas.",
        "Compartir la interpretación en público es una decisión de cada persona: se puede entregar por escrito o conversarla en grupo pequeño. Todas las voces son bienvenidas y nadie se burla de otra.",
    ],
    vocab=[("lectura", "interpretación de una obra"), ("lectura fundada", "interpretación apoyada en evidencia observable"), ("lectura débil", "interpretación con poca o ninguna evidencia"), ("criterio", "aspecto desde el cual se mira"), ("postura respetuosa", "opinión que no desprecia a personas ni a otras lecturas")],
    worked=[
        ("Comparar dos lecturas", "En la ficha, ¿qué interpretación cita más evidencia?", ["La 1 cita la línea que se separa y vuelve y la luz que baja.", "La 2 no cita ninguna."], "La interpretación 1"),
        ("Reforzar una lectura débil", "¿Cómo se podría mejorar la interpretación 2?", ["Agregar un rasgo observable (por ejemplo, la quietud final).", "Marcarla como posible y decir desde qué criterio se mira."], "Añadiendo evidencia observable y marcándola como posible"),
    ],
    mistakes=[("Elegir la interpretación más dramática como la mejor.", "Lo dramático no es evidencia.", "Evalúa cuánta evidencia observable cita cada una."),
              ("Descalificar una lectura diciendo «eso no tiene sentido» sin razones.", "No ayuda a mejorar y puede ofender.", "Pregunta por la evidencia y propone otra lectura con respeto.")],
    T=[
        ('abc', '¿Qué es una lectura fundada?', 'Una interpretación apoyada en evidencia observable', 'Una interpretación que coincide con la de la mayoría', 'Una interpretación que usa palabras difíciles', 'Se funda en lo que se ve y se oye.'),
        ('abc', '{F} ¿Qué evidencia cita la interpretación 1?', 'La línea que se separa y vuelve y la luz que baja', 'La música triste y el color de la ropa', 'El nombre de los intérpretes', 'La ficha cita línea y luz.'),
        ('abc', '{F} ¿Por qué la interpretación 2 es débil?', 'Porque no cita ninguna evidencia de la obra', 'Porque es negativa y las lecturas negativas no se pueden fundar', 'Porque habla de la vida en general y no de la obra descrita', 'Una lectura sin evidencia es débil.'),
        ('=', '{F} La obra tiene 6 intérpretes y cada uno ondula 4 veces durante la línea inicial. ¿Cuántas ondulaciones hay en total?', '6*4', 'Se multiplican los intérpretes por las ondulaciones.', ' ondulaciones'),
        ('abc', 'Al comparar dos lecturas se revisa', 'cuánta evidencia observable citan y si coincide con la obra', 'cuál es más larga y dramática', 'cuál escribió una persona más conocida o con más experiencia en danza', 'Las lecturas se comparan por la evidencia observable que citan.'),
        ('abc', '{F} ¿Cómo podrías reforzar la interpretación 2 con la ficha?', 'Citando la quietud final y marcándola como lectura posible', 'Escribiendo lo mismo con más énfasis y añadiendo que todos están de acuerdo', 'Quitando la luz que baja de la descripción', 'Se agrega evidencia real y se marca como posible.'),
        ('abc', '{F} Una compañera defiende la interpretación 2 con «porque yo lo siento así». ¿Cuál es una respuesta respetuosa?', 'Valorar su sensación y pedirle qué rasgo de la obra la produjo', 'Decirle que se equivoca porque una sensación no sirve como argumento', 'Ignorarla, porque una sensación personal no cuenta como evidencia', 'Se respeta la sensación y se pide evidencia.'),
        ('=', '{F} Si la obra se cruza en diagonal durante 24 tiempos a 2 segundos cada uno, ¿cuántos segundos dura el cruce?', '24*2', 'Se multiplican los tiempos por los segundos.', ' segundos'),
        ('abc', 'Para escribir una interpretación fundada y respetuosa, ¿qué orden es correcto?', 'Afirmación posible, evidencias, criterio y reconocimiento de otra lectura', 'Juicio final, afirmación y evidencia, en ese orden, sin reconocer otras lecturas', 'Evidencia, burla a otra lectura y afirmación, para dejar clara la diferencia', 'Es el esquema de la clase.'),
        ('abc', 'Una estudiante prefiere entregar su interpretación por escrito y no exponerla. ¿Qué corresponde?', 'Aceptarlo y evaluar su texto', 'Obligarla a exponer su interpretación ante todo el curso', 'No evaluarla, porque no cumplió con exponer en público', 'La exposición es una decisión personal.'),
        ('abc', 'Dos lecturas citan la misma evidencia pero llegan a conclusiones distintas. ¿Qué conclusión es razonable?', 'Ambas pueden ser posibles y se reconocen como lecturas distintas', 'Una es falsa y la otra verdadera, aunque tengan la misma evidencia', 'La obra no tiene sentido si cada persona entiende algo distinto de ella', 'Las lecturas pueden variar con la misma evidencia.'),
        ('=', 'En un taller, 24 estudiantes escriben su interpretación y cada una se lee en 90 segundos. ¿Cuántos minutos se necesitan si se lee una detrás de otra?', '24*90//60', 'Se multiplican los estudiantes por los segundos y se pasa a minutos.', ' minutos'),
        ('abc', 'Alguien comenta «la obra es mala porque los intérpretes no son flexibles». ¿Qué corresponde decir?', 'Que el comentario habla del cuerpo y no de la obra, y que se vuelva a la evidencia de movimiento', 'Que es una buena crítica porque dice algo sincero sobre los intérpretes', 'Que lo repita en voz alta para que todo el curso pueda opinar sobre eso', 'El cuerpo de las personas no se evalúa, solo el movimiento.'),
    ],
    ctx=('abc', 'Dos estudiantes discuten sobre «Marea». Una dice «es sobre el mar» y la otra «es sobre el paso del tiempo». Ambas citan: la línea que se separa y vuelve y la luz que baja. ¿Qué es lo mejor?', 'Reconocer que ambas lecturas son posibles y buscar más evidencia', 'Votar la lectura ganadora entre todo el curso sin revisar la evidencia', 'Pedir a una de las dos que se calle para que no continúe la discusión', 'Con la misma evidencia ambas lecturas siguen siendo posibles.'),
    sc=[
        ("En Danza: ¿qué es una lectura débil?", "Una con poca o ninguna evidencia", "Una lectura sin evidencia no se puede comprobar con la obra."),
        ("¿Cuál es el orden de una interpretación fundada?", "Afirmación, evidencia y criterio", "Es la estructura de la clase."),
        ("¿Se desprecia una lectura distinta?", "No, se pide la evidencia con respeto", "En el grupo todas las voces son bienvenidas y se escuchan con respeto."),
    ],
    op=("Escribe una interpretación fundada (de 4 a 5 líneas) de una obra inventada breve, con afirmación posible, dos evidencias, un criterio y el reconocimiento de otra lectura posible.",
        "Obra: cuatro personas caminan en círculo, lento, cada una con una mano levantada. Podría sugerir un ritual de cuidado (posible). Evidencia 1: el círculo regular. Evidencia 2: la mano levantada que se repite. Criterio: espacio. Otra lectura: espera compartida.",
        ["afirmación posible", "dos evidencias", "reconoce otra lectura"],
        ["hoja con párrafo de interpretación"],
        ["sin evidencia", "juicio sobre los cuerpos"],
        "Pregunta: «¿qué otra lectura podría haber?». Si dice «ninguna», pídele pensar en una."),
    reinforce="Escribe una interpretación fundada de una escena imaginaria, con dos evidencias.",
    extend="Explica por qué reconocer otra lectura mejora tu interpretación.",
)

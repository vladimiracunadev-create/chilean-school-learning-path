"""Lenguaje y Comunicación EPJA Nivel 2, módulo 1 (parte 3): OAD-03, justificar las preferencias literarias (razones con datos del texto, conectores, sinónimos y antónimos, tildes, verbos y ortografía). Textos inventados, en papel."""
from __future__ import annotations

from epja_leco_nb2_common import build

O = "EPJA-LECO-NB2-OAD-03"

F1 = ("Cuento (inventado), «El vecino nuevo»: Cuando don Raúl llegó al pasaje, nadie lo saludó. Él tampoco habló, porque no conocía a nadie. "
      "Un domingo, una vecina le llevó un pan amasado. Don Raúl le agradeció y la invitó a tomar once. Desde entonces el pasaje fue más amable.")

F2 = ("Poema (inventado), «Despedida»: En el andén de la tarde / una mano se levanta; / el bus se lleva a mi amiga / y el aire se queda en calma. "
      "Camino de vuelta a casa / sin prisa y sin compañía, / pero llevo en el bolsillo / su sonrisa de ese día. "
      "Opinión de Ana (inventada): «Me pareció un poema triste, pero tranquilo, ya que habla de una despedida sin dramas.» "
      "Opinión de Beto (inventada): «Me aburrió, por eso no lo recomiendo.»")

F3 = ("Cuento (inventado), «La bicicleta prestada»: Elena le prestó su bicicleta a un vecino para que fuera al consultorio. El vecino prometió devolverla al día siguiente. "
      "Pasaron tres días y no apareció. Elena se preocupó. Al cuarto día llegó con la bicicleta limpia y con una bolsa de duraznos. «Perdón por la demora», dijo.")

F4 = ("Borrador de una lectora (inventado, sin tildes): «Prefiero el cuento porque la protagonista decidio esperar. Despues llego el bus y ella subio con calma. Tambien me gusto el final.»")

F5 = ("Cuento (inventado), «El buzón de la esquina»: En la esquina del pasaje había un buzón viejo que nadie usaba. Una tarde, Inés dejó dentro una carta para un vecino que se había mudado. "
      "Una semana después, recibió la respuesta. Desde entonces, varios vecinos volvieron a escribirse cartas y el buzón se llenó de saludos.")

F6 = ("Borrador de recomendación (inventado, con errores): «Prefiero el cuento «El buzón de la esquina» por que es muy lindo. Inés dejo una carta ay y despues llego la respuesta. Tambien me gusto porque los vecinos se saludan.»")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy distingo entre decir «me gustó» y justificar una preferencia con una razón y un dato del texto.",
    prior=["Sé qué cuentos o poemas me gustan.", "Reconozco personajes y hechos de un cuento.", "Explico una decisión en pocas palabras."],
    explain=[
        "Preferir es elegir algo porque te gusta más. Todas las personas tienen preferencias, y todas son válidas. Lo que hacemos en esta clase es aprender a justificarlas, es decir, a explicar por qué las tienes.",
        "Una justificación tiene tres partes: lo que prefieres, la razón y un dato del texto que la apoya. Por ejemplo: «Prefiero este cuento porque muestra la confianza entre vecinos: doña Berta riega las plantas de quien viajó».",
        "Decir «me gustó porque sí» o «es lindo» no justifica, porque no dice qué del texto te gustó. Para justificar, pregúntate: ¿qué hay en el texto que me hizo pensar eso? La palabra «porque» te ayuda a unir la razón con lo que prefieres.",
    ],
    vocab=[("preferencia", "elección de algo porque te gusta más"), ("justificar", "dar razones de lo que piensas o eliges"), ("razón", "motivo por el que piensas algo"), ("dato", "información concreta que está en el texto")],
    worked=[
        ("Armar una justificación", "Cuento (inventado): «Ruth dejó su radio encendida junto a la ventana para que su vecino enfermo escuchara música. Él, agradecido, le dejó flores en la puerta».", ["Preferencia: me gusta el cuento.", "Razón: muestra cuidado entre vecinos.", "Dato: Ruth deja la radio encendida para que su vecino escuche música."], "Prefiero el cuento porque muestra cuidado entre vecinos: Ruth deja la radio encendida para su vecino enfermo"),
        ("Una frase que no justifica", "«Me gustó porque sí».", ["No dice qué del cuento me gustó.", "No tiene un dato del texto."], "No justifica: falta razón y dato"),
    ],
    mistakes=[("Responder «me gustó, es lindo» y detenerse.", "Es una opinión sin razón ni dato del texto.", "Agrega «porque» y un dato que esté en el texto."),
              ("Dar como razón algo ajeno al texto, como «porque soy del sur».", "La razón debe poder comprobarse en el texto.", "Busca en el texto la frase que apoya tu razón.")],
    T=[
        ("abc", "{F} ¿Qué le lleva la vecina a don Raúl un domingo?", "Un pan amasado", "Una carta", "Una planta", "El cuento dice que le llevó un pan amasado."),
        ("ab", "{F} ¿Por qué don Raúl tampoco habló al llegar?", "Porque no conocía a nadie", "Porque estaba enojado", "El texto explica que no conocía a nadie."),
        ("{F} ¿En qué día de la semana la vecina le lleva el pan? Escribe el día.", "domingo", "El cuento dice que la vecina llegó «un domingo», así que el día es domingo."),
        ("abc", "En Lenguaje: ¿qué significa justificar una preferencia?", "Dar razones, con datos del texto, de por qué la tienes", "Decir que algo es lindo", "Copiar todo el texto", "Justificar es explicar con razones y datos."),
        ("ab", "Escribes: «Me gustó el cuento.» ¿Qué le falta para ser una justificación?", "Una razón con un dato del texto", "Más adjetivos", "Sin razón ni dato solo es una opinión."),
        ("ab", "En «Prefiero este cuento porque muestra un gesto amable», ¿qué palabra introduce la razón?", "porque", "prefiero", "La palabra «porque» une la preferencia con su razón."),
        ("abc", "{F} Quieres justificar que el final es esperanzador. ¿Qué dato citas?", "Desde entonces el pasaje fue más amable", "Don Raúl llegó al pasaje", "Nadie lo saludó", "Solo el final muestra que la situación mejora."),
        ("abc", "Completa la justificación: «Prefiero el cuento ___ muestra cómo un saludo cambia un barrio.»", "porque", "sino", "mientras", "Para dar una razón se necesita «porque»."),
        ("abc", "{F} Quieres justificar que el cuento trata de una situación cotidiana. ¿Qué razón es adecuada?", "Que cuenta cómo llega un vecino nuevo a un pasaje, algo que puede ocurrir en un barrio", "Que es un cuento", "Que tiene un título", "La razón debe apoyarse en lo que cuenta el texto."),
        ("ab", "Pablo dice: «No me gustó porque no me gustan los cuentos.» Rosa dice: «No me gustó porque el final llega muy rápido y no cuenta cómo fue la once.» ¿Quién justifica con el texto?", "Rosa", "Pablo", "Rosa señala algo que está en el texto; Pablo no."),
        ("abc", "Una persona prefiere el cuento y otra prefiere un poema, y las dos dan razones apoyadas en sus textos. ¿Qué se concluye?", "Que las preferencias pueden ser distintas si cada una se justifica", "Que una de las dos está equivocada", "Que hay que votar", "Una preferencia es válida si se explica con razones."),
        ("abc", "{F} ¿Cuál justificación usa una razón y un dato?", "Prefiero el cuento porque el pan amasado muestra que una acción pequeña cambia el ambiente", "Prefiero el cuento porque lo leí primero", "Prefiero el cuento porque es corto y ya", "Solo la primera relaciona un dato del texto con una razón."),
        ("ab", "{F} Una lectora dice que la vecina es generosa. ¿Qué dato lo apoya?", "Que le lleva un pan amasado a don Raúl", "Que ocurre un domingo", "Ser generosa se muestra con una acción hacia otra persona."),
    ],
    ctx=("abc", "En un taller te piden elegir entre dos textos y explicar tu elección sin decir «es mejor». ¿Cómo lo haces?", "Digo cuál prefiero y doy una razón apoyada en algo que dice el texto", "Digo que el otro no sirve", "Elijo el más corto sin explicar", "Una preferencia se justifica con razones del texto."),
    sc=[("En Lenguaje: ¿qué es justificar?", "Dar razones y datos de por qué prefiero algo", "Va más allá de decir «me gustó»."),
        ("¿Qué palabra me ayuda a dar una razón?", "porque", "Une la preferencia con su motivo."),
        ("¿Qué partes tiene una buena justificación?", "Lo que prefiero, la razón y un dato del texto", "Son tres partes que se apoyan.")],
    op=("Lee el cuento: {F} Escribe en tu cuaderno si prefieres este cuento o prefieres no recomendarlo, y justifica con una razón y un dato del texto. Usa la palabra «porque».",
        "Prefiero este cuento porque muestra que un saludo o un gesto pequeño cambia cómo se vive en un barrio: la vecina le lleva un pan amasado a don Raúl y el pasaje se vuelve más amable.",
        ["dice su preferencia", "da una razón", "incluye un dato del texto", "usa «porque»"],
        ["una o dos oraciones escritas"],
        ["escribir solo «me gustó»", "dar una razón que no está en el texto"],
        "Pregunta: «¿Qué parte del texto te hizo pensar eso?»."),
    reinforce="Piensa en un texto o relato que te gustó y di una razón y un dato que lo apoye.",
    extend="Escribe dos justificaciones distintas para el mismo cuento, con datos distintos.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy conozco palabras que ayudan a justificar: conectores, sinónimos y antónimos, y una regla de coma.",
    prior=["Sé dar una razón con «porque».", "Reconozco un poema.", "Entiendo qué es una opinión."],
    explain=[
        "Para justificar con claridad usamos conectores, palabras que unen ideas. «Porque» y «ya que» dan una razón. «Por eso» muestra una consecuencia. «Pero» muestra un contraste. Antes de «pero» se escribe una coma.",
        "También ayuda tener variedad de palabras. Un sinónimo es una palabra con significado parecido: «rápido» y «veloz». Un antónimo significa lo contrario: «grande» y «pequeño». Así puedes decir lo mismo de otra manera y evitar repetir.",
        "Una buena opinión mezcla estas ayudas: «Me pareció triste, pero tranquilo, ya que habla de una despedida sin dramas». Ahí hay un contraste, una razón y palabras precisas.",
    ],
    vocab=[("conector", "palabra que une ideas, como porque, pero o por eso"), ("sinónimo", "palabra de significado parecido a otra"), ("antónimo", "palabra de significado contrario a otra"), ("consecuencia", "lo que resulta de algo que pasó antes")],
    worked=[
        ("Reconocer los conectores", F2, ["En la opinión de Ana: «pero» marca un contraste.", "«Ya que» introduce la razón."], "«Pero» contrasta y «ya que» da la razón"),
        ("Sinónimo y antónimo", "Palabra: «cansado».", ["Un sinónimo es una palabra parecida, como «agotado».", "Un antónimo es la contraria: «descansado»."], "Sinónimo: agotado; antónimo: descansado"),
    ],
    mistakes=[("Usar «por eso» para dar una razón.", "«Por eso» muestra una consecuencia, no la razón.", "Para dar una razón usa «porque» o «ya que»."),
              ("Olvidar la coma antes de «pero».", "La coma separa las dos ideas contrastadas.", "Escribe «Me gustó, pero el final fue triste».")],
    T=[
        ("abc", "{F} ¿Qué se lleva el bus en el poema?", "A la amiga de quien habla", "El aire de la calle", "La mano de la tarde", "El poema dice «el bus se lleva a mi amiga»."),
        ("ab", "{F} ¿Qué conector usa Ana para dar una razón?", "ya que", "pero", "«Ya que» introduce el motivo por el cual el poema le pareció tranquilo."),
        ("abc", "En Lenguaje: ¿qué es un sinónimo?", "Una palabra con significado parecido a otra", "Una palabra con significado contrario", "Una palabra que rima", "Los sinónimos significan casi lo mismo."),
        ("abc", "¿Cuál es un sinónimo de «tranquilo»?", "sereno", "inquieto", "ruidoso", "Sereno y tranquilo significan algo parecido."),
        ("abc", "¿Cuál es un antónimo de «triste»?", "alegre", "serio", "apenado", "Alegre expresa lo contrario de triste."),
        ("ab", "{F} En la opinión de Ana, ¿qué expresa «pero» en «triste, pero tranquilo»?", "Un contraste entre dos ideas", "Una consecuencia", "Une dos ideas que se oponen en parte."),
        ("abc", "Completa: «No me gustó el final, ___ leí el poema hasta el último verso.»", "pero", "porque", "por eso", "Se contrasta lo que no gustó con lo que se hizo."),
        ("abc", "Completa: «Me emocionó el poema, ___ lo leí dos veces.»", "por eso", "pero", "aunque no", "La emoción es la causa y leerlo dos veces es la consecuencia."),
        ("abc", "¿Cuál oración está bien puntuada?", "Me gustó, pero el final fue triste.", "Me gustó pero, el final fue triste.", "Me gustó pero el final, fue triste.", "La coma va antes de «pero»."),
        ("ab", "Marta dice que «alegre» y «contento» son antónimos. ¿Tiene razón?", "No: son sinónimos porque significan algo parecido", "Sí: los dos son estados de ánimo", "«Alegre» y «contento» se parecen; antónimos serían «alegre» y «triste»."),
        ("abc", "{F} ¿Cuál opinión justifica mejor?", "Me gustó porque describe una despedida sin dramas: quien habla camina con calma", "Me gustó, es lindo", "Me gustó, y ya", "La primera da una razón y un dato del poema."),
        ("abc", "¿Qué palabra es un sinónimo de «triste» en «un poema triste»?", "apenado", "alegre", "enojado", "«Apenado» expresa una tristeza parecida a la de «triste»."),
        ("abc", "{F} Beto dice: «Me aburrió, por eso no lo recomiendo.» ¿Qué relación expresa «por eso»?", "Una consecuencia: no lo recomienda porque se aburrió", "Un contraste", "Una pregunta", "«Por eso» une la causa con su resultado."),
    ],
    ctx=("abc", "Quieres escribir en una tarjeta que un poema te pareció breve, pero profundo. ¿Cuál frase está bien escrita?", "Me pareció breve, pero profundo.", "Me pareció breve pero, profundo.", "Me pareció, breve pero profundo.", "La coma se escribe antes de «pero»."),
    sc=[("En Lenguaje: ¿qué es un antónimo?", "Una palabra de significado contrario a otra", "Los antónimos son opuestos, como triste y alegre, o grande y pequeño."),
        ("¿Qué conectores dan una razón?", "Porque y ya que", "«Porque» y «ya que» introducen el motivo de lo que se afirma."),
        ("¿Dónde va la coma con «pero»?", "Antes de «pero»", "La coma separa las dos ideas que se contrastan con «pero».")],
    op=("Escribe en tu cuaderno tres oraciones sobre el poema «Despedida»: una con «porque», una con «pero» y otra con «por eso». Usa un sinónimo o un antónimo en alguna. Poema: {F}",
        "Me gustó porque describe una despedida con calma. Es breve, pero deja una imagen clara. Me emocionó, por eso lo leí dos veces.",
        ["tres oraciones", "usa los tres conectores", "con coma antes de «pero»", "usa un sinónimo o antónimo"],
        ["tres oraciones escritas"],
        ["usar «por eso» como razón", "olvidar la coma antes de «pero»"],
        "Pregunta: «¿Qué relación expresa este conector?»."),
    reinforce="Escribe un sinónimo y un antónimo de «silencio».",
    extend="Escribe cuatro oraciones sobre un texto que conozcas, cada una con un conector distinto.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy escribo una justificación completa paso a paso: afirmo, doy una razón, cito un dato y cierro.",
    prior=["Sé dar una razón con «porque».", "Conozco los conectores.", "Puedo copiar una frase del texto."],
    explain=[
        "Una justificación sólida sigue cuatro pasos. Paso 1: afirma lo que prefieres. Paso 2: da la razón con «porque». Paso 3: cita un dato del texto, tal como está escrito, entre comillas. Paso 4: cierra con una frase corta.",
        "Para citar se escriben dos puntos antes de la cita y comillas angulares: El vecino dijo: «Perdón por la demora». La cita copia las palabras del texto sin cambiarlas. Si las cambias, ya no es una cita, sino tu explicación.",
        "Cuando cites, procura que el dato apoye tu razón de verdad. Si dices que un personaje es honesto, la cita debe mostrar un hecho honesto. Una cita que no tiene relación con la razón no justifica nada.",
    ],
    vocab=[("citar", "copiar una frase del texto tal como está escrita"), ("comillas", "signos «  » que enmarcan una cita"), ("dos puntos", "signo que anuncia una cita o una lista"), ("evidencia", "dato del texto que apoya una razón")],
    worked=[
        ("Los cuatro pasos", "Cuento (inventado): «Tomás, taxista, encontró un celular en el asiento de atrás. Lo llevó a la oficina de objetos perdidos y avisó al dueño».", ["Afirmo: prefiero este cuento.", "Razón: porque muestra honestidad.", "Cita: «Lo llevó a la oficina de objetos perdidos».", "Cierro: devolver lo ajeno genera confianza."], "Prefiero este cuento porque muestra honestidad: «Lo llevó a la oficina de objetos perdidos». Devolver lo ajeno genera confianza"),
        ("Una cita mal elegida", "Razón: «el vecino es responsable». Cita: «Elena se preocupó».", ["La cita habla de Elena, no del vecino.", "No apoya la razón."], "La cita no justifica la razón"),
    ],
    mistakes=[("Citar y cambiar las palabras del texto sin avisar.", "Una cita debe ser exacta.", "Copia las palabras tal como están o explica con las tuyas sin comillas."),
              ("Olvidar cerrar las comillas.", "No se sabe dónde termina la cita.", "Abre con « y cierra con »." )],
    T=[
        ("abc", "{F} ¿En qué día llegó el vecino con la bicicleta?", "Al cuarto día", "Al día siguiente", "Al segundo día", "El texto dice «al cuarto día»."),
        ("ab", "{F} ¿Qué llevó el vecino junto con la bicicleta?", "Una bolsa de duraznos", "Una carta", "El texto dice que llegó con una bolsa de duraznos."),
        ("{F} ¿Cuántos días pasaron sin que el vecino apareciera? Escribe el número.", "3", "El texto dice «pasaron tres días»."),
        ("abc", "¿Qué se hace después de dar la razón en una justificación?", "Citar un dato del texto entre comillas", "Cambiar de tema", "Copiar el título", "Después de la razón va el dato que la apoya."),
        ("ab", "{F} ¿Qué cita apoya decir que el vecino reconoció su error?", "«Perdón por la demora»", "«Elena se preocupó»", "La frase del vecino admite la demora."),
        ("abc", "¿Cómo se escribe correctamente una cita?", "El vecino dijo: «Perdón por la demora».", "El vecino dijo «Perdón por la demora.", "El vecino dijo Perdón por la demora».", "La cita se anuncia con dos puntos y se cierra con comillas."),
        ("abc", "{F} Completa: «Prefiero este cuento ___ muestra honestidad: «Perdón por la demora».»", "porque", "aunque", "pero", "«Porque» une la preferencia con la razón."),
        ("abc", "{F} ¿Qué cita apoya decir que Elena es solidaria?", "«Elena le prestó su bicicleta a un vecino»", "«Elena se preocupó»", "«Al cuarto día llegó»", "Prestar algo que otro necesita muestra solidaridad."),
        ("abc", "Ordena la justificación: 1. cito, 2. afirmo, 3. doy la razón. ¿Cuál es el orden correcto?", "Afirmo, doy la razón, cito", "Cito, afirmo, doy la razón", "Doy la razón, cito, afirmo", "Primero se afirma, luego se explica y después se cita."),
        ("ab", "Teo escribe: «Es el mejor cuento porque es el mejor.» ¿Qué defecto tiene?", "La razón repite la afirmación y no usa un dato del texto", "Usa demasiadas comillas", "La razón no aporta nada nuevo ni cita el texto."),
        ("abc", "{F} ¿Qué justificación es más completa?", "Prefiero el cuento porque el vecino reconoce su error: «Perdón por la demora».", "Prefiero el cuento: «Perdón por la demora».", "Prefiero el cuento porque me gustó.", "La primera tiene afirmación, razón y cita."),
        ("abc", "{F} Otra lectora prefiere el final con reconciliación. ¿Qué dato cita?", "«llegó con la bicicleta limpia y con una bolsa de duraznos»", "«Pasaron tres días»", "«Elena se preocupó»", "Ese dato muestra el gesto que cierra el conflicto."),
        ("ab", "{F} Si el vecino nunca hubiera devuelto la bicicleta, ¿qué parte de la justificación sobre honestidad tendría que cambiar?", "La razón y la cita, porque ya no mostrarían honestidad", "Nada, porque el título sigue igual", "Sin la devolución no hay un dato que muestre honestidad."),
    ],
    ctx=("abc", "El centro de lectura te pide escribir en una tarjeta por qué recomiendas un cuento. ¿Qué escribes?", "Qué recomiendo, por qué y una frase del cuento entre comillas", "Solo el título", "Solo «me gustó»", "Una tarjeta útil explica la recomendación con una cita."),
    sc=[("¿Cuántos pasos tiene la justificación de hoy?", "Cuatro", "Afirmar, dar razón, citar y cerrar."),
        ("En Lenguaje: ¿qué signos enmarcan una cita?", "Las comillas « »", "Las comillas marcan dónde empieza y dónde termina la cita."),
        ("¿Qué debe cumplir la cita?", "Apoyar la razón y estar escrita igual que el texto", "La cita copia el texto sin cambios y debe mostrar lo que dice la razón.")],
    op=("Lee el cuento: {F} Escribe en tu cuaderno una justificación de cuatro pasos: tu preferencia, una razón con «porque», una cita entre comillas y una frase de cierre.",
        "Prefiero este cuento porque muestra solidaridad y honestidad: «Perdón por la demora». Un préstamo bien cuidado fortalece la confianza.",
        ["afirmación", "razón con «porque»", "cita exacta entre comillas", "cierre"],
        ["un párrafo de tres o cuatro oraciones"],
        ["cita que no apoya la razón", "no cerrar las comillas"],
        "Pregunta: «¿La cita muestra lo que dices?»."),
    reinforce="Copia una frase del cuento y escríbela como cita con dos puntos y comillas.",
    extend="Escribe una segunda justificación del mismo cuento con una razón y una cita distintas.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo dos herramientas para escribir bien lo que justifico: las tildes y los tiempos de los verbos.",
    prior=["Sé dividir una palabra en sílabas.", "Distingo presente y pasado.", "Escribo oraciones con porque."],
    explain=[
        "Las tildes dependen de dónde cae la fuerza al pronunciar. Las palabras agudas tienen la fuerza en la última sílaba y llevan tilde si terminan en n, s o vocal: «canción», «también», «después», «decidió». Las graves tienen la fuerza en la penúltima y llevan tilde si no terminan en n, s ni vocal: «árbol», «azúcar». Las esdrújulas siempre llevan tilde: «música».",
        "Los verbos cambian según el tiempo. En presente decimos «ella escribe una carta». En pretérito, para algo ya ocurrido, decimos «ella escribió una carta». En futuro, para algo que va a ocurrir, decimos «ella escribirá una carta». Fíjate que «escribió» lleva tilde porque es aguda y termina en vocal.",
        "Al justificar una preferencia sobre un cuento, mantén los verbos en el mismo tiempo. Si cuentas lo que pasó, usa el pretérito: «llegó», «subió», «gustó». Revisa tildes y tiempos al final, como lo hace cualquier persona que escribe.",
    ],
    vocab=[("palabra aguda", "tiene la fuerza en la última sílaba"), ("palabra grave", "tiene la fuerza en la penúltima sílaba"), ("palabra esdrújula", "tiene la fuerza en la antepenúltima y siempre lleva tilde"), ("pretérito", "tiempo del verbo para algo que ya ocurrió")],
    worked=[
        ("Poner tilde a un verbo", "Palabra sin tilde: «escribio».", ["«escribio» se dice es-cri-BIÓ: la fuerza está en la última sílaba.", "Termina en vocal, así que lleva tilde."], "escribió"),
        ("Presente y pretérito", "Verbo «salir», tercera persona: «sale» y «salió».", ["«Sale» es presente: pasa ahora.", "«Salió» es pretérito: ya pasó."], "Salió es el pretérito"),
    ],
    mistakes=[("Escribir «decidio» o «subio» sin tilde.", "Son agudas terminadas en vocal.", "Pronuncia la palabra: si la fuerza cae al final y termina en vocal, lleva tilde."),
              ("Poner tilde a palabras graves terminadas en vocal, como «cuento».", "Las graves terminadas en n, s o vocal no llevan tilde.", "Aplica la regla de las graves.")],
    T=[
        ("abc", "{F} ¿Cuál es la forma correcta de «decidio»?", "decidió", "décidio", "decidíó", "Es aguda y termina en vocal: lleva tilde en la última sílaba."),
        ("ab", "{F} ¿Cuál es la forma correcta de «Despues»?", "Después", "Despúes", "Es aguda terminada en s: lleva tilde en la última sílaba."),
        ("{F} ¿Cuántas palabras del borrador necesitan tilde? Escribe el número.", "6", "Necesitan tilde decidió, después, llegó, subió, también y gustó."),
        ("abc", "En Lenguaje: ¿qué regla tienen las palabras agudas?", "Llevan tilde si terminan en n, s o vocal", "Nunca llevan tilde", "Llevan tilde si terminan en consonante", "Esa es la regla de las agudas."),
        ("abc", "{F} ¿Por qué lleva tilde «también»?", "Es aguda y termina en n", "Es grave y termina en vocal", "Es esdrújula", "La fuerza cae en «bién» y termina en n."),
        ("ab", "¿Cuál es el verbo en pretérito: «decide» o «decidió»?", "decidió", "decide", "«Decidió» indica que la acción ya ocurrió."),
        ("abc", "Conjuga «llegar» en pretérito, tercera persona singular: «Ella ___ temprano.»", "llegó", "llega", "llegará", "El pretérito expresa algo ya ocurrido."),
        ("abc", "Conjuga «preferir» en presente, primera persona: «Yo ___ el cuento.»", "prefiero", "prefirió", "preferiré", "Con «yo» y en presente, el verbo preferir se escribe «prefiero»; las otras formas son otros tiempos."),
        ("abc", "¿Qué palabra está bien escrita?", "lápiz", "lapiz", "lápis", "Es grave y termina en z: lleva tilde."),
        ("ab", "Ana escribe «ella decide esperar» y «ella decidió esperar». ¿Cuál indica algo que ya ocurrió?", "ella decidió esperar", "ella decide esperar", "El pretérito marca una decisión pasada."),
        ("abc", "Si todo el relato está en pasado, ¿qué forma debe tener «sube» en «Ella ___ con calma»?", "subió", "sube", "subirá", "Debe estar en el mismo tiempo que el resto del relato."),
        ("abc", "¿Cuál oración está completamente bien escrita?", "Después, ella decidió volver.", "Despues, ella decidió volver.", "Después, ella decidio volver.", "Las dos palabras agudas llevan tilde."),
        ("abc", "{F} Corrige la última oración del borrador. ¿Cuál es la forma correcta?", "También me gustó el final.", "Tambien me gustó el final.", "También me gusto el final.", "En la última oración, «también» y «gustó» llevan tilde por ser agudas terminadas en n o vocal."),
    ],
    ctx=("abc", "Vas a escribir una tarjeta recomendando un cuento y no estás seguro de una tilde. ¿Qué haces?", "Pronuncio la palabra, veo dónde cae la fuerza y aplico la regla", "Pongo tilde en todas las palabras", "No pongo ninguna", "La regla de la sílaba tónica resuelve la duda."),
    sc=[("En Lenguaje: ¿qué es una palabra aguda?", "La que tiene la fuerza en la última sílaba", "Lleva tilde si termina en n, s o vocal."),
        ("¿Qué tiempo uso para algo que ya ocurrió?", "El pretérito", "El pretérito es el tiempo del verbo que expresa acciones ya pasadas."),
        ("¿Qué palabras siempre llevan tilde?", "Las esdrújulas", "Su fuerza cae antes de la penúltima sílaba.")],
    op=("Corrige este borrador y reescríbelo con tildes y verbos en pretérito: {F} Después escribe una oración nueva con el verbo «volver» en pretérito.",
        "Prefiero el cuento porque la protagonista decidió esperar. Después llegó el bus y ella subió con calma. También me gustó el final. Nueva oración: Ella volvió a casa.",
        ["corrige todas las tildes", "los verbos están en el mismo tiempo", "escribe una oración nueva con «volvió»"],
        ["un párrafo corregido y una oración"],
        ["poner tilde en «prefiero»", "mezclar presente y pasado"],
        "Pregunta: «¿Dónde cae la fuerza de la palabra?»."),
    reinforce="Escribe tres palabras agudas que lleven tilde.",
    extend="Escribe cinco verbos en pretérito de un cuento que conozcas.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a una tarea real: escribir una recomendación breve para un centro de lectura, con buena ortografía literal.",
    prior=["Sé justificar con razón y dato.", "Conozco conectores y tildes.", "Reviso mis escritos."],
    explain=[
        "Un centro de lectura o una biblioteca de barrio puede pedirte una recomendación breve para otros lectores. Una buena recomendación dice qué cuento recomiendas, por qué y qué dato lo apoya.",
        "La ortografía literal se refiere a las letras con que se escriben las palabras. Hay pares que se confunden: «hay» (del verbo haber) y «ahí» (lugar) y «¡ay!» (queja). También «porque» (razón) y «por qué» (pregunta o duda), y «hecho» (de hacer) y «echo» (de echar). Los verbos terminados en -bir se escriben con b («escribir»), salvo «hervir», «servir» y «vivir».",
        "Para escribir sin errores, relee con calma y revisa las palabras que dudas. Cuando tengas dudas con v, b, h, s, c, z, pide ayuda a un diccionario o a otra persona; es lo que hacen quienes escriben.",
    ],
    vocab=[("recomendación", "texto breve que sugiere leer algo y explica por qué"), ("ortografía literal", "uso correcto de las letras en las palabras"), ("hay / ahí / ay", "hay: haber; ahí: en ese lugar; ¡ay!: queja"), ("por qué / porque", "por qué: pregunta o duda; porque: razón")],
    worked=[
        ("Elegir ahí o hay", "Frases: «___ pocas personas en la fila» y «Te espero ___».", ["La primera dice que existen pocas personas: es el verbo haber, «hay».", "La segunda señala un lugar: «ahí»."], "Hay (haber) y ahí (lugar)"),
        ("Por qué y porque", "Frases: «No sé ___ cerraron la oficina» y «Cerraron la oficina ___ era feriado».", ["La primera es una duda: va separado y con tilde, «por qué».", "La segunda es una razón: se escribe junto y sin tilde, «porque»."], "por qué (duda) y porque (razón)"),
    ],
    mistakes=[("Escribir «por que» para dar una razón.", "La razón se escribe «porque», junto y sin tilde.", "Usa «porque» al responder o explicar."),
              ("Confundir «hay» con «ahí».", "«Hay» indica existencia y «ahí» un lugar.", "Pregunta: ¿hablo de un lugar o de que algo existe?")],
    T=[
        ("abc", "{F} ¿Qué objeto había en la esquina del pasaje?", "Un buzón viejo", "Una banca", "Un farol", "El texto dice que había un buzón viejo."),
        ("ab", "{F} ¿Para quién dejó Inés la carta?", "Para un vecino que se había mudado", "Para un vecino nuevo del pasaje", "La carta era para alguien que ya vivía en otro lugar."),
        ("{F} ¿Cuántas semanas pasaron hasta la respuesta? Escribe el número.", "1", "El texto dice «una semana después»."),
        ("abc", "¿Cuál palabra se escribe correctamente?", "escribir", "escrivir", "eskribir", "Los verbos terminados en -bir se escriben con b, como escribir."),
        ("abc", "Completa: «___ un buzón en la esquina.»", "Hay", "Ahí", "Ay", "El verbo haber se escribe «hay»."),
        ("abc", "Completa: «Inés dejó la carta ___, en el buzón.»", "ahí", "hay", "ay", "«Ahí» señala el lugar donde Inés dejó la carta."),
        ("abc", "Completa: «Quiero saber ___ el buzón se llenó de saludos.»", "por qué", "porque", "porqué", "Es una duda: se escribe separado y con tilde."),
        ("abc", "Completa: «Recomiendo el cuento ___ muestra la importancia de saludar.»", "porque", "por qué", "porqué", "Es una razón: va junto y sin tilde."),
        ("abc", "Completa: «Inés ha ___ una buena acción.»", "hecho", "echo", "hécho", "«Hecho» viene del verbo hacer; «echo» viene de echar, que no cabe aquí."),
        ("ab", "¿Qué frase tiene la ortografía correcta?", "Desde entonces, varios vecinos volvieron a escribirse cartas.", "Desde entonces, varios vecinos bolvieron a escribirse cartas.", "El verbo volver se escribe con v."),
        ("abc", "Una lectora escribe: «Recomiendo este cuento por que enseña a saludar.» ¿Qué debe corregir?", "Escribir «porque», junto, porque da una razón", "Poner tilde en «cuento»", "Cambiar «enseña» por «ensena»", "Cuando se da una razón, la palabra se escribe «porque», junta y sin tilde."),
        ("abc", "{F} ¿Cuál es la recomendación mejor escrita?", "Recomiendo el cuento porque muestra cómo un buzón vuelve a unir a los vecinos: «el buzón se llenó de saludos».", "Recomiendo el cuento por que si.", "Recomiendo el cuento porque, porque me gustó.", "Tiene razón, cita y buena ortografía."),
        ("abc", "{F} ¿Qué dato apoya decir que el cuento muestra comunidad?", "Varios vecinos volvieron a escribirse cartas", "El buzón era viejo", "Inés dejó una carta", "Que varias personas retomen el contacto muestra comunidad."),
    ],
    ctx=("abc", "La biblioteca te pide dos líneas para recomendar un cuento. Terminas y revisas. ¿Qué corriges primero?", "Que la razón tenga un dato del texto y luego la ortografía", "Solo las comas", "Nada, porque ya terminé", "Primero el contenido y después la forma."),
    sc=[("¿Cuándo escribo «porque» junto?", "Cuando doy una razón", "Responde a una pregunta con «por qué»."),
        ("¿Cuándo escribo «ahí»?", "Cuando señalo un lugar", "«Ahí» señala el lugar donde ocurre algo."),
        ("En Lenguaje: ¿qué es la ortografía literal?", "Escribir bien las letras de las palabras", "Incluye b, v, h, s, c, z.")],
    op=("Escribe una recomendación de dos o tres oraciones del cuento «El buzón de la esquina»: {F} Incluye una razón con «porque», una cita entre comillas y al menos una de estas palabras bien escrita: hay, ahí, hecho.",
        "Recomiendo «El buzón de la esquina» porque muestra cómo un objeto olvidado vuelve a unir a un barrio: «el buzón se llenó de saludos». Ahí se ve que un gesto sencillo cambia las cosas.",
        ["recomienda con razón", "cita el texto", "usa bien una de las tres palabras"],
        ["dos o tres oraciones"],
        ["escribir «por que» para dar la razón", "no citar"],
        "Pregunta: «¿Qué dato apoya tu recomendación?»."),
    reinforce="Escribe tres oraciones con hay, ahí y ay.",
    extend="Escribe una segunda recomendación sobre otro texto que conozcas.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso una justificación completa con una lista de verificación y decido qué sigo practicando.",
    prior=["Sé justificar con razón y dato.", "Conozco tildes, conectores y verbos.", "Corrijo mis textos."],
    explain=[
        "Revisar un texto es leerlo de nuevo con una lista. Cinco preguntas ayudan: ¿digo lo que prefiero?, ¿doy una razón con «porque»?, ¿incluyo un dato del texto?, ¿uso bien los conectores y la puntuación?, ¿cuidé tildes y letras?",
        "Conviene revisar en ese orden: primero las ideas, luego los conectores y al final la ortografía. Así no pierdes tiempo corrigiendo una frase que después tendrás que cambiar.",
        "Revisar también es decidir qué sigues practicando. Anota qué mejoró en este módulo y qué necesitas repasar. Pedir apoyo para lo difícil es parte de aprender.",
    ],
    vocab=[("lista de verificación", "lista de preguntas para revisar un texto"), ("borrador", "primera versión de un texto"), ("revisar", "leer de nuevo para mejorar"), ("sinónimo", "palabra de significado parecido a otra")],
    worked=[
        ("Revisar una oración", "Oración: «Mi vecina llego temprano y se sento ay».", ["Verbos en pretérito sin tilde: llegó y sentó.", "«Ay» debe ser «ahí» porque indica un lugar."], "Mi vecina llegó temprano y se sentó ahí"),
        ("Revisar la razón", "Razón: «porque es entretenido».", ["No dice qué del texto es entretenido.", "Falta un dato."], "Falta un dato del texto"),
    ],
    mistakes=[("Corregir solo las tildes y creer que el texto ya está bien.", "También hay que revisar la razón, el dato y los conectores.", "Usa las cinco preguntas de la lista."),
              ("Revisar sin releer el texto original.", "Puedes citar mal un dato.", "Vuelve al cuento y comprueba la cita.")],
    T=[
        ("{F} ¿Cuántas palabras del borrador necesitan tilde? Escribe el número.", "5", "Necesitan tilde dejó, después, llegó, También y gustó."),
        ("abc", "{F} ¿Cuál es la forma correcta de «por que» en «por que es muy lindo»?", "porque", "porqué", "por qué", "Se da una razón: junto y sin tilde."),
        ("ab", "{F} ¿Cómo debe escribirse «ay» en «dejo una carta ay»?", "ahí", "hay", "La frase señala el lugar donde se dejó la carta, y eso se escribe «ahí»."),
        ("abc", "{F} ¿Qué parte del borrador es la razón?", "porque es muy lindo", "Inés dejó una carta", "los vecinos se saludan", "La palabra «porque» introduce la razón."),
        ("ab", "{F} ¿Qué le falta a esa razón para justificar bien?", "Un dato del texto", "Más adjetivos", "«Muy lindo» no dice qué del cuento le gustó."),
        ("ab", "{F} ¿Qué verbo del borrador necesita tilde y está en pretérito?", "dejo, que debe ser dejó", "saludan", "Es la acción ya ocurrida de dejar la carta."),
        ("abc", "{F} Completa con un dato: «Prefiero el cuento porque ___.»", "los vecinos vuelven a escribirse cartas", "es lindo", "yo quiero", "El dato debe estar en el texto."),
        ("abc", "Elige un sinónimo de «viejo» en «un buzón viejo».", "antiguo", "nuevo", "pequeño", "Antiguo significa algo parecido a viejo."),
        ("{F} La lista de revisión tiene cinco preguntas. ¿Cuántas se refieren a la ortografía o la puntuación? Escribe el número.", "2", "Una trata de conectores y puntuación y otra de tildes y letras."),
        ("ab", "Sofía dice que para revisar basta mirar las tildes. ¿Qué respuesta es correcta?", "También hay que revisar la razón, el dato y los conectores", "Tiene razón: todo lo demás es opcional", "Una justificación necesita razón, dato y buena escritura."),
        ("abc", "¿Qué orden de revisión conviene?", "Primero las ideas, luego los conectores y al final la ortografía", "Primero la ortografía, luego las ideas", "Solo los conectores", "Así no corriges frases que luego cambiarás."),
        ("abc", "{F} ¿Qué versión corrige bien la segunda oración?", "Inés dejó una carta ahí y después llegó la respuesta.", "Inés dejo una carta ahí y después llego la respuesta.", "Inés dejó una carta ay y después llegó la respuesta.", "Corrige los verbos con tilde, cambia «ay» por «ahí» y pone las tildes que faltaban."),
        ("abc", "{F} ¿Cuál es una versión mejorada de la primera oración?", "Prefiero el cuento «El buzón de la esquina» porque los vecinos vuelven a escribirse cartas.", "Prefiero el cuento por que es muy lindo.", "Prefiero el cuento porque sí.", "Tiene razón con dato y buena escritura."),
    ],
    ctx=("abc", "Terminas una recomendación para la biblioteca. ¿Qué haces antes de entregarla?", "La reviso con la lista: preferencia, razón, dato, conectores y ortografía", "La entrego sin leerla", "Cambio el título", "Revisar con una lista mejora el texto."),
    sc=[("¿Cuántas preguntas tiene la lista de verificación de hoy?", "Cinco", "Son preferencia, razón, dato, conectores y ortografía."),
        ("¿Qué reviso primero?", "Las ideas", "Después de las ideas se revisan los conectores y al final la ortografía."),
        ("En Lenguaje: ¿qué hago si dudo cómo se escribe una palabra en mi recomendación?", "Pregunto a otra persona o consulto un diccionario", "Resolver la duda con una fuente confiable evita dejar errores en el texto; adivinar no.")],
    op=("Corrige este borrador: {F} Reescríbelo completo, con una razón y un dato del cuento, y agrega una meta de práctica para esta semana.",
        "Prefiero el cuento «El buzón de la esquina» porque los vecinos vuelven a escribirse cartas. Inés dejó una carta ahí y después llegó la respuesta. También me gustó que el buzón se llenara de saludos. Meta: revisaré mis tildes en cada texto.",
        ["corrige tildes y letras", "razón con dato", "meta concreta"],
        ["el borrador reescrito y una meta"],
        ["corregir solo las tildes", "meta vaga"],
        "Pregunta: «¿Qué dato del texto apoya tu razón?»."),
    reinforce="Revisa una nota o mensaje que escribiste hoy con las cinco preguntas.",
    extend="Escribe tu propia lista de verificación de tres preguntas para revisar tus recomendaciones.",
)

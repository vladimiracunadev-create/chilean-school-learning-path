"""Cuaderno del estudiante, 1.º medio Inglés (oficial), IN1M OA 02: expresiones clave, collocations, conectores y sonidos.

Las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado. Los textos son originales y llevan pista en
español. Los sonidos se trabajan con palabras escritas, clasificadas por el sonido que se enseña en la clase.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA = "IN1M OA 02"
ADULT = "Un adulto lee en voz alta (tapa el guion): "
MAT_L = "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz."
MAT_R = "Las palabras y textos escritos en cada ejercicio, lápiz y una hoja para anotar."


def E(rows):
    return [r if isinstance(r, dict) else ex(*r) for r in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ------------------------------------------------------------------ clase 1: collocations y expresiones idiomáticas
W_TEST = "«Mia: Are you ready for the test? Leo: Not really. I need to hit the books tonight. Mia: Don't worry, it's a piece of cake for you!» (ready = listo, test = prueba, hit the books = estudiar mucho, piece of cake = algo muy fácil)"
W_WEATHER = "«I'm a bit under the weather today, so I'll take a break and make a cup of tea.» (under the weather = algo enfermo, take a break = tomar un descanso, make = preparar)"
PLAY = "«Before the school play, Ana says to Ben: Break a leg! Ben smiles and says: Thanks, I have learned my lines.» (school play = obra de teatro del colegio, break a leg = frase para desear buena suerte, lines = diálogos)"
RAIN = "«It was raining cats and dogs, so we stayed at home. We made popcorn, watched a film and had a good time.» (raining cats and dogs = llover muchísimo, stayed = nos quedamos, popcorn = cabritas, film = película)"
MOON = "«I go to the cinema once in a blue moon, because I prefer to watch films at home.» (cinema = cine, once in a blue moon = muy rara vez, prefer = prefiero)"
PARTY = "«Sofi: Are you coming to the party? Tom: I'm tired and I have a cold. I think I'll stay home. Sofi: Oh no! Take care.» (party = fiesta, cold = resfrío, stay = quedarme, take care = cuídate)"
TOWN = "«Host: What is it like in your town? Guest: It's quiet, and the people are friendly. Host: Why don't we visit it next summer? Guest: Great idea!» (what is it like = cómo es, quiet = tranquilo, friendly = amables, visit = visitar, great idea = buena idea)"
WIND = "«Good morning. Because of the strong wind, buses will leave late. Please keep your tickets and pay attention to the announcements.» (strong wind = viento fuerte, keep = conserva, announcements = avisos)"

lesson(
    OA, 1, MAT_L,
    "Aprenderé a reconocer combinaciones frecuentes de palabras (collocations), expresiones de uso común y expresiones idiomáticas cuando las escucho. Sirve para entender conversaciones sin traducir palabra por palabra.",
    ["Conozco verbos como make, do, take y have.", "Sé decir saludos y sugerencias simples en inglés."],
    [
        "Una combinación frecuente de palabras (collocation) es un grupo de palabras que suelen ir juntas. En inglés decimos make a decision, make a mistake y make a plan, pero do homework, do exercise y do a favour. También decimos take a photo, take a break y catch a cold, pay attention y have a good time. Si traduces del español, puedes equivocarte: no se dice do a mistake.",
        "Una expresión idiomática (idiom) es una frase cuyo significado no sale de traducir cada palabra. It's raining cats and dogs significa que llueve muchísimo. A piece of cake es algo muy fácil. Under the weather es sentirse un poco enfermo. Break a leg se dice para desear buena suerte antes de una presentación. Once in a blue moon es muy rara vez. Hit the books es estudiar mucho.",
        "También hay expresiones de uso común en conversaciones: What is it like? pide una descripción, Why don't we...? propone algo, y Nice to meet you se dice al conocer a alguien; la respuesta habitual es Nice to meet you too. Para entenderlas, escucha el grupo completo y piensa en la situación. Si dudas, usa el contexto: quién habla, dónde está y qué quiere lograr.",
    ],
    [("collocation", "combinación frecuente de palabras"), ("idiom", "expresión idiomática"), ("make / do", "hacer (cosas nuevas / tareas)"), ("take a break", "tomar un descanso"), ("a piece of cake", "algo muy fácil"), ("once in a blue moon", "muy rara vez")],
    [
        ("Reconocer un idiom por el contexto", ADULT + W_TEST + " ¿Qué quiere decir Mia con a piece of cake?", ["Leo está preocupado por la prueba.", "Mia lo tranquiliza: para él la prueba es fácil.", "A piece of cake no habla de comida: significa muy fácil."], "Que la prueba es muy fácil para él"),
        ("Reconocer collocations", ADULT + W_WEATHER + " ¿Qué collocations con take y make aparecen?", ["Busco los verbos take y make.", "Aparece take a break.", "Aparece make a cup of tea."], "Take a break y make a cup of tea"),
    ],
    [
        ("Traducir palabra por palabra una expresión idiomática.", "Se piensa que el significado sale de cada palabra, pero el grupo tiene otro sentido.", "Pregunta qué quiere decir la situación completa y no cada palabra."),
        ("Decir do a mistake en lugar de make a mistake.", "Se traduce hacer siempre con do, aunque la collocation pide make.", "Aprende el grupo completo: make a mistake, make a decision."),
    ],
    [
        ("Completa la combinación usada al hablar: ___ a decision. A) make B) do", "A) make", "Se dice make a decision."),
        ("En una conversación oyes: «Can I ___ a photo of you?» ¿Qué verbo falta? A) take B) do", "A) take", "La combinación habitual es take a photo."),
        ("Completa: ___ attention to the teacher. A) Pay B) Make", "A) Pay", "La combinación habitual es pay attention."),
    ],
    [
        (ADULT + PLAY + " ¿Qué le desea Ana a Ben con Break a leg? A) buena suerte B) que tenga cuidado de no caerse en el escenario", "A) buena suerte", "Break a leg es una expresión idiomática que desea suerte antes de actuar."),
        (ADULT + RAIN + " ¿Cómo estaba el tiempo? A) llovía muchísimo B) había animales en la calle", "A) llovía muchísimo", "Raining cats and dogs es una expresión idiomática para lluvia fuerte."),
        (ADULT + MOON + " ¿Con qué frecuencia va al cine? A) muy rara vez B) todas las noches de luna llena", "A) muy rara vez", "Once in a blue moon significa casi nunca."),
    ],
    [
        (ADULT + "«We made a plan for the weekend, did our homework and had a good time.» (plan = plan, weekend = fin de semana). Anota las tres collocations en el orden en que aparecen.", "made a plan, did our homework, had a good time", "Son tres combinaciones habituales: make a plan, do homework, have a good time."),
        ("Alguien te dice «Nice to meet you». ¿Qué respuesta habitual da otra persona? A) Nice to meet you too. B) You're welcome.", "A) Nice to meet you too.", "Se responde repitiendo el saludo con too."),
        ("Un amigo dice «Why don't we study together?». ¿Qué función cumple? A) hace una sugerencia B) pregunta por qué no estudian juntos", "A) hace una sugerencia", "Why don't we...? es una forma de proponer un plan."),
    ],
    [
        ("Tu compañero dice «I did a mistake». ¿Cuál es la forma natural en inglés? A) I made a mistake. B) I did a mistake.", "A) I made a mistake.", "La collocation de mistake es con make."),
        ("Alguien te dice «Break a leg tonight!» antes de tu presentación. ¿Cuál es la mejor respuesta? A) Thanks! B) Oh no, I'm sorry about my leg.", "A) Thanks!", "La frase no habla de una pierna: desea buena suerte."),
    ],
    [
        (ADULT + PARTY + " ¿Por qué Tom no va a la fiesta? A) porque está cansado y tiene resfrío B) porque no le gustan las fiestas", "A) porque está cansado y tiene resfrío", "Dice I'm tired and I have a cold."),
        (ADULT + TOWN + " ¿Qué expresión usa el anfitrión para proponer visitar el pueblo? A) Why don't we visit it...? B) What is it like?", "A) Why don't we visit it...?", "What is it like pide una descripción; la propuesta es la otra."),
    ],
    [(ADULT + WIND + " ¿Qué debes hacer? A) conservar el pasaje y estar atento a los avisos B) cambiar de bus de inmediato", "A) conservar el pasaje y estar atento a los avisos", "Dice keep your tickets y pay attention to the announcements.")],
    [
        ("En Inglés de 1.º medio (OA 2, clase 1): ¿qué es una collocation?", "Una combinación de palabras que suelen ir juntas, como make a decision", "No se traduce palabra por palabra."),
        ("En Inglés de 1.º medio (OA 2, clase 1): ¿qué es una expresión idiomática?", "Una frase cuyo significado no sale de las palabras sueltas", "Su sentido es el del grupo completo."),
        ("En Inglés de 1.º medio (OA 2, clase 1): ¿qué verbo se usa con homework, do o make?", "Do: do homework", "La collocation es do homework."),
    ],
    task("Un adulto lee dos veces este texto: «Last Saturday it was raining cats and dogs. We stayed at home, made a plan for the week and did our homework. Then we baked a cake: it was a piece of cake! We had a good time.» (baked = horneamos, week = semana). Anota tres collocations y una expresión idiomática con su significado en español.", "Collocations: made a plan, did our homework, had a good time. Expresión idiomática: raining cats and dogs = llover muchísimo (también vale a piece of cake = algo muy fácil).", ["anota tres collocations del texto", "elige una expresión idiomática correcta", "explica su significado sin traducir palabra por palabra"], ["hoja con las cuatro respuestas", "nota del adulto"], ["traducir cats and dogs como gatos y perros", "anotar una frase que no es una collocation"], "Reconoce los grupos bien ubicados y, si tradujo literal, vuelve a la situación: ¿qué hacían ellos por la lluvia?"),
    "Escribe cada collocation de esta clase en una tarjeta con un dibujo pequeño que recuerde su significado.",
    "Escribe en español tres expresiones que usas con tus amigos y piensa por qué no se traducirían palabra por palabra al inglés.",
)

# ------------------------------------------------------------------ clase 2: conectores later, last, so that, although, both
W_COLD = "«Although it was cold, we played outside. First we ran, later we played football, and last we drank hot chocolate.» (although = aunque, cold = frío, ran = corrimos, football = fútbol, drank = tomamos)"
W_CHOIR = "«Both Ana and Julia are in the choir. They practise on Mondays so that they can sing well at the concert.» (choir = coro, practise = practican, sing = cantar)"
MORN = "«I started my morning with a quick walk. Later I studied for an hour, and last I called my grandmother. Although I was tired, I felt happy.» (quick = corta, studied = estudié, called = llamé, grandmother = abuela, tired = cansado, felt = me sentí)"
LAPTOP = "«My brother saves money so that he can buy a laptop. Although the laptop is expensive, he is not worried. Both my parents and I help him with small jobs.» (saves = ahorra, laptop = computador portátil, expensive = caro, worried = preocupado, jobs = trabajitos)"
VOLS = "«Marta and Tomás are both volunteers. They collect food so that families can eat well. Last Saturday, they worked for six hours, although it rained all day.» (volunteers = voluntarios, collect = recolectan, food = comida, families = familias, rained = llovió, all day = todo el día)"
FILM = "«The film was long, although it was exciting. Later, we ate pizza. Both of us loved the ending.» (film = película, exciting = emocionante, ending = final)"
UMB = "«Hi Dani. Although the bus is slow, I will be there at six. Later we can have dinner together.» (slow = lento, dinner = cena, together = juntos)"

lesson(
    OA, 2, MAT_L,
    "Aprenderé a reconocer en textos orales los conectores later, last, so that, although y both, y lo que une cada uno. Sirve para seguir el hilo de una explicación o una historia.",
    ["Conozco and, but, because, so, first y then.", "Sé que los conectores unen ideas."],
    [
        "Un conector (connector) es una palabra que une ideas y te dice qué relación tienen. Later significa más tarde y last significa por último; ambos ordenan acciones: First we ran, later we played, and last we drank. Si oyes last al final de una lista de acciones, es la última. Si oyes later, hay otra acción después, pero no necesariamente es la final.",
        "So that introduce un propósito: para que. Se usa con un verbo después: She studies so that she can pass the test. Although introduce un contraste: aunque. La parte con although muestra una dificultad y la otra parte muestra lo que ocurre igual: Although it was cold, we played outside. No significa porque. Both significa ambos y se usa con and: Both Ana and Julia are in the choir.",
        "Cuando escuchas, no traduzcas el conector solo: úsalo para predecir. Si oyes although, espera algo inesperado después. Si oyes so that, espera un propósito. Si oyes both, espera dos personas o cosas. Los conectores del año anterior, como and, but, because, so, first y then, siguen siendo útiles.",
    ],
    [("later", "más tarde"), ("last", "por último"), ("so that", "para que (propósito)"), ("although", "aunque (contraste)"), ("both ... and", "ambos ... y"), ("connector", "palabra que une ideas")],
    [
        ("Ordenar con first, later y last", ADULT + W_COLD + " ¿Qué hicieron por último?", ["First ordena la primera acción: correr.", "Later es la segunda: fútbol.", "Last marca la última: tomaron chocolate caliente."], "Tomaron chocolate caliente"),
        ("Reconocer propósito y ambos", ADULT + W_CHOIR + " ¿Quiénes están en el coro y para qué practican los lunes?", ["Both Ana and Julia indica las dos personas.", "So that introduce el propósito.", "Practican para cantar bien en el concierto."], "Ana y Julia; practican para cantar bien en el concierto"),
    ],
    [
        ("Traducir although como porque.", "Se confunde un contraste con una causa.", "Although (aunque) muestra una dificultad; because muestra la causa."),
        ("Pensar que later significa por último.", "Later y last marcan orden, pero later no cierra la lista.", "Busca last para la acción final."),
    ],
    [
        ("En un texto oyes: «First I ate, later I studied.» ¿Qué significa later? A) más tarde B) por último", "A) más tarde", "Later es más tarde; la última acción se marca con last."),
        ("En un texto oyes: «Last, I called my aunt.» ¿Qué indica last? A) que fue la última acción B) que fue la primera acción", "A) que fue la última acción", "Last cierra la secuencia."),
        ("En «She saves money so that she can travel», ¿qué significa so that? A) para que (propósito) B) aunque (contraste)", "A) para que (propósito)", "Introduce el propósito de ahorrar."),
    ],
    [
        (ADULT + MORN + " ¿Qué hizo por último? A) llamó a su abuela B) salió a caminar", "A) llamó a su abuela", "Last I called my grandmother marca la última acción."),
        (ADULT + MORN + " ¿Cómo se sentía a pesar del cansancio? A) feliz B) tan cansado que no pudo disfrutar el día", "A) feliz", "Although I was tired, I felt happy: contraste entre cansancio y alegría."),
        (ADULT + LAPTOP + " ¿Para qué ahorra el hermano? A) para comprar un computador B) para ayudar a sus padres con los trabajitos", "A) para comprar un computador", "Saves money so that he can buy a laptop."),
    ],
    [
        (ADULT + VOLS + " ¿Para qué recogen comida? A) para que las familias coman bien B) para vender en la feria", "A) para que las familias coman bien", "So that families can eat well expresa el propósito."),
        (ADULT + FILM + " ¿Qué contraste hay en la película? A) era larga pero emocionante B) era emocionante y por eso larga", "A) era larga pero emocionante", "The film was long, although it was exciting."),
        (ADULT + VOLS + " ¿Quiénes son voluntarios? A) Marta y Tomás B) solo Marta", "A) Marta y Tomás", "Both significa ambos: Marta and Tomás are both volunteers."),
    ],
    [
        ("Elige el conector que falta: «___ it was raining, we played football.» A) Although B) So that", "A) Although", "Hay un contraste: llovía y jugaron igual."),
        ("Elige el conector que falta: «She studies hard ___ she can get a good grade.» A) so that B) although", "A) so that", "Expresa el propósito de estudiar."),
    ],
    [
        (ADULT + "«A friend says although means because. Another friend says although shows a contrast.» (friend = amigo, shows = muestra). Con tus conocimientos, ¿quién tiene razón? A) el segundo, porque although indica contraste B) el primero, porque although indica causa", "A) el segundo, porque although indica contraste", "Because es la causa; although es aunque."),
        (ADULT + VOLS + " ¿Qué pasó el sábado a pesar de la lluvia? A) trabajaron seis horas B) se suspendió el trabajo", "A) trabajaron seis horas", "Although it rained all day introduce una dificultad que no los detuvo."),
    ],
    [(ADULT + UMB + " ¿Qué podrán hacer más tarde? A) cenar juntos B) llegar a las seis", "A) cenar juntos", "Later we can have dinner together.")],
    [
        ("En Inglés de 1.º medio (OA 2, clase 2): ¿qué relación expresa although?", "Un contraste: aunque", "Une una dificultad con lo que ocurre igual."),
        ("En Inglés de 1.º medio (OA 2, clase 2): ¿qué relación expresa so that?", "Un propósito: para que", "Dice para qué se hace algo."),
        ("En Inglés de 1.º medio (OA 2, clase 2): ¿qué significa both Ana and Julia?", "Ambas, Ana y Julia", "Both reúne a las dos personas."),
    ],
    task("Un adulto lee dos veces este texto: «Both my sister and I want to go to the concert. Although tickets are expensive, we save money so that we can buy them. Later we will ask a family member to come with us, and last we will choose the seats.» (concert = concierto, tickets = entradas, expensive = caras, save = ahorramos, seats = asientos). Anota qué conector muestra un propósito, cuál un contraste, cuál agrupa a dos personas y cuál marca la última acción.", "Propósito: so that. Contraste: although. Agrupa a dos personas: both. Última acción: last (elegir los asientos).", ["identifica los cuatro conectores", "explica en español lo que une cada uno", "indica la última acción"], ["hoja con cuatro respuestas", "nota del adulto"], ["confundir although con because", "decir que later marca la última acción"], "Reconoce los conectores acertados y vuelve a escuchar solo la oración con so that para distinguir propósito de contraste."),
    "Relee los textos de la clase y marca con un color los conectores later y last.",
    "Escribe en español tres frases tuyas que usen aunque, para que y ambos, y piensa cómo las dirías con although, so that y both.",
)

# ------------------------------------------------------------------ clase 3: vocales largas y cortas
lesson(
    OA, 3, MAT_R,
    "Aprenderé a distinguir vocales largas y cortas en pares como feet y fit, y a elegir la palabra correcta al escuchar. Sirve para que no cambie el significado de lo que digo ni de lo que entiendo.",
    ["Sé leer palabras cortas en inglés.", "Conozco palabras como sit, ship y green."],
    [
        "En inglés, la duración de la vocal cambia el significado. La vocal larga se escribe /iː/ y suena más alargada y tensa, como en feet (pies), seat (asiento), sheep (oveja), leave (irse), heat (calor) y cheap (barato). La vocal corta se escribe /ɪ/ y es breve y relajada, como en fit (calzar), sit (sentarse), ship (barco), live (vivir), hit (golpear) y chip (papa frita o fichita). En español solo tenemos una i, por eso cuesta oír la diferencia.",
        "Ocurre algo parecido con /uː/ y /ʊ/. La vocal larga está en pool (piscina), fool (tonto), food (comida) y Luke; la vocal corta está en pull (tirar), full (lleno), foot (pie) y look (mirar). La escritura ayuda, pero no es una regla: ee y ea suelen dar la vocal larga, como en green y beach, y la i sola suele dar la corta, como en grin y fit.",
        "Para practicar, junta pares mínimos (minimal pairs): palabras que solo se diferencian por un sonido. Sheep y ship, seat y sit, pool y pull. Di el par en voz alta, alarga la primera y acorta la segunda, y pide a otra persona que adivine cuál dijiste. Si cambias el sonido, cambias el mensaje: I want to leave here no es lo mismo que I want to live here.",
    ],
    [("long vowel /iː/", "vocal larga: feet, seat"), ("short vowel /ɪ/", "vocal corta: fit, sit"), ("minimal pair", "par de palabras que solo cambian en un sonido"), ("sheep / ship", "oveja / barco"), ("leave / live", "irse / vivir"), ("pool / pull", "piscina / tirar")],
    [
        ("Clasificar una palabra por su vocal", "¿La palabra beach tiene vocal larga o corta, como feet o como fit?", ["Miro la escritura: ea suele dar la vocal larga.", "Beach suena como feet.", "Por eso tiene la vocal larga /iː/."], "Larga, como feet"),
        ("Elegir según el significado", "Una persona dice «The ship is in the port» y otra «The sheep is in the field». ¿Qué palabra significa barco?", ["Ship significa barco.", "Se oye la vocal corta /ɪ/.", "Sheep, con vocal larga, es oveja."], "Ship (vocal corta)"),
    ],
    [
        ("Decir feet y fit con la misma vocal.", "En español hay una sola i y se transfiere a las dos palabras.", "Alarga feet y acorta fit; practica con un par mínimo."),
        ("Pensar que ea siempre da vocal larga.", "La escritura ayuda, pero tiene excepciones como head, que tiene vocal corta.", "Apóyate en el sonido de la palabra, no solo en la escritura."),
    ],
    [
        ("¿Qué palabra tiene la vocal larga de feet? A) seat B) sit", "A) seat", "Seat se pronuncia con /iː/; sit con /ɪ/."),
        ("¿Qué palabra tiene la vocal corta de fit? A) ship B) sheep", "A) ship", "Ship tiene /ɪ/; sheep, /iː/."),
        ("¿Qué palabra tiene la vocal larga /uː/ de pool? A) food B) foot", "A) food", "Food tiene /uː/; foot tiene /ʊ/ corta."),
    ],
    [
        ("¿Qué palabra significa «asiento»? A) seat B) sit", "A) seat", "Seat, con vocal larga, es asiento; sit es el verbo sentarse."),
        ("Para decir «Prefiero sentarme aquí», ¿qué palabra va? «I prefer to ___ here.» A) sit B) seat", "A) sit", "Sit es el verbo sentarse, con vocal corta; seat es asiento."),
        ("¿En qué par las dos palabras tienen la misma vocal larga? A) seat – meet B) seat – sit", "A) seat – meet", "Ambas tienen /iː/; en seat – sit las vocales son distintas."),
    ],
    [
        ("Clasifica las palabras cheap, chip, heat, hit, pool y pull. Escribe las tres que tienen vocal larga.", "cheap, heat, pool", "Cheap y heat tienen /iː/; pool tiene /uː/; las otras tienen vocal corta."),
        ("¿Qué frase dice «vivir»? A) I live in a small town. B) I leave in a small town.", "A) I live in a small town.", "Live significa vivir y tiene la vocal corta."),
        ("¿Qué palabra significa «piscina»? A) pool B) pull", "A) pool", "Pool, con vocal larga, es piscina; pull es tirar."),
    ],
    [
        ("Un amigo dice «I want to leave here» y otro entiende «I want to live here». ¿Qué cambió entre ambas palabras? A) la longitud de la vocal B) la consonante final", "A) la longitud de la vocal", "Leave tiene /iː/ y live tiene /ɪ/; la consonante final es la misma."),
        ("Una persona pide «a green peach» y le dan «a grin peach». ¿Qué error de sonido hubo? A) pronunció la vocal larga de green como corta B) cambió la consonante inicial", "A) pronunció la vocal larga de green como corta", "Green tiene /iː/; grin tiene /ɪ/; las demás letras son iguales."),
    ],
    [
        ("Eva dice «Where is the pool?» y Sam entiende «Where is the pull?». ¿Qué malentendido ocurrió? A) se oyó una vocal corta en lugar de la larga de pool B) Eva cambió la consonante final de pool", "A) se oyó una vocal corta en lugar de la larga de pool", "Pool tiene /uː/ y pull tiene /ʊ/."),
        ("Un cartel en el verano dice «Keep away from the heat» (keep away = mantente lejos). ¿Qué significa heat? A) calor B) golpe", "A) calor", "Heat, con vocal larga, es calor; hit, con vocal corta, es golpe."),
    ],
    [("La palabra cheap (barato) y chip (papa frita) se diferencian por la vocal. En un cartel aparece «Cheap chips». ¿Cuál es la palabra que tiene vocal larga? A) cheap B) chips", "A) cheap", "Cheap tiene /iː/; chips tiene /ɪ/.")],
    [
        ("En Inglés de 1.º medio (OA 2, clase 3): ¿qué es un par mínimo?", "Dos palabras que se diferencian solo por un sonido, como sheep y ship", "Sirve para practicar un contraste de sonidos."),
        ("En Inglés de 1.º medio (OA 2, clase 3): ¿cómo se diferencia la vocal de feet de la de fit?", "La de feet es larga y tensa; la de fit es corta y relajada", "La duración de la vocal cambia el significado."),
        ("En Inglés de 1.º medio (OA 2, clase 3): ¿qué palabra de estas tiene vocal corta: pull o pool?", "Pull", "Pool tiene la vocal larga."),
    ],
    task("Con una persona de tu casa practica estos tres pares: sheep/ship, seat/sit, pool/pull. Tú lees una palabra de cada par en voz alta, sin mostrar tu hoja, y la otra persona dice cuál oyó. Anota cuántas acertó (de 3) y cuál par fue más difícil, y explica en una frase la diferencia entre las dos vocales.", "Acertó 2 de 3. El par más difícil fue seat/sit. En seat la vocal es larga y tensa; en sit es corta y relajada.", ["lee un par mínimo en voz alta", "anota el resultado y el par más difícil", "explica la diferencia larga/corta con sus palabras"], ["hoja con el resultado", "nota de la persona de tu casa"], ["leer ambas palabras con la misma vocal", "no explicar la diferencia"], "Reconoce el par que acertó y repite con más lentitud el que falló, alargando la vocal de la primera palabra."),
    "Lee en voz alta los seis pares mínimos de esta clase y graba o anota cuál te costó más oír.",
    "Escribe una frase en inglés con leave y otra con live, y dile a alguien que adivine cuál quisiste decir.",
)

# ------------------------------------------------------------------ clase 4: /tr/, /dr/ y /j/
lesson(
    OA, 4, MAT_R,
    "Aprenderé a reconocer y a decir los sonidos /tr/ y /dr/ al inicio de palabras (tree, dress) y el sonido /j/ inicial (year, yes). Sirve para pronunciar y entender palabras que se confunden con facilidad.",
    ["Sé leer palabras simples en inglés.", "Conozco palabras como tree, dress, year y yes."],
    [
        "Hay grupos de sonidos que comienzan palabras y que en español se dicen distinto. El grupo /tr/ está en tree, train, trip, true y truck: la t y la r se dicen juntas y la lengua se mueve hacia atrás, por lo que suena casi como «ch» + r (tree se parece a «chri»). El grupo /dr/ está en dress, drink, drive, dream y draw y suena casi como «y» fuerte + r (dress se parece a «jres»). En español t y r suenan separadas, con una r suave: no pronuncies tree como el tri de «tripa».",
        "Dos pares ayudan a practicar: try (probar) y dry (secar), y trip (viaje) y drip (gota). Si dices uno por otro, cambia el significado. Por eso en una conversación puede ser útil repetir: Did you say try or dry?",
        "El sonido /j/ inicial está en year, yes, yellow, you, young y yesterday. Ojo: la letra j de jacket o juice no suena /j/; ahí el sonido es otro. En cambio, palabras como use, union y university empiezan con /j/ aunque se escriban con u. Compara year con ear: year empieza con una consonante /j/ y ear, con una vocal.",
    ],
    [("/tr/", "tree, train, trip, true"), ("/dr/", "dress, drink, drive, dream"), ("/j/", "year, yes, yellow, you"), ("try / dry", "probar / secar"), ("trip / drip", "viaje / gota"), ("yet / jet", "todavía / avión a reacción")],
    [
        ("Clasificar por sonido inicial", "Palabras: dream, train. ¿Cuál empieza con /dr/?", ["Miro las dos letras iniciales.", "Dream empieza con d y r juntas.", "Train empieza con t y r."], "Dream"),
        ("Reconocer /j/ con u", "¿Empieza university con el sonido /j/ aunque se escribe con u?", ["Comparo con you, que empieza con /j/.", "University suena como you-niversity.", "Por eso su sonido inicial es /j/."], "Sí, empieza con /j/"),
    ],
    [
        ("Decir tree con la t y la r separadas, como el tri de «tripa».", "Se transfiere la pronunciación del español, donde la t es seca y la r es suave y aparte.", "Junta la t con la r en un solo movimiento: tree suena casi como «chri»."),
        ("Decir la j de jacket como si fuera /j/.", "Se piensa que la letra j siempre suena igual, pero el sonido inicial de jacket no es /j/.", "Compara jacket con yellow; el sonido inicial de yellow es /j/."),
    ],
    [
        ("¿Qué palabra empieza con /tr/? A) tree B) dress", "A) tree", "Tree empieza con t y r juntas."),
        ("¿Qué palabra empieza con /dr/? A) drink B) train", "A) drink", "Drink empieza con d y r juntas."),
        ("¿Qué palabra empieza con el sonido /j/? A) yellow B) jacket", "A) yellow", "Yellow empieza con /j/; jacket empieza con otro sonido."),
    ],
    [
        ("¿Qué palabra empieza con /j/ aunque se escribe con u? A) union B) uncle", "A) union", "Union suena como you-nion; uncle empieza con vocal."),
        ("¿Qué palabra empieza con una consonante /j/? A) year B) ear", "A) year", "Ear empieza con vocal."),
        ("¿Cuál empieza con el mismo sonido que yes? A) yet B) jet", "A) yet", "Yet empieza con /j/; jet empieza con otro sonido."),
    ],
    [
        ("En «Draw a dress, a tree and a truck on the page», ¿cuántas palabras empiezan con /tr/?", "2 (tree y truck)", "Draw y dress empiezan con /dr/; page no tiene ese grupo."),
        ("¿Qué palabra necesitas para decir «probar»? A) try B) dry", "A) try", "Try es probar; dry es secar."),
        ("Clasifica por sonido inicial: train, dream, yellow, jam, drive, young, true, yoga. Escribe las dos palabras con /tr/.", "train, true", "Train y true empiezan con /tr/."),
    ],
    [
        ("Alguien dice «I want to try this shirt» y otro entiende «I want to dry this shirt». ¿Qué cambió? A) la primera consonante B) la vocal final", "A) la primera consonante", "Dry empieza con d y try con t; el resto es igual."),
        ("En la frase «Yesterday, the young driver drank orange juice and drew a tree», ¿cuántas palabras empiezan con /dr/? A) 3 B) 1", "A) 3", "Driver, drank y drew empiezan con /dr/."),
    ],
    [
        ("Del texto «Yesterday, the young driver drank orange juice and drew a tree» escribe las dos palabras que empiezan con /j/.", "Yesterday y young", "Juice empieza con otro sonido, no con /j/."),
        ("Clasifica las mismas palabras de antes: train, dream, yellow, jam, drive, young, true, yoga. Escribe las tres con /j/.", "yellow, young, yoga", "Jam no empieza con /j/; las otras sí."),
    ],
    [("Una guía se presenta: «Hello, I'm Yara, a young guide. This year we offer a train trip. You can draw the lake in a free workshop.» (offer = ofrecemos, lake = lago, workshop = taller). ¿Cuántas palabras comienzan con el sonido /j/?", "4 (Yara, young, year, You)", "Son cuatro palabras con /j/ inicial.")],
    [
        ("En Inglés de 1.º medio (OA 2, clase 4): ¿cómo se pronuncia el grupo inicial /tr/ de tree?", "Con la t y la r juntas, sin vocal en medio", "No se agrega ninguna vocal."),
        ("En Inglés de 1.º medio (OA 2, clase 4): ¿cuál es el sonido inicial de year?", "/j/", "Es una consonante, como la y de yes."),
        ("En Inglés de 1.º medio (OA 2, clase 4): ¿qué par se puede confundir si cambias t por d?", "try y dry", "Cambia el significado de probar a secar."),
    ],
    task("Lee tres veces en voz alta esta frase y una persona de tu casa marca con una cruz cada vez que oiga bien el sonido: «The young driver drew a yellow tree on the train.» Luego cuenta en tu hoja cuántas palabras tienen /j/ (young, yellow), /dr/ (driver, drew) y /tr/ (tree, train).", "/j/: young y yellow = 2. /dr/: driver y drew = 2. /tr/: tree y train = 2. En la tercera lectura la persona marcó 5 cruces de 6.", ["lee la frase tres veces", "clasifica seis palabras por sonido inicial", "anota cuántos sonidos fueron claros"], ["hoja con el conteo", "cruces de la persona oyente"], ["pronunciar la t y la r separadas, como en español", "pronunciar yellow con otro sonido inicial"], "Reconoce los sonidos logrados y repite solo las palabras con cruz faltante, más lento, juntando la t o la d con la r."),
    "Di en voz alta las palabras tree, dress, year y yes diez veces cada una, cuidando el inicio.",
    "Escribe una oración con una palabra con /tr/, una con /dr/ y una con /j/, y léela a otra persona.",
)

# ------------------------------------------------------------------ clase 5: el sonido -tion y respuesta autónoma
lesson(
    OA, 5, MAT_L,
    "Aprenderé a reconocer y decir el sonido final -tion /ʃən/ (como en vacation), y a reunir todos los contenidos de esta secuencia en una escucha independiente. Sirve para entender y pronunciar muchas palabras que se parecen al español.",
    ["Conozco palabras terminadas en -ción en español.", "Sé distinguir los sonidos de la clase anterior."],
    [
        "Muchas palabras en inglés terminan en -tion, como vacation, station, information, education y celebration. Se parecen a palabras en español terminadas en -ción, pero el final se pronuncia /ʃən/, como shon, con un sonido suave tipo sh. No se dice ti-on ni se pronuncia la t como en español. Una excepción conocida es question, cuyo final suena /tʃən/ (como «chon»).",
        "La fuerza de la palabra cae en la sílaba justo antes de -tion: vaCAtion, inforMAtion, eduCAtion, celeBRAtion. Si pones la fuerza en otra sílaba, cuesta que te entiendan. Practica diciendo la palabra con un golpe suave en la sílaba marcada, y deja el final corto.",
        "En una escucha independiente aplicas todo: reconoces collocations, conectores, vocales largas y cortas, /tr/ /dr/, /j/ y -tion. Primero busca el tema, luego las palabras clave y por último los sonidos. Si una palabra no se entiende, piensa en las que sí entendiste y en el contexto antes de decidir.",
    ],
    [("-tion /ʃən/", "terminación: vacation, station"), ("vacation", "vacaciones"), ("station", "estación"), ("information", "información"), ("celebration", "celebración"), ("stress", "acento: la sílaba que suena más fuerte")],
    [
        ("Reconocer -tion", "En «Excuse me, where is the bus station? I need some information», ¿qué palabras terminan en -tion?", ["Reviso las terminaciones de cada palabra.", "Station termina en -tion.", "Information también."], "Station e information"),
        ("Ubicar el acento", "En vacation, ¿qué sílaba suena más fuerte?", ["Separo en va-ca-tion.", "La fuerza cae justo antes de -tion.", "Es va-CA-tion."], "La segunda sílaba: va-CA-tion"),
    ],
    [
        ("Pronunciar -tion como ti-on, igual que se lee en español.", "Se lee la t como en español y se separa la terminación en dos sílabas.", "Di una sola sílaba suave: shon."),
        ("Poner la fuerza en la primera sílaba de information.", "Se copia el acento de otras palabras, pero en -tion cae antes de la terminación.", "Marca in-for-MA-tion con la fuerza en -ma-."),
    ],
    [
        ("¿Cómo suena el final -tion en vacation? A) como shon (/ʃən/) B) como ti-on", "A) como shon (/ʃən/)", "La terminación es una sola sílaba suave con /ʃ/."),
        ("¿Qué palabra termina en -tion? A) station B) statue", "A) station", "Station termina en -tion; statue no."),
        ("¿Cuál es el equivalente en español de station? A) estación B) estatua", "A) estación", "Station y estación tienen el mismo origen y significado."),
    ],
    [
        ("¿Qué sílaba suena más fuerte en information? A) -ma- B) in-", "A) -ma-", "La fuerza cae justo antes de -tion: in-for-MA-tion."),
        ("¿Qué sílaba suena más fuerte en celebration? A) -bra- B) cel-", "A) -bra-", "La sílaba fuerte es cel-e-BRA-tion."),
        ("¿Qué sílaba suena más fuerte en education? A) -ca- B) ed-", "A) -ca-", "Es ed-u-CA-tion, con la fuerza antes de -tion."),
    ],
    [
        ("En «Excuse me, where is the train station? I need some information about vacation tickets», ¿cuántas palabras terminan en -tion?", "3 (station, information y vacation)", "Cada una termina en -tion."),
        ("Escribe en inglés la palabra para «conversación».", "conversation", "Cambia -ción por -tion: conversation."),
        ("¿Cuál de estas palabras NO termina con el sonido /ʃən/? A) question B) station", "A) question", "Question es la excepción: termina en /tʃən/; station termina en /ʃən/."),
    ],
    [
        ("Un amigo dice que education se dice con una t fuerte como en español. ¿Qué le corriges? A) que termina en /ʃən/ y la fuerza cae antes de -tion B) que se dice ti-on, en dos sílabas", "A) que termina en /ʃən/ y la fuerza cae antes de -tion", "En education el final es /ʃən/ y se acentúa -ca-."),
        ("Alguien lee vacation como VA-ca-tion. ¿Qué cambia si lo dice bien? A) pone la fuerza en la segunda sílaba: va-CA-tion B) pone la fuerza en tion", "A) pone la fuerza en la segunda sílaba: va-CA-tion", "La fuerza cae justo antes de -tion."),
    ],
    [
        ("Un adulto lee: «Last year, on vacation, I took a train to a beautiful station near a lake. The young guide gave us information. I drank lemonade and drew a tree.» (lake = lago, lemonade = limonada). Escribe las palabras con -tion.", "vacation, station, information", "Las tres terminan en -tion."),
        ("Del mismo texto, escribe las dos palabras que empiezan con /j/: «Last year, on vacation, I took a train to a beautiful station near a lake. The young guide gave us information. I drank lemonade and drew a tree.»", "year y young", "Son las dos únicas con /j/ inicial."),
    ],
    [("Una invitación dice: «Invitation to the school celebration: Please join us on Friday at six. Registration is free. For more information, call the school office.» (join = únete, registration = inscripción, free = gratis, office = oficina). ¿Cuántas palabras terminan en -tion?", "4 (invitation, celebration, registration e information)", "Se cuentan las cuatro palabras con la terminación -tion.")],
    [
        ("En Inglés de 1.º medio (OA 2, clase 5): ¿cómo se pronuncia -tion?", "Como /ʃən/, parecido a shon", "Es una sola sílaba suave con sonido sh."),
        ("En Inglés de 1.º medio (OA 2, clase 5): ¿dónde cae la fuerza en palabras terminadas en -tion?", "En la sílaba justo antes de -tion", "Por ejemplo, va-CA-tion."),
        ("En Inglés de 1.º medio (OA 2, clase 5): ¿cuál es el sonido inicial de year?", "/j/", "Es la consonante de yes."),
    ],
    task("Un adulto lee dos veces este mensaje: «Good evening, everyone. Welcome to the celebration. Thank you for your attention. Please take a program for more information.» (everyone = todos, attention = atención, program = programa). Anota las palabras con -tion y, en una de ellas, marca la sílaba que suena más fuerte.", "Celebration, attention, information. Por ejemplo: cel-e-BRA-tion.", ["encuentra las tres palabras con -tion", "marca la sílaba fuerte de una palabra", "dice la terminación como /ʃən/"], ["hoja con las palabras", "nota del adulto"], ["no anotar attention", "poner la fuerza en la última sílaba"], "Reconoce lo logrado y repite solo la palabra con la sílaba fuerte mal marcada, dando un golpe suave en la sílaba antes de -tion."),
    "Escribe cinco palabras en español terminadas en -ción y piensa cómo se dirían en inglés con -tion.",
    "Prepara una frase corta que tenga una palabra con -tion, una con /tr/ y una con /j/, y léela en voz alta.",
)

"""Cuaderno del estudiante, 6.º básico Inglés (propuesta), EN06 OA 01 (comprensión de textos orales de distintos tipos).

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Los textos son originales y llevan pista en español. Cada palabra o estructura nueva se explica antes de usarla.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1 = "EN06 OA 01"
ADULT = "Un adulto lee en voz alta (tapa el guion): "


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


# ---------------------------------------------------------------- textos de la clase 1 (poemas y canciones)
WIND = "«The wind is a runner, it runs through the street. It shakes every tree and it tickles my feet. It sings in the window, it whistles at night. Then it falls fast asleep when the morning is bright.» (wind = viento, shakes = sacude, tickles = hace cosquillas, feet = pies, whistles = silba, falls asleep = se duerme, bright = luminosa)"
LULLABY = "«Close your eyes, little bird, the night is deep. The moon is a lamp and the stars watch you sleep. Hush, hush, hush, the day is done. Hush, hush, hush, I'm here, little one.» (deep = profunda, lamp = lámpara, hush = shhh, done = terminado)"
PARTY = "«Verse 1: Clap your hands, one two three! Jump up high and dance with me! Chorus: Boom, boom, boom goes the drum! Everybody, here we come! Verse 2: Turn around and touch the ground. Move your feet to the beat and sound! Chorus: Boom, boom, boom goes the drum! Everybody, here we come!» (clap = aplaudir, jump = saltar, drum = tambor, turn around = girar, ground = suelo, beat = ritmo)"
GRAY = "«The day is gray, my friend is far. I look outside, I see no star. I feel alone, I feel so small. I miss my friend, that's all, that's all.» (gray = gris, far = lejos, alone = solo, small = pequeño, miss = extrañar)"

lesson(
    OA1, 1,
    "Los poemas y canciones escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a fijarme en el propósito y en el contexto de un poema o una canción: para qué se dice, quién habla y cómo se siente. Sirve para entender poemas y canciones en inglés sin traducir cada palabra.",
    ["Sé que dos palabras riman si terminan con el mismo sonido.", "Conozco palabras como night, moon, sleep y dance."],
    [
        "Un poema (poem) y una canción (song) se dividen en estrofas (verses). En una canción, el coro (chorus) es la parte que se repite. Antes de entender cada línea, pregúntate para qué existe el texto: su propósito (purpose). Una canción de cuna sirve para calmar, una canción de fiesta sirve para bailar y un poema puede describir algo.",
        "El contexto (context) es la situación: quién habla, a quién y en qué momento. Las palabras clave (key words) te dan pistas. Si oyes moon, night y sleep, el contexto es la noche. Si oyes clap, jump y dance, el contexto es una fiesta. Las palabras como hush (shhh) o alone (solo) muestran el ánimo, es decir, cómo se siente quien habla.",
        "Las rimas (rhymes) ayudan a recordar: street rima con feet porque terminan con el mismo sonido. Escucha dos veces. La primera vez busca el propósito y el contexto. La segunda vez, fíjate en las rimas y en las palabras repetidas. No necesitas entender todas las palabras para comprender el texto.",
    ],
    [("purpose", "propósito: para qué existe el texto"), ("context", "contexto: quién habla y en qué situación"), ("verse", "estrofa"), ("chorus", "coro: parte que se repite"), ("rhyme", "rima: sonido final igual"), ("key word", "palabra clave")],
    [
        ("Propósito y contexto", ADULT + WIND + " ¿Qué describe el poema y en qué momentos del día ocurre?", ["Busco palabras clave: wind, runs, shakes, sings, whistles.", "Las pistas de tiempo son at night y the morning.", "El propósito es describir el viento; ocurre de noche hasta la mañana."], "Describe el viento, desde la noche hasta la mañana"),
        ("Encontrar una rima", "En el poema del viento, ¿qué palabra rima con street?", ["Miro el final de cada línea: street, feet, night, bright.", "Street y feet terminan con el mismo sonido.", "Night rima con bright, no con street."], "feet"),
    ],
    [
        ("Pensar que un texto con rimas es siempre una canción para bailar.", "Las rimas aparecen en todo tipo de poemas y canciones.", "El propósito lo dicen las palabras clave: moon y sleep indican calma, no baile."),
        ("Detenerse en una palabra que no se entiende y perder el resto.", "Se intenta traducir todo y se pierde el sentido general.", "Sigue escuchando y apóyate en las palabras clave y en el contexto."),
    ],
    [
        (ADULT + LULLABY + " ¿Para qué sirve esta canción? a) para calmar a alguien que va a dormir b) para hacer bailar a un grupo c) para enseñar a contar", "a) para calmar a alguien que va a dormir", "Night, moon, sleep y hush indican calma."),
        (ADULT + PARTY + " ¿Cuál es el coro, es decir, la parte que se repite? a) Boom, boom, boom goes the drum! b) Clap your hands, one two three!", "a) Boom, boom, boom goes the drum!", "Esa línea aparece después de cada estrofa."),
        (ADULT + LULLABY + " En la canción de cuna, ¿qué palabra rima con sleep?", "deep", "Deep y sleep terminan con el mismo sonido."),
    ],
    [
        (ADULT + GRAY + " ¿Cómo se siente quien habla? a) solo y triste b) contento y con energía", "a) solo y triste", "Alone, small y miss muestran tristeza."),
        (ADULT + PARTY + " ¿Qué grupo de palabras muestra que es una canción para bailar? a) clap, jump, dance b) sleep, moon, hush", "a) clap, jump, dance", "Son acciones de movimiento y fiesta."),
        (ADULT + GRAY + " ¿Qué par de palabras rima? a) far y star b) gray y small", "a) far y star", "Far y star terminan con el mismo sonido."),
    ],
    [
        (ADULT + PARTY + " ¿Cuántas veces se canta el coro completo?", "2", "Hay un coro después de cada una de las dos estrofas."),
        (ADULT + GRAY + " ¿Cuántos pares de palabras que riman hay al final de las líneas?", "2", "Far con star y small con all."),
        ("Completa la rima: «Wake up, wake up, the sun is high. Look out the window, see the ___.» Opciones: sky, floor, bed.", "sky", "High y sky terminan con el mismo sonido."),
    ],
    [
        ("Luis dice: «Como el poema de la tristeza tiene rimas, es una canción de fiesta». ¿Tiene razón? Responde sí o no.", "No", "Las rimas no definen el propósito; alone y miss muestran tristeza."),
        ("¿Qué par de palabras muestra el contraste entre calma y energía? a) hush – jump b) hush – sleep c) jump – dance", "a) hush – jump", "Hush es calma y jump es movimiento; en las otras opciones las dos palabras van juntas."),
    ],
    [
        (ADULT + LULLABY + " ¿Cuántas veces se oye la palabra hush?", "6", "Son tres hush en una línea y tres en la otra."),
        ("Ordena según el momento del día. A) «The moon is up, the town is still.» B) «The sun is up, the birds begin to sing.» C) «The sun goes down behind the hill.» (still = quieto)", "B, C, A", "Primero amanece, luego atardece y al final es de noche."),
    ],
    [("En el acto de bienvenida del colegio, todo el curso va a cantar moviendo las manos. ¿Qué texto es mejor? a) la canción de cuna sobre la luna b) la canción que dice «Clap your hands» c) el poema triste de la amiga lejana", "b) la canción que dice «Clap your hands»", "Esa canción invita a aplaudir y moverse junto al grupo.")],
    [
        ("¿Qué es el coro de una canción?", "La parte que se repite", "Vuelve a aparecer después de cada estrofa."),
        ("¿Qué dos cosas te dice el contexto de un texto?", "Quién habla y en qué situación", "Así se entiende la situación."),
        ("¿Riman light y night?", "Sí", "Las dos terminan con el mismo sonido."),
    ],
    task("Un adulto lee dos veces este poema: «Warm sun, warm sand. I hold a shell in my hand. Blue sea, blue sky. A white gull flies by.» (warm = tibio, shell = concha, hand = mano, gull = gaviota, flies by = pasa volando). En tu hoja escribe: el propósito del poema (describir, calmar o bailar), dos pares de palabras que riman y dos palabras que se repiten.", "Describe un día de playa. Riman sand-hand y sky-by. Se repiten warm y blue.", ["escribe un propósito coherente con el texto", "anota los dos pares de rima", "anota las dos palabras repetidas"], ["hoja con respuestas", "nota del adulto"], ["decir que riman sun y sand", "no anotar las palabras repetidas"], "Reconoce lo que acertó y vuelve a leer con la persona solo los finales de cada línea para encontrar las rimas."),
    "Pide a un adulto que lea el poema del viento y levanta la mano cada vez que oigas una palabra que rime con feet o night.",
    "Escribe dos líneas que rimen sobre tu día favorito, por ejemplo con las palabras day y play.",
)

# ---------------------------------------------------------------- clase 2 (cuentos y narraciones)
LOSTKEY = "«On Saturday morning, Daniela cannot find her bike key. She looks in her room, under the table and in her backpack. Then her brother laughs and says: It is in your jacket! Daniela puts her hand in the pocket. The key is there. She says Thanks! and rides to the park.» (cannot find = no puede encontrar, key = llave, bike = bicicleta, backpack = mochila, laughs = se ríe, jacket = chaqueta, pocket = bolsillo, rides = va en bicicleta)"
TRIP = "«Last winter, my cousin Pedro visited the south of Chile. First, he took a boat to an island. Then he walked in the forest and saw a tall green tree. At night, he slept in a small wooden house. He was tired but very happy.» (visited = visitó, south = sur, boat = bote, island = isla, forest = bosque, wooden = de madera, tired = cansado)"

lesson(
    OA1, 2,
    "Los cuentos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a encontrar palabras clave y pistas en un cuento o una narración: quién es el personaje, dónde y cuándo pasa, cuál es el problema y cómo termina. Sirve para seguir historias en inglés.",
    ["Sé que first, then y finally ordenan una historia.", "Conozco palabras como morning, night, brother y park."],
    [
        "Un cuento (story) tiene personajes (characters), que son quienes actúan. Tiene un lugar (place) y un momento (time), que juntos forman el entorno (setting). Muchos cuentos presentan un problema (problem) y luego una solución (solution). Una narración (narration) cuenta hechos en orden, aunque no siempre tenga un problema.",
        "Las palabras clave son las que sostienen el significado. Los nombres propios indican los personajes. Palabras como Saturday morning, last winter o at night indican el tiempo. Palabras como park, island o forest indican el lugar. Las palabras de secuencia first, then, after that y finally te dicen el orden de los hechos.",
        "Para escuchar mejor, tenemos tres preguntas: who (¿quién?), where/when (¿dónde y cuándo?) y what happens (¿qué pasa?). Si no entiendes una palabra, no te detengas: busca la pista en la oración siguiente. Por ejemplo, si oyes backpack y no la conoces, fíjate en que Daniela la revisa junto a su room y la table: es un lugar donde buscar cosas.",
    ],
    [("character", "personaje"), ("setting", "entorno: lugar y tiempo"), ("problem / solution", "problema / solución"), ("key word", "palabra clave"), ("first, then, finally", "primero, luego, finalmente"), ("narration", "narración: hechos contados en orden")],
    [
        ("Personaje, problema y solución", ADULT + "«Max has a problem: his kite is stuck in a tree. He tries to jump, but the tree is too tall. Then he asks Mrs. Rojas for a long stick. She helps him, and the kite is free.» (kite = volantín, stuck = atascado, stick = palo). ¿Cuál es el problema y cuál la solución?", ["Busco la palabra problem y lo que sigue: the kite is stuck in a tree.", "Busco quién ayuda: Mrs. Rojas da un palo largo.", "El volantín se baja con el palo."], "Problema: el volantín está en un árbol. Solución: usa un palo largo que le da la Sra. Rojas"),
        ("Pistas de tiempo", "Mira esta oración: «Yesterday afternoon, Camila played chess in the library.» (chess = ajedrez, library = biblioteca). ¿Cuál es la pista de tiempo y cuál la de lugar?", ["Pistas de tiempo: yesterday afternoon.", "Pista de lugar: in the library.", "Camila es el personaje."], "Tiempo: yesterday afternoon. Lugar: in the library"),
    ],
    [
        ("Decir que el cuento pasa en la noche porque se oye la palabra «lake».", "Se confunden la pista de lugar con la de tiempo.", "El tiempo lo dicen palabras como morning, night o winter."),
        ("Contar el final antes que el comienzo.", "No se sigue el orden marcado por first, then y finally.", "Usa las palabras de secuencia para ordenar los hechos."),
    ],
    [
        (ADULT + LOSTKEY + " ¿Qué busca Daniela? a) la llave de su bicicleta b) su mochila c) su chaqueta", "a) la llave de su bicicleta", "Dice cannot find her bike key."),
        (ADULT + LOSTKEY + " ¿Dónde estaba lo que buscaba? a) en el bolsillo de la chaqueta b) debajo de la mesa", "a) en el bolsillo de la chaqueta", "Su hermano dice que está en la jacket y ella la encuentra en el pocket."),
        (ADULT + LOSTKEY + " ¿Cuándo pasa la historia? a) sábado en la mañana b) domingo en la noche", "a) sábado en la mañana", "La primera oración dice Saturday morning."),
    ],
    [
        (ADULT + LOSTKEY + " ¿Quién ayuda a Daniela a resolver el problema?", "Su hermano", "Her brother le dice dónde está."),
        (ADULT + LOSTKEY + " ¿Cuántos lugares revisa Daniela antes de que hable su hermano?", "3", "Revisa su room, under the table y su backpack."),
        (ADULT + LOSTKEY + " ¿Qué hace Daniela al final? a) va en bicicleta al parque b) llama a su hermano c) se queda en su pieza", "a) va en bicicleta al parque", "Termina diciendo Thanks! y rides to the park."),
    ],
    [
        (ADULT + TRIP + " ¿En qué transporte viaja Pedro primero?", "En un bote", "Dice First, he took a boat."),
        (ADULT + TRIP + " ¿Dónde durmió Pedro? a) en una casa pequeña de madera b) en una carpa c) en el bote", "a) en una casa pequeña de madera", "Dice he slept in a small wooden house."),
        (ADULT + TRIP + " ¿Cómo se sentía Pedro al final? a) cansado pero muy feliz b) enojado c) asustado", "a) cansado pero muy feliz", "Dice he was tired but very happy."),
    ],
    [
        ("Ordena los hechos de la historia de Pedro. A) Caminó por el bosque. B) Durmió en una casa de madera. C) Viajó en bote a una isla.", "C, A, B", "La secuencia es: first el bote, then el bosque, at night la casa."),
        ("Lucía dice que Pedro visitó el norte. ¿Qué pista de la historia muestra que se equivoca?", "the south of Chile", "El texto dice que visitó el sur, no el norte."),
    ],
    [
        ("En la historia de Daniela, ¿cuántas personas aparecen como personajes?", "2", "Aparecen Daniela y su hermano."),
        ("¿En qué historia hay un problema que se resuelve: la de Daniela o la de Pedro?", "La de Daniela", "Daniela pierde la llave y la encuentra; Pedro solo cuenta un viaje."),
    ],
    [(ADULT + "Un amigo te deja este mensaje de voz: «Yesterday I lost my pencil case at the library. The librarian found it under a chair.» (pencil case = estuche, librarian = bibliotecaria, found = encontró). ¿Dónde estaba el estuche?", "Debajo de una silla", "Dice under a chair.")],
    [
        ("¿Qué es el setting de un cuento?", "El lugar y el tiempo donde pasa", "Setting es el entorno de la historia."),
        ("¿Qué palabra indica el tiempo en «Last winter, Pedro traveled»?", "last winter", "Last winter dice cuándo pasó."),
        ("¿Para qué sirven first, then y finally?", "Para ordenar los hechos", "Marcan la secuencia."),
    ],
    task("Un adulto lee dos veces este cuento: «One cold evening, Rita finds a small cat near her door. The cat is hungry. Rita gives it a bowl of milk. The cat drinks and purrs. Rita smiles.» (finds = encuentra, hungry = hambriento, bowl = plato hondo, purrs = ronronea). Escribe en tu hoja: el personaje principal, el momento, el lugar y las tres partes: comienzo, medio y final.", "Personaje: Rita. Momento: una tarde fría. Lugar: cerca de su puerta. Comienzo: encuentra un gato. Medio: le da leche. Final: el gato ronronea y ella sonríe.", ["nombra el personaje, el momento y el lugar", "escribe las tres partes en orden", "usa pistas del texto"], ["hoja con respuestas", "nota del adulto"], ["poner el final primero", "olvidar el momento (one cold evening)"], "Reconoce lo que acertó y repasa con la persona el orden de los hechos con las palabras first, then y finally."),
    "Pide a un adulto que lea de nuevo el cuento de Daniela y levanta un dedo cada vez que oigas un lugar.",
    "Escribe tres frases en español con el comienzo, el medio y el final de la historia de Pedro.",
)

# ---------------------------------------------------------------- clase 3 (diálogos y entrevistas)
INTERVIEW = "«Reporter: Good morning, Marta. How old are you? Marta: I'm twelve. Reporter: What sport do you play? Marta: I play basketball on Tuesdays and Thursdays. Reporter: Why do you like it? Marta: Because it is fun and I play with my friends.» (reporter = periodista, sport = deporte, Tuesdays = los martes, Thursdays = los jueves, fun = entretenido)"
PHONE = "«Tomás: Hello, Rosa. Can you come to my house on Friday? Rosa: Sorry, I can't. I have a violin class at four. Tomás: How about Saturday? Rosa: Yes, great! See you at ten.» (Can you come? = ¿puedes venir?, class = clase, How about = ¿y qué tal?)"
SHOP = "«Customer: How much is the blue cap? Seller: It is four thousand pesos. Customer: And the red cap? Seller: It is three thousand five hundred pesos. Customer: I'll take the red one, please.» (cap = gorro, seller = vendedor, I'll take = me llevo)"

lesson(
    OA1, 3,
    "Los diálogos y entrevistas escritos en cada ejercicio, que lee un adulto con voces distintas; una hoja para tapar el guion y lápiz.",
    "Aprenderé una estrategia para entender diálogos y entrevistas: saber quién pregunta, quién responde y qué tipo de dato pide cada pregunta. Sirve para entender conversaciones reales en inglés.",
    ["Sé que en una conversación se habla por turnos.", "Conozco How old are you? y What is your name?"],
    [
        "Un diálogo (dialogue) es una conversación entre dos o más personas. Una entrevista (interview) es un diálogo donde el periodista (reporter) hace preguntas y la persona entrevistada responde. Para saber quién habla, fíjate en el nombre que antecede cada turno. Cuenta solo los nombres distintos para saber cuántas personas hablan.",
        "La estrategia es escuchar primero la palabra interrogativa, porque anuncia qué dato viene. How old pide un número. What sport pide el nombre de un deporte. Where pide un lugar. When pide un tiempo. Why pide una razón, y la respuesta suele empezar con because (porque). How much pide un precio.",
        "Después de la pregunta, busca la respuesta en el turno siguiente. Si escuchas un número, un lugar o una hora, ya tienes el dato. También ayudan las expresiones de cortesía: Sorry, I can't (lo siento, no puedo) indica un rechazo; Great! indica que algo gusta. Un diálogo se entiende mejor si ordenas: pregunta, respuesta y conclusión.",
    ],
    [("dialogue", "diálogo"), ("interview", "entrevista"), ("question word", "palabra interrogativa: How, What, Where, When, Why"), ("because", "porque"), ("How much?", "¿cuánto cuesta?"), ("I can't", "no puedo")],
    [
        ("La palabra interrogativa anuncia el dato", ADULT + "«Teacher: Where do you live, Pablo? Pablo: I live in Temuco. Teacher: How do you go to school? Pablo: I go by bus.» (live = vive, by bus = en bus). ¿Dónde vive Pablo y cómo va al colegio?", ["Where pide un lugar: I live in Temuco.", "How pide la manera: by bus.", "Reúno ambos datos."], "Vive en Temuco y va en bus"),
        ("Quién pregunta y quién responde", "En el mismo diálogo, ¿cuántas personas hablan y quién hace las preguntas?", ["Los nombres que anteceden los turnos son Teacher y Pablo.", "Son dos personas distintas.", "Teacher es quien pregunta."], "Dos personas; pregunta Teacher"),
    ],
    [
        ("Contar cuatro personas porque hay seis turnos.", "Se cuentan los turnos y no los nombres distintos.", "Cuenta solo los nombres diferentes: en una entrevista suelen ser dos."),
        ("Responder a Why con un lugar.", "No se escucha la palabra interrogativa.", "Why pide una razón y la respuesta suele empezar con because."),
    ],
    [
        (ADULT + INTERVIEW + " ¿Qué edad tiene Marta? a) 12 años b) 10 años c) 14 años", "a) 12 años", "Responde I'm twelve a How old are you?"),
        (ADULT + INTERVIEW + " ¿Qué deporte juega Marta?", "Básquetbol", "Responde I play basketball."),
        (ADULT + INTERVIEW + " ¿Por qué le gusta ese deporte? a) porque es entretenido y juega con sus amigos b) porque gana siempre", "a) porque es entretenido y juega con sus amigos", "Responde a Why con because it is fun and I play with my friends."),
    ],
    [
        (ADULT + PHONE + " ¿Qué día no puede ir Rosa a la casa de Tomás? a) viernes b) sábado", "a) viernes", "Dice Sorry, I can't cuando Tomás le propone Friday."),
        (ADULT + PHONE + " ¿Por qué no puede ir Rosa ese día?", "Porque tiene clase de violín", "Dice I have a violin class at four."),
        (ADULT + PHONE + " ¿A qué hora se verán el sábado?", "A las diez", "Rosa dice See you at ten."),
    ],
    [
        ("Lee: «Reporter: When is your match? Marta: It is on Saturday at nine. Reporter: Where is it? Marta: At the school gym.» (match = partido, gym = gimnasio). ¿Qué dato pide when y qué dato pide where?", "When pide el momento y where pide el lugar", "Saturday at nine es el momento y the school gym es el lugar."),
        ("En el mismo diálogo, ¿dónde se juega el partido?", "En el gimnasio del colegio", "La respuesta a where es At the school gym."),
        ("En el mismo diálogo, ¿a qué hora se juega el partido?", "A las nueve", "La respuesta a when incluye at nine."),
    ],
    [
        ("Un compañero dice que Rosa acepta ir el viernes porque dice «Great!». ¿Qué error cometió?", "Great! lo dice para el sábado, no para el viernes", "Para el viernes dice Sorry, I can't."),
        (ADULT + SHOP + " ¿Cuántos pesos más cuesta el gorro azul que el rojo?", "500", "La diferencia entre 4.000 y 3.500 pesos es 500.", "4000-3500"),
    ],
    [
        (ADULT + SHOP + " ¿Qué gorro compra el cliente y cuál de los dos cuesta menos?", "El rojo, que cuesta menos", "El rojo cuesta 3.500 pesos y el azul 4.000 pesos."),
        (ADULT + "«Girl: Excuse me, where is the library? Boy: It is next to the gym. Girl: How do I get there? Boy: Go straight and turn left.» (excuse me = disculpa, next to = al lado de, turn left = gira a la izquierda). ¿Qué dos datos entrega el niño?", "Está al lado del gimnasio y hay que ir derecho y girar a la izquierda", "Responde a where y a how con esas indicaciones."),
    ],
    [(ADULT + "En una papelería un cliente pregunta: «How much is the red pencil box?» y la vendedora responde: «It is two thousand pesos.» (pencil box = estuche). ¿Qué dato entrega la respuesta?", "El precio: 2.000 pesos", "How much pide un precio.")],
    [
        ("¿Qué pide la pregunta «When is the match?»", "Un tiempo (día u hora)", "When pregunta por el momento."),
        ("¿Con qué palabra empieza normalmente la respuesta a Why?", "because", "Because significa porque."),
        ("¿Qué significa «I can't»?", "No puedo", "Es una negación de can."),
    ],
    task("Un adulto lee dos veces este diálogo: «Ana: Hi, Leo! What are you doing on Sunday? Leo: I'm going to the park with my cousin. Ana: What time? Leo: At eleven. Ana: Can I come? Leo: Of course!» (cousin = primo, of course = por supuesto). Escribe: quién pregunta, a dónde va Leo, a qué hora y con quién, y si invita a Ana.", "Ana pregunta. Leo va al parque a las once con su primo y sí invita a Ana.", ["identifica al que pregunta", "escribe lugar, hora y compañía", "dice que Leo acepta"], ["hoja con respuestas", "nota del adulto"], ["confundir quién pregunta", "no escribir la hora"], "Reconoce lo que acertó y repite con la persona las palabras interrogativas y el dato que pide cada una."),
    "Pide a un adulto que lea el diálogo de Tomás y Rosa con dos voces y marca con un lápiz cada palabra interrogativa que oigas.",
    "Escribe un diálogo de cuatro líneas en que una persona pregunta What time? y otra responde.",
)

# ---------------------------------------------------------------- clase 4 (exposiciones orales)
PENGUIN = "«Today I am going to talk about penguins. Penguins are birds, but they cannot fly. They swim very fast and they eat fish. Some penguins live on the coast of Chile. Thank you for listening.» (talk about = hablar sobre, fly = volar, swim = nadar, fish = pescado, coast = costa, thank you for listening = gracias por escuchar)"
RECYCLE = "«Good afternoon. My topic is recycling. We can recycle paper, plastic and cans. First, we put each thing in the right bin. Second, we keep the bins clean. Recycling helps our planet. That is all. Thank you.» (recycling = reciclaje, cans = latas, bin = basurero, helps = ayuda, planet = planeta)"
LIBRARY = "«Our school library has eight hundred books. It opens at eight in the morning and closes at four in the afternoon. Students can take two books for one week. The library is a quiet place, so please do not shout.» (opens = abre, closes = cierra, quiet = silencioso, shout = gritar)"

lesson(
    OA1, 4,
    "Las exposiciones escritas en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a entender una exposición oral: cómo empieza, qué datos entrega y cómo se despide quien expone. Sirve para tomar apuntes de lo que alguien presenta en inglés.",
    ["Sé que una exposición tiene un tema y datos sobre él.", "Conozco palabras como birds, fish y paper."],
    [
        "Una exposición oral (oral presentation) es un texto en que una persona informa sobre un tema. Tiene tres partes. La introducción (introduction) dice el tema, por ejemplo «Today I am going to talk about...» o «My topic is...». El desarrollo (body) entrega datos. El cierre (closing) termina con «Thank you» o «That is all».",
        "En el desarrollo, quien expone usa palabras para ordenar los datos: first (primero), second (segundo), also (además), finally (finalmente). También usa números, lugares y horas. Para tomar apuntes, escribe solo las palabras clave y los números. Por ejemplo: 800 libros, abre 8:00, cierra 16:00. No necesitas escribir oraciones completas.",
        "Después de escuchar, comprueba si puedes responder tres preguntas: ¿cuál es el tema?, ¿cuáles son los datos más importantes? y ¿cómo cierra la exposición? Si una palabra se te escapa, usa el contexto: en «Penguins are birds, but they cannot fly» la palabra but indica un contraste. Escuchar con ese propósito ayuda a recordar mejor.",
    ],
    [("oral presentation", "exposición oral"), ("topic", "tema"), ("introduction / body / closing", "introducción / desarrollo / cierre"), ("first, second, also", "primero, segundo, además"), ("but", "pero: marca contraste"), ("Thank you for listening", "gracias por escuchar")],
    [
        ("Encontrar el tema", ADULT + "«Hello, everyone. Today I am going to talk about bees. Bees are insects with six legs. They make honey and they live in groups. Bees help flowers grow. Thank you.» (bees = abejas, legs = patas, honey = miel, flowers = flores, grow = crecer). ¿Cuál es el tema?", ["Busco la frase Today I am going to talk about.", "Después dice bees.", "El tema son las abejas."], "Las abejas"),
        ("Tomar apuntes", "En el mismo texto, anota dos datos importantes con palabras clave.", ["Subrayo lo que dice sobre las abejas: six legs, honey, groups, flowers.", "Escribo solo palabras clave.", "Elijo dos datos."], "Por ejemplo: 6 patas y hacen miel"),
    ],
    [
        ("Pensar que las exposiciones no tienen una forma fija.", "No se reconocen las tres partes de una presentación.", "Busca la introducción, el desarrollo y el cierre."),
        ("Querer escribir todo lo que se dice al tomar apuntes.", "Se pierde el hilo por escribir demasiado.", "Anota solo palabras clave y números."),
    ],
    [
        (ADULT + PENGUIN + " ¿Cuál es el tema? a) los pingüinos b) los delfines c) los peces", "a) los pingüinos", "Dice Today I am going to talk about penguins."),
        (ADULT + PENGUIN + " ¿Qué no pueden hacer los pingüinos? a) volar b) nadar", "a) volar", "Dice they cannot fly."),
        (ADULT + PENGUIN + " ¿Con qué frase cierra la exposición? a) Thank you for listening. b) Good morning.", "a) Thank you for listening.", "Es la despedida al final de la exposición."),
    ],
    [
        (ADULT + RECYCLE + " ¿Cuáles son los tres materiales que se pueden reciclar? Responde con tres palabras en español.", "Papel, plástico y latas", "Dice paper, plastic and cans."),
        (ADULT + RECYCLE + " ¿Qué dice quien expone que se hace en el segundo paso? a) mantener limpios los basureros b) botar la basura en la calle", "a) mantener limpios los basureros", "Second, we keep the bins clean."),
        (ADULT + RECYCLE + " ¿Cuántos pasos numera quien expone con palabras de orden?", "2", "Usa first y second."),
    ],
    [
        (ADULT + LIBRARY + " ¿Cuántos libros tiene la biblioteca?", "800", "El texto dice eight hundred books."),
        (ADULT + LIBRARY + " ¿Cuántas horas está abierta la biblioteca, desde las 8:00 hasta las 16:00?", "8", "Entre las 8 de la mañana y las 4 de la tarde pasan 8 horas.", "16-8"),
        (ADULT + LIBRARY + " Si cada estudiante puede llevar 2 libros, ¿cuántos libros se llevan 5 estudiantes?", "10", "Cada uno lleva 2 y son 5 personas.", "2*5"),
    ],
    [
        ("Una compañera anotó para la exposición de la biblioteca: «800 books, opens 8, closes 4, 2 books per student». ¿Es un buen apunte? Responde sí o no.", "Sí", "Contiene solo palabras clave y números del texto."),
        (ADULT + RECYCLE + " En la exposición, ¿cuál es la frase de cierre? a) That is all. Thank you. b) My topic is recycling.", "a) That is all. Thank you.", "My topic is recycling es la introducción."),
    ],
    [
        ("Un expositor dice: «First, wash the apple. Second, cut it. Finally, eat it.» (wash = lavar, cut = cortar). Ordena los pasos: A) comer B) cortar C) lavar", "C, B, A", "First es lavar, second es cortar, finally es comer."),
        ("Otra exposición dice: «Cats sleep a lot, but dogs sleep less.» (a lot = mucho, less = menos). ¿Qué palabra marca el contraste?", "but", "But significa pero."),
    ],
    [(ADULT + "En una feria de ciencias, un estudiante dice: «My topic is volcanoes. A volcano has a hole at the top. Hot rock comes out of it.» (volcano = volcán, hole = hoyo, hot rock = roca caliente). ¿De qué habla la exposición?", "De los volcanes", "My topic is volcanoes anuncia el tema.")],
    [
        ("¿Cuáles son las tres partes de una exposición?", "Introducción, desarrollo y cierre", "Así se organiza una presentación."),
        ("¿Qué significa «Thank you for listening»?", "Gracias por escuchar", "Es una despedida."),
        ("¿Qué escribes al tomar apuntes: oraciones completas o palabras clave?", "Palabras clave", "Son más rápidas de anotar."),
    ],
    task("Un adulto lee dos veces esta exposición: «Good morning. My topic is the moon. The moon goes around the Earth. It has no light of its own, but it shines because the sun lights it. Also, the moon changes shape in the sky. Thank you.» (goes around = gira alrededor, shines = brilla, shape = forma, sky = cielo). Escribe: el tema, dos datos con palabras clave y la frase de cierre.", "Tema: la luna. Datos: gira alrededor de la Tierra y brilla porque el sol la ilumina. Cierre: Thank you.", ["escribe el tema correcto", "anota dos datos con palabras clave", "copia la frase de cierre"], ["hoja con apuntes", "nota del adulto"], ["copiar oraciones completas", "olvidar la frase de cierre"], "Reconoce lo que anotó bien y muestra cómo reducir una oración a palabras clave y números."),
    "Pide a un adulto que lea la exposición de los pingüinos y levanta la mano cuando oigas el cierre.",
    "Escribe en tu hoja una introducción de una línea para una exposición sobre tu mascota, con la frase «Today I am going to talk about...».",
)

# ---------------------------------------------------------------- clase 5 (artículos informativos, instrucciones, procedimientos)
CAPY = "«The capybara is the largest rodent in the world. It lives near rivers and lakes in South America. It has brown fur and a short tail. It eats grass and plants. Capybaras like to be in the water.» (largest = más grande, rodent = roedor, rivers = ríos, fur = pelaje, tail = cola, grass = pasto)"
BEAN = "«How to grow a bean. First, put some cotton in a small cup. Second, put a bean on the cotton. Third, add two spoons of water. Fourth, place the cup near a window. Add water every day. After about a week, a small plant appears.» (bean = poroto, cotton = algodón, cup = vaso, spoons = cucharadas, window = ventana, appears = aparece)"

lesson(
    OA1, 5,
    "Los textos informativos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a comprender de forma independiente artículos informativos que describen, dan instrucciones o explican un procedimiento. Sirve para seguir pasos y aprender datos sobre el mundo en inglés.",
    ["Sé que una exposición tiene introducción, desarrollo y cierre.", "Conozco first, second y finally."],
    [
        "Un artículo informativo (informative article) entrega datos reales. Hay tres tipos. Una descripción (description) dice cómo es algo: tamaño, color, lugar donde vive o qué come. Unas instrucciones (instructions) dicen qué hacer, en pasos. Un procedimiento (procedure) explica cómo se hace algo y en qué orden.",
        "Las instrucciones usan verbos en forma de orden al comienzo de la oración: put (pon), add (agrega), place (coloca), wash (lava), mix (mezcla). Las palabras de secuencia first, second, third, next, after that y finally ordenan los pasos. Los números te dicen cantidades, como two spoons (dos cucharadas) o about a week (cerca de una semana).",
        "Cuando escuches un artículo informativo, decide primero de qué tipo es: ¿describe un animal, enseña a hacer algo o cuenta una secuencia? Luego anota los datos con palabras clave. Para comprobar que entendiste, vuelve a ordenar los pasos y responde: ¿qué se hace primero? ¿cuántos pasos hay? ¿qué resultado se espera? Si falta un paso, el procedimiento no queda completo.",
    ],
    [("description", "descripción: dice cómo es algo"), ("instructions", "instrucciones: pasos para hacer algo"), ("procedure", "procedimiento: cómo se hace algo en orden"), ("put / add / place", "pon / agrega / coloca"), ("step", "paso"), ("about", "cerca de")],
    [
        ("Reconocer el tipo de texto", ADULT + "«To wash your hands: wet your hands, put soap on them, rub for twenty seconds, rinse with water and dry with a clean towel.» (wet = moja, soap = jabón, rub = frota, rinse = enjuaga, towel = toalla). ¿Es una descripción o instrucciones? ¿Cuántos pasos tiene?", ["Veo verbos de orden: wet, put, rub, rinse, dry.", "Es un texto de instrucciones.", "Cuento los verbos: son cinco pasos."], "Instrucciones; cinco pasos"),
        ("Datos específicos", "En el mismo texto, ¿por cuántos segundos hay que frotar las manos?", ["Busco la palabra rub.", "Dice for twenty seconds.", "Twenty es veinte."], "20 segundos"),
    ],
    [
        ("Pensar que una descripción tiene pasos numerados.", "Se confunde descripción con instrucciones.", "La descripción dice cómo es algo; las instrucciones dicen qué hacer."),
        ("Cambiar el orden de los pasos de un procedimiento.", "No se escuchan las palabras de secuencia.", "Fíjate en first, second, third y finally."),
    ],
    [
        (ADULT + CAPY + " ¿Qué tipo de texto es? a) una descripción de un animal b) unas instrucciones c) un diálogo", "a) una descripción de un animal", "Dice cómo es y qué come el capibara."),
        (ADULT + CAPY + " ¿Dónde vive el capibara? a) cerca de ríos y lagos b) en el desierto", "a) cerca de ríos y lagos", "Dice near rivers and lakes."),
        (ADULT + CAPY + " ¿De qué color es su pelaje? a) café b) blanco c) verde", "a) café", "Dice brown fur."),
    ],
    [
        (ADULT + BEAN + " ¿Qué tipo de texto es? a) un procedimiento con pasos b) una descripción de un animal", "a) un procedimiento con pasos", "Indica cómo hacer crecer un poroto en orden."),
        (ADULT + BEAN + " ¿Qué se pone dentro del vaso primero?", "Algodón", "First, put some cotton in a small cup."),
        (ADULT + BEAN + " ¿Cuántas cucharadas de agua se agregan al inicio?", "2", "Dice two spoons of water."),
    ],
    [
        (ADULT + BEAN + " ¿Cuántos pasos están marcados con first, second, third y fourth?", "4", "Son cuatro palabras de orden."),
        (ADULT + BEAN + " ¿Cuánto tiempo pasa más o menos hasta que aparece una planta pequeña? a) cerca de una semana b) cerca de un año", "a) cerca de una semana", "Dice after about a week."),
        (ADULT + BEAN + " Si se salta el paso third, ¿qué le falta al poroto? a) el agua b) la ventana", "a) el agua", "El paso third es add two spoons of water."),
    ],
    [
        (ADULT + CAPY + " Un compañero dice que el capibara come carne. ¿Qué dice el texto que come?", "Pasto y plantas", "Dice it eats grass and plants."),
        ("Ordena el procedimiento de una receta. A) Mezcla la masa. B) Hornea (con ayuda de un adulto). C) Agrega huevos y harina.", "C, A, B", "Primero se agregan los ingredientes, luego se mezcla y al final se hornea."),
    ],
    [
        (ADULT + "«How to make a paper plane. Take a sheet of paper. Fold it in half. Open it. Fold the top corners to the middle. Fold both sides again. Your paper plane is ready.» (sheet = hoja, fold = doblar, plane = avión, corners = esquinas, sides = lados). ¿Cuántas veces dice fold el texto?", "3", "Aparece en Fold it in half, Fold the top corners y Fold both sides."),
        ("En el procedimiento del avión de papel, ¿cuál es el resultado final?", "Un avión de papel listo", "La última oración dice Your paper plane is ready."),
    ],
    [(ADULT + "En el laboratorio de Ciencias, un profesor dice: «To measure a plant, put a ruler next to it. Read the number at the top. Write it in your notebook.» (ruler = regla, measure = medir, notebook = cuaderno). ¿Qué hay que hacer después de leer el número?", "Escribirlo en el cuaderno", "El último paso es write it in your notebook.")],
    [
        ("¿Qué tipo de texto da pasos para hacer algo?", "Instrucciones", "Instructions indican qué hacer en orden."),
        ("¿Qué significa «add»?", "Agregar", "Add es poner algo más."),
        ("¿Qué palabras ordenan los pasos de un procedimiento?", "first, second, third y finally", "Son palabras de secuencia."),
    ],
    task("Un adulto lee dos veces este texto: «How to make lemonade. First, squeeze two lemons into a jug. Second, add a spoon of sugar. Third, add a glass of water. Finally, stir and add ice.» (lemonade = limonada, squeeze = exprimir, jug = jarra, sugar = azúcar, stir = revolver, ice = hielo). En tu hoja dibuja los cuatro pasos y escribe bajo cada uno una palabra clave en español. Indica además qué tipo de texto es.", "Es un procedimiento. Paso 1: limones. Paso 2: azúcar. Paso 3: agua. Paso 4: hielo.", ["dice que es un procedimiento o instrucciones", "dibuja y anota cuatro pasos en orden", "usa palabras clave correctas"], ["hoja con dibujos y palabras", "nota del adulto"], ["cambiar el orden de los pasos", "olvidar el hielo del último paso"], "Reconoce lo que ordenó bien y repasa con la persona qué hace cada palabra de secuencia."),
    "Pide a un adulto que lea el procedimiento del poroto y toca la mesa una vez por cada paso.",
    "Escribe en español los pasos para hacer una tostada, usando las palabras first, second y finally en inglés.",
)

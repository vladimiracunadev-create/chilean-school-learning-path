"""Student material for 5.º básico Inglés (propuesta), EN05 OA 01 y OA 02 (comprensión auditiva).

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Todos los textos son originales. Cada palabra o estructura en inglés se explica antes de usarla o lleva su pista en español.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1 = "EN05 OA 01"
OA2 = "EN05 OA 02"
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


POEM_RAIN = "«Grey clouds come, the rain falls down. It paints with water all the town. Puddles here and puddles there. I wear my boots and splash with care.» (clouds = nubes, falls down = cae, town = ciudad, puddles = charcos, boots = botas, splash = chapotear, with care = con cuidado)"
SONG_SEA = "«Verse 1: The sand is warm, the sky is bright. We hold our hats, we hold them tight. Chorus: Walk, walk, walk to the sea! The sea is calling you and me. Verse 2: The waves are cold, they touch my toes. I laugh out loud, and everyone knows. Chorus: Walk, walk, walk to the sea! The sea is calling you and me.» (sand = arena, bright = brillante, hold = sostener, tight = fuerte, waves = olas, laugh out loud = reír fuerte, everyone knows = todos lo saben)"
STORY_DUCK = "«One sunny morning, Leo sees a little duck near the lake. The duck is alone. It cannot find its mother. Leo walks along the lake with the duck. Behind some tall grass, they see a big duck. The little duck runs to the big duck. Leo smiles and goes home.» (duck = pato, lake = lago, alone = solo, mother = mamá, tall grass = pasto alto, smiles = sonríe)"
DIALOGUE_NOTE = "«Ana: Hi, Tom! What are you doing? Tom: I'm looking for my notebook. Ana: What color is it? Tom: It's green. Ana: I see a green notebook on the chair. Tom: Thanks, Ana! It's mine.» (looking for = buscando, notebook = cuaderno, chair = silla, mine = mío)"
TALK_DOG = "«Hello, I'm Camila. This is my dog, Rocky. He is brown and white. He has big ears and a short tail. He likes to play with a ball. He sleeps in a basket near my bed.» (ears = orejas, tail = cola, basket = canasto, bed = cama)"
STEPS_SALAD = "«How to make a fruit salad. First, wash the apple and the grapes. Next, ask an adult to cut the apple. Then put the pieces in a bowl. After that, add the grapes. Finally, mix with a spoon.» (wash = lavar, grapes = uvas, cut = cortar, pieces = trozos, bowl = bol, add = agregar, mix = mezclar, spoon = cuchara)"

# ================================================================ OA 01
lesson(
    OA1, 1,
    "Los poemas y canciones escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a entender la idea principal de un poema o una canción y a reconocer sus rimas y su coro. Sirve para disfrutar y comprender poemas y canciones en inglés.",
    ["Sé que dos palabras riman si terminan con el mismo sonido.", "Conozco palabras como rain, sea, sand y town."],
    [
        "Un poema (poem) y una canción (song) se organizan en líneas (lines). Un grupo de líneas es una estrofa (verse). En una canción, el coro (chorus) es la parte que se repite después de cada estrofa. Escucharlo te ayuda a encontrar lo más importante.",
        "Para entender un poema o una canción, hazte tres preguntas: ¿de qué habla? (la idea principal, main idea), ¿qué palabras riman? y ¿qué siente quien habla? Palabras como happy (feliz), glad (contento) o sad (triste) dan pistas sobre el sentimiento. No necesitas entender todas las palabras.",
        "Fíjate también en las palabras que se repiten, porque suelen ser importantes. En el poema de la lluvia se repite puddles y todas las palabras hablan de agua. Escucha dos veces: la primera vez para la idea general y la segunda para los detalles.",
    ],
    [("poem / song", "poema / canción"), ("verse", "estrofa"), ("chorus", "coro: parte que se repite"), ("main idea", "idea principal"), ("glad", "contento"), ("puddle", "charco")],
    [
        ("Encontrar la idea principal", ADULT + POEM_RAIN + " ¿De qué habla el poema?", ["Escucho rain, puddles y boots.", "Esas palabras hablan de agua y de salir a jugar.", "La idea principal es un día de lluvia."], "De un día de lluvia"),
        ("Encontrar una rima", "En el mismo poema, ¿qué palabra rima con there?", ["Miro el final de cada línea: down, town, there, care.", "There y care terminan con el mismo sonido.", "Down rima con town, no con there."], "care"),
    ],
    [
        ("Querer traducir cada palabra del poema y perder el hilo.", "Se detiene la escucha en una palabra y no se sigue el sentido.", "Busca las palabras clave y las que se repiten; con ellas sale la idea principal."),
        ("Pensar que el coro cambia en cada estrofa.", "No se nota que el coro es la parte que se repite.", "Escucha: el coro dice lo mismo después de cada estrofa."),
    ],
    [
        (ADULT + POEM_RAIN + " ¿Qué clima describe el poema? a) lluvia b) nieve c) calor", "a) lluvia", "Rain falls down y puddles hablan de lluvia."),
        (ADULT + POEM_RAIN + " ¿Qué palabra rima con down? a) care b) town c) boots", "b) town", "Down y town terminan con el mismo sonido."),
        (ADULT + SONG_SEA + " El coro es la parte que se repite. ¿Qué línea se repite después de cada estrofa? a) The sand is warm, the sky is bright. b) Walk, walk, walk to the sea!", "b) Walk, walk, walk to the sea!", "Esa línea aparece dos veces, una después de cada estrofa."),
    ],
    [
        (ADULT + POEM_RAIN + " ¿Cuál es la idea principal? a) Alguien juega con cuidado entre los charcos de un día de lluvia. b) Alguien duerme en la ciudad. c) Alguien compra botas.", "a)", "Rain, puddles, boots y splash cuentan un día de lluvia."),
        (ADULT + SONG_SEA + " ¿Dónde están las personas de la canción? a) En la playa b) En un bosque", "a) En la playa", "Se oyen sand, waves y sea."),
        (ADULT + SONG_SEA + " En la estrofa 2 dice «I laugh out loud». ¿Cómo se siente la persona? a) contenta b) triste", "a) contenta", "Laugh out loud es reír fuerte, y eso muestra alegría."),
    ],
    [
        ("Lee: «The sand is warm, the sky is bright. We hold our hats, we hold them tight.» ¿Qué palabra rima con bright?", "tight", "Bright y tight terminan en el mismo sonido «ait»."),
        ("Lee la canción del mar: " + SONG_SEA + " Si el coro se canta después de cada una de las dos estrofas, ¿cuántas veces se canta «Walk, walk, walk to the sea!»?", "2", "Hay dos coros y cada uno trae esa línea una vez."),
        ("Lee: «Puddles here and puddles there.» ¿Cuántas veces aparece la palabra puddles en esa línea?", "2", "Puddles aparece una vez antes de here y otra antes de there."),
    ],
    [
        (ADULT + POEM_RAIN + " ¿Qué palabras muestran que el poema habla de lluvia? a) rain y puddles b) paints y town", "a) rain y puddles", "Rain es lluvia y puddles son charcos de agua de lluvia."),
        ("Un compañero se detiene en cada palabra del coro y no entiende la canción. ¿Qué estrategia es mejor? a) Buscar la idea principal y las palabras repetidas b) Parar en cada palabra", "a)", "Las palabras repetidas y la idea general dan el sentido sin traducir todo."),
    ],
    [
        ("Lee: «Hot sun, blue sea, a big green tree. I eat a pear, I sit on a chair.» (pear = pera, chair = silla). ¿Cuántos pares de palabras que riman tiene?", "2", "Sea rima con tree y pear rima con chair."),
        ("En el mismo poema, ordena lo que se nombra: A) pear B) sea C) chair.", "B, A, C", "El poema nombra primero sea, luego pear y al final chair."),
    ],
    [(ADULT + "Una canción de cuna dice: «Sleep, little moon, sleep, little star. The night is calm, the night is far.» (sleep = dormir, calm = tranquila, far = lejos). ¿Qué palabras riman? a) star y far b) moon y sleep", "a) star y far", "Star y far terminan con el mismo sonido «ar».")],
    [
        ("¿Qué es el coro (chorus) de una canción?", "La parte que se repite después de cada estrofa", "El coro vuelve a aparecer varias veces."),
        ("Para entender un poema, ¿qué buscas primero?", "La idea general", "Primero se capta de qué habla y después los detalles."),
        ("¿Riman sea y tree?", "Sí", "Las dos terminan con el sonido «i»."),
    ],
    task("Un adulto lee dos veces este poema: «Warm sun, warm sand. I hold a shell in my hand. Blue sea, blue sky. A white gull flies by.» (warm = tibio, shell = concha, hand = mano, gull = gaviota, flies by = pasa volando). En tu hoja escribe una frase en español sobre de qué habla, los dos pares de palabras que riman y las dos palabras que se repiten. Después dibuja la escena.", "Habla de un día en la playa. Riman sand-hand y sky-by. Se repiten warm y blue.", ["escribe la idea principal", "anota los dos pares que riman", "anota las dos palabras repetidas"], ["hoja con respuestas y dibujo", "nota del adulto"], ["decir que riman sun y sand", "no anotar las palabras repetidas"], "Reconoce lo bien hecho y vuelve a leer con él solo los finales de cada línea."),
    "Pide a un adulto que lea el poema de la lluvia y levanta la mano cada vez que oigas puddles.",
    "Escribe dos líneas que rimen sobre tu día favorito, por ejemplo con day y play.",
)

lesson(
    OA1, 2,
    "Los cuentos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a entender un cuento corto: quién es el personaje, dónde y cuándo pasa y qué ocurre al comienzo, en el medio y al final. Sirve para seguir y contar historias en inglés.",
    ["Sé que first, next y finally ordenan una historia.", "Conozco palabras como lake, duck, mother y morning."],
    [
        "Un cuento (story) tiene personajes (characters), que son quienes actúan. Tiene también un lugar (place) y un momento (time). En el cuento de hoy el personaje es Leo, el lugar es un lago (lake) y el momento es una mañana de sol (sunny morning).",
        "La trama (plot) es lo que pasa y tiene tres partes. Al comienzo (beginning) aparece el problema: un patito está solo. En el medio (middle) los personajes hacen algo para resolverlo. Al final (end) el problema se resuelve o cambia. Pregúntate: ¿qué pasó primero, después y al final?",
        "Para responder preguntas de un cuento, usa las palabras who (¿quién?), where (¿dónde?), when (¿cuándo?) y what (¿qué?). Mientras escuchas, ten lista cada pregunta. Si una palabra no se entiende, sigue escuchando: casi siempre la próxima línea da una pista.",
    ],
    [("character", "personaje"), ("place", "lugar"), ("beginning / middle / end", "comienzo / medio / final"), ("plot", "trama"), ("who / where / when / what", "quién / dónde / cuándo / qué"), ("duck", "pato")],
    [
        ("Personaje y lugar", ADULT + STORY_DUCK + " ¿Quién es el personaje que ayuda y dónde está?", ["Pregunto who: Leo ve al patito y camina con él.", "Pregunto where: near the lake.", "Leo ayuda y está cerca del lago."], "Leo, cerca de un lago"),
        ("Partes de la trama", "En el mismo cuento, ¿cuál es el problema del comienzo?", ["Busco la parte inicial.", "Dice: the duck is alone, it cannot find its mother.", "El problema es que el patito no encuentra a su mamá."], "El patito está solo y no encuentra a su mamá"),
    ],
    [
        ("Decir que el cuento pasa en la noche porque se oye «lake».", "Se confunden el lugar y el momento.", "El momento lo da la frase one sunny morning: una mañana de sol."),
        ("Contar el final como si fuera el comienzo.", "No se ordena por la secuencia de la trama.", "El final es lo último que pasa: Leo sonríe y se va a casa."),
    ],
    [
        (ADULT + STORY_DUCK + " ¿Cuándo pasa el cuento? a) en una mañana de sol b) en una noche de lluvia", "a)", "Dice one sunny morning."),
        (ADULT + STORY_DUCK + " ¿Qué ve Leo cerca del lago? a) un patito b) un perro", "a) un patito", "Leo sees a little duck near the lake."),
        (ADULT + STORY_DUCK + " ¿Qué hace Leo al final? a) se va a su casa b) nada en el lago", "a) se va a su casa", "El cuento termina con Leo smiles and goes home."),
    ],
    [
        (ADULT + STORY_DUCK + " ¿Qué hace el patito cuando ve al pato grande? a) corre hacia él b) se esconde", "a) corre hacia él", "Dice the little duck runs to the big duck."),
        (ADULT + STORY_DUCK + " ¿Cuántos patos aparecen en el cuento?", "2", "Hay un patito y un pato grande."),
        (ADULT + STORY_DUCK + " ¿Por qué el patito está alone? a) No encuentra a su mamá b) No quiere jugar", "a)", "El cuento dice it cannot find its mother."),
    ],
    [
        ("Lee: «Mia has a red kite. The wind is strong and the kite flies high. Suddenly, the string breaks. The kite lands in a tree. Mia asks her friend for help, and he gets the kite down.» (kite = volantín, wind = viento, string = hilo, breaks = se corta, lands = cae, gets down = baja). ¿Cuál es el problema del cuento?", "El hilo se rompe y el volantín queda en un árbol", "El problema aparece cuando the string breaks y the kite lands in a tree."),
        ("En el cuento del volantín, ¿cómo se resuelve el problema?", "Un amigo baja el volantín", "El final dice that her friend gets the kite down."),
        ("En el cuento del volantín, ¿cuál es el personaje principal?", "Mia", "Mia es quien tiene el volantín y pide ayuda."),
    ],
    [
        ("Un compañero dice: «El cuento del patito pasa en una casa porque Leo se va a casa». ¿Dónde pasa casi todo el cuento?", "Cerca del lago", "Leo se va a casa solo al final; el resto ocurre cerca del lago."),
        ("En el cuento del volantín, ¿qué pasa en el medio: a) el hilo se corta o b) Mia compra un volantín?", "a) el hilo se corta", "Suddenly the string breaks es el momento del problema."),
    ],
    [
        ("Ordena los hechos del cuento del volantín: A) Un amigo baja el volantín. B) El volantín cae en un árbol. C) Mia tiene un volantín rojo.", "C, B, A", "Primero Mia tiene el volantín, luego cae en el árbol y al final lo bajan."),
        ("En el cuento del volantín y el del patito hay un final feliz. ¿Qué personaje ayuda en el cuento del patito?", "Leo", "Leo camina con el patito hasta el pato grande."),
    ],
    [(ADULT + "Un niño cuenta: «Yesterday, at school, Pedro lost his hat in the yard. He looked under a bench and found it.» (lost = perdió, yard = patio, bench = banca, found = encontró). ¿Dónde pasó la historia? a) en el patio del colegio b) en un lago", "a)", "Dice at school, in the yard.")],
    [
        ("¿Qué significa «lake»?", "Lago", "Lake es una masa de agua rodeada de tierra."),
        ("¿Qué es el problema de un cuento: lo que pasa al comienzo o lo que pasa al final?", "Lo que pasa al comienzo", "El problema aparece al comienzo y se resuelve después."),
        ("¿Qué pregunta usas para saber el lugar: who o where?", "where", "Where significa dónde."),
    ],
    task("Un adulto lee dos veces este cuento: «One cold evening, Rita finds a small cat near her door. The cat is hungry. Rita gives it a bowl of milk. The cat drinks and purrs. Rita smiles.» (finds = encuentra, hungry = hambriento, gives = da, milk = leche, purrs = ronronea). Dibuja tres cuadros: comienzo, medio y final, y escribe una frase en español bajo cada uno.", "Comienzo: Rita encuentra un gatito. Medio: le da leche. Final: el gato ronronea y ella sonríe.", ["tres cuadros en orden", "frase correcta bajo cada uno", "menciona a Rita y al gato"], ["dibujos con frases", "nota del adulto"], ["poner el final primero", "cambiar a Rita por otro personaje"], "Reconoce el orden logrado y repite con él cada parte con las palabras first, next y finally."),
    "Pide a un adulto que lea de nuevo el cuento del patito y levanta un dedo cuando oigas el lugar y dos dedos cuando oigas el momento.",
    "Escribe tres frases en español sobre el cuento del volantín: comienzo, medio y final.",
)

lesson(
    OA1, 3,
    "Los diálogos escritos en cada ejercicio, que lee un adulto con voces distintas; una hoja para tapar el guion y lápiz.",
    "Aprenderé a seguir un diálogo: quién habla, qué pregunta y qué responde. Sirve para entender conversaciones cortas en inglés.",
    ["Sé que en un diálogo se habla por turnos.", "Conozco What color is it? y It's green."],
    [
        "Un diálogo (dialogue) es una conversación entre dos o más personas. Cada persona es un speaker. Para saber quién habla, mira el nombre antes de los dos puntos, por ejemplo «Ana:». Cada cambio de nombre es un turno nuevo.",
        "Una pregunta (question) casi siempre la responde otro speaker. What are you doing? significa «¿qué estás haciendo?». I'm looking for... significa «estoy buscando...». What color is it? significa «¿de qué color es?». It's mine significa «es mío». Estas frases son muy comunes en conversaciones.",
        "Para entender un diálogo, escucha tres cosas: quién habla, qué pide o pregunta y qué se responde. Después comprueba si el problema se resolvió. Cuenta solo los nombres distintos para saber cuántas personas hablan; una misma persona puede hablar varias veces.",
    ],
    [("dialogue", "conversación"), ("speaker", "persona que habla"), ("question / answer", "pregunta / respuesta"), ("looking for", "buscando"), ("mine", "mío"), ("What are you doing?", "¿qué estás haciendo?")],
    [
        ("Quién dice qué", ADULT + DIALOGUE_NOTE + " ¿Quién dice «I'm looking for my notebook»?", ["Busco la frase I'm looking for.", "Antes de ella está el nombre Tom.", "Tom busca su cuaderno."], "Tom"),
        ("Pregunta y respuesta", "En el mismo diálogo, ¿qué responde Tom cuando Ana le pregunta «What color is it?»?", ["Busco la pregunta de Ana.", "La siguiente línea es de Tom.", "Tom dice: It's green."], "It's green: es verde"),
    ],
    [
        ("Contar cuatro speakers porque hay seis turnos.", "Se cuentan turnos y no personas distintas.", "Cuenta solo los nombres distintos: en el diálogo hay dos."),
        ("Pensar que Ana busca el cuaderno porque dice «I see».", "Se confunde quien busca con quien ayuda.", "Ana ayuda: ve el cuaderno. Tom es quien busca."),
    ],
    [
        (ADULT + DIALOGUE_NOTE + " ¿Qué busca Tom? a) su cuaderno b) su chaqueta", "a) su cuaderno", "Dice I'm looking for my notebook."),
        (ADULT + DIALOGUE_NOTE + " ¿De qué color es lo que busca Tom?", "Verde", "Tom responde It's green."),
        (ADULT + DIALOGUE_NOTE + " ¿Quién ve el cuaderno? a) Ana b) Tom", "a) Ana", "Ana dice I see a green notebook on the chair."),
    ],
    [
        (ADULT + DIALOGUE_NOTE + " ¿Cuántas personas hablan en el diálogo?", "2", "Solo hablan Ana y Tom."),
        (ADULT + DIALOGUE_NOTE + " ¿Dónde está el cuaderno? a) en la silla b) en la mochila", "a) en la silla", "Ana dice on the chair."),
        (ADULT + DIALOGUE_NOTE + " ¿Qué dice Tom al final para agradecer? a) Thanks, Ana! b) What color is it?", "a) Thanks, Ana!", "Thanks es gracias y cierra el diálogo."),
    ],
    [
        ("Lee: «Eva: Excuse me, how much is the red pen? Seller: It's three hundred pesos. Eva: Okay, I want one, please.» (how much = cuánto cuesta, seller = vendedor, want = quiero). ¿Cuántos speakers hablan?", "2", "Hablan Eva y Seller."),
        ("En el diálogo de Eva, ¿qué quiere comprar Eva? a) un lápiz rojo (red pen = lápiz de pasta rojo) b) un cuaderno azul", "a) un lápiz rojo", "Eva dice I want one, refiriéndose al red pen."),
        ("En el diálogo de Eva, ¿quién pregunta «how much is the red pen»? a) Eva b) Seller", "a) Eva", "El nombre Eva está antes de esa pregunta."),
    ],
    [
        ("Una compañera dice que en el diálogo de Eva el problema se resuelve porque Eva compra el lápiz. ¿Qué frase lo muestra?", "I want one, please", "Eva dice que quiere comprarlo."),
        ("En el diálogo de Ana y Tom, ¿cómo sabes que el problema se resolvió? a) Tom dice «It's mine» y agradece b) Ana sigue buscando", "a)", "Tom reconoce el cuaderno y da las gracias."),
    ],
    [
        ("Ordena los turnos del diálogo de Ana y Tom: A) Tom dice «It's green». B) Ana dice «Hi, Tom! What are you doing?» C) Ana ve el cuaderno en la silla.", "B, A, C", "Primero saluda y pregunta, luego Tom responde y después Ana lo ve."),
        ("En un diálogo, Mateo dice «I'm looking for my hat. It's blue.» y Sofía dice «Is it on the table?» (table = mesa). ¿Qué pregunta Sofía?", "Si el sombrero está en la mesa", "Is it on the table? pregunta por la mesa."),
    ],
    [(ADULT + "Dos amigos conversan en el recreo. «Leo: What are you doing, Nico? Nico: I'm drawing a car. Leo: It's nice!» (drawing = dibujando, nice = lindo). ¿Qué hace Nico?", "Dibuja un auto", "Nico dice I'm drawing a car.")],
    [
        ("¿Qué significa «What are you doing?»", "¿Qué estás haciendo?", "La frase pregunta por lo que alguien hace ahora."),
        ("¿Cómo sabes quién habla en un diálogo escrito?", "Mirando el nombre antes de los dos puntos", "Cada nombre indica el turno de esa persona."),
        ("¿Qué significa «It's mine»?", "Es mío", "Mine indica que algo me pertenece."),
    ],
    task("Un adulto lee dos veces este diálogo: «Rosa: Hello, Pablo! Where is your bag? Pablo: It's under my desk. Rosa: Is it blue? Pablo: Yes, it is.» (bag = mochila, under = debajo de, desk = escritorio). Escribe: quién pregunta por la mochila, dónde está la mochila y de qué color es.", "Rosa pregunta; está debajo del escritorio; es azul.", ["nombra a Rosa", "dice debajo del escritorio", "dice azul"], ["hoja con respuestas", "nota del adulto"], ["decir que Pablo pregunta", "no mencionar el color"], "Aplaude lo logrado y repite con él quién dice cada frase."),
    "Pide a un adulto que lea el diálogo de Ana y Tom con dos voces y señala con el dedo al speaker que habla.",
    "Escribe un diálogo de cuatro líneas entre dos amigos que buscan un lápiz.",
)

lesson(
    OA1, 4,
    "Las exposiciones e instrucciones escritas en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a entender una exposición oral y unas instrucciones: de qué habla quien expone, qué datos da y cuáles son los pasos. Sirve para aprender información en inglés.",
    ["Sé que first, next, then, after that y finally ordenan pasos.", "Conozco palabras de descripción como big, short y brown."],
    [
        "Una exposición (talk) es un texto oral en que una persona presenta información. Puede describir (describe) a una persona, un animal o un lugar. Para entenderla, busca primero el tema: ¿sobre qué habla? Después anota los datos que oyes: color, tamaño, lo que le gusta.",
        "Unas instrucciones (instructions) explican cómo hacer algo paso a paso (step by step). Usan verbos de orden como wash (lavar), cut (cortar), put (poner), add (agregar) y mix (mezclar), con las palabras first, next, then, after that y finally. El orden de los pasos importa.",
        "Una receta es un buen ejemplo de instrucciones. Para entenderlas, cuenta los pasos y repítelos en orden con tus palabras. Para entender una descripción, escribe el tema y dos o tres datos. En ambos casos escuchar dos veces ayuda mucho.",
    ],
    [("talk", "exposición oral"), ("describe", "describir"), ("instructions", "instrucciones"), ("step", "paso"), ("wash / cut / add / mix", "lavar / cortar / agregar / mezclar"), ("bowl", "bol")],
    [
        ("Tema y datos", ADULT + TALK_DOG + " ¿De qué habla Camila y de qué color es Rocky?", ["Escucho This is my dog: el tema es su perro.", "Busco el color: brown and white.", "Rocky es café y blanco."], "De su perro; es café y blanco"),
        ("Contar pasos", ADULT + STEPS_SALAD + " ¿Cuántos pasos tiene la receta?", ["Busco las palabras de orden: first, next, then, after that, finally.", "Cada una inicia un paso.", "Son cinco palabras de orden."], "5"),
    ],
    [
        ("Mezclar los pasos y poner mix antes de wash.", "No se respeta el orden de las instrucciones.", "Usa las palabras de orden: first es el primer paso y finally es el último."),
        ("Responder con un dato de otro tema (por ejemplo, el nombre de la niña cuando se pregunta por el perro).", "Se pierde el tema de la exposición.", "Primero identifica el tema y luego busca el dato que piden."),
    ],
    [
        (ADULT + TALK_DOG + " ¿Cómo se llama el perro? a) Rocky b) Camila", "a) Rocky", "Camila dice This is my dog, Rocky."),
        (ADULT + TALK_DOG + " ¿Dónde duerme el perro? a) en un canasto cerca de la cama b) en el patio", "a)", "Dice he sleeps in a basket near my bed."),
        (ADULT + STEPS_SALAD + " ¿Qué se hace primero? a) lavar la manzana y las uvas b) mezclar con la cuchara", "a)", "First, wash the apple and the grapes."),
    ],
    [
        (ADULT + STEPS_SALAD + " ¿Qué se hace justo después de poner los trozos en el bol? a) agregar las uvas b) lavar las uvas", "a) agregar las uvas", "After that, add the grapes."),
        (ADULT + STEPS_SALAD + " ¿Quién corta la manzana? a) un adulto b) el niño", "a) un adulto", "Dice ask an adult to cut the apple."),
        (ADULT + TALK_DOG + " ¿Con qué le gusta jugar a Rocky? a) con una pelota b) con un hueso", "a) con una pelota", "Camila dice he likes to play with a ball."),
    ],
    [
        ("Lee: «This is my school. It is big and yellow. It has a library and a playground. I like the playground.» (library = biblioteca, playground = patio de juegos). ¿Cuál es el tema? a) el colegio b) una receta", "a) el colegio", "Todo el texto describe my school."),
        ("En la exposición del colegio, ¿qué le gusta al hablante? a) el patio de juegos b) la biblioteca", "a) el patio de juegos", "Dice I like the playground."),
        ("En la exposición del colegio, ¿de qué color es? a) amarillo b) rojo", "a) amarillo", "Dice big and yellow."),
    ],
    [
        ("Un compañero ordena los pasos así: mezclar, lavar, cortar. ¿Qué paso está mal puesto: «mezclar» al comienzo o «lavar» al comienzo?", "Mezclar al comienzo", "La receta empieza con lavar la fruta."),
        ("En la exposición del colegio, ¿cuántos lugares del colegio se nombran: library y playground?", "2", "Se nombran una biblioteca y un patio de juegos."),
    ],
    [
        ("Ordena los pasos de la receta: A) agregar las uvas B) lavar la fruta C) mezclar con la cuchara D) poner los trozos en el bol.", "B, D, A, C", "Primero se lava, luego se ponen los trozos, después las uvas y al final se mezcla."),
        arith("La receta de ensalada tiene 5 pasos y las instrucciones para un avión de papel tienen 4 pasos. ¿Cuántos pasos hay en total entre las dos?", "5+4", "Se suman los pasos de las dos instrucciones."),
    ],
    [(ADULT + "En clase, una niña dice: «First, take a paper. Next, fold it in half. Then draw a face on it.» (take = toma, fold = dobla, in half = por la mitad, face = cara). ¿Qué se hace después de doblar el papel?", "Dibujar una cara", "Then draw a face viene después de fold it.")],
    [
        ("¿Qué significa «step by step»?", "Paso a paso", "Indica hacer algo en orden, un paso después de otro."),
        ("¿Qué haces primero al escuchar una exposición: buscar el tema o buscar una palabra difícil?", "Buscar el tema", "El tema orienta todo lo que sigue."),
        ("¿Qué significa «mix»?", "Mezclar", "Mix es juntar cosas revolviendo."),
    ],
    task("Un adulto lee dos veces estas instrucciones: «How to make a paper plane. First, take a paper. Next, fold it in half. Then fold the two corners. Finally, fold the wings.» (plane = avión, corner = esquina, wings = alas). Escribe en español los cuatro pasos en el mismo orden y dibuja cada uno.", "1 tomar un papel, 2 doblarlo por la mitad, 3 doblar las dos esquinas, 4 doblar las alas.", ["cuatro pasos", "mismo orden que el texto", "cada paso tiene su dibujo"], ["hoja con pasos y dibujos", "nota del adulto"], ["cambiar el orden de los pasos", "olvidar un paso"], "Reconoce el orden correcto y repite con él las palabras first, next, then y finally."),
    "Pide a un adulto que lea la receta de ensalada y haz un gesto distinto para cada paso.",
    "Escribe en español dos datos que recuerdes de la exposición de Camila sobre Rocky.",
)

# ================================================================ OA 02
lesson(
    OA2, 1,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a distinguir la idea general de un texto oral de sus datos específicos. Sirve para entender de qué habla un mensaje y encontrar el dato que necesito.",
    ["Sé que un texto oral puede hablar de lugares, personas y objetos.", "Conozco palabras como library, books, week y open."],
    [
        "La idea general (main idea) es lo más importante de un texto: de qué habla en total. La información específica (specific information) son los datos pequeños: números, horas, nombres, lugares. Primero se escucha la idea general y después se buscan los datos que se piden.",
        "Un buen método es escuchar dos veces. La primera vez, solo pregúntate: ¿de qué habla? La segunda vez, escucha el dato que te piden: how many (cuántos), what time (a qué hora), where (dónde), who (quién). No anotes todo; anota solo el dato pedido.",
        "En el texto de la biblioteca, la idea general es que la biblioteca de la escuela es un lugar tranquilo con libros. Los datos son cosas como cuántos libros puedes llevar o a qué hora cierra. Si dos datos se parecen, como la hora de apertura y la de cierre, confirma con la palabra que los acompaña (opens, closes).",
    ],
    [("main idea", "idea general"), ("specific information", "información específica"), ("how many", "cuántos"), ("what time", "a qué hora"), ("borrow", "pedir prestado"), ("opens / closes", "abre / cierra")],
    [
        ("Idea general", ADULT + "«Our school library is a quiet place. It has many books about animals, space and sports. You can borrow two books for one week. The library opens at eight in the morning and closes at four in the afternoon.» (quiet = silencioso, space = espacio, borrow = pedir prestado). ¿Cuál es la idea general?", ["Escucho library, books y quiet.", "Todo habla de la biblioteca.", "La idea general es cómo es la biblioteca."], "La biblioteca de la escuela y sus libros"),
        ("Dato específico", "En el mismo texto, ¿cuántos libros puedes llevar?", ["Busco la palabra borrow.", "Dice two books for one week.", "El número es dos."], "2"),
    ],
    [
        ("Anotar la hora de cierre cuando se pregunta la de apertura.", "Se confunden dos datos parecidos.", "Busca la palabra clave: opens es abre y closes es cierra."),
        ("Contestar «habla de libros» cuando preguntan cuántos libros.", "Se responde con la idea general en vez del dato.", "Si preguntan cuántos, busca un número."),
    ],
    [
        (ADULT + "«Our school library is a quiet place. It has many books about animals, space and sports. You can borrow two books for one week. The library opens at eight in the morning and closes at four in the afternoon.» ¿Por cuánto tiempo puedes llevar los libros?", "Una semana", "Dice for one week."),
        (ADULT + "«Our school library is a quiet place. It has many books about animals, space and sports. You can borrow two books for one week. The library opens at eight in the morning and closes at four in the afternoon.» ¿A qué hora abre?", "A las ocho de la mañana", "Dice opens at eight in the morning."),
        ("¿Qué es la idea general de un texto?", "De qué habla en total", "Los datos pequeños son información específica."),
    ],
    [
        (ADULT + "«Mr. Díaz is a baker. He works in a small shop. He makes bread every morning. He sells ten loaves before lunch.» (baker = panadero, shop = tienda, loaves = panes). ¿Cuál es la idea general? a) el trabajo del señor Díaz b) un almuerzo", "a)", "El texto describe su trabajo de panadero."),
        (ADULT + "«Mr. Díaz is a baker. He works in a small shop. He makes bread every morning. He sells ten loaves before lunch.» ¿Cuántos panes vende antes del almuerzo?", "10", "Dice ten loaves."),
        (ADULT + "«Mr. Díaz is a baker. He works in a small shop. He makes bread every morning. He sells ten loaves before lunch.» ¿Dónde trabaja?", "En una tienda pequeña", "Dice in a small shop."),
    ],
    [
        ("Lee: «The library closes at four.» y «The library opens at eight.» ¿Qué dato responde «¿a qué hora cierra?»?", "Las cuatro", "Closes es cierra."),
        arith("La biblioteca abre a las 8 de la mañana y cierra a las 4 de la tarde, que son las 16 horas. ¿Cuántas horas está abierta?", "16-8", "Se resta la hora de apertura a la de cierre."),
        ("Lee: «You can borrow two books for one week.» ¿Qué dato responde «how many»: two o week?", "two", "Two es la cantidad de libros."),
    ],
    [
        ("Una compañera escuchó el texto de la biblioteca y dijo que trata de comida. ¿Dijo la idea general o un detalle equivocado?", "Un error: la idea general es la biblioteca", "El texto habla de libros y de la biblioteca."),
        ("En el texto del panadero, ¿«ten loaves» es idea general o información específica?", "Información específica", "Es un dato con número."),
    ],
    [
        (ADULT + "«On Saturday, the Rojas family goes to the beach. They leave at nine and come back at six. They bring water, hats and sandwiches.» (beach = playa, bring = llevan). ¿Cuáles son números? a) nine y six b) beach y hats", "a) nine y six", "Nine y six son números; beach y hats son un lugar y unos objetos."),
        ("En el texto de la playa, ¿cuántas horas pasan fuera si salen a las 9 de la mañana y vuelven a las 6 de la tarde, que son las 18 horas?", "9", "De 9 a 18 hay 9 horas."),
    ],
    [(ADULT + "En el colegio dicen por altavoz: «Class 5A, please go to the gym at ten o'clock.» (gym = gimnasio). ¿Dónde debe ir la clase? a) al gimnasio b) a la biblioteca", "a) al gimnasio", "El mensaje dice go to the gym.")],
    [
        ("¿Qué significa «how many»?", "Cuántos", "Se usa para preguntar por una cantidad."),
        ("¿Qué escuchas primero: la idea general o los datos?", "La idea general", "Luego se buscan los datos."),
        ("¿Qué significa «closes»?", "Cierra", "Closes marca el final del horario."),
    ],
    task("Un adulto lee dos veces este texto: «My cousin Nora plays football. She trains on Tuesday and Thursday at five o'clock. Her team has twelve players. Their color is red.» (cousin = prima, trains = entrena, team = equipo, players = jugadoras). Escribe la idea general en una frase y tres datos: qué días, a qué hora y cuántas jugadoras.", "Idea general: Nora juega fútbol. Datos: martes y jueves, a las cinco, doce jugadoras.", ["idea general correcta", "días correctos", "hora y cantidad correctas"], ["hoja con respuestas", "nota del adulto"], ["confundir el color con la cantidad", "escribir un solo día"], "Reconoce los datos correctos y repite con él el texto, parando en cada número."),
    "Pide a un adulto que lea el texto de la biblioteca y levanta la mano cuando oigas un número.",
    "Escribe tres datos específicos que tengas sobre tu colegio: una hora, un número y un lugar.",
)

lesson(
    OA2, 2,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a encontrar en un texto oral quién hace qué, dónde y cuándo. Sirve para identificar personas, acciones, objetos, lugares y tiempo.",
    ["Sé que who es quién y where es dónde.", "Conozco los días de la semana y la hora en punto."],
    [
        "Cuando escuchas un texto, puedes buscar cinco tipos de información. People (personas): who. Actions (acciones): what do they do. Objects (objetos): what things. Places (lugares): where. Time (tiempo): when, con días y horas. Cada palabra de pregunta te dice qué buscar.",
        "Las acciones aparecen como verbos: goes (va), leaves (sale), brings (trae), meets (se junta con), sells (vende). Los lugares aparecen después de palabras como at (en), in (en), near (cerca de) y to (hacia). El tiempo aparece con on Friday (el viernes) y at nine (a las nueve).",
        "Tu tarea es escuchar con la pregunta en mente. Si te piden el lugar, escucha las palabras que siguen a to, at, in o near. Si te piden la hora, escucha los números después de at. Así no necesitas entender todo el texto, solo lo que buscas.",
    ],
    [("who / what / where / when", "quién / qué / dónde / cuándo"), ("goes to", "va a"), ("leaves", "sale"), ("brings", "trae"), ("on Friday", "el viernes"), ("at nine o'clock", "a las nueve en punto")],
    [
        ("Persona y acción", ADULT + "«Class 5B goes to the zoo on Friday. The bus leaves at nine o'clock from the school gate. The students bring a sandwich, a bottle of water and a hat. Miss Rojas and Mr. Silva go with the class.» (zoo = zoológico, gate = portón, bottle = botella). ¿Quiénes van con la clase?", ["Pregunto who.", "Busco go with the class.", "Miss Rojas y Mr. Silva."], "La señorita Rojas y el señor Silva"),
        ("Lugar y tiempo", "En el mismo texto, ¿adónde van y cuándo?", ["Where: goes to the zoo.", "When: on Friday.", "Van al zoológico el viernes."], "Al zoológico, el viernes"),
    ],
    [
        ("Responder «a las nueve» cuando preguntan el día.", "Se confunde la hora con el día.", "On Friday es el día; at nine es la hora."),
        ("Anotar solo un objeto de la lista de lo que traen.", "No se escucha la lista completa.", "Cuenta los objetos: sandwich, bottle of water y hat son tres."),
    ],
    [
        (ADULT + "«Class 5B goes to the zoo on Friday. The bus leaves at nine o'clock from the school gate. The students bring a sandwich, a bottle of water and a hat. Miss Rojas and Mr. Silva go with the class.» ¿A qué hora sale el bus?", "A las nueve", "Dice at nine o'clock."),
        (ADULT + "«Class 5B goes to the zoo on Friday. The bus leaves at nine o'clock from the school gate. The students bring a sandwich, a bottle of water and a hat. Miss Rojas and Mr. Silva go with the class.» ¿De dónde sale el bus?", "Del portón del colegio", "Dice from the school gate."),
        (ADULT + "«Class 5B goes to the zoo on Friday. The bus leaves at nine o'clock from the school gate. The students bring a sandwich, a bottle of water and a hat. Miss Rojas and Mr. Silva go with the class.» ¿Cuántas cosas traen los estudiantes?", "3", "Traen un sándwich, una botella de agua y un sombrero."),
    ],
    [
        ("¿Qué pregunta usas para buscar un lugar: where o when?", "where", "Where significa dónde."),
        ("En «on Friday», ¿qué tipo de información es: lugar o tiempo?", "Tiempo", "Friday es un día de la semana."),
        ("En «Miss Rojas and Mr. Silva go with the class», ¿qué dato da: personas o lugares?", "Personas", "Miss Rojas y Mr. Silva son personas."),
    ],
    [
        (ADULT + "«On Monday, Ines meets her friend Paula at the park. They play with a ball for one hour. Then they eat ice cream near the lake.» (meets = se junta con, park = parque, ice cream = helado). ¿Con quién se junta Ines?", "Con su amiga Paula", "Dice meets her friend Paula."),
        (ADULT + "«On Monday, Ines meets her friend Paula at the park. They play with a ball for one hour. Then they eat ice cream near the lake.» ¿Dónde comen helado?", "Cerca del lago", "Dice near the lake."),
        (ADULT + "«On Monday, Ines meets her friend Paula at the park. They play with a ball for one hour. Then they eat ice cream near the lake.» ¿Durante cuánto tiempo juegan con la pelota?", "Una hora", "Dice for one hour."),
    ],
    [
        (ADULT + "«On Monday, Ines meets her friend Paula at the park. They play with a ball for one hour. Then they eat ice cream near the lake.» ¿En qué día se juntan? a) lunes b) viernes", "a) lunes", "Dice on Monday."),
        ("En el texto de la clase 5B, Miss Rojas y Mr. Silva van con la clase. ¿Cuántas personas van con la clase, sin contar a los estudiantes?", "2", "Miss Rojas y Mr. Silva son dos personas."),
    ],
    [
        (ADULT + "«The mail carrier brings a letter to Mr. Pérez on Wednesday at noon. The letter is from his sister in Chile.» (mail carrier = cartero, letter = carta, noon = mediodía, sister = hermana). ¿Qué trae el cartero?", "Una carta", "Dice brings a letter."),
        (ADULT + "«The mail carrier brings a letter to Mr. Pérez on Wednesday at noon. The letter is from his sister in Chile.» (sister = hermana). ¿Quién escribió la carta? a) la hermana del señor Pérez b) el cartero", "a)", "Dice from his sister."),
    ],
    [(ADULT + "Una niña dice por teléfono: «I leave home at seven thirty and I walk to school with my brother.» (seven thirty = siete y media, brother = hermano). ¿Con quién camina al colegio?", "Con su hermano", "Dice with my brother.")],
    [
        ("¿Qué significa «bring»?", "Traer o llevar", "Bring es llevar algo consigo."),
        ("¿Qué significa «near»?", "Cerca de", "Near indica poca distancia."),
        ("¿Qué pregunta usas para saber la hora: who o what time?", "what time", "What time es a qué hora."),
    ],
    task("Un adulto lee dos veces este texto: «On Saturday, Tomás and his father go to the market at ten o'clock. They buy apples, bread and cheese. Then they walk home.» (market = feria, buy = compran, cheese = queso). Escribe: quiénes van, cuándo, a qué hora, adónde y qué compran.", "Tomás y su papá; el sábado; a las diez; a la feria; manzanas, pan y queso.", ["nombra a las dos personas", "da día y hora", "nombra los tres objetos"], ["hoja con respuestas", "nota del adulto"], ["confundir el día con la hora", "olvidar un objeto"], "Reconoce los datos correctos y repite con él las preguntas who, when, where y what."),
    "Pide a un adulto que lea el texto del zoológico y levanta un dedo por cada objeto que traen.",
    "Escribe una oración en español que diga quién, qué y cuándo sobre algo que hiciste esta semana.",
)

lesson(
    OA2, 3,
    "Los textos escritos en cada ejercicio, que lee un adulto con voces distintas; una hoja para tapar el guion y lápiz.",
    "Aprenderé a seguir los pasos de unas instrucciones habladas y a saber quién habla en cada parte. Sirve para hacer algo siguiendo una explicación en inglés.",
    ["Sé que first, next, then y finally ordenan pasos.", "Conozco water, cup, bean y window."],
    [
        "En un texto con dos hablantes (speakers), uno puede explicar y otro preguntar. Los nombres antes de los dos puntos te dicen quién habla. Es útil saber quién da las instrucciones y quién pide ayuda. Cuenta solo los nombres distintos.",
        "Las instrucciones se dan con verbos al comienzo de la frase: put (poner), add (agregar), place (colocar), wait (esperar). También se oyen palabras para el orden: first, second, third, next y finally. Los números como second (segundo), third (tercero) y fourth (cuarto) también marcan el orden.",
        "Para seguir pasos, cuenta cuántos hay y repítelos en orden. Si un paso dice «just a little water», significa «solo un poco de agua»: la cantidad importa. Escucha también las palabras de lugar, como near (cerca de) y on (sobre).",
    ],
    [("speaker", "persona que habla"), ("put / add / place / wait", "poner / agregar / colocar / esperar"), ("first / second / third", "primero / segundo / tercero"), ("just a little", "solo un poco"), ("window", "ventana"), ("bean", "poroto")],
    [
        ("Contar pasos", ADULT + "«Nora: How do we plant a bean? Ben: First, put some cotton in a cup. Second, put the bean on the cotton. Third, add just a little water. Fourth, place the cup near a window. Finally, wait.» (plant = plantar, cotton = algodón, cup = vaso). ¿Cuántos pasos cuenta Ben?", ["Cuento first, second, third, fourth y finally.", "Son cinco palabras de orden.", "Hay cinco pasos."], "5"),
        ("Quién da las instrucciones", "En el mismo diálogo, ¿quién explica y quién pregunta?", ["Nora hace la pregunta How do we plant a bean?", "Ben responde con los pasos.", "Ben explica y Nora pregunta."], "Ben explica y Nora pregunta"),
    ],
    [
        ("Pensar que Nora da las instrucciones porque habla primero.", "Se confunde quien habla primero con quien explica.", "Mira quién dice los pasos: es Ben."),
        ("Agregar mucha agua al poroto.", "No se escuchó just a little.", "La cantidad importa: solo un poco de agua."),
    ],
    [
        (ADULT + "«Nora: How do we plant a bean? Ben: First, put some cotton in a cup. Second, put the bean on the cotton. Third, add just a little water. Fourth, place the cup near a window. Finally, wait.» ¿Qué se pone en el vaso primero?", "Algodón", "First, put some cotton in a cup."),
        (ADULT + "«Nora: How do we plant a bean? Ben: First, put some cotton in a cup. Second, put the bean on the cotton. Third, add just a little water. Fourth, place the cup near a window. Finally, wait.» ¿Cuánta agua se agrega?", "Solo un poco", "Dice just a little water."),
        (ADULT + "«Nora: How do we plant a bean? Ben: First, put some cotton in a cup. Second, put the bean on the cotton. Third, add just a little water. Fourth, place the cup near a window. Finally, wait.» ¿Dónde se coloca el vaso?", "Cerca de una ventana", "Dice near a window."),
    ],
    [
        ("En el diálogo del poroto, ¿cuántos speakers hay?", "2", "Hablan Nora y Ben."),
        ("En el diálogo del poroto, ¿qué paso es el tercero? a) agregar un poco de agua b) poner el poroto sobre el algodón", "a) agregar un poco de agua", "Third, add just a little water."),
        ("En el diálogo del poroto, ¿qué se hace al final? a) esperar b) poner algodón", "a) esperar", "Finally, wait significa esperar al final."),
    ],
    [
        (ADULT + "«Teacher: Open your notebook. Write the date. Draw a line. Then write your name. Student: Where do I write my name? Teacher: Under the line.» (open = abre, date = fecha, line = línea, under = debajo de). ¿Dónde escribe el estudiante su nombre?", "Debajo de la línea", "La profesora dice under the line."),
        (ADULT + "«Teacher: Open your notebook. Write the date. Draw a line. Then write your name. Student: Where do I write my name? Teacher: Under the line.» ¿Cuántas instrucciones da la profesora antes de la pregunta del estudiante?", "4", "Open, write the date, draw a line y write your name."),
        (ADULT + "«Teacher: Open your notebook. Write the date. Draw a line. Then write your name. Student: Where do I write my name? Teacher: Under the line.» ¿Quién hace la pregunta?", "El estudiante", "El nombre Student está antes de Where do I write my name."),
    ],
    [
        ("Un compañero dice que se escribe el nombre antes de la fecha. En el texto de la profesora, ¿qué se escribe primero: la fecha o el nombre?", "La fecha", "La profesora dice write the date antes de write your name."),
        ("En el texto del poroto, ¿por qué es importante la palabra second? a) Indica que poner el poroto es el segundo paso b) Dice dónde está el poroto", "a)", "Second es una palabra de orden."),
    ],
    [
        (ADULT + "«Ana: How do I make a sandwich? Leo: First, take two slices of bread. Second, put cheese on one slice. Third, put the other slice on top. Last, ask an adult to cut it.» (slices = rebanadas, top = encima, last = por último). ¿Qué va en una rebanada?", "Queso", "Dice put cheese on one slice."),
        (ADULT + "«Ana: How do I make a sandwich? Leo: First, take two slices of bread. Second, put cheese on one slice. Third, put the other slice on top. Last, ask an adult to cut it.» ¿Quién responde con los pasos? a) Leo b) Ana", "a) Leo", "Leo dice los pasos y Ana pregunta."),
    ],
    [(ADULT + "Un profesor dice: «Please stand in a line, open the door, and walk slowly.» (stand in a line = ponte en fila, door = puerta, slowly = despacio). ¿Cómo debes caminar?", "Despacio", "La palabra slowly significa despacio.")],
    [
        ("¿Qué significa «second»?", "Segundo", "Second indica el lugar número dos en el orden."),
        ("¿Qué significa «just a little»?", "Solo un poco", "Indica una cantidad pequeña."),
        ("¿Cómo sabes quién habla en un texto con dos speakers?", "Por el nombre antes de los dos puntos", "Cada nombre indica el turno de esa persona."),
    ],
    task("Un adulto lee dos veces este diálogo: «Sam: How do I wash my hands? Lia: First, wet your hands. Second, put soap. Third, rub for twenty seconds. Fourth, rinse. Finally, dry with a towel.» (wet = moja, soap = jabón, rub = frota, seconds = segundos, rinse = enjuaga, dry = seca, towel = toalla). Escribe los cinco pasos en español en orden y marca quién explica.", "1 mojar, 2 poner jabón, 3 frotar veinte segundos, 4 enjuagar, 5 secar con toalla. Explica Lia.", ["cinco pasos en orden", "incluye veinte segundos", "dice que explica Lia"], ["hoja con pasos", "nota del adulto"], ["olvidar enjuagar", "decir que explica Sam"], "Reconoce el orden logrado y repite con él los números first a finally."),
    "Pide a un adulto que lea los pasos del poroto y ve mostrando con los dedos el número de cada paso.",
    "Escribe tres pasos en español para algo que sabes hacer, usando primero, luego y al final.",
)

lesson(
    OA2, 4,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a reconocer palabras conocidas, expresiones comunes y a adivinar algunas palabras nuevas con la ayuda del contexto. Sirve para entender más aunque no conozca todas las palabras.",
    ["Conozco palabras como big, small, fast y happy.", "Sé decir Excuse me y Thank you."],
    [
        "Hay palabras que ya conoces (vocabulario aprendido) y expresiones que se oyen todos los días: Excuse me (disculpa), Let's go (vamos), Be careful (ten cuidado), Of course (por supuesto), I don't understand (no entiendo) y Can you repeat, please? (¿puedes repetir, por favor?). Aprenderlas ayuda mucho a entender.",
        "A veces aparece una palabra menos frecuente, que no conoces. No te detengas: usa el contexto, que son las palabras de alrededor. «The elephant is enormous. It is much bigger than the car.» La segunda oración te dice que enormous significa muy grande. Así adivinas el significado sin diccionario.",
        "Para adivinar, hazte tres preguntas: ¿qué palabras conocidas hay cerca?, ¿qué tipo de palabra puede ser (una cosa, una acción, una cualidad)? y ¿qué significado encaja en la historia? Después comprueba tu idea con la siguiente oración. Si no encaja, prueba otra.",
    ],
    [("Excuse me", "disculpa"), ("Let's go", "vamos"), ("Be careful", "ten cuidado"), ("Of course", "por supuesto"), ("context", "contexto: palabras de alrededor"), ("enormous", "enorme")],
    [
        ("Expresión frecuente", ADULT + "«Sara: Excuse me, can you help me? Paco: Of course! What do you need?» (help = ayudar, need = necesitas). ¿Qué quiere decir Paco con «Of course»?", ["Of course es una expresión frecuente.", "Responde a una petición de ayuda.", "Significa por supuesto."], "Por supuesto"),
        ("Adivinar por contexto", ADULT + "«The elephant is enormous. It is much bigger than the car.» ¿Qué significa enormous?", ["Busco una pista: much bigger than the car.", "El elefante es más grande que un auto.", "Enormous quiere decir muy grande."], "Muy grande"),
    ],
    [
        ("Detenerse en la palabra que no se conoce y dejar de escuchar.", "Se pierde el resto del mensaje.", "Sigue escuchando: el contexto suele explicar la palabra."),
        ("Traducir Let's go como «déjalo ir».", "Se traduce palabra por palabra.", "Let's go es una expresión completa: vamos."),
    ],
    [
        ("¿Qué significa «Be careful»?", "Ten cuidado", "Es una expresión para avisar de un peligro."),
        ("¿Qué significa «Can you repeat, please?»", "¿Puedes repetir, por favor?", "Se usa para pedir que te vuelvan a decir algo."),
        ("Cuando dices «I don't understand», ¿qué quieres decir?", "No entiendo", "Understand es entender."),
    ],
    [
        (ADULT + "«My tiny cat sleeps in a small box. It is so small that I can hold it in one hand.» (hold = sostener, hand = mano). ¿Qué significa tiny? a) muy pequeño b) muy rápido", "a) muy pequeño", "El texto dice small y que cabe en una mano."),
        (ADULT + "«The soup is delicious. I eat it all and I want more.» (soup = sopa, more = más). ¿Qué significa delicious? a) muy rico b) muy caliente", "a) muy rico", "Quien la come quiere más."),
        (ADULT + "«The bike is very fast. It goes quickly down the hill.» (hill = cerro). ¿Qué significa quickly? a) rápido b) despacio", "a) rápido", "Va fast cerro abajo."),
    ],
    [
        (ADULT + "«Look, a rainbow! It is beautiful. I love its colors: red, orange, yellow, green and blue.» (rainbow = arcoíris, colors = colores). ¿Cuántos colores nombra?", "5", "Red, orange, yellow, green y blue son cinco."),
        (ADULT + "«Look, a rainbow! It is beautiful. I love its colors: red, orange, yellow, green and blue.» ¿Qué significa beautiful? a) hermoso b) pequeño", "a) hermoso", "Quien lo dice lo ama y lo admira."),
        ("Una compañera dice «Excuse me» antes de pasar por entre dos personas. ¿Para qué lo usa? a) para pedir permiso b) para despedirse", "a) para pedir permiso", "Excuse me se usa para pedir paso o llamar la atención con cortesía."),
    ],
    [
        ("Un compañero escuchó «The room is silent. Nobody speaks.» (nobody = nadie, speaks = habla) y dijo que silent es «ruidoso». ¿Qué significa silent?", "Silencioso", "Nadie habla, así que el cuarto está en silencio."),
        ("En «Be careful, the floor is wet!» (floor = piso, wet = mojado), ¿qué te avisa la expresión Be careful?", "Que hay un posible peligro", "El piso mojado puede resbalar."),
    ],
    [
        (ADULT + "«I am exhausted. I ran for an hour and now I need to sit down.» (ran = corrí, hour = hora, sit down = sentarme). ¿Qué significa exhausted? a) muy cansado b) muy contento", "a) muy cansado", "Tras correr una hora, uno necesita sentarse."),
        ("Elige la mejor estrategia ante una palabra desconocida: a) parar y no escuchar más b) usar las palabras de alrededor", "b)", "El contexto ayuda a adivinar el sentido."),
    ],
    [(ADULT + "Un compañero te dice: «Let's go to the playground!» (playground = patio de juegos). ¿Qué te propone? a) ir al patio de juegos b) ir a casa", "a)", "Let's go to es vamos a.")],
    [
        ("¿Qué es el contexto?", "Las palabras de alrededor que dan pistas", "El contexto ayuda a adivinar un significado."),
        ("¿Qué significa «enormous»?", "Muy grande", "Enormous es más grande que big."),
        ("¿Qué significa «Of course»?", "Por supuesto", "Es una respuesta afirmativa."),
    ],
    task("Un adulto lee dos veces este texto: «Our dog is very energetic. He runs in the park for an hour and never gets tired. He also loves to splash in the puddles.» (runs = corre, gets tired = se cansa, splash = chapotear). Escribe qué crees que significa energetic y qué palabras del texto te dieron la pista.", "Energetic significa lleno de energía; la pista es que corre una hora y nunca se cansa.", ["da un significado razonable", "cita la pista del texto", "usa español claro"], ["hoja con respuesta", "nota del adulto"], ["decir «cansado»", "no explicar la pista"], "Aplaude la pista correcta y repite con él la palabra never gets tired."),
    "Pide a un adulto que diga «Excuse me», «Of course» y «Be careful» y responde con un gesto distinto para cada uno.",
    "Escribe una oración en español que contenga la expresión «Let's go» y dónde irías.",
)

lesson(
    OA2, 5,
    "Las listas de palabras escritas en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a diferenciar los sonidos /g/ (go, ago, egg) y /dʒ/ (jacket, general, age) al escucharlos. Sirve para no confundir palabras que suenan parecido.",
    ["Conozco palabras como go, egg, jacket y age.", "Sé que una misma letra puede sonar distinto."],
    [
        "El inglés tiene dos sonidos que se confunden. El sonido /g/ es el de «gato» en español: go, ago, egg, goat, game, big, dog, green, bag. El sonido /dʒ/ no existe igual en español: es como una «ch» pero con la garganta vibrando. Aparece en jacket, jam, jump, juice, general, giant, giraffe, gym, age, page, orange, bridge.",
        "La letra j casi siempre suena /dʒ/ en inglés: jacket, jam, jump. La letra g puede sonar de dos formas. Con a, o, u y al final suele sonar /g/: go, game, big. Con e o i, a veces suena /dʒ/: general, giraffe, gym. Hay excepciones, como girl, give y get, que suenan /g/.",
        "Para identificar el sonido, no mires solo la letra: escucha. Para tocar tu garganta, pon un dedo sobre ella y di egg y age: en los dos hay vibración, pero /dʒ/ sale con la lengua pegada arriba y /g/ con la lengua atrás. Practica diciendo las palabras en voz alta.",
    ],
    [("/g/", "sonido de go, ago, egg"), ("/dʒ/", "sonido de jacket, general, age"), ("goat", "cabra"), ("jam", "mermelada"), ("giraffe", "jirafa"), ("bridge", "puente")],
    [
        ("Reconocer /g/", ADULT + "Dice: «goat, jam, game». ¿Cuáles empiezan con el sonido /g/ de go?", ["Escucho goat: empieza como go.", "Escucho jam: empieza como jacket.", "Escucho game: empieza como go."], "goat y game"),
        ("Reconocer /dʒ/", "Lee: giraffe, girl, gym. ¿Cuáles empiezan con el sonido /dʒ/ de general?", ["Giraffe suena como general.", "Girl es excepción: suena /g/.", "Gym suena como general."], "giraffe y gym"),
    ],
    [
        ("Decir que giraffe empieza con /g/ porque se escribe con g.", "Se mira la letra y no el sonido.", "Escucha: giraffe empieza igual que general, con /dʒ/."),
        ("Decir que jacket empieza con /g/.", "Se confunde la j con la g.", "La j suena /dʒ/ en jacket, jam y jump."),
    ],
    [
        ("¿Con qué sonido termina egg: /g/ o /dʒ/?", "/g/", "Egg termina como go, con /g/."),
        ("¿Con qué sonido termina age: /g/ o /dʒ/?", "/dʒ/", "Age termina con el sonido de general."),
        ("¿Con qué sonido empieza jam: /g/ o /dʒ/?", "/dʒ/", "La j de jam suena /dʒ/."),
    ],
    [
        ("Un adulto dice «big». ¿Termina con /g/ o /dʒ/?", "/g/", "Big termina como egg."),
        ("Un adulto dice «page». ¿Termina con /g/ o /dʒ/?", "/dʒ/", "Page termina como age."),
        ("Un adulto dice «dog». ¿Termina con /g/ o /dʒ/?", "/g/", "Dog termina con el sonido de go."),
    ],
    [
        ("Elige la palabra con /dʒ/ al comienzo: a) green b) juice c) game", "b) juice", "Juice empieza como jacket."),
        ("Elige la palabra con /g/ al comienzo: a) giant b) goat c) orange", "b) goat", "Goat empieza como go."),
        ("Elige la palabra que termina con /dʒ/: a) bridge b) dog c) egg", "a) bridge", "Bridge termina como age; dog y egg terminan con /g/."),
    ],
    [
        ("Clasifica estas palabras en /g/ o /dʒ/ al comienzo: green, jump, game, gym. ¿Cuántas empiezan con /dʒ/?", "2", "Jump y gym empiezan con /dʒ/."),
        ("¿Suenan igual el comienzo de «get» y el de «general»?", "No", "Get empieza con /g/ y general con /dʒ/."),
    ],
    [
        ("Lee: «bag» y «badge» (badge = insignia). ¿Cuál termina con /dʒ/?", "badge", "Badge termina con el sonido de age."),
        ("Lee: «jam», «gum» (gum = chicle) y «giraffe». ¿Cuál empieza con /g/?", "gum", "Gum empieza como go; jam y giraffe empiezan con /dʒ/."),
    ],
    [(ADULT + "En una feria, una vendedora dice: «Orange juice for sale!» (orange = naranja, for sale = en venta). ¿Cuántas palabras contienen el sonido /dʒ/?", "2", "Orange y juice contienen /dʒ/.")],
    [
        ("¿Con qué sonido empieza «go»?", "/g/", "Go empieza con el sonido /g/."),
        ("¿La letra j casi siempre suena /g/ o /dʒ/?", "/dʒ/", "La j suena /dʒ/ en jam y jump."),
        ("¿Suena /g/ la g de «girl»?", "Sí", "Girl es una excepción: se dice con /g/."),
    ],
    task("Un adulto lee dos veces estas palabras: goat, giant, game, jacket, egg, orange, dog, bridge. En tu hoja haz dos columnas: /g/ y /dʒ/ y escribe cada palabra donde corresponda. Recuerda que /dʒ/ suena en la mayoría de las palabras con j y en algunas con g.", "/g/: goat, game, egg, dog. /dʒ/: giant, jacket, orange, bridge.", ["cuatro palabras en cada columna", "escribe giant y orange en /dʒ/", "escribe goat y dog en /g/"], ["tabla en la hoja", "nota del adulto"], ["poner giant en /g/", "poner egg en /dʒ/"], "Reconoce las palabras bien ubicadas y repite con él las que cambió, diciéndolas despacio."),
    "Pide a un adulto que diga goat y jacket y pon la mano en la garganta para sentir cada sonido.",
    "Escribe tres palabras con /g/ y tres con /dʒ/ de la lista de esta clase.",
)

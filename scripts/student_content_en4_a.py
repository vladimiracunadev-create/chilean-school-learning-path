"""Student material for 4.º básico Inglés (propuesta), EN04 OA 01 (rimas, chants, canciones, cuentos y diálogos).

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Todos los textos son originales. Cada palabra o estructura en inglés se explica antes de usarla o lleva su pista en español.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1 = "EN04 OA 01"
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


# ================================================================ OA 01
lesson(
    OA1, 1,
    "Las rimas escritas en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a seguir los sonidos que se repiten al final de las líneas de una rima y a saber qué líneas riman entre sí. Sirve para entender y disfrutar rimas en inglés.",
    ["Sé que una rima une palabras con el mismo sonido final.", "Conozco palabras como cat, sun, tree, star y bird."],
    [
        "Una rima (rhyme) tiene palabras que terminan con el mismo sonido. Cat y hat riman: las dos terminan en «at». Lo que importa es el sonido del final, no el del comienzo. Cat y cap comienzan igual, pero no riman, porque sus finales son distintos.",
        "Dos palabras que riman forman un par (rhyme pair). Suelen estar al final de las líneas (lines). En una rima de cuatro líneas, a veces riman las líneas 1 y 2 y también las líneas 3 y 4. Otras veces riman la 1 con la 3 y la 2 con la 4.",
        "Fíjate en el sonido, no en la escritura. Two, blue y shoe riman aunque se escriban distinto. Bear y chair también riman. Para comprobarlo, di las dos palabras en voz alta y escucha solo lo que suena desde la vocal hasta el final.",
    ],
    [("rhyme", "rima: palabras con el mismo sonido final"), ("rhyme pair", "par de palabras que riman"), ("line", "línea o verso"), ("end sound", "sonido del final"), ("sun / run", "sol / correr"), ("tree / me", "árbol / yo")],
    [
        ("Encontrar el par", ADULT + "«The zebra is in the sun. The zebra likes to run. The bird is in the tree. The bird can sing to me.» (zebra = cebra, likes to = le gusta, can sing = puede cantar). ¿Qué palabra rima con sun?", ["Escucho el final de sun.", "Run termina igual.", "Run está en la línea 2."], "run"),
        ("Qué líneas riman", "En la misma rima, ¿qué línea rima con la línea 3 («The bird is in the tree»)?", ["La línea 3 termina en tree.", "La línea 4 termina en me.", "Tree y me terminan igual."], "La línea 4"),
    ],
    [
        ("Pensar que cat y cap riman porque comienzan igual.", "Se escucha el comienzo y no el final.", "Compara los sonidos finales: cat termina en «at» y cap en «ap»; no riman."),
        ("Decir que two y blue no riman porque se escriben distinto.", "Se mira la escritura y no el sonido.", "Di las palabras en voz alta: las dos terminan en el sonido «u»."),
    ],
    [
        (ADULT + "«The cat is on the mat. The cat is very fat.» (mat = alfombrilla, fat = gordo). ¿Qué palabra de la segunda línea rima con mat?", "fat", "Mat y fat terminan en «at»."),
        ("¿Riman bear y chair?", "Sí", "Las dos terminan con el mismo sonido «er»."),
        ("¿Riman book y boat?", "No", "Comienzan igual, pero sus finales son distintos."),
    ],
    [
        ("¿Por qué cat y cap no riman?", "Porque comienzan igual pero terminan con sonidos distintos", "La rima se decide por el sonido final."),
        (ADULT + "Elige el par que rima: a) moon y spoon b) moon y man. (spoon = cuchara)", "a", "Moon y spoon terminan en «un», pero moon y man no."),
        ("¿En qué parte de las líneas de una rima suelen estar las palabras que riman?", "Al final", "Las palabras que riman suelen cerrar la línea."),
    ],
    [
        (ADULT + "«I have a fish. I make a wish. I see a boat. It can float.» (wish = deseo, float = flotar). ¿Qué palabra rima con fish?", "wish", "Fish y wish terminan en «ish»."),
        (ADULT + "«I have a fish. I make a wish. I see a boat. It can float.» ¿Qué palabra rima con boat?", "float", "Boat y float terminan en «ot»."),
        (ADULT + "«A bee, a tree, and me.» ¿Cuántas palabras de esta línea terminan con el sonido «i»?", "3", "Bee, tree y me terminan con el mismo sonido; and no."),
    ],
    [
        ("Pedro dice que door y floor no riman porque empiezan con letras distintas. ¿Tiene razón?", "No; riman porque terminan con el mismo sonido", "El comienzo no importa en una rima."),
        (ADULT + "«1. I see a bird. 2. I hear a song. 3. I say a word. 4. We sing along.» (hear = oigo, sing along = cantar juntos). ¿Qué línea rima con la línea 1?", "La línea 3", "Bird y word terminan con el mismo sonido; song y along riman en las líneas 2 y 4."),
    ],
    [
        ("Rima: «1. I like the sun. 2. It is fun. 3. I eat a pear. 4. I have a chair. 5. The sky is blue.» ¿Qué línea no rima con ninguna otra?", "La línea 5", "Sun y fun riman; pear y chair riman; blue no tiene pareja."),
        ("Completa para que rime: «I see a star. It is very ___.» Elige: far, cat o sun.", "far", "Star y far terminan en «ar»."),
    ],
    [(ADULT + "En el recreo, un grupo canta: «We play all day. We shout hooray!» (shout = gritar, hooray = ¡hurra!). ¿Qué palabra rima con day?", "hooray", "Day y hooray terminan con el sonido «ei».")],
    [
        ("¿Qué significa «rhyme»?", "Rima", "Rhyme es la palabra en inglés para palabras con el mismo sonido final."),
        ("¿Riman too y shoe?", "Sí", "Las dos terminan en el sonido «u»."),
        ("¿Qué escuchas para saber si dos palabras riman: el comienzo o el final?", "El final", "La rima está en el sonido final."),
    ],
    task("Un adulto lee dos veces esta rima: «Look at the moon. It comes up soon. Look at the star. It shines from far.» (moon = luna, soon = pronto, shines = brilla, far = lejos). Escribe en tu hoja los dos pares de palabras que riman. Luego escribe una tercera palabra que rime con moon, como spoon.", "Moon-soon y star-far; otra palabra que rima con moon: spoon.", ["escribe moon-soon", "escribe star-far", "agrega una palabra que rime con moon"], ["hoja con los pares", "nota del adulto"], ["escribir moon-star, que no riman", "elegir una palabra que no termina en «un»"], "Reconoce los pares correctos y repite con él, despacio, los finales «un» y «ar»."),
    "Pide a un adulto que lea «sun, run, fun» y haz una palmada en cada palabra. Después dibuja un sol y a alguien corriendo.",
    "Escribe una rima de dos líneas con las palabras tree y me, por ejemplo «I see a tree. It looks at me.».",
)

lesson(
    OA1, 2,
    "Los chants escritos en cada ejercicio, que lee un adulto en voz alta; espacio libre y seguro para moverte y lápiz.",
    "Aprenderé a seguir las acciones de un chant: qué hacer, cuántas veces y en qué orden. Sirve para participar en juegos y chants en inglés mostrando que entiendo.",
    ["Sé que clap es aplaudir, stamp es pisar fuerte y jump es saltar.", "Sé contar en inglés hasta veinte."],
    [
        "Un chant (chant) es un texto con ritmo que se dice en voz alta y se acompaña con movimientos. Escucha las acciones: stand up (ponerse de pie), sit down (sentarse), turn around (girar), touch (tocar), stretch up (estirarse hacia arriba), march (marchar) y hop (dar saltitos).",
        "Después de la acción puede venir un número y la palabra times (veces). «Clap four times» significa «aplaude cuatro veces». Las palabras then (luego) y after that (después de eso) unen acciones. El orden en que las oyes es el orden en que las haces.",
        "También se nombran partes del cuerpo: hands (manos), feet (pies), head (cabeza), knees (rodillas) y toes (dedos de los pies). Para seguir un chant escucha tres cosas: la acción, la parte del cuerpo o el número y el orden. No imites a otros sin escuchar.",
    ],
    [("stand up / sit down", "ponerse de pie / sentarse"), ("turn around", "girar"), ("touch", "tocar"), ("stretch up", "estirarse hacia arriba"), ("times", "veces"), ("then / after that", "luego / después de eso"), ("hands / feet / head / knees / toes", "manos / pies / cabeza / rodillas / dedos de los pies")],
    [
        ("Qué acción sigue", ADULT + "«Clap, clap, clap your hands. Stamp, stamp, stamp your feet. Turn around, turn around. Sit down on your seat.» (seat = asiento). ¿Qué haces después de pisar fuerte?", ["Oigo clap y luego stamp.", "Después de stamp your feet oigo turn around.", "Esa es la siguiente acción."], "Giro"),
        ("Sumar los movimientos", ADULT + "«Jump five times, then clap two times. Stop!» ¿Cuántos movimientos haces en total, sin contar stop?", ["Oigo jump five times: cinco saltos.", "Oigo clap two times: dos palmadas.", "Sumo 5 + 2."], "7"),
    ],
    [
        ("Ignorar la palabra times y hacer la acción una sola vez.", "No se escuchó el número.", "Escucha el número: «three times» son tres veces."),
        ("Hacer sit down cuando se oyó stand up.", "Se mezclan las palabras de acción.", "Stand up es ponerse de pie y sit down es sentarse; vuelve a escuchar la acción."),
    ],
    [
        (ADULT + "«Stand up!» ¿Qué haces?", "Me pongo de pie", "Stand up significa ponerse de pie."),
        ("¿Qué significa «touch your head»?", "Toca tu cabeza", "Touch es tocar y head es cabeza."),
        (ADULT + "«Clap four times.» ¿Cuántas palmadas das?", "4", "Four times son cuatro veces."),
    ],
    [
        ("En «stamp your feet», ¿qué parte del cuerpo usas?", "Los pies", "Feet significa pies."),
        ("En «jump three times», ¿qué número te dice cuántas veces saltas?", "Tres", "Three es tres."),
        ("¿Qué significa «turn around»?", "Girar", "Turn around es dar una vuelta sobre ti mismo."),
    ],
    [
        (ADULT + "«Touch your head two times. Touch your knees three times. Stop!» ¿Cuántas veces tocas las rodillas?", "3", "Knees three times son tres toques."),
        arith(ADULT + "«Touch your head two times. Touch your knees three times. Stop!» ¿Cuántos toques haces en total, contando cabeza y rodillas?", "2+3", "Se suman los toques de la cabeza y de las rodillas."),
        (ADULT + "«Stand up. Stretch up high. Clap two times. Sit down.» (high = alto). ¿Qué haces justo antes de sentarte?", "Aplaudo dos veces", "Clap two times viene antes de sit down."),
    ],
    [
        ("El chant dice «Jump four times, then turn around». Sofía giró primero y saltó después. ¿Qué debió hacer primero?", "Saltar cuatro veces", "Then indica que girar viene después."),
        (ADULT + "«Clap, clap. Stamp, stamp, stamp. Clap, clap.» ¿Cuántos pisotones y cuántas palmadas hay en total?", "3 pisotones y 4 palmadas", "Stamp aparece tres veces y clap aparece dos veces más dos."),
    ],
    [
        arith(ADULT + "«Clap five times. Stamp four times. Jump six times.» ¿Cuántos movimientos haces en total?", "5+4+6", "Se suman los tres grupos de movimientos."),
        arith(ADULT + "«Hop three times, spin around, hop three times, stop.» (spin around = girar). ¿Cuántos saltitos haces en total?", "3+3", "Se suman los dos grupos de saltitos."),
    ],
    [(ADULT + "En la clase, la profesora dice: «Stand up. Touch your toes. Stretch up high. Sit down.» (toes = dedos de los pies). ¿Qué haces en segundo lugar?", "Toco los dedos de los pies", "Touch your toes es la segunda instrucción.")],
    [
        ("¿Qué significa «then»?", "Luego", "Then une una acción con la siguiente."),
        ("¿Qué parte del cuerpo es «hands»?", "Las manos", "Hands significa manos."),
        ("¿Qué haces si no estás seguro de la acción del chant?", "Vuelvo a escuchar las palabras de acción", "No basta con copiar a otras personas."),
    ],
    task("Un adulto dice dos veces este chant: «Clap two times. Stamp three times. Turn around. Touch your knees. Sit down.» Haz los movimientos en el orden que oyes, en un espacio libre y seguro. Después di en inglés las dos acciones con número que hiciste: clap y stamp.", "Dos palmadas, tres pisotones, un giro, tocar las rodillas y sentarse.", ["hace las acciones en orden", "respeta cuántas veces", "termina sentado con sit down"], ["nota del adulto", "foto o video con permiso de la familia"], ["cambiar el orden de las acciones", "no contar las veces"], "Aplaude el orden logrado y repite con él, despacio, la acción que le costó."),
    "Pide a un adulto que diga «stand up, sit down, turn around» y haz cada acción una vez.",
    "Inventa un chant de tres líneas con las acciones march, clap y sit down, por ejemplo «March four times. Clap two times. Sit down!».",
)

lesson(
    OA1, 3,
    "Las canciones y los cuentos cortos escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a ordenar lo que pasa en una canción o un cuento corto con first, next, then, after that y finally. Sirve para recordar y contar una historia en el orden correcto.",
    ["Sé que first es primero y last es al final.", "Sé que she es ella y he es él."],
    [
        "Un cuento o una canción cuenta cosas en un orden. Las palabras de orden (sequence words) son first (primero), next (después), then (luego), after that (después de eso) y finally (finalmente). Finally marca lo último que pasa.",
        "En los textos de hoy verás acciones con she o he: wakes up (se despierta), brushes her teeth (se cepilla los dientes), eats breakfast (desayuna), packs her bag (guarda cosas en la mochila), walks (camina), kicks (patea), builds (construye) y finds (encuentra).",
        "Para ordenar una historia, busca las palabras de orden y escribe 1, 2, 3, 4. Piensa también en el sentido: un pájaro encuentra ramitas antes de construir un nido. Si dudas, vuelve a escuchar solo la palabra de orden que oíste.",
    ],
    [("first", "primero"), ("next", "después"), ("then", "luego"), ("after that", "después de eso"), ("finally", "finalmente"), ("wakes up", "se despierta"), ("walks", "camina"), ("finds", "encuentra")],
    [
        ("La primera acción", ADULT + "«First, Mia wakes up. Next, she brushes her teeth. After that, she eats breakfast. Then she packs her bag. Finally, she walks to school.» (breakfast = desayuno, school = escuela). ¿Qué hace Mia primero?", ["Busco la palabra first.", "Después de first oigo: Mia wakes up.", "Esa es la primera acción."], "Se despierta"),
        ("Qué viene después", "En el mismo cuento, ¿qué hace Mia justo después de desayunar?", ["Busco eats breakfast.", "La palabra siguiente es then.", "Then: packs her bag."], "Guarda sus cosas en la mochila"),
    ],
    [
        ("Pensar que Mia come antes de cepillarse los dientes porque el desayuno parece importante.", "Se ordena por importancia y no por las palabras de orden.", "Busca next y after that: el cepillado viene antes del desayuno."),
        ("Tomar finally como la primera acción porque aparece con un verbo conocido.", "No se reconoce la palabra de orden.", "Finally significa finalmente: es lo último que pasa."),
    ],
    [
        ("¿Qué palabra de orden marca lo último que pasa?", "finally", "Finally significa finalmente."),
        ("¿Qué significa «after that»?", "Después de eso", "After that une una acción con la anterior."),
        (ADULT + "«First, Mia wakes up. Next, she brushes her teeth. After that, she eats breakfast. Then she packs her bag. Finally, she walks to school.» ¿Qué hace Mia al final?", "Camina a la escuela", "Finally dice she walks to school."),
    ],
    [
        ("Lee: «First, Mia wakes up. Next, she brushes her teeth. After that, she eats breakfast. Then she packs her bag. Finally, she walks to school.» ¿Cuántas acciones hay en el cuento?", "5", "Wakes up, brushes, eats, packs y walks: cinco acciones."),
        ("¿Para qué sirven first, next, then y finally?", "Para decir en qué orden pasa cada cosa", "Son palabras de orden de una historia."),
        ("Lee: «First, Mia wakes up. Next, she brushes her teeth. After that, she eats breakfast. Then she packs her bag. Finally, she walks to school.» ¿Qué hace Mia justo antes de desayunar?", "Se cepilla los dientes", "Next dice she brushes her teeth, y after that viene el desayuno."),
    ],
    [
        (ADULT + "«First, Ben gets a ball. Next, he kicks the ball. After that, the ball goes into the net. Finally, Ben shouts hooray!» (gets = toma, kicks = patea, net = red, shouts = grita). ¿Qué pasa después de patear la pelota?", "La pelota entra en la red", "After that dice the ball goes into the net."),
        ("Lee: «First, Ben gets a ball. Next, he kicks the ball. After that, the ball goes into the net. Finally, Ben shouts hooray!» ¿Qué hace Ben al final?", "Grita hooray", "Finally dice Ben shouts hooray."),
        ("Lee: «First, Ben gets a ball. Next, he kicks the ball. After that, the ball goes into the net. Finally, Ben shouts hooray!» Ordena con letras: A) Ben grita. B) Ben patea la pelota. C) Ben toma la pelota. D) La pelota entra en la red.", "C, B, D, A", "El cuento sigue: toma, patea, entra, grita."),
    ],
    [
        ("Lucas dice que Mia desayuna antes de cepillarse los dientes. ¿Tiene razón?", "No; primero se cepilla los dientes", "Next dice que se cepilla; after that viene el desayuno."),
        (ADULT + "«First, a bird finds a stick. Next, it finds a leaf. After that, it builds a nest. Finally, the bird sleeps.» (stick = ramita, leaf = hoja, nest = nido). ¿Qué hace el pájaro justo antes de construir el nido?", "Encuentra una hoja", "Next dice it finds a leaf, y after that viene el nido."),
    ],
    [
        arith("Mia tiene 5 acciones en su cuento y Ben tiene 4 en el suyo. ¿Cuántas acciones hay en total entre los dos cuentos?", "5+4", "Se suman las acciones de los dos cuentos."),
        ("Cuento del pájaro: «First, a bird finds a stick. Next, it finds a leaf. After that, it builds a nest. Finally, the bird sleeps.» Ordena: A) Duerme. B) Construye el nido. C) Encuentra una hoja. D) Encuentra una ramita.", "D, C, B, A", "Primero ramita, luego hoja, luego nido y al final duerme."),
    ],
    [(ADULT + "En la clase cantan: «First I clap, next I jump, finally I sit.» (sit = me siento). ¿Qué haces al final?", "Me siento", "Finally dice que al final me siento.")],
    [
        ("¿Qué significa «first»?", "Primero", "First indica el comienzo del orden."),
        ("¿Qué significa «she walks»?", "Ella camina", "She es ella y walks es camina."),
        ("¿Qué te ayuda a ordenar una historia: el tamaño de las palabras o las palabras de orden?", "Las palabras de orden", "First, next, then, after that y finally indican el orden."),
    ],
    task("Un adulto lee dos veces este cuento: «First, Ben gets a ball. Next, he kicks the ball. After that, the ball goes into the net. Finally, Ben shouts hooray!» Dibuja cuatro cuadros numerados 1, 2, 3 y 4, uno por cada acción. Escribe debajo de cada uno la palabra de orden: first, next, after that o finally.", "1 first (toma la pelota), 2 next (patea), 3 after that (entra en la red), 4 finally (grita hooray).", ["dibuja las cuatro acciones en orden", "escribe la palabra de orden en cada cuadro", "el último cuadro muestra que Ben grita"], ["dibujos del estudiante", "nota del adulto"], ["poner finally antes de first", "no seguir el orden del cuento"], "Reconoce el orden correcto y vuelve a leer con él first y finally."),
    "Pide a un adulto que lea «First, Mia wakes up. Finally, she walks to school.» y muestra con las manos cuál va primero.",
    "Inventa un cuento de cuatro líneas con first, next, after that y finally sobre cómo te lavas las manos.",
)

lesson(
    OA1, 4,
    "Los diálogos escritos en cada ejercicio, que lee un adulto con voces distintas; lápiz y hoja para tapar el guion.",
    "Aprenderé a saber quién habla en un diálogo de dos o tres personas, qué dice cada una y quién pregunta o responde. Sirve para entender conversaciones en inglés.",
    ["Sé que en un diálogo cada persona habla por turnos.", "Sé decir hello, thank you y I'm happy."],
    [
        "Un diálogo (dialogue) es una conversación. Cada persona que habla es un speaker. Para saber quién habla, mira el nombre antes de los dos puntos, por ejemplo «Ana:». Cada cambio de nombre es un turno nuevo. Hoy hay diálogos con tres speakers.",
        "En los diálogos aparecen frases de uso muy frecuente. «This is my sister» significa «esta es mi hermana». «I'm nine» significa «tengo nueve años». «I want bread, please» significa «quiero pan, por favor». «Here!» significa «¡toma!» o «¡aquí está!». «Who has...?» significa «¿quién tiene...?».",
        "Una pregunta y su respuesta casi siempre las dicen speakers distintos. Para saber quién hace algo, busca su nombre y lee la frase que sigue. Cuenta los nombres distintos para saber cuántos speakers hay; no cuentes a quien lee en voz alta.",
    ],
    [("speaker", "persona que habla"), ("turn", "turno de habla"), ("This is my sister", "esta es mi hermana"), ("I'm nine", "tengo nueve años"), ("I want... please", "quiero... por favor"), ("Here!", "¡toma! / ¡aquí está!"), ("Who has...?", "¿quién tiene...?")],
    [
        ("Quién dice qué", ADULT + "«Ana: Hello, Tom! Tom: Hi, Ana! This is my sister, Eva. Eva: Hello, Ana. I'm nine. Ana: I'm nine, too!» (too = también). ¿Quién dice «This is my sister»?", ["Busco This is my sister.", "Antes de esa frase está el nombre Tom.", "Tom presenta a su hermana."], "Tom"),
        ("Contar speakers", "En el mismo diálogo, ¿cuántos speakers hay?", ["Busco los nombres antes de los dos puntos.", "Veo Ana, Tom y Eva.", "Son tres nombres distintos."], "3"),
    ],
    [
        ("Contar cuatro speakers porque hay cuatro turnos.", "Se cuentan los turnos y no los nombres distintos.", "Cuenta solo los nombres distintos: un mismo speaker puede hablar varias veces."),
        ("Pensar que quien presenta es la persona presentada.", "Se confunde This is con I'm.", "This is presenta a otra persona; I'm habla de quien está hablando."),
    ],
    [
        (ADULT + "«Cook: What do you want? Boy: I want bread, please. Cook: Here! Boy: Thank you.» (cook = cocinero o cocinera, boy = niño, What do you want? = ¿qué quieres?). ¿Quién dice «I want bread, please»?", "Boy", "El nombre Boy está antes de esa frase."),
        ("Lee: «Cook: What do you want? Boy: I want bread, please. Cook: Here! Boy: Thank you.» ¿Qué significa «Here!» en ese diálogo?", "¡Toma!", "Cook entrega el pan con Here!"),
        ("Lee: «Cook: What do you want? Boy: I want bread, please. Cook: Here! Boy: Thank you.» ¿Quién dice «Thank you»?", "Boy", "Boy agradece al final."),
    ],
    [
        ("¿Cómo sabes quién habla en un diálogo escrito?", "Por el nombre antes de los dos puntos", "Ese nombre dice quién habla en cada turno."),
        ("¿Qué significa «I'm nine»?", "Tengo nueve años", "I'm nine se usa para decir la edad."),
        (ADULT + "«Cook: What do you want? Boy: I want bread, please.» ¿Quién pregunta?", "Cook", "Cook hace la pregunta What do you want? y Boy responde."),
    ],
    [
        (ADULT + "«Teacher: Who has a ruler? Leo: I have a ruler. Mia: I have two pencils. Teacher: Great!» (ruler = regla, pencils = lápices, great = ¡excelente!). ¿Quién tiene una regla?", "Leo", "Leo dice «I have a ruler»."),
        (ADULT + "«Teacher: Who has a ruler? Leo: I have a ruler. Mia: I have two pencils. Teacher: Great!» ¿Cuántos lápices tiene Mia?", "2", "Mia dice «two pencils»."),
        (ADULT + "«Teacher: Who has a ruler? Leo: I have a ruler. Mia: I have two pencils. Teacher: Great!» ¿Quién hace la pregunta?", "Teacher", "Teacher dice «Who has a ruler?»."),
    ],
    [
        ("Lee: «Ana: Hello, Tom! Tom: Hi, Ana! This is my sister, Eva. Eva: Hello, Ana. I'm nine. Ana: I'm nine, too!» Un niño dice que Eva es la persona que presenta. ¿Tiene razón?", "No; Tom es quien presenta a Eva", "Tom dice «This is my sister, Eva»."),
        ("Lee: «Ana: Hello, Tom! Tom: Hi, Ana! This is my sister, Eva. Eva: Hello, Ana. I'm nine. Ana: I'm nine, too!» ¿Cuántos turnos y cuántos speakers hay?", "4 turnos y 3 speakers", "Hay cuatro turnos, pero Ana se repite: son tres nombres."),
    ],
    [
        ("Lee: «Ana: Hello, Tom! Tom: Hi, Ana! This is my sister, Eva. Eva: Hello, Ana. I'm nine. Ana: I'm nine, too!» ¿Qué speakers dicen que tienen nueve años?", "Eva y Ana", "Eva dice «I'm nine» y Ana dice «I'm nine, too»."),
        arith("Lee: «Teacher: Who has a ruler? Leo: I have a ruler. Mia: I have two pencils. Teacher: Great!» El diálogo tiene 4 turnos. Leo habla 1 vez y Mia habla 1 vez. ¿Cuántos turnos dice Teacher?", "4-1-1", "Se restan los turnos de Leo y de Mia al total."),
    ],
    [(ADULT + "En el patio, dos amigos hablan: «Sam: I want a ball, please. Lia: Here! Sam: Thank you, Lia.» (ball = pelota). ¿Quién entrega la pelota?", "Lia", "Lia dice Here! y Sam le da las gracias.")],
    [
        ("¿Cómo se dice «¿quién tiene...?» en inglés?", "Who has...?", "Who es quién y has es tiene."),
        ("¿Qué significa «speaker»?", "La persona que habla", "Speaker es quien dice cada turno."),
        (ADULT + "«Ana: Hello, Tom! Tom: Hi, Ana!» ¿Cuántos speakers hay?", "2", "Hablan Ana y Tom."),
    ],
    task("Un adulto lee con tres voces este diálogo: «Lia: Hello, Tom! Tom: Hi, Lia! This is my brother, Max. Max: Hello, Lia. I'm ten. Lia: I'm nine!» (brother = hermano, ten = diez). Escúchalo dos veces. Escribe los tres nombres de los speakers. Debajo de cada uno anota una frase que dice.", "Lia: Hello, Tom! / Tom: This is my brother, Max. / Max: I'm ten.", ["escribe Lia, Tom y Max", "anota una frase correcta bajo cada nombre", "no mezcla quién presenta y quién es presentado"], ["hoja con los nombres y frases", "nota del adulto"], ["atribuir This is my brother a Max", "escribir solo dos speakers"], "Reconoce lo que ubicó bien y vuelve a escuchar solo el turno donde se equivocó."),
    "Pide a un adulto que diga con dos voces «Hello» y «Hi» y señala quién saluda primero.",
    "Escribe un diálogo de cuatro turnos entre tú y dos amigos con Hello, This is my friend... e I'm nine.",
)

lesson(
    OA1, 5,
    "Cuatro textos cortos escritos en el enunciado (una rima, un chant, un cuento y un diálogo), que lee un adulto; lápiz y hoja para tapar el guion.",
    "Aprenderé a responder a un texto nuevo que escucho: reconozco qué tipo de texto es, busco palabras clave y respondo con una acción, una elección o una palabra. Sirve para entender textos nuevos sin conocer todas las palabras.",
    ["Sé reconocer sonidos que riman.", "Sé seguir acciones de un chant, ordenar un cuento y saber quién habla en un diálogo."],
    [
        "Cuando escuchas un texto nuevo, lo primero es saber qué tipo de texto es. Una rima repite sonidos al final de las líneas. Un chant tiene acciones y números. Un cuento o una canción tiene un orden con first, next, then y finally. Un diálogo tiene speakers que se turnan.",
        "Después busca las palabras clave, que son las que dicen qué pasa: una acción, un número, un nombre o un objeto. No necesitas entender todas las palabras. Hoy verás sleep (dormir), kitten (gatito), box (caja), lost (perdido), home (casa) y smile (sonreír).",
        "Por último, responde como pide la tarea: con una acción, eligiendo una opción o diciendo una palabra. Muestra qué palabra del texto te dio la pista. Si dudas, vuelve a escuchar solo esa parte del texto.",
    ],
    [("type of text", "tipo de texto"), ("key word", "palabra clave"), ("lost", "perdido"), ("kitten", "gatito"), ("home", "casa, hogar"), ("smile", "sonreír")],
    [
        ("Reconocer el tipo de texto", ADULT + "«Walk, walk, walk. Hop, hop, hop. Turn around. Stop!» (walk = caminar). ¿Es una rima, un chant o un diálogo?", ["Escucho acciones: walk, hop, turn around.", "No hay dos personas que se turnen.", "Las acciones se repiten con ritmo."], "Un chant"),
        ("Palabras clave de un cuento", ADULT + "«A kitten is lost. It is in a box. Lia finds the kitten. She takes it home. The kitten sleeps.» (finds = encuentra, takes = lleva). ¿Dónde está el gatito al comienzo?", ["Busco kitten is lost.", "Después oigo: in a box.", "La palabra clave es box."], "En una caja"),
    ],
    [
        ("Intentar traducir cada palabra antes de responder.", "Se pierde el hilo del texto.", "Busca las palabras clave y responde con lo que entendiste."),
        ("Responder sin mostrar qué palabra del texto te dio la pista.", "No se vuelve a la evidencia.", "Señala la palabra clave que apoya tu respuesta."),
    ],
    [
        (ADULT + "«The sun and the run. Fun, fun, fun!» ¿Es una rima o un chant? Piensa en los finales.", "Una rima", "Sun, run y fun terminan con el mismo sonido."),
        (ADULT + "«A kitten is lost. It is in a box. Lia finds the kitten. She takes it home. The kitten sleeps.» ¿Quién encuentra al gatito?", "Lia", "Lia finds the kitten."),
        (ADULT + "«A kitten is lost. It is in a box. Lia finds the kitten. She takes it home. The kitten sleeps.» ¿Adónde lleva Lia al gatito?", "A su casa", "Takes it home significa lo lleva a casa."),
    ],
    [
        ("¿Qué debes hacer primero al escuchar un texto nuevo?", "Reconocer qué tipo de texto es", "Así sabes qué pistas buscar."),
        ("¿Qué es una palabra clave?", "Una palabra que dice qué pasa en el texto", "Puede ser una acción, un número, un nombre o un objeto."),
        ("¿Tienes que entender cada palabra para responder?", "No, basta con las palabras clave", "Las palabras clave dan la información importante."),
    ],
    [
        (ADULT + "«Walk, walk, walk. Hop, hop, hop. Turn around. Stop!» ¿Qué haces cuando oyes stop?", "Me detengo", "Stop significa detenerse."),
        (ADULT + "«Leo: Hello, Ana! I want a pencil, please. Ana: Here! Leo: Thank you.» (pencil = lápiz). ¿Qué quiere Leo?", "Un lápiz", "Leo dice I want a pencil."),
        (ADULT + "«Leo: Hello, Ana! I want a pencil, please. Ana: Here! Leo: Thank you.» ¿Quién dice «Here!»?", "Ana", "Ana entrega el lápiz con Here!"),
    ],
    [
        (ADULT + "«Walk, walk, walk. Hop, hop, hop. Turn around. Stop!» ¿Qué haces después de dar saltitos?", "Giro", "Después de hop viene turn around."),
        ("Un niño dice que «The sun and the run. Fun, fun, fun!» es un diálogo porque tiene tres palabras fun. ¿Tiene razón?", "No; es una rima porque sun, run y fun suenan igual al final", "Un diálogo necesita speakers que se turnan; aquí no los hay."),
    ],
    [
        arith(ADULT + "«Walk, walk, walk. Hop, hop, hop. Turn around. Stop!» ¿Cuántos pasos y saltitos haces en total, sin girar?", "3+3", "Se suman los tres walk y los tres hop."),
        ("Texto: «A kitten is lost. It is in a box. Lia finds the kitten. She takes it home. The kitten sleeps.» Elige la frase que prueba que Lia ayudó al gatito: a) It is in a box b) She takes it home. ¿Cuál es?", "b", "Takes it home muestra que ella lo lleva a un lugar seguro."),
    ],
    [(ADULT + "En clase, escuchas un texto nuevo: «Lia: Hello, Tom! Tom: Hi, Lia! Lia: This is my kitten. Tom: Hello, kitten!» ¿Es una rima, un chant o un diálogo?", "Un diálogo", "Hablan Lia y Tom por turnos.")],
    [
        ("¿Cómo se dice «perdido» en inglés?", "lost", "Lost significa perdido."),
        ("¿Qué significa «home»?", "Casa", "Home es el lugar donde vives."),
        ("¿Qué tipo de texto repite sonidos al final de las líneas?", "Una rima", "La rima repite los sonidos finales."),
    ],
    task("Un adulto lee dos veces este texto: «Walk, walk, walk. Hop, hop, hop. Turn around. Stop!» Haz las acciones en el orden que oyes, en un espacio seguro. Luego di si es una rima, un chant o un diálogo y señala la palabra que te dio la pista (por ejemplo stop).", "Es un chant: la pista es que tiene acciones como walk, hop y stop.", ["hace las acciones en orden", "nombra el tipo de texto", "señala una palabra clave"], ["nota del adulto", "foto o video con permiso de la familia"], ["decir que es una rima", "no explicar la pista"], "Aplaude el orden correcto y repite con él las palabras walk y hop."),
    "Pide a un adulto que lea «Walk, walk, walk. Stop!» y haz las acciones.",
    "Escribe una rima de dos líneas que termine con sonido «ai», por ejemplo con sky y fly.",
)

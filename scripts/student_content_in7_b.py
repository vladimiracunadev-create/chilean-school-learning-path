"""Cuaderno del estudiante, 7.º básico Inglés (oficial): IN07 OA 11, comprensión de textos literarios.

Los textos en inglés son originales, breves y llevan glosario en español dentro del enunciado. Cada término se enseña
en la clase antes de usarlo. Sin audio externo: todo lo que hay que leer está escrito en el enunciado.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA = "IN07 OA 11"


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


# ============================================================ clase 1: entorno, personajes y sucesos
A1 = "Laura and her brother Sam walk through the forest at night. It is cold and very dark. Suddenly they hear a strange sound. It is only an owl! They laugh and walk home."
G1 = "(forest = bosque; suddenly = de pronto; strange = extraño; owl = búho)"
B1 = "Panel 1: Mia is in the kitchen. She is hungry. Panel 2: She opens the fridge. It is empty! Panel 3: Mia goes to the market and buys bread."
GB1 = "(fridge = refrigerador; empty = vacío; market = feria o mercado)"
P1 = "The sun goes down behind the hill, / The sea is calm, the night is still. / A little boat sails home with me, / Under the stars, so quiet and free."
GP1 = "(goes down = se pone; hill = colina; still = quieto; sails = navega; free = libre)"
D1 = "On Saturday, Pablo and Dani go to the lake with a small boat. The sky is grey. Dani wants to sail, but Pablo is afraid of the storm. They go back and play cards at home."
GD1 = "(lake = lago; sky = cielo; grey = gris; sail = navegar; afraid of = con miedo de; storm = tormenta)"

lesson(
    OA, 1,
    "Los textos, la tira cómica y el poema escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a encontrar en un texto literario quiénes son los personajes, dónde y cuándo ocurre todo y qué pasa al comienzo, en el desarrollo y al final. Sirve para entender un cuento, un poema o una tira cómica en inglés.",
    ["Sé leer oraciones simples en inglés con ayuda de un glosario.", "Conozco palabras como forest, house, night y morning."],
    [
        "Un texto literario es un texto que cuenta o imagina algo: un cuento breve, un poema, una canción, una tira cómica (comic strip) o una novela adaptada. Para entenderlo, busca primero los personajes (characters): las personas, animales o seres que actúan. Pregunta: ¿quién hace algo?",
        "El entorno (setting) es el lugar y el tiempo donde ocurre la historia: in the forest, at night, on a rainy Monday. La trama (plot) es lo que pasa, en tres partes: el inicio (beginning) presenta a los personajes y el lugar, el desarrollo (middle) trae un problema o una acción, y el final (end) cuenta cómo termina.",
        "Para no equivocarte, subraya pistas: los nombres son personajes, las palabras de lugar y de tiempo son el entorno, y los verbos (walk, open, buy) son acciones. Una oración como «It is cold» describe el entorno; «She opens the fridge» cuenta una acción. En una tira cómica cada cuadro se llama viñeta (panel).",
    ],
    [("character", "personaje"), ("setting", "entorno: lugar y tiempo"), ("plot", "trama: lo que pasa"), ("beginning / middle / end", "inicio / desarrollo / final"), ("comic strip", "tira cómica"), ("panel", "viñeta"), ("poem", "poema")],
    [
        ("Encontrar personaje, lugar y tiempo", "Texto: «Ana lives on a small island. One rainy Monday, she finds a blue bottle on the beach. Inside there is a map. She runs home to show her grandfather.» (island = isla; bottle = botella; map = mapa) ¿Quién es la protagonista, dónde ocurre y cuándo?",
         ["El nombre propio que actúa es Ana: es la protagonista.", "Las palabras de lugar son island y beach.", "La palabra de tiempo es «one rainy Monday»."], "Personaje: Ana. Lugar: una isla y su playa. Tiempo: un lunes lluvioso."),
        ("Ordenar inicio, desarrollo y final", "Texto: «Tom has a red kite. The wind is strong and the kite breaks. Tom and his sister fix it with paper and tape. Now the kite flies again.» (kite = volantín; breaks = se rompe; fix = arreglar) ¿Qué pasa al inicio, en el desarrollo y al final?",
         ["Inicio: se presenta a Tom con su volantín.", "Desarrollo: el volantín se rompe y lo arreglan.", "Final: el volantín vuela otra vez."], "Inicio: Tom tiene un volantín. Desarrollo: se rompe y lo arreglan. Final: vuela de nuevo."),
    ],
    [
        ("Confundir entorno con acción.", "Se piensa que todo lo que dice una oración es «lo que pasa».", "Pregunta si alguien hace algo (acción) o si la oración dice cómo es el lugar o el tiempo (entorno)."),
        ("Contar un animal que solo hace ruido como personaje principal.", "No se mira quién realmente actúa y mueve la historia.", "El personaje principal es quien hace las acciones importantes."),
    ],
    [
        (f"En una historia en inglés, ¿qué es el «setting» (entorno)? a) El lugar y el tiempo donde ocurre todo b) Lo que dicen los personajes", "a", "El setting responde dónde y cuándo ocurre la historia."),
        (f"Lee: «{A1}» {G1} ¿Quiénes caminan juntos? a) Laura y Sam b) Laura y el búho", "a", "Laura and her brother Sam son quienes caminan; el búho solo aparece al final."),
        (f"Lee: «{A1}» {G1} ¿Cuándo ocurre la escena? a) at night b) in the morning", "a", "El texto dice «at night», es decir, de noche."),
    ],
    [
        (f"Lee: «{A1}» {G1} ¿Dónde caminan los hermanos? a) in the forest b) at school", "a", "El texto dice «through the forest», o sea por el bosque."),
        (f"Lee: «{A1}» {G1} Ordena los sucesos con letras según ocurren: x) They hear a strange sound. y) They walk through the forest. z) They laugh and walk home. Escribe las tres letras en orden.", "y, x, z", "Primero caminan, luego oyen el sonido y al final se ríen y vuelven."),
        (f"Lee: «{A1}» {G1} La oración «It is cold and very dark.» es: a) entorno (cómo es el tiempo y el lugar) b) acción de un personaje", "a", "No dice que alguien haga algo; describe el lugar de noche."),
    ],
    [
        (f"Lee la tira: «{B1}» {GB1} ¿En qué viñeta cambia de lugar Mia? a) Panel 3 b) Panel 2", "a", "En el Panel 3 va al mercado; antes seguía en la cocina."),
        (f"Lee la tira: «{B1}» {GB1} ¿Qué oración cuenta el final? a) Mia is hungry b) Mia buys bread.", "b", "Comprar pan resuelve el problema y cierra la historia."),
        (f"Lee la tira: «{B1}» {GB1} Escribe el nombre del único personaje que actúa.", "Mia", "Solo Mia tiene acciones: abre el refrigerador y compra pan."),
    ],
    [
        (f"Lee el poema: «{P1}» {GP1} ¿Qué momento del día muestra? Opciones: evening (atardecer), morning (mañana).", "evening", "La primera línea dice que el sol se pone, así que es el atardecer o la noche."),
        (f"Lee el poema: «{P1}» {GP1} Un compañero dice que ocurre en un bosque. ¿Tiene razón? Responde sí o no y escribe una palabra del poema como prueba.", "No. Pruebas posibles: sea o boat", "El poema habla de mar y de un bote, no de árboles ni de un bosque."),
    ],
    [
        (f"Lee: «{D1}» {GD1} ¿Cuántos lugares distintos aparecen?", "2", "Aparecen el lago y la casa."),
        (f"Lee: «{D1}» {GD1} Elige la mejor prueba de que no es buen día para navegar: a) The sky is grey b) They have a small boat", "a", "El cielo gris y la tormenta muestran mal tiempo; tener un bote no lo prueba."),
    ],
    [(f"Tu profesora te da esta historia para llenar una ficha: «Fran and his dog Bruno are at the park on a sunny Sunday. Bruno runs after a ball.» (sunny = soleado; runs after = corre tras) En la ficha va «Setting». ¿Qué escribes? a) the park, a sunny Sunday b) Bruno runs after a ball", "a", "El setting es lugar y tiempo; correr tras la pelota es una acción.")],
    [
        ("¿Cuáles son las tres partes de la trama, en orden?", "Inicio, desarrollo y final", "La trama avanza desde la presentación hasta el cierre."),
        ("En «Sofia opens the window.», ¿qué hay: una acción o un entorno?", "Una acción", "El verbo opens muestra que un personaje hace algo."),
        ("¿Qué palabras en inglés te dicen el tiempo de una historia? a) at night, on Monday b) Laura, Sam", "a", "At night y on Monday dicen cuándo; Laura y Sam son personajes."),
    ],
    task("Lee esta tira: «Panel 1: Nico is at the bus stop at six o'clock. It is raining. Panel 2: His bus is late. Panel 3: A girl shares her umbrella and they talk.» (bus stop = paradero; late = atrasado; shares = comparte; umbrella = paraguas) En tu hoja arma una ficha con: personajes, lugar, tiempo, qué pasa en el inicio, en el desarrollo y en el final.", "Personajes: Nico y una niña. Lugar: el paradero. Tiempo: las seis, lloviendo. Inicio: Nico espera. Desarrollo: el bus llega tarde. Final: la niña comparte el paraguas.", ["identifica los dos personajes", "nombra lugar y tiempo con palabras del texto", "separa inicio, desarrollo y final"], ["ficha completa en la hoja"], ["poner una acción como si fuera el lugar", "mezclar el orden de las viñetas"], "Pide que señale con el dedo, en el texto, la palabra que justifica cada casilla."),
    "Copia las siete palabras de la tabla de vocabulario con su significado.",
    "Escribe tres oraciones en inglés sobre un cuento que conozcas: una con el personaje, una con el lugar y una con el final.",
)

# ============================================================ clase 2: conflicto y respuesta
C2A = "Carlos loses his umbrella on a rainy day. He is wet and cold. A girl shares her umbrella with him. They walk to school together."
GC2A = "(loses = pierde; wet = mojado; shares = comparte)"
C2B = "Rafa wants to win the swimming race, but he is slow. He practises every day for a month. In the end, he is third. He feels proud."
GC2B = "(race = carrera; slow = lento; practises = practica; third = tercero; proud = orgulloso)"
C2C = "My kite is stuck in the old oak tree, / I cannot reach it, and I'm sad. / My neighbour brings a ladder to me, / Now we both fly it and I'm glad."
GC2C = "(stuck = atascado; oak tree = roble; reach = alcanzar; ladder = escalera; glad = contento)"
C2D = "The class has only one computer, but five students need it for a project. They make a list with times. Each student has a turn."
GC2D = "(only = solo; need = necesitan; turn = turno)"

lesson(
    OA, 2,
    "Los textos y el poema escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a reconocer el conflicto de una historia y la respuesta del personaje. Sirve para entender por qué pasa lo que pasa en un cuento, una tira cómica o un poema.",
    ["Sé identificar personajes, lugar, tiempo e inicio, desarrollo y final.", "Entiendo palabras como but, because y so."],
    [
        "El conflicto (conflict) es el problema que enfrenta un personaje: pierde algo, tiene miedo, quiere algo que no puede conseguir. Casi siempre aparece en el desarrollo de la historia. Palabras que ayudan a verlo son but (pero), cannot (no puede), lost (perdido), afraid (con miedo) y problem (problema).",
        "La respuesta (response) es lo que el personaje hace o decide frente al problema: pide ayuda (asks for help), practica (practises), busca otra solución (finds another way) o se rinde (gives up). Después viene el resultado (result): cómo termina todo. La respuesta y el resultado no son lo mismo: Rafa practica (respuesta) y queda tercero (resultado).",
        "Una buena forma de anotarlo es con tres casillas: Problem → Response → Result. Lee el texto, busca la palabra but o la oración que muestra un obstáculo, y luego pregunta: ¿qué hace el personaje? ¿cómo termina? Así sigues la historia sin inventar nada que no esté escrito.",
    ],
    [("conflict / problem", "conflicto / problema"), ("response", "respuesta del personaje"), ("result", "resultado"), ("but", "pero"), ("ask for help", "pedir ayuda"), ("practise", "practicar"), ("give up", "rendirse")],
    [
        ("Anotar problema, respuesta y resultado", "Texto: «Elena wants to join the school choir, but she is shy. She practises at home with her cat. On Friday she sings in front of the class and everyone claps.» (choir = coro; shy = tímida; claps = aplauden) ¿Cuál es el problema, la respuesta y el resultado?",
         ["La palabra but señala el problema: Elena es tímida.", "Lo que hace es practicar en casa con su gato.", "El resultado es que canta frente al curso y todos aplauden."], "Problema: es tímida. Respuesta: practica en casa. Resultado: canta y la aplauden."),
        ("Distinguir respuesta de resultado", "Texto: «Leo's bike has a flat tyre. He cannot go to the match. He asks his uncle for help and they fix it together.» (flat tyre = rueda pinchada; match = partido; fix = arreglar) ¿Qué es «asks his uncle for help»: respuesta o resultado?",
         ["Pedir ayuda es algo que Leo decide hacer.", "Lo que se decide hacer frente a un problema es la respuesta.", "El resultado sería que la bicicleta queda arreglada."], "Es la respuesta de Leo al problema."),
    ],
    [
        ("Decir que el problema es lo que pasa al final.", "Se confunde el conflicto con el resultado.", "El conflicto aparece antes; el final cuenta cómo se resuelve o qué queda."),
        ("Creer que toda respuesta resuelve el problema.", "Se piensa que el personaje siempre gana.", "Lee el final: a veces la respuesta no logra lo que el personaje quería, como el tercer lugar de Rafa."),
    ],
    [
        (f"Lee: «{C2A}» {GC2A} ¿Cuál es el problema de Carlos? a) Pierde su paraguas en un día de lluvia b) Llega temprano al colegio", "a", "El texto dice que loses his umbrella on a rainy day."),
        (f"Lee: «{C2A}» {GC2A} ¿Qué hace la niña? a) Comparte su paraguas b) Compra un paraguas", "a", "Shares her umbrella significa que lo comparte con Carlos."),
        ("¿Qué significa «give up»?", "Rendirse", "Es dejar de intentar cuando algo es difícil."),
    ],
    [
        (f"Lee: «{C2B}» {GC2B} ¿Qué palabra del texto anuncia el problema de Rafa? Opciones: but, every.", "but", "But introduce la dificultad: quiere ganar, pero es lento."),
        (f"Lee: «{C2B}» {GC2B} Rafa practica todos los días. Eso es: a) la respuesta b) el resultado", "a", "Practicar es lo que él decide hacer frente al problema."),
        (f"Lee: «{C2B}» {GC2B} ¿Cuál es el resultado? a) He is third and feels proud b) He is slow.", "a", "Termina tercero y orgulloso; ser lento era el problema."),
    ],
    [
        (f"Lee el poema: «{C2C}» {GC2C} ¿Cuál es el problema de la voz que habla? Opciones: the kite is stuck, the kite is red.", "the kite is stuck", "El volantín atascado en el árbol es lo que lo entristece."),
        (f"Lee el poema: «{C2C}» {GC2C} ¿Quién ayuda y con qué? Escribe en español.", "El vecino, con una escalera", "My neighbour brings a ladder resuelve el problema."),
        (f"Lee: «{C2D}» {GC2D} ¿Qué hacen los estudiantes ante el problema? a) Hacen una lista con turnos b) Los cinco usan el computador a la vez", "a", "They make a list with times es su respuesta; el texto no habla de comprar nada."),
    ],
    [
        ("Ines tiene miedo de hablar en clase. Respuesta 1: se queda en casa ese día. Respuesta 2: practica con una amiga. ¿Cuál enfrenta el problema? Escribe 1 o 2.", "2", "Practicar con una amiga trabaja el miedo; quedarse en casa lo evita."),
        (f"Lee: «{C2A}» {GC2A} Si la niña no hubiera compartido su paraguas, ¿qué parte de la historia cambiaría? a) El resultado b) El lugar", "a", "Sin la ayuda, Carlos seguiría mojado: cambia cómo termina."),
    ],
    [
        ("Texto: «Mateo is afraid of the dark, but he must get his book from the garden. He takes a small torch and walks slowly. He finds the book and smiles.» (torch = linterna; must = debe) Elige el esquema correcto. a) Problema: miedo a la oscuridad. Respuesta: lleva una linterna. Resultado: encuentra el libro b) Problema: el libro. Respuesta: sonríe. Resultado: miedo", "a", "El miedo es el conflicto, la linterna es la respuesta y encontrar el libro es el resultado."),
        ("Texto: «Dina wants to bake a cake, but she has no eggs. She goes to the neighbour and asks for two eggs.» (bake = hornear; eggs = huevos) Escribe en español cuál es su respuesta.", "Va donde la vecina y le pide dos huevos", "Esa acción es lo que hace Dina frente a la falta de huevos."),
    ],
    [(f"En una tira cómica, un niño dice: «I lost my pencil case!» En la viñeta siguiente pregunta a su compañera: «Can you lend me a pen?» (lost = perdí; lend = prestar) ¿Cuál es la respuesta del niño al problema? a) Pide un lápiz prestado b) Pierde su estuche", "a", "Pedir prestado es lo que hace ante el problema; perder el estuche es el problema.")],
    [
        ("¿Qué es el conflicto de una historia?", "El problema que enfrenta un personaje", "Es la dificultad que mueve la trama."),
        ("¿Qué es la respuesta del personaje?", "Lo que hace o decide frente al problema", "Va después del conflicto y antes del resultado."),
        ("En «Tina cannot find her keys, so she looks under the sofa.», ¿qué es «she looks under the sofa»? a) la respuesta b) el problema", "a", "Buscar bajo el sofá es lo que Tina hace ante el problema."),
    ],
    task("Lee: «Gabi is the new student. She does not know anyone, so she eats alone. One day, a boy asks, 'Do you want to play cards?' Now they are friends.» (new = nueva; alone = sola; cards = naipes) Completa en tu hoja tres casillas: Problema, Respuesta de los personajes y Resultado. Luego escribe qué habría pasado si el niño no hubiera preguntado nada.", "Problema: Gabi no conoce a nadie. Respuesta: el niño la invita a jugar. Resultado: son amigos. Si no preguntaba, ella seguiría sola.", ["separa problema, respuesta y resultado", "usa datos del texto", "explica un cambio posible sin contradecir el texto"], ["tres casillas completas y una oración final"], ["poner el resultado como problema", "inventar sucesos que el texto no dice"], "Pregunta qué palabra del texto le mostró el problema."),
    "Copia las tres casillas Problem, Response y Result y escribe debajo de cada una la frase que la explica.",
    "Inventa un problema de un personaje con la palabra but y escribe dos respuestas posibles distintas.",
)

# ============================================================ clase 3: sonido, imagen y humor
S3A = "Rain, rain, falling down / On the roof and on the town. / Rain, rain, sing for me / A little song of the sea."
GS3A = "(roof = techo; town = pueblo)"
H3A = "Panel 1: A boy says, 'I will study all night!' Panel 2: The boy is asleep on his book. Text: 'Zzz'."
GH3A = "(study = estudiar; asleep = dormido)"
H3B = "Panel 1: Dad asks, 'Where are my glasses?' Panel 2: The glasses are on his head."
GH3B = "(glasses = lentes; head = cabeza)"
S3C = "The bee goes buzz, buzz, buzz. The clock goes tick, tock, tick. The door goes bang! And the cat goes meow."
GS3C = "(bee = abeja; clock = reloj; door = puerta)"

lesson(
    OA, 3,
    "Los poemas, las tiras y los textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a notar la rima, las repeticiones, las palabras que imitan sonidos, las imágenes y el humor de un texto literario. Sirve para entender cómo un poema o una tira cómica transmiten lo que quieren decir.",
    ["Sé reconocer personajes y entorno en un texto.", "Conozco las palabras cat, hat, sea, tree y night."],
    [
        "Los poemas y las canciones juegan con el sonido. La rima (rhyme) ocurre cuando dos palabras terminan con el mismo sonido: cat y hat, tree y sea, night y light. Al final de las líneas de un poema suele haber palabras que riman. La repetición (repetition) es decir la misma palabra o frase varias veces, como «Rain, rain», para dar ritmo.",
        "Algunas palabras imitan sonidos: buzz (zumbido), bang (golpe), splash (chapoteo), meow (miau). Se llaman palabras de sonido (sound words). Ayudan a imaginar lo que se oye. En una tira cómica, además, la imagen cuenta mucho: la viñeta (panel), los globos de diálogo (speech bubbles) y las caras de los personajes muestran sentimientos y acciones.",
        "El humor (humour) suele nacer de una sorpresa: un personaje dice una cosa y hace otra, o busca algo que ya tiene encima. Para explicarlo, pregunta: ¿qué esperaba el lector? ¿qué pasó de verdad? La diferencia entre las dos cosas es el chiste. Una broma se explica con pruebas del texto y de la imagen, no con «me dio risa».",
    ],
    [("rhyme", "rima"), ("repetition", "repetición"), ("sound word", "palabra que imita un sonido"), ("panel", "viñeta"), ("speech bubble", "globo de diálogo"), ("humour", "humor"), ("surprise", "sorpresa")],
    [
        ("Encontrar rimas y repeticiones", "Poema: «Sun, sun, shining bright / Warm my hands and make them light. / Sun, sun, shining free / Over hill and over sea.» (shining = brillando; bright = brillante) ¿Qué palabras riman al final y cuál se repite?",
         ["Mira las últimas palabras de cada línea: bright, light, free, sea.", "Bright rima con light, y free rima con sea.", "La palabra «Sun» se repite al inicio de dos líneas."], "Riman bright con light y free con sea; se repite «Sun, sun»."),
        ("Explicar un chiste con la imagen", "Tira: «Panel 1: A girl says, 'I am never late!' Panel 2: The clock shows ten o'clock and the girl runs to school with a sleepy face.» (never = nunca; late = atrasada; sleepy = con sueño) ¿Por qué tiene humor?",
         ["Primero dice que nunca llega tarde.", "Después se ve que llega tarde y corriendo.", "El humor está en la diferencia entre lo que dice y lo que hace."], "Dice que nunca llega tarde, pero la viñeta la muestra corriendo atrasada."),
    ],
    [
        ("Decir que dos palabras riman porque empiezan igual.", "Se mira el comienzo y no el final del sonido.", "Las rimas se oyen al final: cat y hat riman; cat y cow no."),
        ("Explicar el chiste solo con «es gracioso».", "No se buscan pruebas en el texto o la imagen.", "Señala qué se esperaba y qué ocurrió en realidad."),
    ],
    [
        ("¿Qué pareja de palabras rima? a) cat - hat b) cat - dog", "a", "Cat y hat terminan con el mismo sonido."),
        (f"Lee: «{S3C}» {GS3C} ¿Cuál es una palabra de sonido? a) buzz b) clock", "a", "Buzz imita el zumbido de una abeja."),
        ("¿Qué es una repetición en un poema?", "Decir la misma palabra o frase varias veces", "Sirve para dar ritmo."),
    ],
    [
        (f"Lee: «{S3A}» {GS3A} ¿Qué palabra se repite al principio de dos líneas? Opciones: Rain, sea.", "Rain", "Rain, rain abre las líneas 1 y 3."),
        (f"Lee: «{S3A}» {GS3A} ¿Qué pareja rima al final de las líneas 1 y 2? a) down - town b) roof - sea", "a", "Down y town terminan con el mismo sonido."),
        (f"Lee la tira: «{H3A}» {GH3A} ¿Qué dice el niño que hará? a) Estudiar toda la noche b) Salir a jugar", "a", "Dice «I will study all night»."),
    ],
    [
        (f"Lee la tira: «{H3A}» {GH3A} ¿Qué muestra la segunda viñeta? a) El niño dormido sobre el libro b) El niño estudiando feliz", "a", "La imagen muestra que se queda dormido, lo contrario de lo prometido."),
        (f"Lee la tira: «{H3B}» {GH3B} ¿Dónde estaban los lentes? Escribe en español.", "En su cabeza", "La segunda viñeta lo muestra: on his head."),
        (f"Lee: «{S3C}» {GS3C} ¿Cuántas palabras de sonido hay entre buzz, tick, tock, bang, meow y clock? Cuenta solo las que imitan sonidos.", "5", "Buzz, tick, tock, bang y meow imitan sonidos; clock nombra un objeto."),
    ],
    [
        (f"Lee la tira: «{H3B}» {GH3B} ¿Qué lo hace gracioso? a) Busca algo que ya tiene puesto b) Pierde sus lentes en el mar", "a", "Las dos viñetas contrastan lo que pregunta con la imagen final."),
        ("Un compañero dice que «bright - light» no riman porque tienen distinta primera letra. ¿Está en lo correcto? Responde sí o no.", "No", "La rima depende del sonido final: ight en ambas."),
    ],
    [
        ("Poema: «My dog is big, my dog is sweet, / He runs so fast on four small feet. / My dog is big, my dog is kind, / A better friend I cannot find.» (sweet = dulce; kind = bondadoso) ¿Cuál es la frase que se repite?", "My dog is big", "Abre las líneas 1 y 3 del poema."),
        ("Mismo poema: «My dog is big, my dog is sweet, / He runs so fast on four small feet. / My dog is big, my dog is kind, / A better friend I cannot find.» ¿Qué palabras riman en las líneas 3 y 4? a) kind - find b) big - kind", "a", "Kind y find tienen el mismo sonido final."),
    ],
    [("En una tira, un niño dice con cara seria: «Today I will not eat any sweets!» En la viñeta siguiente aparece con la boca llena de caramelos. (sweets = dulces) ¿Qué produce el humor? a) La diferencia entre lo que dice y lo que hace b) El lugar donde está", "a", "Promete no comer y la imagen muestra lo contrario, esa sorpresa es el chiste.")],
    [
        ("¿Qué es la rima?", "Que dos palabras terminan con el mismo sonido", "Se oye al final de las palabras."),
        ("¿Qué nombre tiene un cuadro de una tira cómica?", "Viñeta (panel)", "Cada cuadro muestra un momento."),
        ("¿Qué palabra imita el sonido de una puerta que se cierra fuerte? a) bang b) night", "a", "Bang imita un golpe."),
    ],
    task("Lee este poema: «Little frog on a green leaf, / Jump, jump, jump! / Little frog, no more grief, / Splash! Into the pond.» (frog = rana; leaf = hoja; grief = pena; pond = estanque) En tu hoja escribe: a) la palabra que rima con leaf, b) la palabra que se repite tres veces seguidas, c) la palabra de sonido, d) una oración que explique qué imagen ves al leerlo.", "a) grief. b) jump. c) splash. d) Veo una rana que salta de una hoja a un estanque.", ["encuentra las tres pistas de sonido", "su oración describe una imagen coherente con el poema", "usa palabras del texto"], ["hoja con cuatro respuestas"], ["tomar la primera letra como criterio de rima", "describir algo que el poema no dice"], "Pide que lea el poema en voz alta marcando el ritmo con la mano."),
    "Escribe tres pares de palabras que rimen, como cat y hat, y marca el sonido final.",
    "Escribe dos líneas de poema en inglés con una rima y una palabra de sonido, por ejemplo rain y train.",
)

# ============================================================ clase 4: inferir el tema con cautela
T4A = "Lila and Omar find a wallet with money on the street. They want to buy ice cream, but they take the wallet to their teacher. The owner thanks them with a smile."
GT4A = "(wallet = billetera; owner = dueño; thanks = agradece)"
T4B = "Five children want to move a long wooden table to the garden. One child alone cannot do it. They lift it together and walk slowly. Soon the table is under the tree."
GT4B = "(lift = levantar; wooden = de madera; slowly = despacio)"
T4C = "Sofia is afraid of the dark. A little lamb is lost in the barn at night. Sofia takes a lamp and goes in. She finds the lamb and carries it home."
GT4C = "(lamb = cordero; barn = establo; lamp = lámpara; carries = lleva en brazos)"
T4D = "A small ant carries a big seed. Some animals laugh at it. Day after day, the ant keeps trying. At last, the seed is in its home."
GT4D = "(ant = hormiga; seed = semilla; keeps trying = sigue intentando; at last = por fin)"

lesson(
    OA, 4,
    "Los textos breves escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a deducir el tema de un texto literario con cuidado, usando pistas del propio texto. Sirve para entender qué idea general quiere mostrar un cuento o un poema.",
    ["Sé reconocer problema, respuesta y resultado.", "Conozco palabras como friend, help y try."],
    [
        "El tema (theme) es la idea general de un texto literario: lo que la historia nos hace pensar. Se dice con una palabra o una frase corta: honesty (honestidad), friendship (amistad), teamwork (trabajo en equipo), courage (valentía), kindness (amabilidad), keep trying (seguir intentando). El tema no es lo que pasa, sino la idea que está detrás de lo que pasa.",
        "Para inferir (deducir) el tema con cautela, usa tres pasos: 1) lee y anota qué hace el personaje y cómo termina, 2) busca dos pistas del texto que apunten a la misma idea, 3) escribe el tema en una frase corta y comprueba que no contradice ninguna parte. Si no hay pistas que lo apoyen, no es un buen tema.",
        "Cuidado: una historia puede tener más de una lectura posible, pero cada lectura necesita pruebas. «A boy loses a ball» es un resumen de la trama, no un tema. «Friends help each other» sí es un tema. Cuando alguien propone un tema, pregúntale: ¿qué dos oraciones del texto lo apoyan?",
    ],
    [("theme", "tema: idea general"), ("infer", "deducir con pistas"), ("evidence", "evidencia: prueba del texto"), ("honesty", "honestidad"), ("teamwork", "trabajo en equipo"), ("courage", "valentía"), ("kindness", "amabilidad")],
    [
        ("Deducir el tema con dos pistas", "Texto: «Mia finds a lost kitten. She puts up a note on the street. Two days later, the owner arrives and Mia gives the kitten back.» (kitten = gatito; owner = dueño; gives back = devuelve) ¿Qué tema se puede deducir y qué dos pistas lo apoyan?",
         ["Mia no se queda con el gatito: lo devuelve.", "Pistas: pone un aviso y entrega el gatito a su dueño.", "Ambas apuntan a ser honesta y amable."], "Tema: honestidad y amabilidad. Pistas: puso un aviso y devolvió el gatito."),
        ("Separar resumen de tema", "¿Cuál de estas dos frases es un tema: a) Two boys lose a ball in the river. b) Never give up. (Texto sobre Ben, que cae tres veces andando en bicicleta y a la cuarta lo logra.)",
         ["La primera cuenta un suceso: es trama.", "La segunda es una idea que sirve para muchas historias.", "Además calza con Ben, que sigue intentando."], "La frase b) es un tema; la a) es un resumen de la trama."),
    ],
    [
        ("Elegir un tema porque «suena bonito».", "No se buscan pruebas en el texto.", "Anota dos oraciones del texto que apoyen el tema."),
        ("Pensar que hay un único tema correcto y que todos deben coincidir.", "Se olvida que un texto permite varias lecturas con pruebas.", "Acepta otro tema si tiene evidencia clara; rechaza el que contradice el texto."),
    ],
    [
        ("¿Qué es el tema de un texto literario?", "La idea general que muestra", "No es un suceso, es lo que la historia nos hace pensar."),
        (f"Lee: «{T4A}» {GT4A} ¿Qué hacen Lila y Omar con la billetera? a) La llevan a su profesora b) Compran helados con el dinero", "a", "Dice que take the wallet to their teacher."),
        ("«Teamwork» significa: a) trabajo en equipo b) valentía", "a", "Teamwork es hacer algo entre varias personas."),
    ],
    [
        (f"Lee: «{T4A}» {GT4A} ¿Qué tema calza mejor? a) honesty b) bad luck", "a", "Devolver lo que no es suyo, aunque quieran helados, muestra honestidad."),
        (f"Lee: «{T4B}» {GT4B} ¿Qué tema calza mejor? a) teamwork b) competition", "a", "Un niño solo no puede, pero juntos sí: trabajo en equipo."),
        (f"Lee: «{T4C}» {GT4C} ¿Qué tema calza mejor? a) courage b) fear", "a", "Sofía tiene miedo, pero entra a buscar al cordero: valentía."),
    ],
    [
        (f"Lee: «{T4B}» {GT4B} ¿Qué oración apoya el tema teamwork? a) One child alone cannot do it b) The table is wooden.", "a", "Muestra que se necesita al grupo; la madera no tiene que ver con el tema."),
        (f"Lee: «{T4C}» {GT4C} ¿Qué oración muestra el miedo de Sofía? Opciones: Sofia is afraid of the dark, She finds the lamb.", "Sofia is afraid of the dark", "Esa oración dice directamente que tiene miedo."),
        (f"Lee: «{T4D}» {GT4D} Escribe en español una frase corta que sea el tema.", "Seguir intentando aunque se rían de uno", "La hormiga insiste día tras día hasta lograrlo."),
    ],
    [
        (f"Lee: «{T4D}» {GT4D} Un compañero dice que el tema es «the ant is small». ¿Es un buen tema? Responde sí o no.", "No", "Describe a la hormiga, pero no es una idea que la historia haga pensar."),
        (f"Lee: «{T4A}» {GT4A} ¿Qué pista contradice que el tema sea «greed» (avaricia)? a) They take the wallet to their teacher b) They are on the street.", "a", "Entregar la billetera muestra lo contrario a quedarse con el dinero."),
    ],
    [
        (f"Lee: «{T4C}» {GT4C} Un compañero propone el tema «friendship». ¿Hay pistas del texto que lo apoyen? Responde sí o no.", "No", "El texto no menciona amigos: habla de miedo y de ayudar a un cordero."),
        ("Texto: «Ruth shares her lunch with a new classmate who forgot his food. The next day, he brings fruit for both.» (shares = comparte; forgot = olvidó; fruit = fruta) Elige el tema mejor apoyado: a) kindness b) jealousy", "a", "Compartir y devolver el gesto muestra amabilidad."),
    ],
    [("Una profesora lee este texto: «Alex finds a ten-thousand-peso note in the library. He gives it to the librarian. She puts a sign on the door: 'Lost money. Ask here.' The next day, a girl comes and thanks him.» (note = billete; librarian = bibliotecaria; sign = letrero; lost = perdido) En tu cuaderno escribes el tema. ¿Cuál es el mejor? a) honesty b) selfishness", "a", "Entregar el billete en vez de guardarlo muestra honestidad.")],
    [
        ("¿Cuántas pistas conviene dar para apoyar un tema?", "Al menos dos del texto", "Dos pistas que apuntan a lo mismo hacen la lectura más segura."),
        ("«A girl loses her hat» ¿es un tema o un resumen de la trama?", "Un resumen de la trama", "Cuenta un suceso, no una idea general."),
        ("¿Qué significa «courage»? a) valentía b) honestidad", "a", "Courage es la fuerza para enfrentar el miedo."),
    ],
    task("Lee: «Bruno the bear cannot climb the hill with his heavy bag. A small fox sees him and carries half of the bag. At the top, Bruno shares his berries with the fox.» (bear = oso; heavy = pesado; fox = zorro; berries = frutillas silvestres; top = cima) En tu hoja escribe: a) el tema en una frase corta, b) dos oraciones del texto que lo apoyen, c) una razón por la que otro tema, como «greed», no calza.", "a) Ayudarse entre sí. b) A small fox carries half of the bag; Bruno shares his berries. c) Bruno comparte, no se queda con todo.", ["el tema es una idea y no un resumen", "cita dos oraciones del texto", "explica por qué rechaza otro tema"], ["hoja con a), b) y c)"], ["escribir un resumen en vez de un tema", "dar un tema sin pruebas"], "Pregunta qué cambiaría en el tema si el zorro no ayudara."),
    "Copia las cuatro frases de tema de la explicación con su significado.",
    "Escribe un cuento de cuatro oraciones en inglés cuyo tema sea kindness y subraya las dos oraciones que lo muestran.",
)

# ============================================================ clase 5: comparar dos formas literarias
ST5 = "Marta's balloon is red. The wind takes it away. Marta runs after it through the park, but she cannot catch it. At the end, she sees the balloon on a tree and a boy gives it back."
GST5 = "(balloon = globo; wind = viento; catch = atrapar; gives back = devuelve)"
PO5 = "Red balloon, red balloon, / Flying high above the moon, / Wind says: 'Come and play with me!' / Then it sits in a tree."
GPO5 = "(flying = volando; above = sobre; sits = se posa)"
CO5 = "Panel 1: Marta holds a red balloon. Panel 2: The wind blows. The balloon is in the sky. 'Oh no!' Panel 3: A boy gives the balloon back. 'Thank you!'"
GCO5 = "(holds = sostiene; blows = sopla)"

lesson(
    OA, 5,
    "El cuento, el poema y la tira escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a comparar un cuento, un poema y una tira cómica que tratan el mismo asunto. Sirve para ver qué muestra cada forma y qué idea comparten.",
    ["Sé reconocer personajes, entorno, trama, rima y humor.", "Sé deducir un tema con dos pistas."],
    [
        "Una misma idea puede contarse de varias formas. El cuento (short story) usa párrafos y narra con oraciones completas. El poema (poem) usa líneas llamadas versos, a veces con rima y repetición, y dice mucho con pocas palabras. La tira cómica (comic strip) usa viñetas, imágenes y globos de diálogo, y muestra acciones con dibujos.",
        "Para comparar, mira los mismos elementos en cada texto: personajes, entorno, qué pasa y qué tema aparece. Luego anota qué cambia: el cuento da más detalles, el poema da más sonido e imágenes en pocas líneas, y la tira cómica muestra las emociones con la cara y el dibujo. Dos textos pueden compartir el tema aunque sean muy distintos.",
        "Al comparar usa palabras como both (ambos), but (pero), however (sin embargo) y different (distinto). Por ejemplo: «Both texts have a red balloon, but the story tells more events than the poem.» Siempre apoya lo que dices con una pista concreta de cada texto.",
    ],
    [("short story", "cuento breve"), ("verse", "verso: línea de un poema"), ("compare", "comparar"), ("both", "ambos"), ("different", "distinto"), ("similar", "parecido"), ("however", "sin embargo")],
    [
        ("Comparar dos formas", "Dos textos sobre una lluvia. Cuento: «It rains all Sunday. Pili stays at home and reads three books. In the evening, the sun comes out.» Poema: «Rain, rain on my window, / Tap, tap, tap, tap. / Stay inside and read a story / On this rainy Sunday nap.» (tap = golpecito; nap = siesta) ¿Qué tienen en común y qué cambia?",
         ["Ambos ocurren un domingo de lluvia y alguien se queda adentro.", "El cuento cuenta sucesos en orden (llueve, lee, sale el sol).", "El poema usa rima (tap - nap) y una palabra de sonido (tap)."], "Comparten el domingo lluvioso; cambia que el cuento narra sucesos y el poema usa sonido y rima."),
        ("Reconocer la forma por sus rasgos", "¿Qué forma es? «Panel 1: A cat sits on a box. Panel 2: The box breaks. 'Meow!' Panel 3: The cat sits on the floor.» Opciones: tira cómica, poema.",
         ["Hay paneles numerados.", "Hay diálogo con exclamación y dibujo que se describe.", "Eso es propio de una tira cómica."], "Tira cómica"),
    ],
    [
        ("Pensar que dos formas distintas no pueden tener el mismo tema.", "Se mira solo la apariencia del texto.", "Compara personajes, suceso y tema: pueden coincidir aunque la forma cambie."),
        ("Comparar sin dar pruebas.", "Se dice «es parecido» sin citar nada.", "Cita una palabra o una viñeta de cada texto."),
    ],
    [
        (f"Lee: «{CO5}» {GCO5} ¿Qué forma literaria es? a) Tira cómica b) Poema", "a", "Tiene viñetas y globos de diálogo."),
        (f"Lee: «{PO5}» {GPO5} ¿Cómo se llaman las líneas de un poema? a) Versos b) Viñetas", "a", "Los versos son las líneas de un poema."),
        ("En Inglés (oficial): ¿Qué significa «both»?", "Ambos", "Se usa para hablar de dos cosas a la vez."),
    ],
    [
        (f"Lee: «{ST5}» {GST5} ¿Quién devuelve el globo? a) A boy b) The wind", "a", "El texto dice que un niño lo devuelve; el viento se lo llevó."),
        (f"Lee: «{PO5}» {GPO5} ¿Qué dos palabras riman en los versos 1 y 2? a) balloon - moon b) high - tree", "a", "Balloon y moon terminan con el mismo sonido."),
        (f"Lee: «{CO5}» {GCO5} ¿Cuántas viñetas hay?", "3", "El texto numera Panel 1, Panel 2 y Panel 3."),
    ],
    [
        (f"Lee el cuento: «{ST5}» {GST5} y la tira: «{CO5}» ¿Qué tienen en común? a) El globo rojo y el viento b) El parque y el árbol", "a", "En ambos aparece un globo rojo y el viento lo aleja."),
        (f"Compara: cuento «{ST5}» y poema «{PO5}» ¿Cuál menciona un árbol? a) Ambos b) Ninguno", "a", "El cuento dice «on a tree» y el poema dice «in a tree»."),
        (f"Lee el cuento: «{ST5}» y el poema: «{PO5}» ¿Cuál muestra que Marta corre tras el globo? a) El cuento b) El poema", "a", "Solo el cuento dice que Marta runs after it."),
    ],
    [
        (f"Lee: «{CO5}» {GCO5} y el cuento «{ST5}» ¿Qué muestra mejor la tira? a) La emoción del momento con el 'Oh no!' b) Todos los pasos de la búsqueda", "a", "El globo de diálogo expresa la sorpresa; el cuento da más pasos."),
        ("Un compañero dice: «El poema del globo no tiene personajes.» Mira el poema: «Red balloon, red balloon, / Flying high above the moon, / Wind says: 'Come and play with me!' / Then it sits in a tree.» ¿Hay algún personaje que habla? Escribe cuál.", "Wind (el viento)", "En el poema el viento habla: Wind says."),
    ],
    [
        (f"Lee el cuento: «{ST5}» {GST5} y la tira: «{CO5}» ¿Qué tema se apoya en ambos textos? a) Ayudar a otros devolviendo lo que se perdió b) No salir cuando hay viento", "a", "En el cuento y en la tira un niño devuelve el globo a Marta; ayudar es la idea compartida."),
        ("Texto 1 (cuento): «Pedro waits at the door for his dog.» Texto 2 (poema): «Door, door, wait and wait / The dog is late, the hour is late.» Se parecen en: a) la espera b) un paseo", "a", "Ambos textos hablan de esperar al perro; ninguno cuenta un paseo."),
    ],
    [("Tu profesora te da dos textos sobre un perro perdido: un cuento de cinco oraciones y un poema de cuatro versos. Quieres saber cuál usa rima. ¿Dónde la buscas? a) En el poema b) En el cuento", "a", "Los versos de un poema suelen terminar con palabras que riman.")],
    [
        ("¿Qué forma literaria usa viñetas y globos de diálogo?", "La tira cómica", "Son sus elementos propios."),
        ("¿Qué forma usa versos y a veces rima?", "El poema", "Se escribe en líneas llamadas versos."),
        ("¿Para qué se citan pistas al comparar textos?", "Para apoyar lo que se dice", "Sin pistas la comparación queda sin pruebas."),
    ],
    task("Lee estos dos textos sobre una luna. Cuento: «Tomi cannot sleep. He looks at the moon from his window. It is round and white. He counts the stars and falls asleep.» Poema: «Moon so round, moon so white, / Watch me sleep through the night.» (round = redonda; stars = estrellas; falls asleep = se duerme) En tu hoja escribe: a) dos cosas que tienen en común, b) dos cosas en que se diferencian, c) en qué forma se nota más el sonido.", "a) Hablan de la luna y de dormir de noche. b) El cuento narra sucesos y tiene más detalle; el poema es corto y rima. c) En el poema, con la rima white - night.", ["compara con elementos concretos", "usa both, but o different en alguna frase", "cita una pista de cada texto"], ["hoja con a), b) y c)"], ["decir «son parecidos» sin pruebas", "ignorar la forma del texto"], "Pide que complete: «Both texts… but… ».",),
    "Copia la tabla de vocabulario y dibuja al lado de poem, verse y panel un ejemplo pequeño de cada uno.",
    "Elige un cuento corto que conozcas y explica en tres oraciones cómo cambiaría si fuera una tira cómica.",
)

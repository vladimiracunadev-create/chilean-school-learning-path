"""Cuaderno del estudiante, 6.º básico Inglés (propuesta), EN06 OA 09 (reproducir y producir textos orales con el sonido inicial /r/ de ready y run).

Sin audio externo: cada ejercicio escribe las palabras y oraciones y se resuelve con la teoría de la clase.
Los textos son originales. Cada palabra o estructura nueva se explica antes de usarla.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA9 = "EN06 OA 09"


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


# ---------------------------------------------------------------- clase 1: sonido inicial /r/ en ready, run
RAY = "«Ray rides a red bike by the river. He rests under a rose bush and listens to the radio.» (rides = anda, red = rojo, river = río, rests = descansa, rose bush = rosal)"

lesson(
    OA9, 1,
    "Las listas de palabras y oraciones escritas en cada ejercicio, lápiz, una hoja y un espejo pequeño si tienes.",
    "Aprenderé a reconocer y producir el sonido inicial /r/ del inglés, como en ready y run. Sirve para que te entiendan mejor cuando hablas inglés.",
    ["Sé que las palabras empiezan con un sonido.", "Conozco palabras como red, run y rain."],
    [
        "En inglés, el sonido inicial /r/ de palabras como ready (listo), run (correr), red (rojo) y rain (lluvia) no se parece a la r del español. En español, la r de «perro» vibra: la lengua golpea el paladar. En inglés no vibra. Los labios se redondean un poco, como para decir «u», y la lengua se recoge hacia atrás sin tocar el paladar ni los dientes.",
        "Para practicar, mírate en un espejo. Redondea los labios, lleva la punta de la lengua hacia atrás, sin tocar nada, y deja salir la voz: «rrr» sin vibración. Di despacio: ready, run, red, rain, rabbit. Escucha cómo suena y compáralo con tu pronunciación de «perro». Este sonido importa porque cambia el significado: right (correcto) y light (luz) son palabras distintas.",
        "Para reconocer el sonido, mira cómo empieza la palabra y dilo en voz baja. Las palabras que empiezan con la letra r, como run y rain, siempre empiezan con /r/. Otras, como lamp y lake, empiezan con /l/. Contar cuántas palabras de una oración empiezan con /r/ te ayuda a entrenar el oído y la boca al mismo tiempo.",
    ],
    [("ready", "listo"), ("run", "correr"), ("red / rain", "rojo / lluvia"), ("rabbit", "conejo"), ("/r/", "sonido inicial inglés, sin vibración"), ("right / light", "correcto / luz")],
    [
        ("Reconocer palabras con /r/", "De la lista «red, lamp, rain, book», ¿cuáles empiezan con /r/?", ["Digo cada palabra en voz baja.", "Red y rain empiezan con /r/.", "Lamp empieza con /l/ y book con /b/."], "red y rain"),
        ("Postura de la boca", "¿Qué haces con los labios para decir /r/ en inglés: los redondeas un poco o los estiras como una sonrisa?", ["La explicación dice que se redondean.", "No se estiran en una sonrisa.", "Elijo redondearlos."], "Los redondeo un poco"),
    ],
    [
        ("Vibrar la r al inicio de run, como en perro.", "Se transfiere el sonido del español.", "En inglés la lengua no toca el paladar ni vibra."),
        ("Decir que right y light suenan igual.", "No se distingue /r/ de /l/.", "Escucha el sonido inicial y cuida la posición de la lengua."),
    ],
    [
        ("¿Cuál de estas palabras empieza con /r/? a) ready b) lady c) many", "a) ready", "Ready empieza con r."),
        ("¿Cuál de estas palabras empieza con /r/? a) lamp b) rain c) window", "b) rain", "Rain comienza con /r/."),
        ("¿Cómo es la lengua al decir /r/ en inglés? a) no toca el paladar ni vibra b) golpea el paladar varias veces", "a) no toca el paladar ni vibra", "La r inglesa no vibra."),
    ],
    [
        ("De la lista «rabbit, lamp, rain, window, rock», ¿cuántas palabras empiezan con /r/?", "3", "Son rabbit, rain y rock."),
        ("¿Qué palabra de estas empieza con /r/: run o sun?", "run", "Run empieza con /r/ y sun con /s/."),
        ("¿Qué palabra de este par empieza con /r/: right o light?", "right", "Right empieza con /r/ y light con /l/."),
    ],
    [
        ("Lee: " + RAY + " ¿Cuántas palabras empiezan con /r/?", "7", "Son Ray, rides, red, river, rests, rose y radio."),
        ("Lee: " + RAY + " ¿Qué palabra con /r/ nombra un medio para escuchar música o noticias?", "radio", "Radio empieza con /r/."),
        ("Lee: «Rita reads a red book by the river.» ¿Cuántas palabras empiezan con /r/?", "4", "Son Rita, reads, red y river."),
    ],
    [
        ("Un compañero pronuncia run como «rrrun» con la lengua vibrando. ¿Qué debe cambiar? a) dejar la lengua sin tocar el paladar b) hablar más fuerte", "a) dejar la lengua sin tocar el paladar", "La r inglesa no vibra."),
        ("En la lista «road, load, rake, lake», ¿cuántas palabras empiezan con /l/?", "2", "Son load y lake; road y rake empiezan con /r/."),
    ],
    [
        ("¿Qué oración tiene más palabras con /r/ inicial? a) Ray runs round the red rock. b) Ray goes to the park.", "a) Ray runs round the red rock.", "La a) tiene cinco palabras con /r/ (Ray, runs, round, red, rock) y la b) ninguna."),
        ("Lee la oración «Ray runs to the red rock». ¿Cuántas palabras tiene y cuántas empiezan con /r/?", "6 palabras; 4 con /r/", "Ray, runs, red y rock empiezan con /r/."),
    ],
    [("En una carrera, la profesora dice: «Ready, set, go!» (set = preparados, go = ¡ya!). ¿Qué palabra empieza con /r/?", "Ready", "Es la primera palabra y comienza con /r/.")],
    [
        ("¿Vibra la r inicial en inglés?", "No", "La lengua no golpea el paladar."),
        ("¿Qué hacen los labios al decir /r/?", "Se redondean un poco", "Es parte de la postura."),
        ("¿Empieza right con /r/ o con /l/?", "Con /r/", "Right empieza con r."),
    ],
    task("Lee estas dos oraciones: «Ray runs to the red road.» y «Rita reads a rain poem.» Escribe cuántas palabras empiezan con /r/ en cada una y repítelas en voz alta tres veces cada una, frente a un espejo, cuidando que no vibre la r. Después escribe tu propia oración con tres palabras con /r/ (por ejemplo, con red, ready y rabbit).", "Oración 1: Ray, runs, red, road = 4. Oración 2: Rita, reads, rain = 3. Mi oración: The rabbit is ready to run.", ["cuenta bien las palabras con /r/", "repite con la boca en la postura de /r/", "escribe una oración con tres palabras con /r/"], ["hoja con conteo y oración", "nota de quien escuchó"], ["vibrar la r", "contar palabras que no empiezan con /r/"], "Reconoce la postura lograda y vuelve a practicar solo ready y run despacio con el espejo."),
    "Mírate en un espejo y di diez veces ready y run con los labios redondeados.",
    "Escribe cinco palabras con /r/ inicial que no estén en esta clase.",
)

# ---------------------------------------------------------------- clase 2: /r/ en palabras con wr- y rh-
lesson(
    OA9, 2,
    "Las listas de palabras escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé que algunas palabras que empiezan con wr- o rh- también empiezan con el sonido /r/, como write y rhyme, y practicaré pares de palabras. Sirve para pronunciar bien palabras de ortografía engañosa.",
    ["Conozco el sonido inicial /r/ de ready y run.", "Conozco palabras como write y right."],
    [
        "En algunas palabras del inglés hay letras que no se pronuncian (silent letters). En las palabras que empiezan con wr-, la w no se dice y la palabra empieza con /r/: write (escribir), wrong (equivocado), wrap (envolver), wrist (muñeca). En las que empiezan con rh-, la h no se dice: rhyme (rima) y rhythm (ritmo) empiezan con /r/.",
        "Por eso right (correcto) y write (escribir) suenan igual: las dos empiezan con /r/ y terminan con el mismo sonido. Son homófonas, es decir, tienen el mismo sonido y distinto significado. En cambio, wait (esperar) y window (ventana) sí empiezan con /w/, porque la w se pronuncia cuando no va seguida de r.",
        "Para decir bien estas palabras, ignora la w de wr- y la h de rh-. Di /r/ con los labios redondeados y la lengua recogida: «rite», «rong», «rap». Aprende los pares mínimos como right–light y road–load. Si cambias el sonido inicial de /r/ a /l/, cambias la palabra. Practicar en pares te ayuda a no confundirlas.",
    ],
    [("write", "escribir"), ("wrong", "equivocado"), ("wrap / wrist", "envolver / muñeca"), ("rhyme / rhythm", "rima / ritmo"), ("silent letter", "letra que no se pronuncia"), ("homophones", "palabras con el mismo sonido")],
    [
        ("Reconocer wr-", "¿Cuál palabra empieza con /r/: wrist o west?", ["Wrist empieza con wr-.", "La w no se pronuncia en wrist.", "West empieza con /w/."], "wrist"),
        ("Homófonas", "¿Suenan igual right (correcto) y write (escribir)? Responde sí o no.", ["Las dos empiezan con /r/.", "Terminan igual.", "Por eso suenan igual."], "Sí"),
    ],
    [
        ("Decir la w en wrong.", "Se pronuncian todas las letras como en español.", "En wr- la w es silenciosa; empieza con /r/."),
        ("Pensar que rhyme empieza con /h/.", "No se conoce la h silenciosa.", "En rh- la h no se pronuncia; rhyme empieza con /r/."),
    ],
    [
        ("¿Cuál de estas palabras empieza con /r/? a) write b) wait c) window", "a) write", "En write la w no se pronuncia."),
        ("¿Cuál de estas palabras empieza con /r/? a) wrong b) walk c) water", "a) wrong", "En wrong la w no se pronuncia."),
        ("¿Cuál de estas palabras empieza con /r/? a) rhyme b) honey c) house", "a) rhyme", "En rhyme la h no se pronuncia."),
    ],
    [
        ("De la lista «wrap, wall, wrist, window, write», ¿cuántas empiezan con /r/?", "3", "Son wrap, wrist y write."),
        ("¿Qué palabra suena igual que right: write o light?", "write", "Right y write empiezan igual y terminan igual."),
        ("En «rhythm», ¿qué letra no se pronuncia al inicio?", "La h", "En rh- la h es silenciosa."),
    ],
    [
        ("¿Cuántas palabras de «We write a rhyme on the wrist» empiezan con /r/?", "3", "Write, rhyme y wrist empiezan con /r/."),
        ("¿Qué palabra de este par empieza con /r/: road o load?", "road", "Road empieza con /r/ y load con /l/."),
        ("¿Qué palabra de este par empieza con /r/: lock o rock?", "rock", "Rock empieza con /r/ y lock con /l/."),
    ],
    [
        ("Un compañero lee wrong como «wrong» con /w/. ¿Qué error cometió?", "Pronunció la w, que es silenciosa", "En wrong la palabra empieza con /r/."),
        ("¿Por qué write y right son homófonas?", "Porque suenan igual aunque se escriben distinto", "Comparten el sonido pero tienen otro significado."),
    ],
    [
        ("Clasifica según su sonido inicial: wrist, light, rain, window. ¿Cuántas empiezan con /r/?", "2", "Wrist y rain empiezan con /r/."),
        ("En la oración «Rita can write the right word», ¿cuántas palabras empiezan con /r/?", "3", "Rita, write y right empiezan con /r/."),
    ],
    [("En la clase de Lenguaje alguien dice «Please write a rhyme.» (please = por favor). ¿Cuántas palabras con /r/ inicial oyes?", "2", "Son write y rhyme.")],
    [
        ("¿Se pronuncia la w en write?", "No", "Es una letra silenciosa."),
        ("¿Se pronuncia la h en rhyme?", "No", "Es una letra silenciosa."),
        ("¿Empieza wait con /r/?", "No", "Empieza con /w/."),
    ],
    task("Lee esta lista: wrap, wall, write, rhyme, window, wrong, lamp. Escribe en dos columnas las palabras que empiezan con /r/ y las que no. Después escribe una oración con write y rhyme, por ejemplo «I write a rhyme». Léela en voz alta tres veces con los labios redondeados.", "Con /r/: wrap, write, rhyme, wrong. Sin /r/: wall, window, lamp. Oración: I write a rhyme for my friend.", ["clasifica correctamente las siete palabras", "escribe una oración con write y rhyme", "lee con /r/ sin vibración"], ["hoja con dos columnas", "nota del adulto"], ["incluir wall en la columna de /r/", "pronunciar la w de write"], "Reconoce la clasificación y repasa las letras silenciosas con la persona."),
    "Escribe en una hoja las parejas right-write y repite cada palabra viendo cómo se mueven tus labios.",
    "Busca tres palabras más con wr- y practícalas con el espejo.",
)

# ---------------------------------------------------------------- clase 3: poemas y canciones
CHANT = "«Run, run, run, rabbit, run! The road is long, the race is fun. Ready, steady, round we go! Red and rosy faces glow.» (race = carrera, steady = firme, round = alrededor, rosy = rosadas, glow = brillan)"
RAINPOEM = "«Rain, rain, rolling down, rolling on the roofs of town. Ready, ready, rivers rise, reaching to the rainy skies.» (rolling = rodando, roofs = techos, rise = suben, reaching = alcanzando, skies = cielos)"

lesson(
    OA9, 3,
    "Los poemas y cantos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a reproducir poemas y cantos con muchas palabras con /r/ y a marcar el ritmo y las rimas. Sirve para practicar la pronunciación con textos divertidos.",
    ["Conozco el sonido /r/ y las palabras wr- y rh-.", "Sé que dos palabras riman si terminan igual."],
    [
        "Un poema (poem) y un canto o chant son textos cortos con ritmo. Para reproducirlos, lee primero en silencio y busca las palabras con /r/ inicial. Luego léelo en voz alta, despacio, marcando el ritmo con golpes suaves de la mano. Las palabras importantes se dicen un poco más fuerte, que se llama énfasis (stress).",
        "En un poema, las palabras que riman terminan con el mismo sonido: run con fun, go con glow. Las rimas ayudan a recordar el texto. La repetición de un sonido inicial, como run, rabbit, road, race, se llama aliteración (alliteration). Es una forma divertida de practicar /r/ varias veces seguidas.",
        "Antes de decir el texto ante otras personas, practica tres veces: la primera lenta y con la boca muy clara; la segunda a velocidad normal; la tercera con ritmo y expresión. No importa tener un acento perfecto: lo que importa es que se escuche /r/ distinto de /l/ y que se entienda el mensaje.",
    ],
    [("chant", "canto rítmico"), ("rhyme", "rima"), ("alliteration", "repetición de un sonido inicial"), ("stress", "énfasis: fuerza en una palabra"), ("rhythm", "ritmo"), ("rolling", "rodando")],
    [
        ("Encontrar la rima", "Lee: «Rain on the roof, rain on the road. Rain on the river, rain on the toad.» (roof = techo, toad = sapo). ¿Qué palabra rima con road?", ["Miro el final de la primera línea: road.", "Busco otra palabra con el mismo sonido final.", "Toad rima con road."], "toad"),
        ("Contar palabras con /r/", "Lee: «Rabbit runs on the road.» ¿Cuántas palabras empiezan con /r/?", ["Rabbit empieza con /r/.", "Runs también.", "Road también: son tres."], "3"),
    ],
    [
        ("Leer el poema muy rápido sin marcar el ritmo.", "No se practican los sonidos con claridad.", "Empieza lento, marca el ritmo y sube la velocidad."),
        ("Pensar que la aliteración y la rima son lo mismo.", "Se confunde el sonido inicial con el final.", "La aliteración repite el comienzo; la rima repite el final."),
    ],
    [
        ("Lee: " + CHANT + " ¿Qué palabra rima con fun? a) run b) road c) glow", "a) run", "Run y fun terminan igual."),
        ("Lee: " + CHANT + " ¿Qué palabra rima con go? a) glow b) race c) red", "a) glow", "Go y glow terminan con el mismo sonido."),
        ("Lee: " + CHANT + " ¿Qué animal aparece? a) un conejo b) un perro", "a) un conejo", "El canto nombra a un rabbit."),
    ],
    [
        ("Lee: " + CHANT + " ¿Cuántas veces aparece la palabra run en la primera línea?", "4", "Dice Run, run, run, rabbit, run."),
        ("Lee: " + CHANT + " ¿Cuántas palabras de la primera línea empiezan con /r/?", "5", "Son run, run, run, rabbit y run."),
        ("Lee: " + CHANT + " ¿Qué palabra con /r/ nombra un camino?", "road", "Road empieza con /r/."),
    ],
    [
        ("Lee: " + RAINPOEM + " ¿Qué palabra rima con town? a) down b) rise c) roofs", "a) down", "Down y town terminan igual."),
        ("Lee: " + RAINPOEM + " ¿Qué palabra rima con rise? a) skies b) rivers c) ready", "a) skies", "Rise y skies terminan con el mismo sonido."),
        ("Lee: " + RAINPOEM + " ¿Qué dice el poema que cae en los techos de la ciudad?", "La lluvia", "Dice rain rolling on the roofs of town."),
    ],
    [
        ("Lee: " + RAINPOEM + " ¿Cuántas veces aparece la palabra rain en el poema?", "2", "Rain se repite en la primera línea; rainy es otra palabra."),
        ("Un compañero lee el poema de la lluvia con r vibrante como en perro. ¿Qué debe corregir? a) hacer la r sin vibración b) hablar más lento", "a) hacer la r sin vibración", "La r inicial inglesa no vibra."),
    ],
    [
        ("Lee: " + CHANT + " Si repites todo el canto tres veces, ¿cuántas veces dices run en total? (El texto tiene la palabra run 4 veces en la primera línea.)", "12", "Se multiplican cuatro por tres.", "4*3"),
        ("Aliteración: ¿cuál oración repite más /r/ al inicio? a) Ray runs round the red rock. b) The cat sits on the mat.", "a) Ray runs round the red rock.", "Todas sus palabras importantes empiezan con /r/."),
    ],
    [("En un acto del colegio vas a decir un canto. La profesora te pide que marques el ritmo. ¿Qué haces? a) golpeo suave con la mano cada palabra importante b) corro por la sala", "a) golpeo suave con la mano cada palabra importante", "El golpe marca el ritmo y el énfasis.")],
    [
        ("¿Qué es una rima?", "Palabras que terminan con el mismo sonido", "Se oye al final."),
        ("¿Qué es la aliteración?", "Repetir un sonido al inicio de varias palabras", "Como run, rabbit, road."),
        ("¿Cómo practicas un poema por primera vez?", "Despacio y con claridad", "Primero se cuida la pronunciación."),
    ],
    task("Lee este canto de cuatro versos: «Red robots, ready to run. Rolling round the rainy sun. Right and left, they race and ride. Rest at night side by side.» (robots = robots, rolling = rodando, race = corren, side by side = lado a lado). Escribe: cuántas palabras de los dos primeros versos empiezan con /r/ y qué palabras riman al final de los versos 3 y 4. Luego léelo tres veces: lento, normal y con ritmo.", "Primeros dos versos: Red, robots, ready, run, Rolling, round, rainy = 7. Riman ride y side.", ["cuenta correctamente las palabras con /r/", "identifica la rima", "lee con tres velocidades"], ["hoja con respuestas", "nota del adulto"], ["no contar rolling o round", "decir que riman race y ride"], "Reconoce el conteo y escucha una vez más la lectura marcando las palabras con /r/."),
    "Aprende de memoria el canto del conejo y dilo con una persona de tu casa marcando el ritmo.",
    "Escribe un canto de dos versos con cinco palabras con /r/ inicial.",
)

# ---------------------------------------------------------------- clase 4: adivinanzas
lesson(
    OA9, 4,
    "Las adivinanzas escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a reproducir y producir adivinanzas en inglés con palabras que empiezan con /r/. Sirve para jugar con el idioma y practicar la pronunciación.",
    ["Conozco el sonido /r/ y palabras como rain, rabbit y river.", "Sé decir What am I?"],
    [
        "Una adivinanza (riddle) describe algo sin decir su nombre y termina con una pregunta: «What am I?» (¿qué soy?). Tiene tres o cuatro pistas: cómo es, qué hace y dónde está. Quien la escucha debe decir la respuesta. Muchas respuestas pueden empezar con /r/: rain (lluvia), rabbit (conejo), river (río), robot (robot) o rainbow (arcoíris).",
        "Para decir una adivinanza, usa el presente: «I fall from the sky» (caigo del cielo), «I have long ears» (tengo orejas largas). Habla despacio y haz una pausa antes de la pregunta final. Para dar la respuesta, di «You are...» o «It is a rabbit». Recuerda cuidar el sonido /r/ en la respuesta, sin vibrar.",
        "Para inventar una adivinanza, elige una cosa, escribe tres pistas verdaderas y agrega What am I? Comprueba que las pistas no digan la respuesta directamente y que sirvan solo para esa cosa. Por ejemplo, para rainbow: «I have seven colours. I appear after rain. What am I?». Luego léela a otra persona y pídele que adivine.",
    ],
    [("riddle", "adivinanza"), ("What am I?", "¿qué soy?"), ("clue", "pista"), ("rainbow", "arcoíris"), ("long ears", "orejas largas"), ("It is a...", "es un...")],
    [
        ("Resolver una adivinanza", "Lee: «I am long and wet. I flow to the sea. Fish live in me. What am I?» (long = largo, wet = mojado, flow = fluye). ¿Cuál es la respuesta: a river o a mountain?", ["Las pistas dicen largo, mojado y fluye hacia el mar.", "Fish live in me confirma que hay agua.", "Es a river."], "a river"),
        ("Reconocer /r/ en la respuesta", "¿Empieza river con /r/? Responde sí o no.", ["River empieza con r.", "Se pronuncia con /r/ sin vibración.", "Sí."], "Sí"),
    ],
    [
        ("Decir la respuesta antes de dar las pistas.", "Se rompe el juego.", "Di las pistas y espera antes de responder."),
        ("Poner pistas que sirven para muchas cosas.", "Pistas muy generales.", "Elige datos exclusivos de la respuesta."),
    ],
    [
        ("Lee: «I have long ears. I hop. I eat carrots. What am I?» (hop = salto, carrots = zanahorias). ¿Cuál es la respuesta? a) a rabbit b) a fish", "a) a rabbit", "Las pistas son orejas largas, saltar y zanahorias."),
        ("Lee: «I fall from the sky. I make puddles. You need an umbrella when I come. What am I?» ¿Cuál es la respuesta? a) rain b) sun", "a) rain", "Las pistas hablan de caer, charcos y paraguas."),
        ("Lee: «I have seven colours. I appear after rain. What am I?» (colours = colores, appear = aparezco). ¿Cuál es la respuesta? a) a rainbow b) a river", "a) a rainbow", "El arcoíris tiene siete colores y sale después de la lluvia."),
    ],
    [
        ("¿Cuál de estas respuestas de adivinanza NO empieza con /r/? a) rain b) rabbit c) snow d) river", "c) snow", "Snow empieza con /s/."),
        ("¿Qué pregunta final tienen casi todas las adivinanzas en inglés? a) What am I? b) Where is the bus?", "a) What am I?", "Significa ¿qué soy?"),
        ("Lee: «I am a machine. I can walk and talk. I am not a person. What am I?» (machine = máquina). ¿Cuál es la respuesta que empieza con /r/? a) robot b) table", "a) robot", "Robot es una máquina que camina y habla."),
    ],
    [
        ("Lee: «I am round. I am red or green. I grow on a tree. What am I?» (tree = árbol). Las pistas dicen redondo, rojo o verde y que crece en un árbol. ¿Cuál es la respuesta? a) an apple b) a rock", "a) an apple", "Una manzana crece en un árbol."),
        ("En la adivinanza «I am a machine. I can walk and talk. I am not a person.», ¿cuántas pistas hay?", "3", "Son tres: es una máquina, camina y habla, y no es una persona."),
        ("Una adivinanza dice: «I live in a river. I have a long tail. I am green. What am I?» Un compañero responde rabbit. ¿Por qué se equivoca?", "Porque un conejo no vive en un río", "Una pista dice que vive en un río."),
    ],
    [
        ("Ordena una adivinanza. A) What am I? B) I have long ears. C) I eat carrots.", "B, C, A", "Primero las pistas y al final la pregunta."),
        ("Lee: «I am white and cold. I fall in winter on the mountains. What am I?» (white = blanco, cold = frío). ¿Cuál es la respuesta? a) snow b) rain", "a) snow", "Blanca, fría y cae en las montañas en invierno."),
    ],
    [
        ("Lee: «I am a flower. I have thorns on my stem. I can be red. What am I?» (thorns = espinas, stem = tallo). ¿Cuál es la respuesta? a) a rose b) a rock", "a) a rose", "Una rosa es una flor con espinas y puede ser roja."),
        ("Lee: «I travel to space. Astronauts ride inside me. What am I?» (space = espacio, astronauts = astronautas). ¿Cuál es la respuesta? a) a rocket b) a river", "a) a rocket", "Los astronautas viajan al espacio en un cohete."),
    ],
    [("En una fiesta, alguien dice: «I have four wheels. I carry people on the road. I am not a bus. What am I?» (wheels = ruedas, carry = llevo). ¿Cuál es la respuesta? a) a car b) a rabbit", "a) a car", "Un auto tiene cuatro ruedas y va por el camino.")],
    [
        ("¿Qué significa «What am I?»", "¿Qué soy?", "Cierra la adivinanza."),
        ("¿Qué son las pistas?", "Datos que ayudan a adivinar", "Describen la respuesta."),
        ("¿Empieza rainbow con /r/?", "Sí", "Rainbow comienza con r."),
    ],
    task("Inventa una adivinanza en inglés con tres pistas y la pregunta What am I? La respuesta debe empezar con /r/: elige entre rain, rabbit, river, robot o rainbow. Usa como modelo: «I have long ears. I hop. I eat carrots. What am I?». Escribe tu adivinanza, la respuesta y léela en voz alta a una persona para que la adivine.", "I am big. I flow to the sea. Fish live in me. What am I? A river.", ["escribe tres pistas verdaderas", "termina con What am I?", "la respuesta empieza con /r/"], ["hoja con la adivinanza", "nota de quien la adivinó"], ["pistas que no sirven para la respuesta", "olvidar la pregunta final"], "Reconoce las pistas más claras y muestra cómo agregar una pista más exclusiva."),
    "Di a una persona de tu casa la adivinanza del conejo y espera que adivine.",
    "Escribe dos adivinanzas más para rain y robot.",
)

# ---------------------------------------------------------------- clase 5: monólogos y diálogos
ROOMTALK = "«This is my room. It is small, and it has a red rug. I read books here. When it rains, I listen to the radio.» (rug = alfombra, read = leo, listen = escucho)"
DIALOG = "«A: Are you ready? B: Yes, I am. A: Run to the red door. B: Right away!» (door = puerta, right away = de inmediato)"

lesson(
    OA9, 5,
    "Los diálogos y monólogos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a producir un monólogo y un diálogo cortos con palabras que empiezan con /r/, cuidando la entonación. Sirve para hablar en inglés con claridad en situaciones cotidianas.",
    ["Conozco el sonido /r/ y las palabras wr- y rh-.", "Sé hacer preguntas como Are you ready?"],
    [
        "Un monólogo (monologue) es un texto que dice una sola persona, como cuando presentas tu pieza o cuentas lo que haces. Un diálogo (dialogue) es una conversación entre dos o más personas. Ambos se pueden producir oralmente con frases cortas que repiten el sonido /r/, por ejemplo: «This is my room. It has a red rug».",
        "La entonación (intonation) es la música de la voz. En inglés, las oraciones afirmativas terminan bajando la voz: «Yes, I am.» Las preguntas de sí o no suben al final: «Are you ready?». Las preguntas con What, Where o Why suelen bajar. Practicar la entonación junto con /r/ te ayuda a sonar natural.",
        "Para producir un diálogo, escribe turnos cortos y marca las palabras con /r/. Practica con otra persona: uno dice la pregunta y otro la respuesta. Cambia el rol y repite. Grábate si puedes y escúchate: ¿se oye /r/ sin vibración? ¿baja o sube la voz cuando corresponde? Así identificas qué mejorar y practicas de forma independiente.",
    ],
    [("monologue", "texto dicho por una sola persona"), ("dialogue", "conversación"), ("intonation", "música de la voz"), ("rising / falling", "sube / baja"), ("right away", "de inmediato"), ("rug", "alfombra")],
    [
        ("Entonación de una pregunta", "En «Are you ready?», ¿la voz sube o baja al final?", ["Es una pregunta de sí o no.", "Las preguntas de sí o no suben al final.", "La voz sube."], "Sube"),
        ("Contar palabras con /r/ en un diálogo", "Lee: «A: Run to the river. B: Right, I am ready.» ¿Cuántas palabras empiezan con /r/?", ["Run y river en la línea A.", "Right y ready en la línea B.", "Son cuatro."], "4"),
    ],
    [
        ("Subir la voz al final de toda oración.", "Se confunden afirmaciones con preguntas.", "En afirmaciones la voz baja; en preguntas de sí o no, sube."),
        ("Hablar muy rápido y perder la /r/.", "Se acelera la lectura.", "Dilo despacio primero."),
    ],
    [
        ("Lee: " + DIALOG + " ¿Cuántas personas hablan? a) 2 b) 3", "a) 2", "Hablan A y B."),
        ("Lee: " + DIALOG + " ¿Qué pregunta hace A? a) Are you ready? b) Where is the bus?", "a) Are you ready?", "Es la primera frase."),
        ("Lee: " + DIALOG + " ¿A dónde debe correr B?", "A la puerta roja", "Dice Run to the red door."),
    ],
    [
        ("Lee: " + DIALOG + " ¿Cuántas palabras empiezan con /r/ en todo el diálogo?", "4", "Son ready, Run, red y Right."),
        ("Lee: " + DIALOG + " ¿La voz sube o baja en «Are you ready?»", "Sube", "Es una pregunta de sí o no."),
        ("Lee: " + DIALOG + " ¿La voz sube o baja en «Yes, I am.»", "Baja", "Es una afirmación."),
    ],
    [
        ("Lee: " + ROOMTALK + " ¿Qué color tiene la alfombra? a) roja b) azul", "a) roja", "Dice a red rug."),
        ("Lee: " + ROOMTALK + " ¿Qué hace el narrador cuando llueve?", "Escucha la radio", "Dice when it rains, I listen to the radio."),
        ("Lee: " + ROOMTALK + " ¿Cuántas palabras con /r/ inicial hay en la última oración (rains, radio)?", "2", "Rains y radio empiezan con /r/."),
    ],
    [
        ("Un compañero lee «Where is the red rug?» con voz que sube mucho. ¿Qué entonación suele tener esa pregunta? a) baja al final b) sube al final", "a) baja al final", "Las preguntas con Where suelen bajar."),
        ("Un compañero dice en el diálogo «Right away!» con voz que sube como pregunta. ¿Es adecuada la entonación? Responde sí o no.", "No", "Es una afirmación que normalmente baja."),
    ],
    [
        ("Ordena el diálogo. A) Run to the red door. B) Are you ready? C) Right away!", "B, A, C", "La pregunta va primero, luego la orden y la respuesta."),
        ("Completa con una palabra con /r/: «The ___ is wet.» Opciones: road, lamp, window.", "road", "Road empieza con /r/."),
    ],
    [("En un negocio, el vendedor dice: «Ready? Here is your change.» (change = vuelto). ¿La voz de «Ready?» sube o baja?", "Sube", "Es una pregunta de sí o no.")],
    [
        ("¿Qué es un monólogo?", "Un texto dicho por una sola persona", "Habla solo uno."),
        ("¿Qué entonación tiene una pregunta de sí o no?", "Sube al final", "Así se reconoce la pregunta."),
        ("¿Qué entonación tiene una afirmación?", "Baja al final", "Termina con tono descendente."),
    ],
    task("Escribe un monólogo de cuatro frases sobre tu pieza o tu escritorio, usando al menos cuatro palabras que empiecen con /r/ (por ejemplo, room, red, read, radio). Modelo: «This is my room. I read books here. I have a red rug». Luego escribe un diálogo de cuatro turnos con Are you ready? y Right away!. Léelos en voz alta con la entonación correcta.", "This is my room. I have a red rug. I read books here. I listen to the radio. A: Are you ready? B: Yes, I am. A: Run to the door. B: Right away!", ["usa al menos cuatro palabras con /r/", "la entonación de las preguntas sube", "el diálogo tiene cuatro turnos"], ["hoja con monólogo y diálogo", "nota de quien escuchó"], ["subir la voz en todas las oraciones", "no repetir /r/"], "Reconoce el esfuerzo y repasa la entonación de preguntas con la persona."),
    "Grábate o practica frente a una persona leyendo tu monólogo y pídele que diga cuántas veces oyó /r/.",
    "Escribe una pregunta de sí o no y una afirmación con /r/ y practica la entonación de cada una.",
)

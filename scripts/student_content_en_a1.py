"""Student material for 1.º básico Inglés, EN01 OA 01 (escuchar rimas, chants, cuentos y diálogos) y OA 02 (temas y funciones conocidas).

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado.
El estudiante puede tapar el guion con una hoja mientras el adulto lee.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA1, OA2 = "EN01 OA 01", "EN01 OA 02"
ADULT = "Un adulto lee en voz alta (el estudiante tapa el guion): "


# ---------------------------------------------------------------- OA 01
register(
    OA1, 1,
    materials="Los textos cortos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    use="Aprenderé a reconocer si lo que escucho en inglés es un chant, un diálogo o un cuento. Sirve para saber qué debo hacer al escuchar: aplaudir, responder o seguir una historia.",
    prior=["Sé escuchar con atención a una persona que lee.", "Sé decir «hello» y «goodbye»."],
    explain=[
        "Un chant es un texto con ritmo, con palabras que se repiten, que se dice con palmas o pasos. Un diálogo es una conversación: dos personas se hablan y se turnan. Un cuento (story) cuenta qué le pasa a un personaje y muchas veces empieza con «Once upon a time», que significa «érase una vez».",
        "Para saber qué tipo de texto escuchas, no necesitas entender todas las palabras. Fíjate en pistas: ¿hay ritmo y palabras repetidas?, ¿hay dos voces que preguntan y responden?, ¿alguien cuenta una historia desde el comienzo?",
        "Cuando sabes el tipo de texto, sabes qué hacer. En un chant te unes con las palmas, en un diálogo respondes a la pregunta, y en un cuento escuchas qué hace el personaje. Si no entiendes una palabra, sigue escuchando: el resto del texto te ayuda.",
    ],
    vocab=[("chant", "texto con ritmo que se repite y se dice en voz alta"), ("dialogue", "conversación entre dos personas"), ("story", "cuento"), ("Once upon a time", "érase una vez"), ("listen", "escuchar"), ("clap", "aplaudir")],
    worked=[
        {"title": "Reconocer un diálogo", "problem": ADULT + "«A: Hello! What's your name? B: I'm Sam.» ¿Qué tipo de texto es?", "steps": ["Hay dos voces: A y B.", "A pregunta y B responde.", "Eso es una conversación."], "answer": "Es un diálogo (dialogue)"},
        {"title": "Reconocer un chant", "problem": ADULT + "«Clap, clap, stamp! Clap, clap, stamp!» ¿Qué tipo de texto es?", "steps": ["Las mismas palabras se repiten.", "Tiene ritmo, como para aplaudir y pisar fuerte.", "No hay pregunta ni historia."], "answer": "Es un chant"},
    ],
    mistakes=[
        {"wrong": "Pensar que no se puede saber el tipo de texto si no se entiende cada palabra.", "why": "Se intenta traducir todo y se pierde el hilo.", "fix": "Busca pistas: ritmo, repetición, dos voces o «Once upon a time»."},
        {"wrong": "Llamar diálogo a cualquier texto que tenga muchas palabras en inglés.", "why": "Se confunde el idioma con el tipo de texto.", "fix": "Un diálogo tiene dos personas que se turnan para hablar."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Hello! What's your name? I'm Sam.» ¿Cuántas personas hablan?", "2", "Una pregunta y otra responde, así que hablan dos personas."),
            ex(ADULT + "«Jump, jump, jump! Stop!» ¿Es un chant o es un cuento?", "Es un chant", "Tiene ritmo y repite la palabra jump."),
            ex(ADULT + "«Once upon a time, a little dog found a bone.» ¿Empieza como un cuento o como un chant?", "Como un cuento", "«Once upon a time» es la forma típica de empezar un cuento."),
        ],
        "understand": [
            ex("¿Qué significa «Once upon a time»?", "Érase una vez", "Es la frase que abre muchos cuentos en inglés."),
            ex("¿Cómo puedes darte cuenta de que un texto es un diálogo?", "Porque dos personas se turnan para hablar, una pregunta y otra responde", "El cambio de voz es la pista principal."),
            ex("¿Qué es un chant y qué haces cuando lo escuchas?", "Es un texto con ritmo y palabras repetidas; me uno con palmas o con la voz", "La repetición permite unirse aunque no se entienda todo."),
        ],
        "apply": [
            ex(ADULT + "«Red, red, red! Blue, blue, blue! Clap your hands, one, two!» ¿Es un chant, un diálogo o un cuento?", "Es un chant", "Repite palabras y tiene ritmo."),
            ex(ADULT + "«A: Is it a cat? B: No, it's a dog.» ¿Es un chant, un diálogo o un cuento?", "Es un diálogo", "A pregunta y B responde."),
            ex(ADULT + "«The little bird sat on a tree. It saw a big yellow sun.» ¿Es un chant, un diálogo o un cuento?", "Es un cuento", "Cuenta lo que hace y ve un personaje, el pájaro."),
        ],
        "reason": [
            ex("Un texto dice «Stamp, stamp, stamp your feet!». ¿Por qué no es un diálogo?", "Porque nadie pregunta ni responde; solo repite palabras con ritmo", "Falta la conversación entre dos personas."),
            ex("Ana dice: «Once upon a time, a fish had a hat» es un diálogo porque está en inglés. ¿Tiene razón?", "No; es el comienzo de un cuento", "El idioma no define el tipo; la forma de empezar sí."),
        ],
        "challenge": [
            ex("Ordena el diálogo con números: (1) B: I'm fine, thank you. (2) A: Hello! How are you?", "2, 1", "Primero A saluda y pregunta; después B responde."),
            ex("Une cada texto con su tipo. (a) «Stamp, stamp, stamp your feet!» (b) «A: What's this? B: It's a ball.» (c) «Once upon a time, a rabbit lived in a house.»", "a = chant, b = diálogo, c = cuento", "Ritmo repetido, pregunta con respuesta y comienzo de historia."),
        ],
    },
    context=[ex("En la sala de clases la profesora lee: «Hello! I'm Mia. What's your name?» y un compañero responde «I'm Leo». ¿Qué tipo de texto escuchaste?", "Un diálogo", "Mia pregunta y Leo responde, como en una conversación.")],
    selfcheck=[
        ex("¿Cómo se dice «cuento» en inglés?", "story", "Es la palabra para un cuento o una historia."),
        ex(ADULT + "«Up, up, up! Down, down, down!» ¿Es un chant o un diálogo?", "Es un chant", "Se repiten palabras con ritmo."),
        ex("¿Qué pista te dice que un texto es un diálogo?", "Dos personas que hablan por turnos", "Pregunta y respuesta muestran dos voces."),
    ],
    open_task=task("Un adulto lee dos veces este mini diálogo: «A: Hello! I'm Ana. B: Hello, Ana! I'm Leo.» Después di en voz alta, con ayuda del adulto: (1) «It's a dialogue.» y (2) tu propio «Hello! I'm ...» con tu nombre.", "«It's a dialogue.» «Hello! I'm Pedro.» (con voz clara y mirando a la otra persona).", ["dice «It's a dialogue»", "se presenta con «Hello! I'm ...»", "habla fuerte y claro"], ["audio o nota del adulto que oyó las dos frases"], ["decir «story» en lugar de «dialogue»", "decir solo el nombre sin «Hello»"], "Felicítale por usar el inglés y repite con él la frase que le costó, más despacio y sin presión."),
    reinforce="Pide a un adulto que lea «Clap, clap, stamp!» y aplaude con él cada vez que oigas «clap».",
    extend="Inventa un chant de dos líneas con la palabra «jump» repetida tres veces y dilo con palmas.",
)

register(
    OA1, 2,
    materials="Los chants escritos en cada ejercicio, que lee un adulto; lápiz y una hoja para tapar el guion.",
    use="Aprenderé a unirme a un chant diciendo la línea que se repite. Sirve para participar en inglés aunque no entienda todas las palabras.",
    prior=["Sé que un chant tiene ritmo.", "Sé decir algunas palabras como «cat», «dog» y «red»."],
    explain=[
        "En un chant, una línea o una palabra se repite una y otra vez. Esa parte repetida es tu oportunidad para unirte (join in). Escuchas, descubres qué se repite y lo dices junto a quien lee.",
        "Por ejemplo, en «I see a cat, cat, cat! I see a hat, hat, hat!» la estructura «I see a ...» se repite, y solo cambia una palabra. Si sabes cuál es la parte que cambia, puedes seguir el chant y hasta crear uno nuevo.",
        "Para unirte bien: escucha primero, di la parte repetida en voz baja y luego más fuerte. No es una carrera: lo importante es seguir el ritmo y decir las palabras con claridad.",
    ],
    vocab=[("repeat", "repetir"), ("join in", "unirse"), ("I see", "yo veo"), ("up / down", "arriba / abajo"), ("jump", "saltar"), ("stop", "detenerse, parar")],
    worked=[
        {"title": "Encontrar la parte repetida", "problem": ADULT + "«I see a cat, cat, cat! I see a hat, hat, hat!» ¿Qué parte se repite en las dos líneas?", "steps": ["Escucho «I see a» al comienzo de cada línea.", "Solo cambian cat y hat.", "La parte repetida es «I see a»."], "answer": "«I see a ...» se repite"},
        {"title": "Completar el chant", "problem": ADULT + "«Up, up, up! Down, down, ...?» ¿Qué palabra falta?", "steps": ["La primera línea dice up tres veces.", "La segunda debe repetir down tres veces.", "Falta la tercera palabra down."], "answer": "down"},
    ],
    mistakes=[
        {"wrong": "Quedarse en silencio hasta entender todas las palabras.", "why": "Se piensa que hay que traducir primero.", "fix": "Di la parte repetida aunque no entiendas lo demás."},
        {"wrong": "Decir la parte repetida muy rápido y fuera del ritmo.", "why": "Se pierde el compás de la lectura.", "fix": "Escucha el ritmo y di las palabras al mismo tiempo que el adulto."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Jump, jump, jump! Clap, clap, clap!» ¿Qué palabra se repite en la primera línea?", "jump", "Se dice tres veces en la primera línea."),
            ex(ADULT + "«Hello, hello, hello!» ¿Cuántas veces se dice hello?", "3", "La palabra aparece tres veces seguidas."),
            ex(ADULT + "«Stop and look, stop and look, one, two, three.» ¿Cuántas veces se dice «stop and look»?", "2", "La expresión se dice dos veces antes de contar."),
        ],
        "understand": [
            ex("¿Para qué sirve una línea repetida en un chant?", "Para que pueda unirme y decirla con los demás", "La repetición hace fácil participar."),
            ex("¿Qué significa «join in» en un chant?", "Unirse a decirlo", "Es participar diciendo las palabras junto al grupo."),
            ex("¿Qué haces cuando oyes «Clap, clap, clap!»?", "Aplaudo tres veces", "Clap significa aplaudir y se dice tres veces."),
        ],
        "apply": [
            ex(ADULT + "«I like red, red, red! I like blue, blue, blue!» Completa: «I like yellow, ___, ___!»", "yellow, yellow", "El patrón repite el color tres veces."),
            ex(ADULT + "«Up, up, up! Down, down, ___!»", "down", "La palabra down se repite tres veces."),
            ex(ADULT + "«Cat, cat, cat! Dog, dog, dog! Fish, fish, ___!»", "fish", "Cada animal se dice tres veces."),
        ],
        "reason": [
            ex(ADULT + "«Run, run, run! Run, run, run! Stop!» ¿Qué palabra no se repite?", "Stop", "Run se repite seis veces y stop una sola vez."),
            ex("¿Por qué no necesitas entender todas las palabras para unirte a un chant?", "Porque la parte repetida se puede copiar sin traducirla toda", "Escuchar el patrón es suficiente para participar."),
        ],
        "challenge": [
            ex("El chant dice «I see a cat, cat, cat!». Cambia cat por dog y escribe la nueva línea.", "I see a dog, dog, dog!", "Se mantiene el patrón y cambia una palabra."),
            ex(ADULT + "«Hop, hop, hop! Sit, sit, sit! Hop, hop, hop!» ¿Cuántas veces oyes la palabra hop en total?", "6", "Hop aparece tres veces en la primera línea y tres en la tercera."),
        ],
    },
    context=[ex("En clase la profesora dice «Wave, wave, wave!» tres veces y mueve la mano de lado a lado. ¿Qué haces tú?", "Muevo la mano saludando", "Wave es saludar con la mano y se hace al ritmo del chant.")],
    selfcheck=[
        ex(ADULT + "«Sit, sit, sit! Stand, stand, stand!» ¿Qué palabra se repite en la segunda línea?", "stand", "Se dice tres veces."),
        ex("¿Qué significa «up» y «down»?", "Arriba y abajo", "Son palabras de dirección muy comunes."),
        ex("¿Qué debes hacer primero al escuchar un chant?", "Escuchar y descubrir qué se repite", "Así sabes qué parte decir con el grupo."),
    ],
    open_task=task("Un adulto lee este chant dos veces: «Clap, clap, clap! Stamp, stamp, stamp! Jump, jump, jump! Stop!» Únete diciendo cada palabra tres veces con su movimiento. Luego cambia una palabra y di tu propio chant, por ejemplo con «turn».", "«Turn, turn, turn! Clap, clap, clap! Stop!» con giro y palmas.", ["repite cada palabra tres veces", "acompaña con el movimiento", "cambia una palabra del chant", "para en «Stop»"], ["nota del adulto", "foto o video con permiso de la familia"], ["decir las palabras sin ritmo", "olvidar la parada"], "Reconoce el ritmo que logró y practica junto a él la palabra que se le hizo más difícil."),
    reinforce="Pide a un adulto que lea «Hello, hello, hello!» y repítelo con él tres veces.",
    extend="Escribe un chant de tres líneas con las palabras «sun», «run» y «fun», repitiendo cada una tres veces.",
)

register(
    OA1, 3,
    materials="Los cuentos cortos escritos en cada ejercicio, que lee un adulto; lápiz y una hoja para tapar el guion.",
    use="Aprenderé a seguir quién es el personaje de un cuento en inglés y qué le pasa. Sirve para entender una historia aunque esté en otro idioma.",
    prior=["Sé que un cuento tiene personajes.", "Sé algunas palabras de animales y colores en inglés."],
    explain=[
        "Un cuento tiene personajes (characters) y hechos (events). Para seguirlo, hazte dos preguntas: ¿quién es? y ¿qué hace? En inglés: Who is it? What does he or she do?",
        "Escucha los nombres y las palabras de acción. Por ejemplo, en «Tom has a red kite. The kite goes up, up, up!», los personajes son Tom y la cometa (kite). El hecho es que la cometa sube. Palabras como has (tiene), goes (va) y says (dice) te ayudan a saber qué ocurre.",
        "Si pierdes una parte, no te detengas. Quédate con los personajes y con lo que pasa primero y después. Casi siempre, el final cuenta cómo termina el problema o qué siente el personaje.",
    ],
    vocab=[("character", "personaje"), ("kite", "cometa"), ("has", "tiene"), ("goes", "va, se mueve"), ("says", "dice"), ("happy", "contento")],
    worked=[
        {"title": "Quién y qué hace", "problem": ADULT + "«Tom has a red kite. The wind is strong. The kite goes up, up, up! Tom says: Wow!» ¿Quién es el personaje principal y qué tiene?", "steps": ["Escucho el nombre Tom.", "Escucho «has a red kite».", "Tom tiene una cometa roja."], "answer": "Tom; tiene una cometa roja"},
        {"title": "Qué pasa después", "problem": "En el mismo cuento, ¿qué hace la cometa cuando el viento es fuerte?", "steps": ["Busco el hecho: «goes up, up, up».", "Up significa arriba."], "answer": "La cometa sube"},
    ],
    mistakes=[
        {"wrong": "Responder con cualquier personaje que se acuerde, sin volver al texto.", "why": "Se confunde el nombre de un personaje con otro.", "fix": "Pide al adulto que lea otra vez y anota el nombre que oyes."},
        {"wrong": "Tratar de traducir cada palabra del cuento.", "why": "Se pierde el hilo de lo que pasa.", "fix": "Quédate con quién es y qué hace."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Ana has a green frog. The frog jumps.» ¿Cómo se llama la niña?", "Ana", "El texto dice «Ana has a green frog»."),
            ex(ADULT + "«Ana has a green frog. The frog jumps.» ¿De qué color es la rana?", "Verde", "Green significa verde."),
            ex(ADULT + "«Ana has a green frog. The frog jumps.» ¿Qué hace la rana?", "Salta", "Jumps significa salta."),
        ],
        "understand": [
            ex("¿Qué significa «character» en un cuento?", "Personaje", "Es quien vive la historia."),
            ex("¿Qué dos preguntas te ayudan a seguir un cuento?", "¿Quién es? y ¿qué hace?", "Con ellas identificas personaje y hecho."),
            ex("¿Qué significa «says» en «Tom says: Wow!»?", "dice", "Says es el verbo que muestra lo que habla el personaje."),
        ],
        "apply": [
            ex(ADULT + "«Mia has a blue ball. She kicks the ball. The ball goes to the dog.» ¿Qué tiene Mia?", "Una pelota azul", "Has a blue ball indica lo que tiene."),
            ex(ADULT + "«Mia has a blue ball. She kicks the ball. The ball goes to the dog.» ¿A quién llega la pelota?", "Al perro", "El texto dice «goes to the dog»."),
            ex(ADULT + "«Leo sees a big cat. The cat is on a chair. Leo says: Hello, cat!» ¿Dónde está el gato?", "En una silla", "On a chair es sobre una silla."),
        ],
        "reason": [
            ex(ADULT + "«Sam has a red hat. The wind takes the hat. Sam says: Oh no!» ¿Cómo crees que se siente Sam y qué palabras te lo dicen?", "Preocupado o triste; lo dice «Oh no!»", "La exclamación muestra el sentimiento."),
            ex("En «Tom has a red kite», ¿por qué la cometa también es un personaje importante en el cuento?", "Porque es lo que hace la acción de subir", "La cometa es protagonista de los hechos."),
        ],
        "challenge": [
            ex("Ordena los hechos del cuento de la cometa: (1) La cometa sube. (2) Tom tiene una cometa roja. (3) Tom dice: Wow!", "2, 1, 3", "Primero la tiene, luego sube y después Tom reacciona."),
            ex(ADULT + "«Beto has two fish. One fish is red. One fish is blue. Beto gives food to the fish.» ¿Cuántos peces tiene Beto?", "2", "Two es dos y se nombran dos peces."),
        ],
    },
    context=[ex(ADULT + "«A little bird is in the garden. The bird sees a worm. The bird eats the worm.» En la casa de Pía, el abuelo cuenta esto en inglés. ¿Qué come el pájaro?", "Un gusano", "Worm es gusano y el texto dice «eats the worm».")],
    selfcheck=[
        ex(ADULT + "«Ana has a green frog. The frog jumps.» ¿Quién salta?", "La rana", "La rana es quien jumps."),
        ex("¿Qué significa «has» en inglés?", "tiene", "Has se usa para decir lo que alguien tiene."),
        ex("¿Qué haces si no entiendes una palabra del cuento?", "Sigo escuchando y me quedo con quién es y qué hace", "El resto del texto ayuda a entender."),
    ],
    open_task=task("Un adulto lee dos veces: «Lola has a small dog. The dog runs to the park. Lola says: Come here!» Responde en voz alta y, si puedes, en inglés: (1) Who is it? (2) What does the dog do?", "(1) Lola. (2) The dog runs to the park. (Valen también las respuestas en español: Lola; corre al parque.)", ["nombra a Lola", "dice que el perro corre al parque", "responde sin mirar el guion"], ["nota del adulto", "dibujo de Lola y el perro en el parque"], ["decir que Lola corre", "no mencionar el parque"], "Pídele que señale en el dibujo dónde está el perro y que cuente de nuevo lo que pasó con sus palabras."),
    reinforce="Pide a un adulto que lea «Ana has a green frog» y dibuja la rana verde.",
    extend="Escribe tres palabras de acción que hayas oído (jumps, runs, eats) y dibuja un cuento corto con ellas.",
)

register(
    OA1, 4,
    materials="Los textos con sonidos y las descripciones de imágenes escritas en cada ejercicio; un adulto lee el guion; lápiz.",
    use="Aprenderé a usar sonidos, rimas e imágenes para entender mejor lo que escucho. Sirve para adivinar el sentido de un texto aunque no conozca todas las palabras.",
    prior=["Sé decir palabras como cat, hat y dog.", "Sé que un dibujo puede ayudarme a entender un texto."],
    explain=[
        "Los textos en inglés tienen pistas que no son palabras. Un sonido como «woof» ayuda a pensar en un perro, y «meow» en un gato. Una imagen también te cuenta cosas: si ves un perro y una pelota, pensarás que habla de jugar.",
        "Las rimas son palabras que terminan con un sonido parecido: cat y hat, sun y run, bee y tree. Cuando oyes una rima, escucha el final de la línea: las palabras que riman suelen estar en el mismo lugar y puedes adivinar cuál viene.",
        "Pero las pistas no son una orden: son ayudas. Usa la imagen y el sonido, y luego comprueba con las palabras que reconoces. Si la pista y el texto no coinciden, cambia tu idea.",
    ],
    vocab=[("rhyme", "palabras que terminan con un sonido parecido"), ("sound", "sonido"), ("picture", "imagen, dibujo"), ("woof", "guau (sonido del perro)"), ("meow", "miau (sonido del gato)"), ("tree", "árbol")],
    worked=[
        {"title": "Pista de sonido", "problem": ADULT + "«Woof, woof! Come here!» ¿Qué animal habla o suena?", "steps": ["Oigo «woof, woof».", "Ese es el sonido de un perro."], "answer": "Un perro (dog)"},
        {"title": "Pista de rima", "problem": ADULT + "«The cat has a hat. The cat sits on a ...» y la palabra que falta rima con cat. ¿Es mat o dog?", "steps": ["Cat rima con hat.", "Mat termina con el mismo sonido.", "Dog no suena parecido."], "answer": "mat"},
    ],
    mistakes=[
        {"wrong": "Creer que la imagen siempre muestra la respuesta correcta.", "why": "Se piensa que mirar el dibujo es suficiente.", "fix": "Usa la imagen como ayuda y comprueba con las palabras que oyes."},
        {"wrong": "Pensar que dos palabras riman porque empiezan igual.", "why": "Se confunde el comienzo con el final.", "fix": "Escucha el final de la palabra: cat y hat riman, cat y cap no."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Meow, meow!» ¿Qué animal hace ese sonido?", "Un gato", "Meow es el sonido del gato."),
            ex("¿Riman «cat» y «hat»?", "Sí", "Terminan con el mismo sonido -at."),
            ex("¿Qué animal hace «woof»?", "El perro", "Woof es el ladrido en inglés."),
        ],
        "understand": [
            ex("¿Qué es una rima?", "Palabras que terminan con un sonido parecido", "Se escucha el final de las palabras."),
            ex("¿Por qué una imagen puede ayudarte a entender un texto?", "Porque muestra personajes o cosas de las que habla el texto", "Da pistas, pero hay que comprobar con las palabras."),
            ex("¿Qué significa «sound» en español?", "sonido", "Es el ruido que hace algo."),
        ],
        "apply": [
            ex(ADULT + "«The sun is hot. Let's run in the ...» Rima con sun: ¿es fun o dog?", "fun", "Sun y fun terminan con el mismo sonido."),
            ex("Una imagen muestra un perro y una pelota. Un adulto lee: «Woof! The dog has a ...». ¿Qué palabra falta: ball o cat?", "ball", "La imagen muestra una pelota."),
            ex(ADULT + "«A bee is in the tree. The bee says: Bzz, bzz!» ¿Qué sonido hace la abeja?", "Bzz", "El texto lo dice."),
        ],
        "reason": [
            ex("En una imagen se ve un gato, pero el adulto lee «Woof, woof!». ¿Qué pistas no coinciden y qué debes hacer?", "El sonido woof es de un perro; debo cambiar mi idea y volver a escuchar", "Si la pista y el texto no coinciden, se cambia la idea."),
            ex("¿Por qué es útil saber que «bee» rima con «tree»?", "Porque puedo adivinar la palabra del final de la línea", "La rima ayuda a predecir el final."),
        ],
        "challenge": [
            ex("Escribe una palabra que rime con «bat».", "Por ejemplo: cat, hat o mat", "Las tres terminan en -at."),
            ex("Une cada sonido con su animal: (a) woof (b) meow (c) quack. Animales: gato, pato, perro.", "a = perro, b = gato, c = pato", "Cada sonido tiene su animal."),
        ],
    },
    context=[ex("En la plaza un niño escucha de lejos «Quack, quack!» y ve un estanque. ¿Qué animal piensa que hay?", "Un pato", "Quack es el sonido del pato y el estanque es su lugar típico.")],
    selfcheck=[
        ex("¿Riman «sun» y «run»?", "Sí", "Terminan en -un."),
        ex("¿Qué animal hace «meow»?", "El gato", "Meow es el sonido de un gato."),
        ex("¿Por qué conviene comprobar la imagen con las palabras?", "Porque la imagen es una ayuda y no siempre muestra todo", "Así se evita adivinar mal."),
    ],
    open_task=task("Un adulto lee este mini cuento: «The cat is on the mat. The cat has a hat. Meow, meow!» Dibuja lo que oyes: el gato, la alfombra y el sombrero. Después di dos palabras que riman en el cuento.", "Dibujo con un gato sobre una alfombra con sombrero. Rimas: cat y mat (también hat).", ["dibuja al gato", "dibuja alfombra y sombrero", "dice dos palabras que riman"], ["dibujo", "nota del adulto"], ["dibujar un perro", "decir cat y dog como rima"], "Haz que compare su dibujo con el texto y corrija solo lo que no coincida."),
    reinforce="Escucha a un adulto leer «cat, hat, mat» y repite las tres palabras señalando el final igual.",
    extend="Escribe dos pares de palabras que rimen en inglés y dibuja cada una.",
)

register(
    OA1, 5,
    materials="Los textos y preguntas escritas en cada ejercicio, que lee un adulto; lápiz y una hoja para tapar el guion.",
    use="Aprenderé a decir de qué trata de manera general lo que escuché en inglés. Sirve para mostrar que entendí un texto aunque no recuerde todos los detalles.",
    prior=["Sé reconocer chants, diálogos y cuentos.", "Sé decir quién es el personaje y qué hace."],
    explain=[
        "Entender un texto en general (gist) es poder decir de qué trata. No es lo mismo que recordar cada palabra. Si escuchas «Pia has a ball. She plays with the ball. She is happy», entiendes que Pía juega con su pelota y está contenta.",
        "Para decir la idea general, pregúntate: ¿quién?, ¿qué hace? y ¿cómo termina? Luego responde con una frase corta, en español o en inglés simple: «Pía juega con una pelota».",
        "En un diálogo, la idea general es de qué hablan las personas. En un chant es qué te piden hacer. En un cuento es qué le pasa al personaje. Después de escuchar, vuelve a escuchar para comprobar tu idea.",
    ],
    vocab=[("main idea", "idea principal"), ("happy", "contento"), ("plays", "juega"), ("ball", "pelota"), ("today", "hoy"), ("end", "final")],
    worked=[
        {"title": "Idea general de un cuento", "problem": ADULT + "«Pia has a ball. She plays with the ball. She is happy.» ¿De qué trata?", "steps": ["¿Quién? Pía.", "¿Qué hace? Juega con su pelota.", "¿Cómo termina? Está contenta."], "answer": "Pía juega con su pelota y está contenta"},
        {"title": "Idea general de un diálogo", "problem": ADULT + "«A: Hello! What's this? B: It's a cat. A: Nice cat!» ¿De qué hablan?", "steps": ["A pregunta qué es algo.", "B dice que es un gato.", "A dice que es lindo."], "answer": "Hablan de un gato"},
    ],
    mistakes=[
        {"wrong": "Responder con una sola palabra que oí al final.", "why": "Se queda con el último detalle.", "fix": "Responde quién, qué hace y cómo termina."},
        {"wrong": "No decir nada porque no entendí todas las palabras.", "why": "Se piensa que hay que traducir todo.", "fix": "Usa las palabras que entendiste para decir la idea general."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Tom has a dog. The dog is big.» ¿Qué tiene Tom?", "Un perro", "Has a dog es tiene un perro."),
            ex(ADULT + "«Tom has a dog. The dog is big.» ¿Cómo es el perro?", "Grande", "Big significa grande."),
            ex(ADULT + "«Lia is happy.» ¿Cómo está Lia?", "Contenta", "Happy es contento o feliz."),
        ],
        "understand": [
            ex("¿Qué significa decir la «idea general» de un texto?", "Decir de qué trata sin repetir todos los detalles", "Es lo más importante del texto."),
            ex("¿Qué tres preguntas ayudan a decir la idea general?", "¿Quién? ¿Qué hace? ¿Cómo termina?", "Resumen mínimo de un cuento."),
            ex("En un chant, ¿qué es la idea general?", "Lo que el chant me pide hacer o decir", "Los chants piden acciones o repiten palabras."),
        ],
        "apply": [
            ex(ADULT + "«Ben has a red car. He drives the car to the park. Ben is happy.» Elige la idea general: (a) Ben pierde su auto (b) Ben pasea en su auto al parque y está contento.", "b", "El texto dice que lleva el auto al parque y está contento."),
            ex(ADULT + "«A: Hello! Do you like apples? B: Yes, I do!» ¿De qué hablan?", "De manzanas", "Apples significa manzanas."),
            ex(ADULT + "«Sit, stand, jump, stop!» ¿Qué te piden hacer?", "Moverme: sentarme, pararme, saltar y detenerme", "Son órdenes de movimiento."),
        ],
        "reason": [
            ex("Un niño dice que el cuento de Pía «es de un perro» porque oyó dog, pero el texto trata de Pía y su pelota. ¿Qué le falta?", "Preguntarse quién y qué hace antes de responder", "No basta con una palabra suelta."),
            ex("¿Por qué conviene volver a escuchar el texto después de dar tu idea?", "Para comprobar si mi idea era correcta", "Escuchar de nuevo permite corregir."),
        ],
        "challenge": [
            ex("Escribe en español una frase que diga la idea general de «Sam has a hat. The wind takes the hat. Sam runs after the hat.»", "Sam persigue su sombrero que se llevó el viento", "Resume quién, qué pasó y qué hace."),
            ex("Ordena los hechos de este cuento: (1) Mia is happy. (2) Mia has a doll. (3) Mia plays with the doll.", "2, 3, 1", "Primero la tiene, luego juega y al final está contenta."),
        ],
    },
    context=[ex(ADULT + "«A: Good morning! B: Good morning! Let's play!» En el patio, dos amigos hablan así. ¿Qué proponen?", "Jugar", "Let's play significa juguemos.")],
    selfcheck=[
        ex("¿Qué significa «happy»?", "contento", "Es una emoción positiva."),
        ex(ADULT + "«Ben has a red car.» ¿Qué tiene Ben?", "Un auto rojo", "Red car es auto rojo."),
        ex("¿Por qué no es necesario entender todas las palabras para decir la idea general?", "Porque con las palabras clave se entiende de qué trata", "El sentido general se apoya en pistas."),
    ],
    open_task=task("Un adulto lee dos veces: «Pia has a red ball. She plays with her dog. Pia is happy.» Di en voz alta la idea general en español o inglés simple, y dibuja la escena.", "Pía juega con su perro y su pelota roja y está contenta. (En inglés: Pia plays with her dog. She is happy.)", ["nombra a Pía", "dice que juega con perro y pelota", "dice que está contenta"], ["dibujo", "nota del adulto"], ["decir solo «dog»", "inventar un final distinto"], "Pídele que cuente el comienzo, el medio y el final con sus dedos."),
    reinforce="Pide a un adulto que lea «Lia is happy» y representa con tu cara cómo se siente.",
    extend="Escribe en español la idea general de un cuento corto de tres líneas inventado por ti.",
)

# ---------------------------------------------------------------- OA 02
register(
    OA2, 1,
    materials="Las instrucciones escritas en cada ejercicio, que lee un adulto; lápiz, un libro o cuaderno y una hoja.",
    use="Aprenderé a entender instrucciones de la sala de clases en inglés. Sirve para seguir lo que pide la profesora sin necesidad de traducción.",
    prior=["Sé que una instrucción pide hacer algo.", "Sé decir «please»."],
    explain=[
        "En la sala de clases se usan órdenes cortas en inglés: Stand up (ponte de pie), Sit down (siéntate), Open your book (abre tu libro), Close your book (cierra tu libro), Listen (escucha), Look (mira) y Raise your hand (levanta la mano). Cuando se dice «please» es más amable.",
        "Una instrucción empieza con la acción: Stand, Sit, Open, Close. Después viene lo que se mueve o se toca: your book, your pencil, the door. Si reconoces la acción y la cosa, sabes qué hacer.",
        "Si no entiendes, puedes decir «Again, please» (otra vez, por favor). Escuchar y actuar es la mejor forma de entender: haz lo que se pide para comprobar que entendiste.",
    ],
    vocab=[("stand up", "ponerse de pie"), ("sit down", "sentarse"), ("open your book", "abre tu libro"), ("close your book", "cierra tu libro"), ("raise your hand", "levanta la mano"), ("again, please", "otra vez, por favor")],
    worked=[
        {"title": "Entender una orden", "problem": ADULT + "«Open your book, please.» ¿Qué debes hacer?", "steps": ["Escucho Open: abrir.", "Escucho your book: tu libro.", "Abro mi libro."], "answer": "Abrir mi libro"},
        {"title": "Elegir la acción", "problem": ADULT + "«Point to the door.» ¿Qué se señala?", "steps": ["Point es señalar.", "The door es la puerta."], "answer": "La puerta"},
    ],
    mistakes=[
        {"wrong": "Confundir «sit down» con «stand up».", "why": "Suenan parecido al principio.", "fix": "Escucha las palabras down y up: bajar y subir."},
        {"wrong": "Quedarse quieto por no entender una palabra.", "why": "Hay miedo a equivocarse.", "fix": "Mira a quien enseña y di «Again, please»."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Stand up.» ¿Qué haces?", "Me pongo de pie", "Stand up es ponerse de pie."),
            ex(ADULT + "«Close your book.» ¿Qué haces?", "Cierro mi libro", "Close es cerrar."),
            ex(ADULT + "«Raise your hand.» ¿Qué haces?", "Levanto la mano", "Raise your hand es levantar la mano."),
        ],
        "understand": [
            ex("¿Qué significa «sit down»?", "Sentarse", "Down indica hacia abajo."),
            ex("¿Para qué sirve decir «Again, please»?", "Para pedir que repitan", "Es una forma amable de pedir otra vez."),
            ex("¿Qué significa «listen»?", "escuchar", "Se usa para pedir atención."),
        ],
        "apply": [
            ex(ADULT + "«Open your book. Look at the picture.» ¿Qué haces después de abrir el libro?", "Miro el dibujo", "Look at the picture es mira el dibujo."),
            ex(ADULT + "«Point to the door.» ¿Qué señalas?", "La puerta", "Door significa puerta."),
            ex(ADULT + "«Come here, please.» ¿Hacia dónde vas?", "Voy hacia quien me llama", "Come here es ven aquí."),
        ],
        "reason": [
            ex("Ana escuchó «Sit down» y se paró. ¿Qué palabra le dio la pista?", "Sit significa sentarse y down indica abajo", "Debió leer las dos palabras juntas."),
            ex("¿Por qué «please» hace la orden más amable?", "Porque significa por favor", "Es una palabra de cortesía."),
        ],
        "challenge": [
            ex(ADULT + "«Stand up. Raise your hand. Sit down. Close your book.» Escribe con números en qué orden hay que hacer estas acciones: (1) sentarse (2) cerrar el libro (3) ponerse de pie (4) levantar la mano.", "3, 4, 1, 2", "Se cumple el orden en que se dicen las órdenes."),
            ex("Dos órdenes son (a) Stand up y (b) Sit down. ¿Cuál lleva al cuerpo hacia arriba?", "a", "Up significa arriba y stand up es ponerse de pie."),
        ],
    },
    context=[ex(ADULT + "«Good morning. Sit down, please. Open your book.» La profesora dice esto al comenzar. ¿Qué haces primero?", "Me siento", "Sit down va antes de open your book.")],
    selfcheck=[
        ex("¿Cómo se dice «mira» en inglés?", "look", "Look significa mirar."),
        ex(ADULT + "«Open your book.» ¿Qué haces?", "Abro mi libro", "Open es abrir."),
        ex("¿Qué respondes si no entiendes una orden?", "Again, please", "Es la frase amable para pedir que repitan."),
    ],
    open_task=task("Un adulto da cuatro órdenes lentas: «Stand up. Touch your head. Sit down. Raise your hand.» Hazlas con tu cuerpo. Luego di tú una orden a otra persona: «Clap, please.»", "Se pone de pie, se toca la cabeza, se sienta y levanta la mano. Luego dice «Clap, please.»", ["hace las cuatro órdenes en orden", "dice una orden con «please»", "pide repetir si no entiende"], ["nota del adulto", "video con permiso"], ["sentarse antes de tocar la cabeza", "no decir please"], "Repite con él las órdenes que olvidó, poniendo un gesto para cada una."),
    reinforce="Haz con tu cuerpo «Stand up» y «Sit down» siguiendo la voz de un adulto.",
    extend="Escribe tres órdenes más de clase en inglés, por ejemplo «Listen» y «Look», y dibuja cada una.",
)

register(
    OA2, 2,
    materials="Los textos con habilidades escritos en cada ejercicio, que lee un adulto; lápiz y papel.",
    use="Aprenderé a entender qué sabe hacer una persona. Sirve para conocer a otros, decir qué puedo hacer yo y preguntar a mis compañeros.",
    prior=["Sé decir «hello» y mi nombre en inglés.", "Sé qué significa correr, saltar y nadar."],
    explain=[
        "En inglés, para decir lo que alguien sabe hacer se usa «can»: I can run (yo puedo correr), She can swim (ella puede nadar). Para decir lo que no puede hacer se usa «can't»: I can't fly (no puedo volar).",
        "Para preguntar, se pone can primero: Can you jump? (¿Puedes saltar?). Se responde Yes, I can (sí puedo) o No, I can't (no puedo). Hay palabras de personas útiles: I (yo), you (tú), he (él), she (ella).",
        "Cuando escuches una frase con can, busca la acción que viene después: run, jump, swim, sing, draw. Esa palabra te dice qué sabe hacer la persona. Si oyes can't, la acción es lo que no puede.",
    ],
    vocab=[("can", "poder, saber hacer"), ("can't", "no poder"), ("run", "correr"), ("swim", "nadar"), ("sing", "cantar"), ("draw", "dibujar")],
    worked=[
        {"title": "Qué sabe hacer", "problem": ADULT + "«I am Leo. I can swim. I can draw.» ¿Qué sabe hacer Leo?", "steps": ["Escucho I can swim: nadar.", "Escucho I can draw: dibujar."], "answer": "Nadar y dibujar"},
        {"title": "Lo que no puede", "problem": ADULT + "«A fish can swim. A fish can't run.» ¿Puede un pez correr?", "steps": ["Escucho can't run.", "Can't significa no puede."], "answer": "No, un pez no puede correr"},
    ],
    mistakes=[
        {"wrong": "Oír «can't» y entender «can».", "why": "Suenan casi iguales.", "fix": "Escucha si hay una t al final y mira el contexto."},
        {"wrong": "Responder «Yes, I do» a «Can you jump?».", "why": "Se usa la respuesta de otras preguntas.", "fix": "Responde con can: Yes, I can o No, I can't."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«I can run.» ¿Qué puede hacer la persona?", "Correr", "Run es correr."),
            ex(ADULT + "«She can sing.» ¿Qué puede hacer ella?", "Cantar", "Sing es cantar."),
            ex(ADULT + "«I can't fly.» ¿Puede volar?", "No", "Can't es no puedo."),
        ],
        "understand": [
            ex("¿Qué significa «can» en «I can swim»?", "puedo o sé", "Can muestra capacidad."),
            ex("¿Cómo se pregunta «¿Puedes saltar?»?", "Can you jump?", "Can va primero en la pregunta."),
            ex("¿Cómo respondes que sí a «Can you draw?»?", "Yes, I can", "Se repite can en la respuesta."),
        ],
        "apply": [
            ex(ADULT + "«A bird can fly. A bird can sing.» ¿Qué sabe hacer un pájaro?", "Volar y cantar", "Fly es volar y sing es cantar."),
            ex(ADULT + "«Tom can run. Tom can't swim.» ¿Qué no puede hacer Tom?", "Nadar", "Can't swim es no puede nadar."),
            ex(ADULT + "«Can you jump? Yes, I can.» ¿Qué responde la persona?", "Que sí puede saltar", "Yes, I can es sí puedo."),
        ],
        "reason": [
            ex(ADULT + "«Ana can swim, but she can't sing.» ¿Cuál es la diferencia entre lo que puede y lo que no puede?", "Puede nadar y no puede cantar", "La palabra but separa lo que sí y no puede."),
            ex("¿Por qué «a dog can run» pero «a dog can't fly»?", "Porque los perros corren y no tienen alas", "Es una capacidad real de cada animal."),
        ],
        "challenge": [
            ex("Completa: «A fish ___ swim. A fish ___ run.» Usa can o can't.", "can, can't", "Un pez nada pero no corre."),
            ex("Escribe en inglés una frase que diga que sabes cantar.", "I can sing", "I can más el verbo sing."),
        ],
    },
    context=[ex(ADULT + "«A: Can you swim? B: Yes, I can. A: Can you fly? B: No, I can't. Ha ha!» Dos amigos juegan a preguntarse. ¿Qué no puede hacer B?", "Volar", "No, I can't responde a Can you fly.")],
    selfcheck=[
        ex(ADULT + "«I can draw.» ¿Qué sabe hacer?", "Dibujar", "Draw es dibujar."),
        ex("¿Qué significa «can't»?", "no puedo", "Es la forma negativa de can."),
        ex("¿Cómo se dice «yo puedo correr» en inglés?", "I can run", "I can más run."),
    ],
    open_task=task("Un adulto te pregunta tres veces: «Can you run?», «Can you sing?» y «Can you fly?». Responde con «Yes, I can» o «No, I can't» y di una frase propia: «I can ...».", "«Yes, I can.» «Yes, I can.» «No, I can't.» «I can draw.»", ["responde con can o can't", "las tres respuestas son claras", "dice una frase propia con «I can»"], ["nota del adulto", "audio con permiso de la familia"], ["responder con Yes, I do", "decir can sin la acción"], "Si la respuesta tiene un error, repítela despacio y anímale a decirla de nuevo."),
    reinforce="Escucha a un adulto decir «I can run» y haz el movimiento de correr.",
    extend="Escribe cuatro frases con «I can» sobre ti, por ejemplo «I can jump».",
)

register(
    OA2, 3,
    materials="Los textos con objetos y cantidades escritos en cada ejercicio, que lee un adulto; lápiz y papel.",
    use="Aprenderé a entender qué tiene una persona y cuántas cosas tiene. Sirve para hablar de mis cosas y de las de otros.",
    prior=["Sé contar hasta 10 en inglés.", "Sé nombrar objetos como ball, book y pencil."],
    explain=[
        "Para decir lo que alguien tiene se usa «have» o «has». Con I y you se dice have: I have a ball (tengo una pelota). Con he, she o el nombre de una persona se dice has: She has two books (ella tiene dos libros).",
        "Cuando el adulto dice un número, escucha el objeto que viene después. Los números del 1 al 10 son: one, two, three, four, five, six, seven, eight, nine y ten. Si hay más de uno, el objeto suele terminar en s: two books, three pencils.",
        "Para preguntar por la cantidad se dice «How many?»: How many pencils? Three pencils. Escucha el número y la cosa, y así sabrás cuántas hay.",
    ],
    vocab=[("have / has", "tener"), ("how many?", "¿cuántos?"), ("book", "libro"), ("pencil", "lápiz"), ("ball", "pelota"), ("two, three, four", "dos, tres, cuatro")],
    worked=[
        {"title": "Quién tiene qué", "problem": ADULT + "«Ana has a pencil. Beto has two books.» ¿Qué tiene Beto?", "steps": ["Escucho Beto has.", "Escucho two books."], "answer": "Dos libros"},
        {"title": "Cuántos hay", "problem": ADULT + "«I have three balls.» ¿Cuántas pelotas tengo?", "steps": ["Three es tres.", "Balls son pelotas."], "answer": "3 pelotas"},
    ],
    mistakes=[
        {"wrong": "Decir «She have a book».", "why": "Se usa have con todas las personas.", "fix": "Con she, he o un nombre se dice has."},
        {"wrong": "Confundir «three» con «tree».", "why": "Son sonidos parecidos.", "fix": "Three es número 3 y tree es árbol: escucha el contexto."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«I have a ball.» ¿Qué tiene la persona?", "Una pelota", "Ball es pelota."),
            ex(ADULT + "«She has two pencils.» ¿Cuántos lápices tiene?", "2", "Two es dos."),
            ex(ADULT + "«Tom has five books.» ¿Cuántos libros tiene Tom?", "5", "Five es cinco."),
        ],
        "understand": [
            ex("¿Qué significa «How many?»", "¿Cuántos?", "Se usa para preguntar cantidades."),
            ex("¿Cuál se usa con «she»: have o has?", "has", "Con he, she e it se usa has."),
            ex("¿Qué significa «I have»?", "yo tengo", "Have es tener."),
        ],
        "apply": [
            ex(ADULT + "«Mia has three red pencils. Leo has one blue pencil.» ¿Quién tiene más lápices?", "Mia", "Tres es mayor que uno."),
            ex(ADULT + "«I have four books and two balls.» ¿Cuántas cosas tengo en total?", "6", "Cuatro libros más dos pelotas son seis cosas."),
            ex(ADULT + "«How many pencils? Three pencils.» ¿Cuántos lápices hay?", "3", "La respuesta es three."),
        ],
        "reason": [
            ex("Un niño dice «She have a ball». ¿Qué error tiene?", "Debe decir has con she", "Se usa has con he, she y los nombres."),
            ex("En «two books» la palabra books termina en s. ¿Qué te dice eso?", "Que hay más de un libro", "La s indica varios objetos."),
        ],
        "challenge": [
            ex(ADULT + "«Ana has seven pencils. Ana gives two pencils to Leo.» ¿Cuántos lápices tiene Ana ahora?", "5", "Siete menos dos son cinco."),
            ex("Escribe una frase en inglés que diga que tienes dos libros.", "I have two books", "I have más número y objeto en plural."),
        ],
    },
    context=[ex(ADULT + "«A: How many apples? B: I have six apples.» Es la hora de colación y dos amigos cuentan. ¿Cuántas manzanas tiene B?", "6", "Six es seis.")],
    selfcheck=[
        ex(ADULT + "«I have a book.» ¿Qué tengo?", "Un libro", "Book es libro."),
        ex("¿Cómo se dice «lápiz» en inglés?", "pencil", "Pencil es lápiz."),
        ex("¿Cómo se pregunta cuántos?", "How many?", "Es la pregunta de cantidad."),
    ],
    open_task=task("Un adulto lee dos veces: «I have three pencils. I have one book. I have two balls.» Dibuja lo que tiene y escribe el número bajo cada grupo. Después di una frase tuya: «I have ...».", "Dibujo con 3 lápices, 1 libro y 2 pelotas, con los números 3, 1 y 2. Frase: «I have a ball.»", ["dibuja las cantidades correctas", "escribe los tres números", "dice una frase con «I have»"], ["dibujo", "nota del adulto"], ["dibujar 2 lápices", "cambiar el objeto"], "Cuenta con él cada grupo con los dedos para comprobar."),
    reinforce="Cuenta en inglés los lápices que tienes en tu estuche: one, two, three...",
    extend="Escribe tres frases con «has» sobre cosas que tienen tus familiares.",
)

register(
    OA2, 4,
    materials="Los textos con lugares y posiciones escritos en cada ejercicio, que lee un adulto; lápiz y papel.",
    use="Aprenderé a entender dónde está algo con palabras como in, on y under. Sirve para encontrar objetos y seguir indicaciones.",
    prior=["Sé nombrar objetos de la sala como table, chair y bag.", "Sé que «where» pregunta dónde."],
    explain=[
        "Para decir dónde está algo se usan palabras de lugar: in (dentro de), on (sobre), under (debajo de) y next to (al lado de). Por ejemplo: The cat is on the chair (el gato está sobre la silla).",
        "La pregunta es «Where is...?» (¿dónde está?). Se responde con It's... y el lugar: Where is the ball? It's under the table. Escucha dos cosas: el objeto y la palabra de lugar.",
        "Lugares comunes: classroom (sala), school (escuela), park (parque), house (casa), garden (jardín). Puedes dibujar lo que oyes para comprobar si entendiste bien la posición.",
    ],
    vocab=[("in", "dentro de"), ("on", "sobre"), ("under", "debajo de"), ("next to", "al lado de"), ("where?", "¿dónde?"), ("park", "parque")],
    worked=[
        {"title": "Dónde está", "problem": ADULT + "«The ball is under the table.» ¿Dónde está la pelota?", "steps": ["Escucho under: debajo.", "Escucho the table: la mesa."], "answer": "Debajo de la mesa"},
        {"title": "Dentro o sobre", "problem": ADULT + "«The pencil is in the bag.» ¿La pencil está dentro o sobre?", "steps": ["Escucho in.", "In es dentro."], "answer": "Dentro de la mochila"},
    ],
    mistakes=[
        {"wrong": "Confundir «in» con «on».", "why": "Suenan casi igual.", "fix": "Fíjate si el objeto está adentro (in) o arriba (on) en el dibujo."},
        {"wrong": "Responder dónde está con un número.", "why": "Se confunde where con how many.", "fix": "Where pide un lugar, no una cantidad."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«The cat is on the chair.» ¿Dónde está el gato?", "Sobre la silla", "On es sobre."),
            ex(ADULT + "«The ball is in the box.» ¿Dónde está la pelota?", "Dentro de la caja", "In es dentro."),
            ex(ADULT + "«The dog is under the table.» ¿Dónde está el perro?", "Debajo de la mesa", "Under es debajo."),
        ],
        "understand": [
            ex("¿Qué significa «where»?", "dónde", "Es la palabra que pregunta por el lugar."),
            ex("¿Cuál es la diferencia entre «on» y «in»?", "On es sobre y in es dentro", "Cada una muestra una posición distinta."),
            ex("¿Qué significa «next to»?", "al lado de", "Indica que algo está junto a otra cosa."),
        ],
        "apply": [
            ex(ADULT + "«Where is the pencil? It's in the bag.» ¿Dónde está el lápiz?", "En la mochila", "Bag es mochila y in es dentro."),
            ex(ADULT + "«The book is next to the lamp.» ¿Dónde está el libro?", "Al lado de la lámpara", "Next to es al lado."),
            ex(ADULT + "«The fish is in the water.» ¿Dónde está el pez?", "En el agua", "Water es agua."),
        ],
        "reason": [
            ex("Si la pelota está «under the chair», ¿la verías arriba o abajo de la silla?", "Abajo", "Under significa debajo."),
            ex("Un gato está parado arriba de un techo. ¿Dices «The cat is in the roof» o «The cat is on the roof»?", "The cat is on the roof", "El gato está sobre el techo, no adentro."),
        ],
        "challenge": [
            ex(ADULT + "«A cat is on the box. A dog is under the box.» ¿Cuál está más arriba?", "El gato", "On es sobre y under es debajo."),
            ex("Escribe una frase en inglés que diga que el libro está sobre la mesa.", "The book is on the table", "Se usa on para sobre."),
        ],
    },
    context=[ex(ADULT + "«A: Where is my bag? B: It's under the chair.» Un niño busca su mochila en la sala. ¿Dónde está?", "Debajo de la silla", "Under the chair es debajo de la silla.")],
    selfcheck=[
        ex(ADULT + "«The ball is on the table.» ¿Está arriba o debajo?", "Arriba, sobre la mesa", "On significa sobre."),
        ex("¿Cómo se dice «parque» en inglés?", "park", "Park es parque."),
        ex("¿Cómo se pregunta dónde está algo?", "Where is...?", "Es la pregunta de lugar."),
    ],
    open_task=task("Un adulto lee dos veces: «The cat is on the chair. The ball is under the table. The book is in the bag.» Dibuja las tres escenas y rotula cada posición con on, under o in.", "Dibujo con un gato sobre una silla (on), una pelota bajo una mesa (under) y un libro en una mochila (in).", ["gato sobre la silla", "pelota debajo de la mesa", "libro dentro de la mochila", "rotula con on, under, in"], ["dibujo", "nota del adulto"], ["dibujar el gato debajo de la silla", "rotular on por in"], "Pídele que señale con el dedo cada posición y que la diga en voz alta."),
    reinforce="Pon un lápiz en, sobre y debajo de tu cuaderno y di cada palabra en inglés.",
    extend="Escribe tres frases sobre dónde están cosas de tu pieza, usando in, on y under.",
)

register(
    OA2, 5,
    materials="Los textos con acciones escritos en cada ejercicio, que lee un adulto; lápiz y papel.",
    use="Aprenderé a entender qué está haciendo alguien en este momento. Sirve para describir lo que veo y para seguir una conversación.",
    prior=["Sé que run es correr y jump es saltar.", "Sé decir I, he y she."],
    explain=[
        "Para contar lo que alguien hace ahora se usa «am», «is» o «are» y la acción terminada en -ing. I am reading (yo estoy leyendo). He is eating (él está comiendo). They are playing (ellos están jugando).",
        "Escucha primero quién hace la acción y luego la palabra terminada en -ing: running, jumping, singing, drawing, reading. Esa palabra te dice qué ocurre en este momento.",
        "Puedes comprobar mirando una imagen o a la persona. Si el adulto dice «She is drawing», tú buscas a quien está dibujando. La pregunta es What is she doing? (¿qué está haciendo ella?).",
    ],
    vocab=[("is / am / are", "estar (en esta forma)"), ("-ing", "terminación que indica acción ahora"), ("reading", "leyendo"), ("eating", "comiendo"), ("playing", "jugando"), ("What is she doing?", "¿qué está haciendo ella?")],
    worked=[
        {"title": "Qué hace ahora", "problem": ADULT + "«Tom is eating an apple.» ¿Qué hace Tom?", "steps": ["Escucho is eating.", "Eating es comiendo."], "answer": "Está comiendo una manzana"},
        {"title": "Quiénes hacen algo", "problem": ADULT + "«They are playing in the park.» ¿Quiénes juegan?", "steps": ["They es ellos.", "Are playing es están jugando."], "answer": "Ellos están jugando en el parque"},
    ],
    mistakes=[
        {"wrong": "Entender «reading» como «leer» siempre y no «leyendo».", "why": "Se pasa por alto el -ing.", "fix": "El -ing indica que la acción pasa ahora."},
        {"wrong": "Decir «I reading» sin am.", "why": "Se olvida el verbo estar.", "fix": "Usa am, is o are: I am reading."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«She is reading.» ¿Qué hace ella?", "Está leyendo", "Reading es leyendo."),
            ex(ADULT + "«He is running.» ¿Qué hace él?", "Está corriendo", "Running es corriendo."),
            ex(ADULT + "«I am drawing.» ¿Qué hago?", "Estoy dibujando", "Drawing es dibujando."),
        ],
        "understand": [
            ex("¿Qué indica la terminación -ing?", "Que la acción pasa ahora", "Es la forma de gerundio."),
            ex("¿Qué significa «What is she doing?»", "¿Qué está haciendo ella?", "Se pregunta por la acción actual."),
            ex("¿Qué palabra se usa con «I»: am, is o are?", "am", "I am es la forma correcta."),
        ],
        "apply": [
            ex(ADULT + "«The boys are playing football.» ¿Quiénes juegan?", "Los niños", "Boys son niños."),
            ex(ADULT + "«Ana is singing and Leo is jumping.» ¿Quién salta?", "Leo", "Leo is jumping."),
            ex(ADULT + "«The dog is sleeping.» ¿Qué hace el perro?", "Duerme", "Sleeping es durmiendo."),
        ],
        "reason": [
            ex(ADULT + "«Mia is eating, but Tom is reading.» ¿Cuál es la diferencia entre ellos?", "Mia come y Tom lee", "Cada uno hace una acción distinta."),
            ex("Un niño dice «She reading». ¿Qué le falta?", "El verbo is", "Se dice She is reading."),
        ],
        "challenge": [
            ex(ADULT + "«Look! Pia is jumping, Leo is singing and Ana is drawing.» ¿Cuántas personas hacen cosas?", "3", "Son Pía, Leo y Ana."),
            ex("Escribe en inglés qué estás haciendo tú ahora si estás leyendo.", "I am reading", "I am más reading."),
        ],
    },
    context=[ex(ADULT + "«Look at the park! A girl is running. A boy is eating. A dog is sleeping.» En la plaza hay tres cosas. ¿Quién duerme?", "El perro", "Sleeping es durmiendo.")],
    selfcheck=[
        ex(ADULT + "«He is eating.» ¿Qué hace él?", "Está comiendo", "Eating es comiendo."),
        ex("¿Cómo se dice «jugando» en inglés?", "playing", "Playing es jugando."),
        ex("¿Qué palabra va con «she»: am, is o are?", "is", "She is es la forma correcta."),
    ],
    open_task=task("Un adulto hace tres acciones y dice: «I am clapping. I am jumping. I am drawing.» Mira bien y repite cada frase con él. Luego haz tú una acción y di «I am ...».", "Repite «I am clapping», «I am jumping», «I am drawing». Luego aplaude y dice «I am clapping.»", ["repite las tres frases", "hace la acción mientras habla", "usa «I am» y una acción en -ing"], ["nota del adulto", "video con permiso de la familia"], ["decir «I clapping»", "no hacer la acción"], "Repite la frase con él y haz la acción juntos."),
    reinforce="Mira a una persona de tu casa y di en voz baja «He is ...» o «She is ...» según lo que hace.",
    extend="Escribe cuatro acciones en -ing que sepas, como running y singing, y dibuja una.",
)

"""Student material for 2.º básico Inglés, EN02 OA 01 (rimas, chants, canciones, cuentos y diálogos) y OA 02 (temas y funciones conocidas).

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado.
El estudiante puede tapar el guion con una hoja mientras el adulto lee.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA1, OA2 = "EN02 OA 01", "EN02 OA 02"
ADULT = "Un adulto lee en voz alta (el estudiante tapa el guion): "


# ---------------------------------------------------------------- OA 01
register(
    OA1, 1,
    materials="Los chants y rimas escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    use="Aprenderé a reconocer rimas y a seguir el patrón de un chant con palmas. Sirve para participar al ritmo cuando escucho inglés, aunque no entienda todas las palabras.",
    prior=["Sé que un chant tiene ritmo y palabras que se repiten.", "Sé decir en inglés algunas palabras como cat, dog, red y blue."],
    explain=[
        "Una rima (rhyme) ocurre cuando dos palabras terminan con el mismo sonido. Cat, hat y mat riman porque todas terminan en «-at». Bee y tree también riman. Para encontrar una rima, no escuches el comienzo de la palabra: escucha el final.",
        "Un chant es un texto corto con ritmo y con un patrón que se repite. Por ejemplo, «Clap, clap, stamp! Clap, clap, stamp!» repite el mismo patrón: dos palmas y un pisotón. Si descubres el patrón, puedes unirte al chant aunque no sepas el significado de todo.",
        "Para responder al ritmo, escucha primero. Luego da una palma por cada golpe fuerte de la voz y repite el patrón con el adulto. Si el texto rima, el final de las líneas te avisa cuándo termina un grupo: ahí puedes hacer una palma más grande.",
    ],
    vocab=[("rhyme", "rima: palabras que terminan con el mismo sonido"), ("chant", "texto con ritmo que se repite"), ("pattern", "patrón: lo que se repite"), ("clap", "aplaudir"), ("stamp", "pisar fuerte"), ("beat", "golpe del ritmo")],
    worked=[
        {"title": "Encontrar la rima", "problem": ADULT + "«The cat is on the mat. The cat has a hat.» ¿Qué palabras riman con cat?", "steps": ["Escucho el final de cada palabra.", "Mat termina igual que cat: «-at».", "Hat también termina en «-at»."], "answer": "mat y hat"},
        {"title": "Seguir el patrón", "problem": ADULT + "«Clap, clap, stamp! Clap, clap, stamp!» ¿Qué haces en el primer grupo?", "steps": ["Escucho que clap se dice dos veces.", "Después viene stamp una sola vez.", "Hago dos palmas y un pisotón."], "answer": "Dos palmas y un pisotón"},
    ],
    mistakes=[
        {"wrong": "Pensar que cat y cap riman porque empiezan igual.", "why": "Se escucha el comienzo en vez del final de la palabra.", "fix": "Escucha el final: cat termina en «-at» y cap termina en «-ap», así que no riman."},
        {"wrong": "Quedarse en silencio hasta entender cada palabra del chant.", "why": "Se piensa que hay que traducir antes de participar.", "fix": "Descubre el patrón que se repite y únete con palmas, aunque no entiendas todo."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Sun, sun, run, run!» ¿Qué dos palabras riman?", "sun y run", "Las dos terminan en «-un»."),
            ex("¿Riman bed y red?", "Sí", "Las dos terminan con el mismo sonido «-ed»."),
            ex("¿Riman cat y dog?", "No", "Cat termina en «-at» y dog en «-og»: sus finales son distintos."),
        ],
        "understand": [
            ex("¿Qué es una rima (rhyme)?", "Palabras que terminan con el mismo sonido", "La rima se escucha en el final de las palabras."),
            ex("¿Qué es el patrón de un chant?", "Lo que se repite en el chant", "El patrón permite unirse sin traducir todo."),
            ex("¿Por qué riman moon y spoon, si empiezan con letras distintas?", "Porque terminan con el mismo sonido «-oon»", "Lo que cuenta es el final, no el comienzo."),
        ],
        "apply": [
            ex(ADULT + "«Star, star, far, far! Look at the car!» ¿Cuál de las palabras rima con star: car o dog?", "car", "Star y car terminan en «-ar»."),
            ex("Elige la palabra que rima con bee: tree, sun o book.", "tree", "Bee y tree terminan con el mismo sonido «-ee»."),
            ex(ADULT + "«Hop, hop, stop!» Das una palma por palabra. ¿Cuántas palmas das?", "3", "Se dicen tres palabras: hop, hop, stop."),
        ],
        "reason": [
            ex("Una niña dice que pen y pig riman porque las dos empiezan con p. ¿Tiene razón?", "No; riman las palabras con el mismo final y estas terminan distinto", "Pen termina en «-en» y pig en «-ig»."),
            ex("El chant dice «Red, red, go to bed». ¿Qué palabra rima con red?", "bed", "Red y bed terminan en «-ed»."),
        ],
        "challenge": [
            ex("Completa con una palabra que rime: «I see a bee in a ___.» Opciones: tree o sun.", "tree", "Bee y tree riman; sun no."),
            ex("En el chant «Red, red, go to bed. Blue, blue, I love you.» escribe las dos parejas de palabras que riman.", "red - bed; blue - you", "Cada pareja termina con el mismo sonido."),
        ],
    },
    context=[ex("En el recreo, un grupo canta: " + ADULT + "«Jump, jump, bump, bump!» ¿Qué dos palabras riman?", "jump y bump", "Las dos terminan con el sonido «-ump».")],
    selfcheck=[
        ex("¿Cómo se dice «rima» en inglés?", "rhyme", "Rhyme es la palabra en inglés para rima."),
        ex("¿Riman hat y mat?", "Sí", "Las dos terminan con el sonido «-at»."),
        ex(ADULT + "«Clap, clap, stamp!» ¿Qué haces al oír stamp?", "Piso fuerte con el pie", "Stamp significa pisar fuerte."),
    ],
    open_task=task("Un adulto lee dos veces este chant: «Cat, cat, sat on a mat. Hat, hat, fat cat!» Aplaude al ritmo y di en voz alta dos palabras que rimen con cat (puedes elegir entre mat, hat, dog o sun; recuerda que riman las que terminan en «-at»).", "«Mat» y «hat» riman con cat.", ["aplaude al ritmo", "dice dos palabras que riman con cat", "no elige dog ni sun"], ["nota del adulto", "foto o video con permiso de la familia"], ["elegir palabras que solo empiezan igual", "no mantener el ritmo"], "Reconoce el ritmo que logró y repite despacio con él el final «-at» para que lo escuche."),
    reinforce="Pide a un adulto que lea «Cat, hat, mat» y haz una palma en cada palabra. Después dibuja un gato con sombrero.",
    extend="Escribe una pareja de palabras que rimen con bed (por ejemplo red) y haz un chant de dos líneas con palmas.",
)

register(
    OA1, 2,
    materials="Las canciones cortas escritas en cada ejercicio, que lee o canta un adulto; lápiz y espacio para moverte.",
    use="Aprenderé a seguir una canción breve con gestos y a reconocer palabras clave de acción. Sirve para participar en una canción en inglés mostrando que entiendes.",
    prior=["Sé que una canción tiene ritmo y partes que se repiten.", "Conozco palabras como clap, jump y sit."],
    explain=[
        "Las canciones para niños suelen tener gestos (actions). Cada palabra clave te dice qué hacer: clap es aplaudir, stamp es pisar fuerte, wave es saludar con la mano, turn es girar, sit es sentarse y stand es ponerse de pie.",
        "Para seguir una canción no necesitas entender cada palabra. Busca las palabras clave, que son las que dicen la acción, y hazlas con el cuerpo. Por ejemplo, en «Wave your hand» oyes wave y haces el gesto con la mano.",
        "Otra palabra de gesto es touch (tocar): Touch your head es «tócate la cabeza». Los gestos también te ayudan a recordar la canción. Si dos versos dicen cosas parecidas, fíjate en lo que cambia: puede cambiar la parte del cuerpo (hand, feet, head) o la acción. Eso te dice qué debes mover.",
    ],
    vocab=[("wave", "saludar con la mano"), ("turn around", "girar, darse la vuelta"), ("sit down", "sentarse"), ("stand up", "ponerse de pie"), ("hand", "mano"), ("feet", "pies")],
    worked=[
        {"title": "Palabra clave de acción", "problem": ADULT + "«Wave, wave, wave your hand.» ¿Qué haces?", "steps": ["La palabra clave es wave.", "Wave significa saludar con la mano.", "La parte del cuerpo es hand."], "answer": "Saludo con la mano"},
        {"title": "Orden de gestos", "problem": ADULT + "«Stamp your feet. Turn around. Sit down.» ¿Qué haces primero y qué haces al final?", "steps": ["Primero oigo stamp your feet.", "Después oigo turn around.", "Al final oigo sit down."], "answer": "Primero piso fuerte con los pies y al final me siento"},
    ],
    mistakes=[
        {"wrong": "Mover una parte del cuerpo equivocada, por ejemplo la cabeza cuando la canción dice feet.", "why": "No se escuchó la palabra clave de la parte del cuerpo.", "fix": "Escucha la palabra clave: feet son los pies y hand es la mano."},
        {"wrong": "Hacer todos los gestos al mismo tiempo.", "why": "No se escuchó el orden de las acciones.", "fix": "Haz un gesto por cada verso, en el mismo orden en que los oyes."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Clap your hands.» ¿Qué haces?", "Aplaudo", "Clap significa aplaudir."),
            ex(ADULT + "«Turn around.» ¿Qué haces?", "Giro, me doy la vuelta", "Turn around significa girar."),
            ex("¿Qué significa «sit down»?", "Sentarse", "Sit es sentarse y down significa abajo."),
        ],
        "understand": [
            ex("En una canción, ¿qué es una palabra clave de acción?", "La palabra que dice qué gesto hacer", "Por ejemplo wave o stamp indican el gesto."),
            ex("¿Qué significan hand y feet?", "mano y pies", "Hand es una mano y feet son los pies."),
            ex("¿Por qué los gestos ayudan a entender una canción?", "Porque muestran que entiendo la palabra de acción", "El cuerpo hace la acción que la palabra nombra."),
        ],
        "apply": [
            ex(ADULT + "«Stamp, stamp, stamp your feet.» ¿Qué parte del cuerpo usas?", "Los pies", "Feet significa pies."),
            ex(ADULT + "«Wave your hand. Stand up. Turn around.» ¿Qué haces en segundo lugar?", "Me pongo de pie", "Stand up es la segunda acción."),
            ex("La canción dice «Touch your head». Touch es tocar y head es cabeza. ¿Qué haces?", "Me toco la cabeza", "Se juntan las dos palabras clave touch y head."),
        ],
        "reason": [
            ex(ADULT + "«Sit down, sit down. Stand up, stand up.» ¿Qué acción cambia en la segunda línea?", "Pasa de sentarse a ponerse de pie", "Sit down y stand up son acciones contrarias."),
            ex("Pedro hizo girar los pies cuando la canción decía «Stamp your feet». ¿Qué debió hacer?", "Pisar fuerte con los pies", "Stamp significa pisar fuerte, no girar."),
        ],
        "challenge": [
            ex("Ordena las acciones de la canción: (1) Sit down. (2) Wave your hand. (3) Stamp your feet. Orden oído: «Wave your hand. Stamp your feet. Sit down.»", "2, 3, 1", "El texto oído dice primero wave, luego stamp y al final sit."),
            ex(ADULT + "«Wave, wave, wave your hand. Stamp, stamp, stamp your feet. Turn around and sit down. Now it's time to eat!» Antes de «Now it's time to eat», ¿cuántas acciones diferentes oyes?", "4", "Wave, stamp, turn y sit son cuatro acciones distintas."),
        ],
    },
    context=[ex("En la clase, la profesora canta: " + ADULT + "«Touch your nose, touch your toes. Clap, clap, clap, and stand up tall.» ¿Qué haces con la palabra clap?", "Aplaudo", "Clap es aplaudir y se dice tres veces.")],
    selfcheck=[
        ex("¿Qué significa «wave»?", "Saludar con la mano", "Wave es mover la mano para saludar."),
        ex(ADULT + "«Stand up.» ¿Qué haces?", "Me pongo de pie", "Stand up significa ponerse de pie."),
        ex("¿Qué haces si no entiendes toda la canción?", "Busco las palabras clave de acción y hago los gestos", "Las palabras clave bastan para seguir la canción."),
    ],
    open_task=task("Un adulto lee o canta dos veces esta canción corta: «Wave, wave, wave your hand. Stamp, stamp, stamp your feet. Turn around and sit down. Now it's time to eat!» Hazla con gestos. Luego, con la ayuda del adulto, di en inglés los cuatro gestos que hiciste: wave, stamp, turn, sit.", "Dice «wave, stamp, turn, sit» mientras muestra cada gesto.", ["hace los cuatro gestos en orden", "dice las cuatro palabras de acción", "mueve la parte del cuerpo correcta"], ["nota del adulto", "foto o video con permiso de la familia"], ["cambiar el orden de los gestos", "usar la mano cuando la canción dice feet"], "Felicítale por los gestos correctos y repite con él, despacio, la palabra que le costó."),
    reinforce="Pide a un adulto que diga «clap, stamp, wave» y haz cada gesto una vez.",
    extend="Inventa un cuarto verso para la canción con la acción jump y su gesto, por ejemplo «Jump, jump, jump up high».",
)

register(
    OA1, 3,
    materials="Los cuentos cortos escritos en cada ejercicio, que lee un adulto; lápiz y una hoja para tapar el guion.",
    use="Aprenderé a reconocer en un cuento oral el personaje, el objeto y la acción. Sirve para entender una historia en inglés aunque no conozca todas las palabras.",
    prior=["Sé que un cuento tiene personajes y cosas que les pasan.", "Conozco palabras como dog, cat, ball, red y big."],
    explain=[
        "Un cuento oral (story) tiene tres pistas que debes escuchar: el personaje (quién es), el objeto (qué cosa aparece) y la acción (qué hace el personaje). Por ejemplo, en «Pablo has a red ball. He kicks the ball.» el personaje es Pablo, el objeto es una pelota roja y la acción es kicks (patea).",
        "Las palabras que dicen acciones suelen terminar en «-s» cuando el personaje es una sola persona o animal: runs, jumps, eats, sees. Las palabras que dicen objetos van a menudo después de a, an o the: a ball, the apple.",
        "Si pierdes una frase, no te detengas. Pide que lo lean otra vez y anota solo tres cosas: nombre del personaje, objeto y acción. Con esas tres pistas puedes contar la historia con tus palabras.",
    ],
    vocab=[("character", "personaje"), ("object", "objeto, cosa"), ("action", "acción"), ("has", "tiene"), ("kicks", "patea"), ("eats", "come")],
    worked=[
        {"title": "Personaje, objeto y acción", "problem": ADULT + "«Pablo has a red ball. He kicks the ball.» ¿Quién es el personaje, cuál es el objeto y qué acción oyes?", "steps": ["El nombre que oigo es Pablo.", "El objeto es a red ball, una pelota roja.", "La acción es kicks, que significa patea."], "answer": "Pablo; una pelota roja; patea"},
        {"title": "Un animal como personaje", "problem": ADULT + "«A big bear is in the forest. The bear sees a red apple. The bear eats the apple.» ¿Qué come el oso?", "steps": ["El personaje es the bear, el oso.", "Busco la palabra eats.", "Después de eats oigo the apple."], "answer": "Una manzana"},
    ],
    mistakes=[
        {"wrong": "Contestar con el nombre de otro personaje del cuento.", "why": "Se mezclan los personajes porque no se anotó el nombre al oírlo.", "fix": "Pide que lo lean otra vez y escribe el nombre del personaje apenas lo oigas."},
        {"wrong": "Tratar de traducir cada palabra del cuento.", "why": "Se pierde el hilo de la historia.", "fix": "Quédate con las tres pistas: personaje, objeto y acción."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Ana has a green frog. The frog jumps.» ¿Cómo se llama la niña?", "Ana", "El texto empieza con el nombre Ana."),
            ex(ADULT + "«Ana has a green frog. The frog jumps.» ¿Qué objeto o animal tiene Ana?", "Una rana verde", "A green frog significa una rana verde."),
            ex(ADULT + "«Ana has a green frog. The frog jumps.» ¿Qué hace la rana?", "Salta", "Jumps significa salta."),
        ],
        "understand": [
            ex("¿Qué significan character, object y action en un cuento?", "personaje, objeto y acción", "Son las tres pistas para seguir una historia oral."),
            ex("¿Qué palabra de acción significa «come»?", "eats", "Eats es la acción de comer."),
            ex("¿Qué significa «has» en «Leo has a cat»?", "tiene", "Has indica lo que alguien tiene."),
        ],
        "apply": [
            ex(ADULT + "«Mia has a blue kite. The kite goes up, up, up!» ¿Qué objeto tiene Mia?", "Una cometa azul", "Blue kite es cometa azul."),
            ex(ADULT + "«A little dog runs in the park. The dog sees a ball.» ¿Qué ve el perro?", "Una pelota", "El texto dice sees a ball."),
            ex(ADULT + "«Leo sits on a chair. Leo eats an apple.» ¿Qué hace Leo con la manzana?", "La come", "Eats an apple significa come una manzana."),
        ],
        "reason": [
            ex(ADULT + "«Sam has a red hat. The wind takes the hat. Sam says: Oh no!» ¿Cómo crees que se siente Sam y qué te lo dice?", "Preocupado o triste; lo dice «Oh no!»", "La exclamación muestra su sentimiento."),
            ex("Una niña dice que Pablo patea un gato, pero el adulto leyó «Pablo has a red ball. He kicks the ball.» ¿Qué debe hacer ella?", "Pedir que lo lean otra vez; Pablo patea una pelota", "El texto dice ball, no cat."),
        ],
        "challenge": [
            ex("Ordena los hechos del cuento del oso: (1) The bear eats the apple. (2) A big bear is in the forest. (3) The bear sees a red apple.", "2, 3, 1", "Primero está en el bosque, luego ve la manzana y al final la come."),
            ex(ADULT + "«Beto has two fish. One fish is red. One fish is blue.» ¿Cuántos peces tiene Beto?", "2", "Two significa dos."),
        ],
    },
    context=[ex("Un abuelo cuenta en inglés en el patio: " + ADULT + "«A little bird is in the garden. The bird sees a worm. The bird eats the worm.» ¿Qué come el pájaro?", "Un gusano", "Worm es gusano y el texto dice eats the worm.")],
    selfcheck=[
        ex(ADULT + "«Ana has a green frog. The frog jumps.» ¿Quién salta?", "La rana", "La rana es quien jumps."),
        ex("¿Cómo se dice «personaje» en inglés?", "character", "Character es el personaje de un cuento."),
        ex("¿Qué tres pistas debes anotar al escuchar un cuento?", "Personaje, objeto y acción", "Con esas pistas se cuenta la historia."),
    ],
    open_task=task("Un adulto lee dos veces: «Lola has a small dog. The dog runs to the park. The dog sees a ball.» Responde en voz alta, en inglés o en español: (1) ¿Quién es el personaje? (2) ¿Cuál es el objeto? (3) ¿Cuál es la acción? Puedes dibujar la escena.", "Personaje: Lola. Objeto: una pelota. Acción: el perro corre (runs).", ["nombra a Lola o al perro", "nombra la pelota", "dice la acción correr"], ["nota del adulto", "dibujo del perro en el parque"], ["mezclar el nombre del personaje con el objeto", "decir que Lola corre"], "Pídele que señale en el dibujo al perro y a la pelota y que cuente la historia con sus palabras."),
    reinforce="Pide a un adulto que lea «Ana has a green frog» y dibuja la rana verde.",
    extend="Escribe tres palabras de acción que hayas oído (jumps, runs, eats) y dibuja un cuento corto con ellas.",
)

register(
    OA1, 4,
    materials="Los mini diálogos escritos en cada ejercicio, que lee un adulto con dos voces (A y B); lápiz.",
    use="Aprenderé a entender un mini diálogo en inglés y a responder a una pregunta. Sirve para conversar con otra persona en clase.",
    prior=["Sé que un diálogo tiene dos voces.", "Conozco las frases «Hello» y «My name is ...»."],
    explain=[
        "Un diálogo (dialogue) es una conversación breve entre dos personas. Una persona pregunta y la otra responde. Por ejemplo: «A: What's your name? B: My name is Ana.» Las preguntas empiezan con palabras como what (qué), how (cómo), can (poder) o do. Con do se pregunta por gustos: «Do you like apples?» (¿te gustan las manzanas?), y se responde «Yes, I do» o «No, I don't».",
        "Para entender un diálogo, escucha quién habla y qué responde. Si la pregunta es «How old are you?», la respuesta lleva un número: «I'm seven.» Si la pregunta es «How are you?» (¿cómo estás?), la respuesta dice un sentimiento: «I'm happy» (estoy contento). Al conocer a alguien se dice «Nice to meet you» (mucho gusto). Si la pregunta es «Can you swim?», la respuesta es «Yes, I can» o «No, I can't».",
        "Después de escuchar, tú también puedes responder. Primero piensa qué pregunta oíste, luego busca en la lista de respuestas la que sirve, y dila con voz clara. Las respuestas cortas son correctas: no necesitas dar frases largas.",
    ],
    vocab=[("What's your name?", "¿Cómo te llamas?"), ("My name is ...", "Me llamo ..."), ("How old are you?", "¿Cuántos años tienes?"), ("Can you swim?", "¿Sabes nadar?"), ("Yes, I can.", "Sí, puedo."), ("No, I can't.", "No, no puedo.")],
    worked=[
        {"title": "Pregunta y respuesta", "problem": ADULT + "«A: Hello! What's your name? B: My name is Ana. A: How old are you? B: I'm seven.» ¿Cuántos años tiene Ana?", "steps": ["A pregunta «How old are you?»", "B responde «I'm seven».", "Seven es siete."], "answer": "7 años"},
        {"title": "Elegir la respuesta", "problem": ADULT + "«A: Can you swim? B: ...» ¿Qué puede responder B si sabe nadar?", "steps": ["La pregunta es can you.", "Si sabe nadar, dice yes.", "Responde con I can."], "answer": "Yes, I can."},
    ],
    mistakes=[
        {"wrong": "Responder «My name is Ana» a la pregunta «How old are you?».", "why": "No se escuchó bien la palabra de la pregunta.", "fix": "Fíjate en la palabra de la pregunta: how old pide un número, what's your name pide un nombre."},
        {"wrong": "Responder «Yes, I do» a «Can you swim?».", "why": "Se mezclan las respuestas de can y de do.", "fix": "Si la pregunta usa can, la respuesta usa can: «Yes, I can.»"},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«A: What's your name? B: My name is Leo.» ¿Cómo se llama B?", "Leo", "B responde My name is Leo."),
            ex(ADULT + "«A: How old are you? B: I'm eight.» ¿Cuántos años tiene B?", "8", "Eight significa ocho."),
            ex(ADULT + "«A: Can you jump? B: Yes, I can.» ¿Puede saltar B?", "Sí", "Yes, I can significa sí, puedo."),
        ],
        "understand": [
            ex("¿Qué significa «What's your name?»", "¿Cómo te llamas?", "What's your name pregunta por el nombre."),
            ex("¿Qué significa «No, I can't»?", "No, no puedo", "Can't es la forma corta de cannot."),
            ex("¿Qué tipo de respuesta pide «How old are you?»", "Un número", "Se responde con la edad, por ejemplo seven."),
        ],
        "apply": [
            ex("Elige la respuesta a «Can you swim?»: (a) I'm seven. (b) Yes, I can. (c) My name is Ana.", "b", "Can you pide yes o no con can."),
            ex("Elige la respuesta a «What's your name?»: (a) Yes, I can. (b) I'm eight. (c) My name is Tomás.", "c", "Pregunta por el nombre y se responde con My name is."),
            ex(ADULT + "«A: Hello, Mia. How are you? B: I'm happy.» ¿Cómo está Mia?", "Contenta", "Happy significa contento."),
        ],
        "reason": [
            ex("Un niño responde «I'm nine» a «What's your name?». ¿Es correcto? ¿Por qué?", "No; esa respuesta es una edad y la pregunta pide un nombre", "Cada pregunta pide un tipo de respuesta."),
            ex(ADULT + "«A: Can you fly? B: No, I can't. But I can run.» ¿Qué puede hacer B?", "Correr", "B dice que no puede volar, pero sí correr."),
        ],
        "challenge": [
            ex("Ordena el diálogo con números: (1) B: I'm Leo. (2) A: Hello! What's your name? (3) A: Nice to meet you, Leo.", "2, 1, 3", "Primero A saluda y pregunta, después B responde y al final A contesta."),
            ex(ADULT + "«A: Do you like apples? B: Yes, I do. A: Do you like fish? B: No, I don't.» ¿Qué le gusta a B?", "Las manzanas", "B dice yes, I do para apples y no, I don't para fish."),
        ],
    },
    context=[ex("En el primer día de clases, una niña nueva habla con Lía. " + ADULT + "«A: Hello! I'm Lía. What's your name? B: My name is Noa. I'm seven.» ¿Cómo se llama la niña nueva y qué edad tiene?", "Noa; siete años", "B dice My name is Noa e I'm seven.")],
    selfcheck=[
        ex("¿Cómo respondes a «Can you run?» si sabes correr?", "Yes, I can.", "Se repite can en la respuesta."),
        ex("¿Qué pregunta pide un nombre?", "What's your name?", "What's your name significa cómo te llamas."),
        ex(ADULT + "«A: How old are you? B: I'm six.» ¿Qué edad tiene B?", "6", "Six significa seis."),
    ],
    open_task=task("Con un adulto, haz este mini diálogo dos veces. El adulto es A y tú eres B. A: «Hello! What's your name?» B (tú): «My name is ...» A: «How old are you?» B (tú): «I'm ...» A: «Can you jump?» B (tú): «Yes, I can» o «No, I can't». Después dibuja a las dos personas y escribe sus nombres.", "«My name is Pedro.» «I'm seven.» «Yes, I can.»", ["responde las tres preguntas", "usa My name is, I'm y can o can't", "habla con voz clara"], ["nota del adulto", "dibujo de las dos personas"], ["responder con un nombre cuando se pregunta la edad", "usar do en lugar de can"], "Felicítale por cada respuesta correcta y repite con él, despacio, la que se le dificultó."),
    reinforce="Pide a un adulto que pregunte «What's your name?» y responde con «My name is ...».",
    extend="Escribe un mini diálogo de tres líneas entre A y B con las palabras hello, name y happy.",
)

register(
    OA1, 5,
    materials="Los cuatro textos escritos en los ejercicios (chant, canción, cuento y diálogo), que lee un adulto; lápiz y una hoja para tapar el guion.",
    use="Aprenderé a mostrar que entiendo cuatro tipos de textos orales: rima, canción, cuento y diálogo. Sirve para comprobar todo lo que he aprendido sobre escuchar inglés.",
    prior=["Reconozco rimas y patrones de un chant.", "Sigo gestos de una canción.", "Distingo personaje, objeto y acción de un cuento.", "Respondo preguntas de un mini diálogo."],
    explain=[
        "Hasta ahora aprendiste que cada tipo de texto tiene pistas distintas. En una rima escuchas el final de las palabras. En un chant escuchas el patrón que se repite. En una canción buscas las palabras clave de acción. En un cuento buscas personaje, objeto y acción. En un diálogo escuchas quién pregunta y quién responde.",
        "Antes de escuchar, mira las preguntas que debes responder. Así sabes qué pista buscar. Si la pregunta dice «Who?» busca un personaje, si dice «What does he do?» busca una acción, si dice «How old?» busca un número.",
        "Después de responder, comprueba pidiendo que lo lean otra vez. Si tu respuesta coincide con las palabras que oyes, está bien. Si no coincide, corrígela. Revisar es parte de escuchar bien.",
    ],
    vocab=[("who", "quién"), ("what", "qué"), ("how old", "cuántos años"), ("listen again", "escuchar otra vez"), ("check", "comprobar"), ("answer", "respuesta")],
    worked=[
        {"title": "Elegir la pista según la pregunta", "problem": ADULT + "«Leo has a yellow duck. The duck swims.» Pregunta: What does the duck do?", "steps": ["La pregunta What does the duck do pide una acción.", "Busco la palabra de acción: swims.", "Swims significa nada."], "answer": "Nada (swims)"},
        {"title": "Comprobar la respuesta", "problem": ADULT + "«A: How old are you? B: I'm eight.» Un niño dijo que B tiene seis años. ¿Cómo lo compruebas?", "steps": ["Pido que lo lean otra vez.", "Escucho el número: eight.", "Eight es ocho, no seis."], "answer": "B tiene 8 años; la respuesta 6 era incorrecta"},
    ],
    mistakes=[
        {"wrong": "Responder sin saber qué pregunta debía contestar.", "why": "No se leyó la pregunta antes de escuchar.", "fix": "Lee la pregunta antes de escuchar y busca esa pista."},
        {"wrong": "No comprobar la respuesta con una segunda escucha.", "why": "Se confía solo en la primera escucha.", "fix": "Pide que lo lean otra vez y revisa tu respuesta."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Hop, hop, stop!» ¿Es un chant o un cuento?", "Un chant", "Tiene ritmo y repite palabras."),
            ex(ADULT + "«A: What's your name? B: I'm Sam.» ¿Es un diálogo o una canción?", "Un diálogo", "Hay dos voces: una pregunta y otra responde."),
            ex(ADULT + "«Clap your hands.» ¿Qué gesto haces?", "Aplaudo", "Clap es aplaudir."),
        ],
        "understand": [
            ex("¿Qué pista buscas en un cuento oral?", "Personaje, objeto y acción", "Con esas tres pistas sigues la historia."),
            ex("¿Qué pista buscas en una rima?", "El final de las palabras", "Las palabras riman cuando terminan igual."),
            ex("¿Por qué conviene leer la pregunta antes de escuchar?", "Para saber qué pista buscar", "La pregunta orienta la atención."),
        ],
        "apply": [
            ex(ADULT + "«Mia has a blue bird. The bird sings.» ¿Qué hace el pájaro?", "Canta", "Sings significa canta."),
            ex(ADULT + "«A: Can you swim? B: No, I can't.» ¿Puede nadar B?", "No", "No, I can't significa no puedo."),
            ex(ADULT + "«Bee, bee, up in the tree.» ¿Qué dos palabras riman?", "bee y tree", "Las dos terminan con el sonido «-ee»."),
        ],
        "reason": [
            ex("Dos niños no están de acuerdo: uno dice que «Stamp your feet» es un diálogo y otro que es una canción con gestos. ¿Quién tiene razón?", "El que dice que es una canción con gestos", "No hay dos voces, pero sí una acción que se hace con el cuerpo."),
            ex(ADULT + "«A: How old are you? B: I'm seven.» Un niño dice que B se llama Seven. ¿Por qué se equivoca?", "Porque seven es un número, la edad, no un nombre", "La pregunta how old pide un número."),
        ],
        "challenge": [
            ex(ADULT + "«A big bear is in the forest. The bear sees a red apple.» Responde: ¿quién es el personaje, qué ve y de qué color es?", "El oso; una manzana; roja", "Bear, apple y red son las palabras clave."),
            ex("Une cada texto con su tipo. (a) «Red, red, go to bed.» (b) «Wave your hand, stamp your feet.» (c) «A: Hello! B: Hi!» (d) «Leo has a cat. The cat runs.»", "a = rima, b = canción con gestos, c = diálogo, d = cuento", "Cada texto tiene sus propias pistas."),
        ],
    },
    context=[ex("En un cumpleaños, una tía lee un cuento para todos los niños. " + ADULT + "«Tom has a green balloon. The wind comes. The balloon goes up.» ¿Qué tiene Tom y qué le pasa?", "Tiene un globo verde y el globo sube", "Balloon es globo; goes up significa sube.")],
    selfcheck=[
        ex("¿Qué haces con una pregunta antes de escuchar?", "La leo para saber qué pista buscar", "Así escuchas con propósito."),
        ex(ADULT + "«Turn around.» ¿Qué haces?", "Giro", "Turn around significa girar."),
        ex("¿Cómo se dice «cuento» en inglés?", "story", "Story es cuento o historia."),
    ],
    open_task=task("Un adulto lee dos veces los cuatro textos: (1) «Hop, hop, stop!» (2) «Stamp your feet. Turn around.» (3) «Ana has a green frog. The frog jumps.» (4) «A: Can you swim? B: Yes, I can.» Para cada uno di si es chant, canción, cuento o diálogo y haz una acción o una respuesta (por ejemplo, el gesto o «Yes, I can»).", "(1) chant; (2) canción; (3) cuento; (4) diálogo.", ["identifica los cuatro tipos de texto", "hace una acción o respuesta para cada uno", "comprueba escuchando otra vez"], ["nota del adulto", "cuadro con los cuatro tipos y una pista de cada uno"], ["confundir chant con canción", "no mencionar la pista que usó"], "Felicítale por cada acierto y vuelve a leer con él el texto que clasificó mal, nombrando la pista."),
    reinforce="Pide a un adulto que lea «Clap, clap, stamp!» y di si es chant, cuento o diálogo.",
    extend="Elige uno de los cuatro textos y haz un dibujo que muestre su pista más importante.",
)

# ---------------------------------------------------------------- OA 02
register(
    OA2, 1,
    materials="Las instrucciones y presentaciones escritas en cada ejercicio, que lee un adulto; lápiz, un cuaderno y un lápiz de color para obedecer las instrucciones.",
    use="Aprenderé a seguir y dar instrucciones de la escuela, y a entender cuando alguien se presenta o presenta a otra persona. Sirve para entender a mi profesor o profesora y conocer amigos.",
    prior=["Sé decir «Hello» y «My name is ...».", "Conozco palabras de la escuela como book, pencil y desk."],
    explain=[
        "Una instrucción (instruction) dice qué debes hacer. En inglés empieza con el verbo: Open your book (abre tu libro), Close the door (cierra la puerta), Stand up (ponte de pie), Sit down (siéntate), Listen (escucha), Look at the board (mira la pizarra), Pick up your pencil (toma tu lápiz).",
        "Para dar una instrucción, usas el mismo verbo con el objeto: Give me the pen (dame el lápiz pasta). Para ser amable, agrega please: Open your book, please. Si alguien te da una instrucción, escucha el verbo y el objeto y haz esa acción. Para decir la edad de un amigo, usa He is o She is: He is eight (él tiene ocho).",
        "Para presentarte (introduce yourself) dices: I'm Ana. Para presentar a otra persona dices: This is my friend, Leo. Si te presentan, puedes responder: Nice to meet you. Esa frase significa «mucho gusto».",
    ],
    vocab=[("open", "abrir"), ("close", "cerrar"), ("stand up / sit down", "ponerse de pie / sentarse"), ("look at", "mirar"), ("This is my friend.", "Este/Esta es mi amigo/a."), ("Nice to meet you.", "Mucho gusto.")],
    worked=[
        {"title": "Seguir una instrucción", "problem": ADULT + "«Open your book, please.» ¿Qué debes hacer?", "steps": ["El verbo es open, que significa abrir.", "El objeto es your book, tu libro.", "Please es por favor."], "answer": "Abrir mi libro"},
        {"title": "Entender una presentación", "problem": ADULT + "«Hello! I'm Ana. This is my friend, Leo.» ¿Quién es Leo?", "steps": ["Ana se presenta con I'm Ana.", "Luego dice This is my friend.", "El amigo es Leo."], "answer": "Leo es el amigo de Ana"},
    ],
    mistakes=[
        {"wrong": "Hacer lo contrario de la instrucción, por ejemplo cerrar el libro cuando dicen open.", "why": "Se confunden los verbos open y close.", "fix": "Open es abrir y close es cerrar; escucha el verbo antes de actuar."},
        {"wrong": "Decir «I'm Leo» para presentar a un amigo.", "why": "I'm sirve solo para presentarse a uno mismo.", "fix": "Para presentar a otra persona, di This is my friend."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Stand up.» ¿Qué haces?", "Me pongo de pie", "Stand up significa ponerse de pie."),
            ex(ADULT + "«Close the door.» ¿Qué haces?", "Cierro la puerta", "Close es cerrar."),
            ex("¿Qué significa «Nice to meet you»?", "Mucho gusto", "Es lo que se dice cuando conoces a alguien."),
        ],
        "understand": [
            ex("¿Con qué parte de la oración empieza una instrucción en inglés?", "Con el verbo", "Open, close y sit son verbos de acción."),
            ex("¿Qué significa «please»?", "por favor", "Please hace la instrucción más amable."),
            ex("¿Cuál frase usas para presentar a otra persona: «I'm Leo» o «This is my friend, Leo»?", "This is my friend, Leo", "I'm Leo es para presentarse uno mismo."),
        ],
        "apply": [
            ex(ADULT + "«Look at the board. Pick up your pencil.» ¿Qué haces primero?", "Miro la pizarra", "Look at the board es la primera instrucción."),
            ex(ADULT + "«Give me the pen, please.» ¿Qué te pide la persona?", "Que le dé el lápiz pasta", "Give me significa dame y pen es lápiz pasta."),
            ex(ADULT + "«Hello! I'm Pía. This is my friend, Dani. He is eight.» ¿Cuántos años tiene Dani?", "8", "Eight significa ocho."),
        ],
        "reason": [
            ex("Un niño cerró su libro cuando la profesora dijo «Open your book». ¿Qué debió hacer y qué palabra debía escuchar?", "Abrirlo; escuchar open", "Open significa abrir."),
            ex("Una niña dice «This is my friend» para presentarse a sí misma. ¿Por qué no es correcto?", "Porque esa frase presenta a otra persona, no a ella", "Para presentarse debe decir I'm y su nombre."),
        ],
        "challenge": [
            ex("Ordena las instrucciones de la clase: (1) Sit down. (2) Open your book. (3) Stand up. Orden oído: «Stand up. Sit down. Open your book.»", "3, 1, 2", "Stand up fue lo primero, luego sit down y al final open your book."),
            ex("Escribe una instrucción en inglés para pedir a alguien que mire la pizarra, usando please.", "Look at the board, please.", "La instrucción lleva el verbo look at, el objeto y please."),
        ],
    },
    context=[ex("En la sala de clases, la profesora dice: " + ADULT + "«Good morning! Listen, please. Open your notebook. Write your name.» ¿Qué debes hacer con el cuaderno?", "Abrirlo", "Open your notebook significa abre tu cuaderno.")],
    selfcheck=[
        ex("¿Cómo se dice «siéntate» en inglés?", "Sit down", "Sit down es la instrucción para sentarse."),
        ex(ADULT + "«Close your book.» ¿Qué haces?", "Cierro mi libro", "Close es cerrar."),
        ex("¿Qué significa «This is my friend»?", "Este es mi amigo o esta es mi amiga", "Se usa para presentar a otra persona."),
    ],
    open_task=task("Con un adulto, juega a «Teacher says». El adulto dice cinco instrucciones y tú las haces: «Stand up. Sit down. Open your book. Close your book. Look at the board.» Después tú le das dos instrucciones en inglés, por ejemplo «Stand up, please» y «Sit down, please». Al final presenta a un familiar así: «This is my ... (mother, father, brother o sister).»", "«Stand up, please.» «Sit down, please.» «This is my mother.»", ["hace las cinco instrucciones", "da dos instrucciones con please", "presenta a un familiar con This is my ..."], ["nota del adulto", "foto o video con permiso de la familia"], ["confundir open con close", "decir I'm en lugar de This is al presentar a otra persona"], "Felicítale por seguir las instrucciones y repite con él, despacio, el verbo que más le costó."),
    reinforce="Pide a un adulto que diga «stand up» y «sit down» y hazlas dos veces cada una.",
    extend="Escribe tres instrucciones de la escuela en inglés usando los verbos open, close y look at.",
)

register(
    OA2, 2,
    materials="Los textos orales escritos en cada ejercicio, que lee un adulto; lápiz.",
    use="Aprenderé a entender cuando alguien dice lo que sabe hacer (ability) y cómo se siente (feelings), por ejemplo con animales salvajes. Sirve para entender descripciones en inglés.",
    prior=["Sé que can significa poder.", "Conozco palabras de animales como lion y monkey."],
    explain=[
        "Para decir lo que sabes o puedes hacer, usas can. I can run (puedo correr), I can swim (puedo nadar), I can sing (puedo cantar). Para decir que no puedes, usas can't: I can't fly (no puedo volar). Los animales también pueden: A monkey can climb (un mono puede trepar), a lion can run (un león puede correr), a fish can swim (un pez puede nadar).",
        "Para decir cómo te sientes, usas I'm y una palabra de sentimiento (feeling): I'm happy (estoy contento), I'm sad (estoy triste), I'm angry (estoy enojado), I'm tired (estoy cansado), I'm scared (tengo miedo), I'm hungry (tengo hambre), I'm thirsty (tengo sed).",
        "Para hablar de otra persona o de un animal, cambia I'm por He's o She's o It's: She's happy (ella está contenta). Para preguntar, usa How are you? (¿cómo estás?), Are you happy? (¿estás contento?), Can you swim? (¿sabes nadar?) o Why? (¿por qué?). También puedes decir lo que alguien no puede hacer: She can't find her ball (no puede encontrar su pelota).",
    ],
    vocab=[("can", "poder, saber hacer algo"), ("can't", "no poder"), ("climb", "trepar"), ("happy / sad", "contento / triste"), ("hungry / thirsty", "con hambre / con sed"), ("scared", "asustado")],
    worked=[
        {"title": "Una habilidad", "problem": ADULT + "«A monkey can climb. A fish can swim.» ¿Qué puede hacer el mono?", "steps": ["Oigo A monkey can ...", "Después de can viene climb.", "Climb es trepar."], "answer": "Trepar"},
        {"title": "Un sentimiento", "problem": ADULT + "«I'm Leo. I'm hungry. I want an apple.» ¿Cómo se siente Leo?", "steps": ["Leo dice I'm.", "La palabra de sentimiento es hungry.", "Hungry es con hambre."], "answer": "Tiene hambre"},
    ],
    mistakes=[
        {"wrong": "Entender «I can't swim» como «puedo nadar».", "why": "No se escuchó la terminación «-n't», que niega.", "fix": "Can't significa no puedo. Escucha si el final es «can» o «can't»."},
        {"wrong": "Decir que happy significa triste.", "why": "Se confunden los sentimientos opuestos happy y sad.", "fix": "Happy es contento y sad es triste; aprende las parejas."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«A lion can run.» ¿Qué puede hacer el león?", "Correr", "Run significa correr."),
            ex(ADULT + "«I'm happy.» ¿Cómo está la persona?", "Contenta", "Happy es contento."),
            ex("¿Qué significa «I can't fly»?", "No puedo volar", "Can't significa no puedo."),
        ],
        "understand": [
            ex("¿Qué palabra usas en inglés para decir «puedo» o «sé hacer»?", "can", "I can se usa para habilidades."),
            ex("¿Qué significa «scared»?", "Asustado o con miedo", "Es un sentimiento."),
            ex("¿Cuál es la palabra opuesta de happy?", "sad", "Happy es contento y sad es triste."),
        ],
        "apply": [
            ex(ADULT + "«An elephant can walk. A bird can fly. A fish can swim.» ¿Qué animal puede volar?", "El pájaro", "Fly significa volar y se dice del bird."),
            ex(ADULT + "«I'm tired. I want to sit down.» ¿Cómo se siente la persona?", "Cansada", "Tired es cansado."),
            ex(ADULT + "«A: Can you sing? B: No, I can't. But I can draw.» ¿Qué sabe hacer B?", "Dibujar", "B dice que no canta, pero sí draw, dibujar."),
        ],
        "reason": [
            ex("Un niño dice que un pez puede volar porque oyó «A fish can ...». ¿Qué palabra debía escuchar después de can?", "swim; el pez puede nadar", "Después de can viene la habilidad."),
            ex(ADULT + "«She's sad. She can't find her ball.» ¿Por qué está triste?", "Porque no puede encontrar su pelota", "Can't find significa no puede encontrar."),
        ],
        "challenge": [
            ex(ADULT + "«A giraffe can walk. A giraffe can't swim. A monkey can climb.» ¿Qué puede hacer la jirafa y qué no puede hacer?", "Camina; no puede nadar", "Walk con can y swim con can't."),
            ex("Une cada animal con lo que puede hacer: (a) a bird (b) a fish (c) a monkey. Habilidades: swim, fly, climb.", "a = fly, b = swim, c = climb", "Cada animal tiene una habilidad propia."),
        ],
    },
    context=[ex("Dos amigos conversan en el patio. " + ADULT + "«A: Are you happy? B: No, I'm sad. A: Why? B: I'm hungry.» ¿Por qué está triste B?", "Porque tiene hambre", "B responde I'm hungry.")],
    selfcheck=[
        ex("¿Cómo dices en inglés «puedo correr»?", "I can run", "Can más el verbo indica la habilidad."),
        ex(ADULT + "«I'm thirsty.» ¿Qué siente la persona?", "Sed", "Thirsty significa con sed."),
        ex("¿Qué animal puede trepar: a monkey o a fish?", "a monkey", "El mono trepa y el pez nada."),
    ],
    open_task=task("Un adulto lee dos veces: «I'm Leo. I can run and jump. I can't swim. Today I'm happy.» Responde: (1) ¿Qué puede hacer Leo? (2) ¿Qué no puede hacer? (3) ¿Cómo se siente? Después di tú tres frases con «I can ...» y una con «I'm ...», por ejemplo «I can draw. I'm tired.»", "Leo corre y salta; no nada; está contento. «I can draw. I'm tired.»", ["responde las tres preguntas", "dice tres frases con I can", "dice una con I'm y un sentimiento"], ["nota del adulto", "dibujo de un animal con lo que puede hacer"], ["decir que Leo puede nadar", "confundir tired con hungry"], "Reconoce lo que respondió bien y pídele que muestre con gestos los sentimientos que dijo."),
    reinforce="Pide a un adulto que diga «I'm happy» y «I'm sad» y haz la cara de cada sentimiento.",
    extend="Dibuja tres animales salvajes y escribe lo que puede hacer cada uno con can, por ejemplo «A lion can run».",
)

register(
    OA2, 3,
    materials="Los textos orales escritos en cada ejercicio, que lee un adulto; lápiz y objetos o dibujos para contar hasta veinte.",
    use="Aprenderé a entender cuando alguien dice lo que tiene (possession) y cuántas cosas son, con números hasta el veinte. Sirve para entender frases con figuras geométricas, útiles escolares y la celebración de Easter.",
    prior=["Conozco los números de uno a diez en inglés.", "Sé decir «I have ...»."],
    explain=[
        "Para decir lo que tienes, usas have. I have a pencil (tengo un lápiz). Para otra persona usas has: She has a ball (ella tiene una pelota). Si preguntas, dices Do you have a pencil? y respondes Yes, I do o No, I don't.",
        "Para decir cuántos, usa los números. Del uno al diez: one, two, three, four, five, six, seven, eight, nine, ten. Del once al veinte: eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty. Con más de uno, la cosa termina en «-s»: two circles (dos círculos).",
        "Estos mismos números se usan con objetos de la escuela, con figuras (circle, square, triangle, rectangle) y con la celebración de Easter (Pascua): I have five Easter eggs (tengo cinco huevos de Pascua). Para preguntar cuántos, dices How many? Por ejemplo: How many eggs? Twelve eggs.",
    ],
    vocab=[("have / has", "tener (yo, tú / él, ella)"), ("How many?", "¿Cuántos?"), ("circle / square / triangle", "círculo / cuadrado / triángulo"), ("egg", "huevo"), ("Easter", "Pascua"), ("eleven ... twenty", "once ... veinte")],
    worked=[
        {"title": "Posesión y cantidad", "problem": ADULT + "«I have twelve crayons.» ¿Cuántos lápices de cera tiene la persona?", "steps": ["Oigo I have.", "El número que oigo es twelve.", "Twelve es doce."], "answer": "12"},
        {"title": "Figuras geométricas", "problem": ADULT + "«I have three triangles and two circles.» ¿Cuántas figuras tiene en total?", "steps": ["Three triangles son 3 triángulos.", "Two circles son 2 círculos.", "Sumo 3 más 2."], "answer": "5 figuras"},
    ],
    mistakes=[
        {"wrong": "Decir «She have a ball».", "why": "Se usa have para todos y no se cambia para she.", "fix": "Con she, he e it se dice has: She has a ball."},
        {"wrong": "Confundir seventeen con seventy.", "why": "Se pierde el final «-teen».", "fix": "Los números del trece al diecinueve terminan en «-teen» y se dicen con fuerza al final."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«I have two pencils.» ¿Cuántos lápices tiene la persona?", "2", "Two significa dos."),
            ex(ADULT + "«She has a red ball.» ¿Qué tiene ella?", "Una pelota roja", "Has a red ball dice lo que tiene."),
            ex("¿Cuál es el número «fifteen»?", "15", "Fifteen significa quince."),
        ],
        "understand": [
            ex("¿Qué significa «How many?»", "¿Cuántos?", "Se usa para preguntar por una cantidad."),
            ex("¿Cuándo se usa has en lugar de have?", "Con he, she, it o el nombre de una persona", "He has, she has, it has, Ana has."),
            ex("¿Qué significa «egg»?", "huevo", "Egg es huevo; Easter egg es huevo de Pascua."),
        ],
        "apply": [
            ex(ADULT + "«I have fourteen books.» ¿Cuántos libros tiene?", "14", "Fourteen significa catorce."),
            ex(ADULT + "«Ana has nineteen stickers.» ¿Cuántos stickers tiene Ana?", "19", "Nineteen significa diecinueve."),
            ex(ADULT + "«I have a square and a circle.» ¿Qué dos figuras tiene?", "Un cuadrado y un círculo", "Square es cuadrado y circle es círculo."),
        ],
        "reason": [
            ex("Un niño oyó «sixteen» y escribió 60. ¿Por qué se equivocó?", "Porque sixteen es 16; el final «-teen» indica que es del trece al diecinueve", "Los números en «-teen» no son decenas completas."),
            ex(ADULT + "«He has twelve eggs. She has eight eggs.» ¿Quién tiene más huevos?", "Él, porque 12 es más que 8", "Twelve es doce y eight es ocho."),
        ],
        "challenge": [
            ex(ADULT + "«I have ten Easter eggs. My friend has seven Easter eggs.» ¿Cuántos huevos hay entre los dos?", "17", "Diez más siete es diecisiete."),
            ex(ADULT + "«In my bag I have eleven pencils and nine pens.» ¿Cuántos son entre lápices y lápices pasta?", "20", "Once más nueve es veinte."),
        ],
    },
    context=[ex("En Pascua, una niña cuenta sus huevos de chocolate. " + ADULT + "«I have six Easter eggs in my basket. My brother has five.» ¿Cuántos huevos tiene su hermano?", "5", "Five significa cinco.")],
    selfcheck=[
        ex("¿Cómo se dice «tengo» en inglés?", "I have", "Have es tener."),
        ex(ADULT + "«I have twenty stickers.» ¿Cuántos stickers tiene?", "20", "Twenty significa veinte."),
        ex("¿Qué figura es un «triangle»?", "Triángulo", "Triangle es triángulo."),
    ],
    open_task=task("Con un adulto, junta objetos pequeños de la casa (por ejemplo, tapas, lápices o botones) hasta tener entre 11 y 20. Cuéntalos en voz alta en inglés y di: «I have ___ (number) ___ (objects).» Un ejemplo: «I have fourteen buttons.» Luego dibuja las figuras circle, square y triangle y di cuántas dibujaste: «I have two circles.»", "«I have fourteen buttons.» «I have two circles.»", ["cuenta los objetos en inglés", "usa I have y el número", "dibuja las tres figuras y las nombra"], ["nota del adulto", "foto del conteo", "dibujo de las figuras"], ["terminar el número como si fuera una decena (sixty en vez de sixteen)", "decir she have"], "Cuenta con él una segunda vez y repite el número más difícil, marcando el final «-teen»."),
    reinforce="Cuenta los dedos de tus manos en inglés de uno a diez y di «I have ten fingers».",
    extend="Escribe en inglés los números del once al veinte en orden y dibuja tantos círculos como indica el número fifteen.",
)

register(
    OA2, 4,
    materials="Los textos orales escritos en cada ejercicio, que lee un adulto; lápiz.",
    use="Aprenderé a entender dónde están las personas y los objetos, y a describir animales y objetos en un lugar (partes de la casa, muebles y lugares de la ciudad). Sirve para entender indicaciones sobre dónde están las cosas.",
    prior=["Conozco palabras como house, table y chair.", "Sé decir «It's a ...»."],
    explain=[
        "Para decir dónde está algo, usas Where is...? (¿dónde está?) y una respuesta con un lugar: It's in the kitchen (está en la cocina). Las palabras de ubicación son: in (en, dentro de), on (sobre), under (debajo de) y next to (al lado de).",
        "Las partes de la casa son kitchen (cocina), bedroom (dormitorio), bathroom (baño), living room (sala) y garden (jardín). Los muebles son bed (cama), table (mesa), chair (silla), sofa (sillón) y desk (escritorio). Los lugares de la ciudad son park (parque), school (escuela), shop (tienda), library (biblioteca) y hospital (hospital).",
        "También puedes describir animales y objetos en un lugar: The cat is under the table (el gato está debajo de la mesa). A monkey is in the tree (un mono está en el árbol). Escucha dos pistas: ¿qué es? y ¿dónde está?",
    ],
    vocab=[("Where is ...?", "¿Dónde está ...?"), ("in / on", "en, dentro de / sobre"), ("under", "debajo de"), ("next to", "al lado de"), ("kitchen / bedroom", "cocina / dormitorio"), ("park / library", "parque / biblioteca")],
    worked=[
        {"title": "Dónde está el gato", "problem": ADULT + "«Where is the cat? It's under the table.» ¿Dónde está el gato?", "steps": ["La respuesta es It's under the table.", "Under significa debajo de.", "Table es mesa."], "answer": "Debajo de la mesa"},
        {"title": "Dónde está la persona", "problem": ADULT + "«Where is Mum? She is in the kitchen.» ¿Dónde está mamá?", "steps": ["Oigo the kitchen.", "In significa en o dentro de.", "Kitchen es cocina."], "answer": "En la cocina"},
    ],
    mistakes=[
        {"wrong": "Entender «on the table» como «debajo de la mesa».", "why": "Se confunden on (sobre) y under (debajo).", "fix": "On es encima de algo y under es debajo de algo; dibuja la escena para comprobar."},
        {"wrong": "Decir «in the park» cuando la persona está al lado: «next to the park».", "why": "No se escuchó la palabra de ubicación.", "fix": "Escucha next to (al lado de) antes de decir el lugar."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«The dog is in the garden.» ¿Dónde está el perro?", "En el jardín", "Garden es jardín."),
            ex(ADULT + "«The book is on the desk.» ¿Dónde está el libro?", "Sobre el escritorio", "On es sobre; desk es escritorio."),
            ex("¿Qué significa «under»?", "debajo de", "Under indica que algo está abajo."),
        ],
        "understand": [
            ex("¿Qué significa «next to»?", "Al lado de", "Next to indica que están juntos, uno al lado del otro."),
            ex("¿Qué pregunta usas para saber la ubicación de algo?", "Where is ...?", "Where significa dónde."),
            ex("¿Cuál de estos lugares es una parte de la casa: kitchen o library?", "kitchen", "Library es biblioteca, un lugar de la ciudad."),
        ],
        "apply": [
            ex(ADULT + "«The ball is under the chair.» ¿Dónde está la pelota?", "Debajo de la silla", "Under the chair es debajo de la silla."),
            ex(ADULT + "«Grandpa is in the living room. He is on the sofa.» ¿Dónde está el abuelo exactamente?", "En el sofá de la sala", "Living room es sala; on the sofa es sobre el sillón."),
            ex(ADULT + "«The shop is next to the library.» ¿Qué lugar está al lado de la biblioteca?", "La tienda", "Next to the library significa al lado de la biblioteca."),
        ],
        "reason": [
            ex("El texto dice «The cat is on the bed». Un niño dice que el gato está debajo. ¿Cómo corriges su idea?", "El gato está sobre la cama, porque on significa sobre", "Under y on tienen significado contrario."),
            ex(ADULT + "«Where is the school? It's next to the park. Where is the hospital? It's next to the school.» ¿Qué está al lado del parque?", "La escuela", "La primera respuesta dice que la escuela está next to the park."),
        ],
        "challenge": [
            ex(ADULT + "«A monkey is in the tree. A lion is under the tree. A bird is on the tree.» ¿Cuál animal está debajo del árbol?", "El león", "Under the tree es debajo del árbol."),
            ex("Une cada frase en inglés con su significado: (a) in the box (b) on the box (c) under the box. Significados: (1) dentro de la caja, (2) sobre la caja, (3) debajo de la caja.", "a = 1, b = 2, c = 3", "In, on y under indican tres lugares distintos."),
        ],
    },
    context=[ex("Mamá llama a su hijo desde la cocina. " + ADULT + "«Where is your bag? It's in the bedroom, under the bed.» ¿Dónde está la mochila?", "En el dormitorio, debajo de la cama", "In the bedroom es en el dormitorio; under the bed, debajo de la cama.")],
    selfcheck=[
        ex("¿Cómo se dice «mesa» en inglés?", "table", "Table es mesa."),
        ex(ADULT + "«The cat is on the sofa.» ¿Dónde está el gato?", "Sobre el sillón", "On the sofa es sobre el sillón."),
        ex("¿Qué es un «bedroom»?", "Un dormitorio", "Bedroom es dormitorio."),
    ],
    open_task=task("Con un adulto, juega a «Where is it?». El adulto esconde una pelota o un calcetín y dice: «Where is the ball?» Tú buscas y respondes en inglés con una de estas frases: «It's in the box.», «It's on the table.», «It's under the chair.» o «It's next to the sofa.» Después tú escondes un objeto y preguntas «Where is the ...?»", "«It's under the chair.»", ["usa It's y la palabra de ubicación correcta", "nombra el mueble o lugar", "pregunta con Where is ...?"], ["nota del adulto", "dibujo con el objeto y el lugar"], ["confundir on con under", "responder solo con el lugar sin usar It's"], "Haz con él un dibujo del objeto y sus tres ubicaciones: in, on y under."),
    reinforce="Pon un lápiz sobre la mesa y di «on the table»; luego ponlo debajo y di «under the table».",
    extend="Dibuja tu casa con tres cuartos y rotula en inglés: kitchen, bedroom y bathroom.",
)

register(
    OA2, 5,
    materials="Los textos orales escritos en cada ejercicio, que lee un adulto; lápiz.",
    use="Aprenderé a entender qué está haciendo alguien ahora mismo y a preguntar por ocupaciones y comida. Sirve para entender frases como «he is cooking» y «I want an apple».",
    prior=["Conozco verbos como run, eat y draw.", "Conozco palabras de comida como apple y bread."],
    explain=[
        "Para decir lo que alguien hace en este momento, usa am, is o are y un verbo con «-ing». I am drawing (estoy dibujando). He is running (él está corriendo). They are eating (ellos están comiendo). Si oyes -ing, la acción está ocurriendo ahora. Otros verbos: cook → is cooking, drink → is drinking (bebiendo), make → is making (haciendo), drive → is driving (manejando), teach → is teaching (enseñando).",
        "Para preguntar por una ocupación, dices What is her job? o Is he a teacher? Las respuestas son cortas: She is a nurse (ella es enfermera). He is a cook (él es cocinero). Ocupaciones: teacher, nurse, doctor, cook, farmer, driver.",
        "Para preguntar por comida, usa What do you want? o Do you like...? y responde I want an apple (quiero una manzana) o Yes, I do. Comidas: apple, bread, milk, rice, fish, egg, cake.",
    ],
    vocab=[("is running", "está corriendo"), ("is cooking", "está cocinando"), ("nurse / doctor", "enfermero(a) / médico(a)"), ("cook", "cocinero(a)"), ("I want ...", "yo quiero ..."), ("milk / bread / rice", "leche / pan / arroz")],
    worked=[
        {"title": "Qué hace ahora", "problem": ADULT + "«Look! The boy is running.» ¿Qué hace el niño ahora?", "steps": ["Oigo is running.", "Running viene de run, correr.", "El «-ing» indica que ocurre ahora."], "answer": "Está corriendo"},
        {"title": "Ocupación", "problem": ADULT + "«A: What is her job? B: She is a nurse.» ¿Cuál es el trabajo de ella?", "steps": ["La pregunta es What is her job.", "La respuesta es She is a nurse.", "Nurse es enfermera."], "answer": "Enfermera"},
    ],
    mistakes=[
        {"wrong": "Decir «He run» para decir que está corriendo.", "why": "Se olvida is y el «-ing».", "fix": "Para hablar de ahora usa is más el verbo con -ing: He is running."},
        {"wrong": "Entender «I want an egg» como «tengo un huevo».", "why": "Se confunde want con have.", "fix": "Want significa querer y have significa tener."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«She is eating.» ¿Qué hace ella ahora?", "Está comiendo", "Eating viene de eat."),
            ex(ADULT + "«He is a doctor.» ¿Qué ocupación tiene?", "Médico", "Doctor es médico."),
            ex("¿Qué significa «milk»?", "leche", "Milk es leche."),
        ],
        "understand": [
            ex("¿Qué indica el final «-ing» en un verbo?", "Que la acción ocurre ahora", "He is running es ahora mismo."),
            ex("¿Qué significa «What is her job?»", "¿Cuál es su trabajo?", "Job es trabajo u ocupación."),
            ex("¿Qué significa «I want a cake»?", "Quiero una torta", "Want es querer y cake es torta."),
        ],
        "apply": [
            ex(ADULT + "«Mum is cooking rice.» ¿Qué cocina mamá?", "Arroz", "Rice es arroz."),
            ex(ADULT + "«Look! The farmer is walking with a cow.» ¿Qué ocupación tiene la persona que camina?", "Granjero o agricultor", "Farmer es la persona que trabaja en el campo."),
            ex(ADULT + "«A: What do you want? B: I want bread and milk.» ¿Qué quiere B?", "Pan y leche", "Bread es pan y milk es leche."),
        ],
        "reason": [
            ex("Un niño oye «The boy runs fast» y otro «The boy is running». ¿Cuál dice que corre ahora mismo?", "The boy is running", "El «-ing» con is indica una acción en este momento."),
            ex(ADULT + "«A: Is she a teacher? B: No, she is a nurse.» ¿Qué ocupación tiene ella?", "Enfermera", "B corrige la pregunta y dice nurse."),
        ],
        "challenge": [
            ex(ADULT + "«Dad is a cook. He is cooking fish now. I am drinking milk.» ¿Qué ocupación tiene papá, qué cocina ahora y qué bebe el niño?", "Cocinero; pescado; leche", "Cook, fish y milk son las palabras clave."),
            ex("Une cada ocupación con su acción de ahora: (a) The driver (b) The cook (c) The teacher. Acciones: is driving, is cooking, is teaching.", "a = is driving, b = is cooking, c = is teaching", "Cada ocupación se relaciona con su verbo."),
        ],
    },
    context=[ex("En un restaurante, un niño escucha: " + ADULT + "«The cook is making a cake. The girl is eating bread. She is happy.» ¿Qué hace la niña?", "Come pan", "Is eating bread significa come pan.")],
    selfcheck=[
        ex("¿Cómo se dice «enfermera» en inglés?", "nurse", "Nurse es enfermera."),
        ex(ADULT + "«He is drawing.» ¿Qué hace él ahora?", "Dibuja", "Drawing viene de draw."),
        ex("¿Qué significa «I want an apple»?", "Quiero una manzana", "Want es querer."),
    ],
    open_task=task("Con un adulto, juega a la mímica: tú haces una acción (por ejemplo run, eat, draw o cook) y el adulto dice «You are running» o «You are eating». Luego, el adulto hace una acción y tú dices «He is ...» o «She is ...». Para terminar, pregunta «What is your job?» y escucha la respuesta, por ejemplo «I am a teacher».", "«She is drawing.» «I am a teacher.»", ["dice dos acciones con is más -ing", "pregunta What is your job?", "entiende la respuesta del adulto"], ["nota del adulto", "foto o video con permiso de la familia"], ["decir He run en lugar de He is running", "no usar -ing"], "Practica con él, despacio, el verbo con -ing que le costó."),
    reinforce="Haz la mímica de eat, run y draw y di cada una con «I am ...ing».",
    extend="Escribe tres frases como «The nurse is walking» con las ocupaciones teacher, cook y doctor.",
)

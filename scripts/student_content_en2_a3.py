"""Student material for 2.º básico Inglés, EN02 OA 05 (responder personal y creativamente a lo escuchado) y OA 06 (leer tipos de texto breves).

Las «escuchas» las lee un adulto en voz alta. Los textos para leer (OA 06) están escritos completos en el enunciado.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA5, OA6 = "EN02 OA 05", "EN02 OA 06"
ADULT = "Un adulto lee en voz alta (el estudiante tapa el guion): "


# ---------------------------------------------------------------- OA 05
register(
    OA5, 1,
    materials="Los textos orales escritos en cada ejercicio, que lee un adulto; papel, lápiz y lápices de colores.",
    use="Aprenderé a reaccionar a lo que escucho con un dibujo y palabras que lo rotulan. Sirve para mostrar lo que entendí y lo que me pareció más importante.",
    prior=["Sé dibujar personas, animales y objetos.", "Sé escribir algunas palabras en inglés como cat, sun y tree."],
    explain=[
        "Un dibujo es una forma de responder a lo que escuchas. Después de oír un texto, puedes dibujar lo que más te importó: un personaje, un animal, un objeto o un lugar. No necesitas dibujar todo; elige lo que te pareció más importante o más lindo.",
        "Para que tu dibujo muestre lo que entendiste, rotúlalo (label). Rotular es escribir palabras junto a las partes del dibujo. Por ejemplo, si dibujas un elefante, escribes elephant. Si dibujas agua, escribes water.",
        "Además del dibujo, puedes decir una frase corta sobre él: «This is an elephant» (este es un elefante) o «I like the elephant» (me gusta el elefante). Así combinas dibujo, palabras y tu opinión. También puedes representar el personaje con una figura de plasticina o de papel recortado y ponerle su rótulo. Palabras que pueden aparecer: kite (cometa), sky (cielo), candle (vela).",
    ],
    vocab=[("draw", "dibujar"), ("label", "rotular, poner nombre"), ("elephant", "elefante"), ("water", "agua"), ("I like ...", "me gusta ..."), ("This is ...", "Esto es ...")],
    worked=[
        {"title": "Dibujar lo importante", "problem": ADULT + "«A big gray elephant is at the zoo. It drinks water. It is happy.» ¿Qué dibujas y qué palabras escribes?", "steps": ["Dibujo un elefante gris.", "Dibujo el agua que bebe.", "Escribo elephant y water."], "answer": "Un elefante gris que bebe agua, con los rótulos elephant y water"},
        {"title": "Decir una frase", "problem": "Dibujaste un elefante. ¿Qué frase en inglés puedes decir para mostrar que te gusta?", "steps": ["Para decir me gusta uso I like.", "El animal es the elephant."], "answer": "I like the elephant."},
    ],
    mistakes=[
        {"wrong": "Dibujar algo que el texto no dice.", "why": "Se inventa en lugar de usar lo que se escuchó.", "fix": "Dibuja solo personajes, animales y objetos que oíste en el texto."},
        {"wrong": "Dibujar sin rotular.", "why": "Se piensa que el dibujo solo basta.", "fix": "Escribe al menos dos palabras en inglés junto al dibujo."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«I see a zebra.» ¿Qué dibujas?", "Una cebra", "Zebra es cebra."),
            ex("¿Qué significa «draw»?", "dibujar", "Draw es dibujar."),
            ex("¿Cómo rotulas el dibujo de un árbol en inglés?", "tree", "Tree es árbol."),
        ],
        "understand": [
            ex("¿Qué significa rotular un dibujo?", "Escribir el nombre de cada parte", "Los rótulos muestran que entendiste las palabras."),
            ex("¿Por qué se dibuja solo lo que se oyó en el texto?", "Porque el dibujo debe mostrar lo que entendí", "No se inventan cosas que el texto no nombra."),
            ex("¿Qué frase dices para mostrar que algo te gusta?", "I like ...", "I like significa me gusta."),
        ],
        "apply": [
            ex(ADULT + "«A girl has a red kite. The kite is in the sky.» Menciona dos cosas que dibujas y su rótulo en inglés.", "Una niña (girl) y una cometa roja (kite)", "Girl y kite aparecen en el texto."),
            ex(ADULT + "«A lion is under the tree. The lion is big.» ¿Dónde dibujas al león?", "Debajo del árbol", "Under the tree es debajo del árbol."),
            ex("Dibujaste una casa con una cocina. ¿Qué rótulo escribes junto a la cocina?", "kitchen", "Kitchen es cocina."),
        ],
        "reason": [
            ex("Un niño dibuja un mono, pero el texto decía «A giraffe is at the zoo». ¿Qué debe cambiar y por qué?", "Dibujar una jirafa porque el texto la nombra", "Giraffe es jirafa."),
            ex("¿Por qué conviene rotular un dibujo con palabras del texto?", "Porque así muestro que entendí esas palabras", "Los rótulos relacionan imagen y texto."),
        ],
        "challenge": [
            ex(ADULT + "«Mia is in the park. She has a blue ball. A dog is next to her.» Escribe tres rótulos en inglés para tu dibujo.", "Mia, ball, dog (o park)", "Son personajes y objetos nombrados."),
            ex("Escribe una frase en inglés que diga qué parte de tu dibujo te gustó más, por ejemplo con un perro: «I like the ...».", "I like the dog.", "I like the más el nombre del dibujo."),
        ],
    },
    context=[ex("En un cumpleaños escuchas: " + ADULT + "«A big cake is on the table. The cake has seven candles.» ¿Cuántas velas dibujas?", "7", "Seven significa siete.")],
    selfcheck=[
        ex("¿Cómo se dice «dibujar» en inglés?", "draw", "Draw es dibujar."),
        ex("¿Qué haces después de dibujar para mostrar lo que entendiste?", "Rotulo el dibujo con palabras en inglés", "Los rótulos muestran comprensión."),
        ex("¿Cómo dices «me gusta» en inglés?", "I like", "I like es me gusta."),
    ],
    open_task=task("Un adulto lee dos veces: «A monkey is in a big tree. It has a banana. The monkey is happy.» Dibuja lo que más te gustó. Escribe en inglés al menos tres rótulos (monkey, tree, banana) y una frase: «I like the ...». Muestra tu dibujo y léela en voz alta.", "Dibujo de un mono con banana en un árbol; rótulos monkey, tree, banana; frase «I like the monkey.»", ["dibuja lo que oyó", "escribe tres rótulos en inglés", "dice una frase con I like"], ["dibujo rotulado", "nota del adulto"], ["dibujar algo que no estaba en el texto", "olvidar los rótulos"], "Celebra los rótulos correctos y pregunta por qué eligió esa parte para dibujar."),
    reinforce="Dibuja un gato y rotula cat.",
    extend="Dibuja un animal salvaje y escribe una frase como «I like the lion». Si quieres, modela el animal con plasticina o recórtalo en papel y rotúlalo.",
)

register(
    OA5, 2,
    materials="Los textos orales escritos en cada ejercicio, que lee un adulto; espacio libre de obstáculos para moverte.",
    use="Aprenderé a mostrar con mímica y acciones que entendí lo que escuché. Sirve para responder con el cuerpo cuando todavía no sé decirlo todo en inglés.",
    prior=["Sé hacer acciones como clap, jump y sit.", "Conozco verbos como run, eat y climb."],
    explain=[
        "Una forma de reaccionar a lo que escuchas es hacer una mímica (mime): mostrar con el cuerpo qué hace un personaje. Si el texto dice «The monkey climbs the tree», haces como si trepases. Si dice «The boy eats an apple», haces como si comieras.",
        "Para actuar bien, escucha las palabras de acción: climb (trepar), eat (comer), run (correr), jump (saltar), swim (nadar), sleep (dormir), drink (beber), fly (volar). Haz un gesto distinto para cada una y mantén el orden del texto.",
        "Actuar con seguridad es importante. Usa un espacio libre, sin cosas que se puedan romper ni muebles filosos. Haz los movimientos despacio y cuida a las personas cerca. Si actúas con otra persona, cada uno hace su gesto y espera su turno.",
    ],
    vocab=[("mime", "mímica, actuar sin palabras"), ("act", "actuar"), ("sleep", "dormir"), ("drink", "beber"), ("swim", "nadar"), ("climb", "trepar")],
    worked=[
        {"title": "Mímica de una acción", "problem": ADULT + "«The monkey climbs the tree.» ¿Qué mímica haces?", "steps": ["La palabra de acción es climbs.", "Climb significa trepar.", "Muevo brazos y piernas como si subiera."], "answer": "Hago como si trepara"},
        {"title": "Orden de dos acciones", "problem": ADULT + "«The boy runs. Then he sits down.» ¿Qué haces primero y qué haces después?", "steps": ["Primero oigo runs.", "Después oigo sits down."], "answer": "Primero corro en el mismo lugar y después me siento"},
    ],
    mistakes=[
        {"wrong": "Hacer un gesto sin escuchar la palabra de acción.", "why": "Se actúa por imitación del compañero.", "fix": "Escucha el verbo y haz el gesto que lo muestra."},
        {"wrong": "Moverse rápido o brusco en un espacio con objetos.", "why": "No se cuidan el espacio ni las personas.", "fix": "Mueve el cuerpo despacio y deja libre el lugar."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«The girl swims.» ¿Qué mímica haces?", "Hago como si nadara", "Swim significa nadar."),
            ex(ADULT + "«The cat sleeps.» ¿Qué mímica haces?", "Hago como si durmiera", "Sleep significa dormir."),
            ex("¿Qué significa «drink»?", "beber", "Drink es beber."),
        ],
        "understand": [
            ex("¿Qué es una mímica?", "Mostrar una acción con el cuerpo sin hablar", "La mímica muestra comprensión con gestos."),
            ex("¿Por qué conviene escuchar los verbos antes de actuar?", "Porque los verbos dicen qué gesto hacer", "Cada verbo es una acción."),
            ex("¿Qué debes cuidar al actuar?", "El espacio y a las personas cercanas", "La seguridad es lo primero."),
        ],
        "apply": [
            ex(ADULT + "«The dog runs and jumps.» ¿Qué dos mímicas haces?", "Corro y salto", "Runs es corre y jumps es salta."),
            ex(ADULT + "«A bird flies. A fish swims.» ¿Qué haces con el segundo animal?", "Hago como si nadara", "Swims es nada."),
            ex(ADULT + "«The boy drinks water.» ¿Qué mímica haces?", "Hago como si bebiera agua", "Drinks water es bebe agua."),
        ],
        "reason": [
            ex("Pedro hizo la mímica de comer cuando el texto decía «The boy sleeps». ¿Qué hizo mal?", "No escuchó el verbo sleeps; debía dormir", "Sleep y eat son acciones distintas."),
            ex("Si dos personas actúan juntas, ¿qué hace cada una?", "Hace su gesto y espera su turno", "Cada una respeta el turno."),
        ],
        "challenge": [
            ex(ADULT + "«First, the monkey climbs. Then it eats. Finally it sleeps.» Escribe el orden de tus tres mímicas.", "Trepar, comer, dormir", "Climb, eat y sleep en ese orden."),
            ex(ADULT + "«The elephant drinks water. The lion sleeps.» ¿Cuántas mímicas haces y cuáles son?", "2: beber y dormir", "Drink y sleep son dos acciones."),
        ],
    },
    context=[ex("En una obra del colegio, el narrador lee: " + ADULT + "«The rabbit jumps. The rabbit eats a carrot.» ¿Qué haces primero?", "Salto", "Jumps es la primera acción.")],
    selfcheck=[
        ex("¿Cómo se dice «trepar» en inglés?", "climb", "Climb es trepar."),
        ex(ADULT + "«The boy runs.» ¿Qué haces?", "Corro", "Runs es corre."),
        ex("¿Qué es «sleep»?", "dormir", "Sleep es dormir."),
    ],
    open_task=task("Con un adulto, haz una mímica del siguiente cuento mientras él lo lee dos veces: «A lion runs. The lion drinks water. Then the lion sleeps.» Después, tú lees (o repites) una acción y el adulto la hace. Al terminar di: «I like the lion!»", "Corre, bebe agua y duerme, en ese orden.", ["hace las tres acciones en orden", "usa gestos claros", "respeta el espacio y el turno"], ["foto o video con permiso de la familia", "nota del adulto"], ["cambiar el orden", "moverse con brusquedad"], "Felicítale por el orden y repite con él el verbo que hizo diferente al texto."),
    reinforce="Haz tres mímicas: run, jump y sleep.",
    extend="Inventa una mini historia de dos acciones con un animal salvaje y represéntala con un adulto.",
)

register(
    OA5, 3,
    materials="Las situaciones y textos escritos en cada ejercicio, que lee un adulto; lápiz y papel.",
    use="Aprenderé a relacionar lo que escucho con mis propias experiencias, de forma segura. Sirve para decir «a mí también me pasa» sin contar datos privados.",
    prior=["Sé decir «I like ...» y «I have ...».", "Sé que algunos datos personales no se comparten con desconocidos."],
    explain=[
        "Conectar lo que escuchas con tu vida (connection) es decir qué tienes en común con el personaje. Si el cuento dice «Leo has a dog», puedes decir «Me too, I have a dog» (yo también tengo un perro) o «I like dogs» (me gustan los perros). Así muestras que entendiste y que lo relacionas contigo. Sam likes pizza significa «a Sam le gusta la pizza». Si no es verdad que tienes algo, di la verdad con I don't have ...: «I don't have a dog» (no tengo un perro).",
        "Hay temas seguros para conectar: comidas, animales, colores, juegos y lugares generales como el parque. Hay datos que no debes compartir en público ni con desconocidos: tu dirección, tu teléfono, el nombre completo de tu escuela, o problemas privados de tu familia.",
        "Cuando no estás seguro de qué compartir, elige un tema general. Por ejemplo, en vez de decir dónde vives, puedes decir «I like the park». Con un adulto de confianza puedes conversar más cosas, pero en un trabajo que otros verán, usa temas generales.",
    ],
    vocab=[("Me too.", "Yo también."), ("I have ...", "Yo tengo ..."), ("I like ...", "Me gusta ..."), ("pet", "mascota"), ("favorite", "favorito"), ("safe", "seguro")],
    worked=[
        {"title": "Conectar con un personaje", "problem": ADULT + "«Ana has a small cat. She likes milk.» Si a ti también te gustan los gatos, ¿qué dices?", "steps": ["Quiero decir que me gustan los gatos.", "Uso I like y la palabra cats."], "answer": "I like cats. / Me too."},
        {"title": "Elegir un tema seguro", "problem": "Quieres mostrar que te gusta un lugar. Opciones: (a) «I like the park.» (b) tu dirección completa. ¿Cuál es seguro?", "steps": ["La dirección es un dato privado.", "El parque es un lugar general."], "answer": "(a) I like the park."},
    ],
    mistakes=[
        {"wrong": "Escribir tu dirección o teléfono en una tarea que otros verán.", "why": "Se piensa que contar más datos muestra más comprensión.", "fix": "Usa temas generales: comidas, animales, colores o juegos."},
        {"wrong": "Decir «Me too» sin que sea verdad.", "why": "Se copia lo que dice otro sin pensar.", "fix": "Di «Me too» solo si es verdad; si no, di «I don't have a dog»."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Leo has a dog.» Si tú también tienes un perro, ¿qué dices?", "Me too", "Me too significa yo también."),
            ex("¿Qué significa «pet»?", "mascota", "Pet es mascota."),
            ex("¿Qué significa «I have a ball»?", "Tengo una pelota", "I have es yo tengo."),
        ],
        "understand": [
            ex("¿Para qué conectas un texto con tu vida?", "Para mostrar que entendí y que lo relaciono conmigo", "La conexión muestra comprensión personal."),
            ex("¿Qué temas son seguros para compartir: comida o dirección?", "Comida", "La dirección es un dato privado."),
            ex("¿Qué significa «favorite»?", "favorito", "Favorite color es color favorito."),
        ],
        "apply": [
            ex(ADULT + "«Mia has a red ball.» Escribe una frase tuya con I have y un objeto.", "I have a ball (u otro objeto cotidiano)", "I have más un objeto cotidiano es una conexión segura."),
            ex(ADULT + "«Sam likes pizza.» Si te gusta la fruta, ¿qué frase dices?", "I like fruit", "I like más una comida."),
            ex("Quieres decir que tu color favorito es el azul. ¿Qué frase dices?", "My favorite color is blue", "My favorite color is ... se usa para el color favorito."),
        ],
        "reason": [
            ex("Un niño escribe su teléfono en el trabajo. ¿Por qué no es una buena idea?", "Porque es un dato privado que otros verán", "Los datos privados no se comparten."),
            ex(ADULT + "«Lia has a green frog.» Un niño dice «Me too» pero no tiene rana. ¿Qué debe decir?", "I don't have a frog", "Se debe decir la verdad."),
        ],
        "challenge": [
            ex("Elige tres temas seguros para conectar con un texto: color favorito, dirección, comida favorita, teléfono, animal favorito.", "color favorito, comida favorita, animal favorito", "Son temas generales y seguros."),
            ex(ADULT + "«Tom likes apples. He has a brown dog.» Escribe dos frases tuyas en inglés que conecten, una con like y otra con have.", "I like apples. I have a dog. (u otras verdaderas)", "Cada frase usa un verbo del texto."),
        ],
    },
    context=[ex("Tu profesora lee: " + ADULT + "«My favorite food is rice. I eat it with chicken.» ¿Qué frase segura puedes decir?", "I like rice (o My favorite food is ...)", "La comida es un tema seguro.")],
    selfcheck=[
        ex("¿Cómo dices «yo también» en inglés?", "Me too", "Me too es yo también."),
        ex("¿Qué dato NO compartes: tu color favorito o tu dirección?", "Mi dirección", "La dirección es privada."),
        ex("¿Cómo se dice «mascota» en inglés?", "pet", "Pet es mascota."),
    ],
    open_task=task("Un adulto lee dos veces: «Leo has a dog. His dog is brown. Leo likes the park.» Escribe o di tres frases en inglés que conecten con tu vida usando solo temas seguros: «I have ...», «I like ...» y «My favorite color is ...». Ejemplo: «I have a cat. I like the park. My favorite color is green.»", "«I have a cat. I like the park. My favorite color is green.»", ["usa I have, I like y My favorite color is", "elige temas seguros", "dice la verdad"], ["frases escritas", "nota del adulto"], ["incluir dirección o teléfono", "copiar la frase del texto sin que sea verdad"], "Revisa juntos que no haya datos privados y celebra las conexiones verdaderas."),
    reinforce="Di en inglés dos cosas que te gustan, por ejemplo «I like apples» y «I like dogs».",
    extend="Escribe tres cosas seguras que puedes compartir en una conversación en inglés.",
)

register(
    OA5, 4,
    materials="Las situaciones escritas en cada ejercicio; lápiz y papel.",
    use="Aprenderé a decir lo que me gusta o no me gusta y a dar una razón sencilla. Sirve para dar mi opinión sobre lo que escucho.",
    prior=["Sé decir «I like ...» y «I don't like ...».", "Conozco palabras como big, small, fast, soft y funny."],
    explain=[
        "Una preferencia (preference) es lo que te gusta más. Para decirla usa I like ... (me gusta) o I don't like ... (no me gusta). Por ejemplo: I like cats. I don't like spiders.",
        "Para dar una razón, usa because, que significa porque. I like cats because they are soft (me gustan los gatos porque son suaves). Las razones sencillas usan palabras como big, small, fast, soft, funny y yummy (rico).",
        "Una razón buena explica tu opinión. «I like pizza because it is yummy» (me gusta la pizza porque es rica). Una razón mala no tiene sentido: «I like pizza because it is funny» (la pizza no es divertida). Elige una palabra que sí describa lo que dices. También puedes decir cómo te sientes con lo que escuchaste: I'm happy (estoy contento) o I'm sad (estoy triste).",
    ],
    vocab=[("because", "porque"), ("soft", "suave"), ("yummy", "rico, delicioso"), ("funny", "divertido, gracioso"), ("fast", "rápido"), ("I don't like ...", "No me gusta ...")],
    worked=[
        {"title": "Preferencia con razón", "problem": "Completa: «I like monkeys because they are ___.» Opciones: funny o yummy.", "steps": ["Los monos hacen cosas divertidas.", "Yummy se usa para comida."], "answer": "funny"},
        {"title": "Opinión negativa", "problem": "A Ana no le gusta la sopa. ¿Cómo lo dice en inglés?", "steps": ["Para decir que no le gusta usa I don't like.", "La comida es soup."], "answer": "I don't like soup."},
    ],
    mistakes=[
        {"wrong": "Dar una razón que no tiene sentido, como «I like bread because it is funny».", "why": "Funny se usa para algo que hace reír, no para el pan.", "fix": "Elige una palabra que describa de verdad: el pan es yummy."},
        {"wrong": "Decir solo «because» sin la razón.", "why": "Se olvida la palabra después de because.", "fix": "Después de because escribe una frase con una palabra de descripción."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué significa «because»?", "porque", "Because introduce la razón."),
            ex("¿Cómo dices «me gusta el pan» en inglés?", "I like bread", "I like es me gusta."),
            ex("¿Cómo dices «no me gusta la sopa» en inglés?", "I don't like soup", "I don't like es no me gusta."),
        ],
        "understand": [
            ex("¿Para qué sirve la palabra because?", "Para dar una razón", "Because explica el porqué."),
            ex("¿Qué significa «yummy»?", "rico o delicioso", "Yummy se usa para la comida."),
            ex("Escuchas un cuento triste y quieres decir cómo te sientes. ¿Qué frase usas: I'm sad o I want sad?", "I'm sad", "I'm más un sentimiento dice cómo me siento."),
        ],
        "apply": [
            ex("Completa: «I like cats because they are ___.» Opciones: soft o big.", "soft", "Los gatos tienen pelaje suave y no son grandes."),
            ex("Completa: «I like cake because it is ___.» Opciones: yummy o big.", "yummy", "Yummy se usa para comida."),
            ex("Completa: «I like horses because they are ___.» Opciones: fast o yummy.", "fast", "Los caballos corren rápido; yummy es para comida."),
        ],
        "reason": [
            ex("Pía dice «I like pizza because it is funny». ¿Qué problema tiene su razón?", "Funny es para algo que hace reír; la pizza se describe con yummy", "La razón debe tener sentido."),
            ex("¿Cuál es una razón mejor: «I like clowns because they are funny» o «because they are yummy»?", "because they are funny", "Los payasos hacen reír."),
        ],
        "challenge": [
            ex("Escribe una frase con preferencia y razón sobre una fruta: «I like ___ because it is ___.» Usa apples o bananas y yummy.", "I like apples because they are yummy. (o bananas)", "La razón yummy tiene sentido para comida."),
            ex("Une cada animal con una razón sencilla: (a) monkey (b) rabbit (c) elephant. Razones: funny, soft, big.", "a = funny, b = soft, c = big", "Cada razón describe al animal."),
        ],
    },
    context=[ex("En clase la profesora pregunta: «Do you like the zoo?» Tu amigo responde: «Yes, I like the zoo because the monkeys are funny». ¿Cuál es su razón?", "Los monos son divertidos", "Funny significa divertido.")],
    selfcheck=[
        ex("¿Cómo se dice «porque» en inglés?", "because", "Because es porque."),
        ex("¿Qué significa «soft»?", "suave", "Soft es suave."),
        ex("¿Qué palabra usas para decir que no te gusta algo?", "I don't like", "I don't like es no me gusta."),
    ],
    open_task=task("Un adulto lee: «Today we talk about animals: cats, monkeys and elephants.» Elige un animal y escribe o di: «I like ___ because they are ___.» Usa una razón de esta lista: soft, funny, big. Luego di un animal que no te gusta con «I don't like ___.» Dibuja tu animal favorito.", "«I like monkeys because they are funny. I don't like spiders.»", ["dice o escribe la preferencia", "da una razón con because", "dice una cosa que no le gusta"], ["frase escrita", "dibujo del animal"], ["dar una razón sin relación", "olvidar because"], "Pregúntale por qué eligió esa razón y celebra las que tienen sentido."),
    reinforce="Di en inglés «I like apples» y «I don't like soup».",
    extend="Escribe dos frases con because sobre tu comida favorita.",
)

register(
    OA5, 5,
    materials="Los textos orales y las consignas escritos en cada ejercicio, que lee un adulto; papel, lápiz y espacio para moverte.",
    use="Aprenderé a combinar dibujo, acción y palabras para responder a un texto oral. Sirve para demostrar de varias maneras lo que entendí y lo que pienso.",
    prior=["Sé dibujar y rotular.", "Sé hacer mímica de acciones.", "Sé decir una preferencia con because."],
    explain=[
        "Puedes responder a lo que escuchas de varias maneras: con un dibujo (draw), con una mímica (act), con una dramatización (drama) o con palabras o frases escritas (write). Una buena respuesta mezcla dos o tres de ellas.",
        "Una dramatización es una escena breve donde dos personas hacen de personajes y dicen frases. Por ejemplo, un niño hace de cocinero y dice «I am a cook», y el otro hace de cliente y dice «I want bread, please». Cada uno espera su turno y habla fuerte y claro.",
        "Cuando mezclas respuestas, cuida que todas muestren lo que entendiste del texto. Puedes dibujar un personaje, hacer su acción y escribir una frase: «I like the monkey because it is funny».",
    ],
    vocab=[("drama", "dramatización, teatro"), ("scene", "escena"), ("character", "personaje"), ("I want ...", "Yo quiero ..."), ("customer", "cliente"), ("write", "escribir")],
    worked=[
        {"title": "Mezclar respuestas", "problem": ADULT + "«The monkey climbs the tree. It eats a banana. It is happy.» ¿Cómo respondes con dibujo, mímica y frase?", "steps": ["Dibujo un mono con una banana.", "Hago la mímica de trepar y comer.", "Escribo «I like the monkey.»"], "answer": "Dibujo, mímica de trepar y comer, y la frase I like the monkey"},
        {"title": "Dramatización con dos personajes", "problem": "En una escena, uno hace de cocinero (cook) y otro de cliente. ¿Qué frase dice el cliente para pedir pan?", "steps": ["El cliente quiere pan.", "Usa I want y please."], "answer": "I want bread, please."},
    ],
    mistakes=[
        {"wrong": "Hacer tres respuestas sin relación con el texto.", "why": "Se llenan hojas sin pensar en lo que se oyó.", "fix": "Cada respuesta debe mostrar algo que dijo el texto."},
        {"wrong": "Hablar muy bajo o tapar la voz del compañero en la dramatización.", "why": "No se respeta el turno.", "fix": "Espera tu turno y habla fuerte y claro."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué significa «drama»?", "dramatización o teatro", "Es actuar una escena."),
            ex(ADULT + "«The cat sleeps.» ¿Qué mímica haces?", "Hago como si durmiera", "Sleep es dormir."),
            ex("¿Cómo dices «yo quiero pan» en inglés?", "I want bread", "I want es yo quiero."),
        ],
        "understand": [
            ex("¿Cuáles son cuatro formas de responder a un texto oral?", "Dibujo, mímica, dramatización y palabras escritas", "Son las formas del OA."),
            ex("¿Qué debe mostrar cualquier respuesta?", "Lo que entendí del texto", "La respuesta debe relacionarse con el texto."),
            ex("¿Qué haces en la dramatización cuando es el turno del otro?", "Espero y escucho", "Cada personaje habla en su turno."),
        ],
        "apply": [
            ex(ADULT + "«A girl has a red ball. She jumps.» ¿Qué dibujas y qué mímica haces?", "Dibujo una niña con pelota roja; hago como si saltara", "Girl, red ball y jumps son las palabras clave."),
            ex("En la escena de la tienda, el cliente dice: «I want an apple, please». ¿Qué responde el vendedor para dársela: Here you are o Sorry?", "Here you are", "Here you are significa aquí tiene."),
            ex(ADULT + "«I see a big elephant.» ¿Qué frase escribes para dar tu opinión?", "I like the elephant", "I like es me gusta."),
        ],
        "reason": [
            ex("Una niña dibuja una casa, pero el texto hablaba de un elefante. ¿Su respuesta es correcta?", "No, porque no muestra lo que dijo el texto", "La respuesta debe relacionarse con el texto."),
            ex("¿Por qué es útil mezclar dibujo, mímica y frase?", "Porque muestro de más formas lo que entendí", "Cada forma muestra algo distinto."),
        ],
        "challenge": [
            ex("Planifica tu respuesta al texto «A monkey eats a banana»: escribe qué dibujas, qué acción haces y qué frase dices.", "Dibujo un mono con banana; hago la mímica de comer; digo «I like the monkey»", "Hay una respuesta de cada tipo."),
            ex("Escribe una mini escena de dos líneas: un cocinero y un cliente que pide leche.", "Customer: I want milk, please. Cook: Here you are.", "Cada personaje dice una línea."),
        ],
    },
    context=[ex("En la escuela, tu grupo representa una tienda de frutas. El cliente dice: «I want two apples, please». ¿Cuántas manzanas da el vendedor?", "2", "Two es dos.")],
    selfcheck=[
        ex("¿Cómo dices «quiero» en inglés?", "I want", "I want es yo quiero."),
        ex("¿Cómo se dice «escena» en inglés?", "scene", "Scene es escena."),
        ex("¿Qué debe mostrar tu respuesta?", "Lo que entendí del texto", "La respuesta muestra comprensión."),
    ],
    open_task=task("Un adulto lee dos veces: «A cook has a cake. A boy says: I want a cake, please. The cook says: Here you are! The boy says: Thank you!» Haz una respuesta mixta: (1) dibuja la escena y rotula cook, boy y cake; (2) represéntala con el adulto con las frases «I want a cake, please», «Here you are» y «Thank you»; (3) escribe una frase: «I like the cake because it is yummy».", "Dibujo con rótulos; dramatización con las tres frases; frase «I like the cake because it is yummy».", ["dibuja y rotula", "dramatiza con frases del texto", "escribe una opinión con because"], ["dibujo rotulado", "foto o video con permiso de la familia", "frase escrita"], ["olvidar la opinión", "no esperar el turno"], "Celebra cada tipo de respuesta y pide que explique cuál mostró mejor lo que entendió."),
    reinforce="Dibuja una torta y di «I like cake».",
    extend="Escribe una escena de tres líneas con un cocinero y un cliente, y represéntala con un adulto.",
)

# ---------------------------------------------------------------- OA 06
register(
    OA6, 1,
    materials="Los textos breves escritos en cada ejercicio; lápiz.",
    use="Aprenderé a reconocer qué tipo de texto en inglés estoy leyendo: cuento, rima, chant, tarjeta de saludo, instrucciones o texto informativo. Sirve para saber cómo leer cada uno.",
    prior=["Sé reconocer palabras frecuentes en inglés.", "Sé que cada texto tiene un formato."],
    explain=[
        "Cada tipo de texto tiene un aspecto distinto. Un cuento (story) empieza muchas veces con «Once upon a time» y cuenta lo que le pasa a un personaje. Una rima (rhyme) tiene palabras que terminan igual. Un chant repite palabras con ritmo. Una tarjeta de saludo (greeting card) empieza con Dear ... o Happy ... y termina con From ... (de parte de).",
        "Las instrucciones (instructions) usan verbos al comienzo de cada línea, como Open, Draw, Color, y a veces están numeradas: 1. 2. 3. Un texto informativo (information) da datos, por ejemplo «Giraffes are tall. They eat leaves».",
        "Para saber qué tipo de texto es, mira cómo empieza, cómo está escrito y qué hace. ¿Cuenta una historia? ¿Da un saludo? ¿Dice qué hacer? ¿Entrega datos? Con esas preguntas puedes decidir.",
    ],
    vocab=[("story", "cuento"), ("rhyme", "rima"), ("greeting card", "tarjeta de saludo"), ("instructions", "instrucciones"), ("information", "información, datos"), ("From", "De parte de")],
    worked=[
        {"title": "Tarjeta de saludo", "problem": "Lee: «Dear Ana, Happy Birthday! You are seven today. From Leo.» ¿Qué tipo de texto es?", "steps": ["Empieza con Dear.", "Dice Happy Birthday.", "Termina con From Leo."], "answer": "Una tarjeta de saludo (greeting card)"},
        {"title": "Instrucciones", "problem": "Lee: «1. Draw a circle. 2. Color it red.» ¿Qué tipo de texto es?", "steps": ["Tiene números.", "Cada línea empieza con un verbo."], "answer": "Instrucciones (instructions)"},
    ],
    mistakes=[
        {"wrong": "Llamar cuento a cualquier texto corto.", "why": "No se mira el formato ni lo que hace el texto.", "fix": "Pregúntate si cuenta una historia, da datos, da un saludo o dice qué hacer."},
        {"wrong": "Pensar que una rima es un cuento si tiene personajes.", "why": "No se fija en el final de las palabras.", "fix": "Si las palabras terminan igual y tienen ritmo, es una rima."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «Once upon a time, a little bird sat on a tree.» ¿Es un cuento o una instrucción?", "Un cuento", "Once upon a time comienza un cuento."),
            ex("Lee: «Dear Mia, Happy Easter! From Leo.» ¿Qué tipo de texto es?", "Una tarjeta de saludo", "Tiene Dear, Happy y From."),
            ex("Lee: «Stand up. Turn around. Sit down.» ¿Qué tipo de texto es?", "Instrucciones", "Cada línea empieza con un verbo."),
        ],
        "understand": [
            ex("¿Qué palabras sugieren una tarjeta de saludo?", "Dear, Happy y From", "Son palabras típicas de una tarjeta."),
            ex("¿Qué diferencia hay entre una rima y un cuento?", "La rima tiene palabras que terminan igual; el cuento cuenta lo que le pasa a un personaje", "Cada uno tiene sus pistas."),
            ex("¿Qué da un texto informativo?", "Datos", "Information significa información."),
        ],
        "apply": [
            ex("Lee: «Giraffes are tall. They eat leaves.» ¿Qué tipo de texto es?", "Informativo", "Da datos sobre un animal."),
            ex("Lee: «Cat, hat, mat, sat.» ¿Qué tipo de texto es?", "Una rima", "Las palabras terminan igual."),
            ex("Lee: «Clap, clap, stamp! Clap, clap, stamp!» ¿Qué tipo de texto es?", "Un chant", "Se repiten palabras con ritmo."),
        ],
        "reason": [
            ex("Lee: «1. Open your book. 2. Look at the board.» Una niña dice que es un cuento. ¿Qué pista dice que no?", "Cada línea empieza con un verbo y hay números", "Esas son pistas de instrucciones."),
            ex("Lee: «Elephants are big. They drink water.» ¿Por qué no es un cuento?", "Porque da datos y no cuenta una historia", "No hay un personaje con una acción única."),
        ],
        "challenge": [
            ex("Une cada texto con su tipo. (a) «Dear Leo, Happy Birthday! From Ana.» (b) «Draw a square. Color it blue.» (c) «Once upon a time, a fish had a hat.» (d) «Zebras have black and white stripes.»", "a = tarjeta, b = instrucciones, c = cuento, d = informativo", "Cada texto tiene sus pistas propias."),
            ex("Escribe el comienzo de una tarjeta de saludo para un cumpleaños.", "Dear ..., Happy Birthday!", "Dear y Happy Birthday son su inicio."),
        ],
    },
    context=[ex("En tu mochila encuentras una nota: «Dear Leo, Happy Easter! I have an egg for you. From Pía». ¿Qué tipo de texto es y quién la escribió?", "Una tarjeta de saludo; Pía", "Termina con From Pía.")],
    selfcheck=[
        ex("¿Cómo se dice «cuento» en inglés?", "story", "Story es cuento."),
        ex("¿Qué palabra marca quién envía una tarjeta?", "From", "From es de parte de."),
        ex("Lee: «Open the door.» ¿Es una instrucción o una rima?", "Una instrucción", "Empieza con un verbo y dice qué hacer."),
    ],
    open_task=task("Lee estos cuatro textos y escribe de qué tipo es cada uno: (1) «Dear Mia, Happy Easter! From Tom.» (2) «Draw a circle. Color it green.» (3) «Pigs are pink. They like mud.» (4) «Once upon a time, a cat found a hat.» Opciones: story, greeting card, instructions, information. Escribe una pista de cada uno.", "(1) greeting card; (2) instructions; (3) information; (4) story.", ["clasifica los cuatro textos", "escribe una pista de cada uno", "usa las palabras en inglés"], ["lista de textos y tipos", "nota del adulto"], ["confundir instrucciones con cuento", "no dar la pista"], "Releen juntos cada texto y subrayan la pista que decidió el tipo."),
    reinforce="Lee en voz alta «Happy Birthday!» y di qué tipo de texto empieza así.",
    extend="Escribe una tarjeta de saludo de tres líneas para Easter, con Dear y From.",
)

register(
    OA6, 2,
    materials="Los textos breves escritos en cada ejercicio; lápiz.",
    use="Aprenderé a identificar la idea general de un texto breve en inglés. Sirve para entender de qué trata sin leer cada palabra con calma.",
    prior=["Reconozco tipos de texto.", "Conozco palabras de animales, casa y comida."],
    explain=[
        "La idea general (main idea) es de qué trata todo el texto. No es un detalle pequeño: es lo más importante. Por ejemplo, el texto «A zebra is a wild animal. It has black and white stripes. It lives in Africa.» trata de una cebra.",
        "Para encontrar la idea general, haz tres pasos. Primero, lee el título si lo hay. Segundo, busca las palabras que se repiten. Tercero, pregúntate: ¿De qué hablan todas las frases? La respuesta es la idea general.",
        "Los detalles dan información extra: colores, cantidades, lugares. En «A zebra has black and white stripes», el detalle son las rayas. Distinguir idea general y detalle te ayuda a entender textos más largos.",
    ],
    vocab=[("main idea", "idea general"), ("detail", "detalle"), ("zebra", "cebra"), ("stripes", "rayas"), ("lives in", "vive en"), ("about", "sobre, acerca de")],
    worked=[
        {"title": "Idea general", "problem": "Lee: «A giraffe is tall. It has a long neck. It eats leaves.» ¿De qué trata el texto?", "steps": ["La palabra giraffe se repite con it.", "Todas las frases hablan de la jirafa."], "answer": "De una jirafa"},
        {"title": "Detalle", "problem": "En el texto anterior, ¿qué come la jirafa?", "steps": ["Busco eats.", "Después viene leaves, hojas."], "answer": "Hojas"},
    ],
    mistakes=[
        {"wrong": "Confundir un detalle con la idea general.", "why": "Se elige la última palabra que se leyó.", "fix": "La idea general es de lo que hablan todas las frases."},
        {"wrong": "Quedarse en una palabra que no se entiende.", "why": "Se piensa que hay que entender todas.", "fix": "Sigue leyendo; la idea general aparece en varias frases."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «I have a cat. The cat is black. The cat is small.» ¿De qué animal trata?", "De un gato", "Cat se repite en cada frase."),
            ex("¿Qué significa «main idea»?", "idea general", "Es de qué trata el texto."),
            ex("Lee: «Pizza is yummy. I eat pizza.» ¿De qué comida habla?", "De pizza", "Pizza se repite."),
        ],
        "understand": [
            ex("¿En qué se diferencian la idea general y un detalle?", "La idea general es de qué trata todo el texto; el detalle es un dato pequeño", "El detalle da información extra."),
            ex("¿Qué palabra de la lectura te ayuda a encontrar la idea general?", "La que se repite", "La repetición muestra el tema."),
            ex("¿Qué significa «lives in»?", "vive en", "Se usa para decir dónde vive un animal."),
        ],
        "apply": [
            ex("Lee: «Elephants are big. They are gray. They drink water.» ¿De qué trata?", "De elefantes", "Elephants se repite en las frases."),
            ex("Lee: «The kitchen is in my house. Mum cooks in the kitchen.» ¿De qué trata?", "De la cocina", "Kitchen se repite."),
            ex("Lee: «A square has four sides. A triangle has three sides.» ¿De qué trata?", "De figuras geométricas", "Square y triangle son figuras."),
        ],
        "reason": [
            ex("Lee: «A lion is a big cat. It lives in Africa. It eats meat.» Un niño dice que trata de carne. ¿Qué responde?", "No; trata del león, y la carne es un detalle", "Meat es lo que come, un detalle."),
            ex("Lee: «A monkey lives in a tree. It climbs fast. It likes bananas.» ¿Cuál es un detalle: monkey o bananas?", "bananas", "Monkey es el tema; bananas es un detalle."),
        ],
        "challenge": [
            ex("Lee: «A farmer has a cow. The cow gives milk. The farmer drinks the milk.» Escribe la idea general y un detalle.", "Idea: un granjero y su vaca; detalle: la vaca da leche", "Todo habla del granjero y la vaca."),
            ex("Escribe un texto de tres frases sobre una cebra y subraya la palabra que se repite.", "A zebra is wild. A zebra has stripes. A zebra lives in Africa.", "Zebra se repite en las tres frases."),
        ],
    },
    context=[ex("En la biblioteca lees: «A bear is big. It lives in the forest. It eats fish.» ¿De qué trata el texto?", "De un oso", "Bear es oso y se nombra primero.")],
    selfcheck=[
        ex("¿Cómo se dice «idea general» en inglés?", "main idea", "Main idea es la idea general."),
        ex("Lee: «The sun is hot. The sun is big.» ¿De qué trata?", "Del sol", "Sun se repite."),
        ex("¿Qué es un detalle?", "Un dato pequeño del texto", "Un detalle no es lo más importante."),
    ],
    open_task=task("Lee este texto: «A giraffe is tall. A giraffe has a long neck. A giraffe eats leaves from the trees.» Escribe en una línea la idea general («This text is about a giraffe.») y dos detalles (neck, leaves). Después escribe otro texto de tres frases sobre un animal que elijas (zebra, lion o monkey) y subraya la palabra que se repite.", "Idea general: giraffe. Detalles: long neck, leaves.", ["escribe la idea general", "escribe dos detalles", "escribe un texto de tres frases con una palabra repetida"], ["hoja con idea y detalles", "texto propio"], ["elegir un detalle como idea general", "no repetir la palabra tema"], "Compara su idea general con la palabra más repetida y pídele que justifique."),
    reinforce="Lee «The cat is black. The cat is small.» y di de qué trata.",
    extend="Escribe tres frases sobre un animal salvaje que repitan su nombre y cuenten un detalle distinto en cada una.",
)

register(
    OA6, 3,
    materials="Los textos breves escritos en cada ejercicio; lápiz y papel para dibujar.",
    use="Aprenderé a identificar personajes y acciones en un texto en inglés. Sirve para entender quién hace qué en un cuento, una rima o un chant.",
    prior=["Reconozco personajes y acciones al escuchar.", "Conozco verbos como run, jump y eat."],
    explain=[
        "En un cuento, los personajes son quienes hacen las cosas. Pueden ser personas (Leo, Ana, the girl), animales (the dog, the monkey) o personajes inventados (the dragon). Las acciones son lo que hacen: runs (corre), jumps (salta), eats (come), sees (ve), feeds (da de comer).",
        "Para encontrar al personaje, busca la palabra que va al comienzo y que hace algo: «Leo runs» dice que Leo corre. Para encontrar la acción, busca el verbo que viene después. En «The dog eats a bone», el personaje es the dog y la acción es eats.",
        "Cuando hay más de un personaje, fíjate en quién hace cada acción. En «The cat sees a mouse. The mouse runs», el gato ve y el ratón corre. Dibujar o escribir una tabla de personaje y acción ayuda a no confundirlos.",
    ],
    vocab=[("character", "personaje"), ("action", "acción"), ("sees", "ve"), ("mouse", "ratón"), ("bone", "hueso"), ("runs", "corre")],
    worked=[
        {"title": "Personaje y acción", "problem": "Lee: «The dog eats a bone.» ¿Quién es el personaje y qué hace?", "steps": ["El personaje es the dog.", "La acción es eats.", "Come un hueso."], "answer": "El perro; come un hueso"},
        {"title": "Dos personajes", "problem": "Lee: «The cat sees a mouse. The mouse runs.» ¿Quién corre?", "steps": ["Busco runs.", "Antes de runs está the mouse."], "answer": "El ratón"},
    ],
    mistakes=[
        {"wrong": "Responder con el nombre del primer personaje que aparece.", "why": "No se revisa quién hace la acción.", "fix": "Busca el verbo y pregúntate quién lo hace."},
        {"wrong": "Confundir el objeto con el personaje.", "why": "Se mezcla el objeto con quien actúa.", "fix": "El personaje hace la acción; el objeto la recibe."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «Leo runs.» ¿Quién corre?", "Leo", "Leo es el personaje que runs."),
            ex("Lee: «The monkey jumps.» ¿Qué hace el mono?", "Salta", "Jumps es salta."),
            ex("¿Qué significa «sees»?", "ve", "Sees es ve."),
        ],
        "understand": [
            ex("¿Qué es un personaje?", "Quien hace las acciones en el texto", "Puede ser una persona o un animal."),
            ex("¿Qué palabra de un texto indica la acción?", "El verbo", "El verbo dice lo que hace el personaje."),
            ex("En «The dog eats a bone», ¿cuál es el objeto?", "a bone", "El hueso es lo que come."),
        ],
        "apply": [
            ex("Lee: «The cat sees a mouse. The mouse runs.» ¿Qué hace el gato?", "Ve un ratón", "The cat sees a mouse."),
            ex("Lee: «Ana draws a house. Leo draws a tree.» ¿Quién dibuja un árbol?", "Leo", "Leo draws a tree."),
            ex("Lee: «The bird flies to a tree.» ¿Qué hace el pájaro?", "Vuela hacia un árbol", "Flies es vuela."),
        ],
        "reason": [
            ex("Lee: «The girl has a dog. The dog jumps.» Un niño dice que la niña salta. ¿Qué dice el texto?", "El perro salta", "Jumps va después de the dog."),
            ex("Lee: «The farmer feeds a cow.» ¿Quién es el personaje y quién recibe la acción?", "El granjero actúa; la vaca recibe la comida", "Feeds es da de comer."),
        ],
        "challenge": [
            ex("Lee: «Pablo has a ball. Pablo kicks the ball. The dog runs.» Completa: Pablo = ___ ; dog = ___", "Pablo patea la pelota; el perro corre", "Cada personaje tiene una acción."),
            ex("Lee: «First, the cat sees a mouse. Then the mouse runs. Finally the cat runs.» Ordena lo que pasa: (1) The mouse runs. (2) The cat sees a mouse. (3) The cat runs.", "2, 1, 3", "Primero el gato ve, luego el ratón corre y al final el gato corre."),
        ],
    },
    context=[ex("Lees en una revista infantil: «A little frog sits on a leaf. The frog jumps into the water.» ¿Qué hace la rana después?", "Salta al agua", "Jumps into the water significa salta al agua.")],
    selfcheck=[
        ex("¿Cómo se dice «personaje» en inglés?", "character", "Character es personaje."),
        ex("Lee: «Mia reads a book.» ¿Qué hace Mia?", "Lee un libro", "Reads es lee."),
        ex("Lee: «The bear eats fish.» ¿Quién es el personaje?", "El oso", "The bear es el personaje."),
    ],
    open_task=task("Lee este cuento: «Tom has a kite. Tom runs. A dog sees the kite. The dog jumps.» Haz una tabla con dos columnas: Character (personaje) y Action (acción) y escribe qué hace Tom y qué hace el perro. Después dibuja una escena del cuento y rotúlala.", "Tom: has a kite, runs. Dog: sees the kite, jumps.", ["identifica a Tom y al perro como personajes", "escribe sus acciones", "dibuja la escena y la rotula"], ["tabla de personaje y acción", "dibujo"], ["poner una acción en el personaje equivocado", "poner la cometa como personaje"], "Releen juntos y verifica que cada acción esté bajo el personaje correcto."),
    reinforce="Lee «The dog runs» y dibuja al perro corriendo.",
    extend="Escribe un cuento de tres frases con dos personajes distintos y subraya los verbos.",
)

register(
    OA6, 4,
    materials="Los textos y diálogos breves escritos en cada ejercicio; lápiz.",
    use="Aprenderé a reconocer palabras y expresiones de uso muy frecuente al leer, como «I want ...» y «Here!». Sirve para leer frases completas con confianza.",
    prior=["Conozco chunks como Thank you y Excuse me.", "Sé leer frases cortas en inglés."],
    explain=[
        "Al leer, algunas frases aparecen una y otra vez y conviene reconocerlas completas. I want ... significa yo quiero ... (I want an apple). Here! o Here you are significa aquí tiene o ¡toma! Thank you significa gracias. Please significa por favor. Excuse me, Sorry y Well done también son frecuentes.",
        "Una frase de uso frecuente se lee como un solo bloque. No necesitas separar I, want y an apple: lees «I want an apple» y entiendes que alguien pide una manzana. En un diálogo, A dice «I want an apple, please» y B responde «Here!» al entregársela.",
        "Si una frase tiene una palabra que no conoces, apóyate en lo que sí conoces. En «I want a banana, please», aunque no supieras banana, entiendes I want ... please y que alguien pide algo. Eso es leer con estrategia.",
    ],
    vocab=[("I want ...", "yo quiero ..."), ("Here!", "¡Aquí! / ¡Toma!"), ("Here you are.", "Aquí tiene."), ("please", "por favor"), ("Well done!", "¡Bien hecho!"), ("Sorry.", "Perdón.")],
    worked=[
        {"title": "Leer un chunk", "problem": "Lee: «I want an apple, please.» ¿Qué pide la persona?", "steps": ["I want significa yo quiero.", "Apple es manzana."], "answer": "Una manzana"},
        {"title": "Entregar algo", "problem": "Lee: «A: I want a pencil, please. B: Here!» ¿Qué hace B?", "steps": ["A pide un lápiz.", "B dice Here! y se lo da."], "answer": "Le da el lápiz"},
    ],
    mistakes=[
        {"wrong": "Leer palabra por palabra I - want - an - apple sin entender la frase.", "why": "Se separa un bloque que va junto.", "fix": "Lee I want ... como un solo bloque que significa yo quiero ..."},
        {"wrong": "Decir I want cuando se entrega algo.", "why": "Se confunde pedir con entregar.", "fix": "I want sirve para pedir; Here! sirve para entregar."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «I want milk.» ¿Qué quiere la persona?", "Leche", "Milk es leche."),
            ex("¿Qué significa «I want»?", "Yo quiero", "I want se usa para pedir."),
            ex("¿Qué significa «Here you are»?", "Aquí tiene", "Se dice al entregar algo."),
        ],
        "understand": [
            ex("¿Cuándo se dice «Here!»", "Cuando entregas algo a alguien", "Here! es aquí o toma."),
            ex("¿Qué es una expresión de uso frecuente?", "Una frase que se repite mucho y se lee completa", "Por ejemplo I want ... o Thank you."),
            ex("¿Qué significa «please»?", "por favor", "Please hace el pedido más amable."),
        ],
        "apply": [
            ex("Lee: «A: I want a banana, please. B: Here you are. A: Thank you.» ¿Qué pide A?", "Una banana (plátano)", "A pide a banana con please."),
            ex("Lee: «I want two eggs, please.» ¿Cuántos huevos pide?", "2", "Two es dos."),
            ex("Lee: «Here! A red pencil.» ¿Qué entrega la persona?", "Un lápiz rojo", "Here! acompaña a lo que entrega."),
        ],
        "reason": [
            ex("Lee: «A: Sorry! B: It's OK.» ¿Por qué dice A Sorry?", "Porque pide perdón", "Sorry es perdón."),
            ex("¿Por qué leer I want an apple como bloque ayuda a entender?", "Porque la frase completa se entiende más rápido", "Un chunk se reconoce sin separar."),
        ],
        "challenge": [
            ex("Ordena el diálogo: (1) B: Here you are. (2) A: I want a pencil, please. (3) A: Thank you.", "2, 1, 3", "Primero A pide, luego B entrega y después A agradece."),
            ex("Completa el diálogo: A: «I want milk, ___.» B: «Here you are.» (opciones: please o sorry)", "please", "Please acompaña a un pedido."),
        ],
    },
    context=[ex("En el kiosco del colegio ves este diálogo: «A: I want bread, please. B: Here!». ¿Qué compró A?", "Pan", "Bread es pan.")],
    selfcheck=[
        ex("¿Cómo se dice «yo quiero» en inglés?", "I want", "I want es yo quiero."),
        ex("Lee: «Thank you.» ¿Qué significa?", "Gracias", "Thank you es gracias."),
        ex("¿Qué dices al entregar un lápiz: Here! o Sorry?", "Here!", "Here! es toma."),
    ],
    open_task=task("Lee este diálogo con un adulto: «A: Excuse me, I want a banana, please. B: Here you are. A: Thank you! B: You're welcome.» Léanlo dos veces, cambiando de papeles. Después escribe tu propio diálogo de tres líneas para pedir leche, pan o una manzana usando I want, please y Here!", "A: I want milk, please. B: Here! A: Thank you.", ["lee el diálogo completo", "usa I want, please y Here!", "escribe tres líneas correctas"], ["diálogo escrito", "nota del adulto"], ["separar las palabras de I want", "olvidar please"], "Practican otra vez el diálogo cambiando de papel y cuidando el tono amable."),
    reinforce="Lee en voz alta «I want an apple, please» tres veces.",
    extend="Escribe un diálogo de cuatro líneas en una tienda de frutas.",
)

register(
    OA6, 5,
    materials="Los textos escritos en cada ejercicio; lápiz, papel y lápices de colores.",
    use="Aprenderé a mostrar que entiendo un texto leído con un dibujo, una acción o una respuesta. Sirve para demostrar comprensión sin traducir todo.",
    prior=["Reconozco tipos de texto.", "Identifico idea general, personajes y acciones.", "Leo chunks frecuentes."],
    explain=[
        "Después de leer, puedes mostrar que entendiste de varias maneras. Puedes dibujar (draw) lo que lees, hacer lo que dicen las instrucciones (do), contestar preguntas cortas (answer) o marcar la respuesta correcta (circle).",
        "Antes de responder, lee todo el texto. Luego busca palabras clave: personajes, objetos, números, colores y acciones. Si el texto es una instrucción, hazla paso a paso. Si es un cuento, dibuja el personaje y su acción. Si es informativo, busca el dato que pide la pregunta.",
        "Al final, revisa tu respuesta con el texto. Pregúntate: ¿mi dibujo o mi respuesta coincide con las palabras que leí? Si no coincide, vuelve a leer.",
    ],
    vocab=[("read", "leer"), ("circle", "encerrar en un círculo"), ("answer", "responder"), ("check", "comprobar"), ("draw", "dibujar"), ("do", "hacer")],
    worked=[
        {"title": "Mostrar con un dibujo", "problem": "Lee: «A girl has a green kite. The kite is in the sky.» ¿Qué dibujas?", "steps": ["Dibujo una niña.", "Dibujo una cometa verde en el cielo."], "answer": "Una niña con una cometa verde en el cielo"},
        {"title": "Hacer lo que dice una instrucción", "problem": "Lee: «1. Draw a square. 2. Color it yellow.» ¿Qué haces?", "steps": ["Dibujo un cuadrado.", "Lo pinto de amarillo."], "answer": "Un cuadrado amarillo"},
    ],
    mistakes=[
        {"wrong": "Responder sin leer el texto completo.", "why": "Se responde con la primera palabra que se entiende.", "fix": "Lee todo el texto y luego responde."},
        {"wrong": "No revisar la respuesta con el texto.", "why": "Se confía en la memoria.", "fix": "Vuelve al texto y comprueba cada palabra clave."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «I see a dog.» ¿Qué dibujas?", "Un perro", "Dog es perro."),
            ex("Lee: «Draw a circle.» ¿Qué haces?", "Dibujo un círculo", "Circle es círculo."),
            ex("¿Qué significa «answer»?", "responder o respuesta", "Answer es responder."),
        ],
        "understand": [
            ex("¿Cuáles son formas de mostrar que entendiste un texto?", "Dibujar, hacer lo que dice, contestar y marcar la respuesta", "Cada forma muestra comprensión."),
            ex("¿Qué haces antes de responder?", "Leo todo el texto", "Así no me quedo con una parte."),
            ex("¿Por qué revisas tu respuesta con el texto?", "Para comprobar que coincide con lo que dice", "Check es comprobar."),
        ],
        "apply": [
            ex("Lee: «Tom has two red pencils. Tom has one blue pen.» ¿Cuántos lápices tiene Tom?", "2", "Two red pencils."),
            ex("Lee: «The cat is under the table.» ¿Dónde dibujas el gato?", "Debajo de la mesa", "Under the table."),
            ex("Lee: «1. Stand up. 2. Clap two times. 3. Sit down.» ¿Qué haces en el paso 2?", "Aplaudo dos veces", "Clap two times es aplaude dos veces."),
        ],
        "reason": [
            ex("Lee: «Elephants are big. They drink water.» Un niño dice que beben leche. ¿Qué debe hacer?", "Volver al texto: beben agua", "Water es agua."),
            ex("Lee: «A bunny has three eggs.» Una niña dibuja cinco huevos. ¿Qué error tiene?", "La cantidad: el texto dice tres", "Three es tres."),
        ],
        "challenge": [
            ex("Lee: «Dear Mia, Happy Easter! I have five eggs for you. From Leo.» Responde: ¿quién escribe, a quién y cuántos huevos hay?", "Leo escribe a Mia; hay cinco huevos", "From Leo, Dear Mia, five eggs."),
            ex("Lee: «A zebra lives in Africa. It has black and white stripes.» Dibuja y escribe dos palabras clave.", "Cebra con rayas; zebra y stripes", "Son palabras clave del texto."),
        ],
    },
    context=[ex("En un papelito lees: «Draw a big sun. Color it yellow.» ¿Cómo queda tu dibujo?", "Un sol grande amarillo", "Big sun y yellow.")],
    selfcheck=[
        ex("¿Cómo se dice «leer» en inglés?", "read", "Read es leer."),
        ex("Lee: «The monkey is in the tree.» ¿Dónde está el mono?", "En el árbol", "In the tree."),
        ex("¿Qué haces si tu respuesta no coincide con el texto?", "Vuelvo a leer", "Se corrige con el texto."),
    ],
    open_task=task("Lee estos dos textos y responde con dibujos y palabras. Texto 1: «A girl has a red hat. A dog is next to the girl.» Dibuja la escena y rotula girl, hat, dog. Texto 2 (instrucciones): «1. Draw a triangle. 2. Color it blue. 3. Write your name under the triangle.» Hazlo.", "Dibujo de niña con sombrero rojo y perro; triángulo azul con tu nombre debajo.", ["dibuja la escena con los detalles", "rotula en inglés", "sigue los tres pasos de la instrucción"], ["dibujos", "nota del adulto"], ["no dibujar el color rojo del sombrero", "no escribir el nombre debajo del triángulo"], "Comparen cada dibujo con las palabras del texto y corrijan lo que falte."),
    reinforce="Lee «Draw a red circle» y dibújalo.",
    extend="Escribe dos textos cortos: unas instrucciones de dos pasos y una tarjeta de saludo.",
)

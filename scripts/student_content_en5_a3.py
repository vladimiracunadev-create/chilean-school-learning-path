"""Student material for 5.º básico Inglés (propuesta), EN05 OA 05 (lectura de textos literarios y no literarios) y OA 06 (funciones comunicativas en textos leídos).

Todos los textos de lectura son originales y están escritos en el propio enunciado. Cada palabra nueva lleva su pista en español.
Las tiras cómicas se describen con palabras (viñeta por viñeta) para que no haga falta ningún dibujo externo.
"""
from __future__ import annotations

from student_content_en5_a import lesson
from student_content_ma01_b import task
from student_lessons import arith

OA5 = "EN05 OA 05"
OA6 = "EN05 OA 06"

BACKPACK = "«Sofía is ten years old. She lives in a small town near the sea. On Monday morning, she cannot find her blue backpack. She looks in her room, in the kitchen and in the garden. At last, her little brother Martín shows her the backpack. It is under his bed! He uses it to carry his toy cars. Sofía laughs and gives him a hug. Then she goes to school.» (backpack = mochila, town = pueblo, at last = por fin, shows = muestra, toy cars = autitos de juguete, laughs = ríe, hug = abrazo)"
TURTLE = "«Tito is a small turtle. He walks very slowly, so the other animals leave him behind. Tito is sad because nobody waits for him. One day, a storm comes and the rabbits cannot find their house. Tito knows the path because he always walks slowly and looks carefully. He guides the rabbits home. Now the animals wait for Tito, and they say: Everyone is good at something.» (turtle = tortuga, slowly = despacio, leave behind = dejar atrás, nobody = nadie, waits = espera, storm = tormenta, rabbits = conejos, path = camino, carefully = con cuidado, guides = guía)"
COMIC = "Viñeta 1: Ana está en el parque y dice: «I am hungry!». Viñeta 2: su perro Rex llega con una bolsa en la boca y dice: «Woof! Look!». Viñeta 3: Ana mira la bolsa vacía y dice: «Rex! Where is my sandwich?». Rex, con la boca llena y feliz, dice: «Woof!» (hungry = con hambre, empty = vacía, sandwich = sándwich)"
LEAVES = "«Leaves are falling, one by one, red and gold in the autumn sun. They dance and spin in the cool wind's song, and cover the grass all day long.» (leaves = hojas, falling = cayendo, one by one = una por una, autumn = otoño, spin = girar, cover = cubrir, grass = pasto, all day long = todo el día)"
EMAIL = "«From: Mr. Pérez. To: Class 5A. Subject: Science Fair. Date: 12 November. Hello students, the science fair is on Friday, 22 November, at 10:00 in the school gym. Please bring your project on Thursday, 21 November. Each project needs a title and a poster. Good luck! Mr. Pérez» (science fair = feria científica, gym = gimnasio, bring = traigan, project = proyecto, poster = afiche, good luck = buena suerte)"
BOOKMARK = "«How to make a bookmark. You need: a strip of colored paper, pencils. 1. Take the strip of paper. 2. Write your name at the top. 3. Draw a flower in the middle. 4. Color the flower. Now you have a bookmark for your book!» (bookmark = marcapáginas, strip = tira, at the top = arriba, in the middle = en el medio)"
PENGUIN = "«Penguins are birds, but they cannot fly. They use their wings to swim fast in the sea. They eat fish and small sea animals. Many penguins live near the cold seas of the south. Some penguins keep their egg warm on their feet. Penguins stay together in big groups.» (penguins = pingüinos, wings = alas, small sea animals = animales marinos pequeños, egg = huevo, feet = pies, groups = grupos)"
NEWS = "«School Plants Fifty Trees. On Saturday, 5 October, one hundred and twenty students and parents planted fifty trees in the yard of Río Verde School. The children brought small shovels and water. The principal said: We want a greener school. The trees will give shade in summer.» (plants/planted = planta/plantaron, parents = apoderados, yard = patio, shovels = palas, principal = director, greener = más verde, shade = sombra)"

# ================================================================ OA 05
lesson(
    OA5, 1,
    "El cuento escrito en cada ejercicio y lápiz.",
    "Aprenderé a leer un cuento y a identificar personajes, lugar, momento y las tres partes de la trama: comienzo, desarrollo y final. Sirve para comprender cuentos en inglés.",
    ["Sé que un cuento tiene personajes, un lugar y un problema.", "Conozco palabras como room, kitchen, garden y school."],
    [
        "Un cuento (story) es un texto literario que cuenta una historia. Tiene personajes (characters), que son quienes actúan. Tiene un entorno (setting), que dice dónde y cuándo ocurre. Y tiene una trama (plot), que es lo que pasa. Para leerlo, subraya los nombres propios, los lugares y los momentos.",
        "La trama tiene tres partes. En el comienzo (beginning) aparece el problema: Sofía no encuentra su mochila. En el desarrollo (middle) los personajes hacen algo para resolverlo: ella busca en varios lugares. En el final (end) el problema se resuelve: su hermano le muestra la mochila. Las palabras On Monday morning y At last te dan pistas de tiempo.",
        "Para encontrar los lugares, fíjate en las palabras in (en), near (cerca de), under (debajo de) y at (en). Para saber qué hace un personaje, busca los verbos: looks (mira), shows (muestra), laughs (ríe), goes (va). Leer con estas preguntas te ayuda a comprender: ¿quién?, ¿dónde?, ¿cuándo? y ¿qué pasa primero, después y al final?",
    ],
    [("character", "personaje"), ("setting", "entorno: lugar y momento"), ("plot", "trama: lo que pasa"), ("beginning / middle / end", "comienzo / desarrollo / final"), ("at last", "por fin"), ("under", "debajo de")],
    [
        ("Personajes y entorno", "Lee: " + BACKPACK + " ¿Quiénes son los personajes y dónde vive Sofía?", ["Busco los nombres: Sofía y Martín.", "Busco el lugar: a small town near the sea.", "Sofía vive en un pueblo pequeño cerca del mar."], "Sofía y Martín; en un pueblo pequeño cerca del mar"),
        ("Partes de la trama", "En el mismo cuento, ¿cuál es el problema del comienzo y cómo se resuelve?", ["Comienzo: she cannot find her blue backpack.", "Final: Martín shows her the backpack.", "El problema se resuelve cuando su hermano le muestra la mochila."], "No encuentra su mochila; su hermano se la muestra"),
    ],
    [
        ("Pensar que el final es cuando Sofía va a la escuela.", "Se confunde el final de la trama con la última acción.", "El problema se resuelve cuando Martín muestra la mochila; ir a la escuela es solo lo último que ocurre."),
        ("Decir que el entorno es solo el lugar.", "No se considera el momento.", "El entorno es lugar y momento: a small town y On Monday morning."),
    ],
    [
        ("Lee: " + BACKPACK + " ¿Cuántos años tiene Sofía?", "10", "El texto dice Sofía is ten years old."),
        ("Lee: " + BACKPACK + " ¿Dónde estaba la mochila? a) debajo de la cama de Martín b) en el jardín", "a)", "Dice it is under his bed."),
        ("Lee: " + BACKPACK + " ¿Para qué usa Martín la mochila? a) para llevar autitos de juguete b) para ir al colegio", "a)", "Dice he uses it to carry his toy cars."),
    ],
    [
        ("Lee: " + BACKPACK + " ¿En cuántos lugares busca Sofía antes de que Martín le muestre la mochila?", "3", "Busca en su pieza, en la cocina y en el jardín."),
        ("Lee: " + BACKPACK + " ¿Cuándo ocurre la historia? a) un lunes en la mañana b) un sábado en la noche", "a)", "Dice On Monday morning."),
        ("Lee: " + BACKPACK + " ¿Cómo reacciona Sofía al final? a) se ríe y abraza a su hermano b) se enoja", "a)", "Dice Sofía laughs and gives him a hug."),
    ],
    [
        ("Lee: " + """«Julia lives in a village near the mountains. On Tuesday afternoon, her bike has a flat tire. She walks to the shop of Mr. Lara. He fixes it. Julia says thank you and rides home.» (village = aldea, flat tire = neumático pinchado, shop = taller, fixes = arregla, rides = anda en bicicleta)""" + " ¿Cuál es el problema del comienzo?", "La bicicleta tiene un neumático pinchado", "Dice her bike has a flat tire."),
        ("Lee: " + """«Julia lives in a village near the mountains. On Tuesday afternoon, her bike has a flat tire. She walks to the shop of Mr. Lara. He fixes it. Julia says thank you and rides home.» (village = aldea, flat tire = neumático pinchado, shop = taller, fixes = arregla, rides = anda en bicicleta)""" + " ¿Quién arregla la bicicleta?", "El señor Lara", "Dice He fixes it, hablando de Mr. Lara."),
        ("Lee: " + """«Julia lives in a village near the mountains. On Tuesday afternoon, her bike has a flat tire. She walks to the shop of Mr. Lara. He fixes it. Julia says thank you and rides home.» (village = aldea, flat tire = neumático pinchado, shop = taller, fixes = arregla, rides = anda en bicicleta)""" + " ¿Cuándo ocurre la historia? a) un martes en la tarde b) un domingo en la mañana", "a)", "Dice On Tuesday afternoon."),
    ],
    [
        ("Lee: " + BACKPACK + " Ordena: A) Sofía va a la escuela. B) Sofía busca en tres lugares. C) Sofía no encuentra su mochila. D) Martín muestra la mochila.", "C, B, D, A", "El texto sigue ese orden."),
        ("Lee: " + BACKPACK + " Un compañero dice que el cuento es sobre una niña que pierde un libro. ¿Qué objeto es en realidad?", "Una mochila", "El texto habla de her blue backpack."),
    ],
    [
        ("Lee: «Pedro lives in a big city. On Saturday, his kite flies into a tree. He asks a neighbor for a ladder. The neighbor helps him get the kite.» (neighbor = vecino, ladder = escalera, flies into = vuela hacia). ¿Cuál es el problema del comienzo?", "El volantín queda en un árbol", "Dice his kite flies into a tree."),
        ("En el texto de Pedro, ¿quién ayuda a resolver el problema?", "Un vecino", "Dice the neighbor helps him."),
    ],
    [("Lee: «At school, Ana loses her pencil case. She looks in her bag and finds it under her book.» (pencil case = estuche, finds = encuentra). ¿Dónde estaba el estuche? a) debajo del libro b) en el patio", "a)", "Dice under her book.")],
    [
        ("¿Qué es el entorno (setting) de un cuento?", "El lugar y el momento", "Responde a dónde y cuándo."),
        ("¿Cómo se llaman las tres partes de la trama?", "Comienzo, desarrollo y final", "Son beginning, middle y end."),
        ("¿Qué significa «at last»?", "Por fin", "Indica que algo ocurre después de un tiempo."),
    ],
    task("Lee este cuento: «Dani lives near a river. On Sunday, he wants to cross the river to see his friend. The bridge is closed, so he asks his dad for help. His dad drives him to the next bridge. Dani sees his friend and smiles.» (cross = cruzar, bridge = puente, closed = cerrado, drives = lleva en auto). Escribe los personajes, el entorno (lugar y momento) y una frase en español para el comienzo, el desarrollo y el final.", "Personajes: Dani, su papá y su amigo. Entorno: cerca de un río, un domingo. Comienzo: el puente está cerrado. Desarrollo: pide ayuda. Final: llega y sonríe.", ["nombra personajes", "dice lugar y momento", "tres frases de la trama"], ["hoja con respuestas", "nota del adulto"], ["olvidar el momento", "contar el final antes del comienzo"], "Reconoce los elementos bien identificados y relee con él el texto buscando cada pregunta: ¿quién?, ¿dónde?, ¿cuándo?"),
    "Relee el cuento de Sofía y subraya con lápiz los nombres de los personajes y los lugares.",
    "Escribe un cuento de cuatro frases en español sobre alguien que pierde algo, con comienzo, desarrollo y final.",
)

lesson(
    OA5, 2,
    "El cuento escrito en cada ejercicio y lápiz.",
    "Aprenderé a encontrar el tema de un cuento y las relaciones de causa y efecto entre los hechos. Sirve para comprender por qué pasan las cosas y qué mensaje deja la historia.",
    ["Sé identificar personajes y las tres partes de la trama.", "Conozco because (porque) y so (por eso)."],
    [
        "El tema (theme) es la idea general del cuento, el mensaje que deja. No es un dato del cuento: es una enseñanza, como «todos somos buenos en algo». Para encontrarlo, pregúntate: ¿qué aprende el personaje? y ¿qué quiere decirnos el cuento? El tema se escribe en una frase corta.",
        "La causa (cause) es la razón por la que algo pasa. El efecto (effect) es lo que pasa como resultado. En inglés se unen con because (porque) y so (por eso). «Tito walks slowly, so the animals leave him behind» significa que caminar despacio es la causa y que lo dejan atrás es el efecto. «Tito is sad because nobody waits for him»: la causa va después de because.",
        "La secuencia (sequence) es el orden en que pasan las cosas. Las palabras one day (un día), then (luego), now (ahora) y at last (por fin) te ayudan. Si ordenas los hechos y buscas causas y efectos, encontrarás el tema. Cuando dudes, relee la parte del cuento donde el personaje cambia.",
    ],
    [("theme", "tema: idea general o mensaje"), ("cause / effect", "causa / efecto"), ("because", "porque"), ("so", "por eso"), ("sequence", "secuencia: orden de los hechos"), ("everyone", "todos")],
    [
        ("Causa y efecto con because", "Lee: " + TURTLE + " ¿Por qué Tito está triste?", ["Busco because.", "Dice: because nobody waits for him.", "La causa es que nadie lo espera."], "Porque nadie lo espera"),
        ("Causa y efecto con so", "En el mismo cuento, ¿qué pasa porque Tito camina despacio?", ["Busco so.", "Dice: he walks very slowly, so the other animals leave him behind.", "El efecto es que los demás lo dejan atrás."], "Los demás animales lo dejan atrás"),
    ],
    [
        ("Decir que el tema es «Tito es una tortuga».", "Se escribe un dato y no una enseñanza.", "El tema es el mensaje: todos somos buenos en algo."),
        ("Poner el efecto después de because.", "Se confunde cuál parte explica la razón.", "Después de because va la causa; antes de so va la causa y después va el efecto."),
    ],
    [
        ("Lee: " + TURTLE + " ¿Cómo camina Tito? a) muy despacio b) muy rápido", "a)", "Dice he walks very slowly."),
        ("Lee: " + TURTLE + " ¿Qué ocurre un día? a) viene una tormenta b) Tito gana una carrera", "a)", "Dice a storm comes."),
        ("Lee: " + TURTLE + " ¿Qué hace Tito por los conejos? a) los guía a su casa b) los deja atrás", "a)", "Dice he guides the rabbits home."),
    ],
    [
        ("Lee: " + TURTLE + " ¿Por qué Tito conoce el camino? a) porque camina despacio y mira con cuidado b) porque tiene un mapa", "a)", "Dice because he always walks slowly and looks carefully."),
        ("Lee: " + TURTLE + " Ordena: A) Los animales esperan a Tito. B) Una tormenta pierde a los conejos. C) Los animales dejan atrás a Tito. D) Tito guía a los conejos.", "C, B, D, A", "El cuento sigue ese orden."),
        ("Lee: " + TURTLE + " ¿Cuál es el tema? a) Todos somos buenos en algo. b) Hay que correr rápido.", "a)", "El final dice Everyone is good at something."),
    ],
    [
        ("Lee: «Teo is afraid of dogs, so he crosses the street.» (afraid of = le teme a, crosses = cruza). ¿Qué hace Teo por tener miedo?", "Cruza la calle", "El efecto está después de so."),
        ("Lee: «The cake is burnt because Mom forgets it in the oven.» (burnt = quemada, forgets = olvida, oven = horno). ¿Por qué la torta está quemada?", "Porque mamá la olvida en el horno", "La causa viene después de because."),
        ("Elige la oración correcta: a) It is hot, so I drink water. b) I drink water, so it is hot.", "a)", "El calor es la causa y beber agua el efecto."),
    ],
    [
        ("Lee: «Ema forgets her umbrella, so she gets wet.» (forgets = olvida, gets wet = se moja). ¿Cuál es la causa?", "Olvida su paraguas", "La causa está antes de so."),
        ("En la misma oración, ¿cuál es el efecto?", "Se moja", "El efecto está después de so."),
    ],
    [
        ("Une las ideas con because: «Leo is happy» y «he wins the game» (wins = gana). ¿Qué oración queda bien? a) Leo is happy because he wins the game. b) Leo wins the game because he is happy.", "a)", "Ganar es la causa de estar contento."),
        ("Lee: «It is very cold, so Mia wears a coat.» (wears = lleva puesto). ¿Qué pasa por el frío?", "Mia lleva un abrigo", "El efecto es que usa abrigo."),
    ],
    [("Lee: «Jaime studies every day, so he gets a good grade.» (studies = estudia, grade = nota). ¿Qué enseñanza deja la oración? a) Estudiar ayuda a obtener buenos resultados b) La nota no importa", "a)", "La causa es estudiar y el efecto es la buena nota.")],
    [
        ("¿Qué significa «so»?", "Por eso", "So une la causa con el efecto."),
        ("¿Qué es el tema de un cuento?", "El mensaje o idea general", "El tema deja una enseñanza."),
        ("¿Qué va después de because: la causa o el efecto?", "La causa", "Because significa porque."),
    ],
    task("Lee este cuento: «Lola never shares her toys, so her friends do not want to play with her. Lola feels alone. One day, she gives a ball to a new girl. Now many children want to play with Lola.» (shares = comparte, toys = juguetes, alone = sola, gives = da, new = nueva). Escribe una causa y su efecto con so, una causa con because y el tema del cuento en una frase.", "Lola never shares, so her friends do not play with her. Lola feels alone because nobody plays with her. Tema: compartir hace amigos.", ["causa y efecto con so", "causa con because", "tema como enseñanza"], ["hoja con respuestas", "nota del adulto"], ["decir un dato como tema", "poner el efecto como causa"], "Reconoce las causas y efectos bien armados y relee con él para probar con so y because."),
    "Relee el cuento de Tito y marca con lápiz las dos oraciones que usan because o so.",
    "Escribe en español el tema de un cuento que conozcas y una causa y un efecto de ese cuento.",
)

lesson(
    OA5, 3,
    "La tira cómica descrita y el poema escrito en cada ejercicio, y lápiz.",
    "Aprenderé a leer una tira cómica y un poema y a identificar quién habla, qué pasa y cuál es la idea general. Sirve para comprender textos literarios breves.",
    ["Sé que una tira cómica tiene viñetas con globos de diálogo.", "Sé que un poema tiene líneas y rimas."],
    [
        "Una tira cómica (comic strip) cuenta una historia con viñetas (panels), que son cuadros con dibujos y textos. Los globos de diálogo (speech bubbles) muestran lo que dicen los personajes. Para leerla, sigue las viñetas de izquierda a derecha y mira a quién pertenece cada globo.",
        "Lo cómico suele venir de una sorpresa: lo que pasa en la última viñeta no es lo que esperabas. En la tira de Ana y Rex, el perro llega con una bolsa vacía y Ana pregunta por su sándwich. La sorpresa es que Rex se lo comió. Los dibujos y las palabras trabajan juntos para dar el mensaje.",
        "Un poema (poem) tiene versos (lines), estrofas (verses) y a veces rimas. Para leerlo, busca de qué habla (la idea general), qué imágenes usa (colores, sonidos) y qué siente quien habla. En el poema de las hojas, las palabras red, gold, sun y dance muestran la belleza del otoño. Tu tema es una frase corta sobre la idea del poema.",
    ],
    [("comic strip", "tira cómica"), ("panel", "viñeta"), ("speech bubble", "globo de diálogo"), ("poem / line / verse", "poema / verso / estrofa"), ("autumn", "otoño"), ("leaves", "hojas")],
    [
        ("Quién habla en la tira", "Lee: " + COMIC + " ¿Qué dice Ana al final y qué dice Rex?", ["Busco el globo de Ana en la viñeta 3: Rex! Where is my sandwich?", "Busco el globo de Rex: Woof!", "Ana pregunta por el sándwich y Rex ladra."], "Ana: Rex! Where is my sandwich? Rex: Woof!"),
        ("Qué sorpresa hay", "En la misma tira, ¿qué pasó con el sándwich?", ["Rex llega con una bolsa vacía.", "Rex tiene la boca llena y feliz.", "Rex se comió el sándwich."], "Rex se lo comió"),
    ],
    [
        ("Leer los globos sin ver a quién pertenecen.", "Se mezclan las voces de los personajes.", "Mira al personaje al que apunta cada globo."),
        ("Pensar que el poema habla de una fiesta porque aparece gold.", "Se toma una palabra aislada.", "Une las imágenes: leaves, autumn, wind y grass muestran el otoño."),
    ],
    [
        ("Lee: " + COMIC + " ¿Quién tiene hambre al comienzo? a) Ana b) Rex", "a) Ana", "En la viñeta 1 Ana dice I am hungry."),
        ("Lee: " + COMIC + " ¿Dónde está Ana? a) en el parque b) en el colegio", "a) en el parque", "La viñeta 1 dice que Ana está en el parque."),
        ("Lee: " + LEAVES + " ¿En qué estación del año ocurre el poema? a) otoño b) verano", "a) otoño", "Dice autumn sun."),
    ],
    [
        ("Lee: " + LEAVES + " ¿Qué palabra rima con sun? a) one b) wind", "a) one", "Sun y one riman: terminan en el mismo sonido."),
        ("Lee: " + LEAVES + " ¿Qué hacen las hojas al ser empujadas por el viento? a) bailan y giran b) se quedan quietas", "a)", "Dice they dance and spin."),
        ("Lee: " + COMIC + " ¿Cuántas viñetas tiene la tira?", "3", "El texto describe la viñeta 1, 2 y 3."),
    ],
    [
        ("Lee: «Viñeta 1: una niña dice: I want to be a chef! Viñeta 2: mezcla ingredientes en un bol y dice: Chocolate, chocolate and more chocolate! Viñeta 3: la torta es toda café y ella dice: Oh no! It is only chocolate!» (chef = cocinera, mix = mezclar, only = solo). ¿Qué quiere ser la niña?", "Cocinera (chef)", "En la viñeta 1 dice I want to be a chef."),
        ("En la tira de la niña chef, ¿qué ingrediente usa en la viñeta 2?", "Chocolate", "Dice Chocolate, chocolate and more chocolate."),
        ("En la tira de la niña chef, ¿cuál es la sorpresa de la última viñeta?", "La torta es solo de chocolate", "Ella dice It is only chocolate."),
    ],
    [
        ("Lee: " + LEAVES + " ¿Cuál es la idea general del poema? a) La belleza de las hojas de otoño b) La lluvia en el mar", "a)", "Todo el poema habla de hojas que caen."),
        ("Lee: " + COMIC + " ¿Cómo sabemos que Rex está contento? a) tiene la boca llena y feliz b) corre por el parque", "a)", "El texto dice que Rex está feliz."),
    ],
    [
        ("Lee el poema: " + LEAVES + " ¿Qué palabra rima con song?", "long", "Song y long terminan con el mismo sonido."),
        ("Una tira cómica tiene dos viñetas: en la 1 una niña dice «Look at my new hat!» (new = nuevo) y en la 2 el viento se lleva el sombrero. ¿Qué es lo gracioso o sorprendente? a) que el sombrero nuevo se vuela b) que la niña compra otro sombrero", "a)", "La viñeta 2 cambia lo esperado: el sombrero vuela."),
    ],
    [("Lee: «Viñeta 1: Tomás dice: I am tired. Viñeta 2: Tomás se sienta en un sillón y dice: Good night! Viñeta 3: su gato está durmiendo en su cabeza.» (tired = cansado, sits = se sienta). ¿Dónde duerme el gato?", "En la cabeza de Tomás", "La viñeta 3 lo muestra.")],
    [
        ("¿Qué es una viñeta?", "Un cuadro de una tira cómica", "Panel es viñeta."),
        ("¿Qué muestra un globo de diálogo?", "Lo que dice un personaje", "Speech bubble es globo de diálogo."),
        ("¿Qué significa «autumn»?", "Otoño", "Es la estación entre el verano y el invierno."),
    ],
    task("Lee este poema original: «The moon is round, the sky is deep. The stars are watching, the world is asleep. I close my eyes and count to three, and dream of a boat on a sleepy sea.» (round = redonda, deep = profundo, asleep = dormido, dream = soñar, boat = bote, sleepy = soñoliento). Escribe de qué habla (una frase en español) y dos pares de palabras que riman. Después dibuja una tira cómica de dos viñetas: en la primera alguien dice Good night! y en la segunda duerme.", "Habla de la noche y de dormir. Riman deep-asleep y three-sea. Tira cómica con Good night! y alguien durmiendo.", ["idea general correcta", "dos pares que riman", "tira cómica de dos viñetas"], ["hoja con respuestas y dibujo", "nota del adulto"], ["decir que riman moon y sky", "no escribir Good night!"], "Reconoce los pares que riman y relee con él el poema diciendo en voz alta las palabras finales."),
    "Relee la tira de Ana y Rex y señala con el dedo qué globo es de cada personaje.",
    "Dibuja una tira cómica de tres viñetas con una sorpresa al final y escribe un globo en inglés en cada viñeta.",
)

lesson(
    OA5, 4,
    "El correo y las instrucciones escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer un correo electrónico y unas instrucciones y a encontrar datos específicos como fechas, lugares y pasos. Sirve para comprender textos que se usan en la vida diaria.",
    ["Sé leer fechas como 12 November y horas como 10:00.", "Conozco first, next, then y finally."],
    [
        "Un correo electrónico (email) tiene partes: From (de), To (para), Subject (asunto), Date (fecha) y el mensaje. Leer esas partes primero te dice quién escribe, a quién y de qué trata. Dentro del mensaje busca datos específicos: días, horas, lugares y lo que se debe traer o hacer.",
        "Unas instrucciones o procedimiento (procedure) explican cómo hacer algo. Tienen un título, una lista de materiales (you need) y pasos numerados. Cada paso empieza con un verbo en orden: take (toma), write (escribe), draw (dibuja), color (colorea). El orden de los pasos importa.",
        "Para leer fechas en inglés: Friday, 22 November se lee «el viernes 22 de noviembre». Las horas como 10:00 se leen «ten o'clock». Las palabras bring (traer) y please (por favor) aparecen en los pedidos. Subraya los datos que respondan a who, when, where y what to bring. Un diálogo escrito se lee por turnos: el nombre antes de los dos puntos dice quién habla.",
    ],
    [("email", "correo electrónico"), ("From / To / Subject", "de / para / asunto"), ("procedure", "procedimiento: pasos para hacer algo"), ("step", "paso"), ("bring", "traer"), ("poster", "afiche")],
    [
        ("Datos del correo", "Lee: " + EMAIL + " ¿Quién escribe el correo y a quién?", ["Miro From y To.", "From: Mr. Pérez. To: Class 5A.", "El señor Pérez escribe a la clase 5A."], "El señor Pérez escribe a la clase 5A"),
        ("Fecha y lugar", "En el mismo correo, ¿cuándo y dónde es la feria científica?", ["Busco Friday, 22 November.", "Busco at 10:00 in the school gym.", "Es el viernes 22 de noviembre a las 10:00 en el gimnasio."], "El viernes 22 de noviembre a las 10:00, en el gimnasio"),
    ],
    [
        ("Confundir la fecha del correo con la fecha del evento.", "Date indica cuándo se escribió el correo.", "El evento es Friday, 22 November; el correo es del 12 de noviembre."),
        ("Cambiar el orden de los pasos de un procedimiento.", "No se respeta la numeración.", "Sigue 1, 2, 3 y 4 en ese orden."),
    ],
    [
        ("Lee: " + EMAIL + " ¿Cuál es el asunto (Subject) del correo?", "Science Fair", "Subject es el asunto."),
        ("Lee: " + EMAIL + " ¿Qué día deben traer el proyecto? a) jueves 21 de noviembre b) viernes 22 de noviembre", "a)", "Dice bring your project on Thursday, 21 November."),
        ("Lee: " + EMAIL + " ¿Qué necesita cada proyecto? a) un título y un afiche b) una canción", "a)", "Dice Each project needs a title and a poster."),
    ],
    [
        ("Lee: " + BOOKMARK + " ¿Cuántos pasos numerados tiene?", "4", "Están numerados del 1 al 4."),
        ("Lee: " + BOOKMARK + " ¿Qué dibujas en el paso 3? a) una flor b) un perro", "a) una flor", "Dice draw a flower in the middle."),
        ("Lee: " + BOOKMARK + " ¿Qué materiales necesitas? a) una tira de papel de color y lápices b) pegamento y tijeras", "a)", "Dice you need a strip of colored paper and pencils."),
    ],
    [
        ("Lee: «From: Nico. To: Grandma. Subject: My Trip. Date: 2 March. Hi Grandma, I am going to the beach on Sunday. I want to bring my kite. Can you help me find it? Love, Nico» (kite = volantín, find = encontrar). ¿Para quién es el correo?", "Para Ben", "En To dice Ben."),
        ("En el correo de Nico, ¿qué quiere llevar a la playa?", "Su volantín", "Dice I want to bring my kite."),
        ("Lee este diálogo: «Pam: Where is the library? Jon: It is next to the park, behind the school. Pam: Thanks!» (next to = al lado de, behind = detrás de). ¿Dónde está la biblioteca?", "Al lado del parque, detrás del colegio", "Jon dice next to the park, behind the school."),
    ],
    [
        ("Lee: " + EMAIL + " Si la feria es el viernes 22 y el proyecto se trae un día antes, ¿qué día se trae?", "El jueves 21", "Un día antes del viernes 22 es el jueves 21."),
        ("Lee: " + BOOKMARK + " Ordena: A) Colorear la flor. B) Tomar la tira. C) Dibujar la flor. D) Escribir tu nombre.", "B, D, C, A", "Son los pasos 1 al 4 en ese orden."),
    ],
    [
        ("Lee: «From: Lía. To: Teo. Subject: Birthday. Date: 3 May. Hi Teo, my birthday party is on Saturday at 4:00 at my house. Please bring a swimsuit.» (swimsuit = traje de baño). ¿Qué debe traer Teo?", "Un traje de baño", "Dice please bring a swimsuit."),
        ("En el correo de Lía, ¿a qué hora es la fiesta?", "A las 4:00", "Dice on Saturday at 4:00."),
    ],
    [("Lee: «From: Mr. Pérez. To: Class 5A. Date: 12 November.» ¿Cuántos días hay entre el 12 de noviembre y el 22 de noviembre?", "10", "22 − 12 = 10.")],
    [
        ("¿Qué significa «Subject» en un correo?", "Asunto", "Subject dice de qué trata el correo."),
        ("¿Qué significa «bring»?", "Traer", "Bring es llevar algo con uno."),
        ("¿Para qué sirve numerar los pasos de un procedimiento?", "Para saber el orden", "El orden de los pasos importa."),
    ],
    task("Lee este correo: «From: Mrs. Rojas. To: Class 5B. Subject: Library Visit. Date: 8 April. Hello students, we visit the library on Wednesday, 10 April, at 11:00. Please bring a notebook and a pencil. Do not bring food.» (visit = visitamos, notebook = cuaderno, food = comida). Escribe quién escribe, a quién, cuándo es la visita y qué deben traer y qué no.", "Mrs. Rojas escribe a la clase 5B; la visita es el miércoles 10 de abril a las 11:00; traen un cuaderno y un lápiz; no traen comida.", ["quién y a quién", "día y hora", "qué traer y qué no"], ["hoja con respuestas", "nota del adulto"], ["confundir las dos fechas", "olvidar do not bring food"], "Reconoce los datos bien encontrados y relee con él subrayando From, To y la fecha del evento."),
    "Relee el correo del señor Pérez y subraya con un color la fecha de la feria y con otro la hora.",
    "Escribe un procedimiento de cuatro pasos en español para hacer un avión de papel, con título y materiales.",
)

lesson(
    OA5, 5,
    "El artículo y la noticia escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer un artículo informativo y una noticia y a encontrar la idea general, datos específicos y palabras clave. Sirve para comprender textos que informan.",
    ["Sé identificar quién, qué, dónde y cuándo.", "Conozco palabras como sea, fish, tree y school."],
    [
        "Un artículo informativo (informative article) da información verdadera sobre un tema, como los pingüinos. Tiene una idea general (main idea) y datos (facts) que la apoyan. Una noticia (news report) cuenta algo que ocurrió: dice qué pasó, quién, dónde, cuándo y por qué. Los dos son textos no literarios.",
        "Para leer un artículo, primero lee el título. Después busca la idea general: ¿de qué trata todo el texto? Luego anota los datos específicos: números, nombres y lugares. Las palabras clave (key words) son sustantivos y verbos que repiten el tema; en el artículo de los pingüinos son penguins, swim, fish y wings.",
        "En una noticia, el titular (headline) resume el hecho: «School Plants Fifty Trees». El primer párrafo responde las preguntas who, what, when y where. Fíjate en las fechas, como Saturday, 5 October, y en los números, como fifty y one hundred and twenty. Así sabes exactamente lo que ocurrió.",
    ],
    [("article", "artículo"), ("news report", "noticia"), ("headline", "titular"), ("main idea", "idea general"), ("fact", "dato"), ("wings", "alas")],
    [
        ("Idea general", "Lee: " + PENGUIN + " ¿Cuál es la idea general?", ["Todo el texto habla de penguins.", "Dice qué son, cómo nadan y qué comen.", "La idea general es cómo son los pingüinos."], "Cómo son los pingüinos"),
        ("Datos de una noticia", "Lee: " + NEWS + " ¿Cuántos árboles plantaron y cuándo?", ["Busco los números: fifty trees.", "Busco la fecha: Saturday, 5 October.", "Plantaron 50 árboles el sábado 5 de octubre."], "50 árboles el sábado 5 de octubre"),
    ],
    [
        ("Confundir un dato con la idea general.", "Un número como fifty es un dato, no la idea.", "La idea general es la que resume todo el texto."),
        ("Pensar que los pingüinos vuelan porque tienen alas.", "No se lee but they cannot fly.", "El texto dice que no vuelan: usan las alas para nadar."),
    ],
    [
        ("Lee: " + PENGUIN + " ¿Para qué usan las alas los pingüinos? a) para nadar rápido b) para volar", "a)", "Dice they use their wings to swim fast."),
        ("Lee: " + PENGUIN + " ¿Qué comen los pingüinos según el texto? a) pescado b) pasto", "a) pescado", "Dice they eat fish."),
        ("Lee: " + NEWS + " ¿Dónde plantaron los árboles? a) en el patio de la escuela Río Verde b) en un parque", "a)", "Dice in the yard of Río Verde School."),
    ],
    [
        ("Lee: " + NEWS + " ¿Cuántas personas ayudaron a plantar?", "120", "Dice one hundred and twenty students and parents."),
        ("Lee: " + NEWS + " ¿Qué dijo el director? a) quiere una escuela más verde b) quiere cerrar la escuela", "a)", "Dice We want a greener school."),
        ("Lee: " + PENGUIN + " ¿Dónde viven muchos pingüinos? a) cerca de los mares fríos del sur b) en el desierto", "a)", "Dice near the cold seas of the south."),
    ],
    [
        ("Lee: «Bees are small insects. They make honey from the nectar of flowers. A bee colony can have thousands of bees. The queen bee lays eggs.» (nectar = néctar, colony = colonia, thousands = miles, queen = reina, lays = pone). ¿Cuál es la idea general?", "Cómo viven las abejas", "Todo el texto habla de abejas y de lo que hacen."),
        ("En el texto de las abejas, ¿de dónde sacan el néctar para hacer miel?", "De las flores", "Dice from the nectar of flowers."),
        ("En el texto de las abejas, ¿quién pone los huevos?", "La reina", "Dice The queen bee lays eggs."),
    ],
    [
        ("Lee: " + NEWS + " ¿Qué función tendrán los árboles en verano? a) darán sombra b) darán frutas", "a)", "Dice will give shade in summer."),
        ("Lee: " + PENGUIN + " ¿Dónde mantienen algunos pingüinos su huevo tibio? a) sobre sus pies b) en el agua", "a)", "Dice on their feet."),
    ],
    [
        ("Lee: " + NEWS + " Si 10 de los 50 árboles se plantaron junto al portón, ¿cuántos se plantaron en otros lugares del patio?", "40", "50 − 10 = 40."),
        ("Elige el mejor titular para el artículo de los pingüinos: a) Pingüinos: aves que nadan b) Pingüinos vuelan sobre el mar", "a)", "El texto dice que no vuelan y sí nadan."),
    ],
    [("Lee: «Cats sleep many hours a day. They also like to clean their fur with their tongues.» (fur = pelaje, tongues = lenguas). ¿Cuál es la idea general? a) Cómo viven los gatos b) El pelaje de los perros", "a)", "El texto habla de gatos.")],
    [
        ("¿Qué es un titular?", "Un título que resume la noticia", "Headline resume el hecho."),
        ("¿Qué preguntas responde el primer párrafo de una noticia?", "Quién, qué, cuándo y dónde", "Who, what, when y where."),
        ("¿Qué significa «wings»?", "Alas", "Las alas sirven para volar o nadar."),
    ],
    task("Lee esta noticia: «Library Opens Today. On Monday, 14 October, the new library of Santa Rosa School opened its doors. It has two thousand books and ten computers. The children enjoyed the first day.» (opened = abrió, doors = puertas, computers = computadores, enjoyed = disfrutaron). Escribe un titular distinto en inglés, el día y la fecha, y cuántos libros y computadores tiene.", "Titular: New Library at Santa Rosa School. Día: lunes 14 de octubre. Tiene 2.000 libros y 10 computadores.", ["titular razonable", "fecha correcta", "cantidades correctas"], ["hoja con respuestas", "nota del adulto"], ["confundir libros con computadores", "olvidar el día"], "Reconoce los datos bien encontrados y relee con él las cantidades."),
    "Relee el artículo de los pingüinos y subraya las tres palabras clave que más se repiten.",
    "Escribe en español tres datos que aprendiste sobre los pingüinos o sobre los árboles de la noticia.",
)

# ================================================================ OA 06
lesson(
    OA6, 1,
    "Los textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer y entender cantidades en textos: cuántos hay, cuánto y expresiones como a lot of, some y few. Sirve para comprender datos con números.",
    ["Sé contar y leer números hasta 100.", "Conozco How many...? y There are..."],
    [
        "Para expresar cantidades usamos números (twenty-five, one hundred, three hundred and fifty) y también palabras: a lot of (mucho/muchos), some (algunos), a few (pocos), many (muchos, con cosas que se cuentan) y no (ninguno). Para preguntar por una cantidad: How many...? se usa con cosas que se cuentan, como books; How much...? se usa con cosas que no se cuentan, como water.",
        "Para leer números grandes, separa las partes: 350 es three hundred and fifty. 25 es twenty-five. Los números como thirteen (13) y thirty (30) se parecen, pero no son iguales. Las frases como There are twelve girls and thirteen boys dan cantidades por grupo; sumándolas obtienes el total.",
        "Al leer un texto con cantidades, subraya el número y la cosa que cuenta. Pregúntate: ¿cuántos hay en total?, ¿cuántos hay de cada tipo?, ¿hay más de uno o de otro? Con estas preguntas comparas y calculas. Recuerda que a few significa pocos y a lot of significa mucho.",
    ],
    [("How many?", "¿cuántos?"), ("How much?", "¿cuánto?"), ("a lot of", "mucho / muchos"), ("a few", "pocos"), ("some", "algunos"), ("There are", "hay (varios)")],
    [
        ("Total de un texto", "Lee: «There are twenty-five students in Class 5C. There are twelve girls and thirteen boys. They have a lot of books and a few pencils.» (students = estudiantes, pencils = lápices). ¿Cuántos niños y niñas hay en total?", ["Busco girls: twelve.", "Busco boys: thirteen.", "12 + 13 = 25."], "25"),
        ("Cantidad con palabra", "En el mismo texto, ¿hay muchos o pocos lápices?", ["Busco pencils.", "Dice a few pencils.", "A few significa pocos."], "Pocos"),
    ],
    [
        ("Usar How much con cosas que se cuentan.", "How much es para lo que no se cuenta.", "Con books, students o pencils usa How many."),
        ("Confundir thirteen con thirty.", "Los números suenan parecido.", "Thirteen es 13 y thirty es 30; mira el final: -teen o -ty."),
    ],
    [
        ("Lee: «There are twenty-five students in Class 5C. There are twelve girls and thirteen boys. They have a lot of books and a few pencils.» ¿Cuántas niñas hay?", "12", "Dice twelve girls."),
        ("¿Qué significa «a lot of»?", "Mucho o muchos", "Se usa para cantidades grandes."),
        ("Elige la pregunta correcta para pedir la cantidad de lápices: a) How many pencils are there? b) How much pencils are there?", "a)", "Pencils se cuentan, por eso se usa How many."),
    ],
    [
        ("Lee: «The school has three hundred and fifty books.» ¿Qué número es?", "350", "Three hundred and fifty es 350."),
        ("Lee: «We have a few apples and a lot of oranges.» (oranges = naranjas). ¿Qué fruta hay en mayor cantidad? a) naranjas b) manzanas", "a)", "A lot of es más que a few."),
        ("Lee: «There is some milk in the cup.» (milk = leche). ¿Qué es cierto? a) Hay leche en el vaso b) No hay leche en el vaso", "a)", "Some indica que hay una cantidad de leche, sin decir cuánta."),
    ],
    [
        arith("Lee: «Class 5A has 14 girls and 16 boys.» ¿Cuántos estudiantes hay en total?", "14+16", "Se suman las niñas y los niños."),
        arith("Lee: «There are 350 books. 120 are about animals.» ¿Cuántos libros no son de animales?", "350-120", "Se resta la cantidad de libros de animales al total."),
        ("Lee: «We have a lot of oranges, some apples and no pears.» (pears = peras). ¿Qué fruta no hay?", "Peras", "No pears significa que no hay ninguna pera."),
    ],
    [
        ("Lee: «There are twenty chairs and fifteen tables.» Pablo dice que hay más mesas que sillas. ¿Es correcto?", "No; hay más sillas", "20 sillas son más que 15 mesas."),
        ("Una compañera lee thirteen y escribe 30. ¿Qué cifra era?", "13", "Thirteen es 13."),
    ],
    [
        arith("Lee: «A bus has forty seats. Twenty-seven are full.» (seats = asientos, full = ocupados). ¿Cuántos asientos están libres?", "40-27", "Se resta lo ocupado al total."),
        arith("Lee: «There are 4 boxes and each box has 6 pencils.» ¿Cuántos lápices hay en total?", "4*6", "Se multiplican las cajas por los lápices de cada una."),
    ],
    [("Lee: «At the market, there are a lot of tomatoes, some onions and no potatoes.» (market = feria, tomatoes = tomates, potatoes = papas). ¿Hay papas? a) No b) Sí", "a) No", "No potatoes significa ninguna papa.")],
    [
        ("¿Qué significa «a few»?", "Pocos", "A few indica una cantidad pequeña."),
        ("¿Cómo se lee 350 en inglés?", "Three hundred and fifty", "Se dicen las centenas y luego las decenas."),
        ("¿Qué pregunta usas para cosas que se cuentan?", "How many", "Con books o students se usa How many."),
    ],
    task("Lee este texto: «My school has two hundred students. There are eighty students in Grade 5, and a lot of them love football. There are some girls in the football team and five teachers help them.» (grade = curso, team = equipo, teachers = profesores). Escribe cuántos estudiantes hay en el colegio, cuántos están en 5.º, cuántos profesores ayudan, y si hay muchos o pocos estudiantes de 5.º que aman el fútbol.", "200 estudiantes; 80 en 5.º; 5 profesores; muchos aman el fútbol (a lot of).", ["tres números correctos", "dice muchos por a lot of"], ["hoja con respuestas", "nota del adulto"], ["confundir 200 con 80", "decir pocos en vez de muchos"], "Reconoce los números y relee con él las palabras a lot of y some."),
    "Relee el texto de la clase 5C y subraya con un color los números y con otro las palabras de cantidad.",
    "Escribe tres oraciones en español sobre tu curso con cantidades: cuántos son y cuántos hay de algo.",
)

lesson(
    OA6, 2,
    "Los mensajes escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer textos donde se pide información, se da, se contrasta y se justifica. Sirve para comprender correos y mensajes cotidianos.",
    ["Sé leer preguntas con what, when y where.", "Conozco because y but."],
    [
        "Para pedir información (request) se usan preguntas como «Could you tell me the time?» (¿podrías decirme la hora?), «What time does it start?» (¿a qué hora empieza?) y «Can you help me?» (¿puedes ayudarme?). Para dar información (give) se responde con datos: «It starts at four.»",
        "Para contrastar (contrast) dos ideas se usa but (pero) o however (sin embargo): «The game starts at four, but we meet at three-thirty.» Muestra que dos datos son distintos o se oponen. Para justificar (justify) se explica el motivo con because (porque) o so (por eso): «We meet early because we need to warm up.»",
        "Al leer un mensaje, identifica qué se pide, qué se responde, dónde hay un contraste y qué razón se da. Las palabras but, however, because y so son pistas. Si el mensaje dice «I cannot come because I am sick», el dato es que no puede venir y la justificación es que está enfermo.",
    ],
    [("Could you tell me...?", "¿podrías decirme...?"), ("What time does it start?", "¿a qué hora empieza?"), ("but / however", "pero / sin embargo"), ("because", "porque"), ("so", "por eso"), ("warm up", "calentar")],
    [
        ("Pedir y dar información", "Lee: «Leo: Could you tell me the time of the match? Mia: It starts at four, but we meet at three-thirty because we need to warm up.» (match = partido). ¿Qué pide Leo?", ["Busco la pregunta de Leo.", "Dice Could you tell me the time of the match?", "Leo pide la hora del partido."], "La hora del partido"),
        ("Contraste y justificación", "En el mismo texto, ¿por qué se juntan a las 3:30 y no a las 4:00?", ["Busco but y because.", "Dice because we need to warm up.", "La justificación es que necesitan calentar."], "Porque necesitan calentar"),
    ],
    [
        ("Pensar que but significa porque.", "Se confunden contraste y justificación.", "But es pero y because es porque."),
        ("Contestar con otro dato cuando se pide la hora.", "No se lee la pregunta con cuidado.", "Busca el dato que responde a What time."),
    ],
    [
        ("Lee: «Leo: Could you tell me the time of the match? Mia: It starts at four, but we meet at three-thirty because we need to warm up.» ¿A qué hora empieza el partido?", "A las 4:00", "Dice It starts at four."),
        ("Lee: «Leo: Could you tell me the time of the match? Mia: It starts at four, but we meet at three-thirty because we need to warm up.» ¿A qué hora se juntan?", "A las 3:30", "Dice we meet at three-thirty."),
        ("¿Qué significa «Could you tell me...?»", "¿Podrías decirme...?", "Es una forma cortés de pedir información."),
    ],
    [
        ("Lee: «Ana is tall, but her brother is short.» (tall = alto, short = bajo). ¿Qué contrasta la oración?", "La altura de Ana y la de su hermano", "But une dos ideas opuestas."),
        ("Lee: «It is raining, so we stay inside.» (stay inside = nos quedamos adentro). ¿Cuál es el motivo? a) está lloviendo b) estamos adentro", "a)", "Lo que viene antes de so es la causa."),
        ("Lee: «I cannot come because I am sick.» (sick = enfermo). ¿Cuál es la justificación?", "Está enfermo", "Because introduce la razón."),
    ],
    [
        ("Lee: «Ana: Can you help me? Leo: Yes, but I need ten minutes.» ¿Cuánto tiempo necesita Leo?", "Diez minutos", "Dice I need ten minutes."),
        ("Elige la palabra que marca contraste: a) however b) because", "a) however", "However significa sin embargo."),
        ("Completa: It is cold, ___ I wear a coat. Elige so o but.", "so", "El frío es la causa y usar abrigo es el efecto."),
    ],
    [
        ("Lee: «Nico: Can you help me with my homework? Sara: Yes, but I am busy until five.» (busy = ocupada). ¿Hasta qué hora está ocupada Sara?", "Hasta las cinco", "Dice until five."),
        ("Lee: «The museum is open on Sunday. However, it is closed on Monday.» (museum = museo, closed = cerrado). ¿Qué día está cerrado?", "El lunes", "Dice it is closed on Monday."),
    ],
    [
        ("Lee: «We need water because we play outside, so we bring bottles.» (bottles = botellas). ¿Qué traen?", "Botellas", "Dice we bring bottles."),
        ("En el mensaje anterior, ¿cuál es la razón por la que necesitan agua?", "Juegan afuera", "Dice because we play outside."),
    ],
    [("Lee: «The pool is open from nine to six. But the children's pool closes at four.» (pool = piscina, children's pool = piscina de niños). ¿A qué hora cierra la piscina de niños?", "A las cuatro", "Dice closes at four.")],
    [
        ("¿Qué significa «however»?", "Sin embargo", "Contrasta dos ideas."),
        ("En Inglés: ¿Qué palabra introduce una razón?", "because", "Because significa porque."),
        ("¿Qué pide «What time does it start?»", "La hora de inicio", "Pregunta cuándo empieza."),
    ],
    task("Lee este mensaje: «Hi Pablo, Could you tell me where the party is? I know it is on Saturday, but I do not know the place. I want to bring a gift, so I need to know the address. Thanks, Eli.» (place = lugar, gift = regalo, address = dirección). Escribe qué pide Eli, el contraste que hay y la razón por la que necesita saber la dirección.", "Pide el lugar de la fiesta. Contraste: sabe el día pero no el lugar. Razón: quiere llevar un regalo.", ["qué pide", "el contraste", "la razón"], ["hoja con respuestas", "nota del adulto"], ["mezclar contraste y razón", "olvidar qué se pide"], "Reconoce lo bien encontrado y relee con él marcando but y so."),
    "Relee el diálogo del partido y subraya but y because con dos colores distintos.",
    "Escribe un mensaje de tres líneas en español que pida información, dé un dato, tenga un contraste y una razón.",
)

lesson(
    OA6, 3,
    "Los textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer sobre gustos y preferencias, ocupaciones y personalidades. Sirve para comprender descripciones de personas y lo que les gusta.",
    ["Sé decir I like y I don't like.", "Conozco nurse, teacher y farmer."],
    [
        "Para expresar gustos y preferencias se usa like (gustar), love (encantar), enjoy (disfrutar), prefer (preferir) y don't like (no gustar). Pueden ir seguidos de un verbo con -ing: «My uncle likes cooking.» Para comparar: «She prefers tea to coffee» significa que prefiere el té al café.",
        "Las ocupaciones (jobs) son: nurse (enfermero), firefighter (bombero), teacher (profesor), chef (cocinero), farmer (agricultor) y mechanic (mecánico). Para describirlas: «My aunt is a nurse.» Para describir la personalidad (personality) se usan adjetivos: kind (amable), brave (valiente), funny (divertido), shy (tímido), hard-working (trabajador) y patient (paciente).",
        "Al leer, une los datos: ¿qué trabajo tiene?, ¿cómo es?, ¿qué le gusta? «My uncle is a chef. He is creative and hard-working. He loves cooking and he likes music.» La personalidad se prueba con acciones: si ayuda a todos, es kind. Si no habla con desconocidos, es shy.",
    ],
    [("nurse / firefighter / chef", "enfermero / bombero / cocinero"), ("kind / brave / funny", "amable / valiente / divertido"), ("shy / patient", "tímido / paciente"), ("hard-working", "trabajador"), ("enjoy", "disfrutar"), ("prefer", "preferir")],
    [
        ("Ocupación y personalidad", "Lee: «My aunt Rosa is a nurse. She is kind and patient. She helps sick people every day. She likes reading and she prefers tea to coffee.» (sick = enfermas, helps = ayuda). ¿Qué trabajo tiene Rosa y cómo es?", ["Busco is a nurse.", "Busco kind and patient.", "Es enfermera, amable y paciente."], "Es enfermera, amable y paciente"),
        ("Gustos", "En el mismo texto, ¿qué le gusta a Rosa y qué prefiere?", ["Busco likes.", "Busco prefers.", "Le gusta leer y prefiere el té al café."], "Le gusta leer y prefiere el té al café"),
    ],
    [
        ("Confundir shy con funny.", "Las dos son palabras de personalidad parecidas en escritura.", "Shy es tímido y funny es divertido."),
        ("Decir que a Rosa le gusta el café.", "Se lee mal prefers tea to coffee.", "Prefiere el té, no el café."),
    ],
    [
        ("Lee: «My aunt Rosa is a nurse. She is kind and patient. She helps sick people every day. She likes reading and she prefers tea to coffee.» ¿Qué hace Rosa cada día?", "Ayuda a personas enfermas", "Dice she helps sick people every day."),
        ("¿Qué significa «brave»?", "Valiente", "Brave es tener coraje."),
        ("¿Qué trabajo tiene un «firefighter»?", "Bombero", "Firefighter es quien apaga incendios."),
    ],
    [
        ("Lee: «Tomás is a firefighter. He is brave. He loves helping people.» ¿Qué le encanta a Tomás?", "Ayudar a la gente", "Dice he loves helping people."),
        ("Lee: «Iris is a teacher. She is funny and patient. She enjoys singing with her students.» (singing = cantando). ¿Qué disfruta Iris?", "Cantar con sus estudiantes", "Dice she enjoys singing."),
        ("Lee: «Carlos is shy. He does not talk to new people. He likes drawing.» ¿Qué le gusta hacer a Carlos?", "Dibujar", "Dice he likes drawing."),
    ],
    [
        ("Lee: «Dina is a vet. She is gentle and loves animals.» (vet = veterinaria, gentle = cariñosa). ¿Qué trabajo tiene Dina?", "Veterinaria", "Vet es veterinaria."),
        ("Lee: «He runs into a burning house to help a child.» (burning = que se quema). ¿Qué rasgo de personalidad muestra? a) brave b) shy", "a) brave", "Ayudar en un peligro muestra valentía."),
        ("Lee: «I like swimming, but I don't like running.» ¿Qué actividad no le gusta?", "Correr", "Don't like running significa que no le gusta correr."),
    ],
    [
        ("Lee: «Max is a farmer. He is hard-working. He gets up at five every morning.» (gets up = se levanta). ¿Cómo sabes que es hard-working?", "Porque se levanta a las cinco todos los días", "La acción de levantarse temprano lo demuestra."),
        ("Lee: «My brother is a mechanic. He is patient. He fixes cars slowly and carefully.» (fixes = arregla). ¿Cuál es su ocupación?", "Mecánico", "Dice he is a mechanic."),
    ],
    [
        ("Lee: «Eva prefers swimming to running.» ¿Qué actividad prefiere Eva?", "Nadar", "Prefers X to Y indica que prefiere X."),
        ("Una compañera dice que Carlos es divertido porque no habla con desconocidos. ¿Qué palabra describe mejor a Carlos? a) shy b) funny", "a) shy", "No hablar con desconocidos muestra timidez."),
    ],
    [("Lee: «My father is a chef. He is creative and he loves making new dishes.» (dishes = platos). ¿Qué hace un chef? a) cocina b) arregla autos", "a) cocina", "Chef es cocinero.")],
    [
        ("¿Qué significa «hard-working»?", "Trabajador", "Describe a alguien que trabaja mucho."),
        ("¿Qué significa «She prefers tea to coffee»?", "Prefiere el té al café", "Prefers X to Y indica preferencia."),
        ("¿Qué ocupación es «teacher»?", "Profesor", "Teacher enseña en un colegio."),
    ],
    task("Lee este texto: «My neighbor Ben is a firefighter. He is brave and strong. He likes running and he loves dogs. He prefers summer to winter.» (neighbor = vecino, strong = fuerte, dogs = perros). Escribe su ocupación, dos rasgos de personalidad, dos cosas que le gustan y qué estación prefiere.", "Bombero; valiente y fuerte; le gustan correr y los perros; prefiere el verano.", ["ocupación correcta", "dos rasgos", "dos gustos y una preferencia"], ["hoja con respuestas", "nota del adulto"], ["confundir rasgos con gustos", "decir invierno"], "Reconoce lo bien clasificado y relee con él marcando con colores ocupación, rasgos y gustos."),
    "Relee el texto de Rosa y subraya con tres colores su ocupación, su personalidad y sus gustos.",
    "Escribe en español la ocupación, dos rasgos y dos gustos de una persona que conozcas.",
)

lesson(
    OA6, 4,
    "Los mensajes escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer y entender qué está pasando en este momento con el presente continuo (am/is/are + verbo con -ing). Sirve para comprender mensajes sobre lo que alguien hace ahora.",
    ["Sé que play, read y run son verbos.", "Sé usar I am, he is y they are."],
    [
        "El presente continuo (present continuous) cuenta lo que ocurre ahora, en el momento de hablar. Se forma con am, is o are y un verbo terminado en -ing: «I am playing», «She is reading», «They are riding bikes». Se usa con palabras como now (ahora), right now (justo ahora) y at the moment (en este momento).",
        "Para negar se agrega not: «It is not raining» o «It isn't raining». Para preguntar se cambia el orden: «Are you playing?» y «What is she doing?» (¿qué está haciendo ella?). La respuesta es corta: «Yes, I am» o «No, I'm not». Con run se escribe running y con ride se escribe riding.",
        "Al leer un mensaje, busca el sujeto (I, she, they) y el verbo con -ing. Pregúntate: ¿quién?, ¿qué hace ahora? y ¿dónde está? Si el texto dice «Mia is reading under a tree», el sujeto es Mia, la acción es leer y el lugar es debajo de un árbol.",
    ],
    [("now / right now", "ahora / justo ahora"), ("am / is / are + -ing", "forma del presente continuo"), ("What is she doing?", "¿qué está haciendo ella?"), ("running / riding", "corriendo / montando"), ("isn't raining", "no está lloviendo"), ("under a tree", "debajo de un árbol")],
    [
        ("Quién hace qué", "Lee: «Hi Mom! I am at the park. I am playing football with Leo. Mia is reading under a tree. Two boys are riding bikes. It is not raining. See you at six!» (see you = nos vemos). ¿Qué está haciendo Mia?", ["Busco Mia.", "Dice Mia is reading under a tree.", "Está leyendo debajo de un árbol."], "Leyendo debajo de un árbol"),
        ("Contar personas", "En el mismo mensaje, ¿cuántos niños andan en bicicleta?", ["Busco riding bikes.", "Dice Two boys are riding bikes.", "Son dos niños."], "2"),
    ],
    [
        ("Escribir «She reading» sin is.", "Falta el verbo auxiliar.", "Con -ing usa am, is o are: She is reading."),
        ("Escribir «runing» o «riding» sin pensar en la ortografía.", "Se olvida cambiar la escritura del verbo.", "Run se escribe running, ride se escribe riding."),
    ],
    [
        ("Lee: «Hi Mom! I am at the park. I am playing football with Leo. Mia is reading under a tree. Two boys are riding bikes. It is not raining. See you at six!» ¿Qué hace quien escribe?", "Juega fútbol con Leo", "Dice I am playing football with Leo."),
        ("Lee: «Hi Mom! I am at the park. I am playing football with Leo. Mia is reading under a tree. Two boys are riding bikes. It is not raining. See you at six!» ¿Está lloviendo?", "No", "Dice It is not raining."),
        ("¿Qué significa «right now»?", "Justo ahora", "Right now indica el momento actual."),
    ],
    [
        ("Elige la oración correcta: a) She is singing. b) She singing.", "a)", "Se necesita is antes de singing."),
        ("Completa con am, is o are: They ___ swimming now.", "are", "They va con are."),
        ("Completa: I ___ eating an apple at the moment.", "am", "I va con am."),
    ],
    [
        ("Completa: The cat ___ sleeping now. Elige is o are.", "is", "The cat es una sola cosa y va con is."),
        ("Lee: «Where are you? I am waiting at the gate.» (waiting = esperando). ¿Qué está haciendo quien escribe?", "Esperando en el portón", "Dice I am waiting at the gate."),
        ("Pregunta: «Are you studying?» ¿Cuál es la respuesta corta afirmativa? a) Yes, I am. b) Yes, I do.", "a)", "La respuesta repite am."),
    ],
    [
        ("Lee: «Pedro is washing the car. His sister is cleaning the window.» (washing = lavando, cleaning = limpiando). ¿Quién limpia la ventana?", "Su hermana", "Dice his sister is cleaning the window."),
        ("Una pregunta: «What is Pedro doing?» ¿Cuál es la respuesta según el texto anterior?", "Está lavando el auto", "Washing the car es lavar el auto."),
    ],
    [
        ("Elige la forma correcta de run: a) running b) runing", "a) running", "Run duplica la n antes de -ing."),
        ("Lee: «We are making lunch. Dad is carrying the bread.» (carrying = llevando). ¿Quién lleva el pan?", "El papá", "Dice Dad is carrying the bread."),
    ],
    [("Lee: «Right now, Ana is talking on the phone and Leo is doing his homework.» (talking = hablando, phone = teléfono, homework = tarea). ¿Qué hace Leo?", "Su tarea", "Dice is doing his homework.")],
    [
        ("¿Cómo se forma el presente continuo?", "Con am, is o are y un verbo con -ing", "Ejemplo: She is reading."),
        ("¿Qué significa «at the moment»?", "En este momento", "Indica que ocurre ahora."),
        ("¿Cómo se escribe «ride» con -ing?", "riding", "Se quita la e y se agrega -ing."),
    ],
    task("Lee este mensaje: «Hello! I am at home. My dad is cooking soup in the kitchen. My sister is drawing at the table. Our cat is sleeping on the sofa. I am writing this message.» (cooking = cocinando, drawing = dibujando, sleeping = durmiendo, sofa = sofá). Escribe qué hace cada persona o animal ahora: papá, hermana, gato y quien escribe.", "Papá cocina sopa; hermana dibuja; gato duerme en el sofá; quien escribe escribe el mensaje.", ["cuatro acciones", "las relaciona con la persona correcta"], ["hoja con respuestas", "nota del adulto"], ["confundir quién hace qué", "olvidar al gato"], "Reconoce las acciones y relee con él subrayando is y el verbo con -ing."),
    "Relee el mensaje del parque y subraya todos los verbos con -ing.",
    "Escribe cuatro oraciones en español que digan qué está haciendo ahora cada persona de tu casa.",
)

lesson(
    OA6, 5,
    "Los textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer sobre acciones del pasado: verbos terminados en -ed, algunos verbos irregulares (went, ate, saw, had) y preguntas con did. Sirve para comprender qué pasó en un texto.",
    ["Sé identificar el presente continuo.", "Conozco was y were como pasado de be."],
    [
        "El pasado simple (simple past) cuenta lo que ocurrió y ya terminó. Los verbos regulares terminan en -ed: visit - visited (visitó), cook - cooked (cocinó), watch - watched (miró). Hay verbos irregulares que cambian: go - went (fue), eat - ate (comió), see - saw (vio), have - had (tuvo), be - was/were (fue/estuvo).",
        "Para preguntar en pasado se usa did: «Did you go to the beach?» (¿fuiste a la playa?). La respuesta es corta: «Yes, I did» o «No, I didn't». Para negar se usa didn't y el verbo sin cambiar: «I didn't swim because the water was cold.» Las palabras yesterday (ayer), last weekend (el fin de semana pasado) y ago (hace) indican pasado.",
        "Al leer un texto en pasado, pregúntate: ¿quién?, ¿qué hizo?, ¿cuándo? y ¿cómo estuvo? Subraya los verbos en pasado. Fíjate en el verbo después de didn't: está en su forma simple (swim, no swam). Con ese cuidado entenderás el relato.",
    ],
    [("visited / cooked / watched", "visitó / cocinó / miró"), ("went / ate / saw / had", "fue / comió / vio / tuvo"), ("was / were", "fue o estuvo"), ("Did you...?", "¿tú...? (pasado)"), ("didn't", "no (pasado)"), ("last weekend / yesterday", "el fin de semana pasado / ayer")],
    [
        ("Acciones pasadas", "Lee: «Last weekend, I visited my neighbor. We cooked soup and watched a film. I was tired but happy. On Sunday, I went to the beach with my friend. I didn't swim because the water was cold.» (film = película, neighbor = vecino o vecina). ¿Qué hicieron en la casa de la vecina o del vecino?", ["Busco visited my grandma.", "Busco cooked soup and watched a film.", "Cocinaron sopa y miraron una película."], "Cocinaron sopa y miraron una película"),
        ("Negación en pasado", "En el mismo texto, ¿por qué no nadó la persona?", ["Busco didn't swim.", "Dice because the water was cold.", "No nadó porque el agua estaba fría."], "Porque el agua estaba fría"),
    ],
    [
        ("Escribir «I didn't swam».", "Después de didn't el verbo va en su forma simple.", "Se dice I didn't swim."),
        ("Pensar que went es el pasado de want.", "Se confunden verbos irregulares.", "Went es el pasado de go."),
    ],
    [
        ("Lee: «Last weekend, I visited my neighbor. We cooked soup and watched a film. I was tired but happy. On Sunday, I went to the beach with my friend. I didn't swim because the water was cold.» ¿Con quién fue a la playa?", "Con su amigo o amiga", "Dice with my friend."),
        ("¿Cuál es el pasado de «go»?", "went", "Go es irregular y su pasado es went."),
        ("¿Cuál es el pasado de «cook»?", "cooked", "Los verbos regulares agregan -ed."),
    ],
    [
        ("Elige la oración en pasado: a) I ate pasta. b) I eat pasta.", "a)", "Ate es el pasado de eat."),
        ("Completa: Yesterday I ___ (see) a rainbow. Elige saw o seen.", "saw", "Saw es el pasado de see."),
        ("Completa la pregunta: ___ you go to school yesterday? Elige Did o Do.", "Did", "Did se usa para preguntar en pasado."),
    ],
    [
        ("¿Cuál es el pasado de «have»?", "had", "Have es irregular."),
        ("Lee: «We watched TV and had dinner.» ¿Qué hicieron?", "Miraron televisión y cenaron", "Watched TV y had dinner son acciones pasadas."),
        ("Pregunta: «Did you see the film?» ¿Cuál es la respuesta corta afirmativa? a) Yes, I did. b) Yes, I do.", "a)", "Did se responde con did."),
    ],
    [
        ("Lee: «Tom visited his uncle and had lunch. They played cards.» (cards = cartas). ¿A qué jugaron Tom y su tío?", "A las cartas", "Dice they played cards."),
        ("Lee: «Did you go to the park?» «No, I didn't. I stayed home.» (stayed = me quedé). ¿Dónde estuvo la persona?", "En su casa", "Dice I stayed home."),
    ],
    [
        ("Lee: «Last Friday, we had a test. It was easy.» ¿Cómo fue la prueba?", "Fácil", "Easy es fácil."),
        ("Una compañera dice «I didn't ate». ¿Cómo se corrige?", "I didn't eat", "Después de didn't el verbo va en forma simple."),
    ],
    [("Lee: «Yesterday I was at home. My friends were at school.» ¿Quién estuvo en el colegio?", "Los amigos", "Were va con friends.")],
    [
        ("¿Cuál es el pasado de «see»?", "saw", "See es irregular."),
        ("¿Cómo se pregunta en pasado: Did you swim? o Are you swim?", "Did you swim?", "Did se usa en pasado."),
        ("¿Qué significa «yesterday»?", "Ayer", "Indica que ocurrió un día antes."),
    ],
    task("Lee este texto: «Last Saturday, Carla went to the market with her mother. They bought apples and bread. Carla saw a small dog. She didn't touch it because it was shy. Then they went home and ate lunch.» (bought = compraron, touch = tocar). Escribe cuatro cosas que hicieron en orden, una cosa que Carla no hizo y por qué.", "Fueron al mercado; compraron manzanas y pan; Carla vio un perro; fueron a casa y almorzaron. No tocó al perro porque era tímido.", ["cuatro acciones en orden", "la acción que no hizo", "la razón"], ["hoja con respuestas", "nota del adulto"], ["decir que tocó al perro", "no explicar la razón"], "Reconoce las acciones y relee con él subrayando los verbos en pasado."),
    "Relee el texto del fin de semana y subraya tres verbos en pasado: dos regulares y uno irregular.",
    "Escribe cuatro oraciones en español sobre lo que hiciste el fin de semana pasado, y luego escribe una en inglés con went o ate.",
)

"""Cuaderno del estudiante, 7.º básico Inglés (oficial), IN07 OA 02 (palabras clave, expresiones frecuentes, vocabulario temático,
conectores y sonidos en textos orales). Las «escuchas» las lee un adulto; los sonidos se describen con ejemplos conocidos.
"""
from __future__ import annotations

from student_content_in7_a import ADULT, lesson, task

OA2 = "IN07 OA 02"

CHAT = "«Nico: Hi, Sara! What's up? Sara: Not much. I'm making a poster for science class. Nico: Cool! Can I help? Sara: Of course. Just a minute, I need some glue. Nico: No problem. By the way, do you want to take a break and have a snack? Sara: Good idea. See you at the cafeteria.» (poster = afiche, glue = pegamento, snack = colación, cafeteria = casino)"
SHOP = "«Customer: Excuse me, how much is this scarf? Seller: It's six thousand pesos. Customer: That's a lot! Do you have a cheaper one? Seller: Sorry, I'm afraid not. But this blue one is on sale. Customer: Perfect, I'll take it. Thank you!» (scarf = bufanda, cheaper = más barato, on sale = en oferta, I'll take it = me lo llevo)"
ROUTINE = "«Before school, Tomás feeds his dog. After school, he helps in the garden, and his sister helps too. He does his homework while his sister watches TV. When they finish, they play chess or cards.» (feeds = alimenta, garden = jardín, homework = tarea, watches = ve, finish = terminan, cards = naipes)"
SALAD = "«How to make a simple fruit salad. First, wash the fruit. Second, cut it into small pieces with an adult's help. Next, put the pieces in a bowl. Finally, add a little orange juice. You can eat it now or you can keep it in the fridge.» (wash = lavar, pieces = trozos, bowl = bol, juice = jugo, keep = guardar, fridge = refrigerador)"
BIKE = "«Ignacio is sad because his bike is broken. He needs a new tire, so he asks his uncle for help. When his uncle arrives, they fix the tire together. Ignacio is happy again, and he can ride before dinner.» (broken = rota, tire = neumático, uncle = tío, fix = arreglar, together = juntos, dinner = cena)"
SPORTS = "«Saturday was the school sports day. The red team and the blue team ran a race of one hundred meters on the track. The referee blew his whistle, and Camila crossed the line first. She won a gold medal. The blue team scored a goal in the last minute of the football match.» (team = equipo, race = carrera, track = pista, referee = árbitro, whistle = silbato, crossed = cruzó, won = ganó, gold = oro, scored = anotó)"
ECO = "«Our class has an energy project. We turn off the lights and we recycle paper, plastic and glass. We collect rubbish from the river bank every month. We want a cleaner forest and a healthy river.» (energy = energía, turn off = apagar, lights = luces, glass = vidrio, collect = recoger, rubbish = basura, river bank = ribera, healthy = sano)"
KITCHEN = "«Today's recipe is pancakes. The ingredients are flour, milk, eggs and a little sugar. Mix them in a big bowl with a spoon. Then ask an adult to cook the pancakes in a pan.» (recipe = receta, pancakes = panqueques, ingredients = ingredientes, flour = harina, mix = mezclar, spoon = cuchara, pan = sartén)"
ZOO = "«Hi, I'm Hugo. First, I go to the zoo with my grandfather. When we arrive, we see a giraffe. Next, we have lunch, so we eat sandwiches and eggs. After that, we buy a small gift. Finally, we go home.» (zoo = zoológico, giraffe = jirafa, arrive = llegar, sandwiches = sándwiches, gift = regalo)"
SHADE = "«It was a hot day and everyone was thirsty. Mario drank a big glass of water. Then he sat in the shade of a tall tree, because the sun was strong. After ten minutes, he felt much better.» (hot = caluroso, thirsty = con sed, drank = bebió, sat = se sentó, strong = fuerte, felt = se sintió)"
MAT = "Un adulto lee en voz alta cada texto escrito en los ejercicios; una hoja para tapar el guion y lápiz."

# ------------------------------------------------------------------ clase 1
lesson(
    OA2, 1, MAT,
    "Aprenderé a reconocer expresiones de uso frecuente (chunks), que son grupos de palabras que se usan juntas. Sirve para entender conversaciones cotidianas sin traducir palabra por palabra.",
    ["Sé saludar y despedirme en inglés.", "Conozco palabras como help, minute y problem."],
    [
        "Un chunk es un grupo de palabras que se aprende y se usa como un bloque, como What's up? (¿qué tal?), Of course (claro), Just a minute (un momento), No problem (no hay problema) o See you later (hasta luego). Si traduces cada palabra por separado, el sentido se pierde: By the way no habla de un camino, sino que introduce un comentario nuevo («a propósito»).",
        "Los chunks aparecen en saludos, en pedidos y en respuestas. Excuse me llama la atención de manera cortés. How much is...? pregunta un precio. That's a lot! puede significar que algo es caro o grande. I'm afraid not es una forma amable de decir «lo siento, no». On sale significa en oferta y take a break significa tomar un descanso.",
        "Para reconocerlos al escuchar, no te detengas en una palabra. Fíjate en el tono, en lo que ocurre antes y después, y en la situación. Si alguien dice Just a minute mientras busca algo, quiere que esperes. Con práctica, tu oído aprende a captar el bloque completo en lugar de cada palabra.",
    ],
    [("What's up?", "¿Qué tal? Saludo informal"), ("Of course", "claro, por supuesto"), ("Just a minute", "un momento"), ("By the way", "a propósito"), ("on sale", "en oferta"), ("See you later", "hasta luego")],
    [
        ("Entender un chunk en contexto", ADULT + CHAT + " ¿Qué quiere decir Sara con Just a minute?", ["Sara dice Just a minute y enseguida agrega I need some glue.", "Necesita buscar algo antes de seguir.", "Entonces pide a Nico que espere un momento."], "Que espere un momento"),
        ("Un chunk que no se traduce palabra por palabra", ADULT + CHAT + " ¿Para qué usa Nico By the way?", ["Nico estaba hablando del afiche.", "Con By the way cambia de tema y propone un descanso.", "No significa «por el camino»."], "Para introducir un comentario nuevo: a propósito"),
    ],
    [
        ("Traducir By the way como «por el camino».", "Se traduce palabra por palabra y se pierde el sentido del bloque.", "Reconoce By the way como bloque que introduce un comentario."),
        ("Entender I'm afraid not como «tengo miedo».", "Se toma afraid por separado.", "En ese bloque significa «lo siento, no»."),
    ],
    [
        (ADULT + CHAT + " ¿Qué significa Of course? a) claro, por supuesto b) de curso escolar", "a) claro, por supuesto", "Sara responde así cuando Nico pregunta si puede ayudar."),
        (ADULT + CHAT + " ¿Qué significa Just a minute? a) un momento b) un minuto exacto", "a) un momento", "Minute es minuto y el bloque pide esperar poco rato."),
        (ADULT + SHOP + " ¿Qué quiere decir on sale? a) en oferta b) en la sala", "a) en oferta", "La bufanda azul tiene un precio especial."),
    ],
    [
        (ADULT + CHAT + " ¿Qué propone Nico con take a break? a) descansar un rato b) terminar el afiche", "a) descansar un rato", "Take a break es tomar un descanso y la propuesta incluye una colación."),
        (ADULT + SHOP + " ¿Para qué sirve Excuse me al comienzo? a) para llamar la atención con cortesía b) para despedirse", "a) para llamar la atención con cortesía", "La clienta lo dice antes de preguntar el precio."),
        (ADULT + CHAT + " Nico pregunta Can I help? ¿Qué chunk usa Sara para aceptar?", "Of course", "Sara responde Of course y sigue con su trabajo."),
    ],
    [
        (ADULT + SHOP + " La clienta dice That's a lot! ¿Qué opina del precio? a) que es caro b) que es barato", "a) que es caro", "Después pregunta si hay uno más barato."),
        ("Completa la conversación. A: I need a pen. B: ___ Here you are. (here you are = aquí tienes; see you later = hasta luego; I'm afraid not = lo siento, no). Opciones: No problem / See you later / I'm afraid not.", "No problem", "Responde con amabilidad y entrega el lápiz; las otras opciones no calzan."),
        ("¿Qué chunk usas para despedirte de alguien que verás más tarde? a) See you later b) By the way", "a) See you later", "See you later significa hasta luego."),
    ],
    [
        ("¿Cuál es la mejor estrategia para entender By the way? a) tratarla como un bloque que introduce un comentario b) traducir by, the y way por separado", "a) tratarla como un bloque que introduce un comentario", "El sentido está en el bloque completo."),
        (ADULT + SHOP + " El vendedor dice I'm afraid not. ¿Significa que tiene miedo? Responde sí o no.", "No", "Es una forma amable de decir «lo siento, no»; no habla de miedo."),
    ],
    [
        (ADULT + SHOP + " Ordena las acciones. A) El cliente pregunta el precio. B) El cliente decide comprar. C) El vendedor ofrece una bufanda en oferta.", "A, C, B", "Primero pregunta, luego el vendedor ofrece otra opción y al final el cliente la compra."),
        (ADULT + CHAT + " ¿Qué chunk usa Nico para cambiar de tema? a) By the way b) No problem", "a) By the way", "Con él pasa del afiche al descanso."),
    ],
    [(ADULT + "Una compañera te dice: «Just a minute, I'm tying my shoes.» (tying = atando, shoes = zapatos). ¿Qué debes hacer?", "Esperar un momento", "Just a minute pide que esperes mientras ella se ata los zapatos.")],
    [
        ("En Inglés de 7.º (OA 2, clase 1): ¿Qué es un chunk?", "Un grupo de palabras que se usa como bloque", "Se aprende y se entiende completo."),
        ("En Inglés de 7.º (OA 2, clase 1): ¿Qué significa «No problem»?", "No hay problema", "Se usa para aceptar un pedido o responder a un agradecimiento."),
        ("¿Qué haces si no entiendes una palabra dentro de un chunk?", "Me fijo en el bloque completo y en la situación", "El sentido del bloque no depende de cada palabra."),
    ],
    task("Un adulto lee dos veces esta mini conversación: «A: What's up? B: Not much. Do you want to play chess? A: Good idea! Just a minute, I need my bag. B: No problem.» (chess = ajedrez, bag = mochila). Escribe en tu hoja los chunks que oíste y qué significan en español.", "What's up? = ¿qué tal?; Not much = no mucho; Good idea = buena idea; Just a minute = un momento; No problem = no hay problema.", ["anota al menos cuatro chunks", "explica cada uno en español", "evita traducir palabra por palabra"], ["hoja con chunks y significados", "nota del adulto"], ["traducir What's up como «qué arriba»", "olvidar el significado de Just a minute"], "Reconoce los chunks que acertó y practica con la persona adulta decirlos en voz alta con su significado."),
    "Pide a un adulto que lea de nuevo la conversación de la tienda y levanta la mano cada vez que oigas un chunk.",
    "Escribe una conversación de cuatro líneas entre un cliente y un vendedor, usando Excuse me, How much is...? y I'll take it.",
)

# ------------------------------------------------------------------ clase 2
lesson(
    OA2, 2, MAT,
    "Aprenderé a seguir el orden y las relaciones entre ideas con conectores como first, next, finally, before, after, when, while, because, or y too. Sirve para entender secuencias y razones en textos orales.",
    ["Sé el significado de now, school y homework.", "Sé que un texto tiene un orden."],
    [
        "Los conectores (connectors) unen ideas y muestran su relación. Para el orden se usan first (primero), second (segundo), next (luego), finally (finalmente), before (antes de) y after (después de). Para el tiempo se usan when (cuando) y while (mientras): en while, dos acciones ocurren a la vez. Para la causa se usa because (porque) y so (por eso).",
        "Otros conectores agregan o eligen. Too significa «también» y va al final de la oración: his sister helps too. Or presenta una elección entre dos opciones: chess or cards. Cuando oigas un conector, pregúntate qué relación marca: ¿orden, tiempo simultáneo, razón, elección o suma de una idea?",
        "En la práctica, anota los conectores como una escalera: first, next, finally. Así reconstruyes qué ocurrió primero. Para las razones, busca because: la razón viene después. En Ignacio is sad because his bike is broken, la razón de la tristeza es la bicicleta rota. Escucha una vez para el sentido general y otra para ordenar los conectores.",
    ],
    [("first / next / finally", "primero / luego / finalmente"), ("before / after", "antes de / después de"), ("when", "cuando"), ("while", "mientras"), ("because / so", "porque / por eso"), ("or / too", "o / también")],
    [
        ("Ordenar con conectores", ADULT + SALAD + " ¿Qué se hace después de cortar la fruta?", ["Busco Second, cut it: es el paso 2.", "El siguiente conector es Next.", "Next dice put the pieces in a bowl."], "Poner los trozos en un bol"),
        ("Causa con because", ADULT + BIKE + " ¿Por qué está triste Ignacio?", ["Busco la palabra because.", "Dice because his bike is broken.", "La razón viene después de because."], "Porque su bicicleta está rota"),
    ],
    [
        ("Pensar que la razón está antes de because.", "En inglés la razón se dice después de because.", "Lee la parte que viene después para encontrar la causa."),
        ("Confundir before con after.", "Los dos marcan orden pero en sentido contrario.", "Before school es antes de la escuela; after school es después."),
    ],
    [
        (ADULT + SALAD + " ¿Qué se hace primero? a) lavar la fruta b) agregar jugo", "a) lavar la fruta", "El paso First es wash the fruit."),
        (ADULT + ROUTINE + " ¿Qué hace Tomás antes de ir al colegio? a) alimenta a su perro b) ayuda en el jardín", "a) alimenta a su perro", "Before school, Tomás feeds his dog."),
        (ADULT + BIKE + " ¿Qué palabra introduce la razón de la tristeza? a) because b) before", "a) because", "Because significa porque."),
    ],
    [
        (ADULT + SALAD + " ¿Qué palabra marca el último paso? a) finally b) next", "a) finally", "Finally significa finalmente."),
        (ADULT + ROUTINE + " ¿Qué hace Tomás después del colegio? a) ayuda en el jardín b) alimenta a su perro", "a) ayuda en el jardín", "After school, he helps in the garden."),
        (ADULT + ROUTINE + " ¿Qué significa while en «while his sister watches TV»? a) mientras b) antes", "a) mientras", "Dos acciones ocurren al mismo tiempo."),
    ],
    [
        (ADULT + SALAD + " Ordena. A) Poner los trozos en un bol. B) Cortar la fruta. C) Agregar jugo de naranja.", "B, A, C", "Los conectores son Second, Next y Finally."),
        (ADULT + SALAD + " En «now or in the fridge», ¿qué indica or? a) una elección entre dos opciones b) una razón", "a) una elección entre dos opciones", "Se puede comer ahora o guardar."),
        (ADULT + BIKE + " ¿Qué hace Ignacio porque la bicicleta está rota? a) pide ayuda a su tío b) vende la bicicleta", "a) pide ayuda a su tío", "Dice so he asks his uncle for help."),
    ],
    [
        (ADULT + BIKE + " ¿Qué ocurre primero? a) llega el tío b) arreglan el neumático", "a) llega el tío", "Dice When his uncle arrives, they fix the tire."),
        ("Completa con before o after: «I turn on the TV ___ I watch a movie» (turn on = encender, movie = película). Escribe la palabra que da sentido lógico.", "before", "Primero se enciende la tele y después se ve la película; con after no tendría sentido."),
    ],
    [
        (ADULT + SALAD + " Un compañero dice que el jugo se agrega antes de cortar la fruta. ¿Qué conector del texto lo contradice? a) Finally b) Second", "a) Finally", "Finally marca el último paso: add a little orange juice; cortar es Second."),
        ("Escribe el conector que falta: «Mateo plays the piano and Lara plays the piano ___». (también)", "too", "Too significa también y va al final."),
    ],
    [(ADULT + "Una persona dice: «First, put on your shoes. Next, take your bag. Finally, lock the door.» (lock = cerrar con llave). ¿Qué paso va justo antes de cerrar la puerta?", "Tomar la mochila", "Next, take your bag viene antes de Finally.")],
    [
        ("En Inglés de 7.º (OA 2, clase 2): ¿Qué indica «while»?", "Que dos acciones ocurren a la vez", "Significa mientras en español."),
        ("¿Qué indica «because»?", "La razón de algo", "Significa porque en español."),
        ("¿Qué conector significa también?", "Too", "Se pone al final de la oración."),
    ],
    task("Un adulto lee dos veces este texto: «Before breakfast, Carla brushes her teeth. After breakfast, she packs her bag. She walks to school because the bus is full. When she arrives, she plays with her friends or reads a book.» (brushes = cepilla, packs = prepara, full = lleno, arrives = llega). Escribe en tu hoja: qué hace Carla antes del desayuno, por qué camina y qué hace al llegar.", "Antes del desayuno se cepilla los dientes; camina porque el bus está lleno; al llegar juega con sus amigos o lee un libro.", ["responde las tres preguntas", "identifica before, because y when", "no inventa datos"], ["hoja con tres respuestas", "nota del adulto"], ["decir que camina porque ama caminar", "confundir antes y después del desayuno"], "Reconoce las respuestas correctas y repasa con la persona adulta qué relación marca cada conector."),
    "Pide a un adulto que lea otra vez el texto de la ensalada y señala con el dedo cada conector que oigas.",
    "Escribe tres frases en inglés sobre tu rutina de la tarde usando before, after y while.",
)

# ------------------------------------------------------------------ clase 3
lesson(
    OA2, 3, MAT,
    "Aprenderé a reconocer vocabulario de un tema (deportes, medio ambiente y cocina) y a usarlo como pista para entender textos orales. Sirve para anticipar de qué hablan y deducir palabras nuevas.",
    ["Sé que las palabras se agrupan por temas.", "Conozco palabras como team, paper, milk y river."],
    [
        "El vocabulario temático (thematic vocabulary) es el conjunto de palabras de un tema. En deportes: race (carrera), team (equipo), goal (gol), medal (medalla), referee (árbitro), track (pista) y whistle (silbato). En medio ambiente: recycle (reciclar), energy (energía), rubbish (basura), forest (bosque), river (río) y plastic (plástico). En cocina: recipe (receta), ingredient (ingrediente), bowl (bol), spoon (cuchara), flour (harina) y mix (mezclar).",
        "Cuando oyes varias palabras del mismo tema, ya sabes de qué se habla, aunque algunas palabras sean nuevas. Si oyes race, track y medal juntas, el tema son los deportes. Con ese tema puedes deducir que una palabra desconocida en la misma oración está relacionada. Esta estrategia se llama usar el contexto.",
        "Un buen oyente hace una lista mental de pistas: ¿qué palabras se repiten?, ¿a qué tema pertenecen? y ¿qué título le pondría al texto? Ten cuidado con las palabras que pertenecen a varios temas. Por ejemplo, bowl en cocina es un recipiente, pero el tema lo decide el resto de las palabras.",
    ],
    [("race / team / goal", "carrera / equipo / gol"), ("referee", "árbitro"), ("recycle / rubbish", "reciclar / basura"), ("energy", "energía"), ("ingredient / recipe", "ingrediente / receta"), ("bowl / spoon", "bol / cuchara")],
    [
        ("Tema por palabras clave", ADULT + SPORTS + " ¿De qué tema habla el texto y qué palabras lo muestran?", ["Escucho race, track, referee, medal y goal.", "Todas pertenecen al mundo del deporte.", "El tema es el día de deportes del colegio."], "Deportes; race, track, referee, medal y goal"),
        ("Clasificar una palabra", "¿A qué tema pertenece la palabra flour (harina): deportes, medio ambiente o cocina?", ["Pienso en dónde se usa la harina.", "Se usa para hacer panqueques, pan o tortas.", "Es un ingrediente de cocina."], "Cocina"),
    ],
    [
        ("Clasificar una palabra por una sola pista, sin mirar las demás.", "Hay palabras que sirven en más de un tema.", "Mira varias palabras clave juntas antes de decidir el tema."),
        ("Pensar que una palabra nueva hace que no se entienda nada.", "Se ignora el contexto.", "Apóyate en el tema y en las palabras que la rodean."),
    ],
    [
        (ADULT + SPORTS + " ¿De qué trata el texto? a) de un día de deportes b) de una receta", "a) de un día de deportes", "Dice sports day, race, medal y goal."),
        (ADULT + ECO + " ¿De qué trata el texto? a) de cuidar el medio ambiente b) de un partido de fútbol", "a) de cuidar el medio ambiente", "Dice recycle, rubbish, forest y river."),
        (ADULT + KITCHEN + " ¿Qué utensilio sirve para mezclar? a) la cuchara b) la harina", "a) la cuchara", "Spoon es cuchara; flour es un ingrediente."),
    ],
    [
        (ADULT + SPORTS + " ¿Qué hace el árbitro (referee)?", "Hace sonar el silbato", "Dice The referee blew his whistle."),
        (ADULT + ECO + " ¿Qué tres materiales recicla el curso? a) papel, plástico y vidrio b) pilas, madera y metal", "a) papel, plástico y vidrio", "Dice recycle paper, plastic and glass."),
        (ADULT + KITCHEN + " ¿Cuál de estas palabras no es un ingrediente: flour, milk, spoon, eggs?", "spoon", "La cuchara es un utensilio; las otras son alimentos."),
    ],
    [
        ("Clasifica por tema las palabras goal, recycle y bowl. Responde en ese orden con deportes, medio ambiente o cocina.", "deportes, medio ambiente, cocina", "Goal es gol, recycle es reciclar y bowl es un recipiente de cocina."),
        (ADULT + SPORTS + " ¿Qué medalla ganó Camila?", "Una medalla de oro", "Dice She won a gold medal."),
        (ADULT + ECO + " ¿Cada cuánto recogen basura de la ribera del río?", "Cada mes", "Dice every month."),
    ],
    [
        ("Una palabra desconocida aparece junto a race, track y medal. ¿De qué tema es probablemente? a) deportes b) cocina", "a) deportes", "Las palabras que la rodean son de deportes."),
        ("En un texto aparecen mix, bowl, ingredients y oven (horno). ¿Qué título le sirve? a) Recipe b) Football match", "a) Recipe", "Las palabras clave son de cocina."),
    ],
    [
        ("¿Cuántas de estas palabras son del tema deportes? goal, referee, spoon, medal, flour, whistle (silbato)", "4", "Goal, referee, medal y whistle son de deportes."),
        (ADULT + SPORTS + " ¿Qué equipo anotó un gol en el último minuto? a) el equipo azul b) el equipo rojo", "a) el equipo azul", "Dice The blue team scored a goal."),
    ],
    [(ADULT + "En la reunión de curso alguien propone: «To save energy, turn off the lights and the computer.» (save = ahorrar, lights = luces). ¿Qué dos cosas se apagan?", "Las luces y el computador", "Dice turn off the lights and the computer.")],
    [
        ("¿Qué es vocabulario temático?", "Las palabras que pertenecen a un mismo tema", "Ayudan a saber de qué trata un texto."),
        ("¿Qué significa «recycle»?", "Reciclar", "Es dar nuevo uso a materiales."),
        ("¿A qué tema pertenece «ingredient»?", "Cocina", "Es un componente de una receta."),
    ],
    task("Un adulto lee dos veces este texto: «In the school garden, we plant tomatoes and lettuce. We water the plants every morning. We use a small shovel and a big bucket. In summer, we collect the vegetables and make a salad.» (garden = huerto, plant = plantar, lettuce = lechuga, water = regar, shovel = pala, bucket = balde, summer = verano, vegetables = verduras). Escribe el tema, cinco palabras clave del tema y un título para el texto.", "Tema: el huerto. Palabras: garden, tomatoes, lettuce, water, vegetables. Título: Nuestro huerto escolar.", ["indica un tema coherente", "anota cinco palabras del tema", "propone un título"], ["hoja con tema, palabras y título", "nota del adulto"], ["incluir palabras que no están en el texto", "no explicar el tema"], "Reconoce las palabras acertadas y vuelve a escuchar solo para encontrar las que se relacionan con plantar."),
    "Pide a un adulto que lea el texto del río y levanta la mano cada vez que oigas una palabra del tema medio ambiente.",
    "Escribe una lista de ocho palabras en inglés del tema deportes y cocina, cuatro de cada tema.",
)

# ------------------------------------------------------------------ clase 4
lesson(
    OA2, 4, "Un adulto que pronuncie cada palabra escrita en los ejercicios (si no tiene claro un sonido, usa los ejemplos de la explicación); lápiz.",
    "Aprenderé a distinguir los sonidos /z/ y /s/, el sonido /h/ al inicio de una palabra, y los sonidos /g/ y /dʒ/. Sirve para entender bien lo que se dice y no confundir palabras parecidas.",
    ["Sé que una letra puede sonar distinto en inglés y en español.", "Conozco palabras como zoo, hot, go y jacket."],
    [
        "El sonido /z/ de zoo es sonoro: si te tocas la garganta, vibra. El sonido /s/ de sad es sordo: no vibra. Esto importa en las terminaciones del plural. En dogs, bags, pens y days, la s final suena /z/, porque viene después de un sonido con voz. En cats, hats y cups, la s suena /s/, porque viene después de p, t o k, que no tienen voz. Si la palabra termina en s, sh, ch, x o z, se agrega -es y se oye una sílaba extra «iz»: bus-es, dish-es, watch-es.",
        "El sonido inicial /h/ de hot es un soplido suave, parecido a una j muy suave. Se oye en hat, hand, house y hungry. Pero hay palabras con h escrita que no se pronuncia: hour (hora) y honest (honesto) comienzan con vocal. Por eso hour no empieza con /h/ y hot sí.",
        "El sonido /g/ de go, ago y egg es como la g de «gato». El sonido /dʒ/ de jacket, general y age se parece a una «ch» con voz. Con frecuencia aparece cuando la g va antes de e, i o y, como en giraffe y gym, pero hay excepciones: gift y game llevan /g/. Fíjate siempre en cómo suena, no solo en cómo se escribe.",
    ],
    [("/z/ (zoo)", "sonido con voz; vibra la garganta"), ("/s/ (sad)", "sonido sin voz; no vibra"), ("/h/ (hot)", "soplido suave al inicio"), ("silent h (hour)", "h que no se pronuncia"), ("/g/ (go, egg)", "como la g de «gato»"), ("/dʒ/ (jacket, age)", "parecido a «ch» pero con voz"), ("-es (buses)", "plural con sílaba extra «iz»")],
    [
        ("h con sonido y h muda", "¿Cuál de estas palabras empieza con el sonido /h/: hour o hot?", ["Pienso en cómo se pronuncian.", "Hour se dice igual que «aur», sin soplido.", "Hot comienza con el soplido /h/."], "hot"),
        ("La s final de un plural", "¿Cómo suena la s final de bags: /z/ o /s/?", ["Miro el sonido anterior: g tiene voz.", "Después de un sonido con voz, la s suena /z/.", "Entonces bags termina con /z/."], "/z/"),
    ],
    [
        ("Creer que toda g escrita suena /dʒ/.", "Se aplica una pista de escritura como regla sin excepciones.", "Escucha cada palabra: gift y game llevan /g/."),
        ("Pronunciar la h de hour.", "Se sigue la escritura en lugar del sonido.", "Recuerda que hour y honest comienzan con vocal."),
    ],
    [
        ("¿Qué palabra empieza con el sonido /h/? a) hour b) hot", "b) hot", "En hot se oye el soplido; hour comienza con vocal."),
        ("¿Qué par de palabras tiene el sonido /dʒ/ en las dos? a) jacket y age b) go y egg", "a) jacket y age", "Jacket y age llevan /dʒ/; go y egg llevan /g/."),
        ("¿Qué palabra lleva el sonido /g/? a) go b) general", "a) go", "General comienza con /dʒ/."),
    ],
    [
        ("Un adulto dice zoo y sad. ¿Cuál de las dos empieza con el sonido /z/? a) zoo b) sad", "a) zoo", "Zoo comienza con /z/; sad comienza con /s/."),
        ("¿Cuántas de las palabras hour, hat, honest y hungry comienzan con el sonido /h/?", "2", "Solo hat y hungry; hour y honest comienzan con vocal."),
        ("¿Cómo suena la s final de cats: /z/ o /s/?", "/s/", "Viene después de t, que no tiene voz."),
    ],
    [
        ("¿Cuántas de las palabras general, go, egg, age, ago y jacket llevan el sonido /dʒ/?", "3", "General, age y jacket llevan /dʒ/; go, egg y ago llevan /g/."),
        ("¿Cuántas de las palabras giraffe, game, gym y gift llevan el sonido /dʒ/?", "2", "Giraffe y gym llevan /dʒ/; game y gift llevan /g/."),
        ("En buses y watches, ¿qué se oye al final de la palabra? a) una sílaba extra «iz» b) solo un sonido /s/", "a) una sílaba extra «iz»", "Después de s o ch el plural se escribe -es y suena como una sílaba más."),
    ],
    [
        ("Rosa dice que hour empieza con /h/ porque se escribe con h. ¿Tiene razón? Responde sí o no.", "No", "La h de hour no se pronuncia: se oye igual que «aur»."),
        ("¿Qué pista ayuda más a distinguir ago de age? a) cómo suena la g b) cuántas letras tienen", "a) cómo suena la g", "Ago lleva /g/ y age lleva /dʒ/, aunque se escriban con la misma letra."),
    ],
    [
        ("En la lista dogs, cats, pens, hats, days y bags, ¿en cuántas palabras la s final suena /z/?", "4", "Dogs, pens, days y bags terminan con /z/; cats y hats terminan con /s/."),
        ("En la lista horse, house, hour y hand, ¿cuántas palabras comienzan con el sonido /h/?", "3", "Horse, house y hand llevan /h/; hour comienza con vocal."),
    ],
    [("Una compañera lee: «My jacket is huge, and the zoo gift shop sells a green giraffe.» (huge = enorme, gift shop = tienda de regalos, sells = vende, green = verde). ¿Cuántas palabras tienen el sonido /dʒ/?", "3", "Jacket, huge y giraffe tienen /dʒ/; gift y green tienen /g/.")],
    [
        ("¿Cómo suena la s final de pens?", "/z/", "Viene después de n, que tiene voz."),
        ("¿Qué sonido tiene la g de gift?", "/g/", "Gift comienza con /g/, no con /dʒ/."),
        ("En Inglés de 7.º (OA 2, clase 4): ¿Se pronuncia la h de honest?", "No", "Honest comienza con vocal."),
    ],
    task("Pide a un adulto que pronuncie estas palabras en voz alta, una por una: zoo, sad, hot, hour, go, age. Escribe en tu hoja el sonido inicial de cada una (/z/, /s/, /h/, vocal, /g/ o /dʒ/) y di en voz alta una palabra nueva con cada sonido.", "zoo = /z/; sad = /s/; hot = /h/; hour = vocal; go = /g/; age = /dʒ/. Palabras nuevas: zebra, soup, hat, honest, game, jam.", ["anota el sonido inicial de las seis palabras", "no se guía solo por la escritura", "da una palabra nueva por sonido"], ["hoja con seis sonidos", "nota del adulto"], ["decir que hour comienza con /h/", "decir que age comienza con /g/"], "Reconoce los sonidos acertados y repasa con la persona adulta las palabras donde la escritura y el sonido no coinciden."),
    "Practica con una persona de tu casa decir en voz alta pares como zoo-sad y go-jacket, y comprueba si notas la diferencia.",
    "Escribe en tu hoja dos listas con tres palabras cada una: una con sonido /g/ y otra con sonido /dʒ/.",
)

# ------------------------------------------------------------------ clase 5
lesson(
    OA2, 5, MAT,
    "Aprenderé a combinar pistas (expresiones frecuentes, conectores, vocabulario temático y sonidos) para reconstruir el significado de un texto oral. Sirve para entender aunque aparezcan palabras desconocidas.",
    ["Sé reconocer conectores como first, next y finally.", "Sé usar el tema para deducir palabras nuevas."],
    [
        "Para reconstruir el significado combina todas las pistas disponibles. Las palabras clave te dicen el tema. Los conectores muestran el orden y las razones. Las expresiones frecuentes, como Excuse me o See you later, indican la función del mensaje. Los sonidos ayudan a distinguir palabras parecidas, como sip y zip, o age y ago.",
        "Si aparece una palabra desconocida, no te detengas. Pregúntate: ¿qué palabras la rodean?, ¿de qué tema habla el texto? y ¿qué conector aparece? Por ejemplo, en «he sat in the shade because the sun was strong», because indica una razón: sentarse a la sombra se relaciona con el sol fuerte. Entonces shade es el lugar protegido del sol.",
        "Después de deducir, comprueba. Vuelve a unir la idea con las otras frases: ¿tiene sentido en el orden de los hechos? ¿Calza con el tema? Si una pista contradice tu idea, cámbiala. Este ciclo de predecir, comprobar y corregir es lo que hace un oyente seguro.",
    ],
    [("clue", "pista"), ("context", "contexto: lo que rodea a una palabra"), ("deduce", "deducir: sacar una idea con pistas"), ("shade", "sombra"), ("gift", "regalo"), ("check", "comprobar")],
    [
        ("Deducir con una razón", ADULT + SHADE + " ¿Qué significa shade?", ["Hay una razón: because the sun was strong.", "Mario se sienta en el shade of a tall tree para no tener sol.", "Shade es sombra."], "Sombra: lugar protegido del sol"),
        ("Ordenar con conectores", ADULT + ZOO + " ¿Qué hace Hugo justo después de ver la jirafa?", ["Busco la jirafa: When we arrive, we see a giraffe.", "El siguiente conector es Next.", "Next, we have lunch."], "Almuerza"),
    ],
    [
        ("Detenerse en una palabra desconocida y perder el resto del texto.", "Se intenta traducir todo y se pierde la idea.", "Usa las palabras que la rodean y sigue escuchando."),
        ("Dar una deducción sin comprobarla con el resto del texto.", "Una pista aislada puede engañar.", "Comprueba que tu idea calce con el orden y el tema."),
    ],
    [
        (ADULT + ZOO + " ¿Qué hace Hugo primero? a) va al zoológico b) compra un regalo", "a) va al zoológico", "Dice First, I go to the zoo."),
        (ADULT + ZOO + " ¿Qué palabra de la historia comienza con el sonido /dʒ/? a) giraffe b) gift", "a) giraffe", "Giraffe comienza con /dʒ/; gift comienza con /g/."),
        (ADULT + ZOO + " ¿Qué conector marca el último paso? a) finally b) first", "a) finally", "Finally significa finalmente."),
    ],
    [
        (ADULT + SHADE + " ¿Cuál es el significado más probable de shade? a) lugar protegido del sol b) vaso grande c) tipo de árbol", "a) lugar protegido del sol", "Aparece con tall tree y sun was strong."),
        (ADULT + SHADE + " ¿Por qué Mario se sienta a la sombra? a) porque el sol estaba fuerte b) porque tenía sed", "a) porque el sol estaba fuerte", "Dice because the sun was strong."),
        (ADULT + ZOO + " ¿Qué compran después del almuerzo?", "Un regalo", "Dice After that, we buy a small gift."),
    ],
    [
        (ADULT + ZOO + " Ordena. A) Comen. B) Ven una jirafa. C) Compran un regalo.", "B, A, C", "Primero llegan y ven la jirafa, luego almuerzan y después compran el regalo."),
        (ADULT + ZOO + " Hugo dice a su abuelo: «Excuse me, can I have a snack?» (snack = colación). ¿Qué función cumple Excuse me? a) pedir atención con cortesía b) despedirse", "a) pedir atención con cortesía", "Es una forma amable de comenzar un pedido."),
        (ADULT + ZOO + " ¿Cuántas de las palabras zoo, giraffe, eggs y gift llevan el sonido /g/?", "2", "Eggs y gift llevan /g/; zoo lleva /z/ y giraffe lleva /dʒ/."),
    ],
    [
        (ADULT + SHADE + " ¿Qué palabra muestra la causa de que Mario tome agua? a) thirsty b) strong", "a) thirsty", "Thirsty es con sed, y por eso bebe."),
        ("Pía dice que After that significa «antes de eso». ¿Tiene razón? Responde sí o no.", "No", "After significa después; la frase significa «después de eso»."),
    ],
    [
        ("Oyes first, bowl y mix. ¿Qué tipo de texto es? a) una receta b) un partido", "a) una receta", "Son palabras de cocina y de pasos."),
        (ADULT + ZOO + " Hugo y su abuelo almuerzan sándwiches y huevos. ¿Qué conector del texto muestra que lo hacen después de ver la jirafa? a) Next b) Finally", "a) Next", "Next, we have lunch viene justo después de ver la jirafa; Finally cierra el día en casa."),
    ],
    [(ADULT + "En la estación se oye: «Attention! The train to Valparaíso leaves in ten minutes, so please go to platform three.» (train = tren, leaves = sale, platform = andén). ¿Qué debes hacer?", "Ir al andén tres", "So marca la consecuencia: como el tren sale pronto, hay que ir al andén.")],
    [
        ("En Inglés de 7.º (OA 2, clase 5): ¿Qué haces con una palabra desconocida?", "Uso las pistas de las palabras que la rodean", "El contexto ayuda a deducir su significado."),
        ("¿Qué hace un oyente seguro después de deducir?", "Comprobar su idea con el resto del texto", "Si una pista no calza, la corrige."),
        ("¿Qué conector marca una razón?", "Because", "Se escribe antes de la razón."),
    ],
    task("Un adulto lee dos veces este texto: «Hello! Today I tell you my morning routine. First, I wake up at seven. Next, I have bread and juice. After that, I walk to school with my cousin. I always say See you later to my neighbor.» (wake up = despertar, cousin = primo, neighbor = vecino). Escribe en tu hoja el orden de tres hechos, el chunk que oíste y su significado.", "Despierta a las 7; toma pan y jugo; camina al colegio con su primo. Chunk: See you later = hasta luego.", ["ordena tres hechos con los conectores", "identifica el chunk", "explica su significado"], ["hoja con tres hechos y un chunk", "nota del adulto"], ["poner el desayuno antes de despertar", "traducir See you later palabra por palabra"], "Reconoce los hechos acertados y repasa con la persona adulta el orden con first, next y after that."),
    "Pide a un adulto que lea otra vez la historia del zoológico y levanta la mano cuando oigas una palabra con sonido /dʒ/.",
    "Escribe cuatro frases en inglés que cuenten tu fin de semana usando first, next, finally y because.",
)

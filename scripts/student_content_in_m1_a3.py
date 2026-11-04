"""Cuaderno del estudiante, 1.º medio Inglés (oficial), IN1M OA 03: propósito, ideas relevantes, detalle, contraste y problema-solución al escuchar.

Las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado. Los textos son originales y llevan pista en español.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA = "IN1M OA 03"
ADULT = "Un adulto lee en voz alta (tapa el guion): "
MAT_L = "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz."


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


# ------------------------------------------------------------------ clase 1: propósito, tema e ideas relevantes
W_BEE = "«Good afternoon. Today I would like to explain how bees make honey. Bees collect nectar from flowers and carry it to the hive. There they change it with special substances. Then they store it in small wax cells.» (bees = abejas, honey = miel, nectar = néctar, hive = colmena, substances = sustancias, store = guardan, wax cells = celdas de cera)"
W_POWER = "«Is your phone always out of battery? Our power bank charges your phone three times! Buy one this week and get a free cable.» (battery = batería, power bank = batería portátil, charges = carga, free = gratis, cable = cable)"
TREES = "«Hello, everyone. In my talk I will explain why cities plant trees along the streets. Trees give shade, clean the air a little and make streets calmer. They also give homes to birds. So I believe every neighbourhood needs more trees.» (shade = sombra, clean = limpian, calmer = más tranquilas, birds = aves, neighbourhood = barrio, I believe = creo)"
PROJ = "«Lucas: We need to choose a topic for the science project. Emma: What about solar energy? Lucas: Good idea, but we need a model. Emma: We can build a small one with cardboard and foil. Lucas: Great, let's start on Monday.» (topic = tema, solar energy = energía solar, model = maqueta, cardboard = cartón, foil = papel de aluminio)"
BOOKS = "«Do you have old books at home? Bring them to the school library next week. We will send them to a rural school that needs books. Every book makes a difference.» (old = viejos, bring = trae, rural = rural, needs = necesita, makes a difference = hace una diferencia)"
SQUARE = "«The city council announced that the main square will be closed on Sunday for a cleaning day. Volunteers will paint benches and plant flowers. Cars cannot enter the square from eight to four.» (city council = municipalidad, announced = anunció, square = plaza, benches = bancas, plant = plantar, enter = entrar)"
TURTLE = "«Today I want to tell you about my pet turtle. She is twelve years old, eats lettuce and sleeps under a lamp. Turtles can live a very long time, so I have to take care of her for many years.» (turtle = tortuga, lettuce = lechuga, lamp = lámpara, live = vivir, take care of = cuidar)"
UNIFORM = "«Good morning, students. Tomorrow is Free Colours Day. Wear your favourite colours and bring one thousand pesos for the class trip fund.» (free colours day = día de colores libres, wear = usa, favourite = favoritos, fund = fondo)"

lesson(
    OA, 1, MAT_L,
    "Aprenderé a identificar el propósito, el tema y las ideas relevantes de un texto que escucho. Sirve para decidir qué es lo central y qué es solo un detalle.",
    ["Sé reconocer el formato de un texto oral.", "Conozco palabras como explain, topic e idea."],
    [
        "Cuando escuchas, lo primero que debes decidir es para qué se habla. El propósito (purpose) puede ser explicar, convencer, informar, invitar o contar. El tema (topic) es de qué trata el texto, y se dice con pocas palabras: how bees make honey, trees in the streets. Una pista del propósito son frases como I would like to explain, I believe o Bring them.",
        "Las ideas relevantes (relevant ideas) son las que sostienen el tema y sin las cuales el texto cambia. En el texto de las abejas, collect nectar, change it y store it son relevantes. En cambio, un detalle como el color de la caja sería secundario. Para encontrarlas, pregúntate: si saco esta idea, ¿se entiende lo central?",
        "Si el texto trata un tema que no conoces mucho, no te detengas en palabras nuevas. Fíjate en las repetidas, en la entonación y en palabras de apoyo como so, because y first. Termina siempre con una frase en español: El texto trata de... y sirve para... Así compruebas que entendiste lo importante.",
    ],
    [("purpose", "propósito: para qué se habla"), ("topic", "tema: de qué trata"), ("relevant idea", "idea relevante: la que sostiene el tema"), ("detail", "detalle: dato secundario"), ("I believe...", "creo que... (opinión)"), ("announce", "anunciar")],
    [
        ("Propósito y tema de una explicación", ADULT + W_BEE + " ¿Cuál es el tema y el propósito?", ["La frase I would like to explain avisa el propósito: explicar.", "El tema está en how bees make honey.", "Las ideas relevantes son los pasos: recolectar, cambiar y guardar."], "Tema: cómo las abejas hacen miel. Propósito: explicar"),
        ("Propósito de un aviso", ADULT + W_POWER + " ¿Cuál es el propósito y qué ofrece?", ["Hace una pregunta al oyente y le pide comprar.", "Ofrece un cable gratis esta semana.", "El propósito es convencer de comprar la batería portátil."], "Convencer de comprar; ofrece un cable gratis"),
    ],
    [
        ("Confundir un detalle con la idea principal.", "El oyente recuerda el dato más llamativo, no el que sostiene el tema.", "Pregunta si sin esa idea el texto cambia de tema."),
        ("Decidir el propósito solo por una palabra, como free.", "Se mira una palabra y no todo el texto.", "Mira las órdenes y preguntas de todo el mensaje."),
    ],
    [
        (ADULT + TREES + " ¿Cuál es el tema? A) por qué se plantan árboles en las calles B) cómo se pintan las bancas", "A) por qué se plantan árboles en las calles", "La frase why cities plant trees along the streets anuncia el tema."),
        (ADULT + BOOKS + " ¿Cuál es el propósito? A) invitar a donar libros B) vender libros usados", "A) invitar a donar libros", "Dice Bring them to the school library para enviarlos a una escuela rural."),
        (ADULT + PROJ + " ¿Quiénes hablan y de qué? A) dos estudiantes que planifican un proyecto de ciencias B) dos estudiantes que discuten la fecha de entrega", "A) dos estudiantes que planifican un proyecto de ciencias", "Se turnan para decidir el tema y la maqueta."),
    ],
    [
        (ADULT + TREES + " ¿Cuál de estas ideas es relevante para el tema? A) los árboles dan sombra y hogar a las aves B) los autos hacen ruido en las calles", "A) los árboles dan sombra y hogar a las aves", "Son razones que apoyan por qué se plantan árboles."),
        (ADULT + SQUARE + " ¿Cuál es el propósito? A) informar un cambio de uso de la plaza B) contar una anécdota", "A) informar un cambio de uso de la plaza", "Anuncia que el domingo la plaza estará cerrada a los autos."),
        (ADULT + PROJ + " ¿Qué idea es relevante para el plan? A) construir una maqueta pequeña con cartón y papel de aluminio B) que el proyecto será sobre energía eólica", "A) construir una maqueta pequeña con cartón y papel de aluminio", "Es lo que acuerdan para el proyecto sobre energía solar."),
    ],
    [
        (ADULT + TREES + " ¿Cuál es el propósito principal? A) explicar y convencer B) informar un cambio de la municipalidad", "A) explicar y convencer", "Explica razones y termina con So I believe every neighbourhood needs more trees."),
        (ADULT + SQUARE + " ¿Qué dos ideas son relevantes para alguien que quiere ir en auto el domingo? A) la plaza está cerrada a los autos y es de ocho a cuatro B) los voluntarios plantan flores", "A) la plaza está cerrada a los autos y es de ocho a cuatro", "Son las restricciones que cambian lo que esa persona puede hacer."),
        (ADULT + BOOKS + " ¿Cuál sería un buen título? A) Dona tus libros viejos B) Una biblioteca nueva para la escuela rural", "A) Dona tus libros viejos", "Resume el propósito y el tema."),
    ],
    [
        (ADULT + BOOKS + " Un compañero dice que la idea principal es que la biblioteca está vieja. ¿Qué respondes? A) no: la idea principal es donar libros para una escuela rural B) sí: la biblioteca es lo central", "A) no: la idea principal es donar libros para una escuela rural", "La biblioteca es solo el lugar de entrega."),
        (ADULT + SQUARE + " Un compañero dice que el propósito es convencer de comprar algo. ¿Qué respondes? A) no: informa un cierre y una actividad de limpieza B) sí: dice comprar", "A) no: informa un cierre y una actividad de limpieza", "No hay órdenes de compra ni promesas: solo información."),
    ],
    [
        (ADULT + TURTLE + " ¿Cuál es el tema? A) su tortuga mascota y los cuidados que necesita B) cuánto viven las tortugas en la naturaleza", "A) su tortuga mascota y los cuidados que necesita", "Cuenta qué come, dónde duerme y por qué debe cuidarla."),
        (ADULT + TURTLE + " ¿Qué idea es un detalle y no la idea central? A) tiene doce años B) hay que cuidarla por muchos años", "A) tiene doce años", "La edad es un dato; la razón de cuidarla muchos años sostiene el mensaje final."),
    ],
    [(ADULT + UNIFORM + " ¿Cuál es el propósito? A) avisar una actividad y pedir un aporte en dinero B) pedir que todos usen el uniforme", "A) avisar una actividad y pedir un aporte en dinero", "Anuncia el día de colores libres y pide mil pesos para el paseo.")],
    [
        ("En Inglés de 1.º medio (OA 3, clase 1): ¿qué es el propósito de un texto oral?", "La razón por la que se habla, como explicar, convencer o invitar", "Responde para qué se dice."),
        ("En Inglés de 1.º medio (OA 3, clase 1): ¿cómo reconoces una idea relevante?", "Es la que sostiene el tema: si se saca, el texto cambia", "No es un detalle secundario."),
        ("En Inglés de 1.º medio (OA 3, clase 1): ¿qué es el tema de un texto?", "De qué trata, dicho en pocas palabras", "Se resume en una frase corta."),
    ],
    task("Un adulto lee dos veces este texto: «Hello, everyone. Today I want to explain why we should drink more water. Water helps us concentrate and keeps us active. Please carry a bottle to school every day.» (concentrate = concentrarse, active = activos, carry = lleva, bottle = botella). Escribe en español el tema, el propósito y dos ideas relevantes.", "Tema: por qué conviene tomar más agua. Propósito: explicar y convencer. Ideas relevantes: ayuda a concentrarse y mantiene activos.", ["escribe el tema en una frase", "indica el propósito con una palabra clara", "anota dos ideas relevantes"], ["hoja con tres respuestas", "nota del adulto"], ["anotar la botella como idea central", "decir que solo cuenta una anécdota"], "Reconoce lo logrado y, si anotó un detalle, pregunta si sin él se entiende igual el tema."),
    "Escucha otra vez el texto de los árboles y escribe en una frase el tema y, en otra, el propósito.",
    "Elige un anuncio que hayas visto o escuchado y escribe su tema y su propósito en dos frases en español.",
)

# ------------------------------------------------------------------ clase 2: información específica y detalles clave
W_GOAL = "«Tomás is the goalkeeper. He stopped three shots in the first half. His teammate Ingrid scored the winning goal in the last minute.» (goalkeeper = arquero, stopped = detuvo, shots = tiros, first half = primer tiempo, teammate = compañera de equipo, scored = anotó, winning goal = gol del triunfo)"
W_LANE = "«I think the new bike lane is useful, but my neighbour Mr Díaz says it is too narrow.» (bike lane = ciclovía, useful = útil, neighbour = vecino, narrow = angosta)"
POOL = "«Hello, this is Nora from the sports centre. The swimming pool opens at seven in the morning and closes at nine at night. On Sundays, it closes at two. The new gym is on the second floor.» (swimming pool = piscina, opens = abre, closes = cierra, gym = gimnasio, floor = piso)"
CANTEEN = "«Interviewer: What do you think of the new school canteen? Pablo: I like it. The food is fresh and the prices are fair. Valeria: I'm not sure. The queue is very long at lunch.» (canteen = casino, fresh = fresca, prices = precios, fair = justos, queue = fila)"
TABLET = "«Carla called the repair shop on Tuesday because her tablet screen was cracked. The technician said the repair costs twenty thousand pesos and takes three days. Carla decided to wait until Friday.» (repair shop = taller de reparación, screen = pantalla, cracked = quebrada, technician = técnico, repair = reparación, wait = esperar)"
GARDEN = "«Welcome to the botanical garden. Please do not pick the flowers. The cactus house is on your left; the rose garden is straight ahead. The next tour starts at half past three, and Mrs Silva will lead it.» (botanical garden = jardín botánico, pick = cortar, cactus house = invernadero de cactus, left = izquierda, straight ahead = al frente, lead = guiar)"
CLINIC = "«Hello, this is the clinic. Your appointment is now on Thursday at four. Please arrive ten minutes early.» (clinic = consultorio, appointment = hora médica, arrive = llegar, early = antes de tiempo)"

lesson(
    OA, 2, MAT_L,
    "Aprenderé a ubicar información específica al escuchar: quién hace qué, dónde, cuándo y qué opina cada hablante. Sirve para responder con precisión sin mezclar datos.",
    ["Sé reconocer el propósito y el tema de un texto.", "Conozco las preguntas who, what, where y when."],
    [
        "La información específica (specific information) son los datos concretos que responden una pregunta. Se asocian a personas (who), acciones (what), lugares (where), tiempo (when) y opiniones (what do they think). Antes de escuchar, lee la pregunta y decide cuál de esas categorías necesitas. Eso te ayuda a anotar solo lo que sirve.",
        "Los detalles clave (key details) cambian si cambia la persona o la situación. En un texto con dos hablantes, anota el nombre junto a cada dato. En I like it y I'm not sure, quien habla importa: la opinión no es de la misma persona. También cambian los días: on Sundays, it closes at two es distinto del horario normal.",
        "Las opiniones se reconocen con verbos como I think, I like, I'm not sure y con adjetivos como useful, fair o narrow. Si dos personas opinan distinto, no las mezcles. Responde con el dato exacto y comprueba que corresponde a la persona y al momento que pide la pregunta.",
    ],
    [("who / what / where / when", "quién / qué / dónde / cuándo"), ("detail", "detalle"), ("opinion", "opinión: lo que alguien piensa"), ("I think / I'm not sure", "creo / no estoy seguro"), ("early", "con anticipación"), ("technician", "técnico")],
    [
        ("Ubicar persona y acción", ADULT + W_GOAL + " ¿Quién anotó el gol del triunfo y cuántos tiros detuvo Tomás?", ["Busco who: scored the winning goal.", "Esa persona es Ingrid.", "Tomás stopped three shots."], "Ingrid anotó el gol; Tomás detuvo tres tiros"),
        ("Ubicar una opinión", ADULT + W_LANE + " ¿Quién cree que la ciclovía es útil y quién dice que es angosta?", ["I think... indica la opinión del que habla.", "El que habla cree que es útil.", "El señor Díaz dice que es angosta."], "El que habla cree que es útil; el señor Díaz, que es angosta"),
    ],
    [
        ("Mezclar la opinión de dos personas.", "Se anota un adjetivo sin ver quién lo dijo.", "Escribe el nombre del hablante junto a cada opinión."),
        ("Usar el horario normal cuando se pregunta por un día especial.", "Se recuerda el primer dato oído y no el que corresponde al día.", "Busca la marca del día, como on Sundays."),
    ],
    [
        (ADULT + POOL + " ¿A qué hora abre la piscina? A) a las siete de la mañana B) a las nueve de la noche", "A) a las siete de la mañana", "Dice opens at seven in the morning."),
        (ADULT + CANTEEN + " ¿Quién cree que los precios son justos? A) Pablo B) Valeria", "A) Pablo", "Pablo dice the prices are fair."),
        (ADULT + TABLET + " ¿Qué le pasaba a la tablet de Carla? A) tenía la pantalla quebrada B) no tenía batería", "A) tenía la pantalla quebrada", "Dice her tablet screen was cracked."),
    ],
    [
        (ADULT + POOL + " ¿A qué hora cierra la piscina los domingos? A) a las dos B) a las nueve", "A) a las dos", "Dice On Sundays, it closes at two."),
        (ADULT + GARDEN + " ¿Dónde queda el rosedal? A) al frente B) a la izquierda", "A) al frente", "Dice the rose garden is straight ahead; la izquierda es el invernadero de cactus."),
        (ADULT + CLINIC + " ¿Qué día cambió la hora médica? A) al jueves B) al martes", "A) al jueves", "Dice now on Thursday at four."),
    ],
    [
        arith(ADULT + TABLET + " Si Carla repara dos tablets iguales, ¿cuántos pesos paga?", "2*20000", "Cada reparación cuesta 20.000 pesos.", " pesos"),
        (ADULT + GARDEN + " ¿Quién guiará el próximo recorrido? A) la señora Silva B) el guardia", "A) la señora Silva", "Dice Mrs Silva will lead it."),
        (ADULT + CANTEEN + " ¿Cuál es el problema que menciona Valeria? A) la fila es muy larga a la hora de almuerzo B) la comida está fría", "A) la fila es muy larga a la hora de almuerzo", "Dice the queue is very long at lunch."),
    ],
    [
        (ADULT + POOL + " Un compañero dice que los domingos la piscina cierra a las nueve. ¿Qué le respondes? A) no: los domingos cierra a las dos B) sí: siempre cierra a las nueve", "A) no: los domingos cierra a las dos", "El horario de los domingos es distinto del habitual."),
        (ADULT + CANTEEN + " Un compañero dice que a Valeria le gusta el casino. ¿Es correcto? A) no: ella no está segura y critica la fila B) sí: dice que la comida es fresca", "A) no: ella no está segura y critica la fila", "La frase de la comida fresca es de Pablo."),
    ],
    [
        (ADULT + GARDEN + " ¿A qué hora empieza el próximo recorrido? A) a las tres y media B) a las cuatro", "A) a las tres y media", "Half past three significa 3:30."),
        (ADULT + TABLET + " ¿Cuántos días demora la reparación y hasta qué día decide esperar Carla? A) tres días y hasta el viernes B) tres días y hasta el martes", "A) tres días y hasta el viernes", "La reparación demora three days y Carla decide wait until Friday."),
    ],
    [(ADULT + CLINIC + " ¿A qué hora debes llegar? A) a las 3:50 B) a las 4:10", "A) a las 3:50", "Llegar diez minutos antes de las cuatro es 3:50.")],
    [
        ("En Inglés de 1.º medio (OA 3, clase 2): ¿qué pregunta busca un lugar?", "Where", "Where pregunta por el lugar."),
        ("En Inglés de 1.º medio (OA 3, clase 2): ¿qué hay que anotar junto a una opinión?", "El nombre de quien la dice", "Así no se mezclan las opiniones."),
        ("En Inglés de 1.º medio (OA 3, clase 2): ¿qué significa half past three?", "Tres y media (3:30)", "Half past es y media."),
    ],
    task("Un adulto lee dos veces este mensaje: «Hi, this is Rosa from the community centre. The photography workshop is on Wednesday at five in room two. I think it is useful for beginners, but my friend Luis says it is a little short. It costs three thousand pesos.» (community centre = centro comunitario, photography = fotografía, beginners = principiantes, short = corto, costs = cuesta). Anota día, hora, sala, precio y qué opina cada persona.", "Miércoles, a las 5, sala 2, 3.000 pesos. Rosa piensa que es útil para principiantes; Luis dice que es un poco corto.", ["anota los cuatro datos exactos", "atribuye cada opinión a la persona correcta", "no mezcla datos de otra hora o sala"], ["hoja con los datos", "nota del adulto"], ["atribuir a Rosa la opinión de Luis", "anotar room two como las dos de la tarde"], "Reconoce los datos exactos y, si mezcló opiniones, relee quién dijo I think y quién dijo my friend says."),
    "Escucha otra vez el texto de la piscina y completa una tabla con día, hora y piso.",
    "Pide a una persona de tu casa que te diga una opinión sobre un lugar y anota quién la dice y qué dato la apoya.",
)

# ------------------------------------------------------------------ clase 3: relaciones de contraste
W_CYCLE = "«Cycling is cheap and healthy. However, it can be dangerous without a helmet.» (cycling = andar en bicicleta, cheap = barato, healthy = saludable, dangerous = peligroso, helmet = casco)"
W_SEAS = "«Ana likes summer, while her brother prefers winter.» (summer = verano, while = mientras que, prefers = prefiere, winter = invierno)"
BUS = "«The old bus was slow and noisy. The new bus is quiet and fast, but it costs more.» (noisy = ruidoso, quiet = silencioso, fast = rápido, costs more = cuesta más)"
CLASSES = "«Online classes are flexible. On the other hand, students can feel alone. Face-to-face classes are good for making friends, although they need travel time.» (online = en línea, flexible = flexibles, on the other hand = por otro lado, alone = solos, face-to-face = presenciales, travel time = tiempo de viaje)"
FOOD = "«My cousin Leo loves spicy food, while I can only eat mild flavours. Instead of ordering the hot sauce, we shared a mild soup.» (spicy = picante, mild = suave, flavours = sabores, ordering = pedir, sauce = salsa, shared = compartimos, soup = sopa)"
FORECAST = "«The weather forecast said it would be sunny. However, in the afternoon, dark clouds arrived, and it rained. Instead of the picnic, we ate at home.» (forecast = pronóstico, sunny = soleado, clouds = nubes, rained = llovió, picnic = picnic)"
SHOES = "«These shoes are comfortable, but they are expensive. Those shoes are cheaper, but they are not comfortable.» (shoes = zapatos, comfortable = cómodos, expensive = caros, cheaper = más baratos)"

lesson(
    OA, 3, MAT_L,
    "Aprenderé a reconocer cuándo un texto oral contrasta dos ideas, con palabras como but, however, while, although, on the other hand e instead. Sirve para entender qué se compara y qué se opone.",
    ["Conozco las palabras but y although.", "Sé reconocer ideas principales y detalles."],
    [
        "Un contraste (contrast) muestra una diferencia o una oposición entre dos ideas. En inglés se señala con palabras específicas. But significa pero: The new bus is fast, but it costs more. However significa sin embargo y suele ir al inicio de una oración nueva, con una pausa. On the other hand significa por otro lado y presenta el otro lado de un tema.",
        "While puede significar mientras que y compara a dos personas o cosas: Ana likes summer, while her brother prefers winter. Although significa aunque y muestra una dificultad que no impide algo. Instead of significa en lugar de: señala lo que se cambió por otra cosa. Al escuchar, anota las dos partes: qué se dice antes de la marca y qué se dice después.",
        "El contraste ayuda a ver el punto de vista del hablante. Si dice A is cheap, but B is strong, la persona valora ambas cosas y compara. Fíjate en la pausa y en la entonación: después de However suele haber una pausa corta. Ante una pregunta, busca qué marca de contraste hay y qué ideas se oponen.",
    ],
    [("but / however", "pero / sin embargo"), ("while", "mientras que (compara)"), ("although", "aunque"), ("on the other hand", "por otro lado"), ("instead of", "en lugar de"), ("contrast", "contraste: diferencia u oposición")],
    [
        ("Reconocer however", ADULT + W_CYCLE + " ¿Qué contraste hay y qué palabra lo señala?", ["Primero se dicen ventajas: barato y saludable.", "However introduce lo opuesto: puede ser peligroso sin casco.", "El contraste es entre ventajas y riesgo."], "Ventajas frente a riesgo; lo señala However"),
        ("Reconocer while", ADULT + W_SEAS + " ¿Qué se compara con while?", ["While une dos personas con gustos distintos.", "Ana prefiere el verano.", "Su hermano prefiere el invierno."], "Los gustos de Ana (verano) y de su hermano (invierno)"),
    ],
    [
        ("Pensar que however significa porque.", "Se confunde un contraste con una causa.", "However es sin embargo: introduce algo opuesto."),
        ("Anotar solo una de las dos ideas del contraste.", "Se atiende a la primera parte y se pierde la que sigue a la marca.", "Anota qué se dijo antes y después de la marca."),
    ],
    [
        (ADULT + BUS + " ¿Qué es mejor en el bus nuevo? A) es silencioso y rápido B) cuesta menos", "A) es silencioso y rápido", "Dice quiet and fast; cuesta más."),
        (ADULT + BUS + " ¿Qué palabra señala el contraste? A) but B) and", "A) but", "But une lo bueno (rápido) con la desventaja (cuesta más)."),
        (ADULT + FOOD + " ¿Qué prefiere el narrador? A) sabores suaves B) comida picante", "A) sabores suaves", "Dice I can only eat mild flavours."),
    ],
    [
        (ADULT + CLASSES + " ¿Cuál es una ventaja de las clases en línea? A) son flexibles B) permiten hacer amigos más fácilmente", "A) son flexibles", "Dice Online classes are flexible."),
        (ADULT + CLASSES + " ¿Qué contraste hay con las clases presenciales? A) sirven para hacer amigos, aunque requieren tiempo de viaje B) son flexibles, aunque requieren tiempo de viaje", "A) sirven para hacer amigos, aunque requieren tiempo de viaje", "Although marca la desventaja de viajar."),
        (ADULT + FORECAST + " ¿Qué dijo el pronóstico y qué ocurrió? A) soleado, pero llovió B) lluvia, pero salió el sol", "A) soleado, pero llovió", "However marca el cambio entre lo esperado y lo ocurrido."),
    ],
    [
        (ADULT + FOOD + " ¿En lugar de qué compartieron una sopa suave? A) de pedir la salsa picante B) de pedir otra sopa", "A) de pedir la salsa picante", "Instead of ordering the hot sauce."),
        (ADULT + FORECAST + " ¿Qué hicieron en lugar del picnic? A) comieron en casa B) comieron en un restaurante", "A) comieron en casa", "Dice Instead of the picnic, we ate at home."),
        (ADULT + FOOD + " ¿Qué palabra compara los gustos de Leo y del narrador? A) while B) instead", "A) while", "While une dos preferencias distintas: picante y suave."),
    ],
    [
        (ADULT + SHOES + " ¿Qué ventaja tienen los zapatos caros? A) son cómodos B) son más baratos", "A) son cómodos", "Los zapatos baratos son los que no son cómodos; los caros sí."),
        (ADULT + CLASSES + " Una persona dice que las clases en línea son perfectas y no tienen desventajas. ¿Qué dato la contradice? A) On the other hand, students can feel alone B) Online classes are flexible", "A) On the other hand, students can feel alone", "Presenta el otro lado: el estudiante puede sentirse solo."),
    ],
    [
        (ADULT + SHOES + " Un amigo dice que los zapatos baratos son mejores en todo. ¿Qué dato lo contradice? A) no son cómodos B) cuestan menos", "A) no son cómodos", "Dice they are not comfortable; que cuesten menos es una ventaja."),
        (ADULT + "«Maya wanted a pet dog. However, her flat is small, so she adopted a cat instead of a dog. Although the cat is calm, Maya still dreams about a dog.» (pet = mascota, flat = departamento, small = pequeño, adopted = adoptó, calm = tranquilo, dreams about = sueña con). ¿Qué adoptó en lugar de un perro y por qué? A) un gato, porque su departamento es pequeño B) un conejo, porque es más barato", "A) un gato, porque su departamento es pequeño", "Instead of a dog significa en lugar de un perro; la razón sigue a so: her flat is small."),
    ],
    [(ADULT + "«I wanted to buy the blue jacket, but it was too big. The red one was smaller, so I bought it.» (jacket = chaqueta, too big = demasiado grande, smaller = más pequeña). ¿Por qué compró la roja? A) porque era más pequeña B) porque era azul", "A) porque era más pequeña", "La azul era demasiado grande; la roja, más pequeña.")],
    [
        ("En Inglés de 1.º medio (OA 3, clase 3): ¿qué significa however?", "Sin embargo", "Introduce una idea que contrasta con la anterior."),
        ("En Inglés de 1.º medio (OA 3, clase 3): ¿para qué sirve while entre dos personas?", "Para comparar sus diferencias: mientras que", "Opone dos gustos o acciones."),
        ("En Inglés de 1.º medio (OA 3, clase 3): ¿qué indica instead of?", "Que algo se cambió por otra cosa: en lugar de", "Señala lo que se reemplazó."),
    ],
    task("Un adulto lee dos veces este texto: «Living in the city is exciting. On the other hand, it can be noisy. My sister likes the city, while I prefer the countryside. Although the countryside is quiet, I sometimes miss my friends.» (exciting = emocionante, noisy = ruidoso, countryside = campo, quiet = tranquilo, miss = extraño). Escribe dos contrastes del texto y la palabra que señala cada uno.", "Contraste 1: ciudad emocionante, pero ruidosa; señala on the other hand. Contraste 2: la hermana prefiere la ciudad, el narrador el campo; señala while. (También: campo tranquilo, pero extraña a sus amigos; señala although.)", ["anota dos contrastes completos", "nombra la palabra que señala cada uno", "indica las dos ideas opuestas"], ["hoja con dos contrastes", "nota del adulto"], ["anotar solo una idea de cada contraste", "decir que while indica causa"], "Reconoce los contrastes bien ubicados y, si faltó una parte, pide que diga qué se dijo antes y después de la marca."),
    "Relee un texto de esta clase y subraya con un color cada palabra de contraste.",
    "Escribe en español dos frases tuyas con pero, mientras que y en lugar de, y piensa cuál sería su marca en inglés.",
)

# ------------------------------------------------------------------ clase 4: problema y solución (dos hablantes)
W_PATIO = "«The school patio floods when it rains. The caretaker cleaned the drain, and now the water goes away.» (patio = patio, floods = se inunda, caretaker = auxiliar, cleaned = limpió, drain = desagüe, goes away = se va)"
W_CHARGER = "«My phone battery died on the bus. Luckily, a classmate lent me a charger.» (died = se agotó, luckily = por suerte, lent = prestó, charger = cargador)"
SLEEP = "«Nico: I can't sleep early because I use my phone in bed. Mara: Why don't you leave it in another room? Nico: Good idea. I'll try tonight.» (sleep = dormir, early = temprano, bed = cama, leave = deja, another room = otra pieza, try = probar)"
TAP = "«Speaker A: Our community garden has no water because the tap is broken. Speaker B: We can ask the neighbours to donate barrels, and we can collect rainwater.» (community garden = huerto comunitario, tap = llave de agua, broken = rota, neighbours = vecinos, donate = donar, barrels = barriles, collect = recolectar, rainwater = agua de lluvia)"
LATE = "«Radio report: Many students arrive late because the bus stops far from school. The mayor's office decided to move the bus stop closer to the main gate.» (arrive = llegan, far = lejos, mayor's office = municipalidad, move = mover, closer = más cerca, gate = portón)"
MIRROR = "«Elena: I'm nervous about my English presentation. Teacher: Practise in front of a mirror and record yourself. Elena: I'll do that, thanks.» (nervous = nerviosa, presentation = presentación, practise = practica, mirror = espejo, record = grábate)"
HOT = "«Speaker A: The classroom is very hot in the afternoon. Speaker B: We could open the windows and use curtains to block the sun.» (hot = calurosa, afternoon = tarde, curtains = cortinas, block = bloquear, sun = sol)"

lesson(
    OA, 4, MAT_L,
    "Aprenderé a identificar un problema y su solución cuando las ideas vienen de dos hablantes o de un reportaje. Sirve para entender qué pasa, por qué pasa y qué se propone.",
    ["Sé reconocer causas con because y consecuencias con so.", "Conozco frases como Why don't you...?"],
    [
        "Una relación de problema y solución (problem-solution) aparece cuando alguien explica una dificultad y otra persona propone cómo resolverla. El problema se dice con frases como I can't..., has no..., is broken o is very hot. La causa aparece con because: I can't sleep early because I use my phone.",
        "La solución se reconoce por frases como Why don't you...?, We can..., The mayor's office decided to... o Practise in front of a mirror. Una buena solución resuelve la causa del problema, no solo lo menciona. Si el problema es que el bus para lejos, mover el paradero cerca de la puerta lo resuelve.",
        "Cuando hay una brecha de información, cada persona sabe solo una parte: una cuenta el problema y la otra propone la solución. Combina ambas y comprueba que calzan. Un orden útil para anotar es: problema, causa, solución y resultado. Así compruebas si el texto dice cómo terminó o solo propone una idea.",
    ],
    [("problem", "problema"), ("solution", "solución"), ("because", "porque (causa)"), ("Why don't you...?", "¿Por qué no...? (sugerencia)"), ("We can...", "podemos... (propuesta)"), ("decided to", "decidió")],
    [
        ("Ubicar problema y solución", ADULT + W_PATIO + " ¿Cuál es el problema y cómo se resolvió?", ["El problema es que el patio se inunda cuando llueve.", "La solución la hizo el auxiliar: limpió el desagüe.", "Ahora el agua se va."], "El patio se inundaba; el auxiliar limpió el desagüe"),
        ("Reconocer una solución prestada", ADULT + W_CHARGER + " ¿Cuál es el problema y la solución?", ["El problema es que se agotó la batería del teléfono.", "Un compañero prestó un cargador.", "Luckily marca una ayuda inesperada."], "Se agotó la batería; un compañero prestó un cargador"),
    ],
    [
        ("Anotar la solución sin comprobar si resuelve el problema.", "Se aceptan propuestas que no tienen relación con la causa.", "Pregúntate si la solución actúa sobre la causa."),
        ("Mezclar la causa con la solución.", "Las dos ideas aparecen cerca en el texto y se confunden.", "Marca because para la causa y can o decided para la solución."),
    ],
    [
        (ADULT + SLEEP + " ¿Cuál es el problema de Nico? A) no puede dormir temprano B) su teléfono está roto", "A) no puede dormir temprano", "Dice I can't sleep early."),
        (ADULT + SLEEP + " ¿Qué solución propone Mara? A) dejar el teléfono en otra pieza B) comprar un teléfono nuevo", "A) dejar el teléfono en otra pieza", "Why don't you leave it in another room?"),
        (ADULT + MIRROR + " ¿Cuál es el problema de Elena? A) está nerviosa por su presentación en inglés B) no tiene tema para su presentación", "A) está nerviosa por su presentación en inglés", "Dice I'm nervous about my English presentation."),
    ],
    [
        (ADULT + TAP + " ¿Cuál es la causa de que el huerto no tenga agua? A) la llave está rota B) los vecinos no quieren ayudar", "A) la llave está rota", "Dice no water because the tap is broken."),
        (ADULT + LATE + " ¿Por qué llegan tarde muchos estudiantes? A) porque el paradero está lejos del colegio B) porque el colegio abre más tarde", "A) porque el paradero está lejos del colegio", "Dice the bus stops far from school."),
        (ADULT + LATE + " ¿Cuál fue la decisión? A) mover el paradero más cerca del portón B) cambiar el horario de clases", "A) mover el paradero más cerca del portón", "Dice decided to move the bus stop closer to the main gate."),
    ],
    [
        (ADULT + TAP + " ¿Qué soluciones propone Persona B? A) pedir barriles a los vecinos y recolectar agua de lluvia B) comprar agua embotellada todos los días", "A) pedir barriles a los vecinos y recolectar agua de lluvia", "Dice We can ask the neighbours to donate barrels y collect rainwater."),
        (ADULT + HOT + " ¿Qué propone Persona B para el calor? A) abrir ventanas y usar cortinas B) cambiar de sala todos los días", "A) abrir ventanas y usar cortinas", "Dice open the windows and use curtains to block the sun."),
        (ADULT + SLEEP + " ¿Cuándo piensa Nico probar la sugerencia? A) esta noche B) el fin de semana", "A) esta noche", "Dice I'll try tonight."),
    ],
    [
        (ADULT + MIRROR + " ¿Por qué el profesor sugiere grabarse? A) para ver cómo mejorar la presentación B) para enviar el video a toda la clase", "A) para ver cómo mejorar la presentación", "Practicar y grabarse ayuda a corregir lo que se dice."),
        (ADULT + LATE + " Un compañero dice que la solución no ayuda porque el problema es la hora de salida de casa. ¿Qué contesta el reporte? A) que la causa es que el paradero queda lejos B) que la causa es el clima", "A) que la causa es que el paradero queda lejos", "El texto dice that the bus stops far from school."),
    ],
    [
        (ADULT + "«Bea: My plants always die. Joel: Do you give them water every day? Bea: Yes, every morning and evening. Joel: Maybe that is the problem. Too much water can hurt them. Water them only twice a week.» (plants = plantas, die = se mueren, evening = tarde-noche, hurt = dañar, twice = dos veces). ¿Qué causa propone Joel? A) exceso de agua B) falta de sol", "A) exceso de agua", "Dice Too much water can hurt them."),
        (ADULT + "«Bea: My plants always die. Joel: Do you give them water every day? Bea: Yes, every morning and evening. Joel: Maybe that is the problem. Too much water can hurt them. Water them only twice a week.» (plants = plantas, die = se mueren, hurt = dañar, twice = dos veces). ¿Qué solución propone Joel? A) regarlas solo dos veces por semana B) regarlas de noche", "A) regarlas solo dos veces por semana", "Dice Water them only twice a week."),
    ],
    [(ADULT + "«Mari: My bike has a flat tyre, and I'm late for school. Dad: Take the bus today, and we'll fix it tonight.» (flat tyre = rueda pinchada, late = atrasada, fix = arreglar, tonight = esta noche). ¿Cuál es la solución inmediata? A) tomar el bus hoy B) arreglar la bicicleta esta noche", "A) tomar el bus hoy", "Take the bus today es la solución inmediata; arreglar la bici será después.")],
    [
        ("En Inglés de 1.º medio (OA 3, clase 4): ¿qué es una relación problema-solución?", "Una dificultad y la propuesta para resolverla", "Se reconoce por frases como Why don't you...? o We can...."),
        ("En Inglés de 1.º medio (OA 3, clase 4): ¿qué palabra introduce una causa?", "Because", "Dice por qué ocurre algo."),
        ("En Inglés de 1.º medio (OA 3, clase 4): ¿cómo se pregunta una sugerencia?", "Why don't you...?", "Es una forma de proponer una solución."),
    ],
    task("Un adulto lee dos veces este diálogo: «Gabi: My little brother always loses his homework. Tom: Why don't you put a box by the door? He can put his papers there every night.» (loses = pierde, little brother = hermano menor, box = caja, door = puerta, papers = papeles). Anota el problema, la solución y una pregunta en inglés para sugerir otra solución.", "Problema: el hermano pierde su tarea. Solución: poner una caja junto a la puerta para dejar los papeles. Pregunta: Why don't you use a folder?", ["identifica el problema", "identifica la solución", "escribe una sugerencia en inglés con Why don't you...?"], ["hoja con problema, solución y pregunta", "nota del adulto"], ["anotar la solución como problema", "escribir una pregunta sin sentido de sugerencia"], "Reconoce lo logrado y, si la pregunta no sugiere algo, practica Why don't you... + verbo."),
    "Relee el texto del huerto y escribe una tabla con problema, causa, solución y resultado.",
    "Piensa en un problema pequeño de tu curso y escribe en español su causa y una solución posible.",
)

# ------------------------------------------------------------------ clase 5: respuesta independiente con temas menos conocidos
OCTO = "«Today I will tell you about octopuses. An octopus has three hearts and eight arms. Although it has no bones, it can pass through very small spaces. Scientists say octopuses are good at solving problems, for example, opening jars.» (octopus = pulpo, hearts = corazones, arms = brazos, bones = huesos, pass through = pasar por, spaces = espacios, jars = frascos)"
NEWYEAR = "«In many countries, people have special traditions for New Year. In Chile, some people eat lentils at midnight to wish for luck. In other places, people eat twelve grapes. Although the foods are different, the wish is the same: a good year.» (traditions = tradiciones, New Year = Año Nuevo, lentils = lentejas, midnight = medianoche, luck = suerte, grapes = uvas, wish = deseo)"
COLD = "«Last winter, our school had a problem: the classrooms were very cold. Some students wanted to buy heaters, while others wanted to seal the windows better. In the end, the school fixed the windows because it was cheaper and safer.» (winter = invierno, classrooms = salas, heaters = estufas, seal = sellar, windows = ventanas, fixed = arregló, cheaper = más barato, safer = más seguro)"
SILK = "«Many centuries ago, traders carried goods across Asia on a famous route. They exchanged cloth, spices and ideas. Today, people study that route to learn how cultures met. However, we still do not know every detail about it.» (centuries = siglos, traders = comerciantes, goods = productos, route = ruta, exchanged = intercambiaron, cloth = telas, spices = especias, cultures = culturas, met = se encontraron)"

lesson(
    OA, 5, MAT_L,
    "Aprenderé a entender por mi cuenta textos sobre temas menos conocidos: ideas generales, detalles, contrastes y problemas con su solución. Sirve para escuchar con confianza aunque el tema sea nuevo.",
    ["Sé reconocer propósito, tema, detalle, contraste y problema-solución.", "Conozco estrategias como escuchar en dos vueltas."],
    [
        "Cuando el tema es nuevo, no necesitas entender todas las palabras para captar la idea general. Primero identifica el propósito y el tema con ayuda de las palabras que se repiten y de las que conoces. En un texto sobre pulpos, aunque no conozcas jars, puedes entender que habla de cómo es un animal y qué puede hacer.",
        "Después busca los detalles que pide la pregunta. Usa lo que ya sabes: cifras, nombres, lugares y marcas de contraste (although, however, while) o de problema y solución (decided to, because). Si una palabra impide entender, usa el contexto: lo que se dice antes y después. No trates de traducirla; intenta adivinar su tipo, como una persona, un animal o un lugar.",
        "Para cerrar, resume en una frase: El texto trata de... y dice que... Luego compruébalo con una idea relevante del texto. Si tu resumen incluye un detalle que no estaba, corrígelo. En estos textos, algunas ideas son hechos que el hablante afirma; otras son opiniones. Distínguelas: Scientists say es un hecho atribuido; I think y In my opinion marcan una opinión.",
    ],
    [("general idea", "idea general"), ("context", "contexto: lo que rodea a una palabra"), ("fact", "hecho: algo que se afirma como cierto"), ("scientists say", "los científicos dicen"), ("tradition", "tradición"), ("summary", "resumen")],
    [
        ("Idea general de un tema nuevo", ADULT + SILK + " ¿Cuál es la idea general?", ["El tema es una ruta antigua de comercio.", "Los comerciantes intercambiaban telas, especias e ideas.", "Hoy se estudia para entender cómo se encontraron las culturas."], "Una ruta de comercio antigua unió culturas, y hoy se estudia"),
        ("Distinguir hecho y opinión", ADULT + OCTO + " ¿Scientists say octopuses are good at solving problems es un hecho atribuido o una opinión del hablante?", ["Scientists say indica que lo dicen los científicos.", "Es una información atribuida a una fuente.", "No es un I think."], "Un hecho atribuido a los científicos"),
    ],
    [
        ("Detenerse en una palabra desconocida.", "Se cree que sin entenderla no se comprende el texto.", "Sigue escuchando y usa el contexto; vuelve a la palabra después."),
        ("Resumir con un dato que no está en el texto.", "Se agregan conocimientos propios como si fueran parte del mensaje.", "Comprueba cada frase del resumen con una idea escuchada."),
    ],
    [
        (ADULT + OCTO + " ¿Cuántos corazones tiene un pulpo según el texto? A) tres B) ocho", "A) tres", "Dice three hearts; eight se refiere a los brazos."),
        (ADULT + NEWYEAR + " ¿Qué comen algunas personas en Chile a medianoche según el texto? A) lentejas B) uvas", "A) lentejas", "Dice In Chile, some people eat lentils."),
        (ADULT + COLD + " ¿Cuál era el problema del colegio? A) las salas estaban muy frías B) las estufas del colegio estaban rotas", "A) las salas estaban muy frías", "Dice the classrooms were very cold."),
    ],
    [
        (ADULT + OCTO + " ¿Por qué un pulpo puede pasar por espacios muy pequeños? A) porque no tiene huesos B) porque tiene tres corazones", "A) porque no tiene huesos", "Although it has no bones, it can pass through very small spaces."),
        (ADULT + NEWYEAR + " ¿Qué tienen en común las tradiciones del texto? A) el deseo de un buen año B) que usan los mismos alimentos", "A) el deseo de un buen año", "Dice the wish is the same: a good year."),
        (ADULT + COLD + " ¿Qué solución eligió el colegio? A) arreglar bien las ventanas B) comprar estufas", "A) arreglar bien las ventanas", "Dice the school fixed the windows."),
    ],
    [
        (ADULT + COLD + " ¿Por qué eligieron esa solución? A) porque era más barata y segura B) porque era más rápida", "A) porque era más barata y segura", "Dice because it was cheaper and safer."),
        (ADULT + SILK + " ¿Qué contraste hay al final del texto? A) hoy se estudia la ruta, pero no se conocen todos los detalles B) la ruta era corta, pero muy peligrosa", "A) hoy se estudia la ruta, pero no se conocen todos los detalles", "However marca lo que todavía no se sabe."),
        (ADULT + SILK + " ¿Qué estudia hoy la gente sobre esa ruta? A) cómo se encontraron las culturas B) cuánto costaban las especias", "A) cómo se encontraron las culturas", "Dice people study that route to learn how cultures met."),
    ],
    [
        (ADULT + NEWYEAR + " Un compañero dice que el texto muestra que una tradición es mejor que otra. ¿Qué respondes? A) no: dice que los alimentos son distintos pero el deseo es el mismo B) sí: el texto elige una tradición", "A) no: dice que los alimentos son distintos pero el deseo es el mismo", "Although marca la diferencia sin juzgar."),
        (ADULT + OCTO + " ¿Qué ejemplo da el texto de que los pulpos resuelven problemas? A) abren frascos B) tienen tres corazones", "A) abren frascos", "Dice for example, opening jars."),
    ],
    [
        (ADULT + SILK + " ¿Qué intercambiaban los comerciantes? A) telas, especias e ideas B) solo oro y plata", "A) telas, especias e ideas", "Dice They exchanged cloth, spices and ideas."),
        (ADULT + COLD + " ¿Qué querían unos estudiantes y qué otros? A) unos comprar estufas, otros sellar mejor las ventanas B) unos cerrar el colegio, otros abrirlo", "A) unos comprar estufas, otros sellar mejor las ventanas", "While une las dos posiciones."),
    ],
    [(ADULT + "«Today, many schools have a school garden. Students plant vegetables and learn about the seasons. However, in winter it is harder to grow food, so they use small greenhouses.» (school garden = huerto escolar, vegetables = verduras, seasons = estaciones, harder = más difícil, grow = cultivar, greenhouses = invernaderos). ¿Cuál es el problema y la solución? A) en invierno es difícil cultivar, y usan invernaderos B) los estudiantes no quieren plantar, y compran verduras", "A) en invierno es difícil cultivar, y usan invernaderos", "Dice harder to grow food in winter, so they use greenhouses.")],
    [
        ("En Inglés de 1.º medio (OA 3, clase 5): ¿qué haces si no entiendes una palabra de un tema nuevo?", "Sigo escuchando y uso el contexto", "El contexto ayuda a inferir su sentido."),
        ("En Inglés de 1.º medio (OA 3, clase 5): ¿qué significa Scientists say?", "Los científicos dicen: una información atribuida a una fuente", "No es una opinión del hablante."),
        ("En Inglés de 1.º medio (OA 3, clase 5): ¿cómo se resume un texto escuchado?", "En una frase con el tema y lo que dice", "Con las ideas relevantes."),
    ],
    task("Un adulto lee dos veces este texto: «Today I want to talk about wind energy. Wind turbines turn the wind into electricity. They do not make smoke, but they can be noisy. In my opinion, they are a good option for places with a lot of wind.» (wind energy = energía eólica, turbines = turbinas, electricity = electricidad, smoke = humo, noisy = ruidosas, option = opción). Escribe la idea general, un contraste y la opinión del hablante.", "Idea general: las turbinas transforman el viento en electricidad. Contraste: no producen humo, pero pueden ser ruidosas. Opinión: son una buena opción donde hay mucho viento.", ["resume la idea general en una frase", "identifica el contraste con su marca (but)", "distingue la opinión (In my opinion)"], ["hoja con tres respuestas", "nota del adulto"], ["confundir un hecho con la opinión", "resumir con un dato que no estaba"], "Reconoce lo logrado y, si mezcló hecho y opinión, subraya In my opinion para separar lo que cree el hablante."),
    "Escucha otra vez el texto del pulpo y escribe un resumen de una frase sin copiar detalles.",
    "Elige un tema que no domines, pide a alguien que te cuente tres ideas y escribe el tema, el propósito y una opinión.",
)

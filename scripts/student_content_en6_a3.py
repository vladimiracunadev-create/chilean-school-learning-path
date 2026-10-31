"""Cuaderno del estudiante, 6.º básico Inglés (propuesta), EN06 OA 03 (estrategias para apoyar la comprensión oral).

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Los textos son originales y llevan pista en español. Cada palabra o estructura nueva se explica antes de usarla.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA3 = "EN06 OA 03"
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


# ---------------------------------------------------------------- clase 1: hacer predicciones y verificarlas
SURPRISE = "«Mia's friends hide behind the door. When Mia enters, they shout: Happy birthday! Mia sees a big cake and many balloons. She is very surprised and happy.» (hide = se esconden, enters = entra, shout = gritan, balloons = globos, surprised = sorprendida)"
LOSTDOG = "«Lucas's dog, Toby, is lost. Lucas puts posters on the trees. Then a woman calls him: she found Toby in the park. Lucas runs to the park and hugs Toby.» (lost = perdido, posters = afiches, found = encontró, runs = corre, hugs = abraza)"

lesson(
    OA3, 1,
    "Los títulos, las descripciones de imágenes y los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a hacer predicciones antes de escuchar y a verificarlas después. Sirve para comprender mejor un texto oral porque ya sabes qué palabras esperar.",
    ["Sé que los títulos y las imágenes dan pistas del tema.", "Conozco palabras como cake, dog, rain y park."],
    [
        "Hacer una predicción (prediction) es pensar, antes de escuchar, qué dirá el texto. Para predecir usa el título (title), una imagen (picture) y lo que ya sabes del tema. Por ejemplo, si el título es «A Rainy Day» y la imagen muestra nubes y paraguas, esperas oír palabras como rain, umbrella o boots.",
        "Una predicción se puede escribir con la frase «I think the text is about... because...» (creo que el texto trata de... porque...). Mientras escuchas, comparas lo que oyes con lo que pensaste. Si las palabras coinciden, tu predicción se confirma (is confirmed). Si no coinciden, la corriges y piensas otra idea.",
        "Predecir no es adivinar sin base: necesitas una razón. Por eso conviene mirar todas las pistas antes de escuchar. Al terminar, verifica (check) tu predicción y di cuáles palabras la confirmaron. Esta estrategia reduce los nervios, porque ya conoces parte del vocabulario que viene.",
    ],
    [("prediction", "predicción: lo que creo que dirá el texto"), ("title", "título"), ("picture", "imagen"), ("I think... because...", "creo que... porque..."), ("confirmed", "confirmada"), ("check", "verificar")],
    [
        ("Predecir con título e imagen", "Título: «A Rainy Day». Imagen: nubes grises, un paraguas y charcos. ¿Cuáles de estas palabras esperas oír: rain, umbrella, sand, boots?", ["Miro las pistas: nubes, paraguas, charcos.", "Rain, umbrella y boots calzan con la lluvia.", "Sand se asocia a la playa, no a este título."], "rain, umbrella y boots"),
        ("Verificar la predicción", ADULT + "«It is a rainy day. Ben wears his boots and takes his umbrella. He jumps in the puddles.» (wears = se pone, takes = toma, jumps = salta, puddles = charcos). ¿Se confirmó la predicción de la palabra umbrella?", ["Escucho el texto y busco umbrella.", "Aparece takes his umbrella.", "La predicción se confirma."], "Sí, se confirmó"),
    ],
    [
        ("Predecir sin ninguna pista, solo adivinando.", "No se usa el título ni la imagen.", "Mira primero el título y la imagen, y da una razón con because."),
        ("Mantener la predicción aunque el texto diga otra cosa.", "No se compara lo que se oye con lo pensado.", "Si no coincide, corrige tu idea con lo que escuchas."),
    ],
    [
        ("Título: «The Birthday Surprise». Imagen: una torta, globos y una puerta. ¿Qué palabra esperas oír? a) cake b) volcano c) tractor", "a) cake", "La torta y los globos se relacionan con un cumpleaños."),
        ("Título: «The Lost Dog». Imagen: un afiche con la foto de un perro. ¿Cuál es el problema que predices? a) un perro está perdido b) un perro gana una carrera", "a) un perro está perdido", "El afiche de un perro sugiere que lo buscan."),
        ("Título: «A Day at the Beach». ¿Qué grupo de palabras esperas? a) sand, sea, umbrella b) snow, ski, coat", "a) sand, sea, umbrella", "Son palabras de playa."),
    ],
    [
        (ADULT + SURPRISE + " ¿Se confirma la predicción «cake»? Responde sí o no.", "Sí", "Dice a big cake."),
        (ADULT + SURPRISE + " ¿Se confirma la predicción «tractor»? Responde sí o no.", "No", "El texto no habla de ningún tractor."),
        (ADULT + SURPRISE + " ¿Cómo se siente Mia al final? a) sorprendida y feliz b) triste c) enojada", "a) sorprendida y feliz", "Dice she is very surprised and happy."),
    ],
    [
        (ADULT + LOSTDOG + " ¿Dónde estaba Toby? a) en el parque b) en el colegio", "a) en el parque", "Dice she found Toby in the park."),
        (ADULT + LOSTDOG + " ¿Qué puso Lucas en los árboles?", "Afiches", "Dice Lucas puts posters on the trees."),
        (ADULT + LOSTDOG + " Predijiste que Lucas estaría feliz al final. ¿Se confirma? Responde sí o no.", "Sí", "Dice Lucas runs to the park and hugs Toby."),
    ],
    [
        ("Una compañera predijo que Toby aparecía en el colegio. ¿Qué dice el texto y cómo debe corregir su predicción?", "Aparece en el parque", "El texto dice que lo encontró en el parque."),
        ("Título: «The Storm». Imagen: nubes oscuras y viento fuerte. ¿Qué primera oración es más probable? a) The wind is very strong today. b) We eat ice cream on the beach.", "a) The wind is very strong today.", "Coincide con las pistas de tormenta."),
    ],
    [
        ("Ordena las pistas para predecir bien. A) Pienso una razón con because. B) Miro el título y la imagen. C) Verifico mi predicción al escuchar.", "B, A, C", "Primero miras, luego razonas y al final verificas."),
        ("Predice. Título: «Soccer Final». Imagen: una pelota, un trofeo y una cancha. ¿Qué grupo de palabras esperas: goal, team, cup o kitchen, soup, spoon?", "goal, team, cup", "Coinciden con un partido de fútbol."),
    ],
    [(ADULT + "Título: «Weather Report». Imagen: sol y un termómetro con 32 grados. Texto: «Tomorrow will be hot and sunny. The temperature will be thirty-two degrees. Please use sunscreen.» (hot = caluroso, temperature = temperatura, sunscreen = bloqueador). ¿Qué recomendación se da?", "Usar bloqueador solar", "Dice please use sunscreen.")],
    [
        ("¿Qué significa «prediction»?", "Lo que creo que dirá el texto antes de escucharlo", "Es una idea basada en pistas."),
        ("¿Qué dos pistas ayudan a predecir?", "El título y la imagen", "Anticipan el tema del texto."),
        ("¿Qué haces si tu predicción no coincide con el texto?", "La corrijo", "Se compara con lo escuchado y se ajusta."),
    ],
    task("Observa este título e imagen: «The School Trip». Imagen: un bus amarillo, una mochila y un árbol. Escribe una predicción con la frase «I think the text is about... because...» y tres palabras que esperas oír. Después un adulto lee este texto: «The students get on the bus at eight. They go to a forest. They walk, take photos and eat lunch under a tree.» (get on = suben a, forest = bosque, take photos = sacan fotos). Escribe si tu predicción se confirmó y cuáles palabras la confirmaron.", "I think the text is about a trip because there is a bus. Palabras: bus, forest, lunch. Se confirmó con bus, forest y tree.", ["escribe una predicción con una razón", "anota tres palabras esperadas", "verifica con palabras del texto"], ["hoja con la predicción y la verificación", "nota del adulto"], ["predecir sin una razón", "no comparar con lo que se oyó"], "Reconoce la razón que dio y ayuda a comparar cada palabra esperada con el texto."),
    "Antes de que un adulto lea el cuento de Mia, escribe tres palabras que esperas oír y revisa cuántas aparecen.",
    "Elige un título de tu cuaderno de otra asignatura, escribe una predicción con because y escribe cómo la verificarías.",
)

# ---------------------------------------------------------------- clase 2: propósito y conocimientos previos
MARKET = "«Attention, shoppers. Today milk is at half price. Apples cost one thousand pesos a kilo. The bakery closes at eight o'clock. Thank you for shopping with us.» (shoppers = clientes, half price = mitad de precio, a kilo = el kilo, bakery = panadería, closes = cierra)"
PLANE = "«Welcome on board. Our plane to Santiago will land in forty minutes. Please fasten your seat belts and put your phone in airplane mode.» (welcome on board = bienvenidos a bordo, land = aterrizar, fasten = abrochar, seat belts = cinturones, airplane mode = modo avión)"
FOOT = "«In football, each team has eleven players on the field. A match has two halves of forty-five minutes. The referee uses a whistle to start and stop the game.» (team = equipo, field = cancha, halves = tiempos, referee = árbitro, whistle = silbato)"

lesson(
    OA3, 2,
    "Los avisos y textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a escuchar con un propósito y a usar lo que ya sé del tema para entender mejor. Sirve para encontrar rápido el dato que necesito en un aviso o en una explicación.",
    ["Sé que se escucha de distinta forma una canción y un aviso.", "Conozco palabras como football, plane y milk."],
    [
        "Escuchar con un propósito (listening purpose) significa decidir antes qué quieres averiguar. Puede ser el precio, la hora, un lugar o la idea general. Si tu propósito es saber a qué hora cierra una panadería, ignoras el resto y atiendes a las palabras bakery y closes y a un número. Así gastas menos esfuerzo y te equivocas menos.",
        "Los conocimientos previos (prior knowledge) son lo que ya sabes del tema. Si sabes cómo es un partido de fútbol, puedes anticipar palabras como team, goal, referee o ball, aunque no recuerdes todas. Pregúntate: ¿qué sé de este tema? ¿qué palabras suelen aparecer? Conectar lo nuevo con lo que ya sabes facilita recordar.",
        "Un buen plan tiene tres pasos. Primero, decide tu propósito. Segundo, recuerda lo que sabes del tema. Tercero, escucha atento a las palabras clave y los números. Cuando termine el texto, comprueba si cumpliste tu propósito: ¿encontraste el dato que buscabas? Si no, pide que repitan o escucha de nuevo.",
    ],
    [("listening purpose", "propósito de escucha"), ("prior knowledge", "conocimientos previos"), ("announcement", "aviso"), ("price", "precio"), ("half price", "mitad de precio"), ("referee", "árbitro")],
    [
        ("Escuchar con propósito", ADULT + "«Attention, passengers. The train to Valdivia leaves at ten fifteen from platform three. Please have your ticket ready.» (platform = andén, ticket ready = ticket listo). Tu propósito es saber de qué andén sale el tren. ¿Cuál es el dato?", ["Mi propósito es el andén; busco la palabra platform.", "Dice platform three.", "Ignoro la hora, que no me pidieron."], "Del andén 3"),
        ("Usar conocimientos previos", "Vas a escuchar un texto sobre un partido de básquetbol. ¿Qué palabras puedes anticipar con lo que ya sabes: ball, basket, players o soup?", ["Recuerdo lo que sé de básquetbol.", "Ball, basket y players aparecen en ese deporte.", "Soup no tiene relación."], "ball, basket y players"),
    ],
    [
        ("Tratar de entender todas las palabras del aviso.", "Se pierde el dato necesario.", "Define un propósito y atiende solo a las palabras clave relacionadas."),
        ("Escuchar sin pensar en lo que se sabe del tema.", "Se pierde la ayuda del vocabulario conocido.", "Antes de escuchar, recuerda las palabras que suelen aparecer."),
    ],
    [
        (ADULT + MARKET + " Tu propósito es saber el precio de las manzanas. ¿Cuánto cuesta el kilo?", "1.000 pesos", "Dice one thousand pesos a kilo."),
        (ADULT + MARKET + " Tu propósito es saber cuándo cierra la panadería. ¿A qué hora?", "A las 8", "Dice the bakery closes at eight o'clock."),
        (ADULT + MARKET + " Tu propósito es saber qué producto tiene descuento. ¿Cuál? a) la leche b) las manzanas", "a) la leche", "Dice milk is at half price."),
    ],
    [
        (ADULT + PLANE + " Tu propósito es saber cuántos minutos faltan para aterrizar. ¿Cuántos?", "40", "Dice in forty minutes."),
        (ADULT + PLANE + " ¿A qué ciudad va el avión?", "Santiago", "Dice our plane to Santiago."),
        (ADULT + PLANE + " ¿Qué se pide hacer con el teléfono? a) ponerlo en modo avión b) apagar la luz", "a) ponerlo en modo avión", "Dice put your phone in airplane mode."),
    ],
    [
        (ADULT + FOOT + " ¿Cuántos jugadores tiene cada equipo en la cancha?", "11", "Dice eleven players."),
        (ADULT + FOOT + " Si cada tiempo dura 45 minutos y hay dos tiempos, ¿cuántos minutos dura el partido sin descuentos?", "90", "Son dos tiempos de 45 minutos cada uno.", "45*2"),
        (ADULT + FOOT + " ¿Qué usa el árbitro para empezar y detener el juego?", "Un silbato", "El texto menciona un whistle."),
    ],
    [
        ("Un compañero escuchó el aviso del supermercado pensando en el precio de la leche y no en la panadería. Su propósito era saber cuándo cierra la panadería. ¿Qué dato necesitaba?", "Las ocho en punto", "La respuesta está en bakery closes at eight."),
        ("Alguien conoce las reglas del fútbol y no entiende la palabra referee. ¿Qué conocimiento previo le ayuda a deducirla? a) en un partido hay una persona que dirige el juego b) los equipos usan camisetas", "a) en un partido hay una persona que dirige el juego", "Esa persona es el árbitro."),
    ],
    [
        ("Ordena las acciones para una buena escucha. A) Compruebo si cumplí mi propósito. B) Escucho las palabras clave. C) Defino mi propósito.", "C, B, A", "Se define, se escucha y se comprueba."),
        (ADULT + "«Attention, students. The English test is on Thursday at nine. The Science test is on Friday at ten.» (test = prueba, Thursday = jueves, Friday = viernes). Tu propósito es la hora de la prueba de Ciencias. ¿Cuál es?", "A las 10", "Dice the Science test is on Friday at ten."),
    ],
    [(ADULT + "En el cine, un altavoz dice: «The film Space Dogs starts at six thirty in room five. Please turn off your phone.» (film = película, starts = empieza, room = sala, turn off = apagar). Tu propósito es saber a qué hora empieza. ¿Cuál es?", "A las 6:30", "Dice six thirty.")],
    [
        ("¿Qué es un propósito de escucha?", "Lo que quiero averiguar al escuchar", "Lo defines antes de escuchar."),
        ("¿Qué son los conocimientos previos?", "Lo que ya sé del tema", "Ayudan a anticipar palabras."),
        ("¿Qué significa «half price»?", "Mitad de precio", "Half es mitad."),
    ],
    task("Un adulto lee dos veces este aviso: «Attention, visitors. The science fair is on Wednesday from nine to one. There are fifteen projects about the Moon, plants and robots. The robot show is at eleven in the main hall.» (visitors = visitantes, science fair = feria científica, projects = proyectos, main hall = salón principal). Define dos propósitos de escucha distintos (por ejemplo, un día y una hora) y escribe el dato que responde a cada uno.", "Propósito 1: día de la feria, miércoles. Propósito 2: hora del show de robots, 11.", ["define dos propósitos distintos", "cada dato corresponde a su propósito", "los datos son correctos"], ["hoja con propósitos y datos", "nota del adulto"], ["cambiar el día por la hora", "anotar datos que no corresponden al propósito"], "Reconoce el propósito bien definido y muestra cómo ignorar las palabras que no sirven."),
    "Antes de que un adulto lea el aviso del supermercado, escribe en una hoja tu propósito y escucha solo el dato que necesitas.",
    "Escribe tres palabras que ya conoces sobre un deporte que te gusta y úsalas para predecir qué diría un texto sobre él.",
)

# ---------------------------------------------------------------- clase 3: palabras y expresiones clave
BUS = "«Attention, please. The bus to the museum leaves at nine o'clock from gate four. Please bring your ticket. Don't forget your water bottle.» (gate = puerta de salida, bring = trae, forget = olvidar, bottle = botella)"
RACE = "«Don't forget your helmet! The bike race starts at ten. The route is five kilometres long. Be careful on the bridge.» (helmet = casco, race = carrera, route = ruta, kilometres = kilómetros, careful = cuidadoso, bridge = puente)"
HANDS = "«Remember to wash your hands. Then tear the lettuce into small pieces. Add one spoon of oil and a little salt. Mix well.» (remember to = recuerda, tear = romper con las manos, lettuce = lechuga, pieces = trozos, oil = aceite, salt = sal)"

lesson(
    OA3, 3,
    "Los avisos e indicaciones escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a focalizar mi atención en palabras y expresiones clave, ignorando las palabras de relleno. Sirve para entender lo esencial aunque se hable rápido.",
    ["Sé que los números y los lugares son datos importantes.", "Conozco palabras como bus, bridge y water."],
    [
        "Las palabras clave (key words) son las que llevan el significado más importante: sustantivos, verbos y números. En «The bus to the museum leaves at nine o'clock», las palabras clave son bus, museum, leaves y nine. Las palabras pequeñas como the, to y at ayudan a formar la oración, pero casi nunca son lo central.",
        "Las expresiones clave anuncian algo importante: Attention, please (atención, por favor), Don't forget (no olvides), Remember to (recuerda), Be careful (ten cuidado) y Please bring (por favor trae). En el habla, las palabras importantes suenan más fuerte y más largas. Esa fuerza se llama énfasis (stress) y te ayuda a distinguirlas.",
        "Una buena estrategia es escribir un apunte en forma de telegrama: solo las palabras clave. Por ejemplo, «bus – museum – 9:00 – gate 4 – ticket». Con esas cinco palabras puedes reconstruir el mensaje. Si oyes una expresión como Don't forget, prepárate: lo que sigue es una cosa necesaria.",
    ],
    [("key words", "palabras clave"), ("Attention, please", "atención, por favor"), ("Don't forget", "no olvides"), ("Remember to", "recuerda..."), ("Be careful", "ten cuidado"), ("stress", "énfasis: palabras dichas con más fuerza")],
    [
        ("Elegir palabras clave", "En la oración «The train to the city leaves at six o'clock», ¿cuáles son las palabras clave: train, city, leaves, six?", ["Busco las palabras que dan el significado.", "Train, city, leaves y six llevan la información.", "The, to, at y o'clock acompañan."], "train, city, leaves y six"),
        ("Detectar una expresión clave", ADULT + "«Be careful on the wet floor. Don't run.» (wet = mojado, floor = piso, run = correr). ¿Qué avisa la expresión Be careful?", ["Be careful es una expresión de advertencia.", "Lo que sigue es on the wet floor.", "Hay que tener cuidado con el piso mojado."], "Que hay que tener cuidado con el piso mojado"),
    ],
    [
        ("Intentar anotar cada palabra que se oye.", "Se pierde el hilo porque se escribe demasiado.", "Anota solo palabras clave y números."),
        ("Pasar por alto la expresión Don't forget.", "No se reconoce que anuncia algo importante.", "Cuando la oigas, atiende lo que viene después."),
    ],
    [
        (ADULT + BUS + " ¿A dónde va el bus? a) al museo b) al parque c) a la playa", "a) al museo", "Las palabras clave son bus y museum."),
        (ADULT + BUS + " ¿De qué puerta sale?", "De la puerta 4", "Dice from gate four."),
        (ADULT + BUS + " ¿Qué expresión anuncia que algo no hay que olvidarlo? a) Don't forget b) Please bring", "a) Don't forget", "Don't forget significa no olvides."),
    ],
    [
        (ADULT + RACE + " ¿Qué no hay que olvidar? a) el casco b) la bicicleta", "a) el casco", "Dice Don't forget your helmet."),
        (ADULT + RACE + " ¿A qué hora empieza la carrera?", "A las 10", "Dice starts at ten."),
        (ADULT + RACE + " ¿Qué largo tiene la ruta?", "5 kilómetros", "Dice five kilometres long."),
    ],
    [
        (ADULT + RACE + " ¿Dónde hay que tener cuidado? a) en el puente b) en la partida", "a) en el puente", "Be careful on the bridge."),
        (ADULT + HANDS + " ¿Qué se agrega después de romper la lechuga? a) una cucharada de aceite y un poco de sal b) agua y azúcar", "a) una cucharada de aceite y un poco de sal", "Dice add one spoon of oil and a little salt."),
        (ADULT + HANDS + " ¿Qué recuerda la expresión Remember to? a) lavarse las manos b) comprar lechuga", "a) lavarse las manos", "Dice remember to wash your hands."),
    ],
    [
        ("Un compañero anotó del aviso del bus: «bus – museum – 9:00 – gate 4 – ticket». ¿Qué dato falta que sí se dijo? a) la botella de agua b) el color del bus", "a) la botella de agua", "El aviso pide no olvidar la water bottle."),
        ("En la oración «The bike race starts at ten», ¿cuáles son las palabras clave: bike, race, starts, ten, the, at?", "bike, race, starts y ten", "Son sustantivos, verbo y número; the y at solo acompañan."),
    ],
    [
        (ADULT + HANDS + " Escribe en telegrama las cuatro acciones de la receta, en el orden en que se dicen. Responde con cuatro verbos en inglés separados por comas.", "wash, tear, add, mix", "Son los verbos de cada acción en orden."),
        (ADULT + "«Attention, please. The lost child is wearing a red coat. Please come to the information desk.» (lost child = niño perdido, wearing = lleva puesto, coat = abrigo, information desk = mesa de información). Escribe en telegrama las tres palabras clave sobre la descripción del niño y el lugar donde ir.", "red coat, information desk", "Las palabras clave son el color del abrigo y el lugar donde presentarse."),
    ],
    [(ADULT + "En la piscina, un salvavidas dice: «Remember to shower before you swim. Don't run near the pool.» (lifeguard = salvavidas, shower = ducharse, swim = nadar, near = cerca de). ¿Qué hay que hacer antes de nadar?", "Ducharse", "Dice remember to shower before you swim.")],
    [
        ("¿Qué significa «Don't forget»?", "No olvides", "Anuncia algo necesario."),
        ("¿Qué palabras anotas en un apunte: todas o solo las clave?", "Solo las clave", "Son suficientes para reconstruir el mensaje."),
        ("¿Qué significa «Be careful»?", "Ten cuidado", "Avisa un posible peligro."),
    ],
    task("Un adulto lee dos veces este aviso: «Attention, please. The school concert is on Thursday at five o'clock in the gym. Don't forget your invitation. Be careful on the stairs. Remember to turn off your phone.» (concert = concierto, invitation = invitación, stairs = escalera). Escribe un apunte en telegrama con las palabras clave y subraya las tres expresiones de aviso.", "concert – Thursday – 5:00 – gym – invitation – stairs – phone off. Expresiones: Don't forget, Be careful, Remember to.", ["anota día, hora y lugar", "anota los tres objetos o avisos", "subraya las tres expresiones"], ["hoja con apuntes", "nota del adulto"], ["escribir oraciones completas", "olvidar la hora"], "Reconoce las palabras clave bien elegidas y practica a reducir el aviso a seis palabras."),
    "Pide a un adulto que lea el aviso del bus y tacha las palabras pequeñas del guion que no necesitas.",
    "Escribe un aviso de cuatro palabras clave para tu casa, por ejemplo sobre la hora de la comida.",
)

# ---------------------------------------------------------------- clase 4: apoyos visuales y gestos del hablante
lesson(
    OA3, 4,
    "Las descripciones de imágenes y de gestos escritas en cada ejercicio, y los textos que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a usar imágenes y los gestos de quien habla para entender mejor. Sirve para comprender cuando no conoces todas las palabras.",
    ["Sé que los gestos y las imágenes dan pistas.", "Conozco palabras como hot, cold, left y right."],
    [
        "Quien habla no solo usa palabras: también usa gestos (gestures), la cara y objetos. Si alguien señala con la mano hacia la derecha y dice «The school is over there», entiendes que la escuela está hacia la derecha aunque no conozcas over there. Una persona que se abraza con los brazos y dice «Brrr!» te indica que hace frío.",
        "Las imágenes (images) también ayudan: una foto, un mapa, un gráfico o un dibujo. Cuando escuches, mira la imagen al mismo tiempo. Pregúntate: ¿qué muestra la imagen? ¿qué palabra puede ir con ella? Si la imagen muestra un termómetro con 5 grados y el hablante dice «It's very ___ today», la palabra que falta es cold.",
        "Los apoyos no reemplazan las palabras; las completan. Combina siempre tres cosas: lo que oyes, lo que ves y lo que ya sabes. Si las pistas coinciden, tu comprensión es segura. Si no coinciden, pide aclaración. En este cuaderno, las imágenes y los gestos se describen entre corchetes.",
    ],
    [("gesture", "gesto"), ("image", "imagen"), ("point", "señalar"), ("map", "mapa"), ("over there", "allá"), ("Brrr!", "brrr: expresa frío")],
    [
        ("Gesto y palabras", "[Gesto: la persona señala hacia la derecha con la mano.] Dice: «The post office is over there, next to the bank.» (post office = correo, bank = banco). ¿Hacia dónde queda el correo?", ["El gesto señala hacia la derecha.", "Over there significa allá.", "Combino el gesto con las palabras."], "Hacia la derecha, al lado del banco"),
        ("Imagen y palabras", "[Imagen: un termómetro marca 35 grados y una persona abanica su cara.] Dice: «It's really ___ today.» Opciones: cold, hot, wet.", ["La imagen muestra mucho calor.", "El abanico confirma el calor.", "La palabra que falta es hot."], "hot"),
    ],
    [
        ("Ignorar el gesto del hablante.", "Se atiende solo a las palabras.", "Observa dónde señala o qué muestra con las manos."),
        ("Creer que la imagen siempre coincide con el texto.", "No se comparan las dos fuentes.", "Compara lo que ves con lo que oyes y pregunta si hay diferencia."),
    ],
    [
        ("[Imagen: una cebolla y lágrimas.] Dice: «I don't like cutting onions. They make me ___.» Opciones: cry, laugh, sing.", "cry", "Las lágrimas indican llorar."),
        ("[Gesto: la persona levanta tres dedos.] Dice: «We need ___ more players.» ¿Cuántos jugadores faltan?", "3", "El gesto de tres dedos indica el número."),
        ("[Imagen: un mapa con una flecha hacia el norte.] Dice: «Go north for two blocks.» (block = cuadra). ¿Hacia dónde hay que ir?", "Hacia el norte", "La palabra y la flecha coinciden."),
    ],
    [
        ("[Gesto: el hablante se frota el estómago y sonríe.] Dice: «Mmm, this soup is delicious!» (delicious = rico). ¿Qué opina del caldo?", "Que está rico", "El gesto y la palabra delicious coinciden."),
        ("[Imagen: una niña con un paraguas abierto bajo la lluvia.] Dice: «Today I have my ___.» Opciones: umbrella, sandwich, bicycle.", "umbrella", "La imagen muestra un paraguas."),
        ("[Gesto: el hablante bosteza y se frota los ojos.] Dice: «I'm very ___.» Opciones: tired, angry, hungry.", "tired", "Bostezar y frotarse los ojos son gestos de cansancio."),
    ],
    [
        ("[Imagen: una receta con una foto de pan, dos huevos y una taza.] Dice: «Today we need bread, ___ eggs and one cup of milk.» (eggs = huevos). ¿Cuántos huevos?", "2", "La foto muestra dos huevos."),
        ("[Imagen: un cartel con una flecha hacia arriba y la palabra BIBLIOTECA.] Dice: «The library is up the stairs.» (stairs = escalera). ¿Hay que subir o bajar para llegar a la biblioteca?", "Subir", "La flecha y up the stairs indican subir."),
        ("[Gesto: la persona señala su reloj.] Dice: «Hurry up! It's late.» (hurry up = apúrate, late = tarde). ¿Qué quiere decir?", "Que hay que apurarse", "El reloj indica que falta tiempo."),
    ],
    [
        ("[Imagen: un gráfico de barras: Lunes 3 libros, Martes 5 libros, Miércoles 2 libros.] Dice: «On Tuesday, the library lent ___ books.» ¿Qué número va en el espacio?", "5", "La barra del martes muestra 5 libros."),
        ("[Imagen: una calle con una farmacia a la derecha y un parque a la izquierda.] Dice: «The pharmacy is on the left.» ¿Qué error hay entre la imagen y las palabras?", "La farmacia está a la derecha en la imagen", "No coinciden la imagen y el audio."),
    ],
    [
        ("[Gesto: el hablante separa las manos unos 30 centímetros.] Dice: «The fish was this big.» (fish = pez). ¿Qué tamaño tenía el pez, aproximadamente?", "Unos 30 centímetros", "Las manos separadas muestran el largo."),
        ("[Imagen: tres vasos con agua: el primero lleno, el segundo a la mitad y el tercero casi vacío.] Dice: «Pass me the full glass, please.» (pass me = pásame, full = lleno). ¿Qué vaso te piden: el primero, el segundo o el tercero?", "El primero", "Full significa lleno y el primer vaso es el lleno."),
    ],
    [("[Imagen: un cartel de la estación con un tren y la hora 5:30.] La voz del altavoz dice: «The train to Rancagua leaves at five thirty.» (leaves = sale). ¿A qué hora sale?", "A las 5:30", "La imagen y las palabras coinciden en la hora.")],
    [
        ("¿Qué puedes mirar para entender mejor cuando hablan?", "Los gestos y las imágenes", "Dan pistas del significado."),
        ("¿Qué haces si la imagen y las palabras no coinciden?", "Pregunto para aclarar", "Hay una duda que resolver."),
        ("¿Qué significa «over there»?", "Allá", "Indica un lugar lejano."),
    ],
    task("Lee esta situación: [Imagen: un mapa del colegio con una flecha desde la puerta hasta la biblioteca pasando por el patio.] [Gesto: el profesor camina con dos dedos hacia adelante.] Dice: «First, go through the yard. Then turn left. The library is the second door.» (yard = patio, turn left = gira a la izquierda). Escribe tres pasos para llegar y di qué ayudó más: la imagen, el gesto o las palabras.", "Pasos: atravesar el patio, girar a la izquierda, entrar por la segunda puerta. Ayudó el mapa, el gesto y las palabras en conjunto.", ["escribe tres pasos en orden", "menciona la segunda puerta", "justifica qué apoyo ayudó"], ["hoja con pasos", "nota del adulto"], ["olvidar el giro a la izquierda", "no mencionar ningún apoyo"], "Reconoce la combinación de pistas y practica a describir el gesto con palabras."),
    "Pide a un adulto que diga «The cat is under the chair» señalando un lugar y comprueba si el gesto coincide con las palabras.",
    "Dibuja un mapa sencillo de tu cuadra y escribe una indicación en inglés usando left, right o straight.",
)

# ---------------------------------------------------------------- clase 5: preguntar para clarificar y verificar
lesson(
    OA3, 5,
    "Los diálogos escritos en cada ejercicio, que lee un adulto con voces distintas; una hoja para tapar el guion y lápiz.",
    "Aprenderé a preguntar para clarificar y corroborar información en una conversación y a verificar mis predicciones. Sirve para no quedarte con dudas y comprender de forma independiente.",
    ["Sé que puedo pedir que repitan.", "Conozco números como thirteen, fifteen y sixty."],
    [
        "En una conversación, si no entiendes, puedes preguntar. Sorry, can you repeat that? (¿puedes repetir eso?) pide una repetición. Can you speak more slowly? (¿puedes hablar más lento?) pide menos velocidad. What does ___ mean? (¿qué significa ___?) pide el sentido de una palabra. Do you mean ___? (¿quieres decir ___?) corrobora una idea que crees haber entendido.",
        "Los números pueden confundirse. En fifteen y fifty, la parte final suena distinta: fifTEEN tiene el énfasis al final, FIFty lo tiene al comienzo. Lo mismo ocurre con sixteen y sixty. Por eso, para corroborar, se pregunta: «Did you say sixteen or sixty?» (¿dijiste dieciséis o sesenta?) y la otra persona confirma: «Sixteen».",
        "Al final de la conversación, vuelve a tu predicción y verifícala: ¿lo que pensabas coincide con lo que se dijo? Preguntar no es una señal de que sabes poco; al contrario, muestra que quieres comprender bien. Una persona que clarifica a tiempo comete menos errores y aprende más rápido.",
    ],
    [("Can you repeat that?", "¿puedes repetir eso?"), ("Can you speak more slowly?", "¿puedes hablar más lento?"), ("What does ___ mean?", "¿qué significa ___?"), ("Do you mean ___?", "¿quieres decir ___?"), ("fifteen / fifty", "quince / cincuenta"), ("sixteen / sixty", "dieciséis / sesenta")],
    [
        ("Corroborar un número", ADULT + "«A: The film is sixteen minutes long. B: Did you say sixteen or sixty? A: Sixteen.» (film = película, minutes = minutos). ¿Cuántos minutos dura?", ["B duda entre dieciséis y sesenta.", "A confirma Sixteen.", "El número es 16."], "16 minutos"),
        ("Pedir el significado", ADULT + "«A: Put your books in the locker. B: What does locker mean? A: It is a small cupboard at school.» (locker = casillero, cupboard = armario). ¿Qué pregunta B y qué recibe?", ["B pregunta What does locker mean?", "A le explica con otras palabras.", "Locker es un armario pequeño del colegio."], "Pregunta el significado de locker y le dicen que es un armario pequeño del colegio"),
    ],
    [
        ("Quedarse callado cuando no se entiende un número.", "Se teme preguntar.", "Pregunta: Did you say fifteen or fifty?"),
        ("Confirmar con Yes sin comprobar el dato.", "No se corrobora la información.", "Repite el dato con tus palabras y pide confirmación."),
    ],
    [
        ("No escuchaste una frase. ¿Qué dices? a) Sorry, can you repeat that? b) See you tomorrow. c) I'm fine, thanks.", "a) Sorry, can you repeat that?", "Esa pregunta pide repetición."),
        ("¿Qué pregunta sirve para pedir que hablen más lento? a) Can you speak more slowly? b) What time is it?", "a) Can you speak more slowly?", "Slowly significa lentamente."),
        ("¿Qué pregunta sirve para saber el significado de una palabra? a) What does ___ mean? b) Where do you live?", "a) What does ___ mean?", "Mean significa significar."),
    ],
    [
        (ADULT + "«A: The ticket costs fifteen thousand pesos. B: Did you say fifteen or fifty? A: Fifteen thousand.» (ticket = entrada). ¿Cuánto cuesta la entrada?", "15.000 pesos", "A confirma fifteen thousand."),
        (ADULT + "«A: My phone number ends in thirteen. B: Thirteen or thirty? A: Thirteen, one-three.» (ends in = termina en). ¿Cómo termina el número?", "En 13", "A confirma thirteen, one-three."),
        (ADULT + "«A: The match is on Saturday. B: Do you mean this Saturday? A: Yes, this Saturday.» (match = partido, this = este). ¿Qué corrobora B?", "Que el partido es este sábado", "B pregunta Do you mean this Saturday?"),
    ],
    [
        ("Elige la pregunta correcta para corroborar: oíste «forty» o «fourteen» y no estás seguro. ¿Qué preguntas? a) Did you say forty or fourteen? b) Where is the bus?", "a) Did you say forty or fourteen?", "Compara los dos números posibles."),
        ("Quieres saber si entendiste bien que la reunión es a las cinco. ¿Qué preguntas? a) Do you mean at five o'clock? b) What is your name?", "a) Do you mean at five o'clock?", "Corrobora el dato con tus palabras."),
        ("En el diálogo «A: We start at eight. B: Do you mean in the morning? A: No, in the evening.», ¿cuándo empiezan?", "En la tarde-noche, a las 8", "A corrige la idea de B con No, in the evening."),
    ],
    [
        ("Un compañero predijo que el diálogo trataba de un partido. En el diálogo anterior (start at eight, in the evening) no se dice la palabra match. ¿Qué debe hacer con la predicción?", "Corregirla o preguntar de qué evento se habla", "El diálogo no confirma que sea un partido."),
        ("Ordena los pasos de una buena clarificación. A) Confirmo con la respuesta. B) Pregunto Did you say...? C) Escucho el dato.", "C, B, A", "Primero escuchas, luego preguntas y al final confirmas."),
    ],
    [
        (ADULT + "«A: We need sixty chairs for the show. B: Sixty or sixteen? A: Sixty, six-zero.» (chairs = sillas, show = presentación). Si cada fila tiene diez sillas, ¿cuántas filas hacen falta?", "6", "Se reparten sesenta sillas en filas de diez.", "60//10"),
        ("¿Qué hace más fácil oír la diferencia entre fifteen y fifty: el énfasis al final o al comienzo?", "En fifteen el énfasis está al final", "Fifteen tiene énfasis en teen; fifty lo tiene en la primera sílaba."),
    ],
    [(ADULT + "En el metro, un turista te dice: «Excuse me, which platform for line five?» y no entiendes la palabra platform. ¿Qué le puedes preguntar? Elige: a) What does platform mean? b) Thanks, goodbye.", "a) What does platform mean?", "Es la pregunta para conocer el significado de una palabra.")],
    [
        ("¿Qué significa «Do you mean...?»", "¿Quieres decir...?", "Se usa para corroborar."),
        ("¿Qué números se confunden con fifteen?", "fifty", "Suenan parecido pero tienen énfasis distinto."),
        ("¿Por qué es bueno preguntar cuando no entiendes?", "Porque evita errores y ayuda a aprender", "Aclara la información."),
    ],
    task("Lee y completa: [Un amigo dice por teléfono] «The party is at five o'clock. Sixteen children are coming.» (children = niños). No estás seguro si oíste sixteen o sixty, ni si la hora es five o'clock. Escribe en inglés tres preguntas que harías para corroborar: una por el número, una por la hora y una para pedir que hablen más lento. Luego escribe la respuesta que recibirías.", "Did you say sixteen or sixty? Do you mean at five o'clock? Can you speak more slowly? Respuesta: Sixteen, yes, at five o'clock.", ["escribe una pregunta para el número", "escribe una pregunta para la hora", "escribe una frase para pedir que hablen más lento"], ["hoja con preguntas", "nota del adulto"], ["escribir una pregunta sin estructura inglesa", "no incluir la respuesta"], "Reconoce las preguntas bien formadas y practica en voz alta con una persona la entonación."),
    "Con una persona de tu casa, practica el diálogo de sixteen y sixty, cambiando los números por fifteen y fifty.",
    "Escribe dos frases en inglés que usarías si no entendieras a un profesor, por ejemplo con Can you repeat...? y What does...?",
)

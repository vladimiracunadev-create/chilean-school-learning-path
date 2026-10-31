"""Cuaderno del estudiante, 7.º básico Inglés (propuesta), EN07 OA 10 (funciones comunicativas en conversaciones y exposiciones).

Las funciones del OA se reparten en las cinco clases: posesión y descripción de objetos, tiempo-grado-modo y preguntas sobre el
tiempo, causa-condición y conexión de ideas, preguntas sobre rutinas y pasado, y acciones interrumpidas con permiso y consejo.
Los diálogos están escritos en cada enunciado, con pista en español; la práctica oral se hace con una persona de la casa.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_content_en7_a import lesson

OA10 = "EN07 OA 10"

# ---------------------------------------------------------------- clase 1: posesión y descripción de objetos
MUSEUM = "Diálogo en un museo: «Guide: Look at this instrument. Visitor: Whose is it? Guide: It is the musicians' charango. It is a small wooden string instrument from the Andes. Visitor: And this one? Guide: That is a long thin flute. It is the old musician's. The new flute is mine.» (guide = guía, whose = de quién, string = de cuerdas, flute = flauta, musician = músico)"
ROOM = "Diálogo en una sala de clases: «Ana: Is this your notebook? Eva: No, it isn't mine. It is Tomás's. Mine is the big green one. Ana: And these pencils? Eva: They are the teachers'. Theirs are in the red box.» (notebook = cuaderno, pencils = lápices, box = caja)"
STORE = "Diálogo en una tienda de segunda mano: «Seller: This is a lovely old leather bag. Customer: How much is it? Seller: It is the owner's favorite. Customer: And that blue ceramic cup? Seller: That small ceramic cup is ours. It is not for sale.» (lovely = precioso, leather = cuero, ceramic = cerámica, owner = dueño, for sale = en venta)"

lesson(
    OA10, 1,
    "Los diálogos escritos en cada ejercicio, lápiz y una persona de tu casa para practicar.",
    "Aprenderé a usar al hablar la posesión (Tomás's, the teachers', mine, theirs, whose) y a describir objetos en detalle con el orden tamaño–edad–color–material. Sirve para decir de quién es algo y cómo es.",
    ["Sé los colores y los materiales: wood, metal, plastic.", "Conozco my, your, his y her."],
    [
        "Cuando hablas, usas la posesión para decir quién es el dueño: Tomás's notebook (el cuaderno de Tomás), the teachers' pencils (los lápices de las profesoras). Con un nombre singular se agrega 's; con un plural regular se agrega solo el apóstrofo. Para preguntar, usa whose: Whose is it? (¿de quién es?). Para responder sin repetir el sustantivo, usa los pronombres posesivos: mine, yours, his, hers, ours y theirs.",
        "Para describir un objeto en detalle, los adjetivos van antes del sustantivo, normalmente en este orden: tamaño, edad, color y material: a small old blue ceramic cup. No es necesario usar todos: dos o tres adjetivos bastan. Una buena descripción permite que otra persona imagine el objeto. Puedes comenzar con It is a… o It's an… (usa an antes de una vocal: an old wooden instrument).",
        "En una conversación, combina ambas funciones: Whose is that long thin flute? — It's the old musician's. — Is the new one yours? — No, it's mine. Practica en voz alta con una persona de tu casa. Cambia los objetos de la mochila o de la pieza y responde las preguntas rápido, usando mine, yours y theirs.",
    ],
    [("'s / s'", "marca de posesión: de uno / de varios"), ("whose", "de quién"), ("mine, yours, theirs", "pronombres: mío, tuyo, de ellos"), ("size, age, color, material", "tamaño, edad, color, material"), ("It is a/an…", "Es un/una…"), ("for sale", "en venta")],
    [
        ("Pregunta y respuesta", "Completa: «Whose is this bag? It is ___.» (de María) Elige María's o Marías.", ["Para un nombre singular se usa 's.", "María más 's es María's.", "Marías no marca posesión."], "María's"),
        ("Orden de adjetivos", "Ordena para describir una taza: ceramic / small / blue / a / cup.", ["El tamaño va primero: small.", "Luego el color: blue.", "Al final el material: ceramic."], "a small blue ceramic cup"),
    ],
    [
        ("Decir «a ceramic blue small cup».", "No se respeta el orden tamaño, color, material.", "Dilo así: a small blue ceramic cup."),
        ("Responder «It is my» sin sustantivo.", "My necesita un sustantivo.", "Sin sustantivo se usa mine: It is mine."),
    ],
    [
        (MUSEUM + " ¿De quiénes es el charango? a) de los músicos b) del visitante", "a) de los músicos", "Dice It is the musicians' charango."),
        (ROOM + " ¿De quién es el cuaderno? a) de Tomás b) de Eva", "a) de Tomás", "Eva dice It is Tomás's."),
        (STORE + " ¿Qué taza no está en venta? a) la taza de cerámica pequeña b) la bolsa de cuero", "a) la taza de cerámica pequeña", "Dice That small ceramic cup is ours. It is not for sale."),
    ],
    [
        (MUSEUM + " ¿Cómo es la flauta larga? a) larga y delgada b) corta y gruesa", "a) larga y delgada", "Dice a long thin flute."),
        (ROOM + " ¿De quiénes son los lápices?", "De las profesoras", "Dice They are the teachers'."),
        (STORE + " ¿Cómo es la bolsa? a) preciosa, vieja y de cuero b) nueva y de plástico", "a) preciosa, vieja y de cuero", "Dice a lovely old leather bag."),
    ],
    [
        (MUSEUM + " Completa con el pronombre: «The new flute is ___.» Elige mine o my.", "mine", "Sin sustantivo se usa mine."),
        (ROOM + " Completa: «Mine is the big green one» significa que el cuaderno verde grande es a) de Eva b) de Ana", "a) de Eva", "Eva es quien dice mine."),
        (STORE + " Completa: «That cup is ___ (de nosotros).» Elige ours o ourselves.", "ours", "Ours es el pronombre posesivo de we."),
    ],
    [
        (ROOM + " Eva dice «Theirs are in the red box». ¿Quién tiene los lápices en la caja roja? a) las profesoras b) Tomás", "a) las profesoras", "Theirs se refiere a the teachers."),
        ("¿Qué frase es correcta? a) It is an old wooden table b) It is a wooden old table.", "a) It is an old wooden table.", "La edad va antes del material."),
    ],
    [
        ("Cuenta cuántos adjetivos tiene esta descripción: «a small old blue ceramic cup».", "4", "Son cuatro palabras que describen la taza."),
        (STORE + " Si compraras 2 bolsas como esa a 25.000 pesos cada una (dato de ejemplo), ¿cuánto pagarías en total?", "$50.000", "Se multiplica el precio de una bolsa por dos.", "2*25000"),
    ],
    [("Mostrando una foto de tu mochila, dices: «It is a medium red nylon backpack. It is mine.» (medium = mediana, nylon = nailon). ¿Qué material mencionas? a) nailon b) cuero", "a) nailon", "Dice red nylon backpack.")],
    [
        ("Al hablar, ¿qué significa la palabra whose en Whose is it?", "De quién", "Se usa para preguntar por el dueño."),
        ("¿Cuál es el orden de los adjetivos?", "Tamaño, edad, color y material", "Es el orden usual."),
        ("¿Qué pronombre significa «de nosotros»?", "ours", "Reemplaza el sustantivo."),
    ],
    task("Trabaja con una persona de tu casa. Elige tres objetos de la casa (por ejemplo, una taza, una mochila y un cojín). Describe cada uno en inglés con tres adjetivos (tamaño, color, material) y di de quién es con 's o mine/yours. Ejemplo ya dado: «It is a small red plastic cup. It is Ana's.» Después pregunta «Whose is it?» y que la otra persona responda.", "It is a big gray cotton cushion. It is ours. — Whose is the green plastic bottle? — It is mine.", ["describe tres objetos con tres adjetivos en el orden correcto", "usa 's o un pronombre posesivo en cada caso", "formula y responde Whose is it?"], ["lista de tres descripciones", "nota de la persona que escuchó"], ["poner el material antes del color", "usar «my» sin sustantivo"], "Reconoce lo que acertó y practica con la persona el orden de los adjetivos objeto por objeto."),
    "Describe en voz alta tres cosas de tu pieza usando solo dos adjetivos cada una.",
    "Escribe cinco preguntas con whose sobre objetos de tu colegio y sus respuestas con mine, yours o theirs.",
)

# ---------------------------------------------------------------- clase 2: tiempo, grado, modo y preguntas de tiempo
CAMP = "Diálogo sobre un campamento: «Leo: When is the camp? Mia: It is in December. We leave on Saturday at 10:00. Leo: Do we walk? Mia: Yes, but the first hill is a bit steep. Every morning we run fast to the river. Leo: And the night? Mia: At night we talk quietly. Suddenly, an owl hooted, and everybody laughed!» (camp = campamento, leave = salir, steep = empinada, river = río, quietly = en voz baja, owl = búho, hooted = ululó)"
RACE = "Presentación breve: «Yesterday, Carla won the school race. She runs very fast, and she trains every week. Her friend Pablo runs a little slowly, but he never gives up. Next week, they will run again. The party is on Friday at six o'clock.» (won = ganó, trains = entrena, slowly = despacio, never gives up = nunca se rinde)"
BAND = "Conversación: «Rosa: When is the concert? Ben: Next Saturday, at 8:30. Rosa: Is it in the evening? Ben: Yes, it is. The guitarist plays very well, and the singer sings quite loudly. Sometimes the drummer plays too fast, but the audience loves it.» (concert = concierto, evening = tarde-noche, guitarist = guitarrista, singer = cantante, loudly = fuerte, drummer = baterista, audience = público)"

lesson(
    OA10, 2,
    "Los diálogos escritos en cada ejercicio, lápiz y una persona de tu casa para practicar.",
    "Aprenderé a usar al hablar expresiones de tiempo (on Saturday, in December, next week), de grado (very, a bit, a little, quite) y de modo (quietly, fast, well), y a preguntar y dar información sobre el tiempo con When is…? Sirve para organizar encuentros y describir cómo ocurren las acciones.",
    ["Sé los días de la semana y los meses.", "Conozco adverbios como always y never."],
    [
        "Para preguntar y dar información sobre el tiempo, usa When is the party? (¿cuándo es la fiesta?) y responde con una preposición: On Saturday (días), At 10:00 (horas), In December (meses), tomorrow, next week, next year. En esas respuestas no se usa preposición con tomorrow, next week, next year ni yesterday. También se puede decir what time para preguntar la hora: What time is it?",
        "Los adverbios de grado (degree) dicen cuánto: very, quite, a bit, a little. Los de modo (manner) dicen cómo: quietly (en voz baja), fast (rápido), well (bien), loudly (fuerte). Los de frecuencia dicen cada cuánto: every week, always, sometimes, never. Suddenly (de pronto) marca un hecho inesperado. Los de modo y de grado suelen ir después del verbo o al final: she sings quietly, they run very fast. Los de frecuencia van antes del verbo principal: she always sings. He won the race yesterday indica el momento.",
        "Observa la diferencia entre a bit y very: he runs a bit slowly (un poco lento) y he runs very fast (muy rápido). A little se usa igual que a bit: she is a little tired. Al hablar, escoge el adverbio que describa la situación con precisión. Practica diciendo la misma oración con adverbios distintos para ver cómo cambia el significado.",
    ],
    [("When is…?", "¿Cuándo es…?"), ("on / at / in", "con días / con horas / con meses"), ("very, quite, a bit, a little", "muy, bastante, un poco"), ("quietly, fast, well", "en voz baja, rápido, bien"), ("suddenly", "de pronto"), ("every week", "cada semana")],
    [
        ("Pregunta de tiempo", "Completa la respuesta: «When is the meeting? ___ Thursday ___ 4:00.» Elige On…at o In…on.", ["Los días llevan on.", "Las horas llevan at.", "Queda On Thursday at 4:00."], "On…at"),
        ("Adverbio de modo", "Completa: «She speaks ___ in the library.» Elige quietly o quiet.", ["Necesito un adverbio que diga cómo habla.", "Quietly es el adverbio.", "Quiet es un adjetivo."], "quietly"),
    ],
    [
        ("Decir «She speaks quiet».", "Se usa el adjetivo en lugar del adverbio.", "Con el verbo se usa quietly."),
        ("Decir «in Saturday».", "Se confunde la preposición.", "Con los días se usa on."),
    ],
    [
        (CAMP + " ¿Cuándo es el campamento? a) en diciembre b) en marzo", "a) en diciembre", "Dice It is in December."),
        (RACE + " ¿Quién ganó la carrera ayer? a) Carla b) Pablo", "a) Carla", "Dice Carla won the school race."),
        (BAND + " ¿A qué hora es el concierto? a) a las 8:30 b) a las 6:00", "a) a las 8:30", "Dice at 8:30."),
    ],
    [
        (CAMP + " ¿Cómo es la primera colina? a) un poco empinada b) muy plana", "a) un poco empinada", "Dice a bit steep."),
        (RACE + " ¿Con qué frecuencia entrena Carla?", "Cada semana", "Dice she trains every week."),
        (BAND + " ¿Cómo toca el guitarrista? a) muy bien b) mal", "a) muy bien", "Dice plays very well."),
    ],
    [
        (CAMP + " ¿Cómo hablan de noche?", "En voz baja", "Dice we talk quietly."),
        (RACE + " ¿Cuándo es la fiesta?", "El viernes a las seis", "Dice The party is on Friday at six o'clock."),
        (BAND + " ¿Qué ocurre a veces con el baterista? a) toca demasiado rápido b) no viene", "a) toca demasiado rápido", "Dice sometimes the drummer plays too fast."),
    ],
    [
        (CAMP + " ¿Qué hecho inesperado ocurrió? a) un búho ululó de pronto b) llegó la lluvia", "a) un búho ululó de pronto", "Dice suddenly, an owl hooted."),
        ("¿Qué oración dice cuánto? a) He is very tired b) He is tired yesterday.", "a) He is very tired.", "Very indica el grado."),
    ],
    [
        ("Responde la pregunta «When is your birthday?» con una oración correcta. a) It is in June b) It is on June.", "a) It is in June.", "Los meses llevan in."),
        (CAMP + " Si salen el sábado a las 10:00 y la caminata dura 3 horas, ¿a qué hora llegan?", "13:00", "Se suman tres horas a las diez de la mañana.", "10+3"),
    ],
    [("Un compañero te pregunta: «When is the school party?» Respondes: «It is on Friday at 7:00.» (party = fiesta). ¿Qué dos datos de tiempo diste? a) el día y la hora b) el mes y el año", "a) el día y la hora", "On Friday indica el día y at 7:00 la hora.")],
    [
        ("Al decir cuándo es un evento en inglés, ¿qué preposición va con un día?", "on", "Se dice on Saturday."),
        ("¿Cómo se dice «de pronto» en inglés?", "suddenly", "Marca un hecho inesperado."),
        ("¿Qué significa «a bit»?", "Un poco", "Es un adverbio de grado."),
    ],
    task("Trabaja con una persona de tu casa. Pregúntale con When is…? por la fecha de tres eventos de la lista ya dada: el cumpleaños de una persona de tu casa, el fin del año escolar y el próximo fin de semana largo. Responde tú con on, at e in. Después describe cómo haces tres actividades usando un adverbio de modo y uno de grado: ejemplo ya dado, «I walk to school very quickly.»", "When is your birthday? It is in May. When is the school trip? It is on Friday at 9:00. I read quietly. I run a bit slowly.", ["formula tres preguntas con When is…?", "responde con on, at o in correctos", "usa adverbios de modo y grado"], ["hoja con preguntas y respuestas", "nota de la persona que escuchó"], ["decir «in Monday»", "usar un adjetivo en lugar del adverbio"], "Reconoce lo que acertó y practica con la persona los días, las horas y los meses con sus preposiciones."),
    "Di cinco oraciones sobre tu semana usando every, always o sometimes.",
    "Escribe una invitación en inglés con día, hora y lugar usando on, at e in.",
)

# ---------------------------------------------------------------- clase 3: causa, condición y conexión de ideas
EXPER = "Conversación sobre un experimento seguro en casa: «Nina: Why is the ice melting? Omar: Because it is warm in the kitchen. If you leave an ice cube on a plate, it melts. Nina: Is it only because of the heat? Omar: Yes. If you put it in the freezer, it will stay hard. First, we put the ice on a plate. Second, we wait. Next, we measure the water. Finally, we write the result.» (ice = hielo, melting = derritiéndose, kitchen = cocina, freezer = congelador, stay hard = seguir duro, measure = medir)"
CHORES = "Conversación: «Sam: I clean my room, and my sister cleans the kitchen too. Lía: If you cook, I'll help you. Sam: Do you want to wash the dishes or set the table? Lía: I'll set the table, because I don't like washing dishes. Sam: First, we cook. Second, we eat. Finally, we clean.» (clean = limpiar, cook = cocinar, wash the dishes = lavar los platos, set the table = poner la mesa)"
PLANT = "Conversación: «Eva: My plant is yellow because it has no water. If I water it every day, it will be green again. Teo: Or maybe it needs more light? Eva: Maybe. I will put it near the window, too. Teo: Good idea. Then it will grow fast.» (yellow = amarilla, water = regar, light = luz, window = ventana, grow = crecer)"

lesson(
    OA10, 3,
    "Los diálogos escritos en cada ejercicio, lápiz y una persona de tu casa para practicar.",
    "Aprenderé a explicar causa y efecto (An ice cream melts if you heat it), a expresar condiciones (If you cook, I'll help you) y a unir ideas con too, or, first, second, next y finally. Sirve para explicar por qué ocurren las cosas y para organizar lo que digo.",
    ["Sé usar because y if.", "Conozco first, second y finally."],
    [
        "La causa y el efecto responden por qué pasa algo. Se pueden decir de dos formas: con because (The ice melts because it is warm) o con if cuando es una verdad general (An ice cream melts if you heat it). Para preguntar la causa, usa why: Why is the ice melting? (¿por qué se derrite el hielo?). Se responde con because.",
        "Las condiciones expresan algo posible en el futuro: if + presente, y el resultado con will: If you cook, I'll help you; If I water it every day, it will be green again. Para unir ideas se usa and (y), or (o) para ofrecer opciones, too (también) al final, y first, second, next y finally para ordenar. Al hablar, combina: First, we put the ice on a plate. Second, we wait.",
        "Observa la diferencia: because da una razón («Because it is warm»); if da una condición («If you put it in the freezer, it will stay hard»). Or ofrece opciones: wash the dishes or set the table. Too se usa en afirmaciones: My sister cleans the kitchen too. Con la práctica, usa los conectores para que tu discurso suene más natural y organizado.",
    ],
    [("because", "porque: razón"), ("if…, will…", "si…, entonces…: condición"), ("or", "o: opciones"), ("too", "también (al final)"), ("first, second, next, finally", "primero, segundo, luego, finalmente"), ("why", "por qué")],
    [
        ("Causa", "Responde: «Why is the ice melting?» a) Because it is warm b) If it is cold.", ["Why pide una razón.", "Because da la razón.", "La opción a es correcta."], "a) Because it is warm."),
        ("Condición", "Completa: «If you cook, I ___ help you.» Elige will o am.", ["Después de if + presente, el resultado lleva will.", "Queda I will help you.", "Se puede contraer: I'll."], "will"),
    ],
    [
        ("Decir «If you will cook, I help you».", "Se invierten los tiempos verbales.", "If + presente; el resultado lleva will."),
        ("Usar too al comienzo de la oración.", "Too va al final de la oración afirmativa.", "Di: My sister cleans too."),
    ],
    [
        (EXPER + " ¿Por qué se derrite el hielo? a) porque hace calor en la cocina b) porque está en el congelador", "a) porque hace calor en la cocina", "Dice because it is warm in the kitchen."),
        (CHORES + " ¿Qué ofrece Lía? a) ayudar a cocinar b) lavar la ropa", "a) ayudar a cocinar", "Dice If you cook, I'll help you."),
        (PLANT + " ¿Por qué está amarilla la planta de Eva? a) porque no tiene agua b) porque tiene mucho sol", "a) porque no tiene agua", "Dice because it has no water."),
    ],
    [
        (EXPER + " ¿Qué pasa si se pone el hielo en el congelador?", "Se queda duro", "Dice it will stay hard."),
        (CHORES + " ¿Qué elige Lía: lavar los platos o poner la mesa?", "Poner la mesa", "Dice I'll set the table."),
        (PLANT + " ¿Qué ocurrirá si Eva riega la planta todos los días? a) volverá a estar verde b) se secará", "a) volverá a estar verde", "Dice it will be green again."),
    ],
    [
        (EXPER + " ¿Qué se hace en el tercer paso? a) medir el agua b) escribir el resultado", "a) medir el agua", "Next, we measure the water."),
        (CHORES + " ¿Por qué no lava los platos Lía?", "Porque no le gusta", "Dice because I don't like washing dishes."),
        (PLANT + " ¿Qué conector ofrece una opción: or o too?", "or", "Or ofrece otra posibilidad: more light."),
    ],
    [
        (EXPER + " ¿Cuál es el resultado general que enseña Omar? a) El hielo se derrite si hace calor b) El hielo se derrite si hace frío", "a) El hielo se derrite si hace calor", "Es la causa que explica."),
        (CHORES + " ¿Qué conector muestra que la hermana también limpia? a) too b) or", "a) too", "Too significa también."),
    ],
    [
        (PLANT + " Ordena el plan. A) Poner la planta cerca de la ventana. B) Regar todos los días. C) La planta crece rápido.", "B, A, C", "Primero se riega, luego se pone en la luz y el resultado es que crece."),
        (EXPER + " Si 4 cubos de hielo caben en una bandeja y hay 3 bandejas, ¿cuántos cubos hay? Dato de ejemplo.", "12", "Se multiplica la cantidad de cubos de cada bandeja por las bandejas.", "4*3"),
    ],
    [("Conversas con un compañero: «If you share your notes, I will help you study.» (notes = apuntes, share = compartir, study = estudiar). ¿Cuál es la condición? a) compartir los apuntes b) estudiar", "a) compartir los apuntes", "Va después de if.")],
    [
        ("En una explicación oral, ¿qué palabra introduce una razón?", "because", "Because significa porque y da la razón."),
        ("¿Qué verbo se usa en el resultado de una condición?", "will", "If + presente, will + verbo."),
        ("¿Dónde va too en la oración?", "Al final", "Es el lugar habitual de too."),
    ],
    task("Trabaja con una persona de tu casa. Haz esta mini conversación con las frases dadas: tú preguntas «Why is the bread hard?» y la otra persona responde «Because it is old.» Luego dices una condición con If y una opción con or. Frases de apoyo: «If you put the bread in a bag, it will stay soft.» y «Do you want butter or jam?». Escribe tu diálogo de seis líneas y úsalo en voz alta.", "Why is the bread hard? — Because it is old. — If you put it in a bag, it will stay soft. — Do you want butter or jam? — Jam, please. — Me too.", ["incluye una pregunta con why y su respuesta con because", "formula una condición con if y will", "usa or y too correctamente"], ["diálogo escrito", "nota de la persona que escuchó"], ["usar will después de if", "poner too al principio"], "Reconoce lo que acertó y revisa con la persona dónde va cada conector."),
    "Explica en voz alta con first, second y finally cómo preparas un jugo.",
    "Escribe tres condiciones con if y will sobre lo que harás el fin de semana.",
)

# ---------------------------------------------------------------- clase 4: preguntas sobre rutinas y pasado
INTERV = "Entrevista de ejemplo: «Reporter: Does your neighbor cook? Student: No, he doesn't. He washes the dishes. Reporter: Did you cook yesterday? Student: Yes, I did. I made rice. Reporter: Do you and your friends play football? Student: Yes, we do, on Fridays. Reporter: Did your team win last week? Student: No, we didn't, but we had fun.» (rice = arroz, dishes = platos, made = preparé, win = ganar, had fun = nos divertimos)"
TABLE = "Tabla de ejemplo de la semana de Lucas. Lunes: lava los platos. Martes: lava los platos. Miércoles: cocina arroz. Jueves: lava los platos. Viernes: cocina pescado. (wash the dishes = lavar los platos, rice = arroz, fish = pescado)"
LIFE = "Conversación: «Maya: Do you walk to school? Ian: No, I don't. I take the bus. Maya: Does your sister take the bus too? Ian: Yes, she does. Maya: Did you take the bus yesterday? Ian: No, I didn't. I walked because it was sunny.» (take the bus = tomar el bus, sister = hermana, walked = caminé, sunny = soleado)"

lesson(
    OA10, 4,
    "Los diálogos y las tablas escritos en cada ejercicio, lápiz y una persona de tu casa para practicar.",
    "Aprenderé a formular y responder preguntas sobre rutinas y acciones presentes y pasadas con do, does y did, y a dar respuestas cortas (Yes, he does / No, he doesn't / Yes, I did / No, I didn't). Sirve para entrevistar a una persona y conversar sobre lo que hace y lo que hizo.",
    ["Sé el presente simple y el pasado simple.", "Conozco verbos como cook, walk y play."],
    [
        "Para preguntar por rutinas en presente se usa do o does + sujeto + verbo base: Do you walk to school? Does your sister take the bus? Do va con I, you, we y they; does va con he, she e it. Para responder de forma corta: Yes, I do / No, I don't; Yes, she does / No, she doesn't. Después de do y does, el verbo no cambia: Does he cook? (no cooks).",
        "Para preguntar por el pasado se usa did + sujeto + verbo base para todos los sujetos: Did you cook yesterday? Did your team win? La respuesta corta es Yes, I did / No, I didn't. Después de did, el verbo vuelve a la forma base, aunque sea irregular: Did she go? (no went). En las respuestas completas sí usas el pasado: Yes, she went.",
        "Para entrevistar a alguien, prepara tres preguntas en presente y dos en pasado. Escucha la respuesta y haz una pregunta de seguimiento con why o what: Why do you take the bus? Anota las respuestas en una tabla. Cuando respondas, usa respuestas cortas y agrega un detalle: «No, I didn't. I walked because it was sunny.» Así tu conversación suena más natural.",
    ],
    [("do / does", "auxiliares para preguntar en presente"), ("did", "auxiliar para preguntar en pasado"), ("Yes, she does", "respuesta corta afirmativa en presente"), ("No, I didn't", "respuesta corta negativa en pasado"), ("base form", "forma base del verbo"), ("follow-up question", "pregunta de seguimiento")],
    [
        ("Pregunta en presente", "Convierte en pregunta: «Your sister takes the bus.»", ["Con sister (she) se usa does.", "El verbo vuelve a la forma base: take.", "Queda Does your sister take the bus?"], "Does your sister take the bus?"),
        ("Respuesta corta en pasado", "Responde con una respuesta corta: «Did you cook yesterday?» Si no cocinaste.", ["La respuesta es negativa.", "Se usa didn't.", "Queda No, I didn't."], "No, I didn't."),
    ],
    [
        ("Decir «Does he cooks?».", "Se conjuga el verbo principal después de does.", "Después de does el verbo va en forma base: Does he cook?"),
        ("Responder «Yes, I cooked» a una pregunta corta.", "No se usa la forma corta esperada.", "La respuesta corta es Yes, I did."),
    ],
    [
        (INTERV + " ¿El vecino cocina? a) no b) sí", "a) no", "Dice No, he doesn't."),
        (LIFE + " ¿Ian camina al colegio normalmente? a) no, toma el bus b) sí, camina", "a) no, toma el bus", "Dice No, I don't. I take the bus."),
        (INTERV + " ¿Cocinó ayer? a) sí b) no", "a) sí", "Dice Yes, I did."),
    ],
    [
        (INTERV + " ¿Qué preparó ayer?", "Arroz", "Dice I made rice."),
        (LIFE + " ¿Su hermana toma el bus? a) sí b) no", "a) sí", "Dice Yes, she does."),
        (INTERV + " ¿Ganó el equipo la semana pasada? a) no b) sí", "a) no", "Dice No, we didn't."),
    ],
    [
        (TABLE + " Responde la pregunta «What does Lucas cook on Wednesdays?»", "Arroz", "En la tabla, el miércoles cocina arroz."),
        (TABLE + " ¿Cocinó Lucas el jueves? Responde con una respuesta corta. a) No, he didn't b) Yes, he did.", "a) No, he didn't.", "El jueves lavó los platos y no cocinó."),
        (LIFE + " ¿Por qué Ian caminó ayer?", "Porque estaba soleado", "Dice because it was sunny."),
    ],
    [
        (INTERV + " Elige la pregunta correcta. a) «Do you and your friends play football?» b) «Does you and your friends play football?»", "a) Do you and your friends play football?", "Con you y friends se usa do."),
        (LIFE + " Elige la pregunta correcta. a) «Did you take the bus yesterday?» b) «Did you took the bus yesterday?»", "a) Did you take the bus yesterday?", "Después de did el verbo va en forma base."),
    ],
    [
        (TABLE + " Escribe la pregunta que se responde con «Yes, he does»: «___ Lucas cook on Wednesdays?» Elige Does o Did.", "Does", "Es una rutina en presente con he."),
        (INTERV + " Una pregunta de seguimiento adecuada a «No, we didn't» es: a) «Why not?» b) «How much is it?»", "a) Why not?", "Pregunta la razón de la respuesta."),
    ],
    [("Entrevistas a un compañero. Preguntas: «Do you walk to school?» y «Did you walk yesterday?». Él responde: «Yes, I do. And yes, I did.» (walk = caminar). ¿Qué te dice? a) que camina habitualmente y que ayer también caminó b) que nunca camina", "a) que camina habitualmente y que ayer también caminó", "Responde en presente y en pasado afirmativamente.")],
    [
        ("En una entrevista oral, ¿qué auxiliar usas para preguntar por el pasado?", "did", "Va con todos los sujetos."),
        ("¿Qué respuesta corta es negativa en presente con she?", "No, she doesn't", "Doesn't es la forma negativa."),
        ("¿Qué forma tiene el verbo después de did?", "La forma base", "No lleva -ed ni forma irregular."),
    ],
    task("Entrevista a una persona de tu casa. Usa esta lista de preguntas ya dada: «Do you cook on Sundays?», «Does your friend call you every day?», «Did you watch TV yesterday?» y «Did you walk last weekend?». Anota las respuestas cortas (Yes, I do / No, I don't / Yes, I did / No, I didn't) en una tabla de dos columnas: pregunta y respuesta. Después agrega una pregunta de seguimiento con Why o What.", "Do you cook on Sundays? Yes, I do. Did you watch TV yesterday? No, I didn't. Why not? Because I was busy.", ["formula las cuatro preguntas correctamente", "anota las respuestas cortas", "agrega una pregunta de seguimiento"], ["tabla de dos columnas", "nota de la persona entrevistada"], ["decir «Did you watched»", "responder «Yes, I cooked» como respuesta corta"], "Reconoce lo que acertó y repasa con la persona el verbo base después de do, does y did."),
    "Prepara tres preguntas con does sobre un personaje de una serie o libro.",
    "Escribe una entrevista de seis líneas con un deportista imaginario usando do, does y did.",
)

# ---------------------------------------------------------------- clase 5: acciones interrumpidas, permiso y consejo
HOLIDAY = "Conversación: «Rita: Yesterday I was playing football in the yard when it started to rain. Pablo: While I was cycling, my friend was listening to music. Rita: Were you wet? Pablo: Yes, I was. Rita: You should wear a raincoat. Pablo: Can I borrow yours? Rita: Of course, you can.» (cycling = andando en bicicleta, listening = escuchando, wet = mojado, raincoat = impermeable, borrow = pedir prestado)"
DOCTOR = "Conversación de ejemplo en el consultorio (es ficticia y no es un consejo médico real): «Patient: I was sleeping when the pain started. Doctor: Does it hurt now? Patient: A little. Can I go to school tomorrow? Doctor: No, you can't. You should rest for two days. You shouldn't run or play football. Patient: Can I drink cold water? Doctor: Yes, you can, but you shouldn't drink it very fast.» (pain = dolor, hurt = doler, rest = descansar)"
PHONE2 = "Conversación: «Lía: I was talking with my friend when the bell rang. Teo: What were you doing at the library? Lía: I was reading a comic. Teo: Can I read it too? Lía: Yes, you can. You should return it before Friday. Teo: I will. Thanks!» (bell = timbre, rang = sonó, comic = historieta, return = devolver)"

lesson(
    OA10, 5,
    "Los diálogos escritos en cada ejercicio, lápiz y una persona de tu casa para practicar.",
    "Aprenderé a describir acciones que interrumpen u ocurren al mismo tiempo en el pasado (I was playing… when…; while he was cycling…) y a pedir permiso y dar consejo (Can I go out? / You shouldn't walk in the rain without an umbrella). Sirve para contar lo que pasaba, pedir permiso y aconsejar.",
    ["Sé el pasado simple y el pasado continuo.", "Conozco can y should."],
    [
        "El pasado continuo (past continuous) usa was o were + verbo con -ing: I was playing, they were listening. Se usa para una acción en desarrollo en el pasado. Con when se muestra una acción larga interrumpida por otra corta: I was playing football when it started to rain (la acción larga va en continuo y la que interrumpe, en pasado simple). Con while se muestran dos acciones que ocurrían a la vez: While he was cycling, she was listening to music.",
        "Para preguntar en pasado continuo se invierte el orden: Were you wet? What were you doing? Las respuestas cortas son Yes, I was / No, I wasn't; Yes, we were / No, we weren't. Para pedir permiso se usa Can I…? (¿puedo…?), y se responde Yes, you can / No, you can't. Para dar consejo se usa should y shouldn't: You should wear a raincoat; You shouldn't run.",
        "Al hablar, combina estas funciones para contar y aconsejar: «I was walking home when it started to rain. You shouldn't walk in the rain without an umbrella.» Fíjate en que después de can y should el verbo va en forma base, sin to. Practica con una persona: una cuenta qué hacía cuando algo ocurrió; la otra pide permiso o da un consejo.",
    ],
    [("was / were + -ing", "estaba / estaban haciendo"), ("when", "cuando: una acción interrumpe a otra"), ("while", "mientras: dos acciones a la vez"), ("Can I…?", "¿Puedo…?"), ("should / shouldn't", "debería / no debería"), ("advice", "consejo")],
    [
        ("Acción interrumpida", "Completa: «I was reading ___ the phone rang.» Elige when o while.", ["La acción corta interrumpe a la larga.", "Se usa when.", "Queda when the phone rang."], "when"),
        ("Dos acciones a la vez", "Completa: «___ I was cooking, he was washing the dishes.» Elige While o When.", ["Las dos acciones ocurren a la vez.", "Se usa while.", "Queda While I was cooking."], "While"),
    ],
    [
        ("Usar el pasado continuo para la acción corta: «It was starting to rain when I played».", "Se invierte el uso de los tiempos.", "La acción larga va en continuo y la corta en pasado simple."),
        ("Decir «Can I to go?».", "Se agrega to.", "Después de can va el verbo base: Can I go?"),
    ],
    [
        (HOLIDAY + " ¿Qué hacía Rita cuando empezó a llover? a) jugaba fútbol b) andaba en bicicleta", "a) jugaba fútbol", "Dice I was playing football when it started to rain."),
        (DOCTOR + " ¿Qué hacía el paciente cuando empezó el dolor? a) dormía b) estudiaba", "a) dormía", "Dice I was sleeping when the pain started."),
        (PHONE2 + " ¿Qué hacía Lía cuando sonó el timbre? a) conversaba con una amiga b) comía", "a) conversaba con una amiga", "Dice I was talking with my friend when the bell rang."),
    ],
    [
        (HOLIDAY + " ¿Qué hacía el amigo de Pablo mientras él andaba en bicicleta?", "Escuchaba música", "Dice my friend was listening to music."),
        (DOCTOR + " ¿Puede ir al colegio mañana? a) no b) sí", "a) no", "Dice No, you can't."),
        (PHONE2 + " ¿Qué leía Lía en la biblioteca? a) una historieta b) un diario", "a) una historieta", "Dice I was reading a comic."),
    ],
    [
        (HOLIDAY + " ¿Qué consejo da Rita? a) usar un impermeable b) quedarse en casa", "a) usar un impermeable", "Dice You should wear a raincoat."),
        (DOCTOR + " ¿Qué no debería hacer el paciente? a) correr o jugar fútbol b) descansar", "a) correr o jugar fútbol", "Dice You shouldn't run or play football."),
        (PHONE2 + " ¿Cuándo debe devolver el cómic Teo? a) antes del viernes b) después del lunes", "a) antes del viernes", "Dice return it before Friday."),
    ],
    [
        (HOLIDAY + " Pablo pide prestado el impermeable. ¿Cuál es la respuesta de Rita? a) Of course, you can b) No, you can't.", "a) Of course, you can.", "Acepta el permiso."),
        (DOCTOR + " ¿Qué permiso se niega? a) ir al colegio mañana b) beber agua fría", "a) ir al colegio mañana", "El médico dice No, you can't."),
    ],
    [
        (PHONE2 + " Completa la pregunta: «What ___ you doing at the library?» Elige were o was.", "were", "You se usa con were."),
        (DOCTOR + " Un compañero dice: «You should rest and you shouldn't run». ¿Son dos consejos? Responde sí o no.", "Sí", "Uno afirmativo y uno negativo."),
    ],
    [("Hablas con tu compañero: «I was walking to school when I saw a friend.» (saw = vi). ¿Cuál fue la acción larga? a) caminaba al colegio b) ver a un amigo", "a) caminaba al colegio", "Was walking indica una acción en desarrollo.")],
    [
        ("¿Qué forma se usa para una acción larga en el pasado?", "was o were + -ing", "Es el pasado continuo."),
        ("Al hablar con alguien, ¿cómo pides permiso en inglés?", "Can I…?", "Se responde Yes, you can o No, you can't."),
        ("¿Qué palabra introduce un consejo?", "should", "Dice qué sería bueno hacer."),
    ],
    task("Trabaja con una persona de tu casa. Cuéntale en inglés dos cosas que ocurrieron: una con when y una con while. Frases de apoyo ya dadas: «I was watching a film when the light went out.» y «While I was cooking, my friend was setting the table.» Luego pide permiso con Can I…? y que ella te dé un consejo con should. Escribe un diálogo de seis líneas.", "I was washing my hands when the phone rang. — Can I answer it? — Yes, you can. — While I was talking, you were writing. — You should write the message.", ["usa when y while correctamente", "pide un permiso con Can I…?", "recibe un consejo con should o shouldn't"], ["diálogo escrito", "nota de la persona que escuchó"], ["usar pasado simple para la acción larga", "agregar to después de can"], "Reconoce lo que acertó y revisa con la persona qué acción es larga y cuál interrumpe."),
    "Cuenta tres cosas que estabas haciendo ayer a las 5 de la tarde.",
    "Escribe tres consejos con should y shouldn't para alguien que se enfermó.",
)

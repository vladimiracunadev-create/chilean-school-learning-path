"""Cuaderno del estudiante, 2.º medio Inglés (propuesta), EN2M OA 05: lectura de textos con las funciones del año.

Textos originales y ficticios, con pista en español. Los títulos de clase del plan son genéricos; aquí cada clase interpreta
un grupo de funciones del OA en textos breves: frecuencia, grado y tiempo; acciones anteriores en el pasado (past perfect);
lugares, oficios y personas; confirmar, sugerir, ofrecer y opinar; y conectar ideas, enfatizar quién actúa e informar lo que otros dicen.
"""
from __future__ import annotations

from en_m2_a_common import MAT_READ, arith, lesson, task

OA = "EN2M OA 05"

# ================================================== clase 1: frecuencia, grado y tiempo
SURVEY = "«Interview with Nico, a student who runs a school podcast.\nQ: How often do you record a new episode? A: Usually once a week, on Thursdays. Q: How often do you practise your voice? A: Almost every day, for ten minutes. Q: Do you ever miss a recording? A: Hardly ever, but last month I missed one because I was ill. Q: Is the work difficult? A: It is rather difficult at the beginning, but I am getting better. Q: When will the next episode be ready? A: Soon, probably on Wednesday.»\n(record = grabar, episode = episodio, practise = practicar, voice = voz, miss = faltar, ill = enfermo, rather = bastante, beginning = comienzo, ready = listo)"
FLYER = "«Weekend Routine of Camila (fictional): Camila always wakes up at eight on Saturdays. She often cycles to the park, and she sometimes meets her friends for a snack. She never watches television in the morning. She is quite tired on Sunday evenings, so she goes to bed early.»\n(wakes up = se despierta, cycles = anda en bicicleta, snack = merienda, tired = cansada, early = temprano)"
GYM = "«Club notice: The climbing club meets twice a week. We practise at least two hours each session. Beginners are very welcome, but the wall is too high for children under twelve. The new route will be open soon.» (climbing = escalada, wall = muro, high = alto, route = ruta, beginners = principiantes)"

lesson(
    OA, 1, MAT_READ,
    "Aprenderé a leer textos que piden o describen la frecuencia de actividades, y que indican el grado y el tiempo de las acciones. Sirve para entender cuántas veces ocurre algo, qué tan intenso es y cuándo ocurrirá.",
    ["Sé el presente simple.", "Sé los días de la semana y las horas."],
    [
        "Para pedir información sobre frecuencia (frequency), se usa How often…? Se responde con adverbios de frecuencia: always (siempre), usually (por lo general), often (a menudo), sometimes (a veces), hardly ever (casi nunca) y never (nunca). También se usan expresiones como once a week (una vez por semana), twice a month (dos veces al mes) y every day (cada día). Los adverbios suelen ir antes del verbo, pero después del verbo to be: She is always on time.",
        "Para describir el grado (degree) de una acción o cualidad se usan palabras como very, quite, rather, too y enough. Rather difficult significa «bastante difícil»; too high significa «demasiado alto»; high enough significa «suficientemente alto». Estas palabras muestran cuánta intensidad tiene una acción o una cualidad, y ayudan a entender la opinión del autor.",
        "Para describir el tiempo (time) se usan soon (pronto), at the beginning (al comienzo), during the summer (durante el verano), last month (el mes pasado) y for ages (por mucho tiempo). Al leer, subraya estas expresiones y pregúntate: ¿cada cuánto?, ¿qué tan intenso? y ¿cuándo? Así encuentras datos exactos sin traducir cada palabra.",
    ],
    [("how often", "con qué frecuencia"), ("always", "siempre"), ("usually", "por lo general"), ("hardly ever", "casi nunca"), ("rather", "bastante"), ("too", "demasiado"), ("enough", "suficiente"), ("soon", "pronto")],
    [
        ("Frecuencia", "Lee: «I hardly ever eat late at night.» ¿Cuál es la frecuencia? A) casi nunca B) casi siempre", ["Hardly ever es una frecuencia baja.", "Significa casi nunca.", "Entonces come tarde muy rara vez."], "A) casi nunca"),
        ("Grado", "Lee: «The box is too heavy for me.» ¿Qué significa too heavy? A) demasiado pesada B) un poco pesada", ["Too indica exceso.", "Demasiado pesada.", "No puede levantarla."], "A) demasiado pesada"),
    ],
    [
        ("Traducir hardly ever como casi siempre.", "Hardly parece «duro» o «fuerte» y se pierde su sentido de poco.", "Recuerda que hardly ever es casi nunca."),
        ("Confundir too (demasiado) con very (muy).", "Too indica exceso que causa un problema; very solo indica intensidad.", "Pregunta si el exceso es un problema."),
    ],
    [
        ("Lee: " + SURVEY + " ¿Cada cuánto graba Nico un episodio nuevo? A) una vez por semana B) todos los días", "A", "Dice Usually once a week, on Thursdays."),
        ("Lee: " + FLYER + " ¿A qué hora se despierta Camila los sábados? A) a las ocho B) a las siete", "A", "Dice always wakes up at eight on Saturdays."),
        ("Lee: " + GYM + " ¿Cuántas veces por semana se reúne el club de escalada? A) dos B) siete", "A", "El texto dice twice a week."),
    ],
    [
        ("Lee: " + SURVEY + " ¿Cuánto practica su voz al día? A) diez minutos B) una hora", "A", "Dice almost every day, for ten minutes."),
        ("Lee: " + FLYER + " ¿Qué nunca hace Camila en la mañana? A) ver televisión B) andar en bicicleta", "A", "Dice She never watches television in the morning."),
        ("Lee: " + GYM + " ¿Por qué los menores de doce no pueden usar el muro? A) porque es demasiado alto B) porque es muy caro", "A", "Dice the wall is too high for children under twelve."),
    ],
    [
        ("Lee: " + SURVEY + " ¿Con qué frecuencia falta Nico a una grabación? A) casi nunca B) siempre", "A", "Responde Hardly ever."),
        ("Lee: " + FLYER + " ¿Cómo está Camila los domingos en la tarde? A) bastante cansada B) muy enérgica", "A", "El texto dice quite tired on Sunday evenings."),
        arith("Según el club de escalada, cada sesión dura al menos dos horas y se hace dos veces por semana. ¿Cuántas horas como mínimo practica una persona en cuatro semanas?", "2*2*4", "Se multiplican horas, sesiones por semana y semanas."),
    ],
    [
        ("Lee: " + SURVEY + " Nico dice que el trabajo fue rather difficult al comienzo. ¿Qué interpreta el lector? A) que fue bastante difícil, pero mejora B) que es imposible", "A", "Rather difficult significa bastante difícil y dice I am getting better."),
        ("Lee: " + FLYER + " ¿Por qué se acuesta temprano los domingos? A) porque está bastante cansada B) porque se levanta tarde", "A", "El texto usa so: está cansada, por eso se acuesta temprano."),
    ],
    [
        ("Lee: " + SURVEY + " ¿Cuándo estará listo el próximo episodio? A) pronto, probablemente el miércoles B) el jueves", "A", "Dice Soon, probably on Wednesday."),
        ("Lee: " + GYM + " Ordena de menor a mayor frecuencia: a) never b) sometimes c) always", "a, b, c", "Never es 0, sometimes es de vez en cuando y always es siempre."),
    ],
    [("Lee: «Marta goes to the library twice a week, and she always borrows two books. Last month she was too busy to go.» (borrows = pide prestado, busy = ocupada). ¿Cuántos libros se lleva en una semana?", "4", "Va dos veces y se lleva dos libros cada vez: 2 por 2 son 4.")],
    [
        ("¿Cómo se pregunta por la frecuencia en inglés?", "How often…?", "Pide cada cuánto ocurre algo."),
        ("¿Qué significa too?", "Demasiado", "Indica un exceso."),
        ("¿Dónde va el adverbio de frecuencia en una oración con to be?", "Después del verbo to be", "She is always on time."),
    ],
    task("Lee este texto original: «Hugo plays the guitar. He practises every day for half an hour, and on Saturdays he practises for two hours. He rarely misses a class. His guitar is old, but it sounds nice enough. He will play in a concert soon.» (guitar = guitarra, rarely = rara vez, sounds = suena, concert = concierto). En tu hoja escribe tres preguntas con How often o When y sus respuestas, usando datos del texto.", "Ejemplos: How often does he practise? Every day, half an hour. How often does he practise on Saturdays? Two hours. When will he play? Soon, in a concert.", ["escribe tres preguntas completas", "las respuestas coinciden con el texto", "usa al menos un adverbio de frecuencia"], ["hoja con tres preguntas y respuestas"], ["usar datos que no están en el texto", "cambiar half an hour por una hora"], "Pide a una persona de tu casa que responda tus preguntas sin mirar el texto y compara."),
    "Relee la rutina de Camila y subraya todos los adverbios de frecuencia.",
    "Escribe cinco oraciones sobre tu semana con always, usually, often, sometimes, hardly ever o never.",
)

# ================================================== clase 2: acciones anteriores a otra en el pasado
DIARY = "«Diary of Ema, Saturday. When I arrived at the station, the train had already left. I looked at my phone and I saw a message from Julia. She had written: ‘I have lost my ticket.’ By the time I called her, she had found it under a seat. We laughed because we had both made the same mistake: we had forgotten to check the time.»\n(station = estación, left = salió, ticket = pasaje, seat = asiento, laughed = nos reímos, mistake = error, check = revisar)"
STORY5 = "«Leo was hungry because he had not eaten breakfast. He opened the fridge, but his brother had finished the milk. Then Leo remembered that he had bought bread the day before. He made a sandwich and felt better.»\n(hungry = con hambre, fridge = refrigerador, finished = terminó, remembered = recordó, bought = compró, the day before = el día anterior)"
NOTE5 = "«Note from the librarian: When students came in this morning, the room was ready. We had moved the tables, and we had put new posters on the wall. After the students left, we cleaned the floor.»\n(moved = movimos, posters = afiches, wall = muro, floor = piso)"

lesson(
    OA, 2, MAT_READ,
    "Aprenderé a reconocer en un texto las acciones que ocurrieron antes que otra acción en el pasado, con el pasado perfecto (had + participio). Sirve para ordenar los hechos de una historia y entender qué pasó primero.",
    ["Sé el pasado simple de verbos regulares e irregulares.", "Sé ordenar hechos con first, then y after."],
    [
        "Cuando se cuentan dos hechos del pasado, el pasado perfecto (past perfect) muestra cuál ocurrió primero. Se forma con had + participio: had left, had written, had lost. El hecho que ocurrió antes va en pasado perfecto, y el que ocurrió después va en pasado simple. Por ejemplo, When I arrived, the train had already left: primero salió el tren y después llegué yo.",
        "Algunos verbos tienen participio regular (-ed): finished, moved, cleaned. Otros son irregulares: lost, eaten, bought, found, forgotten, written. Las palabras already (ya), by the time (cuando…), before (antes), after (después) y the day before (el día anterior) son señales de este tiempo. La forma negativa es had not (hadn’t), como en he had not eaten breakfast.",
        "Para ordenar los hechos al leer, escribe una línea de tiempo con dos puntos: primero (past perfect) y después (past simple). Pregúntate: ¿qué pasó antes?, ¿qué pasó después? y ¿cuál explica a cuál? A menudo la acción anterior es la causa, como en He didn’t have money because he had lost his wallet.",
    ],
    [("past perfect", "pasado perfecto: had + participio"), ("had left", "había salido"), ("already", "ya"), ("by the time", "para cuando"), ("the day before", "el día anterior"), ("hadn’t", "no había")],
    [
        ("Orden de hechos", "Lee: «When she arrived, the class had started.» ¿Qué ocurrió primero? A) la clase empezó B) ella llegó", ["Had started está en pasado perfecto.", "El pasado perfecto va primero.", "La clase empezó antes de que llegara."], "A) la clase empezó"),
        ("Participio", "¿Cuál es el participio de lose en had ___ a pen? A) lost B) loosed", ["Lose es irregular.", "Su participio es lost.", "Had lost a pen."], "A) lost"),
    ],
    [
        ("Decir When I arrived, the train left para expresar que el tren ya se había ido.", "El pasado simple no muestra que el tren salió antes.", "Usa had left para el hecho anterior."),
        ("Escribir had + verbo en pasado simple (had saw).", "Después de had va el participio.", "Escribe had seen."),
    ],
    [
        ("Lee: " + DIARY + " ¿Qué había pasado con el tren al llegar Ema? A) ya había salido B) llegó retrasado", "A", "Dice the train had already left."),
        ("Lee: " + STORY5 + " ¿Por qué tenía hambre Leo? A) no había desayunado B) había comido mucho", "A", "Dice he had not eaten breakfast."),
        ("Lee: " + NOTE5 + " ¿Qué habían hecho antes de que llegaran los estudiantes? A) mover las mesas B) limpiar el piso", "A", "Dice We had moved the tables."),
    ],
    [
        ("Lee: " + DIARY + " ¿Qué había escrito Julia? A) que había perdido su pasaje B) que había llegado al tren", "A", "Dice I have lost my ticket."),
        ("Lee: " + STORY5 + " ¿Qué había terminado el hermano de Leo? A) la leche B) el pan", "A", "Dice his brother had finished the milk."),
        ("Lee: " + NOTE5 + " ¿Qué se hizo después de que se fueron los estudiantes? A) se limpió el piso B) se movieron las mesas", "A", "Dice After the students left, we cleaned the floor."),
    ],
    [
        ("Lee: " + DIARY + " ¿Qué error habían cometido las dos amigas? A) habían olvidado revisar la hora B) habían perdido la aplicación", "A", "Dice we had both made the same mistake: we had forgotten to check the time."),
        ("Lee: " + STORY5 + " ¿Cuándo había comprado Leo el pan? A) el día anterior B) esa mañana", "A", "Dice the day before."),
        ("Completa con el participio correcto: «She had ___ her homework before dinner.» A) finished B) finish", "A", "Después de had va el participio finished."),
    ],
    [
        ("Lee: " + DIARY + " Ordena los hechos: a) Julia encontró su pasaje b) Ema llamó a Julia c) Julia perdió su pasaje", "c, a, b", "By the time I called her, she had found it, por lo que primero lo perdió y luego lo encontró."),
        ("Lee: " + STORY5 + " Un compañero dice que Leo comió pan porque había vaciado el refrigerador. ¿Qué dato corrige? A) la leche la había terminado su hermano B) Leo comió pan sin hambre", "A", "El texto indica que el hermano terminó la leche, no Leo."),
    ],
    [
        ("Lee: " + NOTE5 + " Ordena: a) llegaron los estudiantes b) se pusieron afiches nuevos c) se limpió el piso", "b, a, c", "Primero prepararon la sala, luego llegaron y después limpiaron."),
        ("Lee: «Pedro was late because he had missed the bus.» ¿Qué hecho explica el atraso? A) perder el bus B) llegar tarde", "A", "Had missed ocurrió antes y es la causa."),
    ],
    [("Lee: «By the time the film started, Sara had already bought popcorn, and her friends had saved three seats.» (popcorn = cabritas, saved = guardaron, seats = asientos). ¿Cuántos asientos habían guardado sus amigos?", "3", "El texto dice three seats.")],
    [
        ("¿Cómo se forma el pasado perfecto?", "Had + participio", "Muestra la acción que ocurrió primero."),
        ("¿Qué significa already?", "Ya", "Es una señal de pasado perfecto."),
        ("¿Cuál es el participio de forget?", "Forgotten", "Es un participio irregular."),
    ],
    task("Lee: «Tina couldn’t open the door because she had left her keys at home. She called her brother, who had just arrived from school. He had brought a spare key, so they entered together.» (keys = llaves, brother = hermano, spare = de repuesto, entered = entraron). En tu hoja haz una línea de tiempo con estos tres hechos en orden: Tina llamó a su hermano; Tina dejó las llaves en casa; entraron juntos. Subraya además los verbos en pasado perfecto.", "Orden: 1) Tina dejó las llaves en casa (had left); 2) Tina llamó a su hermano, que acababa de llegar y llevaba una llave de repuesto (had just arrived, had brought); 3) entraron juntos. Verbos: had left, had just arrived, had brought.", ["ordena tres hechos correctos", "subraya had left, had arrived y had brought", "explica qué pasó primero"], ["hoja con línea de tiempo"], ["poner had bring en vez de had brought", "ordenar al revés los hechos"], "Lee tu línea de tiempo a una persona de tu casa y verifica que entienda qué pasó primero."),
    "Escribe tres oraciones con had + participio sobre lo que habías hecho antes de venir al colegio hoy.",
    "Reescribe en español la historia de Tina con un orden distinto y explica qué cambia.",
)

# ================================================== clase 3: lugares, ocupaciones y personas
PLACE = "«The Central Market is very busy on Saturdays. It is crowded from nine to noon, and the stalls sell fruit, bread and flowers. The old clock tower is a famous landmark. The market is interesting for tourists because it has many colours and sounds.» (busy = concurrido, crowded = lleno de gente, stalls = puestos, clock tower = torre del reloj, landmark = punto de referencia, tourists = turistas)"
JOBS = "«Rosa is a paramedic. She is good at staying calm and she is interested in helping people. Her colleague, Mario, is a very organised nurse: he is always prepared and never loses a document. Their work is tiring, but it is also rewarding.» (paramedic = paramédica, calm = tranquila, helping = ayudar, colleague = colega, organised = organizado, nurse = enfermero, prepared = preparado, tiring = agotador, rewarding = gratificante)"
COURT = "«This is the sports centre of our neighbourhood. There is a basketball court with new lines, a small gym and a café. The court is quiet in the morning but noisy after school.» (sports centre = centro deportivo, court = cancha, lines = líneas, noisy = ruidoso, quiet = tranquila)"

lesson(
    OA, 3, MAT_READ,
    "Aprenderé a leer descripciones de lugares, ocupaciones y personas e identificar sus cualidades, usando adjetivos y estructuras como good at, interested in y very busy. Sirve para entender cómo se describe algo con detalle.",
    ["Sé usar adjetivos como big, small y old.", "Sé el verbo to be."],
    [
        "Para describir un lugar se usan adjetivos de estado: busy (concurrido), crowded (lleno de gente), quiet (tranquilo), noisy (ruidoso) y famous (famoso). Se dice It is very busy y no It has very busy. También se nombra el tipo de lugar con un sustantivo compuesto: a basketball court (cancha de básquetbol), a clock tower (torre del reloj), a sports centre (centro deportivo).",
        "Para describir ocupaciones y personas se usan sustantivos de oficio (paramedic, nurse, teacher) y adjetivos de cualidad (organised, calm, friendly). Con la preposición correcta se explica una habilidad o un interés: She is good at staying calm (se le da bien…), She is interested in helping people (le interesa…). Interested describe cómo se siente una persona; interesting describe lo que causa ese interés: The market is interesting, the tourist is interested.",
        "La terminación -ed describe cómo se siente alguien (tired, bored, excited) y -ing describe lo que produce ese sentimiento (tiring, boring, exciting). Por eso decimos The work is tiring y I am tired. Al leer una descripción, subraya los adjetivos, pregúntate si hablan de un lugar o de una persona y busca la evidencia en el texto.",
    ],
    [("busy", "concurrido; ocupado"), ("crowded", "lleno de gente"), ("good at", "bueno para"), ("interested in", "interesado en"), ("organised", "organizado"), ("court", "cancha")],
    [
        ("-ed o -ing", "Completa: «The film is ___.» A) boring B) bored", ["La película produce el sentimiento.", "Se usa -ing.", "Boring."], "A) boring"),
        ("Cualidad de una persona", "Lee: «Ana is good at drawing.» ¿Qué muestra good at? A) que dibuja bien B) que le gusta dormir", ["Good at indica habilidad.", "Se le da bien dibujar.", "Dibuja bien."], "A) que dibuja bien"),
    ],
    [
        ("Decir I am interesting cuando se quiere decir «estoy interesado».", "Interesting describe lo que causa interés, no el sentimiento de quien lo siente.", "Usa I am interested in…"),
        ("Usar good in en vez de good at.", "Con habilidades se usa la preposición at.", "Recuerda good at + sustantivo o verbo con -ing."),
    ],
    [
        ("Lee: " + PLACE + " ¿Cuándo está lleno de gente el mercado? A) de nueve a mediodía B) por la tarde", "A", "Dice crowded from nine to noon."),
        ("Lee: " + JOBS + " ¿Qué trabajo tiene Rosa? A) paramédica B) enfermera", "A", "Dice Rosa is a paramedic."),
        ("Lee: " + COURT + " ¿Cuándo está tranquila la cancha? A) en la mañana B) después del colegio", "A", "Dice quiet in the morning."),
    ],
    [
        ("Lee: " + PLACE + " ¿Por qué es interesante para los turistas? A) porque tiene muchos colores y sonidos B) porque es barato", "A", "Dice many colours and sounds."),
        ("Lee: " + JOBS + " ¿En qué es buena Rosa? A) en mantener la calma B) en escribir informes", "A", "Dice good at staying calm."),
        ("Lee: " + COURT + " ¿Qué hay en el centro deportivo? A) una cancha, un gimnasio pequeño y una cafetería B) una piscina", "A", "El texto nombra court, gym y café."),
    ],
    [
        ("Lee: " + JOBS + " ¿Cómo es Mario como enfermero? A) muy organizado B) lento", "A", "Dice a very organised nurse."),
        ("Lee: " + PLACE + " ¿Qué es la torre del reloj? A) un punto de referencia famoso B) un puesto de flores", "A", "Dice The old clock tower is a famous landmark."),
        ("Completa: «The students are ___ in the new robot.» A) interested B) interesting", "A", "Interested describe a quienes sienten interés."),
    ],
    [
        ("Lee: " + JOBS + " ¿Qué dos adjetivos describen el trabajo? A) agotador y gratificante B) aburrido y fácil", "A", "Dice tiring y rewarding."),
        ("Lee: " + COURT + " ¿Qué muestra after school? A) cuándo está ruidosa la cancha B) cuándo cierra", "A", "Dice noisy after school."),
    ],
    [
        ("Une cada oración con su descripción. 1) She is a very organised person. 2) The market is crowded. 3) He is good at chess. Opciones: a) lugar con mucha gente b) habilidad c) cualidad de una persona", "1-c, 2-a, 3-b", "Organised es cualidad, crowded describe el lugar y good at muestra habilidad."),
        ("Lee: «The bus is full, so Tomás is standing.» ¿Qué palabra sugiere que no hay asientos? A) full B) standing", "A", "Full indica que no queda espacio."),
    ],
    [("Lee: «Elena is a librarian. She is good at finding books quickly, and she is interested in old maps. The library is quiet and bright, with six large tables.» (librarian = bibliotecaria, maps = mapas, bright = luminosa, tables = mesas). ¿Cuántas mesas hay?", "6", "Dice six large tables.")],
    [
        ("¿Qué preposición va con good (en Inglés, 2.º medio)?", "At", "Se dice good at."),
        ("¿Qué diferencia hay entre interested e interesting?", "Interested es quien siente; interesting es lo que produce interés", "Se aplican a distintos sujetos."),
        ("¿Qué significa crowded?", "Lleno de gente", "Describe un lugar."),
    ],
    task("Lee: «Mr. Torres is a bus driver. He is very patient and he is good at driving in heavy traffic. He is interested in old cars. The bus station is busy in the morning and quiet at night.» (driver = conductor, patient = paciente, heavy traffic = mucho tráfico, station = terminal). En tu hoja escribe tres descripciones: del trabajo de Mr. Torres, de su carácter y del lugar, cada una con un adjetivo y una frase del texto como evidencia.", "Trabajo: bus driver, good at driving in heavy traffic. Carácter: very patient. Lugar: bus station, busy in the morning y quiet at night.", ["identifica tres adjetivos o frases correctas", "usa evidencia del texto", "no mezcla persona y lugar"], ["hoja con tres descripciones"], ["decir que la estación es paciente", "escribir un adjetivo que no aparece"], "Muestra tus descripciones a una persona de tu casa y verifica si coinciden con el texto."),
    "Subraya en el texto de Rosa y Mario todos los adjetivos que terminan en -ed o -ing.",
    "Escribe una descripción de cinco oraciones de un lugar de tu barrio y de la ocupación de alguien que trabaja allí.",
)

# ================================================== clase 4: confirmar, sugerir, ofrecer, acuerdo y desacuerdo
CHAT1 = "«Tina: It’s a lovely day, isn’t it? Ben: Yes, it is. Tina: You don’t eat meat, do you? Ben: No, I’m vegetarian. Tina: Your sister plays the violin, doesn’t she? Ben: Yes, she does. She will perform on Friday, won’t she? Tina: I think so.»\n(lovely = lindo, vegetarian = vegetariano, perform = presentarse)"
CHAT2 = "«Sofia: I’m tired. I can’t finish this poster. Dani: Shall I help you? I can bring the markers. Sofia: Would you like to work together? Dani: Yes. You ought to rest first, though. Sofia: I agree. I’ll take a short break. Dani: How about doing it at five? Sofia: That’s a good idea.»\n(markers = plumones, break = descanso, though = sin embargo)"
FORUM = "«Forum: Should school start later?\nAna: I agree with the idea because teenagers are tired in the morning. Beto: I disagree. If school starts later, it ends later. Carla: I agree with Beto, but I also think the break should be longer.»\n(forum = foro, later = más tarde, ends = termina, break = recreo, longer = más largo)"

lesson(
    OA, 4, MAT_READ,
    "Aprenderé a leer diálogos y foros que confirman información con tag questions, que hacen sugerencias, ofrecimientos y solicitudes, y que expresan acuerdo o desacuerdo. Sirve para entender lo que cada persona quiere o piensa.",
    ["Sé el verbo to be y el presente simple.", "Sé decir I think y I like."],
    [
        "Para confirmar información (confirm information) se usan preguntas de cola (tag questions). Si la frase es afirmativa, la cola es negativa: It’s nice, isn’t it? Si la frase es negativa, la cola es afirmativa: You don’t eat meat, do you? El auxiliar de la cola es el mismo de la frase: She plays, doesn’t she? She will come, won’t she? Your brother wasn’t at school, was he? Se responde con Yes, it is o No, I don’t.",
        "Para ofrecer ayuda se usa Shall I…? (¿Quieres que…?) o Would you like…? (¿Te gustaría…?). Para sugerir se usa You ought to… (deberías), How about…? (¿Qué tal…?) o Let’s… (hagamos…). Para hacer solicitudes se usa Could you…? Para expresar acuerdo se usa I agree with…; para desacuerdo, I disagree with… o I don’t think so. Se completa con because para dar la razón.",
        "Al leer un diálogo, fíjate en quién ofrece, quién sugiere y quién acepta. Las respuestas como That’s a good idea o I agree muestran acuerdo. Un but o un though suele marcar que el hablante agrega una condición. Las colas se leen con la voz subiendo cuando se hace una pregunta real, y bajando cuando solo se busca acuerdo.",
    ],
    [("tag question", "pregunta de cola: confirma información"), ("Shall I…?", "¿Quieres que yo…?"), ("Would you like…?", "¿Te gustaría…?"), ("ought to", "deberías"), ("I agree with", "estoy de acuerdo con"), ("I disagree with", "no estoy de acuerdo con")],
    [
        ("Cola correcta", "Completa: «You like pizza, ___?» A) don’t you B) do you", ["La frase es afirmativa.", "La cola es negativa.", "Don’t you."], "A) don’t you"),
        ("Ofrecimiento", "¿Cuál frase ofrece ayuda? A) Shall I carry your bag? B) You ought to sleep more.", ["Shall I pregunta si puedo hacer algo.", "Eso es ofrecer.", "La otra frase es una sugerencia."], "A"),
    ],
    [
        ("Usar una cola afirmativa después de una frase afirmativa (She plays, does she?).", "La cola debe ser opuesta a la frase.", "Cambia la polaridad: afirmativa y cola negativa."),
        ("Confundir Shall I (ofrecer) con You ought to (sugerir).", "Una ofrece ayuda y la otra da un consejo.", "Pregunta si quien habla hará algo o aconsejará algo."),
    ],
    [
        ("Lee: " + CHAT1 + " ¿Qué instrumento toca la hermana de Ben? A) el violín B) la guitarra", "A", "Dice Your sister plays the violin."),
        ("Lee: " + CHAT2 + " ¿Qué ofrece traer Dani? A) los plumones B) la comida", "A", "Dice I can bring the markers."),
        ("Lee: " + FORUM + " ¿Quién está de acuerdo con empezar más tarde? A) Ana B) Beto", "A", "Ana dice I agree with the idea."),
    ],
    [
        ("Lee: " + CHAT1 + " ¿Qué dice Ben que no come? A) carne B) verduras", "A", "Tina pregunta You don’t eat meat y Ben responde que es vegetariano."),
        ("Lee: " + CHAT2 + " ¿Qué sugerencia hace Dani a Sofia? A) descansar primero B) cancelar el afiche", "A", "Dice You ought to rest first."),
        ("Lee: " + FORUM + " ¿Qué razón da Beto para estar en desacuerdo? A) que el colegio terminaría más tarde B) que los estudiantes no estudian", "A", "Dice If school starts later, it ends later."),
    ],
    [
        ("Lee: " + CHAT1 + " ¿Cuándo se presentará la hermana? A) el viernes B) el sábado", "A", "Dice She will perform on Friday."),
        ("Lee: " + CHAT2 + " ¿A qué hora proponen hacer el afiche? A) a las cinco B) a las seis", "A", "Dice How about doing it at five?"),
        ("Lee: " + FORUM + " Carla está de acuerdo con Beto pero agrega una idea. ¿Cuál? A) que el recreo sea más largo B) que se empiece más temprano", "A", "Dice the break should be longer."),
    ],
    [
        ("Lee: " + CHAT2 + " ¿Qué muestra la frase That’s a good idea? A) acuerdo B) desacuerdo", "A", "Sofia acepta la propuesta de la hora."),
        ("Lee: " + FORUM + " ¿Cuántas personas están a favor de empezar más tarde? A) una, Ana B) tres", "A", "Ana está a favor; Beto está en contra; Carla coincide con Beto."),
    ],
    [
        ("Completa con la cola: «They don’t live here, ___?» A) do they B) don’t they", "A", "La frase es negativa y la cola es afirmativa."),
        ("Une cada frase con su función. 1) Shall I open the window? 2) You ought to talk to him. 3) I disagree with you. Funciones: a) sugerencia b) desacuerdo c) ofrecimiento", "1-c, 2-a, 3-b", "Shall I ofrece; ought to sugiere; disagree expresa desacuerdo."),
    ],
    [("Lee: «Mia: This website is useful, isn’t it? Leo: Yes, but it is a bit slow. Mia: Shall I send you the link? Leo: Yes, please.» (website = sitio web, link = enlace). ¿Qué ofrece Mia?", "Enviar el enlace", "Shall I send you the link? es un ofrecimiento.")],
    [
        ("¿Cómo se forma una cola si la frase es afirmativa?", "Con el auxiliar en negativo", "It is nice, isn’t it?"),
        ("¿Qué significa I disagree with…?", "No estoy de acuerdo con…", "Expresa un desacuerdo."),
        ("¿Qué expresa Would you like…?", "Un ofrecimiento", "Pregunta si quiero algo."),
    ],
    task("Lee este foro original: «Topic: A video game club after school. Rita: I think it is a good idea because many students like games. Hugo: I disagree. Games take too much time, don’t they? Rita: Yes, they do, but we could play for one hour only. Hugo: Shall I ask the teacher if the library is free? Rita: That would be great.» (video game = videojuego, club = club, free = libre). En tu hoja escribe: quién está de acuerdo y quién no, una cola, una oferta y la razón de Hugo.", "Rita está de acuerdo; Hugo no. Cola: Games take too much time, don’t they? Oferta: Shall I ask the teacher if the library is free? Razón de Hugo: los juegos toman demasiado tiempo.", ["identifica acuerdo y desacuerdo", "señala una cola y una oferta", "da la razón de Hugo"], ["hoja con cuatro respuestas"], ["decir que Rita rechaza la idea", "no citar la cola"], "Subraya en el texto con distintos colores cada función."),
    "Escribe diez colas con distintos auxiliares y revísalas con la regla de polaridad.",
    "Escribe un diálogo de seis líneas con una oferta, una sugerencia, una cola y un desacuerdo cortés.",
)

# ================================================== clase 5: conectar ideas, enfatizar y reportar
BLOG = "«Neither my brother nor I like football, so we started a chess club. We built the board ourselves. At first, the club was small, though every week more students joined. As a result, we needed a bigger room. As soon as the principal heard about it, he gave us the library. Unless we find new boards, we cannot grow more.»\n(started = empezamos, built = construimos, board = tablero, joined = se unieron, bigger = más grande, principal = director, grow = crecer)"
REPORT = "«Mrs. Lara said that the trip was cancelled because of the weather. She told us to bring our books on Monday, and she asked if we had finished the project. Carlos said that he had already sent it. Lucía told me to wait outside.»\n(cancelled = cancelado, weather = clima, bring = traer, finished = terminado, sent = enviado, wait outside = esperar afuera)"
CAKE = "«Did you make the cake yourself? Yes, I did it myself, but my mother helped me with the oven. My cousin cut himself while slicing the bread, so he had to rest. The twins painted the room themselves.»\n(cake = torta, oven = horno, cut = cortó, slicing = rebanando, rest = descansar, twins = mellizos, painted = pintaron)"

lesson(
    OA, 5, MAT_READ,
    "Aprenderé a leer textos que conectan ideas con neither…nor, either…or, though, unless, as soon as y as a result, que enfatizan quién realiza la acción con pronombres reflexivos, y que informan lo que otros dicen. Sirve para entender relaciones y voces dentro de un texto.",
    ["Sé conectores simples como and, but, so y because.", "Sé el pasado simple."],
    [
        "Los conectores muestran la relación entre ideas: neither…nor (ni… ni), either…or (o… o), though (aunque), unless (a menos que), as soon as (tan pronto como) y as a result (como resultado). Neither John nor Susan is in the office significa que ninguno está. We wouldn’t use gas unless it was cheap significa que solo lo usarían si fuera barato.",
        "Los pronombres reflexivos (reflexive pronouns) son myself, yourself, himself, herself, itself, ourselves, yourselves y themselves. Sirven para enfatizar quién hace la acción (Did you make it yourself?) o para decir que el sujeto y el objeto son la misma persona (He cut himself). Cuando enfatizan, se pueden quitar sin cambiar el significado básico de la oración, pero se pierde el énfasis.",
        "Para informar lo que otros dicen (reported speech) se usa said (dijo) y told (le dijo a alguien). Said that + oración: Mr. Brown said he had finished the report. Told + persona + to + verbo: She told me to go home. En el estilo indirecto el verbo suele retroceder un paso: lo dicho en presente pasa al pasado, y lo dicho en pasado pasa al pasado perfecto. También se informa una pregunta con asked if: She asked if we had finished (Preguntó si habíamos terminado). Al leer, busca quién habla y qué dijo.",
    ],
    [("neither…nor", "ni… ni"), ("unless", "a menos que"), ("as soon as", "tan pronto como"), ("reflexive pronoun", "pronombre reflexivo: myself, himself…"), ("said", "dijo"), ("told", "le dijo a alguien")],
    [
        ("Reflexivo", "Completa: «She made the dress ___.» A) herself B) hers", ["Se enfatiza que ella lo hizo sola.", "Se usa el reflexivo.", "Herself."], "A) herself"),
        ("Estilo indirecto", "Lee: «Mr. Pérez said that he was tired.» ¿Qué dijo Mr. Pérez? A) «I am tired.» B) «I will be tired.»", ["El verbo retrocede.", "Was tired viene de am tired.", "Dijo: I am tired."], "A"),
    ],
    [
        ("Usar himself en vez de herself para una mujer.", "El reflexivo debe coincidir con el sujeto.", "Elige el reflexivo según quién hace la acción."),
        ("Confundir said con told.", "Told necesita una persona a quien se le dice algo.", "She told me to go; she said that I should go."),
    ],
    [
        ("Lee: " + BLOG + " ¿Qué club empezaron? A) de ajedrez B) de fútbol", "A", "Dice we started a chess club."),
        ("Lee: " + REPORT + " ¿Por qué se canceló el paseo? A) por el clima B) por una prueba", "A", "Dice cancelled because of the weather."),
        ("Lee: " + CAKE + " ¿Quién cortó el pan? A) el primo B) la madre", "A", "Dice My cousin cut himself while slicing the bread."),
    ],
    [
        ("Lee: " + BLOG + " ¿A quién no le gusta el fútbol? A) a ninguno de los dos hermanos B) a uno solo", "A", "Neither my brother nor I like football: a ninguno."),
        ("Lee: " + REPORT + " ¿Qué dijo Carlos? A) que ya había enviado el proyecto B) que no había empezado", "A", "Dice Carlos said that he had already sent it."),
        ("Lee: " + CAKE + " ¿Quién pintó la sala? A) los mellizos B) la madre", "A", "Dice The twins painted the room themselves."),
    ],
    [
        ("Lee: " + BLOG + " ¿Qué ocurrió como resultado de que cada semana más estudiantes se unieran? A) necesitaron una sala más grande B) cerró el club", "A", "Dice As a result, we needed a bigger room."),
        ("Lee: " + REPORT + " ¿Qué le dijo Lucía al narrador? A) que esperara afuera B) que trajera libros", "A", "Dice Lucía told me to wait outside."),
        ("Lee: " + BLOG + " ¿Qué ocurrió apenas el director supo del club? A) les dio la biblioteca B) lo cerró", "A", "Dice As soon as the principal heard about it, he gave us the library."),
    ],
    [
        ("Lee: " + BLOG + " ¿Qué necesita el club para crecer? A) nuevos tableros B) otra sala", "A", "Dice Unless we find new boards, we cannot grow more."),
        ("Lee: " + CAKE + " ¿Qué énfasis muestra myself en I did it myself? A) que lo hizo la propia persona que habla B) que lo hizo mal", "A", "El reflexivo destaca quién hizo la acción; luego se aclara que su madre ayudó con el horno."),
    ],
    [
        ("Lee: " + REPORT + " Ordena según el texto: a) Mrs. Lara dijo que el paseo se canceló b) Mrs. Lara pidió traer los libros c) Carlos habló del proyecto", "a, b, c", "El texto sigue ese orden."),
        ("Une cada oración con su función. 1) Neither Ana nor Leo came. 2) He cut himself. 3) She told us to leave. Funciones: a) informar lo que otros dicen b) enfatizar al que actúa c) negar dos opciones", "1-c, 2-b, 3-a", "Neither…nor niega dos; himself marca quién actúa; told reporta una orden."),
    ],
    [("Lee: «The coach said that the team had won last week. She told us to practise on Saturday.» (coach = entrenadora, won = ganó, practise = practicar). ¿Qué día mandó practicar?", "El sábado", "Dice She told us to practise on Saturday.")],
    [
        ("¿Qué significa unless (en lectura de funciones)?", "A menos que", "Expresa una condición."),
        ("¿Qué pronombre reflexivo corresponde a they?", "Themselves", "Se enfatiza quién hace la acción."),
        ("¿Qué estructura se usa con told?", "Told + persona + to + verbo", "She told me to go home."),
    ],
    task("Lee: «Neither Marco nor Eli could come to the meeting. The director said that the budget was ready. He told us to send the list on Friday. We painted the sign ourselves, though it was hard. As soon as we finished, we took a photo.» (budget = presupuesto, list = lista, sign = letrero, hard = difícil, finished = terminamos). En tu hoja escribe: un conector de negación, un conector de contraste, una frase de estilo indirecto y un pronombre reflexivo.", "Neither Marco nor Eli; though; The director said that the budget was ready (o He told us to send the list on Friday); ourselves.", ["identifica los cuatro elementos", "cada uno está citado del texto", "explica una función en español"], ["hoja con cuatro respuestas"], ["decir que though niega dos personas", "copiar una oración sin conector"], "Subraya en el texto cada elemento con un color distinto."),
    "Reescribe tres frases del texto de Mrs. Lara como si la persona hablara directamente.",
    "Escribe un párrafo de seis oraciones con neither…nor, unless, a reflexive pronoun y una frase con said o told.",
)

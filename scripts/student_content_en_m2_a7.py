"""Cuaderno del estudiante, 2.º medio Inglés (propuesta), EN2M OA 07: reaccionar a textos leídos o escuchados.

Textos originales y ficticios, con pista en español; todo texto al que se refiere una pregunta está escrito en el enunciado.
Los títulos de clase del plan son genéricos; aquí cada clase trabaja un grupo de reacciones del OA: hacer conexiones;
evaluar ideas e información (true/false because); expresar acuerdo, desacuerdo, creencias y sentimientos; aconsejar y preferir
(if I were you, I’d rather); y resumir, sintetizar y generar preguntas o hipótesis (What would they…? What if…?).
"""
from __future__ import annotations

from en_m2_a_common import MAT_READ, MAT_SPEAK, arith, lesson, task

OA = "EN2M OA 07"

# ================================================== clase 1: conexiones
T1 = "«Clara’s Market Stall (fictional text). Every Saturday, Clara sells handmade soap at a street market. She buys the ingredients in large quantities, so she pays less per unit. She also keeps a notebook: she writes how many bars she sells each week. When sales are low, she changes the colours. She says that talking to customers is the best way to learn what they like.»\n(stall = puesto, soap = jabón, ingredients = ingredientes, quantities = cantidades, per unit = por unidad, bars = barras, sales = ventas, customers = clientes)"
T2 = "«The Mural Project (fictional text). A group of students painted a mural of their neighbourhood in the school corridor. First, they made drawings on paper. Then they chose three colours: blue, yellow and green. They worked in pairs, and each pair painted one square metre. At the end, they presented the mural to their families.»\n(mural = mural, corridor = pasillo, drawings = bocetos, pairs = parejas, square metre = metro cuadrado, presented = presentaron)"

lesson(
    OA, 1, MAT_SPEAK,
    "Aprenderé a hacer conexiones espontáneas entre un texto y mis otras asignaturas, mi lengua materna y mi cultura, mi vida cotidiana y mis experiencias. Sirve para comprender un texto con ideas propias y para hablar sobre él con frases como I had read…, I have seen… y we usually…",
    ["Sé el presente simple y el pasado simple.", "Sé frases como I think y I like."],
    [
        "Una conexión (connection) une lo que lees o escuchas con algo que ya conoces. Puede ser con otra asignatura (Math, Science, History), con tu lengua materna (el español), con tu cultura o la de otro país, con tu vida cotidiana o con una experiencia personal. Hacer conexiones ayuda a entender mejor y a recordar más.",
        "En inglés hay frases útiles para expresarlas: I had read about… (había leído sobre…), I have seen… (he visto…), I learned in Science that… (aprendí en Ciencias que…), I have been to… (he estado en…), We usually… (nosotros normalmente…), We often… (a menudo…) y It reminds me of… (me recuerda a…). Estas frases se usan con una idea corta: I have seen a market like this in my city.",
        "Una buena conexión tiene dos partes: el dato del texto y lo que tú sabes. Por ejemplo: Clara writes how many bars she sells. In Math, we use tables to organise data. La primera frase está en el texto; la segunda conecta con tu asignatura. Si el texto habla de una experiencia, puedes decir cómo es parecida o diferente a la tuya, usando similar to… o different from…",
    ],
    [("connection", "conexión: unir el texto con algo que conozco"), ("I had read…", "yo había leído…"), ("I have seen…", "he visto…"), ("I have been to…", "he estado en…"), ("we usually…", "normalmente nosotros…"), ("it reminds me of", "me recuerda a")],
    [
        ("Conectar con otra asignatura", "Lee: «A recipe needs two cups of flour for four people.» (flour = harina, cups = tazas). ¿Qué asignatura se conecta con la idea de proporción? A) Math B) Music", ["La receta muestra una relación entre cantidades.", "Eso se trabaja en Matemática.", "Math."], "A) Math"),
        ("Frase de conexión", "Quieres decir «he visto un mural como este». ¿Qué frase sirve? A) I have seen a mural like this. B) I will see a mural.", ["Es una experiencia pasada hasta ahora.", "Se usa I have seen.", "La B es futuro."], "A"),
    ],
    [
        ("Hacer una conexión sin decir qué dice el texto.", "La conexión necesita un dato del texto y un dato propio.", "Primero cita el texto y luego agrega tu experiencia."),
        ("Decir I have seen yesterday.", "Con yesterday se usa el pasado simple: I saw it yesterday.", "Usa I have seen sin una fecha concreta."),
    ],
    [
        ("Lee: " + T1 + " ¿Qué vende Clara? A) jabón artesanal B) pan", "A", "El texto dice handmade soap."),
        ("Lee: " + T2 + " ¿Cuántos colores eligieron? A) tres B) cinco", "A", "Dice three colours."),
        ("Lee: " + T1 + " ¿Qué hace Clara cuando las ventas bajan? A) cambia los colores B) cierra el puesto", "A", "Dice When sales are low, she changes the colours."),
    ],
    [
        ("Lee: " + T1 + " Clara anota cuántas barras vende cada semana. ¿Con qué asignatura se conecta? A) Matemática, por las tablas de datos B) Artes visuales", "A", "Registrar cantidades se relaciona con datos y tablas."),
        ("Lee: " + T2 + " Los estudiantes pintan un metro cuadrado por pareja. ¿Con qué asignatura se conecta esa medida? A) Matemática, por el área B) Música", "A", "El metro cuadrado es una medida de área."),
        ("Lee: " + T2 + " ¿Qué frase conecta el texto con una experiencia propia? A) I have seen a mural like this in my neighbourhood. B) The mural has three colours.", "A", "La frase A agrega algo que el hablante ha visto."),
    ],
    [
        ("Lee: " + T1 + " Completa la conexión: «Clara buys large quantities, so she pays less per unit. In Math, we say that the price per unit ___ when we buy more.» A) goes down B) goes up", "A", "El texto muestra que pagar por cantidad grande baja el precio por unidad."),
        ("Lee: " + T2 + " Un estudiante dice: «We usually paint murals for school events». ¿Qué conexión hace? A) con su vida cotidiana, porque habla de lo que hacen normalmente B) con una experiencia en otro país", "A", "We usually habla de una costumbre propia."),
        arith("Otro curso hace un mural con 7 parejas, y cada pareja pinta 2 metros cuadrados, como en una conexión con Matemática. ¿Cuántos metros cuadrados pintan en total?", "7*2", "Se multiplica el número de parejas por el área de cada una."),
    ],
    [
        ("Lee: " + T1 + " Un compañero dice: «It reminds me of my uncle’s bakery». ¿Qué conexión es? A) con una experiencia personal B) con una asignatura", "A", "Menciona a su tío y una panadería, algo de su vida."),
        ("Lee: " + T2 + " ¿Qué conexión es más clara? A) The mural, like a map, shows our neighbourhood. B) The mural is blue.", "A", "La A compara con otra idea; la B solo repite un dato."),
    ],
    [
        ("Une cada conexión con su tipo. 1) In Science, we learned about colours of light. 2) We usually eat together at lunch. 3) It reminds me of my cousin’s trip. Tipos: a) vida cotidiana b) otra asignatura c) experiencia personal", "1-b, 2-a, 3-c", "Science es otra asignatura; we usually habla de lo cotidiano y el viaje del primo es personal."),
        ("Lee: " + T1 + " Ordena una conexión completa: a) In Math, we use tables to organise data. b) Clara writes how many bars she sells. c) It is similar to what we do in class.", "b, a, c", "Primero el dato del texto, luego la asignatura y al final la comparación."),
    ],
    [("Lee: «My sister sells bracelets at the school fair. She sold 24 bracelets on Monday and 18 on Tuesday.» (bracelets = pulseras, sold = vendió). Haz una conexión con Matemática: ¿cuántas pulseras vendió en total?", "42", "24 más 18 son 42; es una conexión con la suma de datos.")],
    [
        ("¿Qué son las conexiones?", "Uniones entre el texto y lo que ya conozco", "Pueden ser con asignaturas o con la vida diaria."),
        ("¿Qué frase sirve para decir «he estado en»?", "I have been to…", "Habla de una experiencia."),
        ("¿Qué dos partes tiene una buena conexión (en Inglés, 2.º medio)?", "Un dato del texto y un dato propio", "Así se explica la relación."),
    ],
    task("Lee: «A school choir rehearses twice a week. The teacher says that breathing exercises make the voice stronger. The choir will sing at the end-of-year ceremony.» (choir = coro, rehearses = ensaya, breathing = respiración, ceremony = ceremonia). En tu hoja escribe tres conexiones con frases en inglés: una con otra asignatura, una con tu vida cotidiana y una con una experiencia personal, cada una con un dato del texto.", "Ejemplos: In Science, we learned that air goes into the lungs, so breathing helps. We usually practise before a presentation. I have sung at a school event once.", ["las tres conexiones son de distinto tipo", "cada una usa un dato del texto", "usa frases como I have, we usually o in Science"], ["hoja con tres frases"], ["escribir una conexión sin relación con el texto", "decir I have seen yesterday"], "Lee tus frases a una persona de tu casa y pregúntale qué conexión le pareció más clara."),
    "Lee una noticia y escribe en español dos conexiones con otras asignaturas.",
    "Elige un texto de otra asignatura y escribe tres conexiones con inglés usando I had read o I learned.",
)

# ================================================== clase 2: evaluar ideas e información
TEXT_VR = "«Virtual Reality in Class? (fictional). A school tested virtual reality headsets in History lessons for one month. Students visited a model of an old city. The teacher said that students remembered more dates than in normal lessons. However, only twelve headsets were available for forty students, so they worked in groups. Some students felt dizzy after twenty minutes.»\n(virtual reality = realidad virtual, headsets = visores, tested = probó, remembered = recordaron, dates = fechas, available = disponibles, dizzy = mareados)"
TEXT_BIKE = "«Bike Lane Survey (fictional). We asked 100 students how they get to school. 35 walk, 30 take the bus, 25 cycle and 10 come by car. The most common way is walking. However, the number of cyclists increased by 5 since last year.»\n(survey = encuesta, walk = caminan, cycle = andan en bicicleta, by car = en auto, increased = aumentó)"

lesson(
    OA, 2, MAT_READ,
    "Aprenderé a evaluar ideas e información de un texto con frases como This is true / correct / false / wrong, because… Sirve para comprobar afirmaciones con evidencia del texto y expresar por qué son verdaderas o falsas.",
    ["Sé localizar un dato en un texto.", "Sé usar because."],
    [
        "Evaluar (evaluate) una idea es decidir si es verdadera o falsa según la evidencia. Se usan las frases This is true / This is correct (esto es verdadero/correcto) y This is false / This is wrong (esto es falso/incorrecto), siempre seguidas de because y una razón con un dato del texto: This is false, because the text says that only twelve headsets were available.",
        "Para evaluar, sigue tres pasos: 1) lee la afirmación; 2) busca la frase del texto que la confirma o la contradice; 3) responde con true o false y explica con because. Si el texto no da suficiente información, di: The text does not say. Cuidado con las palabras como all, never o only: cambian el sentido de la afirmación y exigen más evidencia.",
        "También se evalúan ideas: This is a good argument because… o I am not sure, because the text does not give numbers. Evaluar no es dar tu opinión sobre el tema, sino juzgar si lo que se dice es coherente y está apoyado por datos. Un dato sin fuente o sin cifras es una evidencia débil.",
    ],
    [("true", "verdadero"), ("false", "falso"), ("correct", "correcto"), ("wrong", "incorrecto"), ("evidence", "evidencia: dato que apoya una idea"), ("The text does not say", "El texto no dice")],
    [
        ("Evaluar una afirmación", "Texto: «The market opens at nine.» Afirmación: «The market opens at ten.» ¿Qué dices? A) This is false, because the market opens at nine. B) This is true.", ["Comparo con el texto.", "El texto dice nine.", "La afirmación es falsa."], "A"),
        ("Cuando el texto contradice", "Texto: «Ana plays football only on Mondays.» Afirmación: «Ana plays football on Tuesdays.» ¿Qué respuesta es adecuada? A) False, because the text says only on Mondays. B) The text does not say.", ["El texto da un solo día con only.", "Eso contradice la afirmación.", "Es falsa."], "A"),
    ],
    [
        ("Decir true o false sin dar razón.", "No se muestra la evidencia.", "Agrega because y un dato del texto."),
        ("Marcar true una afirmación con all o never sin comprobar.", "Palabras como all y never son muy fuertes.", "Busca evidencia para todos los casos."),
    ],
    [
        ("Lee: " + TEXT_VR + " Afirmación: «The school tested the headsets for one month.» A) true B) false", "A", "El texto dice for one month."),
        ("Lee: " + TEXT_BIKE + " Afirmación: «Most students come by car.» A) true B) false", "B", "Solo 10 vienen en auto; la mayoría camina."),
        ("Lee: " + TEXT_VR + " Afirmación: «Only twelve headsets were available.» A) true B) false", "A", "El texto dice only twelve headsets."),
    ],
    [
        ("Lee: " + TEXT_VR + " Afirmación: «All students felt dizzy.» ¿Qué respuesta es correcta? A) False, because only some students felt dizzy. B) True, because the text mentions dizzy.", "A", "El texto dice Some students, no todos."),
        ("Lee: " + TEXT_BIKE + " Afirmación: «The most common way is walking.» ¿Cuál es la razón correcta? A) 35 students walk, the highest number B) 35 students take the bus", "A", "Hay 35 que caminan; es la cifra mayor."),
        ("Lee: " + TEXT_BIKE + " Afirmación: «Thirty students cycle.» A) false, because 25 cycle B) true", "A", "El texto dice 25 cycle."),
    ],
    [
        ("Lee: " + TEXT_VR + " Afirmación: «The teacher said students remembered more dates.» A) true, because the text says so B) false, because nobody said that", "A", "El texto lo dice con the teacher said."),
        ("Lee: " + TEXT_BIKE + " Afirmación: «The number of cyclists decreased.» A) false, because it increased by 5 B) true", "A", "El texto dice increased by 5."),
        arith("Lee: " + TEXT_BIKE + " Afirmación: «The number of students who walk or cycle is 60.» Calcula: ¿cuántos caminan o andan en bicicleta?", "35+25", "Se suman los que caminan con los que andan en bicicleta; 35 + 25 = 60, así que la afirmación es verdadera."),
    ],
    [
        ("Lee: " + TEXT_VR + " ¿Qué tipo de evidencia es más débil? A) el profesor dice que se recuerdan más fechas, sin cifras B) hay doce visores", "A", "No da números ni resultados medibles."),
        ("Lee: " + TEXT_BIKE + " Afirmación: «Most students use public transport.» ¿Qué respuesta es correcta? A) False, because the highest group walks B) True, because 30 take the bus", "A", "30 es menos que 35; no es la mayoría."),
    ],
    [
        ("Lee: " + TEXT_VR + " Afirmación: «The headsets are better than books.» ¿Qué respuesta es correcta? A) The text does not say B) This is true", "A", "El texto no compara con libros."),
        ("Lee: " + TEXT_BIKE + " Ordena de más a menos común: a) bus b) auto c) caminar d) bicicleta", "c, a, d, b", "Las cifras son 35, 30, 25 y 10."),
    ],
    [("Lee: «There are 20 desks in the room. Ten are blue and the rest are red.» (desks = pupitres, rest = el resto). Afirmación: «There are 12 red desks.» ¿Verdadero o falso, y por qué?", "Falso, porque hay 10 rojos", "20 menos 10 azules son 10 rojos.")],
    [
        ("¿Cómo se dice «esto es falso» en inglés?", "This is false", "Se agrega because y una razón."),
        ("¿Qué haces si el texto no da información?", "Digo que el texto no lo dice", "No hay evidencia."),
        ("¿Qué palabras exigen más evidencia?", "All, never y only", "Son afirmaciones fuertes."),
    ],
    task("Lee: «School Lunch Survey (fictional). We asked 80 students: 40 prefer rice with chicken, 25 prefer pasta and 15 prefer salad. The school kitchen has 30 minutes to serve lunch.» (prefer = prefieren, kitchen = cocina, serve = servir). En tu hoja escribe cuatro afirmaciones sobre el texto: dos verdaderas y dos falsas. Para cada una escribe true o false y because con un dato.", "Ejemplos: True, because 40 prefer rice with chicken. False, because only 15 prefer salad, not 25. True, because the kitchen has 30 minutes. False, because pasta is not the first choice.", ["cuatro afirmaciones sobre el texto", "dos verdaderas y dos falsas bien marcadas", "cada una con because y un dato"], ["hoja con cuatro afirmaciones"], ["escribir true sin because", "usar datos que no están en el texto"], "Pide a una persona de tu casa que responda true o false a tus afirmaciones y compara."),
    "Lee una noticia en español y escribe dos afirmaciones verdaderas y dos falsas sobre ella.",
    "Escribe cinco frases con This is true / This is false, because… sobre datos de tu curso.",
)

# ================================================== clase 3: sentimientos, interpretaciones y puntos de vista
TEXT_PHONE = "«Should phones be allowed at school? (fictional) Pablo: I believe that phones should be allowed at breaks, because we can contact our families. Rita: I disagree. I believe in talking face to face. When we use phones, we do not speak to each other. Marta: I agree with Pablo, but only for emergencies.»\n(allowed = permitidos, breaks = recreos, contact = contactar, face to face = cara a cara, speak = hablar, emergencies = emergencias)"
TEXT_FILM = "«A Small Film About Friendship (fictional review). The film shows two friends who move to different cities. They send letters and, after a year, they meet again. The ending is simple, but it made me feel emotional. I believe in films that show real feelings. I would recommend it, although it is a bit slow.»\n(friendship = amistad, move = mudarse, letters = cartas, meet = reencontrarse, ending = final, emotional = emocionado, recommend = recomendar, slow = lenta)"

lesson(
    OA, 3, MAT_SPEAK,
    "Aprenderé a expresar sentimientos, interpretaciones y puntos de vista con frases como I agree / disagree because…, I believe that… y I believe in… Sirve para opinar con respeto y dar razones sobre un texto.",
    ["Sé evaluar si una afirmación es verdadera o falsa.", "Sé usar because."],
    [
        "Para expresar un punto de vista (point of view) se usan frases fijas. I agree with… (estoy de acuerdo con…) y I disagree with… (no estoy de acuerdo con…) se completan con because y una razón. I believe that… (creo que…) introduce una idea, y I believe in… (creo en… / confío en…) introduce un valor o una cosa en la que se confía: I believe in teamwork. In my opinion… y I think that… también sirven.",
        "Para expresar sentimientos (feelings) se usan adjetivos con el verbo to feel o to be: I feel happy, I was surprised, it made me feel emotional. Para interpretar (interpret) un texto, dices qué crees que quiere decir el autor y apoyas con una frase: I think the ending means that friends can stay close, because they write letters. Una interpretación necesita evidencia, igual que una opinión.",
        "Cuando no estás de acuerdo, hazlo con respeto: I see your point, but I disagree because… o I understand, though I believe that… Escucha la razón de la otra persona antes de responder. Un buen argumento tiene tres partes: opinión, razón y ejemplo.",
    ],
    [("point of view", "punto de vista"), ("I agree with", "estoy de acuerdo con"), ("I disagree with", "no estoy de acuerdo con"), ("I believe that", "creo que"), ("I believe in", "creo en; confío en"), ("I see your point", "entiendo tu punto")],
    [
        ("Frase de opinión", "Quieres decir «creo en el trabajo en equipo». ¿Qué frase usas? A) I believe in teamwork. B) I believe that teamwork.", ["Quiero expresar un valor.", "Se usa I believe in + sustantivo.", "La A es correcta."], "A"),
        ("Desacuerdo respetuoso", "¿Cuál es un desacuerdo respetuoso? A) I see your point, but I disagree because… B) That is silly.", ["La A reconoce a la otra persona.", "Luego da una razón.", "La B ofende."], "A"),
    ],
    [
        ("Decir I disagree sin ninguna razón.", "No explica el punto de vista.", "Agrega because y un ejemplo."),
        ("Usar I believe on en vez de I believe in.", "La preposición correcta es in.", "Recuerda I believe in…"),
    ],
    [
        ("Lee: " + TEXT_PHONE + " ¿Quién está de acuerdo con los celulares en el recreo? A) Pablo B) Rita", "A", "Pablo dice I believe that phones should be allowed at breaks."),
        ("Lee: " + TEXT_FILM + " ¿Cómo se sintió quien escribe al ver la película? A) emocionado B) aburrido", "A", "Dice it made me feel emotional."),
        ("Lee: " + TEXT_PHONE + " ¿Qué razón da Pablo? A) contactar a sus familias B) jugar", "A", "Dice because we can contact our families."),
    ],
    [
        ("Lee: " + TEXT_PHONE + " ¿Qué valor defiende Rita? A) hablar cara a cara B) usar más pantallas", "A", "Dice I believe in talking face to face."),
        ("Lee: " + TEXT_FILM + " ¿Qué crítica hace a la película? A) es un poco lenta B) es muy corta", "A", "Dice although it is a bit slow."),
        ("Lee: " + TEXT_PHONE + " ¿En qué coincide Marta con Pablo? A) en permitir los celulares, pero solo para emergencias B) en prohibirlos", "A", "Dice I agree with Pablo, but only for emergencies."),
    ],
    [
        ("Lee: " + TEXT_FILM + " ¿Qué opinión expresa con I believe in films that show real feelings? A) confía en las películas que muestran sentimientos reales B) cree que las películas son caras", "A", "I believe in indica una convicción."),
        ("Lee: " + TEXT_PHONE + " Completa la frase de Rita en el recreo: «When we use phones, we do not ___ to each other.» A) speak B) run", "A", "El texto dice we do not speak to each other."),
        ("Lee: " + TEXT_FILM + " ¿Qué recomendación hace? A) la recomienda, aunque es lenta B) no la recomienda", "A", "Dice I would recommend it, although it is a bit slow."),
    ],
    [
        ("Lee: " + TEXT_FILM + " ¿Qué interpretación apoya el final de la película? A) que los amigos pueden mantenerse cerca aunque vivan lejos B) que las cartas son inútiles", "A", "Se escriben cartas y se reencuentran."),
        ("Lee: " + TEXT_PHONE + " ¿Qué argumento de Pablo tiene un ejemplo? A) contactar a las familias B) usar más tecnología", "A", "El ejemplo es una situación concreta: contactar a su familia."),
    ],
    [
        ("Lee: " + TEXT_PHONE + " Ordena las posturas de a favor a en contra: a) Rita b) Marta, solo emergencias c) Pablo", "c, b, a", "Pablo está a favor, Marta lo acepta con límites y Rita está en contra."),
        ("Lee: " + TEXT_PHONE + " ¿Qué frase respondería con respeto a Pablo? A) I see your point, but I believe in talking face to face. B) You are wrong.", "A", "Reconoce su idea y da una razón."),
    ],
    [("Lee: «I agree with the new library rule because it gives us silence to study.» (rule = norma, silence = silencio). ¿Qué razón da quien habla?", "Que les da silencio para estudiar", "Dice because it gives us silence to study.")],
    [
        ("¿Cómo se expresa un desacuerdo con razón?", "I disagree because…", "Se agrega una razón."),
        ("¿Qué diferencia hay entre believe that y believe in?", "Believe that introduce una idea; believe in, un valor o una confianza", "Se usan con distintas estructuras."),
        ("¿Qué tiene un buen argumento?", "Opinión, razón y ejemplo", "Así convence mejor."),
    ],
    task("Lee: «Some schools have decided to start classes at nine instead of eight. Supporters say that teenagers need more sleep. Critics say that parents must leave work earlier to take them.» (instead of = en vez de, supporters = quienes apoyan, critics = quienes critican, need = necesitan, sleep = sueño). En tu hoja escribe tu punto de vista: I agree o I disagree con una razón, una frase con I believe that o I believe in y un sentimiento con feel.", "Ejemplo: I agree with the change because teenagers need more sleep. I believe that schools should listen to students. I feel worried about parents’ work.", ["dice si está de acuerdo o no", "da una razón con because", "incluye I believe y un sentimiento"], ["hoja con tres frases"], ["no dar razón", "copiar una oración del texto"], "Lee tu opinión a una persona de tu casa y escucha si tiene otro punto de vista; responde con respeto."),
    "Escribe dos opiniones con I believe in y dos con I believe that sobre tu colegio.",
    "Elige un tema de tu curso y escribe una conversación de seis líneas con un desacuerdo respetuoso.",
)

# ================================================== clase 4: consejos y preferencias
LETTER = "«Dear Alex, I have a problem. My best friend and I want to go to a concert on Saturday, but I have a Math test on Monday. I would rather go to the concert, but I am afraid of failing the test. What should I do? Pia»\n(concert = concierto, test = prueba, afraid = con miedo, failing = reprobar)"
REPLY = "«Dear Pia, If I were you, I would study on Friday evening and on Sunday, and I would go to the concert on Saturday. I would not stay up late. You ought to ask your teacher if you can review some questions beforehand. Alex»\n(study = estudiar, stay up late = trasnocharse, ask = preguntar, review = repasar, beforehand = con anticipación)"

lesson(
    OA, 4, MAT_SPEAK,
    "Aprenderé a dar consejos con If I were you… y a expresar preferencias con I’d rather… Sirve para responder a un problema, proponer soluciones y explicar qué prefiero.",
    ["Sé los verbos should y ought to.", "Sé hacer preguntas con What should…?"],
    [
        "Para dar un consejo imaginando que estás en el lugar de la otra persona, usa If I were you, I would… (Si yo fuera tú, yo…). Con If, el verbo to be cambia a were para todas las personas: If I were you, If she were here. Después de la coma se usa would + verbo: I would study, I would ask a teacher. También sirven You ought to… y You should… (deberías).",
        "Para expresar una preferencia (preference) se usa I’d rather + verbo simple (prefiero…) o I’d rather… than… (prefiero… antes que…): I’d rather go to the concert than stay at home. La forma I’d es la contracción de I would. No se agrega to después de rather: I’d rather study, no I’d rather to study.",
        "Cuando aconsejas, piensa en las consecuencias y en los sentimientos de la otra persona. Un buen consejo tiene una acción y una razón: If I were you, I would study on Friday because the test is on Monday. Cuando hay un problema, también puedes preguntar: What would you do? (¿Qué harías?).",
    ],
    [("If I were you", "si yo fuera tú"), ("I would", "yo haría"), ("I’d rather", "prefiero"), ("You ought to", "deberías"), ("advice", "consejo"), ("What would you do?", "¿Qué harías?")],
    [
        ("Consejo", "Quieres aconsejar a un amigo que tiene sueño. ¿Qué dices? A) If I were you, I would go to bed early. B) If I was you, I will go.", ["Se usa were con If.", "Después va would + verbo.", "La A es correcta."], "A"),
        ("Preferencia", "Quieres decir «prefiero leer». ¿Qué frase usas? A) I’d rather read. B) I’d rather to read.", ["Después de rather va el verbo simple.", "No lleva to.", "La A es correcta."], "A"),
    ],
    [
        ("Decir If I was you, I will.", "En los consejos se usa were y would.", "Escribe If I were you, I would…"),
        ("Decir I’d rather to go.", "Después de rather no se usa to.", "Escribe I’d rather go."),
    ],
    [
        ("Lee: " + LETTER + " ¿Qué problema tiene Pia? A) quiere ir a un concierto, pero tiene una prueba el lunes B) perdió su celular", "A", "Dice I have a Math test on Monday."),
        ("Lee: " + REPLY + " ¿Qué le aconseja Alex hacer el sábado? A) ir al concierto B) estudiar toda la noche", "A", "Dice I would go to the concert on Saturday."),
        ("Lee: " + LETTER + " ¿Qué prefiere hacer Pia? A) ir al concierto B) estudiar", "A", "Dice I would rather go to the concert."),
    ],
    [
        ("Lee: " + REPLY + " ¿Qué consejo se refiere a no trasnocharse? A) I would not stay up late. B) You ought to ask your teacher.", "A", "Stay up late es trasnocharse."),
        ("Lee: " + REPLY + " ¿Qué le sugiere preguntar a la profesora? A) si puede repasar algunas preguntas B) si puede cambiar la fecha", "A", "Dice review some questions beforehand."),
        ("Lee: " + LETTER + " ¿Por qué tiene miedo Pia? A) de reprobar la prueba B) de llegar tarde", "A", "Dice I am afraid of failing the test."),
    ],
    [
        ("Completa: «If I ___ you, I would talk to the teacher.» A) were B) am", "A", "En If I were you se usa were."),
        ("Completa: «I’d rather ___ at home.» A) stay B) to stay", "A", "Después de rather va el verbo simple."),
        ("Lee: " + REPLY + " ¿En qué días aconseja estudiar? A) viernes en la tarde y domingo B) lunes en la mañana", "A", "Dice on Friday evening and on Sunday."),
    ],
    [
        ("Lee: " + REPLY + " ¿Por qué el consejo es equilibrado? A) porque permite ir al concierto y también estudiar B) porque prohíbe salir", "A", "Combina diversión y estudio."),
        ("Lee: " + LETTER + " Un compañero dice que Pia prefiere estudiar. ¿Qué frase lo corrige? A) I would rather go to the concert B) I am afraid of failing", "A", "Esa frase expresa su preferencia."),
    ],
    [
        ("Une cada situación con el mejor consejo. 1) Un amigo olvidó su tarea. 2) Un amigo está nervioso por hablar en público. 3) Un amigo está muy cansado. Consejos: a) If I were you, I would practise in front of a mirror. b) If I were you, I would tell the teacher. c) If I were you, I would sleep early.", "1-b, 2-a, 3-c", "Cada consejo responde al problema."),
        ("Elige la frase con I’d rather más natural: A) I’d rather walk than take the bus. B) I’d rather than walk to take the bus.", "A", "Se usa I’d rather + verbo simple + than + verbo simple."),
    ],
    [("Lee: «My friend Leo says: ‘I would rather play football than study. But the exam is tomorrow.’» (exam = prueba). ¿Qué preferiría hacer Leo?", "Jugar fútbol", "Dice I would rather play football than study.")],
    [
        ("¿Cómo se da un consejo con If?", "If I were you, I would…", "Se usa were y would."),
        ("¿Qué se usa después de I’d rather?", "El verbo simple, sin to", "I’d rather go."),
        ("¿Qué pregunta se usa para pedir un consejo?", "What would you do?", "Pide una acción."),
    ],
    task("Lee: «Tom writes: ‘I want to join the school band, but I also need to work on weekends. I would rather play the drums than the guitar. What would you do?’» (join = unirse, band = banda, weekends = fines de semana, drums = batería). En tu hoja escribe una respuesta de cuatro líneas con If I were you, I would…, una razón con because y una frase con I’d rather.", "Ejemplo: If I were you, I would talk to the band teacher about a flexible schedule, because you can still work. I would also ask for a practice time on weekdays. I’d rather play the drums than the guitar, so I would choose that instrument.", ["usa If I were you, I would", "da una razón con because", "incluye I’d rather con verbo simple"], ["hoja con cuatro líneas"], ["escribir If I was you, I will", "agregar to después de rather"], "Lee tu consejo a una persona de tu casa y pregunta si lo seguiría."),
    "Escribe tres consejos con If I were you para problemas comunes de tu curso.",
    "Escribe una carta corta pidiendo consejo y una respuesta con If I were you, I would…",
)

# ================================================== clase 5: resumir, sintetizar y plantear hipótesis
TEXT_TREE = "«The Old Oak Tree (fictional). In a small town, an old oak tree stood in the main square for a hundred years. Children played under it, and old people sat on benches beside it. Last winter, a storm broke a big branch. The council discussed cutting the tree down, but the neighbours asked to keep it. In the end, they decided to cut only the broken part and build a fence.»\n(oak = roble, square = plaza, benches = bancas, storm = tormenta, branch = rama, cutting down = talar, neighbours = vecinos, fence = reja)"
TEXT_ROBOT = "«Robots in the Kitchen (fictional). A restaurant started using a robot to wash dishes. The robot works fast and never gets tired. However, it breaks a dish sometimes, and it cannot clean the pots well. The manager says that the robot saves time, but that the staff still do important work.»\n(wash = lavar, dishes = platos, breaks = rompe, pots = ollas, manager = gerente, saves = ahorra, staff = personal)"

lesson(
    OA, 5, MAT_READ,
    "Aprenderé a resumir y sintetizar información, y a generar preguntas o hipótesis con What would they…? y What if…? Sirve para explicar lo que leí en pocas palabras y para pensar en lo que podría ocurrir.",
    ["Sé evaluar ideas y expresar opiniones.", "Sé usar would para consejos."],
    [
        "Resumir (summarise) es decir lo más importante en pocas palabras. Sintetizar (synthesise) es juntar ideas de dos textos o de varias partes para llegar a una idea nueva. Para resumir, responde quién, qué, cuándo, dónde y por qué, y escribe una o dos oraciones. Empieza con The text says that… o In short,… (en resumen). No copies frases y no agregues tu opinión.",
        "Para generar preguntas, usa What would they…? (¿Qué harían…?) y What if…? (¿Y si…?). What if the council cut the tree down? imagina un caso distinto. Se responde con would: They would lose a symbol of the town. Estas preguntas se llaman hipotéticas (hypothetical) porque piensan en algo que podría ocurrir. Una hipótesis (hypothesis) es una idea que propones y que se puede comprobar.",
        "Para formular una hipótesis, usa probably, maybe o I think that… y apoya con una pista del texto: Maybe the neighbours love the tree because children play under it. Una buena pregunta de lectura no se contesta con sí o no: pide razones o consecuencias. Intercambia tus preguntas con otra persona y respóndanlas con evidencia.",
    ],
    [("summarise", "resumir"), ("synthesise", "sintetizar: juntar ideas para formar una nueva"), ("What if…?", "¿Y si…?"), ("What would they…?", "¿Qué harían…?"), ("hypothesis", "hipótesis"), ("in short", "en resumen")],
    [
        ("Pregunta hipotética", "¿Cuál es una pregunta hipotética? A) What if the library closed? B) What time does it close?", ["Imagina una situación posible.", "La A empieza con What if.", "Es hipotética."], "A"),
        ("Resumen", "Texto: «Ana joined a club, practised daily and won the final.» ¿Cuál es un buen resumen? A) Ana practised and won. B) Ana likes clubs.", ["Un resumen reúne los hechos principales.", "La A los reúne.", "La B es general."], "A"),
    ],
    [
        ("Hacer una pregunta de sí o no como pregunta hipotética.", "No pide razones ni consecuencias.", "Empieza con What if o What would."),
        ("Agregar opinión personal al resumen.", "El resumen informa lo que dice el texto.", "Guarda tu opinión para después."),
    ],
    [
        ("Lee: " + TEXT_TREE + " ¿Cuántos años estuvo el roble en la plaza? A) cien B) diez", "A", "El texto dice for a hundred years."),
        ("Lee: " + TEXT_ROBOT + " ¿Qué lava el robot? A) platos B) ollas", "A", "Dice a robot to wash dishes; no puede limpiar bien las ollas."),
        ("Lee: " + TEXT_TREE + " ¿Qué rompió la tormenta? A) una rama grande B) la plaza", "A", "Dice a storm broke a big branch."),
    ],
    [
        ("Lee: " + TEXT_TREE + " ¿Cuál es el mejor resumen? A) A storm broke a branch of the old tree, and the neighbours decided to keep it and cut only the broken part. B) The tree is old.", "A", "Reúne el problema y la decisión."),
        ("Lee: " + TEXT_ROBOT + " ¿Cuál es el mejor resumen? A) A robot saves time but has problems, and staff still do important work. B) A restaurant has a robot.", "A", "Incluye ventajas, problemas y la idea final."),
        ("Lee: " + TEXT_TREE + " ¿Qué pregunta hipotética es adecuada? A) What if the council cut the tree down? B) How old is the tree?", "A", "La A imagina un caso distinto."),
    ],
    [
        ("Lee: " + TEXT_ROBOT + " Completa la respuesta: «What would the staff do if the robot broke down?» A) They would wash the dishes by hand. B) They will wash.", "A", "En una hipótesis se usa would."),
        ("Lee: " + TEXT_TREE + " ¿Qué hipótesis tiene apoyo en el texto? A) The neighbours probably love the tree because children play under it. B) The neighbours hate the tree.", "A", "El texto dice que los niños juegan allí."),
        ("Lee: " + TEXT_ROBOT + " ¿Qué pregunta pide una consecuencia? A) What if the robot had more power? B) Who is the manager?", "A", "What if plantea una consecuencia."),
    ],
    [
        ("Lee: " + TEXT_ROBOT + " Une las ideas de ventajas y desventajas en una síntesis. ¿Cuál es? A) The robot saves time, but it still needs human help. B) The robot is perfect.", "A", "La síntesis junta ventajas y límites."),
        ("Lee: " + TEXT_TREE + " ¿Qué hipótesis es débil? A) The tree is magic. B) The neighbours love it because of memories.", "A", "El texto no da ninguna pista de magia."),
    ],
    [
        ("Lee: " + TEXT_TREE + " Ordena: a) los vecinos pidieron conservarlo b) la tormenta rompió una rama c) decidieron cortar solo lo roto y construir una reja", "b, a, c", "Es el orden de los hechos del texto."),
        ("Lee: " + TEXT_ROBOT + " Completa el resumen: «A robot saves time, but it ___.» A) breaks dishes sometimes B) cooks the food", "A", "Eso es lo que dice el texto."),
    ],
    [("Lee: «A school decided to stop selling sugary drinks. Sales of juice rose, and students said that they felt less tired.» (sugary drinks = bebidas azucaradas, rose = subieron). Haz una pregunta con What if que explore otra consecuencia.", "What if the school also stopped selling snacks?", "What if plantea otra consecuencia posible.")],
    [
        ("¿Qué es resumir (en Inglés, 2.º medio)?", "Decir lo más importante en pocas palabras", "No se agrega opinión."),
        ("¿Cómo empieza una pregunta hipotética?", "With What if o What would", "Imagina una situación."),
        ("¿Qué es una hipótesis (en Inglés, 2.º medio)?", "Una idea que se propone y se puede comprobar", "Se apoya con pistas."),
    ],
    task("Lee: «The Reading Corner (fictional). Last year, a school created a reading corner with soft chairs and 200 books. After six months, 70 students borrowed books every week. The librarian says that more students come when there are comics.» (corner = rincón, soft = cómodas, borrowed = pidieron prestado, comics = historietas). En tu hoja escribe: un resumen de una oración, una pregunta What if y una hipótesis con probably o maybe.", "Resumen: A school created a reading corner and 70 students borrow books every week. Pregunta: What if the school bought more comics? Hipótesis: Probably more students would come if there were comics.", ["resumen de una oración con dos datos", "pregunta What if razonable", "hipótesis apoyada en el texto"], ["hoja con tres respuestas"], ["copiar una oración del texto", "hacer una hipótesis sin pista"], "Comparte tu pregunta con una persona de tu casa y pide que la responda con would."),
    "Resume en una oración una noticia en español y escribe una pregunta What if sobre ella.",
    "Escribe tres preguntas What if sobre tu colegio y responde una con would.",
)

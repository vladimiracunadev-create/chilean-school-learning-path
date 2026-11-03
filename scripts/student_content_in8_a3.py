"""Cuaderno del estudiante, 8.º básico Inglés (oficial), IN08 OA 03 (propósito, detalle, secuencia, hecho y opinión) y OA 04 (estrategias de escucha).

Las «escuchas» las lee un adulto en voz alta; el guion va escrito y el estudiante lo tapa con una hoja.
"""
from __future__ import annotations

from student_content_in8_a import ADULT, MAT_L, lesson
from student_content_ma01_b import task

OA3 = "IN08 OA 03"
OA4 = "IN08 OA 04"

# ================================================================== OA 3, clase 1
GARDEN = "«Hello, everyone. I'm Fabiola, from the green club. Our school garden has no water on weekends, and the plants are thirsty. Please bring one bottle of water on Friday. Put it in the blue box near the gate. Thank you!» (garden = huerto, weekends = fines de semana, thirsty = con sed, bottle = botella, gate = portón)"
GUIDE = "«Welcome to the Maritime Museum. I'm your guide, Lucas. In this room, you can see old maps and a ship's wheel. The tour lasts forty minutes. Please do not touch the glass boxes.» (maritime = marítimo, guide = guía, ship's wheel = timón, tour = visita guiada, lasts = dura, touch = tocar, glass boxes = vitrinas)"
PLAN = "«Nico: What do you want to do on Saturday? Pía: I'd like to go to the beach. Nico: Good idea, but the forecast says rain. Pía: Then let's go to the cinema. Nico: OK. The film starts at three.» (forecast = pronóstico, rain = lluvia, film = película, starts = empieza)"

lesson(
    OA3, 1, MAT_L,
    "Aprenderé a identificar el propósito, el tema y la idea general de un texto escuchado, y a decir quiénes hablan, dónde y cuándo. Sirve para entender la situación completa antes de buscar detalles.",
    ["Sé reconocer entrevistas, anécdotas y exposiciones.", "Conozco preguntas como who, where y when."],
    [
        "Al escuchar un texto, primero se identifica su propósito (purpose), es decir, para qué se dice: pedir ayuda, dar información, dar una regla, decidir un plan o contar algo. Luego se identifica el tema (topic), que es de qué se habla, y la idea general (main idea), que es lo más importante dicho en una frase.",
        "Después se buscan los detalles relevantes con cinco preguntas: who (quién habla o actúa), what (qué hace o qué pasa), where (dónde), when (cuándo) y which situation (en qué situación, por ejemplo un colegio, un museo o una conversación entre amigos). Las pistas están en saludos, nombres, verbos y expresiones de lugar y tiempo: Hello, everyone; I'm your guide; on Friday; near the gate.",
        "Un hablante (speaker) es la persona que habla. Algunos textos tienen un solo hablante, como un aviso, y otros tienen dos o más, como una conversación. Reconocer cuántos hablantes hay y cómo se llaman evita atribuir a una persona lo que dijo otra.",
    ],
    [("purpose", "propósito: para qué se dice un texto"), ("topic", "tema: de qué se habla"), ("main idea", "idea general: lo más importante del texto"), ("speaker", "hablante: persona que habla"), ("situation", "situación: contexto en que ocurre el texto"), ("rule", "regla: algo que hay que cumplir")],
    [
        ("Propósito y hablante", ADULT + GARDEN + " ¿Quién habla y para qué?", ["Se presenta como Fabiola, del club verde.", "Dice que el huerto no tiene agua los fines de semana.", "Pide traer una botella de agua el viernes."], "Fabiola habla para pedir ayuda con agua para el huerto"),
        ("Situación de una conversación", ADULT + PLAN + " ¿Quiénes hablan y qué deciden?", ["Hablan Nico y Pía por turnos.", "Pía propone la playa, pero el pronóstico dice lluvia.", "Deciden ir al cine."], "Nico y Pía deciden ir al cine"),
    ],
    [
        ("Decir el tema y no el propósito: «el texto habla del huerto» como si fuera lo que quiere lograr.", "El tema dice de qué se habla; el propósito dice qué se quiere lograr.", "Pregunta: ¿qué quiere lograr quien habla?"),
        ("Atribuir a Pía la frase de Nico sobre el pronóstico.", "No se asoció cada frase con su hablante.", "Anota el nombre de quien habla antes de escribir lo que dijo."),
    ],
    [
        (ADULT + GARDEN + " ¿Quién habla? a) Fabiola, del club verde b) Lucas, un guía", "a) Fabiola, del club verde", "Dice I'm Fabiola, from the green club."),
        (ADULT + GUIDE + " ¿Dónde ocurre el texto? a) en un museo marítimo b) en un colegio", "a) en un museo marítimo", "Dice Welcome to the Maritime Museum."),
        (ADULT + PLAN + " ¿Cuántas personas hablan?", "2", "Hablan Nico y Pía."),
    ],
    [
        (ADULT + GARDEN + " ¿Cuál es el propósito? a) pedir ayuda con agua para el huerto b) anunciar un campeonato c) vender plantas", "a) pedir ayuda con agua para el huerto", "Pide traer una botella de agua el viernes."),
        (ADULT + GUIDE + " ¿Cuál es el tema? a) una visita guiada por un museo y sus reglas b) la historia de un barco c) un paseo en bote", "a) una visita guiada por un museo y sus reglas", "El guía da la bienvenida, dice qué se verá y una regla."),
        (ADULT + PLAN + " ¿Qué plan eligen al final? a) ir al cine b) ir a la playa c) quedarse en casa", "a) ir al cine", "Pía dice let's go to the cinema y Nico acepta."),
    ],
    [
        (ADULT + GUIDE + " Si la visita empieza a las 11:00 (dato de ejemplo), ¿a qué hora termina? a) a las 11:40 b) a las 12:00", "a) a las 11:40", "La visita dura cuarenta minutos."),
        (ADULT + PLAN + " ¿A qué hora empieza la película? a) a las 3 b) a las 5", "a) a las 3", "Nico dice The film starts at three."),
        (ADULT + GARDEN + " ¿Dónde hay que dejar la botella? a) en la caja azul junto al portón b) en la oficina", "a) en la caja azul junto al portón", "Dice Put it in the blue box near the gate."),
    ],
    [
        (ADULT + GUIDE + " ¿Qué frase del texto da una regla? a) Please do not touch the glass boxes. b) You can see old maps.", "a) Please do not touch the glass boxes.", "Pide no hacer algo, y eso es una regla."),
        (ADULT + PLAN + " ¿Por qué cambian el plan de la playa? a) porque el pronóstico dice lluvia b) porque la playa queda lejos", "a) porque el pronóstico dice lluvia", "Nico dice the forecast says rain."),
    ],
    [
        (ADULT + GARDEN + " Un oyente dice que Fabiola quiere que lleven plantas. ¿Qué frase del texto lo contradice? a) Please bring one bottle of water b) Thank you", "a) Please bring one bottle of water", "Pide una botella de agua, no plantas."),
        (ADULT + GUIDE + " ¿Cuál de estos dos textos tiene un solo hablante: el de Lucas o el de Nico y Pía? a) el de Lucas b) el de Nico y Pía", "a) el de Lucas", "Lucas habla solo; Nico y Pía se turnan."),
    ],
    [(ADULT + "En el colegio oyes: «Attention, students. The school bus for the trip to the farm leaves at eight sharp from the main gate. Please be on time.» (sharp = en punto, farm = granja, leaves = sale, main gate = portón principal, on time = a tiempo). ¿Cuál es el propósito? a) avisar la hora y el lugar de salida y pedir puntualidad b) contar cómo fue la visita a la granja", "a) avisar la hora y el lugar de salida y pedir puntualidad", "Dice la hora, el lugar y Please be on time.")],
    [
        ("En Inglés de 8.º (OA 3, clase 1): ¿Qué es el propósito de un texto?", "Para qué se dice", "Responde a qué quiere lograr quien habla."),
        ("¿Qué preguntas ayudan a encontrar detalles de personas, lugares y tiempo?", "Who, what, where y when", "Piden persona, acción, lugar y momento."),
        ("¿Qué es un hablante?", "La persona que habla", "Hay textos con uno o con varios hablantes."),
    ],
    task("Un adulto lee dos veces este texto: «Good morning. I'm Mrs. Pérez, the school nurse. This week we are checking vision in the library. Come on Monday or Tuesday between ten and noon. It takes five minutes. You don't need to bring anything.» (nurse = enfermera, vision = visión, noon = mediodía, takes = demora, anything = nada). Escribe quién habla, para qué, dónde, cuándo y cuánto demora.", "Habla la enfermera Sra. Pérez para avisar un control de visión en la biblioteca, el lunes o el martes entre 10 y 12; demora 5 minutos.", ["identifica a la hablante", "dice el propósito", "anota lugar, momento y duración"], ["hoja con cinco respuestas", "nota del adulto"], ["decir que el control es en la sala de clases", "no anotar la duración"], "Reconoce lo que acertó y vuelve a escuchar solo la parte donde estaba el dato que falta."),
    "Pide a un adulto que lea el aviso del huerto y responde en voz alta quién habla, para qué y qué debes llevar.",
    "Escribe un aviso de cuatro líneas en español sobre una actividad de tu curso e indica su propósito y quién lo diría.",
)

# ------------------------------------------------------------------ OA 3, clase 2
LEMON = "«To make lemonade, first squeeze four lemons into a jug. Next, add one litre of cold water. Then stir in three spoons of sugar. After that, put in some ice. Finally, taste it and add more sugar if you want.» (lemonade = limonada, squeeze = exprimir, jug = jarra, litre = litro, stir in = mezclar con, spoons = cucharadas, ice = hielo, taste = probar)"
SUNDAY = "«On Sunday, Raúl got up late. After breakfast, he walked to the park. Before lunch, he met his friend Lía. They played chess until two o'clock. Later, they went home together.» (got up = se levantó, breakfast = desayuno, lunch = almuerzo, chess = ajedrez, later = más tarde, together = juntos)"
BEAN = "«To grow a bean, first put wet cotton in a clean container. Second, place one bean on the cotton. Third, put the container near a window. Every day, add a little water. After a week, a small root appears.» (bean = poroto, wet = húmedo, cotton = algodón, container = envase, place = poner, root = raíz, appears = aparece)"
CONCERT = "«Before the concert, Alba bought two tickets. When she arrived, the door was closed, so she waited. After ten minutes, the guard opened it. Then she found her seat, and the music began.» (concert = concierto, tickets = entradas, door = puerta, guard = guardia, seat = asiento, began = empezó)"

lesson(
    OA3, 2, MAT_L,
    "Aprenderé a identificar los pasos de unas instrucciones y el orden de los hechos de un relato, usando first, next, then, after that, finally, before y after. Sirve para seguir procedimientos y contar en orden lo que pasó.",
    ["Sé reconocer los conectores first, then y finally.", "Conozco verbos como put, add y open."],
    [
        "En unas instrucciones (instructions) o un procedimiento (procedure), cada paso (step) es una acción. Los pasos se ordenan con palabras de secuencia: first (primero), second y third (segundo y tercero), next (luego, a continuación), then (después), after that (después de eso) y finally (por último). El orden importa: si cambias un paso, el resultado puede salir mal.",
        "En un relato de hechos, la secuencia de eventos (sequence of events) se marca con on Sunday, later, before y after. After breakfast significa después del desayuno. Before lunch significa antes del almuerzo. La frase until two o'clock dice cuándo termina una actividad. Estas palabras no siempre aparecen en el orden en que ocurrieron los hechos, así que hay que ordenarlos.",
        "Para anotar una secuencia, escribe números al lado de cada acción mientras escuchas. Después revisa que tengas el primer paso, los intermedios y el último. Un truco: pregunta «¿qué pasó justo antes?» y «¿qué pasó justo después?» para cada acción.",
    ],
    [("step", "paso: una acción dentro de unas instrucciones"), ("sequence", "secuencia: el orden en que ocurren las cosas"), ("first / next / then", "primero / a continuación / después"), ("finally", "por último"), ("before / after", "antes de / después de"), ("later", "más tarde")],
    [
        ("Ubicar un paso", ADULT + LEMON + " ¿Qué se hace en el tercer paso, contando first como el primero?", ["First es exprimir los limones.", "Next es agregar el agua; then es mezclar con azúcar.", "El tercer paso es then: mezclar tres cucharadas de azúcar."], "Mezclar tres cucharadas de azúcar"),
        ("Ordenar hechos", ADULT + SUNDAY + " ¿Qué hizo Raúl justo después del desayuno?", ["Busco after breakfast.", "Dice he walked to the park.", "Caminó al parque."], "Caminó al parque"),
    ],
    [
        ("Seguir el orden en que se nombran los hechos como si fuera el orden en que ocurrieron.", "Una frase puede mencionar antes algo que pasó después, como before lunch.", "Fíjate en before, after y later para ordenar."),
        ("Saltarse un paso y mezclar los pasos de un procedimiento.", "No se anotaron los números de cada paso.", "Escribe un número por cada acción mientras escuchas."),
    ],
    [
        (ADULT + BEAN + " ¿Qué se hace primero? a) poner algodón húmedo en un envase b) poner el envase cerca de la ventana", "a) poner algodón húmedo en un envase", "Dice first put wet cotton in a clean container."),
        (ADULT + BEAN + " ¿Qué se hace después de poner el poroto sobre el algodón? a) poner el envase cerca de una ventana b) esperar una semana", "a) poner el envase cerca de una ventana", "Es el tercer paso: third, put the container near a window."),
        (ADULT + BEAN + " ¿Qué se agrega cada día? a) un poco de agua b) más algodón", "a) un poco de agua", "Dice Every day, add a little water."),
    ],
    [
        (ADULT + BEAN + " ¿Qué aparece después de una semana? a) una pequeña raíz b) una flor grande", "a) una pequeña raíz", "Dice After a week, a small root appears."),
        (ADULT + BEAN + " ¿Cuántos pasos se numeran con first, second y third?", "3", "Los tres primeros pasos tienen número; luego vienen acciones diarias."),
        (ADULT + CONCERT + " ¿Qué hizo Alba antes del concierto? a) compró dos entradas b) abrió la puerta", "a) compró dos entradas", "Dice Before the concert, Alba bought two tickets."),
    ],
    [
        (ADULT + CONCERT + " Ordena estos hechos de primero a último, escribiendo los números: (1) el guardia abrió la puerta, (2) empezó la música, (3) Alba compró las entradas.", "3, 1, 2", "Compró las entradas, esperó hasta que abrieron y luego empezó la música."),
        (ADULT + CONCERT + " ¿Qué hizo Alba mientras la puerta estaba cerrada? a) esperó b) se fue", "a) esperó", "Dice the door was closed, so she waited."),
        (ADULT + SUNDAY + " ¿Qué dice el texto que Raúl hizo «before lunch»? a) se encontró con su amiga Lía b) volvió a casa con ella", "a) se encontró con su amiga Lía", "Dice Before lunch, he met his friend Lía."),
    ],
    [
        (ADULT + SUNDAY + " ¿Qué hicieron justo después de jugar ajedrez hasta las dos? a) volvieron juntos a casa b) tomaron desayuno", "a) volvieron juntos a casa", "Dice Later, they went home together."),
        ("Daniel hizo el tercer paso del poroto (poner el envase en la ventana) antes del segundo. ¿Qué paso hizo tarde? a) poner un poroto sobre el algodón b) poner algodón húmedo en un envase", "a) poner un poroto sobre el algodón", "El segundo paso es place one bean on the cotton."),
    ],
    [
        (ADULT + SUNDAY + " ¿Qué palabras marcan el orden de los hechos? a) after, before, later b) because, so, but", "a) after, before, later", "Esas palabras indican antes y después; las otras indican razón, resultado y contraste."),
        (ADULT + CONCERT + " ¿Cuántos minutos esperó Alba antes de que abrieran la puerta?", "10", "Dice After ten minutes, the guard opened it."),
    ],
    [(ADULT + "Para lavarte las manos oyes: «First, wet your hands. Next, put on soap. Then rub them well, between your fingers too. After that, rinse them. Finally, dry them with a clean towel.» (wet = moja, soap = jabón, rub = frota, between = entre, fingers = dedos, rinse = enjuaga, towel = toalla). ¿Qué se hace justo después de frotar? a) enjuagar las manos b) secar con toalla", "a) enjuagar las manos", "Después de rub viene After that, rinse them; secar es el último paso.")],
    [
        ("¿Qué indica la palabra «finally» en unas instrucciones?", "El último paso", "Finally significa por último."),
        ("En Inglés de 8.º (OA 3, clase 2): ¿Qué significa «before lunch»?", "Antes del almuerzo", "Before es antes de."),
        ("¿Cómo puedes anotar una secuencia mientras escuchas?", "Con un número por cada acción", "Así no pierdes el orden."),
    ],
    task("Un adulto lee dos veces este procedimiento: «To make a paper hat, first take a large sheet of newspaper. Second, fold it in half. Third, fold the two top corners to the middle. Next, fold up the bottom edges, one on each side. Finally, open the hat and put it on your head.» (paper hat = sombrero de papel, sheet = hoja, newspaper = diario, fold = doblar, in half = por la mitad, corners = esquinas, edges = bordes, on each side = a cada lado). Escribe los cinco pasos en español y en orden.", "1) Tomar una hoja grande de diario. 2) Doblarla por la mitad. 3) Doblar las dos esquinas de arriba hacia el centro. 4) Doblar hacia arriba los bordes de abajo, uno a cada lado. 5) Abrir el sombrero y ponérselo.", ["anota cinco pasos", "respeta el orden", "usa las palabras de secuencia como guía"], ["hoja con cinco pasos numerados", "nota del adulto"], ["mezclar el paso tres con el cuatro", "no incluir el último paso"], "Reconoce los pasos que anotó en orden y vuelve a escuchar solo las palabras first, second, third, next y finally."),
    "Pide a un adulto que lea las instrucciones de la limonada y numera cada paso en tu hoja.",
    "Escribe en español cuatro pasos para hacer algo que sabes (por ejemplo, preparar un té) y márcalos con first, next, then y finally.",
)

# ------------------------------------------------------------------ OA 3, clase 3
LIB = "«The library opens at nine in the morning. It has two floors and about three thousand books. I think it is the best place in town. In my opinion, the chairs are too hard.» (opens = abre, floors = pisos, books = libros, best = el mejor, town = ciudad, chairs = sillas, hard = duras)"
NOTE = "«This notebook costs two thousand pesos. It has eighty pages and a blue cover. It is the ugliest notebook in the shop, but my sister believes it is beautiful.» (costs = cuesta, pages = hojas, cover = tapa, ugliest = el más feo, shop = tienda, believes = cree, beautiful = hermoso)"
PARK = "«The park is next to the river. It closes at eight o'clock. Dogs must wear a leash. Honestly, it is boring on Sundays, and I don't like the noisy ducks.» (leash = correa, boring = aburrido, noisy = ruidoso, ducks = patos, honestly = sinceramente)"

lesson(
    OA3, 3, MAT_L,
    "Aprenderé a diferenciar un hecho de una opinión en textos escuchados. Sirve para saber qué datos se pueden comprobar y qué juicios son solo la visión de quien habla.",
    ["Sé ubicar datos como horas, números y lugares.", "Conozco adjetivos como best, boring y beautiful."],
    [
        "Un hecho (fact) es algo que se puede comprobar: una hora, una cantidad, un lugar o una regla. The library opens at nine y It has two floors son hechos, porque puedes ir y verificarlos. Una opinión (opinion) es lo que alguien piensa o siente, y otra persona puede pensar distinto. I think it is the best place es una opinión.",
        "Hay palabras que avisan que viene una opinión: I think, I believe, in my opinion, honestly y adjetivos de juicio como best, ugliest, boring, beautiful, noisy y too hard. Cuidado: esas palabras ayudan, pero decide siempre con la pregunta de comprobación. Y una persona puede mencionar el parecer de otra persona, como my sister believes it is beautiful, que sigue siendo una opinión.",
        "Para decidir, hazte la pregunta de comprobación: «¿puedo verificar esto con una medida, un documento o mirando?». Si la respuesta es sí, es un hecho. Si depende de gustos o sentimientos, es una opinión. Un texto puede mezclar ambos; no todo lo que dice una persona es opinión.",
    ],
    [("fact", "hecho: dato que se puede comprobar"), ("opinion", "opinión: lo que alguien piensa o siente"), ("I think / I believe", "yo creo / yo pienso"), ("in my opinion", "en mi opinión"), ("best / ugliest", "el mejor / el más feo"), ("boring", "aburrido")],
    [
        ("Clasificar una oración", ADULT + LIB + " ¿«It has two floors» es hecho u opinión?", ["Puedo comprobar los pisos yendo a la biblioteca.", "No depende de gustos.", "Es un dato verificable."], "Es un hecho"),
        ("Reconocer una opinión", ADULT + NOTE + " ¿«It is the ugliest notebook in the shop» es hecho u opinión?", ["Ugliest es un juicio personal.", "Otra persona puede pensar que es hermoso.", "No se puede medir."], "Es una opinión"),
    ],
    [
        ("Creer que todo lo que dice alguien con seguridad es un hecho.", "Una opinión puede decirse con mucha seguridad y no por eso se puede comprobar.", "Hazte la pregunta de comprobación."),
        ("Creer que toda frase con un número es un hecho.", "Un número puede aparecer dentro de una opinión, como «the best three books» (los mejores tres libros), que sigue siendo un juicio.", "Revisa si lo que se afirma se puede verificar."),
    ],
    [
        (ADULT + LIB + " ¿«The library opens at nine in the morning» es un hecho o una opinión? a) un hecho b) una opinión", "a) un hecho", "Se puede comprobar con el horario."),
        (ADULT + LIB + " ¿«I think it is the best place in town» es un hecho o una opinión? a) una opinión b) un hecho", "a) una opinión", "Best y I think muestran un juicio personal."),
        (ADULT + NOTE + " ¿«This notebook costs two thousand pesos» es un hecho o una opinión? a) un hecho b) una opinión", "a) un hecho", "El precio se puede comprobar."),
    ],
    [
        (ADULT + PARK + " ¿Cuál de estas oraciones es un hecho? a) The park closes at eight o'clock. b) It is boring on Sundays.", "a) The park closes at eight o'clock.", "La hora de cierre se puede comprobar; boring es un juicio."),
        (ADULT + NOTE + " ¿Cuál de estas oraciones es un hecho? a) It has eighty pages. b) It is beautiful.", "a) It has eighty pages.", "Se pueden contar las hojas."),
        (ADULT + PARK + " ¿Qué palabra avisa de una opinión? a) Honestly b) river", "a) Honestly", "Honestly (sinceramente) introduce lo que piensa quien habla."),
    ],
    [
        (ADULT + LIB + " Clasifica cada oración como hecho (H) u opinión (O): 1) It has about three thousand books. 2) In my opinion, the chairs are too hard. 3) The library opens at nine. Escribe H u O para cada una.", "1 H, 2 O, 3 H", "Las oraciones 1 y 3 se pueden comprobar; la 2 es un juicio con in my opinion."),
        (ADULT + PARK + " ¿Cuál es un hecho? a) Dogs must wear a leash. b) I don't like the noisy ducks.", "a) Dogs must wear a leash.", "Es una regla que se puede comprobar."),
        (ADULT + NOTE + " ¿Qué palabra muestra que la hermana tiene una opinión distinta? a) believes b) costs", "a) believes", "Believes (cree) introduce lo que piensa la hermana."),
    ],
    [
        (ADULT + NOTE + " Pablo dice: «Es un hecho que el cuaderno es el más feo, porque lo dijo la persona». ¿Qué le responderías? a) que sigue siendo una opinión, porque otra persona piensa distinto b) que tiene razón porque lo dijo alguien", "a) que sigue siendo una opinión, porque otra persona piensa distinto", "La hermana dice que es hermoso; eso muestra que es una opinión."),
        (ADULT + LIB + " ¿Por qué «the best place» es una opinión? a) porque se basa en gustos y no se puede medir b) porque se dice en la mañana", "a) porque se basa en gustos y no se puede medir", "Best depende de lo que piensa quien habla."),
    ],
    [
        (ADULT + "«The match was on Saturday. Our team scored three goals. It was the most exciting match of the year, I think.» (match = partido, scored = anotó, goals = goles, exciting = emocionante). ¿Cuántas oraciones son hechos?", "2", "The match was on Saturday y Our team scored three goals se pueden comprobar; la tercera es opinión."),
        (ADULT + "«The cafeteria sells sandwiches for one thousand five hundred pesos. Honestly, the sandwiches are delicious. The cafeteria opens at eight.» (cafeteria = casino, sells = vende, delicious = delicioso). ¿Qué oración es la opinión? a) Honestly, the sandwiches are delicious. b) The cafeteria opens at eight.", "a) Honestly, the sandwiches are delicious.", "Delicious depende del gusto."),
    ],
    [(ADULT + "Escuchas una reseña: «The museum has three rooms. Entry costs two thousand pesos. In my opinion, the second room is the most interesting.» (museum = museo, rooms = salas, entry = entrada, interesting = interesante). Quieres pasar una tarde en el museo. ¿Qué dato debes confiar como hecho para planificar? a) que cuesta 2.000 pesos la entrada b) que la segunda sala es la más interesante", "a) que cuesta 2.000 pesos la entrada", "El precio es verificable; lo interesante es una opinión.")],
    [
        ("En Inglés de 8.º (OA 3, clase 3): ¿Qué es un hecho?", "Un dato que se puede comprobar", "Por ejemplo, una hora o una cantidad."),
        ("En Inglés de 8.º (OA 3, clase 3): ¿por qué una opinión puede ser distinta según la persona?", "Porque es lo que cada persona piensa o siente", "Otra persona puede pensar distinto."),
        ("¿Qué pregunta ayuda a distinguirlos?", "¿Puedo comprobarlo?", "Si se puede comprobar, es un hecho."),
    ],
    task("Un adulto lee dos veces este texto: «Our school canteen has twelve tables. It opens at eleven forty. I believe it is the cleanest room in the school. The soup is too salty, in my opinion.» (canteen = comedor, tables = mesas, cleanest = la más limpia, soup = sopa, salty = salada). Escribe dos hechos y dos opiniones, cada uno con la frase del texto que lo muestra.", "Hechos: tiene doce mesas; abre a las 11:40. Opiniones: I believe it is the cleanest room; the soup is too salty, in my opinion.", ["anota dos hechos del texto", "anota dos opiniones del texto", "cita la frase de apoyo"], ["hoja con cuatro respuestas", "nota del adulto"], ["poner cleanest como hecho", "no indicar la frase que lo muestra"], "Reconoce lo que clasificó bien y vuelve a escuchar las palabras I believe e in my opinion para ubicar las opiniones."),
    "Pide a un adulto que lea el texto de la biblioteca y levanta la mano cada vez que oigas una opinión.",
    "Escribe tres hechos y tres opiniones en español sobre tu sala de clases y márcalos con H y O.",
)

# ------------------------------------------------------------------ OA 3, clase 4
RAIN = "«There was a lot of rain last night, so the football field is wet. The match is cancelled because the field is dangerous. The teams will play next week.» (rain = lluvia, wet = mojada, cancelled = suspendido, dangerous = peligrosa, will play = jugarán)"
SLEEP = "«Dani did not sleep well because his neighbours had a party. So he was tired in class, and he forgot his homework. His teacher asked him if he was ill, but he said he only needed a good night's sleep.» (neighbours = vecinos, party = fiesta, tired = cansado, forgot = olvidó, homework = tarea, ill = enfermo)"
BUSLATE = "«The bus was late because there was an accident on the road. Many students arrived after eight, so the first class started ten minutes later. The teacher was kind and explained the lesson again.» (accident = accidente, road = camino, arrived = llegaron, kind = amable, explained = explicó)"

lesson(
    OA3, 4, MAT_L,
    "Aprenderé a reconocer relaciones de causa y efecto en textos escuchados con because y so. Sirve para entender por qué pasan las cosas y qué consecuencias tienen.",
    ["Sé que because introduce una razón y so introduce un resultado.", "Conozco los conectores then y also."],
    [
        "Una relación de causa y efecto (cause and effect) une dos hechos: la causa (cause) es lo que provoca algo y el efecto (effect) es lo que ocurre a consecuencia. En There was a lot of rain, so the football field is wet, la causa es la lluvia y el efecto es que la cancha está mojada.",
        "Dos palabras te ayudan a encontrarlas. Because (porque) va delante de la causa: The match is cancelled because the field is dangerous. Aquí la causa es que la cancha es peligrosa y el efecto es que el partido se suspende. So (por eso, así que) va delante del efecto: Dani was tired, so he forgot his homework. Aquí la causa es el cansancio y el efecto es olvidar la tarea.",
        "Para no confundirte, pregunta «¿por qué pasó?» para encontrar la causa y «¿qué pasó después a causa de eso?» para encontrar el efecto. Un mismo hecho puede ser efecto de una cosa y causa de otra, como la cancha mojada: efecto de la lluvia y causa de que se suspenda el partido.",
    ],
    [("cause", "causa: lo que provoca algo"), ("effect", "efecto: lo que ocurre a consecuencia"), ("because", "porque (va con la causa)"), ("so", "por eso, así que (va con el efecto)"), ("cancelled", "suspendido"), ("dangerous", "peligroso")],
    [
        ("Encontrar la causa", ADULT + RAIN + " ¿Por qué se suspende el partido?", ["La causa va con because.", "Dice because the field is dangerous.", "La cancha está mojada y es peligrosa."], "Porque la cancha es peligrosa"),
        ("Encontrar el efecto", ADULT + SLEEP + " ¿Qué le pasó a Dani en clases por dormir mal?", ["Busco la palabra so.", "Dice So he was tired in class, and he forgot his homework.", "El efecto es estar cansado y olvidar la tarea."], "Estaba cansado y olvidó la tarea"),
    ],
    [
        ("Poner la causa donde va el efecto: «el partido se suspende porque la lluvia es peligrosa».", "Se mezclan causas y efectos; la lluvia causa la cancha mojada.", "Pregunta ¿qué provoca a qué? y ordena la cadena."),
        ("Decir que so introduce la razón.", "So introduce el resultado; la razón va con because.", "Recuerda: because = razón, so = resultado."),
    ],
    [
        (ADULT + RAIN + " ¿Por qué la cancha está mojada? a) porque llovió mucho anoche b) porque limpiaron la cancha", "a) porque llovió mucho anoche", "Dice There was a lot of rain last night, so the football field is wet."),
        (ADULT + SLEEP + " ¿Por qué Dani durmió mal? a) porque sus vecinos hicieron una fiesta b) porque estaba enfermo", "a) porque sus vecinos hicieron una fiesta", "Dice because his neighbours had a party."),
        (ADULT + BUSLATE + " ¿Por qué el bus llegó tarde? a) porque hubo un accidente en el camino b) porque el chofer se perdió", "a) porque hubo un accidente en el camino", "Dice because there was an accident on the road."),
    ],
    [
        (ADULT + BUSLATE + " ¿Qué efecto tuvo la llegada tarde de los estudiantes? a) la primera clase empezó diez minutos más tarde b) cerraron el colegio", "a) la primera clase empezó diez minutos más tarde", "Dice so the first class started ten minutes later."),
        (ADULT + RAIN + " ¿Cuándo jugarán los equipos? a) la próxima semana b) esta noche c) mañana", "a) la próxima semana", "Dice The teams will play next week."),
        (ADULT + SLEEP + " ¿Qué dijo Dani que necesitaba? a) una buena noche de sueño b) un día libre", "a) una buena noche de sueño", "Dice he only needed a good night's sleep."),
    ],
    [
        (ADULT + SLEEP + " Ordena la cadena de hechos con los números: (1) olvidó la tarea, (2) los vecinos hicieron una fiesta, (3) estaba cansado en clases.", "2, 3, 1", "La fiesta causó el mal sueño, el cansancio y luego el olvido de la tarea."),
        (ADULT + RAIN + " ¿Cuál es el efecto de que la cancha sea peligrosa? a) el partido se suspende b) llueve más", "a) el partido se suspende", "Dice the match is cancelled because the field is dangerous."),
        (ADULT + BUSLATE + " ¿Qué hizo la profesora al ver que llegaron tarde? a) explicó la lección otra vez b) los castigó", "a) explicó la lección otra vez", "Dice The teacher was kind and explained the lesson again."),
    ],
    [
        (ADULT + RAIN + " Camila dice: «El partido se suspende porque llueve en la ciudad». ¿Qué detalle del texto corrige su respuesta? a) la causa directa es que la cancha es peligrosa b) la causa es que los equipos no vinieron", "a) la causa directa es que la cancha es peligrosa", "La lluvia mojó la cancha, y eso la hizo peligrosa."),
        (ADULT + SLEEP + " ¿Cuál de estas dos frases es causa y cuál es efecto? Frase 1: «Dani was tired in class». Frase 2: «His neighbours had a party». a) la frase 2 es causa y la frase 1 es efecto b) la frase 1 es causa y la frase 2 es efecto", "a) la frase 2 es causa y la frase 1 es efecto", "La fiesta provocó el cansancio."),
    ],
    [
        (ADULT + "«The power went out at school, so the computers did not work. Because of that, the class used books instead.» (power = electricidad, went out = se cortó, computers = computadores, instead = en su lugar). ¿Cuál es el efecto de que se cortara la electricidad? a) los computadores no funcionaron b) los libros se perdieron", "a) los computadores no funcionaron", "So introduce el efecto: los computadores no funcionaron."),
        (ADULT + "«Tomás was hungry because he skipped breakfast. So he ate a big sandwich at ten o'clock.» (hungry = con hambre, skipped = se saltó, ate = comió). ¿Cuál es la causa de que Tomás comiera un sándwich grande? a) tenía hambre porque no desayunó b) tenía mucho dinero", "a) tenía hambre porque no desayunó", "Because muestra la causa del hambre y so el efecto."),
    ],
    [(ADULT + "En la radio escolar oyes: «The pool is closed today because the water filter is broken. So swimming class will be in the gym.» (pool = piscina, filter = filtro, broken = roto, swimming = natación). Si tienes natación hoy, ¿dónde será la clase y por qué? a) en el gimnasio, porque el filtro de la piscina está roto b) en la piscina, porque el filtro funciona", "a) en el gimnasio, porque el filtro de la piscina está roto", "Because da la causa y so el efecto: la clase se traslada.")],
    [
        ("¿Qué palabra va con la causa?", "Because", "Because significa porque."),
        ("¿Qué palabra introduce el efecto?", "So", "So significa por eso o así que."),
        ("En Inglés de 8.º (OA 3, clase 4): ¿Qué es un efecto?", "Lo que ocurre a consecuencia de otra cosa", "Es el resultado de una causa."),
    ],
    task("Un adulto lee dos veces este texto: «Last Monday, Clara forgot her umbrella, so she got wet on the way to school. Because her shoes were wet, she took them off in class, and the teacher gave her a dry pair from the lost-and-found box.» (umbrella = paraguas, got wet = se mojó, took off = se sacó, dry = seco, lost-and-found = objetos perdidos). Escribe una causa y su efecto que oíste, y una segunda causa con su efecto.", "Causa: olvidó el paraguas; efecto: se mojó. Causa: sus zapatos estaban mojados; efecto: se los sacó y recibió un par seco.", ["identifica dos pares causa-efecto", "usa so o because para unirlos", "no cambia causa por efecto"], ["hoja con dos pares", "nota del adulto"], ["poner el efecto como causa", "no indicar el segundo par"], "Reconoce el par que acertó y revisa con las palabras so y because cuál es la causa de cada hecho."),
    "Pide a un adulto que lea el texto de la lluvia y subraya las palabras because y so.",
    "Escribe en español dos frases con porque y dos con por eso sobre algo que te pasó esta semana.",
)

# ------------------------------------------------------------------ OA 3, clase 5
PICNIC = "«Listen to the plan for the picnic. If it is sunny on Saturday, we will meet at the lake at ten. If it rains, the picnic will be on Sunday at the same time. If you can't come, please tell Maya. If you bring juice, I will bring the sandwiches.» (picnic = picnic, lake = lago, same time = misma hora, juice = jugo, sandwiches = sándwiches)"
FEST = "«Hi, everyone. This is Gonzalo from the science club. I think our fair is the best event of the year. It is on Friday at four, in the gym. If you come early, you will get a free badge. Because the gym is small, only two hundred people can enter. So please arrive on time.» (fair = feria, event = evento, early = temprano, badge = insignia, small = pequeño, enter = entrar, on time = a tiempo)"

lesson(
    OA3, 5, MAT_L,
    "Aprenderé a reconocer condiciones (if ... will) y a combinar propósito, hecho y opinión, causa y efecto en un mismo texto escuchado. Sirve para entender mensajes completos de forma independiente.",
    ["Sé reconocer hechos y opiniones.", "Conozco because y so."],
    [
        "Una condición (condition) dice qué pasa si ocurre algo. En inglés se forma con if + presente en la primera parte y will + verbo en la segunda parte: If it rains, the picnic will be on Sunday (Si llueve, el picnic será el domingo). La parte con if es la condición y la parte con will es el resultado. Si la condición no se cumple, el resultado no ocurre.",
        "Presta atención a todas las condiciones de un texto, porque cada una cambia el plan. If it is sunny, we will meet at the lake at ten. If it rains, the picnic will be on Sunday. Son dos condiciones opuestas con dos resultados distintos. También hay condiciones sobre personas: If you bring juice, I will bring the sandwiches (si tú traes jugo, yo traeré los sándwiches).",
        "En un texto completo conviene preguntar en este orden: ¿cuál es el propósito?, ¿qué datos son hechos?, ¿qué frases son opiniones?, ¿qué es causa y qué es efecto? y ¿qué dicen las condiciones? Así combinas todo lo que aprendiste y puedes responder con evidencia.",
    ],
    [("condition", "condición: lo que debe ocurrir para que pase otra cosa"), ("if", "si (introduce la condición)"), ("will", "futuro: hará o será"), ("result", "resultado de la condición"), ("early", "temprano"), ("on time", "a tiempo")],
    [
        ("Condición y resultado", ADULT + PICNIC + " ¿Qué pasa si llueve el sábado?", ["Busco la parte que empieza con If it rains.", "El resultado es the picnic will be on Sunday at the same time.", "La condición es la lluvia."], "El picnic será el domingo a la misma hora"),
        ("Hecho, opinión y causa", ADULT + FEST + " ¿Por qué solo pueden entrar doscientas personas?", ["Busco because.", "Dice Because the gym is small, only two hundred people can enter.", "La causa es que el gimnasio es pequeño."], "Porque el gimnasio es pequeño"),
    ],
    [
        ("Pensar que el resultado ocurre aunque la condición no se cumpla.", "El resultado depende de que se cumpla la parte con if.", "Pregunta: ¿se cumplió la condición?"),
        ("Tomar la opinión de Gonzalo como un hecho.", "I think our fair is the best event es un juicio, no un dato verificable.", "Busca I think, best y otros juicios."),
    ],
    [
        (ADULT + PICNIC + " ¿Qué ocurre si está soleado el sábado? a) se juntan en el lago a las diez b) el picnic es el domingo", "a) se juntan en el lago a las diez", "Dice If it is sunny on Saturday, we will meet at the lake at ten."),
        (ADULT + PICNIC + " ¿A quién hay que avisar si no se puede ir? a) a Maya b) a Gonzalo", "a) a Maya", "Dice If you can't come, please tell Maya."),
        (ADULT + FEST + " ¿Dónde es la feria de ciencias? a) en el gimnasio b) en el lago", "a) en el gimnasio", "Dice in the gym."),
    ],
    [
        (ADULT + PICNIC + " ¿Qué llevará quien habla si tú traes jugo? a) los sándwiches b) la música", "a) los sándwiches", "Dice If you bring juice, I will bring the sandwiches."),
        (ADULT + FEST + " ¿Qué recibe quien llega temprano? a) una insignia gratis b) una entrada doble", "a) una insignia gratis", "Dice If you come early, you will get a free badge."),
        (ADULT + FEST + " ¿Cuál es la opinión de Gonzalo? a) que la feria es el mejor evento del año b) que la feria es el viernes a las cuatro", "a) que la feria es el mejor evento del año", "I think ... best es un juicio; el día y la hora se pueden comprobar."),
    ],
    [
        (ADULT + FEST + " Clasifica como hecho (H) u opinión (O): 1) The fair is on Friday at four. 2) I think it is the best event. 3) Only two hundred people can enter. Escribe H u O.", "1 H, 2 O, 3 H", "Las oraciones 1 y 3 son verificables; la 2 es un juicio."),
        (ADULT + PICNIC + " Si llueve el sábado, ¿a qué hora será el picnic del domingo? a) a las diez b) a las doce", "a) a las diez", "El domingo será at the same time: a las diez."),
        (ADULT + FEST + " ¿Qué es la causa y qué es el efecto en «Because the gym is small, only two hundred people can enter»? a) causa: el gimnasio es pequeño; efecto: entran doscientas personas b) causa: entran doscientas; efecto: el gimnasio es pequeño", "a) causa: el gimnasio es pequeño; efecto: entran doscientas personas", "Because va con la causa."),
    ],
    [
        (ADULT + PICNIC + " Elena dice: «Si hay sol el sábado, el picnic es el domingo». ¿Qué parte del texto muestra el error? a) If it rains, the picnic will be on Sunday b) We will meet at the lake at ten", "a) If it rains, the picnic will be on Sunday", "El domingo es solo si llueve."),
        (ADULT + FEST + " ¿Para qué se dice el mensaje? a) para invitar a una feria y pedir puntualidad b) para pedir ayuda con agua", "a) para invitar a una feria y pedir puntualidad", "Da día, hora, lugar y So please arrive on time."),
    ],
    [
        (ADULT + "«Hello, I'm Rocío. If you want to join the chess club, come to room six on Tuesday. The club is great fun, I believe. We are only eight members, so we need more players.» (join = unirse a, chess = ajedrez, great fun = muy entretenido, members = integrantes, players = jugadores). ¿Cuál de estas es una opinión? a) The club is great fun, I believe. b) We are only eight members.", "a) The club is great fun, I believe.", "Great fun y I believe expresan lo que piensa Rocío."),
        (ADULT + "«Hello, I'm Rocío. If you want to join the chess club, come to room six on Tuesday. We are only eight members, so we need more players.» (join = unirse a, room = sala, members = integrantes). Si quieres unirte al club, ¿qué debes hacer? a) ir a la sala seis el martes b) llamar a Rocío el lunes", "a) ir a la sala seis el martes", "La condición If you want to join lleva a come to room six on Tuesday."),
    ],
    [(ADULT + "Tu curso recibe este mensaje: «Dear students, the class trip is on Thursday. If it rains, we will go to the museum. If it is sunny, we will go to the park. I think the museum is more interesting, but the park is free.» (class trip = salida de curso, museum = museo, park = parque, interesting = interesante, free = gratis). Si el jueves está soleado, ¿a dónde van? a) al parque b) al museo", "a) al parque", "If it is sunny, we will go to the park.")],
    [
        ("¿Qué estructura tiene una condición en inglés?", "If + presente, will + verbo", "Por ejemplo, If it rains, we will stay."),
        ("En Inglés de 8.º (OA 3, clase 5): ¿Qué palabra marca la condición?", "If", "If significa si."),
        ("¿Qué preguntas haces para entender un texto completo?", "Propósito, hechos y opiniones, causa y efecto, y condiciones", "Combinan lo aprendido en OA 3."),
    ],
    task("Un adulto lee dos veces este texto: «Good evening. This is Leo from the school radio. Tomorrow is the book swap in the library. If you bring one book, you can take another one. I think it is a great idea because reading is fun. The library will be open from three to five.» (book swap = intercambio de libros, take = llevar, great idea = muy buena idea, reading = leer, open = abierto). Escribe el propósito, la condición con su resultado, una opinión y un hecho.", "Propósito: invitar al intercambio de libros. Condición: si traes un libro, puedes llevarte otro. Opinión: I think it is a great idea. Hecho: la biblioteca está abierta de 3 a 5.", ["dice el propósito", "anota la condición y su resultado", "separa una opinión y un hecho"], ["hoja con cuatro respuestas", "nota del adulto"], ["tomar la hora como opinión", "invertir la condición y el resultado"], "Reconoce lo que acertó y vuelve a escuchar las frases con if y con I think."),
    "Pide a un adulto que lea el picnic y escribe en una tabla dos condiciones con sus resultados.",
    "Escribe en español tres frases «si pasa A, entonces pasará B» sobre un plan de fin de semana.",
)

# ================================================================== OA 4, clase 1
FISH = "«Good morning! Fresh fish today. Salmon is eight thousand pesos a kilo, and hake is four thousand. Everything is on ice. Please ask for a bag, and don't touch the scale.» (fresh = fresco, salmon = salmón, hake = merluza, ice = hielo, bag = bolsa, scale = balanza)"

lesson(
    OA4, 1, MAT_L,
    "Aprenderé a prepararme antes de escuchar: hacer predicciones, usar lo que ya sé y fijar un propósito. Sirve para entender mejor los textos orales desde el comienzo.",
    ["Sé que puedo adivinar de qué trata un texto por su título.", "Conozco palabras como fish, kilo y price."],
    [
        "Antes de escuchar (before listening) puedes prepararte con tres estrategias. La primera es hacer una predicción (prediction): usar el título, una imagen o la situación para adivinar de qué hablará el texto y qué palabras aparecerán. Si el título es A Morning at the Fish Market y la imagen muestra cajas con hielo y una balanza, puedes predecir palabras como fish, kilo, price, fresh y ice.",
        "La segunda estrategia es usar tus conocimientos previos (prior knowledge): lo que ya sabes del tema. Si has estado en una pescadería o caleta, sabes que se venden pescados por kilo, que se guardan en hielo y que un cartel da el precio. Eso te ayuda a esperar números y nombres de pescados. La tercera es escuchar con un propósito: decidir qué quieres averiguar, por ejemplo, ¿cuánto cuesta un kilo de merluza?",
        "Las predicciones son hipótesis: pueden acertar o no. Lo importante es anotarlas antes y revisarlas después. Escribe tres palabras que esperas oír y una pregunta que quieres responder. Mientras escuchas, busca esas palabras y esa respuesta.",
    ],
    [("prediction", "predicción: adivinar qué dirá el texto"), ("prior knowledge", "conocimientos previos: lo que ya sabes"), ("title", "título"), ("purpose for listening", "propósito de escucha: lo que quieres averiguar"), ("picture", "imagen"), ("hypothesis", "hipótesis: idea que luego se comprueba")],
    [
        ("Predecir palabras", "Antes de escuchar, ves el título «A Morning at the Fish Market» y una foto de cajas con hielo y una balanza. ¿Qué palabras esperarías oír?", ["El título y la foto hablan de una pescadería.", "La balanza sugiere kilo y la caja con hielo sugiere fresh.", "Espero fish, kilo, price e ice."], "Fish, kilo, price, ice y fresh"),
        ("Fijar un propósito", "Quieres saber cuánto cuesta un kilo de merluza (hake). ¿Qué dato debes buscar al escuchar?", ["Mi propósito es el precio de un pescado.", "Debo atender números y la palabra hake.", "Escucho hake y el número que la acompaña."], "El número que acompaña a la palabra hake"),
    ],
    [
        ("Empezar a escuchar sin ninguna idea previa del tema.", "Sin predicciones es más difícil seguir el texto desde el comienzo.", "Mira el título o la imagen y escribe tres palabras que esperas."),
        ("Creer que una predicción equivocada es un fracaso.", "Una predicción es una hipótesis: se comprueba y se corrige.", "Corrígela cuando el texto diga otra cosa."),
    ],
    [
        ("Si el título es «A Morning at the Fish Market», ¿qué palabra es más probable que aparezca? a) kilo b) homework", "a) kilo", "En un mercado de pescado se venden productos por kilo."),
        ("Ves una imagen con una balanza y cajas con hielo. ¿Qué tema predices? a) la venta de pescado fresco b) una clase de matemática", "a) la venta de pescado fresco", "La balanza y el hielo son pistas de una pescadería."),
        ("¿Qué es una predicción? a) adivinar de qué hablará el texto antes de escucharlo b) resumir el texto después de escucharlo", "a) adivinar de qué hablará el texto antes de escucharlo", "Se hace antes de escuchar."),
    ],
    [
        (ADULT + FISH + " ¿Cuánto cuesta un kilo de merluza? a) 4.000 pesos b) 8.000 pesos", "a) 4.000 pesos", "Dice hake is four thousand."),
        (ADULT + FISH + " ¿Dónde están los pescados? a) sobre hielo b) en bolsas de plástico", "a) sobre hielo", "Dice Everything is on ice."),
        (ADULT + FISH + " ¿Qué pescado es más caro? a) el salmón b) la merluza", "a) el salmón", "El salmón cuesta 8.000 pesos el kilo y la merluza 4.000."),
    ],
    [
        ("Vas a escuchar un texto con el título «Rules at the Swimming Pool». Escribe qué palabra esperarías oír: a) lifeguard (salvavidas) b) mushroom (hongo)", "a) lifeguard (salvavidas)", "Lifeguard (salvavidas) es una persona de una piscina."),
        ("Vas a escuchar un texto sobre «A Day at the Dentist». ¿Qué conocimiento previo te ayuda? a) que se revisan los dientes y se usa un cepillo b) que se compran zapatos", "a) que se revisan los dientes y se usa un cepillo", "Lo que sabes de una visita al dentista te ayuda a esperar el vocabulario."),
        (ADULT + FISH + " Tenías el propósito de saber cuánto cuesta un salmón (salmon). ¿Qué dato respondes? a) 8.000 pesos el kilo b) 4.000 pesos el kilo", "a) 8.000 pesos el kilo", "Dice Salmon is eight thousand pesos a kilo."),
    ],
    [
        ("Antes de escuchar, Rosa predice: «El texto hablará de ropa». Si el título es «A Morning at the Fish Market», ¿qué le dirías? a) que su predicción no coincide con el título y debe cambiarla b) que su predicción es correcta", "a) que su predicción no coincide con el título y debe cambiarla", "El título habla de pescado, no de ropa."),
        ("¿Por qué conviene fijar un propósito de escucha? a) porque ayuda a atender los datos que importan b) porque evita que se escuche el texto completo", "a) porque ayuda a atender los datos que importan", "Con un propósito escuchas buscando algo concreto."),
    ],
    [
        ("Ves una foto de una cocina escolar con ollas, pan y una profesora con delantal. El título dice «Lunch for Everyone». Entre estas palabras en inglés: soup (sopa), bread (pan), spoon (cuchara), aeroplane (avión), ¿cuál NO esperarías oír? a) aeroplane b) soup", "a) aeroplane", "Soup, bread y spoon son comunes en una cocina."),
        (ADULT + FISH + " Predijiste que oirías el precio de dos pescados. ¿Cuántos precios oyes en el texto?", "2", "Hay dos precios: el salmón y la merluza."),
    ],
    [("Vas a una feria y alguien te dice que escucharás un aviso sobre «Lost Pets». Piensas: ¿qué palabras puedo esperar? ¿Cuál es más probable? a) dog (perro) b) skyscraper (rascacielos)", "a) dog (perro)", "Una mascota perdida suele ser un perro o un gato.")],
    [
        ("En Inglés de 8.º (OA 4, clase 1): ¿cómo te ayudan los conocimientos previos antes de escuchar?", "A esperar palabras y datos del tema", "Lo que ya sabes del tema te ayuda a esperar palabras y datos."),
        ("En Inglés de 8.º (OA 4, clase 1): ¿Qué es escuchar con un propósito?", "Decidir qué quieres averiguar antes de escuchar", "Ayuda a atender los datos clave."),
        ("¿Una predicción siempre acierta?", "No, se comprueba y se corrige", "Es una hipótesis."),
    ],
    task("Lee este título y esta descripción de imagen: «A Rainy Day at the Bus Stop» (un paradero con personas con paraguas y un bus que se acerca). Antes de escuchar, escribe tres palabras que esperas oír, una cosa que ya sabes del tema y una pregunta que quieres responder.", "Palabras: rain, umbrella, bus. Previo: en días de lluvia el bus se atrasa. Pregunta: ¿a qué hora llega el bus?", ["escribe tres palabras coherentes con el título", "dice un conocimiento previo", "formula una pregunta de propósito"], ["hoja con tres elementos", "nota del adulto"], ["escribir palabras que no tienen relación con el título", "no hacer una pregunta"], "Reconoce lo que acertó y relee el título para ajustar las palabras esperadas."),
    "Mira el título «Our School Library» y escribe tres palabras que esperas oír antes de que un adulto lea el texto.",
    "Elige un título de una película o un libro conocido y escribe cinco palabras que predices que aparecerán en una escucha sobre él.",
)

# ------------------------------------------------------------------ OA 4, clase 2
FLAG = "«Guide (holding up a small red flag): Everyone, follow the red flag. (She points to the left.) We go this way. (She shows ten fingers.) We have ten minutes. (She puts a finger on her lips.) Please be quiet in the next room.» (guide = guía, flag = bandera, follow = sigan, points = señala, fingers = dedos, lips = labios, quiet = en silencio, next room = sala siguiente)"
COLD = "«Teacher (hugging herself and shivering): It is freezing today! (She shows a picture of a snowman on the board.) Today's topic is winter. (She points to the window, where it is raining.) Today we are staying inside.» (hugging herself = abrazándose, shivering = temblando, freezing = muy frío, snowman = muñeco de nieve, board = pizarra, window = ventana, staying = quedándonos, inside = adentro)"

lesson(
    OA4, 2, MAT_L,
    "Aprenderé a usar estrategias mientras escucho: atender palabras clave y apoyarme en imágenes y en los gestos del hablante. Sirve para entender aunque aparezcan palabras que no conozco.",
    ["Sé que puedo hacer predicciones antes de escuchar.", "Conozco palabras como cold, window y quiet."],
    [
        "Mientras escuchas (during listening) puedes usar dos estrategias muy útiles. La primera es focalizar la atención en palabras o expresiones clave: números, nombres, verbos y palabras que se repiten o que el hablante dice más fuerte o más despacio. No intentes entender cada palabra; atiende las que llevan el significado.",
        "La segunda es utilizar apoyos: imágenes, objetos y gestos del hablante (gestures). Si el guía levanta una bandera roja y dice follow the red flag, entiendes que debes seguir la bandera. Si muestra diez dedos y dice ten minutes, el gesto confirma el número. Si la profesora se abraza a sí misma y tirita al decir freezing, entiendes que freezing quiere decir muy frío, aunque no conozcas la palabra.",
        "Los gestos y las imágenes confirman el significado, pero conviene comprobarlo con las palabras. Si el gesto y la palabra coinciden, tu respuesta es más segura. Si no coinciden, escucha otra vez. Los textos de esta clase traen entre paréntesis lo que hace el hablante.",
    ],
    [("key words", "palabras clave: las que llevan el significado"), ("gesture", "gesto: movimiento que ayuda a comunicar"), ("support", "apoyo: imagen, objeto o gesto que ayuda"), ("follow", "seguir"), ("freezing", "muy frío"), ("shiver", "temblar de frío")],
    [
        ("Gesto y palabra", ADULT + FLAG + " ¿Cuánto tiempo tienen y cómo lo confirma el gesto?", ["El guía dice ten minutes.", "Muestra diez dedos.", "El gesto confirma el número diez."], "Diez minutos; el gesto de diez dedos lo confirma"),
        ("Deducir una palabra nueva", ADULT + COLD + " La profesora se abraza y tirita al decir «freezing». ¿Qué significa?", ["No conozco la palabra freezing.", "Se abraza y tirita mientras dice que hace mucho frío.", "El gesto indica frío intenso."], "Muy frío"),
    ],
    [
        ("Ignorar los gestos del hablante.", "Los gestos entregan información que confirma o aclara las palabras.", "Mira al hablante o lee las acciones entre paréntesis."),
        ("Quedarse en una palabra que no se entiende y perder el resto.", "Se pierde el hilo del texto.", "Sigue escuchando las palabras clave y vuelve después a la palabra dudosa."),
    ],
    [
        (ADULT + FLAG + " ¿Qué debe seguir el grupo? a) la bandera roja b) a la profesora", "a) la bandera roja", "Dice follow the red flag."),
        (ADULT + FLAG + " ¿Hacia dónde señala la guía? a) hacia la izquierda b) hacia la derecha", "a) hacia la izquierda", "Dice She points to the left."),
        (ADULT + COLD + " ¿Cuál es el tema de hoy? a) el invierno b) el verano", "a) el invierno", "Dice Today's topic is winter."),
    ],
    [
        (ADULT + FLAG + " Cuando la guía se pone un dedo sobre los labios, ¿qué pide? a) silencio en la sala siguiente b) que se grite", "a) silencio en la sala siguiente", "El gesto y la frase be quiet coinciden."),
        (ADULT + COLD + " ¿Qué muestra en la pizarra? a) un muñeco de nieve b) una flor", "a) un muñeco de nieve", "Dice She shows a picture of a snowman."),
        (ADULT + COLD + " ¿Por qué se quedan adentro? a) porque está lloviendo b) porque hace calor", "a) porque está lloviendo", "La profesora señala la ventana, donde llueve."),
    ],
    [
        ("Un guía dice «Please wait here» y abre la palma de la mano hacia ti, como para detenerte. ¿Qué te pide? a) que esperes en ese lugar b) que corras", "a) que esperes en ese lugar", "El gesto de detenerte coincide con wait here."),
        ("Un hablante dice «It is enormous!» y abre los brazos todo lo que puede. ¿Qué significa enormous? a) muy grande b) muy pequeño", "a) muy grande", "El gesto de abrir los brazos muestra gran tamaño."),
        ("Un hablante dice «Look at this tiny seed» y junta el dedo pulgar con el índice, casi sin espacio. ¿Qué significa tiny? a) diminuto b) pesado", "a) diminuto", "El gesto muestra algo muy pequeño."),
    ],
    [
        ("Alguien dice «Turn to the right» y señala hacia la izquierda. ¿Qué haces? a) escuchas otra vez porque las palabras y el gesto no coinciden b) sigues solo el gesto", "a) escuchas otra vez porque las palabras y el gesto no coinciden", "Si no coinciden, conviene comprobar con la palabra."),
        (ADULT + FLAG + " ¿Por qué ten minutes es una palabra clave en este texto? a) porque dice cuánto tiempo tienen b) porque nombra una sala", "a) porque dice cuánto tiempo tienen", "Es un dato de tiempo que necesita el grupo."),
    ],
    [
        (ADULT + "«Coach (clapping twice): Team, line up! (He points to a rope on the grass.) Stand behind the rope. (He lifts three fingers.) Three laps today.» (coach = entrenador, clapping = aplaudiendo, line up = formen una fila, rope = cuerda, grass = pasto, behind = detrás de, laps = vueltas). ¿Cuántas vueltas hay hoy?", "3", "El entrenador dice three laps y levanta tres dedos."),
        (ADULT + "«Coach (clapping twice): Team, line up! (He points to a rope on the grass.) Stand behind the rope.» (line up = formen fila, rope = cuerda, behind = detrás de). ¿Dónde deben ponerse? a) detrás de la cuerda b) delante de la cuerda", "a) detrás de la cuerda", "Behind the rope significa detrás de la cuerda; el gesto señala la cuerda."),
    ],
    [(ADULT + "En un aeropuerto, una empleada dice: «Please show your boarding pass (she lifts a small paper card) and put your bag here (she taps a grey table).» (boarding pass = tarjeta de embarque, bag = bolso, taps = golpea suavemente, grey = gris). ¿Qué debes poner sobre la mesa gris? a) tu bolso b) tu tarjeta de embarque", "a) tu bolso", "El gesto señala la mesa gris y put your bag here lo confirma.")],
    [
        ("¿Qué estrategia usas cuando miras los gestos del hablante?", "Utilizar apoyos", "Los gestos confirman el significado."),
        ("En Inglés de 8.º (OA 4, clase 2): ¿Qué palabras conviene atender mientras escuchas?", "Las palabras clave", "Son las que llevan el significado."),
        ("¿Qué haces si el gesto y la palabra no coinciden?", "Escuchar otra vez y comprobar", "Así se evitan los malentendidos."),
    ],
    task("Un adulto lee dos veces este texto con acciones: «Mr. Tapia (holding a green cup): This is for the plants. (He pours water slowly.) A little water every day. (He shows two fingers.) Two plants only. (He puts a hand on his head.) I forgot the third one!» (cup = taza, pours = vierte, slowly = lentamente, fingers = dedos, forgot = olvidó, third = tercera). Escribe qué hace el hablante, cuántas plantas riega y qué olvidó, apoyándote en las acciones.", "Riega las plantas con un poco de agua cada día; riega dos plantas; olvidó la tercera.", ["usa las acciones del paréntesis", "anota el número de plantas", "dice qué olvidó"], ["hoja con tres respuestas", "nota del adulto"], ["decir que riega tres plantas", "no usar las acciones como pista"], "Reconoce las pistas que usó y vuelve a escuchar el gesto de las manos sobre la cabeza para entender lo que olvidó."),
    "Pide a un adulto que lea el texto del guía y señala con tu dedo la acción que acompaña a cada frase.",
    "Escribe una instrucción corta en español con un gesto entre paréntesis para que otra persona la actúe y pídele que adivine el significado.",
)

# ------------------------------------------------------------------ OA 4, clase 3
lesson(
    OA4, 3, MAT_L,
    "Aprenderé a preguntar para clarificar o confirmar información en una conversación: repetir, aclarar, deletrear y comprobar. Sirve para entender bien cuando algo no se oyó claro.",
    ["Sé hacer preguntas con what, where y when.", "Conozco palabras como slowly, repeat y spell."],
    [
        "Cuando algo no se entiende, no hay que quedarse callado. Hay frases para pedir ayuda. Para pedir que repitan: Sorry, could you repeat that, please? Para pedir que hablen más despacio: Could you speak more slowly? Para pedir el significado: What does «ticket» mean? Para pedir cómo se escribe: How do you spell that? Estas preguntas se llaman preguntas para clarificar (clarifying questions).",
        "Otro tipo de pregunta sirve para corroborar (to check), es decir, para comprobar que entendiste bien. Se hacen repitiendo lo que crees haber oído y agregando una pregunta corta: So the meeting is at four, right? Do you mean next Monday? Is that correct? Si la otra persona dice yes, tu información está confirmada; si dice no, te corrige.",
        "Una buena pregunta es breve, educada y específica. Usa Sorry o Excuse me al comienzo, nombra la parte exacta que dudas y espera la respuesta. Por ejemplo, en vez de decir solo «No entendí», di Sorry, did you say fifteen or fifty? Así la otra persona sabe qué repetir.",
    ],
    [("clarify", "aclarar: pedir que expliquen mejor"), ("check / confirm", "comprobar / confirmar"), ("Could you repeat that?", "¿Podría repetir eso?"), ("How do you spell that?", "¿Cómo se escribe eso?"), ("Do you mean...?", "¿Quiere decir...?"), ("right?", "¿cierto?")],
    [
        ("Pedir que repitan", "Alguien te dice rápido: «The party is on the twelfth». No oíste el día. ¿Qué dices para pedir que lo repita?", ["Necesito que repita la información.", "Una frase educada es Sorry, could you repeat that, please?", "Así me lo dice otra vez."], "Sorry, could you repeat that, please?"),
        ("Confirmar un dato", "Entendiste que la reunión es a las cuatro. ¿Qué dices para comprobarlo con la otra persona?", ["Repito lo que creo haber oído.", "Agrego una pregunta corta.", "So the meeting is at four, right?"], "So the meeting is at four, right?"),
    ],
    [
        ("Quedarse callado cuando no se entendió.", "Se pierde información y se puede actuar con datos equivocados.", "Usa una frase para pedir que repitan o aclaren."),
        ("Decir solo «What?» de forma brusca.", "Puede sonar poco amable y no dice qué parte falta.", "Usa Sorry, could you repeat that, please? o nombra la parte dudosa."),
    ],
    [
        ("No oíste un nombre. ¿Qué frase sirve para pedir que te lo deletreen? a) How do you spell that? b) What does that mean?", "a) How do you spell that?", "How do you spell that? pide las letras del nombre."),
        ("Una persona habla muy rápido. ¿Qué dices? a) Could you speak more slowly, please? b) Could you speak louder, please?", "a) Could you speak more slowly, please?", "Pide que hablen más despacio."),
        ("No sabes qué significa la palabra «ticket». ¿Qué preguntas? a) What does ticket mean? b) What is the price of the ticket?", "a) What does ticket mean?", "What does ... mean? pregunta el significado."),
    ],
    [
        ("Te dicen «The bus leaves at eight fifteen». Quieres confirmar. ¿Cuál es la mejor pregunta? a) So the bus leaves at eight fifteen, right? b) Is the bus full?", "a) So the bus leaves at eight fifteen, right?", "Repite el dato y pregunta si es correcto."),
        ("Dudas entre fifteen y fifty. ¿Qué preguntas? a) Did you say fifteen or fifty? b) Did you say fifteen or sixteen?", "a) Did you say fifteen or fifty?", "Nombra las dos posibilidades que dudas."),
        ("Una profesora dice «Next Monday». No estás seguro si habla del lunes de esta semana. ¿Qué preguntas? a) Do you mean next week? b) Is Monday a good day?", "a) Do you mean next week?", "Do you mean...? comprueba el significado."),
    ],
    [
        ("Ordena la conversación en inglés para confirmar un dato. Frases: 1) Yes, that's right. 2) The test is on Thursday. 3) So the test is on Thursday, right? Escribe los números en orden.", "2, 3, 1", "Primero dicen el dato, luego se confirma con una pregunta y por último responden."),
        ("Quieres que repitan solo el precio, no todo el mensaje. ¿Qué dices? a) Sorry, how much is it again? b) Sorry, where is the shop?", "a) Sorry, how much is it again?", "How much is it again? pide repetir el precio."),
        ("Quieres confirmar que escuchaste bien el lugar: «in the library». ¿Cuál frase sirve? a) Is that in the library? b) Is that on Sunday?", "a) Is that in the library?", "Pregunta por el dato que no estabas seguro."),
    ],
    [
        ("Daniel responde «yes» a tu pregunta «So the party is on Saturday, right?». ¿Qué significa? a) que tu información está confirmada b) que debes preguntar de nuevo", "a) que tu información está confirmada", "Yes confirma el dato."),
        ("Elena dice «Sorry, I don't understand». ¿Cuál es la mejor continuación para ayudar a la otra persona? a) nombrar la parte que no entendió, como: I didn't understand the date b) quedarse en silencio", "a) nombrar la parte que no entendió, como: I didn't understand the date", "Una pregunta específica ayuda a que le repitan solo lo necesario."),
    ],
    [
        ("Alguien dice: «The key is in room fourteen». Tú entendiste «room forty». ¿Qué pregunta ayuda más? a) Did you say fourteen or forty? b) Whose key is it?", "a) Did you say fourteen or forty?", "Aclara la confusión entre dos números parecidos."),
        ("En una conversación, la otra persona usa una palabra que no conoces: «recipe». ¿Cuál es la mejor secuencia? a) Sorry, what does recipe mean? Then I confirm: So it is a list for cooking, right? b) Say nothing and guess", "a) Sorry, what does recipe mean? Then I confirm: So it is a list for cooking, right?", "Primero aclaras el significado y luego lo confirmas."),
    ],
    [("En una tienda, la vendedora dice rápido: «It costs six thousand nine hundred». Quieres estar seguro. ¿Qué frase eliges? a) Sorry, did you say six thousand nine hundred? b) Sorry, what colour is it?", "a) Sorry, did you say six thousand nine hundred?", "Repite el precio que entendiste y pides confirmación.")],
    [
        ("¿Qué frase pide que repitan?", "Sorry, could you repeat that, please?", "Es una frase cortés para pedir repetición."),
        ("En Inglés de 8.º (OA 4, clase 3): ¿Para qué sirve «Do you mean...?»?", "Para comprobar el significado", "Corrobora lo que entendiste."),
        ("¿Qué pregunta pide las letras de una palabra?", "How do you spell that?", "Pide el deletreo."),
    ],
    task("Lee esta situación: un amigo te deja un mensaje de voz que no se oye bien: «Meet me at... the gate... at... twelve... or twenty?» Escribe tres preguntas en inglés: una para pedir que repita, una para aclarar entre dos horas y una para confirmar la hora que crees (twelve).", "Sorry, could you repeat that, please? Did you say twelve or twenty? So we meet at the gate at twelve, right?", ["escribe tres preguntas en inglés", "una aclara dos opciones", "una confirma el dato"], ["hoja con tres preguntas", "nota del adulto"], ["preguntar algo distinto del mensaje", "no incluir la confirmación"], "Reconoce las preguntas útiles y corrige solo la que no aclara la duda."),
    "Practica con un adulto: él dice un número de teléfono falso de ejemplo y tú pides que lo repita despacio y lo confirmas.",
    "Escribe un diálogo de cuatro líneas en inglés en que una persona pide aclarar una hora y otra la confirma.",
)

# ------------------------------------------------------------------ OA 4, clase 4
WATER = "«Today I will talk about how to save water at home. Turn off the tap when you brush your teeth. Take shorter showers. Fix leaks quickly, because a small leak wastes a lot of water in a month.» (save = ahorrar, tap = llave, brush = cepillar, teeth = dientes, shorter showers = duchas más cortas, fix = reparar, leaks = filtraciones, wastes = desperdicia)"
VISIT = "«Hello, I'm Dr. Soto. Today we will visit the school bees. Please wear long sleeves and stay behind the yellow line. If you are allergic to bee stings, tell the teacher first. A beekeeper will open the hive, and we will see how the bees make honey.» (allergic = alérgico, stings = picaduras, tell = avisa, bees = abejas, long sleeves = mangas largas, behind = detrás de, line = línea, beekeeper = apicultor, hive = colmena, honey = miel)"

lesson(
    OA4, 4, MAT_L,
    "Aprenderé a confirmar o corregir mis predicciones después de escuchar y a usar la evidencia del texto. Sirve para saber si entendí bien y corregir lo que no coincidió.",
    ["Sé hacer predicciones antes de escuchar.", "Conozco palabras como save, water y bees."],
    [
        "Después de escuchar (after listening), revisa lo que habías predicho. Una predicción puede confirmarse (el texto dice lo que esperabas), confirmarse en parte o corregirse (el texto dice otra cosa). Esto se hace con evidencia: una palabra o una frase del texto que apoye tu decisión.",
        "Por ejemplo, antes de escuchar predices: «El texto habla de cómo ahorrar energía en casa». Escuchas: Today I will talk about how to save water at home. Tu predicción se confirmó en parte, porque habla de ahorrar en casa, pero se corrigió: el tema es el agua, no la energía. La evidencia es la frase save water at home.",
        "Para revisar, usa tres pasos: 1) lee tu predicción, 2) busca en el texto una frase que coincida o que la contradiga, 3) escribe la predicción corregida. También puedes revisar tus palabras esperadas: marca las que sí aparecieron y agrega las nuevas que escuchaste. Así tu comprensión mejora en cada escucha.",
    ],
    [("confirm", "confirmar: comprobar que algo era cierto"), ("revise / correct", "corregir: cambiar lo que no coincidía"), ("evidence", "evidencia: palabra o frase que apoya una respuesta"), ("partly", "en parte"), ("prediction", "predicción: lo que se espera antes de escuchar"), ("save", "ahorrar")],
    [
        ("Corregir una predicción", ADULT + WATER + " Antes de escuchar predijiste: «El texto habla de ahorrar energía en casa». ¿Se confirma? ¿Qué frase lo prueba?", ["El texto habla de ahorrar en casa.", "Pero dice save water, no energía.", "La evidencia es Today I will talk about how to save water at home."], "Se confirma en parte: ahorrar en casa; se corrige a ahorrar agua"),
        ("Confirmar una predicción", ADULT + VISIT + " Predijiste que oirías la palabra bees. ¿Aparece?", ["Busco bees en el texto.", "Dice we will visit the school bees.", "Aparece, así que se confirma."], "Sí, aparece: se confirma"),
    ],
    [
        ("Mantener la predicción aunque el texto diga otra cosa.", "Se ignora la evidencia del texto.", "Corrige la predicción con una frase del texto."),
        ("Decir que la predicción estaba mal solo porque no se confirmó una palabra.", "Una predicción puede estar bien en parte.", "Revisa qué parte coincide y qué parte se corrige."),
    ],
    [
        (ADULT + WATER + " ¿Cuál es el tema real? a) ahorrar agua en casa b) ahorrar energía en casa", "a) ahorrar agua en casa", "Dice how to save water at home."),
        (ADULT + VISIT + " Predijiste «una visita al colegio». ¿Se confirma? a) sí, dice we will visit the school bees b) no, habla de una clínica", "a) sí, dice we will visit the school bees", "Dr. Soto presenta una visita a las abejas del colegio."),
        (ADULT + VISIT + " ¿Qué ropa se pide? a) mangas largas b) bufanda", "a) mangas largas", "Dice Please wear long sleeves."),
    ],
    [
        (ADULT + WATER + " Predijiste que oirías «shower». ¿Aparece? a) sí, en take shorter showers b) no, no aparece", "a) sí, en take shorter showers", "Showers está en el texto."),
        (ADULT + WATER + " ¿Por qué hay que reparar las filtraciones rápido? a) porque una filtración pequeña desperdicia mucha agua en un mes b) porque suena fuerte", "a) porque una filtración pequeña desperdicia mucha agua en un mes", "Dice because a small leak wastes a lot of water in a month."),
        (ADULT + VISIT + " ¿Dónde hay que quedarse? a) detrás de la línea amarilla b) delante de la colmena", "a) detrás de la línea amarilla", "Dice stay behind the yellow line."),
    ],
    [
        ("Antes de escuchar predijiste: «Dr. Soto hablará de perros». El texto dice: «Today we will visit the school bees». Escribe tu predicción corregida y la evidencia.", "Dr. Soto hablará de abejas; evidencia: we will visit the school bees", "La frase del texto cambia el tema de perros a abejas."),
        (ADULT + WATER + " ¿Cuántos consejos para ahorrar agua se nombran: apagar la llave, duchas más cortas y reparar filtraciones?", "3", "Son tres consejos."),
        (ADULT + VISIT + " Predijiste que verías «cómo las abejas hacen miel». ¿Se confirma? a) sí, dice we will see how the bees make honey b) no, el texto no lo menciona", "a) sí, dice we will see how the bees make honey", "La frase aparece en el texto."),
    ],
    [
        (ADULT + WATER + " Sofía dice que su predicción sobre energía fue totalmente correcta porque habla de ahorrar. ¿Qué parte del texto muestra el error? a) save water b) at home", "a) save water", "El recurso que se ahorra es el agua, no la energía."),
        (ADULT + VISIT + " ¿Por qué decir «el texto es sobre una clase de pintura» se corrige con evidencia? a) porque dice visit the school bees b) porque no aparece la palabra Dr.", "a) porque dice visit the school bees", "Esa frase muestra que se trata de abejas."),
    ],
    [
        (ADULT + "«Welcome to the school fair. Today you can try three games: ring toss, bean bags and a quiz. Each game gives one ticket. With five tickets, you can win a notebook.» (fair = feria, games = juegos, ring toss = lanzamiento de aros, bean bags = bolsitas de semillas, quiz = prueba de preguntas, ticket = boleto, win = ganar). Predijiste «cuatro juegos». ¿Qué corrección haces? a) son tres juegos b) son cinco juegos", "a) son tres juegos", "El texto nombra tres juegos."),
        (ADULT + "«Welcome to the school fair. Today you can try three games: ring toss, bean bags and a quiz. Each game gives one ticket. With five tickets, you can win a notebook.» (ticket = boleto, win = ganar, notebook = cuaderno). Predijiste que con cuatro boletos ganabas un cuaderno. ¿Qué corrección haces? a) con cinco boletos b) con tres boletos", "a) con cinco boletos", "Dice With five tickets, you can win a notebook."),
    ],
    [(ADULT + "Antes de escuchar un aviso sobre la «Feria del Libro» piensas: «Hablará de libros y de un día». Escuchas: «The Book Fair is on Friday in the gym. There are two hundred books.» (book fair = feria del libro, gym = gimnasio). ¿Qué predicciones se confirman? a) libros y un día (viernes) b) solo el nombre del gimnasio", "a) libros y un día (viernes)", "El texto dice books y on Friday.")],
    [
        ("En Inglés de 8.º (OA 4, clase 4): ¿qué haces con tu predicción una vez terminada la escucha?", "La confirmas o la corriges con evidencia", "Compruebas con una frase del texto."),
        ("En Inglés de 8.º (OA 4, clase 4): ¿Qué es la evidencia?", "Una palabra o frase del texto que apoya la respuesta", "Sustenta tu decisión."),
        ("¿Una predicción puede confirmarse solo en parte?", "Sí", "Se corrige la parte que no coincide."),
    ],
    task("Un adulto lee dos veces este texto: «This week, our class will clean the school yard. We need gloves, bags and a lot of energy. If it rains, we will clean the classroom instead.» (yard = patio, gloves = guantes, bags = bolsas, energy = energía, instead = en su lugar). Antes, escribe una predicción a partir del título «A Clean School». Después de escuchar, escribe si se confirmó, qué parte se corrigió y una frase como evidencia.", "Predicción: se limpiará el colegio. Se confirmó: limpiarán el patio. Se corrigió: si llueve, limpiarán la sala. Evidencia: we will clean the school yard.", ["escribe una predicción antes", "dice si se confirmó o se corrigió", "cita una frase como evidencia"], ["hoja con predicción y revisión", "nota del adulto"], ["no escribir la predicción antes", "no usar una frase del texto"], "Reconoce la parte que se confirmó y revisa con la frase que contradice o apoya lo que esperaba."),
    "Escribe una predicción para un título y luego pide a un adulto que lea el texto del agua para revisar si la confirmas.",
    "Elige un cuento corto que conozcas, escribe una predicción a partir de su título y revisa después si coincidió.",
)

# ------------------------------------------------------------------ OA 4, clase 5
BIKE = "«Many students come to school by bike. Cycling is good for health, and it is cheaper than the bus. It is also better for the air than cars. However, some roads are dangerous because there is no bike lane. The school is asking the city for a safe lane.» (health = salud, cheaper = más barato, air = aire, cars = autos, however = sin embargo, dangerous = peligrosas, lane = vía, safe = segura, city = municipalidad)"
OWL = "«Many owls are birds that hunt at night. They have big eyes, so they can see in the dark. Their feathers are soft, so they fly almost without sound. This is why mice rarely hear them coming.» (many = muchos, owls = búhos, hunt = cazan, feathers = plumas, soft = suaves, fly = vuelan, mice = ratones, rarely = rara vez)"

lesson(
    OA4, 5, MAT_L,
    "Aprenderé a resumir una idea de un texto escuchado con ayuda de un esquema (frame). Sirve para decir con pocas palabras lo más importante y mostrar que entendí.",
    ["Sé encontrar la idea general de un texto.", "Conozco los conectores because, so y but."],
    [
        "Resumir (to summarize) es decir con pocas palabras lo más importante de un texto. Un resumen incluye la idea general y uno o dos detalles clave, y deja fuera los ejemplos pequeños. No copia el texto y no agrega opiniones tuyas. Para resumir con apoyo puedes usar un esquema (frame) con espacios por llenar.",
        "Un esquema útil para un texto informativo es: The text says that ___. It explains that ___ because ___. Para el texto de las bicicletas puedes completar: The text says that cycling to school is good. It explains that it is healthy and better for the air, but some roads are dangerous because there is no bike lane. Los conectores because y but ayudan a unir ideas sin copiar frases enteras.",
        "Para resumir, sigue estos pasos: escucha para la idea general; escucha otra vez para dos o tres palabras clave; completa el esquema con tus palabras; y revisa que no hayas dejado fuera algo esencial ni agregado algo que el texto no dice. Un resumen es correcto cuando otra persona que no escuchó el texto puede entender de qué trata.",
    ],
    [("summary", "resumen: lo más importante en pocas palabras"), ("summarize", "resumir"), ("frame", "esquema: frase con espacios para completar"), ("main idea", "idea general"), ("key detail", "detalle clave: dato importante"), ("The text says that...", "El texto dice que...")],
    [
        ("Completar un esquema", ADULT + OWL + " Completa: «The text says that many owls ___ because ___.»", ["La idea general es que muchos búhos cazan de noche.", "La razón es que tienen ojos grandes y plumas suaves.", "Completo el esquema con esas ideas."], "Muchos búhos cazan de noche porque ven en la oscuridad y vuelan casi sin ruido"),
        ("Elegir el mejor resumen", ADULT + BIKE + " ¿Cuál es un buen resumen? a) Ir en bicicleta al colegio es sano y bueno para el aire, pero faltan vías seguras. b) Muchos estudiantes tienen bicicletas de colores.", ["Un buen resumen dice la idea general y un detalle clave.", "La primera opción dice beneficios y el problema de la falta de vía segura.", "La segunda es solo un detalle que no está en el texto."], "a) Ir en bicicleta al colegio es sano y bueno para el aire, pero faltan vías seguras."),
    ],
    [
        ("Copiar frases enteras del texto y llamar a eso un resumen.", "Un resumen usa palabras propias y pocas ideas, no el texto completo.", "Completa el esquema con tus palabras."),
        ("Agregar una opinión personal al resumen.", "El resumen solo repite lo que dice el texto.", "Deja tus opiniones para otra respuesta."),
    ],
    [
        ("Un resumen debe incluir... a) la idea general y uno o dos detalles clave b) todos los detalles del texto", "a) la idea general y uno o dos detalles clave", "Un resumen es breve."),
        (ADULT + OWL + " ¿Cuál es la idea general? a) muchos búhos cazan de noche y tienen rasgos que los ayudan b) los búhos son aves lentas", "a) muchos búhos cazan de noche y tienen rasgos que los ayudan", "El texto lo explica con los ojos y las plumas."),
        (ADULT + BIKE + " ¿Qué problema se nombra en el texto? a) algunas calles son peligrosas porque no hay vía para bicicletas b) las bicicletas cuestan mucho", "a) algunas calles son peligrosas porque no hay vía para bicicletas", "Dice some roads are dangerous because there is no bike lane."),
    ],
    [
        (ADULT + OWL + " Elige el resumen correcto: a) Los búhos del texto ven en la oscuridad y vuelan casi sin ruido. b) Los búhos comen ratones grandes todos los días.", "a) Los búhos del texto ven en la oscuridad y vuelan casi sin ruido.", "Resume dos rasgos que menciona el texto."),
        (ADULT + BIKE + " ¿Qué conector del texto introduce el problema? a) however b) also", "a) however", "However (sin embargo) marca el contraste."),
        (ADULT + OWL + " ¿Qué conector une «tienen ojos grandes» con «pueden ver en la oscuridad»? a) so b) until", "a) so", "They have big eyes, so they can see in the dark."),
    ],
    [
        (ADULT + BIKE + " ¿Qué beneficio NO se menciona en el texto? a) que es más rápido que un bus b) que es más barato que el bus", "a) que es más rápido que un bus", "El texto habla de salud, precio y aire, no de rapidez."),
        (ADULT + OWL + " Sandra resumió: «Los búhos son aves bonitas». ¿Qué le falta? a) la razón por la que cazan de noche con ayuda de sus rasgos b) el nombre de la ciudad", "a) la razón por la que cazan de noche con ayuda de sus rasgos", "El resumen debe incluir la idea del texto."),
        (ADULT + BIKE + " ¿Cuál es la idea que el colegio pide a la municipalidad? a) una vía segura para bicicletas b) más estacionamientos", "a) una vía segura para bicicletas", "Dice The school is asking the city for a safe lane."),
    ],
    [
        (ADULT + BIKE + " Iván resumió: «Ir en bicicleta es malo porque es caro». ¿Por qué no es un buen resumen? a) porque contradice el texto: dice que es más barato que el bus b) porque es demasiado largo", "a) porque contradice el texto: dice que es más barato que el bus", "El texto dice it is cheaper than the bus."),
        (ADULT + OWL + " ¿Cuál de estas frases es un detalle y no la idea general? a) Their feathers are soft. b) Many owls hunt at night and have helpful traits.", "a) Their feathers are soft.", "Es un detalle que apoya la idea de volar sin ruido."),
    ],
    [
        (ADULT + "«Last Friday, our class made a mural. First, we drew a big tree. Then we painted it green and brown. Many students came to help. The mural now decorates the main hall.» (mural = mural, drew = dibujamos, painted = pintamos, decorates = decora, hall = hall). ¿Cuál es el mejor resumen? a) La clase hizo un mural de un árbol que ahora decora el hall. b) Muchos estudiantes pintaron sus casas.", "a) La clase hizo un mural de un árbol que ahora decora el hall.", "Incluye qué hicieron y dónde queda."),
        (ADULT + "«Mr. Ruiz is a bus driver. Every day he drives sixty kilometres. He likes his job because he meets many people. Last week, a child gave him a drawing.» (drives = maneja, kilometres = kilómetros, job = trabajo, meets = conoce, drawing = dibujo). ¿Qué idea NO debería estar en un resumen breve? a) que un niño le regaló un dibujo la semana pasada b) que es chofer y le gusta su trabajo", "a) que un niño le regaló un dibujo la semana pasada", "Es un detalle menor; la idea general es que es chofer y le gusta su trabajo."),
    ],
    [(ADULT + "En la radio escolar oyes: «The school will plant fifty trees on Saturday. Students, teachers and parents can help. We will bring the tools, but you should bring water and a hat. The goal is a greener school yard.» (plant = plantar, trees = árboles, tools = herramientas, goal = meta, greener = más verde). ¿Cuál es el mejor resumen? a) El colegio plantará árboles el sábado con ayuda de la comunidad para tener un patio más verde. b) Los árboles del colegio están enfermos.", "a) El colegio plantará árboles el sábado con ayuda de la comunidad para tener un patio más verde.", "Incluye qué, cuándo y para qué.")],
    [
        ("En Inglés de 8.º (OA 4, clase 5): ¿qué incluye un resumen con ayuda de un esquema?", "La idea general y uno o dos detalles clave", "Incluye la idea general y un detalle clave."),
        ("En Inglés de 8.º (OA 4, clase 5): ¿Para qué sirve un esquema (frame)?", "Para completar un resumen con apoyo", "Tiene espacios por llenar."),
        ("¿Un resumen debe copiar el texto?", "No", "Debe usar tus palabras."),
    ],
    task("Un adulto lee dos veces este texto: «Some penguins live in very cold places. They have thick feathers and a layer of fat, so they stay warm. They cannot fly, but they swim very fast. Many penguins stand close together to share warmth.» (some = algunos, penguins = pingüinos, thick = gruesas, layer = capa, fat = grasa, warm = abrigados, swim = nadan, together = juntos, warmth = calor). Completa el esquema: «The text says that ___. It explains that ___ because ___.»", "Algunos pingüinos viven en lugares muy fríos. Se mantienen abrigados porque tienen plumas gruesas y una capa de grasa (y se juntan).", ["completa los tres espacios", "usa sus propias palabras", "incluye una razón del texto"], ["esquema completado", "nota del adulto"], ["copiar el texto completo", "agregar datos que el texto no dice"], "Reconoce la parte del esquema bien completada y vuelve a escuchar para ubicar la razón."),
    "Pide a un adulto que lea el texto de las bicicletas y escribe un resumen de dos frases usando la palabra however.",
    "Elige un texto breve que hayas leído en otra asignatura y resúmelo con el esquema «The text says that...».",
)

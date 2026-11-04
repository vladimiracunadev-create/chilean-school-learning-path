"""Cuaderno del estudiante, 1.º medio Inglés (propuesta), EN1M OA 10 (uso de funciones del lenguaje en conversaciones, discusiones y exposiciones).

Las oraciones son originales y los datos son «de ejemplo». Los ejercicios piden elegir, completar y corregir; la práctica oral se hace con una persona de tu casa.
"""
from __future__ import annotations

from student_content_en_m1_a import lesson
from student_content_ma01_b import task
from student_lessons import arith

OA10 = "EN1M OA 10"
MATR = "Las oraciones y datos escritos en cada ejercicio; lápiz, hojas y una persona de tu casa para practicar en voz alta."

# ================================================================ OA 10 · clase 1: cantidad, frecuencia y grado
CLUBS = "Inscripciones a talleres (datos de ejemplo): ajedrez 4 estudiantes, fútbol 52, pintura 3, coro 48."
PANTRY = "Despensa de la cocina del colegio (datos de ejemplo): azúcar, 20 gramos (casi nada); leche, una taza (alcanza para un café); harina, 3 kilos; huevos, 6."

lesson(
    OA10, 1, MATR,
    "Aprenderé a hablar de cantidad (a few, few, a little, little, a large/small number of), de frecuencia (once a month) y de grado (quite, really). Sirve para describir datos y hábitos con precisión en una conversación.",
    ["Sé qué son los sustantivos contables e incontables.", "Sé contar y usar los días de la semana."],
    [
        "Con sustantivos contables en plural (students, eggs) se usan a few (unos pocos, hay suficientes) y few (muy pocos, casi no hay). Con incontables (sugar, milk) se usan a little (un poco, algo) y little (muy poco, casi nada). Para cantidades grandes o pequeñas de contables se dice a large number of y a small number of: A large number of students joined football; a small number joined painting.",
        "La frecuencia (frequency) se dice con once, twice y three times más un período: once a month, twice a week, three times a year. El grado (degree) se agrega con adverbios antes del adjetivo: quite shy (bastante tímida), really shy (muy tímida). Hay que recordar que few y little (sin a) tienen un sentido casi negativo: sugerencia de que algo falta.",
        "Para elegir bien, hazte dos preguntas: ¿el sustantivo se puede contar?, ¿hay suficiente o casi no hay? Si es contable y casi no hay, usa few; si es incontable y casi no hay, usa little. Si es contable y alcanza, usa a few; si es incontable y alcanza, usa a little.",
    ],
    [("a few / few", "unos pocos / muy pocos (contables)"), ("a little / little", "un poco / muy poco (incontables)"), ("a large number of", "una gran cantidad de (contables)"), ("once a month", "una vez al mes"), ("quite", "bastante"), ("really", "muy")],
    [
        ("Contable o incontable", CLUBS + " " + PANTRY + " Completa: «There is ____ sugar left» (casi nada). ¿Usas few o little?", ["Sugar es incontable.", "Con incontables se usa little.", "Casi no hay: little."], "Little"),
        ("Cantidad grande", CLUBS + " Completa: «A ____ number of students joined football» (52). ¿Usas large o small?", ["52 es una cantidad grande.", "Con contables se dice a large number of.", "La palabra es large."], "Large"),
    ],
    [
        ("Usar few con sustantivos incontables (few sugar).", "Se olvida que sugar no se cuenta.", "Con incontables usa little o a little."),
        ("Confundir once a month con once a year.", "No se lee el período.", "Fíjate en la palabra final: month, week, year."),
    ],
    [
        (CLUBS + " Completa: «There are ____ students in the chess club» (4, casi nadie). A) few B) little", "A) few", "Students es contable y casi no hay."),
        (PANTRY + " Si en la despensa quedaran solo 2 huevos y la torta pide 6, completa: «There are ____ eggs.» A) few B) little", "A) few", "Eggs es contable y casi no hay."),
        (CLUBS + " Completa: «A ____ number of students joined the choir» (48). A) large B) small", "A) large", "48 es una cantidad grande."),
    ],
    [
        (CLUBS + " Completa: «A ____ number of students joined painting» (3). A) small B) large", "A) small", "3 es una cantidad pequeña."),
        (PANTRY + " Completa: «There is ____ milk, enough for one coffee.» A) a little B) a few", "A) a little", "Milk es incontable y alcanza."),
        (PANTRY + " Completa: «There are ____ eggs, enough for the cake» (6). A) a few B) a little", "A) a few", "Eggs es contable y alcanza."),
    ],
    [
        ("Camila va a la biblioteca doce veces al año. ¿Cuál frase es equivalente? A) She goes once a month. B) She goes once a week.", "A) She goes once a month.", "Doce veces al año es una vez al mes."),
        arith("Tomás va al gimnasio tres veces a la semana. ¿Cuántas veces va en 4 semanas?", "3*4", "Se multiplican las veces por semana por las semanas."),
        ("Ana es muy tímida. Completa: «Ana is ____ shy.» A) really B) quite", "A) really", "Really significa muy; quite significa bastante."),
    ],
    [
        ("Elige la oración correcta. A) There is few salt in the soup. B) There is little salt in the soup.", "B) There is little salt in the soup.", "Salt es incontable y pide little."),
        ("Elige la oración correcta. A) There are a few girls in the choir. B) There are a few girl in the choir.", "A) There are a few girls in the choir.", "Después de a few va el plural."),
    ],
    [
        (CLUBS + " ¿Qué frase describe juntos a ajedrez y pintura? A) A small number of students joined chess and painting. B) A large number of students joined chess and painting.", "A) A small number of students joined chess and painting.", "4 y 3 son cantidades pequeñas."),
        (PANTRY + " Corrige: «There are little eggs.» A) There are a few eggs. B) There is a few eggs.", "A) There are a few eggs.", "Eggs es contable y plural: a few y are."),
    ],
    [("Tu curso tiene 36 estudiantes y solo 2 tocan violín. ¿Qué frase es correcta? A) Few students play the violin. B) Little students play the violin.", "A) Few students play the violin.", "Students es contable y casi no hay.")],
    [
        ("¿Cuándo se usa little?", "Con incontables, cuando casi no hay", "Por ejemplo, little sugar."),
        ("¿Qué significa twice a week?", "Dos veces por semana", "Twice es dos veces."),
        ("¿Qué diferencia hay entre quite y really?", "Quite es bastante y really es muy", "Cambian la intensidad."),
    ],
    task("Con estos datos de ejemplo de la biblioteca: lunes 3 libros prestados, martes 40, miércoles 5; el préstamo de revistas ocurre una vez por semana; el director es muy amable (really kind) y el bibliotecario es bastante tímido (quite shy). Escribe en tu hoja cuatro oraciones en inglés: una con few o a few, una con a large number of, una con once a week y una con really o quite.", "Few books were borrowed on Monday. A large number of books were borrowed on Tuesday. Magazines are lent once a week. The principal is really kind.", ["usa correctamente el cuantificador", "usa a large number of con un contable", "incluye frecuencia y grado"], ["hoja con cuatro oraciones", "nota de la persona oyente"], ["usar few con un incontable", "confundir quite y really"], "Valora las oraciones correctas y revisa si el sustantivo es contable o incontable."),
    "Vuelve a leer las oraciones de la despensa y subraya todos los cuantificadores.",
    "Escribe en español tres datos de tu curso y cómo dirías la cantidad con few, a few o a large number of.",
)

# ---------------------------------------------------------------- clase 2: acciones en curso, duración y hábitos pasados
lesson(
    OA10, 2, MATR,
    "Aprenderé a hablar de acciones que empezaron en el pasado y continúan o acaban de terminar (have been + -ing), a preguntar y responder por la duración (How long…? for/since) y a contar hábitos pasados (used to). Sirve para presentarte y contar tu historia en una conversación.",
    ["Sé el presente simple y el pasado simple.", "Sé el presente continuo."],
    [
        "Para hablar de una acción que empezó antes y sigue ahora, o que acaba de terminar, se usa have/has been + verbo -ing: We have been training for three months. She has been working all day, so she is tired. Con I, you, we y they se usa have; con he, she e it se usa has. El resultado de la acción aún se nota: My hands are dirty because I have been painting.",
        "Para preguntar por la duración se usa How long have/has…? y se responde con for + período (for two years, for an hour) o since + punto de inicio (since September, since Monday): How long have you been friends? We have been friends for two years. Nunca se dice since two years. Para los hábitos pasados se usa used to + verbo: I used to work at the coffee shop, but now I work at a department store.",
        "Antes de hablar, decide: ¿la acción continúa o ya no ocurre? Si continúa, usa have been + -ing; si ya no ocurre, usa used to. Y para la duración, pregúntate si tienes un período (for) o un punto de partida (since).",
    ],
    [("have/has been + -ing", "acción que empezó antes y continúa"), ("How long…?", "¿Cuánto tiempo…?"), ("for", "durante (período)"), ("since", "desde (punto de inicio)"), ("used to", "solía; hábito pasado"), ("department store", "tienda por departamentos")],
    [
        ("Elegir have o has", "Completa: «We ____ been training for three months.» ¿Usas have o has?", ["El sujeto es we.", "Con we se usa have.", "Queda: We have been training."], "Have"),
        ("For o since", "Responde a «How long have you been friends?» con una duración de dos años.", ["Dos años es un período.", "Con un período se usa for.", "Respondo: For two years."], "For two years"),
    ],
    [
        ("Decir since two years.", "Se mezcla since con un período.", "Con un período usa for; since es para un punto de inicio."),
        ("Usar used to para algo que continúa.", "Se confunde con el presente.", "Used to habla de un hábito que ya no ocurre."),
    ],
    [
        ("Completa. «They ____ been rehearsing for two weeks.» A) have B) has", "A) have", "Con they se usa have."),
        ("Completa. «She ____ been working all day.» A) has B) have", "A) has", "Con she se usa has."),
        ("Completa. «I ____ work at the coffee shop, but now I work at a department store.» A) used to B) use to", "A) used to", "Used to expresa un hábito pasado."),
    ],
    [
        ("¿Cuál es la respuesta correcta a «How long has she been in the choir?» A) For six months. B) Since six months.", "A) For six months.", "Con un período se usa for."),
        ("¿Cuál es la respuesta correcta a «Since when has he lived here?» A) Since September. B) For September.", "A) Since September.", "September es un punto de inicio."),
        ("¿Cuál oración habla de una acción que acaba de terminar y cuyo resultado se nota? A) My hands are dirty because I have been painting. B) I painted yesterday.", "A) My hands are dirty because I have been painting.", "El resultado, las manos sucias, se nota ahora."),
    ],
    [
        ("Elige la oración correcta. A) We have been waiting for twenty minutes. B) We are waiting since twenty minutes.", "A) We have been waiting for twenty minutes.", "Veinte minutos es un período: se usa for con have been + -ing."),
        ("Elige la oración correcta. A) She used to live in Temuco, but now she lives in Osorno. B) She used to living in Temuco.", "A) She used to live in Temuco, but now she lives in Osorno.", "Used to va seguido del verbo sin -ing."),
        ("Completa. «How long ____ they been married?» A) have B) has", "A) have", "Con they se usa have."),
    ],
    [
        ("¿Qué oración muestra que la acción ya no ocurre? A) I used to play chess. B) I have been playing chess.", "A) I used to play chess.", "Used to marca un hábito pasado."),
        ("Corrige: «I am working here since March.» A) I have been working here since March. B) I work here for March.", "A) I have been working here since March.", "Since March es un punto de inicio y la acción continúa."),
    ],
    [
        ("«He has been waiting for an hour.» ¿Qué significa? A) empezó hace una hora y sigue esperando B) esperó hace años y terminó", "A) empezó hace una hora y sigue esperando", "Have been + -ing une pasado y presente."),
        ("Ordena las palabras con letras: A) been B) they C) have D) learning E) English", "B, C, A, D, E", "La oración correcta es They have been learning English."),
    ],
    [("Un boletín del club dice: «Our president has been leading the club for two years. She used to be a member of the choir.» ¿Qué sigue haciendo la presidenta? A) liderar el club B) cantar en el coro", "A) liderar el club", "Has been leading continúa; used to be ya no.")],
    [
        ("¿Qué pregunta se usa para preguntar duración?", "How long…?", "Se responde con for o since."),
        ("¿Qué expresa used to?", "Un hábito pasado que ya no ocurre", "Contrasta antes y ahora."),
        ("¿Con qué tipo de expresión de tiempo se usa since?", "Con un punto de inicio, como Monday", "For se usa con períodos y since con puntos de inicio."),
    ],
    task("Presenta oralmente a una persona de tu casa, y escribe en tu hoja, cuatro oraciones sobre ti: una con have been + -ing, una con for, una con since y una con used to. Por ejemplo, algo que llevas haciendo, desde cuándo y qué hábito tenías antes.", "I have been learning English for two years. I have been playing football since March. I used to read comics, but now I read novels. How long have you been learning English?", ["usa have/has been + -ing correctamente", "distingue for y since", "usa used to para un hábito que ya no tiene"], ["hoja con cuatro oraciones", "nota de la persona oyente"], ["decir since con un período", "usar used to con -ing"], "Valora las oraciones correctas y practica en voz alta las que tuvieron errores."),
    "Vuelve a leer las respuestas con for y since y agrega una oración propia con cada una.",
    "Escribe en español tres cosas que llevas haciendo un tiempo y dos hábitos que ya no tienes.",
)

# ---------------------------------------------------------------- clase 3: predicciones, necesidades, promesas y posibilidades
lesson(
    OA10, 3, MATR,
    "Aprenderé a hablar de predicciones, necesidades, promesas y posibilidades con will probably, might, shall, needn't y I promise. Sirve para planificar con otras personas y decir cuánta seguridad tienes.",
    ["Sé will para el futuro.", "Sé que los modales van con el verbo sin to."],
    [
        "Will probably expresa una predicción muy probable: Look at the dark clouds; it will probably rain. Might expresa una posibilidad más débil: It might snow in the mountains. Los modales no cambian con la persona (he might, she might) y van seguidos del verbo sin to: He might come, no He might to come.",
        "Needn't significa que no es necesario: You needn't hurry (no hace falta apurarse). No es una prohibición. Una promesa se hace con I promise I will…: I promise I will call you. Shall se usa con I y we para ofrecer o sugerir (Shall we have lunch at one?): propone un plan y espera respuesta. Para anunciar algo que se hará, se usa will (He will be here at six).",
        "Para elegir el modal adecuado, pregúntate cuánta seguridad tienes: casi seguro (will probably), solo posible (might), no necesario (needn't), compromiso (I promise I will) o sugerencia (Shall we…?).",
    ],
    [("will probably", "probablemente; casi seguro"), ("might", "podría; es posible"), ("needn't", "no hace falta"), ("I promise I will…", "prometo que…"), ("shall", "modal para sugerir: Shall we…? = ¿Y si…?"), ("suggestion", "sugerencia")],
    [
        ("Elegir la certeza", "Hay nubes oscuras en el cielo. Completa: «It ____ rain.» (muy probable) ¿will probably o might not?", ["Las nubes oscuras son una pista fuerte.", "Es muy probable, no solo posible.", "Se usa will probably."], "Will probably"),
        ("No necesario", "El bus llegará tarde. Completa: «You ____ hurry.» (no hace falta) ¿needn't o must?", ["No es necesario apurarse.", "Needn't expresa ausencia de necesidad.", "Must expresaría obligación."], "Needn't"),
    ],
    [
        ("Decir He might to come.", "Se agrega to al modal.", "Los modales van con el verbo sin to: He might come."),
        ("Entender needn't como una prohibición.", "Se confunde con must not.", "Needn't = no es necesario."),
    ],
    [
        ("Completa. «The forecast says sun all day. Tomorrow it ____ be hot.» (muy probable) A) will probably B) might not", "A) will probably", "El pronóstico es una pista fuerte."),
        ("Completa. «It ____ snow in the mountains tonight, but nobody is sure.» A) might B) will", "A) might", "No hay seguridad: es una posibilidad."),
        ("Completa. «You ____ hurry; the bus is late.» (no hace falta) A) needn't B) must", "A) needn't", "No es necesario apurarse."),
    ],
    [
        ("Completa. «I promise I ____ call you tonight.» A) will B) might", "A) will", "Una promesa se hace con will."),
        ("«Shall we have lunch at one?» ¿Qué función tiene? A) una sugerencia B) una obligación", "A) una sugerencia", "Shall we…? invita a hacer algo."),
        ("Une cada idea con su expresión. 1) probablemente 2) quizás 3) no hace falta Expresiones: a) might b) will probably c) needn't", "1-b, 2-a, 3-c", "Cada expresión marca un grado distinto."),
    ],
    [
        ("Elige la oración correcta. A) You needn't bring money. B) You needn't to bring money.", "A) You needn't bring money.", "Después de needn't va el verbo sin to."),
        ("Elige la mejor promesa. A) I promise I will help you. B) I promise I might help you.", "A) I promise I will help you.", "Una promesa debe ser firme."),
        ("Completa para una posibilidad débil. «It ____ rain, but I doubt it.» A) might B) will probably", "A) might", "Might expresa poca seguridad."),
    ],
    [
        ("¿Qué es más seguro? A) It will probably rain. B) It might rain.", "A) It will probably rain.", "Will probably expresa más seguridad."),
        ("Tu entrenadora dice «You needn't wear a jacket». ¿Puedes ir sin chaqueta? A) sí, no hace falta B) no, está prohibido", "A) sí, no hace falta", "Needn't indica que no es necesario."),
    ],
    [
        ("Elige la mejor predicción para mañana: «Tomorrow ____ sunny.» A) will probably be B) needn't be", "A) will probably be", "Una predicción usa will probably."),
        ("Corrige: «He might to come.» A) He might come. B) He might comes.", "A) He might come.", "Los modales van con el verbo sin to ni -s."),
    ],
    [("Un cartel dice: «Please speak quietly. The baby might wake up.» ¿Por qué hay que hablar bajo? A) porque el bebé podría despertarse B) porque el bebé ya está despierto", "A) porque el bebé podría despertarse", "Might expresa una posibilidad.")],
    [
        ("¿Qué expresa needn't?", "Que no es necesario", "No es una prohibición."),
        ("¿Con qué modal haces una promesa?", "Will", "I promise I will…"),
        ("¿Cuál es más seguro: will probably o might?", "Will probably", "Might es solo posibilidad."),
    ],
    task("Escribe y di en voz alta a una persona de tu casa cinco oraciones sobre tu plan de mañana, cada una con una función distinta: una predicción segura (will probably), una posibilidad (might), algo que no hace falta (needn't), una promesa (I promise I will) y una sugerencia (Shall we…?).", "It will probably be sunny. We might go to the park. You needn't bring food. I promise I will help you with your homework. Shall we meet at ten?", ["usa los cinco modales pedidos", "los usa con el verbo sin to", "cada oración tiene su función"], ["hoja con cinco oraciones", "nota de la persona oyente"], ["agregar to después del modal", "usar needn't como prohibición"], "Valora la variedad de funciones y corrige el uso de to y -s si hay errores."),
    "Vuelve a leer las oraciones de esta clase y clasifícalas por su grado de certeza.",
    "Escribe en español tres planes tuyos: uno casi seguro, uno posible y uno que no hace falta hacer.",
)

# ---------------------------------------------------------------- clase 4: expresiones comunes, palabras compuestas y conectores
lesson(
    OA10, 4, MATR,
    "Aprenderé a usar expresiones de uso común (nice to meet you, Why don't we…?, What's it like?, talk about, for example), palabras compuestas (part-time job, chopstick) y conectores (although, both… and, so that, later, last). Sirve para conversar con naturalidad y unir ideas.",
    ["Sé saludar y despedirme en inglés.", "Sé conectores simples como and y but."],
    [
        "Las expresiones de uso común son bloques que se usan en muchas conversaciones. Nice to meet you se dice al conocer a alguien. Why don't we go to the cinema? propone un plan. What's it like? pregunta cómo es algo («¿Cómo es?»). To talk about significa hablar de un tema, y for example introduce un ejemplo. Aprenderlas completas te ayuda a hablar más rápido.",
        "Una palabra compuesta (compound word) une dos palabras para formar un significado nuevo: part-time job (trabajo de media jornada), chopstick (palillo para comer; se escribe con dos palabras unidas: chop + stick). Apply for a job significa postular a un trabajo. Los conectores unen ideas: although (aunque, contraste), both Luis and Tomás (los dos), so that (para que, propósito), later (más tarde) y last (por último). Ejemplo: He learned English so that he could speak with foreigners.",
        "Al hablar, elige el conector según la relación que quieras mostrar: contraste, suma, propósito u orden. Y usa las expresiones comunes para empezar, proponer, preguntar o dar un ejemplo.",
    ],
    [("Nice to meet you", "Mucho gusto"), ("Why don't we…?", "¿Por qué no…? (propuesta)"), ("What's it like?", "¿Cómo es?"), ("part-time job", "trabajo de media jornada"), ("apply for a job", "postular a un trabajo"), ("chopstick", "palillo para comer")],
    [
        ("Elegir la expresión", "Conoces a alguien nuevo. ¿Qué dices: «Nice to meet you» o «See you later»?", ["Es una presentación.", "Nice to meet you se usa al conocer a alguien.", "See you later es una despedida."], "Nice to meet you"),
        ("Palabra compuesta", "La palabra chopstick está formada por dos palabras. ¿Cuáles son?", ["Separo la palabra en dos.", "Chop + stick.", "Se refiere a un palito para comer."], "Chop y stick"),
    ],
    [
        ("Usar what is it like para preguntar «qué le gusta».", "Se confunde con like como verbo.", "What's it like? pregunta cómo es algo."),
        ("Usar although y but juntos en la misma oración.", "Se repite el contraste.", "Usa solo uno por oración."),
    ],
    [
        ("Quieres proponer ir al cine. ¿Qué dices? A) Why don't we go to the cinema? B) What's it like?", "A) Why don't we go to the cinema?", "Why don't we…? propone un plan."),
        ("Quieres saber cómo es un lugar. ¿Qué preguntas? A) What's it like? B) Nice to meet you.", "A) What's it like?", "What's it like? pide una descripción."),
        ("Quieres decir «por ejemplo» antes de dar un caso. ¿Qué dices? A) for example B) later", "A) for example", "For example introduce un caso concreto."),
    ],
    [
        ("¿Qué significa part-time job? A) un trabajo de media jornada B) un trabajo de noche", "A) un trabajo de media jornada", "Part-time significa tiempo parcial."),
        ("¿Qué significa apply for a job? A) postular a un trabajo B) renunciar a un trabajo", "A) postular a un trabajo", "Apply for es solicitar."),
        ("¿De qué dos palabras se forma notebook? A) note y book B) not y book", "A) note y book", "Es una palabra compuesta."),
    ],
    [
        ("Completa. «____ it's cheap, I'm not sure.» ¿Qué indica? A) Although, un contraste B) So that, un propósito", "A) Although, un contraste", "El precio bajo y la duda se oponen."),
        ("Completa. «Both Luis ____ Tomás are my neighbors.» A) and B) or", "A) and", "Both va con and."),
        ("Completa. «I'll talk to you ____.» (más tarde) A) later B) last", "A) later", "Later significa más tarde."),
    ],
    [
        ("Elige la oración correcta. A) He learned English so that he could speak with foreigners. B) He learned English although he could speak with foreigners.", "A) He learned English so that he could speak with foreigners.", "So that introduce el propósito."),
        ("«Last, he played the piano.» ¿Qué indica last? A) el último hecho B) el primer hecho", "A) el último hecho", "Last significa por último."),
    ],
    [
        ("Ordena las palabras con letras: A) apply B) I C) will D) for E) a F) part-time G) job", "B, C, A, D, E, F, G", "La oración correcta es I will apply for a part-time job."),
        ("«Let's talk about the project; for example, the budget.» ¿Qué expresión introduce el ejemplo? A) for example B) talk about", "A) for example", "For example introduce un caso concreto."),
    ],
    [("Un aviso dice: «Part-time job: weekend waiter. Apply for the job by Friday.» (waiter = garzón). ¿Hasta cuándo se puede postular? A) hasta el viernes B) hasta el lunes", "A) hasta el viernes", "Dice by Friday.")],
    [
        ("¿Qué se dice al conocer a alguien?", "Nice to meet you", "Es la fórmula de saludo al conocerse."),
        ("¿Qué indica although?", "Un contraste", "Une ideas que se oponen."),
        ("¿Qué es una palabra compuesta?", "Una palabra formada por dos palabras", "Por ejemplo, chopstick."),
    ],
    task("Imagina que conoces a un compañero nuevo en un taller. Escribe y di en voz alta un minidiálogo de cuatro turnos en inglés con Nice to meet you, Why don't we…?, What's it like? y un for example. Incluye también un conector (although, both… and o so that).", "A: Nice to meet you. B: Nice to meet you too. A: What's it like, the music workshop? B: It is fun. For example, we play drums. Why don't we go together on Friday?", ["usa las cuatro expresiones pedidas", "incluye un conector bien usado", "lo dice en voz alta"], ["hoja con el diálogo", "nota de la persona oyente"], ["usar what is it like con otro sentido", "no incluir el conector"], "Valora la naturalidad y revisa cada expresión usada."),
    "Vuelve a leer las expresiones de esta clase y escribe una oración con cada una.",
    "Escribe en español tres palabras compuestas del inglés que conozcas y su significado.",
)

# ---------------------------------------------------------------- clase 5: situaciones hipotéticas y consejos
lesson(
    OA10, 5, MATR,
    "Aprenderé a describir situaciones hipotéticas o imaginarias y a dar consejos con if + pasado y would, y con If I were you, I would…. Sirve para opinar, recomendar y conversar sobre posibilidades.",
    ["Sé el pasado simple.", "Sé que would expresa una consecuencia imaginaria."],
    [
        "Una situación hipotética es algo imaginario o poco probable. Se forma con if + pasado simple y would + verbo: He would meet more people if he spoke English. El verbo está en pasado, pero habla de una posibilidad del presente o futuro. Con if se usa were para todas las personas: if I were, if she were.",
        "El consejo más típico es If I were you, I would…: If I were you, I would tell her the truth. Con él te pones en el lugar del otro y recomiendas. Para aconsejar a otra persona, elige una acción concreta, posible y respetuosa. Cuando hay un problema serio (por ejemplo, alguien copia tu tarea o te presiona), un buen consejo es hablarlo con una persona adulta de confianza.",
        "Para armar una oración hipotética, haz dos pasos: 1) escribe la condición con if y el verbo en pasado, 2) escribe el resultado con would y el verbo base. Revisa que no uses would en la parte del if.",
    ],
    [("if I were you, I would…", "si yo fuera tú, yo haría… (consejo)"), ("if + pasado, would + verbo", "estructura hipotética"), ("advice", "consejo"), ("truth", "verdad"), ("condition", "condición"), ("result", "resultado")],
    [
        ("Completar el consejo", "Completa: «If I ____ you, I would tell her the truth.» ¿were o am?", ["Es un consejo hipotético.", "Con if se usa were.", "Queda: If I were you."], "Were"),
        ("Condición y resultado", "En «He would meet more people if he spoke English», ¿cuál es la condición?", ["La condición va con if.", "If he spoke English.", "Hablar inglés es la condición."], "If he spoke English"),
    ],
    [
        ("Decir If I would be you.", "Se usa would en la parte del if.", "En el if va el pasado (were); would va en el resultado."),
        ("Dar consejos que dañan o que no son posibles.", "Se piensa solo en el humor.", "Aconseja algo concreto, posible y respetuoso."),
    ],
    [
        ("Completa. «If I ____ in your place, I would ask for help.» A) were B) am", "A) were", "Con if se usa were."),
        ("Completa. «She would feel better if she ____ more water.» A) drank B) drinks", "A) drank", "Después de if va el pasado simple."),
        ("¿Qué frase da un consejo? A) If I were you, I would apologize. B) I was sad yesterday.", "A) If I were you, I would apologize.", "La primera usa la estructura de consejo."),
    ],
    [
        ("Completa. «If we had more time, we ____ visit the museum.» A) would B) will", "A) would", "Con if + pasado va would."),
        ("Elige el consejo para alguien con mucho sueño. A) If I were you, I would go to bed earlier. B) If I am you, I would go to bed earlier.", "A) If I were you, I would go to bed earlier.", "El consejo correcto usa were."),
        ("Une cada problema con su consejo. 1) I forget my homework. 2) I am always late. 3) I cannot save money. Consejos: a) If I were you, I would leave home earlier. b) If I were you, I would use a planner. c) If I were you, I would save a little each week.", "1-b, 2-a, 3-c", "Cada consejo se relaciona con su problema."),
    ],
    [
        ("Completa. «If it ____ cold, I would wear a coat.» A) were B) is", "A) were", "Con if + pasado se usa were."),
        ("Elige la oración correcta. A) If she studied more, she would pass the test. B) If she would study more, she passes the test.", "A) If she studied more, she would pass the test.", "En la parte del if va el pasado, no would."),
        ("Completa. «I ____ buy a bike if I had the money.» A) would B) will", "A) would", "Es una situación hipotética."),
    ],
    [
        ("«If I were you, I would call my cousin.» ¿Quién da el consejo? A) la persona que habla B) la persona a quien le hablan", "A) la persona que habla", "I would es la persona que aconseja."),
        ("Un compañero dice «If I was you». ¿Qué forma se recomienda en la estructura formal? A) were B) am", "A) were", "Se usa were para todas las personas."),
    ],
    [
        ("Ordena las palabras con letras: A) would B) faster C) she D) learn E) if F) she G) practiced H) daily", "C, A, D, B, E, F, G, H", "La oración es She would learn faster if she practiced daily."),
        ("Un amigo te cuenta que otro compañero copia su tarea. ¿Qué consejo es adecuado? A) If I were you, I would talk to my teacher or an adult I trust. B) If I were you, I would say nothing and keep it secret.", "A) If I were you, I would talk to my teacher or an adult I trust.", "Pedir ayuda a una persona adulta de confianza es lo más seguro."),
    ],
    [("En un foro, alguien escribe: «I have a big test tomorrow and I'm nervous. What should I do?» ¿Cuál es el mejor consejo? A) If I were you, I would sleep early and review the main ideas. B) If I were you, I would study all night without sleeping.", "A) If I were you, I would sleep early and review the main ideas.", "Es un consejo concreto y útil.")],
    [
        ("¿Qué estructura expresa una situación imaginaria?", "If + pasado, would + verbo", "Une condición y resultado."),
        ("¿Qué verbo se usa con if para todas las personas?", "Were", "If I were, if she were."),
        ("¿A quién conviene acudir ante un problema serio?", "A una persona adulta de confianza", "Es el consejo más seguro."),
    ],
    task("Escribe y di en voz alta a una persona de tu casa cuatro oraciones en inglés: dos consejos con If I were you, I would… para estos problemas: «I have too many things to study» y «I feel nervous before speaking in class»; y dos oraciones hipotéticas con if + pasado y would sobre tu vida (por ejemplo, If I had more time, I would…).", "If I were you, I would make a study plan. If I were you, I would practice with a friend. If I had more time, I would learn to play the guitar. I would travel to the south if I had a holiday.", ["usa If I were you, I would… en dos consejos", "usa if + pasado y would en dos oraciones", "los consejos son concretos y posibles"], ["hoja con cuatro oraciones", "nota de la persona oyente"], ["usar would en la parte del if", "dar un consejo poco respetuoso"], "Valora los consejos concretos y corrige were y would si es necesario."),
    "Vuelve a leer los consejos de esta clase y escribe uno nuevo para alguien que no puede dormir.",
    "Escribe en español dos situaciones imaginarias que te gustaría vivir y cómo las dirías con if + pasado.",
)

"""Cuaderno del estudiante, 8.º básico Inglés (oficial): IN08 OA 16, funciones del lenguaje en textos escritos.

Cada función (cantidades y ordinales, gustos y comparaciones, planes y condiciones, descripciones y preposiciones,
frecuencia, secuencia y expresiones comunes) se enseña en la clase antes de usarse en un ejercicio. Todos los textos son
originales y breves, con glosario en español. Los datos de los textos son de ejemplo. Los títulos de clase del plan son
genéricos: aquí cada clase trabaja un grupo de funciones del lenguaje.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA = "IN08 OA 16"


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


# ============================================================ clase 1: cantidades, ordinales y tiempo
CINE1 = "Open-air cinema (datos de ejemplo). The first film is on Friday at 6:00 p.m. The second film is on Saturday at 8:00 p.m. The third film is next week, on Wednesday. There are two hundred and fifty seats. Several food stands open at 5:00 p.m."
G_CINE1 = "(open-air = al aire libre; film = película; seats = asientos; food stands = puestos de comida; open = abren)"

lesson(
    OA, 1,
    "Los avisos y las oraciones escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a expresar cantidades, contar y enumerar con números y ordinales, y a preguntar y dar información sobre el tiempo con on, in y at. Sirve para escribir avisos, agendas y mensajes claros.",
    ["Conozco los números hasta cien en inglés.", "Sé los días de la semana y los meses."],
    [
        "Para expresar cantidades usa: a lot of (mucho/s), several (varios, más de dos pero no muchos), a few (unos pocos), all the (todos los): «There are a lot of people. Several students came. All the tickets are sold». Para contar usa los números cardinales: one hundred (100), two hundred and fifty (250), three hundred and twenty (320). En los números de más de cien se usa and antes de las decenas.",
        "Para enumerar usa los ordinales (ordinal numbers): first (1.º), second (2.º), third (3.º), fourth, fifth, sixth, ninth, twelfth. Responden a «¿En qué lugar?»: «She is the first, he is the third». Para preguntar por el tiempo usa When…?: «When is the party?». Respuestas: on + día (on Saturday), in + mes o año (in December, in 2030), at + hora (at 10:00), y expresiones solas como tomorrow, next week, next year.",
        "Revisa siempre la preposición: on para días y fechas, in para meses, años y estaciones, at para la hora. «The meeting is in March, on Monday at 9:30». Si dudas, di la expresión completa en voz alta. Para dar una información completa responde con el día y la hora: «On Friday at 6:00 p.m.».",
    ],
    [("a lot of", "mucho/s"), ("several", "varios"), ("a few", "unos pocos"), ("all the", "todos los"), ("first / second / third", "primero / segundo / tercero"), ("two hundred and fifty", "doscientos cincuenta"), ("on / in / at", "en (día) / en (mes) / a (hora)"), ("next week", "la próxima semana"), ("tomorrow", "mañana")],
    [
        ("Elegir la preposición", "Completa: «The party is ___ December.» Opciones: in, on.",
         ["December es un mes.", "Para los meses se usa in.", "La oración queda: in December."], "in"),
        ("Escribir un número con palabras", "Escribe en inglés el número 350.",
         ["Primero los cientos: three hundred.", "Luego and y las decenas: fifty.", "Todo junto: three hundred and fifty."], "three hundred and fifty"),
    ],
    [
        ("Decir «at Monday» o «in Monday».", "Los días de la semana van con on.", "Escribe on Monday."),
        ("Escribir «two hundred fifty» sin and.", "En inglés se usa and después de los cientos.", "Escribe two hundred and fifty."),
    ],
    [
        ("«Several» significa: a) varios b) ninguno", "a", "Se usa para más de dos, pero no muchos."),
        ("El ordinal de 3 es: a) third b) three", "a", "Third es el ordinal; three es el cardinal."),
        ("Elige la preposición: «The class is ___ Tuesday.» a) on b) in", "a", "Los días de la semana usan on."),
    ],
    [
        (f"Lee: {CINE1} {G_CINE1} ¿Cuándo es la segunda película? a) On Saturday at 8:00 p.m. b) On Friday at 6:00 p.m.", "a", "El aviso dice The second film is on Saturday at 8:00 p.m."),
        (f"Lee: {CINE1} {G_CINE1} ¿Qué película es la próxima semana? a) The third b) The first", "a", "El aviso dice The third film is next week."),
        (f"Lee: {CINE1} {G_CINE1} ¿Cuántos asientos hay? a) Two hundred and fifty b) Two hundred and fifteen", "a", "El aviso dice two hundred and fifty seats, que es 250."),
    ],
    [
        ("Elige cómo se escribe 320 en inglés: a) three hundred and twenty b) three twenty hundred", "a", "El orden es cientos, and, decena."),
        arith(f"Lee: {CINE1} {G_CINE1} De los 250 asientos, 90 están vacíos. ¿Cuántos asientos están ocupados? Escribe el número.", "250-90", "Se restan los asientos vacíos del total de asientos."),
        ("Completa: «There are ___ people in the square, so it is very crowded.» Opciones: a lot of, a few. (crowded = repleta)", "a lot of", "Repleta indica muchas personas."),
    ],
    [
        ("Mensaje de ejemplo: «All the tickets for Friday are sold, but there are several tickets for Saturday.» (tickets = entradas; sold = vendidas) ¿Qué día quedan entradas? a) Saturday b) Friday", "a", "Para el viernes están todas vendidas; para el sábado quedan varias."),
        ("Resultados de una carrera de ejemplo: Ana llegó primera, Cata llegó segunda y Beto llegó tercero. ¿Quién llegó en último lugar de los tres? a) Beto b) Cata", "a", "Beto fue el tercero, es decir, el último de los tres."),
    ],
    [
        ("Completa con las preposiciones: «The meeting is ___ Monday ___ 9:30.» a) on, at b) in, on", "a", "Monday usa on y la hora usa at."),
        (f"Lee: {CINE1} {G_CINE1} Hoy es jueves. ¿Qué película es mañana? a) The first b) The second", "a", "Mañana es viernes y la primera película es el viernes."),
    ],
    [("En un aviso de una feria del libro leíste: «The fair is in March, on Saturday at 11:00. There are a lot of books and several writers.» (fair = feria; writers = escritores) Quieres preguntar la fecha. ¿Qué pregunta en inglés escribes? a) When is the fair? b) Where is the fair?", "a", "When pregunta por el tiempo.")],
    [
        ("¿Qué preposición va con un mes?", "In", "In March, in December."),
        ("En Inglés (oficial): ¿Cómo se dice «mañana» en inglés?", "Tomorrow", "Es el día siguiente a hoy."),
        ("¿Qué ordinal sigue a second?", "Third", "El orden es first, second, third."),
    ],
    task("Escribe en tu hoja una agenda de ejemplo con cuatro oraciones. Incluye: un día con on, un mes con in, una hora con at y un ordinal. Datos que puedes usar: club de ajedrez, el martes a las 4:30; taller de lectura, en abril; Ana es la primera de la lista. (club de ajedrez = chess club; taller = workshop; abril = April; lista = list)", "The chess club is on Tuesday at 4:30. The reading workshop is in April. Ana is the first in the list. There are several students.", ["usa on, in y at correctamente", "incluye un ordinal bien escrito", "usa a lot of o several"], ["agenda de cuatro oraciones en la hoja"], ["usar at con los días", "olvidar and en los cientos"], "Pide que lea su agenda en voz alta y que otra persona la entienda sin ver el papel."),
    "Copia la tabla de cantidades y ordinales y escribe una oración con cada palabra.",
    "Escribe tres números de más de cien con letras en inglés, como 215.",
)

# ============================================================ clase 2: gustos, opiniones y comparaciones
PRO2 = "Camila: I love dancing and I enjoy painting. I hate waking up early. I don't mind helping at home. I'd like to visit Torres del Paine. I find swimming relaxing."
G_PRO2 = "(love = amo; enjoy = disfruto; hate = odio; don't mind = no me molesta; I'd like to = me gustaría; I find = me parece; relaxing = relajante)"
ALT2 = "Alturas de ejemplo: Ana mide 150 cm, Bruno mide 158 cm y Carla mide 154 cm."
PAN2 = "Precio del pan por kilo (datos de ejemplo): Panadería A, $1.600. Panadería B, $1.900. Panadería C, $2.200."

lesson(
    OA, 2,
    "Los perfiles y las tablas escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a expresar gustos, preferencias y opiniones (love, enjoy, hate, don't mind, I'd like, I find) y a comparar con -er than y the -est / the most. Sirve para escribir lo que me gusta y comparar personas, cosas y lugares.",
    ["Conozco el presente simple y los verbos like y want.", "Sé que los adjetivos describen."],
    [
        "Para hablar de gustos usa verbos de preferencia seguidos de un verbo con -ing: I love dancing (amo bailar), I enjoy painting (disfruto pintar), I hate waking up early (odio levantarme temprano), I don't mind helping (no me molesta ayudar). Para un deseo educado usa I'd like (me gustaría) + to + verbo: I'd like to visit Torres del Paine. Para dar una opinión usa I find + algo + adjetivo: I find swimming relaxing.",
        "Para comparar dos cosas con un adjetivo corto agrega -er y than (que): tall → taller than; short → shorter than; fast → faster than. Con adjetivos largos usa more + adjetivo + than: more expensive than. Para decir cuál es el mayor de varios usa the + -est o the most: the tallest, the most expensive in the city. Algunos son irregulares: good → better → the best; bad → worse → the worst.",
        "Cuida el orden: «Bruno is taller than Ana». No digas «more taller». Compara solo con datos que tengas a la vista. Para opinar con claridad usa un adjetivo: interesting, boring, relaxing, difficult, great. Si quieres ser educado al pedir algo, prefiere I'd like a sandwich, please a I want a sandwich.",
    ],
    [("love / enjoy", "amar / disfrutar"), ("hate", "odiar"), ("don't mind", "no me molesta"), ("I'd like", "me gustaría"), ("I find…", "me parece…"), ("taller than", "más alto que"), ("the tallest", "el más alto"), ("more expensive than", "más caro que"), ("the best / the worst", "el mejor / el peor")],
    [
        ("Completar con -ing", "Completa: «I enjoy ___ (swim).» Escribe la forma correcta.",
         ["Después de enjoy va un verbo con -ing.", "Swim termina en consonante: se duplica la m.", "La forma es swimming."], "swimming"),
        ("Comparar con datos", "Datos de ejemplo: Leo mide 140 cm y Mia mide 148 cm. Completa: «Mia is ___ than Leo.» Opciones: taller, tallest.",
         ["Se comparan dos personas: Mia (148) y Leo (140).", "Para dos se usa -er than.", "Mia is taller than Leo."], "taller"),
    ],
    [
        ("Escribir «more taller».", "Se mezclan dos formas de comparar.", "Con adjetivos cortos, solo -er: taller."),
        ("Escribir «I enjoy to swim».", "Después de enjoy se usa el verbo con -ing.", "Escribe I enjoy swimming."),
    ],
    [
        ("«I hate» significa: a) odio b) amo", "a", "Hate expresa un fuerte disgusto."),
        ("Elige la forma correcta: «I love ___ music.» a) listening to b) listen to", "a", "Después de love se usa el verbo con -ing."),
        ("El comparativo de tall es: a) taller b) tallest", "a", "Para comparar dos cosas se usa -er."),
    ],
    [
        (f"Lee: {PRO2} {G_PRO2} ¿Qué le gusta mucho a Camila? a) Dancing b) Waking up early", "a", "Dice I love dancing."),
        (f"Lee: {PRO2} {G_PRO2} ¿Qué actividad no le gusta? a) Waking up early b) Helping at home", "a", "Dice I hate waking up early; ayudar en casa no le molesta."),
        (f"Lee: {PRO2} {G_PRO2} ¿Qué lugar le gustaría visitar? a) Torres del Paine b) The beach", "a", "El texto dice I'd like to visit Torres del Paine."),
    ],
    [
        (f"{ALT2} ¿Quién es la persona más alta? a) Bruno b) Carla", "a", "Bruno mide 158 cm, que es el mayor valor."),
        (f"{PAN2} ¿Qué panadería es la más cara? a) C b) A", "a", "La C cobra $2.200 por kilo, el valor más alto."),
        arith(f"{PAN2} ¿Cuántos pesos más caro es el pan en C que en A? Escribe el número.", "2200-1600", "Se resta el precio de A al precio de C."),
    ],
    [
        ("Una compañera escribió: «Pedro is the most tall in the class.» ¿Cuál es la corrección? a) Pedro is the tallest in the class b) Pedro is more tall in the class", "a", "Con un adjetivo corto se usa the + -est."),
        (f"{PAN2} Elige la oración verdadera. a) Bakery B is more expensive than bakery A b) Bakery B is the cheapest", "a", "B cobra $1.900 y A cobra $1.600; la más barata es A."),
    ],
    [
        (f"{ALT2} Elige la oración falsa. a) Carla is taller than Bruno b) Carla is taller than Ana", "a", "Carla mide 154 cm y Bruno 158 cm, así que es más baja."),
        ("En una cafetería pides algo con cortesía. ¿Qué opción es más cortés? a) I'd like a juice, please b) I want juice", "a", "I'd like es la forma educada de pedir."),
    ],
    [("En una encuesta de ejemplo del curso: fútbol 12 estudiantes, dibujo 9 estudiantes y lectura 7 estudiantes. Se pregunta por el pasatiempo favorito. (survey = encuesta; hobby = pasatiempo) ¿Cuál es el más popular? a) Football b) Reading", "a", "Fútbol tiene 12 votos, el mayor número.")],
    [
        ("¿Qué forma tiene el verbo después de enjoy?", "Con -ing", "Enjoy se usa con verbos terminados en -ing."),
        ("¿Cuál es el superlativo de good?", "The best", "Good es irregular: better, the best."),
        ("¿Qué significa «I find it boring»?", "Me parece aburrido", "I find sirve para dar una opinión."),
    ],
    task("Escribe en tu hoja cinco oraciones: tres sobre tus gustos con love, hate y don't mind (con -ing), una con I'd like to y una comparación con -er than usando los datos: Mount A mide 3.500 m y Mount B mide 4.200 m (de ejemplo). (mountain = montaña)", "I love reading. I hate waiting. I don't mind washing dishes. I'd like to visit the desert. Mount B is higher than Mount A.", ["tres gustos con -ing", "una oración con I'd like to", "una comparación correcta con than"], ["cinco oraciones en la hoja"], ["usar to después de enjoy", "comparar sin than"], "Pide que cambie una oración de gusto por una opinión con I find y un adjetivo."),
    "Copia la tabla de adjetivos y escribe su comparativo y su superlativo.",
    "Escribe dos oraciones que comparen dos prendas de tu ropa, con -er than o more…than.",
)

# ============================================================ clase 3: planes, predicciones y condiciones
PLAN3 = "Plans of the Rojas family (datos de ejemplo). On Monday, Pablo is going to the dentist at 4:00 p.m. On Tuesday, Grandmother is arriving at 10:30 a.m. Next Saturday, the whole family is going to Chiloe by bus."
G_PLAN3 = "(dentist = dentista; arriving = llegando; whole = toda; by bus = en bus)"

lesson(
    OA, 3,
    "Los mensajes y las agendas escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a expresar intenciones, planes futuros, predicciones y condiciones con be going to, el presente continuo, will e if. Sirve para escribir agendas, mensajes y pronósticos.",
    ["Sé usar am, is y are.", "Conozco el presente simple."],
    [
        "Para hablar de planes e intenciones usa be going to + verbo: «I'm going to visit my aunt». También se usa el presente continuo (am/is/are + -ing) con un tiempo futuro cuando ya está acordado: «She's arriving tomorrow morning». Las dos formas sirven para un plan; el presente continuo suena más seguro, porque ya hay un horario o una cita.",
        "Para predecir usa will + verbo, sin to: «People will travel to Mars in the future». Will también sirve para decisiones o promesas. Para expresar una condición usa if + presente simple y, en la otra parte, will + verbo: «If you cook, I'll help you». Nunca escribas will después de if: «If it will rain» es incorrecto. Se escribe «If it rains, we will stay at home».",
        "Para escribir un plan indica siempre cuándo: tomorrow, next week, on Saturday, in July. Para una predicción pon una fecha lejana o in the future. Si el hecho es muy probable puedes escribir I'm sure it will…, y si no lo sabes, I think it will…. Revisa que cada oración con if tenga dos partes: la condición y el resultado.",
    ],
    [("be going to", "ir a / planear"), ("will", "futuro: predicciones y promesas"), ("if", "si (condición)"), ("tomorrow morning", "mañana en la mañana"), ("next week", "la próxima semana"), ("in the future", "en el futuro"), ("I'll", "I will (abreviado)")],
    [
        ("Elegir la forma para un plan", "Completa: «Tomorrow I ___ visit my grandmother.» Opciones: am going to, went.",
         ["Tomorrow indica futuro.", "Un plan usa be going to.", "La respuesta es am going to."], "am going to"),
        ("Completar una condición", "Completa: «If it rains tomorrow, we ___ stay at home.» Opciones: will, would.",
         ["La condición está en presente: if it rains.", "El resultado usa will.", "Se completa con will."], "will"),
    ],
    [
        ("Escribir «If it will rain, we stay home».", "Después de if se usa presente simple, no will.", "Escribe If it rains, we will stay at home."),
        ("Escribir «She will to arrive».", "Después de will va el verbo sin to.", "Escribe She will arrive."),
    ],
    [
        ("«Be going to» se usa para: a) planes b) hechos pasados", "a", "Expresa intenciones sobre el futuro."),
        ("«Will» se usa para: a) predicciones b) acciones terminadas", "a", "Predice qué ocurrirá en el futuro."),
        ("Elige la forma correcta: «If you study, you ___ pass the test.» a) will b) passed", "a", "El resultado de una condición lleva will."),
    ],
    [
        (f"Lee: {PLAN3} {G_PLAN3} ¿Quién va al dentista? a) Pablo b) Grandmother", "a", "El texto dice Pablo is going to the dentist."),
        (f"Lee: {PLAN3} {G_PLAN3} ¿Cuándo llega la abuela? a) On Tuesday at 10:30 a.m. b) On Monday at 4:00 p.m.", "a", "El texto dice On Tuesday, Grandmother is arriving at 10:30 a.m."),
        (f"Lee: {PLAN3} {G_PLAN3} ¿Adónde va toda la familia el próximo sábado? a) To Chiloe by bus b) To the dentist", "a", "El plan dice the whole family is going to Chiloe by bus."),
    ],
    [
        ("Completa: «In the future, people ___ in space hotels.» Opciones: will live, lived.", "will live", "In the future pide una predicción con will."),
        ("Completa: «If you finish your homework, you ___ play outside.» Opciones: will, finished.", "will", "El resultado de la condición lleva will y el verbo sin to."),
        ("Completa: «She ___ tomorrow morning.» Elige la forma de plan acordado: a) is arriving b) arrived", "a", "El presente continuo con tomorrow expresa un plan acordado."),
    ],
    [
        ("Frase: «In 2100, cars will fly.» ¿Es un plan o una predicción? Escribe plan o predicción.", "Predicción", "Habla de un futuro lejano y no tiene una cita concreta."),
        ("Frase: «I'm meeting Eva at 5:00.» ¿Es un plan acordado o una predicción? Escribe plan o predicción.", "Plan", "Tiene una hora y una persona; ya está acordado."),
    ],
    [
        ("Une las dos ideas en una oración con if: «You cook. I help you.» ¿Qué oración es correcta? a) If you cook, I will help you b) If you will cook, I help you", "a", "La condición va en presente y el resultado con will."),
        ("Elige el orden correcto de la condición: a) If the bus is late, I will call you b) If the bus will be late, I call you", "a", "La condición usa presente y el resultado usa will."),
    ],
    [("Mensaje de ejemplo: «Hi Lola, we're arriving on Friday at 9:00 a.m. If the bus is late, I'll call you.» (arriving = llegando; late = atrasado) ¿Qué hará la persona si el bus llega tarde? a) Call b) Wait", "a", "Dice I'll call you.")],
    [
        ("¿Qué se escribe después de will: el verbo con to o sin to?", "Sin to", "Se escribe will + verbo sin to."),
        ("¿Qué tiempo se usa después de if: presente simple o will?", "Presente simple", "If it rains, we will stay."),
        ("¿Qué forma sirve para un plan: be going to o would?", "Be going to", "Expresa una intención sobre el futuro."),
    ],
    task("Escribe en tu hoja cuatro oraciones de ejemplo sobre tu fin de semana y el futuro: un plan con be going to (por ejemplo, ver una película), un plan acordado con el presente continuo y una hora, una predicción con will y una condición con if. (película = film; ver = watch)", "I'm going to watch a film on Saturday. My cousin is arriving on Sunday at 4:00. In ten years, we will travel by electric trains. If it rains, I will read a book.", ["el plan usa be going to", "el plan acordado usa la forma -ing con una hora", "la condición usa presente después de if"], ["cuatro oraciones en la hoja"], ["escribir will después de if", "olvidar to en be going to"], "Pide que cambie la condición para otro clima, como If it is sunny, y escriba un resultado."),
    "Copia la tabla de planes, predicciones y condiciones y escribe una oración con cada forma.",
    "Escribe dos predicciones en inglés sobre cómo será tu colegio dentro de diez años, con will.",
)

# ============================================================ clase 4: describir y preposiciones de tiempo y dirección
DES4 = "Travel review (datos de ejemplo). The destination was great. Our hotel was a big white house near the beach. The man in the blue hat was our guide; he was Peruvian. The woman with the long braid was the cook; she was Brazilian. Every morning we walked from the hotel to the market and went into a small bakery. At five o'clock we came out of the museum and took the bus."
G_DES4 = "(travel review = reseña de un viaje; destination = destino; guide = guía; braid = trenza; cook = cocinera; market = mercado; bakery = panadería; museum = museo)"

lesson(
    OA, 4,
    "Las reseñas y las oraciones escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a identificar y describir objetos, lugares y personas, y a usar preposiciones de tiempo y de dirección. Sirve para escribir reseñas, correos y descripciones claras.",
    ["Conozco adjetivos de tamaño y color.", "Sé usar on, in y at con días, meses y horas."],
    [
        "Para describir un objeto o lugar, pon los adjetivos antes del sustantivo y en este orden: opinión, tamaño, edad y color. «It's a big brown building». «The hotel was a beautiful old house». Con tamaño, edad y color: a big old white house. Para la nacionalidad usa adjetivos con mayúscula: Chilean, Peruvian, French, Brazilian, Spanish. «They are French». Para evaluar un lugar usa palabras como great, good, comfortable: «The location was great. The accommodation was comfortable. The destination was beautiful».",
        "Para identificar a una persona entre varias usa in (con ropa) o with (con una característica): «The man in the blue hat», «The woman with the long braid». Para las preposiciones de tiempo recuerda: on Monday (día), in December (mes), at 5 o'clock (hora). Para la dirección usa from… to… (desde… hasta…), into (hacia adentro de), out of (hacia afuera de): «We walked from the hotel to the market. She went into the bank. He came out of the store».",
        "Para escribir una buena descripción, elige tres adjetivos precisos, usa la preposición adecuada y verifica que cada detalle sea verdadero. Si describes a una persona, usa solo características que se pueden ver. Evita comentar el aspecto de otras personas de forma negativa y usa un tono respetuoso. Revisa también las mayúsculas en los nombres de nacionalidades.",
    ],
    [("big brown building", "edificio grande y café"), ("Chilean / Peruvian / French", "chileno / peruano / francés"), ("the man in…", "el hombre con (ropa)…"), ("the woman with…", "la mujer con (característica)…"), ("location / accommodation / destination", "ubicación / alojamiento / destino"), ("into / out of", "hacia adentro / hacia afuera"), ("from… to…", "desde… hasta…")],
    [
        ("Ordenar los adjetivos", "Elige la frase bien ordenada: «a big brown building» o «a brown big building».",
         ["En inglés el tamaño va antes del color.", "Big es tamaño y brown es color.", "Queda a big brown building."], "a big brown building"),
        ("Identificar a una persona", "En una foto de ejemplo hay una mujer con una chaqueta roja y otra con pelo largo. Para referirte a la que lleva la chaqueta roja, ¿qué usas: in o with?",
         ["La ropa se dice con in.", "La característica física se dice con with.", "Para la chaqueta se usa in."], "in"),
    ],
    [
        ("Escribir «They are chilean» con minúscula.", "Las nacionalidades se escriben con mayúscula.", "Escribe They are Chilean."),
        ("Decir «We went to the bank» cuando entraron al banco.", "Falta indicar que entraron.", "Para entrar usa into: We went into the bank."),
    ],
    [
        ("Elige la frase bien escrita. a) a small red car b) a red small car", "a", "Primero el tamaño y luego el color."),
        ("La nacionalidad de una persona de Perú es: a) Peruvian b) Peru", "a", "Peruvian es el adjetivo de nacionalidad."),
        ("«Accommodation» significa: a) alojamiento b) destino", "a", "Accommodation es donde te quedas durante un viaje."),
    ],
    [
        (f"Lee: {DES4} {G_DES4} ¿Cómo era el hotel? a) A big white house near the beach b) A small blue building", "a", "El texto dice a big white house near the beach."),
        (f"Lee: {DES4} {G_DES4} ¿Qué nacionalidad tenía el guía? a) Peruvian b) Brazilian", "a", "El guía era el hombre con el sombrero azul y era peruano."),
        (f"Lee: {DES4} {G_DES4} ¿Quién era la cocinera? a) The woman with the long braid b) The man in the blue hat", "a", "La cocinera es la mujer con la trenza larga."),
    ],
    [
        ("Completa: «We walked ___ the hotel ___ the market.» a) from, to b) into, out of", "a", "Caminaron desde un lugar hasta otro."),
        ("Completa: «She went ___ the bank to ask for information.» Opciones: into, out of.", "into", "Para entrar a un lugar se usa into."),
        ("Completa: «He came ___ the store with two bags.» Opciones: out of, into.", "out of", "Para salir de un lugar se usa out of."),
    ],
    [
        ("Corrige: «They are french and they arrive ___ December in Santiago.» ¿Qué dos cambios hay que hacer? a) French con mayúscula y usar in b) Cambiar arrive por arrives", "a", "Las nacionalidades llevan mayúscula y los meses usan in."),
        ("Tres personas: Ana lleva chaqueta roja y pelo largo. Bea lleva chaqueta roja y pelo corto. Cata lleva chaqueta azul y pelo largo. ¿A quién describe «the woman with long hair in the red jacket»? a) Ana b) Bea", "a", "Es la única que tiene las dos características."),
    ],
    [
        (f"Lee: {DES4} {G_DES4} Un compañero escribe: «At five o'clock we went into the museum.» ¿Qué dice realmente el texto? a) They came out of the museum at five o'clock b) They went into the museum at five o'clock", "a", "El texto dice came out of the museum."),
        ("Reseña de ejemplo: «The accommodation was a small yellow house with a big garden.» ¿Qué parte describe el lugar donde se alojaron? a) A small yellow house b) A big garden", "a", "Accommodation es el alojamiento: la casa; el jardín es otro lugar."),
    ],
    [("En el blog del colegio, un estudiante escribe una reseña de una excursión: «The destination was a big old museum. The guide, a Chilean woman with short hair, was very friendly.» (museum = museo; friendly = amable) ¿Cuál es la nacionalidad de la guía? a) Chilean b) French", "a", "El texto dice A Chilean woman.")],
    [
        ("¿Qué va antes en una frase de adjetivos: el tamaño o el color?", "El tamaño", "Big brown building."),
        ("¿Cómo se escribe la nacionalidad de Francia: french o French?", "French", "Las nacionalidades llevan mayúscula."),
        ("¿Qué usas para salir de un lugar: into o out of?", "Out of", "Out of significa fuera de un lugar."),
    ],
    task("Escribe una reseña de ejemplo de seis oraciones de un viaje inventado. Incluye: una descripción de un edificio con adjetivos de tamaño y color, una descripción de una persona con in o with, una nacionalidad con mayúscula, tres preposiciones (from… to…, into, out of) y la frase «The location was great». Usa la lista de ejemplo: casa pequeña azul, guía con gorra roja, vecina argentina. (gorra = cap; vecina = neighbour; Argentina = Argentinian)", "We stayed in a small blue house. The guide, the man in the red cap, was kind. Our neighbour was Argentinian. We walked from the house to the beach. We went into a small shop and came out of it with ice cream. The location was great.", ["adjetivos en orden tamaño-color", "nacionalidad con mayúscula", "usa from… to…, into y out of"], ["reseña de seis oraciones en la hoja"], ["poner el color antes del tamaño", "escribir la nacionalidad con minúscula"], "Pide que escriba una pregunta en inglés para identificar a la guía entre dos personas."),
    "Copia las preposiciones y escribe una oración con cada una.",
    "Describe en tres oraciones un lugar de tu barrio, con adjetivos de tamaño y color.",
)

# ============================================================ clase 5: claridad, frecuencia, secuencia, expresiones y unión de ideas
RUT5 = "Mario's morning (datos de ejemplo). First, I look at the timetable. Then I always get on the bus at 7:30 and get off at the school stop. I never arrive late. I usually listen to music, but I sometimes read. I will wait until Monday to tell my friend the news. Let's meet at the gate. After that, we go to class."
G_RUT5 = "(get on = subir a; arrive = llegar; late = tarde; timetable = horario; get off = bajar de; stop = paradero; gate = portón; wait = esperar; news = la noticia)"

lesson(
    OA, 5,
    "Las rutinas y los mensajes escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir con claridad usando adverbios de frecuencia, palabras de secuencia, conectores y expresiones comunes como look at, get on y arrive at. Sirve para escribir una rutina o un mensaje que otra persona entienda.",
    ["Conozco el presente simple y first, then y finally.", "Sé usar and, but y so."],
    [
        "Los adverbios de frecuencia (frequency adverbs) dicen cada cuánto ocurre algo: always (siempre), usually (por lo general), sometimes (a veces) y never (nunca). Van antes del verbo principal y después de be: «I always get on the bus. She is never late». Para ordenar acciones usa first, next, then, after that y finally. Para unir ideas usa and then (y luego), so (así que, por eso), until (hasta que) y also (también): «It was far, so we took the bus. I'll wait until Monday».",
        "Las expresiones comunes (common expressions) se aprenden completas: look at (mirar), get on (subir a) y get off (bajar de) un bus o un tren, arrive at (llegar a un lugar pequeño, como una estación), go on holidays (irse de vacaciones), let's + verbo (hagamos…): «Let's meet at the gate». Muchas palabras tienen sinónimos (synonyms), con significado parecido: big y large, start y begin, glad y happy.",
        "Las palabras compuestas (compound words) unen dos palabras: class + room = classroom; note + book = notebook; home + work = homework; down + load = download. Si conoces las partes, puedes entender palabras nuevas. Para expresarte con claridad, elige la palabra más precisa, evita repetir la misma y lee tu mensaje como si fueras otra persona: ¿se entiende sin explicación?",
    ],
    [("always / usually", "siempre / por lo general"), ("sometimes / never", "a veces / nunca"), ("first / then / after that", "primero / luego / después de eso"), ("until", "hasta que"), ("look at", "mirar"), ("get on / get off", "subir a / bajar de"), ("arrive at", "llegar a"), ("let's", "hagamos"), ("homework / download", "tarea / descargar")],
    [
        ("Ubicar el adverbio de frecuencia", "Ordena las palabras: always / I / get on / the bus. Escribe la oración.",
         ["Los adverbios van antes del verbo principal.", "El verbo principal es get on.", "Queda I always get on the bus."], "I always get on the bus."),
        ("Entender una palabra compuesta", "¿Qué dos palabras forman «homework» y qué significa?",
         ["Home significa casa.", "Work significa trabajo.", "Juntas son la tarea que se hace en casa."], "Home y work: tarea."),
    ],
    [
        ("Escribir «I go always to school».", "El adverbio de frecuencia va antes del verbo.", "Escribe I always go to school."),
        ("Traducir «get off» como «sacar».", "Es una expresión completa que significa bajar de.", "Aprende get on y get off como bloques."),
    ],
    [
        ("«Never» significa: a) nunca b) siempre", "a", "Never expresa que algo no ocurre."),
        ("«Let's» se usa para: a) hacer una propuesta b) negar una acción", "a", "Let's meet significa quedemos o reunámonos."),
        ("«Notebook» está formada por: a) note y book b) not y ebook", "a", "Es una palabra compuesta por note y book."),
    ],
    [
        (f"Lee: {RUT5} {G_RUT5} ¿A qué hora sube Mario al bus? a) At 7:30 b) At 8:30", "a", "El texto dice I always get on the bus at 7:30."),
        (f"Lee: {RUT5} {G_RUT5} ¿Llega tarde Mario? a) No, he never arrives late b) Yes, he sometimes arrives late", "a", "El texto dice I never arrive late."),
        (f"Lee: {RUT5} {G_RUT5} ¿Qué hace primero? a) He looks at the timetable b) He gets off at the school stop", "a", "La palabra First marca esa acción."),
    ],
    [
        ("Completa: «I'll wait ___ Monday to tell my friend.» Opciones: until, and.", "until", "Until une el tiempo de espera con el momento final."),
        ("Elige la oración correcta: a) She is always happy b) She always is happy", "a", "El adverbio va después del verbo be."),
        ("Completa: «It was far, ___ we took the bus.» Opciones: so, until.", "so", "La segunda parte es el resultado de la primera."),
    ],
    [
        (f"Lee: {RUT5} {G_RUT5} ¿Qué propuesta hace Mario a su amigo? a) Let's meet at the gate b) I always get on the bus", "a", "Let's meet at the gate es la propuesta."),
        ("Elige la frase con preposición correcta: a) We arrive at the station at 6:00 b) We arrive on the station on 6:00", "a", "Arrive at va con lugares pequeños como una estación."),
    ],
    [
        ("Elige el sinónimo de «start» en «The film starts at 8:00»: a) begins b) ends", "a", "Begin y start tienen un significado parecido."),
        ("Une las dos ideas con un conector: «She finished her homework. She went to play.» ¿Qué opción es mejor? a) She finished her homework and then she went to play b) She finished her homework until she went to play", "a", "And then une dos hechos que ocurren en orden."),
    ],
    [("Un compañero nuevo recibe este mensaje de ejemplo: «First, get on bus 12. Then get off at the library. Let's meet at the gate.» (library = biblioteca; gate = portón) ¿Dónde se baja del bus? a) At the library b) At the gate", "a", "El mensaje dice get off at the library; el portón es donde se encuentran después.")],
    [
        ("¿Dónde va always: antes del verbo principal o al final?", "Antes del verbo principal", "I always get on the bus."),
        ("¿Qué significa «go on holidays»?", "Irse de vacaciones", "Es una expresión común."),
        ("¿Qué conector expresa resultado: so o until?", "So", "So introduce una consecuencia."),
    ],
    task("Escribe un mensaje de ejemplo de seis oraciones para un compañero que va a visitar tu colegio. Incluye: un adverbio de frecuencia, First, then y after that, until o so, las expresiones get on / get off y arrive at, una propuesta con Let's y una palabra compuesta como classroom. Datos de ejemplo: bus 22, paradero Plaza, sala 8.", "I always arrive at school at 7:45. First, get on bus 22. Then get off at the Plaza stop. After that, walk to the gate. Let's meet in classroom 8. I'll wait until you arrive.", ["usa un adverbio de frecuencia y la secuencia first, then, after that", "incluye get on / get off o arrive at", "propone algo con Let's"], ["mensaje de seis oraciones en la hoja"], ["poner el adverbio al final", "usar arrive on en vez de arrive at"], "Pide que cambie una palabra por un sinónimo y compruebe que el mensaje se entiende igual."),
    "Copia las expresiones comunes de la clase y escribe una oración con cada una.",
    "Escribe tres palabras compuestas en inglés y dibuja las dos partes de cada una.",
)

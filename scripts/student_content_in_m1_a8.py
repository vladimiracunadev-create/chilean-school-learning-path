"""Cuaderno del estudiante, 1.º medio Inglés (oficial), IN1M OA 08: funciones comunicativas del año al hablar.

Las clases del plan son genéricas; aquí se reparten las funciones del OA así: (1) cantidades, lugares, personas, ocupaciones
y objetos; (2) frecuencia, grado y tiempo, y hábitos pasados con used to; (3) acciones pasadas que continúan (present perfect)
y duración; (4) posibilidades, necesidades y promesas, y preguntas de confirmación; (5) información esencial o adicional,
conectores y voz pasiva. Cada ejercicio trae sus propios datos. Las cifras y los años son de ejemplo.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA = "IN1M OA 08"
MAT = "Las oraciones y diálogos escritos en cada ejercicio, lápiz y una hoja para anotar; si quieres, una persona de tu casa para practicar en voz alta."


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


# ------------------------------------------------------------------ clase 1: cantidades, lugares, personas, objetos
lesson(
    OA, 1, MAT,
    "Aprenderé a expresar cantidades grandes, a describir lugares, personas, ocupaciones y objetos, y a usar palabras compuestas y expresiones comunes. Sirve para hablar con precisión y claridad de lo que me rodea.",
    ["Conozco los números hasta cien y muchos adjetivos simples.", "Sé construir frases con is y are."],
    [
        "Las cantidades grandes se dicen así: one hundred (100), one thousand (1.000), two thousand (2.000), four thousand (4.000) y one million (1.000.000). Para decir si algo alcanza usamos enough (suficiente): We have enough chairs. Para decir que no hay nada usamos no: There is no time. Para enumerar usa first, second, third.",
        "Para describir lugares, personas y ocupaciones: a place can be busy o crowded (con mucha gente). He is interested in robots describe cómo se siente una persona (-ed), y The book is interesting describe la cosa (-ing). She is good at drawing indica habilidad y She is a very organized person describe una cualidad. It's a basketball court es un sustantivo compuesto.",
        "Las palabras compuestas (compound words) se forman con dos palabras: part-time job (trabajo de media jornada), chopstick (palito para comer). Expresiones útiles: apply for a job (postular a un trabajo), talk about (hablar de), for example, What's it like? (¿cómo es?), Why don't we...? (¿por qué no...?) y Nice to meet you. Para describir un objeto, ordena los adjetivos así: opinión, tamaño, edad, forma, material y tipo, y al final el sustantivo: an old wooden musical instrument, a small round metal box.",
    ],
    [("enough", "suficiente"), ("crowded / busy", "con mucha gente / ocupado"), ("interested / interesting", "interesado / interesante"), ("good at", "bueno para"), ("part-time job", "trabajo de media jornada"), ("What's it like?", "¿Cómo es?")],
    [
        ("Decir cantidades", "Escribe en palabras 2.000 y 1.000.000.", ["2.000 son dos mil.", "1.000.000 es un millón.", "En inglés: two thousand y one million."], "two thousand; one million"),
        ("Distinguir -ed y -ing", "Completa: «The film is ___. I am ___ in films.» (interesting / interested)", ["El adjetivo de la cosa termina en -ing.", "El adjetivo de la persona que siente termina en -ed.", "The film is interesting; I am interested."], "interesting; interested"),
    ],
    [
        ("Decir interested para una cosa, como The film is interested.", "Se mezclan los dos adjetivos porque en español es la misma palabra.", "Usa -ing para la cosa y -ed para quien siente."),
        ("Poner el material antes de la edad, como a wooden old box.", "Se traduce el orden del español.", "Ordena: edad, material y luego el sustantivo."),
    ],
    [
        ("¿Cómo se escribe en cifras four thousand? A) 4.000 B) 40.000", "A) 4.000", "Four thousand es cuatro mil."),
        ("«We have enough chairs» significa: A) tenemos sillas suficientes B) no tenemos sillas", "A) tenemos sillas suficientes", "Enough significa suficiente."),
        ("¿Qué palabra describe un lugar con mucha gente? A) crowded B) empty", "A) crowded", "Crowded es lleno de gente; empty es vacío."),
    ],
    [
        ("Completa: «The book is ___.» A) interesting B) interested", "A) interesting", "Describe la cosa, por eso termina en -ing."),
        ("Completa: «My sister is ___ in robots.» A) interested B) interesting", "A) interested", "Describe cómo se siente la persona."),
        ("¿Qué significa «She is good at drawing»? A) se le da bien dibujar B) le molesta dibujar", "A) se le da bien dibujar", "Good at + -ing indica habilidad."),
    ],
    [
        ("Escribe en palabras 1.000.000.", "one million", "Un millón es one million."),
        ("Completa: «We have ___ money to buy the tickets.» (Sí alcanza). A) enough B) no", "A) enough", "Enough dice que es suficiente; no diría que no hay nada."),
        ("¿Qué frase tiene el orden natural de adjetivos? A) an old wooden box B) a wooden old box", "A) an old wooden box", "La edad va antes del material."),
    ],
    [
        ("¿Qué frase es correcta para describir a una persona? A) She is a very organized person. B) She is a very organize person.", "A) She is a very organized person.", "Organized es el adjetivo."),
        ("¿Qué expresión significa «trabajo de media jornada»? A) part-time job B) job part-time", "A) part-time job", "En un compuesto, la descripción va antes del sustantivo."),
    ],
    [
        arith("Una tienda vende 4.000 cuadernos y 2.000 lápices. ¿Cuántos artículos son en total?", "4000+2000", "Se suman las dos cantidades.", " artículos"),
        ("Describe un objeto: pequeño, redondo y de metal. ¿Qué frase tiene el orden correcto? A) a small round metal box B) a metal round small box", "A) a small round metal box", "El orden natural es tamaño, forma y material antes del sustantivo."),
    ],
    [("Un aviso dice: «Wanted: part-time job at a library. You must be good at organizing books and interested in reading. Apply for the job this week.» (wanted = se busca, must = debes, organizing = organizar). ¿Qué piden? A) ser bueno para organizar libros e interesado en leer B) hablar tres idiomas", "A) ser bueno para organizar libros e interesado en leer", "El aviso usa good at e interested in.")],
    [
        ("En Inglés de 1.º medio (OA 8, clase 1): ¿cómo se dice 1.000.000?", "One million", "Es un millón."),
        ("En Inglés de 1.º medio (OA 8, clase 1): ¿cuándo se usa -ing y cuándo -ed en interesting e interested?", "-ing para la cosa y -ed para la persona que siente", "Describen cosas o sentimientos."),
        ("En Inglés de 1.º medio (OA 8, clase 1): ¿qué significa enough?", "Suficiente", "Dice que la cantidad alcanza."),
    ],
    task("Elige un lugar que conoces y un objeto de tu casa. Escribe en inglés cuatro frases: una con una cantidad (por ejemplo, two thousand), una con crowded o busy, una con interested in o good at y una que describa el objeto con tres adjetivos en orden (por ejemplo, an old wooden chair). Las cifras pueden ser de ejemplo.", "There are two thousand people in my town centre. It is very busy on Saturdays. My father is good at cooking. We have a big old wooden table.", ["usa una cantidad grande bien escrita", "usa crowded o busy", "usa good at o interested in", "ordena los adjetivos del objeto"], ["hoja con cuatro frases", "lectura en voz alta"], ["decir interested para la cosa", "poner el material antes de la edad"], "Reconoce cada función lograda y pide revisar el orden de adjetivos si falla."),
    "Escribe tres cantidades grandes en cifras y en palabras en inglés.",
    "Describe a un familiar con una cualidad, una habilidad y un interés, usando very, good at e interested in.",
)

# ------------------------------------------------------------------ clase 2: frecuencia, grado, tiempo y hábitos pasados
lesson(
    OA, 2, MAT,
    "Aprenderé a señalar frecuencia, grado y tiempo de las acciones y a hablar de hábitos pasados con used to. Sirve para contar cuánto, cada cuánto y desde cuándo hago algo.",
    ["Sé usar el presente y el pasado simple.", "Conozco palabras como always, never y yesterday."],
    [
        "Para hablar del tiempo hay tres palabras clave. For indica cuánto tiempo dura algo: for three years. Since indica desde cuándo: since 2018, since March. Ago indica cuánto tiempo atrás ocurrió algo y va con el pasado simple: I studied French five years ago. Con for y since se usa have o has + participio: He has worked here since 2010 (todavía trabaja).",
        "La frecuencia (frequency) dice cada cuánto: once a month, twice a week, three times a year, every day. Los adverbios always, usually, sometimes y never van antes del verbo: I usually go to the bank. El grado (degree) dice cuánto: a bit, quite (bastante) y really (muy) o very. She is quite shy es menos fuerte que She is really shy.",
        "Used to + verbo habla de un hábito pasado que ya no existe: I used to work at the coffee shop, but now I work at a department store. En pregunta se dice Did you use to...? y en negativo, I didn't use to.... Es distinto de used to + sustantivo o -ing, que significa estar acostumbrado. Aquí solo trabajamos el hábito pasado.",
    ],
    [("for / since / ago", "durante / desde / hace"), ("once a month", "una vez al mes"), ("twice a week", "dos veces por semana"), ("quite / really", "bastante / muy"), ("used to", "solía (ya no)"), ("department store", "tienda por departamentos")],
    [
        ("Elegir for o since", "Completa con for o since: «She has lived in Chile ___ 2019 and ___ six years.»", ["Un año de inicio pide since.", "Una duración pide for.", "Since 2019 y for six years."], "since 2019; for six years"),
        ("Hablar de un hábito pasado", "Quieres decir que antes ibas en bus al colegio y ahora vas en bicicleta. ¿Qué frase usas?", ["El hábito pasado se dice con used to.", "Agrego el contraste con now.", "I used to go by bus, but now I go by bike."], "I used to go by bus, but now I go by bike."),
    ],
    [
        ("Usar since con una duración, como since five years.", "Se mezclan duración y punto de inicio.", "Usa for con la duración y since con el inicio."),
        ("Decir I used to going en vez de I used to go.", "Se confunde con estar acostumbrado.", "Para hábito pasado usa used to + verbo en base."),
    ],
    [
        ("Completa: «___ three years.» A) for B) since", "A) for", "Three years es una duración."),
        ("Completa: «___ 2019.» A) since B) for", "A) since", "2019 es un punto de inicio."),
        ("Completa: «five years ___» A) ago B) for", "A) ago", "Ago va después de la duración y con el pasado simple."),
    ],
    [
        ("¿Qué significa twice a week? A) dos veces por semana B) cada dos semanas", "A) dos veces por semana", "Twice significa dos veces."),
        ("«She is quite shy» significa: A) es bastante tímida B) no es tímida", "A) es bastante tímida", "Quite significa bastante."),
        ("Completa: «I ___ the guitar two years ago.» A) started B) have started", "A) started", "Con ago se usa el pasado simple."),
    ],
    [
        ("Completa: «He has worked here ___ 2010.» A) since B) for", "A) since", "2010 es un inicio."),
        ("Completa: «She has lived in Chile ___ six months.» A) for B) since", "A) for", "Six months es una duración."),
        ("Completa: «I ___ to play chess, but now I don't.» A) used B) use", "A) used", "El hábito pasado es used to."),
    ],
    [
        ("¿Qué frase es correcta? A) I have lived here for five years. B) I have lived here since five years.", "A) I have lived here for five years.", "Una duración lleva for."),
        ("Comparas «She is really shy» y «She is quite shy». ¿Cuál indica más timidez? A) la primera B) la segunda", "A) la primera", "Really es más fuerte que quite."),
    ],
    [
        arith("Vas al gimnasio three times a week. ¿Cuántas veces vas en 4 semanas?", "3*4", "Se multiplican las visitas semanales por 4.", " veces"),
        ("«I used to walk to school, but now I take the bus.» ¿Cómo va hoy al colegio? A) en bus B) caminando", "A) en bus", "Used to walk es el hábito pasado; hoy toma el bus."),
    ],
    [("Una persona cuenta: «I worked at a bakery two years ago. Now I work in a library. I have worked here since March. I go to the market once a week.» (bakery = panadería, library = biblioteca, market = feria). ¿Qué enunciado es verdadero? A) trabaja en la biblioteca desde marzo B) trabaja en la panadería desde hace dos años", "A) trabaja en la biblioteca desde marzo", "Since March indica el inicio en la biblioteca; la panadería fue hace dos años.")],
    [
        ("En Inglés de 1.º medio (OA 8, clase 2): ¿cuándo se usa for?", "Con una duración, como for three years", "Dice cuánto tiempo dura algo."),
        ("En Inglés de 1.º medio (OA 8, clase 2): ¿cuándo se usa since?", "Con un punto de inicio, como since 2018", "Dice desde cuándo."),
        ("En Inglés de 1.º medio (OA 8, clase 2): ¿qué significa used to + verbo?", "Un hábito pasado que ya no ocurre", "Contrasta antes y ahora."),
    ],
    task("Escribe en inglés cinco frases sobre tu vida (los datos pueden ser de ejemplo): una con for, una con since, una con ago, una con once a month, twice a week o three times a year, y una con used to. Después subraya el conector de tiempo de cada una.", "I have studied English for six years. I have lived here since 2018. I started school ten years ago. I go to the library once a month. I used to play with toys, but now I play video games.", ["usa for y since con el significado correcto", "usa ago con el pasado simple", "usa used to + verbo para un hábito pasado"], ["hoja con cinco frases", "lectura en voz alta"], ["usar since con una duración", "usar ago con have"], "Reconoce lo logrado y revisa con ella qué palabra va con duración y cuál con inicio."),
    "Anota en una tabla cinco hábitos que tienes ahora y cinco que tenías antes, con used to.",
    "Pregunta a una persona de tu casa How often do you...? y registra su frecuencia con once a month, twice a week o every day.",
)

# ------------------------------------------------------------------ clase 3: present perfect y duración
lesson(
    OA, 3, MAT,
    "Aprenderé a hablar de acciones pasadas que continúan en el presente o que son experiencias, usando have o has + participio, ever, never y How long. Sirve para contar qué he hecho y desde cuándo.",
    ["Sé usar el pasado simple.", "Conozco for y since."],
    [
        "El present perfect se forma con have o has + participio. El participio regular termina en -ed: saved, studied. Los irregulares hay que aprenderlos: be – been, see – seen, eat – eaten, go – gone, do – done, write – written, take – taken, give – given, know – known. Con I, you, we y they se usa have; con he, she e it se usa has.",
        "Tiene tres usos principales. Una acción que empezó en el pasado y continúa: I have studied for three days. Una experiencia de vida, con ever (alguna vez) y never (nunca): Have you ever eaten insects? I have never seen that program. Una acción con un propósito o resultado actual: I have saved money to buy a bike. No se usa con fechas pasadas concretas, como yesterday o last year; ahí va el pasado simple.",
        "Para preguntar la duración se usa How long have you been friends? y se responde con for (for two years) o since (since 2010). Ojo con been y gone: She has been to Peru significa que fue y ya volvió; She has gone to Peru significa que está allá. Las respuestas cortas son Yes, I have. y No, I haven't.",
    ],
    [("have / has + participio", "forma del present perfect"), ("ever / never", "alguna vez / nunca"), ("How long have you...?", "¿Hace cuánto...?"), ("been / gone", "estuvo y volvió / está allá"), ("seen, eaten, done", "participios irregulares"), ("Yes, I have.", "Sí, he...")],
    [
        ("Armar una experiencia", "Quieres decir que nunca has visto una ballena. ¿Qué frase usas?", ["Experiencia de vida con never.", "Uso have + participio de see.", "I have never seen a whale."], "I have never seen a whale."),
        ("Preguntar una duración", "Quieres saber hace cuánto tiempo son amigos Ana y Pedro. ¿Qué preguntas?", ["La duración se pregunta con How long.", "Uso have con they.", "How long have Ana and Pedro been friends?"], "How long have Ana and Pedro been friends?"),
    ],
    [
        ("Usar have con yesterday, como I have eaten yesterday.", "Se mezcla un hecho con fecha concreta con el present perfect.", "Con yesterday usa el pasado simple: I ate yesterday."),
        ("Decir I have went en vez de I have gone.", "Se usa el pasado simple como participio.", "Aprende la tabla: go – went – gone."),
    ],
    [
        ("¿Cuál es el participio de see? A) seen B) saw", "A) seen", "Saw es el pasado simple; seen es el participio."),
        ("¿Cuál es el participio de eat? A) eaten B) ate", "A) eaten", "Ate es el pasado; eaten es el participio."),
        ("Completa: «She ___ studied for three days.» A) has B) have", "A) has", "Con she se usa has."),
    ],
    [
        ("¿Qué significa Have you ever eaten fish? A) ¿has comido pescado alguna vez? B) ¿comiste pescado ayer?", "A) ¿has comido pescado alguna vez?", "Ever pregunta por una experiencia de vida."),
        ("¿Qué significa «I have never seen that program»? A) nunca he visto ese programa B) vi ese programa ayer", "A) nunca he visto ese programa", "Never significa nunca."),
        ("Completa: «I have saved money ___ buy a bike.» A) to B) for to", "A) to", "To expresa el propósito."),
    ],
    [
        ("Completa con for o since: «We have been friends ___ 2018.» A) since B) for", "A) since", "2018 es un inicio."),
        ("Completa con for o since: «They have lived here ___ two years.» A) for B) since", "A) for", "Two years es una duración."),
        ("¿Qué pregunta corresponde a «For two years»? A) How long have you been friends? B) Have you ever been friends?", "A) How long have you been friends?", "How long pide la duración."),
    ],
    [
        ("¿Qué frase es correcta? A) I have never been to Peru. B) I have never went to Peru.", "A) I have never been to Peru.", "El participio de be es been."),
        ("«Sara has been to Peru» y «Sara has gone to Peru». ¿Cuál indica que ya volvió? A) has been B) has gone", "A) has been", "Been indica ida y regreso; gone, que sigue allá."),
    ],
    [
        ("¿Qué frase es correcta? A) I saw that film yesterday. B) I have seen that film yesterday.", "A) I saw that film yesterday.", "Con yesterday se usa el pasado simple."),
        ("Una amiga pregunta «Have you ever visited a museum?» y respondes que no. ¿Qué respuesta corta es correcta? A) No, I haven't. B) No, I didn't.", "A) No, I haven't.", "Se responde con el mismo auxiliar have."),
    ],
    [("Un diálogo: «Mia: Have you ever eaten sushi? Leo: No, I haven't. But I have eaten rice with fish.» (sushi = sushi, rice = arroz). ¿Qué es verdadero? A) Leo nunca ha comido sushi B) Leo comió sushi ayer", "A) Leo nunca ha comido sushi", "Dice No, I haven't a la pregunta con ever.")],
    [
        ("En Inglés de 1.º medio (OA 8, clase 3): ¿cómo se forma el present perfect?", "Have o has + participio", "Has va con he, she e it."),
        ("En Inglés de 1.º medio (OA 8, clase 3): ¿qué diferencia hay entre been y gone?", "Been: fue y volvió; gone: sigue allá", "Cambia el sentido de la frase."),
        ("En Inglés de 1.º medio (OA 8, clase 3): ¿cómo se pregunta una duración?", "How long have/has...?", "Se responde con for o since."),
    ],
    task("Entrevista a una persona de tu casa y escribe en inglés tres preguntas con Have you ever...? y una con How long have you...? (por ejemplo, How long have you lived here?). Anota sus respuestas con Yes, I have. / No, I haven't. y con for o since. Los datos pueden ser de ejemplo.", "Have you ever eaten oysters? Have you ever seen a volcano? Have you ever given a speech? How long have you lived here? — No, I haven't. Yes, I have. No, I haven't. For ten years.", ["forma bien tres preguntas con ever", "forma bien How long have you...?", "responde con las respuestas cortas y for o since"], ["hoja con preguntas y respuestas", "lectura en voz alta"], ["usar el pasado simple como participio", "usar since con una duración"], "Reconoce las preguntas bien formadas y revisa los participios irregulares con ella."),
    "Escribe diez participios, cinco regulares y cinco irregulares, y una frase con cada uno.",
    "Escribe cinco cosas que nunca has hecho con I have never... y una que ya hiciste con I have already....",
)

# ------------------------------------------------------------------ clase 4: posibilidades, necesidades, promesas y confirmación
lesson(
    OA, 4, MAT,
    "Aprenderé a expresar predicciones, necesidades, promesas y posibilidades con will probably, might, needn't y shall, y a confirmar información con preguntas de confirmación (question tags). Sirve para conversar con naturalidad y comprobar lo que creo saber.",
    ["Conozco will y el presente simple.", "Sé responder preguntas de sí o no."],
    [
        "Para hablar de lo que puede ocurrir se usan verbos modales. Will probably expresa una predicción bastante segura: It will probably rain tomorrow. Might expresa una posibilidad menos segura: It might snow. Needn't indica que no es necesario: You needn't hurry (no necesitas apurarte). Shall se usa en inglés formal para prometer u ofrecer: I shall call you tomorrow; y para sugerir: Shall we start?",
        "Las preguntas de confirmación (question tags) se agregan al final de una frase para pedir que la otra persona confirme. La regla es: si la frase es afirmativa, la pregunta es negativa, y al revés. It's nice, isn't it? Your brother wasn't at school, was he? You go to the pool on Fridays, don't you? She will come tomorrow, won't she? La pregunta repite el auxiliar de la frase.",
        "Cuando no hay auxiliar en la frase, se usa do, does o did: You like music, don't you? He plays chess, doesn't he? They left early, didn't they? Si estás casi seguro, la voz baja al final; si de verdad no sabes, la voz sube. Los modales no cambian con he, she o it: might, will y shall se usan igual con todos.",
    ],
    [("will probably", "probablemente"), ("might", "podría (posibilidad)"), ("needn't", "no necesita"), ("shall", "promesa, oferta o sugerencia formal"), ("question tag", "pregunta de confirmación"), ("isn't it? / don't you?", "¿no es cierto?")],
    [
        ("Elegir la pregunta de confirmación", "Completa: «You go to the pool on Fridays, ___?»", ["La frase es afirmativa y usa el presente simple con you.", "La pregunta es negativa y usa don't.", "Es don't you."], "don't you"),
        ("Expresar posibilidad", "El pronóstico dice que quizás nieve, pero no es seguro. ¿Qué frase usas? A) It might snow. B) It needn't snow.", ["Es una posibilidad.", "Might expresa posibilidad.", "Needn't expresa que no es necesario."], "A) It might snow."),
    ],
    [
        ("Usar una pregunta de confirmación afirmativa tras una frase afirmativa.", "Se olvida invertir positivo y negativo.", "Positiva + pregunta negativa; negativa + pregunta positiva."),
        ("Usar needn't para una posibilidad.", "Se piensa que needn't es might negativo.", "Needn't = no hace falta; might = quizás."),
    ],
    [
        ("«It will probably rain tomorrow» expresa: A) una predicción bastante segura B) una promesa", "A) una predicción bastante segura", "Will probably indica una predicción."),
        ("«You needn't hurry» significa: A) no necesitas apurarte B) debes apurarte", "A) no necesitas apurarte", "Needn't indica que no es necesario."),
        ("Completa: «It's nice, ___?» A) isn't it B) is it", "A) isn't it", "Frase afirmativa, pregunta negativa."),
    ],
    [
        ("Completa: «Your brother wasn't at school, ___?» A) was he B) wasn't he", "A) was he", "Frase negativa, pregunta afirmativa."),
        ("Completa: «She will come tomorrow, ___?» A) won't she B) will she", "A) won't she", "Frase afirmativa con will."),
        ("¿Qué frase expresa una promesa formal? A) I shall call you tomorrow. B) I might call you tomorrow.", "A) I shall call you tomorrow.", "Shall expresa una promesa."),
    ],
    [
        ("Completa: «They have finished, ___?» A) haven't they B) don't they", "A) haven't they", "Repite el auxiliar have."),
        ("Completa: «He doesn't like fish, ___?» A) does he B) doesn't he", "A) does he", "Frase negativa, pregunta afirmativa con does."),
        ("Quieres sugerir empezar la reunión. ¿Qué frase usas? A) Shall we start? B) We needn't start.", "A) Shall we start?", "Shall we...? es una sugerencia."),
    ],
    [
        ("La persona que hace la pregunta «You like music, don't you?» ¿qué espera? A) que le confirmen B) que le expliquen qué es música", "A) que le confirmen", "La pregunta de confirmación pide acuerdo."),
        ("¿Cuál frase expresa mayor seguridad? A) It will probably rain. B) It might rain.", "A) It will probably rain.", "Will probably es más seguro que might."),
    ],
    [
        ("Hay una reunión y el profesor dice «You needn't bring your book». ¿Qué debes hacer? A) no hace falta llevar el libro B) debes llevar el libro", "A) no hace falta llevar el libro", "Needn't quita la necesidad."),
        ("Completa: «You play football on Saturdays, ___?» A) don't you B) aren't you", "A) don't you", "Presente simple con you: do/don't."),
    ],
    [("Un diálogo: «Ana: It's cold today, isn't it? Leo: Yes, it is. It might snow tonight. Ana: Then you needn't water the garden.» (cold = frío, snow = nevar, water = regar, garden = jardín). ¿Qué dos posibilidades o necesidades aparecen? A) puede nevar y no hace falta regar B) lloverá seguro y hay que regar", "A) puede nevar y no hace falta regar", "Might snow es posibilidad y needn't water, falta de necesidad.")],
    [
        ("En Inglés de 1.º medio (OA 8, clase 4): ¿cómo se forma una pregunta de confirmación?", "Se invierte el signo: positiva con negativa y negativa con positiva, repitiendo el auxiliar", "Por ejemplo, isn't it?"),
        ("En Inglés de 1.º medio (OA 8, clase 4): ¿qué diferencia hay entre will probably y might?", "Will probably es más seguro; might, una posibilidad menor", "Indican distinto grado de certeza."),
        ("En Inglés de 1.º medio (OA 8, clase 4): ¿qué significa needn't?", "No es necesario", "Quita la obligación."),
    ],
    task("Escribe en inglés una conversación de cuatro líneas entre dos amigos sobre el clima del fin de semana (los datos pueden ser de ejemplo). Usa una pregunta de confirmación afirmativa-negativa, otra negativa-afirmativa, will probably o might, y needn't o shall. Léela con una persona de tu casa.", "A: It's sunny today, isn't it? B: Yes, it is. It will probably be warm tomorrow, too. A: You don't have a jacket, do you? B: No, I don't. I needn't bring one.", ["una pregunta de confirmación bien formada con frase afirmativa", "otra con frase negativa", "un modal de predicción o posibilidad", "needn't o shall bien usado"], ["hoja con el diálogo", "lectura en voz alta"], ["repetir el mismo signo en la frase y la pregunta", "confundir needn't con might"], "Reconoce lo logrado y revisa que cada tag repita el auxiliar de la frase."),
    "Escribe diez frases con question tags, cinco positivas y cinco negativas, sobre personas de tu curso.",
    "Habla con una persona de tu casa sobre el día de mañana usando will probably, might y shall.",
)

# ------------------------------------------------------------------ clase 5: relativas, voz pasiva y conectores
lesson(
    OA, 5, MAT,
    "Aprenderé a dar información esencial o adicional con who y which, a describir acciones con agente desconocido usando la voz pasiva, y a unir ideas con although, both, later, last y so that. Sirve para hablar con más detalle y orden.",
    ["Sé usar el presente y el pasado simple.", "Conozco conectores como and, but y because."],
    [
        "Una oración de relativo (relative clause) agrega información sobre una persona o cosa. Who se usa para personas: Simon is the boy who lives next door. Which se usa para cosas: The science book, which I borrowed from the library, is very interesting. Cuando la información es esencial para saber de quién o de qué hablas, no lleva comas. Cuando es adicional, va entre comas.",
        "La voz pasiva (passive voice) se forma con be + participio y se usa cuando no se sabe quién hizo la acción o no importa: The money was found on the floor; rooms are cleaned daily; plastic is produced from oil. El tiempo lo marca be: was en pasado, is o are en presente. La persona que hace la acción puede aparecer con by, pero a menudo se omite.",
        "Los conectores unen ideas. Although (aunque) opone: Although it's cheap, I'm not sure. Both ... and significa ambos: Both Luis and Tomás are my neighbours. Later (más tarde) y last (por último) ordenan: I'll talk to you later; ...and last he played the piano. So that expresa propósito: He learned English so that he could speak with foreigners.",
    ],
    [("who / which", "que (personas / cosas)"), ("relative clause", "oración de relativo"), ("passive voice", "voz pasiva"), ("was found", "fue encontrado"), ("although / both", "aunque / ambos"), ("so that", "para que")],
    [
        ("Elegir who o which", "Completa: «The girl ___ sits next to me is my cousin.»", ["Hablo de una persona.", "Para personas se usa who.", "The girl who sits next to me."], "who"),
        ("Formar una pasiva", "Convierte a pasiva: «Someone found the keys on the table.» (keys = llaves)", ["No se sabe quién las encontró.", "Uso was + participio.", "The keys were found on the table."], "The keys were found on the table."),
    ],
    [
        ("Usar which para una persona.", "Se usa which para todo.", "Who para personas y which para cosas."),
        ("Olvidar be en la pasiva, como The money found on the floor.", "Se omite el verbo auxiliar.", "Usa be + participio: was found."),
    ],
    [
        ("Completa: «The man ___ lives next door is a doctor.» A) who B) which", "A) who", "Se habla de una persona."),
        ("Completa: «The book, ___ I borrowed from the library, is long.» A) which B) who", "A) which", "Se habla de una cosa."),
        ("¿Qué frase está en pasiva? A) The room is cleaned daily. B) They clean the room.", "A) The room is cleaned daily.", "Es be + participio."),
    ],
    [
        ("Completa: «Plastic ___ produced from oil.» A) is B) are", "A) is", "Plastic es singular."),
        ("Completa: «The windows ___ cleaned every week.» A) are B) is", "A) are", "Windows es plural."),
        ("Completa: «Both Ana ___ Luis are my neighbours.» A) and B) or", "A) and", "Both se completa con and."),
    ],
    [
        ("Completa: «___ it's cheap, I'm not sure about it.» A) Although B) So that", "A) Although", "Se opone barato con no estar seguro."),
        ("Completa: «He learned English ___ he could speak with foreigners.» A) so that B) although", "A) so that", "Expresa el propósito."),
        ("Completa: «I'll talk to you ___.» A) later B) last", "A) later", "Later significa más tarde."),
    ],
    [
        ("¿Qué frase es correcta? A) The money was found on the floor. B) The money found on the floor.", "A) The money was found on the floor.", "La pasiva usa be + participio."),
        ("Une las ideas con who: «Simon is the boy. He lives next door.» A) Simon is the boy who lives next door. B) Simon is the boy which lives next door.", "A) Simon is the boy who lives next door.", "El relativo para personas es who."),
    ],
    [
        ("«We played football, then we ate, and last we cleaned.» ¿Qué actividad fue la final? A) limpiar B) comer", "A) limpiar", "Last marca la última acción."),
        ("Une las ideas con so that: «She saves money. She wants to buy a laptop.» A) She saves money so that she can buy a laptop. B) She saves money although she can buy a laptop.", "A) She saves money so that she can buy a laptop.", "Expresa el propósito de ahorrar."),
    ],
    [("En un aviso del colegio: «The library, which is on the second floor, is cleaned daily. Both Mr Díaz and Mrs Rojas work there.» (second floor = segundo piso, daily = a diario). ¿Qué información es adicional? A) que está en el segundo piso B) que se limpia a diario", "A) que está en el segundo piso", "Va entre comas, introducida por which.")],
    [
        ("En Inglés de 1.º medio (OA 8, clase 5): ¿cuándo se usa who?", "Para hablar de personas", "Which se usa para cosas."),
        ("En Inglés de 1.º medio (OA 8, clase 5): ¿cómo se forma la voz pasiva?", "Be + participio", "Por ejemplo, was found."),
        ("En Inglés de 1.º medio (OA 8, clase 5): ¿qué expresa so that?", "Un propósito: para que", "Dice para qué se hace algo."),
    ],
    task("Escribe en inglés seis frases sobre tu colegio o tu barrio: una con who, una con which entre comas, una en voz pasiva con was o is/are, una con although, una con both ... and y una con so that. Los datos pueden ser de ejemplo.", "My friend Pablo, who plays the guitar, is in my class. The library, which is old, is cleaned daily. The patio was painted last year. Although it is small, our school is nice. Both Ana and Lucas are in the choir. We recycle paper so that we can save trees.", ["usa who para una persona y which para una cosa", "forma una pasiva con be + participio", "usa los tres conectores con sentido"], ["hoja con seis frases", "lectura en voz alta"], ["usar which para personas", "omitir be en la pasiva"], "Reconoce cada estructura lograda y revisa la concordancia de be con el sujeto."),
    "Convierte cinco frases en voz activa a voz pasiva y subraya el participio.",
    "Describe a una persona y un objeto de tu casa con una oración de relativo cada uno.",
)

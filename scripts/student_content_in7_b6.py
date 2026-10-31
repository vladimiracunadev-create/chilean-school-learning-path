"""Cuaderno del estudiante, 7.º básico Inglés (oficial): IN07 OA 16, funciones del lenguaje en textos escritos.

Cada estructura (there is/are, much/many, these/those, must/mustn't, pasado simple y continuo, adverbios, conectores y
expresiones frecuentes) se enseña en la clase antes de usarse en un ejercicio. Todos los textos son originales y breves.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA = "IN07 OA 16"


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


# ============================================================ clase 1: cantidades y comparación
lesson(
    OA, 1,
    "Las listas, los avisos y las oraciones escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a expresar cantidades con there is/are, much, many, some y too, a señalar objetos con these y those y a describir con «it's a plastic bottle». Sirve para escribir sobre lo que hay y cuánto hay en un lugar.",
    ["Sé contar y leer números en inglés.", "Conozco this y that."],
    [
        "Para decir qué hay en un lugar usa there is con una cosa o con algo que no se cuenta (water, milk, homework) y there are con varias cosas: «There is a cat on the sofa. There are four birds in the tree.» Con números: eighty (80) y a hundred (100): «There are eighty students and a hundred chairs.»",
        "Many va con cosas que se cuentan (many books, many people). Much va con cosas que no se cuentan (much water, much noise) y se usa sobre todo en negativas y preguntas: «There isn't much milk. How much water is there?» Some se usa en afirmativas: «There is some water.» A lot of sirve para ambos. Too significa «más de lo necesario»: too many cars, too much noise, too hot.",
        "Para señalar varias cosas cercanas usa these; para varias lejanas, those: «These cars are fast. Those cars are slow.» Para describir un objeto con su material usa it's a + material + objeto: «It's a plastic bottle.» Para comparar cantidades usa more… than y fewer… than: «There are more girls than boys.»",
    ],
    [("there is / there are", "hay (uno / varios)"), ("many / much", "muchos / mucho"), ("some", "algo de, unos"), ("too", "demasiado"), ("these / those", "estos / aquellos"), ("a hundred / eighty", "cien / ochenta"), ("more than", "más que")],
    [
        ("Elegir there is o there are", "Completa: «___ a lot of students in the yard.» Opciones: There is, There are. (yard = patio)",
         ["Students es plural.", "Con plural se usa there are.", "Se lee: There are a lot of students."], "There are"),
        ("Describir un objeto con su material", "Tienes una botella hecha de plástico. Escribe en inglés qué es.",
         ["Se usa it's a.", "Después va el material: plastic.", "Al final va el objeto: bottle."], "It's a plastic bottle."),
    ],
    [
        ("Decir «much books» o «many water».", "No se distingue lo que se cuenta de lo que no.", "Many con cosas que se cuentan; much con lo que no se cuenta."),
        ("Decir «there is» con plurales.", "Se traduce «hay» siempre igual.", "Con varias cosas usa there are."),
    ],
    [
        ("«There ___ a cat on the sofa.» Opciones: is, are.", "is", "Es una sola cosa."),
        ("«There ___ four birds in the tree.» Opciones: is, are.", "are", "Son varios pájaros."),
        ("Elige la palabra para algo que no se puede contar, como el agua: a) much b) many", "a", "Much se usa con cosas incontables."),
    ],
    [
        ("«There isn't ___ milk in the fridge.» Opciones: much, many. (fridge = refrigerador)", "much", "La leche no se cuenta."),
        ("«There aren't ___ chairs in the room.» Opciones: much, many.", "many", "Las sillas se cuentan."),
        ("Para varias cosas que están lejos de ti usas: a) those b) these", "a", "Those señala varias cosas lejanas."),
    ],
    [
        ("Aviso del patio: «There are eighty students and a hundred chairs.» ¿Hay sillas para todos? Responde sí o no.", "Sí", "Cien sillas son más que ochenta estudiantes."),
        ("Tienes dos manzanas en las manos. Completa: «___ apples are green.» Opciones: These, Those.", "These", "Están cerca de ti."),
        ("Elige la oración correcta. a) It's a plastic bottle b) It's a bottle plastic.", "a", "El material va antes del objeto."),
    ],
    [
        ("Un compañero dice: «There are too much cars.» ¿Cómo se corrige? a) There are too many cars b) There is too many cars.", "a", "Cars se cuenta, así que lleva many y are."),
        ("En la sala A hay 24 estudiantes y en la sala B hay 29. ¿Qué oración es verdadera? a) There are more students in Room B than in Room A b) There are more students in Room A than in Room B.", "a", "29 es mayor que 24."),
    ],
    [
        arith("En un salón hay ochenta sillas y treinta y cinco están rotas. ¿Cuántas sillas no están rotas? Escribe el número.", "80-35", "Se restan las sillas rotas."),
        ("Elige la oración correcta. a) There is too much homework today b) There are too many homeworks today.", "a", "Homework no se cuenta, así que lleva much y is."),
    ],
    [("En el casino del colegio hay un cartel: «There are too many people in the line. Please wait outside.» (line = fila; wait = esperen) ¿Qué pide el cartel? a) Esperar afuera porque hay demasiada gente b) Entrar más rápido", "a", "Too many people indica más gente de la conveniente.")],
    [
        ("¿Qué usas con cosas que se cuentan: much o many?", "Many", "Se usa con plural contable."),
        ("«There ___ some water in the jug.» Opciones: is, are. (jug = jarro)", "is", "Water no se cuenta."),
        ("En Inglés (oficial): ¿Qué significa «too»?", "Demasiado", "Indica más de lo necesario."),
    ],
    task("Mira esta lista de una sala de arte: 12 pinceles, 3 tarros de pintura, 1 caja de papeles, un poco de agua. En tu hoja escribe cinco oraciones en inglés sobre qué hay en la sala usando there is, there are, some y «It's a plastic jar». (pinceles = brushes; tarro = jar; caja = box)", "There are twelve brushes. There are three jars of paint. There is one box of paper. There is some water. It's a plastic jar.", ["usa there is y there are correctamente", "usa some o many según corresponde", "incluye una descripción con material"], ["hoja con cinco oraciones"], ["usar much con cosas que se cuentan", "olvidar are con plural"], "Pide que explique por qué eligió is o are en cada oración."),
    "Copia la tabla de vocabulario y escribe una oración con cada palabra.",
    "Escribe tres oraciones comparando cuántas personas hay en tu casa y en la casa de un vecino de ejemplo (inventa cifras claras) con more than.",
)

# ============================================================ clase 2: acciones habituales y en curso
lesson(
    OA, 2,
    "Las oraciones, horarios y preguntas escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a distinguir lo que alguien hace siempre de lo que hace ahora, a hablar de actividades con «riding is cool» y a decir cómo ocurre una acción con adverbios. Sirve para describir rutinas y escenas con claridad.",
    ["Conozco el presente simple con I, you y they.", "Sé los verbos play, swim y cook."],
    [
        "Para hablar de hábitos usa el presente simple con palabras como every week, every day o on Mondays: «She plays tennis every week.» Con he, she e it el verbo lleva -s. Para preguntar usa do o does: «Does he cook? Yes, he does. No, he doesn't.» Para lo que ocurre ahora usa am/is/are + -ing: «He is cooking now.»",
        "Un verbo con -ing puede ser el sujeto de una oración para hablar de actividades: «Riding is cool. Skating is boring.» Así das tu opinión sobre pasatiempos y deportes. Si quieres preguntar y justificar: «Why do you like football? Because it's a team sport.»",
        "Los adverbios de modo (manner) dicen cómo ocurre una acción y se escriben después del verbo: «She sings softly. He speaks quietly. They shout loudly.» Muchos se forman con -ly (quick → quickly), pero fast es igual como adjetivo y adverbio: «They run very fast.» Very aumenta la intensidad (very fast = rapidísimo).",
    ],
    [("every week", "cada semana"), ("now", "ahora"), ("does / doesn't", "hace / no hace"), ("riding / skating", "andar / patinar (como actividad)"), ("softly / quietly / loudly", "suavemente / en silencio / fuerte"), ("very", "muy"), ("boring", "aburrido")],
    [
        ("Elegir entre hábito y acción en curso", "Completa: «Look! The children ___ in the yard.» Opciones: are playing, play. (Look! indica ahora.)",
         ["Look! indica que pasa en este momento.", "Para ahora se usa am/is/are + -ing.", "The children are playing."], "are playing"),
        ("Responder una pregunta con does", "Tabla: «Leo plays chess every Tuesday.» ¿Responde sí o no a «Does Leo play chess on Mondays?»",
         ["El hábito es los martes, no los lunes.", "La respuesta es negativa.", "No, he doesn't."], "No, he doesn't."),
    ],
    [
        ("Decir «She play tennis».", "Se olvida la -s con she, he e it.", "She plays, he plays, it plays."),
        ("Usar el adjetivo en vez del adverbio: «She sings soft».", "No se distingue cómo es algo de cómo se hace.", "Usa softly para decir cómo canta."),
    ],
    [
        ("«She ___ tennis every week.» Opciones: plays, play.", "plays", "Con she el verbo lleva -s."),
        ("Palabras: now, every day. ¿Cuál indica algo que ocurre en este momento?", "now", "Now significa ahora."),
        ("¿Cuál es un adverbio de modo? a) quietly b) quiet", "a", "Quietly dice cómo se hace algo."),
    ],
    [
        ("¿Cuál es la respuesta corta afirmativa a «Does he cook»? a) Yes, he does b) Yes, he cooks.", "a", "La respuesta corta usa does."),
        ("En «Skating is boring», ¿qué palabra es el sujeto? a) Skating b) boring", "a", "Skating es la actividad de la que se habla."),
        ("«She sings ___.» Opciones: softly, soft.", "softly", "Hace falta un adverbio que modifique al verbo."),
    ],
    [
        ("«My cousin ___ football every Saturday.» Opciones: plays, is playing.", "plays", "Every Saturday indica hábito."),
        ("«They run very ___.» Opciones: fast, fastly.", "fast", "Fast no cambia como adverbio."),
        ("Elige la oración correcta. a) Do you swim every week? b) Does you swim every week?", "a", "Con you se usa do."),
    ],
    [
        ("«Riding is cool» expresa: a) una opinión sobre una actividad b) la hora de una actividad", "a", "Cool es un juicio sobre andar."),
        ("«Do you swim every week?» ¿Cuál es una respuesta negativa correcta? a) No, I don't b) No, I don't swim not.", "a", "La respuesta corta negativa usa don't."),
    ],
    [
        ("Texto: «Mia swims every Monday. Today is Monday, 4:00 pm, and she is in the pool now.» Elige la oración correcta. a) Mia swims every Monday and she is swimming now b) Mia swims every Monday and she swims now.", "a", "Every Monday es hábito; now pide -ing."),
        ("Texto: «Pia plays the violin every Thursday. Today is Friday and she is at the cinema now.» (cinema = cine) ¿Qué responde a «Is Pia playing the violin today?» a) No, she isn't b) Yes, she is.", "a", "Su hábito es los jueves, pero hoy es viernes y está en el cine: ahora no toca el violín."),
    ],
    [("En el afiche de un gimnasio se lee: «Zumba is fun and the class starts every Monday at 6:00. Dancers move quickly and smile!» (class = clase; starts = empieza; move = se mueven) ¿Qué palabra es un adverbio de modo? a) quickly b) Monday", "a", "Quickly dice cómo se mueven.")],
    [
        ("¿Qué tiempo usas para un hábito?", "Presente simple", "Se usa con every day, every week."),
        ("«He ___ playing now.» Opciones: is, does.", "is", "Para ahora se usa is + -ing."),
        ("¿Cómo responderías a «Does she sing?» si sí lo hace?", "Yes, she does.", "La respuesta corta repite does."),
    ],
    task("Escribe en tu hoja una entrevista de ejemplo a un compañero con cuatro preguntas y respuestas cortas: 1) Does he play a sport? 2) Why does he like it? 3) What is he doing now? 4) How does he play? Responde con estos datos de ejemplo: juega básquetbol todas las semanas, le gusta porque es un deporte de equipo, ahora está estudiando y juega muy rápido. Usa every week, because, now y very fast.", "Yes, he does. He plays basketball every week. He likes it because it's a team sport. He is studying now. He plays very fast.", ["usa presente simple y presente continuo correctamente", "justifica con because", "usa un adverbio y very"], ["entrevista de cuatro respuestas en la hoja"], ["olvidar la -s con he", "confundir hábito con ahora"], "Pregunta qué palabra de tiempo le ayudó a elegir el tiempo verbal."),
    "Copia las oraciones de la explicación y subraya las palabras que indican hábito y ahora.",
    "Escribe tres oraciones con riding, skating o swimming como sujeto, usando is cool o is boring.",
)

# ============================================================ clase 3: narrar hechos pasados
lesson(
    OA, 3,
    "Las oraciones y los textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a contar hechos pasados con did/didn't, verbos en pasado y con was/were + -ing, y a unir una acción larga con otra que la interrumpe usando when y while. Sirve para narrar lo que pasó con claridad.",
    ["Conozco el presente simple y el presente continuo.", "Sé que yesterday indica un día pasado."],
    [
        "El pasado simple cuenta hechos terminados: «He won the race yesterday.» Los verbos regulares agregan -ed (played, walked) y los irregulares cambian: win → won, go → went, see → saw, eat → ate, run → ran, make → made. Para negar usa didn't + verbo base: «She didn't win.» Para preguntar usa did: «Did he cook? Yes, he did. No, he didn't.»",
        "El pasado continuo (was/were + -ing) muestra una acción que estaba en curso: «I was playing football.» Se une con when para una acción que la interrumpió: «I was playing football when it started to rain.» Se une con while para dos acciones al mismo tiempo: «While he was cycling, she was listening to music.»",
        "Con while, la acción larga va en pasado continuo: «I saw a shark while I was swimming.» Con when, la acción corta e inesperada va en pasado simple. (En el inglés de todos los días también se oye when con una acción larga; en este cuaderno usamos while para dos acciones simultáneas y when para la que interrumpe.) Para mantener clara la historia, ordena los hechos con first, then y finally, y usa suddenly (de repente) para marcar el momento de una sorpresa.",
    ],
    [("yesterday", "ayer"), ("did / didn't", "hizo / no hizo"), ("was / were + -ing", "estaba(n) haciendo"), ("when", "cuando (acción que interrumpe)"), ("while", "mientras"), ("suddenly", "de repente"), ("won / went / saw / ate / ran", "ganó / fue / vio / comió / corrió")],
    [
        ("Elegir la forma del pasado", "Completa: «Yesterday I ___ pizza.» Opciones: ate, eat.",
         ["Yesterday indica pasado.", "El pasado irregular de eat es ate.", "Yesterday I ate pizza."], "ate"),
        ("Distinguir la acción larga y la que interrumpe", "Oración: «Dani was reading in the park when it started to rain.» ¿Qué acción interrumpió la otra?",
         ["Was reading es la acción en curso.", "It started to rain es la acción que llega de repente.", "La lluvia interrumpió la lectura."], "La lluvia (it started to rain) interrumpió la lectura."),
    ],
    [
        ("Decir «Did she cooked?».", "Se pone el pasado en el verbo después de did.", "Después de did o didn't el verbo va en forma base: Did she cook?"),
        ("Decir «I was playing football while it started to rain».", "Se usa while en todas partes y no se distingue la acción que interrumpe.", "La acción corta que llega de repente va con when: «…when it started to rain». Para dos acciones largas al mismo tiempo usa while."),
    ],
    [
        ("«Yesterday Ana ___ to the market.» Escribe el pasado de go.", "went", "Go es irregular."),
        ("Escribe el pasado de play.", "played", "Es un verbo regular: se agrega -ed."),
        ("«She didn't ___ the race.» Opciones: win, won.", "win", "Después de didn't va el verbo base."),
    ],
    [
        ("Respuesta corta negativa a «Did he cook?» a) No, he didn't b) No, he doesn't.", "a", "La pregunta está en pasado."),
        ("«While he was cycling, she was ___ to music.» Opciones: listening, listen.", "listening", "Después de was va el verbo con -ing."),
        ("Escribe el pasado de run.", "ran", "Run es un verbo irregular."),
    ],
    [
        ("«I was playing football ___ it started to rain.» Opciones: when, while.", "when", "La lluvia interrumpe de repente."),
        ("En «I saw a shark while I was swimming», ¿qué acción es más larga?", "swimming", "Was swimming muestra la acción en curso."),
        ("«Pedro ___ TV when his sister arrived.» Escribe la forma de watch en pasado continuo.", "was watching", "Es una acción en curso interrumpida."),
    ],
    [
        ("Elige la pregunta correcta. a) Did she cook? b) Did she cooked?", "a", "Después de did el verbo va en forma base."),
        ("En «Dani was reading in the park when it started to rain», ¿qué acción dura más? a) reading b) it started to rain", "a", "La lectura estaba en curso."),
    ],
    [
        ("Texto: «Tom was making a sandwich when the phone rang.» ¿Qué ocurrió de repente?", "The phone rang", "Es la acción corta que interrumpe."),
        ("Completa con dos acciones al mismo tiempo: «___ Mom was cooking, I was doing homework.» Opciones: While, After.", "While", "Las dos acciones duraban al mismo tiempo."),
    ],
    [("Escribes un diario: «Yesterday I woke up at seven. I ate cereal. While I was walking to school, I saw a rainbow. Suddenly, a bus honked.» (rainbow = arcoíris; honked = tocó la bocina) ¿Qué ocurrió de repente mientras caminabas? a) El bus tocó la bocina b) Comí cereal", "a", "Suddenly marca la acción inesperada.")],
    [
        ("¿Cómo se niega en pasado?", "Con didn't + verbo base", "Se usa didn't."),
        ("¿Qué tiempo indica una acción en curso en el pasado?", "El pasado continuo", "Usa was o were + -ing."),
        ("Escribe el pasado de see.", "saw", "See es irregular."),
    ],
    task("Lee estas pistas de un día de ejemplo: ayer Camila ganó una carrera (win), mientras corría vio un perro (see), cuando llegó a la meta empezó a llover (start). En tu hoja escribe cuatro oraciones en inglés: una con yesterday, una con while, una con when y una pregunta con Did que alguien podría hacerle a Camila.", "Yesterday Camila won a race. While she was running, she saw a dog. She was crossing the line when it started to rain. Did she win the race?", ["usa verbos en pasado correctos", "usa while y when con sentido", "la pregunta con Did lleva el verbo en forma base"], ["cuatro oraciones en la hoja"], ["usar el pasado después de did", "usar when y while sin pensar"], "Pregunta cuál acción larga fue interrumpida."),
    "Copia los cinco verbos irregulares de la tabla con su pasado.",
    "Cuenta en cinco oraciones qué hiciste ayer usando yesterday, first, then y suddenly.",
)

# ============================================================ clase 4: planes, obligación y posibilidad
lesson(
    OA, 4,
    "Los carteles, reglas y oraciones escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a expresar obligación y prohibición con must y mustn't, a decir lo que quiero con want y a explicar causa y efecto con if. Sirve para escribir reglas, planes y explicaciones.",
    ["Sé el presente simple.", "Conozco palabras como helmet, hot y safe."],
    [
        "Must expresa obligación: «I must practice. You must wear a helmet.» Mustn't expresa prohibición: «You mustn't ride without a helmet. You mustn't run in the corridor.» Después de must y mustn't va el verbo en forma base, sin to ni -s. Se usan en reglas, carteles y consejos de seguridad.",
        "Para decir lo que quieres hacer usa I want to + verbo: «I want to visit a museum. I don't want to go.» Para armar planes usa también la expresión make plans: «We make plans for the weekend.» Para despedirte, see you later o see you soon.",
        "Para explicar causa y efecto usa if + presente simple: «If you heat ice, it melts. If you press the button, the light turns on. If you don't water a plant, it dies.» También puedes decir que algo es demasiado: «It's too dangerous to swim here» (es demasiado peligroso nadar aquí): too + adjetivo + to + verbo.",
    ],
    [("must", "debes (obligación)"), ("mustn't", "no debes (prohibición)"), ("I want to…", "quiero…"), ("if", "si (causa y efecto)"), ("too dangerous to…", "demasiado peligroso para…"), ("make plans", "hacer planes"), ("see you soon", "nos vemos pronto")],
    [
        ("Distinguir obligación y prohibición", "Cartel: «You mustn't touch the stove.» (stove = cocina) ¿Qué indica?",
         ["Mustn't indica prohibición.", "Touch está en forma base.", "No se debe tocar la cocina."], "Una prohibición: no debes tocar la cocina."),
        ("Completar causa y efecto", "Completa: «If you heat ice, it ___.» Opciones: melts, melt.",
         ["La oración con if expresa una causa y su efecto.", "It es singular: lleva -s.", "If you heat ice, it melts."], "melts"),
    ],
    [
        ("Decir «You must to wear a helmet».", "Se agrega to por traducción.", "Después de must va el verbo base: You must wear a helmet."),
        ("Usar mustn't cuando es obligatorio.", "Se confunde obligación con prohibición.", "Must es hacerlo; mustn't es no hacerlo."),
    ],
    [
        ("«You ___ wear a helmet.» (es obligatorio) Opciones: must, mustn't.", "must", "Must indica obligación."),
        ("«You mustn't run in the corridor» significa: a) está prohibido correr b) es obligatorio correr", "a", "Mustn't es prohibición."),
        ("«I want ___ visit a museum.» Opciones: to, for.", "to", "Want va con to y el verbo base."),
    ],
    [
        ("Cartel: «You must wash your hands.» ¿Es obligación o prohibición?", "Obligación", "Must indica que hay que hacerlo."),
        ("«You mustn't ride without a helmet.» ¿Qué debes usar para andar? a) un casco b) unos guantes", "a", "La prohibición es andar sin casco."),
        ("«If you press the doorbell, it ___.» Opciones: rings, ring. (doorbell = timbre)", "rings", "Con it se agrega -s."),
    ],
    [
        ("Reglas: 1) You must arrive at 8:00. 2) You mustn't use phones in class. 3) You must wear the uniform. ¿Cuál es una prohibición? Escribe el número.", "2", "La regla 2 usa mustn't."),
        ("«You ___ cross the street when the light is red.» Opciones: mustn't, must.", "mustn't", "Cruzar con luz roja es peligroso: está prohibido."),
        ("«I don't want ___ go.» Opciones: to, for.", "to", "Want va con to."),
    ],
    [
        ("«It's too dangerous to swim here» significa: a) es demasiado peligroso nadar aquí b) es muy seguro nadar aquí", "a", "Too dangerous indica demasiado riesgo."),
        ("«If you don't water a plant, it dies.» ¿Cuál es el efecto? a) it dies b) you don't water a plant", "a", "El efecto es que la planta muere."),
    ],
    [
        ("Cartel de una piscina: «You must shower first. You mustn't run. You must listen to the lifeguard.» (lifeguard = salvavidas) ¿Cuántas prohibiciones hay?", "1", "Solo you mustn't run es prohibición."),
        ("Completa: «If you press the button, the light ___ on.» Opciones: turns, turn.", "turns", "The light es singular."),
    ],
    [("En el laboratorio del colegio hay una regla: «You must wear safety glasses. You mustn't taste the liquids.» (safety glasses = antiparras; taste = probar) ¿Qué no debes hacer? a) probar los líquidos b) usar antiparras", "a", "You mustn't taste indica la prohibición.")],
    [
        ("¿Cómo se dice «no debes» en inglés?", "You mustn't", "Es la forma negativa de must."),
        ("«If you mix blue and yellow paint, you get ___.» Opciones: green, orange.", "green", "Azul y amarillo dan verde."),
        ("Para despedirte hasta pronto dices: a) See you soon! b) Good morning!", "a", "See you soon es una despedida."),
    ],
    task("Escribe en tu hoja cuatro reglas de seguridad para andar en bicicleta (usa must y mustn't dos veces cada una), una oración de causa y efecto con if (por ejemplo, sobre el frenado) y una oración con I want to sobre tu plan para el fin de semana. (frenar = brake)", "You must wear a helmet. You must stop at red lights. You mustn't ride without brakes. You mustn't use a phone. If you brake, the bike slows down. I want to ride in the park.", ["usa must y mustn't correctamente con verbo base", "la oración con if es lógica", "usa I want to"], ["reglas y dos oraciones en la hoja"], ["escribir to después de must", "confundir obligación y prohibición"], "Pregunta qué cambia si cambia must por mustn't en una regla."),
    "Copia las tres estructuras con if de la explicación y subraya la causa y el efecto.",
    "Escribe tres reglas para un lugar de tu casa usando must y mustn't con dibujos de apoyo.",
)

# ============================================================ clase 5: combinar funciones en un texto con propósito
lesson(
    OA, 5,
    "Los textos y las listas de expresiones escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a combinar cantidades, rutinas, pasado, reglas, conectores y expresiones frecuentes en un texto con propósito. Sirve para escribir con claridad usando el lenguaje que ya aprendí.",
    ["Conozco there is/are, presente simple y pasado, must y if.", "Sé unir ideas con and, but y because."],
    [
        "Para expresarte con claridad usa expresiones frecuentes: have fun o have a good time (pasarlo bien), make a mistake (equivocarse), make plans (hacer planes), make friends (hacer amigos), afraid of flying (con miedo de volar), angry with a person o angry about something (enojado con alguien o por algo), see you later o see you soon. Para ejemplos usa for example; para una sorpresa, suddenly.",
        "Las palabras compuestas (compound words) juntan dos palabras: foot + ball = football, home + work = homework, class + room = classroom, out + door = outdoor (al aire libre). Los sinónimos son palabras con significado parecido: big y large, begin y start, quick y fast. Usarlos evita repetir.",
        "Para unir ideas usa first, second, next y finally; before y after («He felt nervous before the test»); y because para justificar: «Why do you like football? I like football because it's a team sport.» Un texto con propósito mezcla estas piezas: dice qué hay, qué se hace, qué pasó, qué se debe hacer y por qué. Antes de escribir, anota qué función cumple cada oración.",
    ],
    [("have fun", "pasarlo bien"), ("make a mistake", "equivocarse"), ("afraid of", "con miedo de"), ("angry with / about", "enojado con / por"), ("outdoor", "al aire libre"), ("synonym", "sinónimo"), ("for example", "por ejemplo")],
    [
        ("Elegir la expresión correcta", "Completa: «We ___ fun at the party.» Opciones: have, do.",
         ["La expresión es have fun.", "Do no forma este bloque.", "We have fun at the party."], "have"),
        ("Formar una palabra compuesta", "Une foot + ball. ¿Qué palabra queda?",
         ["Se juntan las dos partes sin espacio.", "El resultado es una sola palabra.", "Es el nombre de un deporte."], "football"),
    ],
    [
        ("Decir «do a mistake».", "Se traduce palabra por palabra.", "La expresión es make a mistake."),
        ("Repetir la misma palabra en todo el texto.", "No se usan sinónimos.", "Usa big/large o begin/start para variar."),
    ],
    [
        ("«He made a ___ in the test.» Opciones: mistake, mistaken.", "mistake", "El bloque es make a mistake."),
        ("«See you soon!» se dice cuando: a) te despides b) saludas por primera vez", "a", "Es una despedida."),
        ("«Suddenly» significa: a) de repente b) todos los días", "a", "Suddenly marca algo inesperado."),
    ],
    [
        ("«I'm afraid ___ flying.» Opciones: of, with.", "of", "Afraid va con of."),
        ("«She is angry ___ her brother.» Opciones: with, of.", "with", "Con una persona se usa angry with."),
        ("«Outdoor» significa: a) al aire libre b) dentro de la cocina", "a", "Out + door da outdoor."),
    ],
    [
        ("Elige el sinónimo de «big». a) large b) tiny", "a", "Large significa grande."),
        ("Une home + work y escribe la palabra compuesta.", "homework", "Se unen sin espacio."),
        ("Completa: «Why do you like football? I like football ___ it's a team sport.» Opciones: because, so.", "because", "La respuesta justifica el gusto."),
    ],
    [
        ("Un compañero dice: «Sinónimo de big es tiny.» ¿Tiene razón? Responde sí o no.", "No", "Tiny significa muy pequeño; big y large son parecidos."),
        ("Elige la oración con la expresión correcta. a) We make plans for the weekend b) We do plans for the weekend.", "a", "Make plans es la expresión."),
    ],
    [
        ("Texto: «Last summer we went camping. First, we walked to the lake. Next, we had a picnic. Finally, we went home.» (camping = campamento; picnic = merienda) ¿Cuál es el último suceso? Escribe la acción.", "went home", "Finally cierra la secuencia."),
        ("Texto de un cartel de parque: «You must keep the park clean. If you leave litter, the park gets dirty.» (litter = basura; dirty = sucio) ¿Qué función cumple la segunda oración? a) Causa y efecto b) Cantidad", "a", "If une una causa con su efecto."),
    ],
    [("Tienes que escribir una nota para el curso. La nota dice: «Our outdoor day is on Friday. We must wear hats. If we forget water, we get thirsty. See you soon!» (hats = sombreros; thirsty = con sed) ¿Qué función cumple «See you soon!»? a) Despedida b) Pregunta", "a", "Es una despedida amistosa.")],
    [
        ("En Inglés (oficial): ¿Qué significa «make friends»?", "Hacer amigos", "Es una expresión frecuente."),
        ("¿Qué conector usas para dar un ejemplo?", "For example", "Introduce un ejemplo concreto."),
        ("«Before the test, he felt nervous» muestra: a) orden en el tiempo b) obligación", "a", "Before indica que algo ocurrió antes."),
    ],
    task("Escribe en tu hoja un texto de seis oraciones para invitar a tu curso a un día al aire libre (outdoor). Debe incluir: 1) there is/are con una cantidad, 2) una regla con must o mustn't, 3) una oración de causa y efecto con if, 4) una oración en pasado, 5) una expresión como have fun, 6) un cierre con see you soon. Usa un sinónimo en lugar de repetir una palabra.", "There are forty students in our class. We must wear hats. If we forget water, we get thirsty. Last year we had a great outdoor day. We have fun outdoors. See you soon!", ["incluye las seis funciones", "las estructuras están bien formadas", "evita repetir palabras con un sinónimo"], ["texto de seis oraciones"], ["omitir una de las funciones", "usar must con to"], "Pregunta qué función cumple cada oración."),
    "Copia las expresiones de la explicación y escribe una oración con cada una.",
    "Escribe un pequeño diálogo de cuatro líneas usando afraid of, angry with, make a mistake y see you later.",
)

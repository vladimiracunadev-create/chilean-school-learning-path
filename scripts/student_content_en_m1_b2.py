"""Cuaderno del estudiante, 1.º medio Inglés (propuesta): EN1M OA 12, funciones del lenguaje en textos escritos conectados.

Todos los textos en inglés son originales, breves y ficticios, con pista en español. Los títulos de clase del plan son
genéricos; aquí cada clase trabaja un grupo de funciones del OA: cantidades; describir personas, lugares y ocupaciones;
opiniones y conectores; acciones que comenzaron antes y continúan (present perfect continuous); situaciones hipotéticas
y consejos. Sin audio ni material externo.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA12 = "EN1M OA 12"


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


# ================================================================ clase 1: expresar cantidades, contar y enumerar
lesson(
    OA12, 1,
    "Los datos y textos escritos en cada ejercicio, lápiz y una hoja. Sin materiales especiales.",
    "Aprenderé a expresar cantidades por escrito con many, much, a few, few, a little y little, y a enumerar con first, second y third. Sirve para escribir informes que digan con precisión cuánto hay de algo.",
    ["Sé usar there is y there are.", "Conozco sustantivos contables (books) y no contables (water)."],
    [
        "Las cantidades dependen de si el sustantivo se puede contar. Con sustantivos contables en plural (chairs, books) se usa many, a few y few. Con no contables (sugar, water, time) se usa much, a little y little. En afirmaciones se usa a lot of para ambos tipos: a lot of chairs, a lot of sugar. Many se usa también en afirmaciones: There are many chairs. Much aparece sobre todo en negaciones y preguntas: There isn't much sugar. How many chairs are there? How much sugar is there?",
        "A few y a little significan «unos pocos» y tienen sentido positivo: hay lo suficiente. Few y little, sin a, significan «casi no hay» y tienen sentido negativo: falta algo. Compara: There are a few chairs, so we can start (alcanzan). There are few chairs, so we cannot start (no alcanzan). There is a little sugar, so we can make tea. There is little sugar left, so we need to buy more. Para enumerar se usan los ordinales First, Second, Third y Finally, y la lista con comas: We need chairs, tables and lamps.",
        "Al escribir un informe, el propósito (purpose) es dar datos claros a quien lo lee. Cuenta primero, decide si es contable o no, y elige la palabra de cantidad que calce con el sentido positivo o negativo. Revisa tu texto con estas preguntas: ¿el sustantivo es contable?, ¿quise decir que alcanza o que falta?, ¿enumeré con First, Second y Third en orden?",
    ],
    [("many", "muchos (con contables)"), ("much", "mucho (con no contables)"), ("a few", "unos pocos: lo suficiente (contables)"), ("few", "casi no hay (contables)"), ("a little", "un poco: lo suficiente (no contables)"), ("little", "casi nada (no contables)"), ("left", "que queda"), ("First / Second / Third", "primero / segundo / tercero")],
    [
        ("Elegir la palabra de cantidad", "Informe de ejemplo: «There are ___ students in the gym, and the room is empty. Only 3 came.» ¿Qué palabra completa mejor: few o a few?", ["Students es contable plural.", "El resto del texto dice que el gimnasio está vacío: sentido negativo.", "Con ese sentido se usa few."], "few"),
        ("Distinguir contable y no contable", "Escribe la palabra correcta, little o few: «There is ___ water in the bottle, so we need to refill it.»", ["Water es no contable.", "Con no contables se usa little o a little.", "Hay que rellenarla: sentido negativo, little."], "little"),
    ],
    [
        ("Escribir «There are much chairs».", "Se usa much con un sustantivo contable plural.", "Chairs es contable: There are many chairs."),
        ("Escribir «There is a few sugar».", "Se usa a few con un sustantivo no contable.", "Sugar no se cuenta: There is a little sugar."),
    ],
    [
        ("Clasifica y escribe solo las palabras contables: sugar, apples, music, books.", "apples, books", "Se pueden contar una por una; sugar y music no."),
        ("Completa: «There are ___ students in the gym.» A) many B) much", "A", "Students es contable plural y se usa many."),
        ("Completa: «There is ___ milk in the glass.» A) a little B) a few", "A", "Milk es no contable y a little significa un poco."),
    ],
    [
        ("«There are few chairs.» significa A) que casi no hay sillas B) que hay unas cuantas y alcanzan", "A", "Few, sin a, tiene sentido negativo: faltan sillas."),
        ("Dos informes: «There are a few pencils, so we can start.» y «There is little time, so we cannot start.» ¿En cuál alcanza lo que hay? Responde con la palabra que lo indica.", "a few", "A few tiene sentido positivo y el texto dice so we can start."),
        ("«There is little sugar left.» significa A) queda casi nada de azúcar B) queda bastante azúcar", "A", "Little, sin a, indica que casi no queda."),
    ],
    [
        ("Completa con few o a few: «We have ___ volunteers, but they are enough to clean the yard.»", "a few", "Alcanzan para limpiar el patio, así que el sentido es positivo."),
        ("Completa con a little o little: «There is ___ time left, but we can still finish one more song.»", "a little", "Se puede cantar una canción más, así que el sentido es positivo."),
        ("Completa la pregunta con la palabra de cantidad correcta: «How ___ water is there in the bottle?» A) much B) many", "A", "Water es no contable y con no contables se pregunta How much."),
    ],
    [
        ("Termina con la conclusión que calza: «There are few buses on Sundays, so ___.» A) it is hard to travel by bus B) it is easy to travel by bus", "A", "Few indica que casi no hay buses y por eso es difícil."),
        ("Corrige con un solo cambio, sabiendo que casi no queda azúcar: «There is few sugar in the bowl.»", "There is little sugar in the bowl.", "Sugar es no contable y casi no queda, así que se usa little."),
    ],
    [
        ("Texto: «The library has many books but little tables.» ¿Qué palabra se debe cambiar? Respóndela en inglés.", "little", "Tables es contable y debería llevar few o a few, no little."),
        ("Encuesta ficticia: de 30 estudiantes, 2 eligieron té y 28 eligieron jugo. Completa para el té: «___ students chose tea.» A) Few B) Many", "A", "Solo 2 de 30 es muy poco, sentido negativo: few."),
    ],
    [("En una fiesta de curso ficticia hay 10 sillas, que no alcanzan para 25 estudiantes, y queda 1 cucharada de azúcar, casi nada, para el té. Elige la oración que describe bien la situación. A) There are few chairs and there is little sugar B) There are a few chairs and there is a little sugar.", "A", "No alcanzan las sillas y casi no queda azúcar: ambos son negativos.")],
    [
        ("¿Qué palabra usas con sustantivos no contables y sentido de «casi nada»?", "little", "Little es para no contables con sentido negativo."),
        ("¿Qué palabra de cantidad significa «unos pocos» con sentido positivo y sirve para sustantivos contables?", "a few", "A few indica que hay lo suficiente."),
        ("¿Cuál es el ordinal de «tercero» en inglés?", "Third", "First, second, third."),
    ],
    task("Lee este encargo: escribe un informe de entre cinco y siete oraciones sobre la sala de clases ficticia 1.º F, usando estos datos de ejemplo. Hay 24 sillas para 30 estudiantes (no alcanzan); queda un poco de pegamento en 2 frascos; hay 8 marcadores (alcanzan para los grupos); no hay casi hojas de colores. Usa al menos cuatro palabras de cantidad distintas (many, a few, few, a little, little) y enumera con First, Second y Finally lo que hay que comprar. Revisa si cada sustantivo es contable.", "In 1F, there are few chairs: only 24 for 30 students. There is a little glue left in 2 jars. There are a few markers: 8, enough for the groups. There is little colored paper. First, buy chairs. Second, buy paper. Finally, buy markers.", ["usa al menos cuatro palabras de cantidad distintas", "cada palabra calza con un sustantivo contable o no contable", "enumera con First, Second y Finally"], ["hoja con el informe y la lista de compras"], ["usar much con contables", "confundir few con a few"], "Lee tu informe a una persona de tu casa y pregunta qué cosa falta, a partir de las palabras de cantidad."),
    "Escribe cuatro oraciones con objetos de tu mochila usando a few, few, a little y little.",
    "Escribe dos oraciones iguales con a few y con few y explica en español qué cambia en el sentido.",
)

# ================================================================ clase 2: describir personas, lugares y ocupaciones
lesson(
    OA12, 2,
    "Los textos y listas escritos en cada ejercicio, lápiz y una hoja. Sin materiales especiales.",
    "Aprenderé a describir personas, lugares y ocupaciones con adjetivos precisos, prefijos de significado contrario y expresiones como good at. Sirve para escribir descripciones claras y evitar palabras vagas como nice.",
    ["Conozco adjetivos básicos como big, small y friendly.", "Sé usar to be en presente y pasado."],
    [
        "Para describir personas se usan adjetivos de cualidad. Muchos tienen un contrario formado con un prefijo (prefix): polite → impolite; complete → incomplete; legal → illegal; responsible → irresponsible; respectful → disrespectful. Los prefijos son im-, in-, il-, ir- y dis-, y no se pueden adivinar: hay que aprenderlos con cada palabra. Ejemplos de uso: He is polite. The form was incomplete. It is illegal to cross there.",
        "Los adjetivos terminados en -ing describen lo que causa un efecto: The film is interesting. Los terminados en -ed describen cómo se siente la persona: She is interested in robots (interested in + sustantivo). Para lugares se usan crowded, busy, colorful y cheerful: The market is very busy and colorful. Para ocupaciones se usa a/an + oficio: He is a teacher; she is a pianist; Dani is a waitress. Para habilidades: She is good at drawing (good at + sustantivo o verbo con -ing).",
        "Al escribir, el propósito (purpose) es que el lector se haga una imagen exacta. Cambia nice por un adjetivo preciso, apoya con un dato y elige -ing o -ed según quién siente. Pregúntate: ¿el adjetivo describe a la persona o lo que le causa algo?, ¿existe un contrario con prefijo?, ¿dije a qué se dedica y en qué es buena?",
    ],
    [("impolite", "descortés (contrario de polite)"), ("incomplete", "incompleto"), ("illegal", "ilegal"), ("irresponsible", "irresponsable"), ("disrespectful", "irrespetuoso"), ("interesting / interested", "interesante (lo que causa) / interesado (quien siente)"), ("crowded / busy", "lleno de gente / con mucha actividad"), ("good at", "bueno para (una habilidad)")],
    [
        ("Elegir -ing o -ed", "Completa con interesting o interested: «The documentary about bees is very ___.»", ["The documentary causes interest: it is the cause.", "Lo que causa el efecto lleva -ing.", "Queda interesting."], "interesting"),
        ("Formar el contrario", "Escribe el contrario de legal para decir que cruzar con el semáforo en rojo no está permitido: «It is ___ to cross on a red light.»", ["El contrario de legal lleva el prefijo il-.", "Se escribe illegal.", "Queda: It is illegal to cross on a red light."], "illegal"),
    ],
    [
        ("Escribir «unpolite» o «unresponsible».", "Se supone que el prefijo un- sirve para todas las palabras.", "Aprende cada contrario: impolite e irresponsible."),
        ("Escribir «I am interesting in music».", "Se usa -ing para decir cómo se siente la persona.", "Se dice I am interested in music."),
    ],
    [
        ("El contrario de polite es A) impolite B) unpolite", "A", "Se forma con im-: impolite."),
        ("Completa: «Ana is good ___ drawing.» A) at B) in", "A", "La expresión es good at + sustantivo o verbo con -ing."),
        ("«Daniela works in a café and takes the orders. She is a ___.» A) waitress B) pianist", "A", "Una persona que atiende mesas en un café es una waitress."),
    ],
    [
        ("«The market is very crowded.» significa A) hay mucha gente B) está vacío", "A", "Crowded describe un lugar con mucha gente."),
        ("¿Cuál es el contrario de responsible? A) irresponsible B) disresponsible", "A", "Se forma con el prefijo ir-: irresponsible."),
        ("Tomás never brings his homework and loses his keys. ¿Qué adjetivo lo describe mejor? A) irresponsible B) impolite", "A", "Olvidar tareas y llaves es no ser responsible; no se trata de falta de cortesía."),
    ],
    [
        ("Completa con interesting o interested: «Mia is ___ in robotics; she reads about it every day.»", "interested", "Se describe cómo se siente Mia y se usa interested in."),
        ("Completa con el contrario de complete: «The form is ___: the date is missing.»", "incomplete", "Falta la fecha, así que el contrario con in- es incomplete."),
        ("Un estudiante grita a su profesora en la sala. ¿Qué adjetivo describe mejor su conducta? A) respectful B) disrespectful", "B", "Gritar a una profesora es irrespetuoso, disrespectful."),
    ],
    [
        ("Texto: «The beach is quiet. There are few people.» ¿Qué descripción no calza con el texto? A) crowded B) quiet", "A", "Con pocas personas la playa no puede ser crowded."),
        ("Pablo plays the piano in concerts. Julia sells sandwiches in a school kiosk. Responde: ¿quién es pianist?", "Pablo", "El oficio de quien toca el piano es pianist."),
    ],
    [
        ("Corrige con un cambio: «The lesson was very interested, so everyone listened.»", "The lesson was very interesting, so everyone listened.", "Se describe lo que causa interés, la lección: interesting."),
        ("Elige la oración más precisa para una exposición: A) The presentation was nice B) The presentation was complete and respectful of other opinions.", "B", "Da dos cualidades concretas en vez de un adjetivo vago."),
    ],
    [("Perfil ficticio para el diario del colegio: Laura trabaja de profesora, es buena para dibujar y disfruta de los museos. ¿Qué oración lo describe mejor? A) Laura is a teacher, she is good at drawing and she is interested in museums B) Laura is a teacher, she is good in drawing and she is interesting in museums.", "A", "Usa good at e interested in, que son las formas correctas.")],
    [
        ("¿Qué prefijo forma el contrario de legal?", "il-", "Se escribe illegal."),
        ("¿Cuál se usa para quien siente: interested o interesting?", "interested", "El -ed describe a la persona."),
        ("¿Qué preposición va con good?", "at", "Es good at."),
    ],
    task("Lee este encargo: escribe en una hoja una descripción de seis oraciones de una persona ficticia, Marta, y de su lugar de trabajo. Datos de ejemplo: Marta es panadera, es buena para hacer pan, está interesada en la cocina, su panadería es muy concurrida y colorida, y siempre es respetuosa con los clientes. Usa al menos un prefijo de contrario (por ejemplo impolite) para decir qué nunca hace, good at, interested in y crowded o colorful. Revisa -ing y -ed.", "Marta is a baker. She is good at making bread and she is interested in cooking. Her bakery is very busy and colorful. She is never impolite to customers. She is always respectful and responsible. Everyone says her place is interesting.", ["usa good at e interested in correctamente", "usa un adjetivo de lugar y un contrario con prefijo", "distingue -ing y -ed"], ["hoja con las seis oraciones y los adjetivos subrayados"], ["usar un- en vez de im- o ir-", "confundir interesting con interested"], "Lee la descripción a una persona de tu casa y pídele que adivine el oficio sin que lo digas."),
    "Escribe cuatro contrarios con prefijo: polite, legal, responsible y complete.",
    "Describe un lugar de tu barrio con tres adjetivos precisos que no sean nice ni good.",
)

# ================================================================ clase 3: opiniones y conectores
lesson(
    OA12, 3,
    "Los textos y datos escritos en cada ejercicio, lápiz y una hoja. Sin materiales especiales.",
    "Aprenderé a expresar mi opinión y la de otros con In my opinion y According to, y a unir ideas con although, so that, both … and y And last. Sirve para escribir textos conectados en lugar de oraciones sueltas.",
    ["Sé usar because y but.", "Conozco I think y I like."],
    [
        "Para dar tu propia opinión (opinion) por escrito se usa In my opinion, seguido de una coma: In my opinion, the park is clean. Para referirte a lo que dicen otros se usa According to + fuente, con coma: According to the teacher, the test is on Friday. No se dice «according to me» ni «according to my opinion». Una opinión es un juicio personal (boring, good); un hecho (fact) se puede comprobar (the library closes at 6 p.m.).",
        "Los conectores (connectors) unen ideas. Although (aunque) introduce un contraste y no se combina con but en la misma oración: Although it is cheap, I am not sure. So that (para que) expresa un propósito: Come early so that we can talk. Both … and (tanto … como) une dos personas o cosas con un verbo en plural: Both Luis and Tomás are my neighbors. Para cerrar una lista se usa And last después de First y Second.",
        "Antes de escribir, define el propósito (purpose) del párrafo y a quién va dirigido. Luego revisa: ¿marqué qué es opinión y qué es hecho?, ¿cité la fuente con According to?, ¿cada conector tiene sentido y la puntuación correcta? Una coma separa la parte con Although del resto: Although it was cold, we played outside.",
    ],
    [("In my opinion", "en mi opinión"), ("According to", "según (una fuente)"), ("although", "aunque"), ("so that", "para que"), ("both … and", "tanto … como"), ("And last", "y por último"), ("fact", "hecho que se puede comprobar"), ("connector", "conector: palabra que une ideas")],
    [
        ("Distinguir opinión y hecho", "Dos oraciones: «The gym opens at 8 a.m.» y «The gym is too noisy.» ¿Cuál es una opinión?", ["Un hecho se puede comprobar con un horario.", "Too noisy depende de quien escucha.", "La opinión es la segunda."], "The gym is too noisy."),
        ("Unir con although", "Une las ideas con Although: «The bag is cheap» y «the bag is strong».", ["Although va al comienzo y la primera idea sigue.", "Se separan con coma.", "Queda: Although the bag is cheap, it is strong."], "Although the bag is cheap, it is strong."),
    ],
    [
        ("Escribir «According to me, the park is clean».", "Se traduce literal «según yo».", "Para tu opinión usa In my opinion, the park is clean."),
        ("Escribir «Although it is cheap, but I am not sure».", "Se usa although y but juntos en la misma oración.", "Elige uno: Although it is cheap, I am not sure."),
    ],
    [
        ("«In my opinion, the bus is slow.» expresa A) una opinión B) un hecho comprobable", "A", "In my opinion indica un juicio personal."),
        ("«According to the teacher, the test is on Friday.» ¿De quién viene la información?", "De la profesora", "La fuente que nombra According to the teacher es la profesora."),
        ("Although significa A) aunque B) porque", "A", "Although introduce un contraste, no una causa."),
    ],
    [
        ("«Come early so that we can talk.» ¿Qué expresa so that? A) un propósito B) un contraste", "A", "So that indica para qué se llega temprano."),
        ("«Both Luis and Tomás are my neighbors.» ¿Cuántas personas son vecinos?", "2", "Both … and une a dos personas."),
        ("«According to the poster, the museum opens at 9 a.m.» ¿Quién da el dato del horario? A) the poster B) the writer", "A", "La fuente nombrada después de According to es el afiche."),
    ],
    [
        ("Completa: «___ the jacket is old, it is warm.»", "Although", "Une un contraste y cabe al comienzo de la oración."),
        ("Completa: «Study today ___ you can rest tomorrow.»", "so that", "Expresa el propósito de estudiar hoy."),
        ("Completa: «___ Ana and Mia are in the choir.»", "Both", "Both … and une a las dos."),
    ],
    [
        ("Elige la oración bien unida. A) Although the film is long, I enjoyed it B) Although the film is long, but I enjoyed it.", "A", "Although no se usa junto con but en la misma oración."),
        ("¿Cuál es la opinión? A) The library closes at 6 p.m. B) The library is too quiet.", "B", "Too quiet es un juicio personal; la hora de cierre se puede comprobar."),
    ],
    [
        ("Completa con la expresión de esta clase para cerrar una lista: «First, uniforms save time. Second, they are cheap. And ___, they look neat.»", "last", "And last cierra la enumeración después de First y Second."),
        ("Dos versiones: A) According to my opinion, the park is clean B) In my opinion, the park is clean. ¿Cuál es correcta?", "B", "No se dice according to my opinion; la forma natural es In my opinion."),
    ],
    [("Un curso ficticio encuesta a 30 estudiantes sobre dónde ir de paseo: 20 prefieren el museo y 10 el parque. ¿Qué oración usa bien la fuente? A) According to the survey, 20 of 30 students prefer the museum B) According to me, 20 of 30 students prefer the museum.", "A", "La fuente es la encuesta, que respalda el dato, no una opinión personal.")],
    [
        ("¿Cómo se dice «en mi opinión» en inglés?", "In my opinion", "Es la fórmula para dar tu propio juicio."),
        ("¿Qué conector significa «para que»?", "so that", "Expresa el propósito de una acción."),
        ("¿Qué se usa para citar una fuente?", "According to", "Seguido de la fuente y una coma."),
    ],
    task("Lee este encargo: escribe en una hoja un párrafo de siete oraciones sobre si tu colegio debería abrir la biblioteca los sábados. Datos de ejemplo: según una encuesta ficticia, 18 de 25 estudiantes dicen que sí; el costo es bajo; algunas personas dicen que es mucho trabajo. Incluye In my opinion, According to, Although, so that y una lista con First, Second y And last. Revisa la puntuación de cada conector.", "In my opinion, the library should open on Saturdays. According to a survey, 18 of 25 students say yes. Although some people say it is a lot of work, the cost is low. The library should open so that students can study. First, it is useful. Second, it is quiet. And last, it is cheap.", ["usa In my opinion y According to correctamente", "usa Although y so that con sentido y sin but", "lista con First, Second y And last"], ["hoja con el párrafo y los conectores subrayados"], ["mezclar although con but", "usar according to me"], "Lee tu párrafo a una persona de tu casa y pregunta cuál es hecho y cuál es opinión."),
    "Escribe una oración con In my opinion y otra con According to sobre el mismo tema.",
    "Escribe dos oraciones con both … and sobre amigos o compañeros que comparten una habilidad.",
)

# ================================================================ clase 4: present perfect continuous
lesson(
    OA12, 4,
    "Los datos y textos escritos en cada ejercicio, lápiz y una hoja. Sin materiales especiales.",
    "Aprenderé a escribir acciones que empezaron en el pasado y continúan o acaban de terminar con have/has been + verbo con -ing. Sirve para contar por cuánto tiempo haces algo, como entrenar o estudiar.",
    ["Sé conjugar el presente continuo (I am playing).", "Conozco los años y los meses en inglés."],
    [
        "El presente perfecto continuo (present perfect continuous) se forma con have/has + been + verbo con -ing: We have been training. She has been working. Se usa have con I, you, we y they; has con he, she e it. Sirve para acciones que empezaron en el pasado y aún continúan, o que acaban de terminar y se notan en el presente. Ejemplos: We have been training for 3 months (y seguimos). Her hands are dirty because she has been painting (acaba de terminar).",
        "Para decir cuánto tiempo se usa for + una duración (for two hours, for 3 months). Para decir desde cuándo se usa since + un punto del pasado (since March, since 8 a.m., since 2022). La pregunta es How long have you been learning English? La forma negativa es haven't/hasn't been. Algunos verbos no suelen usarse en esta forma, como know o have (tener), pero aquí trabajamos con verbos de acción: study, train, play, wait, work, paint.",
        "Para escribir bien: 1) elige have o has según el sujeto; 2) agrega been; 3) pon el verbo con -ing; 4) añade for o since según lo que sabes (una duración o un punto de partida). Si el resultado se ve ahora (zapatos con barro), también sirve esta forma, y no hace falta decir el tiempo.",
    ],
    [("have/has been + -ing", "forma del presente perfecto continuo"), ("for", "durante (una duración: for two hours)"), ("since", "desde (un punto de partida: since March)"), ("How long?", "¿cuánto tiempo?"), ("just", "recién, hace poco"), ("train", "entrenar"), ("wait", "esperar"), ("all day", "todo el día")],
    [
        ("Escoger have o has", "Completa con have o has: «Our neighbors ___ been painting the fence since 9 a.m.»", ["Neighbours es plural, como they.", "Con plural se usa have.", "Queda have been painting."], "have"),
        ("Escoger for o since", "Completa con for o since: «Nico has been studying ___ 6 p.m.»", ["6 p.m. es un punto de partida.", "Un punto de partida se marca con since.", "Queda since 6 p.m."], "since"),
    ],
    [
        ("Escribir «She has working all day».", "Se omite been.", "Se escribe has been working."),
        ("Escribir «We have been training since 3 months».", "Se usa since con una duración.", "Con una duración se usa for: for 3 months."),
    ],
    [
        ("Completa: «She ___ been working all day.» A) has B) have", "A", "She es tercera persona singular y usa has."),
        ("En «for 3 months», ¿qué indica for? A) una duración B) un punto de partida", "A", "Three months es cuánto tiempo."),
        ("Completa con el verbo en -ing: «They have been ___ since Monday.» (train)", "training", "Después de been va el verbo con -ing."),
    ],
    [
        ("¿Qué frase es el punto de partida del pasado? A) since 2022 B) for 2022", "A", "Un año concreto se marca con since."),
        ("Completa: «My brothers ___ been playing football.» A) have B) has", "A", "My brothers equivale a they y usa have."),
        ("«I have been waiting for 20 minutes.» dice que A) empecé a esperar hace 20 minutos y la espera sigue o acaba de terminar B) esperé 20 minutos el año pasado", "A", "La forma indica que la acción empezó antes y continúa."),
    ],
    [
        ("Completa con for o since: «We have been training ___ September.»", "since", "September es un punto de partida."),
        ("Completa con for o since: «Mia has been studying ___ two hours.»", "for", "Two hours es una duración."),
        ("Escribe la oración completa con los datos Paula / paint / all morning, en presente perfecto continuo.", "Paula has been painting all morning.", "Paula usa has, más been y paint con -ing."),
    ],
    [
        ("Los zapatos de Tomás están embarrados. Texto: «He has been playing football.» ¿Qué indica? A) que acaba de terminar de jugar B) que jugó hace varios meses", "A", "El resultado se ve ahora, por eso se usa esta forma."),
        ("¿Cuál usa mal la palabra de tiempo? A) We have been running for 20 minutes B) We have been running since 20 minutes.", "B", "Twenty minutes es una duración y requiere for."),
    ],
    [
        arith("Empezamos a entrenar el 1 de septiembre. Hoy es 1 de diciembre. Completa el número de meses: «We have been training for ___ months.» (diciembre es el mes 12 y septiembre el 9)", "12-9", "Se resta el mes de inicio al mes actual."),
        ("Completa la pregunta: «How long ___ you ___ learning English?»", "have, been", "Con you se usa have y luego been."),
    ],
    [("La banda de un colegio ficticio empezó a ensayar en marzo y hoy sigue ensayando. ¿Qué oración lo cuenta bien? A) Our band has been practicing since March B) Our band is practicing for March.", "A", "March es el punto de partida y la acción continúa.")],
    [
        ("¿Cómo se forma el presente perfecto continuo?", "have/has + been + verbo con -ing", "Esa es la estructura completa."),
        ("¿Qué se usa con una duración: for o since?", "for", "For acompaña a cuánto tiempo."),
        ("¿Qué se usa con un punto de partida: for o since?", "since", "Since marca desde cuándo."),
    ],
    task("Lee este encargo: escribe en una hoja un párrafo de seis oraciones sobre un club ficticio de ciclismo del colegio. Datos de ejemplo: los integrantes entrenan desde abril; la capitana, Laura, practica hace dos años; hoy llevan una hora pedaleando y están cansados; esperan la lluvia desde las 3 p.m. Usa al menos tres veces have/has been + -ing, for y since, y una oración en que se vea un resultado.", "The cycling club has been training since April. Laura has been practicing for two years. We have been riding for an hour, so we are tired. We have been waiting for the rain since 3 p.m. They have been learning the route. I have been practicing too.", ["usa have/has been + -ing con el sujeto correcto", "usa for con duración y since con un punto de partida", "incluye una oración con resultado visible"], ["hoja con el párrafo y las frases de tiempo subrayadas"], ["omitir been", "usar since con una duración"], "Cuenta a una persona de tu casa algo que llevas haciendo desde hace tiempo, usando for y since."),
    "Escribe tres oraciones sobre algo que haces desde hace tiempo con for y since.",
    "Escribe tres preguntas con How long have you been … para entrevistar a un compañero.",
)

# ================================================================ clase 5: situaciones hipotéticas y consejos
lesson(
    OA12, 5,
    "Los textos y casos escritos en cada ejercicio, lápiz y una hoja. Sin materiales especiales.",
    "Aprenderé a escribir situaciones imaginarias con If + pasado simple, would + verbo, y a dar consejos con If I were you, I would. Sirve para sugerir ideas con respeto y para imaginar qué pasaría en otra situación.",
    ["Sé usar el pasado simple.", "Conozco should y can para consejos."],
    [
        "Las situaciones hipotéticas (hypothetical) hablan de algo irreal o poco probable en el presente. La estructura es If + pasado simple, would + verbo en forma base: If she studied more, she would pass the test (pero no estudia más). Aunque if va con pasado simple, el tiempo es presente o futuro imaginario. Con el verbo be se usa were para todas las personas: If I were you, If he were here.",
        "El mismo molde sirve para dar consejos (advice): If I were you, I would talk to the teacher. Significa «yo, en tu lugar, hablaría con la profesora». No se dice If I would be you ni If I will study. Para algo posible, no imaginario, se usa will: If it rains tomorrow, we will stay home. Para cortesía, would suaviza una orden: I would apologize (yo pediría disculpas).",
        "Al escribir consejos, el propósito (purpose) es ayudar sin mandar. Revisa: ¿es una situación irreal o un plan posible?, ¿usé If + pasado y would + verbo?, ¿empleé were con I? Un consejo es más útil si propone una acción concreta: If I were you, I would plan my time with a list.",
    ],
    [("If I were you", "si yo fuera tú (para dar consejo)"), ("would + verb", "forma del condicional para lo imaginario"), ("hypothetical", "hipotético: imaginario"), ("advice", "consejo"), ("were", "forma de be con todas las personas en lo imaginario"), ("apologize", "pedir disculpas"), ("plan", "planificar"), ("pass", "aprobar")],
    [
        ("Completar un consejo", "Completa: «If I ___ you, I would study today.» (opciones: were / was)", ["En lo hipotético con I se usa were.", "Es un consejo con If I were you.", "Queda were."], "were"),
        ("Formar una oración hipotética", "Completa: «If they trained every day, they ___ win the match.»", ["Después de If + pasado simple va would + verbo.", "Falta would.", "Queda would win."], "would"),
    ],
    [
        ("Escribir «If I would be you, I would call her».", "Se usa would en la parte con if.", "La parte con if va en pasado: If I were you, I would call her."),
        ("Escribir «If I will win, I would share it».", "Se mezcla el tipo posible con el hipotético.", "Elige un molde: If I won, I would share it."),
    ],
    [
        ("«If I were you, I would talk to the teacher.» es A) un consejo B) un hecho del pasado", "A", "If I were you, I would… es la fórmula para dar un consejo."),
        ("Completa el consejo: «If I ___ you, I would ask for help.» A) were B) will be", "A", "La forma correcta de be en lo hipotético es were."),
        ("Completa con would + verbo: «If Pedro practiced more, he ___ improve.»", "would", "Después de la parte con pasado va would."),
    ],
    [
        ("«If I had a car, I would drive to school.» ¿Qué significa? A) No tengo un auto B) Tengo un auto", "A", "La estructura habla de una situación imaginaria, que no es real."),
        ("¿Qué estructura es correcta? A) If she studied more, she would pass B) If she will study more, she would pass.", "A", "If va con pasado simple y la otra parte con would."),
        ("Un amigo duerme poco cada noche. ¿Qué consejo está bien escrito y ayuda? A) If I were you, I would go to bed earlier B) If I were you, I will go to bed earlier.", "A", "Usa would después de If I were you y propone dormir más."),
    ],
    [
        ("Completa con el verbo en pasado: «If I ___ a free day, I would visit the museum.» (have)", "had", "En la parte con if va el pasado simple."),
        ("Completa con el verbo en pasado: «If she ___ English, she would meet more people.» (speak)", "spoke", "Speak es irregular y su pasado es spoke."),
        ("Tu amigo siempre olvida su cuaderno. Elige el consejo que completa la frase: «If I were you, I ___.» A) would make a checklist B) will make a checklist", "A", "Después de If I were you se usa would + verbo."),
    ],
    [
        ("¿Cuál es la oración imaginaria? A) If I won a prize, I would share it B) If I win the prize, I will share it.", "A", "La primera usa If + pasado y would y trata una situación improbable."),
        ("Corrige: «If we would have more time, we would visit the park.»", "If we had more time, we would visit the park.", "En la parte con if va el pasado simple, no would."),
    ],
    [
        ("Texto: «If Ana lived near the school, she would arrive on time.» ¿Qué dice la oración sobre la realidad? A) Ana no vive cerca del colegio B) Ana vive cerca del colegio.", "A", "La oración imaginaria revela lo contrario de la realidad."),
        ("Ordena las palabras y escribe el consejo: were / I / would / If / you, / I / apologize", "If I were you, I would apologize.", "La estructura es If + sujeto + were + you, I would + verbo."),
    ],
    [("Una columna de consejos ficticia: Mateo no termina las tareas a tiempo porque juega videojuegos hasta tarde. ¿Qué consejo es adecuado? A) If I were you, I would plan my time and play only after finishing B) If I were you, I would do the homework tomorrow.", "A", "Propone una acción concreta y útil, expresada con respeto.")],
    [
        ("¿Qué forma de be se usa en If I ___ you?", "were", "Se usa were en lo hipotético con I."),
        ("¿Con qué se completa la segunda parte: would + ?", "Un verbo en forma base", "Would plan, would call."),
        ("¿Para qué sirve If I were you, I would…?", "Dar un consejo", "Es la fórmula del consejo."),
    ],
    task("Lee este encargo: responde en una hoja con cuatro consejos escritos a Lía, una estudiante ficticia. Datos de ejemplo: le cuesta madrugar, olvida sus útiles, tiene vergüenza de hablar inglés en clase, y está nerviosa antes de una prueba. Usa If I were you, I would… en dos consejos, y If + pasado simple, would + verbo en otros dos. Escribe también una oración hipotética sobre qué haría Lía con un día libre.", "If I were you, I would go to bed earlier. If I were you, I would make a checklist. If you practiced in a small group, you would feel braver. If you studied a little every day, you would feel calm. If Lía had a free day, she would go to the park.", ["usa If I were you, I would en dos consejos", "usa If + pasado simple y would en otros dos", "los consejos son concretos y respetuosos"], ["hoja con los cuatro consejos y la oración hipotética"], ["usar would en la parte con if", "mezclar will con el molde hipotético"], "Dale uno de tus consejos a una persona de tu casa y pregunta si lo encontró útil."),
    "Escribe tres consejos para un compañero que se aburre en clases usando If I were you, I would.",
    "Escribe cuatro oraciones sobre qué harías si tuvieras una semana libre, usando If + pasado y would.",
)

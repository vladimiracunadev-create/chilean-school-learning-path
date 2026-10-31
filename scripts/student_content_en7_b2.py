"""Cuaderno del estudiante, 7.º básico Inglés (propuesta): EN07 OA 12, funciones comunicativas en textos escritos.

Los textos en inglés son originales, breves y llevan pista en español. Los títulos de clase del plan son genéricos; el OA nombra
muchas funciones, así que se reparten así: 1) cantidades, enumerar y unir ideas; 2) expresiones, sinónimos y palabras compuestas;
3) describir objetos y señalar tiempo, grado y modo; 4) preguntas (Does/Did) y acciones en pasado continuo; 5) causa, efecto y condiciones.
"""
from __future__ import annotations

from student_content_en7_b import E, lesson
from student_content_ma01_b import task
from student_lessons import arith, ex

OA12 = "EN07 OA 12"

# ================================================================ OA 12 clase 1: cantidades, enumerar y unir ideas
lesson(
    OA12, 1,
    "Las oraciones y listas escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a expresar cantidades, a contar y enumerar, y a unir ideas en un texto escrito. Sirve para que mis textos digan cuánto hay y en qué orden ocurren las cosas.",
    ["Conozco los números y palabras como many y people.", "Sé que algunas palabras se pueden contar (books) y otras no (water)."],
    [
        "Para decir cantidades hay palabras distintas. A lot of (mucho/a/os/as) sirve con plurales y con cosas que no se cuentan: a lot of people, a lot of water. Several significa varios: several people. All the significa todos los: all the students. A few (unos pocos) va con plurales: a few apples. A little (un poco) va con cosas que no se cuentan: a little milk. Many se usa con plurales y much con no contables, sobre todo en preguntas y negaciones: How many books? There isn't much water.",
        "Para contar y enumerar en un texto se usan palabras de orden: first (primero), second (segundo), third (tercero), next (luego, a continuación) y finally (finalmente). Sirven para explicar pasos o para listar ideas: «First, put bread on a plate. Next, add cheese. Finally, close the sandwich».",
        "Para unir ideas también se usa too + adjetivo, que significa demasiado y muestra un problema o un límite. «It's too dangerous to visit» quiere decir que es demasiado peligroso para visitarlo. Fíjate en el orden: too va antes del adjetivo y después viene to + verbo. Too no es lo mismo que very: very solo intensifica, too indica que es más de lo conveniente.",
    ],
    [("a lot of", "mucho/a/os/as"), ("several", "varios/as"), ("all the", "todos/as los/las"), ("a few / a little", "unos pocos / un poco"), ("many / much", "muchos (contables) / mucho (no contables)"), ("first / next / finally", "primero / luego / finalmente"), ("too", "demasiado")],
    [
        ("Elegir many o much", "Completa: «How ___ water do we need for the plants?» Opciones: many / much.", ["Water es una cosa que no se cuenta.", "Con no contables se usa much.", "La palabra es much."], "much"),
        ("Ordenar los pasos", "Ordena los pasos para preparar un jugo. a) Finally, drink it. b) First, put fruit in a glass. c) Next, add cold water. Escribe las letras en orden.", ["Busca la palabra que marca el comienzo: First.", "Next va después y Finally cierra.", "El orden es b, c, a."], "b, c, a"),
    ],
    [
        ("Escribir «much people».", "Se traduce «mucha gente» palabra por palabra.", "People es plural y se cuenta: usa many people o a lot of people."),
        ("Confundir too con very.", "Se piensa que significan lo mismo.", "Too indica que algo es más de lo conveniente: too hot to eat."),
    ],
    [
        ("¿Qué significa «several»?", "Varios", "Se usa con plurales para una cantidad no muy grande."),
        ("Completa: «I have a few ___.» Opciones: friends / milk.", "friends", "A few (unos pocos) va con plurales contables; milk no se cuenta."),
        ("Completa: «There are ___ people in the park.» Opciones: a lot of / a little.", "a lot of", "People es plural y a little solo va con no contables."),
    ],
    [
        ("Completa: «I need a little ___.» Opciones: water / apples.", "water", "A little se usa con cosas que no se cuentan."),
        ("Completa: «How ___ books do you have?» Opciones: many / much.", "many", "Books se cuenta, así que lleva many."),
        ("¿Cuál dice lo mismo que «All the students are here»? a) Every student is here. b) Some students are here.", "a", "All the students significa todos los estudiantes."),
    ],
    [
        ("Ordena las palabras para formar una oración: of / There / a lot / are / birds.", "There are a lot of birds.", "Va primero There are, luego a lot of y al final el sustantivo."),
        ("Completa: «There are three steps. ___, wash your hands. Second, open the box. Finally, eat.» Opciones: First / Next.", "First", "Después de first sigue second."),
        arith("Un curso tiene 30 estudiantes. Seis estudiantes están en la biblioteca. ¿Cuántos estudiantes siguen en la sala?", "30 - 6", "Se restan los que se fueron al total del curso.", " estudiantes"),
    ],
    [
        ("«The soup is too hot to eat.» ¿Qué conviene hacer? a) Eat it now. b) Wait a little before eating.", "b", "Too hot to eat significa que está demasiado caliente para comerla."),
        ("Una compañera escribió «There are much people in the shop». ¿Qué expresión la corrige? Opciones: a lot of / a little.", "a lot of", "People es plural y a lot of funciona con plurales."),
    ],
    [
        ("Ordena los pasos. a) Finally, close the sandwich. b) First, put bread on a plate. c) Next, add cheese. Escribe las letras en orden.", "b, c, a", "Primero se pone el pan, luego el queso y al final se cierra."),
        ("«The mountain path is too dangerous to climb in winter.» (path = sendero) ¿Qué recomienda la oración sobre subir en invierno? a) Es mala idea. b) Es una gran idea.", "a", "Too dangerous to climb indica que es demasiado peligroso."),
    ],
    [("Escribes un aviso para una excursión del curso. Hay 40 estudiantes y 4 profesores. ¿Cuál oración dice bien que hay muchas personas? a) There are a lot of people on the trip. b) There is a lot of people on the trip.", "a", "People es plural, así que se usa There are.")],
    [
        ("¿Con qué tipo de palabras se usa «many»?", "Con plurales contables", "Se usa con cosas que se cuentan, como books."),
        ("¿Qué significa «too» antes de un adjetivo?", "Demasiado", "Muestra un límite o un problema."),
        ("¿Qué palabra cierra una lista de pasos?", "Finally", "Marca el último paso."),
    ],
    task("Lee este encargo: escribe en tu hoja cinco oraciones sobre tu colegio o tu barrio. Usa a lot of, several, all the, a few o a little (cada una en una oración) y agrega un párrafo de tres pasos con first, next y finally para explicar cómo llegas al colegio. Revisa que people lleve many o a lot of, no much.", "There are a lot of trees near my school. Several students walk to school. All the classrooms are on the first floor. First, I leave home. Next, I walk to the corner. Finally, I arrive at school.", ["usa al menos tres expresiones de cantidad bien elegidas", "usa first, next y finally en orden", "concuerda there is o there are con el sustantivo"], ["hoja con cinco oraciones y un párrafo de tres pasos"], ["much con plurales", "ordenar mal los pasos"], "Pide que cambie una cantidad por otra y explique cómo cambia el sentido."),
    "Copia las siete palabras importantes de la clase y escribe una oración con cada una.",
    "Escribe una instrucción de cuatro pasos para una receta fría y usa too en una advertencia, como it is too hot to eat.",
)

# ================================================================ OA 12 clase 2: expresiones, sinónimos y palabras compuestas
lesson(
    OA12, 2,
    "Las oraciones y listas de palabras escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé expresiones comunes, sinónimos y palabras compuestas para escribir con más claridad. Sirve para decir lo mismo de varias formas y no repetir siempre las mismas palabras.",
    ["Conozco verbos como make, have y give.", "Sé que algunas palabras se escriben juntas, como homework."],
    [
        "Una colocación es un grupo de palabras que van juntas: make a mistake (cometer un error), make plans (hacer planes), make friends (hacer amigos), have fun o have a good time (pasarlo bien), give advice on (dar consejos sobre). Con adjetivos se usan preposiciones fijas: afraid of flying (miedo a volar), angry about + cosa (enojado por algo) y angry with + persona (enojado con alguien).",
        "Más expresiones útiles para escribir: I want… (quiero…), I don't want to… (no quiero…), See you later (hasta luego, el mismo día) y See you soon (nos vemos pronto). Suddenly significa de repente y se usa al comienzo de una oración, seguida de coma: Suddenly, the lights went out.",
        "Un sinónimo es una palabra con significado parecido: big–large, quick–fast, glad–happy, begin–start. Sirve para no repetir. Una palabra compuesta une dos palabras para formar una nueva: out + door = outdoor (al aire libre, lo contrario de indoor, bajo techo), home + work = homework, note + book = notebook, class + room = classroom.",
    ],
    [("make a mistake", "cometer un error"), ("make plans / friends", "hacer planes / amigos"), ("have fun", "pasarlo bien"), ("give advice on", "dar consejos sobre"), ("afraid of", "con miedo a"), ("angry about / with", "enojado por algo / con alguien"), ("suddenly", "de repente"), ("synonym", "sinónimo"), ("outdoor / indoor", "al aire libre / bajo techo"), ("compound word", "palabra compuesta")],
    [
        ("Elegir la preposición", "Completa: «Rosa is afraid ___ dogs.» Opciones: of / about.", ["Con afraid se usa una preposición fija.", "La expresión es afraid of.", "Queda Rosa is afraid of dogs."], "of"),
        ("Formar una palabra compuesta", "Une las palabras sun + shine. ¿Qué palabra compuesta se forma, con el significado luz del sol?", ["Las dos palabras se escriben juntas.", "Sun + shine forman una sola palabra.", "Es sunshine."], "sunshine"),
    ],
    [
        ("Decir «do a mistake» o «make fun» para pasarlo bien.", "Se traducen los verbos palabra por palabra.", "Aprende el bloque completo: make a mistake y have fun."),
        ("Usar angry about con una persona.", "Se mezclan las dos preposiciones.", "Con una persona usa with: angry with Tom; con una cosa usa about."),
    ],
    [
        ("¿Qué significa «make friends»?", "Hacer amigos", "Es una expresión fija con make."),
        ("Completa: «We ___ a good time at the picnic.» Opciones: had / made.", "had", "El bloque correcto es have a good time."),
        ("Completa: «I ___ to go to the party because I have a cold.» Opciones: don't want / doesn't want.", "don't want", "Con I se usa I don't want to… para decir que no quieres algo."),
    ],
    [
        ("Completa: «Everybody can make a ___.» Opciones: mistake / fun.", "mistake", "Make a mistake es la expresión fija."),
        ("Une note + book y escribe la palabra compuesta que se forma (un cuaderno).", "notebook", "Las dos palabras se escriben juntas."),
        ("Completa: «She is afraid of ___ in planes.» Opciones: flying / fly.", "flying", "Después de la preposición of va el verbo con -ing."),
    ],
    [
        ("Completa: «Tom is angry ___ his brother because he broke his game.» (broke = rompió) Opciones: with / about.", "with", "Se usa with cuando el enojo es contra una persona."),
        ("Completa: «Ana is angry ___ the noise in the street.» Opciones: about / with.", "about", "El enojo es por una cosa, así que se usa about."),
        ("¿Cuál despedida significa «hasta luego, nos vemos más tarde hoy»? a) See you later. b) See you soon.", "a", "Later indica un momento cercano del mismo día."),
    ],
    [
        ("¿Cuál par son sinónimos? a) glad–happy b) glad–sad", "a", "Glad y happy significan contento."),
        ("«Suddenly, the lights went out.» (went out = se apagaron) ¿Qué idea expresa suddenly? a) Que algo pasó de forma inesperada. b) Que algo pasa todos los días.", "a", "Suddenly significa de repente."),
    ],
    [
        ("Completa: «Tomás likes ___ activities like cycling in the park.» Opciones: outdoor / indoor.", "outdoor", "Andar en bicicleta en el parque se hace al aire libre."),
        ("Completa: «My teacher gave me advice ___ my project.» Opciones: on / at.", "on", "La expresión fija es give advice on."),
    ],
    [("Escribes un mensaje a un amigo sobre un campamento. ¿Cuál oración usa bien las expresiones? a) I had a good time and made friends. b) I made a good time and had friends.", "a", "Los bloques correctos son have a good time y make friends.")],
    [
        ("¿Qué significa «have fun»?", "Pasarlo bien", "Es una expresión fija."),
        ("¿Qué es una palabra compuesta?", "Una palabra formada por dos palabras", "Por ejemplo homework o notebook."),
        ("¿Qué preposición va con una persona: about o with?", "with", "Angry with Tom se usa para personas."),
    ],
    task("Lee este encargo: escribe en tu hoja un mensaje de seis a ocho oraciones a un amigo sobre una salida con tu curso (real o imaginaria). Debe incluir tres colocaciones (make friends, have fun, make plans, make a mistake o give advice on), la palabra suddenly con coma, una palabra compuesta y la despedida See you soon. Subraya cada expresión.", "Hi Sam, I had fun at the park with my class. I made new friends. Suddenly, it started to rain, so we played indoor games. I made plans to go again. See you soon, Ana.", ["usa tres colocaciones bien formadas", "usa suddenly con coma y una despedida adecuada", "incluye una palabra compuesta"], ["hoja con el mensaje y las expresiones subrayadas"], ["decir do a mistake", "olvidar la coma después de suddenly"], "Pide que reemplace una palabra por un sinónimo y que explique si el mensaje sigue igual."),
    "Escribe en tu hoja diez expresiones de la clase con su significado en español.",
    "Escribe tres pares de sinónimos nuevos que conozcas y usa uno en cada oración distinta.",
)

# ================================================================ OA 12 clase 3: describir objetos y señalar tiempo, grado y modo
lesson(
    OA12, 3,
    "Las oraciones y descripciones escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a describir objetos con varios adjetivos en orden y a decir cuándo, cómo y cuánto ocurre una acción. Sirve para escribir descripciones y relatos más precisos.",
    ["Conozco adjetivos como old, new, big y small.", "Sé que quiet es un adjetivo y que significa callado."],
    [
        "Para describir un objeto en detalle se pueden juntar varios adjetivos antes del sustantivo. El orden habitual es: opinión (nice), tamaño (big, small), edad (old, new), color (red, brown), material (wooden, metal, plastic) y al final el tipo de objeto. Ejemplos: a big old metal key (una llave grande, vieja, de metal), a small red plastic bag (una bolsa pequeña, roja, de plástico). Además, a o an dependen del primer sonido: an old key.",
        "Para señalar el modo (cómo) se usan adverbios que suelen terminar en -ly: quiet → quietly, loud → loudly, soft → softly, slow → slowly. Dos son especiales: fast se queda fast (He runs fast, no fastly) y good se vuelve well (She sings well). Los adverbios de modo van después del verbo: She sings softly.",
        "Para señalar el tiempo (cuándo) se usan palabras como yesterday (ayer), last night, every week (cada semana) y today; van al final: He won the race yesterday. Para el grado (cuánto) se usa very antes del adjetivo o adverbio: They run very fast. Combinar modo, tiempo y grado hace tus oraciones más completas.",
    ],
    [("adjective order", "orden de los adjetivos"), ("wooden / metal / plastic", "de madera / de metal / de plástico"), ("quietly / loudly / softly", "en silencio / fuerte / suavemente"), ("fast / well", "rápido / bien"), ("yesterday", "ayer"), ("every week", "cada semana"), ("very", "muy")],
    [
        ("Ordenar adjetivos", "Elige la frase correcta. a) a metal big key b) a big metal key", ["El tamaño va antes del material.", "Big es tamaño y metal es material.", "La correcta es a big metal key."], "a big metal key"),
        ("Transformar en adverbio", "Convierte el adjetivo quiet en adverbio de modo: «The cat walks ___.»", ["Los adverbios de modo suelen terminar en -ly.", "Se agrega -ly a quiet.", "Queda quietly."], "quietly"),
    ],
    [
        ("Escribir «He runs fastly».", "Se agrega -ly a todos los adjetivos.", "Fast es la excepción: He runs fast."),
        ("Poner el material antes de la edad: a wooden old table.", "No se conoce el orden habitual.", "Primero la edad y luego el material: an old wooden table."),
    ],
    [
        ("¿Qué significa «every week»?", "Cada semana", "Indica con qué frecuencia ocurre algo."),
        ("¿Qué significa «yesterday»?", "Ayer", "Es un adverbio de tiempo."),
        ("Convierte soft en adverbio: «She sings ___.»", "softly", "Se agrega -ly."),
    ],
    [
        ("Completa: «He runs ___.» Opciones: fast / fastly.", "fast", "Fast es una excepción: no cambia."),
        ("Completa: «She sings very ___.» Opciones: well / good.", "well", "Modifica al verbo y por eso va well."),
        ("¿Qué oración tiene el orden correcto? a) an old wooden table b) a wooden old table", "a", "La edad va antes del material."),
    ],
    [
        ("Ordena las palabras para describir un objeto: bottle / new / a / plastic / water.", "a new plastic water bottle", "Va el artículo, la edad, el material y el tipo de objeto."),
        ("Completa: «The baby sleeps ___.» Opciones: quietly / quiet.", "quietly", "El adverbio de modo describe cómo duerme."),
        ("Completa: «She went to the library ___.» Opciones: yesterday / tomorrow. (went = fue; tomorrow = mañana)", "yesterday", "Went está en pasado y yesterday señala un momento pasado."),
    ],
    [
        ("Los estudiantes caminan callados por la biblioteca. ¿Qué oración es correcta? a) The students walk quiet. b) The students walk quietly.", "b", "Walk es un verbo y necesita un adverbio de modo."),
        ("¿Qué descripción da más información? a) It's a small old brown leather bag. (leather = cuero) b) It's a bag.", "a", "Agrega tamaño, edad, color y material."),
    ],
    [
        ("En «She sings softly every week», ¿cuál es el adverbio de modo?", "softly", "Responde a cómo canta; every week responde a cuándo."),
        ("Hay dos cajas. A) a large old metal box. B) a small new metal box. La descripción dice: «It's the old one, and it's large». ¿De qué caja se trata?", "A", "La caja A es vieja y grande."),
    ],
    [("En una nota de objetos perdidos, ¿qué aviso ayuda más a encontrar la botella? a) Lost: a small blue plastic water bottle. b) Lost: a bottle.", "a", "Da tamaño, color y material.")],
    [
        ("¿En qué orden va el material respecto de la edad?", "Después de la edad", "Primero old y luego wooden."),
        ("¿Cómo se dice «bien» como adverbio de good?", "well", "Es una excepción."),
        ("¿Qué palabra de grado se usa antes de un adjetivo para decir muy?", "very", "Very fast significa muy rápido."),
    ],
    task("Lee este encargo: elige un objeto de tu casa o de tu mochila y describe en tu hoja con una oración el objeto usando tres adjetivos en orden (tamaño, edad o color, y material). Después escribe tres oraciones: una con un adverbio de modo, una con un adverbio de tiempo y una con very.", "It's a small old red plastic ruler. My brother walks quietly. I did my homework yesterday. The teacher speaks very clearly.", ["usa tres adjetivos en el orden habitual", "usa un adverbio de modo bien formado", "usa un adverbio de tiempo al final y very antes de un adjetivo o adverbio"], ["hoja con la descripción y tres oraciones"], ["fastly", "material antes de la edad"], "Pide que cambie el orden de los adjetivos y explique por qué suena raro."),
    "Copia cuatro frases con adjetivos en orden y subraya el material de cada una.",
    "Escribe un aviso de objeto perdido de tres líneas con un objeto, su descripción detallada y el día en que se perdió.",
)

# ================================================================ OA 12 clase 4: preguntas Does/Did y acciones en pasado continuo
lesson(
    OA12, 4,
    "Las oraciones y mini textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a hacer y responder preguntas con Does/Did y a describir acciones que interrumpen u ocurren a la vez en el pasado. Sirve para contar qué hacían las personas y qué pasó en ese momento.",
    ["Conozco el pasado de verbos como went, won, saw y found.", "Sé que en inglés se dice He cooks y I cook."],
    [
        "Para preguntar sobre rutinas en presente se usa Do o Does: Does he cook? (¿Cocina él?). Se responde con respuestas cortas: Yes, he does. / No, he doesn't. Con I, you, we y they se usa Do: Do they live near the school? Para el pasado se usa Did con todos los sujetos: Did he cook? Yes, he did. / No, he didn't. Después de does o did el verbo queda en su forma simple: Did she cook?, no Did she cooked?",
        "El pasado continuo (was/were + verbo con -ing) muestra una acción en progreso en el pasado. Se usa was con I, he, she, it y were con you, we, they. Con when, una acción larga es interrumpida por otra corta en pasado simple: «I was playing football when it started to rain». Con while, dos acciones largas ocurren al mismo tiempo: «While he was cycling, she was listening to music».",
        "Para escribir bien, pregúntate: ¿cuál acción estaba en progreso? Esa lleva was/were + -ing. ¿Cuál la interrumpió? Esa va en pasado simple: started, rang (sonó), came, saw. Cuando while y when abren la oración, se pone una coma antes de la segunda parte: While Ana was cooking, her brother was playing.",
    ],
    [("Does / Did", "preguntas en presente / en pasado"), ("short answer", "respuesta corta: Yes, he did."), ("was / were + -ing", "estaba(n) haciendo"), ("when", "cuando (una acción interrumpe a otra)"), ("while", "mientras (dos acciones a la vez)"), ("rang", "sonó"), ("started", "empezó")],
    [
        ("Responder con una respuesta corta", "Pregunta: «Did he cook yesterday?» Hecho: no cocinó. Escribe la respuesta corta.", ["La pregunta usa Did, así que la respuesta usa did.", "El hecho dice que no cocinó.", "Queda No, he didn't."], "No, he didn't."),
        ("Identificar la acción interrumpida", "«I was reading when the phone rang.» ¿Qué acción estaba en progreso?", ["Was reading tiene el patrón was + -ing.", "Rang es la acción corta que interrumpe.", "La acción en progreso es reading."], "was reading"),
    ],
    [
        ("Escribir «Did she cooked?».", "Se pone el pasado dos veces.", "Después de did el verbo va simple: Did she cook?"),
        ("Usar while con una acción que interrumpe.", "Se piensa que while y when son iguales.", "While une dos acciones largas a la vez; when presenta la acción que interrumpe."),
    ],
    [
        ("Completa: «Does she cook?» Yes, she ___. Opciones: does / did.", "does", "La pregunta está en presente y usa does."),
        ("¿Qué significa «while»?", "Mientras", "Une dos acciones que ocurren a la vez."),
        ("Completa la respuesta corta: «Did he play?» No, he ___. Opciones: didn't / doesn't.", "didn't", "La pregunta usa did, así que la respuesta usa didn't."),
    ],
    [
        ("Completa: «___ Pedro swim yesterday?» Opciones: Did / Does.", "Did", "Yesterday está en pasado y se usa Did."),
        ("¿Cuál pregunta es correcta? a) Did she cook dinner? b) Did she cooked dinner?", "a", "Después de Did el verbo queda en forma simple."),
        ("Completa: «I ___ reading when the bell rang.» Opciones: was / were.", "was", "Con I se usa was."),
    ],
    [
        ("Completa: «They ___ cycling when it started to rain.» Opciones: were / was.", "were", "Con they se usa were."),
        ("Completa: «While Ana was cooking, her brother ___ music.» Opciones: was listening to / were listening to.", "was listening to", "Son dos acciones a la vez y her brother es singular, así que se usa was + -ing."),
        ("Pregunta: «Do they live near the school?» Dato: viven lejos. Escribe la respuesta corta.", "No, they don't.", "La pregunta usa Do con they y el dato dice que no."),
    ],
    [
        ("«The students were reading when the bell rang.» ¿Cuál acción interrumpió a la otra? Opciones: the bell rang / were reading.", "the bell rang", "La acción corta en pasado simple interrumpe la que estaba en progreso."),
        ("¿Qué oración muestra dos acciones al mismo tiempo? a) While Sam was studying, his sister was painting. b) Sam studied and then his sister painted.", "a", "While une dos acciones largas que ocurren a la vez."),
    ],
    [
        ("Completa: «Cuando la profesora entró, nosotros estábamos conversando.» «When the teacher came in, we ___.» Opciones: were talking / talked.", "were talking", "Se pide una acción en progreso que fue interrumpida."),
        ("Respuesta: «Yes, he did». ¿Qué pregunta responde? a) Did he win the race? b) Does he win the race?", "a", "Did he… se responde con did."),
    ],
    [("Tu hermano menor te pregunta: «Did your sister call you yesterday?». Ella no llamó. ¿Cuál respuesta corta es correcta? a) No, she didn't. b) No, she doesn't.", "a", "La pregunta usa Did, así que la respuesta usa didn't.")],
    [
        ("¿Cuándo se usa was con el pasado continuo?", "Con I, he, she e it", "Con you, we y they se usa were."),
        ("¿Qué verbo va después de did: simple o en pasado?", "Simple", "Did ya lleva el pasado."),
        ("¿Qué diferencia hay entre when y while?", "When introduce la acción que interrumpe y while une dos acciones a la vez", "Cambian el sentido de la oración."),
    ],
    task("Lee este encargo: escribe en tu hoja cuatro preguntas Does/Did con sus respuestas cortas sobre la rutina de un compañero (por ejemplo, Does he play soccer? Yes, he does). Después escribe dos oraciones con when y dos con while sobre algo que pasó en tu recreo, usando was/were + -ing.", "Does she read every day? Yes, she does. Did she walk to school? No, she didn't. Do they play soccer? Yes, they do. Did he draw today? No, he didn't. I was eating when the bell rang. We were playing when it started to rain. While I was talking, my friend was drawing. While Leo was running, Ana was laughing.", ["las preguntas usan do/does/did con verbo simple", "las respuestas cortas coinciden con la pregunta", "usa was/were + -ing con when y while según el sentido"], ["hoja con preguntas, respuestas y cuatro oraciones"], ["Did she cooked", "usar while para una interrupción"], "Pide que cambie when por while en una oración y explique si el significado se mantiene."),
    "Copia tres preguntas con Does y tres con Did y escribe sus respuestas cortas.",
    "Escribe un mini relato de cuatro oraciones sobre lo que pasaba en tu casa a una hora de ayer, usando was/were y una interrupción.",
)

# ================================================================ OA 12 clase 5: causa, efecto y condiciones
lesson(
    OA12, 5,
    "Las oraciones y mini textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a explicar causa y efecto y a expresar condiciones con if. Sirve para explicar por qué pasa algo y qué pasa si se cumple una condición.",
    ["Conozco because (porque) y so (así que).", "Sé escribir oraciones en presente y en futuro con will."],
    [
        "Una causa es lo que hace que algo ocurra y el efecto es lo que ocurre. Se unen con because (porque) o so (así que): «It was cold, so I wore a jacket» (la causa es el frío y el efecto es usar chaqueta). También se explican hechos que siempre ocurren con if en presente: «Ice melts if you leave it in the sun». Aquí se usa el presente en las dos partes.",
        "Una condición con if dice qué pasará si algo se cumple. Se usa if + presente simple y, en la otra parte, will + verbo simple: «If you cook, I'll help you» (I'll es I will). No se pone will después de if: no se dice If you will cook. Si la oración empieza con if, se escribe una coma antes de la otra parte: If it rains, we will stay home.",
        "Para escribir un párrafo claro puedes combinar estas ideas: una causa con because, un resultado con so y una condición con if. Primero define cuál es la causa y cuál es el efecto, luego elige el conector. Revisa que la coma esté donde va y que will no aparezca junto a if.",
    ],
    [("cause / effect", "causa / efecto"), ("because / so", "porque / así que"), ("if", "si (condición)"), ("I'll", "I will, yo voy a / yo haré"), ("melts", "se derrite"), ("stay home", "quedarse en casa"), ("condition", "condición")],
    [
        ("Elegir entre because y so", "Completa: «It was cold, ___ I wore a jacket.» Opciones: so / because.", ["La primera parte es la causa.", "La segunda es el efecto.", "Para un efecto se usa so."], "so"),
        ("Formar una condición", "Completa: «If you ask me, I ___ help you.» Opciones: will / are.", ["Después de if va el presente simple.", "En la otra parte se usa will + verbo.", "Queda I will help you."], "will"),
    ],
    [
        ("Escribir «If you will study, you pass».", "Se pone will en las dos partes.", "Después de if va el presente: If you study, you will pass."),
        ("Cambiar causa y efecto: «I wore a jacket, so it was cold».", "No se mira cuál ocurrió primero.", "La causa es el frío y el efecto es la chaqueta: It was cold, so I wore a jacket."),
    ],
    [
        ("¿Qué significa «if»?", "Si, en una condición", "Introduce algo que debe cumplirse."),
        ("¿Qué significa «I'll»?", "I will", "Es la forma corta de I will."),
        ("Completa: «The road was closed, ___ we took the bus.» Opciones: so / because.", "so", "Tomar el bus es el efecto del camino cerrado."),
    ],
    [
        ("Completa: «If it rains, we ___ stay home.» Opciones: will / are.", "will", "Después de la condición con if se usa will + verbo simple."),
        ("¿Cuál oración es correcta? a) If you study, you will pass. b) If you will study, you pass.", "a", "Después de if va el presente simple."),
        ("«A puddle dries if the sun shines.» (puddle = charco) ¿Cuál es la causa?", "Que el sol brille", "Es lo que hace que el charco se seque."),
    ],
    [
        ("Completa: «The plant dies if it ___ water.» Opciones: doesn't get / won't get.", "doesn't get", "En un hecho general, después de if se usa el presente simple."),
        ("Completa: «If you ___ me, I'll help you.» Opciones: ask / will ask.", "ask", "Después de if va el presente simple."),
        ("Causa: Mia didn't sleep. ¿Cuál es el efecto probable? a) She was tired. b) She was not tired.", "a", "No dormir produce cansancio."),
    ],
    [
        ("«The match ended early because it started to rain.» ¿Cuál es la causa?", "It started to rain", "Because introduce la razón por la que terminó antes."),
        ("Un compañero escribió «If I will see you tomorrow, I'll say hello». ¿Cuál es el error? a) Will después de if b) Say hello debe ir en pasado", "a", "Después de if va el presente simple: If I see you…"),
    ],
    [
        ("Ordena las palabras para formar una condición: I'll / If / it / rains, / take / an umbrella.", "If it rains, I'll take an umbrella.", "La condición con if va primero y luego la parte con will."),
        ("¿Qué oración expresa una condición? a) It's too cold, so Ana wears a coat. b) If it snows, she'll stay home.", "b", "Solo la segunda tiene if."),
    ],
    [("Escribes un aviso sobre reciclaje para tu colegio. ¿Cuál oración está correcta? a) If you put paper in the blue bin, we will recycle it. b) If you will put paper in the blue bin, we recycle it.", "a", "Después de if se usa presente y el resultado lleva will.")],
    [
        ("¿Qué verbo se usa después de if en una condición?", "Presente simple", "No se usa will después de if."),
        ("¿Qué conector introduce el efecto: because o so?", "so", "So se usa para el efecto; because introduce la razón."),
        ("¿Dónde va la coma si la oración empieza con if?", "Entre las dos partes", "Separa la condición del resultado."),
    ],
    task("Lee este encargo: escribe en tu hoja un párrafo de cinco oraciones sobre una situación del colegio. Debe tener una causa con because, un efecto con so y dos condiciones con if (una de hecho general, como Ice melts if you leave it in the sun, y otra con will). Subraya los tres conectores y revisa que después de if no aparezca will.", "We stayed inside because it was raining. It was cold, so I wore a jacket. If you leave ice in the sun, it melts. If it stops raining, we will play outside. I was late because the bus came late.", ["usa because y so con la causa y el efecto bien ubicados", "usa dos oraciones con if bien formadas", "usa coma cuando if abre la oración"], ["hoja con el párrafo y los conectores subrayados"], ["will junto a if", "invertir causa y efecto"], "Pide que invierta la causa y el efecto de una oración y explique qué cambia."),
    "Copia las cuatro oraciones de la tarea del ejemplo y subraya la causa en una y la condición en otra.",
    "Escribe una pequeña regla de convivencia para tu curso usando if y will.",
)

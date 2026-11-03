"""Cuaderno del estudiante, 8.º básico Inglés (propuesta), EN08 OA 05 (lectura de textos con las funciones del lenguaje del año).

Todos los textos para leer son originales y están escritos en cada ejercicio, con pista en español.
Las clases del plan tienen títulos genéricos; aquí cada clase recorre un grupo de las funciones que nombra el OA.
Las cifras de los textos son de ejemplo.
"""
from __future__ import annotations

from student_content_en8_a import lesson, task
from student_lessons import arith

OA5 = "EN08 OA 05"
READ = "Lee: "

# ---------------------------------------------------------------- clase 1: cantidades, descripción de objetos, lugares y personas
RACE = "«Last year, the charity race had two thousand runners. This year, there are four thousand. The organizers have enough water for everyone, but there is no time for long speeches. The race raised one million pesos for the animal shelter.» (charity race = corrida solidaria, runners = corredores, organizers = organizadores, enough = suficiente, speeches = discursos, raised = recaudó, shelter = refugio)"
BUILD = "«Lucas lives in a tall gray building near the park. His neighbors are French. The woman with the red scarf is his aunt, and the man in the blue coat is his uncle. They are visiting for the weekend.» (building = edificio, neighbors = vecinos, French = franceses, scarf = bufanda, coat = abrigo, aunt = tía, uncle = tío, visiting = visitando)"

lesson(
    OA5, 1,
    "Los textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer textos que expresan cantidades (thousand, million, enough, no) y que describen objetos, lugares y personas (a tall gray building, the woman with…). Sirve para entender cifras y descripciones en un texto.",
    ["Sé los números hasta cien y los colores.", "Conozco is y are."],
    [
        "Para expresar cantidades, el inglés usa números y palabras de cantidad. Thousand (mil) y million (millón) no llevan -s cuando hay un número antes: two thousand, four thousand, one million. Enough significa suficiente y va antes del sustantivo: enough water. No significa ninguno o nada: no time, no money. Para contar, lee la cifra completa: four thousand es 4.000 y one million es 1.000.000.",
        "Para describir un objeto, un lugar o una persona, el orden más frecuente es artículo + tamaño + color + sustantivo: a tall gray building. Con they are + nacionalidad se dice de dónde son: they are French. También se identifica a una persona con the man in… (el hombre con…) o the woman with… (la mujer con…). In se usa con la ropa con que alguien va vestido: the man in the blue coat. With se usa con un accesorio o un rasgo: the woman with the red scarf, the girl with long hair.",
        "Cuando leas, subraya las cifras y los adjetivos. Pregunta: ¿cuántos?, ¿cómo es?, ¿quién es? Los números grandes se leen por partes: two thousand five hundred es 2.500. Si una frase tiene no money, significa que no hay nada de dinero, no que hay poco. La palabra enough tampoco significa mucho: significa lo necesario.",
    ],
    [("thousand", "mil"), ("million", "millón"), ("enough", "suficiente"), ("no money", "nada de dinero"), ("the woman with…", "la mujer con…"), ("the man in…", "el hombre con (ropa)…")],
    [
        ("Leer una cifra", READ + RACE + " ¿Cuántos corredores hay este año?", ["Busco la frase This year.", "Dice there are four thousand.", "Four thousand es 4.000."], "4.000 corredores"),
        ("Identificar a una persona", READ + BUILD + " ¿Quién es la tía de Lucas?", ["Busco aunt.", "Dice The woman with the red scarf is his aunt.", "La tía lleva una bufanda roja."], "La mujer con la bufanda roja"),
    ],
    [
        ("Leer «two thousand» como 2.000.000.", "Se confunde thousand con million.", "Thousand es mil; million es un millón."),
        ("Pensar que «enough water» significa mucha agua.", "Se confunde enough con many.", "Enough es la cantidad necesaria, ni más ni menos."),
    ],
    [
        # rec
        (READ + RACE + " ¿Cuántos corredores hubo el año pasado? a) 2.000 b) 4.000", "a) 2.000", "El texto dice two thousand runners."),
        (READ + RACE + " ¿Cuánto dinero recaudó la corrida? a) un millón de pesos b) mil pesos", "a) un millón de pesos", "El texto dice one million pesos."),
        (READ + BUILD + " ¿De qué color es el edificio? a) gris b) azul", "a) gris", "Dice a tall gray building."),
    ],
    [
        # und
        (READ + RACE + " ¿Qué significa «enough water»? a) agua suficiente b) nada de agua", "a) agua suficiente", "Enough significa suficiente."),
        (READ + RACE + " ¿Qué falta, según el texto? a) tiempo para discursos largos b) agua", "a) tiempo para discursos largos", "El texto dice there is no time for long speeches."),
        (READ + BUILD + " ¿De qué país son los vecinos? a) de Francia b) de España", "a) de Francia", "They are French significa que son franceses."),
    ],
    [
        # app
        arith(READ + RACE + " ¿Cuántos corredores más hay este año que el año pasado?", "4000-2000", "Se resta 2.000 a 4.000."),
        (READ + BUILD + " ¿Quién lleva el abrigo azul? a) el tío b) la tía", "a) el tío", "Dice the man in the blue coat is his uncle."),
        arith(READ + RACE + " Si cada uno de los 4.000 corredores dona 250 pesos, ¿cuántos pesos se juntan?", "4000*250", "Se multiplica la cantidad de corredores por la donación."),
    ],
    [
        # rea
        (READ + BUILD + " ¿Qué diferencia hay entre «the man in the blue coat» y «the woman with the red scarf»? a) in describe la ropa con que va vestida la persona y with describe un accesorio o rasgo b) no hay diferencia", "a) in describe la ropa con que va vestida la persona y with describe un accesorio o rasgo", "El abrigo es la ropa; la bufanda es un accesorio que identifica a la mujer."),
        (READ + RACE + " Una compañera dice que «no time» significa poco tiempo. ¿Cuál es la corrección? a) significa que no hay nada de tiempo b) significa mucho tiempo", "a) significa que no hay nada de tiempo", "No time quiere decir ningún tiempo."),
    ],
    [
        # cha
        arith(READ + "«The stadium has fifty thousand seats. Today there are forty-eight thousand people.» (stadium = estadio, seats = asientos, people = personas). ¿Cuántos asientos quedan libres?", "50000-48000", "Se resta 48.000 a 50.000."),
        ("¿Cómo se dice «hay dos mil estudiantes»? a) There are two thousand students b) There are two thousands students", "a) There are two thousand students", "Thousand no lleva -s después de un número."),
    ],
    [
        # context
        (READ + "«The new bakery has a long wooden counter. The girl in the green apron is the baker, and the boy with the black cap is her helper. They sell two thousand loaves every month.» (bakery = panadería, counter = mesón, apron = delantal, cap = gorro, loaves = panes, month = mes). ¿Quién es el ayudante? a) el niño con gorro negro b) la niña con delantal verde", "a) el niño con gorro negro", "Dice the boy with the black cap is her helper.")
    ],
    [
        # selfcheck
        ("¿Cómo se escribe 1.000.000 en palabras en inglés?", "One million", "Un millón se escribe one million."),
        ("¿Qué significa «no money»?", "Nada de dinero", "No equivale a ninguno."),
        ("¿Cómo se dice «el hombre con abrigo»?", "The man in the coat", "In se usa con ropa."),
    ],
    task("Lee este texto: «The school choir has fifty members. Last year, it had thirty. The girl with the long black hair is the director, and the boy in the red jacket is the pianist. There is enough music for everyone, but there is no money for new costumes.» (choir = coro, members = integrantes, director = directora, pianist = pianista, costumes = trajes). En tu hoja escribe: cuántos integrantes hay hoy, cuántos más que el año pasado, quién es el pianista y qué falta.", "Hoy hay 50 integrantes; 20 más que el año pasado; el pianista es el niño con la chaqueta roja; falta dinero para trajes nuevos.", ["usa las cifras correctas", "resta bien la diferencia", "identifica a la persona y lo que falta"], ["hoja con cuatro respuestas", "nota del adulto"], ["leer fifty como 15", "no entender no money"], "Reconoce lo que acertó y relee con la persona las cifras y las palabras in, with y no."),
    "Lee de nuevo el texto de la corrida y subraya cada cifra con su palabra.",
    "Escribe en español la descripción de tu vecino o de una persona de tu casa usando las ideas the man in… y the woman with….",
)

# ---------------------------------------------------------------- clase 2: dirección y posesión
ROUTE = "«Yesterday Tomás walked from his house to the supermarket. He went into the store, bought bread and came out of the store at five. Then he went to school to pick up his sister. They walked home together.» (supermarket = supermercado, bought = compró, pick up = recoger, sister = hermana)"
LOST = "«Lost and found. On the table there is a wallet, two pens and a scarf. Teacher: Whose wallet is this? Nico: It's not mine. Julia: It belongs to a friend of mine. Teacher: Which pen is yours, Nico? Nico: The red one is mine, and the blue one is hers (he points to Julia). Julia: No, the blue one is theirs. It belongs to the twins.» (lost and found = objetos perdidos, table = mesa, pens = lapiceras, scarf = bufanda, wallet = billetera, belongs to = pertenece a, twins = gemelos, mine = mío, hers = de ella, theirs = de ellos)"

lesson(
    OA5, 2,
    "Los textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer textos que expresan dirección (into, out of, from, to) y que piden o dan información sobre posesión (Whose…?, belongs to, mine, yours, his, hers, theirs). Sirve para seguir recorridos y saber de quién es cada cosa.",
    ["Sé las preposiciones in, on y at.", "Conozco los adjetivos my, your, his y her."],
    [
        "Las preposiciones de dirección muestran hacia dónde o desde dónde se mueve alguien. To indica el destino: to school. From indica el origen: from his house. Into indica entrar en un lugar cerrado: into the bank. Out of indica salir: out of the store. Se usan con verbos de movimiento como walk, go y come.",
        "Para hablar de posesión, preguntamos Whose…? (¿de quién?): «Whose wallet is this?». Las respuestas pueden ser It belongs to a friend of mine (pertenece a un amigo mío) o con pronombres posesivos que reemplazan al sustantivo: mine (mío), yours (tuyo), his (de él), hers (de ella), ours (nuestro), theirs (de ellos). «The red one is mine» significa «el rojo es mío». Which…? (¿cuál?) pide elegir entre varias: Which is yours?",
        "Los pronombres posesivos no llevan sustantivo después: se dice «It's hers», no «It's hers pen». En cambio, los adjetivos posesivos sí: «her pen». En un texto, ubica primero quién habla, y luego a quién se refiere cada pronombre. Para dirección, dibuja un camino con flechas y escribe sobre ellas to, from, into o out of.",
    ],
    [("into", "hacia adentro de"), ("out of", "hacia afuera de"), ("from", "desde"), ("to", "hacia, a"), ("whose", "de quién"), ("belongs to", "pertenece a")],
    [
        ("Seguir un recorrido", READ + ROUTE + " ¿Desde dónde caminó Tomás y hacia dónde?", ["Busco from: from his house.", "Busco to: to the supermarket.", "Junto el origen y el destino."], "Desde su casa al supermercado"),
        ("Saber de quién es un objeto", READ + LOST + " ¿De quién es la lapicera roja?", ["Nico dice The red one is mine.", "Mine significa mío.", "Es de Nico."], "De Nico"),
    ],
    [
        ("Usar into cuando se sale de un lugar.", "Se confunden entrar y salir.", "Into es entrar; out of es salir."),
        ("Escribir «It's hers pen».", "Se mezcla el pronombre con el adjetivo.", "Di «It's hers» o «It's her pen»."),
    ],
    [
        # rec
        (READ + ROUTE + " ¿A dónde fue Tomás después del supermercado? a) a la escuela b) a la plaza", "a) a la escuela", "El texto dice Then he went to school."),
        (READ + ROUTE + " ¿Qué hizo Tomás al llegar al supermercado? a) entró a la tienda b) salió de la tienda", "a) entró a la tienda", "Dice He went into the store."),
        (READ + LOST + " ¿Cuántas lapiceras hay sobre la mesa? Responde con un número.", "2", "El texto dice two pens."),
    ],
    [
        # und
        (READ + ROUTE + " ¿A qué hora salió de la tienda? a) a las cinco b) a las seis", "a) a las cinco", "El texto dice came out of the store at five."),
        (READ + LOST + " ¿Qué significa «It belongs to a friend of mine»? a) pertenece a un amigo mío b) lo compré en una tienda", "a) pertenece a un amigo mío", "Belongs to significa pertenece a."),
        (READ + LOST + " ¿De quién es la lapicera azul según Julia? a) de los gemelos b) de Nico", "a) de los gemelos", "Julia dice the blue one is theirs, it belongs to the twins."),
    ],
    [
        # app
        (READ + LOST + " Nico dice «the blue one is hers». ¿A quién se refiere con hers? a) a Julia b) a un amigo de Nico", "a) a Julia", "Nico señala a Julia cuando dice hers."),
        (READ + ROUTE + " Ordena los lugares que visita Tomás. A) la escuela B) el supermercado C) su casa (al comienzo)", "C, B, A", "Sale de su casa, entra al supermercado y luego va a la escuela."),
        (READ + LOST + " Completa: «The scarf is ___». Opciones: yours / your.", "yours", "Un pronombre posesivo va solo, sin sustantivo."),
    ],
    [
        # rea
        (READ + LOST + " Julia corrige a Nico. ¿Qué razón da? a) que la lapicera azul pertenece a los gemelos b) que la billetera es de Nico", "a) que la lapicera azul pertenece a los gemelos", "Julia da su razón con belongs to."),
        (READ + ROUTE + " ¿Por qué Tomás fue a la escuela? a) para recoger a su hermana b) para estudiar", "a) para recoger a su hermana", "Dice to pick up his sister."),
    ],
    [
        # cha
        ("Completa con la preposición correcta: «The students came ___ the classroom and went to the yard». Opciones: out of / into.", "out of", "Salieron de la sala, por eso out of."),
        (READ + LOST + " ¿Qué pregunta hace la profesora para elegir un lápiz entre varios? Escríbela.", "Which pen is yours, Nico?", "Which pide elegir entre opciones."),
    ],
    [
        # context
        (READ + "«Mía's bag is on the chair. Leo says: This bag is not mine, it is hers. Mía: Yes, it is mine. Thank you!» (chair = silla). ¿De quién es la mochila? a) de Mía b) de Leo", "a) de Mía", "Leo dice hers y Mía lo confirma.")
    ],
    [
        # selfcheck
        ("¿Qué significa «out of»?", "Hacia afuera de", "Indica salir de un lugar."),
        ("¿Qué pregunta se usa para saber de quién es algo?", "Whose…?", "Whose pregunta por el dueño."),
        ("¿Qué pronombre posesivo significa «de ellos»?", "Theirs", "Reemplaza al sustantivo."),
    ],
    task("Lee este texto: «María walked from her house to the park, then she went into the library and came out at four. On the bench, there were two jackets. Her friend Ana said: They are not mine. María: One belongs to the boy with the red cap. Ana: Which one is yours? María: The black one is mine, and the gray one is his.» (bench = banca, boy = niño, cap = gorro). En tu hoja escribe: el recorrido de María con from, to, into y out of, y de quién es la chaqueta gris.", "Recorrido: de su casa al parque, entró a la biblioteca y salió a las cuatro. La chaqueta gris es del niño con el gorro rojo.", ["usa from, to, into y out of", "identifica de quién es la chaqueta", "mantiene el orden del recorrido"], ["hoja con recorrido y respuesta", "nota del adulto"], ["confundir into con out of", "decir que la chaqueta gris es de María"], "Reconoce lo que acertó y revisa con la persona las flechas del recorrido y los pronombres posesivos."),
    "Dibuja el recorrido de Tomás con flechas y escribe sobre cada una to, from, into o out of.",
    "Escribe en español tres objetos de tu mochila y de quién son, usando las ideas mine, yours y hers.",
)

# ---------------------------------------------------------------- clase 3: frecuencia, grado, tiempo y acciones pasadas que continúan
CAMILA = "«Camila always walks to school, but she sometimes takes the bus when it rains. She is very good at drawing and quite tired after practice. She has studied English for three years, since she was eleven. She moved to this city five years ago. She has never visited Rapa Nui, but she has seen photos.» (always = siempre, sometimes = a veces, very = muy, quite = bastante, moved = se mudó, never = nunca, seen = visto)"

lesson(
    OA5, 3,
    "Los textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer textos que señalan frecuencia (always, sometimes, never), grado (very, quite) y tiempo (ago, for, since), y que describen acciones pasadas que continúan en el presente con have/has + participio. Sirve para saber cuánto, cuántas veces y desde cuándo ocurre algo.",
    ["Sé el presente simple y el pasado simple.", "Conozco los días y los años."],
    [
        "Los adverbios de frecuencia (frequency) dicen cuántas veces ocurre algo: always (siempre), usually (por lo general), sometimes (a veces), never (nunca). Los adverbios de grado (degree) dicen cuánto: very (muy), quite (bastante), a little (un poco). Los de tiempo ubican la acción: ago (hace) se usa con pasado simple: «She moved five years ago». Ago va después del tiempo.",
        "El presente perfecto (present perfect) usa have o has + participio para unir el pasado con el presente. «She has studied English for three years» significa que empezó en el pasado y todavía estudia. For se usa con una duración: for three years. Since se usa con el momento de inicio: since she was eleven. Con never y ever se habla de experiencias: «She has never visited Rapa Nui» (nunca ha visitado). Los participios regulares terminan en -ed (studied); algunos son irregulares: seen, been, eaten.",
        "Para no confundirte, mira el verbo auxiliar. Si hay has o have, la acción incluye el presente. Si hay did o un verbo en pasado con ago, la acción terminó. Pregunta: ¿cuánto tiempo? (for), ¿desde cuándo? (since), ¿hace cuánto? (ago). Las tres respuestas no son iguales.",
    ],
    [("always", "siempre"), ("never", "nunca"), ("very", "muy"), ("ago", "hace (tiempo)"), ("for / since", "durante / desde"), ("has studied", "ha estudiado")],
    [
        ("Frecuencia", READ + CAMILA + " ¿Con qué frecuencia camina Camila al colegio?", ["Busco el adverbio de frecuencia.", "El texto dice always walks to school.", "Always significa siempre."], "Siempre"),
        ("Duración y desde cuándo", READ + CAMILA + " ¿Cuánto tiempo lleva estudiando inglés y desde cuándo?", ["Busco for: for three years.", "Busco since: since she was eleven.", "For marca duración y since marca el inicio."], "Lleva tres años y empezó a los once"),
    ],
    [
        ("Usar for con un momento de inicio (for 2018).", "Se confunde for con since.", "For va con duración; since va con un punto de inicio."),
        ("Pensar que «She moved five years ago» sigue ocurriendo.", "Se ignora ago.", "Ago habla de una acción terminada en el pasado."),
    ],
    [
        # rec
        (READ + CAMILA + " ¿Cuándo toma el bus Camila? a) a veces, cuando llueve b) siempre c) nunca", "a) a veces, cuando llueve", "El texto dice sometimes takes the bus when it rains."),
        (READ + CAMILA + " ¿Hace cuántos años se mudó a la ciudad? a) cinco años b) tres años", "a) cinco años", "El texto dice five years ago."),
        (READ + CAMILA + " ¿Qué nunca ha hecho Camila? a) visitar Rapa Nui b) estudiar inglés", "a) visitar Rapa Nui", "El texto dice has never visited Rapa Nui."),
    ],
    [
        # und
        (READ + CAMILA + " ¿Qué significa «very good at drawing»? a) muy buena para dibujar b) un poco mala para dibujar", "a) muy buena para dibujar", "Very es muy."),
        (READ + CAMILA + " ¿Qué ha visto Camila de Rapa Nui? a) fotos b) la isla en persona", "a) fotos", "El texto dice she has seen photos."),
        (READ + CAMILA + " ¿Qué expresión indica el inicio de sus estudios de inglés? a) since she was eleven b) five years ago", "a) since she was eleven", "Since marca desde cuándo."),
    ],
    [
        # app
        arith(READ + CAMILA + " Camila se mudó hace 5 años y empezó a estudiar inglés hace 3 años. ¿Cuántos años pasaron entre su mudanza y el comienzo de sus estudios de inglés?", "5-3", "Se restan los años de los dos hechos para saber cuánto tiempo los separa."),
        (READ + CAMILA + " Completa: «She has lived here ___ five years». Opciones: for / since.", "for", "Five years es una duración."),
        (READ + CAMILA + " Completa: «She has studied English ___ she was eleven». Opciones: since / for.", "since", "She was eleven marca el inicio."),
    ],
    [
        # rea
        (READ + CAMILA + " ¿Qué muestra que Camila todavía estudia inglés? a) has studied (presente perfecto) b) moved (pasado)", "a) has studied (presente perfecto)", "Has + participio une el pasado con el presente."),
        (READ + CAMILA + " Un compañero dice que Camila nunca ha visto nada de Rapa Nui. ¿Qué dato lo corrige? a) she has seen photos b) she is very tired", "a) she has seen photos", "Vio fotos, aunque no visitó la isla."),
    ],
    [
        # cha
        ("Completa con el participio correcto: «I have ___ that movie three times» (see). Escribe la palabra.", "seen", "El participio de see es seen."),
        ("Ordena las palabras para formar una oración: have / never / I / eaten / insects.", "I have never eaten insects", "El orden es sujeto + have + never + participio."),
    ],
    [
        # context
        (READ + "«My uncle has worked in the same bakery for twenty years. He usually wakes up at four o'clock. He started this job a long time ago.» (worked = trabajado, wakes up = se levanta). ¿Cuántos años lleva trabajando? a) veinte b) cuatro", "a) veinte", "Dice for twenty years.")
    ],
    [
        # selfcheck
        ("¿Qué significa «never»?", "Nunca", "Es el extremo de la frecuencia."),
        ("¿Para qué se usa since?", "Para decir desde cuándo", "Se usa con un punto de inicio."),
        ("¿Cómo se forma el presente perfecto?", "Have o has + participio", "Une pasado y presente."),
    ],
    task("Lee este texto: «Joaquín always plays soccer on Saturdays. He has played for the school team since 2022. He started playing five years ago. He has never won a trophy, but he is quite happy because the team is very friendly.» (trophy = trofeo, started = empezó). En tu hoja escribe: cuándo juega, desde cuándo está en el equipo, hace cuántos años empezó y qué nunca ha hecho.", "Juega los sábados siempre; está en el equipo desde 2022; empezó hace cinco años; nunca ha ganado un trofeo.", ["identifica always, since y ago", "distingue desde cuándo y hace cuánto", "señala la experiencia con never"], ["hoja con cuatro respuestas", "nota del adulto"], ["confundir since con ago", "decir que ha ganado un trofeo"], "Reconoce lo que acertó y relee con la persona las palabras always, since, ago y never."),
    "Subraya en el texto de Camila cada adverbio de frecuencia, grado y tiempo con un color diferente.",
    "Escribe en español dos cosas que has hecho durante años y una que nunca has hecho.",
)

# ---------------------------------------------------------------- clase 4: conectar ideas e información esencial o adicional
NEXT = "«Marta is the girl who sits next to me. My bike, which is blue, was a birthday gift. On Saturday we went to the beach and then we had lunch. It was cold, so we wore jackets. We will wait until the rain stops. The beach is the cleanest in the region. It also has a small cafe.» (sits = se sienta, gift = regalo, lunch = almuerzo, wore = usamos, cleanest = el más limpio, region = región, cafe = cafetería)"

lesson(
    OA5, 4,
    "El texto escrito en cada ejercicio y lápiz.",
    "Aprenderé a leer textos que conectan ideas (and then, so, until, also) y que entregan información esencial o adicional con who y which. Sirve para entender cómo se relacionan las ideas dentro de una oración.",
    ["Sé because, so y then.", "Conozco who y which como preguntas."],
    [
        "Los conectores (connectors) unen ideas: and then (y luego) marca el orden; so (así que) muestra un resultado; until (hasta que) marca un límite; also (además) suma información. En «It was cold, so we wore jackets» el frío causa la decisión. En «We will wait until the rain stops», la espera termina cuando la lluvia para.",
        "Who y which presentan información sobre un sustantivo. Who se usa para personas: «Marta is the girl who sits next to me». Which se usa para cosas: «My bike, which is blue, was a gift». Si la información es esencial, sin ella no sabes de quién o de qué se habla, y no lleva comas: «the girl who sits next to me». Si es adicional (extra), solo agrega un dato y va entre comas: «My bike, which is blue, was a gift».",
        "Para saber si es esencial, quita esa parte y pregunta si la oración sigue identificando el sustantivo. «Marta is the girl» no dice cuál niña: la información es esencial. «My bike was a gift» sigue clara sin «which is blue»: la información es adicional. Lee los conectores y las comas como señales de organización del texto.",
    ],
    [("connector", "conector"), ("who", "que (para personas)"), ("which", "que, el cual (para cosas)"), ("essential information", "información esencial: identifica de quién se habla"), ("extra information", "información adicional: agrega un dato"), ("also", "además")],
    [
        ("Identificar información esencial", READ + NEXT + " ¿Qué niña es Marta, según el texto?", ["Busco who.", "Dice the girl who sits next to me.", "Esa información identifica a Marta."], "La niña que se sienta al lado del que habla"),
        ("Identificar información adicional", READ + NEXT + " ¿Qué dato adicional se da sobre la bicicleta?", ["Busco which.", "My bike, which is blue, was a birthday gift.", "El dato adicional es que es azul."], "Que es azul"),
    ],
    [
        ("Usar which para una persona.", "Se confunde who con which.", "Who va con personas; which va con cosas."),
        ("Poner comas en la información esencial.", "Se cree que todas las partes con who o which llevan comas.", "Solo la información adicional va entre comas."),
    ],
    [
        # rec
        (READ + NEXT + " ¿Qué hicieron después de ir a la playa? a) almorzaron b) fueron al cine", "a) almorzaron", "El texto dice we went to the beach and then we had lunch."),
        (READ + NEXT + " ¿Por qué usaron chaquetas? a) porque hacía frío b) porque llovía", "a) porque hacía frío", "El texto dice It was cold, so we wore jackets."),
        (READ + NEXT + " ¿Hasta cuándo esperarán? a) hasta que pare la lluvia b) hasta que salga el sol", "a) hasta que pare la lluvia", "El texto dice until the rain stops."),
    ],
    [
        # und
        (READ + NEXT + " ¿Qué conector suma la idea de la cafetería? a) also b) so", "a) also", "El texto dice It also has a small cafe."),
        (READ + NEXT + " ¿Con qué palabra se agrega información sobre una persona? a) who b) which", "a) who", "Who se usa para personas."),
        (READ + NEXT + " ¿La frase «which is blue» es información esencial o adicional?", "Adicional", "Va entre comas y solo agrega un dato."),
    ],
    [
        # app
        (READ + NEXT + " Completa: «The woman ___ lives next door is a doctor». Opciones: who / which.", "who", "The woman es una persona."),
        (READ + NEXT + " Completa: «My phone, ___ is new, has a good camera». Opciones: which / who.", "which", "Phone es una cosa."),
        (READ + NEXT + " ¿Qué playa es «la más limpia de la región»? a) la playa donde fueron b) la playa que no visitaron", "a) la playa donde fueron", "El texto dice The beach is the cleanest in the region."),
    ],
    [
        # rea
        (READ + NEXT + " Una compañera quita «who sits next to me» de la primera frase y queda «Marta is the girl». ¿Qué pasa? a) no se sabe qué niña es b) la oración queda igual de clara", "a) no se sabe qué niña es", "La información era esencial."),
        (READ + NEXT + " Si quitamos «which is blue», ¿sigue clara la oración? a) sí, porque era información adicional b) no, porque era esencial", "a) sí, porque era información adicional", "Solo agregaba un dato."),
    ],
    [
        # cha
        ("Une las dos ideas: «The boy is my cousin. He plays the guitar». a) The boy who plays the guitar is my cousin b) The boy which plays the guitar is my cousin", "a) The boy who plays the guitar is my cousin", "Who se usa para personas y es información esencial."),
        ("Une las dos ideas: «My laptop is old. It is still very fast». a) My laptop, which is old, is still very fast b) My laptop, who is old, is still very fast", "a) My laptop, which is old, is still very fast", "Which se usa para cosas y el dato adicional va entre comas."),
    ],
    [
        # context
        (READ + "«I will wait here until you finish. Then we will walk to school together, and also buy a snack.» (finish = terminar, snack = colación). ¿Qué hará la persona cuando el otro termine? a) caminar juntos al colegio b) irse a casa", "a) caminar juntos al colegio", "El texto dice Then we will walk to school together.")
    ],
    [
        # selfcheck
        ("¿Qué palabra se usa para cosas: who o which?", "Which", "Who es para personas."),
        ("¿Qué conector significa «hasta que»?", "Until", "Marca un límite."),
        ("¿La información esencial lleva comas?", "No", "La adicional sí va entre comas."),
    ],
    task("Lee este texto: «My neighbor Sara, who is a nurse, works at night. The hospital where she works is far, so she takes a taxi. She will rest until six, and then she will have dinner. She also teaches yoga on Sundays.» (nurse = enfermera, hospital = hospital, far = lejos, rest = descansar, teaches = enseña). En tu hoja escribe: información adicional sobre Sara, el efecto de que el hospital esté lejos, hasta cuándo descansará y qué hace además.", "Información adicional: es enfermera. Toma un taxi. Descansará hasta las seis. Además enseña yoga los domingos.", ["identifica who como información adicional", "usa so, until y also", "no cambia ningún dato"], ["hoja con cuatro respuestas", "nota del adulto"], ["confundir información esencial con adicional", "poner la hora equivocada"], "Reconoce lo que acertó y relee con la persona los conectores y las comas para revisar cada dato."),
    "Subraya en el texto de Marta las partes con who y which y escribe si son esenciales o adicionales.",
    "Escribe en español dos oraciones sobre personas que conoces: una con información esencial (la persona que…) y otra con información adicional entre comas.",
)

# ---------------------------------------------------------------- clase 5: procesos y acciones con agente desconocido (voz pasiva)
NOTICE = "«School notice. The gym is cleaned every Friday. The lights were repaired yesterday. Students are asked to leave their bags in the lockers. The winners of the quiz will be announced on Monday. Plastic bottles are collected in the yellow bin.» (notice = aviso, cleaned = limpiado, lights = luces, repaired = reparadas, asked = se pide, announced = anunciados, collected = recolectadas)"
OIL = "«How plastic is produced. Plastic is produced from oil. First, the oil is heated and separated. Then, small pieces are made, and finally the pieces are shaped into bottles and toys.» (produced = producido, oil = petróleo, heated = calentado, separated = separado, pieces = piezas, shaped = moldeadas)"

lesson(
    OA5, 5,
    "Los textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer textos que describen procesos y acciones en las que no se sabe o no importa quién las hace, con la voz pasiva (is/are/was/were + participio). Sirve para entender avisos, informes y descripciones de cómo se hace algo.",
    ["Sé el participio de verbos como make, clean y repair.", "Conozco is, are, was y were."],
    [
        "La voz pasiva (passive voice) se usa cuando importa más lo que ocurre que quién lo hace. Se forma con to be + participio. En presente: is/are + participio («The gym is cleaned every Friday»). En pasado: was/were + participio («The lights were repaired yesterday»). En futuro: will be + participio («The winners will be announced»). Se usa cuando el agente (quien hace la acción) es desconocido o no es importante.",
        "En un aviso o en la descripción de un proceso, la voz pasiva es muy frecuente: «Plastic is produced from oil», «Rooms are cleaned daily». No se dice quién produce el plástico ni quién limpia, porque eso no importa. Si quieres decir quién, se agrega by: «The lights were repaired by the school electrician». Sin by, el texto no menciona al agente.",
        "Para reconocer una oración pasiva, busca to be y un participio. Pregunta: ¿quién recibe la acción? En «The lights were repaired», las luces reciben la acción. Para traducir, puedes usar «fueron reparadas» o «se repararon». Atención al tiempo: is cleaned (hoy, habitual), was cleaned (pasado), will be cleaned (futuro).",
    ],
    [("passive voice", "voz pasiva"), ("agent", "agente: quien hace la acción"), ("is / are + participle", "presente pasivo"), ("was / were + participle", "pasado pasivo"), ("will be + participle", "futuro pasivo"), ("by", "por (agente)")],
    [
        ("Reconocer la voz pasiva", READ + NOTICE + " ¿Qué se hace cada viernes en el gimnasio?", ["Busco every Friday.", "Dice The gym is cleaned every Friday.", "Se limpia."], "Se limpia"),
        ("Pasado pasivo", READ + NOTICE + " ¿Qué fue reparado ayer?", ["Busco yesterday.", "Dice The lights were repaired yesterday.", "Las luces."], "Las luces"),
    ],
    [
        ("Decir «The gym is clean every Friday» cuando se quiere decir «se limpia».", "Se omite el participio.", "La voz pasiva necesita to be + participio: is cleaned."),
        ("Agregar siempre by + agente.", "Se cree que debe nombrarse a quien lo hace.", "En la pasiva se omite si es desconocido o no importa."),
    ],
    [
        # rec
        (READ + NOTICE + " ¿Cuándo se anunciarán los ganadores? a) el lunes b) el viernes", "a) el lunes", "El aviso dice will be announced on Monday."),
        (READ + NOTICE + " ¿Dónde se dejan las mochilas? a) en los casilleros b) en la biblioteca", "a) en los casilleros", "El aviso dice in the lockers."),
        (READ + OIL + " ¿De qué se produce el plástico? a) de petróleo b) de madera", "a) de petróleo", "Dice Plastic is produced from oil."),
    ],
    [
        # und
        (READ + NOTICE + " ¿Dónde se recolectan las botellas de plástico? a) en el contenedor amarillo b) en el contenedor azul", "a) en el contenedor amarillo", "Dice Plastic bottles are collected in the yellow bin."),
        (READ + OIL + " ¿Qué se hace primero con el petróleo? a) se calienta y se separa b) se moldea en juguetes", "a) se calienta y se separa", "Dice First, the oil is heated and separated."),
        (READ + OIL + " ¿Qué se fabrica al final del proceso? a) botellas y juguetes b) combustible", "a) botellas y juguetes", "Dice the pieces are shaped into bottles and toys."),
    ],
    [
        # app
        (READ + NOTICE + " Identifica el tiempo: «The lights were repaired». a) pasado b) futuro", "a) pasado", "Were + participio indica pasado."),
        (READ + NOTICE + " Completa: «The winners ___ announced on Monday». Opciones: will be / are.", "will be", "El aviso habla del futuro."),
        (READ + OIL + " Completa: «Plastic ___ from oil». Opciones: is produced / produces.", "is produced", "En la pasiva se usa is + participio."),
    ],
    [
        # rea
        (READ + NOTICE + " ¿Por qué el aviso no dice quién limpia el gimnasio? a) porque quien limpia no es lo importante b) porque nadie lo limpia", "a) porque quien limpia no es lo importante", "El agente se omite si no importa."),
        (READ + OIL + " Un compañero dice que «the pieces are shaped» es presente activo. ¿Qué lo corrige? a) lleva are + participio, que es voz pasiva b) lleva shape sin -ed", "a) lleva are + participio, que es voz pasiva", "Are + participio forma la pasiva."),
    ],
    [
        # cha
        ("Convierte a la voz pasiva y omite al agente: «Someone broke the window last night» (break → broken). Escribe la oración.", "The window was broken last night", "Was + participio de break (broken)."),
        ("Convierte a la voz pasiva en presente: «Workers clean the rooms daily». Escribe la oración sin by.", "The rooms are cleaned daily", "Are + participio."),
    ],
    [
        # context
        (READ + "«The bridge was built last year. It is used by many cyclists every day.» (bridge = puente, built = construido, cyclists = ciclistas). ¿Cuándo fue construido el puente? a) el año pasado b) este año", "a) el año pasado", "Dice was built last year.")
    ],
    [
        # selfcheck
        ("¿Cómo se forma la voz pasiva en presente?", "Is o are + participio", "Se forma con to be."),
        ("¿Qué palabra se usa para nombrar al agente?", "By", "Se usa antes de quien hace la acción."),
        ("¿Cuándo se usa la voz pasiva?", "Cuando el agente es desconocido o no importa", "Pone el foco en la acción."),
    ],
    task("Lee este aviso: «Library notice. The books are returned to the shelf before 5 p.m. The library was repaired last month. New computers will be installed next week. Silence is required in the reading room.» (shelf = estante, repaired = reparada, installed = instaladas, required = se exige). En tu hoja escribe: qué se hace con los libros, qué ocurrió el mes pasado, qué ocurrirá la próxima semana y qué se exige.", "Los libros se devuelven al estante; la biblioteca fue reparada; se instalarán computadores nuevos; se exige silencio en la sala de lectura.", ["identifica el presente pasivo", "identifica el pasado y el futuro", "no nombra agentes que no están"], ["hoja con cuatro respuestas", "nota del adulto"], ["confundir pasado y futuro", "agregar quién hace cada acción"], "Reconoce lo que acertó y subraya con la persona is/are, was y will be para distinguir los tiempos."),
    "Lee de nuevo el aviso del colegio y subraya cada verbo en voz pasiva.",
    "Escribe en español tres cosas que «se hacen» en tu colegio, como «se limpia» o «se cierra», sin decir quién las hace.",
)

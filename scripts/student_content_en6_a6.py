"""Cuaderno del estudiante, 6.º básico Inglés (propuesta), EN06 OA 06 (leer textos con funciones del lenguaje: cantidades, acciones, estados de ánimo, posición, gustos, planes y comparaciones).

Todos los textos están escritos en el enunciado y son originales; llevan pista en español.
Cada palabra o estructura nueva se explica antes de usarla. Sin audio externo.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA6 = "EN06 OA 06"


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


# ---------------------------------------------------------------- clase 1: cantidades y enumerar
CLASSROOM = "«In our classroom there are twenty-eight students, thirty chairs and four windows. There are twelve girls and sixteen boys. There is one teacher and one big map. There aren't any computers.» (students = estudiantes, chairs = sillas, windows = ventanas, girls = niñas, boys = niños, map = mapa, computers = computadores)"
LIBRARY = "«The school library has three hundred books about animals, two hundred and fifty books about space and one hundred and eighty comics. There are more animal books than space books. There are fewer comics than animal books.» (books = libros, space = espacio, comics = historietas, more than = más que, fewer than = menos que)"
RACE = "«Results of the school race. First: Marta. Second: Ian. Third: Zoe. Fourth: Pablo. Fifth: Eli.» (results = resultados, race = carrera)"

lesson(
    OA6, 1,
    "Los textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a leer y entender textos que expresan cantidades y enumeran, con There is, There are, números, how many, more than y fewer than, y los números ordinales. Sirve para entender informes, listas y resultados.",
    ["Sé contar hasta cien en inglés.", "Conozco palabras como books, chairs y windows."],
    [
        "Para decir cuántas cosas hay se usa There is (hay, para uno) y There are (hay, para más de uno). There is one teacher. There are four windows. En negativo: There isn't a... y There aren't any... Para preguntar la cantidad se usa How many...? y la respuesta es un número: twenty-eight (veintiocho), three hundred (trescientos), two hundred and fifty (doscientos cincuenta).",
        "Para comparar cantidades usamos more than (más que) y fewer than (menos que). Con cosas que se cuentan se dice fewer, como en fewer comics. Para enumerar, se usan los números ordinales: first (primero), second (segundo), third (tercero), fourth (cuarto) y fifth (quinto). También se enumera con listas: First,... Second,... Third,...",
        "Al leer un texto con muchos números, subráyalos y escribe qué cuenta cada uno. Después, haz las operaciones necesarias: sumar para saber el total o restar para comparar. Comprueba tus resultados con lo que dice el texto: si dice more, el primer número debe ser mayor. Eso te ayuda a descubrir errores.",
    ],
    [("There is / There are", "hay (uno) / hay (varios)"), ("How many?", "¿cuántos?"), ("more than / fewer than", "más que / menos que"), ("first, second, third", "primero, segundo, tercero"), ("fourth, fifth", "cuarto, quinto"), ("hundred", "cien (un centenar)")],
    [
        ("Leer una cantidad", "Lee: «On the table there are three pens, one ruler and two erasers.» (pens = lápices de pasta, ruler = regla, erasers = gomas). ¿Cuántos objetos hay en total?", ["Anoto cada cantidad: 3, 1 y 2.", "Sumo: 3 + 1 + 2.", "El total es 6."], "6 objetos"),
        ("Ordinales", "Lee: «Lucas finished second and Ana finished fifth.» (finished = terminó). ¿Quién llegó antes a la meta?", ["Second es el segundo lugar y fifth el quinto.", "Un lugar con número menor llega antes.", "Lucas llegó antes."], "Lucas"),
    ],
    [
        ("Usar There is con varios objetos: «There is four windows».", "No se concuerda el verbo con la cantidad.", "Con más de uno, usa There are."),
        ("Decir fewer comics como «más historietas».", "Se confunde fewer con more.", "Fewer es menos y more es más."),
    ],
    [
        ("Lee: " + CLASSROOM + " ¿Cuántas ventanas hay? a) 4 b) 28 c) 30", "a) 4", "Dice four windows."),
        ("Lee: " + CLASSROOM + " ¿Cuántos niños (boys) hay?", "16", "Dice sixteen boys."),
        ("Lee: " + CLASSROOM + " ¿Hay computadores en la sala? Responde sí o no.", "No", "Dice there aren't any computers."),
    ],
    [
        arith("Lee: " + CLASSROOM + " ¿Cuántas sillas más que estudiantes hay?", "30-28", "Hay treinta sillas y veintiocho estudiantes."),
        arith("Lee: " + CLASSROOM + " ¿Cuántas personas hay en la sala sumando estudiantes y profesor?", "28+1", "Son 28 estudiantes y 1 profesor."),
        ("Completa: «___ one teacher in the classroom.» Opciones: There is, There are.", "There is", "El sujeto one teacher es singular."),
    ],
    [
        arith("Lee: " + LIBRARY + " ¿Cuántos libros hay entre animales y espacio?", "300+250", "Se suman los libros de ambos temas."),
        arith("Lee: " + LIBRARY + " ¿Cuántos libros más de animales que de espacio hay?", "300-250", "Se resta el número menor del mayor."),
        arith("Lee: " + LIBRARY + " ¿Cuántos libros hay en total contando animales, espacio e historietas?", "300+250+180", "Se suman las tres cantidades."),
    ],
    [
        ("Lee: " + LIBRARY + " ¿Cuál es la categoría con menos libros? a) historietas b) animales c) espacio", "a) historietas", "180 es el número menor."),
        ("Lee: " + RACE + " ¿Quién llegó tercero y en qué lugar llegó Pablo?", "Zoe llegó tercera y Pablo cuarto", "Third es Zoe y Fourth es Pablo."),
    ],
    [
        ("Lee: " + CLASSROOM + " Una compañera dice que hay más niñas que niños. Con los números del texto, ¿es correcto? Responde sí o no.", "No", "Hay 12 niñas y 16 niños; hay más niños."),
        arith("Lee: " + CLASSROOM + " ¿Cuántos niños más que niñas hay?", "16-12", "Se comparan 16 niños con 12 niñas."),
    ],
    [("Lee la lista de compras de una feria del colegio: «For the cake sale we need two big cakes, twelve cupcakes and thirty cups.» (cake sale = venta de tortas, cupcakes = magdalenas, cups = vasos). ¿Cuántos cupcakes hay que comprar?", "12", "Dice twelve cupcakes.")],
    [
        ("¿Cuándo se usa There are?", "Con más de un objeto", "Se usa con plurales."),
        ("¿Qué significa «fewer than»?", "Menos que", "Sirve para comparar cantidades."),
        ("¿Cómo se dice «quinto» en inglés?", "fifth", "Es el ordinal de cinco."),
    ],
    task("Lee: «In my school there are three floors. On the first floor there are two classrooms and a library. On the second floor there are four classrooms. On the third floor there are five classrooms and one lab. There are no gyms in the building.» (floor = piso, lab = laboratorio, gym = gimnasio). Escribe una lista numerada con el número de salas de cada piso y calcula el total de salas.", "Primer piso: 2 salas. Segundo piso: 4 salas. Tercer piso: 5 salas. Total: 11 salas.", ["anota los tres pisos con ordinales", "suma correctamente 2 + 4 + 5", "indica que no hay gimnasio"], ["hoja con la lista", "nota del adulto"], ["contar la biblioteca o el laboratorio como sala", "sumar mal"], "Reconoce el cálculo correcto y explica por qué la biblioteca y el laboratorio no se contaron como salas."),
    "Cuenta los muebles de una pieza de tu casa y escribe tres oraciones con There is y There are.",
    "Escribe tres oraciones comparando las cantidades de libros de dos estantes con more than y fewer than.",
)

# ---------------------------------------------------------------- clase 2: acciones y cómo se realizan
SPORTSDAY = "«At the school sports day, Lucía runs very fast. Tomás is running slowly because his shoe is untied. The teacher shouts loudly: Good job! Pablo speaks quietly to his friend before the race.» (sports day = día del deporte, untied = desatado, shouts = grita, loudly = fuerte, quietly = en voz baja, before = antes de)"
LAB = "«In the Science lab, we work carefully. First, Ana pours the water slowly into the cup. Then Leo stirs the water gently with a spoon. Finally, they write the results neatly.» (lab = laboratorio, pours = vierte, stirs = revuelve, gently = suavemente, neatly = ordenadamente, results = resultados)"

lesson(
    OA6, 2,
    "Los textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a leer textos que describen acciones y cómo se realizan, con verbos en presente y adverbios como slowly, carefully y well. Sirve para entender instrucciones, relatos y descripciones.",
    ["Sé que run, write y speak son acciones.", "Conozco palabras como fast, slow y quiet."],
    [
        "Un adverbio de modo (adverb of manner) dice cómo se hace una acción. Muchos se forman agregando -ly a un adjetivo: slow → slowly (lentamente), careful → carefully (con cuidado), quiet → quietly (en voz baja), loud → loudly (fuerte), neat → neatly (ordenadamente). El adverbio va después del verbo: She walks slowly.",
        "Algunos adverbios son especiales. Good (bueno) se convierte en well (bien): He plays well. Fast se queda igual: She runs fast. Hard también se queda igual: They work hard (trabajan duro). Para acciones que ocurren ahora se usa el presente continuo: is/are + verbo con -ing, como Tomás is running slowly.",
        "Para comprender un texto con muchas acciones, busca quién hace cada acción (el sujeto) y cómo la hace (el adverbio). Después, comprueba si la manera concuerda con la razón: Tomás corre slowly because su zapato está desatado. La palabra because explica el porqué de la manera de hacer la acción.",
    ],
    [("adverb of manner", "adverbio de modo: cómo se hace algo"), ("slowly / quickly", "lentamente / rápido"), ("carefully", "con cuidado"), ("quietly / loudly", "en voz baja / fuerte"), ("well", "bien"), ("-ing", "terminación de acción en curso")],
    [
        ("Encontrar el adverbio", "Lee: «The baby sleeps quietly in her bed.» (baby = bebé). ¿Cómo duerme la bebé?", ["La acción es sleeps.", "El adverbio después del verbo es quietly.", "Quietly es en silencio."], "En silencio"),
        ("Formar un adverbio", "Forma el adverbio del adjetivo careful para completar: «Ana writes ___.»", ["El adjetivo es careful.", "Agrego -ly: carefully.", "Ana writes carefully."], "carefully"),
    ],
    [
        ("Decir «She plays good» en vez de «She plays well».", "Se usa el adjetivo en lugar del adverbio.", "Con verbos, good se cambia por well."),
        ("Escribir «He walks slow» en vez de «He walks slowly».", "Se usa el adjetivo en lugar del adverbio de modo.", "Para decir cómo se camina, agrega -ly: slowly."),
    ],
    [
        ("Lee: " + SPORTSDAY + " ¿Cómo corre Lucía? a) muy rápido b) lentamente", "a) muy rápido", "Dice Lucía runs very fast."),
        ("Lee: " + SPORTSDAY + " ¿Por qué Tomás corre lentamente?", "Porque tiene el zapato desatado", "Dice because his shoe is untied."),
        ("Lee: " + SPORTSDAY + " ¿Cómo grita la profesora? a) fuerte b) en voz baja", "a) fuerte", "Dice shouts loudly."),
    ],
    [
        ("Lee: " + SPORTSDAY + " ¿Quién habla en voz baja?", "Pablo", "Dice Pablo speaks quietly."),
        ("Lee: " + LAB + " ¿Cómo vierte Ana el agua? a) lentamente b) rápido", "a) lentamente", "Dice pours the water slowly."),
        ("Lee: " + LAB + " ¿Qué usa Leo para revolver el agua?", "Una cuchara", "Dice stirs the water gently with a spoon."),
    ],
    [
        ("Lee: " + LAB + " ¿Cómo escriben los resultados? a) ordenadamente b) con prisa", "a) ordenadamente", "Dice que escriben neatly."),
        ("Completa con el adverbio de good: «My sister sings ___.» Opciones: good, well.", "well", "El adverbio de good es well."),
        ("Forma el adverbio de quick y completa: «The bus goes ___ to school.» (quick = rápido)", "quickly", "Se agrega -ly a quick."),
    ],
    [
        ("Lee: " + LAB + " ¿En qué orden se hacen las tres acciones? Ordena: A) escribir los resultados B) verter el agua C) revolver.", "B, C, A", "Pour, stir y write siguen first, then y finally."),
        ("Una compañera dice que Tomás corre fast. ¿Qué adverbio usa el texto y por qué?", "Slowly, porque su zapato está desatado", "El texto dice running slowly because his shoe is untied."),
    ],
    [
        ("Lee: «Mia is painting a picture. She paints carefully, but her brother is painting fast. Her picture is neater.» (picture = dibujo, neater = más ordenado). ¿Quién pinta con más cuidado?", "Mia", "Dice that Mia paints carefully."),
        ("Cambia la oración a un adverbio: «He is a slow walker.» → «He walks ___.»", "slowly", "El adjetivo slow pasa a adverbio con -ly."),
    ],
    [("En la sala de computación hay un cartel: «Please type quietly and close the door gently.» (type = escribir en el teclado, close = cerrar, door = puerta). ¿Cómo se debe cerrar la puerta?", "Suavemente", "Gently significa suavemente.")],
    [
        ("¿Cómo se forma un adverbio de modo a partir de un adjetivo?", "Agregando -ly", "Es la regla general."),
        ("¿Qué adverbio corresponde a good?", "well", "Es un adverbio irregular."),
        ("¿Qué significa «quietly»?", "En voz baja o en silencio", "Describe cómo se hace algo."),
    ],
    task("Lee: «On Saturday, my cousins and I help in the garden. Elena waters the flowers gently. Paco works hard and digs the ground. Rosa is singing happily. The dog is sleeping quietly under a tree.» (waters = riega, flowers = flores, digs = cava, ground = suelo, happily = alegremente). Escribe cuatro oraciones en español diciendo qué hace cada persona y cómo lo hace, y subraya los cuatro adverbios en inglés.", "Elena riega las flores con suavidad (gently). Paco trabaja duro (hard). Rosa canta alegremente (happily). El perro duerme en silencio (quietly).", ["relaciona cada persona con su acción", "indica cómo la hace", "subraya los cuatro adverbios"], ["hoja con oraciones", "nota del adulto"], ["decir que Paco trabaja con cuidado", "olvidar al perro"], "Reconoce el emparejamiento correcto y repasa con la persona la diferencia entre el adjetivo y el adverbio."),
    "Observa a una persona de tu casa mientras hace una tarea y escribe tres oraciones en inglés con adverbios.",
    "Escribe cinco adverbios formados con -ly y una oración con cada uno.",
)

# ---------------------------------------------------------------- clase 3: estados de ánimo y posición
MAP = "«The park is between the school and the supermarket. The library is opposite the park. The bakery is next to the library, and the bus stop is behind the bakery. The pharmacy is in front of the school.» (between = entre, opposite = al frente de, next to = al lado de, behind = detrás de, in front of = delante de, bus stop = paradero)"
BEN = "«Before the English test, Ben feels nervous. His hands are cold and he looks at the clock all the time. After the test, he is happy and proud because he knows the answers.» (test = prueba, nervous = nervioso, hands = manos, clock = reloj, proud = orgulloso, answers = respuestas)"

lesson(
    OA6, 3,
    "Los textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a leer textos que describen estados de ánimo y la posición de objetos y lugares, con palabras como nervous, bored, between, opposite y behind. Sirve para entender cómo se sienten las personas y dónde están las cosas.",
    ["Sé que happy y sad son estados de ánimo.", "Conozco on, under y next to."],
    [
        "Los estados de ánimo (moods) se dicen con el verbo be o feel y un adjetivo: nervous (nervioso), bored (aburrido), excited (entusiasmado), angry (enojado), worried (preocupado), proud (orgulloso), tired (cansado). Las pistas del texto ayudan: si alguien mira el reloj todo el tiempo y tiene las manos frías, probablemente está nervous.",
        "Para describir la posición de objetos y lugares se usan preposiciones: between (entre dos cosas), opposite (al frente, al otro lado de la calle), next to (al lado de), behind (detrás de), in front of (delante de), on (sobre), under (debajo de), near (cerca de). Con un mapa en la mente puedes ubicar cada lugar.",
        "Cuando leas una descripción, dibuja un croquis sencillo. Marca cada lugar con una palabra y ubica los demás según las preposiciones. Si un lugar está between dos cosas, ubícalo en el centro. Leer con ayuda de un dibujo evita confusiones, especialmente con behind y in front of, que son opuestos.",
    ],
    [("nervous / bored / proud", "nervioso / aburrido / orgulloso"), ("between", "entre"), ("opposite", "al frente de"), ("behind / in front of", "detrás de / delante de"), ("next to / near", "al lado de / cerca de"), ("mood", "estado de ánimo")],
    [
        ("Deducir un estado de ánimo", "Lee: «Pía sits alone and yawns. She looks at the wall and says: There is nothing to do.» (yawns = bosteza, wall = pared, nothing = nada). ¿Cómo se siente Pía?", ["Bosteza y no sabe qué hacer.", "Eso indica falta de interés.", "Se siente bored (aburrida)."], "Aburrida (bored)"),
        ("Ubicar en un mapa", "Lee: «The school is between the church and the bank.» (church = iglesia, bank = banco). ¿Qué hay a cada lado de la escuela?", ["Between indica que está en medio de dos lugares.", "Los dos lugares son church y bank.", "A un lado la iglesia y al otro el banco."], "La iglesia y el banco"),
    ],
    [
        ("Confundir behind con in front of.", "Son posiciones opuestas.", "Behind es detrás y in front of es delante."),
        ("Decir que alguien está nervous porque sonríe.", "No se toma en cuenta la pista del texto.", "Busca pistas: mira el reloj, tiene las manos frías, dice que no puede dormir."),
    ],
    [
        ("Lee: " + BEN + " ¿Cómo se siente Ben antes de la prueba? a) nervioso b) aburrido", "a) nervioso", "Dice Ben feels nervous."),
        ("Lee: " + BEN + " ¿Qué pista muestra que está nervioso? a) mira el reloj todo el tiempo b) corre en el patio", "a) mira el reloj todo el tiempo", "Dice he looks at the clock all the time."),
        ("Lee: " + BEN + " ¿Cómo se siente después de la prueba?", "Contento y orgulloso", "Dice he is happy and proud."),
    ],
    [
        ("Lee: " + MAP + " ¿Qué hay entre el colegio y el supermercado?", "El parque", "Dice the park is between the school and the supermarket."),
        ("Lee: " + MAP + " ¿Qué está al frente del parque? a) la biblioteca b) la farmacia", "a) la biblioteca", "Dice the library is opposite the park."),
        ("Lee: " + MAP + " ¿Qué está detrás de la panadería?", "El paradero", "Dice the bus stop is behind the bakery."),
    ],
    [
        ("Lee: " + MAP + " ¿Qué está delante del colegio? a) la farmacia b) la panadería", "a) la farmacia", "Dice the pharmacy is in front of the school."),
        ("Lee: " + MAP + " ¿Qué lugar está al lado de la biblioteca?", "La panadería", "Dice the bakery is next to the library."),
        ("Lee: " + BEN + " ¿Por qué Ben está orgulloso después de la prueba?", "Porque sabía las respuestas", "Dice because he knows the answers."),
    ],
    [
        ("Lee: «The cat is under the table, between two chairs.» ¿Cuántas sillas hay en la escena y dónde está el gato respecto de ellas?", "Dos sillas; el gato está entre ellas", "Between two chairs indica que está en medio de dos."),
        ("Lee: " + MAP + " Si caminas desde el colegio hacia el supermercado, ¿qué lugar cruzas en medio?", "El parque", "El parque está entre ambos."),
    ],
    [
        ("Dibuja un croquis con: banco a la izquierda, escuela en el centro, iglesia a la derecha. ¿Qué lugar queda entre el banco y la iglesia?", "La escuela", "Between significa en el centro."),
        ("Lee: «Tomás is not happy. His team lost the game and he does not want to talk.» (team = equipo, lost = perdió). ¿Qué estado de ánimo es más probable: sad o excited?", "sad", "Perdió y no quiere hablar."),
    ],
    [("En la sala de espera de un dentista, una niña dice: «My heart is beating fast and my hands are sweaty.» (heart = corazón, beating = latiendo, sweaty = sudadas). ¿Cómo se siente probablemente? a) nerviosa b) aburrida", "a) nerviosa", "Las pistas físicas indican nerviosismo.")],
    [
        ("¿Qué significa «opposite»?", "Al frente de", "Indica un lugar al otro lado."),
        ("¿Qué estado de ánimo indica «bored»?", "Aburrimiento", "Es no tener interés."),
        ("¿Qué significa «between»?", "Entre dos cosas", "Ubica algo en el centro."),
    ],
    task("Lee: «My neighbourhood is small. The post office is next to the bank. The supermarket is opposite the bank. The playground is between the supermarket and the school. I feel proud of my neighbourhood because it is clean and quiet.» (neighbourhood = barrio, post office = correo). Dibuja un croquis con los cinco lugares y escribe dos oraciones en inglés: una para ubicar un lugar y otra con un estado de ánimo.", "Croquis con banco, correo al lado, supermercado al frente, plaza entre supermercado y colegio. The playground is between the supermarket and the school. I feel proud.", ["ubica los cinco lugares según las preposiciones", "escribe una oración con una preposición correcta", "escribe un estado de ánimo"], ["hoja con el croquis", "nota del adulto"], ["poner la plaza al lado del banco", "olvidar el colegio"], "Reconoce lo bien ubicado y revisa con la persona el significado de opposite y between."),
    "Dibuja un mapa de tu cuadra con cuatro lugares y escribe dónde está cada uno con una preposición.",
    "Escribe cinco oraciones sobre cómo te sientes en distintos lugares del colegio.",
)

# ---------------------------------------------------------------- clase 4: objetos, deportes, pasatiempos, gustos, necesidades y comparaciones
PROFILE = "«Hi! I'm Camila. My favourite pastimes are painting and playing chess. I also like swimming. I think chess is more interesting than football, but football is faster. I'd like to join the art club. I need a new box of paints.» (pastimes = pasatiempos, chess = ajedrez, interesting = interesante, faster = más rápido, join = unirme, club, paints = pinturas)"
FACTS = "«Sport facts. A football match has twenty-two players on the field. A basketball game has ten players on the court. A singles tennis match has two players.» (match = partido, field = cancha, court = cancha, singles = individual)"
BACKPACKS = "«My backpack is blue, big and light. It has two pockets and a bottle holder. My friend's backpack is red and heavier than mine, but it is smaller.» (light = liviana, pockets = bolsillos, holder = porta, heavier = más pesada, smaller = más pequeña, mine = la mía)"

lesson(
    OA6, 4,
    "Los textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a leer textos que identifican y describen objetos, deportes y pasatiempos, y que expresan gustos, opiniones, necesidades y comparaciones. Sirve para entender perfiles, anuncios y descripciones.",
    ["Sé decir I like y I don't like.", "Conozco palabras como big, small, fast y slow."],
    [
        "Para describir un objeto se usan adjetivos: blue, big, light (liviano), heavy (pesado). Para hablar de pasatiempos y deportes, se usan sustantivos y verbos con -ing: painting, playing chess, swimming. Para expresar gustos: I like..., I love..., My favourite ... is... (mi ... favorito es...). Para opinar: I think... because... Para necesidades: I need ___ (necesito). Para intenciones: I'd like to ___ (me gustaría ___).",
        "Para comparar dos cosas se usa el comparativo. Con adjetivos cortos se agrega -er y than: faster than (más rápido que), bigger than (más grande que), heavier than (más pesado que). Con adjetivos largos se usa more y than: more interesting than (más interesante que). El adjetivo good cambia a better (mejor) y bad a worse (peor).",
        "Cuando leas un perfil o un anuncio, busca tres cosas: lo que la persona tiene o hace, lo que le gusta y lo que necesita o quiere. Subraya las comparaciones y piensa cuál es la cosa que se coloca primero. En «chess is more interesting than football», el ajedrez es lo que se describe como más interesante.",
    ],
    [("pastime", "pasatiempo"), ("I need ___", "necesito ___"), ("I'd like to ___", "me gustaría ___"), ("faster than", "más rápido que"), ("more interesting than", "más interesante que"), ("better / worse", "mejor / peor")],
    [
        ("Gusto y necesidad", "Lee: «I love reading comics. I need a new book because I finished mine.» (comics = historietas, finished = terminé). ¿Qué le gusta y qué necesita?", ["I love dice lo que le gusta: leer historietas.", "I need dice lo que necesita: un libro nuevo.", "La razón es que terminó el suyo."], "Le gustan las historietas y necesita un libro nuevo"),
        ("Comparar", "Lee: «A bicycle is faster than a skateboard, but a skateboard is easier to carry.» (skateboard = patineta, easier = más fácil, carry = llevar). ¿Cuál es más rápido?", ["Busco faster than.", "A bicycle va antes de faster than.", "La bicicleta es más rápida."], "La bicicleta"),
    ],
    [
        ("Decir «more fast» en lugar de «faster».", "Se usa more con un adjetivo corto.", "Con adjetivos cortos agrega -er: fast → faster."),
        ("Confundir I need con I want.", "Se mezcla necesidad con deseo.", "I need es necesito; I want es quiero."),
    ],
    [
        ("Lee: " + PROFILE + " ¿Cuáles son los pasatiempos favoritos de Camila? a) pintar y jugar ajedrez b) correr y bailar", "a) pintar y jugar ajedrez", "Dice painting and playing chess."),
        ("Lee: " + PROFILE + " ¿Qué necesita Camila?", "Una caja nueva de pinturas", "Dice I need a new box of paints."),
        ("Lee: " + PROFILE + " ¿A qué club le gustaría unirse? a) al club de arte b) al club de natación", "a) al club de arte", "Dice I'd like to join the art club."),
    ],
    [
        ("Lee: " + PROFILE + " Para Camila, ¿qué es más interesante, el ajedrez o el fútbol?", "El ajedrez", "Dice chess is more interesting than football."),
        ("Lee: " + PROFILE + " ¿Qué es más rápido según Camila?", "El fútbol", "Dice football is faster."),
        ("Lee: " + BACKPACKS + " ¿De qué color es la mochila del narrador? a) azul b) roja", "a) azul", "Dice my backpack is blue."),
    ],
    [
        ("Lee: " + BACKPACKS + " ¿Qué mochila es más pesada?", "La mochila roja", "Dice my friend's backpack is heavier than mine."),
        ("Lee: " + BACKPACKS + " ¿Cuál mochila es más pequeña?", "La mochila roja", "Dice it is smaller."),
        arith("Lee: " + FACTS + " ¿Cuántos jugadores más tiene el fútbol que el básquetbol en la cancha?", "22-10", "Se restan los jugadores de las dos canchas."),
    ],
    [
        ("Lee: " + FACTS + " ¿Qué deporte de la lista tiene menos jugadores?", "El tenis individual", "Tiene solo dos."),
        arith("Lee: " + FACTS + " ¿Cuántos jugadores hay si se juegan a la vez un partido de fútbol, uno de básquetbol y uno de tenis?", "22+10+2", "Se suman los jugadores de los tres partidos."),
    ],
    [
        ("Un compañero dice que, para Camila, el fútbol es más interesante que el ajedrez. ¿Es correcto? Responde sí o no.", "No", "Dice que el ajedrez es más interesante; el fútbol solo es más rápido."),
        ("Elige la oración correcta: a) My backpack is lighter than yours. b) My backpack is more light than yours.", "a) My backpack is lighter than yours.", "Light es corto, así que agrega -er."),
    ],
    [("Lee este anuncio de un club: «The Chess Club needs two new members. Meetings are on Tuesday and Thursday. We think chess is better than TV because it makes you think.» (members = miembros, meetings = reuniones). ¿Cuántos nuevos miembros necesitan?", "2", "Dice needs two new members.")],
    [
        ("¿Cómo se dice «me gustaría» en inglés?", "I'd like to", "Expresa una intención."),
        ("¿Qué es el comparativo de good?", "better", "Es un comparativo irregular."),
        ("¿Qué significa «I need»?", "Necesito", "Expresa una necesidad."),
    ],
    task("Lee: «Hello! My name is Iván. My favourite sport is basketball, but I think swimming is more relaxing. I need new shoes because mine are too small. I'd like to join the school team next year.» (relaxing = relajante, shoes = zapatillas, too small = muy pequeñas, team = equipo, next year = el próximo año). Escribe: su deporte favorito, qué opina de la natación, qué necesita y qué le gustaría hacer. Luego escribe tu propia comparación con more ___ than.", "Basquetbol; la natación es más relajante; necesita zapatillas nuevas; se quiere unir al equipo. Football is more exciting than golf.", ["responde las cuatro preguntas", "usa los datos del texto", "escribe una comparación propia con more... than"], ["hoja con respuestas", "nota del adulto"], ["confundir what he needs con what he'd like", "comparación sin than"], "Reconoce la lectura completa y repasa con la persona la estructura more + adjetivo + than."),
    "Escribe una comparación entre dos objetos de tu escritorio usando -er than.",
    "Haz una ficha con tu pasatiempo favorito, algo que necesitas y algo que te gustaría hacer.",
)

# ---------------------------------------------------------------- clase 5: planes futuros y predicciones
PLAN = "«Next Saturday, our class is going to visit the beach. We are going to take sandwiches and juice. Pablo is going to bring a ball. The weather forecast says it will be sunny, so we will wear hats. We are not going to swim in the afternoon because the water will be cold.» (visit = visitar, take = llevar, forecast = pronóstico, sunny = soleado, wear = usar, hats = sombreros)"
FUTURE = "«Scientists think that in the future many cars will be electric. Cities will have more trees, and more people will use bicycles. Maybe robots will help in hospitals. Not everything will change, but life will be different.» (scientists = científicos, electric = eléctricos, trees = árboles, maybe = quizás, hospitals = hospitales, different = distinto)"

lesson(
    OA6, 5,
    "Los textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a leer textos que expresan intenciones, planes futuros y predicciones, con going to y will. Sirve para entender planes de un paseo, pronósticos y textos sobre el futuro.",
    ["Sé usar tomorrow y next week.", "Conozco verbos como visit, bring y wear."],
    [
        "Para hablar de un plan o una intención se usa be going to + verbo: We are going to visit the beach (vamos a visitar la playa). En negativo: We are not going to swim (no vamos a nadar). Las palabras de tiempo ayudan: tomorrow (mañana), next Saturday (el próximo sábado), next year (el próximo año), in the future (en el futuro).",
        "Para hacer una predicción o una decisión espontánea se usa will + verbo: It will be sunny (estará soleado). En negativo: will not o won't. Se usa con palabras como think (creo), maybe (quizás), probably (probablemente). Diferencia clave: going to expresa un plan que ya está decidido; will expresa una predicción o lo que pensamos que ocurrirá.",
        "Al leer un texto sobre el futuro, haz dos listas: planes (going to) y predicciones (will). Pregúntate quién hace el plan, cuándo y qué razón da. Si dice because, la razón explica el plan. Por ejemplo, They are not going to swim because the water will be cold: el plan se explica con una predicción.",
    ],
    [("going to + verbo", "voy a / vamos a (plan)"), ("will + verbo", "predicción: ocurrirá"), ("tomorrow / next year", "mañana / el próximo año"), ("maybe", "quizás"), ("won't", "no ocurrirá"), ("plan / prediction", "plan / predicción")],
    [
        ("Reconocer un plan", "Lee: «Tomorrow, I am going to study for the Math test.» (study = estudiar, test = prueba). ¿Qué plan expresa?", ["Veo am going to study.", "Es un plan para mañana.", "Estudiar para la prueba de Matemática."], "Estudiar para la prueba de Matemática mañana"),
        ("Reconocer una predicción", "Lee: «I think it will rain tonight.» (rain = llover, tonight = esta noche). ¿Es un plan o una predicción?", ["Veo will rain.", "Dice I think, que es una opinión sobre el futuro.", "Es una predicción."], "Una predicción"),
    ],
    [
        ("Usar will para todo plan.", "No se distingue plan de predicción.", "Un plan decidido usa going to; una predicción usa will."),
        ("Olvidar to en going to.", "Se escribe going visit.", "Es going to + verbo."),
    ],
    [
        ("Lee: " + PLAN + " ¿A dónde irá la clase? a) a la playa b) a la montaña", "a) a la playa", "Dice going to visit the beach."),
        ("Lee: " + PLAN + " ¿Qué va a llevar Pablo?", "Una pelota", "Dice Pablo is going to bring a ball."),
        ("Lee: " + PLAN + " ¿Qué dice el pronóstico? a) que estará soleado b) que lloverá", "a) que estará soleado", "Dice it will be sunny."),
    ],
    [
        ("Lee: " + PLAN + " ¿Por qué usarán sombreros?", "Porque estará soleado", "Dice it will be sunny, so we will wear hats."),
        ("Lee: " + PLAN + " ¿Por qué no van a nadar en la tarde?", "Porque el agua estará fría", "Dice because the water will be cold."),
        ("Lee: " + PLAN + " ¿Qué llevarán de comer y beber?", "Sándwiches y jugo", "Dice sandwiches and juice."),
    ],
    [
        ("Lee: " + FUTURE + " ¿Cómo serán muchos autos en el futuro? a) eléctricos b) de madera", "a) eléctricos", "Dice many cars will be electric."),
        ("Lee: " + FUTURE + " ¿Qué tendrán más las ciudades?", "Árboles", "Dice cities will have more trees."),
        ("Lee: " + FUTURE + " ¿Qué palabra muestra duda sobre los robots en hospitales? a) maybe b) will", "a) maybe", "Maybe significa quizás."),
    ],
    [
        ("Lee: " + FUTURE + " ¿Cuántas veces aparece la palabra will en el texto?", "6", "Aparece en cars will be, Cities will have, people will use, robots will help, everything will change y life will be."),
        ("Lee: " + PLAN + " Un compañero dice que la clase va a nadar en la tarde. ¿Qué dice el texto?", "Que no van a nadar en la tarde", "Dice we are not going to swim in the afternoon."),
    ],
    [
        ("¿Qué oración expresa una predicción? a) It will be cold. b) We are going to bring gloves.", "a) It will be cold.", "Will + verbo expresa una predicción."),
        ("Clasifica: «We are going to take juice» es un... a) plan b) predicción", "a) plan", "Going to expresa un plan decidido."),
    ],
    [("Lee este mensaje: «Hi! Next weekend I am going to visit my cousins in Valdivia. We are going to go by bus. I think it will rain there, so I will take my raincoat.» (cousins = primos, by bus = en bus, raincoat = impermeable). ¿Qué va a llevar y por qué?", "Un impermeable, porque cree que lloverá", "Will take se explica con I think it will rain.")],
    [
        ("¿Qué expresa «going to»?", "Un plan", "Indica una intención ya decidida."),
        ("¿Qué expresa «will»?", "Una predicción o decisión espontánea", "Habla de lo que ocurrirá."),
        ("¿Qué significa «maybe»?", "Quizás", "Expresa algo no seguro."),
    ],
    task("Lee: «This Sunday, my school is going to organise a clean-up day in the park. We are going to bring gloves and bags. The teacher thinks that about fifty people will come. Maybe it will be cold, so we will wear jackets. After the clean-up, we are going to eat together.» (organise = organizar, clean-up day = jornada de limpieza, gloves = guantes, bags = bolsas, wear = usar, together = juntos). Escribe dos planes, dos predicciones y una consecuencia que dependa de una predicción.", "Planes: limpiar el parque y comer juntos. Predicciones: vendrán unas 50 personas; quizás haga frío. Consecuencia: usarán chaquetas.", ["anota dos planes", "anota dos predicciones", "indica la consecuencia"], ["hoja con respuestas", "nota del adulto"], ["confundir plan con predicción", "olvidar la consecuencia"], "Reconoce la clasificación correcta y muestra cómo reconocer going to y will en cada oración."),
    "Escribe tres planes tuyos para el fin de semana con I am going to....",
    "Escribe tres predicciones sobre cómo será tu ciudad en el futuro, usando I think... will....",
)

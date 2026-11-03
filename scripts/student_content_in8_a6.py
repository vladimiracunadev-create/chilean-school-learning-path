"""Cuaderno del estudiante, 8.º básico Inglés (oficial), IN08 OA 08 (funciones comunicativas para la interacción).

Los cinco bloques cubren las funciones del OA: cantidades y números, gustos y permisos, comparar, describir y posesión,
tiempo, planes y frecuencia, dirección, unir ideas, condiciones y expresiones de uso común.
"""
from __future__ import annotations

from student_content_in8_a import lesson
from student_content_ma01_b import task
from student_lessons import arith

OA8 = "IN08 OA 08"
MAT = "Lápiz, una hoja y, si puedes, una persona de tu casa para practicar en voz alta; todos los datos vienen escritos."

# ================================================================== OA 8, clase 1
lesson(
    OA8, 1, MAT,
    "Aprenderé a expresar cantidades, contar y enumerar: números hasta miles, ordinales (first, third) y expresiones como a lot of, plenty of, several y all the. Sirve para hablar de cuántos o en qué lugar de una lista.",
    ["Sé contar hasta cien en inglés.", "Conozco first, second y third."],
    [
        "Para contar números grandes en inglés, nombra las centenas y luego el resto: 100 es one hundred, 250 es two hundred and fifty, 340 es three hundred and forty y 709 es seven hundred and nine. Se usa and antes de las decenas y de las unidades. Hundred no lleva s cuando va después de un número: two hundred students (no two hundreds). Para 1.250 se dice one thousand two hundred and fifty.",
        "Los ordinales dicen la posición: first (1.º), second (2.º), third (3.º), fourth (4.º), fifth (5.º), sixth, seventh, eighth, ninth y tenth (10.º). Se usan para enumerar: She is the first; He is the third in line. Para listar ideas puedes usar first, second, third y last.",
        "Las expresiones de cantidad evitan dar un número exacto. A lot of significa mucho o muchos: There are a lot of people. Plenty of significa más que suficiente: There is plenty of food. Several significa varios y solo se usa con cosas que se cuentan: Several students came. All the significa todos: All the students are here. Observa que several va con plural y plenty of y a lot of sirven para cosas contables e incontables.",
    ],
    [("two hundred and fifty", "doscientos cincuenta (250)"), ("first, second, third", "primero, segundo, tercero"), ("a lot of", "mucho(s)"), ("plenty of", "más que suficiente"), ("several", "varios"), ("all the", "todos los")],
    [
        ("Decir un número", "Escribe en inglés el número 250.", ["250 son 200 más 50.", "200 es two hundred; 50 es fifty.", "Se une con and: two hundred and fifty."], "Two hundred and fifty"),
        ("Decir una posición", "En una fila, Lola está en el tercer lugar. ¿Cómo dices su posición en inglés?", ["El número 3 es three.", "El ordinal de three es third.", "Lola is the third."], "Third"),
    ],
    [
        ("Decir «two hundreds».", "Hundred no lleva s después de un número.", "Di two hundred."),
        ("Decir «the three» para tercero.", "Para la posición se usa el ordinal.", "Di the third."),
    ],
    [
        ("¿Qué número es «one hundred and five»? a) 105 b) 150", "a) 105", "One hundred es 100 y five es 5."),
        ("¿Cuál es el ordinal de 3? a) third b) three", "a) third", "Third indica la posición."),
        ("¿Qué significa «several»? a) varios b) ninguno", "a) varios", "Several indica más de dos."),
    ],
    [
        ("¿Qué número es «seven hundred and nine»? a) 709 b) 790", "a) 709", "Seven hundred es 700 y nine es 9."),
        ("¿Qué ordinal es 5.º? a) fifth b) five", "a) fifth", "Fifth es el ordinal de five."),
        ("¿Qué significa «plenty of»? a) más que suficiente b) casi nada", "a) más que suficiente", "There is plenty of food significa que hay comida de sobra."),
    ],
    [
        arith("En un patio hay 120 niños y 130 niñas. ¿Cuántos estudiantes hay en total? (Se dice two hundred and fifty.)", "120+130", "Se suman niños y niñas.", " estudiantes"),
        ("¿Qué oración es correcta? a) Several students came. b) Several water is here.", "a) Several students came.", "Several se usa con cosas que se cuentan, en plural."),
        ("¿Cómo se dice 1.250? a) one thousand two hundred and fifty b) one thousand and two fifty", "a) one thousand two hundred and fifty", "Se dice el millar, la centena y luego and las decenas."),
    ],
    [
        ("En una carrera, Eli llegó tercero y Teo llegó segundo. ¿Quién llegó antes? a) Teo, que fue second b) Eli, que fue third", "a) Teo, que fue second", "Second va antes que third."),
        ("Ana escribió «two hundreds students». ¿Cuál es la forma correcta? a) two hundred students b) twos hundred students", "a) two hundred students", "Hundred no lleva s después de un número."),
    ],
    [
        ("Escribe en inglés los ordinales de 1.º, 3.º y 4.º, separados por comas.", "first, third, fourth", "Son los ordinales de 1, 3 y 4."),
        arith("Una biblioteca tiene one thousand two hundred libros (1.200) y dona two hundred and fifty (250). ¿Cuántos libros quedan?", "1200-250", "Se resta lo que se dona.", " libros"),
    ],
    [("En una feria del colegio hay plenty of comida y several mesas de juegos. ¿Qué significa? a) hay comida de sobra y varias mesas de juegos b) hay poca comida y una mesa", "a) hay comida de sobra y varias mesas de juegos", "Plenty of indica abundancia y several indica varios.")],
    [
        ("¿Cómo se dice 340 en inglés?", "Three hundred and forty", "Se nombra la centena y luego and las decenas."),
        ("En Inglés de 8.º (OA 8, clase 1): ¿Qué quiere decir «all the»?", "Todos los", "All the students significa todos los estudiantes."),
        ("¿Para qué sirven los ordinales?", "Para decir la posición", "Por ejemplo, first, second y third."),
    ],
    task("Con estos datos de ejemplo escribe cuatro frases en inglés: 1) hay 360 sillas en el gimnasio, 2) tu curso quedó en cuarto lugar, 3) hay mucha gente en la plaza y 4) vinieron varios apoderados.", "There are three hundred and sixty chairs in the gym. Our class is fourth. There are a lot of people in the square. Several parents came.", ["escribe el número 360 en palabras", "usa el ordinal fourth", "usa a lot of y several correctamente"], ["hoja con cuatro frases", "nota de una persona de tu casa"], ["three hundreds sixty", "several water"], "Reconoce las frases bien formadas y corrige solo el número o el ordinal."),
    "Di en voz alta los números 105, 250, 340 y 709 en inglés.",
    "Escribe cinco frases sobre tu colegio con un número grande, un ordinal y una expresión de cantidad.",
)

# ------------------------------------------------------------------ OA 8, clase 2
lesson(
    OA8, 2, MAT,
    "Aprenderé a expresar gustos y preferencias (love, enjoy, hate, don't mind, would like) y a pedir permiso y dar consejos (Can I...?, You should...). Sirve para decir lo que me gusta, pedir con cortesía y aconsejar.",
    ["Sé decir I like y I don't like.", "Conozco verbos como swim, read y cook."],
    [
        "Para hablar de gustos usa verbos de preferencia seguidos de un verbo con -ing. I love swimming (me encanta nadar), I enjoy reading (disfruto leer), I don't mind cooking (no me molesta cocinar) e I hate waiting (odio esperar). Del más positivo al más negativo: love, enjoy, don't mind, hate. Con he y she: She enjoys drawing; He doesn't mind waiting.",
        "Para pedir o decir lo que quieres con cortesía usa I'd like (me gustaría): I'd like a juice, please; I'd like to go to the park. I'd like es más amable que I want. Para pedir permiso usa Can I...?: Can I go out? Can I borrow your pen? Se responde Yes, you can o Sorry, you can't.",
        "Para dar consejos usa should (deberías) o shouldn't (no deberías) con el verbo en forma base: You should drink water; You shouldn't walk in the rain without an umbrella. Después de should y can no se agrega -s ni to. Por ejemplo, no se dice You should to drink.",
    ],
    [("love / enjoy", "me encanta / disfruto"), ("don't mind", "no me molesta"), ("hate", "odiar"), ("I'd like", "me gustaría"), ("Can I...?", "¿Puedo...?"), ("should / shouldn't", "deberías / no deberías")],
    [
        ("Gusto con -ing", "Dices que disfrutas nadar. ¿Cómo lo dices en inglés?", ["El verbo enjoy va con otro verbo con -ing.", "Swim se escribe swimming.", "I enjoy swimming."], "I enjoy swimming"),
        ("Pedir permiso", "Quieres pedir permiso para salir. ¿Qué dices y cómo te pueden responder?", ["Se usa Can I...?", "Se pregunta Can I go out?", "Pueden responder Yes, you can o Sorry, you can't."], "Can I go out? / Yes, you can o Sorry, you can't"),
    ],
    [
        ("Decir «I enjoy to swim».", "Después de enjoy el verbo lleva -ing.", "Di I enjoy swimming."),
        ("Decir «You should to drink water».", "Después de should el verbo va en forma base, sin to.", "Di You should drink water."),
    ],
    [
        ("¿Qué frase es correcta? a) I enjoy reading. b) I enjoy read.", "a) I enjoy reading.", "Enjoy va con verbo + -ing."),
        ("¿Qué significa «I hate waiting»? a) odio esperar b) me encanta esperar", "a) odio esperar", "Hate significa odiar."),
        ("¿Qué significa «I don't mind cooking»? a) no me molesta cocinar b) odio cocinar", "a) no me molesta cocinar", "Don't mind indica que es aceptable para ti."),
    ],
    [
        ("¿Cuál es más fuerte, «love» o «enjoy»? a) love b) enjoy", "a) love", "Love expresa un gusto más intenso."),
        ("¿Cuál es una forma cortés de pedir un jugo? a) I'd like a juice, please. b) I want a juice.", "a) I'd like a juice, please.", "I'd like es más cortés que I want."),
        ("Pides permiso. ¿Qué respuesta lo acepta? a) Yes, you can. b) Sorry, you can't.", "a) Yes, you can.", "You can permite hacer algo."),
    ],
    [
        ("Completa: «She ___ waiting» (no le molesta). a) doesn't mind b) don't mind", "a) doesn't mind", "Con she se usa doesn't."),
        ("Completa: «You ___ walk in the rain without an umbrella.» a) shouldn't b) don't should", "a) shouldn't", "Shouldn't da un consejo de no hacer algo."),
        ("Completa: «I'd like ___ to the park.» a) to go b) going", "a) to go", "I'd like se usa con to + verbo."),
    ],
    [
        ("¿Qué frase da un consejo? a) You should drink water. b) You drink water yesterday.", "a) You should drink water.", "Should + verbo da un consejo."),
        ("Elena dice «I'd like to going to the park». ¿Qué corriges? a) I'd like to go to the park b) I'd like going to the park", "a) I'd like to go to the park", "Después de to va el verbo en forma base."),
    ],
    [
        ("Datos de ejemplo: Ana ama nadar y odia cocinar; Beto disfruta cocinar y no le molesta nadar. ¿A quién no le molesta nadar? a) a Beto b) a Ana", "a) a Beto", "Beto dice I don't mind swimming."),
        ("¿Qué respuesta rechaza con cortesía una petición de «Can I borrow your pen?»? a) Sorry, you can't. I need it. b) Yes, you can.", "a) Sorry, you can't. I need it.", "Niega el permiso con una razón."),
    ],
    [("En un restaurante quieres pedir una sopa con cortesía. ¿Qué dices? a) I'd like a soup, please. b) Soup now.", "a) I'd like a soup, please.", "I'd like y please son una forma cortés de pedir.")],
    [
        ("En Inglés de 8.º (OA 8, clase 2): ¿Qué forma del verbo sigue a enjoy, love y hate?", "El verbo con -ing", "Por ejemplo, I enjoy swimming."),
        ("En Inglés de 8.º (OA 8, clase 2): ¿Qué frase pide permiso?", "Can I...?", "Por ejemplo, Can I go out?"),
        ("¿Qué usas para dar un consejo?", "Should / shouldn't", "You should drink water."),
    ],
    task("Escribe cinco frases en inglés: 1) algo que amas hacer con -ing, 2) algo que no te molesta, 3) algo que odias, 4) una petición con I'd like y 5) un consejo con shouldn't para un amigo que va a salir en un día de lluvia.", "I love drawing. I don't mind washing the dishes. I hate waiting. I'd like a glass of water, please. You shouldn't go out without an umbrella.", ["usa -ing después de love, hate y don't mind", "usa I'd like con cortesía", "usa shouldn't con el verbo en forma base"], ["hoja con cinco frases", "nota de una persona de tu casa"], ["I love to drawing", "You shouldn't to go"], "Reconoce las frases correctas y corrige las formas con -ing o con to."),
    "Practica con una persona de tu casa pedir permiso con Can I... y responder de dos maneras.",
    "Escribe un diálogo de cuatro líneas en que alguien pide permiso y otra persona da un consejo.",
)

# ------------------------------------------------------------------ OA 8, clase 3
lesson(
    OA8, 3, MAT,
    "Aprenderé a comparar con -er/-est y more/most, a identificar y describir personas y objetos, y a hablar de posesión con Whose...? e It's mine/hers. Sirve para describir, comparar y decir de quién es algo.",
    ["Sé que -er y more se usan para comparar.", "Conozco colores y adjetivos como big, small y tall."],
    [
        "Para comparar dos cosas, los adjetivos cortos llevan -er y than: cheaper than, bigger than, heavier than. Si el adjetivo termina en una vocal y una consonante, se duplica la consonante (big, bigger); si termina en y, cambia a ier (happy, happier). Con tres o más cosas, se usa the + -est: the cheapest, the biggest. Los adjetivos largos usan more y the most: more expensive, the most expensive. Hay formas irregulares: good, better, the best; bad, worse, the worst.",
        "Para describir objetos, lugares y personas, ordena los adjetivos así: tamaño y luego color: a big brown building. Para nacionalidades usa be: They are French. Para identificar personas usa in con la ropa (the man in the red coat) y with con rasgos (the woman with long hair).",
        "Para hablar de posesión pregunta Whose wallet is this? y responde con un pronombre: mine (mío), yours (tuyo o suyo), his (de él), hers (de ella), ours (nuestro), theirs (de ellos). También puedes decir It belongs to a friend of mine. Para escoger entre varios, Which is yours? (¿Cuál es el tuyo?).",
    ],
    [("cheaper / the cheapest", "más barato / el más barato"), ("more expensive", "más caro"), ("better / the best", "mejor / el mejor"), ("a big brown building", "un edificio grande y café"), ("Whose...?", "¿De quién...?"), ("mine, yours, hers, theirs", "mío, tuyo, de ella, de ellos")],
    [
        ("Comparar con tres", "Tres supermercados venden arroz a 1.800, 1.500 y 2.100 pesos. ¿Cómo dices que el de 1.500 es el más barato?", ["Cheap es un adjetivo corto.", "Con tres cosas se usa the + -est.", "Es the cheapest."], "It is the cheapest"),
        ("Posesión", "Una billetera es de Ema. Te preguntan «Whose wallet is this?». ¿Qué respondes con un pronombre?", ["La billetera pertenece a una mujer.", "El pronombre para ella es hers.", "It's hers."], "It's hers"),
    ],
    [
        ("Decir «more cheap» en vez de cheaper.", "Cheap es corto y lleva -er.", "Di cheaper than."),
        ("Decir «a brown big dog».", "El orden es tamaño y luego color.", "Di a big brown dog."),
    ],
    [
        ("¿Cuál es el comparativo de «big»? a) bigger b) more big", "a) bigger", "Big duplica la g y lleva -er."),
        ("¿Cuál es el superlativo de «cheap»? a) the cheapest b) the most cheap", "a) the cheapest", "Cheap es un adjetivo corto."),
        ("«This pen belongs to a friend of mine.» ¿Qué significa? a) el bolígrafo es de un amigo mío b) el bolígrafo es mía", "a) el bolígrafo es de un amigo mío", "Belongs to es pertenecer a, y a friend of mine es un amigo mío."),
    ],
    [
        ("¿Cuál es el comparativo de «happy»? a) happier b) more happy", "a) happier", "La y cambia a ier."),
        ("¿Qué frase es correcta? a) This bag is more expensive than that bag. b) This bag is expensiver than that bag.", "a) This bag is more expensive than that bag.", "Expensive es largo y usa more."),
        ("Completa: «Whose wallet is this? It's ___» (de ella). a) hers b) his", "a) hers", "Hers es de ella."),
    ],
    [
        ("Completa: «This supermarket is the ___ in the city» (cheap). a) cheapest b) most cheap", "a) cheapest", "Cheap lleva the + -est."),
        ("Completa: «The bag is ___ than the box» (heavy). a) heavier b) more heavy", "a) heavier", "Heavy cambia y por i y lleva -er."),
        ("¿Qué frase ordena bien los adjetivos? a) a big brown dog b) a brown big dog", "a) a big brown dog", "El tamaño va antes del color."),
    ],
    [
        ("Para identificar a una niña por su pelo, ¿qué frase usas? a) The girl with long hair b) The girl in long hair", "a) The girl with long hair", "Con rasgos se usa with; con ropa se usa in."),
        ("Dos mochilas: la roja es de Ana y la azul es de Beto. Beto responde a «Which is yours?». ¿Qué dice? a) The blue one is mine. b) The blue one is yours.", "a) The blue one is mine.", "Beto habla de su mochila; usa mine."),
    ],
    [
        ("Datos de ejemplo: el supermercado A vende arroz a 2.400 pesos, B a 1.900 pesos y C a 2.700 pesos. ¿Qué frase es correcta? a) C is the most expensive. b) C is the cheapest.", "a) C is the most expensive.", "2.700 es el mayor precio."),
        ("¿Cuál es el superlativo de «good»? a) the best b) the goodest", "a) the best", "Good es irregular: better, the best."),
    ],
    [("Perdiste tu chaqueta y la describes a la encargada: «It's a small blue jacket with a white zip». ¿Qué orden de adjetivos usaste? a) tamaño y luego color b) color y luego tamaño", "a) tamaño y luego color", "Small va antes de blue.")],
    [
        ("¿Cómo se forma el superlativo de un adjetivo corto?", "The + adjetivo + -est", "Por ejemplo, the cheapest."),
        ("En Inglés de 8.º (OA 8, clase 3): ¿Qué significa «hers»?", "De ella", "Hers es el pronombre posesivo de she."),
        ("¿Qué orden llevan los adjetivos de tamaño y color?", "Primero tamaño y luego color", "A big brown building."),
    ],
    task("Con estos datos de ejemplo escribe cuatro frases en inglés: 1) una billetera es de Julia (responde con hers), 2) una torta cuesta 6.000 pesos, otra 8.000 pesos (compara con cheaper o more expensive), 3) la torta más cara de la tienda cuesta 9.500 pesos (superlativo), y 4) describe a un niño con camiseta roja y pelo corto.", "It's hers. The first cake is cheaper than the second one. The nine thousand five hundred peso cake is the most expensive in the shop. The boy in the red T-shirt has short hair.", ["usa un pronombre posesivo", "usa un comparativo y un superlativo", "describe usando in y with"], ["hoja con cuatro frases", "nota de una persona de tu casa"], ["more cheap", "a red big T-shirt"], "Reconoce las formas correctas y corrige el comparativo o el orden de los adjetivos."),
    "Describe a una persona de tu casa con la estructura The man/woman in... o with...",
    "Escribe cinco comparaciones de objetos de tu pieza usando -er than, more... than y the -est.",
)

# ------------------------------------------------------------------ OA 8, clase 4
lesson(
    OA8, 4, MAT,
    "Aprenderé a hablar del tiempo (on, at, in), a expresar planes y predicciones (be going to, presente continuo, will), a señalar frecuencia (never, sometimes, always) y a ordenar acciones (first, next, then, last, finally). Sirve para organizar mi agenda y contar mi rutina.",
    ["Sé decir los días y los meses en inglés.", "Conozco will y first."],
    [
        "Para preguntar por el tiempo usa When: When is the party? Se responde con una preposición. On va con días: on Saturday. At va con horas: at ten o'clock. In va con meses y partes del día: in December, in the morning. Con tomorrow, next week o next year no se usa preposición: The test is tomorrow.",
        "Para planes y predicciones hay tres formas. Be going to expresa un plan: I'm going to visit my cousin. El presente continuo expresa un plan acordado: I'm going to Easter Island next week; She's arriving tomorrow morning. Will expresa una predicción: Man will land on Mars in the future.",
        "Los adverbios de frecuencia dicen cuántas veces: never (nunca), sometimes (a veces), usually (generalmente), always (siempre). Van antes del verbo principal (I always visit) y después de be (She is never late). Para ordenar acciones usa first (primero), next (a continuación), then (después), last (por último) y finally (finalmente).",
    ],
    [("When...?", "¿Cuándo...?"), ("on / at / in", "con días / con horas / con meses"), ("I'm going to + verbo", "voy a... (plan)"), ("will", "predicción futura"), ("never, sometimes, always", "nunca, a veces, siempre"), ("first, next, then, last", "primero, a continuación, después, por último")],
    [
        ("Elegir la preposición", "Completa con on, at o in: «The concert is ___ December.»", ["December es un mes.", "Los meses llevan in.", "Es in December."], "In"),
        ("Ubicar el adverbio", "Ordena las palabras: She / never / is / late. ¿Dónde va never con el verbo be?", ["Con be, el adverbio va después de be.", "Never va después de is.", "She is never late."], "She is never late"),
    ],
    [
        ("Decir «on December».", "Los meses llevan in.", "Di in December."),
        ("Decir «She never is late».", "Con be el adverbio de frecuencia va después del verbo.", "Di She is never late."),
    ],
    [
        ("Completa: «The party is ___ Saturday.» a) on b) at", "a) on", "Los días llevan on."),
        ("Completa: «The meeting is ___ ten o'clock.» a) at b) on", "a) at", "Las horas llevan at."),
        ("Completa: «The concert is ___ July.» a) in b) on", "a) in", "Los meses llevan in."),
    ],
    [
        ("¿Qué frase habla de un plan? a) I'm going to the beach next week. b) I go to the beach yesterday.", "a) I'm going to the beach next week.", "Next week y el presente continuo expresan un plan."),
        ("¿Cuál frase tiene bien puesto el adverbio de frecuencia? a) I always visit my cousin. b) I visit always my cousin.", "a) I always visit my cousin.", "El adverbio va antes del verbo principal."),
        ("¿Qué frase es correcta? a) The test is tomorrow. b) The test is on tomorrow.", "a) The test is tomorrow.", "Tomorrow no lleva preposición."),
    ],
    [
        ("Completa: «Man ___ land on Mars in the future» (predicción). a) will b) is landing", "a) will", "Will expresa una predicción."),
        ("Completa: «___ is the party? On Saturday.» a) When b) Whose", "a) When", "On Saturday responde por el tiempo."),
        ("Ordena con números: (1) Finally, I turn off the lights. (2) First, I close the windows. (3) Then, I lock the door.", "2, 3, 1", "First va primero, then después y finally al final."),
    ],
    [
        ("Pedro visita a su primo dos veces al año. ¿Qué adverbio es mejor? a) sometimes b) always", "a) sometimes", "Dos veces al año es a veces."),
        ("«She's arriving tomorrow morning» expresa... a) un plan acordado en el futuro b) una costumbre del pasado", "a) un plan acordado en el futuro", "El presente continuo con tomorrow expresa un plan."),
    ],
    [
        ("Datos de ejemplo: Teo va al gimnasio de lunes a viernes, todos los días de la semana escolar. ¿Qué adverbio completa «Teo ___ goes to the gym on weekdays»? a) always b) never", "a) always", "Va todos los días."),
        ("Ordena de menos a más frecuente: always, never, sometimes. Escribe las tres palabras en orden.", "never, sometimes, always", "Nunca es 0, a veces es poco y siempre es todos."),
    ],
    [("Tu agenda de ejemplo dice: «Excursión: miércoles, 8:30». Alguien pregunta «When is the school trip?». ¿Qué respondes? a) It is on Wednesday at half past eight. b) It is in Wednesday on half past eight.", "a) It is on Wednesday at half past eight.", "On para el día y at para la hora.")],
    [
        ("¿Qué preposición va con los meses?", "In", "Los meses llevan in, como in December."),
        ("En Inglés de 8.º (OA 8, clase 4): ¿Dónde va el adverbio de frecuencia con el verbo be?", "Después de be", "She is never late."),
        ("En Inglés de 8.º (OA 8, clase 4): ¿qué palabra usas para ordenar la última acción de tu rutina?", "Finally", "Finally significa por último o finalmente."),
    ],
    task("Con esta agenda de ejemplo escribe cuatro frases en inglés: lunes, 9:00, entrenamiento de fútbol (siempre); junio, viaje a la playa (plan); jueves, prueba de inglés; mañana, visita al museo (plan acordado).", "I always play football on Monday at nine o'clock. In June, I'm going to the beach. The English test is on Thursday. I'm visiting the museum tomorrow.", ["usa on, at e in correctamente", "usa un adverbio de frecuencia", "expresa un plan con going to o presente continuo"], ["hoja con cuatro frases", "nota de una persona de tu casa"], ["on June", "I visit always"], "Reconoce las frases correctas y revisa las preposiciones."),
    "Pregunta a una persona de tu casa When is...? sobre tres eventos y responde con on, at o in.",
    "Escribe tu rutina de un día con first, next, then, last y un adverbio de frecuencia.",
)

# ------------------------------------------------------------------ OA 8, clase 5
lesson(
    OA8, 5, MAT,
    "Aprenderé a indicar dirección (into, out of, from, to), a unir ideas (and then, so, until, also), a expresar condiciones (If you cook, I'll help you) y a usar expresiones de uso común (catch a bus, get on/off, let's, tired of, maybe, download). Sirve para dar indicaciones y conversar con naturalidad.",
    ["Sé usar will para el futuro.", "Conozco verbos como walk, go y come."],
    [
        "Para indicar dirección usa preposiciones. Into es entrar en un lugar: She walks into the bank. Out of es salir de un lugar: He comes out of the store. From dice desde dónde: I come from the supermarket. To dice hacia dónde: I go to school. Observa la diferencia entre to y into: go to school indica el destino; walk into the bank indica entrar.",
        "Para unir ideas usa and then (y después): He came and then we watched the film. So da un resultado: It was far, so we took the bus. Until marca un límite: I'll wait until Monday. Also agrega algo: The library is the best in town. It also has a quiet room. Para una condición usa If + presente, will + verbo: If you cook, I'll help you; If it rains, we will stay at home.",
        "Algunas expresiones de uso común se aprenden como bloques: catch a bus/coach/train (tomar un bus o tren), get on/off the bus (subir/bajar del bus), arrive at the station (llegar a la estación), look at (mirar), go on holidays (irse de vacaciones), tired of (cansado de), maybe (quizás), download (descargar), let's... (hagamos...) y that's OK (está bien). Una palabra compuesta junta dos palabras en una: classroom (class + room), football (foot + ball), homework (home + work) y download (down + load).",
    ],
    [("into / out of", "entrar en / salir de"), ("from / to", "desde / hacia"), ("and then", "y después"), ("If you cook, I'll help you", "si cocinas, te ayudaré"), ("catch / get on / get off", "tomar / subirse / bajarse"), ("tired of, maybe, download", "cansado de, quizás, descargar")],
    [
        ("Elegir la preposición", "Completa: «She walks ___ the bank.» (entra al banco) ¿into o out of?", ["Entrar en un lugar se dice into.", "Out of significa salir.", "La respuesta es into."], "Into"),
        ("Condición", "Dices: «Si estudias, aprobarás». ¿Cómo lo dices en inglés con if y will?", ["La condición usa If + presente.", "El resultado usa will + verbo.", "If you study, you will pass."], "If you study, you will pass"),
    ],
    [
        ("Decir «If you will study, you pass».", "La condición va en presente y el resultado con will.", "Di If you study, you will pass."),
        ("Usar to en lugar de into para entrar.", "To indica destino; into indica entrar en un lugar.", "Di walk into the bank."),
    ],
    [
        ("Completa: «He comes ___ the store» (sale de la tienda). a) out of b) into", "a) out of", "Out of significa salir de."),
        ("Completa: «I go ___ school every day.» a) to b) into", "a) to", "Go to school indica el destino."),
        ("Completa: «If you cook, I ___ help you.» a) will b) did", "a) will", "El resultado de la condición usa will."),
    ],
    [
        ("Completa: «It was far, ___ we took the bus.» a) so b) until", "a) so", "Tomar el bus es el resultado de que estaba lejos."),
        ("Completa: «I'll wait ___ Monday.» a) until b) because", "a) until", "Until marca el límite de tiempo."),
        ("Un amigo dice: «We go on holidays in February». ¿Qué hará en febrero? a) irse de vacaciones b) ir a clases", "a) irse de vacaciones", "Go on holidays es irse de vacaciones."),
    ],
    [
        ("Un profesor dice: «Look at the board». ¿Qué debes hacer? a) mirar la pizarra b) escribir en la pizarra", "a) mirar la pizarra", "Look at es mirar."),
        ("Preguntas «Can I sit here?» y te responden «That's OK». ¿Qué te dijeron? a) que está bien, que puedes sentarte b) que no puedes sentarte", "a) que está bien, que puedes sentarte", "That's OK significa está bien."),
        ("¿Qué significa «I'm tired of waiting»? a) estoy cansado de esperar b) estoy contento de esperar", "a) estoy cansado de esperar", "Tired of expresa que ya cansa."),
    ],
    [
        ("Elena dice: «If you will cook, I help». ¿Cuál es la forma correcta? a) If you cook, I'll help b) If you will cook, I will help", "a) If you cook, I'll help", "Después de if va el presente."),
        ("¿Qué frase es correcta? a) We arrive at the station at nine. b) We arrive to the station at nine.", "a) We arrive at the station at nine.", "Arrive at es llegar a un lugar; arrive to es un error frecuente."),
    ],
    [
        ("Instrucciones: «Get on the 21 bus, get off at the station, walk into the main hall, then go out of the building by the north door». ¿Qué haces después de entrar al hall? a) salir del edificio por la puerta norte b) subir al bus 21", "a) salir del edificio por la puerta norte", "Then go out of the building viene después de walk into."),
        ("Une las dos palabras «home» y «work» para formar una palabra compuesta. ¿Cuál es? a) homework b) workhome", "a) homework", "Home + work forman homework (tarea)."),
    ],
    [("Un amigo te dice: «The film is at six. It is far, so let's catch the 14 bus. If we leave now, we'll arrive on time». ¿Qué debes hacer para llegar a tiempo? a) salir ahora y tomar el bus 14 b) esperar hasta las seis", "a) salir ahora y tomar el bus 14", "La condición If we leave now lleva al resultado we'll arrive on time.")],
    [
        ("¿Qué estructura tiene una condición?", "If + presente, will + verbo", "If you cook, I'll help you."),
        ("En Inglés de 8.º (OA 8, clase 5): ¿Qué significa «out of»?", "Salir de", "He comes out of the store."),
        ("¿Qué significa «let's»?", "Hagamos algo juntos", "Let's go significa vamos."),
    ],
    task("Con estos datos de ejemplo escribe cuatro frases en inglés: 1) una condición (si llueve, te quedas en casa), 2) un resultado con so (estaba lejos, tomaste un bus), 3) una dirección con into o out of y 4) una frase con let's y maybe.", "If it rains, I will stay at home. It was far, so I took the bus. She walks out of the store. Let's go to the park. Maybe we can play football.", ["usa If + presente y will", "usa so correctamente", "usa into u out of"], ["hoja con cuatro frases", "nota de una persona de tu casa"], ["If it will rain", "walk to the bank para entrar"], "Reconoce las frases correctas y corrige el tiempo verbal después de if."),
    "Di en voz alta tres condiciones con if y sus resultados con will.",
    "Escribe un diálogo de cinco líneas en que dos amigos planean cómo llegar a un lugar usando catch, get off, if y let's.",
)

"""Cuaderno del estudiante, 6.º básico Inglés (propuesta): EN06 OA 14 (escribir para realizar funciones) y OA 15 (proceso de escritura).

Los textos en inglés son originales, breves y llevan pista en español. Cada palabra o estructura se enseña en la propia clase
antes de usarla. Las herramientas (diccionario en línea, procesador de textos) se explican y se simulan con ejemplos escritos,
de modo que el cuaderno se puede resolver también en papel.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA14 = "EN06 OA 14"
OA15 = "EN06 OA 15"


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


# ================================================================ OA 14 clase 1: escribir preguntas
lesson(
    OA14, 1,
    "Las oraciones y tarjetas escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir preguntas con Who, How much, How many, Can y Where, con el orden de palabras y la puntuación correcta. Sirve para pedir información por escrito.",
    ["Conozco las palabras Who, Where y Can.", "Sé qué es un signo de interrogación."],
    [
        "En inglés una pregunta escrita empieza con mayúscula y termina con un solo signo de interrogación (?). No lleva el signo de apertura (¿) como en español. Las palabras de pregunta van al comienzo: Who (quién), How much (cuánto, precio o cantidad que no se cuenta), How many (cuántos, cosas que se cuentan), Where (dónde).",
        "El orden es: palabra de pregunta + is/are/do + sujeto + resto. Ejemplos: «Who is your teacher?», «How many pencils do you have?», «How much is the notebook?», «Where is the library?» Con Can el verbo va primero: «Can you swim?» (no «You can swim?»).",
        "Para responder por escrito se contesta con el dato que pide la palabra: Who → una persona, How many → un número, How much → un precio o cantidad, Where → un lugar, Can → Yes, I can. / No, I can't.",
    ],
    [("question mark (?)", "signo de interrogación"), ("Who is…?", "¿Quién es…?"), ("How many…?", "¿Cuántos…?"), ("How much…?", "¿Cuánto…?"), ("Where is…?", "¿Dónde está…?"), ("Can you…?", "¿Puedes…?")],
    [
        ("Ordenar una pregunta", "Ordena las palabras para formar una pregunta: is / Where / the / gym ?", ["Where es la palabra de pregunta, va primero.", "Luego is y el sujeto the gym.", "Se cierra con ?."], "Where is the gym?"),
        ("Corregir una pregunta", "Corrige: «you can swim?»", ["Can va primero.", "La pregunta empieza con mayúscula.", "Se escribe Can you swim?"], "Can you swim?"),
    ],
    [
        ("Escribir «¿Where is the park?» con signo de apertura.", "Se copia la puntuación del español.", "En inglés solo se escribe el signo final: Where is the park?"),
        ("Usar How many con precios.", "Se confunde cantidad con precio.", "Para precios usa How much."),
    ],
    [
        ("¿Qué signo cierra una pregunta en inglés?", "?", "Solo se escribe el signo final."),
        ("¿Qué significa «How many»?", "Cuántos", "Se usa con cosas que se cuentan."),
        ("¿Cuál es correcta? a) Where the school is? b) Where is the school?", "b", "El verbo is va antes del sujeto."),
    ],
    [
        ("Ordena: you / Can / play / chess ?", "Can you play chess?", "Can va primero."),
        ("Completa: «___ is the librarian?» La respuesta es Mr. Soto. Opciones: Who, Where.", "Who", "La respuesta es una persona."),
        ("Completa: «How ___ is the juice?» La respuesta es 600 pesos. Opciones: much, many.", "much", "Un precio se pregunta con How much."),
    ],
    [
        ("Escribe la pregunta para esta respuesta: «There are 25 students.» Completa: «How ___ students are there?»", "many", "Los estudiantes se cuentan."),
        ("Escribe la pregunta: pides el lugar de la biblioteca. Completa: «___ is the library?»", "Where", "Where pide un lugar."),
        ("Corrige y escribe la pregunta: «who is your friend.»", "Who is your friend?", "Falta la mayúscula y el signo ? final."),
    ],
    [
        ("¿Qué pregunta responde «I have six books»? a) How many books do you have? b) How much is the book?", "a", "Six es un número de cosas que se cuentan."),
        ("¿Qué pregunta responde «Yes, I can»? a) Can you sing? b) Where is the stage?", "a", "Es la respuesta corta a una pregunta con Can."),
    ],
    [
        ("Ordena las palabras para formar la pregunta: do / How / you / many / have / books ? ¿Cuál palabra queda en tercer lugar?", "books", "La pregunta es How many books do you have?, con How, many y books en los tres primeros lugares."),
        ("Cuenta las palabras de «How many pencils do you have?» Escribe solo el número.", "6", "How, many, pencils, do, you, have son seis palabras."),
    ],
    [("Quieres saber el precio de una pelota en la tienda de la escuela. ¿Qué escribes? a) How much is the ball? b) How many is the ball?", "a", "El precio se pregunta con How much.")],
    [
        ("¿Dónde va el signo de interrogación en inglés?", "Solo al final", "No se escribe el de apertura."),
        ("¿Qué letra inicia una pregunta?", "Mayúscula", "Toda oración empieza con mayúscula."),
        ("¿Qué palabra de pregunta pide un lugar?", "Where", "Where significa dónde."),
    ],
    task("Lee estas respuestas: 1) Ms. Rojas. 2) Twelve. 3) 500 pesos. 4) Yes, I can. 5) It's next to the gym. Escribe en tu hoja la pregunta que corresponde a cada respuesta usando Who, How many, How much, Can y Where. Después escribe tres preguntas nuevas sobre tu escuela con la puntuación correcta.", "1) Who is your teacher? 2) How many students are there? 3) How much is the pen? 4) Can you swim? 5) Where is the library? Nuevas: Who is your friend? How many desks are there? Where is the gym?", ["cada pregunta calza con su respuesta", "empieza con mayúscula y termina con ?", "respeta el orden de las palabras"], ["hoja con ocho preguntas"], ["olvidar el signo de interrogación", "poner el sujeto antes del verbo"], "Pide que escriba una respuesta nueva para cada una de sus preguntas."),
    "Copia las cinco palabras de pregunta con su significado.",
    "Escribe un cuestionario de cinco preguntas para conocer a un compañero nuevo.",
)

# ================================================================ OA 14 clase 2: posición y objetos
lesson(
    OA14, 2,
    "Los planos y descripciones escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir dónde están los objetos y a describirlos con these, those y el material. Sirve para dar instrucciones y describir lugares por escrito.",
    ["Conozco next to, behind e in front of.", "Conozco palabras como table, bottle y chair."],
    [
        "Para escribir la posición de un objeto se usa it's o they're y una expresión de lugar: «It's next to the lamp.» (Está al lado de la lámpara.) «They're beside the door.» (Están junto a la puerta.) «It's in front of the school.» (Está delante de la escuela.) «It's behind the sofa.» (Está detrás del sofá.) «It's on the table.» (Está sobre la mesa.)",
        "Para identificar objetos: this/that son para uno y these/those para varios. These está cerca y those está lejos: «These books are new.» «Those cars are fast.» Para el material se usa It's a… : «It's a plastic bottle.» «It's a wooden chair.» «It's a metal spoon.» (metal = metal).",
        "Para deportes y pasatiempos: «Chess is a game.» «Skating is a sport.» «Painting is a hobby.» (hobby = pasatiempo). Cuando describes, escribe oraciones completas con sujeto y verbo, y revisa que la posición diga claramente dónde está cada objeto.",
    ],
    [("it's / they're", "está / están"), ("next to / beside", "al lado de / junto a"), ("in front of", "delante de"), ("behind", "detrás de"), ("these / those", "estos (cerca) / esos (lejos)"), ("plastic / wooden / metal", "de plástico / madera / metal"), ("hobby", "pasatiempo"), ("on", "sobre")],
    [
        ("Escribir la posición", "El plano: el libro está sobre la mesa y la mochila está detrás de la mesa. Escribe dónde está la mochila.", ["Busco la mochila en el plano.", "Está detrás de la mesa.", "Escribo it's behind the table."], "It's behind the table."),
        ("Describir el material", "Una cuchara de madera. Completa: «It's a ___ spoon.» Opciones: wooden, plastic.", ["Madera se dice wood.", "El adjetivo es wooden.", "It's a wooden spoon."], "wooden"),
    ],
    [
        ("Escribir «It's next the lamp».", "Se omite la palabra to.", "Next to lleva to: It's next to the lamp."),
        ("Usar this para varios objetos.", "Se confunde el singular con el plural.", "Para varios objetos usa these o those."),
    ],
    [
        ("¿Qué significa «beside»?", "Junto a", "Describe una posición."),
        ("¿Qué palabra se usa para varios objetos cercanos? Opciones: these, those.", "these", "These señala varios cercanos."),
        ("¿Qué significa «metal»?", "Metal", "Es un material."),
    ],
    [
        ("Escena: la botella está delante de la caja. Completa: «It's ___ the box.»", "in front of", "In front of es delante de."),
        ("Completa: «___ chairs are wooden.» Hablas de tres sillas que están lejos. Opciones: These, Those.", "Those", "Las sillas están lejos."),
        ("Completa: «Painting is a ___.» Opciones: hobby, plastic.", "hobby", "Pintar es un pasatiempo."),
    ],
    [
        ("Escribe una oración sobre una botella de plástico: «It's a ___ bottle.»", "plastic", "Plastic es el material."),
        ("Plano: la lámpara está sobre la mesa y el gato está junto a la mesa. Completa: «The cat is ___ the table.» Opciones: beside, behind.", "beside", "Junto a se dice beside."),
        ("Completa con it's o they're: «___ behind the sofa.» (Hablas de una pelota.)", "It's", "Una pelota es un solo objeto."),
    ],
    [
        ("Dos oraciones dicen lo mismo: «It's next to the lamp.» y «It's beside the lamp.» ¿Es verdad? Responde sí o no.", "Sí", "Next to y beside significan al lado de."),
        ("Una oración dice «Those books are on my desk». ¿Los libros están cerca o lejos?", "Lejos", "Those señala varios objetos lejanos."),
    ],
    [
        ("Plano de una sala: el sofá está en el centro. La mesa está delante del sofá. La lámpara está detrás del sofá. ¿Qué objeto está más lejos de la mesa?", "La lámpara", "La lámpara está detrás del sofá, más lejos."),
        ("Cuenta las palabras de «They're beside the door.» Escribe solo el número.", "4", "They're, beside, the y door son cuatro palabras."),
    ],
    [("Escribes una nota para tu hermano: la mochila está detrás de la puerta. ¿Qué escribes? a) It's behind the door. b) It's in front of the door.", "a", "Detrás se dice behind.")],
    [
        ("¿Cómo se dice «de madera» en inglés?", "wooden", "Wooden es el adjetivo de madera."),
        ("¿Qué palabra señala varios objetos lejanos?", "those", "Those indica lejanía."),
        ("¿Qué escribes para dar la posición de una cosa?", "It's + expresión de lugar", "Por ejemplo, it's behind the door."),
    ],
    task("Lee este plano escrito: «In my room, the bed is next to the window. The desk is in front of the bed. The lamp is on the desk. The backpack is behind the desk. These books are on the shelf. It's a wooden chair.» Dibuja un plano de tu habitación o cocina en la hoja y escribe cinco oraciones sobre dónde están cinco objetos (usa next to, beside, in front of y behind), una con these o those y una con plastic, wooden o metal.", "The table is in front of the window. The chair is next to the table. The bag is behind the chair. These cups are plastic. Those plants are beside the door.", ["usa al menos tres expresiones de posición distintas", "incluye these o those correctamente", "describe un material bien escrito"], ["hoja con plano y siete oraciones"], ["omitir to en next to", "confundir these con those"], "Pide que cambie un objeto de lugar y escriba la nueva oración."),
    "Copia las cuatro expresiones de posición con su significado.",
    "Escribe una descripción de ocho oraciones de un lugar de tu barrio usando posición y materiales.",
)

# ================================================================ OA 14 clase 3: ánimo, actividades y gustos
lesson(
    OA14, 3,
    "Las oraciones y descripciones escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir cómo se ve una persona, qué opino de una actividad y qué me gusta o no. Sirve para escribir sobre emociones y gustos.",
    ["Conozco look + adjetivo (looks tired).", "Sé que después de like se usa -ing."],
    [
        "Para describir el estado de ánimo se escribe: sujeto + look(s) + adjetivo. «He looks tired.» «She looks hungry.» «I look nervous.» «They look good.» Con he, she e it se agrega -s a look. Un adjetivo para la salud o el ánimo puede ser tired (cansado), hungry (con hambre), nervous (nervioso) o good (bien).",
        "Para opinar sobre actividades se usa el verbo con -ing como sujeto: «Playing is cool.» (Jugar es genial.) «Gaming is boring.» (Jugar videojuegos es aburrido, según quien opina.) «Reading is great.» Cool y great son positivas; boring es negativa.",
        "Para gustos y preferencias: I love, I like, I don't mind e I hate más un verbo con -ing: «I love playing baseball.» «I don't mind helping.» «I hate waiting.» Escribe siempre tu opinión con una razón si puedes: «I love reading because it is relaxing.» (relaxing = relajante)",
    ],
    [("looks tired / hungry / nervous / good", "se ve cansado / con hambre / nervioso / bien"), ("cool / great", "genial / muy bueno"), ("boring", "aburrido"), ("I love / like / don't mind / hate", "me encanta / me gusta / no me molesta / no soporto"), ("because", "porque"), ("relaxing", "relajante")],
    [
        ("Escribir el estado de ánimo", "Una niña tiembla antes de hablar frente a su curso. Completa: «She looks ___.» Opciones: nervous, tired.", ["Temblar antes de hablar muestra nervios.", "Con she se escribe looks.", "El adjetivo es nervous."], "nervous"),
        ("Escribir un gusto con razón", "A Leo le encanta nadar porque es relajante. Escribe su oración.", ["Después de love se usa -ing.", "Se agrega because más la razón.", "I love swimming because it is relaxing."], "I love swimming because it is relaxing."),
    ],
    [
        ("Escribir «She look hungry».", "Falta la -s con she.", "Escribe She looks hungry."),
        ("Escribir «I hate wait».", "Falta -ing después de hate.", "Escribe I hate waiting."),
    ],
    [
        ("¿Qué significa «boring»?", "Aburrido", "Es una opinión negativa."),
        ("¿Qué significa «I don't mind…»?", "No me molesta…", "No es un gusto fuerte."),
        ("Completa: «He ___ tired.» Opciones: looks, look.", "looks", "Con he se agrega la -s."),
    ],
    [
        ("Completa: «Reading is ___.» Opinas bien de la lectura. Opciones: great, boring.", "great", "Great es positiva."),
        ("Completa: «I ___ cooking.» Te gusta mucho. Opciones: love, hate.", "love", "Love expresa un gusto fuerte."),
        ("Ordena: playing / love / I / chess. Escribe la oración.", "I love playing chess.", "Primero va I y luego love más -ing."),
    ],
    [
        ("Pedro tiene la cara cansada y bosteza. Escribe la oración con looks: «Pedro looks ___.»", "tired", "Bostezar indica cansancio."),
        ("Corrige y escribe: «I like swim.»", "I like swimming.", "Después de like se usa -ing."),
        ("A María no le molesta lavar los platos (washing dishes). Escribe la oración con don't mind.", "I don't mind washing dishes.", "Don't mind más -ing expresa que no le molesta."),
    ],
    [
        ("Dos amigos dicen: A: «Gaming is boring.» B: «Gaming is cool.» ¿Opinan lo mismo? Responde sí o no.", "No", "Boring y cool son opuestas."),
        ("Una oración dice «She loves painting because it is relaxing». ¿Qué razón da?", "Que es relajante", "Después de because aparece la razón."),
    ],
    [
        ("Ordena de gusto fuerte a rechazo: I hate, I love, I like. Escribe las tres expresiones separadas por comas.", "I love, I like, I hate", "Love es lo más fuerte, luego like y al final hate."),
        ("Cuenta las palabras de «I love playing baseball because it is fun.» Escribe solo el número.", "8", "I, love, playing, baseball, because, it, is y fun son ocho palabras."),
    ],
    [("Un compañero llega con la cara pálida a una prueba. Quieres escribirle una nota. ¿Qué escribes? a) You look nervous. b) You nervous look.", "a", "El orden correcto es you look + adjetivo.")],
    [
        ("¿Cómo se escribe «Se ve con hambre»?", "He looks hungry.", "Looks + adjetivo."),
        ("¿Qué va después de I like?", "Un verbo con -ing", "Se dice I like reading."),
        ("En Inglés: ¿Qué palabra introduce la razón?", "because", "Because significa porque."),
    ],
    task("Lee este modelo: «My friend looks tired. He loves playing soccer because it is fun. He hates losing.» Escribe en tu hoja cinco oraciones sobre ti: una con I look + adjetivo, una con I love, una con I like, una con I don't mind o I hate, y una opinión con cool, great o boring. Agrega una razón con because en al menos una.", "I look good today. I love swimming because it is relaxing. I like reading. I hate waiting. Skating is cool.", ["usa look(s) con un adjetivo adecuado", "usa -ing después de cada verbo de gusto", "incluye una razón con because"], ["hoja con cinco oraciones"], ["olvidar -ing", "omitir la -s en looks"], "Pide que cambie un gusto por su opuesto y explique el cambio."),
    "Copia las cuatro expresiones de gusto con su significado.",
    "Escribe un párrafo de seis oraciones sobre tus pasatiempos y cómo te hacen sentir.",
)

# ================================================================ OA 14 clase 4: pasado y cantidades
lesson(
    OA14, 4,
    "Las tablas y oraciones escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir hechos del pasado con expresiones de tiempo y a escribir cantidades y el orden de los lugares. Sirve para contar lo que pasó y los resultados de una competencia.",
    ["Conozco yesterday y last week.", "Conozco los números hasta cincuenta en inglés."],
    [
        "Para hablar del pasado se escriben las expresiones yesterday (ayer), last week (la semana pasada), last month (el mes pasado) y last year (el año pasado), y el verbo en pasado. Los verbos regulares agregan -ed: played, watched, visited. Algunos son irregulares: went (fue), ate (comió), saw (vio), had (tuvo), ran (corrió). Ejemplo: «Last week I visited my uncle and ate fish.»",
        "Para enumerar se usan first (primero), second (segundo), third (tercero) y fourth (cuarto). Ejemplo: «Ana is first. Leo is second.» Para las cantidades grandes: sixty (60), seventy (70), eighty (80), ninety (90), one hundred (100) y two hundred (200). Ejemplo: «The school has two hundred students.»",
        "Cuando escribes un hecho del pasado con una cantidad, revisa que el verbo esté en pasado y que el número esté escrito correctamente: «Yesterday we collected sixty bottles.»",
    ],
    [("yesterday", "ayer"), ("last week / month / year", "la semana / mes / año pasado"), ("played / visited", "jugó / visitó"), ("went / ate / saw / ran", "fue / comió / vio / corrió"), ("first / second / third / fourth", "primero / segundo / tercero / cuarto"), ("sixty / eighty / two hundred", "sesenta / ochenta / doscientos")],
    [
        ("Escribir una oración en pasado", "Ayer jugaste fútbol. Completa: «Yesterday I ___ soccer.» Opciones: played, play.", ["Yesterday indica pasado.", "Play agrega -ed.", "El verbo es played."], "played"),
        ("Escribir una cantidad", "En una carrera participaron 80 niños. Completa: «Eighty students ___ in the race.» Opciones: ran, run.", ["Eighty es 80.", "La carrera ocurrió antes.", "El verbo en pasado es ran."], "ran"),
    ],
    [
        ("Escribir «Yesterday I go to the park».", "Se usa el presente con una expresión del pasado.", "Con yesterday escribe el pasado: I went to the park."),
        ("Escribir «eigthy».", "Se invierten letras al escribir el número.", "Se escribe eighty."),
    ],
    [
        ("¿Qué significa «last year»?", "El año pasado", "Se refiere a un año anterior."),
        ("¿Cómo se escribe 60 en inglés?", "sixty", "Es el número sesenta."),
        ("¿Qué significa «second»?", "Segundo", "Se usa para ordenar."),
    ],
    [
        ("Completa: «___ week we visited my aunt.» Opciones: Last, Next. (Ya pasó.)", "Last", "Last week es la semana pasada."),
        ("Completa: «Yesterday we ___ a movie.» Opciones: watched, watch.", "watched", "Con yesterday se usa el pasado."),
        ("Completa: «Ana is ___ in the list.» Ana tiene el primer lugar. Opciones: first, third.", "first", "First es primero."),
    ],
    [
        ("Escribe con letras el número 200.", "two hundred", "200 se dice two hundred."),
        ("Completa: «Last month I ___ my cousin.» (verbo see en pasado) Opciones: saw, see.", "saw", "Saw es el pasado de see."),
        ("En la tabla: Mía 90 puntos, Leo 80 puntos. Escribe quién es first.", "Mía", "Mía tiene más puntos."),
    ],
    [
        ("Alguien escribió «Yesterday I eat pizza». ¿Qué corregirías? a) Cambiar eat por ate b) Cambiar yesterday por tomorrow", "a", "Con yesterday el verbo va en pasado."),
        ("Una lista dice: first Ana, second Leo, third Mía. ¿Quién es third?", "Mía", "Mía ocupa el tercer lugar."),
    ],
    [
        ("Tres niños recogieron botellas: 60, 80 y 100. Escribe cuántas recogieron entre los tres. Solo el número.", "240", "Se suman: 60 + 80 + 100 = 240."),
        ("Ordena de menor a mayor: eighty, sixty, two hundred. Escribe los números 60, 80, 200 en ese orden separados por comas.", "60, 80, 200", "Sixty es 60, eighty es 80 y two hundred es 200."),
    ],
    [("Escribes sobre tu semana pasada: fuiste a la biblioteca y comiste fruta. ¿Cuál oración usas? a) Last week I went to the library and ate fruit. b) Last week I go to the library and eat fruit.", "a", "Last week pide el pasado.")],
    [
        ("¿Cómo se dice «ayer» en inglés?", "yesterday", "Indica el día anterior."),
        ("¿Qué letras agrega un verbo regular en pasado?", "-ed", "Played, watched y visited terminan en -ed."),
        ("¿Cómo se escribe 80?", "eighty", "Es el número ochenta."),
    ],
    task("Lee esta tabla: Mía 90 puntos, Ana 80 puntos, Leo 60 puntos. Y este modelo: «Last week we visited the museum. Mía was first with ninety points. Ana was second.» Escribe en tu hoja cuatro oraciones sobre la semana pasada (una con went, una con ate o saw, una con un verbo regular terminado en -ed y una con yesterday), y tres oraciones con first, second y third sobre la tabla.", "Last week I went to the park. Yesterday I played soccer. I ate fruit. Mía is first. Ana is second. Leo is third.", ["usa verbos en pasado con expresiones de tiempo", "ordena los lugares según la tabla", "escribe los números con letras correctas"], ["hoja con siete oraciones"], ["usar presente con yesterday", "escribir mal un número"], "Pide que cambie un número de la tabla y reescriba el orden."),
    "Copia los cuatro verbos del pasado con su significado.",
    "Escribe un párrafo de seis oraciones sobre tus vacaciones pasadas usando expresiones de pasado y cantidades.",
)

# ================================================================ OA 14 clase 5: comparar y texto integrado
lesson(
    OA14, 5,
    "Las tablas y descripciones escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir comparaciones y a integrar varias funciones en un párrafo corto. Sirve para describir y comparar con claridad.",
    ["Conozco las preguntas con Who, Where y How many.", "Conozco taller, faster y the easiest."],
    [
        "Para comparar dos cosas se agrega -er al adjetivo corto y luego se escribe than: «Tom is taller than Ana.» «My bike is faster than yours.» Para el más de todos se usa the + -est: «Tom is the tallest.» Si el adjetivo termina en -y, la y cambia a i: easy → easier → the easiest, tidy → the tidiest. Si termina en vocal y consonante, se duplica la consonante: big → bigger → the biggest. Con adjetivos largos se usa more: «This game is more difficult than that one.» y the most difficult of all.",
        "Un párrafo corto reúne varias funciones. Ejemplo: «My room is small. The bed is next to the window. These books are new. I love reading, so I read every day. Last year I had forty books, but now I have sixty. My room is the tidiest in my house.» Cada oración tiene una función distinta: describir, ubicar, gustos, pasado, cantidad y comparar.",
        "Para escribir tu párrafo, elige un tema, anota una oración por función y ordénalas con sentido. Usa palabras como and, but, because y so (así que) para unir ideas. Al final revisa la mayúscula en I y que cada oración tenga sujeto y verbo.",
    ],
    [("taller than", "más alto que"), ("faster than", "más rápido que"), ("the tallest", "el más alto"), ("more difficult than", "más difícil que"), ("the most difficult", "el más difícil"), ("tidy / tidiest", "ordenado / el más ordenado")],
    [
        ("Escribir una comparación de dos", "Datos: el libro A tiene 100 páginas y el libro B tiene 150. Completa: «Book B is ___ than book A.» Opciones: longer, longest.", ["Se comparan dos libros.", "Para dos se usa -er más than.", "Longer es la respuesta."], "longer"),
        ("Escribir el superlativo", "Tres pruebas: A tarda 10 minutos, B 20 y C 30. Completa: «C is the ___ test.» Opciones: longest, longer. (long = largo)", ["Se comparan tres cosas.", "Para el grupo se usa the -est.", "Longest es la respuesta."], "longest"),
    ],
    [
        ("Escribir «more taller than».", "Se mezcla more con -er.", "Con taller no se usa more."),
        ("Escribir un párrafo con una sola función.", "Solo se repite el mismo tipo de oración.", "Reúne varias funciones: describir, gustos, pasado y comparar."),
    ],
    [
        ("¿Qué palabra va después de faster al comparar?", "than", "Faster than compara dos cosas."),
        ("¿Cuál es el superlativo de tall? Opciones: tallest, taller.", "tallest", "El superlativo agrega the -est."),
        ("¿Qué significa «more difficult than»?", "Más difícil que", "Compara dos cosas."),
    ],
    [
        ("Completa: «Ana is ___ than Leo.» Ana mide 150 cm y Leo 145 cm. Opciones: taller, tallest.", "taller", "Se comparan dos personas."),
        ("Completa: «This is the ___ question of all.» Opciones: easiest, easier.", "easiest", "Of all pide el superlativo."),
        ("Completa: «This game is ___ difficult than chess.» Opciones: more, most.", "more", "Para comparar dos se usa more."),
    ],
    [
        ("Escribe la oración con faster than: el perro corre más rápido que el gato. Completa: «The dog is ___ than the cat.»", "faster", "Se compara la velocidad de dos animales."),
        ("Tres niñas miden 140, 150 y 155 cm. Escribe la oración con the tallest sobre la que mide 155 cm: «Sofía is ___.»", "the tallest", "El superlativo se escribe the tallest."),
        ("Corrige: «This game is the most easiest.»", "This game is the easiest.", "No se mezclan most y -est."),
    ],
    [
        ("«I love chess. Yesterday I played chess. Chess is more difficult than checkers.» (checkers = damas) ¿Cuántas funciones distintas hay: gusto, pasado y comparar?", "3", "La primera da un gusto, la segunda habla del pasado y la tercera compara."),
        ("En «My room is the tidiest in my house», ¿se compara con otro objeto o con todo el grupo?", "Con todo el grupo", "The tidiest es un superlativo."),
    ],
    [
        ("En un párrafo hay tres oraciones: a) Yesterday I played chess. b) I love chess. c) Chess is a game. ¿Cuál presenta el tema general y por eso va primero?", "c", "Chess is a game presenta el tema antes de dar detalles."),
        ("Cuenta las oraciones: «My school is big. The gym is next to the library. I love reading, but I hate waiting. Last year I had forty books.» Escribe solo el número.", "4", "Hay cuatro puntos finales, uno por oración."),
    ],
    [("Escribes sobre dos deportes: el fútbol es más rápido que el ajedrez. ¿Qué escribes? a) Soccer is faster than chess. b) Soccer is the faster chess.", "a", "Faster than compara dos cosas.")],
    [
        ("¿Qué palabra usas para comparar dos cosas?", "than", "Va después del adjetivo con -er."),
        ("¿Qué agregas a un adjetivo corto para el superlativo?", "the + -est", "Por ejemplo, the tallest."),
        ("¿Para qué sirven and, but y because en un párrafo?", "Para unir ideas", "Conectan unas oraciones con otras."),
    ],
    task("Lee este modelo: «My room is small. The bed is next to the window. I love reading, so I read every day. Last year I had forty books, but now I have sixty. My room is the tidiest in my house.» Escribe en tu hoja un párrafo de seis oraciones sobre tu habitación, tu escuela o tu mascota, con estas funciones: describir, ubicar, un gusto, un hecho del pasado, una cantidad y una comparación. Subraya cada función.", "My school is big. The library is next to the gym. I love reading. Last year I read twenty books. Now I read thirty. My school is bigger than my old school.", ["incluye al menos cinco funciones distintas", "cada oración tiene sujeto y verbo", "usa mayúscula, puntos y la palabra than o -est correctamente"], ["hoja con párrafo y funciones subrayadas"], ["repetir una sola función", "mezclar more y -er"], "Pide que cambie una oración por otra función y explique el cambio."),
    "Copia las tres formas de comparar con un ejemplo cada una.",
    "Escribe un párrafo de ocho oraciones comparando dos deportes que conoces.",
)

# ================================================================ OA 15 clase 1: organizar ideas
lesson(
    OA15, 1,
    "Los ejemplos de mapa de ideas y listas escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé el primer paso del proceso de escritura: organizar ideas antes de escribir. Sirve para que mis textos tengan orden y no se me olvide nada.",
    ["Sé escribir oraciones cortas en inglés.", "Conozco palabras de mis pasatiempos."],
    [
        "El proceso de escritura tiene cinco pasos: organizar ideas, redactar (escribir el primer borrador), revisar, editar y publicar. El primer paso es organizar: elegir el tema, anotar palabras o frases clave y ordenarlas. Puedes usar una lista, un mapa de ideas (mind map) o una tabla.",
        "Ejemplo de mapa de ideas sobre My pet: centro «My pet»; ramas: name (Toby), animal (dog), color (brown), likes (play with a ball). Con esas ideas puedes escribir después oraciones completas: «My pet is a dog. His name is Toby. He is brown. He likes playing with a ball.»",
        "Cuando organices ideas, revisa que sean sobre el mismo tema, que no se repitan y que estén en un orden lógico: primero presentar y después dar detalles. No escribas aún oraciones completas; anota solo palabras clave, y usa el diccionario si no sabes cómo se dice algo.",
    ],
    [("writing process", "proceso de escritura"), ("organize ideas", "organizar ideas"), ("mind map", "mapa de ideas"), ("draft", "borrador"), ("topic", "tema"), ("key words", "palabras clave"), ("pet", "mascota")],
    [
        ("Elegir ideas del mismo tema", "Tema: My school. Ideas: library, gym, airplane, teacher. ¿Cuál no es del tema?", ["Library, gym y teacher son parte de la escuela.", "Airplane es un avión, no una parte de la escuela.", "No es del tema."], "airplane"),
        ("Elegir la primera oración", "Para presentar a tu mascota, ¿cuál oración va primero? a) She likes balls. b) My pet is a dog. c) Her name is Luna.", ["Presentar es decir qué animal es.", "My pet is a dog lo dice.", "Los nombres y gustos son detalles."], "b"),
    ],
    [
        ("Escribir directamente oraciones sin organizar ideas.", "Se salta el primer paso.", "Anota primero palabras clave en un mapa o lista."),
        ("Mezclar ideas de temas distintos.", "No se revisa el tema.", "Pregunta: ¿cada idea es sobre mi tema?"),
    ],
    [
        ("¿Cuál es el primer paso del proceso de escritura?", "Organizar ideas", "Antes de escribir se ordenan las ideas."),
        ("¿Qué es un «mind map»?", "Un mapa de ideas", "Muestra el tema en el centro y las ideas alrededor."),
        ("¿Qué significa «draft»?", "Borrador", "Es la primera versión del texto."),
    ],
    [
        ("Tema: My pet. Ideas: name, color, spaceship, food. ¿Cuál no es del tema? Opciones: color, spaceship.", "spaceship", "Una nave no es parte de una mascota."),
        ("¿Cuántos pasos tiene el proceso de escritura? Escribe solo el número.", "5", "Son organizar, redactar, revisar, editar y publicar."),
        ("Tema: My day. Ideas: breakfast, school, lunch. ¿Cuál va primero en un orden lógico? Opciones: breakfast, lunch.", "breakfast", "El desayuno ocurre al comienzo del día."),
    ],
    [
        ("Mapa de ideas: centro «My friend»; ramas: name (Pablo), age (11), likes (chess). Completa la oración con la rama likes: «Pablo ___ chess.» Opciones: likes, like.", "likes", "Con Pablo (él) el verbo lleva -s."),
        ("Tema: My family. Anotas: mother, father, brother, dinosaur. Escribe la palabra que sobra.", "dinosaur", "No es parte de la familia."),
        ("Completa el mapa: centro «My room»; ramas: bed, desk, lamp, ___. Opciones: chair, ocean.", "chair", "Una silla puede estar en la habitación."),
    ],
    [
        ("Alguien escribió su mapa con las ramas: dog, cat, school, pizza. Tema: Animals. ¿Cuántas ideas son del tema?", "2", "Solo dog y cat son animales."),
        ("¿Por qué no se escriben oraciones completas en el mapa?", "Porque solo se anotan palabras clave", "El mapa organiza ideas, no es el borrador."),
    ],
    [
        ("Tema: My hobby. Un mapa tiene 6 ramas, pero 2 son copias de otras ramas. ¿Cuántas ideas distintas hay? Solo el número.", "4", "6 − 2 = 4."),
        ("Ordena los pasos: publish, organize ideas, draft. Escribe el que va primero.", "organize ideas", "Es el primer paso."),
    ],
    [("Vas a escribir sobre tu mejor amigo. ¿Qué haces primero? a) Anotar ideas clave en un mapa b) Publicar el texto", "a", "Organizar es el primer paso.")],
    [
        ("¿Qué son las palabras clave?", "Las ideas principales del tema", "Guían las oraciones."),
        ("¿Qué no debe haber en un mapa de ideas?", "Ideas repetidas o de otro tema", "Se revisa que sean del tema."),
        ("¿Qué paso viene después de organizar ideas?", "Redactar", "Se escribe el borrador."),
    ],
    task("Lee este modelo: «Centro: My pet. Ramas: name (Toby), animal (dog), color (brown), likes (play with a ball).» Elige un tema (My friend, My school o My hobby). Dibuja en tu hoja un mapa de ideas con el tema en el centro y cuatro ramas con palabras clave. Luego ordena las ideas con números del 1 al 4 en el orden en que las escribirías.", "Centro: My hobby. Ramas: 1 name (soccer), 2 where (park), 3 when (Saturday), 4 friends (Pablo, Ana).", ["el centro es el tema", "las cuatro ramas son del mismo tema", "las ideas están numeradas en orden lógico"], ["hoja con mapa de ideas y numeración"], ["ramas de otro tema", "escribir oraciones completas"], "Pregunta por qué ordenó así las ideas y qué cambiaría."),
    "Copia los cinco pasos del proceso de escritura en orden.",
    "Crea un mapa de ideas de seis ramas sobre un tema que conoces bien.",
)

# ================================================================ OA 15 clase 2: redactar oraciones y párrafos
lesson(
    OA15, 2,
    "Los mapas de ideas y borradores escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a pasar de las ideas a oraciones completas y a un párrafo breve. Sirve para escribir mi primer borrador con orden.",
    ["Sé organizar ideas en un mapa.", "Sé escribir oraciones con sujeto y verbo."],
    [
        "Redactar es escribir el primer borrador con las ideas que anotaste. Cada idea clave se convierte en una oración completa con sujeto y verbo. Del mapa «name: Toby, animal: dog» sale «My pet is a dog. His name is Toby.» Un párrafo breve tiene una oración que presenta el tema, dos o tres oraciones con detalles y, a veces, una oración final.",
        "Las palabras de unión ayudan a ordenar: and (y), but (pero), because (porque), also (también). Ejemplo: «I like soccer because it is fun, and I also like chess.» Cuida que cada oración comience con mayúscula y termine con punto.",
        "En un borrador no hay que buscar la perfección: se escribe para llegar al final. Después se revisa y se corrige. Puedes pedir ayuda a tu docente o a una persona de tu casa, pero las ideas deben ser tuyas.",
    ],
    [("sentence", "oración"), ("paragraph", "párrafo"), ("first draft", "primer borrador"), ("also", "también"), ("topic sentence", "oración que presenta el tema"), ("detail", "detalle")],
    [
        ("Convertir ideas en oración", "Idea del mapa: color (brown). Tema: My dog. Escribe la oración.", ["La idea es el color.", "El sujeto puede ser My dog.", "Se escribe My dog is brown."], "My dog is brown."),
        ("Unir dos ideas", "Une con and: I like soccer. I like chess.", ["Las ideas son parecidas.", "And las une.", "Se puede decir I like soccer and chess."], "I like soccer and chess."),
    ],
    [
        ("Escribir ideas sueltas en lugar de oraciones.", "Se copian las palabras del mapa.", "Convierte cada idea en una oración con sujeto y verbo."),
        ("Olvidar la mayúscula inicial.", "No se vuelve a revisar la oración.", "Toda oración empieza con mayúscula."),
    ],
    [
        ("¿Qué es redactar?", "Escribir el primer borrador", "Es el segundo paso del proceso."),
        ("¿Qué significa «also»?", "También", "Agrega una idea."),
        ("¿Cuál es una oración completa? a) My dog b) My dog is brown.", "b", "Tiene sujeto y verbo."),
    ],
    [
        ("Completa: «I like swimming ___ it is relaxing.» Opciones: because, but.", "because", "Introduce la razón."),
        ("Completa: «I like apples, ___ I don't like pears.» Las ideas son contrarias. Opciones: but, because.", "but", "But une dos ideas contrarias."),
        ("En un párrafo sobre tu gata, ¿cuál oración presenta el tema? a) Her name is Luna. b) My cat is white. c) She likes fish.", "b", "My cat is white presenta a la mascota; las otras dan detalles."),
    ],
    [
        ("Mapa: centro My school; ramas: gym, library. Escribe una oración con library: «The ___ is big.»", "library", "Se usa la rama del mapa."),
        ("Convierte la rama name (Mía) en oración: «Her name ___ Mía.» Opciones: is, are.", "is", "Con her name (una cosa) se usa is."),
        ("Completa: «She plays chess ___ tennis.» Suma dos actividades. Opciones: and, because.", "and", "And suma las dos actividades."),
    ],
    [
        ("Un borrador dice: «dog, brown, ball». ¿Es un párrafo? Responde sí o no.", "No", "Son palabras sueltas, no oraciones."),
        ("¿Por qué no hay que buscar la perfección en un borrador?", "Porque se revisa después", "Los errores se corrigen en el paso siguiente."),
    ],
    [
        ("Lee: «I like soccer because it is fun. I also like chess. My dog is brown.» ¿Cuántas oraciones usan una palabra de unión (because, also, and, but)? Solo el número.", "2", "La primera usa because y la segunda usa also."),
        ("Une con because: I am tired. I played all day. Escribe la oración completa.", "I am tired because I played all day.", "Because introduce la razón."),
    ],
    [("Tienes las ideas: school, friends, Monday. Vas a escribir una oración. ¿Cuál sirve? a) I see my friends at school on Monday. b) School friends Monday.", "a", "La opción a tiene sujeto y verbo.")],
    [
        ("¿Qué lleva una oración completa?", "Sujeto y verbo", "Sin eso son palabras sueltas."),
        ("¿Para qué sirve and?", "Para unir ideas", "Suma dos ideas."),
        ("¿Qué paso sigue al borrador?", "Revisar", "Se mejora el texto."),
    ],
    task("Lee este mapa: «Centro: My hobby. Ramas: name (soccer), where (park), when (Saturday), friends (Pablo).» y este borrador: «My hobby is soccer. I play it at the park on Saturday. I play with my friend Pablo, and we have fun.» Elige un tema y haz tu mapa de cuatro ideas. Escribe en tu hoja un borrador de cuatro a cinco oraciones usando todas las ideas y al menos una palabra de unión (and, but, because o also).", "My friend is Ana. She is eleven. She likes drawing because it is fun. We also play at the park on Monday.", ["cada idea del mapa se convierte en una oración", "las oraciones tienen sujeto y verbo", "usa al menos una palabra de unión"], ["hoja con mapa y borrador"], ["dejar palabras sueltas", "olvidar mayúsculas y puntos"], "Pide que lea el borrador y señale qué idea del mapa usó en cada oración."),
    "Copia las cuatro palabras de unión con su significado.",
    "Escribe un párrafo de seis oraciones a partir de un mapa de ideas nuevo.",
)

# ================================================================ OA 15 clase 3: diálogos con ayuda del docente
lesson(
    OA15, 3,
    "Los diálogos modelo escritos en cada ejercicio, lápiz, una hoja y una persona que lea contigo.",
    "Aprenderé a escribir un diálogo corto con turnos y puntuación correcta, con ayuda de otra persona. Sirve para escribir conversaciones que otros puedan leer en voz alta.",
    ["Conozco preguntas con Who, Where y Can.", "Sé usar expresiones como Great! y That's cool!"],
    [
        "Un diálogo escrito muestra los turnos de dos personas. Se escribe el nombre de quien habla seguido de dos puntos (A: o Ana:) y después lo que dice. Cada turno comienza con mayúscula; las preguntas terminan con signo de interrogación; las exclamaciones (That's cool!) terminan con signo de exclamación (!).",
        "Modelo: «Ana: Hi, Tom! Can you play chess? Tom: Yes, I can. Where do you want to play? Ana: At the library. Tom: Great! See you at four.» Observa: la palabra I siempre se escribe con mayúscula, aunque esté en medio de la oración.",
        "Con la ayuda del docente o de otra persona, lee tu diálogo en voz alta y comprueba que se entienda quién habla en cada turno. Si hay confusión, aclara con el nombre. Revisa también que las respuestas calcen con las preguntas.",
    ],
    [("dialogue", "diálogo"), ("turn", "turno"), ("Hi!", "¡Hola!"), ("at four", "a las cuatro"), ("See you…", "Nos vemos…"), ("capital I", "I mayúscula"), ("exclamation mark (!)", "signo de exclamación")],
    [
        ("Ordenar un diálogo", "Ordena: a) Tom: Yes, I can. b) Ana: Can you play chess? c) Ana: Great! Escribe las letras en orden.", ["Primero va la pregunta.", "Luego la respuesta.", "Al final la reacción."], "b, a, c"),
        ("Corregir la puntuación", "Corrige: «tom: can you swim».", ["Se agrega mayúscula a Tom.", "Se agrega Can con mayúscula.", "Se agrega el signo ? al final."], "Tom: Can you swim?"),
    ],
    [
        ("Escribir «i can» con i minúscula.", "No se recuerda la regla de la I.", "La I siempre va con mayúscula."),
        ("Escribir las respuestas sin el nombre del que habla.", "Se pierde el turno.", "Escribe Nombre: antes de cada intervención."),
    ],
    [
        ("¿Qué signo termina una pregunta?", "?", "Marca la interrogación."),
        ("¿Cuál es correcta? a) i like chess b) I like chess.", "b", "La I va con mayúscula y la oración termina con punto."),
        ("¿Qué escribes antes de lo que dice cada persona?", "Su nombre y dos puntos", "Así se sabe quién habla."),
    ],
    [
        ("Completa: «Ana: Where ___ you want to play?» Opciones: do, are.", "do", "Con want se usa do."),
        ("Completa la respuesta: «Ana: Can you dance? Tom: Yes, ___ can.» Opciones: I, i.", "I", "La I va con mayúscula."),
        ("Completa la reacción final: «Tom: I won! Ana: ___ !» Opciones: Great, Excuse me.", "Great", "Great felicita un logro."),
    ],
    [
        ("Escribe un turno con pregunta: Ana pregunta dónde está la biblioteca. Completa: «Ana: ___ is the library?»", "Where", "Where pide un lugar."),
        ("Corrige: «Ana: yes i can.»", "Ana: Yes, I can.", "Se agregan mayúsculas, coma y punto final."),
        ("¿Cuál de estos turnos necesita ? al final? a) Where do you live b) That's cool", "a", "Where do you live es una pregunta."),
    ],
    [
        ("Un diálogo dice: «Hi! Can you play chess? Yes, I can.» sin nombres. ¿Se sabe quién habla en cada turno? Responde sí o no.", "No", "Sin el nombre y los dos puntos no se distinguen los turnos."),
        ("En «Tom: Great! See you at four.» ¿Se hace una pregunta o se despide?", "Se despide", "See you at four es una despedida."),
    ],
    [
        ("En el modelo de la explicación («Ana: Hi, Tom! Can you play chess? Tom: Yes, I can. Where do you want to play? Ana: At the library. Tom: Great! See you at four.») ¿cuántos turnos hay? Solo el número.", "4", "Hablan Ana, Tom, Ana y Tom: cuatro turnos."),
        ("Cuenta las palabras en «Yes, I can.» Escribe solo el número.", "3", "Yes, I y can son tres palabras."),
    ],
    [("Escribes un diálogo entre dos amigos que quedan para jugar. Quieres que uno proponga: «¿Jugamos?». ¿Cuál escribes? a) Ana: Can we play? b) Ana: we can play", "a", "La pregunta empieza con Can y termina con ?.")],
    [
        ("¿Cómo se escribe «yo» en inglés?", "I", "Siempre va con mayúscula."),
        ("¿Qué signo usas al final de That's cool?", "!", "Marca la emoción de la expresión."),
        ("¿Para qué lees el diálogo en voz alta?", "Para comprobar que se entiende", "Escuchar ayuda a detectar errores."),
    ],
    task("Lee este modelo: «Ana: Hi, Tom! Can you play chess? Tom: Yes, I can. Where do you want to play? Ana: At the library. Tom: Great! See you at four.» Escribe en tu hoja un diálogo de seis turnos entre dos amigos que quedan para hacer algo (jugar, estudiar o cocinar). Usa al menos una pregunta, una respuesta con I y una expresión como Great! o That's cool! Luego léelo en voz alta con otra persona.", "Mía: Hi, Leo! Can you help me with homework? Leo: Yes, I can. When? Mía: At five. Leo: Great! See you.", ["cada turno lleva el nombre de quien habla", "usa I con mayúscula y ? en las preguntas", "incluye una expresión común"], ["hoja con el diálogo y lectura en voz alta"], ["olvidar el nombre", "escribir i minúscula"], "Pide que subraye las preguntas y las exclamaciones."),
    "Copia el diálogo modelo corrigiendo la I y los signos.",
    "Escribe un diálogo de ocho turnos con una compra en una tienda de la escuela.",
)

# ================================================================ OA 15 clase 4: diccionario en línea
lesson(
    OA15, 4,
    "Las entradas de diccionario escritas en cada ejercicio, lápiz y una hoja. Si tienes computador, puedes comprobar lo aprendido en un diccionario en línea con ayuda de una persona adulta.",
    "Aprenderé a leer una entrada de diccionario para elegir la palabra y el significado correctos. Sirve para escribir con vocabulario preciso y sin errores.",
    ["Sé el orden alfabético.", "Conozco palabras como bat y book."],
    [
        "Un diccionario en línea es una página que muestra el significado de una palabra. Una entrada tiene: la palabra (por ejemplo bat), su tipo (noun = sustantivo, verb = verbo, adjective = adjetivo), uno o más significados numerados y una oración de ejemplo. Muchas entradas tienen una pronunciación escrita con símbolos, y a veces un botón para escuchar.",
        "Entrada de ejemplo: «bat (noun) 1. an animal that flies at night. Example: A bat lives in a cave. 2. a stick used to hit a ball. Example: He holds a bat. (Spanish: murciélago / bate)». Si una palabra tiene dos significados, hay que mirar la oración para elegir el correcto.",
        "Para buscar una palabra en español y encontrar su equivalente en inglés, escribe la palabra en la barra de búsqueda y mira los resultados. Verifica con la oración de ejemplo que el significado calza con tu texto. No copies un texto completo de internet: usa el diccionario solo para palabras sueltas.",
    ],
    [("dictionary", "diccionario"), ("entry", "entrada: la información de una palabra"), ("noun / verb / adjective", "sustantivo / verbo / adjetivo"), ("example sentence", "oración de ejemplo"), ("meaning", "significado"), ("bat", "murciélago o bate")],
    [
        ("Elegir el significado", "Entrada: bat (noun) 1. an animal that flies at night. 2. a stick used to hit a ball. Oración: «He holds a bat in the baseball game.» ¿Qué significado calza?", ["La oración habla de un partido de baseball.", "El significado 2 es un palo para golpear una pelota.", "El 2 calza."], "El significado 2 (bate)"),
        ("Leer el tipo de palabra", "Entrada: run (verb). ¿Qué tipo de palabra es run?", ["Entre paréntesis dice verb.", "Verb significa verbo.", "Run es un verbo."], "Un verbo"),
    ],
    [
        ("Elegir el primer significado sin leer el ejemplo.", "Se supone que siempre es el correcto.", "Lee la oración de ejemplo y elige el que calza con tu texto."),
        ("Copiar un texto completo de internet.", "Se confunde buscar una palabra con copiar.", "Usa el diccionario solo para palabras sueltas y escribe con tus palabras."),
    ],
    [
        ("¿Qué significa «noun»?", "Sustantivo", "Es el tipo de palabra que nombra cosas."),
        ("¿Para qué sirve la oración de ejemplo?", "Para ver el uso de la palabra", "Muestra cómo se usa en una oración."),
        ("¿Qué indica «verb» en una entrada?", "Que la palabra es un verbo", "Es el tipo de palabra."),
    ],
    [
        ("Entrada: bark (noun) 1. the outside of a tree. 2. the sound a dog makes. Oración: «The dog's bark is loud.» ¿Qué significado calza?", "El 2 (ladrido)", "La oración habla de un perro."),
        ("Entrada: fast (adjective) not slow. Oración: «My bike is fast.» ¿Qué tipo de palabra es fast?", "Un adjetivo", "La entrada dice adjective, que significa adjetivo."),
        ("Quieres decir «biblioteca». Entrada: library (noun) a place with books. ¿Qué palabra en inglés usas?", "library", "La entrada muestra la palabra."),
    ],
    [
        ("Entrada: play (verb) 1. to take part in a game or sport. 2. to make music with an instrument. Oración: «I play the guitar.» ¿Qué significado calza?", "El 2", "Se habla de tocar un instrumento."),
        ("Entrada: light 1. (noun) what comes from the sun or a lamp. 2. (adjective) not heavy. Oración: «This bag is light.» ¿Qué significado calza?", "No pesado", "Bag is light significa que la mochila es liviana."),
        ("Una compañera busca «mascota» y encuentra pet. Entrada: pet (noun) an animal you keep at home. ¿Es la palabra correcta? Responde sí o no.", "Sí", "La definición coincide con la idea de mascota."),
    ],
    [
        ("Si una palabra tiene dos significados, ¿qué te ayuda a elegir el correcto?", "La oración de ejemplo", "Compara con el contexto de tu texto."),
        ("Un compañero copió un párrafo completo de internet. ¿Usó bien el diccionario? Responde sí o no.", "No", "El diccionario se usa para palabras sueltas."),
    ],
    [
        ("Tienes que ordenar alfabéticamente: pet, book, chair. Escribe la que va primero.", "book", "B va antes que C y que P."),
        ("Entrada: duck 1. (noun) a bird that swims on lakes. 2. (verb) to bend down quickly. Oración: «The duck swims on the lake.» ¿Qué significado calza? Escribe 1 o 2.", "1", "Swims on the lake habla de un ave."),
    ],
    [("Escribes «My cat is very ___» y quieres decir «grande». Entrada: big (adjective) large. ¿Qué palabra pones? a) big b) pet", "a", "Big significa grande.")],
    [
        ("¿Qué partes tiene una entrada de diccionario?", "Palabra, tipo, significado y ejemplo", "Es la estructura típica."),
        ("¿Qué haces si una palabra tiene varios significados?", "Eliges el que calza con tu texto", "Mira la oración de ejemplo."),
        ("¿Qué significa «adjective»?", "Adjetivo", "Describe cómo es algo."),
    ],
    task("Lee esta entrada: «bat (noun) 1. an animal that flies at night. Example: A bat lives in a cave. 2. a stick used to hit a ball. Example: He holds a bat.» Escribe en tu hoja dos oraciones nuevas: una con bat en el significado 1 y otra con bat en el significado 2. Después escoge dos palabras que quieras usar en un texto, escribe su significado en español y una oración de ejemplo con cada una (si tienes diccionario en línea, compruébalas con una persona adulta; si no, usa un diccionario de papel).", "A bat flies at night. I use a bat in baseball. Palabra: happy = feliz. I am happy today.", ["usa el significado correcto de bat en cada oración", "escribe significado y ejemplo para dos palabras más", "no copia textos completos"], ["hoja con cuatro oraciones y dos significados"], ["mezclar los significados", "copiar la definición completa"], "Pide que explique cómo eligió el significado."),
    "Copia la entrada de bat y subraya el tipo de palabra y la oración de ejemplo.",
    "Elige tres palabras nuevas, busca su significado y escribe una oración con cada una.",
)

# ================================================================ OA 15 clase 5: procesador de textos y publicar
lesson(
    OA15, 5,
    "Las descripciones de herramientas y borradores escritos en cada ejercicio, lápiz y una hoja. Si tienes computador, puedes practicar los pasos con ayuda de una persona adulta; si no, hazlo en papel.",
    "Aprenderé a usar las herramientas de un procesador de textos para escribir, corregir y publicar mi texto. Sirve para presentar un texto limpio y fácil de leer.",
    ["Sé redactar un borrador.", "Sé qué son los signos de interrogación y la I mayúscula."],
    [
        "Un procesador de textos es un programa para escribir y dar formato a un texto. Sus herramientas principales son: escribir y borrar, poner el título en negrita (bold), cambiar el tamaño de la letra (size), guardar el archivo (save) y revisar la ortografía (spell check). Una línea roja bajo una palabra avisa que quizás está mal escrita.",
        "El corrector no entiende el significado: puede aceptar una palabra bien escrita pero equivocada (por ejemplo right, que significa correcto, en lugar de write, que significa escribir). Por eso tú debes releer. También puede cambiar palabras solo (autocorrect): revisa que no cambie lo que quisiste decir.",
        "Publicar es presentar tu texto final: guardar, imprimir o compartir con tu curso. Antes de publicar, revisa que el título esté arriba, que no haya líneas rojas, que tus datos privados no aparezcan y que el texto se lea bien. Si no tienes computador, publica copiando el texto limpio en una hoja o en un cartel.",
    ],
    [("word processor", "procesador de textos"), ("bold", "negrita"), ("title", "título"), ("save", "guardar"), ("spell check", "corrector de ortografía"), ("publish", "publicar"), ("print", "imprimir")],
    [
        ("Interpretar la línea roja", "En tu texto aparece «frend» con una línea roja. ¿Qué te avisa?", ["La línea roja marca una posible falta de ortografía.", "La palabra correcta es friend.", "Debes corregirla."], "Que quizás está mal escrita y debe revisarse"),
        ("Elegir la herramienta", "Quieres que el título se vea más fuerte. ¿Qué herramienta usas? Opciones: bold, save.", ["Más fuerte significa negrita.", "Negrita se dice bold.", "La herramienta es bold."], "bold"),
    ],
    [
        ("Aceptar siempre lo que dice el corrector.", "Se cree que el corrector entiende el significado.", "Relee tú y verifica el significado."),
        ("Publicar sin releer el texto final.", "Se cree que está listo al terminar de escribir.", "Antes de publicar revisa título, ortografía y datos privados."),
    ],
    [
        ("¿Qué es «save»?", "Guardar", "Conserva el archivo."),
        ("¿Qué hace la herramienta «bold»?", "Pone la letra en negrita", "Resalta el texto."),
        ("¿Qué avisa una línea roja?", "Una posible falta de ortografía", "Revisa la palabra marcada."),
    ],
    [
        ("Escribes «I like soccor» y aparece una línea roja bajo soccor. ¿Cuál es la palabra correcta? Opciones: soccer, soker.", "soccer", "Es la ortografía correcta."),
        ("Quieres conservar tu texto para mañana. ¿Qué botón usas? Opciones: save, bold.", "save", "Guardar conserva el archivo."),
        ("Quieres compartir una copia en papel. ¿Qué haces? Opciones: print, spell check.", "print", "Imprimir da una copia en papel."),
    ],
    [
        ("Escribes «teh book» y aparece una línea roja bajo teh. ¿Cuál es la corrección más probable? Opciones: the, tea.", "the", "The book es la frase y teh es un error de tipeo."),
        ("Antes de publicar, ¿qué revisas? a) título, ortografía y datos privados b) solo el color", "a", "Se revisa que el texto sea claro y seguro."),
        ("Un texto tiene dos líneas rojas y las corriges. ¿Qué haces después? a) Releer todo b) Publicar sin revisar", "a", "Al corregir se vuelve a leer."),
    ],
    [
        ("Dos compañeros aceptan todo lo que sugiere el corrector. ¿Pueden quedar errores? Responde sí o no.", "Sí", "El corrector no entiende el significado."),
        ("Si no hay computador, ¿cómo puedes publicar tu texto? a) Copiarlo limpio en una hoja o cartel b) No publicarlo", "a", "El objetivo es presentarlo ordenado."),
    ],
    [
        ("¿Qué hace la herramienta «size»? a) Cambiar el tamaño de la letra b) Guardar el archivo", "a", "Size significa tamaño."),
        ("Ordena los pasos: publicar, revisar, redactar. Escribe el que va último.", "publicar", "Primero se redacta, luego se revisa y al final se publica."),
    ],
    [("Escribes «I want to right a story» y el corrector no marca nada. ¿Por qué? a) Right está bien escrita, aunque no calza con el sentido b) El corrector entiende todo", "a", "El corrector revisa la ortografía, no el sentido.")],
    [
        ("¿Para qué sirve el corrector?", "Para detectar posibles errores de ortografía", "Es una ayuda, pero no lo sabe todo."),
        ("¿Qué significa «publish»?", "Publicar", "Presentar el texto final."),
        ("¿Por qué hay que releer después de usar el corrector?", "Porque no entiende el significado", "Puede dejar pasar errores."),
    ],
    task("Lee este borrador: «my frend is Ana she is eleven she likes swiming». Corrígelo en tu hoja: agrega mayúsculas, puntos y arregla las palabras mal escritas (friend y swimming). Después, pasa el texto limpio a una hoja nueva como si lo publicaras: título arriba en negrita (subráyalo), texto ordenado y tu nombre abajo si quieres. Si tienes computador, repite el trabajo con un procesador de textos y una persona adulta cerca.", "My friend is Ana. She is eleven. She likes swimming.", ["corrige mayúsculas, puntos y las dos palabras", "presenta el título destacado", "el texto final se lee limpio"], ["hoja con borrador corregido y versión final"], ["dejar palabras sin corregir", "no releer"], "Pide que explique qué herramienta usó para cada corrección."),
    "Copia las siete palabras de la lista de herramientas con su significado.",
    "Escribe tres consejos para publicar un texto limpio en inglés.",
)

# ================================================================ OA 15 clase 6: revisar sentido y corregir
lesson(
    OA15, 6,
    "Los borradores escritos en cada ejercicio, lápiz, una hoja y colores o un subrayador.",
    "Aprenderé a revisar y editar mi texto: mayúscula en I, signos de interrogación, vocabulario del tema y expresiones como That's cool! o Great! Sirve para dejar mi texto claro y bien escrito.",
    ["Sé organizar ideas, redactar y usar el diccionario.", "Conozco los signos ? y !"],
    [
        "Revisar es leer tu borrador para ver si el mensaje se entiende. Editar es corregir errores de escritura. Una lista de revisión útil: 1) ¿Cada oración tiene sujeto y verbo? 2) ¿Escribí I con mayúscula? 3) ¿Las preguntas terminan con ? 4) ¿Usé palabras del tema? 5) ¿Mi texto incluye alguna expresión como That's cool! o Great!?",
        "Ejemplo: borrador «i like chess. do you play chess. that's cool» → versión revisada «I like chess. Do you play chess? That's cool!» Se corrigieron: la I, la mayúscula inicial, el ? y el !. Las expresiones comunes (That's cool!, Great!, Well done!) llevan signo de exclamación y mayúscula.",
        "Revisa el sentido: ¿cada oración dice lo que quieres decir? Si una palabra no calza, busca otra en el diccionario. Pide a otra persona que lea tu texto; si algo no se entiende, reescríbelo.",
    ],
    [("revise", "revisar: ver si el mensaje se entiende"), ("edit", "editar: corregir errores"), ("checklist", "lista de revisión"), ("capital letter", "letra mayúscula"), ("question mark", "signo de interrogación"), ("Great!", "¡Genial!"), ("That's cool!", "¡Qué genial!")],
    [
        ("Corregir la I", "Corrige: «i am eleven.»", ["La I siempre va con mayúscula.", "La oración empieza con mayúscula.", "Termina con punto."], "I am eleven."),
        ("Corregir una pregunta", "Corrige: «where is my book.»", ["Where empieza con mayúscula.", "Es una pregunta, entonces lleva ?.", "Se escribe Where is my book?"], "Where is my book?"),
    ],
    [
        ("Corregir solo la ortografía y no el sentido.", "Se revisa una sola cosa.", "Revisa también si el mensaje se entiende."),
        ("Olvidar el signo ! en una expresión como Great.", "No se piensa en la emoción.", "Great! y That's cool! llevan signo de exclamación."),
    ],
    [
        ("¿Cómo se escribe «yo» en inglés?", "I", "Siempre va con mayúscula."),
        ("¿Qué signo termina una pregunta?", "?", "Marca la interrogación."),
        ("¿Qué significa «Great!»?", "¡Genial!", "Es una expresión de alegría."),
    ],
    [
        ("Corrige: «my friend and i play chess.» ¿Qué dos letras cambias? Escribe solo las dos letras ya corregidas separadas por coma.", "M, I", "La m inicial pasa a M y la i pasa a I."),
        ("Corrige: «can you swim» Escribe la oración.", "Can you swim?", "Falta mayúscula y ?."),
        ("Completa con una expresión: «You won the game! ___!» Opciones: Great, Excuse me.", "Great", "Great felicita un logro."),
    ],
    [
        ("Corrige: «i love swimming and i like cycling.»", "I love swimming and I like cycling.", "Las dos I van con mayúscula y la inicial también."),
        ("Texto: «Pablo: do you like tennis. Ana: yes i do that's cool» ¿Cuántos signos ? faltan? Solo el número.", "1", "Solo hay una pregunta."),
        ("Elige el texto corregido: a) Do you like music? Yes, I do. That's cool! b) do you like music. yes i do. thats cool", "a", "Tiene mayúsculas, signos y expresión correctas."),
    ],
    [
        ("Un texto dice «I like tennis because is fun». ¿Qué falta? a) it antes de is b) mayúscula", "a", "Falta el sujeto it."),
        ("Texto: «I like music. do you like music?» ¿Qué falta corregir? a) La D mayúscula inicial b) El signo de interrogación", "a", "El signo ? ya está; falta la mayúscula."),
    ],
    [
        ("Texto: «i go to school. i like Art. do you like art» Cuenta cuántas veces falta mayúscula en I. Solo el número.", "2", "Falta en las dos oraciones que empiezan con i."),
        ("En el mismo texto, ¿qué signo falta al final? Escribe el signo.", "?", "La última oración es pregunta."),
    ],
    [("Escribiste una carta y tu amigo no entiende una oración. ¿Qué haces? a) Reescribirla con otras palabras b) Dejarla igual", "a", "Revisar es mejorar el sentido.")],
    [
        ("¿Qué diferencia hay entre revisar y editar?", "Revisar mira el sentido y editar corrige errores", "Son dos pasos distintos."),
        ("¿Qué expresión sirve para felicitar a alguien?", "Well done!", "Es una expresión común."),
        ("¿Dónde va el signo de interrogación?", "Al final de la pregunta", "Solo se escribe el de cierre."),
    ],
    task("Lee este borrador: «hi i am sam. i like soccer. do you like soccer. that's cool» Revisa y edita en tu hoja con la lista: sujeto y verbo en cada oración, I con mayúscula, ? en las preguntas, palabras del tema y una expresión final con !. Después escribe en otra hoja tu propio borrador de cinco oraciones, revísalo con la misma lista y marca con un visto cada punto cumplido.", "Hi! I am Sam. I like soccer. Do you like soccer? That's cool!", ["corrige las I, las mayúsculas y los signos", "incluye una expresión común con signo !", "marca la lista de revisión en su propio texto"], ["hoja con borrador corregido y lista marcada"], ["olvidar el ? en la pregunta", "dejar la i minúscula"], "Pide que lea en voz alta el texto final y diga qué corrigió."),
    "Copia la versión revisada del ejemplo de la explicación y subraya los cambios.",
    "Escribe un texto de siete oraciones sobre tus pasatiempos y revísalo con la lista de cinco puntos.",
)

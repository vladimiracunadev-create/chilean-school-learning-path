"""Cuaderno del estudiante, 8.º básico Inglés (oficial), IN08 OA 07 (respuesta personal y crítica a textos leídos o escuchados).

Cada texto va escrito dentro del ejercicio, con su pista en español. La discusión se practica por escrito y, si se puede, en voz alta con una persona de tu casa.
"""
from __future__ import annotations

from student_content_in8_a import lesson
from student_content_ma01_b import task
from student_lessons import arith

OA7 = "IN08 OA 07"
MAT = "Lápiz, una hoja y, si puedes, una persona de tu casa para conversar; cada texto viene escrito en el ejercicio."

PLANTS = "«Plants make their own food. They use sunlight, water and air. This process is called photosynthesis.» (plants = plantas, sunlight = luz solar, air = aire, process = proceso, photosynthesis = fotosíntesis)"
SHOES = "«In many countries, people take off their shoes before they enter a house. It shows respect and keeps the floor clean.» (take off = sacarse, shoes = zapatos, enter = entrar, respect = respeto, floor = piso, clean = limpio)"
RICE = "«A rice recipe for six people uses 300 grams of rice. For twelve people, you need double.» (recipe = receta, rice = arroz, grams = gramos, double = el doble)"

# ================================================================== OA 7, clase 1
lesson(
    OA7, 1, MAT,
    "Aprenderé a conectar lo que leo o escucho con otras asignaturas, mi lengua materna, mi vida cotidiana y otras culturas, usando I know (about) this because... e I remember that.... Sirve para dar una respuesta personal a un texto.",
    ["Sé dar la idea general de un texto.", "Conozco la palabra because."],
    [
        "Reaccionar a un texto (to respond to a text) es decir qué piensas o sabes sobre él. Una forma es hacer conexiones (connections): relacionar el texto con algo que ya conoces. Puedes conectar con otras asignaturas (el texto de las plantas se relaciona con Ciencias Naturales), con tu lengua materna (photosynthesis se parece a fotosíntesis), con tu vida cotidiana y tus experiencias personales (lo que haces a diario) o con otras culturas (costumbres de otros países).",
        "En inglés usas frases como I know about this because we studied plants in Science, I remember that in Math we learned to double numbers o This is like what happens when... La palabra because da la razón de tu conexión. Mientras más específica es la conexión, mejor: «because we studied photosynthesis in Science» dice más que «because I like Science».",
        "Una buena conexión debe ser verdadera y relacionarse con una idea del texto. Escoge una frase del texto, piensa en dónde la has visto o aprendido y usa un esquema: I know about this because ___ / I remember that ___. Evita conexiones que no tienen relación con lo que dice el texto.",
    ],
    [("connection", "conexión: relación con algo que conoces"), ("I know about this because...", "sé de esto porque..."), ("I remember that...", "recuerdo que..."), ("subject", "asignatura"), ("culture", "cultura: costumbres de un grupo"), ("experience", "experiencia")],
    [
        ("Conectar con una asignatura", PLANTS + " ¿Con qué asignatura conectas este texto y con qué frase?", ["El texto habla de plantas y de fotosíntesis.", "Eso se estudia en Ciencias Naturales.", "Digo I know about this because we studied plants in Science."], "Con Ciencias Naturales: I know about this because we studied plants in Science"),
        ("Conectar con matemática", RICE + " ¿Con qué asignatura conectas la idea de «double»?", ["Double significa el doble.", "Multiplicar por dos se estudia en Matemática.", "La conexión es con Matemática."], "Con Matemática, porque el doble se calcula multiplicando por 2"),
    ],
    [
        ("Dar una conexión sin relación con el texto.", "La conexión debe relacionarse con una idea del texto.", "Busca una frase del texto y relaciónala con lo que sabes."),
        ("Decir solo «I like it» como conexión.", "No muestra qué sabes ni qué relación hay con el texto.", "Usa because y una experiencia o contenido concretos."),
    ],
    [
        (PLANTS + " ¿Con qué asignatura conectas el texto? a) Ciencias Naturales b) Educación Física", "a) Ciencias Naturales", "Habla de plantas y de fotosíntesis."),
        (SHOES + " ¿Con qué asignatura conectas este texto sobre costumbres? a) Historia, Geografía y Ciencias Sociales b) Matemática", "a) Historia, Geografía y Ciencias Sociales", "Las costumbres de los países se estudian en Ciencias Sociales."),
        ("«I know about this because we studied plants in Science.» ¿Qué muestra esta frase? a) una conexión con otra asignatura b) un plan futuro", "a) una conexión con otra asignatura", "Relaciona el texto con lo que se vio en Ciencias."),
    ],
    [
        (SHOES + " ¿Qué frase hace una conexión con otras culturas? a) In some homes I know, people also take off their shoes. b) I like pizza.", "a) In some homes I know, people also take off their shoes.", "Relaciona la costumbre del texto con otros lugares."),
        (RICE + " ¿Qué parte del texto se conecta con una multiplicación? a) For twelve people, you need double. b) A rice recipe", "a) For twelve people, you need double.", "Double implica multiplicar por 2."),
        ("¿Para qué sirve «I remember that...»? a) para recordar una experiencia o algo aprendido b) para hacer un plan futuro", "a) para recordar una experiencia o algo aprendido", "I remember that introduce un recuerdo."),
    ],
    [
        ("Completa: «I know about this ___ we studied plants in Science.» a) because b) so", "a) because", "Because introduce la razón de la conexión."),
        (PLANTS + " La palabra photosynthesis se parece a «fotosíntesis». ¿Qué tipo de conexión es? a) con la lengua materna b) con las matemáticas", "a) con la lengua materna", "Son palabras parecidas en inglés y en español."),
        (SHOES + " ¿Qué conexión con la vida cotidiana es adecuada? a) In my school we clean the floor to keep the room neat. b) I am going to the beach next week.", "a) In my school we clean the floor to keep the room neat.", "Se relaciona con mantener el piso limpio."),
    ],
    [
        ("Ana dice «I know about this because we studied photosynthesis in Science». Luis dice «I know about this because I like Science». ¿Quién da una conexión más específica? a) Ana b) Luis", "a) Ana", "Nombra el contenido concreto."),
        (RICE + " Pedro dice que con doce personas se necesita el triple. ¿Qué parte del texto lo corrige? a) you need double b) 300 grams of rice", "a) you need double", "El texto dice el doble, no el triple."),
    ],
    [
        arith(RICE + " Aplicando lo que dice el texto, ¿cuántos gramos de arroz se necesitan para doce personas?", "300*2", "Doce personas es el doble de seis.", " gramos"),
        ("Un compañero dice: «I remember that in Social Studies we learned that customs change in each country». ¿Con qué texto lo conectas? a) el de los zapatos en la casa b) el de las plantas", "a) el de los zapatos en la casa", "Habla de costumbres que cambian."),
    ],
    [("Lees: «A tap that drips can waste water.» (tap = llave, drips = gotea, waste = desperdiciar). Dices: «I know about this because I close the tap when I brush my teeth.» ¿Qué tipo de conexión es? a) una experiencia personal b) una conexión con otra asignatura", "a) una experiencia personal", "Habla de algo que haces tú.")],
    [
        ("En Inglés de 8.º (OA 7, clase 1): ¿Qué es una conexión con un texto?", "Relacionarlo con algo que ya conoces", "Puede ser con otra asignatura o con tu vida."),
        ("¿Qué palabra da la razón de tu conexión?", "Because", "I know this because..."),
        ("¿Qué frase sirve para recordar algo aprendido?", "I remember that...", "Introduce un recuerdo."),
    ],
    task("Lee este texto de ejemplo: «In some countries, people greet each other with a bow. In others, they shake hands.» (greet = saludan, bow = reverencia, shake hands = dan la mano). Escribe tres conexiones con frases en inglés: una con otra cultura, una con tu vida cotidiana y una con una asignatura (por ejemplo, Historia).", "I remember that in Social Studies we learned that customs change. In my school we greet teachers with a handshake or a smile. I know about this because some countries have different customs.", ["escribe tres conexiones distintas", "usa because o I remember that", "se relacionan con el texto"], ["hoja con tres frases", "nota de una persona de tu casa"], ["escribir conexiones sin relación con el saludo", "no usar because"], "Reconoce la mejor conexión y ayuda a hacer más específica la que dice solo «I like»."),
    "Lee en voz alta el texto de las plantas y di una conexión con tu experiencia en Ciencias.",
    "Elige un texto breve de otra asignatura y escribe dos conexiones con I know about this because... e I remember that...",
)

# ------------------------------------------------------------------ OA 7, clase 2
TRIP = "«The class can choose a trip. Option A is the science museum. It costs 2,000 pesos for each student and has forty experiments. Option B is the city park. It is free, and students can play football. The park is closer than the museum, but the museum is more interesting.» (option = opción, experiments = experimentos, free = gratis, closer = más cerca, interesting = interesante)"

lesson(
    OA7, 2, MAT,
    "Aprenderé a dar mi opinión, hacer comparaciones y justificarlas con because. Uso frases como I think..., ... is more important than..., ... is the oldest... y you should/shouldn't... because.... Sirve para participar en una discusión con razones.",
    ["Sé comparar con -er than y more... than.", "Conozco should y because."],
    [
        "Una opinión (opinion) es lo que piensas; una justificación (justification) es la razón con because. Un buen esquema es: I think + opinión + because + razón. Por ejemplo: I think we should go to the park because it is free. Sin razón, la opinión es débil.",
        "Para comparar, usa el comparativo o el superlativo: The park is closer than the museum; The museum is more interesting than the park; It is the cheapest option. Para decir qué es más importante: Safety is more important than speed. Para el más antiguo: The lighthouse is the oldest building in the town because it was built long ago. Para dar un consejo: You should wear a helmet because it protects your head; You shouldn't run on the stairs because you can fall.",
        "Cuando alguien opina distinto, puedes responder con respeto: I see your point, but I think... Usa datos del texto para apoyar tu opinión: costs 2,000 pesos, forty experiments, free. Una razón basada en datos es más fuerte que una basada solo en gustos.",
    ],
    [("I think... because...", "creo que... porque..."), ("justify", "justificar: dar la razón"), ("more important than", "más importante que"), ("the oldest", "el más antiguo"), ("you should / shouldn't", "deberías / no deberías"), ("I see your point, but...", "entiendo tu punto, pero...")],
    [
        ("Opinión con razón", TRIP + " Usa un dato del texto para justificar: «I think we should go to the park because...»", ["El texto dice que el parque es gratis.", "Esa es una razón basada en un dato.", "I think we should go to the park because it is free."], "I think we should go to the park because it is free"),
        ("Comparar con el texto", TRIP + " ¿Qué opción es más barata y cuál es más interesante, según el texto?", ["El parque es gratis; el museo cuesta 2.000 pesos.", "El texto dice que el museo es más interesante.", "Más barata: el parque. Más interesante: el museo."], "Más barata: el parque; más interesante: el museo"),
    ],
    [
        ("Dar una opinión sin razón.", "Sin because no se sabe por qué piensas así.", "Agrega because y un dato."),
        ("Decir «more cheap» en vez de cheaper.", "Cheap es un adjetivo corto y lleva -er.", "Di cheaper than."),
    ],
    [
        (TRIP + " ¿Qué opción es gratis? a) el parque b) el museo", "a) el parque", "El texto dice It is free."),
        (TRIP + " ¿Qué frase justifica una opinión? a) I think we should go to the museum because it has forty experiments. b) I think we should go to the museum.", "a) I think we should go to the museum because it has forty experiments.", "Tiene la razón con because."),
        (TRIP + " ¿Qué opción está más cerca? a) el parque b) el museo", "a) el parque", "Dice The park is closer than the museum."),
    ],
    [
        ("Completa: «Safety is ___ than speed.» a) more important b) importanter", "a) more important", "Important es largo y usa more."),
        ("Completa: «This is ___ building in the town» (old). a) the oldest b) the most old", "a) the oldest", "Old es corto y su superlativo lleva -est."),
        ("¿Qué consejo es correcto? a) You should wear a helmet because it protects your head. b) You should wearing a helmet.", "a) You should wear a helmet because it protects your head.", "Should va con el verbo en forma base."),
    ],
    [
        arith(TRIP + " Si 25 estudiantes van al museo, ¿cuántos pesos se pagan en total?", "25*2000", "El museo cuesta 2.000 pesos por estudiante.", " pesos"),
        (TRIP + " Camila dice: «The museum is cheaper than the park». ¿Qué dato del texto la contradice? a) The park is free. b) The museum has forty experiments.", "a) The park is free.", "Gratis es más barato que 2.000 pesos."),
        ("Elige la mejor respuesta a un compañero que opina distinto: a) I see your point, but I think we should go to the park because it is free. b) You are wrong.", "a) I see your point, but I think we should go to the park because it is free.", "Reconoce el punto del otro y justifica con un dato."),
    ],
    [
        (TRIP + " Pedro dice: «Elijo el museo porque sí». ¿Qué le falta? a) una razón con because b) más gritos", "a) una razón con because", "Una opinión necesita justificación."),
        (TRIP + " Lucas dice: «The park is better than the museum because it is closer and free». Ana dice: «The museum is better than the park because I like experiments». ¿Cuál justificación usa más datos del texto? a) la de Lucas b) la de Ana", "a) la de Lucas", "Usa dos datos del texto: cercanía y precio."),
    ],
    [
        ("Un compañero dice «You shouldn't run on the stairs because you can fall». ¿Qué función cumple? a) dar un consejo con razón b) hacer una pregunta", "a) dar un consejo con razón", "Shouldn't da un consejo y because explica."),
        ("Elige la frase que compara y justifica: a) Reading is more important than watching TV because it helps you learn words. b) Reading is TV.", "a) Reading is more important than watching TV because it helps you learn words.", "Compara y da una razón."),
    ],
    [("Tu curso debate si el recreo debe tener juegos de pelota o juegos de mesa. Quieres dar tu opinión con razón. ¿Cuál frase es mejor? a) I think ball games are better because we need to move after sitting in class. b) I think ball games are better.", "a) I think ball games are better because we need to move after sitting in class.", "Agrega una razón con because.")],
    [
        ("¿Qué esquema usa una opinión justificada?", "I think + opinión + because + razón", "Ordena la opinión y su razón."),
        ("En Inglés de 8.º (OA 7, clase 2): ¿Cómo se dice «el más antiguo» con old?", "The oldest", "Superlativo de un adjetivo corto."),
        ("¿Qué palabra da un consejo?", "Should", "You should... da un consejo."),
    ],
    task("Lee este texto de ejemplo: «Bike A costs 90,000 pesos and has three gears. Bike B costs 120,000 pesos and has twenty-one gears.» (gears = cambios). Escribe una opinión justificada sobre cuál comprarías, con un comparativo y un dato, y un consejo con should o shouldn't.", "I think bike B is better than bike A because it has more gears. You should save money before buying it.", ["da una opinión con because", "usa un comparativo", "incluye un consejo con should/shouldn't"], ["hoja con opinión y consejo", "nota de una persona de tu casa"], ["no usar un dato del texto", "decir more cheap"], "Reconoce la opinión mejor apoyada y agrega un dato en la que solo usa gustos."),
    "Di en voz alta tres opiniones con I think... because... sobre un tema de tu curso.",
    "Escribe un consejo con should y otro con shouldn't para una persona que va a andar en bicicleta.",
)

# ------------------------------------------------------------------ OA 7, clase 3
TOWN = "«The town will open a new bike lane next year. It will connect the school with the main square. Right now, 60 students come to school by bike. The school hopes that more students will join them.» (bike lane = ciclovía, connect = conectar, main square = plaza principal, hopes = espera, join = unirse)"

lesson(
    OA7, 3, MAT,
    "Aprenderé a hacer predicciones y explicarlas con there will be... because..., I think there will... e I know/find.... Sirve para opinar sobre lo que podría ocurrir según un texto.",
    ["Sé que will habla del futuro.", "Conozco because y so."],
    [
        "Una predicción (prediction) es decir qué crees que va a pasar. En inglés usas will: There will be more bikes next year; I think there will be fewer cars. Puedes agregar tu razón con because: I think there will be more students on bikes because the lane will be safer. También puedes introducir lo que sabes: I know that the lane will connect the school and the square; I find that many students live nearby.",
        "Una buena predicción se apoya en datos del texto. El texto dice que ahora 60 estudiantes van en bicicleta y que el colegio espera más. Con eso es razonable predecir que habrá más bicicletas, pero no es razonable predecir que no habrá ninguna. Pregúntate: ¿qué dato del texto apoya mi predicción?",
        "Usa I think para mostrar que no estás seguro y will para la predicción. Compara predicciones: ¿cuál tiene mejor razón? La que se apoya en un dato del texto es la más fuerte. Si luego sabes qué ocurrió, puedes decir si tu predicción se cumplió o no.",
    ],
    [("prediction", "predicción: lo que crees que pasará"), ("will", "futuro: habrá, será, hará"), ("I think there will be...", "creo que habrá..."), ("I know that...", "sé que..."), ("I find that...", "encuentro que..."), ("safer", "más segura")],
    [
        ("Hacer una predicción apoyada", TOWN + " Escribe una predicción con there will be y because.", ["El texto dice que habrá una ciclovía nueva.", "Eso hace pensar que más estudiantes usarán bicicleta.", "I think there will be more bikes because the lane will be safer."], "I think there will be more bikes because the lane will be safer"),
        ("Revisar una predicción", TOWN + " Un compañero dice: «There will be no bikes next year». ¿Se apoya en el texto?", ["Ahora hay 60 estudiantes en bicicleta.", "El colegio espera que más se unan.", "Predecir que no habrá bicicletas contradice el texto."], "No, porque el texto dice que ya hay 60 y se espera que sean más"),
    ],
    [
        ("Hacer una predicción que contradice el texto.", "No se apoya en datos.", "Busca un dato que apoye tu predicción."),
        ("Usar present en lugar de will para predecir: «There are more bikes next year».", "El futuro necesita will.", "Di There will be more bikes next year."),
    ],
    [
        (TOWN + " ¿Cuándo abrirá la ciclovía? a) el próximo año b) hoy", "a) el próximo año", "Dice will open a new bike lane next year."),
        (TOWN + " ¿Qué conectará la ciclovía? a) el colegio con la plaza principal b) la plaza con el parque", "a) el colegio con la plaza principal", "Dice connect the school with the main square."),
        (TOWN + " ¿Cuántos estudiantes van hoy en bicicleta? a) 60 b) 160", "a) 60", "Dice 60 students come to school by bike."),
    ],
    [
        ("¿Qué predicción se apoya en el texto? a) I think there will be more bikes because the lane will be safer. b) I think there will be no students.", "a) I think there will be more bikes because the lane will be safer.", "El texto habla de más estudiantes en bicicleta."),
        ("Completa: «Next year, there ___ more bikes.» a) will be b) are", "a) will be", "Para el futuro se usa will."),
        ("¿Qué frase muestra que no estás seguro? a) I think there will be more bikes. b) There will be more bikes for sure.", "a) I think there will be more bikes.", "I think expresa una opinión no segura."),
    ],
    [
        arith("Si 60 estudiantes van en bicicleta hoy y se espera que se sumen 30 más (dato de ejemplo), ¿cuántos podrían ir en total?", "60+30", "Se suman los que van hoy y los que se unen.", " estudiantes"),
        ("Elena predice: «There will be fewer cars near the school because more students will use the lane». ¿Qué relación muestra because? a) razón de la predicción b) orden de acciones", "a) razón de la predicción", "Because explica por qué pasaría."),
        (TOWN + " ¿Qué frase del texto dice que se espera que haya más estudiantes en bicicleta? a) The school hopes that more students will join them. b) It will connect the school with the main square.", "a) The school hopes that more students will join them.", "Dice que se espera que más estudiantes se sumen."),
    ],
    [
        ("Luis dice: «I know that the lane connects the school with the square, so I think more students will come by bike». Ana dice: «I think more students will come by bike because I like bikes». ¿Cuál predicción se apoya mejor en el texto? a) la de Luis b) la de Ana", "a) la de Luis", "Usa un dato del texto."),
        ("Si dentro de un año hay 100 estudiantes en bicicleta, ¿se cumplió la predicción de más bicicletas? a) sí, porque 100 es más que 60 b) no, porque 100 es menos que 60", "a) sí, porque 100 es más que 60", "Hay más estudiantes que antes."),
    ],
    [
        ("Un compañero dice «I find that many students live near the school, so there will be more bikes». ¿Qué predicción hace? a) habrá más bicicletas b) habrá menos bicicletas", "a) habrá más bicicletas", "So muestra el resultado esperado."),
        ("¿Qué predicción es más razonable si el invierno es muy lluvioso? a) I think fewer students will come by bike on rainy days. b) I think nobody will walk in the rain.", "a) I think fewer students will come by bike on rainy days.", "Es una predicción moderada y razonable."),
    ],
    [("Lees: «The school will plant fifty trees next month.» Quieres predecir qué pasará con el patio. ¿Cuál frase es razonable? a) I think the school yard will be greener because there will be more trees. b) I think the school yard will disappear.", "a) I think the school yard will be greener because there will be more trees.", "Se apoya en el dato de los árboles.")],
    [
        ("¿Qué palabra se usa para predecir en inglés?", "Will", "Will habla del futuro."),
        ("En Inglés de 8.º (OA 7, clase 3): ¿Qué hace más fuerte una predicción?", "Un dato del texto que la apoye", "La razón se basa en evidencia."),
        ("¿Qué frase usas para introducir algo que sabes?", "I know that...", "Presenta un dato conocido."),
    ],
    task("Lee este texto de ejemplo: «The library will have a new reading room next month. It will have twenty chairs and two big tables. The librarian hopes that more students will come after school.» (reading room = sala de lectura, chairs = sillas, librarian = bibliotecaria). Escribe dos predicciones: una con there will be y otra con I think... because...; ambas apoyadas en el texto.", "There will be more students in the library. I think there will be more readers because the new room will be comfortable.", ["escribe dos predicciones", "una usa there will be", "otra usa I think... because..."], ["hoja con dos predicciones", "nota de una persona de tu casa"], ["contradecir el texto", "no dar razón"], "Reconoce la predicción más apoyada y agrega un dato del texto a la otra."),
    "Di en voz alta dos predicciones sobre tu barrio con there will be.",
    "Escribe tres predicciones para tu colegio dentro de cinco años y una razón para cada una.",
)

# ------------------------------------------------------------------ OA 7, clase 4
LIGHT = "«The lighthouse stands on a rock near the coast. Its light turns and can be seen from far away. Ships use it to find the coast at night. Today, many lighthouses work automatically, so there are fewer keepers.» (lighthouse = faro, rock = roca, coast = costa, turns = gira, ships = barcos, automatically = automáticamente, keepers = fareros)"
BEES2 = "«Bees visit flowers to collect nectar. While they do this, pollen sticks to their bodies. When they visit the next flower, some pollen falls off, and the flower can make seeds. Because of this, bees help many fruits and vegetables to grow.» (nectar = néctar, pollen = polen, sticks = se pega, falls off = cae, seeds = semillas, fruits = frutas)"

lesson(
    OA7, 4, MAT,
    "Aprenderé a resumir y sintetizar la información de un texto con oraciones simples y descripciones breves. Sirve para contar lo más importante a otra persona con mis propias palabras.",
    ["Sé encontrar la idea general de un texto.", "Conozco conectores como because, so y then."],
    [
        "Resumir (to summarize) es contar lo más importante de un texto con menos palabras. Sintetizar (to synthesize) es reunir las ideas de uno o varios textos en un mensaje corto. En 8.º lo haces con oraciones simples: sujeto + verbo + dato. Por ejemplo, del texto del faro puedes escribir: The lighthouse helps ships find the coast at night. Today, many lighthouses work automatically.",
        "Para resumir, sigue tres pasos. Primero, subraya la idea principal de cada oración. Segundo, elimina los detalles menos importantes, como los ejemplos o los números pequeños. Tercero, une las ideas con conectores como so, because, then o also. Un resumen no copia el texto, no agrega opiniones y mantiene el orden de las ideas.",
        "Una descripción breve (short description) dice cómo es algo con pocas palabras: It is a tall tower with a turning light. Combina la descripción con el resumen para dar una idea completa. Revisa que cada oración sea simple y esté bien escrita. Si puedes explicar el texto a otra persona en dos o tres oraciones, lo comprendiste.",
    ],
    [("summarize", "resumir"), ("synthesize", "sintetizar: reunir ideas en un mensaje corto"), ("main idea", "idea principal"), ("detail", "detalle"), ("short description", "descripción breve"), ("in your own words", "con tus propias palabras")],
    [
        ("Elegir el mejor resumen", LIGHT + " ¿Cuál es un buen resumen? a) The lighthouse helps ships find the coast at night, and many now work automatically. b) The lighthouse is on a rock and there are keepers.", ["Un buen resumen recoge las ideas principales.", "La primera opción dice la función y el cambio actual.", "La segunda solo menciona detalles."], "a) The lighthouse helps ships find the coast at night, and many now work automatically."),
        ("Quitar un detalle", BEES2 + " ¿Qué detalle puedes quitar de un resumen breve: que las abejas visitan flores o que el polen se pega a su cuerpo?", ["La idea principal es que las abejas ayudan a que crezcan frutas.", "El polen pegado es un detalle del proceso.", "Se puede quitar que el polen se pega a su cuerpo."], "Que el polen se pega a su cuerpo"),
    ],
    [
        ("Copiar el texto casi completo.", "Un resumen es más corto y usa tus palabras.", "Elige las ideas principales y reescribe."),
        ("Agregar opiniones como «I think the lighthouse is beautiful».", "El resumen solo repite lo que dice el texto.", "Deja tus opiniones para otra respuesta."),
    ],
    [
        (LIGHT + " ¿Cuál es la idea principal? a) el faro ayuda a los barcos a encontrar la costa de noche b) los fareros viven en rocas", "a) el faro ayuda a los barcos a encontrar la costa de noche", "Es la función central del faro."),
        (BEES2 + " ¿Para qué visitan las abejas las flores? a) para recoger néctar b) para pintar las flores", "a) para recoger néctar", "Dice Bees visit flowers to collect nectar."),
        (LIGHT + " ¿Qué ocurre hoy con muchos faros? a) funcionan automáticamente b) tienen más fareros", "a) funcionan automáticamente", "Dice many lighthouses work automatically."),
    ],
    [
        (BEES2 + " ¿Qué resumen es mejor? a) Bees carry pollen between flowers, so many fruits and vegetables can grow. b) Bees have pollen on their bodies.", "a) Bees carry pollen between flowers, so many fruits and vegetables can grow.", "Dice la acción y el resultado."),
        (LIGHT + " ¿Qué conector une «many lighthouses work automatically» con «there are fewer keepers»? a) so b) until", "a) so", "Muestra el resultado: hay menos fareros."),
        (BEES2 + " ¿Qué descripción breve del polen es adecuada? a) It sticks to the bees and falls on other flowers. b) It is a big yellow fruit.", "a) It sticks to the bees and falls on other flowers.", "Describe lo que dice el texto."),
    ],
    [
        (LIGHT + " Elige la descripción breve del faro: a) It is a tall building with a turning light. b) It is a small boat with a flag.", "a) It is a tall building with a turning light.", "Sigue la información del texto."),
        (BEES2 + " Marta resumió: «Bees help plants grow». ¿Qué le falta para ser un resumen más completo? a) decir cómo ayudan: llevan polen de flor en flor b) decir cuántas abejas hay", "a) decir cómo ayudan: llevan polen de flor en flor", "Falta la explicación del proceso."),
        (LIGHT + " ¿Cuántas ideas principales hay en este resumen: «The lighthouse helps ships. Many lighthouses are automatic.»?", "2", "Hay una oración sobre la función y otra sobre el cambio actual."),
    ],
    [
        ("Un resumen dice: «The lighthouse is beautiful and I love it». ¿Qué problema tiene? a) agrega una opinión que el texto no dice b) es demasiado corto", "a) agrega una opinión que el texto no dice", "Un resumen solo repite el contenido del texto."),
        (BEES2 + " ¿Qué expresión del texto introduce el resultado final de la visita de las abejas? a) Because of this b) While they do this", "a) Because of this", "Because of this (por esto) introduce que las abejas ayudan a que crezcan frutas."),
    ],
    [
        ("Lees: «The school canteen opens at noon. It serves soup and bread. Students pay with a card. The soup is vegetarian on Fridays.» (canteen = comedor, noon = mediodía, serves = sirve, vegetarian = vegetariana). ¿Cuál es el mejor resumen? a) The canteen opens at noon and serves soup and bread. b) Students like the soup.", "a) The canteen opens at noon and serves soup and bread.", "Recoge los datos principales."),
        ("Del mismo texto, ¿qué detalle puedes quitar de un resumen muy breve? a) The soup is vegetarian on Fridays. b) The canteen opens at noon.", "a) The soup is vegetarian on Fridays.", "Es un detalle menor."),
    ],
    [("Un compañero que no leyó el texto del faro te pregunta de qué trata. ¿Qué respuesta le das? a) The lighthouse helps ships find the coast at night, and now many work automatically. b) I don't know.", "a) The lighthouse helps ships find the coast at night, and now many work automatically.", "Es un resumen breve de la información principal.")],
    [
        ("En Inglés de 8.º (OA 7, clase 4): ¿qué haces al resumir un texto con tus palabras?", "Contar lo más importante con menos palabras", "Mantiene las ideas principales."),
        ("En Inglés de 8.º (OA 7, clase 4): ¿Qué se quita al resumir?", "Los detalles menos importantes", "Se deja la idea principal."),
        ("¿Un resumen incluye opiniones tuyas?", "No", "Solo repite lo que dice el texto."),
    ],
    task("Lee este texto de ejemplo: «The old tram runs through the city centre. It is painted red and yellow. It carries tourists and students. It stops at ten places. Last year, the city repaired its rails.» (tram = tranvía, runs = recorre, painted = pintado, carries = lleva, tourists = turistas, stops = se detiene, repaired = reparó, rails = rieles). Escribe un resumen de dos oraciones simples y una descripción breve del tranvía.", "The old tram runs through the city centre and carries tourists and students. Last year, the city repaired its rails. Description: it is red and yellow.", ["escribe dos oraciones simples", "incluye una descripción breve", "no agrega opiniones"], ["resumen y descripción", "nota de una persona de tu casa"], ["copiar todo el texto", "agregar «I like it»"], "Reconoce la idea principal que dejó y ayuda a quitar un detalle menor."),
    "Cuenta a una persona de tu casa el texto de las abejas en dos oraciones.",
    "Escribe un resumen de tres oraciones de una noticia o texto breve que hayas leído esta semana.",
)

# ------------------------------------------------------------------ OA 7, clase 5
lesson(
    OA7, 5, MAT,
    "Aprenderé a generar preguntas sobre un texto con Whose...?, How much taller is...? y When...? Sirve para conversar, comprobar la información y participar en una discusión.",
    ["Sé hacer preguntas con who, what y where.", "Conozco comparativos como taller."],
    [
        "Hacer preguntas (to ask questions) te ayuda a comprender mejor y a mantener una conversación. Whose pregunta por el dueño de algo: Whose bags are these? (¿De quién son estas mochilas?). Se responde con un nombre más 's: They are Ana's. How much taller... pregunta por una diferencia entre dos alturas: How much taller is Leo than Tina? Se responde con una cantidad: He is 12 centimetres taller.",
        "When pregunta por el tiempo: When is the party? On Saturday at ten. How many pregunta por una cantidad contable: How many students came? How much pregunta por una cantidad no contable o un precio: How much is the ticket? Which pregunta por una opción entre varias. Para formar la pregunta, pon la palabra interrogativa al comienzo y sigue con el verbo: When is the concert?, Whose pen is this? Con otros verbos usa do o does: How many cats does Mia have?, What time does the concert start?",
        "Una buena pregunta se puede responder con el texto. Antes de preguntar, lee los datos y piensa: ¿qué quiero saber? Después, elige la palabra interrogativa que corresponde al dato: tiempo, dueño, cantidad, diferencia. Con ayuda de un modelo o una lista de palabras, formula la pregunta completa.",
    ],
    [("Whose...?", "¿De quién...?"), ("How much taller...?", "¿Cuánto más alto...?"), ("When...?", "¿Cuándo...?"), ("How many...?", "¿Cuántos...?"), ("How much...?", "¿Cuánto cuesta / cuánta cantidad...?"), ("Which...?", "¿Cuál...?")],
    [
        ("Formar una pregunta de posesión", "Datos: las mochilas azules son de Ana. Escribe la pregunta que obtiene esta respuesta: «They are Ana's».", ["La respuesta nombra al dueño.", "La palabra interrogativa para el dueño es Whose.", "Whose bags are these?"], "Whose bags are these?"),
        ("Preguntar por una diferencia", "Datos de ejemplo: Leo mide 160 centímetros y Tina mide 148 centímetros. ¿Qué pregunta y qué respuesta obtienes con How much taller?", ["La pregunta compara las alturas de Leo y Tina.", "Se restan: 160 - 148 = 12.", "How much taller is Leo than Tina? He is 12 centimetres taller."], "How much taller is Leo than Tina? Doce centímetros"),
    ],
    [
        ("Usar Who en vez de Whose para preguntar el dueño.", "Who pregunta por una persona; Whose pregunta por el dueño de algo.", "Si preguntas «¿de quién es?», usa Whose."),
        ("Poner el verbo antes de la palabra interrogativa: «Is when the party?».", "La palabra interrogativa va al comienzo.", "Di When is the party?"),
    ],
    [
        ("La respuesta es «On Saturday». ¿Qué pregunta corresponde? a) When is the party? b) Whose is the party?", "a) When is the party?", "On Saturday responde por el tiempo."),
        ("La respuesta es «They are Ana's». ¿Qué pregunta corresponde? a) Whose bags are these? b) How many bags are these?", "a) Whose bags are these?", "Ana's indica el dueño."),
        ("La respuesta es «Four thousand pesos». ¿Qué pregunta corresponde? a) How much is the ticket? b) When is the ticket?", "a) How much is the ticket?", "Pregunta por un precio."),
    ],
    [
        ("Completa la pregunta: «___ pen is this?» (de quién) a) Whose b) Who", "a) Whose", "Pregunta por el dueño."),
        ("Completa la pregunta: «How ___ students came?» (cantidad contable) a) many b) much", "a) many", "Students se cuentan."),
        arith("Datos de ejemplo: Marcos mide 175 cm y Dani mide 161 cm. ¿Cuántos centímetros más alto es Marcos que Dani?", "175-161", "Se resta la altura menor a la mayor.", " cm"),
    ],
    [
        ("Datos de ejemplo: el concierto es en diciembre. ¿Qué pregunta tiene esa respuesta? a) When is the concert? b) Whose is the concert?", "a) When is the concert?", "In December responde cuándo."),
        ("Datos de ejemplo: Ema mide 152 cm, Pía mide 139 cm. ¿Qué pregunta y respuesta son correctas? a) How much taller is Ema than Pía? 13 cm b) How much taller is Pía than Ema? 13 cm", "a) How much taller is Ema than Pía? 13 cm", "Ema es más alta; 152 - 139 = 13."),
        ("¿Qué pregunta formula bien Whose? a) Whose bike is this? b) Whose is bike this?", "a) Whose bike is this?", "Whose va con el sustantivo y luego el verbo."),
    ],
    [
        ("Pedro pregunta «Who bag is this?» y quiere saber el dueño. ¿Qué corriges? a) Whose bag is this? b) What bag is this?", "a) Whose bag is this?", "Para el dueño se usa Whose."),
        ("Lees: «The concert starts at 7 pm and the tickets cost 5,000 pesos». ¿Qué dos preguntas puedes hacer? a) What time does the concert start? How much are the tickets? b) Whose concert is it? Why is it 7?", "a) What time does the concert start? How much are the tickets?", "Se responden con los datos del texto."),
    ],
    [
        ("Del texto «Mia has three cats and Ben has two dogs», ¿qué pregunta con How many tiene respuesta? a) How many cats does Mia have? b) How many fish does Mia have?", "a) How many cats does Mia have?", "El texto dice que tiene tres gatos."),
        arith("Datos de ejemplo: la torre A mide 50 metros y la torre B mide 38 metros. ¿Cuántos metros más alta es la torre A?", "50-38", "Se resta la altura menor a la mayor.", " metros"),
    ],
    [("Ves tres mochilas sin dueño en la sala y quieres saber de quién son. ¿Cuál es la mejor pregunta? a) Whose bags are these? b) Where are the bags?", "a) Whose bags are these?", "Whose averigua a quién pertenecen.")],
    [
        ("¿Con qué palabra preguntas por el dueño de algo?", "Whose", "Whose bag is this?"),
        ("En Inglés de 8.º (OA 7, clase 5): ¿Qué pregunta usas para saber cuánto más alta es una persona que otra?", "How much taller is... than...?", "Pregunta por la diferencia."),
        ("¿Qué pregunta usas para el tiempo?", "When", "When is the party?"),
    ],
    task("Lee estos datos de ejemplo: «The school fair is on Friday. The tickets cost 1,500 pesos. Tomás is 158 cm tall and Sara is 145 cm tall. The red pencil case is Sara's.» (fair = feria, tickets = entradas, tall = alto, pencil case = estuche). Escribe cuatro preguntas en inglés que se puedan responder con estos datos, usando When, How much, How much taller y Whose.", "When is the school fair? How much are the tickets? How much taller is Tomás than Sara? Whose is the red pencil case?", ["escribe cuatro preguntas", "usa las cuatro palabras interrogativas", "cada pregunta tiene respuesta en los datos"], ["hoja con cuatro preguntas", "nota de una persona de tu casa"], ["usar Who en vez de Whose", "hacer preguntas sin respuesta en los datos"], "Reconoce las preguntas bien formadas y corrige solo el orden de las palabras en la que falló."),
    "Haz a una persona de tu casa tres preguntas con When, Whose y How many sobre objetos de la casa.",
    "Escribe cinco preguntas en inglés para una entrevista a un compañero, con las palabras When, Whose, How much y Which.",
)

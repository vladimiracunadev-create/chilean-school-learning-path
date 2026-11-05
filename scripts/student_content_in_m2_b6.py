"""Cuaderno del estudiante, 2.º medio Inglés (oficial), IN2M OA 15: escribir para analizar, narrar y opinar.

Trabajo con borradores y modelos escritos en el enunciado. Se usan comillas dobles de estilo americano en el diálogo.
Textos originales, inglés americano. Los títulos de clase del plan son genéricos; aquí se aplican a opinión con razones,
narración con diálogo, análisis (causa y efecto, ventajas y desventajas), variedad de palabras, oraciones y conectores,
ortografía y puntuación (comillas), y repaso y transferencia.
"""
from __future__ import annotations

from in_m2_common import MAT_R, arith, lesson, mc, mr, task

OA = "IN2M OA 15"

# ------------------------------------------------------------------ clase 1: opinión con razones
OP1 = "Párrafo de opinión A: «I believe that cities should build more bike lanes. First, bike lanes make riding safer. Second, they reduce traffic. For example, many students ride to school every morning, and a safe lane protects them. In conclusion, more bike lanes would help more students.» (bike lanes = ciclovías, safer = más seguro, reduce = reducir, traffic = tránsito, protects = protege, in conclusion = en conclusión)"
OP2 = "Párrafo de opinión B: «Bike lanes are good. They are nice. I like them. Everybody should use them.»"
OP3 = "Párrafo de opinión C: «I disagree with the idea that students should choose all their classes. Although choice is important, students need a basic education. Neither art nor math should be optional. As a result, I think students could choose only some classes.» (choice = elección, basic = básica, optional = optativa, only some = solo algunas)"

lesson(
    OA, 1, MAT_R,
    "Aprenderé a escribir un párrafo de opinión con una afirmación clara, razones, un ejemplo y una conclusión, usando I believe that/in, I agree/disagree y conectores. Sirve para expresar mi punto de vista de forma convincente.",
    ["Sé usar because y so.", "Conozco I think y in my opinion."],
    [
        "Un párrafo de opinión (opinion paragraph) tiene cuatro partes. La afirmación (claim) dice tu postura: I believe that cities should have more public libraries. Las razones (reasons) la apoyan, con First y Second. El ejemplo (example) muestra un caso concreto: For example, many students without internet use the library. La conclusión (conclusion) cierra con In conclusion o To sum up y repite tu postura con otras palabras.",
        "Para dar fuerza a tu opinión, usa frases como I believe that, I agree with, I disagree with, In my opinion y I strongly feel that. Usa conectores para unir razones: because, so, although, as a result y neither ... nor. Con neither ... nor, el verbo concuerda con el sujeto más cercano: Neither art nor math is optional.",
        "Evita las opiniones sin razón (I like it, everybody should use them). Una opinión necesita al menos dos razones y un ejemplo. También evita repetir la misma palabra: usa sinónimos, como good, useful o helpful. Cierra siempre con una conclusión que refuerce la afirmación.",
    ],
    [("claim", "afirmación: tu postura"), ("reason", "razón"), ("example", "ejemplo"), ("conclusion", "conclusión"), ("I believe that / I disagree with", "creo que / no estoy de acuerdo con"), ("although / as a result", "aunque / como resultado")],
    [
        ("Reconocer las partes", OP1 + " ¿Cuáles son la afirmación y las razones?", ["La afirmación está en la primera oración.", "Las razones aparecen con First y Second.", "El ejemplo viene con For example."], "Afirmación: las ciudades deberían construir más ciclovías. Razones: andar es más seguro y hay menos tránsito"),
        ("Mejorar una opinión débil", OP2 + " ¿Qué le falta?", ["Dice que las ciclovías son buenas, pero no por qué.", "No da razones ni ejemplo ni conclusión.", "Debe agregarlos."], "Le faltan razones, un ejemplo y una conclusión"),
    ],
    [
        ("Escribir I like it como única razón.", "No convence a quien lee.", "Da dos razones y un ejemplo."),
        ("Usar Neither art nor math are optional.", "El verbo concuerda con el sujeto más cercano, math.", "Escribe Neither art nor math is optional."),
    ],
    [
        mr(OP1, "¿Qué palabras introducen las razones?", "First y Second", ["Although y unless", "Never y always"], "Ordenan las razones."),
        mr(OP1, "¿Qué ejemplo da el autor?", "Muchos estudiantes van en bicicleta al colegio cada mañana", ["Los profesores van al colegio en bicicleta los fines de semana", "Las ciclovías son más baratas que construir más calles"], "Dice many students ride to school every morning."),
        mr(OP3, "¿Cuál es la postura de C?", "Los estudiantes podrían elegir solo algunas clases", ["Los estudiantes deberían elegir todas sus clases libremente", "Ningún estudiante debería poder elegir clases"], "Dice students could choose only some classes."),
    ],
    [
        mr(OP3, "¿Qué conector marca contraste en C?", "Although", ["As a result", "First"], "Although introduce el contraste."),
        mr(OP2, "¿Cuál de estas oraciones es una opinión sin razón?", "I like them", ["Libraries give free access", "Many students study there"], "No explica por qué."),
        mr(OP1, "¿Qué frase introduce la conclusión?", "In conclusion", ["For example", "Second"], "In conclusion cierra el párrafo."),
    ],
    [
        mc("Completa: Neither art nor math ____ optional in my opinion.", "is", ["are", "be"], "El verbo concuerda con math, que está más cerca."),
        mc("Elige la afirmación más clara (una postura, no un hecho ni un tema):", "I believe that schools should start later", ["Many schools start at eight o'clock every morning", "In this paragraph I will write about school times"], "Dice la postura con una oración completa; las otras dan un hecho o anuncian el tema."),
        mr(OP2, "Mejora la oración «Bike lanes are good». ¿Cuál es mejor?", "Bike lanes are useful because they make riding safer for students", ["Bike lanes are very, very good for all the people in the city", "Bike lanes are useful because they are useful for everybody"], "Agrega una razón concreta; las otras repiten la idea sin explicarla."),
    ],
    [
        mr(OP1, "Un compañero dice que el párrafo A solo da una razón. ¿Qué respuesta es más acertada?", "No: da dos, la seguridad y la reducción del tránsito", ["Sí: da solo una razón, la seguridad, y el resto es un ejemplo", "No: da cinco razones, una por cada oración del párrafo"], "First y Second dan dos razones."),
        mr(OP3, "Otro compañero dice que C contradice su postura al usar Although choice is important. ¿Qué respuesta es mejor?", "No: admite un punto contrario y mantiene su postura", ["Sí: cambia de idea a la mitad del párrafo y se contradice", "No: no usa razones para apoyar su postura"], "Although admite un contraargumento."),
    ],
    [
        mr(OP2, "Reescribe B con afirmación, una razón y un ejemplo. ¿Cuál es la mejor?", "I believe bike lanes are useful. They make riding safer. For example, I ride to school every day", ["I think bike lanes are fine. They are nice and I like them. I ride every day", "Bike lanes are useful. Riding is safer. Many people agree. In conclusion, ride"], "Tiene afirmación, razón y ejemplo; las otras no dan razón ni ejemplo claros."),
        arith("Un párrafo debe tener 80 palabras. La afirmación tiene 15, las dos razones tienen 22 cada una y el ejemplo 12. ¿Cuántas palabras faltan para la conclusión?", "80-15-22-22-12", "Se restan las partes escritas del total.", " palabras"),
    ],
    [mc("Debes opinar sobre «El transporte público debería ser más barato para estudiantes». ¿Qué afirmación es adecuada?", "I strongly feel that public transport should be cheaper for students", ["Public transport is a service that students use every day to get to school", "I am going to write about public transport and prices for students"], "Dice la postura con una oración completa; las otras dan un hecho o anuncian el tema.")],
    [
        ("En Inglés de 2.º medio (OA 15, clase 1): ¿cuáles son las cuatro partes de un párrafo de opinión?", "Afirmación, razones, ejemplo y conclusión", "Cada una cumple una función."),
        ("En Inglés de 2.º medio (OA 15, clase 1): ¿qué frase introduce un ejemplo?", "For example", "Presenta un caso concreto."),
        ("En Inglés de 2.º medio (OA 15, clase 1): ¿qué marca although en una opinión?", "Un contraste o contraargumento", "Admite otro punto de vista."),
    ],
    task("Elige una afirmación: A) «Students should have a short break between classes». B) «Public parks should be open until late». C) «Every school should have a music room». Escribe en inglés un párrafo de opinión de 45 a 70 palabras con afirmación, dos razones, un ejemplo, un conector del año y una conclusión. Sigue este ejemplo.", "I believe that every school should have a music room. First, music helps students express feelings. Second, it improves teamwork. For example, a school band learns to listen to each other. Although rooms cost money, the benefits are great. In conclusion, a music room is a good investment.", ["afirmación clara", "dos razones y un ejemplo", "un conector del año y una conclusión"], ["párrafo en la hoja"], ["opinar sin razones", "olvidar la conclusión"], "Pide que cambie una razón por otra y vea si la afirmación se mantiene."),
    "Escribe tres afirmaciones de opinión sobre tu colegio.",
    "Escribe en español dos razones para una opinión que tengas sobre tu barrio.",
)

# ------------------------------------------------------------------ clase 2: narrar con diálogo y comillas
NR1 = "Relato A: «When I opened the door, my cousin was standing there. “Surprise!” she shouted. “I am staying for the weekend.” I was speechless, but I hugged her.» (cousin = prima, shouted = gritó, staying = quedándome, speechless = sin palabras, hugged = abracé)"
NR2 = "Relato B (sin comillas): «Where are you going? asked Mom. To the library, I answered. Take your umbrella, she said.» (umbrella = paraguas, answered = respondí)"
NR3 = "Relato C: «Last winter, we planned a surprise for Grandma. First, we bought flowers. Then we cooked her favorite soup. When she arrived, she cried and said, “This is the best day of my year.”» (planned = planeamos, soup = sopa, cried = lloró, best = mejor)"
NR4 = "Relato D: «Leo was nervous because he had never given a speech before. He took a deep breath. “Good morning,” he said. His voice was shaky at first, but he finished with a smile.» (nervous = nervioso, speech = discurso, deep breath = respiración profunda, shaky = temblorosa)"

lesson(
    OA, 2, MAT_R,
    "Aprenderé a narrar una historia con inicio, desarrollo y final, usando el pasado, palabras de secuencia y diálogo con comillas. Sirve para escribir relatos claros que den vida a los personajes.",
    ["Sé usar el pasado simple.", "Conozco first, then y finally."],
    [
        "Un relato (narrative) cuenta hechos en orden. Tiene inicio, con personajes y lugar; desarrollo, con los hechos y el problema; y final, con la solución. Usa el pasado simple (opened, shouted, cried) y palabras de secuencia: when, first, then, after that, finally. Usa had + participio solo cuando una acción pasada ocurrió antes de otra: Leo was nervous because he had never given a speech before.",
        "El diálogo (dialogue) muestra lo que dicen los personajes. En inglés americano se escribe entre comillas dobles: “Surprise!” she shouted. Las comillas encierran las palabras exactas. La coma o el punto va dentro de las comillas: “Good morning,” he said. Cuando cambia el que habla, cambia la línea. Si la frase dicha es una pregunta, el signo va dentro: “Where are you going?” asked Mom.",
        "Para dar vida al relato, agrega detalles de sentidos y sentimientos: his voice was shaky, she cried. Evita repetir said todo el tiempo: usa asked, answered, shouted, whispered. Revisa que cada verbo esté en pasado y que las comillas abran y cierren.",
    ],
    [("narrative", "relato"), ("dialogue", "diálogo"), ("quotation marks", "comillas “ ”"), ("said / asked / shouted / whispered", "verbos de habla"), ("when / then / after that", "cuando / luego / después de eso"), ("shaky", "temblorosa")],
    [
        ("Poner comillas", NR2 + " Escríbelo con comillas.", ["Mamá pregunta: Where are you going.", "Yo respondo: To the library.", "Mamá dice: Take your umbrella."], "“Where are you going?” asked Mom. “To the library,” I answered. “Take your umbrella,” she said"),
        ("Partes del relato", NR3 + " ¿Cuál es el inicio, el desarrollo y el final?", ["Inicio: planearon una sorpresa para la abuela.", "Desarrollo: compraron flores y cocinaron.", "Final: ella llegó, lloró y dijo que era el mejor día."], "Inicio: planean una sorpresa. Desarrollo: compran flores y cocinan. Final: la abuela llora y dice que es el mejor día"),
    ],
    [
        ("Poner el punto fuera de las comillas en inglés americano.", "En inglés americano el punto y la coma van dentro.", "Escribe “Good morning,” he said."),
        ("Mezclar presente y pasado en el relato.", "El relato pierde coherencia.", "Mantén los verbos en pasado."),
    ],
    [
        mr(NR1, "¿Qué verbo de habla se usa en Relato A?", "shouted", ["whispered", "answered"], "Dice she shouted."),
        mr(NR4, "¿Qué palabras dichas por Leo van entre comillas?", "Good morning", ["He took a deep breath", "His voice was shaky"], "Son sus palabras exactas."),
        mc("¿Qué signos se usan en inglés americano para un diálogo?", "Comillas dobles", ["Guiones largos al inicio de la línea", "Paréntesis alrededor de las palabras"], "El inglés americano usa “ ”."),
    ],
    [
        mr(NR3, "¿Qué palabra marca el orden de los hechos al comienzo?", "First", ["Although", "Never"], "First marca la primera acción."),
        mr(NR4, "¿Por qué estaba nervioso Leo?", "Porque nunca había dado un discurso", ["Porque su voz temblaba desde antes de hablar", "Porque no sabía qué decir en su saludo"], "Dice he had never given a speech before."),
        mr(NR1, "¿Cómo se sintió el narrador al ver a su prima?", "Sin palabras, pero contento", ["Enojado y molesto por la visita", "Aburrido y sin ganas de hablar"], "Dice I was speechless, but I hugged her."),
    ],
    [
        mc("Elige la puntuación correcta:", "“Good morning,” he said.", ["“Good morning”, he said.", "Good morning, he said."], "La coma va dentro de las comillas."),
        mc("Elige la puntuación correcta:", "“Where are you going?” asked Mom.", ["“Where are you going”? asked Mom.", "“Where are you going?”, asked Mom."], "El signo de interrogación va dentro."),
        mc("Completa con el pasado: Yesterday I ____ my cousin at the station.", "met", ["meet", "have meet"], "Meet pasa a met."),
    ],
    [
        mr(NR2, "Un compañero dice que el relato B está bien así. ¿Qué respuesta es más acertada?", "No: faltan las comillas", ["Sí: se entiende bien y eso es suficiente", "No: le sobran los verbos de habla"], "Las palabras exactas van entre comillas."),
        mr(NR4, "Otro compañero escribe: “Good morning, he said”. ¿Qué falla?", "La coma debe ir dentro de las comillas, y he said fuera", ["He said también debe ir entre comillas, con la coma fuera", "Debe usar comillas simples y poner la coma después"], "Debe ser “Good morning,” he said."),
    ],
    [
        mr(NR1, "Agrega un diálogo a Relato A después de la sorpresa. ¿Cuál es el mejor?", "“I am so happy to see you!” I whispered", ["I am so happy to see you I whispered", "“I am so happy to see you!” I whispered, ”"], "Tiene comillas y verbo de habla."),
        mr(NR3, "Cambia el final de C. ¿Cuál está bien escrito?", "She hugged us and said, “Thank you for this surprise.”", ["She hugs us and said, “Thank you for this surprise.”", "She hugged us and said, “Thank you for this surprise”."], "Mantiene el pasado y el punto dentro de las comillas."),
        arith("Un relato tiene 5 diálogos y cada diálogo usa 2 comillas (abrir y cerrar). ¿Cuántas comillas hay en total?", "5*2", "Se multiplican los diálogos por las comillas de cada uno.", " comillas"),
    ],
    [mr(NR4, "Escribe un final para D. ¿Cuál está bien escrito en pasado?", "When he finished, everyone clapped, and he felt proud", ["When he finishes, everyone claps, and he feels proud of it", "When he finished, everyone clap, and he was feel proud"], "Mantiene el pasado y cierra la historia.")],
    [
        ("En Inglés de 2.º medio (OA 15, clase 2): ¿qué puntuación usa el diálogo en inglés americano?", "Comillas dobles", "Se escriben “ ”."),
        ("En Inglés de 2.º medio (OA 15, clase 2): ¿dónde va la coma en “Good morning,” he said?", "Dentro de las comillas", "Así se escribe en inglés americano."),
        ("En Inglés de 2.º medio (OA 15, clase 2): ¿qué tiempo se usa para narrar?", "El pasado", "Cuenta hechos que ya ocurrieron."),
    ],
    task("Escribe un relato breve de 45 a 80 palabras en inglés sobre «A day I had a surprise». Incluye inicio, desarrollo y final, palabras de secuencia, al menos dos oraciones de diálogo con comillas y verbos de habla distintos. Sigue este ejemplo.", "When I arrived home, my brother was waiting. “Close your eyes,” he said. Then he gave me a small box. “What is it?” I asked. Inside was a ticket for my favorite band. “Thank you!” I shouted. It was the best surprise.", ["inicio, desarrollo y final", "dos diálogos con comillas", "verbos de habla distintos"], ["relato en la hoja"], ["poner el punto fuera de las comillas", "mezclar presente y pasado"], "Pide que cambie un verbo de habla por otro y diga cómo cambia el tono."),
    "Reescribe un diálogo de una película en inglés con comillas.",
    "Escribe un diálogo de cuatro líneas en español y luego ponle comillas.",
)

# ------------------------------------------------------------------ clase 3: analizar causas, efectos y ventajas
AN1 = "Texto A (análisis): «Many students arrive late because the bus is slow. As a result, they lose the first lesson. Another cause is heavy traffic in the morning. One possible solution is to start the school day later.» (arrive = llegan, slow = lento, lose = pierden, lesson = clase, traffic = tránsito)"
AN2 = "Texto B (ventajas y desventajas de las clases en línea): «Online classes have advantages. You can learn from home, and you save travel time. However, they also have disadvantages. Some students find it hard to concentrate, and few can ask questions quickly. Neither the advantages nor the disadvantages are the same for everyone.» (online classes = clases en línea, advantages = ventajas, save = ahorrar, disadvantages = desventajas, concentrate = concentrarse)"
AN3 = "Texto C (comparación): «Reading a book and watching a movie are different. A book lets you imagine the characters; a movie shows them. Both can tell a story well, but a book usually takes longer.» (imagine = imaginar, characters = personajes, takes longer = demora más)"

lesson(
    OA, 3, MAT_R,
    "Aprenderé a escribir un texto de análisis: explicar causas y efectos, comparar y dar ventajas y desventajas, con conectores como because, as a result, however y neither ... nor. Sirve para razonar por escrito sobre un tema.",
    ["Sé opinar con razones.", "Conozco as a result y however."],
    [
        "Analizar (to analyze) es separar un tema en partes y explicar cómo se relacionan. Hay varios tipos de análisis. En causa y efecto, explicas por qué ocurre algo (because, one cause is) y qué resulta (as a result, so). En comparación, muestras semejanzas (both, similarly) y diferencias (but, however, while). En ventajas y desventajas (advantages and disadvantages), das lo bueno y lo malo de algo.",
        "Un buen texto de análisis tiene una frase inicial que presenta el tema, partes que desarrollan cada aspecto con ejemplos, y un cierre con una conclusión o una solución. Los conectores muestran las relaciones: because da la causa, as a result da el efecto, however y although contrastan, neither ... nor niega ambos aspectos, y unless pone una condición.",
        "Para evitar la opinión sin base, apoya cada afirmación con un dato o un ejemplo. Escribe en presente simple para hechos generales (Many students arrive late) y mantén un tono neutral. Antes de entregar, revisa que cada causa tenga su efecto y que cada ventaja tenga una desventaja del mismo tipo.",
    ],
    [("analyze", "analizar"), ("cause / effect", "causa / efecto"), ("advantage / disadvantage", "ventaja / desventaja"), ("compare", "comparar"), ("however / while", "sin embargo / mientras que"), ("solution", "solución")],
    [
        ("Causa y efecto", AN1 + " ¿Cuál es la causa y cuál el efecto?", ["Busco because: el bus es lento.", "Busco as a result: pierden la primera clase.", "La causa y el efecto están unidos."], "Causa: el bus es lento. Efecto: pierden la primera clase"),
        ("Ventajas y desventajas", AN2 + " ¿Cuál es una ventaja y cuál una desventaja?", ["Ventaja: aprender desde casa y ahorrar tiempo de viaje.", "Desventaja: concentrarse y hacer preguntas.", "However marca el paso a las desventajas."], "Ventaja: aprender desde casa; desventaja: dificultad para concentrarse"),
    ],
    [
        ("Dar solo ventajas y olvidar las desventajas.", "El análisis queda incompleto.", "Incluye ambas con un conector de contraste."),
        ("Poner el efecto como si fuera la causa.", "Se cambia la relación causal.", "Pregunta qué ocurre primero y qué resulta."),
    ],
    [
        mr(AN1, "¿Qué conector introduce el efecto?", "As a result", ["Because", "Another"], "As a result marca la consecuencia."),
        mr(AN2, "¿Qué conector introduce las desventajas?", "However", ["As a result", "First"], "However marca el contraste."),
        mr(AN3, "¿Qué diferencia se menciona?", "El libro los hace imaginar; la película los muestra", ["La película es siempre más corta que el libro", "El libro muestra a los personajes en imágenes"], "Dice A book lets you imagine; a movie shows them."),
    ],
    [
        mr(AN1, "¿Qué otra causa se menciona?", "El tránsito pesado de la mañana", ["La lluvia fuerte durante la mañana", "La falta de buses en la ciudad"], "Dice Another cause is heavy traffic in the morning."),
        mr(AN2, "¿Qué ventaja menciona sobre el tiempo?", "Se ahorra tiempo de viaje", ["Se tiene más tiempo de recreo entre clases", "Se pierde tiempo en el viaje de ida"], "Dice you save travel time."),
        mr(AN3, "¿Qué tienen en común el libro y la película?", "Ambos pueden contar bien una historia", ["Ambos muestran los personajes en imágenes", "Ambos demoran lo mismo en terminar"], "Dice Both can tell a story well."),
    ],
    [
        mc("Completa: Many students are late. ____, they lose the first lesson.", "As a result", ["Neither", "Unless"], "Introduce la consecuencia."),
        mc("Completa: Online classes save time; ____, some students find it hard to concentrate.", "however", ["so", "as soon as"], "Introduce un contraste."),
        mc("Completa: Neither the advantages nor the disadvantages ____ the same for everyone.", "are", ["is", "be"], "El verbo concuerda con disadvantages, el sujeto más cercano."),
    ],
    [
        mr(AN1, "Un compañero dice que la solución es quitar la primera clase. ¿Qué solución propone el texto?", "Empezar el día escolar más tarde", ["Quitar la primera clase de cada día", "Cambiar el bus por uno más rápido"], "Dice One possible solution is to start the school day later."),
        mr(AN2, "Otro compañero dice que las clases en línea son malas para todos. ¿Qué respuesta es más acertada?", "No: dice que no afectan igual a todos", ["Sí: el texto solo menciona desventajas", "No: el texto no menciona desventajas"], "Dice Neither the advantages nor the disadvantages are the same for everyone."),
    ],
    [
        mr(AN3, "Escribe una oración de comparación con while. ¿Cuál es correcta?", "A book lets you imagine the characters, while a movie shows them", ["A book lets you imagine the characters while, and a movie shows them", "A book lets you imagine the characters, while a movie"], "Contrasta dos ideas completas con while."),
        arith("En una encuesta, 12 de 30 estudiantes dicen que llegan tarde por el bus. ¿Cuántos no llegan tarde por esa causa?", "30-12", "Se resta el grupo con esa causa del total.", " estudiantes"),
    ],
    [mr(AN1, "Escribe una conclusión para A que retome la solución. ¿Cuál es adecuada?", "In conclusion, a later start could help students arrive on time", ["In conclusion, the bus is slow and there is heavy traffic in the morning", "In conclusion, students will lose the first lesson as a result of it"], "Resume la solución; las otras repiten causas o efectos sin proponer nada.")],
    [
        ("En Inglés de 2.º medio (OA 15, clase 3): ¿qué conector marca el efecto?", "As a result", "Introduce la consecuencia."),
        ("En Inglés de 2.º medio (OA 15, clase 3): ¿qué conector marca un contraste?", "However", "Introduce una idea opuesta."),
        ("En Inglés de 2.º medio (OA 15, clase 3): ¿qué incluye un análisis de ventajas y desventajas?", "Lo bueno y lo malo con ejemplos", "Debe ser equilibrado."),
    ],
    task("Elige uno: A) causa y efecto de «Why students feel stressed before exams», B) ventajas y desventajas de «Studying with friends», o C) comparación entre «A bus and a train». Escribe un texto de 45 a 70 palabras con una frase inicial, dos aspectos con ejemplos, un conector de contraste y una conclusión. Sigue este ejemplo.", "Studying with friends has advantages and disadvantages. One advantage is that you can ask questions quickly. For example, a friend can explain a math problem. However, sometimes friends talk too much. As a result, you can lose time. In conclusion, studying with friends works if the group has rules.", ["frase inicial", "dos aspectos con ejemplos", "un conector de contraste y una conclusión"], ["texto en la hoja"], ["dar solo un lado", "no usar conectores"], "Pide que cambie un conector y explique el cambio."),
    "Haz una tabla de ventajas y desventajas de las redes sociales para estudiantes.",
    "Explica en español por qué algo que te pasó hoy ocurrió (causa y efecto).",
)

# ------------------------------------------------------------------ clase 4: variedad de palabras, oraciones y conectores
VR1 = "Texto repetitivo: «The trip was good. The food was good. The guide was good. The hotel was good.»"
VR2 = "Texto con oraciones cortas: «I woke up. I got dressed. I ate breakfast. I went to school.»"
VR3 = "Texto con un solo conector: «I was tired and I went home and I ate dinner and I watched TV and I went to bed.»"
VR4 = "Texto mejorado: «The trip was wonderful. The food was delicious, the guide was friendly, and the hotel was comfortable. As soon as we arrived, we felt welcome.»"

lesson(
    OA, 4, MAT_R,
    "Aprenderé a escribir con variedad: usar sinónimos para no repetir palabras, combinar oraciones cortas y emplear conectores distintos (neither ... nor, either ... or, though, unless, as soon as, as a result, however). Sirve para que mis textos sean más ricos y fluidos.",
    ["Sé escribir oraciones simples y compuestas.", "Conozco sinónimos como big y large."],
    [
        "La variedad (variety) hace más interesante un texto. En vocabulario, evita repetir good: puedes usar wonderful, delicious, friendly, comfortable o useful, según lo que describes. Elige el sinónimo que mejor encaja y comprueba en un diccionario si dudas. En oraciones, combina varias cortas en una más larga con and, but, because o with: I woke up and got dressed, then I ate breakfast before going to school.",
        "En los conectores, no uses siempre and. Usa as soon as para el momento, as a result para la consecuencia, though o however para contraste, unless para condición, either ... or para opciones y neither ... nor para negar dos opciones. Varía el comienzo de las oraciones: In the morning, After lunch, When we arrived, Although it was late.",
        "Pero la variedad no debe confundir. Cada palabra y conector debe decir con claridad lo que quieres expresar. Revisa tu texto subrayando las palabras repetidas y los conectores iguales, y reemplaza algunos. Lee en voz alta: si suena monótono, necesita variedad.",
    ],
    [("variety", "variedad"), ("synonym", "sinónimo"), ("combine sentences", "unir oraciones"), ("sentence starter", "comienzo de oración"), ("wonderful / delicious", "maravilloso / delicioso"), ("monotonous", "monótono")],
    [
        ("Reemplazar una palabra repetida", VR1 + " Mejora el texto con sinónimos de good.", ["La palabra good se repite cuatro veces.", "Busco adjetivos que digan más: wonderful, delicious, friendly, comfortable.", "Los uso según cada cosa."], "The trip was wonderful. The food was delicious, the guide was friendly and the hotel was comfortable"),
        ("Unir oraciones cortas", VR2 + " Una dos oraciones cortas.", ["Las oraciones son cortas y similares.", "Puedo unir con and y then.", "Escribo: I woke up and got dressed, then I ate breakfast."], "I woke up and got dressed, then I ate breakfast"),
    ],
    [
        ("Usar and como único conector.", "El texto se vuelve monótono.", "Varía con as soon as, though, as a result, etc."),
        ("Cambiar una palabra por un sinónimo que no encaja.", "El sentido cambia o suena extraño.", "Elige el sinónimo según el contexto."),
    ],
    [
        mc("Elige un sinónimo de good para la comida:", "delicious", ["comfortable", "loud"], "Delicious describe una comida buena."),
        mc("Elige un sinónimo de good para un hotel:", "comfortable", ["delicious", "loud"], "Comfortable describe un lugar cómodo."),
        mr(VR3, "¿Qué conector se repite?", "and", ["but", "so"], "Aparece cuatro veces."),
    ],
    [
        mr(VR4, "¿Qué conector marca el momento en el texto mejorado?", "As soon as", ["Although", "Unless"], "Marca cuándo se sintieron bienvenidos."),
        mr(VR2, "¿Cuántas oraciones tiene el texto con oraciones cortas?", "Cuatro", ["Tres", "Seis"], "Hay cuatro puntos."),
        mc("¿Qué conector sirve para decir que algo no ocurre si no se cumple una condición?", "unless", ["as soon as", "though"], "Unless es una condición negativa."),
    ],
    [
        mc("Reescribe con un conector de contraste: «The movie was long. I enjoyed it».", "The movie was long, though I enjoyed it", ["The movie was long, so I enjoyed it", "The movie was long, as soon as I enjoyed it"], "Though marca el contraste."),
        mc("Reescribe con as a result: «It rained all day. We stayed home».", "It rained all day. As a result, we stayed home", ["It rained all day. However, we decided to stay home", "It rained all day, unless we stayed home"], "As a result marca la consecuencia; however marca contraste y unless una condición."),
        mc("Reescribe con neither ... nor: «Ana didn't come. Beto didn't come».", "Neither Ana nor Beto came", ["Either Ana or Beto came", "Ana nor Beto came"], "Niega los dos."),
    ],
    [
        mr(VR3, "Un compañero dice que no hace falta cambiar el texto de los and. ¿Qué respuesta es más acertada?", "Sí hace falta: tantos and lo hacen monótono y difícil de seguir", ["No: está perfecto", "Hay que agregar más and"], "Se necesita variedad."),
        mr(VR1, "Otro compañero propone cambiar cada good por nice. ¿Qué respuesta es mejor?", "Mejor usar adjetivos distintos según cada cosa, para dar más información", ["Perfecto: nice es mejor", "Es mejor quitar el texto"], "Nice repetido sigue siendo repetitivo."),
    ],
    [
        mr(VR3, "Reescribe el texto de los and con variedad. ¿Cuál es mejor?", "I was tired, so I went home. After I ate dinner, I watched TV, and then I went to bed", ["I was tired and I went home. Then I ate dinner and I watched TV and I went to bed", "I was tired, but I went home, because I ate dinner, though I watched TV, and bed"], "Usa so, after y then con sentido; las otras repiten and o usan conectores que no corresponden."),
        arith("Un texto tiene 8 oraciones con and. Si reemplazas 5 por otros conectores, ¿cuántas oraciones con and quedan?", "8-5", "Se restan las reemplazadas de las originales.", " oraciones"),
    ],
    [mc("Une con either ... or: «We can go by bus. We can go by train».", "We can go either by bus or by train", ["We can go either by bus and by train", "We can go neither by bus or by train"], "Either ... or presenta dos opciones; either ... and y neither ... or no existen.")],
    [
        ("En Inglés de 2.º medio (OA 15, clase 4): ¿qué haces para no repetir good?", "Uso sinónimos según el contexto", "Aportan más información."),
        ("En Inglés de 2.º medio (OA 15, clase 4): ¿qué conector indica una condición negativa?", "Unless", "Significa a menos que."),
        ("En Inglés de 2.º medio (OA 15, clase 4): ¿qué evitas usar en exceso para unir ideas?", "And", "Vuelve monótono el texto."),
    ],
    task("Mejora este texto con variedad: «My weekend was nice. We went to the park and we played and we ate and we talked. The food was nice. The park was nice. We went home.» Reemplaza palabras repetidas, une oraciones y usa tres conectores distintos (por ejemplo as soon as, though, as a result, neither ... nor). Escribe la versión mejorada. Sigue este ejemplo.", "My weekend was wonderful. We went to the park, played soccer and ate sandwiches. The food was delicious and the park was peaceful. As soon as it got dark, we went home. Neither my brother nor I wanted to leave.", ["reemplaza palabras repetidas", "usa tres conectores distintos", "une oraciones cortas"], ["texto mejorado en la hoja"], ["cambiar el sentido", "usar un conector que no corresponde"], "Pide que lea el texto en voz alta y diga si suena menos monótono."),
    "Reemplaza good, nice y big en cinco oraciones tuyas.",
    "Reescribe en español un párrafo tuyo cambiando palabras repetidas y uniendo oraciones.",
)

# ------------------------------------------------------------------ clase 5: ortografía y puntuación
SP1 = "Texto con errores: «Their going to recieve there prizes tomorow. Its a beautifull day, and your friends are definately comming.» (prizes = premios, beautiful = hermoso, definitely = sin duda)"
SP2 = "Texto corregido: «They're going to receive their prizes tomorrow. It's a beautiful day, and your friends are definitely coming.»"
SP3 = "Texto con puntuación incorrecta: «“I am tired”, said Ana. “Let’s go home.”, she added.»"
SP4 = "Texto con ortografía inconsistente: «I like color. My favourite colour is blue. These colors are bright.»"

lesson(
    OA, 5, MAT_R,
    "Aprenderé a escribir con ortografía correcta y consistente las palabras de uso frecuente y a puntuar con comillas, comas, apóstrofos y puntos. Sirve para que mis textos se lean sin confusión.",
    ["Sé revisar y editar un texto.", "Conozco palabras frecuentes como friend y because."],
    [
        "Hay palabras de uso frecuente que muchas personas escriben mal: receive (ei después de c), friend (ie), because, beautiful, tomorrow, definitely, separate, different, necessary y which. También hay homófonos, que suenan igual pero se escriben distinto: their (de ellos), there (allí) y they're (they are); your (tu) y you're (you are); its (de él) e it's (it is); to, too (también) y two (dos). Aprende cada pareja con una oración modelo.",
        "La consistencia es escribir siempre del mismo modo. En inglés americano se escribe color, favorite y neighbor; en inglés británico, colour, favourite y neighbour. No mezcles las dos formas en el mismo texto. Elige una variante y úsala hasta el final.",
        "En la puntuación, el apóstrofo marca contracciones (it's, don't) y posesión (Ana's book). Las comillas dobles encierran las palabras exactas de alguien, y la coma o el punto va dentro de las comillas en inglés americano: “I am tired,” said Ana. “Let’s go home,” she added. Usa mayúscula al comenzar una oración y en los nombres propios.",
    ],
    [("receive / friend / beautiful", "palabras con ortografía frecuente"), ("their / there / they're", "de ellos / allí / ellos son"), ("your / you're", "tu / tú eres"), ("its / it's", "su / es"), ("consistency", "consistencia: escribir siempre igual"), ("apostrophe", "apóstrofo")],
    [
        ("Corregir homófonos", SP1 + " Corrige los homófonos.", ["Their going → They're going.", "there prizes → their prizes.", "Its a → It's a; your friends se mantiene."], "They're going to receive their prizes. It's a beautiful day"),
        ("Corregir la puntuación del diálogo", SP3 + " Corrige las comillas y comas.", ["La coma va dentro de las comillas.", "El punto también va dentro.", "Escribo: “I am tired,” said Ana. “Let’s go home,” she added."], "“I am tired,” said Ana. “Let’s go home,” she added"),
    ],
    [
        ("Escribir recieve.", "La regla es i antes de e, excepto después de c.", "Escribe receive."),
        ("Mezclar color y colour en un mismo texto.", "Se pierde consistencia.", "Elige una variante y mantenla."),
    ],
    [
        mc("¿Cuál es la ortografía correcta?", "receive", ["recieve", "receeve"], "Después de c va ei."),
        mc("¿Cuál es la ortografía correcta?", "beautiful", ["beautifull", "butiful"], "Termina en -ful."),
        mc("¿Cuál es la ortografía correcta?", "definitely", ["definately", "definitly"], "Se escribe con -itely al final."),
    ],
    [
        mc("Completa: ____ going to arrive soon. (ellos son)", "They're", ["Their", "There"], "They're es they are."),
        mc("Completa: This is ____ house. (de ellos)", "their", ["there", "they're"], "Their indica posesión."),
        mc("Completa: ____ a long day. (es)", "It's", ["Its", "Its'"], "It's es it is."),
    ],
    [
        mc("Elige la variante americana coherente:", "My favorite color is blue", ["My favourite color is blue", "My favorite colour is blue"], "Todas las palabras deben ser de la misma variante."),
        mc("Elige la oración correcta:", "You're my best friend", ["Your my best friend", "Youre my best friend"], "You're es you are."),
        mc("Elige la oración correcta (quieres decir «yo también quiero ir»):", "I want to go too", ["I want too go to", "I want to go to"], "Too significa también."),
    ],
    [
        mr(SP4, "Un compañero dice que el texto está bien porque se entiende. ¿Qué respuesta es más acertada?", "Falta consistencia: mezcla color y colour", ["Está perfecto", "Faltan mayúsculas"], "Hay que elegir una variante."),
        mr(SP2, "Otro compañero dice que your friends debería ser you're friends. ¿Qué respuesta es mejor?", "No: your indica posesión (tus amigos)", ["Sí: you're es siempre mejor", "Sí: your no existe"], "Your friends es tus amigos."),
    ],
    [
        mc("Elige la puntuación correcta para: Ana said I am tired.", "Ana said, “I am tired.”", ["Ana said “I am tired”.", "Ana said I am “tired.”"], "La coma va antes de las comillas y el punto dentro."),
        arith("Un texto tiene 12 errores de ortografía. Corriges 9 con el diccionario y 2 con el revisor. ¿Cuántos quedan por corregir?", "12-9-2", "Se restan los errores corregidos.", " error"),
    ],
    [mc("Corrige el texto con ortografía inconsistente («I like color. My favourite colour is blue. These colors are bright.») con la variante americana. ¿Cuál es la versión correcta?", "I like color. My favorite color is blue. These colors are bright", ["I like color. My favorite colour is blue. These colors are bright", "I like colour. My favourite colour is blue. These colours are bright"], "Todas las palabras en la variante americana; la tercera es consistente, pero británica.")],
    [
        ("En Inglés de 2.º medio (OA 15, clase 5): ¿qué significa they're?", "They are", "Es una contracción."),
        ("En Inglés de 2.º medio (OA 15, clase 5): ¿dónde va la coma en un diálogo en inglés americano?", "Dentro de las comillas", "Así se escribe: “Hello,” she said."),
        ("En Inglés de 2.º medio (OA 15, clase 5): ¿qué es la consistencia ortográfica?", "Escribir siempre de la misma forma", "No se mezclan variantes."),
    ],
    task("Corrige este texto con ortografía y puntuación (variante americana): «Their was a beautifull colour in the sky. “It's definately going to rain” said Leo. “Lets go home”, said Ana. Your going to recieve a surprise tomorow.» Escribe el texto corregido y una lista con los errores que corregiste y su regla.", "There was a beautiful color in the sky. “It's definitely going to rain,” said Leo. “Let's go home,” said Ana. You're going to receive a surprise tomorrow. Errores: there/their, ortografía, color/colour, coma dentro, you're.", ["corrige todos los errores", "usa comillas con la coma dentro", "explica la regla de cada corrección"], ["texto corregido y lista de reglas"], ["dejar their por there", "mezclar color y colour"], "Pide que lea en voz alta y confirme que suena igual con las formas correctas."),
    "Escribe diez palabras frecuentes con su ortografía correcta.",
    "Revisa un mensaje que escribiste y anota tres errores de ortografía.",
)

# ------------------------------------------------------------------ clase 6: repasar, reparar y transferir
RP1 = "Párrafo mixto con errores: «I think students should have more breaks. Because they gets tired. For example my friend loses focus in class. In conclusion breaks is important» (breaks = recreos, loses focus = pierde la concentración)"
RP2 = "Párrafo de opinión corregido: «I believe that students should have more breaks. First, they get tired after long lessons. For example, my friend finds it hard to concentrate in the last class. In conclusion, breaks are important.»"
RP3 = "Relato breve con errores: «Yesterday i go to the park with my dog. “Come here!” I shout. He did not came. Then I seen him near the trees.»"
RP4 = "Texto de análisis con errores: «Many students feel stressed because the exams. As a result, they not sleep well. Two solution are study plans and breaks.» (stressed = estresados, study plans = planes de estudio)"

lesson(
    OA, 6, MAT_R,
    "Aprenderé a repasar, reparar y transferir lo aprendido sobre escribir para opinar, narrar y analizar: reconocer los errores frecuentes, corregirlos y aplicar las estrategias a tres propósitos distintos. Sirve para consolidar mis habilidades de escritura.",
    ["Sé escribir opiniones, relatos y análisis.", "Sé editar ortografía y puntuación."],
    [
        "Repasar es volver a las estrategias clave. Para opinar: afirmación, dos razones, ejemplo y conclusión. Para narrar: inicio, desarrollo y final, pasado, secuencia y diálogo con comillas. Para analizar: causa y efecto, comparación o ventajas y desventajas, con conectores. En los tres casos: variedad de palabras, ortografía correcta y consistente, y puntuación adecuada.",
        "Reparar es corregir los errores frecuentes. Los más comunes son: concordancia (they gets → they get; breaks is → breaks are), tiempo verbal (I go yesterday → I went), formas irregulares (I seen → I saw; did not came → did not come), falta de verbo (they not sleep → they do not sleep), plural (solution → solutions), mayúsculas (i → I) y puntuación (comas, comillas, punto final). Una oración que empieza con Because sin una segunda idea es un fragmento: debe unirse a la oración anterior.",
        "Transferir es usar lo aprendido en una nueva situación. Si sabes escribir una opinión sobre los recreos, puedes escribir una opinión sobre otro tema con la misma estructura. Si sabes narrar con diálogo, puedes narrar otro hecho. Antes de entregar, revisa con una lista: contenido, organización, vocabulario, conectores, ortografía y puntuación.",
    ],
    [("repair", "reparar errores"), ("transfer", "usar lo aprendido en otra situación"), ("fragment", "fragmento: oración incompleta"), ("agreement", "concordancia"), ("irregular verb", "verbo irregular"), ("checklist", "lista de revisión")],
    [
        ("Reparar una opinión", RP1 + " ¿Qué errores tiene?", ["They gets debe ser they get.", "Because suelto es un fragmento.", "Breaks is debe ser breaks are, y faltan comas."], "They gets → they get; breaks is → breaks are; el fragmento Because; faltan comas"),
        ("Reparar un relato", RP3 + " ¿Qué errores tiene?", ["Yesterday i go: i debe ser I y go debe ser went.", "I shout: debe ser shouted.", "did not came → did not come; I seen → I saw."], "i → I; go → went; shout → shouted; came → come; seen → saw"),
    ],
    [
        ("Corregir solo la ortografía y dejar los errores de concordancia.", "Los errores de forma verbal también cambian el sentido.", "Revisa concordancia, tiempo y formas irregulares."),
        ("Usar la estrategia de opinión para un relato.", "Cada propósito tiene su estructura.", "Elige la estructura según el propósito."),
    ],
    [
        mc("¿Cuál es la forma correcta?", "they get tired", ["they gets tired", "they getting tired"], "Con they, el verbo no lleva -s."),
        mc("¿Cuál es la forma correcta?", "breaks are important", ["breaks is important", "break are importants"], "Breaks es plural."),
        mc("¿Cuál es la forma correcta del pasado de see?", "saw", ["seen", "seed"], "I saw him; seen necesita have."),
    ],
    [
        mr(RP4, "¿Cuál es la forma correcta de they not sleep well?", "they do not sleep well", ["they not sleeps well", "they are not sleep well"], "Se necesita do en la negación."),
        mr(RP4, "¿Cuál es la forma correcta de Two solution are?", "Two solutions are", ["Two solution is", "Two solutions is"], "El número 2 pide plural."),
        mr(RP1, "¿Qué hay que hacer con la oración Because they gets tired?", "Unirla a la anterior y corregir el verbo", ["Dejarla igual porque tiene sujeto y verbo", "Cambiar Because por And y dejarla sola"], "Es un fragmento."),
    ],
    [
        mr(RP2, "¿Qué parte del párrafo corregido es la afirmación?", "I believe that students should have more breaks", ["First, they get tired after long lessons", "For example, my friend finds it hard to concentrate"], "Es la primera oración."),
        mc("Estás escribiendo un texto de análisis. ¿Qué conector sirve para el efecto?", "As a result", ["Neither", "Unless"], "Marca la consecuencia."),
        mc("Estás escribiendo un relato. ¿Qué verbo es el correcto en pasado de shout?", "shouted", ["shout", "shouts"], "En pasado se agrega -ed."),
    ],
    [
        mr(RP1 + " " + RP2, "Un compañero dice que el párrafo con errores ya cumple el género de opinión. ¿Qué responde alguien que lo compara con el corregido?", "El corregido tiene razones, ejemplo y conclusión", ["Sí: el primero es más corto, así que es más claro", "Los dos son iguales porque dicen lo mismo"], "El párrafo corregido tiene la estructura completa."),
        mr(RP3, "Otro compañero dice que el diálogo está bien así. ¿Qué responde alguien que lee con cuidado?", "Las comillas están bien, pero shout debe ser shouted", ["Falta el punto final de cada diálogo dentro de las comillas", "Todo está bien porque el diálogo se entiende"], "El diálogo debe mantener el pasado."),
    ],
    [
        mr(RP4, "Reescribe el texto de análisis con errores. ¿Cuál es la mejor?", "Many students feel stressed because of the exams. As a result, they do not sleep well. Two solutions are study plans and breaks", ["Many students feel stressed because the exams. As a result, they do not sleep well. Two solutions are study plans and breaks", "Many students feel stressed because of the exams. As a result, they not sleep well. Two solutions are study plans and breaks"], "Corrige la causa (because of), el verbo (do not sleep) y los plurales; las otras dejan un error."),
        arith("Tienes 3 textos (opinión, relato, análisis) y revisas 4 errores frecuentes en cada uno. ¿Cuántos errores revisas en total?", "3*4", "Se multiplica los textos por los errores.", " errores"),
    ],
    [mc("Debes transferir la estructura de opinión a un tema nuevo: «Schools should have a garden». ¿Qué parte va primero?", "La afirmación", ["La conclusión", "El ejemplo"], "Se parte con la postura.")],
    [
        ("En Inglés de 2.º medio (OA 15, clase 6): ¿qué significa transferir una estrategia?", "Usarla en una nueva situación", "Es aplicar lo aprendido."),
        ("En Inglés de 2.º medio (OA 15, clase 6): ¿qué es un fragmento?", "Una oración incompleta", "Por ejemplo, Because they get tired."),
        ("En Inglés de 2.º medio (OA 15, clase 6): ¿qué revisas en una lista de revisión final?", "Contenido, organización, vocabulario, conectores, ortografía y puntuación", "Cubre todo el texto."),
    ],
    task("Elige uno de los tres propósitos (opinión, relato o análisis) con un tema nuevo: A) «Should schools have a garden?», B) «A day I got lost», C) «Why people use phones so much». Escribe un texto de 45 a 80 palabras con la estructura correcta, tres conectores, al menos un diálogo con comillas (si es relato) o un ejemplo (si es opinión o análisis) y revisa con la lista final. Sigue este ejemplo.", "I believe that schools should have a garden. First, students need a place to relax. Second, a garden helps them learn about plants. For example, a class can grow tomatoes. Although it costs money, it is useful. In conclusion, schools should have a garden.", ["usa la estructura del propósito elegido", "tres conectores y vocabulario variado", "ortografía y puntuación correctas"], ["texto en la hoja", "lista de revisión final"], ["mezclar estructuras", "no revisar la lista final"], "Pide que cambie el propósito y explique qué cambia en la estructura."),
    "Haz una lista de errores frecuentes que has cometido y su forma correcta.",
    "Elige un tema que te importe y decide si sirve para opinar, narrar o analizar.",
)

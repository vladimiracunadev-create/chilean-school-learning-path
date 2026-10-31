"""Cuaderno del estudiante, 7.º básico Inglés (oficial): IN07 OA 15, escribir para informar, opinar y narrar.

Los textos en inglés son originales y breves, con glosario en español dentro del enunciado. Los conectores, la ortografía
de palabras frecuentes y la puntuación se enseñan en la clase antes de usarse en un ejercicio.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA = "IN07 OA 15"


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


# ============================================================ clase 1: declarar un propósito claro
lesson(
    OA, 1,
    "Las situaciones y los textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a decidir si escribo para informar, para dar mi opinión o para narrar, y a decirlo con una oración clara. Sirve para que el lector sepa desde el inicio qué va a encontrar.",
    ["Sé escribir oraciones con sujeto y verbo.", "Conozco palabras como think, because y yesterday."],
    [
        "Escribir para informar (to inform) es dar datos que se pueden comprobar: qué, cuándo, dónde. Ejemplo: «The robotics club meets on Wednesdays at 3:00.» Escribir para opinar (to give an opinion) es decir lo que piensas y por qué: «I think the club is useful because we learn to build things.» Escribir para narrar (to narrate) es contar lo que pasó, en orden: «Last week, our robot moved for the first time.»",
        "Cada propósito tiene frases que lo anuncian. Para informar: «This note is about…», «I want to tell you that…». Para opinar: «I think…», «In my opinion…», «I like… because…». Para narrar: «Yesterday…», «Last Saturday…», «One day…» y verbos en pasado: went, saw, found. Empezar con una de estas frases deja claro el propósito.",
        "Antes de escribir, completa en una línea: «I write to ___ because ___.» Si no puedes completarla, el propósito aún no está claro. Mientras escribes, vuelve a esa línea: si una oración no ayuda a informar, opinar o narrar según tu propósito, probablemente sobra.",
    ],
    [("purpose", "propósito"), ("to inform", "informar"), ("opinion", "opinión"), ("to narrate", "narrar"), ("fact", "dato comprobable"), ("I think…", "yo pienso…"), ("last week", "la semana pasada")],
    [
        ("Identificar el propósito de un texto", "Texto: «I think the school garden is great because we grow vegetables and learn about plants.» (garden = huerto; vegetables = verduras) ¿Informa, opina o narra?",
         ["Aparece I think.", "Da una razón con because.", "Eso es dar una opinión."], "Opina."),
        ("Elegir la frase de inicio", "Quieres contar lo que ocurrió en tu paseo del sábado. ¿Qué frase eliges? Opciones: «Last Saturday, we went to the lake.» / «This note is about the lake.»",
         ["Es un relato de algo pasado.", "Necesitas una expresión de tiempo pasado y un verbo en pasado.", "La primera cumple ambas."], "Last Saturday, we went to the lake."),
    ],
    [
        ("Mezclar propósitos sin avisar al lector.", "No se decide antes de escribir.", "Escribe «I write to…» y úsalo como guía."),
        ("Dar una opinión sin ninguna razón.", "Se olvida because.", "Después de I think, agrega because y una razón."),
    ],
    [
        ("¿Qué significa «to inform»?", "Informar, dar datos", "Los datos se pueden comprobar."),
        ("«Last week our robot moved.» ¿Para qué se escribe? a) Para narrar b) Para opinar", "a", "Cuenta lo que pasó, en pasado."),
        ("«I think the club is useful.» ¿Qué propósito tiene? a) Opinar b) Informar", "a", "Expresa lo que alguien piensa."),
    ],
    [
        ("Lee: «The library opens at 8:30 and closes at 6:00.» (opens = abre; closes = cierra) ¿Qué propósito tiene? a) Informar b) Narrar", "a", "Da datos comprobables de un horario."),
        ("Lee: «Yesterday, Mia found a purse in the yard and gave it to the teacher.» (purse = monedero; yard = patio) ¿Qué propósito tiene? a) Narrar b) Opinar", "a", "Cuenta lo que ocurrió con verbos en pasado."),
        ("Quieres decir lo que piensas de una película. ¿Qué frase eliges para empezar? a) In my opinion, the film is funny b) The film opens at 5:00.", "a", "In my opinion anuncia una opinión."),
    ],
    [
        ("Texto: «The school has 24 classrooms and one gym.» (classrooms = salas) ¿Es un hecho o una opinión? Escribe hecho u opinión.", "hecho", "Se puede contar y comprobar."),
        ("Texto: «The best subject is Art.» ¿Es un hecho o una opinión? Escribe hecho u opinión.", "opinión", "Depende de lo que piensa cada persona."),
        ("Texto: «I write to tell you that the camp starts on Monday.» (camp = campamento; starts = empieza) ¿Qué propósito anuncia? a) Informar un dato b) Dar una opinión", "a", "I write to tell you that anuncia un dato que se puede comprobar: cuándo empieza."),
    ],
    [
        ("Un compañero escribe: «I like pizza.» y dice que está informando. ¿Qué le respondes? a) Es una opinión, no un dato b) Es un dato porque habla de comida", "a", "Lo que alguien prefiere es una opinión."),
        ("Julia empieza con «Last Sunday I», pero sigue con «The park is open from 9 to 6.» ¿Qué problema tiene? a) Mezcla narrar con informar sin avisar b) Usa pocas mayúsculas", "a", "Cambia de propósito sin explicar."),
    ],
    [
        ("Tienes que escribir: «I write to ___ because ___.» para una nota sobre el horario del casino escolar. Completa el primer espacio. Opciones: inform, narrate.", "inform", "Un horario da datos."),
        ("Quieres que tus compañeros sepan por qué te gusta el básquetbol. Completa: «I ___ basketball is fun because it is a team sport.» (team sport = deporte de equipo) Opciones: think, went.", "think", "I think introduce una opinión."),
    ],
    [("Tu profesora te pide tres textos breves: uno que cuente un paseo, otro que diga si te gustó, otro que dé el horario de salida. ¿Cuál de estos es el texto de opinión? a) «I loved the trip because we saw dolphins.» (dolphins = delfines) b) «The bus leaves at 8:00.»", "a", "Dice que le encantó y da una razón.")],
    [
        ("¿Qué frase anuncia una opinión?", "I think / In my opinion", "Presentan lo que alguien piensa."),
        ("¿Qué tiempo verbal usa un texto para narrar lo que ocurrió? a) Pasado b) Futuro", "a", "Cuenta sucesos que ya ocurrieron."),
        ("Completa: «I write to ___ because I want you to know the time.» Opciones: inform, complain.", "inform", "Dar la hora es informar."),
    ],
    task("Lee estas tres situaciones: 1) Tu curso ganó un partido ayer. 2) Tu colegio abre la biblioteca de 8:00 a 17:00. 3) Piensas que usar uniforme es útil. En tu hoja escribe, para cada una, qué propósito tiene el texto (inform, give an opinion o narrate) y escribe una primera oración en inglés que lo deje claro.", "1) Narrate: Yesterday our class won the match. 2) Inform: The library opens from 8:00 to 5:00. 3) Opinion: I think the uniform is useful because it is comfortable.", ["identifica el propósito de las tres", "usa una frase que lo anuncia", "usa pasado en el relato y because en la opinión"], ["tres oraciones con su propósito"], ["usar opinión en vez de hecho", "narrar sin tiempo pasado"], "Pregunta qué palabra de la oración muestra el propósito."),
    "Copia las tres frases de ejemplo de la explicación (informar, opinar y narrar) y subraya la palabra que las delata.",
    "Escribe una oración de cada tipo sobre tu colegio: una que informe, una que opine y una que narre.",
)

# ============================================================ clase 2: seleccionar información o razones relevantes
lesson(
    OA, 2,
    "Los textos y listas escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escoger los datos o las razones que realmente apoyan lo que quiero decir. Sirve para que mi nota informativa y mi párrafo de opinión tengan sentido y no se llenen de detalles que sobran.",
    ["Sé declarar un propósito.", "Sé distinguir hecho y opinión."],
    [
        "Cuando informas, escoge los datos que responden a las preguntas del lector. Para una nota sobre una feria del libro, el lector quiere saber qué, cuándo, dónde y a qué hora. Un dato es relevante (relevant) si responde a una de esas preguntas. Un dato irrelevante (irrelevant) no ayuda, como «My cousin likes comics» en un aviso de horario.",
        "Cuando opinas, elige razones (reasons) que apoyen tu opinión. «I like the library because it is quiet and I can read» da dos razones. «I like it because I like it» no da ninguna. Una buena razón responde por qué: es útil, es seguro, es divertido, enseña algo. Usa because y, para varias razones, also (además).",
        "Revisa cada oración con esta pregunta: ¿esto ayuda a cumplir mi propósito? Si la respuesta es no, quítala. Si falta un dato (por ejemplo, la hora), agrégalo. Un buen texto es corto pero completo: tiene lo necesario y nada más.",
    ],
    [("relevant", "relevante: sirve para el propósito"), ("irrelevant", "irrelevante: no sirve"), ("reason", "razón"), ("because", "porque"), ("also", "además"), ("detail", "detalle"), ("fact", "dato")],
    [
        ("Escoger los datos relevantes", "Aviso: «Book Fair. Saturday, 10:00, school hall. My cousin likes comics. Free entrance.» (hall = salón; entrance = entrada) ¿Qué dato no es relevante?",
         ["El aviso debe decir qué, cuándo y dónde.", "Free entrance también ayuda.", "My cousin likes comics no responde a ninguna pregunta del lector."], "My cousin likes comics."),
        ("Elegir razones para una opinión", "Opinión: «I like the school garden.» Razones posibles: a) because we plant tomatoes and learn about plants b) because I like it. ¿Cuál es una buena razón?",
         ["Una razón debe explicar por qué.", "La primera da información concreta.", "La segunda repite la opinión."], "La opción a)."),
    ],
    [
        ("Poner todos los datos que se me ocurren.", "Se cree que más información siempre es mejor.", "Incluye solo lo que apoya el propósito."),
        ("Dar como razón la misma opinión.", "Se repite lo que se piensa.", "Explica por qué con un hecho o un beneficio."),
    ],
    [
        ("Un dato relevante es: a) el que responde a lo que el lector necesita b) el que me gusta más", "a", "Sirve al propósito del texto."),
        ("En Inglés (oficial): ¿Qué palabra introduce una razón?", "because", "Because significa porque."),
        ("«I like football because it is fun.» ¿Dónde está la razón? a) it is fun b) I like", "a", "Después de because aparece la razón."),
    ],
    [
        ("Aviso: «Movie Club. Thursday, 4:00, Room 7. The snacks are in the bag.» (snacks = colaciones) El lector quiere saber cuándo es. ¿Qué dato elige? a) Thursday, 4:00 b) Room 7", "a", "Responde a cuándo."),
        ("Opinión: «I like swimming because it is good for my health.» (health = salud) ¿Cuántas razones hay? a) 1 b) 2", "a", "Hay una sola razón."),
        ("Aviso de una excursión: «Bring water and a hat. Bus leaves at 8:00. My dog is brown.» (hat = sombrero; leaves = sale) ¿Cuántas de las tres oraciones son relevantes?", "2", "La oración de agua y sombrero y la de la salida del bus son relevantes; la del perro no."),
    ],
    [
        ("Texto: «The park has a playground and a lake. My shoes are new. It opens at 9.» (playground = juegos infantiles) ¿Qué oración sobra? Opciones: My shoes are new, It opens at 9.", "My shoes are new", "No informa sobre el parque."),
        ("Opinión: «Homework is useful.» ¿Cuál razón la apoya? a) because we practise what we learn b) because I have homework", "a", "Explica un beneficio concreto."),
        ("Tu nota informa sobre un concurso de dibujo. ¿Qué dato es imprescindible? a) la fecha b) mi color favorito", "a", "El lector necesita saber cuándo."),
    ],
    [
        ("Un compañero dice: «I like cats because they are cats.» ¿Es una buena razón? Responde sí o no.", "No", "Repite la idea sin explicarla."),
        ("Ana escribe una nota sobre una feria y agrega que ayer comió pizza. ¿Qué debe hacer al revisar? a) Quitar esa oración b) Agregar más comida", "a", "No ayuda al propósito de informar sobre la feria."),
    ],
    [
        ("Opinión: «Reading is good.» Razones disponibles: 1) It helps us learn new words. 2) I have a red bag. 3) Stories are exciting. ¿Cuáles dos apoyan la opinión? Escribe los números.", "1 y 3", "Hablan de beneficios de leer; la mochila no se relaciona."),
        ("Nota: «Soccer practice is on Tuesday. It starts at 5:00. Wear a blue T-shirt. I like movies on Saturday.» ¿Qué oración quitas? Escribe la última oración.", "I like movies on Saturday", "No es sobre la práctica de fútbol."),
    ],
    [("Tu curso organiza una venta de pasteles y tú escribes el aviso. Tienes estos datos: Friday, 12:30, in the yard, cakes cost $500, my brother plays guitar. ¿Cuál no incluyes? a) my brother plays guitar b) cakes cost $500", "a", "No tiene relación con la venta.")],
    [
        ("¿Para qué sirve preguntar «qué, cuándo, dónde» antes de informar?", "Para escoger los datos que necesita el lector", "Ayuda a no dejar nada importante fuera."),
        ("¿Qué es una razón?", "Una explicación de por qué opinas algo", "Se introduce con because."),
        ("Una oración irrelevante: a) se quita b) se repite", "a", "No apoya el propósito."),
    ],
    task("Lee estas notas para un aviso de una carrera escolar: «Race on Friday. It starts at 11:00. Meet in the yard. My shoes are red. Wear sports clothes. Water is free.» (race = carrera; sports clothes = ropa deportiva) En tu hoja: a) tacha el dato irrelevante, b) escribe el aviso en tres oraciones con los datos que quedan, c) escribe una oración de opinión con I think y una razón con because sobre correr.", "a) My shoes are red. b) There is a race on Friday at 11:00. Meet in the yard and wear sports clothes. Water is free. c) I think running is great because it is good for my health.", ["tacha solo el dato irrelevante", "incluye qué, cuándo y dónde", "la opinión tiene razón con because"], ["aviso en la hoja con un dato tachado"], ["tachar un dato importante", "no dar razón"], "Pregunta qué pregunta del lector responde cada oración."),
    "Copia la tabla de vocabulario y escribe un ejemplo de dato relevante y uno irrelevante para un aviso de reunión.",
    "Escribe una opinión sobre tu comida favorita con dos razones usando because y also.",
)

# ============================================================ clase 3: ordenar eventos e ideas
lesson(
    OA, 3,
    "Los textos y las listas de oraciones escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a ordenar las ideas y los sucesos de un texto para que se entienda. Sirve para contar una historia o dar una opinión paso a paso.",
    ["Sé elegir información relevante.", "Conozco palabras como first, then y finally."],
    [
        "Un relato se ordena por tiempo (chronological order): primero lo que pasó antes y después lo que pasó luego. Las palabras que guían son first (primero), then (luego), next (después), after that (después de eso) y finally (finalmente). También puedes usar before (antes de) y after (después de): «Before the test, he felt nervous.»",
        "Una opinión se ordena por razones. Presentas tu opinión, das la primera razón (first), la segunda (second) y terminas con una conclusión (in conclusion o that is why). Puedes poner primero la razón más importante o dejarla para el final, pero siempre usa palabras de orden para guiar al lector.",
        "Un texto informativo se ordena por temas o por pasos. Si explicas cómo hacer algo, usa first, next, then y finally. Si describes un lugar, agrupa los datos: ubicación, horario, qué hay. Al revisar, lee solo las palabras de orden: si cuentan la historia en el orden correcto, tu texto está bien organizado.",
    ],
    [("order", "orden"), ("first / second", "primero / segundo"), ("then / next", "luego / después"), ("after that", "después de eso"), ("finally", "finalmente"), ("before / after", "antes / después"), ("in conclusion", "en conclusión")],
    [
        ("Ordenar un relato", "Oraciones: x) Finally, they ate the cake. y) First, Ema and Luz bought flour. z) Then they mixed everything. (flour = harina; mixed = mezclaron) ¿En qué orden van?",
         ["Busca la palabra First: es el comienzo.", "Then va después, y Finally es el cierre.", "Orden: y, z, x."], "y, z, x"),
        ("Ordenar razones de una opinión", "Texto desordenado: x) In conclusion, a garden is a great school project. y) I think a school garden is useful. z) First, we learn about plants. ¿Cuál es el orden correcto?",
         ["La opinión va primero.", "Luego va la razón con First.", "La conclusión cierra."], "y, z, x"),
    ],
    [
        ("Contar el final antes que el comienzo.", "No se piensa en el orden del tiempo.", "Anota los sucesos en una línea de tiempo antes de escribir."),
        ("Usar finally en medio del texto.", "No se recuerda que finally cierra.", "Usa first, then y finally en ese orden."),
    ],
    [
        ("¿Qué palabra marca el comienzo? a) First b) Finally", "a", "First significa primero."),
        ("¿Qué palabra cierra una secuencia? a) Finally b) Then", "a", "Finally significa finalmente."),
        ("Ordena: Then / First / Finally. Escribe el orden.", "First, Then, Finally", "Es el orden natural de una secuencia."),
    ],
    [
        ("Oraciones: x) Then he opened the box. y) First, Leo found a box in the attic. z) Finally, he saw an old map. (attic = desván; map = mapa) Escribe el orden correcto.", "y, x, z", "First abre, Then continúa y Finally cierra."),
        ("Ana estudió dos horas y después rindió la prueba. Completa: «___ the test, Ana studied for two hours.» Opciones: Before, After.", "Before", "Estudió antes de la prueba."),
        ("Completa con la palabra de orden: «First, we choose a topic. ___ we write the draft.» Opciones: Next, Finally.", "Next", "Después de elegir el tema viene el borrador."),
    ],
    [
        ("Pasos para hacer una carta: x) Put it in an envelope. y) Write the letter. z) Write the address. (envelope = sobre; address = dirección) El orden lógico es: a) y, z, x b) x, y, z", "a", "Primero se escribe la carta y al final se pone en el sobre."),
        ("Una opinión tiene estas partes: 1) razón 1, 2) opinión, 3) conclusión, 4) razón 2. ¿Cuál es el orden más claro? a) 2, 1, 4, 3 b) 3, 1, 2, 4", "a", "Opinión, razones y conclusión."),
        ("Ordena por tiempo: «after lunch / in the morning / at night». Escribe el orden con las letras x) after lunch y) in the morning z) at night.", "y, x, z", "Mañana, después del almuerzo y noche."),
    ],
    [
        ("Texto: «Finally, Nico won. First, he trained hard. Then, he ran the race.» ¿Qué oración está en el lugar equivocado? Opciones: Finally, Nico won; First, he trained hard.", "Finally, Nico won", "Debe ir al final del texto."),
        ("Texto: «First, I wake up. Then I eat breakfast. After that I go to school.» ¿Cuántas palabras de orden hay (first, then, after that)?", "3", "Hay First, Then y After that."),
    ],
    [
        ("Un relato dice: «After the storm, the sky was clear.» ¿Qué ocurrió primero? a) La tormenta b) El cielo despejado", "a", "After indica que el cielo se despejó luego de la tormenta."),
        ("Quieres opinar sobre usar casco y tienes dos razones: protege la cabeza y da buen ejemplo. Escribe el texto con First, Second e In conclusion. ¿Cuál orden de palabras es correcto? a) First, Second, In conclusion b) In conclusion, First, Second", "a", "La conclusión va al final."),
    ],
    [("Tu profesora te da estos pasos para preparar un té: pour hot water, put the tea bag in the cup, wait three minutes. (pour = verter; tea bag = bolsita de té; wait = esperar) ¿Qué paso va primero? a) put the tea bag in the cup b) wait three minutes", "a", "Primero se pone la bolsita; luego se agrega el agua y se espera.")],
    [
        ("¿Qué palabras ordenan los pasos de un relato?", "First, then, next, finally", "Guían al lector."),
        ("¿Dónde va la conclusión de una opinión?", "Al final", "Cierra las razones."),
        ("«Before» significa: a) antes de b) después de", "a", "Before indica algo anterior."),
    ],
    task("Ordena estas oraciones para escribir un relato de cinco líneas: «Finally, we ate lunch near the river.» «First, we left home at 8:00.» «Then, we walked in the forest.» «Last Sunday, my family went on a trip.» «After that, we found a small waterfall.» (river = río; waterfall = cascada) En tu hoja escribe el relato en orden y subraya las palabras de orden. Luego escribe una oración final de opinión con I think.", "Last Sunday, my family went on a trip. First, we left home at 8:00. Then, we walked in the forest. After that, we found a small waterfall. Finally, we ate lunch near the river. I think it was a great day because we were together.", ["las oraciones están en orden lógico", "subraya las palabras de orden", "la opinión usa I think y because"], ["relato ordenado y opinión en la hoja"], ["poner Finally al inicio", "olvidar la oración de presentación"], "Pregunta qué cambia si After that va antes de Then."),
    "Copia la lista de palabras de orden y escribe una oración con cada una.",
    "Escribe en cinco oraciones cómo preparas tu mochila antes de ir a clases, con First, Then, Next y Finally.",
)

# ============================================================ clase 4: conectar oraciones con coherencia
lesson(
    OA, 4,
    "Las oraciones y los párrafos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a unir oraciones con conectores como and, but, because, so, also y for example. Sirve para que mis textos se lean con fluidez y se entienda cómo se relacionan mis ideas.",
    ["Sé ordenar eventos con first, then y finally.", "Sé escribir oraciones simples."],
    [
        "Los conectores (connectors) muestran cómo se relacionan dos ideas. And suma: «I like tea and cake.» But contrasta: «I like tea but not coffee.» Because da una razón: «I stay home because I am sick.» So da un resultado: «I am sick, so I stay home.» Also agrega otra idea: «She is kind. She is also funny.» For example introduce un ejemplo.",
        "Para elegir, pregunta qué relación hay entre las dos ideas: ¿se suman?, ¿se oponen?, ¿una explica a la otra?, ¿una causa la otra? Si pones el conector equivocado, el sentido cambia. «It was cold, but I wore a jacket» suena raro; lo lógico es «It was cold, so I wore a jacket».",
        "Cuida la puntuación: antes de but y so se suele poner una coma cuando unen dos oraciones completas. Con because no se usa coma si la razón va al final. No abuses de un solo conector: si cada oración empieza con and, el texto se vuelve monótono. Alterna y usa palabras de orden y de ejemplo para dar variedad.",
    ],
    [("and", "y: suma"), ("but", "pero: contraste"), ("because", "porque: razón"), ("so", "así que: resultado"), ("also", "además"), ("for example", "por ejemplo"), ("comma", "coma")],
    [
        ("Elegir el conector según la relación", "Completa: «The movie was long, ___ I liked it.» Opciones: but, because. (long = larga)",
         ["Una película larga y que me gustó: hay un contraste.", "But expresa contraste.", "Because daría una razón que no calza."], "but"),
        ("Reconocer la relación", "Oración: «I was hungry, so I made a sandwich.» ¿Qué relación muestra so?",
         ["Primero ocurre el hambre.", "Luego ocurre la acción de hacer el sándwich.", "So muestra un resultado."], "Resultado."),
    ],
    [
        ("Poner and en todas las oraciones.", "Se usa el conector más conocido.", "Pregunta qué relación hay y elige el conector que calza."),
        ("Usar so cuando se da una razón.", "Se confunden causa y consecuencia.", "Because introduce la causa; so, la consecuencia."),
    ],
    [
        ("«So» muestra: a) un resultado b) una razón", "a", "So se usa para la consecuencia."),
        ("«But» muestra: a) un contraste b) un orden", "a", "But une ideas que se oponen."),
        ("Completa: «She likes apples ___ oranges.» Opciones: and, but.", "and", "Se suman dos frutas que le gustan."),
    ],
    [
        ("Completa: «I did not go out ___ it was raining.» Opciones: because, so.", "because", "La lluvia es la razón."),
        ("Completa: «It was raining, ___ I did not go out.» Opciones: because, so.", "so", "No salir es el resultado."),
        ("Completa: «My brother plays the guitar. He is ___ a good singer.» Opciones: also, because.", "also", "Agrega otra característica."),
    ],
    [
        ("Une con el conector adecuado: «I like cooking. I am not good at it.» a) I like cooking, but I am not good at it b) I like cooking, so I am not good at it.", "a", "Hay un contraste entre gusto y habilidad."),
        ("Une con el conector adecuado: «The room was dark. We turned on the light.» a) The room was dark, so we turned on the light b) The room was dark, but we turned on the light.", "a", "Encender la luz es consecuencia de la oscuridad."),
        ("Completa con un ejemplo: «We have many animals in the school, ___ two rabbits and a turtle.» Opciones: for example, because. (turtle = tortuga)", "for example", "Introduce ejemplos de los animales."),
    ],
    [
        ("Texto: «I love summer. I can swim. I can play outside.» ¿Qué conector une mejor las dos últimas? a) and b) but", "a", "Suma dos actividades."),
        ("Un compañero escribe: «I was tired, but I slept early.» ¿Qué conector sería más lógico? a) so b) but", "a", "Dormir temprano es consecuencia del cansancio."),
    ],
    [
        ("Elige la mejor versión: a) I like football because it is exciting and fun, but I also like reading b) I like football because it is exciting and fun and I like reading and I like music and I like sports.", "a", "Usa conectores variados y no repite."),
        ("Texto: «My city is big. It has many parks. ___, there is a river.» Opciones: Also, Because.", "Also", "Agrega otro dato."),
    ],
    [("Tu compañero te pide ayuda para unir estas ideas en una nota: «The match was cancelled. It rained all day.» (cancelled = cancelado) ¿Cuál une mejor? a) The match was cancelled because it rained all day b) The match was cancelled but it rained all day.", "a", "La lluvia es la razón de la cancelación.")],
    [
        ("¿Qué conector da una razón?", "Because", "Responde por qué."),
        ("¿Qué conector da un resultado?", "So", "Muestra una consecuencia."),
        ("Para dar un ejemplo usas: a) for example b) but", "a", "For example introduce un ejemplo."),
    ],
    task("Une las ideas de cada línea con un conector adecuado y escribe en tu hoja las tres oraciones: 1) «I want ice cream. It is too cold.» 2) «Maya is kind. She is generous.» 3) «The bus was late. We arrived at 9:00.» (generous = generosa; late = atrasado; arrived = llegamos) Luego escribe una oración propia con for example sobre tus pasatiempos.", "1) I want ice cream, but it is too cold. 2) Maya is kind and also generous. 3) The bus was late, so we arrived at 9:00. For example, I like drawing, reading and swimming.", ["elige conectores que calzan con la relación", "usa coma antes de but y so", "su oración con for example da ejemplos"], ["tres oraciones unidas y una oración propia"], ["usar and en las tres", "confundir because con so"], "Pregunta qué relación hay entre las ideas antes de escoger."),
    "Copia la tabla del vocabulario y escribe una oración con cada conector.",
    "Escribe un párrafo de cinco oraciones sobre tu semana usando but, so, because, also y for example.",
)

# ============================================================ clase 5: revisar primero el contenido y luego la exactitud
lesson(
    OA, 5,
    "Los textos con errores escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a revisar primero las ideas y el orden, y después la ortografía y la puntuación. Sirve para mejorar mis textos con método y no perder tiempo corrigiendo oraciones que luego se van a cambiar.",
    ["Sé declarar un propósito, elegir información, ordenarla y conectarla.", "Sé que las oraciones empiezan con mayúscula y terminan con punto."],
    [
        "Revisar un texto tiene dos etapas. Primero se revisa el contenido: ¿el texto cumple el propósito?, ¿tiene los datos o las razones necesarias?, ¿están en orden?, ¿sobra algo? Después se revisa la exactitud (accuracy): ortografía, puntuación y gramática. Esta secuencia evita corregir comas en una oración que luego vas a borrar.",
        "En la puntuación recuerda tres cosas. El punto (.) cierra una oración. La coma (,) separa elementos de una lista («apples, pears and bananas») y va antes de but y so. El signo de pregunta (?) cierra una pregunta: «Where do you live?» En inglés no existe el signo de pregunta inicial (¿): solo se usa al final.",
        "La ortografía de palabras frecuentes se aprende con práctica. Estas se escriben así: because, friend, people, school, together, favourite, beautiful. Si dudas, consulta tu lista o un diccionario. Hazte siempre dos preguntas: ¿se entiende lo que quiero decir? y ¿está bien escrito lo que quiero decir? En ese orden.",
    ],
    [("content", "contenido: ideas y orden"), ("accuracy", "exactitud: ortografía y gramática"), ("spelling", "ortografía"), ("full stop / period", "punto"), ("comma", "coma"), ("question mark", "signo de pregunta"), ("proofread", "revisar la forma final")],
    [
        ("Decidir qué revisar primero", "Borrador: «i like football becouse its fun. my frend plays with me. my dog is brown.» ¿Qué revisas primero: el contenido (la oración del perro no apoya la idea) o la ortografía?",
         ["El contenido está antes que la forma.", "La oración del perro sobra.", "Si la quitas, no gastas tiempo corrigiéndola."], "El contenido: quitar la oración del perro."),
        ("Corregir puntuación", "Oración: «Where do you live» Corrígela.",
         ["Es una pregunta.", "Va con signo de pregunta al final.", "No lleva signo inicial en inglés."], "Where do you live?"),
    ],
    [
        ("Corregir la ortografía de un texto que luego se rehará.", "Se empieza por la forma.", "Revisa primero contenido y orden."),
        ("Poner el signo de pregunta al inicio, como en español.", "Se traslada una regla del español.", "En inglés solo va al final: Where are you?"),
    ],
    [
        ("¿Qué se revisa primero? a) El contenido b) La ortografía", "a", "Las ideas y el orden van antes que la forma."),
        ("¿Cómo se escribe correctamente? a) because b) becouse", "a", "Because se escribe b-e-c-a-u-s-e; con o está mal."),
        ("En Inglés (oficial): ¿Qué signo cierra una pregunta en inglés?", "?", "El signo de pregunta va solo al final."),
    ],
    [
        ("Elige la oración bien puntuada. a) What is your name? b) What is your name", "a", "Una pregunta termina en ?"),
        ("Elige la lista bien escrita. a) I have a pen, a book and a ruler. b) I have a pen a book and a ruler", "a", "Se separa con comas y termina en punto."),
        ("Corrige la ortografía de «frend». Opciones: friend, freind.", "friend", "Se escribe friend."),
    ],
    [
        ("Texto: «We play together. We are frends.» ¿Qué palabra tiene error de ortografía y cómo se escribe bien?", "frends; friends", "Se escribe friends: la i va antes de la e, y es plural."),
        ("Texto: «People like the park becouse it is beautiful.» ¿Cuántas palabras tienen error?", "1", "Solo becouse debe ser because."),
        ("Elige la oración corregida. a) I like the school because my friends are there. b) i like the school becouse my frends are there", "a", "Corrige mayúscula, ortografía y plural."),
    ],
    [
        ("Un compañero revisa las comas de su texto, pero el texto no explica por qué le gusta el parque. ¿Qué etapa se saltó? a) Revisar el contenido b) Revisar la ortografía", "a", "Debe revisar primero que el texto cumpla su propósito."),
        ("Ordena las tareas de revisión: x) Revisar ortografía y puntuación y) Agregar una razón que falta z) Quitar una oración que sobra. ¿Cuál es el mejor orden? a) y, z, x b) x, y, z", "a", "Primero contenido, después forma."),
    ],
    [
        ("Texto: «Why do you like music? I like music because it makes me happy.» (makes me happy = me alegra) ¿Cuántos signos de pregunta tiene?", "1", "Solo la primera oración es pregunta."),
        ("Lee: «We go to scool with our frend.» ¿Cuántas palabras están mal escritas?", "2", "Faltan school y friend."),
    ],
    [("Tu profesora devuelve tu texto sobre un parque con la nota: «Faltan razones». ¿Qué haces primero? a) Agregar razones con because b) Corregir comas", "a", "La nota habla del contenido, que se revisa antes.")],
    [
        ("¿Por qué se revisa primero el contenido?", "Para no corregir lo que luego se va a cambiar", "Ahorra tiempo y evita repetir trabajo."),
        ("¿Dónde va el signo de pregunta en inglés?", "Solo al final", "No existe el signo inicial."),
        ("Elige la grafía correcta: a) people b) peeple", "a", "People se escribe con o."),
    ],
    task("Revisa este texto en dos pasos: «i think the park is good becouse it have trees. my frend likes the park too. the zoo is far. do you like the park» (far = lejos). Paso 1, contenido: tacha la oración que sobra y agrega una razón más con also. Paso 2, exactitud: reescribe el texto corregido con mayúsculas, puntos, signo de pregunta, becouse y frend corregidos, y have a has.", "Paso 1: se tacha The zoo is far. Se agrega Also, we can play there. Paso 2: I think the park is good because it has trees. Also, we can play there. My friend likes the park too. Do you like the park?", ["revisa primero el contenido", "corrige mayúsculas, puntos y ?", "corrige because, friend y has"], ["texto revisado y texto final en la hoja"], ["corregir solo la forma", "dejar la oración irrelevante"], "Pregunta por qué empezó por el contenido."),
    "Copia las siete palabras de ortografía de la explicación y escribe una oración con cada una.",
    "Pide a otra persona que lea tu texto y marque una parte que no se entiende; mejora esa parte.",
)

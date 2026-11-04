"""Cuaderno del estudiante, 1.º medio Inglés (oficial), IN1M OA 06: planificar, reparar y revisar el inglés hablado.

Las clases del plan son genéricas; aquí se aplican a: antes de hablar (diagramas, ensayo, conexiones), al hablar (parafrasear,
sinónimos, chunks), rellenos y autocorrección, después de hablar (metas y registro de errores) y un ciclo completo.
Las situaciones traen los diálogos, tablas y notas escritos en el enunciado.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA = "IN1M OA 06"
MAT = "Los diálogos, diagramas y tablas escritos en cada ejercicio, lápiz, una hoja para dibujar y una persona de tu casa para ensayar en voz alta."


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


# ------------------------------------------------------------------ clase 1: antes de hablar
DIAG = "Diagrama: centro «Healthy lunch». Rama 1: fruit (apple, banana). Rama 2: water. Rama 3: protein (egg, beans). Conexión: my school canteen. (healthy lunch = almuerzo saludable, fruit = fruta, protein = proteína, egg = huevo, beans = porotos)"

lesson(
    OA, 1, MAT,
    "Aprenderé a prepararme antes de hablar: organizar las ideas clave en un diagrama, hacer conexiones con lo que sé y ensayar en voz alta. Sirve para hablar con más claridad y menos nervios.",
    ["Sé hacer una presentación corta con ideas ordenadas.", "Conozco palabras como topic, idea y example."],
    [
        "Antes de hablar, planificar ahorra problemas. Un diagrama (diagram) o mapa de ideas pone en el centro la idea principal y en las ramas las ideas clave, escritas con pocas palabras. No copies tu texto completo: las ramas son pistas para recordar. Un diagrama de Healthy lunch puede tener tres ramas: fruit, water y protein.",
        "Hacer conexiones (making connections) significa relacionar tu tema con lo que ya sabes: otra asignatura, tu vida diaria o una experiencia. Por ejemplo: In Science, we learned that plants need light. Las conexiones hacen tu presentación más interesante y te dan frases que ya conoces. Anótalas junto a las ramas del diagrama.",
        "Por último, practica (practise) tu presentación en voz alta. Ensayar tres veces es mejor que leer en silencio una vez, porque tu boca practica los sonidos y puedes medir el tiempo. Si cada rama dura unos 30 segundos y tienes cuatro ramas, tu presentación durará unos dos minutos. Ensaya con una persona de tu casa o frente a un espejo.",
    ],
    [("diagram", "diagrama o mapa de ideas"), ("branch", "rama: una idea clave"), ("connection", "conexión: relación con lo que sé"), ("practise", "ensayar, practicar"), ("key idea", "idea clave"), ("rehearse", "ensayar")],
    [
        ("Leer un diagrama", DIAG + " ¿Cuántas ideas principales hay y cuál es la conexión?", ["Cuento las ramas: fruit, water y protein.", "Son tres ideas principales.", "La conexión es my school canteen."], "Tres ideas; la conexión es la cafetería del colegio"),
        ("Calcular el tiempo de ensayo", "Tienes cuatro ramas y cada una dura unos 30 segundos. ¿Cuántos segundos dura tu presentación?", ["Multiplico el número de ramas por el tiempo de cada una.", "4 × 30 = 120.", "120 segundos son dos minutos."], "120 segundos, es decir, 2 minutos"),
    ],
    [
        ("Escribir frases completas en las ramas del diagrama.", "Se confunde el diagrama con un guion y se pierde el tiempo.", "Escribe solo palabras clave que te recuerden la idea."),
        ("Leer el texto en silencio y no ensayar en voz alta.", "Se cree que entender el texto basta para hablar bien.", "Practica en voz alta, con reloj, al menos tres veces."),
    ],
    [
        ("En un diagrama, ¿qué va en el centro? A) la idea principal B) los saludos", "A) la idea principal", "El centro muestra el tema y las ramas lo desarrollan."),
        ("¿Qué escribes en las ramas del diagrama? A) palabras clave de cada idea B) el texto completo de la presentación", "A) palabras clave de cada idea", "Las ramas son pistas breves."),
        ("¿Qué es más útil para practicar antes de hablar? A) decirlo en voz alta tres veces B) leerlo mentalmente una vez", "A) decirlo en voz alta tres veces", "Practicar en voz alta entrena los sonidos y el tiempo."),
    ],
    [
        (DIAG + " ¿Cuántas ideas principales tiene el diagrama? A) tres B) cuatro", "A) tres", "Las ramas son fruit, water y protein."),
        (DIAG + " ¿Qué frase sale de la rama 2? A) Water is important for lunch. B) Beans are a fruit.", "A) Water is important for lunch.", "La rama 2 dice water."),
        (DIAG + " ¿Qué muestra la conexión «my school canteen»? A) relaciona el tema con la vida cotidiana B) agrega una cuarta rama", "A) relaciona el tema con la vida cotidiana", "Conecta el almuerzo saludable con un lugar real."),
    ],
    [
        ("Diagrama con centro «Sports at school». Ramas posibles: football, basketball, my cousin's birthday, volleyball. ¿Cuál no corresponde al tema? A) my cousin's birthday B) volleyball", "A) my cousin's birthday", "No es un deporte escolar."),
        arith("Cada rama de tu diagrama se explica en 20 segundos y tienes 6 ramas. ¿Cuántos segundos dura la presentación?", "6*20", "Se multiplican las ramas por 20 segundos.", " segundos"),
        ("Tu tema es «plants» y quieres conectarlo con Ciencias. ¿Qué frase sirve? A) In Science, we learned that plants need light. B) In Music, we learned a new song.", "A) In Science, we learned that plants need light.", "Relaciona el tema con Ciencias."),
    ],
    [
        ("Un diagrama tiene el texto completo de la presentación en cada rama. ¿Por qué es poco útil? A) porque no se lee rápido y no ayuda a recordar B) porque ocupa menos espacio", "A) porque no se lee rápido y no ayuda a recordar", "Las ramas deben ser breves para servir de pista."),
        arith("Ensayas tres veces en voz alta una presentación de 2 minutos. ¿Cuántos minutos practicas en total?", "3*2", "Tres ensayos de 2 minutos cada uno.", " minutos"),
    ],
    [
        ("Ordena con letras los pasos para prepararte: (a) ensayar en voz alta (b) elegir el tema y la idea central (c) escribir las ramas con palabras clave (d) agregar una conexión con tu experiencia.", "b, c, d, a", "Se planifica antes de ensayar."),
        ("Diagrama: centro «My pet», ramas food, walks, vet y conexión «I have walked my dog every day since March». ¿Qué dato de la conexión muestra experiencia personal? A) I have walked my dog every day since March B) food", "A) I have walked my dog every day since March", "Es una experiencia propia que se relaciona con el tema."),
    ],
    [("Mañana presentas sobre bicicletas ante tu curso y tienes 20 minutos para prepararte. ¿Qué plan usas? A) hacer un diagrama de tres ramas y ensayar dos veces en voz alta B) escribir todo y leerlo una vez en silencio", "A) hacer un diagrama de tres ramas y ensayar dos veces en voz alta", "Combina planificación y práctica oral.")],
    [
        ("En Inglés de 1.º medio (OA 6, clase 1): ¿qué es un diagrama de ideas?", "Un esquema con la idea principal al centro y las ideas clave en ramas", "Ayuda a organizar lo que se va a decir."),
        ("En Inglés de 1.º medio (OA 6, clase 1): ¿qué es hacer una conexión?", "Relacionar el tema con lo que ya sé, como otra asignatura o una experiencia", "Aporta frases conocidas."),
        ("En Inglés de 1.º medio (OA 6, clase 1): ¿cuántas veces conviene ensayar en voz alta?", "Al menos tres veces", "La práctica oral mejora la fluidez."),
    ],
    task("Tema: «My favourite season» (mi estación favorita). Dibuja en tu hoja un diagrama con el tema al centro, tres ramas de palabras clave y una conexión con tu experiencia. Luego ensaya tres veces en voz alta frente a una persona de tu casa y anota cuánto duró cada intento.", "Centro: My favourite season. Ramas: weather, food, activities. Conexión: In summer, I swim in the sea. Duración: 1 min 40 s, 1 min 30 s, 1 min 25 s.", ["el centro y las ramas son claros y breves", "incluye una conexión personal", "registra tres intentos con su duración"], ["hoja con el diagrama", "tabla de tiempos"], ["escribir frases largas en las ramas", "ensayar solo en silencio"], "Reconoce el diagrama y pide acortar las ramas a palabras clave si se parecen a un texto."),
    "Convierte el diagrama de esta clase en tres frases en inglés, una por rama.",
    "Haz un diagrama para un tema de otra asignatura y explícalo en voz alta en un minuto.",
)

# ------------------------------------------------------------------ clase 2: parafrasear, sinónimos y chunks
lesson(
    OA, 2, MAT,
    "Aprenderé a seguir hablando cuando me falta una palabra: parafraseando, usando sinónimos y apoyándome en expresiones de uso frecuente (chunks). Sirve para mantener la conversación sin quedarme en silencio.",
    ["Conozco palabras básicas como big, small y easy.", "Sé usar frases como for example."],
    [
        "Parafrasear (to paraphrase) es decir lo mismo con otras palabras. Si no recuerdas hard, puedes decir difficult. Un sinónimo (synonym) es una palabra con significado muy parecido: big y large, begin y start, easy y simple, fast y quick, glad y happy. Elegir un sinónimo conocido evita repetir la misma palabra o quedarse sin palabra.",
        "Los chunks son grupos de palabras que se aprenden y se usan juntos, sin armarlos palabra por palabra. Ejemplos: a lot of, for example, in my opinion, as far as I know, kind of, it depends on y by the way. Usar chunks te da fluidez, porque los dices como una sola unidad. Aprende cada chunk con una frase completa: A lot of students like music.",
        "Si no conoces una palabra, descríbela: lo llaman circunloquio. Si olvidaste eraser (goma), puedes decir It's the thing you use to remove pencil marks. Describe para qué sirve, cómo es o dónde está. La otra persona suele entender y a veces te da la palabra. Esa estrategia mantiene tu mensaje vivo.",
    ],
    [("paraphrase", "decir lo mismo con otras palabras"), ("synonym", "sinónimo: palabra de sentido parecido"), ("chunk", "grupo de palabras de uso frecuente"), ("a lot of", "muchos, mucha"), ("it depends on", "depende de"), ("the thing you use to...", "la cosa que se usa para...")],
    [
        ("Parafrasear con un sinónimo", "Quieres decir «The test was difficult» con otra palabra. ¿Qué frase sirve? A) The test was hard. B) The test was boring.", ["Busco una palabra de sentido parecido.", "Difficult y hard significan difícil.", "Boring significa aburrido."], "A) The test was hard."),
        ("Describir una palabra olvidada", "Olvidaste la palabra ruler (regla). ¿Qué descripción te ayuda? A) It's the thing you use to draw straight lines. B) It's a type of food.", ["Pienso para qué sirve el objeto.", "La regla sirve para trazar líneas rectas.", "La descripción A calza."], "A) It's the thing you use to draw straight lines."),
    ],
    [
        ("Quedarse en silencio cuando falta una palabra.", "Se cree que sin la palabra exacta no se puede seguir.", "Parafrasea o describe para qué sirve."),
        ("Armar un chunk palabra por palabra, como a lot students.", "No se aprendió como un grupo completo.", "Aprende a lot of con una frase completa."),
    ],
    [
        ("¿Qué sinónimo de big sirve? A) large B) tiny", "A) large", "Large significa grande."),
        ("¿Qué sinónimo de begin sirve? A) start B) finish", "A) start", "Start significa comenzar."),
        ("¿Qué significa el chunk for example? A) por ejemplo B) por favor", "A) por ejemplo", "Introduce un caso concreto."),
    ],
    [
        ("Completa: «As far as ___ know, the bus leaves at eight.» A) I B) me", "A) I", "El chunk completo es as far as I know."),
        ("Completa: «It ___ on the weather.» A) depends B) depend", "A) depends", "It depends on... lleva s con it."),
        ("Olvidaste la palabra umbrella. ¿Qué descripción ayuda? A) It's what you open when it rains. B) It's what you wear on your feet.", "A) It's what you open when it rains.", "Describe para qué se usa."),
    ],
    [
        ("Cambia glad por un sinónimo en «She is glad today.» A) She is happy today. B) She is tall today.", "A) She is happy today.", "Glad y happy son sinónimos."),
        ("¿Qué significa kind of en «The film was kind of long»? A) más o menos, algo B) muy corta", "A) más o menos, algo", "Kind of suaviza la descripción."),
        ("¿Qué frase usa bien el chunk a lot of? A) A lot of students like music. B) A lot students like music.", "A) A lot of students like music.", "El chunk lleva of."),
    ],
    [
        ("Quieres decir «The test was easy» de otra manera. ¿Qué paráfrasis sirve? A) The test was simple. B) The test was complicated.", "A) The test was simple.", "Easy y simple son sinónimos."),
        ("No recuerdas ruler y dices «the thing for drawing straight lines». ¿Qué estrategia usaste? A) describir el objeto B) quedarte en silencio", "A) describir el objeto", "Es un circunloquio: describir para qué sirve."),
    ],
    [
        ("Reemplaza la repetición en «The park is nice. The weather is nice. The people are nice.» ¿Cuál es la mejor versión? A) The park is nice. The weather is pleasant. The people are friendly. B) The park is nice. The weather is nice. The people are nice.", "A) The park is nice. The weather is pleasant. The people are friendly.", "Se usan palabras distintas con sentido parecido."),
        ("¿Cuál frase usa un chunk para dar una opinión? A) In my opinion, the park needs more trees. B) The park trees more needs.", "A) In my opinion, the park needs more trees.", "In my opinion es un chunk para opinar."),
    ],
    [("En una entrevista olvidas la palabra backpack (mochila). ¿Qué dices? A) It's the bag we carry on our back to school. B) I don't know, sorry.", "A) It's the bag we carry on our back to school.", "Describir mantiene la conversación.")],
    [
        ("En Inglés de 1.º medio (OA 6, clase 2): ¿qué es parafrasear?", "Decir lo mismo con otras palabras", "Evita quedarse sin palabra."),
        ("En Inglés de 1.º medio (OA 6, clase 2): ¿qué es un chunk?", "Un grupo de palabras de uso frecuente que se aprende como una unidad", "Por ejemplo, a lot of."),
        ("En Inglés de 1.º medio (OA 6, clase 2): ¿qué haces si olvidas una palabra?", "La describes: para qué sirve, cómo es o dónde está", "Mantiene el mensaje."),
    ],
    task("Imagina que olvidaste estas tres palabras: eraser (goma), scissors (tijeras) y fridge (refrigerador). Escribe en inglés una descripción de una frase para cada una, sin decir la palabra. Luego escribe una frase con el chunk a lot of y otra con it depends on.", "Eraser: It's the thing you use to remove pencil marks. Scissors: They are the tool we use to cut paper. Fridge: It's the machine that keeps food cold. A lot of students use erasers. It depends on the weather.", ["las tres descripciones dicen para qué sirve el objeto", "ninguna usa la palabra olvidada", "las frases con chunks son correctas"], ["hoja con cinco frases", "lectura en voz alta"], ["decir la palabra en español en vez de describir", "escribir a lot students"], "Reconoce las descripciones útiles y, si aparece la palabra prohibida, pide reformular con función o lugar."),
    "Escribe en tarjetas diez sinónimos o chunks de esta clase con una frase de ejemplo cada uno.",
    "Elige un objeto de tu casa y descríbelo en inglés sin decir su nombre para que otra persona lo adivine.",
)

# ------------------------------------------------------------------ clase 3: rellenos, conectores y autocorrección
lesson(
    OA, 3, MAT,
    "Aprenderé a ganar tiempo al hablar con rellenos como Well... e I mean..., a unir ideas con conectores y a corregirme con ayuda. Sirve para sonar más natural y no detenerme cuando me equivoco.",
    ["Sé parafrasear y usar chunks.", "Conozco conectores como and, but, because y so."],
    [
        "Los rellenos temporales (fillers) son palabras o frases que usas mientras piensas. Well... significa bueno. Let me think... significa déjame pensar. I mean... sirve para aclarar o corregir: It's on Monday, I mean Tuesday. I see... significa ya veo o entiendo cuando reaccionas a lo que dice otra persona. Úsalos con moderación: uno o dos por frase larga, no en cada palabra.",
        "Los conectores (connectors) unen tus ideas y ayudan a que suenes fluido: and agrega, but contrasta, because da una razón, so da una consecuencia, then muestra el orden y also agrega algo más. Con conectores puedes hablar más tiempo y con más claridad: I like football because it is fun, but I also like swimming.",
        "Autocorregirse (to self-correct) es notar tu error y arreglarlo mientras hablas. Puedes decir I go... sorry, I went to the park yesterday. A veces otra persona te ayuda: Do you mean went? Aceptar la ayuda y repetir la frase correcta es parte de aprender. Corregirte no es un fracaso: muestra que estás atento a tu inglés.",
    ],
    [("Well...", "Bueno..."), ("Let me think...", "Déjame pensar..."), ("I mean...", "Quiero decir..."), ("I see...", "Ya veo..., entiendo"), ("sorry, I mean...", "perdón, quiero decir..."), ("self-correct", "corregirse")],
    [
        ("Usar un relleno para pensar", "Te preguntan «Where were you last weekend?» y necesitas pensar. ¿Qué empiezas diciendo? A) Well... let me think... B) Because and then.", ["Necesito unos segundos.", "Well y Let me think son rellenos.", "Después sigo con la respuesta."], "A) Well... let me think..."),
        ("Corregirte", "Dijiste «I go to the park yesterday» y notas el error. ¿Qué puedes decir? A) Sorry, I went to the park yesterday. B) I go to the park yesterday.", ["Noto que yesterday pide pasado.", "Uso Sorry para corregirme.", "Repito con went."], "A) Sorry, I went to the park yesterday."),
    ],
    [
        ("Decir I mean... en cada frase sin pensar.", "Se usa el relleno por nervios y deja de ayudar.", "Úsalo solo cuando necesites aclarar o pensar."),
        ("Detenerse por completo al notar un error.", "Se cree que corregirse interrumpe todo.", "Di Sorry, I mean... y sigue."),
    ],
    [
        ("¿Qué significa Let me think...? A) déjame pensar B) quiero comer", "A) déjame pensar", "Gana tiempo para elegir la respuesta."),
        ("En «It's on Monday, I mean Tuesday», ¿para qué sirve I mean? A) para corregir un dato B) para saludar", "A) para corregir un dato", "Cambia Monday por Tuesday."),
        ("¿Qué conector da una razón? A) because B) but", "A) because", "Because explica por qué."),
    ],
    [
        ("Alguien te cuenta que su perro se perdió y respondes «I see...». ¿Qué significa tu reacción? A) entiendo lo que me cuentas B) tengo un perro", "A) entiendo lo que me cuentas", "I see... reacciona mostrando comprensión."),
        ("Completa con un conector: «I like football, ___ I also like swimming.» A) but B) because", "A) but", "El conector agrega un contraste suave con also."),
        ("Completa con un conector: «It was raining, ___ we stayed at home.» A) so B) but", "A) so", "So da la consecuencia."),
    ],
    [
        ("Un amigo te dice «Do you mean went?» cuando dijiste «I go yesterday». ¿Qué haces? A) Repites: I went to the park yesterday. B) Repites: I go yesterday.", "A) Repites: I went to the park yesterday.", "Aceptas la ayuda y dices la forma correcta."),
        ("Quieres decir «I like football because it is fun, but I also like swimming». ¿Qué conectores usas? A) because, but, also B) so, then, first", "A) because, but, also", "Son los de la frase original."),
        ("En «Then I played football, but I was tired, so I came home», ¿qué conector muestra una consecuencia? A) so B) then", "A) so", "So indica lo que pasó como resultado del cansancio."),
    ],
    [
        ("Quieres decir en inglés «Es el lunes, perdón, el martes». ¿Qué frase usa un relleno para corregir? A) It's on Monday, I mean Tuesday. B) It's on Monday and Tuesday.", "A) It's on Monday, I mean Tuesday.", "I mean reemplaza el dato equivocado."),
        ("Te preguntan «Where do you live?» y necesitas pensar. ¿Qué respuesta usa un relleno sin detener la conversación? A) Well... let me think. I live near the park. B) Park... near... I... live...", "A) Well... let me think. I live near the park.", "El relleno da tiempo y luego viene una frase completa."),
    ],
    [
        ("Un estudiante dice: «Well... I mean, last weekend I went to the park. It was, let me think, a nice place.» ¿Cuántos rellenos usó? A) 3 B) 2", "A) 3", "Well, I mean y let me think son tres."),
        ("Un estudiante usa un relleno antes de cada palabra: «Well... I mean... the... well... park... I mean... is... well... big.» ¿Qué debería mejorar? A) usar los rellenos con moderación B) usar más rellenos", "A) usar los rellenos con moderación", "Demasiados rellenos interrumpen la fluidez."),
    ],
    [("Te dicen «We could go to the cinema or to the beach». No quieres decidir de inmediato. ¿Qué respuesta ganas tiempo con naturalidad? A) Well... let me think. I mean, both are good. B) Cinema beach.", "A) Well... let me think. I mean, both are good.", "Usa dos rellenos y una frase completa.")],
    [
        ("En Inglés de 1.º medio (OA 6, clase 3): ¿para qué sirve I mean...?", "Para aclarar o corregir lo que dijiste", "Por ejemplo, Monday, I mean Tuesday."),
        ("En Inglés de 1.º medio (OA 6, clase 3): ¿qué conector da una consecuencia?", "So", "Dice qué pasó por eso."),
        ("En Inglés de 1.º medio (OA 6, clase 3): ¿qué dices para corregirte mientras hablas?", "Sorry, I mean...", "Anuncia la corrección."),
    ],
    task("Responde en voz alta, en tres a cinco frases, la pregunta «What did you do last weekend?» (qué hiciste el fin de semana). Usa al menos un relleno (Well, Let me think, I mean), dos conectores (because, but, so, then, also) y una autocorrección con Sorry, I mean... Pide a una persona de tu casa que marque cada estrategia que oiga.", "Well, last Saturday I went to the park because the weather was nice. Then I played football, but I was tired, so I came home. I played... sorry, I mean, I watched a film in the evening.", ["usa un relleno", "usa dos conectores", "se corrige con Sorry, I mean..."], ["hoja con la respuesta", "marcas de la persona oyente"], ["usar relleno en cada palabra", "no corregir un error evidente"], "Reconoce cada estrategia usada y sugiere dónde sacar un relleno si hay demasiados."),
    "Haz una lista de tres rellenos y tres conectores y úsalos en una conversación de un minuto.",
    "Cuenta en inglés lo que hiciste ayer y corrígete en voz alta cada vez que notes un error de pasado.",
)

# ------------------------------------------------------------------ clase 4: después de hablar
LOG = "Registro de errores: (1) «I go yesterday» (2) «I have 15 years» (3) «She don't like pizza» (4) «I make homework» (5) «more bigger»."

lesson(
    OA, 4, MAT,
    "Aprenderé a revisar mi manera de hablar después de una presentación: identificar debilidades, registrar errores, corregirlos con recursos y fijarme metas. Sirve para mejorar de verdad en la próxima ocasión.",
    ["Sé usar estrategias para hablar mejor.", "Conozco el tiempo pasado y el presente simple."],
    [
        "Después de hablar viene la revisión (review). Primero identifica tus debilidades (weaknesses): lo que no salió bien, con ayuda de una grabación o de los comentarios de otra persona. También anota tus fortalezas (strengths): lo que salió bien. Un buen comentario es específico: I said 'I go yesterday' en vez de hablaste mal.",
        "Después registra tus errores en una tabla con tres columnas: lo que dije, la forma correcta y el consejo o la regla. Por ejemplo: I have 15 years → I am 15 years old (en inglés la edad se dice con be). She don't like pizza → She doesn't like pizza (con she se usa doesn't). I make homework → I do homework. more bigger → bigger (no se duplica la comparación).",
        "Para corregir usa recursos: un diccionario, tus apuntes de gramática, una lista de collocations o una grabación para escucharte. Luego fija una meta concreta (goal): hoy corregiré el pasado de tres verbos y la usaré en mi próxima presentación. Revisa la meta después. Cuando dos personas te dan comentarios, junta ambos y prioriza uno o dos errores a la vez.",
    ],
    [("weakness / strength", "debilidad / fortaleza"), ("error log", "registro de errores"), ("goal", "meta"), ("dictionary", "diccionario"), ("I am 15 years old.", "Tengo 15 años."), ("She doesn't like...", "A ella no le gusta...")],
    [
        ("Corregir con una regla", LOG + " Corrige el error (2) y explica la regla.", ["El error es I have 15 years.", "La edad se dice con be.", "La forma correcta es I am 15 years old."], "I am 15 years old; la edad se dice con be"),
        ("Corregir un error de tiempo", LOG + " Corrige el error (1).", ["El error es I go yesterday.", "Yesterday indica pasado.", "El pasado de go es went."], "I went yesterday"),
    ],
    [
        ("Anotar solo que hablé mal, sin decir qué errores hubo.", "Un comentario general no se puede corregir.", "Anota la frase exacta y la forma correcta."),
        ("Corregir diez errores a la vez.", "Se pierde el foco y no se recuerda ninguno.", "Elige uno o dos errores como meta."),
    ],
    [
        ("¿Qué es una debilidad en la revisión de una presentación? A) algo que no salió bien y puedes mejorar B) un premio que ganaste", "A) algo que no salió bien y puedes mejorar", "Se identifica para trabajarla."),
        ("¿Qué columnas tiene un registro de errores? A) lo que dije, la forma correcta y el consejo B) solo la fecha", "A) lo que dije, la forma correcta y el consejo", "Así el error se vuelve aprendizaje."),
        ("¿Qué recurso sirve para revisar palabras? A) un diccionario B) un reloj", "A) un diccionario", "Muestra significado y uso."),
    ],
    [
        (LOG + " ¿Cuál es la forma correcta del error (3)? A) She doesn't like pizza. B) She don't likes pizza.", "A) She doesn't like pizza.", "Con she se usa doesn't y el verbo va sin s."),
        (LOG + " ¿Cuál es la forma correcta del error (4)? A) I do homework. B) I make homework.", "A) I do homework.", "La collocation de homework es con do."),
        (LOG + " ¿Cuál es la forma correcta del error (5)? A) bigger B) more bigger", "A) bigger", "No se usa more con un comparativo en -er."),
    ],
    [
        ("Tienes cinco errores en tu registro. ¿Cuántos eliges como meta para la próxima vez? A) uno o dos B) todos", "A) uno o dos", "Un foco pequeño es más fácil de lograr."),
        ("¿Qué meta es mejor? A) Use the past tense of go, see and eat in my next talk. B) Speak better.", "A) Use the past tense of go, see and eat in my next talk.", "Es específica y se puede comprobar."),
        ("Tu compañero dice «You spoke clearly, but add examples». ¿Qué anotas como fortaleza? A) hablaste claro B) agregar ejemplos", "A) hablaste claro", "Los ejemplos son la debilidad que mejorar."),
    ],
    [
        ("Tu profesor anota «Check past tense: I go yesterday». Tu compañero anota «Your voice was clear; I have 15 years is wrong». Juntando ambos comentarios, ¿cuántos errores debes registrar? A) 2 B) 1", "A) 2", "I go yesterday e I have 15 years son dos errores distintos."),
        ("Escuchas tu grabación y notas que dijiste «I am agree». ¿Qué corrección corresponde? A) I agree. B) I am agreed.", "A) I agree.", "Agree es un verbo y no lleva am."),
    ],
    [
        ("Una grabación te ayuda a revisar. ¿Qué haces con ella? A) la escuchas y anotas frases con errores B) la borras sin escucharla", "A) la escuchas y anotas frases con errores", "Escucharte permite detectar errores reales."),
        ("Tu registro dice: «I make homework → I do homework». ¿Qué consejo anotas en la tercera columna? A) homework va con do B) usar siempre make", "A) homework va con do", "Es la collocation correcta."),
    ],
    [("Un estudiante escribe como meta «Be perfect». ¿Cómo la mejoras? A) Use because and so in two sentences next time. B) Never make mistakes.", "A) Use because and so in two sentences next time.", "Una meta mejor es concreta, alcanzable y se puede comprobar.")],
    [
        ("En Inglés de 1.º medio (OA 6, clase 4): ¿qué es un registro de errores?", "Una tabla con lo que dije, la forma correcta y un consejo", "Sirve para aprender de los errores."),
        ("En Inglés de 1.º medio (OA 6, clase 4): ¿cómo se dice la edad en inglés?", "Con be: I am 15 years old", "No se usa have para la edad."),
        ("En Inglés de 1.º medio (OA 6, clase 4): ¿cómo es una buena meta?", "Concreta y fácil de comprobar", "Dice qué harás y cómo notarás el logro."),
    ],
    task("Lee estos errores de una presentación (de ejemplo): (1) «I play football yesterday», (2) «My brother have 12 years», (3) «She go to school every day». Escribe en una tabla con tres columnas lo que se dijo, la forma correcta y un consejo, y fija una meta de una frase.", "(1) I play football yesterday → I played football yesterday (pasado con yesterday). (2) My brother have 12 years → My brother is 12 years old (edad con be). (3) She go to school → She goes to school (con she el verbo lleva s). Meta: Use the past simple with yesterday in my next talk.", ["corrige los tres errores", "escribe la forma correcta y un consejo", "fija una meta concreta"], ["tabla de tres columnas", "meta escrita"], ["dejar un error sin su consejo", "una meta vaga"], "Reconoce los errores bien registrados y revisa que la meta diga qué hará y cuándo."),
    "Escribe en una tabla tres errores que cometes al hablar inglés y su forma correcta.",
    "Graba un mensaje de 30 segundos en inglés, escúchalo y anota una fortaleza y una debilidad.",
)

# ------------------------------------------------------------------ clase 5: ciclo completo
TRANS = "Un estudiante dice: «Well... last weekend I went to the park. It was, let me think, a nice place. I forgot the word... the thing for sitting. Yes, the bench. We played football, but I was tired, so I went home. I go... sorry, I went to bed early.»"

lesson(
    OA, 5, MAT,
    "Aprenderé a usar el ciclo completo de estrategias: planificar antes, parafrasear y corregirme al hablar, y revisar después con metas. Sirve para hablar inglés con más seguridad.",
    ["Sé planificar con un diagrama y ensayar.", "Sé parafrasear, usar rellenos y registrar errores."],
    [
        "El ciclo de estrategias tiene tres momentos. Antes de hablar: diagrama de ideas, conexiones y ensayo en voz alta. Mientras hablas: parafrasear, usar sinónimos y chunks, ganar tiempo con rellenos (Well..., I mean..., I see...), unir ideas con conectores y corregirte si te equivocas. Después de hablar: identificar debilidades, registrar errores y fijar metas.",
        "Cada estrategia resuelve un problema distinto. Si olvidas una palabra, describe su uso. Si necesitas tiempo, usa un relleno. Si te equivocas, di Sorry, I mean... y continúa. Si al final notas que repites el mismo error, anótalo en el registro y busca el consejo en un diccionario o en tus apuntes. No necesitas hablar perfecto, sino comunicar y mejorar.",
        "Un ejemplo completo de uso: Well... I went to the park, but I forgot the word... the thing for sitting. Yes, the bench. Aquí hay relleno, conector, descripción y la palabra recuperada. Para evaluarte, marca qué estrategias usaste, qué error cometiste y qué meta fijas. El progreso se ve cuando comparas dos intentos.",
    ],
    [("strategy", "estrategia"), ("cycle", "ciclo: antes, durante y después"), ("describe", "describir"), ("bench", "banca"), ("progress", "progreso"), ("attempt", "intento")],
    [
        ("Identificar estrategias en un habla", TRANS + " ¿Qué estrategia usó cuando olvidó una palabra?", ["Dijo I forgot the word.", "Describió: the thing for sitting.", "Recuperó la palabra: bench."], "Describió el objeto (the thing for sitting) y recuperó bench"),
        ("Identificar una autocorrección", TRANS + " ¿Qué se corrigió y cómo?", ["Dijo I go.", "Notó el error y dijo sorry.", "Corrigió a I went to bed early."], "Corrigió I go por I went con sorry"),
    ],
    [
        ("Pensar que solo se necesitan estrategias cuando se habla mal.", "Se piensa que las estrategias son para corregir, no para preparar.", "Planifica antes, usa estrategias durante y revisa después."),
        ("Registrar errores pero no fijar una meta.", "Se cree que anotar basta.", "Convierte el error en una meta concreta para la próxima vez."),
    ],
    [
        ("¿Qué estrategia se usa antes de hablar? A) hacer un diagrama de ideas B) corregirte con Sorry", "A) hacer un diagrama de ideas", "Es una estrategia de planificación."),
        ("¿Qué estrategia se usa mientras hablas si olvidas una palabra? A) describirla B) borrarla de la mente", "A) describirla", "Mantiene el mensaje."),
        ("¿Qué estrategia se usa después de hablar? A) registrar errores y fijar una meta B) ensayar antes", "A) registrar errores y fijar una meta", "Es la revisión posterior."),
    ],
    [
        (TRANS + " ¿Cuántos rellenos de tiempo aparecen? A) 2 B) 4", "A) 2", "Aparecen Well y let me think."),
        (TRANS + " ¿Qué conectores usó para unir ideas? A) but y so B) because y then", "A) but y so", "Dice but I was tired, so I went home."),
        (TRANS + " ¿Qué palabra recuperó? A) bench B) park", "A) bench", "Dijo Yes, the bench."),
    ],
    [
        ("Después de hablar notas que dijiste «She go to school». ¿Qué registras? A) She goes to school (con she el verbo lleva s) B) She go to school (está bien)", "A) She goes to school (con she el verbo lleva s)", "Se anota el error y la forma correcta."),
        ("Quieres mejorar tu fluidez. ¿Qué plan completo es mejor? A) diagrama, ensayo, rellenos en la presentación y registro de errores B) leer el texto una vez y no revisar", "A) diagrama, ensayo, rellenos en la presentación y registro de errores", "Cubre antes, durante y después."),
        ("Olvidaste la palabra wallet (billetera). ¿Qué frase te ayuda? A) It's the small thing for money and cards. B) It's an animal.", "A) It's the small thing for money and cards.", "Describe función y uso."),
    ],
    [
        ("Tienes dos intentos de la misma presentación. En el primero usaste 0 rellenos y en el segundo 2. ¿Qué cambió? A) ganó fluidez con rellenos B) disminuyó la fluidez", "A) ganó fluidez con rellenos", "Los rellenos dieron tiempo para pensar."),
        ("Registras «I made a plan» y «I make a plan yesterday». ¿Cuál necesita corrección? A) I make a plan yesterday B) I made a plan", "A) I make a plan yesterday", "Con yesterday el verbo va en pasado: made."),
    ],
    [
        ("Tu meta fue «use the past tense of go». En tu segundo intento dijiste «I went, I saw and I ate». ¿Cumpliste la meta? A) sí: usaste went en pasado B) no: no usaste ningún pasado", "A) sí: usaste went en pasado", "Went es el pasado de go."),
        ("Un compañero te ve nervioso y te sugiere respirar y hacer una pausa antes de hablar. ¿Qué momento del ciclo es? A) antes de hablar B) después de hablar", "A) antes de hablar", "Es una preparación."),
    ],
    [("Ensayas con una persona de tu casa y te dice «You said 'I am agree'». ¿Qué paso del ciclo sigue? A) registrar el error, corregirlo a I agree y fijar una meta B) ignorarlo", "A) registrar el error, corregirlo a I agree y fijar una meta", "Es la revisión posterior.")],
    [
        ("En Inglés de 1.º medio (OA 6, clase 5): ¿en qué momentos se usan las estrategias?", "Antes, durante y después de hablar", "Es un ciclo."),
        ("En Inglés de 1.º medio (OA 6, clase 5): ¿qué haces si olvidas una palabra?", "La describo con otras palabras", "Mantiene la comunicación."),
        ("En Inglés de 1.º medio (OA 6, clase 5): ¿cómo se ve el progreso?", "Comparando dos intentos", "Se nota qué mejoró."),
    ],
    task("Habla un minuto en voz alta sobre «A place I like in my city or town». Antes, haz un diagrama con tres ramas. Durante la conversación usa al menos un relleno, un conector y una descripción si olvidas una palabra. Después anota una fortaleza, un error con su forma correcta y una meta, con ayuda de una persona de tu casa.", "Diagrama: park, trees, football. Habla: Well, I like the park because it has many trees... the thing for sitting, the bench. Fortaleza: conectores claros. Error: I go yesterday → I went. Meta: use past tense with yesterday.", ["hace un diagrama antes", "usa relleno, conector y descripción al hablar", "registra fortaleza, error y meta después"], ["hoja con el diagrama y la revisión", "nota de la persona oyente"], ["no registrar ningún error", "meta demasiado general"], "Reconoce las estrategias usadas en cada momento y ayuda a hacer concreta la meta."),
    "Repite el ciclo con otro tema y compara con tu primer intento.",
    "Explica a otra persona, en español, qué estrategia usarías en cada momento: antes, durante y después de hablar.",
)

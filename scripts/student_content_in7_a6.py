"""Cuaderno del estudiante, 7.º básico Inglés (oficial), IN07 OA 06 (estrategias para expresarse con claridad y fluidez:
antes, durante y después de hablar). Los diálogos y errores de ejemplo están escritos en cada enunciado.
"""
from __future__ import annotations

from student_content_in7_a import lesson, task
from student_lessons import arith

OA6 = "IN07 OA 06"
MAT = "Los diálogos y frases escritos en cada ejercicio, lápiz y, para practicar en voz alta, una persona de tu casa que te escuche."

D1 = "«Teacher: Please open your book at page forty-six. Student: Sorry, could you speak more slowly? Teacher: Of course. Please open your book at page forty-six. Student: Page forty-six? Thank you.» (page = página, slowly = más despacio, open = abrir)"
D2 = "«Visitor: How do I get to the museum? Guide: Take bus 21 and get off at the last stop. Visitor: Do you mean the stop near the river? Guide: Yes, exactly.» (get off = bajarse, last stop = última parada, near = cerca de, exactly = exacto)"
OFF = "«Yesterday I goed to the park with my friend. We play football and I am very tired.» (yesterday = ayer, tired = cansado)"

# ------------------------------------------------------------------ clase 1
lesson(
    OA6, 1, MAT,
    "Aprenderé a prepararme antes de hablar: practicar en voz alta, predecir el vocabulario y las expresiones frecuentes (chunks) que necesitaré y preparar un apoyo escrito. Sirve para hablar con más seguridad.",
    ["Sé qué es un chunk.", "Conozco palabras como excuse me, library y club."],
    [
        "Antes de hablar, la preparación marca la diferencia. Primero, predice la situación y el vocabulario: si vas a inscribirte en un club de natación, necesitarás pool (piscina), lesson (clase), swimsuit (traje de baño) y towel (toalla). Segundo, elige los chunks que usarás: I'd like to join the club (me gustaría unirme), How much is it? (¿cuánto cuesta?) y What time is the lesson? (¿a qué hora es la clase?).",
        "Tercero, practica en voz alta, repitiendo cada chunk varias veces hasta que salga sin pensar. La boca se acostumbra a los sonidos, y eso te da fluidez (fluency). Cuarto, prepara un apoyo organizativo y visual: una tarjeta con palabras clave y los chunks, no un texto completo. Con eso en la mano puedes concentrarte en comunicar.",
        "Los chunks de cortesía suenan mejor que las órdenes directas. Could you tell me where the gym is? es más amable que Tell me the gym. Excuse me, al comienzo, llama la atención con respeto. Piensa en la situación, elige tus chunks y repásalos con tu tarjeta: así llegarás a hablar con la mente tranquila.",
    ],
    [("rehearse", "ensayar, practicar en voz alta"), ("chunk", "expresión frecuente que se usa como bloque"), ("fluency", "fluidez: hablar sin interrupciones"), ("join", "unirse a"), ("Could you tell me...?", "¿Podría decirme...? (cortés)"), ("I'd like to...", "Me gustaría...")],
    [
        ("Predecir vocabulario", "Vas a inscribirte en un club de natación. ¿Qué palabras predices: pool, lesson, swimsuit o oven, bowl, spoon?", ["Pienso en la situación: un club de natación.", "Pool, lesson y swimsuit se relacionan con nadar.", "Oven, bowl y spoon son de cocina."], "pool, lesson, swimsuit"),
        ("Elegir chunks", "Quieres preguntar por el precio de la inscripción. ¿Qué chunk preparas?", ["Busco un chunk de precio.", "How much is it? pregunta cuánto cuesta.", "Es la frase indicada."], "How much is it?"),
    ],
    [
        ("Preparar un texto completo y leerlo.", "Se pierde la naturalidad y el contacto con quien escucha.", "Prepara solo palabras clave y chunks."),
        ("No ensayar en voz alta.", "La boca no se entrena y aparecen dudas.", "Repite cada chunk en voz alta."),
    ],
    [
        ("Quieres preguntar cómo llegar a la biblioteca. ¿Qué chunk eliges? a) Could you tell me how to get to the library? b) The library is big.", "a) Could you tell me how to get to the library?", "Es una pregunta cortés sobre cómo llegar."),
        ("¿Qué significa «I'd like to join the club»?", "Me gustaría unirme al club", "I'd like to es me gustaría."),
        ("¿Qué chunk sirve para preguntar el precio?", "How much is it?", "Pregunta cuánto cuesta."),
    ],
    [
        ("¿Qué lista predice vocabulario para inscribirte en un club de natación? a) pool, lesson, swimsuit b) oven, bowl, spoon", "a) pool, lesson, swimsuit", "Son palabras de natación."),
        ("Ordena los pasos para prepararte. A) Practicar los chunks en voz alta. B) Predecir la situación y el vocabulario. C) Elegir los chunks que usarás.", "B, C, A", "Primero predices, luego eliges los chunks y por último los practicas."),
        ("¿Cuál chunk usas para llamar la atención con respeto? a) Excuse me b) Give me", "a) Excuse me", "Excuse me es cortés."),
    ],
    [
        ("Completa: «___ you tell me where the gym is?» Escribe la palabra que da sentido a la pregunta cortés (Could / Tell).", "Could", "Could you tell me... es una pregunta educada."),
        ("¿Qué frase pide permiso para unirte? a) Can I join the club? b) The club is big.", "a) Can I join the club?", "Can I... pide permiso."),
        ("¿Qué debe llevar una tarjeta de apoyo? a) palabras clave y chunks b) el texto completo", "a) palabras clave y chunks", "Un apoyo breve evita leer."),
    ],
    [
        ("¿Por qué repetir los chunks en voz alta antes de hablar? a) porque la boca se acostumbra y hablas con más fluidez b) porque así no necesitas escuchar", "a) porque la boca se acostumbra y hablas con más fluidez", "La práctica entrena la pronunciación."),
        ("Dos estudiantes preparan chunks: uno prepara «Could you tell me...?» y otro «Tell me!». ¿Cuál suena más cortés?", "Could you tell me...?", "Could you es una pregunta amable; Tell me! es una orden."),
    ],
    [
        arith("Practicas cada chunk 3 veces al día durante 4 días. ¿Cuántas veces lo practicas en total?", "3*4", "Se multiplican las veces diarias por los días.", " veces"),
        ("Ordena el turno. A) Thank you very much. B) Excuse me. C) Could you tell me where the gym is?", "B, C, A", "Primero se llama la atención, luego se pregunta y al final se agradece."),
    ],
    [("Mañana preguntarás en la biblioteca si puedes llevarte un libro por dos semanas. ¿Qué chunk preparas? a) Can I borrow this book for two weeks? b) I borrow book two.", "a) Can I borrow this book for two weeks?", "Es una pregunta completa y correcta.")],
    [
        ("¿Qué haces antes de hablar para estar preparado?", "Predigo vocabulario, elijo chunks y practico en voz alta", "La preparación da fluidez."),
        ("¿Qué significa «How much is it?»", "¿Cuánto cuesta?", "Pregunta por el precio."),
        ("¿Qué apoyo escrito conviene?", "Una tarjeta con palabras clave", "Evita leer un texto completo."),
    ],
    task("Imagina que quieres inscribirte en un club de teatro del colegio. En tu hoja escribe tres chunks en inglés que usarías (uno para llamar la atención, uno para preguntar el horario y uno para agradecer) y tres palabras de vocabulario que predices. Practica los chunks en voz alta tres veces con una persona de tu casa.", "Excuse me; What time is the class?; Thank you very much. Vocabulario: stage, actor, costume.", ["tres chunks adecuados a la situación", "tres palabras predichas", "practica en voz alta"], ["hoja con los chunks", "nota de la persona que escuchó"], ["elegir chunks sin relación con la situación", "no practicar en voz alta"], "Reconoce lo que acertó y ayuda a elegir un chunk más cortés si hace falta."),
    "Repite en voz alta cinco veces cada chunk de la tarjeta, cada vez un poco más rápido, sin perder claridad.",
    "Prepara otra tarjeta para una situación distinta, como pedir ayuda en una tienda.",
)

# ------------------------------------------------------------------ clase 2
lesson(
    OA6, 2, MAT,
    "Aprenderé a abrir mi turno de habla y a mantenerlo usando rellenos temporales (well, okay, so), conectores y gestos. Sirve para ganar tiempo para pensar y seguir hablando con naturalidad.",
    ["Sé preparar chunks antes de hablar.", "Conozco because, but y and."],
    [
        "Hablar con fluidez no significa hablar rápido, sino no quedarse en silencio. Los rellenos temporales (fillers) son palabras cortas que te dan un segundo para pensar: well... (bueno...), okay, so... (entonces...), let me think (déjame pensar). Se usan al comienzo o entre ideas, pero no hay que abusar: si pones well en cada frase, cansas a quien te escucha.",
        "Para mantener el turno, usa conectores que prolongan tu idea. Because agrega una razón: I like football because it is a team sport. But marca un contraste: I like skating, but I am afraid of falling. And agrega otra idea. Con un conector siempre tienes por dónde seguir. También ayudan los gestos: levantar un dedo muestra que quieres hablar y que aún no terminas.",
        "Para abrir un turno puedes usar Excuse me, can I say something? o I think that... Para cerrarlo, un gesto o una frase como That's all, thank you. Pregúntate antes de hablar: ¿cuál es mi idea?, ¿qué razón puedo agregar? y ¿cuál conector uso? Así tu turno tendrá al menos dos frases en vez de un simple «yes».",
    ],
    [("filler", "relleno: palabra que da tiempo para pensar"), ("well / so / okay", "bueno / entonces / está bien"), ("turn", "turno de habla"), ("because", "porque"), ("but", "pero"), ("let me think", "déjame pensar")],
    [
        ("Usar un relleno", "A: What do you do on weekends? B: «Well... I usually play football with my cousins.» ¿Para qué usa B la palabra well?", ["Well aparece al comienzo de la respuesta.", "B todavía no dice la idea.", "Gana un segundo para pensar."], "Para ganar tiempo para pensar"),
        ("Agregar una razón", "Completa con un conector: «I like football ___ it is a team sport.» (because / but)", ["Después del espacio viene una razón.", "La razón de que le guste es que es un deporte de equipo.", "El conector es because."], "because"),
    ],
    [
        ("Repetir well en cada frase.", "Se abusa del relleno y se pierde claridad.", "Usa un relleno al comenzar y avanza con conectores."),
        ("Responder con una sola palabra.", "Se corta el turno y no se comunica la idea.", "Agrega una razón con because."),
    ],
    [
        ("¿Para qué sirve «well...»? a) para ganar tiempo mientras piensas b) para despedirse", "a) para ganar tiempo mientras piensas", "Es un relleno temporal."),
        ("En Inglés de 7.º (OA 6, clase 2): ¿Qué significa «Let me think»?", "Déjame pensar", "Se usa para pedir tiempo."),
        ("¿Qué conector agrega una razón?", "because", "Because significa porque."),
    ],
    [
        ("¿Cuál frase continúa mejor «I like football because ___»? a) it is a team sport b) yesterday", "a) it is a team sport", "Después de because va una razón."),
        ("Completa con un conector: «I like skating, ___ I am afraid of falling.» (because / but). Escribe el que marca contraste.", "but", "Hay una idea que se opone a otra."),
        ("¿Qué gesto muestra que quieres hablar? a) levantar un dedo b) cruzar los brazos", "a) levantar un dedo", "Es un gesto común para pedir turno."),
    ],
    [
        ("Ordena. A) Well... B) I think the park is nice C) because it has big trees", "A, B, C", "Relleno, idea y razón."),
        ("¿Qué respuesta mantiene mejor el turno ante «What is your favorite food?»? a) Well... I like pasta because it is tasty. b) Yes.", "a) Well... I like pasta because it is tasty.", "Es una respuesta completa con razón."),
        ("Une las ideas con because: «I like winter. I like snow.» Escribe la oración completa.", "I like winter because I like snow.", "Because introduce la razón."),
    ],
    [
        ("Si repites well en cada frase, ¿mejora tu respuesta? Responde sí o no.", "No", "El relleno sirve para ganar tiempo, no para llenar toda la respuesta."),
        ("Ante «Do you like reading?», ¿qué respuesta es mejor? a) Yes, I do, because stories are exciting. b) Yes.", "a) Yes, I do, because stories are exciting.", "Agrega una razón y sostiene el turno."),
    ],
    [
        arith("Tienes 60 segundos para tu turno. Usas 15 segundos en pausas y rellenos. ¿Cuántos segundos quedan para tus ideas?", "60-15", "Se resta el tiempo de rellenos al total.", " segundos"),
        ("«I like winter, but I do not like rain.» ¿Qué conector marca el contraste?", "but", "But opone dos ideas."),
    ],
    [("En la entrevista del club te dicen «Tell us about your hobby» y tu mente queda en blanco. ¿Qué dices para ganar tiempo? a) Well... let me think. b) I have no hobby.", "a) Well... let me think.", "Es un relleno que da tiempo sin cortar la comunicación.")],
    [
        ("¿Qué son los rellenos temporales?", "Palabras cortas que dan tiempo para pensar", "Ejemplos: well, okay, so."),
        ("¿Qué conector marca un contraste?", "But", "Opone dos ideas."),
        ("¿Cuántas frases debería tener un buen turno?", "Al menos dos", "Una idea y una razón."),
    ],
    task("Practica con una persona de tu casa este mini diálogo. Ella pregunta: «What is your favorite sport?». Tú respondes con un relleno, una idea y una razón con because. Escribe tu respuesta y repítela en voz alta dos veces.", "Well... I like swimming because it is relaxing.", ["usa un relleno temporal", "da una idea", "agrega una razón con because"], ["hoja con la respuesta", "nota de la persona que escuchó"], ["responder solo con una palabra", "repetir well varias veces"], "Reconoce lo que acertó y ayuda a mejorar la razón si es poco clara."),
    "Responde en voz alta dos preguntas simples usando siempre un relleno al comienzo y un because.",
    "Escribe una respuesta de tres frases a «Tell me about your best friend» usando well, but y because.",
)

# ------------------------------------------------------------------ clase 3
lesson(
    OA6, 3, MAT,
    "Aprenderé a pedir aclaraciones y ayuda cuando no entiendo, usando frases como Sorry, could you repeat that? Sirve para no quedarme sin entender y para mantener la conversación.",
    ["Sé usar Excuse me y Thank you.", "Conozco palabras como page, bus y museum."],
    [
        "Pedir aclaración (clarification) es una estrategia de buenos hablantes. Algunas frases útiles: Sorry, could you repeat that? (¿puede repetir?), Could you speak more slowly? (¿puede hablar más despacio?), What does '...' mean? (¿qué significa '...'?), How do you say '...' in English? (¿cómo se dice '...' en inglés?) y Do you mean...? (¿quiere decir...?).",
        "Cada frase tiene un propósito. Para un dato que no oíste, pide repetir. Para una palabra que no conoces, pregunta qué significa. Para confirmar que entendiste, repite lo que oíste con tono de pregunta: Page forty-six? Si crees que entendiste pero quieres estar seguro, usa Do you mean the stop near the river?",
        "Pedir ayuda no es un fracaso. Los hablantes nativos también piden repetir. Lo que sí complica es quedarse en silencio sin entender. Usa un tono amable, con Sorry o Excuse me al comienzo, y mira a la persona. Después de recibir la ayuda, agradece con Thank you y continúa la conversación.",
    ],
    [("repeat", "repetir"), ("slowly", "despacio"), ("What does ... mean?", "¿Qué significa ...?"), ("How do you say ... in English?", "¿Cómo se dice ... en inglés?"), ("Do you mean ...?", "¿Quiere decir ...?"), ("clarification", "aclaración")],
    [
        ("Pedir que hablen más despacio", D1 + " ¿Qué pide el estudiante?", ["Busco Sorry, could you speak more slowly?", "Slowly significa despacio.", "Pide que la profesora hable más despacio."], "Que hable más despacio"),
        ("Confirmar lo entendido", D2 + " ¿Qué verifica el visitante con «Do you mean the stop near the river?»", ["Do you mean... confirma una idea.", "Pregunta por la parada cerca del río.", "Quiere asegurarse de que entendió bien."], "Que la última parada es la que está cerca del río"),
    ],
    [
        ("Quedarse en silencio sin entender.", "Se pierde la conversación y no se aprende.", "Usa Sorry, could you repeat that?"),
        ("Pedir ayuda sin ser cortés.", "Se omite Sorry o Excuse me.", "Comienza con una palabra amable."),
    ],
    [
        (D1 + " ¿Qué pide el estudiante? a) que hable más despacio b) que cambie de página", "a) que hable más despacio", "Dice could you speak more slowly."),
        (D1 + " ¿Qué número de página dice la profesora?", "46", "La profesora dice forty-six."),
        (D2 + " ¿Qué número de bus debe tomar el visitante?", "21", "Dice Take bus 21."),
    ],
    [
        (D2 + " ¿Qué frase sirve para preguntar el significado de «last stop»? a) What does 'last stop' mean? b) How are you?", "a) What does 'last stop' mean?", "What does... mean? pregunta por el significado."),
        ("¿Qué frase usas para preguntar cómo se dice «paradero» en inglés?", "How do you say 'paradero' in English?", "Es la frase que pide una palabra."),
        (D1 + " Cuando el estudiante repite «Page forty-six?», ¿qué hace? a) confirma lo que entendió b) se despide", "a) confirma lo que entendió", "Repetir con tono de pregunta confirma el dato."),
    ],
    [
        ("Completa: «Sorry, ___ you repeat that?» Escribe la palabra (could / are).", "could", "Could you repeat that? es una petición educada."),
        (D2 + " No entendiste el número de bus. ¿Qué dices? a) Sorry, which number? b) Thank you, goodbye.", "a) Sorry, which number?", "Pide el dato que faltó."),
        ("Ordena. A) Take bus 21 and get off at the last stop. B) Sorry, what does 'get off' mean? C) It means 'leave the bus'.", "A, B, C", "Primero la indicación, luego la pregunta y la respuesta."),
    ],
    [
        ("¿Pedir una aclaración es señal de que lo haces mal? Responde sí o no.", "No", "Es una estrategia que usan también los hablantes expertos."),
        (D1 + " ¿Para qué repite el estudiante «Page forty-six?»? a) para asegurarse de que entendió b) para pedir otro libro", "a) para asegurarse de que entendió", "Confirma el dato."),
    ],
    [
        arith("El bus pasa cada 15 minutos. Llegas 5 minutos después de que pasó uno. ¿Cuántos minutos esperas hasta el siguiente?", "15-5", "Al ciclo de 15 minutos se le restan los 5 que ya pasaron.", " minutos"),
        ("¿Qué frase se usa para saber si entendiste bien la idea de otra persona? a) Do you mean...? b) See you later.", "a) Do you mean...?", "Do you mean... confirma una interpretación."),
    ],
    [("En una tienda no estás seguro del precio: oíste «twenty» o «twelve». ¿Qué dices para confirmar? a) Sorry, did you say twelve or twenty? b) I do not like this shop.", "a) Sorry, did you say twelve or twenty?", "Ofrece las dos opciones para verificar.")],
    [
        ("¿Qué frase pide repetir?", "Sorry, could you repeat that?", "Es una petición amable."),
        ("¿Qué significa «What does ... mean?»", "¿Qué significa ...?", "Pregunta por el significado."),
        ("¿Qué haces después de recibir ayuda?", "Agradezco y continúo", "Se mantiene la conversación."),
    ],
    task("Lee este diálogo a una persona de tu casa y completa los espacios con frases de clarificación: «A: The film starts at nineteen thirty. B: ___ (pedir que repita la hora). A: Nineteen thirty, that is half past seven in the evening. B: ___ (preguntar qué significa half past).» Después, represéntalo en voz alta.", "B: Sorry, could you repeat the time? B: What does 'half past' mean?", ["completa los dos espacios", "usa frases cortés", "lo representa en voz alta"], ["hoja con las frases", "nota de la persona que escuchó"], ["no usar Sorry", "responder sin pedir aclaración"], "Reconoce las frases correctas y repasa con la persona de tu casa cuándo usar cada una."),
    "Practica en voz alta las cinco frases de clarificación y usa una en cada conversación breve que tengas.",
    "Escribe otro diálogo de cuatro líneas en que una persona pide repetir y otra explica una palabra.",
)

# ------------------------------------------------------------------ clase 4
lesson(
    OA6, 4, MAT,
    "Aprenderé a parafrasear, usar sinónimos y gestos cuando no sé una palabra. Sirve para seguir comunicándome sin detenerme.",
    ["Sé pedir ayuda cuando no entiendo.", "Conozco palabras como big, small, fast y shop."],
    [
        "A veces no recuerdas la palabra exacta. En vez de quedarte en silencio, puedes parafrasear (paraphrase), es decir, explicar la idea con otras palabras. Por ejemplo, si no sabes bakery, dices: It's a shop where you buy bread. Si no sabes umbrella, dices: It's a thing you open when it rains. Basta con decir para qué sirve, dónde está o cómo es.",
        "También puedes usar sinónimos (synonyms), que son palabras con significado parecido: big y large, small y little, fast y quick, start y begin, kid y child. Si olvidas una, usa la otra. Los gestos ayudan mucho: abrir los brazos muestra algo grande, mover las manos muestra un movimiento y señalar un objeto evita nombrarlo.",
        "Mientras explicas, usa frases como It's like... (es como...), It's a place where... (es un lugar donde...) o It's a thing you use to... (es una cosa que se usa para...). Es mejor una explicación sencilla que un silencio largo. Y si la otra persona te ayuda con la palabra, repítela para recordarla la próxima vez.",
    ],
    [("paraphrase", "parafrasear: decir lo mismo con otras palabras"), ("synonym", "sinónimo: palabra de significado parecido"), ("gesture", "gesto"), ("It's a place where...", "es un lugar donde..."), ("It's a thing you use to...", "es una cosa que se usa para..."), ("big / large", "grande")],
    [
        ("Sinónimo", "¿Qué sinónimo tiene big?", ["Big significa grande.", "Otra palabra para grande es large.", "Las dos sirven."], "large"),
        ("Parafrasear", "Olvidaste la palabra umbrella. ¿Qué dices para explicarla?", ["Pienso para qué sirve.", "Sirve cuando llueve y se abre.", "It's a thing you open when it rains."], "It's a thing you open when it rains"),
    ],
    [
        ("Quedarse en silencio por no saber una palabra.", "Se interrumpe la comunicación.", "Explica la idea con otras palabras."),
        ("Usar un sinónimo que no calza con el sentido.", "Los sinónimos no siempre se pueden cambiar en todo contexto.", "Verifica que signifique lo mismo en tu frase."),
    ],
    [
        ("¿Qué sinónimo tiene start? a) begin b) stop", "a) begin", "Start y begin significan comenzar."),
        ("Olvidaste umbrella. ¿Qué explicación sirve? a) It's a thing you open when it rains. b) It's a thing you wear on your feet.", "a) It's a thing you open when it rains.", "Explica para qué se usa."),
        ("¿Qué sinónimo tiene little?", "small", "Little y small significan pequeño."),
    ],
    [
        ("Olvidaste bakery. ¿Qué dices? a) It's a shop where you buy bread. b) It's a panadería.", "a) It's a shop where you buy bread.", "Explica qué es y para qué sirve."),
        ("¿Qué gesto sirve para mostrar algo grande? a) abrir los brazos b) cerrar la mano", "a) abrir los brazos", "El gesto muestra tamaño."),
        ("¿Cuál palabra es sinónimo de quick? a) fast b) slow", "a) fast", "Quick y fast significan rápido."),
    ],
    [
        ("Elige la mejor explicación de backpack. a) a bag you carry on your back for school b) a small box for pencils", "a) a bag you carry on your back for school", "Dice qué es y para qué sirve."),
        ("¿Cuál palabra es sinónimo de kid? a) child b) teacher", "a) child", "Kid y child significan niño."),
        ("Olvidaste el verbo begin. ¿Qué puedes decir? a) start b) finish", "a) start", "Start es sinónimo de begin."),
    ],
    [
        ("¿Por qué parafrasear ayuda? a) porque permite seguir hablando aunque falte una palabra b) porque cambia el tema", "a) porque permite seguir hablando aunque falte una palabra", "Mantiene la comunicación."),
        ("Un compañero se detiene porque no sabe bakery. ¿Cuál es la mejor opción? a) parafrasear y continuar b) esperar en silencio", "a) parafrasear y continuar", "Evita perder el hilo."),
    ],
    [
        ("Elige la mejor explicación de fridge sin decir la palabra. a) A cold machine in the kitchen where we keep milk. b) A hot place where we cook.", "a) A cold machine in the kitchen where we keep milk.", "Describe función y lugar."),
        ("Entre big–large, small–tiny, fast–slow y start–begin, ¿cuántos pares son sinónimos?", "3", "Fast y slow son opuestos; los otros tres son sinónimos."),
    ],
    [("En una tienda de bicicletas no sabes decir helmet. ¿Qué dices? a) I need something to protect my head when I ride a bike. b) I need a thing to clean my bike.", "a) I need something to protect my head when I ride a bike.", "Explica para qué sirve el objeto.")],
    [
        ("En Inglés de 7.º (OA 6, clase 4): ¿Qué es parafrasear?", "Decir lo mismo con otras palabras", "Mantiene la comunicación."),
        ("En Inglés de 7.º (OA 6, clase 4): ¿Qué es un sinónimo?", "Una palabra de significado parecido", "Por ejemplo, big y large."),
        ("¿Qué frase sirve para explicar un lugar?", "It's a place where...", "Describe un lugar por su función."),
    ],
    task("Explica en inglés, sin decir la palabra, tres objetos: un lápiz, una puerta y un reloj. Usa It's a thing you use to... o It's a place where... y un gesto. Pide a una persona de tu casa que adivine cuál es cada uno.", "It's a thing you use to write. It's a thing you open to enter a room. It's a thing that shows the time.", ["explica tres objetos", "usa una frase de paráfrasis", "usa un gesto"], ["hoja con las tres explicaciones", "nota de la persona que adivinó"], ["decir la palabra directamente", "no explicar para qué sirve"], "Reconoce las explicaciones claras y practica con la persona de tu casa una que fue difícil de adivinar."),
    "Juega a explicar objetos de la casa sin decir su nombre, usando solo gestos y frases en inglés.",
    "Escribe cinco pares de sinónimos en inglés y úsalos en frases.",
)

# ------------------------------------------------------------------ clase 5
lesson(
    OA6, 5, MAT,
    "Aprenderé a registrar mis errores después de hablar y a corregirlos con ayuda del docente y recursos. Sirve para mejorar con cada conversación.",
    ["Sé usar rellenos, conectores y paráfrasis.", "Conozco el pasado went de go y played de play."],
    [
        "Después de hablar viene una etapa muy valiosa: revisar lo que dijiste. Anota tus errores en un registro (error log) con tres columnas: lo que dije, la corrección y la regla. Revisa con tu docente o con un recurso, como un diccionario o tu cuaderno. Corregir no significa que seas malo en inglés: significa que estás aprendiendo.",
        "Algunos errores frecuentes: go es irregular y su pasado es went, no goed. Los verbos regulares forman el pasado con -ed: play, played. En presente, con he, she o it, el auxiliar es doesn't, no don't, y el verbo have cambia a has: She doesn't like fish. He has a dog. También se dice I agree, no I am agree. Cada regla se aprende mejor con un ejemplo que tú mismo escribes.",
        "Mientras hablas, también puedes corregirte con frases de reparación: I mean... (quiero decir...), Sorry, let me say that again (perdón, lo digo otra vez). Eso muestra que te escuchas. Al final de cada conversación, escoge uno o dos errores y propónte decir la forma correcta la próxima vez.",
    ],
    [("error log", "registro de errores"), ("correct", "corregir"), ("I mean...", "quiero decir..."), ("went", "pasado de go"), ("doesn't", "no (con he, she, it)"), ("rule", "regla")],
    [
        ("Corregir un pasado irregular", "Corrige la frase: «Yesterday I goed to the park.»", ["Go es un verbo irregular.", "Su pasado es went.", "La frase correcta es I went to the park."], "Yesterday I went to the park"),
        ("Corregir con he, she o it", "Corrige: «She don't like fish.»", ["She es tercera persona.", "Con she se usa doesn't.", "She doesn't like fish."], "She doesn't like fish"),
    ],
    [
        ("Ignorar los errores después de hablar.", "No se aprende de ellos.", "Anota cada error en un registro."),
        ("Anotar el error pero no la corrección.", "El registro no sirve para mejorar.", "Escribe siempre qué dijiste y cómo se corrige."),
    ],
    [
        ("Corrige: «Yesterday I goed to the park.»", "Yesterday I went to the park.", "Go es irregular y su pasado es went."),
        ("Corrige: «She don't like fish.»", "She doesn't like fish.", "Con she se usa doesn't."),
        ("¿Qué frase usas para corregirte mientras hablas? a) Sorry, I mean... b) See you later.", "a) Sorry, I mean...", "Sorry, I mean... repara lo dicho."),
    ],
    [
        ("¿Qué tipo de error es «I am agree»? a) de gramática b) de pronunciación", "a) de gramática", "Se dice I agree, sin am."),
        ("Corrige: «He have a dog.»", "He has a dog.", "Con he se usa has."),
        ("¿Dónde conviene anotar los errores después de hablar? a) en un registro con corrección b) en ningún lugar", "a) en un registro con corrección", "Permite revisarlos luego."),
    ],
    [
        ("Corrige: «We play football yesterday.»", "We played football yesterday.", "Con yesterday se usa el pasado: play se convierte en played."),
        ("¿Cuántos errores hay en «Yesterday I goed to the park and we play football»?", "2", "Hay goed en vez de went y play en vez de played."),
        ("En un registro de errores, ¿qué tres columnas conviene tener? a) lo que dije, la corrección y la regla b) fecha, hora y lugar", "a) lo que dije, la corrección y la regla", "Así se aprende la regla."),
    ],
    [
        ("¿Por qué conviene anotar los errores después de hablar? a) para corregirlos con ayuda del docente y recursos b) para olvidarlos", "a) para corregirlos con ayuda del docente y recursos", "Corregir permite mejorar."),
        ("Un diccionario y tu cuaderno de reglas, ¿sirven para corregir? Responde sí o no.", "Sí", "Son recursos de apoyo."),
    ],
    [
        ("Corrige las dos partes: «My brother don't play and he have a bike.»", "My brother doesn't play and he has a bike.", "Se corrigen don't por doesn't y have por has."),
        ("¿Cuántos errores hay en «She don't like cats. I am agree. He have a car.»?", "3", "Son don't, am agree y have."),
    ],
    [("Después de hablar con tu profesor anotas «I am agree». ¿Cómo lo corriges?", "I agree.", "El verbo agree no lleva am.")],
    [
        ("¿Qué haces después de hablar?", "Registro mis errores y los corrijo", "Así mejoro mi inglés poco a poco."),
        ("¿Qué significa «I mean...»?", "Quiero decir...", "Sirve para corregirte."),
        ("¿Cuál es el pasado de go?", "went", "Go es un verbo irregular."),
    ],
    task("Lee esta pequeña conversación y escribe en un registro de errores tres columnas (lo que dije, corrección, regla): «My sister don't like soup. Yesterday we goed to the market. I am agree with her.» Revisa con una persona de tu casa y úsenlas para practicar las frases correctas en voz alta.", "Don't → doesn't (con she/he/it). Goed → went (pasado irregular). I am agree → I agree.", ["anota los tres errores", "escribe la corrección de cada uno", "indica la regla"], ["registro con tres columnas", "nota de la persona que revisó"], ["no escribir la regla", "olvidar un error"], "Reconoce las correcciones acertadas y practica las frases correctas en voz alta."),
    "Lee en voz alta las tres frases corregidas dos veces cada una.",
    "Después de tu próxima conversación en inglés, anota dos errores y su corrección en un registro.",
)

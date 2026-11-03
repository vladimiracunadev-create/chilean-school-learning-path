"""Cuaderno del estudiante, 8.º básico Inglés (propuesta), EN08 OA 01 (textos orales en distintos formatos).

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Los textos son originales (incluida la canción de la clase 5) y llevan pista en español.
Los títulos de las clases del plan son genéricos; aquí cada clase recorre un grupo de formatos que nombra el OA.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1 = "EN08 OA 01"
ADULT = "Un adulto lee en voz alta (tapa el guion): "


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


# ---------------------------------------------------------------- clase 1: narraciones y anécdotas
SNOW = "«Last winter, my brother and I built a snowman in front of our house. We used a carrot for the nose and two black buttons for the eyes. Then we took a photo. In the afternoon the sun came out, and the snowman melted. We were sad, but we still had the photo.» (last winter = el invierno pasado, built = construimos, snowman = muñeco de nieve, carrot = zanahoria, buttons = botones, melted = se derritió, still = todavía)"
TURTLE = "«Once upon a time, a small turtle lived near a river. Every day she watched the fast rabbits and wished to be fast too. One day a flood came, and the rabbits could not cross the water. The turtle swam across with a rope. The rabbits held the rope and crossed. Now the rabbits respect her.» (once upon a time = érase una vez, turtle = tortuga, rabbits = conejos, flood = crecida del río, swam = nadó, rope = cuerda, held = sostuvieron, respect = respetan)"
LUNCH = "«Last Friday, I forgot my lunch box on the school bus. My classmate Fernanda shared her sandwich with me. Today I brought two sandwiches, one for her. I think small kind acts are important.» (forgot = olvidé, lunch box = lonchera, shared = compartió, brought = traje, kind acts = gestos amables)"
MARKER = "«Last Monday, my little sister painted the wall of her room with a red marker. My father laughed first. Then we cleaned the wall together, and she promised never to do it again.» (painted = pintó, wall = pared, marker = plumón, laughed = se rió, cleaned = limpiamos, promised = prometió)"

lesson(
    OA1, 1,
    "Las narraciones y anécdotas escritas en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a distinguir una narración inventada de una anécdota real y a reconocer su propósito y su contexto (quién cuenta, cuándo y para qué). Sirve para entender historias contadas en inglés sin traducir palabra por palabra.",
    ["Sé que el pasado simple (went, took, built) cuenta hechos ya terminados.", "Sé preguntar who, where y when."],
    [
        "Una narración (narrative) cuenta hechos en orden y suele tener personajes, un lugar, un problema y un final. Puede ser inventada, como un cuento que empieza con «Once upon a time». Una anécdota (anecdote) es una historia breve y real que cuenta la misma persona que la vivió; por eso usa I, my y we. Las dos usan el pasado simple: built (construyó), took (tomó), laughed (se rió).",
        "El propósito (purpose) es la razón por la que alguien cuenta algo. Se puede contar para entretener (entertain), para informar (inform) o para dejar una enseñanza (lesson). El contexto es la situación: quién habla, cuándo ocurrió (last winter, last Friday) y dónde. Las pistas de tiempo y las palabras personales te avisan si el texto es real o inventado.",
        "Al escuchar, haz tres preguntas: ¿quién cuenta?, ¿cuándo pasó? y ¿para qué lo cuenta? No necesitas entender cada palabra: nombres, fechas, verbos en pasado y sentimientos (sad, kind) entregan casi todo el significado. En una segunda escucha, completa los detalles que faltan.",
    ],
    [("narrative", "narración: cuenta hechos en orden"), ("anecdote", "anécdota: historia breve y real contada por quien la vivió"), ("purpose", "propósito: para qué se cuenta algo"), ("entertain", "entretener"), ("lesson", "enseñanza que deja una historia"), ("context", "contexto: quién, cuándo y dónde")],
    [
        ("Reconocer una anécdota", ADULT + LUNCH + " ¿Es una anécdota o un cuento inventado? Da una pista.", ["Busco quién habla: dice I y my, o sea que cuenta algo propio.", "Veo la pista de tiempo last Friday, un día real y cercano.", "Esas dos pistas indican un hecho vivido."], "Es una anécdota: la persona cuenta algo que le pasó (I forgot, my classmate)"),
        ("Reconocer el propósito", ADULT + TURTLE + " ¿Para qué se cuenta esta historia?", ["Empieza con Once upon a time, así que es un cuento inventado.", "Hay un problema (la crecida) y una solución (la tortuga y la cuerda).", "Al final los conejos respetan a la tortuga: deja una enseñanza."], "Para entretener y dejar una enseñanza: cada uno tiene una cualidad útil"),
    ],
    [
        ("Creer que toda historia en pasado es una anécdota.", "Se confunde el tiempo verbal con el tipo de texto.", "Revisa si el narrador cuenta algo que vivió (I, my) o si hay un inicio de cuento como Once upon a time."),
        ("Contar todos los detalles en lugar del propósito.", "Se mira cada palabra y se pierde la razón del texto.", "Pregunta primero para qué se cuenta y luego busca dos detalles que lo apoyen."),
    ],
    [
        (ADULT + SNOW + " ¿Qué construyeron los hermanos? a) un muñeco de nieve b) un trineo", "a) un muñeco de nieve", "El guion dice they built a snowman."),
        (ADULT + SNOW + " ¿Qué usaron para la nariz?", "Una zanahoria", "El guion dice a carrot for the nose."),
        ("Un texto empieza con «Once upon a time». ¿Qué es más probable? a) un cuento inventado b) una anécdota personal", "a) un cuento inventado", "Esa frase abre los cuentos de ficción."),
    ],
    [
        (ADULT + TURTLE + " ¿Qué tipo de texto es? a) una narración inventada b) una anécdota real", "a) una narración inventada", "Tiene inicio de cuento, una tortuga y conejos que hablan de respeto."),
        (ADULT + LUNCH + " ¿Qué clave muestra que quien habla vivió la historia? a) usa I y my b) menciona a una compañera de curso", "a) usa I y my", "Esos pronombres muestran que cuenta algo propio."),
        (ADULT + TURTLE + " ¿Cuál es el propósito principal? a) entretener y dejar una enseñanza b) dar instrucciones para cruzar un río", "a) entretener y dejar una enseñanza", "Es un cuento con problema, solución y un cierre que valora a la tortuga."),
    ],
    [
        (ADULT + SNOW + " Ordena los hechos. A) The snowman melted. B) They built the snowman. C) They took a photo. D) They were sad.", "B, C, A, D", "Primero lo construyeron, luego tomaron la foto, después se derritió y al final estaban tristes."),
        (ADULT + LUNCH + " ¿Qué hizo Fernanda? a) compartió su sándwich b) perdió su lonchera", "a) compartió su sándwich", "El guion dice Fernanda shared her sandwich with me."),
        (ADULT + TURTLE + " ¿Cómo cruzaron el río los conejos?", "Sujetando la cuerda que llevó la tortuga", "Dice The rabbits held the rope and crossed."),
    ],
    [
        ("Un compañero dice que la historia de Fernanda es un cuento inventado porque está en pasado. ¿Cuál es la mejor respuesta? a) No: es una anécdota, porque la cuenta quien la vivió y usa I y my b) Sí: todo lo que está en pasado es un cuento", "a) No: es una anécdota, porque la cuenta quien la vivió y usa I y my", "El pasado no basta: importa quién cuenta y qué pistas personales hay."),
        (ADULT + SNOW + " ¿Cuál oración resume mejor la anécdota? a) Los hermanos hicieron un muñeco de nieve que se derritió, pero conservaron una foto. b) Los hermanos viajaron al sur y vieron nevar.", "a) Los hermanos hicieron un muñeco de nieve que se derritió, pero conservaron una foto.", "Une quién, qué pasó y cómo terminó, sin inventar datos."),
    ],
    [
        (ADULT + MARKER + " ¿Qué propósito tiene quien cuenta esta anécdota? Elige: a) entretener contando algo gracioso b) pedir ayuda para pintar una pared c) explicar cómo fabricar un plumón", "a) entretener contando algo gracioso", "Cuenta un hecho familiar con risas y una promesa, no pide ayuda ni explica un proceso."),
        (ADULT + MARKER + " ¿Cuántos verbos distintos en pasado simple hay en el guion?", "4", "Son cuatro verbos distintos en pasado en el guion."),
    ],
    [(ADULT + "«Hi, Sofía. Last summer I visited my grandparents in the countryside. I picked apples with my grandfather and I learned to make jam. It was a lot of fun!» (countryside = campo, picked = recogí, learned = aprendí, jam = mermelada). Una amiga te envía este mensaje de voz. ¿Qué te cuenta? a) una anécdota de sus vacaciones b) instrucciones para viajar", "a) una anécdota de sus vacaciones", "Habla de algo que vivió el verano pasado, con I y my.")],
    [
        ("¿Qué frase abre muchos cuentos inventados en inglés?", "Once upon a time", "Equivale a «érase una vez»."),
        ("¿Quién cuenta una anécdota?", "La persona que vivió la historia", "Por eso suele usar I, my o we."),
        ("¿Qué palabras del guion de la lonchera muestran que ocurrió en un tiempo real y cercano?", "Last Friday y today", "Señalan días concretos, no un tiempo de cuento."),
    ],
    task("Un adulto lee dos veces este texto: «Last Saturday, I helped my neighbor carry his shopping bags. He gave me a fresh bread as a thank-you. I felt happy because I made someone's day easier.» (neighbor = vecino, shopping bags = bolsas de compras, fresh bread = pan fresco, thank-you = agradecimiento). En tu hoja escribe: si es anécdota o cuento inventado, quién cuenta, cuándo pasó y para qué lo cuenta.", "Es una anécdota. Cuenta alguien que vivió el hecho (I helped). Pasó el sábado pasado. Lo cuenta para compartir una experiencia positiva de ayudar.", ["indica correctamente el tipo de texto", "nombra una pista de tiempo y una pista personal", "expresa un propósito coherente con el guion"], ["hoja con cuatro respuestas", "nota del adulto"], ["decir que es un cuento por estar en pasado", "no mencionar ninguna pista del guion"], "Reconoce lo que acertó y relee con la persona solo las palabras I, my y last Saturday para decidir tipo de texto y momento."),
    "Pide a un adulto que lea de nuevo la historia de la tortuga y anota quién, dónde, cuál es el problema y cómo termina.",
    "Escribe en español tres oraciones sobre algo que te pasó el fin de semana pasado y subraya los verbos que irían en pasado en inglés.",
)

# ---------------------------------------------------------------- clase 2: exposiciones orales y noticieros
TALK = "«Good morning, everyone. Today I will talk about the recycling project of our school. First, we put three bins in the yard: blue for paper, yellow for plastic and green for glass. Second, each class chooses a monitor every week. In September we collected one hundred and twenty kilos of paper. Finally, we want to collect two hundred kilos in October.» (recycling = reciclaje, bins = contenedores, yard = patio, monitor = encargado, collected = recolectamos, kilos = kilos)"
NEWS = "«Good evening. This is the six o'clock news. A new bike lane opened today in the center of the city. It is three kilometers long and connects the main square with the university. The mayor said that cyclists must wear helmets. Tomorrow the weather will be cloudy, with light rain in the afternoon.» (news = noticias, bike lane = ciclovía, connects = conecta, main square = plaza principal, mayor = alcalde, cyclists = ciclistas, helmets = cascos, cloudy = nublado, light rain = lluvia ligera)"
LECTURE = "«Today I will explain how a rainbow forms. Sunlight enters a drop of water. The drop separates the light into colors. We see seven colors: red, orange, yellow, green, blue, indigo and violet. To see a rainbow, the sun must be behind you and the rain in front of you.» (rainbow = arcoíris, forms = se forma, drop = gota, separates = separa, behind = detrás, in front of = frente a)"

lesson(
    OA1, 2,
    "Las exposiciones y noticias escritas en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a ubicar la evidencia precisa (cifras, nombres, lugares y pasos) en una exposición oral y en un noticiero. Sirve para responder con datos exactos y no solo con ideas generales.",
    ["Sé los números en inglés hasta las centenas.", "Conozco first, second y finally."],
    [
        "Una exposición oral (oral presentation) es un texto en que una persona explica un tema a un público. Un noticiero (news broadcast) informa hechos recientes. Los dos tienen una estructura: saludo, tema y datos. La idea general (gist) responde «¿de qué trata?». La información específica (specific information) son los datos concretos: cifras, nombres, lugares y horas.",
        "Para encontrar evidencia precisa (precise evidence), escucha con una pregunta en mente y anota solo la palabra que responde. Si preguntan «¿cuántos kilos?», busca un número. Si preguntan «¿dónde?», busca un lugar. En un noticiero, la frase de apertura («This is the six o'clock news») marca el formato, y la noticia principal viene casi siempre primero.",
        "Un dato exacto vale más que una respuesta aproximada. «Seiscientos» no es «seiscientos treinta». Cuando oigas two hundred, anota 200; con one hundred and twenty, anota 120. Compara tu nota con la segunda lectura del guion. Así detectas errores, por ejemplo confundir thirteen (13) con thirty (30).",
    ],
    [("oral presentation", "exposición oral"), ("news broadcast", "noticiero"), ("gist", "idea general"), ("specific information", "información específica: datos exactos"), ("evidence", "evidencia: la palabra o dato que respalda tu respuesta"), ("announcer", "presentador, quien lee las noticias")],
    [
        ("Cifra exacta en una exposición", ADULT + TALK + " ¿Cuántos kilos de papel recolectaron en septiembre?", ["La pregunta pide una cifra, así que busco un número.", "El guion dice one hundred and twenty kilos.", "One hundred and twenty se escribe 120."], "120 kilos"),
        ("Dato de lugar en un noticiero", ADULT + NEWS + " ¿Qué dos lugares conecta la ciclovía?", ["La pregunta pide lugares: busco connects.", "Dice connects the main square with the university.", "Los dos lugares están en esa frase."], "La plaza principal y la universidad"),
    ],
    [
        ("Responder con la idea general cuando se pide un dato exacto.", "Se entiende el tema pero no se busca la palabra que contesta.", "Primero marca qué pide la pregunta (cifra, lugar, nombre) y luego escucha esa palabra."),
        ("Confundir thirteen con thirty.", "Los dos suenan parecido; cambia la sílaba acentuada.", "En thirteen suena fuerte teen al final; en thirty suena fuerte la primera sílaba. Confirma en la segunda escucha."),
    ],
    [
        (ADULT + TALK + " ¿De qué color es el contenedor para el plástico? a) amarillo b) azul", "a) amarillo", "El guion dice yellow for plastic."),
        (ADULT + NEWS + " ¿Qué tipo de texto es? a) un noticiero b) una exposición escolar", "a) un noticiero", "Abre con Good evening, This is the six o'clock news."),
        (ADULT + LECTURE + " ¿Qué fenómeno se explica?", "El arcoíris", "El guion dice how a rainbow forms."),
    ],
    [
        arith(ADULT + TALK + " La meta de octubre es 200 kilos y en septiembre recolectaron 120. ¿Cuántos kilos más necesitan en octubre que en septiembre?", "200-120", "Se resta lo recolectado a la meta."),
        (ADULT + NEWS + " ¿Cuántos kilómetros de largo tiene la ciclovía?", "3", "El guion dice three kilometers long."),
        (ADULT + NEWS + " ¿Qué pronóstico dieron para mañana? a) nublado con lluvia ligera en la tarde b) sol y calor todo el día", "a) nublado con lluvia ligera en la tarde", "El guion dice cloudy, with light rain in the afternoon."),
    ],
    [
        (ADULT + TALK + " ¿Cuántos contenedores pusieron en el patio?", "3", "El guion dice three bins: azul, amarillo y verde."),
        (ADULT + NEWS + " ¿A qué hora es este noticiero? a) a las seis b) a las ocho", "a) a las seis", "Abre con This is the six o'clock news."),
        (ADULT + LECTURE + " ¿Qué hace la gota de agua con la luz del sol? a) la separa en colores b) la apaga", "a) la separa en colores", "El guion dice The drop separates the light into colors."),
    ],
    [
        (ADULT + LECTURE + " ¿Dónde debe estar el sol para ver un arcoíris? a) detrás de quien mira b) frente a quien mira", "a) detrás de quien mira", "El guion dice the sun must be behind you."),
        (ADULT + TALK + " ¿Con cuál frase confirmas que cada curso tiene una tarea fija? Cópiala.", "Each class chooses a monitor every week", "Esa frase dice que cada curso elige un encargado cada semana."),
    ],
    [
        (ADULT + LECTURE + " ¿Cuántos colores se nombran en el guion?", "7", "Son red, orange, yellow, green, blue, indigo y violet."),
        (ADULT + NEWS + " Una vecina dice que la ciclovía mide treinta kilómetros. ¿Qué dato del guion lo corrige?", "Three kilometers long", "El guion dice tres kilómetros, no treinta."),
    ],
    [(ADULT + "«Attention, students. The school fair will be on Thursday, October twelfth, from ten to one, in the main yard. Each class brings one game. Prizes for the three best stands.» (fair = feria, prizes = premios, stands = puestos). ¿De qué hora a qué hora dura la feria? a) de diez a una b) de doce a tres", "a) de diez a una", "El guion dice from ten to one.")],
    [
        ("¿Qué es la información específica?", "Los datos concretos, como cifras, nombres y lugares", "Responde preguntas exactas del texto."),
        ("¿Qué palabra del guion de las noticias muestra que habla un presentador?", "News", "This is the six o'clock news presenta el formato."),
        ("Si la pregunta es «¿cuántos?», ¿qué palabra buscas al escuchar?", "Un número", "La pregunta pide una cantidad."),
    ],
    task("Un adulto lee dos veces este texto: «Good afternoon. Today I will talk about my pet, a dog named Max. Max is five years old and weighs eleven kilos. He eats twice a day and walks forty minutes every afternoon. His favorite game is catching a red ball.» (pet = mascota, weighs = pesa, twice = dos veces, walks = pasea, catching = atrapar). En tu hoja escribe cinco datos exactos de Max, cada uno con la palabra del guion que lo respalda.", "Cinco años (five years old); once kilos (eleven kilos); come dos veces al día (twice a day); pasea cuarenta minutos (forty minutes); juega con una pelota roja (red ball).", ["escribe cinco datos distintos", "cada dato tiene su cifra o palabra exacta", "no mezcla datos de otro texto"], ["hoja con cinco datos", "nota del adulto"], ["cambiar eleven por una cifra aproximada", "escribir datos que no están en el guion"], "Reconoce los datos exactos y repasa con la persona los números que se confundieron con una segunda lectura."),
    "Pide a un adulto que lea otra vez la noticia de la ciclovía y subraya en tu hoja cada número que oigas.",
    "Escribe en español tres datos exactos de tu comuna o tu colegio que podrías incluir en una exposición oral.",
)

# ---------------------------------------------------------------- clase 3: entrevistas y conversaciones
SCIENCE = "«Reporter: Congratulations, Isidora! How long did you work on your project? Isidora: Four months. Reporter: What was the hardest part? Isidora: Finding the right box, because my first solar oven was too small. Reporter: What is your advice for other students? Isidora: Start early and ask for help.» (congratulations = felicitaciones, solar oven = horno solar, hardest = más difícil, advice = consejo, start early = empieza temprano)"
BAND = "«Diego: Do you want to join the school band? Valentina: I'm not sure. Do I need an instrument? Diego: No, the school lends instruments. Valentina: Then I'd like to try the drums. Diego: Great! The first rehearsal is on Wednesday at half past five.» (join = unirse, band = banda, instrument = instrumento, lends = presta, drums = batería, rehearsal = ensayo, half past five = cinco y media)"
TRAVEL = "«Interviewer: Mr. Rojas, where do you work? Mr. Rojas: I'm a bus driver in Valparaíso. Interviewer: Do you like your job? Mr. Rojas: Yes, I do. I meet many people every day. Interviewer: What is difficult? Mr. Rojas: The traffic in the morning.» (interviewer = entrevistador, bus driver = conductor de bus, job = trabajo, meet = conozco, traffic = tráfico)"

lesson(
    OA1, 3,
    "Las entrevistas y conversaciones escritas en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé una estrategia para entender entrevistas y conversaciones: unir cada pregunta con su respuesta mirando la palabra interrogativa. Sirve para encontrar datos sin perderte cuando hablan dos personas.",
    ["Sé las palabras what, where, when, who y how.", "Reconozco el presente simple con do y does."],
    [
        "En una entrevista, el entrevistador (interviewer) hace preguntas y la persona entrevistada responde. En una conversación (conversation) ambos hablan por turnos. Cada turno tiene una función: preguntar, responder, invitar, aceptar o dar un consejo. Para seguirlas, usa la estrategia pregunta-respuesta: cada palabra interrogativa anuncia qué tipo de dato viene después.",
        "How long pide un tiempo (four months). What pide una cosa o una idea. Where pide un lugar. When pide un día o una hora. Who pide una persona. Why pide un motivo y se responde con because. Las preguntas con Do you…? o Are you…? se responden con una respuesta corta: Yes, I do. / No, I don't. Escucha la pregunta, espera y luego anota solo la parte de la respuesta que contesta.",
        "Un consejo (advice) puede aparecer con un verbo en orden: «Start early and ask for help». Los acuerdos cierran muchas conversaciones: Great!, Perfect, See you on Wednesday. Si pierdes un turno, no te detengas: sigue con el siguiente y vuelve a la parte que falta en la segunda escucha.",
    ],
    [("interviewer", "entrevistador: quien hace las preguntas"), ("turn", "turno: cada vez que habla una persona"), ("advice", "consejo"), ("How long…?", "¿Cuánto tiempo…?"), ("short answer", "respuesta corta: Yes, I do."), ("rehearsal", "ensayo")],
    [
        ("Unir pregunta y respuesta", ADULT + SCIENCE + " ¿Cuánto tiempo trabajó Isidora en su proyecto?", ["La pregunta es How long, que pide un tiempo.", "La respuesta inmediata es Four months.", "Cuatro meses contesta la pregunta."], "Cuatro meses"),
        ("Identificar el consejo", ADULT + SCIENCE + " ¿Qué consejo da Isidora?", ["La pregunta dice advice, así que busco la recomendación.", "Isidora dice Start early and ask for help.", "Son dos acciones: empezar temprano y pedir ayuda."], "Empezar temprano y pedir ayuda"),
    ],
    [
        ("Anotar la pregunta del entrevistador como si fuera la respuesta.", "Se mezclan los turnos de las dos personas.", "Marca R (reportero) y E (entrevistada) y anota solo los datos de la persona que responde."),
        ("Responder «Yes» a una pregunta que empieza con What.", "Se ignora la palabra interrogativa.", "What no se responde con sí o no: pide una cosa o una idea."),
    ],
    [
        (ADULT + BAND + " ¿Quién invita a quién? a) Diego invita a Valentina b) Valentina invita a Diego", "a) Diego invita a Valentina", "Diego pregunta Do you want to join the school band?"),
        (ADULT + TRAVEL + " ¿Dónde trabaja el Sr. Rojas?", "En Valparaíso, como conductor de bus", "Dice I'm a bus driver in Valparaíso."),
        (ADULT + BAND + " ¿Qué instrumento quiere probar Valentina?", "La batería", "Dice I'd like to try the drums."),
    ],
    [
        (ADULT + BAND + " ¿Cuándo es el primer ensayo? a) el miércoles a las cinco y media b) el viernes a las cinco", "a) el miércoles a las cinco y media", "Diego dice Wednesday at half past five."),
        (ADULT + TRAVEL + " ¿Qué es lo difícil de su trabajo? a) el tráfico en la mañana b) conocer gente", "a) el tráfico en la mañana", "Responde a What is difficult con the traffic in the morning."),
        (ADULT + SCIENCE + " ¿Qué fue lo más difícil del proyecto?", "Encontrar la caja adecuada", "Dice Finding the right box porque el primer horno era muy pequeño."),
    ],
    [
        (ADULT + TRAVEL + " ¿Le gusta su trabajo al Sr. Rojas? a) sí, le gusta b) no, no le gusta", "a) sí, le gusta", "Responde Yes, I do a la pregunta Do you like your job?"),
        (ADULT + SCIENCE + " ¿Con qué pregunta empieza el reportero después de felicitarla? a) How long did you work on your project? b) What was the hardest part?", "a) How long did you work on your project?", "Esa es la primera pregunta; What was the hardest part viene después."),
        (ADULT + BAND + " ¿Qué le pregunta Valentina a Diego sobre el instrumento?", "Si necesita un instrumento", "Pregunta Do I need an instrument?"),
    ],
    [
        (ADULT + SCIENCE + " ¿Por qué fue difícil encontrar la caja adecuada? a) porque el primer horno solar era muy pequeño b) porque la caja se quebró", "a) porque el primer horno solar era muy pequeño", "Isidora explica con because: my first solar oven was too small."),
        (ADULT + BAND + " Valentina pregunta si necesita un instrumento. ¿Cuál es la respuesta de Diego? a) No, la escuela presta instrumentos. b) Sí, debe comprar uno.", "a) No, la escuela presta instrumentos.", "Diego dice No, the school lends instruments."),
    ],
    [
        (ADULT + TRAVEL + " El Sr. Rojas contesta Yes, I do. ¿A qué pregunta responde? a) Do you like your job? b) Where do you work?", "a) Do you like your job?", "Do you…? se responde con Yes, I do; Where pide un lugar."),
        ("Une cada pregunta con el dato que pide. 1) When is the rehearsal? 2) Who is the reporter? 3) How long was the project? Datos: a) una persona b) un tiempo de duración c) un día u hora", "1-c, 2-a, 3-b", "When pide día u hora, Who pide una persona y How long pide una duración."),
    ],
    [(ADULT + "«Teacher: Good morning, Pablo. Why are you late? Pablo: Sorry, the bus broke down. Teacher: Don't worry. Please sit down. Pablo: Thank you, miss.» (late = atrasado, broke down = se descompuso, don't worry = no te preocupes, sit down = siéntate). ¿Por qué llegó tarde Pablo? a) el bus se descompuso b) se levantó tarde", "a) el bus se descompuso", "Responde a Why con the bus broke down.")],
    [
        ("¿Qué tipo de dato pide la pregunta «Where…?»?", "Un lugar", "Where pregunta por dónde está o pasa algo."),
        ("¿Quién responde las preguntas en una entrevista?", "La persona entrevistada", "El entrevistador solo pregunta."),
        ("¿Qué respuesta corta va con «Do you like your job?» si la persona dice que sí?", "Yes, I do", "Do you…? se responde con do o don't."),
    ],
    task("Un adulto lee dos veces esta conversación: «Ana: Hi, Marcos. Are you free on Sunday? Marcos: Yes, I am. Ana: My family and I are going to the park at noon. Do you want to come? Marcos: Sure! Should I bring something? Ana: Yes, please bring a ball. Marcos: Perfect.» (free = libre, noon = mediodía, bring = traer). En tu hoja escribe: quién invita, adónde, a qué hora y qué debe traer Marcos.", "Ana invita a Marcos. Van al parque. A mediodía. Marcos debe traer una pelota.", ["responde las cuatro preguntas", "cada dato es exacto", "separa quién pregunta y quién responde"], ["hoja con cuatro respuestas", "nota del adulto"], ["confundir quién invita", "poner la hora de otra pregunta"], "Reconoce lo que acertó y relee con la persona solo las preguntas de Ana para unir cada una con su dato."),
    "Pide a un adulto que lea la entrevista a Isidora y subraya en tu hoja cada palabra interrogativa que oigas.",
    "Escribe en español dos preguntas que harías a un deportista y qué tipo de dato esperas en cada respuesta.",
)

# ---------------------------------------------------------------- clase 4: instrucciones, procedimientos y descripciones (brecha de información)
BEANS = "«How to grow a bean. First, put a wet cotton ball in a plastic cup. Second, put two beans on the cotton. Next, put the cup near a window. Then add a little water every day. Finally, after one week, look at the small roots.» (grow = hacer crecer, bean = poroto, cotton ball = bola de algodón, cup = vaso, near = cerca de, roots = raíces)"
ROOM = "«My classroom is on the second floor. It has twenty-eight desks, two big windows and a green board. There is a plant next to the door. The clock is above the board.» (floor = piso, desks = pupitres, windows = ventanas, board = pizarra, plant = planta, door = puerta, above = encima de)"
BEANS_A = "Persona A escuchó: «First, put a wet cotton ball in a plastic cup. Second, put two beans on the cotton.»"
BEANS_B = "Persona B escuchó: «Next, put the cup near a window. Then add a little water every day. Finally, after one week, look at the small roots.»"

lesson(
    OA1, 4,
    "Los textos de instrucciones y descripciones escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a entender instrucciones, procedimientos y descripciones y a completar la información que me falta con ayuda de otra persona. Sirve para seguir pasos en inglés y para preguntar lo que no entendí.",
    ["Sé first, second, next, then y finally.", "Conozco los colores y los números hasta cien."],
    [
        "Una instrucción (instruction) dice qué hacer con un verbo en orden: put, add, look, turn. Un procedimiento (procedure) es una serie de pasos para lograr algo. Las palabras first, second, next, then y finally marcan el orden. Una descripción (description) dice cómo es un lugar o una persona: tiene verbos como is y has, adjetivos y preposiciones como next to y above.",
        "En una brecha de información (information gap), dos personas escuchan partes distintas y deben compartir lo que oyeron para completar el texto. Por eso es útil hacer preguntas cortas: What is your first step? How many desks are there? Where is the plant? Para responder, cada persona lee solo lo que anotó, sin mostrar el guion completo del otro.",
        "Al juntar la información, revisa el orden: los pasos de A van antes que los de B si usan first y second, y los de B usan next, then y finally. Si dos datos chocan, pregunta para aclarar: Can you repeat, please? o Do you mean two beans? Preguntar no es un error: es una forma de confirmar lo que se escuchó.",
    ],
    [("instruction", "instrucción: qué hay que hacer"), ("procedure", "procedimiento: pasos ordenados"), ("description", "descripción"), ("information gap", "brecha de información: cada persona tiene una parte"), ("Can you repeat?", "¿Puedes repetir?"), ("above", "encima de")],
    [
        ("Completar los pasos entre dos personas", BEANS_A + " " + BEANS_B + " ¿Cuántos pasos tiene el procedimiento completo?", ["Cuento los pasos de A: put a cotton ball (1) y put two beans (2).", "Cuento los pasos de B: near a window (3), add water (4) y look at the roots (5).", "Sumo 2 y 3."], "5 pasos"),
        ("Ubicar un objeto en una descripción", ADULT + ROOM + " ¿Dónde está la planta?", ["Busco la palabra plant en el guion.", "Dice There is a plant next to the door.", "Next to significa al lado de."], "Al lado de la puerta"),
    ],
    [
        ("Poner los pasos de B antes que los de A.", "No se miran las palabras de secuencia.", "First y second van antes que next, then y finally; ordena con esas palabras."),
        ("No preguntar cuando falta un dato y adivinar.", "Se cree que preguntar es un error.", "Usa una pregunta corta, como Can you repeat, please?, y confirma el dato."),
    ],
    [
        (ADULT + BEANS + " ¿Qué se pone en el vaso al comienzo? a) una bola de algodón mojada b) tierra seca", "a) una bola de algodón mojada", "El primer paso dice a wet cotton ball."),
        (ADULT + ROOM + " ¿De qué color es la pizarra?", "Verde", "El guion dice a green board."),
        (ADULT + BEANS + " ¿Cuántos porotos se ponen sobre el algodón?", "2", "El segundo paso dice two beans."),
    ],
    [
        (ADULT + ROOM + " ¿Cuántos pupitres hay en la sala? a) 28 b) 18", "a) 28", "El guion dice twenty-eight desks, no eighteen."),
        (ADULT + BEANS + " ¿Cada cuánto se agrega agua? a) todos los días b) una vez por semana", "a) todos los días", "El guion dice add a little water every day."),
        (ADULT + ROOM + " ¿Dónde está el reloj?", "Encima de la pizarra", "El guion dice The clock is above the board."),
    ],
    [
        (ADULT + BEANS + " ¿Dónde se pone el vaso? a) cerca de una ventana b) dentro de un cajón", "a) cerca de una ventana", "El tercer paso dice put the cup near a window."),
        (ADULT + ROOM + " ¿En qué piso está la sala? a) en el segundo piso b) en el primer piso", "a) en el segundo piso", "El guion dice on the second floor."),
        (ADULT + ROOM + " ¿Cuántas ventanas grandes hay?", "2", "El guion dice two big windows."),
    ],
    [
        (BEANS_B + " Para el paso 5, ¿cuánto tiempo debe pasar antes de mirar las raíces? a) una semana b) un día", "a) una semana", "Finally, after one week, look at the small roots."),
        ("Persona A escuchó: «My room has one bed and two shelves.» (room = pieza, shelves = repisas) Persona B escuchó: «There is a lamp on the desk and a poster above the bed.» (lamp = lámpara, desk = escritorio, poster = afiche) Juntan los datos. ¿Qué hay sobre el escritorio y qué hay encima de la cama?", "Una lámpara sobre el escritorio y un afiche encima de la cama", "B dice a lamp on the desk y a poster above the bed."),
    ],
    [
        ("Persona A escuchó: «The kitchen is next to the living room.» Persona B escuchó: «The bathroom is between the bedroom and the kitchen.» (kitchen = cocina, living room = living, bathroom = baño, bedroom = dormitorio, between = entre) ¿Qué cuarto está entre el dormitorio y la cocina? a) el baño b) la sala", "a) el baño", "Persona B dice The bathroom is between the bedroom and the kitchen."),
        ("Una persona escuchó «put two beans» y otra anotó «put three beans». ¿Qué pregunta de aclaración ayuda a decidir? a) Do you mean two beans? b) Where is the window?", "a) Do you mean two beans?", "Esa pregunta confirma el dato que se contradice."),
    ],
    [(ADULT + "«To keep your classroom clean: first, put paper in the blue bin. Second, put plastic in the yellow bin. Finally, close the window before you leave.» (keep clean = mantener limpio, leave = salir). Persona A anotó el primer paso y Persona B anotó el segundo. ¿Qué paso falta anotar? a) cerrar la ventana antes de salir b) botar el plástico en el contenedor azul", "a) cerrar la ventana antes de salir", "El tercer paso, con finally, es close the window before you leave.")],
    [
        ("¿Qué es una brecha de información?", "Una tarea en que cada persona tiene una parte de la información", "Se completa preguntando y compartiendo."),
        ("¿Qué significa «next to»?", "Al lado de", "Es una preposición de lugar."),
        ("¿Qué frase pide que alguien repita?", "Can you repeat, please?", "Sirve para aclarar un dato."),
    ],
    task("Con una persona de tu casa: ella lee en voz alta esta primera mitad, «First, put a sheet of paper on the table. Second, fold it in half.», y tú anotas los dos pasos. Después ella lee la segunda mitad, «Next, fold the top corners to the center. Finally, write your name on the paper.» (sheet = hoja, table = mesa, half = mitad, corners = esquinas, center = centro). Escribe en español los cuatro pasos completos y una pregunta en inglés que harías si no entendieras uno.", "1. Poner una hoja sobre la mesa. 2. Doblarla por la mitad. 3. Doblar las esquinas de arriba al centro. 4. Escribir tu nombre. Pregunta: Can you repeat the third step, please?", ["escribe los cuatro pasos en el orden correcto", "relaciona cada paso con su palabra de secuencia", "formula una pregunta en inglés para aclarar"], ["hoja con cuatro pasos", "nota del adulto"], ["mezclar el orden de las dos mitades", "no escribir la pregunta de aclaración"], "Reconoce lo que acertó y repasa con la persona solo las palabras first, second, next y finally para ordenar el procedimiento."),
    "Pide a una persona de tu casa que lea la descripción de la sala y dibuja un croquis con los muebles y las preposiciones.",
    "Escribe en español la descripción de tu pieza en tres frases y marca dónde irían next to y above.",
)

# ---------------------------------------------------------------- clase 5: canciones y respuesta independiente
CHANT = "«Monday morning, hear the bell, / Books and pens and stories to tell. / Tuesday, Wednesday, friends and games, / Thursday, Friday, we all know names. / Saturday sun, we play outside, / Sunday family, side by side.» (hear = escuchar, bell = timbre, stories = historias, games = juegos, play outside = jugar afuera, side by side = lado a lado)"
SPORT = "«Good evening, sports fans. Chile won the volleyball match three sets to one. The final score was twenty-five to twenty-one in the last set. The team captain said: We played together, and that was the key.» (sports fans = hinchas, match = partido, sets = sets, score = marcador, captain = capitana, key = clave)"
RECIPE = "«To make a fruit salad: first, wash the fruit. Second, ask an adult to cut it into small pieces. Next, mix the pieces in a bowl. Finally, add a little orange juice.» (fruit salad = ensalada de frutas, wash = lavar, pieces = trozos, bowl = bol, juice = jugo)"

lesson(
    OA1, 5,
    "Las canciones, noticias, recetas y conversaciones escritas en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a responder por mi cuenta ante textos orales de formatos mezclados: canción, noticiero, instrucciones, conversación y anécdota. Sirve para reconocer el formato y buscar el dato que se pide sin ayuda.",
    ["Sé distinguir anécdotas, noticieros, entrevistas e instrucciones.", "Reconozco la evidencia con números, lugares y pasos."],
    [
        "Cada formato oral tiene señales. Una canción (song) tiene versos que riman y se repiten; sus palabras finales suenan parecido (bell – tell, games – names). Un noticiero abre con un saludo y entrega hechos recientes. Una receta o procedimiento usa first, next y finally con verbos en orden. Una conversación tiene dos hablantes por turnos. Una anécdota usa I, my y verbos en pasado.",
        "Cuando enfrentes un texto nuevo, sigue tres pasos. Primero, reconoce el formato por su comienzo y por las palabras de apertura. Segundo, lee la pregunta antes de volver a escuchar, para saber qué dato buscas. Tercero, comprueba tu respuesta con una palabra exacta del guion. Esa palabra es tu evidencia.",
        "En una canción, el tema es la idea general (los días de la semana, una amistad); las palabras que riman ayudan a recordar el orden. La entonación (intonation) y el ritmo también comunican: una canción alegre suena rápida y una triste, más lenta. No hace falta traducir cada verso; basta con entender el tema, los días o lugares nombrados y el sentimiento.",
    ],
    [("song", "canción"), ("rhyme", "rima: palabras de final parecido"), ("verse", "verso: una línea de la canción"), ("theme", "tema: de qué trata el texto"), ("intonation", "entonación: la subida y bajada de la voz"), ("score", "marcador de un partido")],
    [
        ("Reconocer el tema de una canción", ADULT + CHANT + " ¿De qué trata la canción?", ["Cuento los días que aparecen: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday y Sunday.", "Cada verso nombra algo que se hace en esos días.", "El tema general es la semana."], "De los días de la semana y lo que se hace en ellos"),
        ("Reconocer rimas", ADULT + CHANT + " ¿Qué palabra rima con «bell»?", ["Miro el final de los versos 1 y 2: bell y tell.", "Suenan parecido porque terminan en -ell.", "La palabra que rima es tell."], "tell"),
    ],
    [
        ("Pensar que una canción siempre cuenta una historia.", "Se confunden canción y narración.", "Pregunta cuál es el tema y si los versos riman o repiten ideas; algunas canciones solo enumeran o expresan sentimientos."),
        ("Responder sin comprobar la evidencia.", "Se confía en la memoria y se mezclan datos.", "Escribe junto a tu respuesta la palabra exacta que la respalda."),
    ],
    [
        (ADULT + SPORT + " ¿Qué ganó el equipo de Chile? a) un partido de vóleibol b) una carrera de bicicletas", "a) un partido de vóleibol", "El guion dice Chile won the volleyball match."),
        (ADULT + RECIPE + " ¿Qué se agrega al final? a) un poco de jugo de naranja b) azúcar y leche", "a) un poco de jugo de naranja", "Finally, add a little orange juice."),
        (ADULT + CHANT + " ¿Qué día es para jugar afuera?", "Sábado", "El verso dice Saturday sun, we play outside."),
    ],
    [
        (ADULT + SPORT + " ¿Cuál fue el marcador del último set?", "25 a 21", "El guion dice twenty-five to twenty-one in the last set."),
        (ADULT + RECIPE + " ¿Quién debe cortar la fruta? a) una persona adulta b) cada estudiante con un cuchillo", "a) una persona adulta", "El segundo paso dice ask an adult to cut it."),
        (ADULT + CHANT + " ¿Qué día se asocia con la familia?", "Domingo", "El verso final dice Sunday family, side by side."),
    ],
    [
        (ADULT + SPORT + " ¿Cuántos sets ganó el equipo de Chile?", "3", "El guion dice three sets to one."),
        (ADULT + RECIPE + " ¿Qué se hace con los trozos en el tercer paso? a) se mezclan en un bol b) se guardan en el refrigerador", "a) se mezclan en un bol", "El tercer paso dice mix the pieces in a bowl."),
        (ADULT + CHANT + " ¿Cuántos días de la semana nombra la canción?", "7", "Nombra de lunes a domingo."),
    ],
    [
        ("Clasifica estos comienzos por formato. 1) «Good evening. This is the news.» 2) «First, wash the fruit.» 3) «Once upon a time…» Formatos: a) noticiero b) receta c) cuento", "1-a, 2-b, 3-c", "Cada comienzo es una señal típica de su formato."),
        (ADULT + SPORT + " La capitana dice que la clave fue jugar juntas. ¿Qué sentimiento transmite el mensaje? a) trabajo en equipo b) enojo contra el rival", "a) trabajo en equipo", "Dice We played together, and that was the key."),
    ],
    [
        ("Una amiga escuchó: «My father and I made a kite last Saturday. It flew very high, and we were happy.» (kite = volantín, flew = voló). ¿Qué formato tiene? a) anécdota b) noticiero", "a) anécdota", "Usa my y I, y cuenta algo vivido en pasado."),
        ("Otra amiga escuchó: «The mayor opened a new library today. It has ten thousand books.» (mayor = alcalde, opened = abrió, library = biblioteca). ¿Qué formato tiene? a) noticiero b) canción", "a) noticiero", "Informa un hecho reciente con datos."),
    ],
    [(ADULT + "«Friday afternoon, bell is ringing, / Bags are packed and friends are singing. / See you Monday, wave goodbye, / Weekend sun is in the sky.» (ringing = sonando, bags = mochilas, packed = guardadas, singing = cantando, wave goodbye = decir adiós con la mano, sky = cielo). ¿Qué sentimiento transmite esta canción? a) alegría por el fin de semana b) tristeza porque termina el fin de semana", "a) alegría por el fin de semana", "Habla de despedirse y de que llega el sol del fin de semana.")],
    [
        ("En «Tuesday, Wednesday, friends and games» y «Thursday, Friday, we all know names», ¿qué palabra rima con games?", "names", "Games y names terminan con el mismo sonido."),
        ("¿Qué tipo de texto abre con «Good evening» y datos recientes?", "Un noticiero", "Saluda y entrega noticias."),
        ("¿Qué debes escribir junto a tu respuesta para justificarla?", "La palabra exacta del guion", "Esa es la evidencia."),
    ],
    task("Un adulto lee dos veces esta mini canción: «Rainy morning, umbrella blue, / Puddles dance and so do you. / Splash, splash, splash, we jump and play, / Rainy morning, happy day.» (rainy = lluvioso, umbrella = paraguas, puddles = charcos, splash = chapoteo, jump = saltar). En tu hoja escribe: el tema, dos palabras que riman y el sentimiento de la canción.", "Tema: un día de lluvia. Rimas: play y day (o blue y you). Sentimiento: alegría.", ["nombra el tema correctamente", "escribe un par de palabras que riman", "indica un sentimiento coherente con el texto"], ["hoja con tema, rima y sentimiento", "nota del adulto"], ["decir que la canción trata de un examen", "escribir palabras que no riman"], "Reconoce lo que acertó y relee con la persona los finales de cada verso para encontrar las rimas."),
    "Pide a un adulto que lea de nuevo la canción de los días de la semana y marca con colores cada día que oigas.",
    "Escribe en español qué formato oral te resulta más difícil de entender y qué haces para mejorar.",
)

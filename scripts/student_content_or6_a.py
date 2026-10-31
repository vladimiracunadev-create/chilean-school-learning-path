"""Cuaderno del estudiante, 6.º básico Orientación: OA 01 (valoración positiva de sí mismo) y OA 02 (emociones y su expresión)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1, OA2 = "OR06 OA 01", "OR06 OA 02"


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 01
lesson(
    OA1, 1,
    "Una hoja y un lápiz. El caso de Bastián, un estudiante inventado, y todos sus datos están escritos en los ejercicios. No necesitas contar nada privado tuyo.",
    "Aprenderé a diferenciar una habilidad, una fortaleza y un aspecto a superar, y a probar cada una con un hecho. Sirve para valorarme con sinceridad, sin presumir y sin criticarme de más.",
    ["Sé que un hecho se puede observar y una etiqueta no.", "Sé que en clase nadie debe contar cosas privadas si no quiere."],
    [
        "Valorarse de forma positiva es reconocer con sinceridad lo que uno es y lo que hace. Para lograrlo conviene separar tres ideas. Una habilidad es algo concreto que sabes hacer, como dibujar mapas o explicar una resta. Una fortaleza es una cualidad tuya que te ayuda a ti y a otros, como la perseverancia o la empatía. Un aspecto a superar es algo que hoy te cuesta y que puedes mejorar con práctica y con ayuda.",
        "Para no exagerar ni quedarte corto necesitas evidencia: un hecho que se pueda mostrar o contar. «Bastián explicó la tarea a Ema y ella la terminó» es evidencia. «Todos dicen que soy genial» no lo es, porque no cuenta qué hiciste. Con evidencia, tu valoración se vuelve justa: ni «soy perfecto» ni «soy un desastre».",
        "Bastián es un estudiante inventado. Esta semana armó la maqueta del curso en tres tardes, ayudó a Ema con una resta y volvió a intentar un dibujo cuatro veces sin rendirse. También llegó tarde tres de cinco días. Todo eso es verdad a la vez: tiene habilidades, una fortaleza (perseverancia) y un aspecto a superar (la puntualidad).",
    ],
    [("habilidad", "algo concreto que sé hacer y puedo mejorar"), ("fortaleza", "cualidad mía que me ayuda a mí y a otros"), ("aspecto a superar", "algo que hoy me cuesta y puedo mejorar"), ("evidencia", "hecho que se puede mostrar o contar"), ("valoración positiva", "reconocer con sinceridad lo que valgo, también lo que quiero mejorar")],
    [
        W("Clasificar un hecho", "Hecho: «Bastián armó la maqueta del curso en tres tardes». ¿Muestra una habilidad o un aspecto a superar?", ["Pregunta: ¿lo hizo y se puede mostrar? Sí, la maqueta existe.", "Armar una maqueta es algo concreto que sabe hacer.", "Por eso es evidencia de una habilidad."], "Evidencia de una habilidad"),
        W("Frase justa", "Bastián llegó tarde 3 de 5 días. ¿Qué frase es más justa: «Soy un irresponsable» o «Todavía me cuesta llegar a la hora: esta semana llegué tarde 3 de 5 días»?", ["«Soy un irresponsable» juzga a toda la persona sin mostrar hechos.", "La segunda frase cuenta un hecho y dice «todavía», que deja espacio para mejorar.", "Una valoración positiva es sincera y no hiere."], "«Todavía me cuesta llegar a la hora: esta semana llegué tarde 3 de 5 días»"),
    ],
    [
        M("Pensar que valorarme bien es decir que soy perfecto.", "Se confunde sentirse bien con no tener nada que mejorar.", "Reconoce lo que haces bien y lo que quieres mejorar, siempre con un hecho."),
        M("Decir «no sirvo para esto» después de un solo error.", "Un solo hecho parece mostrar cómo es toda la persona.", "Di «todavía me cuesta» y cuenta el hecho concreto."),
    ],
    R=[
        ex("«Bastián corrigió las faltas de ortografía de la invitación del curso». ¿Muestra una habilidad o un aspecto a superar?", "Una habilidad", "Corregir ortografía es algo concreto que sabe hacer y se ve en la invitación."),
        ex("«Bastián olvidó su material de arte en 4 de las 5 clases». ¿Muestra una habilidad o un aspecto a superar?", "Un aspecto a superar", "Es algo que hoy le cuesta y que puede mejorar con un sistema de recordatorios."),
        ex("¿Cuál es una evidencia: «Todos dicen que Bastián es genial» o «Bastián ayudó a Ema y ella terminó la resta»?", "«Bastián ayudó a Ema y ella terminó la resta»", "Cuenta algo que hizo y se puede comprobar."),
    ],
    U=[
        ex("¿Por qué decir «todavía me cuesta» describe un aspecto a superar mejor que «soy malo en esto»?", "Porque deja abierta la posibilidad de mejorar", "«Todavía» muestra que con práctica puede cambiar; la etiqueta no."),
        ex("¿Cuál de estas es una fortaleza de carácter y no una habilidad concreta: «dibujar mapas» o «no rendirse cuando algo sale mal»?", "«No rendirse cuando algo sale mal»", "Es una cualidad que ayuda en muchas tareas, no un saber hacer una sola cosa."),
        ex("¿Cuál frase combina sinceridad y respeto hacia uno mismo? A) «No me cuesta nada». B) «Soy bueno explicando y todavía me cuesta llegar a la hora». C) «Soy pésimo en todo».", "B", "Reconoce una habilidad y un aspecto a superar, sin exagerar ni insultarse."),
    ],
    A=[
        ex("Hechos de un perfil: 1) explicó una resta a Ema; 2) llegó tarde 3 de 5 días; 3) mantuvo ordenada su mochila toda la semana; 4) repitió un dibujo cuatro veces hasta terminarlo; 5) olvidó la tarea de Lenguaje. ¿Cuántos son evidencia de habilidades o fortalezas?", "3", "Los hechos 1, 3 y 4 muestran algo que sabe hacer o una cualidad; el 2 y el 5 muestran aspectos a superar."),
        ex("El hecho «Bastián ayudó a Ema con una resta» apoya una fortaleza. ¿Cuál: la empatía o la puntualidad?", "La empatía", "Ayudar a una compañera muestra que se preocupa por otros, no que llegue a la hora."),
        ex("Bastián habló 20 segundos al exponer, en voz baja y mirando el suelo. ¿Qué escritura es mejor para su aspecto a superar? A) «Soy malo para exponer». B) «Todavía me cuesta hablar con voz fuerte: hoy hablé 20 segundos en voz baja».", "B", "Usa «todavía» y cuenta el hecho; A es una etiqueta sin evidencia."),
    ],
    Z=[
        ex("Camila dice: «Bastián llegó tarde tres días, así que es irresponsable en todo». ¿Qué error comete?", "Usa un solo tipo de hecho para juzgar a toda la persona", "Llegar tarde no muestra cómo es Bastián en el resto de sus tareas."),
        ex("¿Por qué es mejor escribir un aspecto a superar con un hecho (llegué tarde 3 de 5 días) que con una etiqueta (soy impuntual)?", "Porque con un hecho se puede ver después si mejora", "Un número o conducta concreta se puede medir; una etiqueta no."),
    ],
    D=[
        arith("La semana 1 Bastián llegó tarde 3 de 5 días y la semana 2 llegó tarde 1 de 5 días. ¿Cuántos días menos llegó tarde en la semana 2?", "3-1", "Se restan los días de atraso de la semana 2 a los de la semana 1."),
        arith("Camila anotó 12 hechos de su perfil: 7 son habilidades, 3 son fortalezas de carácter y el resto son aspectos a superar. ¿Cuántos son aspectos a superar?", "12-7-3", "Al total de hechos se le restan los de los otros dos grupos."),
    ],
    context=[ex("El profesor entrega la frase para completar: «Una habilidad mía es… porque…». Maite escribe: «Una habilidad mía es ser simpática porque todos me quieren». ¿Usó evidencia?", "No", "«Todos me quieren» no cuenta un hecho que ella hizo ni que se pueda comprobar.")],
    selfcheck=[ex("En Orientación: ¿valorarme con sinceridad exige ocultar lo que me cuesta?", "No", "Incluye reconocer también lo que quiero mejorar."), ex("¿Una evidencia es un hecho que se puede mostrar o contar?", "Sí", "No es una opinión ni una etiqueta."), ex("¿Un aspecto a superar se puede mejorar con práctica y ayuda?", "Sí", "Lo que cuesta hoy puede cambiar con tiempo.")],
    task=T("Lee el perfil de Rocío, una estudiante inventada. Hechos: ordenó el material de ciencias de su grupo; tradujo una instrucción de inglés a sus compañeros; se puso nerviosa al exponer y habló muy bajo; esperó su turno para hablar aunque estaba nerviosa. Escribe una habilidad con su evidencia, una fortaleza con su evidencia y un aspecto a superar con «todavía». No uses etiquetas como «tímida».", "Habilidad: ordenar, porque ordenó el material de ciencias de su grupo. Fortaleza: ayudar a otros, porque tradujo una instrucción de inglés a sus compañeros. Aspecto a superar: todavía me cuesta hablar fuerte al exponer; hoy habló muy bajo.", ["escribe una habilidad con evidencia", "escribe una fortaleza con evidencia", "escribe un aspecto a superar con «todavía» y un hecho", "no usa etiquetas ni cuenta algo íntimo"], ["texto escrito o dicho", "cuadro de tres columnas"], ["decir la habilidad sin evidencia", "usar una etiqueta como «tímida»"], "Reconoce lo bien escrito y pregunta qué hecho apoya cada afirmación."),
    reinforce="Escribe tres hechos de un personaje de cuento y clasifica cada uno como habilidad, fortaleza o aspecto a superar.",
    extend="Cambia una frase dura que hayas escuchado sobre alguien («es un desastre») por un hecho con «todavía».",
)

lesson(
    OA1, 2,
    "Una hoja y un lápiz. El caso de Fran, un estudiante inventado, está escrito en los ejercicios.",
    "Aprenderé a separar lo que pasó, lo que siento y lo que me digo, y a poner un límite cuando me piden demasiado. Sirve para valorarme aunque tenga una mala racha o me compare con otros.",
    ["Sé distinguir habilidades, fortalezas y aspectos a superar con evidencia.", "Sé que un hecho se puede observar."],
    [
        "Cuando algo sale mal, se mezclan tres cosas. El hecho es lo que pasó y se puede observar: «Fran respondió bien 11 de 25 preguntas». La emoción es lo que siente: desánimo, vergüenza o rabia. La voz crítica es lo que se dice a sí mismo: «soy tonto». La voz crítica parece un hecho, pero es una suposición dura que exagera.",
        "Separar las tres cosas ayuda a valorarse bien. El hecho se acepta, la emoción se reconoce («me siento desanimado») y la voz crítica se cambia por una frase más justa: «hoy me fue mal en esta prueba y puedo estudiar de otra manera». Lo mismo pasa al compararse. Si un compañero sacó más puntos, eso es un hecho sobre él; no dice nada sobre tu valor.",
        "También existe el límite: lo que puedo y no puedo hacer ahora sin perjudicarme. Si te piden más tareas de las que alcanzas, puedes decir con respeto: «ahora no puedo asumir eso, pero sí puedo hacer esto otro». Poner un límite no es egoísmo; es una forma de cumplir lo que prometes y cuidar tu valoración personal.",
    ],
    [("hecho", "lo que pasó y se puede observar"), ("emoción", "lo que siente una persona"), ("voz crítica", "frase dura que una persona se dice a sí misma"), ("límite", "lo que puedo y no puedo hacer ahora sin perjudicarme"), ("mala racha", "período en que varias cosas salen mal, pero que pasa")],
    [
        W("Separar hecho y voz crítica", "Fran dice: «Respondí bien 11 de 25 preguntas. Soy un tonto». ¿Cuál parte es el hecho?", ["Pregunta: ¿se puede observar y contar? Las 11 respuestas buenas sí.", "«Soy un tonto» no se puede comprobar: es una suposición dura.", "El hecho es la primera frase."], "«Respondí bien 11 de 25 preguntas»"),
        W("Poner un límite", "Le piden a Fran hacer los carteles, la lista de turnos y las invitaciones, y solo alcanza a hacer una cosa. ¿Qué puede decir?", ["Un límite dice con claridad lo que puede hacer ahora.", "Propone algo posible, sin enojarse.", "Así cuida su tiempo y también colabora."], "«Ahora solo puedo hacer los carteles; ¿alguien puede tomar la lista?»"),
    ],
    [
        M("Creer que sentir desánimo prueba que no sirvo.", "Se confunde una emoción pasajera con un hecho sobre uno mismo.", "Reconoce la emoción y mira los hechos: qué pasó y qué puedes hacer."),
        M("Aceptar todas las tareas para que no se enojen conmigo.", "Se piensa que decir que no pone en riesgo la amistad.", "Di lo que alcanzas a hacer con respeto: «esto sí puedo»."),
    ],
    R=[
        ex("«Fran respondió bien 11 de 25 preguntas». ¿Es un hecho o una voz crítica?", "Un hecho", "Cuenta algo que pasó y se puede comprobar."),
        ex("«Me da vergüenza haber respondido tan pocas». ¿Nombra una emoción o un hecho?", "Una emoción", "Dice lo que siente quien habla, no lo que pasó."),
        ex("«Nunca voy a aprender nada». ¿Es una voz crítica o un hecho?", "Una voz crítica", "Es una frase dura que exagera y no se puede comprobar."),
    ],
    U=[
        ex("¿Por qué «nunca voy a aprender nada» no puede ser un hecho?", "Porque no se puede comprobar", "Habla del futuro y exagera, sin evidencia que lo muestre."),
        ex("¿Qué frase reemplaza mejor «soy un fracaso»: «Esta vez no me resultó y puedo intentarlo con otro método» o «Mejor no lo intento más»?", "«Esta vez no me resultó y puedo intentarlo con otro método»", "Acepta el hecho y abre una posibilidad de mejorar."),
        ex("¿Decir «hoy no alcanzo» a tiempo ayuda a cumplir lo que prometo? Responde sí o no.", "Sí", "Evita aceptar más de lo que se puede hacer."),
    ],
    A=[
        ex("Separa: «Mi equipo perdió 2 a 1, me siento triste y creo que soy un inútil». ¿Cuál es la voz crítica?", "«creo que soy un inútil»", "Es la frase dura sin evidencia; el marcador es el hecho y la tristeza es la emoción."),
        ex("Un compañero de Fran sacó 22 puntos y Fran sacó 11. ¿Qué dice ese dato sobre el valor de Fran como persona?", "Nada", "Un puntaje mide una prueba, no cuánto vale una persona."),
        ex("Fran ya tiene dos tareas por entregar hoy y le piden una tercera. ¿Qué respuesta pone un límite con respeto? A) «Ya, dame todo». B) «Hoy no alcanzo con una tercera; mañana sí puedo». C) «Ni se te ocurra pedirme eso».", "B", "Dice lo que puede hacer y propone otra fecha, sin ofender."),
    ],
    Z=[
        ex("Fran piensa: «Tuve una mala semana, entonces soy un fracaso». ¿Qué parte de la frase es la voz crítica?", "«soy un fracaso»", "Convierte una mala semana en un juicio sobre toda la persona."),
        ex("¿Por qué decir «ahora no puedo, pero mañana sí» es mejor que aceptar y no cumplir?", "Porque dice la verdad y permite cumplir", "Prometer lo que no se alcanza daña la confianza en uno mismo y en los demás."),
    ],
    D=[
        arith("Fran respondió bien 11 de 25 preguntas. ¿Cuántas respondió mal o dejó en blanco?", "25-11", "A las preguntas totales se les restan las bien respondidas."),
        arith("Fran tiene 60 minutos de tarea. Ya usó 15 minutos en Matemática y 20 en Lenguaje. ¿Cuántos minutos le quedan para Ciencias?", "60-15-20", "Se restan los dos tiempos ya usados."),
    ],
    context=[ex("Después de ver en una red social la medalla de un primo, Dani piensa: «Yo nunca he ganado nada, no valgo». ¿Qué parte de su pensamiento es una suposición sin evidencia?", "«no valgo»", "Que otro tenga una medalla no prueba nada sobre el valor de Dani.")],
    selfcheck=[ex("En Orientación: ¿una emoción como el desánimo prueba que no sirvo?", "No", "Una emoción es pasajera; los hechos dicen otra cosa."), ex("¿La voz crítica es siempre un hecho comprobable?", "No", "Es una suposición dura sin evidencia."), ex("¿Decir «hoy no alcanzo» puede ser una forma respetuosa de poner un límite?", "Sí", "Dice la verdad y cuida el tiempo propio.")],
    task=T("Lee la situación de Joaquín, un estudiante inventado: sacó 9 puntos de 20 en una prueba; siente vergüenza; se dice «soy un burro». Un compañero le pide además que haga solo el afiche del curso para mañana, y él ya tiene dos tareas. Escribe: el hecho, la emoción, una frase para reemplazar la voz crítica y una frase para poner un límite con respeto.", "Hecho: sacó 9 puntos de 20. Emoción: vergüenza. Frase justa: «Hoy me fue mal en esta prueba y puedo repasar de otra forma». Límite: «Hoy no alcanzo a hacer el afiche solo; puedo ayudar con las letras si alguien más lo arma».", ["separa hecho, emoción y voz crítica", "reemplaza la voz crítica por una frase justa", "pone un límite con respeto", "no cuenta nada íntimo propio"], ["texto escrito o dicho"], ["escribir la voz crítica como si fuera el hecho", "poner un límite con enojo"], "Reconoce cada parte y pregunta qué cambiaría en la frase del límite para sonar más amable."),
    reinforce="Escribe una mala racha de un personaje de cuento y separa el hecho, la emoción y la voz crítica.",
    extend="Escribe cómo responderías a un amigo que te dice «soy un fracaso» sin darle la razón y sin burlarte.",
)

lesson(
    OA1, 3,
    "Una hoja y un lápiz. El caso de Camila y la tabla de metas están escritos en los ejercicios.",
    "Aprenderé a comparar opciones frente a un aspecto a superar y a escribir una meta clara. Sirve para pasar de «me cuesta» a un plan pequeño que sí puedo cumplir.",
    ["Sé separar hecho, emoción y voz crítica.", "Sé escribir un aspecto a superar con «todavía» y un hecho."],
    [
        "Cuando reconoces un aspecto a superar, puedes elegir qué hacer. Hay opciones que no ayudan: esconderlo, culpar a otros («el profe me caía mal») o rendirte. Otras sí ayudan: ponerte una meta pequeña, practicar con constancia y pedir ayuda. Cada opción tiene consecuencias. Esconderlo puede evitar un mal rato hoy, pero el problema sigue. Una meta pequeña tarda más en dar frutos, pero se nota con los días.",
        "Una buena meta es clara y se puede comprobar. Debe decir qué vas a hacer, cuánto, cuándo y hasta qué fecha. «Estudiar más» no sirve porque no dice cuánto ni cuándo. En cambio, «repasar las tablas 15 minutos los lunes, miércoles y viernes durante tres semanas» se puede cumplir y revisar. Además, conviene que sea posible: si hoy no repasas nada, una meta de dos horas diarias es difícil de sostener.",
        "Camila, una estudiante inventada, tiene un aspecto a superar: entrega tarde sus trabajos. Compara tres opciones: no decir nada, pedir que le recuerden la fecha o anotar las fechas en un calendario. Escoge anotar las fechas, porque depende de ella, es fácil de hacer y puede revisar si lo cumple. Mejorar no es cambiar de golpe; es avanzar en pasos que se puedan contar.",
    ],
    [("opción", "una de las cosas que puedo elegir hacer"), ("consecuencia", "lo que ocurre después de una decisión"), ("meta", "lo que quiero lograr, dicho con claridad y con plazo"), ("plazo", "fecha o tiempo en que reviso mi meta"), ("constancia", "repetir algo con regularidad aunque cueste")],
    [
        W("Comparar dos metas", "Camila duda entre «ser más ordenada» y «anotar cada lunes las fechas de entrega de la semana en un calendario durante 4 semanas». ¿Cuál es una meta clara?", ["Pregunta: ¿dice qué, cuándo y hasta cuándo? La segunda sí.", "«Ser más ordenada» no se puede contar ni revisar.", "La meta clara se puede comprobar."], "«Anotar cada lunes las fechas de entrega de la semana en un calendario durante 4 semanas»"),
        W("Anticipar una consecuencia", "Camila piensa en esconder su atraso y no decir nada. ¿Qué consecuencia es más probable?", ["Esconder el problema no lo resuelve.", "Si no cambia nada, seguirá entregando tarde.", "Además, nadie podrá ayudarla."], "El atraso continúa y nadie la puede ayudar"),
    ],
    [
        M("Ponerme una meta enorme para cambiar de golpe.", "Se cree que más grande es mejor, pero se abandona pronto.", "Parte con una meta pequeña que puedas cumplir esta semana."),
        M("Culpar a otros por lo que me cuesta.", "Culpar alivia un rato, pero no cambia lo que depende de mí.", "Pregunta qué parte sí puedo cambiar yo y empieza por ahí."),
    ],
    R=[
        ex("«Estudiar más». ¿Es una meta clara o poco clara?", "Poco clara", "No dice cuánto ni cuándo."),
        ex("¿Culpar a otros es una opción que ayuda a mejorar un aspecto a superar? Responde sí o no.", "No", "No cambia lo que depende de mí."),
        ex("¿Cuál meta dice cuánto y cuándo: «Leer mejor» o «Leer 10 páginas de lunes a jueves»?", "«Leer 10 páginas de lunes a jueves»", "Indica cantidad y días, así se puede revisar."),
    ],
    U=[
        ex("¿Por qué una meta pequeña suele ser mejor que una gigante para empezar?", "Porque es más fácil de cumplir y mantener", "Cumplirla da confianza para seguir."),
        ex("Camila oculta que entregó tarde. ¿Qué consecuencia tiene para ella a futuro?", "Nadie puede ayudarla y el problema sigue", "Lo que no se dice no se puede mejorar con apoyo."),
        ex("¿Qué dato debe tener una meta para poder revisarla: una fecha o un deseo?", "Una fecha", "Con plazo se puede comprobar si se cumplió."),
    ],
    A=[
        ex("Mateo quiere mejorar su lectura. Opciones: A) «leer mucho». B) «leer 12 páginas, 4 días a la semana, por 3 semanas». C) «ser un gran lector». ¿Cuál es una meta clara?", "B", "Dice cuánto, cuándo y por cuánto tiempo."),
        ex("Tras 3 semanas, Camila cumplió su meta 9 de 12 veces. ¿Cuántas veces no la cumplió?", "3", "Se restan las veces cumplidas a las 12 programadas: 12 − 9 = 3."),
        ex("Camila puede (A) pedir ayuda a su profesora para organizar fechas, o (B) decir «no me importa». ¿Cuál opción ayuda a mejorar?", "A", "Pedir ayuda suma apoyo; decir «no me importa» no cambia nada."),
    ],
    Z=[
        ex("Una meta dice «dormir bien». ¿Qué le falta para que se pueda revisar?", "Cuánto y desde cuándo", "Sin cantidad y plazo no se puede saber si se cumplió."),
        ex("Si una persona no cumple su meta dos semanas seguidas, ¿qué conviene hacer: abandonar o hacerla más pequeña?", "Hacerla más pequeña", "Ajustar la meta mantiene el avance sin rendirse."),
    ],
    D=[
        arith("Camila repasa 15 minutos por día durante 3 días a la semana. ¿Cuántos minutos repasa en una semana?", "15*3", "Se multiplican los minutos por los días."),
        arith("Su meta dura 4 semanas y cada semana repasa 45 minutos. ¿Cuántos minutos repasa en total?", "45*4", "Se multiplican los minutos por semana por las semanas."),
    ],
    context=[ex("En una reunión de curso, Tomás dice: «Mi aspecto a superar es la ortografía. Mi meta: escribir 5 palabras difíciles cada día y revisarlas el viernes durante 3 semanas». ¿Su meta es clara?", "Sí", "Dice qué hará, cuánto, con qué frecuencia y por cuánto tiempo.")],
    selfcheck=[ex("En Orientación: ¿una meta clara dice qué hacer, cuánto y hasta cuándo?", "Sí", "Con eso se puede revisar."), ex("¿Esconder un aspecto a superar lo hace desaparecer?", "No", "Sin acción y sin ayuda, sigue igual."), ex("¿Conviene empezar con una meta pequeña que pueda cumplir?", "Sí", "Los pasos pequeños se sostienen mejor.")],
    task=T("Lee el caso de Isidora, una estudiante inventada: se distrae con el celular mientras estudia Matemática y termina las tareas muy tarde. Escribe una opción que no ayuda y su consecuencia, y una opción que sí ayuda convertida en meta con qué, cuánto, cuándo y plazo.", "No ayuda: decir «es que la tarea es aburrida» y seguir igual; consecuencia: seguirá terminando muy tarde. Meta: guardar el celular en otra pieza mientras estudia 30 minutos de Matemática, de lunes a jueves, durante 3 semanas.", ["escribe una opción que no ayuda y su consecuencia", "escribe una opción que ayuda", "la meta tiene qué, cuánto, cuándo y plazo", "es posible de cumplir"], ["texto escrito o dicho", "tabla de dos columnas"], ["meta sin plazo", "meta demasiado grande"], "Reconoce la claridad de la meta y pregunta cómo sabría Isidora que la cumplió."),
    reinforce="Escribe una meta clara para un aspecto a superar de un personaje de cuento, con qué, cuánto, cuándo y plazo.",
    extend="Explica por qué ajustar una meta que no se cumple no es lo mismo que rendirse.",
)

lesson(
    OA1, 4,
    "Una hoja y un lápiz. El caso de Ian y el registro de avances están escritos en los ejercicios.",
    "Aprenderé a elegir una acción segura para seguir adelante y a reconocer cuándo conviene pedir ayuda a un adulto. Sirve para cuidar mi valoración personal incluso cuando me siento mal por muchos días.",
    ["Sé escribir una meta clara.", "Sé separar hecho, emoción y voz crítica."],
    [
        "Una acción segura es una que te ayuda a avanzar sin dañarte ni dañar a otros. Para valorarte bien es útil llevar un registro de avances: anotar cada semana qué hiciste, qué te salió bien y qué sigues practicando. El registro funciona como evidencia. Cuando la voz crítica dice «nunca mejoro», puedes mirar la hoja y ver los hechos.",
        "También es importante celebrar los pasos pequeños. Si te propusiste repasar 4 veces en la semana y repasaste 3, eso es un avance real aunque no sea perfecto. Reconocer lo que sí lograste da energía para seguir. Equivocarse o fallar una vez no borra lo que ya hiciste.",
        "A veces la voz crítica se vuelve muy fuerte y dura muchos días: te sientes triste o sin ganas de nada, y piensas cosas como «no valgo». En ese caso no hay que aguantar solo. Una acción segura es contárselo a una persona adulta de confianza, como alguien de tu casa, tu profesor o profesora o el orientador. Pedir ayuda es una decisión valiente y muestra que te cuidas. Si alguna vez piensas en hacerte daño, avísale a un adulto ese mismo día; si el primero no te escucha, cuéntaselo a otro. En Chile también puedes llamar gratis al Fono Niños 147 de Carabineros.",
    ],
    [("acción segura", "decisión que me ayuda a avanzar sin dañarme ni dañar a otros"), ("registro de avances", "hoja donde anoto lo que hago y lo que logro"), ("avance", "paso que me acerca a mi meta, aunque sea pequeño"), ("adulto de confianza", "persona adulta con la que me siento seguro de hablar"), ("pedir ayuda", "contar lo que me pasa para recibir apoyo")],
    [
        W("Usar el registro como evidencia", "Ian se dice: «Nunca mejoro en Matemática». Su registro dice: semana 1, 2 ejercicios correctos; semana 2, 5; semana 3, 8. ¿Qué muestra el registro?", ["Se comparan las semanas: 2, 5 y 8.", "Cada semana tiene más ejercicios correctos.", "Eso contradice «nunca mejoro»."], "Que sí mejora: pasó de 2 a 8 ejercicios correctos"),
        W("Decidir cuándo pedir ayuda", "Ian lleva dos semanas sintiéndose triste y piensa «no valgo» casi todos los días. ¿Qué acción segura elige?", ["Son muchos días con una emoción fuerte.", "Aguantarlo solo no ayuda.", "Debe contárselo a un adulto de confianza."], "Contárselo a un adulto de confianza"),
    ],
    [
        M("Pensar que pedir ayuda es una señal de que soy débil.", "Se cree que un problema se debe resolver solo.", "Pedir ayuda a tiempo es una forma de cuidarse y de resolver más rápido."),
        M("Celebrar solo cuando todo sale perfecto.", "Se ignoran los pasos pequeños y se pierde motivación.", "Anota y celebra cada avance, aunque sea pequeño."),
    ],
    R=[
        ex("¿Un registro de avances sirve como evidencia de que estás mejorando? Responde sí o no.", "Sí", "Muestra con hechos lo que hiciste cada semana."),
        ex("Si te sientes muy triste durante muchos días, ¿es una acción segura hablar con un adulto de confianza?", "Sí", "Contar lo que pasa permite recibir apoyo."),
        ex("¿Qué es un avance pequeño: repasar 3 veces cuando la meta era 4 o no repasar nada?", "Repasar 3 veces cuando la meta era 4", "Aunque falta un poco, es un paso real hacia la meta."),
    ],
    U=[
        ex("¿Por qué conviene celebrar los pasos pequeños?", "Porque dan energía para seguir", "Reconocer lo logrado ayuda a mantener la constancia."),
        ex("¿Por qué pedir ayuda no es señal de debilidad?", "Porque es una forma de cuidarse", "Cuidarse incluye buscar apoyo cuando algo pesa."),
        ex("La voz crítica dice «nunca mejoro». ¿Qué puedes mirar para comprobarlo: tu registro de avances o lo que opina otro compañero?", "Tu registro de avances", "Contiene hechos tuyos; la opinión de otro no prueba nada."),
    ],
    A=[
        ex("Ian anotó los ejercicios correctos de 4 semanas: 3, 6, 6 y 9. ¿En cuántas semanas igualó o mejoró el resultado de la semana anterior?", "3", "Semana 2 mejoró (6 > 3), semana 3 igualó (6 = 6) y semana 4 mejoró (9 > 6)."),
        ex("Una amiga te cuenta que lleva semanas sin ganas de nada y piensa que no vale. ¿Qué acción segura le recomiendas? A) «Aguanta y no digas nada». B) «Habla con un adulto de confianza, y yo te acompaño». C) «Ríete de eso».", "B", "Propone apoyo de un adulto y acompañamiento, sin dejarla sola."),
        ex("Ian eligió como primer paso «resolver 5 ejercicios hoy». ¿Es una acción segura y posible o un cambio gigante?", "Una acción segura y posible", "Es un paso concreto, pequeño y fácil de comprobar."),
    ],
    Z=[
        ex("Dos semanas seguidas, Ian cumplió 2 de las 4 veces propuestas. ¿Es lo mismo que no haber avanzado nada?", "No", "Cumplir 2 de 4 es un avance real aunque falte para la meta."),
        ex("¿Por qué sería poco seguro que Ian ocultara por mucho tiempo su tristeza a todos los adultos?", "Porque nadie podría ayudarlo", "Cuando una emoción pesa mucho, el apoyo de un adulto ayuda a sentirse mejor."),
    ],
    D=[
        arith("En su registro, Ian anotó 3 ejercicios correctos la semana 1 y 12 la semana 4. ¿Cuántos más hizo en la semana 4?", "12-3", "Se resta el resultado de la semana 1 al de la semana 4."),
        arith("Ian se propuso repasar 4 días a la semana durante 5 semanas. ¿Cuántos días de repaso son en total?", "4*5", "Se multiplican los días por semana por las semanas."),
    ],
    context=[ex("Sofi lleva tres semanas sin ánimo para ir al colegio y se dice todos los días «soy un desastre». Su tía le pregunta cómo está. ¿Qué es lo más seguro que puede hacer Sofi?", "Contarle a su tía cómo se siente", "Decir lo que le pasa a un adulto de confianza permite recibir apoyo.")],
    selfcheck=[ex("En Orientación: ¿una acción segura me ayuda sin dañarme ni dañar a otros?", "Sí", "Ese es el criterio para elegirla."), ex("¿Pedir ayuda a un adulto de confianza es una forma de cuidarse?", "Sí", "Permite recibir apoyo."), ex("¿El registro de avances puede ayudarme a responder a la voz crítica?", "Sí", "Aporta hechos para contradecir suposiciones.")],
    task=T("Lee el registro de avances de Leo, un estudiante inventado, que quiere mejorar su lectura en voz alta: semana 1, leyó 1 vez; semana 2, leyó 2 veces; semana 3, leyó 2 veces; semana 4, leyó 4 veces. Su meta era leer 4 veces por semana. Escribe (1) qué avance real muestra su registro, (2) una frase para celebrarlo y (3) qué debería hacer Leo si además llevara semanas muy triste pensando que no vale.", "Avance: pasó de 1 a 4 veces por semana y en la semana 4 cumplió su meta. Frase: «Subí de 1 a 4 veces por semana; puedo seguir». Si lleva semanas triste, debe contárselo a un adulto de confianza.", ["describe el avance con números del registro", "celebra con una frase concreta", "recomienda pedir ayuda a un adulto de confianza", "no usa etiquetas ni cuenta algo íntimo propio"], ["texto escrito o dicho"], ["decir que no avanzó nada", "recomendar aguantar solo"], "Reconoce el uso de los números y pregunta qué adulto de confianza podría elegir Leo."),
    reinforce="Haz un registro de avances de cuatro semanas para un personaje inventado y escribe qué muestra.",
    extend="Explica cómo cambiaría tu forma de hablarte si usaras un registro de avances en vez de la voz crítica.",
)

# ================================================================ OA 02
lesson(
    OA2, 1,
    "Una hoja y un lápiz. Las situaciones y la escala de intensidad están escritas en los ejercicios. Trabajas con personajes inventados.",
    "Aprenderé a distinguir y describir emociones con palabras precisas y a medir su intensidad. Sirve para entender lo que siento y decirlo mejor.",
    ["Sé nombrar emociones básicas: alegría, tristeza, miedo y enojo.", "Sé que sentir una emoción no es bueno ni malo."],
    [
        "Las emociones son reacciones que sentimos ante lo que ocurre. Todas son normales y avisan algo. El enojo avisa que algo parece injusto o que alguien pasó un límite. El miedo avisa de un peligro. La tristeza avisa de una pérdida. La alegría avisa de algo agradable. Hay emociones más precisas, como la frustración, que es lo que sentimos cuando algo que queremos lograr no sale, y la vergüenza, que es sentir que otros nos miran y nos juzgan.",
        "Para describir una emoción conviene mirar tres cosas. Primero, qué la provocó: un hecho concreto. Segundo, qué siente el cuerpo: el corazón late rápido, el estómago se aprieta, las manos sudan. Tercero, su intensidad, que puedes medir en una escala de 1 (muy suave) a 5 (muy fuerte). Una misma emoción puede ser un 2 o un 5, y eso cambia lo que conviene hacer.",
        "Nombrar con exactitud ayuda a calmarse. Decir «estoy frustrado, un 4, porque el trabajo no me sale» da más información que «estoy mal». Además, cada persona siente de forma distinta ante lo mismo: lo que a uno le da risa a otro le puede dar vergüenza. Por eso hay que preguntar y no suponer lo que siente el otro.",
    ],
    [("emoción", "reacción que siento ante algo que ocurre"), ("intensidad", "qué tan fuerte es una emoción, de 1 a 5"), ("frustración", "emoción cuando algo que quiero lograr no sale"), ("vergüenza", "sentir que otros me miran y me juzgan"), ("señal del cuerpo", "cambio que noto en el cuerpo cuando siento una emoción")],
    [
        W("Nombrar con precisión", "A Tomás no le sale el trabajo de ciencias después de intentarlo cuatro veces y siente rabia y ganas de botarlo. ¿Qué emoción precisa describe esto: frustración o alegría?", ["El trabajo no sale aunque lo intentó varias veces.", "Eso es lo que define la frustración.", "La alegría no encaja con lo que ocurre."], "Frustración"),
        W("Medir la intensidad", "Camila siente el corazón muy rápido y las manos sudadas antes de exponer, y no puede quedarse quieta. ¿Qué intensidad de nervios le pondrías en la escala de 1 a 5: 1 o 4?", ["Las señales del cuerpo son fuertes y muchas.", "Un 1 sería casi no notarlo.", "Por eso corresponde un 4."], "4"),
    ],
    [
        M("Decir «estoy mal» sin explicar qué siento.", "Una palabra tan amplia no dice qué emoción es ni qué la causó.", "Usa una palabra precisa (frustración, vergüenza, miedo) y di qué la provocó."),
        M("Creer que todos sienten lo mismo ante lo mismo.", "Se supone lo que siente el otro sin preguntar.", "Pregunta cómo se siente cada persona antes de opinar."),
    ],
    R=[
        ex("«El corazón late rápido y las manos sudan antes de una prueba». ¿Es una señal del cuerpo o una causa?", "Una señal del cuerpo", "Es lo que siente el cuerpo cuando hay una emoción."),
        ex("¿Qué emoción avisa de una pérdida: la tristeza o el miedo?", "La tristeza", "La tristeza aparece cuando se pierde algo importante."),
        ex("En una escala de 1 a 5, ¿cuál número es una emoción muy suave: 1 o 5?", "1", "El 1 es la intensidad más baja."),
    ],
    U=[
        ex("¿Por qué «estoy frustrado porque el trabajo no me sale» describe mejor que «estoy mal»?", "Porque nombra la emoción y su causa", "Da información precisa sobre lo que siente y por qué."),
        ex("A Sofi le dio risa que su curso cantara «cumpleaños feliz» en forma exagerada; a Luz le dio vergüenza. ¿Es raro que sientan distinto?", "No", "Cada persona puede sentir algo diferente ante el mismo hecho."),
        ex("¿Qué avisa el enojo: que algo parece injusto o que viene un peligro?", "Que algo parece injusto", "El enojo suele aparecer ante una injusticia o un límite pasado."),
    ],
    A=[
        ex("Frases: 1) «Me da vergüenza equivocarme frente al curso»; 2) «Me da miedo la oscuridad»; 3) «Me da frustración que mi dibujo no salga»; 4) «Me da vergüenza que me mire todo el curso». ¿Cuántas nombran vergüenza?", "2", "Las frases 1 y 4 hablan de sentirse mirado o juzgado por otros."),
        ex("Ian describe: «Rabia, intensidad 5, porque rompieron mi proyecto». ¿Qué dato es la causa?", "Que rompieron su proyecto", "La causa es el hecho que provocó la emoción."),
        ex("Un compañero dice: «Seguro que a todos les da lo mismo la nota». ¿Qué conviene hacer: preguntar a cada uno o suponer?", "Preguntar a cada uno", "Cada persona siente distinto y solo preguntando se sabe."),
    ],
    Z=[
        ex("Dos estudiantes sienten rabia, una en nivel 1 y otra en nivel 5. ¿Debería ser igual lo que hagan para calmarse?", "No", "Una intensidad alta necesita más tiempo y apoyo que una baja."),
        ex("¿Por qué ayuda notar las señales del cuerpo para descubrir una emoción?", "Porque el cuerpo avisa antes de que uno la nombre", "Latidos, sudor o tensión muestran que algo se siente."),
    ],
    D=[
        arith("En un día, Camila anotó la intensidad de su nerviosismo: 4 antes de exponer y 1 después de terminar. ¿Cuántos puntos bajó?", "4-1", "Se resta la intensidad final a la inicial."),
        arith("Un curso de 28 estudiantes marcó su emoción antes de una prueba: 11 nervios, 9 calma y el resto preocupación. ¿Cuántos marcaron preocupación?", "28-11-9", "Al total se le restan los otros dos grupos."),
    ],
    context=[ex("Antes de la feria de ciencias, Mati dice: «Estoy nervioso, un 3: el estómago se me aprieta, pero creo que puedo». ¿Describió su emoción con causa, señal del cuerpo e intensidad?", "Sí", "Dijo la emoción, la intensidad (3) y una señal del cuerpo (estómago apretado).")],
    selfcheck=[ex("En Orientación: ¿sentir enojo o miedo es siempre algo malo?", "No", "Todas las emociones son normales y avisan algo."), ex("¿Una escala de 1 a 5 sirve para medir la intensidad de una emoción?", "Sí", "Permite saber qué tan fuerte es."), ex("¿Todas las personas sienten lo mismo ante lo mismo?", "No", "Cada una puede sentir algo distinto.")],
    task=T("Lee las situaciones de Gabo, un estudiante inventado: (1) su equipo perdió el partido por un punto; (2) su amigo no lo invitó a su cumpleaños; (3) le tocó exponer solo frente al curso. Para cada una escribe una emoción precisa, una señal del cuerpo que podría sentir y una intensidad de 1 a 5.", "(1) Frustración, 4: aprieta los puños. (2) Tristeza, 3: nudo en la garganta. (3) Nervios, 4: corazón rápido y manos sudadas.", ["usa tres emociones precisas", "incluye una señal del cuerpo por cada una", "indica una intensidad de 1 a 5 por cada una", "no cuenta una vivencia propia"], ["tabla escrita o dicha"], ["decir solo «mal»", "no incluir intensidad"], "Reconoce la precisión de las palabras y pregunta qué cambiaría si la intensidad fuera 1."),
    reinforce="Escribe tres emociones de un personaje de cuento con su causa, su señal del cuerpo y su intensidad.",
    extend="Explica por qué dos personas pueden sentir emociones distintas ante el mismo hecho.",
)

lesson(
    OA2, 2,
    "Una hoja y un lápiz. Las frases de los personajes están escritas en los ejercicios.",
    "Aprenderé a decir lo que siento sin herir, usando el mensaje «yo»: hecho, emoción y petición. Sirve para que los demás me entiendan y para cuidar la relación.",
    ["Sé nombrar una emoción con su intensidad.", "Sé separar hechos de suposiciones."],
    [
        "Expresar una emoción de forma apropiada es decirla de modo que me entiendan y que no dañe a otros ni a mí. Un modo que ayuda es el mensaje «yo», que tiene tres partes: el hecho que ocurrió, la emoción que siento y lo que necesito. Por ejemplo: «Cuando no me esperaste en el recreo, me sentí triste. Me gustaría que me avises si te vas».",
        "El mensaje «yo» es distinto de la acusación. «Tú nunca me escuchas, eres un egoísta» juzga a la otra persona con palabras como «nunca» y «siempre» y con insultos. Eso provoca defensa o pelea. En cambio, hablar desde lo que me pasa a mí invita a escuchar. Es más probable que el otro responda con cuidado.",
        "Expresar una emoción también tiene límites. Tengo derecho a sentir rabia, pero no a gritar, insultar o empujar. Puedo decir «necesito un momento» antes de hablar si me siento muy alterado. Así cuido mi relación con los demás y cuido mi propia tranquilidad.",
    ],
    [("mensaje «yo»", "frase con hecho, emoción y petición, dicha desde lo que me pasa"), ("acusación", "frase que culpa o insulta a la otra persona"), ("petición", "lo que necesito que cambie o que haga el otro"), ("expresar", "decir lo que siento para que me entiendan"), ("respeto", "tratar con cuidado a los demás y a mí mismo")],
    [
        W("Armar un mensaje «yo»", "Camila prestó su lápiz y no se lo devolvieron. Arma un mensaje «yo» con hecho, emoción y petición.", ["Hecho: «cuando no me devolviste el lápiz».", "Emoción: «me sentí molesta».", "Petición: «me gustaría que me lo devuelvas mañana»."], "«Cuando no me devolviste el lápiz, me sentí molesta. Me gustaría que me lo devuelvas mañana»"),
        W("Distinguir una acusación", "¿«Tú siempre arruinas todo» es mensaje «yo» o acusación?", ["Usa «tú siempre», que es una generalización.", "Culpa a la otra persona sin decir qué pasó.", "No cuenta lo que siente quien habla."], "Acusación"),
    ],
    [
        M("Pensar que si digo lo que siento con gritos me entienden mejor.", "Se cree que la fuerza hace que se escuche.", "Habla con voz firme y calmada: el otro escucha más cuando no se defiende."),
        M("Guardar todo hasta que explota.", "Se cree que callar evita problemas.", "Dilo antes con un mensaje «yo», cuando la emoción aún es manejable."),
    ],
    R=[
        ex("¿Cuáles son las tres partes del mensaje «yo»: hecho, emoción y petición, o insulto, queja y amenaza?", "Hecho, emoción y petición", "Esas tres partes explican qué pasó, cómo me siento y qué necesito."),
        ex("«Eres un egoísta y nunca escuchas». ¿Es mensaje «yo» o acusación?", "Acusación", "Insulta y generaliza con «nunca»."),
        ex("En el mensaje «Me sentí triste cuando no me esperaste», ¿cuál es la emoción?", "Triste", "Es lo que siente quien habla."),
    ],
    U=[
        ex("¿Por qué una acusación suele provocar defensa en el otro?", "Porque lo culpa y lo insulta", "La persona acusada tiende a defenderse en vez de escuchar."),
        ex("¿Se puede sentir rabia sin gritar ni insultar? Responde sí o no.", "Sí", "La emoción es válida; la forma de expresarla se puede elegir."),
        ex("¿Qué parte del mensaje «yo» dice lo que quiero que cambie: el hecho o la petición?", "La petición", "La petición es lo que necesito que el otro haga."),
    ],
    A=[
        ex("Frases: 1) «Cuando hablas mientras explico, me siento interrumpida; ¿puedes esperar?»; 2) «Eres un pesado»; 3) «Cuando no me avisaste del cambio, me sentí fuera; me gustaría que me avises»; 4) «Siempre haces lo mismo». ¿Cuántas son mensajes «yo»?", "2", "Las frases 1 y 3 tienen hecho, emoción o efecto y petición."),
        ex("Ordena las partes de un mensaje «yo»: A) «Me gustaría que me avises». B) «Cuando no me avisaste». C) «Me sentí confundido». ¿Qué letra va primero?", "B", "Primero se cuenta el hecho, luego la emoción y al final la petición."),
        ex("Ian se siente molesto porque lo interrumpieron tres veces. ¿Cuál es el mejor mensaje? A) «Me interrumpes siempre». B) «Cuando me interrumpen, no puedo terminar mi idea; me gustaría hablar sin cortes». C) «Cállate tú».", "B", "Cuenta el efecto y la petición sin acusar."),
    ],
    Z=[
        ex("Un compañero dice: «Si digo lo que siento, voy a pelear». ¿Qué le responderías?", "Que decirlo con calma evita más peleas", "El mensaje «yo» invita a escuchar y baja la tensión."),
        ex("¿Por qué «necesito un momento antes de hablar» puede ser una frase respetuosa cuando uno está muy alterado?", "Porque evita decir cosas que hieren", "La pausa permite calmarse y elegir mejor las palabras."),
    ],
    D=[
        arith("Camila escribió 3 mensajes «yo» el lunes, 2 el martes y 4 el miércoles. ¿Cuántos escribió en total?", "3+2+4", "Se suman los mensajes de los tres días."),
        arith("En una actividad hubo 30 frases. 12 eran mensajes «yo», 5 eran preguntas y el resto eran acusaciones. ¿Cuántas eran acusaciones?", "30-12-5", "Al total se le restan los otros dos tipos."),
    ],
    context=[ex("Un grupo de trabajo se enoja porque Bruno no trajo su parte. Valentina dice: «Cuando no trajiste tu parte, me preocupé porque la entrega es mañana; ¿puedes traerla hoy en la tarde?». ¿Usó un mensaje «yo»?", "Sí", "Dice el hecho, la emoción y la petición sin insultar.")],
    selfcheck=[ex("En Orientación: ¿el mensaje «yo» incluye hecho, emoción y petición?", "Sí", "Esas son sus tres partes."), ex("¿Gritar es la mejor forma de que me entiendan?", "No", "Los gritos hacen que el otro se defienda."), ex("¿Puedo pedir un momento antes de hablar si estoy muy alterado?", "Sí", "Una pausa ayuda a elegir las palabras.")],
    task=T("Lee estas tres situaciones de Dani, un estudiante inventado: (1) le cambiaron su puesto sin avisar; (2) un compañero se rió cuando se equivocó leyendo; (3) un amigo lo dejó esperando 20 minutos. Escribe un mensaje «yo» para la situación (2): con hecho, emoción y petición, y sin acusar.", "«Cuando te reíste porque me equivoqué leyendo, me sentí avergonzado. Me gustaría que, si me equivoco, esperes a que termine y me ayudes».", ["incluye un hecho", "incluye una emoción", "incluye una petición", "no insulta ni usa «nunca» o «siempre»"], ["frase escrita o dicha"], ["acusar a la otra persona", "omitir la petición"], "Reconoce las tres partes y pregunta cómo sonaría con un tono calmado."),
    reinforce="Convierte tres acusaciones en mensajes «yo» con hecho, emoción y petición.",
    extend="Explica por qué «siempre» y «nunca» hacen que el otro escuche menos.",
)

lesson(
    OA2, 3,
    "Una hoja y un lápiz. La situación de Mateo y la tabla de opciones están escritas en los ejercicios.",
    "Aprenderé a comparar formas de expresar una emoción y a prever su impacto en mí y en los demás. Sirve para elegir la forma que cuida a todos antes de actuar.",
    ["Sé armar un mensaje «yo».", "Sé que una emoción se puede expresar de más de una forma."],
    [
        "Ante una misma emoción hay varias formas de expresarla. Se pueden agrupar en cuatro. Explotar es gritar, insultar o empujar. Callar es guardarse todo. Escapar es irse sin decir nada. Y la forma apropiada es expresar con respeto: decir lo que siento con un mensaje «yo», pedir un momento o escribirlo. Cada forma tiene un impacto distinto.",
        "El impacto es lo que ocurre después, en ti y en los demás. Si explotas, tal vez te desahogues un rato, pero lastimas a otros, te arrepientes y pueden aparecer castigos. Si callas, el enojo se acumula y puedes sentir malestar o explotar más tarde. Si escapas, el problema queda sin resolver. Si expresas con respeto, hay más posibilidades de que te entiendan y de mantener la amistad.",
        "Una forma práctica de decidir es hacerte tres preguntas antes de actuar: ¿esto me ayuda a sentirme mejor de verdad?, ¿hiere a otra persona?, ¿resuelve lo que me molesta? La mejor opción es la que responde sí, no, sí. Practicar estas preguntas ayuda a elegir con calma y no por impulso.",
    ],
    [("explotar", "gritar, insultar o empujar al sentir una emoción fuerte"), ("callar", "guardarse la emoción sin decirla"), ("escapar", "irse sin decir nada"), ("impacto", "lo que ocurre después, en mí y en otros"), ("impulso", "acción que hago sin pensar")],
    [
        W("Comparar formas de expresar", "Mateo está enojado porque su compañero rompió su dibujo. Opciones: A) empujarlo, B) no decir nada, C) decirle «Cuando rompiste mi dibujo me sentí enojado; quiero que lo repares». ¿Cuál es la forma apropiada?", ["A hiere a otra persona.", "B guarda el enojo y no resuelve nada.", "C dice el hecho, la emoción y la petición con respeto."], "C"),
        W("Prever el impacto", "Si Mateo explota y grita, ¿cuál es el impacto probable en los demás?", ["Gritar asusta o molesta a otros.", "La otra persona se defiende o se enoja.", "Se pierde la oportunidad de resolver."], "Los demás se asustan o se enojan y el problema no se resuelve"),
    ],
    [
        M("Creer que explotar «saca todo» y es lo único que alivia.", "El alivio es corto y luego aparecen consecuencias.", "Busca primero una pausa o un mensaje «yo»."),
        M("Pensar que callar siempre es ser prudente.", "Se confunde guardarse algo con resolverlo.", "Si algo te molesta de verdad, dilo con respeto cuando estés más calmado."),
    ],
    R=[
        ex("Gritar e insultar al sentir enojo, ¿es explotar, callar o escapar?", "Explotar", "Es expresar la emoción con fuerza y sin cuidar a otros."),
        ex("Irse del lugar sin decir nada para evitar el problema, ¿es callar o escapar?", "Escapar", "Es dejar la situación sin resolverla."),
        ex("¿Decir lo que siento con un mensaje «yo» es una forma apropiada de expresar una emoción? Responde sí o no.", "Sí", "Explica lo que me pasa y cuida a los demás."),
    ],
    U=[
        ex("¿Qué impacto puede tener guardarse el enojo por mucho tiempo?", "Que se acumule y explote más tarde", "Lo que se calla sin resolver puede crecer."),
        ex("¿Por qué empujar a otro empeora la situación?", "Porque lo daña y se pierde la posibilidad de arreglar", "Hiere y genera más conflicto."),
        ex("De las tres preguntas «¿me ayuda de verdad?, ¿hiere?, ¿resuelve?», ¿cuál debe responderse «no» para que la opción sea buena?", "¿Hiere a otra persona?", "Una buena opción no daña a nadie."),
    ],
    A=[
        ex("Maite está molesta porque la dejaron fuera de un grupo de trabajo. Opciones: A) gritar en la sala; B) no hablar con nadie; C) decir «Cuando me dejaron fuera, me sentí triste; ¿puedo unirme?». ¿Cuál cuida a todos?", "C", "Dice el hecho, la emoción y una petición sin herir."),
        ex("Clasifica: «Gritarle a un compañero y empujar su mesa». ¿Es explotar, callar o escapar?", "Explotar", "Gritar y empujar es descargar la emoción con fuerza y sin cuidar a otros."),
        ex("Una opción: respirar hondo, esperar un minuto y luego hablar. Respuestas: ¿ayuda de verdad, hiere y resuelve? Elige la combinación correcta: A) sí, no, sí. B) no, sí, no.", "A", "Ayuda, no hiere y permite resolver."),
    ],
    Z=[
        ex("Un amigo dice: «Prefiero callar y evitar peleas». ¿Qué desventaja tiene si el problema es importante?", "Que no se resuelve y la molestia crece", "Callar evita la pelea hoy, pero deja el problema sin atender."),
        ex("¿Por qué expresar una emoción con respeto ayuda también a quien la siente?", "Porque se siente mejor sin arrepentirse", "Evita el arrepentimiento y puede resolver el problema."),
    ],
    D=[
        arith("En un curso de 32 estudiantes, 14 dicen que suelen explotar al enojarse, 9 que suelen callar y el resto que suelen hablar con calma. ¿Cuántos hablan con calma?", "32-14-9", "Al total se le restan los otros dos grupos."),
        arith("Mateo practicó respirar y esperar 1 minuto en 3 conflictos la semana pasada y en 5 esta semana. ¿Cuántas veces lo practicó entre las dos semanas?", "3+5", "Se suman las veces de cada semana."),
    ],
    context=[ex("Valentina está muy enojada porque un compañero la culpó sin razón delante del curso. Pide un momento, sale 3 minutos, respira y luego dice: «Cuando me culpaste sin preguntar, me sentí injustamente tratada; quiero que preguntes primero». ¿Eligió una forma apropiada?", "Sí", "Se calmó primero y luego dijo hecho, emoción y petición con respeto.")],
    selfcheck=[ex("En Orientación: ¿explotar, callar y escapar son lo mismo?", "No", "Son formas distintas con impactos distintos."), ex("¿Preguntar si algo hiere a otro ayuda a decidir cómo expresarse?", "Sí", "Una buena opción no daña a nadie."), ex("¿La pausa antes de hablar puede evitar un arrepentimiento?", "Sí", "Da tiempo para elegir mejor.")],
    task=T("Lee el caso de Bruno, un estudiante inventado: sus compañeros eligieron una música para el acto y no le preguntaron; se siente ignorado y con rabia nivel 4. Completa una tabla con tres opciones (explotar, callar, expresar con respeto): qué haría Bruno en cada una y qué impacto tendría en él y en los demás. Marca la opción que elegirías y por qué.", "Explotar: gritar a todos; impacto: se asustan y él se arrepiente. Callar: no decir nada; impacto: la rabia crece y nadie sabe. Expresar: «Cuando no me preguntaron por la música, me sentí ignorado; ¿podemos votar?»; impacto: lo escuchan. Elijo la tercera porque no hiere y resuelve.", ["describe las tres opciones", "anticipa un impacto en él y otro en los demás", "elige una opción y justifica", "no cuenta una vivencia propia"], ["tabla escrita"], ["no considerar el impacto en los demás", "elegir la opción que hiere"], "Reconoce la tabla y pregunta qué señal del cuerpo avisaría que Bruno debe pedir una pausa."),
    reinforce="Describe una situación de un personaje de cuento y escribe tres formas de expresar su emoción con el impacto de cada una.",
    extend="Explica por qué actuar por impulso puede hacer que uno se arrepienta después.",
)

lesson(
    OA2, 4,
    "Una hoja y un lápiz. Las situaciones y la lista de estrategias están escritas en los ejercicios.",
    "Aprenderé a elegir y practicar una estrategia para calmarme y a saber cuándo pedir ayuda. Sirve para expresar mis emociones de forma apropiada incluso cuando son muy fuertes.",
    ["Sé comparar formas de expresar una emoción.", "Sé medir la intensidad de una emoción de 1 a 5."],
    [
        "Cuando una emoción es muy fuerte, un nivel 4 o 5, pensar con claridad cuesta más. Primero hay que calmar el cuerpo y después hablar. Hay estrategias seguras que sirven: respirar lento (por ejemplo, inhalar contando 4 y exhalar contando 6), tomar un momento aparte, tomar agua, estirar los brazos, caminar con calma o escribir lo que sientes. No todas funcionan igual para todos, por eso conviene probarlas y quedarte con las que te ayudan.",
        "Una buena estrategia respeta dos reglas: no te daña a ti ni a otros, y te permite volver a conversar o a trabajar. Golpear una pared, romper cosas o insultar no cumplen esas reglas, aunque alivien un instante. Después de calmarte, usa el mensaje «yo» para decir lo que sientes y, si hace falta, pide un acuerdo.",
        "Hay momentos en que ninguna estrategia alcanza, por ejemplo si la emoción fuerte dura muchos días o si sientes que no puedes controlarte. Ahí es importante pedir ayuda a un adulto de confianza, como alguien de tu casa, tu profesor o el orientador. Pedir ayuda es parte de cuidar tus emociones y no significa que algo esté mal contigo.",
    ],
    [("estrategia", "forma planificada de enfrentar algo"), ("respiración lenta", "inhalar y exhalar despacio para calmar el cuerpo"), ("pausa", "momento aparte para calmarme antes de hablar"), ("autorregulación", "calmar mis emociones para actuar con cuidado"), ("pedir ayuda", "contar lo que me pasa a un adulto de confianza")],
    [
        W("Elegir una estrategia segura", "Ian siente enojo nivel 5 porque perdió en un juego. Opciones: A) respirar lento y tomar agua; B) romper la hoja de puntajes; C) insultar al ganador. ¿Cuál cumple las dos reglas?", ["A no daña a nadie y le permite volver a hablar.", "B daña un objeto y C hiere a una persona.", "Solo A cumple las dos reglas."], "A"),
        W("Decidir cuándo pedir ayuda", "Rocío lleva tres semanas con rabia que no puede controlar y se pelea casi todos los días. ¿Qué acción es la más segura?", ["La emoción dura mucho y es muy fuerte.", "Las estrategias solas no alcanzan.", "Debe contarle a un adulto de confianza."], "Contarle a un adulto de confianza"),
    ],
    [
        M("Pensar que golpear algo para descargar es una buena estrategia.", "Se alivia un momento, pero se daña a sí mismo o a otros.", "Elige estrategias seguras: respirar, pausa, caminar con calma."),
        M("Creer que si necesito ayuda es porque soy débil.", "Se piensa que las emociones se deben controlar solos.", "Pedir ayuda a tiempo es cuidarse."),
    ],
    R=[
        ex("¿Respirar lento y contar es una estrategia segura para calmarse? Responde sí o no.", "Sí", "Calma el cuerpo sin dañar a nadie."),
        ex("¿Romper cosas cuando uno se enoja es una estrategia segura? Responde sí o no.", "No", "Daña objetos y puede herir a otros."),
        ex("Si una emoción fuerte dura muchos días, ¿conviene hablar con un adulto de confianza?", "Sí", "Un adulto puede ayudar cuando las estrategias no alcanzan."),
    ],
    U=[
        ex("¿Por qué conviene calmar el cuerpo antes de hablar cuando la emoción es nivel 5?", "Porque pensar con claridad cuesta cuando la emoción es muy fuerte", "Calmarse permite elegir mejor las palabras."),
        ex("¿Cuáles son las dos reglas de una buena estrategia?", "No dañar a nadie y permitir volver a conversar o trabajar", "Así se calma la emoción sin crear otro problema."),
        ex("¿Funciona igual la misma estrategia para todas las personas? Responde sí o no.", "No", "Cada persona debe probar y quedarse con las que le ayudan."),
    ],
    A=[
        ex("Lista: 1) respirar lento; 2) gritar al compañero; 3) tomar agua y estirar los brazos; 4) caminar con calma por el patio; 5) tirar la mochila contra la pared. ¿Cuántas cumplen las dos reglas?", "3", "Las opciones 1, 3 y 4 no dañan a nadie y permiten volver a hablar."),
        ex("Ema practica respiración: inhala contando 4 y exhala contando 6. ¿Cuántos segundos dura un ciclo completo de respiración?", "10", "Se suman 4 s de inhalar y 6 s de exhalar: 4 + 6 = 10."),
        ex("Un compañero está muy alterado y dice que no puede parar de llorar desde hace una semana. ¿Qué le recomiendas? A) «Aguanta». B) «Habla con un adulto de confianza; puedo acompañarte». C) «No le cuentes a nadie».", "B", "Propone apoyo adulto y compañía."),
    ],
    Z=[
        ex("¿Por qué «aguantar solo una emoción muy fuerte por mucho tiempo» no es la mejor decisión?", "Porque puede aumentar el malestar sin apoyo", "Compartirlo con un adulto de confianza ayuda a manejarlo."),
        ex("Después de calmarse, ¿qué debe hacer Ian para resolver lo que lo molestó: usar un mensaje «yo» o ignorarlo?", "Usar un mensaje «yo»", "Calmarse es el primer paso; luego se conversa para resolver."),
    ],
    D=[
        arith("Ema practicó 5 respiraciones de 10 segundos cada una. ¿Cuántos segundos respiró en total?", "5*10", "Se multiplica el número de respiraciones por su duración."),
        arith("Tomás calmó su rabia en 2 de cada 3 intentos la primera semana, y en total intentó 9 veces. ¿Cuántas veces la calmó?", "9//3*2", "Cada grupo de 3 intentos tuvo 2 éxitos: 9 ÷ 3 = 3 grupos, y 3 × 2 = 6."),
    ],
    context=[ex("Durante un juego, Joaquín siente que le sube la rabia a nivel 4. Dice «necesito un momento», se sienta aparte, respira lento y vuelve a los 3 minutos a conversar. ¿Eligió una estrategia segura?", "Sí", "Se calmó sin dañar a nadie y volvió a conversar.")],
    selfcheck=[ex("En Orientación: ¿respirar lento puede ayudar a calmar una emoción fuerte?", "Sí", "Calma el cuerpo."), ex("¿Una estrategia segura debe dañar a otros para funcionar?", "No", "No debe dañar a nadie."), ex("¿Pedir ayuda a un adulto es parte de cuidar mis emociones?", "Sí", "Es una decisión que protege.")],
    task=T("Lee el caso de Sofi, una estudiante inventada: antes de una prueba siente nervios nivel 5, le tiemblan las manos y piensa en salir corriendo. Arma un plan con cuatro pasos: (1) cómo calmar su cuerpo con una estrategia segura, (2) qué mensaje «yo» le diría a su profesora, (3) a quién pediría ayuda si los nervios fueran así todos los días y (4) cómo sabría que bajó la intensidad.", "(1) Respirar lento: inhalar contando 4 y exhalar contando 6, cinco veces. (2) «Estoy muy nerviosa antes de la prueba; ¿puedo tomar agua y empezar en un minuto?» (3) A un adulto de confianza como la orientadora. (4) Si los nervios bajan de nivel 5 a 2.", ["incluye una estrategia segura", "incluye un mensaje «yo»", "nombra un adulto de confianza", "dice cómo comprobar el cambio", "no cuenta una vivencia propia"], ["plan escrito de cuatro pasos"], ["elegir una estrategia que dañe", "no pedir ayuda cuando es frecuente"], "Reconoce el plan y pregunta qué otra estrategia podría probar si la primera no funciona."),
    reinforce="Haz una lista de cinco estrategias seguras para calmarte y marca las dos que probarías primero.",
    extend="Explica la diferencia entre calmarse y esconder una emoción.",
)

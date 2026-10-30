"""Cuaderno del estudiante, 4.º básico Orientación: OA 09 (hábitos, esfuerzo, honestidad y organización escolar)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA9 = "OR04 OA 09"


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


lesson(
    OA9, 1,
    "Una hoja y un lápiz. Los horarios y las listas están escritos en los ejercicios. No se pide comprar nada: usa los materiales que tengas.",
    "Aprenderé a organizar mi tiempo y mis materiales para estudiar mejor. Sirve para llegar preparado y sin apuros.",
    ["Sé preparar mis útiles.", "Sé proponerme una meta pequeña."],
    [
        "Organizarte significa decidir qué harás, cuánto tiempo necesitas y qué materiales usarás. Para el tiempo, puedes hacer un horario de la tarde con las tareas y su duración estimada, por ejemplo: lectura, 20 minutos; matemática, 30 minutos. Es útil empezar por lo que tiene plazo más cercano o es más difícil, y dejar pausas cortas.",
        "Para los materiales, haz una lista de lo que necesitas según el horario del día siguiente: cuadernos, estuche, libros y lo que te pidieron. Prepara la mochila la noche anterior y deja un lugar fijo para tus cosas. Así evitas buscar a última hora y llegas a tiempo.",
        "Un horario no es una prisión: se puede ajustar. Si falta un material, avisa con anticipación a tu profesora, porque no siempre depende de ti. En esta clase no se compara quién tiene más útiles. Lo importante es organizar lo que tienes de la mejor forma posible.",
    ],
    [("organizar", "ordenar mi tiempo y mis cosas para lograr algo"), ("horario", "plan que dice qué hago y a qué hora"), ("duración estimada", "tiempo que calculo que tomará una tarea"), ("prioridad", "lo que conviene hacer primero"), ("material", "cosa que necesito para trabajar, como un cuaderno")],
    [
        W("Sumar el tiempo", "Una tarde tiene lectura de 20 minutos, matemática de 30 minutos y una pausa de 10 minutos. ¿Cuánto dura en total?", ["Se suman las tres duraciones.", "20 más 30 más 10.", "El total es el tiempo de la tarde de estudio."], "60 minutos"),
        W("Lista de materiales", "Mañana tienes Lenguaje, Matemática y Artes. ¿Qué haces la noche anterior: dejar la mochila lista con lo que necesitas o buscar todo en la mañana?", ["Mirar el horario del día siguiente.", "Poner en la mochila lo necesario.", "Evita los apuros de la mañana."], "Dejar la mochila lista con lo que necesitas"),
    ],
    [
        M("Pensar que organizarme es tener muchos útiles.", "Se mide por cuántas cosas tengo.", "Se trata de usar bien lo que tengo y avisar si falta algo."),
        M("Armar un horario tan lleno que no deja pausas.", "Se cree que más tareas es mejor.", "Incluye pausas cortas y ajusta si algo cambia."),
    ],
    R=[
        ex("Un horario, ¿dice qué haces y a qué hora?", "Sí", "Ordena el tiempo."),
        ex("Preparar la mochila la noche anterior, ¿evita buscar cosas a última hora?", "Sí", "Ya está todo listo."),
        ex("¿Los horarios pueden ajustarse?", "Sí", "Se adaptan si algo cambia."),
    ],
    U=[
        ex("Si te falta un material, ¿qué haces: esperar al último momento o avisar con anticipación a tu profesora?", "Avisar con anticipación", "Así se busca una solución a tiempo."),
        ex("¿Qué es una duración estimada?", "El tiempo que calculo que tomará una tarea", "Ayuda a planear."),
        ex("¿Organizarme significa tener más útiles que los demás?", "No", "Significa usar bien lo que tengo."),
    ],
    A=[
        arith("En una tarde, Lola planea lectura de 15 minutos, escritura de 25 minutos y matemática de 30 minutos. ¿Cuántos minutos son en total?", "15+25+30", "Se suman las tres duraciones."),
        arith("Pedro tiene 90 minutos para estudiar. Ya planeó 55 minutos. ¿Cuántos minutos le quedan para planear?", "90-55", "Se resta lo planeado al total."),
        ex("Mañana tienes Matemática, Lenguaje y Educación Física. ¿Qué mochila está lista: «cuaderno de Matemática, cuaderno de Lenguaje y ropa de deporte» o «solo el estuche»?", "«Cuaderno de Matemática, cuaderno de Lenguaje y ropa de deporte»", "Cada cosa corresponde a una clase."),
    ],
    Z=[
        ex("Un niño dice: «No puedo organizarme porque no tengo todos los útiles». ¿Qué le dirías?", "Que avise a su profesora y organice lo que sí tiene", "No es su culpa y puede pedir ayuda."),
        ex("Un horario dice: tarea 3 horas sin pausas. ¿Es un buen horario?", "No", "Falta tiempo para descansar."),
    ],
    D=[
        arith("En una semana de 5 días, Ana estudia 40 minutos cada día. ¿Cuántos minutos estudia en la semana?", "40*5", "Son 40 minutos repetidos 5 días."),
        ex("Dos horarios: A) lectura 20, matemática 30, pausa 10. B) lectura 20, matemática 30, tareas extras 60, sin pausas. ¿Cuál es más realista para una tarde?", "A", "Incluye una pausa y no se sobrecarga."),
    ],
    context=[ex("Marta mira su horario del día siguiente, pone en su mochila el libro de Lenguaje y su estuche, y deja lista su ropa de deporte. ¿Se organizó?", "Sí", "Preparó sus materiales con anticipación.")],
    selfcheck=[ex("En Orientación: ¿preparar los útiles la noche anterior ayuda?", "Sí", "Evita los apuros después."), ex("¿Un horario puede ajustarse?", "Sí", "Se adapta a los cambios."), ex("¿Hay que avisar si falta un material?", "Sí", "Así se busca una solución.")],
    task=T("Arma un horario de tu tarde de lunes con tres tareas escolares (por ejemplo, lectura, matemática y escritura). Escribe la duración estimada de cada una y una pausa de 10 minutos. Suma el tiempo total. Después escribe una lista de cinco materiales que dejarías en la mochila para el martes. Si crees que podría faltarte uno, escribe a quién avisarías.", "Lectura 20 min, matemática 30 min, pausa 10 min, escritura 20 min. Total 80 min. Mochila: cuaderno, estuche, libro, ropa de deporte, botella. Aviso a mi profesora si falta algo.", ["escribe tres tareas con duración y una pausa", "suma bien el tiempo", "arma una lista de materiales y nombra a quién avisar"], ["horario escrito o dibujado"], ["horario sin pausa", "no avisar si falta algo"], "Reconoce el horario y revisa la suma."),
    reinforce="Haz un horario de una tarde con dos tareas y una pausa.",
    extend="Compara tu horario con el de un compañero y anota una idea que quieras probar.",
)

lesson(
    OA9, 2,
    "Una hoja y un lápiz. Los calendarios y planes están escritos en los ejercicios.",
    "Aprenderé a cumplir plazos con un plan que se pueda ajustar y a valorar la puntualidad. Sirve para entregar trabajos a tiempo sin angustia.",
    ["Sé organizar mi tiempo y mis materiales.", "Sé qué es un plazo."],
    [
        "La puntualidad es llegar a la hora a clases y a las actividades. Llegar a tiempo permite no perder lo que se explica y respeta a los demás. Hay causas que no dependen de ti, como el transporte o una emergencia en tu casa. Si llegaste tarde por algo que no pudiste controlar, avisa y pide ayuda; no es una falta tuya.",
        "Un plazo es el día o la hora en que debes entregar algo. Para cumplirlo, divide el trabajo en pasos y pon una fecha a cada uno. Por ejemplo, para un trabajo que se entrega el viernes: lunes, buscar información; martes, escribir; miércoles, dibujar; jueves, revisar. Así evitas dejar todo para el último día.",
        "Un plan se puede ajustar. Si un día no alcanzaste, mueve el paso al día siguiente o pide ayuda. Lo importante es avisar con anticipación si crees que no llegarás. Cumplir a tiempo es una forma de respetar el trabajo propio y el de los demás.",
    ],
    [("puntualidad", "llegar a la hora"), ("plazo", "día u hora de entrega"), ("paso", "parte pequeña de un trabajo"), ("ajustar", "cambiar el plan para que funcione mejor"), ("anticipación", "con tiempo antes de que algo ocurra")],
    [
        W("Dividir en pasos", "Un trabajo se entrega el viernes. Tienes lunes, martes, miércoles y jueves. ¿Cuántos pasos puedes planear si haces uno por día?", ["Hay 4 días antes del viernes.", "Un paso por día.", "Son 4 pasos."], "4 pasos"),
        W("Ajustar el plan", "El martes no alcanzaste a escribir. ¿Qué haces: abandonar el trabajo o mover ese paso al miércoles y avisar si necesitas ayuda?", ["Un plan se ajusta.", "Mueves el paso.", "Avisas si lo necesitas."], "Mover el paso al miércoles y avisar si necesito ayuda"),
    ],
    [
        M("Dejar todo para el último día.", "Se piensa que da tiempo.", "Divide en pasos con fechas."),
        M("Culparme por llegar tarde por el transporte.", "Se cree que todo depende de mí.", "Avisa y pide ayuda; no todo depende de ti."),
    ],
    R=[
        ex("Puntualidad, ¿es llegar a la hora?", "Sí", "Así se define."),
        ex("Un plazo, ¿es el día en que debes entregar algo?", "Sí", "Marca la entrega."),
        ex("¿Un plan puede ajustarse?", "Sí", "Se adapta si algo cambia."),
    ],
    U=[
        ex("¿Por qué conviene dividir un trabajo en pasos?", "Para no dejarlo todo para el final", "Cada paso tiene su día."),
        ex("Si llegaste tarde por el transporte, ¿es tu culpa?", "No", "No dependía de ti."),
        ex("Si crees que no llegarás al plazo, ¿qué haces?", "Aviso con anticipación", "Así se busca una solución."),
    ],
    A=[
        arith("Un trabajo tiene 5 pasos y ya completaste 3. ¿Cuántos pasos te faltan?", "5-3", "Se resta lo hecho al total."),
        arith("Un trabajo se entrega en 6 días y planeas 2 pasos por día. ¿Cuántos pasos puedes hacer en total?", "6*2", "Son 2 pasos repetidos 6 días."),
        ex("Tienes una prueba el viernes. ¿Qué plan de dos días reparte el trabajo: «miércoles repasar el cuaderno y jueves hacer ejercicios» o «jueves en la noche, todo junto»?", "«Miércoles repasar el cuaderno y jueves hacer ejercicios»", "Reparte el trabajo en pasos y fechas."),
    ],
    Z=[
        ex("Un niño dice: «Si no termino hoy, ya no sirve». ¿Es verdad?", "No", "Se puede ajustar el plan."),
        ex("Un compañero dice que estudiará todo la noche anterior. ¿Es un buen plan?", "No", "Dividir en pasos es mejor."),
    ],
    D=[
        arith("Una niña planea 15 minutos por día durante 4 días. Un día solo alcanzó 5 minutos. ¿Cuántos minutos hizo en total?", "15*3+5", "Tres días de 15 minutos y uno de 5."),
        ex("Dos planes: A) «Lo hago todo el jueves». B) «Un paso cada día y reviso el jueves». ¿Cuál es más ajustable?", "B", "Si falla un día, se mueve un paso."),
    ],
    context=[ex("Un lunes, Tomás recibe un trabajo para el viernes. Escribe en su cuaderno qué hará cada día y lo revisa el miércoles. ¿Cumplió un plan ajustable?", "Sí", "Dividió en pasos y revisó.")],
    selfcheck=[ex("En Orientación: ¿dividir en pasos ayuda a cumplir plazos?", "Sí", "Reparte el trabajo."), ex("¿Llegar tarde siempre es culpa mía?", "No", "A veces depende de otras causas."), ex("¿Puedo ajustar mi plan?", "Sí", "Un plan se adapta.")],
    task=T("Un trabajo se entrega el viernes. Arma un plan con un paso por día, de lunes a jueves. Agrega qué harías si el martes te enfermas o no puedes cumplir y a quién avisarías. Escribe también dos cosas que harías para llegar puntual a clases.", "Lunes: buscar información. Martes: escribir. Miércoles: dibujar. Jueves: revisar. Si no puedo el martes, lo muevo al miércoles y aviso a la profesora. Puntualidad: dejar la mochila lista y salir con tiempo.", ["un paso por día con fecha", "dice cómo ajustaría el plan", "incluye dos acciones de puntualidad"], ["plan escrito o dibujado"], ["dejarlo todo para el final", "no avisar"], "Reconoce el plan y revisa que se pueda ajustar."),
    reinforce="Divide un trabajo imaginario en tres pasos con fechas.",
    extend="Escribe dos cosas que te ayudarían a llegar puntual a clases.",
)

lesson(
    OA9, 3,
    "Una hoja y un lápiz. Los casos de personajes están escritos en los ejercicios.",
    "Aprenderé a respetar el estudio y el trabajo de otros. Sirve para que todos podamos concentrarnos y aprender.",
    ["Conozco el buen trato.", "Sé esperar mi turno."],
    [
        "Respetar el estudio y el trabajo de los demás significa cuidar su concentración y sus materiales. La concentración es poner la atención en una tarea. El ruido, los gritos y las interrupciones la rompen. Cuando alguien trabaja, puedes hablar en voz baja, esperar a que termine o ir a un lugar donde no moleste.",
        "También se respeta el trabajo ajeno cuando no se tocan, mueven ni rompen las cosas de otros sin permiso. Si necesitas un material, pide prestado y devuélvelo. No se miran las respuestas de otros para copiarlas ni se burlan de lo que alguien hizo. Si alguien te molesta mientras trabajas, puedes decir con respeto: «Necesito concentrarme, ¿puedes hablar más bajo?».",
        "Respetar el estudio de otros también significa valorar que cada persona tiene su propio ritmo para aprender. Unos terminan antes y otros después. El que termina antes puede ayudar o hacer algo tranquilo, sin molestar a los demás.",
    ],
    [("concentración", "poner la atención en una tarea"), ("interrupción", "cortar lo que alguien estaba haciendo o diciendo"), ("ruido", "sonido fuerte que molesta"), ("permiso", "aceptación de la otra persona para usar algo suyo"), ("ritmo", "velocidad con que cada persona trabaja")],
    [
        W("Pedir permiso", "Eli necesita el sacapuntas de Tomás. ¿Qué es respetuoso: tomarlo mientras él no mira o pedirlo prestado?", ["Tomar sin permiso no respeta.", "Pedir prestado sí.", "Devuelve lo prestado."], "Pedirlo prestado"),
        W("Decir que necesitas concentración", "Pedro conversa en voz alta cerca de Ana, que está escribiendo. ¿Qué puede decirle Ana con respeto?", ["Ana necesita concentrarse.", "Puede explicarlo con calma.", "Pedirle hablar más bajo."], "«Necesito concentrarme, ¿puedes hablar más bajo?»"),
    ],
    [
        M("Pensar que molestar a otros mientras trabajan es solo una broma.", "No se mira cómo afecta a los demás.", "Respeta su concentración y busca otro momento."),
        M("Tomar un material de un compañero sin pedir permiso.", "Se cree que no pasa nada.", "Pide prestado y devuelve."),
    ],
    R=[
        ex("¿El ruido fuerte rompe la concentración?", "Sí", "Distrae a quien trabaja."),
        ex("Pedir permiso para usar algo de otro, ¿es respetuoso?", "Sí", "Respeta lo suyo."),
        ex("¿Se puede romper el trabajo de otro sin querer y no decir nada?", "No", "Se debe reparar y avisar."),
    ],
    U=[
        ex("¿Qué haces si alguien te interrumpe mientras trabajas?", "Le pido con respeto que espere", "Así se respeta tu concentración."),
        ex("¿Por qué no se debe copiar mirando las respuestas de otro?", "Porque no es tu propio trabajo y no respeta el de él", "Respeta la autoría."),
        ex("Cuando terminas antes, ¿qué puedes hacer?", "Ayudar o hacer algo tranquilo", "Así no molestas a los demás."),
    ],
    A=[
        ex("Marta necesita el borrador de Luis. ¿Cómo lo pide con respeto: «¿Me prestas tu borrador? Te lo devuelvo» o «Dame tu borrador»?", "«¿Me prestas tu borrador? Te lo devuelvo»", "Pide y se compromete a devolver."),
        ex("Tomás terminó antes que sus compañeros. Elige qué hacer sin molestar: «leer en silencio» o «hacer ruido con el lápiz»", "Leer en silencio", "No interrumpe a otros."),
        ex("Un compañero conversa fuerte mientras Ema estudia. ¿Qué frase respetuosa puede decirle Ema: «Necesito concentrarme, ¿puedes hablar más bajo?» o «¡Cállate ya!»?", "«Necesito concentrarme, ¿puedes hablar más bajo?»", "Pide con respeto."),
    ],
    Z=[
        ex("Un niño dice: «No molesté, solo conversé fuerte». ¿Cuidó la concentración de los demás?", "No", "El ruido distrae."),
        ex("Una niña ve que otro compañero se burla del trabajo de un tercero. ¿Qué puede hacer?", "Decir que no está bien y apoyar al compañero", "Respeta el trabajo ajeno."),
    ],
    D=[
        arith("En una sala hay 28 estudiantes. Si 7 conversan fuerte, ¿cuántos estudiantes están trabajando en calma?", "28-7", "Se resta a los 28 los 7 que conversan."),
        ex("Frases: A) «Pido permiso para usar tu material». B) «Tomo tus cosas sin preguntar». C) «Hablo bajo cuando otros trabajan». ¿Cuáles respetan el trabajo ajeno?", "A y C", "La B no pide permiso."),
    ],
    context=[ex("Durante una prueba, Pía espera a que todos terminen antes de levantarse a afilar su lápiz. ¿Respetó la concentración de los demás?", "Sí", "Evitó interrumpir a otros.")],
    selfcheck=[ex("En Orientación: ¿pedir permiso respeta el trabajo ajeno?", "Sí", "Reconoce que es de otro."), ex("¿El ruido puede romper la concentración?", "Sí", "Distrae a quien trabaja."), ex("¿Copiar mirando al compañero respeta su trabajo?", "No", "No respeta la autoría.")],
    task=T("Lee: en la sala, Ema escribe un cuento, Luis mueve la silla con ruido y Rita se burla del dibujo de Pedro. Escribe qué conductas no respetan el estudio o el trabajo de otros, qué dirías o harías con cada una y una norma de curso para cuidar la concentración.", "Luis hace ruido: «¿Puedes mover la silla con cuidado?». Rita se burla: «Eso no está bien». Norma: hablamos bajo cuando otros trabajan.", ["identifica las dos conductas", "escribe una frase respetuosa para cada una", "propone una norma"], ["texto escrito o dicho"], ["justificar las conductas", "no proponer norma"], "Reconoce las conductas y revisa que las frases sean respetuosas."),
    reinforce="Escribe tres conductas que respetan la concentración de otros.",
    extend="Propón dos normas de curso para cuidar el estudio de todos.",
)

lesson(
    OA9, 4,
    "Una hoja y un lápiz. Los ejemplos de textos y trabajos están escritos en los ejercicios. No se copian obras reales: se usan textos inventados.",
    "Aprenderé a distinguir entre ayuda, copia y plagio, y a respetar la autoría. Sirve para ser honesto y aprender de verdad.",
    ["Sé respetar el trabajo de otros.", "Sé pedir ayuda."],
    [
        "La autoría es ser quien hizo un trabajo. Cuando firmas un trabajo, estás diciendo: «Esto lo hice yo». Ser honesto es decir la verdad sobre quién hizo qué. La ayuda legítima es cuando alguien te explica, te da una pista o revisa lo que hiciste, y tú haces el trabajo. Eso te permite aprender.",
        "La copia es pasar o tomar las respuestas de otro como si fueran propias, por ejemplo mirar el examen del compañero o entregar su cuaderno. El plagio es usar un texto, una imagen o una idea de otra persona como si fueran tuyas, sin decir de dónde salió. Puede ser pegar un párrafo de internet o de un libro sin mencionarlo.",
        "Cuando usas información de una fuente, haz dos cosas. Primero, escribe con tus propias palabras lo que entendiste. Segundo, di de dónde salió: «Según el libro de ciencias, la Luna…». Si necesitas ayuda, pídela sin dar tu trabajo a otro para que lo copie. Preguntar es parte de aprender.",
    ],
    [("autoría", "ser quien hizo un trabajo"), ("honestidad", "decir la verdad sobre lo que hice"), ("copia", "tomar las respuestas de otro como propias"), ("plagio", "usar un texto o una idea ajena como si fueran mías"), ("fuente", "lugar de donde saco información")],
    [
        W("Ayuda o copia", "Ana no entiende un ejercicio. Su amiga le explica el primer paso y Ana lo resuelve sola. ¿Es ayuda, copia o plagio?", ["La amiga explicó.", "Ana hizo el ejercicio.", "Es ayuda."], "Es ayuda"),
        W("Plagio", "Teo pega un párrafo de un libro en su trabajo sin decir de dónde salió. ¿Es copia o plagio?", ["Usó texto de otra persona.", "No dijo la fuente.", "Es plagio."], "Es plagio"),
    ],
    [
        M("Pasarle mi cuaderno a un compañero para que copie, porque es mi amigo.", "Se confunde ayudar con dejar que copie.", "Ayuda explicando o dando pistas; el trabajo lo hace cada uno."),
        M("Pegar un texto de internet y cambiar solo el nombre.", "Se piensa que así ya es mío.", "Escribe con tus palabras y di de dónde salió."),
    ],
    R=[
        ex("Explicar un paso a un compañero para que lo resuelva solo, ¿es ayuda?", "Sí", "Él hace el trabajo."),
        ex("Mirar el examen del compañero y copiar sus respuestas, ¿es copia?", "Sí", "Toma las respuestas de otro."),
        ex("Pegar un párrafo de un libro sin decir su fuente, ¿es plagio?", "Sí", "Usa un texto ajeno como propio."),
    ],
    U=[
        ex("En Orientación: ¿Qué es la autoría?", "Ser quien hizo un trabajo", "Es saber quién lo creó."),
        ex("Si usas información de un libro, ¿qué dos cosas haces?", "La escribo con mis palabras y digo de dónde salió", "Así evito el plagio."),
        ex("¿Pedir ayuda a una persona adulta o a un compañero es deshonesto?", "No", "Pedir ayuda es parte de aprender."),
    ],
    A=[
        ex("Clasifica: 1) un amigo te da una pista, 2) un amigo te pasa sus respuestas, 3) pegas un texto de internet sin decir la fuente. ¿Cuántas son ayuda?", "1", "Solo la primera es ayuda."),
        ex("Un libro de ciencias dice que la Luna gira alrededor de la Tierra. ¿Qué frase cita la fuente: «Según el libro de ciencias, la Luna gira alrededor de la Tierra» o «La Luna gira alrededor de la Tierra»?", "«Según el libro de ciencias, la Luna gira alrededor de la Tierra»", "Dice de dónde salió la información."),
        ex("Eli no entiende un ejercicio. ¿Qué debe hacer: pedir una pista o copiar la respuesta del compañero?", "Pedir una pista", "Así aprende y hace su trabajo."),
    ],
    Z=[
        ex("Un niño dice: «Si cambio algunas palabras del texto, ya no es copia». ¿Es correcto?", "No", "Sigue usando la idea sin decir la fuente."),
        ex("Una niña le deja copiar a una amiga porque «si no, se enoja». ¿Es una buena decisión?", "No", "Ayudar es explicar, no dejar copiar."),
    ],
    D=[
        arith("En un trabajo de 10 oraciones, 4 son copiadas de un libro sin decir la fuente. ¿Cuántas oraciones son propias?", "10-4", "Se restan las copiadas del total."),
        ex("Frases: A) «Escribo con mis palabras y cito la fuente». B) «Copio y pego». C) «Pido ayuda a mi profesora». ¿Cuáles son honestas?", "A y C", "La B es plagio."),
    ],
    context=[ex("Marta busca información sobre los volcanes, la resume con sus palabras y escribe «Según el libro de la biblioteca». ¿Evitó el plagio?", "Sí", "Usó sus palabras y citó la fuente.")],
    selfcheck=[ex("En Orientación: ¿la ayuda es lo mismo que la copia?", "No", "La ayuda explica; la copia toma respuestas."), ex("¿El plagio es usar algo ajeno como propio?", "Sí", "No dice la fuente."), ex("¿Citar la fuente ayuda a ser honesto?", "Sí", "Reconoce de dónde viene la información.")],
    task=T("Lee: Lola debe escribir tres oraciones sobre el Sol. Un libro dice: «El Sol es una estrella que da luz y calor a la Tierra». Escribe cómo lo dirías con tus propias palabras, cómo citarías la fuente y qué harías si te dan ganas de copiar. Después escribe una situación de ayuda legítima entre dos compañeros.", "Con mis palabras: El Sol es una estrella que nos da luz y calor. Cita: Según un libro de ciencias. Si quiero copiar, pido una pista. Ayuda: un compañero me explica el primer paso.", ["usa sus propias palabras", "cita la fuente", "describe una ayuda legítima"], ["texto escrito o dicho"], ["copiar el texto", "no citar"], "Reconoce la diferencia y revisa que no copie."),
    reinforce="Escribe una situación de ayuda y una de copia, y explica la diferencia.",
    extend="Reescribe con tus palabras una frase de un libro y escribe cómo citarías la fuente.",
)

lesson(
    OA9, 5,
    "Una hoja y un lápiz. Los casos y las listas están escritos en los ejercicios. Para buscar información usa un libro, la biblioteca o a una persona adulta.",
    "Aprenderé a evaluar mi esfuerzo, mi estrategia y mi siguiente paso, y a buscar información sobre temas de mi interés. Sirve para aprender con motivación y mejorar.",
    ["Sé organizarme y cumplir plazos.", "Sé citar una fuente."],
    [
        "El esfuerzo es la energía que pones en hacer algo, aunque cueste. Es distinto del resultado: puedes esforzarte mucho y que el resultado no sea el que esperabas. Una estrategia es la forma que usas para aprender, como repasar en voz alta, hacer un esquema o pedir una pista. Si una estrategia no funcionó, se cambia por otra.",
        "Para evaluar, hazte tres preguntas. ¿Cuánto me esforcé? ¿Qué estrategia usé y funcionó? ¿Cuál será mi siguiente paso? Cumplir con la tarea no siempre significa que aprendiste: hay que preguntarse qué entendiste. Y hay cosas que no dependen de ti, como no tener internet o un lugar tranquilo en tu casa. Si te pasa, avisa a tu profesora y busca otra solución; no es tu culpa.",
        "Tus intereses también son una fuente de aprendizaje. Elige un tema que te guste, como los animales, el espacio o la música. Escribe tres preguntas que quieras responder y busca información en dos fuentes, como un libro, la biblioteca o una persona adulta de confianza. Anota lo que encontraste con tus palabras y di de dónde salió. Preguntar y buscar son formas de aprender.",
    ],
    [("esfuerzo", "energía que pongo en hacer algo"), ("estrategia", "forma que uso para aprender"), ("siguiente paso", "lo próximo que haré para mejorar"), ("interés", "tema que me gusta y quiero conocer mejor"), ("fuente", "lugar de donde saco información")],
    [
        W("Evaluar con tres preguntas", "Tomás estudió 20 minutos por 3 días repasando en voz alta, y aun así tuvo algunas respuestas incorrectas. ¿Qué evalúa: esfuerzo, estrategia o siguiente paso? Escribe un siguiente paso.", ["El esfuerzo fue bueno.", "La estrategia puede mejorar.", "Siguiente paso: probar hacer un esquema."], "Esfuerzo bueno; siguiente paso: probar un esquema además de repasar en voz alta"),
        W("Buscar por interés", "Lola quiere saber más sobre los delfines. Escribe tres preguntas y dos fuentes posibles.", ["Preguntas: ¿qué comen?, ¿dónde viven?, ¿cómo se comunican?", "Fuentes: un libro y la biblioteca.", "Anotará con sus palabras y dirá la fuente."], "Tres preguntas sobre los delfines y dos fuentes: un libro y la biblioteca"),
    ],
    [
        M("Pensar que si cumplí la tarea ya aprendí.", "Se confunde terminar con entender.", "Pregúntate qué aprendiste y qué te falta."),
        M("Culparme por no tener internet o silencio en casa.", "Se cree que todo depende de mí.", "Avisa a tu profesora y busca otra solución."),
    ],
    R=[
        ex("El esfuerzo, ¿es la energía que pongo en hacer algo?", "Sí", "Aunque el resultado cambie."),
        ex("Una estrategia, ¿es la forma que uso para aprender?", "Sí", "Por ejemplo, repasar en voz alta."),
        ex("Si una estrategia no funcionó, ¿se puede cambiar?", "Sí", "Se prueba otra."),
    ],
    U=[
        ex("¿Cumplir una tarea siempre significa que aprendí?", "No", "Hay que preguntarse qué entendí."),
        ex("Si no tienes silencio en casa para estudiar, ¿es tu culpa?", "No", "Depende de condiciones fuera de tu control."),
        ex("Si eliges un tema de interés para investigar, ¿qué haces primero?", "Escribir tres preguntas", "Las preguntas guían la búsqueda."),
    ],
    A=[
        ex("Ema dibujó un esquema para estudiar y le sirvió. Eli estudió solo mirando el cuaderno y no le sirvió. ¿Qué conviene que haga Eli: probar otra estrategia, como un esquema, o repetir exactamente lo mismo?", "Probar otra estrategia, como un esquema", "Si una estrategia no funciona, se cambia por otra."),
        ex("Pedro quiere aprender sobre el espacio. ¿Qué pregunta puede investigar en una fuente: «¿Cuántos planetas hay en el sistema solar?» o «¿Es el espacio más lindo que el mar?»", "«¿Cuántos planetas hay en el sistema solar?»", "Se puede responder buscando en una fuente; la otra es solo una opinión."),
        arith("Lola buscó información en 2 fuentes y encontró 3 datos en cada una. ¿Cuántos datos anotó?", "2*3", "Son 3 datos repetidos en 2 fuentes."),
    ],
    Z=[
        ex("Un niño dice: «Me esforcé y no me fue bien, así que no sirvo». ¿Qué le dices?", "Que el esfuerzo vale y que puede cambiar la estrategia", "El resultado se puede mejorar."),
        ex("Un compañero dice: «Mi tarea está hecha, así que ya lo aprendí todo». ¿Qué le falta preguntarse?", "Qué entendí y qué me falta", "Cumplir no es lo mismo que aprender."),
    ],
    D=[
        arith("Una niña se esforzó estudiando 25 minutos durante 4 días. ¿Cuántos minutos estudió en total?", "25*4", "Son 25 minutos repetidos 4 días."),
        ex("Frases: A) «Cambio la estrategia y lo intento de nuevo». B) «Soy tonto, no puedo». C) «Avisó que no tiene silencio en casa». ¿Cuáles ayudan a aprender?", "A y C", "La B es una etiqueta."),
    ],
    context=[ex("Después de una prueba, Eli se pregunta cuánto se esforzó, qué estrategia usó y qué hará distinto. Luego elige un tema que le gusta y busca información en un libro. ¿Evaluó su esfuerzo y buscó por interés?", "Sí", "Hizo las tres preguntas y buscó información.")],
    selfcheck=[ex("En Orientación: ¿esfuerzo y resultado son lo mismo?", "No", "Puedes esforzarte y el resultado no ser el esperado."), ex("¿Puedes cambiar de estrategia?", "Sí", "Si una no funcionó, se prueba otra."), ex("¿Buscar información sobre un interés es aprender?", "Sí", "Preguntar y buscar es parte de aprender.")],
    task=T("Elige un tema que te guste (animales, música, el espacio, un deporte). Escribe tres preguntas y dos fuentes donde podrías buscar (por ejemplo, un libro o una persona adulta). Anota un dato que encuentres, con tus palabras y la fuente. Después evalúa tu esfuerzo de esta semana con tres preguntas: esfuerzo, estrategia y siguiente paso.", "Tema: delfines. Preguntas: ¿qué comen?, ¿dónde viven?, ¿cómo se comunican? Fuentes: libro y biblioteca. Dato: según un libro, muchos delfines viven en el mar. Esfuerzo: bueno. Estrategia: repasar. Siguiente paso: hacer un esquema.", ["tres preguntas y dos fuentes", "un dato con sus palabras y la fuente", "evalúa esfuerzo, estrategia y siguiente paso"], ["texto escrito o dibujado"], ["copiar el dato", "culparse por lo que no depende de uno"], "Reconoce la evaluación y revisa que cite la fuente."),
    reinforce="Escribe una pregunta sobre un tema que te interese y dónde podrías buscar la respuesta.",
    extend="Investiga una pregunta de tu tema y presenta lo que encontraste con tus palabras en tres frases.",
)

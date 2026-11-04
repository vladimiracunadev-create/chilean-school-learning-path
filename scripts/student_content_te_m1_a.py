"""Cuaderno del estudiante, 1.º medio Tecnología: OA 01 (oportunidades y necesidades para crear un servicio) y OA 02 (desarrollo ético y seguro de un servicio), clases 1 a 4 de cada OA.

Seguridad: las tareas son de lectura, cálculo y escritura; si se llega a prestar un servicio, es solo de papel, mensajes entre el propio curso o ayuda cotidiana, siempre en un lugar visible y con permiso de una persona adulta responsable.
Cifras enteras. Los casos, las encuestas, los tiempos y los precios son inventados («de ejemplo») para practicar y no nombran marcas ni personas reales. Las herramientas digitales se nombran por tipo (formulario, planilla, mensajería).
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "TE1M OA 01"
OA2 = "TE1M OA 02"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    def conv(i):
        return i if isinstance(i, dict) else ex(*i)
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": [conv(i) for i in R], "understand": [conv(i) for i in C], "apply": [conv(i) for i in A], "reason": [conv(i) for i in Z], "challenge": [conv(i) for i in D]},
        context=[conv(ctx)], selfcheck=[conv(i) for i in sc], open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )


# ------------------------------------------------------------------ OA 01, clase 1
reg(
    OA1, 1,
    materials="Hoja, lápiz y los casos escritos en este cuaderno. Si quieres, una persona de tu casa para comentar tus respuestas.",
    use="Aprenderé a distinguir un servicio de un objeto, a decir si una necesidad es personal, grupal o local y a decidir si pide crear un servicio. Sirve para elegir bien el problema antes de diseñar nada.",
    prior=["Sé que una necesidad es algo que falta o que no funciona bien.", "Sé que un usuario es quien usa un producto.", "Sé calcular un porcentaje sencillo."],
    explain=[
        "Un servicio es una actividad organizada que una persona o un equipo presta a otras personas para resolver una necesidad. A diferencia de un objeto, no se puede guardar en una repisa: se presta en el momento. Un préstamo de libros, una tutoría entre compañeros o un reparto de apuntes son servicios. Pueden apoyarse en recursos digitales (formulario, planilla, mensajería) o en otros medios (un cartel, una conversación, un cuaderno de registro).",
        "Una necesidad es algo que falta para estar seguro, para aprender o para participar. Un deseo es algo que se quiere, pero cuya falta no impide hacer lo importante. Según a cuántas personas afecta, una necesidad es personal (una persona), grupal (un grupo que se conoce, como un curso o un taller) o local (quienes comparten un lugar, como un edificio, un pasaje o una población).",
        "Hay oportunidad de crear un servicio cuando lo que falta es una actividad que alguien podría hacer: acompañar, entregar, informar, prestar o enseñar. Si lo que falta es un objeto, se piensa en un producto. Si lo que falta es un acuerdo entre personas, se conversa. Para mostrar que una necesidad es real se usan datos: un porcentaje dice cuántas personas de cada 100 la viven. Por ejemplo, 15 de 20 personas es 75 %, porque 15 × 100 ÷ 20 = 75.",
    ],
    vocab=[("servicio", "actividad que se presta a otras personas para resolver una necesidad"), ("usuario", "persona que recibe un servicio"), ("necesidad", "algo que falta para estar seguro, aprender o participar"), ("deseo", "algo que se quiere, pero no impide hacer lo importante"), ("alcance", "a cuántas personas afecta una necesidad: personal, grupal o local"), ("oportunidad", "situación que se puede mejorar con un servicio")],
    worked=[
        ("Reconocer un servicio", "En un edificio, varios adultos mayores no pueden subir las compras por la escalera. Una vecina propone que un grupo de jóvenes suba las bolsas cuando se les pida. ¿Es un servicio?", ["Reviso qué se propone: una actividad que se hace por otra persona, en el momento en que lo pide.", "No es un objeto que se guarde: es algo que alguien presta."], "Sí, es un servicio"),
        ("Decidir el alcance", "En un curso de 36 estudiantes, 9 faltaron por enfermedad y no se enteraron de las tareas. ¿Qué alcance tiene la necesidad?", ["Los afectados forman un grupo que se conoce: el curso.", "No son una sola persona ni todo un barrio."], "Es una necesidad grupal"),
    ],
    mistakes=[
        ("Decir «el servicio es la aplicación».", "La aplicación es solo un medio; el servicio es la actividad que se presta con ella.", "Describe qué actividad se hace, para quién y con qué medio."),
        ("Llamar necesidad a todo lo que se quiere.", "Un deseo no impide hacer lo importante.", "Pregunta qué pasa si falta: si no pasa nada grave, es un deseo."),
    ],
    R=[
        ("¿Qué rasgo distingue a un servicio de un objeto? A) es una actividad que se presta y no una cosa que se guarda B) siempre usa internet", "A", "Lo propio del servicio es la actividad prestada, con o sin tecnología digital."),
        ("Clasifica por alcance (personal, grupal o local): «los 25 integrantes de un taller de teatro no tienen cómo coordinar los ensayos».", "Grupal", "Afecta a un grupo que se conoce."),
        ("Una persona escribe: «Quiero que mi celular tenga otro color». ¿Es una necesidad o un deseo?", "Un deseo", "Sin ese color el celular funciona igual."),
    ],
    C=[
        ("¿En cuál caso se presta un servicio? A) una mochila nueva B) estudiantes de cursos superiores explican materia a quien lo pide, un turno por semana", "B", "Explicar materia es una actividad prestada; la mochila es un objeto."),
        ("¿En cuál caso lo que falta es una actividad que alguien presta? A) falta un candado para una bicicleta B) falta quien revise y arregle las bicicletas del barrio los sábados", "B", "Revisar y arreglar es una actividad; el candado es un objeto."),
        ("Un servicio de mensajes entre estudiantes se presta solo por chat, sin verse en persona. ¿Sigue siendo un servicio?", "Sí", "Lo que lo define es la actividad prestada, no que sea cara a cara."),
    ],
    A=[
        arith("En una encuesta de ejemplo a 50 vecinos de un edificio, 35 dicen que necesitan ayuda para subir las compras. ¿Qué porcentaje es?", "35*100//50", "Se calcula cuántos de cada 100 lo dicen.", " %"),
        ("Escribe el alcance (personal, grupal o local) de cada caso: (1) una estudiante necesita que le expliquen una materia que no entendió, (2) los 20 integrantes de un taller de música no tienen cómo repartirse los turnos de la sala, (3) en una población, las personas mayores no se enteran de los operativos de salud.", "1 personal, 2 grupal, 3 local", "La primera afecta a una persona, la segunda a un grupo conocido y la tercera a quienes comparten un lugar."),
        ("Separa necesidad de deseo: (1) una vecina en silla de ruedas necesita ayuda para cruzar una calle sin rampa, (2) un grupo quiere un afiche más colorido, (3) un adulto mayor necesita que le lleven sus remedios porque no puede salir. ¿Cuáles son necesidades?", "1 y 3", "Sin ayuda en esos dos casos se pierde seguridad o salud; el color del afiche es un gusto."),
    ],
    Z=[
        ("Equipo 1 escribe: «Queremos crear un servicio de chat para el curso». Equipo 2 escribe: «Queremos que los estudiantes ausentes reciban las tareas el mismo día». ¿Cuál enuncia la necesidad?", "Equipo 2", "La necesidad dice qué lograr; el equipo 1 ya eligió el medio."),
        ("Un grupo propone un reparto de comida por aplicación en un barrio donde 14 de 20 familias no tienen datos móviles. ¿Qué falla tiene la idea?", "No llega a la mayoría de los usuarios", "Catorce de veinte es el 70 %: la mayoría no podría usarla."),
    ],
    D=[
        arith("Se consultó a 4 grupos de 25 vecinos. 40 dijeron que necesitan ayuda con trámites en línea y 22 que necesitan ayuda con las compras; ninguno marcó ambas. Los demás no necesitan ayuda. ¿Cuántos vecinos no necesitan ayuda?", "4*25-40-22", "Se calcula el total consultado y se restan los dos grupos que sí piden ayuda.", " vecinos"),
        ("Regla: se atiende primero la necesidad que afecta a más personas y, si empatan, la de riesgo más alto. P: 40 personas, riesgo alto. Q: 55 personas, riesgo bajo. R: 55 personas, riesgo medio. S: 30 personas, riesgo alto. ¿Cuál se atiende primero?", "R", "Q y R empatan en 55 personas y R gana por su riesgo medio frente al bajo."),
    ],
    ctx=ex("En un edificio de ejemplo viven 30 adultos mayores y 24 dicen que necesitan ayuda para ir a la farmacia. ¿Qué porcentaje es y qué alcance tiene la necesidad?", "80 %; local", "Se calcula 24 × 100 ÷ 30 = 80, y todos comparten el edificio.", calc="24*100//30"),
    sc=[
        ("En Tecnología: ¿Qué es un servicio?", "Una actividad que se presta a otras personas para resolver una necesidad", "Es la definición de servicio."),
        ("Una persona quiere un color distinto para su cuaderno, ¿es necesidad o deseo?", "Deseo", "Con cualquier color puede usar el cuaderno."),
        ("¿Qué alcance tiene una necesidad de los vecinos de un pasaje?", "Local", "Comparten un lugar."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: en una sede vecinal, 3 adultos mayores no pueden inscribirse a un taller porque la inscripción es solo por formulario en línea. Caso 2: en un curso de 40 estudiantes, 30 dicen que no encuentran los apuntes cuando faltan a clases. Caso 3: en una feria de barrio, quienes llegan nuevos no saben dónde están los puestos. Escribe el alcance, si es necesidad o deseo, si pide un servicio (y por qué) y una oportunidad en una oración sin nombrar la solución.",
        "Caso 2: alcance grupal; es necesidad porque sin apuntes se pierde aprendizaje; pide un servicio (alguien que reúna y entregue los apuntes). Oportunidad: el 75 % del curso necesita recibir los apuntes cuando falta",
        ["clasifica el alcance", "distingue necesidad de deseo", "decide si pide un servicio y lo justifica", "redacta la oportunidad sin nombrar la solución"],
        ["ficha con alcance, necesidad o deseo, decisión y oportunidad"],
        ["llamar necesidad a un deseo", "nombrar la herramienta dentro de la oportunidad"],
        "Pregunta: «¿esta frase dice qué lograr o ya dice qué construir?». Si dice qué construir, pídele reescribirla.",
    ),
    reinforce="Mira tu casa, tu calle o tu curso y anota dos situaciones: una que sea necesidad y una que sea solo un deseo, explicando la diferencia.",
    extend="Piensa en una necesidad que se resuelva mejor con un acuerdo entre personas que con un servicio, y explica por qué.",
)

# ------------------------------------------------------------------ OA 01, clase 2
reg(
    OA1, 2,
    materials="Hoja, lápiz, calculadora si la necesitas y las tablas escritas en este cuaderno. Alternativa sin conexión: todo se resuelve en papel.",
    use="Aprenderé a reunir evidencia con observación, encuesta y búsqueda en fuentes, a elegir fuentes confiables y a leer los datos como porcentajes y promedios. Sirve para comprobar que una necesidad existe antes de crear un servicio.",
    prior=["Sé qué es una necesidad y cuál es su alcance.", "Sé calcular un porcentaje.", "Sé sumar y dividir con números enteros."],
    explain=[
        "Para saber si una necesidad es real se reúne evidencia. La observación anota lo que ocurre, cuántas veces y dónde. La encuesta hace las mismas preguntas, con alternativas, a muchas personas, por ejemplo con un formulario digital o una hoja de papel. La entrevista es una conversación con pocas personas para entender sus razones. También se buscan datos en fuentes escritas. Los resultados se ordenan en una tabla de frecuencias, que cuenta cuántas veces aparece cada respuesta.",
        "Una fuente es confiable si tiene autor o institución identificable, fecha, un propósito claro y datos que se pueden contrastar con otra fuente. Las personas consultadas forman la muestra. Si es muy pequeña o incluye solo a un tipo de persona, hay sesgo y el resultado engaña. Una pregunta que empuja a contestar de cierta manera también engaña. Porcentaje = cantidad × 100 ÷ total. Promedio = suma de los datos ÷ cantidad de datos.",
        "En una encuesta se aplica el principio de datos mínimos: se pide solo lo que hace falta. Si basta saber la opinión, no se pide nombre, dirección ni teléfono. Así se protege la privacidad de las personas. Y siempre conviene tener una alternativa sin conexión, como la encuesta en papel, para no dejar fuera a quien no tiene internet.",
    ],
    vocab=[("encuesta", "mismas preguntas con alternativas a muchas personas"), ("muestra", "personas consultadas"), ("sesgo", "error por consultar solo a un tipo de personas"), ("frecuencia", "cuántas veces aparece una respuesta"), ("fuente confiable", "la que tiene autor, fecha y propósito claros y datos contrastables"), ("promedio", "suma de los datos dividida entre cuántos son")],
    worked=[
        ("Calcular un porcentaje", "En una encuesta de ejemplo a 40 estudiantes, 14 prefieren recibir los avisos por chat. ¿Qué porcentaje es?", ["Multiplico 14 por 100: 1.400.", "Divido entre el total: 1.400 ÷ 40 = 35."], "35 %"),
        ("Evaluar una fuente", "Un sitio sin autor ni fecha afirma que «9 de cada 10 jóvenes quieren este servicio» y al final vende ese servicio. ¿Es confiable?", ["No tiene autor ni fecha, así que no se puede saber quién lo dice ni cuándo.", "Su propósito es vender, y la cifra no se puede contrastar con otra fuente."], "No es confiable"),
    ],
    mistakes=[
        ("Preguntar solo a mis amigos y generalizar a todo el curso.", "La muestra tiene sesgo: deja fuera a otros grupos.", "Incluye a personas de distintos grupos del lugar."),
        ("Pedir en la encuesta nombre, teléfono y dirección «por si acaso».", "No se necesitan para conocer la opinión y exponen la privacidad.", "Pide solo los datos que vas a usar."),
    ],
    R=[
        ("¿Qué técnica anota lo que ocurre sin hacer preguntas? A) la observación B) la encuesta", "A", "Observar es registrar lo que pasa, sin preguntar."),
        ("Una encuesta la responden solo 3 amigos muy cercanos. ¿Tiene sesgo?", "Sí", "Deja fuera a casi todos los demás y la muestra es muy pequeña."),
        ("Para saber qué servicio prefiere el curso, ¿qué datos debe pedir el formulario? A) solo la opción elegida B) nombre completo, teléfono y dirección", "A", "Datos mínimos: se pide solo lo necesario."),
    ],
    C=[
        ("Dos fuentes sobre el uso de bicicletas en una comuna. La primera es un informe de la municipalidad con autor, fecha del año pasado y método descrito. La segunda es una publicación anónima sin fecha que vende bicicletas. ¿Cuál es más confiable? A) la primera B) la segunda", "A", "Tiene autor, fecha y método que se pueden revisar."),
        ("Una pregunta dice: «¿No cree usted que el servicio de reparto es excelente y necesario?». ¿Qué defecto tiene? A) empuja a contestar que sí B) tiene demasiadas alternativas", "A", "La pregunta ya sugiere la respuesta que se espera."),
        ("Una encuesta tuvo 8 respuestas y 6 a favor. Otra tuvo 80 respuestas y 52 a favor. ¿Cuál aporta evidencia más sólida? A) la de 80 respuestas B) la de 8 respuestas, por tener 75 %", "A", "Una muestra mayor es más confiable que un porcentaje alto con muy pocos datos."),
    ],
    A=[
        arith("En una encuesta de ejemplo a 80 estudiantes, 36 prefieren recibir los apuntes por carpeta digital. ¿Qué porcentaje es?", "36*100//80", "Se multiplica por 100 y se divide entre el total.", " %"),
        arith("Observación de ejemplo: personas que esperan más de 10 minutos el bus, de lunes a viernes: 12, 15, 9, 14 y 10. ¿Cuál es el promedio por día?", "(12+15+9+14+10)//5", "El promedio es la suma de los datos dividida entre 5 días.", " personas"),
        ex("Tabla de ejemplo de 50 respuestas: ayuda con tareas 25, ayuda con trámites 13, ayuda con compras 7, otra 5. ¿Qué necesidad aparece más veces y qué porcentaje del total es?", "Ayuda con tareas, 50 %", "Tiene la mayor frecuencia y 25 × 100 ÷ 50 = 50.", calc="25*100//50"),
    ],
    Z=[
        ("Un equipo concluye «a todo el barrio le falta una biblioteca» porque lo respondieron 10 estudiantes del mismo curso. ¿Qué falla en su conclusión?", "La muestra es pequeña y de un solo grupo", "Diez estudiantes de un curso no representan a todo el barrio."),
        ("Una fuente dice que un servicio de reparto reduce los tiempos en 30 %, pero no indica autor, fecha ni cómo midió. ¿Qué haces antes de usar la cifra? A) buscar otra fuente que la confirme B) usarla porque trae un porcentaje", "A", "Una cifra sin autor ni método debe contrastarse antes de usarla."),
    ],
    D=[
        arith("Se encuestó a 3 cursos de 30 estudiantes. 27 eligieron mensajería, 18 llamada y los demás correo. ¿Qué porcentaje eligió correo?", "(3*30-27-18)*100//(3*30)", "Se calcula el total, se restan las otras opciones y se pasa a porcentaje.", " %"),
        ex("Dos encuestas del mismo tema: la primera tuvo 40 respuestas y 30 a favor; la segunda, 120 respuestas y 84 a favor. ¿En cuál es mayor el porcentaje a favor y por cuántos puntos?", "En la primera, por 5 puntos", "La primera es 75 % y la segunda 70 %; la diferencia es 5.", calc="30*100//40-84*100//120"),
    ],
    ctx=ex("La junta de vecinos anota qué piden 50 familias de ejemplo: 20 más iluminación, 15 mejores veredas, 10 ayuda con trámites y 5 otra cosa. ¿Qué porcentaje pidió ayuda con trámites?", "20 %", "Se calcula 10 × 100 ÷ 50 = 20.", calc="10*100//50"),
    sc=[
        ("¿Qué es una muestra?", "El grupo de personas consultadas", "Es quien aporta los datos."),
        ("¿Qué porcentaje son 15 personas de 60?", "25 %", "15 × 100 ÷ 60 = 25.", "15*100//60"),
        ("¿Qué significa el principio de datos mínimos?", "Pedir solo los datos que hacen falta", "Protege la privacidad de quienes responden."),
    ],
    open_task=(
        "Escoge un registro. Registro 1: encuesta de ejemplo a 60 estudiantes sobre un servicio de apuntes: carpeta digital 27, copias en papel 21, grupo de mensajería 12. Registro 2: observación de ejemplo de cuántos estudiantes se quedan sin sala de estudio en 5 recreos: 14, 18, 16, 20 y 17. Calcula los porcentajes (registro 1) o el promedio por recreo (registro 2), y escribe qué oportunidad detectas y si la evidencia te convence o no, y por qué.",
        "Registro 1: carpeta digital 45 %, copias 35 %, mensajería 20 %; la oportunidad es entregar los apuntes en carpeta digital, y la evidencia convence porque 60 estudiantes es una muestra razonable, aunque conviene ofrecer también copias en papel",
        ["calcula bien porcentajes o promedio", "señala la oportunidad", "juzga la evidencia (tamaño, repetición)", "propone una alternativa sin conexión o una precaución de privacidad"],
        ["hoja con cálculos y conclusión"],
        ["comparar porcentajes sin mirar el tamaño de la muestra", "olvidar a quienes no tienen internet"],
        "Pregunta: «¿cuántas personas respondieron o cuántas veces observaste?». Si no lo menciona, pídele agregarlo.",
    ),
    reinforce="Haz una mini encuesta de ejemplo con tres alternativas a cinco personas de tu casa o de tu curso, sin pedir nombres, y calcula el porcentaje de cada una.",
    extend="Explica cómo cambiarías una pregunta que empuja a responder «sí» para que sea neutra.",
)

# ------------------------------------------------------------------ OA 01, clase 3
reg(
    OA1, 3,
    materials="Hoja, lápiz y las fichas escritas en este cuaderno.",
    use="Aprenderé a describir al usuario con una ficha, a escribir una oportunidad sin nombrar la solución y a priorizar varias necesidades con una matriz con pesos. Sirve para quedar con una sola oportunidad clara.",
    prior=["Sé qué es un servicio y distingo necesidad de deseo.", "Sé calcular un porcentaje.", "Sé multiplicar y sumar enteros."],
    explain=[
        "El usuario es la persona o el grupo que recibirá el servicio. Se describe en una ficha de usuario: quién es, qué hace, dónde y cuándo vive la dificultad y qué le cuesta. La ficha se apoya en la evidencia reunida. No lleva nombres reales, direcciones ni otros datos personales: se describe un usuario tipo, como «estudiante de 1.º medio que falta por enfermedad».",
        "Una oportunidad bien escrita sigue este formato: «[Quiénes] necesitan [lograr algo] porque [evidencia]». Por ejemplo: «Los 12 adultos mayores del edificio necesitan subir sus compras sin riesgo porque 9 no pueden con la escalera». No nombra la solución: la herramienta se elige después, al diseñar. Si dice «necesitamos una aplicación», ya eligió el medio.",
        "Cuando hay varias necesidades se priorizan con una matriz con pesos. El peso dice qué tan importante es cada criterio: 3 es muy importante y 1 es poco importante. Cada necesidad recibe un puntaje de 1 a 3 en cada criterio. El total ponderado es la suma de peso × puntaje. Gana la necesidad con el total más alto. Si cambian los pesos, el resultado puede cambiar.",
    ],
    vocab=[("ficha de usuario", "descripción de quién recibe el servicio y qué dificultad tiene"), ("usuario tipo", "descripción general que no corresponde a una persona real"), ("oportunidad", "frase que dice quiénes necesitan qué y por qué"), ("peso", "importancia que se da a un criterio"), ("total ponderado", "suma de peso × puntaje de todos los criterios")],
    worked=[
        ("Escribir la oportunidad", "Evidencia de ejemplo: 10 de 25 vecinos no saben cuándo pasa el camión de la basura. Escribe la oportunidad.", ["Identifico quiénes: los vecinos. Qué lograr: saber a tiempo cuándo pasa el camión.", "Agrego la evidencia, 10 de 25 (40 %), y no nombro ninguna herramienta."], "Los vecinos necesitan saber a tiempo cuándo pasa el camión porque 10 de 25 (40 %) no lo saben"),
        ("Priorizar con pesos", "Pesos: personas afectadas 3, urgencia 2, facilidad 1. Necesidad X: puntajes 2, 1 y 3. Necesidad Y: puntajes 1, 3 y 3. ¿Cuál se prioriza?", ["X: 3×2 + 2×1 + 1×3 = 6 + 2 + 3 = 11.", "Y: 3×1 + 2×3 + 1×3 = 3 + 6 + 3 = 12."], "Se prioriza Y, con 12 puntos contra 11"),
    ],
    mistakes=[
        ("Escribir «necesitamos una página web de la feria» como oportunidad.", "Nombra la solución en vez de la necesidad.", "Escribe quiénes necesitan qué y por qué, sin nombrar la herramienta."),
        ("Poner en la ficha el nombre real y la dirección de una persona.", "Expone datos personales que no hacen falta.", "Describe un usuario tipo."),
    ],
    R=[
        ("¿Quién es el usuario de un servicio? A) quien lo recibe B) quien lo diseña", "A", "El usuario es quien recibe el servicio."),
        ("¿Qué debe llevar una oportunidad bien escrita: «quiénes, qué lograr y evidencia» o «el nombre de la herramienta»?", "Quiénes, qué lograr y evidencia", "La herramienta se elige después, al diseñar."),
        ("¿Una ficha de usuario debe incluir el nombre real y la dirección de una persona?", "No", "Son datos personales que no hacen falta; se describe un usuario tipo."),
    ],
    C=[
        ("¿Cuál es una oportunidad bien escrita? A) «Los 15 estudiantes nuevos necesitan conocer las salas el primer día porque 11 se perdieron.» B) «Hay que hacer una aplicación con un mapa del colegio.»", "A", "La primera dice quiénes, qué lograr y evidencia; la segunda ya eligió la solución."),
        ("Una ficha dice: «Marta, 14 años, vive en Los Aromos 123». ¿Qué conviene corregir? A) quitar nombre y dirección y dejar un usuario tipo B) agregar su teléfono", "A", "Los datos personales no se necesitan para diseñar el servicio."),
        ("En una matriz con pesos, ¿qué indica un peso 3 frente a uno 1? A) que el criterio es más importante B) que el criterio ya se cumplió", "A", "El peso mide la importancia del criterio."),
    ],
    A=[
        ("Dos frases: (1) «Los 20 deportistas del taller necesitan saber a tiempo si se suspende el entrenamiento.» (2) «Crear un grupo de mensajería para el taller.» ¿Cuál es la oportunidad y cuál la solución?", "1 es la oportunidad y 2 es la solución", "La primera dice quiénes necesitan qué; la segunda nombra un medio."),
        arith("Pesos: personas afectadas 3, urgencia 2, facilidad 1. La necesidad «aviso de horarios» tiene puntajes 3, 2 y 2. ¿Cuál es su total ponderado?", "3*3+2*2+1*2", "Se multiplica cada puntaje por su peso y se suman los resultados.", " puntos"),
        arith("Evidencia de ejemplo: 18 de 30 estudiantes nuevos se perdieron el primer día. ¿Qué porcentaje escribirías en la oportunidad?", "18*100//30", "Se calcula cuántos de cada 100 se perdieron.", " %"),
    ],
    Z=[
        ("Pesos: personas 1, urgencia 3, facilidad 1. Necesidad M: puntajes 3, 1, 3. Necesidad N: puntajes 1, 3, 1. ¿Cuál gana?", "N", "M suma 3 + 3 + 3 = 9 y N suma 1 + 9 + 1 = 11, porque la urgencia pesa más."),
        ("Una ficha describe a «estudiantes de 1.º medio» pero la oportunidad habla de «adultos mayores del edificio». ¿Qué incoherencia hay?", "El usuario de la ficha no coincide con quienes tienen la necesidad", "La ficha y la oportunidad deben referirse a las mismas personas."),
    ],
    D=[
        ex("Pesos: personas 3, urgencia 3, facilidad 2. Aviso de horarios: puntajes 2, 3, 3. Tutorías: 3, 2, 2. Préstamo de apuntes: 3, 3, 1. ¿Cuál tiene el total mayor y cuánto es?", "Aviso de horarios, 21", "Aviso suma 6 + 9 + 6 = 21; tutorías 9 + 6 + 4 = 19; apuntes 9 + 9 + 2 = 20.", calc="3*2+3*3+2*3"),
        ex("Un equipo obtiene estos totales para sus cuatro necesidades: 21, 19, 20 y 18. Eliminan las que quedan 2 puntos o más bajo la mayor. ¿Cuántas siguen en carrera?", "2", "Siguen 21 y 20; los totales 19 y 18 están 2 o más puntos bajo 21."),
    ],
    ctx=ex("En una escuela de ejemplo, 30 de 40 estudiantes de 1.º medio no saben dónde pedir certificados. ¿Qué porcentaje es y quiénes son los usuarios de la oportunidad?", "75 %; los estudiantes de 1.º medio", "Se calcula 30 × 100 ÷ 40 = 75, y ellos son quienes tienen la dificultad.", calc="30*100//40"),
    sc=[
        ("¿Qué es un usuario?", "La persona o el grupo que recibe el servicio", "Es quien lo usa."),
        ("¿Una oportunidad bien escrita nombra la solución?", "No", "Debe decir quiénes necesitan qué y por qué."),
        ("En una matriz con pesos, ¿qué se hace con peso y puntaje?", "Se multiplican y se suman", "Así se obtiene el total ponderado."),
    ],
    open_task=(
        "Escoge un caso con su evidencia de ejemplo. Caso 1: 12 de 30 estudiantes de un curso no saben cómo reservar la sala de computación. Caso 2: 9 de 15 adultos mayores de un edificio no pueden subir las compras. Caso 3: 18 de 24 vecinos no se enteran de las reuniones de la junta. Escribe (a) una ficha de usuario tipo sin datos personales y (b) la oportunidad en el formato «quiénes necesitan qué porque evidencia», con el porcentaje calculado, sin nombrar la solución.",
        "Caso 3: usuario tipo, vecina o vecino del barrio que trabaja y llega tarde a la reunión. Oportunidad: los vecinos necesitan enterarse a tiempo de las reuniones de la junta porque 18 de 24 (75 %) no se enteran",
        ["ficha sin datos personales", "formato quiénes-qué-porque", "porcentaje bien calculado", "no nombra la solución"],
        ["ficha y oportunidad escritas"],
        ["escribir un nombre real", "nombrar la herramienta en la oportunidad"],
        "Pregunta: «¿puedo cambiar la herramienta sin cambiar esta frase?». Si no puedes, la frase ya nombra la solución.",
    ),
    reinforce="Escribe una oportunidad con el formato «quiénes necesitan qué porque evidencia» para una situación de tu curso, con una cifra de ejemplo.",
    extend="Cambia los pesos de la matriz (por ejemplo, urgencia 1 y facilidad 3) y explica si cambia la necesidad que gana.",
)

# ------------------------------------------------------------------ OA 01, clase 4
reg(
    OA1, 4,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a generar ideas de servicio, a describir cómo se prestaría y a comprobar si es viable con restricciones, capacidad y criterios de éxito. Sirve para elegir una idea que de verdad se pueda realizar.",
    prior=["Sé escribir una oportunidad con evidencia.", "Sé calcular porcentajes.", "Sé multiplicar enteros."],
    explain=[
        "A partir de la oportunidad se piensan varias ideas de servicio. Primero se anotan sin criticar y después se filtran. Cada idea se describe con cinco datos: qué hace el servicio, quién lo presta, a quién, cuándo y por qué canal. El canal es el medio por el que el usuario pide o recibe el servicio: presencial, mensajería, formulario o cartel.",
        "Una idea es viable cuando se puede realizar con lo que se tiene. Las restricciones son los límites: tiempo, dinero, personas disponibles, acceso a internet, permisos y cuidado de datos personales. La capacidad es cuántas atenciones se pueden dar: personas que prestan × atenciones por hora × horas. Si llegan más solicitudes que la capacidad, algunas quedan sin atender.",
        "Los criterios de éxito dicen cuándo el servicio funcionó, con un indicador y un umbral, que es el valor mínimo aceptable: «al menos 80 % de las solicitudes atendidas en menos de 2 días». Se elige la idea que cumple más criterios y restricciones. Siempre se piensa una alternativa sin conexión para que nadie quede fuera por no tener internet.",
    ],
    vocab=[("canal", "medio por el que el usuario pide o recibe el servicio"), ("restricción", "límite de tiempo, dinero, personas, acceso o permisos"), ("capacidad", "cuántas atenciones puede dar el servicio"), ("indicador", "dato que permite medir si se cumple un criterio"), ("umbral", "valor mínimo aceptable de un indicador"), ("viable", "que se puede realizar con lo que se tiene")],
    worked=[
        ("Calcular la capacidad", "Tres estudiantes dan tutorías de 30 minutos, cada uno durante 2 horas por semana. ¿Cuántas tutorías pueden dar por semana?", ["En una hora, cada estudiante da 2 tutorías de 30 minutos.", "Calculo 3 estudiantes × 2 horas × 2 tutorías por hora = 12."], "12 tutorías por semana"),
        ("Comprobar un criterio de éxito", "El criterio pide al menos 80 % de solicitudes atendidas en menos de 2 días. En una prueba se atendieron 18 de 24 a tiempo. ¿Cumple?", ["Calculo el porcentaje: 18 × 100 ÷ 24 = 75.", "Comparo con el umbral: 75 es menor que 80."], "No cumple, con 75 %"),
    ],
    mistakes=[
        ("Elegir la idea más ingeniosa sin revisar las restricciones.", "Una idea brillante que no se puede realizar no resuelve la necesidad.", "Revisa tiempo, personas, dinero y acceso antes de elegir."),
        ("Escribir un criterio como «que funcione bien».", "No tiene indicador ni umbral, así que no se puede comprobar.", "Escribe una cantidad: «al menos 80 % atendidas en 2 días»."),
    ],
    R=[
        ("¿Qué es el canal de un servicio? A) el medio por el que el usuario pide o recibe el servicio B) el costo del servicio", "A", "El canal es el medio de contacto o de entrega."),
        ("¿Cuál es una restricción? A) solo hay 2 personas disponibles los miércoles B) los usuarios quedaron contentos", "A", "Una restricción es un límite de los recursos disponibles."),
        ("Un servicio de avisos necesita internet y varias familias del barrio no tienen señal. ¿Qué necesita para ser viable?", "Una alternativa sin conexión, como avisos en papel", "Así nadie queda fuera por no tener internet."),
    ],
    C=[
        ("¿Cuál es un criterio bien escrito? A) «al menos 80 % de solicitudes respondidas en 2 días» B) «que sea rápido y bueno»", "A", "Solo el primero tiene indicador y umbral comprobables."),
        ("La idea 1 necesita 5 personas y hay 3 disponibles. La idea 2 necesita 2 personas. Considerando solo ese dato, ¿cuál es viable?", "La idea 2", "Hay 3 personas: alcanzan para la idea 2 y no para la 1."),
        ("¿Por qué conviene pensar en un canal alternativo sin conexión? A) para que no queden fuera quienes no tienen internet B) para que el servicio cueste más", "A", "Un servicio justo debe poder usarlo todo el que lo necesita."),
    ],
    A=[
        arith("Un servicio de apuntes tiene 4 estudiantes que atienden 3 solicitudes por hora cada uno durante 2 horas. ¿Cuántas solicitudes puede atender?", "4*3*2", "Se multiplican personas, atenciones por hora y horas.", " solicitudes"),
        arith("Llegan 50 solicitudes por semana y el servicio puede atender 40. ¿Qué porcentaje de las solicitudes puede atender?", "40*100//50", "Se calcula cuántas de cada 100 alcanza a atender.", " %"),
        ex("Se atendieron 27 de 30 solicitudes en menos de 2 días y el umbral es 85 %. ¿Cumple el criterio y con qué porcentaje?", "Sí, con 90 %", "27 × 100 ÷ 30 = 90, que supera el 85.", calc="27*100//30"),
    ],
    Z=[
        ("Idea A: imprimir apuntes para todos (el curso tiene $0 de presupuesto y cada hoja cuesta $50). Idea B: compartir los apuntes en una carpeta digital sin costo. Con presupuesto $0, ¿cuál es viable y qué debe revisarse?", "La B; hay que revisar que todos tengan acceso a internet", "La A cuesta dinero que no hay; la B es gratis pero depende del acceso."),
        ("Un equipo elige su idea porque «a todos les pareció genial», sin medir capacidad ni costo. ¿Qué paso omitió? A) revisar restricciones y criterios de éxito B) pensar más ideas", "A", "Una idea se elige por viabilidad y criterios, no solo por entusiasmo."),
    ],
    D=[
        arith("Un servicio atiende 2 turnos semanales de 3 horas, con 2 personas por turno, y cada persona da 4 atenciones por hora. Se esperan 90 solicitudes por semana. ¿Cuántas quedan sin atender?", "90-2*3*2*4", "Se calcula la capacidad (48) y se resta de las solicitudes esperadas.", " solicitudes"),
        ("Criterios: (1) al menos 80 % atendidas en 2 días; (2) costo máximo de $2.000 por semana. Resultado de una prueba de ejemplo: 16 de 20 atendidas en 2 días y costo de $2.500. ¿Cuáles criterios se cumplen?", "Solo el 1", "16 de 20 es 80 %, que alcanza el umbral; $2.500 supera el máximo de $2.000."),
    ],
    ctx=arith("Un servicio de préstamo de libros de ejemplo tiene 3 encargados que atienden 5 préstamos por hora cada uno durante 2 horas al día. ¿Cuántos préstamos pueden atender por día?", "3*5*2", "Se multiplican encargados, préstamos por hora y horas.", " préstamos"),
    sc=[
        ("¿Qué es una restricción?", "Un límite de tiempo, dinero, personas, acceso o permisos", "Condiciona lo que se puede realizar."),
        ("¿Qué es un umbral?", "El valor mínimo aceptable de un indicador", "Permite decidir si el criterio se cumple."),
        ("¿Cómo se calcula la capacidad de un servicio?", "Personas × atenciones por hora × horas", "Indica cuántas atenciones se pueden dar."),
    ],
    open_task=(
        "Escoge una oportunidad. A: «Los 24 estudiantes de un curso necesitan recibir los apuntes cuando faltan, porque 18 no los consiguen». B: «Los 15 adultos mayores de un edificio necesitan subir sus compras sin riesgo, porque 9 no pueden con la escalera». Propón dos ideas de servicio con sus cinco datos (qué hace, quién presta, a quién, cuándo y canal), un canal alternativo sin conexión, la capacidad semanal con cifras de ejemplo y un criterio de éxito con indicador y umbral. Elige una idea y justifica con las restricciones.",
        "A: idea 1, carpeta compartida actualizada por 3 encargados; idea 2, cuaderno de apuntes en la sala. Capacidad: 3 encargados × 4 apuntes al día × 5 días = 60 apuntes por semana. Criterio: al menos 90 % de las ausencias con apuntes entregados en 2 días. Alternativa sin conexión: copias en papel. Se elige la idea 1 porque cabe en el tiempo y no cuesta dinero",
        ["describe cada idea con los cinco datos", "propone un canal sin conexión", "calcula una capacidad", "escribe un criterio con indicador y umbral", "justifica con restricciones"],
        ["hoja con dos ideas, capacidad, criterio y elección"],
        ["criterio sin umbral", "elegir sin revisar restricciones"],
        "Pregunta: «¿cómo sabrías en una semana si el servicio funcionó?». La respuesta debe ser un número.",
    ),
    reinforce="Elige un servicio cotidiano de tu barrio y anota su canal, quién lo presta, a quién y una restricción que tenga.",
    extend="Explica por qué una idea muy buena puede no ser viable y qué cambiarías para que lo fuera.",
)

# ------------------------------------------------------------------ OA 02, clase 1
reg(
    OA2, 1,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a diseñar el flujo de un servicio paso a paso, con responsables y tiempos, y a encontrar su cuello de botella. Sirve para desarrollar un servicio que se pueda prestar con orden.",
    prior=["Sé qué es un servicio y su canal.", "Sé calcular una capacidad.", "Sé sumar y dividir enteros."],
    explain=[
        "Desarrollar un servicio es definir cómo se presta, paso a paso. Las etapas habituales son: solicitud (el usuario pide), registro (se anota qué pidió), atención (se presta el servicio), entrega o cierre, y seguimiento (se pregunta si la necesidad quedó resuelta). Cada paso tiene un responsable, que es el rol que lo hace, y un tiempo estimado.",
        "El flujo se dibuja en un diagrama de flujo: los pasos van en rectángulos, las decisiones de sí o no en rombos y las flechas muestran el orden. Cada rombo debe tener una flecha para cada respuesta. El tiempo total de una solicitud es la suma de los tiempos de sus pasos en secuencia. Si cada paso lo hace una persona distinta, el servicio avanza al ritmo del paso más lento, que es el cuello de botella: solicitudes por hora = 60 ÷ minutos del paso más lento. Si dos personas hacen el mismo paso, ese paso atiende el doble.",
        "Si el servicio usa recursos digitales, se define cuáles son (formulario, planilla, mensajería) y qué se hace si fallan: el plan B puede ser un formulario en papel. Un flujo claro permite repartir roles y probar el servicio antes de abrirlo a todos.",
    ],
    vocab=[("flujo", "orden de los pasos con que se presta un servicio"), ("rol", "función que cumple cada persona del equipo"), ("diagrama de flujo", "dibujo de los pasos con rectángulos, rombos y flechas"), ("cuello de botella", "paso más lento, que limita al servicio"), ("seguimiento", "paso en que se comprueba si la necesidad quedó resuelta"), ("plan B", "forma alternativa de seguir si algo falla")],
    worked=[
        ("Sumar los tiempos", "Un servicio de préstamo tiene pasos en secuencia: registrar 2 min, buscar el libro 3 min y entregar 1 min. ¿Cuánto demora cada préstamo?", ["Los pasos ocurren uno tras otro, así que sumo sus tiempos.", "Calculo 2 + 3 + 1 = 6."], "6 minutos"),
        ("Encontrar el cuello de botella", "En un reparto de apuntes, cada paso lo hace una persona distinta: recibir 1 min, preparar 6 min y entregar 2 min. ¿Cuál es el cuello de botella y cuántas solicitudes por hora se completan?", ["El paso más lento es preparar, con 6 minutos.", "Calculo 60 ÷ 6 = 10."], "Preparar; se completan 10 solicitudes por hora"),
    ],
    mistakes=[
        ("Dejar pasos sin responsable.", "Si nadie tiene el paso a cargo, puede que nadie lo haga y las solicitudes se pierdan.", "Escribe el rol de cada paso."),
        ("Cerrar el servicio sin preguntar si la necesidad quedó resuelta.", "Falta el seguimiento, que es lo que permite mejorar.", "Agrega una etapa final de seguimiento."),
    ],
    R=[
        ("¿Qué forma lleva una decisión de sí o no en un diagrama de flujo? A) un rombo B) un rectángulo", "A", "Los rectángulos son pasos y los rombos son decisiones."),
        ("Ordena las etapas de un servicio: atención, solicitud, seguimiento, entrega y registro.", "solicitud, registro, atención, entrega, seguimiento", "Es el orden habitual de prestación y cierre."),
        ("¿Qué es el cuello de botella? A) el paso más lento, que limita al servicio B) el paso más barato", "A", "El ritmo de todo el servicio lo marca el paso más lento."),
    ],
    C=[
        ("En un servicio, el paso «registrar la solicitud» no tiene responsable. ¿Qué puede pasar? A) que nadie lo haga y se pierdan solicitudes B) que el servicio sea más rápido", "A", "Un paso sin responsable queda sin hacerse."),
        ("¿Para qué sirve el paso de seguimiento? A) para comprobar si la necesidad quedó resuelta B) para registrar de nuevo la solicitud", "A", "El seguimiento muestra si el servicio cumplió su objetivo."),
        ("Un servicio usa un formulario digital. ¿Qué plan B evita que falle si se cae internet? A) un formulario en papel B) pedir a los usuarios que vuelvan otro día", "A", "El papel permite seguir atendiendo sin conexión."),
    ],
    A=[
        arith("Un servicio de apuntes tiene pasos en secuencia: recibir 2 min, buscar 5 min, copiar 8 min y entregar 1 min. ¿Cuánto demora en total una solicitud?", "2+5+8+1", "Los pasos son secuenciales, así que se suman sus tiempos.", " minutos"),
        arith("En un servicio de reparación de mochilas, cada paso lo hace una persona distinta: recibir 3 min, reparar 12 min y entregar 2 min. ¿Cuántas solicitudes por hora puede completar?", "60//12", "Se divide la hora entre los minutos del paso más lento.", " solicitudes"),
        ("Pasos de un servicio de ejemplo: recibir 4 min, atender 10 min, entregar 5 min, uno por persona. ¿Cuál es el cuello de botella?", "Atender", "Es el paso que más demora."),
    ],
    Z=[
        ("Un equipo quiere atender 12 solicitudes por hora, pero su paso más lento demora 6 minutos y lo hace una sola persona. ¿Cuántas atiende por hora y alcanza su meta?", "10 por hora; no alcanza la meta", "60 ÷ 6 = 10, que es menos que 12."),
        ("Un diagrama tiene un rombo «¿el libro está disponible?» con una sola flecha de salida. ¿Qué falta? A) la flecha del caso «no» B) otro rectángulo al final", "A", "Un rombo necesita una salida para cada respuesta."),
    ],
    D=[
        ex("El paso más lento de un servicio demora 8 minutos y lo hace una persona; el siguiente más lento demora 5 minutos. Se suma una segunda persona al paso de 8 minutos. ¿Cuántas solicitudes por hora puede completar ahora el servicio?", "12 por hora", "Con dos personas, el paso de 8 minutos atiende 15 por hora; ahora el cuello es el paso de 5 minutos: 60 ÷ 5 = 12.", calc="60//5"),
        arith("Una prueba de ejemplo: recibir 1 min, buscar 4 min y entregar 2 min, uno por persona. Llegan 20 solicitudes por hora. ¿Cuántas quedan sin atender cada hora?", "20-60//4", "El servicio atiende 60 ÷ 4 = 15 por hora y llegan 20.", " solicitudes"),
    ],
    ctx=arith("Un reparto de apuntes de ejemplo tiene tres pasos, uno por persona: recibir 3 min, copiar 6 min y entregar 2 min. ¿Cuántas solicitudes puede completar por hora?", "60//6", "El paso más lento es copiar, con 6 minutos.", " solicitudes"),
    sc=[
        ("¿Qué forma lleva un paso en un diagrama de flujo?", "Un rectángulo", "Los rombos se reservan para las decisiones."),
        ("En Tecnología: ¿Qué es un rol?", "La función que cumple cada persona del equipo", "Asigna responsables a los pasos."),
        ("Si cada paso lo hace una persona, ¿qué paso marca el ritmo del servicio?", "El más lento", "Es el cuello de botella."),
    ],
    open_task=(
        "Escoge un servicio. A: préstamo de libros del curso. B: reparto de apuntes a quienes faltaron. C: ayuda para subir compras en un edificio. Dibuja o escribe el flujo con al menos 5 pasos (incluye solicitud, registro, atención, entrega y seguimiento), un rombo con una decisión de sí o no, el rol de cada paso, un tiempo de ejemplo para cada uno, el cuello de botella con cuántas solicitudes por hora se completan y un plan B si falla el medio digital.",
        "B: solicitud por formulario (1 min, delegada o delegado), registro en planilla (1 min, secretaria o secretario), ¿hay apuntes? sí: copiar (6 min, encargada o encargado); no: avisar a quien pidió (1 min), entregar (2 min), seguimiento (1 min). Cuello de botella: copiar, 10 solicitudes por hora. Plan B: formulario en papel",
        ["incluye las cinco etapas", "pone un rombo con ambas salidas", "asigna un rol a cada paso", "calcula el cuello de botella", "propone un plan B"],
        ["flujo escrito o dibujado con cálculos"],
        ["rombo con una sola salida", "pasos sin responsable"],
        "Pregunta: «¿quién hace este paso y qué pasa si la respuesta es no?». Revisa cada rombo.",
    ),
    reinforce="Describe un servicio que conozcas (por ejemplo, una fotocopiadora o una panadería) con sus pasos en orden y señala cuál crees que es el más lento.",
    extend="Explica qué le pasa a un servicio si se acelera un paso que no es el cuello de botella.",
)

# ------------------------------------------------------------------ OA 02, clase 2
reg(
    OA2, 2,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a cuidar la privacidad con datos mínimos y consentimiento, a respetar la autoría de lo que uso y a ser honesto con lo que prometo. Sirve para que el servicio trate bien a las personas.",
    prior=["Sé describir el flujo de un servicio.", "Sé calcular porcentajes.", "Sé qué es una fuente confiable."],
    explain=[
        "La ética es preguntarse qué es correcto para todas las personas que el servicio afecta, y no solo qué es posible hacer. En un servicio importan el respeto, la honestidad, la justicia (no dejar fuera a nadie sin razón) y el cuidado de las personas.",
        "La privacidad se cuida con los datos personales, que son los que identifican a alguien: nombre, RUT, dirección, teléfono, fotos o la voz. Se aplica el principio de datos mínimos: se pide solo lo necesario. Se pide consentimiento, que es un permiso claro y libre; si la persona es menor de edad, se pide además el de su adulto responsable. Los datos se guardan con acceso limitado y se borran cuando ya no se necesitan.",
        "La autoría exige respetar a quien creó algo. Las imágenes, la música y los textos tienen autor: se usan con permiso o con una licencia que lo permita, y se nombra a su autor o autora. Copiar un trabajo ajeno y presentarlo como propio es plagio. También es ética la honestidad: no se promete algo que el servicio no puede cumplir.",
    ],
    vocab=[("dato personal", "información que identifica a una persona"), ("datos mínimos", "pedir solo los datos necesarios"), ("consentimiento", "permiso claro y libre de la persona"), ("licencia", "permiso de uso que da quien creó una obra"), ("plagio", "presentar como propio el trabajo de otra persona"), ("honestidad", "no prometer ni decir cosas falsas")],
    worked=[
        ("Decidir qué datos hacen falta", "Un formulario de préstamo de libros pide: nombre, RUT, dirección, teléfono, curso y libro solicitado. ¿Qué datos hacen falta?", ["Para prestar, necesito saber quién retira y qué libro: el nombre (o el curso) y el libro.", "El RUT, la dirección y el teléfono no se usan para el préstamo."], "Nombre o curso y libro; sobran RUT, dirección y teléfono"),
        ("Usar una imagen ajena", "Un grupo quiere poner en su afiche una ilustración que encontró en internet, sin autor ni licencia visibles. ¿Qué hace?", ["Busca quién la creó y qué licencia tiene.", "Si no puede saberlo, no la usa: dibuja una propia o elige otra con licencia que lo permita y nombra a su autora."], "No la usa sin saber su autoría y licencia"),
    ],
    mistakes=[
        ("Pensar que una imagen es libre porque está en internet.", "Estar publicada no significa que se pueda usar sin permiso.", "Revisa la licencia y nombra al autor."),
        ("Pedir datos «por si acaso».", "Cada dato innecesario aumenta el riesgo para las personas.", "Pide solo lo que vas a usar."),
    ],
    R=[
        ("¿Qué es un dato personal? A) información que identifica a una persona, como su nombre o su foto B) cualquier número", "A", "Identificar a alguien es lo que lo hace personal."),
        ("Quieres publicar la foto de un compañero en el afiche del servicio. ¿Qué necesitas antes?", "Su permiso (consentimiento)", "Mostrar a alguien exige que lo autorice."),
        ("Datos mínimos significa: A) pedir solo los datos necesarios B) pedir los datos más cortos", "A", "El principio habla de necesidad, no de largo."),
    ],
    C=[
        ("Un servicio de tutorías pide nombre, materia y teléfono del apoderado, pero solo necesita saber nombre y materia. ¿Qué dato sobra?", "El teléfono del apoderado", "No se usa para dar la tutoría."),
        ("¿Cuál respeta la autoría? A) usar una imagen con licencia que lo permite y nombrar a su autora B) usar la imagen y no decir de dónde salió", "A", "Se usa con permiso y con crédito."),
        ("Un afiche promete «respuesta en 5 minutos» pero el equipo responde en 2 días. ¿Qué falla? A) la honestidad, porque promete algo que no cumple B) la privacidad, porque muestra datos de alguien", "A", "Prometer lo que no se cumple es faltar a la honestidad."),
    ],
    A=[
        ("Marca cuáles de estos datos son personales: (1) la opción «prefiero chat», (2) el nombre y apellido de una estudiante, (3) su dirección, (4) la cantidad de respuestas del día.", "2 y 3", "Identifican a una persona; los otros dos son datos generales."),
        arith("Un formulario de ejemplo pedía 10 datos y solo 4 eran necesarios. ¿Qué porcentaje de los datos pedidos sobraba?", "(10-4)*100//10", "Sobraban 6 de 10 datos.", " %"),
        ("El equipo quiere publicar una foto de la atención con 3 usuarios sonriendo. Dos dieron permiso y uno no. ¿Puede publicarla tal como está?", "No", "Falta el consentimiento de una de las personas."),
    ],
    Z=[
        ("Un equipo guarda durante 2 años las direcciones de todos los usuarios «por si sirven». ¿Qué principio incumple y qué debería hacer?", "Datos mínimos; borrarlas cuando ya no se necesiten", "Guardar datos que no se usan expone a las personas sin necesidad."),
        ("Quieres usar una canción conocida como fondo del video del servicio y no sabes si la licencia lo permite. ¿Qué es lo más correcto? A) buscar música con licencia que lo permita o pedir permiso B) usarla porque es solo para el curso", "A", "Que sea solo para el curso no asegura que la licencia lo permita."),
    ],
    D=[
        arith("Un formulario pide nombre (necesario), curso (necesario), RUT (no necesario), fecha de nacimiento (no necesaria), opción de servicio (necesaria) y teléfono (no necesario). Recibe 40 respuestas. ¿Cuántos datos innecesarios recogió en total?", "3*40", "Hay 3 datos innecesarios por formulario y 40 formularios.", " datos"),
        ("Un afiche tiene tres elementos: una foto de una compañera sin su permiso, una ilustración con licencia y crédito, y la promesa de «atención inmediata» que el equipo no puede cumplir. ¿Cuántos problemas éticos tiene?", "2", "La foto sin permiso y la promesa falsa; la ilustración está bien."),
    ],
    ctx=arith("Un servicio de ejemplo recibió 25 solicitudes por semana durante 4 semanas y cada formulario pedía una dirección que no era necesaria. ¿Cuántas direcciones innecesarias recogió?", "25*4", "Se multiplica la cantidad semanal por las semanas.", " direcciones"),
    sc=[
        ("En Tecnología: ¿Qué es el consentimiento?", "Un permiso claro y libre de la persona", "Es lo que se pide antes de usar sus datos o su imagen."),
        ("En Tecnología: ¿Qué es plagio?", "Presentar como propio el trabajo de otra persona", "Falta a la autoría."),
        ("¿Qué se hace con los datos cuando ya no se necesitan?", "Se borran", "Así se reduce el riesgo."),
    ],
    open_task=(
        "Revisa este caso de ejemplo. Un equipo prepara el servicio «apuntes para quienes faltan». Su formulario pide: nombre completo, RUT, dirección, teléfono, curso, fecha en que faltó y materia. Su afiche usa una foto de un compañero sin avisarle, una ilustración copiada de internet sin autor y dice «entregamos en 10 minutos» (en realidad demoran 1 día). Escribe (a) qué datos dejarías y cuáles quitarías, (b) tres problemas éticos del afiche y (c) cómo corregirías cada uno.",
        "(a) Dejo curso, fecha y materia, y un nombre o un curso para saber a quién entregar; quito RUT, dirección y teléfono. (b) Foto sin consentimiento, ilustración sin autoría ni licencia, promesa falsa. (c) Pedir permiso o usar otra foto; usar una ilustración propia o con licencia y nombrar a la autora; escribir «entregamos en 1 día»",
        ["distingue datos necesarios de innecesarios", "identifica los tres problemas", "propone una corrección para cada uno", "usa los términos consentimiento, licencia y honestidad"],
        ["hoja con la revisión y las correcciones"],
        ["dejar datos innecesarios por costumbre", "corregir la promesa sin hacerla verdadera"],
        "Pregunta: «¿qué le pasaría a esta persona si alguien más viera ese dato o esa foto?». Úsala para decidir qué quitar.",
    ),
    reinforce="Revisa un formulario o una cuenta que uses y anota qué datos pide y cuáles crees que no hacen falta.",
    extend="Explica por qué pedir permiso para usar una foto es un acto de respeto y no solo una formalidad.",
)

# ------------------------------------------------------------------ OA 02, clase 3
reg(
    OA2, 3,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a anticipar los impactos sociales, ambientales y económicos de un servicio, positivos y negativos, y a proponer medidas para reducirlos. Sirve para desarrollar un servicio que no dañe a otros.",
    prior=["Sé describir el flujo de un servicio.", "Sé cuidar los datos personales.", "Sé sumar y restar enteros."],
    explain=[
        "Todo servicio produce efectos, que se llaman impactos. Un impacto puede ser positivo (un beneficio) o negativo (un daño o un costo). Según qué afecte, es social (las personas y sus relaciones), ambiental (recursos, residuos, energía) o económico (dinero, tiempo, trabajo). También puede ser directo, si recae en el usuario enseguida, o indirecto, si llega a otras personas o más tarde. Un impacto potencial es uno que podría ocurrir, aunque todavía no haya ocurrido.",
        "Para anticiparlos se hacen preguntas a cada etapa del servicio: ¿quién gana?, ¿quién pierde o queda fuera?, ¿qué se gasta?, ¿qué se deja? Por ejemplo, un reparto en bicicleta puede reducir viajes en auto (ambiental positivo), pero aumentar el riesgo de accidentes (social negativo) y dejar fuera a quien no tiene celular (social negativo).",
        "Los impactos se ordenan en una matriz con las filas social, ambiental y económico, y las columnas positivo y negativo. Después se proponen medidas: potenciar lo positivo y reducir lo negativo. Si a cada impacto se le da un puntaje de ejemplo, el balance es la suma de los positivos menos la suma de los negativos. Un impacto negativo no obliga a cancelar el servicio: muchas veces se corrige con una medida.",
    ],
    vocab=[("impacto", "efecto que produce un servicio"), ("impacto potencial", "efecto que podría ocurrir"), ("impacto directo", "el que recae en el usuario de inmediato"), ("impacto indirecto", "el que llega a otras personas o más tarde"), ("balance", "suma de positivos menos suma de negativos"), ("medida", "acción para potenciar lo positivo o reducir lo negativo")],
    worked=[
        ("Clasificar impactos", "Un reparto de comida de barrio en bicicleta: (a) disminuye viajes en auto, (b) algunos repartidores circulan de noche sin luces, (c) adultos mayores sin celular no pueden pedir. Clasifica cada impacto.", ["(a) cuida el aire: ambiental positivo.", "(b) pone en riesgo a personas: social negativo. (c) deja gente fuera: social negativo."], "(a) ambiental positivo, (b) social negativo, (c) social negativo"),
        ("Tipo de un ahorro", "Un servicio de apuntes digitales evita 200 hojas por semana. ¿Qué tipo de impacto es?", ["Se gastan menos recursos: papel.", "Es un efecto sobre el ambiente y es beneficioso."], "Ambiental positivo"),
    ],
    mistakes=[
        ("Creer que si un servicio tiene un impacto negativo hay que cancelarlo.", "Muchos impactos negativos se reducen con una medida.", "Propón una medida para cada impacto negativo."),
        ("Pensar solo en los usuarios.", "Un servicio también afecta a quienes lo prestan, a los vecinos y al ambiente.", "Pregunta siempre quién más resulta afectado."),
    ],
    R=[
        ("Un servicio ahorra papel. ¿Qué tipo de impacto es? A) ambiental positivo B) económico negativo", "A", "Gastar menos papel cuida los recursos."),
        ("Un efecto que llega a otras personas, o más tarde, y no al usuario inmediato, ¿es directo o indirecto?", "Indirecto", "Lo directo recae enseguida en el usuario."),
        ("¿Qué significa impacto potencial? A) uno que podría ocurrir B) uno que ya ocurrió", "A", "Potencial significa posible."),
    ],
    C=[
        ("Los repartidores de un servicio trabajan 10 horas seguidas sin pausa. ¿Qué tipo de impacto es? A) social negativo B) ambiental negativo", "A", "Afecta el bienestar de las personas."),
        ("¿Qué medida reduce el impacto de dejar fuera a quienes no tienen celular? A) ofrecer también un formulario en papel B) pedir que compren celulares", "A", "Mantiene el acceso sin exigir un gasto."),
        ("¿Qué pregunta ayuda a descubrir impactos indirectos? A) ¿quién más resulta afectado además del usuario? B) ¿cuántos usuarios hay?", "A", "Los impactos indirectos recaen en otras personas."),
    ],
    A=[
        ("Clasifica cada efecto como ambiental, social o económico: (1) se gastan menos hojas, (2) los estudiantes se hacen más amigos al colaborar, (3) el curso ahorra dinero en fotocopias.", "1 ambiental, 2 social, 3 económico", "Recursos, relaciones y dinero son tipos distintos de impacto."),
        arith("Un servicio de apuntes digitales evita 120 hojas por semana durante 8 semanas, y cada hoja cuesta $10 (dato de ejemplo). ¿Cuánto dinero se ahorra?", "120*8*10", "Se multiplican hojas por semana, semanas y precio.", " pesos"),
        ("Impactos de un reparto en bicicleta: (1) menos viajes en auto, (2) riesgo de accidentes, (3) menos gasto en bencina. ¿Cuáles son negativos?", "Solo el 2", "El riesgo de accidentes es un daño; los otros dos son beneficios."),
    ],
    Z=[
        ("Un equipo dice: «Nuestro servicio no tiene impactos negativos porque es gratis». ¿Qué error tiene? A) un servicio gratis igual puede excluir, gastar recursos o afectar a otros B) los servicios gratis siempre dañan", "A", "La gratuidad no elimina los otros impactos."),
        ("Un servicio de reparto reduce 30 viajes en auto por semana, pero entrega todo en bolsas plásticas desechables. ¿Qué medida reduce el impacto negativo sin perder el positivo? A) entregar en bolsas reutilizables B) cancelar el reparto", "A", "Corrige el problema sin eliminar el beneficio."),
    ],
    D=[
        arith("Puntajes de ejemplo: los impactos positivos suman 5, 4 y 3, y los negativos suman 2 y 6. ¿Cuál es el balance?", "5+4+3-2-6", "Balance = positivos menos negativos.", " puntos"),
        arith("Un servicio tiene balance 4. Con una medida, un impacto negativo baja de 6 a 2 puntos. ¿Cuál es el nuevo balance?", "4+6-2", "Los negativos bajan 4 puntos, así que el balance sube 4.", " puntos"),
    ],
    ctx=ex("Un servicio vecinal de ejemplo presta mesas plegables: 15 familias dejaron de comprar una de $20.000. ¿Cuánto dinero evitaron gastar y de qué tipo es el impacto?", "300.000 pesos; económico positivo", "15 × 20.000 = 300.000 y se trata de dinero.", calc="15*20000"),
    sc=[
        ("¿Qué es un impacto indirecto?", "El que llega a otras personas o más tarde", "No recae enseguida en el usuario."),
        ("Un servicio genera muchos residuos, ¿qué tipo de impacto es?", "Ambiental negativo", "Afecta los recursos y el ambiente."),
        ("¿Cómo se calcula el balance?", "Positivos menos negativos", "Muestra si pesan más los beneficios."),
    ],
    open_task=(
        "Analiza este servicio de ejemplo: «reparto de comida del barrio en bicicleta, de 18:00 a 21:00, con pedidos por celular». Completa una matriz con al menos un impacto social, uno ambiental y uno económico (positivos o negativos), indica cuáles son indirectos, y propone una medida para cada impacto negativo. Calcula el balance con puntajes de ejemplo de 1 a 5.",
        "Social negativo: adultos mayores sin celular quedan fuera (3 puntos); medida: pedidos también por teléfono fijo o en papel. Ambiental positivo: menos viajes en auto (4). Económico positivo: ingreso para los repartidores (4). Social negativo, riesgo nocturno (3); medida: luces, chaleco y horario hasta las 20:00. Balance: 4 + 4 − 3 − 3 = 2. Indirectos: el efecto en el aire y el ingreso de los repartidores llegan a otras personas y más tarde",
        ["incluye los tres tipos de impacto", "distingue positivo de negativo", "propone una medida para cada negativo", "calcula el balance"],
        ["matriz con medidas y balance"],
        ["olvidar a quienes quedan fuera", "medida que no se relaciona con el impacto"],
        "Pregunta: «¿esta medida reduce exactamente el impacto que anotaste?». Si no, pídele ajustarla.",
    ),
    reinforce="Elige un servicio que uses (por ejemplo, un reparto o una biblioteca) y anota un impacto positivo y uno negativo.",
    extend="Explica por qué dos personas pueden valorar distinto el balance del mismo servicio.",
)

# ------------------------------------------------------------------ OA 02, clase 4
reg(
    OA2, 4,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a aplicar normas de cuidado y seguridad digital y presencial, a probar el servicio con un piloto y a actuar con un protocolo ante un problema. Sirve para prestar el servicio sin poner en riesgo a nadie.",
    prior=["Sé cuidar datos personales.", "Sé anticipar impactos.", "Sé calcular porcentajes."],
    explain=[
        "La seguridad digital protege a las personas y a sus datos. Se usan contraseñas largas, distintas para cada cuenta y que no se comparten ni se escriben en el chat. Al terminar en un equipo compartido se cierra la sesión. No se abren enlaces dudosos. Nunca se pide ni se anota la clave de un usuario: si hay que ingresar a su cuenta, lo hace él o ella. Los datos se guardan en un lugar con acceso limitado y, cuando se puede, se usan recursos que no exigen cuenta.",
        "La seguridad física importa si el servicio es presencial: se presta en un lugar visible, con otras personas del equipo presentes y con el permiso de la escuela o de una persona adulta responsable. Nadie atiende solo a una persona desconocida. Al usar pantallas se hacen pausas y se cuida la postura.",
        "Cuando ocurre un problema se sigue un protocolo, que es una secuencia acordada de pasos: no responder a quien ofende o presiona, guardar evidencia (por ejemplo una captura), bloquear si corresponde y avisar a una persona adulta responsable. No se borra el chat y nunca se guarda ni se reenvía una imagen íntima de nadie. Nunca se enfrenta solo a alguien ni se guarda un secreto. Antes de abrir el servicio a todos se hace una prueba piloto con un grupo pequeño para descubrir fallas y riesgos.",
    ],
    vocab=[("contraseña segura", "clave larga, distinta para cada cuenta y no compartida"), ("acceso limitado", "solo entran quienes lo necesitan"), ("protocolo", "secuencia acordada de pasos ante un problema"), ("evidencia", "registro que muestra lo ocurrido, como una captura"), ("prueba piloto", "ensayo del servicio con un grupo pequeño"), ("riesgo", "posibilidad de que algo cause daño")],
    worked=[
        ("Elegir una contraseña", "Dos contraseñas de ejemplo: «maria2010» y «Cuaderno-azul-lluvia-47». ¿Cuál es más segura?", ["«maria2010» es corta y usa un nombre y un año fáciles de adivinar.", "La otra es larga y mezcla palabras, mayúscula, guiones y números."], "«Cuaderno-azul-lluvia-47»"),
        ("Actuar ante un mensaje extraño", "Una persona desconocida escribe al chat del servicio y pide la dirección de un usuario. ¿Qué hace el equipo?", ["No responde ni entrega ningún dato, y guarda una captura del mensaje.", "Avisa a la persona adulta responsable y bloquea a quien escribió."], "No entrega datos, guarda evidencia, bloquea y avisa a una persona adulta responsable"),
    ],
    mistakes=[
        ("Compartir la contraseña del servicio por el chat del equipo «para que todos entren».", "Cualquiera que vea el chat podría usarla.", "Usa cuentas con acceso limitado y no compartas claves por mensajes."),
        ("Enfrentar a quien molesta o guardar el problema en secreto.", "Puede empeorar la situación o dejarte sin ayuda.", "Sigue el protocolo y avisa a una persona adulta responsable."),
    ],
    R=[
        ("¿Cuál contraseña es mejor? A) «Luna-verde-tren-52» B) «123456»", "A", "Es larga y difícil de adivinar."),
        ("Si alguien desconocido pide datos de un usuario, ¿qué haces: entregarlos o avisar a una persona adulta responsable?", "Avisar a una persona adulta responsable", "No se entregan datos de otros a desconocidos."),
        ("En un equipo compartido, al terminar, ¿qué haces? A) cerrar la sesión B) dejarla abierta para el siguiente", "A", "Si no, otra persona puede entrar a tu cuenta."),
    ],
    C=[
        ("Un servicio presencial de ayuda a adultos mayores se hará en un lugar apartado con una sola persona del equipo. ¿Qué cambio lo hace más seguro? A) hacerlo en un lugar visible, con varias personas del equipo y permiso del colegio B) dejar que atienda la persona con más experiencia", "A", "La visibilidad, la compañía y el permiso protegen a todos."),
        ("¿Para qué sirve una prueba piloto? A) para detectar fallas y riesgos con un grupo pequeño antes de abrir el servicio B) para anunciar el servicio", "A", "Permite corregir antes de que muchas personas usen el servicio."),
        ("Alguien del equipo recibe un enlace dudoso en el chat. ¿Qué hace? A) no lo abre y avisa al resto y a la persona adulta responsable B) lo abre para comprobar", "A", "Abrirlo podría poner en riesgo los datos del equipo."),
    ],
    A=[
        ("Prácticas observadas: (1) contraseña compartida por todo el grupo, (2) sesión cerrada al terminar, (3) enlace dudoso abierto «para ver qué era», (4) datos guardados en una carpeta con acceso limitado. ¿Cuáles son riesgos?", "1 y 3", "Compartir la clave y abrir enlaces dudosos exponen las cuentas."),
        arith("En una prueba piloto de ejemplo se detectaron 8 fallas de seguridad y se corrigieron 6. ¿Qué porcentaje queda sin corregir?", "(8-6)*100//8", "Quedan 2 de 8 fallas.", " %"),
        ("Las claves del equipo tienen 4, 6, 12 y 14 caracteres y la norma pide al menos 12. ¿Cuántas claves cumplen?", "2", "Solo las de 12 y 14 caracteres alcanzan el mínimo."),
    ],
    Z=[
        ("Un equipo guarda las solicitudes con nombres de usuarios en una carpeta que abre cualquiera que tenga el enlace. ¿Qué norma incumple y cómo se corrige?", "Acceso limitado; restringirlo a quienes lo necesitan", "Los datos personales deben verlos solo quienes los usan."),
        ("Durante la prueba piloto, una usuaria cuenta que otro estudiante le exige no decir nada de lo ocurrido en el chat. ¿Qué debe hacer ella? A) contarlo a una persona adulta de confianza B) guardar el secreto", "A", "Los secretos que presionan o dan miedo se cuentan a una persona adulta."),
    ],
    D=[
        arith("Un servicio presencial tiene 6 integrantes. La norma exige que en cada atención haya al menos 2 personas del equipo. ¿Cuántas atenciones al mismo tiempo se pueden hacer como máximo?", "6//2", "Con 6 integrantes se forman 3 parejas.", " atenciones"),
        arith("En un piloto de 40 solicitudes, 3 usuarios entregaron datos innecesarios y 5 tuvieron demoras de más de 2 días; ninguno estuvo en ambos grupos. ¿Cuántas solicitudes quedaron sin esos problemas?", "40-3-5", "Se restan los dos grupos con problemas.", " solicitudes"),
    ],
    ctx=ex("Un equipo de ejemplo tiene 4 cuentas con claves de 8 caracteres y 6 con claves de 14. La norma pide al menos 12. ¿Qué porcentaje de las claves cumple?", "60 %", "Cumplen 6 de 10 claves: 6 × 100 ÷ 10 = 60.", calc="6*100//10"),
    sc=[
        ("¿Qué es un protocolo?", "Una secuencia acordada de pasos ante un problema", "Evita improvisar cuando algo sale mal."),
        ("¿Para qué sirve una prueba piloto?", "Para detectar fallas y riesgos con un grupo pequeño", "Se corrige antes de abrir el servicio a todos."),
        ("Ante un mensaje que te presiona o te da miedo, ¿qué haces?", "Avisas a una persona adulta de confianza", "Nunca se enfrenta ni se guarda el secreto."),
    ],
    open_task=(
        "Escribe el manual de cuidado y seguridad de este servicio de ejemplo: «ayuda presencial con trámites en línea para adultos mayores del barrio, en la sede vecinal, los sábados». Incluye (a) tres normas de seguridad digital, (b) tres normas de seguridad física, (c) un protocolo de cuatro pasos ante un mensaje ofensivo en el chat del servicio y (d) cómo harías una prueba piloto con 5 personas y qué medirías.",
        "(a) Claves largas y distintas, sin pedir ni anotar las de los usuarios; no abrir enlaces dudosos; cerrar sesión al terminar. (b) Lugar visible; al menos dos integrantes por atención; permiso de la sede y de una persona adulta responsable. (c) No responder, guardar captura, bloquear, avisar a una persona adulta responsable. (d) 5 atenciones; medir fallas de seguridad detectadas y satisfacción",
        ["tres normas digitales", "tres normas físicas", "protocolo con avisar a una persona adulta", "piloto con algo medible"],
        ["manual de una hoja"],
        ["protocolo que enfrenta al agresor", "piloto sin medición"],
        "Pregunta: «¿en qué paso del protocolo se avisa a una persona adulta?». Debe estar presente.",
    ),
    reinforce="Revisa tus contraseñas más usadas y anota cuáles cambiarías por una frase larga, sin escribirlas aquí.",
    extend="Explica por qué una prueba piloto con pocas personas es mejor que abrir el servicio a todos desde el primer día.",
)

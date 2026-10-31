"""Cuaderno del estudiante, 5.º básico Historia, Geografía y Ciencias Sociales: OA 21 (evaluar soluciones y justificar su elección)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA21 = "HI05 OA 21"


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def tiers(recovery, understand, apply, reason, challenge):
    return {"recovery": recovery, "understand": understand, "apply": apply, "reason": reason, "challenge": challenge}


register(
    OA21, 1,
    materials="Este cuaderno y un lápiz. Los casos (escuelas y barrios inventados) están escritos en los ejercicios.",
    use="Aprenderé a describir con claridad un problema: qué ocurre, dónde, desde cuándo y a quiénes afecta. Sirve para que las soluciones que se propongan sirvan de verdad para ese problema.",
    prior=["Sé ubicar un tema en el tiempo y el espacio.", "Sé distinguir causas, actores y consecuencias.", "Sé usar un dato como evidencia."],
    explain=[
        "Un problema es una situación que afecta a personas y que se quiere mejorar. Antes de pensar en soluciones hay que describirlo bien. Me pregunto: ¿qué ocurre?, ¿dónde?, ¿desde cuándo?, ¿a quiénes afecta? y ¿cómo lo sé? La última pregunta pide evidencia, como un conteo, una observación o lo que dice una fuente. Un problema bien descrito evita elegir soluciones que no se relacionan con él.",
        "No hay que confundir el problema con la solución. «Falta un techo en el patio» ya contiene una solución escondida. El problema es: «Cuando llueve, el patio de la Escuela Los Aromos (inventada) se llena de charcos y el curso no puede jugar». Si describo así el problema, puedo proponer varias soluciones distintas: un canal, un recreo bajo techo o plantas que absorban agua.",
        "También conviene delimitar el problema, es decir, decir hasta dónde llega. No es lo mismo un problema de un curso que uno de toda la comuna. Delimitar el lugar, el tiempo y las personas afectadas ayuda a no prometer más de lo que una solución puede lograr. Si el patio se inunda, no necesito arreglar toda la escuela.",
    ],
    vocab=[("problema", "situación que afecta a personas y que se quiere mejorar"), ("solución", "acción que busca resolver un problema"), ("delimitar", "decir hasta dónde llega un problema"), ("afectados", "personas a las que el problema perjudica"), ("evidencia", "dato u observación que muestra que el problema existe")],
    worked=[
        W("Problema o solución", "¿Es «Falta un techo en el patio» un problema bien descrito?",
          ["Veo si nombra una situación o una solución.", "«Falta un techo» sugiere construir un techo.", "No dice qué ocurre ni a quiénes afecta."], "No, porque ya contiene una solución y no describe qué ocurre"),
        W("Describir con cinco preguntas", "Escuela Los Aromos (inventada): cuando llueve se forman charcos en el patio desde hace dos meses. Los 120 estudiantes no pueden jugar afuera. Responde qué, dónde, desde cuándo y a quiénes afecta.",
          ["Qué: se forman charcos.", "Dónde: patio de la escuela.", "Desde cuándo y a quiénes: dos meses; 120 estudiantes."], "Charcos; patio; dos meses; 120 estudiantes"),
    ],
    mistakes=[
        M("Escribir el problema como si fuera una solución.", "Así se descartan otras soluciones posibles.", "Describe qué ocurre y a quién afecta, sin decir cómo arreglarlo."),
        M("Hablar del problema sin ningún dato.", "No se sabe si existe ni qué tan grande es.", "Agrega una observación, un conteo o una fuente."),
    ],
    tiers=tiers(
        [ex("En Ciencias Sociales, ¿qué es un problema?", "Una situación que afecta a personas y que se quiere mejorar", "Así se define en esta clase."),
         ex("De las cinco preguntas para describir un problema, ¿cuál pide el lugar donde ocurre?", "¿Dónde?", "Pregunta por el lugar."),
         ex("Frase: «Cuando llueve, el patio tiene charcos». ¿Dice qué ocurre o propone una solución?", "Dice qué ocurre", "Describe la situación sin proponer acciones.")],
        [ex("¿Por qué no hay que confundir el problema con la solución?", "Porque la solución escondida impide ver otras posibilidades", "Se pierde la oportunidad de comparar."),
         ex("¿Qué significa delimitar un problema?", "Decir hasta dónde llega", "Fija el lugar, el tiempo y las personas."),
         ex("¿Para qué sirve la pregunta «¿cómo lo sé?»", "Para pedir evidencia de que el problema existe", "Evita problemas inventados.")],
        [ex("Elige el problema bien descrito: A) «Hay que comprar más basureros.» B) «En la plaza del barrio se acumula basura desde el verano y los vecinos sienten mal olor.»", "B", "Dice qué, dónde, desde cuándo y a quiénes."),
         arith("Hubo charcos en el patio durante 3 semanas, con 4 días de lluvia por semana. ¿Cuántos días de lluvia hubo en total?", "3*4", "Se repite la misma cantidad cada semana.", unit=" días"),
         ex("«El kiosco de la escuela cierra a las 10:00 y 80 estudiantes quedan sin colación». ¿A quiénes afecta el problema?", "A los 80 estudiantes", "Son las personas afectadas.")],
        [ex("Lola dice que el problema es «falta un semáforo». ¿Cómo lo reescribes sin dar la solución, si en la esquina de su escuela hay muchos autos y los niños cruzan con miedo?", "En la esquina hay muchos autos y los niños cruzan con miedo", "Describe lo que ocurre y no la solución."),
         ex("Un grupo dice que el problema «es de todo Chile» pero solo observó una cancha de su barrio. ¿Qué error cometió?", "No delimitó el problema", "Habló de más personas y lugares que los observados.")],
        [arith("En un curso de 36 estudiantes, 9 dicen que no tienen dónde guardar su abrigo. ¿Cuántos estudiantes sí tienen dónde guardarlo?", "36-9", "Se resta quienes no tienen del total.", unit=" estudiantes"),
         ex("Ordena para describir bien: A) desde hace un mes, B) se forma una fila larga en el kiosco, C) los estudiantes de 5.º pierden parte del recreo.", "B, A, C", "Primero qué, luego desde cuándo y luego a quiénes afecta.")],
    ),
    context=[ex("En tu curso nadie ordena la sala al terminar el día y los materiales se pierden. Escribe una frase que describa el problema sin proponer solución.", "Por ejemplo: Al terminar el día la sala queda desordenada y los materiales se pierden", "Describe la situación sin decir cómo arreglarla.")],
    selfcheck=[ex("En Ciencias Sociales: ¿qué son los afectados por un problema?", "Las personas a las que el problema perjudica", "Hay que conocerlos para buscar soluciones."), ex("¿Qué es delimitar?", "Decir hasta dónde llega un problema", "Ayuda a no prometer de más."), ex("¿Qué se pregunta para pedir evidencia?", "Cómo lo sé", "Pide datos que muestren el problema.")],
    open_task=task("Elige una situación: A) el kiosco de una escuela tiene filas largas, B) una esquina peligrosa cerca de un colegio, C) una plaza con luces apagadas. Escribe el problema con las cinco preguntas (qué, dónde, desde cuándo, a quiénes y cómo lo sé), inventando datos razonables. No escribas ninguna solución.", "Tema A. Qué: filas largas. Dónde: kiosco. Desde cuándo: este mes. A quiénes: 60 estudiantes. Cómo lo sé: conté 25 en la fila.", ["cinco preguntas respondidas", "un dato como evidencia", "sin solución escondida"], ["descripción del problema en cinco partes"], ["mezclar el problema con la solución", "no poner ningún dato"], "Muestra tu descripción a una persona de tu casa y pídele que diga qué falta."),
    reinforce="Elige algo que moleste en tu barrio y cuéntalo a una persona de tu casa con qué, dónde y desde cuándo.",
    extend="Escribe dos problemas con solución escondida y reescríbelos como problemas bien descritos.",
)

register(
    OA21, 2,
    materials="Este cuaderno y un lápiz. Los datos, las notas y las encuestas inventadas están escritos en los ejercicios.",
    use="Aprenderé a reunir información confiable para saber qué soluciones son posibles y qué se necesita para cada una. Sirve para elegir con datos y no por simple simpatía.",
    prior=["Sé describir un problema con cinco preguntas.", "Sé revisar la procedencia de una fuente."],
    explain=[
        "Para evaluar soluciones necesito información. Hay varias formas de obtenerla. Puedo observar el lugar y anotar lo que veo; puedo hacer una encuesta, que es preguntar lo mismo a varias personas; puedo leer un informe o un mapa; y puedo preguntar a una persona que sabe del tema, como un maestro o una encargada del municipio. Cada forma entrega un tipo distinto de dato.",
        "No toda información sirve igual. Pregunto: ¿viene de una fuente con autor y fecha?, ¿es actual?, ¿mide lo que necesito? Por ejemplo, una encuesta a solo 3 personas dice poco. Una encuesta a todo un curso de 30 estudiantes dice más del curso. También separo datos de opiniones: «El patio tiene 5 charcos» es un dato, y «el patio es horrible» es una opinión.",
        "Con esa información ordeno lo que cada solución necesita: tiempo, dinero, personas y permisos. Por ejemplo, un canal de desagüe puede requerir ayuda de personas expertas y permiso de la escuela. Una campaña de limpieza necesita voluntarios. Anotar los requisitos de cada solución me ayuda a compararlas después con justicia.",
    ],
    vocab=[("encuesta", "pregunta igual hecha a varias personas"), ("observación", "mirar con atención y anotar lo que se ve"), ("dato", "información que se puede comprobar"), ("requisito", "lo que se necesita para que una solución funcione"), ("actualizada", "que corresponde a un tiempo reciente")],
    worked=[
        W("Elegir la forma de reunir información", "Quieres saber cuántos estudiantes de tu curso prefieren un recreo extra de lectura. ¿Observas el patio, haces una encuesta o lees un mapa?",
          ["Quiero saber preferencias de varias personas.", "Una encuesta pregunta lo mismo a todos.", "Un mapa no entrega preferencias."], "Hacer una encuesta"),
        W("Separar dato de opinión", "«El patio tiene 5 charcos» y «el patio es horrible». ¿Cuál es un dato?",
          ["Veo si se puede comprobar.", "Se pueden contar los charcos.", "«Horrible» es lo que alguien siente."], "«El patio tiene 5 charcos»"),
    ],
    mistakes=[
        M("Decidir con la opinión de una sola persona.", "Una persona no representa a todo el grupo.", "Reúne datos de varias personas o de una fuente confiable."),
        M("Mezclar datos con opiniones sin distinguirlas.", "Se toman decisiones con sensaciones.", "Marca qué parte se puede comprobar."),
    ],
    tiers=tiers(
        [ex("En Ciencias Sociales: ¿qué es una encuesta?", "Hacer la misma pregunta a varias personas", "Así se reúne la opinión de un grupo."),
         ex("«El pasillo mide 12 pasos» ¿es un dato o una opinión?", "Un dato", "Se puede contar."),
         ex("¿Qué es un requisito de una solución?", "Lo que se necesita para que funcione", "Por ejemplo, personas o permisos.")],
        [ex("¿Por qué una encuesta a solo 3 personas dice poco del curso?", "Porque no representa a todo el curso", "Muy pocas personas no muestran al grupo."),
         ex("Quieres saber cuántos autos pasan por una calle en 20 minutos. ¿Qué forma de reunir información usas: observar y contar, o hacer una encuesta?", "Observar y contar", "Se puede ver y contar sin preguntar a nadie."),
         ex("¿Qué se pregunta sobre una fuente para saber si es confiable?", "Quién la hizo, cuándo y si mide lo que necesito", "La procedencia entrega confianza.")],
        [ex("Elige la información más útil para saber si los estudiantes quieren un huerto escolar: A) una encuesta al curso con 28 respuestas, B) un comentario anónimo en una pared.", "A", "Reúne varias respuestas y se puede contar."),
         arith("En una encuesta del curso, 17 estudiantes votaron por un huerto y 11 por una biblioteca de aula. ¿Cuántos estudiantes respondieron en total?", "17+11", "Se suman los votos de ambas opciones.", unit=" estudiantes"),
         ex("El canal de desagüe necesita una persona experta, un permiso del colegio y dinero para materiales. Una campaña de limpieza necesita solo voluntarios. ¿Cuál de las dos exige más requisitos?", "El canal de desagüe", "Tiene tres requisitos y la campaña tiene uno.")],
        [ex("Un compañero dice: «El 100 % de las personas está de acuerdo» porque preguntó a su mejor amigo. ¿Qué error tiene?", "Preguntó a una sola persona que no representa al grupo", "El dato es muy pequeño."),
         ex("Un afiche de 2005 sin autor dice cuántos autos pasan por una calle. ¿Por qué es débil esa fuente para saber cuántos pasan hoy?", "No tiene autor y no está actualizada", "Falta procedencia y actualidad.")],
        [arith("En otra encuesta votaron 14 estudiantes por «más juegos» y 9 por «más sombra». ¿Cuántos votos más tiene «más juegos»?", "14-9", "Se resta la menor cantidad de la mayor.", unit=" votos"),
         ex("Para saber cuántos autos pasan por la calle, ¿qué es más confiable: A) un conteo propio de 30 minutos anotado con fecha y hora o B) un rumor escuchado en el recreo?", "A", "Se anotó con fecha y se puede comprobar.")],
    ),
    context=[ex("Quieres saber si hay peligro en la esquina de tu escuela. ¿Qué haces: observar en distintos horarios y anotar, o preguntar solo a un amigo?", "Observar en distintos horarios y anotar", "Reúne datos propios y comprobables.")],
    selfcheck=[ex("En Ciencias Sociales: ¿qué es un dato?", "Información que se puede comprobar", "Se distingue de una opinión."), ex("En Historia: ¿qué es una observación?", "Mirar con atención y anotar lo que se ve", "Es una forma de reunir información."), ex("¿Qué es un requisito?", "Lo que se necesita para que una solución funcione", "Se anota para comparar soluciones.")],
    open_task=task("Elige un problema: A) un patio con charcos, B) una biblioteca de curso desordenada, C) una calle con mucho ruido en la hora de salida. Escribe tres formas de reunir información (por ejemplo, observar algo y anotarlo, hacer una pregunta de encuesta y buscar una fuente), qué fuente con autor y fecha buscarías y qué sería un dato y qué sería una opinión en tu tema.", "Tema B. Observaría cuántos libros están en el suelo, preguntaría a 20 compañeros si encuentran los libros y buscaría el horario de uso. Dato: hay 10 libros en el suelo. Opinión: el lugar es un desastre.", ["tres formas de reunir información", "una fuente con procedencia", "un dato y una opinión separados"], ["lista de preguntas u observaciones y un ejemplo de dato y de opinión"], ["usar solo la opinión de una persona", "mezclar dato y opinión"], "Pide a una persona de tu casa que responda tus preguntas y revisa si le sirven."),
    reinforce="Cuenta cuántos objetos de un tipo hay en una habitación y anótalo como dato.",
    extend="Escribe una pregunta de encuesta con tres opciones de respuesta sobre el uso del patio.",
)

register(
    OA21, 3,
    materials="Este cuaderno y un lápiz. Las soluciones y los actores del caso inventado están escritos en los ejercicios.",
    use="Aprenderé a pensar en las causas del problema y en las consecuencias de cada solución para todos los actores. Sirve para no elegir una solución que ayude a unos y perjudique a otros sin darse cuenta.",
    prior=["Sé describir un problema y reunir información.", "Sé nombrar causas, actores y consecuencias."],
    explain=[
        "Una buena solución ataca las causas del problema y no solo lo que se ve. Si el patio se llena de charcos porque el suelo no deja pasar el agua, secar charcos cada día no resuelve la causa. Por eso, antes de elegir, pregunto por qué ocurre el problema. Una solución que quita la causa dura más que una que solo tapa la consecuencia.",
        "Cada solución tiene efectos. Los efectos positivos son beneficios, como un patio seco. Los efectos negativos son costos (dinero, tiempo, trabajo o algo que se pierde, como espacio de juego) o riesgos (algo malo que podría pasar). También hay actores distintos: estudiantes, profesores, familias y la dirección. Una solución puede ser buena para los estudiantes y difícil para quienes deben pagarla o mantenerla.",
        "Para evaluar anoto, para cada solución, quién gana, quién pierde o se esfuerza, y cuánto cuesta en dinero, tiempo y trabajo. Tres soluciones del patio inundado pueden ser: un canal de desagüe, un jardín que absorba agua y un recreo bajo techo. El canal es seguro, pero caro. El jardín es barato y participativo, pero tarda en crecer. El recreo bajo techo es rápido, pero reduce el juego libre.",
    ],
    vocab=[("beneficio", "efecto bueno de una solución"), ("costo", "lo que exige o hace perder una solución: dinero, tiempo, trabajo o espacio"), ("riesgo", "algo malo que podría pasar"), ("mantener", "cuidar algo para que siga funcionando"), ("efecto", "lo que ocurre a raíz de una acción")],
    worked=[
        W("Atacar la causa", "El patio se inunda porque el agua no tiene por dónde salir. ¿Qué solución ataca la causa: secar los charcos cada día o hacer un canal que lleve el agua a otro lugar?",
          ["La causa es que el agua no tiene salida.", "Secar charcos solo quita el resultado.", "El canal le da una salida al agua."], "El canal de desagüe"),
        W("Beneficio y costo", "Jardín que absorba agua en el patio: es barato y participativo, pero tarda en crecer. ¿Cuál es un beneficio y cuál un costo?",
          ["Barato y participativo son buenos.", "Tardar es un esfuerzo de tiempo.", "Los separo."], "Beneficios: barato y participativo; costo: tarda en crecer"),
    ],
    mistakes=[
        M("Elegir una solución que solo quita lo que se ve.", "El problema vuelve porque la causa sigue.", "Pregunta qué causa el problema y revisa si la solución la ataca."),
        M("Pensar solo en cómo beneficia a mi grupo.", "Otros actores pueden salir perjudicados.", "Anota qué gana y qué pierde cada actor."),
    ],
    tiers=tiers(
        [ex("¿Qué es un beneficio de una solución?", "Un efecto bueno que produce", "Es lo que mejora con ella."),
         ex("Un costo puede ser de dinero o de tiempo. ¿Qué otro esfuerzo cuenta como costo?", "El trabajo", "El esfuerzo también cuenta."),
         ex("Un recreo bajo techo reduce el espacio de juego. ¿Ese efecto es un beneficio o un costo?", "Un costo", "Es algo que se pierde.")],
        [ex("¿Por qué una solución que ataca la causa suele durar más?", "Porque evita que el problema vuelva", "Elimina el origen del problema."),
         ex("¿Por qué hay que mirar a varios actores al evaluar una solución?", "Porque puede ayudar a unos y perjudicar a otros", "Los efectos no son iguales para todos."),
         ex("¿Qué significa «mantener» una solución?", "Cuidarla para que siga funcionando", "Una solución sin cuidado se deteriora.")],
        [ex("Un jardín que absorbe agua es barato, pero tarda en crecer. ¿«Tarda en crecer» es beneficio o costo?", "Costo", "Exige tiempo de espera."),
         ex("Un recreo bajo techo es rápido, pero reduce el juego libre. ¿Qué actor puede salir perjudicado?", "Los estudiantes", "Ellos pierden espacio de juego."),
         ex("El patio se inunda porque el suelo no deja pasar el agua. Elige la solución que ataca la causa: A) poner tarros para recoger charcos cada día, B) mejorar el suelo para que el agua pase.", "B", "Cambia la causa y no solo el resultado.")],
        [ex("Matías propone la solución más cara solo porque ayuda a su curso. ¿Qué le falta considerar?", "Los efectos sobre los otros actores y su costo", "Evaluar es mirar a todos."),
         ex("Un grupo dice: «Esta solución no tiene ningún costo». ¿Qué pregunta debes hacerles?", "Quién la mantendrá y cuánto tiempo y trabajo exige", "Toda solución exige algo de alguien.")],
        [ex("Ordena de menor a mayor espera: A) canal de desagüe en tres meses, B) recreo bajo techo desde mañana, C) jardín que crece en un año.", "B, A, C", "El tiempo es un costo distinto en cada solución."),
         ex("Dos soluciones para el patio: el canal es seguro, pero caro; el jardín es barato, pero lento. Si la escuela tiene poco dinero y no urge, ¿cuál conviene más?", "El jardín", "Respeta el presupuesto y no hay urgencia.")],
    ),
    context=[ex("En tu curso proponen guardar las mochilas en cajas para que el pasillo quede libre. Tú preguntas quién las comprará y quién las ordenará. ¿Qué estás evaluando?", "Los costos y los actores de la solución", "Verifica qué esfuerzo exige y a quién.")],
    selfcheck=[ex("En Ciencias Sociales: ¿qué es un beneficio?", "Un efecto bueno de una solución", "Es lo que mejora."), ex("¿Qué debe atacar una buena solución?", "La causa del problema", "Así el problema no vuelve."), ex("En Historia: ¿qué es un riesgo?", "Algo malo que podría pasar", "Se evalúa antes de elegir.")],
    open_task=task("Problema inventado: en la Escuela Los Aromos hay mucha basura en el patio. Soluciones: A) poner más basureros, B) campaña de cuidado con afiches, C) turnos de limpieza por curso. Para dos soluciones escribe un beneficio, un costo y un actor que podría esforzarse o perderse algo. Indica cuál ataca mejor la causa «las personas botan papeles porque no hay costumbre».", "A) Beneficio: es fácil de usar. Costo: dinero para comprarlos. Actor: la dirección. B) Beneficio: cambia la costumbre. Costo: tiempo para los afiches. Actor: los estudiantes que los hacen. Ataca mejor la causa: B, porque busca crear la costumbre de no botar papeles.", ["beneficio y costo por solución", "un actor por solución", "elige la que ataca la causa"], ["lista breve para dos soluciones y una elección"], ["pensar solo en un actor", "elegir una solución que no ataca la causa"], "Cuéntaselo a una persona de tu casa y pídele que diga qué solución elegiría."),
    reinforce="Elige un hábito que quieras mejorar y di una solución que ataque la causa.",
    extend="Explica por qué una solución barata puede salir cara si nadie la mantiene.",
)

register(
    OA21, 4,
    materials="Este cuaderno y un lápiz. Los criterios y los puntajes de la tabla están escritos en los ejercicios.",
    use="Aprenderé a comparar soluciones con criterios y a sumar puntajes para decidir con orden. Sirve para elegir de manera justa en un proyecto del curso o de la comunidad.",
    prior=["Sé nombrar beneficios, costos y actores.", "Sé sumar y comparar números."],
    explain=[
        "Un criterio es un aspecto que uso para juzgar una solución. Algunos criterios comunes son: costo (cuánto cuesta), rapidez (cuánto tarda), seguridad (si evita riesgos) y participación (si la comunidad puede ayudar). Elijo los criterios según lo que importa en el problema. Si el problema es urgente, la rapidez pesa más; si hay poco dinero, el costo pesa más.",
        "Para comparar uso una tabla. En las filas pongo las soluciones y en las columnas los criterios. Pongo un puntaje de 1 a 3: 3 es lo mejor y 1 lo menos bueno. Por ejemplo, una solución barata recibe 3 en costo, y una cara, 1. Luego sumo los puntajes de cada solución. La que suma más es la que, con esos criterios, resulta mejor.",
        "Una tabla ayuda, pero no decide sola. Si dos soluciones empatan, miro qué criterio importa más en este problema. También reviso que los puntajes tengan una razón, no que sean al azar. Y recuerdo que los números resumen una evaluación, pero también debo explicar los motivos con palabras.",
    ],
    vocab=[("criterio", "aspecto que se usa para juzgar una solución"), ("puntaje", "número que muestra qué tan bien cumple un criterio"), ("empate", "cuando dos opciones suman lo mismo"), ("tabla de decisión", "cuadro que compara soluciones según criterios"), ("prioridad", "lo que importa más en una decisión")],
    worked=[
        W("Sumar puntajes", "Solución canal: costo 1, rapidez 2, seguridad 3, participación 2. Solución jardín: costo 3, rapidez 1, seguridad 2, participación 3. ¿Cuál suma más?",
          ["Canal: 1 + 2 + 3 + 2 = 8.", "Jardín: 3 + 1 + 2 + 3 = 9.", "9 es mayor que 8."], "El jardín, con 9 puntos"),
        W("Desempatar con prioridad", "Dos soluciones empatan en 8 puntos. El problema es urgente. Una tiene rapidez 3 y la otra rapidez 1. ¿Cuál eliges?",
          ["Reviso qué importa más: la urgencia.", "El criterio que pesa es la rapidez.", "La de rapidez 3 es más rápida."], "La de rapidez 3"),
    ],
    mistakes=[
        M("Poner puntajes al azar.", "La tabla pierde sentido si no se justifican.", "Escribe una razón para cada puntaje."),
        M("Dejar que la tabla decida sin pensar.", "Los números no muestran todo.", "Revisa también la prioridad y explica con palabras."),
    ],
    tiers=tiers(
        [ex("En Historia: ¿qué es un criterio?", "Un aspecto que se usa para juzgar una solución", "Por ejemplo, el costo."),
         ex("En la tabla, ¿qué significa un 3?", "Que cumple muy bien el criterio", "3 es el mejor puntaje."),
         ex("¿Qué es un empate en puntajes?", "Que dos soluciones suman lo mismo", "No hay una ganadora clara.")],
        [ex("¿Por qué los criterios se eligen según el problema?", "Porque cada problema tiene prioridades distintas", "Si es urgente importa más la rapidez."),
         ex("¿Qué se pone en las filas y qué en las columnas de la tabla?", "Soluciones en las filas y criterios en las columnas", "Así se comparan."),
         ex("¿Qué se debe hacer si dos soluciones empatan?", "Mirar qué criterio importa más", "Se aplica la prioridad del problema.")],
        [arith("Solución A: costo 2, rapidez 3, seguridad 3, participación 1. ¿Cuántos puntos suma en total?", "2+3+3+1", "Se suman los cuatro criterios.", unit=" puntos"),
         arith("Solución B: costo 3, rapidez 2, seguridad 2, participación 3. ¿Cuántos puntos suma en total?", "3+2+2+3", "Se suman los cuatro criterios.", unit=" puntos"),
         ex("Con las sumas de A (9) y de B (10), ¿cuál solución queda mejor según la tabla?", "La solución B", "Tiene más puntos.")],
        [ex("Un grupo puso un 3 en costo para una solución que cuesta mucho dinero. ¿Qué error cometió?", "Puso un puntaje sin sentido para el criterio", "Un 3 en costo debía ser lo barato."),
         ex("Dos soluciones suman 8. El problema es de seguridad en una esquina. Una tiene seguridad 3 y la otra 1. ¿Cuál eliges y por qué?", "La de seguridad 3 porque el problema es de seguridad", "La prioridad guía el desempate.")],
        [arith("Solución C: costo 3, rapidez 3, seguridad 1, participación 2. ¿Cuántos puntos suma en total?", "3+3+1+2", "Se suman los cuatro criterios.", unit=" puntos"),
         ex("Ordena de menor a mayor puntaje: A) solución X con 9, B) solución Y con 7, C) solución Z con 11.", "B, A, C", "7 es menor que 9 y 9 menor que 11.")],
    ),
    context=[ex("Tu curso debe elegir entre una excursión cercana o una visita virtual con poco dinero y poco tiempo. Con poco dinero y poco tiempo, ¿qué dos criterios de la lista pesan más?", "Costo y rapidez", "Se relacionan con la falta de dinero y de tiempo.")],
    selfcheck=[ex("En Ciencias Sociales: ¿qué es un criterio?", "Un aspecto para juzgar una solución", "Guía la evaluación."), ex("¿Qué es una prioridad?", "Lo que importa más en una decisión", "Sirve para desempatar."), ex("¿Qué hace una tabla de decisión?", "Compara soluciones según criterios", "Ordena la evaluación.")],
    open_task=task("Problema: un patio con charcos. Soluciones: A) canal de desagüe, B) jardín que absorbe agua, C) recreo bajo techo. Usa los criterios costo, rapidez, seguridad y participación. Haz una tabla con puntajes de 1 a 3, suma, escribe una razón para dos puntajes y di cuál eliges si el problema es urgente.", "Canal: 1,2,3,2 = 8. Jardín: 3,1,2,3 = 9. Recreo bajo techo: 3,3,2,1 = 9. Como es urgente, elijo recreo bajo techo por rapidez.", ["tabla con cuatro criterios", "suma correcta", "razón para dos puntajes", "desempate con prioridad"], ["tabla de tres filas con suma y elección"], ["puntajes sin razón", "no usar la prioridad al empatar"], "Muestra tu tabla a una persona de tu casa y pídele que revise las sumas."),
    reinforce="Compara dos meriendas con los criterios precio y rapidez, con puntajes de 1 a 3.",
    extend="Agrega un quinto criterio a tu tabla y explica cómo cambia la decisión.",
)

register(
    OA21, 5,
    materials="Este cuaderno y un lápiz. Los resultados de la evaluación y el caso están escritos en los ejercicios.",
    use="Aprenderé a elegir una solución, justificar mi elección con evidencia y criterios, y revisar si funcionó. Sirve para tomar decisiones en proyectos del curso y para explicarlas con respeto.",
    prior=["Sé comparar soluciones con criterios.", "Sé argumentar con afirmación, evidencia y explicación."],
    explain=[
        "Elegir una solución es el paso final de la evaluación. Para justificarla uso tres partes: la solución elegida, los criterios y datos que la apoyan y una respuesta a lo que preocupa de las otras. Por ejemplo: «Elegimos el jardín porque obtuvo 9 puntos, es barato y las familias pueden ayudar. El canal es seguro, pero cuesta demasiado para este año».",
        "Una buena justificación también reconoce los costos de la elección. No existe una solución perfecta. Podemos decir: «El jardín tarda en crecer, por eso pondremos un recreo bajo techo mientras tanto». Así la decisión es honesta y considera a quienes podrían perder algo. Además, escuchamos a las demás personas del grupo antes de decidir.",
        "Elegir no termina el proyecto. Hay que hacer un plan, con tareas, responsables y fechas, y luego revisar el resultado: ¿se logró lo que se quería?, ¿qué falló?, ¿qué cambiaríamos? Si el resultado no es el esperado, se ajusta o se elige otra solución. Así se aprende a decidir mejor la próxima vez.",
    ],
    vocab=[("justificar", "explicar con razones y evidencia por qué se eligió algo"), ("plan", "tareas con responsables y fechas"), ("responsable", "persona a cargo de una tarea"), ("revisar", "mirar los resultados y ver qué ajustar"), ("ajustar", "cambiar algo para mejorarlo")],
    worked=[
        W("Armar una justificación", "Elegiste el jardín con 9 puntos, barato y con apoyo de familias. Escribe una justificación breve.",
          ["Digo qué solución elegí.", "Uso el puntaje y los criterios.", "Respondo a una duda sobre otra solución."], "Elegimos el jardín porque sumó 9 puntos, es barato y las familias pueden ayudar"),
        W("Revisar un resultado", "Después de un mes, el jardín creció poco porque nadie lo regó. ¿Qué haces?",
          ["Pregunto qué falló.", "Falló la tarea de regar.", "Ajusto el plan con una persona responsable."], "Asignar una persona responsable de regar y revisar de nuevo"),
    ],
    mistakes=[
        M("Justificar solo con «me gusta más».", "No convence ni muestra criterios.", "Usa puntajes, datos y criterios."),
        M("Decir que la solución elegida no tiene ningún costo.", "Toda solución exige algo.", "Reconoce el costo y explica cómo se enfrentará."),
    ],
    tiers=tiers(
        [ex("¿Qué es justificar una elección?", "Explicar con razones y evidencia por qué se eligió", "Así se entiende la decisión."),
         ex("¿Qué es un plan?", "Tareas con responsables y fechas", "Ordena la acción."),
         ex("¿Qué significa «ajustar» un plan?", "Cambiar algo para mejorarlo", "Se hace tras revisar el resultado.")],
        [ex("¿Por qué una justificación debe reconocer los costos de la solución elegida?", "Porque ninguna solución es perfecta y hay que ser honestos", "Reconocerlo hace la decisión más creíble."),
         ex("¿Por qué conviene escuchar a todo el grupo antes de decidir?", "Porque cada actor puede aportar razones distintas", "Mejora la decisión."),
         ex("¿Qué se hace después de aplicar una solución?", "Revisar si se logró lo que se quería", "Así se aprende de la decisión.")],
        [ex("Elige la mejor justificación: A) «Elegimos el jardín porque me gusta.» B) «Elegimos el jardín porque sumó 9 puntos y es barato.»", "B", "Usa puntaje y un criterio."),
         ex("En un plan, «regar el jardín los lunes: Camila» ¿quién es la persona responsable?", "Camila", "Es la persona a cargo de la tarea."),
         ex("Un recreo bajo techo se usa mientras crece el jardín. ¿Qué costo de la solución elegida reconoce esa medida?", "Que el jardín tarda en crecer", "Ofrece una medida para esperar.")],
        [ex("Tomás dice: «Nuestra solución es perfecta y no necesita revisión». ¿Qué le respondes?", "Toda solución se revisa para ver qué ajustar", "Revisar permite mejorar."),
         ex("Un grupo eligió una solución, pero no escribió quién hará cada tarea. ¿Qué problema puede ocurrir?", "Que nadie la haga", "Sin responsables nadie sabe qué le toca.")],
        [ex("Ordena el proceso: A) revisar resultados, B) elegir y justificar, C) hacer el plan.", "B, C, A", "Primero se elige, luego se planifica y al final se revisa."),
         arith("Después de dos semanas, 3 de las 5 tareas del plan se cumplieron. ¿Cuántas tareas faltan por cumplir?", "5-3", "Se resta lo cumplido del total.", unit=" tareas")],
    ),
    context=[ex("Tu curso eligió hacer una feria de libros usados para reunir fondos, pero llegaron pocas personas. ¿Qué hace el grupo para evaluar el proyecto?", "Revisa qué falló y ajusta el plan", "La evaluación sigue después de actuar.")],
    selfcheck=[ex("En Ciencias Sociales: ¿qué es justificar?", "Explicar con razones y evidencia por qué se eligió algo", "Es la idea central de la clase."), ex("¿Qué debe tener un plan?", "Tareas, responsables y fechas", "Permite organizar la acción."), ex("¿Qué se hace al revisar?", "Ver si se logró lo que se quería y qué ajustar", "Cierra el ciclo.")],
    open_task=task("Elige un problema del curso: A) un patio con charcos, B) una biblioteca de aula desordenada, C) filas largas en el kiosco. Piensa en tres soluciones posibles, elige una y justifícala con dos criterios y un dato (si lo inventas, escribe «dato de ejemplo»), reconoce un costo, escribe un plan con tres tareas, responsables inventados y fechas, y cómo revisarías el resultado.", "Tema B. Elegimos turnos de orden porque cuesta poco y participa todo el curso. Dato de ejemplo: hoy hay 10 libros en el suelo. Costo: tiempo del recreo. Plan: lunes, Ana ordena; martes, Luis ordena; viernes, Sofía cuenta los libros del suelo. Revisaremos en dos semanas si bajaron de 10.", ["solución justificada con criterios", "un costo reconocido", "plan con tres tareas", "forma de revisar"], ["texto de justificación y plan"], ["justificar solo con gusto", "no revisar resultados"], "Lee tu plan a una persona de tu casa y pídele que diga qué cambiaría."),
    reinforce="Cuenta a una persona de tu casa cómo elegirías entre dos juegos para un cumpleaños, con un criterio.",
    extend="Escribe cómo cambiarías tu plan si tu revisión muestra que la solución elegida no funcionó.",
)

"""Cuaderno del estudiante, 5.º básico Historia, Geografía y Ciencias Sociales: OA 17 (elección responsable de una directiva de curso)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA17 = "HI05 OA 17"
E = ex


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def tiers(recovery, understand, apply, reason, challenge):
    return {"recovery": recovery, "understand": understand, "apply": apply, "reason": reason, "challenge": challenge}


register(
    OA17, 1,
    materials="Este cuaderno y un lápiz. Los cargos y las reglas de la elección están escritos en los ejercicios.",
    use="Aprenderé qué es una directiva de curso, qué cargos tiene y qué funciones cumple cada uno. Sirve para saber qué se espera de quien es elegido y a quién elegir.",
    prior=["Sé que participar en la comunidad es un derecho y una responsabilidad.", "Sé qué es una actitud cívica."],
    explain=[
        "La directiva de curso es el grupo de estudiantes que el curso elige para ayudar a organizarlo durante el año. Cada cargo tiene funciones. La presidencia representa al curso y dirige las reuniones. La vicepresidencia reemplaza a la presidencia si falta. La secretaría anota los acuerdos. La tesorería cuida el dinero del curso y lleva las cuentas. Puede haber delegados, por ejemplo de convivencia o de deportes.",
        "Tener un cargo es una responsabilidad, no un privilegio. Quien lo ocupa debe cumplir sus funciones, escuchar a sus compañeros y dar el ejemplo. Por eso importa elegir personas idóneas, es decir, adecuadas para el cargo: responsables, respetuosas, que escuchen y que cumplan lo que prometen.",
        "Las directivas se eligen al comienzo del año, en la sala de clases, con una votación. Así el curso se organiza, se resuelven los problemas de convivencia y se puede trabajar mejor. Ubicar el cargo y su función nos ayuda a elegir con criterio.",
    ],
    vocab=[("directiva de curso", "grupo de estudiantes elegido para organizar al curso"), ("cargo", "puesto con funciones y responsabilidades"), ("función", "tarea que corresponde a un cargo"), ("idóneo", "adecuado para un cargo por sus cualidades"), ("representar", "hablar y actuar en nombre del grupo")],
    worked=[
        W("Función de cada cargo", "En la directiva hay presidencia, secretaría y tesorería. ¿Quién anota los acuerdos de las reuniones?",
          ["Reviso las funciones.", "La secretaría anota los acuerdos.", "La tesorería lleva el dinero."], "La secretaría"),
        W("Qué es idóneo", "Una candidata promete cumplir sus tareas y escucha a todos. Otro quiere el cargo para tener privilegios. ¿Quién es más idónea?",
          ["El cargo es una responsabilidad.", "La primera escucha y cumple.", "El segundo busca beneficio personal."], "La candidata que escucha y cumple"),
    ],
    mistakes=[
        M("Pensar que tener un cargo da más derechos que a los demás.", "Un cargo es una responsabilidad hacia el curso.", "Piensa en lo que debe hacer, no en lo que gana."),
        M("Elegir a alguien solo por ser tu amigo.", "El cargo requiere cualidades para cumplirlo.", "Elige a quien sea idóneo."),
    ],
    tiers=tiers(
        [E("Quien anota los acuerdos del curso, ¿es la secretaría o la tesorería?", "La secretaría", "Esa es su función."),
         E("Quien cuida el dinero del curso, ¿es la tesorería o la presidencia?", "La tesorería", "Esa es su función."),
         E("Un puesto con funciones y responsabilidades, ¿es un cargo o un privilegio?", "Un cargo", "El privilegio es una ventaja.")],
        [E("¿Por qué un cargo es una responsabilidad y no un privilegio?", "Porque exige cumplir tareas por el curso", "Se trabaja para el grupo."),
         E("¿Qué significa que una persona sea idónea para un cargo?", "Que tiene las cualidades adecuadas para cumplirlo", "Es la definición del vocabulario."),
         E("Según la clase, ¿cuándo se elige la directiva de curso?", "Al comienzo del año", "Así el curso se organiza desde el principio.")],
        [E("Clasifica cada tarea con su cargo: a) dirigir la reunión; b) anotar los acuerdos; c) llevar las cuentas del curso. Cargos: tesorería, presidencia, secretaría.", "a presidencia; b secretaría; c tesorería", "Cada cargo tiene su función."),
         E("Si la presidencia falta a una reunión, ¿quién la reemplaza: la vicepresidencia o la secretaría?", "La vicepresidencia", "Su función es reemplazarla."),
         arith("Una directiva de ejemplo tiene presidencia, vicepresidencia, secretaría, tesorería y 2 delegados. ¿Cuántas personas la forman?", "1+1+1+1+2", "Se suman los cargos.")],
        [E("Lía dice: «Voy a ser presidenta para mandar a todos». ¿Qué error tiene?", "Un cargo es una responsabilidad, no una forma de mandar", "Se sirve al curso."),
         E("Un curso quiere elegir como tesorero a un compañero que dice «no quiero llevar cuentas ni anotar nada». ¿Es idóneo para ese cargo? Responde sí o no y explica.", "No; no quiere cumplir la función de llevar las cuentas", "El cargo exige cumplir sus funciones.")],
        [E("Ordena los pasos para organizar al curso: A) cumplir las funciones, B) elegir la directiva, C) conocer los cargos.", "C, B, A", "Primero se conocen los cargos, luego se elige y después se cumple."),
         E("Un curso de 32 estudiantes tiene 6 cargos. ¿Cuántos estudiantes no tienen cargo?", "26", "32 menos 6 son 26.", "32-6")],
    ),
    context=[E("En la reunión, nadie anotó los acuerdos y después el curso olvidó qué había decidido. ¿Qué cargo debería haber cumplido esa función?", "La secretaría", "Es el cargo que anota los acuerdos.")],
    selfcheck=[E("¿Qué es una directiva de curso?", "Un grupo elegido para organizar al curso", "Es la definición de la clase."), E("¿Qué hace la tesorería?", "Cuida el dinero y lleva las cuentas", "Es su función."), E("¿Qué significa idóneo?", "Adecuado para un cargo por sus cualidades", "Es la definición del vocabulario.")],
    open_task=task("Haz una tabla con cinco cargos (presidencia, vicepresidencia, secretaría, tesorería y delegado de convivencia). Escribe para cada uno su función y una cualidad que debería tener quien lo ocupe.", "Secretaría: anota acuerdos; cualidad: ordenada y cuidadosa.", ["describe la función de cada cargo", "propone una cualidad adecuada", "no usa la palabra privilegio"], ["tabla de cinco filas"], ["confundir las funciones", "decir que el cargo da ventajas"], "Pide a una persona que adivine el cargo leyendo solo su función."),
    reinforce="Escribe qué cargo te gustaría tener y qué harías para cumplirlo.",
    extend="Escribe una función más que podría tener un delegado de convivencia.",
)

register(
    OA17, 2,
    materials="Este cuaderno y un lápiz. Las propuestas y el acta están escritas en los ejercicios.",
    use="Aprenderé a leer propuestas de candidatos y el acta de una elección, y a preguntar quién las escribió y qué dicen realmente. Sirve para votar con información.",
    prior=["Sé qué cargos tiene una directiva de curso.", "Sé qué es una fuente y su procedencia."],
    explain=[
        "En una elección encontramos distintas fuentes. La propuesta de un candidato es un texto donde cuenta qué hará si lo eligen. El acta de la elección es un documento que registra cuántos votos obtuvo cada candidato y quién ganó. Una conversación de pasillo es solo un rumor.",
        "Para leer una propuesta preguntamos: ¿quién la escribió?, ¿qué promete?, ¿se puede cumplir?, ¿cuándo y cómo? Una promesa como «haré que nunca haya tareas» no se puede cumplir porque no depende del cargo. Una promesa como «anotaré cada acuerdo en el cuaderno del curso» sí depende de la secretaría.",
        "El acta se lee con cuidado: nombres, cantidad de votos, votos nulos o en blanco, y total. Los números deben coincidir. Si no suman, hay que revisar. Una elección transparente deja claro cómo se votó y cómo se contó.",
    ],
    vocab=[("propuesta", "lo que un candidato promete hacer si es elegido"), ("acta", "documento que registra lo que ocurrió en una reunión o elección"), ("voto nulo", "voto que no vale porque está mal marcado"), ("voto en blanco", "voto que no elige a ningún candidato"), ("transparente", "claro, que se puede revisar")],
    worked=[
        W("Promesa posible o imposible", "Un candidato promete «no habrá pruebas nunca». ¿Puede cumplirlo desde el cargo?",
          ["Reviso qué decisiones dependen del cargo.", "Las pruebas las decide el profesor.", "No puede cumplirlo."], "No; no depende del cargo"),
        W("Leer un acta", "Acta de ejemplo: Ana 12 votos, Beto 9, nulos 1. ¿Cuántos votos se emitieron?",
          ["Sumo todos los votos.", "12 + 9 + 1.", "Resulta 22."], "22 votos"),
    ],
    mistakes=[
        M("Creer toda promesa que suena bien.", "Algunas no dependen del cargo.", "Pregunta si se puede cumplir."),
        M("Contar solo los votos de los candidatos y olvidar los nulos.", "El total incluye todos los votos emitidos.", "Suma candidatos, nulos y blancos."),
    ],
    tiers=tiers(
        [E("Lo que un candidato promete hacer si es elegido, ¿es su propuesta o su acta?", "Su propuesta", "El acta registra los resultados."),
         E("El documento que registra cuántos votos tuvo cada candidato, ¿es un acta o una propuesta?", "Un acta", "Deja constancia de la elección."),
         E("Un voto que no vale porque está mal marcado, ¿es nulo o en blanco?", "Nulo", "El voto en blanco no elige a nadie.")],
        [E("¿Qué preguntas haces a la propuesta de un candidato?", "Quién la escribió, qué promete y si se puede cumplir", "Así se evalúa si es realista."),
         E("¿Por qué una elección debe ser transparente?", "Para que todos puedan revisar cómo se votó y contó", "Da confianza a todos los votantes."),
         E("¿Por qué los números del acta deben coincidir?", "Porque si no suman, hay un error que revisar", "Todos los votos deben estar contados.")],
        [arith("Acta de ejemplo: Ema 10 votos, Luis 8 votos, 2 nulos. ¿Cuántos votos se emitieron en total?", "10+8+2", "Se suman todos los votos emitidos."),
         E("Un candidato promete «anotar cada acuerdo en el cuaderno del curso». ¿Para qué cargo es esa promesa: secretaría o tesorería?", "Secretaría", "La secretaría anota los acuerdos."),
         E("Acta de ejemplo: Ana 12 votos y Beto 9 votos. ¿Quién ganó?", "Ana", "12 es mayor que 9.")],
        [E("Nico dice: «Voto por quien prometa regalar dulces a todos». ¿Qué debería preguntar sobre esa promesa?", "Si se puede cumplir y si importa para el cargo", "Una promesa debe ser realista y relacionada con el cargo."),
         E("Un candidato promete cambiar las notas de todos. ¿Es una promesa posible? Responde sí o no y explica.", "No; las notas no dependen de la directiva", "Los cargos de curso no deciden las notas.")],
        [E("Ordena los pasos para leer un acta: A) revisar que los números sumen, B) leer los nombres, C) ver quién obtuvo más votos.", "B, C, A", "Primero los nombres, luego los resultados y al final la comprobación."),
         E("En un curso de 30 estudiantes votaron 28. Hubo 3 votos nulos. ¿Cuántos votos válidos hubo?", "25", "28 menos 3 son 25.", "28-3")],
    ),
    context=[E("En el acta de ejemplo: Ana 11 votos, Beto 9 votos, nulos 1, blancos 1. Dicen que votaron 21 personas. ¿Es correcto?", "No; fueron 22", "11 + 9 + 1 + 1 son 22.")],
    selfcheck=[E("¿Qué es un acta?", "Un documento que registra lo que ocurrió en una elección o reunión", "Es la definición de la clase."), E("¿Qué es un voto nulo?", "Un voto que no vale por estar mal marcado", "Es la definición del vocabulario."), E("¿Toda promesa se puede cumplir desde cualquier cargo?", "No", "Algunas no dependen del cargo.")],
    open_task=task("Lee estas dos propuestas de ejemplo: Candidata A: «Haré una reunión cada mes y anotaré los acuerdos en un cuaderno». Candidato B: «Haré que no haya tareas nunca más». Escribe cuál promesa es posible y por qué, qué pregunta le harías a cada uno y qué dato te gustaría ver en un acta.", "A es posible; B no. Pregunta a A: ¿cómo avisarás las reuniones? Pregunta a B: ¿cómo lo lograrás? Acta: votos de cada uno.", ["distingue promesa posible de imposible", "hace una pregunta a cada candidato", "nombra un dato del acta"], ["cuatro frases"], ["creer toda promesa", "no justificar"], "Pide a una persona que elija a quién votaría y por qué."),
    reinforce="Escribe una promesa realista que harías si te eligieran delegado de convivencia.",
    extend="Escribe cómo cuidarías que el conteo de votos sea transparente.",
)

register(
    OA17, 3,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé a relacionar cómo se elige a una directiva con la convivencia y la organización del curso. Sirve para entender por qué elegir bien importa para todos.",
    prior=["Sé qué cargos y funciones tiene una directiva.", "Sé leer propuestas y actas."],
    explain=[
        "Una buena elección tiene causas y consecuencias. Si el curso elige a personas responsables, la directiva organiza reuniones, anota acuerdos, cuida el dinero y ayuda a resolver los conflictos. El resultado es una buena convivencia y un curso donde se puede trabajar. Si se elige por amistad, por miedo o por broma, puede faltar quien cumpla las funciones.",
        "Los actores son los estudiantes electores, los candidatos, el profesor o profesora jefe que acompaña el proceso y quienes cuentan los votos. Cada uno tiene un rol: los electores votan con información, los candidatos presentan propuestas reales, y el profesor ayuda a que las reglas se cumplan.",
        "Para que el voto sea libre, se vota en secreto: nadie debe saber por quién votó otro, para evitar presiones. Las consecuencias de una elección responsable duran todo el año: confianza, orden y respeto. Las de una elección irresponsable son desorden y desánimo.",
    ],
    vocab=[("elector", "persona que vota"), ("candidato", "persona que se presenta para ser elegida"), ("voto secreto", "voto que nadie más puede conocer"), ("presión", "intentar que alguien decida algo sin libertad"), ("consecuencia", "lo que ocurre después de una decisión")],
    worked=[
        W("Causa y consecuencia", "Un curso eligió a un tesorero responsable y el dinero se registró siempre. ¿Qué causa y qué consecuencia hay?",
          ["Causa: se eligió a alguien responsable.", "Consecuencia: las cuentas están claras.", "También aumenta la confianza."], "Causa: elegir a un responsable; consecuencia: cuentas claras y confianza"),
        W("Por qué el voto es secreto", "Un compañero insiste en que todos le muestren por quién votaron. ¿Qué se pierde?",
          ["La libertad de elegir.", "Algunos votarían por miedo.", "El secreto evita presiones."], "La libertad; el voto secreto evita presiones"),
    ],
    mistakes=[
        M("Votar por broma o por quien dé algo a cambio.", "La directiva trabajará todo el año; una mala elección afecta a todos.", "Vota con criterios."),
        M("Contar a los demás por quién votaste para convencerlos.", "Puede presionar a otros.", "Respeta el voto secreto y comparte razones, no presiones."),
    ],
    tiers=tiers(
        [E("La persona que vota, ¿es un elector o un candidato?", "Un elector", "El candidato es quien se presenta."),
         E("Un voto que nadie más puede conocer, ¿es un voto secreto o un voto nulo?", "Un voto secreto", "Es el voto que se mantiene privado."),
         E("Intentar que alguien decida sin libertad, ¿es presión o respeto?", "Presión", "El respeto deja decidir libremente.")],
        [E("¿Por qué el voto se hace en secreto?", "Para que nadie sea presionado y todos elijan libremente", "Protege la libertad del voto."),
         E("¿Qué consecuencia tiene elegir a personas responsables?", "El curso se organiza y convive mejor", "Cumplen las funciones del cargo."),
         E("¿Qué rol tiene el profesor jefe en la elección?", "Acompañar el proceso para que se cumplan las reglas", "No vota por los estudiantes.")],
        [E("Un curso elige presidente a un compañero solo porque es muy gracioso, y él no organiza las reuniones. ¿Cuál fue la causa del problema: la elección sin criterio o el horario de las reuniones?", "La elección sin criterio", "No se pensó si era idóneo."),
         arith("En un curso de 30 estudiantes, 25 votan con información y 5 votan por broma. ¿Cuántos votaron con información más que por broma?", "25-5", "Se resta los votos por broma a los informados."),
         E("Una candidata presenta una propuesta realista, el curso la escucha y la elige. ¿Qué actores participaron: electores y candidata, o solo la candidata?", "Electores y candidata", "Ambos participan en la elección.")],
        [E("Rodrigo dice: «Da lo mismo a quién elijamos, la directiva no hace nada». ¿Qué error tiene?", "La directiva organiza y su desempeño afecta a todo el curso", "Una buena elección tiene consecuencias positivas."),
         E("Un grupo amenaza a otros para que voten por cierto candidato. ¿Qué principio no respetan?", "La libertad del voto", "La presión impide elegir libremente.")],
        [E("Ordena la cadena: A) el curso convive mejor, B) se elige a personas responsables, C) la directiva cumple sus funciones.", "B, C, A", "Primero la elección, luego el cumplimiento y luego la convivencia."),
         E("Dos estudiantes elegidos por el curso miran cómo la profesora cuenta los votos. ¿Qué se logra con eso: un conteo transparente o un conteo secreto?", "Un conteo transparente", "Así todos pueden comprobar que se contó bien.")],
    ),
    context=[E("Un curso fue desordenado todo el año porque la directiva nunca cumplió sus funciones. En la nueva elección, los estudiantes piden propuestas claras y revisan quién cumple lo que promete. ¿Qué buscan con eso?", "Elegir personas idóneas", "Así mejoran la organización del curso.")],
    selfcheck=[E("¿Qué es un candidato?", "La persona que se presenta para ser elegida", "Es la definición del vocabulario."), E("¿Por qué el voto es secreto?", "Para evitar presiones", "Protege la libertad."), E("¿Qué consecuencia tiene una buena elección?", "Buena convivencia y organización", "El curso funciona mejor.")],
    open_task=task("Caso de ejemplo: un curso eligió presidente a quien prometió regalos. Dos meses después no hay reuniones ni acuerdos. Escribe la causa, los actores que influyeron, dos consecuencias y qué harías en la próxima elección para elegir mejor.", "Causa: se votó por regalos. Actores: electores, candidato, profesor. Consecuencias: desorden, desánimo. Próxima vez: pedir propuestas reales.", ["identifica la causa", "nombra al menos tres actores", "propone una mejora concreta"], ["ficha de cuatro partes"], ["culpar solo al presidente", "no proponer cambios"], "Pide a otra persona que opine si tu mejora es realista."),
    reinforce="Escribe una razón por la cual elegirías a un compañero para un cargo.",
    extend="Escribe qué pasaría si nadie quisiera presentarse como candidato.",
)

register(
    OA17, 4,
    materials="Este cuaderno y un lápiz. Los perfiles de los candidatos están escritos en los ejercicios.",
    use="Aprenderé a comparar candidaturas y las perspectivas de distintos votantes con criterios claros. Sirve para elegir sin dejarme llevar por la simpatía.",
    prior=["Sé leer propuestas y actas.", "Sé que elegir bien afecta la convivencia."],
    explain=[
        "Comparar candidaturas es poner a los candidatos frente a los mismos criterios. Algunos criterios útiles son la responsabilidad que han mostrado, la capacidad de escuchar, la claridad de sus propuestas y si estas se pueden cumplir. Comparar así evita elegir solo por simpatía o por amistad.",
        "Los votantes también tienen perspectivas distintas. Una persona tímida puede querer una directiva que escuche; otra puede preferir que organice más actividades; otra, que cuide el orden. Todas las perspectivas son válidas, pero la directiva debe trabajar para todo el curso.",
        "También se puede comparar cómo se organizan otros cursos o escuelas: algunos eligen cada año, otros dividen las tareas en comisiones. Ver otras formas ayuda a mejorar la propia, sin copiarlas sin pensar.",
    ],
    vocab=[("criterio", "regla igual para comparar a todos los candidatos"), ("simpatía", "gusto personal por alguien"), ("comisión", "grupo pequeño que se encarga de una tarea"), ("válido", "que se puede aceptar como razonable"), ("equitativo", "que trata a todos de forma justa")],
    worked=[
        W("Comparar con criterios", "Candidato A: cumplió siempre sus tareas, propuestas claras. Candidata B: simpática, propuestas confusas. Con los criterios «responsabilidad» y «propuestas claras», ¿quién cumple más?",
          ["Reviso cada criterio.", "A cumple ambos; B solo es simpática.", "La simpatía no es un criterio del cargo."], "El candidato A"),
        W("Perspectivas de votantes", "Un votante quiere más actividades y otro más orden. ¿Cómo debe actuar la directiva?",
          ["Escuchar a ambos.", "Buscar un equilibrio.", "Trabajar para todo el curso."], "Escuchar a ambos y buscar un equilibrio"),
    ],
    mistakes=[
        M("Elegir por simpatía en vez de por criterios.", "El cargo requiere cumplir funciones.", "Compara con los mismos criterios."),
        M("Pensar que la directiva solo debe representar a sus amigos.", "Debe trabajar para todo el curso.", "Escucha todas las perspectivas."),
    ],
    tiers=tiers(
        [E("Una regla igual para comparar a todos los candidatos, ¿es un criterio o una simpatía?", "Un criterio", "La simpatía es un gusto personal."),
         E("Un grupo pequeño que se encarga de una tarea, ¿es una comisión o un acta?", "Una comisión", "El acta es un documento."),
         E("Algo que se puede aceptar como razonable, ¿es válido o imposible?", "Válido", "Es una opinión razonable.")],
        [E("¿Por qué conviene comparar candidatos con los mismos criterios?", "Para elegir de manera justa y no por simpatía", "Todos son juzgados igual."),
         E("¿Por qué la directiva debe trabajar para todo el curso?", "Porque fue elegida por todos y representa a todos", "No solo a sus amigos."),
         E("¿Qué ayuda a mejorar tu curso cuando miras cómo se organizan otros?", "Conocer otras formas y adaptarlas con criterio", "Se aprende de otras experiencias.")],
        [E("Criterios: responsabilidad y escucha. Candidato C: responsable y escucha. Candidata D: responsable pero no escucha. ¿Quién cumple ambos?", "El candidato C", "D no cumple el criterio de escucha."),
         E("Un curso quiere dividir tareas en comisiones de 4 estudiantes. Si son 28 estudiantes, ¿cuántas comisiones se forman?", "7", "28 dividido en grupos de 4 da 7.", "28//4"),
         E("Un candidato dice que hará lo que le pidan sus amigos. ¿Cumple con representar a todo el curso? Responde sí o no.", "No", "Debe pensar en todos.")],
        [E("Sara dice: «Voto por Ana porque es mi amiga». ¿Qué criterio debería agregar?", "Si cumple las funciones del cargo", "La amistad no basta."),
         E("Un votante tímido y otro muy activo quieren cosas distintas de la directiva. ¿Es un problema que haya perspectivas distintas? Responde sí o no.", "No", "La directiva debe escuchar a todas.")],
        [E("Ordena según criterios (de mejor a peor en responsabilidad): A) cumplió 8 de 10 tareas, B) cumplió 10 de 10, C) cumplió 5 de 10.", "B, A, C", "10 es mayor que 8 y 8 mayor que 5."),
         arith("Candidato E cumplió 9 tareas y Candidata F cumplió 6. ¿Cuántas tareas más que F cumplió E?", "9-6", "Se resta lo que cumplió F a lo que cumplió E.")],
    ),
    context=[E("En un curso, 12 estudiantes quieren más actividades y 8 quieren más orden. La directiva decide ignorar a los 8. ¿Es equitativo? Responde sí o no.", "No", "Debe considerar a todo el curso.")],
    selfcheck=[E("En Historia: ¿Qué es un criterio?", "Una regla igual para comparar a todos", "Es la definición de la clase."), E("¿Qué es la simpatía?", "El gusto personal por alguien", "Es la definición del vocabulario."), E("¿Para quién trabaja la directiva?", "Para todo el curso", "Fue elegida por todos.")],
    open_task=task("Perfiles de ejemplo: Candidato 1: cumplió 9 de 10 tareas, escucha a todos, propone reuniones cada mes. Candidata 2: cumplió 6 de 10 tareas, es muy simpática, a veces no escucha, propone fiestas. Candidato 3: cumplió 8 de 10 tareas, escucha a quienes piden la palabra, propone comisiones de trabajo. Compara con tres criterios (responsabilidad, escucha, propuestas) y escribe a quién elegirías y qué perspectiva de otro votante podría llevarlo a decidir distinto.", "Elegiría al 1: más tareas cumplidas y escucha. Otro votante podría preferir las actividades de la 2.", ["usa los tres criterios", "compara con datos", "reconoce otra perspectiva"], ["tabla de tres criterios y una decisión"], ["decidir por simpatía", "ignorar la perspectiva de otros"], "Pide a una persona que diga a quién elegiría y compara sus razones."),
    reinforce="Escribe tres criterios que usarías para elegir a un delegado de deportes.",
    extend="Escribe cómo podría una directiva escuchar a quienes no votaron por ella.",
)

register(
    OA17, 5,
    materials="Este cuaderno y un lápiz. Los datos y el caso están escritos en los ejercicios.",
    use="Aprenderé a defender con evidencia mi voto o mi candidatura y a aceptar los resultados de una elección. Sirve para participar con responsabilidad en las decisiones del curso.",
    prior=["Sé comparar candidaturas con criterios.", "Sé que el voto es libre y secreto."],
    explain=[
        "Una persona responsable puede explicar por qué vota por alguien. La razón debe apoyarse en evidencia, no en el rumor ni en la simpatía. La evidencia puede ser lo que el candidato hizo antes, cuántas tareas cumplió, si sus propuestas se pueden realizar o lo que dicen compañeros que trabajaron con él.",
        "Quien se presenta también debe argumentar. Una buena candidatura dice qué hará, cómo y en qué plazo, y reconoce lo que no depende del cargo. Por ejemplo: «Haré una reunión al mes y anotaré los acuerdos; no puedo cambiar las notas».",
        "Después de la votación, el curso acepta los resultados. Quien gana debe trabajar para todos; quien pierde puede colaborar y vigilar que se cumplan las promesas. Si hay empate, el curso aplica la regla acordada, como una segunda votación entre los empatados.",
    ],
    vocab=[("evidencia", "dato o hecho que apoya una decisión"), ("plazo", "tiempo en que se propone hacer algo"), ("empate", "cuando dos o más candidatos tienen los mismos votos"), ("resultado", "lo que sale después de contar los votos"), ("vigilar", "observar que se cumpla lo prometido")],
    worked=[
        W("Argumentar un voto", "Votas por Clara porque cumplió 9 de 10 tareas como delegada y sus propuestas son claras. ¿Cuál es la evidencia?",
          ["Busco el dato.", "Cumplió 9 de 10 tareas.", "También sus propuestas son claras."], "Cumplió 9 de 10 tareas"),
        W("Resolver un empate", "Regla acordada: si hay empate, se vota de nuevo solo entre los empatados. Ana y Beto tienen 10 votos cada uno. ¿Qué se hace?",
          ["Reconozco el empate.", "Aplico la regla.", "Se vota de nuevo entre Ana y Beto."], "Votar de nuevo entre Ana y Beto"),
    ],
    mistakes=[
        M("Votar por un rumor sin comprobarlo.", "Un rumor puede ser falso.", "Pide evidencia."),
        M("No aceptar el resultado porque ganó otro.", "Las reglas valen para todos.", "Respeta el resultado y colabora."),
    ],
    tiers=tiers(
        [E("Cuando dos candidatos tienen los mismos votos, ¿hay empate o plazo?", "Empate", "Tienen igual cantidad."),
         E("Un dato que apoya una decisión, ¿es evidencia o rumor?", "Evidencia", "Se puede comprobar."),
         E("Lo que sale después de contar los votos, ¿es el resultado o el plazo?", "El resultado", "Es lo que se obtiene del conteo.")],
        [E("¿Qué evidencia puede apoyar tu voto?", "Lo que el candidato hizo antes y si sus propuestas se pueden cumplir", "Son datos comprobables."),
         E("¿Por qué una candidatura debe decir qué no depende del cargo?", "Para no prometer cosas imposibles", "Así es honesta y realista."),
         E("¿Qué debe hacer quien pierde una elección?", "Aceptar el resultado y colaborar", "Respeta las reglas.")],
        [E("Votos de ejemplo: Dora 14, Eli 11, Fer 5. ¿Quién ganó?", "Dora", "14 es el mayor número."),
         arith("Con los votos de ejemplo (Dora 14, Eli 11, Fer 5), ¿cuántos votos más tuvo Dora que Eli?", "14-11", "Se resta los votos de Eli a los de Dora."),
         E("Regla acordada: si hay empate, se vota de nuevo entre empatados. Ana y Beto tienen 10 votos y Cata 4. ¿Entre quiénes se vota de nuevo?", "Entre Ana y Beto", "Ellos son los empatados.")],
        [E("Mía dice: «Votaré por Tomás porque escuché que hace regalos». ¿Qué debe hacer antes de votar?", "Comprobar la información con evidencia", "Un rumor no basta."),
         E("Un candidato prometió reuniones mensuales y después no las hizo. ¿Qué puede hacer el curso: vigilar y reclamar o callarse?", "Vigilar y reclamar", "Los votantes pueden exigir que se cumpla lo prometido.")],
        [E("Ordena los pasos de una elección: A) contar los votos, B) escuchar propuestas, C) votar en secreto.", "B, C, A", "Primero se escucha, luego se vota y después se cuenta."),
         arith("En una elección votaron 30 estudiantes. 14 por Dora, 11 por Eli y el resto por Fer. ¿Cuántos votaron por Fer?", "30-14-11", "Se resta los votos de Dora y de Eli al total.")],
    ),
    context=[E("Un curso de ejemplo eligió presidente a Dora con 14 votos. Eli, que tuvo 11, ofrece ayudar a organizar la reunión de apoderados. ¿Qué actitud muestra: aceptar el resultado y colaborar o rechazarlo?", "Aceptar el resultado y colaborar", "Respeta la decisión del curso.")],
    selfcheck=[E("¿Qué es un empate?", "Cuando dos o más candidatos tienen los mismos votos", "Es la definición del vocabulario."), E("¿Qué debe hacer quien gana?", "Trabajar para todo el curso", "Fue elegido por todos."), E("¿Qué es la evidencia?", "Un dato que apoya una decisión", "Es la definición de la clase.")],
    open_task=task("Elige un cargo (por ejemplo secretaría) y escribe una mini candidatura con: qué harás, cómo lo harás, en qué plazo, qué no depende del cargo y una evidencia de por qué eres idóneo (por ejemplo, «cumplí todas las tareas del último mes»). Luego escribe cómo aceptarías el resultado si no ganas.", "Candidatura a secretaría: anotaré los acuerdos en el cuaderno, cada reunión, este semestre. No puedo cambiar las notas. Evidencia: entregué todas mis tareas. Si no gano, colaboraré.", ["incluye qué, cómo y plazo", "reconoce lo que no depende del cargo", "incluye evidencia y aceptación del resultado"], ["párrafo de cinco frases"], ["prometer algo imposible", "no mencionar la aceptación del resultado"], "Lee tu candidatura a una persona y pídele que diga si le creería."),
    reinforce="Escribe una razón basada en un dato para votar por alguien en una elección de curso.",
    extend="Escribe cómo el curso puede revisar a mitad de año si la directiva cumple.",
)

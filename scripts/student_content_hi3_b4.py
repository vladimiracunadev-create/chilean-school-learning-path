"""Cuaderno del estudiante, 3.º básico Historia, Geografía y Ciencias Sociales: OA 16 (participación responsable en el hogar y la escuela)."""
from __future__ import annotations

from student_content_hi3_b import M, W, tiers
from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA16 = "HI03 OA 16"

register(
    OA16, 1,
    materials="Este cuaderno y un lápiz. Las situaciones del hogar y de la escuela están escritas en los ejercicios.",
    use="Aprenderé a elegir un compromiso que pueda cumplir en mi hogar o en mi escuela. Sirve para participar con responsabilidad sin prometer más de lo que puedo hacer.",
    prior=["Sé qué es un deber y qué es un compromiso.", "Sé que mis acciones tienen consecuencias."],
    explain=[
        "Participar es tomar parte de lo que pasa en mi casa y en mi escuela. En el hogar puedo participar con encargos, como poner la mesa o regar una planta, con celebraciones, como ayudar a decorar, y con el cuidado de las cosas, como guardar mis juguetes. En la escuela puedo participar en campañas solidarias, celebraciones, deportes y juegos.",
        "Un compromiso es una promesa de hacer algo. Un compromiso alcanzable es pequeño, concreto, seguro y adecuado a mi edad. Para saber si lo es me pregunto: ¿puedo hacerlo yo?, ¿tengo el tiempo?, ¿es seguro?, ¿sé cuándo lo haré? Prometer mucho y no cumplir hace perder la confianza.",
        "Participar no es dirigir ni mandar a los demás. Es hacer mi parte y colaborar. Antes de prometer, conviene hablar con la persona adulta o con el grupo para saber qué hace falta. Así el compromiso sirve de verdad.",
    ],
    vocab=[("participar", "tomar parte en lo que ocurre en un grupo"), ("encargo", "tarea pequeña que me corresponde"), ("compromiso alcanzable", "promesa que puedo cumplir"), ("campaña solidaria", "actividad para ayudar a otras personas"), ("colaborar", "hacer mi parte para un trabajo en común")],
    worked=[
        W("Compromiso alcanzable", "Lucas promete: «Haré toda la limpieza de la casa cada día». ¿Es alcanzable? Propón uno mejor.", ["Es muy grande para su edad.", "Algunas tareas no son seguras para un niño.", "Puede prometer: «Guardaré mis juguetes cada tarde»."], "No es alcanzable; mejor: guardar mis juguetes cada tarde"),
        W("Participar sin dirigir", "En una campaña de alimentos, Ana dice: «Yo mando y ustedes traen». ¿Participa bien?", ["Participar es colaborar.", "Ana quiere dirigir sin hacer su parte."], "No; debería hacer también su parte y colaborar"),
    ],
    mistakes=[
        M("Prometer varias tareas grandes para quedar bien.", "No se piensa en el tiempo ni en la edad.", "Elige una tarea pequeña que puedas cumplir."),
        M("Confundir participar con mandar a los demás.", "Se olvida de hacer la propia parte.", "Haz tu parte y colabora."),
    ],
    tiers=tiers(
        [ex("Poner la mesa, ¿es un encargo del hogar o una campaña solidaria?", "Un encargo del hogar", "Es una tarea pequeña de la casa."),
         ex("Juntar alimentos para ayudar a otros, ¿es una campaña solidaria o un juego?", "Una campaña solidaria", "Ayuda a otras personas."),
         ex("Un compromiso alcanzable, ¿se puede cumplir o es imposible?", "Se puede cumplir", "Es pequeño y adecuado a mi edad.")],
        [ex("Con tus palabras, ¿qué es participar?", "Tomar parte en lo que ocurre en un grupo", "Es hacer mi parte."),
         ex("Nombra dos preguntas para saber si un compromiso es alcanzable.", "Por ejemplo: ¿puedo hacerlo yo? y ¿es seguro?", "Son preguntas de la clase."),
         ex("¿Por qué conviene hablar con un adulto antes de prometer?", "Para saber qué hace falta y que el compromiso sirva", "Así se elige bien.")],
        [ex("Ana puede prometer: A) «Regaré la planta de la sala los lunes» o B) «Cuidaré a un bebé solo toda la noche». ¿Cuál es alcanzable?", "A", "B es una tarea de personas adultas."),
         ex("Caso: En el curso se organiza un campeonato de juegos. Beto dice «yo traeré la pelota que sé que tengo». ¿Es un compromiso alcanzable? Responde sí o no.", "Sí", "Es concreto y puede cumplirlo."),
         ex("Caso: Lola quiere ayudar en una celebración de curso. ¿Cuál es una tarea segura para un niño: poner los vasos de plástico en la mesa o encender velas?", "Poner los vasos de plástico en la mesa", "Encender velas es peligroso.")],
        [ex("Rafa dice: «Participar es mandar a todos». ¿Qué corriges?", "Participar es colaborar y hacer mi parte", "No es dirigir."),
         ex("Mía dice: «Si prometo mucho, quedo mejor». ¿Qué problema tiene?", "Puede no cumplir y perder la confianza", "Conviene prometer lo que se puede.")],
        [ex("Escribe un compromiso alcanzable para tu hogar.", "Por ejemplo: guardaré mis zapatos cada noche", "Es pequeño y concreto."),
         ex("Escribe un compromiso alcanzable para una campaña solidaria del curso.", "Por ejemplo: traeré un alimento sellado para la campaña", "Es concreto y seguro.")],
    ),
    context=[ex("El curso hará una campaña de abrigo para personas que lo necesitan. Pedro dice: «Yo traeré una bufanda que ya no uso, limpia y en buen estado». ¿Es un compromiso alcanzable? Explica.", "Sí; es concreto, seguro y puede cumplirlo", "Dice qué traerá y es posible.")],
    selfcheck=[ex("¿Qué es un encargo?", "Una tarea pequeña que me corresponde", "Se hace en casa o en la escuela."), ex("Menciona un ejemplo de campaña solidaria.", "Juntar alimentos o abrigo para ayudar", "Ayuda a otras personas."), ex("¿Participar es lo mismo que mandar?", "No", "Participar es colaborar.")],
    open_task=task("Escribe un compromiso para tu hogar y otro para tu escuela. Elige entre estas ideas o usa otras parecidas: poner la mesa, regar una planta, guardar mis juguetes, traer un alimento sellado para una campaña, ordenar los materiales del curso. Escribe cuándo lo cumplirás.", "En mi hogar: guardaré mis juguetes cada tarde. En mi escuela: ordenaré los materiales del curso los viernes.", ["un compromiso del hogar y uno de la escuela", "ambos son alcanzables y seguros", "dice cuándo se cumplirán"], ["dos compromisos con su momento"], ["prometer algo peligroso", "no decir cuándo"], "Muestra tus compromisos a una persona adulta y pregúntale si te parecen posibles."),
    reinforce="Cumple hoy un pequeño encargo en tu casa y dibuja una cruz si lo lograste.",
    extend="Explica por qué es mejor un compromiso pequeño que se cumple que uno enorme que no se cumple.",
)

register(
    OA16, 2,
    materials="Este cuaderno y un lápiz. Las listas de tareas y los grupos están escritos en los ejercicios.",
    use="Aprenderé a repartir tareas con equidad entre las personas de un grupo. Sirve para que todos participen y nadie cargue con demasiado.",
    prior=["Sé qué es un compromiso alcanzable.", "Sé dividir en grupos iguales con números pequeños."],
    explain=[
        "Cuando un grupo hace una tarea, cada persona tiene un rol: una parte del trabajo. Distribuir con equidad significa repartir las tareas de forma justa, de modo que nadie haga mucho más ni mucho menos que los demás. Equidad no siempre es igual: si alguien no puede cargar peso, le damos otra tarea de similar esfuerzo.",
        "También hay roles en una celebración, como decorar, servir o ordenar, y en deportes y juegos, como anotar el puntaje, repartir los turnos o cuidar los materiales deportivos. Para repartir con equidad hago una lista de las tareas, miro cuántas personas somos, y reparto. A veces conviene que roten: hoy una persona pone la mesa y mañana otra. También escuchamos qué puede y qué le gusta a cada uno, sin obligar. Todos deben poder proponer.",
        "Si el reparto es desigual, lo hablamos con calma y lo cambiamos. Y recordamos algo importante: participar no es mandar. Una persona puede coordinar para ordenar, pero también hace su parte.",
    ],
    vocab=[("rol", "parte del trabajo que le toca a cada persona"), ("equidad", "repartir de manera justa"), ("rotar", "cambiar los roles por turnos"), ("coordinar", "ayudar a organizar el trabajo"), ("lista de tareas", "anotación de lo que hay que hacer")],
    worked=[
        W("Repartir en partes iguales", "Hay 12 tareas para un grupo de 4 personas. ¿Cuántas tareas le toca a cada una?", ["Divido las tareas en partes iguales.", "12 dividido en 4 da 3."], "3 tareas a cada una"),
        W("Equidad no es igual", "Teo tiene un yeso en el brazo y no puede cargar cajas. ¿Qué tarea le damos en una campaña?", ["No puede cargar peso.", "Puede anotar las cosas que llegan, que requiere un esfuerzo parecido."], "Anotar lo que llega, una tarea de esfuerzo parecido sin cargar peso"),
    ],
    mistakes=[
        M("Que una persona mande y los demás hagan todo.", "No es un reparto justo.", "Todos hacen su parte, también quien coordina."),
        M("Dar siempre la tarea más pesada al mismo niño.", "No hay equidad.", "Roten los roles."),
    ],
    tiers=tiers(
        [ex("Repartir de forma justa, ¿es equidad o desorden?", "Equidad", "Nadie carga con demasiado."),
         ex("Rotar las tareas, ¿es cambiar roles por turnos o dejarlas siempre igual?", "Cambiar roles por turnos", "Así se reparte mejor."),
         ex("En un campeonato del curso, anotar el puntaje en una tabla, ¿es un rol del grupo o un premio?", "Un rol del grupo", "Es una parte del trabajo que le toca a una persona.")],
        [ex("¿Por qué la equidad no siempre significa que todos hagan lo mismo?", "Porque cada persona puede distinto", "Se busca un reparto justo."),
         ex("Menciona una forma de repartir tareas de manera justa.", "Rotar los roles o escuchar a cada uno", "Así nadie queda con todo."),
         ex("¿Puede quien coordina no hacer su parte? Responde sí o no.", "No", "Quien coordina también colabora.")],
        [arith("Hay 10 tareas para 5 personas. ¿Cuántas tareas le toca a cada una?", "10//5", "Se reparten en partes iguales."),
         arith("Hay 15 sillas para ordenar entre 3 niños. ¿Cuántas sillas ordena cada niño?", "15//3", "Se divide en partes iguales."),
         arith("Para una celebración hay 20 vasos que hay que poner en la mesa. Los pondrán 4 niños y todos ponen la misma cantidad. ¿Cuántos vasos pone cada niño?", "20//4", "Se reparten en partes iguales.")],
        [ex("Laura dice: «Yo mando y los demás hacen todo». ¿Qué corriges?", "Quien coordina también hace su parte", "No se reparte con equidad."),
         ex("Raúl hizo 5 tareas y sus tres compañeros hicieron una cada uno. ¿El reparto es justo? Responde sí o no.", "No", "Raúl hizo mucho más que los demás.")],
        [ex("En un grupo de 3 hay 9 tareas. Hoy Lía hizo 4, Teo 3 y Eli 2. Escribe cómo repartirlas mejor para que cada uno haga 3.", "Lía 3, Teo 3 y Eli 3", "9 dividido en 3 da 3."),
         ex("Plan de rotación: lunes pone la mesa Ana, martes Beto, miércoles Eli. ¿Quién la pone el jueves si siguen el mismo orden?", "Ana", "Después de Eli vuelve a empezar Ana.")],
    ),
    context=[arith("Para una celebración del curso hay 8 tareas y 4 estudiantes. Si reparten las tareas en partes iguales, ¿cuántas tareas hace cada estudiante?", "8//4", "Se divide el total entre el número de estudiantes.")],
    selfcheck=[ex("¿Qué es equidad?", "Repartir de manera justa", "Nadie hace demasiado."), ex("En Historia: ¿Qué significa rotar?", "Cambiar los roles por turnos", "Así todos prueban distintas tareas."), ex("¿Quién coordina hace su parte?", "Sí", "Participar es colaborar.")],
    open_task=task("Reparte con equidad estas 6 tareas de una campaña de abrigo entre 3 niños (Ana, Beto y Cami): anotar lo que llega, doblar prendas, contar prendas, hacer carteles, ordenar cajas livianas, agradecer a quienes traen. Cada uno hace 2. Escribe quién hará qué y una regla para cambiar los roles la próxima vez.", "Ana: anotar y contar. Beto: doblar y ordenar cajas livianas. Cami: carteles y agradecer. La próxima semana rotamos los roles.", ["cada niño tiene 2 tareas", "las tareas son seguras", "incluye una regla de rotación"], ["lista de tareas por persona", "regla"], ["dar más tareas a una persona", "tareas peligrosas"], "Pide a una persona que revise si todos tienen la misma cantidad de tareas."),
    reinforce="Reparte con una persona de tu casa dos tareas pequeñas en partes justas.",
    extend="Explica la diferencia entre repartir en partes iguales y repartir con equidad.",
)

register(
    OA16, 3,
    materials="Este cuaderno y un lápiz. Los acuerdos y el registro están escritos en los ejercicios.",
    use="Aprenderé a cumplir los acuerdos y a registrarlos para comprobar que se cumplieron. Sirve para participar con seguimiento.",
    prior=["Sé elegir un compromiso alcanzable.", "Sé repartir tareas con equidad."],
    explain=[
        "Un acuerdo es una decisión que un grupo toma entre todos. Cuando hay un acuerdo, cada persona sabe qué tiene que hacer y cuándo. Para cumplir, conviene anotarlo en una lista: quién, qué y para cuándo. Así no dependemos de la memoria.",
        "El seguimiento es mirar cada cierto tiempo cómo vamos. Podemos usar un registro: una tabla donde marcamos con una cruz lo que ya se hizo. Si alguien no puede cumplir, avisa antes, y el grupo busca cómo resolverlo. Avisar a tiempo es parte de ser responsable.",
        "Al final contamos lo cumplido y lo pendiente. Si falta mucho trabajo, hablamos y lo organizamos. Cumplir un compromiso en el hogar o en la escuela ayuda a que todos confíen en mí.",
    ],
    vocab=[("acuerdo", "decisión que se toma entre todos"), ("registro", "anotación de lo que se hizo"), ("seguimiento", "mirar cada tanto cómo va el trabajo"), ("pendiente", "lo que aún falta hacer"), ("avisar", "decir a tiempo que algo no podrá cumplirse")],
    worked=[
        W("Contar lo cumplido", "Registro de una campaña: Ana ✓, Beto ✓, Cami ✗, Dani ✓. ¿Cuántos cumplieron y cuántos están pendientes?", ["Cuento las marcas ✓: 3.", "Falta Cami: 1."], "Cumplieron 3; está pendiente 1"),
        W("Avisar a tiempo", "Teo prometió traer un cartel el viernes, pero se enfermó. ¿Qué debe hacer?", ["No puede cumplir.", "Debe avisar antes.", "El grupo busca otra solución."], "Avisar a tiempo para que el grupo busque otra solución"),
    ],
    mistakes=[
        M("No anotar los acuerdos y confiar en la memoria.", "Se olvidan fácilmente.", "Escribe quién, qué y para cuándo."),
        M("Avisar cuando ya es tarde.", "El grupo ya no puede reaccionar.", "Avisa apenas sepas que no podrás."),
    ],
    tiers=tiers(
        [ex("Un acuerdo, ¿se toma entre todos o lo decide uno solo?", "Entre todos", "Es una decisión del grupo."),
         ex("Un registro, ¿sirve para anotar lo que se hizo o para jugar?", "Para anotar lo que se hizo", "Es una evidencia."),
         ex("Avisar a tiempo, ¿es parte de ser responsable o una falta?", "Parte de ser responsable", "Permite buscar solución.")],
        [ex("¿Qué tres datos anoto en un acuerdo?", "Quién, qué y para cuándo", "Son los datos de la clase."),
         ex("¿Para qué sirve el seguimiento?", "Para ver cómo va el trabajo", "Permite corregir a tiempo."),
         ex("¿Qué hago si no puedo cumplir un compromiso?", "Aviso antes al grupo", "Así buscamos una solución.")],
        [ex("Registro: Pía ✓, Luis ✗, Eli ✓, Rafa ✓, Mía ✗. ¿Cuántos cumplieron?", "3", "Hay tres marcas ✓."),
         ex("Mismo registro: Pía ✓, Luis ✗, Eli ✓, Rafa ✓, Mía ✗. ¿Cuántos están pendientes?", "2", "Hay dos marcas ✗."),
         ex("Acuerdo escrito: «Ana trae cartulina el lunes». Es martes y Ana no la trajo. ¿Qué debería haber hecho?", "Avisar antes del lunes", "Así el grupo buscaba otra cartulina.")],
        [ex("Gabo dice: «Me acuerdo de todo, no necesito anotar». ¿Qué le explicas?", "Anotar ayuda a no olvidar y a que todos lo vean", "La memoria falla."),
         ex("Sofía no cumplió y no dijo nada. ¿Qué problema hay?", "El grupo no pudo buscar una solución", "Ella debía avisar antes.")],
        [ex("Escribe un acuerdo con quién, qué y para cuándo, para una celebración del curso.", "Por ejemplo: Beto trae los vasos de plástico el viernes", "Incluye los tres datos."),
         arith("Un registro tiene 8 compromisos. Se cumplieron 5. ¿Cuántos faltan?", "8-5", "Se resta lo cumplido del total.")],
    ),
    context=[ex("Un curso organiza una campaña de alimentos. Tiene 10 cajas por llenar y ya llenó 6. ¿Cuántas cajas están pendientes?", "4", "10 menos 6 da 4.", calc="10-6")],
    selfcheck=[ex("En Historia: ¿Qué es un acuerdo?", "Una decisión que se toma entre todos", "Es del grupo."), ex("¿Qué es un pendiente?", "Lo que aún falta hacer", "Se anota en el registro."), ex("¿Cuándo debo avisar que no cumpliré?", "Lo antes posible", "Así el grupo puede reaccionar.")],
    open_task=task("Completa un registro de una semana para un acuerdo del curso. Escribe tres compromisos (quién, qué, para cuándo) y deja una columna con casilla para marcar cuando se cumple. Marca los que ya hayas cumplido y cuenta cuántos cumplieron y cuántos faltan.", "1) Ana trae cartulina el lunes ✓. 2) Beto trae marcadores el martes ✓. 3) Cami trae cinta el miércoles ✗. Cumplieron 2 y falta 1.", ["tres compromisos con quién, qué y cuándo", "registro con marcas", "conteo de cumplidos y pendientes"], ["tabla con tres filas", "frase con el conteo"], ["no anotar cuándo", "no contar"], "Revisa con una persona adulta que cada fila diga quién, qué y cuándo."),
    reinforce="Anota un acuerdo de tu casa en un papel y pégalo donde se vea.",
    extend="Explica por qué el seguimiento ayuda a cumplir los acuerdos.",
)

register(
    OA16, 4,
    materials="Este cuaderno y un lápiz. La pauta de evaluación está escrita en los ejercicios.",
    use="Aprenderé a evaluar mi aporte en un trabajo en grupo y a decidir cómo mejorar. Sirve para participar mejor la próxima vez.",
    prior=["Sé cumplir y registrar acuerdos.", "Sé que equivocarse ayuda a aprender."],
    explain=[
        "Evaluar mi aporte es mirar qué hice, cómo lo hice y qué puedo mejorar. No es ponerme una nota de castigo. Sirve para aprender. Puedo preguntarme: ¿cumplí mi compromiso?, ¿colaboré con los demás?, ¿escuché a mis compañeros?, ¿qué haría distinto?",
        "Una evaluación honesta incluye lo que salió bien y lo que puede mejorar. Anoto una evidencia: por ejemplo, «traje los materiales los cuatro días». Y escribo una mejora concreta: «dejaré mi mochila lista la noche anterior». También agradezco el aporte de otras personas del grupo.",
        "Participar bien en el hogar y la escuela se nota en celebraciones, campañas solidarias, deportes y juegos. En un juego de equipo, mi aporte puede ser respetar las reglas, esperar mi turno, animar a los demás y aceptar el resultado con respeto.",
    ],
    vocab=[("aporte", "lo que cada persona entrega a un trabajo en común"), ("evaluar", "mirar cómo resultó algo para aprender"), ("mejora", "cambio que hace algo mejor"), ("evidencia", "señal que prueba que algo se hizo"), ("agradecer", "reconocer lo que otra persona hizo")],
    worked=[
        W("Evaluar con evidencia", "Beto pregunta: «¿Cumplí?». Registro: llevó los materiales 3 de 4 días. ¿Qué evidencia puede escribir?", ["Cuento los días: 3 de 4.", "Escribo el dato exacto."], "Llevé los materiales 3 de 4 días"),
        W("Mejora concreta", "Cami olvidó una tarea. ¿Cuál es una mejora concreta: A) «Seré mejor» o B) «Pondré un recordatorio en mi mochila»?", ["La A es muy general.", "La B dice qué hará."], "B"),
    ],
    mistakes=[
        M("Evaluar solo lo malo o solo lo bueno.", "La evaluación queda incompleta.", "Anota lo que salió bien y lo que mejorarías."),
        M("Culpar a los demás de lo que no salió bien.", "No se revisa mi propio aporte.", "Mira primero tu parte."),
    ],
    tiers=tiers(
        [ex("Evaluar mi aporte, ¿sirve para aprender o para castigarme?", "Para aprender", "Busca mejorar el aporte."),
         ex("Agradecer, ¿es reconocer lo que otro hizo o ignorarlo?", "Reconocer lo que otro hizo", "Valora su aporte."),
         ex("Una mejora, ¿es un cambio para hacer algo mejor o algo que no cambia?", "Un cambio para hacer algo mejor", "Así se definió.")],
        [ex("Nombra dos preguntas para evaluar mi aporte.", "Por ejemplo: ¿cumplí mi compromiso? y ¿colaboré?", "Son preguntas de la clase."),
         ex("¿Por qué conviene escribir una evidencia?", "Para saber con datos si cumplí", "Los datos ayudan a evaluar."),
         ex("Menciona una forma de aportar en un juego de equipo.", "Respetar las reglas o esperar mi turno", "Es un aporte al equipo.")],
        [ex("Registro de Ana: llevó el cuaderno 4 de 5 días. ¿Cuántos días faltó?", "1", "5 menos 4 da 1.", calc="5-4"),
         ex("Elige la mejora concreta: A) «Participaré mejor» o B) «Dejaré lista mi mochila la noche anterior».", "B", "B dice qué hará."),
         ex("Después de un juego, un niño pierde y dice «felicitaciones» al otro equipo. ¿Qué aporte hizo: aceptar el resultado con respeto o hacer trampa?", "Aceptar el resultado con respeto", "Es una forma de participar bien.")],
        [ex("Rafa dice: «Todo salió mal por mis compañeros». ¿Qué le falta revisar?", "Su propio aporte", "Debe mirar qué hizo él."),
         ex("Mía solo anotó lo que salió mal. ¿Qué falta?", "Lo que salió bien", "Una evaluación honesta incluye ambas cosas.")],
        [ex("Evalúa este caso: Lía cumplió su tarea, escuchó a sus compañeros pero llegó tarde dos veces. Escribe una cosa buena y una mejora.", "Cumplió y escuchó; mejorar la puntualidad", "Incluye lo bueno y una mejora."),
         ex("Escribe una mejora concreta para quien olvida traer sus materiales.", "Por ejemplo: dejar la mochila lista la noche anterior", "Dice qué hará.")],
    ),
    context=[ex("Después de una campaña de abrigo, un curso reunió 20 prendas el primer día y 15 el segundo. ¿Cuántas prendas juntó el curso en total?", "35", "20 más 15 suma 35.", calc="20+15")],
    selfcheck=[ex("¿Qué es un aporte?", "Lo que cada persona entrega a un trabajo en común", "Cada uno colabora."), ex("¿Qué incluye una evaluación honesta?", "Lo que salió bien y lo que puede mejorar", "Así la evaluación es completa."), ex("¿Evaluar es lo mismo que castigarse?", "No", "Sirve para aprender.")],
    open_task=task("Evalúa tu aporte en una tarea reciente de tu hogar o de tu escuela. Completa: 1) Mi compromiso era..., 2) Lo cumplí en... de... días, 3) Lo que salió bien fue..., 4) Mejoraré así... Usa números verdaderos de tu registro.", "Mi compromiso era guardar mis juguetes. Lo cumplí 4 de 5 días. Salió bien que lo hice rápido. Mejoraré dejando una caja cerca de mi cama.", ["completa las cuatro partes", "incluye un dato numérico", "propone una mejora concreta"], ["cuatro frases completas"], ["no incluir mejora", "culpar a otros"], "Comparte tu evaluación con una persona de tu casa y escucha qué mejora sugiere."),
    reinforce="Agradece hoy a una persona por su aporte en tu casa o en tu escuela.",
    extend="Explica cómo cambiaría tu aporte si volvieras a hacer la misma tarea.",
)

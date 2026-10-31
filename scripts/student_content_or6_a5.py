"""Cuaderno del estudiante, 6.º básico Orientación: OA 09 (hábitos y actitudes que favorecen el aprendizaje y los intereses)."""
from __future__ import annotations

from student_lessons import arith, ex
from student_content_or6_a import M, T, W, lesson

OA9 = "OR06 OA 09"

lesson(
    OA9, 1,
    "Una hoja y un lápiz. El caso de Rocío y la lista de metas están escritos en los ejercicios. Trabajas con un personaje inventado.",
    "Aprenderé a establecer metas de aprendizaje claras y a revisarlas. Sirve para saber qué quiero lograr, cómo lo haré y si voy avanzando.",
    ["Sé que puedo mejorar con práctica.", "Sé escribir una meta con plazo."],
    [
        "Una meta de aprendizaje es lo que quiero lograr en un tiempo determinado. Sirve para dirigir mi esfuerzo y saber si avanzo. Una buena meta es específica, es decir, dice qué voy a aprender; medible, porque tiene una cantidad o una señal; posible, porque puedo cumplirla con mi tiempo y mis recursos; y con plazo, porque dice hasta cuándo. «Mejorar en Matemática» es vaga. «Resolver bien 8 de 10 problemas de la guía en tres semanas» es una meta clara.",
        "Para lograrla conviene dividirla en pasos pequeños. Si la meta es leer un libro de 120 páginas en 4 semanas, se pueden leer 30 páginas por semana, o unas 5 páginas por día durante 6 días. También hay que revisar el avance cada cierto tiempo: si voy atrasado, ajusto el plan; si voy bien, lo celebro. Una meta se puede cambiar si cambian las condiciones, siempre que no sea solo por flojera.",
        "Las metas deben ser propias. Cuando tú las eliges, te importan más. Pero también puedes pedir ayuda a tu profesor o a una persona de tu casa para ajustarlas. Escribir la meta y colocarla en un lugar visible ayuda a recordarla.",
    ],
    [("meta de aprendizaje", "lo que quiero lograr aprender en un tiempo determinado"), ("específica", "que dice con claridad qué voy a hacer"), ("medible", "que tiene una cantidad o señal para comprobar"), ("plazo", "fecha en que reviso mi meta"), ("avance", "paso que me acerca a mi meta")],
    [
        W("Elegir la meta clara", "Rocío debe elegir entre dos metas: «Leer más» o «Leer 15 páginas de lunes a jueves durante 3 semanas». ¿Cuál es clara?", ["La segunda dice qué, cuánto y hasta cuándo.", "La primera es vaga.", "Una meta clara se puede comprobar."], "«Leer 15 páginas de lunes a jueves durante 3 semanas»"),
        W("Dividir una meta", "Rocío quiere leer 120 páginas en 4 semanas. ¿Cuántas páginas debe leer por semana?", ["Se reparte el total en partes iguales.", "120 ÷ 4 = 30.", "Debe leer 30 páginas por semana."], "30 páginas por semana"),
    ],
    [
        M("Ponerme una meta enorme para sentirme motivado.", "Se cree que cuanto más grande, mejor.", "Elige una meta posible y ajústala si hace falta."),
        M("Anotar la meta y no volver a mirarla.", "Se olvida revisarla.", "Revisa tu avance en fechas fijas."),
    ],
    R=[
        ex("«Mejorar en Lenguaje». ¿Es una meta específica o vaga?", "Vaga", "No dice qué ni cuánto."),
        ex("¿Una buena meta tiene plazo? Responde sí o no.", "Sí", "Con plazo se puede revisar."),
        ex("¿Dividir una meta en pasos pequeños la hace más fácil de cumplir? Responde sí o no.", "Sí", "Los pasos pequeños son más manejables."),
    ],
    U=[
        ex("¿Por qué una meta medible ayuda a saber si avanzo?", "Porque tiene una cantidad que puedo comprobar", "Se puede contar lo logrado."),
        ex("¿Por qué conviene revisar el avance cada cierto tiempo?", "Para ajustar el plan a tiempo", "Si voy atrasado, puedo corregir."),
        ex("¿Por qué una meta propia suele motivar más que una impuesta?", "Porque me importa a mí", "Elegirla genera compromiso."),
    ],
    A=[
        ex("Metas: A) «Estudiar más»; B) «Resolver 10 ejercicios de fracciones cada martes durante 4 semanas»; C) «Ser el mejor». ¿Cuál es una meta clara?", "B", "Dice qué, cuánto, cuándo y por cuánto tiempo."),
        arith("Una meta es leer 90 páginas en 3 semanas, en partes iguales. ¿Cuántas páginas por semana?", "90//3", "Se divide el total entre las semanas."),
        ex("Ema se propuso practicar escritura 20 minutos al día. A la semana 2, solo lo hizo 3 días de 7. ¿Qué es mejor: ajustar la meta a 10 minutos o abandonarla?", "Ajustar la meta a 10 minutos", "Ajustar permite seguir avanzando."),
    ],
    Z=[
        ex("¿Por qué una meta sin plazo se vuelve fácil de olvidar?", "Porque no hay un momento para revisarla", "El plazo marca cuándo comprobar."),
        ex("¿Por qué es bueno pedir ayuda a un adulto para ajustar una meta?", "Porque puede ayudar a que sea posible", "Otra mirada ayuda a calibrarla."),
    ],
    D=[
        arith("Rocío lee 5 páginas por día durante 6 días. ¿Cuántas páginas lee en total?", "5*6", "Se multiplican las páginas por los días."),
        arith("Otra estudiante se propuso leer 200 páginas en un mes y lleva 85. ¿Cuántas páginas le faltan?", "200-85", "Se resta lo leído a la meta."),
    ],
    context=[ex("Tomás quiere mejorar su ortografía. Escribe: «Escribir 6 palabras difíciles cada día y revisarlas el viernes durante 4 semanas». ¿Su meta es específica, medible y con plazo?", "Sí", "Dice qué, cuántas, cuándo y por cuánto tiempo.")],
    selfcheck=[ex("En Orientación: ¿una meta de aprendizaje tiene plazo?", "Sí", "Permite revisar el avance."), ex("¿Una meta vaga es mejor que una específica?", "No", "No se puede comprobar."), ex("¿Es posible ajustar una meta?", "Sí", "Si las condiciones cambian.")],
    task=T("Elige un tema que quieras mejorar en un personaje inventado llamado Dani (por ejemplo, la lectura en voz alta o las tablas de multiplicar). Escribe una meta clara (qué, cuánto, cuándo y plazo), tres pasos pequeños para lograrla y cómo revisará su avance cada semana.", "Meta: leer en voz alta 10 minutos de lunes a jueves durante 3 semanas. Pasos: elegir un libro corto, leer frente a un espejo y pedir a una persona de su casa que lo escuche. Revisión: cada viernes anotar cuántos días cumplió.", ["meta con qué, cuánto, cuándo y plazo", "tres pasos pequeños", "una forma de revisar", "no cuenta una vivencia propia"], ["texto escrito"], ["meta sin plazo", "pasos imposibles"], "Reconoce la claridad y pregunta cómo ajustaría la meta si no alcanza."),
    reinforce="Escribe tres metas de aprendizaje con qué, cuánto, cuándo y plazo para un personaje inventado.",
    extend="Explica por qué una meta puede ajustarse sin que eso signifique rendirse.",
)

lesson(
    OA9, 2,
    "Una hoja y un lápiz. El horario de Camila y las tareas están escritos en los ejercicios.",
    "Aprenderé a estudiar con anticipación y a organizar mi tiempo con un horario. Sirve para evitar el apuro de última hora y aprender mejor.",
    ["Sé escribir una meta con plazo.", "Sé calcular minutos y horas."],
    [
        "Estudiar con anticipación significa empezar a preparar una prueba o un trabajo varios días antes y no la noche anterior. Así el cerebro tiene tiempo de aprender, repasar y descansar. Estudiar muchas horas seguidas el último día cansa y se olvida más rápido. En cambio, estudiar un poco cada día durante varios días ayuda a recordar mejor.",
        "Para organizar el tiempo conviene hacer un horario semanal. Primero anota lo que debes hacer y la fecha límite de cada cosa. Luego calcula cuánto tiempo necesita cada una. Reparte las tareas en los días disponibles, dejando tiempo para descansar, comer y jugar. Prioriza lo más urgente y lo más difícil. Es útil estudiar en periodos de unos 25 a 30 minutos con pausas cortas de 5 minutos.",
        "También ayudan algunos hábitos: tener un lugar tranquilo, guardar el celular si no se necesita y preparar el material antes de empezar. Si un plan no funciona, se ajusta. Un horario no es una cárcel, es una guía que te permite usar mejor tu tiempo.",
    ],
    [("anticipación", "hacer algo con tiempo antes de la fecha límite"), ("horario", "plan que reparte las tareas en días y horas"), ("prioridad", "lo que debo hacer primero por ser urgente o importante"), ("pausa", "descanso corto entre periodos de estudio"), ("repasar", "volver a estudiar lo ya visto")],
    [
        W("Repartir el estudio", "Camila tiene prueba el viernes y necesita 2 horas de estudio en total. ¿Es mejor estudiar 2 horas el jueves en la noche o 30 minutos cada día de lunes a jueves?", ["30 minutos × 4 días = 120 minutos = 2 horas.", "Estudiar un poco cada día ayuda a recordar.", "Estudiar todo la noche anterior cansa."], "30 minutos cada día de lunes a jueves"),
        W("Priorizar", "Camila tiene: una prueba el jueves, una tarea para el lunes siguiente y leer un libro por gusto. ¿Qué debe hacer primero?", ["La prueba del jueves es lo más cercano.", "La tarea tiene más plazo.", "El libro por gusto no tiene fecha."], "Estudiar para la prueba del jueves"),
    ],
    [
        M("Dejar todo para la noche anterior porque 'me rinde más'.", "Se confunde el apuro con eficacia.", "Reparte el estudio en varios días."),
        M("Hacer un horario tan lleno que no deja descanso.", "Se cree que más horas es mejor.", "Incluye pausas, comida y tiempo libre."),
    ],
    R=[
        ex("Estudiar un poco cada día, ¿es mejor que estudiar todo la noche anterior? Responde sí o no.", "Sí", "Ayuda a recordar mejor y cansa menos."),
        ex("Lo que debo hacer primero por ser urgente se llama prioridad. ¿Es verdadero?", "Sí", "Prioridad es lo que va primero."),
        ex("¿Un horario debe incluir descanso? Responde sí o no.", "Sí", "El descanso ayuda a aprender."),
    ],
    U=[
        ex("¿Por qué conviene hacer pausas cortas entre periodos de estudio?", "Porque descansar ayuda a concentrarse", "Después de la pausa se aprende mejor."),
        ex("¿Por qué conviene guardar el celular al estudiar si no se necesita?", "Porque distrae", "Evita interrumpir la concentración."),
        ex("Si un plan no funciona, ¿qué se hace: ajustarlo o culparse?", "Ajustarlo", "El plan es una guía que se mejora."),
    ],
    A=[
        ex("Tareas: 1) prueba de Ciencias el miércoles; 2) cartel para el viernes; 3) leer por gusto. ¿Cuál va primero en el horario?", "La prueba de Ciencias", "Es la fecha más cercana."),
        arith("Camila estudia 25 minutos y descansa 5. Repite el ciclo 3 veces. ¿Cuántos minutos pasan en total?", "(25+5)*3", "Cada ciclo dura 30 minutos y son tres."),
        arith("Un horario dice: lunes 40 min Matemática, martes 30 min Lenguaje, miércoles 40 min Matemática. ¿Cuántos minutos de Matemática hay?", "40+40", "Se suman solo los días de Matemática."),
    ],
    Z=[
        ex("¿Por qué estudiar 3 horas seguidas sin pausa suele ser menos eficaz que 3 periodos de 1 hora con pausas?", "Porque el cansancio baja la concentración", "Las pausas ayudan a mantener atención."),
        ex("¿Por qué conviene dejar tiempo libre en el horario?", "Porque el descanso y el juego también son necesarios", "Evita el agotamiento."),
    ],
    D=[
        arith("Camila estudia 35 minutos por día durante 4 días. ¿Cuántos minutos estudió?", "35*4", "Se multiplican los minutos por los días."),
        arith("Tiene 3 horas libres el sábado, o 180 minutos, y usa 100 para estudiar. ¿Cuántos minutos le quedan libres?", "180-100", "Se restan los minutos de estudio al total."),
    ],
    context=[ex("Ema tiene una prueba el viernes. Hace un horario: lunes 30 min, martes 30 min, miércoles 30 min y jueves repaso de 20 min. ¿Estudió con anticipación?", "Sí", "Repartió el estudio en cuatro días antes de la prueba.")],
    selfcheck=[ex("En Orientación: ¿estudiar con anticipación es empezar días antes?", "Sí", "Da tiempo de repasar."), ex("¿Un horario debe dejar tiempo para descansar?", "Sí", "El descanso ayuda."), ex("¿Estudiar solo la noche anterior es lo mejor?", "No", "Se olvida más rápido.")],
    task=T("Haz un horario semanal inventado para Luz, que tiene: prueba de Ciencias el jueves, un cartel de Artes para el viernes y lectura de 40 páginas para el lunes siguiente. Reparte las tareas de lunes a jueves con minutos, incluye pausas y un momento de descanso o juego.", "Lunes: Ciencias 30 min y leer 10 páginas. Martes: Ciencias 30 min y leer 10 páginas. Miércoles: repaso de Ciencias 20 min, cartel 30 min y leer 10 páginas. Jueves: cartel 30 min y leer 10 páginas (40 en total). Pausas de 5 minutos y descanso o juego cada tarde.", ["reparte las tareas en días y minutos", "incluye pausas o descanso", "prioriza la prueba", "no cuenta una vivencia propia"], ["horario escrito"], ["dejar todo para el último día", "horario sin descanso"], "Reconoce el horario y pregunta qué ajustaría si falta tiempo."),
    reinforce="Haz un horario de tres días para estudiar una prueba, con minutos y pausas.",
    extend="Explica por qué la organización del tiempo también cuida tu ánimo.",
)

lesson(
    OA9, 3,
    "Una hoja y un lápiz. El caso del trabajo grupal y las normas están escritos en los ejercicios.",
    "Aprenderé a trabajar en forma colaborativa y a respetar el estudio y el trabajo de otros. Sirve para lograr mejores resultados y cuidar la convivencia.",
    ["Sé organizar mi tiempo.", "Sé escuchar y respetar opiniones."],
    [
        "Trabajar de forma colaborativa es que cada integrante aporta algo y todos comparten un mismo objetivo. No es dividir el trabajo para que cada uno haga lo suyo sin hablar; ni que uno haga todo. Para colaborar, el grupo acuerda el objetivo, reparte tareas según intereses y habilidades, fija plazos y se reúne para unir las partes y revisar. Cada persona responde por su parte y también ayuda cuando alguien tiene dificultades.",
        "En el trabajo grupal, respetar significa escuchar las ideas de todos, hablar por turnos, cumplir lo prometido y reconocer el aporte de cada uno. Si alguien no avanza, el grupo conversa y busca apoyo, sin burlarse. El respeto también se extiende al estudio de los demás: no hacer ruido que moleste, no interrumpir a quien está concentrado, no esconder ni tomar sin permiso sus materiales y no mirar sus respuestas en una evaluación.",
        "Cuando un grupo funciona bien, todos aprenden más. Evaluar el trabajo en equipo, por ejemplo, con preguntas como «¿cumplimos nuestras tareas?» y «¿todos fueron escuchados?», ayuda a mejorar la próxima vez.",
    ],
    [("colaborar", "trabajar juntos con un mismo objetivo y aportes de todos"), ("aporte", "lo que cada integrante pone en el trabajo"), ("turno", "momento que le toca a cada persona para hablar"), ("respeto", "tratar con cuidado el trabajo y el estudio de otros"), ("evaluar", "revisar cómo funcionó el trabajo en equipo")],
    [
        W("Reconocer colaboración", "En un grupo de 4, Beto hace todo mientras los demás conversan. ¿Es trabajo colaborativo?", ["Solo una persona trabaja.", "Los otros no aportan.", "No es colaborativo."], "No, no es trabajo colaborativo"),
        W("Respetar el estudio de otro", "Ema está concentrada resolviendo una guía. ¿Qué conducta respeta su estudio: hablar bajo o gritarle una broma?", ["Gritar interrumpe su concentración.", "Hablar bajo no la molesta.", "Respetar es no distraer."], "Hablar bajo"),
    ],
    [
        M("Creer que colaborar es dividir y no hablar más.", "Se piensa que cada uno hace lo suyo sin revisar.", "Reúnanse para unir las partes y revisar juntos."),
        M("Copiarle a un compañero 'para ayudarlo'.", "Se confunde ayudar con hacer por el otro.", "Explícale cómo hacerlo, sin darle la respuesta."),
    ],
    R=[
        ex("Trabajar juntos con un mismo objetivo y aportes de todos, ¿es colaborar o competir?", "Colaborar", "Todos aportan al objetivo común."),
        ex("¿Respetar el estudio de otros incluye no interrumpir a quien está concentrado? Responde sí o no.", "Sí", "Permite que todos aprendan."),
        ex("¿Mirar las respuestas de otro en una evaluación respeta su trabajo? Responde sí o no.", "No", "Es copiar y no respeta el esfuerzo del otro."),
    ],
    U=[
        ex("¿Por qué conviene repartir tareas según intereses y habilidades?", "Porque cada uno aporta mejor", "El grupo aprovecha las fortalezas."),
        ex("Si un integrante no avanza, ¿qué conviene hacer: burlarse o conversar y buscar apoyo?", "Conversar y buscar apoyo", "Busca soluciones sin humillar."),
        ex("¿Por qué conviene evaluar el trabajo en equipo al terminar?", "Para mejorar la próxima vez", "Se detecta qué funcionó y qué no."),
    ],
    A=[
        ex("Conductas: 1) hablar por turnos; 2) hacer todo uno solo; 3) reconocer el aporte de otro; 4) tomar sin permiso un material ajeno; 5) cumplir la tarea prometida. ¿Cuántas son colaborativas y respetuosas?", "3", "Los números 1, 3 y 5 lo son."),
        ex("Un grupo de 4 tiene que armar un cartel con título, dibujo, texto y bordes. ¿Cuál reparto es mejor? A) Cada uno según su habilidad y luego unen todo. B) Uno hace todo. C) Nadie hace nada hasta el último día.", "A", "Reparte tareas y luego integra."),
        ex("Tomás no entendió una tarea y le pide ayuda a Dani. ¿Qué respuesta ayuda mejor? A) «Copia la mía». B) «Te explico cómo lo hice, y luego tú la haces». C) «No me molestes».", "B", "Explica sin dar la respuesta."),
    ],
    Z=[
        ex("¿Por qué «dividir y no volver a hablar» puede arruinar un trabajo grupal?", "Porque las partes pueden no encajar", "Falta unir y revisar juntos."),
        ex("¿Por qué ayudar a un compañero no es lo mismo que hacerle la tarea?", "Porque la ayuda lo hace aprender", "Hacerle la tarea no le enseña."),
    ],
    D=[
        arith("Un grupo de 5 estudiantes tiene 60 minutos y cada uno usa 12 minutos en su parte. ¿Cuántos minutos usan entre todos?", "5*12", "Se multiplican los integrantes por los minutos de cada uno."),
        arith("El trabajo tiene 20 preguntas y 4 integrantes se reparten por igual. ¿Cuántas responde cada uno?", "20//4", "Se divide el total entre los integrantes."),
    ],
    context=[ex("Un grupo reparte un trabajo: Luz investiga, Teo escribe, Mati dibuja y Camila revisa. Al final se reúnen, unen las partes y revisan juntos. ¿Trabajaron de forma colaborativa?", "Sí", "Repartieron tareas, aportaron todos y revisaron juntos.")],
    selfcheck=[ex("En Orientación: ¿colaborar significa que todos aportan?", "Sí", "Es trabajo conjunto."), ex("¿Ayudar es lo mismo que hacer la tarea del otro?", "No", "La ayuda enseña."), ex("¿Respetar el estudio de otros es parte del aprendizaje?", "Sí", "Permite que todos se concentren.")],
    task=T("Un grupo inventado de cuatro personas (Ema, Luz, Teo y Mati) debe preparar una exposición sobre el reciclaje. Escribe el reparto de tareas, dos normas para respetar el estudio y el trabajo de los demás y tres preguntas para evaluar el trabajo en equipo al final.", "Reparto: Ema investiga, Luz escribe, Teo prepara láminas, Mati ensaya la presentación. Normas: hablar por turnos y no tomar materiales sin permiso. Preguntas: ¿cumplimos nuestras tareas? ¿todos fueron escuchados? ¿qué mejoraríamos?", ["reparte las tareas", "incluye dos normas de respeto", "formula tres preguntas de evaluación", "no cuenta una vivencia propia"], ["lista escrita"], ["que uno haga todo", "normas vagas"], "Reconoce el reparto y pregunta cómo resolverían si alguien no cumple."),
    reinforce="Escribe cinco normas para respetar el estudio y el trabajo de los demás.",
    extend="Explica la diferencia entre ayudar a un compañero y dejar que copie.",
)

lesson(
    OA9, 4,
    "Una hoja y un lápiz. Los textos de ejemplo y las listas de fuentes están escritos en los ejercicios. Todos los textos son originales y breves.",
    "Aprenderé a evitar el plagio y la copia: qué son, cómo citar la fuente y cómo escribir con mis propias palabras. Sirve para ser honesto y aprender de verdad.",
    ["Sé buscar información en fuentes confiables.", "Sé trabajar de forma colaborativa."],
    [
        "Copiar es usar el trabajo o las respuestas de otro como si fueran tuyos, por ejemplo, mirar las respuestas de un compañero en una prueba. El plagio es presentar como propias las palabras o ideas de otra persona sin decir de dónde las sacaste, por ejemplo, copiar un párrafo de internet y entregarlo sin avisar. Ambos son faltas de honestidad y no te permiten aprender; además dañan el esfuerzo de quien hizo el trabajo.",
        "Es válido usar información de libros o de internet si respetas el trabajo del autor. Hay dos formas. Una es parafrasear: leer la idea, entenderla y explicarla con tus propias palabras, cambiando la forma y no solo algunas palabras. Siempre debes decir de dónde la sacaste. La otra es citar: copiar una frase exacta entre comillas e indicar la fuente, con autor, título y fecha o sitio. Por ejemplo: «El agua cubre gran parte del planeta» (Libro de Ciencias del curso).",
        "Para evitar el plagio: anota la fuente mientras investigas, usa tus palabras, pon comillas si copias algo exacto y escribe al final la lista de fuentes. Si no estás seguro de cómo citar algo, pregunta a tu profesor o profesora. Hacer el trabajo con honestidad vale más que una nota alta obtenida con trampa.",
    ],
    [("copia", "usar el trabajo de otro como si fuera propio"), ("plagio", "presentar como propias las palabras o ideas de otro sin decir su fuente"), ("parafrasear", "explicar una idea con mis propias palabras"), ("citar", "copiar una frase exacta entre comillas e indicar la fuente"), ("fuente", "lugar o persona de donde viene la información")],
    [
        W("Reconocer un plagio", "Luz copia un párrafo completo de una página web y lo entrega sin decir de dónde lo sacó. ¿Qué es esto?", ["Presenta palabras ajenas como propias.", "No cita la fuente.", "Es plagio."], "Plagio"),
        W("Parafrasear bien", "Texto original: «Las abejas fabrican miel a partir del néctar de las flores». ¿Cuál es una paráfrasis: «Las abejas hacen miel con el néctar que sacan de las flores» o «Las abejas fabrican miel a partir del néctar de las flores»?", ["La segunda es copia exacta.", "La primera expresa la idea con otras palabras.", "Aún así hay que decir la fuente."], "«Las abejas hacen miel con el néctar que sacan de las flores»"),
    ],
    [
        M("Creer que cambiar una o dos palabras ya es mi propio texto.", "Se confunde cambio mínimo con paráfrasis.", "Entiende la idea y escríbela de nuevo con tus palabras, y cita la fuente."),
        M("Pensar que lo que está en internet es de todos y no hace falta citar.", "Se confunde estar disponible con ser propio.", "Anota siempre la fuente."),
    ],
    R=[
        ex("Mirar las respuestas de un compañero en una prueba, ¿es copiar o investigar?", "Copiar", "Usa el trabajo de otro como propio."),
        ex("Presentar como propias las palabras de otro sin decir su fuente, ¿es plagio o parafraseo?", "Plagio", "No reconoce al autor."),
        ex("¿Escribir al final la lista de fuentes ayuda a evitar el plagio? Responde sí o no.", "Sí", "Reconoce de dónde viene la información."),
    ],
    U=[
        ex("¿Por qué copiar no te permite aprender?", "Porque no haces el esfuerzo de entender", "Copiar no desarrolla tu comprensión."),
        ex("¿Qué diferencia hay entre citar y parafrasear?", "Citar copia exacto entre comillas; parafrasear usa mis palabras", "Ambos requieren decir la fuente."),
        ex("Si quiero usar una frase exacta de un libro, ¿qué debo poner: comillas y la fuente o nada?", "Comillas y la fuente", "Así se reconoce al autor."),
    ],
    A=[
        ex("Conductas: 1) escribir con mis palabras y poner la fuente; 2) copiar un párrafo sin decir de dónde; 3) poner comillas a una frase exacta con la fuente; 4) cambiar dos palabras y no citar; 5) mirar la hoja del compañero. ¿Cuántas evitan el plagio y la copia?", "2", "Las conductas 1 y 3 son correctas; las demás no."),
        ex("Original: «Los volcanes expulsan lava y ceniza». ¿Cuál es una buena paráfrasis? A) «Los volcanes expulsan lava y ceniza». B) «Cuando un volcán hace erupción, salen roca derretida y polvo caliente». C) «Los volcanes expulsan lava y cenizas».", "B", "Usa palabras nuevas para la misma idea."),
        ex("Tomás encontró la frase «el agua es esencial para la vida» en el Libro de Ciencias del curso y la quiere usar tal cual. ¿Qué debe hacer? A) Ponerla entre comillas y decir la fuente. B) Copiarla sin avisar. C) Esconder la fuente.", "A", "Es una cita exacta con su fuente."),
    ],
    Z=[
        ex("¿Por qué copiar la tarea de un compañero también daña a quien la hizo?", "Porque usa su esfuerzo sin reconocerlo", "No respeta su trabajo."),
        ex("¿Por qué es mejor una nota más baja con trabajo honesto que una alta con copia?", "Porque la honestidad y el aprendizaje valen más", "La copia no te enseña ni te hace confiable."),
    ],
    D=[
        arith("Para un trabajo, Luz usó 5 fuentes y citó 3 correctamente. ¿Cuántas le faltan por citar?", "5-3", "Se restan las citadas al total de fuentes."),
        arith("Una guía tiene 12 preguntas. Dani respondió 9 con sus palabras. ¿Cuántas le faltan?", "12-9", "Se restan las respondidas al total."),
    ],
    context=[ex("Para un trabajo sobre abejas, Camila lee un libro, anota la idea, la explica con sus palabras y escribe al final: «Fuente: libro de Ciencias de la biblioteca». ¿Evitó el plagio?", "Sí", "Usó sus palabras y citó la fuente.")],
    selfcheck=[ex("En Orientación: ¿parafrasear es usar mis propias palabras y decir la fuente?", "Sí", "Reconoce al autor."), ex("¿Copiar sin citar es plagio?", "Sí", "Presenta lo ajeno como propio."), ex("¿Preguntar cómo citar es mala idea?", "No", "Pedir ayuda es correcto.")],
    task=T("Texto original inventado: «Las plantas necesitan luz, agua y aire para crecer. Con la luz fabrican su alimento». Escribe (1) una paráfrasis con tus palabras, (2) una cita exacta con comillas y la fuente «Texto del cuaderno» y (3) una frase para pedir ayuda si no sabes cómo citar.", "(1) Para crecer, las plantas requieren sol, agua y aire; con el sol elaboran su comida. (2) «Con la luz fabrican su alimento» (Texto del cuaderno). (3) «Profesora, ¿me ayuda a citar bien esta fuente?»", ["parafrasea sin copiar", "cita exacta con comillas y fuente", "pide ayuda de forma respetuosa", "no cuenta una vivencia propia"], ["texto escrito"], ["cambiar solo una palabra", "no poner fuente"], "Reconoce la diferencia entre citar y parafrasear."),
    reinforce="Parafrasea tres frases cortas de un libro y escribe la fuente.",
    extend="Explica por qué dar crédito a un autor es una forma de respeto.",
)

lesson(
    OA9, 5,
    "Una hoja y un lápiz. Las preguntas, los intereses y las actividades están escritos en los ejercicios. Trabajas con personajes inventados.",
    "Aprenderé a preguntar, buscar información sobre mis intereses y desarrollar actividades propias con perseverancia. Sirve para aprender con curiosidad y continuar aunque cueste.",
    ["Sé evitar el plagio.", "Sé establecer metas y organizar mi tiempo."],
    [
        "Los intereses son los temas o actividades que te gustan y te hacen querer saber más. Desarrollarlos mejora tu aprendizaje porque cuando algo te interesa, te esfuerzas más. Para avanzar, empieza con una pregunta concreta, por ejemplo: «¿cómo vuelan los aviones?». Una buena pregunta es clara y se puede investigar. «¿Todo sobre los aviones?» es demasiado amplia.",
        "Luego busca información en varias fuentes confiables: libros de la biblioteca, páginas de instituciones y personas que sepan del tema, como un profesor o un familiar. Compara lo que dicen. Anota lo que aprendes con tus palabras y la fuente. Después puedes desarrollar una actividad con lo aprendido: hacer un cartel, una maqueta, una exposición, un cuadro de datos o enseñar a un compañero.",
        "Perseverar es seguir intentándolo cuando algo cuesta. Si no encuentras la respuesta, cambia la pregunta, prueba otra fuente o pide ayuda. Equivocarte no significa fracasar; significa que estás aprendiendo. Tomar nota de lo que aprendiste y de lo que sigue pendiente te ayuda a continuar.",
    ],
    [("interés", "tema o actividad que me gusta y quiero conocer más"), ("pregunta de investigación", "pregunta clara que se puede responder buscando información"), ("perseverancia", "seguir intentándolo cuando algo cuesta"), ("fuente confiable", "fuente con autor identificable y datos correctos"), ("actividad propia", "trabajo que desarrollo a partir de mis intereses")],
    [
        W("Mejorar una pregunta", "Ian quiere aprender sobre aviones y escribe «Todo sobre aviones». ¿Cuál pregunta es mejor: «¿Cómo logran volar los aviones?» o «Todo sobre aviones»?", ["La primera es concreta.", "La segunda es muy amplia.", "Una buena pregunta se puede investigar."], "«¿Cómo logran volar los aviones?»"),
        W("Elegir una actividad propia", "Después de investigar cómo vuelan los aviones, Ian quiere compartir lo que aprendió. ¿Qué actividad usa su interés: hacer una maqueta con explicación o copiar un texto?", ["La maqueta usa lo aprendido.", "Copiar no desarrolla el interés.", "La maqueta es una actividad propia."], "Hacer una maqueta con explicación"),
    ],
    [
        M("Pensar que los intereses son una pérdida de tiempo si no son de la escuela.", "Se cree que solo cuenta lo que se evalúa.", "Los intereses desarrollan curiosidad, constancia y habilidades."),
        M("Rendirme cuando la primera búsqueda no responde mi pregunta.", "Se piensa que fallar es el final.", "Cambia la pregunta, prueba otra fuente o pide ayuda."),
    ],
    R=[
        ex("Seguir intentándolo cuando algo cuesta, ¿es perseverancia o rendirse?", "Perseverancia", "Es no abandonar al primer obstáculo."),
        ex("¿Una buena pregunta de investigación es clara y se puede responder? Responde sí o no.", "Sí", "Permite buscar información."),
        ex("¿Se debe anotar la fuente de lo que se aprende? Responde sí o no.", "Sí", "Ayuda a no plagiar y a volver a consultar."),
    ],
    U=[
        ex("¿Por qué conviene buscar información en varias fuentes?", "Para comparar y verificar", "Si coinciden, es más confiable."),
        ex("¿Por qué «todo sobre los volcanes» es una pregunta demasiado amplia?", "Porque no se puede responder en un trabajo", "Es mejor una pregunta más concreta."),
        ex("¿Equivocarse significa fracasar? Responde sí o no.", "No", "Equivocarse es parte de aprender."),
    ],
    A=[
        ex("Preguntas: 1) «Todo sobre los animales»; 2) «¿Por qué algunas aves migran en invierno?»; 3) «¿Cuántos tipos de nubes hay y cómo se forman?»; 4) «Cosas interesantes». ¿Cuántas son buenas preguntas de investigación?", "2", "Las preguntas 2 y 3 son concretas y se pueden investigar."),
        ex("Sofi quiere aprender sobre cómo se forman las olas. ¿Qué fuente es más adecuada? A) Un libro de ciencias de la biblioteca. B) Un compañero que dice saber todo. C) Un video anónimo que promete 'secretos'.", "A", "Es una fuente identificable y confiable."),
        ex("Dani se interesa por dibujar mapas. ¿Cuál es una actividad propia? A) Dibujar el mapa de su barrio con sus lugares favoritos. B) Copiar un mapa de internet. C) No hacer nada.", "A", "Usa su interés y desarrolla una habilidad."),
    ],
    Z=[
        ex("¿Por qué anotar con tus palabras lo que aprendes ayuda a recordar?", "Porque entiendes y reformulas la idea", "Escribir con palabras propias fortalece la comprensión."),
        ex("Si no encuentras la respuesta en una fuente, ¿qué conviene hacer?", "Probar otra fuente o cambiar la pregunta", "Insistir con otras opciones es perseverar."),
    ],
    D=[
        arith("Ian consultó 3 libros y 2 páginas de instituciones. ¿Cuántas fuentes usó?", "3+2", "Se suman libros y páginas."),
        arith("Dedicó 20 minutos por día a su proyecto durante 6 días. ¿Cuántos minutos dedicó en total?", "20*6", "Se multiplican los minutos por los días."),
    ],
    context=[ex("A Matilde le interesan los insectos. Escribe la pregunta «¿cómo caminan las hormigas en fila?», busca en un libro de la biblioteca, anota con sus palabras y dibuja un cartel. Al principio no entendía, pero preguntó a su profesora y siguió. ¿Mostró perseverancia?", "Sí", "No se rindió ante la dificultad y pidió ayuda.")],
    selfcheck=[ex("En Orientación: ¿mis intereses pueden ayudarme a aprender?", "Sí", "Motivan a esforzarme."), ex("¿Una buena pregunta de investigación es clara?", "Sí", "Se puede responder."), ex("¿Perseverar es seguir intentando cuando cuesta?", "Sí", "No me rindo al primer obstáculo.")],
    task=T("Escribe un mini proyecto de interés para un personaje inventado, Rocío, a quien le gustan los planetas. Incluye: una pregunta de investigación concreta, dos fuentes confiables posibles, tres pasos para investigar y una actividad propia para mostrar lo aprendido.", "Pregunta: ¿por qué el planeta Marte se ve rojizo? Fuentes: un libro de astronomía de la biblioteca y la página de una institución científica. Pasos: leer, anotar con sus palabras, comparar fuentes. Actividad: hacer un cartel con un dibujo de Marte y una explicación.", ["pregunta concreta", "dos fuentes confiables", "tres pasos", "una actividad propia", "no cuenta una vivencia propia"], ["proyecto escrito"], ["pregunta demasiado amplia", "no incluir fuentes"], "Reconoce el proyecto y pregunta qué haría si no encuentra la respuesta."),
    reinforce="Convierte tres temas amplios en preguntas concretas que se puedan investigar.",
    extend="Explica cómo un interés personal puede ayudarte también a aprender en otras asignaturas.",
)

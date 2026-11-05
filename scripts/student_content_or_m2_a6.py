"""Cuaderno del estudiante, 2.º medio Orientación: OA 08 (iniciativas democráticas de justicia y buen trato) y OA 09 (opciones académicas y laborales)."""
from __future__ import annotations

from or_m2_common import M, T, W, lesson
from student_lessons import arith, ex

OA8, OA9 = "OR2M OA 08", "OR2M OA 09"

# ================================================================ OA 08
lesson(
    OA8, 1,
    "Una hoja y un lápiz. El caso del curso 2.º C, un curso inventado, está escrito en la clase y en los ejercicios.",
    "Aprenderé a examinar una iniciativa ficticia de buen trato en un curso, reconociendo qué instancia colectiva la impulsa y cómo se participa de forma democrática. Sirve para entender cómo nace una iniciativa.",
    ["Sé qué es una instancia de participación (OA 7).", "Sé que todos tienen derecho a opinar."],
    [
        "Una iniciativa es una idea que un grupo pone en marcha para mejorar algo. Una iniciativa de buen trato busca que las personas se traten con respeto y que el curso tenga relaciones pacíficas. Se orienta al bien común, que es lo que beneficia a todos y no solo a algunos. Se desarrolla de manera colaborativa, es decir, entre varios, y democrática, es decir, con participación e igualdad de voz.",
        "Las iniciativas se impulsan en instancias colectivas, como el Consejo de Curso, el Centro de Estudiantes u otros órganos de representación. En ellas se usa el diálogo, que es conversar para entenderse, y el debate respetuoso, que es defender una opinión con argumentos escuchando las de otras personas. La diversidad de opiniones no es un problema: es parte de la democracia.",
        "Para examinar un caso se anotan la idea, quién la propone, qué instancia la discute, quiénes participan y qué principio la sostiene, como el respeto o la justicia. Si en el caso aparece violencia, además se avisa a una persona adulta de confianza, porque una iniciativa no reemplaza esa ayuda.",
    ],
    [("iniciativa", "idea que un grupo pone en marcha para mejorar algo"), ("bien común", "lo que beneficia a todos y no solo a algunos"), ("colaborativo", "que se hace entre varias personas"), ("debate respetuoso", "defender una opinión con argumentos escuchando las de otros"), ("relaciones pacíficas", "formas de convivir sin violencia")],
    [
        W("Reconocer la iniciativa", "En el curso 2.º C, una estudiante propone «un día al mes para reconocer una conducta de buen trato». ¿Es una iniciativa de buen trato?", ["Es una idea para mejorar la convivencia.", "Busca reconocer el respeto."], "Sí"),
        W("Elegir la instancia", "La propuesta afecta solo a 2.º C. ¿Qué instancia la discute primero?", ["Es un asunto del curso.", "El Consejo de Curso es su espacio."], "El Consejo de Curso"),
    ],
    [
        M("Pensar que democracia es que gane la mayoría sin escuchar a nadie.", "Se reduce a votar.", "La democracia incluye escuchar, debatir con respeto y cuidar los derechos de todos."),
        M("Creer que una iniciativa de buen trato reemplaza avisar a un adulto ante violencia.", "Se piensa que el curso lo resuelve todo.", "Ante violencia, avisa a una persona adulta de confianza."),
    ],
    R=[
        ex("Lo que beneficia a todos y no solo a algunos es A) el bien común B) un privilegio", "A", "Esa es la definición."),
        ex("El Consejo de Curso, ¿es una instancia colectiva? Responde sí o no.", "Sí", "Reúne al curso para decidir."),
        ex("Defender una opinión con argumentos escuchando las de otros es A) debate respetuoso B) pelea", "A", "El respeto es parte del debate."),
    ],
    U=[
        ex("¿Qué significa que una iniciativa sea democrática? A) Que todos participan con igualdad de voz B) Que decide una sola persona", "A", "La voz de cada persona cuenta."),
        ex("La diversidad de opiniones en el curso es A) parte de la democracia B) un problema que se evita", "A", "Escuchar diferencias enriquece las decisiones."),
        ex("Si hay violencia en el curso, ¿qué se hace además de la iniciativa? A) Avisar a una persona adulta B) Esperar la próxima reunión", "A", "La seguridad no espera."),
    ],
    A=[
        ex("Clasifica con B (buen trato) o N (no): 1) Reconocer a quien ayuda a un compañero. 2) Apodos burlescos en un chat. 3) Turnos para hablar en el consejo. Escribe las letras en orden.", "B, N, B", "La 2 daña la dignidad; las otras cuidan la convivencia."),
        ex("En el curso 2.º C, 36 estudiantes votan una iniciativa: 24 a favor. ¿Cuántos no votaron a favor?", "12", "A los 36 se les restan los 24 a favor."),
        ex("¿Qué instancia debería recibir una iniciativa que afecta a todo el liceo? A) El Centro de Estudiantes B) Un grupo de amigos", "A", "Representa al estudiantado."),
    ],
    Z=[
        ex("¿Por qué una iniciativa de buen trato debe mirar el bien común?", "Porque busca que todas las personas del curso se beneficien y no solo un grupo", "El bien común es de todos."),
        ex("Un compañero dice: «Si la mayoría quiere, da lo mismo lo que sienta la minoría». ¿Qué respondes? A) Los derechos de todos se respetan siempre B) Tienes razón", "A", "La mayoría no puede vulnerar derechos."),
    ],
    D=[
        arith("En una asamblea de ejemplo participan 9 equipos de 4 estudiantes. ¿Cuántos estudiantes participan?", "9*4", "Se multiplican equipos por integrantes."),
        arith("El Consejo de Curso recibe 3 ideas de cada una de 4 comisiones. ¿Cuántas ideas debe discutir?", "3*4", "Se multiplican las ideas por las comisiones."),
    ],
    context=[ex("En una reunión inventada, un estudiante propone «un mural sobre el respeto». Otro dice «mejor un campeonato». ¿Qué conviene hacer? A) Escuchar ambas y decidir con reglas conocidas B) Imponer una", "A", "Respeta la participación democrática.")],
    selfcheck=[ex("En Orientación: ¿el bien común beneficia a todos?", "Sí", "No favorece solo a algunos."), ex("¿La diversidad de opiniones es parte de la democracia?", "Sí", "Enriquece las decisiones."), ex("¿Una iniciativa reemplaza avisar a un adulto ante violencia?", "No", "Son acciones complementarias.")],
    task=T("Lee el caso inventado: En 2.º C, varias personas se burlan de quien se equivoca al leer. Tres estudiantes proponen una iniciativa para el Consejo de Curso. Escribe: (1) un nombre para la iniciativa, (2) qué instancia la discutiría, (3) un principio que la sostiene y (4) qué haría el curso si además hay un caso de violencia física.", "Nombre: «Aquí nos escuchamos». Instancia: Consejo de Curso. Principio: respeto. Violencia física: avisar a la persona adulta, como el profesor jefe.", ["escribe un nombre", "nombra la instancia", "nombra un principio", "indica avisar a una persona adulta"], ["texto escrito", "tabla"], ["no mencionar a un adulto", "proponer castigos"], "Reconoce el nombre y pregunta qué acción concreta incluiría."),
    reinforce="Escribe una iniciativa de buen trato inventada para un recreo.",
    extend="Explica la diferencia entre un diálogo y una imposición.",
)

lesson(
    OA8, 2,
    "Una hoja y un lápiz. Las frases de ejemplo y las reglas están escritas en los ejercicios.",
    "Aprenderé a distinguir argumento, opinión y ataque personal, y a reconocer los derechos y límites de un debate democrático. Sirve para discutir ideas sin dañar a las personas.",
    ["Sé qué es una iniciativa de buen trato.", "Sé distinguir hecho y opinión."],
    [
        "Un argumento es una razón que respalda una opinión. «Propongo turnos para hablar porque así todos opinan» tiene opinión y razón. Un ataque personal, en cambio, critica a la persona y no a su idea, como «no tiene idea de nada». Los ataques personales rompen el diálogo y vulneran la dignidad, por eso no son válidos en un debate.",
        "Un debate respetuoso tiene reglas conocidas: pedir la palabra, respetar los turnos, no interrumpir, escuchar hasta el final y responder a la idea y no a la persona. También permite decir «no estoy de acuerdo» sin gritar. La mayoría decide en una votación, pero no puede quitar derechos como la dignidad, la seguridad o la no discriminación.",
        "Un derecho importante de las minorías es ser escuchadas. Una persona puede quedar en minoría y seguir siendo respetada. Y si alguien rompe una regla del debate, se le recuerda con calma. Si hay insultos o amenazas, se detiene la reunión y se avisa a una persona adulta que acompañe.",
    ],
    [("argumento", "razón que respalda una opinión"), ("ataque personal", "crítica a la persona y no a su idea"), ("turno", "momento asignado para hablar"), ("minoría", "grupo con menos votos en una decisión"), ("moderar", "guiar un debate para que se respeten las reglas")],
    [
        W("Argumento o ataque", "«Esa propuesta no sirve porque la hizo alguien que nunca viene». ¿Es un argumento o un ataque personal?", ["Critica a la persona, no a la idea.", "No explica por qué la propuesta falla."], "Un ataque personal"),
        W("Respetar a la minoría", "En una votación, 10 estudiantes de 30 quedaron en minoría. ¿Pueden ser ignorados?", ["Tienen derecho a ser escuchados.", "La mayoría no anula sus derechos."], "No, deben ser escuchados y respetados"),
    ],
    [
        M("Pensar que ganar la votación permite ignorar a quien perdió.", "Se confunde mayoría con todos los derechos.", "La minoría conserva el derecho a opinar y a ser respetada."),
        M("Contestar a la persona en vez de a su idea.", "Se piensa que desacreditar a alguien gana el debate.", "Responde a la razón que dio."),
    ],
    R=[
        ex("Una razón que respalda una opinión es A) un argumento B) un ataque personal", "A", "El argumento da motivos."),
        ex("«No tiene idea de nada» es A) un ataque personal B) un argumento", "A", "Critica a la persona."),
        ex("Pedir la palabra y esperar el turno, ¿es una regla del debate? Responde sí o no.", "Sí", "Permite que todos hablen."),
    ],
    U=[
        ex("¿Qué derecho tiene la minoría en una votación? A) Ser escuchada y respetada B) Que se cumpla su propuesta", "A", "No siempre gana, pero tiene derecho a opinar."),
        ex("¿Por qué no se vota para quitar un derecho? A) Porque los derechos no dependen de la mayoría B) Porque se demora", "A", "Son límites que protegen a todos."),
        ex("Si en una reunión hay insultos, ¿qué se hace? A) Detenerla y pedir apoyo adulto B) Seguir igual", "A", "Se cuida el diálogo."),
    ],
    A=[
        ex("Clasifica con A (argumento) o P (ataque personal): 1) «Propongo turnos para que todos hablen.» 2) «Siempre dices tonteras.» 3) «No me convence porque no cubre a los de otros cursos.» Escribe las letras en orden.", "A, P, A", "La 2 critica a la persona."),
        ex("En una votación de 30 estudiantes, 18 votan por la propuesta A y 12 por la B. ¿Cuántos votos de diferencia hay?", "6", "18 menos 12 son 6."),
        ex("Un debate de 3 equipos con 2 minutos cada uno por ronda y 3 rondas dura A) 18 minutos B) 8 minutos", "A", "3 equipos por 2 minutos son 6 minutos y 3 rondas son 18."),
    ],
    Z=[
        ex("¿Por qué responder a la idea y no a la persona mejora el debate?", "Porque mantiene el respeto y permite evaluar las razones", "Se discute con argumentos."),
        ex("Un compañero dice: «Como somos mayoría, no tenemos que escuchar». ¿Qué respondes? A) Escuchar es parte de la democracia B) Tienes razón", "A", "El respeto incluye a las minorías."),
    ],
    D=[
        arith("Una moderadora da 2 minutos de turno a cada uno de 8 estudiantes. ¿Cuántos minutos dura la ronda?", "2*8", "Se multiplican los minutos por los estudiantes."),
        arith("De 28 estudiantes, 17 votaron a favor de una propuesta. ¿Cuántos no votaron a favor?", "28-17", "Al total se le restan los votos a favor."),
    ],
    context=[ex("En un Consejo de Curso inventado, un estudiante responde «tu idea es mala porque eres nuevo». ¿Qué corrección hace la moderadora? A) Pide que responda a la idea y no a la persona B) Pide que se quede callado", "A", "Se cuida el respeto en el debate.")],
    selfcheck=[ex("En Orientación: ¿un argumento da una razón?", "Sí", "Respalda la opinión."), ex("¿Se puede votar para quitar un derecho?", "No", "Los derechos no dependen de la mayoría."), ex("¿La minoría tiene derecho a ser escuchada?", "Sí", "Es parte de la democracia.")],
    task=T("Lee las frases inventadas de un debate: (a) «Propongo un recreo de juegos porque ayuda a convivir»; (b) «Eres flojo y no puedes opinar»; (c) «No estoy de acuerdo porque no hay espacio»; (d) «Ganamos la votación, no hay que escuchar a nadie». Clasifica cada una como argumento, ataque personal o error de democracia y reescribe (b) y (d) con respeto.", "(a) Argumento. (b) Ataque personal: «No estoy de acuerdo con tu propuesta porque…». (c) Argumento. (d) Error: «Ganó la propuesta; escuchemos igual las ideas de quienes votaron distinto».", ["clasifica las cuatro frases", "reescribe (b)", "reescribe (d)", "usa argumentos"], ["tabla escrita", "texto breve"], ["responder a la persona", "ignorar a la minoría"], "Reconoce las reescrituras y pregunta qué regla del debate aplicó."),
    reinforce="Reescribe sin ataque personal la frase inventada «Eres un pesado, siempre opinas lo mismo».",
    extend="Explica por qué un derecho no se decide por votación.",
)

lesson(
    OA8, 3,
    "Una hoja y un lápiz. Las formas de decidir y los datos del curso inventado están escritos en los ejercicios.",
    "Aprenderé a comparar formas de decidir una iniciativa, como votación por mayoría, consenso y decisión de una sola persona, con criterios de participación, rapidez y aceptación. Sirve para elegir cómo decidir.",
    ["Sé distinguir argumento y ataque personal.", "Sé qué hace una instancia colectiva."],
    [
        "Hay varias formas de decidir en grupo. Con la votación por mayoría gana la opción con más votos. Con el consenso se busca una opción que todos puedan aceptar, aunque no sea la favorita de cada persona. Con la decisión de una sola persona, alguien decide por todos, lo que no es democrático en una iniciativa del curso.",
        "Para comparar, se usan tres preguntas: ¿todos participan?, ¿es rápida? y ¿la mayoría de las personas la acepta? Cada sí vale 1 punto. La votación suele ser rápida y participativa. El consenso es más lento pero logra más aceptación. Decidir por una sola persona rara vez suma puntos de participación.",
        "Ninguna forma sirve siempre. Para elegir un nombre de una campaña puede bastar votar. Para un acuerdo de convivencia que afecta a todos, conviene buscar consenso. Y si una votación deja a muchos descontentos, se pueden revisar las ideas y buscar un ajuste.",
    ],
    [("votación por mayoría", "gana la opción con más votos"), ("consenso", "acuerdo que todos pueden aceptar"), ("participación", "que todas las personas opinen o voten"), ("aceptación", "que las personas estén de acuerdo con la decisión"), ("ajuste", "cambio pequeño para mejorar una propuesta")],
    [
        W("Elegir la forma", "El curso inventado debe elegir un nombre para una campaña. Hay 3 opciones y 30 estudiantes. ¿Qué forma es más práctica?", ["Es una decisión simple.", "La votación es rápida y participativa."], "La votación por mayoría"),
        W("Puntuar", "Consenso: todos participan sí, rápida no, la mayoría acepta sí. ¿Cuántos puntos suma?", ["Hay dos síes.", "Un no."], "2 puntos"),
    ],
    [
        M("Creer que la votación siempre es la mejor forma.", "Se olvida que puede dejar descontentos a muchos.", "Para temas que afectan a todos, busca consenso."),
        M("Pensar que el consenso exige que todos opinen igual.", "Se confunde consenso con unanimidad de opinión.", "El consenso es una opción que todos pueden aceptar."),
    ],
    R=[
        ex("Una opción que todos pueden aceptar se logra con A) consenso B) decisión de una persona", "A", "Busca aceptación general."),
        ex("En la votación por mayoría gana la opción con A) más votos B) menos votos", "A", "Esa es la regla."),
        ex("¿Decidir una sola persona por todo el curso es democrático? Responde sí o no.", "No", "Se pierde la participación."),
    ],
    U=[
        ex("¿Qué ventaja tiene el consenso? A) Mayor aceptación B) Mayor rapidez siempre", "A", "Todos pueden aceptar la decisión."),
        ex("¿Qué ventaja tiene la votación? A) Es rápida y participativa B) Evita que alguien opine", "A", "Se decide con pocos pasos."),
        ex("Una votación deja a 14 de 30 descontentos. ¿Qué conviene? A) Revisar ideas y buscar un ajuste B) Ignorarlos", "A", "Se recupera la aceptación."),
    ],
    A=[
        ex("Votación: participación sí, rápida sí, aceptación no. Consenso: sí, no, sí. Decisión de una persona: no, sí, no. Cada sí vale 1. ¿Qué forma suma menos?", "La decisión de una persona", "Suma 1, mientras las otras suman 2."),
        ex("Un acuerdo de convivencia afecta a todos. ¿Qué forma conviene más? A) Consenso B) Decidir una sola persona", "A", "Logra aceptación de todos."),
        ex("En un curso de 32 estudiantes hay 3 propuestas y todos votan una vez. Si A tiene 15 y B tiene 10, ¿cuántos votos tiene C?", "7", "32 menos 15 y 10 son 7."),
    ],
    Z=[
        ex("¿Por qué ninguna forma de decidir sirve para todas las situaciones?", "Porque cada tema necesita distinto equilibrio entre rapidez, participación y aceptación", "Se elige según el caso."),
        ex("Un compañero dice: «Con votar basta siempre». ¿Qué respondes? A) En temas que afectan a todos conviene buscar consenso B) Tienes razón", "A", "El consenso cuida la aceptación."),
    ],
    D=[
        arith("En una votación de ejemplo participan 5 cursos de 30 estudiantes. ¿Cuántos votos posibles hay?", "5*30", "Se multiplican cursos por estudiantes."),
        arith("De 150 votos posibles, se emiten 120. ¿Cuántos estudiantes no votaron?", "150-120", "Al total posible se le restan los votos emitidos."),
    ],
    context=[ex("El Centro de Estudiantes debe elegir la fecha del día del buen trato entre dos opciones. ¿Qué forma es práctica? A) Votación B) Que lo decida el presidente sin consultar", "A", "Es rápida y participativa.")],
    selfcheck=[ex("En Orientación: ¿el consenso busca una opción aceptable para todos?", "Sí", "Prioriza la aceptación."), ex("¿La votación es siempre la mejor?", "No", "Puede dejar descontentos."), ex("¿Se puede ajustar una propuesta tras una votación?", "Sí", "Mejora la aceptación.")],
    task=T("Compara las tres formas de decidir (votación, consenso y decisión de una persona) para este caso inventado: el curso 2.º D debe acordar normas de uso del celular en clases. Usa las tres preguntas (participación, rapidez y aceptación), suma puntos y elige. Escribe además un posible ajuste si queda un grupo descontento.", "Votación: 1+1+0=2. Consenso: 1+0+1=2. Una persona: 0+1+0=1. Se elige consenso porque afecta a todos. Ajuste: permitir el celular en recreos y limitarlo en clases.", ["responde las tres preguntas por forma", "suma bien", "elige y justifica", "propone un ajuste"], ["tabla escrita", "texto breve"], ["sumar mal", "decidir sin justificar"], "Reconoce el uso de criterios y pregunta cómo revisarían la norma."),
    reinforce="Elige una forma de decidir para un paseo inventado y justifica en una frase.",
    extend="Explica por qué el consenso puede ser más lento pero más duradero.",
)

lesson(
    OA8, 4,
    "Una hoja y un lápiz. Los pasos y los casos de ejemplo están escritos en los ejercicios.",
    "Aprenderé a planificar una iniciativa de manera segura y democrática, con pasos, responsables y fechas, y a reconocer cuándo debe sumarse una persona adulta. Sirve para llevar una idea a la acción sin riesgos.",
    ["Sé comparar formas de decidir.", "Sé que las iniciativas no reemplazan al adulto ante violencia."],
    [
        "Una iniciativa se planifica en pasos: diagnosticar el problema, definir un objetivo, decidir las acciones, repartir responsables, fijar fechas y evaluar al final. Un objetivo claro dice qué se quiere lograr, como «reducir los apodos burlescos en el curso en un mes». Cada acción tiene un responsable y una fecha.",
        "Una iniciativa segura cumple tres condiciones: no expone a nadie, respeta los derechos de todos y cuenta con apoyo adulto cuando corresponde. Por ejemplo, una campaña no debe señalar a personas, y una actividad con otros cursos requiere avisar a la dirección. Si surge un caso de violencia mientras se desarrolla, se detiene y se avisa a una persona adulta.",
        "Evaluar es comprobar si se logró el objetivo, con un dato simple, como contar cuántos apodos se registraron antes y después. Lo evaluado sirve para ajustar. Si no resultó, no es un fracaso: es información para mejorar la próxima vez.",
    ],
    [("objetivo", "lo que se quiere lograr con una iniciativa"), ("responsable", "persona que se compromete a hacer una tarea"), ("diagnóstico", "descripción del problema antes de actuar"), ("evaluar", "comprobar si se logró lo propuesto"), ("registro", "anotación ordenada de datos")],
    [
        W("Escribir un objetivo", "Un curso quiere mejorar el trato. ¿Qué objetivo es claro: «ser mejores» o «reducir los apodos burlescos en un mes»?", ["Un objetivo claro se puede medir.", "El primero es vago."], "Reducir los apodos burlescos en un mes"),
        W("Repartir tareas", "La iniciativa tiene 4 acciones y 4 responsables. ¿Cuántas personas se necesitan como mínimo si cada responsable hace una acción?", ["Cada responsable asume una acción.", "Son 4 acciones."], "4 personas"),
    ],
    [
        M("Hacer una campaña señalando a quienes se portan mal.", "Se piensa que exponer cambia conductas.", "Promueve conductas positivas sin señalar a nadie."),
        M("Planificar sin fechas ni responsables.", "Se cree que la idea basta.", "Cada acción necesita una persona y una fecha."),
    ],
    R=[
        ex("Lo que se quiere lograr con una iniciativa es A) el objetivo B) la evaluación", "A", "Es la meta."),
        ex("Una acción necesita un responsable y una fecha. Responde sí o no.", "Sí", "Así se puede cumplir."),
        ex("Una campaña que señala a personas, ¿es segura? Responde sí o no.", "No", "Expone a las personas."),
    ],
    U=[
        ex("¿Para qué sirve evaluar al final? A) Para ver si se logró el objetivo y ajustar B) Para culpar", "A", "La evaluación mejora la próxima vez."),
        ex("¿Qué debe hacerse si surge un caso de violencia durante la iniciativa? A) Detenerse y avisar a una persona adulta B) Seguir como si nada", "A", "Se protege a las personas."),
        ex("Una actividad con otros cursos necesita A) avisar a la dirección B) mantenerse en secreto", "A", "Requiere apoyo adulto."),
    ],
    A=[
        ex("Ordena con letras los pasos de planificación: (a) fijar fechas, (b) diagnosticar, (c) evaluar. ¿Cuál va primero?", "b", "Primero se describe el problema."),
        ex("Clasifica con O (objetivo claro) o V (vago): 1) «Mejorar el curso.» 2) «Bajar de 10 a 5 los apodos en un mes.» 3) «Hacer cosas lindas.» Escribe las letras en orden.", "V, O, V", "Solo la 2 se puede medir."),
        ex("Un curso registró 12 apodos burlescos en septiembre y 7 en octubre. ¿Cuántos menos hubo?", "5", "12 menos 7 son 5."),
    ],
    Z=[
        ex("¿Por qué evaluar con un dato simple ayuda más que opinar «creo que mejoró»?", "Porque el dato permite comprobar el cambio y no depender de impresiones", "Un número permite comparar."),
        ex("Un compañero dice: «Si no se logró, fue un fracaso». ¿Qué respondes? A) Es información para ajustar B) Tienes razón", "A", "Aprender de un resultado es parte del proceso."),
    ],
    D=[
        arith("Una iniciativa tiene 5 acciones y cada una se revisa 3 veces. ¿Cuántas revisiones hay?", "5*3", "Se multiplican acciones por revisiones."),
        arith("Un curso se propone bajar de 20 a 8 los incidentes de burla en un mes. ¿Cuántos incidentes menos busca?", "20-8", "Se resta la meta del punto de partida."),
    ],
    context=[ex("Un grupo inventado quiere organizar un mural de buen trato. ¿Qué debe hacer antes de pintar? A) Avisar y pedir autorización a la dirección B) Pintar de noche", "A", "Las actividades en el liceo requieren apoyo adulto.")],
    selfcheck=[ex("En Orientación: ¿una iniciativa necesita responsables y fechas?", "Sí", "Se organiza para cumplirse."), ex("¿Evaluar sirve para ajustar?", "Sí", "Mejora la iniciativa."), ex("¿Una campaña puede señalar a personas?", "No", "Expondría a alguien.")],
    task=T("Planifica una iniciativa inventada de buen trato para un curso: escribe (1) un objetivo medible, (2) cuatro acciones con responsable y fecha, (3) una condición de seguridad (qué no se hará) y (4) cómo evaluarán con un dato simple. Indica a qué persona adulta pedirán apoyo.", "Objetivo: bajar de 10 a 5 apodos burlescos en un mes. Acciones: mural (Ana, semana 1), reglas del chat (Luis, semana 1), reconocimiento mensual (equipo B, semana 3), conteo de apodos (equipo C, semana 4). Seguridad: no señalar a personas. Evaluación: contar apodos antes y después. Apoyo: profesor jefe.", ["objetivo medible", "cuatro acciones con responsable y fecha", "condición de seguridad", "evaluación y persona adulta"], ["plan escrito", "tabla"], ["objetivo vago", "olvidar al adulto"], "Reconoce el plan claro y pregunta cómo ajustaría si el dato no mejora."),
    reinforce="Escribe un objetivo medible para una iniciativa inventada sobre puntualidad.",
    extend="Explica por qué una iniciativa segura no debe señalar a personas.",
)

lesson(
    OA8, 5,
    "Una hoja y un lápiz. El debate de ejemplo y las frases para participar están escritos en los ejercicios.",
    "Aprenderé a participar en un debate respetuoso con una estructura simple: opinión, razón, pregunta y reformulación, y a pedir apoyo cuando el debate se vuelve violento. Sirve para hablar y escuchar mejor.",
    ["Sé distinguir argumento y ataque.", "Sé cómo se decide en grupo."],
    [
        "Un debate respetuoso puede seguir cuatro movimientos. Dar tu opinión con una razón, por ejemplo: «Creo que conviene un mural porque se ve todos los días». Hacer una pregunta para entender a la otra persona: «¿Qué te preocupa del mural?». Reformular, que es repetir con tus palabras lo que entendiste que dijo la otra persona. Y proponer un ajuste que considere ambas ideas.",
        "Reformular ayuda a evitar malentendidos y muestra respeto: «Entiendo que te preocupa el costo». Escuchar activamente es mirar, no interrumpir y recordar lo que dijo la otra persona. También hay que cuidar el tono de voz y los gestos, que comunican tanto como las palabras.",
        "Si el debate se vuelve violento, con gritos, insultos o amenazas, se pide una pausa, se avisa a una persona adulta y se retoma cuando todos estén calmos. Pedir ayuda no es perder el debate: es proteger a las personas. El Fono Niños 147 puede orientar a adolescentes, junto con el aviso a una persona adulta.",
    ],
    [("reformular", "repetir con tus palabras lo que entendiste de otro"), ("escuchar activamente", "atender sin interrumpir y recordar lo dicho"), ("tono", "forma de la voz al hablar"), ("pausa", "momento de detenerse para calmarse"), ("ajuste", "cambio que considera varias ideas")],
    [
        W("Reformular", "Un compañero dice: «El mural es caro y no hay presupuesto». ¿Cuál es una buena reformulación?", ["Repite con tus palabras lo que entendiste.", "No responde con una crítica."], "«Entiendo que te preocupa el costo del mural»"),
        W("Pedir pausa", "En el debate, dos estudiantes empiezan a gritar. ¿Qué conviene hacer?", ["Los gritos impiden dialogar.", "Una pausa permite calmarse."], "Pedir una pausa y avisar a una persona adulta"),
    ],
    [
        M("Preparar la respuesta mientras el otro habla, sin escuchar.", "Se piensa que defender es más importante que entender.", "Escucha, reformula y luego responde."),
        M("Pensar que pedir una pausa es rendirse.", "Se confunde calma con derrota.", "Una pausa protege el diálogo."),
    ],
    R=[
        ex("Repetir con tus palabras lo que entendiste es A) reformular B) interrumpir", "A", "Esa es la definición."),
        ex("Si el debate se vuelve violento, ¿se pide una pausa? Responde sí o no.", "Sí", "Se protege a las personas."),
        ex("Una pregunta para entender al otro, ¿ayuda al debate? Responde sí o no.", "Sí", "Reduce los malentendidos."),
    ],
    U=[
        ex("¿Qué incluye escuchar activamente? A) No interrumpir y recordar lo dicho B) Preparar solo tu respuesta", "A", "Muestra respeto y atención."),
        ex("¿Por qué el tono de voz importa? A) Comunica tanto como las palabras B) No importa", "A", "Puede sonar a agresión o a respeto."),
        ex("Ante gritos y amenazas, ¿qué corresponde? A) Pausa y aviso a un adulto B) Gritar más fuerte", "A", "Hay un riesgo para las personas."),
    ],
    A=[
        ex("Ordena con letras los movimientos: (a) pregunta, (b) opinión con razón, (c) reformulación. ¿Cuál va primero?", "b", "Primero se expone la opinión con su razón."),
        ex("Clasifica con O (opinión con razón), P (pregunta) o R (reformulación): 1) «Entiendo que te preocupa el costo.» 2) «Creo que conviene porque se ve todos los días.» 3) «¿Qué te preocupa?» Escribe las letras en orden.", "R, O, P", "Cada frase cumple una función distinta."),
        ex("En un debate de ejemplo hay 4 equipos y cada uno habla 3 minutos. ¿Cuánto dura la ronda?", "12", "4 por 3 son 12 minutos."),
    ],
    Z=[
        ex("¿Por qué reformular evita malentendidos?", "Porque comprueba que entendiste y le muestra al otro que lo escuchaste", "Hace visible la comprensión."),
        ex("Un compañero dice: «Pedir pausa es perder». ¿Qué respondes? A) Es proteger el diálogo y a las personas B) Tienes razón", "A", "Calmarse permite seguir."),
    ],
    D=[
        arith("Un grupo ensaya un debate con 6 estudiantes y cada uno habla 2 veces de 90 segundos. ¿Cuántos segundos hablan en total?", "6*2*90", "Se multiplican estudiantes, intervenciones y segundos."),
        arith("En una ronda de 20 minutos, 3 equipos usan 4 minutos cada uno. ¿Cuántos minutos quedan para preguntas?", "20-3*4", "Se restan los 12 minutos de los equipos."),
    ],
    context=[ex("En el Centro de Estudiantes inventado, dos delegados discuten fuerte y uno amenaza al otro. ¿Qué hace una persona presente? A) Pedir una pausa y avisar a una persona adulta B) Grabar y publicar", "A", "Protege y busca ayuda.")],
    selfcheck=[ex("En Orientación: ¿reformular es repetir con tus palabras?", "Sí", "Muestra que escuchaste."), ex("¿Una pausa puede proteger un debate?", "Sí", "Calma las emociones."), ex("¿El tono de voz comunica?", "Sí", "Puede sonar a respeto o a agresión.")],
    task=T("Escribe un mini diálogo de cuatro intervenciones para un debate inventado sobre si el curso debe hacer un mural o un campeonato de buen trato. Debe tener: una opinión con razón, una pregunta, una reformulación y un ajuste. Agrega al final qué harías si el debate se vuelve violento.", "A: «Creo que conviene un mural porque se ve todos los días.» B: «Prefiero un campeonato porque participa más gente. ¿Qué te gusta del mural?» A: «Entiendo que para ti es importante que participe más gente.» B: «Propongo un mural y un mini campeonato en el recreo.» Si hay violencia: pausa y avisar a la profesora jefa.", ["incluye opinión con razón", "incluye pregunta y reformulación", "incluye un ajuste", "indica qué hacer ante violencia"], ["texto escrito", "ensayo oral"], ["responder a la persona", "no incluir a un adulto"], "Reconoce el diálogo claro y pregunta cómo suena el tono al decirlo."),
    reinforce="Escribe una reformulación para la frase inventada «No quiero participar porque nadie me escucha».",
    extend="Explica cómo cambia un debate cuando todos reformulan antes de responder.",
)

# ================================================================ OA 09
lesson(
    OA9, 1,
    "Una hoja y un lápiz. El caso de Sofía, una estudiante inventada, y sus opciones están escritos en la clase y en los ejercicios.",
    "Aprenderé a examinar un caso ficticio con caminos posibles para después de la enseñanza media, y a relacionarlos con habilidades e intereses. Sirve para conocer las opciones antes de elegir.",
    ["Sé comparar alternativas de proyecto de vida (OA 1).", "Sé distinguir interés y capacidad."],
    [
        "Después de la enseñanza media hay varios caminos. Se puede seguir estudios superiores en una universidad, en un instituto profesional (IP) o en un centro de formación técnica (CFT). También se puede trabajar, capacitarse en un oficio o combinar estudio y trabajo. Cada camino pide cosas distintas y abre oportunidades distintas.",
        "En 3.º y 4.º medio, el sistema escolar ofrece distintas formaciones: científico-humanista, técnico-profesional y artística. Elegir una de ellas influye en las opciones posteriores, pero no cierra todas las puertas. Por eso es útil informarse con tiempo en fuentes confiables y con la persona orientadora.",
        "Para examinar un caso se anotan los intereses, las habilidades, las condiciones y los caminos posibles de la persona. Las habilidades son cosas que se saben hacer o aprender, como organizar, calcular, explicar o crear. Los intereses son lo que atrae. Un camino se relaciona mejor con quien lo elige cuando coincide con sus habilidades e intereses y es viable.",
    ],
    [("universidad", "institución de educación superior que otorga grados y títulos profesionales"), ("instituto profesional", "institución de educación superior orientada a carreras profesionales y técnicas"), ("centro de formación técnica", "institución de educación superior que forma técnicos"), ("habilidad", "cosa que una persona sabe hacer o puede aprender"), ("oficio", "trabajo que requiere un conocimiento práctico")],
    [
        W("Relacionar habilidad y camino", "Sofía, personaje inventado, es buena para organizar eventos y le gusta ayudar. ¿Qué camino se relaciona mejor: administración de eventos o minería subterránea?", ["Organiza y ayuda a otros.", "Administración de eventos usa esas habilidades."], "Administración de eventos"),
        W("Tipo de institución", "Un joven quiere formarse como técnico en un área. ¿Qué tipo de institución ofrece esa formación?", ["Un centro de formación técnica forma técnicos.", "También hay institutos profesionales con carreras técnicas."], "Un centro de formación técnica o un instituto profesional"),
    ],
    [
        M("Creer que un solo camino es el correcto para todos.", "Se compara con lo que eligieron otros.", "Cada persona elige según sus habilidades, intereses y condiciones."),
        M("Elegir solo por el prestigio del título.", "Se olvida lo que atrae y lo que se puede hacer.", "Revisa tus habilidades, intereses y las condiciones reales."),
    ],
    R=[
        ex("Una universidad, un IP y un CFT son A) instituciones de educación superior B) tipos de deporte", "A", "Ofrecen estudios después de la media."),
        ex("Trabajar o capacitarse en un oficio, ¿es un camino posible? Responde sí o no.", "Sí", "No todos los caminos pasan por estudios superiores."),
        ex("Algo que una persona sabe hacer o puede aprender es una A) habilidad B) condición", "A", "Esa es la definición."),
    ],
    U=[
        ex("¿Qué formaciones existen en 3.º y 4.º medio? A) Científico-humanista, técnico-profesional y artística B) Solo una", "A", "El sistema ofrece varias formaciones."),
        ex("¿Por qué conviene informarse con tiempo? A) Porque elegir bien requiere comparar con calma B) Porque todo se decide en un día", "A", "La información reduce errores."),
        ex("Sofía disfruta ayudar a otros y explicar. ¿Qué es eso? A) Un interés y una habilidad B) Una condición económica", "A", "Mezcla lo que le atrae y lo que sabe hacer."),
    ],
    A=[
        ex("Clasifica con H (habilidad) o I (interés): 1) Calcular bien. 2) Atraerle la biología. 3) Explicar con claridad. Escribe las letras en orden.", "H, I, H", "La 2 es lo que atrae; las otras son cosas que sabe hacer."),
        ex("Sofía anota 6 carreras y descarta 2 por no coincidir con sus habilidades. ¿Cuántas quedan?", "4", "A las 6 se les restan las 2."),
        ex("Un camino puede ser estudiar y trabajar a la vez. ¿Qué condición exige? A) Organizar bien el tiempo y la energía B) Que ambas actividades cuesten lo mismo", "A", "El tiempo es el recurso clave."),
    ],
    Z=[
        ex("¿Por qué una formación técnico-profesional en 3.º y 4.º medio no cierra todas las puertas?", "Porque después se puede seguir estudiando o trabajar y existen caminos para continuar", "Hay varias salidas."),
        ex("Un compañero dice: «Si no voy a la universidad, no me irá bien». ¿Qué respondes? A) Hay varios caminos válidos según cada persona B) Tienes razón", "A", "No hay un único camino."),
    ],
    D=[
        arith("Sofía visita 2 instituciones por mes durante 3 meses. ¿Cuántas visitas hace en total?", "2*3", "Se multiplican las visitas por los meses."),
        arith("Una feria de ejemplo tiene 8 stands de carreras técnicas y 5 de carreras profesionales. ¿Cuántos stands hay?", "8+5", "Se suman ambos tipos de stands."),
    ],
    context=[ex("En una charla de orientación inventada, un joven dice que no sabe qué hacer después de 4.º medio. ¿Qué paso conviene? A) Conocer opciones y relacionarlas con sus intereses y habilidades B) Esperar que alguien decida", "A", "Informarse es el primer paso.")],
    selfcheck=[ex("En Orientación: ¿hay más de un camino después de la media?", "Sí", "Estudios, trabajo o ambos."), ex("¿Una habilidad es algo que se sabe hacer?", "Sí", "Se puede aprender también."), ex("¿Conviene informarse con tiempo?", "Sí", "Mejora la decisión.")],
    task=T("Lee el caso inventado: Mateo, de 16 años, es bueno para armar y reparar cosas, le atraen los computadores y vive lejos de la ciudad. Sus ahorros son pocos. Escribe: (1) dos habilidades de Mateo, (2) un interés, (3) una condición que influye y (4) dos caminos posibles que podría explorar, con una razón.", "Habilidades: armar y reparar. Interés: computadores. Condición: vive lejos y tiene pocos ahorros. Caminos: técnico en informática en un CFT (coincide con su interés) o capacitarse en reparación de equipos mientras trabaja.", ["dos habilidades", "un interés", "una condición", "dos caminos con razón"], ["texto escrito", "tabla"], ["ignorar las condiciones", "elegir sin razón"], "Reconoce la relación entre habilidades e intereses y pregunta qué dato falta."),
    reinforce="Anota tres habilidades de un personaje inventado y una carrera que las use.",
    extend="Explica la diferencia entre un CFT, un IP y una universidad con tus palabras.",
)

lesson(
    OA9, 2,
    "Una hoja y un lápiz. Los datos de ejemplo de requisitos, duración y costo están escritos en los ejercicios; son de ejemplo.",
    "Aprenderé a distinguir hechos, mitos y derechos sobre estudiar y trabajar después de la media, y a reconocer ofertas engañosas. Sirve para decidir con información confiable.",
    ["Sé reconocer caminos posibles.", "Sé distinguir hechos y mitos."],
    [
        "Un hecho se comprueba en una fuente oficial. Es un hecho que para ingresar a la educación superior se necesita haber terminado la enseñanza media, y que las instituciones publican sus requisitos, sus carreras y sus costos. Un mito es una creencia sin respaldo, como «los técnicos no consiguen trabajo» o «solo las carreras largas valen la pena».",
        "Los apoyos económicos, como becas y gratuidad, existen según requisitos que se consultan en fuentes oficiales y con la persona orientadora, porque cambian con el tiempo. Los datos de duración y costo de este cuaderno son de ejemplo y deben comprobarse en cada institución.",
        "Toda persona tiene derecho a educarse y a trabajar sin discriminación por género, origen o apariencia. Hay también límites y cuidados. Una oferta de trabajo que pide pagar antes de empezar, o que solicita claves y datos privados, puede ser una estafa. En ese caso no se entrega nada y se avisa a una persona adulta de confianza.",
    ],
    [("requisito", "condición que se debe cumplir para ingresar o postular"), ("beca", "apoyo económico para estudiar"), ("estafa", "engaño para quitar dinero o datos"), ("fuente oficial", "sitio o documento de una institución reconocida"), ("empleabilidad", "posibilidad de conseguir trabajo")],
    [
        W("Mito o hecho", "«Los técnicos nunca consiguen trabajo». ¿Es un hecho o un mito?", ["Es una generalización.", "No se apoya en datos oficiales."], "Es un mito"),
        W("Detectar una estafa", "Un aviso dice: «Trabajo seguro: paga $30.000 para tomar el puesto y envía tu clave del banco». ¿Qué haces?", ["Pide dinero previo.", "Pide una clave privada."], "No pagas ni envías nada y avisas a una persona adulta"),
    ],
    [
        M("Aceptar una oferta que pide pagar antes de trabajar.", "Se confía en la promesa de empleo rápido.", "Ninguna oferta seria cobra por contratar; avisa a una persona adulta."),
        M("Usar cifras de duración o costo sin comprobarlas.", "Se toma un dato de ejemplo como real.", "Verifica los datos en la institución."),
    ],
    R=[
        ex("Para ingresar a la educación superior se necesita haber terminado la enseñanza media. ¿Es un hecho o un mito?", "Un hecho", "Es un requisito general."),
        ex("Una oferta de trabajo que pide pagar antes de empezar, ¿puede ser estafa? Responde sí o no.", "Sí", "Es una señal de alerta."),
        ex("Una beca es un apoyo para estudiar A) económico B) deportivo", "A", "Ayuda a pagar estudios."),
    ],
    U=[
        ex("¿Dónde se comprueban los requisitos de una carrera? A) En la fuente oficial de la institución B) En una cadena de mensajes", "A", "Una fuente oficial es confiable."),
        ex("«Solo las carreras largas valen la pena» es A) un mito B) un hecho", "A", "Cada persona valora distintos caminos."),
        ex("¿Qué haces si un aviso pide tu clave? A) No la entregas y avisas a un adulto B) La envías", "A", "Las claves no se comparten."),
    ],
    A=[
        ex("Clasifica con H (hecho) o M (mito): 1) «Las instituciones publican sus requisitos.» 2) «Los técnicos no sirven.» 3) «Hay apoyos económicos según requisitos.» Escribe las letras en orden.", "H, M, H", "La 2 es una generalización sin base."),
        ex("En un ejemplo, un CFT de datos inventados dura 4 semestres y un IP, 8 semestres. ¿Cuántos semestres más dura el IP?", "4", "8 menos 4 son 4."),
        ex("Un aviso pide el nombre completo, la dirección y un pago de $10.000 «para reservar el puesto». ¿Qué señal de alerta tiene? A) Pide pago y datos privados B) Ofrece trabajo", "A", "Una oferta seria no cobra por contratar."),
    ],
    Z=[
        ex("¿Por qué conviene verificar los datos en la fuente oficial?", "Porque los datos cambian y las cadenas de mensajes pueden estar desactualizadas o ser falsas", "Los datos oficiales son más confiables."),
        ex("Un compañero dice: «Mi tío dijo que esa carrera ya no sirve». ¿Qué respondes? A) Lo verifico en una fuente oficial antes de descartar B) Lo creo y la descarto", "A", "Una opinión no es una prueba."),
    ],
    D=[
        arith("Una carrera de datos inventados cuesta $900.000 por año y una beca cubre $400.000. ¿Cuánto debe pagar la familia al año?", "900000-400000", "Al costo se le resta la beca.", " pesos"),
        arith("Un curso de ejemplo cuesta $15.000 al mes durante 6 meses. ¿Cuánto cuesta en total?", "15000*6", "Se multiplica el costo mensual por los meses.", " pesos"),
    ],
    context=[ex("Una joven de ejemplo recibe un mensaje: «Ganaste una beca, envía tus claves». ¿Qué conviene hacer? A) No enviar nada y avisar a una persona adulta B) Enviar para no perderla", "A", "Es una posible estafa.")],
    selfcheck=[ex("En Orientación: ¿una oferta seria cobra por contratar?", "No", "Pedir pago previo es alerta."), ex("¿Los apoyos económicos se consultan en fuentes oficiales?", "Sí", "Cambian con el tiempo."), ex("¿Un mito es una creencia sin respaldo?", "Sí", "Se repite sin pruebas.")],
    task=T("Clasifica estas cuatro frases inventadas como hecho, mito o señal de estafa y escribe una razón: (a) «Hay que terminar la media para entrar a la educación superior»; (b) «Una carrera técnica nunca da trabajo»; (c) «Paga $50.000 hoy y empiezas mañana»; (d) «Las instituciones publican sus requisitos». Luego escribe qué harías con (c).", "(a) Hecho. (b) Mito: generaliza. (c) Señal de estafa: pide pago previo; no pagar y avisar a una persona adulta de confianza. (d) Hecho.", ["clasifica las cuatro frases", "da una razón", "indica qué hacer con (c)", "nombra a una persona adulta"], ["tabla escrita", "explicación oral"], ["llamar hecho a un mito", "pagar o enviar datos"], "Reconoce las razones y pregunta dónde comprobaría la información."),
    reinforce="Escribe un mito que hayas oído sobre estudiar en general y cómo lo comprobarías.",
    extend="Explica por qué los datos de este cuaderno deben comprobarse en cada institución.",
)

lesson(
    OA9, 3,
    "Una hoja y un lápiz. Los caminos de Ignacia, una estudiante inventada, y sus datos de ejemplo están escritos en los ejercicios.",
    "Aprenderé a contrastar caminos académicos y laborales con una tabla de habilidades, intereses, viabilidad y proyección. Sirve para decidir entre varias opciones con datos.",
    ["Sé que hay varios caminos.", "Sé verificar información en fuentes oficiales."],
    [
        "Contrastar es poner dos o más caminos lado a lado con los mismos criterios. Una tabla útil usa cuatro: habilidades (¿coincide con lo que sé hacer?), intereses (¿me atrae?), viabilidad (¿puedo hacerlo con mi tiempo, dinero y ubicación?) y proyección (¿qué oportunidades abre después?). Cada sí vale 1 punto.",
        "Los puntos no dan un resultado automático. Si dos caminos empatan, se averigua el dato que falta. También se puede ponderar, es decir, dar más peso a un criterio, pero hay que decirlo antes de sumar. Y siempre se puede probar un camino y cambiar si aparece nueva información.",
        "Hay caminos que combinan, como trabajar y estudiar de noche, o capacitarse mientras se termina la media. Contrastar no exige elegir para siempre. Ayuda a dar el próximo paso con más seguridad. Los datos de duración y costo de los ejemplos son inventados: en la vida real se comprueban en cada institución.",
    ],
    [("contrastar", "poner opciones lado a lado con los mismos criterios"), ("viabilidad", "posibilidad de realizarse con las condiciones de hoy"), ("proyección", "oportunidades que una opción abre a futuro"), ("ponderar", "dar más peso a un criterio"), ("combinar", "hacer dos cosas a la vez, como estudiar y trabajar")],
    [
        W("Sumar puntos", "Ignacia evalúa técnico en enfermería: habilidades sí, intereses sí, viabilidad no, proyección sí. ¿Cuántos puntos suma?", ["Se cuentan los síes.", "Son tres."], "3 puntos"),
        W("Ponderar", "Ignacia decide que viabilidad vale doble. Camino X: habilidades sí, intereses no, viabilidad sí, proyección sí. ¿Cuántos puntos suma?", ["Habilidades vale 1.", "Intereses vale 0.", "Viabilidad vale 2 y proyección 1."], "4 puntos"),
    ],
    [
        M("Elegir solo por el camino con más puntos sin mirar el dato que lo sostiene.", "Se confía en el número.", "Revisa qué criterio aportó el punto."),
        M("Creer que la elección es para toda la vida.", "Se teme equivocarse.", "Puedes ajustar si cambian los datos."),
    ],
    R=[
        ex("Un camino con cuatro síes, ¿cuántos puntos suma si cada sí vale 1?", "4", "Se cuentan los síes."),
        ex("¿Qué criterio mira si puedes hacerlo con tu tiempo y dinero? A) Viabilidad B) Interés", "A", "Habla de las condiciones."),
        ex("Dar más peso a un criterio al comparar es A) ponderar B) empatar", "A", "Esa es la definición."),
    ],
    U=[
        ex("Si dos caminos empatan, ¿qué haces? A) Averiguas el dato que falta B) Eliges al azar", "A", "El empate indica falta de información."),
        ex("¿Qué criterio mira las oportunidades que abre después? A) La proyección B) Las habilidades", "A", "Habla del futuro."),
        ex("¿Se puede cambiar de camino si aparece nueva información? A) Sí B) No", "A", "El proyecto es flexible."),
    ],
    A=[
        ex("Ignacia evalúa: Enfermería: habilidades sí, intereses sí, viabilidad no, proyección sí. Informática: sí, no, sí, sí. Cada sí vale 1. ¿Qué camino suma más?", "Hay empate con 3 puntos cada uno", "Cada una suma 3 síes."),
        ex("Con viabilidad valiendo doble, Enfermería suma 3 y Informática suma 4. ¿Cuál tiene más puntos?", "Informática", "Gana por un punto."),
        ex("Un camino combina trabajar de día y estudiar de noche. ¿Qué criterio conviene revisar especialmente? A) Viabilidad B) Interés", "A", "Exige organizar el tiempo y la energía."),
    ],
    Z=[
        ex("¿Por qué un empate de puntos no obliga a elegir al azar?", "Porque indica que falta un dato para decidir mejor", "La tabla orienta."),
        ex("Dos estudiantes tienen los mismos datos pero ponderan distinto. ¿Es posible que decidan diferente? A) Sí, si explican su ponderación B) No", "A", "Los pesos son personales."),
    ],
    D=[
        arith("Ignacia compara 4 caminos con 4 criterios. ¿Cuántas respuestas debe dar en total?", "4*4", "Se multiplican caminos por criterios."),
        arith("Un camino técnico de datos inventados dura 4 semestres y uno universitario, 10 semestres. ¿Cuántos semestres más dura el universitario?", "10-4", "Se resta la duración menor de la mayor."),
    ],
    context=[ex("En la hora de orientación, un grupo compara estudiar un oficio o trabajar de inmediato en un taller familiar. ¿Qué criterio es clave? A) Viabilidad y proyección B) El color del taller", "A", "Decide qué se puede hacer hoy y qué abre después.")],
    selfcheck=[ex("En Orientación: ¿contrastar es poner opciones lado a lado?", "Sí", "Con los mismos criterios."), ex("¿Ponderar exige decirlo antes de sumar?", "Sí", "Así se entiende el resultado."), ex("¿Un camino se puede ajustar después?", "Sí", "Con nueva información.")],
    task=T("Ignacia tiene tres caminos: (1) técnico en una especialidad de salud en un CFT, 2 años, costo medio (datos de ejemplo); (2) trabajar en un comercio familiar con ingreso inmediato; (3) estudiar una carrera universitaria en otra ciudad, 5 años, costo alto. Datos de Ignacia: se le dan bien la biología y atender público; le interesan la salud y ayudar a otras personas; su familia puede pagar un costo medio, pero no uno alto. Haz una tabla con los cuatro criterios (habilidades, intereses, viabilidad, proyección), un sí o no por cada uno con una razón, suma puntos y elige. Escribe un dato que averiguarías.", "Ejemplo: (1) sí, sí, sí, sí = 4. (2) sí, no, sí, no = 2. (3) sí, sí, no, sí = 3. Elige (1). Dato a averiguar: becas para ese CFT.", ["completa los cuatro criterios por camino", "da razones", "suma bien", "señala un dato a averiguar"], ["tabla escrita", "explicación oral"], ["sumar mal", "no justificar"], "Reconoce el orden y pregunta qué dato cambiaría su decisión."),
    reinforce="Compara dos caminos inventados con los cuatro criterios y suma sus puntos.",
    extend="Explica cómo cambiaría tu tabla si ponderas más el interés.",
)

lesson(
    OA9, 4,
    "Una hoja y un lápiz. Los pasos de un plan de exploración y las ofertas de ejemplo están escritos en los ejercicios.",
    "Aprenderé a elegir un próximo paso seguro para explorar caminos académicos y laborales: informarme, hablar con una persona orientadora, visitar y evitar ofertas engañosas. Sirve para avanzar sin riesgos.",
    ["Sé contrastar caminos con una tabla.", "Sé reconocer una estafa."],
    [
        "Elegir un camino es un proceso, no un momento. Un plan de exploración tiene cuatro pasos: informarse en fuentes oficiales, conversar con personas que ya recorrieron el camino y con la persona orientadora, probar con una actividad pequeña, como una visita o un taller, y decidir el próximo paso. Cada paso reduce la incertidumbre.",
        "Una acción segura al explorar es usar sitios oficiales, ir a ferias y visitas con apoyo de una persona adulta o del liceo, y compartir pocos datos personales. No se paga por empleos ni se entregan claves. Si una oferta parece demasiado buena, se consulta con una persona adulta de confianza antes de contestar.",
        "También conviene tener un plan B, que es otra opción por si el primer camino no resulta. Por ejemplo, si no entras a una carrera, puedes intentar otra institución, preparar de nuevo la prueba o capacitarte y trabajar. Tener un plan B no es rendirse: es ser flexible.",
    ],
    [("plan de exploración", "pasos para conocer caminos antes de decidir"), ("incertidumbre", "falta de seguridad sobre lo que ocurrirá"), ("plan B", "otra opción por si la primera no resulta"), ("feria", "evento donde instituciones muestran sus carreras"), ("flexible", "que puede cambiar según las circunstancias")],
    [
        W("Ordenar un plan", "Ignacia quiere explorar. ¿Cuál es un primer paso adecuado: pagar por un cupo o informarse en una fuente oficial?", ["Pagar sin informarse es riesgoso.", "Informarse reduce la incertidumbre."], "Informarse en una fuente oficial"),
        W("Plan B", "Si Ignacia no entra a su primera opción, ¿qué plan B puede tener?", ["Otra institución, otra carrera o capacitación.", "Debe ser realista."], "Otra institución, otra carrera o capacitarse y trabajar"),
    ],
    [
        M("Decidir sin hablar con nadie que haya recorrido el camino.", "Se cree que basta lo que se imagina.", "Conversa con personas y con la orientadora."),
        M("Pensar que tener plan B es no creer en el plan A.", "Se confunde flexibilidad con duda.", "Un plan B te protege."),
    ],
    R=[
        ex("Informarse en fuentes oficiales, ¿es un buen primer paso? Responde sí o no.", "Sí", "Reduce la incertidumbre."),
        ex("¿Qué es un plan B? A) Otra opción por si la primera no resulta B) Un abandono", "A", "Es una alternativa realista."),
        ex("Una oferta que pide claves, ¿se contesta? Responde sí o no.", "No", "Se consulta antes con una persona adulta."),
    ],
    U=[
        ex("¿Para qué sirve una visita o taller pequeño? A) Para probar un camino antes de decidir B) Para ganar tiempo", "A", "Permite conocerlo en la práctica."),
        ex("¿Con quién conviene conversar? A) Con personas que ya recorrieron ese camino y con la orientadora B) Con nadie", "A", "Aportan experiencia real del camino."),
        ex("Una oferta demasiado buena, ¿qué conviene? A) Consultar a una persona adulta de confianza B) Aceptar rápido", "A", "Puede ser una estafa."),
    ],
    A=[
        ex("Ordena con letras los pasos: (a) decidir el próximo paso, (b) informarse, (c) probar con una actividad pequeña. ¿Cuál va primero?", "b", "Primero se informa."),
        ex("Clasifica con S (segura) o N (no segura): 1) Visitar una feria con el liceo. 2) Enviar tus claves a un aviso. 3) Hablar con la orientadora. Escribe las letras en orden.", "S, N, S", "La 2 entrega datos privados."),
        ex("Ignacia planea visitar 2 instituciones por mes durante 3 meses. ¿Cuántas visitas hace?", "6", "2 por 3 son 6."),
    ],
    Z=[
        ex("¿Por qué probar con una actividad pequeña ayuda a decidir?", "Porque permite conocer el camino en la práctica antes de comprometerse del todo", "La experiencia aporta datos."),
        ex("Un compañero dice: «Si cambio de camino, perdí el tiempo». ¿Qué respondes? A) Lo aprendido sirve para el próximo paso B) Tienes razón", "A", "Toda experiencia da información."),
    ],
    D=[
        arith("Un plan de exploración tiene 4 pasos y cada uno se revisa en 2 semanas. ¿Cuántas semanas dura el plan?", "4*2", "Se multiplican pasos por semanas."),
        arith("De 40 estudiantes que visitan una feria, 26 anotan al menos una carrera que les interesa. ¿Cuántos no anotan ninguna?", "40-26", "Al total se le restan quienes anotaron."),
    ],
    context=[ex("En una feria vocacional inventada, un stand ofrece «empleo seguro» si dejas tus datos y pagas un cupo. ¿Qué conviene? A) No dejar datos ni pagar y consultar a una persona adulta B) Pagar para asegurarlo", "A", "Pedir pago previo es una señal de alerta.")],
    selfcheck=[ex("En Orientación: ¿explorar es un proceso?", "Sí", "Se hace en pasos."), ex("¿Se entregan claves en una oferta de trabajo?", "No", "Son datos privados que no se comparten."), ex("¿Un plan B es ser flexible?", "Sí", "Protege ante cambios.")],
    task=T("Arma un plan de exploración de cuatro pasos para un personaje inventado, Felipe, a quien le interesa la mecánica y la electricidad, y que quiere decidir si seguir un técnico o trabajar primero. Incluye: (1) una fuente oficial para informarse, (2) una persona con quien hablar, (3) una actividad para probar el camino y (4) un plan B. Agrega una señal de oferta engañosa que debe evitar y a quién consultaría.", "Fuente: sitios oficiales de instituciones. Persona: la orientadora y un técnico del rubro. Actividad: visitar un taller o feria con el liceo. Plan B: trabajar un año y volver a postular. Señal engañosa: pedir pago previo o claves; consulta a una persona adulta de confianza.", ["cuatro pasos", "incluye plan B", "señala una oferta engañosa", "nombra a una persona adulta"], ["plan escrito", "tabla"], ["omitir fuentes oficiales", "no considerar riesgos"], "Reconoce el orden del plan y pregunta cómo evaluaría cada paso."),
    reinforce="Escribe un plan B posible para un personaje inventado que no ingresa a su carrera.",
    extend="Explica cómo cambiaría tu plan si tu primera visita no te convence.",
)

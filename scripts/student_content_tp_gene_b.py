"""Objetivos genéricos TP 3.º y 4.º medio, módulo B: OAG-04 (trabajo en equipo), OAG-05 (respeto y no discriminación) y OAG-06 (deberes y derechos laborales).
Todo en papel: empresas, personas, documentos y cifras inventados y rotulados «de ejemplo». Sin cifras legales: para los derechos laborales se remite a la norma vigente y a las fuentes oficiales."""
from __future__ import annotations

from tp_gene_common import build

G4 = "TP-GENE-3y4-OAG-04"
G5 = "TP-GENE-3y4-OAG-05"
G6 = "TP-GENE-3y4-OAG-06"
LIM = " Este cuaderno trabaja en papel, con casos de ejemplo: no reemplaza a tu profesor, a tu jefatura ni a la norma vigente."

# ============================================================ OAG-04, clase 1
F = ("Ficha 13 (equipo de un centro de salud familiar de ejemplo, turno de mañana). Jefa de turno: Marta (coordina y resuelve problemas). Admisión: Ignacia (registra a las personas y entrega números de atención). "
     "Técnico en enfermería: Paulo (apoya la atención en los boxes y mantiene ordenados los insumos). Auxiliar de servicios: Rosa (mantiene limpias las salas). "
     "Objetivo común: atender a 40 personas entre las 08:00 y las 12:00 con buen trato y sin esperas largas.")
build(
    G4, 1, F,
    use="Aprenderé qué es un equipo de trabajo, cómo se distribuyen los roles y qué actitudes ayudan a lograr un objetivo común.",
    prior=["Sé leer una ficha con roles.", "Sé dividir números enteros.", "Sé que cada trabajo tiene funciones distintas."],
    explain=[
        "Un equipo de trabajo es un grupo de personas que se coordinan para lograr un objetivo común. No basta con compartir el lugar de trabajo: hace falta un objetivo conocido por todos, roles claros, comunicación y apoyo mutuo. El rol es la función y las responsabilidades que cumple cada integrante; el objetivo común es el resultado que todos buscan.",
        "Cada persona es responsable de su parte, y el equipo es responsable del resultado completo. Por eso, si una persona se atrasa, el resto lo siente: el trabajo es una cadena. Un buen integrante cumple lo suyo, avisa con tiempo si tiene un problema, pide ayuda cuando la necesita y ayuda a otros dentro de lo que sabe hacer y está autorizado a hacer. La jefatura o coordinación decide, organiza y resuelve los conflictos de funciones.",
        "Un equipo funciona mejor con respeto: se escucha a todos, se valoran los aportes de cada uno y no se discrimina por ninguna característica personal." + LIM,
    ],
    vocab=[("equipo de trabajo", "grupo de personas que se coordinan para lograr un objetivo común"), ("rol", "función y responsabilidades que cumple cada integrante"), ("objetivo común", "resultado que todo el equipo busca lograr"), ("coordinación", "organización del trabajo entre varias personas para que se complemente"), ("apoyo mutuo", "ayuda entre integrantes del equipo"), ("responsabilidad", "obligación de cumplir lo que corresponde a cada uno")],
    worked=[
        ("Identificar el objetivo común", "En una cocina de casino de ejemplo, todas las personas buscan servir 120 almuerzos a las 13:00, con buena calidad. ¿Cuál es el objetivo común?", ["Es el resultado que todos buscan.", "Servir los almuerzos a la hora con buena calidad."], "Servir los 120 almuerzos a las 13:00 con buena calidad"),
        ("Calcular un ritmo", "Un equipo de ejemplo debe atender 60 personas en 3 horas. ¿Cuántas personas por hora, en promedio?", ["Se divide el total entre las horas.", "60 ÷ 3 = 20."], "20 personas por hora"),
    ],
    mistakes=[("Pensar «yo cumplo mi parte y lo demás no me importa».", "El resultado es del equipo completo; si otra parte se atrasa, mi trabajo también se ve afectado.", "Cumple lo tuyo y avisa o ayuda si ves un problema que afecta al objetivo."),
              ("Cambiar el orden de las tareas sin avisar al resto.", "Quienes dependen de ese orden quedan desorientados y se generan atrasos.", "Comunica las decisiones que afectan a otros antes de ejecutarlas.")],
    T=[
        ("abc", "En trabajo en equipo: ¿qué es un rol?", "La función y las responsabilidades de cada integrante", "El cargo más alto del equipo", "La personalidad de cada integrante", "El rol describe qué hace y de qué responde cada persona, no su carácter ni su jerarquía."),
        ("abc", "{F} ¿Cuál es el objetivo común del equipo?", "Atender a 40 personas entre las 08:00 y las 12:00 con buen trato y sin esperas largas", "Que Marta termine antes sus tareas", "Que cada persona atienda más rápido que las demás", "El objetivo común es del equipo completo y está escrito en la ficha."),
        ("abc", "{F} ¿Qué rol cumple Ignacia?", "Admisión: registra a las personas y entrega números", "Coordina y resuelve problemas", "Mantiene limpias las salas", "La ficha le asigna admisión; la coordinación es de Marta y el aseo de Rosa."),
        ("abc", "Cinco cocineros de ejemplo se reparten tareas, se avisan los pedidos y se ayudan cuando uno se atrasa. ¿Qué característica de un equipo muestran?", "Coordinación y apoyo mutuo para un objetivo común", "Competencia entre ellos para ver quién gana", "Trabajo individual sin comunicación", "Repartir tareas, avisarse y ayudarse son rasgos propios de un equipo."),
        ("abc", "{F} Paulo ve que Rosa tiene 3 salas por limpiar y él ya terminó lo suyo. ¿Qué actitud de equipo corresponde?", "Ofrecer ayuda en lo que pueda hacer sin riesgo ni autorización especial, y avisar a Marta", "No ayudar, porque no es su función", "Hacer el aseo con prisa sin avisar a nadie", "Ayudar dentro de lo permitido y comunicarlo mantiene el orden del equipo."),
        ("abc", "Un integrante de un equipo de bodega de ejemplo no cumple su parte. ¿Qué efecto tiene?", "Se afecta el resultado de todo el equipo", "Solo se afecta él, porque cada uno trabaja aparte", "No pasa nada si los demás trabajan más rápido", "En un equipo las tareas se encadenan, así que una falla repercute en los demás."),
        ("=", "{F} ¿Cuántas personas por hora, en promedio, deben atenderse entre las 08:00 y las 12:00?", "40//(12-8)", "Se divide el total de personas entre las horas de atención.", " personas por hora"),
        ("=", "{F} Ignacia registra a cada persona en 3 minutos. ¿Cuántas personas puede registrar en una hora?", "60//3", "Se divide el total de minutos entre lo que tarda cada registro.", " personas"),
        ("=", "{F} Rosa limpia 6 salas en 2 horas a ritmo constante. ¿Cuántas salas limpia entre las 08:00 y las 12:00?", "(6//2)*(12-8)", "Se calcula el ritmo por hora y se multiplica por las horas de la jornada.", " salas"),
        ("abc", "{F} Marta dice: «Si cada uno hace solo lo suyo y no avisa nada, igual cumpliremos el objetivo». ¿Qué problema tiene esa idea?", "Sin coordinación, el atraso de una persona se acumula y afecta al resto", "Ninguno, porque cada rol es independiente", "Que obliga a todos a hacer el trabajo de los demás", "Los roles se complementan y exigen comunicación para llegar al objetivo."),
        ("abc", "Una integrante de un equipo de oficina de ejemplo se ausenta un día. ¿Qué conviene hacer?", "Redistribuir sus tareas entre todos de forma acordada y avisar a la jefatura", "Que una sola persona haga todo", "Dejar sus tareas sin hacer hasta que vuelva", "Redistribuir de forma acordada mantiene el trabajo sin sobrecargar a una persona."),
        ("abc", "{F} Una persona nueva pregunta qué hacer si faltan insumos en los boxes. ¿Qué respuesta corresponde según los roles?", "Paulo detecta el faltante y avisa a Marta, quien resuelve", "Rosa los compra sin avisar", "Ignacia suspende la atención", "Según los roles, Paulo cuida los insumos y Marta coordina y resuelve."),
        ("abc", "{F} Un integrante propone que Marta no reparta funciones, porque «todos saben qué hacer». ¿Qué riesgo hay?", "Dos personas pueden hacer lo mismo y otras tareas quedar sin responsable", "Ninguno, porque con el tiempo todos aprenden solos", "Que Marta trabaje de más", "Sin roles claros se duplican esfuerzos y se pierden tareas."),
    ],
    ctx=("abc", "{F} A las 10:00 hay una fila larga en admisión y Paulo tiene un rato libre. Marta no está disponible por unos minutos. ¿Qué hace Paulo?", "Avisa a Marta o a Ignacia y ofrece ayudar en tareas que le corresponda hacer, como ordenar el paso de las personas", "Se queda esperando porque «no es su función»", "Empieza a registrar datos de las personas sin conocer el procedimiento", "Ayudar a coordinar la fila no exige autorización especial, pero registrar datos sí requiere conocer el procedimiento."),
    sc=[
        ("En un equipo de ejemplo: ¿qué es el objetivo común?", "El resultado que todos buscan", "Todos los integrantes trabajan para lograrlo."),
        ("¿Qué haces si tienes un problema que puede atrasar al equipo?", "Aviso con tiempo", "Avisar a tiempo permite reorganizar el trabajo de todos."),
        ("¿Qué es el apoyo mutuo?", "Ayuda entre integrantes del equipo", "Ayuda a lograr el objetivo cuando alguien se atrasa."),
    ],
    op=("Caso de ejemplo. Un restaurante ficticio prepara 96 almuerzos para las 13:00. Equipo: la cocinera Lidia (prepara los platos de fondo), el ayudante Mario (corta ingredientes y los deja listos), la garzona Eva (recibe pedidos y sirve) y el encargado Bruno (coordina y resuelve). Tres días antes, Mario avisa que no podrá cumplir su parte porque tendrá un trámite. "
        "Escribe: (1) el objetivo común, (2) el rol de cada persona, (3) cuántos almuerzos por hora debe sacar el equipo si empieza a las 09:00, (4) dos acciones que debería hacer Mario y una que debería hacer Bruno.",
        "(1) Servir 96 almuerzos a las 13:00 con buena calidad. (2) Lidia: platos de fondo; Mario: cortar ingredientes; Eva: pedidos y servicio; Bruno: coordinar. (3) De 09:00 a 13:00 hay 4 horas: 96 ÷ 4 = 24 almuerzos por hora. (4) Mario avisa con tiempo y propone cómo cubrir su parte; Bruno reorganiza las tareas.",
        ["identifica el objetivo común", "asigna correctamente los roles", "propone acciones de equipo"],
        ["hoja con cuatro respuestas"],
        ["no avisar a tiempo", "no reorganizar los roles", "culpar a Mario"],
        "Pregunta: «¿qué pasaría si nadie reorganiza el trabajo?». Debe decir que el resto se sobrecarga o que los platos no estarían a tiempo."),
    reinforce="Escribe los roles de un equipo de tu especialidad y el objetivo común que comparten.",
    extend="Explica con un ejemplo por qué comunicar un problema a tiempo es una forma de apoyo al equipo.",
)

# ============================================================ OAG-04, clase 2
F = ("Ficha 14 (equipo de archivo de una oficina de ejemplo). Meta de hoy: archivar 108 carpetas entre las 09:00 y las 13:00. Ritmos de ejemplo: Alma archiva 12 carpetas por hora, Bruno 9, Carla 6 y Diego 9. "
     "Regla del equipo: las tareas se reparten según el ritmo de cada persona y se avisa a la jefatura si no se llega a la meta.")
build(
    G4, 2, F,
    use="Aprenderé a repartir tareas y a coordinar un equipo según las capacidades de cada persona, avisando cuando no se llega a la meta.",
    prior=["Sé qué es un rol y un objetivo común.", "Sé sumar y multiplicar enteros.", "Sé calcular tiempos."],
    explain=[
        "Repartir una tarea entre varias personas no siempre significa dar lo mismo a cada una. Un reparto equitativo considera el ritmo, la experiencia y la carga que ya tiene cada persona. Si Alma archiva el doble que Carla, le toca una parte mayor para que todos terminen a la vez. Un reparto en partes iguales puede dejar a alguien sin terminar y atrasar al equipo.",
        "Para saber si un equipo llega a la meta se calcula su capacidad: lo que logra entre todos en una hora, multiplicado por las horas disponibles. Si la capacidad es menor que la meta, se avisa a tiempo a la jefatura y se propone una solución: más plazo, apoyo de otra persona o reorganizar tareas. Un cuadro de tareas con nombre de la persona, la tarea y la hora ayuda a que todos sepan qué les toca y permite revisar el avance.",
        "El equipo registra con honestidad lo que avanza. Marcar «listo» una tarea que no está terminada engaña a quien toma decisiones." + LIM,
    ],
    vocab=[("reparto equitativo", "reparto que considera el ritmo y la carga de cada persona"), ("capacidad", "cantidad de trabajo que un equipo puede hacer en un tiempo"), ("ritmo", "cantidad de trabajo que una persona hace en una hora"), ("cuadro de tareas", "lista que indica quién hace cada tarea y para cuándo"), ("avance", "parte del trabajo ya realizada")],
    worked=[
        ("Capacidad por hora", "Dos personas de ejemplo arman 8 y 12 cajas por hora. ¿Cuántas arman juntas en una hora?", ["Se suman los ritmos individuales.", "8 + 12 = 20."], "20 cajas por hora"),
        ("Reparto según ritmo", "Un equipo de ejemplo debe empacar 60 pedidos. Una persona hace 1 de cada 3 pedidos del equipo y otra los otros 2 de cada 3. ¿Cuántos pedidos le tocan a cada una?", ["Se divide 60 en tres partes iguales.", "Una hace 20 y la otra 40."], "20 y 40 pedidos"),
    ],
    mistakes=[("Repartir en partes iguales aunque los ritmos sean muy distintos.", "La persona más lenta puede no terminar y retrasar al equipo.", "Reparte según el ritmo y la carga de cada persona."),
              ("Marcar «listo» una tarea que no está terminada para que el equipo «parezca» al día.", "La jefatura decide con datos falsos y el atraso se descubre tarde.", "Registra el avance real y avisa si hay retraso.")],
    T=[
        ("abc", "En trabajo en equipo: ¿cómo se reparte una tarea de forma equitativa?", "Considerando el ritmo y la carga de cada persona", "Dando exactamente lo mismo a todas sin mirar nada más", "Dando más trabajo a quien reclama menos", "El reparto equitativo ajusta la carga a la capacidad de cada persona."),
        ("=", "{F} ¿Cuántas carpetas archiva el equipo en una hora, sumando los cuatro ritmos?", "12+9+6+9", "Se suman los ritmos de las cuatro personas.", " carpetas"),
        ("abc", "{F} ¿Qué dice la regla del equipo si no se llega a la meta?", "Avisar a la jefatura", "Seguir trabajando sin avisar", "Reducir la meta por cuenta propia", "La ficha establece que se avisa a la jefatura cuando no se llega a la meta."),
        ("=", "{F} ¿Cuántas carpetas puede archivar el equipo entre las 09:00 y las 13:00?", "(12+9+6+9)*(13-9)", "Se multiplica la capacidad por hora por las horas de la jornada.", " carpetas"),
        ("abc", "En una cocina de ejemplo, el jefe anota en un cuadro quién hace cada tarea del servicio. ¿Para qué sirve ese cuadro?", "Para que cada persona sepa qué le toca y se pueda revisar el avance", "Para que nadie pueda cambiar de tarea nunca", "Para decidir los sueldos del mes", "El cuadro de tareas ordena las responsabilidades y permite seguir el avance."),
        ("=", "{F} Si el equipo archiva a su capacidad completa, ¿cuántas carpetas más que la meta alcanzaría a archivar?", "(12+9+6+9)*(13-9)-108", "Se resta la meta a la capacidad total del equipo.", " carpetas"),
        ("=", "{F} Si Carla y Diego no pueden venir, ¿cuántas carpetas de la meta no alcanzan a archivarse?", "108-(12+9)*(13-9)", "Se calcula la capacidad de Alma y Bruno y se resta de la meta.", " carpetas"),
        ("=", "{F} Si la meta se repartiera según el ritmo (12 de cada 36 carpetas de la meta para Alma), ¿cuántas carpetas le tocan a Alma?", "108*12//36", "Se calcula la parte de Alma según su ritmo dentro del total.", " carpetas"),
        ("abc", "{F} Bruno termina antes y ve que Diego va atrasado. ¿Qué actitud ayuda más al equipo?", "Ofrecerle ayuda y avisar a la jefatura del nuevo reparto", "Esperar a que Diego lo pida", "Archivar solo sus carpetas", "La ayuda ofrecida a tiempo y comunicada mantiene la meta del equipo."),
        ("abc", "{F} Un compañero propone repartir la meta en partes iguales entre las 4 personas. ¿Qué problema puede tener?", "Carla, más lenta, podría no terminar su parte y retrasar al equipo", "Ninguno, porque lo igual siempre es lo más justo", "Que Alma se aburra", "Con ritmos distintos, las partes iguales hacen que algunos terminen antes que otros."),
        ("abc", "Alma anota «listo» en el cuadro, aunque le quedan 5 carpetas, para que parezca que el equipo va al día. ¿Qué problema genera?", "La jefatura decide con datos falsos y el atraso se descubre tarde", "Ninguno, porque son pocas carpetas", "Que Alma queda con menos trabajo", "Un registro falso impide reorganizar el trabajo a tiempo."),
        ("abc", "{F} Con Carla y Diego ausentes faltan carpetas para la meta. ¿Qué propuesta es la mejor?", "Avisar a la jefatura y proponer más plazo o apoyo de otra persona para las que faltan", "Ocultar la falta y archivar menos sin decir nada", "Pedir a Alma y Bruno que trabajen sin pausa para cumplir", "Avisar y proponer una solución cumple la regla y protege el bienestar del equipo."),
        ("abc", "Un equipo de ejemplo reparte las tareas de cierre de una tienda: contar caja, ordenar góndolas y apagar luces. Una persona termina con tiempo de sobra y otra está atrasada. ¿Qué es lo más útil?", "Reasignar una tarea de la persona atrasada a quien terminó, previo aviso al encargado", "Que cada uno termine su tarea sin importar el tiempo", "Esperar al día siguiente", "Reasignar sobre la marcha, con aviso, permite que el equipo termine a la vez."),
    ],
    ctx=("abc", "{F} A las 11:00 el equipo lleva 40 carpetas archivadas y trabaja a su capacidad completa. ¿Qué conclusión es correcta sobre la meta de 108 carpetas?", "Aún puede llegar a la meta, pero casi sin holgura: faltan 68 carpetas y en 2 horas puede archivar 72", "Ya no puede llegar a la meta y debe avisar de inmediato que no se cumplirá", "Va con mucha holgura, porque su capacidad de todo el día es de 144 carpetas", "A las 11:00 han pasado 2 horas; faltan 108 − 40 = 68 carpetas y en las 2 horas que quedan, a 36 por hora, se pueden archivar 72, es decir, 4 más de las que faltan."),
    sc=[
        ("En un equipo de ejemplo: ¿cómo se calcula la capacidad en una hora?", "Sumando los ritmos de todos", "La suma de ritmos individuales da la capacidad conjunta."),
        ("¿Qué haces si el equipo no llegará a la meta?", "Aviso a la jefatura y propongo una solución", "Avisar a tiempo permite reorganizar o cambiar el plazo."),
        ("¿Qué anotas en un cuadro de avance?", "Lo que realmente avanzaste", "Un registro verdadero permite tomar buenas decisiones."),
    ],
    op=("Caso de ejemplo. Un equipo de cuatro personas de un taller de confección ficticio debe empacar 120 prendas hoy entre las 10:00 y las 14:00. Ritmos de ejemplo por hora: Nina 10 prendas, Óscar 8, Paula 6 y Raúl 6. Regla del equipo: se avisa a la jefa si no se alcanza la meta. "
        "Escribe: (1) la capacidad del equipo en una hora, (2) la capacidad en la jornada, (3) si alcanza la meta, (4) qué harías si Raúl se ausenta, con los números.",
        "(1) 10 + 8 + 6 + 6 = 30 prendas por hora. (2) 30 × 4 = 120 prendas. (3) Alcanza justo, sin holgura. (4) Sin Raúl: 24 prendas por hora × 4 = 96; faltan 24, por lo que aviso a la jefa y propongo más plazo o apoyo de otra persona.",
        ["suma bien los ritmos", "calcula la capacidad de la jornada", "compara con la meta", "propone un aviso con números"],
        ["hoja con cuatro respuestas y cálculos"],
        ["repartir sin considerar ritmos", "no calcular la holgura", "no avisar"],
        "Pregunta: «¿qué ocurre si todos pierden 30 minutos?». Debe notar que la meta quedaría sin holgura y habría que avisar."),
    reinforce="Escribe un cuadro de tareas con cuatro tareas, quién las hace y para cuándo, para una tarea de tu especialidad.",
    extend="Explica por qué repartir según el ritmo es más justo que repartir en partes iguales cuando los ritmos son muy distintos.",
)

# ============================================================ OAG-04, clase 3
F = ("Ficha 15 (acta de reunión de ejemplo, cocina de un casino ficticio, 15 minutos). Asistentes: Julia (jefa), Tomás y Valeria. Tema: reparto del lavado de utensilios entre las 14:00 y las 15:00. "
     "Tomás dice que Valeria deja siempre utensilios sin lavar; Valeria dice que a ella le toca más cantidad. Datos del registro: Tomás lava 14 piezas por turno y Valeria 22. "
     "Acuerdos: 1) igualar la carga entre ambos; 2) Julia anotará el nuevo reparto en el cuadro de turnos; 3) revisar el resultado en una semana.")
build(
    G4, 3, F,
    use="Aprenderé a manejar un desacuerdo en el equipo con respeto, a comunicarme de forma asertiva y a conducir y registrar una reunión de trabajo.",
    prior=["Conozco roles y objetivo común.", "Sé calcular repartos.", "Sé escribir una lista corta."],
    explain=[
        "Un conflicto es una diferencia entre personas por opiniones, intereses o formas de trabajar. Es normal que aparezca en un equipo y puede resolverse si se maneja con respeto. Primero se escucha a cada persona sin interrumpir. Luego se separan los hechos de las opiniones, se identifica cuál es el problema real y se buscan opciones. Al final se acuerda una solución y se registra. Si no hay acuerdo, se pide ayuda a la jefatura o a la persona designada para mediar.",
        "Comunicarse de forma asertiva significa decir lo que piensas o necesitas con claridad y respeto, hablando de hechos y de cómo te afectan, sin atacar a la persona. Las formas pasiva (callar) y agresiva (insultar, burlarse) no resuelven el problema. Una reunión eficaz tiene objetivo, agenda con tiempos, turnos para hablar y un acta que registra los acuerdos: qué se hará, quién y para cuándo.",
        "Las burlas, los insultos y el acoso entre compañeros no son un conflicto de opiniones: son faltas de respeto que se informan a la jefatura." + LIM,
    ],
    vocab=[("conflicto", "diferencia entre personas por opiniones, intereses o formas de trabajar"), ("asertividad", "decir lo que piensas o necesitas con claridad y respeto"), ("mediar", "ayudar a que dos personas lleguen a un acuerdo"), ("agenda", "lista de temas y tiempos de una reunión"), ("acta", "registro escrito de los acuerdos de una reunión"), ("acuerdo", "decisión tomada por las personas, con quién la cumple y para cuándo")],
    worked=[
        ("Mensaje asertivo", "Una auxiliar de ejemplo está molesta porque su compañero deja la mesa sucia. ¿Qué frase es asertiva: «Eres un desordenado» o «Cuando la mesa queda sucia, me atraso; ¿podemos acordar quién la limpia?»?", ["La asertiva habla del hecho y de su efecto, sin atacar.", "Y propone una solución."], "La segunda frase"),
        ("Tiempo en una reunión", "Una reunión de ejemplo dura 40 minutos y tiene 2 temas de 10 minutos cada uno. ¿Cuántos minutos quedan para el acta y el cierre?", ["Se restan los tiempos de los temas.", "40 − 10 − 10 = 20."], "20 minutos"),
    ],
    mistakes=[("Responder a una crítica con otro insulto.", "El conflicto crece y se pierde el problema de fondo.", "Responde con calma, habla del hecho y propone una solución."),
              ("Escribir en el acta todo lo que dijo cada persona, palabra por palabra.", "El acta se vuelve larga y no se sabe qué se acordó.", "Registra solo los acuerdos: qué, quién y para cuándo.")],
    T=[
        ("abc", "En equipos de trabajo: ¿qué es un conflicto?", "Una diferencia entre personas por opiniones, intereses o formas de trabajar", "Una pelea física entre compañeros", "Una falta grave de respeto que siempre termina en sanción", "Un conflicto es una diferencia que se puede resolver; las faltas graves de respeto son otro tema."),
        ("abc", "{F} ¿Cuál es el problema que se discute en la reunión?", "El reparto de la carga del lavado de utensilios", "La compra de utensilios nuevos", "Los turnos de vacaciones del casino", "La ficha dice que el tema es el reparto del lavado entre Tomás y Valeria."),
        ("=", "{F} ¿Cuántas piezas lavan entre los dos por turno, según el registro?", "14+22", "Se suman las piezas de Tomás y las de Valeria.", " piezas"),
        ("=", "{F} Para igualar la carga entre ambos, ¿cuántas piezas debe lavar cada uno?", "(14+22)//2", "Se divide el total de piezas entre las dos personas.", " piezas"),
        ("abc", "Tomás está molesto con Valeria. ¿Qué formulación es asertiva?", "«Cuando quedan utensilios sin lavar al final del turno, me retraso; ¿revisamos el reparto?»", "«Siempre dejas todo botado»", "No decir nada y guardarse la molestia", "Lo asertivo describe el hecho y su efecto y propone algo, sin atacar ni callar."),
        ("abc", "{F} ¿Qué acuerdo del acta tiene un plazo de revisión?", "El acuerdo 3: revisar el resultado en una semana", "El acuerdo 1: igualar la carga", "El acuerdo 2: anotar el reparto", "El plazo de una semana aparece solo en el acuerdo 3."),
        ("=", "{F} Si Valeria pasa de lavar 22 a 18 piezas, ¿cuántas piezas menos lava?", "22-18", "Se resta la nueva carga a la que tenía antes.", " piezas"),
        ("abc", "Antes de una reunión de ejemplo, ¿qué conviene preparar?", "El objetivo, la agenda y el tiempo de cada tema", "Solo la sala, sin más preparación", "Una lista de quejas contra los demás", "Una reunión eficaz parte con objetivo claro y tiempos definidos."),
        ("abc", "¿Qué debe contener un acta de reunión?", "Los acuerdos con qué se hará, quién y para cuándo", "Todo lo que dijo cada persona, palabra por palabra", "Solo la lista de asistentes", "El acta sirve para saber qué se acordó y quién responde."),
        ("abc", "{F} Julia propone que en la próxima reunión se hable de la carga y no de las personas. ¿Por qué es útil?", "Centra la discusión en hechos y soluciones, no en culpas", "Evita que alguien tenga que hablar", "Hace la reunión más corta sin importar el resultado", "Hablar de hechos ayuda a encontrar soluciones sin atacar a nadie."),
        ("abc", "Dos compañeros conversaron del problema y no llegaron a acuerdo. ¿Qué corresponde?", "Pedir apoyo a la jefatura o a la persona que media", "Seguir discutiendo hasta que uno gane", "Dejar de hablarse para evitar problemas", "Cuando no hay acuerdo, se pide ayuda para mediar y no se escala el conflicto."),
        ("abc", "{F} Durante la reunión, Tomás imita burlándose la forma de hablar de Valeria. ¿Qué corresponde?", "Apoyar a Valeria y avisar a la jefatura o a la persona que conduce la reunión, sin responder con otra burla", "Reírse para no incomodar", "Ignorarlo, porque es parte del conflicto", "Una burla es una falta de respeto, no un desacuerdo de opiniones, y se informa a quien conduce la reunión o a la jefatura, sin devolver la burla."),
        ("=", "Una reunión de ejemplo de 60 minutos tiene tres temas: el primero de 15 minutos, el segundo de 20 y el tercero con el tiempo que queda. ¿Cuántos minutos tiene el tercero?", "60-15-20", "Al tiempo total se le restan los tiempos de los otros dos temas.", " minutos"),
    ],
    ctx=("abc", "{F} Después de la reunión, Valeria sigue sintiendo que el acuerdo 1 no considera que ella también atiende pedidos urgentes. ¿Qué hace?", "Pide conversar con Julia, expone el hecho con calma y propone ajustar el acuerdo en la revisión de la semana", "Incumple el acuerdo sin avisar", "Comenta con otros compañeros que Julia es injusta", "Plantear un hecho y proponer un ajuste respeta el acuerdo y permite mejorarlo."),
    sc=[
        ("En un equipo de ejemplo: ¿qué es hablar de forma asertiva?", "Decir lo que necesito con claridad y respeto", "Evita el ataque y también el silencio."),
        ("¿Qué datos tiene un acuerdo bien registrado?", "Qué, quién y para cuándo", "Así se sabe quién debe cumplir qué y cuándo."),
        ("¿Qué haces ante una burla en una reunión?", "Apoyo a la persona y aviso a la jefatura", "Una burla no es una opinión, es una falta de respeto que se informa."),
    ],
    op=("Caso de ejemplo. En una bodega ficticia, dos auxiliares, Camilo y Daniela, discuten porque Camilo siempre deja las cajas del pasillo 3 sin ordenar y Daniela debe hacerlo al final del turno. Camilo dice que a él le toca descargar y Daniela dice que ella tiene más pasillos. La jefa convoca a una reunión de 20 minutos. "
        "Escribe: (1) una frase asertiva que Daniela podría decir, (2) una agenda de 3 temas con minutos que sumen 20, (3) un acta con dos acuerdos que digan qué, quién y para cuándo.",
        "(1) «Cuando las cajas quedan sin ordenar, termino mi turno más tarde; ¿podemos revisar quién ordena cada pasillo?». (2) Tema 1: exponer los hechos, 8 minutos; tema 2: opciones, 7 minutos; tema 3: acuerdos, 5 minutos (total 20). (3) Acuerdo 1: Camilo ordenará el pasillo 3 a partir de mañana; acuerdo 2: la jefa revisará el reparto el viernes.",
        ["frase asertiva sin ataque", "agenda que suma 20", "acuerdos con qué, quién y cuándo"],
        ["hoja con la frase, la agenda y el acta"],
        ["agenda que no suma 20", "acuerdos sin responsable", "frase que ataca a la persona"],
        "Pregunta: «¿qué harías si Camilo no cumple el acuerdo?». Debe hablar de conversar y, si no cambia, informar a la jefa."),
    reinforce="Escribe una frase agresiva y conviértela en una asertiva sobre un problema de tu especialidad.",
    extend="Explica por qué una reunión sin acta puede terminar en un nuevo conflicto.",
)

# ============================================================ OAG-04, clase 4
F = ("Ficha 16 (seguimiento de acuerdos de un equipo de oficina de ejemplo, cuatro semanas). Semana 1: 5 acuerdos, 4 cumplidos. Semana 2: 5 acuerdos, 5 cumplidos. Semana 3: 10 acuerdos, 4 cumplidos. Semana 4: 5 acuerdos, 3 cumplidos. "
     "Criterio de ejemplo del equipo: una semana es buena si se cumplen al menos 80 de cada 100 acuerdos.")
build(
    G4, 4, F,
    use="Aprenderé a hacer seguimiento de los acuerdos de un equipo con datos, a dar retroalimentación respetuosa y a proponer mejoras sin culpar.",
    prior=["Sé hacer actas con acuerdos.", "Sé calcular cuántos por cada 100.", "Sé que informar con verdad ayuda al equipo."],
    explain=[
        "El seguimiento de acuerdos consiste en revisar cada cierto tiempo si lo acordado se cumplió. Se mide el cumplimiento: los acuerdos cumplidos multiplicados por 100 y divididos entre los acuerdos tomados dan cuántos de cada 100 se cumplieron. Se compara con un criterio del equipo, por ejemplo 80 de cada 100. Los acuerdos que no se cumplen no se esconden: se analiza por qué, con curiosidad y sin buscar culpables.",
        "Algunas causas frecuentes son acuerdos sin responsable o sin fecha, demasiados acuerdos al mismo tiempo, falta de recursos o poca comunicación. La mejora puede ser tomar menos acuerdos, escribir quién y para cuándo, y recordar los plazos a mitad de semana. La retroalimentación es la información que se da a otra persona sobre su desempeño: es mejor darla en privado, hablando de hechos, reconociendo lo que hizo bien y acordando cómo mejorar.",
        "Registrar con honestidad el cumplimiento permite aprender. Esconder los incumplidos solo posterga el problema." + LIM,
    ],
    vocab=[("seguimiento", "revisión periódica de si se cumple lo acordado"), ("cumplimiento", "cuántos acuerdos se cumplieron de los tomados, por cada 100"), ("retroalimentación", "información que se da a otra persona sobre su desempeño para ayudarla a mejorar"), ("responsable", "persona que se compromete a cumplir un acuerdo"), ("causa", "razón que explica por qué ocurrió algo")],
    worked=[
        ("Calcular el cumplimiento", "Un equipo de ejemplo tomó 20 acuerdos y cumplió 15. ¿Cuántos de cada 100 se cumplieron?", ["Se multiplica por 100 y se divide entre el total.", "15 × 100 ÷ 20 = 75."], "75 de cada 100"),
        ("Retroalimentación respetuosa", "Un compañero de ejemplo llegó tarde a una entrega. ¿Qué forma de decírselo es mejor: «Eres impuntual» o «La entrega llegó 20 minutos tarde; ¿cómo podemos evitarlo?»?", ["La mejor habla de un hecho y busca una solución.", "No ataca a la persona."], "La segunda forma"),
    ],
    mistakes=[("Descartar los acuerdos incumplidos del registro para que el equipo se vea mejor.", "Oculta los problemas y no permite mejorar.", "Registra todos los acuerdos y analiza por qué algunos no se cumplieron."),
              ("Dar retroalimentación frente a todo el equipo para «que aprenda».", "Humilla a la persona y suele provocar rechazo en lugar de mejora.", "Hazlo en privado, con hechos y propuesta de mejora.")],
    T=[
        ("abc", "En trabajo en equipo: ¿qué es hacer seguimiento de los acuerdos?", "Revisar si se cumplieron y qué hacer con los que no", "Cambiar los acuerdos cada semana", "Informar los acuerdos a otras empresas", "El seguimiento revisa el cumplimiento y busca soluciones a lo pendiente."),
        ("abc", "{F} ¿Qué semana cumplió todos sus acuerdos?", "La semana 2", "La semana 1", "La semana 4", "En la semana 2 hubo 5 acuerdos y 5 cumplidos."),
        ("=", "{F} ¿Cuántos acuerdos se tomaron en total en las cuatro semanas?", "5+5+10+5", "Se suman los acuerdos tomados en cada semana.", " acuerdos"),
        ("=", "{F} ¿Cuántos acuerdos se cumplieron en total en las cuatro semanas?", "4+5+4+3", "Se suman los acuerdos cumplidos de cada semana.", " acuerdos"),
        ("=", "{F} ¿Cuántos acuerdos de cada 100 se cumplieron en la semana 4?", "3*100//5", "Se multiplican los cumplidos por 100 y se divide entre los tomados.", " de cada 100"),
        ("abc", "{F} ¿Qué semanas cumplen el criterio de 80 de cada 100?", "Las semanas 1 y 2", "Las semanas 2 y 4", "Solo la semana 2", "La semana 1 cumple 80 de cada 100 y la 2 cumple 100; las otras no llegan."),
        ("=", "{F} ¿Cuántos acuerdos no se cumplieron la semana 3?", "10-4", "A los acuerdos tomados se les restan los cumplidos.", " acuerdos"),
        ("=", "{F} Considerando las cuatro semanas juntas, ¿cuántos acuerdos de cada 100 se cumplieron?", "16*100//25", "Se usa el total de cumplidos y el total de tomados de las cuatro semanas.", " de cada 100"),
        ("abc", "{F} La semana 3 tuvo 10 acuerdos, el doble que las demás. ¿Qué hipótesis es razonable?", "Se tomaron demasiados acuerdos para la capacidad del equipo", "El equipo perdió el interés en trabajar", "Los acuerdos siempre se escriben mal", "Más acuerdos con el mismo equipo aumentan el riesgo de no cumplirlos."),
        ("abc", "{F} Un compañero propone no registrar los acuerdos incumplidos para que el porcentaje se vea mejor. ¿Qué corresponde?", "Registrar todos y analizar por qué no se cumplieron", "Aceptar la propuesta porque mejora la imagen", "Borrar solo los de la semana 3", "Registrar la verdad permite detectar causas y mejorar el funcionamiento."),
        ("abc", "¿Cuál es la mejor forma de dar retroalimentación a un compañero que se atrasó?", "En privado, hablando de hechos, reconociendo lo bueno y acordando cómo mejorar", "Frente a todos, para que aprenda", "No decir nada para evitar un conflicto", "La retroalimentación respetuosa se centra en hechos y busca una mejora conjunta."),
        ("abc", "{F} ¿Qué acción de mejora es más adecuada para el equipo?", "Escribir quién y para cuándo en cada acuerdo y recordar los plazos a mitad de semana", "Dejar de tomar acuerdos", "Cambiar el criterio a 50 de cada 100", "Un acuerdo con responsable y fecha, y un recordatorio, aumenta la probabilidad de cumplimiento."),
        ("=", "{F} Para cumplir el criterio de 80 de cada 100 en una semana de 10 acuerdos, ¿cuántos acuerdos deben cumplirse como mínimo?", "10*80//100", "Se calcula el 80 de cada 100 aplicado a los 10 acuerdos.", " acuerdos"),
    ],
    ctx=("abc", "{F} En la semana 3, Karina cumplió 0 de 4 acuerdos que tenía asignados. ¿Qué hace la jefa del equipo?", "Conversa con ella en privado, revisa si tenía recursos y tiempo y acuerdan cómo apoyarla", "La reta delante de todos", "Le quita todos sus acuerdos sin conversar", "Conversar en privado y buscar causas permite ayudar y evita humillar."),
    sc=[
        ("En un equipo de ejemplo: ¿cómo se calcula el cumplimiento de acuerdos?", "Cumplidos por 100 dividido por tomados", "Eso da cuántos de cada 100 acuerdos se cumplieron."),
        ("¿Qué haces con un acuerdo que no se cumplió?", "Analizo por qué y propongo una solución", "Entender la causa evita que se repita."),
        ("¿Cómo das retroalimentación?", "En privado, con hechos y propuesta", "Así la persona puede mejorar sin sentirse humillada."),
    ],
    op=("Caso de ejemplo. El equipo de una librería ficticia registró sus acuerdos de 3 semanas: semana 1, 10 acuerdos y 8 cumplidos; semana 2, 5 acuerdos y 2 cumplidos; semana 3, 5 acuerdos y 4 cumplidos. Criterio de ejemplo: al menos 80 de cada 100. "
        "Escribe: (1) el cumplimiento de cada semana por cada 100, (2) qué semanas cumplen el criterio, (3) una causa posible de la semana 2, (4) una mejora, y (5) cómo darías retroalimentación a un compañero que no cumplió dos acuerdos.",
        "(1) Semana 1: 80; semana 2: 40; semana 3: 80. (2) Semanas 1 y 3. (3) Posible causa: los acuerdos no tenían fecha, o una persona tuvo ausencias. (4) Escribir quién y para cuándo y recordar los plazos. (5) «En privado: la entrega del lunes quedó pendiente; ¿qué te lo dificultó? ¿cómo te apoyamos?».",
        ["calcula bien el cumplimiento", "compara con el criterio", "propone una causa sin culpar", "propone una mejora", "da retroalimentación en privado y con hechos"],
        ["hoja con cinco respuestas"],
        ["no multiplicar por 100", "culpar a una persona", "retroalimentación pública"],
        "Pregunta: «¿qué pasaría si se juntaran las tres semanas?». Debe calcular 14 de 20, es decir 70 de cada 100, y notar que no llega a 80."),
    reinforce="Escribe tres acuerdos de un equipo con responsable y fecha y márcalos como cumplidos o no, con datos de ejemplo.",
    extend="Explica por qué tomar muchos acuerdos al mismo tiempo puede bajar el cumplimiento de un equipo.",
)

# ============================================================ OAG-05, clase 1
F = ("Ficha 17 (cuatro situaciones de ejemplo en empresas ficticias). Situación A: en una entrevista para un puesto de bodega, el entrevistador descarta a un postulante por su acento y por haber nacido en otro país, aunque su experiencia cumple lo pedido. "
     "Situación B: en una oficina se pregunta a una candidata si piensa tener hijos antes de decidir su contratación. Situación C: en una cocina no se invita a una cocinera de 58 años a una capacitación porque «ya está mayor». "
     "Situación D: en un taller, dos compañeros se burlan a diario del modo de caminar de otro, aunque él les ha pedido que paren.")
build(
    G5, 1, F,
    use="Aprenderé qué es discriminar, por qué es una falta de respeto en el trabajo y cómo se aplican criterios objetivos y trato digno.",
    prior=["Conozco el trabajo en equipo.", "Sé calcular restas de enteros.", "Sé que todas las personas merecen respeto."],
    explain=[
        "Discriminar es dar un trato desigual, excluir o humillar a una persona por una característica personal, sin una razón justificada. Algunas características son el origen o la nacionalidad, el sexo o el género, la edad, la discapacidad, la religión, la apariencia, la orientación sexual o la situación económica. En el trabajo, las decisiones deben basarse en criterios objetivos: experiencia, conocimientos, habilidades y cumplimiento de las funciones del cargo.",
        "Un estereotipo es una idea simplificada sobre un grupo de personas («los jóvenes no son responsables»). Los estereotipos llevan a prejuicios y a decisiones injustas. El trato digno incluye hablar con respeto, usar el nombre que la persona prefiere, no hacer burlas ni apodos que molesten y valorar su aporte. Una broma que humilla no es broma: importa el efecto sobre la persona.",
        "En Chile existen normas que protegen contra la discriminación laboral; para informarte puedes acudir a tu jefatura, al área de personas de la empresa o a la Dirección del Trabajo. Si presencias o sufres un trato discriminatorio, avisa a una persona adulta de confianza y a los canales de la empresa." + LIM,
    ],
    vocab=[("discriminar", "dar un trato desigual o excluir a una persona por una característica personal, sin razón justificada"), ("criterio objetivo", "razón relacionada con las funciones del cargo, como experiencia o conocimientos"), ("estereotipo", "idea simplificada sobre un grupo de personas"), ("prejuicio", "opinión negativa formada antes de conocer a la persona"), ("trato digno", "trato respetuoso que valora a la persona"), ("selección", "proceso en que una empresa elige a quién contratar")],
    worked=[
        ("Reconocer un criterio objetivo", "Una empresa de ejemplo busca un cocinero y evalúa: experiencia en cocina, conocimiento de higiene y puntualidad. ¿Son criterios objetivos?", ["Se relacionan con las funciones del cargo.", "Son criterios laborales."], "Sí, son criterios objetivos"),
        ("Postulantes que pasan", "Una empresa de ejemplo recibe 30 postulaciones y descarta 12 por no cumplir los requisitos del cargo. ¿Cuántas pasan a entrevista?", ["Se resta lo descartado al total.", "30 − 12 = 18."], "18 postulaciones"),
    ],
    mistakes=[("Decir «es solo una broma» cuando la persona pidió que pararan.", "Una burla que humilla es una falta de respeto aunque el que la hace no la vea así.", "Detén la burla apenas la persona lo pida y respeta su límite."),
              ("Descartar a un postulante por su apariencia o su origen y no por su experiencia.", "Es una decisión injusta basada en prejuicios y no en el cargo.", "Decide con criterios objetivos relacionados con las funciones.")],
    T=[
        ("abc", "En el mundo laboral: ¿qué es discriminar?", "Dar un trato desigual a una persona por una característica personal, sin razón justificada", "Elegir a la persona con más experiencia para un cargo", "Rechazar a quien no cumple los requisitos del puesto", "Discriminar se basa en una característica personal; los requisitos del cargo son criterios objetivos."),
        ("abc", "{F} ¿Qué característica personal usa como razón la situación A?", "El acento y el país de origen", "La experiencia", "La edad", "El entrevistador descarta al postulante por su acento y su origen, no por su experiencia."),
        ("abc", "{F} ¿En qué situación se usa la edad como razón?", "En la situación C", "En la situación A", "En la situación B", "La situación C deja fuera a la cocinera porque «ya está mayor»."),
        ("abc", "{F} ¿Por qué la pregunta de la situación B no es adecuada en una selección?", "Se refiere a un asunto personal que no se relaciona con las funciones del cargo", "Porque las entrevistas deben ser cortas", "Porque la candidata no tenía experiencia", "Una decisión de contratación debe basarse en aptitudes para el cargo, no en planes familiares."),
        ("abc", "¿Cuál es un criterio objetivo para elegir a una persona para un cargo de bodega?", "Su experiencia y sus conocimientos relacionados con las funciones", "El lugar donde nació", "Su apariencia al llegar a la entrevista", "Los criterios objetivos se relacionan con lo que se hace en el cargo."),
        ("abc", "{F} ¿Cómo se debe considerar la situación D?", "Como una falta de respeto que debe detenerse e informarse", "Como una broma normal entre compañeros", "Como un conflicto de opiniones sin importancia", "Si la persona pidió que pararan, seguir es una falta de respeto."),
        ("=", "Tres postulantes obtienen estos puntajes en tres criterios laborales (de 0 a 5). A: 4, 3 y 5. B: 5, 5 y 3. C: 4, 4 y 4. ¿Cuántos puntos de diferencia hay entre el mayor y el menor puntaje total?", "(5+5+3)-(4+3+5)", "Se suman los puntajes de cada postulante y se restan el mayor y el menor.", " punto"),
        ("abc", "Un jefe de ejemplo dice: «Prefiero hombres para este turno porque son más fuertes». ¿Qué es esa afirmación?", "Un estereotipo que no mide las capacidades de cada persona", "Un criterio técnico del cargo", "Una exigencia legal", "Atribuir una capacidad a todo un grupo es un estereotipo; la capacidad se evalúa en cada persona."),
        ("abc", "Un compañero nuevo ha pedido que le llamen por su nombre y no por un apodo. ¿Qué actitud corresponde?", "Llamarlo por su nombre", "Seguir con el apodo, porque es una costumbre del taller", "Llamarlo por su país de origen cada vez", "El trato digno incluye respetar cómo la persona pide que la llamen."),
        ("abc", "Una compañera dice: «Yo no discrimino, solo bromeo». ¿Qué respuesta es correcta?", "Lo importante es el efecto: si la persona se siente humillada, es una falta de respeto", "Si hay intención de reír, nunca es un problema", "Solo importa si lo escucha la jefatura", "El trato digno se mide por cómo afecta a la otra persona, no por la intención de quien bromea."),
        ("abc", "{F} Un trabajador ve la situación D y no dice nada para no meterse en problemas. ¿Qué puede hacer sin exponerse a riesgos?", "Apoyar al compañero, anotar lo que ve y avisar a la jefatura o al canal de la empresa", "Sumarse a las burlas", "Enfrentar a gritos a los compañeros", "Apoyar y avisar por los canales formales protege a la persona sin generar nuevas agresiones."),
        ("abc", "Una empresa de ejemplo contrata solo a menores de 30 años «por imagen». ¿Cuál es el problema?", "Excluye por edad sin relación con las funciones del cargo", "Ninguno: la empresa puede elegir libremente cualquier criterio", "Que los menores de 30 cuestan más", "La edad no mide la capacidad para las funciones, así que es un criterio discriminatorio."),
        ("=", "Una empresa de ejemplo recibió 45 postulaciones y descartó 18 por no cumplir los requisitos del cargo. ¿Cuántas pasan a entrevista?", "45-18", "Al total se le restan las descartadas por requisitos objetivos.", " postulaciones"),
    ],
    ctx=("abc", "{F} Una compañera nueva, de otro país, escucha que en el almuerzo se burlan de su acento. Ella se queda callada. ¿Qué puede hacer una persona que lo presencia?", "Acercarse a apoyarla y avisar a la jefatura o al canal de la empresa si continúa", "Reírse para integrarse al grupo", "Decirle que no se ofenda", "Apoyar a la persona afectada y usar los canales formales ayuda a detener la burla sin enfrentamientos y protege su dignidad."),
    sc=[
        ("En el trabajo: ¿qué es discriminar?", "Dar un trato desigual por una característica personal", "No se basa en las funciones del cargo."),
        ("¿En qué debe basarse la selección de personal?", "En criterios objetivos del cargo", "Así la decisión es justa y relacionada con el trabajo."),
        ("¿Qué haces si ves una burla repetida a un compañero?", "Lo apoyo y aviso por los canales de la empresa", "Callar permite que el maltrato continúe."),
    ],
    op=("Caso de ejemplo. Una cadena de panaderías ficticia busca un auxiliar de bodega. Se presentan tres personas: Rosa (45 años, 6 años de experiencia), Mateo (19 años, sin experiencia pero con curso de inventarios) y Ali (31 años, nacido en otro país, 3 años de experiencia). El jefe dice: «Prefiero a Mateo porque es joven». "
        "Escribe: (1) tres criterios objetivos para elegir, (2) por qué la frase del jefe no es un criterio objetivo, (3) una pregunta adecuada y una inadecuada para la entrevista, (4) a quién avisarías si el jefe insiste.",
        "(1) Experiencia en bodega, conocimiento de inventarios, disposición para el trabajo en equipo. (2) La edad no mide si la persona puede cumplir las funciones. (3) Adecuada: «¿Qué experiencia tiene en control de inventarios?»; inadecuada: «¿Cuántos años tiene realmente?». (4) A la jefatura superior, al área de personas o al canal de la empresa.",
        ["propone criterios objetivos", "explica por qué la edad no lo es", "distingue preguntas adecuadas e inadecuadas", "nombra un canal de aviso"],
        ["hoja con cuatro respuestas"],
        ["usar la edad como criterio", "no proponer un canal", "inventar datos de los candidatos"],
        "Pregunta: «¿qué harías si tú fueras el candidato descartado?». Debe expresar qué sentiría y cómo pediría las razones por los canales de la empresa."),
    reinforce="Escribe tres criterios objetivos para elegir a una persona para un cargo de tu especialidad.",
    extend="Explica con un ejemplo por qué un estereotipo puede llevar a una decisión injusta aunque nadie tenga mala intención.",
)

# ============================================================ OAG-05, clase 2
F = ("Ficha 18 (caso de ejemplo en una oficina ficticia, «Servicios Lago de Ejemplo»). Se contrató a Elena, usuaria de silla de ruedas, para atención de público. Hallazgos: 1) la entrada principal tiene 5 escalones y no hay rampa; "
     "2) el mesón de atención mide 110 cm de alto y no tiene un tramo bajo; 3) los avisos importantes se dan solo por altavoz; 4) los formularios se entregan solo en papel y con letra muy pequeña; "
     "5) un compañero dice: «pobrecita, mejor no le damos mucha responsabilidad». Medidas de ejemplo: cada escalón sube 18 cm.")
build(
    G5, 2, F,
    use="Aprenderé a incluir a las personas con discapacidad en el trabajo: reconocer barreras, aplicar ajustes razonables y usar un trato y un lenguaje respetuosos.",
    prior=["Sé qué es discriminar.", "Sé multiplicar y restar.", "Sé que todas las personas pueden aportar al trabajo."],
    explain=[
        "Una persona con discapacidad es una persona que, por una condición física, sensorial, intelectual o psíquica, encuentra barreras para participar en igualdad de condiciones. Las barreras pueden ser físicas (escalones sin rampa), comunicacionales (avisos que solo se dan por altavoz o por escrito en letra muy pequeña) y de actitud (prejuicios, como creer que no podrá hacer tareas importantes). La discapacidad no está solo en la persona: depende también de las barreras que pone el entorno.",
        "La accesibilidad universal busca que los espacios, servicios y herramientas puedan ser usados por todas las personas sin necesidad de adaptaciones especiales. Cuando eso no basta, se aplican ajustes razonables: cambios adecuados en el puesto o en la forma de trabajar que permiten cumplir las funciones en igualdad de condiciones, sin imponer una carga desmedida a la empresa. El trato es respetuoso: se usa la expresión «persona con discapacidad», se pregunta antes de ayudar («¿le puedo ayudar?»), se respeta la respuesta y no se decide por ella.",
        "La información médica es privada: nadie está obligado a contarla y el equipo no la difunde. En Chile existen normas sobre inclusión laboral de personas con discapacidad; para informarte consulta a tu jefatura o a la Dirección del Trabajo." + LIM,
    ],
    vocab=[("discapacidad", "condición de una persona que, junto con barreras del entorno, dificulta su participación en igualdad de condiciones"), ("barrera", "obstáculo físico, comunicacional o de actitud que impide la participación"), ("accesibilidad universal", "diseño que permite que todas las personas usen espacios y servicios"), ("ajuste razonable", "cambio adecuado que permite a una persona cumplir sus funciones en igualdad de condiciones"), ("inclusión", "participar y ser valorado en igualdad de condiciones"), ("información médica", "datos de salud, que son privados")],
    worked=[
        ("Clasificar una barrera", "En un taller de ejemplo, el manual de seguridad solo se entrega impreso y una trabajadora ciega no puede leerlo. ¿Qué tipo de barrera es?", ["Impide acceder a la información.", "Es una barrera comunicacional."], "Comunicacional"),
        ("Medir un desnivel", "Una puerta de ejemplo tiene 3 escalones de 15 cm cada uno. ¿Cuánto desnivel debe salvar una rampa?", ["Se multiplica la altura de un escalón por la cantidad.", "3 × 15 = 45."], "45 cm"),
    ],
    mistakes=[("Tomar del brazo a una persona con bastón para ayudarla sin preguntar.", "Se invade su espacio y se le quita autonomía; puede desequilibrarla.", "Pregunta si quiere ayuda y respeta su respuesta."),
              ("Pensar «la discapacidad es un problema de la persona» y no del entorno.", "Se olvidan las barreras que el entorno puede eliminar.", "Revisa qué barreras hay y cómo eliminarlas o ajustarlas.")],
    T=[
        ("abc", "En inclusión laboral: ¿qué es una barrera?", "Un obstáculo físico, comunicacional o de actitud que impide participar", "Una característica de la persona que no se puede cambiar", "Una regla de la empresa para el uso del baño", "Las barreras están en el entorno o en las actitudes y se pueden reducir."),
        ("abc", "{F} ¿Qué tipo de barrera es la falta de rampa en la entrada?", "Una barrera física", "Una barrera comunicacional", "Una barrera de actitud", "La rampa falta en la infraestructura, que es un obstáculo físico."),
        ("abc", "{F} ¿Qué tipo de barrera es dar los avisos importantes solo por altavoz?", "Una barrera comunicacional", "Una barrera física", "Una barrera de actitud", "El aviso solo auditivo no llega a quien no oye, y eso es comunicacional."),
        ("abc", "{F} ¿Qué hallazgo muestra una barrera de actitud?", "La frase «pobrecita, mejor no le damos mucha responsabilidad»", "Los 5 escalones sin rampa", "Los formularios con letra pequeña", "La frase supone, sin base, que Elena no podrá asumir responsabilidades."),
        ("abc", "¿Qué es un ajuste razonable?", "Un cambio adecuado que permite a la persona cumplir sus funciones en igualdad de condiciones", "Un beneficio sin relación con el trabajo", "Reducir las tareas sin acordarlo con la persona", "El ajuste razonable adapta el puesto o la forma de trabajar, con la participación de la persona."),
        ("abc", "¿Qué expresión es respetuosa para referirse a alguien?", "Una persona con discapacidad", "Un discapacitado", "Un enfermo", "La expresión centrada en la persona es la más respetuosa."),
        ("=", "{F} Se quiere construir una rampa para salvar los 5 escalones de la entrada. ¿Cuántos centímetros de altura debe salvar?", "5*18", "Se multiplica la altura de cada escalón por la cantidad de escalones.", " cm"),
        ("=", "{F} Un tramo accesible del mesón debe quedar 30 cm más bajo que el mesón actual (valor de ejemplo). ¿Cuántos centímetros debe medir ese tramo?", "110-30", "A la altura actual se le resta lo que debe bajar el tramo.", " cm"),
        ("abc", "{F} Para el problema de los avisos por altavoz, ¿qué ajuste razonable es adecuado?", "Entregar los avisos también por escrito o en una pantalla", "Subir el volumen del altavoz", "Pedir a Elena que pregunte a sus compañeros cada vez", "Dar el aviso por otro medio elimina la barrera, mientras que subir el volumen no sirve a quien no oye."),
        ("abc", "Un compañero ve a una persona con bastón dudando frente a una puerta. ¿Qué es lo más respetuoso?", "Ofrecer ayuda preguntando «¿le puedo ayudar?» y respetar su respuesta", "Tomarla del brazo para guiarla", "Ignorarla para no incomodar", "Preguntar y respetar la decisión mantiene la autonomía de la persona."),
        ("abc", "Elena prefiere no hablar de su salud en el trabajo. ¿Cómo debe manejar el equipo la información médica?", "No pedirla ni difundirla, salvo que ella decida compartirla o sea necesaria para un ajuste", "Pedirla a todos los compañeros para tener un registro", "Comentarla entre colegas para ayudarla mejor", "La información médica es privada y solo se comparte con permiso de la persona."),
        ("abc", "{F} Un jefe dice: «Ya la contratamos, ahora que se las arregle sola». ¿Qué observación es correcta?", "La inclusión exige además condiciones de accesibilidad, ajustes y trato respetuoso", "Tiene razón: la contratación basta", "Hay que reducirle las funciones para que no se canse", "Incluir no es solo contratar: es crear condiciones para que la persona trabaje en igualdad."),
        ("=", "{F} Adaptar la entrada cuesta $480.000, el mesón $150.000 y la señalización $90.000 (valores de ejemplo). ¿Cuánto cuestan los tres ajustes juntos?", "480000+150000+90000", "Se suman los costos de las tres adaptaciones.", " pesos"),
    ],
    ctx=("abc", "{F} Elena debe atender a una fila y el mesón actual le queda alto. Mientras se construye el tramo bajo, su jefa le pregunta qué le sirve. ¿Qué es lo adecuado?", "Escuchar a Elena y acordar un ajuste provisorio, como atender en una mesa a su altura", "Decidir por ella sin consultarla", "Dejarla sin atención hasta que se construya el tramo", "Los ajustes se acuerdan con la persona y se aplican sin esperar a la obra definitiva."),
    sc=[
        ("En inclusión laboral: ¿qué es la accesibilidad universal?", "Que todas las personas puedan usar espacios y servicios", "Evita barreras para todos y no solo para algunos."),
        ("¿Qué haces antes de ayudar a una persona con discapacidad?", "Le pregunto si quiere ayuda", "Así se respeta su autonomía y su decisión."),
        ("¿Se difunde la información médica de un compañero?", "No, es privada", "Solo la persona decide si la comparte."),
    ],
    op=("Caso de ejemplo. Una cafetería ficticia contrató a Joaquín, un joven sordo, como ayudante de caja. Los pedidos se avisan por el altavoz, los turnos se informan de palabra y el menú está solo en un cartel muy alto. El gerente dice: «No sé si podrá trabajar acá». "
        "Escribe: (1) tres barreras (indica si son físicas, comunicacionales o de actitud), (2) un ajuste razonable para cada una y (3) tres cosas que el equipo debe hacer para tratar a Joaquín con respeto.",
        "(1) Avisos por altavoz (comunicacional), turnos solo de palabra (comunicacional), menú alto (física), frase del gerente (de actitud). (2) Pantalla o aviso escrito; turnos por escrito o mensajería; menú impreso o a la altura de la vista. (3) Mirarlo de frente al hablar, preguntar cómo prefiere comunicarse, no hablar de su salud con otros.",
        ["identifica barreras y su tipo", "propone ajustes razonables", "describe un trato respetuoso"],
        ["hoja con una tabla de barrera, tipo y ajuste, y una lista de tres acciones"],
        ["no distinguir tipos de barrera", "decidir sin consultar a Joaquín", "difundir información médica"],
        "Pregunta: «¿qué harías si Joaquín dice que prefiere otro ajuste?». Debe responder que se acuerda con él y se respeta su preferencia."),
    reinforce="Escribe una barrera física, una comunicacional y una de actitud que podrías encontrar en tu liceo y un ajuste para cada una.",
    extend="Explica por qué preguntar antes de ayudar respeta mejor a una persona que ayudar sin preguntar.",
)

# ============================================================ OAG-05, clase 3
F = ("Ficha 19 (tres situaciones de ejemplo en empresas ficticias). Situación A: un jefe de local manda mensajes a una trabajadora de 17 años fuera del horario, pidiéndole salir con él, y cuando ella se niega le asigna los turnos más pesados. "
     "Situación B: dos compañeros esparcen rumores falsos sobre otro para que lo cambien de sección. Situación C: una supervisora corrige en privado un error de un trabajador, con respeto, y le explica cómo mejorar.")
build(
    G5, 3, F,
    use="Aprenderé a reconocer el acoso, el maltrato y el buen trato en el trabajo, y qué hacer si ocurren: registrar, avisar y buscar apoyo.",
    prior=["Sé qué es discriminar.", "Sé qué es un trato digno.", "Sé que debo avisar a una persona adulta de confianza ante un riesgo."],
    explain=[
        "El acoso laboral son conductas repetidas de maltrato, humillación o presión hacia una persona en el trabajo, que le causan daño. El acoso sexual son requerimientos de carácter sexual o personal no deseados, que amenazan o perjudican a quien los recibe. La violencia en el trabajo incluye gritos, amenazas, insultos o agresiones. En cambio, una corrección respetuosa de un error, hecha en privado y con hechos, no es acoso.",
        "Si te ocurre algo así, recuerda que no es tu culpa. No enfrentes solo a quien te maltrata. Anota los hechos (fecha, lugar, qué pasó, quién lo vio) y guarda sin borrar mensajes u otras pruebas. Cuéntalo cuanto antes a una persona adulta de confianza y usa los canales formales de la empresa, como la jefatura superior, el área de personas o el canal de denuncia. La Dirección del Trabajo puede orientar sobre qué hacer. Si eres menor de 18 años y estás en riesgo, avisa a una persona adulta responsable; el Fono Niños 147 también orienta.",
        "Si presencias una situación, apoya a la persona afectada, avisa por los canales formales y no difundas rumores. Informar de buena fe no es motivo de castigo." + LIM,
    ],
    vocab=[("acoso laboral", "conductas repetidas de maltrato o humillación hacia una persona en el trabajo"), ("acoso sexual", "requerimientos sexuales o personales no deseados que amenazan o perjudican"), ("maltrato", "trato que humilla, insulta o agrede a otra persona"), ("canal de denuncia", "vía formal de la empresa para informar una situación de maltrato"), ("evidencia", "mensaje, registro o testimonio que muestra lo ocurrido"), ("buen trato", "trato respetuoso que cuida la dignidad de las personas")],
    worked=[
        ("Reconocer un buen trato", "Un jefe de ejemplo le dice a un ayudante, en privado: «El informe llegó con dos errores; revisémoslos juntos». ¿Es acoso?", ["Es una corrección centrada en hechos.", "Se hace en privado y con respeto."], "No, es una corrección respetuosa"),
        ("Registrar los hechos", "Una trabajadora de ejemplo recibe 3 mensajes ofensivos por semana durante 4 semanas. ¿Cuántos mensajes debe tener registrados?", ["Se multiplican los mensajes por semana por las semanas.", "3 × 4 = 12."], "12 mensajes"),
    ],
    mistakes=[("Borrar los mensajes ofensivos para «no pensar en eso».", "Se pierde la evidencia que podría ayudar a que la situación se atienda.", "Guarda los mensajes y muéstralos a una persona adulta de confianza."),
              ("Enfrentar solo a la persona que acosa.", "Puede aumentar el riesgo y la presión sobre ti.", "Cuéntalo a una persona adulta de confianza y usa los canales formales.")],
    T=[
        ("abc", "En convivencia laboral: ¿qué es el acoso laboral?", "Conductas repetidas de maltrato o humillación hacia una persona en el trabajo", "Una corrección respetuosa de un error", "Un desacuerdo puntual sobre un turno", "El acoso es repetido y daña; una corrección respetuosa o un desacuerdo puntual no lo son."),
        ("abc", "{F} ¿Qué situación es una corrección laboral respetuosa?", "La situación C", "La situación A", "La situación B", "En la C la supervisora habla en privado, con respeto y propone una mejora."),
        ("abc", "{F} ¿Qué situación incluye peticiones personales no deseadas y un castigo cuando se rechazan?", "La situación A", "La situación B", "La situación C", "En la A el jefe presiona con turnos pesados a quien se niega."),
        ("abc", "{F} ¿Qué conducta se observa en la situación B?", "Esparcir rumores falsos para dañar a otra persona", "Una evaluación justa del desempeño", "Una reunión de equipo", "Los rumores falsos buscan dañar la imagen del compañero."),
        ("abc", "¿Qué debe recordar primero una persona que sufre acoso?", "Que no es su culpa y que puede pedir ayuda", "Que debe aguantar para no perder el trabajo", "Que debe vengarse de quien la acosa", "La culpa es de quien maltrata; pedir ayuda es la acción correcta."),
        ("abc", "Un trabajador de 17 años sufre una situación como la A. ¿Qué hace?", "Avisa a una persona adulta de confianza, anota los hechos y guarda las pruebas; el Fono Niños 147 también orienta", "Lo guarda en secreto para evitar problemas", "Enfrenta al jefe solo", "Una persona menor de edad debe contar con adultos de confianza y no guardar el secreto."),
        ("=", "{F} Una trabajadora anotó 2 mensajes por semana durante 6 semanas. ¿Cuántos mensajes registró en total?", "2*6", "Se multiplican los mensajes por semana por las semanas registradas.", " mensajes"),
        ("abc", "¿Qué conviene anotar para dar aviso de una situación de acoso?", "Fecha, lugar, qué ocurrió, quién lo vio y los mensajes guardados", "Solo cuánto me molestó", "Nada, para olvidarlo cuanto antes", "Los hechos concretos permiten investigar y proteger a la persona."),
        ("abc", "Si la persona que maltrata es la jefatura directa, ¿a quién se puede recurrir?", "A la jefatura superior, al área de personas o al canal de denuncia, y a la Dirección del Trabajo para orientarse", "Solo a los clientes", "A nadie, porque la jefatura decide todo", "Existen canales formales distintos de la jefatura directa para estos casos."),
        ("abc", "{F} Un compañero que supo de la situación B dice: «No es asunto mío». ¿Qué conviene hacer?", "Apoyar a la persona afectada y avisar por los canales formales, sin difundir el rumor", "Compartir el rumor para comprobarlo", "Esperar a que se resuelva solo", "Apoyar y avisar detiene el daño; difundir el rumor lo agrava."),
        ("abc", "Una trabajadora recibe un mensaje ofensivo. ¿Qué hace con la evidencia?", "La guarda sin borrarla y la muestra a una persona adulta de confianza o al canal formal", "La borra para evitar que otros la vean", "La publica en redes sociales", "La evidencia guardada permite que la situación se atienda sin exponer a la persona."),
        ("abc", "{F} Un gerente dice: «Corregir a gritos y delante de todos es disciplina». ¿Qué observación corresponde?", "Una corrección debe ser respetuosa y centrada en el hecho; humillar en público es maltrato", "Tiene razón: la disciplina exige firmeza pública", "Solo es maltrato si hay golpes", "Corregir puede hacerse sin humillar; los gritos públicos dañan la dignidad."),
        ("=", "Una empresa de ejemplo recibió 9 avisos de maltrato en un año y 6 ya fueron atendidos. ¿Cuántos quedan pendientes?", "9-6", "A los avisos recibidos se les restan los atendidos.", " avisos"),
    ],
    ctx=("abc", "{F} Una trabajadora de 18 años, que vio la situación A, le cuenta a una compañera que teme perder su turno si denuncia. ¿Qué le aconsejas?", "Que cuente lo que vio a una persona adulta de confianza o a un canal formal, y que guarde la evidencia que tenga", "Que se calle hasta que cambie el jefe", "Que enfrente al jefe en el pasillo", "Informar por canales formales protege a la afectada y respeta la confidencialidad."),
    sc=[
        ("En convivencia laboral: ¿qué distingue el acoso de una corrección respetuosa?", "El maltrato repetido y la humillación", "La corrección es puntual, privada y centrada en hechos."),
        ("¿Qué haces con un mensaje ofensivo que recibes?", "Lo guardo sin borrar", "Los mensajes guardados son evidencia de lo ocurrido."),
        ("¿A quién cuentas una situación de acoso?", "A una persona adulta de confianza y a un canal formal", "Así se activa la protección y no se queda solo."),
    ],
    op=("Caso de ejemplo. En un restaurante ficticio, el encargado grita todos los días a una ayudante nueva, la llama «inútil» delante de los clientes y le quita su colación cuando se equivoca. La ayudante, de 17 años, tiene miedo de perder el trabajo. "
        "Escribe: (1) por qué esto no es una corrección respetuosa, (2) cinco datos que anotarías, (3) a quién avisarías primero y a qué canal formal después, (4) una frase de apoyo que una compañera podría decirle.",
        "(1) Es repetido, humilla en público y castiga; una corrección sería privada, con hechos y con propuesta de mejora. (2) Fechas, lugar, qué dijo, quién lo escuchó, lo que le quitó. (3) A una persona adulta de confianza (por ejemplo, su madre, padre o profesora) y luego a la jefatura superior o al canal de denuncia; la Dirección del Trabajo orienta. (4) «No es tu culpa; yo te acompaño a contarlo».",
        ["explica por qué es maltrato", "propone datos útiles", "nombra una persona de confianza y un canal", "escribe una frase de apoyo"],
        ["hoja con cuatro respuestas"],
        ["sugerir enfrentar al encargado solo", "sugerir guardar el secreto", "culpar a la ayudante"],
        "Pregunta: «¿qué pasaría si la ayudante borra los mensajes?». Debe responder que perdería evidencia y que conviene guardarlos."),
    reinforce="Escribe tres frases de apoyo respetuosas para una compañera que sufre maltrato y tres acciones que no ayudan.",
    extend="Explica por qué un rumor falso puede ser una forma de acoso, aunque nadie grite.",
)

# ============================================================ OAG-05, clase 4
F = ("Ficha 20 (pauta de selección de ejemplo para un auxiliar de bodega, empresa ficticia). Criterios laborales, de 0 a 5 puntos cada uno: A) conocimiento de bodega; B) experiencia; C) disposición al trabajo en equipo; D) puntualidad según referencias. "
     "No se pueden usar como criterio: edad, sexo, origen, apariencia, estado civil, embarazo o intención de tenerlo, ni una discapacidad que no impida cumplir las funciones. "
     "Puntajes: Postulante 1: A 4, B 3, C 5, D 4. Postulante 2: A 5, B 4, C 3, D 4. Postulante 3: A 3, B 5, C 4, D 5. Ponderación es dar más valor a un criterio: aquí se prueba que A valga el doble.")
build(
    G5, 4, F,
    use="Aprenderé a aplicar criterios objetivos en una selección, a usar lenguaje inclusivo en un aviso y a decidir sin discriminar.",
    prior=["Conozco criterios objetivos y estereotipos.", "Sé sumar y comparar puntajes.", "Conozco barreras y ajustes razonables."],
    explain=[
        "Una selección justa usa una pauta con criterios relacionados con las funciones del cargo, como conocimientos, experiencia y actitud de trabajo en equipo. Cada criterio se puntúa y se suman los puntajes para comparar. La ponderación consiste en dar más peso a un criterio importante: por ejemplo, si el conocimiento vale el doble, su puntaje se multiplica por 2 antes de sumar.",
        "Quedan fuera de la selección las características personales sin relación con el cargo: edad, sexo, origen, apariencia, estado civil, embarazo o intención de tenerlo. Una discapacidad no se usa para descartar: se revisa si la persona puede cumplir las funciones con ajustes razonables. En un aviso de empleo se describen las funciones y requisitos, y se usa un lenguaje que no excluya, como «se busca persona para...».",
        "Las preguntas de la entrevista se centran en la experiencia y en cómo la persona enfrentaría tareas del cargo. Las decisiones se registran con sus razones, para poder explicarlas." + LIM,
    ],
    vocab=[("pauta de selección", "lista de criterios con puntajes para comparar a los postulantes"), ("ponderación", "dar más valor a un criterio importante"), ("lenguaje inclusivo", "forma de escribir que no excluye a ninguna persona"), ("aviso de empleo", "texto que describe un cargo y sus requisitos"), ("postulante", "persona que pide ser considerada para un cargo")],
    worked=[
        ("Puntaje total", "Un postulante de ejemplo obtiene 3, 4 y 5 puntos en tres criterios. ¿Cuál es su puntaje total?", ["Se suman los tres puntajes.", "3 + 4 + 5 = 12."], "12 puntos"),
        ("Ponderar un criterio", "En otro caso de ejemplo, el criterio A vale el doble. Un postulante obtiene A 2, B 3 y C 4. ¿Cuál es el total?", ["A se multiplica por 2: 2 × 2 = 4.", "Total: 4 + 3 + 4 = 11."], "11 puntos"),
    ],
    mistakes=[("Descartar a un postulante porque «se ve muy joven» o «muy mayor».", "La edad no mide si la persona puede cumplir las funciones.", "Evalúa con los criterios de la pauta y deja el registro de razones."),
              ("Escribir un aviso que pide «joven soltero, buena presencia».", "Excluye a personas por características que no se relacionan con el cargo.", "Describe las funciones y los requisitos del trabajo con lenguaje inclusivo.")],
    T=[
        ("abc", "{F} ¿Cuál es un criterio permitido en la pauta?", "La experiencia", "La edad", "El estado civil", "La pauta incluye la experiencia como criterio laboral; la edad y el estado civil están prohibidos."),
        ("abc", "{F} ¿Cuál de estos NO puede usarse como criterio de selección?", "El origen del postulante", "La puntualidad según referencias", "La disposición al trabajo en equipo", "El origen es una característica personal que no mide las funciones del cargo."),
        ("=", "{F} ¿Cuántos puntos suma el postulante 1 sin ponderar?", "4+3+5+4", "Se suman los puntajes de los cuatro criterios.", " puntos"),
        ("=", "{F} ¿Cuántos puntos suma el postulante 3 sin ponderar?", "3+5+4+5", "Se suman los puntajes de los cuatro criterios.", " puntos"),
        ("abc", "{F} Sin ponderar, ¿qué postulante obtiene el mayor puntaje?", "El postulante 3", "El postulante 1", "El postulante 2", "Los totales son 16, 16 y 17; el mayor es el del postulante 3."),
        ("abc", "¿Qué pregunta es adecuada en una entrevista para un cargo de bodega?", "«¿Qué experiencia tiene en control de inventarios?»", "«¿Piensa tener hijos pronto?»", "«¿De qué país es su familia?»", "La pregunta adecuada se relaciona con las funciones del cargo."),
        ("=", "{F} Si el criterio A valiera el doble, ¿cuántos puntos sumaría el postulante 2?", "5*2+4+3+4", "Se multiplica por 2 el puntaje de A y se suman los demás.", " puntos"),
        ("=", "{F} El puntaje máximo posible es 5 puntos por 4 criterios. ¿Cuántos puntos le faltan al postulante 3 para el máximo?", "5*4-(3+5+4+5)", "Se resta el puntaje obtenido al puntaje máximo posible.", " puntos"),
        ("abc", "{F} El jefe quiere elegir al postulante 2 porque «se ve más joven». ¿Qué corresponde?", "Decidir según los puntajes de la pauta, no según la apariencia", "Aceptar, porque el jefe tiene la última palabra", "Elegir al más joven si hay empate", "La apariencia no es un criterio permitido; se decide con la pauta."),
        ("abc", "{F} El postulante 1 cuenta que tiene una discapacidad física. ¿Qué corresponde?", "Revisar si puede cumplir las funciones con ajustes razonables y no descartarlo por ello", "Descartarlo para evitar complicaciones", "Pedirle un certificado médico completo a todos los postulantes", "La discapacidad no es un criterio de descarte; se evalúan funciones y posibles ajustes."),
        ("abc", "¿Qué aviso de empleo usa un lenguaje inclusivo y centrado en las funciones?", "«Se busca persona para auxiliar de bodega, con experiencia en inventarios»", "«Se busca joven soltero para auxiliar de bodega»", "«Se busca varón fuerte de buena presencia»", "El aviso inclusivo describe el cargo y sus requisitos sin excluir por características personales."),
        ("abc", "El aviso original dice «Se busca joven soltera, buena presencia». ¿Qué cambio de fondo corresponde?", "Reemplazar esas características por las funciones y requisitos del cargo", "Cambiar «soltera» por «soltero»", "Agregar la edad máxima exacta", "El cambio de fondo es quitar los criterios personales y describir lo que el cargo exige."),
        ("abc", "Una empresa registra sus decisiones de selección con la pauta y las razones. ¿Para qué sirve ese registro?", "Para poder explicar y revisar que la decisión fue justa", "Para decidir sin tener que justificar", "Para comparar la apariencia de los postulantes", "Una decisión registrada y razonada puede revisarse y explicarse a la persona."),
    ],
    ctx=("abc", "{F} Un postulante descartado pide saber por qué no fue elegido. ¿Qué respuesta es adecuada?", "Explicar con respeto sus puntajes en los criterios de la pauta y qué podría reforzar", "Decir que «no daba el perfil» sin más", "Decir que el jefe decide y no tiene que explicar", "Una explicación basada en la pauta es respetuosa y útil para el postulante."),
    sc=[
        ("En una selección de ejemplo: ¿qué es la ponderación?", "Dar más valor a un criterio importante", "Permite que lo más relevante pese más en el total."),
        ("¿Se descarta a alguien por una discapacidad?", "No; se revisan las funciones y los ajustes razonables", "La discapacidad no mide la capacidad de cumplir el cargo."),
        ("¿Qué describe un aviso inclusivo?", "Las funciones y los requisitos del cargo", "Así no se excluye por características personales."),
    ],
    op=("Caso de ejemplo. Una escuela de oficios ficticia busca un auxiliar administrativo. Pauta (de 0 a 5): A) manejo de documentos; B) experiencia; C) atención de público; D) trabajo en equipo. Puntajes: Ana (A 5, B 3, C 4, D 4), Bruno (A 3, B 5, C 4, D 5) y Carlos (A 4, B 4, C 5, D 3). "
        "Escribe: (1) el puntaje total de cada persona, (2) los puntajes totales de cada persona si C valiera el doble y si hay empate, (3) un aviso inclusivo de dos líneas para este cargo, (4) una pregunta adecuada y una inadecuada para la entrevista.",
        "(1) Ana: 16; Bruno: 17; Carlos: 16. (2) Con C doble: Ana 5+3+8+4 = 20; Bruno 3+5+8+5 = 21; Carlos 4+4+10+3 = 21; hay empate entre Bruno y Carlos. (3) «Se busca persona para auxiliar administrativo, con experiencia en manejo de documentos y atención de público». (4) Adecuada: «¿Cómo ordena un archivo de documentos?»; inadecuada: «¿Qué edad tiene?».",
        ["suma bien los puntajes", "aplica la ponderación", "redacta un aviso inclusivo", "distingue preguntas"],
        ["hoja con cuatro respuestas"],
        ["usar criterios personales", "no ponderar bien", "aviso con características personales"],
        "Pregunta: «¿cómo desempatarías entre Bruno y Carlos?». Debe proponer otro criterio laboral objetivo, como una prueba de la función, y no la edad ni la apariencia."),
    reinforce="Escribe una pauta de cuatro criterios para un cargo de tu especialidad y dos preguntas de entrevista adecuadas.",
    extend="Explica por qué registrar las razones de una selección ayuda a que sea más justa.",
)

# ============================================================ OAG-06, clase 1
F = ("Ficha 21 (extracto de contrato de trabajo de ejemplo; empresa y persona inventadas). Empleador: «Ferretería El Roble de Ejemplo». Trabajador: Luis Pérez (nombre de ejemplo). Cargo y funciones: auxiliar de bodega; recibe, ordena y entrega mercadería. "
     "Lugar de trabajo: sucursal Centro. Jornada (de ejemplo): de lunes a viernes, de 08:30 a 16:30, con 1 hora de colación. Remuneración: sueldo base mensual de $500.000 (monto de ejemplo), pagadero el último día hábil de cada mes. Duración: indefinida. Inicio: 3 de marzo (fecha de ejemplo).")
build(
    G6, 1, F,
    use="Aprenderé qué es una relación laboral, qué elementos tiene un contrato de trabajo y dónde informarme sobre mis derechos y deberes laborales.",
    prior=["Sé leer un documento con cláusulas.", "Sé multiplicar y calcular horas.", "Sé que debo leer antes de firmar."],
    explain=[
        "Hay una relación laboral cuando una persona presta servicios personales a otra, bajo su dirección, a cambio de una remuneración. Esa relación se formaliza en un contrato de trabajo escrito. Un contrato incluye, entre otros datos: quiénes son el empleador y el trabajador, el cargo y las funciones, el lugar, la jornada, la remuneración y su forma de pago, la duración y la fecha de inicio. Lo que no está claro en el contrato conviene aclararlo por escrito.",
        "Las normas generales sobre el trabajo en Chile están en el Código del Trabajo y en otras normas vigentes. La Dirección del Trabajo es la institución que orienta sobre ellas y fiscaliza su cumplimiento. Los derechos y los deberes del trabajador y del empleador se derivan del contrato y de esa norma. Las personas menores de 18 años tienen normas especiales; si quieres trabajar siendo menor, consúltalas con una persona adulta responsable y con la Dirección del Trabajo.",
        "Este cuaderno no entrega cifras legales como horas, plazos o porcentajes: esas cifras dependen de la norma vigente. Los montos y horarios de las fichas son de ejemplo. Si tienes un problema laboral real, consulta a las fuentes oficiales o a un profesional." + LIM,
    ],
    vocab=[("relación laboral", "vínculo en que una persona presta servicios a otra, bajo su dirección, a cambio de pago"), ("empleador", "persona o empresa que contrata y paga el trabajo"), ("trabajador", "persona que presta sus servicios a cambio de una remuneración"), ("contrato de trabajo", "acuerdo escrito que fija las condiciones del trabajo"), ("remuneración", "pago que recibe el trabajador por su trabajo"), ("Dirección del Trabajo", "institución que orienta y fiscaliza el cumplimiento de las normas laborales")],
    worked=[
        ("Identificar una cláusula", "Un contrato de ejemplo dice: «Lugar de trabajo: sucursal Norte». ¿Qué elemento del contrato es?", ["Indica dónde se trabaja.", "Es el lugar de trabajo."], "El lugar de trabajo"),
        ("Pago en varios meses", "Una remuneración de ejemplo es de $400.000 al mes. ¿Cuánto se recibe en 2 meses, sin descuentos?", ["Se multiplica por los meses.", "400.000 × 2 = 800.000."], "$800.000"),
    ],
    mistakes=[("Firmar un contrato sin leerlo porque «el jefe es de confianza».", "No se sabe qué condiciones se aceptan y después es más difícil aclararlas.", "Léelo completo, pregunta lo que no entiendas y guarda tu copia firmada."),
              ("Aceptar las condiciones solo de palabra: «ya veremos después».", "Lo que no está por escrito es difícil de probar y puede interpretarse distinto.", "Pide que las condiciones queden escritas antes de comenzar.")],
    T=[
        ("abc", "En relaciones laborales: ¿qué es un contrato de trabajo?", "Un acuerdo escrito entre empleador y trabajador que fija las condiciones del trabajo", "Un permiso de la jefatura para faltar un día", "Un reglamento del curso para aprobar la práctica", "El contrato de trabajo fija las condiciones acordadas; los otros documentos tienen fines distintos."),
        ("abc", "{F} ¿Quién es el empleador en este contrato?", "«Ferretería El Roble de Ejemplo»", "Luis Pérez", "La sucursal Centro", "El empleador es la empresa que contrata; Luis es el trabajador y la sucursal es el lugar."),
        ("abc", "{F} ¿Qué dato del contrato indica lo que hará Luis?", "El cargo y las funciones", "El lugar de trabajo", "La duración", "Las funciones describen las tareas: recibir, ordenar y entregar mercadería."),
        ("abc", "{F} ¿Qué duración tiene el contrato de ejemplo?", "Indefinida", "Hasta fin de año", "Solo por una obra", "La duración está escrita en el contrato como indefinida."),
        ("abc", "¿Qué institución orienta y fiscaliza el cumplimiento de las normas laborales en Chile?", "La Dirección del Trabajo", "El Servicio de Impuestos Internos", "El Registro Civil", "La Dirección del Trabajo es la institución a cargo de orientar sobre las normas laborales."),
        ("abc", "¿Dónde están las normas generales sobre el trabajo en Chile?", "En el Código del Trabajo y en otras normas vigentes", "Solo en lo que dice cada jefatura", "En los reglamentos de los liceos", "Las normas generales están en la ley, no en la opinión de cada jefatura."),
        ("=", "{F} Si el sueldo base de ejemplo se paga durante 3 meses, ¿cuánto se recibe en total, sin descuentos?", "500000*3", "Se multiplica el sueldo mensual por el número de meses.", " pesos"),
        ("abc", "Luis firma el contrato sin leerlo porque «confía en su jefe». ¿Qué problema tiene?", "No sabe qué condiciones acepta y no tiene claro qué puede pedir después", "Ninguno, porque el contrato nunca cambia nada", "Que el contrato queda sin validez", "Leer el contrato es la única forma de saber lo que se acepta."),
        ("abc", "{F} Después de firmar, ¿qué conviene hacer con la copia del contrato?", "Guardarla y tenerla a mano para consultar las condiciones", "Entregarla a un compañero", "Romperla, porque el original está en la empresa", "La copia sirve como respaldo si hay dudas sobre lo acordado."),
        ("abc", "Un empleador dice a un trabajador nuevo: «Las condiciones las vemos después, tú empieza». ¿Qué conviene?", "Pedir que las condiciones queden por escrito antes de comenzar", "Comenzar sin preguntar", "Aceptar de palabra y no decir más", "Lo acordado por escrito evita malentendidos futuros."),
        ("abc", "Una estudiante de 17 años quiere trabajar en vacaciones. ¿Qué hace?", "Consultar las normas especiales para menores con una persona adulta responsable y con la Dirección del Trabajo", "Trabajar sin avisar a nadie", "Decir que tiene 18 años", "Las personas menores tienen normas especiales que se deben conocer antes de trabajar."),
        ("abc", "{F} El jefe pide a Luis quedarse una hora más sin hablar de pago. ¿Cuál es el mejor primer paso?", "Preguntar con respeto cómo se regula eso según su contrato y la norma vigente", "Aceptar sin preguntar", "Negarse a gritos", "Preguntar con respeto y revisar el contrato es el primer paso."),
        ("=", "{F} Con la jornada de ejemplo, ¿cuántas horas de trabajo efectivo hay a la semana, descontando 1 hora diaria de colación?", "((16*60+30)-(8*60+30)-60)*5//60", "Se calculan las horas del día, se descuenta la colación y se multiplica por cinco días.", " horas"),
    ],
    ctx=("abc", "{F} Luis duda si la cláusula de la jornada permite cambios de horario sin aviso. ¿Qué hace?", "Lee la cláusula, pregunta por escrito a la empresa y, si persiste la duda, consulta a la Dirección del Trabajo", "Pide consejo a un desconocido en internet", "Acepta cualquier cambio para no tener problemas", "Revisar el contrato y consultar fuentes oficiales es el camino seguro."),
    sc=[
        ("En derechos laborales: ¿qué fija el contrato de trabajo?", "Las condiciones del trabajo", "Es el acuerdo escrito entre las dos partes."),
        ("¿Qué institución orienta sobre las normas laborales?", "La Dirección del Trabajo", "Su función es orientar y fiscalizar el cumplimiento."),
        ("¿Qué haces antes de firmar un contrato?", "Lo leo completo y pregunto mis dudas", "Firmar sin leer es aceptar condiciones desconocidas."),
    ],
    op=("Caso de ejemplo. Una joven llamada Daniela, de 18 años, recibe una oferta de la panadería ficticia «Pan del Valle de Ejemplo». El contrato dice: cargo, vendedora; lugar, local Centro; remuneración, $450.000 mensuales (monto de ejemplo); jornada, la que se acuerde después; duración, no se indica. "
        "Escribe: (1) qué elementos del contrato están claros, (2) cuáles están incompletos, (3) tres preguntas que harías por escrito, (4) dónde buscarías información oficial.",
        "(1) Cargo, lugar y remuneración. (2) La jornada y la duración. (3) «¿Cuál será mi horario?», «¿El contrato es indefinido o por plazo?», «¿Cuándo se paga el sueldo?». (4) El Código del Trabajo vigente y las orientaciones de la Dirección del Trabajo.",
        ["distingue lo claro de lo incompleto", "formula preguntas pertinentes", "nombra fuentes oficiales"],
        ["hoja con cuatro respuestas"],
        ["firmar sin aclarar", "inventar cifras legales", "buscar consejo en fuentes no oficiales"],
        "Pregunta: «¿qué harías si te piden firmar hoy mismo?». Debe responder que pedirá tiempo para leer y consultar."),
    reinforce="Elige un oficio de tu especialidad y escribe las seis partes que debería tener su contrato de trabajo.",
    extend="Explica por qué los acuerdos verbales son más difíciles de probar que los escritos.",
)

# ============================================================ OAG-06, clase 2
F = ("Ficha 22 (liquidación de sueldo de ejemplo; todos los montos son inventados). Haberes: sueldo base $520.000; bono de movilización $40.000; bono por meta $60.000. "
     "Descuentos: previsión (ahorro destinado a la pensión) $54.000; salud $36.000; anticipo de sueldo ya entregado $100.000. Sueldo líquido = total de haberes menos total de descuentos. "
     "Los montos y porcentajes de los descuentos obligatorios los fija la norma vigente; aquí son solo cifras de ejemplo.")
build(
    G6, 2, F,
    use="Aprenderé a leer una liquidación de sueldo: haberes, descuentos y sueldo líquido, y a comprobar que coincida con lo acordado.",
    prior=["Conozco el contrato de trabajo.", "Sé sumar y restar cifras grandes.", "Sé qué es una remuneración."],
    explain=[
        "La remuneración se explica en un documento llamado liquidación de sueldo. Allí se anotan los haberes, que son los montos que se suman (sueldo base, bonos u otros pagos), y los descuentos, que son los montos que se restan. El total de haberes menos el total de descuentos da el sueldo líquido, que es lo que la persona recibe. Los descuentos pueden ser obligatorios según la norma vigente (por ejemplo, para previsión y salud) o acordados (como un anticipo de sueldo ya entregado).",
        "La previsión es el ahorro que se destina a la pensión de la persona cuando deje de trabajar; la salud se destina a la cobertura de atenciones de salud. Los porcentajes y montos de estos descuentos los fija la norma vigente y puedes consultarlos en fuentes oficiales; en este cuaderno solo se usan cifras de ejemplo.",
        "Conviene revisar cada liquidación y comparar los haberes con lo escrito en el contrato. Si algo no coincide, se pregunta por escrito a quien corresponda. Guarda tus liquidaciones: son un respaldo de lo que has recibido." + LIM,
    ],
    vocab=[("liquidación de sueldo", "documento que detalla cómo se calcula el pago de un mes"), ("haber", "monto que se suma a la remuneración"), ("descuento", "monto que se resta de los haberes"), ("sueldo líquido", "monto que la persona recibe después de los descuentos"), ("anticipo", "dinero que se paga antes de la fecha de pago y luego se descuenta"), ("previsión", "ahorro destinado a la pensión de la persona")],
    worked=[
        ("Calcular haberes", "En una liquidación de ejemplo, el sueldo base es $400.000 y hay un bono de $30.000. ¿Cuál es el total de haberes?", ["Se suman los haberes.", "400.000 + 30.000 = 430.000."], "$430.000"),
        ("Calcular el líquido", "En otro ejemplo hay haberes por $450.000 y descuentos por $90.000. ¿Cuál es el sueldo líquido?", ["Líquido = haberes − descuentos.", "450.000 − 90.000 = 360.000."], "$360.000"),
    ],
    mistakes=[("Fijarse solo en el sueldo líquido y no revisar el detalle.", "Un haber que falta o un descuento incorrecto pasa inadvertido.", "Revisa cada haber y cada descuento y compáralos con lo acordado."),
              ("Perder las liquidaciones «porque ya se pagó».", "Son un respaldo si después hay dudas sobre el pago.", "Guárdalas, en papel o digitalmente.")],
    T=[
        ("abc", "En remuneraciones: ¿qué son los haberes?", "Los montos que se suman a la remuneración", "Los montos que se restan", "Los gastos de la empresa", "Los haberes son lo que se suma; lo que se resta son los descuentos."),
        ("abc", "{F} ¿Cuál de estos es un descuento?", "El anticipo de sueldo ya entregado", "El bono por meta", "El sueldo base", "El anticipo ya recibido se resta del pago del mes."),
        ("abc", "{F} ¿Cuál de estos es un haber?", "El bono de movilización", "La salud", "La previsión", "El bono se suma a la remuneración; salud y previsión son descuentos."),
        ("=", "{F} ¿Cuál es el total de haberes?", "520000+40000+60000", "Se suman el sueldo base y los dos bonos.", " pesos"),
        ("=", "{F} ¿Cuál es el total de descuentos?", "54000+36000+100000", "Se suman previsión, salud y anticipo.", " pesos"),
        ("=", "{F} ¿Cuál es el sueldo líquido?", "(520000+40000+60000)-(54000+36000+100000)", "Se restan los descuentos al total de haberes.", " pesos"),
        ("abc", "¿Quién fija los montos y porcentajes de los descuentos obligatorios, como previsión y salud?", "La norma vigente", "Cada jefatura según su criterio", "El trabajador cuando lo desea", "Los descuentos obligatorios están regulados por norma, no por la voluntad de cada empresa."),
        ("=", "{F} Si el anticipo no se hubiera entregado, ¿cuál sería el sueldo líquido, manteniendo los demás montos?", "(520000+40000+60000)-(54000+36000)", "Se calcula el total de haberes y se restan solo previsión y salud.", " pesos"),
        ("abc", "Un trabajador nota que su liquidación no incluye un bono acordado por escrito. ¿Qué hace?", "Pide una aclaración por escrito al área correspondiente, adjuntando el documento del bono", "Se calla para no molestar", "Se cobra por su cuenta de otra forma", "Lo adecuado es pedir la aclaración por escrito con la evidencia del acuerdo."),
        ("abc", "{F} Una compañera dice: «Solo importa el sueldo líquido; el detalle no sirve». ¿Qué respuesta es correcta?", "El detalle permite comprobar que haberes y descuentos son los acordados y los que corresponden", "Tiene razón, el detalle es innecesario", "El detalle sirve solo a la empresa", "Sin revisar el detalle no se detectan errores de haberes ni de descuentos."),
        ("abc", "¿Para qué sirve el ahorro descontado por previsión?", "Para formar un ahorro destinado a la pensión de la persona", "Para pagar los gastos de la empresa", "Para premiar la asistencia del mes", "La previsión se destina a la pensión de la propia persona."),
        ("abc", "El contrato dice sueldo base de $520.000 y la liquidación indica $502.000. ¿Qué hace el trabajador?", "Consulta por escrito, adjuntando el contrato, para aclarar la diferencia", "Supone que fue un aumento de sueldo y no pregunta", "Cobra la diferencia por su cuenta", "Una diferencia entre contrato y liquidación se aclara por escrito con el respaldo del contrato, sin suponer la causa."),
        ("=", "{F} Supón que un mes no se cumple la meta y el anticipo es de $80.000 en vez de $100.000; los demás montos no cambian. ¿Cuál sería el sueldo líquido?", "(520000+40000)-(54000+36000+80000)", "Se calcula el total de haberes sin el bono por meta y se restan los nuevos descuentos.", " pesos"),
    ],
    ctx=("abc", "{F} Al recibir su liquidación, Sofía ve que el bono de movilización es de $30.000 y no de $40.000, como dice su contrato de ejemplo. ¿Qué hace?", "Revisa su contrato y pide por escrito una aclaración al área de personas", "Reclama a gritos delante de sus compañeros", "No dice nada y espera el próximo mes", "Una consulta por escrito, con el contrato a la vista, permite corregir un posible error."),
    sc=[
        ("En una liquidación de ejemplo: ¿cómo se calcula el sueldo líquido?", "Haberes menos descuentos", "El líquido es lo que queda después de restar los descuentos."),
        ("¿Qué son los descuentos obligatorios?", "Montos que fija la norma vigente", "No dependen de la voluntad de cada jefe."),
        ("¿Qué haces si un haber no coincide con tu contrato?", "Pido una aclaración por escrito", "Así queda constancia y se puede corregir."),
    ],
    op=("Caso de ejemplo. Liquidación de ejemplo de Marcos, auxiliar de aseo de una empresa ficticia. Haberes: sueldo base $480.000; bono de asistencia $20.000. Descuentos: previsión $48.000; salud $34.000; anticipo $60.000. Su contrato (de ejemplo) dice: sueldo base $480.000, bono de asistencia $30.000. "
        "Escribe: (1) el total de haberes, (2) el total de descuentos, (3) el sueldo líquido, (4) la diferencia con el contrato, (5) cómo pedirías la aclaración.",
        "(1) 480.000 + 20.000 = 500.000. (2) 48.000 + 34.000 + 60.000 = 142.000. (3) 500.000 − 142.000 = 358.000. (4) El bono de asistencia es $10.000 menor que lo del contrato. (5) «Estimada encargada: según mi contrato mi bono de asistencia es de $30.000 y en la liquidación aparece $20.000. ¿Pueden revisarlo? Adjunto mi contrato».",
        ["calcula haberes, descuentos y líquido", "detecta la diferencia", "redacta una consulta respetuosa y por escrito"],
        ["hoja con cinco respuestas"],
        ["restar mal los descuentos", "no detectar la diferencia", "reclamar sin respaldo"],
        "Pregunta: «¿qué harías si la empresa dice que fue un error?». Debe pedir que se corrija y que quede por escrito."),
    reinforce="Inventa una liquidación con tres haberes y tres descuentos y calcula el sueldo líquido.",
    extend="Explica por qué guardar las liquidaciones sirve como respaldo.",
)

# ============================================================ OAG-06, clase 3
F = ("Ficha 23 (cuatro situaciones de ejemplo; personas y empresas inventadas). A: Valentina, auxiliar en un centro de salud ficticio, comenta en una red social el caso de una paciente, mencionando su calle y su enfermedad. "
     "B: Pedro llega 25 minutos tarde, 4 días a la semana, sin avisar, y sus compañeros cubren su puesto. C: Rosario pide a su empleador una copia de su contrato firmado y se la niegan «por tanto trámite». "
     "D: Camilo recibe del jefe la orden de operar una máquina nueva para la que nadie lo ha capacitado.")
build(
    G6, 3, F,
    use="Aprenderé a distinguir deberes y derechos generales del trabajador en situaciones laborales y a saber a quién consultar.",
    prior=["Conozco el contrato de trabajo.", "Sé qué es la confidencialidad.", "Sé que la seguridad es parte del trabajo."],
    explain=[
        "Los deberes de un trabajador son las obligaciones que asume al firmar su contrato. Entre los generales están cumplir sus funciones y las instrucciones razonables, llegar a su hora y avisar si no puede, cuidar los bienes de la empresa, respetar a compañeros y clientes, seguir las normas de seguridad y guardar la confidencialidad: no divulgar información reservada de la empresa ni datos personales de clientes, pacientes o compañeros.",
        "Los derechos generales son las protecciones que la norma vigente reconoce al trabajador. Entre ellos están conocer las condiciones de su trabajo por escrito, recibir la remuneración acordada, ser tratado con dignidad y sin discriminación, trabajar en condiciones seguras, ser informado de los riesgos de su tarea y recibir capacitación para realizarla, y organizarse con otros trabajadores. Los descansos, las vacaciones y otros beneficios se rigen por la norma vigente: consúltalos en fuentes oficiales y no confíes en cifras de memoria.",
        "Derechos y deberes van juntos: cumplir los deberes protege el trabajo del equipo, y reclamar los derechos con respeto protege a la persona. Ante dudas, consulta a tu jefatura, al área de personas o a la Dirección del Trabajo." + LIM,
    ],
    vocab=[("deber", "obligación que el trabajador asume al aceptar un trabajo"), ("derecho", "protección que la norma vigente reconoce al trabajador"), ("confidencialidad", "obligación de no divulgar información reservada o datos personales"), ("puntualidad", "llegar a la hora acordada"), ("capacitación", "formación que se entrega para poder realizar una tarea de forma segura"), ("organizarse", "reunirse con otros trabajadores para defender sus intereses")],
    worked=[
        ("Identificar un deber", "Un auxiliar de ejemplo cuenta en redes los datos de un cliente de la tienda. ¿Qué deber incumple?", ["Divulga datos personales que debe proteger.", "Es el deber de confidencialidad."], "Confidencialidad"),
        ("Minutos acumulados", "Una trabajadora de ejemplo llega 10 minutos tarde 3 veces por semana. ¿Cuántos minutos de atraso acumula en 2 semanas?", ["Minutos por semana: 10 × 3 = 30.", "En 2 semanas: 30 × 2 = 60."], "60 minutos"),
    ],
    mistakes=[("Decir «tengo derechos, no tengo deberes».", "Los derechos y los deberes van juntos; no cumplir los deberes perjudica al equipo.", "Cumple tus deberes y reclama tus derechos con respeto."),
              ("Aceptar operar una máquina sin capacitación «para no quedar mal».", "Es riesgoso para ti y para otros, y no se debe hacer sin formación y autorización.", "Informa que no estás capacitado y pide capacitación antes de operarla.")],
    T=[
        ("abc", "En deberes laborales: ¿qué es la confidencialidad?", "No divulgar información reservada ni datos personales", "Hablar con todos los clientes de los temas de la empresa", "Contar a los compañeros lo que se sabe de un cliente", "La confidencialidad protege los datos reservados y personales."),
        ("abc", "{F} ¿Qué deber incumple Valentina en la situación A?", "La confidencialidad: expone datos de una paciente", "La puntualidad", "El cuidado de los bienes de la empresa", "Publicar datos de una paciente vulnera su privacidad y el deber de reserva."),
        ("abc", "{F} ¿Qué deber incumple Pedro en la situación B?", "La puntualidad y el aviso de sus atrasos", "La confidencialidad", "El cuidado de los bienes", "Llegar tarde sin avisar incumple la puntualidad y recarga a los compañeros."),
        ("abc", "{F} ¿Qué derecho se ve afectado en la situación C?", "Conocer sus condiciones de trabajo por escrito", "Ser promovida", "Elegir su horario libremente", "Una copia del contrato permite conocer y conservar las condiciones acordadas."),
        ("abc", "{F} ¿Qué corresponde a Camilo en la situación D antes de operar la máquina?", "Informar que no tiene capacitación y pedirla, junto con la autorización, antes de operarla", "Operarla igual para no quedar mal", "Operarla observando a un compañero", "La capacitación es un derecho y una condición de seguridad para tareas con riesgo."),
        ("abc", "¿Qué institución orienta sobre los derechos laborales en Chile?", "La Dirección del Trabajo", "El Servicio de Impuestos Internos", "El Registro Civil", "La Dirección del Trabajo orienta y fiscaliza las normas laborales."),
        ("=", "{F} Pedro llega 25 minutos tarde, 4 días a la semana. ¿Cuántos minutos de atraso acumula en 3 semanas?", "25*4*3", "Se multiplican los minutos por los días y por las semanas.", " minutos"),
        ("=", "Una empresa de ejemplo tiene 18 trabajadores y 12 ya firmaron el compromiso de confidencialidad. ¿Cuántos faltan por firmarlo?", "18-12", "Al total de trabajadores se le restan los que ya firmaron.", " trabajadores"),
        ("abc", "{F} Rosario insiste en su copia del contrato. ¿Qué es lo mejor?", "Pedirla por escrito y, si no se la entregan, consultar en la Dirección del Trabajo", "Dejar de pedirla para no tener problemas", "Tomar una copia a escondidas", "Pedir por escrito y consultar a la institución correcta es lo adecuado."),
        ("abc", "Un compañero dice: «Si tengo derechos, no tengo deberes». ¿Qué respuesta es correcta?", "Derechos y deberes van juntos: cumplir mis deberes protege el trabajo del equipo", "Tiene razón, los derechos anulan los deberes", "Solo los jefes tienen deberes", "Derechos y deberes se complementan y se aplican a ambas partes."),
        ("abc", "{F} Pedro dice: «Mis compañeros me cubren, nadie sale perjudicado». ¿Qué observación corresponde?", "Sí hay perjuicio: sobrecarga a los compañeros y afecta el servicio; lo correcto es avisar y acordar", "Tiene razón, porque no hay quejas", "Solo importa si el jefe se entera", "Cubrir un puesto recarga a otros y puede afectar la atención."),
        ("=", "{F} Un turno de 4 personas atiende 80 personas en un día. Si Pedro llega tarde y se atienden 12 menos, ¿cuántas personas se atienden?", "80-12", "A las personas atendidas normalmente se les restan las que dejaron de atenderse.", " personas"),
        ("abc", "Una trabajadora quiere saber cuántos días de descanso le corresponden. ¿Qué es lo más seguro?", "Consultar la norma vigente en fuentes oficiales y el contrato", "Preguntar a un compañero que «lo recuerda»", "Suponer una cifra de memoria", "Las cifras legales deben verificarse en fuentes oficiales y no de memoria."),
    ],
    ctx=("abc", "{F} Valentina ya publicó el comentario sobre la paciente. Su jefa lo descubre. ¿Qué actitud es la más adecuada?", "Reconocer el error, borrar la publicación y conversar con la jefa para reparar y evitar que se repita", "Decir que fue una broma", "Negar que fue ella", "Asumir la falta con honestidad ayuda a reparar el daño y cumplir el deber de reserva."),
    sc=[
        ("En derechos laborales: ¿qué es un deber?", "Una obligación que se asume al aceptar el trabajo", "Los deberes forman parte del contrato."),
        ("¿Qué haces si te piden operar una máquina sin capacitación?", "Informo que no estoy capacitado y pido formación", "Es un derecho y también una condición de seguridad."),
        ("¿Dónde verificas cifras como días de descanso?", "En fuentes oficiales y en mi contrato", "Las cifras legales no se confían a la memoria."),
    ],
    op=("Caso de ejemplo. En una bodega ficticia, Hernán se queda en el celular durante el turno y no revisa un pedido; deja el pasillo con cajas en el suelo y publica en un grupo una foto de los datos de un cliente. Su jefa le pide que cambie. Él responde: «Yo tengo derecho a descansar». "
        "Escribe: (1) tres deberes que Hernán no cumple, (2) un derecho que sí tiene, (3) por qué derechos y deberes van juntos, (4) a quién podría consultar si cree que la jefa no respeta sus derechos.",
        "(1) Cumplir sus funciones, cuidar el orden y la seguridad del lugar, guardar la confidencialidad de los datos del cliente. (2) Tiene derecho a recibir un trato digno y a conocer sus condiciones de trabajo, y a descansos según la norma vigente. (3) El derecho de uno se respeta si todos cumplen su parte. (4) A la jefatura superior, al área de personas o a la Dirección del Trabajo.",
        ["identifica deberes", "reconoce un derecho", "explica la relación entre ambos", "nombra una fuente de consulta"],
        ["hoja con cuatro respuestas"],
        ["inventar cifras de descanso", "olvidar la confidencialidad", "culpar a la jefa sin consultar"],
        "Pregunta: «¿cómo pedirías respeto a un derecho sin faltar a un deber?». Debe hablar de pedirlo por escrito o con calma y por el conducto correcto."),
    reinforce="Escribe tres deberes y tres derechos de un trabajador de tu especialidad y marca los que dependen de la norma vigente.",
    extend="Explica con un ejemplo por qué no cumplir un deber puede afectar el derecho de otra persona.",
)

# ============================================================ OAG-06, clase 4
F = ("Ficha 24 (documentos de ejemplo de una trabajadora ficticia, Ana Soto, tienda de ejemplo). Contrato: sueldo base $480.000; bono de colación $30.000 mensual; bono por meta $50.000 si cumple la meta. "
     "Liquidación del mes: sueldo base $480.000; bono de colación $0; bono por meta $50.000 (cumplió la meta); descuentos de previsión y salud $82.000 en total. "
     "Un finiquito es el documento que deja constancia del término de la relación laboral y de los pagos pendientes.")
build(
    G6, 4, F,
    use="Aprenderé a comparar contrato y liquidación con datos, a reconocer qué es un finiquito y a seguir pasos para informarme y consultar antes de firmar.",
    prior=["Sé leer una liquidación.", "Sé sumar y restar montos.", "Conozco la Dirección del Trabajo."],
    explain=[
        "Para verificar que se respetan tus condiciones, compara tres cosas: lo que dice el contrato, lo que dice la liquidación y lo que realmente recibes. Si algo no coincide, calcula la diferencia, anota qué falta y consulta por escrito al área de personas o a la jefatura, adjuntando el contrato. Guarda copia de todo. Si no se resuelve, puedes pedir orientación a la Dirección del Trabajo.",
        "El finiquito es el documento que deja constancia del término de la relación laboral y de los pagos pendientes. Antes de firmarlo, léelo completo, verifica que los montos coincidan con tu contrato y tus liquidaciones, y consulta tus dudas. La norma vigente regula las causas y los procedimientos del término de un contrato; no los inventes ni los supongas: consúltalos en fuentes oficiales.",
        "Para informarte usa fuentes confiables: el texto vigente del Código del Trabajo, las orientaciones de la Dirección del Trabajo y las organizaciones de trabajadores si existen. Evita consejos de desconocidos y cifras de memoria." + LIM,
    ],
    vocab=[("finiquito", "documento que deja constancia del término de la relación laboral y de los pagos pendientes"), ("comparar", "revisar dos documentos para ver si coinciden"), ("diferencia", "monto que separa lo acordado de lo pagado"), ("fuente oficial", "institución o texto oficial confiable para informarse"), ("consulta por escrito", "pregunta enviada con respaldo")],
    worked=[
        ("Comparar contrato y liquidación", "Un contrato de ejemplo dice bono de $40.000 y la liquidación $25.000. ¿Cuál es la diferencia?", ["Se resta lo pagado a lo acordado.", "40.000 − 25.000 = 15.000."], "$15.000"),
        ("Qué hacer con una diferencia", "Un trabajador de ejemplo ve que su bono pagado es $15.000 menor que lo que dice su contrato. ¿Cuál es el primer paso adecuado?", ["Se avisa a quien corresponde con respaldo.", "Se hace una consulta por escrito adjuntando el contrato."], "Consultar por escrito, con el contrato, al área de personas"),
    ],
    mistakes=[("Firmar un finiquito «porque es puro trámite» sin leerlo.", "Puede tener montos incorrectos o renunciar a pagos sin que la persona lo note.", "Léelo completo, compara con tus documentos y consulta antes de firmar."),
              ("Informarse sobre derechos laborales en foros anónimos o por cifras de memoria.", "Pueden ser datos incorrectos o desactualizados.", "Usa fuentes oficiales y el texto vigente de la norma.")],
    T=[
        ("abc", "{F} ¿Qué bono aparece en el contrato y no aparece pagado en la liquidación?", "El bono de colación", "El bono por meta", "El sueldo base", "El contrato fija $30.000 de colación y la liquidación indica $0."),
        ("=", "{F} Según el contrato, ¿cuál es el total de haberes que debería tener Ana si cumple la meta?", "480000+30000+50000", "Se suman el sueldo base y los dos bonos del contrato.", " pesos"),
        ("=", "{F} ¿Cuál es el total de haberes de la liquidación?", "480000+0+50000", "Se suman los haberes que sí aparecen en la liquidación.", " pesos"),
        ("=", "{F} ¿Cuántos pesos de diferencia hay entre lo que dice el contrato y lo que aparece en la liquidación?", "(480000+30000+50000)-(480000+0+50000)", "Se resta el total de la liquidación al total del contrato.", " pesos"),
        ("=", "{F} ¿Cuál es el sueldo líquido de la liquidación (haberes menos descuentos)?", "(480000+0+50000)-82000", "Al total de haberes de la liquidación se le restan los descuentos.", " pesos"),
        ("abc", "{F} ¿Qué es lo primero que debe hacer Ana al ver la diferencia?", "Comparar contrato y liquidación y consultar por escrito al área de personas", "No decir nada para evitar problemas", "Pedir prestado a un compañero para compensar", "Verificar y consultar por escrito permite corregir un posible error."),
        ("abc", "{F} ¿Qué es un finiquito?", "El documento que deja constancia del término de la relación laboral y de los pagos pendientes", "El documento que fija el sueldo del mes", "La liquidación que se entrega todos los meses", "El finiquito se firma al terminar la relación laboral, no mensualmente."),
        ("abc", "¿Qué conviene hacer antes de firmar un finiquito?", "Leerlo completo y consultar las dudas", "Firmarlo de inmediato para terminar el trámite", "Pedir a un compañero que lo firme por ti", "Firmar sin leer puede significar aceptar montos incorrectos."),
        ("abc", "¿Qué fuentes son adecuadas para informarse sobre derechos laborales?", "El texto vigente del Código del Trabajo y las orientaciones de la Dirección del Trabajo", "Un foro anónimo en internet", "El comentario de un compañero que lo recuerda", "Las fuentes oficiales son confiables y se mantienen actualizadas."),
        ("abc", "{F} Ana piensa que se «olvidó» el bono de colación y que es mejor no reclamar. ¿Qué respuesta es correcta?", "Conviene preguntar con respeto y por escrito, porque puede ser un error que se corrige", "Es mejor no preguntar nunca", "Debe descontarse el bono ella misma de otra parte", "Un error de liquidación se corrige si se consulta con respaldo."),
        ("abc", "Un compañero dice a otro: «Firma el finiquito aquí mismo, es puro trámite». ¿Qué responde?", "Que lo leerá con calma y consultará antes de firmar", "Que firma sin leer por confianza", "Que lo firmará el próximo mes", "Leer y consultar antes de firmar protege a la persona."),
        ("abc", "{F} La empresa responde que el bono de colación se pagó en efectivo, pero no hay comprobante. ¿Qué conviene?", "Pedir que el pago quede respaldado por escrito y consultar a la Dirección del Trabajo si persiste la duda", "Aceptar la explicación sin pruebas", "Amenazar con abandonar el trabajo", "Un pago debe quedar respaldado por escrito; si hay dudas, se consulta a la institución."),
        ("=", "{F} Si Ana lleva 3 meses sin que se le pague el bono de colación, ¿cuánto se le adeuda por ese bono?", "30000*3", "Se multiplica el bono mensual por los meses impagos.", " pesos"),
    ],
    ctx=("abc", "{F} Ana consultó por escrito hace 10 días y no tiene respuesta. ¿Qué hace?", "Reitera la consulta con respeto y, si no hay respuesta, pide orientación a la Dirección del Trabajo", "Deja de trabajar hasta que le contesten", "Comenta el problema con todos los clientes", "Reiterar por escrito y buscar orientación oficial es el camino ordenado."),
    sc=[
        ("En derechos laborales: ¿qué comparas para verificar tus condiciones?", "El contrato y la liquidación", "Si coinciden, se cumplen las condiciones acordadas."),
        ("¿Qué haces antes de firmar un finiquito?", "Lo leo completo y consulto mis dudas", "Firmar sin revisar puede perjudicarte más adelante."),
        ("¿Dónde buscas información confiable sobre normas laborales?", "En fuentes oficiales", "Las fuentes oficiales son confiables y están actualizadas."),
    ],
    op=("Caso de ejemplo. Bruno trabaja en una distribuidora ficticia. Su contrato (de ejemplo) dice: sueldo base $450.000; bono de transporte $25.000; bono por ventas $40.000 si cumple la meta. Su liquidación del mes dice: sueldo base $450.000; bono de transporte $25.000; bono por ventas $0, aunque cumplió la meta. Descuentos: $70.000. "
        "Escribe: (1) el total de haberes que debería tener, (2) el de la liquidación, (3) la diferencia, (4) el sueldo líquido de la liquidación, (5) la consulta por escrito que enviarías y a quién.",
        "(1) 450.000 + 25.000 + 40.000 = 515.000. (2) 450.000 + 25.000 = 475.000. (3) 40.000. (4) 475.000 − 70.000 = 405.000. (5) «Estimada encargada de personas: cumplí la meta de ventas del mes y en mi liquidación el bono aparece en $0, aunque mi contrato lo establece en $40.000. ¿Pueden revisarlo? Adjunto mi contrato».",
        ["calcula bien los totales", "detecta la diferencia", "calcula el líquido", "redacta una consulta respetuosa y por escrito"],
        ["hoja con cinco respuestas"],
        ["no comparar con el contrato", "reclamar sin respaldo", "inventar normas"],
        "Pregunta: «¿qué harías si en el finiquito aparece el bono pendiente?». Debe revisar que el monto sea correcto antes de firmar."),
    reinforce="Escribe los pasos para comparar tu contrato con una liquidación y qué harías con una diferencia.",
    extend="Explica por qué conviene guardar copias de contrato, liquidaciones y consultas.",
)

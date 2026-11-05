"""Cuaderno del estudiante, 2.º medio Orientación: OA 07 (participación, equidad y bienestar en el entorno)."""
from __future__ import annotations

from or_m2_common import M, T, W, lesson
from student_lessons import arith, ex

OA7 = "OR2M OA 07"

lesson(
    OA7, 1,
    "Una hoja y un lápiz. El caso de un liceo inventado está escrito en la clase y en los ejercicios. No necesitas contar nada de tu curso real.",
    "Aprenderé a examinar un caso ficticio de un problema del entorno, como el curso, el liceo o el barrio, e identificar quiénes son sujetos de derecho y dónde se puede participar. Sirve para pasar de quejarse a proponer.",
    ["Sé que todas las personas tienen derechos (1.º medio).", "Sé qué es el Consejo de Curso."],
    [
        "Un sujeto de derecho es una persona que tiene derechos y puede exigirlos y respetar los de otros. Los estudiantes lo son, igual que sus profesores, sus familias y las personas del barrio. Reconocerse así significa saber que mi opinión cuenta y que también debo escuchar la de los demás. El entorno cercano es el curso, el establecimiento y el barrio.",
        "En cada entorno hay instancias de participación, es decir, espacios organizados donde las personas opinan y deciden. Por ejemplo: el Consejo de Curso, el Centro de Estudiantes, el Consejo Escolar o una junta de vecinos. Participar es aportar con ideas, votar, colaborar en una tarea o representar a otros, siempre con respeto por la dignidad, la diversidad y el bienestar de todos.",
        "Para examinar un caso conviene anotar el problema, quiénes se ven afectados, qué derecho está en juego y qué instancia podría ayudar. Un problema bien descrito puede resolverse mejor. Y si el problema incluye violencia o discriminación grave, además se avisa a una persona adulta de confianza.",
    ],
    [("sujeto de derecho", "persona que tiene derechos y puede ejercerlos"), ("instancia de participación", "espacio organizado donde se opina y se decide"), ("entorno", "lo que rodea a una persona, como el curso o el barrio"), ("bienestar", "estado en que las personas se sienten bien y seguras"), ("diversidad", "existencia de personas distintas en un mismo lugar")],
    [
        W("Identificar el problema", "En el liceo inventado, el baño de un piso no tiene luz hace tres semanas. ¿Qué derecho se ve afectado y quiénes?", ["Afecta la seguridad y la dignidad.", "Lo usan todos los estudiantes de ese piso."], "El bienestar y la seguridad de quienes usan ese baño"),
        W("Elegir una instancia", "Un grupo quiere pedir que reparen el baño. ¿A qué instancia puede llevar el tema primero?", ["Es un problema del liceo, no solo del curso.", "El Centro de Estudiantes representa a los estudiantes."], "Al Consejo de Curso y al Centro de Estudiantes"),
    ],
    [
        M("Pensar que participar es solo votar.", "Se reduce la participación a una acción.", "También es proponer, colaborar y representar a otros."),
        M("Creer que un problema del liceo no es de los estudiantes.", "Se cree que solo deciden los adultos.", "Los estudiantes son sujetos de derecho y pueden aportar."),
    ],
    R=[
        ex("Una persona con derechos que puede ejercerlos y respetar los de otros es A) un sujeto de derecho B) un espectador", "A", "Esa es la definición."),
        ex("El Consejo de Curso, ¿es una instancia de participación? Responde sí o no.", "Sí", "Es un espacio donde el curso opina y decide."),
        ex("¿Participar es solo votar? Responde sí o no.", "No", "También incluye proponer y colaborar."),
    ],
    U=[
        ex("Un baño sin luz por semanas afecta A) la seguridad y el bienestar B) solo el horario", "A", "Hay un riesgo para las personas que lo usan."),
        ex("¿Por qué conviene describir bien el problema antes de proponer? A) Porque así se encuentra una solución más adecuada B) Porque se ahorra tinta", "A", "Un buen diagnóstico mejora la solución."),
        ex("¿Qué es el entorno cercano? A) El curso, el liceo y el barrio B) Un país lejano", "A", "Es lo que rodea a las personas cada día."),
    ],
    A=[
        ex("Clasifica con C (curso), L (liceo) o B (barrio): 1) No hay tacho de basura en la plaza de la esquina. 2) Los bancos de la sala 3 están rotos. 3) El comedor del liceo es pequeño. Escribe las letras en orden.", "B, C, L", "Cada problema pertenece al lugar que lo contiene."),
        ex("En el liceo inventado, 120 estudiantes de 3 pisos usan el baño del primer piso. Si cada piso aporta el mismo número, ¿cuántos hay por piso?", "40", "120 dividido en 3 es 40."),
        ex("¿Cuál instancia es más adecuada para un problema que afecta a todos los estudiantes del liceo? A) El Centro de Estudiantes B) Un grupo de amigos", "A", "Representa a todo el estudiantado."),
    ],
    Z=[
        ex("¿Por qué un derecho se ejerce mejor cuando se participa?", "Porque la participación permite que las personas expresen sus necesidades y se tomen decisiones que las consideren", "Sin participación, nadie sabe qué se necesita."),
        ex("Un compañero dice: «Mi opinión no importa porque soy joven». ¿Qué respondes? A) Los jóvenes también son sujetos de derecho B) Tienes razón", "A", "La edad no quita el derecho a opinar."),
    ],
    D=[
        arith("En una encuesta de ejemplo, 90 estudiantes opinan sobre los baños: 54 dicen que hay problemas. ¿Cuántos no dicen que hay problemas?", "90-54", "Al total se le restan quienes dicen que sí."),
        ex("Un grupo propone reparar la luz del baño y también cuidar que nadie quede aislado en las actividades. ¿Qué dos aspectos incluye? A) Bienestar y inclusión B) Notas y horarios", "A", "Cuida la seguridad y la participación de todos."),
    ],
    context=[ex("En un barrio inventado, los vecinos notan que la plaza no tiene rampa para sillas de ruedas. ¿Qué derecho está en juego? A) La inclusión y el acceso de todos B) La moda", "A", "Sin rampa algunas personas quedan fuera.")],
    selfcheck=[ex("En Orientación: ¿un sujeto de derecho puede opinar y proponer?", "Sí", "Ejerce sus derechos con respeto."), ex("¿El Consejo de Curso es una instancia de participación?", "Sí", "Es un espacio de decisión del curso."), ex("¿Los estudiantes pueden participar en problemas del liceo?", "Sí", "Son parte de la comunidad.")],
    task=T("Lee el caso inventado: En un liceo, la cancha se usa siempre para fútbol de varones y las demás estudiantes casi nunca tienen un turno. Varias dicen que quieren jugar básquetbol o vóleibol. Escribe: (1) el problema en una frase, (2) quiénes se ven afectados, (3) qué derecho o principio está en juego y (4) dos instancias donde podrían participar.", "Problema: la cancha se reparte de forma desigual. Afectadas: estudiantes que no juegan fútbol. Principio: inclusión y participación de todas. Instancias: Consejo de Curso y Centro de Estudiantes.", ["describe el problema en una frase", "nombra quiénes se ven afectados", "nombra un principio o derecho", "nombra dos instancias"], ["texto escrito", "tabla"], ["culpar a personas", "no nombrar instancias"], "Reconoce el problema bien descrito y pregunta qué dato falta para entenderlo mejor."),
    reinforce="Anota un problema inventado del barrio y qué instancia podría ayudar.",
    extend="Explica por qué ser sujeto de derecho también implica escuchar a otros.",
)

lesson(
    OA7, 2,
    "Una hoja y un lápiz. Los datos de ejemplo, como horarios y listas, están escritos en los ejercicios.",
    "Aprenderé a distinguir igualdad, equidad e inclusión, a reconocer hechos y derechos en problemas del entorno y a detectar prejuicios de género. Sirve para plantear problemas con justicia.",
    ["Sé qué es un sujeto de derecho.", "Sé distinguir hecho y opinión."],
    [
        "La igualdad es dar a todas las personas el mismo trato y los mismos derechos. La equidad es dar a cada persona lo que necesita para que tenga las mismas oportunidades. Por ejemplo, si un estudiante usa silla de ruedas, una rampa no es un privilegio sino equidad. La inclusión es lograr que todas las personas puedan participar. Estas ideas se complementan y ayudan a decidir con justicia.",
        "La equidad de género es que mujeres, hombres y personas de otras identidades tengan las mismas oportunidades, sin estereotipos. Un estereotipo es una idea fija sobre cómo debería ser un grupo, como «el fútbol es de hombres». Un hecho se comprueba, por ejemplo, con un registro de turnos de uso de la cancha. Un prejuicio es una opinión sin base que tratas como cierta.",
        "Los derechos no se pierden por tener otra opinión ni por ser distintos. La participación democrática es que todas las personas puedan opinar y que las decisiones se tomen con reglas conocidas. Y la justicia es que cada persona reciba un trato justo. Cuando una situación vulnera estos principios, se plantea en la instancia adecuada y, si hay daño, se avisa a una persona adulta.",
    ],
    [("equidad", "dar a cada persona lo que necesita para tener las mismas oportunidades"), ("estereotipo", "idea fija sobre cómo debe ser un grupo"), ("prejuicio", "opinión sin base que se trata como verdad"), ("participación democrática", "que todos opinen y se decida con reglas conocidas"), ("justicia", "trato justo para cada persona")],
    [
        W("Igualdad o equidad", "Un liceo inventado instala una rampa para que un estudiante en silla de ruedas llegue a la sala. ¿Es igualdad o equidad?", ["Da lo que esa persona necesita.", "Permite las mismas oportunidades."], "Equidad"),
        W("Detectar el estereotipo", "Un compañero dice: «El básquetbol es solo para hombres». ¿Es un hecho o un estereotipo?", ["Generaliza sobre un grupo.", "No se apoya en datos."], "Un estereotipo"),
    ],
    [
        M("Creer que la equidad es un trato de favor.", "Se confunde dar apoyo con dar ventaja.", "La equidad da lo necesario para que todos partan con las mismas oportunidades."),
        M("Pensar que igualdad es tratar a todos exactamente igual en cualquier caso.", "Se olvidan las necesidades distintas.", "A veces se necesitan apoyos distintos para llegar al mismo derecho."),
    ],
    R=[
        ex("Dar a cada persona lo que necesita para tener las mismas oportunidades es A) equidad B) estereotipo", "A", "Esa es la definición de equidad."),
        ex("«Esa carrera es solo para hombres» es un A) estereotipo B) hecho", "A", "Generaliza sobre un grupo sin datos."),
        ex("La inclusión busca que todas las personas puedan participar. Responde sí o no.", "Sí", "Nadie queda fuera."),
    ],
    U=[
        ex("Una rampa para una persona que usa silla de ruedas es A) equidad B) un privilegio", "A", "Permite el mismo acceso."),
        ex("¿Qué es la participación democrática? A) Que todos opinen y se decida con reglas conocidas B) Que decida solo uno", "A", "Las reglas son claras para todos."),
        ex("¿Qué se comprueba con un registro de turnos de la cancha? A) Un hecho B) Un prejuicio", "A", "Los registros muestran datos reales."),
    ],
    A=[
        ex("Clasifica con H (hecho) o P (prejuicio): 1) «En el registro, las mujeres usaron la cancha 2 de 20 turnos.» 2) «A ellas no les gusta el deporte.» 3) «Hay 3 canchas y solo una tiene luz.» Escribe las letras en orden.", "H, P, H", "La 1 y la 3 se comprueban; la 2 supone un gusto."),
        ex("De 20 turnos de ejemplo de la cancha, 2 fueron de mujeres. ¿Cuántos turnos fueron de otros grupos?", "18", "A los 20 se les restan los 2."),
        ex("Una propuesta justa para repartir turnos es A) alternar los grupos según un calendario conocido B) que usen la cancha los que lleguen primero siempre", "A", "Las reglas son claras y parejas."),
    ],
    Z=[
        ex("¿Por qué una regla conocida por todos hace más justa una decisión?", "Porque todas las personas saben cómo se decide y pueden participar con las mismas condiciones", "La transparencia da justicia."),
        ex("Un compañero dice: «Si damos apoyo especial a alguien, los demás pierden». ¿Qué respondes? A) El apoyo permite igualdad de oportunidades para todos B) Tienes razón", "A", "Equidad no quita derechos a nadie."),
    ],
    D=[
        arith("Un liceo de ejemplo tiene 3 canchas y 5 días hábiles. Si cada día se usan las 3 en 4 turnos, ¿cuántos turnos hay en la semana?", "3*5*4", "Se multiplican canchas, días y turnos."),
        ex("Un calendario reparte 12 turnos de cancha en partes iguales entre 3 grupos. ¿Cuántos turnos recibe cada grupo?", "4", "12 turnos divididos en 3 son 4 turnos."),
    ],
    context=[ex("En una asamblea, un estudiante dice «si cambiamos los turnos, ya no somos iguales». ¿Qué conviene aclarar? A) Que alternar turnos busca equidad y que todos puedan participar B) Que no se cambie nada", "A", "Los turnos justos amplían la participación.")],
    selfcheck=[ex("En Orientación: ¿la equidad da a cada persona lo que necesita?", "Sí", "Busca igualdad de oportunidades."), ex("¿Un estereotipo es una idea fija sobre un grupo?", "Sí", "Se aplica sin comprobar."), ex("¿Una regla conocida hace más justa una decisión?", "Sí", "Todos pueden participar.")],
    task=T("Lee los datos de ejemplo: en un mes, una cancha de liceo tuvo turnos de uso. El grupo A usó 12 turnos, el grupo B usó 3 y el grupo C usó 3. Escribe: (1) el total de turnos usados, (2) cuántos turnos tendría cada grupo si se repartieran en partes iguales, (3) una propuesta de calendario justa y conocida por todos y (4) la instancia donde la presentarías.", "Total: 18 turnos. En partes iguales, 6 turnos por grupo. Propuesta: turnos rotativos publicados en un calendario. Instancia: Consejo de Curso y Centro de Estudiantes.", ["calcula el total", "calcula el reparto igual", "propone un calendario conocido", "nombra una instancia"], ["texto escrito", "tabla"], ["calcular mal", "proponer reglas que nadie conoce"], "Reconoce el reparto razonado y pregunta cómo se enterarían todos."),
    reinforce="Escribe una diferencia entre igualdad y equidad con un ejemplo inventado.",
    extend="Explica por qué un estereotipo puede limitar los derechos de alguien.",
)

lesson(
    OA7, 3,
    "Una hoja y un lápiz. Las instancias y los datos de ejemplo están escritos en los ejercicios.",
    "Aprenderé a comparar instancias de participación y a elegir la más adecuada para un problema, según su alcance, su rapidez y su capacidad de decidir. Sirve para llevar un tema al lugar donde puede resolverse.",
    ["Sé distinguir igualdad, equidad e inclusión.", "Sé identificar el problema y quiénes afectan."],
    [
        "No todas las instancias de participación sirven para lo mismo. El Consejo de Curso es el espacio del curso para conversar y decidir asuntos propios del curso. El Centro de Estudiantes representa al estudiantado ante la dirección del establecimiento. El Consejo Escolar reúne a distintos integrantes de la comunidad, como la dirección, docentes, familias y estudiantes. Una junta de vecinos reúne a personas del barrio.",
        "Para elegir una instancia se hacen tres preguntas: ¿afecta a ese grupo?, ¿puede decidir o llevar el tema a quien decide? y ¿es rápida o lenta para el problema? Cada sí vale 1 punto. Un problema de un curso va primero al Consejo de Curso. Uno que afecta a todo el establecimiento puede ir al Centro de Estudiantes. Uno del barrio, a la junta de vecinos.",
        "A veces conviene usar dos instancias en secuencia: primero el curso, luego el Centro de Estudiantes. Las consecuencias de elegir mal son perder tiempo o que el problema no llegue a quien puede resolverlo. Y si el problema incluye un riesgo para alguien, se avisa de inmediato a una persona adulta, sin esperar una reunión.",
    ],
    [("alcance", "a cuántas personas llega o afecta algo"), ("representar", "hablar en nombre de otras personas"), ("Consejo Escolar", "instancia con dirección, docentes, familias y estudiantes"), ("secuencia", "orden en que se hacen las cosas"), ("junta de vecinos", "organización de personas del mismo barrio")],
    [
        W("Elegir la instancia", "Un problema afecta solo a un curso: la sala no tiene suficientes mesas. ¿Dónde se lleva primero?", ["Afecta a un solo curso.", "El Consejo de Curso es el espacio del curso."], "Al Consejo de Curso"),
        W("Puntuar", "Para un problema de todo el liceo, el Centro de Estudiantes: afecta al grupo sí, puede llevar el tema a la dirección sí, es rápido no. Cada sí vale 1. ¿Cuántos puntos suma?", ["Hay dos síes.", "Un no."], "2 puntos"),
    ],
    [
        M("Llevar todo a una sola instancia sin pensar.", "Se cree que da igual dónde se plantee.", "Elige según el alcance y quién puede decidir."),
        M("Esperar la reunión cuando hay un riesgo urgente.", "Se piensa que todo debe ir por la instancia.", "Si hay riesgo, avisa de inmediato a una persona adulta."),
    ],
    R=[
        ex("Un problema de un solo curso, ¿se lleva primero al Consejo de Curso? Responde sí o no.", "Sí", "Es el espacio del curso."),
        ex("El Centro de Estudiantes representa al estudiantado ante la dirección. Responde sí o no.", "Sí", "Esa es su función."),
        ex("Una junta de vecinos reúne a personas A) del barrio B) de otra ciudad", "A", "Es una organización barrial."),
    ],
    U=[
        ex("¿Qué instancia reúne a dirección, docentes, familias y estudiantes? A) El Consejo Escolar B) El Consejo de Curso", "A", "Incluye a varios integrantes de la comunidad."),
        ex("¿Por qué conviene usar dos instancias en secuencia a veces? A) Porque se parte por el grupo cercano y luego se amplía B) Porque duplica el trabajo", "A", "Se recoge opinión y luego se representa."),
        ex("Si hay un riesgo urgente para alguien, ¿qué haces? A) Avisas de inmediato a una persona adulta B) Esperas la próxima reunión", "A", "La seguridad no puede esperar."),
    ],
    A=[
        ex("Clasifica con C (Consejo de Curso), E (Centro de Estudiantes) o V (junta de vecinos): 1) Falta de alumbrado en la calle del barrio. 2) Pizarra rota en una sala. 3) Falta de acceso en el liceo para todos. Escribe las letras en orden.", "V, C, E", "Cada problema pertenece a la instancia que lo contiene."),
        ex("Un problema de 3 cursos del mismo nivel se presenta primero en cada Consejo de Curso y luego al Centro de Estudiantes. ¿Cuántas instancias distintas usa en total?", "4", "Son 3 consejos de curso y 1 Centro de Estudiantes."),
        ex("Un Centro de Estudiantes recibe 6 propuestas y elige 2 para presentar. ¿Cuántas quedan para otra reunión?", "4", "A las 6 se les restan las 2 elegidas."),
    ],
    Z=[
        ex("¿Por qué conviene elegir la instancia según el alcance del problema?", "Porque así el tema llega a quienes pueden decidir y no se pierde tiempo", "La elección correcta hace avanzar la solución."),
        ex("Un compañero dice: «Con llevar el problema a un solo lugar basta». ¿Qué respondes? A) A veces conviene usar dos instancias en orden B) Tienes razón", "A", "Cada instancia aporta algo distinto."),
    ],
    D=[
        arith("En una votación de ejemplo participan 35 estudiantes y 21 votan a favor de una propuesta. ¿Cuántos no votaron a favor?", "35-21", "Del total se restan los votos a favor."),
        arith("Una instancia se reúne 2 veces por mes durante 6 meses. ¿Cuántas reuniones hay?", "2*6", "Se multiplican reuniones por meses."),
    ],
    context=[ex("Un estudiante inventado dice que el comedor del liceo es pequeño. ¿A qué instancia lo llevarías? A) Al Centro de Estudiantes B) Al grupo de amigos", "A", "Afecta a todo el liceo.")],
    selfcheck=[ex("En Orientación: ¿el Consejo de Curso sirve para asuntos del curso?", "Sí", "Es su ámbito."), ex("¿El Centro de Estudiantes representa al estudiantado?", "Sí", "Habla en nombre de los estudiantes."), ex("¿Un riesgo urgente se avisa de inmediato a un adulto?", "Sí", "No se espera una reunión.")],
    task=T("Lee los tres problemas inventados: (a) el curso 2.º A no tiene suficientes enchufes en la sala; (b) todo el liceo tiene pocas mesas en el comedor; (c) la plaza del barrio no tiene luz de noche. Elige para cada uno la instancia más adecuada (Consejo de Curso, Centro de Estudiantes o junta de vecinos), con tres preguntas: afecta, puede decidir y es rápida. Suma puntos y justifica.", "(a) Consejo de Curso: afecta sí, puede decidir sí, es rápido sí = 3 puntos. (b) Centro de Estudiantes: afecta a todos sí, lleva el tema a la dirección sí, es rápido no = 2 puntos. (c) Junta de vecinos: es un asunto del barrio sí, puede llevar el tema a quien decide sí, es rápida no = 2 puntos.", ["elige una instancia por problema", "responde las tres preguntas", "suma los puntos", "justifica"], ["tabla escrita", "texto breve"], ["elegir una instancia que no corresponde", "no justificar"], "Reconoce el uso de criterios y pregunta cuándo usaría dos instancias."),
    reinforce="Escribe un problema inventado de tu comuna y la instancia que lo recibiría.",
    extend="Explica por qué una instancia puede ser muy lenta para un riesgo urgente.",
)

lesson(
    OA7, 4,
    "Una hoja y un lápiz. Los casos de participación, con y sin riesgo, están escritos en los ejercicios.",
    "Aprenderé a elegir una acción segura y respetuosa para participar o contribuir, y a reconocer cuándo una situación de discriminación o violencia exige avisar a una persona adulta. Sirve para participar sin exponerme.",
    ["Sé elegir la instancia adecuada.", "Sé que hay riesgos que exigen a una persona adulta."],
    [
        "Participar de forma segura es hacerlo por canales conocidos, con respeto y sin exponer a nadie. Por ejemplo, presentar una propuesta por escrito en el Consejo de Curso, recoger firmas voluntarias o conversar con el equipo directivo en horario acordado. No es seguro difundir fotos de personas, acusar a alguien sin pruebas ni hacer campañas que humillen.",
        "Si un problema incluye discriminación o violencia, la participación no reemplaza el aviso a una persona adulta. Por ejemplo, si un grupo hostiga a un compañero por su origen, la acción segura es apoyar a la persona afectada, guardar evidencia sin difundirla y contarlo a un adulto del establecimiento. Las instancias estudiantiles pueden acompañar después, pero no resolver solas un caso de violencia.",
        "También hay una forma segura de reclamar: describir hechos, evitar nombres cuando no es necesario, pedir algo concreto y decir a quién se dirige la petición. Un reclamo bien hecho es respetuoso, claro y viable. Y quien lo presenta no debe sufrir represalias, es decir, castigos por participar.",
    ],
    [("canal", "vía conocida para presentar una petición"), ("represalia", "castigo por haber participado o reclamado"), ("reclamo", "petición formal por un problema"), ("viable", "que se puede realizar"), ("evidencia", "registro de lo que ocurrió")],
    [
        W("Canal seguro", "Un grupo quiere cambiar el horario del recreo. ¿Qué es más seguro: presentar una propuesta escrita en el Consejo de Curso o hacer una campaña burlándose de quien decidió?", ["Una propuesta escrita usa un canal conocido.", "La burla no respeta la dignidad."], "Presentar una propuesta escrita"),
        W("Riesgo que exige adulto", "Un grupo hostiga a un compañero por su origen. ¿La instancia estudiantil puede resolverlo sola?", ["Hay discriminación y violencia.", "Se requiere la intervención de adultos."], "No, hay que avisar a una persona adulta"),
    ],
    [
        M("Difundir fotos de quien agrede para presionar.", "Se cree que exponer ayuda a resolver.", "Guarda evidencia y entrégala solo a una persona adulta."),
        M("Pensar que la instancia estudiantil reemplaza al adulto en casos de violencia.", "Se supone que puede resolver todo.", "Ante violencia, avisa a una persona adulta."),
    ],
    R=[
        ex("Presentar una propuesta por escrito, ¿es un canal seguro? Responde sí o no.", "Sí", "Es una vía conocida y respetuosa."),
        ex("Publicar la foto de alguien para presionar, ¿es seguro? Responde sí o no.", "No", "Expone a la persona."),
        ex("Un reclamo bien hecho es A) claro y respetuoso B) con insultos", "A", "Debe describir hechos y pedir algo concreto."),
    ],
    U=[
        ex("¿Qué es una represalia? A) Un castigo por haber participado B) Un premio", "A", "La participación no debe castigarse."),
        ex("Si hay hostigamiento por origen, ¿qué corresponde? A) Apoyar y avisar a una persona adulta B) Hacer una votación del curso", "A", "No se vota un derecho."),
        ex("¿Qué debe incluir un reclamo? A) Hechos, una petición concreta y a quién se dirige B) Solo quejas", "A", "Así es viable y claro."),
    ],
    A=[
        ex("Clasifica con S (segura) o N (no segura): 1) Entregar una propuesta firmada voluntariamente. 2) Acusar a alguien sin pruebas por un chat. 3) Contar a la orientadora que hostigan a un compañero. Escribe las letras en orden.", "S, N, S", "La 2 daña a alguien sin evidencia."),
        ex("Una propuesta recibió 42 firmas de 60 estudiantes del nivel. ¿Cuántos no firmaron?", "18", "A los 60 se les restan los 42."),
        ex("Un estudiante de ejemplo teme represalias por reclamar. ¿Qué haces? A) Le sugieres contarlo a una persona adulta de confianza B) Le sugieres callar", "A", "Así se protege su derecho a participar."),
    ],
    Z=[
        ex("¿Por qué las instancias estudiantiles no deben resolver solas un caso de violencia?", "Porque se necesita la intervención de personas adultas con protocolos para proteger a todos", "La violencia requiere ayuda competente."),
        ex("Un compañero dice: «Si hay discriminación, lo resolvemos en el Consejo de Curso». ¿Qué respondes? A) El curso puede apoyar, pero hay que avisar a un adulto B) Tienes razón", "A", "Ambas acciones se complementan."),
    ],
    D=[
        arith("Un reclamo de ejemplo tiene 5 firmas el lunes, 11 el martes y 17 el miércoles. ¿Cuántas firmas tiene en total?", "5+11+17", "Se suman las firmas de los tres días."),
        ex("Si un reclamo no incluye petición concreta, ¿qué le falta? A) Decir qué se pide y a quién B) Más adjetivos", "A", "Sin petición no se puede responder."),
    ],
    context=[ex("Un grupo de ejemplo quiere pedir más basureros en el patio. ¿Qué acción es segura y respetuosa? A) Redactar una propuesta y presentarla al Centro de Estudiantes B) Dejar basura para presionar", "A", "Usa un canal conocido y no daña a nadie.")],
    selfcheck=[ex("En Orientación: ¿participar de forma segura usa canales conocidos?", "Sí", "Evita exponer a otros."), ex("¿Difundir fotos de personas es seguro?", "No", "Las expone ante muchas personas."), ex("¿Ante violencia se avisa a una persona adulta?", "Sí", "Las instancias estudiantiles no la reemplazan.")],
    task=T("Lee los dos casos inventados: (a) un grupo quiere pedir un espacio techado para almorzar; (b) un grupo se burla de un compañero por su acento y alguien propone publicar su foto. Para cada caso escribe la acción segura, el canal o persona adulta a quien se dirige y una acción que no conviene. En (a) redacta además una petición concreta de una frase.", "(a) Presentar una propuesta al Centro de Estudiantes: «Pedimos un espacio techado en el patio para almorzar los días de lluvia.» No convienen las campañas que ofendan. (b) Apoyar al compañero y avisar a la orientadora; no publicar su foto.", ["elige una acción segura por caso", "nombra canal o adulto", "indica una acción que no conviene", "redacta una petición concreta"], ["texto escrito", "tabla"], ["difundir la foto", "reclamo sin petición"], "Reconoce la diferencia entre ambos casos y pregunta qué evidencia entregaría a la persona adulta."),
    reinforce="Redacta una petición concreta de una frase para mejorar un espacio inventado de tu curso.",
    extend="Explica por qué quien reclama no debe sufrir represalias.",
)

lesson(
    OA7, 5,
    "Una hoja y un lápiz. La propuesta de ejemplo y las frases para presentar están escritas en los ejercicios.",
    "Aprenderé a comunicar una propuesta de participación con un esquema claro de problema, evidencia, propuesta y compromiso, y a pedir ayuda cuando una situación me supera. Sirve para ser escuchado en una reunión.",
    ["Sé elegir una acción segura para participar.", "Sé qué es una petición concreta."],
    [
        "Una propuesta clara tiene cuatro partes. El problema, que se describe con hechos. La evidencia, que son datos o testimonios sin exponer a nadie. La propuesta, que es lo que se pide, y el compromiso, que es lo que el grupo hará para colaborar. Por ejemplo: «Hay 40 estudiantes y 12 puestos en el comedor; proponemos turnos; nos comprometemos a organizarlos».",
        "Al presentar en una reunión conviene hablar con calma, mirar al grupo, usar frases breves y pedir opiniones. Si alguien responde con una crítica, se escucha y se responde con respeto. Los números ayudan, pero hay que comprobarlos. Y no se menciona a personas concretas ni se habla de problemas personales de otros.",
        "Si un problema incluye violencia o riesgo, no se presenta en una reunión pública sino que se cuenta en privado a una persona adulta de confianza. Para eso, se usa el mensaje de hecho, emoción y petición. El Fono Niños 147 puede orientar a adolescentes, siempre junto con avisar a una persona adulta.",
    ],
    [("evidencia", "dato o testimonio que respalda lo que se dice"), ("propuesta", "lo que se pide para resolver un problema"), ("compromiso", "lo que el grupo se obliga a hacer"), ("testimonio", "relato de quien vivió una situación"), ("pública", "que ocurre ante muchas personas")],
    [
        W("Armar la propuesta", "Un curso inventado dice: «El comedor tiene 12 puestos para 40 estudiantes. Pedimos turnos. Nos comprometemos a organizarlos». ¿Cuál es el compromiso?", ["El compromiso es lo que el grupo hará.", "Es la última frase."], "Nos comprometemos a organizarlos"),
        W("Decidir dónde decirlo", "Un estudiante inventado sufre hostigamiento repetido. ¿Lo cuenta en una reunión pública o en privado a una persona adulta?", ["Es un tema de riesgo.", "Exponer su caso lo daña más."], "En privado, a una persona adulta de confianza"),
    ],
    [
        M("Presentar una propuesta con quejas sin datos.", "Se cree que la queja basta.", "Agrega evidencia y una petición concreta."),
        M("Contar un caso de violencia en una reunión pública.", "Se piensa que mostrar todo ayuda.", "Cuéntalo en privado a una persona adulta de confianza."),
    ],
    R=[
        ex("¿Qué parte de la propuesta dice lo que se pide? A) La propuesta B) El compromiso", "A", "Es el pedido para resolver el problema."),
        ex("Un dato que respalda lo que se dice es A) evidencia B) una opinión", "A", "Respalda con información."),
        ex("Un caso de violencia, ¿se cuenta en privado a una persona adulta? Responde sí o no.", "Sí", "Así se protege a la persona afectada."),
    ],
    U=[
        ex("¿Por qué conviene hablar con frases breves y calma? A) Para ser entendido y escuchado B) Para terminar rápido", "A", "La claridad ayuda."),
        ex("Si te critican, ¿qué haces? A) Escuchas y respondes con respeto B) Gritas", "A", "Escuchar abre el diálogo."),
        ex("¿Qué NO se hace en una presentación? A) Mencionar problemas personales de otros B) Usar datos comprobados", "A", "Eso expone a las personas."),
    ],
    A=[
        ex("Ordena con letras las partes de una propuesta: (a) «Nos comprometemos a organizarlos.» (b) «Hay 12 puestos para 40 estudiantes.» (c) «Pedimos turnos.» ¿Cuál es el orden problema, propuesta, compromiso?", "b, c, a", "La b es el problema, la c la propuesta y la a el compromiso."),
        arith("El comedor de ejemplo tiene 12 puestos. ¿Cuántos turnos mínimos necesitan 36 estudiantes para almorzar, si en cada turno se ocupan todos los puestos?", "36//12", "Se divide el total de estudiantes entre los puestos de cada turno."),
        ex("¿Cuál frase abre bien una presentación? A) «Queremos presentar un problema y una propuesta.» B) «Esto es un desastre y es culpa de todos.»", "A", "Es clara y no acusa."),
    ],
    Z=[
        ex("¿Por qué el compromiso del grupo hace más fuerte una propuesta?", "Porque muestra que el grupo no solo pide, sino que también colabora", "Aumenta la credibilidad."),
        ex("Un compañero dice: «Mejor nombrar a la persona que causó el problema». ¿Qué respondes? A) Es mejor describir hechos sin acusar a personas B) Tienes razón", "A", "Evita exponer y facilita el acuerdo."),
    ],
    D=[
        arith("Un grupo ensaya su presentación 4 veces de 6 minutos cada una. ¿Cuántos minutos ensaya?", "4*6", "Se multiplican las veces por los minutos."),
        arith("Un comedor de ejemplo tiene 12 puestos y 40 estudiantes. ¿Cuántos estudiantes quedan sin puesto si todos llegan a la vez?", "40-12", "Del total se restan los puestos disponibles."),
    ],
    context=[ex("En una reunión de curso, una estudiante propone turnos de aseo. ¿Qué agregar para que sea una propuesta completa? A) Evidencia y un compromiso B) Un apodo para quien no limpia", "A", "Completa las cuatro partes.")],
    selfcheck=[ex("En Orientación: ¿una propuesta tiene problema, evidencia, propuesta y compromiso?", "Sí", "Son las cuatro partes."), ex("¿Se nombra a personas concretas en una queja pública?", "No", "Se describen hechos sin exponer."), ex("¿Un caso de violencia se cuenta en privado a un adulto?", "Sí", "Se protege a la persona.")],
    task=T("Redacta una propuesta de cuatro partes (problema, evidencia, propuesta y compromiso) para este caso inventado: en un liceo no hay buena señalización de la salida de emergencia y cuesta encontrarla. Usa estos datos: 3 pisos y 2 salidas, una sin cartel. Luego escribe una frase para abrir la presentación y una para responder a una crítica con respeto.", "Problema: cuesta encontrar la salida de emergencia. Evidencia: el liceo tiene 3 pisos y 2 salidas, y una no tiene cartel. Propuesta: instalar un cartel en esa salida. Compromiso: ofrecemos diseñar los carteles. Apertura: «Queremos presentar un problema de seguridad y una propuesta.» Respuesta: «Gracias por la observación; revisemos cómo ajustarla.»", ["incluye las cuatro partes", "usa los datos entregados", "escribe una frase de apertura", "responde con respeto"], ["texto escrito", "presentación oral"], ["omitir el compromiso", "acusar a personas"], "Reconoce las cuatro partes y pregunta qué dato sumaría."),
    reinforce="Escribe en una frase el problema de un espacio inventado del liceo con un dato.",
    extend="Explica por qué se presenta en privado un problema de violencia.",
)

lesson(
    OA7, 6,
    "Una hoja y un lápiz. La matriz de diagnóstico y los datos están escritos en los ejercicios; nada de lo tuyo.",
    "Aprenderé a transferir lo aprendido a un entorno inventado, haciendo un diagnóstico con una matriz de problema, afectados, derecho, instancia y acción segura. Sirve para analizar cualquier barrio o liceo sin exponer a nadie.",
    ["Sé elegir instancia y acción segura.", "Sé armar una propuesta."],
    [
        "Un diagnóstico es una descripción ordenada de un problema antes de actuar. Se puede hacer con una matriz de cinco columnas: problema, personas afectadas, derecho o principio en juego, instancia y acción segura. Completarla obliga a separar hechos de opiniones y a pensar en todos, sin usar nombres reales.",
        "Para transferir, se aplica la misma matriz a un entorno nuevo. Por ejemplo, un barrio inventado con una plaza sin luz, un liceo con un baño inaccesible o un curso donde siempre hablan los mismos. El método no cambia: describir, ver a quién afecta, nombrar el derecho, elegir la instancia y decidir qué hacer.",
        "Una matriz bien hecha también incluye cuándo avisar a una persona adulta. Si en el caso hay violencia o discriminación grave, esa fila indica avisar. El aprendizaje es el método, no los nombres: puedes usarlo luego con casos reales sin contar datos privados.",
    ],
    [("diagnóstico", "descripción ordenada de un problema antes de actuar"), ("matriz", "tabla para ordenar información"), ("transferir", "aplicar lo aprendido a otro caso"), ("fila", "línea horizontal de una tabla"), ("sin exposición", "sin dar datos privados de nadie")],
    [
        W("Completar una fila", "Barrio inventado: la plaza no tiene luz. Completa persona afectada y derecho.", ["Afecta a quienes usan la plaza de noche.", "Está en juego la seguridad."], "Afectadas: quienes usan la plaza; derecho: seguridad y bienestar"),
        W("Elegir la instancia", "Para el problema de la plaza, ¿cuál es la instancia más adecuada?", ["Es un asunto del barrio.", "La junta de vecinos lo representa."], "La junta de vecinos"),
    ],
    [
        M("Llenar la matriz con nombres de personas reales.", "Se mezcla el análisis con casos personales.", "Usa personajes inventados."),
        M("Saltarse la fila de acción segura.", "Se piensa que describir basta.", "Cierra siempre con una acción segura y, si hay riesgo, un adulto."),
    ],
    R=[
        ex("Una matriz de diagnóstico, ¿ordena información en una tabla? Responde sí o no.", "Sí", "Esa es su función."),
        ex("¿Qué columna dice qué derecho está en juego? A) Derecho o principio B) Instancia", "A", "Nombra el principio afectado."),
        ex("Transferir es aplicar lo aprendido a otro caso. Responde sí o no.", "Sí", "Esa es la definición."),
    ],
    U=[
        ex("¿Por qué se usan personajes inventados? A) Para no exponer a nadie B) Para que sea más largo", "A", "Se aprende sin datos privados."),
        ex("¿Qué indica la fila de acción segura si hay violencia? A) Avisar a una persona adulta B) Esperar", "A", "La seguridad es prioritaria."),
        ex("¿Qué método se mantiene al cambiar de caso? A) Describir, ver afectados, nombrar el derecho, elegir instancia y actuar B) Cambiar todo", "A", "La matriz sirve en cualquier entorno."),
    ],
    A=[
        ex("Une cada problema con su instancia, escribe las letras en orden: 1) pocos basureros en una plaza, 2) falta de enchufes en una sala, 3) comedor pequeño en un liceo. Instancias: (a) Consejo de Curso, (b) junta de vecinos, (c) Centro de Estudiantes.", "b, a, c", "Cada problema se lleva al lugar que lo contiene."),
        ex("En una matriz de ejemplo hay 5 problemas y cada uno tiene 5 columnas. ¿Cuántas casillas hay?", "25", "5 por 5 son 25."),
        ex("Un caso de ejemplo muestra a un grupo hostigando a un compañero por su origen. ¿Qué incluye la fila de acción segura? A) Apoyar y avisar a una persona adulta B) Hacer un meme", "A", "Es una acción segura."),
    ],
    Z=[
        ex("¿Por qué el método importa más que los nombres del caso?", "Porque se puede aplicar a cualquier entorno sin exponer a nadie", "El método se transfiere."),
        ex("Un compañero dice: «Con una matriz sobra pensar». ¿Qué respondes? A) La matriz ordena el pensamiento, no lo reemplaza B) Tienes razón", "A", "Hay que juzgar cada caso."),
    ],
    D=[
        arith("Un grupo analiza 3 entornos inventados con 4 problemas cada uno. ¿Cuántos problemas analiza?", "3*4", "Se multiplican entornos por problemas."),
        arith("En una matriz de ejemplo, 8 problemas son del barrio y 5 del liceo. ¿Cuántos problemas hay?", "8+5", "Se suman los problemas de ambos entornos."),
    ],
    context=[ex("En una feria de proyectos, un grupo presenta una matriz sobre un barrio inventado. ¿Qué es lo más importante que debe mostrar? A) Cómo se pasa del problema a una acción segura B) Fotos de personas", "A", "El método es el aprendizaje.")],
    selfcheck=[ex("En Orientación: ¿un diagnóstico describe un problema antes de actuar?", "Sí", "Ordena la información."), ex("¿Se usan nombres reales en la matriz?", "No", "Se protege la privacidad."), ex("¿La matriz incluye una acción segura?", "Sí", "Es la última columna.")],
    task=T("Completa una matriz de cinco columnas (problema, personas afectadas, derecho o principio, instancia y acción segura) para un entorno inventado de tu elección entre estos tres: (a) un barrio con una plaza sin rampa; (b) un liceo donde el cartel de salida de emergencia está roto; (c) un curso donde un grupo excluye a una persona nueva. Una de las filas debe incluir avisar a una persona adulta.", "Plaza sin rampa: afectadas, personas con movilidad reducida y familias con coches; derecho: inclusión y acceso; instancia: junta de vecinos; acción: presentar una propuesta con evidencia. Curso que excluye: afectada, la persona nueva; derecho: inclusión y dignidad; instancia: Consejo de Curso; acción: invitarla y avisar a la orientadora.", ["completa las cinco columnas", "no usa nombres reales", "una fila avisa a una persona adulta", "la acción es segura"], ["tabla escrita", "mapa"], ["usar datos personales", "olvidar la acción segura"], "Reconoce el método y pregunta cómo lo aplicaría a otro entorno."),
    reinforce="Completa la matriz para un problema inventado distinto al que elegiste.",
    extend="Explica por qué el diagnóstico evita actuar con rumores.",
)

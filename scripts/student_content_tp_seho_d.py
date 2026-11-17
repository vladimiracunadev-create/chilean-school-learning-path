"""Hotelería TP 3.º y 4.º medio: OAE-07 (animación y actividades recreativas seguras), OAE-08 (montaje de eventos y servicios) y OAE-09 (inglés básico para atender turistas). Todo en papel: grupos, salones, presupuestos y diálogos inventados y rotulados «de ejemplo»; sin actividades de riesgo, sin procedimientos de evacuación ni manejo de alimentos."""
from __future__ import annotations

from tp_seho_common import build

O7 = "TP-SEHO-3y4-OAE-07"
O8 = "TP-SEHO-3y4-OAE-08"
O9 = "TP-SEHO-3y4-OAE-09"
LIM = " Este cuaderno trabaja en papel, con datos de ejemplo: no reemplaza la práctica con un instructor ni la norma vigente."
SEG = " Esto es aprendizaje conceptual en papel: practicar actividades, montajes o emergencias reales exige instructor autorizado, norma vigente y elementos de protección; este cuaderno no te habilita para trabajar."

# ============================================================ OAE-07, clase 1
F = ("Ficha 29 (animación de ejemplo, inventada). «Hotel Brisa de Ejemplo» ofrece animación para sus huéspedes: familias con niños de 4 a 12 años, personas mayores y grupos de adultos. Sala de actividades con aforo máximo de 40 personas (de ejemplo) y 2 animadores. "
     "Actividades propuestas: A) juego de pistas con tarjetas dentro del salón; B) carrera de relevos en el borde de la piscina; C) baile libre con sillas en círculo. Reglas del hotel: participación voluntaria, niños con su adulto responsable, fotos solo con autorización.")
build(
    O7, 1, F,
    use="Aprenderé qué es la animación turística, cómo se adaptan las actividades a cada grupo y qué reglas de seguridad, inclusión y privacidad se respetan.",
    prior=["Sé organizar una lista de tareas.", "Sé restar y multiplicar.", "Conozco el trato respetuoso a los huéspedes."],
    explain=[
        "En Hotelería, la animación turística es el conjunto de actividades recreativas que el hotel organiza para entretener e integrar a los huéspedes. Se diseñan según el grupo: sus edades, intereses, capacidades y tiempo. Una actividad recreativa es una actividad de juego, cultura o deporte suave que se hace por gusto y no por obligación.",
        "La prevención de riesgos consiste en pensar antes qué podría salir mal (tropiezos, caídas, empujones, ruido excesivo) y tomar medidas: espacio despejado, reglas claras, supervisión suficiente y actividades adecuadas a la edad. Las actividades con agua o con esfuerzo físico exigente requieren personal capacitado y autorizado; en este cuaderno solo se trabajan actividades de bajo riesgo en sala.",
        "La participación es voluntaria, los niños participan con su adulto responsable y las fotos se toman solo con autorización. Se incluye a todas las personas, adaptando la actividad si hace falta, y nadie se burla de otra. Ante una caída o un malestar, se avisa de inmediato a personal capacitado." + SEG,
    ],
    vocab=[("animación turística", "actividades recreativas que el hotel organiza para entretener e integrar a los huéspedes"), ("actividad recreativa", "actividad de juego, cultura o deporte suave hecha por gusto"), ("prevención de riesgos", "pensar antes qué podría salir mal y tomar medidas"), ("aforo", "cantidad máxima de personas que caben de forma segura en un espacio"), ("inclusión", "adaptar la actividad para que todas las personas puedan participar"), ("voluntaria", "que cada persona decide si participa")],
    worked=[
        ("Calcular lugares libres", "Una sala de ejemplo tiene aforo de 30 personas y hay 22 inscritas. ¿Cuántas personas más caben?", ["Lugares libres = aforo − inscritas.", "30 − 22 = 8."], "8 personas"),
        ("Elegir una actividad segura", "Para un grupo de adultos mayores, ¿conviene una actividad de pie, corriendo, o una sentada con juegos de memoria?", ["Correr tiene riesgo de caídas.", "La actividad sentada es de bajo riesgo."], "La sentada con juegos de memoria"),
    ],
    mistakes=[("Proponer una carrera en el borde de una piscina para «hacer más divertido» el programa.", "El borde mojado y el agua exigen personal capacitado; hay riesgo de caídas y no es una actividad de bajo riesgo.", "Elige una actividad en sala con espacio despejado y supervisión."),
              ("Tomar fotos de los niños sin pedir permiso para subirlas a las redes del hotel.", "La imagen de una persona es un dato personal y los menores necesitan la autorización de su adulto responsable.", "Pide autorización antes de fotografiar.")],
    T=[
        ("abc", "En Hotelería: ¿qué es la animación turística?", "Actividades recreativas que organiza el hotel para entretener e integrar a los huéspedes", "El cobro de los servicios del hotel", "La limpieza de las habitaciones", "La animación organiza juegos y actividades; el cobro y la limpieza son otras áreas."),
        ("abc", "{F} ¿Cuál de las actividades propuestas no corresponde por su riesgo?", "La B, carrera de relevos en el borde de la piscina", "La A, juego de pistas en el salón", "La C, baile libre con sillas en círculo", "El borde de la piscina exige personal capacitado y tiene riesgo de caídas."),
        ("=", "{F} Hay 28 personas inscritas para la actividad. ¿Cuántas más caben en la sala según el aforo?", "40-28", "Al aforo máximo se le restan las personas inscritas.", " personas"),
        ("abc", "{F} Un adulto mayor no quiere participar. ¿Qué corresponde?", "Respetar su decisión y ofrecerle mirar o sumarse más tarde", "Insistir hasta que participe", "Hacerlo participar para dar el ejemplo", "La participación en la actividad es voluntaria para todos."),
        ("abc", "{F} Un niño de 5 años llega solo a la actividad. ¿Qué haces?", "Ubicar a su adulto responsable antes de que participe", "Dejarlo participar sin avisar a nadie", "Pedirle que se vaya a su habitación solo", "Los niños participan con su adulto responsable según la ficha."),
        ("abc", "{F} Quieres tomar fotos del grupo para el álbum del hotel. ¿Qué haces antes?", "Pedir autorización a las personas, o a su adulto responsable si son menores", "Tomar las fotos y pedir permiso después", "Tomar fotos solo a quienes sonríen", "La imagen de una persona es un dato personal y requiere autorización."),
        ("=", "{F} Si cada animador puede supervisar a 10 niños (valor de ejemplo), ¿cuántos niños pueden participar con los 2 animadores?", "2*10", "Se multiplican los animadores por los niños que puede supervisar cada uno.", " niños"),
        ("abc", "Llega a la actividad un huésped en silla de ruedas. ¿Qué haces?", "Preguntarle cómo prefiere participar y adaptar la actividad", "Decirle que mejor mire", "Darle una actividad distinta sin preguntarle", "La inclusión pide preguntar y adaptar, no suponer."),
        ("abc", "Un niño se cae y llora. ¿Qué haces?", "Avisar de inmediato a personal capacitado y a su adulto responsable", "Tratarlo por tu cuenta con lo que tengas", "Decirle que se levante y siga jugando", "Ante una caída se avisa a personal capacitado; no se improvisan curaciones."),
        ("abc", "Antes de comenzar, notas un cable suelto en el piso del salón. ¿Qué haces?", "No usar ese espacio hasta que se corrija y avisar a mantención", "Poner una alfombra encima", "Avisar al terminar la actividad", "Un riesgo se corrige antes de empezar y lo repara personal autorizado."),
        ("abc", "Un animador quiere hacer una broma sobre la apariencia de un huésped. ¿Qué corresponde?", "No hacerla: el humor debe respetar a todas las personas", "Hacerla si todos se ríen", "Hacerla solo a quienes no se ven molestos", "El trato respetuoso y sin discriminación es parte del servicio."),
        ("=", "{F} El programa va de 10:00 a 12:30 con 3 actividades de igual duración y sin pausas. ¿Cuántos minutos dura cada una?", "(12*60+30-10*60)//3", "Se calcula el total de minutos del programa y se divide por 3.", " minutos"),
        ("abc", "Suena una alarma de emergencia durante la actividad. ¿Qué corresponde?", "Seguir el plan de emergencia del hotel y las indicaciones del personal capacitado", "Inventar una ruta de salida por tu cuenta", "Terminar el juego antes de salir", "La evacuación sigue el plan del hotel y la norma vigente, con personal capacitado."),
    ],
    ctx=("abc", "{F} Llegan 3 familias con niños y 2 personas mayores y piden «algo para todos». ¿Qué actividad de la ficha propones?", "La A, juego de pistas en el salón, adaptable para todas las edades", "La B, carrera en la piscina", "Ninguna, porque no hay actividades", "Es de bajo riesgo, en sala y se adapta a todas las edades."),
    sc=[
        ("En Hotelería: ¿qué es el aforo de una sala?", "La cantidad máxima de personas que caben de forma segura", "Pasarse del aforo pone en riesgo a las personas."),
        ("¿Qué haces si una persona no quiere participar?", "Respeto su decisión", "La participación en la actividad es siempre voluntaria."),
        ("¿Qué haces antes de tomar fotos?", "Pido autorización", "La imagen es un dato personal."),
    ],
    op=("Un hotel de ejemplo recibe un grupo de tarde: 10 niños de 6 a 11 años con sus adultos, 4 adultos mayores y 1 persona con muletas. Sala con aforo de 30 personas (los adultos de los niños también cuentan: 10 adultos). 2 animadores. "
        "Escribe: cuántas personas hay en total y si caben en la sala, una actividad de bajo riesgo para todos con una razón, una medida de prevención de riesgos, y una regla de inclusión o de privacidad.",
        "Total: 10 + 10 + 4 + 1 = 25 personas, que caben en el aforo de 30. Actividad: un juego de pistas en sala con tarjetas, porque se hace caminando y se adapta a todas las edades. Prevención: piso despejado y reglas de caminar, no correr. Inclusión: preguntar a la persona con muletas cómo prefiere participar; privacidad: pedir autorización antes de las fotos.",
        ["calcula el total y compara con el aforo", "propone una actividad de bajo riesgo con razón", "incluye una medida de prevención y una de inclusión o privacidad"],
        ["hoja con el cálculo, la actividad, la medida y la regla"],
        ["olvidar contar a los adultos", "proponer actividades con carreras o agua", "no incluir a la persona con muletas"],
        "Pregunta: «¿cuántas personas entran a la sala?». Si no cuenta a los adultos, repasa el aforo."),
    reinforce="Escribe tres riesgos posibles en una actividad en sala y una medida para cada uno.",
    extend="Explica por qué la participación voluntaria hace que una actividad sea más agradable para todos.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 30 (ficha de actividad de ejemplo, inventada). Nombre: Bingo de pistas. Público: familias con niños de 6 a 12 años. Duración: 45 minutos. Lugar: salón con aforo de 40 personas. Materiales: 20 tarjetas de papel y lápices. Personal: 2 animadores. "
     "Riesgo y medida: tropiezos; piso despejado y se camina, no se corre. Participación voluntaria. Evaluación: encuesta de 3 preguntas al final. Cada ronda del juego dura 9 minutos.")
build(
    O7, 2, F,
    use="Aprenderé los documentos y técnicas de la animación: ficha de actividad, programa, lista de asistentes, instrucciones claras y rompehielos.",
    prior=["Conozco la prevención de riesgos.", "Sé dividir y sumar.", "Sé explicar algo en pasos."],
    explain=[
        "Cada actividad se registra en una ficha de actividad: nombre, público, duración, lugar, materiales, personal, riesgos con sus medidas y forma de evaluar. El programa es el horario que reúne todas las actividades del día o de la semana. La lista de asistentes anota quiénes participan, para controlar el aforo y a los menores.",
        "Las técnicas comunicativas del animador son hablar con voz clara, dar instrucciones en pasos cortos (por ejemplo, un máximo de tres), demostrar lo que se pide y preguntar si todos entendieron. El rompehielos es una actividad breve para que los participantes se conozcan y se relajen. El refuerzo positivo es felicitar con respeto el esfuerzo, sin comparar ni burlarse.",
        "Al final, la evaluación (por ejemplo, una encuesta breve) permite saber qué mejorar. Los datos de los participantes son personales y se manejan con discreción." + SEG,
    ],
    vocab=[("ficha de actividad", "documento con nombre, público, duración, materiales, riesgos y evaluación de una actividad"), ("programa", "horario que reúne las actividades del día o de la semana"), ("lista de asistentes", "anotación de quiénes participan en una actividad"), ("rompehielos", "actividad breve para que los participantes se conozcan"), ("refuerzo positivo", "felicitar con respeto el esfuerzo de las personas"), ("evaluación", "forma de saber cómo resultó la actividad")],
    worked=[
        ("Dividir en equipos", "Una actividad de ejemplo tiene 24 tarjetas y se reparten 6 por equipo. ¿Cuántos equipos hay?", ["Equipos = tarjetas ÷ tarjetas por equipo.", "24 ÷ 6 = 4."], "4 equipos"),
        ("Dar instrucciones", "¿Qué es mejor para explicar un juego: un párrafo largo de memoria o tres pasos cortos con una demostración?", ["Las personas recuerdan mejor pasos breves.", "La demostración muestra lo que se pide."], "Tres pasos cortos con demostración"),
    ],
    mistakes=[("Dar las instrucciones de un juego muy rápido y en un solo párrafo largo.", "Los participantes, sobre todo los niños, no recuerdan todo y se confunden.", "Usa pasos cortos, demuestra y pregunta si todos entendieron."),
              ("Usar el nombre completo y el teléfono de los niños en una lista pegada en la pared.", "Se exponen datos personales de menores.", "Usa solo lo necesario y guarda la lista en lugar reservado.")],
    T=[
        ("abc", "En Hotelería: ¿qué es un rompehielos?", "Una actividad breve para que los participantes se conozcan y se relajen", "Una regla de seguridad del salón", "La lista de materiales", "El rompehielos ayuda a integrar al grupo al comienzo."),
        ("abc", "{F} ¿Cuánto dura la actividad completa?", "45 minutos", "9 minutos", "60 minutos", "La ficha fija 45 minutos; 9 minutos es lo que dura cada ronda."),
        ("abc", "{F} ¿Qué riesgo se identificó y qué medida se tomó?", "Tropiezos; piso despejado y caminar sin correr", "Quemaduras; usar guantes", "Ruido; apagar la luz", "La ficha menciona tropiezos y la medida de mantener el piso despejado."),
        ("=", "{F} Se reparten las 20 tarjetas en equipos de 4 tarjetas cada uno. ¿Cuántos equipos hay?", "20//4", "Se divide el total de tarjetas por las de cada equipo.", " equipos"),
        ("=", "{F} Si no hay pausas, ¿cuántas rondas completas de 9 minutos caben en la actividad?", "45//9", "Se divide la duración total por la duración de una ronda.", " rondas"),
        ("abc", "{F} Si la actividad comienza a las 16:15, ¿a qué hora termina?", "A las 17:00", "A las 16:45", "A las 17:15", "A las 16:15 se suman 45 minutos y resulta 17:00."),
        ("abc", "¿Cuál es una buena forma de dar instrucciones a niños?", "Pasos cortos, con voz clara y una demostración", "Un párrafo largo sin pausas", "Gritando para que oigan", "Los pasos cortos y la demostración ayudan a recordar."),
        ("abc", "Un niño dice que no entendió el juego. ¿Qué respondes?", "Repetir de forma sencilla y mostrarle cómo se hace", "Decirle que preste atención", "Pedirle que mire a los demás sin explicarle", "Repetir y demostrar respeta su ritmo."),
        ("abc", "¿Qué frase es un refuerzo positivo?", "«¡Buen trabajo en equipo!»", "«Ustedes son muy lentos»", "«Así no, está mal»", "El refuerzo positivo reconoce el esfuerzo sin comparar."),
        ("abc", "{F} Dos niños empiezan a correr por el salón. ¿Qué corresponde?", "Recordar con calma la regla de caminar y mostrar cómo hacerlo", "Dejar que corran", "Retarlos frente a los demás", "La regla de caminar es la medida de la ficha."),
        ("abc", "{F} ¿Para qué sirve la encuesta de 3 preguntas al final?", "Para saber qué mejorar de la actividad", "Para cobrar a los participantes", "Para decidir quién gana", "La evaluación permite mejorar las próximas actividades."),
        ("abc", "Un huésped pide la lista de asistentes para saber quiénes participaron. ¿Qué respondes?", "Que la lista es reservada y no se entrega a terceros", "Que sí, porque son sus vecinos", "Que se la fotografíe si quiere", "Los datos de los participantes son personales."),
        ("abc", "{F} Un adulto quiere participar en la actividad pensada para niños de 6 a 12 años. ¿Qué haces?", "Consultar al responsable y ver cómo adaptarla de forma segura", "Impedirle participar siempre", "Cambiar las reglas sin consultar a nadie", "Las adaptaciones se evalúan y no se improvisan."),
    ],
    ctx=("abc", "{F} A mitad de la actividad, la mayoría de los niños se aburre. ¿Qué haces?", "Cambiar a un rompehielos breve o ajustar la ronda, y registrar lo ocurrido para mejorar", "Seguir igual hasta el final", "Terminar de inmediato sin explicar", "Se adapta con flexibilidad y se registra para mejorar."),
    sc=[
        ("En Hotelería: ¿qué contiene una ficha de actividad?", "Nombre, público, duración, materiales, riesgos y evaluación", "Reúne lo necesario para organizar la actividad."),
        ("¿Cómo se dan buenas instrucciones?", "En pasos cortos y con una demostración", "Así los participantes entienden y recuerdan."),
        ("¿Para qué sirve el rompehielos?", "Para integrar al grupo", "Ayuda a que los participantes se conozcan."),
    ],
    op=("Ficha de ejemplo: «Mímica por equipos». Público: adultos y jóvenes. Duración: 40 minutos. Aforo de la sala: 36 personas. Hay 24 inscritas. Cada ronda dura 8 minutos. Materiales: 30 tarjetas con palabras. "
        "Calcula: cuántas rondas caben, cuántas personas más caben, y escribe tres pasos cortos para explicar el juego, un riesgo con su medida y cómo evaluarías la actividad.",
        "Rondas: 40 ÷ 8 = 5. Lugares libres: 36 − 24 = 12. Pasos: 1) Formamos equipos; 2) Una persona actúa la palabra sin hablar; 3) Su equipo adivina antes de que termine la ronda. Riesgo: tropiezos, con piso despejado. Evaluación: encuesta breve de tres preguntas al final.",
        ["calcula rondas y lugares libres", "da tres pasos cortos y claros", "incluye riesgo, medida y evaluación"],
        ["hoja con cálculos, pasos, riesgo y evaluación"],
        ["dar instrucciones largas", "olvidar la medida de prevención", "no evaluar"],
        "Pregunta: «¿cómo sabrías si la actividad resultó?». Si no menciona la evaluación, repasa la ficha."),
    reinforce="Escribe una ficha de actividad con nombre, público, duración, materiales y un riesgo con su medida.",
    extend="Explica por qué un buen rompehielos mejora el resto de la actividad.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 31 (caso de ejemplo, inventado). Grupo de la tarde: 12 niños de 4 a 12 años, 8 adultos, 4 adultos mayores y 1 huésped en silla de ruedas. Salón con aforo de 40 personas (de ejemplo). 2 animadores. "
     "Opciones: A) carrera de relevos corriendo por el salón; B) bingo de pistas con tarjetas grandes, que se puede hacer sentado o caminando; C) búsqueda del tesoro por todo el hotel, 90 minutos, con escaleras.")
build(
    O7, 3, F,
    use="Aprenderé a analizar un grupo mixto de huéspedes y a elegir y adaptar una actividad que sea segura, inclusiva y adecuada para todos.",
    prior=["Conozco la ficha de actividad.", "Conozco la prevención de riesgos.", "Sé comparar opciones con requisitos."],
    explain=[
        "Para analizar un grupo se cuenta cuántas personas son, qué edades tienen y si alguien necesita apoyo para participar. Con esos datos se comparan las actividades posibles frente a las características del grupo: aforo, duración, esfuerzo físico, accesibilidad y riesgo. Se descarta la actividad que deja a alguien afuera o que pone en riesgo a alguien.",
        "Una actividad inclusiva se puede hacer de distintas maneras, de modo que cada persona participe a su ritmo y con sus capacidades. Por ejemplo, un juego se puede hacer sentado o caminando. Se pregunta a cada persona cómo prefiere participar y no se la obliga ni se la excluye.",
        "Una vez elegida la actividad, se confirma que cumple el aforo, que haya suficientes animadores, que el espacio sea seguro y que se avise a los participantes de las reglas. Ante cualquier accidente, se avisa a personal capacitado." + SEG,
    ],
    vocab=[("grupo mixto", "grupo con personas de distintas edades y capacidades"), ("actividad inclusiva", "actividad que se puede hacer de distintas maneras para que todos participen"), ("accesibilidad", "facilidad con que cualquier persona puede llegar y usar un lugar o actividad"), ("esfuerzo físico", "cuánto trabajo corporal exige una actividad"), ("descartar", "dejar de considerar una opción porque no cumple un requisito")],
    worked=[
        ("Contar participantes", "Un grupo de ejemplo tiene 9 niños y 6 adultos. ¿Cuántas personas son?", ["Se suman los dos grupos.", "9 + 6 = 15."], "15 personas"),
        ("Descartar una opción", "Una actividad de ejemplo exige subir escaleras y en el grupo hay una persona en silla de ruedas. ¿Qué se hace?", ["La persona no podría participar.", "Se descarta o se adapta."], "Se descarta esa opción o se adapta"),
    ],
    mistakes=[("Elegir la actividad más emocionante sin mirar si todas las personas pueden participar.", "Alguien queda afuera o se expone a un riesgo.", "Compara cada opción con las características del grupo antes de elegir."),
              ("Preguntar frente a todos a una persona qué le «pasa» para participar.", "La expone y puede incomodarla.", "Pregúntale en privado cómo prefiere participar.")],
    T=[
        ("abc", "En Hotelería: ¿qué es una actividad inclusiva?", "Una actividad que se puede hacer de distintas maneras para que todos participen", "Una actividad solo para quienes corren rápido", "Una actividad que cobra más", "La inclusión adapta la actividad a las capacidades de cada persona."),
        ("=", "{F} ¿Cuántas personas participan en total?", "12+8+4+1", "Se suman niños, adultos, adultos mayores y la persona en silla de ruedas.", " personas"),
        ("=", "{F} ¿Cuántos lugares libres quedan según el aforo?", "40-(12+8+4+1)", "Al aforo se le restan las personas que participan.", " personas"),
        ("abc", "{F} ¿Por qué se descarta la opción A?", "Porque exige correr y hay riesgo de caídas para varias personas", "Porque dura 90 minutos", "Porque incluye escaleras", "La carrera con tantos niños y personas mayores tiene riesgo de caídas."),
        ("abc", "{F} ¿Por qué se descarta la opción C?", "Porque tiene escaleras y una persona del grupo usa silla de ruedas", "Porque se puede hacer sentado y a ritmo propio", "Porque solo pueden participar los niños", "Las escaleras impiden participar a la persona en silla de ruedas."),
        ("abc", "{F} ¿Qué opción conviene para este grupo?", "La B, porque se hace sentado o caminando", "La A, porque es la más divertida", "La C, porque dura más", "La B se adapta a niños, adultos mayores y a la persona en silla de ruedas."),
        ("=", "{F} Si cada animador supervisa como máximo a 15 participantes (valor de ejemplo), ¿cuántos participantes pueden supervisar los 2 animadores?", "2*15", "Se multiplican los animadores por los participantes que supervisa cada uno.", " participantes"),
        ("abc", "{F} Si cada animador supervisa como máximo a 15 participantes, ¿alcanzan los 2 animadores para el grupo de 25 personas?", "Sí, porque supervisan hasta 30 y el grupo es de 25", "No, porque el grupo es de 40", "No se puede saber", "Con capacidad para 30 participantes, el grupo de 25 queda cubierto."),
        ("abc", "{F} Una persona mayor dice que prefiere solo mirar. ¿Qué haces?", "Respetar su decisión y ofrecerle participar cuando quiera", "Insistir en que participe", "Cambiar la actividad por una que no le gusta", "La participación es voluntaria y se respeta."),
        ("abc", "{F} El huésped en silla de ruedas llega y el salón tiene un escalón en la entrada. ¿Qué haces?", "Ofrecer otro acceso sin escalón o una rampa, y avisar a quien corresponda", "Pedirle que no venga", "Dejarlo esperando afuera", "La accesibilidad es parte del servicio."),
        ("abc", "{F} Un niño se queja de que un adulto se burla de otro participante. ¿Qué haces?", "Recordar con calma las reglas de respeto y cuidar que todos se sientan bien", "Reírte con el grupo", "Ignorar la queja", "La burla no se permite; el respeto es una regla de la actividad."),
        ("abc", "{F} A mitad de la actividad un adulto mayor refiere sentirse mareado. ¿Qué haces?", "Hacerlo sentar y avisar de inmediato a personal capacitado", "Darle un remedio que llevas", "Decirle que siga participando", "Ante un malestar, se avisa a personal capacitado."),
        ("=", "{F} La actividad B dura 45 minutos y cada ronda dura 9 minutos. ¿Cuántas rondas completas caben?", "45//9", "Se divide la duración total por la duración de cada ronda.", " rondas"),
    ],
    ctx=("abc", "{F} Un niño de 4 años quiere participar solo y su adulto responsable no está. ¿Qué haces?", "Pedirle que espere con un animador mientras se busca a su adulto, y no dejarlo solo", "Dejarlo participar solo", "Pedirle que vuelva en una hora", "Los menores participan con su adulto responsable; se busca a esa persona."),
    sc=[
        ("En Hotelería: ¿cómo se elige una actividad para un grupo mixto?", "Comparando cada opción con las características del grupo", "Así se descarta lo que deja afuera o expone a alguien."),
        ("¿Qué haces si una opción deja a alguien afuera?", "Se descarta o se adapta", "Todos los participantes deben poder participar sin riesgo."),
        ("¿Qué haces ante un mareo de un participante?", "Aviso a personal capacitado", "No se medica ni se improvisa."),
    ],
    op=("Caso de ejemplo. Grupo: 8 niños de 5 a 9 años, 6 adultos, 3 adultos mayores y 1 persona con muletas. Sala de aforo 25. 2 animadores. Opciones: X) juego de saltos sobre aros en el piso; Y) concurso de preguntas y respuestas por equipos, sentados; Z) caminata de 2 horas por un sendero. "
        "Cuenta los participantes, di si caben, elige una opción con tres razones, y escribe una adaptación o regla de inclusión.",
        "Participantes: 8 + 6 + 3 + 1 = 18, que caben en 25. Elijo Y porque se hace sentado, no exige esfuerzo físico fuerte y todos pueden participar. X exige saltar y Z dura 2 horas. Adaptación: formar equipos mixtos y preguntar a cada persona cómo prefiere participar.",
        ["cuenta bien y compara con el aforo", "elige con razones del grupo", "incluye una adaptación"],
        ["hoja con conteo, elección con razones y adaptación"],
        ["elegir X o Z", "no contar a la persona con muletas", "no incluir ninguna adaptación"],
        "Pregunta: «¿por qué no X?». Si no menciona el esfuerzo o el riesgo de caídas, repasa la prevención."),
    reinforce="Inventa un grupo de 15 personas con edades distintas y elige una actividad adecuada con una razón.",
    extend="Explica por qué preguntar a la persona cómo prefiere participar es mejor que suponerlo.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 32 (recursos de una actividad de ejemplo, inventada). Concurso de preguntas por equipos para 36 participantes, en equipos de 4 personas. Cada equipo recibe 1 sobre con 6 pistas. Cada participante recibe 1 lápiz. 36 sillas en círculos. "
     "Premios simbólicos de ejemplo: $400 por participante. Tiempos: explicación 10 minutos, juego 35 minutos y cierre 10 minutos. Comienza a las 17:00. Presupuesto máximo de la actividad: $20.000.")
build(
    O7, 4, F,
    use="Aprenderé a calcular los recursos, el tiempo y el presupuesto de una actividad recreativa y a comprobar que se puede realizar de forma segura.",
    prior=["Conozco la ficha de actividad.", "Sé multiplicar, dividir y sumar.", "Sé calcular horas y minutos."],
    explain=[
        "Los recursos de una actividad son lo que se necesita para realizarla: materiales, espacio, personal y tiempo. Se calculan a partir del número de participantes y de equipos. Por ejemplo, si hay 36 participantes en equipos de 4, hay 36 ÷ 4 = 9 equipos. Si cada equipo recibe 6 pistas, se necesitan 9 × 6 = 54 pistas.",
        "El tiempo total es la suma de las etapas: explicación, juego y cierre. La hora de término es la hora de inicio más ese total. El presupuesto es el dinero máximo disponible; se calcula el costo (cantidad por precio) y se compara con el presupuesto para ver si alcanza.",
        "Además se verifica la seguridad: sillas ubicadas sin obstruir las salidas, piso despejado y materiales sin riesgo. Si algo no alcanza, se ajusta antes de comenzar." + SEG,
    ],
    vocab=[("recursos", "lo que se necesita para realizar una actividad: materiales, espacio, personal y tiempo"), ("presupuesto", "dinero máximo disponible para una actividad"), ("costo", "dinero que cuesta realizar algo"), ("etapa", "parte de una actividad con un tiempo propio"), ("ajustar", "cambiar algo del plan para que cumpla los límites")],
    worked=[
        ("Calcular equipos y pistas", "Una actividad de ejemplo tiene 20 participantes en equipos de 5 y cada equipo recibe 4 pistas. ¿Cuántas pistas se necesitan?", ["Equipos: 20 ÷ 5 = 4.", "Pistas: 4 × 4 = 16."], "16 pistas"),
        ("Calcular la hora de término", "Una actividad de ejemplo comienza a las 15:00 y tiene etapas de 10, 30 y 5 minutos. ¿A qué hora termina?", ["Total: 10 + 30 + 5 = 45 minutos.", "15:00 + 45 minutos = 15:45."], "15:45"),
    ],
    mistakes=[("Calcular los lápices por equipo en vez de por participante.", "Faltan lápices y el juego se detiene.", "Revisa en la ficha si el recurso se entrega por persona o por equipo."),
              ("Olvidar sumar la etapa de cierre al calcular la hora de término.", "El grupo termina más tarde de lo avisado.", "Suma todas las etapas antes de informar la hora.")],
    T=[
        ("abc", "En Hotelería: ¿qué son los recursos de una actividad?", "Lo que se necesita para realizarla: materiales, espacio, personal y tiempo", "Solo el dinero que se cobra", "Los nombres de los participantes", "Los recursos abarcan todo lo necesario, no solo el dinero."),
        ("=", "{F} ¿Cuántos equipos hay?", "36//4", "Se divide el total de participantes por las personas de cada equipo.", " equipos"),
        ("=", "{F} ¿Cuántas pistas se necesitan en total?", "36//4*6", "Se multiplican los equipos por las pistas de cada sobre.", " pistas"),
        ("=", "{F} Si se alistan 4 lápices de repuesto además de uno por participante, ¿cuántos lápices se preparan?", "36+4", "Se suma un lápiz por participante y los de repuesto.", " lápices"),
        ("=", "{F} ¿Cuántos minutos dura la actividad completa?", "10+35+10", "Se suman las tres etapas de la actividad.", " minutos"),
        ("abc", "{F} ¿A qué hora termina la actividad?", "A las 17:55", "A las 17:45", "A las 18:05", "A las 17:00 se suman 55 minutos y resulta 17:55."),
        ("=", "{F} ¿Cuánto cuestan los premios para todos los participantes?", "36*400", "Se multiplican los participantes por el valor del premio.", " pesos"),
        ("abc", "{F} ¿Alcanza el presupuesto para los premios?", "Sí, porque cuestan $14.400 y el máximo es $20.000", "No, porque cuestan más de $20.000", "No se puede saber", "Los premios cuestan menos que el presupuesto máximo."),
        ("=", "{F} ¿Cuánto dinero sobra del presupuesto después de pagar los premios?", "20000-36*400", "Al presupuesto máximo se le resta el costo de los premios.", " pesos"),
        ("abc", "{F} Se agregan 4 participantes (un equipo más). ¿Alcanzan las 36 sillas?", "No: harían falta 40 sillas", "Sí, alcanzan las mismas", "Sobrarían 4 sillas", "Con 40 participantes se necesitan 40 sillas."),
        ("abc", "{F} Un compañero propone colocar sillas extra bloqueando una de las salidas. ¿Qué respondes?", "Que no: las salidas deben quedar despejadas", "Que sí, mientras haya espacio", "Que sí, si es por poco tiempo", "Las salidas despejadas son una regla básica de seguridad."),
        ("abc", "{F} El presupuesto cae a $12.000. ¿Qué ajuste mantiene la actividad?", "Reducir el costo de los premios o dar premios más simples", "Dejar sin premio a algunos equipos sin avisarles", "Cobrar un extra a los participantes sin informarles antes", "Se ajusta el gasto sin afectar la seguridad."),
        ("=", "{F} Con premios de $300 por participante, ¿cuánto sobraría de los $20.000?", "20000-36*300", "Se calcula el costo con el nuevo valor y se resta del presupuesto.", " pesos"),
    ],
    ctx=("abc", "{F} A los 10 minutos del juego, un equipo pierde su sobre de pistas. ¿Qué haces?", "Tener un sobre de repuesto y entregárselo, sin culpar al equipo", "Eliminar al equipo", "Terminar la actividad", "Un sobre de repuesto mantiene la actividad y el buen trato."),
    sc=[
        ("En Hotelería: ¿cómo se calcula la cantidad de equipos?", "Participantes divididos por personas de cada equipo", "Así se sabe cuántos equipos formar."),
        ("¿Cómo se calcula la hora de término?", "Hora de inicio más la duración total", "La duración total suma todas las etapas."),
        ("¿Qué haces si el costo supera el presupuesto?", "Ajusto el plan", "No se puede gastar más de lo disponible."),
    ],
    op=("Ficha de ejemplo. Bingo de pistas para 30 participantes en equipos de 5; cada equipo recibe 8 tarjetas; hay un lápiz por participante; premios de $500 por participante; presupuesto máximo de $18.000. Etapas: 8 minutos de explicación, 30 de juego y 7 de cierre; comienza a las 16:00. "
        "Calcula equipos, tarjetas, lápices, costo de premios, si alcanza el presupuesto y la hora de término.",
        "Equipos: 30 ÷ 5 = 6. Tarjetas: 6 × 8 = 48. Lápices: 30. Premios: 30 × 500 = 15.000, que no supera 18.000 y deja 3.000. Duración: 8 + 30 + 7 = 45 minutos; termina a las 16:45.",
        ["calcula equipos, tarjetas y lápices", "compara el costo con el presupuesto", "calcula la hora de término"],
        ["hoja con los cálculos"],
        ["calcular tarjetas por participante", "no sumar el cierre", "olvidar comparar con el presupuesto"],
        "Pregunta: «¿por qué 6 equipos?». Si no responde 30 ÷ 5, repasa la división en equipos."),
    reinforce="Inventa una actividad para 24 personas y calcula equipos, materiales y duración.",
    extend="Explica por qué conviene tener materiales de repuesto en una actividad con muchos participantes.",
)

# ============================================================ OAE-07, clase 5
F = ("Ficha 33 (dos opciones de ejemplo, inventadas). Opción X: gincana en sala, 60 minutos, costo $18.000, accesible, se realiza con cualquier clima. Opción Y: caminata al mirador, 150 minutos, costo $0, con escalones, requiere guía autorizado y buen clima. "
     "Requisitos del grupo: duración máxima de 90 minutos, presupuesto máximo de $25.000, accesible para una persona con bastón, y hoy se pronostica lluvia. Encuesta de la actividad de ayer: 30 respondieron y 24 se declararon satisfechos.")
build(
    O7, 5, F,
    use="Aprenderé a comparar dos actividades con los requisitos del grupo, elegir la más adecuada y evaluar una actividad con una encuesta de satisfacción.",
    prior=["Conozco recursos y presupuesto.", "Sé calcular un porcentaje exacto.", "Conozco la prevención de riesgos."],
    explain=[
        "Comparar alternativas es contrastar cada actividad con los requisitos del grupo: duración, presupuesto, accesibilidad, clima y seguridad. Una actividad que incumple un requisito se descarta aunque sea atractiva. Si ninguna cumple, se ajusta una o se busca otra.",
        "Para evaluar una actividad se usa una encuesta de satisfacción: se pregunta a los participantes si quedaron conformes. El porcentaje de satisfechos es satisfechos × 100 ÷ respuestas. También se anota lo que salió bien, lo que se puede mejorar y los incidentes, como una caída o un reclamo.",
        "La evaluación se comparte con el equipo para aprender y mejorar, sin culpar a nadie. Los comentarios de los participantes se tratan con respeto." + SEG,
    ],
    vocab=[("requisito", "condición que la actividad elegida debe cumplir"), ("encuesta de satisfacción", "preguntas a los participantes para saber si quedaron conformes"), ("porcentaje de satisfechos", "satisfechos × 100 ÷ total de respuestas"), ("incidente", "hecho inesperado durante la actividad, como una caída o un reclamo"), ("mejora", "cambio que se propone para hacerlo mejor")],
    worked=[
        ("Descartar por un requisito", "Un grupo de ejemplo tiene 60 minutos y una actividad dura 90. ¿Cumple?", ["Se compara la duración con el tiempo disponible.", "90 es mayor que 60."], "No cumple y se descarta"),
        ("Calcular un porcentaje", "En una encuesta de ejemplo, 18 de 20 personas quedaron satisfechas. ¿Qué porcentaje es?", ["18 × 100 ÷ 20 = 90.", "Es el 90 %."], "90 %"),
    ],
    mistakes=[("Elegir la actividad gratis sin mirar si cumple el clima y la accesibilidad.", "El bajo costo no compensa que no se pueda realizar o que deje a alguien afuera.", "Verifica todos los requisitos antes de comparar el costo."),
              ("Leer solo los comentarios positivos de la encuesta.", "Se pierde información útil para mejorar.", "Lee todos los comentarios con respeto, también los críticos.")],
    T=[
        ("abc", "En Hotelería: ¿qué es un requisito de una actividad?", "Una condición que la actividad elegida debe cumplir", "El nombre de la actividad", "El precio que paga el animador", "Un requisito es una condición del grupo que se verifica."),
        ("abc", "{F} ¿Qué opción cumple la duración máxima de 90 minutos?", "La X, de 60 minutos", "La Y, de 150 minutos", "Ambas", "La Y dura más que el máximo permitido."),
        ("abc", "{F} ¿Qué opción cumple el presupuesto de $25.000?", "Ambas cumplen", "Solo la X", "Ninguna", "La X cuesta 18.000 y la Y cuesta 0; ambas son menores que 25.000."),
        ("abc", "{F} ¿Qué opción es accesible para una persona con bastón?", "La X, accesible", "La Y, con escalones", "Ambas", "La Y tiene escalones; la X es accesible."),
        ("abc", "{F} Se pronostica lluvia. ¿Qué opción se puede realizar?", "La X, que se hace con cualquier clima", "La Y, que requiere buen clima", "Ambas", "La Y requiere buen clima y hoy se pronostica lluvia."),
        ("abc", "{F} ¿Qué opción se elige?", "La X", "La Y", "Ninguna", "La X cumple todos los requisitos y la Y incumple varios."),
        ("=", "{F} ¿Cuánto presupuesto sobra con la opción X?", "25000-18000", "Al presupuesto máximo se le resta el costo de la actividad.", " pesos"),
        ("=", "{F} ¿Qué porcentaje de satisfechos tuvo la actividad de ayer?", "24*100//30", "Se multiplican los satisfechos por 100 y se dividen por las respuestas.", " %"),
        ("=", "{F} ¿Cuántas personas de la encuesta no se declararon satisfechas?", "30-24", "Al total de respuestas se le restan los satisfechos.", " personas"),
        ("abc", "{F} Un comentario crítico dice que «las instrucciones fueron confusas». ¿Qué haces?", "Tomarlo como una oportunidad de mejora y revisar cómo se dan las instrucciones", "Ignorarlo porque fue un solo comentario", "Buscar a quien lo escribió para reclamarle", "Un comentario crítico ayuda a mejorar."),
        ("abc", "{F} Un animador propone elegir la opción Y «porque es gratis». ¿Qué respondes?", "Que la Y incumple la duración, la accesibilidad y el clima", "Que tiene razón: lo gratis siempre conviene", "Que se cambie el clima", "Una opción gratuita que incumple requisitos se descarta."),
        ("abc", "{F} Durante la actividad ocurrió un incidente leve: un niño se tropezó. ¿Qué anotas en la evaluación?", "El incidente, lo que se hizo y cómo evitarlo la próxima vez", "Nada, porque fue leve", "Quién tuvo la culpa", "Se registra para aprender y prevenir."),
        ("=", "{F} Si mañana 27 de 30 se declaran satisfechos, ¿cuántos puntos porcentuales sube respecto de ayer?", "27*100//30-24*100//30", "Se restan los dos porcentajes de satisfacción.", " puntos porcentuales"),
    ],
    ctx=("abc", "{F} En la mañana el día amanece despejado y alguien propone cambiar a la opción Y. Tú sabes que sigue sin cumplir la accesibilidad y la duración. ¿Qué haces?", "Mantener la X y explicar con respeto que la Y sigue incumpliendo requisitos", "Cambiar a la Y de todas formas", "No decidir nada", "El clima no resuelve los otros requisitos incumplidos."),
    sc=[
        ("En Hotelería: ¿cómo se calcula el porcentaje de satisfechos?", "Satisfechos por 100, dividido por las respuestas", "Es la parte respecto del total."),
        ("¿Qué haces con una opción que incumple un requisito?", "La descarto", "Por atractiva que sea, no cumple lo necesario."),
        ("¿Para qué sirven los comentarios críticos?", "Para mejorar", "Muestran con claridad qué conviene cambiar."),
    ],
    op=("Opciones de ejemplo para un grupo con presupuesto máximo de $20.000, 60 minutos y una persona en silla de ruedas, con lluvia. Opción P: concurso de talentos en sala, 50 minutos, $12.000, accesible. Opción Q: paseo en bicicleta, 60 minutos, $9.000, no accesible, solo con buen clima. "
        "Encuesta de la semana anterior: 20 respuestas, 16 satisfechas. Elige una opción verificando los requisitos y calcula el porcentaje de satisfacción y lo que sobra del presupuesto.",
        "P cumple duración (50 ≤ 60), presupuesto (12.000 ≤ 20.000), accesibilidad y lluvia. Q no es accesible ni sirve con lluvia. Elijo P. Sobran 20.000 − 12.000 = 8.000. Satisfacción: 16 × 100 ÷ 20 = 80 %.",
        ["verifica los cuatro requisitos", "elige con razón", "calcula presupuesto y porcentaje"],
        ["tabla de requisitos, elección y dos cálculos"],
        ["elegir Q por precio", "olvidar la lluvia", "calcular mal el porcentaje"],
        "Pregunta: «¿por qué no Q?». Si no menciona accesibilidad y lluvia, repasa los requisitos."),
    reinforce="Escribe tres requisitos de un grupo inventado y evalúa dos actividades.",
    extend="Explica por qué registrar los incidentes ayuda a prevenir accidentes futuros.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 34 (evento de ejemplo, inventado). Reunión de una empresa de ejemplo con 60 invitados en el «Salón Mar» del Hotel Brisa de Ejemplo. Aforo máximo del salón: 80 personas (valor de ejemplo; en la práctica lo fija la norma vigente para cada recinto). "
     "El salón tiene 2 salidas señalizadas que deben quedar siempre despejadas. Horario: ingreso 09:00, inicio 09:30, pausa de café 11:00, término 12:30. El cliente pide proyector y micrófono.")
build(
    O8, 1, F,
    use="Aprenderé qué es el montaje de un evento, qué información entrega el cliente y qué reglas generales de seguridad, higiene y prevención se aplican.",
    prior=["Sé leer un horario.", "Sé restar y multiplicar.", "Conozco la prevención de riesgos."],
    explain=[
        "En Hotelería, el montaje de un evento es disponer el salón, los equipos, los implementos (mesas, sillas, manteles, vajilla) y los ornamentos (adornos) según el objetivo del evento, el programa y lo que pide el cliente. Un evento puede ser una reunión, una celebración o un banquete. El programa es el horario de todo lo que ocurrirá.",
        "Hay reglas generales de seguridad: respetar el aforo del salón (el máximo de personas), mantener las salidas y pasillos despejados, no cruzar cables por donde se camina y pedir ayuda para mover objetos pesados. Los equipos eléctricos y las instalaciones los revisa personal autorizado. En la alimentación se cumple la normativa sanitaria: manos limpias, alimentos manejados por personal capacitado y respeto de las indicaciones del hotel.",
        "Quien monta un evento también cuida la accesibilidad: pasillos anchos y espacio para personas en silla de ruedas. La evacuación y el combate de incendios se aprenden con instructor autorizado y la norma vigente." + SEG,
    ],
    vocab=[("montaje", "disposición del salón, equipos e implementos para un evento"), ("implemento", "objeto necesario, como mesas, sillas, manteles o vajilla"), ("ornamento", "adorno que decora el evento"), ("programa del evento", "horario de lo que ocurrirá durante el evento"), ("aforo", "cantidad máxima de personas que pueden estar de forma segura en un salón"), ("salida despejada", "salida libre de objetos que impidan evacuar")],
    worked=[
        ("Calcular lugares libres", "Un salón de ejemplo tiene aforo de 50 personas y esperan 38. ¿Cuántos lugares quedan libres según el aforo?", ["Lugares = aforo − invitados.", "50 − 38 = 12."], "12 lugares"),
        ("Proteger una salida", "Se propone poner mesas frente a una salida señalizada «para ganar espacio». ¿Qué corresponde?", ["Las salidas deben quedar despejadas.", "Se busca otro lugar para las mesas."], "No hacerlo: la salida debe quedar libre"),
    ],
    mistakes=[("Poner sillas en el pasillo central para que quepan más invitados.", "Se bloquea la circulación y se supera una distribución segura.", "Respeta el aforo y deja los pasillos libres."),
              ("Cruzar un cable de extensión por el pasillo sin cubrirlo ni avisar.", "Puede causar un tropiezo o una falla; la instalación eléctrica es de personal autorizado.", "Pide a mantención que ubique la fuente de energía de forma segura.")],
    T=[
        ("abc", "En Hotelería: ¿qué es el montaje de un evento?", "Disponer el salón, equipos e implementos según el programa y lo que pide el cliente", "Cobrar a los invitados", "Limpiar las habitaciones", "El montaje organiza el espacio y los recursos del evento."),
        ("abc", "{F} ¿Cuál es el aforo máximo del salón?", "80 personas", "60 personas", "30 personas", "La ficha fija 80; 60 es el número de invitados."),
        ("=", "{F} ¿Cuántas personas más podrían entrar según el aforo?", "80-60", "Al aforo se le restan los invitados.", " personas"),
        ("abc", "{F} ¿Qué debe pasar con las 2 salidas señalizadas?", "Quedar siempre despejadas", "Usarse como bodega", "Cerrarse durante el evento", "La ficha manda mantenerlas siempre libres y despejadas."),
        ("=", "{F} ¿Cuántos minutos hay entre el inicio del evento y la pausa de café?", "(11*60)-(9*60+30)", "Se restan a la hora del café, en minutos, los minutos del inicio.", " minutos"),
        ("abc", "{F} El cliente pide agregar 30 invitados más. ¿Qué corresponde?", "Informar que superaría el aforo de 80 y ofrecer otra solución, como otro salón", "Aceptar sin avisar", "Poner sillas en los pasillos", "60 más 30 son 90, más que el aforo."),
        ("abc", "Un cable cruza el pasillo por donde pasarán los invitados. ¿Qué haces?", "Pedir a personal autorizado que reubique la conexión o la proteja", "Dejarlo así con cinta", "Taparlo con una alfombra suelta", "Un cable en el pasillo es un riesgo de tropiezo y lo resuelve personal autorizado."),
        ("abc", "Debes mover una mesa muy pesada sola. ¿Qué regla de ergonomía aplicas?", "Pedir ayuda para moverla", "Moverla tirando con la espalda", "Moverla rápido", "Las cargas pesadas se mueven entre varias personas."),
        ("abc", "{F} Una persona en silla de ruedas asistirá al evento. ¿Qué cuidas en el montaje?", "Dejar pasillos anchos y un lugar con espacio para ella", "Ubicarla detrás de una columna", "Pedirle que se siente en el piso", "La accesibilidad es parte del montaje."),
        ("abc", "Alguien del equipo va a manipular los alimentos de la pausa de café con las manos sucias. ¿Qué corresponde?", "Lavarse las manos antes y cumplir las indicaciones de higiene del hotel", "Seguir, porque es rápido", "Usar un delantal sucio", "La normativa sanitaria exige higiene al manipular alimentos."),
        ("abc", "Un compañero quiere probar el combate de un incendio en el salón «para estar listos». ¿Qué respondes?", "Que eso se aprende solo con instructor autorizado y la norma vigente", "Que sí, si hay mucho espacio", "Que sí, con agua", "Estas prácticas exigen instructor y norma, no se improvisan."),
        ("=", "{F} ¿Cuántos minutos dura el evento desde el inicio hasta el término?", "(12*60+30)-(9*60+30)", "Se restan los minutos del inicio a los del término.", " minutos"),
        ("abc", "{F} El cliente pide que se retire un adorno que le molesta. ¿Qué haces?", "Retirarlo con amabilidad y registrar el cambio", "Negarte porque ya está puesto", "Dejarlo sin avisar", "El montaje atiende las orientaciones del cliente cuando es seguro."),
    ],
    ctx=("abc", "{F} A las 08:45 descubres que el micrófono no funciona. ¿Qué haces?", "Avisar a mantención o al responsable de equipos y registrar la novedad", "Reparar el micrófono abriéndolo", "No decir nada y esperar", "Los equipos los revisa personal autorizado; se avisa con tiempo."),
    sc=[
        ("En Hotelería: ¿qué es el aforo?", "La cantidad máxima de personas permitidas en un salón", "Superarlo pone en riesgo la seguridad."),
        ("¿Qué debe pasar con las salidas?", "Deben quedar despejadas", "Así se puede evacuar de forma segura."),
        ("¿Quién revisa los equipos eléctricos?", "Personal autorizado", "Esos equipos no se manipulan sin capacitación."),
    ],
    op=("Evento de ejemplo: una celebración de 50 invitados en un salón con aforo de 70, con 2 salidas señalizadas. Horario: ingreso 18:00, inicio 18:30, cena 19:30, término 22:00. El cliente pide un micrófono y una mesa para regalos. "
        "Calcula los lugares libres, y escribe tres reglas de seguridad y una de higiene o accesibilidad que aplicarías, y qué harías si el cliente pide 25 invitados más.",
        "Lugares libres: 70 − 50 = 20. Reglas: salidas despejadas, cables fuera del pasillo y ayuda para mover cosas pesadas; accesibilidad: pasillos anchos y espacio para sillas de ruedas. Si pide 25 invitados más, serían 75, más que el aforo de 70, así que informaría el límite y ofrecería otro salón.",
        ["calcula lugares libres", "nombra tres reglas de seguridad y una de higiene o accesibilidad", "responde con el aforo"],
        ["hoja con el cálculo, las reglas y la respuesta"],
        ["olvidar el aforo", "proponer bloquear las salidas", "aceptar los 25 invitados"],
        "Pregunta: «¿cuántos serían con 25 más?». Si no responde 75, repasa el cálculo del aforo."),
    reinforce="Escribe cinco reglas generales de seguridad para el montaje de un salón.",
    extend="Explica por qué las salidas despejadas son importantes aunque nunca haya una emergencia.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 35 (orden de servicio de ejemplo, inventada). Cliente: Empresa Ejemplo. Fecha: día 15. Personas: 60. Montaje: tipo escuela (mesas rectangulares con sillas mirando al frente, para tomar notas). Equipos: proyector y micrófono. Alimentación: café a las 11:00. "
     "Responsable del evento: jefe de banquetes. Montaje: de 08:00 a 09:00. Otros tipos de montaje: teatro (filas de sillas sin mesas), banquete (mesas redondas), en U (mesas formando una U abierta al frente).")
build(
    O8, 2, F,
    use="Aprenderé los documentos y tipos de montaje de un evento: orden de servicio, plano del salón y lista de verificación.",
    prior=["Conozco el aforo y las salidas.", "Sé multiplicar y dividir.", "Sé leer un plano simple."],
    explain=[
        "La orden de servicio del evento es el documento que reúne lo que el cliente pidió: fecha, número de personas, tipo de montaje, equipos, alimentación, horarios y responsable. Todo el equipo trabaja con la misma orden, y cualquier cambio se anota y se avisa. El plano del salón es un dibujo que muestra dónde van las mesas, las sillas, los equipos y las salidas.",
        "Hay varios tipos de montaje. En teatro se ponen filas de sillas sin mesas y caben más personas; en escuela hay mesas y sillas mirando al frente, para tomar notas; en banquete hay mesas redondas para comer; en U las mesas forman una U abierta al frente, y sirve para reuniones con conversación. El tipo se elige según el objetivo del evento.",
        "La lista de verificación (checklist) permite comprobar que todo se montó: sillas, mesas, manteles, equipos, ornamentos, salidas despejadas. Se marca solo lo que realmente se hizo." + SEG,
    ],
    vocab=[("orden de servicio del evento", "documento con lo que el cliente pidió: fecha, personas, montaje, equipos, alimentación y horarios"), ("plano del salón", "dibujo que muestra dónde va cada elemento"), ("montaje en teatro", "filas de sillas sin mesas"), ("montaje en escuela", "mesas con sillas mirando al frente"), ("montaje en banquete", "mesas redondas para comer"), ("montaje en U", "mesas formando una U abierta al frente")],
    worked=[
        ("Elegir el tipo de montaje", "Un evento de ejemplo es una conferencia de 100 personas que solo escuchará. ¿Qué montaje conviene?", ["No necesitan mesas.", "Caben más personas con sillas en filas."], "Montaje en teatro"),
        ("Calcular sillas", "Un montaje en escuela de ejemplo tiene 12 mesas con 5 sillas cada una. ¿Cuántas sillas necesita?", ["Sillas = mesas × sillas por mesa.", "12 × 5 = 60."], "60 sillas"),
    ],
    mistakes=[("Usar un montaje en banquete para una conferencia donde solo se escuchará.", "Ocupa mucho espacio y reduce la cantidad de personas que caben.", "Elige el tipo de montaje según el objetivo del evento."),
              ("Hacer un cambio pedido por teléfono sin anotarlo en la orden de servicio.", "El resto del equipo trabaja con datos distintos.", "Anota el cambio y avisa a todo el equipo.")],
    T=[
        ("abc", "En Hotelería: ¿qué es una orden de servicio del evento?", "El documento con lo que el cliente pidió: fecha, personas, montaje, equipos y horarios", "Una lista de precios de habitaciones", "El menú de un restaurante", "La orden de servicio reúne los acuerdos con el cliente."),
        ("abc", "{F} ¿Qué tipo de montaje pide la orden?", "Escuela", "Teatro", "Banquete", "La ficha indica montaje tipo escuela."),
        ("abc", "{F} ¿Qué diferencia al montaje en teatro?", "Tiene filas de sillas sin mesas", "Tiene mesas redondas", "Forma una U de mesas", "El montaje en teatro solo usa sillas."),
        ("=", "{F} Si hay 10 mesas con 6 sillas cada una, ¿cuántas sillas hay en total?", "10*6", "Se multiplican las mesas por las sillas de cada mesa.", " sillas"),
        ("=", "{F} Para las 60 personas, ¿cuántas mesas se necesitan si cada mesa tiene 6 sillas?", "60//6", "Se divide el total de personas por las sillas de cada mesa.", " mesas"),
        ("abc", "{F} Para un banquete de comida con conversación entre invitados, ¿qué montaje conviene?", "El banquete, con mesas redondas", "El teatro", "La escuela", "Las mesas redondas facilitan comer y conversar."),
        ("abc", "{F} Una reunión de 12 personas que discuten cara a cara, ¿qué montaje conviene?", "En U", "Teatro", "Banquete", "La U permite que todos se vean y conversen."),
        ("=", "{F} ¿Cuántos minutos dura el montaje, según la orden?", "(9-8)*60", "Se restan las horas y se pasan a minutos.", " minutos"),
        ("abc", "{F} El cliente llama y dice que el café será a las 11:30. ¿Qué haces?", "Anotar el cambio en la orden y avisar a todo el equipo", "Cambiarlo solo en tu cabeza", "No cambiar nada", "Los cambios se anotan para que todos tengan los mismos datos."),
        ("abc", "{F} ¿Para qué sirve el plano del salón?", "Para mostrar dónde va cada mesa, silla, equipo y salida", "Para fijar el precio del evento", "Para saber quién paga", "El plano guía el montaje y evita errores."),
        ("abc", "{F} Al revisar la lista de verificación falta el proyector. ¿Qué haces?", "Marcar que no está y avisar al responsable", "Marcarlo como listo", "Ignorarlo", "Solo se marca lo realmente hecho."),
        ("abc", "{F} Un compañero propone omitir el plano «porque es un salón conocido». ¿Qué respondes?", "Que el plano ayuda a ubicar bien todo y evita errores", "Que tiene razón siempre", "Que el plano es para decorar", "Un plano evita improvisar y respeta las salidas."),
        ("=", "{F} Para las 60 personas con 6 sillas por mesa se necesitan 10 mesas. Si se agregan 2 mesas más de repuesto, ¿cuántas mesas se alistan?", "60//6+2", "Primero se calculan las mesas y luego se suman las 2 adicionales.", " mesas"),
    ],
    ctx=("abc", "{F} El cliente cambia de idea: ahora quiere una cena para las 60 personas, con mesas redondas de 8. ¿Qué haces?", "Calcular las mesas, comprobar el espacio y las salidas, actualizar la orden y avisar a todos", "Montar en escuela de todas formas", "Montar sin calcular", "Un cambio de montaje exige recalcular y actualizar la orden."),
    sc=[
        ("En Hotelería: ¿qué es un montaje en teatro?", "Filas de sillas sin mesas", "Sirve para que muchas personas escuchen."),
        ("¿Dónde se anotan los cambios del cliente?", "En la orden de servicio", "Así todo el equipo conoce los mismos datos."),
        ("¿Qué muestra el plano del salón?", "Dónde va cada elemento", "Orienta el montaje y las salidas."),
    ],
    op=("Orden de ejemplo: taller de capacitación para 36 personas, que toman notas; café a media mañana; proyector. Hay mesas rectangulares de 3 sillas. "
        "Elige el tipo de montaje con una razón, calcula cuántas mesas y sillas se necesitan, y escribe cuatro cosas que anotarías en la lista de verificación.",
        "Montaje en escuela, porque toman notas y necesitan mesa. Mesas: 36 ÷ 3 = 12. Sillas: 36. Lista: mesas y sillas montadas, proyector probado, café coordinado y salidas despejadas.",
        ["elige el montaje con razón", "calcula mesas y sillas", "escribe cuatro puntos de verificación"],
        ["hoja con elección, cálculos y lista"],
        ["elegir banquete", "confundir mesas y sillas", "olvidar las salidas"],
        "Pregunta: «¿por qué no teatro?». Debe responder que necesitan mesas para tomar notas."),
    reinforce="Dibuja un plano simple de un salón con 3 mesas, sillas y 2 salidas.",
    extend="Explica por qué cada cambio del cliente debe quedar escrito.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 36 (caso de ejemplo, inventado). La víspera de un evento, el cliente avisa que los invitados serán 72 en vez de 60. Quiere montaje tipo banquete, con mesas redondas de 8 personas. Hay 12 mesas redondas disponibles. "
     "Salón con aforo de 80 personas (valor de ejemplo) y 2 salidas despejadas. Una invitada usa silla de ruedas y necesita un pasillo libre hasta su mesa. El café se sirve a las 11:00.")
build(
    O8, 3, F,
    use="Aprenderé a analizar un cambio de última hora en un evento y a decidir qué montaje es posible respetando aforo, salidas y accesibilidad.",
    prior=["Conozco la orden de servicio.", "Sé dividir y comparar.", "Conozco el aforo y las salidas."],
    explain=[
        "Cuando el cliente cambia un dato, se analiza el caso: se calcula qué se necesita con el dato nuevo, se compara con lo que hay disponible y con el aforo, y se decide. Por ejemplo, las mesas necesarias son los invitados divididos por los lugares de cada mesa, redondeando hacia arriba cuando sobran personas.",
        "El montaje debe respetar el aforo, las salidas y el espacio para circular. También se piensa en la accesibilidad: un pasillo libre hasta la mesa de una persona en silla de ruedas. Si lo pedido no es posible, se informa con honestidad y se ofrece una alternativa.",
        "Todo cambio se anota en la orden de servicio y se avisa al equipo, con la hora en que se acordó. Se mantiene un trato amable con el cliente." + SEG,
    ],
    vocab=[("cambio de última hora", "modificación pedida poco antes del evento"), ("redondear hacia arriba", "usar el número entero siguiente cuando sobra una parte"), ("circulación", "espacio libre para que las personas caminen"), ("alternativa", "otra opción que se ofrece si lo pedido no es posible"), ("registro", "anotación de lo acordado en la orden de servicio")],
    worked=[
        ("Redondear mesas", "En un evento de ejemplo asisten 25 personas y cada mesa es para 8. ¿Cuántas mesas se necesitan?", ["25 ÷ 8 es 3 y sobra 1 persona.", "Esa persona necesita una mesa más: 4."], "4 mesas"),
        ("Comparar con el aforo", "Un evento de ejemplo espera 90 invitados y el aforo es 80. ¿Qué se hace?", ["90 es mayor que 80.", "Se informa y se ofrece otra solución."], "Informar el límite y ofrecer una alternativa"),
    ],
    mistakes=[("Calcular las mesas con una división y no considerar a las personas que sobran.", "Quedarían invitados sin mesa.", "Redondea hacia arriba cuando sobra una parte."),
              ("Aceptar el cambio sin comparar con el aforo y las salidas.", "Se puede superar el máximo permitido o bloquear las salidas.", "Compara siempre con el aforo y el plano antes de aceptar.")],
    T=[
        ("abc", "En Hotelería: ¿qué se hace cuando el cliente cambia un dato de último momento?", "Se analiza el cambio, se compara con lo disponible y se registra en la orden", "Se ignora para no complicar", "Se cambia solo si el cliente insiste", "El cambio se estudia, se decide y se anota."),
        ("=", "{F} ¿Cuántos invitados más hay respecto de lo pedido al comienzo?", "72-60", "Se resta lo inicial a lo nuevo.", " invitados"),
        ("abc", "{F} ¿Cumple el aforo de 80 con 72 invitados?", "Sí, porque 72 es menor que 80", "No, porque 72 es mayor que 80", "No se puede saber", "72 es menor que el aforo de 80."),
        ("=", "{F} ¿Cuántas mesas redondas de 8 se necesitan para 72 invitados?", "72//8", "Se divide el total de invitados por los lugares de cada mesa.", " mesas"),
        ("abc", "{F} ¿Alcanzan las mesas disponibles?", "Sí: se necesitan 9 y hay 12", "No: se necesitan 15", "No: se necesitan 12", "Hay 12 mesas y se requieren 9."),
        ("=", "{F} ¿Cuántas mesas sobran sin usar?", "12-72//8", "A las mesas disponibles se les restan las necesarias.", " mesas"),
        ("=", "{F} Si además se alistan 4 sillas de repuesto, ¿cuántas sillas se preparan en total?", "72+4", "Se suma una silla por invitado y las sillas de repuesto.", " sillas"),
        ("abc", "{F} ¿Qué se cuida para la invitada que usa silla de ruedas?", "Dejar un pasillo libre hasta su mesa y un lugar con espacio", "Ubicarla lejos del grupo", "Pedirle que se cambie de salón", "La accesibilidad incluye pasillos libres y espacio."),
        ("abc", "{F} Un compañero propone usar las 12 mesas para tener más espacio entre ellas. ¿Qué respondes?", "Se pueden usar más mesas si el espacio y las salidas lo permiten, comprobándolo en el plano", "Es imposible, solo hay 9", "Hay que usar siempre 12", "Más mesas pueden dar más espacio, pero se verifica con el plano."),
        ("abc", "{F} El cliente llama a las 22:00 para pedir 90 invitados. ¿Qué haces?", "Informar que superaría el aforo de 80 y ofrecer otra solución", "Aceptar y poner sillas en los pasillos", "No contestar", "El aforo es un límite de seguridad que no se supera."),
        ("abc", "{F} Se acuerda el cambio de 72 invitados. ¿Qué haces con la orden de servicio?", "Anotar el cambio con la fecha, la hora y quién lo acordó, y avisar al equipo", "Dejarla igual", "Guardarla sin revisar", "Se registra para que todos trabajen con los mismos datos."),
        ("=", "{F} Si cada mesa lleva 1 mantel y se agregan 2 de repuesto, ¿cuántos manteles se alistan para las mesas necesarias?", "72//8+2", "Se suman las mesas necesarias y los 2 manteles de repuesto.", " manteles"),
        ("abc", "{F} A las 10:30 llega el café y no hay dónde ubicarlo sin bloquear una salida. ¿Qué haces?", "Buscar otro lugar y mantener las salidas libres", "Dejarlo frente a la salida por esta vez", "Cancelar el café", "Las salidas despejadas no se negocian."),
    ],
    ctx=("abc", "{F} El cliente pregunta si podrían ser 80 invitados al final. ¿Qué respondes?", "Que 80 es el aforo máximo, que habría que revisar las mesas y la circulación, y que consultarás a la jefatura", "Que sí, sin revisar", "Que no, sin explicar", "Se evalúa el límite y se consulta antes de comprometerse."),
    sc=[
        ("En Hotelería: ¿cómo se calculan las mesas necesarias?", "Invitados divididos por lugares de cada mesa", "Se redondea hacia arriba si sobran personas."),
        ("¿Con qué se compara un cambio de invitados?", "Con el aforo y el plano", "El aforo es el límite de seguridad."),
        ("¿Qué haces con el acuerdo del cambio?", "Lo anoto en la orden de servicio", "Así todo el equipo lo conoce."),
    ],
    op=("Caso de ejemplo. Un evento pasa de 40 a 54 invitados. Salón con aforo de 60 y 2 salidas. Mesas redondas de 6 personas; hay 10 disponibles. Una invitada usa bastón. "
        "Calcula cuántas mesas y sillas se necesitan, si alcanzan las mesas, si cumple el aforo, y escribe tres cosas que harías para registrar y comunicar el cambio y cuidar la accesibilidad.",
        "Mesas: 54 ÷ 6 = 9; hay 10, alcanzan y sobra 1. Sillas: 54. Aforo: 54 es menor que 60, cumple. Acciones: anotar el cambio en la orden con fecha y hora, avisar al equipo y dejar un pasillo libre y un lugar cercano para la invitada con bastón.",
        ["calcula mesas, sillas y aforo", "comprueba disponibilidad", "describe registro, aviso y accesibilidad"],
        ["hoja con cálculos y tres acciones"],
        ["usar 8 por mesa en vez de 6", "olvidar el aforo", "no registrar el cambio"],
        "Pregunta: «¿cuántas personas por mesa?». Si responde 8, repasa los datos del caso."),
    reinforce="Inventa un evento con un cambio de invitados y calcula las mesas necesarias.",
    extend="Explica por qué redondear hacia arriba evita que queden invitados sin mesa.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 37 (montaje de ejemplo, inventado). Banquete para 72 invitados en 9 mesas redondas de 8 sillas. Cada mesa lleva 1 mantel, 8 servilletas de tela y 1 centro de mesa de $3.500. Equipos: 1 proyector y 1 micrófono. "
     "Montaje por 3 personas; cada persona monta una mesa completa en 12 minutos (tiempo de ejemplo). El montaje comienza a las 08:00 y debe terminar 30 minutos antes de que ingresen los invitados a las 09:30. Presupuesto de ornamentos: $35.000.")
build(
    O8, 4, F,
    use="Aprenderé a calcular cantidades, tiempos y costos de un montaje y a comprobar que se puede terminar a tiempo y dentro del presupuesto.",
    prior=["Sé multiplicar, dividir y sumar.", "Sé calcular horas y minutos.", "Conozco el aforo y la orden de servicio."],
    explain=[
        "Para planificar un montaje se calculan las cantidades: mesas, sillas, manteles, servilletas y ornamentos, a partir del número de invitados y de la organización de las mesas. Por ejemplo, si cada mesa lleva 8 servilletas y hay 9 mesas, se necesitan 72 servilletas.",
        "El tiempo de montaje se calcula repartiendo las mesas entre las personas. Si hay 9 mesas y 3 personas, cada una monta 3 mesas, y si cada mesa toma 12 minutos, cada persona demora 36 minutos. La hora de término es la hora de inicio más ese tiempo y debe quedar antes del límite para tener un margen.",
        "El costo se calcula multiplicando la cantidad por el precio y se compara con el presupuesto. Si no alcanza, se ajusta con un ornamento más simple. Cuando se mueven mesas o sillas, se pide ayuda para las cargas pesadas." + SEG,
    ],
    vocab=[("cantidad", "número de objetos que se necesitan"), ("margen de tiempo", "tiempo extra antes del límite para resolver imprevistos"), ("costo", "dinero que cuesta algo"), ("presupuesto", "dinero máximo disponible"), ("ornamentos", "adornos del evento")],
    worked=[
        ("Calcular servilletas", "Un evento de ejemplo tiene 6 mesas y cada una lleva 10 servilletas. ¿Cuántas servilletas se necesitan?", ["Servilletas = mesas × servilletas por mesa.", "6 × 10 = 60."], "60 servilletas"),
        ("Calcular el tiempo de montaje", "Cuatro personas montan 8 mesas de ejemplo; cada persona monta una mesa en 10 minutos. ¿Cuánto demoran?", ["8 ÷ 4 = 2 mesas por persona.", "2 × 10 = 20 minutos."], "20 minutos"),
    ],
    mistakes=[("Calcular el tiempo sumando todas las mesas como si una sola persona las montara.", "Se exagera el tiempo y se descarta un plan que sí alcanza.", "Divide las mesas entre las personas antes de multiplicar por los minutos."),
              ("No dejar margen de tiempo antes de que lleguen los invitados.", "Cualquier imprevisto atrasa el evento.", "Termina el montaje antes del límite fijado.")],
    T=[
        ("abc", "En Hotelería: ¿para qué sirve el margen de tiempo?", "Para resolver imprevistos antes de que lleguen los invitados", "Para bajar el presupuesto", "Para cambiar el programa", "El margen evita que un atraso afecte el inicio del evento."),
        ("=", "{F} ¿Cuántas sillas se necesitan para las 9 mesas?", "9*8", "Se multiplican las mesas por las sillas de cada mesa.", " sillas"),
        ("=", "{F} Si se alistan 2 manteles de repuesto además de uno por mesa, ¿cuántos manteles se preparan?", "9+2", "Se suma un mantel por mesa y los de repuesto.", " manteles"),
        ("=", "{F} ¿Cuántas servilletas de tela se necesitan?", "9*8", "Se multiplican las mesas por las servilletas de cada mesa.", " servilletas"),
        ("=", "{F} ¿Cuánto cuestan los centros de mesa?", "9*3500", "Se multiplican las mesas por el precio de cada centro.", " pesos"),
        ("abc", "{F} ¿Alcanza el presupuesto de ornamentos?", "Sí: cuestan $31.500 y el máximo es $35.000", "No: cuestan más de $35.000", "No se puede saber", "El costo es menor que el presupuesto."),
        ("=", "{F} ¿Cuántas mesas monta cada persona?", "9//3", "Se reparten las mesas entre las personas.", " mesas"),
        ("=", "{F} ¿Cuántos minutos demora cada persona en montar sus mesas?", "9//3*12", "Se multiplican las mesas por persona por los minutos de cada mesa.", " minutos"),
        ("abc", "{F} ¿A qué hora termina el montaje si comienza a las 08:00?", "A las 08:36", "A las 09:00", "A las 08:12", "A las 08:00 se suman 36 minutos y resulta 08:36."),
        ("abc", "{F} ¿Se cumple el límite de terminar 30 minutos antes de las 09:30?", "Sí: termina a las 08:36 y el límite es las 09:00", "No: termina después de las 09:00", "No se puede saber", "08:36 es anterior a las 09:00."),
        ("=", "{F} ¿Cuántos minutos de margen quedan antes de las 09:00?", "(9*60)-(8*60+36)", "Se restan los minutos del término a los del límite.", " minutos"),
        ("abc", "{F} Una persona del equipo no llega y quedan solo 2 personas. ¿Qué debe revisarse?", "Recalcular el tiempo: cada persona montaría más mesas y debe seguir el límite", "Nada, porque el tiempo es igual", "Suspender el evento sin calcular", "Menos personas aumentan el tiempo y hay que recalcularlo."),
        ("=", "{F} Con solo 2 personas y 9 mesas, ¿cuántos minutos demora la persona que monta más mesas? (una monta 5 y la otra 4)", "5*12", "Se multiplican las mesas de la persona con más carga por los minutos de cada mesa.", " minutos"),
    ],
    ctx=("abc", "{F} Al terminar el montaje notas que falta el centro de mesa de una mesa. ¿Qué haces?", "Reponerlo con uno de repuesto o avisar al responsable antes de que lleguen los invitados", "No decir nada", "Quitar el de otra mesa sin avisar", "Se corrige o se avisa a tiempo sin dejar el montaje incompleto."),
    sc=[
        ("En Hotelería: ¿cómo se calcula el tiempo de montaje?", "Mesas por persona multiplicadas por los minutos de cada mesa", "Primero se reparte el trabajo entre las personas."),
        ("¿Qué haces si el costo supera el presupuesto?", "Ajusto los ornamentos", "No se puede gastar más de lo disponible."),
        ("En la organización de un evento del hotel, ¿para qué sirve el margen de tiempo?", "Para imprevistos", "Evita que un atraso afecte el inicio."),
    ],
    op=("Montaje de ejemplo: cena para 48 invitados en mesas redondas de 6. Cada mesa lleva 1 mantel, 6 servilletas y un adorno de $2.800. Montan 4 personas; cada una monta una mesa en 10 minutos. Comienza a las 15:00 y debe terminar a las 16:00. Presupuesto de adornos: $24.000. "
        "Calcula mesas, sillas, servilletas, costo de adornos, si alcanza el presupuesto, y la hora de término y si cumple el límite.",
        "Mesas: 48 ÷ 6 = 8. Sillas: 48. Servilletas: 8 × 6 = 48. Adornos: 8 × 2.800 = 22.400, que cumple el presupuesto de 24.000. Cada persona monta 2 mesas, 2 × 10 = 20 minutos; termina a las 15:20 y cumple el límite de las 16:00.",
        ["calcula mesas, sillas y servilletas", "calcula costo y compara con el presupuesto", "calcula el tiempo y la hora de término"],
        ["hoja con los cálculos"],
        ["calcular las mesas con 8 por mesa", "no repartir las mesas entre las personas", "olvidar comparar con el presupuesto"],
        "Pregunta: «¿cuántas mesas monta cada persona?». Si no responde 2, repasa el reparto."),
    reinforce="Inventa un montaje para 30 invitados y calcula sillas, manteles y costo de adornos.",
    extend="Explica por qué conviene anotar la hora real de término del montaje.",
)

# ============================================================ OAE-09, clase 1
F = ("Ficha 38 (glosario de ejemplo, inglés básico). Welcome to the hotel = Bienvenido al hotel. May I help you? = ¿Puedo ayudarle? reservation = reserva. room = habitación. single room = habitación individual. double room = habitación doble. key card = tarjeta de acceso. "
     "Here is your key card = Aquí está su tarjeta de acceso. breakfast = desayuno. check-in = ingreso. check-out = salida. bill = cuenta. elevator = ascensor. luggage = equipaje. Where is...? = ¿Dónde está...? "
     "Could you repeat, please? = ¿Podría repetir, por favor? Could you spell your name, please? = ¿Podría deletrear su nombre, por favor? I'm sorry, I can't give that information = Lo siento, no puedo dar esa información. Thank you = Gracias.")
build(
    O9, 1, F,
    use="Aprenderé el vocabulario y las frases básicas en inglés para recibir a un huésped, entender lo que pide y responder con cortesía.",
    prior=["Sé saludar con cortesía.", "Conozco el vocabulario básico del hotel en español.", "Sé leer frases cortas."],
    explain=[
        "En Hotelería, el inglés básico se usa para recibir y atender a turistas que no hablan español. No hace falta saber mucho: con unas pocas frases claras, dichas con un tono amable, se puede entender lo que el huésped necesita. Las palabras básicas son reservation (reserva), room (habitación), key card (tarjeta de acceso), breakfast (desayuno), check-in, check-out y bill (cuenta).",
        "Las frases de cortesía son parte del servicio: «Welcome to the hotel» para recibir, «May I help you?» para ofrecer ayuda, «Thank you» para agradecer y «Could you repeat, please?» cuando no entiendes. Si necesitas el nombre exacto, puedes pedir «Could you spell your name, please?». Hablar despacio y con una sonrisa ayuda mucho.",
        "También se aplica la privacidad en inglés: si alguien pide datos de otro huésped, se responde con cortesía «I'm sorry, I can't give that information». Esto es una guía de ejemplo y no reemplaza un curso de inglés." + LIM,
    ],
    vocab=[("reservation", "reserva"), ("room", "habitación"), ("key card", "tarjeta de acceso"), ("breakfast", "desayuno"), ("bill", "cuenta"), ("elevator", "ascensor"), ("luggage", "equipaje")],
    worked=[
        ("Traducir una palabra", "Un huésped dice: «I need my luggage». ¿Qué necesita?", ["Se busca luggage en el glosario.", "Luggage es equipaje."], "Su equipaje"),
        ("Elegir una frase", "Quieres ofrecer ayuda a un turista en la recepción. ¿Qué frase usas?", ["Se busca la frase de ofrecer ayuda.", "Es «May I help you?»."], "«May I help you?»"),
    ],
    mistakes=[("Responder «yes» a todo sin haber entendido lo que preguntó el huésped.", "Puede aceptar algo que no corresponde y causar un error.", "Pide con cortesía «Could you repeat, please?»."),
              ("Dar el número de habitación de otro huésped porque «es fácil decirlo en inglés».", "La confidencialidad no cambia con el idioma.", "Responde «I'm sorry, I can't give that information»." )],
    T=[
        ("abc", "En Hotelería: ¿qué significa «reservation»?", "Reserva", "Recepción", "Resfriado", "Reservation es la palabra para la reserva de una habitación."),
        ("abc", "{F} ¿Qué significa «breakfast»?", "Desayuno", "Cena", "Almuerzo", "La ficha traduce breakfast como desayuno."),
        ("abc", "{F} ¿Cómo se dice «equipaje» en inglés?", "Luggage", "Elevator", "Bill", "Luggage es equipaje; elevator es ascensor y bill es cuenta."),
        ("abc", "{F} ¿Qué significa «double room»?", "Habitación doble", "Habitación individual", "Tarjeta de acceso", "Double room es una habitación doble; single room es individual."),
        ("abc", "{F} Un huésped dice: «I have a reservation». ¿Qué quiere decir?", "Tiene una reserva", "Quiere el desayuno", "Quiere su cuenta", "La frase indica que ya tiene una reserva."),
        ("abc", "{F} ¿Qué frase usas para entregar la tarjeta de la habitación?", "Here is your key card", "Where is the elevator?", "Thank you", "Esa frase entrega la tarjeta de acceso."),
        ("abc", "{F} Un huésped pregunta: «Where is the elevator?». ¿Qué quiere saber?", "Dónde está el ascensor", "Dónde está el equipaje", "Cuánto cuesta el desayuno", "Elevator es ascensor y where is es dónde está."),
        ("abc", "{F} No entendiste lo que dijo el huésped. ¿Qué frase usas?", "Could you repeat, please?", "Welcome to the hotel", "Here is your bill", "Esa frase pide repetir con cortesía."),
        ("abc", "{F} Un huésped tiene un apellido difícil. ¿Qué frase usas?", "Could you spell your name, please?", "Thank you", "May I help you?", "Esa frase pide que deletree su nombre."),
        ("abc", "{F} Al despedir a un huésped que ya pagó, ¿qué dices para agradecer?", "Thank you", "Welcome to the hotel", "Where is...?", "Thank you significa gracias y sirve para agradecer."),
        ("abc", "{F} Alguien pregunta en inglés cuál es la habitación de otro huésped. ¿Qué respuesta usas?", "I'm sorry, I can't give that information", "The room is number twelve", "Here is your key card", "La privacidad de los huéspedes se mantiene en cualquier idioma."),
        ("abc", "{F} Quieres ofrecer ayuda a un turista que llega. ¿Qué dices primero?", "Welcome to the hotel. May I help you?", "Here is your bill", "I'm sorry, I can't give that information", "Se saluda y se ofrece ayuda."),
        ("abc", "{F} Un huésped que sale pide: «My bill, please». ¿Qué necesita?", "Su cuenta", "Su reserva", "Su equipaje", "Bill significa cuenta, el documento de cobro del hotel."),
    ],
    ctx=("abc", "{F} Un turista llega, dice algo muy rápido en inglés y no lo entiendes. ¿Qué haces?", "Sonreír y decir «Could you repeat, please?» con calma", "Decir «yes» sin entender", "Pedirle que se vaya", "Pedir que repita con cortesía evita errores."),
    sc=[
        ("En Hotelería: ¿cómo se dice «habitación» en inglés?", "Room", "Es la palabra básica de la ficha."),
        ("¿Qué significa «key card»?", "Tarjeta de acceso", "Es la tarjeta que abre la habitación."),
        ("En recepción de un hotel, ¿qué frase pide que repitan?", "Could you repeat, please?", "Es la forma cortés de pedir otra vez."),
    ],
    op=("Un turista de ejemplo llega a un hotel y dice: «Hello, I have a reservation. A double room, please». "
        "Escribe: qué quiere decir en español, tres frases en inglés de la ficha para atenderlo (saludo, pedir el nombre, entregar la tarjeta) y una frase para cuando alguien te pida datos de otro huésped.",
        "Quiere decir: «Hola, tengo una reserva. Una habitación doble, por favor». Frases: «Welcome to the hotel», «Could you spell your name, please?», «Here is your key card». Privacidad: «I'm sorry, I can't give that information».",
        ["traduce bien la frase del turista", "usa tres frases correctas de la ficha", "incluye la frase de privacidad"],
        ["hoja con la traducción y las cuatro frases"],
        ["inventar frases que no están en la ficha", "confundir double con single", "olvidar la frase de privacidad"],
        "Pregunta: «¿qué tipo de habitación pidió?». Si responde 'individual', repasa double room."),
    reinforce="Escribe en una tabla las 12 palabras y frases más importantes de la ficha con su significado.",
    extend="Explica por qué decir «Could you repeat, please?» es mejor que adivinar lo que dijo el huésped.",
)

# ============================================================ OAE-09, clase 2
F = ("Ficha 39 (números, horas y precios de ejemplo, en inglés básico). one = 1, two = 2, three = 3, four = 4, five = 5, seven = 7, ten = 10, twelve = 12, twenty = 20, fifty = 50. thousand = mil. night = noche. from ... to ... = de ... a .... at = a las. per = por. "
     "Frases de ejemplo: Breakfast is from seven to ten. = El desayuno es de siete a diez. Check-in is at three p.m. = El ingreso es a las tres de la tarde. Check-out is at twelve. = La salida es a las doce. The room is fifty thousand pesos per night. = La habitación cuesta cincuenta mil pesos por noche. How many nights? = ¿Cuántas noches? What time is ...? = ¿A qué hora es ...?")
build(
    O9, 2, F,
    use="Aprenderé números, horas y precios en inglés básico para informar horarios y tarifas a un huésped y preguntar la cantidad de noches.",
    prior=["Conozco el vocabulario básico del hotel en inglés.", "Sé leer horas y precios.", "Sé multiplicar."],
    explain=[
        "Informar horarios y precios en inglés requiere conocer los números y unas pocas estructuras. Las horas se dicen con at (a las): «Check-in is at three p.m.». Los rangos se dicen con from ... to ...: «Breakfast is from seven to ten». Los precios se dicen con per (por): «fifty thousand pesos per night».",
        "Los números clave son one, two, three, four, five, seven, ten, twelve, twenty y fifty, y la palabra thousand para mil. Para preguntar la cantidad de noches se dice «How many nights?». Con el precio por noche y la cantidad de noches, se calcula el total multiplicando.",
        "Si el huésped no entiende, se escribe el número en cifras en un papel. Esto es una guía de ejemplo con vocabulario limitado y no reemplaza un curso de inglés." + LIM,
    ],
    vocab=[("from ... to ...", "de ... a ..., para decir un rango de horas"), ("at", "a las, para una hora exacta"), ("per night", "por noche"), ("thousand", "mil"), ("How many nights?", "¿Cuántas noches?"), ("p.m.", "de la tarde o noche")],
    worked=[
        ("Traducir una hora", "Un cartel de ejemplo dice «Check-out is at twelve». ¿Cuál es la hora de salida?", ["At indica una hora exacta.", "Twelve es doce."], "A las 12:00"),
        ("Calcular un total", "Un huésped de ejemplo se queda two nights y la habitación cuesta ten thousand pesos per night. ¿Cuánto paga?", ["Two es 2 y ten thousand es 10.000.", "2 × 10.000 = 20.000."], "20.000 pesos"),
    ],
    mistakes=[("Decir «Breakfast is at seven to ten» con «at» en lugar de «from».", "At es para una hora exacta, no para un rango.", "Usa from ... to ... para un rango de horas."),
              ("Decir el precio sin decir si es por noche o total.", "El huésped puede entender mal cuánto pagará.", "Di «per night» y el total si lo conoces.")],
    T=[
        ("abc", "En Hotelería: ¿qué significa «per night»?", "Por noche", "Por persona", "Por día de semana", "Per night indica que el precio corresponde a cada noche."),
        ("abc", "{F} ¿Qué dice «Breakfast is from seven to ten»?", "El desayuno es de siete a diez", "El desayuno es a las diez", "El desayuno cuesta diez mil pesos", "From ... to ... indica un rango de horas."),
        ("abc", "{F} ¿Qué dice «Check-in is at three p.m.»?", "El ingreso es a las tres de la tarde", "El ingreso es a las tres de la mañana", "La salida es a las tres", "At indica la hora exacta y p.m. indica la tarde."),
        ("abc", "{F} ¿Cómo se pregunta la cantidad de noches?", "How many nights?", "How much per night?", "What time is it?", "Esa frase pregunta cuántas noches se quedará el huésped."),
        ("=", "{F} Un huésped se queda three nights y la habitación cuesta fifty thousand pesos per night. ¿Cuánto es el total?", "3*50000", "Se multiplican las noches por el precio por noche.", " pesos"),
        ("=", "{F} El desayuno es de seven to ten. ¿Cuántas horas dura?", "10-7", "Se resta la hora de inicio a la de término.", " horas"),
        ("abc", "{F} Un huésped pregunta la hora de salida y respondes: «Check-out is at twelve». ¿A qué hora debe salir?", "A las 12:00", "A las 10:00", "A las 15:00", "At twelve es a las doce."),
        ("=", "{F} Un grupo se queda two nights en una habitación de twenty thousand pesos per night. ¿Cuánto paga? (veinte mil)", "2*20000", "Se multiplican las noches por el precio por noche.", " pesos"),
        ("abc", "{F} Un huésped dice «five nights». ¿Cuántas noches se queda?", "5", "7", "10", "Five es cinco, así que se queda cinco noches."),
        ("abc", "{F} Un huésped pregunta «What time is check-in?». Con la ficha, ¿qué respondes?", "Check-in is at three p.m.", "Breakfast is from seven to ten", "The room is fifty thousand pesos per night", "Responde a la hora del ingreso."),
        ("abc", "{F} Un turista no entiende los números en inglés. ¿Qué haces?", "Escribir las cifras en un papel", "Repetir más fuerte lo mismo", "Dejarlo sin respuesta", "Un apoyo visual ayuda cuando hay una barrera de idioma."),
        ("abc", "{F} El huésped pregunta por el precio y respondes: «Fifty thousand pesos». ¿Qué falta aclarar?", "Si el precio es per night o total", "Su apellido", "El número de ascensores", "Sin aclarar, el precio puede entenderse mal."),
        ("=", "{F} Si el huésped paga con un billete de cien mil pesos (100.000) por one night a fifty thousand, ¿cuánto vuelto recibe?", "100000-50000", "Al billete se le resta el precio de la noche.", " pesos"),
    ],
    ctx=("abc", "{F} Un huésped pregunta: «What time is breakfast?». ¿Qué respondes?", "Breakfast is from seven to ten", "Check-out is at twelve", "The room is fifty thousand pesos per night", "Responde a la pregunta con el horario de la ficha."),
    sc=[
        ("En Hotelería: ¿cómo se dice «por noche» en inglés?", "Per night", "Se usa per para decir por."),
        ("¿Cómo se dice un rango de horas?", "From ... to ...", "Indica la hora de inicio y la de término."),
        ("¿Qué haces si el huésped no entiende un número?", "Lo escribo en cifras", "Un papel con cifras evita el error de comprensión."),
    ],
    op=("Un hotel de ejemplo informa a un turista: «Breakfast is from seven to ten. Check-out is at twelve. The room is forty thousand pesos per night». El turista dice que se queda four nights. "
        "Escribe: qué dice cada frase en español, el total que debe pagar (forty thousand = 40.000), y la pregunta que harías para saber cuántas noches se queda.",
        "Frases: el desayuno es de siete a diez; la salida es a las doce; la habitación cuesta cuarenta mil pesos por noche. Total: 4 × 40.000 = 160.000 pesos. Pregunta: «How many nights?».",
        ["traduce las tres frases", "calcula el total", "usa la pregunta correcta"],
        ["hoja con traducciones, total y pregunta"],
        ["confundir at con from", "olvidar multiplicar por las noches", "inventar otra pregunta"],
        "Pregunta: «¿cuál frase usa from ... to ...?». Si no la identifica, repasa rangos."),
    reinforce="Escribe cinco horarios en inglés de un hotel inventado con la estructura de la ficha.",
    extend="Explica por qué es importante decir si un precio es por noche o total.",
)

# ============================================================ OAE-09, clase 3
F = ("Ficha 40 (diálogo de ejemplo, original, en inglés básico). Receptionist (R) y Guest (G). R: Good evening. May I help you? G: Hello. I have a reservation for two nights. My name is Anna Ejemplo. "
     "R: Thank you. Could you spell your last name, please? G: E-J-E-M-P-L-O. R: Yes, I see it. A double room for two nights. Here is your key card. Breakfast is from seven to ten. G: Thank you. Where is the elevator? R: The elevator is on the left. "
     "Glosario: Good evening = Buenas tardes o buenas noches; last name = apellido; I see it = lo veo; on the left = a la izquierda; on the right = a la derecha; straight ahead = todo recto; double room = habitación doble; single room = habitación individual; nights = noches; reservation = reserva.")
build(
    O9, 3, F,
    use="Aprenderé a leer un diálogo corto en inglés de recepción, entender qué pide el huésped y reconocer qué datos se dieron.",
    prior=["Conozco el vocabulario básico del hotel en inglés.", "Conozco números y horas en inglés.", "Sé leer un diálogo."],
    explain=[
        "Un diálogo de recepción sigue un orden: saludo, ofrecimiento de ayuda, datos de la reserva, entrega de la llave y de la información del hotel, y despedida. Al leer, se identifica quién habla (R es la recepcionista y G el huésped) y qué dice cada uno.",
        "Para entender un diálogo, se buscan las palabras clave: reservation, nights, double room, key card, breakfast, elevator. Así se sabe qué pidió el huésped y qué datos se le dieron: el tipo de habitación, cuántas noches, el horario del desayuno y dónde está el ascensor.",
        "Las direcciones simples se dicen con on the left (a la izquierda), on the right (a la derecha) y straight ahead (todo recto). Cuando el huésped no entiende, se repite más despacio y se apoya con gestos." + LIM,
    ],
    vocab=[("last name", "apellido"), ("I see it", "lo veo"), ("on the left", "a la izquierda"), ("on the right", "a la derecha"), ("straight ahead", "todo recto"), ("Good evening", "buenas tardes o buenas noches")],
    worked=[
        ("Identificar un dato", "En un diálogo de ejemplo, el huésped dice «I have a reservation for three nights». ¿Cuántas noches reservó?", ["Se busca la palabra nights.", "Three nights son 3 noches."], "3 noches"),
        ("Entender una dirección", "En otro diálogo de ejemplo, la recepcionista dice «The restaurant is on the right». ¿Hacia dónde queda?", ["On the right es a la derecha.", "Queda a la derecha."], "A la derecha"),
    ],
    mistakes=[("Entender «I see it» como «yo veo la llave».", "En este contexto significa que la reserva está registrada.", "Lee la frase completa y su contexto."),
              ("Dar la dirección al revés, diciendo «left» cuando es «right».", "El huésped va hacia el lado equivocado.", "Revisa la dirección antes de decirla y apóyate con gestos.")],
    T=[
        ("abc", "En Hotelería: ¿quién habla primero en el diálogo?", "La recepcionista, con «Good evening»", "El huésped, con «Hello»", "Nadie", "El diálogo comienza con la recepcionista saludando."),
        ("abc", "{F} ¿Qué reservó la huésped?", "Una habitación doble por dos noches", "Una habitación individual por una noche", "Un desayuno por tres noches", "El diálogo dice double room y two nights."),
        ("=", "{F} El hotel cobra 30.000 pesos por noche (dato de ejemplo). ¿Cuánto paga la huésped por las noches reservadas?", "2*30000", "Se multiplican las noches reservadas por el precio por noche.", " pesos"),
        ("abc", "{F} ¿Qué apellido deletreó la huésped?", "Ejemplo", "Anna", "Receptionist", "Deletreó las letras E-J-E-M-P-L-O, que forman Ejemplo."),
        ("abc", "{F} ¿Qué pidió la recepcionista cuando dijo «Could you spell your last name, please?»", "Que deletreara su apellido", "Que pagara la cuenta", "Que mostrara su llave", "Spell es deletrear y last name es apellido."),
        ("abc", "{F} ¿A qué hora es el desayuno según el diálogo?", "De siete a diez", "A las doce", "A las tres de la tarde", "La recepcionista dice «from seven to ten»."),
        ("abc", "{F} ¿Dónde está el ascensor?", "A la izquierda", "A la derecha", "Todo recto", "La recepcionista dice «on the left»."),
        ("abc", "{F} ¿Qué entregó la recepcionista a la huésped?", "La tarjeta de acceso", "La cuenta", "El equipaje", "Dijo «Here is your key card»."),
        ("abc", "{F} ¿Qué significa que la recepcionista diga «Yes, I see it»?", "Que la reserva está registrada", "Que ve a la huésped", "Que ve el ascensor", "En ese contexto confirma que encontró la reserva."),
        ("=", "{F} La huésped llegó el día 14 del mes y se queda las noches reservadas. ¿Qué día del mes sale?", "14+2", "Se suman las noches reservadas al día de llegada.", ""),
        ("abc", "{F} Una compañera propone responder «yes» a todo lo que diga la huésped. ¿Qué observación corresponde?", "Es mejor pedir que repita si no se entiende, para evitar errores", "Es una buena idea, porque es amable", "Es mejor no hablar nunca", "Responder sin entender puede causar errores en la reserva."),
        ("abc", "{F} La huésped pregunta por el restaurante y la ficha no tiene el dato. ¿Qué haces?", "Que consultarás y volverás con la información", "Que está a la derecha, aunque no lo sepas", "Que no existe", "Si falta el dato, se consulta; no se inventa."),
        ("abc", "{F} Al despedirte de la huésped, ¿qué frase corresponde?", "Thank you", "Where is the elevator?", "Could you spell your name, please?", "Thank you es una forma cortés de despedir y agradecer."),
    ],
    ctx=("abc", "{F} Otro huésped dice: «I have a reservation for three nights. Single room». Con las palabras de la ficha, ¿qué entendiste?", "Tiene una reserva de tres noches en una habitación individual", "Quiere el desayuno y la cuenta", "Quiere dejar su equipaje", "Reservation es reserva, three nights son tres noches y single room es individual."),
    sc=[
        ("En Hotelería: ¿qué significa «last name»?", "Apellido", "Es el nombre de familia de la persona."),
        ("¿Qué significa «on the left»?", "A la izquierda", "Es una dirección simple de uso frecuente."),
        ("¿Qué haces si no entiendes un diálogo?", "Pido que repita", "Es mejor que adivinar y equivocarse."),
    ],
    op=("Diálogo de ejemplo. R: Good evening. May I help you? G: Hello. I have a reservation for one night. Single room. My name is Mark Ejemplo. R: Could you spell your last name, please? G: E-J-E-M-P-L-O. R: Thank you. Here is your key card. Breakfast is from seven to ten. The elevator is on the right. "
        "Escribe: qué reservó, el nombre, qué horario de desayuno se dijo, dónde está el ascensor, y una frase en inglés que tú dirías para despedir al huésped.",
        "Reservó una habitación individual por una noche. Nombre: Mark Ejemplo. Desayuno: de siete a diez. El ascensor está a la derecha. Despedida: «Thank you».",
        ["identifica los cinco datos", "usa una frase de despedida correcta", "no inventa datos"],
        ["hoja con cinco datos y una frase"],
        ["confundir left con right", "decir dos noches", "inventar un horario"],
        "Pregunta: «¿dónde está el ascensor?». Si responde 'a la izquierda', repasa la dirección del diálogo."),
    reinforce="Escribe tu propio diálogo de seis líneas entre una recepcionista y un huésped usando las frases de la ficha.",
    extend="Explica por qué las palabras clave ayudan a entender un diálogo aunque no se conozca todo el vocabulario.",
)

# ============================================================ OAE-09, clase 4
F = ("Ficha 41 (información del hotel, de ejemplo, en inglés básico). Restaurant: open from six to nine p.m. Pool: closes at eight p.m. Laundry: two thousand pesos per bag. Restrooms (baños): on the right. Elevator: on the left. Restaurant: straight ahead. "
     "Glosario: restaurant = restaurante; pool = piscina; closes = cierra; open = abierto; laundry = lavandería; bag = bolsa; restrooms = baños. Frases útiles: What time...? = ¿A qué hora...?; How much...? = ¿Cuánto cuesta...?; Where is...? = ¿Dónde está...?")
build(
    O9, 4, F,
    use="Aprenderé a responder en inglés básico preguntas de un turista sobre horarios, precios y ubicaciones, usando una ficha de información del hotel.",
    prior=["Conozco números, horas y direcciones en inglés.", "Conozco el vocabulario del hotel.", "Sé leer una ficha de información."],
    explain=[
        "Atender en inglés básico es entender la pregunta, buscar el dato en la ficha de información y responder con una frase corta. Las preguntas más comunes empiezan con What time...? (a qué hora), How much...? (cuánto cuesta) y Where is...? (dónde está). Se identifica la palabra clave de la pregunta para encontrar la respuesta.",
        "La respuesta debe ser clara y completa: «The pool closes at eight p.m.» responde la hora de cierre; «The laundry is two thousand pesos per bag» responde el precio con su unidad. Para indicar una ubicación se usa on the left, on the right o straight ahead.",
        "Si no tienes el dato, se dice con cortesía que se consultará, sin inventar. También se mantiene la privacidad: no se dan datos de otros huéspedes en ningún idioma." + LIM,
    ],
    vocab=[("What time...?", "¿A qué hora...?"), ("How much...?", "¿Cuánto cuesta...?"), ("Where is...?", "¿Dónde está...?"), ("open", "abierto"), ("closes", "cierra"), ("bag", "bolsa")],
    worked=[
        ("Responder un horario", "Una ficha de ejemplo dice «Gym: open from seven to nine p.m.». Un turista pregunta «What time does the gym open?». ¿Qué respondes?", ["La pregunta pide la hora de apertura.", "La ficha dice que abre a las siete."], "«The gym opens at seven»"),
        ("Responder un precio", "Una ficha de ejemplo dice «Towel: one thousand pesos». Un turista pregunta «How much is the towel?». ¿Qué respondes?", ["La pregunta pide el precio.", "La ficha dice mil pesos."], "«The towel is one thousand pesos»"),
    ],
    mistakes=[("Responder la hora de cierre cuando preguntan la hora de apertura.", "El huésped puede llegar cuando el lugar aún está cerrado.", "Identifica si la pregunta es sobre abrir (open) o cerrar (close)."),
              ("Indicar una dirección sin comprobar el lado.", "El huésped va al lugar equivocado.", "Revisa la ficha y usa gestos para señalar.")],
    T=[
        ("abc", "En Hotelería: ¿qué significa «What time...?»", "¿A qué hora...?", "¿Cuánto cuesta...?", "¿Dónde está...?", "What time pregunta por una hora."),
        ("abc", "{F} Un turista pregunta: «What time does the pool close?». ¿Qué respondes?", "The pool closes at eight p.m.", "The pool is on the right", "The pool is two thousand pesos", "Responde la hora de cierre de la ficha."),
        ("abc", "{F} Un turista pregunta: «How much is the laundry?». ¿Qué respondes?", "Two thousand pesos per bag", "From six to nine p.m.", "On the left", "La pregunta pide el precio de la lavandería."),
        ("abc", "{F} Un turista pregunta: «Where is the elevator?». ¿Qué respondes?", "On the left", "On the right", "Straight ahead", "La ficha dice que el ascensor está a la izquierda."),
        ("abc", "{F} Un turista pregunta: «Where are the restrooms?». ¿Qué respondes?", "On the right", "On the left", "At eight p.m.", "La ficha ubica los baños a la derecha."),
        ("abc", "{F} Un turista pregunta: «What time does the restaurant close?». ¿Qué respondes?", "The restaurant closes at nine p.m.", "The restaurant is on the left", "The restaurant is two thousand pesos", "La pregunta pide la hora de cierre y la ficha dice que el restaurante está abierto hasta las nueve de la noche."),
        ("=", "{F} Un turista pide lavar three bags. ¿Cuánto paga?", "3*2000", "Se multiplican las bolsas por el precio de cada una.", " pesos"),
        ("=", "{F} ¿Cuántas horas está abierto el restaurante según la ficha?", "9-6", "Se resta la hora de apertura a la de cierre.", " horas"),
        ("abc", "{F} Un turista pregunta por el spa, que no figura en la ficha. ¿Qué haces?", "Decir con cortesía que consultarás, por ejemplo «Just a moment, please»", "Inventar un horario", "Decir que no hay spa", "Si el dato no está, se consulta y no se inventa."),
        ("abc", "{F} Un turista pregunta «Where is the restaurant?». ¿Qué respondes y cómo ayudas?", "Straight ahead, y señalar con la mano", "On the left, sin gestos", "At six p.m.", "La ficha dice todo recto; los gestos ayudan."),
        ("abc", "{F} Alguien pregunta en inglés qué huésped ocupa la habitación 20. ¿Qué respondes?", "I'm sorry, I can't give that information", "The room is number twenty", "He is on the right", "La privacidad se mantiene en cualquier idioma."),
        ("abc", "{F} ¿Cuál es la respuesta correcta a «What time does the restaurant open?»", "At six p.m.", "At nine p.m.", "Two thousand pesos", "El restaurante abre a las seis según la ficha."),
        ("=", "{F} Si un turista paga la lavandería de two bags con un billete de cinco mil pesos (5.000), ¿cuánto vuelto recibe?", "5000-2*2000", "Al billete se le resta el precio de las dos bolsas.", " pesos"),
    ],
    ctx=("abc", "{F} Una turista pregunta con una sonrisa: «Excuse me, where is the pool?» y la ficha no dice dónde está. ¿Qué haces?", "Decir «Just a moment, please», consultar y volver con la respuesta", "Decir «on the left» al azar", "Decir que no sabes y no ayudar", "Se consulta con cortesía y no se inventa la ubicación."),
    sc=[
        ("En Hotelería: ¿cómo se pregunta «¿cuánto cuesta?» en inglés?", "How much...?", "Es la forma básica de preguntar un precio."),
        ("¿Cómo se dice «a la derecha»?", "On the right", "Es una dirección simple de uso frecuente."),
        ("¿Qué haces si no tienes el dato?", "Consulto con cortesía", "No se inventa información que no se tiene."),
    ],
    op=("Ficha de ejemplo: Gym: open from seven a.m. to nine p.m., on the left. Laundry: one thousand five hundred pesos per bag. Restaurant: open from six to nine p.m., straight ahead. "
        "Un turista pregunta tres cosas: «What time does the gym close?», «How much is the laundry for two bags?» y «Where is the restaurant?». Escribe una respuesta en inglés para cada una y calcula el costo de dos bolsas.",
        "Gym: «The gym closes at nine p.m.». Lavandería: «It is one thousand five hundred pesos per bag; two bags are three thousand pesos». Restaurante: «The restaurant is straight ahead». Costo: 2 × 1.500 = 3.000 pesos.",
        ["responde con el dato correcto de la ficha", "incluye la unidad y el cálculo del precio", "usa la dirección correcta"],
        ["hoja con tres respuestas y el cálculo"],
        ["confundir abrir con cerrar", "olvidar la unidad por bolsa", "decir left en lugar de straight ahead"],
        "Pregunta: «¿a qué hora cierra el gimnasio?». Si responde 'a las siete', repasa la diferencia entre abrir y cerrar."),
    reinforce="Inventa una ficha de información con cuatro datos y escribe cuatro preguntas con sus respuestas en inglés.",
    extend="Explica por qué es útil identificar la palabra clave de una pregunta en inglés.",
)

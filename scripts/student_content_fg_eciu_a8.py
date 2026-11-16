"""Educación Ciudadana 4.º medio FG: OA 07 (territorio, espacio público, interculturalidad e inclusión) y OA 08 (principios éticos, virtudes públicas y decisiones ciudadanas). Casos y cifras de ejemplo inventados."""
from __future__ import annotations

from fg_eciu_common import build

O7 = "FG-ECIU-4M-OAC-07"
O8 = "FG-ECIU-4M-OAC-08"

# ============================================================ OA 07, clase 1
F = ("Ficha 69 (barrio ficticio de ejemplo, Las Palmas): una plaza central con bancas, una cancha y una feria los sábados; sin rampas, con poca luz de noche; "
     "en el barrio viven familias de distintos orígenes, personas mayores, jóvenes y personas con discapacidad. Hay una junta de vecinos, un club deportivo y un grupo de adultos mayores. "
     "El municipio decide sobre el mantenimiento y los vecinos pueden proponer mejoras.")
build(
    O7, 1, F,
    use="Aprenderé qué es el espacio público, cómo se organiza el territorio para la vida en comunidad y qué significan la acción colectiva, la interculturalidad y la inclusión.",
    prior=["Sé qué es un territorio y una escala.", "Sé qué es la inclusión.", "Sé qué es participar."],
    explain=[
        "El espacio público es el espacio de uso común y acceso libre, como calles, plazas, parques y veredas. Es el lugar donde las personas se encuentran, conversan, se organizan y ejercen derechos como la reunión y la expresión. Su diseño y cuidado influyen en la seguridad, la salud y la convivencia. Un buen espacio público es accesible, seguro, iluminado, limpio y usado por distintos grupos.",
        "El territorio se organiza con reglas, equipamientos y decisiones de distintas autoridades. Los vecinos y vecinas participan mediante la acción colectiva, es decir, el esfuerzo conjunto para lograr un fin común, como una junta de vecinos o un club deportivo. La planificación participativa invita a la comunidad a opinar antes de decidir.",
        "La interculturalidad es el diálogo respetuoso entre personas de culturas distintas, que reconoce lo que cada una aporta y no impone una sobre otra. La inclusión es diseñar para que todas las personas puedan participar. El diseño universal busca que los espacios puedan usarse por todas y todos, por ejemplo con rampas y señales claras. Las tradiciones de los pueblos originarios las explican sus comunidades y educadores tradicionales.",
    ],
    vocab=[("espacio público", "espacio de uso común y acceso libre, como una plaza o una calle"), ("acción colectiva", "esfuerzo conjunto de varias personas para lograr un fin común"), ("planificación participativa", "forma de decidir en que la comunidad opina antes de actuar"), ("interculturalidad", "diálogo respetuoso entre culturas que reconoce lo que cada una aporta"), ("diseño universal", "diseño que permite que todas las personas usen un espacio")],
    worked=[
        ("Reconocer una barrera", "Una plaza de ejemplo tiene gradas sin rampa. ¿Qué principio se afecta?", ["Algunas personas no pueden entrar.", "Falta inclusión y diseño universal."], "Inclusión y diseño universal"),
        ("Acción colectiva", "Vecinos de ejemplo se organizan para pintar un muro. ¿Qué tipo de acción es?", ["Varias personas se unen para un fin común.", "Es acción colectiva."], "Acción colectiva"),
    ],
    mistakes=[("Pensar que el espacio público es del municipio y no de la comunidad.", "Es de uso común y se puede opinar sobre él.", "Pregunta cómo participan las personas."),
              ("Confundir interculturalidad con convivir sin conocerse.", "Implica diálogo y reconocimiento.", "Busca espacios de encuentro y diálogo.")],
    T=[
        ('abc', '¿Qué es el espacio público?', 'Un espacio de uso común y acceso libre, como calles, plazas y parques', 'Cualquier terreno que pertenece al municipio y que está cercado', 'Un lugar al que solo acceden quienes viven cerca de él', 'El espacio público es de todas las personas, no de un grupo ni de un propietario.'),
        ('abc', '¿Qué es la acción colectiva?', 'El esfuerzo conjunto de varias personas para lograr un fin común', 'Una decisión que toma una autoridad por su cuenta', 'Una actividad que cada persona hace por separado', 'Se hace entre varias personas con un objetivo compartido.'),
        ('abc', '{F} ¿Qué son la junta de vecinos y el club deportivo del barrio?', 'Organizaciones de acción colectiva', 'Órganos del municipio que deciden el mantenimiento', 'Negocios del barrio', 'Reúnen a personas del barrio para fines comunes.'),
        ('abc', '{F} ¿Qué mejora la inclusión en la plaza?', 'Construir rampas y señales claras para que todas las personas la usen', 'Quitar las bancas para ampliar el espacio de la plaza', 'Reservar la plaza para un solo grupo de usuarios', 'Elimina barreras que impiden la participación de algunas personas.'),
        ('abc', '{F} ¿Qué mejora la seguridad de noche en la plaza?', 'Mejorar la iluminación y mantener la plaza activa de noche', 'Cerrar la plaza con rejas durante toda la noche', 'Prohibir el uso a los jóvenes después de cierta hora', 'Un espacio bien iluminado y usado es más seguro; cerrar o prohibir limita el uso común.'),
        ('abc', '¿Qué es la planificación participativa?', 'Invitar a la comunidad a opinar antes de decidir', 'Que una sola autoridad decida y luego informe', 'Que decida el grupo más grande del barrio', 'Incluye la voz de quienes usarán el espacio antes de decidir.'),
        ('abc', '¿Qué es la interculturalidad?', 'El diálogo respetuoso entre personas de culturas distintas, sin imponer una sobre otra', 'Que todas las personas adopten la cultura mayoritaria del barrio', 'Que cada cultura se mantenga separada de las demás sin mezclarse', 'Reconoce lo que cada cultura aporta.'),
        ('abc', '{F} ¿Qué actividad de la plaza podría fomentar la interculturalidad?', 'Una feria donde familias de distintos orígenes compartan sus saberes', 'Una feria con puestos de un solo origen y un solo tipo de producto', 'Una feria donde se prohíbe hablar otras lenguas en los puestos', 'Promueve el encuentro y el diálogo entre culturas.'),
        ('abc', '{F} Alguien dice: «El espacio público es solo para quienes viven al lado». ¿Qué corresponde?', 'Recordar que es de uso común y de acceso libre para todas las personas', 'Aceptarlo, porque los vecinos cercanos lo cuidan mucho más', 'Rechazarlo, porque en la práctica nadie lo cuida', 'Que sea público significa que no pertenece a un grupo en particular.'),
        ('abc', '{F} ¿Qué es el diseño universal?', 'Que todas las personas puedan usar los espacios, por ejemplo con rampas y señales', 'Que el mismo diseño se copie en todas las ciudades del país', 'Que el espacio se adapte solo a personas con discapacidad', 'Busca que el diseño sirva a todas las personas desde el inicio.'),
        ('abc', '{F} ¿Quién debe explicar las tradiciones de un pueblo originario?', 'Sus comunidades y educadores tradicionales', 'Cualquier persona que haya visto un documental', 'Un grupo de estudiantes que lo investigó en internet', 'Son quienes conocen su cultura y su lengua.'),
        ('abc', '{F} ¿Qué pregunta ayuda a evaluar si la plaza es inclusiva?', '¿Quiénes no pueden usarla y por qué?', '¿Cuántos postes tiene?', '¿Cuál es el grupo que más la usa?', 'Busca barreras, que es lo que impide la inclusión.'),
        ('=', 'Si una plaza es usada por 300 personas un fin de semana y 45 de ellas son adultos mayores, ¿qué porcentaje son?', '45*100//300', 'Se compara la parte con el total de usuarios.', ' %'),
    ],
    ctx=('abc', 'En un parque de ejemplo solo hay juegos para niños de 5 a 10 años. ¿Qué grupos quedan fuera?', 'Jóvenes y personas mayores', 'Niños de 5 a 10 años', 'Ninguno, porque todos juegan', 'El diseño no considera a todos los grupos.'),
    sc=[
        ('¿Qué es un equipamiento urbano?', 'Los elementos como bancas, luminarias y juegos que usan las personas', 'Forman parte de la infraestructura del espacio público.'),
        ('abc', 'En un espacio público, ¿qué es la inclusión?', 'Diseñar para que todas las personas puedan participar', 'Reservar el espacio a un solo grupo de usuarios', 'Aumentar el número de actividades que se ofrecen', 'Se refiere a eliminar barreras para participar.'),
        ('¿Para qué sirve la acción colectiva en un barrio?', 'Para lograr entre varias personas mejoras que una sola no alcanzaría', 'Al sumar esfuerzos y voces se consiguen mejoras que una sola persona no logra.'),
    ],
    op=("Con la {F} haz un plano en palabras de la plaza: cuatro elementos, cuatro grupos de personas que la usan y una barrera para cada grupo. Después propone tres mejoras que incluyan a todas y todos.",
        "Elementos: bancas, cancha, feria, calle. Grupos: personas mayores, jóvenes, familias, personas con discapacidad. Barreras: faltan sombra, horarios para jóvenes, espacio de juego, rampas. Mejoras: rampas, iluminación y una feria intercultural.",
        ["identifica grupos y barreras", "propone mejoras inclusivas", "promueve diálogo"], ["plano en palabras", "tres mejoras"], ["olvidar a un grupo", "proponer solo para algunos"],
        "Pregunta cómo invitaría a las personas a opinar."),
    reinforce="Explica con tus palabras tres características de un espacio público inclusivo.",
    extend="Observa un espacio público de tu barrio y anota una barrera y una mejora.",
)

# ============================================================ OA 07, clase 2
F = ("Ficha 70 (caso de ejemplo): en el barrio ficticio de Santa Rosa, la plaza El Encuentro se usa por 300 personas en un fin de semana. "
     "Un diagnóstico de ejemplo registró: iluminación en 2 de 6 postes; 1 rampa para 4 accesos; 3 grupos que la usan (familias, jóvenes, adultos mayores); "
     "conflictos por ruido entre jóvenes y vecinos en 5 de los últimos 10 fines de semana. Fuentes: el diagnóstico, una carta de vecinos y un acta de la junta.")
build(
    O7, 2, F,
    use="Aprenderé a investigar un espacio público con datos y fuentes, identificando usos, conflictos y barreras de inclusión.",
    prior=["Sé qué es el espacio público.", "Sé calcular proporciones simples.", "Sé comparar fuentes."],
    explain=[
        "Para investigar un espacio público se registran datos: cuántas personas lo usan, qué grupos, qué infraestructura tiene, en qué estado, en qué horarios y qué conflictos existen. Se complementa con la voz de las personas usuarias. Un diagnóstico participativo combina datos y opiniones para decidir mejoras.",
        "Las proporciones ayudan a ver el problema: «2 de 6 postes con luz» significa que faltan 4. «1 rampa para 4 accesos» muestra que hay 3 accesos sin rampa. Los conflictos, como el ruido, no son culpa de un solo grupo: hay que entender horarios, necesidades y reglas. Para este análisis se usan fuentes con propósitos distintos: datos, cartas y actas.",
        "Una conclusión prudente dice qué mejoras son urgentes, quién podría implementarlas y qué falta averiguar. Las soluciones se piensan con quienes usan el espacio, incluyendo a quienes tienen más barreras para participar. Se evita estigmatizar a un grupo (por ejemplo, «los jóvenes molestan») sin evidencia.",
    ],
    vocab=[("diagnóstico participativo", "estudio de un problema que incluye la voz de las personas afectadas"), ("infraestructura", "elementos construidos, como postes, rampas y bancas"), ("conflicto de uso", "desacuerdo entre personas por el uso de un espacio"), ("estigmatizar", "marcar de modo negativo a un grupo de personas"), ("acceso", "entrada o posibilidad de llegar a un lugar")],
    worked=[
        ("Calcular lo que falta", "Un parque de ejemplo tiene 3 de 8 postes con luz. ¿Cuántos faltan?", ["Se resta 3 a 8.", "Faltan 5."], "5 postes"),
        ("Evitar estigmatizar", "Una carta de ejemplo dice «los jóvenes arruinan la plaza». ¿Qué se hace?", ["Se piden datos.", "Se escucha a los jóvenes."], "Pedir datos y escuchar a los jóvenes"),
    ],
    mistakes=[("Culpar a un grupo de los conflictos sin datos.", "Se estigmatiza.", "Revisa horarios y necesidades."),
              ("Mirar solo los datos y no la voz de las personas.", "Se pierde información importante.", "Combina datos y opiniones.")],
    T=[
        ('abc', '¿Qué es un diagnóstico participativo?', 'Un estudio que combina datos y opiniones de quienes usan el espacio', 'Un informe hecho solo por técnicos del municipio sin consultar', 'Una votación para elegir un proyecto entre varios', 'Incluye la voz de las personas afectadas además de las cifras.'),
        ('=', '{F} ¿Cuántos postes deben instalarse o repararse para que los 6 tengan luz?', '6-2', 'Se resta los postes que tienen luz al total.', ' postes'),
        ('=', '{F} ¿Qué porcentaje de los accesos no tiene rampa?', '(4-1)*100//4', 'Se calcula los accesos sin rampa y se compara con el total.', ' %'),
        ('=', '{F} ¿Qué porcentaje de los últimos 10 fines de semana tuvo conflicto por ruido?', '5*100//10', 'Se compara la parte con el total de fines de semana.', ' %'),
        ('abc', '{F} ¿Qué problema de inclusión muestra el dato de la rampa?', 'Tres de los cuatro accesos no son utilizables por algunas personas', 'Hay demasiadas rampas para el número de accesos de la plaza', 'La rampa es innecesaria si hay escaleras en los otros accesos', 'Con una rampa para cuatro accesos, la mayoría de ellos no son accesibles.'),
        ('abc', '{F} ¿Qué problema de seguridad muestra el dato de los postes?', 'La plaza está poco iluminada, lo que reduce la seguridad de noche', 'La plaza tiene exceso de luz que molesta a los vecinos', 'Los postes están en buen estado y alumbran bien toda la plaza', 'Solo 2 de 6 postes tienen luz.'),
        ('abc', '{F} ¿Qué fuente muestra datos?', 'El diagnóstico, que registra cifras', 'La carta de vecinos, que expresa una preocupación', 'El acta de la junta, que registra opiniones', 'Cada fuente tiene un propósito; el diagnóstico es el que cuenta y mide.'),
        ('abc', '{F} Alguien dice: «Los jóvenes son los culpables del ruido». ¿Qué corresponde?', 'Pedir datos de horarios y escuchar a los jóvenes antes de atribuir culpas', 'Aceptarlo, porque hubo conflictos en 5 de 10 fines de semana', 'Rechazarlo, porque los jóvenes nunca hacen ruido', 'No se estigmatiza a un grupo sin evidencia.'),
        ('abc', '{F} ¿Qué conclusión es prudente?', 'Hay problemas de iluminación, accesibilidad y convivencia que se abordan con la comunidad', 'Hay que cerrar la plaza por las noches para evitar los conflictos', 'El problema principal es el ruido de los jóvenes y debe resolverse primero', 'Se apoya en los datos del diagnóstico sin culpar a un grupo.'),
        ('abc', '{F} ¿Qué dato falta para decidir un orden de prioridad?', 'Cuánto cuesta cada mejora y quién puede financiarla', 'Qué opinan los vecinos de otra comuna sobre el proyecto', 'Cuántos postes tenía la plaza hace veinte años', 'Permite priorizar según recursos y responsables.'),
        ('abc', 'Un diagnóstico de ejemplo muestra que una cancha solo la usan hombres. ¿Qué pregunta conviene hacer?', '¿Qué barreras tienen las mujeres para usarla?', '¿Quién llega primero a jugar en la cancha?', '¿Cuántos balones tiene el club deportivo?', 'Busca las causas y las barreras que limitan el uso.'),
        ('abc', '{F} ¿Qué es la infraestructura de la plaza?', 'Los elementos construidos, como postes y rampas', 'Las opiniones de las personas que la usan', 'Las normas de convivencia', 'Es lo construido, que se puede contar y evaluar.'),
        ('abc', '{F} ¿Qué es un conflicto de uso?', 'Un desacuerdo entre personas o grupos por el uso de un espacio', 'Un daño causado al espacio por un grupo de usuarios', 'Un reclamo ante el municipio por falta de mantención', 'Se resuelve entendiendo horarios, necesidades y reglas.'),
    ],
    ctx=('abc', 'Para decidir mejoras, ¿qué combina un diagnóstico participativo?', 'Datos y opiniones de quienes usan el espacio', 'Solo la opinión del alcalde y de su equipo', 'Solo datos de otras ciudades sobre espacios parecidos', 'Los datos miden y las voces explican.'),
    sc=[
        ('¿Qué es estigmatizar a un grupo?', 'Marcarlo de manera negativa sin evidencia', 'Por ejemplo, decir que «los jóvenes molestan» sin datos.'),
        ('abc', '¿Qué es el acceso a un espacio público?', 'La posibilidad real de llegar y usarlo, sin barreras', 'El derecho a cobrar por usarlo para mantenerlo', 'El número de entradas que tiene el espacio', 'El acceso depende de rampas, iluminación y seguridad.'),
        ('¿Por qué se complementan los datos con la voz de las personas?', 'Porque los datos miden y las voces explican lo que viven', 'Con ambos se obtiene un diagnóstico que mide y también explica lo que viven las personas.'),
    ],
    op=("Con la {F} haz un informe de cinco puntos: dos datos de infraestructura con lo que falta, un conflicto, una barrera de inclusión, una mejora urgente y quién debería opinar antes de decidir.",
        "Faltan luz en 4 de 6 postes y rampas en 3 de 4 accesos. Conflicto: ruido en 5 de 10 fines de semana. Barrera: personas con discapacidad no pueden entrar por 3 accesos. Mejora urgente: rampas e iluminación. Opinan: vecinos, jóvenes, adultos mayores y personas con discapacidad.",
        ["calcula lo que falta", "no estigmatiza", "incluye a quienes opinan"], ["informe de cinco puntos"], ["culpar a un grupo", "olvidar a quienes tienen barreras"],
        "Pregunta cómo reuniría las opiniones."),
    reinforce="Calcula cuántos postes sin luz hay en una plaza con 10 postes y 4 con luz.",
    extend="Anota un conflicto de uso que veas en tu barrio y quién debería opinar.",
)

# ============================================================ OA 07, clase 3
F = ("Ficha 71 (perspectivas de ejemplo sobre el uso de una plaza en el barrio ficticio Las Lomas). "
     "Perspectiva 1 (vecina): «Necesitamos silencio en la noche y que se cuide el pasto». "
     "Perspectiva 2 (joven skater): «Queremos un espacio para practicar y reunirnos; no hay otro cercano». "
     "Perspectiva 3 (comerciante de la feria): «La feria da trabajo y atrae gente; necesitamos espacio y electricidad». "
     "Perspectiva 4 (adulta mayor): «Queremos bancas con sombra y senderos sin gradas». "
     "Dato de ejemplo: la plaza mide 1.000 metros cuadrados (m²): 600 son pasto, 200 pista, 200 feria.")
build(
    O7, 3, F,
    use="Aprenderé a contrastar usos de un espacio público y a proponer una organización que promueva la acción colectiva, la inclusión y el diálogo entre grupos.",
    prior=["Sé qué es el espacio público.", "Sé comparar perspectivas.", "Sé calcular partes de un total."],
    explain=[
        "Un espacio público suele tener usos en competencia: descanso, deporte, comercio y encuentro. Cada grupo tiene necesidades legítimas. Contrastar significa identificar qué valor defiende cada uno (tranquilidad, recreación, trabajo, accesibilidad) y cómo se distribuye el espacio. La inclusión pide que ningún grupo quede sistemáticamente fuera.",
        "El espacio se puede organizar por zonas y horarios. Una zona puede ser silenciosa; otra, deportiva; otra, de feria en ciertos días. Los acuerdos se escriben en normas de convivencia que definan reglas, horarios y responsables. Un dato, como los metros cuadrados disponibles, ayuda a ver los límites, pero no decide por sí solo: hay que conversar.",
        "La interculturalidad aparece cuando los grupos dialogan y reconocen lo que cada uno aporta. Una mesa de diálogo con representantes de todos los grupos puede proponer soluciones, probarlas por un tiempo y evaluarlas. El objetivo no es que todos ganen todo, sino que todos sean escuchados y que el resultado sea justo.",
    ],
    vocab=[("uso en competencia", "situación en que varios grupos quieren usar un mismo espacio para fines distintos"), ("zonificación", "división de un espacio en áreas con usos distintos"), ("norma de convivencia", "regla acordada para convivir en un espacio"), ("mesa de diálogo", "espacio donde representantes de distintos grupos conversan para acordar"), ("prueba piloto", "ensayo de una medida por un tiempo para evaluarla")],
    worked=[
        ("Repartir un espacio", "Una plaza de ejemplo de 500 m² reserva 100 m² para juegos y 150 m² para pasto. ¿Cuántos quedan para otros usos?", ["Se suman 100 y 150.", "Se resta de 500."], "250 m²"),
        ("Acuerdo de horarios", "Un grupo quiere música fuerte en la tarde y otro silencio. ¿Qué acuerdo ayuda?", ["Definir horarios.", "Por ejemplo, música hasta cierta hora."], "Un horario acordado"),
    ],
    mistakes=[("Decidir por el grupo que más ruido hace.", "Se excluye a quien tiene menos voz.", "Escucha a todos los grupos."),
              ("Creer que el dato de los metros cuadrados decide.", "Los valores también pesan.", "Usa el dato y conversa.")],
    T=[
        ('abc', '¿Qué es un uso en competencia de un espacio público?', 'Una situación en que distintos grupos necesitan el mismo espacio para usos diferentes', 'Una situación en que un grupo usa el espacio sin autorización', 'Una situación en que el espacio no se usa por falta de interés', 'Los usos como descanso, deporte y comercio pueden competir por el mismo lugar.'),
        ('=', '{F} ¿Cuántos m² suman la pista y la feria?', '200+200', 'Se suman ambas superficies.', ' m²'),
        ('=', '{F} ¿Qué porcentaje de la plaza es pasto?', '600*100//1000', 'Se compara el pasto con el total de 1.000 m².', ' %'),
        ('=', '{F} Si la pista se ampliara en 100 m² quitándolos al pasto, ¿qué porcentaje de la plaza sería pasto?', '(600-100)*100//1000', 'Se calcula el pasto restante y se compara con el total.', ' %'),
        ('abc', '{F} ¿Qué valor defiende la vecina?', 'Tranquilidad y cuidado del espacio', 'Trabajo y actividad económica', 'Recreación y deporte', 'Pide silencio en la noche y que se cuide el pasto.'),
        ('abc', '{F} ¿Qué valor defiende la comerciante?', 'Trabajo y actividad económica de la feria del barrio', 'Silencio durante la noche', 'Deporte en la pista de skate', 'Habla del empleo que da la feria.'),
        ('abc', '{F} ¿Qué valor defiende la adulta mayor?', 'Accesibilidad', 'Deporte extremo', 'Silencio nocturno', 'Pide bancas con sombra y senderos sin gradas.'),
        ('abc', '{F} ¿Qué valor defiende el joven skater?', 'Recreación y un lugar de encuentro para jóvenes', 'Silencio y descanso en la noche', 'Mayor actividad comercial en la plaza', 'Quiere un espacio para practicar y reunirse.'),
        ('abc', '{F} ¿Qué es la zonificación?', 'Dividir el espacio en áreas con usos distintos', 'Cerrar el espacio hasta decidir', 'Ceder todo el espacio al grupo más grande', 'Ordena los usos para que convivan.'),
        ('abc', '{F} ¿Qué propuesta combina las cuatro perspectivas?', 'Zonas y horarios acordados, senderos accesibles y prueba piloto evaluada', 'Dar todo el espacio a un grupo y excluir a los demás', 'Mantener la plaza sin cambios aunque haya conflictos', 'Incluye lo que cada grupo necesita.'),
        ('abc', '{F} Alguien dice: «Los metros cuadrados dicen que el pasto debe quedarse». ¿Qué corresponde?', 'Recordar que el dato muestra límites, pero decidir implica conversar', 'Aceptarlo, porque el pasto ocupa más superficie', 'Rechazarlo, porque el pasto no tiene ningún valor', 'El dato no decide solo: también pesan los valores y necesidades.'),
        ('abc', '{F} ¿Qué haría más inclusiva la mesa de diálogo?', 'Invitar a representantes de todos los grupos', 'Invitar solo a la junta de vecinos', 'Invitar solo a quienes ya participan', 'Todos los grupos deben ser escuchados.'),
        ('abc', '{F} ¿Qué indicador mostraría si la prueba piloto funciona?', 'Conflictos registrados y satisfacción de los grupos', 'Cantidad de carteles instalados en la plaza', 'Cantidad de reuniones realizadas por la junta', 'Mide el resultado de la medida.'),
    ],
    ctx=('abc', 'Un curso comparte la sala con otro y hay conflictos por el uso. ¿Qué solución es buena?', 'Acordar horarios y reglas con ambos cursos', 'Que uno se imponga sobre el otro según el curso', 'Dividir la sala con una línea sin conversar', 'Un acuerdo de horarios y reglas permite que ambos cursos usen la sala.'),
    sc=[
        ('¿Qué es una norma de convivencia?', 'Una regla acordada sobre horarios, usos y responsables de un espacio', 'Ayuda a prevenir conflictos de uso.'),
        ('abc', '¿Qué es una mesa de diálogo?', 'Un espacio donde representantes de distintos grupos conversan', 'Una reunión de la directiva de la junta de vecinos', 'Una votación entre dos opciones con mayoría simple', 'Reúne a los grupos para buscar soluciones en común.'),
        ('En Educación Ciudadana: ¿Qué es una prueba piloto?', 'El ensayo de una medida por un tiempo para evaluarla', 'Permite ajustar la medida antes de aplicarla de forma definitiva.'),
    ],
    op=("Con la {F} diseña una zonificación: cuántos m² para pasto, pista, feria, senderos accesibles y sombra (deben sumar 1.000), horarios y una norma de convivencia para cada grupo. Explica cómo se evaluará.",
        "Pasto 500 m², pista 200 m², feria 200 m², senderos y sombra 100 m². Horarios: música hasta las 21:00; feria sábado. Normas: silencio después de las 22:00, la feria deja el espacio limpio. Evaluación: prueba piloto de un mes con registro de conflictos.",
        ["suma 1.000", "considera a los cuatro grupos", "incluye evaluación"], ["zonificación", "normas"], ["no sumar el total", "olvidar un grupo"],
        "Pregunta quién tendría la última palabra y por qué."),
    reinforce="Reparte 800 m² entre tres usos y justifica tu elección.",
    extend="Observa cómo se reparten los usos en un espacio de tu comunidad.",
)

# ============================================================ OA 07, clase 4
F = ("Ficha 72 (tema de deliberación de ejemplo): el municipio ficticio de Pueblo Nuevo debe decidir cómo mejorar una plaza con un presupuesto de 8 millones de pesos. "
     "Opción 1: iluminación y rampas (6 millones) más bancas (2 millones). Opción 2: un escenario para ferias interculturales (7 millones) y un poste de luz (1 millón). "
     "Opción 3: un mural participativo (1 millón), rampas (3 millones) y luces (4 millones). Evaluación de ejemplo (1 a 5) en inclusión, seguridad e interculturalidad: Op. 1 = 5, 4, 2; Op. 2 = 2, 2, 5; Op. 3 = 4, 4, 4.")
build(
    O7, 4, F,
    use="Aprenderé a deliberar y a proponer cómo organizar un espacio público para promover la acción colectiva, la interculturalidad y la inclusión con un presupuesto limitado.",
    prior=["Sé contrastar usos de un espacio.", "Sé usar una matriz de criterios.", "Sé sumar y comparar."],
    explain=[
        "Un presupuesto limitado obliga a priorizar. Una forma de ordenar la decisión es una matriz de criterios: se asigna un puntaje a cada opción en inclusión, seguridad e interculturalidad y se suma. Pero la matriz no decide sola: se discute qué significa cada puntaje y si algún criterio es indispensable, como que el espacio sea accesible.",
        "Las propuestas de espacio público deben pensar en la participación: quién opina, quién cuida el espacio y cómo se mantendrá. Un mural participativo, por ejemplo, convoca a la comunidad y refuerza la identidad; un escenario favorece el encuentro intercultural, pero si no hay rampas deja fuera a algunas personas. Combinar medidas puede ser mejor que elegir una sola.",
        "Una propuesta sólida define objetivos, costos, responsables, plazo y un indicador. Reconoce los límites: el presupuesto no alcanza para todo. Se compromete a evaluar y a mantener el espacio. Se respeta el derecho de las minorías a ser escuchadas y a que su postura quede registrada.",
    ],
    vocab=[("presupuesto limitado", "cantidad de dinero que no alcanza para hacer todo lo deseado"), ("priorizar", "ordenar según la importancia o urgencia"), ("mural participativo", "pintura colectiva hecha con la comunidad"), ("mantenimiento", "cuidado continuo de un espacio"), ("corresponsabilidad", "responsabilidad compartida entre autoridades y comunidad")],
    worked=[
        ("Sumar costos", "Una opción de ejemplo cuesta 3 millones en rampas y 2 millones en luces. ¿Cuánto cuesta en total?", ["Se suman los costos.", "3 más 2."], "5 millones"),
        ("Criterio indispensable", "Una opción de ejemplo tiene alto puntaje, pero deja el acceso inaccesible. ¿Qué se hace?", ["Se revisa el criterio indispensable.", "Se ajusta la opción."], "Ajustar para que sea accesible"),
    ],
    mistakes=[("Elegir solo por el puntaje total.", "Puede dejar fuera un criterio indispensable.", "Revisa criterios imprescindibles."),
              ("No pensar en el mantenimiento.", "El espacio se deteriora.", "Define responsables.")],
    T=[
        ('abc', '¿Qué significa priorizar?', 'Ordenar según la importancia o urgencia', 'Elegir lo más barato', 'Elegir lo que prefiere la mayoría', 'Un presupuesto limitado obliga a decidir qué primero.'),
        ('=', '{F} ¿Cuál es el total de puntajes de la opción 1 (5, 4, 2)?', '5+4+2', 'Se suman los tres puntajes.', ' puntos'),
        ('=', '{F} ¿Cuál es el total de puntajes de la opción 3 (4, 4, 4)?', '4+4+4', 'Se suman los tres puntajes.', ' puntos'),
        ('=', '{F} ¿Cuánto cuesta en total la opción 2 (7 y 1 millones)?', '7+1', 'Se suman los dos costos.', ' millones'),
        ('abc', '{F} ¿Qué opción tiene el total más alto?', 'La opción 3, con 12 puntos', 'La opción 1, con 11 puntos', 'La opción 2, con 9 puntos', 'Los totales son 11, 9 y 12.'),
        ('abc', '{F} ¿Qué opción tiene el mayor puntaje de interculturalidad?', 'La opción 2, con 5', 'La opción 1, con 5', 'La opción 3, con 4', 'La opción 2 obtiene 5 en interculturalidad.'),
        ('abc', '{F} ¿Qué problema tiene la opción 2 para la inclusión?', 'Obtiene 2 en inclusión: no incluye rampas', 'Cuesta más que el presupuesto', 'No promueve la interculturalidad', 'Un escenario sin rampas deja fuera a algunas personas.'),
        ('abc', '{F} Si la comunidad considera indispensable que el espacio sea accesible, ¿qué ocurre con la opción 2?', 'Queda en desventaja, aunque tenga el mayor puntaje intercultural', 'Se vuelve la mejor opción por tener el mayor puntaje intercultural', 'No cambia nada, porque la suma de puntajes decide sola', 'Un criterio indispensable puede descartar una opción aunque tenga otros puntajes altos.'),
        ('abc', '{F} ¿Qué ventaja tiene el mural participativo?', 'Convoca a la comunidad y refuerza la identidad', 'Aumenta los costos de mantención de la plaza', 'Reduce la participación de los vecinos', 'Se pinta entre muchas personas, lo que convoca a la comunidad.'),
        ('abc', '{F} Alguien dice: «La suma decide, no hay que discutir». ¿Qué corresponde?', 'Recordar que los puntajes se discuten y hay criterios indispensables', 'Aceptarlo, porque la suma de los puntajes es objetiva', 'Rechazar las matrices, porque no sirven para decidir', 'La matriz ordena la discusión, pero no decide sola.'),
        ('abc', '{F} ¿Qué propuesta combinada es más sólida?', 'Rampas, luces y un mural participativo, y financiamiento aparte para un escenario', 'Gastar todo en un escenario y dejar las rampas para después', 'Gastar todo en luces y nada en rampas ni en el mural', 'Cuida inclusión y diálogo con el presupuesto disponible.'),
        ('abc', '{F} ¿Qué haría sostenible la mejora?', 'Definir responsables del mantenimiento con apoyo de la comunidad', 'Dejar el cuidado al azar y que cada vecino decida si ayuda', 'Esperar que el municipio lo haga todo sin colaboración', 'Con responsables claros el espacio se cuida y no se deteriora con el tiempo.'),
        ('abc', '{F} ¿Qué indicador mostraría que la propuesta tuvo éxito?', 'Uso del espacio por distintos grupos y accesos sin barreras', 'Cantidad de discursos de autoridades sobre la plaza', 'Número de bancas instaladas en el espacio', 'Mide el efecto en la inclusión y el uso.'),
    ],
    ctx=('abc', 'Un liceo destina $100.000 a su patio. ¿Qué paso garantiza una buena decisión?', 'Consultar a distintos cursos y priorizar con criterios', 'Decidir en privado entre la dirección y el centro de estudiantes', 'Gastar en lo primero que se proponga en la reunión', 'Incluye la participación y ordena la decisión.'),
    sc=[
        ('¿Qué es un mural participativo?', 'Una obra que se pinta entre muchas personas de la comunidad', 'Convoca a la comunidad y refuerza la identidad.'),
        ('abc', '¿Qué es el mantenimiento de un espacio?', 'El cuidado continuo de un espacio', 'La construcción de un espacio nuevo', 'El cierre de un espacio por un tiempo', 'Evita el deterioro con el paso del tiempo.'),
        ('En Educación Ciudadana: ¿Qué es la corresponsabilidad?', 'La responsabilidad compartida entre autoridades y comunidad', 'Todas las partes se hacen cargo del cuidado.'),
    ],
    op=("Con la {F} escribe una propuesta de siete líneas: opción o combinación elegida (el costo no puede superar 8 millones), criterios, un beneficio, un límite, cómo participará la comunidad, quién mantendrá el espacio y un indicador.",
        "Elijo rampas (3), luces (4) y mural participativo (1): 8 millones. Criterios: inclusión, seguridad e interculturalidad. Beneficio: accesibilidad y encuentro. Límite: no alcanza para un escenario. Participación: el mural lo pinta la comunidad. Mantenimiento: la junta y el municipio. Indicador: usos y accesos.",
        ["respeta el presupuesto", "incluye mantenimiento", "incluye participación"], ["propuesta de siete líneas"], ["superar el presupuesto", "olvidar la inclusión"],
        "Pregunta qué sacrificaría si el presupuesto se redujera a 6 millones."),
    reinforce="Explica por qué la matriz no decide sola.",
    extend="Propón una mejora de bajo costo para un espacio de tu liceo.",
)

# ============================================================ OA 08, clase 1
F = ("Ficha 73 (situaciones de ejemplo): (1) Un funcionario municipal de ejemplo recibe un regalo caro de una empresa que quiere ganar una licitación. "
     "(2) Una vecina ve que un camión vierte escombros en un terreno y duda si denunciar. "
     "(3) Un estudiante nota que un compañero copia en una evaluación. "
     "(4) Un delegado de curso tiene que decidir cómo usar $30.000 del curso y un amigo le pide que lo destine a su cumpleaños.")
build(
    O8, 1, F,
    use="Aprenderé qué son los principios éticos y las virtudes públicas y cómo se usan para tomar decisiones ciudadanas que resguarden la dignidad de las personas y la vida en democracia.",
    prior=["Sé qué son los derechos humanos.", "Sé qué es la probidad.", "Sé qué es una norma justa."],
    explain=[
        "La ética reflexiona sobre qué es correcto hacer y por qué. Un principio ético es una idea que orienta la acción, como la dignidad (todas las personas valen), la justicia (dar a cada quien lo que corresponde), la honestidad (decir y hacer la verdad), la responsabilidad (hacerse cargo de las consecuencias) y el respeto. En democracia, estos principios se expresan en los derechos humanos y en las normas.",
        "Las virtudes públicas son cualidades de carácter que ayudan a vivir en comunidad: la honestidad, la justicia, la prudencia (decidir con cuidado), la solidaridad, la valentía cívica (actuar por el bien común aunque cueste) y la tolerancia (respetar al que piensa distinto). Se desarrollan con la práctica, no solo con las ideas.",
        "Una decisión fundada sigue pasos: ver los hechos, identificar los valores en juego, pensar opciones, imaginar consecuencias para todas las personas, comprobar que se respeta la dignidad y que se aceptaría que otros actuaran igual, decidir y estar dispuesto a explicar la decisión. Si hay riesgo para alguien, se avisa a una persona adulta de confianza.",
    ],
    vocab=[("principio ético", "idea que orienta la acción correcta, como la dignidad o la justicia"), ("virtud pública", "cualidad de carácter que ayuda a vivir bien en comunidad"), ("prudencia", "decidir con cuidado considerando las consecuencias"), ("valentía cívica", "actuar por el bien común aunque cueste"), ("dilema ético", "situación en que dos valores o deberes se enfrentan")],
    worked=[
        ("Identificar el principio", "Un jurado de ejemplo ayuda a un amigo porque es su amigo. ¿Qué principio se vulnera?", ["No trata a todos por igual.", "Es la justicia."], "Justicia"),
        ("Identificar una virtud", "Una joven de ejemplo informa un abuso de poder aunque teme represalias. ¿Qué virtud muestra?", ["Actúa por el bien común aunque cueste.", "Es valentía cívica."], "Valentía cívica"),
    ],
    mistakes=[("Decidir solo por lo que conviene a uno o a sus amigos.", "Se ignora la justicia.", "Pregunta si todos serían tratados igual."),
              ("Creer que ser honesto es solo no mentir.", "También es no usar el cargo para beneficio propio.", "Revisa conflictos de interés.")],
    T=[
        ('abc', '¿Qué es un principio ético?', 'Una idea que orienta la acción, como la dignidad, la justicia o la honestidad', 'Una norma que impone una sanción a quien la incumple', 'Una preferencia personal sobre lo que se prefiere hacer', 'Orienta lo que es correcto hacer y por qué.'),
        ('abc', '¿Qué son las virtudes públicas?', 'Cualidades de carácter que ayudan a vivir en comunidad, como honestidad y prudencia', 'Conocimientos que se aprenden en la escuela durante la enseñanza media', 'Derechos que reconoce la ley a las personas de una comunidad', 'Se desarrollan con la práctica, no solo con las ideas.'),
        ('abc', '{F} ¿Qué principios se ven afectados en la situación 1 si el funcionario acepta el regalo?', 'Honestidad y justicia: usaría su cargo para favorecer a una empresa', 'Tolerancia: respetar a quien piensa distinto del funcionario', 'Valentía cívica: actuar por el bien común aunque cueste', 'Recibir un regalo de quien busca ganar una licitación compromete su imparcialidad.'),
        ('abc', '{F} ¿Qué virtud sería denunciar el vertido de escombros?', 'Valentía cívica: actuar por el bien común aunque cueste', 'Indiferencia: no involucrarse', 'Tolerancia: aceptar lo que hacen los demás', 'La valentía cívica es actuar por el bien común aunque sea difícil.'),
        ('abc', '{F} ¿Qué valores se enfrentan en la situación 3?', 'Honestidad y justicia con el curso frente a la lealtad con el compañero', 'Libertad de expresión y libertad de reunión de los estudiantes', 'Solidaridad con el curso y valentía cívica del compañero', 'Es un dilema ético porque dos valores se enfrentan.'),
        ('abc', '{F} ¿Qué decisión respeta la justicia en la situación 4?', 'Usar el dinero para el curso, según lo acordado, y explicárselo al amigo', 'Usarlo para el cumpleaños del amigo, que se lo pidió', 'Repartirlo entre los amigos del delegado como regalo', 'El dinero del curso se usa con criterios iguales para todos.'),
        ('abc', '¿Qué es la prudencia?', 'Decidir con cuidado considerando las consecuencias', 'Decidir rápido para no perder oportunidades', 'No decidir nunca para evitar los errores', 'La prudencia consiste en pensar en las consecuencias antes de actuar.'),
        ('abc', '¿Qué es un dilema ético?', 'Una situación en que dos valores o deberes se enfrentan', 'Un error de cálculo en un presupuesto', 'Una situación con una única respuesta obvia', 'No existe una respuesta simple: hay que ponderar valores.'),
        ('abc', '{F} ¿Qué pregunta ayuda a decidir bien?', '¿Aceptaría que todas las personas actuaran de esta forma?', '¿Qué me conviene más a mí en esta situación?', '¿Qué haría la mayoría sin pensarlo mucho?', 'Prueba si la decisión es justa y universalizable.'),
        ('abc', '{F} Alguien dice: «Si nadie se entera, no importa». ¿Qué corresponde?', 'Recordar que la honestidad no depende de que nos vean', 'Aceptarlo, porque no hay daño visible', 'Rechazarlo, porque siempre alguien se entera', 'Los principios éticos no dependen de que haya testigos.'),
        ('abc', '{F} En la situación 3, ¿qué opción respeta la dignidad de todos?', 'Hablar con el compañero o avisar a un docente con respeto, sin humillarlo', 'Burlarse de él frente al curso para que no lo repita', 'Quitarle la hoja y mostrársela a todos para que se sepa', 'Se cuida a todas las personas involucradas.'),
        ('abc', '{F} Si una decisión pone en riesgo a alguien, ¿qué haces?', 'Avisar a una persona adulta de confianza', 'Actuar solo y en secreto', 'Esperar a ver si el problema se resuelve', 'Una persona adulta puede proteger y ayudar a decidir.'),
        ('abc', '¿Cuáles son los pasos de una decisión fundada?', 'Ver los hechos, identificar los valores, pensar opciones, imaginar consecuencias y decidir', 'Decidir primero y buscar después razones que justifiquen la decisión', 'Preguntar a los amigos y hacer lo que ellos digan', 'Una decisión fundada sigue pasos y se puede explicar con razones.'),
    ],
    ctx=('abc', 'Un compañero te pide que le dejes copiar tu tarea. ¿Qué se pone a prueba?', 'La honestidad y la justicia, frente al deseo de ayudar', 'Solo la solidaridad, porque ayudar siempre es lo correcto', 'Solo la prudencia, porque no hay valores en juego', 'Hay un dilema entre ayudar y actuar con honestidad.'),
    sc=[
        ('¿Qué es la valentía cívica?', 'Actuar por el bien común aunque cueste', 'Es una cualidad de carácter que ayuda a vivir en comunidad.'),
        ('abc', '¿Qué es la responsabilidad como principio ético?', 'Hacerse cargo de las consecuencias de lo que se decide', 'Cumplir órdenes sin cuestionarlas, aunque se perjudique a otros', 'Evitar tomar decisiones para no equivocarse nunca', 'Implica asumir lo que ocurre a partir de nuestras decisiones.'),
        ('¿Qué es la justicia como principio ético?', 'Dar a cada quien lo que corresponde', 'Se aplica con criterios claros para todas las personas.'),
    ],
    op=("Con la {F} elige dos situaciones y haz una tabla: valores en juego, opciones, consecuencias, la opción que elegirías y la virtud que muestra. Agrega a quién avisarías si hay riesgo para alguien.",
        "Situación 1: honestidad y justicia; aceptar o rechazar; rechazarlo y avisar a la autoridad; probidad. Situación 3: honestidad y lealtad; ignorar o hablar; hablar con respeto; valentía cívica. Aviso: a un docente o a una persona adulta de confianza.",
        ["identifica valores", "analiza consecuencias", "elige con razones"], ["tabla de dos situaciones"], ["decidir por conveniencia", "no cuidar la dignidad"],
        "Pregunta qué virtud le resulta más difícil de practicar."),
    reinforce="Explica con tus palabras cómo decidir ante un dilema ético en cinco pasos.",
    extend="Anota un dilema pequeño que viviste y qué principio te ayudó a decidir.",
)

# ============================================================ OA 08, clase 2
F = ("Ficha 74 (caso de ejemplo): en la municipalidad ficticia de Costa Alta se investiga si el jefe de compras Daniel adjudicó un contrato de 20 millones de pesos a una empresa de su cuñado, sin concurso. "
     "Fuentes: (1) el contrato firmado; (2) el reglamento, que exige concurso público para compras sobre 10 millones; (3) una declaración de Daniel, que dice que «era la oferta más barata»; (4) una nota que cita a un trabajador que dice haber visto una reunión entre ambos. "
     "El caso aún no ha sido resuelto por ninguna autoridad.")
build(
    O8, 2, F,
    use="Aprenderé a investigar un caso de probidad con prudencia: separar hechos de sospechas, ver qué norma aplica y respetar la presunción de inocencia.",
    prior=["Sé qué es la probidad.", "Sé comparar fuentes.", "Sé qué es la presunción de inocencia."],
    explain=[
        "La probidad es actuar con honestidad en la función pública, sin usar el cargo para beneficios propios o de familiares. Un conflicto de intereses ocurre cuando una persona debe decidir sobre algo en que tiene un interés personal. Las normas, como exigir un concurso público para compras grandes, buscan evitar favoritismos y asegurar transparencia.",
        "Al investigar un caso público se separan los hechos comprobables (el contrato existe, el monto es de 20 millones, el reglamento exige concurso sobre 10 millones) de las sospechas o rumores (la reunión, la intención). La presunción de inocencia exige no declarar culpable a nadie antes de que una autoridad competente lo resuelva. Se pide la evidencia que falta, como si hubo concurso o declaración de intereses.",
        "Una conclusión prudente dice lo que muestran los documentos, lo que falta y qué institución puede decidir. También se cuida la dignidad de las personas: no se difunden acusaciones sin pruebas. Quien tiene información sobre un posible delito puede informar a las autoridades competentes por los canales formales.",
    ],
    vocab=[("conflicto de intereses", "situación en que una persona debe decidir sobre algo en que tiene un interés personal"), ("concurso público", "procedimiento abierto para elegir entre varias ofertas"), ("presunción de inocencia", "principio según el cual nadie es culpable hasta que se demuestre"), ("hecho comprobable", "dato respaldado por un documento o prueba"), ("canal formal", "vía oficial para informar o reclamar")],
    worked=[
        ("Aplicar una norma", "El reglamento de ejemplo exige concurso sobre 5 millones y se compra por 8 millones sin concurso. ¿Se cumplió?", ["8 supera 5.", "Debía haber concurso."], "No se cumplió la norma"),
        ("Hecho y sospecha", "«El contrato existe» y «Daniel quería favorecer a su cuñado». ¿Cuál es hecho?", ["La primera se comprueba con un documento.", "La segunda es una sospecha."], "La primera"),
    ],
    mistakes=[("Declarar culpable a alguien por una sospecha.", "Se vulnera la presunción de inocencia.", "Espera la decisión de la autoridad."),
              ("Difundir el caso en redes antes de verificarlo.", "Puede dañar la honra de una persona.", "Usa los canales formales.")],
    T=[
        ('abc', '¿Qué es un conflicto de intereses?', 'Una situación en que una persona debe decidir sobre algo en que tiene un interés personal', 'Un desacuerdo entre dos funcionarios sobre cómo gastar el presupuesto', 'Una discusión sobre un contrato entre dos empresas del mismo rubro', 'Lo central es el interés personal de quien decide.'),
        ('abc', '¿Qué es la probidad?', 'Actuar con honestidad en la función pública, sin usar el cargo para beneficio propio o familiar', 'Cumplir las instrucciones de un jefe sin cuestionarlas nunca', 'Ahorrar el dinero público en todas las compras', 'La probidad exige honestidad e imparcialidad en el cargo.'),
        ('=', '{F} ¿Qué porcentaje del límite que exige concurso (10 millones) representa el contrato de 20 millones?', '20*100//10', 'Se compara el monto del contrato con el límite.', ' %'),
        ('abc', '{F} ¿Cuál es un hecho comprobable?', 'El contrato firmado por 20 millones', 'La intención de Daniel al elegir la empresa', 'Que hubo favoritismo', 'Hay un documento que lo respalda.'),
        ('abc', '{F} ¿Cuál es una sospecha?', 'Que hubo favoritismo hacia la empresa del cuñado', 'Que el reglamento exige concurso sobre 10 millones', 'Que el contrato existe', 'Aún no está probada: depende de si hubo o no concurso.'),
        ('abc', '{F} ¿Cuál es el posible conflicto de intereses del caso?', 'Que la empresa adjudicada es del cuñado del jefe de compras, quien decidió', 'Que el contrato sea de un monto grande para la municipalidad', 'Que Daniel trabaje en el área de compras de la municipalidad', 'Existe un vínculo personal entre quien decide y quien se beneficia.'),
        ('abc', '{F} ¿Qué falta comprobar?', 'Si hubo concurso público, como exige la norma', 'Si el contrato existe', 'Si Daniel trabaja en la municipalidad', 'Es la clave para saber si se cumplió el reglamento.'),
        ('abc', '{F} ¿Qué principio impide declarar culpable a Daniel hoy?', 'La presunción de inocencia, que protege a todas las personas', 'La probidad, que exige honestidad en el cargo', 'La transparencia, que hace pública la información', 'Nadie es culpable hasta que una autoridad competente lo resuelva.'),
        ('abc', '{F} ¿Qué valor tiene la declaración de Daniel?', 'Es una versión que debe verificarse con documentos', 'Prueba su inocencia, porque dice que era la oferta más barata', 'Prueba su culpa, porque no hubo concurso', 'Una declaración sin respaldo sigue siendo una versión.'),
        ('abc', '{F} ¿Qué valor tiene lo que dice el trabajador de la nota?', 'Es un testimonio que necesita comprobación', 'Es una prueba definitiva de culpa', 'Es un dato sin valor', 'Un testimonio solo se vuelve evidencia cuando otras fuentes lo confirman.'),
        ('abc', '{F} Alguien dice: «Daniel es culpable, publiquémoslo». ¿Qué corresponde?', 'Esperar la decisión de la autoridad y usar los canales formales', 'Publicarlo, porque la ciudadanía debe saber la verdad enseguida', 'Ignorar el caso para no meterse en problemas', 'Se respeta la presunción de inocencia y la dignidad de la persona.'),
        ('abc', '{F} ¿Qué conclusión es prudente?', 'Los documentos sugieren que no hubo concurso, pero falta confirmar y que una autoridad resuelva', 'Daniel es corrupto, porque el contrato es de su cuñado', 'No hay nada irregular porque era la oferta más barata', 'Se limita a lo que muestran los documentos.'),
        ('abc', '{F} Si alguien tiene información sobre un posible delito, ¿a quién puede informar?', 'A las autoridades competentes por los canales formales', 'A nadie, para no perjudicar a la persona', 'A todos sus contactos, para que se sepa', 'Es la vía legítima que respeta derechos.'),
    ],
    ctx=('abc', 'Una presidenta de curso compra materiales a la empresa de su padre sin consultar. ¿Qué principios se afectan?', 'Probidad y transparencia, por el conflicto de intereses', 'Libertad de expresión, por el derecho a opinar', 'Solidaridad, por el apoyo a un familiar', 'Decide sobre algo en que su familia tiene un interés personal.'),
    sc=[
        ('¿Qué es un hecho comprobable?', 'Algo que puede verificarse con documentos o datos', 'Se distingue de una sospecha o un rumor.'),
        ('abc', '¿Qué es un concurso público?', 'Un procedimiento abierto para elegir entre varias ofertas', 'Una elección de funcionarios por sorteo entre postulantes', 'Una compra directa a un proveedor conocido por el municipio', 'Al ser abierto a varias ofertas, evita favoritismos y asegura transparencia.'),
        ('En Educación Ciudadana: ¿Qué es la presunción de inocencia?', 'El principio según el cual nadie es culpable hasta que se demuestre', 'Protege a las personas ante acusaciones sin pruebas.'),
    ],
    op=("Con la {F} escribe un informe de seis líneas: hechos comprobables, sospechas, la norma que se aplica, dos datos que pedirías, la institución a la que se podría informar y una frase que cuide la dignidad de Daniel.",
        "Hechos: contrato por 20 millones; el reglamento exige concurso sobre 10 millones. Sospechas: favoritismo. Norma: concurso público. Datos: si hubo concurso y si hubo declaración de intereses. Institución: autoridades competentes por canales formales. Frase: Daniel tiene derecho a presentar sus descargos.",
        ["separa hechos y sospechas", "aplica la norma", "cuida la dignidad"], ["informe de seis líneas"], ["declarar culpable", "difundir sin pruebas"],
        "Pregunta cómo se comunicaría el caso sin dañar la honra."),
    reinforce="Explica por qué la presunción de inocencia protege a todas las personas.",
    extend="Averigua cómo se hacen las compras o contrataciones en tu liceo.",
)

# ============================================================ OA 08, clase 3
F = ("Ficha 75 (tres enfoques de ejemplo para decidir un dilema: un estudiante sabe que un compañero copió en una prueba que otros prepararon con esfuerzo). "
     "Enfoque 1 (mirar las reglas y los deberes): «Hay una norma de honestidad; hay que informarla». "
     "Enfoque 2 (mirar las consecuencias): «Informar puede dañar al compañero, pero callar perjudica a quienes estudiaron; hay que ver qué produce menos daño y más justicia». "
     "Enfoque 3 (mirar el carácter y las virtudes): «Una persona honesta y prudente conversaría primero con el compañero y, si no basta, hablaría con el docente».")
build(
    O8, 3, F,
    use="Aprenderé a contrastar distintas maneras de razonar éticamente (reglas, consecuencias y virtudes) para tomar decisiones que resguarden la dignidad de todas las personas.",
    prior=["Sé qué es un dilema ético.", "Sé qué son los principios y las virtudes.", "Sé comparar perspectivas."],
    explain=[
        "Hay formas distintas de razonar ante un dilema ético. Una mira las reglas y los deberes: qué norma o principio debe cumplirse. Otra mira las consecuencias: qué opción produce más bien y menos daño para todas las personas. Otra mira el carácter: qué haría una persona honesta, justa y prudente. Cada una aporta algo y todas tienen límites.",
        "Mirar solo las reglas puede olvidar a las personas; mirar solo las consecuencias puede justificar tratar mal a alguien por un fin; mirar solo el carácter puede ser vago si no se aterriza. Por eso se combinan: se parte de los principios, se analizan las consecuencias y se elige una acción coherente con las virtudes.",
        "Estas formas de razonar no son posturas partidistas, sino herramientas. Al contrastarlas, se evita descalificar a quien piensa distinto y se busca una decisión que se pueda explicar con razones. Cuando hay riesgo para alguien, o cuando se necesita ayuda para resolver el dilema, se consulta a una persona adulta de confianza.",
    ],
    vocab=[("enfoque de deberes", "forma de razonar que mira las reglas y principios que deben cumplirse"), ("enfoque de consecuencias", "forma de razonar que mira los efectos de cada opción"), ("enfoque de virtudes", "forma de razonar que mira qué haría una persona de buen carácter"), ("proporcionalidad", "equilibrio entre lo que se hace y la gravedad de la situación"), ("coherencia", "acuerdo entre lo que se piensa, se dice y se hace")],
    worked=[
        ("Identificar el enfoque", "«Debemos cumplir la norma, sin importar lo que pase». ¿Qué enfoque es?", ["Mira las reglas y deberes.", "Es el enfoque de deberes."], "Enfoque de deberes"),
        ("Identificar el límite", "Alguien dice: «Si el resultado es bueno, da lo mismo cómo se logre». ¿Qué riesgo tiene el enfoque de consecuencias?", ["Puede justificar tratar mal a alguien.", "Se olvida la dignidad."], "Puede justificar tratar mal a alguien"),
    ],
    mistakes=[("Quedarse con un solo enfoque y descalificar los otros.", "Cada uno aporta algo.", "Combina enfoques."),
              ("Dar una respuesta de ejemplo sin razones.", "No se puede explicar.", "Justifica con principios y consecuencias.")],
    T=[
        ('abc', '¿Qué mira cada enfoque para razonar ante un dilema?', 'Deberes: las reglas; consecuencias: los efectos; virtudes: el carácter', 'Deberes: los efectos; consecuencias: el carácter; virtudes: las reglas', 'Deberes: el carácter; consecuencias: las reglas; virtudes: los efectos', 'Cada enfoque pone su atención en un aspecto distinto de la decisión.'),
        ('abc', '{F} «Hay una norma de honestidad; hay que informarla». ¿Qué enfoque es?', 'El de deberes', 'El de consecuencias', 'El de virtudes', 'Mira la norma que debe cumplirse.'),
        ('abc', '{F} «Hay que ver qué produce menos daño y más justicia». ¿Qué enfoque es?', 'El de consecuencias, que mira los efectos', 'El de deberes, que mira las reglas', 'El de virtudes, que mira el carácter', 'Se centra en los efectos de cada opción.'),
        ('abc', '{F} «Una persona honesta y prudente conversaría primero». ¿Qué enfoque es?', 'El de virtudes', 'El de deberes', 'El de consecuencias', 'Se pregunta qué haría una persona de buen carácter.'),
        ('abc', '{F} ¿Qué límite tiene el enfoque de deberes?', 'Puede olvidar a las personas y el contexto', 'Ignora todas las reglas de la comunidad', 'Solo mira los resultados de cada acción', 'Aplicar la regla sin mirar el contexto puede ser injusto.'),
        ('abc', '{F} ¿Qué límite tiene el enfoque de consecuencias?', 'Puede justificar tratar mal a alguien por un fin', 'Ignora los resultados de las decisiones', 'No considera ninguna consecuencia de lo que se hace', 'Mira solo los efectos totales y puede sacrificar a una persona.'),
        ('abc', '{F} ¿Qué límite tiene el enfoque de virtudes?', 'Puede ser vago si no se concreta en acciones', 'Es demasiado rígido porque solo mira las normas', 'Ignora el carácter de la persona que decide', 'Hay que aterrizar el carácter en decisiones concretas.'),
        ('abc', '{F} ¿Qué combinación de enfoques es más completa?', 'Partir del principio, ver las consecuencias y actuar como una persona honesta y prudente', 'Elegir el enfoque que dé la respuesta más cómoda para todos', 'Usar solo las reglas porque son claras y fáciles de aplicar', 'Usa las tres herramientas y compensa sus límites.'),
        ('abc', '{F} Un compañero dice: «Informar es traicionar». ¿Qué corresponde?', 'Preguntar qué principio y qué consecuencias están en juego', 'Aceptarlo, porque la lealtad es lo primero', 'Rechazarlo, porque informar es siempre lo correcto', 'Se razona con principios y efectos, sin dar nada por obvio.'),
        ('abc', '{F} ¿Qué acción es proporcionada si es la primera vez que ocurre?', 'Conversar primero y, si no basta, hablar con el docente', 'Humillar públicamente para dar el ejemplo', 'Ignorarlo para evitar problemas', 'Equilibra respeto por la persona y justicia con el curso.'),
        ('abc', '{F} Si el compañero está siendo presionado y corre riesgo, ¿qué haces?', 'Avisar a una persona adulta de confianza', 'Callar para no empeorar la situación', 'Enfrentar solo al grupo que lo presiona', 'Una persona adulta puede proteger a quien corre riesgo.'),
        ('abc', 'Un estudiante encuentra una billetera con $10.000 y un carnet. ¿Qué enfoque de virtudes lo guía?', 'Honestidad: devolverla a su dueño', 'Prudencia: guardarla sin buscar al dueño', 'Solidaridad: usar el dinero para ayudar a otro', 'Una persona honesta la devolvería a quien corresponde.'),
        ('abc', '{F} Alguien dice: «El enfoque de consecuencias es de un partido». ¿Qué corresponde?', 'Aclarar que son herramientas para razonar, no posturas partidistas', 'Aceptarlo, porque cada enfoque pertenece a un grupo político', 'Rechazarlo, porque ningún enfoque sirve', 'Los enfoques sirven para analizar dilemas, no para identificar partidos.'),
    ],
    ctx=('abc', 'Un curso debe decidir si mantiene en secreto quién mintió en un trabajo grupal. ¿Qué pregunta ayuda?', '¿Qué principio se cumple y qué efectos tiene para todas las personas?', '¿Qué opción es más cómoda para el curso en este momento?', '¿Qué opción prefiere el grupo más fuerte del curso?', 'Combina el análisis de principios y de consecuencias.'),
    sc=[
        ('¿Qué es el enfoque de deberes?', 'Una forma de razonar que mira las reglas y principios que deben cumplirse', 'Se pregunta qué norma obliga en cada caso.'),
        ('abc', '¿Qué es el enfoque de consecuencias?', 'Una forma de razonar que mira los efectos de cada opción', 'Una forma de razonar que mira solo las reglas', 'Una forma de razonar que mira solo el carácter', 'Evalúa qué opción produce más bien y menos daño.'),
        ('En Educación Ciudadana: ¿Qué es la coherencia?', 'El acuerdo entre lo que se piensa, se dice y se hace', 'Una decisión coherente se puede explicar con razones.'),
    ],
    op=("Con la {F} escribe una decisión de seis líneas: el dilema, qué diría cada enfoque, la opción que elegirías, tu razón, cómo cuidarías la dignidad del compañero y si avisarías a una persona adulta de confianza.",
        "Dilema: informar o callar. Deberes: informar la honestidad. Consecuencias: callar perjudica a otros. Virtudes: conversar primero. Elijo conversar y, si no basta, hablar con el docente. Cuidaría su dignidad sin humillarlo. Avisaría a un adulto si hay presión o riesgo.",
        ["usa los tres enfoques", "cuida la dignidad", "justifica la elección"], ["decisión de seis líneas"], ["usar un solo enfoque", "humillar al compañero"],
        "Pregunta qué parte de su decisión le costaría más cumplir."),
    reinforce="Explica un límite de cada enfoque con tus palabras.",
    extend="Aplica los tres enfoques a un dilema pequeño de tu vida diaria.",
)

# ============================================================ OA 08, clase 4
F = ("Ficha 76 (tema de deliberación de ejemplo): el centro de estudiantes ficticio del liceo Los Cóndores discute qué hacer con una donación de 200.000 pesos. "
     "Opción A: pagar un paseo para el curso que recaude menos. Opción B: financiar útiles para estudiantes que lo necesiten. Opción C: repartir el dinero entre todos los cursos por igual. "
     "Principios en juego: justicia, solidaridad, transparencia, respeto de la dignidad. Datos de ejemplo: 8 cursos; 15 estudiantes necesitan útiles con un costo de 8.000 pesos cada uno.")
build(
    O8, 4, F,
    use="Aprenderé a deliberar y decidir en la práctica ciudadana con principios éticos, resguardando la dignidad de las personas y rindiendo cuentas.",
    prior=["Sé los enfoques éticos.", "Sé qué es la transparencia.", "Sé estructurar un argumento."],
    explain=[
        "Una decisión ciudadana ética se justifica con razones públicas, es decir, razones que cualquier persona puede entender y discutir, no solo intereses privados. Se pregunta: ¿es justa?, ¿respeta la dignidad?, ¿es transparente?, ¿rinde cuentas?, ¿qué consecuencias tiene para quienes menos tienen? La decisión se comunica con claridad.",
        "La solidaridad pide mirar a quienes necesitan más, pero la justicia pide criterios claros y no humillar. Por ejemplo, ayudar con útiles sin exponer públicamente quién los recibe protege la dignidad. La transparencia implica informar cuánto se gastó y en qué. Se pueden combinar opciones: parte del dinero para necesidades y parte para actividades comunes.",
        "Al terminar la deliberación se registra la decisión y las posturas de minoría, se establece quién ejecuta y cuándo se rendirá cuenta. Esto fortalece la confianza y la vida en democracia. Si se detecta que alguien actuó sin honestidad, se informa por los canales formales y se respeta la presunción de inocencia.",
    ],
    vocab=[("razón pública", "argumento que cualquier persona puede entender y discutir"), ("criterio claro", "regla conocida que se aplica a todos por igual"), ("rendición de cuentas", "informe de cómo se usó un recurso"), ("dignidad", "valor que tiene toda persona y que debe respetarse"), ("opción combinada", "decisión que une partes de varias propuestas")],
    worked=[
        ("Calcular una necesidad", "Si 10 estudiantes necesitan útiles que cuestan 5.000 pesos cada uno, ¿cuánto se necesita?", ["Se multiplican 10 por 5.000.", "Resultado: 50.000."], "50.000 pesos"),
        ("Proteger la dignidad", "¿Qué es mejor: entregar los útiles en privado o llamar a los beneficiarios al frente?", ["La entrega privada protege.", "Llamarlos al frente expone."], "Entregarlos en privado"),
    ],
    mistakes=[("Entregar ayuda de forma que humilla.", "Daña la dignidad.", "Hazlo con discreción."),
              ("No informar cómo se usó el dinero.", "Se pierde la confianza.", "Rinde cuentas.")],
    T=[
        ('abc', '¿Qué es una razón pública?', 'Un argumento que cualquier persona puede entender y discutir', 'Una razón anunciada públicamente pero que responde a un interés privado', 'La opinión del presidente del centro', 'Debe poder compartirse y debatirse, no ocultar intereses privados.'),
        ('=', '{F} ¿Cuánto cuestan los útiles de los 15 estudiantes?', '15*8000', 'Se multiplica el número de estudiantes por el costo de cada útil.', ' pesos'),
        ('=', '{F} ¿Cuánto recibiría cada curso si se reparte por igual (opción C)?', '200000//8', 'Se divide el dinero entre los cursos.', ' pesos'),
        ('=', '{F} ¿Cuánto dinero sobraría si se financian los útiles?', '200000-15*8000', 'Se resta el costo de los útiles al total.', ' pesos'),
        ('abc', '{F} ¿Qué principio favorece la opción B?', 'Solidaridad: apoya a quienes más lo necesitan', 'Igualdad estricta: todos reciben lo mismo', 'Azar: se sortea quién recibe', 'La solidaridad pide mirar a quienes necesitan más.'),
        ('abc', '{F} ¿Qué riesgo tiene la opción C?', 'No atiende a quienes más necesitan', 'Reparte de forma muy desigual', 'Excluye a algunos cursos', 'Reparte igual sin considerar necesidades distintas.'),
        ('abc', '{F} ¿Qué riesgo tiene la opción A?', 'Puede estigmatizar al curso que recaudó menos', 'Ayuda a todos los cursos por igual', 'No usa nada del dinero donado', 'Marcaría al curso que recaudó menos.'),
        ('abc', '{F} ¿Qué opción combinada es más sólida?', 'Útiles para quienes los necesitan y el resto para una actividad común', 'Gastar todo en un paseo del curso con más cuotas pagadas', 'Guardar el dinero sin informar a nadie por un tiempo', 'Une el apoyo a quienes necesitan con un beneficio compartido por todos.'),
        ('abc', '{F} ¿Cómo se protege la dignidad al entregar los útiles?', 'Entregándolos con discreción, sin anunciar quiénes los reciben', 'Anunciando los nombres para dar transparencia al proceso', 'Pidiendo que agradezcan en público ante todo el liceo', 'La transparencia no exige exponer a las personas.'),
        ('abc', '{F} Alguien dice: «Hagamos lo que decida el presidente». ¿Qué corresponde?', 'Deliberar con razones y dejar registro de la decisión', 'Aceptar, porque el presidente conoce mejor el tema', 'Votar sin discutir para ahorrar tiempo', 'La decisión debe justificarse con razones públicas.'),
        ('abc', '{F} ¿Qué es la rendición de cuentas?', 'Informar cómo se usó el recurso', 'Anunciar lo que se piensa gastar', 'Guardar los comprobantes sin mostrarlos', 'Mostrar en qué se gastó genera transparencia y confianza en la comunidad.'),
        ('abc', '{F} Si la minoría no está de acuerdo, ¿qué corresponde?', 'Registrar su postura y respetar la decisión', 'Ignorar su postura porque perdió la votación', 'Repetir la discusión hasta que la minoría cambie', 'Se respeta a la minoría y la decisión adoptada.'),
        ('=', '{F} Si se destinan 120.000 pesos a útiles y el resto se reparte por igual entre los 8 cursos, ¿cuánto recibe cada curso?', '(200000-120000)//8', 'Se calcula lo que sobra y se reparte entre los cursos.', ' pesos'),
    ],
    ctx=('abc', 'Un curso debe elegir entre un paseo caro y uno que todos puedan pagar. ¿Qué principio guía una buena decisión?', 'Justicia y respeto a todos, buscando una opción que todos puedan pagar', 'Lo que quiere el grupo más fuerte del curso', 'Lo más rápido de organizar para el curso', 'Incluye a todos y evita excluir por razones económicas.'),
    sc=[
        ('¿Qué es un criterio claro?', 'Una regla conocida y aplicable por igual para decidir', 'Evita que la decisión parezca arbitraria.'),
        ('abc', '¿Qué es una opción combinada?', 'Una que une partes de distintas opciones para equilibrar valores', 'La que gana en una votación por mayoría simple', 'La que elige la dirección sin consultar al curso', 'Equilibra, por ejemplo, solidaridad con actividades comunes.'),
        ('En Educación Ciudadana: ¿Qué es la dignidad?', 'El valor que tiene toda persona y que debe respetarse', 'Es la base de los derechos.'),
    ],
    op=("Con la {F} escribe tu decisión de siete líneas: la opción o combinación elegida, el principio principal, los cálculos (que el total no supere 200.000), cómo protegerás la dignidad, cómo rendirás cuentas, la postura de minoría y qué harías si descubres un uso indebido (a quién avisarías).",
        "Elijo útiles (120.000) y una actividad común (80.000). Principio: solidaridad y justicia. Cálculo: 120.000 más 80.000 son 200.000. Dignidad: entrega discreta. Rendición de cuentas: informe en el consejo de curso. Minoría: se registra su postura. Uso indebido: informar a la dirección por canal formal.",
        ["cálculos correctos", "protege la dignidad", "incluye rendición de cuentas"], ["decisión de siete líneas"], ["superar el total", "exponer a beneficiarios"],
        "Pregunta cómo explicaría su decisión a quien no la comparte."),
    reinforce="Explica por qué la rendición de cuentas fortalece la democracia.",
    extend="Anota una decisión de tu curso y qué principio ético la orienta.",
)

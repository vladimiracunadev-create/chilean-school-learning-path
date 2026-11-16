"""Educación Ciudadana 4.º medio FG: OA 01 (institucionalidad democrática, representación y distribución del poder) y OA 02 (corresponsabilidad ética ante desafíos multiescalares). Casos y cifras de ejemplo inventados."""
from __future__ import annotations

from fg_eciu_common import build

O1 = "FG-ECIU-4M-OAC-01"
O2 = "FG-ECIU-4M-OAC-02"

# ============================================================ OA 01, clase 1
F = ("Ficha 38 (país ficticio de ejemplo, Tierra Alta): una asamblea elegida dicta las leyes; un gobierno ejecuta y administra; los tribunales resuelven conflictos; "
     "un organismo autónomo revisa si el gasto público cumple la ley; las regiones eligen a sus autoridades y manejan parte del presupuesto; "
     "una ley puede ser revisada por un tribunal constitucional que verifica si respeta la Constitución.")
build(
    O1, 1, F,
    use="Aprenderé a describir cómo funciona la institucionalidad democrática, qué son la representación y la distribución del poder, y con qué criterios se evalúan (bien común, cohesión y justicia social).",
    prior=["Sé qué es la democracia y sus atributos.", "Sé qué es la separación de poderes.", "Sé qué es un derecho y un deber."],
    explain=[
        "La institucionalidad democrática es el conjunto de órganos, reglas y procedimientos que organizan el poder. Típicamente hay un poder legislativo que hace las leyes, un poder ejecutivo que gobierna y administra, y un poder judicial que resuelve conflictos. Además existen órganos autónomos de control y, en muchos países, un tribunal que verifica que las leyes respeten la Constitución.",
        "La representación es el mecanismo por el cual la ciudadanía elige a personas que deciden en su nombre. Se mejora con elecciones libres, información, rendición de cuentas y participación entre elecciones. La distribución del poder reparte las decisiones entre niveles (nacional, regional, local) y entre órganos, con frenos y contrapesos para que nadie concentre un poder excesivo.",
        "Para evaluar una institución se usan criterios: ¿contribuye al bien común?, ¿fortalece la cohesión social, es decir, los vínculos y la confianza entre las personas?, ¿promueve la justicia social, es decir, un reparto equitativo de recursos y oportunidades? Las respuestas se apoyan en evidencia y admiten matices.",
    ],
    vocab=[("institucionalidad", "conjunto de órganos, reglas y procedimientos que organizan el poder"), ("representación", "mecanismo por el que la ciudadanía elige a quienes deciden en su nombre"), ("frenos y contrapesos", "controles mutuos entre órganos para evitar la concentración del poder"), ("cohesión social", "vínculos y confianza que mantienen unida a una sociedad"), ("descentralización", "traspaso de decisiones y recursos a niveles regionales o locales")],
    worked=[
        ("Reconocer un contrapeso", "En un país de ejemplo, un tribunal puede dejar sin efecto un decreto del gobierno que viola la ley. ¿Qué es eso?", ["Un órgano controla a otro.", "Es un contrapeso."], "Un freno o contrapeso"),
        ("Descentralización", "Una región de ejemplo decide en qué se gasta parte de su presupuesto. ¿Qué principio muestra?", ["Una decisión se toma en un nivel regional.", "Es descentralización."], "Descentralización"),
    ],
    mistakes=[("Pensar que la representación termina al votar.", "Se necesita rendición de cuentas y participación entre elecciones.", "Revisa información, control y participación."),
              ("Creer que concentrar el poder siempre hace más eficiente al Estado.", "Se pierden controles y se arriesgan los derechos.", "Evalúa el bien común, la cohesión y la justicia social.")],
    T=[
        ('abc', '¿Qué es la institucionalidad democrática?', 'El conjunto de órganos, reglas y procedimientos que organizan el poder', 'Un conjunto de leyes sin órganos que las apliquen', 'Una lista de las personas que ocupan cargos públicos', 'La institucionalidad incluye órganos, reglas y procedimientos, no solo leyes ni personas.'),
        ('abc', '¿Qué función cumple cada poder del Estado?', 'El legislativo hace las leyes, el ejecutivo gobierna y administra, y el judicial resuelve conflictos', 'El legislativo resuelve conflictos, el ejecutivo hace las leyes y el judicial gobierna', 'El legislativo gobierna, el ejecutivo resuelve conflictos y el judicial dicta las leyes', 'Cada poder tiene una función distinta que ayuda a repartir y controlar el poder.'),
        ('abc', '{F} ¿Qué órgano de Tierra Alta cumple una función de control del gasto?', 'El organismo autónomo que revisa si el gasto cumple la ley', 'La asamblea elegida que dicta las leyes y las discute en la capital', 'El gobierno que administra los recursos y ejecuta el gasto público', 'Un control eficaz lo hace un órgano distinto del que gasta.'),
        ('abc', '{F} ¿Qué es un freno o contrapeso en Tierra Alta?', 'El tribunal constitucional que revisa si una ley respeta la Constitución', 'Una ley que ningún órgano puede revisar una vez que se aprueba', 'Un gobierno que además dicta las leyes y las hace cumplir', 'Un contrapeso es un control de un órgano sobre otro.'),
        ('abc', '{F} ¿Qué significa la descentralización en Tierra Alta?', 'Las regiones eligen sus autoridades y manejan parte del presupuesto', 'El gobierno decide todo desde la capital y las regiones solo ejecutan', 'Cada región dicta sus propias leyes sin límites ni controles', 'Reparte decisiones y recursos entre niveles.'),
        ('abc', '¿Qué es la representación en una democracia?', 'El mecanismo por el cual la ciudadanía elige a quienes deciden en su nombre', 'La obligación de votar en toda decisión pública', 'La participación directa de toda la población en cada ley', 'Se delegan decisiones en personas elegidas que rinden cuentas.'),
        ('abc', '¿Qué es la cohesión social?', 'Los vínculos y la confianza que mantienen unida a una sociedad', 'La igualdad de ingresos entre todas las personas', 'El acuerdo total entre todos los partidos', 'Se refiere a la unión y confianza entre las personas.'),
        ('abc', '{F} ¿Qué criterio evalúa si una institución repara desigualdades?', 'Justicia social: el reparto equitativo de recursos y oportunidades', 'Cohesión social: los vínculos y la confianza entre las personas', 'Representación: la elección de las autoridades que deciden', 'La justicia social se centra en el reparto equitativo.'),
        ('abc', '{F} Alguien dice: «Si una institución concentra todas las decisiones es mejor». ¿Qué respuesta es más completa?', 'Se pierden los controles y se arriesgan los derechos', 'Es correcto, porque se decide más rápido', 'Solo ocurre en países pequeños', 'Los frenos y contrapesos evitan que nadie concentre un poder excesivo.'),
        ('abc', '{F} ¿Qué mejora la representación entre una elección y otra?', 'La rendición de cuentas, la información y la participación', 'Reducir la información que recibe la ciudadanía', 'Esperar a la siguiente elección', 'La ciudadanía puede vigilar y exigir cuentas entre elecciones.'),
        ('abc', '{F} ¿Qué pregunta evalúa el bien común de una institución?', '¿Contribuye a que todas las personas vivan con dignidad?', '¿Cuántos funcionarios trabajan en ella y cuánto ganan al mes?', '¿Hace que se decida más rápido que otras instituciones?', 'El bien común se relaciona con las condiciones de vida digna de todos.'),
        ('abc', 'Una comuna de ejemplo permite que los vecinos fiscalicen el gasto en una plaza. ¿Qué fortalece?', 'El control ciudadano y la rendición de cuentas', 'La concentración del poder', 'La centralización de las decisiones', 'La ciudadanía vigila el uso de los recursos públicos.'),
        ('=', 'Si las regiones manejan el 25 % de un presupuesto de 8.000 millones, ¿cuántos millones manejan?', '8000*25//100', 'Se calcula el 25 % del presupuesto total.', ' millones'),
    ],
    ctx=('abc', 'Un liceo de ejemplo permite que un solo directivo decida todo, sin consejo ni revisión. ¿Qué elemento falta?', 'Frenos y contrapesos', 'Cohesión social', 'Descentralización', 'Sin controles mutuos, el poder queda concentrado.'),
    sc=[
        ('¿Qué son los frenos y contrapesos?', 'Controles mutuos entre órganos', 'Evitan la concentración del poder y los abusos.'),
        ('abc', '¿Qué significa la distribución del poder?', 'Repartir las decisiones entre niveles y órganos para evitar su concentración', 'Entregar todo el poder a la mayoría que ganó la última elección', 'Reunir todas las decisiones en el nivel nacional y en un solo órgano', 'Se reparte entre órganos y niveles, con controles.'),
        ('En Educación Ciudadana: ¿qué es rendir cuentas?', 'Explicar y justificar las decisiones y los gastos ante la ciudadanía', 'Permite que la ciudadanía controle a las autoridades.'),
    ],
    op=("Con la {F} haz una tabla de cuatro filas: órgano, función y qué control tiene o podría tener. Luego evalúa en tres líneas si la institucionalidad de Tierra Alta favorece el bien común, la cohesión y la justicia social, indicando qué evidencia falta.",
        "Asamblea: dicta leyes; revisada por el tribunal. Gobierno: administra; controlado por el organismo autónomo. Tribunales: resuelven conflictos; independientes. Regiones: manejan presupuesto; control ciudadano. Evaluación: hay frenos y contrapesos y descentralización; falta evidencia de cómo se reparten los recursos entre regiones.",
        ["asocia función y control", "evalúa con criterios", "señala evidencia faltante"], ["tabla de cuatro filas", "evaluación de tres líneas"], ["afirmar sin evidencia", "confundir poderes"],
        "Pregunta qué indicador mostraría la cohesión social."),
    reinforce="Explica con tus palabras cómo se relacionan separación de poderes y contrapesos.",
    extend="Anota una decisión que tome tu municipio y qué órgano la controla.",
)

# ============================================================ OA 01, clase 2
F = ("Ficha 39 (caso de ejemplo, Tierra Alta): una ley sobre agua se tramita así: (1) el gobierno presenta un proyecto; (2) una cámara lo aprueba por 90 votos a favor y 60 en contra; "
     "(3) la otra cámara lo aprueba con 30 votos a favor y 10 en contra; (4) el presidente lo promulga; (5) un grupo de ciudadanos reclama ante el tribunal constitucional que la ley no consultó a las comunidades. "
     "Fuentes: el texto del proyecto, el acta de votación y el reclamo de los ciudadanos.")
build(
    O1, 2, F,
    use="Aprenderé a investigar cómo se toma una decisión en la institucionalidad democrática, qué controles intervienen y cómo se mide el apoyo de una decisión.",
    prior=["Sé qué es el poder legislativo.", "Sé qué son los contrapesos.", "Sé sumar y calcular porcentajes."],
    explain=[
        'Una ley sigue un proceso: alguien propone un proyecto (iniciativa), se discute en las cámaras, se vota, el presidente la promulga (la declara ley) y se publica. En cada paso hay controles: debate, votación por mayoría, posibilidad de que un tribunal revise si respeta la Constitución. Por eso una ley debe cumplir tanto el procedimiento como los derechos. El quórum es el número mínimo de personas presentes o de votos necesarios para que una votación sea válida.',
        'Para leer una votación se suman los votos a favor y en contra y se calcula qué parte representa cada uno. La mayoría simple exige más votos a favor que en contra. Un alto apoyo no impide que la ley sea revisada, porque una mayoría no puede violar derechos fundamentales. Que haya reclamos es parte del control ciudadano.',
        'Al investigar se separan hechos de valoraciones: «la ley se aprobó por 90 a 60» es un hecho; «la ley es injusta» es una valoración que necesita argumentos. Se revisa qué alegan los ciudadanos (falta de consulta) y qué dice el procedimiento. Una conclusión prudente dice lo que se sabe y lo que falta por resolver.',
    ],
    vocab=[("iniciativa", "propuesta con la que comienza una ley"), ("promulgar", "declarar oficialmente que un proyecto aprobado es ley"), ("mayoría simple", "más votos a favor que en contra"), ("control de constitucionalidad", "revisión de si una ley respeta la Constitución"), ("quórum", "número mínimo de votos o de presentes exigido para decidir")],
    worked=[
        ("Leer una votación", "En una votación de ejemplo hay 60 votos a favor y 40 en contra. ¿Hay mayoría simple a favor?", ["60 es mayor que 40.", "Hay mayoría simple."], "Sí"),
        ("Porcentaje", "De 80 votos totales, 60 son a favor. ¿Qué porcentaje es?", ["60 entre 80 son tres cuartas partes.", "Es el 75 %."], "75 %"),
    ],
    mistakes=[("Creer que una ley aprobada por mayoría no puede ser cuestionada.", "Debe respetar la Constitución y los derechos.", "Revisa el control de constitucionalidad."),
              ("Contar solo los votos a favor para saber el apoyo.", "El apoyo depende de la proporción respecto del total.", "Suma a favor y en contra.")],
    T=[
        ('abc', '¿Cuál es el orden básico de la tramitación de una ley?', 'Iniciativa, discusión y votación en las cámaras, promulgación y publicación', 'Promulgación, votación en las cámaras, iniciativa y publicación', 'Votación, iniciativa, publicación y promulgación', 'Primero se propone el proyecto, luego se discute y vota, y al final se promulga y publica.'),
        ('=', '{F} En la primera cámara, ¿qué porcentaje de los votos fue a favor?', '90*100//150', 'Se compara la parte a favor con el total de votos (90 + 60).', ' %'),
        ('=', '{F} En la segunda cámara, ¿qué porcentaje de los votos fue a favor?', '30*100//40', 'Se compara la parte a favor con el total de votos (30 + 10).', ' %'),
        ('abc', '¿Qué significa promulgar?', 'Declarar oficialmente que un proyecto aprobado es ley', 'Votar el proyecto en la cámara', 'Revisar si el proyecto respeta la Constitución', 'Promulgar es el paso en que el presidente declara la ley.'),
        ('abc', '¿Qué es la mayoría simple?', 'Más votos a favor que en contra', 'Todos los votos a favor', 'Más de dos tercios de los votos', 'La mayoría simple compara los votos a favor con los votos en contra.'),
        ('abc', 'En un consejo de curso un acuerdo se aprueba por 18 votos a favor y 12 en contra. ¿Tiene mayoría simple?', 'Sí, porque 18 es mayor que 12', 'No, porque no llega a la unanimidad', 'No, porque faltan los votos nulos', 'La mayoría simple exige más votos a favor que en contra, no unanimidad.'),
        ('abc', '{F} ¿Cuál de estas afirmaciones es un hecho?', '«La primera cámara aprobó el proyecto con 90 votos a favor»', '«La ley es injusta con las comunidades y debería anularse»', '«El gobierno no quiso consultar a las comunidades por mala fe»', 'Un hecho se puede comprobar con el acta; las otras son valoraciones o acusaciones.'),
        ('abc', '{F} ¿Qué alegan los ciudadanos ante el tribunal constitucional?', 'Que la ley no consultó a las comunidades', 'Que la ley tuvo pocos votos a favor', 'Que el presidente no la promulgó', 'Es el reclamo que registra la ficha.'),
        ('abc', '{F} ¿Por qué el apoyo mayoritario no impide el reclamo?', 'Porque una ley debe respetar la Constitución y los derechos, aunque tenga mayoría', 'Porque no se puede reclamar después de promulgar una ley', 'Porque un tribunal puede reemplazar al Congreso para votar las leyes', 'Una mayoría no puede violar derechos fundamentales.'),
        ('abc', '{F} Un asistente dice: «La ley es válida, por eso es justa». ¿Qué corresponde?', 'Distinguir entre cumplir el procedimiento y ser justa, que requiere argumentos', 'Aceptarlo, porque lo aprobó una mayoría en las dos cámaras', 'Rechazarlo, porque toda ley aprobada por mayoría es injusta', 'Una ley válida puede igualmente ser discutida.'),
        ('abc', '{F} ¿Qué dato falta para evaluar el reclamo?', 'Si la Constitución o la ley exigían consultar a las comunidades', 'Cuántas personas leyeron el texto del proyecto de ley', 'En qué fecha exacta se publicó el proyecto en el diario oficial', 'Define si hubo o no una falta al procedimiento.'),
        ('abc', '{F} ¿Qué conclusión es prudente?', 'Hubo apoyo mayoritario, pero falta resolver si se cumplió con la consulta', 'La ley es ilegal por el solo hecho de que hubo un reclamo', 'La ley es justa porque obtuvo mayoría en ambas cámaras', 'Se limita a lo que se sabe y a lo que falta resolver.'),
        ('abc', '¿Qué es el control de constitucionalidad?', 'La revisión de si una ley respeta la Constitución', 'La votación en la segunda cámara', 'La promulgación por parte del presidente', 'Es el control de un tribunal sobre las leyes.'),
    ],
    ctx=('abc', 'Un acuerdo en un consejo de curso se aprueba por 14 votos a favor y 14 en contra. ¿Tiene mayoría simple?', 'No, porque no hay más votos a favor que en contra', 'Sí, porque 14 es la mitad de los 28 votos emitidos', 'Sí, porque nadie votó nulo ni se abstuvo de votar', 'Con empate no hay más votos a favor que en contra.'),
    sc=[
        ('¿Qué es una iniciativa de ley?', 'El proyecto que alguien propone para que se discuta y se vote', 'Es el primer paso de la tramitación de una ley.'),
        ('abc', '¿Qué es el quórum?', 'El número mínimo de personas o votos necesarios para que una votación sea válida', 'El total de votos a favor que obtiene un proyecto en la cámara', 'La diferencia entre votos a favor y votos en contra', 'Sin quórum, una votación no es válida.'),
        ('¿Para qué sirve el reclamo de la ciudadanía ante un tribunal?', 'Para ejercer control sobre el procedimiento y los derechos', 'Es parte del control ciudadano sobre las leyes.'),
    ],
    op=("Con la {F} escribe una línea de tiempo de cinco pasos con el control o actor de cada uno, calcula el apoyo total (a favor y en contra sumados de ambas cámaras) y redacta una conclusión prudente de tres líneas sobre el reclamo.",
        "1 Proyecto: gobierno. 2 Primera cámara: 90-60. 3 Segunda cámara: 30-10. 4 Promulgación: presidente. 5 Reclamo: tribunal. Apoyo total: 120 a favor y 70 en contra. Conclusión: la ley tuvo mayoría, pero el tribunal debe resolver si faltó la consulta a las comunidades.",
        ["ordena el proceso", "calcula votos", "conclusión prudente"], ["línea de tiempo", "conclusión"], ["afirmar que la ley es ilegal", "ignorar el reclamo"],
        "Pregunta qué cambiaría si el tribunal acoge el reclamo."),
    reinforce="Explica por qué una ley aprobada por mayoría puede ser revisada.",
    extend="Averigua cómo se aprobó una norma reciente de tu comuna.",
)

# ============================================================ OA 01, clase 3
F = ("Ficha 40 (sistemas de ejemplo, país ficticio Valle Sur). En una elección se reparten 10 escaños entre 3 listas. Votos: Lista A 600, Lista B 300, Lista C 100 (total 1.000). "
     "Sistema 1 (mayoritario): la lista con más votos obtiene los 10 escaños. "
     "Sistema 2 (proporcional): los escaños se reparten en proporción a los votos. "
     "Perspectiva 1: «El mayoritario da gobiernos estables». Perspectiva 2: «El proporcional representa mejor a todas las opiniones».")
build(
    O1, 3, F,
    use="Aprenderé a contrastar sistemas de representación y a ver cómo cambian la distribución del poder, con ventajas y límites en cada uno.",
    prior=["Sé qué es la representación.", "Sé calcular porcentajes y proporciones simples.", "Sé comparar perspectivas."],
    explain=[
        'Un sistema electoral es el conjunto de reglas que convierte los votos en cargos. En un sistema mayoritario gana quien obtiene más votos y los demás no obtienen representación en ese cargo. En un sistema proporcional los cargos se reparten en proporción a los votos de cada lista. Ambos son democráticos, pero distribuyen el poder de modo distinto. Un umbral mínimo de votos exige a cada lista un porcentaje para obtener escaños, lo que limita la dispersión en muchos grupos pequeños.',
        'El sistema mayoritario tiende a producir mayorías claras y gobiernos estables, pero deja sin representación a quienes votaron por opciones menores. El proporcional representa más opiniones, pero puede dificultar acuerdos si hay muchos grupos. Cada país los combina o ajusta según sus objetivos, como estabilidad, pluralismo o cercanía de los representantes.',
        'Contrastar significa calcular qué resultado produce cada sistema con los mismos votos y valorarlo con criterios: representatividad, estabilidad, cohesión y justicia social. Los números muestran una consecuencia, pero decidir cuál sistema es mejor implica valores, y por eso se argumenta sin dar por obvio uno solo.',
    ],
    vocab=[("sistema electoral", "reglas que convierten los votos en cargos"), ("sistema mayoritario", "sistema en que gana quien obtiene más votos"), ("sistema proporcional", "sistema que reparte cargos en proporción a los votos"), ("estabilidad", "capacidad de un gobierno de mantenerse y decidir con apoyo"), ("pluralismo", "existencia y representación de varias opiniones")],
    worked=[
        ("Repartir proporcionalmente", "Con 10 escaños y votos de 700 para X y 300 para Y (total 1.000), ¿cuántos escaños recibe cada una en un sistema proporcional?", ["X tiene el 70 %: 7 escaños.", "Y tiene el 30 %: 3 escaños."], "X, 7; Y, 3"),
        ("Aplicar el sistema mayoritario", "Con los mismos votos, ¿cuántos escaños recibe X si el sistema es mayoritario?", ["Gana quien tiene más votos.", "Se lleva los 10."], "X, 10"),
    ],
    mistakes=[("Pensar que el sistema proporcional siempre es mejor.", "También tiene riesgos, como dificultar acuerdos.", "Evalúa varios criterios."),
              ("Creer que el sistema mayoritario no es democrático.", "También lo es, pero distribuye el poder de otra forma.", "Compara efectos con criterios.")],
    T=[
        ('abc', '¿Qué es un sistema electoral?', 'Un conjunto de reglas que convierte los votos en cargos', 'Una lista de personas habilitadas para votar', 'El número de candidatos que presenta cada lista', 'Determina cómo se asignan los cargos a partir de los votos.'),
        ('=', '{F} En el sistema proporcional, ¿cuántos escaños obtiene la Lista A?', '10*600//1000', 'Se aplica a los escaños la misma proporción de votos de la Lista A.', ' escaños'),
        ('=', '{F} En el sistema proporcional, ¿cuántos escaños obtiene la Lista B?', '10*300//1000', 'Se aplica a los escaños la proporción de votos de la Lista B.', ' escaños'),
        ('abc', '{F} ¿Qué sistema deja sin escaños a las Listas B y C?', 'El mayoritario: la lista con más votos obtiene todos los escaños', 'El proporcional: reparte los escaños según los votos de cada lista', 'Ninguno: ambos sistemas reparten los escaños de igual manera', 'En el mayoritario gana todo quien tiene más votos.'),
        ('abc', '{F} ¿Qué ventaja destaca la perspectiva 1?', 'Estabilidad de gobierno por mayorías claras', 'Pluralismo y representación de minorías', 'Mayor participación electoral', 'La perspectiva 1 destaca los gobiernos estables que producen las mayorías claras.'),
        ('abc', '{F} ¿Qué riesgo puede tener el sistema proporcional?', 'Dificultad para llegar a acuerdos si hay muchos grupos', 'Que gane siempre la lista más grande con todos los escaños', 'Que ninguna opinión quede representada', 'Más grupos con escaños exigen más negociación.'),
        ('abc', '{F} ¿Qué parte de los votos obtuvieron las Listas B y C juntas?', '40 % (400 de 1.000)', '30 % (300 de 1.000)', '10 % (100 de 1.000)', 'Las listas B y C suman 300 + 100 = 400 votos, es decir 40 % del total.'),
        ('abc', '{F} Un asistente dice: «Los números prueban cuál sistema es mejor». ¿Qué corresponde?', 'Aclarar que los números muestran consecuencias, pero decidir implica valores', 'Aceptarlo, porque los números son objetivos y no hay nada más que discutir', 'Rechazarlo, porque los números no sirven para comparar sistemas', 'Los datos describen efectos; elegir entre estabilidad y pluralismo es una decisión de valores.'),
        ('abc', '{F} ¿Qué propuesta combinada puede equilibrar estabilidad y representación?', 'Un sistema proporcional con un umbral mínimo de votos para obtener escaños', 'Un sistema mayoritario para todos los cargos, sin ningún ajuste', 'Un sistema proporcional sin límite al número de listas', 'El umbral reduce la dispersión sin eliminar la representación.'),
        ('abc', '{F} Con la regla proporcional, ¿qué criterio mejora más?', 'Representatividad: más opiniones obtienen escaños', 'Estabilidad: siempre se forma una mayoría clara', 'Rapidez del conteo de votos', 'Reparte escaños en proporción a los votos de cada lista.'),
        ('abc', 'En un centro de estudiantes de ejemplo, cada curso elige a un representante por mayoría. ¿Qué tipo de sistema es?', 'Mayoritario, porque cada curso elige al que tiene más votos', 'Proporcional, porque participan todos los cursos', 'Ninguno, porque no hay escaños', 'El cargo lo gana quien obtiene más votos.'),
        ('abc', '{F} En el sistema mayoritario, ¿qué obtiene la Lista A?', 'El 100 % de los escaños con el 60 % de los votos', 'El 60 % de los escaños con el 60 % de los votos', 'El 40 % de los escaños con el 60 % de los votos', 'En el mayoritario gana todos los escaños quien tiene más votos.'),
        ('abc', 'Un país prioriza que ningún grupo quede sin voz. ¿Qué sistema se acerca más a ese valor?', 'El proporcional, porque valora el pluralismo', 'El mayoritario, porque valora la estabilidad', 'Ninguno, porque ambos dejan a algunos sin voz', 'La elección entre sistemas implica valores, y el pluralismo se asocia al proporcional.'),
    ],
    ctx=('=', 'En un curso de ejemplo, la lista X obtiene 15 votos, la Y 10 y la Z 5, y se reparten 6 cargos de forma proporcional. ¿Cuántos cargos obtiene la lista Y?', '6*10//30', 'Se aplica a los cargos la proporción de votos de la lista Y.', ' cargos'),
    sc=[
        ('abc', '¿Qué es el sistema mayoritario?', 'Gana quien obtiene más votos y los demás no obtienen representación en ese cargo', 'Los cargos se reparten según los votos que obtiene cada lista', 'Todos los candidatos obtienen un cargo sin importar los votos', 'Se caracteriza por el efecto de «el ganador se lleva todo».'),
        ('¿Qué es el pluralismo?', 'La existencia y representación de varias opiniones', 'Reconoce la diversidad de opiniones políticas.'),
        ('¿Qué es la estabilidad en un sistema electoral?', 'La capacidad de formar gobiernos con apoyo claro y que puedan gobernar', 'Se asocia a las mayorías claras.'),
    ],
    op=("Con la {F} arma una tabla con los dos sistemas: escaños de cada lista, ventaja, riesgo y un criterio (estabilidad, pluralismo, cohesión, justicia social) que cada uno favorece. Escribe luego una propuesta de tres líneas que combine lo mejor de ambos, sin tomar partido.",
        "Mayoritario: A 10, B 0, C 0; ventaja, mayoría clara; riesgo, dejar sin voz al 40 %; favorece estabilidad. Proporcional: A 6, B 3, C 1; ventaja, representa más; riesgo, acuerdos difíciles; favorece pluralismo. Propuesta: proporcional con un umbral mínimo y mecanismos de acuerdo.",
        ["calcula bien", "usa criterios", "propone sin partido"], ["tabla de dos sistemas", "propuesta"], ["decir que un sistema es antidemocrático", "tomar partido"],
        "Pregunta qué valor pesa más para ella o él y por qué."),
    reinforce="Calcula cómo se repartirían 10 escaños con votos 500, 300 y 200.",
    extend="Anota cómo se eligen los representantes de curso en tu liceo y qué tipo de sistema es.",
)

# ============================================================ OA 01, clase 4
F = ("Ficha 41 (tema de deliberación de ejemplo): en el país ficticio Tierra Alta se propone descentralizar: que las regiones decidan sobre el 40 % de la inversión en salud y educación que hoy decide el gobierno central. "
     "A favor: decisiones más cercanas a las necesidades. En contra: puede aumentar las desigualdades entre regiones con distinta capacidad técnica. "
     "Dato de ejemplo: de 10 regiones, 3 tienen equipos técnicos fuertes y 7 equipos débiles.")
build(
    O1, 4, F,
    use="Aprenderé a deliberar sobre cómo distribuir el poder entre niveles, con razones, evidencia y propuestas que cuiden el bien común y la justicia social.",
    prior=["Sé qué es la descentralización.", "Sé estructurar un argumento.", "Sé leer proporciones."],
    explain=[
        "Descentralizar acerca las decisiones a quienes viven los problemas y puede aumentar la participación. Pero también puede crear desigualdades si no todas las regiones cuentan con los mismos recursos y capacidades. Por eso las propuestas serias combinan traspaso de decisiones con apoyo técnico, reglas comunes y mecanismos de control.",
        "Para deliberar se examinan los criterios: cercanía, eficacia, equidad entre regiones, rendición de cuentas y capacidad. Un argumento fuerte reconoce la objeción: si 7 de 10 regiones tienen equipos débiles, se necesita un plan de fortalecimiento. Una propuesta puede ser gradual: traspasar primero una parte y ampliar según resultados.",
        "También se decide cómo se controlará: auditorías, transparencia y participación de la ciudadanía regional. La deliberación respeta a quienes disienten y acepta que la decisión puede ajustarse con evidencia. Lo importante es que la distribución del poder no deje a nadie con peores servicios por vivir en un lugar.",
    ],
    vocab=[("capacidad técnica", "conocimientos y recursos de un equipo para gestionar bien"), ("equidad territorial", "reparto justo de recursos y oportunidades entre territorios"), ("auditoría", "revisión independiente del uso de recursos"), ("traspaso gradual", "paso de decisiones por etapas"), ("rendición de cuentas", "deber de explicar y justificar las decisiones y gastos")],
    worked=[
        ("Proporción de regiones", "De 10 regiones de ejemplo, 4 tienen equipos fuertes. ¿Cuántas tienen equipos débiles?", ["Se resta 4 a 10.", "Son 6."], "6 regiones"),
        ("Medida de equidad", "Si las regiones con equipos débiles reciben apoyo técnico, ¿qué criterio mejora?", ["Se reducen diferencias.", "Mejora la equidad territorial."], "Equidad territorial"),
    ],
    mistakes=[("Suponer que acercar las decisiones siempre las mejora.", "Sin capacidad técnica pueden empeorar.", "Combínalo con apoyo y control."),
              ("Rechazar la descentralización por un solo riesgo.", "Se puede diseñar con salvaguardas.", "Propón ajustes y plazos.")],
    T=[
        ('abc', '¿Qué significa descentralizar?', 'Traspasar decisiones y recursos a niveles regionales o locales', 'Reunir todas las decisiones en el nivel nacional', 'Eliminar los gobiernos locales', 'Descentralizar acerca las decisiones a quienes viven los problemas.'),
        ('=', '{F} Si la inversión en salud y educación es de 5.000 millones, ¿cuántos millones decidirían las regiones con la propuesta del 40 %?', '5000*40//100', 'Se calcula el 40 % de la inversión total.', ' millones'),
        ('=', '{F} ¿Qué porcentaje de las regiones tiene equipos técnicos débiles?', '7*100//10', 'Se compara la cantidad de regiones débiles con el total.', ' %'),
        ('abc', '{F} ¿Qué ventaja menciona la ficha?', 'Decisiones más cercanas a las necesidades de cada región', 'Menos necesidad de controles, porque cada región decide por sí sola', 'Servicios idénticos en todo el país, sin diferencias entre regiones', 'Es el argumento a favor registrado en la ficha.'),
        ('abc', '{F} ¿Qué riesgo menciona la ficha?', 'Aumentar las desigualdades entre regiones con distinta capacidad técnica', 'Disminuir la participación local, porque se decide lejos de la gente', 'Concentrar el poder en el gobierno central y en sus oficinas', 'Es la objeción registrada en la ficha.'),
        ('abc', '{F} ¿Qué criterio se afecta con los equipos débiles?', 'Equidad territorial, entre regiones fuertes y débiles', 'Cercanía, porque se decide más cerca de la gente', 'Rendición de cuentas, porque se informa al gobierno central', 'Habría diferencias de resultados entre regiones por vivir en lugares distintos.'),
        ('abc', '{F} ¿Qué medida reduce el riesgo de desigualdad?', 'Apoyo técnico a las regiones más débiles y traspaso gradual', 'Traspasar todo de una vez para ganar tiempo y evitar demoras', 'Traspasar solo a las regiones fuertes y dejar a las demás sin apoyo', 'Fortalece la capacidad donde falta y avanza por etapas.'),
        ('abc', '{F} ¿Qué es una auditoría?', 'Una revisión independiente del uso de recursos', 'Un informe que prepara la propia región sobre sus resultados', 'Una votación regional sobre el gasto', 'Es un control hecho por quien no administra los recursos.'),
        ('abc', '{F} Un participante dice: «Descentralizar siempre mejora los servicios». ¿Qué corresponde?', 'Pedir evidencia y considerar el caso de las regiones con equipos débiles', 'Aceptarlo, porque lo local siempre funciona mejor que lo central', 'Rechazarlo, porque lo central siempre funciona mejor que lo local', 'Ningún modelo es siempre mejor; depende de las condiciones.'),
        ('=', '{F} Si el traspaso gradual parte con la mitad del 40 % en el primer año, ¿qué porcentaje de la inversión deciden las regiones ese año?', '40//2', 'Se toma la mitad del porcentaje total.', ' %'),
        ('abc', '{F} ¿Qué indicador mostraría si mejora la equidad?', 'La diferencia de resultados en salud y educación entre regiones', 'Cantidad de discursos de autoridades sobre el traspaso', 'Número de regiones que firmaron el acuerdo de traspaso', 'Mide el efecto en las desigualdades entre regiones.'),
        ('abc', '{F} ¿Qué propuesta es más sólida?', 'Traspaso gradual con apoyo técnico, auditoría y participación regional', 'Traspaso inmediato sin controles para acelerar las decisiones', 'Mantener todo centralizado sin cambios ni apoyo a las regiones', 'Combina las razones a favor con salvaguardas frente a la objeción.'),
        ('abc', '{F} Un participante dice: «Las regiones débiles no sirven para decidir». ¿Qué respuesta es más justa?', 'Apoyarlas con capacidad técnica en vez de excluirlas de las decisiones', 'Aceptarlo y mantener las decisiones en el nivel central', 'Traspasar igualmente sin ningún apoyo', 'El problema se enfrenta fortaleciendo capacidades, no negando la participación.'),
    ],
    ctx=('abc', 'Un liceo de ejemplo traspasa el manejo de un fondo a cada curso. ¿Qué medida evita desigualdades entre cursos?', 'Orientación y reglas comunes para todos los cursos', 'Más dinero para el curso con mejor desempeño', 'Ninguna regla, para respetar la autonomía', 'Apoya a quien tiene menos capacidad y mantiene un marco común.'),
    sc=[
        ('¿Qué es el traspaso gradual?', 'Traspasar decisiones por etapas, ampliándolas según los resultados', 'Reduce los riesgos de un cambio brusco.'),
        ('abc', '¿Qué es la equidad territorial?', 'El reparto justo de recursos y oportunidades entre territorios', 'Que todos los lugares tengan exactamente lo mismo', 'Que cada territorio dependa solo de sus propios recursos', 'Toma en cuenta que los territorios parten con recursos y capacidades distintas.'),
        ('¿Qué es la rendición de cuentas?', 'El deber de explicar y justificar decisiones y gastos', 'Permite que la ciudadanía controle a las autoridades.'),
    ],
    op=("Con la {F} escribe una propuesta de siete líneas: tu postura sobre la descentralización, una razón con el dato, una objeción, una medida de apoyo, una medida de control, un indicador y qué harías si el indicador no mejora.",
        "Postura: descentralizar con gradualidad. Razón: las decisiones cercanas responden mejor. Objeción: 7 de 10 regiones tienen equipos débiles. Apoyo: asistencia técnica. Control: auditoría y transparencia. Indicador: diferencia de resultados entre regiones. Si no mejora: detener el traspaso y reforzar apoyo.",
        ["usa el dato", "propone control y apoyo", "incluye indicador"], ["propuesta de siete líneas"], ["ignorar las desigualdades", "no fijar control"],
        "Pregunta cómo participaría la ciudadanía regional."),
    reinforce="Explica por qué descentralizar requiere apoyo técnico.",
    extend="Averigua qué decisiones toma tu municipio y cuáles el gobierno regional.",
)

# ============================================================ OA 01, clase 5
F = ("Ficha 42 (diagnóstico de ejemplo en el liceo ficticio Los Espinos): 80 estudiantes encuestados; 60 no saben cómo se decide el uso del presupuesto del centro de estudiantes y 20 sí. "
     "Recursos: un parlamento escolar simulado de una jornada, 12 voluntarios, 3 semanas y una persona adulta responsable. Idea: simular el proceso de una ley (iniciativa, comisión, votación, promulgación y control) con un tema del liceo.")
build(
    O1, 5, F,
    use="Aprenderé a diseñar una acción democrática para comprender y mejorar la institucionalidad, con objetivos, roles, simulación y evaluación.",
    prior=["Sé cómo se tramita una ley.", "Sé diseñar una acción con objetivo e indicador.", "Sé cuidar la inclusión."],
    explain=[
        "Un parlamento escolar simulado es una actividad en que los estudiantes representan roles (iniciativa, comisión, plenario, gobierno, tribunal) para entender cómo se toman las decisiones. Se elige un tema del liceo, se debate con reglas y se vota. Al final se reflexiona sobre qué aprendieron y qué cambiarían en las instituciones reales.",
        "El diseño parte del diagnóstico: 60 de 80 estudiantes no saben cómo se decide el presupuesto. Se plantea un objetivo medible, se asignan roles, se preparan reglas de debate y de votación, y se define un indicador, como cuántos estudiantes explican el proceso al final. Se cuida la inclusión: todos pueden hablar y no se obliga a posturas personales.",
        "Se incluye un control: un grupo que verifica el cumplimiento de las reglas, como un tribunal. Al terminar se evalúa con una encuesta, se informan los resultados y se propone un cambio real posible, por ejemplo publicar el presupuesto. Una simulación bien hecha enseña que las instituciones requieren reglas, tiempo y respeto.",
    ],
    vocab=[("simulación", "actividad en que se representan roles para entender un proceso real"), ("plenario", "reunión de todos los participantes para votar"), ("comisión", "grupo que estudia un tema antes del plenario"), ("regla de debate", "norma para hablar y escuchar con orden"), ("indicador de aprendizaje", "dato que muestra si las personas comprendieron")],
    worked=[
        ("Objetivo medible", "En un curso de ejemplo 30 de 100 saben cómo se elige al centro de estudiantes y se quiere llegar a 70. ¿Cuántos más deben aprender?", ["Se resta 30 a 70.", "Son 40."], "40 estudiantes más"),
        ("Rol de control", "En la simulación de ejemplo, un grupo revisa si se respetaron las reglas. ¿Qué institución real representa?", ["Controla el procedimiento.", "Se parece a un tribunal."], "Un tribunal o un órgano de control"),
    ],
    mistakes=[("Hacer la simulación sin reglas de debate.", "Gana quien habla más fuerte.", "Fija tiempos y turnos."),
              ("Obligar a defender una postura personal en el juego de roles.", "Puede exponer a las personas.", "Asigna roles y posturas ficticias.")],
    T=[
        ('abc', '¿Qué es una simulación como el parlamento escolar?', 'Una actividad en que se representan roles para entender un proceso real', 'Una votación real que decide un cambio inmediato en el liceo', 'Una charla en que expone una sola persona ante el curso', 'Se imita un proceso para aprender cómo funciona.'),
        ('=', '{F} ¿Qué porcentaje de los 80 encuestados no sabe cómo se decide el presupuesto?', '60*100//80', 'Se compara la cantidad que no sabe con el total.', ' %'),
        ('abc', '{F} ¿Qué es un plenario?', 'La reunión de todos los participantes para debatir y votar', 'El grupo que prepara el tema antes de votar', 'El grupo que revisa si se cumplieron las reglas', 'El plenario reúne a todos; la comisión prepara y el tribunal verifica.'),
        ('abc', '{F} ¿Qué hace la comisión?', 'Estudia el tema y prepara la discusión antes del plenario', 'Vota la propuesta final junto con todos los participantes', 'Promulga el resultado de la votación como si fuera ley', 'Prepara el debate para que el plenario decida mejor.'),
        ('abc', '{F} ¿Qué función cumple el tribunal en la simulación?', 'Verifica que se cumplan las reglas y los derechos del debate', 'Decide el tema que se votará antes de la simulación', 'Presenta el proyecto de ley que se discutirá en el plenario', 'Es el control sobre el procedimiento.'),
        ('abc', '{F} ¿Cuál es un objetivo medible?', 'Que al final 60 de los 80 estudiantes expliquen cómo se decide el presupuesto', 'Que los estudiantes valoren más al centro de estudiantes del liceo', 'Que la actividad sea entretenida y divertida para todos', 'Un número y un plazo permiten comprobarlo.'),
        ('=', '{F} Si el objetivo es que 60 de los 80 estudiantes sepan cómo se decide el presupuesto, ¿cuántos más que los 20 actuales deben aprenderlo?', '60-20', 'Se resta los actuales a la meta.', ' estudiantes'),
        ('abc', '{F} ¿Qué indicador mide el aprendizaje?', 'Cuántos estudiantes explican el proceso al final en una breve prueba', 'Cuántos estudiantes asistieron al plenario el día de la simulación', 'Cuántos afiches se pegaron durante las tres semanas', 'Mide comprensión, no solo asistencia o actividad.'),
        ('=', '{F} Si cada uno de los 5 roles (iniciativa, comisión, plenario, gobierno y tribunal) necesita 3 voluntarios, ¿cuántos faltan con los 12 disponibles?', '5*3-12', 'Se calcula cuántos se necesitan y se resta los disponibles.', ' voluntarios'),
        ('abc', '{F} ¿Qué regla favorece un debate respetuoso?', 'Turnos y tiempos para hablar iguales para todos', 'Hablar todos a la vez para ahorrar tiempo', 'Dar la palabra primero a quienes más conocen el tema', 'Una regla de debate asegura orden e igualdad de oportunidades.'),
        ('abc', '{F} ¿Qué cuidado se tiene con las posturas de los participantes?', 'Se asignan posturas ficticias para no exponer opiniones personales', 'Se obliga a cada persona a revelar su opinión real', 'Se evalúa a quienes defiendan posturas impopulares', 'Protege la privacidad y la libertad de pensamiento.'),
        ('abc', '{F} ¿Qué cambio real podría proponerse al final?', 'Publicar el presupuesto del centro de estudiantes y cómo se decide', 'Eliminar el centro de estudiantes y pasar sus funciones a la dirección', 'Aumentar el presupuesto del centro sin consultar a nadie', 'Mejora la transparencia, que es lo que el diagnóstico muestra que falta.'),
        ('abc', '{F} ¿Qué medida de seguridad corresponde?', 'Una persona adulta responsable durante la jornada', 'Hacerla sin supervisión para dar autonomía', 'Pedir a un estudiante que vigile solo', 'La presencia de un adulto responsable cuida al grupo durante toda la actividad.'),
    ],
    ctx=('abc', 'Un curso de ejemplo simula un juicio sobre una norma de convivencia. ¿Qué aprende sobre las instituciones?', 'Que los procedimientos y roles buscan asegurar un trato justo', 'Que las instituciones no sirven', 'Que el resultado de un juicio se decide por votación del curso', 'Un juicio simulado muestra cómo un procedimiento protege derechos.'),
    sc=[
        ('¿Qué es un plenario?', 'La reunión de todos los participantes para debatir y votar', 'Es la instancia donde se toma la decisión final.'),
        ('abc', '¿Qué es un indicador de aprendizaje?', 'Un dato que muestra cuánto comprendieron las personas', 'Una calificación de cada participante en el curso de educación ciudadana', 'Una lista de asistencia a las actividades de la simulación', 'Mide la comprensión de lo aprendido.'),
        ('¿Qué es una regla de debate?', 'Una norma para hablar y escuchar con orden', 'Asegura respeto e igualdad de oportunidades para hablar.'),
    ],
    op=("Con la {F} diseña el parlamento escolar: objetivo medible, tema, cinco roles, reglas de debate, pasos con semana, un control del procedimiento, un indicador y una medida de inclusión.",
        "Objetivo: 60 de 80 expliquen cómo se decide el presupuesto. Tema: uso de un fondo de $100.000. Roles: iniciativa, comisión, plenario, gobierno, tribunal. Reglas: turnos de un minuto. Pasos: semana 1 reglas, semana 2 ensayo, semana 3 jornada. Control: tribunal. Indicador: encuesta final. Inclusión: todos pueden hablar.",
        ["objetivo medible", "roles y reglas", "inclusión"], ["diseño de la simulación"], ["olvidar el control", "exponer posturas personales"],
        "Pregunta qué cambio real propondría tras la simulación."),
    reinforce="Escribe tres roles de una simulación y la función de cada uno.",
    extend="Averigua cómo se decide el uso de un fondo en tu liceo.",
)

# ============================================================ OA 02, clase 1
F = ("Ficha 43 (desafío de ejemplo, cuenca ficticia del río Claro): el río abastece a una ciudad, a agricultores y a una industria; en verano baja su caudal. "
     "Actores y escalas: una familia (local), un municipio (comunal), un gobierno regional, un acuerdo entre países vecinos por otro río (internacional). "
     "Valores en tensión: desarrollo económico, democracia (que se escuche a las personas), equidad y sustentabilidad.")
build(
    O2, 1, F,
    use="Aprenderé qué es la corresponsabilidad ética y cómo se arman soluciones a desafíos en distintas escalas que armonicen desarrollo, democracia, equidad y sustentabilidad.",
    prior=["Sé qué es una escala territorial.", "Sé qué es la justicia ambiental.", "Sé qué es una virtud pública."],
    explain=[
        "La corresponsabilidad es la responsabilidad compartida: los problemas colectivos no los resuelve una sola persona o institución, sino todas las que contribuyen a ellos o se benefician de ellos, cada una según sus posibilidades. Es ética cuando se basa en principios como la dignidad, la justicia, el respeto y el cuidado de las generaciones futuras.",
        "Los desafíos ocurren en varias escalas: personal, comunitaria, comunal, regional, nacional y global. Un problema como la escasez de agua exige acciones en cada una: hábitos y cuidado en el hogar, reglas locales, planificación regional y acuerdos internacionales. Mirar las escalas evita culpar a uno solo o creer que otros deben resolverlo todo.",
        "Armonizar significa buscar soluciones que cuiden a la vez cuatro aspectos: desarrollo (bienestar y empleo), democracia (participación y derechos), equidad (reparto justo) y sustentabilidad (cuidado del futuro). A veces hay tensiones entre ellos y se necesitan acuerdos, plazos y compensaciones. Una solución justa explica quién gana, quién cede y cómo se revisará.",
    ],
    vocab=[("corresponsabilidad", "responsabilidad compartida entre quienes contribuyen a un problema o se benefician de él"), ("armonizar", "buscar soluciones que cuiden varios aspectos a la vez"), ("sustentabilidad", "uso de recursos sin comprometer a las generaciones futuras"), ("equidad", "reparto justo que considera necesidades distintas"), ("generaciones futuras", "personas que vivirán después de nosotros")],
    worked=[
        ("Escalas de un problema", "El exceso de basura en una ciudad de ejemplo se enfrenta con hábitos en cada hogar y con normas comunales. ¿Qué escalas aparecen?", ["Hogar es personal.", "Normas comunales son comunales."], "Personal y comunal"),
        ("Valores en tensión", "Una decisión de ejemplo crea empleos pero contamina un río. ¿Qué valores chocan?", ["Desarrollo.", "Sustentabilidad."], "Desarrollo y sustentabilidad"),
    ],
    mistakes=[("Pensar que un problema colectivo es responsabilidad de otro.", "Todos los que contribuyen o se benefician comparten parte.", "Identifica qué hace cada actor según sus posibilidades."),
              ("Creer que se debe elegir un solo valor.", "Se puede armonizar.", "Busca soluciones que cuiden varios aspectos.")],
    T=[
        ('abc', 'En Educación Ciudadana: ¿Qué es la corresponsabilidad?', 'La responsabilidad compartida entre quienes contribuyen a un problema o se benefician', 'La responsabilidad de la autoridad que tiene más poder para decidir', 'La responsabilidad de la persona que causó el problema primero', 'Los problemas colectivos no los resuelve una sola persona o institución.'),
        ('abc', '¿Qué significa armonizar desarrollo, democracia, equidad y sustentabilidad?', 'Buscar soluciones que cuiden los cuatro aspectos a la vez', 'Elegir el valor que más personas defienden y dejar los demás', 'Acordar que todos cedan exactamente lo mismo en la solución', 'Armonizar es equilibrar valores que a veces entran en tensión.'),
        ('abc', '{F} ¿Qué escala representa la familia?', 'Local', 'Regional', 'Nacional', 'La ficha ubica a la familia como la escala local.'),
        ('abc', '{F} ¿Qué escala representa el acuerdo entre países vecinos?', 'Internacional, por involucrar a varios países', 'Comunal, por involucrar a un solo municipio', 'Regional, por involucrar a varias comunas', 'Un acuerdo entre varios países se ubica en la escala internacional.'),
        ('abc', '{F} ¿Qué valor corresponde a cuidar el río para el futuro?', 'Sustentabilidad', 'Desarrollo económico', 'Equidad', 'Cuidar el río para el futuro es pensar en las generaciones que vienen.'),
        ('abc', '{F} ¿Qué valor es que se escuche a las personas afectadas?', 'Democracia, que incluye participación y derechos', 'Equidad, que es el reparto justo', 'Desarrollo, que es el bienestar y el empleo', 'La ficha asocia la democracia con que se escuche a las personas.'),
        ('abc', '{F} ¿Qué acción es de escala personal?', 'Ahorrar agua en casa y reparar fugas', 'Firmar un tratado internacional', 'Crear una ley nacional', 'Es una acción individual dentro del hogar.'),
        ('abc', '{F} ¿Qué acción es de escala regional?', 'Planificar el uso del agua entre varias comunas', 'Arreglar una llave de un hogar para evitar el goteo', 'Firmar un acuerdo con otros países sobre un río compartido', 'Coordina varios municipios de una región.'),
        ('abc', '{F} Un participante dice: «El agua es problema del gobierno, no mío». ¿Qué corresponde?', 'Recordar que cada actor tiene una parte, según sus posibilidades', 'Aceptarlo, porque el Estado tiene más recursos', 'Responder que solo los hogares deben cuidar el agua', 'La corresponsabilidad reparte tareas entre todos los actores.'),
        ('abc', '{F} ¿Qué solución armoniza los cuatro aspectos?', 'Un acuerdo de uso del agua con participación, apoyo a quienes tienen menos y metas de ahorro', 'Dar más agua a quien paga más, sin considerar a los demás', 'Priorizar la industria por los empleos que genera en la cuenca', 'Cuida a la vez democracia, equidad, sustentabilidad y desarrollo.'),
        ('abc', '{F} ¿Qué principio ético orienta una solución justa?', 'Cuidar la dignidad de todas las personas y de las generaciones futuras', 'Priorizar a quienes tienen más poder de decisión sobre el agua', 'Priorizar el beneficio de hoy sobre el de las generaciones futuras', 'La ética de la corresponsabilidad se basa en dignidad, justicia y cuidado del futuro.'),
        ('abc', '{F} ¿Por qué conviene mirar el problema en varias escalas?', 'Porque evita culpar a un solo actor o esperar que otros lo resuelvan todo', 'Porque así cada actor puede desentenderse de su parte del problema', 'Porque la escala global es la única que importa en el caso', 'Cada escala aporta acciones distintas y complementarias.'),
        ('=', '{F} Si en verano el río aporta 600 unidades y la demanda es de 1.000, ¿qué porcentaje de la demanda no se cubre?', '(1000-600)*100//1000', 'Se calcula lo que falta y se compara con la demanda.', ' %'),
    ],
    ctx=('abc', 'Un edificio de ejemplo tiene cortes de agua por mal uso. ¿Qué es una acción corresponsable?', 'Acordar entre vecinos reglas de uso y revisar las fugas', 'Culpar a un solo vecino y pedirle que repare todo', 'Esperar a que la administración lo resuelva por su cuenta', 'En la corresponsabilidad, todas las personas asumen una parte del cuidado común.'),
    sc=[
        ('¿Qué es la equidad?', 'Un reparto justo que considera necesidades distintas', 'Mira las diferencias entre personas y territorios.'),
        ('abc', '¿Qué es la sustentabilidad?', 'El uso de recursos sin comprometer a las generaciones futuras', 'Gastar todo hoy para asegurar el bienestar de las personas actuales', 'Ahorrar sin usar ningún recurso para no afectar el futuro', 'Piensa en el futuro al tomar decisiones.'),
        ('¿Qué son las generaciones futuras?', 'Las personas que vivirán después y dependerán de los recursos que cuidemos hoy', 'Su cuidado es un principio ético de la corresponsabilidad.'),
    ],
    op=("Con la {F} haz una tabla con cuatro escalas (personal, comunal, regional, internacional): una acción posible, quién la hace y qué valor protege. Termina con una frase sobre cómo armonizar desarrollo, democracia, equidad y sustentabilidad.",
        "Personal: ahorrar agua; cada persona; sustentabilidad. Comunal: reglas de uso; municipio; equidad. Regional: planificación; gobierno regional; desarrollo. Internacional: acuerdos; países; democracia. Armonizar: acuerdos con participación, apoyo a quienes tienen menos y metas de ahorro.",
        ["relaciona escalas y acciones", "identifica valores", "propone armonizar"], ["tabla de cuatro escalas", "frase final"], ["culpar a un solo actor", "elegir un solo valor"],
        "Pregunta qué acción personal puede hacer esta semana."),
    reinforce="Explica con tus palabras por qué el problema del agua es de corresponsabilidad.",
    extend="Anota una acción de tu hogar que ayude a cuidar un recurso.",
)

# ============================================================ OA 02, clase 2
F = ("Ficha 44 (caso de ejemplo): en la cuenca del río Claro, el municipio de Villa Verde propone reducir en 20 % el uso de agua en verano. "
     "Datos de ejemplo: la ciudad usa 1.000 unidades de agua al mes; los agricultores, 2.000; la industria, 1.000. Sin la medida, en verano faltarían 400 unidades. "
     "Fuentes: el informe técnico del municipio, una carta de agricultores que dice que la medida los perjudica más, y una nota de un medio local.")
build(
    O2, 2, F,
    use="Aprenderé a investigar un problema ambiental y social con cifras, para ver quién usa los recursos, quién se perjudica y qué soluciones se proponen.",
    prior=["Sé qué es la corresponsabilidad.", "Sé calcular porcentajes simples.", "Sé comparar fuentes."],
    explain=[
        "Investigar un problema de recursos compartidos exige conocer quién usa cuánto y cuánto falta. En el caso de ejemplo, el consumo total es la suma de los usos de la ciudad, los agricultores y la industria. Una reducción porcentual afecta distinto a cada uno según su uso y su capacidad de adaptarse.",
        "Una medida puede ser igual para todos o diferenciada. Una reducción igual del 20 % parece justa, pero puede afectar más a quienes dependen del agua para su sustento. Una medida diferenciada considera usos esenciales (beber, higiene), productivos y de lujo. Se evalúa con criterios: eficacia, equidad, participación y sustentabilidad.",
        "Las fuentes tienen propósitos: un informe técnico entrega datos; una carta expresa preocupación de un grupo; una nota informa. Se anotan los hechos, los límites de los datos y lo que falta, como el costo de adaptarse. Se evita atribuir mala intención a un grupo sin pruebas y se respeta la voz de todos.",
    ],
    vocab=[("consumo", "cantidad de un recurso que se usa"), ("reducción porcentual", "disminución expresada como parte de cada 100"), ("uso esencial", "uso necesario para vivir con dignidad, como beber"), ("medida diferenciada", "medida que considera distintas situaciones"), ("adaptación", "cambio que permite seguir funcionando con menos recursos")],
    worked=[
        ("Calcular una reducción", "Un grupo de ejemplo usa 500 unidades y debe reducir 10 %. ¿Cuántas unidades ahorra?", ["10 % de 500 es una décima parte.", "500 entre 10."], "50 unidades"),
        ("Medida diferenciada", "En un caso de ejemplo se pide reducir más el riego de jardines que el agua para beber. ¿Qué tipo de medida es?", ["Considera usos distintos.", "Es diferenciada."], "Diferenciada"),
    ],
    mistakes=[("Creer que una reducción igual es siempre justa.", "Afecta distinto a quienes tienen menos capacidad.", "Considera usos esenciales y capacidad de adaptarse."),
              ("Culpar a un sector sin mirar los datos.", "Se omiten los usos y las responsabilidades.", "Usa cifras y escucha a todos.")],
    T=[
        ('abc', '¿Qué es un uso esencial del agua?', 'Un uso necesario para vivir con dignidad, como beber o la higiene', 'Un uso que genera más ingresos para quienes lo realizan', 'Un uso que realizan más personas en la ciudad', 'Se prioriza al diseñar medidas diferenciadas.'),
        ('=', '{F} ¿Cuántas unidades usan en total los tres sectores?', '1000+2000+1000', 'Se suman los usos de la ciudad, los agricultores y la industria.', ' unidades'),
        ('=', '{F} ¿Cuántas unidades se ahorrarían con una reducción del 20 % del total?', '4000*20//100', 'Se calcula el 20 % del consumo total de 4.000 unidades.', ' unidades'),
        ('=', '{F} ¿Cuántas unidades ahorrarían los agricultores si reducen el 20 % de su uso?', '2000*20//100', 'Se calcula el 20 % de 2.000 unidades.', ' unidades'),
        ('abc', '{F} ¿Qué sector usa más agua?', 'Los agricultores, con 2.000 unidades', 'La ciudad, con 1.000 unidades', 'La industria, con 1.500 unidades', 'Usan 2.000, más que los otros dos sectores.'),
        ('abc', '{F} ¿Qué dice la carta de los agricultores?', 'Que la medida los perjudica más que a otros sectores', 'Que la medida es perfecta y debe aplicarse sin cambios', 'Que el agua no falta en verano y la medida es innecesaria', 'La ficha registra que la carta afirma que la medida los perjudica más.'),
        ('abc', '{F} ¿Qué dato falta para evaluar la carta?', 'Cuánto cuesta a los agricultores adaptarse a usar menos agua', 'Cuántos agricultores votan en el municipio y cuántos son socios', 'Cuántos años tiene el municipio y cuántos alcaldes ha tenido', 'Sin ese dato no se puede medir el perjuicio.'),
        ('abc', '{F} ¿Qué medida sería diferenciada?', 'Proteger el agua para beber y reducir más los usos no esenciales', 'Reducir exactamente 20 % a todos por igual, sin considerar el uso', 'No reducir el consumo de ningún sector y esperar a que llueva', 'Una medida diferenciada considera los distintos usos.'),
        ('abc', '{F} Alguien dice: «Los agricultores gastan demasiada agua porque son egoístas». ¿Qué corresponde?', 'Revisar los datos y escuchar sus razones', 'Aceptarlo, porque usan la mayor parte', 'Rechazarlo, porque la agricultura nunca daña', 'No se atribuye mala intención sin pruebas.'),
        ('abc', '{F} ¿Qué conclusión es prudente?', 'Una reducción del 20 % cubriría el déficit de 400 unidades, pero hay que revisar cada sector', 'La medida es injusta porque afecta a los agricultores más que a otros', 'La medida es suficiente y no necesita revisión ni ajustes posteriores', 'Se apoya en el cálculo y deja preguntas abiertas sobre la equidad.'),
        ('=', '{F} Con una reducción del 20 % del total, ¿cuántas unidades se ahorran de más respecto del déficit de 400?', '4000*20//100-400', 'Se calcula el ahorro y se resta lo que faltaba.', ' unidades'),
        ('abc', '{F} ¿Qué diferencia hay entre una reducción igual y una diferenciada?', 'La igual aplica el mismo porcentaje a todos; la diferenciada considera usos y capacidades', 'La igual considera usos esenciales y la diferenciada no los considera', 'Ambas aplican el mismo porcentaje, pero a distintos sectores de la cuenca', 'Una medida diferenciada ajusta el esfuerzo según el uso y la capacidad.'),
        ('abc', '{F} ¿Qué es la adaptación?', 'Un cambio que permite seguir funcionando con menos recursos', 'Una sanción por usar demasiado de un recurso compartido', 'Una ampliación del consumo cuando hay más disponibilidad', 'Reduce el impacto de una restricción.'),
    ],
    ctx=('abc', 'Una comunidad de ejemplo decide que cada familia reduzca 10 % su consumo de energía. ¿Qué pregunta de equidad conviene hacer?', '¿Todas las familias tienen la misma capacidad para reducir?', '¿Cuánta energía consume el edificio municipal al año?', '¿Quién redactó la medida y en qué fecha lo hizo?', 'Una reducción igual puede pesar más sobre quienes tienen menos capacidad.'),
    sc=[
        ('¿Qué es una reducción porcentual?', 'Una disminución expresada como una parte de cada 100', 'Por ejemplo, reducir 20 % es quitar 20 de cada 100 unidades.'),
        ('abc', '¿Qué es una medida diferenciada?', 'Una que ajusta el esfuerzo según el uso y la capacidad de cada sector', 'Una que se aplica igual a todos los sectores sin excepción', 'Una que se aplica solo a quien no quiere cumplir la norma', 'Considera usos esenciales, productivos y de lujo.'),
        ('¿Qué es el consumo?', 'La cantidad de un recurso que usa una persona o un sector', 'El consumo total es la suma de los usos de cada sector.'),
    ],
    op=("Con la {F} escribe un informe de cinco puntos: consumo total, déficit, ahorro que logra la medida, dos efectos desiguales posibles y una medida diferenciada que propondrías.",
        "Consumo total: 4.000 unidades. Déficit: 400. La medida ahorra 800. Efectos desiguales: afecta más a los agricultores y a hogares con menos recursos. Medida diferenciada: proteger usos esenciales, reducir más los usos no esenciales y apoyar la adaptación agrícola.",
        ["calcula bien", "identifica desigualdades", "propone medida diferenciada"], ["informe de cinco puntos"], ["culpar a un sector", "usar una sola cifra"],
        "Pregunta qué dato adicional pediría a los agricultores."),
    reinforce="Calcula el 20 % de 1.500 y explica qué significa.",
    extend="Anota un recurso compartido de tu barrio y quién lo usa.",
)

# ============================================================ OA 02, clase 3
F = ("Ficha 45 (soluciones de ejemplo para reducir residuos en una ciudad ficticia). "
     "Solución 1 (regulatoria): prohibir bolsas plásticas de un solo uso. Solución 2 (educativa): campañas de reciclaje en barrios y colegios. "
     "Solución 3 (económica): cobrar por cada bolsa que se entregue. Solución 4 (colaborativa): puntos limpios comunitarios con participación de vecinos. "
     "Dato de ejemplo: una prueba en un barrio redujo el uso de bolsas de 100 a 40 con el cobro y a 55 con la campaña.")
build(
    O2, 3, F,
    use="Aprenderé a contrastar distintas estrategias para resolver un desafío colectivo y a evaluarlas con criterios de efectividad, equidad, participación y sustentabilidad.",
    prior=["Sé qué es la corresponsabilidad.", "Sé comparar medidas con criterios.", "Sé leer datos simples."],
    explain=[
        "Un mismo desafío admite estrategias distintas. Las regulatorias prohíben o exigen (leyes y normas); las económicas cambian incentivos (cobros, subsidios); las educativas buscan cambiar hábitos con información; las colaborativas organizan a la comunidad. Cada una tiene ventajas y límites y suelen combinarse.",
        "Para contrastarlas se usan criterios: efectividad (cuánto reduce el problema), equidad (a quién perjudica más), participación (si la comunidad opina), costo y sustentabilidad (si dura). Un dato como «de 100 a 40» muestra el efecto en una prueba, pero no garantiza el mismo resultado en todas partes ni habla de quién paga más.",
        "Una evaluación ética pregunta por los efectos en las personas con menos recursos, por la libertad de elegir y por el cuidado del futuro. Una combinación frecuente es una regla clara, apoyo educativo y alternativas accesibles para quienes tienen menos ingresos. Se revisa con indicadores y se corrige si algo no funciona.",
    ],
    vocab=[("estrategia regulatoria", "solución basada en leyes y normas"), ("estrategia económica", "solución que cambia incentivos mediante cobros o ayudas"), ("estrategia educativa", "solución que busca cambiar hábitos con información"), ("incentivo", "estímulo que motiva a actuar de cierta forma"), ("efectividad", "cuánto reduce un problema una medida")],
    worked=[
        ("Calcular efectividad", "Un cobro de ejemplo baja el uso de 200 a 120. ¿Cuánto redujo?", ["Se resta 120 a 200.", "Redujo 80 unidades."], "80 unidades"),
        ("Clasificar una estrategia", "Un municipio de ejemplo premia con descuentos a quienes reciclan. ¿Qué estrategia es?", ["Usa un incentivo.", "Es económica."], "Económica"),
    ],
    mistakes=[("Elegir la estrategia solo por su efectividad.", "Puede perjudicar más a quienes tienen menos recursos.", "Revisa equidad y participación."),
              ("Creer que el resultado de una prueba vale para todas partes.", "Cambian los contextos.", "Habla de «en esa prueba».")],
    T=[
        ('abc', '¿Qué caracteriza a una estrategia económica?', 'Cambia incentivos con cobros o subsidios', 'Prohíbe o exige mediante leyes', 'Informa para cambiar hábitos', 'Las estrategias económicas actúan sobre los incentivos.'),
        ('abc', '{F} Cobrar por cada bolsa que se entregue, ¿qué tipo de estrategia es?', 'Económica', 'Regulatoria', 'Educativa', 'Cambia el incentivo para usar bolsas.'),
        ('abc', '{F} Las campañas de reciclaje en barrios y colegios, ¿qué tipo de estrategia son?', 'Educativa', 'Económica', 'Regulatoria', 'Las campañas informan para que las personas cambien sus hábitos.'),
        ('abc', '{F} Los puntos limpios comunitarios con participación de vecinos, ¿qué estrategia son?', 'Colaborativa', 'Regulatoria', 'Económica', 'Organizan a la comunidad para actuar.'),
        ('=', '{F} ¿En qué porcentaje redujo el uso de bolsas el cobro en la prueba?', '(100-40)*100//100', 'Se compara la reducción con el uso inicial.', ' %'),
        ('=', '{F} ¿En qué porcentaje redujo el uso de bolsas la campaña en la prueba?', '(100-55)*100//100', 'Se compara la reducción con el uso inicial.', ' %'),
        ('abc', '{F} ¿Qué estrategia fue más efectiva en la prueba?', 'El cobro: redujo el uso de 100 a 40 bolsas', 'La campaña: redujo el uso de 100 a 55 bolsas', 'Ambas redujeron lo mismo', 'Una reducción de 60 es mayor que una de 45.'),
        ('abc', '{F} ¿Qué criterio puede cuestionar al cobro?', 'Equidad, porque pesa más en hogares de menos ingresos', 'Efectividad, porque no redujo el uso', 'Participación, porque exige que todos opinen', 'El mismo cobro pesa más en quienes tienen menos ingresos.'),
        ('abc', '{F} ¿Qué estrategia fomenta la participación de vecinos?', 'Los puntos limpios comunitarios', 'La prohibición de bolsas', 'El cobro por bolsa', 'Los vecinos participan en su organización.'),
        ('abc', '{F} ¿Qué combinación es más equilibrada?', 'Regla clara, campaña educativa y alternativas accesibles', 'Solo prohibir, sin ofrecer alternativas accesibles a las personas', 'Solo campañas, sin ninguna regla que las respalde', 'Cuida efectividad, equidad y participación a la vez.'),
        ('abc', '{F} Alguien dice: «El cobro funciona en todas las ciudades». ¿Qué corresponde?', 'Recordar que fue una prueba en un barrio', 'Aceptarlo, porque redujo más que la campaña', 'Rechazarlo, porque los cobros nunca funcionan', 'Un dato de prueba no se generaliza sin más evidencia.'),
        ('abc', '{F} ¿Qué medida corrige el efecto desigual del cobro?', 'Entregar bolsas reutilizables gratuitas a hogares de bajos ingresos', 'Aumentar el cobro por bolsa para reducir todavía más el uso', 'Eliminar la campaña educativa y mantener solo el cobro', 'Mejora la equidad sin renunciar al incentivo.'),
        ('abc', '{F} ¿Qué indicador mide el éxito de la combinación?', 'Bolsas usadas por persona y satisfacción de los vecinos', 'Cantidad de carteles instalados en las calles de la ciudad', 'Número de reuniones realizadas en los barrios', 'Mide resultados y no solo actividades.'),
    ],
    ctx=('abc', 'Un liceo de ejemplo prohíbe vender bebidas en envases desechables. ¿Qué tipo de estrategia es?', 'Regulatoria', 'Económica', 'Educativa', 'Una prohibición es una norma que exige o impide algo.'),
    sc=[
        ('¿Qué es un incentivo?', 'Un estímulo que motiva a actuar de cierta forma', 'Un cobro o un premio pueden ser incentivos.'),
        ('abc', '¿Qué es una estrategia educativa?', 'Una solución que busca cambiar hábitos con información', 'Una multa por incumplir una norma sobre el uso de bolsas', 'Un cobro por cada unidad usada, que cambia el incentivo', 'Busca cambiar hábitos informando y haciendo conscientes a las personas del problema.'),
        ('¿Qué es la efectividad?', 'Cuánto reduce un problema una medida', 'Mide el resultado de la medida.'),
    ],
    op=("Con la {F} arma una tabla con las cuatro soluciones: ventaja, riesgo y criterio que mejor cumple. Luego propone una combinación de tres líneas que cuide la equidad.",
        "Prohibir: ventaja clara; riesgo, pocas alternativas; efectividad. Campaña: ventaja, conciencia; riesgo, efecto menor; participación. Cobro: ventaja, gran reducción; riesgo, pesa más en bajos ingresos; efectividad. Puntos limpios: ventaja, comunidad; riesgo, requiere organización; participación. Combinación: regla, campaña y bolsas gratuitas para hogares con menos ingresos.",
        ["usa criterios", "reconoce riesgos", "combina estrategias"], ["tabla de cuatro soluciones", "combinación"], ["elegir solo por efectividad", "olvidar la equidad"],
        "Pregunta cómo medir el resultado en un año."),
    reinforce="Explica por qué conviene combinar estrategias.",
    extend="Anota un hábito de tu hogar que podría cambiar con un incentivo.",
)

# ============================================================ OA 02, clase 4
F = ("Ficha 46 (tema de deliberación de ejemplo): una comuna ficticia debe priorizar entre tres proyectos con presupuesto para uno solo. "
     "Proyecto 1: un parque industrial que crearía 300 empleos pero ocuparía humedales. Proyecto 2: un programa de energía solar en techos de viviendas, 100 empleos y menor cuenta de luz. "
     "Proyecto 3: un sistema de transporte público gratuito para estudiantes. Puntaje de ejemplo (de 1 a 5) en desarrollo, democracia, equidad y sustentabilidad: P1 = 5, 2, 2, 1; P2 = 3, 4, 4, 5; P3 = 5, 3, 4, 3.")
build(
    O2, 4, F,
    use="Aprenderé a deliberar y decidir con una matriz de criterios que armonice desarrollo, democracia, equidad y sustentabilidad, reconociendo sus límites.",
    prior=["Sé armonizar valores.", "Sé evaluar con criterios.", "Sé sumar y comparar puntajes."],
    explain=[
        "Una matriz de decisión es una tabla que compara opciones según criterios. En cada celda se pone un puntaje; luego se suman o se promedian. Sirve para ordenar la discusión, pero no decide sola: los puntajes se basan en juicios y los criterios pueden tener pesos distintos según lo que la comunidad valore.",
        "Antes de sumar se discute qué significa cada puntaje y con qué evidencia se asignó. Después se revisa si algún criterio es indispensable (por ejemplo, no dañar irreversiblemente un humedal) y se prueba cómo cambia el resultado si se dan pesos distintos. Una opción con la suma más alta puede tener un riesgo grave que la matriz no muestra.",
        "La decisión final debe ser transparente: se publican criterios, puntajes y razones, se escucha a las personas afectadas y se define cómo se corregirá. Las minorías conservan su derecho a expresar desacuerdos. Una decisión corresponsable explica qué se prioriza, qué se pierde y cómo se compensará.",
    ],
    vocab=[("matriz de decisión", "tabla que compara opciones según criterios"), ("peso de un criterio", "importancia que se le da a un criterio en la decisión"), ("irreversible", "que no puede volver a su estado anterior"), ("transparencia", "publicar las razones y los datos de una decisión"), ("compensación", "medida que equilibra un costo asumido por alguien")],
    worked=[
        ("Sumar puntajes", "Una opción de ejemplo tiene puntajes 4, 3, 2 y 5. ¿Cuál es el total?", ["Se suman los cuatro números.", "4 más 3 más 2 más 5."], "14"),
        ("Criterio indispensable", "Una opción de ejemplo tiene el total más alto pero destruye un ecosistema único. ¿Qué conviene hacer?", ["Verificar si un criterio indispensable no se cumple.", "No basta el total."], "Revisar el criterio indispensable"),
    ],
    mistakes=[("Decidir solo por la suma de puntajes.", "Los puntajes no muestran riesgos graves ni valores indispensables.", "Revisa criterios indispensables y pesos."),
              ("Asignar puntajes sin evidencia.", "Parecen objetivos pero son opiniones.", "Anota la razón de cada puntaje.")],
    T=[
        ('abc', '¿Qué es una matriz de decisión?', 'Una tabla que compara opciones según criterios con puntajes', 'Una votación entre dos opciones que decide por mayoría simple', 'Un informe con la opinión de especialistas sobre cada proyecto', 'Ordena la discusión, pero no decide sola.'),
        ('=', '{F} ¿Cuál es el total del proyecto 2 (3, 4, 4, 5)?', '3+4+4+5', 'Se suman los cuatro puntajes.', ' puntos'),
        ('=', '{F} ¿Cuál es el total del proyecto 3 (5, 3, 4, 3)?', '5+3+4+3', 'Se suman los cuatro puntajes.', ' puntos'),
        ('abc', '{F} ¿Qué proyecto tiene el mayor total sin pesos?', 'El proyecto 2, con 16 puntos', 'El proyecto 3, con 15 puntos', 'El proyecto 1, por tener el mayor puntaje en desarrollo', 'Los totales son 10, 16 y 15.'),
        ('abc', '{F} ¿Qué criterio puntúa más bajo el proyecto 1?', 'Sustentabilidad, con 1', 'Desarrollo, con 5', 'Democracia, con 2', 'Obtiene 1 en sustentabilidad y ocupa humedales.'),
        ('abc', '{F} ¿Qué es el peso de un criterio?', 'La importancia que se le da a cada criterio en la decisión', 'El puntaje más alto que aparece en la tabla de decisión', 'El número de personas que votó por cada criterio', 'Define cuánto vale cada criterio en el total.'),
        ('=', '{F} Si la comunidad da doble peso a desarrollo, ¿cuál es el total del proyecto 3?', '5*2+3+4+3', 'Se duplica el puntaje de desarrollo y se suman los demás.', ' puntos'),
        ('abc', '{F} Con doble peso a desarrollo, ¿qué proyecto lidera?', 'El proyecto 3, con 20 frente a 19 del proyecto 2', 'El proyecto 2, que mantiene el mayor total con 19 puntos', 'El proyecto 1, que sube hasta 25 puntos', 'Con doble peso, P2 suma 19, P3 suma 20 y P1 suma 15.'),
        ('abc', '{F} ¿Qué problema puede ocultar la suma en el proyecto 1?', 'Un daño irreversible a los humedales que la suma no muestra', 'Que genere demasiados empleos para la capacidad del liceo', 'Que el puntaje en desarrollo sea alto frente a los demás', 'La matriz no muestra riesgos graves que no se pueden revertir.'),
        ('abc', '{F} Alguien dice: «La matriz decide sola, no hay que discutir». ¿Qué corresponde?', 'Aclarar que los puntajes son juicios que se discuten y justifican', 'Aceptarlo, porque los números son objetivos y evitan discusiones', 'Rechazar las matrices, porque no sirven para decidir', 'La deliberación es necesaria para dar sentido a los puntajes.'),
        ('abc', '{F} ¿Qué haría más transparente la decisión?', 'Publicar criterios, puntajes y razones', 'Decidir en privado y comunicar solo el resultado', 'Publicar solo el proyecto ganador', 'Permite que otros revisen y controlen.'),
        ('abc', '{F} ¿Qué compensación podría acompañar al proyecto 2?', 'Apoyo para que quienes no tienen techo propio accedan a la energía', 'Entregar el beneficio solo a quienes ya tienen techo propio', 'Ninguna, porque no necesita ajustes', 'Cuida la equidad de quienes quedarían fuera.'),
        ('abc', '{F} ¿Qué conclusión es prudente?', 'El proyecto 2 es una buena opción por su total, sujeta a revisar el acceso y los costos', 'El proyecto 1 es siempre malo y debe descartarse de entrada', 'El proyecto 3 es mejor porque ganó en desarrollo, que es lo importante', 'Reconoce límites y evita afirmaciones absolutas.'),
    ],
    ctx=('abc', 'Un curso de ejemplo elige entre tres paseos con una matriz de seguridad, costo, aprendizaje y participación. ¿Qué debe hacerse antes de sumar?', 'Discutir qué significa cada puntaje y con qué evidencia se asignó', 'Sumar los puntajes sin conversar', 'Elegir el paseo con mayor puntaje en un solo criterio', 'Los puntajes son juicios y deben justificarse antes de sumarse.'),
    sc=[
        ('¿Qué es lo irreversible?', 'Lo que no puede volver a su estado anterior', 'Un daño irreversible no se corrige con una compensación posterior.'),
        ('abc', '¿Qué es una compensación?', 'Una medida que repara o equilibra un daño', 'Un premio para quien gana una votación', 'Un castigo para quien perdió', 'Busca equilibrar lo que se pierde con la decisión.'),
        ('En una decisión pública, ¿qué es la transparencia?', 'Publicar las razones y los datos de una decisión', 'Permite que otras personas revisen y controlen.'),
    ],
    op=("Con la {F} arma tu matriz: calcula los totales, aplica doble peso a un criterio que elijas y recalcula, y escribe una decisión de cuatro líneas con una compensación y un indicador. Debes publicar tus criterios y razones.",
        "Totales: P1 10, P2 16, P3 16. Doble peso a sustentabilidad: P1 11, P2 21, P3 20. Decisión: elegir el proyecto 2 con apoyo a hogares sin techo propio. Compensación: programa de acceso. Indicador: hogares beneficiados y ahorro en cuenta.",
        ["calcula bien", "justifica pesos", "incluye compensación e indicador"], ["matriz", "decisión de cuatro líneas"], ["decidir solo por la suma", "olvidar compensación"],
        "Pregunta qué cambiaría si el presupuesto alcanzara para dos proyectos."),
    reinforce="Explica por qué una matriz no decide sola.",
    extend="Arma una matriz simple para elegir una actividad de curso con tres criterios.",
)

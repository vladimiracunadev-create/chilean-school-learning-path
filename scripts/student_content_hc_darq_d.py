"""Diseño y arquitectura 3.º y 4.º medio HC: OAC-07 (relacionar habilidades y conocimientos de la asignatura con contextos laborales, profesionales y de desarrollo personal). Casos y fichas inventados; sin datos de remuneración ni de empleabilidad."""
from __future__ import annotations

from hc_darq_common import build

O7 = "AR-DARQ-3y4-OAC-07"

# ============================================================ OAC-07, clase 1
F = ("Ficha 30 (campos de ejemplo, descripciones generales; no son avisos de empleo). "
     "Arquitectura: proyecta edificios y espacios; usa dibujo técnico, pensamiento espacial y coordinación con otros oficios. "
     "Diseño industrial: diseña objetos que se producen en serie; trabaja con prototipos y materiales. "
     "Diseño gráfico: comunica con imágenes y texto en soportes impresos y digitales. "
     "Diseño de interiores: organiza y equipa espacios interiores. "
     "Paisajismo: diseña espacios exteriores con vegetación y recorridos. "
     "Construcción y oficios, como carpintería, albañilería y electricidad: ejecutan obras; requieren formación y, en algunos casos, certificación o licencia según la normativa vigente. "
     "Conservación del patrimonio: cuida y restaura obras de valor histórico con equipos especializados.")
build(
    O7, 1, F,
    use="Aprenderé a reconocer campos y contextos de trabajo ligados al diseño y la arquitectura y a relacionar las habilidades de esta asignatura con cada uno, sin estereotipos.",
    prior=["Sé qué habilidades he practicado en el curso.", "Sé que hay oficios con formación y normas propias.", "Sé distinguir un dato de una opinión."],
    explain=[
        "El diseño y la arquitectura se relacionan con muchos campos de trabajo. La arquitectura proyecta edificios y espacios; el diseño industrial, objetos producidos en serie; el diseño gráfico, mensajes visuales; el diseño de interiores, espacios interiores; el paisajismo, espacios exteriores con vegetación; la conservación del patrimonio, el cuidado de obras antiguas; y los oficios de la construcción, como la carpintería, la albañilería y la electricidad, ejecutan las obras. Ningún campo es mejor que otro: cumplen funciones distintas y complementarias.",
        "Las habilidades que se practican en la asignatura sirven en varios campos: leer encargos y necesidades, dibujar y medir a escala, investigar materiales, presentar a públicos distintos, evaluar con evidencia, recibir y dar retroalimentación, y cuidar la accesibilidad y la sustentabilidad. Un contexto laboral es el lugar y la forma de trabajar: una oficina, una obra, un taller, una municipalidad, una empresa o el trabajo independiente. También hay contextos de desarrollo personal, como organizar un proyecto de barrio o mejorar un espacio de la casa con apoyo de personas adultas.",
        "Algunas tareas, como el cálculo estructural, las instalaciones eléctricas o la dirección de una obra, solo pueden hacerlas personas con formación y habilitación según la normativa vigente, porque un error pone en riesgo a otras personas. Las habilidades no dependen del género ni del origen: cualquier persona con formación puede trabajar en cualquiera de estos campos. Esta ficha es general y de ejemplo.",
    ],
    vocab=[("campo profesional", "área de trabajo con tareas y formación propias"), ("contexto laboral", "lugar y forma en que se trabaja"), ("habilidad transferible", "habilidad que sirve en varios campos"), ("habilitación", "formación o licencia que exige la normativa para ciertas tareas"), ("desarrollo personal", "crecimiento de las propias capacidades e intereses")],
    worked=[
        ("Reconocer un campo", "Con la ficha, ¿qué campo diseña objetos que se producen en serie?", ["Se busca el campo que trabaja con objetos en serie.", "Es el diseño industrial."], "Diseño industrial"),
        ("Contar casillas", "Otra estudiante hace una tabla con los 7 campos de la ficha y 5 habilidades. ¿Cuántas casillas tiene?", ["Se multiplican los campos por las habilidades.", "7 × 5 = 35."], "35 casillas"),
    ],
    mistakes=[("Pensar que solo hay un camino para trabajar en diseño y arquitectura.", "Hay muchos campos y contextos, con formaciones distintas.", "Explora varios campos antes de decidir."),
              ("Creer que ciertos campos son «de hombres» o «de mujeres».", "Las habilidades no dependen del género.", "Cualquier persona con formación puede trabajar en cualquier campo.")],
    T=[
        ('abc', '¿Qué es un contexto laboral?', 'El lugar y la forma en que se trabaja, como una oficina, una obra o un taller', 'El sueldo y los beneficios que recibe quien trabaja', 'El título del curso o de la carrera que estudió quien trabaja', 'El contexto laboral describe dónde y cómo se trabaja.'),
        ('abc', '{F} ¿Qué campo proyecta edificios y espacios?', 'Arquitectura', 'Diseño gráfico', 'Paisajismo', 'La ficha dice que la arquitectura proyecta edificios y espacios.'),
        ('abc', '{F} ¿Qué campo comunica con imágenes y texto en soportes impresos y digitales?', 'Diseño gráfico', 'Diseño industrial', 'Conservación del patrimonio', 'Es el campo del mensaje visual.'),
        ('abc', '{F} ¿Qué habilidad de la asignatura es central para el diseño de interiores?', 'Organizar espacios con medidas y circulación accesible', 'Calcular la estructura de un edificio y dirigir su construcción', 'Dirigir una obra completa aunque no se tenga formación', 'El diseño de interiores usa medidas, circulación y accesibilidad.'),
        ('abc', '{F} ¿Qué campo diseña espacios exteriores con vegetación y recorridos?', 'Paisajismo', 'Diseño de interiores', 'Diseño industrial', 'Es lo que describe la ficha para el paisajismo.'),
        ('abc', '{F} ¿Por qué la ficha dice que algunos oficios requieren formación y, a veces, certificación?', 'Porque un error en algunas tareas, como las instalaciones eléctricas, pone en riesgo a las personas y la normativa lo regula', 'Porque son tareas poco importantes y por eso se pide un papel que lo certifique', 'Porque cualquier persona puede aprenderlas sin guía en un día y la certificación es solo un trámite', 'Un error en ciertas tareas pone en riesgo a otras personas.'),
        ('=', '{F} Una estudiante hace una tabla con los 7 campos de la ficha y 4 habilidades. ¿Cuántas casillas tiene?', '7*4', 'Se multiplican los campos por las habilidades.', ' casillas'),
        ('abc', '{F} Una estudiante dice: «el diseño gráfico no usa nada de lo que aprendí sobre presentaciones». ¿Qué respuesta es mejor?', 'Sí lo usa: la jerarquía, la legibilidad y la accesibilidad de un panel se parecen al trabajo gráfico', 'Tiene razón, porque el diseño gráfico solo usa dibujo artístico y nada de lo del curso', 'Solo lo usa quien dibuja a mano, porque lo digital no usa jerarquía', 'La jerarquía y la legibilidad son habilidades comunes.'),
        ('abc', '¿Qué habilidad de las trabajadas en el curso sirve en cualquier campo?', 'Evaluar con evidencia y dar retroalimentación respetuosa', 'Dibujar a escala, que solo sirve en arquitectura', 'Calcular estructuras, que sirve en todos los campos sin necesitar formación', 'Evaluar con evidencia y comunicarse con respeto sirve en todos los contextos.'),
        ('abc', 'Alguien dice: «solo los hombres sirven para construcción y solo las mujeres para diseño de interiores». ¿Qué corrección es adecuada?', 'Las habilidades no dependen del género: cualquier persona con formación puede trabajar en cualquier campo', 'Tiene razón, porque así cada persona se dedica a lo que mejor le sale por su género', 'Depende de la edad de la persona y de lo que su familia espere de ella', 'Las capacidades se desarrollan con formación y práctica, sin importar el género.'),
        ('abc', '{F} ¿Qué aplicación de desarrollo personal es adecuada y segura?', 'Diseñar una mejora accesible para la casa o el barrio, con apoyo de personas adultas y sin obras riesgosas', 'Cambiar una instalación eléctrica de la casa sin ayuda, siguiendo un video', 'Cortar muros de la casa para ampliar una pieza, midiendo bien antes de empezar', 'Las mejoras de diseño se hacen con apoyo y sin tareas que exijan habilitación.'),
        ('abc', '{F} ¿Qué relación entre habilidad y campo es más completa?', 'Dibujar y medir a escala sirve para arquitectura e interiores; comunicar con jerarquía, para diseño gráfico; probar prototipos, para diseño industrial', 'Todas las habilidades sirven con la misma intensidad en todos los campos, sin diferencias', 'Cada habilidad sirve para un solo campo y no puede usarse en otros', 'Relaciona habilidades con campos usando la información de la ficha.'),
        ('abc', '¿Por qué es útil explorar varios campos antes de decidir?', 'Porque las habilidades se usan en muchos campos y conocerlos ayuda a decidir con información', 'Porque hay que elegir el primero que aparezca para no perder tiempo', 'Porque ningún campo exige formación, así que da lo mismo cuál se elija', 'Explorar permite comparar y decidir con más información.'),
    ],
    ctx=('abc', 'Una estudiante arma una tabla: «Arquitectura: dibujar y medir a escala; diseño gráfico: presentar con jerarquía; paisajismo: investigar materiales y recorridos accesibles». ¿Qué hace bien?', 'Relaciona habilidades del curso con campos de la ficha', 'Describe campos que no están en la ficha', 'Elige un solo campo para toda la clase', 'La tabla une habilidades y campos de manera coherente.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué es una habilidad transferible?", "Una habilidad que sirve en varios campos", "Por ejemplo, evaluar con evidencia sirve en todos los campos."),
        ("¿Qué tareas requieren habilitación según la normativa?", "Las que ponen en riesgo a otras personas si se hacen sin preparación, como instalaciones eléctricas", "La formación protege a las personas."),
        ("¿Dependen las habilidades del género?", "No: cualquier persona con formación puede desarrollarlas", "Las capacidades se aprenden con práctica."),
    ],
    op=("Elige tres campos de la ficha 30. Para cada uno escribe dos habilidades de este curso que usaría, un contexto donde trabajaría (oficina, taller, obra, municipalidad, trabajo independiente u otro) y una pregunta que te gustaría hacerle a una persona que trabaje en él.",
        "Paisajismo: habilidades, medir a escala y cuidar la accesibilidad; contexto, municipalidad que mejora plazas; pregunta: ¿cómo deciden qué plantas usar? Diseño gráfico: habilidades, jerarquía visual y presentar a públicos; contexto, taller independiente; pregunta: ¿cómo comprueban que un cartel se lee? Arquitectura: habilidades, dibujar a escala e investigar materiales; contexto, oficina de arquitectura; pregunta: ¿cómo trabajan con otros oficios?",
        ["relaciona habilidades con campos", "nombra contextos distintos", "formula preguntas respetuosas y concretas"],
        ["hoja con tres campos, habilidades, contextos y preguntas"],
        ["usar estereotipos de género", "inventar datos de sueldos", "no relacionar con el curso"],
        "Pregunta: «¿qué habilidad del curso usas ahí?». Si no puede responder, pídele volver a la lista."),
    reinforce="Pregunta a una persona de tu casa o barrio qué hace en su trabajo y anota dos habilidades que usa y una que también practicaste en este curso.",
    extend="Explica por qué una persona puede trabajar en dos campos distintos usando las mismas habilidades.",
)

# ============================================================ OAC-07, clase 2
F = ("Ficha 31 (investigación de ejemplo, inventada). Una estudiante investiga el campo «paisajismo» con cuatro fuentes. "
     "Fuente 1: entrevista a una paisajista adulta, hecha con su permiso y sin pedir datos personales. "
     "Fuente 2: sitio de una institución de educación superior que describe una carrera de paisajismo con duración de 8 semestres, de 18 semanas cada uno (dato de ejemplo). "
     "Fuente 3: un comentario anónimo en una red social que dice «ganan una fortuna». "
     "Fuente 4: una ficha de una guía de orientación de un organismo público, con fecha y autoría (de ejemplo).")
build(
    O7, 2, F,
    use="Aprenderé a investigar un campo o una ocupación con fuentes confiables, a separar datos de opiniones y a registrar lo que no está verificado.",
    prior=["Sé contrastar fuentes.", "Sé calcular duraciones.", "Sé cuidar los datos personales."],
    explain=[
        "Investigar un campo laboral o de estudio ayuda a decidir con información. Las preguntas guía son: qué hace una persona en ese trabajo, dónde trabaja, qué formación o estudios requiere, qué habilidades usa, qué desafíos tiene y qué relación tiene con lo aprendido en el curso. Las respuestas se buscan en fuentes distintas y se anotan con su autoría y fecha.",
        "Las fuentes más confiables son las personas que ejercen la ocupación (con su permiso), las instituciones de formación, las guías de orientación de organismos públicos y los textos especializados. Un comentario anónimo no es confiable por sí solo. Se separan los datos, que se pueden verificar (la duración de una carrera, los requisitos), de las opiniones, que expresan valoraciones («ganan una fortuna»). Las cifras de sueldos o de empleo solo se usan si tienen fuente y fecha; en este cuaderno no se dan.",
        "Una entrevista se hace con respeto: se pide permiso, se explica para qué es, no se preguntan datos privados y se agradece. Si la investigación indica que una actividad exige licencia o certificación, se anota y se consulta la normativa vigente y a una persona orientadora, sin suponer detalles. La ficha de esta clase es inventada.",
    ],
    vocab=[("fuente confiable", "fuente con autoría, fecha y datos verificables"), ("dato", "información que se puede verificar"), ("opinión", "valoración personal que no se puede verificar"), ("pregunta guía", "pregunta que orienta la investigación"), ("verificar", "comprobar un dato con otra fuente")],
    worked=[
        ("Calcular una duración", "Con la ficha, ¿cuántas semanas de clases suman 2 semestres de 18 semanas cada uno?", ["Se multiplican los semestres por las semanas de cada uno.", "2 × 18 = 36."], "36 semanas"),
        ("Separar dato y opinión", "¿«Ganan una fortuna» es un dato o una opinión?", ["No se puede verificar y no tiene fuente.", "Es una opinión."], "Una opinión"),
    ],
    mistakes=[("Usar una cifra de un comentario anónimo como si fuera un dato.", "No tiene autoría ni fecha, así que no se puede verificar.", "Busca una fuente confiable con fecha, o anótala como no verificada."),
              ("Preguntar en una entrevista por la vida privada de la persona.", "No es necesario y puede incomodar.", "Pregunta por su trabajo, su formación y sus desafíos.")],
    T=[
        ('abc', '¿Qué preguntas guían la investigación de un campo laboral?', 'Qué hace, dónde trabaja, qué formación requiere, qué habilidades usa y qué desafíos tiene', 'Cuánto dinero tiene la persona y dónde vive actualmente', 'Si a mi familia le gusta o no esa ocupación y qué opinan sus vecinos', 'Las preguntas guía se centran en el trabajo y la formación.'),
        ('abc', '{F} ¿Cuál fuente es una entrevista a una persona que ejerce la ocupación?', 'La fuente 1', 'La fuente 3', 'La fuente 4', 'La ficha describe la entrevista a una paisajista en la fuente 1.'),
        ('abc', '{F} ¿Cuál fuente tiene menos confiabilidad?', 'La fuente 3, el comentario anónimo', 'La fuente 2, el sitio institucional', 'La fuente 4, la guía con fecha y autoría', 'Un comentario anónimo no tiene autoría ni datos verificables.'),
        ('=', '{F} ¿Cuántos años son 8 semestres (2 semestres por año)?', '8//2', 'Se divide el número de semestres entre 2.', ' años'),
        ('=', '{F} ¿Cuántas semanas de clases suman 8 semestres de 18 semanas cada uno?', '8*18', 'Se multiplica el número de semestres por las semanas de cada uno.', ' semanas'),
        ('abc', '{F} ¿Qué se hace con la cifra de la fuente 3?', 'No usarla como dato; buscar una fuente con autoría y fecha que la respalde, o descartarla', 'Usarla como dato central de la ficha, citando que viene de una red social', 'Compartirla con el curso como verdad, porque muchas personas la repiten', 'Una cifra sin fuente no es confiable.'),
        ('abc', '{F} ¿Por qué conviene contrastar la fuente 1 con la fuente 2?', 'Porque una entrega experiencia práctica y la otra informa los estudios: juntas dan una imagen más completa', 'Porque deben decir exactamente lo mismo; si no, una de las dos está equivocada', 'Porque una de las dos sobra y basta con quedarse con la más larga', 'Cada fuente aporta información distinta y complementaria.'),
        ('abc', 'Antes de una entrevista a una persona que trabaja en diseño, ¿qué corresponde?', 'Pedir permiso, explicar para qué es, no preguntar datos privados y agradecer', 'Grabarla sin avisar para no olvidar nada de lo que diga', 'Preguntarle cuánto gana y dónde vive para entender su situación', 'Una entrevista respetuosa cuida la privacidad.'),
        ('abc', '{F} Un compañero anota «paisajismo: sueldo alto» sin ninguna fuente. ¿Qué corresponde?', 'Pedir fuente y fecha, y anotarlo como no verificado mientras no la tenga', 'Aceptarlo, porque suena probable y es una idea muy extendida', 'Cambiarlo por una cifra aproximada que parezca razonable', 'Sin fuente ni fecha, una afirmación no verificada se rotula como tal.'),
        ('abc', '{F} ¿Qué diferencia un dato de una opinión?', 'Un dato se puede verificar, como la duración de una carrera; una opinión valora, como «ganan una fortuna»', 'No hay diferencia, porque toda información que se lee en una fuente es un dato', 'Un dato siempre es una cifra y una opinión siempre es un texto largo', 'Lo verificable es dato; lo valorativo es opinión.'),
        ('abc', '{F} Dos instituciones dicen 8 y 10 semestres para una carrera parecida. ¿Qué es correcto?', 'La duración puede variar según la institución; se anotan ambas con su fuente y se comparan', 'Una de las dos miente, porque una carrera parecida debe durar lo mismo', 'Se promedian y se anota 9 semestres como dato, sin indicar la fuente', 'Los planes de estudio varían entre instituciones.'),
        ('abc', '{F} ¿Cuál es una ficha de investigación completa?', 'Ocupación, qué hace, dónde trabaja, formación con fuente y fecha, habilidades del curso relacionadas, dos fuentes contrastadas y lo pendiente', 'Solo el nombre de la ocupación, qué hace y cuánto se dice que se gana', 'Solo una frase que dice si es un buen trabajo o no, y una opinión de la familia', 'Reúne datos, fuentes, relación con el curso y pendientes.'),
        ('abc', 'La investigación sugiere que una actividad requiere licencia o certificación. ¿Qué corresponde?', 'Anotarlo y consultar la normativa vigente y a una persona orientadora, sin suponer detalles', 'Suponer los requisitos según lo que se sabe de otras ocupaciones parecidas', 'Ignorarlo, porque los requisitos se explican después de elegir el campo', 'Los requisitos se consultan en fuentes vigentes y no se suponen.'),
    ],
    ctx=('abc', 'Una estudiante anota: «Paisajismo, carrera de 8 semestres según la institución (fuente 2, dato de ejemplo); según la paisajista entrevistada (fuente 1), trabaja en una municipalidad. Sueldos: no verificado». ¿Qué hace bien?', 'Distingue datos de fuentes y marca lo no verificado', 'Inventa una cifra de sueldo', 'Usa solo una opinión anónima', 'El registro cita fuentes y declara lo que falta.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué es una fuente confiable?", "Una fuente con autoría, fecha y datos verificables", "Permite comprobar lo que dice la información."),
        ("¿Qué se hace con una cifra sin fuente?", "Se anota como no verificada o se descarta", "Nadie puede comprobar su origen ni su fecha."),
        ("¿Qué se evita en una entrevista?", "Preguntar por datos privados de la persona", "La entrevista se centra en su trabajo y formación."),
    ],
    op=("Elige un campo de la ficha 30 (por ejemplo, diseño industrial, diseño de interiores o conservación del patrimonio). Escribe cinco preguntas guía, tres tipos de fuentes confiables donde buscarías las respuestas (inventa sus nombres genéricos, como «guía de orientación de un organismo público») y una regla para registrar lo no verificado.",
        "Campo: diseño industrial. Preguntas: ¿qué hace una persona que diseña objetos?, ¿dónde trabaja?, ¿qué formación requiere?, ¿qué habilidades usa?, ¿qué desafíos tiene? Fuentes: entrevista con una persona del oficio con permiso, sitio de una institución de formación y guía de orientación de un organismo público. Regla: todo dato sin fuente y fecha se anota como no verificado.",
        ["formula cinco preguntas guía", "elige fuentes confiables", "define cómo registrar lo no verificado"],
        ["hoja con preguntas, fuentes y regla de registro"],
        ["usar fuentes anónimas", "preguntar por datos privados", "inventar cifras"],
        "Pregunta: «¿de dónde saldrá cada respuesta?». Si no hay fuente, pídele agregarla."),
    reinforce="Elige una ocupación que te interese y escribe tres preguntas guía y una fuente confiable donde buscarías la respuesta.",
    extend="Explica por qué contrastar dos fuentes ayuda a decidir mejor sobre qué estudiar.",
)

# ============================================================ OAC-07, clase 3
F = ("Ficha 32 (habilidades y contextos de ejemplo, inventados). Habilidades del curso: H1 leer encargos y necesidades; H2 dibujar y medir a escala; H3 investigar materiales; H4 presentar a públicos; H5 evaluar con evidencia. "
     "Contextos: C1 oficina de arquitectura que diseña viviendas accesibles; C2 taller de mobiliario con materiales reciclados; C3 municipalidad que mejora plazas con participación de vecinos; C4 desarrollo personal: organizar un emprendimiento escolar de objetos reutilizados. "
     "Matriz de una estudiante (0 = no se usa, 3 = se usa mucho). C1: H1 3, H2 3, H3 2, H4 2, H5 1. C2: H1 2, H2 2, H3 3, H4 1, H5 2. C3: H1 3, H2 1, H3 1, H4 3, H5 2. C4: H1 2, H2 1, H3 2, H4 2, H5 3.")
build(
    O7, 3, F,
    use="Aprenderé a relacionar las habilidades de la asignatura con contextos laborales y de desarrollo personal mediante una matriz, y a leerla sin convertirla en una sentencia.",
    prior=["Sé investigar un campo con fuentes.", "Sé sumar filas y columnas de una tabla.", "Sé distinguir interés de obligación."],
    explain=[
        "Una matriz de habilidades y contextos es una tabla que muestra cuánto se usa cada habilidad en cada contexto, por ejemplo con un puntaje de 0 (no se usa) a 3 (se usa mucho). Los puntajes salen de la investigación: entrevistas, descripciones de cargos, observación. Sumar por filas dice qué contexto usa más habilidades; sumar por columnas dice qué habilidades son más transversales, es decir, útiles en muchos contextos.",
        "La matriz orienta, pero no decide. Una persona elige un camino considerando también sus intereses, valores, condiciones y más información; los contextos no son excluyentes y una persona puede cambiar de rumbo. Para practicar una habilidad que un contexto usa mucho se puede buscar oportunidades en el liceo, como un taller, un voluntariado o un proyecto de curso.",
        "Los contextos de desarrollo personal también cuentan: organizar un emprendimiento escolar, ayudar a mejorar una plaza o preparar un portafolio. Se cuida no presionar a nadie a elegir una opción y no compartir datos privados. Los datos de esta clase son inventados.",
    ],
    vocab=[("matriz", "tabla que cruza filas y columnas"), ("habilidad transversal", "habilidad útil en muchos contextos"), ("contexto", "lugar y forma de trabajar o aplicar lo aprendido"), ("emprendimiento", "proyecto propio para ofrecer algo útil"), ("orientar", "ayudar a explorar sin decidir por la persona")],
    worked=[
        ("Sumar una fila", "¿Cuántos puntos suma el contexto C3?", ["Los puntajes de C3 son 3, 1, 1, 3 y 2.", "3 + 1 + 1 + 3 + 2 = 10."], "10 puntos"),
        ("Sumar una columna", "¿Cuántos puntos suma la habilidad H3 en los cuatro contextos?", ["Los puntajes de H3 son 2, 3, 1 y 2.", "2 + 3 + 1 + 2 = 8."], "8 puntos"),
    ],
    mistakes=[("Elegir un contexto solo porque su total es el más alto.", "Los totales dependen de cómo se puntuó y no consideran intereses ni condiciones.", "Usa la matriz para explorar y conversa con una persona orientadora."),
              ("Dar por seguro un puntaje sin fuente.", "Puede reflejar una suposición y no la realidad del contexto.", "Respalda cada puntaje con una entrevista, una descripción o una observación.")],
    T=[
        ('abc', '¿Qué muestra una matriz de habilidades y contextos?', 'Cuánto se usa cada habilidad en cada contexto', 'Cuánto cuesta estudiar para cada contexto', 'Qué profesión debe estudiar cada persona según sus puntajes', 'La matriz cruza habilidades y contextos con un puntaje de uso.'),
        ('=', '{F} ¿Cuántos puntos suma el contexto C1?', '3+3+2+2+1', 'Se suman los cinco puntajes de C1.', ' puntos'),
        ('=', '{F} ¿Cuántos puntos suma el contexto C2?', '2+2+3+1+2', 'Se suman los cinco puntajes de C2.', ' puntos'),
        ('=', '{F} ¿Cuántos puntos suma la habilidad H1 en los cuatro contextos?', '3+2+3+2', 'Se suman los puntajes de H1 en cada contexto.', ' puntos'),
        ('abc', '{F} ¿Qué habilidad se usa más en total?', 'H1, leer encargos y necesidades, que suma 10 puntos', 'H2, dibujar y medir a escala, que suma 7 puntos', 'H5, evaluar con evidencia, que suma 8 puntos', 'Los totales son H1 = 10, H2 = 7, H3 = 8, H4 = 8 y H5 = 8.'),
        ('abc', '{F} ¿Qué habilidad se usa menos en total?', 'H2, dibujar y medir a escala, que suma 7 puntos', 'H1, leer encargos y necesidades, que suma 10 puntos', 'H4, presentar a públicos, que suma 8 puntos', 'Con 7 puntos, H2 tiene el menor total.'),
        ('abc', '{F} ¿Qué contexto usa más intensamente la habilidad H4, presentar a públicos?', 'C3, la municipalidad que mejora plazas con participación de vecinos', 'C1, la oficina de arquitectura que diseña viviendas accesibles', 'C2, el taller de mobiliario con materiales reciclados', 'C3 tiene puntaje 3 en H4 y los otros tienen 2 o 1.'),
        ('=', '{F} ¿Cuántos puntos suma toda la matriz (los cuatro contextos)?', '11+10+10+10', 'Se suman los totales de los cuatro contextos.', ' puntos'),
        ('abc', '{F} A una estudiante le gusta evaluar con evidencia. ¿Qué contexto de la matriz le ofrece más práctica en esa habilidad?', 'C4, el emprendimiento escolar, con puntaje 3 en H5', 'C1, la oficina de arquitectura, con puntaje 1 en H5', 'C3, la municipalidad, con puntaje 2 en H5', 'C4 tiene el puntaje más alto en H5.'),
        ('abc', '{F} Alguien dice: «la matriz demuestra qué profesión debo estudiar». ¿Qué respuesta es mejor?', 'La matriz orienta una exploración, pero la decisión también considera intereses, valores y condiciones', 'Tiene razón: la matriz suma puntos y la profesión con más puntos es la que corresponde', 'La matriz no sirve, porque ninguna tabla puede decir algo útil sobre el futuro', 'Una matriz es un apoyo para explorar y no una sentencia.'),
        ('abc', '{F} ¿Qué conclusión es válida sobre la habilidad H2?', 'Se usa mucho en la oficina de arquitectura (3) y menos en los otros contextos (1 o 2): conviene practicarla si interesa ese campo', 'Se usa igual en todos los contextos, porque suma lo mismo en cada uno', 'No sirve en ningún contexto, porque su total es el más bajo', 'La columna de H2 es alta solo en C1.'),
        ('abc', '{F} ¿Qué decisión orientadora es más sólida?', 'Explorar C1 y C3 con visitas o entrevistas, porque usan mucho H1, H2 y H4, y luego comparar con otros contextos', 'Elegir C4 porque tiene el puntaje más alto en H5, sin explorar más', 'No explorar nada y esperar a que el contexto ideal aparezca solo', 'Combina la matriz con exploración y comparación.'),
        ('abc', '¿Qué cuidado se toma al hablar de contextos de desarrollo personal?', 'No exponer datos privados ni presionar a nadie a elegir un camino', 'Obligar a todas las personas a elegir el mismo contexto para comparar', 'Ocultar las preguntas y respuestas de las demás personas del curso', 'El respeto a la privacidad y a la libertad de elegir es esencial.'),
    ],
    ctx=('abc', 'Una estudiante escribe: «Mi matriz dice que C3 usa mucho presentar a públicos. Voy a pedir ayuda a mi orientadora para entrevistar a alguien de una municipalidad y verificar mis puntajes». ¿Qué hace bien?', 'Usa la matriz para explorar y busca verificar con una fuente', 'Decide su carrera solo con el total', 'Ignora la matriz', 'La matriz se contrasta con una entrevista, no se toma como verdad.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué es una habilidad transversal?", "Una habilidad útil en muchos contextos", "Se reconoce porque su columna suma alto."),
        ("¿Qué hace la suma de una fila de la matriz?", "Muestra cuántas habilidades usa un contexto en total", "Permite comparar contextos entre sí con un mismo número."),
        ("¿La matriz decide qué estudiar?", "No: orienta, y la decisión considera más cosas", "Intereses, valores y condiciones también cuentan."),
    ],
    op=("Elige dos contextos de la ficha 32 y suma sus puntajes. Escribe una conclusión sobre cuál usa más habilidades, otra sobre una habilidad que se usa mucho en uno de ellos, y una acción para practicar esa habilidad este año en el liceo (por ejemplo, un proyecto de curso o un voluntariado) y verificarla con una persona que trabaje en ese contexto.",
        "Contextos: C2 (10 puntos) y C3 (10 puntos): usan igual cantidad de habilidades. En C3, H4 (presentar a públicos) tiene puntaje 3. Acción: organizar una presentación de un proyecto del curso ante vecinos del liceo, y entrevistar a una persona de una municipalidad para verificar cuánto presenta a públicos.",
        ["suma correctamente", "formula conclusiones con datos", "propone una acción y una verificación"],
        ["hoja con sumas, conclusiones y acción"],
        ["decidir solo por el total", "no verificar los puntajes", "proponer acciones riesgosas"],
        "Pregunta: «¿cómo comprobarías este puntaje?». Si no responde, pídele pensar en una fuente."),
    reinforce="Haz una matriz de dos contextos y tres habilidades de tu vida diaria, con puntajes de 0 a 3, y suma cada columna.",
    extend="Explica por qué una habilidad transversal es una buena inversión de práctica.",
)

# ============================================================ OAC-07, clase 4
F = ("Ficha 33 (plan de ejemplo de una estudiante ficticia). Meta: probar durante el último año del liceo si le interesa un campo de diseño o arquitectura. "
     "Acciones por semana: 2 horas de dibujo técnico a mano, 1 hora de lectura de fichas de carreras y 3 horas para armar su portafolio. "
     "Acción mensual: una entrevista de 1 hora con una persona profesional, con permiso. "
     "Portafolio: 4 proyectos del curso, cada uno con bitácora, un panel y una evaluación crítica. "
     "Fuentes: persona orientadora del liceo, sitios de instituciones de educación superior y la entrevista. "
     "Semanas de trabajo hasta fin de año: 20, con 5 entrevistas.")
build(
    O7, 4, F,
    use="Aprenderé a elaborar un plan de desarrollo personal propio con meta, acciones, tiempos y un portafolio, relacionando lo aprendido en el curso con rutas de formación y trabajo.",
    prior=["Sé investigar con fuentes.", "Sé leer una matriz de habilidades.", "Sé calcular horas."],
    explain=[
        "Un plan de desarrollo personal parte de una meta realista y la divide en acciones con tiempos: qué haré cada semana o cada mes, con qué recursos, y cómo sabré que avanzo (indicadores). Se incluye una revisión a mitad de camino para ajustar. El ritmo debe ser realista y dejar descanso: un plan sobrecargado se abandona.",
        "El portafolio es una selección de trabajos que muestra qué se hizo y cómo se pensó. Un portafolio de diseño y arquitectura incluye proyectos con su bitácora, paneles de presentación, evaluaciones críticas y las versiones sucesivas. Muestra habilidades de aprendizaje y no reemplaza la formación: proyectar o calcular obras reales exige formación y habilitación según la normativa vigente.",
        "Las rutas de formación posibles incluyen estudios técnicos o profesionales en educación superior, formación en oficios, certificaciones y aprendizaje continuo. Los requisitos, costos y ayudas cambian: se consultan en fuentes oficiales vigentes y con una persona orientadora. Si algo te preocupa o te sobrecarga, conversa con una persona adulta de confianza. El plan de esta clase es inventado.",
    ],
    vocab=[("plan de desarrollo personal", "meta con acciones, tiempos, recursos e indicadores"), ("portafolio", "selección de trabajos con evidencia de proceso"), ("indicador", "dato que muestra si se avanza hacia la meta"), ("ruta de formación", "camino de estudios o capacitación hacia un campo"), ("aprendizaje continuo", "seguir aprendiendo a lo largo de la vida")],
    worked=[
        ("Sumar horas semanales", "Con la ficha, ¿cuántas horas por semana suman solo el dibujo técnico y la lectura de fichas?", ["Son 2 y 1 horas.", "2 + 1 = 3."], "3 horas"),
        ("Proyectar el total", "¿Cuántas horas de dibujo técnico suma la estudiante en 20 semanas?", ["Se multiplican las 2 horas semanales por las semanas.", "2 × 20 = 40."], "40 horas"),
    ],
    mistakes=[("Llenar cada día de actividades sin dejar descanso.", "Un plan sobrecargado se abandona y afecta el bienestar.", "Elige un ritmo realista y revisa a mitad de camino."),
              ("Creer que el portafolio habilita para proyectar una obra real.", "Una obra real exige formación y habilitación según la normativa vigente.", "Usa el portafolio para mostrar habilidades y consulta rutas de formación.")],
    T=[
        ('abc', '¿Qué partes tiene un plan de desarrollo personal?', 'Meta, acciones con tiempos, recursos, indicadores y revisión', 'Solo un deseo y una fecha final, sin pasos intermedios', 'Solo una lista de materiales y de personas que podrían ayudar', 'Un plan define qué, cuándo, con qué y cómo se comprueba.'),
        ('=', '{F} ¿Cuántas horas por semana suman las tres acciones semanales (2, 1 y 3 horas)?', '2+1+3', 'Se suman las horas de cada acción semanal.', ' horas'),
        ('=', '{F} ¿Cuántas horas suman esas acciones semanales en 20 semanas?', '6*20', 'Se multiplican las horas semanales por las semanas.', ' horas'),
        ('=', '{F} ¿Cuántas horas dedica al portafolio en las 20 semanas, a 3 horas por semana?', '3*20', 'Se multiplican las horas semanales de portafolio por las semanas.', ' horas'),
        ('abc', '{F} ¿Qué incluye cada proyecto del portafolio?', 'Una bitácora, un panel y una evaluación crítica', 'Una fotografía y la nota del proyecto', 'Solo el resultado final, sin bitácora ni proceso', 'La ficha lista esos tres elementos para cada proyecto.'),
        ('abc', '{F} ¿Qué indicador permite revisar el avance de la meta?', 'Cuántas horas de dibujo y cuántos proyectos del portafolio se completaron cada mes', 'Cuánto le gusta a su familia el plan y cuánto la apoyan', 'El precio de las herramientas y los materiales que compra', 'Un indicador es un dato medible de avance.'),
        ('abc', '{F} ¿Qué fuentes de la ficha sirven para consultar rutas de estudio y requisitos vigentes?', 'La persona orientadora del liceo y los sitios de las instituciones de educación superior', 'Un comentario anónimo en una red social que habla de carreras', 'Lo que cuentan compañeros de otro curso sobre una carrera, sin fuente', 'Son fuentes con autoría que informan requisitos vigentes.'),
        ('abc', 'Al planificar los tiempos, ¿qué corresponde?', 'Elegir un ritmo realista que permita descansar y no sobrecargarse', 'Llenar todos los días con actividades, sin pausas, para avanzar más rápido', 'No planificar nada y avanzar según el ánimo de cada día', 'Un plan realista se puede sostener en el tiempo.'),
        ('abc', '{F} La estudiante descubre que armar el portafolio toma más horas de lo previsto. ¿Qué es mejor?', 'Ajustar el plan: reducir otra acción o ampliar el plazo, y registrar el cambio', 'Abandonar el plan, porque ya no se cumplió lo previsto', 'Ocultar el problema y mantener el plan original sin cambios', 'Ajustar con registro mantiene el plan viable.'),
        ('abc', '¿Por qué incluir la evaluación crítica de cada proyecto en el portafolio?', 'Porque muestra cómo se piensa y se mejora, no solo el resultado final', 'Porque ocupa más páginas y el portafolio se ve más completo', 'Porque reemplaza el proyecto cuando este quedó incompleto', 'La evaluación muestra el aprendizaje del proceso.'),
        ('abc', '{F} Alguien dice: «con este portafolio ya puedo diseñar y calcular un edificio real». ¿Qué respuesta es mejor?', 'El portafolio muestra habilidades de aprendizaje; proyectar y calcular un edificio real exige formación y habilitación', 'Tiene razón: un portafolio con varios proyectos bien evaluados es suficiente para proyectar obras reales', 'El portafolio no sirve para nada, porque solo la formación formal tiene valor', 'Una obra real requiere formación y habilitación profesional.'),
        ('abc', '{F} ¿Cuál es un plan de desarrollo personal completo?', 'Meta, acciones con horas semanales, fuentes, indicadores mensuales, revisión a mitad de año y apoyo de una persona orientadora', 'Una lista de deseos con las carreras que se quiere estudiar, sin tiempos', 'Un plan muy ambicioso que ocupa todas las horas del día para no perder tiempo', 'Incluye meta, acciones, fuentes, indicadores, revisión y apoyo.'),
        ('abc', '¿Qué rutas de formación puede explorar una persona interesada en diseño y arquitectura?', 'Estudios técnicos o profesionales, formación en oficios y certificaciones; los requisitos vigentes se consultan a orientación', 'Una sola ruta fija para todas las personas, definida por el campo elegido', 'Ninguna, porque el diseño y la arquitectura se aprenden solo de forma autodidacta', 'Hay varias rutas, cuyos requisitos cambian y se consultan.'),
    ],
    ctx=('abc', 'Una estudiante escribe: «Meta: probar si me interesa el paisajismo. Cada semana, 2 horas de dibujo y 3 de portafolio (5 horas); cada mes, una entrevista de 1 hora. Indicador: un proyecto terminado cada dos meses. Revisión: en el mes 3». ¿Qué hace bien?', 'Define meta, tiempos, indicador y revisión realistas', 'No dice cuándo revisará', 'Planea 40 horas semanales sin descanso', 'El plan es medible, realista y revisable.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué es un portafolio?", "Una selección de trabajos con evidencia de proceso y evaluación", "Muestra cómo se piensa y se mejora."),
        ("¿Qué es un indicador?", "Un dato medible que muestra si se avanza hacia la meta", "Permite revisar el plan a mitad de camino."),
        ("¿Dónde se consultan los requisitos de formación vigentes?", "En fuentes oficiales y con una persona orientadora", "Los requisitos y costos cambian con el tiempo."),
    ],
    op=("Escribe tu propio plan de desarrollo personal de un mes (o inventa uno de ejemplo) para explorar un campo de diseño o arquitectura. Incluye una meta, tres acciones con horas por semana (que sumen no más de 6 horas), una entrevista con permiso, una fuente para consultar rutas de formación, un indicador y la fecha de revisión. Calcula las horas del mes con 4 semanas.",
        "Meta: conocer cómo se trabaja en diseño de interiores. Acciones: 2 horas de dibujo a escala, 1 hora de lectura de fichas de carreras y 2 horas de portafolio por semana: 5 horas semanales, 20 horas en 4 semanas. Entrevista: una vez en el mes, 1 hora, con permiso. Fuente: persona orientadora del liceo. Indicador: dos láminas terminadas. Revisión: al final de la semana 2.",
        ["incluye meta, acciones, tiempos e indicador", "calcula bien las horas", "propone una revisión y una fuente confiable"],
        ["hoja con plan, horas y revisión"],
        ["sobrecargar el plan", "no definir indicadores", "usar fuentes no confiables"],
        "Pregunta: «¿cómo sabrás que avanzas?». Si no tiene indicador, pídele agregar uno."),
    reinforce="Escribe una meta pequeña para esta semana relacionada con diseño o arquitectura, una acción de 30 minutos y cómo comprobarás que la hiciste.",
    extend="Explica por qué es mejor un plan pequeño que se cumple que uno enorme que se abandona.",
)

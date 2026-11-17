"""Interpretación musical 3.º y 4.º medio HC: OAC-02 (proyectos de interpretación: intereses, investigación, estilo y referentes, ensamble, bitácora y atribución). Referentes y piezas inventados."""
from __future__ import annotations

from hc_imus_common import CLAVE, build

O2 = "AR-IMUS-3y4-OAC-02"

# ============================================================ OAC-02, clase 1
F = ("Ficha 1 (referentes de ejemplo, todos inventados; los intérpretes reales los aporta tu docente). "
     "Referente 1, «Trío Aguacero» (ficticio, nacional): voz, guitarra y cajón; 72 pulsos por minuto; voz cálida y cercana; guitarra rasgueada; forma de estrofa y estribillo; fuerza casi siempre entre p y mf. "
     "Referente 2, «Cuarteto Ventana» (ficticio, internacional): dos violines, viola y chelo; 120 pulsos por minuto; articulación picada; forma con muchas repeticiones y cambios de fuerza; sin voz. "
     "Referente 3, «Colectivo Marea» (ficticio, mixto): voces y sonidos electrónicos; 60 pulsos por minuto; sonidos largos y ligados; crescendos muy amplios; forma libre.")
build(
    O2, 1, F,
    use="Aprenderé a reconocer rasgos de estilo en referentes de la interpretación vocal e instrumental y a relacionarlos con un interés personal o grupal, para empezar un proyecto de interpretación con ideas claras.",
    prior=["Reconozco fraseo, ritmo, dinámica y articulación.", "Sé comparar dos casos con evidencia.", "Sé que mi voz y mis manos necesitan descanso."],
    explain=[
        "Un proyecto de interpretación musical es un trabajo planificado que lleva una idea hasta una interpretación, sola o en grupo. Parte de un interés personal o grupal: lo que quiero comunicar, el tipo de música que me mueve o el reto técnico que quiero abordar. Un buen interés se escribe en una frase concreta, por ejemplo «una canción íntima para acompañar un momento de calma».",
        "Para darle forma al interés se estudian referentes, es decir, intérpretes o agrupaciones, nacionales o internacionales, cuyo modo de tocar o cantar sirve de modelo. De cada referente se anotan rasgos de estilo: instrumentación, tempo, articulación, dinámica, forma y carácter de la voz. Conocer un estilo no es copiarlo: es entender qué decisiones lo definen para después elegir cuáles tomar, cuáles cambiar y cuáles dejar.",
        "Los referentes reales los propone tu docente, con atribución clara del nombre y la obra. Aquí se usan ejemplos inventados para practicar el método: se leen los rasgos en una ficha, se comparan con evidencia y se elige qué rasgos se relacionan con el interés del proyecto. Se trabaja siempre con volumen moderado y con pausas, y se respeta el trabajo de las personas que sirven de referente.",
    ],
    vocab=[("proyecto de interpretación", "trabajo planificado que lleva una idea hasta una ejecución"), ("referente", "intérprete o agrupación cuyo modo de tocar sirve de modelo"),
           ("rasgo de estilo", "característica que se repite en un intérprete o tradición"), ("instrumentación", "conjunto de instrumentos y voces que participan"),
           ("tempo", "velocidad del pulso, en pulsos por minuto"), ("interés", "lo que una persona o un grupo quiere comunicar o aprender")],
    worked=[
        ("Reconocer rasgos", "Un conjunto de ejemplo toca a 144 pulsos por minuto, con violines y chelo, golpes cortos y sin voz. ¿Cuáles son su tempo, su instrumentación y su articulación?",
         ["El tempo está dicho: 144 pulsos por minuto. La instrumentación son violines y chelo, sin voz.", "La articulación son golpes cortos, es decir, picada."],
         "Tempo de 144 pulsos por minuto; violines y chelo sin voz; articulación picada"),
        ("Relacionar interés y referente", "Una estudiante quiere interpretar una pieza «cálida y cercana para una sala pequeña». Un referente de ejemplo canta con voz suave, guitarra rasgueada y dinámica entre p y mf. ¿Le sirve?",
         ["El interés pide calidez y cercanía; el referente tiene voz suave y fuerza baja a media, dos rasgos que apoyan ese interés.", "Le sirve como inspiración, y puede tomar esos rasgos sin copiar una pieza."],
         "Sí: la voz suave y la dinámica entre p y mf apoyan el interés"),
    ],
    mistakes=[("Creer que seguir un estilo es copiar nota por nota una obra.", "Se confunde estilo con una pieza concreta.", "Un estilo es un conjunto de rasgos; se pueden tomar algunos y componer algo nuevo."),
              ("Decir «me gusta ese conjunto» sin nombrar ningún rasgo.", "El gusto no sirve para decidir qué tomar.", "Nombra un rasgo concreto (tempo, articulación, instrumentación) y su efecto.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es un rasgo de estilo?', 'Una característica que se repite en un intérprete, como el tempo o la articulación', 'Un adorno que se añade al final de la pieza para recibir más aplausos del público presente', 'La cantidad de público que asiste a las presentaciones de un grupo durante el año', 'Los rasgos de estilo son características musicales que se repiten; no son adornos ni cifras de público.'),
        ('abc', '{F} ¿Qué referente toca con articulación picada?', 'Cuarteto Ventana', 'Trío Aguacero', 'Colectivo Marea', 'La ficha asigna la articulación picada solo al Cuarteto Ventana.'),
        ('abc', '{F} ¿Qué instrumentos tiene el Trío Aguacero?', 'Voz, guitarra y cajón', 'Violines, viola y chelo', 'Voces y sonidos electrónicos', 'Los otros dos conjuntos tienen instrumentación distinta según la ficha.'),
        ('abc', '{F} ¿Cuál referente tiene el tempo más lento?', 'Colectivo Marea, con 60 pulsos por minuto', 'Trío Aguacero, con 72 pulsos por minuto', 'Cuarteto Ventana, con 120 pulsos por minuto', 'Entre 60, 72 y 120 pulsos por minuto, el más lento es 60.'),
        ('=', '{F} ¿Cuántos segundos duran 18 pulsos en el tempo del Trío Aguacero?', '18*60//72', 'Los segundos se obtienen multiplicando los pulsos por 60 y dividiendo por los pulsos por minuto.', ' s'),
        ('abc', '{F} Un grupo quiere una canción íntima para una sala pequeña. ¿Qué referente le sirve más de inspiración?', 'Trío Aguacero, por su voz cálida y su fuerza baja', 'Cuarteto Ventana, por su tempo rápido y sus golpes cortos', 'Colectivo Marea, por sus crescendos amplios y su forma libre', 'La intimidad se apoya en voz cálida y fuerza entre p y mf, que son rasgos del Trío Aguacero.'),
        ('abc', '{F} Una estudiante quiere un proyecto enérgico sin voz. ¿Qué rasgos tomaría del Cuarteto Ventana?', 'El tempo rápido y la articulación picada', 'La forma libre y los sonidos largos', 'La voz cálida y la guitarra rasgueada', 'La energía se apoya en el tempo de 120 y en la articulación picada, rasgos del cuarteto.'),
        ('=', '{F} Un compás de 4 pulsos del Cuarteto Ventana se toca 8 veces seguidas. ¿Cuántos segundos dura esa repetición?', '8*4*60//120', 'Se multiplican las 8 repeticiones por 4 pulsos y se pasa a segundos con el tempo dado.', ' s'),
        ('abc', '{F} Un grupo toma el estilo del Trío Aguacero, pero lo toca en f, picado y a 120 pulsos por minuto. ¿Qué pasa con el estilo?', 'Se aleja del referente, porque cambia varios de sus rasgos', 'Se mantiene igual al referente, porque la instrumentación no cambió en nada', 'Se vuelve idéntico al del Cuarteto Ventana, porque comparte el tempo rápido', 'Cambiar fuerza, articulación y tempo aleja la interpretación del estilo del trío aunque se conserve la instrumentación.'),
        ('abc', 'Un grupo copia nota por nota una pieza de un referente y la presenta como propia. Otro toma su tempo y su forma y compone una pieza nueva. ¿Cuál hace un proyecto con decisiones propias?', 'El segundo, que toma rasgos y hace algo nuevo', 'El primero, que copia con exactitud todos los sonidos', 'Los dos, porque ambos usan un referente como punto de partida', 'Un proyecto propio decide qué rasgos tomar y construye algo nuevo; copiar y atribuirlo como propio no lo es.'),
        ('abc', '{F} Ana quiere un proyecto que calme al público antes de una prueba. ¿Qué rasgos del Colectivo Marea la apoyan?', 'El tempo de 60 pulsos por minuto y los sonidos largos y ligados', 'La articulación picada y los cambios rápidos de fuerza en cada compás', 'La guitarra rasgueada y el estribillo que se repite en cada estrofa', 'La calma se apoya en un pulso lento y sonidos largos y unidos, rasgos de Marea.'),
        ('abc', '{F} Ema quiere ritmo enérgico y Hugo quiere voz cálida. ¿Qué decisión integra ambos intereses?', 'Una pieza con voz cálida sobre un acompañamiento rítmico y picado', 'Una pieza lenta y sin voz, para que nadie quede disconforme con el resultado', 'Dos piezas separadas, cada una hecha por una persona sola, sin juntarlas nunca', 'Se integran tomando un rasgo de cada interés en una misma pieza: la voz cálida y el ritmo picado.'),
        ('abc', '{F} ¿Cuál de estas comparaciones usa evidencia?', 'Ventana toca a 120 pulsos por minuto y Marea a 60, así que Ventana es más rápida', 'Ventana es mejor que Marea porque suena más moderna y todos la prefieren hoy', 'Marea es más difícil porque todos dicen que es especial y diferente a las demás', 'Una comparación con evidencia cita datos comprobables, como el tempo de cada ficha.'),
    ],
    ctx=('=', 'Tu grupo investiga los referentes de la ficha y quiere escuchar de cada uno un fragmento de 3 minutos. Con tres referentes y 2 minutos de pausa de silencio entre cada fragmento (2 pausas), ¿cuántos minutos dura la sesión de escucha?', '3*3+2*2', 'Se suman los tres fragmentos de 3 minutos y las dos pausas de 2 minutos entre ellos.', ' minutos'),
    sc=[
        ("En Interpretación musical: ¿qué es un referente?", "Un intérprete o agrupación cuyo modo de tocar sirve de modelo", "El referente inspira decisiones, pero no se copia."),
        ('abc', 'Un buen interés para un proyecto es:', 'Una frase concreta sobre lo que se quiere comunicar', 'Una lista de todos los estilos musicales que existen en el mundo', 'La obra de otra persona copiada igual, sin cambiar ningún rasgo', 'Un interés concreto guía las decisiones del proyecto.'),
        ("¿Por qué se anotan rasgos de estilo y no solo gustos?", "Porque los rasgos se pueden comprobar y servir para decidir qué tomar", "Un rasgo como el tempo es verificable; un gusto no lo es."),
    ],
    op=("Con la {F}, escribe en una frase tu interés para un proyecto (por ejemplo: calmar, animar, contar algo). Elige un referente de la ficha, anota dos de sus rasgos y explica cuál tomarías y cuál cambiarías, y por qué.",
        "Interés: una pieza que anime a mi curso antes de un partido. Referente: Cuarteto Ventana. Rasgos: tempo de 120 pulsos por minuto y articulación picada. Tomaría el tempo y la articulación porque dan energía; cambiaría la instrumentación y usaría voz y percusión de mesa porque es lo que tengo disponible.",
        ["escribe un interés concreto", "elige un referente de la ficha y anota dos rasgos", "decide qué toma y qué cambia", "justifica con el interés"],
        ["hoja con interés, referente, dos rasgos y decisión"],
        ["elegir un referente por gusto sin relacionarlo con el interés", "copiar la pieza completa", "no cambiar ningún rasgo"],
        "Pregunta: «¿qué rasgo del referente apoya tu interés?». Si no lo nombra, pídele que lo busque en la ficha."),
    reinforce="Describe un referente imaginario con tres rasgos (instrumentación, tempo, articulación) y escribe para qué interés serviría.",
    extend="Explica con un ejemplo por qué un proyecto puede inspirarse en un referente nacional y en uno internacional a la vez.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 2 (fuentes de ejemplo para investigar el estilo de un conjunto de cuerdas ficticio, inventadas). "
     "Fuente A: entrevista de una radio local al director del conjunto; dice que el grupo toca a unos 120 pulsos por minuto y que ensaya 3 veces por semana. "
     "Fuente B: comentario anónimo en un foro; dice que el conjunto «toca siempre a toda velocidad». "
     "Fuente C: ficha del programa de un concierto, escrita por el propio conjunto; trae los nombres de sus integrantes, el tempo de cada pieza (todos entre 116 y 124 pulsos por minuto) y un texto de presentación. "
     "Pregunta de investigación: ¿a qué tempo suele tocar el conjunto y cómo se organizan sus ensayos?")
build(
    O2, 2, F,
    use="Aprenderé a investigar para un proyecto de interpretación: formular una pregunta, comparar fuentes, elegir las más confiables y registrar lo hallado con su origen.",
    prior=["Reconozco rasgos de estilo en un referente.", "Sé comparar datos con evidencia.", "Sé que una opinión no es un dato."],
    explain=[
        "Investigar para un proyecto de interpretación es buscar información que ayude a tomar decisiones: cómo se tocaba o cantaba un estilo, qué instrumentos usaba, cómo ensayaba un grupo. Se parte de una pregunta de investigación clara, que se pueda contestar con datos. «¿A qué tempo suele tocar este conjunto?» es una buena pregunta; «¿es bueno este conjunto?» es solo una opinión.",
        "No todas las fuentes valen lo mismo. Una fuente primaria viene de quien vivió o hizo lo que se estudia, como una entrevista a un integrante o el programa de un concierto. Una fuente secundaria interpreta lo que otros dijeron. Una opinión anónima es una fuente débil porque no se sabe quién habla ni en qué se apoya. Una información es más confiable si la dan al menos dos fuentes distintas que coinciden.",
        "Cada hallazgo se registra con su origen: qué dato es, de qué fuente viene, de qué tipo es y qué tan confiable parece. Así otra persona puede revisarlo y se evita pasar una opinión como si fuera un dato. En los ejemplos de este cuaderno todo está inventado; las fuentes reales las revisas con tu docente, y siempre se cita a quien las escribió, lo que se llama atribución.",
    ],
    vocab=[("pregunta de investigación", "pregunta que se puede responder con datos"), ("fuente primaria", "fuente que viene de quien vivió o hizo lo que se estudia"),
           ("fuente secundaria", "fuente que interpreta lo que otras personas dijeron"), ("confiable", "que se puede creer porque se sabe quién la escribió y en qué se apoya"),
           ("registro", "nota ordenada de un dato, su fuente y su confiabilidad"), ("contrastar", "comparar dos fuentes para ver si coinciden")],
    worked=[
        ("Elegir la pregunta", "Una estudiante duda entre «¿es genial este grupo?» y «¿cuántos integrantes tiene este grupo en escena?». ¿Cuál sirve para investigar?",
         ["La primera depende de opiniones: no se puede comprobar con un dato.", "La segunda se contesta con un número que aparece en una fuente: sirve."],
         "La segunda, porque se responde con datos"),
        ("Clasificar una fuente", "La ficha de un programa de concierto, escrita por el propio conjunto, dice cuántas piezas tocará. ¿Qué tipo de fuente es?",
         ["Quien la escribió es el propio conjunto, o sea que viene de quien hizo el concierto.", "Es una fuente primaria; para confirmarla convendría contrastarla con otra fuente."],
         "Fuente primaria"),
    ],
    mistakes=[("Copiar un dato de una opinión anónima como si fuera confiable.", "No se sabe quién lo dijo ni en qué se apoya.", "Busca otra fuente que lo confirme y registra de dónde viene cada dato."),
              ("Formular preguntas que solo piden una opinión («¿es lindo?»).", "No se pueden responder con datos.", "Formula una pregunta que un dato pueda contestar («¿a qué tempo toca?»).")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es una fuente primaria?', 'Una fuente que viene de quien vivió o hizo lo que se estudia', 'Una fuente que siempre aparece primero en una búsqueda', 'Una opinión que muchas personas repiten sin saber de dónde viene', 'La fuente primaria viene de quien hizo la actividad, como un integrante que da una entrevista.'),
        ('abc', '{F} ¿Cuál es la pregunta de investigación de la ficha?', '¿A qué tempo suele tocar el conjunto y cómo se organizan sus ensayos?', '¿Es el conjunto el mejor de todos los conjuntos que existen en el país?', '¿Cuántas personas fueron a verlo en el último concierto de la temporada?', 'La pregunta de la ficha busca un tempo y una forma de ensayar, que se responden con datos.'),
        ('abc', '{F} ¿Qué fuente es una opinión anónima?', 'La fuente B, el comentario del foro', 'La fuente A, la entrevista en la radio', 'La fuente C, la ficha del programa', 'En la fuente B no se sabe quién habla, mientras que A y C tienen autoría.'),
        ('abc', '{F} ¿Qué fuentes coinciden sobre un tempo de unos 120 pulsos por minuto?', 'La A, que dice unos 120, y la C, que trae tempos entre 116 y 124', 'La B, que dice «a toda velocidad», y la A, que dice unos 120', 'Ninguna, porque una entrevista y un programa de concierto nunca pueden coincidir', 'La fuente A da unos 120 y la C trae tempos entre 116 y 124, que son cercanos; la B no da ningún número.'),
        ('=', '{F} Según la fuente A, el grupo ensaya 3 veces por semana. ¿Cuántos ensayos hace en 4 semanas?', '3*4', 'Se multiplican los ensayos de cada semana por las cuatro semanas.', ' ensayos'),
        ('abc', '{F} ¿Qué fuente es la más débil para responder la pregunta de la ficha?', 'La B, porque es anónima y no cita ningún dato concreto', 'La A, porque es una entrevista al director del conjunto', 'La C, porque la escribieron los integrantes del grupo', 'Una opinión anónima sin datos concretos es la fuente menos confiable de las tres.'),
        ('{F} Registra en una línea la afirmación «toca siempre a toda velocidad» con su fuente, su tipo y su confiabilidad.', 'Dato: toca siempre a toda velocidad; fuente: B, comentario anónimo en un foro; tipo: opinión sin autoría; confiabilidad: baja', 'Un registro lleva el dato, su fuente, su tipo y qué tan confiable parece.'),
        ('=', '{F} Un conjunto toca una pieza de 96 pulsos a 120 pulsos por minuto. ¿Cuántos segundos dura?', '96*60//120', 'Se multiplican los pulsos por 60 y se divide por los pulsos por minuto.', ' s'),
        ('abc', '{F} Un grupo quiere confirmar el tempo del conjunto. ¿Qué paso es el más adecuado?', 'Contrastar la entrevista con el programa del concierto', 'Aceptar el comentario del foro, porque es el más reciente', 'Repetir la misma fuente tres veces para estar seguros', 'Contrastar dos fuentes distintas aumenta la confianza en un dato.'),
        ('abc', '{F} Un compañero escribe en su registro: «tocan a toda velocidad, fuente: foro». ¿Qué problema tiene?', 'Presenta una opinión anónima como si fuera un dato confiable', 'Ninguno, porque el foro tiene muchos comentarios de otras personas', 'Que no menciona la entrevista que dio el director del conjunto', 'Una opinión sin autoría no puede registrarse como dato confiable.'),
        ('abc', 'Dos preguntas para un proyecto sobre un grupo de percusión: (1) «¿qué instrumentos usa en su último concierto?»; (2) «¿es el grupo más lindo?». ¿Cuál sirve para investigar y por qué?', 'La 1, porque un dato en una fuente la puede responder', 'La 2, porque todo el mundo tiene una opinión', 'Ninguna, porque ninguna pregunta se responde con una fuente', 'Una pregunta de investigación se contesta con datos; la 2 es una opinión.'),
        ('abc', '{F} Si la fuente A y la fuente C dieran tempos distintos, ¿qué debe hacer el grupo con ese dato?', 'Registrar ambos con su fuente y buscar una tercera fuente que contraste', 'Elegir el que suene más rápido, porque dará más energía a la presentación', 'Promediar ambos datos sin saber de dónde salió cada uno de ellos', 'Cuando dos fuentes difieren se registran ambas y se busca otra que ayude a decidir.'),
        ('abc', 'Un grupo pide permiso a una persona para citar su entrevista en el programa de su proyecto, y escribe su nombre como autora. ¿Qué respeta con eso?', 'La atribución: reconoce quién dio la información', 'La velocidad de la investigación sobre el tema', 'La confiabilidad de todas las fuentes anónimas del foro', 'Citar a quien dio la información es atribuir y respetar su trabajo.'),
    ],
    ctx=('=', 'Tu grupo pide una entrevista de 15 minutos a una música de la comunidad, y quiere dedicar otros 30 minutos a ordenar los registros de lo que dijo. ¿Cuántos minutos suma todo el trabajo?', '15+30', 'Se suman los minutos de la entrevista y los de ordenar los registros.', ' minutos'),
    sc=[
        ("En Interpretación musical: ¿qué es contrastar fuentes?", "Comparar dos fuentes para ver si coinciden", "Contrastar da más confianza a un dato."),
        ('abc', 'Una opinión anónima es una fuente:', 'Débil', 'Primaria', 'Siempre confiable', 'No se sabe quién habla ni en qué se apoya.'),
        ("¿Qué datos lleva un registro de investigación?", "El dato, su fuente, su tipo y qué tan confiable parece", "Con esos datos otra persona puede revisar lo investigado."),
    ],
    op=("Con la {F}, escribe un registro de dos líneas: una con el dato sobre el tempo y otra con el dato sobre los ensayos, cada una con su fuente, su tipo y su confiabilidad. Después escribe una pregunta nueva para continuar la investigación.",
        "Línea 1: tempo de unos 120 pulsos por minuto; fuente A (entrevista); primaria; confiabilidad media, se confirma con la ficha C. Línea 2: ensayan 3 veces por semana; fuente A; primaria; confiabilidad media, falta contrastar. Pregunta nueva: ¿cuánto dura cada ensayo?",
        ["registra dos datos con fuente y tipo", "indica la confiabilidad de cada uno", "formula una pregunta que un dato pueda responder", "no usa la fuente anónima como dato"],
        ["hoja con los dos registros y la pregunta nueva"],
        ["usar la opinión anónima como dato", "olvidar la fuente", "formular una pregunta que pide opinión"],
        "Pregunta: «¿cómo sabes que ese dato es confiable?». Si no puede responder, pídele que busque una segunda fuente."),
    reinforce="Formula tres preguntas de investigación para un proyecto de interpretación y marca cuáles se responden con datos y cuáles son opiniones.",
    extend="Explica por qué una sola fuente, aunque sea primaria, no basta para afirmar algo con seguridad.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 3 (plan de proyecto de ejemplo «Ronda de invierno», inventado). Grupo de 4 integrantes: dos voces, una guitarra y percusión de mesa. "
     "Producto: una pieza original de 3 minutos para el acto de cierre del liceo. "
     "Calendario de ensayos: 5 ensayos de 45 minutos cada uno, uno por semana. "
     "Cada ensayo: calentamiento de 8 minutos, trabajo de la pieza y 5 minutos de silencio y descanso a la mitad. "
     "Roles: voz principal, segunda voz, guitarra y percusión; Lía coordina el calendario. "
     "Restricción: el acto admite como máximo 4 minutos por grupo.")
build(
    O2, 3, F,
    use="Aprenderé a planificar un proyecto de interpretación: definir producto, roles, calendario y tiempos de ensayo con calentamiento y descanso, y a decidir entre opciones usando las restricciones.",
    prior=["Sé formular un interés y reconozco rasgos de estilo.", "Sé que ensayar necesita calentamiento y pausas.", "Sé calcular duraciones a partir de minutos y pulsos."],
    explain=[
        "Planificar un proyecto significa decidir de antemano qué se va a lograr, quién hace qué y cuándo. Un plan básico tiene cuatro partes: el producto (qué se presentará y cuánto dura), los roles (quién canta, toca o coordina), el calendario (cuántos ensayos y de qué duración) y las restricciones (límites de tiempo, espacio o recursos). Escribir el plan evita decidir todo a último momento.",
        "Cada ensayo se organiza en tramos: un calentamiento suave (soltar hombros, respirar lento, cantar o tocar muy despacio), el trabajo de la pieza, una pausa de silencio y descanso, y un cierre breve con lo aprendido. El tiempo de trabajo real es lo que queda al restar calentamiento y pausas. Un plan realista cuenta ese tiempo y no los minutos totales de la sala.",
        "Un plan también se revisa. Si un ensayo se pierde o la pieza dura más de lo permitido, se ajusta un solo elemento: se acorta la pieza, se agrega un ensayo o se cambia un rol. Cada ajuste se anota con su razón. Las personas del grupo acuerdan el plan en conjunto, y cada una puede avisar si siente cansancio o dolor y pedir descanso.",
    ],
    vocab=[("producto", "lo que el proyecto presentará, con su duración"), ("rol", "tarea que asume cada integrante del grupo"), ("calendario", "plan de fechas y duraciones de los ensayos"),
           ("restricción", "límite de tiempo, espacio o recursos que el plan debe respetar"), ("tiempo de trabajo", "minutos de un ensayo que quedan al restar calentamiento y pausas"), ("ajuste", "cambio pequeño que se hace al plan, con su razón")],
    worked=[
        ("Calcular el tiempo de trabajo", "Un ensayo de ejemplo dura 40 minutos, con 6 minutos de calentamiento y 4 minutos de silencio y descanso. ¿Cuántos minutos quedan para trabajar la pieza?",
         ["Se suman los minutos que no son de trabajo: 6 + 4 = 10.", "Se restan del total: 40 − 10 = 30 minutos."],
         "30 minutos"),
        ("Ajustar un plan", "Un grupo de ejemplo debe presentar 5 minutos como máximo, pero su pieza dura 6. ¿Qué ajuste cumple la restricción cambiando un solo elemento?",
         ["La restricción es de 5 minutos y la pieza dura 6, o sea 1 minuto de más.", "Se acorta la pieza, por ejemplo quitando una repetición de 1 minuto, y se anota la razón."],
         "Acortar la pieza en 1 minuto, quitando una repetición"),
    ],
    mistakes=[("Contar todos los minutos de la sala como tiempo de trabajo.", "Se olvidan el calentamiento y la pausa.", "Resta calentamiento y descansos del total antes de planificar."),
              ("Cambiar la pieza, los roles y el calendario a la vez cuando algo falla.", "No se sabe qué ajuste resolvió el problema.", "Cambia un solo elemento y anota su razón.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es un rol en un proyecto de grupo?', 'La tarea que asume cada integrante, como cantar, tocar o coordinar', 'La cantidad de ensayos que se hacen cada semana en la sala del liceo', 'La obra que otro grupo estrena en el mismo acto de cierre del liceo', 'Un rol es la tarea de cada persona; no es un ensayo ni la obra de otro grupo.'),
        ('abc', '{F} ¿Cuántos integrantes tiene el grupo de la ficha?', 'Cuatro', 'Dos', 'Tres', 'La ficha dice que son cuatro integrantes: dos voces, una guitarra y percusión.'),
        ('abc', '{F} ¿Cuál es la restricción de tiempo del acto?', 'Máximo 4 minutos por grupo', 'Máximo 3 minutos por grupo', 'Al menos 5 minutos por grupo', 'La ficha dice que el acto admite como máximo 4 minutos por grupo.'),
        ('=', '{F} ¿Cuántos minutos quedan para trabajar la pieza en un ensayo, si se restan el calentamiento y los 5 minutos de silencio y descanso?', '45-8-5', 'Se restan del total del ensayo el calentamiento y la pausa para conocer el tiempo de trabajo.', ' minutos'),
        ('=', '{F} ¿Cuántos minutos de ensayo suman los 5 ensayos en total?', '5*45', 'Se multiplican los 5 ensayos por 45 minutos cada uno.', ' minutos'),
        ('abc', '{F} La pieza dura 3 minutos y el acto admite 4. ¿Qué se puede decir del plan?', 'Cumple la restricción y sobra 1 minuto', 'No cumple, porque se pasa por 1 minuto', 'Cumple, pero justo sin sobrar nada', 'Con 3 minutos de pieza y 4 permitidos, sobra 1 minuto.'),
        ('{F} Escribe el plan de un ensayo de la ficha con sus tres tramos (calentamiento, trabajo y silencio y descanso) y los minutos de cada uno.', 'Calentamiento 8 min; trabajo de la pieza 32 min; silencio y descanso 5 min; total 45 min', 'El total es 45 minutos y el trabajo queda en 45 − 8 − 5 = 32 minutos.'),
        ('abc', '{F} Falta una semana y el grupo pierde el ensayo 4. ¿Qué ajuste cambia un solo elemento y mantiene el producto?', 'Agregar un ensayo de 45 minutos al final del calendario', 'Cambiar la pieza por otra más larga a último momento', 'Quitar el calentamiento de todos los ensayos', 'Agregar un ensayo recupera el tiempo perdido sin tocar el producto ni los cuidados.'),
        ('=', '{F} Si cada ensayo dedica 32 minutos al trabajo de la pieza, ¿cuántos minutos de trabajo suman los 5 ensayos?', '5*32', 'Se multiplican los 5 ensayos por los 32 minutos de trabajo de cada uno.', ' minutos'),
        ('abc', 'Un grupo propone suprimir el calentamiento y la pausa de silencio para «ganar tiempo de trabajo». ¿Qué problema tiene esa propuesta?', 'Aumenta el riesgo de fatiga o lesión y no garantiza un mejor resultado', 'Ninguno, porque más minutos de trabajo siempre mejoran la pieza que se prepara', 'Hace que la pieza dure menos de lo permitido y no quede tiempo suficiente', 'El calentamiento y el descanso cuidan la voz y las manos y sostienen la calidad del trabajo.'),
        ('abc', '{F} Un integrante dice que siente cansancio en la voz a mitad del ensayo. ¿Qué respuesta del grupo es la más adecuada?', 'Dar una pausa de silencio y retomar con tareas más suaves', 'Pedirle que cante más fuerte para no atrasarse con el resto del grupo', 'Cambiar su rol por otro sin preguntarle ni explicarle la razón', 'Ante cansancio se descansa y se retoma con suavidad; no se fuerza ni se decide por la persona.'),
        ('abc', '{F} Si el grupo decidiera cambiar a la vez la pieza, los roles y el calendario porque «algo no salió», ¿qué falla en esa decisión?', 'No se sabría cuál de los cambios resolvió el problema', 'Habría demasiados ensayos para el tiempo disponible', 'La restricción del acto dejaría de existir', 'Cambiar un solo elemento por vez permite saber qué ajuste funcionó.'),
        ('=', '{F} Si el acto admite 4 minutos y la pieza dura 3 minutos y 20 segundos, ¿cuántos segundos sobran?', '4*60-(3*60+20)', 'Se pasan los minutos a segundos y se resta la duración de la pieza al máximo permitido.', ' s'),
    ],
    ctx=('abc', 'Tu grupo dispone de 5 semanas hasta el acto y de una sala solo los jueves. ¿Qué plan respeta mejor el calendario de la ficha?', 'Un ensayo cada jueves, con calentamiento, pausa y cierre', 'Cinco ensayos el último jueves, uno tras otro sin descanso', 'Un solo ensayo largo de 225 minutos la víspera del acto', 'Ensayar una vez por semana reparte el trabajo y respeta el cuidado del cuerpo.'),
    sc=[
        ("En Interpretación musical: ¿qué es el tiempo de trabajo de un ensayo?", "Los minutos que quedan al restar el calentamiento y las pausas", "Es el tiempo realmente dedicado a trabajar la pieza."),
        ('abc', 'Si algo falla en el plan, conviene:', 'Cambiar un solo elemento y anotar su razón', 'Cambiar todo a la vez para empezar de cero', 'No cambiar nada y esperar al día del acto', 'Un ajuste por vez permite saber si funcionó.'),
        ("¿Por qué se incluye una pausa de silencio en cada ensayo?", "Para descansar la voz, las manos y el oído y mantener la calidad del trabajo", "El descanso previene la fatiga y mejora la atención."),
    ],
    op=("Con la {F}, escribe un ajuste al plan por una de estas situaciones: (a) la pieza dura 4 minutos y 30 segundos; (b) falta un ensayo de los cinco. Elige una y escribe el ajuste de un solo elemento, su razón y cómo comprobarás que funcionó.",
        "Situación (a): la pieza dura 30 segundos más que el máximo. Ajuste: quitar una repetición de 30 segundos. Razón: así cumple los 4 minutos permitidos sin tocar roles ni calendario. Comprobación: cronometrar una pasada completa en el próximo ensayo.",
        ["elige una situación", "propone un solo ajuste", "da una razón relacionada con la restricción", "dice cómo comprobar que funcionó"],
        ["hoja con la situación elegida, el ajuste, la razón y la comprobación"],
        ["cambiar varios elementos a la vez", "no explicar la razón", "olvidar la comprobación"],
        "Pregunta: «¿qué restricción estás respetando con ese ajuste?». Si no la nombra, pídele que la busque en la ficha."),
    reinforce="Escribe un plan de ensayo de 30 minutos con calentamiento, trabajo, pausa y cierre, y calcula los minutos de trabajo.",
    extend="Explica cómo cambiaría un plan si el grupo pasara de cuatro a seis integrantes y qué rol nuevo agregarías.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 4 (ensamble de ejemplo «Ronda de invierno», inventado, a 80 pulsos por minuto). Tres partes: percusión de mesa, guitarra y voz. "
     "Percusión: c1 a c8 | X . X X | X . X . |, un patrón de 2 compases que se repite durante toda la pieza. "
     "Guitarra: entra en c3; acorde Do en c3 y c4, Fa en c5 y c6, Sol en c7 y Do en c8. "
     "Voz: entra en c5 con la melodía; c5 | Mi Mi Fa Sol |; c6 | Sol Fa Mi - |; c7 | Re Re Mi Fa |; c8 | Mi - Do - |. "
     "Dinámica: la percusión empieza en mf y la guitarra entra en mf; al entrar la voz en c5, la percusión y la guitarra bajan a p y la voz canta en mf. " + CLAVE)
build(
    O2, 4, F,
    use="Aprenderé a interpretar en ensamble: repartir partes, hacer entradas claras, escucharnos y mantener el equilibrio entre voz, acompañamiento y ritmo, con volumen cuidado.",
    prior=["Sé leer una cuadrícula de pulsos y los compases.", "Sé qué es una frase y un acorde.", "Sé planificar un ensayo con calentamiento y pausas."],
    explain=[
        "Un ensamble es un grupo que interpreta una pieza repartida en partes. Cada parte cumple una función: la melodía lleva la idea principal, el acompañamiento arma el fondo con acordes y el ritmo mantiene el pulso. Una interpretación de ensamble se logra cuando las tres funciones se oyen y ninguna tapa a las otras.",
        "Para tocar juntos se necesitan tres hábitos. Primero, pulso compartido: todas las personas sienten el mismo pulso y no lo corren. Segundo, entradas claras: antes de empezar, una persona marca el pulso con un gesto de cabeza o con cuatro pulsos contados en voz baja, y cada parte entra en su compás. Tercero, escucha: se toca atendiendo a las demás partes, ajustando la fuerza para que la melodía se oiga sobre el acompañamiento.",
        "El equilibrio se logra con la dinámica de cada parte: cuando entra la voz, el acompañamiento baja la fuerza. Se ensaya a volumen moderado, con pausas de silencio; nunca se toca fuerte «para que se oiga» a costa del oído. Si alguien se pierde, se regresa a un punto de entrada acordado, que suele ser el comienzo de una frase.",
    ],
    vocab=[("ensamble", "grupo que interpreta una pieza repartida en partes"), ("melodía", "idea musical principal que se canta o toca"), ("acompañamiento", "fondo de acordes que sostiene la melodía"),
           ("entrada", "momento en que una parte empieza a sonar"), ("equilibrio", "estado en que ninguna parte tapa a las otras"), ("pulso compartido", "pulso que todas las partes sienten por igual")],
    worked=[
        ("Ubicar una entrada", "En una pieza de ejemplo con 8 compases de 4 pulsos, la voz entra en el compás 5. ¿Cuántos pulsos suenan antes de su entrada?",
         ["Antes del compás 5 hay 4 compases completos.", "Cada compás tiene 4 pulsos: 4 × 4 = 16 pulsos."],
         "16 pulsos"),
        ("Ajustar el equilibrio", "En un ensayo de ejemplo, la guitarra suena tan fuerte que no se oye la voz. ¿Qué ajuste busca el equilibrio sin subir el volumen total?",
         ["La voz es la melodía, así que debe oírse sobre el fondo.", "La guitarra baja su fuerza y la voz se mantiene: el volumen total no aumenta."],
         "Que la guitarra baje su fuerza y la voz se mantenga"),
    ],
    mistakes=[("Subir el volumen de todas las partes para que se oiga la melodía.", "El volumen total aumenta y se pierde el equilibrio.", "Baja el acompañamiento para que la melodía se oiga sin forzar el oído."),
              ("Entrar «cuando uno siente» sin contar con las demás partes.", "Se pierde el pulso compartido.", "Cuenta cuatro pulsos y entra en el compás acordado.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es el acompañamiento?', 'El fondo de acordes que sostiene la melodía', 'La melodía principal que lleva la idea central', 'El silencio que se hace antes de empezar', 'El acompañamiento arma el fondo; la melodía es la idea principal.'),
        ('abc', '{F} ¿En qué compás entra la guitarra?', 'En el compás 3', 'En el compás 1', 'En el compás 5', 'La ficha dice que la guitarra entra en c3; la voz entra en c5.'),
        ('abc', '{F} ¿Qué parte lleva la melodía?', 'La voz', 'La percusión de mesa', 'La guitarra', 'La voz canta la melodía; la percusión y la guitarra acompañan.'),
        ('=', '{F} ¿Cuántos pulsos suenan antes de que entre la guitarra, que lo hace en el compás 3?', '2*4', 'Antes del compás 3 hay dos compases completos de 4 pulsos cada uno.', ' pulsos'),
        ('abc', '{F} ¿Qué acorde toca la guitarra en el compás 6?', 'Fa', 'Do', 'Sol', 'La ficha dice Fa en c5 y c6; Do en c3 y c4; Sol en c7 y Do en c8.'),
        ('abc', '{F} ¿Qué pasa con la dinámica cuando entra la voz?', 'La percusión y la guitarra bajan a p y la voz se mantiene en mf', 'La percusión y la guitarra suben a f para acompañar mejor a la voz', 'La voz baja a p y las demás partes siguen igual que antes de su entrada', 'Para que la melodía se oiga, el acompañamiento baja y la voz se mantiene.'),
        ('=', '{F} La pieza tiene 8 compases de 4 pulsos a 80 pulsos por minuto. ¿Cuántos segundos dura?', '8*4*60//80', 'Los pulsos totales se multiplican por 60 y se dividen por los pulsos por minuto.', ' s'),
        ('abc', '{F} La voz no se oye en el ensayo. ¿Qué ajuste de equilibrio corresponde?', 'Que el acompañamiento baje su fuerza y la voz se mantenga', 'Que la voz grite y el resto siga igual', 'Que la percusión toque más fuerte para marcar el pulso', 'El ajuste cuida el oído y mantiene el equilibrio: baja el fondo y no sube el volumen total.'),
        ('{F} Escribe, compás por compás, qué partes suenan en los compases 1 a 8, con las palabras «percusión», «guitarra» y «voz».', 'c1-c2 percusión; c3-c4 percusión y guitarra; c5-c8 percusión, guitarra y voz', 'La percusión suena todo el tiempo, la guitarra desde c3 y la voz desde c5.'),
        ('abc', '{F} Un integrante se pierde en el compás 6. ¿Cuál es el mejor punto para volver a entrar?', 'El comienzo de la siguiente frase, en el compás 7, tras contar los pulsos', 'Cualquier pulso, a medida que la persona lo sienta mejor para entrar', 'El compás 1, aunque los demás sigan tocando el compás 6 en ese momento', 'Se vuelve a entrar en un punto acordado, normalmente el comienzo de una frase.'),
        ('abc', 'Un grupo toca a volumen muy alto «para sentirse más potente». ¿Qué decisión de ensayo es más segura?', 'Bajar el volumen y escucharse entre todas las partes', 'Seguir tocando fuerte porque así se aprende mejor', 'Poner los auriculares a tope para oírse más', 'Un volumen moderado protege el oído y permite escuchar el equilibrio de las partes.'),
        ('abc', '{F} La percusión acelera un poco en el compás 4 y la guitarra sigue en el tempo original. ¿Qué falla en el ensamble?', 'No se mantiene un pulso compartido', 'La voz entró demasiado temprano', 'La guitarra no tiene acordes', 'Cuando el pulso se corre, las partes dejan de estar sincronizadas.'),
        ('=', '{F} La voz entra en el compás 5. ¿Cuántos segundos pasan, a 80 pulsos por minuto, desde el inicio hasta su entrada?', '4*4*60//80', 'Antes del compás 5 hay 16 pulsos; se pasan a segundos con el tempo dado.', ' s'),
    ],
    ctx=('abc', 'Tu grupo ensaya en una sala pequeña con la guitarra y la voz, y las personas del salón de al lado piden menos ruido. ¿Qué decisión respeta al grupo y a los demás?', 'Bajar el volumen general y mantener el equilibrio entre las partes', 'Subir el volumen de la voz para tapar la guitarra y el ruido del salón', 'Dejar de ensayar del todo y presentar la pieza sin practicar antes', 'Bajar el volumen respeta a los demás y protege el oído sin perder el equilibrio.'),
    sc=[
        ("En Interpretación musical: ¿qué es el equilibrio en un ensamble?", "Que ninguna parte tape a las otras", "El equilibrio se logra con la fuerza de cada parte."),
        ('abc', 'Para entrar juntas, las personas del grupo:', 'Cuentan cuatro pulsos y entran en el compás acordado', 'Entran cada una cuando siente que es el momento de hacerlo', 'Esperan a que otra parte se equivoque para poder entrar con más calma', 'Una entrada clara usa pulsos contados y un compás acordado.'),
        ("¿Qué haces si el volumen del ensayo molesta o te cansa el oído?", "Bajo el volumen y hago una pausa de silencio", "El oído se cuida con volumen moderado y descanso."),
    ],
    op=("Con la {F}, escribe un plan de entrada para el ensamble: quién cuenta los pulsos, cómo lo hace y en qué compás entra cada parte. Después escribe un ajuste de equilibrio para el compás 5, cuando entra la voz.",
        "Cuenta la percusión, que empieza el ensayo: cuatro pulsos en voz baja con un gesto de cabeza. Entradas: percusión en c1, guitarra en c3, voz en c5. Ajuste del compás 5: la percusión y la guitarra bajan a p y la voz se mantiene en mf, para que se oiga la melodía sin subir el volumen total.",
        ["indica quién cuenta y cómo", "nombra el compás de entrada de cada parte", "describe un ajuste de equilibrio", "cuida el volumen y el oído"],
        ["hoja con el plan de entrada y el ajuste de equilibrio"],
        ["no decir quién cuenta", "confundir el compás de entrada", "subir el volumen para equilibrar"],
        "Pregunta: «¿cómo sabe la guitarra que debe entrar?». Si no puede responder, pídele que escriba los pulsos que cuenta antes de entrar."),
    reinforce="Escribe en una cuadrícula las entradas de tres partes de una pieza de 6 compases, con cada parte entrando en un compás distinto.",
    extend="Explica por qué un ensamble de dos personas también necesita acordar quién entra primero y cómo se cuenta.",
)

# ============================================================ OAC-02, clase 5
F = ("Ficha 5 (bitácora de ensayo de ejemplo del grupo «Ronda de invierno», inventada). "
     "Ensayo 1: problema, la guitarra y la percusión se desfasan en c3 (en 4 pasadas hubo 6 desfases en total); ajuste, contar cuatro pulsos antes de entrar; resultado, en el ensayo 2 hubo 3 desfases en 4 pasadas. "
     "Ensayo 2: problema, la voz no se oye en c5-c6; ajuste, la guitarra baja de mf a p desde c5; resultado, se oye la voz, pero la guitarra se oye muy débil. "
     "Ensayo 3: problema, la guitarra suena muy débil; ajuste, la guitarra sube de p a un punto entre p y mf; resultado, se oyen ambas, pero la voz se cansa en la tercera pasada. "
     "Regla del grupo: se cambia un solo elemento por ensayo y se anota la razón.")
build(
    O2, 5, F,
    use="Aprenderé a llevar una bitácora de ensayo (problema, ajuste, resultado) y a decidir el siguiente ajuste con evidencia, cambiando una sola cosa a la vez y cuidando la voz y las manos.",
    prior=["Sé planificar un ensayo.", "Sé que una prueba cambia un solo recurso.", "Sé contrastar datos con evidencia."],
    explain=[
        "Una bitácora de ensayo es un registro breve que se escribe después de cada ensayo. Cada entrada tiene cuatro partes: el problema (qué no salió como se quería), el ajuste (qué se cambió), el resultado (qué se oyó después) y el siguiente paso. Con una bitácora, el grupo no depende de la memoria ni de la sensación del momento: puede revisar su avance con datos.",
        "Para que un ajuste sirva, se cambia un solo elemento por vez. Si el grupo cambia el tempo, la fuerza y la entrada a la vez, no sabrá cuál de los tres resolvió el problema. Cuando es posible, el resultado se mide: cuántos desfases hubo en cuatro pasadas, cuántos segundos duró la pieza, cuántas veces se perdió alguien. Un número permite comparar entre ensayos.",
        "La bitácora también registra el cuerpo: si hubo cansancio en la voz, tensión en las manos o dolor de oído. Eso se anota como parte del resultado y puede cambiar el siguiente paso (más descanso, menos pasadas, otra postura). Ensayar más no siempre es ensayar mejor; la bitácora ayuda a decidir cuándo parar.",
    ],
    vocab=[("bitácora", "registro de cada ensayo con problema, ajuste y resultado"), ("problema", "lo que no salió como se quería"), ("ajuste", "cambio de un solo elemento para resolver un problema"),
           ("resultado", "lo que se observó después del ajuste"), ("desfase", "momento en que dos partes no coinciden en el pulso"), ("siguiente paso", "decisión para el próximo ensayo")],
    worked=[
        ("Leer una entrada", "Una bitácora dice: «Ensayo 2: problema, el final se acelera; ajuste, practicar el último compás con pulso marcado; resultado, en 4 pasadas el final se aceleró 1 vez, antes eran 3». ¿Mejoró el problema y cuánto?",
         ["Antes se aceleraba 3 veces y ahora 1 vez, en las mismas 4 pasadas.", "Bajó de 3 a 1: 3 − 1 = 2 veces menos."],
         "Sí: 2 aceleraciones menos en 4 pasadas"),
        ("Decidir el siguiente paso", "Una entrada dice: «ajuste, subir la fuerza de la guitarra; resultado, ahora la voz queda tapada». ¿Qué siguiente paso conserva la regla de un solo cambio?",
         ["El problema nuevo es que la voz queda tapada: hay que cuidar un solo elemento.", "Se baja un poco la fuerza de la guitarra, sin tocar tempo ni entradas, y se anota."],
         "Bajar un poco la fuerza de la guitarra, sin cambiar nada más"),
    ],
    mistakes=[("Escribir «salió mejor» sin decir qué cambió ni cuánto mejoró.", "No permite comparar ni repetir lo que funcionó.", "Anota el ajuste y un resultado medible o descrito con detalle."),
              ("Seguir ensayando varias horas aunque haya cansancio de voz.", "La bitácora no se usa para cuidar el cuerpo.", "Registra el cansancio y baja las pasadas o suma descanso.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es una bitácora de ensayo?', 'Un registro de cada ensayo con problema, ajuste y resultado', 'Una lista de las canciones que el grupo quiere tocar algún día', 'Un permiso firmado para usar la sala de ensayo del liceo', 'La bitácora ordena lo que se hizo en cada ensayo; no es un repertorio ni un permiso.'),
        ('abc', '{F} ¿Cuál fue el problema del ensayo 1?', 'La guitarra y la percusión se desfasaban en c3', 'La voz no se oía en c5-c6', 'La guitarra sonaba muy débil', 'Los otros problemas aparecen en los ensayos 2 y 3.'),
        ('abc', '{F} ¿Qué ajuste se hizo en el ensayo 1?', 'Contar cuatro pulsos antes de entrar', 'Bajar la fuerza de la guitarra a p', 'Subir la fuerza de la voz a f', 'La ficha dice que el ajuste del ensayo 1 fue contar cuatro pulsos antes de entrar.'),
        ('=', '{F} En 4 pasadas hubo 6 desfases en el ensayo 1 y 3 en el ensayo 2. ¿Cuántos desfases menos hubo en el ensayo 2?', '6-3', 'Se restan los desfases del ensayo 2 a los del ensayo 1.', ' desfases'),
        ('abc', '{F} ¿Qué resultado tuvo el ajuste del ensayo 2?', 'Se oyó la voz, pero la guitarra quedó muy débil', 'Se oyó la guitarra, pero la voz quedó muy débil', 'No cambió nada en el equilibrio de las partes', 'La ficha dice que se oye la voz, pero la guitarra queda muy débil.'),
        ('abc', '{F} ¿Qué se debió anotar en el ensayo 3 sobre el cuerpo?', 'Que la voz se cansó en la tercera pasada', 'Que la guitarra necesita otras cuerdas', 'Que el calendario tiene 5 ensayos', 'La ficha registra que la voz se cansa en la tercera pasada, un dato de cuidado.'),
        ('=', '{F} Si cada pasada dura 24 segundos, ¿cuántos segundos suman las 4 pasadas de un ensayo?', '4*24', 'Se multiplican las pasadas por la duración de cada una.', ' s'),
        ('abc', '{F} El grupo ve que la voz se cansa en la tercera pasada. ¿Cuál es el siguiente paso que respeta la regla de un solo cambio?', 'Hacer solo dos pasadas seguidas y una pausa de silencio', 'Aumentar a seis pasadas para que la voz se acostumbre', 'Cambiar a la vez el tempo, la entrada y la fuerza', 'Reducir las pasadas es un solo cambio y cuida la voz.'),
        ('=', '{F} Si en el ensayo 3 hubo 1 desfase en 4 pasadas, ¿cuántos desfases menos que en el ensayo 1 hubo?', '6-1', 'Se compara el desfase del ensayo 3 con el del ensayo 1.', ' desfases'),
        ('abc', 'Dos entradas de bitácora: (1) «salió mejor»; (2) «ajuste: pulso marcado en c8; resultado: 1 aceleración en 4 pasadas, antes 3». ¿Cuál es más útil?', 'La 2, porque nombra el ajuste y mide el resultado', 'La 1, porque es más corta y rápida de leer en el ensayo', 'Las dos igual, porque las dos dicen que hubo una mejora', 'La entrada 2 permite repetir el ajuste y comparar con datos; la 1 no.'),
        ('abc', '{F} El grupo cambió a la vez la fuerza de la guitarra, el tempo y la entrada, y el problema mejoró. ¿Qué falla en esa conclusión?', 'No se sabe cuál de los tres cambios fue el que ayudó', 'Cambiar el tempo nunca puede ayudar a un grupo', 'Las bitácoras no admiten registrar más de un cambio', 'La regla del grupo es cambiar un elemento por ensayo, para atribuir el efecto a un cambio.'),
        ('abc', '{F} ¿Qué decisión corresponde si la voz se cansa de nuevo en la tercera pasada con la nueva forma de ensayo?', 'Anotar el cansancio y sumar descanso, aunque se hagan menos pasadas', 'Ignorarlo y subir la exigencia en el siguiente ensayo para acostumbrar la voz', 'Quitar la voz de la pieza sin conversarlo antes con la persona afectada', 'El cansancio es un dato de salud y se atiende con descanso y menos pasadas.'),
        ('abc', 'Un grupo escribe: «ensayo 4: problema, el final se acelera; ajuste, practicar el final con pulso marcado y también subir el tempo». ¿Qué problema tiene esta entrada?', 'Incluye dos cambios, así que no se sabrá cuál funcionó', 'Falta el nombre del grupo en la entrada de la bitácora', 'No dice cuántas personas ensayaron ese día en la sala', 'La regla es cambiar un solo elemento por vez; esta entrada cambia dos.'),
    ],
    ctx=('=', 'Un grupo mide cuántos desfases hay en 5 pasadas: antes del ajuste hubo 10 y después hubo 4. ¿Cuántos desfases menos hubo con el ajuste?', '10-4', 'Se restan los desfases posteriores a los anteriores para ver cuánto mejoró.', ' desfases'),
    sc=[
        ("En Interpretación musical: ¿qué es un ajuste?", "Un cambio de un solo elemento para resolver un problema del ensayo", "Un ajuste se limita a un cambio para saber si funcionó."),
        ('abc', 'Una entrada de bitácora lleva:', 'Problema, ajuste, resultado y siguiente paso', 'Solo el nombre de las personas del grupo y la fecha', 'Solo una opinión sobre cómo estuvo el grupo', 'La estructura completa permite revisar el avance.'),
        ("¿Por qué se anota si hubo cansancio de voz o de manos?", "Porque cuidar el cuerpo cambia las decisiones del siguiente ensayo", "El cansancio es un dato que ayuda a ensayar de manera segura."),
    ],
    op=("Con la {F}, escribe la entrada del ensayo 4 del grupo: elige un problema posible (por ejemplo, la voz se cansa o la guitarra se retrasa), un único ajuste, el resultado que esperas medir y el siguiente paso. Incluye una nota sobre el cuidado del cuerpo.",
        "Ensayo 4: problema, la voz se cansa en la tercera pasada. Ajuste: hacer solo dos pasadas seguidas y una pausa de silencio. Resultado esperado: llegar al final de la segunda pasada sin cansancio. Siguiente paso: si funciona, sumar una pasada corta. Nota de cuidado: tomar agua y soltar los hombros antes de empezar.",
        ["describe un problema concreto", "propone un solo ajuste", "dice qué resultado medirá", "incluye una nota de cuidado del cuerpo"],
        ["hoja con la entrada de bitácora completa"],
        ["proponer varios ajustes a la vez", "no decir cómo medirá el resultado", "olvidar el cuidado del cuerpo"],
        "Pregunta: «¿qué dato te dirá si el ajuste funcionó?». Si no lo tiene, pídele un número o una descripción observable."),
    reinforce="Escribe tres entradas de bitácora de ejemplo para un grupo que corrige el pulso, cambiando un solo elemento por entrada.",
    extend="Explica cómo cambiaría tu decisión si un ajuste mejora el sonido pero deja a una persona con cansancio fuerte.",
)

# ============================================================ OAC-02, clase 6
F = ("Ficha 6 (proyecto de ejemplo «Ronda de invierno», inventado). Pieza original del grupo, con un arreglo de una canción tradicional de dominio público (el docente verifica la procedencia). "
     "Datos del proyecto: título, «Ronda de invierno»; autoría de la pieza propia, las cuatro personas del grupo; arreglo de la canción tradicional, hecho por el grupo; intérpretes, las cuatro personas del grupo. "
     "Presentación: acto del liceo, con registro en video propuesto por el grupo. Dos integrantes, Sol y Max, aceptan ser grabados; una persona, Ema, prefiere no aparecer. "
     "Pauta de evaluación del proyecto: (1) cumple su propósito; (2) cumple la duración; (3) hay trabajo de ensamble; (4) las fuentes y autorías están citadas.")
build(
    O2, 6, F,
    use="Aprenderé a evaluar un proyecto de interpretación con una pauta, a atribuir autorías y fuentes (pieza propia, arreglo, obra de otra persona) y a decidir cómo difundirlo con consentimiento y respeto.",
    prior=["Sé investigar y registrar fuentes.", "Sé planificar y llevar una bitácora.", "Sé que una persona puede decidir si la graban."],
    explain=[
        "Al terminar un proyecto se evalúa con una pauta de criterios: si cumplió su propósito, si respetó la duración, si hubo trabajo de ensamble y si las fuentes están citadas. Cada criterio se evalúa con evidencia (la bitácora, la duración medida, lo que se oyó en la última pasada). Evaluar permite decidir qué conservar para el próximo proyecto.",
        "Atribuir es decir de quién es cada cosa. En una interpretación se distinguen: la pieza original (quién la compuso), el arreglo (quién cambió la manera de tocarla) y la interpretación (quiénes la tocan). Si el grupo toca una obra de otra persona, se cita su nombre y su título. Si la obra está protegida, se pide permiso o se elige otra; tu docente te guía sobre qué obras se pueden usar y cómo.",
        "Difundir un proyecto es compartirlo con un público. Antes de grabar o publicar se pide permiso a cada persona que aparece, y quien prefiere no aparecer puede decir que no sin dar explicaciones. Se comparte solo lo que el grupo acordó, sin datos personales ni de personas que no participan, y se cita la autoría. Si algo incomoda, se avisa a una persona adulta de confianza.",
    ],
    vocab=[("atribuir", "indicar de quién es cada obra, arreglo o interpretación"), ("arreglo", "versión de una pieza con cambios en su manera de tocarse"), ("consentimiento", "permiso libre de una persona para aparecer o ser grabada"),
           ("difundir", "compartir un proyecto con un público"), ("pauta", "lista de criterios observables para evaluar"), ("dominio público", "obras cuyo uso no requiere permiso del autor (el docente verifica cada caso)")],
    worked=[
        ("Atribuir correctamente", "Un grupo toca un arreglo propio de una canción tradicional. ¿Cómo se atribuye la autoría en el programa?",
         ["La canción es tradicional: se cita como canción tradicional.", "El arreglo y la interpretación los hizo el grupo: «arreglo e interpretación: nombre del grupo»."],
         "«Canción tradicional; arreglo e interpretación: el grupo»"),
        ("Decidir sobre el registro", "Tres personas del grupo aceptan ser grabadas y una dice que prefiere no aparecer. ¿Qué decisión respeta a todas?",
         ["El permiso es de cada persona y quien prefiere no aparecer puede decir que no.", "Se graba solo con quienes aceptaron, o se hace un registro de audio sin imagen, o se graba sin que aparezca esa persona."],
         "Respetar su decisión y grabar solo con quienes aceptaron, sin que aparezca esa persona"),
    ],
    mistakes=[("Presentar un arreglo de una obra ajena como si fuera obra propia.", "Se omite la autoría de la pieza original.", "Cita la obra original y atribuye el arreglo al grupo."),
              ("Grabar y publicar a todo el grupo porque «la mayoría quiso».", "El permiso es individual y no se decide por mayoría.", "Pide permiso a cada persona y respeta una negativa sin presionar.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es atribuir?', 'Indicar de quién es cada obra, arreglo o interpretación', 'Aumentar el volumen de la parte que lleva la melodía', 'Cambiar el título de una obra para que parezca nueva', 'Atribuir es reconocer autorías; no es subir el volumen ni cambiar títulos.'),
        ('abc', '{F} ¿Quiénes son los autores de la pieza propia del grupo?', 'Las cuatro personas del grupo', 'Solo la voz principal', 'La persona que coordina el calendario', 'La ficha dice que la autoría de la pieza propia es de las cuatro personas del grupo.'),
        ('abc', '{F} ¿Qué es la canción tradicional de la ficha respecto del arreglo?', 'La obra original, a la que el grupo le hizo un arreglo', 'La obra nueva compuesta por las personas del grupo para el acto', 'Una copia de otra obra, sin ningún cambio ni arreglo del grupo', 'El grupo arregla una canción tradicional: la obra original es la tradicional.'),
        ('abc', '{F} ¿Cuántas personas del grupo aceptan ser grabadas?', 'Dos, Sol y Max', 'Cuatro, todas las personas del grupo', 'Tres, todas menos una persona', 'La ficha dice que Sol y Max aceptan y que Ema prefiere no aparecer.'),
        ('=', '{F} De las 4 personas del grupo, 2 aceptan ser grabadas. Según la ficha, ¿cuántas personas del grupo aún no han dicho su decisión sobre aparecer en el video?', '4-2-1', 'Se restan las que aceptan y la que prefiere no aparecer de las cuatro personas.', ' persona'),
        ('abc', '{F} ¿Qué decisión respeta a Ema?', 'No grabarla y avisar al grupo que se respeta su decisión', 'Grabarla igual, porque la mayoría del grupo aceptó aparecer', 'Pedirle una y otra vez hasta que acepte aparecer en el video', 'El permiso es individual; respetar una negativa es parte del consentimiento.'),
        ('Otro grupo toca sin cambios una canción tradicional y una pieza que compuso solo Lía. Escribe cómo se atribuye cada una en su programa.', 'Canción tradicional: interpretación del grupo; pieza propia: composición de Lía, interpretación del grupo', 'La obra tradicional se cita como tal, y la pieza se atribuye a quien la compuso.'),
        ('=', '{F} El grupo toca la pieza propia de 3 minutos y el arreglo de 2 minutos. ¿Cuántos minutos suman?', '3+2', 'Se suman las duraciones de las dos piezas del programa.', ' minutos'),
        ('abc', '{F} El acto admite 6 minutos y el programa dura 5. ¿Qué criterio de la pauta se cumple?', 'El criterio 2, porque cumple la duración', 'El criterio 4, porque cita las fuentes', 'El criterio 1, porque cumple el propósito', 'La duración de 5 minutos cabe en los 6 permitidos, por lo que se cumple el criterio 2.'),
        ('abc', 'En el programa de otro grupo aparece: «Autor: nuestro grupo», pero tocan sin cambios una canción de otra persona. ¿Qué falla en esa atribución?', 'No se cita a la autora de la obra original', 'Falta el nombre de la sala de ensayo del grupo', 'No dice cuántas veces ensayaron antes del acto', 'Una obra ajena debe citarse; atribuir como propio algo que no lo es, es un error.'),
        ('abc', '{F} Un amigo del grupo pide ver el video y dice que lo subirá a una red para «que todos lo vean». ¿Qué debe hacer el grupo?', 'Acordar primero con quienes aparecen y con su docente si se difunde', 'Mandarlo de inmediato, porque ya está grabado y es del grupo', 'Subirlo sin mostrar quiénes tocan para evitar pedir permisos a nadie', 'Se difunde solo lo acordado con quienes aparecen; la grabación no equivale a permiso.'),
        ('abc', '{F} El grupo evalúa el criterio 4 de la pauta. ¿Qué evidencia sirve?', 'El programa con la autoría de la pieza y del arreglo citada', 'El número de personas que aplaudió con fuerza al final del acto', 'El largo de las uñas de la persona que tocó la guitarra en el acto', 'El criterio 4 se evalúa con evidencia de fuentes y autorías citadas.'),
        ('abc', '{F} Ema recibe presión de una persona para aparecer en el video. ¿Qué respuesta de Ema y del grupo es la más adecuada?', 'Mantener su decisión y avisar a una persona adulta de confianza si la presión sigue', 'Ceder para evitar un conflicto con quien presiona y aparecer igual en el video', 'Esconder lo ocurrido y no avisar a nadie por miedo a empeorar el problema', 'La decisión de Ema se respeta y, ante presión, se avisa a una persona adulta de confianza.'),
    ],
    ctx=('abc', 'Tu grupo quiere tocar en una feria del liceo una canción actual muy conocida. No sabe si puede usarla. ¿Qué decisión es la más adecuada?', 'Consultar a su docente y, si no se puede, elegir otra obra o una propia', 'Tocarla igual y no decir de quién es, porque ya es muy conocida', 'Cambiar el título de la canción y presentarla como si fuera propia', 'Si hay dudas de derechos se consulta al docente y se elige una obra que se pueda usar.'),
    sc=[
        ("En Interpretación musical: ¿qué es el consentimiento para ser grabado?", "El permiso libre de cada persona para aparecer o ser grabada", "El permiso es individual y se puede negar."),
        ('abc', 'Un arreglo de una canción tradicional se atribuye:', 'Citando la canción tradicional y a quien hizo el arreglo', 'Como obra propia del grupo, sin citar la canción tradicional', 'Sin ninguna atribución, porque el arreglo ya es del grupo', 'Se reconoce la obra original y el trabajo del arreglo.'),
        ("¿Qué haces si una persona del grupo no quiere que la graben?", "Respeto su decisión y grabo sin que aparezca", "Respetar una negativa es parte del consentimiento."),
    ],
    op=("Con la {F}, escribe un breve texto para el programa del acto que atribuya la pieza propia y el arreglo, y una frase para decidir cómo difundir el video respetando a Ema. Luego evalúa el proyecto con los cuatro criterios de la pauta con «cumple» o «falta» y una evidencia.",
        "Programa: «Ronda de invierno», pieza original de las cuatro personas del grupo; arreglo de una canción tradicional, arreglo del grupo. Difusión: se graba solo a Sol y Max, y Ema no aparece. Evaluación: (1) propósito, cumple, el público se calmó; (2) duración, cumple, 5 de 6 minutos; (3) ensamble, cumple, hubo pocos desfases; (4) fuentes, cumple, el programa cita la autoría.",
        ["atribuye la pieza propia y el arreglo", "decide la difusión respetando a Ema", "evalúa los cuatro criterios", "cita una evidencia en cada criterio"],
        ["hoja con el texto del programa, la decisión de difusión y la pauta evaluada"],
        ["omitir la obra original", "grabar a Ema contra su deseo", "evaluar sin evidencia"],
        "Pregunta: «¿de quién es cada parte del programa?». Si no lo sabe, pídele que lea de nuevo la ficha."),
    reinforce="Escribe la atribución completa del programa de un grupo imaginario con una pieza propia, un arreglo y una obra de otra persona.",
    extend="Explica por qué es importante respetar una negativa a ser grabado aunque el resto del grupo esté de acuerdo.",
)

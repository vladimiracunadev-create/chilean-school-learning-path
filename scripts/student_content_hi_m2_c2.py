"""Cuaderno del estudiante, 2.º medio Historia, Geografía y Ciencias Sociales: OA 19 (recuperación democrática en los años ochenta) y OA 20 (plebiscito, transición y reparación)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI2M OA 19"

# ---------------------------------------------------------------- OA 19, clase 1
F1 = ("Ficha 1 (hechos y actores; los datos de ejemplo están rotulados). "
      "Hechos: en 1973 comienza el gobierno militar encabezado por Augusto Pinochet; en 1976 la Iglesia Católica crea la Vicaría de la Solidaridad para ayudar a personas perseguidas; "
      "en 1982 el país entra en una grave crisis económica, con empresas cerradas y desempleo; en 1983 se realizan las primeras protestas nacionales y se forma la Alianza Democrática, un conglomerado de partidos de oposición; "
      "en 1985 varios partidos firman el Acuerdo Nacional para la Transición a la Plena Democracia, con la mediación de la Iglesia; en 1987 el papa Juan Pablo II visita Chile; el 5 de octubre de 1988 se realiza el plebiscito. "
      "Actores: gobierno militar, partidos políticos, Iglesia Católica, organismos de defensa de los derechos humanos, sindicatos, pobladores, estudiantes y comunidad internacional (gobiernos y organismos de otros países).")
build(
    OA, 1, F1,
    use="Aprenderé a situar en el tiempo los hechos que llevaron a recuperar la democracia en los años ochenta y a reconocer quiénes participaron, para formular una pregunta de investigación clara.",
    prior=["Sé que en 1973 se interrumpió la democracia y que comenzó un gobierno militar.", "Sé ubicar un año en una línea de tiempo y calcular diferencias entre años.", "Sé que una fuente es una huella del pasado."],
    explain=[
        "La recuperación de la democracia en Chile no ocurrió en un solo día: fue un proceso de varios años. Una crisis económica grave en 1982 aumentó el descontento, y en 1983 comenzaron las primeras protestas nacionales. Después, los partidos de oposición se reorganizaron, como en la Alianza Democrática de 1983, y junto con organizaciones sociales y otros actores buscaron salidas políticas, hasta llegar al plebiscito de 1988.",
        "Un actor es una persona o grupo que participa en un hecho histórico. Los actores sociales son los grupos de la sociedad, como sindicatos, pobladores y estudiantes. Otros actores fueron los partidos, el gobierno militar, la Iglesia Católica, los organismos de defensa de los derechos humanos y la comunidad internacional, es decir, gobiernos y organismos de otros países.",
        "Para estudiar el tema hay que ubicar cada hecho en su fecha y decir quién lo impulsó. Un error frecuente es explicar todo con un solo actor o con una sola fecha. Una buena pregunta de investigación nombra el proceso, el tiempo y varios factores posibles, y se puede responder con evidencia.",
    ],
    vocab=[("actor social", "grupo de la sociedad que se organiza y participa, como sindicatos, pobladores o estudiantes"), ("comunidad internacional", "gobiernos y organismos de otros países que opinan o actúan sobre un hecho"), ("protesta", "manifestación pública para expresar descontento o exigir un cambio"), ("mediación", "ayuda de un tercero para que dos partes lleguen a acuerdo"), ("proceso histórico", "conjunto de hechos encadenados durante varios años")],
    worked=[
        ("Calcular un intervalo", "¿Cuántos años pasaron entre las primeras protestas nacionales y el Acuerdo Nacional?", ["Tomo los años de la ficha: 1983 y 1985.", "Resto: 1985 − 1983 = 2."], "2 años"),
        ("Clasificar un actor", "Un sindicato convoca a sus socios a una jornada de protesta. ¿Qué tipo de actor es?", ["Un sindicato es un grupo de la sociedad que se organiza.", "No es un gobierno ni un partido."], "Un actor social"),
    ],
    mistakes=[("Decir que la democracia volvió en 1983, cuando empezaron las protestas.", "Se confunde el comienzo de un proceso con su resultado.", "Ubica protestas, acuerdos y plebiscito en fechas distintas."),
              ("Explicar el proceso con un solo actor.", "Se ignoran los partidos, las organizaciones sociales y la comunidad internacional.", "Nombra al menos tres actores y qué hizo cada uno.")],
    T=[
        ("{F} ¿Qué organización creó la Iglesia Católica en 1976?", "La Vicaría de la Solidaridad", "La ficha dice que se creó para ayudar a personas perseguidas."),
        ("{F} ¿En qué año se realizaron las primeras protestas nacionales?", "1983", "La ficha lo indica en la lista de hechos."),
        ("{F} ¿Quién visitó Chile en 1987?", "El papa Juan Pablo II", "La ficha registra esa visita."),
        ("{F} ¿Cuál de estos hechos ocurrió antes de la crisis económica de 1982? A) La creación de la Vicaría de la Solidaridad B) Las primeras protestas nacionales", "A) La creación de la Vicaría de la Solidaridad", "La Vicaría se creó en 1976; las protestas fueron en 1983."),
        ("{F} ¿Qué hecho de 1983 muestra que los partidos de oposición volvían a organizarse? A) La formación de la Alianza Democrática B) La visita del papa", "A) La formación de la Alianza Democrática", "La visita del papa fue en 1987 y no es una organización de partidos."),
        ("{F} Estudiantes, pobladores y un sindicato salen a protestar. ¿Cómo se les llama en conjunto? A) Actores sociales B) Comunidad internacional", "A) Actores sociales", "Son grupos de la sociedad que se organizan, no gobiernos de otros países."),
        ("{F} El gobierno de otro país envía una nota pidiendo respeto a los derechos humanos en Chile. ¿Qué actor es? A) Comunidad internacional B) Actor social", "A) Comunidad internacional", "Los gobiernos de otros países forman parte de la comunidad internacional según la ficha."),
        ("{F} ¿Cuál es el orden correcto? A) Crisis económica, protestas nacionales, plebiscito B) Protestas nacionales, crisis económica, plebiscito", "A) Crisis económica, protestas nacionales, plebiscito", "La crisis es de 1982, las protestas de 1983 y el plebiscito de 1988."),
        ("=", "{F} Una línea de tiempo usa 1 cm = 3 años y va de 1973 a 1988. ¿Cuántos centímetros mide?", "(1988-1973)/3", "Se divide el tramo de 15 años por lo que vale cada centímetro.", " cm"),
        ("{F} ¿Por qué no basta una sola fecha para explicar la recuperación de la democracia?", "Porque fue un proceso de varios años con muchos actores", "La ficha muestra hechos entre 1982 y 1988 y actores distintos."),
        ("{F} Un compañero dice: «La democracia volvió solo porque la Iglesia lo decidió». ¿Qué corrección haces? A) Participaron muchos actores, como partidos, organizaciones sociales y comunidad internacional B) Es correcto porque la Iglesia ayudó a las víctimas", "A) Participaron muchos actores, como partidos, organizaciones sociales y comunidad internacional", "Un solo actor no explica un proceso con tantos participantes."),
        ("{F} ¿Cuál es la mejor pregunta de investigación? A) ¿Qué factores económicos, sociales y políticos incidieron en la recuperación de la democracia en los años ochenta? B) ¿Quién fue el opositor más valiente?", "A) ¿Qué factores económicos, sociales y políticos incidieron en la recuperación de la democracia en los años ochenta?", "La pregunta A tiene tema, tiempo y se responde con evidencia; la B es una opinión."),
        ("{F} ¿Qué ocurrió después del Acuerdo Nacional? A) La visita del papa en 1987 B) Las primeras protestas nacionales", "A) La visita del papa en 1987", "1987 es posterior a 1985; las protestas fueron en 1983."),
    ],
    ctx=("Un afiche de una muestra escolar dice: «En 1983 se recuperó la democracia». ¿Qué problema tiene? A) Confunde el inicio de las protestas con el fin de un proceso que continuó hasta 1988 y después B) Es demasiado corto", "A) Confunde el inicio de las protestas con el fin de un proceso que continuó hasta 1988 y después", "La ficha ubica el plebiscito en 1988; en 1983 solo comenzaron las protestas."),
    sc=[("¿Qué es un actor social?", "Un grupo de la sociedad que se organiza y participa, como sindicatos, pobladores o estudiantes", "Así se define en el vocabulario."),
        ("¿En qué año ocurrió el plebiscito?", "1988", "La ficha lo ubica el 5 de octubre de 1988."),
        ("¿Qué actor medió en el Acuerdo Nacional de 1985, según la ficha?", "La Iglesia Católica", "La ficha dice que el acuerdo se firmó con la mediación de la Iglesia.")],
    op=("Dibuja una línea de tiempo de 1973 a 1988 con la escala 1 cm = 3 años. Marca con su nombre: Vicaría de la Solidaridad (1976), crisis económica (1982), primeras protestas nacionales (1983), Acuerdo Nacional (1985), visita del papa (1987) y plebiscito (1988). Debajo, escribe una pregunta de investigación sobre la recuperación de la democracia que nombre al menos dos actores. {F}",
        "Posiciones desde 1973: 1 cm, 3 cm, 3,3 cm, 4 cm, 4,7 cm y 5 cm. Pregunta: «¿Cómo influyeron la crisis económica, las protestas y los acuerdos entre partidos en la recuperación de la democracia?».",
        ["respeta la escala", "ubica los seis hechos en orden", "la pregunta nombra dos actores o factores y se puede responder con evidencia"], ["línea de tiempo dibujada", "pregunta escrita"], ["ubicar los hechos sin medir", "escribir una pregunta que se responde con sí o no"],
        "Pide que explique por qué la recuperación de la democracia es un proceso y no un solo hecho."),
    reinforce="Explica en voz alta qué es un actor social y nombra dos actores del proceso con un hecho cada uno.",
    extend="Pregunta a una persona mayor de tu casa qué recuerda de los años ochenta y anota una frase con el año que mencione.",
)

# ---------------------------------------------------------------- OA 19, clase 2
F2 = ("Ficha 2 (tres fuentes de ejemplo escritas para este cuaderno; no son documentos reales). "
      "Fuente A, comunicado de ejemplo de una autoridad del gobierno militar, 1983: «Las protestas son obra de grupos minoritarios y el orden público está garantizado.» "
      "Fuente B, boletín de ejemplo de una parroquia de una población, 1984: «Esta semana las familias de la comunidad se reunieron para compartir comida y pedir que se acabe el desempleo.» "
      "Fuente C, nota de ejemplo de un periódico extranjero, 1985: «Varios partidos chilenos firmaron un acuerdo para pedir elecciones libres; el gobierno respondió que seguiría su calendario.»")
build(
    OA, 2, F2,
    use="Aprenderé a preguntar quién escribió una fuente, cuándo y para qué, y a decidir qué puede y qué no puede probar sobre los años ochenta.",
    prior=["Sé distinguir un hecho de una opinión.", "Conozco los actores del proceso de recuperación de la democracia.", "Sé que una fuente puede mostrar solo una parte de lo ocurrido."],
    explain=[
        "La procedencia de una fuente es su origen: quién la escribió, en qué fecha, dónde se publicó y con qué propósito. Una misma noticia se cuenta distinto si la escribe una autoridad, una parroquia o un periódico de otro país. Por eso, antes de usar una fuente, se responden esas preguntas.",
        "El propósito es lo que el autor quiere lograr: informar, convencer, defenderse o pedir ayuda. Un comunicado del gobierno puede querer mostrar control; un boletín de una comunidad, contar cómo viven sus familias; un diario extranjero, informar a lectores de otro país. Ninguna fuente muestra toda la realidad.",
        "Una fuente solo prueba lo que dice y lo que su autor pudo saber. Un boletín de una parroquia prueba lo que hizo una comunidad, no lo que hizo todo el país. Por eso se contrastan varias fuentes y la conclusión debe ser proporcional: no afirmar más de lo que la evidencia permite.",
    ],
    vocab=[("procedencia", "origen de una fuente: autor, fecha, lugar y propósito"), ("propósito", "lo que el autor quiere lograr con su texto"), ("contrastar", "comparar varias fuentes para ver en qué coinciden y en qué no"), ("comunicado", "texto breve que una autoridad o institución entrega al público"), ("proporcional", "que no afirma más de lo que la evidencia permite")],
    worked=[
        ("Describir la procedencia", "Una carta de ejemplo de un obrero, escrita en 1982 en una fábrica del sur, cuenta que lo despidieron. ¿Cuáles son su autor, año y lugar?", ["El autor es un obrero.", "El año es 1982 y el lugar, una fábrica del sur."], "Obrero, 1982, fábrica del sur"),
        ("Decir qué prueba una fuente", "La carta del obrero dice que lo despidieron en 1982. ¿Qué prueba y qué no?", ["Prueba la experiencia de ese obrero en esa fábrica.", "No prueba cuántos despidos hubo en todo el país."], "Prueba un caso concreto, no el total nacional"),
    ],
    mistakes=[("Aceptar una fuente como verdadera solo porque es oficial.", "Una autoridad también puede tener interés en mostrar una imagen favorable.", "Pregunta quién escribe, para qué y qué dicen otras fuentes."),
              ("Usar una fuente local para hablar de todo el país.", "Se generaliza más allá de lo que el autor pudo ver.", "Limita la conclusión al lugar y al grupo de la fuente.")],
    T=[
        ("{F} ¿Quién escribe la fuente A?", "Una autoridad del gobierno militar", "La ficha lo indica en su procedencia."),
        ("{F} ¿En qué año es la fuente B?", "1984", "La ficha fecha el boletín en 1984."),
        ("{F} ¿Dónde se publicó la fuente C?", "En un periódico extranjero", "La ficha la presenta como nota de un periódico de otro país."),
        ("{F} ¿Qué propósito probable tiene la fuente A? A) Mostrar que la situación está bajo control B) Convocar a una protesta", "A) Mostrar que la situación está bajo control", "El comunicado dice que el orden está garantizado, lo que defiende la imagen del gobierno."),
        ("{F} ¿Qué puede probar la fuente B? A) Que una comunidad se organizó en 1984 para ayudarse y pedir empleo B) Que todo el país se organizó igual", "A) Que una comunidad se organizó en 1984 para ayudarse y pedir empleo", "Una fuente local solo prueba lo que ocurrió en su comunidad."),
        ("{F} ¿Por qué puede ser útil la nota de un periódico extranjero? A) Registra el acuerdo y la respuesta del gobierno desde afuera del conflicto B) Porque un periódico extranjero siempre es neutral", "A) Registra el acuerdo y la respuesta del gobierno desde afuera del conflicto", "Ninguna fuente es perfecta, pero esta aporta una mirada externa."),
        ("{F} Quieres saber cómo vivían las familias de una población. ¿Qué fuente sirve más? A) La fuente B B) La fuente A", "A) La fuente B", "El boletín de la parroquia cuenta la vida de las familias de la comunidad."),
        ("{F} Quieres saber cómo respondió el gobierno al acuerdo de los partidos. ¿Qué fuente lo registra? A) La fuente C B) La fuente B", "A) La fuente C", "La nota extranjera dice que el gobierno respondió que seguiría su calendario."),
        ("{F} Un compañero cita la fuente A como prueba de que las protestas fueron pocas. ¿Qué respondes? A) Es un comunicado del propio gobierno y hay que contrastarlo con otras fuentes B) Tiene razón porque es una fuente oficial", "A) Es un comunicado del propio gobierno y hay que contrastarlo con otras fuentes", "Una autoridad puede minimizar un hecho; se necesita comparar fuentes."),
        ("{F} ¿Por qué conviene usar juntas las fuentes A, B y C?", "Porque cada una muestra una perspectiva distinta y permite contrastar", "Autor, propósito y lugar cambian en cada fuente."),
        ("{F} Un estudiante afirma que el boletín B se escribió por el acuerdo de la fuente C. ¿Qué error tiene? A) Un hecho de 1985 no puede causar un texto de 1984 B) Ninguno, porque ambos hablan de Chile", "A) Un hecho de 1985 no puede causar un texto de 1984", "La causa no puede ocurrir después del efecto."),
        ("{F} ¿Qué conclusión es proporcional a las tres fuentes? A) Entre 1983 y 1985 hubo miradas distintas: el gobierno minimizó las protestas, una comunidad se organizó y varios partidos pidieron elecciones B) Entre 1983 y 1985 el gobierno aceptó todo lo que pedían los partidos", "A) Entre 1983 y 1985 hubo miradas distintas: el gobierno minimizó las protestas, una comunidad se organizó y varios partidos pidieron elecciones", "La opción A solo afirma lo que las fuentes dicen; la B contradice la fuente C, que dice que el gobierno seguiría su calendario."),
        ("{F} Ordena de la más antigua a la más reciente: fuente C, fuente A, fuente B. ¿Cuál es el orden correcto? A) A, B, C B) B, A, C", "A) A, B, C", "La A es de 1983, la B de 1984 y la C de 1985."),
    ],
    ctx=("Una compañera quiere explicar los años ochenta usando solo el boletín de una parroquia de su barrio. ¿Qué limitación tendrá? A) Solo podrá hablar de esa comunidad, no de todo el país B) No podrá usar fechas", "A) Solo podrá hablar de esa comunidad, no de todo el país", "Una fuente local prueba lo ocurrido en su lugar; la conclusión debe ser proporcional."),
    sc=[("¿Qué es la procedencia de una fuente?", "Su origen: quién la escribió, cuándo, dónde y para qué", "Así se define en el vocabulario."),
        ("¿Qué significa contrastar fuentes?", "Compararlas para ver en qué coinciden y en qué no", "Contrastar es comparar fuentes."),
        ("Una autoridad publica un comunicado sobre una protesta. ¿Qué pregunta de procedencia es la más importante? A) ¿Para qué lo escribió? B) ¿Cuántas líneas tiene?", "A) ¿Para qué lo escribió?", "El propósito permite ver si defiende una imagen del gobierno.")],
    op=("Elige una de estas dos fuentes de ejemplo y analiza su procedencia con una tabla de cuatro filas: autor, fecha, propósito probable y qué puede probar. Fuente D, 1986, carta de ejemplo de una dirigente vecinal: «Pedimos que se escuche a las familias que perdieron su trabajo.» Fuente E, 1986, declaración de ejemplo de un ministro: «La economía mejora y el calendario político sigue su curso.» Escribe al final una frase que diga qué no puede probar la fuente que elegiste. {F}",
        "Fuente D: autor, una dirigente vecinal; fecha, 1986; propósito, pedir que se escuche a las familias; prueba que existía ese reclamo, pero no que todos pensaran igual.",
        ["responde las cuatro preguntas de procedencia", "el propósito es razonable", "dice un límite de la fuente"], ["tabla de cuatro filas", "frase con el límite de la fuente"], ["tratar la fuente como verdad completa", "no escribir el propósito"],
        "Pide que explique qué otra fuente usaría para contrastar la que eligió."),
    reinforce="Explica en voz alta por qué un comunicado del gobierno y un boletín de una parroquia pueden decir cosas distintas del mismo año.",
    extend="Busca en tu casa un documento con autor y fecha y anota su procedencia en tres datos.",
)

# ---------------------------------------------------------------- OA 19, clase 3
F3 = ("Ficha 3 (descripciones de ejemplo de 1984 desde distintas escalas y perspectivas). "
      "Escala local, una población de una ciudad: las familias organizan una olla común y una vigilia con ayuda de la parroquia. "
      "Escala nacional: dirigentes de varios partidos discuten cómo pedir elecciones libres sin usar la violencia. "
      "Escala internacional: una organización de derechos humanos de otro país publica un informe de ejemplo que pide al gobierno chileno respetar esos derechos. "
      "Perspectiva del gobierno militar: sostiene que el calendario político fijado en la Constitución de 1980 debe respetarse. "
      "Perspectiva de la oposición: pide adelantar las elecciones. "
      "Dato de ejemplo: en una encuesta en una población, 120 de 200 familias dicen que participaron en una actividad comunitaria.")
build(
    OA, 3, F3,
    use="Aprenderé a comparar cómo veían el proceso el gobierno, la oposición y otros actores, y a distinguir lo que se ve desde la escala local, nacional e internacional.",
    prior=["Sé situar los hechos de los años ochenta y sus actores.", "Sé que una fuente tiene procedencia y propósito.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Una perspectiva es la manera de ver un hecho desde la posición de un actor. En los años ochenta el gobierno militar defendía su calendario político, mientras la oposición pedía adelantar las elecciones. Describir ambas perspectivas no significa estar de acuerdo con las dos: significa explicar qué defendía cada una y con qué argumentos.",
        "La escala es el nivel desde el que se observa un hecho. En la escala local se ve cómo vivían las familias de una población; en la nacional, las decisiones de los partidos y del gobierno; en la internacional, lo que opinaban otros países y organizaciones. Cada escala muestra algo que las otras no ven.",
        "Un buen análisis compara perspectivas y escalas sin mezclarlas. Un dato local, como una encuesta en una población, no se puede aplicar a todo el país sin más. Por eso se dice qué grupo y qué lugar describe cada dato antes de generalizar.",
    ],
    vocab=[("perspectiva", "manera de ver un hecho desde la posición de un actor"), ("escala local", "nivel que observa un barrio, una población o una comunidad"), ("escala nacional", "nivel que observa decisiones y procesos de todo el país"), ("escala internacional", "nivel que observa la relación con otros países y organismos"), ("generalizar", "extender lo observado en un grupo a todos los demás")],
    worked=[
        ("Identificar una escala", "Un comité de vecinos de una población reparte alimentos. ¿Qué escala muestra?", ["Es un grupo de una comunidad.", "No habla de decisiones del país ni de otros países."], "Escala local"),
        ("Calcular un porcentaje", "En otra población de ejemplo, 30 de 50 vecinos fueron a una reunión. ¿Qué porcentaje es?", ["Multiplico por 100 y divido: 30 × 100 ÷ 50.", "El resultado es 60."], "60 %"),
    ],
    mistakes=[("Decir que todos pensaban lo mismo en 1984.", "Se ignoran las perspectivas distintas del gobierno y de la oposición.", "Nombra qué defendía cada actor."),
              ("Aplicar un dato de una población a todo el país.", "Se confunde la escala local con la nacional.", "Di a qué lugar y grupo corresponde el dato antes de generalizar.")],
    T=[
        ("{F} ¿A qué escala pertenece la olla común de la población?", "Escala local", "La ficha la ubica en una población de una ciudad."),
        ("{F} ¿Qué pide la oposición según la ficha?", "Adelantar las elecciones", "La ficha lo presenta como su perspectiva."),
        ("{F} ¿Qué perspectiva defiende el calendario fijado en la Constitución de 1980?", "La del gobierno militar", "La ficha se lo atribuye al gobierno militar."),
        ("{F} Dirigentes de varios partidos discuten cómo pedir elecciones libres. ¿Qué escala es? A) Escala nacional B) Escala local", "A) Escala nacional", "Se trata de decisiones políticas que afectan a todo el país."),
        ("{F} Una organización de otro país publica un informe sobre Chile. ¿Qué escala es? A) Escala internacional B) Escala local", "A) Escala internacional", "Viene de otro país y mira a Chile desde afuera."),
        ("{F} ¿Cuál es la diferencia central entre las dos perspectivas? A) El gobierno defiende su calendario y la oposición pide adelantar las elecciones B) Ambas piden exactamente lo mismo", "A) El gobierno defiende su calendario y la oposición pide adelantar las elecciones", "Esa diferencia está escrita en la ficha."),
        ("{F} Quieres explicar cómo afectó la crisis a las familias de un barrio. ¿Qué escala sirve más? A) La local B) La internacional", "A) La local", "La escala local muestra cómo vivían las familias."),
        ("{F} Quieres mostrar que otros países seguían el caso chileno. ¿Qué escala usarías? A) La internacional B) La local", "A) La internacional", "Se trata de la mirada de organizaciones de otros países."),
        ("=", "{F} ¿Qué porcentaje de las familias encuestadas participó en una actividad comunitaria?", "120*100/200", "Se divide 120 por 200 y se multiplica por 100.", " %"),
        ("{F} ¿Por qué una explicación hecha solo desde la escala nacional deja hechos fuera?", "Porque no muestra lo que vivían las familias ni lo que opinaban otros países", "La ficha muestra que las escalas local e internacional agregan datos distintos."),
        ("{F} Un compañero dice que gobierno y oposición no pueden compararse porque una es «buena» y otra «mala». ¿Qué se hace en historia? A) Describir qué defendía cada una, con qué argumentos y evidencia B) Elegir la que más simpatiza", "A) Describir qué defendía cada una, con qué argumentos y evidencia", "Comparar perspectivas exige explicar cada una con evidencia, no juzgarlas sin criterio."),
        ("{F} ¿Se puede afirmar con la encuesta que el 60 % de las familias de todo Chile participó en actividades comunitarias? A) No, el dato describe solo una población B) Sí, porque es una encuesta", "A) No, el dato describe solo una población", "La ficha dice que la encuesta se hizo en una población; generalizarla sería ir más allá del dato."),
        ("{F} Para explicar por qué crecía la presión por elecciones, ¿qué combinación es más completa? A) Escala local, nacional e internacional B) Solo escala local", "A) Escala local, nacional e internacional", "Cada escala aporta información que las otras no tienen."),
    ],
    ctx=("Una exposición dice: «En 1984 todos los chilenos querían lo mismo». ¿Qué falla tiene? A) Ignora que el gobierno y la oposición sostenían perspectivas distintas B) Mezcla la escala local con la internacional", "A) Ignora que el gobierno y la oposición sostenían perspectivas distintas", "La ficha muestra posiciones opuestas sobre el calendario político."),
    sc=[("¿Qué es una perspectiva?", "La manera de ver un hecho desde la posición de un actor", "Así se define en el vocabulario."),
        ("¿Qué escala observa un barrio o una población?", "La escala local", "Así se define en la clase."),
        ("=", "En un liceo de ejemplo, 45 de 60 estudiantes firmaron una carta. ¿Qué porcentaje es?", "45*100/60", "Se divide 45 por 60 y se multiplica por 100.", " %")],
    op=("Haz una tabla de tres filas (local, nacional, internacional) y tres columnas: qué se ve, qué actor aparece y qué no se puede saber desde esa escala. Usa los datos de la ficha. Después escribe dos frases: una que explique la perspectiva del gobierno y otra la de la oposición, con las palabras «según» y «argumenta». {F}",
        "Local: se ve una olla común, actor, las familias, no se sabe qué hacían los partidos. Frases: «Según el gobierno, el calendario de 1980 debe respetarse»; «La oposición argumenta que se deben adelantar las elecciones».",
        ["completa las tres escalas", "explica cada perspectiva con sus palabras", "no mezcla datos de escalas distintas"], ["tabla", "dos frases"], ["usar la misma frase para las dos perspectivas", "generalizar un dato local"],
        "Pide que explique qué fuente nueva necesitaría para completar la escala internacional."),
    reinforce="Explica en voz alta una diferencia entre la perspectiva del gobierno y la de la oposición en 1984.",
    extend="Anota un hecho de tu comuna que se vea distinto desde la escala local y desde la nacional.",
)

# ---------------------------------------------------------------- OA 19, clase 4
F4 = ("Ficha 4 (causas, cambios y continuidades). "
      "Causas de fondo: la crisis económica de 1982, que dejó empresas cerradas y desempleo; el descontento social; la acción de la Iglesia y de organismos de derechos humanos, que denunciaron violaciones y protegieron a las víctimas; la presión internacional. "
      "Detonante: las primeras protestas nacionales de 1983. "
      "Cambios: los partidos, prohibidos o en receso desde la década anterior, vuelven a actuar en la práctica y buscan acuerdos, como el de 1985; se abre la discusión pública sobre la salida política. "
      "Continuidades: sigue vigente la Constitución de 1980 con su calendario; Pinochet sigue al mando del gobierno; continúan las medidas represivas contra muchas protestas. "
      "Dato de ejemplo: de 400 personas con empleo en una población, 90 lo pierden en 1982.")
build(
    OA, 4, F4,
    use="Aprenderé a relacionar la crisis económica, las protestas y los acuerdos políticos como causas de un proceso, y a distinguir lo que cambió de lo que siguió igual.",
    prior=["Sé que un hecho tiene varias causas.", "Sé comparar perspectivas y escalas.", "Sé restar y calcular diferencias entre años."],
    explain=[
        "Una causa de fondo es un problema que se acumula con los años, como el desempleo y el descontento tras la crisis de 1982. Un detonante es el hecho que dispara el conflicto cuando esas causas ya existen: en este proceso, las primeras protestas nacionales de 1983. Separar ambas ideas evita decir que un solo día explica todo.",
        "En la década de 1980 hubo cambios: los partidos volvieron a actuar y se discutió públicamente cómo salir del gobierno militar. Pero también hubo continuidades: seguía vigente la Constitución de 1980, Pinochet continuaba al mando y muchas protestas fueron reprimidas. Un cambio no borra lo que seguía igual.",
        "Para relacionar causas se usan expresiones prudentes como «contribuyó a» o «ayudó a explicar». Decir «causó por sí sola» exige mucha evidencia. Además, que un hecho ocurra después de otro no prueba que el primero lo causara.",
    ],
    vocab=[("causa de fondo", "problema acumulado en el tiempo que prepara un conflicto"), ("detonante", "hecho que dispara un conflicto cuando ya existían causas"), ("cambio", "aspecto que se transforma entre un momento y otro"), ("continuidad", "aspecto que sigue igual a pesar de otros cambios"), ("represión", "uso de la fuerza para impedir o castigar una protesta")],
    worked=[
        ("Distinguir causa y detonante", "Una huelga estalla un día de abril tras años de salarios bajos. ¿Qué es la huelga y qué son los salarios bajos?", ["Los salarios bajos se acumularon con los años.", "La huelga fue el hecho que desató el conflicto."], "Salarios bajos, causa de fondo; huelga, detonante"),
        ("Clasificar un aspecto", "En una ciudad de ejemplo se abre un diario de oposición, pero la ley de prensa sigue igual. ¿Qué es cada cosa?", ["El diario nuevo es algo que se transforma.", "La ley que no cambia es lo que sigue."], "El diario es un cambio y la ley, una continuidad"),
    ],
    mistakes=[("Decir que las protestas de 1983 explican por sí solas el fin del gobierno militar.", "Se confunde el detonante con todas las causas de fondo.", "Nombra la crisis, el descontento, la Iglesia y la presión internacional."),
              ("Creer que si hubo cambios ya no había continuidades.", "Se piensa que un proceso cambia todo a la vez.", "Revisa qué seguía vigente: Constitución, mando y represión.")],
    T=[
        ("{F} ¿Qué crisis ocurrió en 1982?", "Una crisis económica", "La ficha la menciona como causa de fondo."),
        ("{F} ¿Qué hecho de 1983 se presenta como detonante?", "Las primeras protestas nacionales", "La ficha lo nombra como detonante."),
        ("{F} ¿Qué dos actores denunciaron violaciones de derechos humanos y protegieron a las víctimas?", "La Iglesia y los organismos de derechos humanos", "La ficha los nombra entre las causas de fondo."),
        ("=", "{F} ¿Cuántas personas con empleo conservaron su trabajo en la población del dato de ejemplo?", "400-90", "Se resta el número de despedidos al total.", " personas"),
        ("{F} La Constitución de 1980 sigue vigente. ¿Qué es? A) Una continuidad B) Un cambio", "A) Una continuidad", "Sigue igual a pesar de las protestas."),
        ("{F} Los partidos vuelven a actuar y firman un acuerdo en 1985. ¿Qué es? A) Un cambio B) Una continuidad", "A) Un cambio", "Antes estaban prohibidos o en receso y ahora actúan."),
        ("{F} ¿Cuál de estas es una causa de fondo y no un detonante? A) El descontento por la crisis y el desempleo B) Las protestas nacionales de 1983", "A) El descontento por la crisis y el desempleo", "El descontento se acumuló antes; las protestas fueron el hecho que lo hizo visible."),
        ("{F} Un titular dice: «Las protestas de 1983 explican por sí solas el fin del gobierno militar». ¿Qué corrección haces? A) Fueron el detonante, pero se sumaron crisis, Iglesia, partidos y presión internacional B) Es correcto porque ocurrieron antes de 1988", "A) Fueron el detonante, pero se sumaron crisis, Iglesia, partidos y presión internacional", "Ocurrir antes no prueba una causa única."),
        ("{F} ¿Qué continuidad respecto de la represión muestra la ficha? A) Siguieron las medidas represivas contra muchas protestas B) Las protestas se permitieron sin restricciones", "A) Siguieron las medidas represivas contra muchas protestas", "La ficha la enumera entre las continuidades."),
        ("{F} ¿Por qué decir «la crisis causó las protestas» es una simplificación?", "Porque la crisis fue una causa entre varias y también influyeron otros actores y descontentos", "La ficha nombra además la Iglesia, los organismos de derechos humanos y la presión internacional."),
        ("{F} En 1985 hay un acuerdo entre partidos, pero Pinochet sigue al mando. ¿Qué muestra? A) Que hubo cambios políticos junto a continuidades en el poder B) Que ya había terminado el gobierno militar", "A) Que hubo cambios políticos junto a continuidades en el poder", "La ficha dice que Pinochet seguía al mando."),
        ("{F} ¿Qué frase usa bien una expresión prudente? A) La crisis de 1982 contribuyó a aumentar el descontento que se expresó en 1983 B) La crisis de 1982 fue la única causa de todo", "A) La crisis de 1982 contribuyó a aumentar el descontento que se expresó en 1983", "«Contribuyó a» no exagera la evidencia."),
        ("Una carta de ejemplo de 1986 dice: «Ahora hay más reuniones y debates públicos, pero las reglas de la Constitución siguen iguales». ¿Cuál es el cambio y cuál la continuidad?", "Cambio: más reuniones y debates; continuidad: las reglas de la Constitución", "La carta separa lo que se transforma de lo que sigue igual."),
    ],
    ctx=("Un estudiante escribe: «En 1985 los partidos firmaron un acuerdo, así que ese año terminó el gobierno militar». ¿Qué falla tiene? A) Confunde un cambio político con el fin del gobierno, que aún continuaba B) Ubica el acuerdo antes de las protestas de 1983", "A) Confunde un cambio político con el fin del gobierno, que aún continuaba", "La ficha dice que Pinochet seguía al mando."),
    sc=[("¿Qué es un detonante?", "El hecho que dispara un conflicto cuando ya existían causas", "Así se define en el vocabulario."),
        ("¿Qué es una continuidad?", "Un aspecto que sigue igual a pesar de otros cambios", "Así se define en la clase."),
        ("=", "En una población de ejemplo hay 250 personas con empleo y 60 lo pierden. ¿Cuántas lo conservan?", "250-60", "Se resta el número de despidos al total.", " personas")],
    op=("Dibuja un esquema con «recuperación de la democracia» al centro. A la izquierda, tres causas de fondo; arriba, el detonante; a la derecha, un cambio y una continuidad. Debajo escribe una frase con «contribuyó a…» sobre el papel de la crisis de 1982. {F}",
        "Causas de fondo: crisis de 1982, descontento, acción de la Iglesia y los organismos de derechos humanos. Detonante: protestas de 1983. Cambio: vuelven los partidos. Continuidad: sigue la Constitución de 1980. Frase: «La crisis de 1982 contribuyó a aumentar el descontento».",
        ["separa causa de fondo y detonante", "incluye un cambio y una continuidad", "evita la causa única"], ["esquema", "frase con «contribuyó a…»"], ["poner el detonante como causa de fondo", "usar «causó por sí sola»"],
        "Pide que explique por qué un hecho posterior no prueba que fue causado por el anterior."),
    reinforce="Explica a alguien de tu casa la diferencia entre causa de fondo y detonante con un ejemplo de este tema.",
    extend="Piensa en una discusión que empezó por algo pequeño y anota qué causas de fondo la hicieron posible.",
)

# ---------------------------------------------------------------- OA 19, clase 5
F5 = ("Ficha 5 (evidencias de ejemplo escritas para este cuaderno). "
      "Pregunta de investigación: ¿qué factores permitieron recuperar la democracia en los años ochenta? "
      "Evidencia 1, informe de ejemplo de un organismo de derechos humanos, 1986: describe denuncias y apoyo a familias de personas perseguidas. "
      "Evidencia 2, columna de ejemplo de un economista, 1983: sostiene que la crisis económica quitó apoyo al gobierno entre sectores medios. "
      "Evidencia 3, acta de ejemplo de una reunión de partidos, 1985: acuerdan pedir elecciones libres y renunciar a la violencia. "
      "Hecho: el plebiscito del 5 de octubre de 1988 tuvo dos opciones, Sí y No, y ganó el No.")
build(
    OA, 5, F5,
    use="Aprenderé a construir una interpretación con una tesis, evidencias citadas con su procedencia y un contraargumento, sin afirmar más de lo que las fuentes permiten.",
    prior=["Sé analizar la procedencia de una fuente.", "Sé distinguir causas de fondo, detonantes, cambios y continuidades.", "Sé comparar perspectivas."],
    explain=[
        "Una interpretación documentada responde una pregunta con una tesis, que es una respuesta que se propone y se defiende. Cada razón de la tesis se apoya en una evidencia citada con su procedencia: quién la escribió, cuándo y de qué tipo es. Sin evidencia, una tesis es solo una opinión.",
        "Un contraargumento es una razón o evidencia que podría debilitar la tesis. Considerarlo no es un error: muestra que se revisó el tema con honestidad. Una tesis proporcional reconoce varios factores y sus límites; frases como «la única causa» o «lo explica todo» casi nunca se pueden sostener.",
        "Un párrafo bien armado sigue este orden: tesis, evidencia con su procedencia, contraargumento y conclusión. Si las evidencias muestran factores distintos, no alcanzan para decir cuál pesó más, salvo que haya datos que lo midan.",
    ],
    vocab=[("tesis", "respuesta que se propone a una pregunta y se defiende con evidencia"), ("evidencia", "información de una fuente que apoya o debilita una afirmación"), ("contraargumento", "razón o evidencia que podría debilitar la tesis"), ("interpretación", "explicación de un hecho apoyada en fuentes"), ("conclusión", "cierre que resume lo que la evidencia permite afirmar")],
    worked=[
        ("Reconocer una tesis", "«La participación de varios actores, y no solo de uno, contribuyó a recuperar la democracia». ¿Es una tesis o un dato?", ["Responde una pregunta y se puede defender con evidencia.", "Un dato sería una fecha o una cifra."], "Es una tesis"),
        ("Contar evidencias", "Un estudiante revisó 20 documentos: 8 hablan de economía y 7 de protestas. El resto habla de partidos. ¿Cuántos hablan de partidos?", ["Sumo los otros: 8 + 7 = 15.", "Resto: 20 − 15 = 5."], "5 documentos"),
    ],
    mistakes=[("Dar una tesis sin ninguna evidencia.", "Se confunde opinión con interpretación documentada.", "Cita al menos dos evidencias con su procedencia."),
              ("Usar solo las fuentes que apoyan la tesis.", "Se ignoran evidencias que muestran otros factores.", "Incluye un contraargumento y respóndelo.")],
    T=[
        ("{F} ¿Qué evidencia habla de la crisis económica?", "La evidencia 2", "La columna del economista de 1983 trata de la crisis."),
        ("{F} ¿Qué opciones tuvo el plebiscito de 1988?", "Sí y No", "La ficha las nombra."),
        ("{F} ¿Qué acordaron los partidos según la evidencia 3?", "Pedir elecciones libres y renunciar a la violencia", "El acta lo dice."),
        ("{F} ¿Qué es una tesis? A) Una respuesta que se propone a la pregunta y se defiende con evidencia B) Una lista de fechas", "A) Una respuesta que se propone a la pregunta y se defiende con evidencia", "Una tesis se defiende; una lista no responde la pregunta."),
        ("{F} ¿Qué es un contraargumento? A) Una razón que podría debilitar mi tesis y que debo considerar B) Repetir mi tesis con otras palabras", "A) Una razón que podría debilitar mi tesis y que debo considerar", "Repetir no aporta; el contraargumento muestra límites de la tesis."),
        ("{F} ¿Qué evidencia respalda mejor que los organismos de derechos humanos ayudaron a mantener el tema en discusión? A) La evidencia 1 B) La evidencia 2", "A) La evidencia 1", "El informe de 1986 describe denuncias y apoyo a familias."),
        ("{F} Tesis: «La crisis económica fue la única causa de la recuperación de la democracia». ¿Qué evidencias la debilitan? A) La 1 y la 3, que muestran otros factores B) La 2, que habla de la crisis", "A) La 1 y la 3, que muestran otros factores", "Si hay otros factores, la crisis no puede ser la única causa."),
        ("{F} ¿Cuál es una tesis proporcional? A) Varios factores se combinaron: la crisis, los acuerdos políticos y el apoyo de organismos de derechos humanos B) Solo importó el plebiscito", "A) Varios factores se combinaron: la crisis, los acuerdos políticos y el apoyo de organismos de derechos humanos", "Reconoce varios factores que las tres evidencias respaldan."),
        ("{F} ¿Sirve la evidencia 2 para probar por sí sola por qué ganó el No en 1988? A) No, es de 1983 y habla del apoyo entre sectores medios, no del resultado B) Sí, porque habla de la crisis", "A) No, es de 1983 y habla del apoyo entre sectores medios, no del resultado", "Una fuente solo prueba lo que dice y lo que su autor pudo saber."),
        ("{F} ¿Por qué las evidencias 1 y 3 no permiten decidir cuál factor pesó más?", "Porque cada una muestra un factor distinto y no mide cuánto pesó cada uno", "Para comparar pesos haría falta algún dato que los midiera."),
        ("{F} Un compañero dice que su tesis es cierta porque tiene tres fuentes que la apoyan. ¿Qué le falta? A) Considerar también fuentes que digan algo distinto B) Citar más fechas", "A) Considerar también fuentes que digan algo distinto", "Sin contraargumentos puede haber sesgo en la selección."),
        ("{F} ¿Cuál es el orden de un párrafo bien armado? A) Tesis, evidencia con procedencia, contraargumento y conclusión B) Conclusión, fecha, tesis y evidencia", "A) Tesis, evidencia con procedencia, contraargumento y conclusión", "Ese orden permite defender y revisar la tesis."),
        ("=", "Un estudiante revisó 40 documentos de 1983 a 1988: 16 hablan de protestas, 12 de acuerdos entre partidos y el resto de la ayuda a las víctimas. ¿Cuántos hablan de la ayuda a las víctimas?", "40-16-12", "Se restan los dos grupos conocidos al total.", " documentos"),
    ],
    ctx=("Una compañera escribe: «Como el No ganó en 1988, la crisis de 1982 lo explica todo». ¿Qué mejora le sugieres? A) Considerar también los acuerdos políticos y el apoyo de organismos de derechos humanos, con evidencias B) Citar solo fuentes de 1988", "A) Considerar también los acuerdos políticos y el apoyo de organismos de derechos humanos, con evidencias", "Un solo factor no se puede sostener con las tres evidencias de la ficha."),
    sc=[("En Historia: ¿Qué es una evidencia?", "Información de una fuente que apoya o debilita una afirmación", "Así se define en el vocabulario."),
        ("¿Para qué sirve incluir un contraargumento?", "Para mostrar los límites de la tesis y revisarla con honestidad", "Eso permite que la tesis sea proporcional."),
        ("=", "De 30 fuentes que revisó una estudiante, 18 destacan la crisis económica. ¿Cuántas no la destacan?", "30-18", "Se resta al total las fuentes que sí la destacan.", " fuentes")],
    op=("Escribe un párrafo de cinco o seis líneas que responda: ¿qué factores permitieron recuperar la democracia en los años ochenta? Debe incluir una tesis, dos evidencias de la ficha citadas con su procedencia (quién y año), un contraargumento y una conclusión que no use «la única causa». {F}",
        "Tesis: varios factores se combinaron. Evidencia: según una columna de ejemplo de un economista (1983), la crisis quitó apoyo al gobierno; según un acta de ejemplo (1985), los partidos acordaron pedir elecciones libres. Contraargumento: las evidencias no miden cuál factor pesó más.",
        ["la tesis responde la pregunta", "cita dos evidencias con procedencia", "incluye un contraargumento", "la conclusión es proporcional"], ["párrafo escrito"], ["afirmar una causa única", "citar sin decir quién ni cuándo"],
        "Pide que subraye la tesis, las evidencias y el contraargumento con tres colores."),
    reinforce="Explica en voz alta la diferencia entre una tesis y un dato, con un ejemplo de este tema.",
    extend="Busca en tu casa una noticia o un aviso y anota cuál es su afirmación principal y qué evidencia da.",
)

# ================================================================ OA 20
OA = "HI2M OA 20"

# ---------------------------------------------------------------- OA 20, clase 1
G1 = ("Ficha 6 (hechos y actores de la transición). "
      "La Constitución de 1980 comenzó a regir en 1981 y fijó un plebiscito para decidir si continuaba el candidato propuesto por la Junta de Gobierno. "
      "El 5 de octubre de 1988 se votó entre dos opciones: Sí, que Augusto Pinochet siguiera ocho años más; y No, que se convocara a elecciones libres de presidente y de parlamentarios. Ganó la opción No. "
      "En 1989 se votaron reformas a la Constitución acordadas entre el gobierno y la oposición y se realizaron elecciones presidencial y parlamentaria. En marzo de 1990 asumió la presidencia Patricio Aylwin. "
      "Actores: Junta de Gobierno, partidos de oposición reunidos en la Concertación de Partidos por el No, partidos de derecha, Fuerzas Armadas y votantes.")
build(
    OA, 1, G1,
    use="Aprenderé a situar el plebiscito de 1988 y los hechos de la transición hasta 1990, y a reconocer quiénes participaron.",
    prior=["Conozco los factores que permitieron recuperar la democracia en los años ochenta.", "Sé calcular diferencias entre años.", "Sé qué es un plebiscito: una votación directa sobre una decisión."],
    explain=[
        "La transición a la democracia es el período en que un país pasa de un gobierno autoritario a uno elegido por la ciudadanía. En Chile no ocurrió en un día: incluyó el plebiscito de 1988, las reformas y elecciones de 1989 y el cambio de gobierno en marzo de 1990. Por eso se la estudia como un proceso con varias etapas.",
        "La Constitución de 1980 fijaba que en 1988 se votara si continuaba el candidato propuesto por la Junta de Gobierno. La opción Sí significaba que Pinochet siguiera ocho años más; la opción No, que se convocara a elecciones libres. La oposición se agrupó para el No en la Concertación de Partidos por el No y ganó esa opción.",
        "Después del plebiscito, gobierno y oposición acordaron reformas a la Constitución, que se votaron en 1989, y se realizaron elecciones de presidente y de parlamentarios. En 1990 asumió Patricio Aylwin. Para estudiar el tema se ubica cada hecho en su fecha y se identifica quién lo impulsó.",
    ],
    vocab=[("transición", "paso de un gobierno autoritario a uno elegido por la ciudadanía"), ("plebiscito", "votación directa de la ciudadanía sobre una decisión"), ("Junta de Gobierno", "órgano militar que gobernó entre 1973 y 1990"), ("reforma constitucional", "cambio en el texto de la Constitución, aprobado por un procedimiento especial"), ("parlamentarios", "senadores y diputados que integran el Congreso")],
    worked=[
        ("Ordenar etapas", "El plebiscito, las elecciones de 1989 y la asunción de Aylwin son etapas de la transición. ¿Cuál fue primero?", ["Busco las fechas: octubre de 1988, 1989 y marzo de 1990.", "La más antigua es la de 1988."], "El plebiscito de 1988"),
        ("Interpretar una opción", "Una persona vota Sí en 1988. ¿Qué apoyaba?", ["La ficha dice qué significaba el Sí.", "Era que Pinochet siguiera ocho años más."], "Que Pinochet siguiera ocho años más"),
    ],
    mistakes=[("Creer que Pinochet dejó el gobierno el mismo día del plebiscito.", "Se confunde el resultado de una votación con el cambio de gobierno.", "Ubica el plebiscito en 1988 y la asunción de Aylwin en marzo de 1990."),
              ("Pensar que votar No era votar contra las elecciones.", "No se lee qué significaba cada opción.", "Recuerda que el No pedía elecciones libres.")],
    T=[
        ("{F} ¿Qué opciones tuvo el plebiscito de 1988?", "Sí y No", "La ficha las nombra."),
        ("{F} ¿Quién asumió la presidencia en marzo de 1990?", "Patricio Aylwin", "La ficha lo indica."),
        ("{F} ¿Qué opción ganó en el plebiscito?", "El No", "La ficha lo dice."),
        ("{F} ¿Qué fijó la Constitución de 1980 para decidir si continuaba el candidato propuesto por la Junta? A) Un plebiscito B) Una elección de parlamentarios", "A) Un plebiscito", "La ficha dice que la Constitución fijó un plebiscito."),
        ("{F} ¿Qué se votó en 1989, además de elegir presidente y parlamentarios? A) Reformas a la Constitución acordadas entre el gobierno y la oposición B) El regreso de la Junta de Gobierno", "A) Reformas a la Constitución acordadas entre el gobierno y la oposición", "La ficha lo indica; la Junta dejó el poder en 1990."),
        ("{F} Una persona marca Sí en 1988. ¿Qué apoyaba? A) Que Pinochet siguiera ocho años más B) Que se convocara a elecciones libres", "A) Que Pinochet siguiera ocho años más", "Eso significaba el Sí según la ficha."),
        ("{F} ¿Qué agrupación reunió a los partidos de oposición para el plebiscito? A) La Concertación de Partidos por el No B) La Junta de Gobierno", "A) La Concertación de Partidos por el No", "La Junta era el órgano militar; la agrupación opositora era la Concertación."),
        ("{F} ¿Cuál es el orden correcto? A) Plebiscito, reformas y elecciones de 1989, asunción de Aylwin B) Reformas y elecciones de 1989, plebiscito, asunción de Aylwin", "A) Plebiscito, reformas y elecciones de 1989, asunción de Aylwin", "El plebiscito fue en 1988, antes de 1989 y de 1990."),
        ("{F} Un compañero dice: «Al ganar el No, Pinochet dejó el gobierno al día siguiente». ¿Qué dato lo corrige? A) Hubo reformas y elecciones en 1989 y Aylwin asumió en marzo de 1990 B) El plebiscito fue un 5 de octubre", "A) Hubo reformas y elecciones en 1989 y Aylwin asumió en marzo de 1990", "El cambio de gobierno ocurrió más de un año después."),
        ("{F} ¿Por qué se dice que la transición fue un proceso y no un solo día?", "Porque incluyó plebiscito, reformas, elecciones y cambio de gobierno en años distintos", "La ficha ubica esos hechos entre 1988 y 1990."),
        ("{F} El plebiscito se hizo con reglas de la Constitución de 1980, redactada durante el gobierno militar. ¿Qué implica? A) La oposición usó reglas fijadas por el gobierno militar para lograr elecciones libres B) La oposición había escrito esas reglas", "A) La oposición usó reglas fijadas por el gobierno militar para lograr elecciones libres", "La ficha dice que la Constitución fijó el plebiscito."),
        ("{F} ¿Cuál es la mejor pregunta de investigación? A) ¿Cómo fue el paso del gobierno militar a un gobierno elegido entre 1988 y 1990? B) ¿Quién fue el mejor político de la transición?", "A) ¿Cómo fue el paso del gobierno militar a un gobierno elegido entre 1988 y 1990?", "La A tiene tema, tiempo y se responde con hechos."),
        ("{F} Una persona afirma: «Con el triunfo del No en 1988 ya estaba completa la transición». ¿Qué le falta considerar? A) Las reformas y elecciones de 1989 y el cambio de gobierno de 1990 B) Nada, porque el No ganó", "A) Las reformas y elecciones de 1989 y el cambio de gobierno de 1990", "La ficha muestra etapas posteriores al plebiscito."),
    ],
    ctx=("Un diario mural escolar titula «1988: el año en que se acabó todo el gobierno militar». ¿Qué falla tiene? A) Ignora que Aylwin asumió recién en 1990, después de las elecciones de 1989 B) Ubica el plebiscito en 1990", "A) Ignora que Aylwin asumió recién en 1990, después de las elecciones de 1989", "La ficha ubica la asunción en marzo de 1990."),
    sc=[("¿Qué es un plebiscito?", "Una votación directa de la ciudadanía sobre una decisión", "Así se define en el vocabulario."),
        ("¿Qué pedía la opción No?", "Que se convocara a elecciones libres de presidente y de parlamentarios", "La ficha lo indica."),
        ("¿Quién ejercía el poder entre el plebiscito de 1988 y marzo de 1990? A) La Junta de Gobierno B) Patricio Aylwin", "A) La Junta de Gobierno", "Aylwin asumió en marzo de 1990; hasta entonces gobernaba la Junta.")],
    op=("Dibuja una línea de tiempo de 1981 a 1990 con la escala 1 cm = 1 año. Marca con su nombre: inicio de la Constitución (1981), plebiscito (1988), reformas y elecciones (1989) y asunción de Aylwin (1990). Debajo, escribe qué significaba votar Sí y qué significaba votar No, y nombra dos actores de la transición. {F}",
        "Posiciones desde 1981: 0 cm, 7 cm, 8 cm y 9 cm. Sí: que Pinochet siguiera ocho años más. No: que se convocara a elecciones libres. Actores: Concertación de Partidos por el No y Junta de Gobierno.",
        ["respeta la escala", "ubica los cuatro hechos", "explica bien las dos opciones", "nombra dos actores"], ["línea de tiempo", "frases escritas"], ["confundir las opciones Sí y No", "poner la asunción en 1988"],
        "Pide que explique por qué la transición abarca más de un año."),
    reinforce="Explica en voz alta qué decidió el plebiscito de 1988 y qué ocurrió después, con las fechas.",
    extend="Pregunta a una persona mayor de tu casa si recuerda el plebiscito de 1988 y anota una frase, sin pedir más detalles de los que quiera contar.",
)

# ---------------------------------------------------------------- OA 20, clase 2
G2 = ("Ficha 7 (fuentes de ejemplo escritas para este cuaderno; no son documentos reales). "
      "Fuente A, mensaje de ejemplo de la campaña del No, 1988: «Vota No y elige a tus autoridades en elecciones libres.» "
      "Fuente B, mensaje de ejemplo de la campaña del Sí, 1988: «Vota Sí y mantén el orden y la estabilidad que el país necesita.» "
      "Fuente C, acta de ejemplo de una mesa de votación, 1988, firmada por los vocales de mesa: 250 inscritos; votos Sí, 90; votos No, 130; nulos y blancos, 5.")
build(
    OA, 2, G2,
    use="Aprenderé a preguntar quién produjo cada fuente sobre el plebiscito, para qué y qué puede probar: una campaña no es lo mismo que un acta de votación.",
    prior=["Sé analizar la procedencia de una fuente.", "Conozco los hechos del plebiscito de 1988.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Las fuentes del plebiscito de 1988 tienen propósitos distintos. Los mensajes de campaña, como los de la fuente A y la B, buscan convencer a las personas de votar de cierta manera. No sirven para saber qué pensaba cada votante, sino qué argumentos usaba cada lado para persuadir.",
        "Un acta de mesa es un documento donde los vocales de mesa, personas que supervisan la votación, anotan cuántos votos hubo. Su propósito es registrar un resultado, no persuadir. Pero un acta de una sola mesa solo prueba lo ocurrido en esa mesa: no entrega el resultado de todo el país.",
        "Al interrogar una fuente se pregunta: ¿quién la escribió?, ¿cuándo?, ¿para qué? y ¿qué puede probar? Luego se contrastan varias fuentes. La participación se calcula dividiendo los votantes por los inscritos y multiplicando por 100.",
    ],
    vocab=[("campaña", "conjunto de mensajes con que un grupo busca convencer a la ciudadanía de votar de una manera"), ("acta de mesa", "documento donde se anotan los votos contados en una mesa de votación"), ("vocal de mesa", "persona que supervisa una mesa de votación y cuenta los votos"), ("inscritos", "personas que figuran en el registro para poder votar"), ("participación", "porcentaje de inscritos que efectivamente vota")],
    worked=[
        ("Reconocer el propósito", "Un cartel de ejemplo dice: «Vota por la lista verde y asegura tu futuro». ¿Cuál es su propósito?", ["Pide votar por una opción.", "Su objetivo es convencer."], "Persuadir a votar"),
        ("Calcular participación", "En otra mesa de ejemplo con 200 inscritos votaron 150 personas. ¿Qué porcentaje participó?", ["Divido: 150 ÷ 200 = 0,75.", "Multiplico por 100: 75."], "75 %"),
    ],
    mistakes=[("Usar un mensaje de campaña como prueba del resultado.", "Se confunde un texto que persuade con un registro de votos.", "Para votos usa actas; para argumentos, mensajes de campaña."),
              ("Decir que una mesa muestra el resultado de todo el país.", "Se generaliza un dato local.", "Limita la conclusión a esa mesa o junta todas las actas.")],
    T=[
        ("{F} ¿Qué fuente es el acta de una mesa de votación?", "La fuente C", "La ficha la describe como acta firmada por vocales de mesa."),
        ("{F} ¿Cuántos votos No hubo en esa mesa?", "130", "El acta registra 130 votos No."),
        ("{F} ¿Quién produjo la fuente A?", "La campaña del No", "La ficha lo indica en su procedencia."),
        ("=", "{F} ¿Cuántos inscritos de esa mesa no votaron?", "250-(90+130+5)", "Se restan los votos emitidos al total de inscritos.", " personas"),
        ("=", "{F} ¿Cuántos votos más tuvo el No que el Sí en esa mesa?", "130-90", "Se resta el Sí al No.", " votos"),
        ("{F} ¿Cuál es el propósito de los mensajes A y B? A) Persuadir a las personas de votar de cierta manera B) Registrar cuántos votos hubo", "A) Persuadir a las personas de votar de cierta manera", "Son mensajes de campaña."),
        ("{F} ¿Qué puede probar el acta C? A) El resultado de esa mesa B) El resultado de todo el país", "A) El resultado de esa mesa", "Es un acta de una sola mesa."),
        ("{F} Quieres saber qué prometía la campaña del Sí. ¿Qué fuente usas? A) La fuente B B) La fuente C", "A) La fuente B", "La B es el mensaje de esa campaña."),
        ("{F} Un compañero afirma que el No ganó en todo el país porque ganó en el acta C. ¿Cuál es su error? A) El acta es de una sola mesa y el resultado nacional necesita todas las mesas B) Contó mal los votos nulos y blancos", "A) El acta es de una sola mesa y el resultado nacional necesita todas las mesas", "Una fuente local no permite generalizar."),
        ("{F} ¿Por qué los mensajes A y B no sirven para saber qué pensaban todos los votantes?", "Porque son mensajes de campaña hechos para persuadir, no registros de opiniones", "Su propósito es convencer, no medir."),
        ("{F} El acta C fue firmada por vocales de mesa. ¿Por qué es más adecuada para contar votos que un cartel de campaña? A) Porque registra un conteo y no busca persuadir B) Porque los vocales de mesa prefieren una opción", "A) Porque registra un conteo y no busca persuadir", "El propósito de cada fuente determina para qué sirve."),
        ("=", "{F} ¿Qué porcentaje de los inscritos de esa mesa votó?", "(90+130+5)*100/250", "Se suman los votos emitidos, se dividen por los inscritos y se multiplica por 100.", " %"),
        ("{F} ¿Qué conclusión es proporcional? A) En esa mesa de ejemplo ganó el No y las campañas ofrecieron mensajes distintos B) En todo Chile el No ganó por el mismo margen que en esa mesa", "A) En esa mesa de ejemplo ganó el No y las campañas ofrecieron mensajes distintos", "La B generaliza un dato de una sola mesa."),
    ],
    ctx=("Para un trabajo escolar, una compañera quiere probar qué porcentaje votó No en todo el país usando solo un mensaje de campaña. ¿Qué le sugieres? A) Usar las actas de todas las mesas, porque la campaña busca persuadir B) Usar el mismo mensaje, porque es una fuente oficial", "A) Usar las actas de todas las mesas, porque la campaña busca persuadir", "El conteo de votos está en las actas; el mensaje de campaña tiene otro propósito."),
    sc=[("¿Qué es un acta de mesa?", "Un documento donde se anotan los votos contados en una mesa de votación", "Así se define en el vocabulario."),
        ("¿Qué es la participación?", "El porcentaje de inscritos que efectivamente vota", "Así se define en la clase."),
        ("=", "En otra mesa de ejemplo, 168 de 200 inscritos votan. ¿Qué porcentaje de participación hay?", "168*100/200", "Se divide 168 por 200 y se multiplica por 100.", " %")],
    op=("Analiza esta fuente de ejemplo con cuatro preguntas (autor, fecha, propósito, qué puede probar). Fuente D, volante de ejemplo de un comité vecinal, 1988: «Revisa que estés inscrito y ve a votar con tu cédula; tu voto es secreto.» Después escribe una frase que diga qué no puede probar este volante. {F}",
        "Autor: un comité vecinal; fecha: 1988; propósito: informar y animar a votar; prueba que había información para votar, no cómo votó la gente.",
        ["responde las cuatro preguntas", "el propósito es razonable", "dice un límite de la fuente"], ["cuatro respuestas", "frase con el límite"], ["pensar que el volante muestra el resultado", "no decir el propósito"],
        "Pide que explique qué fuente usaría para saber el resultado en esa mesa."),
    reinforce="Explica en voz alta la diferencia entre un mensaje de campaña y un acta de mesa.",
    extend="Anota un aviso de tu entorno que busque convencer y di qué quiere que hagas.",
)

# ---------------------------------------------------------------- OA 20, clase 3
G3 = ("Ficha 8 (perspectivas y escalas de la transición; descripciones de ejemplo). "
      "Perspectiva 1, sectores partidarios del gobierno militar: defienden mantener la Constitución de 1980 con pocos cambios y el modelo económico. "
      "Perspectiva 2, partidos de oposición: proponen reformar la Constitución para ampliar la democracia, pero aceptan negociar esos cambios para asegurar la transición. "
      "Perspectiva 3, agrupaciones de familiares de víctimas de violaciones de derechos humanos: piden verdad y justicia. "
      "Escala local: en una población de ejemplo, los vecinos organizan comités para inscribirse en los registros electorales y acompañar la votación. "
      "Escala internacional: gobiernos de otros países observan y comentan el proceso. "
      "Dato de ejemplo: de 40 vecinos de una población, 28 se inscribieron en los registros.")
build(
    OA, 3, G3,
    use="Aprenderé a comparar cómo veían la transición los sectores partidarios del gobierno militar, la oposición y los familiares de víctimas, y a distinguir lo que muestran la escala local y la internacional.",
    prior=["Sé comparar perspectivas y escalas.", "Conozco el plebiscito de 1988 y las reformas de 1989.", "Sé calcular porcentajes sencillos."],
    explain=[
        "En la transición había perspectivas distintas. Los sectores partidarios del gobierno militar querían mantener la Constitución de 1980 con pocos cambios. Los partidos de oposición proponían reformarla y aceptaron negociar para asegurar el paso a la democracia. Las agrupaciones de familiares de víctimas pedían verdad y justicia sobre lo ocurrido.",
        "Estas posiciones podían coincidir en algunos puntos y chocar en otros. Por ejemplo, quienes ponían el foco en asegurar un acuerdo político y quienes pedían verdad y justicia no siempre tenían las mismas prioridades. Comparar no significa decidir quién tenía razón, sino explicar qué defendía cada actor y con qué argumentos.",
        "También hay que cambiar de escala. En la escala local se ve cómo las personas se organizaron para inscribirse y votar; en la nacional, las negociaciones políticas; en la internacional, cómo otros países observaron el proceso. Un dato de una población no se puede generalizar a todo el país.",
    ],
    vocab=[("perspectiva", "manera de ver un hecho desde la posición de un actor"), ("reformar", "cambiar parte de un texto o de una institución sin eliminarlos por completo"), ("verdad y justicia", "conocer lo ocurrido y que se determinen responsabilidades"), ("registro electoral", "lista de personas habilitadas para votar"), ("escala", "nivel desde el que se observa un hecho: local, nacional o internacional")],
    worked=[
        ("Asignar una frase a una perspectiva", "«Queremos saber qué pasó con nuestros seres queridos». ¿A qué perspectiva de la ficha corresponde?", ["Habla de saber lo ocurrido.", "Eso piden las agrupaciones de familiares."], "A la perspectiva 3, de familiares de víctimas"),
        ("Calcular un porcentaje", "En otra población de ejemplo, 36 de 45 vecinos se inscribieron. ¿Qué porcentaje es?", ["Divido 36 entre 45: 0,8.", "Multiplico por 100: 80."], "80 %"),
    ],
    mistakes=[("Creer que la oposición quería lo mismo que los partidarios del gobierno militar.", "Se ignora que proponía reformar la Constitución.", "Compara qué quería cada uno respecto de la Constitución."),
              ("Juzgar una perspectiva sin explicar sus argumentos.", "Se confunde comparar con tomar partido.", "Describe qué defiende cada actor antes de evaluar.")],
    T=[
        ("{F} ¿Qué piden las agrupaciones de familiares de víctimas?", "Verdad y justicia", "La ficha lo indica."),
        ("{F} ¿Qué proponen los partidos de oposición respecto de la Constitución?", "Reformarla para ampliar la democracia y negociar esos cambios", "La ficha lo dice en la perspectiva 2."),
        ("{F} ¿Qué defienden los sectores partidarios del gobierno militar?", "Mantener la Constitución de 1980 con pocos cambios y el modelo económico", "La ficha lo presenta en la perspectiva 1."),
        ("{F} Vecinos de una población se inscriben en los registros electorales. ¿Qué escala es? A) La local B) La internacional", "A) La local", "Es una acción de una comunidad."),
        ("{F} Gobiernos de otros países observan y comentan el proceso. ¿Qué escala es? A) La internacional B) La local", "A) La internacional", "Son actores de otros países."),
        ("{F} ¿Cuál es la diferencia entre las perspectivas 1 y 2? A) La 1 quiere mantener la Constitución con pocos cambios y la 2 quiere reformarla B) La 1 quiere reformarla y la 2 mantenerla", "A) La 1 quiere mantener la Constitución con pocos cambios y la 2 quiere reformarla", "Esa diferencia está en la ficha."),
        ("{F} Una declaración de ejemplo dice: «La democracia necesita saber qué ocurrió con las víctimas». ¿A qué perspectiva se parece? A) La de las agrupaciones de familiares B) La de los sectores partidarios del gobierno militar", "A) La de las agrupaciones de familiares", "Pide verdad, como la perspectiva 3."),
        ("{F} Otra declaración dice: «La Constitución actual funciona y no hay que tocarla». ¿A qué perspectiva se parece? A) La de los sectores partidarios del gobierno militar B) La de la oposición", "A) La de los sectores partidarios del gobierno militar", "Quiere mantenerla con pocos cambios."),
        ("=", "{F} ¿Qué porcentaje de los vecinos de la población se inscribió?", "28*100/40", "Se divide 28 por 40 y se multiplica por 100.", " %"),
        ("{F} ¿Por qué la perspectiva 3 puede chocar con quienes ponían el foco en asegurar el acuerdo político?", "Porque algunos priorizaban estabilizar el acuerdo y otros priorizaban conocer la verdad y obtener justicia", "Las prioridades eran distintas, aunque todas hablaban de la transición."),
        ("{F} Un estudiante dice: «La oposición quería lo mismo que sus adversarios». ¿Qué corrección haces? A) La oposición proponía reformar la Constitución, no mantenerla con pocos cambios B) Es correcto porque todos participaron en 1988", "A) La oposición proponía reformar la Constitución, no mantenerla con pocos cambios", "Participar en la misma votación no significa pensar igual."),
        ("{F} ¿Cuál es una comparación con criterio? A) Unos querían mantener la Constitución con pocos cambios, otros reformarla y otros priorizaban la verdad y la justicia B) Unos tenían razón y otros no", "A) Unos querían mantener la Constitución con pocos cambios, otros reformarla y otros priorizaban la verdad y la justicia", "La A describe cada posición; la B juzga sin explicar."),
        ("{F} ¿Se puede decir que el 70 % de los chilenos se inscribió usando el dato de la población? A) No, el dato es de una población y no se puede generalizar B) Sí, porque es un porcentaje", "A) No, el dato es de una población y no se puede generalizar", "Un dato local no representa a todo el país."),
    ],
    ctx=("Un compañero escribe: «Todos los chilenos pensaban lo mismo sobre el futuro político en 1988». ¿Qué falla tiene? A) Ignora que había perspectivas distintas sobre la Constitución y sobre la verdad y la justicia B) Menciona un año", "A) Ignora que había perspectivas distintas sobre la Constitución y sobre la verdad y la justicia", "La ficha presenta tres perspectivas diferentes."),
    sc=[("¿Qué es una perspectiva?", "La manera de ver un hecho desde la posición de un actor", "Así se define en el vocabulario."),
        ("¿Qué significa «verdad y justicia»?", "Conocer lo ocurrido y que se determinen responsabilidades", "Así se define en la clase."),
        ("=", "En un liceo de ejemplo, 24 de 30 estudiantes de tercero medio se informaron sobre el plebiscito. ¿Qué porcentaje es?", "24*100/30", "Se divide 24 por 30 y se multiplica por 100.", " %")],
    op=("Haz una tabla con las tres perspectivas de la ficha y tres columnas: qué defienden, con qué argumento posible y qué otra perspectiva podría discrepar. Luego escribe una frase que compare dos de ellas con «mientras que». No debes decidir cuál tiene razón. {F}",
        "Perspectiva 1: mantener la Constitución con pocos cambios; perspectiva 2: reformarla. Frase: «Los sectores partidarios del gobierno militar querían mantener la Constitución con pocos cambios, mientras que la oposición proponía reformarla».",
        ["describe las tres perspectivas", "la frase compara con «mientras que»", "no toma partido sin argumentos"], ["tabla", "frase de comparación"], ["mezclar las perspectivas", "decidir quién tiene razón sin evidencia"],
        "Pide que explique qué fuente nueva necesitaría para conocer mejor la perspectiva internacional."),
    reinforce="Explica en voz alta dos perspectivas de la ficha y una diferencia entre ellas.",
    extend="Anota un tema en que dos personas de tu entorno piensan distinto y cómo se puede conversar sin faltarse el respeto.",
)

# ---------------------------------------------------------------- OA 20, clase 4
G4 = ("Ficha 9 (causas, cambios y continuidades de la transición). "
      "Causas de una transición pactada: el camino fijado por la Constitución de 1980, que obligaba a usar un plebiscito; el triunfo del No en 1988; la negociación entre gobierno y oposición sobre reformas, aprobadas en 1989; el deseo de evitar la violencia. "
      "Cambios: se eligen presidente y parlamentarios en 1989; en marzo de 1990 asume Patricio Aylwin y se reabre el Congreso con parlamentarios elegidos. "
      "Continuidades: sigue vigente la Constitución de 1980, con reformas; Pinochet continúa como comandante en jefe del Ejército hasta 1998; hay senadores designados y no elegidos; se mantiene el sistema electoral binominal; continúa el modelo económico de mercado. "
      "Tensiones cívico-militares: episodios como el «ejercicio de enlace» de 1990 y el «boinazo» de 1993, en que el Ejército realizó movimientos de tropas. "
      "Consenso: los principales sectores políticos aceptan la democracia representativa (la ciudadanía elige a sus autoridades, que la representan) como sistema político. "
      "Dato de ejemplo: un Senado de 40 miembros tiene 32 elegidos y 8 designados.")
build(
    OA, 4, G4,
    use="Aprenderé a explicar por qué la transición fue pactada y a distinguir qué cambió con el regreso de autoridades elegidas y qué siguió igual, incluidas las tensiones cívico-militares.",
    prior=["Conozco los hechos de 1988 a 1990.", "Sé comparar perspectivas.", "Sé distinguir cambio y continuidad."],
    explain=[
        "Se habla de transición pactada porque el cambio se hizo siguiendo las reglas de la Constitución de 1980 y mediante acuerdos entre gobierno y oposición. Tras el triunfo del No, se negociaron reformas que se aprobaron en 1989. Esto permitió elegir autoridades, pero también dejó reglas heredadas de la etapa anterior.",
        "Entre los cambios están las elecciones de presidente y parlamentarios, la asunción de Patricio Aylwin en 1990 y la reapertura del Congreso. Entre las continuidades están la Constitución de 1980 con reformas, los senadores designados, el sistema electoral binominal, el modelo económico de mercado y la permanencia de Pinochet como comandante en jefe del Ejército hasta 1998.",
        "Las tensiones cívico-militares son las dificultades entre las autoridades civiles elegidas y las Fuerzas Armadas, que conservaron un peso institucional importante; se vieron en episodios como el «ejercicio de enlace» de 1990 y el «boinazo» de 1993. A la vez se formó un consenso: los principales sectores políticos aceptaron la democracia representativa, el sistema en que la ciudadanía elige a quienes la representan. Un cambio de gobierno no elimina de inmediato todas las reglas anteriores: por eso se evalúa por separado qué cambió y qué siguió igual.",
    ],
    vocab=[("transición pactada", "paso a la democracia basado en acuerdos entre gobierno y oposición y en las reglas vigentes"), ("senador designado", "senador que no es elegido por voto popular, sino nombrado según la Constitución de 1980"), ("sistema binominal", "sistema electoral con dos cargos por circunscripción, que favorecía a las dos primeras mayorías"), ("tensión cívico-militar", "dificultad entre autoridades civiles elegidas y las Fuerzas Armadas"), ("comandante en jefe", "máxima autoridad de una rama de las Fuerzas Armadas, como el Ejército"), ("democracia representativa", "sistema político en que la ciudadanía elige a las autoridades que la representan")],
    worked=[
        ("Clasificar un aspecto", "Se reabre el Congreso con parlamentarios elegidos. ¿Es cambio o continuidad?", ["Antes no había Congreso en funciones.", "Ahora vuelve con elegidos."], "Cambio"),
        ("Calcular un porcentaje", "Un Senado de ejemplo de 50 miembros tiene 10 designados. ¿Qué porcentaje son?", ["Divido 10 entre 50: 0,2.", "Multiplico por 100: 20."], "20 %"),
    ],
    mistakes=[("Decir que con la asunción de Aylwin terminó todo lo que venía de la etapa anterior.", "Se ignoran las continuidades institucionales.", "Revisa la Constitución, los senadores designados y el mando del Ejército."),
              ("Creer que «pactada» significa que todos estaban de acuerdo en todo.", "Se confunde acuerdo con unanimidad.", "Recuerda que hubo perspectivas distintas y tensiones.")],
    T=[
        ("{F} ¿Quién asume la presidencia en 1990, un cambio?", "Patricio Aylwin", "La ficha lo presenta como cambio."),
        ("{F} ¿Quién continúa como comandante en jefe del Ejército tras 1990?", "Pinochet", "La ficha lo indica."),
        ("{F} ¿Qué sistema electoral se mantiene?", "El binominal", "La ficha lo nombra entre las continuidades."),
        ("=", "{F} En el Senado de ejemplo, ¿qué porcentaje son los senadores designados?", "8*100/40", "Se divide 8 por 40 y se multiplica por 100.", " %"),
        ("En Historia: ¿qué es una democracia representativa?", "Un sistema político en que la ciudadanía elige a las autoridades que la representan", "Es la definición de la clase y el sistema sobre el que hubo consenso."),
        ("{F} Se reabre el Congreso con parlamentarios elegidos. ¿Qué es? A) Un cambio B) Una continuidad", "A) Un cambio", "Vuelve una institución con integrantes elegidos."),
        ("{F} Continúa el modelo económico de mercado. ¿Qué es? A) Una continuidad B) Un cambio", "A) Una continuidad", "Sigue igual, según la ficha."),
        ("{F} Existen senadores designados. ¿Qué muestra? A) Una continuidad con la institucionalidad heredada B) Un cambio completo hacia el voto popular", "A) Una continuidad con la institucionalidad heredada", "No son elegidos por voto popular."),
        ("{F} ¿Por qué la oposición participó en un plebiscito que regía la Constitución de 1980? A) Porque era el camino previsto y lo usó para lograr elecciones libres B) Porque la dictadura ya había terminado", "A) Porque era el camino previsto y lo usó para lograr elecciones libres", "La ficha dice que la Constitución fijó el plebiscito."),
        ("{F} ¿Por qué se habla de transición pactada?", "Porque gobierno y oposición negociaron reformas y el cambio siguió las reglas vigentes", "La ficha menciona la negociación y el camino de la Constitución de 1980."),
        ("{F} ¿Por qué la elección de 1989 no eliminó todas las tensiones cívico-militares? A) Porque Pinochet siguió al mando del Ejército y las Fuerzas Armadas conservaron peso institucional B) Porque la Constitución de 1980 fue derogada en 1990", "A) Porque Pinochet siguió al mando del Ejército y las Fuerzas Armadas conservaron peso institucional", "La ficha dice que continuó como comandante en jefe hasta 1998."),
        ("{F} Un estudiante dice: «Con aquellas elecciones se terminó todo lo de la etapa anterior». ¿Qué corrección haces? A) Hubo cambios, pero siguieron vigentes la Constitución con reformas, los senadores designados y el sistema binominal B) Tiene razón porque cambió el presidente", "A) Hubo cambios, pero siguieron vigentes la Constitución con reformas, los senadores designados y el sistema binominal", "La ficha enumera continuidades institucionales."),
        ("{F} ¿Qué evidencia permitiría probar que el peso militar continuó después de 1990? A) Que Pinochet siguiera como comandante en jefe hasta 1998 B) Que se realizaran elecciones en 1989", "A) Que Pinochet siguiera como comandante en jefe hasta 1998", "Muestra un mando militar que seguía vigente; las elecciones son un cambio."),
    ],
    ctx=("Un cartel escolar dice: «Con el plebiscito de 1988 y las elecciones de 1989, Chile quedó con una democracia sin ninguna limitación». ¿Qué falla tiene? A) Ignora los senadores designados, el sistema binominal y el mando militar que continuaron B) Usa fechas que no corresponden a ningún hecho de la ficha", "A) Ignora los senadores designados, el sistema binominal y el mando militar que continuaron", "La ficha enumera continuidades que limitaban a las autoridades elegidas."),
    sc=[("¿Qué es un senador designado?", "Un senador nombrado según la Constitución de 1980 y no elegido por voto popular", "Así se define en el vocabulario."),
        ("¿Qué es una tensión cívico-militar?", "Una dificultad entre autoridades civiles elegidas y las Fuerzas Armadas", "Así se define en la clase."),
        ("Un dirigente de derecha y una dirigente de izquierda coinciden en que las autoridades deben elegirse por voto. ¿Qué consenso muestran? A) En la democracia representativa como sistema político B) En mantener a Pinochet como presidente", "A) En la democracia representativa como sistema político", "Aceptar que la ciudadanía elige a sus autoridades es el consenso de la transición.")],
    op=("Haz una tabla con dos columnas, «Cambios» y «Continuidades», con al menos tres filas en cada una, usando la ficha. Luego escribe una frase con «aunque» que explique por qué se llama transición pactada. {F}",
        "Cambios: se eligen presidente y parlamentarios, asume Aylwin, se reabre el Congreso. Continuidades: Constitución con reformas, senadores designados, sistema binominal. Frase: «Aunque hubo elecciones, se mantuvieron reglas heredadas».",
        ["clasifica bien cambios y continuidades", "la frase usa «aunque» con sentido", "no afirma que todo cambió"], ["tabla", "frase"], ["poner un cambio como continuidad", "decir que todo terminó en 1990"],
        "Pide que explique por qué una continuidad no significa que no hubo cambios."),
    reinforce="Explica en voz alta qué significa transición pactada y da un cambio y una continuidad.",
    extend="Piensa en una regla de tu liceo que cambió y otra que siguió igual, y anota cuál fue cada una.",
)

# ---------------------------------------------------------------- OA 20, clase 5
G5 = ("Ficha 10 (evidencias de ejemplo escritas para este cuaderno). "
      "Pregunta: ¿qué logró y qué dejó pendiente la transición? "
      "Evidencia 1, columna de ejemplo de un dirigente de oposición, 1989: «Negociar reformas evitó un conflicto mayor y abrió el camino a elecciones.» "
      "Evidencia 2, carta de ejemplo de una agrupación de familiares de víctimas, 1990: «Se vuelve a votar, pero aún no sabemos qué ocurrió con nuestros seres queridos.» "
      "Evidencia 3, informe de ejemplo de un centro de estudios, 1991: «Persisten leyes y cargos heredados que limitan el poder de las autoridades elegidas.» "
      "Hecho: en 1990 se creó la Comisión Nacional de Verdad y Reconciliación, que entregó su informe en 1991.")
build(
    OA, 5, G5,
    use="Aprenderé a construir una interpretación documentada de la transición, con tesis, evidencias con procedencia y contraargumento, sin juzgar como éxito total ni fracaso total.",
    prior=["Sé armar una tesis con evidencia.", "Conozco cambios y continuidades de la transición.", "Sé que cada fuente tiene procedencia y propósito."],
    explain=[
        "Una interpretación documentada de la transición responde una pregunta con una tesis y con evidencias citadas. Las tres evidencias de la ficha muestran miradas distintas: un dirigente que valora la negociación, unos familiares que reclaman verdad y un centro de estudios que señala límites institucionales. Ninguna basta por sí sola.",
        "Para citar una evidencia hay que decir quién la escribió, en qué año y qué tipo de texto es. También hay que pensar su posición: un dirigente que participó en las negociaciones puede defenderlas, y una agrupación de familiares habla desde su experiencia. Eso no invalida sus textos, pero hay que considerarlo.",
        "Las tesis de «éxito total» o «fracaso total» son difíciles de sostener cuando las evidencias muestran logros y límites a la vez. Una tesis proporcional reconoce que hubo elecciones y acuerdos, junto a tareas pendientes. El contraargumento muestra que se revisaron las evidencias que no calzan.",
    ],
    vocab=[("tesis", "respuesta que se propone a una pregunta y se defiende con evidencia"), ("evidencia", "información de una fuente que apoya o debilita una afirmación"), ("contraargumento", "razón o evidencia que podría debilitar la tesis"), ("logro", "resultado positivo que se consiguió"), ("tarea pendiente", "asunto que quedó sin resolver")],
    worked=[
        ("Citar con procedencia", "Se quiere citar una frase de un informe de ejemplo de un centro de estudios de 1991. ¿Cómo se cita?", ["Se dice el tipo de texto y su autor.", "Se agrega el año."], "Según un informe de ejemplo de un centro de estudios (1991)…"),
        ("Contar tipos de fuentes", "En una muestra de 25 fuentes, 10 destacan logros, 9 destacan límites y el resto ambos. ¿Cuántas destacan ambos?", ["Sumo logros y límites: 10 + 9 = 19.", "Resto: 25 − 19 = 6."], "6 fuentes"),
    ],
    mistakes=[("Usar solo la evidencia que apoya la tesis.", "Se ignoran las evidencias que muestran límites.", "Incluye un contraargumento y respóndelo."),
              ("Concluir «fue un éxito total» o «un fracaso total».", "Las evidencias muestran logros y límites a la vez.", "Usa una tesis proporcional que nombre ambos.")],
    T=[
        ("{F} ¿Qué evidencia valora la negociación?", "La evidencia 1", "La columna del dirigente dice que negociar evitó un conflicto mayor."),
        ("{F} ¿Qué comisión se creó en 1990?", "La Comisión Nacional de Verdad y Reconciliación", "La ficha la nombra."),
        ("{F} ¿Qué dice la evidencia 3 que persiste?", "Leyes y cargos heredados", "El informe de 1991 lo señala."),
        ("{F} ¿Qué evidencias sustentan la idea de que la transición dejó límites? A) Las evidencias 2 y 3 B) Solo la evidencia 1", "A) Las evidencias 2 y 3", "La 2 habla de lo que no se sabe y la 3, de leyes heredadas."),
        ("{F} ¿Cuál es una tesis proporcional? A) La transición recuperó elecciones y acuerdos, pero dejó límites institucionales y tareas pendientes de verdad B) La transición fue un fracaso total", "A) La transición recuperó elecciones y acuerdos, pero dejó límites institucionales y tareas pendientes de verdad", "Reconoce logros y límites que las evidencias muestran."),
        ("{F} Alguien sostiene que la transición fue un éxito completo. ¿Qué evidencia sería su contraargumento más fuerte? A) La evidencia 3, que señala límites heredados B) La evidencia 1, que valora la negociación", "A) La evidencia 3, que señala límites heredados", "Muestra límites que desafían la idea de éxito completo."),
        ("{F} ¿Qué datos debes dar al citar la evidencia 3? A) Quién la escribió, el año y el tipo de texto B) Solo la frase", "A) Quién la escribió, el año y el tipo de texto", "Eso permite saber su procedencia."),
        ("{F} ¿Cuál es una buena forma de citar? A) Según un informe de ejemplo de un centro de estudios (1991), persisten leyes y cargos heredados B) Todo el mundo sabe que persisten leyes heredadas", "A) Según un informe de ejemplo de un centro de estudios (1991), persisten leyes y cargos heredados", "Atribuye la afirmación a una fuente con año."),
        ("{F} La evidencia 1 la escribe un dirigente de oposición. ¿Qué conviene considerar? A) Que participó en el proceso y puede defender lo negociado B) Que es neutral por escribir una columna", "A) Que participó en el proceso y puede defender lo negociado", "La posición del autor influye en lo que destaca."),
        ("{F} ¿Por qué una tesis de «éxito total» o «fracaso total» es difícil de sostener con estas evidencias?", "Porque las evidencias muestran logros y límites a la vez", "Hay elecciones y acuerdos junto a reclamos pendientes."),
        ("{F} Una compañera usa solo la evidencia 1. ¿Qué problema tiene su interpretación? A) Ignora las evidencias 2 y 3, que muestran límites B) Usa una columna de opinión, que nunca sirve como evidencia", "A) Ignora las evidencias 2 y 3, que muestran límites", "Selecciona solo la evidencia que apoya su tesis."),
        ("=", "Una estudiante revisó 30 fuentes sobre la transición: 12 destacan logros, 11 destacan límites y el resto ambos. ¿Cuántas destacan ambos?", "30-12-11", "Se restan los dos grupos conocidos al total.", " fuentes"),
        ("{F} ¿Qué conclusión es proporcional? A) Entre 1989 y 1991 se recuperaron las elecciones, pero quedaron límites heredados y reclamos de verdad sin resolver B) La transición dejó todo resuelto", "A) Entre 1989 y 1991 se recuperaron las elecciones, pero quedaron límites heredados y reclamos de verdad sin resolver", "Reúne los datos de las tres evidencias sin exagerar."),
    ],
    ctx=("Una alumna escribe: «La transición fue perfecta porque se votó en 1989». ¿Qué evidencia de la ficha puede mostrarle un límite? A) La evidencia 2 o la 3 B) Ninguna, porque votar basta", "A) La evidencia 2 o la 3", "Ambas muestran asuntos pendientes después de votar."),
    sc=[("¿Qué es un contraargumento?", "Una razón o evidencia que podría debilitar la tesis", "Así se define en el vocabulario."),
        ("¿Por qué conviene decir quién escribe una evidencia?", "Porque su posición y propósito influyen en lo que dice", "La procedencia ayuda a interpretar la fuente."),
        ("=", "De 20 documentos revisados, 12 destacan logros. ¿Cuántos no los destacan?", "20-12", "Se restan los que sí los destacan.", " documentos")],
    op=("Escribe un párrafo de cinco o seis líneas que responda: ¿qué logró y qué dejó pendiente la transición? Incluye una tesis, dos evidencias de la ficha con su procedencia (quién y año), un contraargumento y una conclusión que no diga «éxito total» ni «fracaso total». {F}",
        "Tesis: la transición recuperó las elecciones y los acuerdos, pero dejó límites. Evidencias: según una columna de ejemplo de 1989, negociar abrió el camino a elecciones; según un informe de ejemplo de 1991, persisten leyes heredadas. Contraargumento: la carta de familiares reclama verdad.",
        ["tesis clara", "dos evidencias con procedencia", "contraargumento", "conclusión proporcional"], ["párrafo escrito"], ["citar sin procedencia", "usar solo evidencias que apoyan"],
        "Pide que subraye la tesis, las evidencias y el contraargumento con tres colores."),
    reinforce="Explica en voz alta por qué es mejor una tesis que reconozca logros y límites que una de éxito o fracaso total.",
    extend="Elige una decisión de tu liceo y anota un logro y una tarea pendiente.",
)

# ---------------------------------------------------------------- OA 20, clase 6
G6 = ("Ficha 11 (políticas de reparación y debate; hechos y posturas de ejemplo). "
      "Hechos: en 1990 se creó la Comisión Nacional de Verdad y Reconciliación para esclarecer las violaciones de derechos humanos con resultado de muerte o desaparición cometidas hasta 1990; no tenía facultad para juzgar ni individualizar responsables, tarea que correspondía a los tribunales; entregó su informe en 1991 y el presidente Patricio Aylwin pidió perdón en nombre del Estado a las víctimas y sus familias. "
      "Se adoptaron medidas de reparación, como pensiones, atención de salud y apoyo educacional para familiares. "
      "En 2003 se creó otra comisión que reconoció a personas que sufrieron prisión política y tortura y entregó su informe en 2004. "
      "Pregunta de debate: ¿fue suficiente la reparación de los primeros años de la transición? "
      "Postura 1 (de ejemplo): fue un avance necesario pero insuficiente, porque faltó justicia. "
      "Postura 2 (de ejemplo): fue lo máximo posible en esas condiciones y evitó mayores tensiones. "
      "Dato de ejemplo: en un debate de 30 estudiantes, 18 apoyan la postura 1.")
build(
    OA, 6, G6,
    use="Aprenderé a debatir con respeto y con evidencia sobre las políticas de reparación de derechos humanos, reconociendo sus consecuencias y sus límites.",
    prior=["Conozco la transición y las tensiones cívico-militares.", "Sé que en la dictadura hubo violaciones de derechos humanos.", "Sé construir una tesis con evidencia."],
    explain=[
        "Reparar es reconocer el daño causado y compensarlo con medidas del Estado. Tras 1990 hubo comisiones que investigaron violaciones de derechos humanos, un informe entregado en 1991, un pedido de perdón en nombre del Estado y medidas como pensiones, atención de salud y apoyo educacional para familiares. En 2003 y 2004 otra comisión reconoció a personas que sufrieron prisión política y tortura.",
        "La reparación no es lo mismo que la justicia. La reparación reconoce y compensa el daño; la justicia determina responsabilidades. Por eso hubo posturas distintas sobre si las medidas fueron suficientes. Hay que hablar de estos temas con rigor y respeto, sin minimizar el sufrimiento de las víctimas.",
        "Un buen debate presenta una postura, la apoya con evidencia, considera el contraargumento y escucha sin burlarse. Si un tema te angustia, puedes pausar y hablar con una persona adulta de confianza. En este cuaderno los casos son de ejemplo y no se pide contar experiencias personales.",
    ],
    vocab=[("reparación", "conjunto de medidas del Estado para reconocer el daño y compensarlo"), ("comisión de verdad", "grupo creado para investigar y reconocer hechos de violaciones de derechos humanos"), ("justicia", "determinación de responsabilidades por parte de los tribunales"), ("pedir perdón en nombre del Estado", "reconocimiento público de la responsabilidad del Estado"), ("postura", "posición que se defiende en un debate con argumentos")],
    worked=[
        ("Distinguir reparación y justicia", "Una pensión para familiares de víctimas, ¿es reparación o justicia?", ["Compensa y reconoce un daño.", "No determina responsabilidades."], "Reparación"),
        ("Calcular un porcentaje", "En otro debate de ejemplo, 12 de 40 estudiantes apoyan una postura. ¿Qué porcentaje es?", ["Divido 12 entre 40: 0,3.", "Multiplico por 100: 30."], "30 %"),
    ],
    mistakes=[("Pensar que reparar es lo mismo que hacer justicia.", "Se confunde compensar un daño con determinar responsabilidades.", "Pregunta si la medida compensa o si establece responsables."),
              ("Descalificar a quien piensa distinto en el debate.", "Se confunde criticar un argumento con atacar a la persona.", "Responde al argumento y pide evidencia.")],
    T=[
        ("{F} ¿En qué año entregó su informe la Comisión Nacional de Verdad y Reconciliación?", "1991", "La ficha lo indica."),
        ("{F} ¿Qué hizo el presidente Aylwin al conocer el informe?", "Pidió perdón en nombre del Estado a las víctimas y sus familias", "La ficha lo registra."),
        ("{F} ¿Cuál de estas es una medida de reparación que menciona la ficha? A) Apoyo educacional para familiares B) Cierre del Congreso", "A) Apoyo educacional para familiares", "La ficha enumera pensiones, atención de salud y apoyo educacional."),
        ("{F} ¿Qué reconoció la comisión creada en 2003? A) A personas que sufrieron prisión política y tortura B) Solo a víctimas de muerte o desaparición", "A) A personas que sufrieron prisión política y tortura", "La de 1990 se ocupó de muerte y desaparición; la de 2003 amplió el reconocimiento."),
        ("{F} ¿Qué postura dice que faltó justicia? A) La postura 1 B) La postura 2", "A) La postura 1", "La ficha dice que fue un avance insuficiente porque faltó justicia."),
        ("{F} ¿Qué es una medida de reparación? A) Una acción del Estado para reconocer el daño y compensarlo B) Un castigo para los responsables", "A) Una acción del Estado para reconocer el daño y compensarlo", "El castigo corresponde a la justicia, no a la reparación."),
        ("{F} ¿Cuál es un argumento con evidencia? A) El informe de 1991 reconoció casos y se pidió perdón en nombre del Estado, aunque quedó trabajo pendiente B) Todos saben que no sirvió para nada", "A) El informe de 1991 reconoció casos y se pidió perdón en nombre del Estado, aunque quedó trabajo pendiente", "Se apoya en hechos de la ficha."),
        ("{F} En el debate, un compañero se burla de quien piensa distinto. ¿Qué es lo adecuado? A) Pedir que responda al argumento con respeto y evidencia B) Ignorarlo y seguir sin responderle", "A) Pedir que responda al argumento con respeto y evidencia", "Un debate se basa en razones, no en burlas."),
        ("{F} Si el tema del debate te produce angustia, ¿qué haces? A) Pausar y avisar a una persona adulta de confianza B) Callarlo para no molestar", "A) Pausar y avisar a una persona adulta de confianza", "Cuidar el bienestar emocional incluye pedir apoyo."),
        ("{F} ¿Por qué la reparación no reemplaza a la justicia?", "Porque la reparación compensa y reconoce el daño, mientras que la justicia determina responsabilidades", "Son funciones distintas, según la explicación."),
        ("{F} Un compañero dice: «Como hubo comisiones, el tema está cerrado». ¿Qué respuesta tiene argumento? A) Las comisiones aportaron verdad y reparación, pero siguieron las posturas sobre justicia y memoria B) Tiene razón porque hubo informes", "A) Las comisiones aportaron verdad y reparación, pero siguieron las posturas sobre justicia y memoria", "Reconoce el aporte sin afirmar que todo se resolvió."),
        ("=", "{F} ¿Qué porcentaje de los estudiantes del debate apoya la postura 1?", "18*100/30", "Se divide 18 por 30 y se multiplica por 100.", " %"),
        ("{F} ¿Qué afirmación es proporcional? A) Las medidas de los primeros años fueron un avance, aunque hay posturas que consideran que faltó justicia B) Las medidas resolvieron todo", "A) Las medidas de los primeros años fueron un avance, aunque hay posturas que consideran que faltó justicia", "Reconoce logros y la discusión pendiente."),
    ],
    ctx=("En un debate escolar, una compañera dice: «Reparar y hacer justicia es lo mismo». ¿Cómo la corriges? A) Reparar compensa y reconoce el daño; hacer justicia determina responsabilidades B) Tienes razón, son sinónimos", "A) Reparar compensa y reconoce el daño; hacer justicia determina responsabilidades", "Son conceptos distintos con funciones diferentes."),
    sc=[("¿Qué es la reparación?", "El conjunto de medidas del Estado para reconocer el daño y compensarlo", "Así se define en el vocabulario."),
        ("¿Qué regla básica sigue un debate respetuoso?", "Responder a los argumentos con evidencia y sin burlas", "Así se explica en la clase."),
        ("=", "En un curso de ejemplo de 40 estudiantes, 25 apoyan la postura 2. ¿Cuántos no la apoyan?", "40-25", "Se resta los que sí la apoyan al total.", " estudiantes")],
    op=("Prepara dos minutos de intervención en un debate sobre la pregunta de la ficha. Elige la postura 1 o la 2 y escribe: tu tesis, dos argumentos con evidencia de la ficha, un contraargumento y cómo lo responderás con respeto. No cuentes experiencias personales ni de tu familia. {F}",
        "Tesis (postura 1): la reparación fue un avance necesario pero insuficiente. Argumentos: el informe de 1991 y el perdón en nombre del Estado reconocieron el daño; faltó determinar responsabilidades. Contraargumento: hubo condiciones difíciles; respuesta: aun así quedaron tareas pendientes.",
        ["tesis clara", "dos argumentos con evidencia", "contraargumento respondido con respeto"], ["texto de intervención"], ["atacar a quien piensa distinto", "no usar evidencia"],
        "Pide que explique cómo sabría si cambió de opinión con nueva evidencia."),
    reinforce="Explica en voz alta la diferencia entre reparación y justicia con un ejemplo de la ficha.",
    extend="Anota tres reglas que ayudarían a conversar sobre un tema difícil sin faltar el respeto, y comparte una con una persona de tu casa.",
)
